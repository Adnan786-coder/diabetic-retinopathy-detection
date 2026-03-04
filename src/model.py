import torch
import torchvision.models as models

class_names = [
    "No DR",
    "Mild",
    "Moderate",
    "Severe",
    "Proliferative DR"
]

def load_model(model_path):
    model = models.resnet18(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, 5)
    model.load_state_dict(torch.load(model_path, map_location="cpu"))
    model.eval()
    return model
