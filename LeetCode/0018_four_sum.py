'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

from functools import reduce
class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        length = len(nums)
        if length<4:
            return res
        nums.sort()
        for i in range(length-3):
            for j in range(i+1, length-2):
                l, r = j+1, length-1
                while l<r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s==target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif s<target:
                        l += 1
                    else:
                        r -= 1
        return reduce(lambda x,y: x if y in x else x+[y], res, [])

if __name__ == '__main__':
    nums = [1,0,-1,0,-2,2,4]
    print(nums)
    target = 0
    solution = Solution()
    res = solution.fourSum(nums, target)
    print(res)
