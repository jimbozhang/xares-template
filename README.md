# xares-audio-encoder-template

This repository provides a template for creating audio encoders compatible with [X-ARES: the eXtensive Audio Representation and Evaluation Suite](https://github.com/jimbozhang/xares). Your encoder should process raw audio waveforms and generate meaningful audio embeddings.

## Steps to create your own audio encoder

1. Make a copy of `template_encoder.py` in the root directory of this repository.

    ```bash
    cp template_encoder.py my_encoder.py
    ```

1. Edit the newly created `my_encoder.py` file to implement your own audio encoder.

1. Check your encoder to make sure it is compatible with X-ARES.

    ```python
    >>> from audio_encoder_checker import check_audio_encoder
    >>> from my_encoder import MyEncoder

    >>> encoder = MyEncoder()

    >>> check_audio_encoder(encoder)
    True
    ```
