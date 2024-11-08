from collections import Counter
from typing import List

def findSubstring(s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    # Length of each word and total length of concatenated words
    word_len = len(words[0])
    total_len = word_len * len(words)

    # Create a word count dictionary from the words list
    word_count = Counter(words)
    result = []

    # Loop through the string with an offset up to the length of a word
    for i in range(word_len):
        left = i
        right = i
        seen = Counter()

        # Slide the window across `s`
        while right + word_len <= len(s):
            # Get the current word from the string
            word = s[right:right + word_len]
            right += word_len
            print(word)
            # Check if it's a valid word
            if word in word_count:
                seen[word] += 1

                # If there are more occurrences than in word_count, shift the window
                while seen[word] > word_count[word]:
                    seen[s[left:left + word_len]] -= 1
                    left += word_len

                # If the window size matches the total length, record the start index
                if right - left == total_len:
                    result.append(left)
            else:
                # Reset the window if the word is not in `words`
                seen.clear()
                left = right

    return result

# Example usage
s = "barfoofoobarthefoobarman"
words = ["bar", "foo", "the"]
print(findSubstring(s, words))  # Expected output: [6, 9, 12]
