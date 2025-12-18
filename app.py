from flask import Flask, request, render_template
from celery import Celery
import os

app = Flask(__name__)
celery = Celery(app.name, broker='redis://redis:6379/0')

@celery.task
def generate_and_upload(topic, count):
    # Burada video üretim ve YouTube yükleme kodları olacak
    print(f"{topic} için {count} adet video oluşturulup yükleniyor...")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        topic = request.form['topic']
        count = int(request.form['count'])
        generate_and_upload.delay(topic, count)
        return "İşlem başlatıldı! Videolar kısa sürede YouTube'a yüklenecek."
    return render_template('index.html')
