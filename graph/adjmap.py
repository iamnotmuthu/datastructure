
from collections import defaultdict,deque

class Graph():
    def __init__(self) -> None:
       self.g=defaultdict(list)
       self.vertices=[]
    
    def addVertex(self,v):
        self.vertices.append(v)
            
    def addEdge(self,frm,to):
        if frm not in self.vertices:
            print('unknown vertex',frm)
        elif to not in self.vertices:
            print('unknown vertex',to)
        else:
            self.g[frm].append(to)
            #self.g[to].append(frm)

    def print(self):
        for v in self.vertices:
            print(v,'-> ',self.g[v])
        
    def dfs(self,start):
        visited=set()
        self._dfs(start,visited)
    
    def _dfs(self,vertex,visited):
        if vertex not in visited:
            print('visiting',vertex)
            visited.add(vertex)
            for e in self.g[vertex]:
                self._dfs(e,visited)
        #else:
           # print('skipping visited vertex',vertex)
    

    def bfs(self, vertex):
        print('Starting bfs')
        visited=set()
        q=deque([])
        q.append(vertex)
        while q:
            v=q.popleft()
            if v not in visited:
                visited.add(v)
                print('visiting ',v)
                q.extend(self.g[v])
    


    def bfs_recur(self,q,visited_set):
        while q:
            vtx=q.pop(0)
            if vtx not in visited_set:
                q.extend(self.g[vtx])
                visited_set.add(vtx)
                print('visiting', vtx)
            self.bfs_recur(q,visited_set)

    
    def topsort(self,v,visited_set,res):
        if v not in visited_set:
            visited_set.add(v)
            for vtx in self.g[v]:
                self.topsort(vtx,visited_set,res)
            res.append(v)
        

            

       




    








    
       



class test:
    g=Graph()
    for i in range(1,6):
        g.addVertex(i)
    '''g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(2,3)
    g.addEdge(3,4)
    g.addEdge(4,5)
    g.addEdge(5,3)
    g.addEdge(3,1)'''

    g.addEdge(2,1)
    g.addEdge(2,3)
    g.addEdge(4,3)
    g.addEdge(5,4)
    




    g.print()
    g.dfs(3)
    print('*************** dfs traversal over*******************')
    g.bfs(3)
    print('*************** bfs traversal over*******************')

    visited_set=set()
    q=[]
    q.append(3)
    g.bfs_recur(q,visited_set)
    print('*************** bfs traversal over with recursion*******************')

    res=[]
    visited_set=set()
    g.topsort(5,visited_set,res)
    print('topological order is ',res)






