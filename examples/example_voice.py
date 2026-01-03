"""
Example: Using the Voice Module

This example demonstrates how to use the voice module for speech recognition and TTS.
"""

from local_ai import LocalAI


def main():
    # Initialize the AI system
    ai = LocalAI()
    
    print("=" * 60)
    print("Voice Module Examples")
    print("=" * 60)
    print()
    
    voice_module = ai.get_module('voice')
    
    if not voice_module:
        print("Voice module not enabled!")
        return
    
    # Example 1: Text-to-Speech
    print("1. Text-to-Speech")
    print("-" * 60)
    text = "Hello! I am your local AI assistant."
    success = voice_module.speak(text)
    print(f"Spoke: {text}")
    print(f"Success: {success}")
    print()
    
    # Example 2: Single voice command
    print("2. Listen for a Single Command")
    print("-" * 60)
    print("Speak now (you have 5 seconds)...")
    text = voice_module.listen_once()
    print(f"You said: {text}")
    print()
    
    # Example 3: Process voice command
    print("3. Process Voice Command")
    print("-" * 60)
    response = ai.process_request("speak hello world", {'text': 'Hello World!'})
    print(f"Response: {response}")
    print()
    
    # Example 4: Transcribe audio file
    print("4. Transcribe Audio File")
    print("-" * 60)
    audio_file = "/path/to/audio.wav"
    transcription = voice_module.transcribe_audio_file(audio_file)
    print(f"Transcription: {transcription}")
    print()
    
    # Cleanup
    ai.shutdown()


if __name__ == '__main__':
    main()
