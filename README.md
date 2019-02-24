# Basic Service Template 

Basic template with a local database setup and initial GrapQL set-up (not
working yet)

### Prerequisites

Install the required extensions from requrements.txt

```
pipenv install -r /path/to/requirements.txt
```

### Installing

You can query and change the database from flask shell for now

```
flask shell
Role.query.all()
User.query.all()
```
For the quick update and tracking use Migrate extension

```
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```
[Reference on migrate] (https://flask-migrate.readthedocs.io/en/latest/)

## On the GraphQL

It's not currently working with the GraphQL (even though extensions are included), so
the full implementation has to be done. I havent't figured out how to do that properly yet.


### Other stuff 

I figured to try to implement the organization through Blueprint to fetch views
and forms as needed as was suggested everywhere. Also the create_app function is
used for apps initialization.


