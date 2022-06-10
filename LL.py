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