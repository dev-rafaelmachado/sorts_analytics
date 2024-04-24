from utils import algorithms, N, T
from typing import List

import matplotlib.pyplot as plt

sizes = [i * T for i in range(N)]

def plot_algorithm_progression(results: List[List[float]], title: str, filename: str) -> None:
    for idx, algorithm in enumerate(algorithms):
        chart = [x[idx] for x in results]
        plt.plot(sizes, chart, label=algorithm)
        plt.plot([2 * size for size in sizes], chart, linestyle='--', label='Double the Data')

        plt.xlabel('Data Size')
        plt.ylabel('Time Spent')

        plt.title(f'Time Progression for {title}')

        plt.legend()
        plt.savefig(f'result/charts/{filename}_{algorithm}.png')
        plt.close()
