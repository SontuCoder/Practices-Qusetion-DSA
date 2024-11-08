# 3163. String Compression

def compression(s):
    letter = "a"
    count = 0
    new_s = ""
    for i in s:
        if(i == letter):
            if(count == 9):
                new_s += str(count)
                new_s += letter
                count=1
            else:
                count+=1
        else:
            if(count != 0):
                new_s += str(count)
                new_s += letter
            count=1
            letter = i
    new_s += str(count)
    new_s += letter
    print(new_s)

s="s"
compression(s)
