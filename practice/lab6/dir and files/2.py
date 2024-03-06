import os
from string import ascii_uppercase
print('Path exists:', os.access('/', os.F_OK))
print('Path readable:', os.access('/', os.R_OK))
print('Path writable:', os.access('/', os.W_OK))
print('Path executable:', os.access('/', os.X_OK))