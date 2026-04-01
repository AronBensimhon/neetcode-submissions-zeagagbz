from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1, c2 = Counter(s), Counter(t)
        for key, value in c1.items():
            if key not in c2.keys():
                return False
            if c2[key] != value:
                return False
        return True
        