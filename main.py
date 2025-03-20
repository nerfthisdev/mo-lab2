import os
from optimizers import BisectionMethod, GoldenSectionMethod, NewtonMethod
from plot_utils import plot_method
from functions import f

# Создаем папку для графиков
os.makedirs("plots", exist_ok=True)

# Параметры задачи
a, b, eps = 0, 1, 0.003

# Инициализация методов
methods = {
    "Dichotomy": BisectionMethod(a, b, eps),
    "Golden Section": GoldenSectionMethod(a, b, eps),
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

# Сравнение с аналитическим решением
from scipy.optimize import minimize_scalar
res = minimize_scalar(f, bounds=(a, b), method='bounded')
print(f"\nАналитическое решение: x = {res.x:.5f}, f(x) = {res.fun:.5f}")
