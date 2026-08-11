class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for ch in s:
            if ch.isalnum():
                res += ch
        res = res.lower()
        return res == res[::-1]
        