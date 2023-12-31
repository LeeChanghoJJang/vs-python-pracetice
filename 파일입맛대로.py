users = {'kim':'3kid9','sun80':'393948','ljm':'py90390'}
f = open('users','wb')
import pickle
pickle.dump(users,f)
f.close()

import os 
print(os.path.exists('users'))

f= open('users','rb')
a=pickle.load(f)
print(a)

from glob import glob
print(glob('*.exe'))
print(glob('*.txt'))
print(glob(r'C:\U*'))
from os.path import isdir

for x in glob('*'):
    if isdir(x):
        print(x,'<DIR>')
    else:
        print(x)