# from fake_data import fake_data_gen
from lib.fake_data import fake_data_gen


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


    headers = ["Name", "Birth Date", "Phone Number","Own House", "Country",
                "Zip Code","Year", "Time","Longitude","Latitude"]

    mode = 'wt' if MODE == 1 else 'a'

    fake_data_gen(records=RECORDS, headers=headers, mode=mode)

    print("CSV generation complete!")
