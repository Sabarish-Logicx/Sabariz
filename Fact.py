#Factorial using loop

#User input
num = int(input("Enter a number: "))
          
num = 4
factorial = 1
for i in range(1, num + 1):
        factorial *= i
print("The factorial of", num, "is", factorial)
