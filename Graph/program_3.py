

# To Implement Graph Insertion Operation | Add Node | Adjacency List

# Undirected Unweighted Graph

""" def add_node(v):
    if v in graph:
        print(v, "is already present in Graph")
    else:
        graph[v]=[]
    
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not persent in the Graph")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)

graph={}
add_node("A")
add_node("B")
add_node("c")
add_edge("A", "B")
print(graph)  """

# Undirected Weighted Graph

""" def add_node(v):
    if v in graph:
        print(v, "is already present in Graph")
    else:
        graph[v]=[]
    
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not persent in the Graph")
    else:
        list1=[v2, cost]
        list2=[v1, cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print(graph)  """

# Directed Weighted Graph

""" def add_node(v):
    if v in graph:
        print(v, "is already present in Graph")
    else:
        graph[v]=[]
    
def add_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not persent in the Graph")
    else:
        list1=[v2, cost]
        # list2=[v1, cost]
        graph[v1].append(list1)
        # graph[v2].append(list2) 

graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print(graph)  """

# Directed Unweighted Graph

""" def add_node(v):
    if v in graph:
        print(v, "is already present in Graph")
    else:
        graph[v]=[]
    
def add_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not persent in the Graph")
    else:
        # list1=[v2, cost]
        # list2=[v1, cost]
        graph[v1].append(v2)
        # graph[v2].append(list2) 

graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B")
add_edge("A", "C")
print(graph)  """