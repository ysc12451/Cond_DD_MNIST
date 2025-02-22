import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import models, transforms, datasets
from torchvision.datasets import MNIST, Food101
from torchvision.utils import save_image, make_grid

data_path = '/mnt/c/Code/cs771_project/data/food-101-subset/images/caesar_salad'
save_dir = os.path.join(data_path, 'normalized/')
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
ws_test = [2.0] # strength of generative guidance
imag_size = 64
batch_size = 32
raw_transform = transforms.Compose([
    transforms.Resize(imag_size),
    transforms.CenterCrop(imag_size),
    transforms.ToTensor()])

train_transform = transforms.Compose([
    transforms.Resize(imag_size),
    transforms.CenterCrop(imag_size),
    transforms.ToTensor(),
    transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

raw_dataset = datasets.ImageFolder(root=data_path, transform=raw_transform)
raw_dataloader = DataLoader(raw_dataset, batch_size=batch_size, shuffle=True, num_workers=5)
for x, c in raw_dataloader:
    grid = make_grid(x, nrow=5)
    save_image(grid, save_dir + f"raw_image.png")
    break

# dataset = Food101(data_path, split='train', download=True, transform=train_transform)
dataset = datasets.ImageFolder(root=data_path, transform=train_transform)
dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True, num_workers=5)
for x, c in dataloader:
    grid = make_grid(x, nrow=5)
    save_image(grid, save_dir + f"normalized_image.png")
    break

# mean, std = torch.Tensor((0.485, 0.456, 0.406)).unsqueeze(1).unsqueeze(2), torch.Tensor((0.229, 0.224, 0.225)).unsqueeze(1).unsqueeze(2)
# invTrans = transforms.Compose([ transforms.Normalize(mean = [ 0., 0., 0. ],
#                                                     std = [ 1/0.229, 1/0.224, 1/0.225 ]),
#                             transforms.Normalize(mean = [ -0.485, -0.456, -0.406 ],
#                                                     std = [ 1., 1., 1. ]),
#                             ])