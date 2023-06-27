class Node:
    def __init__(self):
        self.data = 0
        self.left = None 
        self.right = None 



def insert(root,data): # 500,350  300,350   400,350   None,350
    if root == None:
        root= Node()
        root.data = data 
        return root 
    else:
        if root.data > data : 
            root.left  = insert(root.left,data)
        else:
            root.right = insert(root.right,data)

    return root 

def inorder(root):  #left-root-right 
    if root != None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def preorder(root):  #root-left-right
    pass

def postorder(root): #left-right-root 
    pass 


root = None




while True: 
    print("\n0 For Exit\n1 For Add\n2 Print\nEnter choice")
    choice = int(input())
    if choice == 1 :
        
        data = int(input("Enter data")) # 350 
        root = insert(root,data) #  500,350 
    elif choice == 2:
        inorder(root)
    elif choice ==  0:
        exit(0)
