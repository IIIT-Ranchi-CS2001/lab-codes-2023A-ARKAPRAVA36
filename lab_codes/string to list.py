l={1,2,3,4,5,6,7,8,9}
print(len(l));
print(max(l))
print(min(l))
print(sum(l))
l1=sorted(l)
print(l1)
l2=l1.sort()
print(l2)
l4=[1,2,3,l,l1,l2]
print(l4)
result=[i for i in l if i%2==0]
print(result)