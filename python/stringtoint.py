class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=s.strip()
        new_string=''
        sign=1
        if s.startswith('-'):
                    sign=-1
    
        for ch in n:
              if ch.isdigit():
                     new_string+=ch
              if ch.isalpha():
                     break
              if ch=='-' and ch!=n[0]:
                     break
        return(sign*int(new_string))
                     
x=Solution().myAtoi('  -042')
print(x)