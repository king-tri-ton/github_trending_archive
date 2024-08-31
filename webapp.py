from flask import Flask, render_template
from database import get_distinct_dates, get_trends_by_date

app = Flask(__name__)

@app.route('/')
def index():
    dates = get_distinct_dates()
    return render_template('index.html', dates=[d[0] for d in dates])

@app.route('/<date>')
def trends(date):
    projects = get_trends_by_date(date)

    # Группируем проекты по языкам
    projects_by_language = {}
    for language, project_name, project_url, description in projects:
        if language not in projects_by_language:
            projects_by_language[language] = []
        projects_by_language[language].append((project_name, project_url, description))

    return render_template('trends.html', date=date, projects_by_language=projects_by_language)

if __name__ == '__main__':
    app.run(port=5000)
