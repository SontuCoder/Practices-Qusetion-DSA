
# IO:- [2,5,2,8,5,6,8,8] =>[8,8,8,2,2,5,5,6]

# convert arr to 2D arr where [number, frequency]
def arr_2Darr(arr):
    frequency_map = {}
    for num in arr:
        if num in frequency_map:
            frequency_map[num] += 1
        else:
            frequency_map[num] = 1
    # Convert the frequency map to a list of [number, frequency]
    return [[key, value] for key, value in frequency_map.items()]

# Re-formate arr:
def reformate(li):
    arr=[]
    for i in range(len(li)):
        for j in range(li[i][1]):
            arr.append(li[i][0])
    return arr

def sort_freq(arr):
    li=arr_2Darr(arr)
    li.sort(key = lambda x: -x[1])
    return reformate(li)

arr = [6,2,5,5,2,8,5,6,8,8]
print(sort_freq(arr))




