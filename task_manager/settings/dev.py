from task_manager.settings.base import *

SECRET_KEY = "django-insecure-8e&tffdi3nnwhgw=87=-z63q5dy9(9e#0kee$)a-))$s%keve)"
DEBUG = True


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
