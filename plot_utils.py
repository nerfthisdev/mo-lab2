import matplotlib.pyplot as plt
import numpy as np
from functions import f
import os

def plot_optimization(history, a, b, title, filename):
    plt.figure(figsize=(10, 6))
    x = np.linspace(a, b, 400)
    y = [f(xi) for xi in x]
    
    plt.plot(x, y, label='f(x) = x² + e⁻ˣ', lw=2)
    
    if history:
        iterations = np.array(history)
        plt.scatter(iterations[:, 0], iterations[:, 1], c='red', s=50, zorder=3)
        plt.plot(iterations[:, 0], iterations[:, 1], '--', color='blue', alpha=0.5, label='Итерации')
    
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    
    # Создаем папку если нужно
    os.makedirs('plots', exist_ok=True)
    plt.savefig(f'plots/{filename}.png')
    plt.close()
