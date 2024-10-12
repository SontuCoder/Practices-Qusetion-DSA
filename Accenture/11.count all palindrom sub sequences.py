# Count All palindromic subsequence in a given string.
#IO: "abcd" ==> 4 ..("a", "b", "c", "d")
# "babab" ==> 9 ..("b", "a", "b", "a", "b", "bab", "aba", "bab")


def count_palin(s,i,j):
    if(i>j):
        return 0
    if(i==j):
        return 1
    if(s[i]==s[j]):
        return 1+ count_palin(s,i,j-1)+count_palin(s,i+1,j)-count_palin(s,i+1,j-1)
    if(s[i]!=s[j]):
        return count_palin(s,i,j-1)+count_palin(s,i+1,j)-count_palin(s,i+1,j-1)
    

s="babab"
print(count_palin(s,0,len(s)-1))
