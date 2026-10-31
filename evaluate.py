import torch
from PIL import Image
import torchvision
torchvision.datasets.MNIST(root='./data', train=False, download=True)

transform =  torchvision.transforms.ToTensor()

