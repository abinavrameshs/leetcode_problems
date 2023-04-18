"""
Problem : 
https://leetcode.com/problems/intersection-of-two-linked-lists/submissions/935501902/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        :type head1, head1: ListNode
        :rtype: ListNode

        Time : O(m+n)
        Space : O(1)
        """
        # print(headA)
        # print(headB)
        nodeA = headA
        nodeB = headB
        # print(f"Print Node A")
        lenA ,lenB = 0,0

        def _get_len(node) :
            _len=0
            while node is not None : 
                _len+=1
                node = node.next
            return _len

        lenA = _get_len(node = nodeA)
        lenB = _get_len(node = nodeB)
        

        # print(f"lenA = {lenA}\nlenB = {lenB}")

        # ################## Movements 
        nodeA = headA
        nodeB = headB
        len_diff = lenA-lenB
        # A is bigger than B : reduce A to come to the length of B
        if len_diff>=0 : 
            while len_diff>0 : 
                nodeA= nodeA.next
                len_diff-=1 
        # B is bigger than A : reduce B to come to the length of A
        else : 
            len_diff = -len_diff 
            while len_diff>0 : 
                nodeB= nodeB.next
                len_diff-=1
        #print(f"Final nodeA = {nodeA}")
        #print(f"Final nodeB = {nodeB}")
        while nodeA!=nodeB : 
            nodeA = nodeA.next
            nodeB = nodeB.next

        if nodeA==nodeB : 
            return nodeA
        else: return None