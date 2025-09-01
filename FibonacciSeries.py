
#Input From User
n=int(input("Enter a Number : "))

n=12
a,b=0,1
count=0
#if n<=0:
#  print("Please Enter a positive terms")
#elif n==1:
print("Fibonacci Series up to ",n,"Terms")
# print (a)
#else:
#  print("Fibonacci Series")
while count<n:
        print(a,end=" ")
        c=a+b
        a=b
        b=c
        count+=1
