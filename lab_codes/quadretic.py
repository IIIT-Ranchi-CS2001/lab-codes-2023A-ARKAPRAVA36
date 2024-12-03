import math
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
c = int(input("Enter 3rd number : "))

d = (b**2) - (4*a*c)
k = -b/(2*a)
if(d==0):
    print("Both roots are same : ",k)
elif(d>0):
    print("1st root is : ", (-b + math.sqrt(d))/(2*a))    
    print("2nd root is : ", (-b - math.sqrt(d))/(2*a)) 
else:
    print("Real part is : ",k)       
    print("Imaginary part is : ",(math.sqrt(-d))/(2*a))