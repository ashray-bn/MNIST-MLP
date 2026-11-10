import torch
import torchvision

transform =  torchvision.transforms.ToTensor()

#importing the dataset and applying the transform to convert from image to tensor
train_data=torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)
test_data=torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

#creating data loaders
train_loader=torch.utils.data.DataLoader(train_data, batch_size=128, shuffle=True)
test_loader=torch.utils.data.DataLoader(test_data, batch_size=128, shuffle=False)

images,labels=next(iter(train_loader))
