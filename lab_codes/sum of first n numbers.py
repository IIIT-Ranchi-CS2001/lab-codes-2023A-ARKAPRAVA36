m=int(input("Enter a number:"))
i=m
s=0
while(i>0 ):
     s=s+(i%10)
     i=i//10
print("Sum is:",s)
