print("Strong number calculator")
def fat(a):
    b=1
    for i in range (1,a+1):
        b=i*b
    return(b)
aa=z=int(input("Enter the nuber to check :"))
z=aa
bb=[]
c=0
while aa>0 :
    bb.insert(0,aa%10)
    aa=aa//10
for i in bb:
    c=c+fat(i)
  
if z==c :
    print("Result =" +str(c))
    print("The given number is a Strong number")
else:
    print("Result =" +str(c))
    print("The given number is a not Strong number")

