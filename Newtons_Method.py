#this program approximates the root (exact 0), of a function
# in this example i have it set up to approximate the value of pi by using the function sin(x), which crosses the x axis every pi
import math
def FofX(x):
    y = math.sin(x)
    return y
        
def DXofX(x):
    y = math.cos(x) #derivative of FofX equall to Y
    return y

def approx(x0,xn):
    xn = x0 - (FofX(x0)/DXofX(x0))
    #print(xn)
    if abs(x0-xn)>.000001:
        xn = approx(xn,x0)
    return xn


print("the funtion returns 0 when x is equal to:")
print(approx(3,0))