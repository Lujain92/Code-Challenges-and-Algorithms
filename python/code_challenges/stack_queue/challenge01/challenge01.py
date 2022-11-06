class Node :
    def __init__(self,value):
        self.value=value
        self.next=None
class Stack :
    def __init__(self):
        self.top=None
        self.size=0
    def push(self,value):
        node=Node(value)
        if self.top :
            node.next=self.top
        self.top=node
        self.size+=1
        
    def pop(self):
        if self.top:
            temp=self.top
            self.top=self.top.next
            self.size-=1
            return temp.value
        else:
            return("this stack is empty")
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("This stack is empty")

    def is_empty(self):
        return self.size == 0

    def get_size(self):
        return self.size
class MyQueue(object):
    '''
    Class used MyQueue that implemnet using 2 stacks
    '''

    def __init__(self):
        '''
        constrcutor that has 2 stacks the implement by list
        '''
        self.s1=Stack()
        self.s2=Stack()

        

    def push(self, x):
        """
        method used to push the element on it
        :type x: int
        :rtype: None
        """
        while self.s1 :
            self.s2.push(self.s1.pop())
        self.s1.push(x)
        while self.s2:
            self.s1.push(self.s2.pop())
       
        
        
        
        

    def pop(self):
        """
        method used to pop the last element and return it
        :rtype: int
        """

        return self.s1.pop()
    def peek(self):
        """
        method used to return the last element
        :rtype: int
        """
        
        
        return self.s1.peek()
        
        

    def empty(self):
        """
        method used to check if queue is empty or not
        :rtype: bool
        """
        return self.s1.get_size()==0
        





# q=MyQueue()
# q.push(1)
# q.push(2)
# q.push(3)
# q.push(4)
# print(q.pop())
