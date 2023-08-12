class person:
     def __init__(self,name,roll_no):
          self.name = name
          self.roll_no = roll_no
     def display_person(self):
          print("My name is ",self.name)
          print("My Roll no is ",self.roll_no)


class student(person):
     def __init__(self, my_name, my_roll_no,marks,percentage):
          self.marks = marks
          self.percentage = percentage
          person.__init__(self, my_name, my_roll_no)
     
     def display_student(self):
          print("My name is ",self.name)
          print("my Roll no is ",self.roll_no)
          print("My marks are ",self.marks)
          print("My percentage are ",self.percentage)

p1 = person('param',58)
p1.display_person()
print("-----------------------------------------------")
s1 = student('Devarsh', 59, 100, 98)
s1.display_person()
s1.display_student()