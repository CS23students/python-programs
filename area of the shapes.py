def square():
    a=int(input("enter the side of square:"))
    return a*a
def rectangle():
    l=int(input("enter the length:"))
    b=int(input("enter the bradth:"))
    return l*b
def circle():
    r=int(input("enter the radius;"))
    return 3.14*r*r
def triangle():
    l=int(input("enter the length of the base:"))
    h=int(input("enter the height oh the triangle:"))
    return 0.5*l*h
print("1.area of square\n,2.area of the triangle \n,3.area of circle\n,4.area of triangle \n")
opt=int(input("enter an option:"))
if opt==1:
  print("the area of the square:",square())
elif opt==2:
    print("the area of rectangle:",rectangle())
elif opt==3:
    print("the area of the circle:",circle())
elif opt==4:
    print("the area of the trianglke:",triangle())
else:
    print("invalid choice")
      
          
