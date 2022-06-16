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

"""
Swap nodes kth and kth end elements
"""
def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:  
    first = head
    second = head
    
    curr = head
    while(k > 1 or curr.next):
        if(k > 1):
            first = first.next
        else:
            second = second.next
        curr = curr.next
        k -= 1
    
    first.val, second.val = second.val, first.val
    return head

def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    first = head
    second = head
    
    curr = head
    while(k > 1 or curr.next):
        if(k > 1):
            first = first.next
        else:
            second = second.next
        curr = curr.next
        k -= 1
    
    if(first == second):
        return None
    
    a = None
    b = None
    headRef = head
    while(headRef.next):
        if(headRef.next == first):
            a = headRef
        elif(headRef.next == second):
            b = headRef
        headRef = headRef.next
    
    if(a is not None and b is not None):
        temp = a.next
        a.next = b.next
        b.next = temp
        temp = a.next.next
        a.next.next = b.next.next
        b.next.next = temp
    
    return head

"""
Add two numbers as LL
"""
def addTwoLists(self, first, second):
    # helper funtion
    def revLL(LL):
        curr = LL
        prev = None
        while(curr):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    
    first = revLL(first)
    second = revLL(second)
    
    dummy = Node(None)
    curr = dummy
    
    carry = 0
    while(carry or first or second):
        v1 = 0 if first is None else first.data
        v2 = 0 if second is None else second.data
        
        total = v1 + v2 + carry
        carry = total//10
        digit = total%10
        curr.next = Node(digit)
        curr = curr.next
        
        first = first.next if first else None
        second = second.next if second else None
    
    return revLL(dummy.next)

"""
Check if 2 LL once contactinated are same or not
"""
# Input: L1 = [“He”, “llo”, “wor”, “ld”], 
#            L2 = [“H”, “e”, “ll”, “owo”, “r”, “ld”]
# Output: true
# Explanation: both lists makes the string of “Helloworld”.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

## Approach 1 - O(N + M) and O(N + M)
def solve(ll1, ll2):

    str1 = ""
    str2 = ""

    while(ll1):
        str1 += ll1.val
        ll1 = ll1.next

    while(ll2):
        str2 += ll2.val
        ll2 = ll2.next
    
    return str1 == str2

## Approach 2 - O(N + M) and O(1)

def solve(ll1, ll2):
    
    pt1 = 0
    pt2 = 0

    while(ll1 and ll2):
        while(pt1 < len(ll1.val) and pt2 < len(ll2.val)):
            if(ll1.val[pt1] != ll2.val[pt2]):
                return False
            pt1 += 1
            pt2 += 1


        if(pt1 == len(ll1.val)):
            pt1 = 0
            ll1 = ll1.next
        
        if(pt2 == len(ll2.val)):
            pt2 = 0
            ll2 = ll2.next
    return ll1 == None and ll2 == None