import math 
import sys 
import datetime 
def display_module_function(modulename):
    list = dir(modulename)
    for item in list:
        print(item)
    print("-"*150)

display_module_function(math)
display_module_function(sys)
display_module_function(datetime)