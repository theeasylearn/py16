import myconverter

inch = int(input("Enter inches "))

foot = myconverter.get_foot(inch)
meter = myconverter.get_meter(inch)
km = myconverter.get_kilometer(inch)
mile = myconverter.get_mile(inch)

print(f"foot = {foot} meter = {meter} km = {km} mile = {mile}")
