class Solution:
    def countAndSay(self, n: int) -> str:
        # 시간복잡도: 재귀호출 수를 n, 문자열 길이를 m으로 했을 때 O(n * m)
        # 공간복잡도: O(n)
        def recursion(string):
            count = 0
            temp = string[0]
            result = ""
            for char in string:
                if char == temp:
                    count += 1
                else:
                    result += str(count) + temp
                    count = 1
                    temp = char
            result += str(count) + temp
            return result

        if n == 1:
            return "1"
        return recursion(self.countAndSay(n - 1))
        