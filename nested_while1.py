# Write a programe to print half pyramid 
# https://i1.faceprep.in/fp/articles/img/46684_1580817324.png
count = 0 
flash = 0 
temp = 1
while flash < 8:
    while count < temp: #1
        print("*",end='')
        count +=1
    print("")
    temp +=1
    count = 0
    flash+=1



# while count < 3:
#     print("*",end='')
#     count+=1
# print('')
# count = 0
# while count < 4:
#     print("*",end='')
#     count+=1
# print('')
# count = 0 
# while count < 5:
#     print("*",end="")
#     count+=1