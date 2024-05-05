import re

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
    operations = {"push": 0, "pop": 0, "peek": 0} if data_structure == "Stack" else {"append": 0, "remove": 0, "index": 0}
    
    # Define operation names
    operation_names = {"Stack": {"push", "pop", "peek"}, "Array": {"append", "remove", "index"}}
    
    # Find operation occurrences using regex
    for op in operation_names[data_structure]:
        occurrences = len(re.findall(r'\b{}\b'.format(op), code))
        operations[op] += occurrences
    
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

# Example usage:
analyze_code("stack1.c")


