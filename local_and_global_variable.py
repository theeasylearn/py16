salary = 10000 #global variable
def increase_salary():
    global salary #salary from global scope will be accessed
    salary = salary * 1.10

def add_ta_da_into_salary():
    salary = 10000 #create local variable salary
    salary = salary * 1.40

print(f"salary before increment {salary}")
increase_salary()
print(f"salary after increment {salary}")
add_ta_da_into_salary()
print(f"salary after ta da {salary}")
