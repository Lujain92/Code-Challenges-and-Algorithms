class Node:
    def __init__(self, value=None):
        self.value = value
    
 

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Grahp:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        
       if node1 and node2:
            edge1 = Edge(node2,weight)
            self.adj_list[node1].append(edge1)

            edge2 = Edge(node1,weight)
            self.adj_list[node2].append(edge2)