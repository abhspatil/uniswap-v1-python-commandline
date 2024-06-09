 
def add_liquidity(x, y, x1, y1):
    xtoy, ytox = get_curr_ratio(x, y)
    if x1 != 0:
        y1 = ytox * x1 
    else:
        x1 = xtoy * y1
    
    print("Adding Liquidity (x, y) : ", (x1, y1))
    
    return x + x1, y + y1

def swap(x, y, x1, y1):
    xtoy, ytox = get_curr_ratio(x, y)
    if x1 != 0:
        y1 = ytox * x1 
        return x + x1, y - y1
    else:
        x1 = xtoy * y1
        return x - x1, y + y1

def get_curr_ratio(x, y):
    print(f"Current running ratio: x_to_y = {x/y}, y_to_x= {y/x}")
    print(f"Current Liquidity, (x, y) = ", (x, y))
    return x/y, y/x 
 
print("Enter Initial X: ", end = "")
x = float(input())

print("Enter Initial Y: ", end = "")
y = float(input())

print(f"Current running ratio: x_to_y = {x/y}, y_to_x= {y/x}",)

while True:
    get_curr_ratio(x, y)
    print("Please Enter: 1. Add Liquidity, 2. Remove Liquidity, 3. Swap,  0. Exit : ", end = "")
    n = input()
    if n == "3":
        get_curr_ratio(x, y)
        print("enter value for x or y (any one, other will be auto calculated) " + 
        "in this format x:10 or y:0.11 :: ")
        xy = input()
        if "x" in xy:
            x, y = swap(x, y, float(xy[2:]), 0)
        else:
            x, y = swap(x, y, 0, float(xy[2:]))
    
    if n == "1":
        get_curr_ratio(x, y)
        print("Enter Liquidity value for x or y (any one, other will be auto calculated) in this "+
        "format x:10 or y:0.11 :: ")
        xy = input()
        if "x" in xy:
            x, y = add_liquidity(x, y, float(xy[2:]), 0)
        else:
            x, y = add_liquidity(x, y, 0, float(xy[2:]))
        
    if n == "0": break
      
