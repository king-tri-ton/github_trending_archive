from PIL import Image
import pystray
import threading
import time
import webbrowser
import signal
import os
import datetime
from scraper import scrape
from webapp import app
from database import create_table

# Глобальный флаг для остановки
stop_event = threading.Event()

def create_image():
    # Загрузка изображения из файла
    return Image.open('github.png')

def run_flask():
    # Запускаем Flask приложение
    app.run(port=5000, use_reloader=False)

def scrape_daily():
    while not stop_event.is_set():
        now = datetime.datetime.now()
        # Рассчитываем время до следующего запуска (23:00)
        next_run = now.replace(hour=23, minute=0, second=0, microsecond=0)
        if now >= next_run:
            next_run += datetime.timedelta(days=1)
        
        # Вычисляем разницу во времени
        sleep_duration = (next_run - now).total_seconds()
        time.sleep(sleep_duration)
        
        # Запускаем парсер
        scrape()

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
    icon = pystray.Icon('Trends', create_image())
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
