import os
from optimizers import (
    BisectionMethod,
    GoldenSectionMethod,
    ChordMethod,
    QuadraticApproximation,
    NewtonMethod
)
from plot_utils import plot_method

# Настройки
os.makedirs("plots", exist_ok=True)
a, b, eps = 0, 1, 0.003

# Инициализация всех методов
methods = {
    "Dichotomy": BisectionMethod(a, b, eps),
    "Golden Section": GoldenSectionMethod(a, b, eps),
    "Chord": ChordMethod(a, b, eps),
    "Quadratic Approx": QuadraticApproximation(a, b, eps),
    "Newton": NewtonMethod(a, b, eps, x0=0.5)
}

# Запуск оптимизации и построение графиков
results = {}
for name, method in methods.items():
    result, iterations = method.solve()
    plot_method(method, f"{name} Method", name.lower().replace(" ", "_"))
    results[name] = (result, iterations)

# Вывод результатов
print("{:<15} | {:<10} | {:<10}".format("Method", "Result", "Iterations"))
print("-"*40)
for name, (res, iters) in results.items():
    print("{:<15} | {:<10.5f} | {:<10}".format(name, res, iters))

# Аналитическая проверка
from scipy.optimize import minimize_scalar
res = minimize_scalar(f, bounds=(a, b), method='bounded').x
print(f"\nAnalytical solution: {res:.5f}")
