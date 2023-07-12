#list related methods
box = ['Toys',100,3.14,True,100,'Books']
print(box)
box.append('Kites')
print(box)
box.insert(0,"Car")
print(box)
box.remove(3.14)
print(box)
box.pop(0)
print(box)
print(box.index("Books"))
print(box.count(100))
basket = ['games','pencil']
box.extend(basket)
print(box)
box.clear()
print(box)
box = ['Toys',100,3.14,True,100,'Books']
copy_list = box.copy()
print(copy_list)