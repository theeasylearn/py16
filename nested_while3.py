# Write a programe to print inverted half pyramid 
count = 0 
flash = 6

while flash > 0:
    while count < flash: 
        print("*",end='')
        count +=1
    print('')
    count = 0
    flash -=1


# while count < 5:
#     print("*",end='')
#     count+=1
# print('')
# count = 0
# while count < 4:
#     print('*',end='')
#     count +=1
# print('')
# count = 0
# while count < 3:
#     print("*",end='')
#     count += 1