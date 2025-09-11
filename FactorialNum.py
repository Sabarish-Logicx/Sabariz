#Factorial of Single Number

num=int(input("Enter a Number: "))

def factorial(n)
    result = 1
    for i in range(1,n+1):
        result*=i
        return result
    print("5!=",factorial(5))    #120


#
num=5
factorial=1
for i in range(1,num+1):
    factorial*=i
    print(factorial)