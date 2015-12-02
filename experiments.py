from datagen import generate_normals, generate_uniforms, generate_exponentials, generate_partialsorts
from sorts import mergesort, quicksort, radixsort, heapsort, insertionsort # all sorts just take an array as their only param
import time

def partialsort_experiment(data_size, a=0, b=10):
    data = generate_uniforms(n_uniforms=data_size, a=a, b=b) # Pick different values maybe?
    results = []
    for ps_data in generate_partialsorts(data, data_size//2):
        # ps_data will contain a partially sorted array (starting at fully sorted and slowly becoming less sorted,
        # until every item is out of place)
        print(ps_data)
        # Do tests, save it to a csv or something and we can plot it
    return results

def allsort_experiment(data):
    results = []
    # run all sorts on data, time them, save as csv or something
    # run multiple times using different distributions
    return results

def quicksort_v_radix_experiment(data):
    results = []
    # repeatedly generate a fixed number of uniforms with an increasing range, time quicksort/radix, save as csv
    # on the google keep note you say range of size 5,10,100,200 and 1 million ints, I think that's too small a range
    # and maybe too many numbers?
