def check(a,b,c):
    if (b > a and b < c) and (b % 3 == 0):
        return True
    else:
        return False
print(check(5,10,11))