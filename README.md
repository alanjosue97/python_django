# Django-PostgresSQL

## Initial setup

Initialize the Poetry and add its requirements:

```bash
poetry init
poetry add django pyscopg2-binary
```
Start the django project and aplication:

```bash
poetry run django-admin starproject academia
cd academia
poetry add python mange.py startapp polls
```
## Setup

Spin up a PostgresSQL database:

```bash
docker run --name academia-postgres -e POSTGRES_PASSWORD=academia -e POSTGRES_USER=academia -e POSTGRES_DB=academia -d postgres:15.3
```
Install:
```bash
poetry install
```
Run:
```bash
poetry run pyhton mange.py runserver 0.0.0.0:8000
```