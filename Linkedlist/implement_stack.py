

# implement this using linkedlist

'''Python supports automatic garbage collection so deallocation of memory
is done implicitly. However to force it to deallocate each node after use,
add the following code:

    import gc         #added at the start of program
    gc.collect()     #to be added wherever memory is to be deallocated
'''


class Node:

    # Class to create nodes of linked list
    # constructor initializes node automatically
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    # head is default NULL
    def __init__(self):
        self.head = None

    # Checks if stack is empty
    def isempty(self):
        if self.head == None:
            return True
        else:
            return False

    # Method to add data to the stack
    # adds to the start of the stack
    def push(self, data):

        if self.head == None:
            self.head = Node(data)


        else:
            newnode = Node(data)
            newnode.next = self.head
            self.head = newnode

    # Remove element that is the current head (start of the stack)

    def pop(s):

        if s.isempty():
            return None


        else:

            # make head the next element
            poppedNode = s.head
            s.head = s.head.next
            poppedNode.next = None
            return poppedNode.data

    # Returns the head node data
    def peek(self):

        if self.isempty():
            return None

        else:
            return self.head.data

    # Prints out the stack
    def display(self):

        iternode = self.head
        if self.isempty():
            print("Stack Underflow")

        else:

            while (iternode != None):
                print(iternode.data, "->", end=" ")
                iternode = iternode.next
            return


# Driver code
MyStack = Stack()

MyStack.push(11)
MyStack.push(22)
MyStack.push(33)
MyStack.push(44)

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ", MyStack.peek())

# Delete top elements of stack
MyStack.pop()
MyStack.pop()

# Display stack elements
MyStack.display()

# Print top element of stack
print("\nTop element is ", MyStack.peek())

# This code is contributed by Mathew George