import torch
from PIL import Image
import torchvision.transforms as transforms
from src.augmentation.transforms import FILLCOLOR, SquarePad



def transform_image(image: Image) -> torch.Tensor:
    transform = transforms.Compose(
        [
            SquarePad(),
            transforms.Resize((96, 96)),
            transforms.ToTensor(),
            transforms.Normalize(
                (0.4914, 0.4822, 0.4465),
                (0.2470, 0.2435, 0.2616),
            ),
        ]
    )
    return transform(image).unsqueeze(0)
