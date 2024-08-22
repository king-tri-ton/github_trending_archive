import os
from dotenv import load_dotenv

def ensure_env_file():
    # Путь к директории и файлу .env
    env_dir = r'C:\Program Files\King-Triton\GTA'
    env_file_path = os.path.join(env_dir, '.env')

    # Проверяем, существует ли директория, и создаем её, если нет
    if not os.path.exists(env_dir):
        os.makedirs(env_dir)

    # Проверяем, существует ли файл .env, и создаем его, если нет
    if not os.path.exists(env_file_path):
        with open(env_file_path, 'w') as file:
            file.write('SCAN_TIME=17:00\n')  # Пример начальных значений
            file.write('DATABASE_PATH=C:\\Program Files\\King-Triton\\GTA\\trends.db\n')  # Путь к базе данных
            file.write('LANGUAGES=python,java,javaScript\n')  # Пример языков

def ensure_db_file():
    # Загружаем переменные окружения из .env файла
    load_dotenv()

    # Получаем путь к базе данных из переменной окружения
    db_path = os.getenv('DATABASE_PATH')
    
    # Проверяем, существует ли директория, и создаем её, если нет
    db_dir = os.path.dirname(db_path)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    # Проверяем, существует ли файл базы данных, и создаем его, если нет
    if not os.path.exists(db_path):
        with open(db_path, 'w'):  # Создаем пустой файл базы данных
            pass

def get_languages():
    load_dotenv()
    languages = os.getenv('LANGUAGES', '')
    return [lang.strip() for lang in languages.split(',') if lang.strip()]

def load_env():
    # Путь к файлу .env
    env_file_path = r'C:\Program Files\King-Triton\GTA\.env'
    load_dotenv(env_file_path)
