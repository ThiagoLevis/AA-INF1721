# AA - INF1721

Quantos nós e arestas existem no grafo do espaço de estados que você construiu
    vertices:
    362880 = 9! 
    arestas:
    483840 = 8! * 12
    
Um exemplo de dois nós no grafo conectados por uma aresta
    exemplos conectados:
    - [0,1,2,3,4,5,6,7,8] 
    - [3,1,2,0,4,5,6,7,8]

Um exemplo de dois nós no grafo que não tem uma aresta entre eles
    exemplos não conectados:
    - [0,1,2,3,4,5,6,7,8] 
    - [1,2,3,4,5,6,7,8,0]
    
O código principal da sua BFS:
  
  def bfs(graph, start, visited):
    queue =  [start]
    while queue:
        vertex = queue.pop(0)	
        if visited[vertex] == False:
            visited[vertex] = True
            queue.extend(removeCommonElements(visited, list(graph[vertex]))) # graph[vertex] da os vizinhos de vertex
    return visited

Reporte quantos gráficos conexos tem o grafo construído na tarefa 1.
  print(connectedComponents(g, '012345678'))
  foram achados 2 componentes conexo
  
A configuração inicial viável que necessita o maior número de movimentos para se chegar a configuração cfg* ...

O número de movimentos necessários para ir dessa configuração a cfg* ...
