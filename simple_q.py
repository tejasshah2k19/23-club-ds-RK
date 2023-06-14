class Queue:
    def __init__(self):
        self.q = []
        self.size = 5 
        self.f = -1
        self.r = -1 
    

    def insert(self,num):
        if self.r == self.size - 1 :
            print("Q is Full")
        else:
            self.r = self.r + 1
            self.q.append(num) 
            if self.f == -1:
                self.f = 0 

    def display(self):
        print("**** ELEMENTS IN QUEUE *****")
        for i in range(self.f,self.r+1,1):
            print(self.q[i],end=" ")    
    
    def delete(self):
        if self.f == -1:
            print("Q is empty")
        else:
            print(self.q[self.f]," deleted")
            if self.f == self.r :
                self.f = -1
                self.r = -1 
            else:
                self.f = self.f + 1


queue = Queue() 


while True:
    print("############################################")
    print("1 For Insert\n2 For Delete\n3 For Display\n4 for Exit\n")
    print("Enter Choice :: ",end="")
    print("")

    choice = int(input())

    if  choice == 1:
        num = int(input("Enter number"))
        queue.insert(num) 

    elif choice == 2:
        queue.delete()

    elif choice == 3:
        queue.display()

    elif choice == 4:
        exit(0)

    else: 
        print("Invalid choice") 

