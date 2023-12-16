inventario = {}


def adicionar_item(id: int, quantidade: int, localizacao: str, informacoes_fornecedor: str) -> None:
    inventario[id] = {
        "quantidade": quantidade,
        "localizacao": localizacao,
        "informacoes_fornecedor": informacoes_fornecedor
    }


def buscar_item(id: int) -> str:
    if id in inventario:
        return f"id: {id} \nquantidade: {inventario[id]["quantidade"]} \nlocalização: {inventario[id]["localizacao"]} \ninformacoes do fornecedor: {inventario[id]["informacoes_fornecedor"]}\n"
    else:
        return "Este item não está no inventário.\n"


def atualizar_item(id: int, quantidade: int, localizacao: str, informacoes_fornecedor: str) -> None | str:
    if id in inventario:
        inventario[id]["quantidade"] = quantidade
        inventario[id]["localizacao"] = localizacao
        inventario[id]["informacoes_fornecedor"] = informacoes_fornecedor
    else:
        return "Este item não está presente no inventário."


# exemplo de adição
adicionar_item(2, 250, "Ratanabá, AM", "Mercado Líder Gold")
adicionar_item(112, 750, "Doutor Severiano, RN", "Mercado Líder Platinum")

# exemplo de busca
print(buscar_item(2))
print(buscar_item(112))
