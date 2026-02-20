'''if 2==4:
    print("Hell0")
elif 2!=2:
    print("Hi")
else:
    print("Bye")'''


#1.Eligible for vote or not
'''
age = int(input("Enter your age:"))
if age>=18:
    print("Eligible")
else:
    print("Not eligible")
'''
'''
#2.Check if a number is positive,negative or zero.
num=int(input("Enter the number:"))
if num>0:
    print(num,"is a Positive")
elif num<0:
    print(num,"is a Negative")
else:
    print("Zero")


#3.Check if a number is even or odd.
num=int(input("Enter a number:"))
if num%2==0:
    print(num,"is an even number")
else:
    print(num,"is a odd number")


#4.A shop gives a 10% discount if the purchase amount is more than 1000rs.Write a python program to calculate the final bill amount.
amount=int(input("Enter the amount:"))
if amount>1000:
    discount=(amount*10)/100
else:
    discount=0
final_bill=amount-discount
print("Final amount is",final_bill)

'''
'''
#5.Find the largest of three numbers entered by the user.
a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if a>b and a>c:
    print(a,"is the largest number")
elif b>a and b>c:
    print(b,"is the largest number")
else:
    print(c,"is the largest number")
'''

'''#5.Check given year is leap or not-ASS
year=int(input("Enter Year:"))
if year%4==0:
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")
#Nested if
'''
'''if 2==4:
j    if 2==3:
        print("Hi")
elif 2!=8:
    print("Hello")
else:
    print("bye")
'''
#Check whether a number is a multiple of both 3 and 7
'''num=int(input("Enter number:"))
if num%3==0 and num%7==0:
    print(num,"is a multiple of botha 3 and 7")
else:
    print(num,"is not multiple of 3 and 7")
'''
#Check whether a character is vowel or consonant
'''
char=input("Enter char:")
v="aeiouAEIOU"
if char in v:
    print(char,"is vowel")
else:
(    print(char,"is consonant")
'''
#Check whether a number is a 2 digit number
'''
num=int(input("Enter num:"))
if num<100 and num>9 or num>-100 and num<-9:
    print(num,"is a 2 digit number")
else:
    print(num,"is not a 2 digit number")
'''
#Check whether a given number is greater than 10
'''
num=int(input("Enter num:"))
if num>10:
    print(num,"is greater than 10")
else:
    print(num,"is not greater than 10")'''
#Check whether a number is divisible by 5
'''
num=int(input("Enter num:"))
if num%5==0:
    print(num,"is divisible by 5")
else:
    print(num,"is not divisible by 5")
'''
#Check whether a number is inside the range 10 to 50
'''
num=int(input("Enter num:"))
if num>=10 and num<50:
    print("Inside the range")
else:
    print("Not inside the range")
'''
#Check whether a number is divisible by 4,Not divisible by 8
'''
num=int(input("Enter number:"))
if num%4==0 and num%8!=0:
    print(num,"is divisible by 4 only")
else:
    print(num,"is divisible by both")
    
#Write a program to validate username and password
    #username="admin"
    #password="1234"
'''
'''
name=input("Enter Username:")
pw=int(input("Enter password:"))
username="admin"
password=1234
if name==username :
    if pw==password:
        print("Welcome")
    else:
        print("Please enter correct password")
elif name!=username and pw==password:
    print("Please enter correct username")
else:
    print("Sorry,try again")
'''


#LOOPING STMTS
#while loop
'''
a="Harshi"
while a=="Harshi":
    print("Harshitha")
    a=False
'''

#count 1 to 5
'''
count=1
while count<=5:
    print(count)
    count+=1
'''
#Descending order
'''
count=5
while count>=1:
    count-=1
    print(count)
'''

#Print the 5 table
'''
a=1
while a<=10:
    print("5 *",a ,"=",5*a)
    a+=1
 '''   
'''
i=1
while i<=3:
    print("Inside loop:",i)
    i+=1
else:
    print("Loop finished")
'''
'''
i=0
a=i
while a<=5:
    i+=a
    a+=1
print(i)
'''
'''
count=5
while count>=1:
    print(count*"*")
    count-=1
'''
'''
count=1
while count<=5:
    print(count*"*")
    count+=1
'''  
'''        
count=4
while count>=1:
    print(4*" *")
    count-=1
 '''
