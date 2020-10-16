import numpy as np 
# dt = np.dtype([('age',np.int8)]) 
# print(dt)

# dt=np.dtype('i4')
# print(dt)

# dt=np.dtype([('age',np.int8)])
# a=np.array([(10,),(20,),(30,)],dtype=dt)
# print(a)
# print(a['age'])


# a = np.array([[1,2,3],[4,5]]) 
# a.shape = (2,2) 
# print(a)

# Live Demo
import numpy as np 
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]]) 
   
print ('Our array is:' )
print (x) 
print ('\n') 

rows = np.array([[0,0],[3,3]])
cols = np.array([[0,2],[0,2]]) 
y = x[rows,cols] 
   
print (rows)
print(cols)
print ('The corner elements of this array are:' )
print (y)