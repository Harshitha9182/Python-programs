#List=["David",["Hello",[58,4,["hi","good",["HI","Done"],9]]]]
#print(List[1][1][2][1][3][1][0:1])

'''

l=(1,2,3,4,5,6,7)
for i in l:
    print(i)
'''

'''
L=[10,20,[30,40],50]
print(L[2][0])
print(L[2][1])


L1=["apple",["banana","mango"],"grapes"]
print(L1[1][0])
print(L1[1][1])
print(L1[1][1][0])


L2=[10,[20,[30,40],50,60]]
print(L2[1][1][0])
print(L2[1][1][1])
'''

'''
L3=["Hi",[10,["Hello","Python"],30]]
print(L3[1][1][0])
print(L3[1][1][1])
print(L3[1][1][1][0])
'''

'''
L4=["David",["Hello",[58,4,["hi","good",["HI","Done"],9]]]]
print(L4[1][1][2][0])
print(L4[1][1][2][1])
print(L4[1][1][2][2][0])
print(L4[1][1][2][2][1])
print(L4[1][1][2][2][1][0])
'''
'''
L5=[1,[2,[3,[4,[5]]]]]
print(L5[1][1][1][1][0])
'''

'''
L6=[[10,20],[30,40],[50,60]]
print(L6[2][1])
'''

'''
L7=["Python",["Java",["C","C++","SQL"]]]
print(L7[1][1][2])
print(L7[1][1][2][:2])
'''
'''
L8=[["A","B"],["C",["D","E",["F"]]]]
print(L8[1][1][0])
print(L8[1][1][2][0])
'''
'''
L=[10,[20,30],40]
print(L[1][0])
print(L[1][1])
'''
'''
L=["A",["B","C","D"],"E"]
print(L[1][0])
print(L[1][2])
'''
'''
L=[1,[2,[3,4],5],6]
print(L[1][1][0])
print(L[1][1][1])
'''
'''
L=["Hi",[10,["Hello","Python"],30]]
print(L[1][1][0])
print(L[1][1][1])
print(L[1][1][1][0])
'''
'''
L=[[100,200],[300,[400,500]]]
print(L[1][1][0])
print(L[1][1][1])
'''
'''
L=["X",["Y",["Z",["A","B"]]]]
print(L[1][1][0])
print(L[1][1][1][1])
'''
'''
L=[5,[10,[15,[20,[25]]]]]
print(L[1][1][1][1][0])
'''

'''
L=[["apple","banana"],["mango",["grapes","orange"]]]
print(L[1][0])
print(L[1][1][1])
print(L[1][1][1][0])
'''
'''
L=[1,["Hi",[2,["Hello",[3,["python"]]]]]]
print(L[1][1][1][0])
print(L[1][1][1][1][1][0][:5])
'''
'''
L=["A",["B",["C",["D",["E",["F"]]]]]]
print(L[1][1][1][1][1][0])
'''
'''
#Max in list
l=[12,45,32,56]
max=l[0]
for i in l:
    if i>max:
        max=i
print(max)

#Min in list
l=[45,32,12,56]
min=l[0]
for i in l:
    if i< min:
        min=i
print(min)
'''

#using in built
'''
l=[23,56,43,75,21]
print(max(l))
l.insert(1,8)
print(l)
'''


#Tuple
'''
t=(1,2,3,4,5,6,7,4,3)
print(t[4])
'''
t1=(1,"hi",False,(44,(34,"Done",78),67),4.8)
#print(t1[3][1])
#lst=list(t1)
#lst[2]=True
#lst[3]=(44,58)
#lst[3]=(44,(34,"Harshi",78),67)
#t1=tuple(lst)
#print(t1[3][1][1])

#print(t1)




#List
'''
list=[]
list.append(10)
list.append(20)
list.append(30)
list.append(40)
list.append(50)
list.insert(0,100)
list.insert(6,200)
list.remove(50)
list.pop(2)
list.append(25)
print(list.index(25))
print(list.count(5))
list.extend([1,2,3])
list.reverse()
list.sort()
list.sort(reverse=True)
print(list.copy())
#list.clear()
list.pop(0)
list.pop()
print(min(list))
print(max(list))
print(list)
'''

