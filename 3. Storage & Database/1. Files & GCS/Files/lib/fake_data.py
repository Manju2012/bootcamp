import csv
from faker import Faker
import datetime


def fake_data_gen(records, headers, mode):
    fake = Faker('en_US')
    fake1 = Faker('en_GB')   # To generate phone numbers

    with open("data/file.csv", mode=mode, newline="") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        if mode=='wt':
            writer.writeheader()

        for _ in range(records):
            writer.writerow({
                    "Name": fake.name(),
                    "Birth Date" : fake.date(pattern="%Y-%m-%d", end_datetime=datetime.date(2021, 1,1)),
                    "Phone Number" : fake1.phone_number(),
                    "Own House" : fake.random.choice([True, False]),
                    "Country" : fake.country(),
                    "Zip Code" : fake.zipcode(),
                    "Year" : fake.year(),
                    "Time": fake.time(),
                    "Longitude": fake.longitude(),
                    "Latitude" : fake.latitude() 
                    })


