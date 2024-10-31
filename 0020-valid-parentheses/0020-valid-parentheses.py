class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False

        bracket_que = []
        
        for char in s:
            if char == "(" or char == "{" or char == "[":
                bracket_que.append(char)
            elif char == ")" or char == "]" or char == "}":
                if len(bracket_que) == 0:
                    return False
                comparison = bracket_que.pop()

                if char == ")":
                    if comparison != "(":
                        return False
                if char == "]":
                    if comparison != "[":
                        return False
                if char == "}":
                    if comparison != "{":
                        return False
        if len(bracket_que) != 0:
            return False

        return True
            


        