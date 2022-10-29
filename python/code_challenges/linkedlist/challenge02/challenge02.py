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
    has a constructor with head value,length and tail value 
    and a push method
    and allinlist method
    '''
    def __init__(self) :
        '''
        constrctor to create an attribute called head,tail,length
        '''
        self.head= None
        self.tail=None
        self.length=0
    def push (self,value):
        '''
        method push used for add a new node at a tail
        input value:int
        output:None
        '''
        node=Node(value)
       
        if self.head is None :
            self.head =node
        
            
        else:
            current=self.head
            while current.next is not None:
                current=current.next

            current.next=node 
        self.length+=1
        
    def middle(self):
        '''
        method called middle used to find the middle node in the linklist and return it
        input:
        output:node
        '''
        if self.head==None :
            return None

        index=self.length//2
        counter=0
        current=self.head
        while counter != index:
            current=current.next
            counter+=1
        return current
    def from_middle_in_list (self):
        '''
        method all_in_list used to print the  nodes in a list that start from middle one
        input :
        output:list[int]
        
        '''
        l=[]
        if self.head is None:
            print("The linked list is empty")
        else:
            current = self.middle()
            while current is not None:
                l.append(current.value)
                current = current.next
            return l


#  index=self.length//2
#         l=[]
#         mylist=self.all_in_list()
#         for x in range(index,self.length):
#             l.append(mylist[x])
#         return l 
l=Linked_list()
l.push(1)
l.push(2)
# l.push(3)
# l.push(4)
# l.push(5)
print(l.middle())
print(l.from_middle_in_list())