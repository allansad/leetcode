class Solution:
    # 시간복잡도: 조합의 길이 k, 조합의 개수 n에 대해 O(n x k)
    # 공간복잡도: 조합의 길이 k, 조합의 개수 n에 대해 O(n x k)
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        temp = []

        def backtracking(s):
            if len(temp) == k:
                res.append(temp[:])
                return
            
            for i in range(s, n + 1):
                temp.append(i)
                backtracking(i + 1)
                temp.pop()

        backtracking(1)

        return res