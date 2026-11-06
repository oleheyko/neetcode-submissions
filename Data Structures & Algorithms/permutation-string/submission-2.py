class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        target_freq = [0]*26
        for ch in s1:
            idx = ord(ch) - ord('a')
            target_freq[idx] += 1
        right = len(s1)
        while right <= len(s2):
            freq = [0]*26
            left = right - len(s1)
            for ch in s2[left:right]:
                idx = ord(ch) - ord('a')
                freq[idx] += 1
            if freq == target_freq:
                return True
            right += 1
        return False