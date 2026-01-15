from datetime import timedelta
from pathlib import Path
import os


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = os.environ['DEBUG'].lower() == 'true'

ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')

DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # <--- adicionado
    'django.contrib.messages',  # <--- adicionado (útil pro admin)
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'apps.usuario.apps.UsuarioConfig',
    'apps.cliente.apps.ClienteConfig',
    'apps.departamento.apps.DepartamentoConfig',
]


OTHERS_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',  # para swagger UI
    'django_filters',
    "corsheaders",
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + OTHERS_APPS

AUTH_USER_MODEL = 'usuario.Usuario'

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # Se você não usa cookies de CSRF, pode manter removido, caso contrário reincluir:
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    # <--- bom ter se messages/ admin forem usados
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.EnforceJSONContentTypeMiddleware',
]


ROOT_URLCONF = 'core.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                # messages removido porque não há MessageMiddleware
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': os.environ['POSTGRES_PORT'],
    }
}

# Necessário para createsuperuser --noinput
os.environ.setdefault(
    "DJANGO_SUPERUSER_PASSWORD",
    os.environ["DJANGO_SUPERUSER_PASSWORD"]
)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = os.environ["STATIC_ROOT"]

if DEBUG:
    STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.environ["MEDIA_ROOT"]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Django Backend API',
    'DESCRIPTION': 'Projeto em django com backend exclusivo para APIs RESTful',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    "SORT_OPERATION_PARAMETERS": False,

    # OTHER SETTINGS
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=int(os.environ['JWT_ACCESS_MINUTES'])),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=int(os.environ['JWT_REFRESH_DAYS'])),
    'AUTH_HEADER_TYPES': ('Bearer',),
}

LOGS_DIR = BASE_DIR / 'logs'
LOGS_DIR.mkdir(exist_ok=True)

if os.environ['LOG_REGISTER'].lower() == 'true':
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': str(BASE_DIR / 'logs' / 'django.log'),
                'when': 'midnight',
                'interval': 1,
                'backupCount': 30,
                'encoding': 'utf-8',
                'delay': True,
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }

# configurações de CORS

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

# Se você precisar enviar cookies / credenciais:
CORS_ALLOW_CREDENTIALS = True

# (opcional) Métodos e headers permitidos — geralmente os defaults já cobrem:
CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
