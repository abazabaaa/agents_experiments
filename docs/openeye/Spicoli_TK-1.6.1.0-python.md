![](_page_0_Picture_0.jpeg)

**Spicoli TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| <b>1</b>                            | <b>Theory</b>                          | 1    |
|-------------------------------------|----------------------------------------|------|
| 1.1                                 | Surfaces                               | 1    |
| 1.1.1                               | Vertices                               | 1    |
| 1.1.2                               | Triangles                              | 1    |
| 1.1.3                               | Normal Vectors                         | 1    |
| 1.1.4                               | Specific Data                          | 1    |
| 1.1.5                               | Associative Data                       | 1    |
| 1.2                                 | Surface Generation                     | 1    |
| 1.2.1                               | Molecules: Accessible vs Molecular     | 1    |
| 1.2.2                               | Grids                                  | 2    |
| 1.2.3                               | Surface Subsets                        | 2    |
| 1.2.4                               | Geometric Primitives                   | 2    |
| 1.3                                 | Atom Association and Surface Splitting | 1    |
| 1.4                                 | Surface Manipulation                   | 1    |
| 1.4.1                               | Cliques                                | 1    |
| 1.4.2                               | Grids                                  | 1    |
| 1.5                                 | Surface Storage                        | 1    |
| 1.5.1                               | File Formats                           | 1    |
| 1.5.2                               | Attached to Molecules                  | 1    |
| <b>2</b>                            | <b>API</b>                             | 13   |
| 2.1                                 | OESpicoli Classes                      | 13   |
| 2.1.1                               | OESurface                              | 13   |
| 2.2                                 | OESpicoli Constants                    | 25   |
| 2.2.1                               | OEEdgeReductionType                    | 25   |
| 2.2.2                               | OEPolygonizeMethod                     | 25   |
| 2.2.3                               | OESurfaceFileType                      | 26   |
| 2.2.4                               | OEVoxelizeMethod                       | 27   |
| 2.2.5                               | OERibbonType                           | 28   |
| 2.3                                 | OESpicoli Functions                    | 28   |
| 2.3.1                               | OEAddSurfaces                          | 28   |
| 2.3.2                               | OECalculateFaceNormals                 | 29   |
| 2.3.3                               | OECalculateNormals                     | 29   |
| 2.3.4                               | OECalculateSurfaceCurvature            | 29   |
| 2.3.5                               | OECalculateSurfacePotentials           | 29   |
| 2.3.6                               | OECalculateTriangleAreas               | 30   |
| 2.3.7                               | OEColorSurfaceByPotential              | 30   |
| 2.3.8                               | OEGetCenterAndExtents                  | 31   |
| Section                             | Title                                  | Page |
| 2.3.11                              | OEGetSurfaceFormatExtension            | 3    |
| 2.3.12                              | OEGetSurfaceFormatString               | 3    |
| 2.3.13                              | OEInitSurfaceHandlers                  | 3    |
| 2.3.14                              | OEInvertSurface                        | 3    |
| 2.3.15                              | OEIsReadableSurface                    | 3    |
| 2.3.16                              | OEIsWriteableSurface                   | 3    |
| 2.3.17                              | OEMakeAccessibleSurface                | 3    |
| 2.3.18                              | OEMakeBitGridFromSurface               | 3    |
| 2.3.19                              | OEMakeBoxSurface                       | 3    |
| 2.3.20                              | OEMakeCavitySurfaces                   | 3    |
| 2.3.21                              | OEMakeCliqueSurface                    | 3    |
| 2.3.22                              | OEMakeComplexCavities                  | 3    |
| 2.3.23                              | OEMakeConnectedSurfaceCliques          | 3    |
| 2.3.24                              | OEMakeEllipsoidSurface                 | 3    |
| 2.3.25                              | OEMakeGridFromSurface                  | 3    |
| 2.3.26                              | OEMakeMolecularSurface                 | 3    |
| 2.3.27                              | OEMakeProteinRibbonSurface             | 3    |
| 2.3.28                              | OEMakeSphericalSurface                 | 3    |
| 2.3.29                              | OEMakeSurfaceFromGrid                  | 3    |
| 2.3.30                              | OEMakeVoidVolume                       | 3    |
| 2.3.31                              | OEReadSurface                          | 3    |
| 2.3.32                              | OEReduceSurface                        | 3    |
| 2.3.33                              | OERotateSurface                        | 3    |
| 2.3.34                              | OESetSurface                           | 3    |
| 2.3.35                              | OESetSurfaceColor                      | 3    |
| 2.3.36                              | OESetSurfacePotentials                 | 3    |
| 2.3.37                              | OESmoothSurfaceEdges                   | 3    |
| 2.3.38                              | OESpicoliGetArch                       | 3    |
| 2.3.39                              | OESpicoliGetLicensee                   | 3    |
| 2.3.40                              | OESpicoliGetPlatform                   | 3    |
| 2.3.41                              | OESpicoliGetRelease                    | 3    |
| 2.3.42                              | OESpicoliGetSite                       | 3    |
| 2.3.43                              | OESpicoliGetVersion                    | 3    |
| 2.3.44                              | OESpicoliIsLicensed                    | 3    |
| 2.3.45                              | OESplitSurfaceByAtoms                  | 3    |
| 2.3.46                              | OESurfaceArea                          | 4    |
| 2.3.47                              | OESurfaceCliqueArea                    | 4    |
| 2.3.48                              | OESurfaceCliqueCentroid                | 4    |
| 2.3.49                              | OESurfaceCliqueVolume                  | 4    |
| 2.3.50                              | OESurfaceCropToClique                  | 4    |
| 2.3.51                              | OESurfaceIsOpen                        | 4    |
| 2.3.52                              | OESurfaceToMoleculeDistance            | 4    |
| 2.3.53                              | OESurfaceVolume                        | 4    |
| 2.3.54                              | OETransformSurface                     | 4    |
| 2.3.55                              | OETranslateSurface                     | 4    |
| 2.3.56                              | OEWriteSurface                         | 4    |
| 3                                   | Release History                        | 4    |
| 3.1                                 | Spicoli TK 1.6.1                       | 4    |
| 3.2                                 | Spicoli TK 1.6.0                       | 4    |
| 3.3                                 | Spicoli TK 1.5.7                       | 4    |
| 3.3.1                               | New features                           | 4    |
| 3.4                                 | Spicoli TK 1.5.6                       | 4    |
| 3.6                                 | Spicoli TK 1.5.4                       | 44   |
| 3.7                                 | Spicoli TK 1.5.3                       | 44   |
| 3.8                                 | Spicoli TK 1.5.2                       | 44   |
| 3.9                                 | Spicoli TK 1.5.1                       | 44   |
| 3.10                                | Spicoli TK 1.5.0                       | 44   |
| 3.11                                | Spicoli TK 1.4.7                       | 44   |
| 3.12                                | Spicoli TK 1.4.6                       | 44   |
| 3.13                                | Spicoli TK 1.4.5                       | 45   |
|                                     | 3.13.1 New features                    | 45   |
|                                     | 3.13.2 Major bug fixes                 | 45   |
| 3.14                                | Spicoli TK 1.4.4                       | 45   |
| 3.15                                | Spicoli TK 1.4.3                       | 45   |
|                                     | 3.15.1 Minor bug fixes                 | 45   |
| 3.16                                | Spicoli TK 1.4.2                       | 45   |
|                                     | 3.16.1 New features                    | 45   |
|                                     | 3.16.2 Major bug fixes                 | 45   |
| 3.17                                | Spicoli TK 1.4.1                       | 45   |
| 3.18                                | Spicoli TK 1.4.0                       | 45   |
|                                     | 3.18.1 Minor bug fixes                 | 45   |
| 3.19                                | Spicoli TK 1.3.7                       | 46   |
| 3.20                                | Spicoli TK 1.3.6                       | 46   |
|                                     | 3.20.1 New features                    | 46   |
|                                     | 3.20.2 Major bug fixes                 | 46   |
| 3.21                                | Spicoli TK 1.3.5                       | 46   |
|                                     | 3.21.1 Major bug fixes                 | 46   |
|                                     | 3.21.2 Documentation changes           | 46   |
| 3.22                                | Spicoli TK 1.3.4                       | 46   |
| 3.23                                | Spicoli TK 1.3.3                       | 46   |
|                                     | 3.23.1 Minor bug fixes                 | 46   |
|                                     | 3.23.2 Documentation fixes             | 47   |
| 3.24                                | Spicoli TK 1.3.2                       | 47   |
| 3.25                                | Spicoli TK 1.3.1                       | 47   |
|                                     | 3.25.1 New features                    | 47   |
|                                     | 3.25.2 Documentation fixes             | 47   |
| 3.26                                | Spicoli TK 1.3.0                       | 47   |
|                                     | 3.26.1 New features                    | 47   |
|                                     | 3.26.2 Minor bug fixes                 | 48   |
| 3.27                                | Spicoli TK 1.2.2                       | 48   |
| 3.28                                | Spicoli TK 1.2.1                       | 48   |
| 3.29                                | Spicoli TK 1.2.0                       | 48   |
| 3.30                                | Spicoli TK 1.1.3                       | 49   |
| 3.31                                | Spicoli TK 1.1.2                       | 49   |
| 3.32                                | Spicoli TK 1.1.1                       | 49   |
|                                     | 3.32.1 Bug fixes                       | 49   |
| 3.33                                | Spicoli TK 1.1.0                       | 49   |
|                                     | 3.33.1 New features                    | 49   |
|                                     | 3.33.2 Bug fixes                       | 49   |
| 3.34                                | Spicoli TK 1.0.2                       | 50   |
|                                     | 3.34.1 New features                    | 50   |
|                                     | 3.34.2 Minor bug fixes                 | 50   |
| 3.35                                | Spicoli TK 1.0.1                       | 50   |
|                                     | 3.35.1 Bug fixes                       | 50   |
| 4                                   | <b>Copyright and Trademarks</b>        | 51   |
| 5 Sample Code                       | 53                                     |      |
| 6 Citation                          | 55                                     |      |
| 6.1 Orion ® Floes                   | 55                                     |      |
| 6.2 Toolkits and Applications       | 55                                     |      |
| 6.3 OpenEye Web Services            | 57                                     |      |
| 7 Technology Licensing              | 59                                     |      |
| 7.1 GCC                             | 74                                     |      |
| 7.1.1 GCC RUNTIME LIBRARY EXCEPTION | 74                                     |      |
| 7.1.2 GNU GENERAL PUBLIC LICENSE    | 76                                     |      |
| Index                               | 89                                     |      |

### **CHAPTER**

# **THEORY**

The Spicoli toolkit provides broad functionality for creating, manipulating, and analyzing surfaces of many types. Surfaces can be created from molecules, grids, or other surfaces, and can be cropped, colored, and modified to enable visual and analytical analyses. The Spicoli library also provides support for saving and reading surface files.

## **1.1 Surfaces**

In Spicoli, the surface is presented as a first-class object, i.e., an object in its own right, named OESurface. This presentation requires a minimalist definition similar to the way OEChem represents molecules as a collection of atoms and bonds. Basically, both OESurfaces and OEMolBases represent a graph in computer memory.

An *OESurface* provides two ways of retrieving data. The first is a set of methods that will return a copy of the entire underlying data array, e.g. GetVertices. The second is a set of methods that allow random access directly into the array of data, e.g. GetVertex. Basic usage of both will be shown for vertices and triangles.

## 1.1.1 Vertices

The simplest datum in a surface is the vertex: a set of  $(x, y, z)$  coordinates. Vertices are stored internally as an array of large enough to hold GetNumVertices ()  $\star$  3 floats. Figure 1 shows how equivalent dimensions are stored at every third place in the array:

![](_page_6_Figure_9.jpeg)

Fig. 1: Figure 1

Arrangement of coordinates in the vertices array

A copy of this array can be obtained using the code fragment in  $Listing 1$ , where surf is a OESurface object.

#### Listing 1: Example of retrieving the coordinates of all the vertices

```
coords = oechem. OEFloatArray (surf. GetNumVertices () \star 3)
surf.GetVertices(coords)
```

For direct access to the vertex array use OESurface. GetVertex. Listing 2 is a code fragment that shows how to iterate over all the vertex coordinates of a surface.

Listing 2: Example of iterating over all vertices

```
for i in range (surf. GetNumVertices ()) :
    vert = surf. GetVertex(i)
```

### 1.1.2 Triangles

A triangle in Spicoli is a set of three vertices. However, it is important that the order of these vertices be locally consistent. To maintain this consistency vertices of the triangles are defined in a clockwise fashion.

Consider the two triangles in Figure 2 defined by the vertices  $A$ ,  $B$ ,  $C$ ,  $D$ . The triangle on the left is defined by the set (A, B, C). The triangle on the right is defined by the set (D, B, A). Also notice how the edge AB is defined in both triangles but in opposite order. This reversal of order in the two definitions is a direct consequence of the clockwise ordering rule.

![](_page_7_Figure_6.jpeg)

Fig. 2: Figure 2 Two adjacent triangles in a surface

All the methods of construction described in this document obey this rule. A surface that does not follow this rule can still be operated on by Spicoli, but it is not considered a canonical surface and some results may be incorrect or ambiguous.

Spicoli stores triangle vertices as an integer array large enough to hold GetNumTriangles ()  $\star$  3 unsigned integers. Each integer is an index into the vertex array explained in Vertices. Listing 3 is a code fragment that will retrieve a copy of the entire triangles array.

#### Listing 3: Example of retrieving the indices of all the triangles

```
coords = oechem. OEUIntArray (surf. GetNumTriangles () * 3)surf.GetTriangles(coords)
```

For direct access to the triangles array use OESurface. Get Triangle. Listing 4 is a code fragment that shows how to iterate over all the triangles of a surface.

### Listing 4: Example of iterating over all triangles

```
for i in range (surf.GetNumTriangles()):
    tri = surf.GetTriangle(i)
```

## **1.1.3 Normal Vectors**

The emphasis on triangle vertex ordering is to support the notion of the triangle's front and back. The front of the triangle is the side that the vertices appear ordered in a clockwise fashion. Surface normals can then be calculated to point out from the front of the triangle (and conversely from the back of the triangle).

The OESurface also supports vertex normals since vertices are often easier to work with analytically. Vertex normals are calculated by averaging all of the face normals of triangles of which the vertex is a part. The following figures contrasts the differences between face and vertex normals respectively.

![](_page_8_Figure_6.jpeg)

Vectors in Spicoli are represented by three floating point values. Normal vectors are always of unit length. They can be calculated and stored on a OESurface object by invoking the free functions OECalculateNormals and OECalculateFaceNormals for vertex and face normals, respectively.

It is important to remember that the size of a normal array is determined by whether it is a face or vertex normal. For example the size of the vertex normal array is GetNumVertices ()  $\star$  3 floats. While the size of the face normal array is GetNumTriangles ()  $\star$  3 floats.

### 1.1.4 Specific Data

Specific data is any information that can be derived from the surface alone but not from any one triangle or vertex. Currently these properties include the following:

**Curvature** (float) Solvent accessibility of the vertex

**Distance** (float) The Euclidean distance to the vertex from another portion of the surface

Curvature follows a pragmatic computational chemistry definition. It is a property of solvent molecules, represented as spheres, packed onto the surface. Figures 5, 6, and 7 demonstrate the two dimensional case of how solvent molecules are packed onto a surface. The first sphere is mapped adjacent to the vertex using the vertex's normal. Two more spheres are then packed adjacent to the surface and the starting sphere. The angle between these two spheres is used to calculate the accessibility to solvent of the initial sphere using the following formula:

$$
100 * \frac{\theta - \pi}{\pi}
$$

Where  $\theta$  is in radians. For this simple case the angle is also a measure of the surface curvature, hence the name. In three dimensions steradians are required to accomplish the same functional form:

$$
100*\frac{\theta-2\pi}{2\pi}
$$

Where  $\theta$  is in steradians. Therefore, a vertex's "curvature" falls into a range with the following bounds:

-100.0 Solvent that is completely secluded within the surface

0.0 Flat portion of the surface

100.0 Solvent that is completely detached from the surface

![](_page_9_Figure_13.jpeg)

Distance is listed as specific data because it can be derived as the distance between different portions of the surface. This can be useful for measuring the thickness of a volume that is enclosed by a surface. Distances can also be measured to other arbitrary objects as well, such as molecules and other surfaces.

### 1.1.5 Associative Data

Associative data is not inherent from the first-class object definition of a surface. Instead, they are properties mapped onto the surface. Spicoli provides the following associative data arrays:

Atoms (unsigned int) Atom index for the vertex

Color (4 floats or 4 unsigned chars) Color of the vertex

**Potential** (float) Electrostatic potential at the vertex

To map chemical properties onto a surface it is useful to know which atoms are responsible for portions of the surface. When a surface is constructed from a molecule, a data array containing the corresponding atom index for each vertex is created. An atom's index can be obtained from the OEAt omBase. Get Idx method and is unique over the molecule. Refer to the *OEChem* manual for more information about atom indices.

To display chemical properties it is often useful to render them as either discrete colors or a spectrum of colors. The color data array allows the user to set a color for every vertex in the surface. When the surface is then read into a visualizer, such as Vida, the properties can easily be interpreted. Every vertex has the associated values: red, green, blue, and alpha. Alpha is the transparency of the vertex. If any value is retrieved as a float, then that value will range from 0 to 1 inclusive. If retrieved as an unsigned char, the value will range from 0 to 255 inclusive.

Electrostatic potentials can be calculated and displayed on a surface. This can be done with current OpenEye tools such as Zap.

The potentials array is essentially an array of floats the user can use to record analytical data for each vertex.

## **1.2 Surface Generation**

Spicoli can generate surfaces from the following other types of objects:

- Molecules
- $\bullet$  Grids
- Other Surfaces
- Geometric Primitives

## 1.2.1 Molecules: Accessible vs Molecular

OESpicoli provides two functions for generating surfaces directly from molecules: OEMakeAccessibleSurface and OEMakeMolecularSurface. Both functions require the definition of a solvent molecule's probe radius. The default solvent is water with a probe radius of 1.4 Angströms.

The accessible surface is created by representing each atom as a hard sphere [Lee-1971]. The radius of each sphere is the radius of the atom plus the probe radius. Figures 1 and 2 demonstrate how the spheres are packed together to form the surface. In the figures, portions of the surface are colored based upon each atom's contribution to the final accessible surface.

![](_page_11_Figure_1.jpeg)

The molecular surface is composed of atom centered spheres plus reentrants [Connolly-1983]. Each sphere's radius is the atomic radii of the atom it is associated with. The defining characteristic of the molecular surface is the reentrant as shown in Figures 3 and 4. The reentrant models the portion of the molecule inaccessible to solvent. For this reason the volume enclosed by the molecular surface is sometimes referred to as the "solvent-excluded" volume.

![](_page_11_Figure_3.jpeg)

Note: The atoms associated with every surface vertex can be obtained by using the OESurface. GetAtoms and OESurface. GetAtomsElement methods. For an accessible surface this is simple to define, it is the atom closest to the vertex. However, for the molecular surface it is not so clear because of the re-entrants. Typically, it is the closest atom to the vertex, but that is not guaranteed. If this guarantee is required you should call the OESurfaceToMoleculeDistance function on the molecule and surface.

## **1.2.2 Grids**

In Spicoli the construction of surfaces from a molecule proceeds through a grid intermediate. The space between grid points determines the resolution of the surface, i.e., how many triangles there are and the size of each triangle. Grids usually consist of equidistant points aligned along orthogonal axes, but this need not always be the case (for instance, electron density grids from crystallography).

Scalar values are placed at every grid point. Surfaces are constructed by tracing out a contour through the grid points. A contour is a separator of points based on whether they are greater than or less than a given value. The separator is a line in two dimensions and a surface in three dimensions. This is similar to how topographic maps use lines to convey elevation.

When dealing with surfaces the points on the grid with a value less than the chosen contour value are inside the surface and vice versa. OEMakeSurfaceFromGrid will generate a surface from a grid using a variation of the marching cubes algorithm.

