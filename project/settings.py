import os 
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = 'django-insecure-rybwn0^2a#%cpit%q)0!&ain98k@x$z)k679h&q7#mn1ojykns'
DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1']


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', #django-allauth

    'rest_framework',
    'corsheaders',
    'rest_framework.authtoken',
    'dj_rest_auth',
    'allauth', #django-allauth
    'allauth.account', #django-allauth
    'allauth.socialaccount', #django-allauth
    'dj_rest_auth.registration', #django-allauth
    
    'createPost.apps.CreatepostConfig',
    'payment.apps.PaymentConfig',
    'produit.apps.ProduitConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    'hundelreactdj.apps.HundelreactdjConfig',
    'testApi.apps.TestapiConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', #new
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (  
    'http://localhost:3000', 
    'http://localhost:8000', 
)


#to use session between django and react without any issue.
CORS_ALLOW_CREDENTIALS = True

# Session settings
SESSION_SAVE_EVERY_REQUEST = True 
SESSION_COOKIE_SAMESITE = None


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly', #new
    ],
    'DEFAULT_AUTHENTICATION_CLASSES' : [ #new
        'rest_framework.authentication.TokenAuthentication' , #new       
    ],
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' #django-allauth

SITE_ID = 1 #django-allauth

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'front', 'build')],
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

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'front', 'build', 'static')]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {  'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {  'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {  'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {  'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/' 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

PAYPAL_CLIENT_ID = 'ARC9EimTFv6eHfgZ-2cib8KaE3dzTVwyPuLkxxbmJArgO7jfQvtDXo9eoc7chCcYrR_Tc2hroOAfV-SF'
PAYPAL_CLIENT_SECRET = 'ECKBMwmITpmzOiO_UpfYbuKyWJj2tvRmKpBkR33gf8xNenWQJh4t8nvI166zNbsVONgaynlbg6-L2hgk'