# forsit-task
Forsit Take Home Task

## Setting up locally
Clone the project and run following commands to install requirements in a virtual environment:

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Connecting with local Postgres Database
Create a Postgres database on localhost and update the database connection string in app/settings.py

This is the ER Diagram of the database:
<img width="941" alt="ERD" src="https://github.com/mirzahaider/forsit-task/assets/45700845/27a28534-7909-4bbe-8853-a0da1837723c">


## Run server
```
uvicorn app.main:app --reload 
```

## API Documentation
Checkout swagger docs for a detailed documentation on available endpoints.
```
http://127.0.0.1:8000/docs
```

## Populate database with test data
Hit the following endpoint to insert test data in database tables:
```
http://127.0.0.1:8000/initial-data
```
This endpoint should be hit only once, when tables are first created.
