"""Voice module for speech recognition and text-to-speech."""

import asyncio
from typing import Optional, Callable
import os


class VoiceModule:
    """Handles voice interaction using local speech recognition and TTS."""
    
    def __init__(self, config):
        """
        Initialize the voice module.
        
        Args:
            config: Configuration object
        """
        self.config = config
        self.recognition_engine = config.get('voice.speech_recognition.engine', 'whisper')
        self.recognition_model = config.get('voice.speech_recognition.model', 'base')
        self.tts_engine = config.get('voice.text_to_speech.engine', 'coqui-tts')
        self.tts_model = config.get('voice.text_to_speech.model')
        self.wake_word = config.get('voice.wake_word', 'assistant')
        self.is_listening = False
        print(f"  Voice module configured: {self.recognition_engine} + {self.tts_engine}")
    
    def process(self, request: str, context: Optional[dict] = None) -> str:
        """
        Process a voice-related request.
        
        Args:
            request: The voice request
            context: Additional context
            
        Returns:
            Response text (which can be spoken)
        """
        context = context or {}
        
        if 'speak' in request.lower():
            text_to_speak = context.get('text', request)
            self.speak(text_to_speak)
            return f"Speaking: {text_to_speak}"
        elif 'listen' in request.lower():
            return "Starting voice listener..."
        else:
            return "Voice module ready for speech recognition and text-to-speech."
    
    def listen_once(self) -> str:
        """
        Listen for a single voice command.
        
        Returns:
            Transcribed text
        """
        try:
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5)
                print("Processing...")
                
                # Use Whisper for local recognition if available
                try:
                    text = recognizer.recognize_whisper(audio, model=self.recognition_model)
                    return text
                except:
                    # Fallback to Google Speech Recognition (requires internet)
                    text = recognizer.recognize_google(audio)
                    return text
        except Exception as e:
            return f"Error listening: {e}"
    
    async def start_listening(self, callback: Optional[Callable] = None):
        """
        Start continuous listening for voice commands.
        
        Args:
            callback: Function to call with transcribed text
        """
        self.is_listening = True
        print(f"Voice listener started. Say '{self.wake_word}' to activate.")
        
        while self.is_listening:
            try:
                text = self.listen_once()
                
                if self.wake_word.lower() in text.lower():
                    print(f"Wake word detected: {text}")
                    if callback:
                        response = callback(text)
                        self.speak(response)
                
                await asyncio.sleep(0.1)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Listening error: {e}")
                await asyncio.sleep(1)
    
    def stop_listening(self):
        """Stop continuous listening."""
        self.is_listening = False
        print("Voice listener stopped.")
    
    def speak(self, text: str) -> bool:
        """
        Convert text to speech and play it.
        
        Args:
            text: Text to speak
            
        Returns:
            True if successful, False otherwise
        """
        try:
            # Try using pyttsx3 as a free, local TTS option
            import pyttsx3
            
            engine = pyttsx3.init()
            engine.setProperty('rate', 150)  # Speed
            engine.setProperty('volume', 0.9)  # Volume
            
            print(f"Speaking: {text}")
            engine.say(text)
            engine.runAndWait()
            return True
        except ImportError:
            print("TTS not available. Install pyttsx3: pip install pyttsx3")
            print(f"Would speak: {text}")
            return False
        except Exception as e:
            print(f"Error speaking: {e}")
            return False
    
    def transcribe_audio_file(self, audio_file: str) -> str:
        """
        Transcribe an audio file.
        
        Args:
            audio_file: Path to audio file
            
        Returns:
            Transcribed text
        """
        try:
            import speech_recognition as sr
            
            recognizer = sr.Recognizer()
            
            with sr.AudioFile(audio_file) as source:
                audio = recognizer.record(source)
                
                try:
                    # Use Whisper for better accuracy
                    text = recognizer.recognize_whisper(audio, model=self.recognition_model)
                    return text
                except:
                    # Fallback
                    text = recognizer.recognize_google(audio)
                    return text
        except Exception as e:
            return f"Error transcribing audio: {e}"
    
    def save_speech_to_file(self, text: str, output_file: str) -> bool:
        """
        Convert text to speech and save to file.
        
        Args:
            text: Text to convert
            output_file: Output audio file path
            
        Returns:
            True if successful
        """
        try:
            from TTS.api import TTS
            
            tts = TTS(model_name=self.tts_model)
            tts.tts_to_file(text=text, file_path=output_file)
            print(f"Speech saved to: {output_file}")
            return True
        except Exception as e:
            print(f"Error saving speech: {e}")
            return False
    
    def cleanup(self):
        """Cleanup resources."""
        self.stop_listening()
