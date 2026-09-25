# CollegeWebsite
A dynamic and responsive College Department Web Portal built with Django and Bootstrap 5. Features role-based access, interactive notices, events management, course details, and a visitor feedback system for SYBSc Computer Science practicals.
# 🎓 Department of Computer Science - Web Portal

A dynamic, responsive, and interactive College Department Web Portal built with **Python, Django, and Bootstrap 5**. This project serves as a comprehensive portal for students, prospective applicants, and faculty members to access academic resources, department notices, course syllabi, event updates, and feedback submission mechanisms.

---

## 🚀 Key Features

* **Public Information Center:** Dedicated pages for Department Overview, Principal's Message, Admission Guidelines, and Fee Structures.
* **Academic Catalog:** Clear listing of offered courses and downloadable subject-wise syllabi.
* **Interactive Notice Board:** Dynamic database-driven notices with support for PDF attachments.
* **Event Management:** Displays upcoming and past departmental events, workshops, and hackathons.
* **Visitor Feedback System:** Integrated form allowing visitors to submit queries directly to the database.
* **Admin Dashboard:** Built-in Django Admin interface for instant CRUD management of notices, events, and feedback entries.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.12, Django 6.0
* **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5 (Responsive Layout)
* **Database:** SQLite3 (Default relational database)
* **Environment:** GitHub Codespaces / Local Virtualenv

---

## 📂 Project Structure

```text
college_website/
├── manage.py
├── college_website/      # Project configurations & root URL routes
├── core/                 # App for informational pages (About, Courses, Fees, etc.)
├── portal/               # App for interactive dynamic features (Notices, Events, Feedback)
├── static/               # Central CSS, JavaScript, and asset files
├── templates/            # Global HTML templates using Django template inheritance
└── media/                # User-uploaded files (Syllabus PDFs, event posters)
```

---

## ⚙️ How to Run Locally

### 1. Clone the Repository
```bash
git clone [https://github.com/Coderonaut08spacesci/CollegeWebsite.git](https://github.com/Coderonaut08spacesci/CollegeWebsite.git)
cd CollegeWebsite
```

### 2. Set Up Virtual Environment *(Optional but Recommended)*
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin Account)
```bash
python manage.py createsuperuser
```

### 6. Start Development Server
```bash
python manage.py runserver
```
Open `http://127.0.0.1:8000/` in your web browser to view the application!

---

## 👤 Author

* **Student Name:** SYBSc Computer Science Student
* **Course:** Bachelor of Science in Computer Science (SYBSc CS)
* **Purpose:** Academic Practical & Portfolio Project
