# 🛒 Neosales E-Commerce Project

A **Django-based e-commerce web application** built to manage **products, customers, and orders**.  
The project demonstrates a full **e-commerce workflow**, including:

- 🔑 **Authentication** (Login & Registration)  {To be made}
- 📝 **CRUD operations** for products, customers, and orders  
- 📊 **Admin-friendly dashboard** with modern UI components  

![Dashboard Screenshot](./static/assets/images/neosales01.png)

---

## 📂 Project Structure


.<br>
├── ecommerce/                 # Main Django project (settings, configs, WSGI/ASGI)<br>
│   ├── __init__.py<br>
│   ├── settings.py           # Project settings and configuration<br>
│   ├── urls.py               # Main URL routing<br>
│   └── wsgi.py<br>
├── store/                     # Core store application<br>
│   ├── migrations/           # Database migrations<br>
│   ├── models.py             # Data models (Product, Customer, Order)<br>
│   ├── views.py              # Business logic and view handlers<br>
│   ├── forms.py              # Django forms for data validation<br>
│   ├── urls.py               # App-specific URL routes<br>
│   └── admin.py              # Admin panel configuration<br>
├── templates/                 # HTML templates<br>
│   ├── base.html             # Base template structure<br>
│   ├── partials/             # Reusable template components<br>
│   └── pages/                # Individual page templates<br>
├── static/                    # Static assets<br>
│   ├── css/                  # Compiled CSS and SCSS files<br>
│   ├── js/                   # JavaScript functionality<br>
│   ├── images/               # Product images and UI assets<br>
│   ├── fonts/                # Custom typography<br>
│   └── vendor/               # Third-party libraries (Bootstrap, etc.)<br>
├── db.sqlite3                # SQLite database (development)<br>
├── data_seed.py              # Initial data population script<br>
├── manage.py                 # Django management CLI<br>
├── requirements.txt          # Python dependencies<br>
└── README.md                 # Project documentation<br>


---

## 🚀 Features

- **Product Management**: Add, update, delete, and view product listings.  
- **Customer Management**: Register customers, view details, and manage records.  
- **Order Management**: Track and update order statuses.  
- **Authentication**: User login and registration. 
- **Admin Dashboard**: Styled UI with charts, tables, and forms.  
- **Responsive UI**: Built with SCSS, Bootstrap, and vendor libraries.  
- **Seed Data**: Preload sample products and customers using `data_seed.py`.  

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Maikoandre/neosales.git
cd django-ecommerce
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```

### 3. Install Dependencies
```bash
pip install django
```

### 4. Run Database Migrations
```bash
python3 manage.py migrate
```
### 5. Seed the Database (Optional)
```bash
python3 data_seed.py
```

### 6. Run Development Server
```bash
python3 manage.py runserver
```

## 🧑‍💻 Tech Stack

- **Backend**: Django (Python)

- **Frontend**: HTML, SCSS, Bootstrap, JS

- **Database**: SQLite (default, but easily swappable to PostgreSQL/MySQL)

- **Task Runner**: Gulp (for static asset management)

