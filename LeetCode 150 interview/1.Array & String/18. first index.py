#  28. Find the Index of the First Occurrence in a String

def strStr( haystack, needle):
    return haystack.find(needle)


h = "hello"
n = "le"

print(strStr(h,n))