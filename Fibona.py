#Fibonaaci Series

n=int(input("Enter the value : "))

n=10
a,b=0,1

for i in range(n):
    print(a,end=" ")   #0 1 1 2 3 5 8 13 21 34 
    a,b=b,a+b          #Update values

#Swap 2 num
temp=a
a=b
b=temp