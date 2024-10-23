# Leet Code:- 134

def calculate_each(gas,cost):
    if(sum(gas)<sum(cost)):
        return -1
    tank=0
    res=0
    for i in range(len(gas)):
        tank+=(gas[i]-cost[i])

        if(tank<0):
            res+=i
            tank=0
    return res


gas=[5,1,2,3,4]
cost=[4,4,1,5,1]

print(calculate_each(gas,cost))
