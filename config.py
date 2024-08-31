import os
from dotenv import load_dotenv

# Путь к файлу .env
ENV_FILE_PATH = r'C:\Program Files\King-Triton\GTA\.env'

def ensure_env_file():
    """Проверяет, существует ли .env файл и создаёт его, если нет."""
    env_dir = os.path.dirname(ENV_FILE_PATH)

    # Проверяем, существует ли директория, и создаем её, если нет
    if not os.path.exists(env_dir):
        os.makedirs(env_dir)

    # Проверяем, существует ли файл .env, и создаем его, если нет
    if not os.path.exists(ENV_FILE_PATH):
        with open(ENV_FILE_PATH, 'w') as file:
            file.write('SCAN_TIME=17:00\n')  # Пример начальных значений
            file.write('DATABASE_PATH=C:\\Program Files\\King-Triton\\GTA\\trends.db\n')  # Путь к базе данных
            file.write('LANGUAGES=python,java,javaScript\n')  # Пример языков

def load_env():
    """Загружает переменные окружения из .env файла."""
    load_dotenv(ENV_FILE_PATH)

def get_languages():
    """Получает список языков из переменной окружения."""
    # Убедитесь, что переменные окружения загружены
    load_env()  # Загружаем переменные окружения из .env файла
    languages = os.getenv('LANGUAGES', '')
    return [lang.strip() for lang in languages.split(',') if lang.strip()]

def ensure_db_file():
    """Проверяет, существует ли файл базы данных и создает его, если нет."""
    # Загружаем переменные окружения из .env файла
    load_env()

    # Получаем путь к базе данных из переменной окружения
    db_path = os.getenv('DATABASE_PATH')

    if not db_path:
        raise ValueError("DATABASE_PATH не задан в .env файле")

    # Проверяем, существует ли директория, и создаем её, если нет
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)

    # Проверяем, существует ли файл базы данных, и создаем его, если нет
    if not os.path.exists(db_path):
        with open(db_path, 'w'):  # Создаем пустой файл базы данных
            pass
