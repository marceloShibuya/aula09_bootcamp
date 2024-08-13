from functools import wraps
import time
from loguru import logger

def time_measure_decorator(func):
    """
    Decorador de medida de tempo
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Chamando função '{func.__name__}' com args {args} e kwargs {kwargs}")
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            logger.info(f"Função '{func.__name__}' executada em {end_time - start_time}")
            return result
        except Exception as e:
            logger.info(f"Função '{func.__name__}' não executada")
            raise
    return wrapper

