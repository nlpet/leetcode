'''
Given an array of integers, return indices of the two numbers such that they add up to
a specific target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''


class Solution(object):
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        comps_of_seen = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comps_of_seen.get(comp):
                return comps_of_seen[comp] + [i]
            else:
                comps_of_seen[n] = [i]


if __name__ == '__main__':
    s = Solution()
    assert s.two_sum([1, 2, 3], 5) == [1, 2]
    assert s.two_sum([4, 7, 1, -2, 4, -9], -8) == [2, 5]
