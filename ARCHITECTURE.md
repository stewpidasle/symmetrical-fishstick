# Project Architecture

## Overview

The Local AI Assistant is a modular, extensible system for running AI capabilities locally. It's designed to be:
- **Free**: Uses only open-source models and libraries
- **Private**: All processing happens locally
- **Modular**: Easy to enable/disable features
- **Extensible**: Simple to add new capabilities

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                         User Interface                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │     CLI      │  │     API      │  │    Voice     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└────────────────────────┬────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────┐
│                      Core Orchestrator                       │
│                        (LocalAI)                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │              Configuration Manager                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                         │                                    │
│      ┌──────────────────┼──────────────────┐                │
│      ▼                  ▼                  ▼                │
│  ┌────────┐       ┌──────────┐       ┌──────────┐          │
│  │Request │       │  Module  │       │ Response │          │
│  │ Router │──────▶│ Selector │──────▶│ Handler  │          │
│  └────────┘       └──────────┘       └──────────┘          │
└─────────────────────────┬────────────────────────────────────┘
                          │
          ┌───────────────┼───────────────┬─────────────┐
          ▼               ▼               ▼             ▼
    ┌─────────┐    ┌──────────┐    ┌─────────┐   ┌──────────┐
    │ Coding  │    │  Vision  │    │  Voice  │   │Automation│
    │ Module  │    │  Module  │    │ Module  │   │  Module  │
    └─────────┘    └──────────┘    └─────────┘   └──────────┘
         │              │               │              │
         ▼              ▼               ▼              ▼
    ┌─────────┐    ┌──────────┐    ┌─────────┐   ┌──────────┐
    │CodeLlama│    │  LLaVA   │    │ Whisper │   │PyAutoGUI │
    │  Model  │    │  Model   │    │   TTS   │   │  System  │
    └─────────┘    └──────────┘    └─────────┘   └──────────┘
```

## Component Details

### 1. Core Components

#### LocalAI (core.py)
- Main orchestrator class
- Routes requests to appropriate modules
- Manages module lifecycle
- Handles configuration

#### Config (config.py)
- Loads and manages configuration
- Provides access to settings
- Supports defaults and overrides

### 2. Modules

#### Coding Module (modules/coding.py)
**Purpose**: Generate, review, debug, and refactor code

**Capabilities**:
- Code generation from natural language
- Code review and quality analysis
- Debugging assistance
- Code refactoring suggestions

**Models**: CodeLlama, Mistral, DeepSeek-Coder

**Key Methods**:
- `process(request, context)`: Main processing
- `_generate_code()`: Generate new code
- `_review_code()`: Analyze existing code
- `_debug_code()`: Debug assistance

#### Vision Module (modules/vision.py)
**Purpose**: Understand and analyze images

**Capabilities**:
- Image description and understanding
- Object detection
- OCR (text extraction)
- Screenshot analysis
- Webcam integration

**Models**: LLaVA, BakLLaVA

**Key Methods**:
- `process(request, context)`: Main processing
- `capture_and_analyze(source)`: Capture and analyze
- `_describe_image()`: Generate descriptions
- `_perform_ocr()`: Extract text

#### Voice Module (modules/voice.py)
**Purpose**: Speech recognition and text-to-speech

**Capabilities**:
- Speech-to-text transcription
- Text-to-speech synthesis
- Continuous listening mode
- Wake word detection
- Audio file transcription

**Models**: Whisper (speech recognition), Coqui TTS, pyttsx3

**Key Methods**:
- `listen_once()`: Single command
- `start_listening()`: Continuous mode
- `speak(text)`: Text-to-speech
- `transcribe_audio_file()`: File transcription

#### Automation Module (modules/automation.py)
**Purpose**: Control computer and automate tasks

**Capabilities**:
- Mouse control (click, move, drag)
- Keyboard input (type, hotkeys)
- Window management
- File operations
- Process management
- Complex task execution

**Libraries**: PyAutoGUI, psutil, subprocess

**Key Methods**:
- `process(request, context)`: Main processing
- `_handle_mouse_action()`: Mouse control
- `_handle_keyboard_action()`: Keyboard control
- `execute_complex_task()`: Multi-step tasks

### 3. User Interfaces

#### CLI Interface (main.py)
- Interactive command-line interface
- Single command execution
- Help and documentation

#### API Interface (main.py)
- REST API with FastAPI
- JSON request/response
- OpenAPI documentation
- Health check endpoints

#### Voice Interface (main.py)
- Continuous listening mode
- Wake word activation
- Voice feedback

## Data Flow

### Example: Coding Request

```
1. User Input: "Write a Python function to sort a list"
   ↓
