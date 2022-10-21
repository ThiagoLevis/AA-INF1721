import networkx as nx

# Trabalho 1

g = nx.Graph()

def printgraph():
    print(g.nodes())
    print(g.edges())

def addNode(node):
    g.add_node(node)

def addEdge(node1, node2):
    g.add_edge(node1, node2)
    
def nodeExist(node):
    for node in g.nodes():
        if node == node:
            return True
    return False

def edgeExist(node1, node2):
    for edge in g.edges():
        if edge[0] == node1 and edge[1] == node2:
            return True
    return False

# find eges of a node
def findEdges(node):
    for edge in g.edges():
        if edge[0] == node:
            print(edge[1])
        if edge[1] == node:
            print(edge[0])

def countNodes():
    return len(g.nodes())

def countEdges():
    return len(g.edges())

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

# create all possible arrays from a given array
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


# def printmatrix3x3(m):
#     for matrix in m:
#         print(matrix[0], matrix[1], matrix[2])
#         print(matrix[3], matrix[4], matrix[5])
#         print(matrix[6], matrix[7], matrix[8])
#         print('-------------')

# def printmatrix(matrix):
#     print(matrix[0], matrix[1], matrix[2])
#     print(matrix[3], matrix[4], matrix[5])
#     print(matrix[6], matrix[7], matrix[8])
#     print('-------------')

def makeListString(lista):
    string = ""
    for i in lista:
        string += str(i)
    return string

def criaGrafo(config):
    p = permutate(config)
    
    for cfgAtual in p:
        
        cfgAtualList = makeListString(cfgAtual)
        addNode(makeListString(cfgAtualList))

        newCfgList = moveItem(cfgAtual, 0)

        for cfg in newCfgList:
            cfgString = makeListString(cfg)

            addNode(cfgString)
            addEdge(cfgAtualList, cfgString)
            addEdge(cfgString, cfgAtualList)
            
        
    print("Nodes: ", countNodes())
    print("Edges: ", countEdges())


criaGrafo([0,1,2,3,4,5,6,7,8])
