# Installation
In a virtual environment,
```
pip install -r requirements.txt
docker run --name smartodds_db -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -e POSTGRES_USER=smartoods -d postgres
python manage.py migrate
python manage.py createsuperuser
python manage.py load_data tennis/data/2011.xls 2011
python manage.py runserver
```


[development notes](development_notes.md)
