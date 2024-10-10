# LeetCode:1832.
# Check if the Sentence Is Pangram
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

# Example 1:
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.

# Example 2:
# Input: sentence = "leetcode"
# Output: false

# Method 1: O(n) takes
def pangram(s):
    li=[0]*26
    s=s.lower()
    for i in s:
        if(li[ord(i)-ord("a")]!=1):
            li[ord(i)-ord("a")]+=1
    for i in range(len(li)):
        if(li[i]==0):
            return False
    return True

s="thequickbrownfoxjumpsoverthelazydog"
print(pangram(s))