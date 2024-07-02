import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# BASE_DIR es la ruta base de nuestro proyecto
BASE_DIR = Path(__file__).resolve().parent.parent

# Clave secreta utilizada para la encriptación en Django
SECRET_KEY = 'adminkey'

# Configuración para la creación automática de claves primarias
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Lista de hosts permitidos para acceder a la aplicación
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Aplicaciones instaladas en nuestro proyecto
INSTALLED_APPS = [
    'django.contrib.admin', # Panel de administración de Django
    'django.contrib.auth', # Autenticación de usuarios
    'django.contrib.contenttypes', # Tipos de contenido
    'django.contrib.sessions', # Manejo de sesiones
    'django.contrib.messages', # Manejo de mensajes
    'django.contrib.staticfiles', # Configuración de archivos estáticos
    'gestion.views' # Aplicación principal de nuestro proyecto
]

# Middlewares que se ejecutarán antes y después de cada petición
MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware', # Manejo de sesiones
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Autenticación de usuarios
    'django.contrib.messages.middleware.MessageMiddleware', # Manejo de mensajes
    # ...
]

# Archivo de URLs principal de nuestro proyecto
ROOT_URLCONF = 'inventario.urls'

# Configuración de plantillas para nuestro proyecto
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], # Directorio para plantillas personalizadas
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

# Configuración de la base de datos
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Motor de base de datos que utilizamos
        'NAME': 'inventario', # Nombre de la base de datos
        'USER': 'postgres', # Usuario de la base de datos
        'PASSWORD': '', # Contraseña del usuario
        'HOST': 'localhost', # Dirección del servidor de base de datos
        'PORT': '5432', # Puerto de la base de datos
    }
}

# Configuración para archivos estáticos
STATIC_URL = '/static/' # URL donde se buscarán los archivos estáticos
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), # Directorio donde se encuentran los archivos estáticos
]

