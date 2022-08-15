class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        max_len = 0
        l = 0
        for c in s:
            while(c in substring):
                substring.remove(s[l])
                l +=1
            substring.add(c)
            max_len = max(max_len, len(substring))
        return max_len
        
                