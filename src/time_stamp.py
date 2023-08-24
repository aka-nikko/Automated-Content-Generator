import datetime
from config import sleep_time

def time_stamp():
    try:
        date_and_time = datetime.datetime.now()
        time_change = datetime.timedelta(hours=sleep_time)
        new_time = date_and_time + time_change
        print("Next Video Will Be Uploaded At: "+new_time.strftime("%I:%M %p"))
    except Exception as e:
        raise e