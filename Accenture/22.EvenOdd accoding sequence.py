# Jack has an array A of length N. He wants to label whether the number in the array is even or odd. Your task is to help him find and return a string with labels even or odd in sequence according to which the numbers appear in the array.
# IO:[1,2,3,4,5] ==> "oddevenoddevenodd"

def get_string(arr):
    s=""
    for i in arr:
        if(i%2==0):
            s+="even"
        else:
            s+="odd"
    return s

arr=[1,2,3,4,5]
print(get_string(arr))