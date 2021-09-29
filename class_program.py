class Person:
    def __init__(self,a,b,c):
        self.name=a
        self.address=b
        self.place=c
    def display(self):
        print(self.name,self.address,self.place)



class Employee(Person):
    def __init__(self,dept,sal,name,address,place):
        Person.__init__(self,name,address,place)
        self.dept=dept
        self.sal=sal
    def display1(self):
        print(self.name,self.address,self.place)



p=Person("jhansi","ongole","andhra pradesh")
p.display()

e1=Employee("dd","10000","john","blr","karnataka")
e1.display1()

e2=Employee("ww","1323","sad","qweq","wq")
e2.display1()

print(getattr(e1,"place"))
print(hasattr(e1,"smd"))
print(hasattr(e1,"name"))
print(setattr(e1,"age",8))
delattr(e1,"age") #

