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

You can access CRUD forms via django admin at http://127.0.0.1:8000/

You can access the http api at http://127.0.0.1:8000/api/tennis/

---

[Development notes](development_notes.md)
