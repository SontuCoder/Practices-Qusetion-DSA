# Alice has collection of songs represented as a string S where 
# each character represents a song. A playlist is the substring of 
# the given string with exactly k number of songs. She wants to create 
# a playlist that contains maximum number of her favourite song 
# which is 'a'. Your task is to find and return an integer value 
# representing the maximum number of favourite songs that she 
# can get in a single playlist.

# S= "acdbaaca" , k=3
# {"acd","cdb","dba","baa","aac","aca"}
# ans: 2..("baa" or "aac")

#IO: "aabaaa" ==>3 ..(aaa)

# Method sliding window + loop: takes O(n^2)
def songs(arr,k):
    max_element=0
    a=[0]*26
    for i in arr:
        a[ord(i)-ord("a")]+=1
    max_count=0
    for i in range(len(a)):
        if(max_count<a[i]):
            max_count=a[i]
            max_element=(i+ord("a"))
    max_element=chr(max_element)
    i=0
    j=k-1
    max_c=0
    while(j<len(arr)):
        count=0
        for m in range(i,j+1):
            if(arr[m]==max_element):
                count+=1
        max_c=max(max_c,count)
        i+=1
        j+=1
    return max_c

S="acdbabca" 
k=3
print(songs(S,k))

