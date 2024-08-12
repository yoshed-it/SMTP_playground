import datetime as dt
import smtplib
import os
from dotenv import load_dotenv
import json
from random import randint


load_dotenv()
test_email = os.getenv('EMAIL')
test_password = os.getenv('PASSWORD')
wife_email = os.getenv('WIFE_EMAIL')




current_date_time = dt.datetime.now()
day_of_week = dt.datetime.weekday(current_date_time)



with open('SMTP_playground/demotivational_quote.json', 'r') as quotes:
    demotivational_quote = json.load(quotes)
    
    number_of_quotes = len(demotivational_quote["demotivational_quotes"])
    print(number_of_quotes)
    random_quote_idx = randint(0, number_of_quotes)
    quote = demotivational_quote["demotivational_quotes"][random_quote_idx]["quote"]
    author = demotivational_quote["demotivational_quotes"][random_quote_idx]["author"]
    
    print(random_quote_idx)

message = (f"Subject: Monday Motivational Quote\n"
            f"Content-Type: text/plain; charset=\"UTF-8\"\n\n"
            f"Hello! Today's quote is: {quote}\n- {author}")

if day_of_week == 0:
    try:    
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=test_email, password=test_password)
            connection.sendmail(
                from_addr=test_email, 
                to_addrs=wife_email , 
                msg=message.encode('utf-8'))
            print("email send is good")
    except Exception as error:
        print(f"an {error} happened")
else:
    print(f"Its actually {day_of_week}")




