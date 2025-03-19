import math

def f(x):
    return x**2 + math.exp(-x)

def df(x):
    return 2*x - math.exp(-x)

def d2f(x):
    return 2 + math.exp(-x)

def dichotomy_method(a_init, b_init, epsilon):
    a, b = a_init, b_init
    delta = epsilon / 3
    iterations = 0
    while (b - a) > epsilon:
        c = (a + b) / 2
        x1 = max(a, c - delta)
        x2 = min(b, c + delta)
        if f(x1) < f(x2):
            b = x2
        else:
            a = x1
        iterations += 1
    return (a, b) if f(a) < f(b) else (b, a), iterations

def golden_section_method(a_init, b_init, epsilon):
    a, b = a_init, b_init
    ratio = (math.sqrt(5) - 1) / 2
    iterations = 0

    x1 = b - ratio * (b - a)
    x2 = a + ratio * (b - a)
    f1, f2 = f(x1), f(x2)

    while (b - a) > epsilon:
        if f1 < f2:
            b, x2, f2 = x2, x1, f1
            x1 = b - ratio * (b - a)
            f1 = f(x1)
        else:
            a, x1, f1 = x1, x2, f2
            x2 = a + ratio * (b - a)
            f2 = f(x2)
        iterations += 1

    return (a, b) if f(a) < f(b) else (b, a), iterations

def chord_method(a_init, b_init, epsilon):
    a, b = a_init, b_init
    df_a, df_b = df(a), df(b)
    if df_a * df_b > 0:
        return (a if f(a) < f(b) else b), 0

    x_prev, x_curr = a, b
    iterations, max_iter = 0, 1000
    for _ in range(max_iter):
        df_prev, df_curr = df(x_prev), df(x_curr)
        if abs(df_curr) < epsilon:
            break
        if df_curr == df_prev:
            break
        denominator = df_curr - df_prev
        x_next = x_curr - df_curr * (x_curr - x_prev) / denominator
        x_next = max(a, min(x_next, b))
        if abs(x_next - x_curr) < epsilon:
            x_curr = x_next
            break
        x_prev, x_curr = x_curr, x_next
        iterations += 1

    return (x_curr if a <= x_curr <= b else (a if f(a) < f(b) else b)), iterations

def newton_method(initial_guess, epsilon, a, b):
    x = initial_guess
    iterations, max_iter = 0, 1000
    for _ in range(max_iter):
        df_val, d2f_val = df(x), d2f(x)
        if abs(df_val) < epsilon:
            break
        x_next = x - df_val / d2f_val
        x_next = max(a, min(x_next, b))
        if abs(x_next - x) < epsilon:
            x = x_next
            break
        x = x_next
        iterations += 1

    return (x if a <= x <= b else (a if f(a) < f(b) else b)), iterations

# Параметры задачи
a, b, epsilon = 0, 1, 0.0001

# Применение методов
dichotomy_result, di_iters = dichotomy_method(a, b, epsilon)
golden_result, gs_iters = golden_section_method(a, b, epsilon)
chord_result, ch_iters = chord_method(a, b, epsilon)
newton_result, nt_iters = newton_method((a + b)/2, epsilon, a, b)
# Вывод результатов
print(f"Метод половинного деления: x = {dichotomy_result[1]:.5f}, итераций: {di_iters}")
print(f"Метод золотого сечения: x = {golden_result[1]:.5f}, итераций: {gs_iters}")
print(f"Метод хорд: x = {chord_result:.5f}, итераций: {ch_iters}")
print(f"Метод Ньютона: x = {newton_result:.5f}, итераций: {nt_iters}")
print(f"Проверка границ: f(0) = {f(0):.5f}, f(1) = {f(1):.5f}")
