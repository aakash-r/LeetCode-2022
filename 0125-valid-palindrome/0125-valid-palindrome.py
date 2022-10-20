class Solution:
    def isPalindrome(self, s: str) -> bool:
        return [i.lower() for i in s if (i!=' ' and i.isalnum()) ]==[i.lower() for i in s if (i!=' ' and i.isalnum()) ][::-1]
        