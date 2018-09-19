'''
Given a string, find the length of the longest substring without repeating characters.

Examples:
    Given "abcabcbb", the answer is "abc", which the length is 3.
    Given "bbbbb", the answer is "b", with the length of 1.
    Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must
    be a substring, "pwke" is a subsequence and not a substring.
'''


class Solution(object):
    def lenthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        buf_dict, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in buf_dict.keys():
                res = max(res, i-start)
                # be careflul here. start = buf_dict[ch]+1 doesn't work for "abba".
                start = max(start, buf_dict[ch]+1)
            buf_dict[ch] = i
        return max(res, len(s)-start)

s = "aaabbbaaadefegehile"
solution = Solution()
print(solution.lenthOfLongestSubstring(s))
