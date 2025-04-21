#  Companion API + Automation

This project includes a simple RESTful Flask API that serves random cat facts & random cat breeds and a Selenium script to automate interaction with the API.

---

## 📁 Project Structure

```
API Creation & Web Automation/
├── API/
│   └── api.py               # Flask API
├── Web Automation/
│   └── WebAutomation.py       # Selenium script
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

### 1. open the folder

### 2. Create a Virtual Environment

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Flask API

```bash
cd API
python api.py
```

- Visit [http://127.0.0.1:5000/fact](http://127.0.0.1:5000/fact) for a JSON cat fact.
- Visit [http://127.0.0.1:5000/home](http://127.0.0.1:5000/home) for an HTML cat fact.
- Visit [http://127.0.0.1:5000/breeds](http://127.0.0.1:5000/home) for an HTML cat breeds.

---

## 🤖 Running the Selenium Script

In a new terminal (while Flask API is running):

```bash
cd Web Automation
python WebAutomation.py
```

You will see a cat fact printed in your console!

---

## 💡 Notes & Assumptions

- Chrome and ChromeDriver must be installed and added to PATH.
- Selenium runs in headless mode for simplicity.
- Designed for educational and pet engagement purposes.

---

## ✅ Requirements

- Python 3.7+
- Flask
- Selenium
- Google Chrome + ChromeDriver