Figure 5 is an example of a two dimensional molecular Gaussian grid for a simple molecule arbitrarily oriented in the grid. Figure 6 shows a contour at 1.0 of that same molecular Gaussian grid.

| 0.01                    | 0.18 | 0.82 | 1.21         | 8.30      | 12.11        | 5.64 | 0.84 | 0.04 | 0.00 | 0.01                            | 0.18 | 0.82 | 1.21         | 8.30      | 12.11        | 5.64 | 0.84 | 0.04 | 0.00 |
|-------------------------|------|------|--------------|-----------|--------------|------|------|------|------|---------------------------------|------|------|--------------|-----------|--------------|------|------|------|------|
| 0.06                    | 0.93 | 4.33 | 6.43         | 11.89     | CH3<br>17.36 | 8.08 | 1.20 | 0.11 | 0.01 | 0.06                            | 0.93 | 4.33 | 6.43         | 11.89     | CH3<br>17.36 | 8.08 | 1.20 | 0.11 | 0.01 |
| 0.11                    | 1.57 | 7.33 | H3N<br>10.89 | 17.69     | 12.12        | 4.94 | 3.33 | 0.71 | 0.05 | 0.11                            | 1.57 | 7.33 | H3N<br>10.89 | 17.69     | 12.12        | 4.94 | 3.33 | 0.71 | 0.05 |
| 0.06                    | 0.85 | 3.96 | 5.88         | 12.05     | 17.59        | 9.88 | 6.65 | 1.43 | 0.10 | 0.06                            | 0.85 | 3.96 | 5.88         | 12.05     | 17.59        | 9.88 | 6.65 | 1.43 | 0.10 |
| 0.01                    | 0.15 | 0.66 | 4.45         | 9.56<br>O | 6.55         | 6.30 | 4.24 | 0.91 | 0.06 | 0.01                            | 0.15 | 0.66 | 4.45         | 9.56<br>O | 6.55         | 6.30 | 4.24 | 0.91 | 0.06 |
| 0.00                    | 0.02 | 0.50 | 3.35         | 7.20      | 4.93         | 1.28 | 0.86 | 0.18 | 0.01 | 0.00                            | 0.02 | 0.50 | 3.35         | 7.20      | 4.93         | 1.28 | 0.86 | 0.18 | 0.01 |
| <b>Figure 5</b>         |      |      |              |           |              |      |      |      |      | <b>Figure 6</b>                 |      |      |              |           |              |      |      |      |      |
| Molecular Gaussian Grid |      |      |              |           |              |      |      |      |      | Molecular Gaussian Grid Contour |      |      |              |           |              |      |      |      |      |

Hint: Grids and surfaces are fairly interchangeable. A grid can be constructed from a surface using the OEMakeGridFromSurface function. Then that grid can be used to recreate the original surface by using the OEMakeSurfaceFromGridfunction.

## **1.2.3 Surface Subsets**

Surface subsetting is done through the use of *Cliques*. The triangle, not the vertex, is the most physically relevant intrinsic property of the surface. To maintain a constant surface area for the sum of all partitions Spicoli will not duplicate triangles across surface partitions. However, this does not restrict the duplication of vertices across partitions.

Therefore, the sum of the surface area of every partition will equal the surface area of the whole surface. The sum of OESurface. GetNumTriangles over every partition will equal the total number of triangles in the whole surface. However, the sum of  $OESurface$ . GetNumVertices over every partition will not equal the total number of vertices in the whole surface

#### See also:

- · OESurfaceCropToClique
- · OEMakeCliqueSurface

## **1.2.4 Geometric Primitives**

Spicoli provides the following free functions to construct surfaces from primitive geometric shapes:

**Boxes** OEMakeBoxSurface **Spheres** OEMakeSphericalSurface Ellipsoids OEMakeEllipsoidSurface

## 1.3 Atom Association and Surface Splitting

Molecular and accessible surfaces are created with an atom associated to each vertex. These atom indices can be obtained using the OESurface. GetAtoms and OESurface. GetAtomsElement methods, but the default assignments are not very accurate. Using the OESurfaceToMoleculeDistance function will ensure that each vertex's atom assignment is to the atom whose van der Waals surface is closest to that vertex. While the associations provide an accurate mapping of individual vertices to atoms, *triangles* on the surface may have vertices belonging to different atoms. This can make make mapping of atom-based properties onto the surface problematic.

Surface splitting, using the OESplitSurfaceByAtoms function, will divide a surface such that the boundaries between atoms are distinct, with no triangles being shared by multiple atoms. Surfaces are split through a process of moving vertices and subdividing triangles until no triangle edges cross the analytical boundaries between atoms. A comparison of the atom associations of unsplit and split surfaces is shown in Table: Atom Associations.

### **Atom Associations**

| Image: Molecular surface of benzene colored by atom indices | Molecular surface of benzene, colored by atom indices assigned during surface construction |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| Image: Same surface after atom indices are reassigned       | Same surface after atom indices are reassigned using OESurfaceToMoleculeDistance           |
| Image: Same surface after splitting by atoms                | Same surface after splitting with OESplitSurfaceByAtoms                                    |

Splitting a surface has some consequences that you should be aware of. A split surface will have significantly more vertices and triangles than the surface it was created from. In addition, it will contain numerous duplicate vertices, having the same coordinates and normals but with different atom associations. Finally, it will contain "zero-area" triangles, generated between duplicated vertices to preserve the connectivity of vertices within the surface.

## **1.4 Surface Manipulation**

Spicoli manipulates surfaces through the following two primary mechanisms:

- $\bullet$  Cliques
- $\bullet$  Grids

## 1.4.1 Cliques

A clique is an integral value associated with portions of the surface. They can be arbitrarily assigned in order to create groupings of vertices. Cliques in Spicoli are unsigned ints that can be associated with every vertex of the surface. Spicoli treats the zero clique as a special NULL clique. Therefore, the user should not use zero for performing any clique operations on the surface.

Cliques in Spicoli are collections of vertices. However, an ambiguity occurs when performing triangle-based operations on these cliques. Spicoli will automatically resolve vertex cliques into triangle cliques using the following rule: if two or more vertices in the triangle have the same clique value, the triangle is assigned that clique value; otherwise, if every vertex of the triangle has a different clique value then the triangle is arbitrarily assigned the lowest clique value of the three vertices.

#### See also:

- · OESurfaceCropToClique
- · OEMakeCliqueSurface
- · OEMakeConnectedSurfaceCliques
- · OESurfaceCliqueArea
- OESurfaceCliqueVolume

## **1.4.2 Grids**

Spicoli can construct grids from surfaces. Grid values are assigned using the distance to the nearest surface vertex to the grid point. This makes grid construction very expensive because every grid point must be compared to every surface vertex. The  $OEVoxellizedMethod$  namespace describes the available methods.

#### See also:

- OFMakeGridFromSurface
- · OEMakeSurfaceFromGrid

## **1.5 Surface Storage**

## 1.5.1 File Formats

Spicoli supports the following storage formats:

.srf Old GRASP format

**.oesrf** OpenEye format based upon tagged binary files

The GRASP format is provided for backwards compatibility with older visualization programs. There were byte ordering issues with the format so OpenEye developed a more flexible format based upon the tagged binary IO available in OESystem.

See also:

- · OEWriteSurface
- OESurfaceFileType

### **1.5.2 Attached to Molecules**

The OpenEye format allows surfaces to be attached to molecules and then written out to OEBinary (.oeb) files. A visualizer can then read in the molecule and surface without any other means of making the association. Listing 1 demonstrates how to properly attach surfaces to molecules.

#### Listing 1: Attaching a surface as generic data to be written to OEB

```
surf = oespicoli.OESurface()oespicoli.OEMakeMolecularSurface(surf, mol)
mol.SetData("surface", surf)
ofs = oechem.oemolostream("foo.oeb")
oechem.OEWriteMolecule(ofs, mol)
```

Listing 2 demonstrates how to then read that surface back out of the OEB file.

#### Listing 2: Retrieving a surface attached as generic data from an OEB file

```
ifs = oechem.oemolistream("foo.oeb")
oechem.OEReadMolecule(ifs, mol)
msrf = mol.GetData("surface")
```

#### See also:

- · OEBase. SetData
- · OEBase.GetData

Note: Versions of Spicoli prior to 1.0.2 required calling OEInitSurfaceHandlers in order to have surfaces attached to molecules be read and written to and from OEB.

### **CHAPTER**

## **TWO**

**API** 

## 2.1 OESpicoli Classes

## 2.1.1 OESurface

```
class OESurface : public OESystem: : OEBase
```

#### **Constructors**

```
OESurface()
OESurface (const OESurface & rhs)
OESurface (const OESurfaceImpl & rhs)
```

Default and copy constructors.

#### operator bool

operator bool() const

Whether the surface contains any data (vertices).

#### **Clear**

void Clear()

Delete and deallocate all data associated with this surface. This includes all OEBase data as well.

#### **ClearVertexClique**

**bool** ClearVertexClique()

Sets every vertex clique value to zero. Afterwards, OESurface. IsVertexCliqueSet will return false. This will prevent vertex clique values from being output by OEWriteSurface.

#### **CreateCopy**

OESystem:: OEBase \*CreateCopy() const

#### **GetAtoms**

bool GetAtoms (unsigned int \*atoms) const

Fills the memory pointed to by a toms with the atom index associated with every vertex of the surface. The array passed in should be large enough to hold GetNumVertices () unsigned ints.

#### **GetAtomsElement**

unsigned int GetAtomsElement (unsigned int n) const

Retrieves an element from the internal atoms array. The index n should be less than GetNumVertices ().

#### **GetColor**

```
bool GetColor(float *color) const
bool GetColor (unsigned char *color) const
```

Fills the memory pointed to by color with the color associated with every vertex of the surface. The array passed in should be large enough to hold GetNumVertices ()  $\star$  4 floats or GetNumVertices ()  $\star$  4 unsigned chars, depending on which overload is used.

#### **GetColorElement**

```
GetColorElement (unsigned int n) \rightarrow (r, g, b, a)
```

Retrieves an element from the internal color array. The index n should be less than GetNumVertices ().

#### **GetCurvature**

```
bool GetCurvature (float *curvature) const
```

Fills the memory pointed to by curvature with the curvature associated with every vertex of the surface. The array passed in should be large enough to hold GetNumVertices () floats.

### **GetCurvatureElement**

float GetCurvatureElement (unsigned int n) const

Retrieves an element from the internal curvature array. The index n should be less than GetNumVertices ().

#### **GetDataType**

const void \*GetDataType() const

#### **GetDistance**

bool GetDistance (float \*distance) const

Fills the memory pointed to by distance with the distance each vertex is from another object. The array passed in should be large enough to hold GetNumVertices () floats.

#### **GetDistanceElement**

float GetDistanceElement (unsigned int n) const

Retrieves an element from the internal distance array. The index n should be less than GetNumVertices ().

#### **GetFaceNormals**

bool GetFaceNormals (float \*faceNormals) const

Fills the memory pointed to by faceNormals with a normal vector associated with every triangle of the surface. The array passed in should be large enough to hold GetNumTriangles ()  $\star$  3 floats.

#### **GetFaceNormal**

bool GetFaceNormal (unsigned int n, float \*normal) const

Retrieves a 3-component face normal vector for the specified triangle and stores it in the normal array. The index n must be less than GetNumTriangles (). Returns true upon success.

#### **GetFaceNormalsElement**

float GetFaceNormalsElement (unsigned int n) const

This method has been deprecated. Use OESurface. GetFaceNormal instead.

#### **GetNormals**

bool GetNormals (float \*normals) const

Fills the memory pointed to by normals with a normal vector associated with every vertex of the surface. The array passed in should be large enough to hold GetNumVertices ()  $\star$  3 floats. A vertex normal is calculated by averaging the face normals of all the triangles in which the vertex resides.

#### **GetNormal**

bool GetNormal (unsigned int n, float \*normal) const

Retrieves an 3-component vertex normal for the specified vertex and stores it in the normal array. The index n must be less than GetNumVertices (). This method returns true upon success.

#### **GetNormalsElement**

float GetNormalsElement (unsigned int n) const

This method has been deprecated. Use OESurface. GetNormal instead.

#### **GetNumTriangles**

unsigned int GetNumTriangles() const

Returns the number of triangles in the surface.

#### **GetNumVertices**

unsigned int GetNumVertices() const

Returns the number of vertices in the surface.

#### **GetPotential**

bool GetPotential (float \*potential) const

Fills the memory pointed to by potential with the potential associated with every vertex of the surface. The array passed in should be large enough to hold GetNumVertices () floats.

### **GetPotentialElement**

float GetPotentialElement (unsigned int n) const

Retrieves an element from the internal potentials array. The index n should be less than GetNumVertices ().

#### **GetPotentialName**

const char \*GetPotentialName() const

Returns name of the potentials stored in the surface's potential array.

#### **GetProbeRadius**

float GetProbeRadius() const

Returns the probe radius used in the construction of the surface.

#### **GetResolution**

float GetResolution() const

Returns the grid spacing used in the surface construction.

#### **GetTitle**

const char \*GetTitle() const

Returns the title of the surface.

#### **GetTriangles**

bool GetTriangles (unsigned int \*triangles) const

Fills the memory pointed to by triangles with the vertex indices that compose every triangle in the surface. The vertex indices will obey the clockwise ordering rule described in the Triangles section. The array passed in should be large enough to hold GetNumTriangles ()  $\star$  3 unsigned ints.

#### **GetTriangle**

bool GetTriangle (unsigned int n, unsigned int \*triangle) const

Retrieves the three vertex indices for the specified triangle and stores them in the triangle array. The triangle index n must be less than GetNumTriangles().

#### **GetTrianglesElement**

unsigned int GetTrianglesElement (unsigned int n) const

This method has been deprecated. Use OESurface. Get Triangle instead.

#### **GetVertex**

bool GetVertex (unsigned int n, float \*vertex) const

Retrieves coordinates for the specified vertex and stores them in the vertex array. The vertex index n must be less than GetNumVertices ().

#### **GetVertexClique**

**bool** GetVertexClique (unsigned int \*vertexClique) const

Fills the memory pointed to by vertexClique with the clique values associated with every vertex of the surface. The array passed in should be large enough to hold GetNumVertices () unsigned ints.

#### **GetVertexCliqueElement**

unsigned int GetVertexCliqueElement (unsigned int n) const

Retrieves an element from the internal cliques array. The index n should be less than GetNumVertices ().

#### **GetVertices**

bool GetVertices (float \*vertices) const

Fills the memory pointed to by vertices with the vertex coordinates of the surface. Vertices are aligned every three places in the array as described in the Vertices section. The array passed in should be large enough to hold GetNumVertices ()  $\star$  3 floats.

#### **GetVerticesElement**

float GetVerticesElement (unsigned int n) const

This method has been deprecated. Use OESurface. GetVertex instead.

#### **IsAtomsSet**

bool IsAtomsSet() const

Determine whether the surface has atom indices associated with each vertex. Surfaces generated from OEMakeAccessibleSurface and OEMakeAccessibleSurface automatically set this data.

#### **IsColorSet**

bool IsColorSet () const

Determine whether the surface has color values associated with each vertex.

#### **IsCurvatureSet**

bool IsCurvatureSet() const

Determine whether the surface has curvature value calculated for each vertex.

#### **IsDataType**

bool IsDataType (const void \*type) const

#### **IsDistanceSet**

bool IsDistanceSet() const

Determine whether the surface has a distance value associated with each vertex.

#### **IsFaceNormalsSet**

```
bool IsFaceNormalsSet() const
```

Determine whether the surface has face normals calculated for each triangle.

#### **IsNormalsSet**

```
bool IsNormalsSet() const
```

Determine whether the surface has vertex normals calculated for each vertex. Surfaces generated from OEMakeAccessibleSurface and OEMakeAccessibleSurface automatically set this data.

#### **IsPotentialSet**

bool IsPotentialSet() const

Determine whether the surface has a potential value associated with each vertex.

#### **IsVertexCliqueSet**

bool IsVertexCliqueSet() const

Determine whether the surface has a clique value associated with each vertex.

#### **SetAtoms**

bool SetAtoms (const unsigned int \*atoms)

Sets the internal atoms array data to the values pointed to by  $atoms$ . This should be a pointer to an array of unsigned ints of length GetNumVertices (). Returns true upon success.

#### **SetAtomsElement**

bool SetAtomsElement (unsigned int n, unsigned int value)

Sets an element in the internal atoms array. The index n should be less than GetNumVertices (). Returns true upon success.

#### **SetColor**

```
bool SetColor (const float *color)
bool SetColor (const unsigned char *color)
```

Sets the internal color array data to the values pointed to by color. This should be a pointer to an array of floats or unsigned chars of length GetNumVertices ()  $\star$  4 or GetNumVertices ()  $\star$  4 respectively. Returns true upon success.

#### **SetColorElement**

```
bool SetColorElement (unsigned int n, float r, float g, float b, float a=1.0f)
bool SetColorElement (unsigned int n, unsigned char r, unsigned char q,
                     unsigned char b, unsigned char a=255)
```

Sets an element in the internal color array. The index n should be less than GetNumVertices (). The alpha value, a, defaults to be opaque. Returns true upon success.

#### **SetCurvature**

bool SetCurvature (const float \*curvature)

Sets the internal curvature array data to the values pointed to by curvature. This should be a pointer to an array of floats of length GetNumVertices (). Returns true upon success.

#### **SetCurvatureElement**

bool SetCurvatureElement (unsigned int n, float value)

Sets an element in the internal curvature array. The index n should be less than GetNumVertices (). Returns true upon success.

#### **SetDistance**

**bool** SetDistance (const float \*distance)

Sets the internal distance array data to the values pointed to by distance. This should be a pointer to an array of floats of length GetNumVertices (). Returns true upon success.

### **SetDistanceElement**

bool SetDistanceElement (unsigned int n, float value)

Sets an element in the internal distance array. The index n should be less than GetNumVertices. Returns true upon success.

#### **SetFaceNormal**

bool SetFaceNormal (unsigned int n, const float \*normal)

Sets the face normal for the specified triangle index. The triangle index n must be less than GetNumTriangles(). and normal must contain three elements. Returns true upon success.

#### **SetFaceNormals**

bool SetFaceNormals (const float \*faceNormals)

Sets the internal face normals array data to the values pointed to by faceNormals. This should be a pointer to an array of floats of length GetNumTriangles ()  $\star$  3. Face normals are associated with triangles by their location in the array. Returns true upon success.

#### **SetFaceNormalsElement**

bool SetFaceNormalsElement (unsigned int n, float value)

This method has been deprecated. Use OESurface. SetFaceNormal instead.

#### **SetNormal**

bool SetNormal (unsigned int n, const float \*normal)

Sets the vertex normal for the specified vertex. The vertex index n must be less than GetNumVertices (), and normal must contain three elements. Returns true upon success.

#### **SetNormals**

bool SetNormals (const float \*normals)

Sets the internal vertex normals array data to the values pointed to by normals. This should be a pointer to an array of floats of length GetNumVertices ()  $\star$  3. Vertex normals are associated with vertices by their location in the array. Returns true upon success.

### **SetNormalsElement**

bool SetNormalsElement (unsigned int n, float value)

This method has been deprecated. Use OESurface. Set Normal instead.

#### **SetNumTriangles**

```
bool SetNumTriangles (unsigned int n)
```

Warning: Expert use only.

Set the number of triangles in this surface. Setting this to a value lower than OESurface. Get NumTriangles effectively erases triangles from the surface. The memory for the OESurface is not freed immediately, but cached for reuse. The Clear method should be used if deallocation is desired. Deallocation is also handled automatically by the class destructor.

If the user wants to add more triangles to the surface, SetNumTriangles should be called first to resize the internal triangles array. Note that the methods for accessing individual triangles should not be used after a call to SetNumTriangles. Any data reliant on the number of triangles should first be set using the array based methods. This includes OESurface. SetTriangles and OESurface. SetFaceNormals.

### **SetNumVertices**

**bool** SetNumVertices (unsigned int n)

Warning: Expert use only.

