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
    stack_operations = ["push", "pop"]
    array_operations = ["append", "remove"]
    
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

    if data_structure == "Array":
        append_count = code.count("append")
        remove_count = code.count("remove")
        print("\nAdditional Array Operations Detected:")
        print("No of append operations:", append_count)
        print("No of remove or index operations:", remove_count)

    if data_structure == "Stack":
            analyze_stack_operations(code, operations_count)

def analyze_stack_operations(code, operations_count):
    """Perform aggregate analysis of stack operations."""
    push_count = code.count("push")
    pop_count = code.count("pop")
    total_count = push_count+pop_count

    print("\nAggregate Analysis of Stack Operations:")
    print(f"Push Count: {push_count}/{total_count} ({push_count/total_count:.2%})")
    print(f"Pop Count: {pop_count}/{total_count} ({pop_count/total_count:.2%})")

# Example usage:
file_path = "stack1.py"
analyze_code(file_path)
