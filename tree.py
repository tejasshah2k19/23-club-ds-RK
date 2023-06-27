class Node:
    def __init__(self):
        self.data = 0
        self.left = None 
        self.right = None 



root = None 


root = Node() 
root.data = int(input("Enter data"))

tmp = Node()
root.left = tmp 
tmp.data = int(input("Enter data"))



tmp = Node()
root.right = tmp 
tmp.data = int(input("Enter data"))


print(root.data)
print(root.left.data)
print(root.right.data)

