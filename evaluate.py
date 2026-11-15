import torch
import torchvision

'''Data Preprocessing and loading'''
transform =  torchvision.transforms.ToTensor()
#importing the dataset and applying the transform to convert from image to tensor
train_data=torchvision.datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_data=torchvision.datasets.MNIST(root='./data', train=False, download=True, transform=transform)

#creating data loaders
train_loader=torch.utils.data.DataLoader(train_data, batch_size=128, shuffle=True)
test_loader=torch.utils.data.DataLoader(test_data, batch_size=128, shuffle=False)

import torch.nn as nn

class MNIST_MLP_ReLu(nn.Module):
    def __init__(self):
        super().__init__()

        self.fc1=nn.Linear(784, 128)
        self.fc2=nn.Linear(128, 10)

        self.relu=nn.ReLU()

    def forward(self, x):
        x = x.view(x.shape[0], -1)

        x = self.relu(self.fc1(x))
        x = self.fc2(x)

        return x

model = MNIST_MLP_ReLu()
print(model)

'''
testing whether to architecture works or not by passing a batch of images through the model and checking the output shape
images, labels = next(iter(train_loader))

output = model(images)

print("Input shape:", images.shape)
print("Output shape:", output.shape)
#expected output-
#Input shape: torch.Size([128, 1, 28, 28])
#Output shape: torch.Size([128, 10])
'''

criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr=0.001)