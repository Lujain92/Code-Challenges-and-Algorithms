
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
        return self.top.value
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



class Queue :
    '''
    class queue to create queue 
    and it is implemnted by 2 stack

    '''
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def enqueue(self,val):
        pushed=self.stack1.push(val)

        return pushed

    def dequeue(self):
        self.stack2.push(self.stack1.pop())
        poped=self.stack2.pop()
        return poped
    def peek(self):
        pass
    def is_empty(self):
        pass




# sta=Stack()
# sta2=Stack()

# sta.push(1)
# sta.push(2)
# sta.push(3)
# sta.push(4)

# sta2.push(sta.pop())
# sta2.push(sta.pop())
# sta2.push(sta.pop())
# sta2.push(sta.pop())
# # q= Queue()
# # print(q.enqueue(2))
# # print(q.enqueue(3))
# # print(q.enqueue(4))
# # print(q.dequeue())
# # print(q.dequeue())
# # print(q.dequeue())
# print(sta2.pop())



