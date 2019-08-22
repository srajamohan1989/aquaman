def prod (num1, num2):
    value = num1 * num2
    if(value<1000):
        return value
    else:
        return num1+num2

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

result = prod(number1, number2)
print ("Result is : ", result)