
def sce_largest(arr):
    max_num = -99999
    for i in arr:
        max_num = max(i, max_num)
    sec_max = -99999
    for i in arr:
        if(i>sec_max and i != max_num):
            sec_max = i
    return sec_max

arr = list(map(int, input().split()))
print(sce_largest(arr))
