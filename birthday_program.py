list={"jhansi":"29/05/00",
    "john":"23/1/22",
    "sai":"12/3/12"
}
def birth(n):
    if n=="jhansi":
        print(n+" birthday date is "+list["jhansi"])
    elif n=="john":
        print(n + " birthday date is " + list["john"])
    else:
        print(n + " birthday date is " + list["sai"])
    k=input("enter y/n")
    if k=='y':
        h = input("enter whos birthday you want:")
        birth(h)
n=input("enter whos birthday you want:")
birth(n)