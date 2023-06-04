from app import app
from celery import Celery
import requests

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def sync_dataset():
    headers = {
        'X-Parse-Application-Id': 'gP38fEGPgSSBvvO4Kz9McQD2UpUrcpIlrXDyHLWc',
        'X-Parse-REST-API-Key': '72gJMaTFClPr90oA7bkRYdUy0PJIcKQ8tj8bQvtP'
    }

    # Make requests to retrieve and store data
