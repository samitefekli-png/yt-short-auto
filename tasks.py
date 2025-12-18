from celery import shared_task
import subprocess, os

@shared_task
def generate_and_upload(topic, count):
    # TTS, video birleştirme ve YouTube yükleme burada yapılır
    print(f"{topic} – {count} video yapılıyor...")
