#write a program to findout factorial of given number 
#number = 5
# process = 5 x 4 x 3 x 2 x 1
#output = 120 

number = int(input("Enter number"))
factorial = 1 

while number>=1:
    factorial = number * factorial #5
    number = number - 1 #4
print(factorial)

