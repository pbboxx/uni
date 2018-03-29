# url-shortener
Django web-app where a user can search for university courses.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

install virtualenv.


```
pip install virtualenv

virtualenv my_env

```

### Installing

Clone the repo.

migrate the DB Model.

Run the server.
```

git clone https://github.com/pbboxx/uni.git

pip install -r requirements.txt

python manage.py makemigration
python manage.py migrate
python manage.py runserver


```

## Running the tests
To run test execute the following script

```
python test_app.py

```


## Deploying 

Different providers available for convienence use heroku.
More details on heroku.



## Todo

Improve UX
Integrate recommandation engine