Set the number of vertices in this surface. Setting this to a value lower than GetNumVertices effectively erases vertices from the surface. The memory for the OESurface is not freed immediately, but cached for reuse. The  $OESurface$ . Clear method should be used if deallocation is desired. Deallocation is also handled automatically by the class destructor.

If the user wants to add more vertices to the surface, OESurface. Set NumVertices should be called first to resize the internal vertices array. Note that the methods for accessing individual vertices should not be used after a call to SetNumVertices. Any data reliant on the number of vertices should first be set using the array based methods. These include the following:

- · OESurface. SetVertices
- · OESurface. SetNormals
- · OESurface. SetCurvature
- · OESurface. SetDistance
- · OESurface. SetAtoms
- · OESurface. SetColor
- · OESurface. SetPotential
- · OESurface. SetVertexClique

#### **SetPotential**

bool SetPotential (const float \*potential)

Sets the internal potential array data to the values pointed to by potential. This should be a pointer to an array of floats of length GetNumVertices ()  $\star$  size of (float). Returns true upon success.

#### **SetPotentialElement**

bool SetPotentialElement (unsigned int n, float value)

Sets an element in the internal potential array. The index n should be less than GetNumVertices (). Returns true upon success.

#### **SetPotentialName**

void SetPotentialName (const char \*name)

Set the name of the potentials that are set on the surface.

#### **SetTitle**

```
bool SetTitle (const char *title)
bool SetTitle (const std:: string &title)
```

Set the title of the surface.

#### **SetTriangle**

bool SetTriangle (unsigned int n, const unsigned int \*triangle)

Sets the vertex indices for the specified triangle. The triangle index n must be less than GetNumTriangles (), and triangle must contain three elements. Returns true upon success.

#### **SetTriangles**

bool SetTriangles (const unsigned int \*triangles)

Sets the internal triangles array data to the values pointed to by triangles. This should be a pointer to an array of unsigned ints of length GetNumTriangles ()  $\star$  3. Returns true upon success.

#### **SetTrianglesElement**

bool SetTrianglesElement (unsigned int n, unsigned int value)

This method is deprecated. Use OESurface. Set Triangle instead.

#### **SetVertex**

bool SetVertex (unsigned int n, const float \*vertex)

Sets the coordinates for the specified vertex. The vertex index n must be less than GetNumVertices (), and vertex must contain three elements. Returns true upon success.

#### **SetVertexClique**

bool SetVertexClique (const unsigned int \*vertexClique)

Sets the internal vertex clique array data to the values pointed to by vertex Clique. This should be a pointer to an array of unsigned ints of length GetNumVertices (). Returns true upon success.

#### **SetVertexCliqueElement**

bool SetVertexCliqueElement (unsigned int n, unsigned int value)

Sets an element in the internal vertex clique array. The index n should be less than GetNumVertices (). Returns true upon success.

#### **SetVertices**

**bool** SetVertices (const float \*vertices)

Sets the internal vertices array data to the values pointed to by vertices. This should be a pointer to an array of floats of length GetNumVertices ()  $\star$  3. Returns true upon success.

### **SetVerticesElement**

bool SetVerticesElement (unsigned int n, float value)

This method is deprecated. Use OESurface. Set Vertex instead.

## **2.2 OESpicoli Constants**

### 2.2.1 OEEdgeReductionType

This namespace contains constants used by the OEReduceSurface function.

#### **MinimumDistance**

Specifies a surface edge reduction algorithm which decreases the number of triangles and vertices in a surface by iteratively removing triangles with the shortest edges.

### 2.2.2 OEPolygonizeMethod

The OEPolygonizeMethod namespace is used to specify to the OEMakeMolecularSurface and  $OEMakeAccessibleSurface$  functions the method to be used for polygonizing the surface.

#### See also:

The OEMakeMolecularSurface and OEMakeAccessibleSurface functions for how to pass this constant into the functions.

#### **Grasp**

This polygonization method uses a marching cubes type of algorithm to generate surface triangles.

#### **Compact**

This polygonization method uses a variation on the marching cubes method in which grid vertex warping is used to generate a more "compact" surface. This method results in a surface which has approximately 30% fewer triangles and vertices than those generated using the OEPolygonizeMethod\_Grasp method, with no discernible loss of quality.

#### **Default**

The default polygonization method is OEPolygonizeMethod\_Grasp.

## 2.2.3 OESurfaceFileType

This namespace contains constants for passing to the OEWriteSurface function.

#### See also:

Surface Storage

#### **UNDEFINED**

Used to indicate errors.

#### **Grasp**

The legacy GRASP file format. Will not store all data present on the OESurface object.

#### **OESurface**

Binary Surface format developed by OpenEye. It will store all OESurface data.

## 2.2.4 OEVoxelizeMethod

The OEVoxelizeMethod namespace is used to instruct the OEMakeGridFromSurface function how to voxelize the surface onto the grid. A voxel is the three dimensional equivalent of a pixel.

#### See also:

The OEMakeGridFromSurface function for how to pass this constant into the function.

#### **Distance**

Each grid point is filled with the minimum distance squared from the surface. The distance is negative if the grid point is inside the surface.

Note: The distance is squared to avoid calling the costly square root function.

#### Gaussian

Same as distance, but the value placed in the grid is plotted as a Gaussian function. This means each gridpoint is set to  $e^{-0.33 \cdot d^2}$ , where d is the minimum distance to the surface. Note, where d can still be negative inside the surface. Therefore, the grid values have the following correlation to the volume enclosed by the surface:

Inside the Surface Values are greater than 1.0

At the Surface Values are 1.0

Outside the Surface Values are less than 1.0 and greater than 0.0

#### **Blank**

Same as distance, but grid points inside the surface are set to 1.

#### **Blur**

Discern the shape of the volume enclosed by the surface. This is done by mapping a Gaussian for every grid point inside the volume. This smears out the surface boundary a bit and allowing a smooth drop off from the surface.

#### **Default**

The default voxelization method is OEVoxelizeMethod\_Distance.

## 2.2.5 OERibbonType

The OERibbonType namespace is used to tell the OEMakeProteinRibbonSurface function what style of ribbon to create.

#### See also:

OEMakeProteinRibbonSurface

#### **CAlpha**

The ribbon is created to follow the protein backbone alpha carbons, and its helix and sheet regions will have elliptical cross-sections.

#### **Pretty**

The ribbon is created to follow the protein backbone peptide bonds, and its helix and sheet regions will have rectangular cross-sections. Ribbons created with this type tend to have a smoother, less wavy appearance.

The default ribbon type is OERibbonType\_CAlpha.

## **2.3 OESpicoli Functions**

### 2.3.1 OEAddSurfaces

**bool** OEAddSurfaces (OESurface &surf1, const OESurface &surf2)

Adds surf2 to surf1 using OESurface.operator+=. Always returns true.

### 2.3.2 OECalculateFaceNormals

**bool** OECalculateFaceNormals (OESurface &surf)

Will calculate a normal vector for every triangle of the surface and store them on the surf. To retrieve the vectors after calculation, use the OESurface. GetFaceNormals or OESurface. GetFaceNormal methods.

#### See also:

**Normal Vectors** 

### 2.3.3 OECalculateNormals

```
bool OECalculateNormals (OESurface &surf)
```

Will calculate a normal vector for every vertex of the surface and store them on the surf. To retrieve the vectors after calculation, use the OESurface. GetNormals or OESurface. GetNormal methods.

See also:

**Normal Vectors** 

## 2.3.4 OECalculateSurfaceCurvature

```
bool OECalculateSurfaceCurvature(OESurface &surf, const OEChem::OEMolBase &mol,
                                 float probeRadius=1.4f)
```

Will calculate the surface curvature at every vertex according to the definition given in the Specific Data section. The data can then be retrieved using the OESurface. GetCurvature or OESurface. GetCurvatureElement methods.

The molecule passed in as mol is used to construct a grid marking which regions of space are inaccessible to solvent molecules. Typically this is just the molecule used to construct the surface.

## 2.3.5 OECalculateSurfacePotentials

```
bool OECalculateSurfacePotentials (OESurface& surface,
                                         const OEChem:: OEMolBase& target,
                                         const bool grasp = false;
```

Will calculate atomic potentials and assign those potentials to surface vertices on the supplied surface. The optional parameter grasp set to true will calculate the potentials based on the GRASP method, which is a coarser perspective of the potential using formal charges.

See also:

Atom Potentials Associative Data OEColorSurfaceByPotential

## 2.3.6 OECalculateTriangleAreas

bool OECalculateTriangleAreas (const OESurface &surf, float \*areas)

Will calculate the area of every triangle of surf and store the result in the array areas of that should be large enough to hold GetNumTriangles () floats. The array is indexed by the triangle indices.

Listing 1 demonstrates how to calculate the surface area contribution from each atom. It is assumed surf is an OESurface created from the molecule mol.

Listing 1: Calculates the surface area contribution from each atom

```
areas = occhem. OEFloatArray(surf.GetNumTriangles())oespicoli.OECalculateTriangleAreas(surf, areas)
atoms = [0.0] * mol.fetMaxAtomIdx()for i in range (surf.GetNumTriangles()):
   tri = surf.GetTriangle(i)a1 = surf.GetAtomsElement(trif[0])a2 = surf.GetAtomsElement(tri[1])a3 = surf.GetAtomsElement(tri[2])atomareas[a1] += areas[i]/3.0atoms[a2] += areas[i]/3.0atoms[a3] += areas[i]/3.0for atom in mol. GetAtoms () :
    print ("atom %d area = %2.4f" % (atom.GetIdx(), atomareas[atom.GetIdx()]))
```

## 2.3.7 OEColorSurfaceByPotential

```
bool OEColorSurfaceByPotential (OESurface& surf, OESystem:: OEColorGradientBase& grad,
                               const unsigned alpha = 255);
```

Method to color a surface using a defined gradient based on the stored potentials on the surface vertices.

See also:

Associative Data OEColorGradientBase

## 2.3.8 OEGetCenterAndExtents

void OEGetCenterAndExtents (const OESurface &surf, float \*center, float \*extents)

Iterates through all the vertices in surf to find the center and extents of the surface in Cartesian coordinates. The center will be placed in the memory pointed to by center that should be large enough to hold 3 floats. The extents will be placed in the memory pointed to by extents that should be large enough to hold 3 floats. The extents are the difference between the maximum of the surface along any dimension and the minimum along that same dimension.

See also:

• OEMakeGridFromCenterAndExtents

### 2.3.9 OEGetSurface

OEGetSurface(obj, tag) -> OESurface

Retrieves an OESurface that has been stored as generic data on an OEBase object, using the specified tag.

#### See also:

· OESetSurface function

## 2.3.10 OEGetSurfaceFileType

unsigned int OEGetSurfaceFileType (const char \*ext)

Returns a constant from the  $OESurfaceFileType$  namespace for the file extension ext.

### 2.3.11 OEGetSurfaceFormatExtension

const char \*OEGetSurfaceFormatExtension (unsigned int tag)

Returns a comma-separated list of possible file extensions corresponding to the specified parameter. The parameter, tag, should be drawn from the OESurfaceFileType namespace.

### 2.3.12 OEGetSurfaceFormatString

const char \*OEGetSurfaceFormatString (unsigned int tag)

Returns the name of the file format associated with the symbolic constant tag from the  $OESurfaceFileType$ namespace.

### 2.3.13 OEInitSurfaceHandlers

```
void OEInitSurfaceHandlers (OEChem:: oemolstreambase &fs)
bool OEInitSurfaceHandlers (OESystem:: OEBinaryIOHandlerBase &b)
```

Needs to be called in order for the OEBinary writer to be able to write surfaces as generic data tagged to a molecule or any OEBase object.

Warning: Deprecated as of Spicoli 1.0.2. No longer needs to be called.

See also:

**Attached to Molecules** 

### 2.3.14 OEInvertSurface

**bool** OEInvertSurface (OESurface &surf)

Reverses all the triangle orderings and normal vectors in the surface. This essentially turns the surface inside-out because all the normals facing out are turned in and vice versa.

**Hint:** Water pockets inside of protein structures have their normals facing into the protein. This can be used to make the disconnected surface a surface enclosing the occluded water.

### 2.3.15 OEIsReadableSurface

```
bool OEIsReadableSurface (unsigned int type)
bool OEIsReadableSurface(const std::string &filename)
```

Returns true if the supplied file format is readable by Spicoli. The filename can be a file name or a file extension. The unsigned int parameter value should be drawn from the  $OESurfaceFileType$  namespace.

### 2.3.16 OEIsWriteableSurface

```
bool OEIsWriteableSurface (unsigned int type)
bool OEIsWriteableSurface(const std::string &filename)
```

Returns true if the supplied file format is writable by Spicoli. The filename can be a filename or a file extension. The unsigned int parameter value should be drawn from the OESurfaceFileType namespace.

### 2.3.17 OEMakeAccessibleSurface

```
bool OEMakeAccessibleSurface(OESurface & surf, const OEChem::OEMolBase & mol,
                              float resolution=0.5f, float probeRadius=1.4f,
                              unsigned int polygonizeMethod =
→OEPolygonizeMethod::Default)
bool OEMakeAccessibleSurface (OESurface &surf, const float *coords,
                              const float *radii, int natoms,
                              float resolution=0.5f, float probeRadius=1.4f,
                              unsigned int polygonizeMethod =
\rightarrowOEPolygonizeMethod::Default)
```

Fill the surface surf with the accessible surface for the molecule mol. See the Molecules: Accessible vs Molecular section for a full description of the accessible surface. The atomic radius of each atom in the molecule should already be set before calling this function. The suggested radii can be set with OEAssignBondiVdWRadii.

The resolution is the grid spacing to use during surface construction. This is typically scaled with the size of the molecule. For most molecules, 0.5 is good.

The default probe Radius is  $1.4 \text{ Å}$ , the radius of water approximated as a sphere.

The polygonizeMethod argument specifies the method to be used when generating the triangles for the surface. Allowed values are from the OEPolygonizeMethod namespace.

The overloaded version of the function takes coordinate and radii arrays, coords and radii respectively, of length natoms to create the accessible surface.

This function will set the vertex normals and atoms arrays on the surface.

#### See also:

- Molecules: Accessible vs Molecular
- The OEPolygonizeMethod namespace

### 2.3.18 OEMakeBitGridFromSurface

```
bool OEMakeBitGridFromSurface(OESystem::OEScalarGrid &grid,
                              const OESurface &surf)
bool OEMakeBitGridFromSurface(OESystem::OEScalarGrid &grid,
                              const OESurface &surf, float spacing, float buffer)
```

Fill  $\sigma$ rid with either 0.0 or 1.0 marking whether that grid points lies inside or outside the volume enclosed by the surface. 0.0 indicates the point is outside the surface. 1.0 indicates the point is inside the surface.

### 2.3.19 OEMakeBoxSurface

```
bool OEMakeBoxSurface (OESurface &surf, const float *center,
                      const float *extents)
```

Creates a box in surf located at center and extending extents in each dimension. Each of the six faces of the box will be composed of two triangles.

### 2.3.20 OEMakeCavitySurfaces

```
bool OEMakeCavitySurfaces(const OEChem:: OEMolBase & mol, OESurface & surf,
                           float resolution=0.5f, float probeRadius = 1.4f)
```

Create a surface, surf, from the macromolecule, mol, representing where solvent can be occluded inside the molecule. Therefore, this will not give cavities contiguous with the outside of the molecule. The resolution is the grid spacing to use during surface construction. The probe Radius is the size of the solvent probe to use, in Angstroms.

### 2.3.21 OEMakeCliqueSurface

```
bool OEMakeCliqueSurface (OESurface &newsurf, const OESurface &surf,
                         unsigned int clique)
```

Creates a new surface in newsurf from the triangles in surf marked with the vertex clique value clique. Zero is not a valid clique. See the *Cliques* section on how vertex cliques are assigned to triangles. See the *Surface Subsets* section for an explanation of how Spicoli handles subset boundaries. Returns true if successful.

### 2.3.22 OEMakeComplexCavities

```
bool OEMakeComplexCavities (const OEChem:: OEMolBase &moll,
                            const OEChem:: OEMolBase &mol2,
                            OESurface &surf,
                            float resolution=0.5f,
                            float probeRadius=1.4f)
```

Constructs a surface representing the volume between a ligand  $(mol1)$  and a macromolecule  $(mol2)$  that can accommodate a spherical probe with radius of probeRadius. The resolution of the grid used to construct the surface is specified by resolution. The surface is restricted to a 6 Angstrom envelope around moll.

### 2.3.23 OEMakeConnectedSurfaceCliques

```
unsigned int OEMakeConnectedSurfaceCliques (OESurface &surf)
```

Assigns a different clique value, starting at 1, to each connected component of the surface. The number of connected components is returned. Listing 2 demonstrates cropping a surface to its largest component.

#### Listing 2: Extracting the largest portion of the surface

```
nclqs = oespicoli.OEMakeConnectedSurfaceCliques(surf)
ares = []for i in range (1, nclqs+1):
   areas.append((oespicoli.OESurfaceCliqueArea(surf, i), i))
maxarea, maxclq = max(ares)oespicoli.OESurfaceCropToClique(surf, maxclq)
```

## 2.3.24 OEMakeEllipsoidSurface

```
bool OEMakeEllipsoidSurface(OESurface &surf, float *center, float a, float b,
                            float c, float *dir1, float *dir2, float *dir3,
                            int level=4)
```

### 2.3.25 OEMakeGridFromSurface

bool OEMakeGridFromSurface (OESystem:: OEScalarGrid & qrid, const OESurface & surf, unsigned int method=OEVoxelizeMethod::Default)

Fill grid with a voxelized representation of the surface by the method passed as the method parameter. The constants for method parameter are defined by the OEVoxelizeMethod namespace.

#### See also:

The OEVoxelizeMethod namespace.

### 2.3.26 OEMakeMolecularSurface

```
bool OEMakeMolecularSurface (OESurface &surf, const OEChem::OEMolBase &mol,
                            float resolution=0.5f, float probeRadius=1.4f,
                            unsigned int polygonizeMethod =
→OEPolygonizeMethod::Default)
bool OEMakeMolecularSurface (OESurface & surf, const float *coords,
                            const float *radii, int natoms, float resolution=0.5f,
                            float probeRadius=1.4f,
                            unsigned int polygonizeMethod =
→OEPolygonizeMethod::Default)
```

Fill the surface surf with the molecular surface for the molecule mol. See Molecules: Accessible vs Molecular section for a full description of the molecular surface. The atomic radius of each atom in the molecule should already be set before calling this function. The suggested radii can be set with OEAssignBondiVdWRadii.

The resolution is the grid spacing to use during surface construction. This is typically scaled with the size of the molecule. For most molecules 0.5 is good.

The default probeRadius is 1.4 Å, the radius of water approximated as a sphere.

The polygonizeMethod specifies the method to be used when generating the triangles for the surface. Allowed values are from the OEPolygonizeMethod namespace.

The overloaded version of the function takes a coordinate and radii array, coords and radii respectively, of length natoms to create the accessible surface.

This function will set the array of vertex normals and array of atom indices on the surface.

#### See also:

- Molecules: Accessible vs Molecular
- The OEPolygonizeMethod namespace

## 2.3.27 OEMakeProteinRibbonSurface

```
bool OEMakeProteinRibbonSurface(OESurface &surf, const OEChem::OEMolBase &mol,
\rightarrowunsigned int type)
```

This function fills the surface surf with a ribbon surface for the molecule.

It will set the vertex normals, colors, and atom indices on the surface.

The type argument specifies the type of ribbon to be created, from the  $OERibbonType$  namespace.

### 2.3.28 OEMakeSphericalSurface

```
bool OEMakeSphericalSurface (OESurface &surf, float *center, float radius,
                            unsigned int level=4)
```

Creates a spherical surface in surf with the center located at center (an array of three floats) with the radius radius. The level argument determines the number of triangles used to approximate the sphere. The number of triangles is equal to  $level (level + 1) \times 8$ . For example the default level of 4 generates 160 triangles which is generally considered to be a good sphere to the human eye.

### 2.3.29 OEMakeSurfaceFromGrid

