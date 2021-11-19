from faker import Faker
import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter


def fake_data_gen(n):
    fake = Faker('en_US')

    schema = avro.schema.parse(open("/home/fagcpdebc1_09/BootCamp/4. Ingestion/ClodComposer/user.avsc", "rb").read())
    writer = DataFileWriter(open("/home/fagcpdebc1_09/BootCamp/4. Ingestion/ClodComposer/users.avro", "wb"), DatumWriter(), schema)

    for _ in range(n):     
        writer.append({"name": fake.name(), 
                        "favorite_number": fake.random.randint(1,100),
                        "favorite_color": fake.random.choice(['red','blue','green','white','black'])})
    
    writer.close()


if __name__ == '__main__':

    n = int(input('Enter no. of data to be generated : '))

    fake_data_gen(n)
    
    # reader = DataFileReader(open("/home/fagcpdebc1_09/BootCamp/4. Ingestion/ClodComposer/users.avro", "rb"), DatumReader())
    # for user in reader:
    #     print(user)
    # reader.close()