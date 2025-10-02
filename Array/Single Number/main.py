class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        if(len(nums)==1):
            return nums[0]
        for i in range(len(nums)):
            if(i<len(nums)-1 and nums[i]!=nums[i+1] and nums[i] != nums[i-1]):
                return nums[i]
            elif(i==len(nums)-1 and nums[i] != nums[i-1]):
                return nums[i]