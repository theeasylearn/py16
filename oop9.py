class person:
     def talk(self):
          print("I can talk ")
     def walk(self):
          print("I can walk ")

class employee(person):
     def earn(self):
          print("I can Earn ")
     def holiday(self):
          print("I will take Leave")
     def whatICanDo(self):
          self.earn()
          self.holiday()
          person.talk(self)
          person.walk(self)

class student(employee):
     def read(self):
          print("I can read")
     def write(self):
          print("I can write ")
     def whatICanDo(self):
          self.read()
          self.write()
          employee.whatICanDo(self)

p1 = person()
e1 = employee()
s1 = student()

p1.talk()
p1.walk()
print("===============================")
e1.whatICanDo()
print("===============================")
s1.whatICanDo()