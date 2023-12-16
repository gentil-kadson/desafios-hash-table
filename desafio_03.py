sensores = {}


def adicionar_sensor(id: int, leituras_recentes: list[str]) -> None:
    sensores[id] = {
        "leituras_recentes": leituras_recentes
    }


def buscar_informacoes_sensor(id: int) -> str:
    if id in sensores:
        return f"id: {id} \nleituras recentes: {", ".join(sensores[id]["leituras_recentes"])}\n"
    else:
        return "Este sensor não está sendo monitorado.\n"


# exemplo de cadastro
adicionar_sensor(5542, ["40 ºC", "-20 ºC", "48 ºC"])
adicionar_sensor(3566, ["100 ºC", "0 ºC", "17 ºC"])

# exemplo de busca
print(buscar_informacoes_sensor(5542))
print(buscar_informacoes_sensor(3566))
print(buscar_informacoes_sensor(110))
