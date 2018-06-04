from scipy.linalg import hilbert
from numpy.linalg import cond
from numpy.linalg import inv
from numpy.linalg import solve



for n in range(1,15):
    h = hilbert(n)
    c = cond(h,2)
    print c


for n in range(1,15):
    H= hilbert(n)
    Hinv = inv(H)
    s=H*Hinv
    print s
    
b = []
for n in range(1,15):
    H = hilbert(n)
    bi = 0
    i = 1
    for j in range(1,n+1):
        
        bi += 1.0/(i + j - 1)
        
    b.append(bi)
    i += 1
    x = solve(H,b)
    print ""
    print x
    print ""
        


    
        


    
    

        