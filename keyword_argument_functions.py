#example of keywords argument function
#write a program to findout area of cylinder from given height and radius 
def get_pi():
    return 3.14159265359

def get_cyliender_area(radius,height):
    area = 2 * get_pi() * radius * height + (2 * get_pi() * radius * radius)
    return area 


r = int(input("Enter radius"))
h = int(input("Enter height"))
area = get_cyliender_area(height=h,radius=r)
print(area)



    
