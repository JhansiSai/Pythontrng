print("hello")
def add(n1,n2):
    return n1+n2
n1=int(input("enter first number"))
n2=int(input("enter second number"))
print(add(n1,n2))

def fun(n):
    r=0
    if n>0:
        r=n+fun(n-1)
    return r
print(fun(5))