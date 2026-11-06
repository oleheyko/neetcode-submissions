class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        for s in strs:
            freq = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                freq[idx] += 1
            key = tuple(freq)
            group_dict.setdefault(key, []).append(s)
        return list(group_dict.values())