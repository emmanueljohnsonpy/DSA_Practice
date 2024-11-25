

# To Implement DFS Using Recursion / Unweighted Undirected Graph

def add_node(v):
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

def DFS(node, visited, graph):
    if node not in graph:
        print("Node is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)  # In weighted graph instead of calling i call i[0]

visited=set()
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

DFS("A", visited, graph)