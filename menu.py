from graph import latitudeLongitude
from graph import grafoStarbucks
import numpy as np
import random
import pandas as pd

dados_planilha = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Pilha/main/directory.csv", encoding="UTF-8")
quant_linhas = len(dados_planilha)
print("Quantidade de linhas do dataframe é {}.\n".format(quant_linhas))

grafo = grafoStarbucks()

def menu():
    quantVertices = int(input("Digite a quantidade de vértices:\n"))
    
    for i in range(quantVertices):
        linha_aleatoria = random.randint(0, quant_linhas)-1
        linha = dados_planilha.iloc[linha_aleatoria]
        print(linha)
        #AQUI chame a função para adicionar as linhas no grafo
        grafo.add_node(dados_planilha[0], linha)
    print(grafo)
        
    # AQUI chame a função para mostrar todos os vértices dentro do grafo

    
    # mostra_adjacentes()
    vertice1 = input("Escolha o vértice inicial:\n")
    vertice2 = input("Escolha o vértice final:\n")
    
    # AQUI chame a função que vai calcular a menor distância entre esses nós
    menu()
menu()

# matriz_adj = np.zeros((quant_linhas, quant_linhas))

# print(dados_planilha)
# g = latitudeLongitude(dados_planilha.Latitude, dados_planilha.Longitude)
# g.montar_matriz()


# print(g.distancia(0,1))
# print(matriz_adj.shape)



# graph = {}
# vstd = {}
# edges = []
# tree = {} 
# tam = 25600

# n = tam



# for i in range(n+1):
# 	graph[i] = {}
# #print(graph)

# dados = {}

# lista = LinkedList()
# # prim_check = Prim()

# for linha in range(2):
#     #print(linha)

#     elemento = dados_planilha.iloc[linha]
#     lista.append(elemento)

# print(lista)

#prim_check.iniciar()
#print("Custo da loja 0 para loja 1: ", tree[0][1])