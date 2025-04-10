# E-Commerce_site_with_chatbot

E-commerce platform built with Django that integrates an AI-powered chatbot using the OpenAI API to enhance customer experience and support.
## Requirements

- Python
- Django
- OpenAI API key

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/Wymagin/E-Commerce_site_with_chatbot.git
```
### Install requirements
```bash
pip install -r requirements.txt
```

### Generate a Django Secret Key

Before running the application, ensure that you have a unique secret key set in your settings.py file. You can generate a secret key using the following Python script:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Once generated, set the SECRET_KEY environment variable or update the settings.py file directly:

```bash
SECRET_KEY = 'your-generated-secret-key'
```

## Build and Run the Application

```bash
py manage.py runserver
```

### Running Migrations

To apply database migrations, run:

```bash
py manage.py makemigrations
py manage.py migrate
```

### Creating a Superuser

To create a superuser for accessing the Django admin, run:

```bash
python manage.py createsuperuser
```

## Project Structure

```bash
tbd
```


### License
This project is licensed under the MIT License.
