# Write a programe to find bmi of user using oop

height = int(input("enter your height(in metres)"))
weight = int(input("enter your weight(in kgs)"))

class bmi:
     def get_bmi(self):
          
          bmi = weight/(height* height)
          print(bmi)

b1 = bmi()
b1.get_bmi()

