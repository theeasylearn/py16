#set in python 

fruits = {'apple','banana','mango','orange','pinapple'}
print(fruits)
fruits.add('apple') #will be ignored and not added because there is already apple 
fruits.add('kiwi')
print(fruits)
# del fruits[0]

set1 = {10,20,30,40,50}
set2 = {40,50,60}

union = set1.union(set2)
intersection = set1.intersection(set2)

print("union of set1 and set2",union)
print("intersection of set1 and set2",intersection)

difference = set1.difference(set2)
print("difference of set1 and set2",difference)

print('Good bye....')
