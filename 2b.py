import re
import os
import random
def detect_language(code):
    """Detect whether the code is Python or C."""
    if any(re.match(r"\s*#include", line) for line in code.split("\n")):
        return "C"
    else:
        return "Python"

def detect_data_structures(code):
    """Detect usage of stack or array."""
    stack_operations = ["push", "pop", "peek", "stack"]
    array_operations = ["append", "remove", "index", "array"]
    
    stack_count = sum(code.lower().count(op) for op in stack_operations)
    array_count = sum(code.lower().count(op) for op in array_operations)
    
    if stack_count > array_count:
        return "Stack"
    elif array_count > stack_count:
        return "Array"
    else:
        return "Unknown"

def count_operations(code, data_structure):
    """Count the number of operations related to the identified data structure."""
    operations = {"push_count": 0, "pop_count": 0, "total_count": 0} if data_structure == "Stack" else {"append": 0, "remove": 0, "index": 0}
    
    # Find operation occurrences using regex
    if data_structure == "Stack":
        operations["push_count"] = len(re.findall(r'\b{}\b'.format("push"), code))
        operations["pop_count"] = len(re.findall(r'\b{}\b'.format("pop"), code))
        operations["total_count"] = operations["push_count"] + operations["pop_count"]
    
    return operations

def analyze_code(file_path):
    """Analyze code from a file."""
    with open(file_path, "r") as file:
        code = file.read()
    
    language = detect_language(code)
    data_structure = detect_data_structures(code)
    operations_count = count_operations(code, data_structure)
    
    print("Language:", language)
    print("Data Structure:", data_structure)
    print("Operations Count:", operations_count)

    # Count array operations using provided snippet
    count = 0
    count2 = 0
    for line in code.split("\n"):
        if 'append' in line:
            count += 1
        elif 'remove' in line or 'index' in line:
            count2 += 1

    if count >= 1 or count2 >= 1:
        print("Additional Array Operations Detected:")
        print("No of append operations:", count)
        print("No of remove or index operations:", count2)

    if data_structure == "Stack":
        analyze_accounting(code, operations_count)
            

def analyze_accounting(code, operations_count):
    """Perform accounting analysis."""
    print("\nCase 1:")
    # Generating random values for push and pop operations
    push_value = random.randint(1, 100)
    pop_value = random.randint(1, 100)
    
    # Calculating total values for push and pop operations
    total_push_value = (push_value-1) * operations_count["push_count"]
    total_pop_value = (pop_value-1) * operations_count["pop_count"]

    # Displaying the accounting analysis results
    print("\nAccounting Analysis:")
    print(f"Amortized Random value for push:{push_value}")
    print(f"Amortized Random value for pop:{pop_value}")
    print(f"Total Value for Push Operations: {total_push_value}")
    print(f"Total Value for Pop Operations: {total_pop_value}")
    print(f"Net Value in Credit Bank: {total_push_value + total_pop_value}")

    print("\nCase 2:")
    # Generating random values for push and pop operations
    push_value2 = random.randint(1, 100)
    pop_value2 = random.randint(-100, 0)
    
    # Calculating total values for push and pop operations
    total_push_value2 = (push_value2-1) * operations_count["push_count"]
    total_pop_value2 = (pop_value2-1) * operations_count["pop_count"]

    # Displaying the accounting analysis results
    print("\nAccounting Analysis:")
    print(f"Amortized Random value for push:{push_value2}")
    print(f"Amortized Random value for pop:{pop_value2}")
    print(f"Total Value for Push Operations: {total_push_value2}")
    print(f"Total Value for Pop Operations: {total_pop_value2}")
    net_value=total_push_value2 + total_pop_value2
    if net_value>=0:
        print(f"Net Value in Credit Bank: {net_value}")
    else:
        print(f"Net Value in dept: {-net_value} Therefore not possible")

# Example usage:
file_path = "stack1.py"
analyze_code(file_path)