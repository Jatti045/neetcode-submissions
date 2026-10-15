class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
            
        charSet = set()

        left = 0
        right = 0

        longest = 0
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            longest = max(longest, right - left)
            charSet.add(s[right])
            right += 1
        return longest + 1
