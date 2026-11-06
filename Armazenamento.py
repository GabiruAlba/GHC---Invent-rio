import csv

def carregar_inventario():

    inventario = {}

    with open("inventario.csv", "r", newline="", encoding="utf-8") as arquivo:

        leitor = csv.DictReader(arquivo)

        for linha in leitor:

            categoria = linha["categoria"]

            if categoria not in inventario:
                inventario[categoria] = []

            movimentacao = {
                "codigo": linha["codigo"],
                "lote": linha["lote"],
                "tipo": linha["tipo"],
                "quantidade": int(linha["quantidade"])
            }

            inventario[categoria].append(movimentacao)

    return inventario