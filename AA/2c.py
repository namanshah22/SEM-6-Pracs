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
    stack_ops = ["push", "pop", "peek"]
    array_ops = ["append", "remove", "index"]
    
    if data_structure == "Stack":
        counts = {}
        for op in stack_ops:
            counts[op] = code.count(op)
    else:  # Assume Array
        counts = {}
        for op in array_ops:
            counts[op] = code.count(op)
    return counts

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
    if data_structure == "Array":
        append_count = code.count("append")
        remove_count = code.count("remove")
        print("\nAdditional Array Operations Detected:")
        print("No of append operations:", append_count)
        print("No of remove or index operations:", remove_count)

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
    total_push_value3 = (amortized_cost_push-1) * code.count("push")
    total_pop_value3 = (amortized_cost_pop-1) * code.count("pop")
    print(f"Total Value for Push Operations: {total_push_value3}")
    print(f"Total Value for Pop Operations: {total_pop_value3}")
    net_value=total_push_value3 + total_pop_value3
    print(f"Net Value in Credit Bank: {net_value}")

# Example usage:
file_path = "stack1.py"
analyze_code(file_path)
