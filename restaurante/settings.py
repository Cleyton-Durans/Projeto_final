from pathlib import Path
import os

# ============================
# BASE DIR
# ============================
BASE_DIR = Path(__file__).resolve().parent.parent

# ============================
# SEGURANÇA
# ============================
SECRET_KEY = 'django-insecure-4af+)@m6iw3mnx+hs6^^(7a-&_pw8skq#afp5hz&qivu*%od&-'  # troque por variável de ambiente em produção
DEBUG = False  # importante desativar em produção

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'projeto-restaurante-0qjk.onrender.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://projeto-restaurante-0qjk.onrender.com',
]

# ============================
# APLICAÇÕES
# ============================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'reserva',  # seu app principal
    'widget_tweaks',  # utilitário para formulários
]

# ============================
# MIDDLEWARE
# ============================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   
]

# ============================
# URLs e WSGI
# ============================
ROOT_URLCONF = 'restaurante.urls'
WSGI_APPLICATION = 'restaurante.wsgi.application'

# ============================
# TEMPLATES
# ============================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # adicione aqui pastas personalizadas de templates, se necessário
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# ============================
# BANCO DE DADOS
# ============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ============================
# VALIDAÇÃO DE SENHA
# ============================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ============================
# LOCALIZAÇÃO E TEMPO
# ============================
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True
DATE_INPUT_FORMATS = ['%d/%m/%Y']

# ============================
# ARQUIVOS ESTÁTICOS E MÍDIA
# ============================
STATIC_URL = '/static/'

# Durante o desenvolvimento
STATICFILES_DIRS = [
    BASE_DIR / 'reserva' / 'static',  # pasta de estáticos do app reserva
    # BASE_DIR / 'static',              # pasta estática global (se existir)
]

# Para o Render coletar os estáticos em produção
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Mídia (uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ============================
# REDIRECIONAMENTO DE LOGIN/LOGOUT
# ============================
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/reservas/'
LOGOUT_REDIRECT_URL = '/'

# ============================
# CHAVE PRIMÁRIA PADRÃO
# ============================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
