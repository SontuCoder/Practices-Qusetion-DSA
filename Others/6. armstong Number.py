# 153 => true ( 1^3 + 5^3 + 3^3 = 153 == 153)
# 135 => false (1^3 + 3^3 + 5^3 = 153 != 135)
# 22 => false (2^2 + 2^2 = 8 != 22)

def armstrong(n):
    digit = 0
    m=n
    while(m!=0):
        digit +=1
        m=m//10
    sum_arm = 0
    a = n
    while(n!=0):
        i = n%10
        n //=10
        sum_arm += (i**digit)
    print(sum_arm == a)

n = 135
armstrong(n)