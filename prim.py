class Prim:
    def iniciar():
	global graph, vstd, edges, tree, tam

	if len(graph) == 0 :	
		return

	for i in graph:
		if(len(graph[i]) > 0):
			tam = i
		tree [i]= {}

	vstd[tam] = True
	q = queue.PriorityQueue()
	
	for i in graph[tam]:
		q.put( ( graph[tam][i] , i, tam ) )

	cost = 0
	while not q.empty() :
		e = q.get()
		if e[1] in vstd : continue
		vstd[ e[1] ] , cost = True, cost + e[0]

        #Contruindo o novo grafo -> MST 
		edges.append( (e[1],e[2]) )
		tree[ e[1] ][ e[2] ] = e[0]
		tree[ e[2] ][ e[1] ] = e[0]

		for v in graph[ e[1] ]:
			if v not in vstd:
				q.put( (graph[ e[1] ][v] , v , e[1] ) )

	print("árvore", tree)
	print("custo:", cost)
	print("Arestas", edges)
	return cost , tree , edges