'''
l=[1,20,11,4,78,9,0,23]
e=[]
for i in l:
    if i>=1 and i<=20:
        if i==4:
            continue
        e.append(i)
   
            
print(e)      


L=[1,2,3,4,5]
e=[]
for i in L:
    if i in L:
        e.append(i*2)
print(e)


L1=[1,2,3,4,5,6,7,8,9,10]
e=[]
for i in L1:
    if (i%2==0):
        e.append(i)
print(e)



L2=[1,2,3,4,5,6,7,8,9,10]
e=[]
for i in L2:
    if(i%2!=0):
        e.append(i)
print(e)

tuple_=("hello",)
print(type(tuple_))



lst=[ i for i in range(5)]
print(lst)

'''
'''

s="Banana"
dic={i:s.count(i) for i in s}
print(dic)

s="h a rs h i"
dic={i:s.count(i) for i in s}
print(dic)


s=input()
dic={i for i in s if i in 'aeiouAEIOU'}
print(dic)
'''
'''
#Create a list of numbers from 1 to 20 using list comprehension.
lis=[i for i in range(1,21)]
print(lis)


#Create a list of squares from 1 to 10.
lis=[i**2 for i in range(1,11)]
print(lis)


#Create a list of cubes from 1 to 10.
lis=[i**3 for i in range(1,11)]
print(lis)


#Create a list of even numbers from 1 to 20.
lis=[i for i in range(1,21) if i%2==0]
print(lis)


#Create a list of odd numbers from 1 to 20.
lis=[i for i in range(1,21) if i%2!=0]
print(lis)


#Create a list of numbers divisible by 5 from 1 to 50.
lis=[i for i in range(1,51) if i%5==0]
print(lis)


#From a list [10, 15, 20, 25, 30], create a new list with each value divisible by 2.
lis=[10,15,20,25,30]
L=[i for i in lis if i%2==0]
print(L)


#From a list [10, 15, 20, 25, 30], create a new list with each value multiplied by 2.
lis=[10,15,20,25,30]
L=[i*2 for i in lis]
print(L)


#Convert all characters of string "python" into uppercase using list comprehension.
s="python"
L=[i.upper() for i in s]
print(L)

#user input
s=input("Enter string:")
L=[i.upper() for i in s]
print(L)


#From a string "hello world", extract only vowels.
s="hello world"
L=[i for i in s if i in'aeiouAEIOU']
print(L)

#user input
s=input("Enter string:")
L=[i for i in s if i in'aeiouAEIOU']
print(L)


#From list [1, 2, 3, 4, 5], create list of squares of even numbers only.
lis=[1,2,3,4,5]
L=[i**2 for i in lis if i%2==0]
print(L)
'''

#From list [10, -5, 20, -8, 30], replace negative numbers with 0.
lis=[10,-5,20,-8,30]
L=[i if i>1 else 0  for i in lis]
print(L)


#From list [5, 12, 17, 18, 24, 32], create list of numbers greater than 15.
lis=[5,12,17,18,24,32]
L=[i for i in lis if i>15]
print(L)


#From list [1, 2, 3, 4, 5], create list where even numbers are squared and odd numbers are kept same.
lis=[1,2,3,4,5]
L=[i**2 if i%2==0 else i for i in lis]
print(L)


#From list [25, 36, 49, 64], create list of square roots (hint: use **0.5).
lis=[25,36,49,64]
L=[i**0.5 for i in lis]
print(L)


#Count length of each word in list
lis=['apple','banana','cherry']
L=[len(i) for i in lis]
print(L)


#Extract repeated letters from string "programming".
s="programming"
L=[i for i in set(s) if s.count(i)>1]
print(L)


#Remove spaces from string "hello world".
s="hello world"
L="".join([i for i in s if i!=" "])
print(L)


#Create list of ASCII values of characters in "ABC" using ord().
L=[ord(i) for i in 'ABC']
print(L)


#Create list of tuples (number, square)
L=[(i,i*i)for i in range(1,11)]
print(L)
