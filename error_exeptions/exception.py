num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def divide(num1, num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        return "Divisin by zero is not allowed"
    else:
        return result
print(divide(num1, num2))