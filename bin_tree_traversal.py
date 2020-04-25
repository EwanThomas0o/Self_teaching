
#A binary tree is a structure where each node has at most two children

#       root node
#        /    \
#       /      \
# left child   right child

# The depth of a node is how many nodes it is away from the root
# The dead ends of the tree are called leaves, and the height of a node is how many nodes another node is from its furthest leaf

# In a complete binary tree, every level except possibly the last, is completely filled and all nodes in the last level are as far left as possible.
# A full binary tree (sometimes referred to as a proper or plane binary tree) is a tree in which every node has either 0 or 2 children.

#----- Implementation -----#

#Defining a queue class, used later on for level-order traversal (line 167)
class Queue(object):
  def __init__(self):
    self.items = []    #Is just an empty array

  def enqueue(self, item):
    self.items.insert(0, item)   #insert an item at the 0th index (end of the queue)

  def dequeue(self):
    if not self.is_empty():      #remove the last element 
      return self.items.pop()

  def is_empty(self):
    return len(self.items) == 0   #empty checker

  def peek(self):
    if not self.is_empty():         #Since queues are first-in, first out the next item out is the last item in the list
      return self.items[-1].value

  def __len__(self):    #size of queue
    return self.size()

  def size(self):
    return len(self.items)

class node(object):
    def __init__(self,value):  #Creates an object called node to be used in tree
        self.value = value
        self.left = None
        self.right = None



class binar_tree(object):
    def __init__(self,root):  #creates a tree as an object, must start tree with root so we call node and input a val to start.
        self.root = node(root) 

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)            

        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False


    def preorder_print(self, start, traversal):  #Start is current node, traversal is the string that records visited nodes
        if start:   #Checking to see if starting node is null
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):  #Start is current node, traversal is the string that records visited nodes
        if start:   #Checking to see if starting node is null
            traversal = self.preorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):  #Start is current node, traversal is the string that records visited nodes
        if start:   #Checking to see if starting node is null
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):  #Theres also a way to do this in reverse! Instead of pushing into a string, push into a stack then pop off things from the stack!
        if start is None:               #   First-in last out nature of stack means that the levelorder print will now be in reverse! Stacks are great for reversing things!
            return

        q = Queue()
        q.enqueue(start)  #Add first node to the queue, gotta start somewhere!

        traversal = ""

        while len(q) > 0:
            traversal += str(q.peek()) + "-"
            node = q.dequeue()  #removes last element in list from the q (first-in first-out)

            if node.left:
                q.enqueue(node.left)  #gets value from left
            if node.right:
                q.enqueue(node.right)

        return traversal



                                        #            ___1___
tree = binar_tree(1)                    #          /        \
tree.root.left = node(2)                #         /          \
tree.root.right = node(3)               #        /            \
tree.root.left.left = node(4)           #       2              3 
tree.root.left.right = node(5)          #     /   \          /   \
tree.root.right.left = node(6)          #    /     \        /     \
tree.root.right.right = node(7)         #   4       5      6       7


#now that we've built our tree lets traverse it

#----- Traversal -----#

#   Traversal is the process of visitin each node in a tree data structure,exactly once. Unlike linear linked lists which can be accessed in a logical fashion, bin trees can be
# accessed in many different ways.

#   Can be traversed depth-first or bredth-first
#   Some depth-first traversal methods are in-order, pre-order and post-order.

#----- Pre-order Traversal -----#

# 1. Check if current node is empty or null
# 2. Display data or current node
# 3. Traverse left subtree by calling pre-order method recursively
# 4. Traverse right subtree by calling pre-order method 

# visit, left, right

#----- In-order Traversal -----#

# 1. Check if current node is empty or null
# 2. Traverse left subtree by calling pre-order method recursively
# 3. Display data or current node
# 4. Traverse right subtree by calling pre-order method 

#  left, visit, right


#----- post-order Traversal -----#

# 1. Check if current node is empty or null
# 2. Traverse left subtree by calling pre-order method recursively
# 3. Traverse right subtree by calling pre-order method
# 4. Display data or current node

#left, right, visit

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("levelorder"))



#----- Level-Order traversal -----#

# This is a type of bredth-first traversal. instead of using a stack we use a queuing system instead. We have to define a class called Queue (opposite of stack)
#   as first index is last in the queue and last index is first in the queue (cyle via A[-1])
#   We basically look at each level and look at what values are one each level

#            ___1___             Level 1
#          /        \
#         /          \
#        /            \
#       2              3         Level 2
#     /   \       
#    /     \        
#   4       5                    Level 3

# we start at Level 1: We add 1 to the queue
#                      Then we remove from q and add it to the traversal string

# we move on to Level 2: We add 2 and 3 (the children of the node we de-"q"ed) the to the q
#                      : we remove 2 from the q and then add 4 and 5 to the q (as they are the children of 2 which we just de-"q"ed)

#  Level 3: We remove 3 and because it has no children we can then simply remove 4 and 5 too, This will make Traversal = 12345



















