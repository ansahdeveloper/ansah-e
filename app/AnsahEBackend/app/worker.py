from celery import Celery
from app.core.config import settings

celery = Celery(__name__)
celery.conf.broker_url = settings.REDIS_URL
celery.conf.result_backend = settings.REDIS_URL

celery.conf.task_routes = {
    'app.tasks.high_priority': {'queue': 'high_priority'},
    'app.tasks.default': {'queue': 'default'},
    'app.tasks.low_priority': {'queue': 'low_priority'},
}

celery.conf.task_annotations = {
    'app.tasks.high_priority': {'rate_limit': '100/s'},
    'app.tasks.default': {'rate_limit': '50/s'},
    'app.tasks.low_priority': {'rate_limit': '10/s'},
}

