### Follow the approach

-------

```shell
$ mkdir authuser

$ virtualenv venv
$ source venv/bin/activate

$ pip3 install django
$ pip3 install django-crispy-forms

$ pip3 freeze > requirements.txt

$ django-admin startproject mysite .
$ python3 manage.py startapp main
```

- add these two app in INSTALLED_APP
- `'crispy_forms', 'main'`

- then add templates and html files
- change: TEMPLATES => `'DIRS': [BASE_DIR / 'templates'],`
- add this line in settings.py => `CRISPY_TEMPLATE_PACK = 'bootstrap4'`

- then, fix the urls in mysite
- complete main app => `forms.py`, `views.py`, `urls.py`

```shell
$ python3 manage.py makemigrations
$ python3 manage.py migrate
$ pyhton3 manage.py runserver
```

```url
http://127.0.0.1:8000/register
http://127.0.0.1:8000/login
http://127.0.0.1:8000/
```