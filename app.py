import os
import sys
import ctypes
import signal
import threading
import time
import webbrowser
import datetime
from PIL import Image
import pystray

from scraper import scrape
from webapp import app
from database import create_table, get_distinct_dates
from config import ensure_env_file, load_env

def is_admin():
    """Проверяет, запущено ли приложение с правами администратора."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    """Перезапускает программу с правами администратора."""
    if not is_admin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        sys.exit()

def resource_path(relative_path):
    """Получает путь к ресурсам, как в режиме разработки, так и в собранном виде."""
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def create_image():
    """Создает изображение для иконки в системном трее."""
    return Image.open(resource_path('github.ico'))

def run_flask():
    """Запускает Flask приложение."""
    app.run(port=5000, use_reloader=False)

def scrape_daily():
    """Запускает ежедневный сбор данных в 17:00, если нет записей на текущую дату."""
    scan_time_str = os.getenv('SCAN_TIME', '17:00')
    scan_hour, scan_minute = map(int, scan_time_str.split(':'))

    while not stop_event.is_set():
        now = datetime.datetime.now()
        date_str = now.strftime('%d.%m.%Y')

        # Определение следующего запуска
        next_run = now.replace(hour=scan_hour, minute=scan_minute, second=0, microsecond=0)
        if now >= next_run:
            # Если текущее время уже прошло, запускаем на следующий день
            next_run += datetime.timedelta(days=1)
        
        sleep_duration = (next_run - now).total_seconds()
        time.sleep(sleep_duration)  # Ждём до следующего запуска
        
        # После ожидания, проверяем наличие записей на текущую дату
        if date_str not in [d[0] for d in get_distinct_dates()]:
            scrape()

def on_quit(icon, item):
    """Обработчик для выхода из приложения."""
    stop_event.set()
    icon.stop()
    os.kill(os.getpid(), signal.SIGINT)

def on_open_url(icon, item):
    """Открывает веб-приложение в браузере."""
    webbrowser.open('http://127.0.0.1:5000')

def setup(icon):
    """Настраивает иконку в системном трее."""
    icon.visible = True

def start_icon():
    """Запускает иконку в системном трее."""
    icon = pystray.Icon('Trends', create_image(), title="GitHub Trends Archive by King Triton")
    icon.menu = pystray.Menu(
        pystray.MenuItem('Open Web App', on_open_url),
        pystray.MenuItem('Quit', on_quit)
    )
    icon.run(setup)

def main():
    """Основная логика приложения."""
    ensure_env_file()
    load_env()
    create_table()

    threading.Thread(target=scrape_daily, daemon=True).start()
    threading.Thread(target=start_icon, daemon=True).start()
    try:
        run_flask()
    except KeyboardInterrupt:
        stop_event.set()

if __name__ == "__main__":
    run_as_admin()
    stop_event = threading.Event()
    main()
