from graph import grafoStarbucks
import numpy as np
import random
import pandas as pd

dados_planilha = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Pilha/main/directory.csv", encoding="UTF-8")
quant_linhas = len(dados_planilha)
print("Quantidade de linhas do dataframe é {}.\n".format(quant_linhas))

grafo = grafoStarbucks()

def menu():
    quant_vertices = int(input("Digite a quantidade de vértices:\n"))
    
    for i in range(quant_vertices):
        linha_aleatoria = random.randint(0, quant_linhas)-1
        linha = dados_planilha.iloc[linha_aleatoria]
        print(linha)
        #AQUI chame a função para adicionar as linhas no grafo
        grafo.add_vertex(linha, dados_planilha, i)
    print(grafo)
        
    # AQUI chame a função para mostrar todos os vértices dentro do grafo

    
    # mostra_adjacentes()
    vertice1 = input("Escolha o vértice inicial:\n")
    vertice2 = input("Escolha o vértice final:\n")
    
    # AQUI chame a função que vai calcular a menor distância entre esses nós
    menu()
menu()
