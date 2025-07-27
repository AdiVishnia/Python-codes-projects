class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

def mystery_function(a, b):
    addition_result = a + b
    subtraction_result = a - b
    return addition_result, subtraction_result

# Create instances of the Calculator class
x = Calculator(10)
y = Calculator(5)

# Use the mystery function with Calculator instances
add_result, sub_result = mystery_function(x, y)

# Print the results
print("Addition Result:", add_result.value)        # Output: Addition Result: 15
print("Subtraction Result:", sub_result.value)     # Output: Subtraction Result: 5