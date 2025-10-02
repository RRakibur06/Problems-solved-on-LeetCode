class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = sorted(set(nums))
        n = len(m)
        i = 0
        for a in m:
            nums[i] = a
            i+=1
        return n