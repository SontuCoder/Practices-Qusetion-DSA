# 3. Longest Substring Without Repeating Characters

def longest_subbstring(s):
    char_index = {}  # Dictionary to store the latest index of each character
    rear = 0
    max_len = 0

    for front in range(len(s)):
        if s[front] in char_index and char_index[s[front]] >= rear:
            # Move the rear pointer to the right of the last occurrence of s[front]
            rear = char_index[s[front]] + 1

        # Update the latest index of the character
        char_index[s[front]] = front

        # Calculate the maximum length of substring without repeating characters
        max_len = max(max_len, front - rear + 1)

    return max_len

s = "pwwkew"
print(longest_subbstring(s))
