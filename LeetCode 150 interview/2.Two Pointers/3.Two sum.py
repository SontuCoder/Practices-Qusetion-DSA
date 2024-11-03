# Two Sum - 167

def twoSum(numbers, target):
    i=0
    j=len(numbers)-1
    li=[]
    while(i<j):
        total = numbers[i]+numbers[j]
        if(total==target):
            li.append(i+1)
            li.append(j+1)
            return li
        elif(total<target):
            i+=1
        else:
            j-=1

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers,target))