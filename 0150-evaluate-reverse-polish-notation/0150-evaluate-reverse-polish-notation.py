class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 시간복잡도: list의 길이에 대해 O(n)
        # 공간복잡도: list의 길이에 대해 O(n)
        stack = []

        for token in tokens:
            if token in {"+", "-", "*", "/"}:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(int(a + b))
                if token == "-":
                    stack.append(int(a - b))
                if token == "*":
                    stack.append(int(a * b))
                if token == "/":
                    stack.append(int(a / b))
            else:
                stack.append(int(token))
        
        return stack[0]