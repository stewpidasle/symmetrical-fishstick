"""
Example: Using the Vision Module

This example demonstrates how to use the vision module for image analysis.
"""

from local_ai import LocalAI


def main():
    # Initialize the AI system
    ai = LocalAI()
    
    print("=" * 60)
    print("Vision Module Examples")
    print("=" * 60)
    print()
    
    vision_module = ai.get_module('vision')
    
    if not vision_module:
        print("Vision module not enabled!")
        return
    
    # Example 1: Analyze a screenshot
    print("1. Screenshot Analysis")
    print("-" * 60)
    request = "What do you see on my screen?"
    response = ai.process_request(request, {'screenshot': True})
    print(f"Request: {request}")
    print(f"Response:\n{response}")
    print()
    
    # Example 2: Analyze an image file
    print("2. Image File Analysis")
    print("-" * 60)
    request = "Describe this image"
    response = ai.process_request(request, {'image_path': '/path/to/image.jpg'})
    print(f"Request: {request}")
    print(f"Response:\n{response}")
    print()
    
    # Example 3: OCR - Extract text from image
    print("3. OCR - Text Extraction")
    print("-" * 60)
    request = "Read the text in this image"
    response = ai.process_request(request, {'image_path': '/path/to/text_image.jpg'})
    print(f"Request: {request}")
    print(f"Response:\n{response}")
    print()
    
    # Example 4: Direct screenshot capture and analysis
    print("4. Direct Screenshot Capture")
    print("-" * 60)
    result = vision_module.capture_and_analyze('screenshot')
    print(f"Result:\n{result}")
    print()
    
    # Cleanup
    ai.shutdown()


if __name__ == '__main__':
    main()
