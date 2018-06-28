def popmin(pqueue):
    # A (ascending or min) priority queue keeps element with
    # lowest priority on top. So pop function pops out the element with
    # lowest value. It can be implemented as sorted or unsorted array
    # (dictionary in this case) or as a tree (lowest priority element is
    # root of tree)
    lowest = 1000
    keylowest = None
    for key in pqueue:
        if pqueue[key] < lowest:
            lowest = pqueue[key]
            keylowest = key
    del pqueue[keylowest]
    return keylowest
 
def prim(graph, root,V):
    key = {}  # keep track of minimum weight for each vertex
    key = [1000] * V
    key[root] = 0 

    for i in range(V-1):
        for u,v,w in graph: # all neighbors of v
            if key[u] != 1000 and (key[u] + w) < key[v]:
                key[v] = key[u] + w
                print (key)
    print ('Check Negative edge cycle now.....')
    for u,v,w in graph: # all neighbors of v
        if key[u] != 1000 and (key[u] + w) < key[v]:
            print ('Graph contains negative weight cycle...')
            key[v] = key[u] + w
            print(key)
            return
    return key
 
##graph = {0 : {1:5, 2:4},
##1 : {3:3},
##2 : {1:-6},
##3 : {2:2}}

graph = ([0,1,5],[0,2,4],[1,3,3],[2,1,-6],[3,2,2])
key = prim(graph, 0,4)
print ('Vertex vs Distance from source...!!!')
##for i in range(3): print ("%s: %s" % (i, key[i]))

print (key)
