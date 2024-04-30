from typing import List
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from utils import algorithms, N, T

sizes = [i * T for i in range(N)]

def plot_algorithm_progression(results: List[List[float]], title: str, filename_prefix: str) -> None:
    for idx, algorithm in enumerate(algorithms):
        times = [result[idx] for result in results]
        plt.plot(sizes, times, label=f'{algorithm} - Original', linestyle='-')

        # Calcula a regressão linear
        slope, intercept, r_value, p_value, std_err = linregress(sizes, times)
        line = slope * np.array(sizes) + intercept

        # Plota a linha de tendência
        plt.plot(sizes, line, linestyle='--', color='gray', label=f'{algorithm} - Trendline')

        # Anota a equação da linha
        equation = f'y = {slope:.2f}x + {intercept:.2f}'
        plt.text(sizes[-1], line[-1], equation, fontsize=8, ha='right')

        # Calcula os tamanhos de dados adicionais para a linha de projeção
        projection_sizes = list(range(N * T, 2 * N * T + T, T))
        projection_line = slope * np.array(projection_sizes) + intercept

        # Plota a linha de projeção
        plt.plot(projection_sizes, projection_line, linestyle='--', color='red', label=f'{algorithm} - Projection')

        plt.xlabel('Data Size')
        plt.ylabel('Time Spent')
        plt.title(f'Time Progression for {title}')
        plt.legend()
        plt.savefig(f'result/charts/{filename_prefix}_{algorithm}.png')
        plt.close()
