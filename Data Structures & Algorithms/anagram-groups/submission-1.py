class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = defaultdict(list)
        for s in strs:
            freq = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                freq[idx] += 1
            key = tuple(freq)
            group_dict[key].append(s)
        return list(group_dict.values())