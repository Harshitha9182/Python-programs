#Variable[Start:Stop:Step]
'''
s="Harshi"
s=s[::-1]
print(s)
print(s[0:7])
print(s[0:4:1])
print(s[0])
print(s[1])
print(s[-1])
print(s[-4])
print(s[0:2])
'''

stri='go"h"hello"i"od'
'''print(stri[-10:-5])
print(stri[-7:-2])
print(stri[-4:])
print(len(stri))
print(stri.count('h'))
print(stri.count(stri))
print(stri.upper())
print(stri.lower())
print(stri.title())
print(stri.find('g'))
print(stri.index('h'))
print("".join(reversed(stri)))
print(stri[-1:-5:-1])
print(stri[-6:-11:-1])
'''
'''
s='harshi"sonu'
print(s.isalpha())
print(stri[:-3:-1])
'''

#Reverse a string
'''
string="hello"
rev_string=""
for i in string:
    rev_string=i+rev_string
print(rev_string)
'''

'''
string="hello"
rev_string=""
i=len(string)-1
while i>=0:
    rev_string=rev_string+string[i]
    i-=1
print(rev_string)'''

'''
s="HelloWorlD"
print(s[2:9])
print(s[-7:-1])
print(s[-2:-9:-1])'''


'''

s = "Python"
start = 1
end = 5

i = start
while i < end:
    print(s[i], end="")
    i += 1




s = "Python"
i = 0

while i < len(s):
    print(s[i], end="")
    i += 1



s = "Python"

i = 0
step = 2

while i < len(s):
    print(s[i], end="")
    i += step

'''


s = "Harshi"
start = -5
end = -1

i = start
while i < end:
    print(s[i], end="")
    i += 1

