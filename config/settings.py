import os
from pathlib import Path
import pymysql; 
pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-your-secret-key-here'

DEBUG = True
ALLOWED_HOSTS = []
#ALLOWED_HOSTS = ['halphaservice.com', 'z283816-s72f6.ps10.zwhhosting.com']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'django.contrib.sitemaps',
    
    'ygnyoga', 
    'blogs',
    'user',
    'classes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

# ၅။ Templates (HTML) ဖိုင်များရှိရာ လမ်းကြောင်း
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'config.context_processors.role_based_menus',  # Role-based menu context processor ထည့်သွင်းခြင်း
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# local UAT
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

##MySQL local UAT
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.mysql',   
        'ENGINE': 'mysql.connector.django',
        'NAME': 'YgnPrivateYoga_uat',                  
        'USER': 'root',                        
        'PASSWORD': 'He!n1293',            
        'HOST': 'localhost',                   
        'PORT': '3306',                         
     
    }
}

# DATABASES = {
#     'default': {
#         # 'ENGINE': 'django.db.backends.mysql',  
#         'ENGINE': 'mysql.connector.django',
#         'NAME': 'zsfpszwh_YgnPrivateYoga_uat',                  
#         'USER': 'zsfpszwh_alphaygnyogauat',                         
#         'PASSWORD': '@lph@Yog@uat1293',            
#         'HOST': 'localhost',                    
#         'PORT': '3306',                         
#     }
# }

# ၇။ Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ၈။ Language နှင့် Timezone (မြန်မာစံတော်ချိန် ပြောင်းချင်လျှင် Asia/Yangon)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Yangon' 
USE_I18N = True
USE_TZ = True

# Static Files (CSS, JavaScript, Images)
STATIC_URL = '/static/' 
STATICFILES_DIRS = [BASE_DIR / "static"] 
STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = '/media/' 
MEDIA_ROOT = BASE_DIR / "media"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = "user-login"

AUTH_USER_MODEL = 'user.CustomUser'

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"