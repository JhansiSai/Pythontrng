l=[1,2,3,4,5]
print(l)
for a in l:
    print(a)
    print(type(a))
print(l)
for v in range(-10,-100,-30):
    print(v)
words=['cat','dog','monkey']
for w in words:
    print(w,len(w))
if len(w) > 5:
    words.insert(0,w)
print(words)

lst=[]
n=int(input("enter number of elements:"))
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)