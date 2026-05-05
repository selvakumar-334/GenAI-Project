import numpy as np
print(np.__version__)

import numpy as np
a= np.array([1,2,3])
print(a)


text= "hello"
for char in text:
    print(char,ord(char))
    
import numpy as np
image =np.array([[255,0,0],[0,255,0],[0,0,255]])
print(image)

import numpy as np
data=np.array([[25,50000],[30,60000]])
print(data)

import numpy as np
a=np.array([1,2,3])
print(a)

import numpy as np
a=np.array([[1,2],[3,4]])
print(a)

import numpy as np
a=np.zeros((2,3))
print(a)

import numpy as np
a=np.ones((3,3))
print(a)

import numpy as np
a=np.eye(3)
print(a)


import numpy as np
a=np.arange(0,10,2)
print(a)


import numpy as np
a=np.linspace(0,1,5)
print(a)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a.shape)

import numpy as np
a=np.array([1,2,3])
print(a.dtype)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(a[0,1])
print(a[:,1])

import numpy as np
a=np.array([1,2,3])
b=np.array([4,5,6])
print(a+b)
print(a*b)

import numpy as np
a=np.array([1,2,3])
print(a+10)
print(a*2)

import numpy as np
a=np.array([1,2,3])
b=10
print(a+b)

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([1,1,1])
print(a+b)

import numpy as np
a=np.array([1,2,3,4,5,6])
print(np.sum(a))
print(np.mean(a))
print(np.max(a))
print(np.min(a))


import numpy as np
a=np.array([1,2,3,4,5,6])
b=a.reshape(2,3)
print(b)


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.reshape(6)
print(b)

import numpy as np
marks=np.array([70,80,60,90,95])
print(np.sum(marks))
print(np.mean(marks))
print(np.max(marks))
print(np.min(marks))
print(marks>70)