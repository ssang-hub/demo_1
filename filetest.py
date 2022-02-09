a = int(input())
b = int(input())

def power(a, b):
    if b==1:
        return a
    elif b==0:
        return 1
    else:
        return power(a,int( b/2))*power(a, b-int(b/2))
print(power(a,b))