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
        print(root.data,end=' ')
        if (root.right!=None):
            self.inorder(root.right)
            
    def preorder(self,right):
        print(root.data,end=' ')
        if (root.left!=None):
            self.preorder(root.left)
        if (root.right!=None):
            self.preorder(root.right)
            
    def postorder(self,left):
        if (root.left!=None):
            self.postorder(root.left)
        if (root.right!=None):
            self.postorder(root.right)
        print(root.data,end=' ')
        
    def levelorder(self,root):
        q=[]
        q.append(root)
        while len(q)!=0:
            ele=q.pop(0)
            if ele.left:
                q.append(ele.left)
            if ele.right:
                q.append(ele.right)
            print(ele.data,end=' ')

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
T.print_tree(root)
