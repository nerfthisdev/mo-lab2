import math
from functions import f, d2f, df

class BisectionMethod:
    def __init__(self, a, b, eps):
        self.a = a
        self.b = b
        self.eps = eps
        self.history = []
        
    def solve(self):
        a, b = self.a, self.b
        delta = self.eps / 3
        iterations = 0
        
        while (b - a) > self.eps:
            c = (a + b)/2
            x1 = max(a, c - delta)
            x2 = min(b, c + delta)
            
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
        self.history = []
        
    def solve(self):
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

class ChordMethod:
    def __init__(self, a, b, eps):
        self.a = a
        self.b = b
        self.eps = eps
        self.history = []
        
    def solve(self):
        """Метод хорд для поиска корня производной"""
        x_prev = self.a
        x_curr = self.b
        iterations = 0
        
        while True:
            df_prev = df(x_prev)
            df_curr = df(x_curr)
            
            self.history.append({
                'points': [x_curr],
                'derivatives': [df_curr]
            })
            
            if abs(df_curr) < self.eps:
                break
                
            try:
                x_next = x_curr - df_curr*(x_curr - x_prev)/(df_curr - df_prev)
            except ZeroDivisionError:
                break
                
            x_next = max(self.a, min(x_next, self.b))
            
            if abs(x_next - x_curr) < self.eps:
                break
                
            x_prev, x_curr = x_curr, x_next
            iterations += 1
            
        self.result = x_curr
        return self.result, iterations

class QuadraticApproximation:
    def __init__(self, a, b, eps):
        self.a = a
        self.b = b
        self.eps = eps
        self.history = []
        
    def solve(self):
        """Метод квадратичной аппроксимации"""
        a, c, b = self.a, (self.a+self.b)/2, self.b
        iterations = 0
        
        while True:
            fa, fc, fb = f(a), f(c), f(b)
            
            # Коэффициенты параболы
            denominator = (b - a)*(b - c)*(c - a)
            if denominator == 0:
                break
                
            A = (fb*(c - a) + fc*(a - b) + fa*(b - c)) / denominator
            B = (fb*(a**2 - c**2) + fc*(b**2 - a**2) + fa*(c**2 - b**2)) / denominator
            C = (fb*(c - a)*a*c + fc*(a - b)*b*a + fa*(b - c)*c*b) / denominator
            
            # Вершина параболы
            x_min = -B/(2*A) if A != 0 else c
            x_min = max(self.a, min(x_min, self.b))
            
            self.history.append({
                'points': [a, c, b, x_min],
                'parabola': (A, B, C)
            })
            
            if abs(x_min - c) < self.eps:
                break
                
            # Обновление точек
            new_points = sorted([a, b, c, x_min], key=lambda x: f(x))[:3]
            a, c, b = sorted(new_points)
            iterations += 1
            
        self.result = x_min
        return self.result, iterations

class NewtonMethod:
    def __init__(self, a, b, eps, x0=None):
        self.a = a
        self.b = b
        self.eps = eps
        self.x0 = x0 or (a + b)/2
        self.history = []
        
    def solve(self):
        x = self.x0
        iterations = 0
        
        while True:
            self.history.append(x)
            grad = df(x)
            hess = d2f(x)
            
            if abs(grad) < self.eps or hess == 0:
                break
                
            x_new = x - grad/hess
            x_new = max(self.a, min(x_new, self.b))
            
            if abs(x_new - x) < self.eps:
                break
                
            x = x_new
            iterations += 1
            
        self.result = x
        return self.result, iterations
