# Write here the code challenge solution
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
    def remove_reverse(self,index):
        new_index=self.length-index-1
        counter=0
        # if self.head is None :
        #     self.head =self.head.next
        # else:
        prev=self.head
        while counter != new_index:
            prev=prev.next
        prev.next=prev.next.next
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
l=Linked_list()
l.push(1)
l.push(2)
l.push(33)
l.push(44)
print(l.all_in_list())
l.remove_reverse(1)
print(l.all_in_list())
