class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 시간복잡도: s의 길이에 대해 O(n)
        # 공간복잡도: s의 길이에 대해 O(n)
        
        left = 0
        max_len = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len

        