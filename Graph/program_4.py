

# Graph Deletion Operation | Delete Node | Adjacency Matrix

# It will work for every type of Graph

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


def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()


add_node("A")
add_node("B")
add_node("C")
add_edge("A", "B", 10)
print("Graph after deleting : ")
delete_node("D")
print_graph()
print(nodes) 

