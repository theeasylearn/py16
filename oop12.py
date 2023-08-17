class person:
     def walk(self):
          print("I can walk ")
     
     def talk(self):
          print("I can talk")

class student(person):
     def read(self):
          print("I can read ")
     def write(self):
          print("I can write ")
     def whatICanDo(self):
          self.read()
          self.write()
          person.walk(self)
          person.talk(self)

class employee(person):
     def work(self):
          print("I can work ")
     def holiday(self):
          print("I will take holiday ")
     def whatICanDo(self):
          self.work()
          self.holiday()
          person.walk(self)
          person.talk(self)

class teacher(student,employee):
     def teach(self):
          print("I can teach ")
     def homework(self):
          print("I will Give homework ")
     def whatICanDo(self):
          self.teach()
          self.homework()
          student.whatICanDo(self)
          employee.whatICanDo(self)


p1 = person()
s1 = student()
e1 = employee()
t1 = teacher()

p1.talk()
p1.walk()
print("--------------------------------")
s1.whatICanDo()
print("--------------------------------")
e1.whatICanDo()
print("--------------------------------")
t1.whatICanDo()