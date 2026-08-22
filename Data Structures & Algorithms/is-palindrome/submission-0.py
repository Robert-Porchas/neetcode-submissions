class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        stack = []
        midpoint = len(s) // 2
        for i in range(len(s)):
            if i < midpoint:
                stack.append(s[i])
            elif i >= (midpoint + (1 if len(s) % 2 != 0 else 0)):
                if s[i] != stack.pop():
                    return False
        return True