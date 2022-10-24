class Node :
    '''
    Class for creating node
    '''
    def __init__(self,value):
        self.value=value
        self.next=None

class Linked_list :
    '''
    Class the has whole method regarding the linkedlist
    '''
    def __init__(self) :
        self.head= None
        self.tail=None
        self.length=0
    def push (self,value):
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
        index=self.length//2
        l=[]
        mylist=self.all_in_list()
        for x in range(index,self.length):
            l.append(mylist[x])
        return l 

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


