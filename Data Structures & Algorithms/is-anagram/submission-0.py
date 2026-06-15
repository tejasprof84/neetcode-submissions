from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Returns True if the counts match exactly, otherwise False
        return Counter(s) == Counter(t)
