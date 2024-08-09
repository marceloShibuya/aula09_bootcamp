from loguru import logger

logger.add(
            "logs_critical.log",
            format = "{time} {level} {message} {file}",
            level = "CRITICAL"
)

def soma(x,y):
    try:
        total = x + y
        logger.info(f"O total da soma é de: {total}")
        return total
    except:
        logger.critical("Por favor, digite números inteiros")


soma(1,10)
soma(20,1)
soma(1,"2")