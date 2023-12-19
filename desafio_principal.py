from _thread import start_new_thread
from random import randint
from datetime import datetime

tabela_sensores = {}


def resolver_conflito(tabela_sensores: dict[str], chave: str):
    lista_sensores: list[tuple] = list(tabela_sensores.items())
    while lista_sensores.count((chave, tabela_sensores[chave])) > 1:
        indice_da_copia = lista_sensores.index((chave, tabela_sensores[chave]))
        del lista_sensores[indice_da_copia]
        lista_sensores = tuple(lista_sensores)
        tabela_sensores = dict((x, y) for x, y in lista_sensores)


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


id = 1
while True:
    runningThread = start_new_thread(cadastrar_sensor, (id,))
    id = id + 1
