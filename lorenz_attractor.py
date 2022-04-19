import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



#Setting up inital conditions.
# sigma, beta, rho = 12, 1.667, 18 ## First set of values

# sigma, rho,beta = 1.5, 39, 0.42 ## Second set of values

sigma, rho,beta = 11, 29, 8/3 

a_0, b_0, c_0 = 1, 1, 1

#max time value T
T = 100
n = 10000

def lorenz(t, X, sigma, rho, beta): #providing the order differential eqautions (ODE)
    
    a, b, c = X
    da = -sigma*(a - b)
    db = rho*a - b - a*c
    dc = -beta*c + a*b
    return da, db, dc


soln = solve_ivp(lorenz, (0, T), (a_0, b_0, c_0), args=(sigma, rho, beta),
                 dense_output=True)

t = np.linspace(0, T, n)
x, y, z = soln.sol(t)

%matplotlib
fig = plt.figure()
ax = plt.axes(projection = '3d')
ax.plot3D(x,y,z, 'green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')


ax.set_axis_off()
