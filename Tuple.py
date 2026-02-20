#Create tuple from range
t=tuple(i for i in range(1,6))
print(t)


#Squares of tuple elements
t=tuple(i*i for i in range(1,5))
print(t)


#Convert tuple values to uppercase
t=('a','b','c')
T=tuple(i.upper() for i in t)
print(T)


#Get even numbers from tuple
t=(1,2,3,4,5,6)
T=tuple(i for i in t if i%2==0)
print(T)


#ASCII values from tuple
t=('a','b','c')
T=tuple(ord(i) for i in t)
print(T)
