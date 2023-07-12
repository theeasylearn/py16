num1 = 10
num2 = 10

print(num1 is num2,"when both are same ")

num1 = 11
print(num1 is num2,"when both are not same ")

print(num1 is not num2,"when both are not same using is not ")

num1 = 10
print(num1 is not num2,"When both are same using is not ")

# num1 = 11
print("the address of num1 is ",id(num1))
print("the address of num2 is ",id(num2))