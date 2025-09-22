![](_page_0_Picture_0.jpeg)

**Omega TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1      | Theory                     |                                                        | 2  |
|--------|----------------------------|--------------------------------------------------------|----|
|        | 1.1                        | OMEGA Theory                                           | 3  |
|        | 1.2                        | Macrocycle Conformations                               | 4  |
| 2      | GPU-Omega                  |                                                        | 5  |
|        | 2.1                        | GPU-Related Requirements                               | 5  |
|        |                            | 2.1.1 Supported Platforms                              | 5  |
|        |                            | 2.1.2 Supported GPUs                                   | 5  |
|        |                            | 2.1.3 NVIDIA Drivers                                   | 5  |
|        |                            | 2.1.4 Performance Tuning                               | 6  |
|        | 2.2                        | Usage                                                  | 6  |
| 3      | OMEGA Examples             |                                                        | 9  |
|        | 3.1                        | Classic OEOmega Examples                               | 9  |
|        |                            | 3.1.1 Generating Conformers                            | 9  |
|        |                            | 3.1.2 Generating a Single Conformer                    | 11 |
|        |                            | 3.1.3 Generating Densely Sampled Conformers            | 12 |
|        | 3.2                        | Flipper Examples                                       | 13 |
|        |                            | 3.2.1 Generating Stereoisomers                         | 13 |
|        | 3.3                        | Generating Torsion-Driven Conformation Examples        | 15 |
|        |                            | 3.3.1 Torsion Driving to Generating Conformer Ensemble | 15 |
|        | 3.4                        | Fragment Library Generation Examples                   | 16 |
|        |                            | 3.4.1 Making Fragment Library                          | 16 |
|        | 3.5                        | Macrocycle Examples                                    | 18 |
|        |                            | 3.5.1 Generating Macrocycle Conformers                 | 18 |
|        |                            | 3.5.2 Generating a Single Macrocycle Conformer         | 19 |
| 4      | API                        |                                                        | 21 |
|        | 4.1                        | OEConfGen Classes                                      | 21 |
|        |                            | 4.1.1 OEBuilderBase                                    | 21 |
|        |                            | 4.1.2 OEConfFixOptions                                 | 22 |
|        |                            | 4.1.3 GetAtomExpr                                      | 24 |
|        |                            | 4.1.4 GetBondExpr                                      | 24 |
|        |                            | 4.1.5 GetFixDeleteH                                    | 24 |
|        |                            | 4.1.6 GetFixMaxMatch                                   | 24 |
|        |                            | 4.1.7 GetFixMCS                                        | 24 |
|        |                            | 4.1.8 GetFixMol                                        | 24 |
|        |                            | 4.1.9 GetFixPredicate                                  | 24 |
|        |                            | 4.1.10 GetFixRMS                                       | 25 |
|        |                            | 4.1.11 GetFixSmarts                                    | 25 |
| 4.1.12 | GetFixSubSearch            | 25                                                     |    |
| 4.1.13 | GetFixUniqueMatch          | 25                                                     |    |
| 4.1.14 | GetMCSMinAtoms             | 25                                                     |    |
| 4.1.15 | GetMCSFunc                 | 25                                                     |    |
| 4.1.16 | GetMCSType                 | 25                                                     |    |
| 4.1.17 | HasFixPattern              | 26                                                     |    |
| 4.1.18 | SetAtomExpr                | 26                                                     |    |
| 4.1.19 | SetBondExpr                | 26                                                     |    |
| 4.1.20 | SetFixDeleteH              | 26                                                     |    |
| 4.1.21 | SetFixMaxMatch             | 26                                                     |    |
| 4.1.22 | SetFixMol                  | 27                                                     |    |
| 4.1.23 | SetFixMCS                  | 27                                                     |    |
| 4.1.24 | SetFixPredicate            | 27                                                     |    |
| 4.1.25 | SetFixRMS                  | 27                                                     |    |
| 4.1.26 | SetFixSmarts               | 27                                                     |    |
| 4.1.27 | SetFixSubSearch            | 27                                                     |    |
| 4.1.28 | SetFixUniqueMatch          | 28                                                     |    |
| 4.1.29 | SetMCSMinAtoms             | 28                                                     |    |
| 4.1.30 | SetMCSFunc                 | 28                                                     |    |
| 4.1.31 | SetMCSType                 | 28                                                     |    |
| 4.1.32 | OEConformerBuilder         | 28                                                     |    |
| 4.1.33 | OEConfSlicer               | 29                                                     |    |
| 4.1.34 | OEFlipperClassicOptions    | 30                                                     |    |
| 4.1.35 | OEFlipperOptions           | 34                                                     |    |
| 4.1.36 | OEFragBuilder              | 40                                                     |    |
| 4.1.37 | Build                      | 41                                                     |    |
| 4.1.38 | GetOptions                 | 41                                                     |    |
| 4.1.39 | SetOptions                 | 41                                                     |    |
| 4.1.40 | OEFragBuilderOptions       | 41                                                     |    |
| 4.1.41 | OEFragOptions              | 44                                                     |    |
| 4.1.42 | GetEnergyWindow            | 44                                                     |    |
| 4.1.43 | GetFragGen                 | 44                                                     |    |
| 4.1.44 | GetFragKeep                | 45                                                     |    |
| 4.1.45 | GetRMS                     | 45                                                     |    |
| 4.1.46 | GetTimeLimit               | 45                                                     |    |
| 4.1.47 | SetEnergyWindow            | 45                                                     |    |
| 4.1.48 | SetFragGen                 | 45                                                     |    |
| 4.1.49 | SetFragKeep                | 45                                                     |    |
| 4.1.50 | SetRMS                     | 45                                                     |    |
| 4.1.51 | SetTimeLimit               | 46                                                     |    |
| 4.1.52 | OEMacrocycleBuilder        | 46                                                     |    |
| 4.1.53 | OEMacrocycleBuilderOptions | 47                                                     |    |
| 4.1.54 | OEMacrocycleOmega          | 49                                                     |    |
| 4.1.55 | OEMacrocycleOmegaOptions   | 50                                                     |    |
| 4.1.56 | OEMakeFragLib              | 53                                                     |    |
| 4.1.57 | AddFrag                    | 54                                                     |    |
| 4.1.58 | GenerateMissingFrags       | 54                                                     |    |
| 4.1.59 | GetMissingFrags            | 54                                                     |    |
| 4.1.60 | OEMolBuilder               | 54                                                     |    |
| 4.1.61 | Build                      | 55                                                     |    |
| 4.1.62 | GetOptions                 | 55                                                     |    |
| 4.1.63 | Prep                       | 56                                                     |    |
| 4.1.64 | SetOptions                 | 56                                                     |    |
| 4.1.65 | OEMolBuilderOptions        | 56                                                     |    |
|        | 4.1.66                     | OEOmega                                                | 6  |
|        | 4.1.67                     | AddFragLib                                             | 6  |
|        | 4.1.68                     | Build                                                  | 6  |
|        | 4.1.69                     | ClearFragLibs                                          | 6  |
|        | 4.1.70                     | GetOptions                                             | 6  |
|        | 4.1.71                     | SetOptions                                             | 6  |
|        | 4.1.72                     | OEOmegaOptions                                         | 6  |
|        | 4.1.73                     | Suboption Parameter Defaults                           | 6  |
|        | 4.1.74                     | OERingFragOptions                                      | 6  |
|        | 4.1.75                     | OESliceEnsembleOptions                                 | 6  |
|        | 4.1.76                     | OETorDriveOptions                                      | 7  |
|        | 4.1.77                     | OETorDriver                                            | 7  |
|        | 4.1.78                     | OETorLib                                               | 7  |
|        | 4.1.79                     | AddTorsionLibrary                                      | 7  |
|        | 4.1.80                     | AddTorsionRule                                         | 7  |
|        | 4.1.81                     | ClearTorsionLibrary                                    | 7  |
|        | 4.1.82                     | GetTorRule                                             | 8  |
|        | 4.1.83                     | GetTorRules                                            | 8  |
|        | 4.1.84                     | HasTorRule                                             | 8  |
|        | 4.1.85                     | ResetTorsionLibrary                                    | 8  |
|        | 4.1.86                     | SetTorsionLibrary                                      | 8  |
|        | 4.1.87                     | OETorLibParameter                                      | 8  |
| 4.2    |                            | OEConfGen Constants                                    | 8  |
|        | 4.2.1                      | OEFragBuilderMode                                      | 8  |
|        | 4.2.2                      | OENitrogenEnumeration                                  | 8  |
|        | 4.2.3                      | OEOmegaForceFieldType                                  | 8  |
|        | 4.2.4                      | OEOmegaReturnCode                                      | 8  |
|        | 4.2.5                      | OEOmegaSampling                                        | 8  |
|        | 4.2.6                      | OESliceEnsembleDefaults                                | 9  |
|        | 4.2.7                      | OETorLibType                                           | 9  |
| 4.3    |                            | OEConfGen Functions                                    | 9  |
|        | 4.3.1                      | OEAddGlobalFragLib                                     | 9  |
|        | 4.3.2                      | OEClearGlobalFragLib                                   | 9  |
|        | 4.3.3                      | OEGetOmegaError                                        | 9  |
|        | 4.3.4                      | OEGetTorValues                                         | 9  |
|        | 4.3.5                      | OEIsMacrocycle                                         | 9  |
|        | 4.3.6                      | OEFlipper                                              | 9  |
|        | 4.3.7                      | OEFlipperStereoCenters                                 | 9  |
|        | 4.3.8                      | OEOmegaGetArch                                         | 9  |
|        | 4.3.9                      | OEOmegaGetLibraryRelease                               | 9  |
|        | 4.3.10                     | OEOmegaGetLibraryVersion                               | 9  |
|        | 4.3.11                     | OEOmegaGetLicensee                                     | 9  |
|        | 4.3.12                     | OEOmegaGetPlatform                                     | 9  |
|        | 4.3.13                     | OEOmegaGetRelease                                      | 9  |
|        | 4.3.14                     | OEOmegaGetSite                                         | 9  |
|        | 4.3.15                     | OEOmegaGetVersion                                      | 9  |
|        | 4.3.16                     | OEOmegaIsGPUReady                                      | 9  |
|        | 4.3.17                     | OEOmegaIsLicensed                                      | 9  |
|        | 4.3.18                     | OEOmegaSystemHasGPU                                    | 9  |
|        | 4.3.19                     | OESliceEnsemble                                        | 9  |
|        | <b>Preliminary API</b>     |                                                        | 9  |
| 5.1    |                            | Preliminary OEConfGen Classes                          | 9  |
|        | 5.1.1                      | OEThompsonOptions                                      | 9  |

 $\overline{\mathbf{5}}$ 

| 5.1.2 GetMaxTrials            | 9  |
|-------------------------------|----|
| 5.1.3 GetMaxTrialsRange       | 9  |
| 5.1.4 GetTrialsRangeIncrement | 9  |
| 5.1.5 GetBatchMaxRotors       | 9  |
| 5.1.6 GetPriorTemperature     | 9  |
| 5.1.7 SetMaxTrials            | 9  |
| 5.1.8 SetMaxTrialsRange       | 9  |
| 5.1.9 SetTrialsRangeIncrement | 9  |
| 5.1.10 SetBatchMaxRotors      | 9  |
| 5.1.11 SetPriorTemperature    | 9  |
| 6 Release History             | 10 |
| 6.1 Omega TK 6.0.0            | 10 |
| 6.1.1 New features            | 10 |
| 6.1.2 Minor bug fixes         | 10 |
| 6.2 Omega TK 5.1.0            | 10 |
| 6.2.1 New features            | 10 |
| 6.2.2 Minor bug fixes         | 10 |
| 6.3 Omega TK 5.0.0            | 10 |
| 6.3.1 New features            | 10 |
| 6.3.2 Minor bug fixes         | 10 |
| 6.4 Omega TK 4.2.2            | 10 |
| 6.4.1 Minor bug fixes         | 10 |
| 6.5 Omega TK 4.2.1            | 10 |
| 6.5.1 New features            | 10 |
| 6.5.2 Minor bug fixes         | 10 |
| 6.6 Omega TK 4.2.0            | 10 |
| 6.6.1 New features            | 10 |
| 6.6.2 Minor bug fixes         | 10 |
| 6.7 Omega TK 4.1.2            | 10 |
| 6.7.1 Minor bug fixes         | 10 |
| 6.8 Omega TK 4.1.1            | 10 |
| 6.8.1 New features            | 10 |
| 6.8.2 Major bug fixes         | 10 |
| 6.8.3 Minor bug fixes         | 10 |
| 6.9 Omega TK 4.1.0            | 10 |
| 6.9.1 New features            | 10 |
| 6.9.2 Major bug fixes         | 10 |
| 6.9.3 Minor bug fixes         | 10 |
| 6.9.4 Documentation changes   | 10 |
| 6.10 Omega TK 4.0.0.6         | 10 |
| 6.11 Omega TK 4.0.0           | 10 |
| 6.11.1 New features           | 10 |
| 6.11.2 Minor bug fixes        | 10 |
| 6.11.3 Documentation changes  | 11 |
| 6.11.4 General Notices        | 11 |
| 6.12 Omega TK 2.9.1           | 11 |
| 6.12.1 New features           | 11 |
| 6.12.2 Major bug fixes        | 11 |
| 6.12.3 Minor bug fixes        | 11 |
| 6.13 Omega TK 2.9.0           | 11 |
| 6.13.1 New features           | 11 |
| 6.13.2 Major bug fixes        | 11 |
| 6.13.3 Minor bug fixes        | 11 |

| Section | Description                    | Page |
|---------|--------------------------------|------|
| 6.14    | Omega TK 2.8.0                 | 11   |
| 6.14.1  | New features (Preliminary API) | 11   |
| 6.14.2  | New features                   | 11   |
| 6.14.3  | Major bug fixes                | 11   |
| 6.14.4  | Minor bug fixes                | 11   |
| 6.14.5  | Documentation changes          | 11   |
| 6.15    | Omega TK 2.7.0                 | 11   |
| 6.16    | Omega TK 2.6.7                 | 11   |
| 6.16.1  | New features                   | 11   |
| 6.16.2  | Documentation changes          | 11   |
| 6.17    | Omega TK 2.6.6                 | 11   |
| 6.17.1  | Major bug fixes                | 11   |
| 6.17.2  | Minor bug fixes                | 11   |
| 6.18    | Omega TK 2.6.5                 | 11   |
| 6.18.1  | New features                   | 11   |
| 6.19    | Omega TK 2.6.4                 | 11   |
| 6.19.1  | Minor bug fixes                | 11   |
| 6.20    | Omega TK 2.6.3                 | 11   |
| 6.20.1  | Major bug fixes                | 11   |
| 6.20.2  | Minor bug fixes                | 11   |
| 6.20.3  | Documentation changes          | 11   |
| 6.21    | Omega TK 2.6.2                 | 11   |
| 6.21.1  | Major bug fixes                | 11   |
| 6.21.2  | Documentation changes          | 11   |
| 6.22    | Omega TK 2.6.1                 | 11   |
| 6.22.1  | Minor bug fixes                | 11   |
| 6.23    | Omega TK 2.6.0                 | 11   |
| 6.23.1  | Major bug fixes                | 11   |
| 6.23.2  | Documentation changes          | 11   |
| 6.24    | Omega TK 2.5.7                 | 11   |
| 6.24.1  | Minor bug fixes                | 11   |
| 6.24.2  | C#-specific changes            | 11   |
| 6.25    | Omega TK 2.5.6                 | 11   |
| 6.25.1  | New features                   | 11   |
| 6.25.2  | Minor bug fixes                | 11   |
| 6.25.3  | Documentation fixes            | 11   |
| 6.26    | Omega TK 2.5.5                 | 11   |
| 6.26.1  | Minor bug fixes                | 11   |
| 6.26.2  | Documentation fixes            | 11   |
| 6.27    | Omega TK 2.5.4                 | 12   |
| 6.27.1  | New features                   | 12   |
| 6.27.2  | Major bug fixes                | 12   |
| 6.27.3  | Minor bug fixes                | 12   |
| 6.28    | Omega TK 2.5.3                 | 12   |
| 6.28.1  | New features                   | 12   |
| 6.28.2  | Minor bug fixes                | 12   |
| 6.29    | Omega TK 2.5.2                 | 12   |
| 6.29.1  | New features                   | 12   |
| 6.29.2  | Minor bug fixes                | 12   |
| 6.30    | Omega TK 2.5.1                 | 12   |
| 6.30.1  | New features                   | 12   |
| 6.30.2  | Major bug fixes                | 12   |
| 6.30.3  | Minor bug fixes                | 12   |
| 6.30.4  | Documentation fixes            | 12   |

| 6.31 Omega TK 2.5.0 ...........................................       | 12 |
|-----------------------------------------------------------------------|----|
| 6.31.1 New features ....................................              | 12 |
| 6.31.2 Major bug fixes ..............................                 | 12 |
| 6.31.3 Minor bug fixes ..............................                 | 12 |
| 6.32 Omega TK 2.4.6 ...........................................       | 12 |
| 6.32.1 Minor bug fixes ..............................                 | 12 |
| 6.33 Omega TK 2.4.5 ...........................................       | 12 |
| 6.33.1 New features ....................................              | 12 |
| 6.34 Omega TK 2.4.4 ...........................................       | 12 |
| 6.34.1 Bug fixes .........................................            | 12 |
| 6.35 Omega TK 2.4.1 ...........................................       | 12 |
| 6.35.1 New features ....................................              | 12 |
| 6.35.2 Bug fixes .........................................            | 12 |
| 6.36 Omega TK 2.4.0 ...........................................       | 12 |
| 6.36.1 New features ....................................              | 12 |
| 6.36.2 Bug fixes .........................................            | 12 |
| 6.37 Omega TK 2.3.3 ...........................................       | 12 |
| 6.37.1 New features ....................................              | 12 |
| 6.37.2 Bug fixes .........................................            | 12 |
| 6.38 Omega TK 2.3.2 ...........................................       | 12 |
| 6.38.1 Bug fixes .........................................            | 12 |
| 6.39 Omega TK 2.3.1 ...........................................       | 12 |
| 6.39.1 New features ....................................              | 12 |
| 6.39.2 Bug fixes .........................................            | 12 |
| 6.40 Omega TK 2.3.0 ...........................................       | 12 |
| 6.40.1 New features ....................................              | 12 |
| 6.40.2 Bug fixes .........................................            | 12 |
| 6.41 Omega TK 2.2.2 ...........................................       | 12 |
| 6.41.1 Bug fixes .........................................            | 12 |
| 6.42 Omega TK 2.2.1 ...........................................       | 12 |
| 6.42.1 Bug fixes .........................................            | 12 |
| 7 Copyright and Trademarks ....................................       | 12 |
| 8 Sample Code ...................................................     | 13 |
| 9 Citation .......................................................... | 13 |
| 9.1 Orion ® Floes .........................................           | 13 |
| 9.2 Toolkits and Applications .............................           | 13 |
| 9.3 OpenEye Web Services .................................            | 13 |
| 10 Technology Licensing ........................................      | 13 |
| 10.1 GCC ......................................................       | 15 |
| 10.1.1 GCC RUNTIME LIBRARY EXCEPTION ..............                   | 15 |
| 10.1.2 GNU GENERAL PUBLIC LICENSE .................                   | 15 |

# **THEORY**

# **1.1 OMEGA Theory**

**OMEGA** is a conformation generator for molecules. **OMEGA** is composed of two main components; model building of molecular fragments and torsion driving. Model generation may be bypassed by importing fragment structures from external sources ([Hawkins-2010], [Stahl-2001], [Stahl-2002]).

**OMEGA** builds initial models of structures by assembling fragment templates along sigma bonds. Input molecules' graphs are fragmented at exocyclic sigma, and carbon to heteroatom acyclic (but not exocyclic) sigma bonds. Conformations for the fragments are either retrieved from pregenerated libraries built with MakeFraglib, or constructed on-the-fly using the same distance constraints followed by the geometry optimization protocol that MakeFraglib uses. Molecule assembly is accomplished by simple vector alignment since all inter-fragment joints are along sigma bonds.

Once an initial model of a structure is constructed, or given as input, OMEGA generates additional models by enumerating ring conformations and invertible nitrogen atoms. Ring conformations are taken from the same fragment library used to build an initial model. OMEGA detaches all exocyclic substituents from a ring system, aligns and attaches them relative to the new ring conformation. OMEGA attempts to generate every possible combination of ring conformations possible for a given structure.

The next step in model generation is to detect and enumerate invertible nitrogens. Nitrogens that have pyramidal geometry, no stereochemistry specified, no more than one hydrogen, are three valent, and have no more than three ring bonds are considered by OMEGA to be invertible. Invertible in this context simply means that at room temperature a pyramidal nitrogen is likely to be able to rapidly (on an NMR timescale) interconvert between two puckered forms. All multiconformer ring models are further expanded by enumerating all possible nitrogen puckers. The resulting model set is the starting point for conformer search by torsion driving.

**OMEGA** begins the torsion search process by examining the molecular graph and determining the bonds that may freely rotate. By default, OMEGA selects acyclic sigma bonds that have at least one non-hydrogen atom attached to each end of the bond. By default, hydrogen rotors (e.g. hydroxyl groups) are not altered during the torsion search; however, this may be enabled as of version 2.5.1. The final ensemble selection is based on RMS distance of heavy atoms and sampled hydrogen atoms; unsampled hydrogen atoms do not affect this RMS distance. A list of possible dihedral angles are then assigned to each rotatable bond. The current mechanism for assignment is based on SMARTS matching, although alternate strategies for assigning angles based on experimental (i.e. X-ray) or theoretical (i.e. fragment optimization studies) are possible. The molecular graph is then subjected to pattern and geometric symmetry detection. Common patterns such as para-disubstituted benzene are used to reduce the number of symmetry equivalent dihedral angles that need to be searched. All torsions are altered by 120 and 180 degrees, and an RMS calculation is performed taking into account symmetry equivalent atoms in order to detect two and three fold symmetries. Exhaustive depth first torsion search is performed on each of the fragments, and the resulting conformers are placed into a list sorted by energy. Entire structures are assembled by combining the lowest energy set of fragments, and then the next lowest set, until the search is terminated. The search will terminate when the limit on the total number of conformers that may be generated is exceeded, the fragment list is exhausted, or the sum of the fragment energies exceeds the energy window of the global minimum structure. The best conformers identified in the torsion search are rank ordered by energy. A final ensemble is selected by sequentially testing the conformers using the RMS distance cutoff. To be accepted in to the final ensemble, a conformer must have an RMS distance to every other member of the ensemble that exceeds the user defined cutoff value. The final ensemble is populated up to the user defined maximum ensemble size limit, or until the list of low energy conformers is exhausted.

Note: Conformers generated from OMEGA with default options do not maintaining input relative stereo chemistry ie. cis/trans for cyclohexane or other cyclic molecules.

# **1.2 Macrocycle Conformations**

Torsion driving conformational sampling methods such as described in the OMEGA Theory section often perform poorly for macrocyclic molecules due to the problem of ring closure after the torsion driving step. Conformational sampling of macrocycles therefore requires a different approach; for example distance geometry (DG) [Crippen-1988], molecular dynamic (MD/LLMOD) [Watts-2014], MD with perturbation along low energy eigenvectors [Labute-2010], or inverse kinematics [Coutsias-2016] have all been applied to this problem.

**OMEGA's** method of conformational sampling of macrocycles is an adaptation of the distance geometry method of Spellmeyer et al. [Spellmeyer-1997]. In this method a traditional embedding DG algorithm is replaced with a direct error function minimization of the random atomic coordinates, followed by force field refinement. Each initial Cartesian atomic coordinate x is assigned by choosing a random number  $r$  between  $-1$  and  $1$ , multiplied by a factor  $f\sqrt{N}$  which determines the box of maximum extent for molecule with N atoms:

$$
x = f\sqrt{N}r\tag{1.1}
$$

Alternatively, instead of randomly placing atoms in Cartesian space, the method allows for random placement of rigid fragments such as aromatic rings, nitro groups etc. After randomly placing molecules atoms or rigid fragments, an error function of the form:

$$
F = \sum_{i,j} (d_{ij} - c_{i,j})^2 + \sum_k V_k
$$
\n(1.2)

is optimized. In the above equation the first sum runs over all pairs of atoms in the molecule, where  $d_{ij}$  are the interatomic distances and  $c_{ij}$  are elements of the constraint matrix respectively; they are obtained from the MMFF94 force field parameters. When atoms  $(i, j)$  are bonded or are the first and last atoms in a bond angle, the upper and lower bounds are the same and are taken as the corresponding equilibrium force field distances. When atoms  $(i,j)$  are the first and last atoms of a torsion angle, the lower bound corresponds to the cis configuration and the upper bound to the trans configuration of those atoms. Finally, when atoms  $(i,j)$  are separated with more than 3 bonds, the lower bound is taken as the sum of the vdW radii and the upper bound as the sum of bond lengths which separate the pair. The second summation in equation  $(1.2)$  is over the tetrahedral constraints which result from:

- 1. planarity
- 2. chirality
- 3. cis-trans isomerism

