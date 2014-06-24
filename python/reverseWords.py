class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        s = s.strip()
        return ' '.join(list(reversed(s.split())))
        
