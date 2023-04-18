"""
https://leetcode.com/problems/design-browser-history/
"""
class ListNode:
    def __init__(self, url: str):
        self.url = url
        self.next = None
        self.previous = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current_node = self.tail = self.head = ListNode(homepage)
        print(f"returned None, tail = {self.tail.url}, current ={self.current_node.url} ")
        self.len = 1
    
    def print_list(self, operation, steps : None):
        """
        Time : O(n)
        Space : O(1)
        """
        print(f"# PRINTING after {operation} {steps} steps ############")
        n = self.head
        while n!=self.tail : 
            print(n.url, end = '\t')
            n=n.next
        print(self.tail.url, end = '\n')
        #print("\n")
        

    def visit(self, url: str) -> None:     
        """
        Time : O(1)
        Space : O(1)
        """
        new_visit = ListNode(url)
        self.current_node.next = new_visit
        new_visit.previous = self.current_node 
        self.tail = self.current_node = new_visit
        self.tail.next = None
        # self.print_list("visit","")
        print(f"returned None, tail = {self.tail.url}, current ={self.current_node.url}")



    def back(self, steps: int) -> str:
        """
        Time : O(n)
        Space : O(1)
        """
        initial_steps = steps
        node = self.current_node 
        while node!=self.head and steps>0 : 
            node = node.previous
            steps-=1
        self.current_node = node
        # self.print_list("back", initial_steps)
        print(f"returned {self.current_node.url}, tail = {self.tail.url}, current ={self.current_node.url}")
        return self.current_node.url
        

    def forward(self, steps: int) -> str:
        """
        Time : O(n)
        Space : O(1)
        """
        initial_steps=steps
        node = self.current_node 
        while node!=self.tail and steps>0 : 
            node = node.next 
            steps-=1
        self.current_node = node 
        # self.print_list("forward",initial_steps)
        print(f"returned {self.current_node.url}, tail = {self.tail.url}, current ={self.current_node.url}")
        return self.current_node.url

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)