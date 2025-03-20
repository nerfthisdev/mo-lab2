import numpy as np
import matplotlib.pyplot as plt
from optimizers import *

def plot_method(method, title, filename):
    """Визуализация работы метода"""
    plt.figure(figsize=(10, 6))
    
    # Основной график функции
    x = np.linspace(method.a, method.b, 400)
    y = [f(xi) for xi in x]
    plt.plot(x, y, label='f(x) = x² + e⁻ˣ', lw=2)
    
    # Отрисовка итераций
    if isinstance(method, (BisectionMethod, GoldenSectionMethod)):
        for step in method.history:
            plt.axvspan(step['left'], step['right'], 
                        alpha=0.1, color='blue')
            plt.scatter(step['points'], [f(p) for p in step['points']], 
                       color='red', s=40, zorder=3)
            
    elif isinstance(method, NewtonMethod):
        plt.scatter(method.history, [f(x) for x in method.history],
                   color='red', s=40, zorder=3)
        plt.plot(method.history, [f(x) for x in method.history], 
                '--', color='blue', alpha=0.5)
    
    # Финальная точка
    plt.scatter(method.result, f(method.result), 
               color='green', marker='*', s=200, label='Result')
    
    plt.title(f"{title}\nFound minimum at x = {method.result:.5f}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend()
    plt.grid(True)
    
    # Сохранение в файл
    plt.savefig(f"plots/{filename}.png", dpi=100)
    plt.close()
