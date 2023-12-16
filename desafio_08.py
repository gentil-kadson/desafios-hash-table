produtos_ou_categorias = {}


def cadastrar_produto(id: str, dados_vendas: int, demanda: str, avaliacoes: list[dict[str]]):
    produtos_ou_categorias[id] = {
        "dados_vendas": dados_vendas,
        "demanda": demanda,
        "avaliacoes": avaliacoes
    }


def imprimir_avaliacoes(avaliacoes: list[dict[str]]):
    string_de_avaliacoes = ''
    for avaliacao in avaliacoes:
        string_de_avaliacoes += f"  Cliente: {avaliacao["cliente"]} \n  detalhe: {
            avaliacao["detalhe"]}\n\n"

    return string_de_avaliacoes


def buscar_produto_ou_categoria(id: str):
    if id in produtos_ou_categorias:
        avaliacoes = produtos_ou_categorias[id]["avaliacoes"]

        return f"id: {id} \nVendas: {produtos_ou_categorias[id]["dados_vendas"]} unidades \nDemanda: {produtos_ou_categorias[id]["demanda"]} \nAvaliações: \n{imprimir_avaliacoes(avaliacoes)}"
    else:
        return "Produto ou categoria não registrado."


def atualizar_produto_ou_categoria(id: str, dados_vendas: int, demanda: str, avaliacoes: list[dict[str]]) -> None | str:
    if id in produtos_ou_categorias:
        produtos_ou_categorias[id]["dados_vendas"] = dados_vendas
        produtos_ou_categorias[id]["demanda"] = demanda
        produtos_ou_categorias[id]["avaliacoes"] = avaliacoes
    else:
        return "Este produto ou categoria não está na nossa base de dados."


# exemplo de registro
avaliacoes_produto_um = [
    {
        "cliente": "Dante",
        "detalhe": "Adorei, vou esquiar nisso."
    },
    {
        "cliente": "Vergil",
        "detalhe": "Is there something missing?!"
    },
    {
        "cliente": "Sparda",
        "detalhe": "Vou selar."
    }
]

avaliacoes_produto_dois = [
    {
        "cliente": "Itadori Yuji",
        "detalhe": "Sugoi!"
    },
    {
        "cliente": "Gojo Satoru",
        "detalhe": "I will win."
    },
    {
        "cliente": "Sukuna",
        "detalhe": "Amei meu Mahogara."
    }
]

cadastrar_produto("ccff0024", 2500, "Média", avaliacoes_produto_um)
cadastrar_produto("ddab580f", 7000, "Alta", avaliacoes_produto_dois)

print(buscar_produto_ou_categoria("ccff0024"))
print(buscar_produto_ou_categoria("ddab580f"))
print(buscar_produto_ou_categoria("00fff5ab"))
