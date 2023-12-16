componentes = {}


def registrar_rastreio_componente(id: str, status_atual: str, historico_processos: list[str]) -> None:
    componentes[id] = {
        "status_atual": status_atual,
        "historico_processos": historico_processos
    }


def buscar_componente(id: str) -> str:
    if id in componentes:
        return f"id: {id} \nstatus atual: {componentes[id]["status_atual"]} \n{', '.join(componentes[id]["historico_processos"])}\n"
    else:
        return f"Este componente não está sendo rastreado.\n"


def atualizar_componente(id: int, status_atual: str, historico_processo: str) -> None | str:
    if id in componentes:
        componentes[id]["status_atual"] = status_atual
        componentes[id]["historico_processos"].append(historico_processo)
    else:
        return "Este componente não está sendo rastreado"


# exemplo de registro
registrar_rastreio_componente(16, "Em produção", ["Setor A"])
registrar_rastreio_componente(
    24, "Checagem de qualidade", ["Setor A", "Setor B"])

# exemplo de busca e atualização
print(buscar_componente(16))
atualizar_componente(24, "Preparando para entrega", "Setor C")
print(atualizar_componente(11, "Em produção", "Setor A"))
print(buscar_componente(24))