2. LocalAI.process_request()
   ↓
3. Request Router → Detects coding keywords
   ↓
4. CodingModule.process()
   ↓
5. Load CodeLlama model (if not loaded)
   ↓
6. Generate code using LLM
   ↓
7. Format response
   ↓
8. Return to user
```

### Example: Vision Request

```
1. User Input: "What's on my screen?"
   ↓
2. LocalAI.process_request(context={'screenshot': True})
   ↓
3. Request Router → Detects vision keywords
   ↓
4. VisionModule.process()
   ↓
5. Capture screenshot
   ↓
6. Load LLaVA model (if not loaded)
   ↓
7. Analyze image with multimodal LLM
   ↓
8. Generate description
   ↓
9. Return to user
```

## Configuration

Configuration is YAML-based and hierarchical:

```yaml
ai_system:          # System metadata
  name: "..."
  version: "..."

coding:             # Module configuration
  enabled: true
  model:
    path: "..."
    
resources:          # Resource limits
  max_memory_gb: 8
  gpu_enabled: false
```

## Extension Points

### Adding a New Module

1. Create module class in `local_ai/modules/`
2. Implement required methods:
   - `__init__(config)`
   - `process(request, context)`
   - `cleanup()`
3. Register in `core.py`
4. Add configuration in `config.yaml`
5. Update documentation

### Adding a New Model

1. Implement model loading in module
2. Add configuration options
3. Update MODELS.md documentation
4. Test with new model

### Adding a New Interface

1. Create interface in `main.py`
2. Use `LocalAI` class to process requests
3. Handle input/output formatting
4. Add documentation

## Security Considerations

1. **Safety Checks**: Restricted operations require confirmation
2. **Sandboxing**: Modules are isolated
3. **Local Processing**: No data sent externally
4. **File Access**: Limited to configured directories
5. **Process Control**: Whitelist/blacklist for automation

## Performance Optimization

1. **Lazy Loading**: Models loaded on first use
2. **Quantization**: Use GGUF quantized models
3. **Context Management**: Limit context length
4. **Resource Limits**: Configurable memory/CPU limits
5. **GPU Acceleration**: Optional CUDA/Metal support

## Testing Strategy

1. **Unit Tests**: Test individual modules
2. **Integration Tests**: Test module interactions
3. **System Tests**: End-to-end testing
4. **Performance Tests**: Measure inference speed
5. **Compatibility Tests**: Test across OS/Python versions

## Future Enhancements

1. **Memory System**: Maintain conversation history
2. **Plugin Architecture**: Third-party extensions
3. **Web UI**: Browser-based interface
4. **Multi-modal Chains**: Complex workflows
5. **Fine-tuning**: Custom model training
6. **Distributed Processing**: Multi-machine support

## Dependencies

### Core
- Python 3.8+
- PyYAML (configuration)
- transformers, torch (ML framework)

### Optional (by module)
- llama-cpp-python (local LLM inference)
- opencv-python, PIL (vision)
- SpeechRecognition, pyttsx3 (voice)
- pyautogui, psutil (automation)
- FastAPI, uvicorn (API)

## License

MIT License - See LICENSE file for details.
