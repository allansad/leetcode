class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 시간복잡도: O(4^n)
        # 공간복잡도: O(n)
        result = []

        def backtrack(path, left, right):
            if left == 0 and right == 0:
                result.append(path)
                return
            
            if left > 0:
                backtrack(path + "(", left - 1, right)
            
            if right > left:
                backtrack(path + ")", left, right - 1)
            
        backtrack("", n, n)
        return result