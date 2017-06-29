import matplotlib.pyplot as plt
import numpy as np

with open("PE_experiment_BNT-7BT") as f:
    lines = f.readlines()
    x = [line.split()[0] for line in lines]
    y = [line.split()[1] for line in lines]

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y,"+r")
ax.set_xlabel('Electric Field (kV/mm)')
ax.set_ylabel('Polarization (C/m$\mathregular{^2}$)')

plt.show()
