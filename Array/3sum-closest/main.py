class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        nums.sort()
        n = len(nums)
        d = 100000
        sol = 0
        
        for i in range(n-2):
            l, r = i+1, n-1

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                x = abs(target - sum)
                
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    return sum
                
                if x < d:
                    d = x
                    sol = sum
                
        return sol
             
