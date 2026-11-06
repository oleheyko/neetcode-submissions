class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_table = {}
        char_index = {}
        r = 0
        l = 0
        max_length = 0
        while r < len(s):
            hash_table[s[r]] = hash_table.get(s[r],0) + 1
            # if not valid move left until condition is satisfied
            if s[r] in char_index and char_index[s[r]] >= l:
                l = char_index[s[r]] + 1
            max_length = max(max_length, (r-l+1))
            char_index[s[r]] = r
            r += 1
        return max_length