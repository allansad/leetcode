class Solution:
    def climbStairs(self, n: int) -> int:
        # 시간복잡도: n의 크기에 대해 O(n)
        # 공간복잡도: n의 크기만큼 재귀하므로 n의 크기에 대해 O(n)

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 2) + self.climbStairs(n - 1)
            