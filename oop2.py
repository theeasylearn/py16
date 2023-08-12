class person:

     def  __init__(self):
          print("Constructor Called...")
          self.name = "Param "
          self.age = 18

     def walk(self):
          print("I can walk ",self.name,"age is ",self.age)
     def talk(self):
          print("I can talk ",self.name)


p1 = person()
p1.walk()
p1.talk()