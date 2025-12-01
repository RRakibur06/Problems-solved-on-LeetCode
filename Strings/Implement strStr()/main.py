class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        a = [[] for _ in range(123)]
        if needle in haystack:
            for i, x in enumerate(haystack):
                a[ord(x)].append(i)

        for start in a[ord(needle[0])]:
            pos = start
            found = True
            for i in range(1, len(needle)):
                pos += 1
                if pos not in a[ord(needle[i])]:
                    found = False
                    break
            if found:
                return start
        return -1

x = Solution()
print(x.strStr(haystack = "adbutsad", needle = "sad"))
