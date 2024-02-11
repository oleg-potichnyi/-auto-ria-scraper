import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

app = Celery("auto_ria")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(["auto_ria"])

app.conf.beat_schedule = {
    "schedule-car-scraping": {
        "task": "auto_ria.tasks.schedule_car_scraping",
        "schedule": (crontab(hour=12, minute=0)),
    },
    "schedule-database-dump": {
        "task": "auto_ria.tasks.schedule_database_dump",
        "schedule": crontab(hour=12, minute=0),
    },
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
