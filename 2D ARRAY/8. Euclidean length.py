import math

def eucli_length(s):
    ptr_row = 0
    ptr_col = 0

    for i in s:
        if(i=="N"):
            ptr_row -=1
        elif(i=="S"):
            ptr_row +=1
        elif(i=="E"):
            ptr_col+=1
        else:
            ptr_col-=1
    
    a = ((ptr_col)**2) + ((ptr_row)**2)
    return  math.sqrt(a)

s="NSN"
print(eucli_length(s))