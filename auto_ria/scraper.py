import datetime
import os
import requests
from django.conf import settings

from auto_ria.models import Scraper


def scrape_cars() -> list[Scraper]:
    cars_response = requests.get("https://auto.ria.com/uk/car/used/").json()
    cars = []
    for car_dict in cars_response:
        cars.append(
            Scraper(
                url=car_dict.get["url"],
                title=car_dict.get["title"],
                price_usd=car_dict.get["price_usd"],
                odometer=car_dict.get["odometer"],
                username=car_dict.get["username"],
                phone_number=car_dict.get["phone_number"],
                image_url=car_dict.get["image_url"],
                images_count=car_dict.get["images_count"],
                car_number=car_dict.get["car_number"],
                car_vin=car_dict.get["car_vin"],
                datetime_found=datetime.datetime.now()
            )
        )
    return cars


def dump_database() -> None:
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time == "12:00":
        if not os.path.exists("dumps"):
            os.makedirs("dumps")
        dump_filename = f"dumps/dump_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.sql"
        pg_dump_command = (
            f"pg_dump -U {settings.DATABASES['default']['USER']} "
            f"-d {settings.DATABASES['default']['NAME']} "
            f"> {dump_filename}"
        )
        os.system(pg_dump_command)


if __name__ == "__main__":
    cars = scrape_cars()
    for car in cars:
        car.save()
    dump_database()
