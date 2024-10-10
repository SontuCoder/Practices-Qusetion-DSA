# In this approach, we treat every character
# (or every pair of consecutive characters for
# even-length palindromes) as the center of a 
# potential palindrome and expand outward while 
# checking if the substring is still a palindrome.

#IO: "babad" ==> "aba"
#IO: "cbcbbcc" ==> "cbbc"

# Method 1: O(N^2) time

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def longest_palindromic_substring(s):
    if len(s) == 0:
        return ""
    start, end = 0, 0
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
    
    return s[start:end + 1]

# Example usage
s = "cbcbbcc"
print("Longest Palindromic Substring:", longest_palindromic_substring(s))
