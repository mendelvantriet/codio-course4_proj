# Course4_proj

## Dependencies

Redis

```commandline
sudo apt install -y redis
redis-cli ping
```

## Commands

```commandline
DJANGO_OMDB_KEY="..." python3 manage.py movie_search django unchained

DJANGO_OMDB_KEY="..." python3 manage.py movie_fill tt1853728
```

## Start app

A Celery worker needs to run in the background

```commandline
DJANGO_OMDB_KEY="..." celery -A course4_proj worker -l DEBUG &
DJANGO_OMDB_KEY="..." python3 manage.py runserver 0.0.0.0:8000
```

## Usage

    http://localhost:8000/search/?search_term=star+wars

