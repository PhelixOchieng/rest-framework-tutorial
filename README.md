# Rest Framework Example

Credits to [Dev To](https://dev.to/joshuadeguzman/definitive-guide-developing-restful-apis-using-python-django-and-drf-2h7e)

This is a simple blog app that enables you to use api to make posts
Authentication is done using [`rest_framework tokens`](https://www.django-rest-framework.org/api-guide/authentication/)

You can find a hosted version of the code at [Rest Example](http://rest-example.herokuapp.com)

## Setup

Clone the repo

```shell

$ git clone https://github.com/PhelixOchieng/rest-framework-tutorial.git

# or using ssh
$ git clone git@github.com:PhelixOchieng/rest-framework-tutorial.git
```

Create and activate a new virtual environment (using [virtualenvwrapper](virtualenvwrapper.readthedocs.io))

```shell
$ mkvirtualenv rest-framework-tut   # create the virtual environment
....
$ workon rest-framework-tut         # activate the virtual environment
```

Download the requirements then run the migrations

```shell

$ pip install -r requirements.txt
$ python manage.py makemigrations && python manage.py migrate
```

Run the server

```shell
$ python manager.py runserver
```

## Suported Activities

Users, upon successfull login, can:

1. Create/Read/Update/Delete posts.
1. View and Update their profiles.
1. Upload their avatars (or be given a default)

User's can only modify posts that __belong to them__ i.e the one which they have created
