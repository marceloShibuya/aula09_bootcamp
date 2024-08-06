from loguru import logger

# def soma(x,y):
#     # print(x)
#     logger.info(x)
#     # print(y)
#     logger.info(y)
#     # print(x + y)
#     logger.info(x + y)
#     return x + y

# total = soma(1,2)
# print(total)

"""
O logger.add() é uma função que cria o arquivo .log
"""
logger.add("meu_log.log")

"""
Salvando apenas os logs que são críticos
"""
logger.add("meu_log_critico.log", level="CRITICAL")

def soma(x,y):
    try:
        soma = x + y
        logger.info(f"Você digitou corretamente e a soma dos números é: {soma}")
        return soma
    except:
        logger.critical("É preciso digitar valores corretos")


soma(1,4)
soma(2,2)
soma(2,"3")