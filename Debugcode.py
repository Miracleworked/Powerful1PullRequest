def lone_sum(a, b, c):
    if a == b and a == c and b == c:
        return 0
    elif a >= b:
        return c
    elif b == c:
        return a
    elif a == c:
     return c
    else:
        return a+b+c
print(lone_sum(1,1,2)) # Add the number to print and I indent some code it work 
#I Debuge you code and I fixing some line 
# Tank to you Powerful1
