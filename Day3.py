""" 1)Double Linked List
      -> Insertion elements
      -> deletion elements
      -> traversing elements
      -> searching elements
      
    2) Trees and Types
      -> Binary trees
      -> Binary Search trees
      -> AVL trees
      -> B-Trees
      
    3) TRAVERSING
      -> in-order    left-root-right
      -> pre-order   root-left-right
      -> post order  left-right-root"""

class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        
class DoubleLinkedList:

    def add_element(self,head,value):
        new_node=Node(value) #step-1
        temp=head
        while temp.next!=None: #step-2
            temp= temp.next
            temp.prev=None
        temp.next=new_node  #step-3
        new_node.prev=temp #step-4
        
    def deletion(self,head): 
        temp=head
        while temp.next.next != None:
            temp= temp.next
        temp.next.prev=None
        temp.next=None
    def reverse(self,head):
        temp=head
        while temp.next!=None:
            temp=temp.next
        while temp:
            print("<-",temp.data,end="")
            temp=temp.prev
        print()
        
    def print_list(self,head):
        temp=head
        while temp!=None:
            print("<-",temp.data,end="->")                  
            temp= temp.next
        print()

obj=DoubleLinkedList()
head=Node(10)
obj.add_element(head,20)
obj.add_element(head,30)
obj.add_element(head,40)
obj.print_list(head)
obj.reverse(head)


#number of prime numbers in the linked list 
#Binary search trees
class Node:
    def __init__(self,value):
        self.data=value
        self.left=None
        self.right=None

class BStree:
    def add_element(self,root,value):
        new_node=Node(value)
        if new_node.data < root.data:
            if root.left!=None:
                self.add_element(root.left,value)
            else:
                root.left=new_node
        else:
            if root.right!=None:
                self.add_element(root.right,value)
            else:
                root.right=new_node
                 

    def inorder(self,root):
        if (root.left!=None):
            self.inorder(root.left)
        print(root.data)
        if (root.right!=None):
            self.inorder(root.right)
            
    def preorder(self,right):
        print(root.data)
        if (root.left!=None):
            self.preorder(root.left)
        if (root.right!=None):
            self.preorder(root.right)
            
    def postorder(self,left):
        if (root.left!=None):
            self.postorder(root.left)
        if (root.right!=None):
            self.postorder(root.right)
        print(root.data)
        
    def levelorder(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            ele=q.pop(0)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            print(ele.data)

    def height(self,root):
        if root==None:
            return -1
        
        left_height=self.height(root.left)
        right_height=self.height(root.height)
        return 1+max(left_height,root.right)
    
    def search(self,root,value):
        pass
    
    def sum(self,root):
        pass
            
    def print_tree(self,head):
        pass

T=BStree()
root=Node(10)
T.add_element(root,7)
T.add_element(root,5)
T.add_element(root,9)
T.add_element(root,40)
T.add_element(root,15)
T.add_element(root,60)
T.inorder(root)
print()
T.preorder(root)
print()
T.postorder(root)
print()
T.levelorder(root)
T.print_tree(head)
