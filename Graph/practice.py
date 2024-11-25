""" def add_node(v):
    global node_count
    if v in nodes:
        print(v, 'is already in the graph')
    else:
        nodes.append(v)
        node_count+=1
    for i in graph:
        i.append(0)
    temp=[]
    for i in range(node_count):
        temp.append(0)
    graph.append(temp)

def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<3"), end=" ")
        print()
    
def add_edge_uduw(v1, v2):
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    if v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1
        graph[index2][index1]=1
    
def add_edge_udw(v1, v2, cost):
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    if v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost
        graph[index2][index1]=cost

def add_edge_dw(v1, v2, cost):
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    if v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=cost

def add_edge_duw(v1, v2):
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    if v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=1

def delete_node(v): # it will work for every types of graphs
    global node_count
    if v not in nodes:
        print(v, 'is not present in the graph')
    else:
        index=nodes.index(v)
        nodes.remove(v)
        node_count-=1
        graph.pop(index)
        for i in graph:
            i.pop(index)
def delete_edge_uwud(v1, v2):
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    if v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0
        graph[index2][index1]=0

def delete_edge_uwd(v1, v2):
    if v1 not in nodes:
        print(v1, 'is not present in the graph')
    if v2 not in nodes:
        print(v2, 'is not present in the graph')
    else:
        index1=nodes.index(v1)
        index2=nodes.index(v2)
        graph[index1][index2]=0 


nodes=[]
graph=[]
node_count=0
add_node('A')
add_node('B')
add_node('C')
print("Nodes :", nodes) 
delete_node('B')
print_graph()  """



def add_node(v):
    if v in graph:
        print(v, 'is already present in Graph')
    else:
        graph[v]=[]

def add_edge_uduw(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
def add_edge_udw(v1, v2, cost):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])

def add_edge_dw(v1, v2, cost):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        graph[v1].append([v2, cost])

def add_edge_duw(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        graph[v1].append(v2)

def delete_node_duw(v): # uduw
    if v not in graph:
        print(v, 'is not present in the graph')
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            if v in list1:
                list1.remove(v)

def delete_node_udw(v): # dw
    if v not in graph:
        print(v, 'is not present in the graph')
    else:
        graph.pop(v)
        for i in graph:
            list1=graph[i]
            for j in list1:
                if j[0]==v:
                    list1.remove(j)
                    break

def delete_edge_uduw(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)

def delete_edge_duw(v1, v2):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)

def delete_edge_udw(v1, v2, cost):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        if [v2, cost] in graph[v1]:
            graph[v1].remove([v2, cost])
            graph[v2].remove([v1, cost])

def delete_edge_dw(v1, v2, cost):
    if v1 not in graph:
        print(v1, 'is not present in the graph')
    if v2 not in graph:
        print(v2, 'is not present in the graph')
    else:
        if [v2, cost] in graph[v1]:
            graph[v1].remove([v2, cost])

def DFS(node, visited, graph):
    if node not in graph:
        print("node is not present in the graph")
        return
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i, visited, graph)    # w use i[0]

def DFSiterative(node, graph):
    visited=set()
    if node not in graph:
        print("Node is not prsent in the Graph")
        return
    stack=[]
    stack.append(node)
    while stack:
        current=stack.pop()
        if current not in visited:
            print(current)
            visited.add(current)
            for i in graph[current]:
                stack.append(i)


visited=set()
graph={}
add_node('A')
add_node('B')
add_node('C')
print(graph) 