class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self, key, val):
        newNode = Node(key, val)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        return newNode
    
    def delete(self, node):
        if not node: return

        if not node.prev and not node.next:
            self.head = None

        elif node == self.head:
            self.head = self.head.next
            self.head.prev = None

        elif node == self.tail:
            node.prev.next = None
            self.tail = node.prev

        elif node.next and node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev

        return node

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.dll = DLL()
        self.cache = {}

    # @return an integer
    def get(self, key):
        if key in self.cache:
            self.dll.delete(self.cache[key])
            self.cache[key] = self.dll.insert(key, self.cache[key].val)
            return self.cache[key].val
        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def put(self, key, value):
        if key in self.cache:
            self.dll.delete(self.cache[key])
            self.cache[key] = self.dll.insert(key, value)
            return 

        if self.size == self.capacity:
            del self.cache[self.dll.head.key]
            self.dll.delete(self.dll.head)
            self.size -= 1
        
        self.cache[key] = self.dll.insert(key, value)
        self.size += 1
        
        


