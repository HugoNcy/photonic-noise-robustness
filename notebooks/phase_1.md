---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.19.5
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Phase 1 validation: testing a basic model

The goal of this notebook is to show that a classical-quantum model generative model can actually learn, using a simple model.

```python
from data import * 
from models import *

import torch
```


