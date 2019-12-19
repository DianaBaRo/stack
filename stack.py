# Stacks are abstract data types
# Basic operations: pop(), push() and peek()
# LIFO structure: last in first out, with the pop operation
# An stack can be easily implemented either with arrays or linked lists.

# Push operation in O(1), constant time complexity
# pop operation, LIFO, last in first out. Takes O(1), constant time complexity.
# peek() return the value of the last item without removing it.

# Applications:
  # In stack-oriented programming languages.
  # Graph algorithms
  # Finding Euler-cycles in a graph
  # Finding strongly connected components in a graph

# We have two types of memory:
  # Stack memory:

        # Stack memory is a special region of the memory in the RAM.
        # A call stack is an abstract data type that store info about the active subroutines / methods / fucntions of a computer program
        # Local variables: they are pushed on the stack, after function returns the are popped, lost.
        # Stack memory is limited, it is inside the RAM, the random access memory, and this one is quite limited.
        # Fast access
        # space is managed efficiently by CPU
        #Variables cannot be resized

  # Heap memory

        # Stored in the RAM memory too
        # It is a region of memory that is not managed automatically for you.
        # This is a large region of memory // unlike stack memory
        # We have to deadlocate these memory chunks, because it is no managed automatically, if not memory leak.
        # Slower because of the pointers.
        # Java, reference types and objects are on the heap.
        # Slow access
        # Memory may be fragmented
        # Variables can be resized

# Stack and recursion
  # Recursive methods can be handy in DFS, traversing a binary search tree, looking for an item in a linked list...
  # All the recursive algorithms can be transformed into a simple method with stacks.
  # If we use recursion, the OS will use stacks anyway.

# Stack implementation:

class Stack:
    
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []
    
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        data = self.stack[-1]
        return data

    def sizeStack(self):
        return len(self.stack)


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

print(stack.sizeStack())

print("Popped ", stack.pop())
print("Popped ", stack.pop())
print(stack.sizeStack())
print("Peeked: ", stack.peek())
print(stack.sizeStack())