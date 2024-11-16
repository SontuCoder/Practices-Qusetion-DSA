# 12345 => 0
# 1213422 => 2 (1,2)

def count_reapeat(n):
    count = 0
    li = [0]*10
    while(n!=0):
        a = n%10
        li[a] += 1
        n //=10
    for i in range(10):
        if(li[i]>1):
            count+=1
    return count


arr = int(input())
print(count_reapeat(arr))