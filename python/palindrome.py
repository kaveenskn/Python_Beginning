class Example:
     @staticmethod
     def palindrome(x):
          if str(x)==str(x)[::-1]:
               print("true")
          else:
               print("false")
          
             
Example.palindrome(-121)