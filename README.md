# sms_panel project

## Installation
create virtual environment
```bash
pip install virtualenv
cd env/bin/activate
```

```bash

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
cd kavenegar-python-master
pip install .
cd ..
python manage.py runserver

```