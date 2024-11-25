

# Graph Deletion Operation | Delete Edge | Adjacency Matrix

# Weighted or Unweighted and Undirected Graph 

nodes=[]
graph=[]
node_count=0

def add_node(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count+=1
        nodes.append(v)
    for n in graph:
        n.append(0)
    temp=[]
    for i in range(node_count):
        temp.append(0)
    graph.append(temp)

def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in the Graph")
    elif v2 not in nodes:
        print(v2, "is not present in the Graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present in the Graph")
    else:
        index=nodes.index(v)
        node_count-=1
        nodes.remove(v)
        graph.pop(index)
        for i in graph:
            i.pop(index)

def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in Graph")
    elif v2 not in nodes:
        print(v2, "is not present in Graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0
    

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()


add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print_graph()
delete_edge("A", "C")
print("Graph after deleting : ")
print_graph()
print("Nodes", nodes)
print("node_count", node_count)

# Weighted or Unweighted and Directed Graph 

nodes=[]
graph=[]
node_count=0

def add_node(v):
    global node_count
    if v in nodes:
        print(v, "is already present in the graph")
    else:
        node_count+=1
        nodes.append(v)
    for n in graph:
        n.append(0)
    temp=[]
    for i in range(node_count):
        temp.append(0)
    graph.append(temp)

def add_edge(v1, v2, cost):
    if v1 not in nodes:
        print(v1, "is not present in the Graph")
    elif v2 not in nodes:
        print(v2, "is not present in the Graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        # graph[index2][index1]=cost

def delete_node(v):
    global node_count
    if v not in nodes:
        print(v, "is not present in the Graph")
    else:
        index=nodes.index(v)
        node_count-=1
        nodes.remove(v)
        graph.pop(index)
        for i in graph:
            i.pop(index)

def delete_edge(v1, v2):
    if v1 not in nodes:
        print(v1, "is not present in Graph")
    elif v2 not in nodes:
        print(v2, "is not present in Graph")
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        # graph[index2][index1]=0
    

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()


add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
add_edge("A", "C", 5)
print_graph()
delete_edge("A", "C")
print("Graph after deleting : ")
print_graph()
print("Nodes", nodes)
print("node_count", node_count)