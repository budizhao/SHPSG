import numpy as np
from scipy.special import sph_harm

# calcualte coordinates with SH expansion
def sph2cart(coeff, phi, theta):
    x = 0
    y = 0
    z = 0
    index = 0
    for n in range(9):
        order = [*range(-n,n+1)]
        for m in range(2*n+1):
            x += coeff[index,0]*sph_harm(order[m], n, theta, phi)
            y += coeff[index,1]*sph_harm(order[m], n, theta, phi)
            z += coeff[index,2]*sph_harm(order[m], n, theta, phi)
            index += 1
    return x, y, z

# define icosahedron surface
def icosahedron():
    # create unit regular icosahedron
    t = (1+np.sqrt(5)) / 2
    #create vertices
    v = np.array([[-1, t, 0], # v1
         [1, t, 0], # v2
         [-1,-t, 0], # v3
         [1,-t, 0], # v4
         [0,-1, t], # v5
         [0, 1, t], # v6
         [0,-1,-t], # v7
         [0, 1,-t], # v8
         [t, 0,-1], # v9
         [t, 0, 1], # v10
         [-t, 0,-1], # v11
         [-t, 0, 1]])# v12
    # normalise vertices to unit size
    v = v/np.linalg.norm(v[0,:])/2
    #create faces
    f = np.array([[0,11, 5], # f1
         [0, 5, 1], # f2
         [0, 1, 7], # f3
         [0, 7,10], # f4
         [0,10,11], # f5
         [1, 5,9], # f6
         [5,11, 4], # f7
         [11,10, 2], # f8
         [10, 7, 6], # f9
         [7, 1, 8], # f10
         [3,9, 4], # f11
         [3, 4, 2], # f12
         [3, 2, 6], # f13
         [3, 6, 8], # f14
         [3, 8,9], # f15
         [4,9, 5], # f16
         [2, 4,11], # f17
         [6, 2,10], # f18
         [8, 6, 7], # f19
         [9, 8, 1]])# f20
    return v,f

# calculate sphercial coordinates based on xyz
def car2sph(xyz):
    ptsnew = np.hstack((xyz, np.zeros(xyz.shape)))
    xy = xyz[:,0]**2 + xyz[:,1]**2
    ptsnew[:,3] = np.sqrt(xy + xyz[:,2]**2)
    ptsnew[:,4] = np.arctan2(np.sqrt(xy), xyz[:,2]) # for elevation angle defined from Z-axis down
    #ptsnew[:,4] = np.arctan2(xyz[:,2], np.sqrt(xy)) # for elevation angle defined from XY-plane up
    ptsnew[:,5] = np.arctan2(xyz[:,1], xyz[:,0])
    return ptsnew

# subdivide triangle faces
def subdivsurf(f,v):
    f_ = np.zeros((len(f)*4,3))
    for i in range(len(f)): # for each triangle
        tri = f[i,:]
        # calculate mid points (add new points to v)
        [a,v] = getMidPoint(tri[0],tri[1],v)
        [b,v] = getMidPoint(tri[1],tri[2],v)
        [c,v] = getMidPoint(tri[2],tri[0],v)
        # generate new subdivision triangles
        nfc = np.array([[tri[0],a,c],
               [tri[1],b,a],
               [tri[2],c,b],
               [a,b,c]])
        # replace triangle with subdivision
        idx = range(4*i,4*(i+1),1)
        f_[idx,:] = nfc
    return v,f_.astype(int)

def getMidPoint(t1,t2,v):
    # GETMIDPOINT calculates point between two vertices
    # Calculate new vertex in sub-division and normalise to unit length
    # then find or add it to v and return index
    # get vertice positions
    p1 = v[t1,:]
    p2 = v[t2,:]
    # calculate mid point (on unit sphere)
    pm = (p1 + p2) / 2
    pm = pm/np.linalg.norm(pm)/2
    # add to vertices list, return index
    i = len(v)
    v = np.vstack((v,pm))
    return [i,v]

def cleanmesh(f,v):
    # remove duplicate vertices
    v,AC,TC = np.unique(v,return_index = True, return_inverse=True,axis = 0)
    # reassign faces to trimmed vertex list
    for i in range(len(f)):
        for j in range(3):
            f[i,j] = TC[f[i,j]]
    return v,f

from stl import mesh
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

def plotstl(stlpath,figpath):
    # create a new plot
    fig = plt.figure(figsize=(3, 3), dpi=300)
    ax = mplot3d.Axes3D(fig, proj_type ='ortho') 
    plt.rc('font', size=6) 

    # load STL files and add the vectors to the plot
    your_mesh = mesh.Mesh.from_file(stlpath)
    surf = mplot3d.art3d.Poly3DCollection(your_mesh.vectors,linewidth=0.15,facecolors='grey', 
                                          edgecolor = 'b', alpha=.8)
    # set axis properties
    ax.add_collection3d(surf)

    # set scale
    ax.set_xlim([-0.6, 0.6])
    ax.set_ylim([-0.6, 0.6])
    ax.set_zlim([-0.6, 0.6])
    ax.set_xticks(np.arange(-0.6, 0.601, step=0.3))
    ax.set_yticks(np.arange(-0.6, 0.601, step=0.3))
    ax.set_zticks(np.arange(-0.6, 0.601, step=0.3))

    # Show the plot to the screen
    plt.show()

    fig.savefig(figpath,dpi = 300, bbox_inches='tight')

def sh2stl(coeff, sph_cor, vertices, faces,stlpath):
    # update vertices by SH expansion
    for i in range(3):
        vertices[:,i] = sph2cart(coeff,sph_cor[:,4],sph_cor[:,5])[i]

    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = vertices[f[j],:]
    # Write the mesh to file "cube.stl"
    cube.save(stlpath)
