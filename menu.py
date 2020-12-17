import queue
from node import Node
from linkedlist import LinkedList
# from prim import Prim
# from geopy.distance import geodesic
# import csv
import pandas as pd

dados_planilha = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Pilha/main/directory.csv", encoding="UTF-8")
graph = {}
vstd = {}
edges = []
tree = {} 
tam = 25600 

n = tam

for i in range(n+1):
	graph[i] = {}
#print(graph)

dados = {}

lista = LinkedList()
# prim_check = Prim()

for linha in range(1):
    #print(linha)
    elemento = dados_planilha.iloc[linha]
    lista.append(elemento)

print(lista)

#prim_check.iniciar()
#print("Custo da loja 0 para loja 1: ", tree[0][1])