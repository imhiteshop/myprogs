'''TO CHECK THE TYPE OF TRIANGLE'''
x = input("Enter x :")
y = input("Enter y :")
z = input("Enter y :")
 
def checkTriangle(x, y, z):
 
    
    if x == y == z:
        print("Equilateral Triangle")
 
    
    elif x == y or y == z or z == x:
        print("Isosceles Triangle")
 
   
    else:
        print("Scalene Triangle")
 


checkTriangle(x, y, z)