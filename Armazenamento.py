import csv

def carregar_inventario():
    """Estabelece o inventario atraves do tratamento de arquivo CSV, com categoria e quantidade"""

    Inventario = {}

    with open("Inventario.csv", "r", newline="", encoding="utf-8") as arquivo_inventario:

        leitor = csv.DictReader(arquivo_inventario)

        for linha in leitor:

            categoria = linha["categoria"]
            quantidade = linha["quantidade"]

            if categoria not in Inventario:
                Inventario[categoria] = []

            amostra = {
                "categoria": categoria,
                "quantidade": int(quantidade)
            }

            Inventario[categoria].append(amostra)

    return Inventario

def carregar_movimentacao():
        
    movimentacao_lista = {}

    with open("Movimentacao.csv", "r", newline="", encoding="utf-8") as arquivo_mov:

        leitor = csv.DictReader(arquivo_mov)

        for linha in leitor:

            categoria = linha["categoria"]

            if categoria not in movimentacao_lista:
                movimentacao_lista[categoria] = []

            movimentacao = {
                "codigo": linha["codigo"],
                "lote": linha["lote"],
                "tipo": linha["tipo"],
                "quantidade": int(linha["quantidade"])
            }

            movimentacao_lista[categoria].append(movimentacao)

    return movimentacao_lista