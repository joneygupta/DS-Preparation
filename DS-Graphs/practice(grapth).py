def BFS(graph,start,path = []):
    count = 0
    q=[start]
    while q:
        v = q.pop(0)
        if v not in path:
            path += [v]
            q += graph[v]
    return path

#Cycles in a Directed graph
def DFS(graph,start,path = []):
    final = []
    count = 0
    q=[start]
    while q:
        v = q.pop()
        if v not in path:
            path += [v]
            q += graph[v]
            print(v)
        else:
            print ('helol')
            count += 1
    return path, count, final


    
def main():
##    graph = {'A':['B','D'], 'B':['A','D','C'], 'C':['B','E'], 'D':['A','B'], 'E':['C']}
    graph = {'A':['B','D'], 'B':['E'], 'D':['E'], 'E':[]}
    ans, count, final = DFS(graph,'A')
    print ('DFS Traversalof the graph is :%s' %ans)
    print ('%d Cycles found in the given Graph' %count)
    print('cycles contains paths: %s' %final)
    BFSresult = BFS(graph, 'A')
    print ('BFS Traversalof the graph is :%s' %BFSresult)

main()
