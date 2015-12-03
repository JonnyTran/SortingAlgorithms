from datagen import generate_normals, generate_uniforms, generate_exponentials, generate_partialsorts
from sorts import mergesort, quicksort, radixsort, heapsort, insertionsort # all sorts just take an array as their only param
import time
import matplotlib.pyplot as plt


def partialsort_experiment(data_size, a=0, b=10):
    data = generate_uniforms(n_uniforms=data_size, a=a, b=b) # Pick different values maybe?
    results = []
    for ps_data in generate_partialsorts(data, data_size//2):
        # ps_data will contain a partially sorted array (starting at fully sorted and slowly becoming less sorted,
        # until every item is out of place)
        print(ps_data)
        # Do tests, save it to a csv or something and we can plot it
    return results

def allsort_experiment_avg_time(sort_algo, data_generator, n_times=10):
    total_time = 0

    for i in range(n_times):
        data = data_generator()
        start_time = time.time()
        sort_algo(data)
        runtime = time.time() - start_time
        total_time += runtime

    return total_time / n_times

def plot_all_sorts_increasing_data(start=100, stop=10000, step=1000):
    sort_algorithms = [mergesort, quicksort, radixsort, heapsort]
    x=[]
    y={}
    for sort_algo in sort_algorithms:
        y[sort_algo.func_name] = []

    for data_size in range(start, stop+step, step):
        x.append(data_size)
        for sort_algo in sort_algorithms:
            running_time = allsort_experiment_avg_time(sort_algo, lambda: generate_uniforms(data_size, 1, 100))
            y[sort_algo.func_name].append(running_time)

    for sort_algo in sort_algorithms:
        plt.plot(x, y[sort_algo.func_name], label=sort_algo.func_name)

    plt.title("Different Sorting Algorithms Running Time (averaged over 100) with Increasing Data Size")
    plt.xlabel("Data Size (# of uniform integers)")
    plt.ylabel("Running Time (seconds)")
    plt.legend()
    plt.show()

if __name__ == '__main__':
    print allsort_experiment_avg_time(radixsort, lambda: generate_uniforms(100, 1, 10))
    print allsort_experiment_avg_time(quicksort, lambda: generate_uniforms(100, 1, 10))
    plot_all_sorts_increasing_data(start=1000, stop=10000, step=2000)