```
bool OEMakeSurfaceFromGrid(OESurface &surf, const OESystem:: OESkewGrid &grid,
                           float contour)
bool OEMakeSurfaceFromGrid(OESurface &surf,
                           const OESystem:: OEFixedGrid<float> &grid,
                           float contour)
bool OEMakeSurfaceFromGrid(OESurface &surf,
                           const OESystem:: OEFixedGrid<float> &grid,
                           float contour, float resolution)
```

An implementation of the marching cubes algorithm to create a surface, surf, through the values in the grid, grid. Grid points with values less than contour are inside the surface and the converse is true for grid points outside the surface

#### See also:

The *Grids* section for more information on converting grids to surfaces.

### 2.3.30 OEMakeVoidVolume

```
bool OEMakeVoidVolume (const OEChem:: OEMolBase &mol1,
                       const OEChem:: OEMolBase &mol2,
                       OESystem:: OEScalarGrid & qrid,
                       float resolution,
                       float probeRadius = 1.4f)
```

Constructs a grid representing the void, or unoccupied, volume between a ligand  $(mol1)$  and a macromolecule  $(mol2)$ that can accommodate a spherical probe with radius less than probeRadius. The resolution of the grid is specified by resolution. The grid grid is resized to fit a 5 Angstrom envelope around  $mol1$ , and its values are set to 1.0 inside the void volume and 0.0 outside.

## 2.3.31 OEReadSurface

```
bool OEReadSurface(const std:: string & fname, OESurface & surf)
bool OEReadSurface(OEPlatform:: oeistream &ifs, OESurface &surf,
                   unsigned int type)
```

Read the contents of the file named frame into the surface surf. Returns false if frame is not a valid surface file name.

An overload is provided to take any arbitrary oeistream.

### 2.3.32 OEReduceSurface

```
bool OEReduceSurface (OESurface & reducedSurface,
                     const OESurface &original,
                     unsigned int targetNumberOfVertices,
                     unsigned int type = OEEdgeReductionType::MinimumDistance)
```

Takes a surface and creates a new surface from it, with the new surface having a reduced number of vertices and triangles. The targetNumberOfVertices argument supplies a value for the desired number of vertices for the returned surface. The overall quality of the new surface will depend on this value, with smaller values giving lower quality surfaces. Currently only one edge reduction method is supported (OEEdgeReductionType\_MinimumDistance). Returns true if the returned surface contains the requested number of vertices.

### 2.3.33 OERotateSurface

void OERotateSurface (OESurface &surf, float \*rmat)

Rotates the surface by the supplied 3x3 matrix  $r \text{mat}$ , specified as a 9-element array in row-major order.

#### See also:

- · OETranslateSurface
- · OETransformSurface

### 2.3.34 OESetSurface

OESetSurface(obj, tag, surface) -> bool

Sets an OESurface as generic data on an OEBase object, using the specified tag.

#### See also:

• OEGetSurface function

### 2.3.35 OESetSurfaceColor

```
bool OESetSurfaceColor(OESurface &surf, float r, float g, float b, float a=1.0f)
bool OESetSurfaceColor(OESurface &surf, unsigned char r, unsigned char g,
                      unsigned char b, unsigned char a=255)
```

Sets the color of the entire surface to the specified color.

### 2.3.36 OESetSurfacePotentials

```
bool OESetSurfacePotentials (OESurface &surf,
                             const OESystem:: OEScalarGrid & grid)
```

Linearly interpolates the values in the OEScalarGrid grid onto the surface surf. The scalar value associated with each vertex can then be accessed using the OESurface. GetPotential and OESurface. GetPotentialElement methods.

## 2.3.37 OESmoothSurfaceEdges

```
bool OESmoothSurfaceEdges (OESurface &surf)
```

Smooth the edges of an open surface by adjusting edge vertices. This is designed mostly for cleaner visual representation in 3D.

![](_page_43_Picture_4.jpeg)

Fig. 1: Left picture is a standard, cropped subsurface. Right is the same surface after smoothing.

## 2.3.38 OESpicoliGetArch

```
const char *OESpicoliGetArch()
```

## 2.3.39 OESpicoliGetLicensee

```
bool OESpicoliGetLicensee(std::string &licensee)
```

## 2.3.40 OESpicoliGetPlatform

```
const char *OESpicoliGetPlatform()
```

Return the internal build string used by OpenEye Scientific Software to identify a platform. The format of these strings may change over time, and future distributions may contain different values even when using the same operating system, compiler and processor. For example, on a x86\_64 Red Hat Enterprise Linux box this would return  $redhat-RHEL5-q++4.1-x64.$ 

## 2.3.41 OESpicoliGetRelease

const char \*OESpicoliGetRelease()

Return the release name of the OESpicoli library being used. This returns a value similar to 1.0 for production versions of the library, and 1.0 debug for the checking version of the library.

## 2.3.42 OESpicoliGetSite

```
bool OESpicoliGetSite(std::string &site)
```

## 2.3.43 OESpicoliGetVersion

unsigned int OESpicoliGetVersion ()

Return the version number of the library being used. This is an unsigned integer value indicating the date on which the library was built, for example 20020903, for the 3rd of September 2002. This value should be used when reporting problems, and unlike the release string, may be used in comparisons if needed.

## 2.3.44 OESpicolilsLicensed

