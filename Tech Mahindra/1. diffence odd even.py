# Write a code to return diff between the count odd and even numbers.

#  IO1:- 8
#  IO2:- 10 20 30 40 55 60 77 83
#  OP:- -2

def diff(m,arr):
    count =0
    for i in arr:
        if i%2==0:
            count-=1
        else:
            count+=1
    return count

m=int(input())
arr = list(map(int,input().split()))
print(diff(m,arr))

