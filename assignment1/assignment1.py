# Task 1
def hello(): 
    return "Hello!"

print(hello())

# Task 2
def greet(name):
    return (f"Hello, {name}!")

print(greet("Sung"))

# Task 3
def calc(a, b, operation="multiply"):
    match operation: 
        case "add": 
            a + b
        case "subtract":
            a - b 
        case "multiply": 
            a * b
        case "divide":
            a / b
        case "modulo":
            a % b
        case "int_divide":
            a // b
        case "power":
            a ** b
