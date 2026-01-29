# 📚 Django Development Notes

> **Chai Aur Django** - A comprehensive guide to Django development

---

## 🚀 Environment Setup

### Using UV Package Manager

UV is chosen for this project due to its exceptional speed and efficiency.

**Installation:**
```bash
uv pip install django
```

---

## 🏗️ Project Initialization

### Starting a New Django Project

To initialize a Django project:

```bash
django-admin startproject project_name
```

**Project Structure:**
- Creates a `project_name` folder
- Contains `manage.py` (project management script)
- Includes a `project_name` subfolder with configuration files

---

## 📁 Key Files Overview

| File | Purpose |
|------|---------|
| `views.py` | Contains business logic and request handlers |
| `urls.py` | Handles URL routing and path configuration |

---

## 🔧 Creating Views

### Basic View Example

**File:** `views.py`

```python
from django.http import HttpResponse

def contact(request):
    return HttpResponse("Contact Us at Chai Aur Django")
```

---

## 🛣️ URL Configuration

### Setting Up Routes

**File:** `urls.py`

```python
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact, name='contact'),
]
```

---

## ▶️ Running the Development Server

Launch the server with:

```bash
python manage.py runserver
```

---

## 🎨 Templates

### Directory Structure

**Best Practice:**
1. Create a `templates` folder in your project root
2. Inside `templates`, create a subfolder for each app/section (e.g., `home`, `about`)

**Example:**
```
templates/
    ├── home/
    │   └── index.html
    └── about/
        └── about.html
```

### Configuration

**File:** `settings.py`

Locate the `TEMPLATES` dictionary and update the `DIRS` setting:

```python
TEMPLATES = [
    {
        ...
        'DIRS': ['templates'],
        ...
    },
]
```

### Rendering Templates

**File:** `views.py`

```python
from django.shortcuts import render

def home(request):
    return render(request, 'home/index.html')
```

---

## 📦 Static Files

### Overview

Static files include:
- 🎨 **CSS** - Stylesheets
- ⚡ **JavaScript** - Client-side scripts
- 🖼️ **Images** - Graphics and media files

### Directory Structure

Create a `static` folder in your project root with appropriate subfolders:

```
static/
    ├── css/
    │   └── styles.css
    ├── js/
    │   └── script.js
    └── images/
        └── logo.png
```

### Configuration

**File:** `settings.py`

Import `os` and configure static files directories:

```python
import os

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
```

### Using Static Files in Templates

**Step 1:** Load the static tag at the top of your HTML file

```django
{% load static %}
```

**Step 2:** Link your static files

```html
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
<script src="{% static 'js/script.js' %}"></script>
<img src="{% static 'images/logo.png' %}" alt="Logo">
```

> ⚠️ **Important:** Always include `{% load static %}` at the beginning of your template file!

---

## 🔤 Jinja2 Template Language

### Template Syntax

Django uses a template language similar to Jinja2 for dynamic content rendering.

**Variables:**
```django
{{ variable_name }}
{{ user.username }}
{{ items.0 }}
```

