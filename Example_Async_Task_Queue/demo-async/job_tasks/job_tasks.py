import os
from celery import Celery
import requests
from collections import Counter
import re

import time # added this library 

broker_url  = os.environ.get("CELERY_BROKER_URL"),
res_backend = os.environ.get("CELERY_RESULT_BACKEND")

celery_app = Celery(name           = 'job_tasks',
                    broker         = broker_url,
                    result_backend = res_backend)

@celery_app.task
def count_words_from_url(text):
    co = len(text.split(' '))
    time.sleep(co) # added this item 
    return co #raw_words_count
    
        


        