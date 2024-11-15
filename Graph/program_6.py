

# Graph Deletion Operation | Delete Node | Adjacency List

# Directed and Unweighted Graph

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

def delete_node(v):
    if v not in graph:
        print(v, "is not present in the Graph")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B")
add_edge("A", "C")
delete_node("A")
print(graph)  """

# Undirected and Unweighted Graph 

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
        graph[v2].append(v1) 

def delete_node(v):
    if v not in graph:
        print(v, "is not present in the Graph")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B")
add_edge("A", "C")
delete_node("A")
print(graph)  """

# Undirected Weighted Graph

def add_node(v):
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

def delete_node(v):
    if v not in graph:
        print(v, "is not present in the Graph")
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break


graph={}
add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 3)
add_edge("A", "C", 3)
delete_node("A")
print(graph) 

