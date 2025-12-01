from collections import Counter

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = Counter(s)  
        for i, x in enumerate(s):
            if freq[x] == 1:
                return i
        return -1
