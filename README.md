# Django Real-Time Blog Platform

A **fully-featured real-time blog platform** built with [Django](https://www.djangoproject.com/) and [Django Channels](https://channels.readthedocs.io/en/stable/) that enables seamless updates using WebSockets and Redis. It supports user authentication, post creation and deletion, real-time notifications, and a responsive UI.

---

## ✨ Features
- ✅ **User Authentication** — Register, log in, and log out securely.
- ✅ **Create, Edit, and Delete Posts** — Fully permission-controlled post management.
- ✅ **Real-Time Notifications** — Powered by Redis and Django Channels for pub/sub messaging.
- ✅ **Test Coverage** — Includes unit tests for views, models, and real-time features.
- ✅ **Responsive Design** — Optimized for desktops and mobile devices.

---

## 🛠️ Technologies Used
- **Backend** — Python 3.x, Django 5.x
- **Real-Time Backend** — Django Channels + Redis
- **Database** — SQLite (default), switchable to Postgres/MySQL
- **Frontend** — HTML5, CSS3, Bootstrap
- **Testing** — Django's built-in test framework
- **Version Control** — Git

---

## ⚙️ Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the Redis server:
   ```bash
   redis-server
   ```
6. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
7. Visit http://127.0.0.1:8000

---

## 🧪 Running Tests
Run the test suite:
```bash
python manage.py test
```

---

## 🤝 Contributing
Feel free to submit issues or pull requests. Contributions are highly appreciated!

---

💡 **Happy Coding!**
