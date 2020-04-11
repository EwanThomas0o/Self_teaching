#Building a singly linked list 
from numpy import *

class node:                     #Creating node class
    def __init__(self, data):
        self.data = data
        self.next = None 


class linked_list:              #Creating LL class with a head pointing to nothing i.e. empty LL
    def __init__(self):
        self.head = None

    def append(self, data):        #Puts new node at the end of the LL
        new_node = node(data)      #Creates a new node with the input as the data
        if self.head is None:      #If the LL is empty this new node becomes the head
            self.head = new_node
            return

        last_node = self.head          #This is the case for if we have a populated LL. last_node starts at the start of the LL
        while last_node.next:          #We then cyle through and while there is a next node we continue
            last_node = last_node.next #Simply saying point to same place as next
        last_node.next = new_node      #When we break out of loop i.e. were pointing to null we then change to point to new_node. new_node is now at the end of the list.

    def prepend(self, data):        #Adds a node to the beginning of the LL
        new_node = node(data)       #Simply creating a new node again
        new_node.next = self.head   #The new_node's next pointer points to the head. if A -> B -> C and prepend(C) then C -> A
        self.head = new_node        #Then we set the head as the new node!

    def insert_after_node(self, prev_node, data):  #Allows one to insert a node depending on the data of other nodes
        if not prev_node:
            print("Previous node does not exist")  #If the node specified doesn't exist then we print error message
            return
        new_node = node(data)                      #Simply creeating a new node again
        new_node.next = prev_node.next             #The new node points to the same place as the previous node does.
        prev_node.ext = new_node                   #Then we make the previous node point to the new node, thus inserting new_node after prev_node

    def delete_node(self, key):
        cur_node = self.head                    #Set the "current node" to the head node, we gotta start somewhere!
        if cur_node and cur_node.data == key:   #Check, if current node is not None & if the data of current node is the same as the key.
            self.head = cur_node.next           #set the head to the next of node (since that's where it would be pointing if cur was deleted) 
            cur_node = None                     #set current node to none, thus unlinking it from the list which == deletion.
            return                              #This whole case is for is we want to delete the head node

        prev = None                                 #pointer called prev, keeps track of previous node to the one to be deleted 
        while cur_node and cur_node.data != key:    #runs until cur_node becomes none (didnt find key) or cur_node.data = key which means we found the node to be deleted!
            prev = cur_node                         #we set prev to current node to keep track of it...
            cur_node = cur_node.next                #then we advance current to the next node.

        if cur_node is None:
            return            #Return from method as theres no node to delete, what happens when we break out of loop above bc theres no key match

        prev.next = cur_node.next  #If we broke out for the other reason then we set the previous next guy to point to the guy after current node
        cur_node = None            #we make cur_node to None, thus unlinking it from the list which == deletion.

    def delete_node_at(self, pos):
        if self.head:                       #Check to see if list is empty or not, continues if it isnt empty
            cur_node = self.head            #Initialising cur_node to the head node
            if pos == 0:                    #if pos = 0 then we basically want to delete the head node 
                self.head = cur_node.next   #we advance the head node the the 2nd node 
                cur_node = None             #then set cur node (which is at the original node to none, thus unlinking it from the list which == deletion.)
                return

            prev = None
            count = 0 
            while cur_node and count != pos:   #simple traversion of a linked list - IMPORTANT!
                prev = cur_node                #remember cur_node is at the head as defined by line 55.           
                cur_node = cur_node.next
                count += 1

            if cur_node is None: #Breaking out of method if we dont find the position i.e cur_node reached None before if founf the pos in the list
                return

            prev.next = cur_node.next  #if we broke out of the loop for the 2nd reason i.e. we found the position
            cur_node = None

    def print_list(self):
        cur_node = self.head                   #start at head

        while cur_node:                        #as long as cur_node is not None keep looping 
            print(cur_node.data)               #print the data 
            cur_node = cur_node.next           #make the current node the next one in the list 

    def list_length(self):
        cur_node = self.head            #Starting the current node at the head of the LL
        count = 0                       #Initialising some variable that keeps track of the index of the LL

        while cur_node:
            cur_node = cur_node.next    #This while loop simply iterates through the LL and tallys up the count so we can get the Length
            count += 1

        print(count)                    #This can also be done recursively!

    def list_length_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.list_length_recursive(node.next)    #I preferf doing this iteratively, it's more intuitive, although this requires less code...
                
#Test some of the attributes of the linked_list class below!

l = linked_list()
l.append('A')
l.append('B')
l.prepend('NULL')
l.print_list()
l.list_length()
l.delete_node_at(0)
l.print_list()
l.list_length()
print(l.list_length_recursive(l.head))


