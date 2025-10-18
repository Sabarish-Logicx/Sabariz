#Basic Syntax
print ("Sabarish_Logicz")

#floor Division
print(5//2)  //2

#Division
print(5/2)   //2.5

#String 
a="12"
a+="1"          //a = a+1 = "12"+"1"
print(int(a)*2)  //121*2=242

a="12"
print(a*3+"5")  //1212125

a="12"
print(a*3+5)  //KeyError

#a^AnyNum (a**n)
print(5**(2**3))   //5**(8)=5^8

print((2**2)**3)   //4^3=48

print(2**2**1)   #Base(2)^2^1=4

#String Manipulation
a="1"
b="2"
print(int(a+b)+int(b+a))  #12+21=33

a="12"
b=1
print(int(a)+b)      #13

a="12"
b=1
print(a+str(b))      #121

print("python"+str(3*2))   #python6

s="banana"
print(s.replace("a","o",2))   #bonona (first two occurance of a -> o)

s=1234
print(str(s)[::-1])       #4321 reverse

s=123456
rev=0
while a>0:
    digit=a%10
    rev=rev*10+digit
    a=a//10
    print(rev)              #654321

#array
a=[1,2,3]
b=a
b[0]=99
print(a)          #[99,2,3]

#String Reverse
def reverse_string(a)
return a[::-1]
print (reverse_string("SABARISH"))     #HSIRABAS

#without Slice
a="SABARISH"
reversed_text=""       #result==reversed_text
for ch in a:
    reversed_text=ch+reversed_text
    print(reversed_text)               #HSIRABAS

# Looping 
for i range (2,10,2)
print(i,end=" ")               # 2 4 6 8 

for i range (2,10,3)
print(i)                       # 369   

#Types
print(type(([1,2,3])))      #<class 'list'>
print(type(({1,2,3})))      #<class 'set'>
print(type((1,2,3)))        #<class 'tuple'>

#Dictionary (Dict)
student={"name"="Sabarish","age"=20}
print(type((student)))      #<class 'dict'>

#Array Sorting
Num=[4,1,3,5,6,2]
Num.sort()
#Num.sort(Reverse=flase)     #Descending [6,5,4,3,2,1]
#Num.sort(Reverse=ture)      #Ascening [1,2,3,4,5,6]
print(Num)                   #[1,2,3,4,5,6]

#Slicing
s="SABARISH"        
print(s(0:6:2))              #SBRS

string="Hello World"
print(string(0:6:3))         #Hlwl

x=[1,2,3,4,5,6]
print(x[-1])                 #3    -2 -->2,-3 -->1
print(x[1])                  #2     0 -->1,3 -->2

print(x[2:5])                #3,4,5
print(x[:5])                 #1,2,3,4
print(x[:-5])                #1
print(x[-5:])                #2,3,4,5,6

#[:] for Copy a list
a=[1,2,3]
b=a[:]
print(b)                     #[1,2,3]

#Set {}
s={1,2,3,4}
for i range
