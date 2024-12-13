class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 시간복잡도: digits의 길이 n에 대해 O(4^n)
        # 공간복잡도: digits의 길이 n에 대해 O(n)
        if not digits:
            return []
        temp_dict = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = [""]
        for i in digits:
            temp = []
            for j in result:
                for k in temp_dict[i]:
                    temp.append(j + k)
            result = temp

        return result