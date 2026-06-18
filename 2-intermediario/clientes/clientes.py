# Trabalhe com JSON: leia um arquivo de clientes, filtre os que têm mais de 30 anos, adicione um novo campo "senior" e salve de volta em JSON.

import os, json
def gerar_relatorio(entrada, saida):
    caminho = os.path.join(os.path.dirname(__file__), "clientes.json")
    with open(caminho, "r", encoding="utf-8") as f:
        clientes = json.load(f)

    clientes_filtrados = []
    for cliente in clientes:
        if cliente["idade"] > 30:
            cliente["senior"] = True 
            clientes_filtrados.append(cliente)
    print(clientes_filtrados)

    relatorio = (
            f"Relatório do arquivo: {entrada}\n"
            f"Clientes filtrados: {clientes_filtrados}\n"
        )
    with open(saida, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print("Relatório salvo em:", saida)

gerar_relatorio("intermediario/clientes/clientes.txt", "intermediario/clientes/clientesFiltrados.json")