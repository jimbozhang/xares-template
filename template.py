import torch
import torch.nn as nn


class MyAwesomeModel(nn.Module):
    def __init__(self, output_dim):
        super().__init__()
        self.output_dim = output_dim

    def forward(self, x):
        return torch.randn(x.shape[0], int(x.shape[1] / self.sampling_rate / self.hop_size_in_ms), self.output_dim)


class MyEncoder(nn.Module):
    def __init__(self):
        super().__init__()
        self.sampling_rate = 16000  # Required. The recommended sampling rate of the input audio
        self.output_dim = 128  # Required. The output dimension of the model
        self.hop_size_in_ms = 40  # Required. The hop size in milliseconds

        self.model = MyAwesomeModel(self.output_dim)  # [B, T] -> [B, T', D], D == 128 in this model

    def forward(self, audio: torch.Tensor):
        """
        Processes the input audio signal and returns the model's encoded output.
        Args:
            audio (torch.Tensor): A single-channel audio signal, represented as a PyTorch tensor with shape [B, T].
        Returns:
            torch.Tensor: The model's encoded output. The output tensor has shape [B, T', D], where T' can be different from the input T.
        """
        if audio.ndim == 1:
            audio = audio.unsqueeze(0)

        self.model.eval()
        with torch.inference_mode():
            encoded_audio = self.model(audio)

        return encoded_audio


if __name__ == "__main__":
    from audio_encoder_checker import check_audio_encoder

    encoder = MyEncoder()
    assert check_audio_encoder(encoder)