'''x=0
while x<=3:
    while x<=2:
        print(x)
        x+=1
    print("I'm outer loop x:",x)
    x+=1
    print(x)
'''
'''i=1
while i<=5:
    print("*$"*i)
    i+=1


i=1
while i<=5:
    j=1
    while j<=i:
        print(i,end="")
        j+=1
    print()
    i+=1


i=1
while i<=5:
    j=1
    while j<=i:
        print(j,end="" )
        j+=1
    print()
    i+=1
'''


#Butterfly Pattern
'''
n=3
i=1
while i<=n:
    print("*"*i," "*(2*(n-i))+"*"*i)
    i+=1
i=n
while i>=1:
    print("*"*i+" "*(2*(n-i)+"*"*i))
    i-=1
'''
#For Loop
'''sonu="harshi"
for harshi in sonu:
    print(sonu)
'''
'''
for harshi in "harshi":
    print(harshi,end="//")'''
'''
for var in "12345"+"harshi":
    print(var,end=" ")'''
'''for i in "hi"*3:
    print(i)'''
'''a="b"
for b in a:
    print(a)
    '''

'''
for mine in "var":
    print(mine)
'''
'''
for i in range(7):
    print(i)
'''

'''for i in range(1,8):
    print(i)
'''
'''
for i in range(1,9,2):
    print(i)
'''

#Sum of 5 numbers
'''
count=0
for i in range(1,6):
    count+=i
print(count)


#Multiplication
count=1
for i in range(1,4):
    count*=i
print(count)
'''
#Descending
'''
count=7
for i in range(0,7):
    count-=1
    print(count)
'''
'''
for i in range(0,11,2):
    print(i)
'''
'''
for i in range(0,11):
    if i%2!=0:
        print(i)
'''

'''
for i in range(6):
    print(i*"*")
'''
'''

for i in range(6,0,-1):
    print("*"*i)
'''

'''
#Hallow Square
n=8
for i in range(8):
    for j in range(8):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()



#Hallow Rectangle

for i in range(5):
    for j in range(8):
        if i == 0 or i ==4 or j == 0 or j ==7:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


#Hallow pyramid
n=5
for i in range(1,n+1):
    print(" "* (n - i), end="")
    for j in range(1,2*i):
        if j==1 or j==2*i-1 or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
'''

for i in range(1,5):
    for j in range(1,4):
        print((i,j),end="")
    print()
'''
'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 and j<=5 :
            print("= ",end="")
        else:
             print(" ",end="")
    print()
'''

'''
for i in range(1,6):
    for j in range(1,6):
        if i==3 or j==3:
            print("= ",end="")
        else:
             print(" ",end=" ")
    print()
'''

'''
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5 :
            print("=",end=" ")
        else:
             print(" ",end=" ")
    print()
'''

'''

for i in range(1,6):
    for j in range(1,6):
        if i<=5 or i==3 and j==3 or j==2 or j==4:
            print("= ",end="")
        else:
             print(" ",end="")
    print()

'''

'''

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==0 or j==6:
            print("*",end="")
        else:
            print("0 1 2",end="")
    print()
'''
'''
for i in range(0,5):
    for j in range(0,5):
        if i == 0 or i == 4 or j == 0 or j ==4:
            print("*",end=" ")
        else:
            print(j-1,end=" ")
    print()
'''
'''


for i in range(1,6):
    for j in range(1,8):
        if i==1 or i==5 or j==1 or j==7:
            print("*",end=" ")
        else:
            if j%2==0:
                print(j-2,end=" ")
            else:
                print("*",end=" ")
    print()

'''

for i in range(1,6):
    for j in range(1,8):
        if i==1 or i==5 or i==3 or j==1 or j==3 or j==7:
            print("*",end=" ")
        else:
            if j%2==0:
                print(j-2,end=" ")
            else:
                print("*",end=" ")
            
    print()

#Transverse stmts
'''
for i in range(4):
    if i==3:
        break
    print(i)
'''
'''
for i in range(7):
    if i==6:
        break
    print(i)

'''
'''
name="Harshitha"
for ch in name:
    if ch=='t':
        break
    print(ch,end=" ")
'''


for i in range(1,45):
    if i%3==0:
        break
    print(i)
