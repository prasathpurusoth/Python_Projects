print("HCF calculator")
a=int(input("Enter the first number :"))
b=int(input("Enter the second number :"))
c=1
for i in range(1,min(a,b)):
    if(a%i==0 and b%i==0):
        c=i
print("Hcf of ",a,"and",b,"are :",c)
