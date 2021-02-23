**install postgresql, postgis**

$ brew install postgresql
$ brew install postgis

**add in installed app**

'django.contrib.gis',
'rest_framework',

**change database**

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis  ',
        'NAME': 'studentdb',
        'USER': 'admin',
        'PASSWORD': 'admin',
        'HOST': 'localhost'
    }
}