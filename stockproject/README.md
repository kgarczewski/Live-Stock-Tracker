Simple app to live track cryptocurrencies exchange rate.
App fetch live data from api and dynamically display it via VueJs.

Setup:
- create your database and make migrations
- install (snap install redis) and run redis server (redis-server)
- in your django project runserver and run celery beat(celery -A stockproject beat -l info
) and celery worker (celery -A stockproject.celery worker --loglevel=info) separately 
