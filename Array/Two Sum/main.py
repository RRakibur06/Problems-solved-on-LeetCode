class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        x = list(enumerate(nums))
        y = sorted(x, key=lambda x: x[1])
        l, r = 0, len(nums) - 1

        while l < r:
            sum = y[l][1] + y[r][1]

            if sum == target:
                return [y[l][0], y[r][0]]
            elif sum < target:
                l += 1
            else:
                r -= 1

            
