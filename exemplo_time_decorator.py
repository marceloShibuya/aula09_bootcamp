from time_decorator import time_measure_decorator

@time_measure_decorator
def soma(x, y):
    return x + y

soma(x=2,y=1)
soma(5,5)
soma(2,"3")