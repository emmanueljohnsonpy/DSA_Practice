

# Graph Deletion Operation | Delete Edge | Adjacency List

# Undirected UnWeighted Graph

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
            for j in list1:
                if v==j[0]:
                    list1.remove(j)
                    break

def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A", "B")
add_edge("B", "E")
add_edge("A", "C")
add_edge("A", "D")
add_edge("B", "D")

add_edge("C", "D")
add_edge("E", "D")
print(graph) 
delete_edge("C", "D")
print(graph)
"""

# Directed UnWeighted Graph

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
        # graph[v2].append(v1) 

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

def delete_edge(v1, v2):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            # graph[v2].remove(v1)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")
add_node("F")
add_node("G")

add_edge("A", "B")
add_edge("B", "E")
add_edge("A", "C")
add_edge("B", "D")
add_edge("F", "C")
add_edge("F", "G")
add_edge("G", "D")

print(graph) 
delete_edge("F", "C")
print(graph) """

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

def delete_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        temp1=[v1, cost]
        temp2=[v2, cost]
        if temp2 in graph[v1]:
            graph[v1].remove(temp2)
            graph[v2].remove(temp1)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A", "B", 10)
add_edge("B", "E", 3)
add_edge("A", "C", 5)
add_edge("A", "D", 4)
add_edge("B", "D", 7)
add_edge("C", "D", 1)
add_edge("E", "D", 2)

print(graph) 
delete_edge("C", "D", 1)
print(graph) """

# Directed Weighted Graph

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
        # list2=[v1, cost]
        graph[v1].append(list1)
        # graph[v2].append(list2) 

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

def delete_edge(v1, v2, cost):
    if v1 not in graph:
        print(v1, "is not present in the Graph")
    elif v2 not in graph:
        print(v2, "is not present in the graph")
    else:
        # temp1=[v1, cost]
        temp2=[v2, cost]
        if temp2 in graph[v1]:
            graph[v1].remove(temp2)
            # graph[v2].remove(temp1)

graph={}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge("A", "B", 10)
add_edge("B", "E", 3)
add_edge("A", "C", 5)
add_edge("A", "D", 4)
add_edge("B", "D", 7)
add_edge("C", "D", 1)
add_edge("E", "D", 2)

print(graph) 
delete_edge("C", "D", 1)
print(graph)
