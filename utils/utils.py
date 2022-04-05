import torchvision.transforms as T
import torchvision
import torch
import matplotlib.pyplot as plt

# imageNet's mean and std
mean = torch.tensor([0.485, 0.456, 0.406])
std = torch.tensor([0.229, 0.224, 0.225])

demean = - mean
destd = 1/std

def preprocess(img, div_std=False):
    """
    convert img to tensor and normalize it using imagenet's mean and std
    """
    transform = T.Compose([
        T.ToTensor(),
        T.Normalize(mean=mean, std=[1, 1, 1] if div_std==False else std),
    ])
    return transform(img)

def deprocess(tensor, div_std=False):
    """
    denormalize the input tensor and convert tensor to PIL image
    """
    transform = T.Compose([
        T.Normalize(mean=[0,0,0], std=[1,1,1] if div_std==False else destd),
        T.Normalize(mean=demean, std=[1,1,1]),
        # in my code when use to PILImage, leading some highlight points in pic
        # so i comment this
        # T.ToPILImage()
    ])
    return transform(tensor)


def plot_img_tensor(img_tensor):
    """
    plot a batch of image tensor


    params:
        tensors: torch.tensor of size (N, img_channel, width, height)

    return:
        None
    """
    grid = torchvision.utils.make_grid(img_tensor, normalize=True)
    img_data = grid.permute(1, 2, 0).numpy()
    plt.imshow(img_data)
    plt.axis("off")