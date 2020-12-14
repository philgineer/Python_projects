class node:
    node_cnt = 0 # class variable
    
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.add = None
        
        self.adder()
        
        node.node_cnt += 1
        
    def adder(self):
        self.add = self.x + self.y
        
node1 = node(10, 20)
print("x: ", node1.x, "\ny: ", node1.y, "\nadd: ", node1.add, "\ncnt: ", node1.node_cnt)
node2 = node(100, 200)
print("\nx: ", node2.x, "\ny: ", node2.y, "\nadd: ", node2.add, "\ncnt: ", node2.node_cnt)