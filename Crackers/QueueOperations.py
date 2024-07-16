class Deque:  
    def __init__(self, size):  
        self.size = size  
        self.queue = []  

    def pushFront(self, x):  
        if len(self.queue) < self.size:  
            self.queue.insert(0, x)  
            return True  
        else:  
            return False  

    def pushRear(self, x):  
        if len(self.queue) < self.size:  
            self.queue.append(x)  
            return True  
        else:  
            return False  

    def popFront(self):  
        if not self.isEmpty():  
            return self.queue.pop(0)  
        else:  
            return -1  

    def popRear(self):  
        if not self.isEmpty():  
            return self.queue.pop()  
        else:  
            return -1  

    def getFront(self):  
        if not self.isEmpty():  
            return self.queue[0]  
        else:  
            return -1  

    def getRear(self):  
        if not self.isEmpty():  
            return self.queue[-1]  
        else:  
            return -1  

    def isEmpty(self):  
        return len(self.queue) == 0  

    def isFull(self):  
        return len(self.queue) == self.size