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

def deleteNode(root,data): #200,175
    if root is None: 
        return root 
    
    if root.data == data :
        #0 1 child -> left  
        if root.left == None : 
            tmp = root.right 
            del root 
            return tmp
        elif root.right == None: 
            tmp = root.left 
            del root
            return tmp 
        else:
            #2 child 
            success = root.right 
            while success.left != None:
                success = success ->left 
            root.data = success.data 
            return deleteNode(root.right,success.data)
        
    elif root.data > data :
        #left 
        root.left = deleteNode(root.left,data)
    elif root.data < data :
        #right 
        root.right = deleteNode(root.right,data)
    


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
    elif choice == 3:
        data = int(input("Enter num that you want to delete"))
        deleteNode(root,data)        
