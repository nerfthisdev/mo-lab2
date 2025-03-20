import math

def f(x):
    return x**2 + math.exp(-x)

def df(x):
    return 2*x - math.exp(-x)

def d2f(x):
    return 2 + math.exp(-x)
