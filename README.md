# Spherical Harmonics Particle Shape Generator - SHPSG

## Why should I use SHPSG?

* Particle shape influences the properties of granular materials, e.g., packing density, shear strength, permeability. 

* Existing methods generating irregular particle shapes are sometimes over-simplified, e.g., ellipsoids, rod-like particles, or particle 'clusters'.

* SHPSG provides a systemetic approch to randomly generates 3D particle morphologies with user-specified irregularity.

* Shape irregularity is controlled at different scales, e.g., form, roundness and roughness.

## How to use SHPSG?

* Clone the repository and get started.

* Run the example provided in main.ipynb.

* We provide particle shape introduction, parameter examples, and randonly generated angular particles.

## Particle shape introduction

* Particle shape is a multi-scale feature and usually quantified at three scales, i.e. form, roundness and roughness.

* Spherical Harmonics decompose particle shape features into different SH degrees. Higher SH degree reproduces smaller surface features. Particle form and roundness are well represented up to SH degree 8.

* Particle form is defined by three principal dimensions that perpendicular to each other: a$\geq$b$\geq$c. We control two aspect ratios: elongation index Ei = b/a, and flatness index Fi = c/b.

* Particle roundness reflects curvatures at corners. We increase D2_8 to generate more angular particles.

* Roughness characterizes surface featureas at corners and between corners. We increase D9_15 to produce a higher roughness.

* More details about the theory behind SHPSG were described in two papers: rotational-invirant analysis <a href="https://www.icevirtuallibrary.com/doi/abs/10.1680/jgele.17.00011" target="_blank">Link</a> and SHs coeffecients random generation method <a href="https://www.sciencedirect.com/science/article/abs/pii/S0032591018301189" target="_blank">Link</a>

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

We were inspired by prevoius studies and libraries during methodology and code development. We would like to thank their authors for the great work and publishing the code. We welcome discussion and contribution to improve SHPSG.

- [SPHARM-MAT](http://www.iu.edu/~spharm/SPHARM-docs/C01_Introduction.html)
- [Fourier2D](https://link.springer.com/article/10.1007/s10035-012-0356-x)
- [icosphere](https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere)
