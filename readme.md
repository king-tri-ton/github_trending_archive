# GitHub Trending Archive

![github](https://github.com/user-attachments/assets/142a537b-b895-4df7-b2ed-bdec6f224cfa)

GitHub Trending Archive is an application that collects information about popular GitHub repositories daily and saves it to a database. With this application, you can track changes in trends for selected programming languages.

## Project Structure

- **app.py**: The main script that launches the Flask application and the system tray icon. It also initiates daily trend data collection.
- **config.py**: Configuration parameters, including the path to the `.env` file and application settings.
- **database.py**: Functions for interacting with the SQLite database, including table creation and data insertion.
- **scraper.py**: A script for scraping data from GitHub trending pages and saving it to the database.
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

   For version 1.0.4 and later, create a `.env` file in the `C:\Program Files\King-Triton\GTA` directory and specify the parameters:
   ```
   SCAN_TIME=17:00
   DATABASE_PATH=C:\\Program Files\\King-Triton\\GTA\\trends.db
   LANGUAGES=python,java,javaScript
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

   This will start the Flask server and the system tray icon. The application will automatically collect trend data daily at 03:00.

## Usage

- **System Tray:** Right-click the icon in the system tray to open or close the web application.
- **Web Interface:** Open a browser and go to `http://127.0.0.1:5000` to view available trend dates and information.

## Screenshots

Here are some screenshots of the web application:

1. ![Screenshot_67](https://github.com/user-attachments/assets/c5c64667-72f4-463a-9ff4-078bf75d9071)
2. ![Screenshot_68](https://github.com/user-attachments/assets/c1ea8b75-ba77-4ec2-990a-fdc42478fad2)
3. ![Screenshot_69](https://github.com/user-attachments/assets/46aca1b7-64de-42da-99f6-a605ff0bb3cd)

## Future Plans

1. **Trend Analysis with AI:** Integration with OpenAI API for trend analysis and providing additional insights.

2. **Installer with Configuration Wizard:** Creating an installer with a graphical configuration tool for selecting programming languages and setting other parameters without manually editing files.

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).

## Author’s Note

I came across an interesting project called [GitHub Trending Archive](https://github.com/frodeaa/github_trending_archive) but couldn't get it running on Windows. I liked the project’s website ([archive](https://archive.faabli.com/)), and after some thought, I decided to create a similar project entirely in Python. I think it turned out great. Thanks to [@frodeaa](https://github.com/frodeaa) for the inspiration!

## Contact

If you have any questions or suggestions, feel free to reach out to me via [telegram](https://t.me/king_triton).