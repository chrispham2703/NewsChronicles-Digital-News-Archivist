📜 NewsChronicles: Digital News Archivist
A Python-based application for archiving and displaying news articles efficiently.


📌 Overview
NewsChronicles is a Python application that downloads, archives, and displays news articles in a user-friendly Tkinter GUI. It uses regular expressions (Regex) for parsing HTML/XML data and web scraping techniques to extract real-time news content.

🚀 Features
✅ Download & Archive News – Fetches the latest news from NBC News RSS feed.
✅ Graphical User Interface – Built with Tkinter for easy navigation.
✅ Search & Display – Allows users to view archived news stories with descriptions & images.
✅ Regex-Based Parsing – Extracts key details (title, date, description, image).
✅ Offline Viewing – Stores news locally for access even without an internet connection.

🛠 Installation
1️⃣ Clone the Repository
git clone git@github.com:chrispham2703/NewsChronicles-Digital-News-Archivist.git
cd NewsChronicles-Digital-News-Archivist
2️⃣ Run the Application
python NewsChronicles.py
📌 Ensure you have Python 3 installed before running the script.


📂 Project Structure

NewsChronicles-Digital-News-Archivist/
│── NewsChronicles.py          # Main Python script
│── NewsArchive/               # Folder containing archived news files
│── README.md                  # Project documentation
│── requirements.txt            # Dependencies (if needed)
└── NBC_News_Logo.png          # Logo used in the GUI
📡 How It Works
User launches the app.

News is fetched from NBC News RSS feed.

Regex extracts news titles, links, descriptions, and images.

News is displayed in the Tkinter GUI.

Users can view archived news or fetch the latest updates.

📜 Technologies Used
Python 3 – Core programming language

Tkinter – GUI framework

Regular Expressions (Regex) – Data extraction

urllib.request – Fetching web data

datetime – Formatting timestamps

💡 Future Improvements
✅ Add keyword-based search for archived news.
✅ Implement database storage instead of text-based files.
✅ Improve UI with modern styling (Tkinter.ttk).
✅ Introduce multi-language support for international news.

📜 License
This project is licensed under the MIT License – feel free to modify and use it.

👨‍💻 Author
👤 Van Truong Pham (Christopher)
📧 LinkedIn Profile
📌 GitHub Profile

🔗 Repository Link
🌍 GitHub Repo: NewsChronicles-Digital-News-Archivist

✨ Happy Coding! 🚀🔥
📌 How to Save This?
Create a new file in your project folder:

touch README.md
Open it in a text editor (VS Code, Sublime, etc.), and paste the content above.

Save and push it to GitHub:

git add README.md
git commit -m "Added README.md"
git push origin main

Let me know if you want any modifications! 🚀
