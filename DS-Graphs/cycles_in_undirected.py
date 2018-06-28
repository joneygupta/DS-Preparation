# Python Program to <a href="#">detect cycle in an undirected graph</a>
 
from collections import defaultdict
  
#This class represents a undirected graph using adjacency list representation
class Graph:
  
    def __init__(self,vertices):
        self.V= vertices #No. of vertices
        self.graph = defaultdict(list) # default dictionary to store graph
 
  
    # function to add an edge to graph
    def addEdge(self,v,w):
        self.graph[v].append(w) #Add w to v_s list
        self.graph[w].append(v) #Add v to w_s list
  
    # A recursive function that uses visited[] and parent to detect
    # cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self,v,visited,parent):
        visited[v]= True
 
        for i in self.graph[v]:
            if  visited[i]==False : 
                if(self.isCyclicUtil(i,visited,v)):
                    return True
            # If an adjacent vertex is visited and not parent of current vertex,
            # then there is a cycle
            elif  parent!=i:
                return True
         
        return False
         
  
    #Returns true if the graph contains a cycle, else false.
    def isCyclic(self):
        visited =[False]*(self.V)
        #DFS trees
        for i in range(self.V):
            if visited[i] ==False: 
                if(self.isCyclicUtil(i,visited,-1))== True:
                    return True
         
        return False


def main():
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 0)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
     
    if g.isCyclic():
        print ("Graph contains cycle")
    else :
        print ("Graph does not contain cycle ")
    g1 = Graph(3)
    g1.addEdge(0,1)
    g1.addEdge(1,2)
     
     
    if g1.isCyclic():
        print ("Graph contains cycle")
    else :
        print ("Graph does not contain cycle ")

main()    
