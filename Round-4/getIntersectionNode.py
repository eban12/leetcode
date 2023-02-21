# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def length(node):
            l = 0
            while node:
                l += 1
                node = node.next
            return l
        

        lenA = length(headA)
        lenB = length(headB)
        if lenB > lenA:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        
        while lenA > lenB:
            if headA == headB:
                return headA
            
            headA = headA.next
            lenA -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA
