# Approach

Utilized Django, a widely used web framework for python. For data storage, this project uses sqlite. The application is intended to be built using docker and runs inside of a docker container to maximize cross-platform compatibility and ease-of-use. A swagger page was added to make interacting with the apis a bit easier and to document the apis.

Overview of technologies used:
- Python 3
- Django 4.1
- sqlite
- Docker
- Swagger

# Requirements
To run this project, you must have Docker installed



# Quick Start

In the project root directory, run the following:

`$ docker compose up --build pybank`

This will build the docker image:
- retrieve all of the python packages for the project, 
- run the database migrations and build the sqlite database

Then run the application in a docker container

When the application is up and running, the server will be listening on port 8000 by default. 

Note: On occasion, the console output will get cutoff as docker attaches to the container. If the last statement reads:

`Watching for file changes with StatReloader`

the app is running and waiting for requests.

To interact with the Bank Apis, open your browser to http://localhost:8000/swagger. This will direct you to a swagger doc listing all of the bank APIs...

### `POST /account/`
Creates a new account with the provided name. Returns 400 if the account already exists.

example request:
```
{
    "name": "bob"
}
```

response:
```
OK
```
### `GET /account/{name}/`
Retrieves the account info with the account name and balance. Returns 404 if account does not exist.

example request:

`GET /account/bob/`

example response:

```
{
    "name": "bob",
    "balance": 0.00
}
```


### `POST /account/{name}/deposit`
Deposits a given amount to the account with the provided name. Returns 404 if account does not exist.

example request:

`POST /account/bob/deposit`

```
{
    "amount": 10
}
```

example response:
```
OK
```

### `POST /account/{name}/withdraw`
Withdraws a given amount from the account with the provided name. Returns 404 if account does not exist.

example request:

`POST /account/bob/withdraw`

```
{
    "amount": 5
}
```

example response:
```
OK
```



# Project Structure

This project consists of 3 main directories:

- bank
- api
- docs

### bank
contains the parent Django project

### api
contains the api app. The business logic for the bank apis can be found inside the /bank/views.py file.

### docs
contains the routing for the openapi/swagger doc generation.
