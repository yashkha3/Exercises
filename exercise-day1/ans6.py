import math

a=0
c= 50
h = 30
result =[]
Dv=input("enter the value of D\n").split(",")
d = [int(i) for i in Dv]



while(a<len(d)):
    ans = str(round(math.sqrt((2*c*d[a])/h)))
    result.append(ans)
    a = a+1


print(",". join(result))