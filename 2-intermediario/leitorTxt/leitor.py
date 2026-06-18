
# Escreva um programa que leia um arquivo .txt, conte palavras, linhas e caracteres, e salve um relatório em outro arquivo.
import os

os.system("cls")
def gerar_relatorio(entrada, saida):
    with open("intermediario/leitorTxt/texto.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
    
    contagem_linhas = len(conteudo.splitlines())
    contagem_palavras = len(conteudo.split())
    contagem_caracteres = len(conteudo)
    print(contagem_linhas, contagem_palavras, contagem_caracteres)

    relatorio = (
            f"Relatório do arquivo: {entrada}\n"
            f"Total de linhas: {contagem_linhas}\n"
            f"Total de palavras: {contagem_palavras}\n"
            f"Total de caracteres: {contagem_caracteres}\n"
        )
    with open(saida, "w", encoding="utf-8") as f:
        f.write(relatorio)

    print("Relatório salvo em:", saida)



gerar_relatorio("intermediario/leitorTxt/texto.txt", "intermediario/leitorTxt/relatorio.txt")