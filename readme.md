# GitHub Trending Archive

![github](https://github.com/user-attachments/assets/142a537b-b895-4df7-b2ed-bdec6f224cfa)

GitHub Trending Archive is an application that daily collects information about popular repositories on GitHub and stores it in a database. With this application, you can track changes in trends for selected programming languages.

## Project Structure

- **app.py**: The main script that launches the Flask application and the system tray icon. It also initiates daily trend parsing.
- **config.py**: Configuration parameters, including the API token (needed in the future) and a list of programming languages.
- **database.py**: Functions for interacting with the SQLite database, including table creation and data insertion.
- **scraper.py**: Script for scraping the GitHub trends page and saving data to the database.
- **webapp.py**: Flask application for displaying trend data through a web interface.
- **templates/**: Directory containing HTML templates for the web application.

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/king-tri-ton/github_trending_archive.git
   cd github_trending_archive
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure settings:**
   Edit the `config.py` file to specify your OpenAI API token and the list of programming languages. For example:
   ```python
   AI_TOKEN = 'sk-your_token'
   LANGUAGE = [
       "python",
       "php",
       "javascript"
   ]
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

   This will start the Flask server and the system tray icon. The application will automatically collect trend data daily at 03:00 AM.

## Usage

- **System Tray:** Right-click the icon in the system tray to open or close the Flask application.
- **Web Interface:** Open your browser and go to `http://127.0.0.1:5000` to view available trend dates and information.

## Screenshots

Here are some screenshots of the web application:

1. ![Screenshot_67](https://github.com/user-attachments/assets/c5c64667-72f4-463a-9ff4-078bf75d9071)
2. ![Screenshot_68](https://github.com/user-attachments/assets/c1ea8b75-ba77-4ec2-990a-fdc42478fad2)
3. ![Screenshot_69](https://github.com/user-attachments/assets/46aca1b7-64de-42da-99f6-a605ff0bb3cd)

## Future Plans

1. **Trend Analysis with AI:**
   I plan to integrate with the OpenAI API for analyzing and providing additional insights on trends.

2. **Installer with Configuration Wizard:**
   I plan to create an installer with a graphical configuration tool to allow users to select programming languages and adjust other settings without editing files manually.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Author's Note

I came across an interesting project called [GitHub Trending Archive](https://github.com/frodeaa/github_trending_archive) but couldn't get it running on my Windows. I liked the project’s website ([archive](https://archive.faabli.com/)), and after some thought, I decided to create a similar project entirely in Python. I think it turned out great. Thanks to [@frodeaa](https://github.com/frodeaa) for the inspiration!

## Contacts

If you have any questions or suggestions, feel free to contact me via [telegram](https://t.me/king_triton).