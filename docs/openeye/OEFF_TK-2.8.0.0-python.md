![](_page_0_Picture_0.jpeg)

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| Section                            | Title                                                | Page                                                     |            |
|------------------------------------|------------------------------------------------------|----------------------------------------------------------|------------|
| 1                                  | <b>Theory</b>                                        | 1                                                        |            |
|                                    | 1.1 Components                                       | 1                                                        |            |
|                                    | 1.1.1 Objective Functions                            | 1                                                        |            |
|                                    | 1.1.2 Molecule Objective Function                    | 1                                                        |            |
|                                    | 1.1.3 Adaptors                                       | 1                                                        |            |
|                                    | 1.1.4 Optimizers                                     | 1                                                        |            |
|                                    | 1.2 Force Field                                      | 1                                                        |            |
|                                    | 1.2.1 MMFF                                           | 1                                                        |            |
|                                    | 1.2.2 FF14SB                                         | 1                                                        |            |
|                                    | 1.2.3 SMIRNOFF                                       | 1                                                        |            |
|                                    | 1.2.4 AMBER force field terms                        | 1                                                        |            |
|                                    | 1.2.5 MMFFAmber                                      | 2                                                        |            |
|                                    | 1.2.6 MMFFIEFF                                       | 2                                                        |            |
|                                    | 1.3 Sheffield Model                                  | 2                                                        |            |
|                                    | 1.3.1 Small molecules                                | 2                                                        |            |
|                                    | 1.3.2 Proteins                                       | 2                                                        |            |
| 2                                  | <b>OEFF Examples</b>                                 | 1                                                        |            |
|                                    | 2.1 Simple Functions and Optimization                | 1                                                        |            |
|                                    | 2.1.1 Solving a simple equation                      | 1                                                        |            |
|                                    | 2.1.2 Using checkpoints for optimization monitoring  | 1                                                        |            |
|                                    | 2.2 Molecule Functions                               | 1                                                        |            |
|                                    | 2.2.1 User defined molecule function                 | 1                                                        |            |
|                                    | 2.3 Small Molecule Force fields                      | 1                                                        |            |
|                                    | 2.3.1 Single ligand in vacuum                        | 1                                                        |            |
|                                    | 2.3.2 Energy components of a single ligand in vacuum | 1                                                        |            |
|                                    | 2.3.3 MMFF interactions of a single ligand           | 2                                                        |            |
|                                    | 2.4 Protein-Ligand Complexes                         | 2                                                        |            |
|                                    | 2.4.1 Protein-ligand optimization                    | 2                                                        |            |
|                                    | 2.5 Using adaptors                                   | 2                                                        |            |
|                                    | 2.5.1 Optimizing a single ligand with fixed atoms    | 2                                                        |            |
|                                    | 2.5.2 Optimizing a single ligand torsions            | 2                                                        |            |
|                                    | 2.5.3 Optimizing rigid ligand in protein             | 3                                                        |            |
|                                    | 2.6 Custom Force Fields                              | 3                                                        |            |
|                                    | 2.6.1 Custom Smirnoff                                | 3                                                        |            |
| 3                                  | <b>OEFF API</b>                                      | 1                                                        |            |
|                                    | 3.1 OEOpt Classes                                    | 1                                                        |            |
|                                    | 3.1.1 OEAdaptor                                      | 1                                                        |            |
|                                    | 3.1.2 OEBFGSOpt                                      | 1                                                        |            |
| Section                            | Class                                                | Page                                                     |            |
| 3.1.3                              | OECGLineMinimize                                     | 4                                                        |            |
| 3.1.4                              | OECheckpoint0                                        | 4                                                        |            |
| 3.1.5                              | OECheckpoint1                                        | 4                                                        |            |
| 3.1.6                              | OEConjGradOpt                                        | 4                                                        |            |
| 3.1.7                              | OEDFPOpt                                             | 4                                                        |            |
| 3.1.8                              | OEFComponent                                         | 4                                                        |            |
| 3.1.9                              | OEFletcherReevesOpt                                  | 4                                                        |            |
| 3.1.10                             | OEFunc0                                              | 4                                                        |            |
| 3.1.11                             | OEFunc1                                              | 4                                                        |            |
| 3.1.12                             | OEFunc2                                              | 4                                                        |            |
| 3.1.13                             | OEHestenesStiefelOpt                                 | 5                                                        |            |
| 3.1.14                             | OELineMinimize                                       | 5                                                        |            |
| 3.1.15                             | OEMaxStepLineMinimize                                | 5                                                        |            |
| 3.1.16                             | OENRLineSearch                                       | 5                                                        |            |
| 3.1.17                             | OEOptimizer0                                         | 5                                                        |            |
| 3.1.18                             | OEOptimizer1                                         | 5                                                        |            |
| 3.1.19                             | OEOptimizer2                                         | 5                                                        |            |
| 3.1.20                             | OEQNLineMinimize                                     | 5                                                        |            |
| 3.1.21                             | OERibierePolakOpt                                    | 5                                                        |            |
| 3.1.22                             | OESteepestDescentOpt                                 | 5                                                        |            |
| 3.1.23                             | OENewtonOpt                                          | 6                                                        |            |
| 3.2                                | OEMolPotential Classes                               | 6                                                        |            |
| 3.2.1                              | OEBendParams                                         | 6                                                        |            |
| 3.2.2                              | OEBendPotential                                      | 6                                                        |            |
| 3.2.3                              | OECoulombPotential                                   | 6                                                        |            |
| 3.2.4                              | OEFFParams                                           | 6                                                        |            |
| 3.2.5                              | OEFFPotential                                        | 7                                                        |            |
| 3.2.6                              | OEForceField                                         | 7                                                        |            |
| 3.2.7                              | OEGenericFF                                          | 7                                                        |            |
| 3.2.8                              | OEGenericFF2                                         | 7                                                        |            |
| 3.2.9                              | OEInteraction                                        | 8                                                        |            |
| 3.2.10                             | OEInteractParams                                     | 8                                                        |            |
| 3.2.11                             | OEInterAdaptor                                       | 8                                                        |            |
| 3.2.12                             | OEInterCoulombPotential                              | 8                                                        |            |
| 3.2.13                             | OEInterMolFunc1                                      | 8                                                        |            |
| 3.2.14                             | OEInterMolFunc2                                      | 8                                                        |            |
| 3.2.15                             | OEInterNonBondPotBase                                | 8                                                        |            |
| 3.2.16                             | OEInterNonBondPotential                              | 9                                                        |            |
| 3.2.17                             | OEInterVdwPotential                                  | 9                                                        |            |
| 3.2.18                             | OEMolAdaptor                                         | 9                                                        |            |
| 3.2.19                             | OEMolAdaptor2                                        | 9                                                        |            |
| 3.2.20                             | OEMolFunc                                            | 9                                                        |            |
| 3.2.21                             | OEMolFunc0                                           | 9                                                        |            |
| 3.2.22                             | OEMolFunc1                                           | 10                                                       |            |
| 3.2.23                             | OEMolFunc2                                           | 10                                                       |            |
| 3.2.24                             | OENonBondPotBase                                     | 10                                                       |            |
| 3.2.25                             | OENonBondPotential                                   | 10                                                       |            |
| 3.2.26                             | OENonBondIntcsOptions                                | 10                                                       |            |
| 3.2.27                             | OENumericMolFunc2                                    | 11                                                       |            |
| 3.2.28                             | OEOutOfPlaneParams                                   | 11                                                       |            |
| 3.2.29                             | OEOutOfPlanePotential                                | 11                                                       |            |
| 3.2.30                             | OEQuatAdaptor                                        | 11                                                       |            |
| 3.2.31                             | OEScaledMolFunc                                      | 11                                                       |            |
| 3.2.32                             | OEStretchParams                                      | 11                                                       |            |
|                                    | 3.2.33                                               | OEStretchPotential                                       |            |
|                                    | 3.2.34                                               | OESubsetAdaptor                                          |            |
|                                    | 3.2.35                                               | OETorAdaptor                                             |            |
|                                    | 3.2.36                                               | OETorQuatAdaptor                                         |            |
|                                    | 3.2.37                                               | OETorsionParams                                          |            |
|                                    | 3.2.38                                               | OETorsionPotential                                       |            |
|                                    | 3.2.39                                               | OEVdwParams                                              |            |
|                                    | 3.2.40                                               | OEVdwPotential                                           |            |
| 3.3                                |                                                      | OEMolPotential Constants                                 |            |
|                                    | 3.3.1                                                | OEFFParam                                                |            |
|                                    | 3.3.2                                                | OEVarType                                                |            |
|                                    | 3.3.3                                                | OEFuncType                                               |            |
| 3.4                                |                                                      | OEConstr Classes                                         |            |
|                                    | 3.4.1                                                | OEDihedralQuadPenalty                                    |            |
|                                    | 3.4.2                                                | OEHarmonicPotential                                      |            |
| 3.5                                |                                                      | OEMolMMFF Classes                                        |            |
|                                    | 3.5.1                                                | OEMMFF                                                   |            |
|                                    | 3.5.2                                                | OEMMFF94sParams                                          |            |
|                                    | 3.5.3                                                | OEMMFFOutOfPlane                                         |            |
|                                    | 3.5.4                                                | OEMMFFParams                                             |            |
|                                    | 3.5.5                                                | OEMMFFStretchBend                                        |            |
| 3.6                                |                                                      | OEMolMMFF Functions                                      |            |
|                                    | 3.6.1                                                | OEIsValidMMFFMolecule                                    |            |
|                                    | 3.6.2                                                | OEMMFFCalcVdw                                            |            |
| 3.7                                |                                                      | OEMolSmirnoff Classes                                    |            |
|                                    | 3.7.1                                                | OEParsley                                                |            |
|                                    | 3.7.2                                                | OEParsleyParams                                          |            |
|                                    | 3.7.3                                                | OESage                                                   |            |
|                                    | 3.7.4                                                | OESageParams                                             |            |
|                                    | 3.7.5                                                | OESmirnoff                                               |            |
|                                    | 3.7.6                                                | OESmirnoffParams                                         |            |
| 3.8                                |                                                      | OEMolSmirnoff Constants                                  |            |
|                                    | 3.8.1                                                | OESmirnoffType                                           |            |
| 3.9                                |                                                      | OESheff Classes                                          |            |
|                                    | 3.9.1                                                | OESheffield                                              |            |
|                                    | 3.9.2                                                | OESheffieldOptions                                       |            |
| 3.10                               |                                                      | OESheff Constants                                        |            |
|                                    | 3.10.1                                               | OESheffieldParamType                                     |            |
| 3.11                               |                                                      | OEFF Classes                                             |            |
|                                    | 3.11.1                                               | OEComplexEnergies                                        |            |
|                                    | 3.11.2                                               | OEComplexFF                                              |            |
|                                    | 3.11.3                                               | OEComplexFFParameter                                     |            |
|                                    | 3.11.4                                               | OEFF14SBParsleyComplex                                   |            |
|                                    | 3.11.5                                               | OEFF14SBSmirnoffComplex                                  |            |
|                                    | 3.11.6                                               | OEForceFieldParameter                                    |            |
|                                    | 3.11.7                                               | OEMMFFAmberComplex                                       |            |
|                                    | 3.11.8                                               | OEMMFFComplex                                            |            |
|                                    | 3.11.9                                               | OEMMFFIEFF                                               |            |
|                                    | 3.11.10                                              | OEMMFFIEFFOptions                                        |            |
|                                    | 3.11.11                                              | OEMMFFSheffield                                          |            |
|                                    | 3.11.12                                              | OEMMFFSheffieldOptions                                   |            |
|                                    | 3.11.13                                              | OEFF14SBSageComplex                                      |            |
|                                    | 3.11.14                                              | OEFF14SBSmirnoff                                         |            |
|                                    | 3.11.15                                              | OEFF14SBSmirnoffParams                                   |            |
| 3.11.16 OEFF14SBSage               | 188                                                  |                                                          |            |
| 3.11.17 OEFF14SBSageParams         | 188                                                  |                                                          |            |
| 3.11.18 OEFF14SBParsley            | 188                                                  |                                                          |            |
| 3.11.19 OEFF14SBParsleyParams      | 188                                                  |                                                          |            |
| 3.11.20 OESmirnoffComplex          | 191                                                  |                                                          |            |
| 3.12 OEFF Functions                | 192                                                  |                                                          |            |
| 3.12.1 OEClearForceFieldDummyAtom  | 192                                                  |                                                          |            |
| 3.12.2 OEClearForceFieldDummyAtoms | 192                                                  |                                                          |            |
| 3.12.3 OEGetMMFFSheffieldFFName    | 193                                                  |                                                          |            |
| 3.12.4 OEGetMMFFSheffieldFFType    | 193                                                  |                                                          |            |
| 3.12.5 OEIsForceFieldDummyAtom     | 193                                                  |                                                          |            |
| 3.12.6 OEIsValidMMFFSheffieldFF    | 193                                                  |                                                          |            |
| 3.12.7 OESetForceFieldDummyAtom    | 194                                                  |                                                          |            |
| 3.12.8 OEFFGetArch                 | 194                                                  |                                                          |            |
| 3.12.9 OEFFGetLicensee             | 194                                                  |                                                          |            |
| 3.12.10 OEFFGetPlatform            | 194                                                  |                                                          |            |
| 3.12.11 OEFFGetRelease             | 195                                                  |                                                          |            |
| 3.12.12 OEFFGetSite                | 195                                                  |                                                          |            |
| 3.12.13 OEFFGetVersion             | 195                                                  |                                                          |            |
| 3.12.14 OEFFIsLicensed             | 195                                                  |                                                          |            |
| 3.13 OEFF Constants                | 195                                                  |                                                          |            |
| 3.13.1 OELigandFFType              | 195                                                  |                                                          |            |
| 3.13.2 OEMMFFSheffieldFFType       | 196                                                  |                                                          |            |
| 4 Release History                  | 199                                                  |                                                          |            |
| 4.1 OEFF TK 2.8.0                  | 199                                                  |                                                          |            |
| 4.1.1 New features                 | 199                                                  |                                                          |            |
| 4.1.2 Minor Bug Fixes              | 199                                                  |                                                          |            |
| 4.2 OEFF TK 2.7.1                  | 199                                                  |                                                          |            |
| 4.2.1 New features                 | 199                                                  |                                                          |            |
| 4.2.2 Minor bug fixes              | 200                                                  |                                                          |            |
| 4.3 OEFF TK 2.7.0                  | 200                                                  |                                                          |            |
| 4.3.1 New features                 | 200                                                  |                                                          |            |
| 4.3.2 Major bug fixes              | 200                                                  |                                                          |            |
| 4.3.3 Minor bug fixes              | 200                                                  |                                                          |            |
| 4.4 OEFF TK 2.5.2.1                | 200                                                  |                                                          |            |
| 4.5 OEFF TK 2.5.2.0                | 200                                                  |                                                          |            |
| 4.5.1 Major bug fixes              | 200                                                  |                                                          |            |
| 4.6 OEFF TK 2.5.1                  | 201                                                  |                                                          |            |
| 4.6.1 New features                 | 201                                                  |                                                          |            |
| 4.6.2 Major bug fixes              | 201                                                  |                                                          |            |
| 4.6.3 Minor bug fixes              | 201                                                  |                                                          |            |
| 4.7 OEFF TK 2.5.0                  | 201                                                  |                                                          |            |
| 4.7.1 New features                 | 201                                                  |                                                          |            |
| 4.7.2 Major bug fixes              | 202                                                  |                                                          |            |
| 4.8 OEFF TK 2.4.0                  | 202                                                  |                                                          |            |
| 4.8.1 New features                 | 202                                                  |                                                          |            |
| 4.8.2 Minor bug fixes              | 203                                                  |                                                          |            |
| 4.9 OEFF TK 2.3.1                  | 203                                                  |                                                          |            |
| 4.10 OEFF TK 2.3.0                 | 203                                                  |                                                          |            |
| 4.10.1 New features                | 203                                                  |                                                          |            |
| 4.10.2 Documentation changes       | 205                                                  |                                                          |            |
| 4.11 OEFF TK 2.2.0                 |                                                      |                                                          |            |
| 4.11.1 New features                |                                                      |                                                          |            |
|                                    |                                                      | 4.11.2<br>Major bug fixes                                | 200        |
|                                    |                                                      | 4.11.3<br>Minor bug fixes                                | 200        |
|                                    | 4.12                                                 | OEFF TK 2.1.0                                            | 200        |
|                                    |                                                      | 4.12.1<br>New features                                   | 200        |
|                                    |                                                      | 4.12.2<br>Major bug fixes                                | 201        |
|                                    |                                                      | 4.12.3<br>Documentation changes                          | 201        |
|                                    | 4.13                                                 | OEFF TK 2.0.4                                            | 202        |
|                                    | 4.14                                                 | OEFF TK 2.0.3                                            | 203        |
|                                    |                                                      | 4.14.1<br>New features                                   | 203        |
|                                    |                                                      | 4.14.2<br>Minor bug fixes                                | 203        |
|                                    |                                                      | 4.14.3<br>Documentation changes                          | 203        |
|                                    | 4.15                                                 | OEFF TK 2.0.2                                            | 204        |
|                                    | 4.16                                                 | OEFF TK 2.0.1                                            | 205        |
|                                    |                                                      | 4.16.1<br>New features                                   | 205        |
|                                    |                                                      | 4.16.2<br>Minor Bug Fixes                                | 205        |
|                                    | 4.17                                                 | OEFF TK 2.0.0                                            | 210        |
|                                    |                                                      | 4.17.1<br>Licensing                                      | 210        |
|                                    |                                                      | 4.17.2<br>OEFF functionality                             | 210        |
|                                    |                                                      | 4.17.3<br>Objective functions and molecular interactions | 210        |
|                                    |                                                      | 4.17.4<br>Force fields                                   | 210        |
|                                    |                                                      | 4.17.5<br>Optimizers                                     | 211        |
|                                    |                                                      | 4.17.6<br>Adaptors                                       | 211        |
|                                    |                                                      | 4.17.7<br>New features                                   | 211        |
| 5                                  |                                                      | <b>Copyright and Trademarks</b>                          | 213        |
| 6                                  |                                                      | <b>Sample Code</b>                                       | 215        |
| 7                                  | <b>Citation</b>                                      |                                                          | 217        |
|                                    | 7.1                                                  | Orion ® Floes                                            | 217        |
|                                    | 7.2                                                  | Toolkits and Applications                                | 218        |
|                                    | 7.3                                                  | OpenEye Web Services                                     | 219        |
| 8                                  | 8.1                                                  | <b>Technology Licensing</b><br><b>GCC</b>                | 221<br>233 |
|                                    |                                                      | 8.1.1<br>GCC RUNTIME LIBRARY EXCEPTION                   | 233        |
|                                    |                                                      | 8.1.2<br>GNU GENERAL PUBLIC LICENSE                      | 238        |
|                                    | <b>Index</b>                                         |                                                          | 251        |

Attention: OEFF TK is currently only available in C++ and Python.

# **CHAPTER**

# **ONE**

# **THEORY**

# **1.1 Components**

# **1.1.1 Objective Functions**

At the core of the objective functions are pure virtual interfaces OEFunc0, OEFunc1 and OEFunc2. A new objective function can be defined by providing appropriate expressions for these interface methods. The objective functions can be used along with the optimizers to find the minima of any function.

# **1.1.2 Molecule Objective Function**

The molecule objective functions extend the objective function interfaces to define molecular interactions through OEMolFunc. Similar to the objective functions, a new molecule objective function can also be defined by providing the appropriate expressions for the interface methods. All of the force field components are defined as molecule objective functions to allow easy minimization of molecule systems.

# 1.1.3 Adaptors

Adaptors wrap molecule objective functions to allow working in different coordinate systems, instead of the default all atom Cartesian coordinates. Adaptors can be powerful tool for selective energy evaluation and minimization of specific subdomains. Methods to convert between the adaptor coordinates and the Cartesian coordinates are also provided through these interfaces.

# 1.1.4 Optimizers

A number of general purpose optimizers are provided that can be used to minimize any basic or extended objective functions. Optimizer interfaces are defined through OEOptimizer1 and OEOptimizer2. Pros and cons of various optimizers are established in the literature, and one needs to use their understanding of the problem in choosing the appropriate optimizer. Optimizers that can solve objective functions with known gradients but no Hessian ( $OEOpti$ mizer1) requires an additional line minimizer (OELineMinimize).

# **1.2 Force Field**

# **1.2.1 MMFF**

The MMFF potential expression is:

$$
V_{MMFF} = \sum_{b} V_b + \sum_{a} V_a + \sum_{s} V_s + \sum_{o} V_o + \sum_{t} V_t + \sum_{v} V_v + \sum_{c} V_c
$$

where the seven terms respectively describe bond stretching  $(b)$ , angle bending  $(a)$ , stretch-bending  $(s)$ , out-of-plane bending  $(o)$ , torsion  $(t)$ , Van der Waals  $(v)$  and electrostatic  $(c)$  interactions. Their functional forms are given below.

## **Bond stretching**

For a bond  $b$  between atoms  $i$  and  $j$  the stretching potential is:

$$
V_b = 143.9325 \frac{k_{ij}}{2} \Delta r_{ij}^2 (1 + c_s \Delta r_{ij} + 7/12 c_s^2 \Delta r_{ij}^2)
$$

where  $k_{ij}$  is the force constant,  $\Delta r_{ij}$  is the difference between actual and reference bond lengths, and  $c_s$  is so called "cubic-stretch" constant for which the value is -2  $\AA^{-1}$ .

### **Angle bending**

The bending potential of a bond angle  $a$  made by the bonds between atoms  $i, j$  and atoms  $j, k$  is given by:

$$
V_a = 0.043844 \frac{k_{ijk}}{2} \Delta \vartheta_{ijk}^2 (1 + c_b \Delta \vartheta_{ijk})
$$

where  $k_{ijk}$  is the force constant,  $\Delta \vartheta_{ijk}$  is the difference between actual and reference bond angles, and  $c_b$  is the so called "cubic-bend" constant for which the value is  $-0.4rad^{-1}$ .

#### **Stretch-bend interaction**

The coupling between the stretching potential of two bonds forming a bond angle and bending that angle is described by:

$$
V_s = 2.5121(k_{ijk}\Delta r_{ij} + k_{kji}\Delta r_{kj})\Delta \vartheta_{ijk}
$$

where  $k_{ijk}$  and  $k_{kji}$  are force constants which couple stretches of *i-j* and *k-j* to the *i-j-k* bend respectively.  $\Delta r$  and  $\Delta \vartheta$ are defined above.

### **Out-of-plane bending**

For a trigonal center *j*, the potential of displacement for an atom *l* bonded to atom *j* out of plane  $i-j-k$  is:

$$
V_o = 0.043844 \frac{k_{ijkl}}{2} \chi_{ijkl}^2
$$

where  $k_{ijkl}$  is the force constant and  $\chi_{ijkl}$  is an angle formed by the bond j-l and the plane i-j-k.

## **Torsion interactions**

For every four bonded atoms  $i-j-k-l$  the torsion interaction is described by the term:

$$
V_t = 0.5(V_1(1 + \cos \Phi) + V_2(1 - \cos 2\Phi) + V_3(1 + \cos 3\Phi)
$$

where  $V_1$ ,  $V_2$  and  $V_3$  are constants depending on atoms i, j, k, l, and  $\Phi$  is the dihedral angle formed by bonds i-j and  $k-l.$ 

#### **Van der Waals interactions**

For a pair of atoms i and j separated by three or more bonds, where the distance between them is  $r_{ij}$ , MMFF adopts the following Van der Waals potential:

$$
V_v = \epsilon_{ij} \left( \frac{1.07 R_{ij}}{r_{ij} + 0.07 R_{ij}} \right)^7 \left( \frac{1.12 R_{ij}^7}{r_{ij}^7 + 0.12 R_{ij}} - 2 \right)
$$

where  $R_{ij}$  and  $\epsilon_{ij}$  are defined as follows:

$$
R_i = A_i \alpha_i^{0.25}
$$
  
\n
$$
R_{ij} = 0.5(R_i + R_j)(1 + B(1 - \exp(-12\gamma_{ij}^2)))
$$
  
\n
$$
\gamma_{ij} = (R_i - R_j)/(R_i + R_j)
$$
  
\n
$$
\epsilon_{ij} = \frac{181.16G_iG_j\alpha_i\alpha_j}{(\alpha_i/N_i)^{0.5} + (\alpha_j/N_j)^{0.5}} \frac{1}{R_{ij}^6}
$$

where  $\alpha_i$  is atomic polarizability of atom i, B is 0.2 or 0.0 if one of the atoms is polar hydrogen,  $N_i$  and  $N_j$  are the Slater-Kirkwood effective numbers of valence electrons,  $G_i$ ,  $G_j$  and  $A_i$  are scale factors.

#### **Electrostatic interactions**

The electrostatic interaction between two charged atoms  $i$  and  $j$  separated by at least three bonds is calculated from the standard Coulombic expression:

$$
V_c = f \frac{332.0716q_i q_j}{D(r_{ij} + \delta)}
$$

where D is the dielectric constant for which the default value is 1,  $q_i$  and  $q_j$  are the MMFF partial charges on atoms i and j,  $r_{ij}$  is the interatomic distance,  $\delta$  is the "electrostatic buffering" constant of 0.05 Å. Scaling factor f is 0.75 for 1,4 interactions, and 1.0 otherwise.

## **1.2.2 FF14SB**

FF14SB is Amber primary force field for protein modeling. Its details are described in the paper of Maier et al. ([Maier-2015]) and in http://ambermd.org/AmberModels.php. The functional form of FF14SB is described under the chapter "AMBER force field terms".

## **1.2.3 SMIRNOFF**

SMIRNOFF (SMIRKS Natural Open Force Field) is a kind of small-molecule force field springing from the Open Force Field Initiative (OFF Initiative or OFFI) (https://openforcefield.org/). The key feature of this force field is its chemical representation of parameters by using extended SMARTS patterns. "Extended" here means that the SMARTS patterns also use atom assignment syntax from SMIRKS. For example,  $[\star:2] \sim [\star:1] \sim [\star:1]$  specifies three atoms, where the first is assigned to be atom 2, the second atom is assigned to be atom 1, and the third atom is not assigned. This format frees the force field from using atom types, instead it uses the direct chemical perception of the extended SMARTS patterns ([Mobley-2018]). Compared to traditional atom typing approaches, this representation greatly reduces the number of parameters needed to specify a general small-molecule force field and makes each parameter more independent.

While it currently has a traditional "Amber" type functional form as specified below, future versions expect to modify the functional form. The OFF Initiative will be releasing periodic revisions of the parameters which will include changes to the chemical specifications (i.e. the extended SMARTS patterns) as well as the numerical parameters. The revision used by the API points will be given with the results.

Currently SMIRNOFF force field has 6 similar to those in AMBER force field and are given below.

## 1.2.4 AMBER force field terms

Amber force field functional form has 6 terms:

$$
V_{AMBER} = \sum_{b} V_b + \sum_{a} V_a + \sum_{o} V_o + \sum_{t} V_t + \sum_{v} V_v + \sum_{c} V_c
$$

describing respectively bond stretching  $(b)$ , angle bending  $(a)$ , out-of-plane displacement  $(o)$ , torsion  $(t)$ , Van der Waals  $(v)$  and electrostatic  $(c)$  interactions.

## **Bond stretching**

For a bond b the stretching potential has a simple harmonic form:

$$
V_b = k_b (r - r_0)^2
$$

where  $k_b$  is the force constant, r, and  $r_0$  are actual and reference bond length, respectively.

### **Angle bending**

For bond angle  $a$ , the angle bending potential form is:

$$
V_a = k_a (\alpha - \alpha_0)^2
$$

where  $k_a$  is the force constant,  $\alpha$ , and  $\alpha_0$  are actual and reference bond angle values, respectively.

### **Torsion interactions**

Every 4 bonded atoms defined a torsion whose energy is represented with 1 to 6 terms of a Fourier series:

$$
V_t = \sum_n V_n / d_n (1 + \cos (p_n \theta - \gamma_n))
$$

where  $V_n$ ,  $d_n$ ,  $p_n$  and  $\gamma_n$  are barrier height, degeneracy, periodicity and phase for the *n* component of a torsion whose dihedral angle is  $\theta$ 

#### **Out-of-plane bending**

It is defined as potential of a displacement of the trigonal center atom  $a$  bonded to 3 other out-of-plane atoms,  $b$ ,  $c$  and d. Its functional form is similar to a regular torsion with a single term. Sometimes it is also called an *improper torsion*.

$$
V_o = V_n(1 + \cos(p_n \theta - \gamma_n))
$$

While in FF14SB this term is used to preserved planarity of the sp2 configuration, any improper torsion moving a central trigonal atom out of plane can be used, in SMIRNOFF this term has been redefined to account for the fact that one can define 3 improper torsions of moving a trigonal atom a out of plane defined by atoms  $b$ , c and d. The energy of such a displacement in SMIRNOFF is calculated as 1/3 of the sum of those torsions.

#### **Van der Waals interactions**

For a pair of nonbonded atoms *i* and *j*, SMIRNOFF force field adopts Lennard-Jones potential:

$$
V_v = \epsilon_{ij} \left[ \left( \frac{R_{ij}}{r_{ij}} \right)^{12} - 2 \left( \frac{R_{ij}}{r_{ij}} \right)^6 \right]
$$

where  $\epsilon_{ij}$  is well depth,  $R_{ij}$  and  $r_{ij}$  are the equilibrium and actual distance between atoms i and j, respectively.

## **Electrostatic interactions**

A simple Coulomb term:

$$
V_c = \frac{q_i q_j}{4\pi\epsilon_0 r_{ij}}
$$

represents Coulomb interactions, where  $q_i$  and  $q_j$  are partial atomic charges,  $\epsilon_0$  is the vacuum permittivity, and  $r_{ij}$  is the distance between atoms  $i$  and  $j$ .

## 1.2.5 MMFFAmber

#### **Intermolecular Amber potential**

Intermolecular interaction can be described by the Amber force field instead of MMFF potential:

$$
V_{Amber} = \sum_{i,j} \left\{ \epsilon_{ij} \left[ \left( \frac{R_{ij}}{r_{ij}} \right)^{12} - 2 \left( \frac{R_{ij}}{r_{ij}} \right)^{6} \right] + \frac{q_i q_j}{4 \pi \epsilon_0 r_{ij}} \right\}
$$

where the summation is over protein-ligand atom pairs.  $r_{ij}$  is the interatomic distance,  $R_{ij}$  is the VdW distance for a pair of atoms,  $q_i$  and  $q_j$  are the Amber partial charges on atoms i and j, and  $\epsilon_0$  is the vacuum permittivity. VdW parameters  $R_{ij}$  and  $\epsilon_{ij}$  and partial charges are taken from work by Wang and coworkers ([Wang-J-2000]).

## 1.2.6 MMFFIEFF

#### **Intermolecular IEFF potential**

Intermolecular interaction can be described by the IEFF (Intermolecular Force Field) instead of MMFF potential.

The IEFF is an ongoing development effort internally at OpenEye to obtain high accuracy Intermolecular Force Field. The initial development of IEFF was done during 2010. The goal of the initial development was to prove internally at OpenEye as well as to external collaborators that point charge monopole approximation in the Coulomb terms are inadequate to capture intermolecular Coulomb interactions within chemical accuracy (within about 1 kcal/mol) regardless of the charge models used. The higher accuracy in the Coulomb terms is especially important and vital in optimizing and ranking organic crystal structures. The initial IEFF development has had some successful crystal predictions. It has also clearly shown, for the formamide dimer case, that there is a 1D energy curve along a given torsion angle where all tested point charge models fails even qualitatively showing repulsive interactions while accurate ab-initio calculations and IEFF with multipole based Coulomb interactions show a minimum along the torsion with great agreement to each other.

The IEFF has not been improved significantly since those initial academic studies and cannot be considered as a general purpose intermolecular force field due to lack of sufficient coverage. However, major development effort is underway to make IEFF an industry quality general intermolecular force field.

The currently available IEFF supports only a few selected elements that were the most important ones for organic crystal predictions, including H, C, N, O, S, F, and Cl. The atomic multipoles are obtained by an internal analysis program that obtains the SCF converged density matrices from ab-initio (PSI4) calculations. The current IEFF does not use any atom types, all VdW parameters are associated to each element types. This obviously introduces a very significant weakness especially for hydrogens where both polar and apolar hydrogens share the same FF parameters but it is also important deficiency for other elements as well. The new version of the IEFF that is under development will try to address all of these deficiencies.

# **1.3 Sheffield Model**

## **1.3.1 Small molecules**

The "Sheffield Solvation Model" [Grant-2007] is a simple two parameter model for calculating the electrostatic component of molecular solvation energy. The Sheffield model is robust and works well for calculating solvation energies of small drug-like molecules with good accuracy, when compared against the more accurate Poisson-Boltzmann calculations, and requires significantly low computational resource. The model is represented by the following simple expression:

$$
E_{Sheff} = -\frac{f_{\epsilon}}{4\pi\epsilon_0} \frac{1}{2} \sum_{i,j} \frac{Q_i Q_j}{\sqrt{A\sigma_i \sigma_j + BR_{ij}^2}}
$$

where  $f_{\epsilon}$  is

$$
f_{\epsilon}=\frac{1}{\epsilon_{in}}-\frac{1}{\epsilon_{out}}
$$

and  $\epsilon_{in}$ ,  $\epsilon_{out}$  are he relative permittivities (dielectric constants) in solute and solvent, respectively.  $Q_i$  and  $Q_j$  are charges on atoms i and j,  $\sigma_i$  and  $\sigma_j$  are corresponding atomic radii, and  $R_{ij}$  is an interatomic distance between atoms i and j.  $A$  and  $B$  are parameters to the model.

This model works well in the situation where atoms in molecules are well exposed to the solvent. In macromolecules like proteins, this condition is not met.

# 1.3.2 Proteins

In order to apply Sheffield model for proteins and complexes a modification is required to correct the atomic radii according to their exposure to solvent. The correction to atomic radii is applied by introduction of a third parameter to the original two parameter model.

$$
\sigma_i = \sigma_{0,i} + C \left( 1 - \sqrt{\frac{S_i}{S_{0,i}}} \right)
$$

where  $S_i$  and  $S_{0,i}$  are atomic contributions to the solvent accessible surface of atom i in the protein and in a residue to which it belongs which was isolated from the rest of the protein. Initial atomic radii  $\sigma_{0,i}$  was assumed to be of ZAP9 [Nicholls-2010] type.

# **CHAPTER**

**TWO** 

# **OEFF EXAMPLES**

# 2.1 Simple Functions and Optimization

# 2.1.1 Solving a simple equation

The following example illustrates how to define a simple objective function. By deriving the objective function from OEFunc2, we can find the roots of the simple quadratic equation using OENewtonOpt optimizer. A class derived from OEFunc2 must contain analytical gradients and Hessians. This example expects a number as input for the initial guess to solve the simple function.

## Listing 1: Define a simple objective function

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
#\}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}
# The following function is a contrived example to show how to
                                                                         \frac{1}{2}# write a user-defined objective function and optimize it. The simple
                                                                         \frac{1}{2}# function defines a quadradic equation, and contains expressions for
                                                                         \frac{1}{2}# gradient and second derivative of the function.
                                                                         \frac{1}{2},,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
```

```
class Function (oeff.OEFunc2):
    def __init__(self):oeff.OEFunc2.__init__(self)
        pass
    def begin (self) :
        pass
    def NumVar(self):
        return 1
    def _call_(self, x, h=None, g=None):
        if isinstance(x, oechem.OEDoubleArray):
            if q is not None:
                 g[0] = 2.0 \times x[0] - 7.0 # gradient
                 h[0] = 2.0 # hessien
                 return True
            elif h is not None:
                 h[0] = 2.0 \times x[0] - 7.0 # gradient
                 return x[0]*x[0]-7*x[0]+63else:
                 return x[0]*x[0]-7*x[0]+63else:
            x1 = occhem.OEDoubleArray(x, self.NumVar(), False)
            if q is not None:
                 g1 = oechem. OEDoubleArray (g, self. NumVar(), False)
                 q1[0] = 2.0 \times x1[0]-7.0h1 = occhem.OEDoubleArray(h, self.NumVar(), False)
                 h1[0] = 2.0return True
            elif h is not None:
                 h1 = oechem. OEDoubleArray (h, self. NumVar (), False)
                 h1[0] = 2.0 \times x1[0] - 7.0return x1[0]*x1[0]-7*x1[0]+63else:
                 return x1[0]*x1[0]-7*x1[0]+63def main (args) :
    if len(args) != 2:
        oechem. OEThrow. Usage ("%s <initial guess>" % args [0])
    x = occhem.OEDoubleArray(1)try:
        x[0] = float(args[1])except ValueError:
        oechem. OEThrow. Usage ("%s <initial quess (expecting a number) >" % args [0])
    func = Function()# Calculate function value at given x
    value = func(x)oechem. OEThrow. Info ("Function value at x = \frac{2}{3}d is \frac{2}{3}d'' + \frac{2}{3} (x[0], value))
    # Optimize function using BFGS Optimizer and checkpoint
    xOpt = occhem.OEDoubleArray(1)
```

```
optimize r = oeff. 0ENewtonOpt()
    value = optimize(func, x, x0pt)oechem. OEThrow. Info ("Function has a minimia at x = \frac{2}{3}d and the minimum value is \frac{2}{3}d"
                           % (xOpt[0], value)return 0
if __name__ == "__main__\sim 0.1sys.exit(main(sys.argv))
```

## 2.1.2 Using checkpoints for optimization monitoring

The following example illustrates how to define checkpoints and use then along with optimizers to monitor progress during optimization. For simplicity, a simple quadratic equation is defined as objective function and derived from  $OEFunc1$ . The quadratic equation is solved using the  $OEBFGSOpt$  optimizer. A class derived from  $OEFunc1$  must contain analytical gradients. This examples expects a number as input for the initial guess to solve the simple function.

#### Listing 2: Define and use checkpoints

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
# The following function displays how to use a checkpoint during function //
# optimization. A simple quadradic equation is minimized for which the
                                                                       \frac{1}{2}# analytical gradient is provided but the second derivative is not.
                                                                       \frac{1}{2}# ////////////////////////////////////
class Function (oeff. OEFunc1) :
   def init (self):
```

```
oeff.OEFunc1.__init__(self)
        pass
    def begin(self):
        pass
    def NumVar (self) :
        return 1
   def _call_(self, x, g=None):
        if isinstance(x, oechem.OEDoubleArray):
            if g is not None:
                g[0] = 2.0 \times x[0] - 7.0return x[0]*x[0]-7*x[0]+63Also:return x[0]*x[0]-7*x[0]+63else:
            x1 = occhem.OEDoubleArray(x, self.NumVar(), False)
            if g is not None:
                g1 = oechem. OEDoubleArray (g, self. NumVar(), False)
                q1[0] = 2.0 \times x1[0] - 7.0return x1[0]*x1[0]-7*x1[0]+63Also:return x1[0]*x1[0]-7*x1[0]+63class ChkPt (oeff.OECheckpoint0):
   def init (self):
        oeff.OECheckpoint0.__init__(self)
        pass
    def _call_(self, iteration, nvar, fval, var, state):
        # Intermediate information during optimization
        var1 = oechem. 0EDoubleArray(var, 1, False)oechem. OEThrow. Info ("iteration: %d x: %d value: %d state: %d"
                            % (iteration, var1[0], fval, state))
        # To demonstrate how to force quitting optimization from checkpoint
        # this returns false when iteration is 5
        if iteration >= 5:
            return False
        else:
            return True
def main (args) :
    if len(args) != 2:
        oechem.OEThrow.Usage("%s <initial guess>" % args[0])
   x = occhem.OEDoubleArray(1)try:
        x[0] = float(args[1])except ValueError:
        oechem. OEThrow. Usage ("% s <initial quess (expecting a number) >" % args [0])
    func = Function()
```

```
# Calculate function value at given x
    value = func(x)oechem. OEThrow. Info ("Function value at x = \frac{2}{3}d is \frac{2}{3}d'' - \frac{2}{3} (x[0], value))
    # Optimize function using BFGS Optimizer and checkpoint
    xOpt = occhem. 0EDoubleArray(1)optimizer = oeff.OEBFGSOpt()
    value = optimizer (func, ChkPt (), x, xOpt)
    oechem. OEThrow. Info ("Function has a minimia at x = \frac{2}{3}d and the minimum value is \frac{2}{3}d"
                           \frac{1}{6} (xOpt[0], value))
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# **2.2 Molecule Functions**

# 2.2.1 User defined molecule function

The following example illustrates how to define an objective function within the context of a molecule. Generally speaking, a molecule function (*OEMolFunc*) defines some sort of interaction involving a part or all of a molecule. For simplicity, a simple energy function is defined that consists sum of square of distance of all the atoms in the molecule. The molecule function is optimized using the OEBFGSOpt optimizer. A class derived from OEMolFunc1 must contain analytical gradients.

### Listing 3: Define an objective function within the context of a molecule

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
```

```
# The following function is a contrived example to show how to
                                                                            \frac{1}{2}# write a user-defined function. The energy function is the square
                                                                            \sqrt{}# of the distance from the origin. The derivative then is two times the
                                                                            \frac{1}{2}# coordinate component. The function will attempt to place all atoms of
                                                                            \frac{1}{2}# a molecule at the origin.
                                                                            \frac{1}{2}# /////////////////////////////////////
class Harmonic (oeff.OEMolFunc1) :
   def __init__(self):oeff.OEMolFunc1.__init__(self)
        self.natoms = 0pass
   def begin(self):
       pass
   def NumVar (self):
        return 3*self.natoms
   def Setup(self, mol):
        self.natoms = mol.GetMaxAtomIdx()
        return True
    def _call_(self, coord, grad=None) :
        energy = 0.0if isinstance (coord, oechem. OEDoubleArray):
            if grad is not None:
                for i in range (0, self. natoms):
                    grad[3*1] += 2.0 * coord[3*i] # x gradient
                    grad[3* i+1] += 2.0 * coord[3* i+1] # y gradientgrad[3*1+2] += 2.0 * coord[3*1+2] # z gradientenergy +=\text{coord}[3*1] * \text{coord}[3*1] * x distance from zero
                    energy += coord[3*i+1] * coord[3*i+1] # y distance from zero
                    energy += coord[3*i+2] * coord[3*i+2] # z distance from zero
            else:
                for i in range (0, \text{ self.natoms}):
                    energy += coord[3*i] * coord[3*i] # x distance from zero
                    energy += coord[3*i+1] * coord[3*i+1] # y distance from zero
                    energy += coord[3*1+2] * coord[3*1+2] # z distance from zeroelse:
            coord1 = oechem. OEDoubleArray (coord, self. NumVar (), False)
            if grad is not None:
                grad1 = oechem. OEDoubleArray (grad, self. NumVar(), False)
                for i in range (0, self.natoms):
                    grad1[3*1] += 2.0 * coord1[3*1] # x gradientgrad1[3* i+1] += 2.0 * coord1[3* i+1] # y gradientgrad1[3* i+2] += 2.0 * coord1[3* i+2] # z gradientenergy += coord1[3*i] * coord1[3*i] # x distance from zero
                    energy += coord1[3*i+1] * coord1[3*i+1] # y distance from zero
                    energy += coord1[3*i+2] * coord1[3*i+2] # z distance from zero
            else:
                for i in range(0, self.natoms):
                    energy += coord1[3*i] * coord1[3*i] # x distance from zero
                    energy += coord1[3*i+1] * coord1[3*i+1] # y distance from zero
                    energy += coord[3*1+2] * coord[3*1+2] # z distance from zero
        return energy
```

```
def main (args) :
    if len(args) != 2:
        oechem.OEThrow.Usage("%s <input>" % args[0])
    if s = oechem. oemolistream()if not ifs.open(arg[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   mol = occhem. OEGraphMol()oechem.OEReadMolecule(ifs, mol)
   vecCoordinates = oechem. OEDoubleArray(3*mol. GetMaxAtomIdx())mol.GetCoords(vecCoords)
   hermonic = Harmonic()hermonic.Setup(mol)
   optimizer = oeff.OEBFGSOpt()
    energy = optimizer (hermonic, vecCoords, vecCoords)
    oechem.OEThrow.Info("Optimized energy: \frac{2}{3}d" % energy)
    return 0
if _name_ = = "_main_".sys.exit(main(sys.argv))
```

# 2.3 Small Molecule Force fields

## 2.3.1 Single ligand in vacuum

The following example illustrates how to calculate energy and optimize a single ligand in vacuum. The molecule needs to be prepared (OEForceField, PrepMol), followed by a call to OEMolFunc, Setup to create the interactions. Optimization is carried out using the OEBFGSOpt optimizer.

#### Listing 4: Calculate energy and optimize a single ligand in vacuum

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
```

```
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
# The following example demonstrates how to perform ligand optimization
# ////////////////////////////////////
class FFOptions (oechem. OEOptions) :
   def init (self):oechem.OEOptions. init (self, "FFOptions")
       ffType = oechem. OEStringParameter("-ff", "parsley")
       ffType.AddLegalValue("parsley")
       ffType.AddLegalValue("mmff94")
       ffType.AddLegalValue("mmff94s")
       ffType.SetBrief("Force field type")
       self._fftype = self.AddParameter(ffType)
       pass
   def CreateCopy (self) :
       return self
   def GetFF(self):
       ff = self._fftype.GetStringValue()
       if ff == ".
           ff = self._fftype.GetStringDefault()
       if ff = "mmff94":
           return oeff.OEMMFF()
       elif ff == "mmff94s":
           return oeff.OEMMFF(oeff.OEMMFF94sParams())
       else:return oeff.OEParsley()
def main(argy=[ name ]):
   ffOpts = FFOptions()opts = oechem.OESimpleAppOptions(ffOpts, "FFOptimize", oechem.OEFileStringType_
\rightarrowMol3D,
                                    oechem.OEFileStringType_Mol3D)
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
       return 0
   ffOpts. UpdateValues (opts)
   ifs = oechem.oemolistream()
   if not ifs.open(opts.GetInFile()):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
```

```
ff = ffOpts.GetFF()for mol in ifs. GetOEMols():
        print ("Optimizing", mol. GetTitle())
        if not ff. PrepMol(mol) or not ff. Setup(mol):
             oechem. OEThrow. Warning ("Unable to process molecule: title = ' %s'" % mol.
\rightarrowGetTitle())
             oechem.OEWriteMolecule(ofs, mol)
             continue
        vecCoordinates = oechem. OEDoubleArray(3*mol.fetMaxAtomIdx())for conf in mol. GetConfs():
            oechem. OEThrow. Info("Molecule: %s Conformer: %d" % (mol. GetTitle(), conf.
\rightarrow GetIdx()+1))
            conf.GetCoords(vecCoords)
             # Calculate energy
             energy = ff(vecCoordinates)oechem. OEThrow. Info ("Initial energy: \frac{2}{3}0.2f kcal/mol" % energy)
             # Optimize the ligand
            optimizer = oeff.OEBFGSOpt()
             energy = optimizer(ff, vecCoords, vecCoords)
             oechem. OEThrow. Info ("Optimized energy: 80.2f kcal/mol" % energy)
             conf.SetCoords(vecCoords)
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if _name_ = = "_main_".sys.exit(main(sys.argv))
```

# 2.3.2 Energy components of a single ligand in vacuum

The following example illustrates how to obtain various intermolecular energy components of a single ligand in vacuum.

### Listing 5: Obtain intermolecular energy components of a single ligand in vacuum

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
                                                                          (continues on next page)
```

```
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
# The following is an example to show how to evaluate energies
                                                                         \frac{1}{2}# of a small molecule and obtain various energy components.
# ////////////////////////////////////
class FFOptions (oechem. OEOptions) :
   def __init__(self):oechem.OEOptions.__init__(self, "FFOptions")
       ffType = oechem. OEstringParameter(" - ff", "parsey")ffType.AddLegalValue("parsley")
       ffType.AddLegalValue("mmff94")
       ffType.AddLegalValue("mmff94s")
       ffType.SetBrief("Force field type")
       self._fftype = self.AddParameter(ffType)
       pass
   def CreateCopy(self):
       return self
   def GetFF(self):
       ff = self. _fftype. GetStringValue()
       if ff == m.
           ff = self. fftype. GetStringDefault()if ff == "mmff94":
           return oeff.OEMMFF()
       elif ff == "mmff94s":
           return oeff.OEMMFF(oeff.OEMMFF94sParams())
       else:return oeff.OEParsley()
def main(argv=[_name_]):
   ffiopts = FFOptions()
   opts = oechem.OESimpleAppOptions(ffOpts, "FFEnergy", oechem.OEFileStringType
\rightarrowMol3D.
                                    oechem.OEFileStringType_Mol3D)
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
       return 0
   ffOpts. UpdateValues (opts)
   if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oemolostream()
```

```
if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    ff = ffOpts.GetFF()for mol in ifs. GetOEMols():
        if not ff. PrepMol(mol) or not ff. Setup(mol):
            oechem. OEThrow. Warning ("Unable to process molecule: title = '%s'" % mol.
\rightarrowGetTitle())
            oechem.OEWriteMolecule(ofs, mol)
            continue
        vecCoords = oechem. OEDoubleArray (3*mol. GetMaxAtomIdx())
        for conf in mol. GetConfs():
            oechem.OEThrow.Info("Molecule: %s Conformer: %d" % (mol.GetTitle(), conf.
\rightarrow GetIdx()+1))
            conf.GetCoords(vecCoords)
            for fcomp in ff.GetFComponents (vecCoords):
                 oechem.OEThrow.Info("Component: %s Energy: %0.2f kcal/mol"
                                      % (fcomp.name, fcomp.value))
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if name == " main ":
    sys.exit(main(sys.argy))
```

## 2.3.3 MMFF interactions of a single ligand

The following example illustrates how to obtain various interactions of a single ligand in the context of a force field.

Listing 6: Obtain interactions of a single ligand in the context of a force field

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
```

```
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
# The following example demonstrates how to obtain interactions
                                                                         \frac{1}{2}# of a small molecule in the context of a force field.
                                                                         \frac{1}{2}# ////////////////////////////////////
class FFOptions (oechem. OEOptions) :
   def __init__(self):oechem.OEOptions.__init__(self, "FFOptions")
       ffType = oechem. OESTringParameter('fff', "parsev")ffType.AddLegalValue("parsley")
       ffType.AddLegalValue("mmff94")
       ffType.AddLegalValue("mmff94s")
       ffType.SetBrief("Force field type")
       self._fftype = self.AddParameter(ffType)
       pass
   def CreateCopy(self):
       return self
   def GetFF(self):
       ff = self._fftype.GetStringValue()
       if ff == ".
           ff = self._fftype.GetStringDefault()
       if ff == "mmff94":
           return oeff.OEMMFF()
       elif ff == "mmff94s":
           return oeff.OEMMFF(oeff.OEMMFF94sParams())
       else:
           return oeff.OEParsley()
def main(argv=[_name_]):
   ffOpts = FFOptions()opts = oechem.OESimpleAppOptions(ffOpts, "FFInteractions", oechem.
\rightarrowOEFileStringType_Mol3D,
                                    oechem.OEFileStringType_Mol3D)
   if oechem. OEConfigureOpts (opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
       return 0
    ffOpts. UpdateValues (opts)
   if s = oechem.oemolistream()if not ifs.open(opts.GetInFile()):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    ff = ffOpts.GetFF()for mol in ifs. GetOEMols():
```

```
(continued from previous page)
```

```
if not ff. PrepMol(mol) or not ff. Setup(mol):
            oechem. OEThrow. Warning ("Unable to process molecule: title = '%s'" % mol.
\rightarrowGetTitle())
            oechem.OEWriteMolecule(ofs, mol)
            continue
        vecCoordinates = oechem. OEDoubleArray(3*mol. GetMaxAtomIdx())for conf in mol. GetConfs():
            oechem.OEThrow.Info("Molecule: %s Conformer: %d" % (mol.GetTitle(), conf.
\rightarrowGetIdx()+1))
            conf.GetCoords(vecCoords)
            for inte in ff.GetInteractions(mol, vecCoords):
                vecGrads = occhem. OEDoubleArray(intc.WamValues())oechem.OEThrow.Info("Interaction: % Value: %0.2f"
                                      % (intc.GetName(), intc.GetValues(vecGrads)))
                for atom in intc. GetAtoms () :
                     oechem. OEThrow. Info ("Atom index: %d" % atom. GetIdx ())
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# **2.4 Protein-Ligand Complexes**

# 2.4.1 Protein-ligand optimization

The following example illustrates how to set up a ligand optimization within the context of a protein contained in a design unit.

## Listing 7: Set up a ligand optimization

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
```

```
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
# The following example demonstrates how to perform ligand optimization //
# in the context of a protein using a complex force field.
                                                                         \frac{1}{2}# ////////////////////////////////////
class FFOptions (oechem. OEOptions) :
   def init (self):
       oechem.OEOptions.__init__(self, "FFOptions")
       ffType = oechem. OEStringParameter("-ff", "ff14sb_parsley")
       ffType.AddLegalValue("ff14sb_parsley")
       ffType.AddLegalValue("mmff_amber")
       ffType.AddLegalValue("mmff")
       ffType.SetBrief("Force field type")
       self. _fftype = self.AddParameter(ffType)
       pass
   def CreateCopy (self) :
       return self
   def GetFF(self):
       ff = self._fftype.GetStringValue()
       if ff == ".
           ff = self._fftype.GetStringDefault()
       if ff == "mmff":return oeff.OEMMFFComplex()
       elif ff == "mmff\_amber":return oeff.OEMMFFAmberComplex()
       else:
           return oeff.OEFF14SBParsleyComplex()
def main(argv=[_name_]):
    ffOpts = FFOptions()opts = oechem.OERefInputAppOptions(ffOpts, "FFComplexOpt", oechem.
\rightarrowOEFileStringType_Mol3D,
                                      oechem.OEFileStringType_Mol3D, oechem.
\rightarrowOEFileStringType_DU, "-protein")
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
       return 0
   ffOpts. UpdateValues (opts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
       oechem. OEThrow. Fatal ("Unable to open % for reading" % opts. GetInFile())
    rfs = oechem.oeifstream()if not rfs.open(opts.GetRefFile()):
```

```
oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    du = oechem. 0EDesignUnit()if not oechem. OEReadDesignUnit (rfs, du) :
        oechem. OEThrow. Fatal ("Failed to read design unit")
    protein = oechem. OEGraphMol()
    du.GetProtein (protein)
    ff = ffOpts.GetFF()if not ff.SetupHost (protein):
        oechem. OEThrow. Fatal ("Failed to setup protein: %s" % protein. GetTitle())
    for mol in ifs. GetOEMols():
        print ("Optimizing", mol. GetTitle())
        if (not ff. Setup(mol)):
            oechem. OEThrow. Warning ("Unable to process molecule: title = 's s'" s mol.
\rightarrowGetTitle())
            oechem.OEWriteMolecule(ofs, mol)
            continue
        vecCoordinates = oechem. OEDoubleArray(3*mol.GetMaxAtomIdx())for conf in mol. GetConfs():
            oechem.OEThrow.Info("Molecule: %s Conformer: %d" % (mol.GetTitle(), conf.
\rightarrow GetIdx()+1))
            conf.GetCoords(vecCoords)
             # Calculate energy
            energy = ff(vecCoordinates)oechem. OEThrow. Info ("Initial energy: \frac{2}{3}0.2f kcal/mol" % energy)
            # Optimize the ligand
            optimizer = oeff.OEBFGSOpt()
            energy = optimizer(ff, vecCoords, vecCoords)
            oechem. OEThrow. Info ("Optimized energy: %0.2f kcal/mol" % energy)
            conf.SetCoords(vecCoords)
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if _name == "_main_":
    sys.exit(main(sys.argv))
```

# **2.5 Using adaptors**

## 2.5.1 Optimizing a single ligand with fixed atoms

The following example illustrates how to fix a subset of atoms using the OESubsetAdaptor during a single ligand optimization in vacuum. The adaptor is initialized with the force field interactions of the ligand, and passed as the objective function to be optimized. Methods of the adaptor are used to convert between the Cartesian coordinates of the ligand and the adaptor variables.

## Listing 8: Fix a subset of atoms

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
# The following is an example to show how to evaluate energy
                                                                         \frac{1}{2}# and optimize a small molecule, with keeping a subset of atoms fixed.
                                                                         \frac{1}{2}# ////////////////////////////////////
class FFOptions (oechem. OEOptions):
   def __init__(self):oechem.OEOptions.__init__(self, "FFOptions")
       ffType = oechem. OEStringParameter ("-ff", "parsley")
       ffType.AddLegalValue("parsley")
       ffType.AddLegalValue("mmff94")
       ffType.AddLegalValue("mmff94s")
       ffType.SetBrief("Force field type")
       self._fftype = self.AddParameter(ffType)
       pass
   def CreateCopy(self):
       return self
   def GetFF(self):
```

```
(continued from previous page)
```

```
\mathsf{ff} = \mathsf{self}. \mathsf{fftype}. GetStringValue()
        if ff == ".
            ff = self. _fftype.GetStringDefault()
        if ff = "mmff94":
            return oeff.OEMMFF()
        elif ff == "mmff94s":
            return oeff.OEMMFF(oeff.OEMMFF94sParams())
        else:return oeff.OEParsley()
def main(argv=[_name_]):
    ffOpts = FFOptions()opts = oechem.OESimpleAppOptions(ffOpts, "FFSubset", oechem.OEFileStringType
\rightarrowMol3D.
                                       oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    ffOpts. UpdateValues (opts)
    if s = oechem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    ff = ffOpts.GetFF()# Setup adaptor. The first (false) means not to pass ownership of ff,
    # and the second (false) means not to exclude interactions related
    # to the subset which would be fixed for calculations.
    adaptor = oeff.OESubsetAdaptor(ff, False, False)
    # Use a simple atoms predicate for the subset
    adaptor.Set(oechem.OEIsCarbon())
    for mol in ifs. GetOEMols():
        print ("Optimizing", mol. GetTitle())
        if not ff. PrepMol(mol) or not adaptor. Setup(mol):
            oechem. OEThrow. Warning ("Unable to process molecule: title = '%s'" % mol.
\rightarrowGetTitle())
            oechem.OEWriteMolecule(ofs, mol)
            continue
        vecCoordinates = occhem.OEDoubleArray(3*mol.GetMaxAtomIdx())for conf in mol. GetConfs():
            oechem.OEThrow.Info("Molecule: %s Conformer: %d" % (mol.GetTitle(), conf.
\rightarrow GetIdx()+1))
            conf.GetCoords(vecCoords)
            # Get adaptor variables set corresponding to the coordinates
            vecX = occhem. OEDoubleArray (adaptor. NumVar())
            adaptor.GetVar(vecX, vecCoords)
```

```
# Calculate energy using adaptor
            energy = adaptor (vecX)oechem. OEThrow. Info ("Initial energy: 80.2f kcal/mol" % energy)
             # Optimize the adaptor
            optimize r = oeff.OEBFGSOpt()energy = optimizer (adaptor, vecX, vecX)
            oechem.OEThrow.Info("Optimized energy: %0.2f kcal/mol" % energy)
             # Get optimized coordinates corresponding to the adaptor optimized,
\leftrightarrowvariables
            adaptor. AdaptVar (vecCoords, vecX)
            conf.SetCoords(vecCoords)
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if _name__ == " _main_
                         \mathbf{m}_2sys.exit(main(sys.argv))
```

# 2.5.2 Optimizing a single ligand torsions

The following example illustrates how to optimize a set of torsion angles using the OETorAdaptor for a single ligand in vacuum. The adaptor is initialized with the force field interactions of the ligand, and passed as the objective function to be optimized. Methods of the adaptor are used to convert between the Cartesian coordinates of the ligand and the adaptor variables.

### Listing 9: Optimize a set of torsion angles

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
```

```
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# The following is an example to show how to evaluate energy
                                                                          \frac{1}{2}# and optimize a set of torsions in a small molecule
                                                                          \frac{1}{2}# ////////////////////////////////////
class FFOptions (oechem. OEOptions) :
   def __init__(self):oechem.OEOptions.__init__(self, "FFOptions")
       ffType = oechem. OEStringParameter ("-ff", "parsley")
       ffType.AddLegalValue("parsley")
       ffType.AddLegalValue("mmff94")
       ffType.AddLegalValue("mmff94s")
       ffType.SetBrief("Force field type")
       self._fftype = self.AddParameter(ffType)
       pass
    def CreateCopy (self) :
       return self
   def GetFF(self):
       ff = self._fftype.GetStringValue()
       if ff == ".
           ff = self._fftype.GetStringDefault()
       if ff == "mmff94":
           return oeff.OEMMFF()
       elif ff == "mmff94s":
           return oeff.OEMMFF(oeff.OEMMFF94sParams())
       else:return oeff.OEParsley()
def main(argv=[_name_]):
   ffOrts = FPOptions()opts = oechem.OESimpleAppOptions(ffOpts, "FFTorAdaptor", oechem.OEFileStringType_
\leftrightarrowMol3D,
                                    oechem.OEFileStringType_Mol3D)
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
       return 0
   ffOpts. UpdateValues (opts)
   if s = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   ff = ffOpts.GetFF()# Setup adaptor. The first (false) means not to pass ownership of mmff,
    # and the second (false) means not to exclude interactions related
    # to the subset which would be fixed for calculations.
    adaptor = oeff.OETorAdaptor(ff, False, False)
```

```
# Use a simple predicate for the subset of torsions to optimize
    adaptor.Set(oechem.OEIsRotor())
    for mol in ifs. GetOEMols():
        print ("Optimizing", mol. GetTitle())
        if not ff. PrepMol(mol) or not adaptor. Setup (mol) :
             oechem. OEThrow. Warning ("Unable to process molecule: title = '%s'" % mol.
\rightarrowGetTitle())
             oechem.OEWriteMolecule(ofs, mol)
            continue
        vecCoordinates = oechem. OEDoubleArray(3*mol.GetMaxAtomIdx())for conf in mol. GetConfs():
            oechem.OEThrow.Info("Molecule: %s Conformer: %d" % (mol.GetTitle(), conf.
\rightarrow GetIdx()+1))
             conf.GetCoords(vecCoords)
             # Get adaptor variables set corresponding to the coordinates
            vecX = occhem. OEDoubleArray (adaptor. NumVar())adaptor.GetVar (vecX, vecCoords)
             # Calculate energy using adaptor
             energy = adapter (vecX)oechem. OEThrow. Info ("Initial energy: \frac{2}{3}0.2f kcal/mol" % energy)
             # Optimize the adaptor
             optionizer = oeff.OEBFGSOpt()energy = optimizer(adaptor, vecX, vecX)
             oechem. OEThrow. Info ("Optimized energy: % 0.2f kcal/mol" % energy)
             # Get optimized coordinates corresponding to the adaptor optimized
\leftrightarrowvariables
             adaptor.AdaptVar(vecCoords, vecX)
             conf.SetCoords(vecCoords)
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# 2.5.3 Optimizing rigid ligand in protein

The following example illustrates how to perform rigid optimization of a ligand in the context of a protein using the OEQuatAdaptor. The adaptor is initialized with the protein-ligand interactions, and passed as the objective function to be optimized. Methods of the adaptor are used to convert between the Cartesian coordinates of the ligand and the adaptor variables.

## Listing 10: Perform rigid optimization of a ligand

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
# ////////////////////////////////////
# The following example demonstrates how to perform rigid optimization of //
# a ligand in the context of a protein. The OEQuatAdaptor it used for
                                                                        \!/# rigid optimization.
# ////////////////////////////////////
class FFOptions (oechem. OEOptions) :
   def __init__(self):oechem.OEOptions.__init__(self, "FFOptions")
       ffType = oechem. OEStringParameter ("-ff", "ff14sb_parsley")
       ffType.AddLegalValue("ff14sb_parsley")
       ffType.AddLegalValue("mmff_amber")
       ffType.AddLegalValue("mmff")
       ffType.SetBrief("Force field type")
       self._fftype = self.AddParameter(ffType)
       pass
   def CreateCopy(self):
       return self
   def GetFF(self):
       ff = self._fftype.GetStringValue()
       if ff == ":
```

```
ff = self._fftype.GetStringDefault()
        if ff == "mmff":return oeff.OEMMFFComplex()
        elif ff == "mmff\_amber":return oeff.OEMMFFAmberComplex()
        else:
            return oeff.OEFF14SBParsleyComplex()
def main(argv=[_name_]):
    ffopts = FFOptions()opts = oechem.OERefInputAppOptions(ffOpts, "FFComplexQuat", oechem.
\rightarrowOEFileStringType_Mol3D,
                                         oechem.OEFileStringType Mol3D, oechem.
→OEFileStringType_DU, "-protein")
    if oechem. OEConfigureOpts (opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return <sub>0</sub>ffOpts. UpdateValues (opts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    rfs = oechem.oeifstream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    du = oechem.OEDesignUnit()
    if not oechem. OEReadDesignUnit (rfs, du) :
        oechem. OEThrow. Fatal ("Failed to read design unit")
    protein = oechem. OEGraphMol()
    du.GetProtein(protein)
    ff = ffOrts.GetFF()if not ff.SetupHost (protein):
        oechem. OEThrow. Fatal ("Failed to setup protein: %s" % protein. GetTitle())
    adap = oeff.OEQuatAdaptor (ff)for mol in ifs. GetOEMols():
        print ("Optimizing", mol. GetTitle())
        if not adap. Setup (mol) :
            oechem. OEThrow. Warning ("Unable to process molecule: title = 's s'" s mol.
\rightarrowGetTitle())
            oechem.OEWriteMolecule(ofs, mol)
            continue
        vecCoordinates = occhem. 0EDoubleArray(3*mol. GetMaxAtomIdx())for conf in mol. GetConfs():
            oechem.OEThrow.Info("Molecule: %s Conformer: %d" % (mol.GetTitle(), conf.
\rightarrow GetIdx () +1))
            conf.GetCoords(vecCoords)
```

```
vecX = occhem. OEDoubleArray (adap. NumVar())adap.GetVar(vecX, vecCoords)
            # Calculate energy
            energy = adap(vecX)oechem. OEThrow. Info ("Initial energy: \frac{2}{3}0.2f kcal/mol" % energy)
            # Optimize the ligand
            optimizer = oeff.OEBFGSOpt()
            energy = optimizer (adap, vecX, vecX)oechem. OEThrow. Info ("Optimized energy: % 0.2f kcal/mol" % energy)
            adap.AdaptVar(vecCoords, vecX)
            conf.SetCoords(vecCoords)
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# **2.6 Custom Force Fields**

# 2.6.1 Custom Smirnoff

The following example illustrates how to load custom SMIRNOFF force field parameters from an OFFXML file and use that to calculate energy and optimize a single ligand in vacuum.

#### Listing 11: Load custom SMIRNOFF force field parameters

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
# subject to these terms. Cadence claims no rights to Customer's
# modifications. Modification of Sample Code is at Customer's sole and
# exclusive risk. Sample Code may require Customer to have a then
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeff
```

```
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
# The following example demonstrates how to load a custom Smirnoff
                                                                             \frac{1}{2}# forcefield, and use that to optiiza a ligand.
                                                                             \frac{1}{2}# ////////////////////////////////////
class FFOptions (oechem. OEOptions) :
   def __init__(self):oechem.OEOptions.__init__(self, "FFOptions")
        fffype = oechem. OESTringParameter("-ff", "")ffType.SetBrief("Force field XML file")
        self._fftype = self.AddParameter(ffType)
        pass
    def CreateCopy(self):
        return self
    def GetXML(self):
        ffxml = self._fftype.GetStringValue()
        if ffxml == "ffxml = self._fftype.GetStringDefault()
        return ffxml
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
   ffOpts = FFOptions()opts = oechem. OESimpleAppOptions(ffOpts, "FFCustomSmirnoff", oechem.
\rightarrowOEFileStringType_Mol3D,
                                      oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    ffOpts. UpdateValues (opts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   params = oeff.OESmirnoffParams()
    if fffOpts. GetXML() != "":
        if not params. Load (ffOpts. GetXML()):
            oechem. OEThrow. Fatal ("Unable to load force field parameters: %s" % ffOpts.
\rightarrow Get XML() )
   ff = oeff.OESmirnoff(params)for mol in ifs. GetOEMols():
        print ("Optimizing", mol. GetTitle())
        if not ff. PrepMol(mol) or not ff. Setup(mol):
            oechem. OEThrow. Warning ("Unable to process molecule: title = '%s'" % mol.
\rightarrowGetTitle())
            oechem.OEWriteMolecule(ofs, mol)
            continue
```

```
vecCoordinates = oechem. OEDoubleArray(3*mol. GetMaxAtomIdx())for conf in mol. GetConfs():
            oechem.OEThrow.Info("Molecule: %s Conformer: %d" % (mol.GetTitle(), conf.
\rightarrow GetIdx()+1))
            conf.GetCoords(vecCoords)
            # Calculate energy
            energy = ff(vecg)oechem. OEThrow. Info ("Initial energy: %0.2f kcal/mol" % energy)
            # Optimize the ligand
            optimizer = oeff.OEBFGSOpt()
            energy = optimizer(ff, vecCoords, vecCoords)
            oechem. OEThrow. Info ("Optimized energy: 80.2f kcal/mol" % energy)
            conf.SetCoords(vecCoords)
        oechem.OEWriteMolecule(ofs, mol)
    return 0
if __name__ == "__main__".sys.exit(main(sys.argv))
```

# **CHAPTER**

# **THREE**

# **OEFF API**

# **3.1 OEOpt Classes**

# 3.1.1 OEAdaptor

Attention: This API is currently available in C++ and Python.

class OEAdaptor

The OEAdaptor class is a pure virtual base class which defines the interface for classes which adapt or transform variables and gradients during an optimization. Adaptors are useful in cases where function evaluations are performed in a different coordinate system than the variables being optimized (for example polar coordinates are optimized but the function is evaluated in Cartesian coordinates).

![](_page_44_Figure_8.jpeg)

### The OEAdaptor class defines the following public methods:

- · AdaptVar
- · GetVar

#### The following classes derive from this class:

- OEInterAdaptor
- OEMolAdaptor
- OEMolAdaptor2
- OEQuatAdaptor
- OESubsetAdaptor
- OETorAdaptor
- OETorQuatAdaptor

## **AdaptVar**

bool AdaptVar (double \*ca, const double \*) const

Takes a set of variables as the second argument and copies a set of transformed variables into the first argument. This method is commonly used to transform optimized variables back into the coordinate system of the original reference variables.

#### **GetVar**

void GetVar (double\* var, const double\* refVar)

Takes reference variables as an argument ( $r \in fVar$ ), and transforms them into the variable type or coordinate system  $(\forall ar)$  that will be used during an optimization. Reference variables normally use the same coordinate system as the function evaluations that will be performed in an optimization. Many adaptors take Cartesian coordinates as the argument to the method, and return an array of variables containing the initial adapted state, such as torsion angles or a quaternion.

## 3.1.2 OEBFGSOpt

**Attention:** This API is currently available in C++ and Python.

class OEBFGSOpt : public OEOptimizer1

The OEBFGSOpt implements the quasi-Newton optimization method with updating Hessian according to the scheme of Broyden, Fletcher, Goldfarb and Shanno. The convergence criteria in based on  $\sum_i g_i g_i$ .

The following methods are publicly inherited from OEOptimizer1:

- operator()
- · GetIterLimit and SetIterLimit
- SetLineMinimize
- · GetTolerance and SetTolerance

## The OEBFGSOpt class defines the following public methods:

· GetHessianDimension

- · GetInverseHessian
- GetKeepHessian
- SetKeepHessian
- · UseSavedHessian

## **Constructors**

```
OEBFGSOpt()
OEBFGSOpt (const OEBFGSOpt &)
```

Default and copy constructors.

#### operator=

```
OEBFGSOpt & operator=(const OEBFGSOpt &)
```

#### GetHessianDimension

unsigned int GetHessianDimension() const

Returns the dimension of the Hessian matrix.

## **GetInverseHessian**

bool GetInverseHessian (double \*h, unsigned int nv) const

Copies the inverted Hessian matrix into the array h in the form of lower triangle of complete Hessian. This function is useful when the Hessian matrix generated during optimization is needed. nv is the number of optimized variables.

### **GetKeepHessian**

bool GetKeepHessian () const

Returns true if the OEBFGSOpt object is set to keep its Hessian

## SetKeepHessian

void SetKeepHessian (bool keep)

If the value of the argument passed is  $true$ , the *OEBFGSOpt* object will keep its Hessian when the optimization is done.

## **UseSavedHessian**

```
void UseSavedHessian (bool ini)
```

By default, at the start of the optimization Hessian is initiated as unit matrix. In the case when optimization has to repeated, for example starting with different values of variables, one can use this method to initiate optimization with the Hessian from the previous run.

## 3.1.3 OECGLineMinimize

Attention: This API is currently available in C++ and Python.

class OECGLineMinimize : public OELineMinimize

The OECGLineMinimize class implements line minimization used by the Conjugate Gradient optimizer OEConj-**GradOpt** 

The following methods are publicly inherited from OELineMinimize:

- operator()
- CreateCopy
- · SetMaxStep

#### **Constructors**

OECGLineMinimize()

Default and copy constructors.

# 3.1.4 OECheckpoint0

Attention: This API is currently available in C++ and Python.

class OECheckpoint0

The OECheckpoint0 class is an abstract class which provides a "callback" facility to monitor the progress of an optimization. In addition, the checkpoint class can also be used to control the termination of an optimization. This class is specifically for use with optimizers which do not use gradients.

## The OECheckpoint0 class defines the following public methods:

• operator()

The following classes derive from this class:

• OECheckpoint1

operator()

```
bool operator () (unsigned int iteration, unsigned int nvar, double fval,
                const double *var=(double *) 0, unsigned int state=0)
```

This operator method is called by an optimizer at least once per iteration during an optimization. The variables passed to the method from the optimizer reflect the current state of an optimization.

*iteration* The iteration number.

*nvar* The number of variables.

*fral* The most recent function evaluation during the current iteration.

var Array containing current set of optimized variables. If available, the array has a length of nvar.

state The current state of optimization.

## 3.1.5 OECheckpoint1

**Attention:** This API is currently available in C++ and Python.

class OECheckpoint1 : public OECheckpoint0

The OECheckpoint1 provides a "callback" facility to monitor the progress of an optimization. In addition, it can also be used to control the termination of an optimization. This class may be used with optimizers that do not use gradients as well as those that use gradients

The following methods are publicly inherited from OECheckpoint0:

```
• operator()
```

The OECheckpoint1 class defines the following public methods:

```
• operator()
```

### operator()

```
bool operator () (unsigned int iteration, unsigned int nvar, double fval,
                double gnorm, const double *var=(double *) 0,
                const double *grad=(double *) 0, unsigned int state=0)=0
```

This operator method is called by an optimizer at least once per iteration during an optimization. The variables passed to the method from the optimizer reflect the current state of an optimization.

*iteration* The iteration number.

*nvar* The number of variables.

*fval* The most recent function evaluation during the current iteration.

gnorm The most recent gradient norm evaluation during the current iteration. The gradient norm is defined as  $\sqrt{\sum_i g_i g_i}$ 

var Array containing current set of optimized variables. If available, the array has a length of  $n \vee a$ r.

grad Array containing current set of optimized variables. If available, the array has a length of nvar.

state The current state of optimization.

# 3.1.6 OEConjGradOpt

Attention: This API is currently available in C++ and Python.

class OEConjGradOpt : public OEOptimizer1

The OEConjGradOpt implements the conjugate gradient optimization method. The convergence criteria in based on  $\sum_i g_i g_i$ .

The following methods are publicly inherited from OEOptimizer1:

- operator ()
- · GetIterLimit and SetIterLimit
- · SetLineMinimize
- · GetTolerance and SetTolerance

## **Constructors**

```
OEConjGradOpt()
OEConjGradOpt (const OEConjGradOpt &)
```

Default and copy constructors.

## operator=

OEConjGradOpt & operator=(const OEConjGradOpt &)

# 3.1.7 OEDFPOpt

Attention: This API is currently available in C++ and Python.

class OEDFPOpt : public OEOptimizer1

The OEDFPOpt implements the quasi-Newton optimization according to the Davidon-Fletcher-Powell method. The convergence criteria in based on  $\sum_i g_i g_i$ .

The following methods are publicly inherited from OEOptimizer1:

- operator ()
- · GetIterLimit and SetIterLimit
- · SetLineMinimize
- · GetTolerance and SetTolerance

## **Constructors**

```
OEDFPOpt()
OEDFPOpt (const OEDFPOpt &)
```

Default and copy constructors.

#### operator=

```
OEDFPOpt & operator=(const OEDFPOpt &)
```

# 3.1.8 OEFComponent

Attention: This API is currently available in C++ and Python.

struct OEFComponent

The OEFComponent class associates interaction-component names with with computed energy values. Methods which override GetFComponents return an iterator over OEFComponent instances.

## **Constructors**

```
OEFComponent ()
OEFComponent (const char *n, double v)
```

Default and copy constructors.

Second constructor makes an instance of *OEF Component* given a name and value for an interaction.

# 3.1.9 OEFletcherReevesOpt

Attention: This API is currently available in C++ and Python.

class OEFletcherReevesOpt : public OEOptimizer1

The OEFletcherReevesOpt class implements the Fletcher-Reeves optimization method belonging to the family of conjugate gradient methods. The convergence criteria in based on  $\sum_i g_i g_i$ .

The following methods are publicly inherited from OEOptimizer1:

- operator()
- · GetIterLimit and SetIterLimit
- · SetLineMinimize
- · GetTolerance and SetTolerance

## **Constructors**

```
OEFletcherReevesOpt()
OEFletcherReevesOpt(const OEFletcherReevesOpt &)
```

Default and copy constructors.

### operator=

OEFletcherReevesOpt & operator=(const OEFletcherReevesOpt &)

# 3.1.10 OEFunc0

Attention: This API is currently available in C++ and Python.

## class OEFunc0

The  $OEFuncO$  is an abstract base class. This class defines the interface for functions which take a set of variables and compute a function value, but have no defined analytical gradients. Classes derived from  $OEFuncO$  are intended for use with optimizers which do not require gradients.

## The OEFunc0 class defines the following public methods:

- operator ()
- · GetFComponents
- NumVar

## The following classes derive from this class:

- $\bullet$  OEFuncl
- $\bullet$  OEFunc2
- OEMolFunc0
- $\bullet$  OEMolFunc1
- $\bullet$  OEMolFunc2
- OEForceField
- OEGenericFF
- OEGenericFF2
- OEInterAdaptor
- OEMolAdaptor
- OEQuatAdaptor
- OESubsetAdaptor
- OETorAdaptor
- OETorQuatAdaptor

![](_page_52_Figure_1.jpeg)

- OENumericMolFunc2
- OEScaledMolFunc
- OEFFPotential
- $\bullet$  OEStretchPotential
- $\bullet$  OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential
- OENonBondPotBase
- OEVdwPotential
- OECoulombPotential
- OEInterMolFunc1
- OEInterMolFunc2

- OEInterNonBondPotBase
- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential
- OEHarmonicPotential
- OEMMFF
- OEMMFFStretchBend
- OEMMFFIEFF
- OESheffield
- OEOverlapFuncBase
- OEOverlapFunc
- OEShapeFunc
- OEExactShapeFunc
- OEAnalyticShapeFunc
- OEHermiteShapeFunc
- OEGridShapeFunc
- OEColorFunc
- OEExactColorFunc
- OEAnalyticColorFunc
- OEGridColorFunc

## operator()

 $double operator() (const double*)$ 

This method defines the interface for function evaluation. An array of variables is passed as an argument, and a function value is returned. All classes derived from  $OEFuncO$  implements this method.

#### **GetFComponents**

OESystem:: OEIterBase<OEFComponent> \*GetFComponents (const double \*)

This method defines the interface for retrieving information about function names and associated function values, given a set of variables. The method takes an array of variables, and returns an iterator over the names and component values (typically energies).

All OE classes derived from OEFuncO, implements this method. However, due to the unique construct of the return value from this method, it is not possible to implement this in a user derived class. It is suggested to return a NULL for user derived classes and handle things accordingly.

## **NumVar**

unsigned int NumVar () const

This method defines the interface for returning the number of function variables. All classes derived from OEFuncO implements this method.

# 3.1.11 OEFunc1

Attention: This API is currently available in C++ and Python.

```
class OEFunc1 : public OEFunc0
```

The OEFunc1 is an abstract base class. This class defines the interface for functions which take a set of variables and compute a function value and gradients. Classes derived from OEFunc1 are intended for use with optimizers which require gradients.

![](_page_54_Figure_8.jpeg)

### The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

#### The OEFunc1 class defines the following additional public methods:

• operator ()

## The following classes derive from this class:

- $\bullet$  OEFunc2
- OEMolFunc1
- OEMolFunc2
- OEForceField
- OEGenericFF
- OEGenericFF2
- OEInterAdaptor
- OEMolAdaptor
- OEQuatAdaptor
- OESubsetAdaptor
- OETorAdaptor
- OETorQuatAdaptor
- OENumericMolFunc2
- OEScaledMolFunc
- OEFFPotential
- $\bullet$  OEStretchPotential
- OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential
- $\bullet$  OENonBondPotBase
- OEVdwPotential
- OECoulombPotential
- $\bullet$  OEInterMolFunc1
- OEInterMolFunc2
- OEInterNonBondPotBase
- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential
- OEHarmonicPotential

- OEMMFF
- OEMMFFStretchBend
- OEMMFFIEFF
- OESheffield
- OEOverlapFuncBase
- OEOverlapFunc
- OEShapeFunc
- OEExactShapeFunc
- OEAnalyticShapeFunc
- OEHermiteShapeFunc
- OEGridShapeFunc
- OEColorFunc
- OEExactColorFunc
- OEAnalyticColorFunc
- OEGridColorFunc

## operator()

double operator () (const double \*x, double \*g)

This method defines the interface for function evaluation along with the gradients. An array of variables is passed as an argument, and a function value is returned. The corresponding gradients for the given set of variable is returned in the second argument. All classes derived from OEFunc1 implements this method.

There should be a one to one correspondence between the elements of the variable and gradient arrays. Methods that override this operator method must not initialize the gradient array, but rather assume the array has already been initialized.

# 3.1.12 OEFunc2

**Attention:** This API is currently available in C++ and Python.

class OEFunc2 : public OEFunc1

The OEFunc2 is an abstract base class. This class defines the interface for functions which take a set of variables and compute a function value, gradients and second derivatives.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

![](_page_57_Figure_1.jpeg)

• operator ()

The OEFunc2 class defines the following additional public methods:

• operator ()

## The following classes derive from this class:

- OEMolFunc2
- OEGenericFF2
- OESubsetAdaptor
- OENumericMolFunc2
- OEScaledMolFunc
- OEFFPotential
- OEStretchPotential
- OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential
- OENonBondPotBase
- OEVdwPotential
- OECoulombPotential

- OEInterMolFunc2
- OEInterNonBondPotBase
- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential
- OEMMFF
- OEMMFFStretchBend
- OESheffield
- OEHermiteShapeFunc

#### operator()

bool operator () (const double \*x, double \*h, double \*g)

This method defines the interface for function evaluation along with gradients and second derivatives. The corresponding second derivatives for the given set of variable is returned in the second argument, and the gradients are returned in the third argument.

There should be a one to one correspondence between the elements of the variable and that second derivatives and gradients arrays. Methods that override this operator method must not initialize the second derivatives and the gradient arrays, but rather assume that the arrays has already been initialized.

## 3.1.13 OEHestenesStiefelOpt

```
Attention: This API is currently available in C++ and Python.
```

class OEHestenesStiefelOpt : public OEOptimizer1

The OEHestenesStiefelOpt class implements the Hestenes-Stiefel optimization method belonging to the family of conjugate gradient methods. The convergence criteria in based on  $\sum_i g_i g_i$ .

The following methods are publicly inherited from OEOptimizer1:

- operator()
- · GetIterLimit and SetIterLimit
- · SetLineMinimize
- · GetTolerance and SetTolerance

## **Constructors**

```
OEHestenesStiefelOpt()
OEHestenesStiefelOpt (const OEHestenesStiefelOpt & rhs)
```

Default and copy constructors.

#### operator=

OEHestenesStiefelOpt & operator=(const OEHestenesStiefelOpt & rhs)

# 3.1.14 OELineMinimize

Attention: This API is currently available in C++ and Python.

#### class OELineMinimize

The OELineMinimize class is a base class which defines the interface for line minimization used in different types of optimization.

#### The OELineMinimize class defines the following public methods:

- · operator()
- CreateCopy
- · SetMaxStep

#### The following classes derive from this class:

- OECGLineMinimize
- OEMaxStepLineMinimize
- OEQNLineMinimize
- $\bullet$  OENRLineSearch

### operator()

```
bool operator() (unsigned int n, double *p, double *d, double *g, double *k,
                double *gmin, double *alpha, OEFunc1 &fun) const
```

Defines the interface for finding the step size alpha for the current optimizer iteration in the search direction determined by the vector d. n is the number of optimized variables, array p and g contain initial coordinates and gradients, while array k returns gradients for the coordinates determined by the returned step size alpha. gmin contains the initial function value and returns its optimized value, and fun is a reference to optimized function object. Operator returns  $t_{\text{rule}}$  when a value lower than the initial function value is found.  $fa \ge 0$  otherwise.

## **SetMaxStep**

bool SetMaxStep (unsigned int, double \*)

Defines the interface for determination of the maximum step size. This method has a trivial implementation in the base class, and provides a way to determine the maximum step if the specific line optimization derived from OELine-Minimize needs it.

## **CreateCopy**

OELineMinimize \*CreateCopy() const

Defines the interface for creating a copy of line minimization object.

# 3.1.15 OEMaxStepLineMinimize

Attention: This API is currently available in C++ and Python.

class OEMaxStepLineMinimize : public OELineMinimize

The following methods are publicly inherited from OELineMinimize:

- operator()
- CreateCopy
- · SetMaxStep

## **Constructors**

```
OEMaxStepLineMinimize()
OEMaxStepLineMinimize(double *maxStep, unsigned len)
OEMaxStepLineMinimize (const OEMaxStepLineMinimize &rhs)
```

Default and copy constructors.

#### operator=

OEMaxStepLineMinimize & operator= (const OEMaxStepLineMinimize & rhs)

# 3.1.16 OENRLineSearch

Attention: This API is currently available in C++ and Python.

class OENRLineSearch : public OELineMinimize

The OENRLineSearch class implements line minimization using backtracking line search method.

The following methods are publicly inherited from OELineMinimize:

- operator ()
- · SetMaxStep
- CreateCopy

### **Constructors**

OENRLineSearch()

Default and copy constructors.

# 3.1.17 OEOptimizer0

Attention: This API is currently available in C++ and Python.

class OEOptimizer0

The OEOptimizer0 abstract class defines the interface for optimizing a set of variables for which a function can be evaluated. Implementations of  $OEOptimizer0$  use only function values during optimization, so it does not calculate gradients.

The OEOptimizer0 class defines the following public methods:

- operator ()
- GetIterLimit and SetIterLimit

operator()

```
double operator () (OEFunc0 &function, const double *var, double *opt_var)
double operator () (OEFunc0 &function, OECheckpoint0 *check, const double *var,
                  double *opt_var)
```

These methods define the interface for optimizing a set of variables with the use of evaluated function values. The reference to the function object is passed as a first argument. Initial values of variables are passed in the array var. The optimized variables are returned in the array opt\_var. Both operators return the value of the corresponding optimized function value. The second operator takes a pointer to the OECheckpoint0 object that can be used to monitor the progress of an optimization.

## **GetIterLimit**

unsigned GetIterLimit() const

See Set IterLimit.

## **SetIterLimit**

void SetIterLimit (unsigned int itmax)

Defines the interface for setting the maximum number of iterations that an optimizer derived from the OEOptimizer0 will attempt while trying to identify a converged minimum function value. Optimization will cease if the iteration limit is reached without finding a converged minimum.

# 3.1.18 OEOptimizer1

Attention: This API is currently available in C++ and Python.

#### class OEOptimizer1

The OEOptimizer1 abstract class defines the interface for optimizing a set of variables for which a function and gradients can be evaluated. Implementations of *OEOptimizer1* use both function values and gradients during optimization.

#### The OEOptimizer1 class defines the following public methods:

- operator()
- · GetIterLimit and SetIterLimit
- · SetLineMinimize
- · GetTolerance and SetTolerance

The following classes derive from this class:

- OEBFGSOpt
- OEConjGradOpt
- OEDFPOpt
- OEFletcherReevesOpt

- OEHestenesStiefelOpt
- OERibierePolakOpt
- OESteepestDescentOpt

#### operator()

```
double operator () (OEFuncl & function, const double *var, double *opt_var)
double operator () (OEFunc1 & function, OECheckpoint1 *check, const double *var,
                  double *opt_var)
```

These virtual methods define the interface for optimizing a set of variables with the use of evaluated function values. The reference to the function object is passed as a first argument. Initial values of variables are passed in the array var. The optimized variables are returned in the array opt\_var. Both operators return the value of the corresponding optimized function value. The second operator takes a pointer to the OECheckpoint1 object that can be used to monitor the progress of an optimization.

## **GetIterLimit**

```
unsigned GetIterLimit() const
```

See SetIterLimit.

#### **GetTolerance**

double GetTolerance() const

See Set Tolerance.

#### **SetIterLimit**

void SetIterLimit (unsigned int itmax)

Defines the interface for setting the maximum number of iterations that an optimizer derived from the OEOptimizer0 will attempt while trying to identify a converged minimum function value. Optimization will cease if the iteration limit is reached without finding a converged minimum.

#### **SetLineMinimize**

```
bool SetLineMinimize (const OELineMinimize &linmin)
```

Allows selection of the line minimization object used by the optimizer.

### **SetTolerance**

void SetTolerance (double t)

Defines the interface for setting the gradient convergence criteria. Depending on the implementation it might be the root mean square gradient, gradient norm or gradient dot product. Optimization will terminate normally if the convergence criteria set by this method is achieved during an optimization.

# 3.1.19 OEOptimizer2

Attention: This API is currently available in C++ and Python.

class OEOptimizer2

The OEOptimizer2 abstract class defines the interface for optimizing a set of variables for which a function, gradients and second derivatives (elements oh Hessian matrix) can be evaluated. Implementations of OEOptimizer2 use function values, gradients and second derivatives of function during optimization.

The *OEOptimizer2* class defines the following public methods:

- · operator ()
- · GetIterLimit and SetIterLimit
- · GetTolerance and SetTolerance

#### The following classes derive from this class:

• OENewtonOpt

#### operator()

```
double operator () (OEFunc2 & function, const double *var, double *opt_var)
double operator () (OEFunc2 & function, OECheckpoint1 *check, const double *var,
                  double *opt_var)
```

These virtual methods define the interface for optimizing a set of variables with the use of evaluated function values. The reference to the function object is passed as a first argument. Initial values of variables are passed in the array var. The optimized variables are returned in the array opt\_var. Both operators return the value of the corresponding optimized function value. The second operator takes a pointer to the OECheckpoint1 object that can be used to monitor the progress of an optimization.

## **GetIterLimit**

unsigned GetIterLimit () const

See Set IterLimit.

## **GetTolerance**

double GetTolerance() const

See Set Tolerance.

### **SetIterLimit**

void SetIterLimit (unsigned int itmax)

Defines the interface for setting the maximum number of iterations that an optimizer derived from the OEOptimizer2 will attempt while trying to identify a converged minimum function value. Optimization will cease if the iteration limit is reached without finding a converged minimum.

## **SetTolerance**

void SetTolerance (double t)

Defines the interface for setting the gradient convergence criteria. Depending on the implementation it might be the root mean square gradient, gradient norm or gradient dot product. Optimization will terminate normally if the convergence criteria set by this method is achieved during an optimization.

# 3.1.20 OEQNLineMinimize

Attention: This API is currently available in C++ and Python.

class OEQNLineMinimize : public OELineMinimize

The OEQNLineMinimize class implements line minimization for the optional use in quasi-Newton optimization.

## The following methods are publicly inherited from OELineMinimize:

- operator ()
- CreateCopy
- SetMaxStep

### **Constructors**

OEONLineMinimize()

Default and copy constructors.

# 3.1.21 OERibierePolakOpt

Attention: This API is currently available in C++ and Python.

class OERibierePolakOpt : public OEOptimizer1

The OERibierePolakOpt class implements the Polak-Ribière optimization method belonging to the family of conjugate gradient methods. The convergence criteria in based on  $\sum_i g_i g_i$ .

The following methods are publicly inherited from OEOptimizer1:

- operator()
- · GetIterLimit and SetIterLimit
- · SetLineMinimize
- Get Tolerance and Set Tolerance

#### **Constructors**

```
OERibierePolakOpt()
OERibierePolakOpt (const OERibierePolakOpt & rhs)
```

Default and copy constructors.

#### operator=

```
OERibierePolakOpt & operator=(const OERibierePolakOpt & rhs)
```

## 3.1.22 OESteepestDescentOpt

Attention: This API is currently available in C++ and Python.

class OESteepestDescentOpt : public OEOptimizer1

The OESteepestDescentOpt class implements the steepest descent optimization method. The convergence criteria in based on  $\sum_i g_i g_i$ .

The following methods are publicly inherited from OEOptimizer1:

- · operator ()
- · GetIterLimit and SetIterLimit
- · GetTolerance and SetTolerance

#### The OESteepestDescentOpt class defines the following public methods:

· SetInitialStep

## **Constructors**

OESteepestDescentOpt()

Default and copy constructors.

## **SetInitialStep**

void SetInitialStep (double step)

Sets the initial step. The default initial step is  $\sqrt{(1.0/\sum_i g_i g_i)}$ 

# 3.1.23 OENewtonOpt

Attention: This API is currently available in C++ and Python.

class OENewtonOpt : public OEOptimizer2

The OENewtonOpt implements the Newton-Raphson optimization method using analytical Hessian and its Cholesky decomposition for determination of current search direction.

## The following methods are publicly inherited from OEOptimizer2:

- · operator()
- · GetIterLimit and SetIterLimit
- · GetTolerance and SetTolerance

## **Constructors**

```
OENewtonOpt()
OENewtonOpt (const OENewtonOpt &)
```

Default and copy constructors.

#### operator=

```
OENewtonOpt & operator= (const OENewtonOpt &)
```

## See also:

• Solving a simple equation example

# **3.2 OEMolPotential Classes**

# 3.2.1 OEBendParams

Attention: This API is currently available in C++ and Python.

OEBendParams : public OEMolPotential:: OEInteractParams class

The OEBendParams class defines generic angle-bend parameters used in any force field which has bond angle term.

The following methods are publicly inherited from OEInteractParams:

- · Clear
- $\bullet$  Get
- $\bullet$  Set

The OEBendParams class defines the following public methods:

- · GetAtomIndex1
- · GetAtomIndex2
- · GetAtomIndex3
- · IsValid
- · IsAngle

#### **Constructors**

```
OEBendParams (const OEChem:: OEBondBase* bond1, const OEChem:: OEBondBase* bond2)
OEBendParams (const OEBendParams&) = default;
```

Constructor and copy constructor. Constructs an OEBendParams object for two bonds which make the bond angle.

### operator=

```
OEBendParams& operator=(const OEBendParams&) = default
```

The assignment operator.

## GetAtomIndex1

```
unsigned GetAtomIndex1() const
```

Returns atom index of the first atom for bond angle for which the instance of OEBendParams was created.

## GetAtomIndex2

```
unsigned GetAtomIndex2() const
```

Returns atom index of the second atom for bond angle for which the instance of OEBendParams was created.

### GetAtomIndex3

unsigned GetAtomIndex3() const

Returns atom index of the third atom for bond angle for which the instance of OEBendParams was created.

## **IsValid**

```
bool IsValid() const
bool IsValid(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>& pred) const
bool IsValid(const OESystem::OEBinaryPredicate<OEChem::OEBondBase, OEChem::OEBondBase>
\leftrightarrow pred) const;
```

Methods which check if an instance of the OEBendParams class was created for the bond angle to be included in force field calculation. First method is checking if the above instance was correctly constructed, while two remaining methods provide predicates to test if atoms (second method) and two bonds which define bond angle belong to that instance.

## **IsAngle**

```
bool IsAngle (const OEChem:: OEAtomBase* atoml, const OEChem:: OEAtomBase* atom2,
             const OEChem:: OEAtomBase* atom3) const
```

Used to check if 3 atom passed as an arguments belong to the current OEBendParams instance.

# 3.2.2 OEBendPotential

Attention: This API is currently available in C++ and Python.

class OEBendPotential : public virtual OEMolPotential:: OEFFPotential

The OEBendPotential defines an interface all angle bending force field interaction potentials.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The OEBendPotential implements the following methods:

 $\bullet$  Set

#### **Constructors**

```
OEBendPotential (const OEFFParams&)
OEBendPotential (const OEBendPotential&)
```

Constructor and copy constructor.

## **Assignment operator**

OEBendPotential& operator=(const OEBendPotential&)

Assignment operator.

#### **Set**

bool Set (const OESystem::OEBinaryPredicate<OEChem::OEBondBase, OEChem::OEBondBase>&)

This method allows interaction-level control of the angle-bend term. The predicate passed is used to test the molecule's bond angles. Only those bond angles which are reported as  $true$  are included in the list of interactions to be calculated. The Set method must be called before the Set up for it to be effective.

## 3.2.3 OECoulombPotential

**Attention:** This API is currently available in C++ and Python.

class OECoulombPotential : public virtual OENonBondPotBase

The OECoulombPotential class defines an interface for calculation of intra-molecular Coulomb force field interaction potentials.

The following methods are publicly inherited from OEFunc0:

• operator ()

- GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The following methods are publicly inherited from OENonBondPotBase:

- · GetNonBondOptions
- $\bullet$  Set

## **Constructors**

```
OECoulombPotential (const OEFFParams&, const double cutoff) = default;
OECoulombPotential (const OECoulombPotential() = default;
```

Constructor and copy constructor.

## **Assignment operator**

```
OECoulombPotential& operator=(const OECoulombPotential&) = default;
```

Assignment operator.

# 3.2.4 OEFFParams

Attention: This API is currently available in C++ and Python.

class OEFFParams

The OEFFParams is an abstract base class. This class defines the interface to retrieve parameters defined by a force field. In addition, simple methods are included for facile extraction of idealized geometric information base on the force field.

The OEFFParams class defines the following public methods:

• CreateCopy

- · GetAtomTypeIndex
- · GetAtomTypeName
- · GetContactDistance
- · GetCoulombParams
- · GetEquilibriumAngle
- · GetEquilibriumBondLength
- · GetStretchBendParams
- GetVdwRadius
- PrepMol
- · GetVdwParams
- · GetStretchParams
- GetBendParams
- GetTorsionParams
- GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- · GetTitle

#### The following classes derive from this class:

- OEMMFF94sParams
- OEMMFFParams
- OESmirnoffParams

## **Constructors**

```
OEFFParams() = default;
OEFFParams (const OEFFParams&) = default;
```

Constructor and copy constructor.

## **Assignment operator**

OEFFParams& operator=(const OEFFParams&) = default;

Assignment operator.

### **CreateCopy**

OEFFParams \*CreateCopy() const

This method returns a deep copy of the OEFFParams derived object. The copy of the object returned is in memory owned by the user making the function call. The delete operator must be called for the returned pointer when the copy is no longer needed in order to avoid memory leaks.

## **GetAtomTypeIndex**

unsigned int GetAtomTypeIndex (unsigned int) const

Provides interface to get an atom type index for the atom identified by the force field type passed as an argument. The point is that a number of chemically different atom types in the force field can belong to a single type for which force field parameters are defined.

## **GetAtomTypeName**

const char \*GetAtomTypeName(unsigned int) const

Provides interface to convert the integer force field atom type into a symbolic type.

### **GetContactDistance**

```
bool GetContactDistance(double &, const OEChem:: OEAtomBase *,
                        const OEChem:: OEAtomBase *) const
```

Provides the interface for retrieving the distance between two atoms corresponding to the minimum on their VdW potential curve. The double precision floating point reference passed as the first argument to the method is assigned to the contact distance for the two atoms if it is defined by the force field. The method returns  $true$  only if a valid force field parameter for the interaction exists. OEFFParams. PrepMol must be called for the molecule prior to using this method.

### **GetCoulombParams**

```
bool GetCoulombParams (OEInteractParams &, const OEChem:: OEAtomBase *,
                      const OEChem:: OEAtomBase *) const
```

Defines the interface for retrieving the parameters used in calculating an electrostatic interaction for two atoms. Overriding methods return true only if valid parameters exist for the atoms passed as the second and third arguments, otherwise they return false. OEFFParams. PrepMol must be called for the molecule prior to using this method.

## **GetEquilibriumAngle**

```
bool GetEquilibriumAngle(double &, const OEChem:: OEAtomBase *,
                          const OEChem:: OEAtomBase *,
                          const OEChem:: OEAtomBase *) const
```

This method is used to retrieve the equilibrium bond angle for the three atoms passed to it. The second atom passed to the method (atom2) must be the central atom of the requested bond angle. The double precision floating point reference passed as the first argument to the method is assigned to the equilibrium bond angle if it is defined by the force field. The method returns true only if a valid force field parameter for the interaction exists. OEFFParams. PrepMol must be called for the molecule prior to using this method.

## GetEquilibriumBondLength

bool GetEquilibriumBondLength (double &, const OEChem:: OEBondBase \*) const

This method is used to retrieve the equilibrium bond length for the bond passed as the second argument. The double precision floating point reference passed as the first argument to the method is assigned to the equilibrium bond length if it is defined by the force field. The method returns  $true$  only if a valid force field parameter for the bond exists. OEFFParams. PrepMol must be called for the molecule prior to using this method.

## **GetStretchBendParams**

```
bool GetStretchBendParams (OEInteractParams &, const OEChem:: OEAtomBase *,
                           const OEChem:: OEAtomBase *,
                           const OEChem:: OEAtomBase *) const
```

Defines the interface for retrieving the parameters used in calculating a stretch-bend interaction. The central atom of the bond-angle must be passed as the third argument to the method. Overriding methods return true only if valid parameters exist for the atoms passed as arguments, otherwise they should return false. OEFFParams. PrepMol must be called for the molecule prior to using this method.

## **GetVdwRadius**

bool GetVdwRadius (double &, const OEChem:: OEAtomBase \*atm) const

Defines the interface for retrieving the VdW radius for an atom. Overriding methods return true only if a VdW radius can be calculated or retrieved for an atom, false otherwise. OEFFParams. PrepMol must be called for the molecule prior to using this method.

## **PrepMol**

bool PrepMol(OEChem::OEMolBase &mol, bool sweep=true, bool closestTypeAllowed=true)  $\rightarrow$ const

Defines the interface for preparing a molecule for force field parameter retrieval. Atom types, names, partial charges, and indices stored within the molecule may be modified by overriding methods. The second argument to the method specifies whether a call to OEMo1Base. Sweep is allowed during the preparation. By default, sweeping a molecule is allowed by the method. A return value of true indicates a successful preparation, however, if the method returns false calculations with the resultant modified molecule should not be attempted. The return value of this method should always be checked before use with its associated force field and components.

**closestTypeAllowed** If true then the MMFF typing method will substitute close atom types if exact atom types do not exist.

#### See also:

OEMMFFAtomType function

### **GetVdwParams**

```
bool GetVdwParams (OEMolPotential:: OEInteractParams&, const OEChem:: OEAtomBase*,
                  const OEChem:: OEAtomBase*) const
```

Fills the first argument, OEInteractParams, with the Vdw parameters for the two non-bonded atoms specified by the second and the third arguments, OEAtomBase. If parameters were not found, it returns false; otherwise, it returns true.

```
OESystem::OEIterBase<OEMolPotential::OEVdwParams>*
GetVdwParams (const OEChem:: OEMolBase& mol,
             const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>* pred=0,
             const double rout=0.0) const
```

Takes a molecule object, mol, and returns an iterator to all *OEVdwParams* objects created for that molecule. If the pointer to atom predicate is passed as the second argument, all atoms engaged in vdw non-bonded interactions will be tested against with that predicate. In this case, the returned iterator will contain parameters for only those pairs of atoms that pass the test. Similarly, all OEVdwParams objects for pairs outside the cutoff radius, reut, will be eliminated. An  $r$  cut value of  $0.0$  or less assumes that all interactions should be included without any cutoff.

```
OESystem:: OEIterBase<OEMolPotential:: OEVdwParams>*
GetVdwParams (const OEChem:: OEMolBase& mol,
             const OEChem:: OEMolBase& host,
             const double rout=0.0) const
```

Returns an iterator to all OEVdwParams objects created for host-ligand interactions specified by the ligand molecule, mol, and the host molecule, host. All OEVdwParams objects for pairs outside the cutoff radius, rout, will be eliminated. An  $r$  cut value of  $0.0$  or less assumes that all interactions should be included without any cutoff.

## **GetStretchParams**

```
bool GetStretchParams (OEMolPotential::OEInteractParams&, const OEChem::OEBondBase*).
\rightarrowconst
```

Fills the first argument, OEInteractParams, with the bond stretch parameters for the bond, OEBondBase. If the parameters were not found, it returns false; otherwise, it returns true.

```
OESystem::OEIterBase<OEMolPotential::OEStretchParams>*
GetStretchParams (const OEChem:: OEMolBase& mol,
                 const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> *pred=0) const
```

Takes a molecule object, mol, and returns an iterator to all OEStretchParams objects created for that molecule. If the pointer to an atom predicate is passed as the second argument, all atoms making bonds will be tested against with that predicate. In this case, the returned iterator will contain parameters for only those bonds made between the atoms that pass the test.

## **GetBendParams**

```
bool GetBendParams (OEMolPotential:: OEInteractParams&, const OEChem:: OEAtomBase*,
                   const OEChem:: OEAtomBase*, const OEChem:: OEAtomBase*) const
```

Fills the first argument, *OEInteractParams*, with the bend parameters for a bond angle made by 3 atoms, OEAtomBase, passed as the second, third and the forth arguments. If the parameters were not found, it returns false; otherwise, it returns true.

```
OESystem:: OEIterBase<OEMolPotential:: OEBendParams>*
GetBendParams (const OEChem:: OEMolBase& mol,
              const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> *pred=0) const
```

Takes a molecule object, mol, and returns an iterator to all *OEBendParams* objects created for that molecule. If the pointer to an atom predicate is passed as the second argument, all atoms making bond angles will be tested against that with predicate and the returned iterator will contain parameters for only those bond angles whose atom members pass the test.

## **GetTorsionParams**

```
bool GetTorsionParams(OEMolPotential:: OEInteractParams&, const OEChem:: OEAtomBase*,
                       const OEChem:: OEAtomBase*, const OEChem:: OEAtomBase*,
                       const OEChem:: OEAtomBase*) const
```

Fills the first argument, *OEInteractParams*, with the torsion parameters for a torsion made by 4 atoms, OEAtomBase, passed as the second, third, forth and the fifth arguments. If the parameters were not found, it returns false; otherwise, it returns true.

```
OESystem:: OEIterBase<OEMolPotential:: OETorsionParams>*
GetTorsionParams(const OEChem:: OEMolBase& mol,
                 const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> *pred=0) const
```

Takes a molecule object, mol, and returns an iterator to all OETorsionParams objects created for that molecule. If the pointer to an atom predicate is passed as the second argument, all atoms making torsions will be tested against with that predicate and the returned iterator will contain parameters for only those torsions whose atom members pass the test.

### **GetOutOfPlaneParams**

```
bool GetOutOfPlaneParams(OEMolPotential::OEInteractParams&, const OEChem::OEAtomBase*,
                         const OEChem:: OEAtomBase*, const OEChem:: OEAtomBase*,
                         const OEChem:: OEAtomBase*) const
```

Fills the first argument, *OEInteractParams*, with the improper torsion parameters for an improper torsion made by 4 atoms, OEAtomBase, passed as the second, third, forth and the fifth arguments. If the parameters were not found, it returns false; otherwise, it returns true.

```
OESvstem::OEIterBase<OEMolPotential::OEOutOfPlaneParams>*
GetOutOfPlaneParams (const OEChem:: OEMolBase& mol,
                     const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> *pred=0),
\rightarrowconst
```

Takes a molecule object, mol, and returns an iterator to all OESmirnoffOutOfPlane objects created for that molecule. If the pointer to an atom predicate is passed as the second argument, all atoms making improper torsions will be tested against with that predicate and the returned iterator will contain parameters for only those improper torsions whose atom members pass the test.

## **HasVdwParams**

```
bool HasVdwParams (const OEChem:: OEMolBase& mol,
             const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>* pred=0,
             const double rout=0.0) const
bool HasVdwParams (const OEChem:: OEMolBase& mol,
                  const OEChem:: OEMolBase& host,
                  const double rout=0.0) const
```

Returns if the desired Vdw parameters exist for the specified molecule, mol. See the GetVdwParams method.

## **HasStretchParams**

```
bool HasStretchParams (const OEChem:: OEMolBase& mol,
                 const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> *pred=0) const
```

Returns if the desired bond stretching parameters exist for the specified molecule, mol. See the GetStretchParams method.

## **HasBendParams**

```
bool HasBendParams (const OEChem:: OEMolBase& mol,
              const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> *pred=0) const
```

Returns if the desired bend parameters exist for the specified molecule, mol. See the GetBendParams method.

## **HasTorsionParams**

```
bool HasTorsionParams (const OEChem:: OEMolBase& mol,
                 const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> *pred=0) const
```

Returns if the desired torison parameters exist for the specified molecule, mol. See the GetTorsionParams method.

### **GetTitle**

std::string GetTitle() const

Returns name of the force field parameter.

# 3.2.5 OEFFPotential

Attention: This API is currently available in C++ and Python.

class OEFFPotential : public virtual OEMolPotential:: OEMolFunc2

The OEFFPotential is an abstract base class. This class defines a common base class for all force field potential function implementations.

### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator()

## The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- $\bullet$  Setup

#### The OEFFPotential implements the following methods:

 $\bullet$  Set

## The following classes derive from this class:

- OENonBondPotBase
- OEInterNonBondPotBase
- OEStretchPotential
- OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential

## **Constructors**

```
OEFFPotential (const OEFFParams&)
OEFFPotential (const OEFFPotential&)
```

Constructor and copy constructor.

## **Assignment operator**

OEFFPotential& operator= (const OEFFPotential&)

Assignment operator.

#### **Set**

**bool** Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&)

This method can be used for interaction-level control of the potential terms. Interactions between two atoms are only included if the OEUnaryPredicate test of all the atoms returns true. The Set methods must be called before the Set up to be effective.

# 3.2.6 OEForceField

**Attention:** This API is currently available in C++ and Python.

```
class OEForceField : public OEMolFunc1
```

The OEForceField is an abstract base class. This class defines an interface for the collection of force field components. The OEForceField extends the OEMolFunc1 class to allow this being a collection of multiple components. The collection of components into a force field needs to be done concomitant with one or more OEFFParams derived classes.

#### The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

#### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

#### The OEForceField class defines the following public methods:

![](_page_80_Figure_1.jpeg)

- GetTitle and SetTitle
- · HasCoulomb
- · HasInternalCharges
- · PrepMol
- $\bullet$  Set
- · SetNonBondCutoff

## The following classes derive from this class:

- OEGenericFF
- $\bullet$  OEGenericFF2
- $\bullet$  OEMMFF
- OEMMFFIEFF

## **GetTitle**

std::string GetTitle() const

See SetTitle.

## **HasCoulomb**

bool HasCoulomb() const

Returns if coulombic interactions are currently turned on.

## **HasInternalCharges**

bool HasInternalCharges () const

Returns True if associated force field parameters has internal charges.

## **PrepMol**

bool PrepMol(OEChem::OEMolBase &mol, bool sweep=true, bool warnOK=true) const

Defines the interface to prepare a molecule to be used for force field setup ( $OEMOIFunc$ .  $Set up$ ). This method internally calls for all contained OEFFParams instances in the OEForceField derived class to perform necessary preparation to enable using those parameters.

The second argument to the method specifies whether a call to OEMolBase. Sweep is allowed during the preparation. By default, sweeping a molecule is allowed by the method. Methods that override OEFFParams. PrepMol may alter the contents of the passed molecule.

Method returns true if preparation is successful, and false otherwise.

#### See also:

• Energy components of a single ligand in vacuum example

#### **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEAtomBase,
         OEChem:: OEAtomBase> &pred, unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEBondBase,
         OEChem:: OEBondBase> &pred, unsigned int functype)
```

These methods assigns interaction-control predicates. The first argument is the predicate type to be passed to the interaction component. The second argument is a value or a set of binary OR'ed values taken from the  $OEFuncType$ namespace which specifies the intended target for the predicate assignment.

The set method passed on the interaction-control predicates to the appropriate force field components contained. Method returns false if predicate was not set to any of the components contained by the force field.

Set must be called before the Setup for it to be effective.

#### **SetNonBondCutoff**

bool SetNonBondCutoff (const double)

Sets the non-bonded interactions cutoff, in angstroms.

## **SetTitle**

void SetTitle (const std:: string&)

Title for the force field.

## 3.2.7 OEGenericFF

**Attention:** This API is currently available in C++ and Python.

class OEGenericFF : public OEMolPotential:: OEForceField

The OEGenericFF class facilitates creation of a user defined force field. The force field instance can be extended by adding internally or externally defined potential functions.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents

![](_page_83_Figure_1.jpeg)

• NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- ClearPredicates
- GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEForceField:

- GetTitle and SetTitle
- · HasCoulomb
- · HasInternalCharges
- · PrepMol
- $\bullet$  Set
- · SetNonBondCutoff

The OEGenericFF class defines the following public methods:

- · AddMolFunc
- · GetComponents
- · RemoveMolFunc

The following classes derive from this class:

• OEMMFFIEFF

#### **Constructors**

OEGenericFF()

Default and copy constructors.

#### **AddMolFunc**

bool AddMolFunc (OEMolPotential:: OEMolFunc1 &f, bool own=false)

This method defines the interface for adding externally declared functions to an OEGenericFF derived instance. The second argument denotes whether the OEGenericFF derived instance is to take ownership of the memory occupied by the external function. If ownership is passed, then it would be deleted during destruction of the OEGenericFF derived class. Any object derived from the OEMolFunc1 may be added using this method. The method returns true if the object of OEMolFunc1 is successfully added. Only one copy of a OEMolFunc1 may be added to an OEGenericFF instance. Subsequent attempts to add the same function object to already contained in a OEGenericFF derived class will fail with a return value of false.

### **GetComponents**

std::vector<OEMolPotential::OEMolFunc1\*> GetComponents() const

Method returns a vector of pointers to the currently contained OEMolFunc1 instances on this OEGenericFF.

## **RemoveMolFunc**

**bool** RemoveMolFunc(OEMolPotential:: OEMolFunc1&)

Defines an interface to remove a function previously added to an OEGenericFF instance. If the function is not contained in the OEGenericFF instance then the method will return false. If the function is found and removed successfully, then the method will return true.

# 3.2.8 OEGenericFF2

**Attention:** This API is currently available in C++ and Python.

```
class OEGenericFF2 : public OEMolPotential:: OEForceField,
                                                           public.
→OEMolPotential::OEMolFunc2
```

The OEGenericFF2 class facilitates creation of a user defined force field of type OEMolFunc2. The force field instance can be extended by adding internally or externally defined potential functions.

The following methods are publicly inherited from OEFunc0:

```
· operator()
```

![](_page_85_Figure_1.jpeg)

- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEForceField:

- GetTitle and SetTitle
- · HasCoulomb
- · HasInternalCharges
- PrepMol

- $\bullet$  Set
- · SetNonBondCutoff

The OEGenericFF2 class defines the following public methods:

- · AddMolFunc
- · GetComponents
- · RemoveMolFunc

The following classes derive from this class:

• OEMMFF

## **Constructors**

OEGenericFF2()

Default and copy constructors.

## **AddMolFunc**

bool AddMolFunc (OEMolPotential:: OEMolFunc2 &f, bool own=false)

This method defines the interface for adding externally declared functions to an OEGenericFF2 derived instance. The second argument denotes whether the OEGenericFF2 derived instance is to take ownership of the memory occupied by the external function. If ownership is passed, then it would be deleted during destruction of the OEGenericFF2 derived class. Any object derived from the OEMolFunc2 may be added using this method. The method returns true if the object of OEMolFunc2 is successfully added. Only one copy of a OEMolFunc2 may be added to an OEGenericFF2 instance. Subsequent attempts to add the same function object to already contained in a OEGenericFF2 derived class will fail with a return value of false.

## **GetComponents**

std::vector<OEMolPotential::OEMolFunc2\*> GetComponents() const

Method returns a vector of pointers to the currently contained OEMolFunc2 instances on this OEGenericFF2.

#### **RemoveMolFunc**

**bool** RemoveMolFunc(OEMolPotential::OEMolFunc2&)

Defines an interface to remove a function previously added to an OEGenericFF2 instance. If the function is not contained in the OEGenericFF2 instance then the method will return false. If the function is found and removed successfully, then the method will return true.

# 3.2.9 OEInteraction

Attention: This API is currently available in C++ and Python.

#### class OEInteraction

The OEInteraction class provides a general mechanism to report individual interactions calculated within a function or force field component. For instance, pairwise atom interactions in an intramolecular VdW component calculation can be obtained by the OEMolFunc. GetInteractions method that returns an iterator over the OEInteraction instances.

The OEInteraction class defines the following public methods:

- · GetAtoms
- GetName
- · GetValues
- · NumAtoms
- · NumValues

## **Constructors**

```
OEInteraction (OEInteractImpl &)
OEInteraction (const OEInteraction &)
```

Default and copy constructors.

#### operator=

```
OEInteraction & operator= (const OEInteraction &)
```

#### **GetAtoms**

OESystem::OEIterBase<OEChem::OEAtomBase> \*GetAtoms() const

Returns an iterator over the atoms involved in the calculated interaction.

#### **GetName**

const char \*GetName() const

Returns a clear text human readable identifier for the type of interaction.

## **GetValues**

double GetValues (double \*grads=0) const

Returns the energy associated with the calculated interaction. The associated gradients may also be obtained by passing in an array of the length returned by the OEInteraction. NumValues method. The derivatives correspond to the atom ordering returned by the OEInteraction. GetAtoms method.

#### **NumAtoms**

unsigned NumAtoms () const

Returns the number of atoms involved in the calculated interactions. One-body interactions, such as an atom in a field, will only have one atom involved in the interaction. VdW interactions will consist of two atoms. Torsions are composed of four interacting atoms.

## **NumValues**

unsigned NumValues () const

Returns the number of gradients associated with the particular interaction. For interactions calculated from Cartesian coordinates of atoms, this method will typically return three times the number of atoms involved in the interaction as x, y, and z gradient values are calculated for each atom.

## 3.2.10 OEInteractParams

Attention: This API is currently available in C++ and Python.

class OEInteractParams

The OEInteractParams class provides a general mechanism for retrieving multiple parameters from methods defined in the OEFFParams class. The number and types of parameters required for calculating molecular interactions varies among force fields. To keep the interface consistent among implementations of OEFFParams for various force fields, parameters are stored in the OEInteractParams class. Once parameters have been assigned in an OEInteractParams instance they may be retrieved using OEInteractParams. Get method.

The OEInteractParams class defines the following public methods:

- $\bullet$  Clear
- $\bullet$  Get
- $\bullet$  GetList
- $\bullet$  Set
- · SetList

## **Constructors**

```
OEInteractParams();
OEInteractParams (const OEInteractParams&) = default;
```

Constructor and copy constructor.

#### **Assignment operator**

OEInteractParams& operator=(const OEInteractParams&) = default;

Thwe assignment operator

#### **Clear**

 $void Clear()$ 

Assigns all parameters to 0.0 in the OEInteractParams instance.

#### Get

double Get (const unsigned int idx) const

Returns the parameter value associated with an integer taken from OEFFParam namespace. The integer argument specifies the type of parameter requested from the OEInteractParams instance. The requested parameter type must match OEFFParams retrieval method to which the OEInteractParams instance was passed.

## **GetList**

std::vector<double> GetList(const unsigned idx) const

Returns a vector of parameters associated with an integer taken from OEFFParam namespace. The integer argument specifies the type of parameter vector requested from the OEInteractParams instance.

#### **Set**

bool Set (const unsigned idx, const double value)

Sets the value of a parameter associated with an integer taken from the OEFFParam namespace (first argument) in the OEFFParam namespace instance.

## **SetList**

bool SetList (const unsigned idx, const std::vector<double>& values)

Sets the values of a parameter vector in the OEFFParam namespace instance. The integer argument specifies the type of parameter vector which will be set.

## 3.2.11 OEInterAdaptor

Attention: This API is currently available in C++ and Python.

```
class OEInterAdaptor : public OEMolAdaptor
```

The OEInterAdaptor class provides the ability to optimize a molecule or conformation with the use of internal coordinates (bond lengths, bond angle bonds and dihedral angles) defined by the internal Z-matrix.

![](_page_90_Figure_8.jpeg)

The following methods are publicly inherited from OEAdaptor:

- · AdaptVar
- · GetVar

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

#### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEMolAdaptor:

· SetMolFunc

The OEInterAdaptor class defines the following public methods:

- · AdaptGrad
- $\bullet$  Set

#### **Constructors**

OEInterAdaptor(OEMolFunc1 &, bool dihedrals=true, bool own=false)

The molecule function used for function evaluation must be provided as the first argument to the constructor. The second argument allows to fix all dihedral angles. By default all dihedral angles are optimized. The third argument specifies whether the OEInterAdaptor object takes ownership of the memory of the molecule function instance. By default the OEInterAdaptor instance does not take ownership of the molecule function, so the OEInterAdaptor destructor does not delete the molecule function instance. If ownership of the molecule function is transferred to the OEInterAdaptor instance, the molecule function's delete operator will be called in the OEInterAdaptor destructor.

Default and copy constructors.

## **AdaptGrad**

bool AdaptGrad(double \*qa, const double \*q) const

Transforms the set of Cartesian gradients passed as a second argument to the method, into a set of internal coordinates gradients and copies them into the array passed as a first argument.

## **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&,
         unsigned int functype = OEFuncType::InterAdapter)bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase>&,
         unsigned int functype = OEFuncType:: InterAdapt)
```

Those two methods assign atom and bond predicates which are used to partially restrict molecules during optimization. First method specifies atoms which are to be held fixed in their starting positions. Second method is used to fix dihedral angles a1-a2-a3-a4 defined by a middle bond a2-a3. Both methods  $Set$  must be called before the method derived from Setup.

# 3.2.12 OEInterCoulombPotential

Attention: This API is currently available in C++ and Python.

class OEInterCoulombPotential : public OEInterNonBondBase

The OEInterCoulombPotential class defines an interface for calculation of inter-molecular Coulomb interaction potentials.

## The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The following methods are publicly inherited from OEInterMolFunc1:

- · AdaptHostCoords
- $\bullet$  GetVar
- · SetHostFlex
- SetupHost

The following methods are publicly inherited from OEInterNonBondPotBase:

- $\bullet$  Set
- · SetNonBondCutoff

## **Constructors**

```
OEInterCoulombPotential (const OEFFParams&, const double cutoff)
OEInterCoulombPotential(const OEInterCoulombPotential&)
```

Constructor and copy constructor.

## **Assignment operator**

OEInterCoulombPotential& operator=(const OEInterCoulombPotential&)

Assignment operator.

# 3.2.13 OEInterMolFunc1

Attention: This API is currently available in C++ and Python.

class OEInterMolFunc1 : public OEMolFunc1

The OEInterMolFunc1 is an abstract base class. It extends OEMolFunc1 to the cases where a small molecule interacts with a macromolecule that is rigid or partially flexible.

#### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

### The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Set
- · Setup

## The OEInterMolFunc1 class defines the following public methods:

- · AdaptHostCoords
- · GetVar
- SetHostFlex
- SetupHost

#### The following classes derive from this class:

• OEInterMolFunc2

## **AdaptHostCoords**

bool AdaptHostCoords (double \*coords, const double \*var) const;

Produces the complete host coordinates (coords) from a set of host coordinates representing the flexible part of the host  $(\forall ar)$ .

#### **GetVar**

void GetVar (double\* var, const double\* x) ;

Takes the complete set coordinates of the host-ligand system  $(x)$  and transforms them to a subset of coordinates to be optimized (var).

### **SetHostFlex**

**bool** SetHostFlex (const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>& pred)

Sets predicate (OEUnaryPredicate) that defines the flexible atoms of the host molecule (usually a macromolecule). Host atoms that pass the predicate (OEUnaryPredicate) will be subject to optimization along with the ligand atoms for which a Set up method is called.

## **SetupHost**

bool SetupHost (const OEChem:: OEMolBase& host)

Sets a macromolecule as host.

## 3.2.14 OEInterMolFunc2

Attention: This API is currently available in C++ and Python.

class OEInterMolFunc2 : public InterMolFunc1, public OEMolFunc2

The OEInterMolFunc2 is an abstract base class. This class defines the interface for stateful functions which operate on molecules and conformers, compute a function value, gradients, and second derivatives. OEInterMolFunc2 combines OEInterMolFunc1 with OEMolFunc2 interface. Classes derived from OEInterMolFunc2 can be used with any optimizers.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Set
- $\bullet$  Setup

## The following methods are publicly inherited from OEInterMolFunc1:

- · AdaptHostCoords
- $\bullet$  GetVar
- SetHostFlex
- SetupHost

#### The following classes derive from this class:

• OEInterNonBondPotBase

# 3.2.15 OEInterNonBondPotBase

Attention: This API is currently available in C++ and Python.

```
class OEInterNonBondPotBase : public OEFFPotential, public
→OEMolPotential::OEInterMolFunc2
```

The OEInterNonBondPotBase is an abstract base class. This class defines a common base class for all inter-molecular non-bonded force field interaction potentials.

### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The following methods are publicly inherited from OEInterMolFunc1:

- · AdaptHostCoords
- GetVar
- SetHostFlex
- SetupHost

### The OEInterNonBondPotBase implements the following methods:

- $\bullet$  Set
- · SetNonBondCutoff

## The following classes derive from this class:

- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential

#### **Constructors**

```
OEInterNonBondPotBase(const OEFFParams&, const OENonBondIntcsOption&)
OEInterNonBondPotBase(const OEInterNonBondPotBase&)
```

Constructor and copy constructor.

#### **Assignment operator**

OEInterNonBondPotBase& operator=(const OEInterNonBondPotBase&)

Assignment operator.

#### **Set**

bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEAtomBase, OEChem:: OEAtomBase>&)

This method can be used for interaction-level control of the non-bonded terms. Interactions between two atoms are only included if the test of the binary predicate with both atoms returns t rue. The Set method must be called before the Setup for it to be effective.

## **SetNonBondCutoff**

```
bool SetNonBondCutoff (const double)
```

Sets non-bonded interactions cutoff. Setting a value of 0,00 or less assumes that all interactions should be included without any cutoff.

# 3.2.16 OEInterNonBondPotential

Attention: This API is currently available in C++ and Python.

```
class OEInterNonBondPotential : public OEInterNonBondBase
```

The OEInterNonBondPotential class defines an interface for calculation of inter-molecular non-bonded (both VdW and Coulomb) force field interaction potentials...

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $• Set$ 

The following methods are publicly inherited from OEInterMolFunc1:

- · AdaptHostCoords
- $\bullet$  GetVar
- SetHostFlex
- · SetupHost

The following methods are publicly inherited from OEInterNonBondPotBase:

- $\bullet$  Set
- · SetNonBondCutoff

## **Constructors**

```
OEInterNonBondPotential(const OEFFParams&, const OENonBondIntcsOption&)
OEInterNonBondPotential(const OEInterNonBondPotential&)
```

Constructor and copy constructor.

## **Assignment operator**

OEInterNonBondPotential& operator=(const OEInterNonBondPotential&)

Assignment operator.

# 3.2.17 OEInterVdwPotential

Attention: This API is currently available in C++ and Python.

class OEInterVdwPotential : public OEInterNonBondBase

The OEInterVdwPotential class defines an interface for calculation of inter-molecular Vdw force field interaction potentials.

### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The following methods are publicly inherited from OEInterMolFunc1:

- · AdaptHostCoords
- · GetVar
- · SetHostFlex

· SetupHost

#### The following methods are publicly inherited from OEInterNonBondPotBase:

- $\bullet$  Set
- · SetNonBondCutoff

## **Constructors**

```
OEInterVdwPotential(const OEFFParams&, const double cutoff)
OEInterVdwPotential(const OEInterVdwPotential&)
```

#### Constructor and copy constructor.

## **Assignment operator**

OEInterVdwPotential& operator=(const OEInterVdwPotential&)

Assignment operator.

# 3.2.18 OEMolAdaptor

**Attention:** This API is currently available in C++ and Python.

class OEMolAdaptor : public OEOpt:: OEAdaptor, public OEMolPotential:: OEMolFuncl

The OEMolAdaptor class is a pure virtual base class which defines the interface for classes which adapt or transform molecular coordinates and gradients during an optimization. Adaptors are useful in cases where energy and gradients evaluation for a molecule or conformation are performed in Cartesian coordinates, but the optimization is done in different coordinate system, for example in torsion space.

## The following methods are publicly inherited from OEAdaptor:

- · AdaptVar
- GetVar

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

•  $operator()$ 

The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions

![](_page_100_Figure_1.jpeg)

- $\bullet$  Set
- $\bullet$  Setup

The OEMolAdaptor class defines the following public methods:

· SetMolFunc

The following classes derive from this class:

- OEInterAdaptor
- OEMolAdaptor2
- OEQuatAdaptor
- OESubsetAdaptor
- OETorAdaptor
- OETorQuatAdaptor

## **SetMolFunc**

**bool** SetMolFunc (OEMolFunc1 &molfunc, **bool** own) =0

Defines the interface for resetting the molecule function within a OEMolAdaptor derived instance. Any molecule functions which are "owned" at the time of calling this method will be deleted. If the value of a second argument passed to the method is true, the adaptor derived from *OEMolAdaptor* will take ownership of the memory of the molecule function, and will call the molecule function's delete operator when either the destructor or the current method is called.

# 3.2.19 OEMolAdaptor2

Attention: This API is currently available in C++ and Python.

```
class OEMolAdaptor2 : public OEMolPotential:: OEMolAdaptor, public OEMolPotential::
→OEMolFunc2
```

The OEMolAdaptor2 class is a pure virtual base class which defines the interface for classes which adapt or transform molecular coordinates, gradients, and hessians of a given OEMolFunc2 during an optimization. Adaptors are useful in cases where energy, gradients and hessians evaluation for a molecule or conformation are performed in Cartesian coordinates, but the optimization is done in different coordinate system.

![](_page_101_Figure_5.jpeg)

The following methods are publicly inherited from OEAdaptor:

- · AdaptVar
- $\bullet$  GetVar

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- $\bullet$  Set
- $\bullet$  Setup

The following methods are publicly inherited from OEMolAdaptor:

· SetMolFunc

The OEMolAdaptor2 class defines the following public methods:

· SetMolFunc2

The following classes derive from this class:

• OESubsetAdaptor

## **SetMolFunc2**

**bool** SetMolFunc2 (OEMolFunc2 &molfunc, **bool** own)=0

Defines the interface for resetting the molecule function, OEMolFunc2, within a OEMolAdaptor2 derived instance. Any molecule functions which are "owned" at the time of calling this method will be deleted. If the value of a second argument passed to the method is true, the adaptor derived from OEMolAdaptor2 will take ownership of the memory of the molecule function, and will call the molecule function's delete operator when either the destructor or the current method is called

## 3.2.20 OEMolFunc

Attention: This API is currently available in C++ and Python.

class OEMolFunc

The OEMolFunc is an abstract base class. This class defines the interface for functions that require a molecule to compute the function value, and is often associated with a force field. When associated with a force field, this represents a forcefield component or a collection of components with each component being a collection of interactions (OEInteraction). Thus, classes derived from OEMolFunc can represent a part of or a complete force field. The force field components need to be done concomitant with one or more OEFFParams derived classes.

The OEMolFunc class defines the following public methods:

- · Clear
- · ClearPredicates
- GetInteractions

![](_page_103_Figure_1.jpeg)

- $Set$
- · Setup

### The following classes derive from this class:

- $\bullet$  OEMolFunc0
- $\bullet$  OEMolFunc1
- OEMolFunc2
- OEForceField
- OEGenericFF
- $\bullet$  OEGenericFF2
- OEInterAdaptor
- OEMolAdaptor
- OEQuatAdaptor

- OESubsetAdaptor
- OETorAdaptor
- OETorQuatAdaptor
- OENumericMolFunc2
- OEScaledMolFunc
- OEFFPotential
- OEStretchPotential
- OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential
- OENonBondPotBase
- OEVdwPotential
- OECoulombPotential
- OEInterMolFunc1
- OEInterMolFunc2
- OEInterNonBondPotBase
- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential
- OEHarmonicPotential
- $\bullet$  OEMMFF
- OEMMFFStretchBend
- OEMMFFIEFF
- OESheffield
- OEOverlapFuncBase
- OEOverlapFunc
- OEShapeFunc
- OEExactShapeFunc
- OEAnalyticShapeFunc
- OEHermiteShapeFunc
- OEGridShapeFunc
- OEColorFunc
- OEExactColorFunc
- OEAnalyticColorFunc
- OEGridColorFunc

## **Clear**

| void Clear() |
|--------------|
|--------------|

Deletes all interactions contained in the OEMolFunc derived instance. The interactions are created during setup (OEMolFunc. Setup).

## **ClearPredicates**

```
void ClearPredicates ()
```

Deletes all stored predicates set, previously created by using one of the overloaded OEMO1Func. Set methods. Predicates control function behavior during setup (OEMolFunc. Setup).

## **GetInteractions**

```
OESystem:: OEIterBase<OEInteraction> *GetInteractions (const OEChem:: OEMolBase &,
                                                       const double *,
                                                       unsigned functype=0) const
```

This method defines the interface for retrieving interaction level information computed by the OEMolFunc instance, given a molecule (first argument) and a set of coordinates (second argument). The method returns an iterator over the OEInteraction objects. See the section on OEInteraction for the details regarding interaction interrogation and reporting.

If OEMolFunc is a composition of multiple components, the last argument may be used to request the interactions of only a single component by passing a value from the  $OEFuncType$  namespace.

Due to the unique construct of the return value from this method, it is not possible to implement this in a user derived class. Default implementation of this method return an iterator over an empty vector.

## **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEAtomBase,
         OEChem:: OEAtomBase> &pred, unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEBondBase,
         OEChem:: OEBondBase> &pred, unsigned int functype)
```

These methods assigns interaction-control predicates to the OEMolFunc derived instance. The first argument is the predicate type to be passed to the interaction component. The second argument is a value or a set of binary OR'ed values taken from the  $OEFuncType$  namespace which specifies the intended target for the predicate assignment.

Most derived classes can only use a handful of the four different kinds of predicates allowed in these overloads, thus only the specific overloads are overwritten by various derived class. The default implementation for all the overloads has trivial implementation and returns a false.

#### **Setup**

```
bool Setup (const OEChem:: OEMolBase&)
```

This method defines the interface for initializing a OEMolFunc derived instance with a molecule. All classes derived from OEMolFunc implements this method. Typically the implementation of this method requires perception of the passed molecule for efficient energy evaluation.

### See also:

• Energy components of a single ligand in vacuum example

# 3.2.21 OEMolFunc0

Attention: This API is currently available in C++ and Python.

class OEMolFunc0 : public OEOpt:: OEFunc0, public OEMolFunc

The OEMolFunc0 is an abstract base class. This class defines the interface for stateful functions which operate on molecules and conformers, compute a function value, but have no defined analytical gradients. OEMolFunc0 combines OEFunc0 with OEMolFunc interface. Classes derived from OEMolFunc0 are intended for use with optimizers which do not require gradients.

## The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Set
- $Set up$

### The following classes derive from this class:

- $\bullet$  OEMolFunc1
- $\bullet$  OEMolFunc2
- $\bullet$  OEForceField
- OEGenericFF
- OEGenericFF2
- OEInterAdaptor
- OEMolAdaptor
- OEQuatAdaptor
- OESubsetAdaptor

![](_page_107_Figure_1.jpeg)

- OETorAdaptor
- OETorQuatAdaptor
- OENumericMolFunc2
- OEScaledMolFunc
- OEFFPotential
- OEStretchPotential
- $\bullet$  OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential
- OENonBondPotBase
- OEVdwPotential
- OECoulombPotential

- OEInterMolFunc1
- OEInterMolFunc2
- OEInterNonBondPotBase
- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential
- OEHarmonicPotential
- OEMMFF
- OEMMFFStretchBend
- OEMMFFIEFF
- OESheffield
- OEOverlapFuncBase
- OEOverlapFunc
- OEShapeFunc
- OEExactShapeFunc
- OEAnalyticShapeFunc
- OEHermiteShapeFunc
- OEGridShapeFunc
- OEColorFunc
- OEExactColorFunc
- OEAnalyticColorFunc
- OEGridColorFunc

## 3.2.22 OEMolFunc1

Attention: This API is currently available in C++ and Python.

class OEMolFunc1 : public OEOpt:: OEFunc1, public OEMolFunc0

The OEMolFunc1 is an abstract base class. This class defines the interface for stateful functions which operate on molecules and conformers, compute a function value, and has defined analytical gradients. OEMolFunc1 combines OEFunc1 with OEMolFunc0 interface. Classes derived from OEMolFunc1 are intended for use with optimizers which require gradients but do not require second derivatives.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

![](_page_109_Figure_1.jpeg)

### • operator ()

### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- $\bullet$  Set
- $\bullet$  Setup

## The following classes derive from this class:

- OEMolFunc2
- OEForceField
- OEGenericFF
- OEGenericFF2

- OEInterAdaptor
- OEMolAdaptor
- OEQuatAdaptor
- OESubsetAdaptor
- OETorAdaptor
- OETorQuatAdaptor
- OENumericMolFunc2
- OEScaledMolFunc
- OEFFPotential
- OEStretchPotential
- OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential
- OENonBondPotBase
- OEVdwPotential
- $\bullet$  OECoulombPotential
- OEInterMolFunc1
- OEInterMolFunc2
- OEInterNonBondPotBase
- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential
- OEHarmonicPotential
- OEMMFF
- OEMMFFStretchBend
- OEMMFFIEFF
- OESheffield
- OEOverlapFuncBase
- OEOverlapFunc
- OEShapeFunc
- OEExactShapeFunc
- OEAnalyticShapeFunc
- OEHermiteShapeFunc
- OEGridShapeFunc
- OEColorFunc
- OEExactColorFunc

- OEAnalyticColorFunc
- OEGridColorFunc

## 3.2.23 OEMolFunc2

Attention: This API is currently available in C++ and Python.

class OEMolFunc2 : public OEOpt:: OEFunc2, public OEMolFunc1

The OEMolFunc2 is an abstract base class. This class defines the interface for stateful functions which operate on molecules and conformers, compute a function value, gradients, and second derivatives. *OEMolFunc2* combines OEFunc2 with OEMolFunc interface. Classes derived from OEMolFunc2 can be used with any optimizers.

![](_page_111_Figure_7.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

· operator()

### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Set
- · Setup

## The following classes derive from this class:

- OEGenericFF2
- OESubsetAdaptor
- OENumericMolFunc2
- OEScaledMolFunc
- $\bullet$  OEFFPotential
- OEStretchPotential
- OEBendPotential
- OETorsionPotential
- OEOutOfPlanePotential
- OENonBondPotBase
- OEVdwPotential
- OECoulombPotential
- OEInterMolFunc2
- $\bullet$  OEInterNonBondPotBase
- OEInterNonBondPotential
- OEInterVdwPotential
- OEInterCoulombPotential
- OEMMFF
- OEMMFFStretchBend
- OESheffield
- OEHermiteShapeFunc

# 3.2.24 OENonBondPotBase

Attention: This API is currently available in C++ and Python.

class OENonBondPotBase : public virtual OEMolPotential:: OEFFPotential

The OENonBondPotBase is an abstract base class. This class defines a common base class for all intra-molecular non-bonded force field interaction potentials.

#### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

#### The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator()

### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

## The OENonBondPotBase implements the following methods:

- · GetNonBondOptions
- $\bullet$  Set

The following classes derive from this class:

- OENonBondPotential
- OEVdwPotential
- OECoulombPotential

## **Constructors**

```
OENonBondPotBase(const OEFFParams&, const OENonBondIntcsOption&)
OENonBondPotBase(const OENonBondPotBase&)
```

Constructor and copy constructor.

## **Assignment operator**

```
OENonBondPotBase& operator=(const OENonBondPotBase&)
```

Assignment operator.

## **GetNonBondOptions**

```
OENonBondIntcsOptions& GetNonBondOptions()
const OENonBondIntcsOptions& GetNonBondOptions() const
```

Returns *options* related to non-bonded interactions.

### **Set**

bool Set (const OESystem::OEBinaryPredicate<OEChem::OEAtomBase, OEChem::OEAtomBase>&)

This method can be used for interaction-level control of the non-bonded terms. Interactions between two atoms are only included if the test of the binary predicate with both atoms returns true. The Set method must be called before the *Setup* for it to be effective.

# 3.2.25 OENonBondPotential

**Attention:** This API is currently available in C++ and Python.

class OENonBondPotential : public virtual OENonBondPotBase

The OENonBondPotential class defines an interface for calculation of intra-molecular non-bonded (both VdW and Coulomb) force field interaction potentials.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

•  $operator()$ 

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $• Set$ 

The following methods are publicly inherited from OENonBondPotBase:

- · GetNonBondOptions
- $\bullet$  Set

## **Constructors**

```
OENonBondPotential(const OEFFParams&, const OENonBondIntcsOption&)
OENonBondPotential(const OENonBondPotential&)
```

Constructor and copy constructor.

## **Assignment operator**

OENonBondPotential& operator=(const OENonBondPotential&)

Assignment operator.

# 3.2.26 OENonBondIntcsOptions

Attention: This API is currently available in C++ and Python.

class OENonBondIntcsOptions : public OESystem:: OEOptions

The OENonBondIntcsOptions is a class that defines common options for OENonBondPotBase.

#### The OENonBondIntcsOptions class defines the following public methods:

- CreateCopy
- · GetCoulombCutoff
- · GetUseCoulomb
- · GetUseVdW
- · GetVdWCutoff
- · SetUseCoulomb
- SetUseVdW

### **Constructors**

```
OENonBondIntcsOptions() = default;
OENonBondIntcsOptions (const OENonBondIntcsOptions() = default;
```

#### Constructor and copy constructor.

## **Assignment operator**

OENonBondIntcsOptions& operator=(const OENonBondIntcsOptions&) = default;

Assignment operator.

## **CreateCopy**

OEMolPotential:: OENonBondIntcsOptions\* CreateCopy()

This method returns a pointer to a deep copy of the instance of OENonBondIntcsOptions.

## **GetCutoff**

double GetCutoff()

See SetCutoff method.

## **GetUseCoulomb**

bool GetUseCoulomb()

See SetUseCoulomb method.

### **GetUseVdW**

bool GetUseVdW()

See SetUseVdW method.

### **SetCutoff**

bool SetCutoff (const double)

Sets the cutoff to be used for non-bonded interactions (van der Waals and coulombic potentials). A cutoff value of 0.0 implies that a cutoff value should not be used at all. Default: 0.0

## **SetUseCoulomb**

bool SetUseCoulomb (const double)

Sets flag specifying if coulombic interactions should be included in calculation. Default: True

## **SetUseVdW**

```
bool SetUseVdW (const bool)
```

Sets flag specifying if van der Waals interactions should be included in calculation. Default: True

# 3.2.27 OENumericMolFunc2

Attention: This API is currently available in C++ and Python.

```
class OENumericMolFunc2 : public OEMolFunc2
```

The OENumericMolFunc2 class converts a OEMolFunc1 into a OEMolFunc2 by providing numeric hessians.

![](_page_117_Figure_8.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

· Clear

- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The OENumericMolFunc2 class defines the following public methods:

 $\bullet$  Set

## **Constructors**

OENumericMolFunc2 (OEMolFunc1 &, bool own=false)

Default and copy constructors.

The molecule function used for function evaluation and to be converted must be provided as the first argument to the constructor. The second argument specifies the scaling factor. The third argument specifies whether the OENumeric-MolFunc2 object takes ownership of the memory of the molecule function instance. By default that does not happen, so the OENumericMolFunc2 destructor does not delete the molecule function instance. If ownership of the molecule function is transferred to the OENumericMolFunc2 instance, the molecule function's delete operator will be called in the OENumericMolFunc2 destructor.

#### **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEAtomBase,
         OEChem:: OEAtomBase> &pred, unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEBondBase,
         OEChem:: OEBondBase> &pred, unsigned int functype)
```

Predicates are passed directly to the molecule function that is to be scaled.

# 3.2.28 OEOutOfPlaneParams

Attention: This API is currently available in C++ and Python.

class OEOutOfPlaneParams : public OEMolPotential:: OEInteractParams

The OEOutOfPlaneParams class defines generic parameters for out-of-plane term which might be used in any force field.

The following methods are publicly inherited from OEInteractParams:

- · Clear
- $\bullet$  Get
- $Set$

The OETorsionParams class defines the following public methods:

- · GetAtomIndex1
- · GetAtomIndex2
- · GetAtomIndex3
- · GetAtomIndex4
- · IsValid

### **Constructors**

```
{\tt OEOutOfPlaneParameters}\ (\textbf{const}\ \texttt{OEChem::OEAtomBase} \ast\ \texttt{atom1,}\ \texttt{const}\ \texttt{OEChem::OEAtomBase} \ast\ \texttt{atom2,}const OEChem:: OEAtomBase* atom3, const OEChem:: OEAtomBase* atom4)
OEOutOfPlaneParams (const OEOutOfPlaneParams&) = default;
```

Constructor and copy constructor. Constructs an OEOutOfPlaneParams object for for atoms defining improper torsion passed as arguments. Second atom (second argument) is an atom which might occure above or beyond the plane make by 3 remaining atoms.

#### operator=

 $OEOutOfPlaneParams & operator = (const OEOutOfPlaneParams & ) = default$ 

The assignment operator.

### GetAtomIndex1

unsigned GetAtomIndex1() const

Returns atom index of the first atom for an improper torsion for which the instance of OEOutOfPlaneParams was created.

### **GetAtomIndex2**

```
unsigned GetAtomIndex2() const
```

Returns atom index of the second atom for an improper torsion for which the instance of OEOutOfPlaneParams was created.

#### GetAtomIndex3

unsigned GetAtomIndex3() const

Returns atom index of the third atom for an improper torsion for which the instance of OEOutOfPlaneParams was created.

## GetAtomIndex4

unsigned GetAtomIndex4() const

Returns atom index of the forth atom for an improper torsion for which the instance of OEOutOfPlaneParams was created.

### **IsValid**

bool IsValid(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>& pred) const

Method which checks if an instance of the OEOutOfPlaneParams class was created for the improper torsion to be included in force field calculation. Method provides a predicate which should be used to test all 4 atoms used to make this instance.

# 3.2.29 OEOutOfPlanePotential

**Attention:** This API is currently available in C++ and Python.

class OEOutOfPlanePotential : public virtual OEMolPotential:: OEFFPotential

The OEOutOfPlanePotential defines an interface for all out-of-plane force field interaction potentials.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

## **Constructors**

```
OEOutOfPlanePotential(const OEFFParams&)
OEOutOfPlanePotential(const OEOutOfPlanePotential&)
```

Constructor and copy constructor.

## **Assignment operator**

OEOutOfPlanePotential& operator=(const OEOutOfPlanePotential&)

Assignment operator.

# 3.2.30 OEQuatAdaptor

Attention: This API is currently available in C++ and Python.

class OEQuatAdaptor : public OEMolAdaptor

The OEQuatAdaptor class provides the ability to rotate and translate a molecule as single rigid unit or solid body in the presence of an external field. Rotations are represented with quaternion variables.

![](_page_121_Figure_11.jpeg)

The following methods are publicly inherited from OEA daptor:

- · AdaptVar
- · GetVar

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEMolAdaptor:

· SetMolFunc

The OEQuatAdaptor class defines the following public methods:

- · AdaptGrad
- · IsRedundant

## **Constructors**

OEQuatAdaptor(OEMolFunc1 &, bool own=false, bool excludeInteract=true)

Default and copy constructors.

Constructs an OEQuatAdaptor instance. The molecule function used for function evaluation must be provided as the first argument to the constructor. The second argument specifies whether the OEQuatAdaptor object takes ownership of the memory of the molecule function instance. By default that does not happen, so the OEQuatAdaptor destructor does not delete the molecule function instance. If ownership of the molecule function is transferred to the OEQuatAdaptor instance, the molecule function's delete operator will be called in the OEQuatAdaptor destructor. The third argument controls the inclusion of invariant molecule function interactions. By default, interactions which remain constant during the solid-body optimization (all intramolecular interactions) are excluded from calculation. If the third calling argument is false then all interactions will be computed during every function evaluation.

#### **AdaptGrad**

```
bool AdaptGrad(double *qg, const double *q, const double *quat,
               const double *coords) const
```

Transforms a set of the input Cartesian gradients (second argument) into rotation and translation gradients which are copied to the first argument array. Third and fourth arguments are the arrays of quaternion plus translation vector and Cartesian coordinates respectively, used for the transformation.

## **IsRedundant**

bool IsRedundant (const double\* x, const double\* y, const double tolerance=0.1) const

Compares two sets of quaternions-translational vectors coordinates. If points  $x$  and  $y$  represent the same point in Cartesian space within given tolerance, method returns true.

# 3.2.31 OEScaledMolFunc

Attention: This API is currently available in C++ and Python.

```
class OEScaledMolFunc : public OEMolFunc2
```

The OEScaledMolFunc class allows scaling energies, gradients and hessians of a molecule function, with a specified constant.

![](_page_123_Figure_8.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator ()

#### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

#### The *OEScaledMolFunc* class defines the following public methods:

 $\bullet$  Set

## **Constructors**

```
OEScaledMolFunc(OEMolFunc1 &, const double factor, bool own=false)
OEScaledMolFunc (OEMolFunc2 &, const double factor, bool own=false)
```

Default and copy constructors.

The molecule function used for function evaluation and to be scaled must be provided as the first argument to the constructor. The second argument specifies the scaling factor. The third argument specifies whether the OEScaled-MolFunc object takes ownership of the memory of the molecule function instance. By default that does not happen, so the OEScaledMolFunc destructor does not delete the molecule function instance. If ownership of the molecule function is transferred to the OEScaledMolFunc instance, the molecule function's delete operator will be called in the OEScaledMolFunc destructor.

## **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEAtomBase,
         OEChem:: OEAtomBase> &pred, unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEBondBase,
         OEChem:: OEBondBase> &pred, unsigned int functype)
```

Predicates are passed directly to the molecule function that is to be scaled.

# 3.2.32 OEStretchParams

**Attention:** This API is currently available in C++ and Python.

class OEStretchParams : public OEMolPotential:: OEInteractParams

The OEStretchParams class defines generic bond stretch parameters used in any force field which has bond stretch term.

The following methods are publicly inherited from OEInteractParams:

- · Clear
- $-$  Get

 $\bullet$  Set

#### The OEStretchParams class defines the following public methods:

- · GetAtomIndex1
- · GetAtomIndex2
- · IsValid
- · IsBond

## **Constructors**

```
OEStretchParams (const OEChem:: OEBondBase* bond)
OESTretchParams (const OESTretchParams > = default
```

Constructor and copy constructor. Constructs an OEStretchParams object for the bond passed as argument.

#### operator=

 $OESTretchParams$  operator=(const OEStretchParams&) = default;

The assignment operator.

## GetAtomIndex1

```
unsigned GetAtomIndex1() const
```

Returns atom index of the first atom making a bond for which the instance of OEStretchParams was created.

## **GetAtomIndex2**

```
unsigned GetAtomIndex2() const
```

Returns atom index of the second atom making a bond for which the instance of OEStretchParams was created.

## **IsValid**

```
bool IsValid(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>& pred) const
bool IsValid(const OESystem::OEUnaryPredicate<OEChem::OEBondBase>& pred) const
```

Methods which check if an instance of the OEStretchParams class was created for a bond to be included in force field calculation. The first method provides a predicate which tests each of the 2 atoms belonging to a bond for which the above instance was created, while the second method provides a predicate which tests a particular bond.

## **IsBond**

bool IsBond (const OEChem:: OEBondBase\* bond) const

Used to check if the bond passed as an argument belongs to the current OEStretchParams instance.

# 3.2.33 OEStretchPotential

**Attention:** This API is currently available in C++ and Python.

class OEStretchPotential : public virtual OEMolPotential::OEFFPotential

The OEStretchPotential defines an interface all bond stretching force field interaction potentials.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The OEStretchPotential implements the following methods:

 $\bullet$  Set

## **Constructors**

```
OEStretchPotential(const OEFFParams&)
{\tt OESTretohPotential} \hspace{1.5mm} \textbf{(const} \hspace{1.5mm} {\tt OESTretohPotential\, \& \,)}
```

Constructor and copy constructor.

## **Assignment operator**

OEStretchPotential& operator=(const OEStretchPotential&)

Assignment operator.

#### **Set**

**bool** Set (OESystem::OEUnaryPredicate<OEChem::OEBondBase>&)

This method can be used for interaction-level control of the bond stretching terms. Interactions between two atoms are only included if the test of the unary bond predicate returns true. The Set method must be called before the Setup for it to be effective.

## 3.2.34 OESubsetAdaptor

Attention: This API is currently available in C++ and Python.

class OESubsetAdaptor : public OEMolAdaptor2

The OESubsetAdaptor class allows optimization of Cartesian coordinates for a subset of atoms in a molecule, while the remaining atoms are fixed. This is accomplished by subsetting the coordinates and gradients into the subsets which correspond to atoms being optimized. Additional facilities are provided for excluding invariant molecule function interactions, and controlling which subset of atoms are held fixed during an optimization.

The following methods are publicly inherited from OEAdaptor:

- · AdaptVar
- GetVar

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEMolAdaptor:

![](_page_128_Figure_1.jpeg)

· SetMolFunc

The following methods are publicly inherited from OEMolAdaptor2:

• SetMolFunc

The OESubsetAdaptor class defines the following public methods:

- · AdaptGrad
- · AdaptHessian
- $Set$

### **Constructors**

```
OESubsetAdaptor(OEMolFunc1 &, bool own=false, bool excludeInteract=true)
OESubsetAdaptor(OEMolFunc2 &, bool own=false, bool excludeInteract=true)
```

Default and copy constructors.

The molecule function used for function evaluation must be provided as the first argument to the constructor. The second argument specifies whether the OESubsetAdaptor object takes ownership of the memory of the molecule function instance. By default that does not happen, so the OESubsetAdaptor destructor does not delete the molecule function instance. If ownership of the molecule function is transferred to the OESubsetAdaptor instance, the molecule function's delete operator will be called in the OESubsetAdaptor destructor. The third argument controls the inclusion of invariant molecule function interactions. By default, interactions which remain constant during the optimization are

excluded from calculation. Interactions composed entirely of atoms held fixed during the optimization will not change during the optimization. Excluding invariant interactions does not affect the optimization, however, the total energy calculated for a set of coordinates will be altered by the exclusion. If the third calling argument is false then all interactions will be computed during every function evaluation.

## **AdaptGrad**

bool AdaptGrad (double \*ga, const double \*g) const

Takes a set of gradients from a molecule function evaluation as the second argument, and subsets the gradients into the array passed as the first argument.

### **AdaptHessian**

bool AdaptHessian (double \*ha, const double \*h) const

Takes a set of hessians from a molecule function evaluation as the second argument, and subsets the hessians into the array passed as the first argument.

#### **Set**

bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&)

This method assigns an atom predicate which is used to specify atoms which are to be held fixed in their starting positions during an optimization. The  $Set$  method must be called before the  $Setup$  for it to be effective.

## 3.2.35 OETorAdaptor

Attention: This API is currently available in C++ and Python.

class OETorAdaptor : public OEMolAdaptor

The OETorAdaptor class provides the ability to optimize torsion angles of a molecule while holding bond lengths and bond angles fixed. OEMolFunc1 derived classes typically require Cartesian coordinates for function evaluation. OETorAdaptor transforms a set of torsions into Cartesian coordinates, passes the resultant coordinates to the internally stored OEMolFunc1 type function, and transforms the Cartesian gradients back into torsion gradients. Additional facilities are provided for excluding invariant molecule function interactions, controlling the definition of a rotatable bond, and fixing atomic positions during coordinate transformation.

The following methods are publicly inherited from OEAdaptor:

- · AdaptVar
- · GetVar

#### The following methods are publicly inherited from OEFunc0:

- · operator()
- · GetFComponents
- · NumVar

![](_page_130_Figure_1.jpeg)

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEMolAdaptor:

· SetMolFunc

The OETorAdaptor class defines the following public methods:

- · AdaptGrad
- $\bullet$  Set

## **Constructors**

OETorAdaptor (OEMolFunc1 &, bool own=false, bool excludeInteract=true)

Default and copy constructors.

Constructs an OETorAdaptor instance. The molecule function used for function evaluation must be provided as the first argument to the constructor. The second argument specifies whether the OETorAdaptor object takes ownership of the memory of the molecule function instance. By default the OETorAdaptor instance does not take ownership of the molecule function, so the OETorAdaptor destructor does not delete the molecule function instance. If ownership of the molecule function is transferred to the OETorAdaptor instance, the molecule function's delete operator will be called

in the OETorAdaptor destructor. The third argument controls the inclusion of invariant molecule function interactions. By default, interactions which remain constant during the torsion minimization are excluded from calculation (for example bond stretch interactions). If the third calling argument is false then all interactions will be computed during every function evaluation.

## **AdaptGrad**

bool AdaptGrad (double \*torGrad, const double \*grads) const

Takes a set of Cartesian gradients of a conformer (second argument), and transforms them into angular torsion gradients (first argument).

#### **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&)
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase>&)
```

The first method assigns an atom predicate which is used to specify atoms which are to be held fixed in their starting positions during an optimization. The second method assigns a bond predicate which is used to determine which bonds of a molecule are to be rotated during an optimization. Both the  $Set$  methods must be called before the  $Setup$  for it to be effective.

## 3.2.36 OETorQuatAdaptor

Attention: This API is currently available in C++ and Python.

class OETorQuatAdaptor : public OEMolAdaptor

The OETorOuatAdaptor class provides the ability to optimize a molecule in coordinate space by a combination of rotation, translation and torsion changes. This class combines the functionality of both OEQuatAdaptor and OE-TorAdaptor classes. Its main application is optimization of ligands in the potential generated by protein-receptor, in the case when ligand's bond lengths and bond angles are chosen to be fixed.

#### The following methods are publicly inherited from OEAdaptor:

- · AdaptVar
- · GetVar

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

 $\bullet$  operator()

The following methods are publicly inherited from OEMolFunc:

 $\bullet$  Clear

![](_page_132_Figure_1.jpeg)

- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEMolAdaptor:

• SetMolFunc

The OETorQuatAdaptor class defines the following public methods:

- · AdaptGrad
- $\bullet$  Set

## **Constructors**

OETorQuatAdaptor(OEMolFunc1 &, bool own=false, bool excludeInteract=true)

Default and copy constructors.

The molecule function used for function evaluation must be provided as the first argument to the constructor. The second argument specifies whether the OETorQuatAdaptor object takes ownership of the memory of the molecule function instance. By default the OETorQuatAdaptor instance does not take ownership of the molecule function, so the OETorQuatAdaptor destructor does not delete the molecule function instance. If ownership of the molecule function is transferred to the OETorQuatAdaptor instance, the molecule function's delete operator will be called in the OETorQuatAdaptor destructor. The third argument controls the inclusion of invariant molecule function interactions. By default, interactions which remain constant during the torsion minimization are excluded from calculation (for example bond stretch interactions). If the third calling argument is false then all interactions will be computed during every function evaluation.

## **AdaptGrad**

bool AdaptGrad(double  $*$ , const double  $*$ , const double  $*$ ) const

Transforms a set of the input Cartesian gradients passed to the method as a second argument, into torsional-rotationaltranslational gradients which are copied to the first argument array. The third argument to the method is an array of the current quaternion and translational vector.

#### **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&)
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase>&)
```

The first method assigns an atom predicate which is used to specify atoms which are to be held fixed in their starting positions during an optimization. The second method assigns a bond predicate which is used to determine which bonds of a molecule are to be rotated during an optimization. Both the  $Set$  methods must be called before the  $Setup$  for it to be effective.

# 3.2.37 OETorsionParams

Attention: This API is currently available in C++ and Python.

class OETorsionParams : public OEMolPotential:: OEInteractParams

The OETorsionParams class defines generic torsion parameters used in any force field which has torsion term.

The following methods are publicly inherited from OEInteractParams:

- · Clear
- $\bullet$  Get
- $\bullet$  Get
- $\bullet$  Set
- $\bullet$  Set

The OETorsionParams class defines the following public methods:

- · GetAtomIndex1
- · GetAtomIndex2
- · GetAtomIndex3
- · GetAtomIndex4
- · IsValid
- · IsTorsion

## **Constructors**

```
OETorsionParams (const OEChem:: OEBondBase* bond, const OEChem:: OEAtomBase* atom1,
                const OEChem:: OEAtomBase* atom2)
OETorsionParams (const OETorsionParams&) = default;
```

Constructor and copy constructor. Constructs an *OETorsionParams* object for a middle bond passed as the first argument and two terminal atoms (second and third arguments).

#### operator=

OETorsionParams& operator=(const OETorsionParams&) = default

The assignment operator.

### GetAtomIndex1

unsigned GetAtomIndex1() const

Returns atom index of the first atom for a torsion for which the instance of OETorsionParams was created.

#### GetAtomIndex2

unsigned GetAtomIndex2() const

Returns atom index of the second atom for a torsion for which the instance of *OETorsionParams* was created.

#### GetAtomIndex3

unsigned GetAtomIndex3() const

Returns atom index of the third atom for a torsion for which the instance of OETorsionParams was created.

#### GetAtomIndex4

unsigned GetAtomIndex4() const

Returns atom index of the forth atom for a torsion for which the instance of *OETorsionParams* was created.

#### **IsValid**

```
bool IsValid() const;
bool IsValid(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>& pred) const;
bool IsValid(const OESystem::OEUnaryPredicate<OEChem::OEBondBase>& pred) const;
```

Methods which check if an instance of the OETorsionParams class was created for the torsion to be included in force field calculation. First method is checking if the above instance was correctly constructed, while two remaining methods provide predicates which test if atoms (second method) and a middle bond (third method) belong to that instance.

## **IsTorsion**

```
bool IsTorsion (const OEChem:: OEAtomBase* atoml, const OEChem:: OEAtomBase* atom2,
               const OEChem:: OEAtomBase* atom3, const OEChem:: OEAtomBase* atom4)
```

Used to check if 4 atoms passed as arguments belong to the current OETorsionParams instance.

# 3.2.38 OETorsionPotential

Attention: This API is currently available in C++ and Python.

class OETorsionPotential : public virtual OEMolPotential:: OEFFPotential

The OETorsionPotential defines an interface for all torsional force field interaction potentials.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The OETorsionPotential implements the following methods:

 $\bullet$  Set

## **Constructors**

```
OETorsionPotential (const OEFFParams&)
OETorsionPotential (const OETorsionPotential&)
```

Constructor and copy constructor.

## **Assignment operator**

OETorsionPotential& operator=(const OETorsionPotential&)

Assignment operator.

### **Set**

bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEBondBase, OEChem:: OEBondBase>&)

This method provides interaction-level control of the torsion terms. The method tests the central bond of a torsion angle. If such a bond returns true from the predicate test then all torsions that cross the bond are included in the list of interactions to be calculated. The  $Set$  method must be called before the  $Setup$  for it to be effective.

## 3.2.39 OEVdwParams

Attention: This API is currently available in C++ and Python.

class OEVdwParams : public OEMolPotential:: OEInteractParams

The OEVdwParams class defines generic vdw parameters used in any force field which has Lennard-Jones 6-12 (or similar 7-14) non-bonded term.

The following methods are publicly inherited from OEInteractParams:

- $\bullet$  Clear
- $\bullet$  Get
- $\bullet$  Set

The OEVdwParams class defines the following public methods:

- · GetAtomIndex1
- · GetAtomIndex2
- · GetAtom1
- · GetAtom2
- · IsValid
- $ISPair$

## **Constructors**

```
OEVdwParams (const OEChem:: OEAtomBase* atom1, const OEChem:: OEAtomBase* atom2)
OEVdwParams operator=(const OEVdwParams&) = default;
```

Constructor and copy constructor. Constructs an OEVdwParams object for a pair of atoms passed as arguments.

#### operator=

```
OEVdwParams operator = (const OEVdwParams&) = default;
```

The assignment operator.

### GetAtomIndex1

unsigned GetAtomIndex1() const

Returns atom index of the first atom from non-bonded interacting pair for which the instance of OEVdwParams was created.

#### **GetAtomIndex2**

unsigned GetAtomIndex2() const

Returns atom index of the second atom from non-bonded interacting pair for which the instance of OEVdwParams was created.

## GetAtom1

const OEChem:: OEAtomBase\* GetAtom1 () const

Returns the first atom from non-bonded interacting pair for which the instance of OEVdwParams was created.

#### GetAtom2

const OEChem:: OEAtomBase\* GetAtom2 () const

Returns the second atom from non-bonded interacting pair for which the instance of OEVdwParams was created.

### **IsValid**

```
bool IsValid(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>& pred) const
bool IsValid(const OESystem::OEBinaryPredicate<OEChem::OEAtomBase, OEChem::OEAtomBase>
\leftrightarrow (pred) const
```

Methods which check if an instance of the OEVdwParams class was created for a pair of non-bonded atoms to be included in force field calculation. The first method provides a predicate which is used to test individually each of the two atoms from the non-boned pair, while the second method provides a predicate which tests a non-bonded pair of atoms in a single test.

## **IsPair**

bool IsPair (const OEChem:: OEAtomBase\* atom1, const OEChem:: OEAtomBase\* atom2) const

Used to check if atoms passed as arguments belong to the current OEStretchParams instance.

# 3.2.40 OEVdwPotential

Attention: This API is currently available in C++ and Python.

class OEVdwPotential : public virtual OENonBondPotBase

The OEVdwPotential class defines an interface for calculation of intra-molecular VdW force field interaction potentials.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEFFPotential:

 $\bullet$  Set

The following methods are publicly inherited from OENonBondPotBase:

- · GetNonBondOptions
- $\bullet$  Set

## **Constructors**

```
OEVdwPotential (const OEFFParams&, const double cutoff) = default;
OEVdwPotential (const OEVdwPotential&) = default;
```

Constructor and copy constructor.

## **Assignment operator**

OEVdwPotential& operator=(const OEVdwPotential&) = default;

Assignment operator.

# **3.3 OEMolPotential Constants**

# 3.3.1 OEFFParam

Attention: This API is currently available in C++ and Python.

This namespace contains constants used to define integer constants, associated with OEInteractParams, that are used to retrieve force field parameters.

## $r0$

Equilibrium bond length.

## **EqDist**

Equilibrium bond length.

## **EqDistance**

Equilibrium bond length.

# **StretchConst**

Bond stretching constant.

## $\mathbf k$

Bond stretching constant.

## rij

Radius parameter in van der Waals potential.

## rij

Square of radius parameter in van der Waals potential.

## **ContactDist**

Radius parameter in van der Waals potential.

## **Epsilon**

Energy parameter in van der Waals potential.

## eps

Energy parameter in van der Waals potential.

## $a<sub>0</sub>$

Equilibrium bending angle.

## **EqAngle**

Equilibrium bending angle.

## **BendConst**

Angle bending constant.

## ka

Angle bending constant.

## $kb1$

First constant term in the stretch-bend potential.

## **StretchBendConst1**

First constant term in the stretch-bend potential.

## **StretchBendConst2**

Second constant term in the stretch-bend potential.

## $kb2$

Second constant term in the stretch-bend potential.

## $r1$

First distance term in the stretch-bend potential.

# $r2$

Second distance term in the stretch-bend potential.

## **OutOfPlaneConst**

Out-of-plane potential constant.

## **OOP**

Out-of-plane potential constant.

## ko

Out-of-plane potential constant.

## $V<sub>1</sub>$

First constant term in torsion potential.

## $V<sub>2</sub>$

Second constant term in torsion potential.

## $V3$

Third constant term in torsion potential.

## $V<sub>1</sub>$

First constant term in torsion potential.

# $v2$

Second constant term in torsion potential.

## $v3$

Third constant term in torsion potential.

## p1

Periodicity of improper torsion (used in SMIRNOFF)

## ph1

Phase of improper torsion (used in SMIRNOFF)

## ntt

Number of terms in torsion Fourier expansion

## listKv

Identifies vector which stores torsion barrier heights

## **listDv**

Identifies vector which stores a set of torsion degeneracies

## **listPv**

Identifies vector which stores a set of torsion periodicities

## **listPhy**

Identifies vector which stores a set of torsion phases

# 3.3.2 OEVarType

Attention: This API is currently available in C++ and Python.

This namespace contains constants which define the type of molecular coordinates to be optimized.

## **SolidBody**

Defines 6 degrees of freedom: 3 translations and 3 rotations. Because rotations are represented with quaternions, the total number of variables is 7.

## **Torsions**

Torsional coordinates which are defined as hindered rotations around single bonds. Molecule has as many torsions as the number of rotatable bonds.

## **Cart**

3N Cartesian coordinates where N is the number of atoms in the molecule.

## **TranRotTor**

A combination of SolidBody and Torsions defined above, usually used for the optimization of a ligand inside the protein binding site.

# 3.3.3 OEFuncType

Attention: This API is currently available in C++ and Python.

This namespace contains constants which define the type of force field potential components which might be used separately or in combination for the energy estimation of a molecular system. Constants defined below are passed to the methods *OEMolFunc*. Set as a second parameter.

## **Undefined**

Undefined potential type.

## VdW

Defines vdW potential type represented by the OEVdwPotential class.

## **VdWRepel**

Same as above but without long range attractive forces.

## **Coulomb**

Defines Coulomb potential type represented by the OECoulombPotential class.

## **Bond**

Defines bond stretching potential type represented by the OEStretchPotential class.

## **Stretch**

Same as above

## **Bend**

Defines angle bending potential type represented by the OEBendPotential class.

## **StretchBend**

Defines angle-stretch coupling potential type represented by the OEMMFFStretchBend class.

## **Torsion**

Defines torsion potential type represented by the OETorsionPotential class.

### **ImproperTorsion**

Defines improper torsion potential type represented by the OEOutOfPlanePotential class.

## **OutOfPlane**

Same as above.

## All

Defines a combination of all 7 above components.

### **AllRepel**

Same as above with a modified vdW component of the OEFuncType\_VdWRepel type.

#### **InterMolVdW**

Defines intermolecular vdW potential type represented by the OEInterVdwPotential class.

## **InterMolCoulomb**

Defines intermolecular Coulomb potential type represented by the OEInterCoulombPotential class.

## **TorAdapt**

Defines torsion adaptor potential type represented by the OETorAdaptor class.

## **QuatAdapt**

Defines quaternion adaptor potential type represented by the OEQuatAdaptor class.

#### **SubsetAdapt**

Defines subset adaptor potential type represented by the OESubsetAdaptor class.

#### **SubsetAdaptor**

Same as above.

#### **InterAdapt**

Defines internal coordinates adaptor potential type represented by the OEInterAdaptor class.

## **HarmonicPot**

Defines harmonic potential type represented by the OEHarmonicPotential class.

#### **Sheffield**

Defines Sheffield solvation potential type represented by the OESheffield class.

# **3.4 OEConstr Classes**

# 3.4.1 OEDihedralQuadPenalty

Attention: This API is currently available in C++ and Python.

class OEDihedralQuadPenalty : public OEMolPotential:: OEMolFunc2

The OEDihedralQuadPenalty class defines harmonic restraints to dihedrals or torsions. The restraint is applied on the cosine of the angle, in the form of  $K * (cos(\alpha) - cos(\alpha_0))^2$ .

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents

#### $\bullet$ NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The OEDihedralQuadPenalty class defines the following public methods:

- · GetPenaltyConstant
- · GetSpecifiedAngle

## **Constructors**

```
OEDihedralQuadPenalty(const OEChem::OEAtomBase& a1, const OEChem::OEAtomBase& a2,
               const OEChem:: OEAtomBase& a3, const OEChem:: OEAtomBase& a4,
               double alpha0)
const OEChem:: OEAtomBase& a1, const OEChem:: OEAtomBase& a2,
               const OEChem:: OEAtomBase& a3, const OEChem:: OEAtomBase& a4,
               double alpha0, double K)
OEDihedralQuadPenalty(const OEDihedralQuadPenalty &)
```

Default and copy constructors. Arguments al-a4 correspond to the four atoms that define the dihedral to be restrained,  $alpha0$  corresponds to the specified angle, and  $K$  corresponds to the penalty force constant.

## operator=

OEDihedralQuadPenalty &operator=(const OEDihedralQuadPenalty&)

### **GetPenaltyConstant**

double GetPenaltyConstant () const

Returns the current value of the penalty force constant.

## **GetSpecifiedAngle**

```
double GetSpecifiedAngle() const
```

Returns the current value of the specified angle *alpha0*.

# 3.4.2 OEHarmonicPotential

Attention: This API is currently available in C++ and Python.

class OEHarmonicPotential : public OEMolPotential:: OEMolFunc1

The OEHarmonicPotential class defines harmonic constraint interactions between atoms.

![](_page_149_Figure_8.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- GetInteractions
- · Setup

## The OEHarmonicPotential class defines the following public methods:

 $\bullet$  Get\_dc

- $\bullet$  Get  $kc$
- $\bullet$  Set
- $\bullet$  Set\_dc
- $\bullet$  Set\_kc

## **Constructors**

```
OEHarmonicPotential (double _kc, double _dc)
OEHarmonicPotential (const OEHarmonicPotential &)
```

Default and copy constructors. Parameters passed in the first constructor correspond to k and d in the harmonic potential  $V = k(r - d)^2$ .

#### operator=

OEHarmonicPotential &operator=(const OEHarmonicPotential&)

#### Get dc

double Get\_dc() const

Returns the current value of parameter d (constraining distance) in constraining potential  $V = k(r - d)^2$ .

### Get\_kc

double Get\_kc() const

Returns the current value of parameter k (force constant) in constraining potential  $V = k(r - d)^2$ .

## **Set**

bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&)

The Set function can be used to set the unary atomic predicate used for the selective constraining of atoms. This function has to be used before Setup(const OEChem::OEMolBase&).

#### Set dc

void Set\_dc(double d)

Sets d parameter in  $V = k(r - d)^2$ .

#### Set kc

```
void Set_kc(double k)
```

Sets k parameter in  $V = k(r - d)^2$ .

# **3.5 OEMoIMMFF Classes**

## **3.5.1 OEMMFF**

Attention: This API is currently available in C++ and Python.

```
class OEMMFF : public OEMolPotential:: OEGenericFF2
```

The OEMMFF class facilitates creation of an instance of a partial or full MMFF94 or MMFF94s force field. In addition, a force field instance can be extended by adding externally defined potential functions.

![](_page_151_Figure_9.jpeg)

The following methods are publicly inherited from OEFunc0:

• operator ()

- GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEForceField:

- GetTitle and SetTitle
- · HasCoulomb
- · HasInternalCharges
- · PrepMol
- $\bullet$  Set
- · SetNonBondCutoff

The following methods are publicly inherited from OEGenericFF2:

- · AddMolFunc
- · GetComponents
- · RemoveMolFunc

## **Constructors**

```
OEMMFF (const OEMMFFParams& params, const OEMolPotential:: OENonBondIntcsOptions& opts
\rightarrow OEMolPotential:: OENonBondIntcsOptions())
OEMMFF (const OEMMFF&)
```

Default and copy constructors.

#### operator=

OEMMFF& operator=(const OEMMFF&)

The assignment operator.

## 3.5.2 OEMMFF94sParams

Attention: This API is currently available in C++ and Python.

class OEMMFF94sParams : public OEMMFFParams

The OEMMFF94sParams class provides the ability to retrieve parameters necessary to perform energy and gradient calculations using the MMFF94s variant of the MMFF94 force field. Most force field terms are identical between MMFF94 and MMFF94s. The torsion and improper-torsion components of the MMFF94s have a different set of parameters which tend to planarize certain types of trigonal nitrogens.

The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams
- · GetStretchParams
- · GetAtomTypeIndex
- · GetEquilibriumAngle
- GetTorsionParams
- GetAtomTypeName
- · GetEquilibriumBondLength
- GetVdwParams
- GetBendParams
- · GetOutOfPlaneParams
- · GetVdwRadius
- · GetContactDistance
- · GetStretchBendParams
- PrepMol
- · GetVdwParams
- · GetStretchParams
- GetBendParams
- GetTorsionParams
- · GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- · GetTitle

## **Constructors**

OEMMFF94sParams()

Default and copy constructors.

# 3.5.3 OEMMFFOutOfPlane

Attention: This API is currently available in C++ and Python.

```
class OEMMFFOutOfPlane : public OEMolPotential:: OEMolFunc2
```

The OEMMFFOutOfPlane class defines out-of-plane (improper torsion) interaction function using the functional forms used in MMFF94 force field. The function can be initialized with parameters defined in MMFF94 (OEMMFF-Params) or MMFF94s (OEMMFF94sParams) force field, or a different set of user defined parameters (OEFFParams) during construction.

![](_page_154_Figure_8.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEFunc2:

• operator()

#### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

#### The OEMMFFOutOfPlane class defines the following public methods:

 $\bullet$  Set

## **Constructors**

```
OEMMFFOutOfPlane (const OEMMFFOutOfPlane &)
OEMMFFOutOfPlane (const OEMolPotential:: OEFFParams &)
```

Default and copy constructors.

Constructs an OEMMFFOutOfPlane instance using the specified set of parameters.

#### operator=

```
OEMMFFOutOfPlane & operator=(const OEMMFFOutOfPlane &)
```

The assignment operator.

### **Set**

bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&)

This method allows interaction-level control of the out-of-plane term. The predicate passed is used to test all impropertorsions in the molecule. If the predicate returns  $t_{\text{true}}$  for all four atoms engaged in the improper-torsion interaction, then the interaction is included. Conversely, if the predicate test of any one of the four atoms of the improper-torsion returns false then the interaction will be excluded from calculation. The Set method must be called before the Set up for it to be effective.

# 3.5.4 OEMMFFParams

Attention: This API is currently available in C++ and Python.

class OEMMFFParams : public OEMolPotential:: OEFFParams

The OEMMFFParams class provides the ability to retrieve parameters used in the MMFF94 force field.

The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams

- · GetStretchParams
- · GetAtomTypeIndex
- · GetEquilibriumAngle
- · GetTorsionParams
- · GetAtomTypeName
- · GetEquilibriumBondLength
- GetVdwParams
- GetBendParams
- GetOutOfPlaneParams
- · GetVdwRadius
- · GetContactDistance
- · GetStretchBendParams
- · PrepMol
- · GetVdwParams
- · GetStretchParams
- · GetBendParams
- · GetTorsionParams
- · GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- GetTitle

## The following classes derive from this class:

• OEMMFF94sParams

### **Constructors**

OEMMFFParams()

Default and copy constructors.

# 3.5.5 OEMMFFStretchBend

Attention: This API is currently available in C++ and Python.

```
class OEMMFFStretchBend : public OEMolPotential:: OEMolFunc2
```

The OEMMFFStretchBend class defines stretch-bend interaction function using the functional forms used in MMFF94 force field. The function can be initialized with parameters defined in MMFF94 (OEMMFFParams) or MMFF94s (OEMMFF94sParams) force field, or a different set of user defined parameters (OEFFParams) during construction.

![](_page_157_Figure_5.jpeg)

The following methods are publicly inherited from OEFunc0:

- · operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- · Setup

The OEMMFFStretchBend class defines the following public methods:

 $\bullet$  Set

## **Constructors**

```
OEMMFFStretchBend (const OEMMFFStretchBend &)
OEMMFFStretchBend(const OEMolPotential:: OEFFParams &)
```

#### Default and copy constructors.

Constructs an OEMMFFStretchBend instance using the specified set of parameters.

#### operator=

OEMMFFStretchBend & operator= (const OEMMFFStretchBend &)

The assignment operator.

### Set

bool Set (const OESystem::OEBinaryPredicate<OEChem::OEBondBase, OEChem::OEBondBase>&)

This method defines the set of stretch-bending interactions that should not be included during the  $Setup$ . Set must be called before the Setup for it to be effective.

# **3.6 OEMoIMMFF Functions**

# 3.6.1 OEIsValidMMFFMolecule

Attention: This API is currently available in C++ and Python.

```
bool OEIsValidMMFFMolecule (const OEChem:: OEMolBase& mol)
bool OEIsValidMMFFMolecule (const OEChem:: OEMolBase& mol, const OEMMFFParams& params)
```

This free function checks if MMFF parameters are available for the specified molecule. If the optional argument param is provided, check is performed against that specific OEMMFFParams, otherwise the OEMMFF94sParams is used by default.

## 3.6.2 OEMMFFCalcVdw

Attention: This API is currently available in C++ and Python.

```
double OEMMFFCalcVdw (const OEChem:: OEMolBase & mol,
                     const OEChem:: OEAtomBase *patom,
                     const OEChem:: OEAtomBase *latom, bool coloumb=false,
                     bool attract=false)
```

This free function calculates the VdW/Coulomb interaction energy between a pair of atoms passed to the function as the second and third arguments, belonging to a molecule mol. Coulomb term is added to the result only when the fourth argument to the function is set true. A regular (not modified) MMFF VdW potential is used when the value of the last argument is set to true.

# **3.7 OEMolSmirnoff Classes**

# 3.7.1 OEParslev

**Attention:** This API is currently available in C++ and Python.

```
class OEParsley : public OESmirnoff
```

The OEParsley class facilitates creation of an instance of Parsley force field.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEForceField:

- · GetTitle and SetTitle
- · HasCoulomb
- · HasInternalCharges

- · PrepMol
- $\bullet$  Set
- · SetNonBondCutoff

The following methods are publicly inherited from OEGenericFF2:

- · AddMolFunc
- · GetComponents
- · RemoveMolFunc

## **Constructors**

```
OEParsley (const OEMolPotential:: OENonBondIntcsOptions& opts =_
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OEParsley (const OEParsley&)
```

Default and copy constructors.

#### operator=

OEParsley& operator=(const OEParsley&)

The assignment operator.

# 3.7.2 OEParsleyParams

Attention: This API is currently available in C++ and Python.

class OEParsleyParams : public OESmirnoffParams

The OEParsleyParams class provides the ability to retrieve parameters necessary to perform energy and gradient calculations using the OEParsley force field.

The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams
- · GetStretchParams
- · GetAtomTypeIndex
- · GetEquilibriumAngle
- · GetTorsionParams
- GetAtomTypeName
- · GetEquilibriumBondLength
- · GetVdwParams
- · GetBendParams

- · GetOutOfPlaneParams
- · GetVdwRadius
- · GetContactDistance
- · GetStretchBendParams
- · PrepMol
- GetVdwParams
- · GetStretchParams
- GetBendParams
- · GetTorsionParams
- · GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- GetTitle

### **Constructors**

```
OEParsleyParams()
OEParsleyParams (const OEParsleyParams&)
```

Default and copy constructors.

## operator=

OEParsleyParams& operator=(const OEParsleyParams&)

The assignment operator.

## 3.7.3 OESage

Attention: This API is currently available in C++ and Python.

class OESage : public OESmirnoff

The OESage class facilitates creation of an instance of Sage force field.

## The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- ClearPredicates
- GetInteractions
- · Setup

#### The following methods are publicly inherited from OEForceField:

- GetTitle and SetTitle
- · HasCoulomb
- · HasInternalCharges
- · PrepMol
- $\bullet$  Set
- · SetNonBondCutoff

## The following methods are publicly inherited from OEGenericFF2:

- · AddMolFunc
- · GetComponents
- RemoveMolFunc

## **Constructors**

```
OESage(const OEMolPotential:: OENonBondIntcsOptions& opts =
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OESage (const OESage&)
```

Default and copy constructors.

## operator=

OESage& operator=(const OESage&)

The assignment operator.

# 3.7.4 OESageParams

Attention: This API is currently available in C++ and Python.

class OESageParams : public OESmirnoffParams

The OESageParams class provides the ability to retrieve parameters necessary to perform energy and gradient calculations using the OESage force field.

#### The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams
- · GetStretchParams
- · GetAtomTypeIndex
- · GetEquilibriumAngle
- GetTorsionParams
- · GetAtomTypeName
- · GetEquilibriumBondLength
- GetVdwParams
- · GetBendParams
- · GetOutOfPlaneParams
- · GetVdwRadius
- · GetContactDistance
- · GetStretchBendParams
- · PrepMol
- GetVdwParams
- · GetStretchParams
- · GetBendParams
- GetTorsionParams
- · GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- · GetTitle

## **Constructors**

```
OESageParams()
OESageParams (const OESageParams&)
```

Default and copy constructors.

#### operator=

OESageParams& operator=(const OESageParams&)

The assignment operator.

# 3.7.5 OESmirnoff

Attention: This API is currently available in C++ and Python.

class OESmirnoff : public OEMolPotential:: OEGenericFF2

The OESmirnoff class facilitates creation of an instance of SMIRNOFF force field (see SMIRNOFF). In addition, a force field instance can be extended by adding externally defined potential functions.

#### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEForceField:

- · GetTitle and SetTitle
- · HasCoulomb
- · HasInternalCharges
- · PrepMol
- $\bullet$  Set

· SetNonBondCutoff

### The following methods are publicly inherited from OEGenericFF2:

- · AddMolFunc
- · GetComponents
- RemoveMolFunc

## **Constructors**

```
OESmirnoff (const OESmirnoffParams& params, const
→OEMolPotential::OENonBondIntcsOptions& opts =
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OESmirnoff (const OESmirnoff&)
```

Default and copy constructors.

### operator=

OESmirnoff& operator=(const OESmirnoff&)

The assignment operator.

# 3.7.6 OESmirnoffParams

Attention: This API is currently available in C++ and Python.

class OESmirnoffParams : public OEMolPotential:: OEFFParams

The OESmirnoffParams class provides the ability to retrieve parameters necessary to perform energy and gradient calculations using the SMIRNOFF force field (see SMIRNOFF). By default OESmirnoffParams loads the Smirnoff99Frost force field.

Note: The inherited methods, GetAtomTypeIndex, GetAtomTypeName and GetStretchBendParams, have no meaning in the SMIRNOFF force field and SHOULD NOT be used. When these methods are called, they return 0, none, and false, respectively.

The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams
- · GetStretchParams
- · GetAtomTypeIndex
- · GetEquilibriumAngle
- · GetTorsionParams
- GetAtomTypeName

- · GetEquilibriumBondLength
- GetVdwParams
- · GetBendParams
- · GetOutOfPlaneParams
- · GetVdwRadius
- · GetContactDistance
- · GetStretchBendParams
- PrepMol
- GetVdwParams
- · GetStretchParams
- · GetBendParams
- · GetTorsionParams
- · GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- GetTitle

#### **Constructors**

```
OESmirnoffParams()
{\tt OESmin} {\tt noffParameters}\ ({\tt const\ } {\tt OESmin} {\tt noffParameters} \, \&\, )
```

Default and copy constructors.

#### operator=

OESmirnoffParams& operator=(const OESmirnoffParams&)

The assignment operator.

### Load

```
bool Load (const unsigned int fftype)
bool Load (const std:: string& xml_file_name)
bool Load (const OEPlatform:: oeisstream& ifs)
```

Methods which load force field parameters. The first method is used to load available build-in parameter set, defined in the OESmi rnoffType namespace. The second method takes the name of the parameter file in XML format. This file might contain user custom parameters. The third method takes a stream object oeisstream which contains Smirnoff parameters. It is a convenience method which might be used in user code when the parameters XML file is converted a stream.

# **3.8 OEMolSmirnoff Constants**

# 3.8.1 OESmirnoffType

This namespace contains constants that are used in OESmirnoffParams. Load to define a specific build-in set of paramaters which might be used.

## SMIRNOFF99FROSST

SMIRNOFF99FROSST set of parameters

## **PARSLEY OPENFF**

Parsley OpenFF1.3.1 set of parameters

## **SAGE\_OPENFF**

Latest version of the Sage set of parameters

# **3.9 OESheff Classes**

# 3.9.1 OESheffield

Attention: This API is currently available in C++ and Python.

class OESheffield : public OEMolPotential:: OEMolFunc2

This class represents OESheffield.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator ()

The following methods are publicly inherited from OEMolFunc:

· Clear

![](_page_168_Figure_1.jpeg)

- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The OESheffield class defines the following public methods:

- · GetDielectricDerivative
- $\bullet$  Set
- SetCharges
- · SetRadii

## **Constructors**

```
OESheffield()
OESheffield(const OESheffieldOptions&)
OESheffield(const OESheffield&)
```

Default and copy constructors.

The first constructor uses default options and the second uses the user specific options. The default Sheffield model parameters are set according to Grant et. al. ([Grant-2007]).

#### operator=

```
OESheffield & operator= (const OESheffield &)
```

## **GetDielectricDerivative**

double GetDielectricDerivative (const double \*x, double solv\_diel) const

Returns the derivative of the solvation energy with respect to the solvent dielectric constant.

#### **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEAtomBase, OEChem:: OEAtomBase>&)
```

Sets the unary and binary predicates respectively which might be used to modify the results of the calculations. Unary predicate might be used to selectively exclude a subset of atoms from the calculation of molecule "self" energy, while the binary predicate can include only selected pairs of atoms in the calculation of solvation energy. By default when no predicates are set, atomic pairs are included in the solvation energy of a molecule.

## **SetCharges**

```
void SetCharges (float*)
```

Atomic charges are taken from the provided external array.

#### **SetRadii**

void SetRadii (float\*)

Atomic radii values are taken from the provided external array.

## 3.9.2 OESheffieldOptions

Attention: This API is currently available in C++ and Python.

class OESheffieldOptions : public OESystem:: OEOptions

This class orovides interface to setup options required for OESheffield calculations.

The OESheffieldOptions class defines the following public methods:

- $\bullet$  GetA
- $\bullet$  GetB
- $\bullet$  GetC
- · GetSoluteDielectricConstant

- · GetSolventDielectricConstant
- $\bullet$  SetA
- $\bullet$  SetB
- $\bullet$  SetC
- · SetSoluteDielectricConstant
- · SetSolventDielectricConstant

## **Constructors**

```
OESheffieldOptions()
OESheffieldOptions (const OESheffieldOptions&)
```

Default and copy constructors.

#### operator=

OESheffieldOptions & operator= (const OESheffieldOptions &)

### **GetA**

double GetA() const

Gets the first Sheffield parameter value.

## **GetB**

double GetB() const

Gets the second Sheffield parameter value.

## **GetC**

double GetC() const

Gets the third Sheffield parameter value.

## **GetSoluteDielectricConstant**

```
double GetSoluteDielectricConstant() const
```

Gets the dielectric constant of the solute.

## **GetSolventDielectricConstant**

double GetSolventDielectricConstant() const

Gets the dielectric constant of the solvent.

#### **SetA**

bool SetA(const double a)

Optionally changes the first Sheffield parameter to the passed value a.

## **SetB**

bool SetB (const double b)

Optionally changes the second Sheffield parameter to the passed value b.

## **SetC**

bool SetC(const double c)

Optionally changes the third Sheffield parameter to the passed value c.

## **SetSoluteDielectricConstant**

bool SetSoluteDielectricConstant (const double epsilon)

Sets the dielectric constant for the solute.

## **SetSolventDielectricConstant**

bool SetSolventDielectricConstant (const double eps)

Sets the dielectric constant for the solvent.

# **3.10 OESheff Constants**

## 3.10.1 OESheffieldParamType

This namespace contains constants that defines which set of Sheffield parameters are to be loaded in construction of OESheffieldOptions.

## **SmallMol**

Classical Sheffield parameters suitable for small-molecules

## **Protein**

Modified Sheffield parameters suitable for proteins and complexes

# **3.11 OEFF Classes**

# 3.11.1 OEComplexEnergies

#### class OEComplexEnergies

This class provides energy components resulting from energy calculation for a protein-ligand complex.

#### The OEComplexEnergies class defines the following public methods:

- · GetComplexSolvationEnergy
- · GetDesolvationEnergy
- · GetHostComponents
- · GetHostEnergy
- · GetHostSolvationEnergy
- · GetInterComponents
- GetInterEnergy
- · GetLigandComponents
- · GetLigandEnergy
- · GetLigandSolvationEnergy
- GetTotalEnergy

#### **Constructors**

```
OEComplexEnergies()
OEComplexEnergies (const OEComplexEnergies&)
```

Default and copy constructors.

#### operator=

OEComplexEnergies & operator= (const OEComplexEnergies &)

## **GetComplexSolvationEnergy**

double GetComplexSolvationEnergy() const

Returns the solvation energy of the protein-ligand complex.

## **GetDesolvationEnergy**

double GetDesolvationEnergy() const

Returns the desolvation energy.

## **GetHostComponents**

OESystem:: OEIterBase<OEOpt:: OEFComponent>\* GetHostComponents() const

Returns the intra-molecular energy components of the host (protein) molecule.

#### **GetHostEnergy**

double GetHostEnergy () const

Returns the total intra-molecular energy of the host (protein) molecule.

## **GetHostSolvationEnergy**

double GetHostSolvationEnergy () const

Returns the solvation energy of the host (protein) molecule.

## **GetInterComponents**

OESystem::OEIterBase<OEOpt::OEFComponent>\* GetInterComponents() const

Returns the inter-molecular energy components of the complex.

#### **GetInterEnergy**

double GetInterEnergy() const

Returns the total inter-molecular energy.

#### **GetLigandComponents**

OESystem:: OEIterBase<OEOpt:: OEFComponent>\* GetLigandComponents() const

Returns the intra-molecular energy components of the ligand molecule.

## **GetLigandEnergy**

double GetLigandEnergy () const

Returns the total intra-molecular energy of the ligand molecule.

#### GetLigandSolvationEnergy

double GetLigandSolvationEnergy() const

Returns the solvation energy of the ligand molecule.

#### **GetTotalEnergy**

double GetTotalEnergy () const

Returns the total energy of the complex.

## 3.11.2 OEComplexFF

Attention: This API is currently available in C++ and Python.

class OEComplexFF : public OEMolFunc1

The OEComplexFF is a generic class for force-fields of complexes. This class defines an interface for combining multiple OEForceField to easily construct a force field for a host/guest or protein/ligand complex. The OEComplexFF extends the OEMolFunc1 class to allow this being a collection of multiple force fields.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

#### The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

## The OEComplexFF class defines the following public methods:

- · AdaptHostCoords
- · GetVar
- $\bullet$  Set
- SetHostFlex
- · SetNonBondCutoff
- SetupHost

### The following classes derive from this class:

- OEMMFFComplex
- OESmirnoffComplex
- OEMMFFAmberComplex
- OEFF14SBSmirnoffComplex

### **Constructors**

```
OEComplexFF (const OEMolPotential:: OEForceField& ligandFF,
            const OEMolPotential:: OEForceField& hostFF,
            const OEMolPotential:: OEInterMolFunc1& interFF);
OEComplexFF (const OEComplexFF&)
```

Default and copy constructors.

Construction of a OEComplexFF requires a OEForceField for the guest or the ligand molecule, a OEForceField for the host or the protein molecule, and an OEInterMolFunc1 for the inter-molecular interactions.

## **AdaptHostCoords**

bool AdaptHostCoords (double \*coords, const double \*var) const

Takes a set of variables as the second argument and provides the corresponding host molecule coordinates into the first argument. This method is used to obtain optimized coordinates for the flexible host or protein molecule.

## **GetVar**

void GetVar (double\* var, const double\* coords)

Takes reference coordinates of the molecule, and transforms them into the variable type or coordinate system ( $var$ ) that will be used during an optimization. The transfored variables here provides the combined host/guest coordinates, whenoptimization involves flexible host or protein molecule.

#### **Set**

```
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &pred,
         unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEAtomBase,
         OEChem:: OEAtomBase> &pred, unsigned int functype)
bool Set (const OESystem:: OEBinaryPredicate<OEChem:: OEBondBase,
         OEChem:: OEBondBase> &pred, unsigned int functype)
```

These methods assigns interaction-control predicates, and only applies to the guest or the ligand molecule. The first argument is the predicate type to be passed to the interaction component. The second argument is a value or a set of binary OR'ed values taken from the  $OEFuncType$  namespace which specifies the intended target for the predicate assignment.

The Set method passes on the interaction-control predicates to the appropriate force field components contained. Method returns false if predicate was not set to any of the components contained by the force field.

Set must be called before the Setup for it to be effective.

## **SetHostFlex**

bool SetHostFlex (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>& pred)

Set predicate to define the flexible portion of the host or protein molecule. If no predicate is set to define flexibility, the host or protein is considered rigid.

SetHostFlex must be called before the Setup for it to be effective.

### **SetNonBondCutoff**

bool SetNonBondCutoff (const double)

Sets non-bonded interactions cutoff. Setting a value of  $0.0$  or less assumes that all interactions should be included without any cutoff.

### **SetupHost**

bool SetupHost (const OEChem:: OEMolBase& host)

This method defines the interface for initializing the host in the OEComplexFF.

SetupHost must be called before calling Setup.

# 3.11.3 OEComplexFFParameter

Attention: This API is currently available in C++ and Python.

```
class OEComplexFFParameter : public OESystem:: OEMultiParameter
→<OEMolPotential::OEForceField>
```

The OEComplexFFParameter represents parameter that has a value of type OEComplexFF.

## Following methods are publicly inherited from OEParameter:

- AddAlias and GetAliases
- . AddDetail and GetDetail
- · AddIllegalRange and GetIllegalRanges
- · AddIllegalValue and GetIllegalValues
- · AddLegalRange and GetLegalRanges
- · AddStringDefault, GetStringDefault and GetStringDefaults
- · AddStringValue, GetStringValue andw GetStringValues
- · ClearDefaults
- ClearValues
- CreateCopy
- GetBrief and SetBrief
- · GetHasDefault
- · GetHasValue
- · GetIsList and SetIsList
- · GetKeyless and SetKeyless
- GetName and SetName
- · GetOrderPriority and SetOrderPriority
- · GetVisibility and SetVisibility
- · IsLegalString
- · IsSet and IsSetToString

## Following methods are publicly inherited from OEMultiParameter:

· AddLegalEntry

- · GetDefault and SetDefault
- · GetSetting
- · GetValue and SetValue

#### **Constructors**

```
OEComplexFFParameter()
OEComplexFFParameter (const std::string& name, const bool customAllowed)
OEComplexFFParameter (const OEComplexFFParameter&)
```

Default and copy constructors.

Constructs an OEComplexFFParameter instance using the specified set of parameters. The second argument in the second constructor represents if a custom force field can be used.

### operator=

OEComplexFFParameter & operator= (const OEComplexFFParameter &)

The assignment operator.

# 3.11.4 OEFF14SBParsleyComplex

Attention: This API is currently available in C++ and Python.

class OEFF14SBParsleyComplex : public OEComplexFF

The OEFF14SBParsleyComplex represents a force field for a protein-ligand complex system, where the interactions are described with OEFF14SBParsleyParams.

#### The following methods are publicly inherited from OEFunc0:

- · operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

#### The following methods are publicly inherited from OEComplexFF:

· AdaptHostCoords

- · GetVar
- $\bullet$  Set
- SetHostFlex
- · SetNonBondCutoff
- SetupHost

## **Constructors**

```
OEFF14SBParsleyComplex(const OEMolPotential::OENonBondIntcsOptions& opts =
→OEMolPotential::OENonBondIntcsOptions())
OEFF14SBParsleyComplex(const OEFF14SBParsleyComplex&)
```

Default and copy constructors.

# 3.11.5 OEFF14SBSmirnoffComplex

Attention: This API is currently available in C++ and Python.

class OEFF14SBSmirnoffComplex : public OEComplexFF

The OEFF14SBSmirnoffComplex represents a force field for a protein-ligand complex system, where the interactions are described with OEFF14SBSmirnoffParams.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEComplexFF:

- · AdaptHostCoords
- $\bullet$  GetVar
- $\bullet$  Set
- SetHostFlex
- · SetNonBondCutoff

· SetupHost

## **Constructors**

```
OEFF14SBSmirnoffComplex(const OEFF14SBSmirnoffParams& params =
\rightarrowOEFF14SBSmirnoffParams(),
                   const OEMolPotential:: OENonBondIntcsOptions& opts =
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OEFF14SBSmirnoffComplex(const OEFF14SBSmirnoffComplex&)
```

Default and copy constructors.

# 3.11.6 OEForceFieldParameter

Attention: This API is currently available in C++ and Python.

```
class OEForceFieldParameter : public OESystem:: OEMultiParameter
→<OEMolPotential::OEForceField>
```

The OEForceFieldParameter represents parameter that has a value of type OEForceField.

#### Following methods are publicly inherited from OEParameter:

- AddAlias and GetAliases
- · AddDetail and GetDetail
- · AddIllegalRange and GetIllegalRanges
- · AddIllegalValue and GetIllegalValues
- · AddLegalRange and GetLegalRanges
- · AddStringDefault, GetStringDefault and GetStringDefaults
- · AddStringValue, GetStringValue and GetStringValues
- · ClearDefaults
- · ClearValues
- CreateCopy
- GetBrief and SetBrief
- · GetHasDefault
- · GetHasValue
- · GetIsList and SetIsList
- GetKeyless and SetKeyless
- GetName and SetName
- · GetOrderPriority and SetOrderPriority
- · GetVisibility and SetVisibility
- · IsLegalString

· IsSet and IsSetToString

#### Following methods are publicly inherited from OEMultiParameter:

- · AddLegalEntry
- · GetDefault and SetDefault
- · GetSetting
- · GetValue and SetValue

## **Constructors**

```
OEForceFieldParameter()
OEForceFieldParameter (const std:: string& name, const bool customAllowed)
OEForceFieldParameter(const OEForceFieldParameter&)
```

Default and copy constructors.

Constructs an OEForceFieldParameter instance using the specified set of parameters. The second argument in the second constructor represents if a custom forcefield can be used.

#### operator=

OEForceFieldParameter &operator=(const OEForceFieldParameter &)

The assignment operator.

# 3.11.7 OEMMFFAmberComplex

**Attention:** This API is currently available in C++ and Python.

class OEMMFFAmberComplex : public OEComplexFF

The OEMMFFAmberComplex represents a force field for a protein-ligand complex system, where both the protein and ligand intra-molecular interactions are described with OEMMFFParams and the inter-molecular interactions are described with Amber.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates

- · GetInteractions
- · Setup

#### The following methods are publicly inherited from OEComplexFF:

- · AdaptHostCoords
- GetVar
- $\bullet$  Set
- SetHostFlex
- · SetNonBondCutoff
- SetupHost

## **Constructors**

```
OEMMFFAmberComplex(const OEMolMMFF:: OEMMFFParams& params = OEMolMMFF:: OEMMFFParams(),
                    const OEMolPotential:: OENonBondIntcsOptions& opts =_
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OEMMFFAmberComplex(const OEMMFFAmberComplex&)
```

Default and copy constructors.

# 3.11.8 OEMMFFComplex

Attention: This API is currently available in C++ and Python.

class OEMMFFComplex : public OEComplexFF

The OEMMFFComplex provides a predefined interface to use OEMMFF for all interactions in a protein-ligand complex.

#### The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

#### The following methods are publicly inherited from OEMolFunc:

- Clear
- · ClearPredicates
- GetInteractions
- $Set up$

#### The following methods are publicly inherited from OEComplexFF:

· AdaptHostCoords

- · GetVar
- $\bullet$  Set
- SetHostFlex
- · SetNonBondCutoff
- · SetupHost

## **Constructors**

```
OEMMFFComplex (const OEMolMMFF:: OEMMFFParams& params = OEMolMMFF:: OEMMFFParams (),
                 const OEMolPotential:: OENonBondIntcsOptions& opts =
\qquad \qquad \mbox{$\hookrightarrow$ OEMolPotential: : OENonBondIntcsOptions()$)}OEMMFFComplex (const OEMMFFComplex&)
```

Default and copy constructors.

# 3.11.9 OEMMFFIEFF

Attention: This API is currently available in C++ and Python.

```
class OEMMFFIEFF : public OEMolPotential: : OEGenericFF
```

The OEMMFFIEFF class facilitates creation of an instance of a MMFFIEFF force field. The MMFFIEFF hybrid force field uses MMFF for intramolecular interactions and Amber for intermolecular interactions. In addition, a force field instance can be extended by adding externally defined potential functions.

![](_page_183_Figure_13.jpeg)

### The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- · Setup

The following methods are publicly inherited from OEForceField:

- · PrepMol
- $\bullet$  Set

## The following methods are publicly inherited from OEGenericFF:

- · AddMolFunc
- · GetComponents
- · RemoveMolFunc

## **Constructors**

```
OEMMFFIEFF (const OEChem:: OEMolBase & host)
OEMMFFIEFF (const OEChem:: OEMolBase &host, const OEMMFFIEFFOptions& options)
```

Default and copy constructors.

The first constructor creates the force field with default options. The second constructor creates the force field with user specified options. The host refers to the host molecule for the interactions.

## 3.11.10 OEMMFFIEFFOptions

Attention: This API is currently available in C++ and Python.

class OEMMFFIEFFOptions : public OESystem: : OEOptions

This class orovides interface to setup options required for OEMMFFIEFF initialization.

The OEMMFFIEFFOptions class defines the following public methods:

- Get IEFFTerms
- · GetMMFFTerms
- · GetUseMMFF94s

- · Set IEFFTerms
- SetMMFFTerms
- SetUseMMFF94s

#### **Constructors**

```
OEMMFFIEFFOptions()
OEMMFFIEFFOptions (const OEMMFFIEFFOptions&)
```

Default and copy constructors.

#### operator=

OEMMFFIEFFOptions & operator=(const OEMMFFIEFFOptions&)

## **GetIEFFTerms**

unsigned int GetIEFFTerms () const

Gets the constant defining what terms of the IEFF force field to be used.

## **GetMMFFTerms**

unsigned int GetMMFFTerms() const

Gets the constant defining what terms of the MMFF force field to be used.

## GetUseMMFF94s

bool GetUseMMFF94s() const

Gets flag that defines if MMFF94s variation of parameters should be used.

## **SetIEFFTerms**

void SetIEFFTerms (const unsigned int)

Sets the constant defining what terms of the IEFF force field to be used.

## **SetMMFFTerms**

void SetMMFFTerms (const unsigned int)

Sets the constant defining what terms of the MMFF force field to be used.

#### **SetUseMMFF94s**

void SetUseMMFF94s (const bool)

Sets flag that defines if MMFF94s variation of parameters should be used.

# 3.11.11 OEMMFFSheffield

Attention: This API is currently available in C++ and Python.

class OEMMFFSheffield : public OEMolPotential: : OEGenericFF2

The OEMMFFSheffield is a hybrid force field that combines the OEMMFF with the OESheffield. This force field is designed to be used exactly as that of *OEMMFF* or a variation of it, such as a truncated-OEMMFF, OEMMFF without electrostatics, or OEMMFF with OESheffield.

..seealso:

```
* :ref:'sub-section_MMFF-IEFF' section
* :ref:'section_mmff' section
```

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEForceField:

- · PrepMol
- $\bullet$  Set

![](_page_187_Figure_1.jpeg)

The following methods are publicly inherited from OEGenericFF2:

- · AddMolFunc
- · GetComponents
- RemoveMolFunc

# **Constructors**

OEMMFFSheffield()

Default constructor.

OEMMFFSheffield (const OEMMFFSheffieldOptions& options)

Creates the force field with user specified options.

## 3.11.12 OEMMFFSheffieldOptions

Attention: This API is currently available in C++ and Python.

class OEMMFFSheffieldOptions : public OESystem: : OEOptions

This class provides interface to setup options required for OEMMFFSheffield initialization.

The OEMMFFSheffieldOptions class defines the following public methods:

- · GetDielectric and SetDielectric
- · GetExponent and SetExponent
- GetForceFieldType and SetForceFieldType

#### **Constructors**

```
OEMMFFSheffieldOptions()
OEMMFFSheffieldOptions (const OEMMFFSheffieldOptions&)
```

Default and copy constructors.

## operator=

```
OEMMFFSheffieldOptions & operator=(const OEMMFFSheffieldOptions &)
```

#### **GetDielectric**

double GetDielectric() const

See SetDielectric method.

## **GetExponent**

double GetExponent () const

See SetExponent method.

### **GetForceFieldType**

```
unsigned int GetForceFieldType() const
```

See SetForceFieldType method.

## **SetDielectric**

bool SetDielectric (const double)

The Dielectric defines the solvent dielectric constant to be used for coulombic interactions with OEMMFF. Default:  $1.0.$ 

## **SetExponent**

bool SetExponent (const double)

The Exponent defines the coulombic exponent term to be used for coulombic interactions with OEMMFF. Default:  $1.0.$ 

### **SetForceFieldType**

bool SetForceFieldType (const unsigned int)

The ForceFieldType defines the variation of forcefield to be used. Options are defined in the OEMMFFSheffieldFFType namespace. Default: OEMMFFSheffieldFFType\_MMFF94Smod\_NOESTAT.

# 3.11.13 OEFF14SBSageComplex

Attention: This API is currently available in C++ and Python.

class OEFF14SBSageComplex : public OEComplexFF

The OEFF14SBSageComplex represents a force field for a protein-ligand complex system, where the interactions are described with OEFF14SBSageParams.

#### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

#### The following methods are publicly inherited from OEComplexFF:

· AdaptHostCoords

- $\bullet$  GetVar
- $\bullet$  Set
- SetHostFlex
- · SetNonBondCutoff
- · SetupHost

## **Constructors**

```
OEFF14SBSageComplex(const OEMolPotential::OENonBondIntcsOptions& opts =_
→OEMolPotential::OENonBondIntcsOptions())
OEFF14SBSageComplex(const OEFF14SBSageComplex&)
```

Default and copy constructors.

# 3.11.14 OEFF14SBSmirnoff

Attention: This API is currently available in C++ and Python.

class OEFF14SBSmirnoff : public OEGenericFF2

The OEFF14SBSmirnoff is a generic class for protein systems which might contain cofactors. It assumes that the intetractions are descrined with **OEFF14SBSmirnoffParams**.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- · ClearPredicates
- GetInteractions
- · Setup

The following methods are publicly inherited from OEForceField:

 $\bullet$  Set

The following methods are publicly inherited from OEGenericFF2:

· AddMolFunc

- GetComponents
- RemoveMolFunc

#### The following classes derive from this class:

- OEFF14SBParsley
- OEFF14SBSage

### **Constructors**

```
OEFF14SBSmirnoff(const OEFF14SBSmirnoffParams& params = OEFF14SBSmirnoffParams(),
                 const OEMolPotential:: OENonBondIntcsOptions& opts =
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OEFF14SBSmirnoff (const OEFF14SBSmirnoff&)
```

Default and copy constructors.

#### operator=

OEFF14SBSmirnoff& operator=(const OEFF14SBSmirnoff&)

The assignment operator.

### **PrepMol**

```
bool PrepMol(OEChem::OEMolBase& mol, bool sweep = true, bool warnOK = true) const
```

Prepares molecule to be handled with proper parameters

## 3.11.15 OEFF14SBSmirnoffParams

Attention: This API is currently available in C++ and Python.

class OEFF14SBSmirnoffParams : public OEMolPotential:: OEFFParams

The OEFF14SBSmirnoffParams class provides the ability to retrieve parameters necessary to perform energy and gradient calculations using OEFF14SBSmirnoff force field. By default parameters for the Smirnoff99Frost force field are used to handle nonprotein part of the molecular system.

Note: The inherited methods, GetAtomTypeIndex, GetAtomTypeName and GetStretchBendParams, have no meaning in the SMIRNOFF force field and SHOULD NOT be used.

The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams
- · GetStretchParams

- · GetAtomTypeIndex
- · GetEquilibriumAngle
- GetTorsionParams
- · GetAtomTypeName
- · GetEquilibriumBondLength
- GetVdwParams
- GetBendParams
- GetOutOfPlaneParams
- · GetVdwRadius
- · GetContactDistance
- · GetStretchBendParams
- · PrepMol
- GetVdwParams
- · GetStretchParams
- · GetBendParams
- · GetTorsionParams
- · GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- · GetTitle

## **Constructors**

```
OEFF14SBSmirnoffParams()
OEFF14SBSmirnoffParams(const OEFF14SBSmirnoffParams&)
```

Default and copy constructors.

#### operator=

OEFF14SBSmirnoffParams& operator=(const OEFF14SBSmirnoffParams&)

The assignment operator.

Load

```
bool Load (const unsigned int fftype)
bool Load (const std::string& xml_file_name)
bool Load (const OEPlatform:: oeisstream& ifs)
```

Methods which load force field parameters for the SMIRNOFF/Parsley part of the potential. First method is used to load available build-in parameter set defined in the OESmirnoffType namespace. Second method takes the name of the parameter file in XML format. This file might contain user custom parameters. Third method takes a stream object oeisstream which contains Smirnoff parameters. It is a convenience method which might be used in user code when the parameters XML file is converted to a stream.

# 3.11.16 OEFF14SBSage

**Attention:** This API is currently available in C++ and Python.

class OEFF14SBSage : public OEFF14SBSmirnoff

The OEFF14SBSage is a class for protein systems which might contain cofactors. It assumes that the iteraction are described with OEFF14SBSageParams.

#### The following methods are publicly inherited from OEFunc0:

- · operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEFunc2:

• operator()

### The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEForceField:

 $• Set$ 

The following methods are publicly inherited from OEGenericFF2:

- · AddMolFunc
- · GetComponents
- · RemoveMolFunc

The following methods are publicly inherited from OEFF14SBSmirnoff

· PrepMol

## **Constructors**

```
OEFF14SBSage(const OEMolPotential:: OENonBondIntcsOptions& opts =
\rightarrow OEMolPotential:: OENonBondIntcsOptions())
OEFF14SBSage(const OEFF14SBSage&)
```

Default and copy constructors.

### operator=

```
OEFF14SBSage& operator=(const OEFF14SBSage&)
```

The assignment operator.

## 3.11.17 OEFF14SBSageParams

Attention: This API is currently available in C++ and Python.

class OEFF14SBSageParams : public public OEFF14SBSmirnoffParams

The OEFF14SBSageParams class provides the ability to retrieve parameters necessary to perform energy and gradient calculations using the OEFF14SBSage force field.

Note: The inherited methods, GetAtomTypeIndex, GetAtomTypeName and GetStretchBendParams, have no meaning in the Sage force field and SHOULD NOT be used.

#### The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams
- · GetStretchParams
- · GetAtomTypeIndex
- · GetEquilibriumAngle
- · GetTorsionParams
- GetAtomTypeName
- · GetEquilibriumBondLength
- · GetVdwParams
- GetBendParams
- · GetOutOfPlaneParams
- · GetVdwRadius
- · GetContactDistance

- · GetStretchBendParams
- PrepMol
- · GetVdwParams
- · GetStretchParams
- GetBendParams
- · GetTorsionParams
- GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- · GetTitle

## The following methods are publicly inherited from OEFF14SBSmirnoffParams:

 $-Load$ 

## **Constructors**

```
OEFF14SBSageParams()
OEFF14SBSageParams (const OEFF14SBSageParams&)
```

Default and copy constructors.

#### operator=

OEFF14SBSageParams& operator=(const OEFF14SBSageParams&)

The assignment operator.

# 3.11.18 OEFF14SBParsley

Attention: This API is currently available in C++ and Python.

class OEFF14SBParsley : public OEFF14SBSmirnoff

The OEFF14SBParsley is a class for protein systems which might contain cofactors. It assumes that the iteraction are described with OEFF14SBParsleyParams.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEFunc2:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- · Clear
- ClearPredicates
- GetInteractions
- · Setup

The following methods are publicly inherited from OEForceField:

 $\bullet$  Set

The following methods are publicly inherited from OEGenericFF2:

- · AddMolFunc
- · GetComponents
- · RemoveMolFunc

The following methods are publicly inherited from OEFF14SBSmirnoff

· PrepMol

## **Constructors**

```
OEFF14SBParsley (const OEMolPotential:: OENonBondIntcsOptions& opts = ...
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OEFF14SBParsley (const OEFF14SBParsley&)
```

Default and copy constructors.

## operator=

OEFF14SBParsley& operator=(const OEFF14SBParsley&)

The assignment operator.

# 3.11.19 OEFF14SBParsleyParams

Attention: This API is currently available in C++ and Python.

class OEFF14SBParsleyParams : public public OEFF14SBSmirnoffParams

The OEFF14SBParsleyParams class provides the ability to retrieve parameters necessary to perform energy and gradient calculations using the OEFF14SBParsley force field.

Note: The inherited methods, GetAtomTypeIndex, GetAtomTypeName and GetStretchBendParams, have no meaning in the Parsley force field and SHOULD NOT be used.

## The following methods are publicly inherited from OEFFParams:

- CreateCopy
- · GetCoulombParams
- · GetStretchParams
- GetAtomTypeIndex
- · GetEquilibriumAngle
- · GetTorsionParams
- · GetAtomTypeName
- · GetEquilibriumBondLength
- GetVdwParams
- · GetBendParams
- · GetOutOfPlaneParams
- GetVdwRadius
- · GetContactDistance
- · GetStretchBendParams
- PrepMol
- GetVdwParams
- · GetStretchParams
- · GetBendParams
- · GetTorsionParams
- · GetOutOfPlaneParams
- · HasVdwParams
- · HasStretchParams
- · HasBendParams
- · HasTorsionParams
- · GetTitle

The following methods are publicly inherited from OEFF14SBSmirnoffParams:

 $\bullet$  Load

## **Constructors**

```
OEFF14SBParsleyParams()
OEFF14SBParsleyParams(const OEFF14SBParsleyParams&)
```

Default and copy constructors.

#### operator=

OEFF14SBParsleyParams& operator=(const OEFF14SBParsleyParams&)

The assignment operator.

# 3.11.20 OESmirnoffComplex

Attention: This API is currently available in C++ and Python.

class OESmirnoffComplex : public OEComplexFF

The OESmirnoffComplex provides a predefined interface to use OESmirnoff for all interactions in a protein-ligand complex.

### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

### The following methods are publicly inherited from OEMolFunc:

- $\bullet$  Clear
- · ClearPredicates
- · GetInteractions
- $\bullet$  Setup

#### The following methods are publicly inherited from OEComplexFF:

- · AdaptHostCoords
- GetVar
- $\bullet$  Set
- SetHostFlex
- · SetNonBondCutoff
- SetupHost

## **Constructors**

```
OESmirnoffComplex(const OEMolSmirnoff:: OESmirnoffParams& params = ,\rightarrowOEMolSmirnoff:: OESmirnoffParams(),
                   const OEMolPotential:: OENonBondIntcsOptions& opts =_
\rightarrowOEMolPotential::OENonBondIntcsOptions())
OESmirnoffComplex (const OESmirnoffComplex&)
```

Default and copy constructors.

# **3.12 OEFF Functions**

# 3.12.1 OEClearForceFieldDummyAtom

**void** OEClearForceFieldDummyAtom (OEChem::OEAtomBase \*atom)

Clear any force field dummy atom information associated with the specified atom by OESetForceFieldDummyAtom.

## See also:

- · OESetForceFieldDummyAtom function
- · OEIsForceFieldDummyAtom function
- · OEClearForceFieldDummyAtoms function

Note: This function is defined in the OEChem TK, but in the OEFF main namespace.

# 3.12.2 OEClearForceFieldDummyAtoms

void OEClearForceFieldDummyAtoms (OEChem:: OEMolBase &mol)

Clear any force field dummy atom information for all atoms in the molecule.

### See also:

- · OESetForceFieldDummyAtom function
- · OEIsForceFieldDummyAtom function
- · OEClearForceFieldDummyAtom function

Note: This function is defined in the OEChem TK, but in the OEFF main namespace.

# 3.12.3 OEGetMMFFSheffieldFFName

std::string OEGetMMFFSheffieldFFName(const unsigned int);

Get the OEMMFFSheffield forcefield name, corresponding to the given type ID. The valid type ID's are defined in the OEMMFFSheffieldFFType namespace.

### See also:

- · OEGetMMFFSheffieldFFType function
- · OEIsValidMMFFSheffieldFF function

## 3.12.4 OEGetMMFFSheffieldFFType

unsigned int OEGetMMFFSheffieldFFType (const std::string&)

Get the OEMMFFSheffield forcefield type ID, as defined in the OEMMFFSheffieldFFType namespace, corresponding to the given string.

See also:

- · OEGetMMFFSheffieldFFType function
- · OEIsValidMMFFSheffieldFF function

## 3.12.5 OEIsForceFieldDummyAtom

**bool** OEIsForceFieldDummyAtom(const OEChem::OEAtomBase \*atom)

Returns whether OESetForceFieldDummyAtom has been used on the atom to indicate it can be used as a force field dummy atom. The atom's atomic number does *not* have to be OEE1emNo Du for the function to return t rue.

See also:

- · OESetForceFieldDummyAtom function
- · OEClearForceFieldDummyAtom function
- OEClearForceFieldDummyAtoms function

Note: This function is defined in the OEChem TK, but in the OEFF main namespace.

## 3.12.6 OEIsValidMMFFSheffieldFF

```
bool OEIsValidMMFFSheffieldFF (const std::string&)
bool OEIsValidMMFFSheffieldFF (const unsigned int)
```

Check if the specified value correspond to a valid OEMMFFSheffield forcefield.

See also:

- · OEGetMMFFSheffieldFFName function
- · OEGetMMFFSheffieldFFType function

# 3.12.7 OESetForceFieldDummyAtom

void OESetForceFieldDummyAtom(OEChem::OEAtomBase \*atom)

Modify information associated with an atom to indicate that if the atom has atomic number OEE1emNo\_Du it can be used for certain force field calculations where it would not normally be valid.

**Note:** Currently, only **MMFF** and **Amber** support support dummy atoms at all, and even then *only* for calculations involving non-bonded terms and when this special indication has been set.

See also:

- · OEIsForceFieldDummyAtom function
- OEClearForceFieldDummyAtom function
- OEClearForceFieldDummyAtomsfunction

Note: This function is defined in the OEChem TK, but in the OEFF main namespace.

# 3.12.8 OEFFGetArch

const char \*OEFFGetArch()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify the hardware architecture. The format of these strings may change over time.

# 3.12.9 OEFFGetLicensee

```
std::string OEFFGetLicensee()
bool OEFFGetLicensee (std::string &licensee)
```

Returns the licensee name from the license file.

# 3.12.10 OEFFGetPlatform

```
const char *OEFFGetPlatform()
```

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify a platform. The format of these strings may change over time, and future distributions may contain different values even when using the same operating system, compiler and processor. For example, on a x86\_64 Red Hat Enterprise Linux box this would return  $redhat-RHEL7-q++4.1-x64.$ 

## 3.12.11 OEFFGetRelease

const char \*OEFFGetRelease()

Returns the release name of the OEFF library being used. This returns a value similar to  $2.0.0$  for production versions of the library, and 2.0.0 debug for the checking version of the library.

# 3.12.12 OEFFGetSite

```
std::string OEFFGetSite()
bool OEFFGetSite(std::string &site)
```

Returns the physical site location of the licensee as registered in the license file.

# 3.12.13 OEFFGetVersion

unsigned int OEFFGetVersion()

Returns the version number of the library being used. This is an unsigned integer value indicating the date on which the library was built, for example  $20141001$ , for the 1st of October 2014. This value should be used when reporting problems, and unlike the release string, may be used in comparisons if needed.

# 3.12.14 OEFFIsLicensed

bool OEFFIsLicensed (const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any OEFF TK functionality.

The 'feature' argument can be used to check for a valid license to OEFF TK along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'explate' argument can be used to obtain the expiration date of the current \*OEFF TK license.

See also:

• OEChemIsLicensed function

# **3.13 OEFF Constants**

# 3.13.1 OELigandFFType

This namespace contains constants that define force fields type appropriate for working with ligands.

## MMFF94

The Merck Molecular Force Field (MMFF). Name: mmff94

### MMFF94S

The 94s variation of the Merck Molecular Force Field (MMFF). Name: mmff94s

## **PARSLEY**

The latest version (1.3.1) of the Parsley series of force field from the OPENFF consortium. Name: parsley

## **SAGE**

The latest version (2.0.0) of the Sage series of force field from the OPENFF consortium. Name: sage

# 3.13.2 OEMMFFSheffieldFFType

This namespace contains constants that are used with OEMMFFSheffieldOptions to define a specific OEMMFFSheffield forcefield.

## **MMFF**

The Merck Molecular Force Field (MMFF). Name: mmff

## **MMFF NOESTAT**

The MMFF forcefield without electrostatics. Name: mmff\_NoEstat

## **MMFF\_TRUNC**

The MMFF forcefield truncated at potential minimum. Name: mmff\_Trunc

## **MMFF SHEFF**

The MMFF forcefield with Sheffield solvation. Name: mmff\_Sheff

## MMFF94S

The 94s variation of the Merck Molecular Force Field (MMFF). Name: mmff94s

### **MMFF94S\_NOESTAT**

The MMFF94S forcefield without electrostatics. Name: mmff94s\_NoEstat

## **MMFF94S\_TRUNC**

The MMFF94S forcefield truncated at potential minimum. Name: mmff94s\_Trunc

#### MMFF94S\_SHEFF

The MMFF94S forcefield with Sheffield solvation. Name: mmff94s\_Sheff

#### **MMFF94Smod**

The modified 94s variation of the Merck Molecular Force Field (MMFF). Name: mmff94smod

## **MMFF94Smod NOESTAT**

The modified MMFF94S forcefield without electrostatics. Name: mmff94smod\_NoEstat

## MMFF94Smod\_TRUNC

The modified MMFF94S forcefield truncated at potential minimum. Name: mmff94smod\_Trunc

# MMFF94Smod\_SHEFF

The modified MMFF94S forcefield with Sheffield solvation. Name: mmff94smod\_Sheff

## **Invalid**

Invalid force field type.

# **CHAPTER**

# **FOUR**

# **RELEASE HISTORY**

# 4.1 OEFF TK 2.8.0

# 4.1.1 New features

- The constant  $OESmi rno fff \gamma pe\_SAGE\_OPENFF$  now refers to the 2.2.1 version of the Sage OpenFF force field.
- Any SMIRNOFF set of parameters loaded using OESmirnoffParams, including the built-in OESageParams and OEParsleyParams, are now supplemented with van der Waals parameters for many metals and counterions, as used with the OpenMM package.
- The OEMMFF94sParams and OEMMFFParams are now supplemented with a generic set of van der Waals parameters for many metals and counterions to improve robustness.
- A new function, OEIsValidMMFFMolecule, has been added that can be used to check if OEMMFFParams are available for a molecule.

# 4.1.2 Minor Bug Fixes

• Loading a SMIRNOFF set of parameters using *OESmirnoffParams* no longer picks up the library charges.

# 4.2 OEFF TK 2.7.1

## 4.2.1 New features

- The following preliminary API classes have been made permanent.
  - OENonBondIntcsOptions
  - $-$  OEComplexFF
  - $-$  OEComplexFFParameter
  - OEFF14SBParsley
  - OEFF14SBParsleyComplex
  - OEFF14SBSage
  - OEFF14SBSageComplex
  - OEFF14SBSmirnoff

- OEFF14SBSmirnoffComplex
- OEForceFieldParameter
- OEMMFFAmberComplex
- OEMMFFComplex
- OESmirnoffComplex

# 4.2.2 Minor bug fixes

• The Get and Set methods in OEInteractParams are now exposed properly in Python.

# 4.3 OFFF TK 2.7.0

# 4.3.1 New features

- A new method, *HasInternalCharges*, has been added to *OEForceField* that returns a boolean indicating whether the parameters in the OEForceField contain charges.
- A new method, *HasCoulomb*, has been added to *OEForceField* that returns a boolean indicating whether coulombic interactions are turned on.
- A new method, GetNonBondOptions, has been added to OENonBondPotBase that provides access to its internal OENonBondIntcsOptions.
- A new method, SetNonBondCutoff, has been added to OEComplexFF that provides a way to set nonbonded interactions cutoffs.

# 4.3.2 Major bug fixes

• The internal algorithms for VdW parameter assignment with *OESmirnoffParams* have been modified to improve performance in working with large molecules.

# 4.3.3 Minor bug fixes

• The  $GetTitle$  method for  $OESimilar$  now properly returns the user set title of the force field.

# 4.4 OEFF TK 2.5.2.1

• Support for the latest released version of the force field from the Open Force Field Initiative (Sage 2.1.0) has been added. The constant OESmirnoffType\_SAGE\_OPENFF now refers to this latest version of Sage force field.

# 4.5 OEFF TK 2.5.2.0

# 4.5.1 Major bug fixes

• The OEComplexFF class is now derived from OEMolFunc2 and has limited support for second derivatives when the protein is fixed.

# 4.6 OEFF TK 2.5.1

# 4.6.1 New features

• Two new constants, OESmirnoffType PARSLEY OPENFF and OESmirnoffType SAGE OPENFF, have been added to OESmirnoffType that define the latest versions of Parsley and Sage forcefields respectively.

# 4.6.2 Major bug fixes

- An issue resulting in a crash when a combine force field ff14SB/OpenFF Sage or ff14SB/OpenFF Parsley was applied to a small molecule which was not a part of the protein-ligand complex has been fixed.
- VdW parameters for atoms which are not explicitly given in the Sage or Parsley versions of OpenFF and are not tabulated in ff14SB parameter sets are now taken from the original AMBER parameter set. An example of such systems are proteins with metal cofactors. Until now such systems failed to be processed by instances of force field classes OEFF14SBParsley or OEFF14SBSage.

# 4.6.3 Minor bug fixes

• A missing improper torsion parameter in ff14SB force field for residue PTR, which is defined by three carbon atoms from a benzene ring and oxygen from a phosphate group, has been added.

# 4.7 OFFF TK 2.5.0

# 4.7.1 New features

- Class OESheffield has been extended with a model which approximates solvation of proteins. This extension might be useful for evaluation of differences in solvation energies between protein conformations and in protein loop modeling.
- The following methods have been added to the OEComplexEnergies class:
  - GetComplexSolvationEnergy
  - GetDesolvationEnergy
  - GetHostSolvationEnergy
  - GetLigandSolvationEnergy
- A new OELigandFFType namespace has been added that defines force fields suitable for working with ligands.

- A new OESheffieldParamType namespace has been added that defines different available Sheffield parameter types.
- Two new methods have been added to OESheffieldOptions:
  - $-$  GetC
  - $-$  SetC

# 4.7.2 Major bug fixes

- An issue have been fixed where failure to assign atom vdw parameters were ignored resulting in calculations being performed with values of zero being assigned as the parameters. Effect of this fix could be observed in calculations performed using the following force fields:
  - $-$  OESmirnoff
  - OEParsley
  - $-$  OESage
  - OEFF14SBSmirnoff
  - OEFF14SBParsley
  - OEFF14SBSage
- Semiempirical AM1/PM3 calculations are not allowed for molecules in which atoms indexing is not compatible with the number of atoms. Until now passing molecules with that feature could caused segmentation fault.

# 4.8 OEFF TK 2.4.0

Fall 2021

## 4.8.1 New features

- The following new classes have been added to provide support for the OpenFF 2.0.0 Sage force field:
  - OESageParams
  - OEFF14SBSageParams
  - $-$  OESage
  - OEFF14SBSage
  - OEFF14SBSageComplex
- OEForceFieldParameter and OEComplexFFParameter now accept case-insensitive string input values.

# 4.8.2 Minor bug fixes

• A potential risk of vectors going out-of-bounds while working with OESmirnoff and related classes have been addressed.

# 4.9 OEFF TK 2.3.1

**July 2021** 

Minor internal improvements have been made.

# 4.10 OEFF TK 2.3.0

Fall 2020

# 4.10.1 New features

- A new generic set of force field potential classes has been added to simplify implementing new force fields in **OEFF TK:** 
  - OEFFPotential
  - $-$  OEStretchPotential
  - $-$  OEBendPotential
  - OETorsionPotential
  - $-$  OEOutOfPlanePotential
  - OENonBondPotBase
  - $-$  OENonBondPotential
  - $-$  OEVdwPotential
  - $-$  OECoulombPotential
  - $-$  OEInterNonBondPotBase
  - $-$  OEInterNonBondPotential
  - OEInterVdwPotential
  - $-$  OEInterCoulombPotential
- With the introduction of the new generic force field potential classes in OEFF TK, several previously existing classes have been deprecated. The following table shows the deprecated classes and their replacements:

| <b>Deprecated Class</b>             | New Class                             |
|-------------------------------------|---------------------------------------|
| OEMolPotential::OEStretchBase       | <i><b>OEStretchPotential</b></i>      |
| OEMolMMFF::OEMMFFStretch            |                                       |
| OEMolSmirnoff::OESmirnoffStretch    |                                       |
| OEMolMMFF::OEMMFFBend               | <i><b>OEBendPotential</b></i>         |
| OEMolSmirnoff::OESmirnoffBend       |                                       |
| OEMolMMFF::OEMMFFTorsion            | <i><b>OETorsionPotential</b></i>      |
| OEMolSmirnoff::OESmirnoffTorsion    |                                       |
| OEMolSmirnoff::OESmirnoffOutOfPlane | <i><b>OEOutOfPlanePotential</b></i>   |
| OEMolPotential::OENonBondBase       | <i><b>OENonBondPotBase</b></i>        |
| OEMolMMFF::OEMMFFVdw                | <i><b>OEVdwPotential</b></i>          |
| OEMolSmirnoff::OESmirnoffVdw        |                                       |
| OEMolMMFF::OEMMFFCoulomb            | <i><b>OECoulombPotential</b></i>      |
| OEMolSmirnoff::OESmirnoffCoulomb    |                                       |
| OEMolMMFF::OEMMFFInterVdw           | <i><b>OEInterVdwPotential</b></i>     |
| OEMolMMFF::OEMMFFInterVdwNN         |                                       |
| OEMolSmirnoff::OESmirnoffInterVdw   |                                       |
| OEMolMMFF::OEMMFFInterCoulomb       | <i><b>OEInterCoulombPotential</b></i> |

- New OpenFF parameters  $\text{parsey}\_1.2.1$  have been added as built-in parameters and can be used in the construction of an *OESmirnoff* object.
- Two new classes, *OEParsleyParams* and *OEParsley*, have been added that work with the latest versions of available OpenFF Parsley force fields.
- New FF14SB ([Maier-2015]) protein force field parameters have been implemented. These parameters are accessible through the following parameter and force field classes.
  - OEFF14SBSmirnoffParams: an FF14SB for proteins with custom OESmirnoffParams for cofactor and/or ligand
  - OEFF14SBParsleyParams: an FF14SB for proteins with OEParsleyParams for cofactor and/or ligand
  - OEFF14SBSmirnoff: a force field for proteins with OEFF14SBSmirnoffParams
  - OEFF14SBParsley: a force field for proteins with OEFF14SBParsleyParams
  - OEFF14SBSmirnoffComplex: a force field for protein-ligand complexes with OEFF14SBSmirnoffParams
  - OEFF14SBParsleyComplex: a force field for protein-ligand complex with OEFF14SBParsleyParams
- A new class, *OEMMFFAmberComplex*, has been added that allows protein-ligand optimization with protein flexibility. Accordingly, OEFF:: OEMMFFAmber has been deprecated.
- A new preliminary class, *OEComplexFFParameter*, has been added as part of the extended set of OEParameter classes. The new parameter class works with predefined complex force fields using an  $OEComplexFF$  object.
- The methods OEFF:: OEComplexFF:: PrepMol and OEFF:: OEComplexFF:: PrepHost have been removed from the preliminary API OEComplexFF as they are no longer required to setup an OEComplexFF.
- A new class, *OEComplexEnergies*, has been added that represents energy components of a protein-ligand complex.
- A new overload of  $GetFComponents$  has been added that provides the energy components in the form of an OEComplexEnergies.

# **4.10.2 Documentation changes**

• All the OEFF TK examples have been reorganized to reflect the modified API behavior.

# 4.11 OEFF TK 2.2.0

# 4.11.1 New features

- OpenFF parameters  $\text{parsey}\_1.0.0$  and  $\text{parsey}\_1.1.1$  are now built-in parameters and can be used in the construction of an *OESmirnoff* object.
- Beginning with this release, custom OpenFF parameters in XML file format can be used. This functionality is achieved by the overloaded method OESmirnoffParams. Load.
- A new set of preliminary api force field classes has been added to simplify working with the host-guest complex system:
  - $-$  OEComplexFF
  - OEMMFFComplex
  - OESmirnoffComplex
- A new preliminary class, OEMo LMMFF:: OEMMFFNonBond, that combines OEMo LMMFF:: OEMMFFVdw and OEMolMMFF:: OEMMFFCoulomb has been added.
- $\bullet$  A new preliminary class. OEMolMMFF:: OEMMFFInterNonBond, that combines OEMolMMFF:: OEMMFFInterVdw and OEMolMMFF:: OEMMFFInterCoulomb has been added.
- OEMolSmirnoff:: OESmirnoffNonBond, combines  $\bullet$  A preliminary class, that new OEMolSmirnoff::OESmirnoffVdw and OEMolSmirnoff::OESmirnoffCoulomb has been added.
- A new preliminary class, OEMolSmirnoff:: OESmirnoffInterCoulomb, has been added to use with the inter-molecular coulomb component in SMIRNOFF-based force fields.
- A new preliminary class, OEMolSmirnoff::OESmirnoffInterNonBond, that combines OEMolMMFF:: OESmirnoffInterVdw OEMolSmirnoff::OESmirnoffInterCoulomb and has been added.
- A new preliminary class, OENonBondIntcsOptions, has been added that provides consistency in setting nonbond interaction calculations in various force fields.
- New constructors for OEMMFF and OESmirnoff have been added that provide consistency and use OENon-*BondIntcsOptions* as arguments.
- Two new SMIRNOFF force fields from the Open Force Field Initiative,  $\text{parsey } 1.0.0$  and  $\text{parsey } 1.$ 1.1, have been added as built-in force fields. They are defined by types PARSLEY\_OPENFF100 and PARS-LEY\_OPENFF111, respectively.
- A new preliminary class, *OEForceFieldParameter*, has been added as part of the extended set of OEParameter classes. The new parameter class works with predefined force fields and custom SMIRNOFF force fields, as well as user-defined *OEForceField* force fields using *OEForceField* for the same parameter object.
- Two new public methods have been added to OEVdwParams:
  - $-$  GetAtom1
  - GetAtom2
- New public methods have been added to OEFFParams:

- HasVdwParams
- HasStretchParams
- HasBendParams
- HasTorsionParams
- GetTitle

## 4.11.2 Major bug fixes

• Copy constructors and assignment operators in the classes OESmirnoffStretch, OESmirnoffBend, OESmirnoffTorsion, and OESmirnoffOutOfPlane had previously failed to copy their private member object of the OESmirnoffParams type. This has been fixed.

For updated information, see Deprecated OEFF Classes.

## 4.11.3 Minor bug fixes

- The following methods now return bool instead of a void:
  - OEMMFFSheffieldOptions. SetDielectric
  - OEMMFFSheffieldOptions. SetExponent
  - OEMMFFSheffieldOptions. SetForceFieldType
  - OESheffieldOptions. SetA
  - OESheffieldOptions.SetB
  - OESheffieldOptions. SetSoluteDielectricConstant
  - OESheffieldOptions.SetSolventDielectricConstant
- The names of the potential components Smirnoff Angle and Smirnoff Imp Torsion were changed to Smirnoff Bend and Smirnoff Improper Torsion, respectively, in order to be compatible with the same term names in the MMFF94 force field.
- The numerical stability in the calculation of second derivatives in the OESmirnoffOutOfPlane class has been improved.

# 4.12 OEFF TK 2.1.0

## 4.12.1 New features

- A new class, *OESmirnoff*, has been added that facilitates creating a SMIRNOFF force field (release 0.3), a small-molecule force field that uses extended SMARTS patterns for its chemical representation of parameters (https://openforcefield.org/). The following classes have also been added that define interaction functions using the functional forms in the SMIRNOFF force field:
  - OESmirnoffParams
  - OEMolSmirnoff:: OESmirnoffStretch
  - OEMolSmirnoff:: OESmirnoffBend
  - OEMolSmirnoff:: OESmirnoffTorsion

- OEMolSmirnoff:: OESmirnoffOutOfPlane
- OEMolSmirnoff:: OESmirnoffVdw
- OEMolSmirnoff:: OESmirnoffInterVdw
- OEMolSmirnoff:: OESmirnoffCoulomb
- The following classes, derived from the parent class OEInteractParams, have been added to create a set of force field parameters for a given molecule:
  - $-$  OEStretchParams
  - OEBendParams
  - OETorsionParams
  - OEVdwParams
  - $-$  OEOutOfPlaneParams
- The OEFFParam namespace has been expanded to support SMIRNOFF force field torsion potential.
- A new method,  $GetIterLimit$ , has been added that allows assessing the state of an  $OEOptimizerO$ .
- Two new methods,  $GetIterLimit$  and  $GetTolerance$ , have been added that allow assessing the state of an OEOptimizer1.
- Two new methods, Get IterLimit and Get Tolerance, have been added that allow assessing the state of an OEOptimizer2.

## 4.12.2 Major bug fixes

- A memory leak in *OEInterAdaptor* has been fixed.
- A memory leak in OEAM1 has been fixed.

## **4.12.3 Documentation changes**

- Theory documentation for SMIRNOFF has been added (see SMIRNOFF).
- A new example program was written that demonstrated calculating energy and optimizing a single ligand in vacuum.
- The following example programs have been corrected:
  - section\_mmff\_example
  - section\_mmff\_energy\_example
  - section\_mmff\_interactions\_example
  - section\_mmff\_complex\_example
  - section\_mmff\_amber\_example
  - section\_mmff\_subset\_example
  - section\_mmff\_tor\_example
  - section\_mmff\_amber\_quat\_example

# 4.13 OEFF TK 2.0.4

• Minor internal improvements have been made.

# 4.14 OEFF TK 2.0.3

# 4.14.1 New features

- A new OEMMFFSheffield class and a new OEMMFFSheffieldFFType namespace have been added to the force field suites for molecular interactions. This is a hybrid force field consisting of OEMMFF and OESheffield.
- A new OEMMFFSheffieldOptions class has been added to set all options of an OEMMFFSheffield object during its construction.
- A new OEGetMMFFSheffieldFFName function has been added to provide the force field name corresponding to a specific variation of a force field type.
- A new OEGetMMFFSheffieldFFType function has been added to provide a specific variation of the force field type corresponding to a force field name.
- A new OEIsValidMMFFSheffieldFF function has been added that can check if a type ID or name corresponds to a valid OEMMFFSheffield force field type.
- New OEForceField. GetTitle and OEForceField. SetTitle methods have been added to set and return the title of the force field.

# 4.14.2 Minor bug fixes

• Water is now treated as natural residue in the AMBER force field.

# **4.14.3 Documentation changes**

• A minor fix has been made in the example in the  $MMFF$  interactions of a single ligand section.

# 4.15 OEFF TK 2.0.2

• Minor internal improvements have been made.

# 4.16 OEFF TK 2.0.1

# 4.16.1 New features

- A set of classes that were previously derived from *OEMolFunc1* are now derived from *OEMolFunc2*. With this change, all of these classes now provide analytical Hessians and can be optimized with OENewtonOpt. The list of classes is as follows:
  - OEMolMMFF:: OEMMFFBend
  - OEMolMMFF:: OEMMFFStretch

- OEMolMMFF:: OEMMFFTorsion
- OEMolMMFF:: OEMMFFCoulomb
- OEMolMMFF:: OEMMFFOutOfPlane
- OEMMFFStretchBend
- OEMolMMFF:: OEMMFFVdw
- $-$  OESheffield
- A new class, OEGenericFF2, has been added that extends OEForceField to be an OEMolFunc2 and provide Hessians.
- Two of the OEForceField classes, OEMMFF and OEFF:: OEMMFFAmber, now derive from OEGenericFF2.
- **OEForceField**  $\bullet$  Two Ω£ the methods, OEMolPotential::OEForceField::Add and OEMolPotential::OEForceField::Remove, have been deprecated and replaced by more userfriendly methods in the derived classes OEGenericFF and OEGenericFF2.

The following table shows the older, deprecated functions and their replacements:

| Deprecated                                  | New                                                      |
|---------------------------------------------|----------------------------------------------------------|
| OEMolPotential::OEForceField::AddMolFunc    | <i>OEGenericFF.AddMolFunc</i><br><i>AddMolFunc</i>       |
| OEMolPotential::OEForceField::RemoveMolFunc | <i>OEGenericFF.RemoveMolFunc</i><br><i>RemoveMolFunc</i> |

- A new method, OEGenericFF. GetComponents, has been added that gives access to the function components of the force field.
- A new class, OEMolAdaptor2, has been added that extends the OEMolAdaptor to be an OEMolFunc2 and provide Hessians.
- The OESubsetAdaptor class now derives from OEMolAdaptor2.
- A new class, OENumericMolFunc2, has been added that can be used to convert any OEMolFunc1 into an OEMolFunc2 with numerical Hessians.
- A new class, OEScaledMolFunc, has been added that can be used to scale (up or down) any OEMolFunc1 or OEMolFunc2 derived classes.

## 4.16.2 Minor Bug Fixes

• The constructor for the OEMMFFCoulomb class previously had an unused OEFFParams parameter. A new overload without this parameter has been added, and the older constructor has been deprecated. For updated information, see Deprecated OEFF Classes.

# 4.17 OEFF TK 2.0.0

# 4.17.1 Licensing

• OEFF TK is available to anyone with an OESzybki TK license. Visit https://www.eyesopen.com/contact if you need an OESzybki TK license.

# 4.17.2 OEFF functionality

This is the first official release of **OEFF TK**. The underlying functionality was previously released in  $C++$  as part of the OESzybki TK advanced interface. This toolkit is currently available in C++ and Python. An overview of its capabilities is provided below.

**OEFF TK** provides access to powerful low-level functionality for advanced users to develop molecular modeling applications. With OEFF TK, users also have the ability to create variations of molecular interaction classes for energy evaluation and optimization, adding to the built-in interactions, if desired. OESzybki TK complements OEFF TK as the high-level API for molecular modeling functionalities.

# 4.17.3 Objective functions and molecular interactions

All molecular interactions are objective functions with additional API points for molecular definitions. A set of pure virtual classes that can be used to define new interactions are provided for both generic objective functions and molecule specific interaction functions. The following virtual base classes are available:

- $\bullet$  OEFunc0
- $\bullet$  OEFuncl
- $\bullet$  OEFunc2
- OEMolFunc
- OEMolFunc0
- OEMolFunc1
- OEMolFunc2

# 4.17.4 Force fields

Force fields and components of force fields are defined as molecule objective functions and are derived from the above-specified base classes. The following force fields and components are available:

- OEMMFF
- · OEMolMMFF:: OEMMFFBend
- · OEMolMMFF:: OEMMFFStretch
- OEMMFFStretchBend
- · OEMolMMFF:: OEMMFFOutOfPlane
- · OEMolMMFF:: OEMMFFTorsion
- · OEMOLMMFF:: OEMMFFVdw
- · OEMolMMFF:: OEMMFFInterVdw

- · OEMolMMFF:: OEMMFFInterVdwNN
- · OEMolMMFF:: OEMMFFCoulomb
- · OEMolMMFF:: OEMMFFInterCoulomb
- · OEFF:: OEMMFFAmber
- OEMMFFIEFF
- OESheffield

# 4.17.5 Optimizers

A powerful set of optimizers that can be used to optimize objective functions is now available:

- OEBFGSOpt
- OEConjGradOpt
- OEDFPOpt
- OEFletcherReevesOpt
- OENewtonOpt
- OERibierePolakOpt
- OESteepestDescentOpt

# 4.17.6 Adaptors

Adaptors that can be used to optimize molecule objective functions in transformed coordinate space are now available:

- OEInterAdaptor
- OEQuatAdaptor
- OESubsetAdaptor
- OETorAdaptor
- OETorQuatAdaptor

# 4.17.7 New features

- Two new intermolecular force fields, OEFF:: OEMMFFAmber and OEMMFFIEFF, have been added to the force field suites for molecular interactions. Both force fields use OEMMFF for intermolecular interactions and more accurate components for intermolecular interactions.
- A new class, OEFF:: OEMMFFAmberOptions, has been added that sets all options of the OEFF:: OEMMFFAmber object during its construction.
- A new class, OEMMFFIEFFOptions, has been added that sets all options of the OEMMFFIEFF object during its construction.
- A new class, OESheffieldOptions, has been added that sets all options of the OESheffield object during its construction. All OESheffield methods with similar names as their OESheffieldOptions counterparts are now deprecated.

The following table shows the older, deprecated functions and their new option replacements:

| Deprecated                                               | New option-based                                |
|----------------------------------------------------------|-------------------------------------------------|
| OESheff::OESheffieldOptions.SetA                         | OESheffieldOptions.SetA                         |
| OESheff::OESheffieldOptions.SetB                         | OESheffieldOptions.SetB                         |
| OESheff::OESheffieldOptions.SetSoluteDielectricConstant  | OESheffieldOptions.SetSoluteDielectricConstant  |
| OESheff::OESheffieldOptions.SetSolventDielectricConstant | OESheffieldOptions.SetSolventDielectricConstant |
| OESheff::OESheffieldOptions.GetA                         | OESheffieldOptions.GetA                         |
| OESheff::OESheffieldOptions.GetB                         | OESheffieldOptions.GetB                         |
| OESheff::OESheffieldOptions.GetSoluteDielectricConstant  | OESheffieldOptions.GetSoluteDielectricConstant  |
| OESheff::OESheffieldOptions.GetSolventDielectricConstant | OESheffieldOptions.GetSolventDielectricConstant |

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

# **CHAPTER**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

# **CHAPTER**

# **SEVEN**

# **CITATION**

# 7.1 Orion<sup>®</sup> Floes

To cite use of an Orion-based Floe package, please use the following:

```
OpenEye <package-name> <version-number>. OpenEye, Cadence Molecular Sciences, Santa
→Fe, NM. http://www.eyesopen.com.
```

#### For example:

```
OpenEye Classic Floes 0.11.2. OpenEye, Cadence Molecular Sciences, Santa Fe, NM.
\rightarrowhttp://www.eyesopen.com.
```

The version number for a Floe package is displayed on the first page of the package's release notes. For example: https://docs.eyesopen.com/floe/modules/classic-floes/docs/source/releasenotes.html.

# **7.2 Toolkits and Applications**

To cite OpenEye toolkits or applications used in your work, please use the following:

```
OpenEye Toolkits [or Applications] <version-number>. OpenEye, Cadence Molecular.
-Sciences, Santa Fe, NM. http://www.eyesopen.com.
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

# **7.3 OpenEye Web Services**

To cite use of the Macromolecular Data Service (MMDS) web service, please use the syntax:

Macromolecular Data Service <version-number>. OpenEye, Cadence Molecular Sciences, -Santa Fe, NM. http://www.eyesopen.com.

## For example:

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

# **CHAPTER**

# **EIGHT**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                                                           | License                                                            |
|-------------------------------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                                              | https:                                                             |
| absl-py                       | https://github.com/abseil/abseil-py                                                               | https:                                                             |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                                               | https:                                                             |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                                             | https:                                                             |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                                             | N/A                                                                |
| AmberUtils                    | http://ambermd.org                                                                                | N/A                                                                |
| ambit                         | https://github.com/khimaros/ambit                                                                 | https:                                                             |
| amqp                          | https://github.com/celery/py-amqp                                                                 | https:                                                             |
| anaconda-anon-usage           | Orion Floes                                                                                       | https:                                                             |
| angular                       | https://github.com/angular/angular.js                                                             | https:                                                             |
| angular-animate               | https://github.com/angular/angular.js                                                             | https:                                                             |
| angular-cache                 | https://github.com/jmdobry/angular-cache                                                          | https:                                                             |
| angular-cookies               | https://github.com/angular/angular.js                                                             | https:                                                             |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                                                  | https:                                                             |
| angular-mocks                 | https://github.com/angular/angular.js                                                             | https:                                                             |
| angular-resource              | https://github.com/angular/angular.js                                                             | https:                                                             |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                                                  | https:                                                             |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                                             | https:                                                             |
| angular-ui-router             | https://github.com/angular-ui/ui-router                                                           | https:                                                             |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                                                | https:                                                             |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                                                      | https:                                                             |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                                                          | https:                                                             |
| annotated-types               | https://github.com/annotated-types/annotated-types                                                | https:                                                             |
| anyio                         | https://github.com/agronholm/anyio                                                                | https:                                                             |
| appdirs                       | http://github.com/ActiveState/appdirs                                                             | http://                                                            |
| appengine                     | https://google.golang.org/appengine                                                               | https:                                                             |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                                                 | https:                                                             |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md                                        | https:                                                             |
| Name of Project               | Website                                                                                           | License                                                            |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                              | https://                                                           |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                                     | https://                                                           |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                                        | https://                                                           |
| ascii85                       | https://github.com/huandu/node-ascii85                                                            | https://                                                           |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                                    | https://                                                           |
| asgiref                       | https://github.com/django/asgiref/                                                                | https://                                                           |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                                               | https://                                                           |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render                             | https://                                                           |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers                                 | https://                                                           |
| assertions                    | https://github.com/smartystreets/assertions                                                       | https://                                                           |
| asttokens                     | https://github.com/gristlabs/asttokens                                                            | https://                                                           |
| astunparse                    | https://github.com/simonpercivall/astunparse                                                      | https://                                                           |
| async-lru                     | https://github.com/aio-libs/async-lru                                                             | https://                                                           |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                                         | https://                                                           |
| atk-1.0                       | https://docs.gtk.org/atk/                                                                         | https://                                                           |
| atomic                        | https://github.com/uber-go/atomic                                                                 | https://                                                           |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                                  | https://                                                           |
| attrs                         | https://www.attrs.org/                                                                            | https://                                                           |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                                                 | https://                                                           |
| Babel                         | https://github.com/python-babel/babel                                                             | https://                                                           |
| backcall                      | https://github.com/takluyver/backcall                                                             | https://                                                           |
| backports                     | https://github.com/brandon-rhodes/backports                                                       | https://                                                           |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                                           | https://                                                           |
| base62                        | https://github.com/kare/base62                                                                    | https://                                                           |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                                    | https://                                                           |
| billiard                      | https://github.com/celery/billiard                                                                | https://                                                           |
| biopython                     | https://biopython.org                                                                             | https://                                                           |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                                     | https://                                                           |
| bitset                        | https://github.com/willf/bitset                                                                   | https://                                                           |
| blas                          | https://www.netlib.org/blas/                                                                      | https://                                                           |
| bleach                        | https://github.com/mozilla/bleach                                                                 | https://                                                           |
| blessings                     | https://github.com/erikrose/blessings                                                             | https://                                                           |
| blinker                       | https://pythonhosted.org/blinker/                                                                 | https://                                                           |
| blosc                         | https://github.com/Blosc/python-blosc                                                             | https://                                                           |
| blosc2                        | https://github.com/Blosc/python-blosc2                                                            | https://                                                           |
| boltons                       | https://github.com/mahmoud/boltons                                                                | https://                                                           |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html                             | https://                                                           |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html                             | https://                                                           |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                                    | https://                                                           |
| boto3                         | https://github.com/boto/boto3                                                                     | https://                                                           |
| botocore                      | https://github.com/boto/botocore                                                                  | https://                                                           |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                                            | https://                                                           |
| Brotli                        | https://github.com/google/brotli                                                                  | https://                                                           |
| brotli-bin                    | https://github.com/google/brotli                                                                  | https://                                                           |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                              | https://                                                           |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                                        | https://                                                           |
| bson                          | http://github.com/py-bson/bson                                                                    | https://                                                           |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                                             | https://                                                           |
| bzip2                         | https://www.bzip.org                                                                              | https://                                                           |
| Name of Project               | Website                                                                                           | License                                                            |
| c-ares                        | https://github.com/c-ares/c-ares                                                                  | https://                                                           |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                                          | https://                                                           |
| cached-property               | https://github.com/pydanny/cached-property                                                        | https://                                                           |
| cachetools                    | https://github.com/tkem/cachetools/                                                               | https://                                                           |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                                         | https://                                                           |
| canvas                        | https://github.com/Automattic/node-canvas                                                         | https://                                                           |
| cctbx                         | https://github.com/cctbx/cctbx_project                                                            | https://                                                           |
| celery                        | https://github.com/celery/celery                                                                  | https://                                                           |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                                       | https://                                                           |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                                         | https://                                                           |
| cffi                          | https://github.com/python-cffi                                                                    | https://                                                           |
| cftime                        | https://pypi.org/project/cftime/                                                                  | https://                                                           |
| chardet                       | https://github.com/chardet/chardet                                                                | https://                                                           |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                                      | https://                                                           |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                                           | https://                                                           |
| click                         | https://palletsprojects.com/p/click/                                                              | https://                                                           |
| click-completion              | https://github.com/click-contrib/click-completion                                                 | https://                                                           |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                                 | https://                                                           |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                                    | https://                                                           |
| click-repl                    | https://github.com/untitaker/click-repl                                                           | https://                                                           |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                                          | https://                                                           |
| cmake                         | https://cmake.org/                                                                                | https://                                                           |
| colorama                      | https://github.com/tartley/colorama                                                               | https://                                                           |
| comm                          | https://github.com/ipython/comm                                                                   | https://                                                           |
| compose                       | https://github.com/docker/compose                                                                 | https://                                                           |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                                      | https://                                                           |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                                    | https://                                                           |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                                   | https://                                                           |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                                          | https://                                                           |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                                         | https://                                                           |
| confuse                       | https://github.com/beetbox/confuse                                                                | https://                                                           |
| contourpy                     | https://github.com/contourpy/contourpy                                                            | https://                                                           |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                                             | https://                                                           |
| cryptography                  | https://github.com/pyca/cryptography                                                              | https://                                                           |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                                              | https://                                                           |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                                         | https://                                                           |
| cupy-cuda113                  | https://cupy.dev/                                                                                 | https://                                                           |
| curl                          | https://curl.se/                                                                                  | https://                                                           |
| cycler                        | https://github.com/matplotlib/cycler                                                              | https://                                                           |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                                           | https://                                                           |
| Cython                        | https://cython.org                                                                                | https://                                                           |
| d3                            | https://github.com/mbostock/d3                                                                    | https://                                                           |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                                         | https://                                                           |
| ddsketch                      | http://github.com/datadog/sketches-py                                                             | https://                                                           |
| debugpy                       | https://aka.ms/debugpy                                                                            | https://                                                           |
| decimal                       | https://github.com/shopspring/decimal                                                             | https://                                                           |
| decorator                     | https://github.com/micheles/decorator                                                             | https://                                                           |
| deepdiff                      | https://github.com/seperman/deepdiff                                                              | https://                                                           |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                                           | https://                                                           |
| Name of Project               | Website                                                                                           | License                                                            |
| defusedxml                    | https://github.com/tiran/defusedxml                                                               | https:/                                                            |
| dill                          | https://github.com/uqfoundation/dill                                                              | https:/                                                            |
| distro                        | <b>Orion Floes</b>                                                                                | https:/                                                            |
| Django                        | https://www.djangoproject.com/                                                                    | https:/                                                            |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                                  | https:/                                                            |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                                 | https:/                                                            |
| django-csp                    | https://github.com/mozilla/django-csp                                                             | https:/                                                            |
| django-extensions             | https://github.com/django-extensions/django-extensions                                            | https:/                                                            |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                                        | https:/                                                            |
| django-redis                  | https://github.com/jazzband/django-redis                                                          | https:/                                                            |
| django-taggit                 | https://github.com/jazzband/django-taggit                                                         | https:/                                                            |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                                            | https:/                                                            |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                                            | https:/                                                            |
| djangorestframework           | https://www.django-rest-framework.org/                                                            | https:/                                                            |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                                    | https:/                                                            |
| dm-tree                       | https://github.com/deepmind/tree                                                                  | https:/                                                            |
| docker-py                     | https://github.com/docker/docker-py/                                                              | https:/                                                            |
| docopt                        | https://docopt.org                                                                                | https:/                                                            |
| docutils                      | https://docutils.sourceforge.io                                                                   | https:/                                                            |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                                       | https:/                                                            |
| editdistance                  | https://github.com/roy-ht/editdistance                                                            | https:/                                                            |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                                             | https:/                                                            |
| einops                        | https://github.com/arogozhnikov/einops                                                            | https:/                                                            |
| entrypoints                   | https://github.com/takluyver/entrypoints                                                          | https:/                                                            |
| errors                        | https://github.com/pkg/errors                                                                     | https:/                                                            |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                                            |                                                                    |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                                     | https:/                                                            |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                                       | https:/                                                            |
| executing                     | https://github.com/alexmojaki/executing                                                           | https:/                                                            |
| expat                         | https://libexpat.github.io                                                                        | https:/                                                            |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                                 | https:/                                                            |
| fastrlock                     | https://github.com/scoder/fastrlock                                                               | https:/                                                            |
| fftw                          | https://www.fftw.org                                                                              | comm                                                               |
| filebuffer                    | https://github.com/mattetti/filebuffer                                                            | https:/                                                            |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                                           | https:/                                                            |
| finufft                       | https://github.com/flatironinstitute/finufft                                                      | https:/                                                            |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                                       | https:/                                                            |
| flatbuffers                   | https://google.github.io/flatbuffers/                                                             | https:/                                                            |
| flit-core                     | https://github.com/pypa/flit                                                                      | https:/                                                            |
| <b>FLTK</b>                   | https://www.fltk.org/index.php                                                                    | https:/                                                            |
| fmt                           | https://fmt.dev/latest/index.html                                                                 | https:/                                                            |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                                       | https:/                                                            |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                                    | https:/                                                            |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                                     | https:/                                                            |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                                 | https:/                                                            |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                                          | https:/                                                            |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                                             | https:/                                                            |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                                           | https:/                                                            |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                               | https:/                                                            |
| Name of Project               | Website                                                                                           | License                                                            |
| fonttools                     | https://github.com/fonttools/fonttools                                                            | https:/                                                            |
| freetype                      | https://freetype.org                                                                              | https:/                                                            |
| fribidi                       | https://github.com/fribidi/fribidi                                                                | https:/                                                            |
| frozendict                    | Orion Floes                                                                                       | https:/                                                            |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                                            | https:/                                                            |
| fsmlite                       | https://github.com/tkem/fsmlite                                                                   | https:/                                                            |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                                         | https:/                                                            |
| funcy                         | https://github.com/Suor/funcy                                                                     | https:/                                                            |
| gast                          | https://github.com/serge-sans-paille/gast/                                                        | https:/                                                            |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                              | https:/                                                            |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                                           | https:/                                                            |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                                         | https:/                                                            |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                                           | https:/                                                            |
| genproto                      | https://google.golang.org/genproto/googleapis                                                     | https:/                                                            |
| geometric                     | https://openbase.com/python/geometric                                                             | https:/                                                            |
| giflib                        | https://giflib.sourceforge.net                                                                    | https:/                                                            |
| glib                          | https://docs.gtk.org/glib/                                                                        | https:/                                                            |
| <b>GLM</b> Library            | https://github.com/g-truc/glm                                                                     | https:/                                                            |
| gls                           | https://github.com/jtolds/gls                                                                     | https:/                                                            |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                                         | https:/                                                            |
| go-connections                | https://github.com/docker/go-connections                                                          | https:/                                                            |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                                          | https:/                                                            |
| go-getter                     | https://github.com/hashicorp/go-getter                                                            | https:/                                                            |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                                           | https:/                                                            |
| go-ini                        | https://github.com/go-ini/ini                                                                     | https:/                                                            |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                                           | https:/                                                            |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                                       | https:/                                                            |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                                         | https:/                                                            |
| go-ole                        | https://github.com/go-ole/go-ole                                                                  | https:/                                                            |
| go-pg                         | https://github.com/go-pg/pg                                                                       | https:/                                                            |
| go-redis                      | https://github.com/go-redis/redis/v8                                                              | https:/                                                            |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                                          | https:/                                                            |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                                          | https:/                                                            |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                                            | https:/                                                            |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                                                 | https:/                                                            |
| go-units                      | https://github.com/docker/go-units                                                                | https:/                                                            |
| go-version                    | https://github.com/hashicorp/go-version                                                           | https:/                                                            |
| go-zglob                      | https://github.com/mattn/go-zglob                                                                 | https:/                                                            |
| go.opencensus                 | https://go.opencensus.io                                                                          | https:/                                                            |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                              | https:/                                                            |
| goconvey                      | https://github.com/smartystreets/goconvey                                                         | https:/                                                            |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                                     | https:/                                                            |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                                     | https:/                                                            |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                                 | https:/                                                            |
| google-cloud-go               | https://cloud.google.com/go                                                                       | https:/                                                            |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                               | https:/                                                            |
| google-pasta                  | https://github.com/google/pasta                                                                   | https:/                                                            |
| google.golang.org/api         | https://google.golang.org/api                                                                     | https:/                                                            |
| gopsutil                      | https://github.com/shirou/gopsutil                                                                | https:/                                                            |
| Name of Project               | Website                                                                                           | License                                                            |
| gorilla websocket             | https://github.com/gorilla/websocket                                                              | https://github.com/gorilla/websocket                               |
| graphite2                     | https://github.com/silnrsi/graphite                                                               | https://github.com/silnrsi/graphite                                |
| graphviz                      | https://graphviz.org/                                                                             | https://graphviz.org/                                              |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                                        | https://greenlet.readthedocs.io/en/latest/                         |
| groupcache                    | https://github.com/golang/groupcache                                                              | https://github.com/golang/groupcache                               |
| grpc                          | https://google.golang.org/grpc                                                                    | https://google.golang.org/grpc                                     |
| grpc-cpp                      | https://github.com/grpc/grpc                                                                      | https://github.com/grpc/grpc                                       |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                                 | https://github.com/grpc/grpc.io/blob/main/LICENSE                  |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                                | https://gitlab.gnome.org/GNOME/gtk                                 |
| gts                           | https://sourceforge.net/projects/gts/                                                             | https://sourceforge.net/projects/gts/                              |
| h5py                          | https://www.h5py.org                                                                              | https://www.h5py.org                                               |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                              | https://github.com/harfbuzz/harfbuzz                               |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                                         | https://hdbscan.readthedocs.io/en/latest/                          |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                                          | https://www.hdfgroup.org/solutions/hdf4/                           |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                                          | https://www.hdfgroup.org/solutions/hdf5/                           |
| he                            | https://github.com/mathiasbynens/he                                                               | https://github.com/mathiasbynens/he                                |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                                    | https://github.com/webpack-contrib/html-loader                     |
| html5lib                      | https://github.com/html5lib/html5lib-python                                                       | https://github.com/html5lib/html5lib-python                        |
| htslib                        | https://www.htslib.org                                                                            | https://www.htslib.org                                             |
| humanize                      | https://github.com/jmoiron/humanize                                                               | https://github.com/jmoiron/humanize                                |
| icu                           | https://github.com/unicode-org/icu                                                                | https://github.com/unicode-org/icu                                 |
| idna                          | https://github.com/kjd/idna                                                                       | https://github.com/kjd/idna                                        |
| imageio                       | https://github.com/imageio/imageio                                                                | https://github.com/imageio/imageio                                 |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                                         | https://github.com/shibukawa/imagesize_py                          |
| ImmuneBuilder                 | https://github.com/oxpig/ImmuneBuilder/tree/main                                                  | https://github.com/oxpig/ImmuneBuilder/tree/main                   |
| importlib-metadata            | https://github.com/python/importlib_metadata                                                      | https://github.com/python/importlib_metadata                       |
| importlib_resources           | https://github.com/python/importlib_resources                                                     | https://github.com/python/importlib_resources                      |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                                    | https://iupac.org/who-we-are/divisions/division-details/inchi/     |
| inflection                    | https://github.com/jinzhu/inflection                                                              | https://github.com/jinzhu/inflection                               |
| ini.v1                        | https://gopkg.in/ini.v1                                                                           | https://gopkg.in/ini.v1                                            |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                                           | https://github.com/pytest-dev/iniconfig                            |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                                       | https://github.com/dnozay/innersvg-polyfill                        |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                                          | https://github.com/hermitcore/libomp_oss                           |
| ipykernel                     | https://ipython.org                                                                               | https://ipython.org                                                |
| ipython                       | https://ipython.org                                                                               | https://ipython.org                                                |
| ipython-genutils              | http://ipython.org                                                                                | http://ipython.org                                                 |
| ipywidgets                    | http://jupyter.org                                                                                | http://jupyter.org                                                 |
| isodate                       | https://github.com/gweis/isodate/                                                                 | https://github.com/gweis/isodate/                                  |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                                       | https://palletsprojects.com/p/itsdangerous/                        |
| jax                           | https://github.com/google/jax                                                                     | https://github.com/google/jax                                      |
| jaxlib                        | https://github.com/google/jax                                                                     | https://github.com/google/jax                                      |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                                            | https://jedi.readthedocs.io/en/latest/                             |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                              | https://palletsprojects.com/p/jinja/                               |
| jmespath                      | https://github.com/jmespath/jmespath.py                                                           | https://github.com/jmespath/jmespath.py                            |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                                          | https://joblib.readthedocs.io/en/latest/                           |
| jpeg                          | https://www.ijg.org                                                                               | https://www.ijg.org                                                |
| json5                         | https://github.com/dpranke/pyjson5                                                                | https://github.com/dpranke/pyjson5                                 |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                                       | https://github.com/dmkoch/django-jsonfield/                        |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                                  | https://github.com/stefankoegl/python-json-patch                   |
| Name of Project               | Website                                                                                           | License                                                            |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                                          | https:                                                             |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                                | https:                                                             |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                                   | https:                                                             |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst               | https:                                                             |
| jstat                         | https://github.com/jstat/jstat                                                                    | https:                                                             |
| jupyter-client                | https://jupyter.org                                                                               | https:                                                             |
| jupyter-core                  | https://jupyter.org                                                                               | https:                                                             |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                                         | https:                                                             |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                                     | https:                                                             |
| jupyter-server                | http://jupyter.org                                                                                | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                                          | https:                                                             |
| jupyterlab-pygments           | http://jupyter.org                                                                                | https:/                                                            |
| jupyterlab-widgets            | http://jupyter.org                                                                                | https:                                                             |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                                   | https:                                                             |
| jupyter_client                | http://jupyter.org                                                                                | https:                                                             |
| jupyter_core                  | http://jupyter.org                                                                                | https:                                                             |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                                  | https:                                                             |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                                        | https:                                                             |
| kaleido                       | https://github.com/plotly/Kaleido                                                                 | https:                                                             |
| keras                         | https://github.com/keras-team/keras                                                               | https:                                                             |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                                 | https:                                                             |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                                         | https:                                                             |
| keyring                       | https://github.com/jaraco/keyring                                                                 | https:                                                             |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                                    | https:                                                             |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                                      | https:                                                             |
| kombu                         | https://kombu.readthedocs.io                                                                      | https:                                                             |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                                     | https:/                                                            |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                                          | https:/                                                            |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                                  | https:/                                                            |
| lcms2                         | https://www.littlecms.com                                                                         | https:/                                                            |
| lerc                          | https://github.com/Esri/lerc                                                                      | https:                                                             |
| libarchive                    | http://www.libarchive.org                                                                         | https:                                                             |
| libblas                       | https://www.netlib.org/blas/                                                                      | https:                                                             |
| libbrotlicommon               | https://github.com/google/brotli                                                                  | https:                                                             |
| libbrotlidec                  | https://github.com/google/brotli                                                                  | https:/                                                            |
| libbrotlienc                  | https://github.com/google/brotli                                                                  | https:/                                                            |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                                         | N/A                                                                |
| libclang                      | Orion Floes                                                                                       | https:                                                             |
| libcurl                       | https://curl.se/libcurl/                                                                          | https:                                                             |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                                             | https:                                                             |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html                        | https:                                                             |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                                            | https:                                                             |
| libedit                       | https://thrysoee.dk/editline/                                                                     | http://                                                            |
| libev                         | https://software.schmorp.de/pkg/libev.html                                                        |                                                                    |
| libffi                        | https://github.com/libffi/libffi                                                                  | https:<br>https:                                                   |
| libgcrypt                     | https://gnupg.org/software/index.html                                                             | https:                                                             |
| libgd                         | https://libgd.github.io                                                                           | https:/                                                            |
| libglib                       | https://github.com/PolMine/libglib                                                                |                                                                    |
| libiconv                      | https://www.gnu.org/software/libiconv/                                                            | https:<br>https:                                                   |
| Name of Project               | Website                                                                                           | License                                                            |
| libint                        | https://tinyurl.com/yvw97wbw                                                                      | https:/                                                            |
| liblapack                     | http://www.netlib.org/lapack/                                                                     | https:/                                                            |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                                       | https:/                                                            |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23                   | https:/                                                            |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                              | https:/                                                            |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                                     | https:/                                                            |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                                | https:/                                                            |
| libopenblas                   | https://www.openblas.net/                                                                         | https:/                                                            |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                                        | https:/                                                            |
| libpq                         | https://www.postgresql.org/                                                                       | https:/                                                            |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                                            | https:/                                                            |
| libsolv                       | https://github.com/openSUSE/libsolv                                                               | https:/                                                            |
| libssh2                       | https://github.com/libssh2/libssh2                                                                | https:/                                                            |
| libtiff                       | https://www.libtiff.org/                                                                          | https:/                                                            |
| libtrust                      | https://github.com/docker/libtrust                                                                | https:/                                                            |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                                         | https:/                                                            |
| libuv                         | https://github.com/libuv/libuv                                                                    | https:/                                                            |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                                    | https:/                                                            |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                                    | https:/                                                            |
| libxc                         | https://www.tddft.org/programs/libxc/                                                             | https:/                                                            |
| libxcb                        | https://xcb.freedesktop.org                                                                       | https:/                                                            |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                                             | https:/                                                            |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                                  | https:/                                                            |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                               | https:/                                                            |
| libzlib                       | https://zlib.net                                                                                  | https:/                                                            |
| lime                          | https://github.com/marcotcr/lime                                                                  | https:/                                                            |
| lit                           | http://llvm.org                                                                                   | https:/                                                            |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                                             | https:/                                                            |
| llvmlite                      | http://llvmlite.readthedocs.io                                                                    | https:/                                                            |
| loader-utils                  | https://github.com/webpack/loader-utils                                                           | https:/                                                            |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                                       | https:/                                                            |
| logrus                        | https://github.com/sirupsen/logrus                                                                | https:/                                                            |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                                | https:/                                                            |
| lxml                          | https://lxml.de                                                                                   | https:/                                                            |
| lz4-c                         | https://www.lz4.org/                                                                              | https:/                                                            |
| markdown                      | https://github.com/evilstreak/markdown-js                                                         | https:/                                                            |
| markdown-it-py                | Orion Floes                                                                                       | https:/                                                            |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                                         | https:/                                                            |
| matplotlib                    | https://matplotlib.org                                                                            | https:/                                                            |
| matplotlib-base               | https://matplotlib.org                                                                            | https:/                                                            |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                                      | https:/                                                            |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                                          | https:/                                                            |
| mdtraj                        | https://www.mdtraj.org/                                                                           | https:/                                                            |
| mdurl                         | Orion Floes                                                                                       | https:/                                                            |
| menuinst                      | Orion Floes                                                                                       | https:/                                                            |
| mergo                         | https://github.com/imdario/mergo                                                                  | https:/                                                            |
| mistune                       | https://github.com/lepture/mistune                                                                | https:/                                                            |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                                        | https:/                                                            |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                                            | https:/                                                            |
| Name of Project               | Website                                                                                           | License                                                            |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                                         | https:/                                                            |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                                        | https:/                                                            |
| ml-dtypes                     | <b>Orion Floes</b>                                                                                | https:/                                                            |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                                        | https:/                                                            |
| moment                        | https://github.com/moment/moment                                                                  | https:/                                                            |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                                   | https:/                                                            |
| more-itertools                | https://github.com/more-itertools/more-itertools                                                  | https:/                                                            |
| mpiplus                       | https://github.com/choderalab/mpiplus                                                             | https:/                                                            |
| mpmath                        | http://mpmath.org/                                                                                | https:/                                                            |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                                  | https:/                                                            |
| msgpack                       | https://msgpack.org/                                                                              | https:/                                                            |
| multidict                     | https://github.com/aio-libs/multidict                                                             | https:/                                                            |
| multierr                      | https://go.uber.org/multierr                                                                      | https:/                                                            |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                                      | https:/                                                            |
| munkres                       | https://software.clapper.org/munkres/                                                             | https:/                                                            |
| myesui uuid                   | https://github.com/myesui/uuid                                                                    | https:/                                                            |
| namex                         | <b>Orion Floes</b>                                                                                | https:/                                                            |
| nbclassic                     | http://jupyter.org                                                                                | https:/                                                            |
| nbclient                      | https://jupyter.org                                                                               | https:/                                                            |
| nbconvert                     | https://jupyter.org                                                                               | https:/                                                            |
| nbformat                      | http://jupyter.org                                                                                | https:/                                                            |
| ncurses                       | https://invisible-island.net/ncurses/                                                             |                                                                    |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                                           | https:/                                                            |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                                     | https:/                                                            |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                                          | https:/                                                            |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                                          | https:/                                                            |
| networkx                      | https://networkx.org                                                                              | https:/                                                            |
| nfpm                          | https://github.com/goreleaser/nfpm                                                                | https:/                                                            |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                                           | https:/                                                            |
| ng-toast                      | https://github.com/tameraydin/ngToast                                                             | https:/                                                            |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                                     | https:/                                                            |
| ngVue                         | https://github.com/ngVue/ngVue                                                                    | https:/                                                            |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                                    | https:/                                                            |
| nodejs                        | https://nodejs.org/en/                                                                            | https:/                                                            |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                                    | https:/                                                            |
| notebook                      | http://jupyter.org                                                                                | https:/                                                            |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                                          | https:/                                                            |
| notebook_shim                 | http://jupyter.org                                                                                | https:/                                                            |
| numba                         | https://numba.pydata.org                                                                          | https:/                                                            |
| numcpus                       | https://github.com/tklauser/numcpus                                                               | https:/                                                            |
| numexpr                       | https://github.com/pydata/numexpr                                                                 | https:/                                                            |
| numpy                         | https://numpy.org                                                                                 | https:/                                                            |
| numpy-base                    | https://numpy.org                                                                                 | https:/                                                            |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                              | https:/                                                            |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                                            | https:/                                                            |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                                            | https:/                                                            |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                                            | https:/                                                            |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                                            | https:/                                                            |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                                            | https:/                                                            |
| Name of Project               | Website                                                                                           | License                                                            |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                                            | https://developer.nvidia.com/cuda-zone                             |
| Oat++                         | https://oatpp.io/                                                                                 | https://oatpp.io/                                                  |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                              | https://github.com/oauthlib/oauthlib                               |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                                | https://github.com/OCL-dev/ocl-icd                                 |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                                           | https://github.com/conda-forge/ocl-icd-system-feedstock            |
| olefile                       | https://www.decalage.info/python/olefileio                                                        | https://www.decalage.info/python/olefileio                         |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                                             | https://github.com/HeliXonProtein/OmegaFold/tree/main              |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                                      | https://omnicanvas.readthedocs.io/en/latest/                       |
| OpenFF                        | https://openforcefield.org/                                                                       | https://openforcefield.org/                                        |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                                           | https://github.com/openforcefield/openff-amber-ff-ports            |
| openff-forcefields            | https://openforcefield.org                                                                        | https://openforcefield.org                                         |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                              | https://github.com/openforcefield/openff-interchange               |
| openff-models                 | https://github.com/openforcefield/openff-models                                                   | https://github.com/openforcefield/openff-models                    |
| openff-toolkit                | https://openforcefield.org                                                                        | https://openforcefield.org                                         |
| openff-toolkit-base           | https://openforcefield.org                                                                        | https://openforcefield.org                                         |
| openff-units                  | https://github.com/openforcefield/openff-units                                                    | https://github.com/openforcefield/openff-units                     |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                                | https://github.com/openforcefield/openff-utilities                 |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                                             | https://github.com/uclouvain/openjpeg                              |
| openldap                      | https://www.openldap.org/software/repo.html                                                       | https://www.openldap.org/software/repo.html                        |
| OpenMM                        | https://openmm.org                                                                                | https://openmm.org                                                 |
| openmmtools                   | https://github.com/choderalab/openmmtools                                                         | https://github.com/choderalab/openmmtools                          |
| openmoltools                  | https://github.com/choderalab/openmoltools                                                        | https://github.com/choderalab/openmoltools                         |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                                        | https://openpyxl.readthedocs.io/en/stable/                         |
| openssl                       | https://www.openssl.org                                                                           | https://www.openssl.org                                            |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                                            | https://github.com/dgasmith/opt_einsum                             |
| OptKing                       | https://github.com/psi-rking/optking                                                              | https://github.com/psi-rking/optking                               |
| oscrypto                      | https://github.com/wbond/oscrypto                                                                 | https://github.com/wbond/oscrypto                                  |
| overrides                     | https://github.com/mkorpela/overrides                                                             | https://github.com/mkorpela/overrides                              |
| packaging                     | https://github.com/pypa/packaging                                                                 | https://github.com/pypa/packaging                                  |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                                             | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml              |
| pandas                        | https://pandas.pydata.org                                                                         | https://pandas.pydata.org                                          |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                               | http://github.com/jgm/pandocfilters                                |
| Name of Project               | Website                                                                                           | J)<br>Licen                                                        |
|                               | https://github.com/MDAnalysis/panedr                                                              |                                                                    |
| panedr                        | https://pango.gnome.org                                                                           | https:/                                                            |
| pango<br>ParmEd               | https://parmed.github.io/ParmEd/html/index.html                                                   | https:/                                                            |
|                               |                                                                                                   | https:/                                                            |
| parser                        | https://github.com/typescript-eslint/typescript-eslint<br>https://parso.readthedocs.io/en/latest/ | https:/                                                            |
| parso                         |                                                                                                   | https:/                                                            |
| pathos                        | https://github.com/uqfoundation/pathos                                                            | https:/                                                            |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                                           | https:/                                                            |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                                | https:/                                                            |
| pbr                           | https://docs.openstack.org/pbr/latest/                                                            | https:/                                                            |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                                       | https:/                                                            |
| pcre                          | https://www.pcre.org                                                                              | https:/                                                            |
| pcre2                         | https://www.pcre.org                                                                              | https:/                                                            |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                                             | https:/                                                            |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                                | https:/                                                            |
| pexpect                       | https://pexpect.readthedocs.io/                                                                   | https:/                                                            |
| pgconn                        | https://github.com/jackc/pgconn                                                                   | https:/                                                            |
| pgio                          | https://github.com/jackc/pgio                                                                     | https:/                                                            |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                               | https:/                                                            |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                              | https:/                                                            |
| pgtype                        | https://github.com/jackc/pgtype                                                                   | https:/                                                            |
| pgx                           | https://github.com/jackc/pgx/v4                                                                   | https:/                                                            |
| phonopy                       | https://github.com/phonopy/phono3py                                                               | https:/                                                            |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                                        | https:/                                                            |
| Pillow                        | https://python-pillow.org                                                                         | https:/                                                            |
| Pint                          | https://pint.readthedocs.io/en/stable/                                                            | https:/                                                            |
| pip                           | https://pip.pypa.io/                                                                              | https:/                                                            |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                                          | https:/                                                            |
| pixman                        | https://pixman.org                                                                                | https:/                                                            |
| pkginfo                       | https://launchpad.net/pkginfo                                                                     | https:/                                                            |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                                      | https:/                                                            |
| plotly                        | https://plotly.com/python/                                                                        | https:/                                                            |
| plotly-orca                   | https://github.com/plotly/orca                                                                    | https:/                                                            |
| plotly.js                     | https://github.com/plotly/plotly.js                                                               | https:/                                                            |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                                | https:/                                                            |
| pooch                         | https://github.com/fatiando/pooch                                                                 | https:/                                                            |
| pox                           | https://github.com/uqfoundation/pox                                                               | https:/                                                            |
| ppft                          | https://github.com/uqfoundation/ppft                                                              | https:/                                                            |
| pq                            | https://github.com/lib/pq                                                                         | https:/                                                            |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                                     | https:/                                                            |
| prometheus-client             | https://github.com/prometheus/client_python                                                       | https:/                                                            |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                                           | https:/                                                            |
| protobuf                      | https://google.golang.org/protobuf                                                                | https:/                                                            |
| psi4                          | https://psicode.org                                                                               | https:/                                                            |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                                          | https:/                                                            |
| psycopg2                      | https://psycopg.org/                                                                              | https:/                                                            |
| PTable                        | https://github.com/kxxoling/PTable                                                                | https:/                                                            |
|                               | https://xcb.freedesktop.org                                                                       |                                                                    |
| pthread-stubs                 | https://ptyprocess.readthedocs.io/en/latest/                                                      | https:/                                                            |
| ptyprocess<br>pure-eval       | http://github.com/alexmojaki/pure_eval                                                            | https:/                                                            |
|                               |                                                                                                   | http://                                                            |
|                               |                                                                                                   | Ъ                                                                  |
| Name of Project               | Website                                                                                           | Licen                                                              |
| py                            | https://py.readthedocs.io/en/latest/                                                              | https:/                                                            |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                                           | https:/                                                            |
| pyasn1                        | https://github.com/etingof/pyasn1                                                                 | https:/                                                            |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                                         | https:/                                                            |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                                | https:/                                                            |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                               | https:/                                                            |
| pycosat                       | https://github.com/conda/pycosat                                                                  | https:/                                                            |
| pycparser                     | https://github.com/eliben/pycparser                                                               | https:/                                                            |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                               | https:/                                                            |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                                         | https:/                                                            |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                              | https:/                                                            |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                              | https:/                                                            |
| Pygments                      | https://pygments.org                                                                              | https:/                                                            |
| pygraphviz                    | https://pygraphviz.github.io                                                                      | https:/                                                            |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                                          | https:/                                                            |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                                      | https:/                                                            |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                                | https:/                                                            |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                                 | https:/                                                            |
| pymbar                        | https://pymbar.org                                                                                | https:/                                                            |
| pyOpenSSL                     | https://pyopenssl.org/                                                                            | https:/                                                            |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                                  | https:/                                                            |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                                  | https:/                                                            |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                               | https:/                                                            |
| pysam                         | https://github.com/pysam-developers/pysam                                                         | https:/                                                            |
| PySocks                       | https://github.com/Anorov/PySocks                                                                 | https:/                                                            |
| pytables                      | https://www.pytables.org                                                                          | https:/                                                            |
| python                        | https://www.python.org/                                                                           | https:/                                                            |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                                        | https:/                                                            |
| python-constraint             | https://github.com/python-constraint/python-constraint                                            | https:/                                                            |
| python-dateutil               | https://dateutil.readthedocs.io                                                                   | https:/                                                            |
| python-json-logger            | http://github.com/madzak/python-json-logger                                                       | https:/                                                            |
| python-Idap                   | https://www.python-ldap.org/                                                                      | https:/                                                            |
| python3-saml                  | https://github.com/onelogin/python3-saml                                                          | https:/                                                            |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                               | https:/                                                            |
| pytz                          | https://pythonhosted.org/pytz                                                                     | https:/                                                            |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                                 | https:/                                                            |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                                | https:/                                                            |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                               | https:/                                                            |
| pyyml                         | No longer available                                                                               | No lor                                                             |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                                           | https:/                                                            |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                                             | https:/                                                            |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                                | https:/                                                            |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                                      | https:/                                                            |
| ramda                         | https://github.com/ramda/ramda                                                                    | https:/                                                            |
| rapidjson                     | https://rapidjson.org/                                                                            | https:/                                                            |
| rdkit                         | https://www.rdkit.org                                                                             | https:/                                                            |
| re2                           | https://github.com/google/re2                                                                     |                                                                    |
| readme-renderer               | https://github.com/pypa/readme_renderer                                                           | https:/                                                            |
|                               |                                                                                                   | https:/                                                            |
| redis-py                      | https://github.com/andymccurdy/redis-py                                                           | https:/                                                            |
| Name of Project               | Website                                                                                           | License                                                            |
| referencing                   | https://github.com/python-jsonschema/referencing                                                  | https:/                                                            |
| regex                         | https://github.com/mrabarnett/mrab-regex                                                          | https:/                                                            |
| reportlab                     | https://www.reportlab.com                                                                         | https:/                                                            |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                                             | https:/                                                            |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                                             | https:/                                                            |
| requests                      | https://requests.readthedocs.io                                                                   | https:/                                                            |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                                     | https:/                                                            |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                                  | https:/                                                            |
| resumable                     | https://github.com/stevvooe/resumable                                                             | https:/                                                            |
| retrying                      | https://github.com/rholder/retrying                                                               | https:/                                                            |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                                     | https:/                                                            |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                                         | https:/                                                            |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                                     | https:/                                                            |
| rich                          | Orion Floes                                                                                       | https:/                                                            |
| rpds-py                       | https://github.com/crate-py/rpds                                                                  | https:/                                                            |
| rpmpack                       | https://github.com/google/rpmpack                                                                 | https:/                                                            |
| rsa                           | https://stuvel.eu/rsa                                                                             | https:/                                                            |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                                       | https:/                                                            |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                                  | https:/                                                            |
| s3transfer                    | https://github.com/boto/s3transfer                                                                | https:/                                                            |
| sasl                          | https://mellium.im/sasl                                                                           | https:/                                                            |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                                         | https:/                                                            |
| scikit-image                  | https://scikit-image.org                                                                          | https:/                                                            |
| scikit-learn                  | https://scikit-learn.org/stable/                                                                  | https:/                                                            |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                                        | https:/                                                            |
| scipy                         | https://scipy.org                                                                                 | https:/                                                            |
| seaborn                       | https://seaborn.pydata.org                                                                        | https:/                                                            |
| seaborn-base                  | https://seaborn.pydata.org                                                                        | https:/                                                            |
| semver                        | https://github.com/Masterminds/semver/v3                                                          | https:/                                                            |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                                           | https:/                                                            |
| setuptools                    | https://github.com/pypa/setuptools                                                                | https:/                                                            |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                                           | https:/                                                            |
| sh                            | https://github.com/amoffat/sh                                                                     | https:/                                                            |
| shellingham                   | https://github.com/sarugaku/shellingham                                                           | https:/                                                            |
| simint                        | https://www.bennyp.org/research/simint/                                                           | https:/                                                            |
| six                           | https://github.com/benjaminp/six                                                                  | https:/                                                            |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                                | https:/                                                            |
| snappy                        | https://github.com/google/snappy                                                                  | https:/                                                            |
| sniffio                       | https://github.com/python-trio/sniffio                                                            | https:/                                                            |
| snowballstemmer               | https://github.com/snowballstem/snowball                                                          | https:/                                                            |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                                         | https:/                                                            |
| spglib                        | Orion Floes                                                                                       | https:/                                                            |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                              | https:/                                                            |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                                             | https:/                                                            |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                               | https:/                                                            |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                              | https:/                                                            |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                                | https:/                                                            |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                                | https:/                                                            |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                                       | https:/                                                            |
|                               |                                                                                                   | Т                                                                  |
| Name of Project               | Website                                                                                           | Licen                                                              |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                                        | https:/                                                            |
| sqlite                        | https://sqlite.org/index.html                                                                     | https:/                                                            |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                                          | https:/                                                            |
| stack-data                    | http://github.com/alexmojaki/stack_data                                                           | https:/                                                            |
| starfile                      | https://github.com/alisterburt/starfile                                                           | https:/                                                            |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                                        | https:/                                                            |
| structlog                     | https://www.structlog.org/                                                                        | https:/                                                            |
| svglib                        | https://github.com/deeplook/svglib                                                                | https:/                                                            |
| sympy                         | https://sympy.org                                                                                 | https:/                                                            |
| tables                        | https://www.pytables.org/                                                                         | https:/                                                            |
| tabulate                      | https://github.com/astanin/python-tabulate                                                        | https:/                                                            |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                              | https:/                                                            |
| tenacity                      | https://github.com/jd/tenacity                                                                    | https:/                                                            |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                                         | https:/                                                            |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                                         | https:/                                                            |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                                         | https:/                                                            |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                                          | https:/                                                            |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                                           | https:/                                                            |
| tensorflow-io-gcs-filesystem  | <b>Orion Floes</b>                                                                                | https:/                                                            |
| tensorflow-probability        | https://github.com/tensorflow/probability                                                         | https:/                                                            |
| termcolor                     | https://github.com/hugovk/termcolor                                                               | https:/                                                            |
| terminado                     | https://github.com/jupyter/terminado                                                              | https:/                                                            |
| testpath                      | https://github.com/jupyter/testpath                                                               | https:/                                                            |
| textangular                   | https://github.com/fraywing/textAngular                                                           | https:/                                                            |
| tf_keras                      | <b>Orion Floes</b>                                                                                | https:/                                                            |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                                           | https:/                                                            |
| three                         | https://github.com/mrdoob/three.js                                                                | https:/                                                            |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                              | https:/                                                            |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                                | https:/                                                            |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                                           | https:/                                                            |
| tk                            | https://www.tcl.tk/                                                                               | https:/                                                            |
| toml                          | https://github.com/toml-lang/toml                                                                 | https:/                                                            |
| tomli                         | https://github.com/hukkin/tomli                                                                   | https:/                                                            |
| toolz                         | https://github.com/pytoolz/toolz                                                                  | https:/                                                            |
| torch                         | https://pytorch.org/                                                                              | https:/                                                            |
| tornado                       | https://www.tornadoweb.org                                                                        | https:/                                                            |
| tqdm                          | https://github.com/tqdm/tqdm                                                                      | https:/                                                            |
| tracy                         | https://github.com/gear-genomics/tracy                                                            | https:/                                                            |
| traitlets                     | https://github.com/ipython/traitlets                                                              | https:/                                                            |
| triton                        | https://github.com/openai/triton/                                                                 | https:/                                                            |
| truststore                    | <b>Orion Floes</b>                                                                                | https:/                                                            |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                                             | https:/                                                            |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                                           |                                                                    |
|                               | https://github.com/pypa/twine                                                                     | https:/                                                            |
| twine                         |                                                                                                   | https:/                                                            |
| twinj uuid                    | https://github.com/twinj/uuid                                                                     | https:/                                                            |
| types                         | https://github.com/babel/babel                                                                    | https:/                                                            |
| typescript                    | https://github.com/Microsoft/TypeScript                                                           | https:/                                                            |
| typing_extensions             | https://github.com/python/typing                                                                  | https:/                                                            |
| tzdata                        | https://github.com/python/tzdata                                                                  | https:/                                                            |
| Name of Project               | Website                                                                                           | License                                                            |
| tzlocal                       | https://github.com/regebro/tzlocal                                                                | https://                                                           |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                                           | https://                                                           |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                                         | https://                                                           |
| uritools                      | https://github.com/tkem/uritools/                                                                 | https://                                                           |
| urllib3                       | https://urllib3.readthedocs.io/                                                                   | https://                                                           |
| vine                          | https://github.com/celery/vine                                                                    | https://                                                           |
| vue                           | https://github.com/vuejs/vue                                                                      | https://                                                           |
| wcwidth                       | https://github.com/jquast/wcwidth                                                                 | https://                                                           |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                                  | https://                                                           |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                                          | https://                                                           |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                                           | https://                                                           |
| westpa                        | Orion Floes                                                                                       | https://                                                           |
| wheel                         | https://github.com/pypa/wheel                                                                     | https://                                                           |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                              | https://                                                           |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                                          | https://                                                           |
| wsutil                        | https://github.com/yhat/wsutil                                                                    | https://                                                           |
| x/lint                        | https://golang.org/x/lint                                                                         | https://                                                           |
| x/mod                         | https://golang.org/x/mod/semver                                                                   | https://                                                           |
| x/net                         | https://golang.org/x/net                                                                          | https://                                                           |
| x/oauth2                      | https://golang.org/x/oauth2                                                                       | https://                                                           |
| x/sys                         | https://golang.org/x/sys                                                                          | https://                                                           |
| x/text                        | https://golang.org/x/text                                                                         | https://                                                           |
| x/tools                       | https://golang.org/x/tools                                                                        | https://                                                           |
| x/xerrors                     | https://golang.org/x/xerrors                                                                      | https://                                                           |
| xhtml2pdf                     | https://github.com/xhtml2pdf/xhtml2pdf                                                            | https://                                                           |
| xlrd                          | https://github.com/python-excel/xlrd                                                              | https://                                                           |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                                          | https://                                                           |
| xmltodict                     | https://github.com/martinblech/xmltodict                                                          | https://                                                           |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                                 | https://                                                           |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                                    | https://                                                           |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                                     | https://                                                           |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                                    | https://                                                           |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                                    | https://                                                           |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                                  | https://                                                           |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                                   | https://                                                           |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                                | https://                                                           |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                                     | https://                                                           |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                                             | https://                                                           |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                               | https://                                                           |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                                  | https://                                                           |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                              | https://                                                           |
| xz                            | https://github.com/ulikunitz/xz                                                                   | https://                                                           |
| yaml                          | https://pyyaml.org/                                                                               | https://                                                           |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                                | https://                                                           |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                                          | https://                                                           |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                                          | https://                                                           |
| yarl                          | https://github.com/aio-libs/yarl/                                                                 | https://                                                           |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                                 | https://                                                           |
| yfiles                        | https://www.yworks.com/products/yfiles                                                            | Commercial                                                         |
| Name of Project               | Website                                                                                           | License                                                            |
| yml                           | https://pypi.org/project/yml/                                                                     | N/A                                                                |
| zap                           | https://go.uber.org/zap                                                                           | https:/                                                            |
| zipp                          | https://github.com/jaraco/zipp                                                                    | https:/                                                            |
| zlib                          | https://zlib.net/                                                                                 | https:/                                                            |
| zstandard                     | https://github.com/indygreg/python-zstandard                                                      | https:/                                                            |
| zstd                          | https://facebook.github.io/zstd/                                                                  | https:/                                                            |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                                            | https:/                                                            |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                                            | https:/                                                            |

# **8.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses GNU Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

# **8.1.1 GCC RUNTIME LIBRARY EXCEPTION**

```
Version 3.1, 31 March 2009
Copyright © 2009 Free Software Foundation, Inc. http://fsf.org/
Everyone is permitted to copy and distribute verbatim copies of this license document,
\rightarrow but changing it is not allowed.
This GCC Runtime Library Exception ("Exception") is an additional permission under.
\rightarrowsection 7 of the GNU General Public License,
version 3 ("GPLv3"). It applies to a given file (the "Runtime Library") that bears a
→notice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

## See also:

• http://www.gnu.org/licenses/gcc-exception.html

# **8.1.2 GNU GENERAL PUBLIC LICENSE**

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

License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. 14. Revised Versions of this License. The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. 15. Disclaimer of Warranty. THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 16. Limitation of Liability. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF

17. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided

(continues on next page)

SUCH DAMAGES.

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page) 8.1. GCC

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

## See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# A

```
AdaptGrad
   OEMolPotential:: OEInterAdaptor, 84
   OEMolPotential:: OEQuatAdaptor, 115
   OEMolPotential:: OESubsetAdaptor, 122
                                            C
   OEMolPotential:: OETorAdaptor, 124
   OEMolPotential:: OETorOuatAdaptor,
       125
AdaptHessian
   OEMolPotential:: OESubsetAdaptor, 122
AdaptHostCoords
   OEFF:: OEComplexFF, 168
   OEMolPotential:: OEInterMolFunc1.86
AdaptVar
   OEOpt:: OEAdaptor, 38
AddMolFunc
   OEMolPotential:: OEGenericFF, 77
   OEMolPotential:: OEGenericFF2, 79
Assignment operator
   OEMolPotential:: OEBendPotential, 63
   OEMolPotential:: OECoulombPotential,
       64
   OEMolPotential:: OEFFParams, 65
   OEMolPotential:: OEFFPotential, 72
   OEMolPotential:: OEInteractParams, 82
   OEMolPotential:: OEInterCoulombPotential, OEFF:: OEFF14SBSmirnoffParams, 185
       86
   OEMolPotential:: OEInterNonBondPotBase,
       89
   OEMolPotential:: OEInterNonBondPotential, OEFF:: OEMMFFIEFF, 177
       Q<sub>1</sub>OEMolPotential:: OEInterVdwPotential,
       92
   OEMolPotential:: OENonBondIntcsOptions,
       108
   OEMolPotential:: OENonBondPotBase,
       106
   OEMolPotential:: OENonBondPotential,
       108
   OEMolPotential:: OEOutOfPlanePotential,
       114
   OEMolPotential:: OEStretchPotential,
```

119 OEMolPotential:: OETorsionPotential,  $128$ OEMolPotential:: OEVdwPotential, 132

```
Clear
   OEMolPotential:: OEInteractParams, 82
   OEMolPotential:: OEMolFunc, 97
ClearPredicates
   OEMolPotential:: OEMolFunc. 98
Constructors
   OEConstr:: OEDihedralQuadPenalty, 141
   OEConstr:: OEHarmonicPotential, 143
   OEFF:: OEComplexEnergies, 165
   OEFF:: OEComplexFF, 168
   OEFF:: OEComplexFFParameter, 171
   OEFF:: OEFF14SBParsley, 189
   OEFF:: OEFF14SBParsleyComplex, 172
   OEFF:: OEFF14SBParsleyParams, 190
   OEFF:: OEFF14SBSage, 187
   OEFF:: OEFF14SBSageComplex, 183
   OEFF:: OEFF14SBSageParams, 188
   OEFF:: OEFF14SBSmirnoff, 184
   OEFF:: OEFF14SBSmirnoffComplex, 173
   OEFF:: OEForceFieldParameter. 174
   OEFF:: OEMMFFAmberComplex, 175
   OEFF:: OEMMFFComplex, 176
   OEFF:: OEMMFFIEFFOptions, 178
   OEFF:: OEMMFFSheffield, 180
   OEFF:: OEMMFFSheffieldOptions, 181
   OEFF:: OESmirnoffComplex, 191
   OEMOLMMFF:: OEMMFF, 145
   OEMolMMFF:: OEMMFF94sParams, 146
   OEMolMMFF:: OEMMFFOutOfPlane, 148
   OEMolMMFF:: OEMMFFParams. 149
   OEMolMMFF:: OEMMFFStretchBend, 151
   OEMolPotential:: OEBendParams, 61
   OEMolPotential:: OEBendPotential, 63
```

```
OEMolPotential:: OECoulombPotential,
                                            OEOpt:: OEFletcherReevesOpt, 43
   64
                                            OEOpt:: OEHestenesStiefelOpt, 51
OEMolPotential:: OEFFParams, 65
                                            OEOpt:: OEMaxStepLineMinimize, 53
OEMolPotential:: OEFFPotential, 71
                                            OEOpt:: OENewtonOpt, 60
OEMolPotential:: OEGenericFF, 77
                                            OEOpt:: OENRLineSearch, 54
OEMolPotential:: OEGenericFF2, 79
                                            OEOpt:: OEQNLineMinimize, 58
OEMolPotential:: OEInteraction. 80
                                            OEOpt:: OERibierePolakOpt, 59
OEMolPotential:: OEInteractParams, 81
                                            OEOpt:: OESteepestDescentOpt, 59
OEMolPotential:: OEInterAdaptor, 84
                                            OESheff:: OESheffield, 161
OEMolPotential:: OEInterCoulombPotential, OESheff:: OESheffieldOptions, 163
   85
                                        CreateCopy
OEMolPotential:: OEInterNonBondPotBase,
                                            OEMolPotential:: OEFFParams, 65
                                            OEMolPotential:: OENonBondIntcsOptions,
   89
OEMolPotential:: OEInterNonBondPotential,
                                               109
   90OEOpt:: OELineMinimize, 53
OEMolPotential:: OEInterVdwPotential,
                                        F
   92
OEMolPotential:: OENonBondIntcsOptionsExample Code
   108
                                            ffcomplexopt.py, 23
OEMolPotential:: OENonBondPotBase,
                                            ffcomplexquat.py, 31
   106
                                            ffcustomsmirnoff.py, 33
OEMolPotential:: OENonBondPotential,
                                            ffenergy.py, 19
   107
                                            ffinteractions.py, 21
OEMolPotential:: OENumericMolFunc2.
                                            ffoptimize.py, 17
   111
                                            ffsubset.py, 26
OEMolPotential:: OEOutOfPlaneParams,
                                            fftoradaptor.py, 28
   112
                                            func1chk.py, 13
OEMolPotential:: OEOutOfPlanePotential,
                                            func2opt.py, 11113
                                            molfunclopt.py, 15
OEMolPotential:: OEQuatAdaptor, 115
                                        F
OEMolPotential:: OEScaledMolFunc. 117
OEMolPotential:: OEStretchParams. 118
                                        ffcomplexopt.py
OEMolPotential:: OEStretchPotential,
                                            Example Code, 23
   119
                                        ffcomplexquat.py
OEMolPotential:: OESubsetAdaptor, 121
                                            Example Code, 31
OEMolPotential:: OETorAdaptor, 123
                                        ffcustomsmirnoff.py
OEMolPotential:: OETorQuatAdaptor,
                                            Example Code, 33
   125ffenergy.py
OEMolPotential:: OETorsionParams, 126
                                            Example Code, 19
OEMolPotential:: OETorsionPotential,
                                        ffinteractions.py
   128
                                            Example Code, 21
OEMolPotential:: OEVdwParams, 129
                                        ffoptimize.py
OEMolPotential:: OEVdwPotential, 131
                                            Example Code, 17
OEMolSmirnoff:: OEParsley, 153
                                        ffsubset.py
OEMolSmirnoff:: OEParsleyParams, 154
                                            Example Code, 26
OEMolSmirnoff:: OESage, 155
                                        fftoradaptor.py
OEMolSmirnoff:: OESageParams, 156
                                            Example Code, 28
OEMolSmirnoff:: OESmirnoff, 158
                                        func1chk.py
OEMolSmirnoff:: OESmirnoffParams, 159
                                            Example Code, 13
OEOpt:: OEBFGSOpt, 39
                                        func2opt.py
OEOpt:: OECGLineMinimize, 40
                                            Example Code, 11
OEOpt:: OEConjGradOpt, 42
                                        G
OEOpt:: OEDFPOpt, 42
```

```
Get
```

OEOpt:: OEFComponent, 43

OEMolPotential:: OEInteractParams, 82 Get dc OEConstr:: OEHarmonicPotential, 143 Get kc OEConstr:: OEHarmonicPotential, 143  $G \ominus F A$ OESheff:: OESheffieldOptions, 163  $Ge+Atom1$ OEMolPotential:: OEVdwParams, 130 GetAtom2 OEMolPotential:: OEVdwParams, 130 GetAtomIndex1 OEMolPotential:: OEBendParams, 61 OEMolPotential:: OEOutOfPlaneParams,  $112$ OEMolPotential:: OEStretchParams, 118 OEMolPotential:: OETorsionParams, 127 OEMolPotential:: OEVdwParams, 130 GetAtomIndex2 OEMolPotential:: OEBendParams, 61 OEMolPotential:: OEOutOfPlaneParams, 112 OEMolPotential:: OEStretchParams, 118 OEMolPotential:: OETorsionParams. 127 OEMolPotential:: OEVdwParams, 130 GetAtomIndex3 OEMolPotential:: OEBendParams, 62 OEMolPotential:: OEOutOfPlaneParams, 112 OEMolPotential:: OETorsionParams, 127 GetAtomIndex4 OEMolPotential:: OEOutOfPlaneParams.  $112$ OEMolPotential:: OETorsionParams, 127 GetAtoms OEMolPotential:: OEInteraction, 80 GetAtomTypeIndex OEMolPotential:: OEFFParams, 66 GetAtomTypeName OEMolPotential:: OEFFParams, 66 GetB OESheff:: OESheffieldOptions, 163 GetBendParams OEMolPotential:: OEFFParams, 68 GetC OESheff:: OESheffieldOptions, 163 GetComplexSolvationEnergy OEFF:: OEComplexEnergies, 166 GetComponents OEMolPotential:: OEGenericFF, 77 OEMolPotential:: OEGenericFF2, 79 GetContactDistance OEMolPotential:: OEFFParams, 66 GetCoulombParams

OEMolPotential:: OEFFParams, 66 GetCutoff OEMolPotential:: OENonBondIntcsOptions, 109 GetDesolvationEnergy OEFF:: OEComplexEnergies, 166 GetDielectric OEFF:: OEMMFFSheffieldOptions, 181 GetDielectricDerivative OESheff:: OESheffield, 162 GetEquilibriumAngle OEMolPotential:: OEFFParams, 66 GetEquilibriumBondLength OEMolPotential:: OEFFParams, 67 GetExponent OEFF:: OEMMFFSheffieldOptions, 181 GetFComponents OEOpt:: OEFunc0, 46 GetForceFieldType OEFF:: OEMMFFSheffieldOptions, 181 GetHessianDimension OEOpt:: OEBFGSOpt, 39 GetHostComponents OEFF:: OEComplexEnergies, 166 GetHostEnergy OEFF:: OEComplexEnergies, 166 GetHostSolvationEnergy OEFF:: OEComplexEnergies, 166 GetIEFFTerms OEFF:: OEMMFFIEFFOptions, 178 GetInteractions OEMolPotential:: OEMolFunc. 98 GetInterComponents OEFF:: OEComplexEnergies, 166 GetInterEnergy OEFF:: OEComplexEnergies, 166 GetInverseHessian OEOpt:: OEBFGSOpt, 39 GetIterLimit OEOpt:: OEOptimizer0, 55 OEOpt:: OEOptimizer1, 56 OEOpt:: OEOptimizer2, 57 GetKeepHessian OEOpt:: OEBFGSOpt, 39 GetLigandComponents OEFF:: OEComplexEnergies, 167 GetLigandEnergy OEFF:: OEComplexEnergies, 167 GetLigandSolvationEnergy OEFF:: OEComplexEnergies, 167 GetList OEMolPotential:: OEInteractParams, 82 GetMMFFTerms OEFF:: OEMMFFIEFFOptions, 178

GetName OEMolPotential:: OEInteraction, 80 GetNonBondOptions OEMolPotential:: OENonBondPotBase, 106 GetOutOfPlaneParams OEMolPotential:: OEFFParams. 69 GetPenaltyConstant OEConstr:: OEDihedralQuadPenalty, 141 GetSoluteDielectricConstant OESheff:: OESheffieldOptions, 163 GetSolventDielectricConstant OESheff:: OESheffieldOptions, 163 GetSpecifiedAngle OEConstr:: OEDihedralOuadPenalty, 141 GetStretchBendParams OEMolPotential:: OEFFParams, 67 GetStretchParams OEMolPotential:: OEFFParams, 68 GetTitle OEMolPotential:: OEFFParams, 70 OEMolPotential:: OEForceField, 73 GetTolerance OEOpt:: OEOptimizer1, 56 OEOpt:: OEOptimizer2, 57 GetTorsionParams OEMolPotential:: OEFFParams, 69 GetTotalEnergy OEFF:: OEComplexEnergies, 167 GetUseCoulomb OEMolPotential:: OENonBondIntcsOptions,  $1<sub>0</sub>$ GetUseMMFF94s OEFF:: OEMMFFIEFFOptions, 178 GetUseVdW OEMolPotential:: OENonBondIntcsOptions. 109 GetValues OEMolPotential:: OEInteraction, 80 GetVar OEFF:: OEComplexFF, 168 OEMolPotential:: OEInterMolFunc1, 87 OEOpt:: OEAdaptor, 38 GetVdwParams OEMolPotential:: OEFFParams, 68 GetVdwRadius OEMolPotential:: OEFFParams, 67

# H.

HasBendParams OEMolPotential:: OEFFParams, 70 HasCoulomb OEMolPotential:: OEForceField, 74 HasInternalCharges

OEMolPotential:: OEForceField, 74 HasStretchParams OEMolPotential:: OEFFParams, 70 HasTorsionParams OEMolPotential:: OEFFParams, 70 HasVdwParams OEMolPotential:: OEFFParams. 70

# $\mathbf{I}$

```
IsAngle
   OEMolPotential:: OEBendParams, 62
IsBond
   OEMolPotential:: OEStretchParams, 118
IsPair
   OEMolPotential:: OEVdwParams, 130
IsRedundant
   OEMolPotential:: OEQuatAdaptor, 115
IsTorsion
   OEMolPotential:: OETorsionParams, 127
IsValid
   OEMolPotential:: OEBendParams, 62
   OEMolPotential:: OEOutOfPlaneParams,
       113
   OEMolPotential:: OEStretchParams, 118
   OEMolPotential:: OETorsionParams, 127
   OEMolPotential:: OEVdwParams, 130
```

# $\mathbf{L}$

Load OEFF:: OEFF14SBSmirnoffParams, 185 OEMolSmirnoff:: OESmirnoffParams, 159

# м

molfunclopt.py Example Code, 15

# N

NumAtoms OEMolPotential:: OEInteraction, 81 NumValues OEMolPotential:: OEInteraction, 81 NumVar OEOpt:: OEFunc0, 46

# O

OEConstr:: OEDihedralQuadPenalty, 140 Constructors, 141 GetPenaltyConstant, 141 GetSpecifiedAngle, 141 operator= $, 141$ OEConstr:: OEHarmonicPotential, 142 Constructors, 143 Get dc, 143 Get kc, 143

operator=, 143 Set, 143 Set dc, 143 Set\_kc, 143 OEFF:: OEClearForceFieldDummyAtom, 192 OEFF:: OEClearForceFieldDummyAtoms, 192 OEFF:: OEComplexEnergies, 165 Constructors, 165 GetComplexSolvationEnergy, 166 GetDesolvationEnergy, 166 GetHostComponents, 166 GetHostEnergy, 166 GetHostSolvationEnergy, 166 GetInterComponents, 166 GetInterEnergy, 166 GetLigandComponents, 167 GetLigandEnergy, 167 GetLigandSolvationEnergy, 167 GetTotalEnergy, 167 operator= $, 165$ OEFF:: OEComplexFF, 167 AdaptHostCoords, 168 Constructors, 168 GetVar. 168 Set, 169 SetHostFlex, 169 SetNonBondCutoff, 169 SetupHost, 169 OEFF:: OEComplexFFParameter, 170 Constructors, 171 operator=, 171 OEFF:: OEFF14SBParsley, 188 Constructors, 189 operator=, 189 OEFF:: OEFF14SBParsleyComplex, 171 Constructors, 172 OEFF:: OEFF14SBParsleyParams, 189 Constructors, 190 operator=, 191 OEFF:: OEFF14SBSage, 186 Constructors, 187 operator=, 187 OEFF:: OEFF14SBSageComplex, 182 Constructors, 183 OEFF:: OEFF14SBSageParams, 187 Constructors, 188 operator=, 188 OEFF:: OEFF14SBSmirnoff, 183 Constructors, 184 operator=, 184 PrepMol, 184 OEFF:: OEFF14SBSmirnoffComplex, 172 Constructors, 173 OEFF:: OEFF14SBSmirnoffParams, 184

Constructors, 185 Load, 185 operator=, 185 OEFF:: OEFFGetArch, 194 OEFF:: OEFFGetLicensee, 194 OEFF:: OEFFGetPlatform, 194 OEFF:: OEFFGetRelease. 194 OEFF:: OEFFGetSite, 195 OEFF:: OEFFGetVersion, 195 OEFF:: OEFFIsLicensed, 195 OEFF:: OEForceFieldParameter, 173 Constructors, 174 operator=, 174 OEFF:: OEGetMMFFSheffieldFFName, 192 OEFF:: OEGetMMFFSheffieldFFType, 193 OEFF:: OEIsForceFieldDummyAtom, 193 OEFF:: OEIsValidMMFFSheffieldFF, 193 OEFF:: OELigandFFType, 195 OEFF:: OELigandFFType:: MMFF94, 195 OEFF:: OELigandFFType:: MMFF94S, 196 OEFF:: OELigandFFType:: PARSLEY, 196 OEFF:: OELigandFFType:: SAGE, 196 OEFF:: OEMMFFAmberComplex, 174 Constructors, 175 OEFF:: OEMMFFComplex, 175 Constructors, 176 OEFF:: OEMMFFIEFF, 176 Constructors, 177 OEFF:: OEMMFFIEFFOptions, 177 Constructors, 178 GetIEFFTerms, 178 GetMMFFTerms, 178 GetUseMMFF94s, 178 operator=, 178 SetIEFFTerms, 178 SetMMFFTerms, 178 SetUseMMFF94s, 179 OEFF:: OEMMFFSheffield, 179 Constructors, 180 OEFF:: OEMMFFSheffieldFFType, 196 OEFF:: OEMMFFSheffieldFFType:: Invalid, 198 OEFF:: OEMMFFSheffieldFFType:: MMFF, 196 OEFF:: OEMMFFSheffieldFFType:: MMFF94S, 197 OEFF:: OEMMFFSheffieldFFType:: MMFF94S\_NOESTAT, 197 OEFF:: OEMMFFSheffieldFFType:: MMFF94S\_SHEFF, 197 OEFF:: OEMMFFSheffieldFFType:: MMFF94S\_TRUNC, 197 OEFF:: OEMMFFSheffieldFFType:: MMFF94Smod, 197

```
OEFF:: OEMMFFSheffieldFFType:: MMFF94Smod NOESB&ELgnment operator. 64
       197
                                                Constructors. 64
OEFF:: OEMMFFSheffieldFFType:: MMFF94Smod_GEMETPotential:: OEFFParam, 132
       197
                                            OEMolPotential:: OEFFParam:: a0, 133
OEFF:: OEMMFFSheffieldFFType:: MMFF94Smod_ORMNCPotential:: OEFFParam:: BendConst,
       197
                                                    134
OEFF:: OEMMFFSheffieldFFType:: MMFF NOESTACEMolPotential:: OEFFParam:: ContactDist,
       196
                                                    133
OEFF:: OEMMFFSheffieldFFType:: MMFF_SHEFF, OEMolPotential:: OEFFParam:: eps, 133
       196
                                            OEMolPotential:: OEFFParam:: Epsilon, 133
OEFF:: OEMMFFSheffieldFFType:: MMFF_TRUNC, OEMolPotential:: OEFFParam:: EqAngle, 133
                                            OEMolPotential:: OEFFParam:: EqDist, 132
       196
OEFF:: OEMMFFSheffieldOptions, 180
                                            OEMolPotential:: OEFFParam:: EqDistance,
   Constructors, 181
                                                    132
   GetDielectric, 181
                                            OEMolPotential:: OEFFParam:: k, 133
   GetExponent, 181
                                            OEMolPotential:: OEFFParam:: ka, 134
   GetForceFieldType, 181
                                            OEMolPotential:: OEFFParam:: kb1, 134
   operator=, 181
                                            OEMolPotential:: OEFFParam:: kb2, 134
   SetDielectric, 181
                                            OEMolPotential:: OEFFParam:: ko, 135
   SetExponent, 182
                                            OEMolPotential:: OEFFParam:: listDv, 136
   SetForceFieldType, 182
                                            OEMolPotential:: OEFFParam:: listKv, 136
OEFF:: OESetForceFieldDummyAtom, 193
                                            OEMolPotential:: OEFFParam:: listPhv, 136
OEFF:: OESmirnoffComplex, 191
                                            OEMolPotential:: OEFFParam:: listPv, 136
   Constructors. 191
                                            OEMolPotential:: OEFFParam:: ntt. 136
OEMolMMFF:: OEIsValidMMFFMolecule, 151
                                            OEMolPotential:: OEFFParam:: OOP, 135
OEMOLMMFF:: OEMMFF, 144
                                            OEMolPotential:: OEFFParam:: OutOfPlaneConst,
   Constructors, 145
                                                    135
   operator=, 145
                                            OEMolPotential:: OEFFParam:: p1, 136
OEMolMMFF:: OEMMFF94sParams, 145
                                            OEMolPotential:: OEFFParam:: ph1, 136
   Constructors, 146
                                            OEMolPotential:: OEFFParam:: r0, 132
OEMolMMFF:: OEMMFFCalcVdw, 151
                                            OEMolPotential:: OEFFParam:: r1, 134
OEMolMMFF:: OEMMFFOutOfPlane.147
                                            OEMolPotential:: OEFFParam:: r2, 134
   Constructors, 148
                                            OEMolPotential:: OEFFParam:: rij, 133
   operator=, 148
                                            OEMolPotential:: OEFFParam:: StretchBendConst1,
   Set. 148
                                                    134
OEMolMMFF:: OEMMFFParams. 148
                                            OEMolPotential:: OEFFParam:: StretchBendConst2.
   Constructors, 149
                                                    134
OEMolMMFF:: OEMMFFStretchBend, 149
                                            OEMolPotential:: OEFFParam:: StretchConst,
   Constructors, 151
                                                    132
                                            OEMolPotential:: OEFFParam:: V1, 135
   operator=, 151
   Set, 151
                                            OEMolPotential:: OEFFParam:: v1, 135
OEMolPotential:: OEBendParams, 61
                                            OEMolPotential:: OEFFParam:: V2, 135
                                            OEMolPotential:: OEFFParam:: v2, 135
   Constructors. 61
                                            OEMolPotential:: OEFFParam:: V3, 135
   GetAtomIndex1, 61
   GetAtomIndex2, 61
                                            OEMolPotential:: OEFFParam:: v3, 136
   GetAtomIndex3, 62
                                            OEMolPotential:: OEFFParams, 64
   IsAngle, 62
                                                Assignment operator, 65
   IsValid, 62
                                                Constructors, 65
   operator=, 61
                                                CreateCopy, 65
OEMolPotential:: OEBendPotential, 62
                                                GetAtomTypeIndex, 66
   Assignment operator, 63
                                                GetAtomTypeName, 66
                                                GetBendParams, 68
   Constructors, 63
   Set. 63
                                                GetContactDistance. 66
OEMolPotential:: OECoulombPotential, 63
                                                GetCoulombParams, 66
```

GetEquilibriumAngle. 66 GetEquilibriumBondLength, 67 GetOutOfPlaneParams, 69 GetStretchBendParams, 67 GetStretchParams, 68 GetTitle, 70 GetTorsionParams. 69 GetVdwParams, 68 GetVdwRadius. 67 HasBendParams, 70 HasStretchParams, 70 HasTorsionParams, 70 HasVdwParams, 70 PrepMol, 67 OEMolPotential:: OEFFPotential, 70 Assignment operator, 72 Constructors, 71 Set.72 OEMolPotential:: OEForceField, 72 GetTitle.73 HasCoulomb, 74 HasInternalCharges, 74 PrepMol, 74 Set.75 SetNonBondCutoff, 75 SetTitle.75 OEMolPotential:: OEFuncType, 137 OEMolPotential:: OEFuncType:: All, 139 OEMolPotential:: OEFuncType:: AllRepel, 139 OEMolPotential:: OEFuncType:: Bend, 138 OEMolPotential:: OEFuncType:: Bond, 138 OEMolPotential:: OEFuncType:: Coulomb, 138 OEMolPotential:: OEFuncType:: HarmonicPot,  $140$ OEMolPotential:: OEFuncType:: ImproperTorsion, SetList, 82 139 OEMolPotential:: OEFuncType:: InterAdapt, 140 OEMolPotential:: OEFuncType:: InterMolCoulomb, Set, 84 139 OEMolPotential:: OEFuncType:: InterMolVdW, 84 139 OEMolPotential:: OEFuncType:: OutOfPlane, 139 OEMolPotential:: OEFuncType:: QuatAdapt, 139 OEMolPotential:: OEFuncType:: Sheffield,  $140$ OEMolPotential::OEFuncType::Stretch,138 OEMolPotential::OEInterMolFunc2,87 OEMolPotential::OEFuncType::StretchBend, OEMolPotential::OEInterNonBondPotBase, 138 88 OEMolPotential:: OEFuncType:: SubsetAdapt,

OEMolPotential:: OEFuncType:: SubsetAdaptor, 140 OEMolPotential:: OEFuncType:: TorAdapt, 139 OEMolPotential:: OEFuncType:: Torsion, 138 OEMolPotential:: OEFuncType:: Undefined, 137 OEMolPotential:: OEFuncType:: VdW, 138 OEMolPotential:: OEFuncType:: VdWRepel, 138 OEMolPotential:: OEGenericFF, 75 AddMolFunc, 77 Constructors, 77 GetComponents, 77 RemoveMolFunc, 77 OEMolPotential:: OEGenericFF2, 77 AddMolFunc. 79 Constructors, 79 GetComponents, 79 RemoveMolFunc, 79 OEMolPotential:: OEInteraction, 79 Constructors, 80 GetAtoms, 80 GetName. 80 GetValues. 80 NumAtoms, 81 NumValues, 81 operator=, 80 OEMolPotential:: OEInteractParams, 81 Assignment operator, 82 Clear, 82 Constructors, 81 Get. 82 GetList, 82 Set. 82 OEMolPotential:: OEInterAdaptor, 83 AdaptGrad, 84 Constructors, 84 OEMolPotential:: OEInterCoulombPotential, Assignment operator, 86 Constructors, 85 OEMolPotential:: OEInterMolFunc1, 86 AdaptHostCoords, 86 GetVar, 87 SetHostFlex, 87 SetupHost, 87 Assignment operator, 89

Constructors, 89

 $140$ 

Set.89 SetNonBondCutoff, 89 OEMolPotential::OEInterNonBondPotential, OEMolPotential::OEQuatAdaptor, 114  $90$ Assignment operator, 91 Constructors, 90 OEMolPotential:: OEInterVdwPotential, 91 Assignment operator, 92 Constructors, 92 OEMolPotential:: OEMolAdaptor, 92 SetMolFunc, 93 OEMolPotential:: OEMolAdaptor2, 93 SetMolFunc2, 95 OEMolPotential:: OEMolFunc, 95 Clear, 97 ClearPredicates, 98 GetInteractions, 98 Set.98 Setup, 98 OEMolPotential:: OEMolFunc0, 99 OEMolPotential:: OEMolFunc1, 101 OEMolPotential:: OEMolFunc2, 104 OEMolPotential:: OENonBondIntcsOptions, 108 Assignment operator, 108 Constructors, 108 CreateCopy, 109 GetCutoff, 109 GetUseCoulomb, 109 GetUseVdW, 109 SetCutoff, 109 SetUseCoulomb, 109 SetUseVdW, 109 OEMolPotential:: OENonBondPotBase, 105 Assignment operator, 106 Constructors, 106 GetNonBondOptions, 106 Set, 107 OEMolPotential:: OENonBondPotential, 107 Assignment operator, 108 Constructors, 107 OEMolPotential:: OENumericMolFunc2, 110 Constructors, 111 Set, 111 OEMolPotential:: OEOutOfPlaneParams, 111 Constructors, 112 GetAtomIndex1, 112 GetAtomIndex2, 112 GetAtomIndex3, 112 GetAtomIndex4, 112 IsValid, 113 operator= $, 112$ OEMolPotential:: OEOutOfPlanePotential, 113

Constructors, 113 AdaptGrad, 115 Constructors, 115 IsRedundant, 115 OEMolPotential:: OEScaledMolFunc, 116 Constructors, 117 Set, 117 OEMolPotential:: OEStretchParams, 117 Constructors, 118 GetAtomIndex1, 118 GetAtomIndex2, 118 IsBond, 118 IsValid, 118 operator=, 118 OEMolPotential:: OEStretchPotential, 119 Assignment operator, 119 Constructors, 119 Set, 120 OEMolPotential:: OESubsetAdaptor, 120 AdaptGrad, 122 AdaptHessian, 122 Constructors, 121 Set, 122 OEMolPotential:: OETorAdaptor, 122 AdaptGrad, 124 Constructors, 123 Set, 124 OEMolPotential:: OETorQuatAdaptor, 124 AdaptGrad, 125 Constructors, 125 Set. 126 OEMolPotential:: OETorsionParams, 126 Constructors, 126 GetAtomIndex1, 127 GetAtomIndex2, 127 GetAtomIndex3, 127 GetAtomIndex4, 127 IsTorsion, 127 IsValid, 127 operator=, 127 OEMolPotential:: OETorsionPotential, 128 Assignment operator, 128 Constructors, 128 Set, 129 OEMolPotential:: OEVarType, 137 OEMolPotential:: OEVarType:: Cart, 137 OEMolPotential:: OEVarType:: SolidBody, 137 OEMolPotential:: OEVarType:: Torsions, 137 OEMolPotential:: OEVarType:: TranRotTor, 137 OEMolPotential:: OEVdwParams, 129

Assignment operator, 114

Constructors, 129 OEOpt:: OEConjGradOpt, 42 GetAtom1.130 Constructors, 42 GetAtom2, 130 operator=, 42 GetAtomIndex1, 130 OEOpt:: OEDFPOpt, 42 GetAtomIndex2, 130 Constructors, 42 IsPair, 130 operator= $, 43$ IsValid. 130 OEOpt:: OEFComponent, 43 operator=, 129 Constructors, 43 OEMolPotential:: OEVdwPotential, 131 OEOpt:: OEFletcherReevesOpt, 43 Assignment operator, 132 Constructors, 43 Constructors, 131 operator=, 44 OEMolSmirnoff:: OEParsley, 152 OEOpt:: OEFunc0, 44 Constructors, 153 GetFComponents, 46 operator=, 153 NumVar, 46 OEMolSmirnoff:: OEParsleyParams, 153 operator(), 46 Constructors, 154 OEOpt:: OEFunc1, 47 operator=, 154 operator(), 49 OEMolSmirnoff:: OESage, 154 OEOpt:: OEFunc2, 49 Constructors, 155 operator(), 51 operator=, 155 OEOpt:: OEHestenesStiefelOpt, 51 OEMolSmirnoff:: OESageParams, 155 Constructors, 51 Constructors, 156 operator=, 52 OEOpt:: OELineMinimize, 52 operator=, 157 OEMolSmirnoff:: OESmirnoff.157 CreateCopy, 53 operator(), 52 Constructors, 158 operator=, 158 SetMaxStep, 52 OEMolSmirnoff:: OESmirnoffParams, 158 OEOpt:: OEMaxStepLineMinimize, 53 Constructors, 159 Constructors, 53 Load, 159  $operatorerator =$ , 53 OEOpt:: OENewtonOpt, 60 operator=, 159 OEMolSmirnoff:: OESmirnoffType, 160 Constructors, 60 OEMolSmirnoff:: OESmirnoffType:: PARSLEY\_OPENEERerator=, 60 OEOpt:: OENRLineSearch, 54 160 OEMolSmirnoff:: OESmirnoffType:: SAGE\_OPENFF, Constructors, 54 160 OEOpt:: OEOptimizer0.54 OEMolSmirnoff:: OESmirnoffType:: SMIRNOFF99FROG& LLerLimit, 55 160 operator $($ ), 54 OEOpt:: OEAdaptor, 37 SetIterLimit, 55 AdaptVar, 38 OEOpt:: OEOptimizer1, 55 GetIterLimit, 56 GetVar, 38 OEOpt:: OEBFGSOpt, 38 GetTolerance, 56 Constructors, 39 operator $($ ), 56 GetHessianDimension, 39 SetIterLimit, 56 GetInverseHessian, 39 SetLineMinimize, 56 GetKeepHessian, 39 SetTolerance, 56 operator=, 39 OEOpt:: OEOptimizer2, 57 SetKeepHessian, 39 GetIterLimit.57 UseSavedHessian, 39 GetTolerance, 57 OEOpt:: OECGLineMinimize, 40 operator(), 57 SetIterLimit.58 Constructors, 40 OEOpt:: OECheckpoint0, 40 SetTolerance, 58 operator $($ ), 40 OEOpt:: OEQNLineMinimize, 58 OEOpt:: OECheckpoint1, 41 Constructors, 58 operator(), 41 OEOpt:: OERibierePolakOpt, 58

```
Constructors, 59
   operator=, 59
OEOpt:: OESteepestDescentOpt, 59
   Constructors, 59
   SetInitialStep, 60
OESheff:: OESheffield, 160
   Constructors. 161
   GetDielectricDerivative, 162
   operator=, 161
   Set, 162
   SetCharges, 162
   SetRadii, 162
OESheff:: OESheffieldOptions, 162
   Constructors, 163
   GetA, 163
   GetB, 163
   GetC, 163
   GetSoluteDielectricConstant, 163
   GetSolventDielectricConstant, 163
   operator=, 163SetA, 164
   SetB, 164
   SetC, 164
   SetSoluteDielectricConstant. 164
   SetSolventDielectricConstant, 164
OESheff:: OESheffieldParamType, 164
OESheff::OESheffieldParamType::Protein,
                                             D
       165
OESheff::OESheffieldParamType::SmallMol, PrepMol
       164
operator()
   OEOpt:: OECheckpoint0, 40
   OEOpt:: OECheckpoint1, 41
   OEOpt:: OEFunc0, 46
   OEOpt:: OEFunc1, 49
   OEOpt:: OEFunc2, 51
   OEOpt:: OELineMinimize, 52
   OEOpt:: OEOptimizer0, 54
   OEOpt:: OEOptimizer1, 56
   OEOpt:: OEOptimizer2, 57
operator=
   OEConstr:: OEDihedralQuadPenalty, 141
   OEConstr:: OEHarmonicPotential, 143
   OEFF:: OEComplexEnergies, 165
   OEFF:: OEComplexFFParameter, 171
   OEFF:: OEFF14SBParsley, 189
   OEFF:: OEFF14SBParsleyParams, 191
   OEFF:: OEFF14SBSage, 187
   OEFF:: OEFF14SBSageParams, 188
   OEFF:: OEFF14SBSmirnoff, 184
   OEFF:: OEFF14SBSmirnoffParams, 185
   OEFF:: OEForceFieldParameter, 174
   OEFF:: OEMMFFIEFFOptions, 178
   OEFF:: OEMMFFSheffieldOptions, 181
```

OEMOLMMFF:: OEMMFF, 145 OEMolMMFF:: OEMMFFOutOfPlane, 148 OEMolMMFF:: OEMMFFStretchBend, 151 OEMolPotential:: OEBendParams, 61 OEMolPotential:: OEInteraction, 80 OEMolPotential:: OEOutOfPlaneParams, 112 OEMolPotential:: OEStretchParams, 118 OEMolPotential:: OETorsionParams, 127 OEMolPotential:: OEVdwParams, 129 OEMolSmirnoff:: OEParsley, 153 OEMolSmirnoff:: OEParsleyParams, 154 OEMolSmirnoff:: OESage, 155 OEMolSmirnoff:: OESageParams, 157 OEMolSmirnoff:: OESmirnoff, 158 OEMolSmirnoff:: OESmirnoffParams, 159 OEOpt:: OEBFGSOpt, 39 OEOpt:: OEConjGradOpt. 42 OEOpt:: OEDFPOpt, 43 OEOpt:: OEFletcherReevesOpt, 44 OEOpt:: OEHestenesStiefelOpt, 52 OEOpt:: OEMaxStepLineMinimize, 53 OEOpt:: OENewtonOpt, 60 OEOpt:: OERibierePolakOpt, 59 OESheff:: OESheffield, 161 OESheff:: OESheffieldOptions, 163

OEFF:: OEFF14SBSmirnoff, 184 OEMolPotential:: OEFFParams, 67 OEMolPotential:: OEForceField, 74

# R

RemoveMolFunc OEMolPotential:: OEGenericFF, 77 OEMolPotential:: OEGenericFF2, 79

# S Set

```
OEConstr:: OEHarmonicPotential, 143
OEFF:: OEComplexFF, 169
OEMolMMFF:: OEMMFFOutOfPlane, 148
OEMolMMFF:: OEMMFFStretchBend, 151
OEMolPotential:: OEBendPotential, 63
OEMolPotential:: OEFFPotential, 72
OEMolPotential:: OEForceField, 75
OEMolPotential:: OEInteractParams, 82
OEMolPotential:: OEInterAdaptor, 84
OEMolPotential:: OEInterNonBondPotBase.
   89
OEMolPotential:: OEMolFunc, 98
OEMolPotential:: OENonBondPotBase,
   107
```

OEMolPotential:: OENumericMolFunc2, 111 OEMolPotential:: OEScaledMolFunc, 117 OEMolPotential:: OEStretchPotential, 120 OEMolPotential:: OESubsetAdaptor, 122 OEMolPotential:: OETorAdaptor. 124 OEMolPotential:: OETorQuatAdaptor, 126 OEMolPotential:: OETorsionPotential, 129 OESheff::OESheffield, 162 Set\_dc OEConstr:: OEHarmonicPotential, 143 Set ko OEConstr:: OEHarmonicPotential, 143  $S \ominus A$ OESheff:: OESheffieldOptions, 164 SetB OESheff:: OESheffieldOptions, 164 SetC OESheff:: OESheffieldOptions, 164 SetCharges OESheff:: OESheffield. 162 SetCutoff OEMolPotential:: OENonBondIntcsOptions\$etUseCoulomb 109 SetDielectric OEFF:: OEMMFFSheffieldOptions, 181 SetExponent OEFF:: OEMMFFSheffieldOptions, 182 SetForceFieldType OEFF:: OEMMFFSheffieldOptions, 182 SetHostFlex OEFF:: OEComplexFF, 169 OEMolPotential:: OEInterMolFunc1, 87 SetIEFFTerms OEFF:: OEMMFFIEFFOptions, 178 SetInitialStep OEOpt:: OESteepestDescentOpt, 60 SetIterLimit OEOpt:: OEOptimizer0, 55 OEOpt:: OEOptimizer1, 56 OEOpt:: OEOptimizer2, 58 SetKeepHessian OEOpt:: OEBFGSOpt, 39 SetLineMinimize OEOpt:: OEOptimizer1, 56 SetList OEMolPotential:: OEInteractParams, 82 SetMaxStep OEOpt:: OELineMinimize, 52 SetMMFFTerms OEFF:: OEMMFFIEFFOptions, 178

SetMolFunc OEMolPotential:: OEMolAdaptor, 93 SetMolFunc2 OEMolPotential:: OEMolAdaptor2, 95 SetNonBondCutoff OEFF:: OEComplexFF, 169 OEMolPotential:: OEForceField.75 OEMolPotential:: OEInterNonBondPotBase, 89 SetRadii OESheff:: OESheffield, 162 SetSoluteDielectricConstant OESheff:: OESheffieldOptions, 164 SetSolventDielectricConstant OESheff:: OESheffieldOptions, 164 SetTitle OEMolPotential:: OEForceField, 75 SetTolerance OEOpt:: OEOptimizer1, 56 OEOpt:: OEOptimizer2, 58 Setup OEMolPotential:: OEMolFunc, 98 SetupHost OEFF:: OEComplexFF, 169 OEMolPotential:: OEInterMolFunc1, 87 OEMolPotential:: OENonBondIntcsOptions, 109 SetUseMMFF94s OEFF:: OEMMFFIEFFOptions, 179 SetUseVdW OEMolPotential:: OENonBondIntcsOptions, 109

# $\cup$

UseSavedHessian OEOpt:: OEBFGSOpt, 39