# Peak element be the greater then neighbors. In corner we concider one neighbor.
#IO:- [10,20,15,2,23,90,67]
#OP:-[20,90]


def peak(arr):
    a=[]
    for i in range(len(arr)):
        if(i==0 and arr[i]>arr[i+1]):
            a.append(arr[i])
        elif(i==(len(arr)-1) and arr[i-1]<arr[i]):
            a.append(arr[i])
        elif(i!=0 and i!=len(arr)-1 and arr[i]>arr[i+1] and arr[i]>arr[i-1]):
            a.append(arr[i])
    return a


arr=[10,20,15,2,23,90,67]
print(peak(arr))