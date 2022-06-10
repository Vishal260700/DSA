
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