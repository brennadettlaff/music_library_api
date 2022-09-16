# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#m3^xt-lf92ffhbs6lnq9n_omiqzquvkzb0-jc^%8d!+xef7mc'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'music_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}