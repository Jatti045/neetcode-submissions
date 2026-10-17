# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = 0

        curr = head
        while curr:
            counter += 1
            curr = curr.next

        print(counter)
        
        res = head
        for i in range(counter//2):
            res = res.next

        return res