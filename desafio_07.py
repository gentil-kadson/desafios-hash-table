remessas = {}


def cadastrar_remessa(numero_rastreio: int, localizacao_atual: str, status_entrega: str, detalhes_destinatario: str) -> None:
    remessas[numero_rastreio] = {
        "localizacao_atual": localizacao_atual,
        "status_entrega": status_entrega,
        "detalhes_destinatario": detalhes_destinatario
    }


def buscar_remessa(numero_rastreio: int) -> str:
    if numero_rastreio in remessas:
        return f"id: {numero_rastreio} \nstatus da entrega: {remessas[numero_rastreio]["status_entrega"]} \nlocalização atual: {remessas[numero_rastreio]["localizacao_atual"]} \ndetalhes do destinatário: {remessas[numero_rastreio]["detalhes_destinatario"]}\n"
    else:
        return "Esta remessa não está sendo rastreada."


def atualizar_remessa(numero_rastreio: int, localizacao_atual: str, status_entrega: str, detalhes_destinatario: str) -> None | str:
    if numero_rastreio in remessas:
        remessas[numero_rastreio] = {
            "localizacao_atual": localizacao_atual,
            "status_entrega": status_entrega,
            "detalhes_destinatario": detalhes_destinatario
        }
    else:
        return "Esta remessa não está sendo rastreada."


# exemplo de cadastro
cadastrar_remessa(10, "Jabutão dos Guararapes, PE",
                  "Em trânsito", "Vizinho ao Beach Park")
cadastrar_remessa(19, "Pau dos Ferros, RN",
                  "A caminho para entrega", "Vizinho ao Oeste Frios.")
cadastrar_remessa(23, "São Miguel, RN",
                  "Unidade de tratamento", "Perdo da Praia Chuvosa.")

# exemplo de uso
print(buscar_remessa(10))
print(buscar_remessa(23))
print(buscar_remessa(24))
atualizar_remessa(19, "Encanto, RN", "Em trânsito",
                  "Parte baixa da cidade, vizinho à praça em frente à igreja.")
print(buscar_remessa(19))
