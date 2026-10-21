#fucntions
def add(a,b):
    return a+b

print("The sum of 5 and 10 is:", add(5,10))
print("The sum of 20 and 30 is:", add(20,30))
print("The sum of 100 and 200 is:", add(100,200))

def greet(name):
    print(f"Hello " + name + ", Welcome to Python Programming!")

greet("Guru")


#to build a calculator using functions
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    elif operation == "modulus":
        if b != 0:
            return a % b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

print("The result of addition is:", calculator(10, 50, "add"))
print("The result of subtraction is:", calculator(10, 9, "subtract"))
print("The result of multiplication is:", calculator(10, 508, "multiply"))
print("The result of division is:", calculator(11, 6, "divide"))
print("The result of modulus is:", calculator(30, 10, "modulus"))


    