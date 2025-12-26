#Reverse a List

a=[1,2,3,4]
a.reverse()
print(a)          #[4,3,2,1]

#Reverse Using Slicing 
[] list       a=[1,2,3,4]
() tuple      b=(1,2,3,4)
" " String    s="SABARISH"

print(a[::-1])     #[4,3,2,1]
print(b[::-1])     #(4,3,2,1) 
print(s[::-1])     #HSIRABAS

#Reverse Using Reversed()
a=[1,2,3]
print(list(reversed(a)))     #[3,2,1]

s="SABARISH"
print("".join(reversed(s)))  #HSIRABAS

#