from django.db import models


class Scraper(models.Model):
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=255)
    price_usd = models.DecimalField(max_digits=10, decimal_places=2)
    odometer = models.IntegerField()
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    image_url = models.URLField(max_length=255, unique=True)
    images_count = models.IntegerField()
    car_number = models.CharField(max_length=20)
    car_vin = models.CharField(max_length=20)
    datetime_found = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        self.odometer = self.convert_odometer_value(str(self.odometer))
        if not self.is_valid_phone_number(str(self.phone_number)):
            raise ValueError("Invalid phone number format")
        super().save(*args, **kwargs)

    @staticmethod
    def convert_odometer_value(odometer) -> int:
        parts = odometer.split()
        if "thousand" in parts:
            index = parts.index("thousand")
            number = int(parts[index - 1]) * 1000
            return number
        else:
            return int(odometer)

    @staticmethod
    def is_valid_phone_number(phone_number) -> str:
        return phone_number.startswith("+380") and len(phone_number) == 13

    class Meta:
        ordering = ["title"]

    def __str__(self) -> str:
        return self.title
