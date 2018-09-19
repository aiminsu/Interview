'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''

class Solution(object):
    def twoSum_slow(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, item1 in enumerate(nums):
            for j, item2 in enumerate(nums):
                if(i!=j and item1+item2==target):
                    return [i, j]

    def twoSum_fast(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        buf_dict = {}
        for i, item in enumerate(nums):
            if item in buf_dict.keys():
                return [buf_dict[item], i]
            else:
                buf_dict[target-item] = i


s = Solution()
print(s.twoSum_fast([3, 2, 4], 6))
print(s.twoSum_fast([3, 3, 4], 6))
