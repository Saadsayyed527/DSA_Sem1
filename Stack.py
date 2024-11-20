class Node :
    def __init__(self ,data):
        self.data = data 
        self.next = None

class Stack :
    def __init__(self):
        self.head = None
        self.size =0
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node 
        self.size +=1 
    def pop(self):
        self.head = self.head.next 
        self.size -=1
    def top(self):
        return self.head.data
    def isempty(self):
        if(self.size == 0):
            True
        return False
    def print(self):
        current = self.head
        while current != None :
            print(current.data)
            current = current.next 
    def max(self):
        current = self.head
        max = self.head.data
        while current :
            if (current.data > max ):
                max = current.data
            current = current.next
        return max   
    def min(self):
        current = self.head
        max = self.head.data
        while current :
            if (current.data < max ):
                max = current.data
            current = current.next
        return max            
st = Stack()
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.push(5)
st.push(6)

st.pop()
# st.print()
print(st.min())
# print(st.isempty())