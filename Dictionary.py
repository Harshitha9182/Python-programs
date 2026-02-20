#Create dictionary with numbers and squares
d={i:i*i for i in range(1,6)}
print(d)


#Create dictionary from list
l=[10,20,30]
d={i:i*2 for i in l}
print(d)


#Convert string to ASCII dictionary
s="HARSHI"
d={i:ord(i) for i in s}
print(d)


#Only even numbers dictionary
d={i:i*i for i in range(1,11) if i%2==0}
print(d)


#Swap keys and values
d={"name":"Harshi","age":21,"course":"DS"}
D={v:k for k ,v in d.items()}
print(D)


#Convert string to uppercase dictionary
s="harshitha"
d={i:i.upper()for i in s}
print(d)
