# 25 77 54 81 48 => 2 (25, 81)

def check_sqrt(n):
    i=1
    while i*i <=n:
        if(i*i==n):
            return True
        i+=1
    return False

def count_sqrt(arr):
    count = 0
    for i in arr:
        if(check_sqrt(i)):
            count+=1
    return count

arr = list(map(int,input().split()))
print(count_sqrt(arr))