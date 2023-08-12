class person:
     def walk(self):
          print("I can Walk ")
     def talk(self):
          print("I can Talk ")

     
class student(person):
     def write(self):
          print("I can Write ")

     def read(self):
          print("I can Read ")


p1 = person()
s1 = student()

p1.walk()
p1.talk()
print("----------------------------------------")
s1.write()
s1.read()
s1.walk()
s1.talk()