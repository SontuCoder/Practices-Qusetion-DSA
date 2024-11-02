# 68. Text Justification

def justify(words, maxWidth):
    result = []
    i = 0
    n = len(words)

    while i < n:
        line_length = len(words[i])
        j = i + 1

        while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
            line_length += len(words[j])
            j += 1

        num_words_in_line = j - i
        total_spaces = maxWidth - line_length

        if j == n or num_words_in_line == 1:
            
            line = " ".join(words[i:j])  
            line += " " * (maxWidth - len(line))  
        else:
            
            space_between_words = total_spaces // (num_words_in_line - 1)
            extra_spaces = total_spaces % (num_words_in_line - 1)

            line = ""
            for k in range(i, j - 1):
                line += words[k]
                line += " " * (space_between_words + (1 if k - i < extra_spaces else 0))
            line += words[j - 1]  # Add the last word in the line without extra spaces

        result.append(line)
        i = j  # Move to the next group of words

    return result



words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
print(justify(words,maxWidth))