bool OESpicoliIsLicensed (const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any Spicoli TK functionality.

The 'feature' argument can be used to check for a valid license to **Spicoli TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current Spicoli TK license.

See also:

· OEChemIsLicensed function

## 2.3.45 OESplitSurfaceByAtoms

```
bool OESplitSurfaceByAtoms (OESurface &newsurf,
                            const OESurface &surf,
                            const OEChem:: OEMolBase & mol,
                            double maxDist = 4.0)
bool OESplitSurfaceByAtoms (OESurface &surf,
                            const OEChem:: OEMolBase & mol,
                            double maxDist = 4.0)
```

Given an OESurface (surf) and the molecule it was constructed from  $(m \circ 1)$ , this function will create a new version of the surface with triangles cleanly partitioned by atom boundaries. The vertices, triangles, and atom associations in the surface are all adjusted from the original surface to create the partitioning. With the first form of this function, the split surface will be returned in the newsurf surface object. With the second form, the input surface is modified in-place. The maxDist parameter specifies an upper limit for the expected distance from any vertex in the surface to its assigned atom. The default value is adequate for normal molecular and solvent-accessible surfaces. Using too small of a value will result in decreased performance.

#### See also:

Atom Association and Surface Splitting

### 2.3.46 OESurfaceArea

float OESurfaceArea (const OESurface & surf)

Returns the total surface area of surf.

## 2.3.47 OESurfaceCliqueArea

float OESurfaceCliqueArea (const OESurface &surf, unsigned int clique)

Return the surface area for a specified clique. Zero is not a valid clique. See Section 2.3.1 on how vertex cliques are assigned to triangles.

## 2.3.48 OESurfaceCliqueCentroid

```
bool OESurfaceCliqueCentroid(const OESurface &surf, unsigned int clique,
                             float *centroid)
```

Return the centroid coordinates  $(x,y,z)$  in centroid for clique. Zero is not a valid clique.

#### See also:

The Cliques section on how vertex cliques are assigned to triangles.

## 2.3.49 OESurfaceCliqueVolume

float OESurfaceCliqueVolume (const OESurface &surf, unsigned int clique)

Return the volume for a specified clique. Zero is not a valid clique.

#### See also:

The Cliques section on how vertex cliques are assigned to triangles.

Note: The volume may be negative if the clique is an open surface. However, the sum of all surface partitions will equal the total volume of the enclosed surface.

### 2.3.50 OESurfaceCropToClique

**bool** OESurfaceCropToClique (OESurface &surf, unsigned int clique)

Trim surf of the triangles not marked with the vertex clique value clique. Zero is not a valid clique. See Section 2.3.1 on how vertex cliques are assigned to triangles. Returns true if successful.

#### See also:

- The Cliques section on how vertex cliques are assigned to triangles.
- The *Surface Subsets* section for an explanation of how Spicoli handles subset boundaries.

### 2.3.51 OESurfacelsOpen

**bool** OESurfaceIsOpen(const OESurface &surf)

Returns whether the surface is open. A surface is open if any triangle does not border exactly three other triangles.

### 2.3.52 OESurfaceToMoleculeDistance

**bool** OESurfaceToMoleculeDistance(OESurface &surf, const OEChem::OEMolBase &mol)

Will calculate the minimum distance between every vertex in the surface (surf) and every atom in the molecule (mol). The minimum distance for each vertex is then stored on the surface to be accessed via the  $OESUrface$ . GetDistance and OESurface. GetDistanceElement methods. Distances are calculated as the euclidean distance between the vertex and atom center minus the atomic radii. Note that this can result in distances that are negative to denote that they are inside the molecule. If atomic radii are not specified on the molecule BondiVdWRadii will be used.

This function will also reassign the atom indices associated with every vertex of the surface. To access these changes use the OESurface. GetAtoms and OESurface. GetAtomsElement methods.

### 2.3.53 OESurfaceVolume

```
float OESurfaceVolume (const OESurface & surf)
```

Returns the volume enclosed by the surface.

### 2.3.54 OETransformSurface

float OETransformSurface (OESurface &surf, const OEChem:: OETrans &trans)

Transforms a surface using a supplied OETrans object.

#### See also:

- OERotateSurface
- · OETranslateSurface
- OETrans

### 2.3.55 OETranslateSurface

void OETranslateSurface (OESurface &surf, float \*trans)

Translates the surface using the supplied 3-element translation vector.

#### See also:

- · OERotateSurface
- · OETransformSurface

## 2.3.56 OEWriteSurface

```
bool OEWriteSurface (const std:: string & fname, const OESurface & surf)
bool OEWriteSurface(OEPlatform::oeostream &ofs, const OESurface &surf,
                    unsigned int type)
```

Write surf to the surface file fname. Returns false if fname is not a valid surface file name. This will overwrite the previous file if it existed.

The overload that takes an oeostream can be used to write multiple surfaces to the same destination. Note that the format must be specified by a constant from the  $OESurfaceFileType$  namespace as the type argument. The OESurfaceFileType\_Grasp format does not support this kind of use. Returns true if written successfully.

### **CHAPTER**

## **THREE**

# **RELEASE HISTORY**

## 3.1 Spicoli TK 1.6.1

Minor internal improvements have been made.

## 3.2 Spicoli TK 1.6.0

Minor internal improvements have been made.

## 3.3 Spicoli TK 1.5.7

### 3.3.1 New features

- A function was added to assign surface potentials based on a molecule's OECalculateSurfacePotentials, using either atomic potentials or a potential based on formal charges of protein residues at the protein surface (GRASP) using Zap (license required).
- A function was added to color a surface based on its stored potential OEColorSurfaceByPotential.

## **3.4 Spicoli TK 1.5.6**

Minor internal improvements have been made.

## 3.5 Spicoli TK 1.5.5

Minor internal improvements have been made.

## 3.6 Spicoli TK 1.5.4

• Minor internal improvements have been made.

## 3.7 Spicoli TK 1.5.3

#### Fall 2021

• Minor internal improvements have been made.

## 3.8 Spicoli TK 1.5.2

July 2021 Minor internal improvements have been made.

## 3.9 Spicoli TK 1.5.1

#### **Fall 2020**

• Minor internal improvements have been made.

## 3.10 Spicoli TK 1.5.0

• Minor internal improvements have been made.

## 3.11 Spicoli TK 1.4.7

• Minor internal improvements have been made.

## 3.12 Spicoli TK 1.4.6

• Minor internal improvements have been made.

## 3.13 Spicoli TK 1.4.5

### 3.13.1 New features

• DNA/RNA ribbons are now available through the OEMakeProteinRibbonSurface function. When molecules containing DNA or RNA residues are passed to this function with a ribbon style of OERibbonType\_Pretty, the resulting surface now contains ribbons for both protein and nucleic acid residues.

## 3.13.2 Major bug fixes

• OEMakeAccessibleSurface no longer crashes when passed extremely large molecules (many hundreds of Angstroms across). The function now reduces the resolution of the surface, if necessary, to allow the surface to fit in the available memory.

## 3.14 Spicoli TK 1.4.4

• Minor internal improvements have been made.

## 3.15 Spicoli TK 1.4.3

### 3.15.1 Minor bug fixes

• A bug that caused protein ribbons created with the type OERibbonType\_Pretty to be truncated by one residue at the C-terminus has been fixed.

## 3.16 Spicoli TK 1.4.2

### 3.16.1 New features

• A new style of protein ribbons has been added and is accessible through the function OEMakeProteinRibbonSurface. A third argument, a constant from the OERibbonType namespace, has been added to this function to specify the ribbon type. The new ribbon style  $OERibbonType\_Prefix$ creates ribbons that have a smoother appearance than the older, default style.

### 3.16.2 Major bug fixes

• A crash that occurred with calling one variant of OEMakeBitGridFromSurface has been fixed.

## 3.17 Spicoli TK 1.4.1

• Minor internal improvements have been made.

## 3.18 Spicoli TK 1.4.0

### 3.18.1 Minor bug fixes

• A crash in the OEMakeProteinRibbonSurface function that occurred when adding a ribbon to proteins with C-alpha atoms and alternate locations has been fixed.

## 3.19 Spicoli TK 1.3.7

• Minor internal improvements have been made.

## 3.20 Spicoli TK 1.3.6

### 3.20.1 New features

· OESmoothSurfaceEdges function has been added for cleaner visual representation in 3D.

### 3.20.2 Major bug fixes

• A crash in  $OEMakeGridFromSurface$  has been fixed. The crash occurred when the function was passed a grid that wasn't large enough to enclose the entire surface.

## 3.21 Spicoli TK 1.3.5

### 3.21.1 Major bug fixes

• Surface readers have been made more robust to junk data being passed to them. They should no longer crash for any random data input.

### 3.21.2 Documentation changes

• The anisotropy example has been updated to perceive residues in cases when it is not done by the molecule reader (for example, in the case of  $mod 2$ ).

## 3.22 Spicoli TK 1.3.4

• Minor internal cleanup has been performed.

## 3.23 Spicoli TK 1.3.3

### 3.23.1 Minor bug fixes

• Internal refactoring has been performed to improve stability.

## 3.23.2 Documentation fixes

- OESetSurface and OEGetSurface documentation have been added for Python, Java, and C#.
- The OEEdgeReductionType namespace is now documented.
- The missing Java example Volume. java has been added.

## **3.24 Spicoli TK 1.3.2**

• OEMakeCliqueSurface and OESurfaceCropToClique will no longer leave the OESurface consuming more memory than necessary.

## 3.25 Spicoli TK 1.3.1

## 3.25.1 New features

- OEMakeComplexCavities added a "probe radius" argument. Previously, the probe radius used in the calculation was always set to 1.4 Angstroms.
- OEMakeProteinRibbonSurface added to generate a protein ribbon as an OESurface object.

### **3.25.2 Documentation fixes**

- OEMakeVoidVolume documentation corrected to clarify the meaning of the probe radius argument.
- Python examples have been added to demonstrate additional functionality.

## 3.26 Spicoli TK 1.3.0

### 3.26.1 New features

- The internals of the Spicoli toolkit have been migrated from C to pure C++ to ensure better interoperability with C++, especially in terms of object lifetime and management.
- A new function, OESplitSurfaceByAtoms, will divide an OESurface and cleanly partition the triangles along atom boundaries. The result is a surface that can be nicely divided and colored by its underlying atoms.
- The OESurface class has a new method, GetProbeRadius, which returns the probe radius value used to create the surface.
- The functions OEMakeCavitySurfaces and OEMakeVoidVolume now accept an optional probe radius parameter to be used for the surface construction. The default value of this parameter is 1.4 Angstroms.

### 3.26.2 Minor bug fixes

• Generic data stored on an OESurface is now saved when the surface is written to .oeb or .oesrf files.

## 3.27 Spicoli TK 1.2.2

• Minor internal improvements.

## 3.28 Spicoli TK 1.2.1

• Minor internal improvements.

## 3.29 Spicoli TK 1.2.0

• A number of OESurface methods for accessing triangles, vertices, and normals have been deprecated and replaced with more convenient methods. The old methods required three calls to get all three components of a vector or triangle, while the new methods only require one.

| Deprecated Methods    | Replacement Methods |
|-----------------------|---------------------|
| GetVerticesElement    | GetVertex           |
| SetVerticesElement    | SetVertex           |
| GetTrianglesElement   | GetTriangle         |
| SetTrianglesElement   | SetTriangle         |
| GetNormalsElement     | GetNormal           |
| SetNormalsElement     | SetNormal           |
| GetFaceNormalsElement | GetFaceNormal       |
| SetFaceNormalsElement | SetFaceNormal       |

- A new polygonization method has been made available to the OEMakeMolecularSurface and OEMakeAccessibleSurface functions. An optional argument to these functions can specify OEPolygonizeMethod\_Grasp (the original method) or OEPolygonizeMethod\_Compact (the newer method). The newer method produces surfaces with around 30% fewer triangles and vertices, and a more uniform spacing of vertices. The argument defaults to the original method, so existing code won't be affected.
- OEReduceSurface added that allows the reduction of the number of vertices in a surface to a user-specified number.
- New functions have been provided for transforming OESurface coordinates and normals: OERotateSurface, OETranslateSurface, and OETransformSurface.

## 3.30 Spicoli TK 1.1.3

• Added two examples of extracting the surface of the protein around a binding site.

## 3.31 Spicoli TK 1.1.2

• Internal build system improvements.

## 3.32 Spicoli TK 1.1.1

### 3.32.1 Bug fixes

- Minor documentation fixes.
- OEMakeComplexCavities example program now properly suppresses hydrogen and passes the protein and ligand to the function in the proper order.

## 3.33 Spicoli TK 1.1.0

### 3.33.1 New Features

· Added the OEMakeBitGridFromSurface function. This is a lot faster than using OEMakeGridFromSurface to generate a lookup grid for whether a point is inside or outside a surface.

### 3.33.2 Bug fixes

• The previous release (1.0.2) introduced the feature that didn't require the user to call OEInitSurfaceHandlers. This didn't work sometimes when statically linking an executable. This was because the library initialization code that needed to get run was getting discarded by the linker because none of the functions in that translation unit were being called. The library initialization code has been migrated to the same translation unit as the OESurface since these functions always have to be called to attach a molecule as generic data.

Note: This only affected C++ users.

## 3.34 Spicoli TK 1.0.2

### 3.34.1 New features

• The user is no longer required to call OEInitSurfaceHandlers in order to attach surfaces to molecules and then write them out to OEB. This occurs at library link time now.

### 3.34.2 Minor bug fixes

- OESurface.operator=now copies the OEBase data.
- · OEMakeCliqueSurface and OESurfaceCropToClique now preserve OEBase data.

## 3.35 Spicoli TK 1.0.1

### 3.35.1 Bug fixes

- OEInvert Surface properly inverts all surface normals.
- OEMakeCavitySurfaces was totally busted before. Added a default resolution of 0.5.
- Added a default resolution of 0.5 to OEMakeComplexCavities.
- OEMakeBoxSurface now takes a const float \* as it should.

# **COPYRIGHT AND TRADEMARKS**

© 1997-2024 Cadence Design Systems, Inc. (Cadence), 2655 Seely Ave., San Jose, CA 95134, USA. All rights reserved.

OpenEye, Lexichem, ROCS, Grapheme, and Orion are registered trademarks of Cadence Design Systems, Inc.

This material contains proprietary information of Cadence Design Systems, Inc. Use of copyright notice is precautionary only and does not imply publication or disclosure.

The information supplied in this document is believed to be true, but no liability is assumed for its use or the infringement of the rights of others resulting from its use. Information in this document is subject to change without notice and does not represent a commitment on the part of Cadence Design Systems, Inc.

This package is sold/licensed/distributed subject to the condition that it shall not, by way of trade or otherwise, be lent, re-sold, hired out, or otherwise circulated without Cadence Design Systems' prior consent, in any form of packaging or cover other than that in which it was produced. No part of this manual or accompanying documentation, may be reproduced, stored in a retrieval system on optical or magnetic disk, tape, CD, DVD or other medium, or transmitted in any form or by any means, electronic, mechanical, photocopying recording, or otherwise for any purpose other than for the purchaser's personal use without a legal agreement or other written permission granted by Cadence.

This product should not be used in the planning, construction, maintenance, operation or use of any nuclear facility nor the flight, navigation, or communication of aircraft or ground support equipment. Cadence Design Systems, Inc., shall not be liable, in whole or in part, for any claims arising from such use, including death, bankruptcy or outbreak of war.

Windows is a registered trademark of Microsoft Corporation. Apple, OS X, macOS, and Macintosh are registered trademarks of Apple Inc. UNIX is a registered trademark of the Open Group. Linux is a registered trademark of Linus Torvalds. Red Hat is a registered trademark of Red Hat, Inc. SUSE, SLED, and SLES are registered trademarks of Novell, Inc. Ubuntu is a registered trademark of Canonical Ltd.

SYBYL is a registered trademark of Certara, L.P. MDL, BIOVIA and ISIS are registered trademarks of Dassault Systemes and/or its affiliates. SMARTS and SMIRKS are registered trademarks of Daylight Chemical Information Systems, Inc. MacroModel is a registered trademark of Schrodinger, LLC.

Python is a registered trademark of the Python Software Foundation. Diango is a registered trademark of the Diango Software Foundation. Java is a registered trademark of Oracle and/or its affiliates.

Other products and software packages referenced in this document are trademarks and registered trademarks of their respective vendors or manufacturers.

### **CHAPTER**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

#### **CHAPTER**

## **SIX**

# **CITATION**

## 6.1 Orion<sup>®</sup> Floes

To cite use of an Orion-based Floe package, please use the following:

```
OpenEye <package-name> <version-number>. OpenEye, Cadence Molecular Sciences, Santa
-Fe, NM. http://www.eyesopen.com.
```

#### For example:

```
OpenEye Classic Floes 0.11.2. OpenEye, Cadence Molecular Sciences, Santa Fe, NM.
\rightarrowhttp://www.eyesopen.com.
```

The version number for a Floe package is displayed on the first page of the package's release notes. For example: https://docs.eyesopen.com/floe/modules/classic-floes/docs/source/releasenotes.html.

## **6.2 Toolkits and Applications**

To cite OpenEye toolkits or applications used in your work, please use the following:

```
OpenEye Toolkits [or Applications] <version-number>. OpenEye, Cadence Molecular.
Sciences, Santa Fe, NM. http://www.eyesopen.com.
```

For example:

```
OpenEye Toolkits 2023.1. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://
→ www.eyesopen.com.
```

The Applications and Toolkits are released as a package, multiple times per year. The first part of the version number designates the calendar year. The version number appears on the summary document for the package.

If you want to cite an individual application or toolkit, you can use the syntax:

```
<product name> <version-number>. OpenEye, Cadence Molecular Sciences, Santa Fe, NM.
→http://www.eyesopen.com.
```

where  $<$ *product name* $>$  is:

- $\bullet$  OEChem TK
- OEDepict TK
- FastROCS TK

- Grapheme TK
- GraphSim TK
- Lexichem TK
- OEMedChem TK
- MolProp TK
- Quacpac TK
- OEFF TK
- OEDocking TK
- Omega TK
- Shape TK
- Spicoli TK
- Spruce TK
- Szmap TK
- Szybki TK
- Zap TK
- AFITT Application
- BROOD Application
- EON Application
- OEDocking Application
- OMEGA Application
- PICTO Application
- pKa-Prospector Application
- QUACPAC Application
- ROCS Application
- SiteHopper Application
- SPRUCE Application
- SZMAP Application
- SZYBKI Application
- VIDA Application

You can use the version number of the individual Application or Toolkit. For example:

```
SZYBKI Application 2.5.1.2. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://
→www.eyesopen.com.
Szybki TK 2.5.1.2. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://www.
→eyesopen.com.
```

The first documentation pages give the product names and version numbers, as in https://docs.eyesopen.com/ applications/szybki/index.html and https://docs.eyesopen.com/toolkits/python/szybkitk/index.html.

## **6.3 OpenEye Web Services**

To cite use of the Macromolecular Data Service (MMDS) web service, please use the syntax:

Macromolecular Data Service <version-number>. OpenEye, Cadence Molecular Sciences, -Santa Fe, NM. http://www.eyesopen.com.

#### For example:

Macromolecular Data Service 1.1. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. →http://www.eyesopen.com.

The MMDS version number appears on the web service's release notes.

To cite use of the FastROCS  $^{TM}$  server, please use the syntax:

FastROCS <version-number>. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http:// →www.eyesopen.com.

#### For example:

```
FastROCS 1.4.4. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://www.
⇔eyesopen.com.
```

The FastROCS version number appears on the web service's release notes.

To cite use of the Molecules as a Service (MaaS) web service, please use the syntax:

MaaS <version-number>. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://www. →eyesopen.com.

#### For example:

MaaS 1.0. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://www.eyesopen.com.

The MaaS version number appears on the web service's release notes.

### **CHAPTER**

# **SEVEN**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                                             | License                                                            |
|-------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                                | https://                                                           |
| absl-py                       | https://github.com/abseil/abseil-py                                                 | https://                                                           |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                                 | https://                                                           |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                               | https://                                                           |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                               | N/A                                                                |
| AmberUtils                    | http://ambermd.org                                                                  | N/A                                                                |
| ambit                         | https://github.com/khimaros/ambit                                                   | https://                                                           |
| amqp                          | https://github.com/celery/py-amqp                                                   | https://                                                           |
| anaconda-anon-usage           | Orion Floes                                                                         | https://                                                           |
| angular                       | https://github.com/angular/angular.js                                               | https://                                                           |
| angular-animate               | https://github.com/angular/angular.js                                               | https://                                                           |
| angular-cache                 | https://github.com/jmdobry/angular-cache                                            | https://                                                           |
| angular-cookies               | https://github.com/angular/angular.js                                               | https://                                                           |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                                    | https://                                                           |
| angular-mocks                 | https://github.com/angular/angular.js                                               | https://                                                           |
| angular-resource              | https://github.com/angular/angular.js                                               | https://                                                           |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                                    | https://                                                           |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                               | https://                                                           |
| angular-ui-router             | https://github.com/angular-ui/ui-router                                             | https://                                                           |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                                  | https://                                                           |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                                        | https://                                                           |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                                            | https://                                                           |
| annotated-types               | https://github.com/annotated-types/annotated-types                                  | https://                                                           |
| anyio                         | https://github.com/agronholm/anyio                                                  | https://                                                           |
| appdirs                       | http://github.com/ActiveState/appdirs                                               | http://                                                            |
| appengine                     | https://google.golang.org/appengine                                                 | https://                                                           |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                                   | https://                                                           |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md                          | https://                                                           |
|                               |                                                                                     | J)                                                                 |
| Name of Project               | Website                                                                             | Licen                                                              |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                | https:/                                                            |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                       | https:/                                                            |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                          | https:/                                                            |
| $\overline{ascii85}$          | https://github.com/huandu/node-ascii85                                              | https:/                                                            |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                      | https:/                                                            |
| asgiref                       | https://github.com/django/asgiref/                                                  | https:/                                                            |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                                 | https:/                                                            |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render               | https:/                                                            |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers                   | https:/                                                            |
| assertions                    | https://github.com/smartystreets/assertions                                         | https:/                                                            |
| asttokens                     | https://github.com/gristlabs/asttokens                                              | https:/                                                            |
| astunparse                    | https://github.com/simonpercivall/astunparse                                        | https:/                                                            |
| async-lru                     | https://github.com/aio-libs/async-lru                                               | https:/                                                            |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                           | https:/                                                            |
| $atk-1.0$                     | https://docs.gtk.org/atk/                                                           | https:/                                                            |
| atomic                        | https://github.com/uber-go/atomic                                                   | https:/                                                            |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                    | https:/                                                            |
| attrs                         | https://www.attrs.org/                                                              | https:/                                                            |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                                   | https:/                                                            |
| <b>Babel</b>                  | https://github.com/python-babel/babel                                               | https:/                                                            |
| backcall                      | https://github.com/takluyver/backcall                                               | https:/                                                            |
| backports                     | https://github.com/brandon-rhodes/backports                                         | https:/                                                            |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                             | https:/                                                            |
| base62                        | https://github.com/kare/base62                                                      | https:/                                                            |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                      | https:/                                                            |
| billiard                      | https://github.com/celery/billiard                                                  | https:/                                                            |
| biopython                     | https://biopython.org                                                               |                                                                    |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https:/                                                            |
| bitset                        | https://github.com/willf/bitset                                                     | https:/                                                            |
|                               |                                                                                     | https:/                                                            |
| blas                          | https://www.netlib.org/blas/                                                        | https:/                                                            |
| bleach                        | https://github.com/mozilla/bleach                                                   | https:/                                                            |
| blessings                     | https://github.com/erikrose/blessings                                               | https:/                                                            |
| blinker                       | https://pythonhosted.org/blinker/                                                   | https:/                                                            |
| blosc                         | https://github.com/Blosc/python-blosc                                               | https:/                                                            |
| blosc2                        | https://github.com/Blosc/python-blosc2                                              | https:/                                                            |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https:/                                                            |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                            |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                            |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                                            |
| boto3                         | https://github.com/boto/boto3                                                       | https:/                                                            |
| botocore                      | https://github.com/boto/botocore                                                    | https:/                                                            |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                                            |
| <b>Brotli</b>                 | https://github.com/google/brotli                                                    | https:/                                                            |
| brotli-bin                    | https://github.com/google/brotli                                                    | https:/                                                            |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                                            |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                          | https:/                                                            |
| bson                          | http://github.com/py-bson/bson                                                      | https:/                                                            |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https:/                                                            |
| bzip2                         | https://www.bzip.org                                                                | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| c-ares                        | https://github.com/c-ares/c-ares                                                    | https:/                                                            |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/                                                            |
| cached-property               | https://github.com/pydanny/cached-property                                          | https:/                                                            |
| cachetools                    | https://github.com/tkem/cachetools                                                  | https:/                                                            |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           | https:/                                                            |
| canvas                        | https://github.com/Automattic/node-canvas                                           | https:/                                                            |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              | https:/                                                            |
| celery                        | https://github.com/celery/celery                                                    | https:/                                                            |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         | https:/                                                            |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                           | https:/                                                            |
| cffi                          | https://github.com/python-cffi/cffi                                                 | https:/                                                            |
| cftime                        | https://pypi.org/project/cftime/                                                    | https:/                                                            |
| chardet                       | https://github.com/chardet/chardet                                                  | https:/                                                            |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        | https:/                                                            |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             | https:/                                                            |
| click                         | https://palletsprojects.com/p/click/                                                | https:/                                                            |
| click-completion              | https://github.com/click-contrib/click-completion                                   | https:/                                                            |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   | https:/                                                            |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      | https:/                                                            |
| click-repl                    | https://github.com/untitaker/click-repl                                             | https:/                                                            |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            | https:/                                                            |
| cmake                         | https://cmake.org/                                                                  | https:/                                                            |
| colorama                      | https://github.com/tartley/colorama                                                 | https:/                                                            |
| comm                          | https://github.com/ipython/comm                                                     | https:/                                                            |
| compose                       | https://github.com/docker/compose                                                   | https:/                                                            |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        | https:/                                                            |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      | https:/                                                            |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     | https:/                                                            |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/                                                            |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           | https:/                                                            |
| confuse                       | https://github.com/beetbox/confuse                                                  | https:/                                                            |
| contourpy                     | https://github.com/contourpy/contourpy                                              | https:/                                                            |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               | https:/                                                            |
| cryptography                  | https://github.com/pyca/cryptography                                                | https:/                                                            |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                                | https:/                                                            |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           | https:/                                                            |
| cupy-cuda113                  | https://cupy.dev/                                                                   | https:/                                                            |
| curl                          | https://curl.se                                                                     | https:/                                                            |
| cycler                        | https://github.com/matplotlib/cycler                                                | https:/                                                            |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             | https:/                                                            |
| Cython                        | https://cython.org                                                                  | https:/                                                            |
| d3                            | https://github.com/mbostock/d3                                                      | https:/                                                            |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           | https:/                                                            |
| ddsketch                      | https://github.com/datadog/sketches-py                                              | https:/                                                            |
| debugpy                       | https://aka.ms/debugpy                                                              | https:/                                                            |
| decimal                       | https://github.com/shopspring/decimal                                               | https:/                                                            |
| decorator                     | https://github.com/micheles/decorator                                               | https:/                                                            |
| deepdiff                      | https://github.com/seperman/deepdiff                                                | https:/                                                            |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             | https:/                                                            |
|                               |                                                                                     | J.                                                                 |
| Name of Project               | Website                                                                             | Licen                                                              |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https:/                                                            |
| $di$ <sup>111</sup>           | https://github.com/uqfoundation/dill                                                | https:/                                                            |
| distro                        | <b>Orion Floes</b>                                                                  | https:/                                                            |
| Django                        | https://www.djangoproject.com/                                                      | https:/                                                            |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                    | https:/                                                            |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                   | https:/                                                            |
| django-csp                    | https://github.com/mozilla/django-csp                                               | https:/                                                            |
| django-extensions             | https://github.com/django-extensions/django-extensions                              | https:/                                                            |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                          | https:/                                                            |
| django-redis                  | https://github.com/jazzband/django-redis                                            | https:/                                                            |
| django-taggit                 | https://github.com/jazzband/django-taggit                                           | https:/                                                            |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/                                                            |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                              | https:/                                                            |
| djangorestframework           | https://www.django-rest-framework.org/                                              | https:/                                                            |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                      | https:/                                                            |
| dm-tree                       | https://github.com/deepmind/tree                                                    | https:/                                                            |
| docker-py                     | https://github.com/docker/docker-py/                                                | https:/                                                            |
| docopt                        | https://docopt.org                                                                  | https:/                                                            |
| docutils                      | https://docutils.sourceforge.io                                                     | https:/                                                            |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/                                                            |
| editdistance                  | https://github.com/roy-ht/editdistance                                              | https:/                                                            |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/                                                            |
| einops                        | https://github.com/arogozhnikov/einops                                              | https:/                                                            |
| entrypoints                   | https://github.com/takluyver/entrypoints                                            | https:/                                                            |
| errors                        | https://github.com/pkg/errors                                                       | https:/                                                            |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                            |
| $et$ <sub>_</sub> xmlfile     | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/                                                            |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         |                                                                    |
| executing                     | https://github.com/alexmojaki/executing                                             | https:/                                                            |
|                               | https://libexpat.github.io                                                          | https:/<br>https:/                                                 |
| expat<br>fastjsonschema       | https://github.com/horejsek/python-fastjsonschema                                   | https:/                                                            |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 |                                                                    |
| fftw                          | https://www.fftw.org                                                                | https:/<br>comm                                                    |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              |                                                                    |
|                               |                                                                                     | https:/                                                            |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/                                                            |
| finufft                       | https://github.com/flatironinstitute/finufft                                        | https:/                                                            |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/                                                            |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               | https:/                                                            |
| flit-core                     | https://github.com/pypa/flit                                                        | https:/                                                            |
| <b>FLTK</b>                   | https://www.fltk.org/index.php                                                      | https:/                                                            |
| fmt                           | https://fmt.dev/latest/index.html                                                   | https:/                                                            |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         | https:/                                                            |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      | https:/                                                            |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       | https:/                                                            |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/                                                            |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            | https:/                                                            |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/                                                            |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/                                                            |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https:/                                                            |
| freetype                      | https://freetype.org                                                                | https:/                                                            |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https:/                                                            |
| frozendict                    | Orion Floes                                                                         | https:/                                                            |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                              | https:/                                                            |
| fsmlite                       | https://github.com/tkem/fsmlite                                                     | https:/                                                            |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                           | https:/                                                            |
| funcy                         | https://github.com/Suor/funcy                                                       | https:/                                                            |
| gast                          | https://github.com/serge-sans-paille/gast/                                          | https:/                                                            |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                | https:/                                                            |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             | https:/                                                            |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https:/                                                            |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             | https:/                                                            |
| genproto                      | https://google.golang.org/genproto/googleapis                                       | https:/                                                            |
| geometric                     | https://openbase.com/python/geometric                                               | https:/                                                            |
| giflib                        | https://giflib.sourceforge.net                                                      | https:/                                                            |
| glib                          | https://docs.gtk.org/glib/                                                          | https:/                                                            |
| GLM Library                   | https://github.com/g-truc/glm                                                       | https:/                                                            |
| gls                           | https://github.com/jtolds/gls                                                       | https:/                                                            |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https:/                                                            |
| go-connections                | https://github.com/docker/go-connections                                            | https:/                                                            |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https:/                                                            |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https:/                                                            |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https:/                                                            |
| go-ini                        | https://github.com/go-ini/ini                                                       | https:/                                                            |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             | https:/                                                            |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https:/                                                            |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           | https:/                                                            |
| go-ole                        | https://github.com/go-ole/go-ole                                                    | https:/                                                            |
| go-pg                         | https://github.com/go-pg/pg                                                         | https:/                                                            |
| go-redis                      | https://github.com/go-redis/redis/v8                                                | https:/                                                            |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                            | https:/                                                            |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                            | https:/                                                            |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                              | https:/                                                            |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                                   | https:/                                                            |
| go-units                      | https://github.com/docker/go-units                                                  | https:/                                                            |
| go-version                    | https://github.com/hashicorp/go-version                                             | https:/                                                            |
| go-zglob                      | https://github.com/mattn/go-zglob                                                   | https:/                                                            |
| go.opencensus                 | https://go.opencensus.io                                                            | https:/                                                            |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                | https:/                                                            |
| goconvey                      | https://github.com/smartystreets/goconvey                                           | https:/                                                            |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                       | https:/                                                            |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       | https:/                                                            |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https:/                                                            |
| google-cloud-go               | https://cloud.google.com/go                                                         | https:/                                                            |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 | https:/                                                            |
| google-pasta                  | https://github.com/google/pasta                                                     | https:/                                                            |
| google.golang.org/api         | https://google.golang.org/api                                                       | https:/                                                            |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https:/                                                            |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https:/                                                            |
| graphviz                      | https://graphviz.org/                                                               | https:/                                                            |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https:/                                                            |
| groupcache                    | https://github.com/golang/groupcache                                                | https:/                                                            |
| grpc                          | https://google.golang.org/grpc                                                      | https:/                                                            |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https:/                                                            |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/                                                            |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/                                                            |
| gts                           | https://sourceforge.net/projects/gts/                                               | https:/                                                            |
| h5py                          | https://www.h5py.org                                                                | https:/                                                            |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https:/                                                            |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https:/                                                            |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/                                                            |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/                                                            |
| he                            | https://github.com/mathiasbynens/he                                                 | https:/                                                            |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https:/                                                            |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https:/                                                            |
| htslib                        | https://www.htslib.org                                                              | https:/                                                            |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https:/                                                            |
| icu                           | https://github.com/unicode-org/icu                                                  | https:/                                                            |
| idna                          | https://github.com/kjd/idna                                                         | https:/                                                            |
| imageio                       | https://github.com/imageio/imageio                                                  | https:/                                                            |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https:/                                                            |
| ImmuneBuilder                 | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/                                                            |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https:/                                                            |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https:/                                                            |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/                                                            |
| inflection                    | https://github.com/jinzhu/inflection                                                | https:/                                                            |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https:/                                                            |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https:/                                                            |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https:/                                                            |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https:/                                                            |
| ipykernel                     | https://ipython.org                                                                 | https:/                                                            |
| ipython                       | https://ipython.org                                                                 | https:/                                                            |
| ipython-genutils              | http://ipython.org                                                                  | https:/                                                            |
| ipywidgets                    | http://jupyter.org                                                                  | https:/                                                            |
| isodate                       | https://github.com/gweis/isodate/                                                   | https:/                                                            |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https:/                                                            |
| jax                           | https://github.com/google/jax                                                       | https:/                                                            |
| jaxlib                        | https://github.com/google/jax                                                       | https:/                                                            |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              | https:/                                                            |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https:/                                                            |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https:/                                                            |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https:/                                                            |
| jpeg                          | https://www.ijg.org                                                                 | https:/                                                            |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https:/                                                            |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https:/                                                            |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:/                                                            |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https:                                                             |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https:                                                             |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:                                                             |
| jstat                         | https://github.com/jstat/jstat                                                      | https:                                                             |
| jupyter-client                | https://jupyter.org                                                                 | https:                                                             |
| jupyter-core                  | https://jupyter.org                                                                 | https:                                                             |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https:                                                             |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:                                                             |
| jupyter-server                | http://jupyter.org                                                                  | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:                                                             |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:                                                             |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:                                                             |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:                                                             |
| jupyter_client                | http://jupyter.org                                                                  | https:                                                             |
| jupyter_core                  | http://jupyter.org                                                                  | https:                                                             |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https:                                                             |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:                                                             |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:                                                             |
| keras                         | https://github.com/keras-team/keras                                                 | https:                                                             |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:                                                             |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:                                                             |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:                                                             |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:                                                             |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:                                                             |
| kombu                         | https://kombu.readthedocs.io                                                        | https:                                                             |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                       | https:                                                             |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:                                                             |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:                                                             |
| lcms2                         | https://www.littlecms.com                                                           | https:                                                             |
| lerc                          | https://github.com/Esri/lerc                                                        | https:                                                             |
| libarchive                    | http://www.libarchive.org                                                           | https:                                                             |
| libblas                       | https://www.netlib.org/blas/                                                        | https:                                                             |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:                                                             |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:                                                             |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https:/                                                            |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                |
| libclang                      | <b>Orion Floes</b>                                                                  | https:                                                             |
| libcurl                       | https://curl.se/libcurl/                                                            | https:/                                                            |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:                                                             |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:                                                             |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              |                                                                    |
| libedit                       | https://thrysoee.dk/editline/                                                       | https:                                                             |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | http://                                                            |
| libffi                        | https://github.com/libffi/libffi                                                    | https:                                                             |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:                                                             |
| libgd                         | https://libgd.github.io                                                             | https:                                                             |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:                                                             |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https:                                                             |
| Name of Project               | Website                                                                             | License                                                            |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https://                                                           |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https://                                                           |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https://                                                           |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https://                                                           |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https://                                                           |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                           |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https://                                                           |
| libopenblas                   | https://www.openblas.net/                                                           | https://                                                           |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https://                                                           |
| libpq                         | https://www.postgresql.org/                                                         | https://                                                           |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https://                                                           |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https://                                                           |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https://                                                           |
| libtiff                       | https://www.libtiff.org/                                                            | https://                                                           |
| libtrust                      | https://github.com/docker/libtrust                                                  | https://                                                           |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https://                                                           |
| libuv                         | https://github.com/libuv/libuv                                                      | https://                                                           |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https://                                                           |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https://                                                           |
| libxc                         | https://www.tddft.org/programs/libxc/                                               | https://                                                           |
| libxcb                        | https://xcb.freedesktop.org                                                         | https://                                                           |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https://                                                           |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https://                                                           |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https://                                                           |
| libzlib                       | https://zlib.net                                                                    | https://                                                           |
| lime                          | https://github.com/marcotcr/lime                                                    | https://                                                           |
| llvm                          | http://llvm.org                                                                     | https://                                                           |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https://                                                           |
| llvmlite                      | http://llvmlite.readthedocs.io                                                      | https://                                                           |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https://                                                           |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https://                                                           |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https://                                                           |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https://                                                           |
| lxml                          | https://lxml.de                                                                     | https://                                                           |
| lz4-c                         | https://www.lz4.org/                                                                | https://                                                           |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https://                                                           |
| markdown-it-py                | Orion Floes                                                                         | https://                                                           |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https://                                                           |
| matplotlib                    | https://matplotlib.org                                                              | https://                                                           |
| matplotlib-base               | https://matplotlib.org                                                              | https://                                                           |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https://                                                           |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https://                                                           |
| mdtraj                        | https://www.mdtraj.org/                                                             | https://                                                           |
| mdurl                         | Orion Floes                                                                         | https://                                                           |
| menuinst                      | Orion Floes                                                                         | https://                                                           |
| mergo                         | https://github.com/imdario/mergo                                                    | https://                                                           |
| mistune                       | https://github.com/lepture/mistune                                                  | https://                                                           |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https://                                                           |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https://                                                           |
|                               |                                                                                     | J.                                                                 |
| Name of Project               | Website                                                                             | Licen                                                              |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https:/                                                            |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https:/                                                            |
| ml-dtypes                     | <b>Orion Floes</b>                                                                  | https:/                                                            |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https:/                                                            |
| moment                        | https://github.com/moment/moment                                                    | https:/                                                            |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https:/                                                            |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https:/                                                            |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https:/                                                            |
| mpmath                        | http://mpmath.org/                                                                  | https:/                                                            |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https:/                                                            |
| msgpack                       | https://msgpack.org/                                                                | https:/                                                            |
| multidict                     | https://github.com/aio-libs/multidict                                               | https:/                                                            |
| multierr                      | https://go.uber.org/multierr                                                        | https:/                                                            |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https:/                                                            |
| munkres                       | https://software.clapper.org/munkres/                                               | https:/                                                            |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https:/                                                            |
| namex                         | <b>Orion Floes</b>                                                                  | https:/                                                            |
| nbclassic                     | http://jupyter.org                                                                  | https:/                                                            |
| nbclient                      | https://jupyter.org                                                                 | https:/                                                            |
| nbconvert                     | https://jupyter.org                                                                 | https:/                                                            |
| nbformat                      | http://jupyter.org                                                                  | https:/                                                            |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https:/                                                            |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             |                                                                    |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                            |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https:/                                                            |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https:/                                                            |
|                               | https://networkx.org                                                                | https:/                                                            |
| networkx                      |                                                                                     | https:/                                                            |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https:/                                                            |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https:/                                                            |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https:/                                                            |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https:/                                                            |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https:/                                                            |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/                                                            |
| nodejs                        | https://nodejs.org/en/                                                              | https:/                                                            |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https:/                                                            |
| notebook                      | http://jupyter.org                                                                  | https:/                                                            |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https:/                                                            |
| notebook_shim                 | http://jupyter.org                                                                  | https:/                                                            |
| numba                         | https://numba.pydata.org                                                            | https:/                                                            |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https:/                                                            |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https:/                                                            |
| numpy                         | https://numpy.org                                                                   | https:/                                                            |
| numpy-base                    | https://numpy.org                                                                   | https:/                                                            |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/                                                            |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                             |
| Oat++                         | https://oatpp.io/                                                                   | https://oatpp.io/                                                  |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https://github.com/oauthlib/oauthlib                               |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https://github.com/OCL-dev/ocl-icd                                 |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https://github.com/conda-forge/ocl-icd-system-feedstock            |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https://www.decalage.info/python/olefileio                         |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               |                                                                    |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https://omnicanvas.readthedocs.io/en/latest/                       |
| OpenFF                        | https://openforcefield.org/                                                         | https://openforcefield.org/                                        |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https://github.com/openforcefield/openff-amber-ff-ports            |
| openff-forcefields            | https://openforcefield.org                                                          | https://openforcefield.org                                         |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https://github.com/openforcefield/openff-interchange               |
| openff-models                 | https://github.com/openforcefield/openff-models                                     | https://github.com/openforcefield/openff-models                    |
| openff-toolkit                | https://openforcefield.org                                                          | https://openforcefield.org                                         |
| openff-toolkit-base           | https://openforcefield.org                                                          | https://openforcefield.org                                         |
| openff-units                  | https://github.com/openforcefield/openff-units                                      | https://github.com/openforcefield/openff-units                     |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https://github.com/openforcefield/openff-utilities                 |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https://github.com/uclouvain/openjpeg                              |
| openldap                      | https://www.openldap.org/software/repo.html                                         | https://www.openldap.org/software/repo.html                        |
| OpenMM                        | https://openmm.org                                                                  | https://openmm.org                                                 |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https://github.com/choderalab/openmmtools                          |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https://github.com/choderalab/openmoltools                         |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https://openpyxl.readthedocs.io/en/stable/                         |
| openssl                       | https://www.openssl.org                                                             | https://www.openssl.org                                            |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https://github.com/dgasmith/opt_einsum                             |
| OptKing                       | https://github.com/psi-rking/optking                                                | https://github.com/psi-rking/optking                               |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https://github.com/wbond/oscrypto                                  |
| overrides                     | https://github.com/mkorpela/overrides                                               | https://github.com/mkorpela/overrides                              |
| packaging                     | https://github.com/pypa/packaging                                                   | https://github.com/pypa/packaging                                  |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml              |
| pandas                        | https://pandas.pydata.org                                                           | https://pandas.pydata.org                                          |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | http://github.com/jgm/pandocfilters                                |

