import re
from _thread import start_new_thread
from random import randint
from datetime import datetime

tabela_sensores = {}


def resolver_conflito(tabela_hash: dict[str], timestamp: str):
    indices_para_exclusao: list[int] = []
    lista_sensores: list[tuple] = list(tabela_hash.items())

    for sensor in lista_sensores:
        if timestamp in sensor[0]:
            indices_para_exclusao.append(lista_sensores.index(sensor))

    while len(indices_para_exclusao) != 1:
        indice = indices_para_exclusao.pop()
        del lista_sensores[indice]

    tabela_hash = dict(lista_sensores)
    return tabela_hash


def cadastrar_sensor(id: int) -> None:
    temperatura = randint(-40, 50)  # ºC
    pressao = randint(1, 5)  # atm
    umidade = randint(10, 60)  # %
    leitura_sensor = {
        "temperatura": temperatura,
        "pressao": pressao,
        "umidade": umidade
    }

    timestamp = str(datetime.now().timestamp())
    chave = str(id) + timestamp
    tabela_sensores[chave] = leitura_sensor
    resolver_conflito(tabela_sensores, chave)


# id = 1
# while True:
#     start_new_thread(cadastrar_sensor, (id,))
#     id = id + 1
