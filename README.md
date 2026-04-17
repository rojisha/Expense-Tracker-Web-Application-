# Django Expense Tracker
A lightweight web application built with Django for managing personal expenses. This tool allows authenticated users to perform full CRUD (Create, Read, Update, Delete) operations on their expense records.

## Features
- **User Authentication:** Secure login/logout system.
- **Personalized Data:** Users can only view and manage their own expenses.
- **Responsive Feedback:** Utilizes Django's messages framework for action confirmations.
- **Clean UI:** Built using Django templates and class-based views.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/rojisha/Expense-Tracker-Web-Application.git](https://github.com/rojisha/Expense-Tracker-Web-Application.git)
   cd Expense-Tracker-Web-Application
   ```
2. **Install Dependencies:**
   ```bash
   python -m pip install django
   ```
3. **Database Setup:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
4. **Create Admin/User Account:**
   ```bash
   python manage.py createsuperuser
   ```
5. **Run the Server:**
   ```bash
   python manage.py runserver
   ```
Navigate to http://127.0.0.1:8000/ in your browser.


## URL Structure & Navigation

| Action | URL Path | Description |
| :--- | :--- | :--- |
| **Login** | `/login/` | Secure entry point for users. |
| **Dashboard** | `/expenses/` | Main view showing the list of all expenses. |
| **Add Expense** | `/expenses/create/` | Form to log a new expenditure. |
| **Edit Expense** | `/expenses/<id>/edit/` | Modify details of an existing entry. |
| **Delete Expense**| `/expenses/<id>/delete/` | Remove an entry from the database. |

## Screenshots
<img width="1479" height="549" alt="image" src="https://github.com/user-attachments/assets/844dc7cf-49a1-4c43-9d12-82ea4acc99fb" />
&nbsp;
<img width="1467" height="798" alt="image" src="https://github.com/user-attachments/assets/3a7e2c4e-a782-4e38-94f5-b9b0f92695ce" />
&nbsp;
<img width="1480" height="376" alt="image" src="https://github.com/user-attachments/assets/a319bcae-aefd-45e8-9423-06b57bb76237" />
