#Factorial of Single Number

def factorial(n):
    result = 1
    for i in range(1,n+1):
        result*=i
        return result
    print("5!=",factorial(5))    #120

#Factorial for Given input numbers

num=int(input("Enter a Number: "))

#num=5

factorial=1
for i in range(1,num+1):
    factorial*=i
    print(factorial)



