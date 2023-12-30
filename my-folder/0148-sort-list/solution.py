# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Merge Sort - divide and conquer

        # 1. Divide 
        # 2. Merge

        # 4 -> 2 -> 1 -> 3
        # 4 -> 2 -> 1 -> 3 -> 5

        # fast = head
        # slow = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        
        # slow is mid node
        def divide(head):
            fast = head
            slow = head
            while fast and fast.next:
                prev = slow
                slow = slow.next
                fast = fast.next.next
            
            prev.next = None
            
            return slow
        
        def MergeSort(head):
            if not head or not head.next:
                return head
            
            mid = divide(head)

            left = MergeSort(head)
            right = MergeSort(mid)

            return merge(left, right)
        
        # 1 -> 4 -> 8
        # 2 -> 3 -> 5
        
        def merge(A, B):
            if not A: return B
            if not B: return A

            small = A if A.val <= B.val else B
            big = A if A.val > B.val else B

            small.next = merge(small.next, big)
            return small
        
        return MergeSort(head)

