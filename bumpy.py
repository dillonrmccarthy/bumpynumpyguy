#!/usr/bin/python

import numpy as np

bumpy = np.random.randint(10,size=(5)) # 1D array
bumpy_a0 = np.expand_dims(bumpy, axis=0) #shape is now (1,5)
print(bumpy_a0.shape) 
bumpy_a0T = bumpy_a0.T #this makes shape (5,1)
print(bumpy_a0T.shape) 

#ORRR YOU COULD BE SMART AND NOT A FUCKING MORON LIKE I AM AND JUST SWAP THE AXIS
bumpy_a1 = np.expand_dims(bumpy, axis=1) #shape is now (5,5)
print(bumpy_a0T.shape == bumpy_a1.shape)

exit
