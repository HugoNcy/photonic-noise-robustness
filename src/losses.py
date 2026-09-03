import torch

def mmd_loss(x: torch.Tensor, y: torch.Tensor, sigma=1.0) -> torch.Tensor:
    """MMD Loss"""
    # Kernel matrix of X against itself
    kxx = kernel(squared_distance(x, x), sigma)
    # Kernel matrix of Y against itself
    kyy = kernel(squared_distance(y, y), sigma)
    # Kernel matrix of X against Y
    kxy = kernel(squared_distance(x, y), sigma)

    return (kxx.mean() + kyy.mean() - 2 * kxy.mean())


def squared_distance(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Squared distance of X - Y, returns (n, n) tensor"""
    diff = x.unsqueeze(1) - y.unsqueeze(0) # This is every pair of x - y
    return (diff ** 2).sum(dim=-1)  # shape: (256, 256)

def kernel(x: torch.Tensor, sigma: float) -> torch.Tensor:
    """RBF kernel function with the pre-computer squared distance as x"""
    return torch.exp(torch.neg(x)/ (2 * sigma ** 2))
