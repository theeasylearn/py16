class person:
     
     def  __init__(self,name,age):
          print("Constructor Called...")
          self.name = name
          self.age = age

     def walk(self):
          print("I can walk ",self.name,"age is ",self.age)

     def talk(self):
          print("I can talk ",self.name)


name = input("Enter your name ")
age = int(input("Enter your age "))
p1 = person(name,age)
p1.walk()
p1.talk()