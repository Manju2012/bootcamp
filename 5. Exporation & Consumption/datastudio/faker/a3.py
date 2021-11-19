import csv
from faker import Faker
import datetime


def fake_data_gen(records):
    fake = Faker('en_US')
    # fake1 = Faker('en_GB')   # To generate phone numbers

    with open("order_quantity.csv",mode='w', newline="") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()

        for i in range(records):
            writer.writerow({
                    'orderid': int(i+1),
                    'productid': fake.random.randint(1,100),
                    'quantity' : fake.random.randint(1,100)
                    })





if __name__ == '__main__':
    n = int(input('n: '))
    headers = ['orderid', 'productid','quantity']

    fake_data_gen(records=n)

    print("CSV generation complete!")