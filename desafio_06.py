produtos = {}


def cadastrar_monitoramento_produto(id: int, dados_qualidade: dict[str], feedbacks: list[str]) -> None:
    produtos[id] = {
        "dados_qualidade": {
            "estado": dados_qualidade["estado"],
            "anos_de_uso": dados_qualidade["anos_de_uso"]
        },
        "feedbacks": ", ".join(feedbacks)
    }


def procurar_produto(id: int) -> str:
    if id in produtos:
        return f"id: {id} \ndados de qualidade: \nestado: {produtos[id]["dados_qualidade"]["estado"]} \nanos de uso: {produtos[id]["dados_qualidade"]["anos_de_uso"]} \n\nfeedbacks: {produtos[id]["feedbacks"]}\n"
    else:
        return f"Este produto não está registrado.\n"


def atualizar_produto(id: int, dados_qualidade: dict[str], feedbacks: list[str]) -> None | str:
    if id in produtos:
        produtos[id]["dados_qualidade"] = dados_qualidade
        produtos[id]["feedbacks"] = feedbacks
    else:
        return "Este produto não está registrado nos produtos."


produto_um = {
    "dados_qualidade": {
        "estado": "semi-novo",
        "anos_de_uso": 4,
    },
    "feedbacks": ["Tá top", "Bala", "Estado chique"]
}

produto_dois = {
    "dados_qualidade": {
        "estado": "usado",
        "anos_de_uso": 0.5,
    },
    "feedbacks": ["Só tem uma rachadura", "Muito bem limpo", "Bateria com saúde"]
}

produto_tres = {
    "dados_qualidade": {
        "estado": "novo",
        "anos_de_uso": 0,
    },
    "feedbacks": ["Produto importado", "Original", "Qualidade top"]
}

# exemplo de cadastro
cadastrar_monitoramento_produto(
    10, produto_um["dados_qualidade"], produto_um["feedbacks"])
cadastrar_monitoramento_produto(
    22, produto_dois["dados_qualidade"], produto_dois["feedbacks"])
cadastrar_monitoramento_produto(
    30, produto_tres["dados_qualidade"], produto_tres["feedbacks"])

# exemplo de busca
print(procurar_produto(10))
print(procurar_produto(22))
print(procurar_produto(30))
print(procurar_produto(222))
