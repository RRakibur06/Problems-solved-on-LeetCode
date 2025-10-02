class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = sorted(s)
        t1 = sorted(t)
        if s1 == t1:
            return True
        else:
            return False
        