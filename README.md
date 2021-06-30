# Running the app

## Prerequisites

- create and activate environment
- pip install -r requirements.txt

## To run the app

```sh
export FLASK_APP="src/main.py"
export POSTGRES_URL="127.0.0.1:5432"
export POSTGRES_DB="NAME _OF_DB"
export POSTGRES_USER="DB_USER"
export POSTGRES_PASSWORD="DB_PASS"



flask db init
flask db migrate
flask db upgrade

flask run
```
