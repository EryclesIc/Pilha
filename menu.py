# from graph import grafoStarbucks
import numpy as np
import random
import pandas as pd
from starbucks import Starbucks

dados_planilha = pd.read_csv("https://raw.githubusercontent.com/EryclesIc/Pilha/main/directory.csv", encoding="UTF-8")

quant_linhas = len(dados_planilha)
print("Quantidade de linhas do dataframe é {}.\n".format(quant_linhas))

linha = dados_planilha.iloc[2]
grande_bosta = Starbucks(linha)

print(grande_bosta)





# grafo = grafoStarbucks()

# def menu():
#     quant_vertices = int(input("Digite a quantidade de vértices:\n"))
    
#     for i in range(quant_vertices):
#         linha_aleatoria = random.randint(0, quant_linhas)-1
#         linha = dados_planilha.iloc[linha_aleatoria]
#         starbucks_linha = Starbucks(linha)
        
#         print(starbucks_linha)
        #AQUI chame a função para adicionar as linhas no grafo
        # grafo.add_vertex(linha, dados_planilha, i)
        
    # AQUI chame a função para mostrar todos os vértices dentro do grafo
    # for j in range(quant_vertices):
    #     grafo.create_edge(j, quant_vertices, dados_planilha)
    # # for k in range(quant_vertices): print(grafo.get_vertex(k))
    # grafo.get_vertices()

    
    # vertice1 = input("Escolha o vértice inicial:\n")
    # vertice2 = input("Escolha o vértice final:\n")
    
    # for v in range(quant_vertices):
    #     for w in grafo.get_connections():
    #         vid = v.get_id()
    #         wid = w.get_id()
    #         print(vid)
    #         print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    # for v in grafo:
    #     print ('grafo.vert_dict[%s]=%s' %(v.get_id(), grafo.vert_dict[v.get_id()]))
    # AQUI chame a função que vai calcular a menor distância entre esses nós
#     menu()
# menu()
