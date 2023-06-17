#Arithmetic operators calculator
print("ON")
print("------------------------------")
n1=int(input("Enter first number:"))
n2=int(input("Enter second number"))
if n1 and n2!=0:
    print("Addition=",n1+n2)
    print("Subtraction=",n1-n2)
    print("Multiplication=",n1*n2)
    print("Division=",n1/n2)
    print("Modulus=",n1%n2)
    print("Floor division=",n1//n2)
    print("Exponential=",n1**n2)
else:
    print("Enter positive numbers!!")  

print("END")
print("------------------------------")