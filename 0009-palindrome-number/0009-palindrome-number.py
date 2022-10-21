class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_x = str(x)
        reversed_x = str(x)[::-1]
        if original_x == reversed_x:
            return True
        else: return False