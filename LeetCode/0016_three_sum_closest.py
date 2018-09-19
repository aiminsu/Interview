'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = sum(nums[0:3])
        nums.sort()
        for i in range(len(nums)-2):
            l, r = i+1, len(nums)-1
            while l<r:
                s = nums[i] + nums[l] + nums[r]
                if s == target:
                    res = s
                    break
                elif s<target:
                    if abs(target-res) > abs(target-s):
                        res = s
                    l += 1
                else:
                    if abs(target-res) > abs(target-s):
                        res = s
                    r -= 1
        return res


if __name__ == '__main__':
    nums = [-1, 2, 1, -4, 1, 2, 3, 5, 7]
    target = 3
    solution = Solution()
    print(solution.threeSumClosest(nums, target))
