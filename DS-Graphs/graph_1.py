
def Cycles_in_Directed(G):
        color = {u : 'white' for u in G}
        found = [False]

        for i in G:
            if color[i] == 'white':
                DFS(G,i,color,found)
            if found[0]:
                break
        return found[0]
    
def DFS(G,i,color,found):
    color[i] = 'grey'
    if found[0]:
        return        
    for j in G[i]:
        if color[j] == 'grey':
            found[0] = True
            return
        if color[j] == 'white':
            DFS(G,j,color,found)
    color[i] = 'black'

def main():
##    G = {0:[1],1:[2],2:[3],3:[4],4:[1]}
    G = {0:[1,3],1:[2,3],2:[],3:[0,4],4:[4]}
    print(Cycles_in_Directed(G))
    
main()    
