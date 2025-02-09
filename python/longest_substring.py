"""
This program calculates the length of the longest substring 
without repeating characters in a given string.
"""

class LSubstring:
    @staticmethod
    def substring(s):
        left = max_length = 0
        last_seen = {}

        for r, c in enumerate(s):
            if c in last_seen and last_seen[c] >= left:
                left = last_seen[c] + 1

            max_length = max(max_length, r - left + 1)
            last_seen[c] = r  # Store the last seen index of the character
            print(last_seen[c])
            print(" ")
        return max_length

# Example usage
s = "abcabcbb"
print(LSubstring.substring(s))  
