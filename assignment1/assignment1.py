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
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b      
            case "power":
                return a ** b
            case _:
                # Handle unknown operation strings
                raise ValueError(f"Unknown operation: {operation}")
    except ZeroDivisionError:
        # Raised when dividing by zero
        return "You can't divide by 0!"
    except TypeError:
        # Raised when operand types don't work together
        return "You can't multiply those values!"