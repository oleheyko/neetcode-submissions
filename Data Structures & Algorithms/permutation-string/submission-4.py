class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target_freq = [0]*26
        window_freq = [0]*26
        
        for i in range(len(s1)):
            idx = ord(s1[i]) - ord('a')
            target_freq[idx] += 1
        
            idx = ord(s2[i]) - ord('a')
            window_freq[idx] += 1

        if window_freq == target_freq:
            return True

        right = len(s1)
        while right < len(s2):
            window_freq[ord(s2[right]) - ord('a')] += 1 
            window_freq[ord(s2[right - len(s1)]) - ord('a')] -=1
            
            if window_freq == target_freq:
                return True
            
            right += 1
   
        return False