**Tags:**
```django
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

**Loops:**
```django
{% for item in item_list %}
    <li>{{ item.name }}</li>
{% endfor %}
```

**Template Inheritance:**
```django
{# base.html #}
<!DOCTYPE html>
<html>
<head>
    {% block title %}My Site{% endblock %}
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

{# child.html #}
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
    <h1>Welcome to my site!</h1>
{% endblock %}
```

**Common Filters:**
```django
{{ value|lower }}           {# Lowercase #}
{{ value|upper }}           {# Uppercase #}
{{ value|title }}           {# Title Case #}
{{ value|length }}          {# Length #}
{{ value|default:"N/A" }}   {# Default value #}
{{ date|date:"Y-m-d" }}     {# Date formatting #}
```

---

## 🧩 Django Apps

### What are Apps?

Django apps are modular components that encapsulate specific functionality (e.g., blog, user authentication, e-commerce).

### Creating a New App

Run the following command in your terminal:

```bash
python manage.py startapp app_name
```

**Generated Structure:**
```
app_name/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── tests.py
    └── views.py
```

### Registering the App

**File:** `settings.py`

Add your app to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_name',  # Your new app
]
```

### Setting Up App URLs

> 💡 **Note:** Apps don't include a `urls.py` file by default.

**Option 1:** Create a new `urls.py` in your app folder

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

**Option 2:** Copy `urls.py` from the project directory and modify it

**Include App URLs in Project:**

**File:** `project_name/urls.py`

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app_name.urls')),
]
```
---

## 🎨 Tailwind CSS Integration

### Installation

**Step 1:** Install required packages

```bash
pip install django-tailwind
pip install 'django-tailwind[reload]'
```

**For UV users:** If using UV package manager, you'll need pip for this installation:

```bash
# Option 1
python -m ensurepip --upgrade

# Option 2
python -m pip install --upgrade pip
```

### Configuration

**Step 2:** Add Tailwind to installed apps

**File:** `settings.py`

```python
INSTALLED_APPS = [
    # ... other apps
    'tailwind',
]
```

**Step 3:** Initialize Tailwind

```bash
python manage.py tailwind init
```

> 📝 **Note:** This command will prompt you for an app name (default: `theme`) and other configuration options.

**Step 4:** Register the Tailwind app

Add the app name (from Step 3) to `INSTALLED_APPS`:

**File:** `settings.py`

```python
INSTALLED_APPS = [
    # ... other apps
    'tailwind',
    'theme',  # Your Tailwind app name
]
```

**Step 5:** Configure Tailwind settings

**File:** `settings.py`

```python
TAILWIND_APP_NAME = 'theme'  # App name used for Tailwind files
INTERNAL_IPS = ['127.0.0.1']
```

**Step 6:** Set NPM binary path (Windows users)

**File:** `settings.py`

```python
NPM_BIN_PATH = r'C:/Program Files/nodejs/npm.cmd'
```

**Step 7:** Install Tailwind dependencies

```bash
python manage.py tailwind install
```

### Running Tailwind

To use Tailwind CSS, you need to run both the Tailwind compiler and Django server:

**Terminal 1 - Tailwind Compiler:**
```bash
python manage.py tailwind start
```

**Terminal 2 - Django Server:**
```bash
python manage.py runserver
```

---

## 🔄 Hot Reloading (Development Only)

Hot reloading enables automatic CSS updates without manual page refresh.

### Installation

```bash
pip install 'django-tailwind[reload]'
```

### Configuration

**Step 1:** Add to installed apps

**File:** `settings.py`

```python
INSTALLED_APPS = [
    # ... other apps
    'django_browser_reload',
]
```

**Step 2:** Add middleware

**File:** `settings.py`

```python
MIDDLEWARE = [
    # ... other middleware
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]
```

**Step 3:** Include reload URLs

**File:** `urls.py`

```python
from django.urls import path, include

urlpatterns = [
    # ... other patterns
    path("__reload__/", include("django_browser_reload.urls")),  # Must be last
]
```

> ⚠️ **Important:** The reload path should be placed at the end of `urlpatterns`.

> 🚀 **Production Note:** Hot reloading is for development only. Disable it in production environments.

---

## 🔐 Django Admin Panel

Django provides a powerful built-in admin interface for managing your application's data.

### Initial Setup

**Step 1:** Run migrations

Before accessing the admin panel, apply database migrations:

```bash
python manage.py migrate
```

**Step 2:** Create a superuser

```bash
python manage.py createsuperuser
```

You'll be prompted to enter:
- **Username**
- **Email address** (optional)
- **Password** (entered twice for confirmation)

**Step 3:** Access the admin panel

Start your development server and navigate to:

```
http://127.0.0.1:8000/admin/
```

Log in with your superuser credentials.

### Password Management

**Change forgotten password:**

```bash
python manage.py changepassword username
```

Replace `username` with your actual username.

---

## 📝 Quick Reference

- ✅ **UV**: Fast package manager
- ✅ **Views**: Logic layer
- ✅ **URLs**: Routing layer
- ✅ **Templates**: Presentation layer

---

*Last updated: January 2026*




