a=int(input())
z=a
b=[]
c=0
while a>0:
    b.insert(0,a%10)
    a=a//10
for i in b:
    c=i+c
print("The sum of the digits of "+str(c))
if(z%c==0):
    print("Given number is Harshad Number")
else:
    print("Given number is Not a Harshad Number")
