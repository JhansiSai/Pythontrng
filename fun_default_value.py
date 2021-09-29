def fun(fname, lname="hello"):
    print(fname + " " + lname)


fun("emil")
fun("jhansi")
fun("sai")


def fun1(*kid):
    print("the young children" + kid[1])
    print(kid)


fun1("emil", "jhansi", "sai")


def fun2(ch1, ch2, ch3):
    print(ch2)
fun2(ch1="emil", ch2="jhansi", ch3="sai")


def fun3(**kid):
    print(kid["lname"])
fun3(fname="jhansi",lname="sai")

def fun4(name="india"):
    print("my country:"+name)
fun4("sweden")
fun4()


def fun5(food):
    print(food)
fruits=['apple','banana']
fun5(fruits)


def fun6(age):
    pass
    #print(age)
fun6(4)



