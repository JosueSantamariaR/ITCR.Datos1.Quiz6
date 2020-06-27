class Node: 
    def __init__(self,data): 
        self.data = data 
        self.left = None
        self.right = None

    def insert(self, data):
            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Node(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Node(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data
    
    #Get the max value
def minimum(temp):
  
    if (temp.left==None):
        print(temp.data)
    else:print(temp.left.data)


def maximum(temp):
    if (temp.right==None):
        print(temp.data)
    else:print(temp.right.data)
   
    
# InOrder 
def inorder(temp): 
    if(not temp): 
        return
    inorder(temp.left) 
    print(temp.data) 
    inorder(temp.right) 

# PreOrder
def preorder(temp): 
    if not temp: 
        return      
    print(temp.data)
    preorder(temp.left) 
    preorder(temp.right)      

# PostOrder
def postorder(temp):
    if not temp:
        return
    postorder(temp.left) 
    postorder(temp.right)
    print(temp.data)

#Compruve the chlids
def delete(root,nodeDeletion): 
    treeList = [] 
    treeList.append(root) 
    while(len(treeList)): 
        temp = treeList.pop(0) 
        if temp is nodeDeletion: 
            temp = None
            return
        if temp.right: 
            if temp.right is nodeDeletion: 
                temp.right = None
                return
            else: 
                treeList.append(temp.right) 
        if temp.left: 
            if temp.left is nodeDeletion: 
                temp.left = None
                return
            else: 
                treeList.append(temp.left) 
   




def deletion(root, number): 
    if root == None : 
        return None
    if root.left == None and root.right == None: 
        if root.number == number :  
            return None
        else : 
            return root 
    nodeDeleting = None
    treeList = [] 
    treeList.append(root) 
    while(len(treeList)): 
        temp = treeList.pop(0) 
        if temp.data == number: 
            nodeDeleting = temp 
        if temp.left: 
            treeList.append(temp.left) 
        if temp.right: 
            treeList.append(temp.right) 
    
    if nodeDeleting :  

        node = temp.data 
        delete(root,temp) 
        nodeDeleting.data = node 
    return root 
   

 
root = Node(10) 
root.insert(11) 
root.insert(7) 
root.insert(12) 
root.insert(9) 
root.insert(15) 
root.insert(8) 



print("(PreOrder)The tree before the deletion:") 
preorder(root)
print()

print("(InOrder)The tree before the deletion:") 
inorder(root)
print()

print("(PostOrder)The tree before the deletion:") 
postorder(root)
print()

  

key = 11
root = deletion(root, key) 
    
print("(PreOrder)The tree after the deletion:") 
preorder(root)
print()

print("(InOrder)The tree after the deletion;") 
inorder(root) 
print()
    
print("(PostOrder)The tree after the deletion;") 
postorder(root) 
print()
    
print("Mininimun: ")
print(minimum(root))
print("Maximunm: ")
print(maximum(root))   
    
    