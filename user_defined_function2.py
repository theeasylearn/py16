#defining function(create function)
import datetime

#with return value without argument function
def get_current_date():
    today = datetime.date.today()
    current_date = str(today.day) + "/" + str(today.month) + "/" + str(today.year)
    return current_date

#with return value without argument
def get_current_time():
    time = datetime.datetime.now()
    current_time = str(time.hour) + ":" + str(time.minute) + ":" + str(time.second)
    return current_time

def print_date_time():
    #wednesday 19-07-2023
    date_time = get_current_date() + " " + get_current_time()
    print(date_time)
    
current_date = get_current_date()
print(current_date)

current_time = get_current_time()
print(current_time)
print_date_time()