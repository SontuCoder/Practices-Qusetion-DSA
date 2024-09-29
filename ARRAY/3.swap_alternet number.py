def swap_alternet(a):
        for i in range(0,len(a),2):
            if(i+1<len(a)):
                a[i],a[i+1]=a[i+1],a[i]


a=[1,2,3,4,5,6]
print(a)
swap_alternet(a)
print(a)