#Leetcode:- 11
# IO: [1,8,6,2,5,4,8,3,7] ==> 49..(min(8,7)*dis(8,7))

def most_water(height):
    left=0
    right= len(height)-1
    max_volum=0
    while(left<right):
        curent_volum=(min(height[right],height[left]))*(right-left)
        max_volum=max(max_volum,curent_volum)
        if(height[left]>height[right]):
            right-=1
        else:
            left+=1
    return max_volum


arr=[1,8,6,2,5,4,8,3,7]
print(most_water(arr))