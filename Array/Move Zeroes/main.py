class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i, k = 0 , 0

        while k < len(nums):
            if(nums[i]==0):
                x = nums.pop(i)
                nums.append(x)
            else:
                i += 1
            k += 1
            