# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def buildList(self, stack):
        if not stack: return
        
        newNode = ListNode(stack.pop())
        newNode.next = self.buildList(stack)
        
        return newNode
    
    def reverse(self, head):
        if not head: return
        temp = head
        # None <- 1 <- 2 <- 3 <- 4 -> None
        prev = None
        while temp:
            tempNext = temp.next
            temp.next = prev
            prev = temp
            
            temp = tempNext
        
        return prev
    
    def mergeLists(self, array, k):
        if not array: return 
        
        stack = array.popleft()
        
        if len(stack) < k:
            return self.reverse(self.buildList(stack))
        
        # 3 -> 2 -> 1 -> None
        head = self.buildList(stack)
        temp = head
        while temp.next:
            temp = temp.next
        
        #temp is now last node 3->2->[1]
        temp.next = self.mergeLists(array, k)
        
        return head
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        arr = deque([])
        
        temp = head
        stack = []
        count = 1
        while temp:
            stack.append(temp.val)
            
            if count == k:
                arr.append(stack)
                count = 0
                stack = []
            
            
            count+=1
            temp = temp.next
        
        if stack: 
            arr.append(stack)
        
        res = self.mergeLists(arr, k)
        return res
