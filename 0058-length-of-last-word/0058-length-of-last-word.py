class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s_arr = s.strip().split(" ")
        return len(s_arr[-1])