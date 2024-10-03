class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        print(s);
        print(s.split());
        list = s.split();
        word = list[-1];
        return len(word);