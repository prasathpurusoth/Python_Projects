a=int(input())
b=pow(a,2)
d=b%10
#print(d)
print('Square of number is '+str(b))
if(a==d):
    print("Given number is Automorphic Number")
else:
    print("Given number is Not a Automorphic Number")
