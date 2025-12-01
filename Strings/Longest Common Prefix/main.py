class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # strs = ["flower","flow","flight"]
        str = min(strs, key=len)
        if not strs:
            return ""
        
        for i, s in enumerate(str):
            for j, m in enumerate(strs):
                if m[i] != s:
                    return str[:i]
        return str
x = Solution()
print(x.longestCommonPrefix(["flower"]))