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
    print("Nodes: ", countNodes(g))
    print("Edges: ", countEdges(g))
    print("--- create graph function time: %s seconds ---" % (time.time() - start_time))

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
            queue.extend(removeCommonElements(visited, list(graph[vertex]))) # graph[vertex] da os vizinhos de vertex
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

# teste com grafo menor
# j = nx.Graph()
# j.add_node(1)
# j.add_node(2)
# j.add_node(3)
# j.add_node(4)
# j.add_edge(1,2)
# j.add_edge(2,1)
# j.add_edge(3,1)
# j.add_edge(1,3)
# print(connectedComponents(j))

print('quantidade de componentes conexos do Grafo: ', connectedComponents(g))


# RESULTADO ABAIXO
# print(connectedComponents(g, '012345678'))
# foram achados 2 componentes conexo

# Trabalho 3


# PRECISA SER TESTADO AINDA

def removeCommonElementsLists(list1, list2):
    for i in list1:
        if i in list2:
            list1.remove(i)
    return list1

def bfsFurthest(graph, start, visited):
    queue =  [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)	
        if visited[vertex] == False:
            visited[vertex] = True
            print(path)
            print(list(graph[vertex]))
            listAux = removeCommonElementsLists(list(graph[vertex]), path)
            for next in listAux:
                queue.append((next, path + [next]))
    return vertex

print('furthest node from 012345678: ', bfsFurthest(g, '123456780', setAllNodesNotVisited(g)))

