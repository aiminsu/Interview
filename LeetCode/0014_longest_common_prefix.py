'''
Write a function to find the longest common prefix string amongst an array
of strings.

If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        if not strs: return ''
        lens = [len(s) for s in strs]
        n = len(strs)
        for i in range(min(lens)):
            tmp = strs[0][i]
            for j in range(n):
                if strs[j][i] != tmp:
                    return res
            res += tmp
        return res


if __name__ == '__main__':
    s = Solution()
    strs = ['flower', 'flow', 'flight']
    print('input:', strs)
    print('output:', s.longestCommonPrefix(strs))
    strs = ['dog', 'racecar', 'car']
    print('input:', strs)
    print('output:', s.longestCommonPrefix(strs))
