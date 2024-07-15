"""
https://leetcode.com/problems/create-binary-tree-from-descriptions/?envType=daily-question&envId=2024-07-15

"""

# Definition for a binary tree node.
from collections import deque 
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        self.descriptions = descriptions
        self.create_nodes()
        
        return  self._get_root_node()
    
    def create_nodes(self):
        nodes = {}
        for (parent,child,isleft) in self.descriptions : 
            #parent_node,child_node = TreeNode(), TreeNode()
            if parent not in nodes : 
                if isleft : 
                    child_node = TreeNode(val = child,left=None, 
                                            right=None)
                    parent_node  = TreeNode(val = parent,left=child_node, 
                                            right=None )
                else :
                    child_node = TreeNode(val = child,left=None, 
                                            right=None)
                    parent_node  = TreeNode(val = parent,left=None, 
                                        right=child_node )
            else : 
                parent_node = nodes[parent]
                if isleft : 
                    parent_node.left = TreeNode(val = child,left=None, 
                                            right=None)
                else : 
                    parent_node.right = TreeNode(val = child,left=None, 
                                            right=None)

            if child not in nodes : 
                child_node = TreeNode(val = child,left=None, 
                                            right=None)
            else : 
                child_node = nodes[child]

            nodes[parent] = parent_node
            nodes[child] = child_node
        self.nodes = nodes

    def _get_root_node(self) : 
        not_root_nodes = set(map(lambda x : x[1],self.descriptions))
        root_node=set(self.nodes.keys())-not_root_nodes
        root_node_value = root_node.pop()
        self.root_node = self.nodes[root_node_value]

    def get_ordered_tree(self):
        lst_tree = deque()
        lst_ordered_tree =[]
        while set(lst_tree) != {None}:
            if lst_tree : 
                value=lst_tree.popleft()
                lst_tree.append(self.nodes[value].left.val if self.nodes[value].left is not None else None)
                lst_tree.append(self.nodes[value].right.val if self.nodes[value].right is not None else None)
                lst_ordered_tree.append(value)
            else : 
                lst_tree.append(self.root_node.val)

        return lst_ordered_tree
