# Spherical Harmonics Particle Shape Generator

* Particle shape influences the hydro-mechanical behaviour of granular materials, e.g., packing density, shear strength, permeability. 
* Previous researches on particle shape effects mainly adopted ellipsoids, rod-like particles, or particle 'clusters'. These particles are either over-simplified or randomly selected. 
* We proposed a systemetic approach to randomly generate 3D particle morphologies with well-controled irregularith. This method depends on a series of Spherical Harmonics fuctions defined on a sphere.

## Getting started

* These instructions will illustrate the procedures to generate irregular particle shapes with SHPSG.

* The algorithm depends on most common packages in Python.

* Please refer to our papers on linking SHs coefficients and shape pactors <a href="https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere" target="_blank">Link</a> and SHs coeffecients random generation method 


## Particle shape

* Particle shape is a multi-scale feature and usually described at three scales, i.e. form, roundness and roughness.

* Spherical Harmonics decompose particle shape features into several degrees. Our study shows particle form and roundness are well represented at degree 1 and 8, respectively. 

* Particle form is defined by three principal dimensions that perpendicular to each other: a$\geq$b$\geq$c. Elongation index Ei = b/a, flatness index Fi = c/b.

* Particle roundness is related to SHs coefficients $D_{2-8}$. Higher $D_{2-8}$ value leads to lower roundness.

* Roughness is related to SHs coefficients $D_{9-15}$. Note that we did not show examples of roughness control. 

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

* **Deheng Wei** - *developed first Matlab code in combination with SPHARM-PDM*
* **Budi Zhao** - *supervised Deheng and developed the standalone Python code*
* **Jianfeng Wang** - *principal investigator for this project*

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* *Icosahedron and subdivision code based on Matlab code by Wil O.C. Ward* <a href="https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere" target="_blank">Link</a>
