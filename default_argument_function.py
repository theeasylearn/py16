#write a python program to convert given hours and minutes and seconds into second

def get_seconds(hours,minutes=0,second=0):
    # total_seconds is local variable
    total_seconds = hours * 60 *60
    if minutes!=0:
        total_seconds += minutes * 60
    total_seconds += second
    return total_seconds

hours = int(input("Enter hours"))
minutes = int(input("Enter minutes"))
seconds = int(input("Enter seconds"))

total_seconds = get_seconds(hours,minutes,seconds)
print(total_seconds)

total_seconds = get_seconds(hours,minutes)
print(total_seconds)

total_seconds = get_seconds(hours)
print(total_seconds)