"""
Example: Using the Coding Module

This example demonstrates how to use the coding module for various tasks.
"""

from local_ai import LocalAI


def main():
    # Initialize the AI system
    ai = LocalAI()
    
    print("=" * 60)
    print("Coding Module Examples")
    print("=" * 60)
    print()
    
    # Example 1: Code Generation
    print("1. Code Generation")
    print("-" * 60)
    request = "Write a Python function to calculate the factorial of a number"
    response = ai.process_request(request, {'language': 'python'})
    print(f"Request: {request}")
    print(f"Response:\n{response}")
    print()
    
    # Example 2: Code Review
    print("2. Code Review")
    print("-" * 60)
    code_to_review = """
def add(a, b):
    return a+b
    """
    request = "Review this code for best practices"
    response = ai.process_request(request, {'code': code_to_review})
    print(f"Request: {request}")
    print(f"Code:\n{code_to_review}")
    print(f"Response:\n{response}")
    print()
    
    # Example 3: Debugging
    print("3. Debugging Help")
    print("-" * 60)
    buggy_code = """
def divide(a, b):
    return a / b
    """
    error = "ZeroDivisionError: division by zero"
    request = "Help me debug this code"
    response = ai.process_request(request, {'code': buggy_code, 'error': error})
    print(f"Request: {request}")
    print(f"Code:\n{buggy_code}")
    print(f"Error: {error}")
    print(f"Response:\n{response}")
    print()
    
    # Cleanup
    ai.shutdown()


if __name__ == '__main__':
    main()
