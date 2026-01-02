# Model Setup Guide

This guide explains how to download and set up the AI models for the Local AI Assistant.

## Overview

The Local AI Assistant uses free, open-source models that you can download and run locally:

- **Coding**: CodeLlama or similar code-focused models
- **Vision**: LLaVA or similar multimodal models
- **Voice**: Whisper for speech recognition, various TTS engines

## Model Formats

We primarily use **GGUF** format models, which are:
- Quantized for efficient CPU inference
- Compatible with llama.cpp and llama-cpp-python
- Smaller in size while maintaining good quality

## Downloading Models

### Method 1: Hugging Face (Recommended)

1. **Install Hugging Face CLI**:
   ```bash
   pip install huggingface-hub
   ```

2. **Download CodeLlama (Coding)**:
   ```bash
   huggingface-cli download TheBloke/CodeLlama-7B-Instruct-GGUF codellama-7b-instruct.Q4_K_M.gguf --local-dir models/
   ```

3. **Download LLaVA (Vision)**:
   ```bash
   huggingface-cli download mys/ggml_llava-v1.5-7b ggml-model-q4_k.gguf --local-dir models/
   huggingface-cli download mys/ggml_llava-v1.5-7b mmproj-model-f16.gguf --local-dir models/
   ```

### Method 2: Direct Download

Visit these Hugging Face repositories and download manually:

**Coding Models**:
- [CodeLlama-7B-Instruct-GGUF](https://huggingface.co/TheBloke/CodeLlama-7B-Instruct-GGUF)
- [CodeLlama-13B-Instruct-GGUF](https://huggingface.co/TheBloke/CodeLlama-13B-Instruct-GGUF) (better quality, more resources)

**Vision Models**:
- [LLaVA-v1.5-7B-GGUF](https://huggingface.co/mys/ggml_llava-v1.5-7b)
- [LLaVA-v1.5-13B-GGUF](https://huggingface.co/mys/ggml_llava-v1.5-13b) (better quality)

## Model Directory Structure

Place downloaded models in the `models/` directory:

```
models/
├── codellama-7b-instruct.Q4_K_M.gguf     # Coding model
├── ggml-model-q4_k.gguf                   # Vision model
├── mmproj-model-f16.gguf                  # Vision projection
└── .gitkeep
```

## Updating Configuration

After downloading models, update `config.yaml` with the correct paths:

```yaml
coding:
  model:
    path: "models/codellama-7b-instruct.Q4_K_M.gguf"

vision:
  model:
    path: "models/ggml-model-q4_k.gguf"
    clip_path: "models/mmproj-model-f16.gguf"
```

## Model Quantization Levels

GGUF models come in different quantization levels:

- **Q4_K_M**: Good balance of quality and size (recommended)
- **Q5_K_M**: Better quality, larger size
- **Q8_0**: Best quality, largest size
- **Q2_K**: Smallest size, lower quality

Choose based on your available resources.

## Alternative Models

### Coding
- **Mistral-7B-Instruct**: General purpose with coding capabilities
- **Phi-2**: Smaller model, good for low-resource systems
- **DeepSeek-Coder**: Specialized coding model

### Vision
- **LLaVA-v1.6**: Improved version with better understanding
- **BakLLaVA**: Alternative vision-language model

### Voice
- **Whisper**: Built-in, downloads automatically
  - Base: Faster, less accurate
  - Small: Good balance
  - Medium: Better accuracy
  - Large: Best accuracy (requires more resources)

## Troubleshooting

### Out of Memory
- Use smaller models (7B instead of 13B)
- Use more aggressive quantization (Q4 or Q2)
- Reduce context length in config.yaml

### Slow Inference
- Enable GPU acceleration if available
- Use quantized models (GGUF format)
- Reduce batch size

### Model Not Loading
- Check file paths in config.yaml
- Verify model file integrity
- Ensure sufficient disk space

## System Requirements by Model

| Model Size | RAM Required | Disk Space | Inference Speed* |
|------------|--------------|------------|------------------|
| 7B Q4      | 4-6 GB       | 4 GB       | ~10 tokens/sec   |
| 7B Q8      | 7-9 GB       | 7 GB       | ~8 tokens/sec    |
| 13B Q4     | 8-10 GB      | 8 GB       | ~5 tokens/sec    |
| 13B Q8     | 14-16 GB     | 14 GB      | ~4 tokens/sec    |

*On CPU. GPU will be significantly faster.

## Next Steps

After setting up models:
1. Run the system: `python main.py`
2. Try the examples in the `examples/` directory
3. Read the [API documentation](API.md)

## Resources

- [llama.cpp documentation](https://github.com/ggerganov/llama.cpp)
- [Hugging Face Model Hub](https://huggingface.co/models)
- [GGUF format specification](https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)
