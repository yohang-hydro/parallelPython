# Parallel Python

```bash
module load python3/3.10.0
module load cuda/12.0.0
```

```bash
python3 -m pip install jupyterlab
python3 -m pip install numba
python3 -m pip install jax
python3 -m pip install cupy-cuda12x
```

## Available methods to speed up the python programming using parallel way

### Numba

[Numba](https://numba.pydata.org/) is an open source JIT (just-in-time) compiler that translates a subset of Python and NumPy code into fast machine code. When a call is made to a Numba-decorated function it is compiled to machine code “just-in-time” for execution and all or part of your code can subsequently run at native machine code speed!

### Jax

[JAX](https://jax.readthedocs.io/en/latest/) is a Python library for **accelerator-oriented array computation** and program transformation, designed for high-performance numerical computing and large-scale machine learning.

If you’re looking to train neural networks, use [Flax](https://flax.readthedocs.io/en/latest/) and start with its documentation. Some associated tools are [Optax](https://optax.readthedocs.io/en/latest/) and [Orbax](https://orbax.readthedocs.io/en/latest/). For an end-to-end transformer library built on JAX, see [MaxText](https://github.com/google/maxtext/).

- Google Jax github:   https://github.com/google/jax
- Google Jax document: https://jax.readthedocs.io/en/latest/

### CUDA

[CuPy](https://cupy.dev/) is an open-source array library for GPU-accelerated computing with Python. CuPy utilizes CUDA Toolkit libraries including cuBLAS, cuRAND, cuSOLVER, cuSPARSE, cuFFT, cuDNN and NCCL to make full use of the GPU architecture.
The figure shows CuPy speedup over NumPy. Most operations perform well on a GPU using CuPy out of the box. CuPy speeds up some operations more than 100X. Read the original benchmark article Single-GPU CuPy Speedups on the RAPIDS AI Medium blog.
