import datetime as dt
import pandas
from random import randint
import smtplib
import os

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = dt.datetime.now()
# print(today)
today_tuple = (today.month, today.day)
# print(today_tuple)

data = pandas.read_csv('birthdays.csv')

birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthday_dict:
    birthday_person = birthday_dict[today_tuple]
    #b_day_person_age = int(today.year - birthday_person['year'])
    file_path = f"letter_templates/letter_{randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])
        print(contents)
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr = MY_EMAIL,
                            to_addrs = birthday_person['email'],
                            msg= f"Subject: Happy Birthday\n\n" #optional {b_day_person_age}
                                 f'{contents}')
