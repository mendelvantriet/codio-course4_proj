# Course4_proj

This repository contains practice assignments for the [Coursera](https://www.coursera.org/) course [Advanced Django: External APIs and Task Queuing](https://www.coursera.org/learn/codio-advanced-django-external-apis-task-queuing).
It is the fourth course in the Specialization [Advanced Django: Mastering Django and Django Rest Framework Specialization](https://www.coursera.org/specializations/codio-advanced-django-and-django-rest-framework).
The practice assignments of the first three courses can be found in [this repo](https://github.com/mendelvantriet/codio-blango). 

## Dependencies

Redis

```commandline
sudo apt install -y redis
redis-cli ping
```

## Django Commands

```commandline
DJANGO_OMDB_KEY="..." python3 manage.py movie_search django unchained

DJANGO_OMDB_KEY="..." python3 manage.py movie_fill tt1853728
```

## Start app

A Celery worker needs to run in the background, and optionally Celery Beat

```commandline
DJANGO_OMDB_KEY="..." celery -A course4_proj worker -l DEBUG &
DJANGO_OMDB_KEY="..." celery -A course4_proj beat -l INFO \
  --scheduler django_celery_beat.schedulers:DatabaseScheduler &
DJANGO_OMDB_KEY="..." python3 manage.py runserver 0.0.0.0:8000
```

## Usage

    http://localhost:8000/search/?search_term=star+wars

