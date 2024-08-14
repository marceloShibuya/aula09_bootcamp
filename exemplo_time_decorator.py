from time_decorator import time_measure_decorator
import time

@time_measure_decorator
def soma(x, y):
    time.sleep(2)
    return x + y

soma(x=2,y=1)
soma(5,5)
soma(2,"3")