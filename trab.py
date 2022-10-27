import networkx as nx
import numpy as np
import time

# Trabalho 1

g = nx.Graph()

def printg():
    print(g.nodes())
    print(g.edges())

def addNode(graph, node):
    graph.add_node(node)

def addEdge(graph, node1, node2):
    graph.add_edge(node1, node2)

def countNodes(graph):
    return len(graph.nodes())

def countEdges(graph):
    return len(graph.edges())

def moveItem(cfgAtual, item): # funcao para achar os vizinhos

    cfgNova = cfgAtual.copy()
    index = cfgAtual.index(item)
    listaCfgs = []

    if  index > 2: # move para cima
        cfgNova[index], cfgNova[index - 3] = cfgNova[index - 3], cfgNova[index]
        listaCfgs.append(cfgNova)
        cfgNova = cfgAtual.copy()
    if  index < 6:  # move para baixo
        cfgNova[index], cfgNova[index + 3] = cfgNova[index + 3], cfgNova[index]
        listaCfgs.append(cfgNova)
        cfgNova = cfgAtual.copy()
    if index % 3 != 0: # move para a esquerda
        cfgNova[index], cfgNova[index - 1] = cfgNova[index - 1], cfgNova[index]
        listaCfgs.append(cfgNova)
        cfgNova = cfgAtual.copy()
    if index % 3 != 2: # move para a direita
        cfgNova[index], cfgNova[index + 1] = cfgNova[index + 1], cfgNova[index]
        listaCfgs.append(cfgNova)
        cfgNova = cfgAtual.copy()

    return listaCfgs

def permutate(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return [arr]
    l = []
    for i in range(len(arr)):
        m = arr[i]
        remLst = arr[:i] + arr[i+1:]
        for p in permutate(remLst):
            l.append([m] + p)
    return l

def makeListString(lista):
    string = ""
    for i in lista:
        string += str(i)
    return string

def createGraph(config):
    start_time = time.time()
    p = permutate(config)
    for cfgAtual in p:
        cfgAtualList = makeListString(cfgAtual)
        addNode(g, makeListString(cfgAtualList))
        newCfgList = moveItem(cfgAtual, 0)
        for cfg in newCfgList:
            cfgString = makeListString(cfg)
            addNode(g, cfgString)
            addEdge(g, cfgAtualList, cfgString)
            addEdge(g, cfgString, cfgAtualList)
    print("--- create graph function time: %s seconds ---" % (time.time() - start_time))
    print("Nodes: ", countNodes(g))
    print("Edges: ", countEdges(g))

createGraph([0,1,2,3,4,5,6,7,8])

# vertices 362880 = 9! 
# arestas 483840 = 8! * 12
# exemplo conectado [0,1,2,3,4,5,6,7,8] - [3,1,2,0,4,5,6,7,8]
# exemplo nao conectado [0,1,2,3,4,5,6,7,8] - [1,2,3,4,5,6,7,8,0]

# Trabalho 2

# Fazendo com Hash

def removeCommonElements(dict1, list1):
    for i in list1:
        if dict1[i]:
            list1.remove(i)
    return list1

def bfs(graph, start, visited):
    queue =  [start]
    while queue:
        vertex = queue.pop(0)	
        if visited[vertex] == False:
            visited[vertex] = True
            queue.extend(removeCommonElements(visited, list(graph[vertex]))) # list(graph[vertex]) da os vizinhos do vertice em uma linha
    return visited

def setAllNodesNotVisited(graph):
    notVisited = {} 
    for node in graph:
        notVisited[node] = False
    return notVisited

def connectedComponents(graph):
    start_time = time.time()
    visited = setAllNodesNotVisited(graph)
    components = 0
    for node in graph:
        if visited[node] == False:	
            bfs(graph, node, visited)
            components += 1
    print("--- find conencted components function time: %s seconds ---" % (time.time() - start_time))

    return components

print('quantidade de componentes conexos do Grafo: ', connectedComponents(g))

# Trabalho 3

def longestPath(graph, start, visited):
    start_time = time.time()
    queue =  [start]
    lvls = [[start]]
    level = 0
    visitedNeighbor = visited.copy()
    visitedNeighbor[start] = True
    while queue != []:
        lvls.append([])
        for vertex in lvls[level]:
            if visited[vertex] == False:
                visited[vertex] = True
                neighbors = list(graph[vertex])
                for neighbor in neighbors:
                    if visitedNeighbor[neighbor] == False:
                        visitedNeighbor[neighbor] = True
                        lvls[level + 1].append(neighbor)
        if lvls[level] == []:
            print("--- find Longest path function time: %s seconds ---" % (time.time() - start_time))
            return [x for x in lvls if x]
        level += 1

a = longestPath(g, '123456780', setAllNodesNotVisited(g))

print('tamanho do caminho mais longo: ',len(a))
