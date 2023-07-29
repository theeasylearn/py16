import random
import string 
def get_otp():
    num1 = random.randint(10,99)
    num2 = random.randint(10,99)
    num3 = random.randint(10,99)
    otp = str(num1) + str(num2) + str(num3)
    return otp

def generate_password(length=15):
    seeds = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()[]|<>?"
    size = len(seeds) - 1
    password = []
    count = 0
    while count<length:
        count=count+1
        password.append(seeds[random.randint(0,size)])
    return ''.join(password)


    
    