| Name of Project   | Website                                                 |
|-------------------|---------------------------------------------------------|
| panedr            | https://github.com/MDAnalysis/panedr                    |
| pango             | https://pango.gnome.org                                 |
| ParmEd            | https://parmed.github.io/ParmEd/html/index.html         |
| parser            | https://github.com/typescript-eslint/typescript-eslint  |
| parso             | https://parso.readthedocs.io/en/latest/                 |
| pathos            | https://github.com/uqfoundation/pathos                  |
| patsy             | https://patsy.readthedocs.io/en/latest/                 |
| pbkdf2            | https://golang.org/x/crypto/pbkdf2                      |
| pbr               | https://docs.openstack.org/pbr/latest/                  |
| pcmsolver         | https://pcmsolver.readthedocs.io/en/stable/             |
| pcre              | https://www.pcre.org                                    |
| pcre2             | https://www.pcre.org                                    |
| pdb4amber         | https://github.com/Amber-MD/pdb4amber                   |
| pdbfixer          | https://github.com/openmm/pdbfixer                      |
| pexpect           | https://pexpect.readthedocs.io/                         |
| pgconn            | https://github.com/jackc/pgconn                         |
| pgio              | https://github.com/jackc/pgio                           |
| pgpassfile        | https://github.com/jackc/pgpassfile                     |
| pgproto3          | https://github.com/jackc/pgproto3/v2                    |
| pgtype            | https://github.com/jackc/pgtype                         |
| pgx               | https://github.com/jackc/pgx/v4                         |
| phonopy           | https://github.com/phonopy/phono3py                     |
| pickleshare       | https://github.com/pickleshare/pickleshare              |
| Pillow            | https://python-pillow.org                               |
| Pint              | https://pint.readthedocs.io/en/stable/                  |
| pip               | https://pip.pypa.io/                                    |
| pip-licenses      | https://github.com/raimon49/pip-licenses                |
| pixman            | https://pixman.org                                      |
| pkginfo           | https://launchpad.net/pkginfo                           |
| platformdirs      | https://github.com/platformdirs/platformdirs            |
| plotly            | https://plotly.com/python/                              |
| plotly-orca       | https://github.com/plotly/orca                          |
| plotly.js         | https://github.com/plotly/plotly.js                     |
| pluggy            | https://pluggy.readthedocs.io/en/stable/index.html      |
| pooch             | https://github.com/fatiando/pooch                       |
| pox               | https://github.com/uqfoundation/pox                     |
| ppft              | https://github.com/uqfoundation/ppft                    |
| pq                | https://github.com/lib/pq                               |
| ProDy             | http://www.csb.pitt.edu/ProDy                           |
| prometheus-client | https://github.com/prometheus/client_python             |
| prompt-toolkit    | https://python-prompt-toolkit.readthedocs.io/en/stable/ |
| protobuf          | https://google.golang.org/protobuf                      |
| psi4              | https://psicode.org                                     |
| psutil            | https://psutil.readthedocs.io/en/latest/                |
| psycopg2          | https://psycopg.org/                                    |
| PTable            | https://github.com/kxxoling/PTable                      |
| pthread-stubs     | https://xcb.freedesktop.org                             |
| ptyprocess        | https://ptyprocess.readthedocs.io/en/latest/            |
| pure-eval         | http://github.com/alexmojaki/pure_eval                  |

