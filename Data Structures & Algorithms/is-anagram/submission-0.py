class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letterFreq = {}
        for i in range(len(s)):
            letterFreq[s[i]] = letterFreq.get(s[i], 0) + 1
            letterFreq[t[i]] = letterFreq.get(t[i], 0) - 1
        return all(i == 0 for i in letterFreq.values())

        