import queue
from graph import grafoStarbucks
import numpy as np
# from prim import Prim
# from geopy.distance import geodesic
# import csv
import pandas as pd

dados_planilha = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Pilha/main/directory.csv", encoding="UTF-8")
# print(dados_planilha.columns.values)
# print(dados_planilha.Longitude[0])
# print(dados_planilha.Latitude[0])
latitude = dados_planilha.Latitude
longitude = dados_planilha.Longitude
store_number = dados_planilha['Store Number']
matriz_adj = np.zeros((100, 100))

print(dados_planilha)
g = grafoStarbucks(dados_planilha.Latitude, dados_planilha.Longitude)
g.montar_matriz()


# print(g.distancia(0,1))
# print(matriz_adj.shape)



graph = {}
vstd = {}
edges = []
tree = {} 
tam = 25600

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