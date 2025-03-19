import math

# Определяем функцию
def f(x):
    return x**2 + math.exp(-x)

# Производная функции (первая производная)
def df(x):
    return 2*x - math.exp(-x)

# Вторая производная функции
def d2f(x):
    return 2 + math.exp(-x)


# Метод половинного деления (для нахождения корня производной)
def bisection_method(left, right, epsilon):
    """
    Метод половинного деления для нахождения корня производной df(x) = 0.
    """
    while abs(right - left) > epsilon:
        mid = (left + right) / 2  # Середина интервала
        if df(mid) == 0:  # Если нашли точный корень
            return mid
        elif df(left) * df(mid) < 0:  # Если корень в левой половине
            right = mid
        else:  # Иначе корень в правой половине
            left = mid
    return (left + right) / 2  # Возвращаем середину последнего интервала



