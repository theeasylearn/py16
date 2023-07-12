#write a program to calculate simple interest from given amount rate and year.
#amount * rate * year /100
amount = int(input('enter amount'))
rate = int(input('enter rate'))
year = int(input('enter year'))
result = (amount * rate * year) / 100
print(f"simple interest = {result}")