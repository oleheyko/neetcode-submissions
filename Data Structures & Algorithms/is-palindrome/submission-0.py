class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = "".join(c.lower() for c in s if c.isalnum())
        print(cleaned)
        left = 0
        right = len(cleaned) - 1
        for c in cleaned:
            if right < left:
                break
            if cleaned[left] != cleaned[right]:
                print(cleaned[left])
                print(cleaned[right])
                return False
            left += 1
            right -=1
            
        return True
