class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 시간복잡도: haystack의 길이 n, needle읠 길이 m에 대해 O(n * m)
        # 공간복잡도: O(1)

        if len(haystack) < len(needle):
            return -1

        for i in range(len(haystack)):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1
                