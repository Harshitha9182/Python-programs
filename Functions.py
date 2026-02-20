def fun():
    print("Hello")
fun()


def sum():
    a=1
    b=2
    c=a+b
    print(c)
sum()


def bru():
    print("step1:Boil the milk")
    print("step2:Add some water")
    print("step3:Add sugar")
    print("step4:Add bru powder")
    print("step5:Bru is ready")
    print("step6:Take it into the cup")
    print("step7:sip the bru and feel like guru")
bru()

#Odd

def fun():
    for a in range(10):
        if a%2!=0:
            print(a)
fun()


#Square pattern
def patt():
    for i in range(4):
        for j in range(4):
            print("*",end=" ")
        print()

patt()


#Using continue
def hars():
    for i in range(10):
        if i==5:
            continue
        print(i)
hars()



#Arithmetic op

def arith():
    a=int(input("a:"))
    b=int(input("b:"))
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b)
    print(a**b)
    print(a%b)
arith()



#List
def lis():
    for i in lis:
        print(lis[1:0])
lis([0,1,2,3,4])

 


#String
def hello():
    print("Hello")
hello()

#Addition
def add(a,b):
    res=a+b
    return res
print(add(2,3))




def ofun():
    x=5
    def ifun():
        x=10
        print(x)
    ifun()
    print(x)
ofun()



x = 5 # Global variable

def change_global():
    global x # Declaring x as global
    x = 10 # Changing global x
    print("Inside function:", x)

change_global()
print("Outside function:", x) # x is changed globally!



#Rectangle

def rect():
    for i in range(1,4):
        for j in range(1,7):
            print("*",end=" ")
        print()
rect()

#Printing numbers
def num():
    i=1
    while i<=5:
        print(i)
        i+=1
num()


#Printing even and odd numbers
def even():
    for i in range(1,11):
        if i%2==0:
            print(i,":even")
        else:
            print(i,":odd")
even()

#List
def lis():
    l=[1,2,3,4,5,6]
    print(len(l))
    print(l.index(3))
    print(l.pop(4))
    print(l[::-1])
    print(l[:6])
lis()


#String
def st():
    S=input("Enter string:")
    print(S[0])
st()

#Comprehensions
def com():
    d={i:i**2 for i in range(1,6)}
    print(d)
    D={v:k for k,v in d.items()}
    print(D)
com()

#set
def set_():
    l=[1,2,4,3,2,6,4,7,6,3,2]
    s={i for i in set(l)}
    print(s)
set_()

#Positional Arguement
def details(name,age,course):
    print(name,age,course)
details("Harshi",21,"DS")


def ex(greet,name):
    print(greet,name)
ex("Hello","Harshi")


#Keyword Arguement
def key(name,age):
    print(name,age)
key(age=21,name="Harshi")


#Default Arguements
def default(name,age,course="DS"):
    print(name,age,course)
default("Harshi",21)


#Variable-length arguement
def num(*num):
    print(num)
num(1,2,3,4,5,3,2,4,6)


def square(*num):
    for i in num:
        print(i**2)
square(1,2,3,4,5)


def add(*n):
    l=[i+4 for i in n]
    print(l)
add(1,2,3,4)


#Keyword variable-length
def stu(**stu):
    print(stu)
stu(name="Harshi",course="DS")


