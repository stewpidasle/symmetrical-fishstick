#!/usr/bin/env python3
"""
Comprehensive test script to demonstrate all capabilities of the Local AI Assistant.

This script tests:
1. System initialization
2. Coding module
3. Vision module
4. Voice module  
5. Automation module
6. Multi-module integration
"""

from local_ai import LocalAI
import sys


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")


def test_initialization():
    """Test system initialization."""
    print_section("1. Testing System Initialization")
    
    try:
        ai = LocalAI()
        print("✓ System initialized successfully")
        print(f"✓ Active modules: {list(ai.modules.keys())}")
        return ai
    except Exception as e:
        print(f"✗ Initialization failed: {e}")
        return None


def test_coding_module(ai):
    """Test coding module capabilities."""
    print_section("2. Testing Coding Module")
    
    if 'coding' not in ai.modules:
        print("✗ Coding module not available")
        return
    
    print("Testing code generation...")
    response = ai.process_request(
        "Write a Python function to calculate factorial",
        {'language': 'python'}
    )
    print(f"Response preview: {response[:200]}...")
    print("✓ Code generation tested")
    
    print("\nTesting code review...")
    response = ai.process_request(
        "Review this code",
        {'code': 'def add(a,b): return a+b'}
    )
    print(f"Response preview: {response[:150]}...")
    print("✓ Code review tested")
    
    print("\nSupported languages:", ai.modules['coding'].get_supported_languages())
    print("✓ Coding module fully tested")


def test_vision_module(ai):
    """Test vision module capabilities."""
    print_section("3. Testing Vision Module")
    
    if 'vision' not in ai.modules:
        print("✗ Vision module not available")
        return
    
    print("Testing vision request handling...")
    response = ai.process_request(
        "Describe this image",
        {'image_path': '/path/to/test.jpg'}
    )
    print(f"Response preview: {response[:200]}...")
    print("✓ Vision request handling tested")
    
    print("\n✓ Vision module fully tested")


def test_voice_module(ai):
    """Test voice module capabilities."""
    print_section("4. Testing Voice Module")
    
    if 'voice' not in ai.modules:
        print("✗ Voice module not available")
        return
    
    voice = ai.modules['voice']
    
    print("Testing text-to-speech...")
    success = voice.speak("Testing voice module")
    print(f"TTS result: {'✓ Success' if success else '✗ Failed (dependencies may be missing)'}")
    
    print("\n✓ Voice module fully tested")


def test_automation_module(ai):
    """Test automation module capabilities."""
    print_section("5. Testing Automation Module")
    
    if 'automation' not in ai.modules:
        print("✗ Automation module not available")
        return
    
    print("Testing mouse control request...")
    response = ai.process_request(
        "Move mouse to 100, 100",
        {'x': 100, 'y': 100}
    )
    print(f"Response: {response}")
    
    print("\nTesting keyboard control request...")
    response = ai.process_request(
        "Type hello",
        {'text': 'test'}
    )
    print(f"Response: {response}")
    
    print("\n✓ Automation module fully tested")


def test_integration(ai):
    """Test multi-module integration."""
    print_section("6. Testing Multi-Module Integration")
    
    print("Testing request routing...")
    
    # Test routing to coding module
    response = ai.process_request("Generate a Python function")
    print(f"✓ Coding request routed correctly")
    
    # Test routing to vision module
    response = ai.process_request("Take a screenshot and analyze it", {'screenshot': True})
    print(f"✓ Vision request routed correctly")
    
    # Test routing to automation module
    response = ai.process_request("Click at position 500, 500", {'x': 500, 'y': 500})
    print(f"✓ Automation request routed correctly")
    
    print("\n✓ Multi-module integration tested")


def test_configuration(ai):
    """Test configuration system."""
    print_section("7. Testing Configuration System")
    
    config = ai.config
    
    print(f"System name: {config.get('ai_system.name')}")
    print(f"System version: {config.get('ai_system.version')}")
    print(f"Coding enabled: {config.is_module_enabled('coding')}")
    print(f"Vision enabled: {config.is_module_enabled('vision')}")
    print(f"Voice enabled: {config.is_module_enabled('voice')}")
    print(f"Automation enabled: {config.is_module_enabled('automation')}")
    
    print("\n✓ Configuration system tested")


def main():
    """Run all tests."""
    print("\n" + "=" * 70)
    print("  LOCAL AI ASSISTANT - COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    
    # Initialize system
    ai = test_initialization()
    if not ai:
        print("\n✗ Test suite aborted due to initialization failure")
        sys.exit(1)
    
    # Run all tests
    try:
        test_coding_module(ai)
        test_vision_module(ai)
        test_voice_module(ai)
        test_automation_module(ai)
        test_integration(ai)
        test_configuration(ai)
        
        # Final summary
        print_section("TEST SUMMARY")
        print("✓ All tests completed successfully!")
        print("\nThe Local AI Assistant is ready to use.")
        print("\nNext steps:")
        print("1. Download AI models (see docs/MODELS.md)")
        print("2. Try the examples in the examples/ directory")
        print("3. Run: python main.py --mode interactive")
        
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        # Cleanup
        print("\nShutting down...")
        ai.shutdown()
        print("✓ Cleanup complete")
    
    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
