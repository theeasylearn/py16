#defining function(create function)
#with return value & with argument function 
def get_interest(amount,rate,year):
    interest = (amount * rate * year) / 100
    return interest


amt = int(input('Enter amount'))
rat = int(input('Enter rate'))
yr = int(input('enter year'))


result = get_interest(amt,rat,yr) #calling function
print(result)

