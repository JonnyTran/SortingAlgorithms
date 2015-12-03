__author__ = 'jason'
import numpy as np

def generate_normals(n_normals, mu, sigma):
    return list(sigma*np.random.randn(n_normals) + mu)

def generate_uniforms(n_uniforms, a, b):
    return list(np.random.random_integers(a, b, (n_uniforms)))

def generate_exponentials(n, _lambda):
    return list(np.random.exponential(scale=1/_lambda, size=(n)))

def swap(arr, i, j):
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def generate_partialsorts(arr, n_swaps):
    fully_sorted = sorted(arr)
    indices = range(len(fully_sorted))
    swaps = np.random.choice(indices, (n_swaps, 2), replace=False)
    yield fully_sorted # First yield a fully sorted array
    for row in swaps:
        l, r = row
        swap(fully_sorted, l, r)
        yield fully_sorted # then yield an array with 1 more swap than the last array

