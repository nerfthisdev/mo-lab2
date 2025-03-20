from functions import f

class QuadraticApproximation:
    def __init__(self, a, b, epsilon):
        self.a = a
        self.b = b
        self.epsilon = epsilon
        self.history = []

    def solve(self):
        a, c, b = self.a, (self.a + self.b)/2, self.b
        
        x_min = 0
        for _ in range(1000):
            fa, fc, fb = f(a), f(c), f(b)
            
            numerator = (c - a)**2 * (fc - fb) - (c - b)**2 * (fc - fa)
            denominator = (c - a) * (fc - fb) - (c - b) * (fc - fa)
            
            if denominator == 0:
                break
                
            x_min = c - 0.5 * numerator / denominator
            x_min = max(self.a, min(x_min, self.b))
            self.history.append((x_min, f(x_min)))
            
            if abs(x_min - c) < self.epsilon:
                break
                
            values = {a: fa, c: fc, b: fb, x_min: f(x_min)}
            sorted_points = sorted(values.items(), key=lambda x: x[1])
            a, c, b = sorted_points[0][0], sorted_points[1][0], sorted_points[2][0]
        
        return x_min
