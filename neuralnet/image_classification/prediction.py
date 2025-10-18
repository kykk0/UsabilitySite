import torch
from torchvision.io import read_image, ImageReadMode
from torchvision.models import resnet50, ResNet50_Weights
from PIL import Image


class ResNetImagePredictor:
    def __init__(self):
        self.weights = ResNet50_Weights.DEFAULT
        self.model = resnet50(weights=self.weights)
        self.model.eval()
        self.preprocess = self.weights.transforms()

    def predict(self, img_path):
        with torch.no_grad():
            try:
                pil_image = Image.open(img_path).convert('RGB')

                from torchvision.transforms import ToTensor
                to_tensor = ToTensor()
                img_tensor = to_tensor(pil_image)

                batch = self.preprocess(img_tensor).unsqueeze(0)

            except Exception as e:
                try:
                    img = read_image(img_path, mode=ImageReadMode.RGB)
                    batch = self.preprocess(img).unsqueeze(0)
                except Exception as e2:
                    return f"Error processing image: {str(e2)}"

            prediction = self.model(batch).squeeze(0).softmax(0)
            results = [f"{self.weights.meta['categories'][i]}: " + f"{100 * v:.1f}%"
                       for v, i in zip(*torch.topk(prediction, 3))]
            results = " | ".join(results)

            return results
