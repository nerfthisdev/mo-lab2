import math
from functions import f, df, d2f

class BisectionMethod:
    def __init__(self, a, b, eps):
        self.a = a
        self.b = b
        self.eps = eps
        self.history = []  # Для визуализации: храним границы интервалов
        
    def solve(self):
        """Метод половинного деления"""
        a, b = self.a, self.b
        iterations = 0
        delta = self.eps / 3
        
        while (b - a) > self.eps:
            c = (a + b)/2
            x1 = c - delta
            x2 = c + delta
            
            # Сохраняем данные для графика
            self.history.append({
                'left': a,
                'right': b,
                'points': [x1, x2]
            })
            
            if f(x1) < f(x2):
                b = x2
            else:
                a = x1
            iterations += 1
            
        self.result = (a + b)/2
        return self.result, iterations

class GoldenSectionMethod:
    def __init__(self, a, b, eps):
        self.a = a
        self.b = b
        self.eps = eps
        self.history = []  # Храним все промежуточные интервалы
        
    def solve(self):
        """Метод золотого сечения"""
        a, b = self.a, self.b
        ratio = (math.sqrt(5)-1)/2
        iterations = 0
        
        x1 = b - ratio*(b-a)
        x2 = a + ratio*(b-a)
        f1, f2 = f(x1), f(x2)
        
        while (b - a) > self.eps:
            self.history.append({
                'left': a,
                'right': b,
                'points': [x1, x2]
            })
            
            if f1 < f2:
                b = x2
                x2, f2 = x1, f1
                x1 = b - ratio*(b-a)
                f1 = f(x1)
            else:
                a = x1
                x1, f1 = x2, f2
                x2 = a + ratio*(b-a)
                f2 = f(x2)
                
            iterations += 1
            
        self.result = (a + b)/2
        return self.result, iterations

class NewtonMethod:
    def __init__(self, a, b, eps, x0=None):
        self.a = a
        self.b = b
        self.eps = eps
        self.x0 = x0 or (a + b)/2  # Начальное приближение
        self.history = []  # Точки итераций
        
    def solve(self):
        """Метод Ньютона"""
        x = self.x0
        iterations = 0
        
        while True:
            self.history.append(x)
            grad = df(x)
            hess = d2f(x)
            
            if abs(grad) < self.eps:
                break
                
            x_new = x - grad/hess
            x_new = max(self.a, min(x_new, self.b))  # Ограничение интервалом
            
            if abs(x_new - x) < self.eps:
                break
                
            x = x_new
            iterations += 1
            
        self.result = x
        return self.result, iterations
