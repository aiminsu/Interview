"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        length = len(s)
        if length==0:
            return True
        if length%2==1:
            return False
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()','').replace('[]','').replace('{}','')
        if s=='':
            return True
        else:
            return False

if __name__ == '__main__':
    s = '{[([])]}'
    solution = Solution()
    print(solution.isValid(s))
