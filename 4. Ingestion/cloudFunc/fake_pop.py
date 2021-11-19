import csv
from faker import Faker
import datetime


def fake_data_gen(records, headers, mode, file):
    fake = Faker('en_US')

    with open(f"/home/fagcpdebc1_09/BootCamp/4. Ingestion/cloudFunc/datafiles/{file}.csv", mode=mode, newline="") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()

        for _ in range(records):
            writer.writerow({
                    "Name": fake.name(),
                    "Own House" : fake.random.choice([True, False]),
                    "Country" : fake.country(),
                    "Zip Code" : fake.zipcode(),
                    "Year" : fake.year(),
                    "Longitude": fake.longitude(),
                    "Latitude" : fake.latitude() 
                    })



if __name__ == '__main__':

    while True:
        try:
            MODE = int(input('please choose mode 1/2. 1:write, 2:append'))
            RECORDS = int(input('Enter how many rows to be inserted')) # To Enter required number of data
            break

        except ValueError:
            print('Wrong input. Please Enter correct number')

        except NameError:
            print('Wrong input. Please Enter correct number')


    headers = ["Name", "Own House", "Country",
                "Zip Code","Year", "Time","Longitude","Latitude"]

    mode = 'wt' if MODE == 1 else 'a'

    file = input('Enter valid file name: ')

    fake_data_gen(records=RECORDS, headers=headers, mode=mode, file=file)

    print("CSV generation complete!")
