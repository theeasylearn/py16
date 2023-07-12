person = { 'name':'Param' , 'weight':55.55 , 'age':19 , 'gender':'Male' }
person2 = {'name':'sahil' , 'weight':50.50 , 'education' : 'Btech'}
print(person)
print(person2)

keys = ['name','email','mobile','dob','city']
person3 = dict.fromkeys(keys)
print(person3)

print(person.get('name')) # Param
print(person.get('city','not found')) # Param
print(person['name'])
# print(person['city']) not good way
print(person.items())
print(person.keys())
print(person.values())
person.pop("weight")
print(person)
# del person['email'] not good way
temp = person.pop("email",'not found')
print(temp)
person.popitem()
print(person)
person.update({'age':20})
print(person)
person.update({'email':'param@gmail.com'})
print(person)
person.clear()
print(person)