|                               |                                                                  | Ŀ                                                                               |
|-------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------|
| Name of Project               | Website                                                          | Licen                                                                           |
| pу                            | https://py.readthedocs.io/en/latest/                             | https:/                                                                         |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                          | https:/                                                                         |
| pyasn1                        | https://github.com/etingof/pyasn1                                | https:/                                                                         |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                        | https:/                                                                         |
| pybind11-abi                  | https://github.com/pybind/pybind11                               | https:/                                                                         |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html              | https:/                                                                         |
| pycosat                       | https://github.com/conda/pycosat                                 | https:/                                                                         |
| pycparser                     | https://github.com/eliben/pycparser                              | https:/                                                                         |
| pydantic                      | https://pydantic-docs.helpmanual.io                              | https:/                                                                         |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                        | https:/                                                                         |
| pyedr                         | https://github.com/MDAnalysis/panedr                             | https:/                                                                         |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                             | https:/                                                                         |
| Pygments                      | https://pygments.org                                             | https:/                                                                         |
| pygraphviz                    | https://pygraphviz.github.io                                     | https:/                                                                         |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                         | https:/                                                                         |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                     | https:/                                                                         |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator               | https:/                                                                         |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                | https:/                                                                         |
| pymbar                        | https://pymbar.org                                               | https:/                                                                         |
| pyOpenSSL                     | https://pyopenssl.org/                                           | https:/                                                                         |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                 | https:/                                                                         |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                 | https:/                                                                         |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                              | https:/                                                                         |
| pysam                         | https://github.com/pysam-developers/pysam                        | https:/                                                                         |
| PySocks                       | https://github.com/Anorov/PySocks                                | https:/                                                                         |
| pytables                      | https://www.pytables.org                                         | https:/                                                                         |
| python                        | https://www.python.org/                                          | https:/                                                                         |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                       | https:/                                                                         |
| python-constraint             | https://github.com/python-constraint/python-constraint           | https:/                                                                         |
| python-dateutil               | https://dateutil.readthedocs.io                                  | https:/                                                                         |
| python-json-logger            | http://github.com/madzak/python-json-logger                      | https:/                                                                         |
| python-Idap                   | https://www.python-ldap.org/                                     | https:/                                                                         |
| python3-saml                  | https://github.com/onelogin/python3-saml                         | https:/                                                                         |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock              | https:/                                                                         |
| pytz                          | https://pythonhosted.org/pytz                                    | https:/                                                                         |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                | https:/                                                                         |
| PyWavelets                    | https://github.com/PyWavelets/pywt                               | https:/                                                                         |
| <b>PyYAML</b>                 | https://pyyaml.org/                                              | https:/                                                                         |
| pyyml                         | No longer available                                              | No lor                                                                          |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                          | https:/                                                                         |
| qcelemental                   | https://github.com/MolSSI/QCElemental                            | https:/                                                                         |
|                               | https://github.com/MolSSI/QCEngine                               |                                                                                 |
| qcengine                      | https://github.com/lincolnloop/python-qrcode                     | https:/                                                                         |
| qrcode                        |                                                                  | https:/                                                                         |
| ramda                         | https://github.com/ramda/ramda                                   | https:/                                                                         |
| rapidjson                     | https://rapidjson.org/                                           | https:/                                                                         |
| rdkit                         | https://www.rdkit.org                                            | https:/                                                                         |
| re2                           | https://github.com/google/re2                                    | https:/                                                                         |
| readme-renderer               | https://github.com/pypa/readme_renderer                          | https:/                                                                         |
| redis-py                      | https://github.com/andymccurdy/redis-py                          | https:/                                                                         |
| Name of Project               | Website                                                          | License                                                                         |
| referencing                   | https://github.com/python-jsonschema/referencing                 | https://github.com/python-jsonschema/referencing/blob/main/LICENSE              |
| regex                         | https://github.com/mrabarnett/mrab-regex                         | https://github.com/mrabarnett/mrab-regex/blob/main/LICENSE                      |
| reportlab                     | https://www.reportlab.com                                        | https://www.reportlab.com/dev/doc/license.html                                  |
| reproc                        | https://github.com/DaanDeMeyer/reproc                            | https://github.com/DaanDeMeyer/reproc/blob/master/LICENSE                       |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                            | https://github.com/DaanDeMeyer/reproc/blob/master/LICENSE                       |
| requests                      | https://requests.readthedocs.io                                  | https://github.com/psf/requests/blob/main/LICENSE                               |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                    | https://github.com/requests/requests-oauthlib/blob/master/LICENSE               |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                 | https://github.com/requests/toolbelt/blob/master/LICENSE                        |
| resumable                     | https://github.com/stevvooe/resumable                            | https://github.com/stevvooe/resumable/blob/master/LICENSE                       |
| retrying                      | https://github.com/rholder/retrying                              | https://github.com/rholder/retrying/blob/master/LICENSE                         |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                    | https://github.com/naimetti/rfc3339-validator/blob/main/LICENSE                 |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                        | https://github.com/python-hyper/rfc3986/blob/main/LICENSE                       |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                    | https://github.com/naimetti/rfc3986-validator/blob/main/LICENSE                 |
| rich                          | https://github.com/Textualize/rich                               | https://github.com/Textualize/rich/blob/master/LICENSE                          |
| rpds-py                       | https://github.com/crate-py/rpds                                 | https://github.com/crate-py/rpds/blob/main/LICENSE                              |
| rpmpack                       | https://github.com/google/rpmpack                                | https://github.com/google/rpmpack/blob/master/LICENSE                           |
| rsa                           | https://stuvel.eu/rsa                                            | https://github.com/sybrenstuvel/python-rsa/blob/master/LICENSE                  |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/      | https://bitbucket.org/ruamel/yaml/src/default/LICENSE                           |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/ | https://bitbucket.org/ruamel/yaml.clib/src/default/LICENSE                      |
| s3transfer                    | https://github.com/boto/s3transfer                               | https://github.com/boto/s3transfer/blob/develop/LICENSE                         |
| sasl                          | https://mellium.im/sasl                                          | https://github.com/mellium/sasl/blob/master/LICENSE                             |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                        | https://github.com/mmaelicke/scikit-gstat/blob/master/LICENSE                   |
| scikit-image                  | https://scikit-image.org                                         | https://github.com/scikit-image/scikit-image/blob/main/LICENSE.txt              |
| scikit-learn                  | https://scikit-learn.org/stable/                                 | https://github.com/scikit-learn/scikit-learn/blob/main/COPYING                  |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra       | https://github.com/scikit-learn-contrib/scikit-learn-extra/blob/master/LICENSE  |
| scipy                         | https://scipy.org                                                | https://github.com/scipy/scipy/blob/main/LICENSE.txt                            |
| seaborn                       | https://seaborn.pydata.org                                       | https://github.com/mwaskom/seaborn/blob/master/LICENSE                          |
| seaborn-base                  | https://seaborn.pydata.org                                       | https://github.com/mwaskom/seaborn/blob/master/LICENSE                          |
| semver                        | https://github.com/Masterminds/semver/v3                         | https://github.com/Masterminds/semver/blob/master/LICENSE                       |
| Send2Trash                    | https://github.com/arsenetar/send2trash                          | https://github.com/arsenetar/send2trash/blob/master/LICENSE                     |
| setuptools                    | https://github.com/pypa/setuptools                               | https://github.com/pypa/setuptools/blob/main/LICENSE                            |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                          | https://github.com/pypa/setuptools_scm/blob/master/LICENSE                      |
| sh                            | https://github.com/amoffat/sh                                    | https://github.com/amoffat/sh/blob/master/LICENSE.txt                           |
| shellingham                   | https://github.com/sarugaku/shellingham                          | https://github.com/sarugaku/shellingham/blob/master/LICENSE                     |
| simint                        | https://www.bennyp.org/research/simint/                          | https://github.com/simint/simint/blob/master/LICENSE                            |
| six                           | https://github.com/benjaminp/six                                 | https://github.com/benjaminp/six/blob/master/LICENSE                            |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst               | https://github.com/openforcefield/smirnoff99frosst/blob/main/LICENSE            |
| snappy                        | https://github.com/google/snappy                                 | https://github.com/google/snappy/blob/main/COPYING                              |
| sniffio                       | https://github.com/python-trio/sniffio                           | https://github.com/python-trio/sniffio/blob/master/LICENSE                      |
| snowballstemmer               | https://github.com/snowballstem/snowball                         | https://github.com/snowballstem/snowball/blob/master/COPYING                    |
| soupsieve                     | https://github.com/facelessuser/soupsieve                        | https://github.com/facelessuser/soupsieve/blob/master/LICENSE                   |
| spglib                        | https://github.com/spglib/spglib                                 | https://github.com/spglib/spglib/blob/develop/LICENSE                           |
| sphinx                        | https://github.com/sphinx-doc/sphinx                             | https://github.com/sphinx-doc/sphinx/blob/master/LICENSE                        |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp            | https://github.com/sphinx-doc/sphinxcontrib-applehelp/blob/master/LICENSE       |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp              | https://github.com/sphinx-doc/sphinxcontrib-devhelp/blob/master/LICENSE         |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp             | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp/blob/master/LICENSE        |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath               | https://github.com/sphinx-doc/sphinxcontrib-jsmath/blob/master/LICENSE          |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp               | https://github.com/sphinx-doc/sphinxcontrib-qthelp/blob/master/LICENSE          |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml      | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml/blob/master/LICENSE |
|                               |                                                                  | L                                                                               |
| Name of Project               | Website                                                          | Licen                                                                           |
| SQLAlchemy                    | https://www.sqlalchemy.org                                       | https:/                                                                         |
| sqlite                        | https://sqlite.org/index.html                                    | https:/                                                                         |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                         | https:/                                                                         |
| stack-data                    | http://github.com/alexmojaki/stack_data                          | https:/                                                                         |
| starfile                      | https://github.com/alisterburt/starfile                          | https:/                                                                         |
| statsmodels                   | https://github.com/statsmodels/statsmodels                       | https:/                                                                         |
| structlog                     | https://www.structlog.org/                                       | https:/                                                                         |
| svglib                        | https://github.com/deeplook/svglib                               | https:/                                                                         |
| sympy                         | https://sympy.org                                                | https:/                                                                         |
| tables                        | https://www.pytables.org/                                        | https:/                                                                         |
| tabulate                      | https://github.com/astanin/python-tabulate                       | https:/                                                                         |
| tbb                           | https://github.com/oneapi-src/oneTBB                             | https:/                                                                         |
| tenacity                      | https://github.com/jd/tenacity                                   | https:/                                                                         |
| tensorboard                   | https://github.com/tensorflow/tensorboard                        | https:/                                                                         |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                        | https:/                                                                         |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                        | https:/                                                                         |
| tensorflow                    | https://github.com/tensorflow/tensorflow                         | https:/                                                                         |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                          | https:/                                                                         |
| tensorflow-io-gcs-filesystem  | <b>Orion Floes</b>                                               | https:/                                                                         |
| tensorflow-probability        | https://github.com/tensorflow/probability                        | https:/                                                                         |
| termcolor                     | https://github.com/hugovk/termcolor                              | https:/                                                                         |
| terminado                     | https://github.com/jupyter/terminado                             | https:/                                                                         |
| testpath                      | https://github.com/jupyter/testpath                              | https:/                                                                         |
| textangular                   | https://github.com/fraywing/textAngular                          | https:/                                                                         |
| tf_keras                      | <b>Orion Floes</b>                                               | https:/                                                                         |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                          | https:/                                                                         |
| three                         | https://github.com/mrdoob/three.js                               | https:/                                                                         |
| tifffile                      | https://github.com/cgohlke/tifffile/                             |                                                                                 |
| tinycss2                      | https://github.com/Kozea/tinycss2/                               | https:/                                                                         |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                          | https:/                                                                         |
| tk                            | https://www.tcl.tk/                                              | https:/<br>https:/                                                              |
| toml                          | https://github.com/toml-lang/toml                                |                                                                                 |
|                               | https://github.com/hukkin/tomli                                  | https:/                                                                         |
| tomli                         |                                                                  | https:/                                                                         |
| toolz                         | https://github.com/pytoolz/toolz                                 | https:/                                                                         |
| torch                         | https://pytorch.org/                                             | https:/                                                                         |
| tornado                       | https://www.tornadoweb.org                                       | https:/                                                                         |
| tqdm                          | https://github.com/tqdm/tqdm                                     | https:/                                                                         |
| tracy                         | https://github.com/gear-genomics/tracy                           | https:/                                                                         |
| traitlets                     | https://github.com/ipython/traitlets                             | https:/                                                                         |
| triton                        | https://github.com/openai/triton/                                | https:/                                                                         |
| truststore                    | Orion Floes                                                      | https:/                                                                         |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                            | https:/                                                                         |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                          | https:/                                                                         |
| twine                         | https://github.com/pypa/twine                                    | https:/                                                                         |
| twinj uuid                    | https://github.com/twinj/uuid                                    | https:/                                                                         |
| types                         | https://github.com/babel/babel                                   | https:/                                                                         |
| typescript                    | https://github.com/Microsoft/TypeScript                          | https:/                                                                         |
| typing_extensions             | https://github.com/python/typing                                 | https:/                                                                         |
| tzdata                        | https://github.com/python/tzdata                                 | https:/                                                                         |
|                               |                                                                  | J.                                                                              |
| Name of Project               | Website                                                          | Licen                                                                           |
| tzlocal                       | https://github.com/regebro/tzlocal                               | https:/                                                                         |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                          | https:/                                                                         |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                        | https:/                                                                         |
| uritools                      | https://github.com/tkem/uritools/                                | https:/                                                                         |
| urllib <sub>3</sub>           | https://urllib3.readthedocs.io/                                  | https:/                                                                         |
| vine                          | https://github.com/celery/vine                                   | https:/                                                                         |
| vue                           | https://github.com/vuejs/vue                                     | https:/                                                                         |
| wcwidth                       | https://github.com/jquast/wcwidth                                | https:/                                                                         |
| webencodings                  | https://github.com/gsnedders/python-webencodings                 | https:/                                                                         |
| websocket-client              | https://github.com/websocket-client/websocket-client.git         | https:/                                                                         |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                          | https:/                                                                         |
| westpa                        | <b>Orion Floes</b>                                               | http: $\overline{N}$                                                            |
| wheel                         | https://github.com/pypa/wheel                                    | https:/                                                                         |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme             | https:/                                                                         |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                         | https:/                                                                         |
| wsutil                        | https://github.com/yhat/wsutil                                   | https:/                                                                         |
| x/lint                        | https://golang.org/x/lint                                        | https:/                                                                         |
| x/mod                         | https://golang.org/x/mod/semver                                  | https:/                                                                         |
| x/net                         | https://golang.org/x/net                                         | https:/                                                                         |
| $x/$ oauth2                   | https://golang.org/x/oauth2                                      | https:/                                                                         |
| x/sys                         | https://golang.org/x/sys                                         | https:/                                                                         |
| $x$ /text                     | https://golang.org/x/text                                        | https:/                                                                         |
| x/tools                       | https://golang.org/x/tools                                       | https:/                                                                         |
| x/xerrors                     | https://golang.org/x/xerrors                                     | https:/                                                                         |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                            | https:/                                                                         |
| xlrd                          | https://github.com/python-excel/xlrd                             | https:/                                                                         |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                         | https:/                                                                         |
| xmltodict                     | https://github.com/martinblech/xmltodict                         | https:/                                                                         |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                | https:/                                                                         |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                   | https:/                                                                         |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                    | https:/                                                                         |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                   | https:/                                                                         |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                   | https:/                                                                         |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                 | https:/                                                                         |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                  | https:/                                                                         |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender               | https:/                                                                         |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                    | https:/                                                                         |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto            | https:/                                                                         |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto              | https:/                                                                         |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                 | https:/                                                                         |
| xxhash                        | https://github.com/cespare/xxhash/v2                             | https:/                                                                         |
| $\mathbf{X} \mathbf{Z}$       | https://github.com/ulikunitz/xz                                  | https:/                                                                         |
| yaml                          | https://pyyaml.org/                                              | https:/                                                                         |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                               | https:/                                                                         |
| yaml.v2                       | https://gopkg.in/yaml.v2                                         | https:/                                                                         |
| yaml.v3                       | https://gopkg.in/yaml.v3                                         | https:/                                                                         |
| yarl                          | https://github.com/aio-libs/yarl/                                | https:/                                                                         |
| yaspin                        | https://github.com/pavdmyt/yaspin                                | https:/                                                                         |
| yfiles                        | https://www.yworks.com/products/yfiles                           | comm                                                                            |
|                               |                                                                  |                                                                                 |
| Name of Project               | Website                                                          | License                                                                         |
| yml                           | https://pypi.org/project/yml/                                    | N/A                                                                             |
| zap                           | https://go.uber.org/zap                                          |                                                                                 |
| zipp                          | https://github.com/jaraco/zipp                                   |                                                                                 |
| zlib                          | https://zlib.net/                                                |                                                                                 |
| zstandard                     | https://github.com/indygreg/python-zstandard                     |                                                                                 |
| zstd                          | https://facebook.github.io/zstd/                                 |                                                                                 |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock           |                                                                                 |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock           |                                                                                 |

## **7.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

### **7.1.1 GCC RUNTIME LIBRARY EXCEPTION**

