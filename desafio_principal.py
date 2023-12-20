from _thread import start_new_thread
from random import randint
from datetime import datetime

tabela_sensores = {}


def resolver_conflito(tabela_hash: dict[str], timestamp: str):
    hashes = []

    for chave in list(tabela_hash):
        if timestamp in chave:
            hashes.append(chave)

    if len(hashes) > 1:
        hashes.pop()
        for hash_code in hashes:
            del tabela_hash[hash_code]


def cadastrar_sensor(tabela_hash_sensores: dict[str], id: int) -> None:
    temperatura = randint(-40, 50)  # ºC
    pressao = randint(1, 5)  # atm
    umidade = randint(10, 60)  # %
    leitura_sensor = {
        "temperatura": temperatura,
        "pressao": pressao,
        "umidade": umidade
    }

    timestamp = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    chave = str(id) + timestamp
    tabela_hash_sensores[chave] = leitura_sensor
    resolver_conflito(tabela_hash_sensores, timestamp)


id = 1
while True:
    start_new_thread(cadastrar_sensor, (tabela_sensores, id))
    id = id + 1
