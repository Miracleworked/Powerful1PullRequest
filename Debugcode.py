#Broken code
def lone_sum(a, b, c):
    if a >= b:
        return c
    elif a == c:
        return b
    elif b == c:
        return a
    elif a == b and a == c and b == c:
        return 0
    else:
        return a+b+c

def lone_sum(a, b, c):     #definiton lone_sum 
    if a == b and a == c, and b == c:     #moved this from an elif statement to the if statement
        return 0
    elif a >= b:           #elif a greater than or equal to b, return value of c
        return c
    elif b == c:           #elif b is equal to c, return value of a
        return a
    elif a == c:           #elif a is equal to c, return value of c
        return c
    else:
        return a+b+c       #else if elif are false return value of a, b and c
print(lone_sum(3, 5, 7))    #Entered in values for the integers
15                         #Return value of a, b, and c

Process finished with exit code 0
