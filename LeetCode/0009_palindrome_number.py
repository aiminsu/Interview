'''
Determine whether an integer is a palindrome. An integer is a palindrome when
it reads the same backward as forward.

Example 1:
    Input: 121
    Output: true

Example 2:
    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it
    becomes 121-. Therefore it is not a palindrome.

Example 3:
    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
'''


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    x1 = 121
    print('input:', x1)
    print('output', s.isPalindrome(x1))
    x2 = -121
    print('input:', x2)
    print('output', s.isPalindrome(x2))
    x3 = 10
    print('input:', x3)
    print('output', s.isPalindrome(x3))
