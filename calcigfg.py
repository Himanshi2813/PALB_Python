def utility(a, b, opr):
#code here
    if (opr==1):
        print(a+b)
    elif (opr==2):
        print(b-a)
    elif (opr==3):
        print(a*b)
    else:
        print("Invalid Input")
a,b=input().split( )
a=int(a)
b=int(b)
opr=int(input())
print(str(utility(a,b,opr)))