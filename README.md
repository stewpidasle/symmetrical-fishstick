# Local AI Assistant 🤖

A completely free, local AI assistant that can code, has vision and voice capabilities, and can complete complex tasks on your computer.

## 🌟 Features

- **🔧 Coding Assistant**: Generate, review, debug, and refactor code in multiple programming languages
- **👁️ Vision**: Analyze images, screenshots, perform OCR, and understand visual content
- **🎤 Voice**: Speech recognition and text-to-speech for hands-free interaction
- **🖥️ Computer Automation**: Control mouse, keyboard, windows, files, and processes
- **🆓 100% Free**: Uses open-source models that run entirely on your local machine
- **🔒 Privacy-First**: All processing happens locally - no data sent to external servers

## 📋 Requirements

- Python 3.8 or higher
- 8GB RAM minimum (16GB recommended for larger models)
- Storage space for AI models (5-10GB depending on models chosen)
- Optional: GPU with CUDA support for faster inference

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/stewpidasle/symmetrical-fishstick.git
cd symmetrical-fishstick
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download AI Models

The system uses free, open-source models that you need to download:

#### Coding Model (CodeLlama)
```bash
# Download from Hugging Face
# Place in models/codellama-7b-instruct.gguf
```

#### Vision Model (LLaVA)
```bash
# Download from Hugging Face
# Place in models/llava-v1.5-7b.gguf
```

See [MODELS.md](MODELS.md) for detailed instructions on downloading and setting up models.

### 4. Run the Assistant

```bash
# Interactive mode (CLI)
python main.py --mode interactive

# Voice mode
python main.py --mode voice

# API server mode
python main.py --mode api

# Single command
python main.py --command "Write a Python function to sort a list"
```

## 📖 Usage Examples

### Coding

```python
from local_ai import LocalAI

ai = LocalAI()
response = ai.process_request(
    "Write a Python function to calculate fibonacci numbers",
    {'language': 'python'}
)
print(response)
```

### Vision

```python
from local_ai import LocalAI

ai = LocalAI()
response = ai.process_request(
    "What do you see in this image?",
    {'image_path': 'screenshot.png'}
)
print(response)
```

### Voice

```python
from local_ai import LocalAI

ai = LocalAI()
voice = ai.get_module('voice')

# Text-to-speech
voice.speak("Hello! I'm your AI assistant.")

# Speech recognition
text = voice.listen_once()
print(f"You said: {text}")
```

### Automation

```python
from local_ai import LocalAI

ai = LocalAI()
response = ai.process_request(
    "Click at position 100, 200",
    {'x': 100, 'y': 200}
)
print(response)
```

## 🏗️ Architecture

```
local_ai/
├── __init__.py          # Package initialization
├── config.py            # Configuration management
├── core.py              # Main orchestrator
└── modules/
    ├── coding.py        # Coding module
    ├── vision.py        # Vision module
    ├── voice.py         # Voice module
    └── automation.py    # Automation module
```

## ⚙️ Configuration

Edit `config.yaml` to customize the system:

```yaml
coding:
  enabled: true
  model:
    path: "models/codellama-7b-instruct.gguf"

vision:
  enabled: true
  model:
    path: "models/llava-v1.5-7b.gguf"

voice:
  enabled: true
  speech_recognition:
    engine: "whisper"
    model: "base"

automation:
  enabled: true
  safety:
    confirm_actions: true
```

## 🛡️ Safety Features

- **Confirmation prompts** for potentially dangerous operations
- **Restricted operations** list for sensitive actions
- **Local processing** - no data leaves your machine
- **Sandboxed execution** for automation tasks

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

This project uses the following open-source technologies:

- **LLaMA** and **CodeLlama** by Meta AI
- **LLaVA** for vision capabilities
- **Whisper** by OpenAI for speech recognition
- **Coqui TTS** for text-to-speech
- **PyAutoGUI** for automation

## 📚 Documentation

- [Installation Guide](docs/INSTALLATION.md)
- [Model Setup](docs/MODELS.md)
- [API Reference](docs/API.md)
- [Examples](examples/)

## ❓ FAQ

**Q: Do I need an internet connection?**
A: After downloading the models, the system works completely offline.

**Q: Which is the best model to start with?**
A: For coding, CodeLlama-7B is a good balance of performance and resource usage. For vision, LLaVA-v1.5-7B works well.

**Q: Can I use this on Windows/Mac/Linux?**
A: Yes! The system is cross-platform and works on all major operating systems.

**Q: How much does this cost?**
A: It's completely free! You only need to provide the hardware to run it.

## 🔮 Roadmap

- [ ] Add more model options (Mistral, Phi, etc.)
- [ ] Web UI for easier interaction
- [ ] Plugin system for extensibility
- [ ] Multi-modal task chains
- [ ] Memory and context management
- [ ] Fine-tuning capabilities

## 📧 Contact

For questions and support, please open an issue on GitHub.

---

Made with ❤️ for the open-source community
