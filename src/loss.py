import torch

def MMD_loss(desired_output: torch.Tensor, predicted_values: torch.Tensor) -> float:
    """Function that computes the loss based on MMD. Takes as parameters the desired output as well as the predicted values."""
    
