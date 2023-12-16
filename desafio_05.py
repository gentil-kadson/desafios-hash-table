from datetime import date
ordens_de_producao = {}


def registrar_ordem_producao(numero_ordem: int, detalhes: str, prazo: date) -> None:
    ordens_de_producao[numero_ordem] = {
        "detalhes": detalhes,
        "prazo": prazo
    }


def procurar_ordem_producao(numero_ordem: int) -> str:
    if numero_ordem in ordens_de_producao:
        return f"número: {numero_ordem} \ndetalhes: {ordens_de_producao[numero_ordem]["detalhes"]} \nprazo: {ordens_de_producao[numero_ordem]["prazo"]}\n"
    else:
        return "Essa ordem de produção não está cadastrada.\n"


# exemplo de cadastro
registrar_ordem_producao(533, "Iphone XR 50 GB", date(2024, 1, 30))
registrar_ordem_producao(1245, "Samsung Galaxy S23", date(2024, 2, 4))

# exemplo de busca
print(procurar_ordem_producao(533))
print(procurar_ordem_producao(1000))
print(procurar_ordem_producao(1245))
