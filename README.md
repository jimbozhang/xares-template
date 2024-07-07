# xares-audio-encoder-template

This repository provides a template for creating audio encoders compatible with [X-ARES: the eXtensive Audio Representation and Evaluation Suite](https://github.com/jimbozhang/xares). Your encoder should process raw audio waveforms and generate meaningful audio embeddings.

**Note: This repository is not yet ready. The first official release is scheduled for August 31, 2024.**

## Getting Started

### 1. Fork the repository and clone your fork

```bash
git clone https://github.com/your-github-id/the-forked-xares-template.git
```

### 2. Install X-ARES

```bash
pip install xares
```

### 3. Implement your encoder

1. Create a new Python file in the root directory of this repository (e.g., `my_encoder.py`).
1. In this file, define a new class (e.g., `MyEncoder`) that inherits from the `AudioEncoderBase` class (defined in `xares.audio_encoder_base`).
1. Override the `__call__` method in your class to handle audio processing and return the encoded audio embeddings. This method should accept a PyTorch tensor representing the input audio and an integer representing the sampling rate. The output should be a PyTorch tensor.
1. You can override additional methods or define new ones as needed. Refer to the examples in `examples/dasheng/dasheng_encoder.py` and `examples/wav2vec2/wav2vec2_encoder.py` for guidance.

### 4. Check the input/output format of your encoder

```python
>>> from my_encoder import MyEncoder
>>> encoder = MyEncoder()

>>> import torch
>>> audio = torch.randn(2, 48_000)

>>> encoder.check_input_audio(audio, encoder.sampling_rate)  # Check if the input audio format is valid (provided by AudioEncoderBase)
True

>>> encoded_audio = encoder(audio, encoder.sampling_rate)
>>> encoder.check_encoded_audio(encoded_audio)  # Check if the encoded audio format is valid (provided by AudioEncoderBase)
True
```
