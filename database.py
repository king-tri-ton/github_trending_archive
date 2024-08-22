import sqlite3
import os
from config import ensure_db_file

# Убедитесь, что файл базы данных существует
ensure_db_file()

def create_connection():
    # Получаем путь к базе данных из переменной окружения
    db_path = os.getenv('DATABASE_PATH')
    return sqlite3.connect(db_path)

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS trends (
            date TEXT,
            language TEXT,
            project_name TEXT,
            description TEXT,
            project_url TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_trends(date, language, project_name, description, project_url):
    conn = create_connection()
    c = conn.cursor()
    
    c.execute('''
        SELECT 1 FROM trends
        WHERE date = ? AND language = ? AND project_name = ? AND description = ? AND project_url = ?
    ''', (date, language, project_name, description, project_url))
    
    if not c.fetchone():  # Если запись не найдена
        c.execute('''
            INSERT INTO trends (date, language, project_name, description, project_url)
            VALUES (?, ?, ?, ?, ?)
        ''', (date, language, project_name, description, project_url))
        conn.commit()
    
    conn.close()

def get_distinct_dates():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT DISTINCT date FROM trends ORDER BY date DESC')
    dates = c.fetchall()
    conn.close()
    return dates

def get_trends_by_date(date):
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT language, project_name, project_url, description FROM trends WHERE date = ? ORDER BY language', (date,))
    projects = c.fetchall()
    conn.close()
    return projects
