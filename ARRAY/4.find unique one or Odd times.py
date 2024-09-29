# def unique(a):
#     i=0
#     cou=0
#     while(i<len(a)):
#         cou^=a[i]
#         i+=1
#     return cou

def unique(a):
    i=0
    while(i<len(a)):
        if(a.count(a[i])!=2):
            return a[i]
        i+=1

a=[3,2,3,4,5,5,2,6,8,6,8]
print(unique(a))
