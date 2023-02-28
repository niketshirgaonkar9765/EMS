import numpy as np
from scipy.sparse import csc_matrix
from fractions import Fraction
def float_format(vector,decimal):return np.round((vector).astype(np.float),decimals=decimal)
G=np.matrix([[0,1,1,],[0,0,1],[1,0,0]])
n=len(G)
print(n)
M=csc_matrix(G,dtype=np.float)
print(M)
rsums=np.array(M.sum(1))[:,0]
ri,ci=M.nonzero()
print("ri matrix ",ri)
M.data=M.data/rsums[ri]
print("M.data matrix ",M.data)
dp=Fraction(1,n)
print(dp)
E=np.zeros((3,3))
print("E ",E)
E[:]=dp
print(E[:])
beta=0.85
A=beta*M+((1-beta)*E)
print("A ",A)
r=np.matrix([dp,dp,dp])
print("Value of dp in r")
print("r ",r)
r=np.transpose(r)
print("Transpose of matrix")
print("r ",r)
previous_r=r
print("presious_r value")
for it in range(1,30):
    r=A*r
    if(previous_r==r).all():break
    previous_r=r
    print("Final:\n",float_format(previous_r,3))
