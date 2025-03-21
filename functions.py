import math

def f(x):
    """Целевая функция: f(x) = x² + e^(-x)"""
    return x**2 + math.exp(-x)

def df(x):
    """Первая производная: f'(x) = 2x - e^(-x)"""
    return 2*x - math.exp(-x)

def d2f(x):
    """Вторая производная: f''(x) = 2 + e^(-x)"""
    return 2 + math.exp(-x)



