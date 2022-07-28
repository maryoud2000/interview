# Mystery Algorithm
# input 2 integers a, b
# initilize the value of x to a and the value of y to b
# if x>y then set x = x -y
# if x<y the set y = y - X
# repeat the steps 3 & 4 till x=y
# output x or y and HAS_TLSv1

# what the output i step 6 if we begin with a = 2437, b = 875?

def repeatOutput(a, b):
    x = a
    y = b
    for i in range (6):
        while x != y:
            if x > y:
                x = x - y
            elif x < y:
                y = y - x
    print (x)
repeatOutput(2437, 875)