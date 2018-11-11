



def f(x,a,b,c,d):
    return a*x*x*x + b*x*x + c*x +d

 
def RaizCub(a,b,c,d):
    quase0 = 0.001
    x=0
    y = f(x,a,b,c,d) 
    x=x+quase0
    while(y>quase0):
        y = f(x,a,b,c,d) 
        x=x+quase0
    return x

def TIR(inv, p1, p2, p3):
    r =RaizCub(inv, p1, p2, p3)
    return r-1


print(TIR(-5,2,2,2 ))