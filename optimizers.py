import math
from abc import ABC, abstractmethod
from functions import f, df, d2f

class BaseOptimizer(ABC):
    def __init__(self, a, b, epsilon):
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.history = []
    
    @abstractmethod
    def solve(self):
        pass

class DichotomyMethod(BaseOptimizer):
    def solve(self):
        a, b = self.a, self.b
        delta = self.epsilon / 3
        
        while (b - a) > self.epsilon:
            c = (a + b) / 2
            x1 = max(a, c - delta)
            x2 = min(b, c + delta)
            
            self.history.extend([(x1, f(x1)), (x2, f(x2))])
            
            if f(x1) < f(x2):
                b = x2
            else:
                a = x1
        
        return (a + b) / 2

class GoldenSectionMethod(BaseOptimizer):
    def solve(self):
        a, b = self.a, self.b
        ratio = (math.sqrt(5) - 1) / 2
        
        x1 = b - ratio * (b - a)
        x2 = a + ratio * (b - a)
        self.history.extend([(x1, f(x1)), (x2, f(x2))])
        
        while (b - a) > self.epsilon:
            if f(x1) < f(x2):
                b = x2
                x2, x1 = x1, b - ratio * (b - a)
            else:
                a = x1
                x1, x2 = x2, a + ratio * (b - a)
            
            self.history.extend([(x1, f(x1)), (x2, f(x2))])
        
        return (a + b) / 2

class ChordMethod(BaseOptimizer):
    def solve(self):
        x_prev, x_curr = self.a, self.b
        
        for _ in range(1000):
            df_prev = df(x_prev)
            df_curr = df(x_curr)
            
            if abs(df_curr) < self.epsilon:
                break
                
            x_next = x_curr - df_curr * (x_curr - x_prev) / (df_curr - df_prev)
            x_next = max(self.a, min(x_next, self.b))
            self.history.append((x_next, f(x_next)))
            
            if abs(x_next - x_curr) < self.epsilon:
                break
                
            x_prev, x_curr = x_curr, x_next
        
        return x_curr

class NewtonMethod(BaseOptimizer):
    def __init__(self, a, b, epsilon, initial_guess=None):
        super().__init__(a, b, epsilon)
        self.initial_guess = initial_guess or (a + b)/2  # Значение по умолчанию
    
    def solve(self):  # Теперь без параметров
        x = self.initial_guess
        for _ in range(1000):
            self.history.append((x, f(x)))
            df_val = df(x)
            
            if abs(df_val) < self.epsilon:
                break
                
            x_next = x - df_val / d2f(x)
            x_next = max(self.a, min(x_next, self.b))
            
            if abs(x_next - x) < self.epsilon:
                break
                
            x = x_next
        
        return x
