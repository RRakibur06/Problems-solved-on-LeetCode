class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''.join(str(x) for x in digits)
        x = (int(s)+1)
        res = list(map(int, str(x)))
        return res