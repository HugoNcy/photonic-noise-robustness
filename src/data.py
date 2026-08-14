import torch

# Used in phase 1 to generate the 256 random numbers following the two-gaussian distribution.
def two_gaussian(n: int, seed: int=0) -> torch.Tensor:
    """Function generating n points of a two-gaussian 2D distribution centered at (-1,0) and (1.0)"""
    # For reproductible results, this always generate the same "random" sequence numbers
    g = torch.Generator().manual_seed(seed)
   
    # Create two tensors with n/2 points following a reduced centered gaussian, then shifted to get the two gaussians, with std 0.3.
    gaussA = torch.randn(n//2, 2, generator=g) * 0.3 + torch.tensor([-1.0, 0.0])
    gaussB = torch.randn(n-n//2, 2, generator=g) * 0.3 + torch.tensor([1.0, 0.0])

    # Merge the two tensors
    return torch.cat([gaussA, gaussB], dim=0)


def random_input_numbers(n: int, seed: int=0) -> torch.Tensor:
    """Function generating the random input numbers"""

    g = torch.Generator().manual_seed(seed)
    # Centered reduced gaussian with std 1. Just random numbers.
    return torch.randn(n, 1, generator=g)
