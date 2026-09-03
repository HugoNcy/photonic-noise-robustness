---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.5
  kernelspec:
    display_name: Python (qlm-photonic)
    language: python
    name: qlm-photonic
---

# Phase 1 validation: testing a basic model

The goal of this notebook is to show that a classical-quantum model generative model can actually learn, using a simple model. For this, we would be using the torch library to create the classical part of our network, and add the quantum part through the functions and objects we created in `data.py` and `models.py`. You can find a more detailed explanation in the `docs`folder, including a schema of our model. Here, we will focus on explaining what we are doing instead of why.


```{python}
# First we add the src folder so the notebook can view the code inside
import sys
sys.path.append("../src")
```

```python
from torch.nn import ReLU, Tanh

from data import * 
from models import *

import torch
import numpy as np

# We build the model
model = nn.Sequential(
    nn.Linear(1, 6), # This is just so it matches the input format.
    nn.Linear(6, 6),
    nn.Tanh(),
    QuantumCircuit(),
    nn.Linear(56, 32),
    nn.ReLU(),
    nn.Linear(32, 2),
)
```

Now, before training the model, we have to generate the desired output so we can train using the MDD loss.


```{python}
desired_output = two_gaussian(256)
print(desired_output[:5])
```

Let's also view this in a graph to ensure that this is working.


```{python}
import matplotlib.pyplot as plt

points = desired_output.numpy() # tensor -> numpy array
plt.scatter(points[:, 0], points[:, 1])
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.show()
```

As we can see, we have two gaussians centered around (-1, 0) and (1, 0).

Now let's test the random_input_numbers function.


```{python}
random_numers_test = []
for i in range(256): # Here, we make a loop instead of just calling random_input_numbers once, because of the seed. 
    # It is best to test it like a real simulation
    random_num_test = random_input_numbers(6, seed=i) # Also, we set the seed as i because taking the same seed
    # would just output 256 times the same numbers.
    random_numers_test.append(random_num_test.numpy())

all_values = np.array(random_numers_test).flatten()
plt.hist(all_values, bins=30)
plt.xlabel("value")
plt.ylabel("count")
plt.show()
```

As we can see here, we do have a random normal distribution, so the random_input_numbers function is properly working.

Now, before doing any training, let's see what result we get from running our model once.

```{python}
outputs_test = []
for i in range(256):
    x = random_input_numbers(6, seed=i)
    y = model(x)
    outputs_test.append(y)

```



We can actually optimize the compute time by sending straight 256 times 6 random numbers into the 
