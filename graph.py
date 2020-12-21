import numpy as np

class grafoStarbucks:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.matriz_adj = np.zeros((100, 100))

    def distancia(self, i, j): 
        return np.sqrt(((self.latitude[i] - self.latitude[j]) ** 2) + ((self.longitude[i] - self.longitude[j]) ** 2))

    def montar_matriz(self):
        for i in range(len(self.matriz_adj)):
            for j in range(len(self.matriz_adj[i])):
                self.matriz_adj[i][j] = self.distancia(i,j)
    
    '''
import heapq

def dijkstra (grafo, source, dist):
    pq, dist[source] = [(0, source)], 0
    while(len(pq)!=0):
        dequeued = heapq.heappop(pq)
        distancia,dequeued = dequeued[0], dequeued[1]
        if(distancia > dist[dequeued]):
            continue
        for i in range(0,len(grafo[dequeued])):
            g = grafo[dequeued]
            if((distancia+1) > dist[g[i]]):
                continue
            dist[g[i]] = distancia + 1
            heapq.heappush(pq, (distancia+1, g[i]) )
    return dist
    '''