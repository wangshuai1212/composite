import matplotlib.pyplot as plt
import numpy as np

block=40
NodeNumber=(1+block)**2

pol=np.zeros(200)
Efield=np.zeros(200)
Emax=6.0

for i in range(25):
    Efield[i]=Emax/25.0*(i+1)
    Efield[49-i]=Emax/25.0*i
    
for i in range(50):
    Efield[i+50]=-Efield[i]

for i in range(100):
    Efield[i+100]=Efield[i]



for fInd in range(200):
    filename="feap.vtk."+str(fInd).zfill(7)
    with open(filename) as f:
        flagu=1
        j=0
        for lines in f:
            if (lines[0] == 'u' and flagu):
                pol_add=0.0
                flagu=0
                continue
    
            if (not flagu): 
                pol_add=pol_add+float(lines.split()[1])
                j=j+1
    
            if(j>NodeNumber-1):
                pol_add=pol_add/NodeNumber
                break
        

    pol[fInd]=pol_add

print(Efield)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(Efield,pol,"+r")
ax.set_xlabel('Electric Field (kV/mm)')
ax.set_ylabel('Polarization (C/m$\mathregular{^2}$)')

plt.show()
 
