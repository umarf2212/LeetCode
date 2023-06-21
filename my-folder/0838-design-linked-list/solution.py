# 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> N
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        i = 0
        temp = self.head
        while temp and i < index:
            temp = temp.next
            i += 1
        
        if temp:
            return temp.val
        return -1

    def addAtHead(self, val: int) -> None:
        new = Node(val)

        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        
        if not self.tail:
            self.tail = new

    def addAtTail(self, val: int) -> None:
        if not self.tail:
            self.addAtHead(val)
            return

        new = Node(val)
        self.tail.next = new
        self.tail = new


    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return

        if not self.head:
            return
        
        i = 0
        temp = self.head
        prev = None
        while temp and i < index:
            prev = temp
            temp = temp.next
            i += 1

        if not temp and i == index:
            self.addAtTail(val)
            return
        
        new = Node(val)
        prev.next = new
        new.next = temp

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return

        # remove head
        if index == 0:
            self.head = self.head.next
            return
        
        i = 0
        temp = self.head
        prev = None
        while temp and i < index:
            prev = temp
            temp = temp.next
            i += 1
        
        # remove tail
        if temp == self.tail and i == index:
            prev.next = None
            self.tail = prev
            return

        if prev and temp:
            prev.next = temp.next
    
    # def printL(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.val, end= ' ')
    #         temp = temp.next
    #     print()


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
