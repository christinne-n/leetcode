"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 3:
Input: s = "(]"
Output: false
"""
#O(n)
class Solution: #use stack and match case function to go through each input
    def isValid(self, s: str) -> bool: 
        stack = [] 
        dict = { ')' : '(', ']' : '[', '}' : '{'} #matching pairs of parentheses
        for paren in s:
            if paren in dict:
                if not stack or stack.pop() != dict[paren]: #if stack is empty or not matching, return false
                    return False #if stack is empty or not matching, return false
            else:
                stack.append(paren) #add to stack if opening bracket
        return not stack #if stack is empty, return true
