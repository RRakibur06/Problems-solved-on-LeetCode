class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        temp = nums[:]  # copy original

        for i in range(n):
            nums[(i + k) % n] = temp[i]