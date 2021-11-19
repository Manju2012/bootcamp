import csv
from faker import Faker
import datetime


def fake_data_gen(records):
    fake = Faker('en_US')
    # fake1 = Faker('en_GB')   # To generate phone numbers

    with open("/home/fagcpdebc1_09/BootCamp/5. Exporation & Consumption/datastudio/customer_master.csv",mode='w', newline="") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=headers)
        writer.writeheader()

        for i in range(records):
            writer.writerow({
                    'customerid':int(i+1),
                    'name':fake.name(),
                    'address':fake.address(),
                    'city':fake.city(),
                    'state':fake.state(),
                    'pincode':fake.zipcode()
                    })





if __name__ == '__main__':
    n = int(input('n: '))
    headers = ['customerid','name','address','city','state','pincode']

    fake_data_gen(records=n)

    print("CSV generation complete!")