
"""
Complete Function isSubTree to check if S is subtree of T or not
Time complexity - O(mn) here m and n are number of nodes in respective trees
"""
def isSubTree(self, T, S):
    def solve(sourceNode, givenNode):
        
        if(givenNode is None or sourceNode is None):
            if(givenNode is None and sourceNode is None):
                return True
            return False
        
        tempRes = False
        if(sourceNode.data == givenNode.data):
            tempRes = solve(sourceNode.left, givenNode.left) and solve(sourceNode.right, givenNode.right)
        
        return solve(sourceNode.left, givenNode) or solve(sourceNode.right, givenNode) or tempRes
    
    return solve(T, S)

"""
Optimised solution - Time complexity - O(n) and space complexity - O(n)
Logic :- Get inorder and preorder traversal for both trees and they should be subset of other to be subtree in both else False
"""
def isSubTree(self, T, S):
    def getInOrderTraversal(tree):
        if(tree is None):
            return "$"
        res = getInOrderTraversal(tree.left)
        res += str(tree.data)
        res += getInOrderTraversal(tree.right)
        return res
        
    def getPreOrderTraversal(tree):
        if(tree is None):
            return "$"
        res = str(tree.data)
        res += getPreOrderTraversal(tree.left)
        res += getPreOrderTraversal(tree.right)
        return res
    
    TInOrder = getInOrderTraversal(T)
    SInOrder = getInOrderTraversal(S)
    TPreOrder = getPreOrderTraversal(T)
    SPreOrder = getPreOrderTraversal(S)
    
    if(SInOrder not in TInOrder):
        return False
    
    if(SPreOrder not in TPreOrder):
        return False
    
    return True

"""
Leaves in BT count them
"""
def countLeaves(root):
    def solve(node):
        if(node is None):
            return 0
        if(node.left is None and node.right is None):
            return 1
        return solve(node.left) + solve(node.right)
    return solve(root)

"""
Invert BT
"""
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]: 
    # base case
    if(root is None):
        return root
    
    def solve(root):
        
        if(root is None):
            return
        
        if(root.left is None and root.right is None):
            return
        
        if(root.left is None or root.right is None):
            if(root.right is None):
                root.right = root.left
                root.left = None
                solve(root.right)
                return
            else:
                root.left = root.right
                root.right = None
                solve(root.left)
                return
        
        root.left, root.right = root.right, root.left
        solve(root.left)
        solve(root.right)
        return
    
    solve(root)
    return root

## Add all elements greater then curr elem in a BST
def modify(root):
    # in place
    def solve(root, total):
        if(root is None):
            return
        
        solve(root.right, total)
        
        total[0] += root.data
        root.data = total[0]
        
        solve(root.left, total)
        
        return
    
    solve(root, [0])
    return root

## Diameter of BT
def diameter(self,root):
    self.ans = 0
    def solve(node):
        # base case
        if(node is None):
            return 0
        # hypothesis
        l = solve(node.left)
        r = solve(node.right)
        
        # choice 1
        self.ans = max(max(self.ans, l + r + 1), max(l, r) + 1)
        # choice 2
        return max(l, r) + 1
    solve(root)
    return self.ans

## Spiral order - O(N)
def findSpiral(root):
    if(root is None):
        return []
    
    lQueue = []
    rQueue = []
    res = []
    
    lQueue.append(root)
    while(len(lQueue) or len(rQueue)):
        
        while(len(lQueue)):
            qe = lQueue.pop()
            res.append(qe.data)
            if(qe.right):
                rQueue.append(qe.right)
            if(qe.left):
                rQueue.append(qe.left)
            
        while(len(rQueue)):
            qe = rQueue.pop()
            res.append(qe.data)
            if(qe.left):
                lQueue.append(qe.left)
            if(qe.right):
                lQueue.append(qe.right)
    
    return res

#Function to return the lowest common ancestor in a Binary Tree.
def lca(self,root, n1, n2):
    
    def solve(n1, n2, node):
        # base case
        if(node is None):
            return None
        
        # one of em is node then remaining one will be in the subtree somewhere so LCA found
        if(node.data == n1 or node.data == n2):
            return node
        
        left = solve(n1, n2, node.left)
        right = solve(n1, n2, node.right)
        
        if(left is None or right is None):
            # subtree has a LCA
            if(left is None):
                return right
            else:
                return left
        else:
            return node
    
    return solve(n1, n2, root)


"""
Input:
2
ab+ef*g*-
wlrb+-*
Output:
a + b - e * f * g
w * l - r + b
"""
## Construct expression tree from postfix
def constructTree(postfix):
    if(postfix == ""):
        return None
    
    def postFixToET(postfix, ptr):
        elem = postfix[ptr[0]]
        node = et(elem + " ")
        ptr[0] -= 1
        if(isOperator(elem)):
            node.right = postFixToET(postfix, ptr)
            node.left = postFixToET(postfix, ptr)
        return node
    
    postfix = list(postfix)
    return postFixToET(postfix, [len(postfix) - 1])

## evaluate Expression tree
# function should return an integer denoting the required answer
def evalTree(self, root):
    def solve(node):
        
        # value
        if(node.left is None and node.right is None):
            return int(node.data)
        
        left = solve(node.left)
        right = solve(node.right)
        
        if(node.data == "+"):
            return left + right
        elif(node.data == "*"):
            return left * right
        elif(node.data == "/"):
            if(abs(right) > abs(left)):
                return 0
            return int(left / right)
        elif(node.data == "-"):
            return left - right
        # never going to happen in ideal case of expressions
        return None
    
    return solve(root)