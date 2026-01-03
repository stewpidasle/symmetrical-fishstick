"""
Example: Using the Automation Module

This example demonstrates how to use the automation module for computer control.
"""

from local_ai import LocalAI
import time


def main():
    # Initialize the AI system
    ai = LocalAI()
    
    print("=" * 60)
    print("Automation Module Examples")
    print("=" * 60)
    print()
    
    automation_module = ai.get_module('automation')
    
    if not automation_module:
        print("Automation module not enabled!")
        return
    
    # Example 1: Mouse control
    print("1. Mouse Control")
    print("-" * 60)
    request = "Move mouse to position 500, 500"
    response = ai.process_request(request, {'x': 500, 'y': 500})
    print(f"Request: {request}")
    print(f"Response: {response}")
    print()
    time.sleep(1)
    
    # Example 2: Keyboard input
    print("2. Keyboard Input")
    print("-" * 60)
    request = "Type hello world"
    response = ai.process_request(request, {'text': 'Hello, World!'})
    print(f"Request: {request}")
    print(f"Response: {response}")
    print()
    time.sleep(1)
    
    # Example 3: Hotkey press
    print("3. Hotkey Press")
    print("-" * 60)
    request = "Press ctrl+c"
    response = ai.process_request(request, {'keys': ['ctrl', 'c']})
    print(f"Request: {request}")
    print(f"Response: {response}")
    print()
    
    # Example 4: File operations
    print("4. File Operations")
    print("-" * 60)
    request = "Copy file from source to destination"
    response = ai.process_request(request, {
        'source': '/path/to/source.txt',
        'destination': '/path/to/destination.txt'
    })
    print(f"Request: {request}")
    print(f"Response: {response}")
    print()
    
    # Example 5: Complex task
    print("5. Complex Task Execution")
    print("-" * 60)
    task = "Open notepad, type a message, and save the file"
    result = automation_module.execute_complex_task(task)
    print(f"Task: {task}")
    print(f"Result:\n{result}")
    print()
    
    # Cleanup
    ai.shutdown()


if __name__ == '__main__':
    main()
