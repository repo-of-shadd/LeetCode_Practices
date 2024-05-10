# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    carry = 0
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.helper(head)
        if self.carry == 1:
            return ListNode(1, head)
        return head


    def helper(self, current):
        if current:
            self.helper(current.next)
            current.val = current.val *2 + self.carry
            if current.val > 9:
                current.val %= 10
                self.carry = 1
            else:
                self.carry = 0