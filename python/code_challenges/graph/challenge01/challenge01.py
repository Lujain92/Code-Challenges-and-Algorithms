# Write here the code challenge solution
class Graph:
    def __init__(self):
        self.adjacencyList={}
    
    def addVertex(self,vertex):
        '''
        method used to add vertex
        '''
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]
        # print(self.adjacencyList)
    
    def addEdge(self,v1,v2):
        '''
        method used to add edge
        '''
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)
        # print(self.adjacencyList)
        
   
    def breadthFirst(self,start):
        '''
        method used to return a lost contain all graph node visited
        input: node
        output:list
        '''
        queue=[start]
        result=[]
        visited={}
        visited[start]=True
        
        while len(queue):
            currentVertex=queue.pop(0)
            result.append(currentVertex)
            
            for neighbor in self.adjacencyList[currentVertex]:
                if neighbor not in visited:
                    visited[neighbor]=True
                    queue.append(neighbor)
        return result