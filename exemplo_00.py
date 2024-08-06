from loguru import logger

def soma(x,y):
    # print(x)
    logger.info(x)
    # print(y)
    logger.info(y)
    # print(x + y)
    logger.info(x + y)
    return x + y

total = soma(1,2)
print(total)



