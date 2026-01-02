# Installation Guide

Complete installation guide for the Local AI Assistant.

## Prerequisites

### System Requirements

**Minimum**:
- CPU: 4 cores
- RAM: 8GB
- Storage: 20GB free space
- OS: Windows 10/11, macOS 10.15+, or Linux (Ubuntu 20.04+)
- Python: 3.8 or higher

**Recommended**:
- CPU: 8+ cores
- RAM: 16GB+
- Storage: 50GB free space (for multiple models)
- GPU: NVIDIA GPU with 6GB+ VRAM (optional, for faster inference)
- OS: Latest stable version
- Python: 3.10 or higher

### Software Dependencies

- Python 3.8+
- pip (Python package manager)
- Git
- (Optional) CUDA Toolkit for GPU acceleration

## Step-by-Step Installation

### 1. Clone the Repository

```bash
git clone https://github.com/stewpidasle/symmetrical-fishstick.git
cd symmetrical-fishstick
```

### 2. Create a Virtual Environment (Recommended)

#### On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### On macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Install System-Specific Dependencies

#### Windows:
```bash
# For voice recognition
pip install pyaudio
# If pyaudio fails, download the wheel from:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
```

#### macOS:
```bash
# Install portaudio for voice
brew install portaudio
pip install pyaudio

# For automation
pip install pyobjc-framework-Quartz
```

#### Linux (Ubuntu/Debian):
```bash
# For voice
sudo apt-get install portaudio19-dev python3-pyaudio

# For automation
sudo apt-get install python3-tk python3-dev

# For OCR
sudo apt-get install tesseract-ocr
```

### 5. Download AI Models

See [MODELS.md](MODELS.md) for detailed instructions.

Quick start:
```bash
# Install Hugging Face CLI
pip install huggingface-hub

# Create models directory
mkdir -p models

# Download CodeLlama (coding)
huggingface-cli download TheBloke/CodeLlama-7B-Instruct-GGUF \
  codellama-7b-instruct.Q4_K_M.gguf --local-dir models/
```

### 6. Configure the System

Copy and edit the configuration file:
```bash
cp config.yaml config.local.yaml
```

Edit `config.local.yaml` with your preferences and model paths.

### 7. Verify Installation

```bash
python main.py --command "test"
```

You should see the system initialize all modules.

## GPU Acceleration (Optional)

### NVIDIA GPU (CUDA)

1. **Install CUDA Toolkit**:
   - Download from [NVIDIA website](https://developer.nvidia.com/cuda-downloads)
   - Version 11.8 or 12.x recommended

2. **Install PyTorch with CUDA**:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   ```

3. **Install llama-cpp-python with CUDA**:
   ```bash
   CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
   ```

4. **Update config.yaml**:
   ```yaml
   resources:
     gpu_enabled: true
     gpu_layers: 35  # Adjust based on your GPU
   ```

### AMD GPU (ROCm)

```bash
# Install ROCm from AMD
# Then install PyTorch with ROCm support
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.6
```

### Apple Silicon (Metal)

```bash
# Install PyTorch with Metal Performance Shaders
pip install torch torchvision torchaudio

# Install llama-cpp-python with Metal support
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python --force-reinstall --no-cache-dir
```

## Troubleshooting

### Common Issues

#### "Module not found" errors
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

#### "Model not found" errors
- Verify model files are in the `models/` directory
- Check paths in `config.yaml` match actual file names
- See [MODELS.md](MODELS.md) for download instructions

#### PyAudio installation fails (Windows)
1. Download the appropriate wheel from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)
2. Install: `pip install PyAudio‑X.X.X‑cpXX‑cpXX‑win_amd64.whl`

#### Permission errors on Linux/macOS
```bash
# For automation features, you may need to grant accessibility permissions
# macOS: System Preferences > Security & Privacy > Accessibility
# Linux: Ensure your user is in the input group
```

#### Out of memory errors
- Use smaller models (7B instead of 13B)
- Reduce context length in config.yaml
- Close other applications
- Enable GPU acceleration if available

#### Slow performance
- Enable GPU acceleration
- Use quantized models (Q4_K_M)
- Reduce batch size in config
- Close background applications

### Getting Help

If you encounter issues:

1. Check the [FAQ](#faq) in README.md
2. Search [existing issues](https://github.com/stewpidasle/symmetrical-fishstick/issues)
3. Open a new issue with:
   - System information (OS, Python version, RAM, GPU)
   - Full error message
   - Steps to reproduce

## Updating

To update to the latest version:

```bash
git pull origin main
pip install -r requirements.txt --upgrade
```

## Uninstalling

To completely remove the system:

```bash
# Deactivate virtual environment
deactivate

# Remove the directory
cd ..
rm -rf symmetrical-fishstick

# Remove Python packages (if not using venv)
pip uninstall -r requirements.txt -y
```

## Next Steps

After successful installation:

1. Read the [Usage Guide](../README.md#usage-examples)
2. Try the [examples](../examples/)
3. Explore the [API documentation](API.md)
4. Configure modules in `config.yaml`

## FAQ

**Q: Do I need to install all dependencies?**
A: You can install only what you need. For example, if you only want coding features, you can skip vision-related packages.

**Q: Can I run this on a Raspberry Pi?**
A: Yes, but use smaller models (3B or smaller) and be patient with inference speed.

**Q: Does this work offline?**
A: Yes! After downloading models, everything runs locally without internet.

**Q: How much disk space do I need?**
A: Base installation: ~2GB. With models: 10-20GB depending on models chosen.
