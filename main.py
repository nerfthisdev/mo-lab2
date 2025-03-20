from optimizers import DichotomyMethod, GoldenSectionMethod, ChordMethod, NewtonMethod
from quadratic_approx import QuadraticApproximation
from plot_utils import plot_optimization
from functions import f
import os

# Параметры задачи
a, b, epsilon = 0, 1, 0.003

# Создаем папку для графиков
os.makedirs('plots', exist_ok=True)

# Инициализация методов
methods = {
    'Dichotomy': DichotomyMethod(a, b, epsilon),
    'GoldenSection': GoldenSectionMethod(a, b, epsilon),
    'Chord': ChordMethod(a, b, epsilon),
    'Newton': NewtonMethod(a, b, epsilon, initial_guess=0.5),
    'QuadraticApproximation': QuadraticApproximation(a, b, epsilon)
}

# Запуск оптимизации и сохранение графиков
results = {}
for name, method in methods.items():
    result = method.solve()
    
    results[name] = result
    plot_optimization(
        history=method.history,
        a=a,
        b=b,
        title=name,
        filename=name.lower()
    )

# Вывод результатов
print("Результаты оптимизации:")
for name, x in results.items():
    print(f"{name:20} -> x = {x:.5f}, f(x) = {f(x):.5f}")

# Аналитическая проверка
from scipy.optimize import minimize_scalar
res = minimize_scalar(f, bounds=(a, b), method='bounded')
print(f"\nАналитическое решение: x = {res.x:.5f}, f(x) = {res.fun:.5f}")
