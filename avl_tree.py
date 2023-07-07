class Node:
    def __init__(self):
        self.data = 0
        self.left = None 
        self.right = None 
        self.height = 1

def calculateBF(root):
    if root is None:
        return 0
    lh = 0
    rh = 0 
    if root.left != None:
        lh =root.left.height  
    if root.right != None: 
        rh = root.right.height 
    return lh - rh 

def calculateHeight(root):
    lh  = 0
    rh = 0
    if root.left != None:
        lh =root.left.height  
    if root.right != None: 
        rh = root.right.height 
    return max(lh,rh)

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
    root.height  = 1+calculateHeight(root)   

    bf = calculateBF(root)
    if bf <= -2 and root.right.data < data : #-2 -3 -4 
        #right  right 
        print(root.data," RR ")
    elif bf >= 2 and root.left.data > data: #2 3 4 5 
        #left left 
        print(root.data," LL ")
    elif bf <= -2 and root.right.data  > data : 
        #right left 
        print(root.data," RL ")
    elif bf >= 2 and root.left.data < data: #2 3 4 5 
        #left right  
        print(root.data," LR ")
    
    
    return root  


def inorder(root):  #left-root-right 
    if root != None:
        inorder(root.left)
        print(root.data,"(",root.height,")",end=" ")
        inorder(root.right)

root = None



while True: 
    print("\n0 For Exit\n1 For Add\n2 Print\n3 For Delete\nEnter choice")
    choice = int(input())
    if choice == 1 :
        
        data = int(input("Enter data")) # 350 
        root = insert(root,data) #  500,350 
    elif choice == 2:
        inorder(root)
    elif choice ==  0:
        exit(0)
   