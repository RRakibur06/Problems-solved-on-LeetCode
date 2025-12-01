class Solution(object):
    def isPalindrome(self, s):
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        processed_string = "".join(filtered_chars)
        return processed_string == processed_string[::-1]