from datagen import generate_normals, generate_uniforms, generate_exponentials, generate_partialsorts
from sorts import mergesort, quicksort, radixsort, heapsort, insertionsort # all sorts just take an array as their only param
import time
import matplotlib.pyplot as plt
import numpy as np


def allsort_experiment_avg_time(sort_algo, data_generator, n_times=1):
    total_time = 0

    for i in range(n_times):
        data = data_generator()
        start_time = time.time()
        sort_algo(data)
        runtime = time.time() - start_time
        total_time += runtime

    return total_time / n_times

def partialsort_experiment(sort_algo, data_size=100000):
    n_swaps = data_size/2
    x = [0,] + [int(2**exponent) for exponent in np.arange(0, 100, 1) if exponent <= np.log2(n_swaps)]
    print x
    y = []
    data = generate_uniforms(n_uniforms=data_size, a=1, b=1000000) # Pick different values maybe?
    for ps_data in generate_partialsorts(data, n_swaps=n_swaps):
        # ps_data will contain a partially sorted array (starting at fully sorted and slowly becoming less sorted,
        # until every item is out of place)
        start_time = time.time()
        sort_algo(ps_data)
        runtime = time.time() - start_time
        y.append(runtime)

    return x,y

def plot_all_sorts_increasing_data(exponents_start=1, exponents_stop=6, exponents_step=0.5):
    sort_algorithms = [mergesort, quicksort, radixsort, heapsort]

    x = [int(10**exponent) for exponent in np.arange(exponents_stop, exponents_start, -exponents_step)]
    y = {}
    for sort_algo in sort_algorithms:
        y[sort_algo.func_name] = []

    print "Running sortings with data sizes:", x
    for data_size in x:
        print "Sorting on size:", data_size
        for sort_algo in sort_algorithms:
            print "Sort algorithm:", sort_algo.func_name
            running_time = allsort_experiment_avg_time(sort_algo, lambda: generate_uniforms(data_size, 1, 1000000), n_times=1)
            y[sort_algo.func_name].append(running_time)

    for sort_algo in sort_algorithms:
        plt.plot(x, y[sort_algo.func_name], label=sort_algo.func_name)

    plt.title("Different Sorting Algorithms with Increasing Data Size")
    plt.xlabel("Data Size (# of uniform integers)")
    plt.ylabel("Running Time (seconds)")
    plt.legend(bbox_to_anchor=(0.3, 1))
    plt.show()

def plot_radix_vs_quicksort_small_range_data(data_size=100000):
    sort_algorithms = [quicksort, radixsort]

    x = [int(10**exponent) for exponent in np.arange(8, 2, -0.7)]
    y = {}
    for sort_algo in sort_algorithms:
        y[sort_algo.func_name] = []

    for max_int in x:
        print "Sorting with max int:", max_int
        for sort_algo in sort_algorithms:
            running_time = allsort_experiment_avg_time(sort_algo, lambda: generate_uniforms(data_size, 1, max_int), n_times=1)
            y[sort_algo.func_name].append(running_time)

    for sort_algo in sort_algorithms:
        plt.plot(x, y[sort_algo.func_name], marker='.', label=sort_algo.func_name)

    plt.title("Radix vs QuickSort on Increasing Data Range (size: %d)" % data_size)
    plt.xlabel("Data Range (uniform integers)")
    plt.ylabel("Running Time (seconds)")
    plt.legend(bbox_to_anchor=(1, 0.3))
    plt.show()

def plot_quick_vs_insertion_partially_sorted(data_size=1000000):
    sort_algorithms = [quicksort, insertionsort]

    for sort_algo in sort_algorithms:
        x, y = partialsort_experiment(sort_algo, data_size=data_size)
        plt.plot(x, y, marker='.', label=sort_algo.func_name)


    plt.title("QuickSort vs Insertion Partially Sorted Data (size: %d)" % data_size)
    plt.xlabel("Number of swaps")
    plt.ylabel("Running Time (seconds)")
    plt.legend(bbox_to_anchor=(1, 0.3))
    plt.show()

def plot_quicksort_different_data_distribution(data_size=10000, n_times=1000):
    sort_algo = quicksort
    data_distributions = [lambda: generate_uniforms(data_size, 1, 100000),
                          lambda: generate_normals(data_size, 0, 5),
                          lambda: generate_exponentials(data_size, 0.5)]
    data_distributions_names = ["Uniforms", "Normals", "Exponentials"]

    y = {}
    for distribution in data_distributions_names:
        y[distribution] = []

    for i, data_gen in enumerate(data_distributions):
        print "Sorting",data_distributions_names[i]
        for experiment in range(n_times):
            running_time = allsort_experiment_avg_time(sort_algo, data_gen)
            y[data_distributions_names[i]].append(running_time)

    for distribution in data_distributions_names:
        plt.hist(y[distribution], bins=50, histtype='step', label=distribution)

    plt.title("QuickSort on Different Data Distributions (size: %d)" % data_size)
    plt.xlabel("Running Time (seconds)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    # plot_all_sorts_increasing_data()
    plot_radix_vs_quicksort_small_range_data()
    # plot_quick_vs_insertion_partially_sorted()
    # plot_quicksort_different_data_distribution()