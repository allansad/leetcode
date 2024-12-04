class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 시간복잡도: s의 길이에 대해 O(n)
        # 공간복잡도: s의 길이에 대해 O(n)

        result = 0
        temp = Counter(s)
        odd_flag = False

        for i in temp:
            if temp[i] % 2 == 0:
                result += temp[i]
            else:
                odd_flag = True
                result += temp[i] - 1
        
        if odd_flag:
            return result + 1
        else:
            return result
        