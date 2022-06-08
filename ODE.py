import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import matplotlib
matplotlib.use('tkagg')
#parms
r=0.0025
M=270000 #carrying capacity of the system
#please note that T, minimum initial population needed to take hold
#is imbedded inside the function
params = (r, M)
y0 = [1]        #start with one bacteria
t = np.linspace(0, 500, num=1000)

#the code below defines the function that is to be integrated
def sim(variables, t, params):
    P = variables[0]
    r = params[0]
    M = params[1]
    dPdt = -r*P*(1-(P/500))*(1-(P/M))
    return ([dPdt])
#y is really our variable P
y = odeint(sim, y0, t, args=(params,))

plt.plot(t, y[:, 0])
plt.xlabel("Time")
plt.ylabel("Bacteria")
plt.show()
