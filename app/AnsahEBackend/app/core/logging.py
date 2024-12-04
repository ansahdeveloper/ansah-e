import logging
from elasticsearch import Elasticsearch
from app.core.config import settings

class ElasticsearchHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.es = Elasticsearch([settings.ELASTICSEARCH_HOST])

    def emit(self, record):
        doc = {
            'message': self.format(record),
            'level': record.levelname,
            'timestamp': record.created
        }
        self.es.index(index="ansah-e-logs", body=doc)

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    
    # Elasticsearch handler
    es_handler = ElasticsearchHandler()
    es_handler.setLevel(logging.INFO)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    es_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(es_handler)

    return logger

logger = setup_logging()

