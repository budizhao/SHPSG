{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Spherical Harmonics Particle Shape Generator\n",
    "\n",
    "* Particle shape influences the hydro-mechanical behaviour of granular materials, e.g., packing density, shear strength, permeability. \n",
    "* Previous researches on particle shape effects mainly adopted ellipsoids, rod-like particles, or particle 'clusters'. These particles are either over-simplified or randomly selected. \n",
    "* We proposed a systemetic approach to randomly generate 3D particle morphologies with well-controled irregularith. This method depends on a series of Spherical Harmonics fuctions defined on a sphere.\n",
    "\n",
    "## Getting started\n",
    "\n",
    "* These instructions will illustrate the procedures to generate irregular particle shapes with SHPSG.\n",
    "\n",
    "* The algorithm depends on most common packages in Python.\n",
    "\n",
    "* Please refer to our papers on linking SHs coefficients and shape pactors <a href=\"https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere\" target=\"_blank\">Link</a> and SHs coeffecients random generation method \n",
    "\n",
    "\n",
    "## Particle shape\n",
    "\n",
    "* Particle shape is a multi-scale feature and usually described at three scales, i.e. form, roundness and roughness.\n",
    "\n",
    "* Spherical Harmonics decompose particle shape features into several degrees. Our study shows particle form and roundness are well represented at degree 1 and 8, respectively. \n",
    "\n",
    "* Particle form is defined by three principal dimensions that perpendicular to each other: a$\\geq$b$\\geq$c. Elongation index Ei = b/a, flatness index Fi = c/b.\n",
    "\n",
    "* Particle roundness is related to SHs coefficients $D_{2-8}$. Higher $D_{2-8}$ value leads to lower roundness.\n",
    "\n",
    "* Roughness is related to SHs coefficients $D_{9-15}$. Note that we did not show examples of roughness control. \n",
    "\n",
    "* The particles are represented by surface meshes with 320 triangular elements. Finer mesh could be used by increasing the mesh subdivision number. A finer surface mesh is needed to show the influence of $D_{9-15}$.\n",
    "\n",
    "\n",
    "## Examples\n",
    "\n",
    "\n",
    "```\n",
    "A sphere: Ei = 1; Fi = 1; $D_{2-8} = 0$, and $D_{9-15} = 0$.\n",
    "\n",
    "An elipsoid: Ei = 1; Fi = 0.5; $D_{2-8} = 0$, and $D_{9-15} = 0$.\n",
    "\n",
    "An elipsoid: Ei = 0.8; Fi = 0.5; $D_{2-8} = 0$, and $D_{9-15} = 0$.\n",
    "\n",
    "Angular particle: Ei = 1; Fi = 1; $D_{2-8} = 0.2$, and $D_{9-15} = 0$.\n",
    "\n",
    "More angular particle: Ei = 1; Fi = 1; $D_{2-8} = 0.4$, and $D_{9-15} = 0$.\n",
    "\n",
    "```\n",
    "\n",
    "\n",
    "## Authors\n",
    "\n",
    "* **Deheng Wei** - *developed first Matlab code in combination with SPHARM-PDM*\n",
    "* **Budi Zhao** - *supervised Deheng and developed the standalone Python code*\n",
    "* **Jianfeng Wang** - *principal investigator for this project*\n",
    "\n",
    "## License\n",
    "\n",
    "This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details\n",
    "\n",
    "## Acknowledgments\n",
    "\n",
    "* *Icosahedron and subdivision code based on Matlab code by Wil O.C. Ward* <a href=\"https://www.mathworks.com/matlabcentral/fileexchange/50105-icosphere\" target=\"_blank\">Link</a>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
