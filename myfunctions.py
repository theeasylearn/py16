import random 
def get_otp():
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    num3 = random.randint(10,99)
    otp = str(num1) + str(num2) + str(num3)
    return otp

