"""
Django settings for blog project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import os
from pathlib import Path

# Define la ruta base del proyecto. Esto se usa para construir rutas de archivos dentro del proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent

# Ajustes rápidos para el desarrollo. No recomendados para producción.
# Advertencia de seguridad: Mantener la clave secreta segura en producción.
SECRET_KEY = 'django-insecure-dg*))(x$uaih3y(18x47awrju++c$z*$gzu$aye+3!xawo*ezp'

# Modo de depuración activado. En producción debe estar en False para evitar la exposición de información sensible.
DEBUG = True

# Lista de hosts permitidos para acceder al sitio. En producción se deben agregar los dominios permitidos.
ALLOWED_HOSTS = []

# Modelo de usuario personalizado para utilizar una tabla específica llamada "USUARIO" en la aplicación "usuario".
AUTH_USER_MODEL = 'usuario.USUARIO'

# Configuración del backend de correo electrónico (en este caso, SMTP de Gmail).
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Servidor SMTP
EMAIL_PORT = 587  # Puerto para TLS
EMAIL_USE_TLS = True  # Habilita el cifrado TLS
EMAIL_HOST_USER = 'economia_4.0@gmail.com'  # Correo emisor
EMAIL_HOST_PASSWORD = 'rwey gvaq amdu pinz'  # Contraseña del correo
DEFAULT_FROM_EMAIL = 'RV15 Soporte <no-reply@economia4.0>'  # Nombre que aparece en el campo "De" en los correos enviados

# Nombre del sitio y ID correspondiente en la tabla de sitios en la base de datos.
SITE_NAME = 'ECONOMIA 4.0'
SITE_ID = 1

# Aplicaciones instaladas que están disponibles para este proyecto.
INSTALLED_APPS = [
    'django.contrib.admin',  # Panel de administración de Django
    'django.contrib.auth',  # Gestión de usuarios y autenticación
    'django.contrib.contenttypes',  # Soporte para tipos de contenido
    'django.contrib.sessions',  # Soporte para sesiones
    'django.contrib.messages',  # Mensajes entre vistas
    'django.contrib.staticfiles',  # Gestión de archivos estáticos como CSS y JavaScript

    'django.contrib.sites',  # Habilita la funcionalidad para manejar múltiples sitios en Django
    'apps.posts',  # Aplicación personalizada para gestión de publicaciones
    'apps.contacto',  # Aplicación personalizada para gestión de contacto
    'apps.usuario',  # Aplicación personalizada para la gestión de usuarios
]

# Middleware que procesa las solicitudes y respuestas HTTP.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Provee medidas de seguridad adicionales
    'django.contrib.sessions.middleware.SessionMiddleware',  # Maneja las sesiones del usuario
    'django.middleware.common.CommonMiddleware',  # Provee funcionalidad general, como el manejo de cabeceras HTTP
    'django.middleware.csrf.CsrfViewMiddleware',  # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Autenticación de usuarios en cada solicitud
    'django.contrib.messages.middleware.MessageMiddleware',  # Soporte para mensajes flash
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Prevención de ataques de clickjacking
]

# Definición de la URL raíz para la configuración de las rutas del proyecto.
ROOT_URLCONF = 'blog.urls'

# Configuración de las plantillas (templates) de Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Backend para renderizado de plantillas
        'DIRS': [os.path.join(os.path.dirname(BASE_DIR), 'templates')],  # Directorio donde se buscan plantillas
        'APP_DIRS': True,  # Habilita la búsqueda de plantillas en cada aplicación instalada
        'OPTIONS': {
            'context_processors': [  # Procesadores de contexto que añaden datos a las plantillas
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Aplicación WSGI utilizada por Django para gestionar solicitudes web.
WSGI_APPLICATION = 'blog.wsgi.application'

# Configuración de la base de datos (aquí se utiliza SQLite por defecto).
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Motor de base de datos (SQLite en este caso)
        'NAME': BASE_DIR / 'db.sqlite3',  # Nombre y ubicación del archivo de base de datos
    }
}

# Validadores de contraseñas para asegurar que cumplan con ciertos requisitos.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',  # No permite contraseñas similares a atributos del usuario
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',  # Exige un mínimo de caracteres
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',  # Bloquea contraseñas comunes
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',  # Bloquea contraseñas solo numéricas
    },
]

# Configuración de la internacionalización (idioma y zona horaria).
LANGUAGE_CODE = 'es-ar'  # Código de idioma para Argentina
TIME_ZONE = 'America/Argentina/Buenos_Aires'  # Zona horaria
USE_I18N = True  # Habilita la traducción de texto
USE_TZ = True  # Habilita el uso de zonas horarias

# Configuración de archivos estáticos (como CSS, JavaScript, etc.).
STATIC_URL = '/static/'  # URL para acceder a archivos estáticos
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), 'static'),)  # Directorios donde se buscan archivos estáticos

# Configuración del campo de clave primaria por defecto en los modelos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de archivos multimedia (como imágenes).
MEDIA_URL = '/media/'  # URL para acceder a archivos multimedia
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')  # Directorio donde se almacenan archivos multimedia


LOGIN_REDIRECT_URL = '/' #redirige a la pagina principal luego del logeo.