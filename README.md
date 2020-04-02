# Spherical Harmonics Particle Shape Generator - SHPSG

* Particle shape influences the properties of granular materials, e.g., packing density, shear strength, permeability. 

* Existing methods generating irregular particle shapes are sometimes over-simplified, e.g., ellipsoids, rod-like particles, or particle 'clusters'.

* This algorithm randomly generates 3D particle morphologies of user-specified irregularity with Spherical Harmonics.

* This algorithm systematically controls shape irregularity at different scales, e.g., form, roundness and roughness.

## Getting started

* These instructions will illustrate the procedures to generate irregular particle shapes with SHPSG.

* The algorithm depends on most common packages in Python.

* The theories were introduced in two papers: rotational-invirant analysis <a href="https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere" target="_blank">Link</a> and SHs coeffecients random generation method <a href="https://www.sciencedirect.com/science/article/abs/pii/S0032591018301189" target="_blank">Link</a>


## Particle shape

* Particle shape is a multi-scale feature and usually described at three scales, i.e. form, roundness and roughness.

* Spherical Harmonics decompose particle shape features into different scales, SH 'degrees'. For example, particle roundness is well represented with SH coefficients from degree 2 to 8.

* Particle form is defined by three principal dimensions that perpendicular to each other: a$\geq$b$\geq$c. We control two aspect ratios: elongation index Ei = b/a, and flatness index Fi = c/b.

* Particle roundness reflects curvatures at corners. A higher roundness particle has a lower $D_{2-8}$.

* Roughness characterizes surface featureas between corners. A higher roughness particle has a lower $D_{9-15}$.

* The particles are represented by surface meshes with 320 triangular elements. Finer mesh could be used by increasing the mesh subdivision number. A finer surface mesh is needed to show the influence of $D_{9-15}$.


## Examples

```
A sphere: Ei = 1; Fi = 1; $D_{2-8} = 0$, and $D_{9-15} = 0$.

An elipsoid: Ei = 1; Fi = 0.5; $D_{2-8} = 0$, and $D_{9-15} = 0$.

An elipsoid: Ei = 0.8; Fi = 0.5; $D_{2-8} = 0$, and $D_{9-15} = 0$.

Angular particle: Ei = 1; Fi = 1; $D_{2-8} = 0.2$, and $D_{9-15} = 0$.

More angular particle: Ei = 1; Fi = 1; $D_{2-8} = 0.4$, and $D_{9-15} = 0$.

```

## Authors

**Budi Zhao** **Deheng Wei** **Jianfeng Wang** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* *Icosahedron and subdivision code based on Matlab code by Wil O.C. Ward* <a href="https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere" target="_blank">Link</a>
