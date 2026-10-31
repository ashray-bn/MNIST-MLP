"""
AlexNet implementation for MNIST classification.

AlexNet was originally designed for 224x224x3 ImageNet images. MNIST images
are 28x28x1 (grayscale), so this version:
  - Accepts 1-channel input instead of 3
  - Uses smaller strides/kernel sizes in the early conv layers so the
    feature map doesn't collapse to nothing on a 28x28 input
  - Outputs 10 classes instead of 1000

Run with: python alexnet_mnist.py
Requires: torch, torchvision
"""

import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


class AlexNet(nn.Module):
    def __init__(self, num_classes: int = 10):
        super().__init__()

        # Feature extractor: 5 conv layers (as in original AlexNet),
        # but with kernel/stride sizes scaled down for 28x28 input.
        self.features = nn.Sequential(
            # Conv1: 1x28x28 -> 64x28x28
            nn.Conv2d(1, 64, kernel_size=3, stride=1, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),           # -> 64x14x14

            # Conv2: 64x14x14 -> 192x14x14
            nn.Conv2d(64, 192, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),           # -> 192x7x7

            # Conv3
            nn.Conv2d(192, 384, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),

            # Conv4
            nn.Conv2d(384, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),

            # Conv5
            nn.Conv2d(256, 256, kernel_size=3, padding=1),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(kernel_size=2, stride=2),           # -> 256x3x3
        )

        self.avgpool = nn.AdaptiveAvgPool2d((3, 3))

        # Classifier: 3 fully-connected layers, as in the original AlexNet
        self.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(256 * 3 * 3, 1024),
            nn.ReLU(inplace=True),
            nn.Dropout(0.5),
            nn.Linear(1024, 512),
            nn.ReLU(inplace=True),
            nn.Linear(512, num_classes),
        )

    def forward(self, x):
        x = self.features(x)
        x = self.avgpool(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x


def get_dataloaders(batch_size: int = 128):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.1307,), (0.3081,)),  # MNIST mean/std
    ])

    train_set = datasets.MNIST(root="./data", train=True, download=True, transform=transform)
    test_set = datasets.MNIST(root="./data", train=False, download=True, transform=transform)

    train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True, num_workers=2)
    test_loader = DataLoader(test_set, batch_size=batch_size, shuffle=False, num_workers=2)

    return train_loader, test_loader


def train_one_epoch(model, loader, optimizer, criterion, device):
    model.train()
    running_loss, correct, total = 0.0, 0, 0

    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()
        outputs = model(images)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item() * images.size(0)
        _, predicted = outputs.max(1)
        correct += predicted.eq(labels).sum().item()
        total += labels.size(0)

    return running_loss / total, 100.0 * correct / total


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    running_loss, correct, total = 0.0, 0, 0

    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)

        running_loss += loss.item() * images.size(0)
        _, predicted = outputs.max(1)
        correct += predicted.eq(labels).sum().item()
        total += labels.size(0)

    return running_loss / total, 100.0 * correct / total


def main():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")

    train_loader, test_loader = get_dataloaders(batch_size=128)

    model = AlexNet(num_classes=10).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=1e-3)

    num_epochs = 10
    for epoch in range(1, num_epochs + 1):
        train_loss, train_acc = train_one_epoch(model, train_loader, optimizer, criterion, device)
        test_loss, test_acc = evaluate(model, test_loader, criterion, device)

        print(
            f"Epoch [{epoch}/{num_epochs}] "
            f"Train loss: {train_loss:.4f}, Train acc: {train_acc:.2f}% | "
            f"Test loss: {test_loss:.4f}, Test acc: {test_acc:.2f}%"
        )

    torch.save(model.state_dict(), "alexnet_mnist.pth")
    print("Model saved to alexnet_mnist.pth")


if __name__ == "__main__":
    main()