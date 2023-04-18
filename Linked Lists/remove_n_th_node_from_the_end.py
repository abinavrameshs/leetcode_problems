"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Time : O(n)
        Space : O(1)

        """
        # print(f"head = {head}\n n = {n}")
        # ========= GET LENGTH FIRST ===============
        node = head
        length_list = 0
        while node : 
            # print(node.val)
            # print(f"node = {node}")
            length_list+=1
            node = node.next
        print(f"length = {length_list}")
        # ========= Traverse from head to len-n ===============

        ######### If there is only 1 node or you are asked to return the last node from first
        if length_list==1 or length_list-n==0 : 
            return head.next
        else : 
        ####### If there are >2 nodes

            node = head
            i=0
            while i<length_list-n-1  : #2
                node = node.next 
                i+=1
            print(f"node after traveral = {node}")
            # we need to remove node.next 
            node_to_remove = node.next
            node_to_connect = node.next.next if node.next else None 
            print(f"node_to_remove = {node_to_remove}\n node_to_connect={node_to_connect}")
            node.next = node_to_connect
            node_to_remove.next = None
            return head
        # # print the list 
        # node = head
        # print("==After removal======")
        # while node : 
        #     print(node.val)
        #     print(f"node = {node}")
        #     length_list+=1
        #     node = node.next
            
