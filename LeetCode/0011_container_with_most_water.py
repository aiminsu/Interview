'''
Given n non-negative integers a1, a2, ..., an, where each represents a point
at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start, end, area = 0, len(height)-1, 0
        if len(height) == 2 and 0 in height:
            return 0
        # two pointer approach
        while start < end:
            tmp = (height[start] if height[start]<=height[end]
                    else height[end]) * (end - start)
            if tmp > area:
                area = tmp
            if height[start] >= height[end]:
                end -= 1
            else:
                start += 1
        return area


if __name__ == '__main__':
    s = Solution()
    height = [1, 2, 3, 4, 5]
    print('input:', height)
    print('output:', s.maxArea(height))

