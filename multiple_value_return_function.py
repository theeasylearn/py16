#function that convert given rupees into dollar, pound and euro
def convert(rupees):
    dollar = rupees * 0.012
    euro = rupees * 0.011
    pound = rupees * 0.0095
    return dollar,euro,pound

rupees = int(input("Enter rupees"))
result = convert(rupees)
print(result)