#Broken code
def lone_sum(a, b, c):
    elif a == b and a == c and b == c:
        return 0
    if a >= b:
        return c
    elif b == c:
        return a
    elif a == c:
        return c
    else:
        return a+b+c
print(lone_sum(1,2,3))




