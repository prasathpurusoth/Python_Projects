print("Perfect Number Calculator")
a=int(input("Enter the number :"))
b=0
for i in range(1,a):
    if(a%i==0):
        b=b+i
if(b==a):
    print("Sum of the diviser are :"+str(b))
    print("Given number is Perfect Number")
else:
    print("Sum of the diviser are :"+str(b))
    print("Given number is Not a Perfect Number")

