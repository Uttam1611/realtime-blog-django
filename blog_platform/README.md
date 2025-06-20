# Prodesk IT Blog Platform

This is a **Django-based blog platform** that allows users to create, edit, delete posts and manage accounts (signup, login, logout). It features real-time notifications for new and deleted posts and includes automated test coverage.

## ✨ Features
- User authentication: signup, login, logout
- Post management: create, edit, delete posts
- Real-time notifications with Django Channels
- Test coverage report with pytest and coverage.py

## 🛠️ Tech Stack
- Python 3.x
- Django
- Django Channels
- SQLite
- HTML/CSS

## 📂 Installation
1. Clone the repo
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Run server: `python manage.py runserver`

## 🧪 Testing
Run tests with pytest and coverage:
```bash
pytest
coverage run -m pytest
coverage report -m
```

## 📜 License
MIT License
