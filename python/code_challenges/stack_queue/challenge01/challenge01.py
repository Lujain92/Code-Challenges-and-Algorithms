
class MyQueue(object):
    '''
    Class used MyQueue that implemnet using 2 stacks
    '''

    def __init__(self):
        '''
        constrcutor that has 2 stacks the implement by list
        '''
        self.s1=[]
        self.s2=[]

        

    def push(self, x):
        """
        method used to push the element on it
        :type x: int
        :rtype: None
        """
        while self.s1 :
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())
       
        
        
        
        

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
        
        
        return self.s1[-1]
        
        

    def empty(self):
        """
        method used to check if queue is empty or not
        :rtype: bool
        """
        return len(self.s1)==0
        





