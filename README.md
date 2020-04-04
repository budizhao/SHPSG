# Spherical Harmonics Particle Shape Generator - SHPSG

## Why should I use SHPSG?

* Particle shape influences the properties of granular materials, e.g., packing density, shear strength, permeability. 

* Existing methods generating irregular particle shapes are sometimes over-simplified, e.g., ellipsoids, rod-like particles, or particle 'clusters'.

* SHPSG provides a systemetic approch to randomly generates 3D particle morphologies with user-specified irregularity.

* Shape irregularity is controlled at different scales, e.g., form, roundness and roughness.

## Getting started

* To install, you just need to clone the repository.

* You could define parameters, export stl files and visulize generated particles in main.ipynb.

* We provide a brief introduction to particle shape and several examples here.

* The theory behind the generation method was illustrated in two papers: rotational-invirant analysis <a href="https://www.icevirtuallibrary.com/doi/abs/10.1680/jgele.17.00011" target="_blank">Link</a> and SHs coeffecients random generation method <a href="https://www.sciencedirect.com/science/article/abs/pii/S0032591018301189" target="_blank">Link</a>

* We welcome discussion and contribution to improve SHPSG.

## Particle shape

* Particle shape is a multi-scale feature and usually described at three scales, i.e. form, roundness and roughness.

* Spherical Harmonics decompose particle shape features into different scales, SH 'degrees'. For example, particle roundness is well represented with SH coefficients from degree 2 to 8.

* Particle form is defined by three principal dimensions that perpendicular to each other: a$\geq$b$\geq$c. We control two aspect ratios: elongation index Ei = b/a, and flatness index Fi = c/b.

* Particle roundness reflects curvatures at corners. A higher roundness particle has a lower D2_8.

* Roughness characterizes surface featureas between corners. A higher roughness particle has a lower D9_15.

* A high-resolution surface mesh is needed to show the influence of D9_15.


## Parameter examples

```
A sphere: Ei = 1; Fi = 1; D2_8 = 0; D9_15 = 0

Oblate spheroid: Ei = 1; Fi = 0.5; D2_8 = 0; D9_15 = 0

Probalate spheroid: Ei = 0.5; Fi =1; D2_8 = 0; D9_15 = 0

Low angularity: Ei = 1; Fi = 1; D2_8 = 0.1; D9_15 = 0

High angularity: Ei = 1; Fi = 1; D2_8 = 0.4; D9_15 = 0
```

## Random generated angular particles
```
D2_8 = 0.1
```
<img src="examples/D2_8_0.1.gif" width="50%" height="50%">

```
D2_8 = 0.2
```
<img src="examples/D2_8_0.2.gif" width="50%" height="50%">

```
D2_8 = 0.3
```
<img src="examples/D2_8_0.3.gif" width="50%" height="50%">


```
D2_8 = 0.4
```
<img src="examples/D2_8_0.4.gif" width="50%" height="50%">

```
Ei = 1; Fi = 1; D9_15 = 0 for these four groups of particles
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

We were inspired by several libraries during methodology and code development. We would like to thank their authors for the great work and publishing the code.

- [SPHARM-MAT](http://www.iu.edu/~spharm/SPHARM-docs/C01_Introduction.html)
- [Fourier2D](https://link.springer.com/article/10.1007/s10035-012-0356-x)
- [icosphere](https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere)
