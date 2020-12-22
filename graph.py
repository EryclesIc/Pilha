import numpy as np
from node import Node

class Vertex:
    def __init__(self, node, dataframe, n):
        self.id = node
        self.adjacent = {}
        self.brand = dataframe.Brand[n]
        self.store_number = dataframe['Store Number'][n]
        self.ownership_type = dataframe['Ownership Type'][n]
        self.street_address = dataframe['Street Address'][n]
        self.city = dataframe.City[n]
        self.state_province = dataframe['State/Province'][n]
        self.country = dataframe.Country[n]
        self.postcode = dataframe.Postcode[n]
        self.phone_number = dataframe['Phone Number'][n]
        self.timezone = dataframe.Timezone[n]
        self.longitude = dataframe.Longitude[n]
        self.latitude = dataframe.Latitude[n]

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([n.id for n in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class grafoStarbucks:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node, dataframe, n):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node, dataframe, n)
        # print(new_vertex)
        self.vert_dict[n] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def create_edge(self, n):
        

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

# if __name__ == '__main__':

#     g = Graph()

#     g.add_vertex('a')
#     g.add_vertex('b')
#     g.add_vertex('c')
#     g.add_vertex('d')
#     g.add_vertex('e')
#     g.add_vertex('f')

#     g.add_edge('a', 'b', 7)  
#     g.add_edge('a', 'c', 9)
#     g.add_edge('a', 'f', 14)
#     g.add_edge('b', 'c', 10)
#     g.add_edge('b', 'd', 15)
#     g.add_edge('c', 'd', 11)
#     g.add_edge('c', 'f', 2)
#     g.add_edge('d', 'e', 6)
#     g.add_edge('e', 'f', 9)

#     for v in g:
#         for w in v.get_connections():
#             vid = v.get_id()
#             wid = w.get_id()
#             print '( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w))

#     for v in g:
#         print 'g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()])


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
# class latitudeLongitude:
#     def __init__(self, latitude, longitude):
#         self.latitude = latitude
#         self.longitude = longitude
#         self.matriz_adj = np.zeros((25600, 25600))

#     def distancia(self, i, j): 
#         return np.sqrt(((self.latitude[i] - self.latitude[j]) ** 2) + ((self.longitude[i] - self.longitude[j]) ** 2))

#     def montar_matriz(self):
#         for i in range(len(self.matriz_adj)):
#             for j in range(len(self.matriz_adj[i])):
#                 self.matriz_adj[i][j] = self.distancia(i,j)