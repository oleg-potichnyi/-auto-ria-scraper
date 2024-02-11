from celery import shared_task

from auto_ria.scraper import scrape_cars, dump_database


@shared_task
def schedule_car_scraping() -> None:
    cars = scrape_cars()
    for car in cars:
        car.save()


@shared_task
def schedule_database_dump() -> None:
    dump_database()
