class Node:
    def __init__(self):
        self.data = 0 
        self.next = None  


head = None 

 
while True:
    print("1 For add\n2 For List")
    print("3 For addBeg")
    print("4 For InsertAfter")
    print("5 For DeleteLast")
    print("6 For DeleteBeg")
    print("7 For Sort")
    print("\nEnter Choice")
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
    elif choice == 3:
        print("enter number")
        num = int(input()) # 40 
        tmp = Node() # create node 
        tmp.data = num # set data into node 
        tmp.next = head # assign head address in next of tmp
        head = tmp # move head to tmp  
    elif choice == 4:
        print("Enter source and new Num")
        source = int(input())
        num = int(input())

        tmp = Node() 
        tmp.data = num 

        p = head 

        while p.data != source:
            p=p.next  

        q = p.next 
        p.next = tmp
        tmp.next = q 
    
    elif choice == 5:
        p = head 

        while p.next != None :
            p = p.next 

        q = head 
        while q.next != p :
            q = q.next 

        q.next = None     
        del p 
    elif choice == 7:    
        p= head 
        while p!= None:
            q = head 
            while q.next != None:
                t = q.next
                if q.data > t.data :
                    tmp = q.data 
                    q.data = t.data 
                    t.data = tmp
                q =q.next 
            p=p.next 

    elif choice == 0:
            exit(0)