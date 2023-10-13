import cmath
import matplotlib.pyplot as plt
import numpy as np

def solveQuad(a,b,c):
    #Solve the quaratic equation
    discriminant = (b**2) - (4*a*c)

    x1 = (-b-cmath.sqrt(discriminant))/(2 * a)
    x2 = (-b + cmath.sqrt(discriminant))/(2 * a)
    #Change the format to eliminate cmath added j for imaginary numbers
    if '+0j' in str(x1):
        x1 = str(x1)
        x1 = x1.replace('+0j','')
        x1 = x1.rstrip(')')
        x1 = x1.lstrip('(')
    else:
        x1 = str(x1)
        x1 = x1.replace('j','i')
        x1 = x1.rstrip(')')
        x1 = x1.lstrip('(')

    if '+0j' in str(x2):
        x2 = str(x2)
        x2 = x2.replace('+0j','')
        x2 = x2.rstrip(')')
        x2 = x2.lstrip('(')
    else:
        x2 = str(x2)
        x2 = x2.replace('j','i')
        x2 = x2.strip(')')
        x2 = x2.lstrip('(')

    return x1, x2

#Creation of the graph using matplolib
def createGraph(a,b,c):
    
    x = np.linspace(-10,10,100)
    y = (a*x) ** 2 + (b*x) + (c)
    fig, ax = plt.subplots(figsize=(6,3), dpi = 136)
    #Changing the axes and adding arrow to get the graph to look like a math book example
    ax.spines[["left", "bottom"]].set_position(("data", 0))
    ax.spines[["top", "right"]].set_visible(False)
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(x, y)
    ax.grid(True)
    
    return fig
