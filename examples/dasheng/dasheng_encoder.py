import torch
from dasheng import dasheng_base


class DashengEncoder(torch.nn.Module):
    def __init__(self):
        self.simple_rate = 16000
        self.output_dim = 768
        self.model = dasheng_base().to(self.device)

    def forward(self, audio: torch.Tensor):
        if audio.ndim == 1:
            audio = audio.unsqueeze(0)

        self.model.eval()
        with torch.inference_mode():
            encoded_audio = self.model(audio.to(self.device))

        return encoded_audio
