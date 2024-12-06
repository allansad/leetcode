class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 시간복잡도: a의 길이 n, b의 길이 m에 대해 O(n+m)
        # 공간복잡도: a의 길이 n, b의 길이 m에 대해 O(n+m)

        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            result.append(str(total % 2))
            carry = total // 2
        return "".join(result[::-1])