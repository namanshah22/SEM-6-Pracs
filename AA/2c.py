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
            analyze_potential_methods(code,operations_count)

def analyze_potential_methods(code,operations_count):
    """Analyze potential methods in the code."""
    # Calculate amortized cost for push and pop operations
    amortized_cost_push = 2
    amortized_cost_pop = 0

    print("\nPotential Methods Analysis:")
    print(f"Amortized Cost for Push Operations: {amortized_cost_push}")
    print(f"Amortized Cost for Pop Operations: {amortized_cost_pop}")
    total_push_value3 = (amortized_cost_push-1) * operations_count["push_count"]
    total_pop_value3 = (amortized_cost_pop-1) * operations_count["pop_count"]
    print(f"Total Value for Push Operations: {total_push_value3}")
    print(f"Total Value for Pop Operations: {total_pop_value3}")
    net_value=total_push_value3 + total_pop_value3
    print(f"Net Value in Credit Bank: {net_value}")

# Example usage:
file_path = "stack1.py"
analyze_code(file_path)