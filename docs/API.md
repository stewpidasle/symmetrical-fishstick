# API Reference

Complete API documentation for the Local AI Assistant.

## Core Classes

### LocalAI

Main orchestrator class for the AI system.

```python
from local_ai import LocalAI

ai = LocalAI(config_path=None)
```

#### Parameters
- `config_path` (str, optional): Path to configuration file. Defaults to `config.yaml`.

#### Methods

##### `process_request(request: str, context: dict = None) -> str`

Process a user request using appropriate modules.

```python
response = ai.process_request(
    "Write a Python function to calculate factorial",
    {'language': 'python'}
)
```

**Parameters**:
- `request` (str): User's request/query
- `context` (dict, optional): Additional context (image data, file paths, etc.)

**Returns**: str - Response from the AI system

##### `get_module(module_name: str)`

Get a specific module by name.

```python
coding_module = ai.get_module('coding')
```

**Parameters**:
- `module_name` (str): Name of module ('coding', 'vision', 'voice', 'automation')

**Returns**: Module object or None

##### `shutdown()`

Shutdown all modules and cleanup resources.

```python
ai.shutdown()
```

### Config

Configuration management class.

```python
from local_ai import Config

config = Config(config_path='config.yaml')
```

#### Methods

##### `get(key: str, default: Any = None) -> Any`

Get configuration value by key (supports dot notation).

```python
model_path = config.get('coding.model.path')
port = config.get('api.port', 8000)
```

##### `is_module_enabled(module_name: str) -> bool`

Check if a module is enabled.

```python
if config.is_module_enabled('vision'):
    print("Vision module enabled")
```

## Modules

### CodingModule

Handles coding-related tasks.

```python
coding = ai.get_module('coding')
```

#### Methods

##### `process(request: str, context: dict = None) -> str`

Process a coding request.

```python
response = coding.process(
    "Generate a binary search function",
    {'language': 'python'}
)
```

**Context Parameters**:
- `language` (str): Programming language
- `code` (str): Code to review/debug
- `error` (str): Error message for debugging

##### `get_supported_languages() -> list`

Get list of supported programming languages.

```python
languages = coding.get_supported_languages()
# ['python', 'javascript', 'java', 'cpp', 'rust', 'go']
```

### VisionModule

Handles vision and image analysis tasks.

```python
vision = ai.get_module('vision')
```

#### Methods

##### `process(request: str, context: dict = None) -> str`

Process a vision request.

```python
response = vision.process(
    "What do you see in this image?",
    {'image_path': 'screenshot.png'}
)
```

**Context Parameters**:
- `image_path` (str): Path to image file
- `screenshot` (bool): Capture screenshot
- `webcam` (bool): Capture from webcam

##### `capture_and_analyze(source: str = 'screenshot') -> str`

Capture an image and analyze it.

```python
result = vision.capture_and_analyze('screenshot')
```

**Parameters**:
- `source` (str): 'screenshot' or 'webcam'

**Returns**: str - Analysis of captured image

### VoiceModule

Handles speech recognition and text-to-speech.

```python
voice = ai.get_module('voice')
```

#### Methods

##### `listen_once() -> str`

Listen for a single voice command.

```python
text = voice.listen_once()
print(f"You said: {text}")
```

**Returns**: str - Transcribed text

##### `speak(text: str) -> bool`

Convert text to speech and play it.

```python
success = voice.speak("Hello, how can I help you?")
```

**Parameters**:
- `text` (str): Text to speak

**Returns**: bool - True if successful

##### `async start_listening(callback: Callable = None)`

Start continuous listening for voice commands.

```python
async def handle_command(text):
    return f"You said: {text}"

await voice.start_listening(callback=handle_command)
```

##### `stop_listening()`

Stop continuous listening.

```python
voice.stop_listening()
```

##### `transcribe_audio_file(audio_file: str) -> str`

Transcribe an audio file.

```python
text = voice.transcribe_audio_file('recording.wav')
```

##### `save_speech_to_file(text: str, output_file: str) -> bool`

