# Mesh comparison in hybrid photonic generative models

Student research project by **Hugo**, **Niels** and **Tony**. This file describes our project in details: it explains what we are trying to do, what was actually done step by step, what each Python file exists and how to reproduce our results.  


## What this project is

We use a classical PyTorch network with a photonic quantum layer using [MerLin](https://github.com/merlinquantum/merlin) (Quandela's QML layer on top of [Perceval](https://perceval.quandela.net/)), training over MDD (Maximum Mean Discrepancy) loss.

The goal of this project is to compare two different mesh structures in classical-quantum generative models: **MZI mesh**, using Clements decomposition, and **tritter mesh**. Our question is the following: 

> At the same number of trainable parameter, do **MZI mesh** and **tritter mesh** have the same generative expressivity?
 
This project does *not* aim to prove a quantum advantage. We are just comparing two different mesh in a similar circuit to see how they are different, how they might influence the result of generative models, and if they are resistant to noise.

This project is decomposed on 4 steps: 

### 1. Construction of a basic model that can learn

Our first step is to build a generic model that proves classical-quantum generative models work in practice.

Our goal is the following: given 6 random numbers sampled from a Gaussian distribution, generate points on a 2D plane whose distribution matches a target: a balanced mixture of two 2D Gaussian blobs, centered at (-1,0) and (1,0).

We went with this architecture: a classical linear layer maps the 6 latent numbers to 6 angles. These angles are encoded into a photonic quantum layer built as a sandwich: a trainable entangling mesh, the layer of angle-encoding phase shifters from the 6 random numbers, and a second trainable entangling mesh. The circuit outputs a probability distribution over Fock states, which a classical adapter network (two linear layers with a ReLU in between) maps down to a single 2D point.

Here is a schema of the model we created:
*insert picture*

For now, we are using for the mesh simple MZI mapped using Clements decomposition. We will compare the MZI and the tritters in the next phases. We are also 6 modes with 3 photons, to create a Fock full space of domension 56.

*Note: With 6 modes, using Clements MZI meshes, we have a total of 15 MZIs, each MZI being composed of 2 beam splitter, and 2 tunable phase shifters, acting as the model's quantum parameters. We have thus a total of 30 parameters over the two meshes, covering the whole U(6) space. This does not cover the whole 56-dimensional Fock space, but is plenty enough for the model to be expressive.*

**Training.** As pointed out by [Gottlieb et al.](https://arxiv.org/abs/2603.08793), generative models using linear optics train well with MMD (Maximum Mean Discrepancy) as the loss. We compute batches of 256 generated points in one go, compare them against a batch of 256 points sampled from the target distribution using MMD, and backpropagate to update every trainable parameter, classical and quantum.

As said before, we used PyTorch and MerLin for our simulation

### 2. Phase 2: noise grid and the mismatch matrix

Goal (plan): train the generator under a grid of noise profiles and measure what happens when training noise and deployment noise differ.

### 3. Phase 3: MZI vs tritter at a fair budget

