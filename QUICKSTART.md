# Quick Start Guide

Get up and running with Local AI Assistant in 5 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/stewpidasle/symmetrical-fishstick.git
cd symmetrical-fishstick

# Install dependencies
pip install -r requirements.txt
```

## First Run (Without Models)

You can test the system immediately without downloading models:

```bash
python main.py --command "Hello, test the system"
```

This will show you the system architecture and module initialization.

## Download Models (For Full Functionality)

### Quick Download
```bash
# Install Hugging Face CLI
pip install huggingface-hub

# Download CodeLlama (for coding)
huggingface-cli download TheBloke/CodeLlama-7B-Instruct-GGUF \
  codellama-7b-instruct.Q4_K_M.gguf --local-dir models/

# Update config.yaml with the exact filename
```

## Try It Out

### 1. Interactive Mode
```bash
python main.py --mode interactive
```

Then type commands like:
- "Write a Python function to reverse a string"
- "Help me debug this code"
- "Take a screenshot and describe it"

### 2. Single Commands
```bash
python main.py --command "Generate a Python hello world program"
```

### 3. API Mode
```bash
python main.py --mode api
```

Then visit http://localhost:8000/docs for interactive API documentation.

## Basic Examples

### Coding
```python
from local_ai import LocalAI

ai = LocalAI()
response = ai.process_request(
    "Write a function to calculate factorial",
    {'language': 'python'}
)
print(response)
ai.shutdown()
```

### Vision
```python
from local_ai import LocalAI

ai = LocalAI()
vision = ai.get_module('vision')

# Analyze a screenshot
result = vision.capture_and_analyze('screenshot')
print(result)
ai.shutdown()
```

### Voice
```python
from local_ai import LocalAI

ai = LocalAI()
voice = ai.get_module('voice')

# Text-to-speech
voice.speak("Hello! I am your AI assistant.")

# Listen to a command
text = voice.listen_once()
print(f"You said: {text}")
ai.shutdown()
```

### Automation
```python
from local_ai import LocalAI

ai = LocalAI()
response = ai.process_request(
    "Click at position 500, 500",
    {'x': 500, 'y': 500}
)
print(response)
ai.shutdown()
```

## Configuration

Edit `config.yaml` to:
- Enable/disable modules
- Change model paths
- Adjust safety settings
- Configure API settings

## What's Next?

1. **Full Installation**: See [INSTALLATION.md](docs/INSTALLATION.md)
2. **Download Models**: See [MODELS.md](docs/MODELS.md)
3. **Learn the API**: See [API.md](docs/API.md)
4. **Try Examples**: Check the `examples/` directory

## Common Issues

**"Model not found"**: The system works without models but with limited functionality. Download models for full features.

**"PyAutoGUI not installed"**: Install automation dependencies:
```bash
pip install pyautogui
```

**"Speech Recognition not working"**: Install voice dependencies:
```bash
pip install SpeechRecognition pyttsx3
```

## Help

- [Full Documentation](README.md)
- [GitHub Issues](https://github.com/stewpidasle/symmetrical-fishstick/issues)

Happy coding! 🚀
