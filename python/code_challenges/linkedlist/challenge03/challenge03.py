# Write here the code challenge solution
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
    def removeNthFromEnd(self,n):
        """
        a method used to remove a node depend on it is index but from end
        :type head: linkedlist
        :type n: int
        :rtype: linkedlist
        """
        new_index=self.length-n-1
        if new_index==self.length-1 or n > self.length or n< 0:
            return "can't"
        if n==self.length:
            removed=self.head
            self.head=self.head.next
          
            
        else:
            prev=self.head
            counter=0
            while counter != new_index:
                prev=prev.next
                counter+=1
            removed=prev.next
            prev.next=prev.next.next
          
        return self.head
        # return removed.value
    
    def all_in_list (self):
        '''
        method all_in_list used to print the whole nodes in a list
        input :
        output:list[int]
        
        '''
        l=[]
        if self.head is None:
            return l
        else:
            current = self.head
            while current is not None:
                l.append(current.value)
                current = current.next
            return l


##for me to make it as a function

# def removeNthFromEnd(head,n):
#         """
#         a function used to remove a node depend on it is index but from end
#         :type head: linkedlist
#         :type n: int
#         :rtype: linkedlist
#         """
#         temp=head
#         length=0
#         while temp:
#             temp=temp.next
#             length+=1
#         print(length)            
         
#         new_index=length-n-1
#         if new_index==length-1 or n > length or n< 0:
#             return "can't"
#         if n==length:
#             head=head.next
            
#         else:
#             prev=head
#             counter=0
#             while counter != new_index:
#                 prev=prev.next
#                 counter+=1
#             removed=prev.next
#             prev.next=prev.next.next
#            # return removed.value
#         return head


# l=Linked_list()
# l.push(1)
# l.push(2)
# l.push(33)
# l.push(44)
# print(l.all_in_list())
# print(removeNthFromEnd(l,1))
# # print(l.all_in_list())