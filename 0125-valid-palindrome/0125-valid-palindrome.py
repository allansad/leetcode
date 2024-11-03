class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        input_string = s
        for char in string.punctuation:
            input_string = input_string.replace(char, "")
        input_string = input_string.replace(" ", "").lower()
        
        return input_string == input_string[::-1]
        
