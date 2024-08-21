from PIL import Image
import pystray
import threading
import time
import webbrowser
import signal
import os
import sys
import datetime
from scraper import scrape
from webapp import app
from database import create_table, get_distinct_dates

# Глобальный флаг для остановки
stop_event = threading.Event()

def resource_path(relative_path):
    """ Получает путь к ресурсам, как в режиме разработки, так и в собранном виде """
    try:
        # Если запущено как исполняемый файл
        base_path = sys._MEIPASS
    except AttributeError:
        # Если запущено из исходного кода
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def create_image():
    return Image.open(resource_path('github.ico'))

def run_flask():
    # Запускаем Flask приложение
    app.run(port=5000, use_reloader=False)

def scrape_daily():
    while not stop_event.is_set():
        now = datetime.datetime.now()
        date_str = now.strftime('%d.%m.%Y')
        
        # Проверяем, есть ли записи с сегодняшней датой
        dates = [d[0] for d in get_distinct_dates()]
        
        if date_str not in dates:
            # Сбор данных, если записи отсутствуют
            scrape()

        # Рассчитываем время до следующего запуска (03:00)
        next_run = now.replace(hour=3, minute=0, second=0, microsecond=0)
        if now >= next_run:
            next_run += datetime.timedelta(days=1)
        
        # Вычисляем разницу во времени
        sleep_duration = (next_run - now).total_seconds()
        time.sleep(sleep_duration)

def on_quit(icon, item):
    stop_event.set()
    icon.stop()
    # Убедитесь, что сервер также остановлен
    os.kill(os.getpid(), signal.SIGINT)

def on_open_url(icon, item):
    webbrowser.open('http://127.0.0.1:5000')

def setup(icon):
    icon.visible = True

def start_icon():
    icon = pystray.Icon('Trends', create_image(), title="GitHub Trends Archive by king_tri_ton")
    icon.menu = pystray.Menu(
        pystray.MenuItem('Open Web App', on_open_url),
        pystray.MenuItem('Quit', on_quit)
    )
    icon.run(setup)

if __name__ == "__main__":
    # Создаем таблицу в базе данных
    create_table()

    # Запускаем Flask приложение и иконку в системном трее в отдельных потоках
    threading.Thread(target=scrape_daily, daemon=True).start()
    threading.Thread(target=start_icon, daemon=True).start()
    try:
        run_flask()
    except KeyboardInterrupt:
        stop_event.set()
