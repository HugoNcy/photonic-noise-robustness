# Mesh comparaison in hybrod photonic generative models

Student research project by **Hugo**, **Niels** and **Tony**.

## Research question

The goal of this project is to compare two different mesh structures in classical-quantum generative models: **MZI mesh**, using Clements decomposition, and **tritter mesh**. Our question is the following: 

> At the same number of trainable parameter, do **MZI mesh** and **tritter mesh** have the same generative expressivity?

We use a classical PyTorch network with a photonic quantum layer using [MerLin](https://github.com/merlinquantum/merlin) (Quandela's QML layer on top of [Perceval](https://perceval.quandela.net/)), training over MDD (Maximum Mean Discrepancy) loss.
 
This project does *not* aim to prove a quantum advantage. We are just comparing two different mesh types, to see if one has an advantage over the other.

A full pedagogical explanation of the project (linear optics, Fock states, MMD loss, ...) is in the `docs/` folder.

## How to read this repository

(include desc)

## Installing the environment

We run this project on Python 3.12.13, Perceval 1.2.4 and MerLin 0.4.0 (see `requirements.txt`). Make sure you have `python3.12.13` and `git` installed.

1. Clone the repository:
```bash
git clone https://github.com/<user>/qlm-photonic.git
cd qlm-photonic
```

2. Create the virtual environment and install the libraries:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

3. Register the environment as a Jupyter kernel:
```bash
python -m ipykernel install --user --name qlm-photonic --display-name "Python (qlm-photonic)"
```

4. Launch Jupyter (with the venv still activated) and select the **Python (qlm-photonic)** kernel:
```bash
jupyter lab
```

