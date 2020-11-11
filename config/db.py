from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

POSTGRESQL = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'yilmer_projects',
        'USER': 'postgres_admin',
        'PASSWORD': '17685923idkcC*',
        'HOST': '3.213.198.175',
        'PORT': '5432',
    }
}
