class Queue:
    def __init__(self,element):
        self.front=0
        self.rear=element-1
        self.element=element

    def isFull(self):
        return "your Queue full"

    def isEmpty(self):
        reurn "Queue is empty inserted the elements"
        
    def enqueue(self,value):
        if len(self.value)!=0:
            

#challenge 1
stack=[]
s=input()
for i in s:
    if i=="(":
        stack.append(i)
    elif i==")" and len(stack)!=0:
        stack.pop()
        

#************ Linked List ********************************
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class LinkedList:
    arr=[]
    #add an element in the beginning of the head node
    def add_ele_at_start(self,head,value):
        new_node=Node(value)
        new_node.next=head
        head=new_node
        return head

    def add_element(self,head,value):
        new_node=Node(value) #step-1
        temp=head
        while temp.next!=None: #step-2
            temp= temp.next
        temp.next=new_node  #step-3
        
    #add an elemnt in between the nodes
    def add_ele_bt(self,head,value,pos):
        new_node=Node(value)
        cur=head
        prev=None
        while pos!=0:
            prev=cur
            cur=cur.next
            pos=pos-1
        prev.next=new_node
        new_node.next=cur
            
        
    def remove_element(self): 
        temp=head
        while temp.next.next != None:
            temp= temp.next
        temp.next=None
        
    def print_list(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end="-->")
            temp= temp.next
        print()
            
    def search_element(self,value):
        pass
            
    def reverse(self,head):
        cur=head
        prev=None
        while cur!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
        return prev
    
    def addition(self,head,value):
        pass
        

obj=LinkedList()
head=Node(10)
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.add_element(head,50)
obj.add_element(head,60)
head=obj.add_ele_at_start(head,50)
obj.add_ele_bt(head,100,3)
obj.remove_element()
obj.remove_element()
obj.print_list(head)
obj.reverse(head)
obj.print_list(head)



class Node:
    def __init__(self,value):
        self.data=value
        self.next=None

        
class linkedlist:
    
    def add_element(self,head,value):
        new_node=Node(value) #step-1
        temp=head
        while temp.next!=None: #step-2
            temp= temp.next
        temp.next=new_node  #step-3
        
    def print_list(self,head):
        temp=head
        while temp!=None:
            print(temp.data,end="-->")
            temp= temp.next
        print()
        
    def half_reverse(self,head):
        first=head
        cur=head
        prev=None
        n=4
        while n!=0:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            n-=1
        first.next=cur
        return prev

oj=linkedlist()
head=Node(1)
oj.add_element(head,2)
oj.add_element(head,3)
oj.add_element(head,4)
oj.add_element(head,5)
oj.add_element(head,6)
oj.add_element(head,7)
oj.add_element(head,8)
oj.print_list(head)
oj.half_reverse(head)
oj.print_list(head)

