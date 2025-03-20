import matplotlib.pyplot as plt
import numpy as np
from optimizers import *

def plot_method(method, title, filename):
    plt.figure(figsize=(12, 7))
    x = np.linspace(method.a, method.b, 400)
    y = [f(xi) for xi in x]
    
    # Основной график функции
    plt.plot(x, y, label='f(x) = x² + e⁻ˣ', lw=2)
    
    # Отрисовка специфичных элементов для каждого метода
    if isinstance(method, (BisectionMethod, GoldenSectionMethod)):
        # Для методов с интервалами
        for step in method.history:
            plt.axvspan(step['left'], step['right'], alpha=0.1, color='blue')
            plt.scatter(step['points'], [f(p) for p in step['points']], 
                       color='red', s=40, zorder=3)
            
    elif isinstance(method, ChordMethod):
        # Для метода хорд
        points = [step['points'][0] for step in method.history]
        derivatives = [step['derivatives'][0] for step in method.history]
        plt.scatter(points, [f(p) for p in points], color='red', s=40)
        plt.plot(points, [f(p) for p in points], '--', color='blue', alpha=0.5)
        
        # Дополнительный график производной
        ax2 = plt.gca().twinx()
        ax2.plot(x, [df(xi) for xi in x], 'green', alpha=0.3, label="f'(x)")
        ax2.scatter(points, derivatives, color='darkgreen', s=40)
        ax2.axhline(0, color='gray', linestyle='--')
        ax2.legend(loc='upper right')
        
    elif isinstance(method, QuadraticApproximation):
        # Для квадратичной аппроксимации
        for i, step in enumerate(method.history):
            a, b, c = step['points'][:3]
            x_parab = np.linspace(a-0.1, b+0.1, 100)
            A, B, C = step['parabola']
            y_parab = A*x_parab**2 + B*x_parab + C
            plt.plot(x_parab, y_parab, '--', alpha=0.3, color='purple')
            
        plt.scatter([p for step in method.history for p in step['points']],
                  [f(p) for step in method.history for p in step['points']],
                  color='red', s=20, alpha=0.5)
        
    elif isinstance(method, NewtonMethod):
        # Для метода Ньютона
        plt.scatter(method.history, [f(x) for x in method.history],
                   color='red', s=40, zorder=3)
        plt.plot(method.history, [f(x) for x in method.history], 
                '--', color='blue', alpha=0.5)
    
    # Финальная точка
    plt.scatter(method.result, f(method.result), 
               color='green', marker='*', s=200, label='Result', zorder=4)
    
    plt.title(f"{title}\nMinimum at x = {method.result:.5f}")
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.grid(True)
    plt.legend()
    
    # Сохранение в файл
    plt.savefig(f"plots/{filename}.png", dpi=100, bbox_inches='tight')
    plt.close()
