# 🛒 Neosales E-Commerce Project

A **Django-based e-commerce web application** built to manage **products, customers, and orders**.  
The project demonstrates a full **e-commerce workflow**, including:

- 📝 **CRUD operations** for products, customers, and orders  
- 📊 **Admin-friendly dashboard** with modern UI components  

![Dashboard Screenshot](./static/assets/images/neosales01.png)

---

## 📂 Project Structure


.<br>
├── ecommerce/                 # Main Django project (settings, configs, WSGI/ASGI)<br>
├── store/                     # Core store application<br>
├── templates/                 # HTML templates<br>
├── static/                    # Static assets<br>
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
- **Admin Dashboard**: Styled UI with charts, tables, and forms.  
- **Responsive UI**: Built with SCSS, Bootstrap, and vendor libraries.  
- **Seed Data**: Preload sample products and customers using `data_seed.py`.  

---

## 🛠️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Maikoandre/NeoSales.git
cd NeoSales
```

### 2. Activate Docker Environment (You need to have docker installed)
```bash
docker compose up -d
```

### 3. Access the site
```bash
http://127.0.0.1:8000/
```

## 🧑‍💻 Tech Stack

- **Backend**: Django (Python)

- **Frontend**: HTML, SCSS, Bootstrap, JS

- **Database**: SQLite