Optimization of the error function  $(1.2)$  leads to a rough conformation. No hydrogen atoms except those which are bonded to chiral atoms are included in the error function minimization. Each rough conformation is checked for chirality correctness before refinement. If the rough conformation passes the chirality checks it is refined against a forcefield, MMFF94 ([Halgren-I-1996], [Halgren-II-1996], [Halgren-III-1996], [Halgren-IV-1996], [Halgren-V-1996]). Solvent forces can be included in the refinement step using a simple continuum solvation model (the Sheffield model [Grant-2007). When the sequence of random placement followed by error function minimization and force field refinement is repeated for large enough number of times for a given macrocycle, its conformational space is reasonably well covered.

Special measures are taken for zwitterionic molecules (containing both positively and negatively charged groups, e.g.  $CO_2^-$  and  $NH_3^+$ ). In order to prevent possible Coulombic collapse in the absence of a stabilizing receptor, zwitterionic molecules are neutralized before performing the distance geometry calculation and the refined structures are recharged before writing them out. This approach meaningfully improves OMEGA's ability to reproduce solidstate conformations of zwitterionic ligands.

This method of conformation sampling is completely general, and can be used to generate conformations for any molecule, whether or not it contains a large ring. However the 'macrocycle' mode in **OMEGA** has been specifically developed and parameterized to perform well on macrocycles, therefore its performance on linear and small ring molecules is worse than 'classic' OMEGA.

# **GPU-OMEGA**

GPU-Omega refers to the CUDA-enabled GPU implementation of Omega TK. GPU-Omega takes advantage of a GPU during torsion driving for accelerated conformer generation. To make use of GPU-Omega conformer generation please follow the guidelines below.

Attention: GPU-Omega is not available in the C# version of the toolkit.

# 2.1 GPU-Related Requirements

The following is required in order to use GPU-accelerated OpenEye toolkits and applications:

# **2.1.1 Supported Platforms**

CUDA-enabled OpenEye software is only available on supported Linux platforms. For supported Linux platforms see above and/or the Platform Support Page

# **2.1.2 Supported GPUs**

An NVIDIA Tesla, Quadro, or GeForce GPU with a compute capability of 3.5 or higher is required on your system. For a comprehensive table of which GPUs fall into which compute capability category please refer to the CUDA wikipedia page.

# 2.1.3 NVIDIA Drivers

- Minimum NVIDIA Driver version: 450.x.
- CUDA is not required to be installed.

We recommend driver 450.80.02 and we strongly advise manually downloading and installing the appropriate NVidia driver for your system as opposed to using a package manager.

To install, root privilege is required. Follow these steps:

- 1. Download the driver to the machine you are installing it on.
- 2. chmod  $+x$  the driver package to make it executable.

3. Ensure you have disabled X-server by killing any running sessions. Reboot may be required if X-server is still running after this step.

Warning: Disabling X-server requires different processes to be killed depending on your Linux distribution. See Nvidia installation guide for more details.

Warning: The NVidia kernel module can often conflict with the open source Nouveau display drivers depending on your specific Linux distribution. The NVidia documentation is a much more complete and up-to-date source for information on how to work around this issue. See Disabling Nouveau on the NVIDIA website.

4. Install the driver by sudo ./NVIDIA-Linux-x86\_64-450.80.02.run and follow the step-by-step installation instructions.

For more details on driver installations see the CUDA Installation Guide

Note: The output of the nvidia-smi command is extremely useful when debugging GPU issues. Please include the output from nvidia-smi in any request to support@eyesopen.com.

# 2.1.4 Performance Tuning

To get the most performance out of an NVIDIA Graphics card, use the persistence daemon to switch persistence mode on across all cards on the system (root privilege required):

sudo nvidia-persistenced --user foo

This will automatically enable persistence mode after reboot.

For full instructions on persistence daemon see the Persistence daemon section of the NVIDIA docs.

# 2.2 Usage

- GPU-Omega accelerates the torsion driving component of conformer generation in Omega TK and is available through the OEOmega and OETorDriver classes.
- For all torsion driving sampling modes except dense modes, if a GPU is detected at runtime, torsion driving will be carried out on the GPU by default. To turn this feature off use OETorDriveOptions. SetUseGPU.

The following code shows how to turn off GPU-omega prior to conformer generation using sparse mode:

### **Example of turning off GPU-Omega**

```
omegaOpts = oeomega.OEOmegaOptions()
omegaOpts.GetTorDriveOptions().SetUseGPU(False)
omega = oeomeqa. OEOmega (omegaOpts)
omega (mol)
```

- GPU-Omega uses the default OEMMFFSheffieldFFType\_MMFF94Smod\_NOESTAT forcefield. - Tf attempting to use an alternative forcefield conformer generation will fall back to the CPU. GPU-Omega is also incompitable with hydrogen sampling, which is turned off in the default sampling mode. As a result of these, GPU-Omega is not compatible with default settings of OEOmegaSampling Dense sampling mode. To take advantage of a GPU with dense sampling mode set OETorDriveOptions. SetForceField to OEMMFFSheffieldFFType\_MMFF94Smod\_NOESTAT, and set OEMolBuilderOptions. SetSampleHydrogens to False.
- The OEOmegaIsGPUReady utility function is provided for detecting available GPUs on a system.

The following code demonstrates how to query the system for an available GPU and then set the force field to default in order to use the GPU for dense mode conformer generation:

### Example of detecting a GPU and changing the force field for dense mode conformer generation

```
omegaOpts = oeomega.OEOmegaOptions(oeomega.OEOmegaSampling_Dense)
if oeomega.OEOmegaIsGPUReady():
    omegaOpts.GetTorDriveOptions().SetForceField(oeff.
→OEMMFFSheffieldFFType_MMFF94Smod_NOESTAT)
   omegaOpts.GetMolBuilderOptions().SetSampleHydrogens(False)
omega = oeomega. OEOmega (omegaOpts)
omega (mol)
```

• GPU-Omega does not support the distance geometry method of torsion driving and therefore is incompatible with OEMacrocycleOmega.

**Caution:** To use GPU-Omega with child processes a new OEOmega object must be created per child. If attempting to use the same instance of an *OEOmega* object in child processes, conformer generation will fall back to the CPU.

# **THREE**

# **OMEGA EXAMPLES**

The following table lists the currently available Omega TK examples:

| Program                          | Description                                      |
|----------------------------------|--------------------------------------------------|
| <i>simple_omega.py</i>           | generating conformers                            |
| <i>single_conformer.py</i>       | generating a single conformer                    |
| <i>dens_omega.py</i>             | generating densely sampled conformers            |
| <i>stereo_and_torsion.py</i>     | generating stereoisomers                         |
| <i>torsion_drive.py</i>          | torsion driving to generating conformer ensemble |
| <i>make_fraglib.py</i>           | making fragment library                          |
| <i>macrocycle.py</i>             | generating macrocycle conformers                 |
| <i>single_conf_macrocycle.py</i> | generating single macrocycle conformer           |

Note: If the input molecule has SD tag data, the data will be copied to every conformer in the results molecule.

# 3.1 Classic OEOmega Examples

# **3.1.1 Generating Conformers**

The following code example is a simple example of how to generate conformers using the OEOmega object.

## See also:

- OEOmegaOptions class
- OEOmega class
- OESimpleAppOptions class

#### **Listing 1: Generating Conformers**

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
from openeye import oeomega
def main(argv=[_name_]):
    omegaOpts = oeomega.OEOmegaOptions()
    omegaOpts.SetParameterVisibility(oechem.OEParamVisibility_Hidden)
    omegaOpts.SetParameterVisibility("-rms", oechem.OEParamVisibility_Simple)
    omegaOpts.SetParameterVisibility("-ewindow", oechem.OEParamVisibility_Simple)
    \verb+omega0pts. Set Parameter V isibility ("-maxcons",\verb+ochem.OEParamV isibility\_Simple)omegaOpts.SetParameterVisibility("-useGPU", oechem.OEParamVisibility_Simple)
    opts = oechem.OESimpleAppOptions(omegaOpts, "Omega", oechem.OEFileStringType_Mol,
→oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    omegaOpts. UpdateValues (opts)
    omega = oeomega. OEOmega (omegaOpts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    for mol in ifs. GetOEMols () :
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        ret\_code =omega. Build (mol)
        if ret_code == oeomega.OEOmegaReturnCode_Success:
            oechem.OEWriteMolecule(ofs, mol)
        else:
            oechem. OEThrow. Warning ("%s: %s" % (mol. GetTitle (), oeomega.
→OEGetOmegaError(ret_code)))
```

```
return 0
if _name_ = = "_main_".sys.exit(main(sys.argv))
```

# 3.1.2 Generating a Single Conformer

The following code example is a simple example of how to generate a single conformer.

See also:

• OEConformerBuilder class

### **Listing 2: Generating a Single Conformer**

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
from openeye import oeomega
def main(argv=[_name_]):
   if len(argv) != 3:
       oechem.OEThrow.Usage("%s <infile> <outfile>" % argv[0])
   if s = oechem.oemolistream()if not ifs.open(argv[1]):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   ofs = occhem.oemolostream()if not ofs.open(argv[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % argv[2])
    if not oechem. OEIs3DFormat (ofs. GetFormat ()):
        oechem. OEThrow. Fatal ("Invalid output file format for 3D coordinates!")
```

```
builder = oeomega.OEConformerBuilder()
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        ret\_code = builder.Buid(mol)if ret_code == oeomega.OEOmegaReturnCode_Success:
            oechem.OEWriteMolecule(ofs, mol)
        else:oechem. OEThrow. Warning ("%s: %s" % (mol. GetTitle (), oeomega.
→OEGetOmegaError(ret_code)))
   return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# **3.1.3 Generating Densely Sampled Conformers**

The following code example is a simple example of how to generate densely sampled conformers, as used in OE-FreeFormConf calculations, using the OEOmega object.

#### See also:

- OEOmegaOptions class
- OEOmega class
- OEOmegaSampling namespace
- OESimpleAppOptions class

#### **Listing 3: Generating Densely Sampled Conformers**

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
```

```
from openeye import oeomega
def main(argv=[_name_]):
    omegaOpts = oeomega.OEOmegaOptions(oeomega.OEOmegaSampling_Dense)
    omegaOpts.SetParameterVisibility(oechem.OEParamVisibility_Hidden)
    omegaOpts.SetParameterVisibility("-rms", oechem.OEParamVisibility_Simple)
    omegaOpts.SetParameterVisibility("-ewindow", oechem.OEParamVisibility_Simple)
    omegaOpts.SetParameterVisibility("-maxconfs", oechem.OEParamVisibility_Simple)
    omegaOpts.SetParameterVisibility("-useGPU", oechem.OEParamVisibility_Simple)
    omegaOpts.SetParameterVisibility("-searchFF", oechem.OEParamVisibility_Simple)
    opts = oechem.OESimpleAppOptions(omegaOpts, "Omega", oechem.OEFileStringType_Mol,
→oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    omegaOpts.UpdateValues(opts)
    omega = oeomega. OEOmega (omegaOpts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    for mol in ifs. GetOEMols () :
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        ret\_code =omega. Build (mol)
        if ret_code == oeomega.OEOmegaReturnCode_Success:
            oechem.OEWriteMolecule(ofs, mol)
        else:oechem. OEThrow. Warning ("%s: %s" % (mol. GetTitle (), oeomega.
→OEGetOmegaError(ret_code)))
    return <sub>0</sub>if name == " main ":
    sys.exit(main(sys.argv))
```

# **3.2 Flipper Examples**

## **3.2.1 Generating Stereoisomers**

The following code example is a simple example of how to use the OEFlipper function to generate stereoisomers. The code example also demonstrates that stereoisomers should be generated before generating conformers.

See also:

- OEOmegaOptions class
- OEOmega class

- OEFlipper function
- OESimpleAppOptions class

### **Listing 4: Generating Stereoisomers**

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
from openeye import oeomega
def main(argv=[_name_]):
    flipperOpts = oeomega.OEFlipperOptions()
    opts = oechem.OESimpleAppOptions(flipperOpts, "stereo_and_torsion", oechem.
\rightarrowOEFileStringType_Mol, oechem.OEFileStringType_Mol)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    flipperOpts. UpdateValues (opts)
    omega = oeomega. OEOmega ()
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = oechem.oemolostream()
   if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        for enantiomer in oeomega. OEFlipper (mol. GetActive (), flipperOpts):
            fmol = oechem. OEMol (enantiomer)
            ret\_code =omega. Build (fmol)
            if ret code == oeomega.OEOmegaReturnCode Success:
                oechem.OEWriteMolecule(ofs, fmol)
            else:
```

```
oechem.OEThrow.Warning("%s: %s" %
                                              (fmol.GetTitle(), oeomega.OEGetOmegaError(ret_
\leftarrowcode)))
    return <sub>0</sub>if _name_
            = "__main__- n +
    sys.exit(main(sys.argv))
```

# 3.3 Generating Torsion Driven Conformation Examples

### 3.3.1 Torsion Driving to Generating Conformer Ensemble

The following code example is a simple example of how to torsion drive from given 3D structure, to generate a conformer ensemble.

#### See also:

- OETorDriveOptions class
- OETorDriver class
- OESimpleAppOptions class

#### **Listing 5: Torsion Driving to Generating Conformer Ensemble**

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
from openeye import oeomega
def main(argv=[_name_]):
    torOpts = oeomega.OETorDriveOptions()
    torOpts.SetParameterVisibility(oechem.OEParamVisibility_Hidden)
```

```
(continued from previous page)
```

```
torOpts.SetParameterVisibility("-rms", oechem.OEParamVisibility_Simple)
    torOpts.SetParameterVisibility("-ewindow", oechem.OEParamVisibility_Simple)
    torOpts.SetParameterVisibility("-maxconfs", oechem.OEParamVisibility_Simple)
    opts = oechem.OESimpleAppOptions(torOpts, "Omega", oechem.OEFileStringType_Mol,
→oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   torOpts.UpdateValues(opts)
   tordriver = oeomega.OETorDriver(torOpts)
   if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        ret_code = tordriver.GenerateConfs(mol)
        if ret_code == oeomega.OEOmegaReturnCode_Success:
            oechem.OEWriteMolecule(ofs, mol)
        else:
           oechem.OEThrow.Warning("%s: %s" % (mol.GetTitle(), oeomega.
\rightarrowOEGetOmegaError(ret code)))
    return 0if name == "_main_":
    sys.exit(main(sys.argv))
```

# 3.4 Fragment Library generation Examples

# **3.4.1 Making Fragment Library**

The following code example is a simple example of how to generate a fragment library.

### See also:

- OEFragBuilderOptions class
- OEMakeFragLib class
- OESimpleAppOptions class

### **Listing 6: Making Fragment Library**

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
from openeye import oeomega
def main(argv=[_name_]):
    libOpts = oeomega.OEFragBuilderOptions()
    libOpts.SetParameterVisibility(oechem.OEParamVisibility_Hidden)
    libOpts.SetParameterVisibility("-buildFF", oechem.OEParamVisibility_Simple)
    opts = oechem.OESimpleAppOptions(libOpts, "Makefraglib", oechem.OEFileStringType_
\rightarrowMol, oechem.OEFileStringType_Mol3D)
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   libOpts.UpdateValues(opts)
   makefraglib = oeomega. 0EMakeFraqlib (libOrts)if s = oechem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    if ofs. GetFormat() != oechem. OEFormat_OEB:
        oechem. OEThrow. Fatal ("Output file has to have OEB format!")
   makefraglib.ClearFragLibs()
   makefraglib.GenerateMissingFrags(ifs, ofs)
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# **3.5 Macrocycle Examples**

## **3.5.1 Generating Macrocycle Conformers**

The following code example is a simple example of how to generate conformers using the OEMacrocycleOmega object.

#### See also:

- OEMacrocycleOmegaOptions class
- OEMacrocycleOmega class
- OESimpleAppOptions class

#### **Listing 7: Generating Macrocycle Conformers**

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
from openeye import oeomega
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    omegaOpts = oeomega.OEMacrocycleOmegaOptions()
    omegaOpts.SetParameterVisibility(oechem.OEParamVisibility_Hidden)
    omegaOpts.SetParameterVisibility("-rms", oechem.OEParamVisibility_Simple)
    omegaOpts.SetParameterVisibility("-ewindow", oechem.OEParamVisibility_Simple)
    omegaOpts.SetParameterVisibility("-maxconfs", oechem.OEParamVisibility_Simple)
   opts = oechem.OESimpleAppOptions(omegaOpts, "Omega", oechem.OEFileStringType_Mol,
→oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts (opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    omegaOpts. UpdateValues (opts)
    mcomega = oeomega.OEMacrocycleOmega(omegaOpts)
    if s = oechem. oemolistream()
```

```
if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = oechem.oemolostream()
    if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        ret\_code = mcomeqa.Buid(mol)if ret_code == oeomega.OEOmegaReturnCode_Success:
            oechem.OEWriteMolecule(ofs, mol)
        else:oechem. OEThrow. Warning ("%s: %s" % (mol. GetTitle (), oeomega.
\rightarrowOEGetOmegaError(ret code)))
    return 0
if _name_ == " _main
                         \mathbf{m}_2sys.exit(main(sys.argv))
```

## 3.5.2 Generating a Single Macrocycle Conformer

The following code example is a simple example of how to generate a single macrocycle conformer using the OEMacrocycleBuilder object.

#### See also:

- OEMacrocycleBuilderOptions class
- OEMacrocycleBuilder class
- OESimpleAppOptions class

#### **Listing 8: Generating a Single Macrocycle Conformer**

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
from openeye import oeomega
def main(argv=[__name__]):
    buildOpts = oeomega.OEMacrocycleBuilderOptions()
    buildOpts.SetParameterVisibility(oechem.OEParamVisibility_Hidden)
   buildOpts.SetParameterVisibility("-seed", oechem.OEParamVisibility_Simple)
   buildOpts.SetParameterVisibility("-dielectric_constant", oechem.OEParamVisibility_
\rightarrowSimple)
   inType = oechem.OEFileStringType_Mol
   outType = oechem.OEFileStringType_Mol3D
   opts = oechem. OESimpleAppOptions (buildOpts, "macrocycle_builder", inType, outType)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   buildOpts. UpdateValues (opts)
    #builder = oeomega.OEMacrocycleBuilder(buildOpts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        itlimit = 1000itnum = 0ret_code = oeomega.OEOmegaReturnCode_Failed
        while itnum \leq itlimit:
            builder = oeomega.OEMacrocycleBuilder(buildOpts)
            ret\_code = builder.Buid(mol)if ret_code == oeomega.OEOmegaReturnCode_Success:
                oechem.OEWriteMolecule(ofs, mol)
                break
            else:
                buildOpts.SetRandomSeed(buildOpts.GetRandomSeed()+1)
            ++itnum
        if ret_code != oeomega.OEOmegaReturnCode_Success:
            oechem. OEThrow. Warning ("%s: %s" % (mol. GetTitle (), oeomega.
→OEGetOmegaError(ret_code)))
    return 0
if __name__ == "_main_":
   sys.exit(main(sys.argv))
```

# **FOUR**

**API** 

# **4.1 OEConfGen Classes**

## 4.1.1 OEBuilderBase

### class OEBuilderBase

This is an abstract base class for structure builder classes that uses fragment library.

#### The OEBuilderBase class defines the following public methods:

- · AddFragLib
- · ClearFragLibs

#### The following classes derive from this class:

- OEMakeFragLib
- OEMolBuilder

### **AddFragLib**

```
bool AddFraqLib()
bool AddFragLib(const std::string &)
bool AddFragLib(OEPlatform::oeistream &)
```

Adds a fragment library to be used for pre-generated fragment coordinates. When the OEBuilderBase. AddFragLib is called without a parameter, the built-in fragments library is loaded immediately. By default, the built-in fragment library does not load until it is required in use for the first time.

The string and oeistream versions of OEBuilderBase. AddFragLib can be used to add external fragments libraries. These external libraries are used in addition to the *built-in* one. Returns True if the fragment library is added successfully.

### See also:

· OEBuilderBase. ClearFragLibs method.

### **ClearFragLibs**

```
void ClearFragLibs()
```

Clears all fragment libraries from the builder.

#### See also:

· OEBuilderBase. AddFragLib method.

# **4.1.2 OEConfFixOptions**

```
class OEConfFixOptions : public OESystem: : OEOptions
```

This class provides an interface to setup options required for constraining a fragment of the molecules during conformational search.

There are multiple ways to define the substructure for defining the constraints.

- The first is to provide a substructure query using the command  $SetFixSubSearch$ . If the input query pattern is 3D the corresponding substructure of the target is fixed to the query coordinates. For a non-3D query, the mapped substructure of an input 3D target is fixed, provided that  $SetIncludeInput$  is set to true.
- The second method is to pass in a 3D structure using the command  $SetFixMOL$ . The  $SetFixDeletEH$ command can be used to control whether hydrogens should be retained or discarded from the FixMol. The corresponding substructure of the target has the atom coordinates fixed to those from the *FixMol*.
- The third method is to provide a SMARTS pattern using the command  $SetFixSmarts$ . The SMARTS pattern is matched against the input molecule to identify a substructure, provided that the input molecule is 3D and that Set Include Input is set to true. The corresponding substructure of the target is fixed during the conformer generation.
- The fourth method is to provide both a FixMol using the command  $SetFixMol$ , and a SMARTS string using the command  $SetFixSmarts$ . In this case, the SMARTS pattern is matched against the FixMol structure to identify a substructure of the  $FixMol$ . The corresponding substructure of the target is fixed to the coordinates of the FixMol substructure during conformer generation.
- The fifth method is to provide both a FixMol using the command  $SetFixMod$ , and turn on MCS based fix using the command  $SetFixMCS$ . In this case, the maximum common substructure matched against the FixMol structure to identify a substructure of the *FixMol*. The corresponding substructure of the target is fixed to the coordinates of the *FixMol* substructure during conformer generation.
- The final method is to provide an atom predicate using the command  $SetFixPredict$  which is used to identify target atoms to be fixed.

For all the above methods, the initialization of the substructure, when applicable, can be controlled using SetAtomExpr and SetBondExpr.

The unique match flag defined using SetFixUniqueMatch applies to all substructure matches performed, either during creation of molecule fragments or when applying the actual constraints.

The MaxMatch defines how many of the matches found during constraint application should be applied, and can be set using the command  $SetFixMaxMatch$ . If the constraining fragment substructure appears twice in the target molecule and the *MaxMatch* is set to 2 or more, the molecule would be constrained to the substructure coordinates twice for each of the generated conformers and could result in twice the number of conformers compared to setting this value to 1.

In all cases the constraints are evaluated by the proximity between the initial generated structure of the molecule and the coordinates of the constraining substructure. The precision of the proximity evaluation can be controlled by an RMS value set using SetFixRMS.

### See also:

- OEMolBuilder class
- OETorDriver class

#### The OEConfFixOptions class defines the following public methods:

- · GetAtomExpr and SetAtomExpr
- · GetBondExpr and SetBondExpr
- · GetFixDeleteH and SetFixDeleteH
- GetFixMaxMatch and SetFixMaxMatch
- GetFixMCS and SetFixMCS
- · GetFixMol and SetFixMol
- · GetFixPredicate and SetFixPredicate
- GetFixRMS and SetFixRMS
- GetFixSmarts and SetFixSmarts
- GetFixSubSearch and SetFixSubSearch
- · GetFixUniqueMatch and SetFixUniqueMatch
- · HasFixPattern
- · GetMCSMinAtoms and SetMCSMinAtoms
- · GetMCSFunc and SetMCSFunc
- · GetMCSType and SetMCSType

### **Constructors**

```
OEConfFixOptions()
OEConfFixOptions (const OEConfFixOptions &)
```

Default and copy constructors.

#### operator=

OEConfFixOptions & operator= (const OEConfFixOptions &)

Assignment operator.

# 4.1.3 GetAtomExpr

unsigned GetatomExpr() const

See SetAtomExpr method.

# 4.1.4 GetBondExpr

unsigned GetBondExpr() const

See SetBondExpr method.

# 4.1.5 GetFixDeleteH

bool GetFixDeleteH() const

See SetFixDeleteH method.

# 4.1.6 GetFixMaxMatch

unsigned int GetFixMaxMatch() const

See SetFixMaxMatch method.

# **4.1.7 GetFixMCS**

bool GetFixMCS() const

See SetFixMCS method.

# 4.1.8 GetFixMol

const OEChem:: OEMolBase& GetFixMol() const

See SetFixMol method.

# 4.1.9 GetFixPredicate

const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>\* GetFixPredicate() const

See SetFixPredicate method.

# 4.1.10 GetFixRMS

double GetFixRMS() const

See SetFixRMS method.

# 4.1.11 GetFixSmarts

const std:: string& GetFixSmarts() const

See SetFixSmarts method.

# 4.1.12 GetFixSubSearch

const OEChem:: OESubSearch & GetFixSubSearch() const

Returns the substructure search (OESubSearch) for fixed fragments.

# 4.1.13 GetFixUniqueMatch

bool GetFixUniqueMatch() const

See SetFixUniqueMatch method.

# **4.1.14 GetMCSMinAtoms**

unsigned GetMCSMinAtoms () const

See SetMCSMinAtoms method.

# 4.1.15 GetMCSFunc

const OEChem:: OEMCSFunc\* GetMCSFunc () const

See SetMCSFunc method.

## 4.1.16 GetMCSType

unsigned GetMCSType () const

See SetMCSType method.

# 4.1.17 HasFixPattern

bool HasFixPattern() const

Method checks if a criterion for fixing a portion of the molecule, during conformation search, is currently set.

# 4.1.18 SetAtomExpr

bool SetAtomExpr (const unsigned)

Sets the atom expression to be used for substructure initialization from a molecule fragment. Default: OEExprOpts\_DefaultAtoms

#### See also:

· OEExprOpts namespace

# 4.1.19 SetBondExpr

bool SetBondExpr (const unsigned)

Sets the bond expression to be used for substructure initialization from a molecule fragment. Default: OEExprOpts\_DefaultBonds

#### See also:

· OEExprOpts namespace

## 4.1.20 SetFixDeleteH

bool SetFixDeleteH (const bool)

Sets whether hydrogens should be stripped from the fix molecule before it is used to match structures. Default: True.

# 4.1.21 SetFixMaxMatch

bool SetFixMaxMatch (const unsigned int)

Sets the maximum number of substructure search matches to be used for constraining molecule fragments. Default: 1.

## 4.1.22 SetFixMol

```
bool SetFixMol(const OEChem:: OEMolBase&)
bool SetFixMol(OEChem::oemolistream& fstream)
```

Uses the 3D coordinates of the provided molecule to fix the corresponding substructure in the target molecule during conformation generation. For the second overload, only the first molecule from the input oemolistream is used.

## 4.1.23 SetFixMCS

```
bool SetFixMCS (const bool)
```

Sets flag to use MCS to fix a portion of the molecule during conformation search. If set to true, maximum common substructure against the FixMol is used to define the portion of the molecule to be kept fixed. Default: false.

# 4.1.24 SetFixPredicate

bool SetFixPredicate(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>&)

Uses the **atom predicate** to define which atoms should be kept fixed during conformation search.

# 4.1.25 SetFixRMS

bool SetFixRMS (const double)

Sets the RMS distance (Root Mean Square (RMS) Cartesian) below which two atom positions are treated as identical. Default: 0.15.

## 4.1.26 SetFixSmarts

```
bool SetFixSmarts (const std::string&)
```

Uses the SMARTS pattern to define which portion of the molecule should be kept fixed during conformation search.

# 4.1.27 SetFixSubSearch

bool SetFixSubSearch (const OEChem:: OESubSearch&)

Uses the substructure search (OESubSearch) to define which portion of the molecule should be kept fixed during conformation search.

### 4.1.28 SetFixUniqueMatch

bool SetFixUniqueMatch (const bool)

Sets whether only the **unique** substructure matches should be used for coordinate replacement. **Default:** True.

## 4.1.29 SetMCSMinAtoms

bool SetMCSMinAtoms (const unsigned)

Sets the minimum number of atoms required of a subgraph match to be used for MCS based fix. Default: 1

### 4.1.30 SetMCSFunc

bool SetMCSFunc (const OEChem:: OEMCSFunc&)

Sets the scoring function to be used for subgraph matching for MCS based fix. Default: OEMCSMaxBondsCompleteCycles

## 4.1.31 SetMCSType

bool SetMCSType (const unsigned)

Sets the MCS search type to be used for subgraph matching for MCS based fix, defined in OEMCSType namespace. Default: OEMCSType\_Exhaustive

## 4.1.32 OEConformerBuilder

class OEConformerBuilder

This class defines an interface for generating 3D structures of small molecules. This class differs from OEMolBuilder in that it makes an effort to ensure that the generated conformer is clash free. However, this is faster than OEOmega for generating a single conformer, as this method does not search for the lowest energy conformer.

#### **Code Examples**

```
• Generating a Single Conformer example
```

The OEConformerBuilder class defines the following public methods:

 $\bullet$  Build

### **Constructors**

```
OEConformerBuilder()
OEConformerBuilder (const OEConformerBuilder&)
```

Default and copy constructors.

#### operator=

OEConformerBuilder &operator=(const OEConformerBuilder&)

Assignment operator.

#### **Build**

```
unsigned Build (OEChem:: OEMolBase&) const
unsigned Build (OEChem:: OEMCMolBase&) const
```

Generates a 3D structure of a small molecule. Returns OEOmegaReturnCode\_Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace.

# 4.1.33 OEConfSlicer

```
class OEConfSlicer
```

This class defines an interface for reducing the number of conformers in a molecule by detecting duplicates. This allows for OEOmega to generate a very large ensemble with much looser deduplication parameters, and then to "slice" that ensemble of conformations by various different parameters after the fact.

#### See also:

- OESliceEnsembleOptions class
- · OESliceEnsemble method

The OEConfSlicer class defines the following public methods:

 $\bullet$  Slice

### **Constructors**

```
OEConfSlicer()
{\tt OECDfSliceer}({\tt const} \ {\tt OESliceEnsembleOptions@})OEConfSlicer (const OEConfSlicer&)
```

Default and copy constructors.

#### operator=

```
OEConfSlicer & operator=(const OEConfSlicer&)
```

Assignment operator.

### **Slice**

**bool** Slice (OEChem:: OEMCMolBase&)

Slice the input molecule to remove duplicates.

# 4.1.34 OEFlipperClassicOptions

class OEFlipperClassicOptions : public OEFlipperOptions

Caution: This is a deprecated API.

This class was introduced to allow validation of previous flipper results against the preferred updated flag options. It will be removed in a subsequent release.

### See also:

- OEFlipperOptions class
- OEFlipper function

#### The OEFlipperClassicOptions class defines the following public methods:

- · GetAtomPredicate and SetAtomPredicate
- · GetBondPredicate and SetBondPredicate
- · GetEnhancedStereo and SetEnhancedStereo
- · GetEnumBridgehead and SetEnumBridgehead
- · GetEnumEZ and SetEnumEZ
- GetEnumNitrogen and SetEnumNitrogen
- · GetEnumRS and SetEnumRS
- · GetEnumSpecifiedStereo and SetEnumSpecifiedStereo
- GetMaxCenters and SetMaxCenters
- GetWarts and SetWarts

### **Constructors**

```
OEFlipperClassicOptions()
OEFlipperClassicOptions (const OEFlipperClassicOptions &)
```

Default and copy constructors.

#### operator=

OEFlipperClassicOptions & operator= (const OEFlipperClassicOptions &)

Assignment operator.

#### **GetAtomPredicate**

const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>\* GetAtomPredicate() const

See SetAtomPredicate method.

#### **GetBondPredicate**

const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase>\* GetBondPredicate() const

See SetBondPredicate method.

### **GetEnhancedStereo**

bool GetEnhancedStereo() const

See SetEnhancedStereo method.

#### **GetEnumBridgehead**

```
bool GetEnumBridgehead() const
```

See SetEnumBridgehead method.

#### **GetEnumEZ**

bool GetEnumEZ () const

See SetEnumEZ method.

### **GetEnumNitrogen**

bool GetEnumNitrogen() const

See SetEnumNitrogen method.

#### **GetEnumRS**

bool GetEnumRS() const

See SetEnumRS method.

### **GetEnumSpecifiedStereo**

bool GetEnumSpecifiedStereo() const

See SetEnumSpecifiedStereo method.

### **GetMaxCenters**

unsigned GetMaxCenters() const

See SetMaxCenters method.

#### **GetWarts**

bool GetWarts () const

See SetWarts method.

#### **SetAtomPredicate**

**bool** SetAtomPredicate(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>&)

Provides an input atom predicate to define the selection of the atom stereocenters which should be enumerated. For explicit user predicates, the bond predicate must also be provided explicitly, see SetBondPredicate method.

### **SetBondPredicate**

**bool** SetBondPredicate(const OESystem::OEUnaryPredicate<OEChem::OEBondBase>&)

Provides an input bond predicate to define the selection of the bond stereocenters which should be enumerated. For explicit user predicates, the atom predicate must also be provided explicitly, see  $SetAtomPredict$  cate method.

### **SetEnhancedStereo**

bool SetEnhancedStereo (const bool)

Sets whether to consider explicit MDL enhanced stereogroups during flipping or not. Enhanced stereogroups generally contain a collection of stereocenters which should be considered as a collective unit, where a 'flip' implies that all centers in the group should be flipped, thus retaining the relative stereo parity between the grouped stereocenters. With this flag enabled, far fewer enantiomers will be generated than for individual stereocenter flipping activities, and relative stereo configurations will be retained. When enabled, explicitly marked absolute stereocenters are excluded from the flipping activities. Default: False.

Note: The membership and type of existing enhanced stereogroups are not modified as a result of the flipping operation. That is, explicit stereogroups of and and  $\circ$ r are not promoted to abs groups as a result of stereocenter parity flips. This retains the source of original stereogroup(s) in the generated isomer(s) for post-flipping validations and processing. This behavior is true regardless of the setting of GetEnhancedStereo. Stereocenters can be explicitly promoted to abs centers by deletion of all stereogroups, or deleting all stereogroups and adding marked stereocenters to a single new abs stereogroup.

#### See also:

- GetGroups method
- · OEIsMDLStereoGroup class

### **SetEnumBridgehead**

bool SetEnumBridgehead (const bool)

Sets whether to enumerate bridgehead stereocenters or not. Default: False.

#### **SetEnumEZ**

bool SetEnumEZ (const bool)

Sets whether to enumerate only E/Z stereocenters or not. If  $\text{true}$ , no atoms are enumerated. Default: False.

#### SetEnumNitrogen

bool SetEnumNitrogen (const bool)

Controls the behavior with respect to enumeration of nonterminal nitrogens. Any nitrogen with pyramidal geometry in the initial model of the input molecule, and having no more than two ring bonds is considered to be 'invertible'. Will enumerate all possible puckers if set to true. Default: False.

### **SetEnumRS**

bool SetEnumRS (const bool)

Sets whether to enumerate only R/S stereocenters or not. If  $\text{true}$ , no bonds are enumerated. Default: False.

#### **SetEnumSpecifiedStereo**

bool SetEnumSpecifiedStereo (const bool)

Sets whether to force the modification of all of the stereocenters in a molecule or not. If false, will only enumerate stereocenters which do not already have a specified stereochemistry. Default: False.

#### **SetMaxCenters**

bool SetMaxCenters (const unsigned)

Sets the maximum number of stereocenters or groups of stereocenters which will be fully enumerated. Default: 12.

#### **SetWarts**

bool SetWarts (const bool)

Sets whether to generate unique titles for molecules. Default: False.

## 4.1.35 OEFlipperOptions

class OEFlipperOptions : public OESystem: : OEOptions

#### See also:

• OEFlipper function

#### **Code Examples**

• Generating Stereoisomers example

#### The OEFlipperOptions class defines the following public methods:

- · GetAtomPredicate and SetAtomPredicate
- · GetBondPredicate and SetBondPredicate
- · GetEnhancedStereo and SetEnhancedStereo
- GetEnumAtoms and SetEnumAtoms
- · GetEnumAtomSpecifiedStereo and SetEnumAtomSpecifiedStereo
- GetEnumBonds and SetEnumBonds
- GetEnumBondSpecifiedStereo and SetEnumBondSpecifiedStereo
- · GetEnumBridgehead and SetEnumBridgehead

- · GetEnumEZ and SetEnumEZ
- · GetEnumNitrogen and SetEnumNitrogen
- · GetEnumRS and SetEnumRS
- · GetEnumSpecifiedStereo and SetEnumSpecifiedStereo
- GetEnumRelativeAtomStereo and SetEnumRelativeAtomStereo
- · GetMaxCenters and SetMaxCenters
- · GetWarts and SetWarts

### **Constructors**

```
OEFlipperOptions()
OEFlipperOptions (const OEFlipperOptions &)
```

Default and copy constructors.

#### operator=

OEFlipperOptions & operator= (const OEFlipperOptions &)

Assignment operator.

#### **GetAtomPredicate**

const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>\* GetAtomPredicate() const

See SetAtomPredicate method.

### **GetBondPredicate**

const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase>\* GetBondPredicate() const

See SetBondPredicate method.

### **GetEnhancedStereo**

bool GetEnhancedStereo() const

See SetEnhancedStereo method.

### **GetEnumAtoms**

bool GetEnumAtoms () const

See Set EnumAtoms method.

### **GetEnumAtomSpecifiedStereo**

bool GetEnumAtomSpecifiedStereo() const

See SetEnumAtomSpecifiedStereo method.

### **GetEnumBonds**

bool GetEnumBonds () const

See SetEnumBonds method.

### **GetEnumBondSpecifiedStereo**

bool GetEnumBondSpecifiedStereo() const

See SetEnumBondSpecifiedStereo method.

### **GetEnumBridgehead**

bool GetEnumBridgehead() const

See SetEnumBridgehead method.

### **GetEnumEZ**

bool GetEnumEZ() const

See Set EnumEZ method.

### **GetEnumNitrogen**

bool GetEnumNitrogen() const

See SetEnumNitrogen method.

### **GetEnumRS**

bool GetEnumRS() const

See Set EnumRS method.

#### **GetEnumRelativeAtomStereo**

bool GetEnumRelativeAtomStereo() const

See SetEnumRelativeAtomStereo method.

### **GetEnumSpecifiedStereo**

bool GetEnumSpecifiedStereo() const

See SetEnumSpecifiedStereo method.

### **GetMaxCenters**

unsigned GetMaxCenters() const

See SetMaxCenters method.

### **GetWarts**

bool GetWarts () const

See SetWarts method.

#### **SetAtomPredicate**

**bool** SetAtomPredicate(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>&)

Provides an input atom predicate to define the selection of the atom stereocenters which should be enumerated.

#### **SetBondPredicate**

**bool** SetBondPredicate(const OESystem::OEUnaryPredicate<OEChem::OEBondBase>&)

Provides an input bond predicate to define the selection of the bond stereocenters which should be enumerated.

### **SetEnhancedStereo**

```
bool SetEnhancedStereo (const bool)
```

Sets whether to consider explicit MDL enhanced stereogroups during flipping or not. Enhanced stereogroups generally contain a collection of stereocenters which should be considered as a collective unit, where a 'flip' implies that all centers in the group should be flipped, thus retaining the relative stereo parity between the grouped stereocenters. With this flag enabled, far fewer enantiomers will be generated than for individual stereocenter flipping activities, and relative stereo configurations will be retained. When enabled, explicitly marked absolute stereocenters are excluded from the flipping activities. Care should be taken to ensure that any custom atom predicate returns all atoms involved in enhanced stereogroups. Default: False.

Note: The membership and type of existing enhanced stereogroups are not modified as a result of the flipping operation. That is, explicit stereogroups of and and or are not promoted to abs groups as a result of stereocenter parity flips. This retains the source of original stereogroup(s) in the generated isomer(s) for post-flipping validations and processing. This behavior is true regardless of the setting of GetEnhancedStereo. Stereocenters can be explicitly promoted to abs centers by deletion of all stereogroups, or deleting all stereogroups and adding marked stereocenters to a single new abs stereogroup.

#### See also:

- · GetGroups method
- · OEIsMDLStereoGroup class

### **SetEnumAtoms**

bool SetEnumAtoms (const bool)

Sets whether to include R/S stereocenters in the enumeration or not. If false, disregards atom enumerations. Default: True.

#### **SetEnumAtomSpecifiedStereo**

bool SetEnumAtomSpecifiedStereo (const bool)

Sets whether to force the modification of all of the R/S stereocenters in a molecule or not. If false, will only enumerate stereocenters which do not already have a specified stereochemistry. Default: False.

### **SetEnumBonds**

```
bool SetEnumBonds (const bool)
```

Sets whether to include E/Z bonds in the enumeration or not. If false, disregards bond enumerations. Default: True.

### **SetEnumBondSpecifiedStereo**

bool SetEnumBondSpecifiedStereo (const bool)

Sets whether to force the modification of all of the E/Z stereocenters in a molecule or not. If false, will only enumerate bonds which do not already have a specified stereochemistry. Default: False.

### **SetEnumBridgehead**

bool SetEnumBridgehead (const bool)

Sets whether to enumerate bridgehead stereocenters or not. Default: False.

### **SetEnumEZ**

bool SetEnumEZ (const bool)

Sets whether to enumerate E/Z stereocenters or not. Default: True.

#### SetEnumNitrogen

bool SetEnumNitrogen (const bool)

Controls the behavior with respect to enumeration of nonterminal nitrogens. Any nitrogen with pyramidal geometry in the initial model of the input molecule, and having no more than two ring bonds is considered to be 'invertible'. Will enumerate all possible puckers if set to true. Default: False.

#### **SetEnumRS**

bool SetEnumRS (const bool)

Sets whether to enumerate R/S stereocenters or not. Default: True.

### **SetEnumRelativeAtomStereo**

```
bool SetEnumRelativeAtomStereo (const bool)
```

Sets whether to include enumeration of internally perceived relative atom sterecenters (e.g., 1,4-disubstituted cyclohexanes) in a molecule or not. If true, consider relative stereocenters during stereoenumeration. Default: False.

### **SetEnumSpecifiedStereo**

bool SetEnumSpecifiedStereo (const bool)

Sets whether to force the modification of all of the atom and bond stereocenters in a molecule or not. If false, will only enumerate stereocenters which do not already have a specified stereochemistry. Default: False.

### **SetMaxCenters**

bool SetMaxCenters (const unsigned)

Sets the maximum number of stereocenters or groups of stereocenters which will be fully enumerated. Default: 12.

### **SetWarts**

```
bool SetWarts (const bool)
```

Sets whether to generate unique titles for molecules. Default: False.

# 4.1.36 OEFragBuilder

class OEFragBuilder

This class defines an interface for generating 3D structure of molecule fragments using a distance geometry based algorithm. A fragment is a building block that is used for initial 3D structure generation of molecules.

#### See also:

OEFragBuilderOptions class

The OEFragBuilder class defines the following public methods:

- $\bullet$  Build
- · GetOptions and SetOptions

### **Constructors**

```
OEFragBuilder()
{\tt OEFragBuilder}({\tt const\;\;OEFragBuilderOptions\&}){\tt OEFragBuidder}({\tt const\;\;OEFragBuider\&})
```

Default and copy constructors.

#### operator=

OEFragBuilder & operator=(const OEFragBuilder&)

Assignment operator.

# **4.1.37 Build**

unsigned Build (OEChem:: OEMCMolBase&) const

Generates 3D structures for a molecule fragment. Returns OEOmegaReturnCode\_Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace.

## 4.1.38 GetOptions

const OEFraqBuilderOptions& GetOptions() const

See SetOptions method.

## 4.1.39 SetOptions

void SetOptions (const OEFragBuilderOptions&)

Sets options for building the fragment structures. Default: OEFragBuilderOptions with OEFragBuilderMode Default mode.

#### See also:

• OEFragBuilderOptions class

## 4.1.40 OEFragBuilderOptions

class OEFragBuilderOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for generating fragment coordinates for different types of fragments. A fragment is a building block that is used for initial 3D structure generation of molecules.

See also:

- OEMolBuilderOptions class
- OEFragOptions class
- OERingFragOptions class

### **Code Examples**

• Making Fragment Library example

#### The OEFragBuilderOptions class defines the following public methods:

• GetForceField and SetForceField

- GetMacroCycOptions and SetMacroCycOptions
- · GetNonRingOptions and SetNonRingOptions
- · GetRingOptions and SetRingOptions

#### **Constructors**

OEFragBuilderOptions (const unsigned int mode = OEFragBuilderMode::Default)

The mode parameter defines the fragment build modes from the OEFragBuilderMode namespace. Default: OEFragBuilderMode\_Default.

#### See also:

· OEFragBuilderMode namespace

OEFragBuilderOptions (const OEFragBuilderOptions &)

#### Copy constructor.

#### operator=

OEFragBuilderOptions & operator= (const OEFragBuilderOptions &)

Assignment operator.

#### **GetForceField**

const OEForceField\* GetForceFieldType() const

See SetForceField method.

#### **GetMacroCycOptions**

```
OEFragOptions& GetMacroCycOptions()
const OEFragOptions& GetMacroCycOptions() const
```

See SetMacroCycOptions method.

### **GetNonRingOptions**

```
OEFragOptions& GetNonRingOptions()
const OEFragOptions& GetNonRingOptions() const
```

See SetNonRingOptions method.

### **GetRingOptions**

```
OERingFragOptions& GetRingOptions()
const OERingFragOptions& GetRingOptions() const
```

See SetRingOptions method.

#### **SetForceField**

```
bool SetForceField (const unsigned)
bool SetForceField(const std::string&)
```

Sets the force field used for torsion driving. The first overload takes an *unsigned* from the OEMMFFSheffieldFFType namespace, and the second overload takes corresponding string val-Method returns false when the invalid selection is chosen, true otherwise. Default: ues. OEMMFFSheffieldFFType\_MMFF\_NOESTAT

### **SetMacroCycOptions**

**void** SetMacroCycOptions (const OEFragOptions&)

Sets *options* related to building macrocycle fragments.

#### See also:

• OEFragOptions class

### **SetNonRingOptions**

void SetNonRingOptions (const OEFragOptions&)

Sets *options* related to building general fragments that are not rings.

#### See also:

• OEFragOptions class

### **SetRingOptions**

void SetRingOptions (const OERingFragOptions&)

Sets *options* related to building ring fragments.

#### See also:

• OERingFragOptions class

# 4.1.41 OEFragOptions

#### class OEFragOptions

This class provides an interface to setup options required for generating fragment coordinates, for a specific type of fragment. A fragment is a building block that is used for initial 3D structure generation of molecules.

#### See also:

• OEFragBuilderOptions class

The OEFragOptions class defines the following public methods:

- · GetEnergyWindow and SetEnergyWindow
- · GetFragGen and SetFragGen
- GetFragKeep and SetFragKeep
- · GetRMS and SetRMS
- · GetTimeLimit and SetTimeLimit

### **Constructors**

```
OEFragOptions()
OEFragOptions (const OEFragOptions &)
```

Default and copy constructors.

#### operator=

```
OEFragOptions & operator=(const OEFragOptions &)
```

Assignment operator.

# 4.1.42 GetEnergyWindow

double GetEnergyWindow() const

See SetEnergyWindow method.

# 4.1.43 GetFragGen

unsigned int GetFragGen() const

See SetFragGen method.

## 4.1.44 GetFragKeep

unsigned int GetFragKeep() const

See SetFragKeep method.

## **4.1.45 GetRMS**

double GetRMS() const

See SetRMS method.

# 4.1.46 GetTimeLimit

double GetTimeLimit() const

See Set TimeLimit method.

# 4.1.47 SetEnergyWindow

bool SetEnergyWindow (const double)

Sets the maximum allowable energy difference between the lowest and the highest energy fragment conformers, in units of kcal/mol. Default: 8.0 kcal/mol.

# 4.1.48 SetFragGen

bool SetFragGen (const unsigned int)

Sets the maximum number of fragment conformers to generate, in obtaining the ensemble of fragment conformers. Default: 40.

# 4.1.49 SetFragKeep

bool SetFragKeep (const unsigned int)

Sets the maximum number of fragments to keep, from the generated ensemble. Default: 1.

# **4.1.50 SetRMS**

bool SetRMS (const double)

Sets the RMS distance (Root Mean Square Cartesian distance) below which two conformers are treated as duplicates. Default: 0.1.

# 4.1.51 SetTimeLimit

bool SetTimeLimit (const double)

Sets the maximum allowable time for generating conformers of a fragment, in units of seconds. Default: 300.0 s.

# 4.1.52 OEMacrocycleBuilder

```
class OEMacrocycleBuilder
```

This class defines an interface for generating 3D structure of macrocycle molecules. Macrocycle structures are generated by first creating an initial structure using distance geometry, followed by a force field based refinement of the structure.

#### See also:

• OEMacrocycleBuilderOptions class

#### **Code Examples**

• Generating a Single Macrocycle Conformer example

#### The OEMacrocycleBuilder class defines the following public methods:

- $\bullet$  Build
- · GetOptions and SetOptions

### **Constructors**

```
OEMacrocycleBuilder()
OEMacrocycleBuilder (const OEMacrocycleBuilderOptions&)
OEMacrocycleBuilder (const OEMacrocycleBuilder&)
```

Default and copy constructors.

#### operator=

OEMacrocycleBuilder &operator=(const OEMacrocycleBuilder&)

Assignment operator.

**Build** 

```
unsigned Build (OEChem:: OEMolBase&) const
unsigned Build (OEChem:: OEMCMolBase&) const
```

Generates 3D structure for a macrocycle molecule. Returns OEOmegaReturnCode\_Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace.

### **GetOptions**

const OEMacrocycleBuilderOptions& GetOptions() const

See SetOptions method.

### **SetOptions**

void SetOptions (const OEMacrocycleBuilderOptions&)

Sets *options* for building the molecule 3D-structures.

#### See also:

• OEMacrocycleBuilderOptions class

## 4.1.53 OEMacrocycleBuilderOptions

class OEMacrocycleBuilderOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for generating 3D structures of macrocycle molecules.

#### See also:

- OEMacrocycleOmegaOptions class
- OEMacrocycleBuilder class

#### **Code Examples**

• Generating a Single Macrocycle Conformer example

#### The OEMacrocycleBuilderOptions class defines the following public methods:

- · GetDielectricConst and SetDielectricConst
- · GetRandomSeed and SetRandomSeed
- · GetRefTolerance and SetRefTolerance
- · GetSkipRefinement and SetSkipRefinement

### **Constructors**

```
OEMacrocycleBuilderOptions()
OEMacrocycleBuilderOptions (const OEMacrocycleBuilderOptions &)
```

Default and copy constructors.

#### operator=

OEMacrocycleBuilderOptions & operator= (const OEMacrocycleBuilderOptions &)

Assignment operator.

### **GetDielectricConst**

double GetDielectricConst() const

See SetDielectricConst method.

### **GetRandomSeed**

unsigned GetRandomSeed() const

See SetRandomSeed method.

### **GetRefTolerance**

double GetRefTolerance() const

See SetRefTolerance method.

### **GetSkipRefinement**

bool GetSkipRefinement () const

See SetSkipRefinement method.

#### **SetDielectricConst**

bool SetDielectricConst (const double)

Sets the dielectric constant of the solvent to be used in the refinement stage. Default: 80.0.

### **SetRandomSeed**

bool SetRandomSeed (const unsigned)

Sets the random seed for initial structure generation. Default: 0.

#### **SetRefTolerance**

bool SetRefTolerance (const double)

Sets the tolerance criteria for the optimizer during refinement. Default: 0.001.

#### **SetSkipRefinement**

bool SetSkipRefinement (const bool)

Sets whether refinement of the generated initial structure should be performed or skipped. If true, refinement is skipped. Default: False.

### 4.1.54 OEMacrocycleOmega

class OEMacrocycleOmega

This class defines an interface for generating ensembles of conformers of macrocycle molecules.

#### See also:

- OEMacrocycleOmegaOptions class
- OEMacrocycleBuilder class

#### **Code Examples**

• Generating Macrocycle Conformers example

The OEMacrocycleOmega class defines the following public methods:

- $\bullet$  Build
- · GetOptions and SetOptions

#### **Constructors**

```
OEMacrocycleOmega()
OEMacrocycleOmega (const OEMacrocycleOmegaOptions&)
OEMacrocycleOmega (const OEMacrocycleOmega&)
```

Default and copy constructors.

#### operator=

```
OEMacrocycleOmega & operator= (const OEMacrocycleOmega&)
```

Assignment operator.

#### **Build**

unsigned Build (OEChem:: OEMCMolBase&) const

Generates conformer ensemble for a macrocycle molecule. Returns OEOmegaReturnCode\_Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace.

#### **GetOptions**

const OEMacrocycleOmegaOptions& GetOptions() const

See SetOptions method.

#### **SetOptions**

void SetOptions (const OEMacrocycleOmegaOptions&)

Sets *options* for generating conformer ensemble.

#### See also:

• OEMacrocycleOmegaOptions class

### 4.1.55 OEMacrocycleOmegaOptions

class OEMacrocycleOmegaOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for generating ensemble of macrocycle molecule conformers.

See also:

- OEMacrocycleOmega class
- OESliceEnsembleOptions class
- OEMacrocycleBuilderOptions class

#### **Code Examples**

• Generating Macrocycle Conformers example

#### The OEMacrocycleOmegaOptions class defines the following public methods:

- GetEnergyWindow and SetEnergyWindow
- GetIterCycleSize and SetIterCycleSize
- · GetMacrocycleBuilderOptions and SetMacrocycleBuilderOptions

- GetMaxConfs and SetMaxConfs
- · GetMaxIter and SetMaxIter
- · GetSliceEnsembleOptions and SetSliceEnsembleOptions

#### **Constructors**

```
OEMacrocycleOmegaOptions()
OEMacrocycleOmegaOptions (const OEMacrocycleOmegaOptions &)
```

Default and copy constructors.

#### operator=

OEMacrocycleOmegaOptions & operator= (const OEMacrocycleOmegaOptions &)

Assignment operator.

#### **GetEnergyWindow**

double GetEnergyWindow() const

See SetEnergyWindow method.

#### **GetIterCycleSize**

```
unsigned int GetIterCycleSize() const
```

See SetIterCycleSize method.

## **GetMacrocycleBuilderOptions**

```
OEMacrocycleBuilderOptions& GetMacrocycleBuilderOptions()
const OEMacrocycleBuilderOptions& GetMacrocycleBuilderOptions() const
```

See SetMacrocycleBuilderOptions method.

### **GetMaxConfs**

unsigned GetMaxConfs() const

See SetMaxConfs method.

### **GetMaxIter**

unsigned int GetMaxIter() const

See SetMaxIter method.

#### **GetSliceEnsembleOptions**

```
OESliceEnsembleOptions& GetSliceEnsembleOptions()
const OESliceEnsembleOptions& GetSliceEnsembleOptions() const
```

See SetSliceEnsembleOptions method.

### **SetEnergyWindow**

bool SetEnergyWindow (const double)

See SetEnergyWindow method. Default: 20.

### **SetIterCycleSize**

bool SetIterCycleSize(const unsigned int)

Sets the number of new conformers are to be attempted before checking if a new minimum was found. Conformer generation run finishes if no new minimum is found during an iteration cycle. Default: 100.

#### **SetMacrocycleBuilderOptions**

void SetMacrocycleBuilderOptions (const OEMacrocycleBuilderOptions&)

Sets *options* that are to be used for generating new conformers.

#### See also:

• OEMacrocycleBuilderOptions class

#### **SetMaxConfs**

bool SetMaxConfs (const unsigned)

See SetMaxConfs method. Default: 400.

### **SetMaxIter**

```
bool SetMaxIter (const unsigned int)
```

Sets the maximum number of iteration cycles are to be attempted. If the desired number of unique conformers are already generated in the ensemble, conformer generation would terminate before reaching this number. Default: 2000.

#### **SetSliceEnsembleOptions**

void SetSliceEnsembleOptions (const OESliceEnsembleOptions&)

Sets *options* that are to be used for removing duplicate conformers during macrocycle conformer ensemble generation.

#### See also:

• OESliceEnsembleOptions class

## 4.1.56 OEMakeFragLib

class OEMakeFragLib : public OEBuilderBase

This class defines an interface for generating a fragment library. The builder allows building either a partial or a complete fragment library by controlling the content of the fraglib currently loaded in the builder.

#### **Code Examples**

• Making Fragment Library example

The following methods are publicly inherited from OEBuilderBase:

- · AddFragLib
- · ClearFragLibs

#### The OEMakeFragLib class defines the following public methods:

- · AddFrag
- · GenerateMissingFrags
- · GetMissingFrags

### **Constructors**

```
OEMakeFragLib()
OEMakeFragLib(const OEFragBuilderOptions&)
OEMakeFragLib(const OEMakeFragLib&)
```

Default and copy constructors. The default constructor instantiates the class with OEFragBuilderOptions with the OEFragBuilderMode\_Strict mode.

#### operator=

```
OEMakeFraqLib & operator= (const OEMakeFraqLib&)
```

Assignment operator.

## 4.1.57 AddFrag

void AddFrag (const OEChem:: OEMCMolBase&)

Adds the specified **fragment** to the currently loaded fragment library.

See also:

· AddFragLib method.

# 4.1.58 GenerateMissingFrags

```
void GenerateMissingFrags(OEChem::oemolistream&, OEChem::oemolostream&).
\leftarrowconst
void GenerateMissingFrags(const OEChem::OEMolBase&, OEChem::oemolostream&).
\hookrightarrow \textbf{const}
```

Finds the missing fragments corresponding to the given input file stream or molecule, generates 3D structures of the fragments and adds those to the output file stream.

## 4.1.59 GetMissingFrags

```
OESystem:: OEIterBase<OEChem:: OEMCMolBase>*..
GetMissingFrags(OEChem::oemolistream&) const
OESystem::OEIterBase<OEChem::OEMCMolBase>* GetMissingFrags(const
→OEChem::OEMolBase&) const
```

Finds the missing fragments corresponding to the given input file stream or molecule, and returns a collection of the fragments. This method does not generate 3D structures of the fragments.

## 4.1.60 OEMolBuilder

```
class OEMolBuilder : public OEBuilderBase
```

This class defines an interface for generating an initial 3D structure of a molecule, by connecting pre-generated fragment coordinates that constitute the molecule. Building the 3D structure of a molecule with this builder is fast when all the fragments constituting a molecule are available in the fraglib associated with the builder. This builder makes no effort to obtain a low energy conformer of the molecule.

See also:

- OEMolBuilderOptions class
- OEConfFixOptions class

#### The following methods are publicly inherited from OEBuilderBase:

- · AddFragLib
- ClearFragLibs

The OEMolBuilder class defines the following public methods:

- $\bullet$  Build
- · GetOptions and SetOptions
- $\bullet$  Prep

### **Constructors**

```
OEMolBuilder()
OEMolBuilder (const OEMolBuilderOptions&)
OEMolBuilder (const OEMolBuilder&)
```

Default and copy constructors.

#### operator=

OEMolBuilder & operator= (const OEMolBuilder&)

Assignment operator.

## **4.1.61 Build**

```
unsigned Build (OEChem:: OEMCMolBase&) const
unsigned Build (OEChem:: OEMCMolBase&, const OEConfFixOptions&) const
```

Generates a 3D structure for a molecule. Returns OEOmegaReturnCode\_Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace. The second argument provided with appropriate options can be used to fix part of a molecule structure to predefined coordinates.

See also:

• OEConfFixOptions class

## 4.1.62 GetOptions

const OEMolBuilderOptions& GetOptions() const

See SetOptions method.

# **4.1.63 Prep**

unsigned Prep (OEChem:: OEMCMolBase& mol) const

Prepares molecule for 3D structure generation. Returns OEOmegaReturnCode\_Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace.

A call to the OEMolBuilder. Prep is not required before calling OEMolBuilder. Build, however is useful in determining if some of the pre-conditions are met for building.

# 4.1.64 SetOptions

void SetOptions (const OEMolBuilderOptions&)

Sets *options* for building the molecule 3D-structures.

#### See also:

• OEMolBuilderOptions class

# 4.1.65 OEMolBuilderOptions

class OEMolBuilderOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for generating an initial 3D structure of a molecule, by connecting pre-generated fragment coordinates that constitute the molecule.

#### See also:

- OEMolBuilder class
- OEFragBuilderOptions class

The OEMolBuilderOptions class defines the following public methods:

- · GetCanonOrder and SetCanonOrder
- GetEnumNitrogen and SetEnumNitrogen
- · GetEnumRing and SetEnumRing
- SetFragBuilderMode
- GetFragBuilderOptions and SetFragBuilderOptions
- · GetFromCT and SetFromCT
- · GetIgnoreStereo and SetIgnoreStereo
- GetMaxEnumConfs and SetMaxEnumConfs
- GetSampleHydrogens and SetSampleHydrogens
- GetStrictAtomTypes and SetStrictAtomTypes

### **Constructors**

```
OEMolBuilderOptions()
OEMolBuilderOptions (const OEMolBuilderOptions &)
```

Default and copy constructors.

#### operator=

OEMolBuilderOptions & operator= (const OEMolBuilderOptions &)

Assignment operator.

#### **GetCanonOrder**

bool GetCanonOrder() const

See SetCanonOrder method.

#### GetEnumNitrogen

unsigned int GetEnumNitrogen() const

See SetEnumNitrogen method.

#### **GetEnumRing**

**bool** GetEnumRing() const

See SetEnumRing method.

### **GetFragBuilderOptions**

```
OEFragBuilderOptions& GetFragBuilderOptions()
const OEFragBuilderOptions& GetFragBuilderOptions() const
```

See SetFragBuilderOptions method.

### **GetFromCT**

bool GetFromCT() const

See SetFromCT method.

### **GetIgnoreStereo**

bool GetIgnoreStereo() const

See Set IgnoreStereo method.

### **GetMaxEnumConfs**

unsigned GetMaxEnumConfs() const

See SetMaxEnumConfs method.

### **GetSampleHydrogens**

bool GetSampleHydrogens() const

See SetSampleHydrogens method.

### **GetStrictAtomTypes**

**bool** GetStrictAtomTypes() const

See SetStrictAtomTypes method.

#### **SetCanonOrder**

```
bool SetCanonOrder (const bool)
```

This method can be used to enable/disable the automatic reordering of input molecules to a canonical atom and bond order. In order obtain consistent results from different file formats and different connection table orders, OMEGA reorders the input connection table. If true, the atoms of the molecule are indexed in canonical order before building the molecule structure. Default: True.

#### **SetEnumNitrogen**

bool SetEnumNitrogen (const unsigned int)

Sets whether the generated initial conformation should be enumerated for invertible nitrogens. Default: OENitrogenEnumeration\_Unspecified.

See also:

· OENitrogenEnumeration namespace

### **SetEnumRing**

bool SetEnumRing (const bool)

Sets whether the generated initial conformation should be **enumerated** for **ring stereo**. If true, the builder will enumerate alternate ring conformations and generate multiple conformations, if available. Default: True.

### **SetFragBuilderMode**

bool SetFragBuilderMode (const unsigned mode)

Sets the OEFragBuilderOptions parameter defaults corresponding to the specified mode.

### **SetFragBuilderOptions**

**void** SetFragBuilderOptions (const OEFragBuilderOptions&)

Sets OEFragBuilderOptions related to building fragment coordinates.

#### See also:

• OEFragBuilderOptions class

#### **SetFromCT**

bool SetFromCT (const bool)

Sets whether the initial 3D coordinates should be generated from the **connection table of the input molecule**. If true, the initial 3D coordinates are generated from the connection table. Default: True.

### **SetIgnoreStereo**

bool SetIgnoreStereo (const bool)

Sets whether **conformer generation should continue** even when specified stereo signatures in a molecule could not be honored. Default: False.

### **SetMaxEnumConfs**

bool SetMaxEnumConfs (const unsigned)

Sets the maximum number of conformers to be generated during enumeration. Default: 1024.

### **SetSampleHydrogens**

bool SetSampleHydrogens (const bool)

Sets whether hydrogen sampling should be performed on generated structures. If true, hydrogen sampling is performed. Default: False.

### **SetStrictAtomTypes**

bool SetStrictAtomTypes (const bool)

Sets whether strict definition of atom typing should be used. If true, a molecule will fail if any atom does not have a valid atom type. Calling this method with false will allow the atom typer to look for a different atom type of the same element and replace the failing atom type with a valid one that is "close enough". Default: True.

### 4.1.66 OEOmega

class OEOmega

This class defines an interface for generating ensembles of conformers of small molecules.

### See also:

• OEOmegaOptions class

#### **Code Examples**

- Generating Conformers example
- Generating Densely Sampled Conformers example
- Generating Stereoisomers example

#### **Constructors**

```
OEOmega()
OEOmega (const OEOmegaOptions&)
OEOmega (const OEOmega&)
```

Default and copy constructors.

#### operator=

OEOmega & operator= (const OEOmega&)

Assignment operator.

## 4.1.67 AddFragLib

```
void AddFragLib()
void AddFragLib (const std:: string &)
void AddFragLib (OEPlatform::oeistream &)
```

The parameterless version will load the built-in fraglib immediately. By default, the built-in fraglib does not load until OEOmega. Build is called for the first time.

The string and oeistream versions will add an external fraglib. This will be used in addition to the built-in fraglib. To use only this fraglib, call OEOmega. ClearFragLibs first.

Note: An enhanced fragment library, omega\_fragment\_lib\_2020.oeb.gz, that improves the performance of conformer generation is available on request from the database downloads page.

## **4.1.68 Build**

unsigned Build (OEChem:: OEMCMolBase&) const

Generates conformers for a molecule. Returns OEOmegaReturnCode Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace.

# 4.1.69 ClearFragLibs

void ClearFragLibs()

Clears all fraglibs from the OEOmega object.

# 4.1.70 GetOptions

const OEOmegaOptions& GetOptions() const

Retrieves a constant reference to the OEOmegaOptions instance as currently set.

# 4.1.71 SetOptions

void SetOptions (const OEOmegaOptions&)

Sets the structure generation options by passing in an OEOmegaOptions instance.

# 4.1.72 OEOmegaOptions

class OEOmegaOptions : public OESystem: : OEOptions

#### See also:

• OEOmega class

#### **Code Examples**

- Generating Conformers example
- Generating Densely Sampled Conformers example
- Generating Stereoisomers example

There is a list of suboption default values later in this section.

The OEOmegaOptions class defines the following public methods:

- · GetConfFixOptions and SetConfFixOptions
- GetEnergyWindow and SetEnergyWindow
- · Get Include Input and Set Include Input
- GetMaxConfs and SetMaxConfs
- · GetMolBuilderOptions and SetMolBuilderOptions
- · GetSliceEnsembleOptions and SetSliceEnsembleOptions
- GetStrictStereo and SetStrictStereo
- · GetTorDriveOptions and SetTorDriveOptions
- · GetTorsionDrive and SetTorsionDrive
- · GetWarts and SetWarts

### **Constructors**

OEOmegaOptions (const unsigned int sampling = OEOmegaSampling::Classic) OEOmegaOptions (const OEOmegaOptions &)

Default and copy constructors.

#### operator=

OEOmegaOptions & operator=(const OEOmegaOptions &)

Assignment operator.

### **GetConfFixOptions**

```
OEConfFixOptions& GetConfFixOptions()
const OEConfFixOptions& GetConfFixOptions() const
```

See SetConfFixOptions method.

#### **GetEnergyWindow**

double GetEnergyWindow() const

See SetEnergyWindow method.

#### GetIncludeInput

bool GetIncludeInput () const

See Set Include Input method.

### **GetMaxConfs**

unsigned GetMaxConfs() const

See SetMaxConfs method.

#### **GetMolBuilderOptions**

```
OEMolBuilderOptions& GetMolBuilderOptions()
const OEMolBuilderOptions& GetMolBuilderOptions() const
```

See SetMolBuilderOptions method.

### **GetSliceEnsembleOptions**

```
OESliceEnsembleOptions& GetSliceEnsembleOptions()
const OESliceEnsembleOptions& GetSliceEnsembleOptions() const
```

See SetSliceEnsembleOptions method.

#### **GetStrictStereo**

bool GetStrictStereo() const

See SetStrictStereo method.

### **GetTorDriveOptions**

```
OETorDriveOptions& GetTorDriveOptions()
const OETorDriveOptions& GetTorDriveOptions() const
```

See Set TorDriveOptions method.

#### **GetTorsionDrive**

bool GetTorsionDrive() const

See Set TorsionDrive method.

### **GetWarts**

bool GetWarts () const

See SetWarts method.

### **SetConfFixOptions**

**void** SetConfFixOptions (const OEConfFixOptions&)

Sets *options* related to partially fixing conformers.

### See also:

• OEConfFixOptions class

### **SetEnergyWindow**

```
bool SetEnergyWindow (const double)
```

See SetEnergyWindow method. Default: 10.

### SetIncludeInput

bool SetIncludeInput (const bool)

Sets whether to pass the unmodified input structure into output conformer ensemble. If true, the input conformers are appended at the beginning of the generated conformer ensemble. Default: False.

### **SetMaxConfs**

bool SetMaxConfs (const unsigned)

See SetMaxConfs method. Default: 200.

#### **SetMolBuilderOptions**

void SetMolBuilderOptions (const OEMolBuilderOptions&)

Sets *options* related to generating initial conformer.

#### See also:

• OEMolBuilderOptions class

#### **SetSliceEnsembleOptions**

**void** SetSliceEnsembleOptions (const OESliceEnsembleOptions&)

Sets *options* related to deduplicating generated ensemble.

#### See also:

• OESliceEnsembleOptions class

#### **SetStrictStereo**

bool SetStrictStereo (const bool)

Sets whether conformer generation should fail if stereo is not specified on the input molecules. Default: True.

### **SetTorDriveOptions**

**void** SetTorDriveOptions (const OETorDriveOptions&)

Sets *options* related to torsion driving for conformer generation.

#### See also:

• OETorDriveOptions class

### **SetTorsionDrive**

bool SetTorsionDrive (const bool)

Sets whether to perform torsion driving. Default: True.

### **SetWarts**

bool SetWarts (const bool)

Sets whether to generate unique titles for conformers. Default: False.

# **4.1.73 Suboption Parameter Defaults**

Default values of the parameters from the suboption classes are compiled below.

| parameter        | Default                                  |
|------------------|------------------------------------------|
| CanonOrder       | True                                     |
| EnumNitrogen     | OENitrogenEnumeration_Unspecified        |
| EnumRing         | True                                     |
| FromCT           | True                                     |
| IgnoreStereo     | False                                    |
| MaxEnumConfs     | 1024                                     |
| SampleHydrogens  | False                                    |
| StrictAtomTypes  | True                                     |
| MaxTerminalHeavy | 0                                        |
| RangeIncrement   | 5                                        |
| RMSThreshold     | 0.5                                      |
| CommentEnergy    | False                                    |
| ForceField       | OEMMFFSheffieldFFType_MMFF94Smod_NOESTAT |
| MaxRotors        | 9999                                     |
| MaxSearchTime    | 120.0 sec                                |
| RotorOffset      | False                                    |
| SDEnergy         | False                                    |
| UseGPU           | True                                     |

# 4.1.74 OERingFragOptions

class OERingFragOptions : public OEFragOptions

This class provides an interface to setup options required for generating coordinates for ring fragments. A fragment is a building block that is used for initial 3D structure generation of molecules.

See also:

• OEFragBuilderOptions class

The following methods are publicly inherited from OEFragOptions:

- · GetEnergyWindow and SetEnergyWindow
- · GetFragGen and SetFragGen
- GetFragKeep and SetFragKeep
- GetRMS and SetRMS
- GetTimeLimit and SetTimeLimit

### The OERingFragOptions class defines the following public methods:

· GetStartFactor and SetStartFactor

### **Constructors**

```
OERingFragOptions()
OERingFragOptions (const OERingFragOptions &)
```

Default and copy constructors.

#### operator=

OERingFragOptions &operator=(const OERingFragOptions &)

Assignment operator.

#### **GetStartFactor**

unsigned GetStartFactor() const

See SetStartFactor method.

### **SetStartFactor**

bool SetStartFactor (const unsigned)

Sets a **multiplicative factor** that determines how many starts are to be used for generating ring fragment coordinates. Default: 2.

### 4.1.75 OESIiceEnsembleOptions

class OESliceEnsembleOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for reducing a molecule conformer ensemble, by removing duplicates and high energy conformers.

The OESliceEnsembleOptions allows multiple ways to set-up the desired settings for each parameter for slicing up an ensemble. There are three (3) main control parameters: *EnergyWindow, RMSThreshold*, and *MaxConfs*. The default usage is to use the same control settings for slicing all molecule ensembles. However, for each of the three parameters, there is also a possibility to set the parameter settings to be a variable based on the number of rotatable bonds in the molecule. The variable settings can be applied by using the *range* based API points.

Here we describe how to use the range based settings for *MaxConfs*, however, the same applies to *EnergyWindow* and RMSThreshold as well. A MaxConfs setting of 100,200,300 with SetMaxConfRange along with a value of 5 for the RangeIncrement set with SetRangeIncrement would use a MaxConfs value of 100 for molecule with number of rotatable bonds between 0-4, that of 200 for molecule with number of rotatable bonds between 5-9, and 300 for molecule with number of rotatable bonds of 10 or higher.

See also:

• OETorDriver class

The OESliceEnsembleOptions class defines the following public methods:

- GetEnergyWindow and SetEnergyWindow
- GetEnergyRange and SetEnergyRange
- · GetMaxConfs and SetMaxConfs
- · GetMaxConfRange and SetMaxConfRange
- GetMaxTerminalHeavy and SetMaxTerminalHeavy
- · GetRangeIncrement and SetRangeIncrement
- · GetRMSThreshold and SetRMSThreshold
- · GetRMSRange and SetRMSRange

#### **Constructors**

```
OESliceEnsembleOptions()
OESliceEnsembleOptions (const OESliceEnsembleOptions &)
```

Default and copy constructors.

#### operator=

OESliceEnsembleOptions & operator=(const OESliceEnsembleOptions &)

Assignment operator.

### **GetEnergyWindow**

```
double GetEnergyWindow() const
double GetEnergyWindow (const unsigned numRotors) const
```

See  $SetEnergyWindow$  method. The second variation of the method returns the value of the energy window that is in effect for a given molecule with specified number of rotors.

### **GetEnergyRange**

std::vector<double> GetEnergyRange() const

See SetEnergyRange method.

### **GetMaxConfs**

```
unsigned GetMaxConfs() const
unsigned GetMaxConfs (const unsigned numRotors) const
```

See SetMaxConfs method. The second variation of the method returns the value of maximum conformers that is in effect for a given molecule with specified number of rotors.

#### **GetMaxConfRange**

std::vector<unsigned int> GetMaxConfRange() const

See SetMaxConfRange method.

#### **GetMaxTerminalHeavy**

unsigned GetMaxTerminalHeavy () const

See SetMaxConfRange method.

### **GetRangeIncrement**

unsigned int GetRangeIncrement () const

See SetRangeIncrement method.

#### **GetRMSThreshold**

```
double GetRMSThreshold() const
double GetRMSThreshold (const unsigned numRotors) const
```

See Set RMSThreshold method. The second variation of the method returns the value of RMS threshold that is in effect for a given molecule with specified number of rotors.

#### **GetRMSRange**

```
std::vector<double> GetRMSRange() const
```

See SetRMSRange method.

#### **SetEnergyWindow**

void SetEnergyWindow (const double)

Sets the **maximum allowable energy** difference between the lowest and the highest energy conformers, in units of kcal/mol. Default: 10.0 kcal/mol.

### **SetEnergyRange**

```
bool SetEnergyRange (const std:: vector<double>&)
bool SetEnergyRange (const std::string&)
```

Sets the energy range that allows to define a varying  $EnergyWindow$  energy window in conjunction with the RangeIncrement. Defining the range overrides the singly defined energy window value. The string version of the overload expects a comma separated string.

### **SetMaxConfs**

void SetMaxConfs (const unsigned int)

Sets the maximum number of conformers to be kept. Default: 200.

### **SetMaxConfRange**

```
bool SetMaxConfRange (const std::vector<unsigned>&)
bool SetMaxConfRange(const std::string&);
```

Sets the **maximum number of conformers range** that allows to define a varying number of  $MaxConfs$  in conjunction with the RangeIncrement. Defining the range overrides the singly defined max confs value. The string version of the overload expects a comma separated string.

### **SetMaxTerminalHeavy**

void SetMaxTerminalHeavy (const unsigned int)

Sets the maximum number of terminal heavy atoms that should be allowed in calculating RMSD between conformers. If the number of terminal heavy atoms in the molecule exceeds the specified limit, all terminal heavy atoms are ignored in RMSD calculation. If the number is set to  $0$ , this value is treated as not set. **Default: 0.** 

#### **SetRangeIncrement**

bool SetRangeIncrement (const unsigned)

Sets the number of rotatable bonds range to be used when the OESliceEnsembleOptions. SetEnergyRange, OESliceEnsembleOptions. SetRMSRange, and OESliceEnsembleOptions. SetMaxConfRange are defines in terms of ranges. Default: 5.

#### **SetRMSRange**

```
bool SetRMSRange (const std::vector<double>&)
bool SetRMSRange (const std::string&)
```

Sets the RMS range that allows to define a varying RMSThreshold in conjunction with the RangeIncrement. Defining the range overrides the singly defined RMS threshold value. The string version of the overload expects a comma separated string.

### **SetRMSThreshold**

```
bool SetRMSThreshold (const double)
```

Sets the RMS threshold (Root Mean Square Cartesian distance) below which two conformers are treated as duplicates. Default: 0.5.

## **4.1.76 OETorDriveOptions**

class OETorDriveOptions : public OESystem:: OEOptions

This class provides an interface to set up options required for generating an ensemble of molecule conformers by torsion driving from an initial 3D structure of a molecule.

### See also:

- OETorDriver class
- OETorLib class

#### **Code Examples**

• Torsion Driving to Generating Conformer Ensemble example

The OETorDriveOptions class defines the following public methods:

- ExceedsMaxRotors
- GetCommentEnergy and SetCommentEnergy
- GetForceField and SetForceField
- GetMaxRotors and SetMaxRotors
- GetMaxSearchTime and SetMaxSearchTime
- GetRotorOffset and SetRotorOffset
- GetRotorPredicate and SetRotorPredicate
- GetSDEnergy and SetSDEnergy
- GetThompsonOptions and SetThompsonOptions
- GetTorLib and SetTorLib
- GetUseGPU and SetUseGPU
- GetUseThompson and SetUseThompson

#### **Constructors**

```
OETorDriveOptions()
OETorDriveOptions (const OETorDriveOptions &)
```

Default and copy constructors.

#### operator=

```
OETorDriveOptions & operator= (const OETorDriveOptions &)
```

Assignment operator.

### **ExceedsMaxRotors**

bool ExceedsMaxRotors (const OEChem:: OEMolBase&) const

This method checks if the number of rotors in the molecule is within the currently specified limit. See the SetMaxRotors method.

### **GetCommentEnergy**

bool GetCommentEnergy () const

See the SetCommentEnergy method.

### **GetForceField**

```
const OEForceField* GetForceFieldType() const
```

See the SetForceField method.

### **GetMaxRotors**

unsigned int GetMaxRotors() const

See the SetMaxRotors method.

#### **GetMaxSearchTime**

double GetMaxSearchTime() const

See the SetMaxSearchTime method.

#### **GetRotorOffset**

bool GetRotorOffset() const

See the SetRotorOffset method.

### **GetRotorPredicate**

const OESystem::OEUnaryPredicate<OEChem::OEBondBase>\* GetRotorPredicate() const

See the SetRotorPredicate method.

### **GetSDEnergy**

bool GetSDEnergy () const

See the SetSDEnergy method.

### **GetThompsonOptions**

```
OEThompsonOptions& GetThompsonOptions()
const OEThompsonOptions& GetThompsonOptions() const
```

See the SetThompsonOptions method.

#### **GetTorLib**

const OETorLib\* GetTorLib() const

See the SetTorLib method.

#### **GetUseGPU**

bool GetUseGPU() const

See the SetUseGPU method.

#### **GetUseThompson**

bool GetUseThompson() const

See the SetUseThompson method.

#### **SetCommentEnergy**

bool SetCommentEnergy (const bool)

Sets whether to add conformer energy in kcal/mol into the comments that appear if the output is written to a MOL2 file. If true, the comment energy is written. Default: False

### **SetForceField**

```
bool SetForceField(const unsigned)
bool SetForceField(const std::string&)
```

Sets the force field used for torsion driving. The first overload takes an *unsigned* from the OEMMFFSheffieldFFType constant namespace, and the second overload takes corresponding string values. The method returns false when the invalid selection is chosen and true otherwise. Default: MMFF94Smod\_NOESTAT

### **SetMaxRotors**

bool SetMaxRotors (const unsigned int)

Sets the limit of molecules with maximum number of rotors that would be handled by torsion driving. If a value of 9999 or higher is defined, this limit is ignored. Default: 9999

### **SetMaxSearchTime**

bool SetMaxSearchTime (const double)

Sets the **maximum time** that should be spent for the torsion driving of a molecule, in units of seconds. **Default: 120.0** sec

### **SetRotorOffset**

bool SetRotorOffset (const bool)

Sets whether the **rotor offset compression** should be turned on. Turning on the rotor offset compression reduces the space required when saved in an OEB file. Default: False

#### **SetRotorPredicate**

bool SetRotorPredicate(const OESystem::OEUnaryPredicate<OEChem::OEBondBase>&)

Sets the predicate that is used to decide whether a bond is rotatable.

### **SetSDEnergy**

bool SetSDEnergy (const bool)

Sets whether the conformer energy in kcal/mol should be stored as SD data. Default: False

#### **SetThompsonOptions**

```
void SetThompsonOptions (const OEThompsonOptions&)
```

Sets *options* related to Thompson sampling.

### **SetTorLib**

```
bool SetTorLib (const unsigned)
bool setTorLib(const std::string&)
bool SetTorLib(const OETorLib&)
```

Sets the torsion library that is used for torsion driving. The first overload takes an *unsigned* from the *OETorLibType* constant namespace, and the second overload takes the corresponding string values. Default: Original

#### See also:

- OETorLib class.
- OETorLibType constant namespace.

#### **SetUseGPU**

```
void SetUseGPU (const bool)
```

Sets whether to use the GPU implementation for torsion driving, aka GPU-Omega. Default is true, however, if no GPU is detected on your system, Omega will fall back to the CPU implementation. GPU-Omega is only available with the default force field MMFF94Smod\_NOESTAT.

#### **SetUseThompson**

```
void SetUseThompson (const bool)
```

Sets whether to use Thompson sampling for exploring the conformer space. Default is false, that is, Omega will use exhaustive sampling by default. If switched Thompson sampling is used, the parameters can be controlled by the Thompson Options class.

# 4.1.77 OETorDriver

#### class OETorDriver

This class defines an interface for generating conformer ensembles of molecules, by torsion driving on the provided 3D structures of the molecules.

See also:

- OETorDriveOptions class
- OESliceEnsembleOptions class
- OEConfFixOptions class

#### **Code Examples**

• Torsion Driving to Generating Conformer Ensemble example

#### The OETorDriver class defines the following public methods:

- · GenerateConfs
- · GetForceField and SetForceField
- · GetSliceEnsembleOptions and SetSliceEnsembleOptions
- · GetTorDriveOptions and SetTorDriveOptions

### **Constructors**

```
OETorDriver()
OETorDriver (const OETorDriverOptions&)
OETorDriver (const OETorDriver&)
```

Default and copy constructors.

#### operator=

OETorDriver & operator= (const OETorDriver&)

Assignment operator.

### **GenerateConfs**

```
unsigned GenerateConfs (OEChem:: OEMCMolBase&) const
unsigned GenerateConfs (OEChem:: OEMCMolBase&, const OEConfFixOptions&) const
```

Generates conformer ensemble for a molecule. Returns OEOmegaReturnCode\_Success if the process succeeds, otherwise returns an error code from the OEOmegaReturnCode namespace. The second argument provided with appropriate options can be used to fix part of a molecule structure to predefined coordinates.

#### See also:

• OEConfFixOptions class

### **GetForceField**

const OEMolPotential:: OEForceField& GetForceField() const

See SetForceField method.

### **GetSliceEnsembleOptions**

const OESliceEnsembleOptions& GetSliceEnsembleOptions() const

See SetSliceEnsembleOptions method.

### **GetTorDriveOptions**

const OETorDriveOptions& GetTorDriveOptions() const

See SetTorDriveOptions.

### **SetForceField**

**void** SetForceField(OEMolPotential::OEForceField&)

Sets the forcefield for torsion driving. Default: **OEMMFFSheffield** with OEMMFFSheffieldFFType\_MMFF94Smod\_NOESTAT.

### See also:

- OEForceField class
- OEMMFFSheffield

### **SetSliceEnsembleOptions**

void SetSliceEnsembleOptions (const OESliceEnsembleOptions&)

Sets *options* for slicing ensemble to remove duplicates.

### See also:

• OESliceEnsembleOptions class

### **SetTorDriveOptions**

void SetTorDriveOptions (const OETorDriveOptions&)

Sets options for torsion driving.

#### See also:

• OETorDriveOptions class

# 4.1.78 OETorLib

#### class OETorLib

This class represents OETorLib.

#### See also:

• OETorDriveOptions class

### **Constructors**

```
OETorLib()
OETorLib(const unsigned type)
```

Default and copy constructors. The constructor with the type parameter allows the user to set the torsion library type from values in the  $OETOTLipType$  namespace.

### operator bool

operator bool() const

Returns false if the OETorLib object is empty, otherwise returns true.

# 4.1.79 AddTorsionLibrary

```
bool AddTorsionLibrary (const std::string &)
bool AddTorsionLibrary (OEPlatform:: oeistream &)
```

Takes a string or an oeistream object to add a torsion library. This will put the new torsion library above the current torsion library, which means that they will be checked first for a match. To replace the torsion library, call OETOrLib. Set TorsionLibrary. Method returns True if the library is added successfully.

## 4.1.80 AddTorsionRule

**bool** AddTorsionRule(const std::string &)

Add a single torsion rule as a string. The format for rules is a SMARTS pattern followed by the torsion angles. Method returns True if the rule is added successfully. The following is an example of a general rule:

 $[*:1][CH2:2][a:3][a:4]$  0 180 90 -90 45 -45 135 -135

The following code demonstrates how to add a new torsion rule to an existing OEOmega object named omega.

#### Example of adding a new torsion rule

```
# Adding the torsion rule "[0:1]=[C:2]-[0:3][CH3:4] 90" as a string
# This takes precedent over previous rule
rule = "[0:1]=[C:2]-[0:3][CH3:4] 90"
if not torlib.AddTorsionRule(rule):
    oechem. OEThrow. Fatal ("Failed to add torsion rule: %s" % rule)
omegaOpts.SetTorLib(torlib)
omega.SetOptions(omegaOpts)
if omega (mol) :
    oechem.OEWriteMolecule(ofs, mol)
```

The new rule will take precedence over all rules previously added to this object either from a file or calling this method.

**bool** AddTorsionRule(OEChem::OEQMolBase &qmol, std::vector<int> &deqrees)

The next signature of AddTorsionRule takes a generic OEQMolBase with a corresponding std::vector<int> containing the angles. The pattern represented by OEQMolBase should have map indices set on the atoms considered the torsion. In SMARTS this means the atoms should have map indices numbered from 1-4. This can theoretically allow torsion rules to be written in other query file formats provided there is a method for setting the appropriate map indices. The following code demonstrates how to initialize an OEQMolBase and use it to define a new torsion rule.

#### Example of adding a new torsion rule from a query molecule

```
# Adding torsion rule "(0:1]=[C:2]-[0:3][CH3:4] 45" as a query
# molecule. This takes precedent over default rule
qmol = oechem.OEQMol()oechem. OEParseSmarts (qmol, "[0:1]=[C:2]-[0:3][CH3:4]")degrees = occhem. OELntVector([45])if not torlib.AddTorsionRule(qmol, degrees):
    oechem. OEThrow. Fatal ("Failed to add torsion rule")
omegaOpts.SetTorLib(torlib)
omega.SetOptions(omegaOpts)
if omega (mol) :
    oechem.OEWriteMolecule(ofs, mol)
```

### 4.1.81 ClearTorsionLibrary

void ClearTorsionLibrary()

Clears the current torsion library. Omega cannot operate with an empty torsion library, so a new torsion library must be set before running Omega.

## 4.1.82 GetTorRule

```
const OEChem:: OESubSearch* GetTorRule (const OEChem:: OEMolBase&,
      const OEChem:: OEBondBase&) const
```

Returns the torsion rule associated with the specified bond of the specified molecule. Method returns a null pointer if a torsion rule is not found. The rules are stored as OESubSearch objects.

#### See also:

• OEGetTorValues function.

# 4.1.83 GetTorRules

OESystem::OEIterBase<OEChem::OESubSearch> \*GetTorRules()

Returns an iterator over the torsion rules. The rules are stored as OESubSearch objects.

## 4.1.84 HasTorRule

bool HasTorRule(const OEChem:: OEMolBase&, const OEChem:: OEBondBase&) const

Checks if a torsion rule exists with the specified bond of the specified molecule. Returns t rue if a rule exists.

## 4.1.85 ResetTorsionLibrary

bool ResetTorsionLibrary()

Resets the torsion library stored internally by Omega. Method returns True if the library is reset successfully.

# 4.1.86 SetTorsionLibrary

```
bool SetTorsionLibrary (const std::string &)
bool SetTorsionLibrary (OEPlatform:: oeistream &)
bool SetTorsionLibrary (unsigned int type)
```

Replaces the current torsion library with the one passed in as an argument. If the argument is a type, it is expected to be a value in the  $OETorLibType$  namespace. Method returns  $True$  if the library is set successfully.

# 4.1.87 OETorLibParameter

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OETorLibParameter : public OESystem:: OEMultiParameter<OEConfGen:: OETorLib>

The OETorLibParameter represents parameter that has a value of type OETorLib.

#### Following methods are publicly inherited from OEParameter:

- · AddAlias and GetAliases
- . AddDetail and GetDetail
- · AddIllegalRange and GetIllegalRanges
- · AddIllegalValue and GetIllegalValues
- · AddLegalRange and GetLegalRanges
- · AddStringDefault, GetStringDefault and GetStringDefaults
- · AddStringValue, GetStringValue and GetStringValues
- · ClearDefaults
- ClearValues
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
- · IsSet and IsSetToString

#### Following methods are publicly inherited from OEMultiParameter:

- · AddLegalEntry
- · GetDefault and SetDefault
- · GetSetting
- · GetValue and SetValue

### **Constructors**

```
OETorLibParameter()
OETorLibParameter (const std::string& name)
OETorLibParameter (const OETorLibParameter&)
```

Default and copy constructors.

Constructs an OETorLibParameter instance using the specified set of parameters.

### operator=

OETorLibParameter &operator=(const OETorLibParameter &)

The assignment operator.

# **4.2 OEConfGen Constants**

# 4.2.1 OEFragBuilderMode

This namespace contains constants that are used with OEFragBuilderOptions to control the defaults to be set for fragment building options. Different set of default options prepares the frag builder to generate structures that are suitable for different usage.

### **Default**

Same as OEFragBuilderMode\_Fast.

### **Dense**

Options suitable for building fragments for molecule building with the OEMolBuilder in the OEOmegaSampling\_Densemode.

| Option              | Non-Ring | Ring | Macrocycle |
|---------------------|----------|------|------------|
| <i>EnergyWindow</i> | 15.0     | 15.0 | 25.0       |
| <i>FragGen</i>      | 40       | 1024 | 2000       |
| <i>FragKeep</i>     | 1        | 1024 | 1024       |
| <i>RMS</i>          | 0.05     | 0.05 | 0.1        |
| <i>TimeLimit</i>    | 3600     | 3600 | 1800       |
| <i>StartFactor</i>  | X        | 100  | X          |

## Fast

Options suitable for fast, on-the-fly building of fragments during molecule building with the OEMolBuilder.

| Option              | Non-Ring | Ring | Macrocycle |
|---------------------|----------|------|------------|
| <i>EnergyWindow</i> | 8.0      | 8.0  | 25.0       |
| <i>FragGen</i>      | 40       | 1024 | 2000       |
| <i>FragKeep</i>     | 1        | 1024 | 1024       |
| <i>RMS</i>          | 0.1      | 0.1  | 0.1        |
| <i>TimeLimit</i>    | 400      | 400  | 1800       |
| <i>StartFactor</i>  | X        | 2    | X          |

### **Strict**

Options suitable for rigorous fragment structure generation, suitable for building fragment library with the OEMake-FragLib.

| Option              | Non-Ring | Ring  | Macrocycle |
|---------------------|----------|-------|------------|
| <i>EnergyWindow</i> | 4.0      | 4.0   | 25.0       |
| <i>FragGen</i>      | 40       | 50000 | 2000       |
| <i>FragKeep</i>     | 1        | 1024  | 1024       |
| <i>RMS</i>          | 0.1      | 0.1   | 0.1        |
| <i>TimeLimit</i>    | 400      | 400   | 1800       |
| <i>StartFactor</i>  | X        | 20    | X          |

# **4.2.2 OENitrogenEnumeration**

This namespace contains constants that are used with OEMolBuilderOptions. SetEnumNitrogen to control the behavior of OEOmega with respect to enumeration of nonterminal nitrogens. Any nitrogen with pyramidal geometry in the initial model of the input molecule, and having no more than two ring bonds is considered by OEOmega to be 'invertible'.

### **Default**

Equivalent to OENitrogenEnumeration\_Unspecified.

### Off

Nitrogens are not enumerated.

### All

All invertible nitrogens will be enumerated.

### **Unspecified**

Only invertible nitrogens with unspecified stereochemistry will be enumerated.

# 4.2.3 OEOmegaForceFieldType

This namespace contains constants that refers to forcefields that are available in OEOmega.

### **SAGE**

The SAGE Force Field from the Open Force Field Initiative. Name: sage

### **SAGE\_NOESTAT**

The SAGE forcefield without electrostatics. Name: sage\_NoEstat

### **SAGE SHEFF**

The SAGE forcefield with Sheffield solvation. Name: sage\_Sheff

### **MMFF**

The Merck Molecular Force Field (MMFF). Name: mmff

### **MMFF NOESTAT**

The MMFF forcefield without electrostatics. Name: mmff\_NoEstat

### **MMFF TRUNC**

The MMFF forcefield truncated at potential minimum. Name: mmff\_Trunc

### **MMFF\_SHEFF**

The MMFF forcefield with Sheffield solvation. Name: mmff\_Sheff

### MMFF94S

The 94s variation of the Merck Molecular Force Field (MMFF). Name: mmff94s

#### **MMFF94S\_NOESTAT**

The MMFF94S forcefield without electrostatics. Name: mmff94s\_NoEstat

### **MMFF94S\_TRUNC**

The MMFF94S forcefield truncated at potential minimum. Name: mmff94s\_Trunc

### MMFF94S\_SHEFF

The MMFF94S forcefield with Sheffield solvation. Name: mmff94s\_Sheff

### MMFF94Smod

The modified 94s variation of the Merck Molecular Force Field (MMFF). Name: mmff94smod

### MMFF94Smod\_NOESTAT

The modified MMFF94S forcefield without electrostatics. Name: mmff94smod\_NoEstat

### **MMFF94Smod TRUNC**

The modified MMFF94S forcefield truncated at potential minimum. Name: mmff94smod\_Trunc

### MMFF94Smod\_SHEFF

The modified MMFF94S forcefield with Sheffield solvation. Name: mmff94smod\_Sheff

### **Invalid**

Invalid force field type.

# 4.2.4 OEOmegaReturnCode

This namespace contains constants that are returned by various methods in **Omega TK** to indicate the outcome.

### **Success**

Method returned successfully.

### **MissingFFParams**

Force field setup failed due to missing parameters.

### **ExplicitHydrogens**

Failed to add explicit hydrogens.

### **InvalidOptions**

Failed due to invalid options.

### **No3DFromCT**

Molecule must be 3 dimensional when from CT is set to false.

### **TooManyRotors**

Maximum number of rotors exceeded.

### **UnspecifiedStereo**

Failed due to unspecified stereochemistry.

### **FailedCTBuild**

Failed to build structure from connection table (CT).

### **FailedTorDrive**

Failed to complete torsion driving.

### **ExceedsAtomDegree4**

Contains atom with degree greater than 4.

### **FailedDupSetup**

Duplicate removal setup failed.

### **FailedDGConfGen**

Unable to generate 3D conformer.

### **FailedTorAssign**

Torsion assignment failed.

### **FailedSmartMatch**

Unable to match SMARTS.

### **FailedFixMatch**

Fixfile match failed.

### **NoFixedFragment**

No fixed fragment found.

### **NoValidConfs**

No valid conformers generated.

### **No3DTorDrive**

Input must be 3 dimensional for torsion driving.

### **FailedCharges**

Failed to assign partial charges.

### **Failed**

Method failed.

# 4.2.5 OEOmegaSampling

This namespace contains constants that are used with  $OEOmegaOptions$  to control the defaults to be set for omega options. Different sets of default options prepares omega to generate structures that are optimal for different usages.

### **Code Examples**

• Generating Densely Sampled Conformers example

### **Classic**

Options to generate a set of conformers representing a gas phase ensemble.

### **Dense**

Options to generate a dense set of conformers optimal for FreeFormConf usage.

**Caution:** GPU-Omega is not compatible with the dense mode default force field. To enable GPU-Omega and utilize  $\mathbf{a}$ GPU set OETorDriveOptions.SetForceField to OEMMFFSheffieldFFType\_MMFF94Smod\_NOESTAT

#### **Pose**

Options to generate a set of conformers suitable for molecular alignment and pose prediction by docking.

### **ROCS**

Options to generate a set of conformers suitable for ROCS usage.

### **FastROCS**

Options to generate a sparse set of conformers suitable for FastROCS usage.

Options overridden by various modes from the default OEOmegaSampling\_Classic mode:

| Option             | Classic                           | Dense                     | Pose     | ROCS | FastROCS |
|--------------------|-----------------------------------|---------------------------|----------|------|----------|
| RangeIncrement     |                                   |                           | 8        |      |          |
| MaxConfs           | 200                               | 20000                     | 200, 800 | 50   | 10       |
| StrictStereo       | True                              | False                     |          |      |          |
| MaxSearchTime      | 120.0                             | 3600.0                    |          |      |          |
| EnergyWindow       | 10.0                              | 15.0                      |          |      |          |
| RMSThreshold       | 0.5                               | 0.3                       |          |      |          |
| EnumNitrogen       | OENitrogenEnumeration_Unspecified | OENitrogenEnumeration_All |          |      |          |
| SampleHydrogens    | False                             | True                      |          |      |          |
| SearchForceField   | mmff94smod_NoEstat                | mmff94s_Sheff             |          |      |          |
| FragBuilderOptions | Fast                              | Dense                     |          |      |          |

# **4.2.6 OESliceEnsembleDefaults**

This namespace contains constants that are used for defaults of OESliceEnsemble.

### **RMS**

RMS value for duplicate removal. Set to 0.5.

### **EWindow**

Energy windows value. Set to 10.0.

### **MaxConfs**

Maximum number of conformers in the ensemble. Set to 200.

# 4.2.7 OETorLibType

This namespace contains constants that are used to construct a OETorLib object.

#### See also:

• OETOrDriveOptions. SetTorLib method to control the torsion library used for conformation generation.

### **Default**

The default torsion library is OETOrLibType\_Original.

#### **Original**

The default **Omega TK** torsion library.

### GubaV21

Torsion library based on the work of Wolfgang Guba, Version 2.1.

See also:

 $\bullet$  [Guba-2016]

# **4.3 OEConfGen Functions**

## 4.3.1 OEAddGlobalFragLib

```
bool OEAddGlobalFragLib(const std::string &fraglib_filename,
                        bool replace=true)
```

Add a fragment library located at *fraglib filename* to Omega's global fragment library. If *replace* is true, previously existing fragments in the current global fragment library are replaced with the ones from *fraglib\_filename*.

Unlike the fragment libraries loaded by OEOmega. AddFragLib, the global fragment library is accessible to all omega instances. It is most useful in the JAVA programming language to minimize memory usage when running multiple OEOmega instances in threads. Other languages have the default fragment library pre-loaded already.

If you use OEAddGlobalFragLib to load your fragment library, do not use OEOmega. AddFragLib, as this will load the fragment library only into that particular OEOmega instance.

Note: This function is not thread-safe and must be called before starting any threads.

#### See also:

· OEClearGlobalFragLib function

# 4.3.2 OEClearGlobalFragLib

void OEClearGlobalFragLib()

Clear the global fragment library. This function can be used to remove the default fragment library in order to load a new one or to ensure that any force-field parameter change will be used during the subsequent runs in favor of the pre-loaded default fragment library.

Note: This function is not thread-safe and must be called before starting any threads.

#### See also:

• OEAddGlobalFragLib function

# 4.3.3 OEGetOmegaError

std::string OEGetOmegaError(const unsigned)

Returns error messages corresponding to return codes defined in OEOmegaReturnCode namespace.

# **4.3.4 OEGetTorValues**

bool OEGetTorValues (const OEChem:: OESubSearch& torrule, std:: vector<double>& values)

Provides the torsion values corresponding to the specified torsion rule. Method returns False If the specified OE-SubSearch object does not contain torsion rules.

#### See also:

· OETorLib. Get TorRule method.

# 4.3.5 OEIsMacrocycle

bool OEIsMacrocycle (const OEChem:: OEMolBase & mol, const unsigned int minSize = 10)

Checks if the specified molecule is a macrocycle. The second argument refers to the minimum number of atoms required to be in a ring for the molecule to be treated as a macrocycle molecule. By default a molecule is defined as macrocycle when it contains a 10-membered or larger ring regardless of their aromaticity and hetero atoms content, so for example large cyclic alkanes, annulenes, crown ethers or porphyrins are all macrocycles.

#### See also:

- OEMacrocycleOmega class
- OEMacrocycleBuilder class

# 4.3.6 OEFlipper

```
OESystem::OEIterBase<OEChem::OEMolBase> *OEFlipper(const OEChem::OEMolBase &mol,
                                                   const OEFlipperOptions &options)
OESystem::OEIterBase<OEChem::OEMolBase> *OEFlipper(const OEChem::OEMCMolBase &mol,
                                                   const OEFlipperOptions &options)
```

Enumerate the stereo-centers of  $mod$  and return them as a series of new molecules.

### **Parameters:**

*mol* The molecule to enumerate. The input molecule will always be returned even if there are no stereocenters to enumerate.

**options** The *options* for enumerating stereo-centers of molecule.

#### **Deprecated**

```
OESystem:: OEIterBase<OEChem:: OEMolBase> *OEFlipper(const OEChem:: OEMolBase &mol,
                                                    unsigned int maxcenters=12,
                                                    bool forceFlip=false,
                                                    bool enumNitrogen=false,
                                                    bool warts=false)
OESystem::OEIterBase<OEChem::OEMolBase> *OEFlipper(const OEChem::OEMCMolBase &mol,
                                                    unsigned int maxcenters=12,
                                                    bool forceFlip=false,
                                                    bool enumNitrogen=false,
                                                    bool warts=false)
```

Enumerate the stereo-centers of  $mod$  and return them as a series of new molecules.

#### **Parameters:**

- *mol* The molecule to enumerate. The input molecule will always be returned even if there are no stereocenters to enumerate.
- *maxcenters* The number of molecules generated by enumerating the stereocenters is  $2^N$ , where N is the number of stereocenters. In some instances, this may be larger than is desired. This parameter indicates the maximum number of stereocenters which will be fully enumerated. If a molecule has more than maxcenters stereocenters, this function will randomly enumerate  $2^{maxcenters}$  instances from the full set of potential isomers.
- **forceFlip** This parameter forces the modification of all of the stereocenters in a molecule. If false (the default), will only enumerate stereocenters which do not already have a specified stereochemistry.
- enumNitrogen Controls the behavior with respect to enumeration of nonterminal nitrogens. Any nitrogen with pyramidal geometry in the initial model of the input molecule, and having no more than two ring bonds is considered to be 'invertible'. Will enumerate all possible puckers if set to true.
- warts Add wart to title of each stereoisomer. A "wart" is a systematic naming scheme for the output titles.

**Caution:** This function will remove the molecule coordinates.

#### **Code Examples**

• Generating Stereoisomers example

# **4.3.7 OEFlipperStereoCenters**

```
unsigned OEFlipperStereoCenters (const OEChem:: OEMolBase &mol,
                                 const OEFlipperOptions &options)
```

Compute number of the stereo-centers of mol.

#### **Parameters:**

mol The input molecule.

options The *options* for enumerating stereo-centers of molecule.

# 4.3.8 OEOmegaGetArch

const char \*OEOmegaGetArch()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify the hardware architecture. The format of these strings may change over time.

# 4.3.9 OEOmegaGetLibraryRelease

```
const char *OEOmegaGetLibraryRelease()
```

Caution: Deprecated, use OEOmegaGetRelease instead.

# 4.3.10 OEOmegaGetLibraryVersion

unsigned int OEOmegaGetLibraryVersion()

**Caution:** Deprecated, use OEOmegaGetVersion instead.

# 4.3.11 OEOmegaGetLicensee

**bool** OEOmegaGetLicensee(std::string &licensee)

Returns the licensee name from the license file.

# 4.3.12 OEOmegaGetPlatform

const char \*OEOmegaGetPlatform()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify a platform. The format of these strings may change over time, and future distributions may contain different values even when using the same operating system, compiler and processor. For example, on a  $\times 86$  64 Red Hat Enterprise Linux box this would return  $redhat-RHEL5-<sub>q</sub>++4.1-x64.$ 

# 4.3.13 OEOmegaGetRelease

const char \*OEOmegaGetRelease()

Returns the release name of the *Omega TK* library being used. This returns a value similar to 0,10,0 for production versions of the library, and 0.10.0 debug for the checking version of the library.

# 4.3.14 OEOmegaGetSite

**bool** OEOmegaGetSite(std::string &site)

Returns the physical site location of the licensee as registered in the license file.

# 4.3.15 OEOmegaGetVersion

unsigned int OEOmegaGetVersion()

Returns the version number of the library being used. This is an unsigned integer value indicating the date on which the library was built, for example 20141001, for the 1st of October 2014. This value should be used when reporting problems, and unlike the release string, may be used in comparisons if needed.

# 4.3.16 OEOmegalsGPUReady

bool OEOmegaIsGPUReady()

Determines whether a GPU is present and available for use on the current system.

This can be used to determine if conformer generation using the torsion driving method will be accelerated by a GPU.

### Caution:

This function causes GPU context creation and so is only safe to use from within a process when using a multithreaded environment such as python's multiprocessing.

#### See also:

GPU-Omega chapter in the OEOmega TK manual.

# 4.3.17 OEOmegalsLicensed

**bool** OEOmegaIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any **Omega TK** functionality.

The 'feature' argument can be used to check for a valid license to **Omega TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'explate' argument can be used to obtain the expiration date of the current **Omega TK** license.

See also:

· OEChemIsLicensed function

# 4.3.18 OEOmegaSystemHasGPU

bool OEOmegaSystemHasGPU()

Determines whether a GPU is present on the current system. This will check that the system is a Linux platform and the /dev/nvidiaN file exits, where N can be between 0 and 100. It will not try to create a context on the GPU so there is still the possibility that the GPU will not be available, either due to the driver being uninstalled or the GPU being used by another system user.

# 4.3.19 OESIiceEnsemble

```
bool OESliceEnsemble (OEChem:: OEMCMolBase &mol, double
\rightarrowrms=OESliceEnsembleDefaults::RMS,
                      double ewindow=OESliceEnsembleDefaults::EWindow,
                      unsigned maxconfs=OESliceEnsembleDefaults::MaxConfs)
bool OESliceEnsemble(OEChem::OEMCMolBase &mol, const OESliceEnsembleOptions& options)
```

Reduces the number of conformers in the input  $mod$  using the OMEGA deduplication algorithm. This allows for *OEOmega* to generate a very large ensemble with much looser deduplication parameters, and then to "slice" that ensemble of conformations by various different parameters after the fact.

The default values for the first overlad of the function are picked from the OESliceEnsembleDefaults namespace.

Conformer slicing proceeds in the following order:

- 1. Slice by energy window. Decreasing this value will result in fewer conformers. For slicing by energy, the algorithm assumes that the energies for each conformer has been pre-calculated and set as the energy property of the conformer using the OEMo1Base. SetEnergy method. Conformer generation using OEOmega, sets this property by default.
- 2. Slice by RMS. Increasing this value will result in fewer conformers.
- 3. Slice by maximum number of conformers. Decreasing this value will result in fewer conformers.

**Note:** If the same energy window and RMS values are being chosen as the defaults being used in the previous OEOmega calculation, it will be faster to just delete conformers directly with OEMCMolBase. DeleteConf. This function is really intended to be run whenever the RMS has changed, or the conformer geometry itself has changed. As RMS deduplication is the expensive  $O(N^2)$  problem that requires many "tricks" to perform very fast.

# **PRELIMINARY API**

# 5.1 Preliminary OEConfGen Classes

# 5.1.1 OEThompsonOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEThompsonOptions : public OESystem:: OEOptions

This class provides an interface to set up options for Thompson sampling. This can be enabled using the UseThompson flag in the OETorDriver flag. Thompson sampling is a powerful and generalizable technique of reinforcement learning that can help search vast spaces more efficiently [Thompson-1933]. The space of all possible conformers of a molecule grows combinatorially with an increasing number of rotors, making exhaustive search prohibitively expensive for larger molecules.

Omega can use the Thompson sampling approach to explore the conformer space of a given molecule to quickly learn the choices of torsion angles resulting in low-strain unique structures. For each rotor in the molecule, the method associates a prior awareness to all the torsion angles to be sampled as obtained from the torsion library. The knowledge of the likelihood of a given angle resulting in a low-strain conformer is used to choose sample torsions and is subsequently updated based on the outcome of that choice.

### See also:

- OETorDriver class
- $\bullet$  *OETorLib* class

### **Code Examples**

• Torsion Driving to Generating Conformer Ensemble example

#### The OEThompsonOptions class defines the following public methods:

- · GetMaxTrials and SetMaxTrials
- GetMaxTrialsRange and SetMaxTrialsRange
- GetTrialsRangeIncrement and SetTrialsRangeIncrement
- · GetBatchMaxRotors and SetBatchMaxRotors
- · GetPriorTemperature and SetPriorTemperature

### **Constructors**

```
OEThompsonOptions()
OEThompsonOptions (const OEThompsonOptions &)
```

Default and copy constructors.

#### operator=

```
OEThompsonOptions &operator=(const OEThompsonOptions &)
```

Assignment operator.

# 5.1.2 GetMaxTrials

bool GetMaxTrials() const

See the SetMaxTrials method.

# 5.1.3 GetMaxTrialsRange

bool GetMaxTrialsRange() const

See the SetMaxTrialsRange method.

# 5.1.4 GetTrialsRangeIncrement

bool GetTrialsRangeIncrement() const

See the Set TrialsRangeIncrement method.

# 5.1.5 GetBatchMaxRotors

bool GetBatchMaxRotors() const

See the SetBatchMaxRotors method.

# 5.1.6 GetPriorTemperature

**bool** GetPriorTemperature() const

See the SetPriorTemperature method.

# 5.1.7 SetMaxTrials

bool SetMaxTrials (const bool)

This parameter sets a limit on the number of Thompson sampling trials. OMEGA will stop exploration of the conformer space once this limit is reached, irrespective of how many conformers have been found so far. The default (and recommended) way of controlling this quantity, however, is through the  $SetMaxTrialsRange parameter. [default = 0]$ 

# 5.1.8 SetMaxTrialsRange

bool SetMaxTrialsRange (const bool)

This flag sets the maximum number of trials in Thompson sampling depending on the number of rotatable bonds in a given molecule. The range is determined by the Set TrialsRangeIncrement parameter. For example, SetMaxTrialsRange([1000,2000,3000,5000]) used with SetTrialsRangeIncrement(3) sets the maximum number of trials to 1000 for molecules with 0–2 rotors, 2000 for 3–5 rotors, 3000 for 6–8 rotors, and 5000 for all molecules with 9 or more rotors.

## 5.1.9 SetTrialsRangeIncrement

bool SetTrialsRangeIncrement (const bool)

This parameter is used to control the dependence of the maximum number of Thompson sampling trials on the number of rotors in the molecule along with the  $SetMaxTrialsRange$  parameter. [default = 1].

# 5.1.10 SetBatchMaxRotors

bool SetBatchMaxRotors (const bool)

This parameter controls the maximum allowed number of rotors for which batching is done; that is, two samples are drawn from the current distributions form all these rotors. The resulting  $2^{BatchMaxRotors}$ conformers are processed in a batch and the distributions associated with the rotors are then updated. Higher batchMaxRotors values result in a lower runtime, but for large enough batches, accuracy can be compromised as the learning is not reinforced frequently enough to influence many samples.  $[default = 2]$ 

# 5.1.11 SetPriorTemperature

bool SetPriorTemperature (const bool)

This parameter sets the initial probabilities (prior distributions) associated with each angle in the torsion rule according to the values of respective strain associated with the angles. If a rule does not provide these strain values, all angles are assumed to be at zero strain and equally likely. For nonzero strains, this parameter acts as a Boltzmann temperature and gives the probability as  $= exp(-1 \times \frac{strain}{PriorTemperature}).$ The lower the parameter, the stronger the initial preference for the angles with low strain.

For instance, a torsion angle with a strain of 5 kcal/mol will be initialized to a probability of 0.7% for *PriorTemperature* = 1, 60.6% for *PriorTemperature* = 10 and 95% for *PriorTemperature* = 100. [default  $= 1001$ 

# **SIX**

# **RELEASE HISTORY**

# 6.1 Omega TK 6.0.0

### 6.1.1 New features

- The following new methods have been added to OETorDriveOptions to enable use of Thompson sampling, instead of exhaustive sampling, of torsion angles during torsion driving. Use of Thompson sampling is especially useful, being significantly faster without losing quality, in generating smaller ensembles as obtained with the FastROCS or ROCS modes.
  - GetUseThompson
  - SetUseThompson
  - GetThompsonOptions
  - SetThompsonOptions
- A new class, OEThompsonOptions, has been added that enables controlling Thompson sampling during torsion driving.
- Generation of a single conformer with OEConformerBuilder has been modified to use Thompson sampling.

## 6.1.2 Minor bug fixes

- User-defined values passed through SetEnergyWindow, SetMaxConfs, and SetRMSThreshold are now properly accounted for, even when the corresponding defaults are range-based.
- . Molecule titles are retained when Build fails in OEOmega with fails to build structure from CT.
- A verbose log is provided for fragments that fail when *Build* fails in *OEOmega* with fails to build structure from CT.
- The OEOmegalsGPUReady function has been safeguarded from a rare crash. The function has also been updated to check not only for device 0, but for devices from 0 to 100.

# 6.2 Omega TK 5.1.0

### 6.2.1 New features

• A new Flipper option has been added to enumerate internally perceived relative stereocenters (e.g., 1,4disubstituted cyclohexanes). See SetEnumRelativeAtomStereo.

# 6.2.2 Minor bug fixes

- Stereochemistry of input molecules is now respected more consistently in OEMacrocycleBuilder.
- For SetMacroCycOptions in OEFragBuilderOptions, defaults for SetFragGen, SetFragKeep, and SetStartFactor have been changed to more appropriate values of 50000, 1024, and 20, respectively.
- An issue with the order of loading rules to an existing torsion library with *AddTorsionLibrary* has been fixed.
- A duplicate entry from the GUBA torsion library has been removed.

# 6.3 Omega TK 5.0.0

### 6.3.1 New features

- The default fragment library for OEOmega and OEMolBuilder has been updated. The new fragment library consists of over 580 K fragments, replacing the previous library with  $\sim80$  K fragments.
- Three new force fields have been added and can be used with OEMolBuilder and OETorDriver in OEOmega:
  - $-$  SAGE
  - SAGE NOESTAT
  - SAGE\_SHEFF
- The behavior of OEFlipperOptions has changed. New flags have been added to OEFlipperOptions, facilitating more complete decoupling of individual flags and more selective enumeration of specific stereocenter classes and environments than was previously possible.
- A new option class, OEFlipperClassicOptions, has been added to allow a detailed comparison of the new flag behaviors with the previous OEFlipper enumeration behavior. This class will be deprecated in a future toolkit release.
- The internal algorithm for storage and usage of torsion rules in  $OETorLib$  has been modified to improve performance when working with a library containing a large set of rules.
- A new return code FailedCharges has been added to OEOmegaReturnCode to indicate failures due to partial charge assignment.

# 6.3.2 Minor bug fixes

• The order of torsion rules in the default *OETorLib* has been changed to ensure that a specific rule is not ignored due to the presence of a more generic rule.

# 6.4 Omega TK 4.2.2

# 6.4.1 Minor bug fixes

• The OEOmega method Build will now fail when MCS matching is requested but a corresponding FixMol has not been set.

# 6.5 Omega TK 4.2.1

## 6.5.1 New features

- The ability to fix a part of a molecule during conformer generation based on maximum common substructure (MCS) has been added. The following new methods have been added to the  $OEConfig$  ix  $Options$  to enable this functionality:
  - $-$  SetFixMCS
  - $-$  GetFixMCS
  - SetMCSFunc
  - GetMCSFunc
  - $-$  SetMCSType
  - $-$  GetMCSType
  - SetMCSMinAtoms
  - GetMCSMinAtoms
- New methods SetIgnoreStereo and GetIgnoreStereo have been added to OEMolBuilderOptions to allow continuation of conformer generation when specified stereo signatures in a molecule could not be honored.
- New methods SetMaxEnumConfs and GetMaxEnumConfs have been added to OEMolBuilderOptions to allow specifying the maximum number of conformers to be generated from ring enumeration, nitrogen enumeration, and/or hydrogen sampling.
- Verbose mode logging now reports torsion angles sampled, along with the rules, during torsion driving.

## 6.5.2 Minor bug fixes

- Conformer generation with OEOmega.Build or OEMolBuilder.Build now fails correctly when specified stereo signatures on a molecule cannot be honored. The existing behavior, to carry on even if stereo signatures could not be honored, can be obtained by setting *IgnoreStereo* to true.
- Ring fragment building during OEOmega.Build, OEFragBuilder.Build, OEMolBuilder.Build, or GenerateMissing Frags now properly honors the SetFragKeep parameter regarding the maximum number of generated fragment conformers to be kept.

# 6.6 Omega TK 4.2.0

## 6.6.1 New features

- Support for consideration of MDL enhanced stereo collection information during isomer generation has been added. The OEFlipperOptions class adds a new SetEnhancedStereo option to control consideration of explicit enhanced stereo groups defined by OEGroupBase information that may have been read from V3000 the OEFormat values indicating SDF structures or CXSMILES files.
- A new method, SetFragBuilderMode, has been added that allows setting fragment building mode in the corresponding OEFragBuilderOptions.

# 6.6.2 Minor bug fixes

• Internal generic data tags applied to the flip-ee used for performance during the flipping activity are now stripped from the structures returned by OEFlipper as this information is no longer relevant.

# 6.7 Omega TK 4.1.2

Fall 2021

## 6.7.1 Minor bug fixes

- An issue with overwriting partial charges of atoms in input molecules has been fixed.
- The Generating Stereoisomers example has been modified to use OEFlipperOptions.
- An issue running OEOmega when both SetUseGPU and SetSampleHydrogens are set to True has been fixed by disabling SetUseGPU in these cases.

# 6.8 Omega TK 4.1.1

July 2021

## 6.8.1 New features

• Function OEOmegaSystemHasGPU has been added to test for availability of a GPU.

# 6.8.2 Major bug fixes

- A bug that caused a segmentation fault when zero was passed to the  $SetMaxConfs$  method has been fixed.
- And issue that prevented oeomega from using the GPU in child threads when OEOmegalsGPUReady was called from the main thread has been fixed.

# 6.8.3 Minor bug fixes

- An issue with stereo specificity of the imino group (=NH) not being retained in a macrocycle has been fixed.
- An issue with loss of relative stereo marked atoms in macrocycle mode has been fixed.

# 6.9 Omega TK 4.1.0

Fall 2020

# 6.9.1 New features

- GPU-Omega now requires a minimum NVIDIA Driver version of 450.x and a minimum GPU compute capability of 3.5. See NVIDIA Drivers and Supported GPUs for more details.
- Conformer generation using dense mode now defaults to running on the CPU instead of the GPU. The other torsion-driving sampling modes (sparse, rocs, fastrocs, and pose) will still run on a GPU by default if one is available on a Linux platform. For details on how to run with dense mode sampling on a GPU, see the Usage section of the **GPU-Omega** docs.
- A new class, OEFlipperOptions, has been added that defines parameters for specifying stereo centers and other options.
- OEFlipper has been updated to take a molecule and an OEFlipperOptions value. The old version of OEFlipper that takes five parameters has been deprecated.
- A new function, OEFlipperStereoCenters, has been added that returns a number of undefined stereo centers in a molecule as interpreted by OEFlipper.

# 6.9.2 Major bug fixes

- A memory leak in GPU-Omega has been fixed.
- An issue with generating conformers on the CPU using child processes with the same OEOmega object has been fixed.
- GPU-Omega no longer throws an error when attempting to generate conformers with the same OEOmega object in child processes. Instead, it falls back to the CPU. To use GPU-Omega with child processes, each child must construct a new OEOmega object.

## 6.9.3 Minor bug fixes

• OEConfGen now clears all fragment libraries. Previous releases did not clear the internal shared fragment library (a shared memory library of fragments accrued while generating conformers with the same OEOmega object).

## **6.9.4 Documentation changes**

• OEOmegaReturnCode has been updated to reflect the current possible values.

# 6.10 Omega TK 4.0.0.6

· OEMolBuilder.Build no longer enumerates specified nitrogen when OEMolBuilderOptions. GetEnumNitrogen is OENitrogenEnumeration\_Unspecified.

# 6.11 Omega TK 4.0.0

As part of the integration of OEToolkits and OEApplications into a single release, the version number of Omega TK has been upgraded to 4.0.0 to make it consistent with that of the OMEGA application.

## 6.11.1 New features

• GPU-Omega, a GPU-accelerated implementation of the torsion driving algorithm, is now available. This will make use of any suitable Nvidia GPU on supported Linux platforms by default for classic mode runs. It is advised to read the GPU-Omega section of the documentation to ensure that your system meets all the prerequisites and that availability is understood for the different sampling modes. On systems that do not meet the requirements, GPU-Omega will be disabled and fall back to the CPU.

#### **GPU-Omega** introduces the following new APIs:

- OETorDriveOptions.GetUseGPU
- OETorDriveOptions. SetUseGPU
- OEOmegaIsGPUReady
- The following APIs have been promoted from preliminary API to stable API status:
  - $-$  OEMacrocycleOmega
  - OEMacrocycleOmegaOptions
  - OEMacrocycleBuilder
  - OEMacrocycleBuilderOptions
  - OEMolBuilder
  - OEMolBuilderOptions
  - OEConformerBuilder
  - OEFragBuilder
  - OEFragBuilderOptions

- OEFragBuilderOptions
- OETorDriver
- OETorDriveOptions
- OEFragOptions
- OERingFragOptions
- OEConfFixOptions
- OEConfSlicer
- OESliceEnsembleOptions
- OEFragBuilderMode
- OEOmegaReturnCode
- OEGetOmegaError
- OEIsMacrocycle
- The OEOmegaOptions class has been simplified and now consists of multiple sub-options: OEMolBuilderOptions, OETorDriveOptions, OESliceEnsembleOptions, and OEConfFixOptions. The specific methods to set or get option values are now provided through these sub-option classes.
- A new abstract base class, OEBuilderBase, has been added that contains the basic functionality of the builders that use a fragment library.
- The following new methods have been added to  $OEConfigFixOptions$ :
  - OEConfFixOptions.GetAtomExpr
  - OEConfFixOptions. SetAtomExpr
  - OEConfFixOptions.GetBondExpr
  - OEConfFixOptions. SetBondExpr
- . Two new methods, OEFragBuilderOptions. SetForceField and OEFragBuilderOptions. GetForceField, have been added to the OEFragBuilderOptions class.
- OEMacrocycleBuilderOptions.SetRandomSeed  $\bullet$  Two methods, and new OEMacrocycleBuilderOptions. GetRandomSeed, have been added to the OEMacrocycleBuilderOptions class.
- The following new methods have been added to OEMacrocycleOmegaOptions:
  - OEMacrocycleOmegaOptions.GetEnergyWindow
  - OEMacrocycleOmegaOptions. SetEnergyWindow
  - OEMacrocycleOmegaOptions.GetMaxConfs
  - OEMacrocycleOmegaOptions. SetMaxConfs
- A new method,  $OEMOIBuilder.Prep$ , has been added to the  $OEMOIBuilder$  class to prepare molecules for building.

## 6.11.2 Minor bug fixes

- The following methods now return bool, instead of a void:
  - OEConfFixOptions. SetFixDeleteH
  - OEConfFixOptions. SetFixMaxMatch
  - OEConfFixOptions. SetFixMol
  - OEConfFixOptions. SetFixPredicate
  - OEConfFixOptions. SetFixRMS
  - OEConfFixOptions. SetFixSmarts
  - OEConfFixOptions. SetFixSubSearch
  - OEConfFixOptions. SetFixUniqueMatch
  - OEFragOptions. SetEnergyWindow
  - OEFragOptions. SetFragGen
  - OEFragOptions. SetFragKeep
  - OEFragOptions. SetRMS
  - OEFragOptions. SetTimeLimit
  - OEMacrocycleBuilderOptions. SetDielectricConst
  - OEMacrocycleBuilderOptions. SetRefTolerance
  - OEMacrocycleBuilderOptions. SetSkipRefinement
  - OEMacrocycleOmegaOptions.SetIterCycleSize
  - OEMacrocycleOmegaOptions. SetMaxIter
  - OEMolBuilderOptions. SetCanonOrder
  - OEMolBuilderOptions. SetEnumNitrogen
  - OEMolBuilderOptions. SetEnumRing
  - OEMolBuilderOptions. SetFromCT
  - OEMolBuilderOptions. SetSampleHydrogens
  - OEMolBuilderOptions. SetStrictAtomTypes
  - OERingFragOptions. SetStartFactor
  - OESliceEnsembleOptions. SetEnergyWindow
  - OESliceEnsembleOptions. SetEnergyRange
  - OESliceEnsembleOptions. SetMaxConfs
  - OESliceEnsembleOptions. SetMaxConfRange
  - OESliceEnsembleOptions. SetMaxTerminalHeavy
  - OESliceEnsembleOptions. SetRangeIncrement
  - OESliceEnsembleOptions. SetRMSThreshold
  - OESliceEnsembleOptions.SetRMSRange
  - OETorDriveOptions. SetCommentEnergy

- OETorDriveOptions. SetMaxRotors
- OETorDriveOptions. SetMaxSearchTime
- OETorDriveOptions. SetRotorOffset
- OETorDriveOptions. SetRotorPredicate
- OETorDriveOptions. SetSDEnergy
- OETorDriveOptions. SetTorLib
- New arguments have been added to the OEMacrocycleBuilder. Build method for consistency with the other classes in OMEGA.
- The following preliminary APIs have been removed from the OESliceEnsembleOptions class:
  - OESliceEnsembleOptions::SetEnergyThreshold
  - OESliceEnsembleOptions::GetEnergyThreshold
  - OESliceEnsembleOptions::SetSliceByEnergy
  - OESliceEnsembleOptions::GetSliceByEnergy
- Two methods, OETorDriver::SetForceField and OETorDriver::GetForceField, that were preliminary APIs, have been removed from the OETorDriver class.
- . Two methods, OEMolBuilder::SetForceField and OEMolBuilder::GetForceField, that were preliminary APIs, have been removed from the OEMolBuilder class.
- . Two methods, OEFragBuilder::SetForceField and OEFragBuilder::GetForceField, that were preliminary APIs, have been removed from the OEFragBuilder class.
- . Two methods, OEMakeFragLib::SetForceField and OEMakeFragLib::GetForceField, that were preliminary APIs, have been removed from the OEMakeFragLib class.
- . Two methods, OEConfFixOptions::ClearFixFile and OEConfFixOptions::SetFixFile, that were preliminary APIs, have been removed from the OEConfFixOptions class. Accordingly,  $OEConffixOptions. SetFixMod 1$  has an overload that takes a molecule file as input.
- OETOrDriver. GenerateConfs now errors out properly if the input molecule is not 3D.
- OEOmega, Build now properly de-duplicates the generated conformers in the case when  $MaxConfs$  is set to 0.
- $OEOmega$ . Build no longer copies the molecule title to every conformer.
- OEGetOmegaError now returns a value for each entry in the OEOmegaReturnCode namespace.
- · OEMakeFragLib.GenerateMissingFrags and OEFragBuilder.Build now perform a deduplication on the generated fragment conformers.
- OEFragBuilder. Build now returns an appropriate failure code if it fails due to lack of atom types.
- SampleHydrogens is now robust when the potential number of conformers is too high due to hydrogen sampling.
- Default values for the parameters in OEMacrocycleOmegaOptions are now consistent with their respective counterparts in the **OMEGA** command line application.
- OEIsMacrocycle has been improved to better identify macrocycles when hetero atoms are involved.

# **6.11.3 Documentation changes**

- A GPU-Omega chapter has been added to the documentation.
- OMEGA examples have been updated to reflect the latest changes for all supported languages.

# 6.11.4 General Notices

• In the C++ toolkit, GPU-Omega is not available on RHEL8 or Ubuntu18 in this release.

# 6.12 Omega TK 2.9.1

# 6.12.1 New features

- The following new methods have been added to the OESliceEnsembleOptions class to make it more efficient with large macrocycles and energy-optimized structures:
  - SetEnergyThreshold
  - GetEnergyThreshold
  - OESliceEnsembleOptions. SetMaxTerminalHeavy
  - OESliceEnsembleOptions.GetMaxTerminalHeavy
  - SetSliceByEnergy
  - GetSliceByEnergy
- A new class, *OEConfSlicer*, has been added that complements the *OES1iceEnsemble* method. In addition, a new overload has been added to OES1iceEnsemble that provides broader functionality by working with an OESliceEnsembleOptions object.
- Deduplication of conformer ensembles in *OEMacrocycleOmega* has been improved by replacing two preliminary API methods, OEConfGen:: OEMacrocycleOmegaOptions:: SetDeduplicateScanOptions OEConfGen::OEMacrocycleOmegaOptions::GetDeduplicateScanOptions, and with OEMacrocycleOmegaOptions.SetSliceEnsembleOptions and OEMacrocycleOmegaOptions.GetSliceEnsembleOptions,respectively.

# 6.12.2 Major bug fixes

- OEMacrocycleOmega. Build now generates conformer ensembles that are centered and aligned to each other, and with better deduplication.
- An issue that occasionally caused knotted conformations of some complex molecules generated with OEOmega. Build has been fixed.

# 6.12.3 Minor bug fixes

- OEOmega. Build now properly adds hydrogens to single heavy atom molecules.
- preliminary API OEConfGen:: OEDuplicateScanner  $\bullet$  Two classes, and OEConfGen:: OEDuplicateScanOptions, have been removed.
- . Two preliminary API methods, OEConfGen:: OETorDriveOptions:: SetIncludeInput and OEConfGen::OETorDriveOptions::GetIncludeInput, have been removed.
- Defaults  $f_{\Omega}r$ OEMolBuilderOptions.SetEnumNitrogen SetSampleHyand drogens OEOmegaSampling Dense mode been changed in the have from OENitrogenEnumeration Unspecified and false to OENitrogenEnumeration All and true, respectively.
- An issue regarding the OEOmegaOptions. SetEnergyWindow not being properly honored for some molecules with OEOmega. Build has been fixed.
- Fragment conformations for CCN and CN have been updated in the built-in fragments library to properly reflect the tetrahedral geometry.
- Occasional failure to generate conformations for molecules containing chiral N=N or C=N bonds has been fixed.

# 6.13 Omega TK 2.9.0

## 6.13.1 New features

- A new method,  $OEOmeqa$ . Build, has been introduced that provides a proper return code on failure, unlike the operator(). Operator() was then deprecated.
- A new namespace, OEOmegaReturnCode, has been introduced that defines return codes for various API methods.
- A new function,  $OEGetOmegaError$ , has been introduced that returns error descriptions corresponding to various Omega return codes.
- A new method,  $OETorLib$ ,  $GetTorRule$ , has been introduced that returns the torsion rule corresponding to a rotatable bond.
- A new method, OETOrLib. HasTOrRule, has been introduced that determines whether a torsion rule is defined for a rotatable bond.
- A new function,  $OEGetTorValues$ , has been introduced that provides torsion values from a torsion ruledefined OESubSearch object.
- The following preliminary APIs, which were introduced in **Omega TK 2.8.0**, have been modified to return an unsigned return code instead of a bool:
  - OEConformerBuilder.Build
  - OEFragBuilder. Build
  - OEMacrocycleBuilder. Build
  - OEMacrocycleOmega.Build
  - OEMolBuilder.Build
  - OETorDriver. GenerateConfs

**Note:** The change in the preliminary APIs mentioned above is a breaking change and needs to be addressed properly by scripts and code that use these APIs. Since bool and unsigned are mutually compatible, any scripts or code using these API methods may continue to function without a proper fix and may not give any runtime or compile-time error. However, the end results obtained from such scripts or codes could be incorrect.

- The following APIs have been modified to be const and some of their arguments have been modified to be const:
  - OEConformerBuilder.Build
  - OEFragBuilder. Build
  - OEMacrocycleBuilder.Build
  - OEMacrocycleOmega.Build
  - OEMakeFragLib.GenerateMissingFrags
  - OEMakeFragLib.GetMissingFrags
  - OEMolBuilder.Build
  - $-$  operator()
  - OEIsMacrocycle
  - OETorDriveOptions. ExceedsMaxRotors
  - OETorDriver. GenerateConfs
- The following APIs have been modified to return a bool instead of a void:
  - OEBuilderBase.AddFragLib
  - OETorLib.AddTorsionLibrary
  - OETorLib. SetTorsionLibrary
  - OETorLib. ResetTorsionLibrary

# 6.13.2 Major bug fixes

- An issue that caused an occasional Coulombic collapse for conformations of zwitterionic molecules generated with the Macrocycle algorithm has been fixed.
- An issue that caused *Omega*<sup>\*</sup> to fail to produce conformations for molecules containing chiral nitrogen atom using macrocycle mode has been fixed.

# 6.13.3 Minor bug fixes

- OEConformerBuilder. Build no longer fails due to unspecified stereo in the input molecule.
- OEConformerBuilder. Build no longer generates more than one conformer in the output molecule.
- OEConformerBuilder. Build no longer writes anything in standard output.
- $\bullet$  The default for EnumNitrogen in *OEMolBuilderOptions* has been changed from OENitrogenEnumeration\_All to OENitrogenEnumeration\_Unspecified so that any userspecified stereo information is not lost by default.

- OEMacrocycleOmega. Build has been fixed to generate conformers in cases when a MaxConfs of 1 is requested.
- operator() now generates a title in the output even when the input molecule has no OEMCMolBase title.
- operator() now produces a title in output conformers when OEOmegaOptions. GetWarts is false.
- operator() now produces correct conformer coordinates when both  $OEOmeqaOptions$ . Set IncludeInput and OEMolBuilderOptions. SetCanonOrder are set to be true.
- Omega calculations no longer repeat an error message.
- OEMakeFragLib. GenerateMissingFrags no longer crashes with extreme energy window value.
- The torsion rule for  $[CH3:1]$   $[CK4H:2]$   $([CH3])$   $[CK4H2:3]$   $[!#1:4]$  in the default torsion library has been improved.

# 6.14 Omega TK 2.8.0

### 6.14.1 New features (Preliminary API)

The following new preliminary APIs have been added for macrocycle functionality in the Omega TK:

- OEMacrocycleOmega and OEMacrocycleOmegaOptions classes to generate a macrocycle molecule conformer ensemble
- OEMacrocycleBuilder and OEMacrocycleBuilderOptions classes to generate a single conformer structure of a macrocycle molecule
- . OEConfGen::OEDuplicateScannerandOEConfGen::OEDuplicateScanOptions classes to enable fast scanning and removal of duplicate conformers from a conformer ensemble
- OEISMacrocycle function to detect if a molecule contains a macrocycle

The following new preliminary APIs have been added to enhance small molecule conformer generation functionality in the **Omega TK**:

- OEMakeFragLib class to generate a fragment library
- OEMolBuilder and OEMolBuilderOptions classes to generate small molecule conformers using a fragment library
- OEConformerBuilder class to generate a single conformer structure of a small molecule
- OEFragBuilder and OEFragBuilderOptions classes to generate fragment conformers using distance geometry. The OEFragBuilderOptions class combines multiple options related to building a fragment library for both OEMakeFragLib and OEMolBuilder.
- OETorDriver and OETorDriveOptions classes to generate small molecule conformer ensembles from torsion driving
- *OEFragOptions* class to store options related to generating a single fragment structure
- *OERingFragOptions* class to store options related to generating a single ring fragment structure
- *OEConfFixOptions* class to store options related to fixing part of the structure of small molecules during a conformational search
- OESliceEnsembleOptions class to store options for ensemble pruning during a small molecule conformational search
- OEFragBuilderMode namespace to set up OEFragBuilderOptions for specific uses

# 6.14.2 New features

New additions and modifications have been made to existing APIs to enhance small molecule conformer generation functionality in Omega TK:

- $\bullet$  Three new modes. OEOmegaSampling\_Pose, OEOmegaSampling\_ROCS, and OEOmegaSampling\_FastROCS, have been added to the OEOmegaSampling namespace.
- A new torsion library based on the work of Wolfgang Guba has been added. A new namespace, OETOrLibType, has been introduced to provide options for the choice of torsion library. Additionally, the OETorLib constructor now takes a torsion type value from the OETOrLibType namespace. Also, a new overload of the OETOrLib. Set TorsionLibrary method has been added to allow setting the desired torsion library from the above-mentioned namespace.
- The OEOmegaForceFieldType namespace has been replaced by the OEMMFFSheffieldFFType namespace. The new namespace adds 4 new options for the force field used in the OEOmega class. These new options are based on a modified variation of the OEMMFF94sParams parameters that prefers the appropriate axial/equatorial conformers for many molecules in OEOmega.

# 6.14.3 Major bug fixes

- The SMILES string hash in the internal fragment library in the OEOmega class has been updated to reflect the proper canonicalization of the fragments. This ensures that OEOmega will always find the fragment in the library if it exists.
- The default search force field in the OEOmega class has been changed to the newly introduced OEMMFFSheffieldFFType\_MMFF94Smod\_NOESTAT type to generate more appropriate axial/equatorial conformers.
- An issue that caused the OEOmega class to not honor the parity bits on relative stereo marked rings has been  $fixed$

# 6.14.4 Minor bug fixes

• An issue that caused the OEOmega class to report the same warning about atoms multiple times has been fixed.

# **6.14.5 Documentation changes**

The following C++ and Python examples have been added to demonstrate using the new preliminary APIs:

- New examples have been added to the *Macrocycle Examples* section that generate a macrocycle conformer ensemble or a single macrocycle conformer.
- A new example has been added to the *Fragment Library generation Examples* section that generates fragment libraries.
- A new example has been added to the Generating Torsion Driven Conformation Examples section that generates a conformer ensemble by torsion driving from a given 3D structure.

# 6.15 Omega TK 2.7.0

• Minor internal improvements have been made.

# 6.16 Omega TK 2.6.7

## 6.16.1 New features

• A new torsion library, based on the work of Guba et al. [Guba-2016], has been added. The OETorLib constructor now includes an optional parameter in the OETOTLIDType namespace to select either the original or new OETOrLibType\_GubaV21 torsion library. A new overload of the SetTorsionLibrary method can also be used to change the torsion library.

# **6.16.2 Documentation changes**

• The function *OEFlipper* now removes molecule coordinates during its processing. This behavior change was introduced in the 2017. Feb release.

# 6.17 Omega TK 2.6.6

# 6.17.1 Major bug fixes

• The OEFlipper function with forceFlip=false no longer flips 3D molecules if stereo is defined.

# 6.17.2 Minor bug fixes

• Molecule titles have been added to some emitted warnings to aid in identifying problematic molecules.

# 6.18 Omega TK 2.6.5

## 6.18.1 New features

- New functionality has been added for generating a densely sampled set of conformers, as required during conformer free energy calculations using OEFreeFormConf.
- Omega has used random coordinate embedding with distance-geometry refinement to generate initial 3D fragment and ring conformers for more than a decade. The pseudo-random number generator used has been upgraded to an implementation of the Mersenne Twister adapted from the work of Kohei Takeda.
- Omega now recognizes and adjusts ring sampling for macrocycles. This improves reproduction of small and medium-sized macrocycle structures without increasing maximum ensemble sizes.
- A new class, *OEOmegaOptions*, has been added that sets all options of the *OEOmega* object during its construction. All the OEOmega methods with the same name as their OEOmegaOptions counterparts are now deprecated except for the options for fraglib, which are still maintained through the OEOmega interface.

The following table shows the older, deprecated functions and their new option replacements:

| Deprecated Method                       | New option Method                              |
|-----------------------------------------|------------------------------------------------|
| OEConfGen::OEOmega::SetCommentEnergy    | OEConfGen::OEOmegaOptions::SetCommentEnergy    |
| OEConfGen::OEOmega::GetCommentEnergy    | OEConfGen::OEOmegaOptions::GetCommentEnergy    |
| OEConfGen::OEOmega::SetIncludeInput     | OEConfGen::OEOmegaOptions::SetIncludeInput     |
| OEConfGen::OEOmega::GetIncludeInput     | OEConfGen::OEOmegaOptions::GetIncludeInput     |
| OEConfGen::OEOmega::SetRotorOffset      | OEConfGen::OEOmegaOptions::SetRotorOffset      |
| OEConfGen::OEOmega::GetRotorOffset      | OEConfGen::OEOmegaOptions::GetRotorOffset      |
| OEConfGen::OEOmega::SetSDEnergy         | OEConfGen::OEOmegaOptions::SetSDEnergy         |
| OEConfGen::OEOmega::GetSDEnergy         | OEConfGen::OEOmegaOptions::GetSDEnergy         |
| OEConfGen::OEOmega::SetWarts            | OEConfGen::OEOmegaOptions::SetWarts            |
| OEConfGen::OEOmega::GetWarts            | OEConfGen::OEOmegaOptions::GetWarts            |
| OEConfGen::OEOmega::SetBuildForceField  | OEConfGen::OEOmegaOptions::SetBuildForceField  |
| OEConfGen::OEOmega::GetBuildForceField  | OEConfGen::OEOmegaOptions::GetBuildForceField  |
| OEConfGen::OEOmega::SetCanonOrder       | OEConfGen::OEOmegaOptions::SetCanonOrder       |
| OEConfGen::OEOmega::GetCanonOrder       | OEConfGen::OEOmegaOptions::GetCanonOrder       |
| OEConfGen::OEOmega::SetFromCT           | OEConfGen::OEOmegaOptions::SetFromCT           |
| OEConfGen::OEOmega::GetFromCT           | OEConfGen::OEOmegaOptions::GetFromCT           |
| OEConfGen::OEOmega::SetFixRMS           | OEConfGen::OEOmegaOptions::SetFixRMS           |
| OEConfGen::OEOmega::GetFixRMS           | OEConfGen::OEOmegaOptions::GetFixRMS           |
| OEConfGen::OEOmega::SetFixDeleteH       | OEConfGen::OEOmegaOptions::SetFixDeleteH       |
| OEConfGen::OEOmega::GetFixDeleteH       | OEConfGen::OEOmegaOptions::GetFixDeleteH       |
| OEConfGen::OEOmega::SetFixUniqueMatch   | OEConfGen::OEOmegaOptions::SetFixUniqueMatch   |
| OEConfGen::OEOmega::GetFixUniqueMatch   | OEConfGen::OEOmegaOptions::GetFixUniqueMatch   |
| OEConfGen::OEOmega::SetFixMaxMatch      | OEConfGen::OEOmegaOptions::SetFixMaxMatch      |
| OEConfGen::OEOmega::GetFixMaxMatch      | OEConfGen::OEOmegaOptions::GetFixMaxMatch      |
| OEConfGen::OEOmega::SetStrictAtomTypes  | OEConfGen::OEOmegaOptions::SetStrictAtomTypes  |
| OEConfGen::OEOmega::GetStrictAtomTypes  | OEConfGen::OEOmegaOptions::GetStrictAtomTypes  |
| OEConfGen::OEOmega::SetStrictStereo     | OEConfGen::OEOmegaOptions::SetStrictStereo     |
| OEConfGen::OEOmega::GetStrictStereo     | OEConfGen::OEOmegaOptions::GetStrictStereo     |
| OEConfGen::OEOmega::SetEnumNitrogen     | OEConfGen::OEOmegaOptions::SetEnumNitrogen     |
| OEConfGen::OEOmega::GetEnumNitrogen     | OEConfGen::OEOmegaOptions::GetEnumNitrogen     |
| OEConfGen::OEOmega::SetEnumRing         | OEConfGen::OEOmegaOptions::SetEnumRing         |
| OEConfGen::OEOmega::GetEnumRing         | OEConfGen::OEOmegaOptions::GetEnumRing         |
| OEConfGen::OEOmega::SetSampleHydrogens  | OEConfGen::OEOmegaOptions::SetSampleHydrogens  |
| OEConfGen::OEOmega::GetSampleHydrogens  | OEConfGen::OEOmegaOptions::GetSampleHydrogens  |
| OEConfGen::OEOmega::SetEnergyWindow     | OEConfGen::OEOmegaOptions::SetEnergyWindow     |
| OEConfGen::OEOmega::GetEnergyWindow     | OEConfGen::OEOmegaOptions::GetEnergyWindow     |
| OEConfGen::OEOmega::SetEnergyRange      | OEConfGen::OEOmegaOptions::SetEnergyRange      |
| OEConfGen::OEOmega::GetEnergyRange      | OEConfGen::OEOmegaOptions::GetEnergyRange      |
| OEConfGen::OEOmega::SetMaxConfs         | OEConfGen::OEOmegaOptions::SetMaxConfs         |
| OEConfGen::OEOmega::GetMaxConfs         | OEConfGen::OEOmegaOptions::GetMaxConfs         |
| OEConfGen::OEOmega::SetMaxConfRange     | OEConfGen::OEOmegaOptions::SetMaxConfRange     |
| OEConfGen::OEOmega::GetMaxConfRange     | OEConfGen::OEOmegaOptions::GetMaxConfRange     |
| OEConfGen::OEOmega::SetMaxRotors        | OEConfGen::OEOmegaOptions::SetMaxRotors        |
| OEConfGen::OEOmega::GetMaxRotors        | OEConfGen::OEOmegaOptions::GetMaxRotors        |
| OEConfGen::OEOmega::SetMaxSearchTime    | OEConfGen::OEOmegaOptions::SetMaxSearchTime    |
| OEConfGen::OEOmega::GetMaxSearchTime    | OEConfGen::OEOmegaOptions::GetMaxSearchTime    |
| OEConfGen::OEOmega::SetRangeIncrement   | OEConfGen::OEOmegaOptions::SetRangeIncrement   |
| OEConfGen::OEOmega::GetRangeIncrement   | OEConfGen::OEOmegaOptions::GetRangeIncrement   |
| OEConfGen::OEOmega::SetRMSRange         | OEConfGen::OEOmegaOptions::SetRMSRange         |
| OEConfGen::OEOmega::GetRMSRange         | OEConfGen::OEOmegaOptions::GetRMSRange         |
| OEConfGen::OEOmega::GetRMSRange         | OEConfGen::OEOmegaOptions::GetRMSRange         |
| OEConfGen::OEOmega::SetRMSThreshold     | OEConfGen::OEOmegaOptions::SetRMSThreshold     |
| OEConfGen::OEOmega::GetRMSThreshold     | OEConfGen::OEOmegaOptions::GetRMSThreshold     |
| OEConfGen::OEOmega::SetSearchForceField | OEConfGen::OEOmegaOptions::SetSearchForceField |
| OEConfGen::OEOmega::GetSearchForceField | OEConfGen::OEOmegaOptions::GetSearchForceField |
| OEConfGen::OEOmega::SetTorsionDrive     | OEConfGen::OEOmegaOptions::SetTorsionDrive     |
| OEConfGen::OEOmega::GetTorsionDrive     | OEConfGen::OEOmegaOptions::GetTorsionDrive     |
| OEConfGen::OEOmega::SetDielectric       | OEConfGen::OEOmegaOptions::SetDielectric       |
| OEConfGen::OEOmega::GetDielectric       | OEConfGen::OEOmegaOptions::GetDielectric       |
| OEConfGen::OEOmega::SetExponent         | OEConfGen::OEOmegaOptions::SetExponent         |
| OEConfGen::OEOmega::GetExponent         | OEConfGen::OEOmegaOptions::GetExponent         |
| OEConfGen::OEOmega::SetFixMol           | OEConfGen::OEOmegaOptions::SetFixMol           |
| OEConfGen::OEOmega::GetFixMol           | OEConfGen::OEOmegaOptions::GetFixMol           |
| OEConfGen::OEOmega::SetFixFile          | OEConfGen::OEOmegaOptions::SetFixFile          |
| OEConfGen::OEOmega::ClearFixFile        | OEConfGen::OEOmegaOptions::ClearFixFile        |
| OEConfGen::OEOmega::SetFixQuery         | OEConfGen::OEOmegaOptions::SetFixQuery         |
| OEConfGen::OEOmega::SetFixSmarts        | OEConfGen::OEOmegaOptions::SetFixSmarts        |
| OEConfGen::OEOmega::GetFixSubSearch     | OEConfGen::OEOmegaOptions::GetFixSubSearch     |
| OEConfGen::OEOmega::SetTorLib           | OEConfGen::OEOmegaOptions::SetTorLib           |
| OEConfGen::OEOmega::GetTorLib           | OEConfGen::OEOmegaOptions::GetTorLib           |

Table 1 - continued from previous page

# 6.19 Omega TK 2.6.4

# 6.19.1 Minor bug fixes

• Memory allocation for limited stack memory usage has been improved.

# 6.20 Omega TK 2.6.3

# 6.20.1 Major bug fixes

• The problem of stripping off all SD data from a multi-conformer molecule has been fixed by introducing an overloaded version of the OEF1ipper function that takes an OEMCMolBase object.

# 6.20.2 Minor bug fixes

 $\bullet$  operator() no longer returns  $t$  rue when it fails due to a timeout.

### **6.20.3 Documentation changes**

• Method operator() is now documented.

# 6.21 Omega TK 2.6.2

## 6.21.1 Major bug fixes

• SetSearchForceField and SetBuildForceField no longer accept illegal inputs and throw a warning for incorrect force field types.

# **6.21.2 Documentation changes**

• SetSearchForceField and SetBuildForceField are now documented in more detail.

# 6.22 Omega TK 2.6.1

# 6.22.1 Minor bug fixes

• OEOmegaGetLibraryRelease and OEOmegaGetLibraryVersion will now throw deprecation warnings and will be removed in a future release. We recommend using OEOmegaGetRelease and OEOmegaGetVersion instead.

# 6.23 Omega TK 2.6.0

# 6.23.1 Major bug fixes

• OEOmega will no longer cause non-deterministic amounts of superfluous messages to be thrown to OEThrow when running in multiple threads. This had been happening because OEOmega calls OEErrorHandler. Set Level to selectively silence warning messages it knows to be benign. This was fixed by only allowing the OEErrorHandler. SetLevel method to change the error level for the current thread, using an OEThread-Local object to control message visibility.

### See also:

The OpenEye GitHub account contains an example of a multi-threaded OMEGA implementation.

# **6.23.2 Documentation changes**

· OEOmegaGetLibraryRelease and OEOmegaGetLibraryVersion have been marked deprecated and will be removed in a future release. Please use OEOmegaGetRelease and OEOmegaGetVersion instead.

# 6.24 Omega TK 2.5.7

# 6.24.1 Minor bug fixes

- The OEOmega constructor will now initialize all data members appropriately to avoid subtle unreproducible errors based on random values in memory.
- Calling SetWarts with true had been broken until the 2014. Oct release. The output conformers would have the numeric index(wart) in the . oeb format but not the . sdf format. This is now fixed. The default behavior of OETautomerOptions has been changed from true to false when applying a numeric index(wart) to titles.

# 6.24.2 C#-specific changes

• OETorLib. AddTorsionRule is now usable from C#.

# 6.25 Omega TK 2.5.6

## 6.25.1 New features

• Omega TK conformers can be produced in double precision and round-tripped through rotor-offset-compress OEB files.

# 6.25.2 Minor bug fixes

• Rare possible race condition prevented.

## **6.25.3 Documentation fixes**

• Examples will now check the return value of the omega process before writing out the molecule.

# 6.26 Omega TK 2.5.5

## 6.26.1 Minor bug fixes

• Removed unbounded stack allocations.

## **6.26.2 Documentation fixes**

- Omega TK examples for Java, C#, and Python will now check to see whether OEOmega failed and not write the molecule in those cases.
- Omega TK examples for Java, C# and Python were renamed to more accurately reflect their function.
- · OETorLib. AddTorsionRule more thoroughly documented.

# 6.27 Omega TK 2.5.4

### 6.27.1 New features

• The namespace OESliceEnsembleDefaults has been created with defaults for OESliceEnsemble. These defaults have been updated in order to match the defaults that OMEGA uses during conformer generation.

# 6.27.2 Major bug fixes

- Fixed possible crash caused when reading empty lines in torsion library files.
- Fixed OENitrogenEnumeration\_All bug where was a equivalent to OENitrogenEnumeration\_Unspecified. Now OENitrogenEnumeration All will properly enumerate nitrogen atoms with specified stereochemistry.

# 6.27.3 Minor bug fixes

• A bug has been fixed where OESubSearch warnings could appear due to unset bond stereochemistry. Bond stereochemistry is now always set properly.

# 6.28 Omega TK 2.5.3

### 6.28.1 New features

• OEAddGlobalFragLib added to allow a given fragment library to be preloaded into the global fragment library where it can be shared among all OEOmega instances.

# 6.28.2 Minor bug fixes

- The wart symbol has been changed from @ to in order to help with parsing SMILES formatting.
- Bond stereochemistry is now properly perceived when strictstereo is set to *false*. Previously, there could be an OESubSearch warning due to unperceived bond stereochemistry.
- The OENitrogenEnumeration namespace has been created. The namespace constants should be used in place of magic numbers.

# 6.29 Omega TK 2.5.2

### 6.29.1 New features

• The fragment library is now shared across multiple instances of the  $OEOmega$  abjects in a thread-safe manner. This can greatly reduce the amount of memory needed to run a multi-threaded version of Omega TK. For example, the memory consumption of Omega TK running across 8-cores dropped from 715MB to 258MB for 14,000 lead-like compounds from MDDR. This can also lead to a performance improvement since expensive fragment generation can sometimes be avoided if it has already been completed by another thread.

- The internal fragment library for the Omega TK shared library is now stored in a more space and time efficient manner. Creating an OEOmega object and running it on a single molecule should now be faster. For example, running the simple omega. py example on a single benzene now takes 0.25 seconds instead of 0.83 seconds. Your mileage may vary depending upon operating system and hardware.
- The python global interpreter lock will now be released when entering OMEGA toolkit calls.

# 6.29.2 Minor bug fixes

- Now operator() will fail nicely and return false for non-3D input if SetFromCT is set to false.
- All ring bonds will be left unset by OEFlipper unless forceFlip=true.

# 6.30 Omega TK 2.5.1

## 6.30.1 New features

- An option has been added to allow hydrogen atoms in -OH, -SH, and amines to take part in conformational sampling. New methods have been added for accessing this option: GetSampleHydrogens and SetSampleHydrogens. By default, hydrogen atoms are not sampled.
- A warts option has been added to *OEFlipper*. Enabling this option will number the output molecules with an  $@$ symbol.
- The parameterless version of  $OEOmega$ , AddFraqLib will now load the built-in fraglib immediately. By default, the built-in fraglib does not load until operator() is called for the first time.

# 6.30.2 Major bug fixes

- Now using SetFixSmarts without SetFixMol will rematch for every input structure. Previously, this would only match the first input structure and reuse that match for the rest of the calculation. Using both SetFixSmarts and SetFixMol will continue to match against the fixmol and use that match for the entire calculation.
- Partial ring matching with SetFixSmarts or SetFixMol could cause a crash. Now only full ring systems may be specified and any attempt at matching a partial ring system will fail gracefully.
- The default value for max matches with SetFixSmarts or SetFixMol has been changed from 10 to 1. This value can be adjusted with SetFixMaxMatch.
- A bug has been fixed where multiple threads using OEOmega could cause a license failure.
- Planar molecules could have problems sprouting hydrogens when disabling SetFromCT because OMEGA was treating them as 2D. Now OMEGA will assume that planar molecules are properly defined 3D coordinates in this situation.
- Stereochemistry at the attachment points of rings with four or less atoms could be lost. Now stereochemistry is saved for rings of all sizes.
- A bug has been fixed where exceptionally long torsion rules could get cutoff early.

## 6.30.3 Minor bug fixes

- Only 3D coordinates were being cleared in FLIPPER. Now 2D coordinates are cleared as well.
- Fragment generation during an OMEGA calculation with SetStrictFrags enabled could yield slightly different fragments than the MakeFraglib app. This has been corrected for consistency.

# **6.30.4 Documentation fixes**

 $\bullet$  The *Omega TK* documentation was showing the incorrect version number.

# 6.31 Omega TK 2.5.0

## 6.31.1 New features

• The *Omega TK* library is now thread safe. Note, different  $OEOmega$  objects are still required per thread.

# 6.31.2 Major bug fixes

• *OEOmega* class would cause a crash on destruction whenever a copy was made. This has been fixed by specifying a proper copy constructor.

# 6.31.3 Minor bug fixes

- Tags for rotor compression are no longer attached to the output molecules when rotoroffsetcompress is false. It was discovered that these tags confuse VIDA when they are attached but not used.
- The torsion library has been updated with better angles for a biphenyl torsion. The entry for 90 degrees has been removed and +/-30 degrees has been added.

# 6.32 Omega TK 2.4.6

## 6.32.1 Minor bug fixes

• The treatment of single-atom systems has been changed to explicitly set the dimension to 3D so that they are not labeled 2D when writing to SDF format.

# 6.33 Omega TK 2.4.5

## 6.33.1 New features

• Now uses an extension of the MMFF94 force field for tricoordinate boron compounds. Most compounds containing B-X bonds where X=C,N,O,S, and H are covered with the following exceptions: X=N(imine),N(sulfonamide), N(pyridinium) and N(quaternary). Also not supported are compounds in which boron is bonded to X=F,Cl,Br,I,B and Si, or makes a bond angle BYX. Compounds in which boron is a part of four-membered rings of B1CCC1 type are also not available in the current parameterization because their existence is questionable: Ab initio calculations at the MP2/6-31G<sup>\*\*</sup> level failed to identify stable structures for them (highly polar structures in which boron is four-coordinated are formed).

# 6.34 Omega TK 2.4.4

## 6.34.1 Bug fixes

- Fixed a bug where OMEGA wasn't checking if 3D construction of fragment generation was successful.
- Fixed a bug where output from flipper could still fail in OMEGA for missing stereo chemistry. Now the rules for required stereo chemistry are consistent.
- Fixed a bug where setting stereo chemistry in too small of a ring could cause a crash. Now only rings greater than 7 members and only one double bond will be set with flipper.

# 6.35 Omega TK 2.4.1

## 6.35.1 New features

- OMEGA and MakeFraglib may now be run with MPI using the *oempirun* script. (May not available on all platforms)
- The default for OMEGA has been changed to require all stereocenters to be specified. Molecules with any unspecified stereo will fail. The previous behavior was for OMEGA to choose a random stereoisomer. This default can be changed back to the previous behavior by setting -strictstereo to false.
- The default for OMEGA has been changed to no longer use 'close enough' atom typing. If a proper MMFF atom type cannot be found for an atom then the molecule will fail. Previous versions would use a different atom type of the same element if it was available. The previous behavior for atom type substitution can be enabled by setting *-strictatomtyping* to false.
- OMEGA now has the option to require on-the-fly generation of fragments to be the same as the MakeFraglib utility by setting -strictfrags to  $true$ . This fragment generation is more rigorous but also more time consuming.
- The convenience flag -strict has been added to turn on or off all of the strict options. These include -strictstereo, -strictatomtyping and -strictfrags.
- On-screen progress has been enabled for OMEGA and MakeFraglib using the *-progress* flag. The options are none, dots, log, and percent.
- The *-maxconfgen* and *-maxpoolsize* flags have been removed. These options are set internally and adjusted automatically subject to the user defined variable of -maxconfs. Additionally, hard limits have been removed from these variables and they are now only limited by available memory.
- The flag *-fixsmarts* has been created to allow a smarts pattern to be used to fix a portion of the molecule. This requires 3D coordinates to be available from either a 3D input file with *-fromCT* set to false or from a molecule set using -*fixfile*.

## 6.35.2 Bug fixes

- Crashes have been fixed that could occur when the *-fixfile* could not find a valid match or did not have enough atoms to match against in a ring system.
- Program no longer crashes if there is not enough memory for duplicate removal. If there is not enough memory available for allocation then the application will exit immediately.

# 6.36 Omega TK 2.4.0

### 6.36.1 New features

- The MaxConfGen and MaxPoolSize variables are now set internally and adjusted automatically subject to the user defined variable of MaxConfs. Additionally, hard limits have been removed from these variables and they are now only limited by available memory. The following methods are deprecated: SetMaxConfGen, GetMaxConfGen, SetMaxPoolSize, GetMaxPoolSize.
- The method SetMaxConfs has been changed from *void* to *bool*. The method will return  $\tau$  rue if the parameter has been set properly and will return false if the number is too high and would cause the memory required for duplicate removal to exceed the maximum theoretical memory for the platform.
- The method SetFixSmarts has been created to allow a smarts pattern to be used to fix a portion of the molecule. This requires 3D coordinates to be available from either a 3D input file with SetFromCT set to false or from a molecule set using SetFixMol.
- Fragment generation for OEOmega is now the same as the MakeFraglib application. Previous versions used a faster but more approximate version of fragment generation.
- The OEOmega default has been changed to no longer use "close enough" atom typing. If a proper MMFF atom type cannot be found for an atom then the molecule will fail. Previous versions would use a different atom type of the same element if it was available. The previous behavior of atom type substitution can be enabled by calling SetStrictAtomTypes with the argument false.
- The error level for most messages coming from the Omega library has been lowered to Verbose. The library can be run in a much quieter manner if the error level is set to  $Info$  by the user.

## 6.36.2 Bug fixes

- Crashes have been fixed that could occur when the FixFile could not find a valid match or did not have enough atoms to match against in a ring system.
- Program no longer crash if there is not enough memory for duplicate removal. If there is not enough memory available for allocation then duplicate removal will be skipped for the molecule and operator() will return true.

# 6.37 Omega TK 2.3.3

# 6.37.1 New features

- New API points have been added: OETorLib.ResetTorsionLibrary, OETorLib. ClearTorsionLibrary, and OETorLib.AddTorsionRule. The torsion rules may be created by passing in a OEQMolBase and vector<int> of angles, or by passing in a string with the standard rule format.
- The corresponding atom symbols, bond symbols, and torsion angles are now printed on a line under the matching smarts pattern.

# 6.37.2 Bug fixes

- Rotor offset compression is now set to false by default. Coordinate changes made in the toolkits after an Omega calculation are lost if rotor offset compression is set to true. If molecules are sent to OEWriteMolecule directly after an Omega run then rotor offset compression may safely be set to true, which will significantly reduce the filesize of the output.
- The energy window set by SetEnergyRange and SetRangeIncrement is now used consistently. Previous versions of Omega did not use this value properly for all aspects of an Omega calculation.

# 6.38 Omega TK 2.3.2

## 6.38.1 Bug fixes

• Fixed a bug where molecules containing boron or selenium could cause a crash. These molecules now are written to the '.fail' file due to missing force field parameters and the program will proceed to the next molecule.

# 6.39 Omega TK 2.3.1

### 6.39.1 New features

• The OMEGA application now includes a utility named oeb2sdconf that allows OMEGA generated conformers to be used with the MOE program. Please contact Chemical Computing Group support if you require assistance with this utility.

# 6.39.2 Bug fixes

- Fixed a bug where the omega2 PVM features would not work on some platforms.
- Fixed a bug where the omega2 script would not function properly with filenames that had spaces in them.

# 6.40 Omega TK 2.3.0

## 6.40.1 New features

- The distribution and installation of OMEGA has been modified. The Windows distribution is now a standard exe installer, and the OS X distribution is a dmg containing a standard pkg installer. The executables are now scripts that chose the correct version of the program at runtime. Please see the Installation and Platform Notes for details.
- The defaults for MaxConfs and RMSThreshold are changed in this version. The default for MaxConfs is reduced from 400 to 200, while the value for RMSThreshold goes from 0.8 down to 0.5. These changes are based on maintaining good reproduction of the crystal structure test set, virtual screening tests with ROCS and FRED, and pose prediction tests with FRED.
- The method OEConfGen:: OEOmega:: ClearFixFile is added to the OMEGA library. This allows an OEConfGen: : OEOmega instance to be reused for an unrestrained search after it has previously been used for a fixed search.
- Untitled molecules are given unique titles of omega 1, omega 2, and so on. Titles allow molecules to be located in the log files.

# 6.40.2 Bug fixes

- Fixed a major bug where molecules that have missing torsion rules caused OMEGA to crash. Molecules with missing torsion rules are now sent to the *omega2.fail* file and are not processed. Missing torsion rules are typically caused by highly unusual molecules for which OEChem cannot properly assign valence to all atoms.
- Fixed a bug in duplicate conformer removal that caused some conformers that should have been removed to pass through as unique. This bug also caused occurrences where a reduction in maxconfs led to an increase in the number of conformers returned.
- Fixed a bug that caused SD data on single conformer molecules to be removed.
- Fixed a bug in the *flipper* library that left 3D coordinates intact, which caused stereo chemistry to be ambiguous. The *flipper* library now replaces 3D coordinates with zeros.
- Fixed a bug where the SyM tag from previous OMEGA calculations caused problems when those molecules where passed back in. Also, the O2Mo1Id tag is now removed from molecules before they are sent to the output.
- When the number of stereo centers exceeds the number of -maxcenters M, *flipper* now generates  $2^M$  random non-repeating flips. Previous versions generated  $2^M$  random flips, leading to molecules with the same stereochemistry being returned multiple times.

# 6.41 Omega TK 2.2.2

# 6.41.1 Bug fixes

- Fixed a major bug that would cause highly-symmetric, highly-fluorinated compounds to crash the program or hang a slave in PVM mode.
- Fixed a bug in atom typing when building fragments from scratch that, in some rare cases, could result in differing fragment geometries depending on the order of input of the molecules.

- Added more places that check for time exceeding max time. This is more just to prevent overly large molecules from appearing to hang.
- If OMEGA is called with a fixed predicate, this now implies that FromCT is false. In other words, if you want to use a predicate to fix atoms, you need to use a 3D structure as input.

# 6.42 Omega TK 2.2.1

# 6.42.1 Bug fixes

• The new build algorithm introduced in v2.2.0 could, on rare occasions, generate a structure with heavy atom clashes. This release is mainly a bug fix for this problem.

# **SEVEN**

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

# **EIGHT**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

# **NINE**

# **CITATION**

# 9.1 Orion<sup>®</sup> Floes

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

# **9.2 Toolkits and Applications**

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

# 9.3 OpenEye Web Services

To cite use of the Macromolecular Data Service (MMDS) web service, please use the syntax:

Macromolecular Data Service <version-number>. OpenEye, Cadence Molecular Sciences, -Santa Fe, NM. http://www.eyesopen.com.

### For example:

Macromolecular Data Service 1.1. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. →http://www.eyesopen.com.

The MMDS version number appears on the web service's release notes.

To cite use of the FastROCS  $^{TM}$  server, please use the syntax:

FastROCS <version-number>. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http:// →www.eyesopen.com.

### For example:

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

**TEN** 

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project                  | Website                                                                                | License                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| abseil-cpp                       | https://github.com/abseil/abseil-cpp                                                   | https://                                                                 |
| absl-py                          | https://github.com/abseil/abseil-py                                                    | https://                                                                 |
| aiohttp                          | https://docs.aiohttp.org/en/stable/                                                    | https://                                                                 |
| aiosignal                        | https://github.com/aio-libs/aiosignal                                                  | https://                                                                 |
| Amazon Linux 2                   | https://aws.amazon.com/amazon-linux-2                                                  | N/A                                                                      |
| AmberUtils                       | http://ambermd.org                                                                     | N/A                                                                      |
| ambit                            | https://github.com/khimaros/ambit                                                      | https://                                                                 |
| amqp                             | https://github.com/celery/py-amqp                                                      | https://                                                                 |
| anaconda-anon-usage              | Orion Floes                                                                            | https://                                                                 |
| angular                          | https://github.com/angular/angular.js                                                  | https://                                                                 |
| angular-animate                  | https://github.com/angular/angular.js                                                  | https://                                                                 |
| angular-cache                    | https://github.com/jmdobry/angular-cache                                               | https://                                                                 |
| angular-cookies                  | https://github.com/angular/angular.js                                                  | https://                                                                 |
| angular-loggly-logger            | https://github.com/ajbrown/angular-loggly-logger                                       | https://                                                                 |
| angular-mocks                    | https://github.com/angular/angular.js                                                  | https://                                                                 |
| angular-resource                 | https://github.com/angular/angular.js                                                  | https://                                                                 |
| angular-toggle-switch            | https://github.com/cgarvis/angular-toggle-switch                                       | https://                                                                 |
| angular-ui-grid                  | https://github.com/angular-ui/ui-grid                                                  | https://                                                                 |
| angular-ui-router                | https://github.com/angular-ui/ui-router                                                | https://                                                                 |
| angular-ui-tree                  | https://github.com/angular-ui-tree/angular-ui-tree                                     | https://                                                                 |
| angular-vs-repeat                | https://github.com/kamilkp/angular-vs-repeat                                           | https://                                                                 |
| aniso8601                        | https://bitbucket.org/nielsenb/aniso8601                                               | https://                                                                 |
| annotated-types                  | https://github.com/annotated-types/annotated-types                                     | https://                                                                 |
| anyio                            | https://github.com/agronholm/anyio                                                     | https://                                                                 |
| appdirs                          | http://github.com/ActiveState/appdirs                                                  | http://                                                                  |
| appengine                        | https://google.golang.org/appengine                                                    | https://                                                                 |
| arabic-reshaper                  | https://github.com/mpcabd/python-arabic-reshaper/                                      | https://                                                                 |
| archspec                         | https://github.com/archspec/archspec/blob/master/README.md                             | https://                                                                 |
| Name of Project                  | Website                                                                                | License                                                                  |
| argon2-cffi                      | https://github.com/hynek/argon2-cffi                                                   | https:/                                                                  |
| argon2-cffi-bindings             | https://github.com/hynek/argon2-cffi-bindings                                          | https:/                                                                  |
| arpack                           | https://www.caam.rice.edu/software/ARPACK/                                             | https:/                                                                  |
| ascii85                          | https://github.com/huandu/node-ascii85                                                 | https:/                                                                  |
| ase                              | https://wiki.fysik.dtu.dk/ase/                                                         | https:/                                                                  |
| asgiref                          | https://github.com/django/asgiref/                                                     | https:/                                                                  |
| asn1crypto                       | https://github.com/wbond/asn1crypto                                                    | https:/                                                                  |
| assertions go-render             | https://github.com/smartystreets/assertions/internal/go-render/render                  | https:/                                                                  |
| assertions oglmatchers           | https://github.com/smartystreets/assertions/internal/oglematchers                      | https:/                                                                  |
| assertions                       | https://github.com/smartystreets/assertions                                            | https:/                                                                  |
| asttokens                        | https://github.com/gristlabs/asttokens                                                 | https:/                                                                  |
| astunparse                       | https://github.com/simonpercivall/astunparse                                           | https:/                                                                  |
| async-lru                        | https://github.com/aio-libs/async-lru                                                  | https:/                                                                  |
| async-timeout                    | https://github.com/aio-libs/async-timeout                                              | https:/                                                                  |
| atk-1.0                          | https://docs.gtk.org/atk/                                                              | https:/                                                                  |
| atomic                           | https://github.com/uber-go/atomic                                                      | https:/                                                                  |
| atomicwrites                     | https://github.com/untitaker/python-atomicwrites                                       | https:/                                                                  |
| attrs                            | https://www.attrs.org/                                                                 | https:/                                                                  |
| aws-sdk-go                       | https://github.com/aws/aws-sdk-go                                                      | https:/                                                                  |
| Babel                            | https://github.com/python-babel/babel                                                  | https:/                                                                  |
| backcall                         | https://github.com/takluyver/backcall                                                  | https:/                                                                  |
| backports                        | https://github.com/brandon-rhodes/backports                                            | https:/                                                                  |
| backports.functools-lru-cache    | https://github.com/jaraco/backports.functools_lru_cache                                | https:/                                                                  |
| base62                           | https://github.com/kare/base62                                                         | https:/                                                                  |
| beautifulsoup4                   | https://www.crummy.com/software/BeautifulSoup/                                         | https:/                                                                  |
| billiard                         | https://github.com/celery/billiard                                                     | https:/                                                                  |
| biopython                        | https://biopython.org                                                                  | https:/                                                                  |
| biotite                          | https://github.com/biotite-dev/biotite/blob/master/README.rst                          | https:/                                                                  |
| bitset                           | https://github.com/willf/bitset                                                        | https:/                                                                  |
| blas                             | https://www.netlib.org/blas/                                                           | https:/                                                                  |
| bleach                           | https://github.com/mozilla/bleach                                                      | https:/                                                                  |
| blessings                        | https://github.com/erikrose/blessings                                                  | https:/                                                                  |
| blinker                          | https://pythonhosted.org/blinker/                                                      | https:/                                                                  |
| blosc                            | https://github.com/Blosc/python-blosc                                                  | https:/                                                                  |
| blosc2                           | https://github.com/Blosc/python-blosc2                                                 | https:/                                                                  |
| boltons                          | https://github.com/mahmoud/boltons                                                     | https:/                                                                  |
| boost                            | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html                  | https:/                                                                  |
| boost-cpp                        | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html                  | https:/                                                                  |
| bootstrap-vue                    | https://github.com/bootstrap-vue/bootstrap-vue                                         | https:/                                                                  |
| boto3                            | https://github.com/boto/boto3                                                          | https:/                                                                  |
| botocore                         | https://github.com/boto/botocore                                                       | https:/                                                                  |
| Bottleneck                       | https://bottleneck.readthedocs.io/en/latest/index.html                                 | https:/                                                                  |
| Brotli                           | https://github.com/google/brotli                                                       | https:/                                                                  |
| brotli-bin                       | https://github.com/google/brotli                                                       | https:/                                                                  |
| brotli-python                    | http://python-hyper.org/projects/brotlipy/en/latest/                                   | https:/                                                                  |
| brotlipy                         | https://github.com/python-hyper/brotlipy                                               | https:/                                                                  |
| bson                             | http://github.com/py-bson/bson                                                         | https:/                                                                  |
| bytefmt                          | https://code.cloudfoundry.org/bytefmt                                                  | https:/                                                                  |
| bzip2                            | https://www.bzip.org                                                                   | https:/                                                                  |
| Name of Project                  | Website                                                                                | License                                                                  |
| c-ares                           | https://github.com/c-ares/c-ares                                                       | https:/                                                                  |
| ca-certificates                  | https://github.com/conda-forge/ca-certificates-feedstock                               | https:/                                                                  |
| cached-property                  | https://github.com/pydanny/cached-property                                             | https:/                                                                  |
| cachetools                       | https://github.com/tkem/cachetools/                                                    | https:/                                                                  |
| cairo                            | https://pycairo.readthedocs.io/en/latest/                                              | https:/                                                                  |
| canvas                           | https://github.com/Automattic/node-canvas                                              | https:/                                                                  |
| cctbx                            | https://github.com/cctbx/cctbx_project                                                 | https:/                                                                  |
| celery                           | https://github.com/celery/celery                                                       | https:/                                                                  |
| Cerberus                         | https://docs.python-cerberus.org/en/stable/                                            | https:/                                                                  |
| certifi                          | https://certifi.readthedocs.io/en/latest/                                              | https:/                                                                  |
| cffi                             | https://github.com/python-cffi/cffi                                                    | https:/                                                                  |
| cftime                           | https://pypi.org/project/cftime/                                                       | https:/                                                                  |
| chardet                          | https://github.com/chardet/chardet                                                     | https:/                                                                  |
| charset-normalizer               | https://github.com/ousret/charset_normalizer                                           | https:/                                                                  |
| chunkreader                      | https://github.com/jackc/chunkreader/v2                                                | https:/                                                                  |
| click                            | https://palletsprojects.com/p/click/                                                   | https:/                                                                  |
| click-completion                 | https://github.com/click-contrib/click-completion                                      | https:/                                                                  |
| click-didyoumean                 | https://github.com/click-contrib/click-didyoumean                                      | https:/                                                                  |
| click-plugins                    | https://github.com/click-contrib/click-plugins                                         | https:/                                                                  |
| click-repl                       | https://github.com/untitaker/click-repl                                                | https:/                                                                  |
| cloudpickle                      | https://github.com/cloudpipe/cloudpickle                                               | https:/                                                                  |
| cmake                            | https://cmake.org/                                                                     | https:/                                                                  |
| colorama                         | https://github.com/tartley/colorama                                                    | https:/                                                                  |
| comm                             | https://github.com/ipython/comm                                                        | https:/                                                                  |
| compose                          | https://github.com/docker/compose                                                      | https:/                                                                  |
| conda-content-trust              | https://github.com/conda/conda-content-trust                                           | https:/                                                                  |
| conda-libmamba-solver            | https://github.com/conda/conda-libmamba-solver                                         | https:/                                                                  |
| conda-package-handling           | https://github.com/conda/conda-package-handling                                        | https:/                                                                  |
| conda-package-streaming          | https://anaconda.org/conda-forge/conda-package-streaming                               | https:/                                                                  |
| conda-token                      | https://anaconda.org/anaconda/conda-token                                              | https:/                                                                  |
| confuse                          | https://github.com/beetbox/confuse                                                     | https:/                                                                  |
| contourpy                        | https://github.com/contourpy/contourpy                                                 | https:/                                                                  |
| cpp-peglib                       | https://github.com/yhirose/cpp-peglib                                                  | https:/                                                                  |
| cryptography                     | https://github.com/pyca/cryptography                                                   | https:/                                                                  |
| cssselect2                       | https://github.com/Kozea/cssselect2/                                                   | https:/                                                                  |
| cudatoolkit                      | https://developer.nvidia.com/cuda-toolkit                                              | https:/                                                                  |
| cupy-cuda113                     | https://cupy.dev/                                                                      | https:/                                                                  |
| curl                             | https://curl.se                                                                        | https:/                                                                  |
| cycler                           | https://github.com/matplotlib/cycler                                                   | https:/                                                                  |
| cyrus-sasl                       | https://github.com/cyrusimap/cyrus-sasl                                                | https:/                                                                  |
| Cython                           | https://cython.org                                                                     | https:/                                                                  |
| $\overline{d3}$                  | https://github.com/mbostock/d3                                                         | https:/                                                                  |
| dataclasses                      | https://github.com/ericvsmith/dataclasses                                              | https:/                                                                  |
| ddsketch                         | http://github.com/datadog/sketches-py                                                  | https:/                                                                  |
| debugpy                          | https://aka.ms/debugpy                                                                 | https:/                                                                  |
| decimal                          | https://github.com/shopspring/decimal                                                  | https:/                                                                  |
| decorator                        | https://github.com/micheles/decorator                                                  | https:/                                                                  |
| deepdiff                         | https://github.com/seperman/deepdiff                                                   | https:/                                                                  |
| deeptime                         | https://github.com/deeptime-ml/deeptime                                                | https:/                                                                  |
| Name of Project                  | Website                                                                                | License                                                                  |
| defusedxml                       | https://github.com/tiran/defusedxml                                                    | https:/                                                                  |
| dill                             | https://github.com/uqfoundation/dill                                                   | https:/                                                                  |
| distro                           | Orion Floes                                                                            | https:/                                                                  |
| Django                           | https://www.djangoproject.com/                                                         | https:/                                                                  |
| django-classy-tags               | https://github.com/django-cms/django-classy-tags                                       | https:/                                                                  |
| django-cors-headers              | https://github.com/adamchainz/django-cors-headers                                      | https:/                                                                  |
| django-csp                       | https://github.com/mozilla/django-csp                                                  | https:/                                                                  |
| django-extensions                | https://github.com/django-extensions/django-extensions                                 | https:/                                                                  |
| django-filter                    | https://github.com/carltongibson/django-filter/tree/master                             | https:/                                                                  |
| django-redis                     | https://github.com/jazzband/django-redis                                               | https:/                                                                  |
| django-taggit                    | https://github.com/jazzband/django-taggit                                              | https:/                                                                  |
| django-taggit-serializer         | https://github.com/glemmaPaul/django-taggit-serializer                                 | https:/                                                                  |
| django-taggit-templatetags2      | https://github.com/fizista/django-taggit-templatetags2                                 | https:/                                                                  |
| djangorestframework              | https://www.django-rest-framework.org/                                                 | https:/                                                                  |
| dkh                              | https://psicode.org/psi4manual/master/dkh.html                                         | https:/                                                                  |
| dm-tree                          | https://github.com/deepmind/tree                                                       | https:/                                                                  |
| docker-py                        | https://github.com/docker/docker-py/                                                   | https:/                                                                  |
| docopt                           | https://docopt.org                                                                     | https:/                                                                  |
| docutils                         | https://docutils.sourceforge.io                                                        | https:/                                                                  |
| drf-dynamic-fields               | https://github.com/dbrgn/drf-dynamic-fields                                            | https:/                                                                  |
| editdistance                     | https://github.com/roy-ht/editdistance                                                 | https:/                                                                  |
| eigen                            | https://eigen.tuxfamily.org/index.php?title=Main_Page                                  | https:/                                                                  |
| einops                           | https://github.com/arogozhnikov/einops                                                 | https:/                                                                  |
| entrypoints                      | https://github.com/takluyver/entrypoints                                               | https:/                                                                  |
| errors                           | https://github.com/pkg/errors                                                          | https:/                                                                  |
| eslint-plugin                    | https://github.com/typescript-eslint/typescript-eslint                                 | https:/                                                                  |
| et_xmlfile                       | https://foss.heptapod.net/openpyxl/et_xmlfile                                          | https:/                                                                  |
| exceptiongroup                   | https://github.com/agronholm/exceptiongroup                                            | https:/                                                                  |
| executing                        | https://github.com/alexmojaki/executing                                                | https:/                                                                  |
| expat                            | https://libexpat.github.io                                                             | https:/                                                                  |
| fastjsonschema                   | https://github.com/horejsek/python-fastjsonschema                                      | https:/                                                                  |
| fastrlock                        | https://github.com/scoder/fastrlock                                                    | https:/                                                                  |
| fftw                             | https://www.fftw.org                                                                   | comm                                                                     |
| filebuffer                       | https://github.com/mattetti/filebuffer                                                 | https:/                                                                  |
| filelock                         | https://py-filelock.readthedocs.io/en/latest/index.html                                | https:/                                                                  |
| finufft                          | https://github.com/flatironinstitute/finufft                                           | https:/                                                                  |
| Flask                            | https://flask.palletsprojects.com/en/2.1.x/                                            | https:/                                                                  |
| flatbuffers                      | https://google.github.io/flatbuffers/                                                  | https:/                                                                  |
| flit-core                        | https://github.com/pypa/flit                                                           | https:/                                                                  |
| FLTK                             | https://www.fltk.org/index.php                                                         | https:/                                                                  |
| fmt                              | https://fmt.dev/latest/index.html                                                      | https:/                                                                  |
| font-awesome                     | https://github.com/FortAwesome/Font-Awesome                                            | https:/                                                                  |
| font-ttf-dejavu-sans-mono        | https://dejavu-fonts.github.io                                                         | https:/                                                                  |
| font-ttf-inconsolata             | https://fonts.google.com/specimen/Inconsolata                                          | https:/                                                                  |
| font-ttf-source-code-pro         | https://fonts.google.com/specimen/Source+Code+Pro                                      | https:/                                                                  |
| font-ttf-ubuntu                  | https://fonts.google.com/specimen/Ubuntu                                               | https:/                                                                  |
| fontconfig                       | https://www.freedesktop.org/wiki/Software/fontconfig/                                  | https:/                                                                  |
| fonts-conda-ecosystem            | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                                | https:/                                                                  |
| fonts-conda-forge                | https://anaconda.org/conda-forge/fonts-conda-forge/                                    | https:/                                                                  |
|                                  |                                                                                        | J)                                                                       |
| Name of Project                  | Website                                                                                | Licen                                                                    |
| fonttools                        | https://github.com/fonttools/fonttools                                                 | https:/                                                                  |
| freetype                         | https://freetype.org                                                                   | https:/                                                                  |
| fribidi                          | https://github.com/fribidi/fribidi                                                     | https:/                                                                  |
| frozendict                       | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| frozenlist                       | https://github.com/aio-libs/frozenlist                                                 | https:/                                                                  |
| fsmlite                          | https://github.com/tkem/fsmlite                                                        | https:/                                                                  |
| fsspec                           | https://github.com/fsspec/filesystem_spec                                              | https:/                                                                  |
| funcy                            | https://github.com/Suor/funcy                                                          | https:/                                                                  |
| gast                             | https://github.com/serge-sans-paille/gast/                                             | https:/                                                                  |
| gau2grid                         | https://github.com/dgasmith/gau2grid                                                   | https:/                                                                  |
| gax-go                           | https://github.com/googleapis/gax-go/v2                                                | https:/                                                                  |
| gdk-pixbuf                       | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                              | https:/                                                                  |
| gemmi                            | https://gemmi.readthedocs.io/en/latest/                                                | https:/                                                                  |
| genproto                         | https://google.golang.org/genproto/googleapis                                          | https:/                                                                  |
| geometric                        | https://openbase.com/python/geometric                                                  | https:/                                                                  |
| giflib                           | https://giflib.sourceforge.net                                                         | https:/                                                                  |
| glib                             | https://docs.gtk.org/glib/                                                             | https:/                                                                  |
| <b>GLM</b> Library               | https://github.com/g-truc/glm                                                          | https:/                                                                  |
| gls                              | https://github.com/jtolds/gls                                                          | https:/                                                                  |
| go-cleanhttp                     | https://github.com/hashicorp/go-cleanhttp                                              | https:/                                                                  |
| go-connections                   | https://github.com/docker/go-connections                                               | https:/                                                                  |
| go-cpio                          | https://github.com/cavaliercoder/go-cpio                                               | https:/                                                                  |
| go-getter                        | https://github.com/hashicorp/go-getter                                                 | https:/                                                                  |
| go-homedir                       | https://github.com/mitchellh/go-homedir                                                | https:/                                                                  |
| go-ini                           | https://github.com/go-ini/ini                                                          | https:/                                                                  |
| go-jmespath                      | https://github.com/jmespath/go-jmespath                                                | https:/                                                                  |
| go-junit-report                  | https://github.com/jstemmer/go-junit-report                                            | https:/                                                                  |
| go-netrc                         | https://github.com/bgentry/go-netrc/netrc                                              | https:/                                                                  |
| go-ole                           | https://github.com/go-ole/go-ole                                                       | https:/                                                                  |
| go-pg                            | https://github.com/go-pg/pg                                                            | https:/                                                                  |
| go-redis                         | https://github.com/go-redis/redis/v8                                                   | https:/                                                                  |
| go-rendezvous                    | https://github.com/dgryski/go-rendezvous                                               | https:/                                                                  |
| go-safetemp                      | https://github.com/hashicorp/go-safetemp                                               | https:/                                                                  |
| go-sysconf                       | https://github.com/tklauser/go-sysconf                                                 | https:/                                                                  |
| go-testing-interface             | https://github.com/mitchellh/go-testing-interface                                      | https:/                                                                  |
| go-units                         | https://github.com/docker/go-units                                                     | https:/                                                                  |
| go-version                       | https://github.com/hashicorp/go-version                                                | https:/                                                                  |
| go-zglob                         | https://github.com/mattn/go-zglob                                                      | https:/                                                                  |
| go.opencensus                    | https://go.opencensus.io                                                               | https:/                                                                  |
| gobrake. $\sqrt{2}$              | https://gopkg.in/airbrake/gobrake.v2                                                   | https:/                                                                  |
| goconvey                         | https://github.com/smartystreets/goconvey                                              | https:/                                                                  |
| golden-layout                    | https://github.com/deepstreamIO/golden-layout                                          | https:/                                                                  |
| google-auth                      | https://google-auth.readthedocs.io/en/master/                                          |                                                                          |
| google-auth-oauthlib             | https://github.com/googleapis/google-auth-library-python-oauthlib                      | https:/<br>https:/                                                       |
| google-cloud-go                  | https://cloud.google.com/go                                                            |                                                                          |
|                                  | https://cloud.google.com/go/storage                                                    | https:/                                                                  |
| google-cloud-go/storage          |                                                                                        | https:/                                                                  |
| google-pasta                     | https://github.com/google/pasta                                                        | https:/                                                                  |
| google.golang.org/api            | https://google.golang.org/api                                                          | https:/                                                                  |
| gopsutil                         | https://github.com/shirou/gopsutil                                                     | https:/                                                                  |
| Name of Project                  | Website                                                                                | License                                                                  |
| gorilla websocket                | https://github.com/gorilla/websocket                                                   | https://github.com/gorilla/websocket/blob/master/LICENSE                 |
| graphite2                        | https://github.com/silnrsi/graphite                                                    | https://github.com/silnrsi/graphite/blob/master/LICENSE                  |
| graphviz                         | https://graphviz.org/                                                                  | https://www.graphviz.org/license/                                        |
| greenlet                         | https://greenlet.readthedocs.io/en/latest/                                             | https://github.com/python-greenlet/greenlet/blob/master/LICENSE          |
| groupcache                       | https://github.com/golang/groupcache                                                   | https://github.com/golang/groupcache/blob/master/LICENSE                 |
| grpc                             | https://google.golang.org/grpc                                                         | https://github.com/grpc/grpc-go/blob/master/LICENSE                      |
| grpc-cpp                         | https://github.com/grpc/grpc                                                           | https://github.com/grpc/grpc/blob/master/LICENSE                         |
| grpcio                           | https://github.com/grpc/grpc.io/blob/main/LICENSE                                      | https://github.com/grpc/grpc.io/blob/main/LICENSE                        |
| gtk2                             | https://gitlab.gnome.org/GNOME/gtk                                                     | https://gitlab.gnome.org/GNOME/gtk/-/blob/master/COPYING                 |
| gts                              | https://sourceforge.net/projects/gts/                                                  | https://sourceforge.net/p/gts/code/ci/master/tree/COPYING                |
| h5py                             | https://www.h5py.org                                                                   | https://github.com/h5py/h5py/blob/master/LICENSE                         |
| harfbuzz                         | https://github.com/harfbuzz/harfbuzz                                                   | https://github.com/harfbuzz/harfbuzz/blob/main/COPYING                   |
| hdbscan                          | https://hdbscan.readthedocs.io/en/latest/                                              | https://github.com/scikit-learn-contrib/hdbscan/blob/master/LICENSE      |
| hdf4                             | https://www.hdfgroup.org/solutions/hdf4/                                               | https://support.hdfgroup.org/ftp/HDF4/current/src/hdf-4.2.15/LICENSE.txt |
| hdf5                             | https://www.hdfgroup.org/solutions/hdf5/                                               | https://raw.githubusercontent.com/HDFGroup/hdf5/develop/COPYING          |
| he                               | https://github.com/mathiasbynens/he                                                    | https://github.com/mathiasbynens/he/blob/main/LICENSE-MIT.txt            |
| html-loader                      | https://github.com/webpack-contrib/html-loader                                         | https://github.com/webpack-contrib/html-loader/blob/master/LICENSE       |
| html5lib                         | https://github.com/html5lib/html5lib-python                                            | https://github.com/html5lib/html5lib-python/blob/master/LICENSE          |
| htslib                           | https://www.htslib.org                                                                 | https://github.com/samtools/htslib/blob/develop/LICENSE                  |
| humanize                         | https://github.com/jmoiron/humanize                                                    | https://github.com/jmoiron/humanize/blob/master/LICENSE                  |
| icu                              | https://github.com/unicode-org/icu                                                     | https://github.com/unicode-org/icu/blob/main/icu4c/LICENSE               |
| idna                             | https://github.com/kjd/idna                                                            | https://github.com/kjd/idna/blob/master/LICENSE.rst                      |
| imageio                          | https://github.com/imageio/imageio                                                     | https://github.com/imageio/imageio/blob/master/LICENSE                   |
| imagesize                        | https://github.com/shibukawa/imagesize_py                                              | https://github.com/shibukawa/imagesize_py/blob/master/LICENSE            |
| ImmuneBuilder                    | https://github.com/oxpig/ImmuneBuilder/tree/main                                       | https://github.com/oxpig/ImmuneBuilder/blob/main/LICENSE                 |
| importlib-metadata               | https://github.com/python/importlib_metadata                                           | https://github.com/python/importlib_metadata/blob/main/LICENSE           |
| importlib_resources              | https://github.com/python/importlib_resources                                          | https://github.com/python/importlib_resources/blob/main/LICENSE          |
| InChI                            | https://iupac.org/who-we-are/divisions/division-details/inchi/                         | https://github.com/IUPAC-InChI/InChI/blob/master/LICENSE                 |
| inflection                       | https://github.com/jinzhu/inflection                                                   | https://github.com/jinzhu/inflection/blob/master/LICENSE                 |
| ini.v1                           | https://gopkg.in/ini.v1                                                                | https://github.com/go-ini/ini/blob/master/LICENSE                        |
| iniconfig                        | https://github.com/pytest-dev/iniconfig                                                | https://github.com/pytest-dev/iniconfig/blob/main/LICENSE                |
| innersvg-polyfill                | https://github.com/dnozay/innersvg-polyfill                                            | https://github.com/dnozay/innersvg-polyfill/blob/master/LICENSE          |
| intel-openmp                     | https://github.com/hermitcore/libomp_oss                                               | https://github.com/llvm/llvm-project/blob/main/openmp/LICENSE.txt        |
| ipykernel                        | https://ipython.org                                                                    | https://github.com/ipython/ipykernel/blob/master/LICENSE                 |
| ipython                          | https://ipython.org                                                                    | https://github.com/ipython/ipython/blob/master/LICENSE                   |
| ipython-genutils                 | https://github.com/ipython/ipython_genutils                                            | https://github.com/ipython/ipython_genutils/blob/master/LICENSE          |
| ipywidgets                       | http://jupyter.org                                                                     | https://github.com/jupyter-widgets/ipywidgets/blob/master/LICENSE        |
| isodate                          | https://github.com/gweis/isodate/                                                      | https://github.com/gweis/isodate/blob/master/LICENSE                     |
| itsdangerous                     | https://palletsprojects.com/p/itsdangerous/                                            | https://github.com/pallets/itsdangerous/blob/main/LICENSE.rst            |
| jax                              | https://github.com/google/jax                                                          | https://github.com/google/jax/blob/main/LICENSE                          |
| jaxlib                           | https://github.com/google/jax                                                          | https://github.com/google/jax/blob/main/LICENSE                          |
| jedi                             | https://jedi.readthedocs.io/en/latest/                                                 | https://github.com/davidhalter/jedi/blob/master/LICENSE.txt              |
| Jinja2                           | https://palletsprojects.com/p/jinja/                                                   | https://github.com/pallets/jinja/blob/main/LICENSE.rst                   |
| jmespath                         | https://github.com/jmespath/jmespath.py                                                | https://github.com/jmespath/jmespath.py/blob/develop/LICENSE.txt         |
| joblib                           | https://joblib.readthedocs.io/en/latest/                                               | https://github.com/joblib/joblib/blob/master/LICENSE.txt                 |
| jpeg                             | https://www.ijg.org                                                                    | https://github.com/libjpeg-turbo/libjpeg-turbo/blob/main/LICENSE.md      |
| json5                            | https://github.com/dpranke/pyjson5                                                     | https://github.com/dpranke/pyjson5/blob/main/LICENSE                     |
| jsonfield                        | https://github.com/dmkoch/django-jsonfield/                                            | https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE           |
| jsonpatch                        | https://github.com/stefankoegl/python-json-patch                                       | https://github.com/stefankoegl/python-json-patch/blob/master/LICENSE     |
|                                  |                                                                                        | T                                                                        |
| Name of Project                  | Website                                                                                | Licen                                                                    |
| jsonpickle                       | https://github.com/jsonpickle/jsonpickle                                               | https:/                                                                  |
| jsonpointer                      | https://github.com/stefankoegl/python-json-pointer                                     | https:/                                                                  |
| jsonschema                       | https://github.com/python-jsonschema/jsonschema                                        | https:/                                                                  |
| jsonschema-specifications        | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst    | https:/                                                                  |
| jstat                            | https://github.com/jstat/jstat                                                         | https:/                                                                  |
| jupyter-client                   | https://jupyter.org                                                                    | https:/                                                                  |
| jupyter-core                     | https://jupyter.org                                                                    | https:/                                                                  |
| jupyter-events                   | https://github.com/jupyter/jupyter_events                                              | https:/                                                                  |
| jupyter-lsp                      | https://github.com/jupyter-lsp/jupyterlab-lsp                                          | https:/                                                                  |
| jupyter-serverhttp://jupyter.org | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE                     |                                                                          |
| jupyterlab                       | https://github.com/jupyterlab/jupyterlab                                               | https:/                                                                  |
| jupyterlab-pygments              | http://jupyter.org                                                                     | https:/                                                                  |
| jupyterlab-widgets               | http://jupyter.org                                                                     | https:/                                                                  |
| jupyterlab_server                | https://github.com/jupyterlab/jupyterlab_server                                        | https:/                                                                  |
| jupyter_client                   | http://jupyter.org                                                                     | https:/                                                                  |
| jupyter_core                     | http://jupyter.org                                                                     | https:/                                                                  |
| jupyter_server                   | https://github.com/jupyter-server/jupyter_server                                       | https:/                                                                  |
| jupyter_server_terminals         | https://github.com/jupyter-server/jupyter_server_terminals                             | https:/                                                                  |
| kaleido                          | https://github.com/plotly/Kaleido                                                      | https:/                                                                  |
| keras                            | https://github.com/keras-team/keras                                                    | https:/                                                                  |
| Keras-Preprocessing              | https://github.com/keras-team/keras-preprocessing                                      | https:/                                                                  |
| keras-tuner                      | https://github.com/keras-team/keras-tuner                                              | https:/                                                                  |
| keyring                          | https://github.com/jaraco/keyring                                                      | https:/                                                                  |
| keyutils                         | https://github.com/sassoftware/python-keyutils                                         | https:/                                                                  |
| kiwisolver                       | https://kiwisolver.readthedocs.io/en/latest/                                           | https:/                                                                  |
| kombu                            | https://kombu.readthedocs.io                                                           | https:/                                                                  |
| $\overline{\text{krb5}}$         | https://web.mit.edu/kerberos/                                                          | https:/                                                                  |
| kt-legacy                        | https://github.com/haifeng-jin/kt-legacy                                               | https:/                                                                  |
| lazy_loader                      | https://github.com/scientific-python/lazy_loader                                       | https:/                                                                  |
| lcms2                            | https://www.littlecms.com                                                              | https:/                                                                  |
| lerc                             | https://github.com/Esri/lerc                                                           | https:/                                                                  |
| libarchive                       | http://www.libarchive.org                                                              | https:/                                                                  |
| libblas                          | https://www.netlib.org/blas/                                                           | https:/                                                                  |
| libbrotlicommon                  | https://github.com/google/brotli                                                       | https:/                                                                  |
| libbrotlidec                     | https://github.com/google/brotli                                                       | https:/                                                                  |
| libbrotlienc                     | https://github.com/google/brotli                                                       | https:/                                                                  |
| libcblas                         | https://anaconda.org/conda-forge/libcblas                                              | N/A                                                                      |
| libclang                         | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| libcurl                          | https://curl.se/libcurl/                                                               | https:/                                                                  |
| libcxx                           | https://github.com/llvm-mirror/libcxx                                                  | https:/                                                                  |
| libdb                            | https://www.oracle.com/technology/software/products/berkeley-db/index.html             | https:/                                                                  |
| libdeflate                       | https://github.com/ebiggers/libdeflate                                                 | https:/                                                                  |
| libedit                          | https://thrysoee.dk/editline/                                                          | http://                                                                  |
| libev                            | https://software.schmorp.de/pkg/libev.html                                             | https:/                                                                  |
| libffi                           | https://github.com/libffi/libffi                                                       | https:/                                                                  |
| libgcrypt                        | https://gnupg.org/software/index.html                                                  | https:/                                                                  |
| libgd                            | https://libgd.github.io                                                                | https:/                                                                  |
| libglib                          | https://github.com/PolMine/libglib                                                     | https:/                                                                  |
|                                  |                                                                                        | -li                                                                      |
| Name of Project                  | Website                                                                                | Licen:                                                                   |
| libint                           | https://tinyurl.com/yvw97wbw                                                           | https:/                                                                  |
| liblapack                        | http://www.netlib.org/lapack/                                                          | https:/                                                                  |
| liblapacke                       | https://anaconda.org/conda-forge/liblapacke                                            | https:/                                                                  |
| libmamba                         | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23        | https:/                                                                  |
| libmambapy                       | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                   | https:/                                                                  |
| libnetcdf                        | https://www.unidata.ucar.edu/software/netcdf/                                          | https:/                                                                  |
| libnghttp2                       | https://github.com/nghttp2/nghttp2                                                     | https:/                                                                  |
| libopenblas                      | https://www.openblas.net/                                                              | https:/                                                                  |
| libpng                           | https://www.libpng.org/pub/png/libpng.html                                             | https:/                                                                  |
| libpq                            | https://www.postgresql.org/                                                            | https:/                                                                  |
| librsvg                          | https://gitlab.gnome.org/GNOME/librsvg                                                 | https:/                                                                  |
| libsolv                          | https://github.com/openSUSE/libsolv                                                    | https:/                                                                  |
| libssh <sub>2</sub>              | https://github.com/libssh2/libssh2                                                     | https:/                                                                  |
| libtiff                          | https://www.libtiff.org/                                                               | https:/                                                                  |
| libtrust                         | https://github.com/docker/libtrust                                                     | https:/                                                                  |
| libuuid                          | https://sourceforge.net/projects/libuuid/                                              | https:/                                                                  |
| libuv                            | https://github.com/libuv/libuv                                                         | https:/                                                                  |
| libwebp                          | https://chromium.googlesource.com/?format=HTML                                         | https:/                                                                  |
| libwebp-base                     | https://chromium.googlesource.com/?format=HTML                                         | https:/                                                                  |
| libxc                            | https://www.tddft.org/programs/libxc/                                                  | https:/                                                                  |
| libxcb                           | https://xcb.freedesktop.org                                                            | https:/                                                                  |
| libxml2                          | https://git.gnome.org/browse/libxml2/                                                  | https:/                                                                  |
| libxmlsec1                       | https://github.com/lsh123/xmlsec                                                       | https:/                                                                  |
| libxslt                          | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                    |                                                                          |
| libzlib                          | https://zlib.net                                                                       | https:/<br>https:/                                                       |
| lime                             | https://github.com/marcotcr/lime                                                       | https:/                                                                  |
| $\overline{\text{lit}}$          | http://llvm.org                                                                        |                                                                          |
|                                  | https://github.com/llvm-mirror/openmp                                                  | https:/                                                                  |
| llvm-openmp<br><b>Ilymlite</b>   | http://llvmlite.readthedocs.io                                                         | https:/                                                                  |
| loader-utils                     |                                                                                        | https:/                                                                  |
|                                  | https://github.com/webpack/loader-utils<br>https://logomaker.readthedocs.io/en/latest/ | https:/                                                                  |
| logomaker                        |                                                                                        | https:/                                                                  |
| logrus                           | https://github.com/sirupsen/logrus                                                     | https:/                                                                  |
| logrus-airbrake-hook.v2          | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                     | https:/                                                                  |
| lxml                             | https://lxml.de                                                                        | https:/                                                                  |
| $1z4-c$                          | https://www.lz4.org/                                                                   | https:/                                                                  |
| markdown                         | https://github.com/evilstreak/markdown-js                                              | https:/                                                                  |
| markdown-it-py                   | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| MarkupSafe                       | https://palletsprojects.com/p/markupsafe/                                              | https:/                                                                  |
| matplotlib                       | https://matplotlib.org                                                                 | https:/                                                                  |
| matplotlib-base                  | https://matplotlib.org                                                                 | https:/                                                                  |
| matplotlib-inline                | https://github.com/ipython/matplotlib-inline                                           | https:/                                                                  |
| mda-xdrlib                       | https://github.com/MDAnalysis/mda-xdrlib                                               | https:/                                                                  |
| mdtraj                           | https://www.mdtraj.org/                                                                | https:/                                                                  |
| mdurl                            | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| menuinst                         | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| mergo                            | https://github.com/imdario/mergo                                                       | https:/                                                                  |
| mistune                          | https://github.com/lepture/mistune                                                     | https:/                                                                  |
| mkl                              | https://github.com/rust-math/intel-mkl-src                                             | https:/                                                                  |
| mkl-fft                          | https://github.com/IntelPython/mkl_fft                                                 | https:/                                                                  |
| Name of Project                  | Website                                                                                | License                                                                  |
| mkl-random                       | https://github.com/IntelPython/mkl_random                                              | https://                                                                 |
| mkl-service                      | https://github.com/IntelPython/mkl-service                                             | https://                                                                 |
| $\overline{\text{ml-dtypes}}$    | <b>Orion Floes</b>                                                                     | https://                                                                 |
| molecupy                         | https://molecupy.readthedocs.io/en/latest/                                             | https://                                                                 |
| moment                           | https://github.com/moment/moment                                                       | https://                                                                 |
| moment-precise-range-plugin      | https://github.com/codebox/moment-precise-range                                        | https://                                                                 |
| more-itertools                   | https://github.com/more-itertools/more-itertools                                       | https://                                                                 |
| mpiplus                          | https://github.com/choderalab/mpiplus                                                  | https://                                                                 |
| mpmath                           | http://mpmath.org/                                                                     | https://                                                                 |
| mrcfile                          | https://github.com/ccpem/mrcfile                                                       | https://                                                                 |
| msgpack                          | https://msgpack.org/                                                                   | https://                                                                 |
| multidict                        | https://github.com/aio-libs/multidict                                                  | https://                                                                 |
| multierr                         | https://go.uber.org/multierr                                                           | https://                                                                 |
| multiprocess                     | https://github.com/uqfoundation/multiprocess                                           | https://                                                                 |
| munkres                          | https://software.clapper.org/munkres/                                                  | https://                                                                 |
| myesui uuid                      | https://github.com/myesui/uuid                                                         | https://                                                                 |
| namex                            | <b>Orion Floes</b>                                                                     | https://                                                                 |
| nbclassic                        | http://jupyter.org                                                                     | https://                                                                 |
| nbclient                         | https://jupyter.org                                                                    | https://                                                                 |
| nbconvert                        | https://jupyter.org                                                                    | https://                                                                 |
| nbformat                         | http://jupyter.org                                                                     | https://                                                                 |
| ncurses                          | https://invisible-island.net/ncurses/                                                  | https://                                                                 |
| nest-asyncio                     | https://github.com/erdewit/nest_asyncio                                                | https://                                                                 |
| netcdf-fortran                   | https://www.unidata.ucar.edu/software/netcdf/                                          | https://                                                                 |
| netCDF4                          | http://github.com/Unidata/netcdf4-python                                               | https://                                                                 |
| nettle                           | https://git.lysator.liu.se/nettle/nettle                                               | https://                                                                 |
| networkx                         | https://networkx.org                                                                   | https://                                                                 |
| nfpm                             | https://github.com/goreleaser/nfpm                                                     | https://                                                                 |
| ng-tags-input                    | https://github.com/mbenford/ngTagsInput                                                | https://                                                                 |
| ng-toast                         | https://github.com/tameraydin/ngToast                                                  | https://                                                                 |
| ngdraggable                      | https://github.com/fatlinesofcode/ngDraggable                                          | https://                                                                 |
| ngVue                            | https://github.com/ngVue/ngVue                                                         | https://                                                                 |
| nlopt                            | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                         | https://                                                                 |
| nodejs                           | https://nodejs.org/en/                                                                 | https://                                                                 |
| nomkl                            | https://github.com/conda-forge/nomkl-feedstock                                         | https://                                                                 |
| notebook                         | http://jupyter.org                                                                     | https://                                                                 |
| notebook-shim                    | https://github.com/jupyter/notebook_shim                                               | https://                                                                 |
| notebook_shim                    | http://jupyter.org                                                                     | https://                                                                 |
| numba                            | https://numba.pydata.org                                                               | https://                                                                 |
| numcpus                          | https://github.com/tklauser/numcpus                                                    | https://                                                                 |
| numexpr                          | https://github.com/pydata/numexpr                                                      | https://                                                                 |
| numpy                            | https://numpy.org                                                                      | https://                                                                 |
| numpy-base                       | https://numpy.org                                                                      | https://                                                                 |
| numpydoc                         | https://numpydoc.readthedocs.io/en/latest/index.html                                   | https://                                                                 |
| nvidia-cublas-cu11               | https://developer.nvidia.com/cuda-zone                                                 | https://                                                                 |
| nvidia-cublas-cu12               | https://developer.nvidia.com/cuda-zone                                                 | https://                                                                 |
| nvidia-cuda-cupti-cu11           | https://developer.nvidia.com/cuda-zone                                                 | https://                                                                 |
| nvidia-cuda-cupti-cu12           | https://developer.nvidia.com/cuda-zone                                                 | https://                                                                 |
| nvidia-cuda-nvrtc-cu11           | https://developer.nvidia.com/cuda-zone                                                 | https://                                                                 |
| Name of Project                  | Website                                                                                | License                                                                  |
| nvidia-cuda-nvrtc-cu12           | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cuda-runtime-cu11         | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cuda-runtime-cu12         | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cudnn-cu11                | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cudnn-cu12                | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cufft-cu11                | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cufft-cu12                | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-curand-cu11               | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-curand-cu12               | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cusolver-cu11             | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cusolver-cu12             | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cusparse-cu11             | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-cusparse-cu12             | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-nccl-cu11                 | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-nccl-cu12                 | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-nvjitlink-cu12            | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-nvtx-cu11                 | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| nvidia-nvtx-cu12                 | https://developer.nvidia.com/cuda-zone                                                 |                                                                          |
| Oat++                            | https://oatpp.io/                                                                      |                                                                          |
| oauthlib                         | https://github.com/oauthlib/oauthlib                                                   |                                                                          |
| ocl-icd                          | https://github.com/OCL-dev/ocl-icd                                                     |                                                                          |
| ocl-icd-system                   | https://github.com/conda-forge/ocl-icd-system-feedstock                                |                                                                          |
| olefile                          | https://www.decalage.info/python/olefileio                                             |                                                                          |
| OmegaFold                        | https://github.com/HeliXonProtein/OmegaFold/tree/main                                  |                                                                          |
| omnicanvas                       | https://omnicanvas.readthedocs.io/en/latest/                                           |                                                                          |
| OpenFF                           | https://openforcefield.org/                                                            |                                                                          |
| openff-amber-ff-ports            | https://github.com/openforcefield/openff-amber-ff-ports                                |                                                                          |
| openff-forcefields               | https://openforcefield.org                                                             |                                                                          |
| openff-interchange               | https://github.com/openforcefield/openff-interchange                                   |                                                                          |
| openff-models                    | https://github.com/openforcefield/openff-models                                        |                                                                          |
| openff-toolkit                   | https://openforcefield.org                                                             |                                                                          |
| openff-toolkit-base              | https://openforcefield.org                                                             |                                                                          |
| openff-units                     | https://github.com/openforcefield/openff-units                                         |                                                                          |
| openff-utilities                 | https://github.com/openforcefield/openff-utilities                                     |                                                                          |
| openjpeg                         | https://github.com/uclouvain/openjpeg                                                  |                                                                          |
| openldap                         | https://www.openldap.org/software/repo.html                                            |                                                                          |
| OpenMM                           | https://openmm.org                                                                     |                                                                          |
| openmmtools                      | https://github.com/choderalab/openmmtools                                              |                                                                          |
| openmoltools                     | https://github.com/choderalab/openmoltools                                             |                                                                          |
| openpyxl                         | https://openpyxl.readthedocs.io/en/stable/                                             |                                                                          |
| openssl                          | https://www.openssl.org                                                                |                                                                          |
| opt-einsum                       | https://github.com/dgasmith/opt_einsum                                                 |                                                                          |
| OptKing                          | https://github.com/psi-rking/optking                                                   |                                                                          |
| oscrypto                         | https://github.com/wbond/oscrypto                                                      |                                                                          |
| overrides                        | https://github.com/mkorpela/overrides                                                  |                                                                          |
| packaging                        | https://github.com/pypa/packaging                                                      |                                                                          |
| packmol                          | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                                  |                                                                          |
| pandas                           | https://pandas.pydata.org                                                              |                                                                          |
| pandocfilters                    | http://github.com/jgm/pandocfilters                                                    |                                                                          |
| Name of Project                  | Website                                                                                | License                                                                  |
| panedr                           | https://github.com/MDAnalysis/panedr                                                   | https:/                                                                  |
| pango                            | https://pango.gnome.org                                                                | https:/                                                                  |
| ParmEd                           | https://parmed.github.io/ParmEd/html/index.html                                        | https:/                                                                  |
| parser                           | https://github.com/typescript-eslint/typescript-eslint                                 | https:/                                                                  |
| parso                            | https://parso.readthedocs.io/en/latest/                                                | https:/                                                                  |
| pathos                           | https://github.com/uqfoundation/pathos                                                 | https:/                                                                  |
| patsy                            | https://patsy.readthedocs.io/en/latest/                                                | https:/                                                                  |
| pbkdf2                           | https://golang.org/x/crypto/pbkdf2                                                     | https:/                                                                  |
| pbr                              | https://docs.openstack.org/pbr/latest/                                                 | https:/                                                                  |
| pcmsolver                        | https://pcmsolver.readthedocs.io/en/stable/                                            | https:/                                                                  |
| pcre                             | https://www.pcre.org                                                                   | https:/                                                                  |
| pcre2                            | https://www.pcre.org                                                                   | https:/                                                                  |
| pdb4amber                        | https://github.com/Amber-MD/pdb4amber                                                  | https:/                                                                  |
| pdbfixer                         | https://github.com/openmm/pdbfixer                                                     | https:/                                                                  |
| pexpect                          | https://pexpect.readthedocs.io/                                                        | https:/                                                                  |
| pgconn                           | https://github.com/jackc/pgconn                                                        | https:/                                                                  |
| pgio                             | https://github.com/jackc/pgio                                                          | https:/                                                                  |
| pgpassfile                       | https://github.com/jackc/pgpassfile                                                    | https:/                                                                  |
| pgproto3                         | https://github.com/jackc/pgproto3/v2                                                   | https:/                                                                  |
| pgtype                           | https://github.com/jackc/pgtype                                                        | https:/                                                                  |
| pgx                              | https://github.com/jackc/pgx/v4                                                        | https:/                                                                  |
| phonopy                          | https://github.com/phonopy/phono3py                                                    | https:/                                                                  |
| pickleshare                      | https://github.com/pickleshare/pickleshare                                             | https:/                                                                  |
| Pillow                           | https://python-pillow.org                                                              | https:/                                                                  |
| Pint                             | https://pint.readthedocs.io/en/stable/                                                 | https:/                                                                  |
| pip                              | https://pip.pypa.io/                                                                   | https:/                                                                  |
| pip-licenses                     | https://github.com/raimon49/pip-licenses                                               | https:/                                                                  |
| pixman                           | https://pixman.org                                                                     | https:/                                                                  |
| pkginfo                          | https://launchpad.net/pkginfo                                                          | https:/                                                                  |
| platformdirs                     | https://github.com/platformdirs/platformdirs                                           | https:/                                                                  |
| plotly                           | https://plotly.com/python/                                                             | https:/                                                                  |
| plotly-orca                      | https://github.com/plotly/orca                                                         | https:/                                                                  |
| plotly.js                        | https://github.com/plotly/plotly.js                                                    | https:/                                                                  |
| pluggy                           | https://pluggy.readthedocs.io/en/stable/index.html                                     | https:/                                                                  |
| pooch                            | https://github.com/fatiando/pooch                                                      | https:/                                                                  |
| pox                              | https://github.com/uqfoundation/pox                                                    | https:/                                                                  |
| ppft                             | https://github.com/uqfoundation/ppft                                                   | https:/                                                                  |
| pq                               | https://github.com/lib/pq                                                              | https:/                                                                  |
| ProDy                            | http://www.csb.pitt.edu/ProDy                                                          | https:/                                                                  |
| prometheus-client                | https://github.com/prometheus/client_python                                            | https:/                                                                  |
| prompt-toolkit                   | https://python-prompt-toolkit.readthedocs.io/en/stable/                                | https:/                                                                  |
| protobuf                         | https://google.golang.org/protobuf                                                     | https:/                                                                  |
| psi4                             | https://psicode.org                                                                    | https:/                                                                  |
| psutil                           | https://psutil.readthedocs.io/en/latest/                                               | https:/                                                                  |
| psycopg2                         | https://psycopg.org/                                                                   | https:/                                                                  |
| PTable                           | https://github.com/kxxoling/PTable                                                     | https:/                                                                  |
| pthread-stubs                    | https://xcb.freedesktop.org                                                            | https:/                                                                  |
| ptyprocess                       | https://ptyprocess.readthedocs.io/en/latest/                                           | https:/                                                                  |
| pure-eval                        | http://github.com/alexmojaki/pure_eval                                                 | http://                                                                  |
| Name of Project                  | Website                                                                                | License                                                                  |
| py                               | https://py.readthedocs.io/en/latest/                                                   | https:/                                                                  |
| py-cpuinfo                       | https://github.com/workhorsy/py-cpuinfo                                                | https:/                                                                  |
| pyasn1                           | https://github.com/etingof/pyasn1                                                      | https:/                                                                  |
| pyasn1-modules                   | https://github.com/etingof/pyasn1-modules                                              | https:/                                                                  |
| pybind11-abi                     | https://github.com/pybind/pybind11                                                     | https:/                                                                  |
| pycairo                          | https://pycairo.readthedocs.io/en/latest/index.html                                    | https:/                                                                  |
| pycosat                          | https://github.com/conda/pycosat                                                       | https:/                                                                  |
| pycparser                        | https://github.com/eliben/pycparser                                                    | https:/                                                                  |
| pydantic                         | https://pydantic-docs.helpmanual.io                                                    | https:/                                                                  |
| pydantic-core                    | https://github.com/pydantic/pydantic-core                                              | https:/                                                                  |
| pyedr                            | https://github.com/MDAnalysis/panedr                                                   | https:/                                                                  |
| pyEMMA                           | http://github.com/markovmodel/PyEMMA                                                   | https:/                                                                  |
| Pygments                         | https://pygments.org                                                                   | https:/                                                                  |
| pygraphviz                       | https://pygraphviz.github.io                                                           | https:/                                                                  |
| pygtop                           | https://pygtop.readthedocs.io/en/latest/                                               | https:/                                                                  |
| pyHanko                          | https://github.com/MatthiasValvekens/pyHanko                                           | https:/                                                                  |
| pyhanko-certvalidator            | https://github.com/MatthiasValvekens/certvalidator                                     | https:/                                                                  |
| PyJWT                            | https://github.com/jpadilla/pyjwt                                                      | https:/                                                                  |
| pymbar                           | https://pymbar.org                                                                     | https:/                                                                  |
| pyOpenSSL                        | https://pyopenssl.org/                                                                 | https:/                                                                  |
| pyparsing                        | https://pyparsing-docs.readthedocs.io/en/latest/                                       | https:/                                                                  |
| PyPDF3                           | https://github.com/sfneal/PyPDF3                                                       | https:/                                                                  |
| pyrsistent                       | http://github.com/tobgu/pyrsistent/                                                    | https:/                                                                  |
| pysam                            | https://github.com/pysam-developers/pysam                                              | https:/                                                                  |
| PySocks                          | https://github.com/Anorov/PySocks                                                      | https:/                                                                  |
| pytables                         | https://www.pytables.org                                                               | https:/                                                                  |
| python                           | https://www.python.org/                                                                | https:/                                                                  |
| python-bidi                      | https://github.com/MeirKriheli/python-bidi                                             | https:/                                                                  |
| python-constraint                | https://github.com/python-constraint/python-constraint                                 | https:/                                                                  |
| python-dateutil                  | https://dateutil.readthedocs.io                                                        | https:/                                                                  |
| python-json-logger               | http://github.com/madzak/python-json-logger                                            | https:/                                                                  |
| python-ldap                      | https://www.python-ldap.org/                                                           | https:/                                                                  |
| python3-saml                     | https://github.com/onelogin/python3-saml                                               | https:/                                                                  |
| python_abi                       | https://github.com/conda-forge/python_abi-feedstock                                    | https:/                                                                  |
| pytz                             | https://pythonhosted.org/pytz                                                          | https:/                                                                  |
| pytz-deprecation-shim            | https://github.com/pganssle/pytz-deprecation-shim                                      | https:/                                                                  |
| PyWavelets                       | https://github.com/PyWavelets/pywt                                                     | https:/                                                                  |
| <b>PyYAML</b>                    | https://pyyaml.org/                                                                    | https:/                                                                  |
| pyyml                            | No longer available                                                                    | No lor                                                                   |
| pyzmq                            | https://pyzmq.readthedocs.io/en/latest/                                                | https:/                                                                  |
| qcelemental                      | https://github.com/MolSSI/QCElemental                                                  | https:/                                                                  |
| qcengine                         | https://github.com/MolSSI/QCEngine                                                     | https:/                                                                  |
| qrcode                           | https://github.com/lincolnloop/python-qrcode                                           | https:/                                                                  |
| ramda                            | https://github.com/ramda/ramda                                                         | https:/                                                                  |
| rapidjson                        | https://rapidjson.org/                                                                 | https:/                                                                  |
| rdkit                            | https://www.rdkit.org                                                                  | https:/                                                                  |
| re2                              | https://github.com/google/re2                                                          | https:/                                                                  |
| readme-renderer                  | https://github.com/pypa/readme_renderer                                                | https:/                                                                  |
| redis-py                         | https://github.com/andymccurdy/redis-py                                                | https:/                                                                  |
|                                  |                                                                                        | Ιá                                                                       |
| Name of Project                  | Website                                                                                | Licen:                                                                   |
| referencing                      | https://github.com/python-jsonschema/referencing                                       | https:/                                                                  |
| regex                            | https://github.com/mrabarnett/mrab-regex                                               | https:/                                                                  |
| reportlab                        | https://www.reportlab.com                                                              | https:/                                                                  |
| reproc                           | https://github.com/DaanDeMeyer/reproc                                                  | https:/                                                                  |
| reproc-cpp                       | https://github.com/DaanDeMeyer/reproc                                                  | https:/                                                                  |
| requests                         | https://requests.readthedocs.io                                                        | https:/                                                                  |
| requests-oauthlib                | https://github.com/requests/requests-oauthlib                                          | https:/                                                                  |
| requests-toolbelt                | https://toolbelt.readthedocs.org                                                       | https:/                                                                  |
| resumable                        | https://github.com/stevvooe/resumable                                                  | https:/                                                                  |
| retrying                         | https://github.com/rholder/retrying                                                    | https:/                                                                  |
| rfc3339-validator                | https://github.com/naimetti/rfc3339-validator                                          | https:/                                                                  |
| rfc3986                          | https://rfc3986.readthedocs.io/en/latest/                                              | https:/                                                                  |
| rfc3986-validator                | https://github.com/naimetti/rfc3986-validator                                          | https:/                                                                  |
| rich                             | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| rpds-py                          | https://github.com/crate-py/rpds                                                       | https:/                                                                  |
| rpmpack                          | https://github.com/google/rpmpack                                                      | https:/                                                                  |
| rsa                              | https://stuvel.eu/rsa                                                                  | https:/                                                                  |
| ruamel-yaml                      | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                            | https:/                                                                  |
| ruamel.yaml.clib                 | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                       | https:/                                                                  |
| s3transfer                       | https://github.com/boto/s3transfer                                                     | https:/                                                                  |
| sasl                             | https://mellium.im/sasl                                                                | https:/                                                                  |
| scikit-gstat                     | https://mmaelicke.github.io/scikit-gstat/                                              | https:/                                                                  |
| scikit-image                     | https://scikit-image.org                                                               | https:/                                                                  |
| scikit-learn                     | https://scikit-learn.org/stable/                                                       | https:/                                                                  |
| scikit-learn-extra               | https://github.com/scikit-learn-contrib/scikit-learn-extra                             | https:/                                                                  |
| scipy                            | https://scipy.org                                                                      | https:/                                                                  |
| seaborn                          | https://seaborn.pydata.org                                                             | https:/                                                                  |
| seaborn-base                     | https://seaborn.pydata.org                                                             | https:/                                                                  |
| semver                           | https://github.com/Masterminds/semver/v3                                               | https:/                                                                  |
| Send2Trash                       | https://github.com/arsenetar/send2trash                                                | https:/                                                                  |
| setuptools                       | https://github.com/pypa/setuptools                                                     | https:/                                                                  |
| setuptools-scm                   | https://github.com/pypa/setuptools_scm/                                                | https:/                                                                  |
| sh                               | https://github.com/amoffat/sh                                                          | https:/                                                                  |
| shellingham                      | https://github.com/sarugaku/shellingham                                                | https:/                                                                  |
| simint                           | https://www.bennyp.org/research/simint/                                                | https:/                                                                  |
| six                              | https://github.com/benjaminp/six                                                       | https:/                                                                  |
| smirnoff99frosst                 | https://github.com/openforcefield/smirnoff99frosst                                     | https:/                                                                  |
| snappy                           | https://github.com/google/snappy                                                       | https:/                                                                  |
| sniffio                          | https://github.com/python-trio/sniffio                                                 | https:/                                                                  |
| snowballstemmer                  | https://github.com/snowballstem/snowball                                               | https:/                                                                  |
| soupsieve                        | https://github.com/facelessuser/soupsieve                                              | https:/                                                                  |
| spglib                           | Orion Floes                                                                            | https:/                                                                  |
| sphinx                           | https://github.com/sphinx-doc/sphinx                                                   | https:/                                                                  |
| sphinxcontrib-applehelp          | https://github.com/sphinx-doc/sphinxcontrib-applehelp                                  | https:/                                                                  |
| sphinxcontrib-devhelp            | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                    | https:/                                                                  |
| sphinxcontrib-htmlhelp           | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                   | https:/                                                                  |
| sphinxcontrib-jsmath             | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                     | https:/                                                                  |
| sphinxcontrib-qthelp             | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                     | https:/                                                                  |
| sphinxcontrib-serializinghtml    | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                            | https:/                                                                  |
|                                  |                                                                                        |                                                                          |
|                                  |                                                                                        | J)                                                                       |
| Name of Project                  | Website                                                                                | Licen                                                                    |
| SQLAlchemy                       | https://www.sqlalchemy.org                                                             | https:/                                                                  |
| sqlite                           | https://sqlite.org/index.html                                                          | https:/                                                                  |
| sqlparse                         | https://github.com/andialbrecht/sqlparse                                               | https:/                                                                  |
| stack-data                       | http://github.com/alexmojaki/stack_data                                                | https:/                                                                  |
| starfile                         | https://github.com/alisterburt/starfile                                                | https:/                                                                  |
| statsmodels                      | https://github.com/statsmodels/statsmodels                                             | https:/                                                                  |
| structlog                        | https://www.structlog.org/                                                             | https:/                                                                  |
| svglib                           | https://github.com/deeplook/svglib                                                     | https:/                                                                  |
| sympy                            | https://sympy.org                                                                      | https:/                                                                  |
| tables                           | https://www.pytables.org/                                                              | https:/                                                                  |
| tabulate                         | https://github.com/astanin/python-tabulate                                             | https:/                                                                  |
| tbb                              | https://github.com/oneapi-src/oneTBB                                                   | https:/                                                                  |
| tenacity                         | https://github.com/jd/tenacity                                                         | https:/                                                                  |
| tensorboard                      | https://github.com/tensorflow/tensorboard                                              | https:/                                                                  |
| tensorboard-data-server          | https://github.com/tensorflow/tensorboard                                              | https:/                                                                  |
| tensorboard-plugin-wit           | https://github.com/pair-code/what-if-tool                                              | https:/                                                                  |
| tensorflow                       | https://github.com/tensorflow/tensorflow                                               | https:/                                                                  |
| tensorflow-estimator             | https://github.com/tensorflow/estimator                                                | https:/                                                                  |
| tensorflow-io-gcs-filesystem     | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| tensorflow-probability           | https://github.com/tensorflow/probability                                              | https:/                                                                  |
| termcolor                        | https://github.com/hugovk/termcolor                                                    | https:/                                                                  |
| terminado                        | https://github.com/jupyter/terminado                                                   | https:/                                                                  |
| testpath                         | https://github.com/jupyter/testpath                                                    | https:/                                                                  |
| textangular                      | https://github.com/fraywing/textAngular                                                | https:/                                                                  |
| tf_keras                         | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| threadpoolctl                    | https://github.com/joblib/threadpoolctl                                                |                                                                          |
| three                            | https://github.com/mrdoob/three.js                                                     | https:/                                                                  |
| tifffile                         | https://github.com/cgohlke/tifffile/                                                   | https:/                                                                  |
|                                  | https://github.com/Kozea/tinycss2/                                                     | https:/                                                                  |
| tinycss2                         |                                                                                        | https:/                                                                  |
| tinyxml2                         | https://github.com/leethomason/tinyxml2                                                | https:/                                                                  |
| tk                               | https://www.tcl.tk/                                                                    | https:/                                                                  |
| toml                             | https://github.com/toml-lang/toml                                                      | https:/                                                                  |
| tomli                            | https://github.com/hukkin/tomli                                                        | https:/                                                                  |
| toolz                            | https://github.com/pytoolz/toolz                                                       | https:/                                                                  |
| torch                            | https://pytorch.org/                                                                   | https:/                                                                  |
| tornado                          | https://www.tornadoweb.org                                                             | https:/                                                                  |
| tqdm                             | https://github.com/tqdm/tqdm                                                           | https:/                                                                  |
| tracy                            | https://github.com/gear-genomics/tracy                                                 | https:/                                                                  |
| traitlets                        | https://github.com/ipython/traitlets                                                   | https:/                                                                  |
| triton                           | https://github.com/openai/triton/                                                      | https:/                                                                  |
| truststore                       | <b>Orion Floes</b>                                                                     | https:/                                                                  |
| ts-jest                          | https://github.com/kulshekhar/ts-jest                                                  | https:/                                                                  |
| ts-loader                        | https://github.com/TypeStrong/ts-loader                                                | https:/                                                                  |
| twine                            | https://github.com/pypa/twine                                                          | https:/                                                                  |
| twinj uuid                       | https://github.com/twinj/uuid                                                          | https:/                                                                  |
| types                            | https://github.com/babel/babel                                                         | https:/                                                                  |
| typescript                       | https://github.com/Microsoft/TypeScript                                                | https:/                                                                  |
| typing_extensions                | https://github.com/python/typing                                                       | https:/                                                                  |
| tzdata                           | https://github.com/python/tzdata                                                       | https:/                                                                  |
| Name of Project                  | Website                                                                                | License                                                                  |
| tzlocal                          | https://github.com/regebro/tzlocal                                                     | MIT                                                                      |
| umi-tools                        | https://github.com/CGATOxford/UMI-tools                                                | MIT                                                                      |
| unicodedata2                     | https://github.com/fonttools/unicodedata2                                              | MIT                                                                      |
| uritools                         | https://github.com/tkem/uritools/                                                      | MIT                                                                      |
| urllib3                          | https://urllib3.readthedocs.io/                                                        | MIT                                                                      |
| vine                             | https://github.com/celery/vine                                                         | BSD                                                                      |
| vue                              | https://github.com/vuejs/vue                                                           | MIT                                                                      |
| wcwidth                          | https://github.com/jquast/wcwidth                                                      | MIT                                                                      |
| webencodings                     | https://github.com/gsnedders/python-webencodings                                       | BSD                                                                      |
| websocket-client                 | https://github.com/websocket-client/websocket-client.git                               | BSD                                                                      |
| Werkzeug                         | https://palletsprojects.com/p/werkzeug/                                                | BSD                                                                      |
| westpa                           | https://github.com/westpa/westpa                                                       | MIT                                                                      |
| wheel                            | https://github.com/pypa/wheel                                                          | MIT                                                                      |
| widgetsnbextension               | https://github.com/jupyter-widgets/ipywidgets#readme                                   | BSD                                                                      |
| wrapt                            | https://github.com/GrahamDumpleton/wrapt                                               | BSD                                                                      |
| wsutil                           | https://github.com/yhat/wsutil                                                         | BSD                                                                      |
| x/lint                           | https://golang.org/x/lint                                                              | BSD                                                                      |
| x/mod                            | https://golang.org/x/mod/semver                                                        | BSD                                                                      |
| x/net                            | https://golang.org/x/net                                                               | BSD                                                                      |
| x/oauth2                         | https://golang.org/x/oauth2                                                            | BSD                                                                      |
| x/sys                            | https://golang.org/x/sys                                                               | BSD                                                                      |
| x/text                           | https://golang.org/x/text                                                              | BSD                                                                      |
| x/tools                          | https://golang.org/x/tools                                                             | BSD                                                                      |
| x/xerrors                        | https://golang.org/x/xerrors                                                           | BSD                                                                      |
| xhtml2pdf                        | https://github.com/xhtml2pdf/xhtml2pdf                                                 | BSD                                                                      |
| xlrd                             | https://github.com/python-excel/xlrd                                                   | BSD                                                                      |
| xmlsec                           | https://github.com/mehcode/python-xmlsec                                               | MIT                                                                      |
| xmltodict                        | https://github.com/martinblech/xmltodict                                               | MIT                                                                      |
| xorg-kbproto                     | https://gitlab.freedesktop.org/xorg/proto/kbproto                                      | MIT                                                                      |
| xorg-libice                      | https://gitlab.freedesktop.org/xorg/lib/libice                                         | MIT                                                                      |
| xorg-libsm                       | https://gitlab.freedesktop.org/xorg/lib/libsm                                          | MIT                                                                      |
| xorg-libx11                      | https://gitlab.freedesktop.org/xorg/lib/libx11                                         | MIT                                                                      |
| xorg-libxau                      | https://gitlab.freedesktop.org/xorg/lib/libxau                                         | MIT                                                                      |
| xorg-libxdmcp                    | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                       | MIT                                                                      |
| xorg-libxext                     | https://gitlab.freedesktop.org/xorg/lib/libxext                                        | MIT                                                                      |
| xorg-libxrender                  | https://gitlab.freedesktop.org/xorg/lib/libxrender                                     | MIT                                                                      |
| xorg-libxt                       | https://gitlab.freedesktop.org/xorg/lib/libxt                                          | MIT                                                                      |
| xorg-renderproto                 | https://gitlab.freedesktop.org/xorg/proto/renderproto                                  | MIT                                                                      |
| xorg-xextproto                   | https://gitlab.freedesktop.org/xorg/proto/xextproto                                    | MIT                                                                      |
| xorg-xproto                      | https://gitlab.freedesktop.org/xorg/proto/xproto                                       | MIT                                                                      |
| xxhash                           | https://github.com/cespare/xxhash/v2                                                   | BSD                                                                      |
| xz                               | https://github.com/ulikunitz/xz                                                        | MIT                                                                      |
| yaml                             | https://pyyaml.org/                                                                    | MIT                                                                      |
| yaml-cpp                         | https://github.com/jbeder/yaml-cpp                                                     | MIT                                                                      |
| yaml.v2                          | https://gopkg.in/yaml.v2                                                               | Apache-2.0                                                               |
| yaml.v3                          | https://gopkg.in/yaml.v3                                                               | Apache-2.0                                                               |
| yarl                             | https://github.com/aio-libs/yarl/                                                      | Apache-2.0                                                               |
| yaspin                           | https://github.com/pavdmyt/yaspin                                                      | MIT                                                                      |
| yfiles                           | https://www.yworks.com/products/yfiles                                                 | Commercial                                                               |
| Name of Project                  | Website                                                                                | License                                                                  |
| yml                              | https://pypi.org/project/yml/                                                          | N/A                                                                      |
| zap                              | https://go.uber.org/zap                                                                |                                                                          |
| zipp                             | https://github.com/jaraco/zipp                                                         |                                                                          |
| zlib                             | https://zlib.net/                                                                      |                                                                          |
| zstandard                        | https://github.com/indygreg/python-zstandard                                           |                                                                          |
| zstd                             | https://facebook.github.io/zstd/                                                       |                                                                          |
| _libgcc_mutex                    | https://github.com/conda-forge/_libgcc_mutex-feedstock                                 |                                                                          |
| _openmp_mutex                    | https://github.com/conda-forge/_openmp_mutex-feedstock                                 |                                                                          |

https://www.gnu.org/software/libiconv/

libiconv

https:/

# **10.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

# **10.1.1 GCC RUNTIME LIBRARY EXCEPTION**

```
Version 3.1, 31 March 2009
Copyright © 2009 Free Software Foundation, Inc. http://fsf.org/
Everyone is permitted to copy and distribute verbatim copies of this license document,
\rightarrow but changing it is not allowed.
This GCC Runtime Library Exception ("Exception") is an additional permission under.
\rightarrow section 7 of the GNU General Public License,
version 3 ("GPLv3"). It applies to a given file (the "Runtime Library") that bears a
\rightarrownotice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

```
(continues on next page)
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

## **10.1.2 GNU GENERAL PUBLIC LICENSE**

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

License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. 14. Revised Versions of this License. The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. 15. Disclaimer of Warranty. THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 16. Limitation of Liability. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE

USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

17. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page)

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

### See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# A

```
AddFraq
   OEConfGen:: OEMakeFragLib, 54
AddFragLib
   OEConfGen:: OEBuilderBase, 21
   OEConfGen:: OEOmega, 60
AddTorsionLibrary
   OEConfGen:: OETorLib, 78
AddTorsionRule
   OEConfGen:: OETorLib, 78
```

# B

```
Build
   OEConfGen:: OEConformerBuilder, 29
   OEConfGen:: OEFragBuilder, 41
   OEConfGen:: OEMacrocycleBuilder, 46
   OEConfGen:: OEMacrocycleOmega, 50
   OEConfGen:: OEMolBuilder, 55
   OEConfGen:: OEOmega, 61
```

# $\mathsf{C}$

```
ClearFraqLibs
   OEConfGen::OEBuilderBase, 21
   OEConfGen:: OEOmega, 61
ClearTorsionLibrary
   OEConfGen:: OETorLib, 79
Constructors
   OEConfGen:: OEConfFixOptions, 23
   OEConfGen:: OEConformerBuilder, 28
   OEConfGen::OEConfSlicer, 29
   OEConfGen::OEFlipperClassicOptions,
       30
   OEConfGen:: OEFlipperOptions, 35
   OEConfGen:: OEFragBuilder, 40
   OEConfGen:: OEFragBuilderOptions, 42
   OEConfGen:: OEFragOptions, 44
   OEConfGen:: OEMacrocycleBuilder, 46
   OEConfGen::OEMacrocycleBuilderOptions,
       47
   OEConfGen:: OEMacrocycleOmega, 49
   OEConfGen:: OEMacrocycleOmegaOptions,
       51
```

```
OEConfGen:: OEMakeFraqLib, 53
OEConfGen:: OEMolBuilder, 55
OEConfGen:: OEMolBuilderOptions, 56
OEConfGen:: OEOmega. 60
OEConfGen:: OEOmegaOptions, 62
OEConfGen:: OERingFragOptions, 67
OEConfGen::OESliceEnsembleOptions,
   68
OEConfGen:: OEThompsonOptions, 97
OEConfGen::OETorDriveOptions, 71
OEConfGen:: OETorDriver.76
OEConfGen:: OETorLib, 78
OEConfGen::OETorLibParameter, 81
```

# D

dense\_omega.py Example Code, 12

# F

```
Example Code
   dense_omega.py, 12
   macrocycle.py, 18
   make_fraglib.py, 16
   simple_omega.py, 9
   single conf macrocycle.pv. 19
   single_conformer.py, 11
   stereo_and_torsion.py, 14
   torsion_drive.py, 15
ExceedsMaxRotors
   OEConfGen:: OETorDriveOptions, 72
```

# G

GenerateConfs OEConfGen:: OETorDriver, 76 GenerateMissingFrags OEConfGen:: OEMakeFragLib, 54 GetAtomExpr OEConfGen:: OEConfFixOptions, 23 GetAtomPredicate OEConfGen::OEFlipperClassicOptions,  $31$ OEConfGen:: OEFlipperOptions, 35

GetBatchMaxRotors OEConfGen:: OEThompsonOptions, 98 GetBondExpr OEConfGen:: OEConfFixOptions, 24 GetBondPredicate OEConfGen::OEFlipperClassicOptions, 31 OEConfGen:: OEFlipperOptions, 35 GetCanonOrder OEConfGen:: OEMolBuilderOptions, 57 GetCommentEnergy OEConfGen::OETorDriveOptions, 72 GetConfFixOptions OEConfGen:: OEOmegaOptions, 62 GetDielectricConst OEConfGen:: OEMacrocycleBuilderOptions, 48 GetEnergyRange OEConfGen::OESliceEnsembleOptions, 68 GetEnergyWindow OEConfGen:: OEFragOptions, 44 OEConfGen:: OEMacrocycleOmegaOptions, GetFixSmarts 51 OEConfGen:: OEOmegaOptions, 63 OEConfGen::OESliceEnsembleOptions, 68 GetEnhancedStereo OEConfGen::OEFlipperClassicOptions, 31 OEConfGen:: OEFlipperOptions, 35 GetEnumAtoms OEConfGen:: OEFlipperOptions, 35 GetEnumAtomSpecifiedStereo OEConfGen:: OEFlipperOptions, 36 GetEnumBonds OEConfGen:: OEFlipperOptions, 36 GetEnumBondSpecifiedStereo OEConfGen:: OEFlipperOptions, 36 GetEnumBridgehead OEConfGen::OEFlipperClassicOptions, 31 OEConfGen:: OEFlipperOptions, 36 GetEnumEZ OEConfGen::OEFlipperClassicOptions, 31 OEConfGen:: OEFlipperOptions, 36 GetEnumNitrogen OEConfGen::OEFlipperClassicOptions,  $31$ OEConfGen:: OEFlipperOptions, 36 OEConfGen:: OEMolBuilderOptions, 57 GetEnumRelativeAtomStereo OEConfGen:: OEFlipperOptions, 37

GetEnumRing OEConfGen:: OEMolBuilderOptions, 57 GetEnumRS OEConfGen::OEFlipperClassicOptions, 32 OEConfGen:: OEFlipperOptions, 36 GetEnumSpecifiedStereo OEConfGen::OEFlipperClassicOptions, 32 OEConfGen:: OEFlipperOptions, 37 GetFixDeleteH OEConfGen:: OEConfFixOptions, 24 GetFixMaxMatch OEConfGen:: OEConfFixOptions, 24 GetFixMCS OEConfGen::OEConfFixOptions, 24 GetFixMol OEConfGen:: OEConfFixOptions, 24 GetFixPredicate OEConfGen:: OEConfFixOptions, 24 GetFixRMS OEConfGen:: OEConfFixOptions, 24 OEConfGen:: OEConfFixOptions, 25 GetFixSubSearch OEConfGen:: OEConfFixOptions, 25 GetFixUniqueMatch OEConfGen:: OEConfFixOptions, 25 GetForceField OEConfGen:: OEFragBuilderOptions, 42 OEConfGen:: OETorDriveOptions, 72 OEConfGen::OETorDriver, 76 GetFragBuilderOptions OEConfGen:: OEMolBuilderOptions, 57 GetFragGen OEConfGen:: OEFragOptions, 44 GetFraqKeep OEConfGen:: OEFragOptions, 44 GetFromCT OEConfGen:: OEMolBuilderOptions, 57 GetIqnoreStereo OEConfGen:: OEMolBuilderOptions, 57 GetIncludeInput OEConfGen:: OEOmegaOptions, 63 GetIterCycleSize OEConfGen::OEMacrocycleOmegaOptions, 51 GetMacrocycleBuilderOptions OEConfGen::OEMacrocycleOmegaOptions,  $51$ GetMacroCycOptions OEConfGen::OEFragBuilderOptions, 42 GetMaxCenters

OEConfGen::OEFlipperClassicOptions, 32 OEConfGen:: OEFlipperOptions, 37 GetMaxConfRange OEConfGen::OESliceEnsembleOptions, 68 GetMaxConfs OEConfGen:: OEMacrocycleOmegaOptions, GetRMSRange 51 OEConfGen:: OEOmegaOptions, 63 OEConfGen:: OESliceEnsembleOptions, 68 GetMaxEnumConfs OEConfGen:: OEMolBuilderOptions, 58 GetMaxIter OEConfGen::OEMacrocycleOmegaOptions, GetRotorPredicate  $51$ GetMaxRotors OEConfGen:: OETorDriveOptions, 72 GetMaxSearchTime OEConfGen:: OETorDriveOptions, 72 GetMaxTerminalHeavy OEConfGen::OESliceEnsembleOptions, 69 GetMaxTrials OEConfGen:: OEThompsonOptions, 98 GetMaxTrialsRange OEConfGen:: OEThompsonOptions, 98 GetMCSFunc OEConfGen:: OEConfFixOptions, 25 GetMCSMinAtoms OEConfGen:: OEConfFixOptions, 25 GetMCSType OEConfGen:: OEConfFixOptions, 25 GetMissingFrags OEConfGen:: OEMakeFraqLib, 54 GetMolBuilderOptions OEConfGen:: OEOmegaOptions, 63 GetNonRingOptions OEConfGen:: OEFragBuilderOptions, 42 GetOptions OEConfGen:: OEFragBuilder, 41 OEConfGen:: OEMacrocycleBuilder, 47 OEConfGen:: OEMacrocycleOmega, 50 OEConfGen:: OEMolBuilder, 55 OEConfGen:: OEOmega, 61 GetPriorTemperature OEConfGen:: OEThompsonOptions, 98 GetRandomSeed OEConfGen:: OEMacrocycleBuilderOptions, 48 GetRangeIncrement OEConfGen::OESliceEnsembleOptions, 69

GetRefTolerance OEConfGen:: OEMacrocycleBuilderOptions, 48 GetRingOptions OEConfGen:: OEFragBuilderOptions, 42 GetRMS OEConfGen:: OEFragOptions, 45 OEConfGen::OESliceEnsembleOptions, 69 GetRMSThreshold OEConfGen::OESliceEnsembleOptions, 69 GetRotorOffset OEConfGen::OETorDriveOptions, 72 OEConfGen:: OETorDriveOptions, 72 GetSampleHydrogens OEConfGen:: OEMolBuilderOptions, 58 GetSDEnergy OEConfGen:: OETorDriveOptions, 73 GetSkipRefinement OEConfGen:: OEMacrocycleBuilderOptions, 48 GetSliceEnsembleOptions OEConfGen::OEMacrocycleOmegaOptions, 52 OEConfGen:: OEOmegaOptions, 63 OEConfGen::OETorDriver, 76 GetStartFactor OEConfGen:: OERingFragOptions, 67 GetStrictAtomTypes OEConfGen:: OEMolBuilderOptions, 58 GetStrictStereo OEConfGen:: OEOmegaOptions, 63 GetThompsonOptions OEConfGen::OETorDriveOptions, 73 GetTimeLimit OEConfGen:: OEFragOptions, 45 GetTorDriveOptions OEConfGen:: OEOmegaOptions, 63 OEConfGen::OETorDriver, 77 GetTorLib OEConfGen:: OETorDriveOptions, 73 GetTorRule OEConfGen:: OETorLib, 79 GetTorRules OEConfGen:: OETorLib, 80 GetTorsionDrive OEConfGen:: OEOmegaOptions, 64 GetTrialsRangeIncrement OEConfGen:: OEThompsonOptions, 98 GetUseGPU OEConfGen:: OETorDriveOptions, 73

GetUseThompson OEConfGen:: OETorDriveOptions, 73 GetWarts OEConfGen::OEFlipperClassicOptions, 32 OEConfGen:: OEFlipperOptions, 37 OEConfGen:: OEOmegaOptions, 64

# H

HasFixPattern OEConfGen:: OEConfFixOptions, 25 HasTorRule OEConfGen:: OETorLib, 80

# M

macrocycle.py Example Code, 18 make\_fraglib.py Example Code, 16

# O

OEConfGen::OEAddGlobalFragLib, 91 OEConfGen:: OEBuilderBase, 21 AddFragLib, 21 ClearFragLibs, 21 OEConfGen::OEClearGlobalFragLib, 91 OEConfGen::OEConfFixOptions, 22 Constructors, 23 GetAtomExpr, 23 GetBondExpr, 24 GetFixDeleteH, 24 GetFixMaxMatch, 24 GetFixMCS.24 GetFixMol, 24 GetFixPredicate, 24 GetFixRMS, 24 GetFixSmarts, 25 GetFixSubSearch, 25 GetFixUniqueMatch, 25 GetMCSFunc, 25 GetMCSMinAtoms, 25 GetMCSType, 25 HasFixPattern, 25  $operatorerator =$ , 23 SetAtomExpr, 26 SetBondExpr. 26 SetFixDeleteH, 26 SetFixMaxMatch, 26 SetFixMCS, 27 SetFixMol.26 SetFixPredicate, 27 SetFixRMS.27 SetFixSmarts, 27 SetFixSubSearch, 27

SetFixUniqueMatch, 27 SetMCSFunc. 28 SetMCSMinAtoms, 28 SetMCSType, 28 OEConfGen:: OEConformerBuilder, 28 Build, 29 Constructors, 28 operator=, 29 OEConfGen::OEConfSlicer, 29 Constructors, 29 operator=, 29 Slice, 30 OEConfGen::OEFlipper, 92 OEConfGen::OEFlipperClassicOptions, 30 Constructors, 30 GetAtomPredicate, 31 GetBondPredicate, 31 GetEnhancedStereo, 31 GetEnumBridgehead, 31 GetEnumEZ, 31 GetEnumNitrogen, 31 GetEnumRS, 32 GetEnumSpecifiedStereo, 32 GetMaxCenters. 32 GetWarts, 32 operator=, 31 SetAtomPredicate, 32 SetBondPredicate, 32 SetEnhancedStereo, 32 SetEnumBridgehead, 33 SetEnumEZ, 33 SetEnumNitrogen, 33 SetEnumRS, 33 SetEnumSpecifiedStereo, 34 SetMaxCenters, 34 SetWarts, 34 OEConfGen:: OEFlipperOptions, 34 Constructors, 35 GetAtomPredicate, 35 GetBondPredicate, 35 GetEnhancedStereo, 35 GetEnumAtoms, 35 GetEnumAtomSpecifiedStereo, 36 GetEnumBonds, 36 GetEnumBondSpecifiedStereo, 36 GetEnumBridgehead, 36 GetEnumEZ, 36 GetEnumNitrogen, 36 GetEnumRelativeAtomStereo, 37 GetEnumRS, 36 GetEnumSpecifiedStereo, 37 GetMaxCenters, 37 GetWarts, 37 operator=, 35

SetAtomPredicate, 37 SetBondPredicate, 37 SetEnhancedStereo, 37 SetEnumAtoms, 38 SetEnumAtomSpecifiedStereo, 38 SetEnumBonds, 38 SetEnumBondSpecifiedStereo, 38 SetEnumBridgehead, 39 SetEnumEZ.39 SetEnumNitrogen, 39 SetEnumRelativeAtomStereo, 39 SetEnumRS, 39 SetEnumSpecifiedStereo, 39 SetMaxCenters, 40 SetWarts, 40 OEConfGen:: OEFlipperStereoCenters, 93 OEConfGen:: OEFragBuilder, 40 Build, 41 Constructors, 40 GetOptions, 41 operator=, 40 SetOptions, 41 OEConfGen:: OEFragBuilderMode, 82 OEConfGen:: OEFragBuilderMode:: Default, 82 OEConfGen:: OEFragBuilderMode:: Dense, 82 OEConfGen:: OEFragBuilderMode:: Fast, 82 OEConfGen::OEFragBuilderMode::Strict, 83 OEConfGen:: OEFragBuilderOptions, 41 Constructors, 42 GetForceField. 42 GetMacroCycOptions, 42 GetNonRingOptions, 42 GetRingOptions, 42 operator=, 42 SetForceField, 43 SetMacroCycOptions, 43 SetNonRingOptions, 43 SetRingOptions, 43 OEConfGen:: OEFragOptions, 43 Constructors, 44 GetEnergyWindow, 44 GetFragGen, 44 GetFragKeep, 44 GetRMS, 45 GetTimeLimit, 45 operator=, 44 SetEnergyWindow, 45 SetFragGen, 45 SetFraqKeep, 45 SetRMS, 45 SetTimeLimit, 45 OEConfGen:: OEGetOmegaError, 92

OEConfGen:: OEGetTorValues, 92 OEConfGen:: OEIsMacrocycle, 92 OEConfGen:: OEMacrocycleBuilder, 46 Build, 46 Constructors, 46 GetOptions, 47 operator=, 46 SetOptions, 47 OEConfGen:: OEMacrocycleBuilderOptions, 47 Constructors, 47 GetDielectricConst, 48 GetRandomSeed, 48 GetRefTolerance, 48 GetSkipRefinement, 48 operator=, 48 SetDielectricConst, 48 SetRandomSeed, 48 SetRefTolerance, 49 SetSkipRefinement, 49 OEConfGen:: OEMacrocycleOmega, 49 Build, 50 Constructors, 49 GetOptions, 50 operator=, 49 SetOptions, 50 OEConfGen:: OEMacrocycleOmegaOptions, 50 Constructors, 51 GetEnergyWindow, 51 GetIterCycleSize, 51 GetMacrocycleBuilderOptions, 51 GetMaxConfs.51 GetMaxIter, 51 GetSliceEnsembleOptions, 52 operator= $, 51$ SetEnergyWindow, 52 SetIterCycleSize, 52 SetMacrocycleBuilderOptions, 52 SetMaxConfs, 52 SetMaxIter, 52 SetSliceEnsembleOptions, 53 OEConfGen:: OEMakeFragLib, 53 AddFrag, 54 Constructors, 53 GenerateMissingFrags, 54 GetMissingFrags, 54 operator=, 53 OEConfGen:: OEMolBuilder, 54 Build. 55 Constructors, 55 GetOptions, 55 operator=, 55 Prep, 55 SetOptions, 56

```
OEConfGen:: OEMolBuilderOptions, 56
                                           OEConfGen::OEOmegaForceFieldType::MMFF94Smod NOEST
   Constructors. 56
                                                  85
                                           OEConfGen:: OEOmegaForceFieldType:: MMFF94Smod SHEFF,
   GetCanonOrder, 57
   GetEnumNitrogen, 57
                                                  86
   GetEnumRing, 57
                                           OEConfGen::OEOmegaForceFieldType::MMFF94Smod_TRUNC,
   GetFragBuilderOptions, 57
                                                  85
   GetFromCT.57
                                           OEConfGen::OEOmegaForceFieldType::MMFF NOESTAT,
   GetIqnoreStereo, 57
                                                  84
   GetMaxEnumConfs, 58
                                           OEConfGen::OEOmegaForceFieldType::MMFF_SHEFF,
   GetSampleHydrogens, 58
                                                  85
   GetStrictAtomTypes, 58
                                           OEConfGen::OEOmegaForceFieldType::MMFF_TRUNC,
   operator=, 57
                                                  84
   SetCanonOrder, 58
                                           OEConfGen:: OEOmegaForceFieldType:: SAGE,
   SetEnumNitrogen, 58
                                                  84
   SetEnumRing, 58
                                           OEConfGen::OEOmegaForceFieldType::SAGE_NOESTAT,
   SetFragBuilderMode, 59
                                                  84
   SetFragBuilderOptions, 59
                                           OEConfGen::OEOmegaForceFieldType::SAGE_SHEFF,
   SetFromCT.59
                                                  84
   SetIgnoreStereo, 59
                                           OEConfGen:: OEOmegaGetArch, 94
   SetMaxEnumConfs, 59
                                           OEConfGen:: OEOmegaGetLibraryRelease, 94
   SetSampleHydrogens, 59
                                           OEConfGen:: OEOmegaGetLibraryVersion, 94
   SetStrictAtomTypes, 60
                                           OEConfGen:: OEOmegaGetLicensee, 94
OEConfGen:: OENitrogenEnumeration, 83
                                           OEConfGen:: OEOmegaGetPlatform, 94
OEConfGen:: OENitrogenEnumeration:: All,
                                           OEConfGen:: OEOmegaGetRelease, 95
       83
                                           OEConfGen:: OEOmegaGetSite, 95
OEConfGen::OENitrogenEnumeration::DefaulOEConfGen::OEOmegaGetVersion, 95
                                           OEConfGen:: OEOmegaIsGPUReady, 95
       83
OEConfGen:: OENitrogenEnumeration:: Off,
                                           OEConfGen:: OEOmegaIsLicensed, 95
                                           OEConfGen:: OEOmegaOptions, 61
       83
OEConfGen:: OENitrogenEnumeration:: Unspecifi@dnstructors, 62
       84
                                               GetConfFixOptions, 62
OEConfGen:: OEOmega, 60
                                               GetEnergyWindow, 63
   AddFragLib, 60
                                               GetIncludeInput. 63
   Build, 61
                                               GetMaxConfs, 63
   ClearFragLibs, 61
                                               GetMolBuilderOptions, 63
   Constructors, 60
                                               GetSliceEnsembleOptions, 63
   GetOptions, 61
                                               GetStrictStereo, 63
   operator=, 60
                                               GetTorDriveOptions, 63
   SetOptions, 61
                                               GetTorsionDrive, 64
OEConfGen:: OEOmegaForceFieldType, 84
                                               GetWarts, 64
OEConfGen::OEOmegaForceFieldType::Invalid, operator=, 62
       86
                                               SetConfFixOptions, 64
OEConfGen:: OEOmegaForceFieldType:: MMFF,
                                               SetEnergyWindow, 64
                                               SetIncludeInput, 64
       84
OEConfGen::OEOmegaForceFieldType::MMFF94S,
                                               SetMaxConfs, 64
                                               SetMolBuilderOptions, 65
       85
OEConfGen::OEOmegaForceFieldType::MMFF94S_NOECLEAL.ceEnsembleOptions, 65
                                               SetStrictStereo. 65
       85
OEConfGen::OEOmegaForceFieldType::MMFF94S_SHERET,orDriveOptions, 65
                                               SetTorsionDrive, 65
       85
OEConfGen::OEOmegaForceFieldType::MMFF94S_TEMMMQarts, 65
                                           OEConfGen:: OEOmegaReturnCode, 86
       85
OEConfGen::OEOmegaForceFieldType::MMFF940m6dnfGen::OEOmegaReturnCode::ExceedsAtomDegree4,
       85
                                                  87
```

OEConfGen::OEOmegaReturnCode::ExplicitHydrogensQ0 86 OEConfGen::OESliceEnsembleDefaults::MaxConfs, OEConfGen:: OEOmegaReturnCode:: Failed,  $90$ OEConfGen:: OESliceEnsembleDefaults:: RMS, 88 OEConfGen::OEOmegaReturnCode::FailedCharges, 90 OEConfGen::OESliceEnsembleOptions, 67 88 OEConfGen:: OEOmegaReturnCode:: FailedCTBuild,Constructors, 68 87 GetEnergyRange, 68 OEConfGen::OEOmegaReturnCode::FailedDGConfG@metEnergyWindow, 68 87 GetMaxConfRange, 68 OEConfGen::OEOmegaReturnCode::FailedDupSetußetMaxConfs, 68 87 GetMaxTerminalHeavy, 69 OEConfGen::OEOmegaReturnCode::FailedFixMatc&etRangeIncrement, 69 88 GetRMSRange, 69 OEConfGen::OEOmegaReturnCode::FailedSmartMatGelt,RMSThreshold, 69 operator=, 68 88 OEConfGen::OEOmegaReturnCode::FailedTorAssi@metEnergyRange, 69 87 SetEnergyWindow, 69 OEConfGen::OEOmegaReturnCode::FailedTorDriv&etMaxConfRange, 70 87 SetMaxConfs, 69 OEConfGen::OEOmegaReturnCode::InvalidOption SetMaxTerminalHeavy, 70 SetRangeIncrement, 70 86 OEConfGen::OEOmegaReturnCode::MissingFFParanSetRMSRange, 70 SetRMSThreshold, 70 86 OEConfGen::OEOmegaReturnCode::No3DFromCTQEConfGen::OEThompsonOptions, 97 86 Constructors, 97 OEConfGen:: OEOmegaReturnCode:: No3DTorDrive, GetBatchMaxRotors, 98 GetMaxTrials, 98 88 OEConfGen::OEOmegaReturnCode::NoFixedFragmerLetMaxTrialsRange, 98 GetPriorTemperature, 98 88 OEConfGen::OEOmegaReturnCode::NoValidConfs. GetTrialsRangeIncrement.98 88 operator=, 98 OEConfGen:: OEOmegaReturnCode:: Success, SetBatchMaxRotors, 99 86 SetMaxTrials, 98 OEConfGen::OEOmegaReturnCode::TooManyRotors,SetMaxTrialsRange.99 SetPriorTemperature, 99 87 OEConfGen::OEOmegaReturnCode::UnspecifiedSteetaTrialsRangeIncrement, 99 87 OEConfGen::OETorDriveOptions, 70 OEConfGen:: OEOmegaSampling, 88 Constructors, 71 OEConfGen:: OEOmegaSampling:: Classic, 89 ExceedsMaxRotors, 72 OEConfGen::OEOmegaSampling::Dense, 89 GetCommentEnergy, 72 OEConfGen:: OEOmegaSampling:: FastROCS, GetForceField, 72 89 GetMaxRotors, 72 OEConfGen:: OEOmegaSampling:: Pose, 89 GetMaxSearchTime, 72 OEConfGen:: OEOmegaSampling:: ROCS, 89 GetRotorOffset, 72 OEConfGen:: OEOmegaSystemHasGPU, 96 GetRotorPredicate, 72 OEConfGen:: OERingFragOptions, 66 GetSDEnergy, 73 Constructors, 67 GetThompsonOptions, 73 GetStartFactor, 67 GetTorLib.73 operator= $, 67$ GetUseGPU, 73 SetStartFactor, 67 GetUseThompson, 73 OEConfGen::OESliceEnsemble, 96 operator=, 71 OEConfGen::OESliceEnsembleDefaults, 90 SetCommentEnergy, 73 OEConfGen::OESliceEnsembleDefaults::EWindow,SetForceField, 73

SetMaxRotors, 74 SetMaxSearchTime.74 SetRotorOffset, 74 SetRotorPredicate, 74 SetSDEnergy, 74 SetThompsonOptions, 74 SetTorLib. 75 SetUseGPU, 75 SetUseThompson, 75 OEConfGen::OETorDriver, 75 Constructors, 76 GenerateConfs, 76 GetForceField, 76 GetSliceEnsembleOptions, 76 GetTorDriveOptions, 77 operator=, 76 SetForceField, 77 SetSliceEnsembleOptions, 77 SetTorDriveOptions, 77 OEConfGen:: OETorLib, 77 AddTorsionLibrary, 78 AddTorsionRule, 78 ClearTorsionLibrary, 79 Constructors. 78 GetTorRule, 79 GetTorRules. 80 HasTorRule, 80 operator bool, 78 ResetTorsionLibrary, 80 SetTorsionLibrary, 80 OEConfGen:: OETorLibParameter, 80 Constructors, 81 operator=, 82 OEConfGen:: OETorLibType, 90 OEConfGen::OETorLibType::Default.91 OEConfGen::OETorLibType::GubaV21,91 OEConfGen::OETorLibType::Original, 91 OEConfGen:: Suboption Parameter Defaults, 66 operator bool OEConfGen:: OETorLib, 78 operator= OEConfGen:: OEConfFixOptions, 23 OEConfGen:: OEConformerBuilder, 29 OEConfGen:: OEConfSlicer, 29 OEConfGen::OEFlipperClassicOptions, 31 OEConfGen:: OEFlipperOptions, 35 OEConfGen::OEFragBuilder, 40 OEConfGen:: OEFragBuilderOptions, 42 OEConfGen:: OEFragOptions, 44 OEConfGen:: OEMacrocycleBuilder, 46 OEConfGen:: OEMacrocycleBuilderOptions, 48

OEConfGen:: OEMacrocycleOmega, 49 OEConfGen::OEMacrocycleOmegaOptions, 51 OEConfGen:: OEMakeFragLib, 53 OEConfGen:: OEMolBuilder, 55 OEConfGen:: OEMolBuilderOptions, 57 OEConfGen:: OEOmega, 60 OEConfGen:: OEOmegaOptions, 62 OEConfGen:: OERingFragOptions, 67 OEConfGen::OESliceEnsembleOptions, 68 OEConfGen:: OEThompsonOptions, 98 OEConfGen::OETorDriveOptions, 71 OEConfGen:: OETorDriver, 76 OEConfGen:: OETorLibParameter, 82

# P

Prep OEConfGen:: OEMolBuilder, 55

# R

ResetTorsionLibrary OEConfGen:: OETorLib, 80

# S

SetAtomExpr OEConfGen:: OEConfFixOptions, 26 SetAtomPredicate OEConfGen::OEFlipperClassicOptions, 32 OEConfGen:: OEFlipperOptions, 37 SetBatchMaxRotors OEConfGen:: OEThompsonOptions, 99 SetBondExpr OEConfGen:: OEConfFixOptions, 26 SetBondPredicate OEConfGen::OEFlipperClassicOptions, 32 OEConfGen:: OEFlipperOptions, 37 SetCanonOrder OEConfGen:: OEMolBuilderOptions, 58 SetCommentEnergy OEConfGen:: OETorDriveOptions, 73 SetConfFixOptions OEConfGen:: OEOmegaOptions, 64 SetDielectricConst OEConfGen:: OEMacrocycleBuilderOptions, 48 SetEnergyRange OEConfGen::OESliceEnsembleOptions, 69 SetEnergyWindow OEConfGen:: OEFragOptions, 45

OEConfGen::OEMacrocycleOmegaOptions, SetFixSmarts 52 OEConfGen:: OEOmegaOptions, 64 OEConfGen::OESliceEnsembleOptions, 69 SetEnhancedStereo OEConfGen::OEFlipperClassicOptions, 32 OEConfGen:: OEFlipperOptions, 37 SetEnumAtoms OEConfGen:: OEFlipperOptions, 38 SetEnumAtomSpecifiedStereo OEConfGen:: OEFlipperOptions, 38 SetEnumBonds OEConfGen:: OEFlipperOptions, 38 SetEnumBondSpecifiedStereo OEConfGen::OEFlipperOptions, 38 SetEnumBridgehead OEConfGen::OEFlipperClassicOptions, 33 OEConfGen:: OEFlipperOptions, 39 SetEnumEZ OEConfGen::OEFlipperClassicOptions, 33 OEConfGen:: OEFlipperOptions, 39 SetEnumNitrogen OEConfGen:: OEFlipperClassicOptions, 33 OEConfGen:: OEFlipperOptions, 39 OEConfGen:: OEMolBuilderOptions, 58 SetEnumRelativeAtomStereo OEConfGen:: OEFlipperOptions, 39 SetEnumRing OEConfGen:: OEMolBuilderOptions, 58 SetEnumRS OEConfGen::OEFlipperClassicOptions, 33 OEConfGen:: OEFlipperOptions, 39 SetEnumSpecifiedStereo OEConfGen::OEFlipperClassicOptions, 34 OEConfGen:: OEFlipperOptions, 39 SetFixDeleteH OEConfGen:: OEConfFixOptions, 26 SetFixMaxMatch OEConfGen:: OEConfFixOptions, 26 SetFixMCS OEConfGen:: OEConfFixOptions, 27 SetFixMol OEConfGen:: OEConfFixOptions, 26 SetFixPredicate OEConfGen:: OEConfFixOptions, 27 SetFixRMS OEConfGen:: OEConfFixOptions, 27

OEConfGen:: OEConfFixOptions, 27 SetFixSubSearch OEConfGen:: OEConfFixOptions, 27 SetFixUniqueMatch OEConfGen:: OEConfFixOptions, 27 SetForceField OEConfGen:: OEFragBuilderOptions, 43 OEConfGen:: OETorDriveOptions, 73 OEConfGen:: OETorDriver, 77 SetFragBuilderMode OEConfGen:: OEMolBuilderOptions, 59 SetFragBuilderOptions OEConfGen:: OEMolBuilderOptions, 59 SetFragGen OEConfGen:: OEFragOptions, 45 SetFraqKeep OEConfGen:: OEFragOptions, 45 SetFromCT OEConfGen:: OEMolBuilderOptions, 59 SetIqnoreStereo OEConfGen:: OEMolBuilderOptions, 59 SetIncludeInput OEConfGen:: OEOmegaOptions, 64 SetIterCycleSize OEConfGen::OEMacrocycleOmegaOptions, 52 SetMacrocycleBuilderOptions OEConfGen::OEMacrocycleOmegaOptions, 52 SetMacroCycOptions OEConfGen:: OEFragBuilderOptions, 43 SetMaxCenters OEConfGen::OEFlipperClassicOptions, 34 OEConfGen:: OEFlipperOptions, 40 SetMaxConfRange OEConfGen::OESliceEnsembleOptions, 70 SetMaxConfs OEConfGen::OEMacrocycleOmegaOptions, 52 OEConfGen:: OEOmegaOptions, 64 OEConfGen::OESliceEnsembleOptions, 69 SetMaxEnumConfs OEConfGen:: OEMolBuilderOptions, 59 SetMaxIter OEConfGen::OEMacrocycleOmegaOptions, 52 SetMaxRotors OEConfGen:: OETorDriveOptions, 74 SetMaxSearchTime OEConfGen::OETorDriveOptions, 74

SetMaxTerminalHeavy OEConfGen::OESliceEnsembleOptions,  $70$ SetMaxTrials OEConfGen:: OEThompsonOptions, 98 SetMaxTrialsRange OEConfGen:: OEThompsonOptions, 99 SetMCSFunc OEConfGen:: OEConfFixOptions, 28 SetMCSMinAtoms OEConfGen:: OEConfFixOptions, 28 SetMCSType OEConfGen:: OEConfFixOptions, 28 SetMolBuilderOptions OEConfGen:: OEOmegaOptions, 65 SetNonRingOptions OEConfGen:: OEFragBuilderOptions, 43 SetOptions OEConfGen:: OEFragBuilder, 41 OEConfGen:: OEMacrocycleBuilder, 47 OEConfGen:: OEMacrocycleOmega, 50 OEConfGen:: OEMolBuilder, 56 OEConfGen:: OEOmega, 61 SetPriorTemperature OEConfGen:: OEThompsonOptions, 99 SetRandomSeed OEConfGen::OEMacrocycleBuilderOptionsSetTrialsRangeIncrement 48 SetRangeIncrement OEConfGen:: OESliceEnsembleOptions, 70 SetRefTolerance OEConfGen::OEMacrocycleBuilderOptions\$etWarts 49 SetRingOptions OEConfGen:: OEFragBuilderOptions, 43 SetRMS OEConfGen:: OEFragOptions, 45 SetRMSRange OEConfGen::OESliceEnsembleOptions, 70 SetRMSThreshold OEConfGen::OESliceEnsembleOptions, 70 SetRotorOffset OEConfGen::OETorDriveOptions, 74 SetRotorPredicate OEConfGen:: OETorDriveOptions, 74 SetSampleHydrogens OEConfGen:: OEMolBuilderOptions, 59 SetSDEnergy OEConfGen:: OETorDriveOptions, 74 SetSkipRefinement

OEConfGen::OEMacrocycleBuilderOptions, 49 SetSliceEnsembleOptions OEConfGen:: OEMacrocycleOmegaOptions, 53 OEConfGen:: OEOmegaOptions, 65 OEConfGen:: OETorDriver.77 SetStartFactor OEConfGen:: OERingFragOptions, 67 SetStrictAtomTypes OEConfGen:: OEMolBuilderOptions, 60 SetStrictStereo OEConfGen:: OEOmegaOptions, 65 SetThompsonOptions OEConfGen:: OETorDriveOptions, 74 SetTimeLimit OEConfGen:: OEFragOptions, 45 SetTorDriveOptions OEConfGen:: OEOmegaOptions, 65 OEConfGen:: OETorDriver, 77 SetTorLib OEConfGen:: OETorDriveOptions, 75 SetTorsionDrive OEConfGen:: OEOmegaOptions, 65 SetTorsionLibrary OEConfGen:: OETorLib, 80 OEConfGen:: OEThompsonOptions, 99 SetUseGPU OEConfGen:: OETorDriveOptions, 75 SetUseThompson OEConfGen::OETorDriveOptions, 75 OEConfGen:: OEFlipperClassicOptions, 34 OEConfGen:: OEFlipperOptions, 40 OEConfGen:: OEOmegaOptions, 65 simple\_omega.py Example Code, 9 single\_conf\_macrocycle.py Example Code, 19 single\_conformer.py Example Code, 11 Slice OEConfGen::OEConfSlicer, 30 stereo\_and\_torsion.py Example Code, 14

# Т

torsion\_drive.py Example Code, 15