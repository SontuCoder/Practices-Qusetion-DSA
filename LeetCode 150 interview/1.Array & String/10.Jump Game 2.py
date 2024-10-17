#Leet Code 45

def jump(arr):
    jump_count=0
    current=0
    fastest=0

    for i in range(len(arr)-1):
        fastest=max(fastest,i+arr[i])
        if(i==current):
            jump_count+=1
            current=fastest
    return jump_count
    
arr=[2,3,1,1,3]
print(jump(arr))