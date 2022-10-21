import networkx as nx
import numpy as np

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

def setAllNodesNotVisited(graph):
    for node in graph.nodes():
        graph.nodes[node]['visited'] = False

def setAllEdgesNotVisited(graph):
    for edge in graph.edges():
        graph.edges[edge]['visited'] = False

def checkIfNodeIsVisited(graph, node):
    if graph.nodes[node]['visited'] == True:
        return True
    return False

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

createGraph([0,1,2,3,4,5,6,7,8])

# vertices 362880 = 9! 
# arestas 483840 = 8! * 12
# exemplo conectado [0,1,2,3,4,5,6,7,8] - [3,1,2,0,4,5,6,7,8]
# exemplo nao conectado [0,1,2,3,4,5,6,7,8] - [1,2,3,4,5,6,7,8,0]

# Trabalho 2

def getVisitedNodes(graph):
    visitedNodes = []
    for node in graph.nodes():
        if graph.nodes[node]['visited'] == True:
            visitedNodes.append(node)
    return visitedNodes

def getConnectedNodes(graph, node):
    connectedNodes = []
    for edge in graph.edges():
        if edge[0] == node:
            connectedNodes.append(edge[1])
        if edge[1] == node:
            connectedNodes.append(edge[0])
    return connectedNodes

def removeCommonElements(list1, list2):
    for i in list2:
        if i in list1:
            list2.remove(i)
    return list2

def bfs(graph, start):
    visited, queue = [], [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(removeCommonElements(visited, list(graph[vertex])))
            graph.nodes[vertex]['visited'] = True
    return visited

def connectedComponents(graph):
    setAllNodesNotVisited(graph)
    components = 0
    for node in graph:
        if checkIfNodeIsVisited(graph, node) == False:
            bfs(graph, node)
            components += 1

    return components

# teste com grafo menor
# j = nx.Graph()
# j.add_node(1)
# j.add_node(2)
# j.add_node(3)
# j.add_node(4)
# j.add_edge(1,2)
# print(connectedComponents(j))


# RESULTADO ABAIXO
# print(connectedComponents(g, '012345678'))
# foram achados 2 componentes conexo

# Trabalho 3

# PRECISA SER TESTADO AINDA

# def bfsLongestPath(graph, start, end):
#     visited, queue = [], [start]
#     while queue:
#         vertex = queue.pop(0)
#         if vertex not in visited:
#             visited.append(vertex)
#             queue.extend(removeCommonElements(visited, list(graph[vertex])))
#             graph.nodes[vertex]['visited'] = True
#     return len(visited)

# print(bfsLongestPath(g, '012345678', '123456780'))