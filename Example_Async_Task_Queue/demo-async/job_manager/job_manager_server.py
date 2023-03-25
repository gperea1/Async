from flask import Flask, request
from job_tasks import count_words_from_url, celery_app
from celery.result import AsyncResult
import json

app = Flask(__name__)

@app.route('/count', methods = ['POST']) # submit_count_words_url_job
def count_words_url():
    try:
        data = request.get_json().get('text')
        result = count_words_from_url.delay(data)
        status_code  = 200
        return json.dumps({"id": result.id}), status_code
    except: 
        return json.dumps({"id": "Error: Invalid input or 'text' not used properly."}), 400

@app.route('/status/<id>', methods = ['GET']) #get_result_count_words_url_job
def get_count_words_url(id):

    res = AsyncResult(id, app=celery_app)
    count = -1
    if res.status == "SUCCESS":
        count = res.get()
        status_code = 200
        return json.dumps({"result": count, "status": "completed"}), status_code
    if res.status == "PENDING":
        status_code = 200
        return json.dumps({"status": "PENDING"}), status_code

    return json.dumps({"result": "No content or 'text' was not used properly."})
    