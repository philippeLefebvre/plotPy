import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-5,5,100)
print ('type(x) = ',type(x),' len = ', len(x) )
plt.plot(x,np.sin(x))  # on utilise la fonction sinus de Numpy
plt.ylabel('fonction sinus')
plt.xlabel("l'axe des abcisses")
plt.grid()
plt.show()
