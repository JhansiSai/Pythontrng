f=lambda a,b:a+b
print(f(2,4))

def fun(n):
    return lambda x:x+n
f=fun(2)
print(f(0))
print(f(1))