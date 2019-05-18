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


#=================================================
#Fixing Debug code by sam lian
def lone_sum(a, b, c): 
    if a == b and a == c and b == c: # I add 2 operator 
        return 0 # the cgange I mage it return 0 
    elif a >= b: # Add code line instead two equal I change to a >= 0.
        return c # the change I mage it I return c
    elif b == c:
        return a
    elif a == c: # In this instead  line 3 equal line i put two equal of elif a == c: and I reutun C
     return c
    else:
        return a+b+c
print(lone_sum(1,2,3))#Out put 
# Add the number to print and I indent some code it work 
#I Debuge you code and I fixing some line 
# Tank to you Powerful1 
