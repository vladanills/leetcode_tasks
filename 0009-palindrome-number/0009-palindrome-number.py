class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        original_x = x
        reversed_x = 0
        while x:
            x,d = divmod(x,10)
            reversed_x = reversed_x*10+d
        if original_x == reversed_x:
            return True
        else: return False