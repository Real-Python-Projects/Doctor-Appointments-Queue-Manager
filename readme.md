## Scheduled tasks with celery and Redis as broker

pip install celery
pip install redis


## Starting Redis Server
$ redis-server

To check if its working
$ redis-cli ping

will return pong if its working correctly
## Starting Celery Services
$ celery -A picha worker -l info
$ celery -A picha beat -l info


## Resource:
https://realpython.com/asynchronous-tasks-with-django-and-celery/

https://devcenter.heroku.com/articles/celery-heroku#:~:text=Celery%20is%20written%20in%20Python,message%20broker%20and%20result%20store.


https://www.youtube.com/watch?v=fvYo6LBZUh8