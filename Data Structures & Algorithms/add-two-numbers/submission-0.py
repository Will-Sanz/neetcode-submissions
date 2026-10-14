# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            next_number = l1val + l2val + carry
            if next_number >= 10:
                carry = next_number // 10
                next_number %= 10
            else:
                carry = 0
            curr.next = ListNode(next_number)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        if carry:
            curr.next = 1
        return dummy.next
