s={i for i in range(1,6)}
print(s)


#Create set of squares
s={i*i for i in range(1,6)}
print(s)


#Even numbers set
s={i for i in range(1,11) if i%2==0}
print(s)


#Remove duplicates from list
l=[1,2,2,3,4,4,5]
s={i for i in set(l)}
print(s)


#Uppercase letters from string
s="harshi"
S={i.upper() for i in s}
print(S)


#Replace negative numbers with 0
l=[10,-5,20,-8]
d={i:i if i>0 else 0 for i in l}
print(d)
