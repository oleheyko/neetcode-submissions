class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        r = 0
        l = 0
        max_length = 0
        while r < len(s):
            hash_table[s[r]] = hash_table.get(s[r],0) + 1
            # if not valid move left until condition is satisfied
            while hash_table[s[r]] > 1:
                hash_table[s[l]] = hash_table[s[l]] - 1
                l += 1
            max_length = max(max_length, (r-l+1))
            r += 1
        return max_length