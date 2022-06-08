import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
#problem from kevin mooney
omega = 0.377   #angular velocity
t_f = 2*np.pi /omega    #time for one revolution

t_eval = np.linspace(0, t_f)

def equation_system(t, x):
    A0 = 3
    xprime = np.zeros(2)
    print(xprime.shape)
    # x[0] = x[1]
    #x[1] = v_x
    xprime[0] = x[1]
    xprime[1] = A0 * np.exp(-x[0])


    return xprime

tspan = (0, t_f)
z0 = (0, 0)
sol = solve_ivp(equation_system, tspan, z0, t_eval = t_eval)
print(sol)
print(sol.y.shape)
#solution object is a matrix with 2 rows and 50 columns
#first row is position (meters)  and 2nd row is velocity
print(sol.y[0, -1])     #39.42 meters is the vertical distance traveled by the particle during one revolution
z = sol.y[0,:]      #first row
v_z = sol.y[1,:]        #second row
plt.plot(sol.t, z, 'k')
plt.show()
plt.plot(sol.t, v_z, 'k')
plt.show()
###########################################################################
def equation_system(x):
    A0 = 3
    xprime = np.zeros(2)
    print(xprime.shape)
    # x[0] = x[1]
    #x[1] = v_x
    xprime[0] = x[1]
    xprime[1] = A0 * np.exp(-x[0])


    return xprime

x = np.array([5, 7])
xprime = equation_system(x)
print(f"xprime: {xprime}")

A0 = 3
xprime = np.zeros(2)
print(xprime.shape)
# x[0] = x[1]
# x[1] = v_x
xprime[0] = x[1]
xprime[1] = A0 * np.exp(-x[0])
print(f"xprime: {xprime}")

boundary = [0,0]
for n in range(10):
     ex = boundary.pop(0)
     print(f"loop: {n}, value: {ex}, {boundary}")
     #print(Add array: {boundary})
     boundary.append(array[n])
     print(f"boundary:{boundary}")