class Solution:
    @staticmethod
    def palindrome(s):
        seen_chars = []  # Renamed from 'list' to avoid conflicts
        for left in range(len(s)):
            if s[left] not in seen_chars:
                seen_chars.append(s[left])
            else:
                for right in range(left + 1, len(s) + 1):  # Iterate over possible substrings
                    if s[left:right] == s[left:right][::-1]:  # Check if substring is a palindrome
                        print(s[left:right])  # Print the found palindrome

Solution.palindrome("klolp")
