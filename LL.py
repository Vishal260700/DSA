"""
Zig Zag Traversal of LL as per rule - a < b > c < d > e < f for abcdef LL
"""
def zigzag(self, head_node):
    # a < b > c < d > e < f
    Flag = True
    currNode = head_node
    while(currNode.next):
        if(Flag):
            if(currNode.data >= currNode.next.data):
                currNode.data, currNode.next.data = currNode.next.data, currNode.data
        else:
            if(currNode.data <= currNode.next.data):
                currNode.data, currNode.next.data = currNode.next.data, currNode.data
        Flag = not Flag
        currNode = currNode.next
    return head_node

"""
Function to remove duplicates from sorted linked list.
"""
def removeDuplicates(head): 
    curr = head
    while(curr.next):
        if(curr.data == curr.next.data):
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

"""
get nth node from end of LL
LOGIC :- single loop method, 2 pointers, let one reach till N then move both together
"""
def getNthFromLast(head,n):
    
    slow = head
    fast = head
    while(n):
        # not possible n > len(LL)
        if(fast is None):
            return -1
        fast = fast.next
        n -= 1
    
    while(fast):
        slow = slow.next
        fast = fast.next
    
    return slow.data