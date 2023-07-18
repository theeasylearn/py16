#defining function(create function)
import datetime

#with return value without argument function
def get_current_date():
    current_date = str(datetime.datetime.day) + "/" + str(datetime.datetime.month) + "/" + str
    return current_date

current_date = get_current_date()
print(current_date)

