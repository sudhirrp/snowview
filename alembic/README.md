# GraphQl Service to query Snowflake data warehouse

## Tech Stacks used

> FastAPI

> Graphene (GraphQl)

> SQLAlchemy (ORM)

> Snowflake

## Pre-requisites

> Add a `.env` file to the project root with following enviornment variables

    DATABASE_URL=snowflake://{SF_USER}:{SF_PASSWORD}@{SF_ACCOUNT}/{SF_DATABASE}/{SF_SCHEMA}?warehouse={SF_WAREHOUSE}&role={SF_ROLE}

    SF_USER=<snowflake user>
    SF_PASSWORD=<snowflake password>
    SF_ACCOUNT=<snowflake account id>
    SF_DATABASE=<snowflake database>
    SF_SCHEMA=<snowflake schema>
    SF_WAREHOUSE=<snowflake warehouse>
    SF_ROLE=<user role in snowflake>

> Docker desktop

> Python >= 3

## Library dependencies

- Link to requirements.txt file

- <details>
  <summary>Library dependencies</summary>

  ##

  - alembic==1.6.5
  - aniso8601>=7.0.0
  - appdirs==1.4.4
  - asgiref==3.4.1
  - black==21.6b0
  - click==8.0.1
  - colorama==0.4.4
  - fastapi==0.66.0
  - graphene>=3.0
  - graphene-sqlalchemy>=2.0
  - graphql-core>=2.0
  - graphql-relay>=2.0
  - greenlet==1.1.0
  - h11==0.12.0
  - Mako==1.1.4
  - MarkupSafe==2.0.1
  - mypy-extensions==0.4.3
  - pathspec==0.8.1
  - promise==2.3
  - psycopg2==2.9.1
  - pydantic==1.8.2
  - python-dateutil==2.8.1
  - python-dotenv==0.18.0
  - python-editor==1.0.4
  - regex==2021.7.1
  - Rx==1.6.1
  - singledispatch==3.6.2
  - six==1.16.0
  - SQLAlchemy==1.4.29
  - starlette==0.14.2
  - toml==0.10.2
  - typing-extensions==3.10.0.0
  - uvicorn==0.14.0
  - snowflake-sqlalchemy
  - graphene-sqlalchemy-filter

</details>

## Build App

### For migration (Only do these steps if you want to migrate any database)

```
$ alembic init alembic
$ docker-compose run app alembic revision --autogenerate -m "New Migration"
$ docker-compose run app alembic upgrade head
```

### Build docker app

```
$ docker-compose build
```

## Run docker app

```
docker-compose up
```

## GraphQl playground

> http://127.0.0.1:8000/graphql
