import torch
import torchvision
from torchvision import transforms
from PIL import Image

model = torchvision.models.resnet50(weights=torchvision.models.ResNet50_Weights.DEFAULT)
model.eval()

class_map = {}
with open("./src/static/resnet-classes.txt", "r") as f:
    classes = f.readlines()
    for i, c in enumerate(classes):
        class_map[i] = c.strip('\n')

def preprocess_image(image):
    # Define the standard ResNet50 transformations
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
    ])
    image = Image.open(image)
    image = preprocess(image)
    image = image.unsqueeze(0)  # Add a batch dimension
    return image

def classify(image):
    image = preprocess_image(image)
    with torch.no_grad():  # No need to compute gradients
        outputs = model(image)
    _, predicted = torch.max(outputs, 1)
    return class_map[predicted.item()]



