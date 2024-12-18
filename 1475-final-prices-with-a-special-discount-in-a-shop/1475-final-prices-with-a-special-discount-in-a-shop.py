class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 시간복잡도: prices의 길이에 대해 O(n^2)
        # 공간복잡도: O(1)
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    prices[i] -= prices[j]
                    break
        return prices