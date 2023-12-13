class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=items
        self.limit =limit

    def isEmpty(self):
        #checking if the stack is empty
        return len(self.items) ==0

    def push(self, item):
        #pushing an item onto the stack
        if len(self.items) <self.limit:
            self.items.append(item)
        else:
            return None #no action if the stack is full
                
        
    def pop(self):
        #pop an item from the stack
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
  
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
  
    
    def size(self):
    # """Get the number of items in the stack."""
        return len(self.items)

    def full(self):
     #    """Check if the stack is full."""
        return len(self.items) == self.limit


    def search(self, target):
         #"""Search for an item in the stack and return its distance from the top."""
        try:
            index = self.items[::-1].index(target)  # Reverse the items list to search from the top
            return len(self.items) - index  # Calculate distance from the top
        except ValueError:
            return None  # Return None if the item is not found