# 🎉 Smart Event Management Portal

A full-stack web application built with **Django** that streamlines event organization and participation. Users can register, browse events, enroll in upcoming activities, while organizers can create and manage events, monitor registrations, and view participants through a dedicated dashboard.

---

## ✨ Features

### 👤 Authentication

* User Registration
* Secure Login & Logout
* Edit Profile
* Protected Routes

### 📅 Event Management

* Create Events
* Edit Events
* Delete Events
* Event Details Page
* Category-Based Event Banners
* Search Events
* Filter Events by Category

### 🎟 Registration System

* Register for Events
* Cancel Registration
* Registration Deadline Validation
* Capacity Validation
* Prevent Duplicate Registrations

### 📊 Dashboards

#### User Dashboard

* View Registered Events
* View Past Events
* Manage Event Participation

#### Organizer Dashboard

* View Events Created
* Total Events Statistics
* Total Registrations
* Upcoming Events Count
* View Participants
* Edit & Delete Events

### 👥 Participant Management

* List Registered Participants
* Registration Status Tracking

---

## 🛠 Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Django Templates

### Database

* SQLite3

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
event_portal/
│
├── accounts/
├── events/
├── registrations/
├── static/
│   ├── css/
│   └── images/
├── templates/
├── event_portal/
├── manage.py
└── requirements.txt
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/<your-repository>.git
```

Navigate into the project:

```bash
cd <your-repository>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser (optional):

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

You can add screenshots here after deployment.

* Home Page
* Event Listing
* Event Details
* User Dashboard
* Organizer Dashboard
* Registration Page

---

## 📌 Future Enhancements

* Event Announcements
* Email Notifications
* QR Code Event Passes
* PDF Registration Pass
* Event Analytics
* Calendar Integration
* Certificate Generation

---

## 🎯 Learning Outcomes

This project helped strengthen my understanding of:

* Django Models
* ModelForms
* Authentication & Authorization
* CRUD Operations
* One-to-One & ForeignKey Relationships
* Django Admin
* Template Inheritance
* Static Files
* URL Routing
* Form Validation
* QuerySets & ORM
* User Roles
* Dashboard Development
* Git & GitHub Workflow

---

## 👨‍💻 Author

**Pavitha P and Prabavathi S**

If you found this project interesting, feel free to ⭐ the repository and share your feedback!
