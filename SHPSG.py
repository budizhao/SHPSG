import numpy as np

def SHPSG(Ei, Fi, D2_8, D9_15):
    Fvec = np.zeros((4,3),dtype=complex)
    # Determine C0 and C1 with Ei, Fi and a unit maximum principal dimension 
    # A sphere with unit diameter  
    fvec_sphere = -np.sqrt(np.pi/6)*np.array([[0,0,0],[-1,1j,0],[0,0,np.sqrt(2)],[1,1j,0]]) 
    Fvec[0:4,0] = fvec_sphere[:,0]
    Fvec[0:4,1] = Ei*fvec_sphere[:,1]
    Fvec[0:4,2] = (Fi*Ei)*fvec_sphere[:,2]
    d1 = np.sqrt(sum(sum((Fvec*np.conj(Fvec))))).real

    # Determine C2-C15 with d2_8 and d9_16
    # Determine d2 and d9
    #   Assume alpha = 1.387 and beta  = 1.426
    D_2 = D2_8/((2/2)**1.387+(2/3)**1.387+(2/4)**1.387+(2/5)**1.387+(2/6)**1.387+(2/7)**1.387+(2/8)**1.387)*d1
    D_9 = D9_15/((9/9)**1.426+(9/10)**1.426+(9/11)**1.426+(9/12)**1.426+(9/13)**1.426+(9/14)**1.426+(9/15)**1.426)*d1

    # Determine d3-d8 and d10-d15 
    #   -Assume all descriptors have three identical decomposition at x-, y- and z-axis
    I = np.zeros((16,3),dtype = float)
    I[1,:] = [1,1,1]
    I[2,:] = [D_2,D_2,D_2]
    for c in range(3,9):
        dn = [D_2*((c-1)/2)**(-1.387)/np.sqrt(3),D_2*((c-1)/2)**(-1.387)/np.sqrt(3),
              D_2*((c-1)/2)**(-1.387)/np.sqrt(3)]
        I[c,:] = dn

    for c in range(9,15):
        dn = [D_9*((c-1)/9)**(-1.426)/np.sqrt(3),D_9*((c-1)/9)**(-1.426)/np.sqrt(3),
              D_9*((c-1)/9)**(-1.426)/np.sqrt(3)]
        I[c,:] = dn

    L = np.zeros((16**2,3))
    N = np.zeros((16**2,3))

    # Randomly generate P including C1'-C15' with c_n^(-m)=(-1)^m*c_n^m*
    for n in range(1,16):
        J = np.ones((n+1,3))-2*np.random.rand(n+1,3) # [-1,1]
        K = np.flipud(J[0:n,:])
        A = [[(-1)**n,(-1)**n,(-1)**n]]
        B = K*A
        L[n**2:(n+1)**2,:] = np.append(J,B,axis=0)
        M = np.ones((n,3))-2*np.random.rand(n,3)
        M1 = np.append(M,[[0,0,0]],axis = 0)
        N[n**2:(n+1)**2,:] = np.append(M1,np.flipud((-1)**(n+1)*M),axis = 0)

    P = L+N*1j
    P[0,:] = np.ones((1,3))-2*np.random.rand(1,3)

    # Calculate d1'-d16' with the SH coeffiecients of P
    Q = np.conj(P)
    R = np.zeros((16,3))

    for n in range(16):
        R[n,:] = np.sqrt(sum(P[n**2:(n+1)**2,:]*Q[n**2:(n+1)**2,:]).real)

    # Determine C2-C15 by making the descriptors of P equal to d2-d15
    fvec = np.zeros((16**2,3),dtype = complex)
    fvec[0:4,:] = Fvec
    for d in range(2,16):
        fvec[d**2:(d+1)**2,0] = P[d**2:(d+1)**2,0]/R[d,0]*I[d,0]
        fvec[d**2:(d+1)**2,1] = P[d**2:(d+1)**2,1]/R[d,1]*I[d,1]
        fvec[d**2:(d+1)**2,2] = P[d**2:(d+1)**2,2]/R[d,2]*I[d,2]
    return fvec
