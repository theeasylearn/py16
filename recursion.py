def calc_factorial(number):
    print("function called ...")
    if number == 1:
        return 1 
    else:
        return (number * calc_factorial(number-1))
    
answer = calc_factorial(7)
print(f"factorial of 5 is {answer}")