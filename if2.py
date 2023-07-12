#write a program to accept RBS level from user and give advise whether can take sugar or not 

rbs = int(input("Enter running blood sugar level"))
if rbs>=126:
    print('you have Diabetes')
    print('you should not take sugar in food or drink')
else:
    print('Congratulation, you do not have Diabetes')
    print('you can take sugar in food or drink')
    
print('Good bye....')
