class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l = max(len(nums1),len(nums1))
        s = []
        if(l==len(nums1)):
            for i in range(l):
                if(nums1[i] in nums2 and (nums1[i] in s)==False):
                    x = min(nums1.count(nums1[i]), nums2.count(nums1[i]))
                    while x>0:
                        s.append(nums1[i])
                        x -= 1
            return s
        else:
            for i in range(l):
                if(nums2[i] in nums1 and (nums2[i] in s)==False):
                    x = min(nums2.count(nums2[i]), nums1.count(nums2[i]))
                    print('x : ', x)
                    while x>0:
                        s.append(nums2[i])
                        x -= 1
            return s