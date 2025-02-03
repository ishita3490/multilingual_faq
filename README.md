# 🌍 Multilingual FAQ System 📝

A **Django-based REST API** for managing FAQs with **multi-language translation support** using Google Translate API. This system allows users to fetch FAQs in different languages via API requests.

---

## 🚀 Features
✅ **Multilingual FAQ Support** - Fetch FAQs in different languages using a query parameter (`?lang=hi`, `?lang=bn`).  
✅ **Automated Translation** - Uses Google Translate API to translate questions & answers dynamically.  
✅ **WYSIWYG Editor Support** - Integrated `django-ckeditor` for rich-text formatting in answers.  
✅ **Caching for Performance** - Implements **Redis caching** to speed up translations.  
✅ **REST API for FAQs** - Provides API endpoints to fetch and manage FAQs.  
✅ **Admin Panel for Management** - User-friendly Django Admin interface to manage FAQs.  
✅ **Unit Tests** - Includes tests to ensure API stability.  

---

## 🛠️ Installation Guide

### **1️⃣ Clone the Repository**
First, clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/multilingual_faq.git
cd multilingual_faq


2️⃣ Create & Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # For Mac/Linux
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Apply Migrations & Run the Server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Once the server starts, open your browser and go to:
http://127.0.0.1:8000/


⚙️ Project Structure
csharp
Copy
Edit
multilingual_faq/
│── faq/                     # Main FAQ App
│   ├── migrations/          # Database Migrations
│   ├── models.py            # Django Models (FAQ Model)
│   ├── serializers.py       # DRF Serializers
│   ├── views.py             # API Views (Handles Translation & Fetching)
│   ├── urls.py              # API Endpoints
│
│── config/                  # Project Configurations
│   ├── settings.py          # Django Settings
│
│── static/                  # Static Files (if any)
│── templates/               # HTML Templates (Admin Panel)
│── manage.py                # Django Management Script
│── requirements.txt         # Required Python Libraries
│── README.md                # Project Documentation (this file)


Technologies Used
Django - Backend Framework
Django REST Framework (DRF) - API Development
Google Translate API - Automatic Language Translation
django-ckeditor - WYSIWYG Editor for Admin Panel
Redis - Caching for faster responses
pytest - Unit Testing



✨ Author
👤 Ishita Bansal
📧 Email: ishitabansal770@gmail.com
🔗 GitHub: ishita3490