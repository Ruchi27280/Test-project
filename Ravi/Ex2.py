#Given a string, display only those characters which are present at an even index number.
a= input("enter string = ")
l= len(a)
print(l)
for i in range(0,l):
    if i%2==0:
        print(a[i])
    
