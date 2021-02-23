### all commands and instructions

```shell
mkdir celery

virtualenv venv
source venv/bin/activate

django-admin startproject core .

pip install django, celery

brew install rabbitmq

export PATH=$PATH:/usr/local/sbin

brew services enable rabbitmq

brew services start rabbitmq

python3 manage.py startapp demoapp
```

- open a <celery.py> file in core app and complete it
- start a new app, <demoapp>, and create a <tasks.py> and complete it
- then, check the task by executing following command

```shell
celery -A core worker -l info
```

```shell
python3 manage.py shell

from demoapp.tasks import add
add.delay(4, 4)
add.delay(4, 234)
add.apply_async((3, 3), countown=5)

# open another terminal and activate venv and execute celery to check
celery -A core worker -l info
```