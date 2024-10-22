# Leet Code:- 134

def calculate_each(gas,cost):
    for i in range(len(gas)):
        if(gas[i]<cost[i]):
            continue
        else:
            if(gas_sufficient_ornot(gas,cost,i)):
                return i
    return -1

gas=[5,1,2,3,4]
cost=[4,4,1,5,1]

print(calculate_each(gas,cost))
