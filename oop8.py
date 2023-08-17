class person:
     def talk(self):
          print("I can Talk ")
     
     def walk(self):
          print("I can Walk ")

class company:
     def work(self):
          print("I can work ")
     
     def progress(self):
          print("I will progress")


class employee(person,company):

     def earn(self):
          print("I can earn")

     def holiday(self):
          print("I will take leave ")

     def whatICanDo(self):
          self.earn()
          self.holiday()
          company.work(self)
          company.progress(self)
          person.talk(self)
          person.walk(self)


p1 = person()
c1 = company()
e1 = employee()
# p1.talk()
# p1.walk()
# print("-----------------------------------------------------")
# c1.work()
# c1.progress()
# print("----------------------------------------")
e1.whatICanDo()