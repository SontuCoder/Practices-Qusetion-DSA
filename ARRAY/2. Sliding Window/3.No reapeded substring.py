# 3. Longest Substring Without Repeating Characters

# Given a strings, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: s "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

def length_substring(s):

    # track the largest value
    longest_val = 0

    # track left index 
    left_index = 0

    # hash map to track charecter
    hash_table = set()

    for i in range(len(s)):
        while s[i] in hash_table:
            hash_table.remove(s[left_index])
            left_index+=1
        
        hash_table.add(s[i])
        longest_val = max(longest_val,i-left_index+1)
    return longest_val

s="bbbbb"
print(length_substring(s))



