from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_counter = Counter(s)
        t_counter = Counter(t)
        for key in s_counter:
            if key in t_counter:
                if s_counter[key] == t_counter[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True

        