Convert text to speech and save to file.

```python
success = voice.save_speech_to_file("Hello world", "output.wav")
```

### AutomationModule

Handles computer automation tasks.

```python
automation = ai.get_module('automation')
```

#### Methods

##### `process(request: str, context: dict = None) -> str`

Process an automation request.

```python
response = automation.process(
    "Click at position",
    {'x': 100, 'y': 200}
)
```

**Context Parameters for Mouse**:
- `x` (int): X coordinate
- `y` (int): Y coordinate
- `amount` (int): Scroll amount

**Context Parameters for Keyboard**:
- `text` (str): Text to type
- `keys` (list): Keys to press

**Context Parameters for Files**:
- `path` (str): File path
- `source` (str): Source path
- `destination` (str): Destination path

**Context Parameters for Processes**:
- `program` (str): Program name or path

##### `execute_complex_task(task_description: str) -> str`

Execute a complex multi-step task.

```python
result = automation.execute_complex_task(
    "Open notepad, type hello, and save the file"
)
```

## REST API Endpoints

When running in API mode (`python main.py --mode api`):

### POST /process

Process an AI request.

```bash
curl -X POST http://localhost:8000/process \
  -H "Content-Type: application/json" \
  -d '{
    "request": "Write a Python function to sort a list",
    "context": {"language": "python"}
  }'
```

**Request Body**:
```json
{
  "request": "string",
  "context": {}
}
```

**Response**:
```json
{
  "response": "string",
  "status": "success"
}
```

### GET /health

Health check endpoint.

```bash
curl http://localhost:8000/health
```

**Response**:
```json
{
  "status": "healthy",
  "modules": ["coding", "vision", "voice", "automation"]
}
```

### GET /

Root endpoint with system information.

```bash
curl http://localhost:8000/
```

**Response**:
```json
{
  "name": "Local AI Assistant API",
  "version": "0.1.0",
  "modules": ["coding", "vision", "voice", "automation"]
}
```

## Command-Line Interface

### Interactive Mode

```bash
python main.py --mode interactive
```

Start an interactive CLI session.

### Voice Mode

```bash
python main.py --mode voice
```

Start voice interaction mode.

### API Mode

```bash
python main.py --mode api
```

Start REST API server.

### Single Command

```bash
python main.py --command "Write a Python hello world program"
```

Execute a single command.

### Custom Config

```bash
python main.py --config custom_config.yaml
```

Use a custom configuration file.

## Configuration File

### Structure

```yaml
ai_system:
  name: "Local AI Assistant"
  version: "0.1.0"

coding:
  enabled: true
  model:
    name: "codellama"
    path: "models/codellama-7b-instruct.gguf"
    context_length: 4096
  languages:
    - python
    - javascript

vision:
  enabled: true
  model:
    name: "llava"
    path: "models/llava-v1.5-7b.gguf"
  features:
    - image_understanding
    - ocr

voice:
  enabled: true
  speech_recognition:
    engine: "whisper"
    model: "base"
  text_to_speech:
    engine: "coqui-tts"
  wake_word: "assistant"

automation:
  enabled: true
  safety:
    confirm_actions: true
    restricted_operations:
      - file_deletion
      - system_shutdown

api:
  host: "127.0.0.1"
  port: 8000
  enable_web_ui: true

resources:
  max_memory_gb: 8
  cpu_threads: 4
  gpu_enabled: false
```

## Error Handling

All methods may raise exceptions. Wrap calls in try-except blocks:

```python
try:
    response = ai.process_request("Generate code")
except Exception as e:
    print(f"Error: {e}")
```

## Examples

See the [examples](../examples/) directory for complete working examples:

- `example_coding.py` - Coding module usage
- `example_vision.py` - Vision module usage
- `example_voice.py` - Voice module usage
- `example_automation.py` - Automation module usage

## Support

For issues and questions:
- GitHub Issues: https://github.com/stewpidasle/symmetrical-fishstick/issues
- Documentation: https://github.com/stewpidasle/symmetrical-fishstick/docs
