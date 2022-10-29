class Node :
    '''
    class used to create node
    has a constrctor with value and next attributes
    '''
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list :
    '''
    Class used to create linkedlist 
    has a constructor with head vslue 
    and a push method
    and allinlist method
    '''
    def __init__(self) :
        '''
        constrctor to create an attribute called head
        '''
        self.head= None
    def push (self,node):
        '''
        method push used for add a new node at a tail
        input :node
        output:None
        '''
       
        if self.head is None :
            self.head =node
        
            
        else:
            current=self.head
            while current.next is not None:
                current=current.next

            current.next=node  
        
   
        
    def all_in_list (self):
        '''
        method all_in_list used to print the whole nodes in a list
        input :
        output:list[int]
        
        '''
        l=[]
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.head
            while current is not None:
                l.append(current.value)
                current = current.next
            return l
###solution#####
def delete (node):
    '''
    function called delete that used to delete specific node without access to a head
    input node :node
    output:None
    '''
    node.value=node.next.value
    node.next=node.next.next 