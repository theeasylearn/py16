#write a program to findout qube of given positive numeber
num1 = int(input("Enter positive number"))
#check whether number is positive or not 
if num1<0:
   num1 = -num1 #unary operator -
   print('negative value is converted into positive value')

qube = num1 * num1 * num1
print(f"{qube} is qube of {num1}")

