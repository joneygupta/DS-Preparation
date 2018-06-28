from collections import defaultdict

class Graph:
    def __init__(self,V):
        self.V = V
        self.graph = defaultdict(list)
        
    def addEdge(self,u,v):
        self.graph[u].append(v)

    def countPaths(self,s,t,visited,countpath):
        if (s==t):
            countpath = countpath+1
            print (countpath)
        else:
            for i in self.graph[s]:
                while(self.graph[i]):
                    if visited[i]==0:
                        visited[i]=1
                        self.countPaths(i,t,visited,countpath)
        return countpath
    
    def countPathUtil(self,s,t):
        visited = [0]*self.V
        countpath = 0
        
        count = self.countPaths(s,t,visited,countpath)
        print(count)
        
def main():
    g = Graph(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(0, 3);
    g.addEdge(2, 0);
    g.addEdge(2, 1);
    g.addEdge(1, 3);
    g.countPathUtil(2, 3)
main()