```
Version 3.1, 31 March 2009
Copyright © 2009 Free Software Foundation, Inc. http://fsf.org/
Everyone is permitted to copy and distribute verbatim copies of this license document,
\rightarrow but changing it is not allowed.
This GCC Runtime Library Exception ("Exception") is an additional permission under
\rightarrowsection 7 of the GNU General Public License,
version 3 ("GPLv3"). It applies to a given file (the "Runtime Library") that bears a
→notice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

### **7.1.2 GNU GENERAL PUBLIC LICENSE**

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007

Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/> Everyone is permitted to copy and distribute verbatim copies of this license document, but changing it is not allowed.

Preamble

The GNU General Public License is a free, copyleft license for software and other kinds of works.

The licenses for most software and other practical works are designed to take away your freedom to share and change the works. By contrast, the GNU General Public License is intended to guarantee your freedom to share and change all versions of a program--to make sure it remains free software for all its users. We, the Free Software Foundation, use the GNU General Public License for most of our software; it applies also to any other work released this way by its authors. You can apply it to your programs, too.

When we speak of free software, we are referring to freedom, not price. Our General Public Licenses are designed to make sure that you have the freedom to distribute copies of free software (and charge for them if you wish), that you receive source code or can get it if you want it, that you can change the software or use pieces of it in new free programs, and that you know you can do these things.

To protect your rights, we need to prevent others from denying you these rights or asking you to surrender the rights. Therefore, you have certain responsibilities if you distribute copies of the software, or if you modify it: responsibilities to respect the freedom of others.

For example, if you distribute copies of such a program, whether gratis or for a fee, you must pass on to the recipients the same freedoms that you received. You must make sure that they, too, receive or can get the source code. And you must show them these terms so they know their rights.

Developers that use the GNU GPL protect your rights with two steps: (1) assert copyright on the software, and (2) offer you this License giving you legal permission to copy, distribute and/or modify it.

For the developers' and authors' protection, the GPL clearly explains that there is no warranty for this free software. For both users' and

authors' sake, the GPL requires that modified versions be marked as changed, so that their problems will not be attributed erroneously to authors of previous versions.

Some devices are designed to deny users access to install or run modified versions of the software inside them, although the manufacturer can do so. This is fundamentally incompatible with the aim of protecting users' freedom to change the software. The systematic pattern of such abuse occurs in the area of products for individuals to use, which is precisely where it is most unacceptable. Therefore, we have designed this version of the GPL to prohibit the practice for those products. If such problems arise substantially in other domains, we stand ready to extend this provision to those domains in future versions of the GPL, as needed to protect the freedom of users.

Finally, every program is threatened constantly by software patents. States should not allow patents to restrict development and use of software on general-purpose computers, but in those that do, we wish to avoid the special danger that patents applied to a free program could make it effectively proprietary. To prevent this, the GPL assures that patents cannot be used to render the program non-free.

The precise terms and conditions for copying, distribution and modification follow.

TERMS AND CONDITIONS

0. Definitions.

"This License" refers to version 3 of the GNU General Public License.

"Copyright" also means copyright-like laws that apply to other kinds of works, such as semiconductor masks.

"The Program" refers to any copyrightable work licensed under this License. Each licensee is addressed as "you". "Licensees" and "recipients" may be individuals or organizations.

To "modify" a work means to copy from or adapt all or part of the work in a fashion requiring copyright permission, other than the making of an exact copy. The resulting work is called a "modified version" of the earlier work or a work "based on" the earlier work.

A "covered work" means either the unmodified Program or a work based on the Program.

To "propagate" a work means to do anything with it that, without permission, would make you directly or secondarily liable for infringement under applicable copyright law, except executing it on a computer or modifying a private copy. Propagation includes copying, distribution (with or without modification), making available to the public, and in some countries other activities as well.

To "convey" a work means any kind of propagation that enables other parties to make or receive copies. Mere interaction with a user through a computer network, with no transfer of a copy, is not conveying.

An interactive user interface displays "Appropriate Legal Notices" to the extent that it includes a convenient and prominently visible feature that (1) displays an appropriate copyright notice, and (2) tells the user that there is no warranty for the work (except to the extent that warranties are provided), that licensees may convey the work under this License, and how to view a copy of this License. If the interface presents a list of user commands or options, such as a menu, a prominent item in the list meets this criterion.

1. Source Code.

The "source code" for a work means the preferred form of the work for making modifications to it. "Object code" means any non-source form of a work.

A "Standard Interface" means an interface that either is an official standard defined by a recognized standards body, or, in the case of interfaces specified for a particular programming language, one that is widely used among developers working in that language.

The "System Libraries" of an executable work include anything, other than the work as a whole, that (a) is included in the normal form of packaging a Major Component, but which is not part of that Major Component, and (b) serves only to enable use of the work with that Major Component, or to implement a Standard Interface for which an implementation is available to the public in source code form. A "Major Component", in this context, means a major essential component (kernel, window system, and so on) of the specific operating system (if any) on which the executable work runs, or a compiler used to produce the work, or an object code interpreter used to run it.

The "Corresponding Source" for a work in object code form means all the source code needed to generate, install, and (for an executable work) run the object code and to modify the work, including scripts to control those activities. However, it does not include the work's System Libraries, or general-purpose tools or generally available free programs which are used unmodified in performing those activities but which are not part of the work. For example, Corresponding Source includes interface definition files associated with source files for the work, and the source code for shared libraries and dynamically linked subprograms that the work is specifically designed to require, such as by intimate data communication or control flow between those subprograms and other parts of the work.

The Corresponding Source need not include anything that users can regenerate automatically from other parts of the Corresponding Source.

The Corresponding Source for a work in source code form is that same work.

2. Basic Permissions.

All rights granted under this License are granted for the term of copyright on the Program, and are irrevocable provided the stated conditions are met. This License explicitly affirms your unlimited permission to run the unmodified Program. The output from running a

covered work is covered by this License only if the output, given its content, constitutes a covered work. This License acknowledges your rights of fair use or other equivalent, as provided by copyright law.

You may make, run and propagate covered works that you do not convey, without conditions so long as your license otherwise remains in force. You may convey covered works to others for the sole purpose of having them make modifications exclusively for you, or provide you with facilities for running those works, provided that you comply with the terms of this License in conveying all material for which you do not control copyright. Those thus making or running the covered works for you must do so exclusively on your behalf, under your direction and control, on terms that prohibit them from making any copies of your copyrighted material outside their relationship with you.

Conveying under any other circumstances is permitted solely under the conditions stated below. Sublicensing is not allowed; section 10 makes it unnecessary.

3. Protecting Users' Legal Rights From Anti-Circumvention Law.

No covered work shall be deemed part of an effective technological measure under any applicable law fulfilling obligations under article 11 of the WIPO copyright treaty adopted on 20 December 1996, or similar laws prohibiting or restricting circumvention of such measures.

When you convey a covered work, you waive any legal power to forbid circumvention of technological measures to the extent such circumvention is effected by exercising rights under this License with respect to the covered work, and you disclaim any intention to limit operation or modification of the work as a means of enforcing, against the work's users, your or third parties' legal rights to forbid circumvention of technological measures.

4. Conveying Verbatim Copies.

You may convey verbatim copies of the Program's source code as you receive it, in any medium, provided that you conspicuously and appropriately publish on each copy an appropriate copyright notice; keep intact all notices stating that this License and any non-permissive terms added in accord with section 7 apply to the code; keep intact all notices of the absence of any warranty; and give all recipients a copy of this License along with the Program.

You may charge any price or no price for each copy that you convey, and you may offer support or warranty protection for a fee.

5. Conveying Modified Source Versions.

You may convey a work based on the Program, or the modifications to produce it from the Program, in the form of source code under the terms of section 4, provided that you also meet all of these conditions:

a) The work must carry prominent notices stating that you modified it, and giving a relevant date.

b) The work must carry prominent notices stating that it is released under this License and any conditions added under section 7. This requirement modifies the requirement in section 4 to "keep intact all notices".

c) You must license the entire work, as a whole, under this License to anyone who comes into possession of a copy. This License will therefore apply, along with any applicable section 7 additional terms, to the whole of the work, and all its parts, regardless of how they are packaged. This License gives no permission to license the work in any other way, but it does not invalidate such permission if you have separately received it.

d) If the work has interactive user interfaces, each must display Appropriate Legal Notices; however, if the Program has interactive interfaces that do not display Appropriate Legal Notices, your work need not make them do so.

A compilation of a covered work with other separate and independent works, which are not by their nature extensions of the covered work, and which are not combined with it such as to form a larger program, in or on a volume of a storage or distribution medium, is called an "aggregate" if the compilation and its resulting copyright are not used to limit the access or legal rights of the compilation's users beyond what the individual works permit. Inclusion of a covered work in an aggregate does not cause this License to apply to the other parts of the aggregate.

6. Conveying Non-Source Forms.

You may convey a covered work in object code form under the terms of sections 4 and 5, provided that you also convey the machine-readable Corresponding Source under the terms of this License, in one of these ways:

a) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by the Corresponding Source fixed on a durable physical medium customarily used for software interchange.

b) Convey the object code in, or embodied in, a physical product (including a physical distribution medium), accompanied by a written offer, valid for at least three years and valid for as long as you offer spare parts or customer support for that product model, to give anyone who possesses the object code either (1) a copy of the Corresponding Source for all the software in the product that is covered by this License, on a durable physical medium customarily used for software interchange, for a price no more than your reasonable cost of physically performing this conveying of source, or (2) access to copy the Corresponding Source from a network server at no charge.

c) Convey individual copies of the object code with a copy of the written offer to provide the Corresponding Source. This alternative is allowed only occasionally and noncommercially, and only if you received the object code with such an offer, in accord

with subsection 6b.

d) Convey the object code by offering access from a designated place (gratis or for a charge), and offer equivalent access to the Corresponding Source in the same way through the same place at no further charge. You need not require recipients to copy the Corresponding Source along with the object code. If the place to copy the object code is a network server, the Corresponding Source may be on a different server (operated by you or a third party) that supports equivalent copying facilities, provided you maintain clear directions next to the object code saying where to find the Corresponding Source. Regardless of what server hosts the Corresponding Source, you remain obligated to ensure that it is available for as long as needed to satisfy these requirements.

e) Convey the object code using peer-to-peer transmission, provided you inform other peers where the object code and Corresponding Source of the work are being offered to the general public at no charge under subsection 6d.

A separable portion of the object code, whose source code is excluded from the Corresponding Source as a System Library, need not be included in conveying the object code work.

A "User Product" is either (1) a "consumer product", which means any tangible personal property which is normally used for personal, family, or household purposes, or (2) anything designed or sold for incorporation into a dwelling. In determining whether a product is a consumer product, doubtful cases shall be resolved in favor of coverage. For a particular product received by a particular user, "normally used" refers to a typical or common use of that class of product, regardless of the status of the particular user or of the way in which the particular user actually uses, or expects or is expected to use, the product. A product is a consumer product regardless of whether the product has substantial commercial, industrial or non-consumer uses, unless such uses represent the only significant mode of use of the product.

"Installation Information" for a User Product means any methods, procedures, authorization keys, or other information required to install and execute modified versions of a covered work in that User Product from a modified version of its Corresponding Source. The information must suffice to ensure that the continued functioning of the modified object code is in no case prevented or interfered with solely because modification has been made.

If you convey an object code work under this section in, or with, or specifically for use in, a User Product, and the conveying occurs as part of a transaction in which the right of possession and use of the User Product is transferred to the recipient in perpetuity or for a fixed term (regardless of how the transaction is characterized), the Corresponding Source conveyed under this section must be accompanied by the Installation Information. But this requirement does not apply if neither you nor any third party retains the ability to install modified object code on the User Product (for example, the work has been installed in ROM).

The requirement to provide Installation Information does not include a

requirement to continue to provide support service, warranty, or updates for a work that has been modified or installed by the recipient, or for the User Product in which it has been modified or installed. Access to a network may be denied when the modification itself materially and adversely affects the operation of the network or violates the rules and protocols for communication across the network.

Corresponding Source conveyed, and Installation Information provided, in accord with this section must be in a format that is publicly documented (and with an implementation available to the public in source code form), and must require no special password or key for unpacking, reading or copying.

7. Additional Terms.

"Additional permissions" are terms that supplement the terms of this License by making exceptions from one or more of its conditions. Additional permissions that are applicable to the entire Program shall be treated as though they were included in this License, to the extent that they are valid under applicable law. If additional permissions apply only to part of the Program, that part may be used separately under those permissions, but the entire Program remains governed by this License without regard to the additional permissions.

When you convey a copy of a covered work, you may at your option remove any additional permissions from that copy, or from any part of it. (Additional permissions may be written to require their own removal in certain cases when you modify the work.) You may place additional permissions on material, added by you to a covered work, for which you have or can give appropriate copyright permission.

Notwithstanding any other provision of this License, for material you add to a covered work, you may (if authorized by the copyright holders of that material) supplement the terms of this License with terms:

a) Disclaiming warranty or limiting liability differently from the terms of sections 15 and 16 of this License; or

b) Requiring preservation of specified reasonable legal notices or author attributions in that material or in the Appropriate Legal Notices displayed by works containing it; or

c) Prohibiting misrepresentation of the origin of that material, or requiring that modified versions of such material be marked in reasonable ways as different from the original version; or

d) Limiting the use for publicity purposes of names of licensors or authors of the material; or

e) Declining to grant rights under trademark law for use of some trade names, trademarks, or service marks; or

f) Requiring indemnification of licensors and authors of that material by anyone who conveys the material (or modified versions of it) with contractual assumptions of liability to the recipient, for any liability that these contractual assumptions directly impose on those licensors and authors.

All other non-permissive additional terms are considered "further restrictions" within the meaning of section 10. If the Program as you received it, or any part of it, contains a notice stating that it is governed by this License along with a term that is a further restriction, you may remove that term. If a license document contains a further restriction but permits relicensing or conveying under this License, you may add to a covered work material governed by the terms of that license document, provided that the further restriction does not survive such relicensing or conveying.

If you add terms to a covered work in accord with this section, you must place, in the relevant source files, a statement of the additional terms that apply to those files, or a notice indicating where to find the applicable terms.

Additional terms, permissive or non-permissive, may be stated in the form of a separately written license, or stated as exceptions; the above requirements apply either way.

#### 8. Termination.

You may not propagate or modify a covered work except as expressly provided under this License. Any attempt otherwise to propagate or modify it is void, and will automatically terminate your rights under this License (including any patent licenses granted under the third paragraph of section 11).

However, if you cease all violation of this License, then your license from a particular copyright holder is reinstated (a) provisionally, unless and until the copyright holder explicitly and finally terminates your license, and (b) permanently, if the copyright holder fails to notify you of the violation by some reasonable means prior to 60 days after the cessation.

Moreover, your license from a particular copyright holder is reinstated permanently if the copyright holder notifies you of the violation by some reasonable means, this is the first time you have received notice of violation of this License (for any work) from that copyright holder, and you cure the violation prior to 30 days after your receipt of the notice.

Termination of your rights under this section does not terminate the licenses of parties who have received copies or rights from you under this License. If your rights have been terminated and not permanently reinstated, you do not qualify to receive new licenses for the same material under section 10.

9. Acceptance Not Required for Having Copies.

You are not required to accept this License in order to receive or run a copy of the Program. Ancillary propagation of a covered work occurring solely as a consequence of using peer-to-peer transmission to receive a copy likewise does not require acceptance. However, nothing other than this License grants you permission to propagate or modify any covered work. These actions infringe copyright if you do not accept this License. Therefore, by modifying or propagating a

covered work, you indicate your acceptance of this License to do so.

10. Automatic Licensing of Downstream Recipients.

Each time you convey a covered work, the recipient automatically receives a license from the original licensors, to run, modify and propagate that work, subject to this License. You are not responsible for enforcing compliance by third parties with this License.

An "entity transaction" is a transaction transferring control of an organization, or substantially all assets of one, or subdividing an organization, or merging organizations. If propagation of a covered work results from an entity transaction, each party to that transaction who receives a copy of the work also receives whatever licenses to the work the party's predecessor in interest had or could give under the previous paragraph, plus a right to possession of the Corresponding Source of the work from the predecessor in interest, if the predecessor has it or can get it with reasonable efforts.

You may not impose any further restrictions on the exercise of the rights granted or affirmed under this License. For example, you may not impose a license fee, royalty, or other charge for exercise of rights granted under this License, and you may not initiate litigation (including a cross-claim or counterclaim in a lawsuit) alleging that any patent claim is infringed by making, using, selling, offering for sale, or importing the Program or any portion of it.

11. Patents.

A "contributor" is a copyright holder who authorizes use under this License of the Program or a work on which the Program is based. The work thus licensed is called the contributor's "contributor version".

A contributor's "essential patent claims" are all patent claims owned or controlled by the contributor, whether already acquired or hereafter acquired, that would be infringed by some manner, permitted by this License, of making, using, or selling its contributor version, but do not include claims that would be infringed only as a consequence of further modification of the contributor version. For purposes of this definition, "control" includes the right to grant patent sublicenses in a manner consistent with the requirements of this License.

Each contributor grants you a non-exclusive, worldwide, royalty-free patent license under the contributor's essential patent claims, to make, use, sell, offer for sale, import and otherwise run, modify and propagate the contents of its contributor version.

In the following three paragraphs, a "patent license" is any express agreement or commitment, however denominated, not to enforce a patent (such as an express permission to practice a patent or covenant not to sue for patent infringement). To "grant" such a patent license to a party means to make such an agreement or commitment not to enforce a patent against the party.

If you convey a covered work, knowingly relying on a patent license, and the Corresponding Source of the work is not available for anyone

to copy, free of charge and under the terms of this License, through a publicly available network server or other readily accessible means, then you must either (1) cause the Corresponding Source to be so available, or (2) arrange to deprive yourself of the benefit of the patent license for this particular work, or (3) arrange, in a manner consistent with the requirements of this License, to extend the patent license to downstream recipients. "Knowingly relying" means you have actual knowledge that, but for the patent license, your conveying the covered work in a country, or your recipient's use of the covered work in a country, would infringe one or more identifiable patents in that country that you have reason to believe are valid.

If, pursuant to or in connection with a single transaction or arrangement, you convey, or propagate by procuring conveyance of, a covered work, and grant a patent license to some of the parties receiving the covered work authorizing them to use, propagate, modify or convey a specific copy of the covered work, then the patent license you grant is automatically extended to all recipients of the covered work and works based on it.

A patent license is "discriminatory" if it does not include within the scope of its coverage, prohibits the exercise of, or is conditioned on the non-exercise of one or more of the rights that are specifically granted under this License. You may not convey a covered work if you are a party to an arrangement with a third party that is in the business of distributing software, under which you make payment to the third party based on the extent of your activity of conveying the work, and under which the third party grants, to any of the parties who would receive the covered work from you, a discriminatory patent license (a) in connection with copies of the covered work conveyed by you (or copies made from those copies), or (b) primarily for and in connection with specific products or compilations that contain the covered work, unless you entered into that arrangement, or that patent license was granted, prior to 28 March 2007.

Nothing in this License shall be construed as excluding or limiting any implied license or other defenses to infringement that may otherwise be available to you under applicable patent law.

12. No Surrender of Others' Freedom.

If conditions are imposed on you (whether by court order, agreement or otherwise) that contradict the conditions of this License, they do not excuse you from the conditions of this License. If you cannot convey a covered work so as to satisfy simultaneously your obligations under this License and any other pertinent obligations, then as a consequence you may not convey it at all. For example, if you agree to terms that obligate you to collect a royalty for further conveying from those to whom you convey the Program, the only way you could satisfy both those terms and this License would be to refrain entirely from conveying the Program.

13. Use with the GNU Affero General Public License.

Notwithstanding any other provision of this License, you have permission to link or combine any covered work with a work licensed under version 3 of the GNU Affero General Public License into a single combined work, and to convey the resulting work. The terms of this

License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. 14. Revised Versions of this License. The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. 15. Disclaimer of Warranty. THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 16. Limitation of Liability. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF

DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

17. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page)

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

#### See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# $\mathsf{C}$

Clear OESpicoli:: OESurface, 13 ClearVertexClique OESpicoli:: OESurface, 13 Constructors OESpicoli:: OESurface, 13 CreateCopy OESpicoli:: OESurface, 13

# G

GetAtoms OESpicoli:: OESurface, 14 GetAtomsElement OESpicoli:: OESurface, 14 GetColor OESpicoli:: OESurface, 14 GetColorElement OESpicoli:: OESurface, 14 GetCurvature OESpicoli:: OESurface, 14 GetCurvatureElement OESpicoli:: OESurface, 14 GetDataType OESpicoli:: OESurface, 15 GetDistance OESpicoli:: OESurface, 15 GetDistanceElement OESpicoli:: OESurface, 15 GetFaceNormal OESpicoli:: OESurface, 15 GetFaceNormals OESpicoli:: OESurface, 15 GetFaceNormalsElement OESpicoli:: OESurface, 15 GetNormal OESpicoli:: OESurface, 16 GetNormals OESpicoli:: OESurface, 15 GetNormalsElement OESpicoli:: OESurface, 16 GetNumTriangles

OESpicoli:: OESurface, 16 GetNumVertices OESpicoli:: OESurface, 16 GetPotential OESpicoli:: OESurface, 16 GetPotentialElement OESpicoli:: OESurface, 16 GetPotentialName OESpicoli:: OESurface, 17 GetProbeRadius OESpicoli:: OESurface, 17 GetResolution OESpicoli:: OESurface, 17 GetTitle OESpicoli:: OESurface, 17 GetTriangle OESpicoli:: OESurface, 17 GetTriangles OESpicoli:: OESurface, 17 GetTrianglesElement OESpicoli:: OESurface, 17 GetVertex OESpicoli:: OESurface, 18 GetVertexClique OESpicoli:: OESurface, 18 GetVertexCliqueElement OESpicoli:: OESurface, 18 GetVertices OESpicoli:: OESurface, 18 GetVerticesElement OESpicoli:: OESurface, 18

# $\mathbf{I}$

```
IsAtomsSet
   OESpicoli:: OESurface, 18
IsColorSet
   OESpicoli:: OESurface, 19
IsCurvatureSet
   OESpicoli:: OESurface, 19
IsDataType
   OESpicoli:: OESurface, 19
IsDistanceSet
```

```
OESpicoli:: OESurface, 19
IsFaceNormalsSet
   OESpicoli:: OESurface, 19
IsNormalsSet
   OESpicoli:: OESurface, 19
IsPotentialSet
   OESpicoli:: OESurface, 19
IsVertexCliqueSet
   OESpicoli:: OESurface, 20
```

# Ő

```
OESpicoli:: OEAddSurfaces, 28
OESpicoli:: OECalculateFaceNormals, 28
OESpicoli:: OECalculateNormals, 28
OESpicoli:: OECalculateSurfaceCurvature,
       29
OESpicoli::OECalculateSurfacePotentials, OESpicoli::OESpicoliGetPlatform, 38
       29
OESpicoli:: OECalculateTriangleAreas, 29
OESpicoli:: OEColorSurfaceByPotential,
       30
OESpicoli:: OEEdgeReductionType, 25
OESpicoli::OEEdgeReductionType::MinimumD950aheeli::OESurface, 13
       25
OESpicoli:: OEGetCenterAndExtents, 30
OESpicoli:: OEGetSurface, 30
OESpicoli::OEGetSurfaceFileType, 31
OESpicoli:: OEGetSurfaceFormatExtension,
       31
OESpicoli:: OEGetSurfaceFormatString, 31
OESpicoli:: OEInitSurfaceHandlers, 31
OESpicoli:: OEInvertSurface, 31
OESpicoli:: OEIsReadableSurface, 32
OESpicoli::OEIsWriteableSurface, 32
OESpicoli:: OEMakeAccessibleSurface, 32
OESpicoli:: OEMakeBitGridFromSurface, 33
OESpicoli:: OEMakeBoxSurface, 33
OESpicoli:: OEMakeCavitySurfaces, 33
OESpicoli:: OEMakeCliqueSurface, 33
OESpicoli:: OEMakeComplexCavities, 33
OESpicoli:: OEMakeConnectedSurfaceCliques,
       34
OESpicoli:: OEMakeEllipsoidSurface, 34
OESpicoli:: OEMakeGridFromSurface, 34
OESpicoli:: OEMakeMolecularSurface, 34
OESpicoli:: OEMakeProteinRibbonSurface,
       35
OESpicoli:: OEMakeSphericalSurface, 35
OESpicoli:: OEMakeSurfaceFromGrid, 35
OESpicoli::OEMakeVoidVolume, 36
OESpicoli:: OEPolygonizeMethod, 25
OESpicoli::OEPolygonizeMethod::Compact,
       26
```

OESpicoli::OEPolygonizeMethod::Default, 26 OESpicoli::OEPolygonizeMethod::Grasp, 25 OESpicoli:: OEReadSurface, 36 OESpicoli:: OEReduceSurface, 36 OESpicoli::OERibbonType, 28 OESpicoli::OERibbonType::CAlpha, 28 OESpicoli:: OERibbonType:: Pretty, 28 OESpicoli:: OERotateSurface, 37 OESpicoli:: OESetSurface, 37 OESpicoli::OESetSurfaceColor, 37 OESpicoli:: OESetSurfacePotentials, 37 OESpicoli::OESmoothSurfaceEdges, 37 OESpicoli:: OESpicoliGetArch, 38 OESpicoli:: OESpicoliGetLicensee, 38 OESpicoli::OESpicoliGetRelease, 38 OESpicoli::OESpicoliGetSite, 39 OESpicoli::OESpicoliGetVersion, 39 OESpicoli:: OESpicoliIsLicensed, 39 OESpicoli:: OESplitSurfaceByAtoms, 39 Clear. 13 ClearVertexClique, 13 Constructors, 13 CreateCopy, 13 GetAtoms, 14 GetAtomsElement, 14 GetColor, 14 GetColorElement, 14 GetCurvature, 14 GetCurvatureElement, 14 GetDataType, 15 GetDistance, 15 GetDistanceElement, 15 GetFaceNormal, 15 GetFaceNormals, 15 GetFaceNormalsElement, 15 GetNormal, 16 GetNormals, 15 GetNormalsElement, 16 GetNumTriangles, 16 GetNumVertices, 16 GetPotential, 16 GetPotentialElement, 16 GetPotentialName, 17 GetProbeRadius, 17 GetResolution, 17 GetTitle, 17 GetTriangle, 17 GetTriangles, 17 GetTrianglesElement, 17 GetVertex, 18

GetVertexClique, 18 GetVertexCliqueElement, 18 GetVertices, 18 GetVerticesElement, 18 IsAtomsSet, 18 IsColorSet, 19 IsCurvatureSet, 19 IsDataType, 19 IsDistanceSet, 19 IsFaceNormalsSet, 19 IsNormalsSet, 19 IsPotentialSet, 19 IsVertexCliqueSet, 20 operator bool, 13 operator+=,  $13$ operator=, 13 SetAtoms, 20 SetAtomsElement, 20 SetColor, 20 SetColorElement, 20 SetCurvature, 20 SetCurvatureElement, 21 SetDistance, 21 SetDistanceElement, 21 SetFaceNormal, 21 SetFaceNormals, 21 SetFaceNormalsElement, 21 SetNormal, 22 SetNormals, 22 SetNormalsElement. 22 SetNumTriangles, 22 SetNumVertices, 22 SetPotential, 23 SetPotentialElement. 23 SetPotentialName, 23 SetTitle, 24 SetTriangle, 24 SetTriangles, 24 SetTrianglesElement, 24 SetVertex, 24 SetVertexClique, 24 SetVertexCliqueElement, 25 SetVertices, 25 SetVerticesElement, 25 OESpicoli:: OESurfaceArea, 40 OESpicoli::OESurfaceCliqueArea, 40 OESpicoli:: OESurfaceCliqueCentroid, 40 OESpicoli::OESurfaceCliqueVolume, 40 OESpicoli::OESurfaceCropToClique, 40 OESpicoli::OESurfaceFileType, 26 OESpicoli:: OESurfaceFileType:: Grasp, 26 OESpicoli::OESurfaceFileType::OESurface, 26

```
OESpicoli::OESurfaceFileType::UNDEFINED,
       26
OESpicoli:: OESurfaceIsOpen, 41
OESpicoli::OESurfaceToMoleculeDistance,
       41
OESpicoli::OESurfaceVolume, 41
OESpicoli:: OETransformSurface, 41
OESpicoli:: OETranslateSurface, 41
OESpicoli:: OEVoxelizeMethod, 26
OESpicoli:: OEVoxelizeMethod:: Blank, 27
OESpicoli::OEVoxelizeMethod::Blur, 27
OESpicoli::OEVoxelizeMethod::Default,
       27
OESpicoli::OEVoxelizeMethod::Distance,
       27
OESpicoli:: OEVoxelizeMethod:: Gaussian,
       27
OESpicoli:: OEWriteSurface, 42
operator bool
   OESpicoli:: OESurface, 13
operator+=
   OESpicoli:: OESurface, 13
operator=
   OESpicoli:: OESurface, 13
```

# S

```
SetAtoms
   OESpicoli:: OESurface, 20
SetAtomsElement
   OESpicoli:: OESurface, 20
SetColor
   OESpicoli:: OESurface, 20
SetColorElement
   OESpicoli:: OESurface, 20
SetCurvature
   OESpicoli:: OESurface, 20
SetCurvatureElement
   OESpicoli:: OESurface, 21
SetDistance
   OESpicoli:: OESurface, 21
SetDistanceElement
   OESpicoli:: OESurface, 21
SetFaceNormal
   OESpicoli::OESurface, 21
SetFaceNormals
   OESpicoli:: OESurface, 21
SetFaceNormalsElement
   OESpicoli:: OESurface, 21
SetNormal
   OESpicoli:: OESurface, 22
SetNormals
   OESpicoli:: OESurface, 22
SetNormalsElement
   OESpicoli:: OESurface, 22
```

SetNumTriangles OESpicoli:: OESurface, 22 SetNumVertices OESpicoli:: OESurface, 22 SetPotential OESpicoli:: OESurface, 23 SetPotentialElement OESpicoli:: OESurface, 23 SetPotentialName OESpicoli:: OESurface, 23 SetTitle OESpicoli:: OESurface, 24 SetTriangle OESpicoli:: OESurface, 24 SetTriangles OESpicoli:: OESurface, 24 SetTrianglesElement OESpicoli:: OESurface, 24 SetVertex OESpicoli:: OESurface, 24 SetVertexClique OESpicoli:: OESurface, 24 SetVertexCliqueElement OESpicoli:: OESurface, 25 SetVertices OESpicoli:: OESurface, 25 SetVerticesElement OESpicoli:: OESurface, 25