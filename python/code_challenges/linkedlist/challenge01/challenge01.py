class Node :
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list :
    def __init__(self) :
        self.head= None
    def push (self,node):
       
        if self.head is None :
            self.head =node
        
            
        else:
            current=self.head
            while current.next is not None:
                current=current.next

            current.next=node  
        
    def delete (self,node):
        node.value=node.next.value
        node.next=node.next.next 
        
    def all_in_list (self):
        l=[]
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                l.append(current.value)
                current = current.next
            return l

