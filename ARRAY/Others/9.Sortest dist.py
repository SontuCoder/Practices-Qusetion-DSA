#IO: [2,1,3,5,2,5,66,5,3,3,1,2,4,3], x=2,y=3 
#OP: 2

def sort_dist(arr,a,b):
    global_dist=999999
    cur_dist=0
    c=min(arr.index(a),arr.index(b))
    var=arr[c]
    for i in range(c,len(arr)):
        if(arr[i]==a and var==b):
            var=a
            global_dist=min(global_dist,cur_dist)
            cur_dist=0
        if(arr[i]==b and var==a):
            var=b
            global_dist=min(global_dist,cur_dist)
            cur_dist=0
        cur_dist+=1
    return global_dist

arr=[2,1,3,5,2,5,66,5,3,3,1,2,4,3]
print(sort_dist(arr,2,3))