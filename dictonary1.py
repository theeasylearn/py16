subject = {}
trainer = {'name':'Ankit','surname':'patel'}

print(subject)
print(trainer)
subject['name'] = 'Python'
subject['trainer'] = 'Ankit Patel'
subject['fees'] = 7500
subject['duration'] = 90
print(subject)

subject['chapters'] = (1,2,3,4,5)
subject['topics'] = ['Basic','Decision making and loop','functions','class and object']
subject['trainer'] = trainer
print(subject)
del subject['duration']
print(subject)
