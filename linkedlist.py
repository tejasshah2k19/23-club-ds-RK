class Node:
    def __init__(self):
        self.data = 0 
        self.next = None  





head = None 

 
while True:
    print("1 For add\n2 For List\nEnter Choice")
    choice = int(input())

    if choice == 1:
        if head == None:
            head = Node() 
            head.data = int(input("Enter a number"))
            head.next = None 
        else:
            tmp = Node()
            tmp.data = int(input("Enter a number"))
            tmp.next = None 
            p = head 

            while p.next != None:
                p = p.next 
            
            p.next = tmp 
    elif choice == 2:
        p = head
        while p!=None:
            print(p.data) # 10 20 30 40
            p = p.next  # 
    elif choice == 0:
            exit(0)