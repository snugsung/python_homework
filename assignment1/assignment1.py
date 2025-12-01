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
    
# Task 4
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "int":
                return int(value)
            case "float":
                return float(value)
            case "str":
                return str(value)
            case _:
                # Unknown type
                raise ValueError(f"Unknown data type: {data_type}")
    except (ValueError, TypeError):
        # Happens if conversion is impossible
        return f"You can't convert {value} into a {data_type}."

# Task 5
def grade(*args):
    try:
        # Calculate average
        average = sum(args) / len(args)

        # Determine letter grade based on the average
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except Exception:
        # For invalid data
        return "Invalid data was provided."
    
# Task 6
def repeat(str, count):
    result = ""
    for i in range(count):
        result += str
    return result
