class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 시간복잡도: digits의 길이에 대해 O(n)
        # 공간복잡도: O(1)
        for i in reversed(range(len(digits))):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits