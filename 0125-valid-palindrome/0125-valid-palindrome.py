class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = [i.lower() for i in s if (i!=' ' and i.isalnum()) ]
        return ans==ans[::-1]