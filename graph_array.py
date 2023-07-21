class Graph:
    def __init__(self):
        self.edges = [] 
        self.totalVertex = 0
        self.totalEdges = 0 
        self.visited = []    
    def createGraph(self):
        print("How many Vertext you want to add")
        self.totalVertex = int(input())  # 5  {0 1 2 3 4}
        print("How mnay Edges You have in Graph")
        self.totalEdges = int(input()) #6
        for i in range(0,self.totalVertex):
            self.visited.append(False)      

    def addEdge(self,source,destination):
       self.edges.append({source:destination}) #0,3 0,1
       self.edges.append({destination:source}) 

    def printAllEdges(self):
        for i in range(0,self.totalVertex):  #5 -> 0 1 2 3 4 
            print("\n",i," connected : ")
            for edge in self.edges:
                if edge.get(i):
                    print(edge.get(i),end=",")

    def BFS(self,v): #BFS(0) BFS(1)
        queue = [] 
        count = 0
        queue.append(v) # 0  1  3 
        self.visited[v] = True 

        while len(queue) != 0 and count != self.totalVertex:
            #input("enter character")
            #print("Q =>",queue)
            v = queue.pop(0) #0 1
            count=count + 1 
            print(v)# 0 1
            for edge in self.edges:
                if edge.get(v) and self.visited[edge.get(v)] == False: #1 
                    queue.append(edge.get(v)) #1 3  2 


g = Graph()

g.createGraph()

#for 
g.addEdge(0,1)
g.addEdge(0,3)
g.addEdge(1,4)
g.addEdge(1,2)
g.addEdge(3,2)
g.addEdge(3,4)

g.printAllEdges()

print("\n")
g.BFS(0)

