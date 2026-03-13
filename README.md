# MEMBER Django Project

A full stack web application built using **Django (Backend)** and **React (Frontend)**.
This project demonstrates how a React frontend communicates with a Django backend API to manage member data.

---

## 🚀 Project Overview

The **Member Django Project** is a simple full stack application where users can manage member information.
The backend is built using Django and provides APIs, while the frontend is built with React to display and interact with the data.

---

## 🛠️ Technologies Used

### Frontend

* ReactJS
* HTML5
* CSS3
* JavaScript
* Axios (for API requests)

### Backend

* Python
* Django
* Django REST Framework

### Database

* SQLite3

### Tools

* Git
* GitHub
* VS Code

---

## 📁 Project Structure

```
MEMBER-Django-Project
│
├── Frontend
│   └── react-frontend
│       ├── public
│       ├── src
│       ├── package.json
│       └── README.md
│
└── backend
    ├── backend
    ├── member
    ├── db.sqlite3
    └── manage.py
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/dineshwaran2004/MEMBER-Django-Project.git
```

```
cd MEMBER-Django-Project
```

---

### 2️⃣ Backend Setup (Django)

```
cd backend
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Backend will run at:

```
http://127.0.0.1:8000/
```

---

### 3️⃣ Frontend Setup (React)

Open another terminal.

```
cd Frontend/react-frontend
npm install
npm start
```

Frontend will run at:

```
http://localhost:3000/
```

---

## ✨ Features

* View members
* Add new members
* Update member details
* Delete members
* React frontend connected with Django backend API




---

## 📌 Future Improvements

* User authentication
* Better UI design
* Deployment on cloud (Render / Vercel / AWS)

---

## 👨‍💻 Author

**Dinesh Waran**

* GitHub: https://github.com/dineshwaran2004
* Portfolio: https://dineshwaran2004.github.io/Portfolio/

---


