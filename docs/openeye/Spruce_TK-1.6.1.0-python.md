![](_page_0_Picture_0.jpeg)

**Spruce TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| Section                                                                         | Page |
|---------------------------------------------------------------------------------|------|
| 1 Introduction                                                                  | 3    |
| 2 Theory                                                                        | 5    |
| 2.1 Definitions                                                                 | 6    |
| 2.2 Biological Unit                                                             | 6    |
| 2.3 Design Unit                                                                 | 7    |
| 2.4 Proton Placement and Optimization                                           | 7    |
| 2.5 Protein Sidechain Modeling                                                  | 8    |
| 2.6 Protein Loop Modeling                                                       | 8    |
| 2.7 Protein Superposition                                                       | 9    |
| 2.8 How to Correctly Read a PDB File                                            | 9    |
| 3 Iridium                                                                       | 11   |
| 3.1 Categorization                                                              | 12   |
| 4 Examples                                                                      | 14   |
| 4.1 Spruce TK Examples                                                          | 15   |
| 4.1.1 Creating OEDesignUnits from a PDB file                                    | 16   |
| 4.1.2 Creating apo OEDesignUnits from a PDB file                                | 19   |
| 4.1.3 Creating mmcif file from an input DU                                      | 22   |
| 4.1.4 Calculating superposition                                                 | 23   |
| 4.1.5 Extracting Biounits from PDB header remarks                               | 27   |
| 4.1.6 Extracting Biounits by aligning to a reference protein                    | 29   |
| 4.1.7 Finding pockets and their properties (like, Surface Area) from a PDB file | 31   |
| 4.1.8 Write a metadata JSON file from a FASTA file                              | 34   |
| 5 OESpruce API                                                                  | 35   |
| 5.1 OESpruce Classes                                                            | 35   |
| 5.1.1 OEBioUnitExtractionOptions                                                | 35   |
| 5.1.2 OECapBuilderOptions                                                       | 37   |
| 5.1.3 OEDesignUnitBuildOptions                                                  | 39   |
| 5.1.4 OEDesignUnitEnumerateSitesOptions                                         | 41   |
| 5.1.5 OEDesignUnitMutationOptions                                               | 44   |
| 5.1.6 OEDesignUnitPrepOptions                                                   | 45   |
| 5.1.7 OEDesignUnitSplitOptions                                                  | 48   |
| 5.1.8 OEHeterogenMetadata                                                       | 53   |
| 5.1.9 OEIsModeledAtom                                                           | 55   |
| 5.1.10 OELoopBuilderOptions                                                     | 56   |
| 5.1.11 OEMakeDesignUnitOptions                                                  | 63   |
| 5.1.12 OEPocket                                                                 | 66   |

| Section | Title                             | Page |
|---------|-----------------------------------|------|
| 5.1.13  | OEPocketOptions                   | 6    |
| 5.1.14  | OEProtonateDesignUnitOptions      | 6    |
| 5.1.15  | OESidechainBuilderOptions         | 7    |
| 5.1.16  | OESequenceMetadata                | 7    |
| 5.1.17  | OEStructureMetadata               | 7    |
| 5.1.18  | OESecondaryStructureSuperposition | 8    |
| 5.1.19  | OESpruceFilter                    | 8    |
| 5.1.20  | OESpruceFilterOptions             | 8    |
| 5.1.21  | OEStructuralSuperposition         | 8    |
| 5.1.22  | OESuperpositionOptions            | 8    |
| 5.1.23  | OESuperpose                       | 9    |
| 5.1.24  | OESuperposeOptions                | 9    |
| 5.1.25  | GetMethod                         | 9    |
| 5.1.26  | SetMethod                         | 9    |
| 5.1.27  | GetUseConstraints                 | 9    |
| 5.1.28  | SetUseConstraints                 | 9    |
| 5.1.29  | GetValidRMSD                      | 9    |
| 5.1.30  | SetValidRMSD                      | 9    |
| 5.1.31  | GetValidTanimoto                  | 9    |
| 5.1.32  | SetValidTanimoto                  | 9    |
| 5.1.33  | GetValidSeqScore                  | 9    |
| 5.1.34  | SetValidSeqScore                  | 9    |
| 5.1.35  | OESuperposeResults                | 9    |
| 5.1.36  | OEValidateDesignUnit              | 10   |
| 5.2     | OESpruce Constants                | 10   |
| 5.2.1   | OEAlternateLocationOption         | 10   |
| 5.2.2   | OEDesignUnitIssueCodes            | 10   |
| 5.2.3   | OEExperimentType                  | 10   |
| 5.2.4   | OEHeterogenType                   | 10   |
| 5.2.5   | OESuperpositionType               | 10   |
| 5.2.6   | OESpruceFilterIssueCodes          | 10   |
| 5.2.7   | OESuperposeMethod                 | 11   |
| 5.3     | OESpruce Functions                | 11   |
| 5.3.1   | OEBuildLoops                      | 11   |
| 5.3.2   | OEBuildSidechains                 | 11   |
| 5.3.3   | OEBuildSingleLoop                 | 11   |
| 5.3.4   | OECapCTermini                     | 11   |
| 5.3.5   | OECapNTermini                     | 11   |
| 5.3.6   | OECapTermini                      | 11   |
| 5.3.7   | OEEnumerateSites                  | 11   |
| 5.3.8   | OEExtractBioUnits                 | 11   |
| 5.3.9   | OEFindPockets                     | 11   |
| 5.3.10  | OEFixBackbone                     | 11   |
| 5.3.11  | OEGetAlternateLocationOptionID    | 11   |
| 5.3.12  | OEGetAlternateLocationOptionName  | 11   |
| 5.3.13  | OEGetExperimentTypeID             | 12   |
| 5.3.14  | OEGetExperimentTypeName           | 12   |
| 5.3.15  | OEGetHeterogenTypeID              | 12   |
| 5.3.16  | OEGetHeterogenTypeName            | 12   |
| 5.3.17  | OEGetPartialResidues              | 12   |
| 5.3.18  | OEMakeBioDesignUnits              | 12   |
| 5.3.19  | OEMakeDesignUnit                  | 12   |
| 5.3.20  | OEMakeDesignUnits                 | 12   |
| 5.3.21  | OEMakeDesignUnitFromPocket        | 12   |

| Section | Title                         | Page |
|---------|-------------------------------|------|
| 5.3.22  | OEMutateResidue               | 12   |
| 5.3.23  | OEMutateResidues              | 12   |
| 5.3.24  | OEProtonateDesignUnit         | 12   |
| 5.3.25  | OESetPackingResidueProperties | 12   |
| 5.3.26  | OESpruceGetArch               | 12   |
| 5.3.27  | OESpruceGetLicensee           | 12   |
| 5.3.28  | OESpruceGetPlatform           | 12   |
| 5.3.29  | OESpruceGetRelease            | 12   |
| 5.3.30  | OESpruceGetSite               | 12   |
| 5.3.31  | OESpruceGetVersion            | 12   |
| 5.3.32  | OESpruceIsLicensed            | 12   |
| 5.3.33  | OEGetSuperposeMethodFromName  | 12   |
| 5.3.34  | OEGetSuperposeMethodName      | 12   |
| 6       | Release History               | 12   |
| 6.1     | Spruce TK 1.6.1               | 12   |
| 6.1.1   | New features                  | 12   |
| 6.1.2   | Major bug fixes               | 12   |
| 6.1.3   | Minor bug fixes               | 12   |
| 6.1.4   | Documentation changes         | 12   |
| 6.2     | Spruce TK 1.6.0               | 13   |
| 6.2.1   | New features                  | 13   |
| 6.2.2   | Major bug fixes               | 13   |
| 6.2.3   | Minor bug fixes               | 13   |
| 6.2.4   | Documentation changes         | 13   |
| 6.3     | Spruce TK 1.5.3               | 13   |
| 6.3.1   | New features                  | 13   |
| 6.3.2   | Major bug fixes               | 13   |
| 6.3.3   | Minor bug fixes               | 13   |
| 6.4     | Spruce TK 1.5.2               | 13   |
| 6.4.1   | New features                  | 13   |
| 6.4.2   | Major bug fixes               | 13   |
| 6.4.3   | Minor bug fixes               | 13   |
| 6.4.4   | Documentation changes         | 13   |
| 6.5     | Spruce TK 1.5.1               | 13   |
| 6.5.1   | New features                  | 13   |
| 6.5.2   | Major bug fixes               | 13   |
| 6.6     | Spruce TK 1.5.0               | 13   |
| 6.6.1   | New features                  | 13   |
| 6.6.2   | Major bug fixes               | 13   |
| 6.6.3   | Minor bug fixes               | 13   |
| 6.7     | Spruce TK 1.4.0               | 13   |
| 6.7.1   | New features                  | 13   |
| 6.7.2   | Major bug fixes               | 13   |
| 6.7.3   | Minor bug fixes               | 13   |
| 6.8     | Spruce TK 1.3.0               | 13   |
| 6.8.1   | New features                  | 13   |
| 6.8.2   | Minor bug fixes               | 13   |
| 6.8.3   | Documentation changes         | 13   |
| 6.9     | Spruce TK 1.2.0               | 13   |
| 6.9.1   | New features                  | 13   |
| 6.9.2   | Major bug fixes               | 13   |
| 6.9.3   | Minor bug fixes               | 13   |

| Section | Title                           | Page |
|---------|---------------------------------|------|
| 6.10.1  | New features                    | 133  |
| 6.10.2  | Major bug fixes                 | 133  |
| 6.10.3  | Minor bug fixes                 | 137  |
| 6.10.4  | Documentation changes           | 138  |
| 6.11    | Spruce TK 1.0.0                 | 138  |
| 6.11.1  | New features                    | 138  |
| 6.11.2  | Major bug fixes                 | 138  |
| 6.11.3  | Minor bug fixes                 | 138  |
| 6.11.4  | Documentation changes           | 138  |
| 6.12    | Spruce TK 0.9.2                 | 139  |
| 6.12.1  | New features                    | 139  |
| 6.12.2  | Major bug fixes                 | 140  |
| 6.12.3  | Minor bug fixes                 | 140  |
| 6.13    | Spruce TK 0.9.1                 | 140  |
| 6.13.1  | New features                    | 140  |
| 6.13.2  | API changes                     | 140  |
| 6.13.3  | Major bug fixes                 | 141  |
| 6.13.4  | Minor bug fixes                 | 141  |
| 6.14    | Spruce TK 0.9.0                 | 142  |
| 6.14.1  | New features                    | 142  |
| 7       | <b>Copyright and Trademarks</b> | 143  |
| 8       | <b>Sample Code</b>              | 145  |
| 9       | <b>Citation</b>                 | 147  |
| 9.1     | Orion ® Floes                   | 147  |
| 9.2     | Toolkits and Applications       | 148  |
| 9.3     | OpenEye Web Services            | 149  |
| 10      | <b>Technology Licensing</b>     | 151  |
| 10.1    | GCC                             | 166  |
| 10.1.1  | GCC RUNTIME LIBRARY EXCEPTION   | 166  |
| 10.1.2  | GNU GENERAL PUBLIC LICENSE      | 167  |
|         | <b>Index</b>                    | 181  |

Attention: Spruce TK is currently only available in C++ and Python.

# **ONE**

# **INTRODUCTION**

OESpruce TK provides functionalities to prepare biomolecules (that is, proteins and nucleic acids) for modeling tasks.

# **THEORY**

**Spruce TK** is used to process PDB or mmCIF files containing the structures, resulting from X-ray crystallography, Nuclear Magnetic Resonance (NMR) spectroscopy, or electron microscopy (EM) experiments. into molecules usable for molecular modeling. Due to the nature of the experiments and data, some processing is required before use in modeling.

**Spruce TK** provides an end-to-end preparation workflow using the  $OEMakeDesignUnits$  API. Options (see  $OE$ -MakeDesignUnitOptions and associated options classes) are available to control for the desired behavior. Metadata (see OEStructureMetadata) can be supplied to infuse experimental data, like the proper variant sequence and also fix common problems reading from PDB files (e.g. bond order perception). Spruce has a built-in Chemical Components Dictionary matching 3-letter residue codes to SMILES, derived from the corresponding one at the RCSB, but curated to fix improper SMILES. The workflow automatically runs through the following steps to produce OEDesignUnit objects:

- 1. Biological unit extraction (see  $OEExt \text{ractB}$ ioUnits)
- 2. If structure is from X-ray, it will also generate packing residues for visualization of crystal contacts
- 3. Alternate location assignment or enumeration (see the OEAlternateLocationOption namespace)
- 4. Splits the system into components, e.g. identifying ligands, cofactors, excipients.
- 5. Building missing side-chains, modeling loops, and capping chain breaks (see OEBuildSidechains, OEBuildLoops, and OECapTermini)
- including 6. Hydrogen placement and optimization, searching ligand tautomer states (see OEProtonateDesignUnit)
- 7. Assignment of partial charges to the entire system (see OEDesignUnitCharges)
- 8. Superposition to a common reference frame (see OEStructuralSuperposition and OESecondaryStructureSuper*position*)
- 9. An OEInteractionHintContainer encoded for visualization and more
- 10. An estimate of the model quality using Iridium [Warren-2012] stored in OEIridiumData.

Note: Multiple design units are often produced. This results from multiple biological units generated during step 1, and further expanding that set when enumerating the alternate locations in step 3. The Iridium categorization (see Categorization) should be helpful in choosing which (if not all) of the produced units to use in downstream modeling tasks. We find that the Iridium categories are also helpful for managing modeling expectations, having a quality measure of the input data for modeling.

Note: Included with Spruce TK is a large database of loop templates generated by parsing the structures in the public PDB repository pulled from the RCSB. This database is available from db-downloads. in a platform-independent format. The SPRUCE loop database is large  $(\sim 13G)$  and will take time to download with a good internet connection. When the download is complete, move the file to a convenient location, a network drive is not recommended for performance.

To use it during prep (OEMakeDesignUnits), set the path in SetLoopDBFilename method on the OELoopBuilderOptions class.

The database can be appended to (updated) using the **LoopDB** Builder utility app, that ships with the **SPRUCE** apps. This would be in the event that the user has a collection of internal/proprietary structures, or if specific structures are released to the public PDB between OpenEye updates of the database that are crucial for a given target that is less well described by the existing templates.

# **2.1 Definitions**

- 1. Biological Unit (BU) the biologically relevant unit for a protein to use in modeling. For example, in Trypsin the BU is a monomer, in HIV Protease the BU is a homo-dimer. See *Biological Unit* below.
- 2. Asymmetric Unit (ASU) the contents of a PDB or mmCIF file from X-ray contain an asymmetric unit as the output of the experiment. This is sometimes equivalent to the BU, but often requires manipulation to create a correct BU.
- 3. Design Unit (DU) the result of preparation in Spruce is a collection of molecules from a single BU, extracted and ready to use for modeling tasks. See *Design Unit* below for more details.
- 4. Alternate locations (alt locs) X-ray experiments can often contain results with atoms occupying more than one location. Crystallographers denote this with a measure of the amount of time an atom occupies a given set of coordinates. A well resolved atom will have an occupancy of 1.0, meaning that  $100\%$  of the time it is in that location. Sometimes, the atom exists in two positions, alternate locations, and these appear in the input file with single letter designations and with occupancy  $< 1.0$ .

# 2.2 Biological Unit

In short, the biological unit (BU) is an object that contains the biologically relevant parts of an ASU, which have not been split into various molecular components and are not yet prepped for modeling. For a more detailed explanation of BUs, refer to Introduction to Biological Assemblies and the PDB Archive hosted at the RCSB.

A BU can be constructed from a single PDB from the PDB's own header remarks, or by using a sequence alignment to an input reference protein. To extract a BU or set of BUs from a PDB, one should use the helper function in **Spruce TK** called OEExtractBioUnits. The following example shows how to extract BUs from the PDB remarks:

biounits = oespruce.OEExtractBioUnits(extract\_prot, opts)

Using the same function, one can also extract BUs from a PDB using an input reference protein. The following example shows how to use  $OEExtracBioUnits$  to extract BUs from a given reference:

biounits = oespruce. OEExtractBioUnits (extract\_prot, ref\_prot, opts)

# 2.3 Design Unit

The design unit (DU) is an object that contains the extracted and prepared parts of a single BU, ready for modeling. The parts include:

- 1. Protein
- 2. Ligand (not always, an apo DU will not contain a ligand)
- 3. Site residues
- 4. Packing residues (if any exist near the site)
- 5. Excipients (if any exist near the site)

One can interact with each part of the DU through APIs. The APIs are listed here OEDesignUnit.

# 2.4 Proton Placement and Optimization

Traditionally, most biomolecular structures have been generated with either no explicit hydrogens or only polar hydrogens. However, having all atoms explicitly represented and positioned to make appropriate hydrogen bonds is sometimes necessary. The function OEP LaceHydrogens does this by adding and placing hydrogens and by "flipping" certain functional groups (e.g., sidechain amides and imidazoles) as required for an optimal hydrogen bonding network. **Spruce TK** leverages this functionality, but builds on top of this by taking the ligand protomer and tautomer states into account in the OEProtonateDesignUnit function. The function identifies the heterogens (ligands, cofactors, etc.) in the structure and enumerates their states using the OEGetReasonableTautomers function or by using user supplied states. The hydrogen bonding network of the biomolecule is then optimized in the presence of each state independently and the most favorable state of the complex is chosen based on interaction energies. If a binding site holds two heterogens, e.g. a ligand and a cofactor and each have multiple tautomer states, the combinatorial number of states are optimized and evaluated. To do this efficiently only the binding site(s) are initially optimized. After selecting the appropriate states of each of the binding sites the remaining parts of the system is optimized keeping these states fixed.

# 2.5 Protein Sidechain Modeling

Amino acid sidechains are sometimes missing in protein structures due to low or missing density from X-ray diffraction crystallography experiments. This can be due to e.g. high flexibility making assignment of a specific location of the atoms difficult. However, most molecule simulation software requires a position of these atoms, and the lack of them can cause incorrect results. Partial sidechains are identified with OEGetPartialResidues. Using OEBuildSidechains these residues are then divided into groups based on proximity and side-chain orientation. The groups are independently optimized taking into account their local environment. In each group the sidechains are built out and a standard rotamer library from the OERotamerLibrary namespace is used. For each side-chain the set of rotamers are evaluated based on an interaction energy with the nearest environment and the most favorable state is chosen. In the case where multiple residues are being built in a group, an iterative procedure attempts to find the optimal energy for the entire set of residues. In the event a sidechain cannot be built due to poor input geometry causing clashes the entire cluster is skipped. Water locations that block side-chain rotamers result in those water molecules being deleted (optional) since their placement is most likely an artifact.

# **2.6 Protein Loop Modeling**

Similarly to missing side-chains above there are sometimes gaps in protein structures, where the position of the entire amino acid residues could not be resolved based on the experimental data. The function  $OEBui1dLoops$  is able to build missing gaps (loops). The workflow is illustrated by the figure below. The function identifies missing loops, by comparing the SEQRES section of the PDB header with the structure using a sequence alignment. The user can optionally input their own sequence using OESequenceMetadata if the SEQRES in the header is incorrect or missing. With the gaps identified, the function loops for templates matching the gap, filters them based on the ability to fit the gap without clashing, and eventually does an optimization of the top candidates in the local environment before picking the most favorable conformation. If multiple results are desired, these can be retrieved using OEBuildSingleLoop.

![](_page_13_Figure_3.jpeg)

Fig. 1: OEBuildLoops: Gaps are searched, filtered, inserted and evaluated for best fit.

The loop template database is built using all the structures in the PDB downloaded from the RCSB, and can be downloaded from db-downloads.

![](_page_13_Figure_6.jpeg)

Fig. 2: Loop template database Loops are extracted from the RCSB PDB, deduplicated, compressed and indexed for easy retrieval.

# **2.7 Protein Superposition**

A protein can be structurally superimposed on to a reference protein structure using the OESpruce TK. Proteins can be superimposed with either atomic coordinates in the OEStructuralSuperposition class, or with secondary structure elements using the OESecondaryStructureSuperposition class.

The OEStructuralSuperposition class can superimpose proteins using any of the following four methods:

- 1. The global method (default for *OEStructuralSuperposition*). This method uses all matching heavy atoms from the reference and fit proteins as the region for performing the superposition calculation (see OESuperpositionType\_Global).
- 2. The Difference Distance Matrix method. This method calculates the pairwise distance matrix of C-alpha atoms for both the reference and fit proteins, then takes the difference of these two matrices to find the difference

distance matrix (DDM).

For a given conformation a, the elements of the distance matrix  $D_{ij}^{\alpha}$  are the distances between atoms *i* and *j* in a molecule.

$$
D_{ij}^a = |r_i - r_j|
$$

where  $r_i$  and  $r_j$  are the Cartesian coordinate vectors of atoms i and j. The elements  $\Delta_{ij}^{ab}$  of the differencedistance matrix for two conformations a and b are

$$
\Delta_{ii}^{ab} = D_{ii}^a - D_{ii}^b
$$

If  $\Delta_{ij}^{ab}$  is positive, the interatomic vector between between *i* and *j* in conformation *b* is contracted with respect to *a*. Conversely, negative elements of the DDM indicate an expansion of the interatomic vector

The longest contiguous region of the resulting difference distance matrix (DDM) is used for the structural superposition calculation (see OESuperpositionType\_DDM).

- 3. The weighted-DDM method. This method uses the DDM matrix, and calculates Gaussian weighting factors for all matching C-alpha atoms. These Gaussian weights are used as a weighting function in the superposition calculation (see OESuperpositionType\_Weighted).
- 4. The site residue method. This method uses a set of site residues (given as a set of unique residue strings) as a constraint on the protein superposition. Site residues must be set with the Set SiteResidues member function of the OESuperpositionOptions class (see OESuperpositionType\_Site).

The OESecondaryStructureSuperposition class can superimpose proteins using the following method:

1. The secondary structure superposition method. This method takes two proteins and performs a structural superposition on them based on the shape overlap of the secondary structure elements of the two proteins.

Note: All structural superposition methods in the OEStructuralSuperposition class have a corresponding score from the sequence alignment that was used to find the matching atoms of both proteins. This score comes from the output of the OESequenceAlignment class, where a larger score indicates a better sequence alignment, and scores below a small threshold (around 200) should be considered a bad alignment.

All structural superposition methods in the OEStructuralSuperposition class have a corresponding RMSD Note: value for superposition that can be loosely associated with the quality of the superposition. The OESecondaryStructureSuperposition class does not have an RMSD value, but instead uses the Tanimoto score from the underlying shape overlap calculation.

# 2.8 How to Correctly Read a PDB File

Reading a PDB file correctly for use in subsequent modeling tasks can be challenging. To correctly read a PDB, one must be aware that PDB header information as well as information about alternate location codes within the PDB file will be lost unless a specific combination of PDB-centric OEIF1avor's are used. Furthermore, the protein itself must be processed by OEAltLocationFactory in order to create a molecule with all alternate location atoms retained. Spruce handles this for the user, so they are not handled by this reader. However, for uses other than Spruce the user needs to either, enumerate the different alternate locations, or pick a specific location. With that in mind, we recommend reading PDB files for use in **OESpruce TK** using the following pattern as shown in **ReadProteinFromPDB** below:

```
if s = oechem.oemolistream()ifs.SetFlavor(oechem.OEFormat_PDB, oechem.OEIFlavor_PDB_Default | oechem.
→OEIFlavor_PDB_DATA | oechem.OEIFlavor_PDB_ALTLOC) # noqa
       if not ifs.open(ifilename):
           oechem. OEThrow. Fatal ("Unable to open %s for reading" % ifilename)
       mol = occhem.OEGraphMol()if not oechem. OEReadMolecule(ifs, mol):
           oechem. OEThrow. Fatal ("Unable to read molecule from \frac{2}{5}" % ifilename)
```

Note: The mmCIF reader was designed to read all the necessary input by default, and therefore no specific OEIFlavor's are necessary to read them.

# **THREE**

# **IRIDIUM**

Iridium [Warren-2012] is a metric used to estimate the model quality of a structure resulting from an X-ray crystallography experiment. The metric evaluates what we deem essential considerations for using protein-ligand structures in drug discovery, particularly virtual screening.

The metric was developed by aggregating previously published docking validation sets, evaluating each of them by eye and even re-refining some of the data. The high quality structures were then deposited into a new dataset called Iridium HT [Warren-2012].

The metric takes a number of parameters into account and categorizes structures into 4 different categories, grading their trustworthiness to use in modeling.

- HT Highly Trustworthy
- MT Mildly Trustworthy
- NT Not Trustworthy
- NA Not Applicable

The latter category is used when no electron density data is available, or when the structure being evaluated is not coming from an X-ray crystallography experiment. Electron density data is available for at least 85% of the public PDB data and is required for all new depositions. Historical data is also being recovered, so that percentage is only expected to increase.

Note: Regarding applicability:

- Iridium is not currently an appropriate metric for electron microscopy (EM) experiments, in part because the contour level, which we use as 1 sigma in X-ray experiments, is determined on a per experiment basis, and also in part due to different diffraction behavior of heavy atoms comparing to the X-ray.
- Iridium is not currently an appropriate metric for neutron diffraction experiments, due to the different diffraction behavior for heavy atoms (e.g. sulfur and phosphorus are largely invisible in neutron diffraction data).
- Iridium relies on a bound ligand, and is therefore not appropriate for apo structures.

# 3.1 Categorization

The initial Iridium categorization was done by eye. The rules developed were then formalized to be able to rigorously assess the Iridium category on every X-ray structure. In some cases the original publication is not explicit about threshold values, but the metric below follows the paper in spirit and is approved by the original authors. The outcome of formalizing the rules, resulted in minor category discrepancies on the published dataset, is likely due to the more stringent adherence to the rules.

The criteria to consider include both global and local quality metrics and are as follows (the acronyms in parentheses, are used when spruce logs the Iridium details):

- DPI The diffraction-component precision index or global precision estimate [Cruickshank-1999]
- Rfree value
- Crystallographic Resolution
- Density coverage of the ligand heavy atoms (LaD)
- Density coverage of the active site residue heavy atoms (including co-factors) (ASaD)
- Occupancy of ligand heavy atoms (POL)
- Occupancy of active site heavy atoms (POAS)
- Alternate locations of the ligand (AltConfs)
- Alternate locations of the active site residues (AltConfs)
- Presence of crystal packing residues near binding site (PackRes)
- Presence of excipients near binding site (Excp)
- Whether ligand is potentially covalently bound, but the covalent bond is not property perceieved (PossCov)

First, the initial consideration is based on the density coverage of the ligand and the active site residues.

|             | HT       | MT                    | NT       |
|-------------|----------|-----------------------|----------|
| Ligand      | $> 0.90$ | $< 0.90$ and $> 0.50$ | $< 0.50$ |
| Active Site | $> 0.95$ | $< 0.95$ and $> 0.50$ | $< 0.50$ |

Subsequently, a structure can be demoted from HT to MT, if any of the conditions below are true:

- DPI  $> 0.50$
- Presence of alternate locations of the ligand or the active site residues
- Any ligand heavy atoms with an occupancy  $< 0.90$
- Any active site heavy atoms with an occupancy  $< 0.50$
- Perception of interactions between packing residues and the ligand using OEPerceiveInteractionOptions with default settings.
- Perception of interactions between any excipient and the ligand using OEPerceiveInteractionOptions with default settings.
- Perception of unperceived covalent interactions of the ligand in the active site using OEPerceiveInteractionOptions with default settings.

Furthermore, any structure will be demoted to NT if the Rfree value is larger than 0.45 and the resolution is below 3.5A, as we consider that an irrational Rfree value (IrrRFree).

Note: Not all structures report a DPI, and in such cases it is calculated using OECalculateDPI.

## See also:

- OEIridiumData class
- · OECalculateDPI class
- · OEDrawIridiumData function in Grapheme TK to visualize OEIridiumData

# **FOUR**

# **EXAMPLES**

# **4.1 Spruce TK Examples**

The following table lists the currently available Spruce TK examples:

| Program                            | Description                                                                                                                  |
|------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <i>make_design_units.py</i>        | constructing design units from a PDB (due to loop modeling this example takes $\sim 10$ min).                                |
| <i>make_apo_design_units</i>       | constructing apo design units from a PDB using a site residue input (due to loop modeling this example takes $\sim 10$ min). |
| <i>du2mmcif.py</i>                 | write an output mmcif file from a spruce generated design unit.                                                              |
| <i>superpose.py</i>                | superposition of two proteins.                                                                                               |
| <i>extract_biounits_remarks.py</i> | extract biounits from PDB header remarks.                                                                                    |
| <i>extract_biounits_ref.py</i>     | extract biounits from a sequence alignment to a reference protein.                                                           |
| <i>findpockets.py</i>              | find pockets and some of its properties from a protein or DesignUnit.                                                        |
| <i>convert_du_to_mmcif</i>         | Writing du to mmcif file                                                                                                     |
| <i>write_metadata_json_file</i>    | Writing a metadata JSON file from a FASTA file                                                                               |

**Examples:** 

# 4.1.1 Creating OEDesignUnits from a PDB file

Preparation of a biological structure file (PDB, mmCIF) to a fully charged, hydrogenated, molecular componentized object (design unit; DU; OEDesignUnit) is one of the more advanced functionalities offered through Spruce TK. This example shows how to construct DUs using an input PDB file and the  $OEMakeDesignUnits$  function.

### **Command Line Interface**

This example uses an input PDB file, and will output a set of DUs from it to a temporary directory (see  $OEMakeDesignUnits$  for details on the API).

```
make_design_units <input biomolecular PDB> [<electron density mtz>] [
-<LoopModelingTemplateDB>]
```

### Code

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
#######################################
# Script to prepare proteins into design units
#######################################
import sys
import os
from openeye import oechem
from openeye import oegrid
from openeye import oespruce
def main (argv=sys.argv) :
   if len(argv) < 2 or len(argv) > 4:
       oechem.OEThrow.Usage("%s <infile> [<mtzfile>] [<loopdbfile>]" % argv[0])
   ifs = oechem.oemolistream()
   ifile = argv[1]if not ifs.open(ifile):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % ifile)
```

```
(continued from previous page)
```

```
include\_loop = Falseinclude\_ed = Falseed = oegrid.OESkewGrid()
   if len(argv) > 2:
       if len(argv) == 4 or (len(argv) == 3 and "mtz" in argv[2]):
            edfile = argv[2]if not oegrid. OEReadMTZ (edfile, ed, oegrid. OEMTZMapType_Fwt) :
                oechem.OEThrow.Fatal(
                    "Unable to read electron density file %s" % edfile
                ) # noqainclude\_ed = Trueif len(argv) == 4:
            loopfile = array[3]include loop = Trueelif len(argv) == 3 and "mtz" not in argv[2]:
            loopfile = argv[2]include\_loop = Trueif ifs.GetFormat() not in [oechem.OEFormat_PDB, oechem.OEFormat_CIF]:
       oechem. OEThrow. Fatal ("Only works for . pdb or . cif input files")
   ifs.SetFlavor(
       oechem.OEFormat_PDB,
       oechem.OEIFlavor_PDB_Default
       | oechem.OEIFlavor_PDB_DATA
       | oechem.OEIFlavor_PDB_ALTLOC,
   ) # noga
   mol = occhem. OEGraphMol()if not oechem. OEReadMolecule(ifs, mol):
       oechem. OEThrow. Fatal ("Unable to read molecule from %s" % ifile)
   allow_filter_errors = False
   metadata = oespruce. OEStructureMetadata()
   filter_opts = oespruce.OESpruceFilterOptions()
   makedu_opts = oespruce.OEMakeDesignUnitOptions()
   makedu_opts.GetPrepOptions().GetBuildOptions().GetLoopBuilderOptions().
\rightarrow SetBuildTails (False)
   if include_loop:
       makedu opts.GetPrepOptions().GetBuildOptions().GetLoopBuilderOptions().
\rightarrowSetLoopDBFilename(
           loopfile
       \lambdafilter = oespruce.OESpruceFilter(filter_opts, makedu_opts)
   ret_filter = filter.StandardizeAndFilter(mol, ed, metadata)
   if ret_filter != oespruce. OESpruceFilterIssueCodes_Success:
       oechem. OEThrow. Warning ("This structure fails spruce filter due to: ")
       oechem.OEThrow.Warning(filter.GetMessages())
       if not allow_filter_errors:
           oechem. OEThrow. Fatal ("This structure fails spruce filter")
   if include ed:
       design\_units = oespruce.OEMakeDesign Units (mol, ed, metadata, makedu_opts)else:
       design_units = oespruce.OEMakeDesignUnits(mol, metadata, makedu_opts)
```

```
validator = oespruce.OEValidateDesignUnit()
   base_name = os.path.basename(ifile) [:-4] + "_DU_{}.oedu"
    for i, design_unit in enumerate(design_units):
        ret_validator = validator.Validate(design_unit, metadata)
        if ret_validator != oespruce.OEDesignUnitIssueCodes_Success:
            oechem. OEThrow. Warning ("This generated DU did not pass DU validator.")
            oechem.OEThrow.Warning(validator.GetMessages())
        oechem.OEWriteDesignUnit(base_name.format(i), design_unit)
if name == " main ":
   sys.exit(main(sys.argy))
```

#### **Example**

make\_design\_units.py 3tpp.pdb 3tpp.mtz spruce\_bace.loop\_db

will generate the following output:

```
DPI: 0.06, RFree: 0.18, Resolution: 1.60
Processing BU # 0 with title: BETA-SECRETASE 1, chains A, alt: A
Warning: For residue ARG -4 A 1 removing clashing solvent molecule HOH 597 A 2
Warning: For residue ARG -4A 1 removing clashing solvent molecule HOH 487 A A 1
Warning: For residue ARG 7 A 1 removing clashing solvent molecule HOH 498 A 2
Warning: For residue ARG 7 A 1 removing clashing solvent molecule HOH 730
                                                                             A<sub>2</sub>Warning: For residue ARG 7 A 1 removing clashing solvent molecule HOH 653 A 2
Warning: For residue ARG 128 A 1 removing clashing solvent molecule HOH 523 A 2
Warning: For residue ARG 128 A 1 removing clashing solvent molecule HOH 654 A 2
Warning: For residue LYS 142 A 1 removing clashing solvent molecule HOH 550 A 2
Warning: For residue LYS 142 A 1 removing clashing solvent molecule HOH 691
                                                                              A 2
Warning: For residue ARG 205 A 1 removing clashing solvent molecule HOH 423
                                                                              A 2
Warning: For residue ARG 205 A 1 removing clashing solvent molecule HOH 703
                                                                              A 2
Warning: For residue LYS 256 A 1
                                   removing clashing solvent molecule HOH 604
                                                                               A 2
Found gap between ALA 157 A 1 and VAL 170 A 1, with sequence GFPLNQSEVLAS
                               and THR 314 A 1, with sequence DVA
Found gap between GLU 310 A 1
Opened database spruce_bace.loop_db
LoopDatabase Info:
   276 loops from RSCB last synced on 03-19-2020, were added to LoopTemplateDatabase
→on 03-19-2020 using Spruce Toolkit 1.0.0.a
   The loop database was built with a max loop length of 22, a termini crop length
\rightarrow of 2, and excluding regular secondary structures
Opened database spruce_bace.loop_db
LoopDatabase Info:
    276 loops from RSCB last synced on 03-19-2020, were added to LoopTemplateDatabase
→on 03-19-2020 using Spruce Toolkit 1.0.0.a
    The loop database was built with a max loop length of 22, a termini crop length
\rightarrow of 2, and excluding regular secondary structures
Processing BU # 1 with title: BETA-SECRETASE 1, chains A, alt: B
Warning: For residue ARG -4 A 1 removing clashing solvent molecule HOH 597 A 2
Warning: For residue ARG -4 A 1 removing clashing solvent molecule HOH 487 A A 1
Warning: For residue LYS 9 A 1 removing clashing solvent molecule HOH 675
                                                                            A 2
Warning: For residue ARG 128 A 1 removing clashing solvent molecule HOH 523 A 2
```

```
Warning: For residue ARG 128 A 1 removing clashing solvent molecule HOH 654
                                                                                    A<sub>2</sub>Warning: For residue LYS 142 A 1 removing clashing solvent molecule HOH 448
                                                                                    A 2
Warning: For residue LYS 142 A 1 removing clashing solvent molecule HOH 735
                                                                                   A<sub>2</sub>Warning: For residue ARG 205 A 1 removing clashing solvent molecule HOH 423
                                                                                    A 2
Warning: For residue ARG 205 A 1 removing clashing solvent molecule HOH 703
                                                                                    A 2
Warning: For residue LYS 256 A 1 removing clashing solvent molecule HOH 604
                                                                                    A 2
Found gap between ALA 157 A 1 and VAL 170 A 1, with sequence GFPLNQSEVLAS
Found gap between GLU 310 A 1 and THR 314 A 1, with sequence DVA
Opened database spruce_bace.loop_db
LoopDatabase Info:
   276 loops from RSCB last synced on 03-19-2020, were added to LoopTemplateDatabase
\rightarrowon 03-19-2020 using Spruce Toolkit 1.0.0.a
   The loop database was built with a max loop length of 22, a termini crop length,
\rightarrow of 2, and excluding regular secondary structures
Opened database spruce bace.loop db
LoopDatabase Info:
    276 loops from RSCB last synced on 03-19-2020, were added to LoopTemplateDatabase
\rightarrowon 03-19-2020 using Spruce Toolkit 1.0.0.a
    The loop database was built with a max loop length of 22, a termini crop length
\rightarrow of 2, and excluding regular secondary structures
DU: BETA-SECRETASE 1(A) altA > 5HA (A-999), Iridium Category: HT, LaD: 1.00, ASaD: 1.00,
\rightarrow DPI: 0.06, POL: false, POAS: false, AltConfs: false, PackRes: false, Excp: false,
→IrrRFree: false, PossCov: false
DU: BETA-SECRETASE 1(A) altB > 5HA (A-999), Iridium Category: HT, LaD: 1.00, ASaD: 1.00,
→ DPI: 0.06, POL: false, POAS: false, AltConfs: false, PackRes: false, Excp: false,
→IrrRFree: false, PossCov: false
Skipping redundant DU with alts outside the site of interest, renaming existing to
\rightarrowcollapse alts
Discarding redundant alt DU with title BETA-SECRETASE 1(A) altB > 5HA (A-999)
```

#### See also:

- · OEMakeDesignUnitsfunction
- OEReadDesignUnit and OEWriteDesignUnit functions in the OEChem TK manual
- OEDesignUnit class in the OEChem TK manual

# 4.1.2 Creating apo OEDesignUnits from a PDB file

Preparation of a biological structure file (PDB, mmCIF) to a fully charged, hydrogenated, molecular componentized object (design unit; DU; OEDesignUnit) is one of the more advanced functionalities offered through Spruce TK. This example shows how to construct apo DUs using an input PDB file and the  $OEMakeDesignUnits$  function.

#### **Command Line Interface**

This example uses an input PDB file, and will output a set of DUs from it to a temporary directory (see OEMakeDesignUnits for details on the API).

```
make_apo_design_units <input biomolecular PDB> <site_residue> [<electron density mtz>
→] <LoopModelingTemplateDB>]
```

#### Code

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
#######################################
# Script to prepare proteins into design units
#######################################
import sys
import os
from openeye import oechem
from openeye import oegrid
from openeye import oespruce
def main (argv=sys.argv) :
   if len(argv) < 3 or len(argv) > 5:
       oechem.OEThrow.Usage(
           "%s <infile> <site_residue> [<mtzfile>] [<loopdbfile>]" % argv[0]
       \lambdaif s = oechem. oemolistream()ifile = argv[1]if not ifs.open(ifile):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % ifile)
   site_residue = \text{argv[2]}include\_loop = Falseinclude\_ed = Falseif len(argv) > 3:
       if len(argv) == 5 or (len(argv) == 4 and "mtz" in argv[3]):
           edfile = \arg(v[3])ed = oeqrid.OESkewGrid()if not oegrid. OEReadMTZ (edfile, ed, oegrid. OEMTZMapType_Fwt) :
               oechem.OEThrow.Fatal(
                   "Unable to read electron density file %s" % edfile
               ) # noga
           include\_ed = Trueif len(argv) == 5:loopfile = argv[4]
```

```
include\_loop = Trueelif len(argv) == 4 and "mtz" not in argv[3]:
            loopfile = argv[3]include\_loop = Trueif ifs. GetFormat () not in [oechem. OEFormat_PDB, oechem. OEFormat_CIF]:
        oechem. OEThrow. Fatal ("Only works for . pdb or . cif input files")
    ifs.SetFlavor(
        oechem.OEFormat_PDB,
        oechem.OEIFlavor_PDB_Default
        | oechem.OEIFlavor_PDB_DATA
        | oechem.OEIFlavor_PDB_ALTLOC,
   ) # noga
   mol = occhem.OEGraphMol()if not oechem. OEReadMolecule(ifs, mol):
        oechem. OEThrow. Fatal ("Unable to read molecule from %s" % ifile)
   metadata = oespruce. OEStructureMetadata()
   opts = oespruce.OEMakeDesignUnitOptions()
    opts.GetPrepOptions().GetBuildOptions().GetLoopBuilderOptions().
\rightarrow SetBuildTails (False)
    if include_loop:
        opts.GetPrepOptions().GetBuildOptions().GetLoopBuilderOptions().
\rightarrowSetLoopDBFilename(
            loopfile
        \lambdaif include_ed:
        design_units = oespruce.OEMakeDesignUnits(mol, ed, metadata, opts, site_
\rightarrowresidue)
    else:
        design_units = oespruce.OEMakeDesignUnits(mol, metadata, opts, site_residue)
   base_name = os.path.basename(ifile) [:-4] + "_DU_{}.oedu"
    for i, design_unit in enumerate(design_units):
        oechem.OEWriteDesignUnit(base_name.format(i), design_unit)
if name == " main ":
    sys.exit(main(sys.argv))
```

### **Example**

make\_apo\_design\_units.py 1w50.pdb "ASP:228: :A" 1w50.mtz spruce\_bace.loop\_db

will generate the following output (failing to add partial charges to iodine):

```
DPI: 0.13, RFree: 0.28, Resolution: 1.75
Processing BU # 0 with title: BETA-SECRETASE 1, chains A
Found gap between ALA 157 A 1
                                and ALA 168 A 1, with sequence GFPLNQSEVL
Opened database spruce_bace.loop_db
LoopDatabase Info:
   276 loops from RSCB last synced on 03-19-2020, were added to LoopTemplateDatabase
→on 03-19-2020 using Spruce Toolkit 1.0.0.a
                                                                         (continues on next page)
```

```
The loop database was built with a max loop length of 22, a termini crop length,
\rightarrow of 2, and excluding regular secondary structures
Warning: Failed to charge miscellaneous components
Warning: Unable to add partial charges and radii to DesignUnit: BETA-SECRETASE 1(A)
→DU_biounit
Iridium Category: NA, DPI: 0.13, RFree: 0.28, Resolution: 1.75
```

See also:

- OEMakeDesignUnits function
- OEReadDesignUnit and OEWriteDesignUnit functions in the OEChem TK manual
- OEDesignUnit class in the OEChem TK manual

# 4.1.3 Creating mmcif file from an input DU

This example shows how to write an output mmcif file from a spruce generated design unit.

### **Command Line Interface**

This example uses an input design unit (oedu) file, and will output a mmcif file from it to a temporary directory (see OEMakeDesignUnits for details on the API).

prompt> du2mmcif <input design unit>

### Code

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
import os
from openeye import oechem
from openeye import oegrid
from openeye import oespruce
```

```
def main (argv=sys.argv) :
   if len(argv) > 2:
        oechem.OEThrow.Usage("%s <infile>" % argv[0])
    ifs = oechem.oemolistream()
    \text{ifile} = \text{argv[1]}ofile = os.path.basename (ifile) [-5] + ".cif"ofs = oechem.oemolostream(ofile)
   ofs.SetFlavor(oechem.OEFormat_MMCIF, oechem.OEOFlavor_MMCIF_Default)
   du = oechem.OEDesignUnit ()
   if not oechem. OEReadDesignUnit (ifile, du) :
        oechem. OEThrow. Fatal ("Cannot read design unit!")
   complex = occhem.OEGraphMol()du.GetComponents(complex, oechem.OEDesignUnitComponents_All ^ oechem.
\rightarrowOEDesignUnitComponents_PackingResidues)
    du.GetPDBMetaData(complex)
    oechem.OEWriteMolecule(ofs, complex)
    ofs.close()
if _name_ = "main":
    sys.exit(main(sys.argv))
```

### **Example**

```
prompt> du2mmcif.py 1TQN A DU HEM A-508.oedu
```

See also:

- · OEMakeDesignUnitsfunction
- OEReadDesignUnit and OEWriteDesignUnit functions in the OEChem TK manual
- OEDesignUnit class in the OEChem TK manual

# 4.1.4 Calculating superposition

The superposition calculation is a functionality offered through the **Spruce TK**. This example shows how to calculate structural superposition using either the global, DDM, weighted-DDM, site sequence, or SSE methods.

### **Command Line Interface**

This example takes in a reference and a fit protein (from either a PDB or OEDU file) and aligns them with one of the supported methods (see OESuperposeMethod for methods and descriptions).

```
prompt> superpose <reference protein PDB> <fit protein PDB>..
\rightarrow[global|ddm|weighted|sse|site] [site-residue file]
```

#### Code

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
#######################################
# Simple superimposition of a fit protein on to a reference protein
#######################################
import sys
import os
from openeye import oechem
from openeye import oespruce
import tempfile
def ReadProteinMol(ifilename):
   if oechem. OEIsReadableDesignUnit(ifilename):
       du = oechem.OEDesignUnit()
       if not oechem. OEReadDesignUnit (ifilename, du) :
           oechem. OEThrow. Fatal ("Unable to open %s for reading OEDesignUnit" %
\rightarrowifilename)
       return du
    else:ifs = oechem.oemolistream()
        ifs.SetFlavor(oechem.OEFormat_PDB, oechem.OEIFlavor_PDB_Default | oechem.
→OEIFlavor_PDB_DATA | oechem.OEIFlavor_PDB_ALTLOC) # noqa
       if not ifs.open(ifilename):
           oechem. OEThrow. Fatal ("Unable to open %s for reading" % ifilename)
       mol = occhem.OEGraphMol()if not oechem. OEReadMolecule(ifs, mol):
           oechem. OEThrow. Fatal ("Unable to read molecule from %s" % ifilename)
       return \text{mol}def ReadSiteResidues(in file):
   site\_residues = []with open (in\_file, "r") as f:
       lines = f.read() .splitlines()for line in lines:
           if line.strip() == "":continue
```

```
site_residues.append(line)
    return site_residues
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) < 3:
        oechem. OEThrow. Usage(f" {argv[0] } <reference protein PDB> <fit protein PDB>
\rightarrow [qlobal|ddm|weighted|sse|site] [site-residue file] [nowrite]") # noga
    inp\_method = "global"if len(argv) > 3:
        inp\_method = argv[3]site_file = None
    do write = Trueif inp_method == "site":if len(argv) > 4:
             site_file = argv[4]else:oechem. OEThrow. Warning (f"A text file containing site residues must be,
\rightarrowprovided for using the SiteSequence method\ln")
            sys<br>.{exit(1)}if not os.path.isfile(site_file):
             oechem. OEThrow. Warning (f"File not found: {site_file}\n")
             sys.exit(1)nowrite_argidx = 5else:
        nowrite_argidx = 4if len(argv) > nowrite_argidx:
        if argv [nowrite_argidx] != "nowrite":
             oechem. OEThrow. Warning (f" {argv[nowrite_argidx] } is not a valid option. \n")
             sys.exit(1)else:
            do write = Falseref\_prot_file = argv[1]fit\_prot\_file = argv[2]ref prot = ReadProteinMol(ref prot file)
    fit_prot = ReadProteinMol(fit_prot_file)
    method = oespruce.OEGetSuperposeMethodFromName(inp_method)
    if method == oespruce. OESuperposeMethod_Undefined:
        oechem. OEThrow. Warning (f" {inp_method} superposition method is not supported.\n
\leftrightarrow<sup>"</sup>)
        sys.exit(1)opts = oespruce.OESuperposeOptions(method)
    print (f"Superposing {fit_prot_file} to {ref_prot_file} using {oespruce.
→OEGetSuperposeMethodName(method) }. \n")
    results = oespruce. OESuperposeResults()
    superposition = oespruce. OESuperpose (opts)
    if opts. GetMethod() == oespruce. OESuperposeMethod_Site and not isinstance (ref_
\rightarrowprot, oechem. OEDesignUnit):
```

```
site_residues = ReadSiteResidues(site_file)
        superposition. SetupRef(ref_prot, site_residues)
    else:superposition. SetupRef (ref_prot)
    superposition. Superpose (results, fit_prot)
    rmsd = results.GetRMSD()segscore = results.GetSegScore()
    tanimoto = results.GetTanimoto()
   results. Transform (fit_prot)
    if opts. GetMethod() == oespruce. OESuperposeMethod_SSE:
       print (f"Tanimoto: /tanimoto: 4.2f/\n")
    Also:print (f"RMSD: {rmsd: 4.2f} Angstroms.")
        print(f"SeqScore: {seqscore:d}.\n")
    if do_write:
        temp_dir = tempfile.mkdtemp()
        if isinstance(fit_prot, oechem.OEDesignUnit):
            str_pos = fit_prot_file.find(".oedu")
            base_name = fit_prot_file[0:str_pos]
            output_fit_file = os.path.join(temp_dir, base_name + "_sp.oedu")
            ofs = oechem.oeofstream(output_fit_file)
            oechem.OEWriteDesignUnit(ofs, fit_prot)
        else:
            str pos = fit prot file.find(".pdb")
            base_name = fit_prob_file[0:str_pos]output_fit_file = os.path.join(temp_dir, base_name + "_sp.oeb.gz")
            ofs = oechem.oemolostream(output_fit_file)
            oechem. OEWriteMolecule (ofs, fit_prot)
        print (f"Superimposed fit protein was written to {output_fit_file}.\n")
if _name == " main ":
    sys.exit(main(sys.argv))
```

### **Example**

prompt> superpose.py 1A29.pdb 1CLL.pdb ddm

will generate the following output:

```
Superposing 1CLL.pdb to 1A29.pdb using ddm
Writing superimposed fit protein to 1CLL_sp.oeb.gz
RMSD: 0.596203 Angstroms
SeqScore: 642
```

See also:

- OESuperpose class
- OESuperposeOptions class
- OESuperposeResults class

• OESuperposeMethod namespace

# 4.1.5 Extracting Biounits from PDB header remarks

Biounit (BU) extraction is one of the more basic functionalities offered through the **Spruce TK**. This example shows how to extract BUs using the PDB header remarks.

### **Command Line Interface**

This example takes in a PDB file, and optionally the maximum number of atoms to be considered a BU as well as a boolean flag to instruct the code to prefer author or software generated headers (see OEExtractBioUnits for details on the API).

prompt> extract\_biounits\_remarks <extract protein PDB> [max atoms] [prefer author]

### **Code**

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
#######################################
# Simple superimposition of a fit protein on to a reference protein
#######################################
import sys
import os
from openeye import oechem
from openeye import oespruce
import tempfile
def ReadProteinFromPDB(pdb_file, mol):
   if s = oechem. oemolistream()ifs.SetFlavor(oechem.OEFormat_PDB, oechem.OEIFlavor_PDB_Default | oechem.
→OEIFlavor_PDB_DATA | oechem.OEIFlavor_PDB_ALTLOC) # noqa
   if not ifs.open(pdb_file):
       oechem. OEThrow. Fatal ("Unable to open %s for reading." % pdb_file)
```

```
temp_{mol} = occhem_{OEGraphMol}()if not oechem. OEReadMolecule(ifs, temp_mol) :
        oechem. OEThrow. Fatal ("Unable to read molecule from %s." % pdb_file)
    ifs.close()
    fact = oechem.OEAltLocationFactory(temp_mol)
   mol.Clear()
    fact.MakePrimaryAltMol(mol)
   return (mol)
def main(argv=[_name_]):
   if len(argv) not in [2, 4, 5]:
        oechem. OEThrow. Usage ("%s <extract protein PDB> [max atoms] [prefer author]
\rightarrow [nowrite]" % argv[0]) # noga
    do\_write = Trueif len(argv) == 5:if argv[4] != "nowrite":
            oechem. OEThrow. Warning ("%s is not a valid option. \n" % argv[4])
            sys.exit(1)else:
            do_write = Falseopts = oespruce.OEBioUnitExtractionOptions()
   if len(argv) > = 4:
        opts.SetMaxAtoms(int(arqv[2]))
        opts.SetPreferAuthorRecord(bool(argy[3]))
    extract_prob_file = argv[1]extract_prot = oechem.OEGraphMol()
    extract_success = ReadProteinFromPDB(extract_prot_file, extract_prot)
    if not extract_success:
        oechem. OEThrow. Fatal ("Unable to read protein (s) from PDB file.")
   biounits = oespruce. OEExtractBioUnits (extract_prot, opts)
    if do_write:
        pdb\_ext = ".pdb"str_pos = extract_prot_file.find(pdb_ext)
        base name = extract prot file[0:str pos]
        temp\_dir = tempfile.mkdtemp()for i, biounit in enumerate (biounits) :
            output_biounit_file = \cos p, path.join(temp_dir, base_name + "_BU_{}.oeb.gz".
\rightarrowformat(i)) # noqa
            print ("Writing biounit \{ to \{ )". format (i, output_biounit_file))
            ofs = oechem.oemolostream(output_biounit_file)
            oechem.OEWriteMolecule(ofs, biounit)
if name == " main ":
   sys.exit(main(sys.argv))
```

### **Example**

```
prompt> extract_biounits_remarks.py 4re6.pdb
```

will generate the following output:

```
Writing biounit 0 to 4re6_BU_0.oeb.gz
Writing biounit 1 to 4re6_BU_1.oeb.gz
```

See also:

- · OEExtractBioUnits function
- OEBioUnitExtractionOptions class

# 4.1.6 Extracting Biounits by aligning to a reference protein

Biounit (BU) extraction is one of the more basic functionalities offered through the **Spruce TK**. This example shows how to extract BUs using a sequence alignment to a reference protein.

### **Command Line Interface**

This example takes in an extraction PDB file, a reference PDB file, and optionally the minimum score for the alignment to the reference as well as a boolean flag to instruct the code to superimpose the output BU to the input reference protein (see OEExtractBioUnits for details on the API).

```
prompt> extract_biounits_ref <extract protein PDB> <reference protein PDB> [min.,
\rightarrowscore] [superpose]
```

### Code

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
#######################################
# Simple superimposition of a fit protein on to a reference protein
#######################################
import sys
```

```
import os
from openeye import oechem
from openeye import oespruce
import tempfile
def ReadProteinFromPDB(pdb_file, mol):
    if s = oechem. oemolistream()ifs.SetFlavor(oechem.OEFormat_PDB, oechem.OEIFlavor_PDB_Default | oechem.
→OEIFlavor_PDB_DATA | oechem.OEIFlavor_PDB_ALTLOC) # noga
    if not ifs.open(pdb_file):
        oechem. OEThrow. Fatal ("Unable to open %s for reading." % pdb_file)
   temp \text{mol} = occhem \text{.} OEGraphMol()if not oechem. OEReadMolecule(ifs, temp_mol):
        oechem. OEThrow. Fatal ("Unable to read molecule from %s." % pdb_file)
    ifs.close()
    fact = oechem. OEAltLocationFactory (temp_mol)
   mol.Clear()
    fact.MakePrimaryAltMol(mol)
   return (mol)
def main(argv=[__name__]):
    if len(argv) not in [3, 5, 6]:
        oechem. OEThrow. Usage ("%s <extract protein PDB> <reference protein PDB> [min.
→score] [superpose] [nowrite]" % argv[0]) # noqa
    do_write = Trueif len(argv) == 6:
        if arrow[5] != "nowrite":
            oechem. OEThrow. Warning ("%s is not a valid option. \ln" % argv[5])
            sys.exit(1)
        else:
            do_write = Falseopts = oespruce.OEBioUnitExtractionOptions()
    if len(argv) >= 5:
        opts.SetMinScore(int(argy[3]))
        opts.SetSuperpose(bool(argv[4]))
   extract_prob_file = argv[1]extract_prot = oechem.OEGraphMol()
    extract_success = ReadProteinFromPDB(extract_prot_file, extract_prot)
    if not extract_success:
        oechem. OEThrow. Fatal ("Unable to extract protein(s) from PDB file.")
   ref\_prot_file = argv[2]ref\_prot = occhem.OEGraphMol()ref_success = ReadProteinFromPDB(ref_prot_file, ref_prot)
    if not ref_success:
        oechem. OEThrow. Fatal ("Unable to reference protein(s) from PDB file.")
   biounits = oespruce. OEExtractBioUnits (extract_prot, ref_prot, opts)
```

```
(continues on next page)
```

```
if do_write:
        pdb\_ext = ".pdb"str_pos = extract_prot_file.find(pdb_ext)
        base_name = extract_prot_file[0:str_pos]
        temp_dir = tempfile.mkdtemp()
        for i, biounit in enumerate (biounits):
            output_biounit_file = os.path.join(temp\_dir, base_name + "_BU_{}/).oeb.gr'.\rightarrowformat(i)) # noqa
           print ("Writing biounit {} to {}". format(i, output_biounit_file))
            ofs = oechem.oemolostream(output_biounit_file)
            oechem.OEWriteMolecule(ofs, biounit)
if name == " main ":
    sys.exit(main(sys.argv))
```

#### **Example**

prompt> extract\_biounits\_ref.py 40BD.pdb 2UPJ.pdb

will generate the following output:

```
Writing biounit 0 to 40BD_BU_0.oeb.gz
Writing biounit 1 to 40BD_BU_1.oeb.gz
```

See also:

```
• OEExtractBioUnits function
```

• OEBioUnitExtractionOptions class

# 4.1.7 Finding pockets and their properties (like, Surface Area) from a PDB file

This example shows how to find pockets in an input PDB file using the OEFindPockets function. OEDesignUnit file (OEDesignUnit) can also be used as input to find the pockets.

### **Command Line Interface**

This example uses an input PDB file, and will print surface area and list of residues for each found pocket in given PDB file.

prompt> findpockets <input protein molecule or DesignUnit file>

#### Code

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
######################################
\longleftrightarrow # # # # # # # # # # # # # # # # # # #
# This program demonstrates how to find pockets and some of its properties from a
protein or DesignUnit file.
#######################################
\longleftrightarrow \# \# \# \# \# \# \# \# \# \# \# \# \# \# \# \# \# \# \#import sys
from openeye import oechem
from openeye import oespruce
def readProteinMol(ifilename):
    if oechem. OEGetFileExtension(ifilename) == 'oedu':
        du = oechem.OEDesignUnit()
        if not oechem. OEReadDesignUnit (ifilename, du) :
            oechem. OEThrow. Fatal ("Unable to open %s for reading OEDesignUnit" %.
\leftrightarrowifilename)
        return du
    else:
        if s = oechem.oemolistream()if not ifs.open(ifilename):
            oechem. OEThrow. Fatal ("Unable to open %s for reading" % ifilename)
        mol = occhem.OEGraphMol()oechem.OEReadMolecule(ifs, mol)
        return moldef main (argv=None) :
   if argv is None:
        \text{arg} v = \lceil \text{ name} \rceilif len(sys.argv) != 2:
        oechem. OEThrow. Usage ("%s <protein or DesignUnit input file>" % argv[0])
   mol = readProteinMol(sys.argv[1])pockets = oespruce. OEFindPockets (mol)
    print ("pockets count: %s" % len(list(pockets)))
```

```
pockets. ToFirst()
   pocket\_cntr = 0for pocket in pockets:
        pocket_cntr += 1
        pocket_residues = pocket.GetResidues()
        print ("pocket_%s Residues count: " % pocket_cntr, len(list(pocket_residues)))
        pocket_residues.ToFirst()
        print ("pocket_%s Residues: " % pocket_cntr)
        for res in pocket_residues:
           print (res)
        print ("pocket_%s Surface Area: " % pocket_cntr, pocket.GetSurfaceArea())
if _name == " main ":
   sys.exit(main(sys.argv))
```

# **Example**

prompt> findpockets.py 7mhf.pdb

### will generate the following output:

| pockets count           | 1                 |
|-------------------------|-------------------|
| pocket_1 Residues count | 22                |
| pocket_1 Residues:      |                   |
| HOH 623 A 2             |                   |
| GLY 143 A 1             |                   |
| ASN 142 A 1             |                   |
| HOH 502 A 2             |                   |
| DMS 404 A 2             |                   |
| MET 165 A 1 A           |                   |
| HOH 624 A 2             |                   |
| ASP 187 A 1             |                   |
| HOH 671 A 2             |                   |
| HOH 655 A 2             |                   |
| HOH 589 A 2             |                   |
| MET 49 A 1              |                   |
| HOH 782 A 2             |                   |
| ARG 188 A 1             |                   |
| THR 25 A 1              |                   |
| HIS 41 A 1              |                   |
| GLN 189 A 1             |                   |
| CYS 44 A 1              |                   |
| HOH 750 A 2             |                   |
| HOH 548 A 2             |                   |
| THR 45 A 1              |                   |
| SER 46 A 1              |                   |
| pocket_1 Surface Area   | 211.0912322998047 |

### See also:

• OEPocketOptions class

# 4.1.8 Write a metadata JSON file from a FASTA file

This example shows how to read in a FASTA to structure metadata and write to a JSON file.

# **Example**

prompt> fasta\_to\_structmeta.py seq.fasta chainIDs output.JSON

Code

**FIVE** 

# **OESPRUCE API**

# **5.1 OESpruce Classes**

Attention: This API is currently available in C++ and Python.

# 5.1.1 OEBioUnitExtractionOptions

class OEBioUnitExtractionOptions : public OESystem:: OEOptions

This class stores the optional parameter sets for biounit extraction for use in the OEExtractBioUnits function.

### **Code Example**

- Extracting Biounits by aligning to a reference protein example
- Extracting Biounits from PDB header remarks example

### **Constructors**

```
OEBioUnitExtractionOptions()=default
OEBioUnitExtractionOptions (const OEBioUnitExtractionOptions &) = default
```

Default and copy constructor that constructs a OEBioUnitExtractionOptions object.

### operator=

```
OEBioUnitExtractionOptions &
  operator=(const OEBioUnitExtractionOptions &) =default
```

Assignment operator.

# **GetMaxAtoms**

unsigned GetMaxAtoms () const

Returns the maximum number of atoms for the extracted biounit.

### **GetMaxParts**

unsigned GetMaxParts() const

Returns the maximum number of parts for a given transformation required to generate a biounit.

# GetMinScore

unsigned GetMinScore() const

Returns the minimum score required for the biounit extraction's sequence alignment.

### **GetPreferAuthorRecord**

bool GetPreferAuthorRecord() const

Returns the boolean whether or not to prefer the author or software record for biounit extraction.

#### **GetSuperpose**

bool GetSuperpose () const

Returns the boolean whether or not to superpose the output biounit to the input reference structure.

### **SetMaxAtoms**

void SetMaxAtoms (unsigned maxAtoms)

Sets the maximum number of atoms allowed for the extracted biounit.

### **SetMaxParts**

void SetMaxParts (unsigned maxParts)

Sets the maximum number of parts allowed for a given transformation required to generate a biounit.

## **SetMinScore**

void SetMinScore (int minScore)

Sets the minimum score required for the biounit extraction's sequence alignment.

### **SetPreferAuthorRecord**

void SetPreferAuthorRecord (bool preferAuthor)

Sets the boolean of whether or not to prefer the author or software record for biounit extraction.

### **SetSuperpose**

void SetSuperpose (bool superpose)

Sets the boolean whether or not to superpose the output biounit to the input reference structure.

### See also:

• OEMakeDesignUnitOptions class

# 5.1.2 OECapBuilderOptions

Attention: This API is currently available in C++ and Python.

class OECapBuilderOptions : public OESystem: : OEOptions

This class stores the optional parameter sets for building caps in the OECapTermini, OECapCTermini, and OECapNTermini functions.

### **Constructors**

```
OECapBuilderOptions()=default
OECapBuilderOptions (const OECapBuilderOptions &) = default
```

Default and copy constructor that constructs a OECapBuilderOptions object.

#### operator=

OECapBuilderOptions & operator=(const OECapBuilderOptions &)=default

Assignment operator.

### **GetDeleteClashingSolvent**

bool GetDeleteClashingSolvent () const

Returns the boolean whether or not to delete solvent waters that clash with other atoms.

### **GetAllowTruncate**

bool GetAllowTruncate() const

Returns the boolean whether or not it is okay to make a terminal residue the cap if building one would result in a clash, or if the backbone of the residue itself is incomplete

### **GetForceCapping**

bool GetForceCapping() const

Returns the boolean of whether or not to force caping in the event the cap would clash with something in the system

### SetDeleteClashingSolvent

void SetDeleteClashingSolvent (bool deleteClashingSolvent)

Sets the boolean of whether or not to delete solvent waters that clash with other atoms.

### **SetAllowTruncate**

void SetAllowTruncate (bool allowTruncate)

Sets the boolean of whether or not it is okay to make a terminal residue the cap if building one would result in a clash, or if the backbone of the residue itself is incomplete

### **SetForceCapping**

```
void SetForceCapping (bool forceCapping)
```

Sets the boolean of whether or not to force capping in the event the cap would clash with something in the system. This setting supersedes the settings for OECapBuilderOptions.GetAllowTruncate and OECapBuilderOptions.GetDeleteClashingSolvent.

See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitBuildOptions class
- · OECapTermini function
- · OECapCTermini function
- OECapNTermini functions

# 5.1.3 OEDesignUnitBuildOptions

Attention: This API is currently available in C++ and Python.

class OEDesignUnitBuildOptions : public OESystem:: OEOptions

This class stores the optional parameter sets for design unit splitting for use in the OEMakeDesignUnitOptions function.

### **Constructors**

```
{\tt OEDesignUnitBuildOptions} {\tt ()=default}OEDesignUnitBuildOptions (const OEDesignUnitBuildOptions &)=default
```

Default and copy constructor that constructs a OEDesignUnitBuildOptions object.

#### operator=

OEDesignUnitBuildOptions & operator=(const OEDesignUnitBuildOptions &)=default

Assignment operator.

### **GetBuildLoops**

bool GetBuildLoops() const

Returns the boolean whether or not to build loops.

# **GetBuildSidechains**

bool GetBuildSidechains() const

Returns the boolean whether or not to build side chains.

### **GetCapCTermini**

bool GetCapCTermini() const

Returns the boolean whether or not to cap all C-termini in the system with NME.

## **GetCapNTermini**

bool GetCapNTermini() const

Returns the boolean whether or not to cap all N-termini in the system with ACE.

## **GetSidechainBuilderOptions**

```
OESidechainBuilderOptions & GetSidechainBuilderOptions()
const OESidechainBuilderOptions & GetSidechainBuilderOptions () const
```

Returns a reference to the stored sidechain builder options (OESidechainBuilderOptions) class.

### **GetLoopBuilderOptions**

```
OELoopBuilderOptions &GetLoopBuilderOptions()
const OELoopBuilderOptions &GetLoopBuilderOptions() const
```

Returns a reference to the stored loop builder options (OELoopBuilderOptions) class.

## **GetCapBuilderOptions**

```
OECapBuilderOptions &GetCapBuilderOptions()
const OECapBuilderOptions &GetCapBuilderOptions () const
```

Returns a reference to the stored cap builder options (OECapBuilderOptions) class.

### **SetBuildLoops**

void SetBuildLoops (bool buildLoops)

Sets the boolean of whether or not to build loops.

### **SetBuildSidechains**

void SetBuildSidechains (bool buildSidechains)

Sets the boolean of whether or not to build side chains.

### **SetCapCTermini**

void SetCapCTermini (bool capCTermini)

Sets the boolean of whether or not to cap all C-termini in the system with NME.

### **SetCapNTermini**

void SetCapNTermini (bool capNTermini)

Sets the boolean of whether or not to cap all N-termini in the system with ACE.

### **SetSidechainBuilderOptions**

void SetSidechainBuilderOptions (OESidechainBuilderOption scOpts)

Set the sidechain builder options class (OESidechainBuilderOptions).

### **SetCapBuilderOptions**

void SetCapBuilderOptions (OECapBuilderOptions capOpts)

Set the cap builder options class (OECapBuilderOptions).

### **SetLoopBuilderOptions**

void SetLoopBuilderOptions (OELoopBuilderOptions lOpts)

Set the loop builder options class (OELoopBuilderOptions).

#### See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OESidechainBuilderOptions class
- OELoopBuilderOptions class
- OECapBuilderOptions class

# 5.1.4 OEDesignUnitEnumerateSitesOptions

Attention: This API is currently available in C++ and Python.

class OEDesignUnitEnumerateSitesOptions : public OESystem:: OEOptions

This class stores the optional parameter sets for design unit binding site enumeration for use in the OEEnumerateSites function.

## **Constructors**

```
OEDesignUnitEnumerateSitesOptions()=default
OEDesignUnitEnumerateSitesOptions(const OEDesignUnitEnumerateSitesOptions &)=default
```

Default and copy constructor that constructs a OEDesignUnitEnumerateSitesOptions object.

#### operator=

```
OEDesignUnitEnumerateSitesOptions &
 operator=(const OEDesignUnitEnumerateSitesOptions &)=default
```

Assignment operator.

### **GetAddInteractionHints**

**bool** GetAddInteractionHints() const

Returns the boolean whether or not to add interaction hints.

### **GetAddStyle**

bool GetAddStyle() const

Returns the boolean whether or not to add style.

#### **GetCollapseNonSiteAlts**

bool GetCollapseNonSiteAlts() const

Returns the boolean whether or not to collapse non site alternate locations.

#### **GetDuplicateRemoval**

bool GetDuplicateRemoval() const

Returns the boolean whether or not to remove duplicate sites.

### **GetEnumerateCofactorSites**

bool GetEnumerateCofactorSites() const

Returns the boolean whether or not to enumerate cofactor sites.

# **GetRestrictToRefSite**

```
bool GetRestrictToRefSite() const
```

Returns the boolean whether or not to restrict enumeration to the site of the reference structure.

### **GetSiteSize**

double GetSiteSize() const

Returns the size of the site.

# **SetAddInteractionHints**

void SetAddInteractionHints (bool addInteractions)

Sets the boolean whether or not to add interactions.

# **SetAddStyle**

void SetAddStyle(bool addStyle)

Sets the boolean whether or not to add style.

### **SetCollapseNonSiteAlts**

void SetCollapseNonSiteAlts (bool collapseNonSiteAlts)

Sets the boolean whether or not to collapse non site alternate locations.

### **SetDuplicateRemoval**

void SetDuplicateRemoval (bool duplicateRemoval)

Sets the boolean whether or not to remove duplicate sites.

### **SetEnumerateCofactorSites**

void SetEnumerateCofactorSites (bool enumCofactorSites)

Sets the boolean whether or not to enumerate cofactor sites.

## **SetRestrictToRefSite**

void SetRestrictToRefSite(bool restrictToRefSite)

Sets the boolean whether or not to restrict enumeration to the reference site.

### **SetSiteSize**

void SetSiteSize(double siteSize)

Sets the size of the site.

### See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitEnumerateSitesOptions class

# 5.1.5 OEDesignUnitMutationOptions

Attention: This API is currently available in C++ and Python.

class OEDesignUnitMutationOptions : public OESystem:: OEOptions

This class stores the optional parameter sets used in design unit mutation for use in the OEMutateResidues function.

#### **Constructors**

```
OEDesignUnitMutationOptions()=default
OEDesignUnitMutationOptions (const OEDesignUnitMutationOptions &)=default
```

Default and copy constructors.

#### operator=

```
OEDesignUnitMutationOptions &
 operator=(const OEDesignUnitMutationOptions &)=default
```

Assignment operator.

# **AddMutation**

void AddMutation (const OEChem:: OEResidue mutationRes, const unsigned targetIdx)

Adds a mutation to make based on an input OEResidue object, along with a constant representing the target component which is taken from the OEDesignUnitComponents namespace.

### **ClearMutations**

void ClearMutations()

Clears all mutations.

### **GetMutations**

std::map<OEChem::OEResidue, unsigned> GetMutations() const

Returns the stored std::map of mutations, which is keyed on an OEResidue object with a value of the target component which is taken from the OEDesignUnitComponents namespace.

### **SetMutations**

void SetMutations (const std:: map<OEChem:: OEResidue, unsigned> &mutations)

Sets the stored *std::map* of mutations, which is keyed on an OEResidue object with a value of the target component which is taken from the OEDesignUnitComponents namespace.

#### See also:

• OESidechainBuilderOptions class

# 5.1.6 OEDesignUnitPrepOptions

Attention: This API is currently available in C++ and Python.

class OEDesignUnitPrepOptions : public OESystem:: OEOptions

This class stores the optional parameter sets used in design unit preparation for use in the OEMakeDesignUnitOptionsfunction.

### **Constructors**

```
OEDesignUnitPrepOptions()=default
OEDesignUnitPrepOptions (const OEDesignUnitPrepOptions &) =default
OEDesignUnitPrepOptions (OEDesignUnitBuildOptions buildOpts,
                        OESpruce:: OEProtonateDesignUnitOptions protonateOpts,
                        OEDesignUnitEnumerateSitesOptions enumOpts)
```

Default, copy, and advanced constructor that constructs a OEDesignUnitPrepOptions object. The advanced constructor take three separate sub-options classes as arguments: an options class that controls prep (OEDesignUnitPrepOptions), an options class that controls the building options (OEDesignUnitBuildOptions), and an options class that controls alternate location handling (OEDesignUnitEnumerateSitesOptions).

#### operator=

OEDesignUnitPrepOptions & operator=(const OEDesignUnitPrepOptions &)=default

Assignment operator.

### **GetAssignPartialChargesAndRadii**

bool GetAssignPartialChargesAndRadii()

Returns the boolean whether or not to assign partial charges and radii.

### **GetBuildOptions**

```
OEDesignUnitBuildOptions &GetBuildOptions()
const OEDesignUnitBuildOptions &GetBuildOptions () const
```

Returns a reference to the stored build options (OEDesignUnitBuildOptions) class.

### **GetChargeEngine**

OEProton:: OEDesignUnitCharges & GetChargeEngine()

Returns a reference to the stored charge engine (OEDesignUnitCharges) class.

### **GetEnumerateSitesOptions**

```
OEDesignUnitEnumerateSitesOptions &GetEnumerateSitesOptions()
const OEDesignUnitEnumerateSitesOptions &GetEnumerateSitesOptions() const
```

Returns a reference to the stored design unit site enumeration options (OEDesignUnitEnumerateSitesOptions) class.

### **GetProtonate**

bool GetProtonate() const

Returns the boolean of whether or not to protonate the design unit.

### **GetStrictProtonationMode**

bool GetStrictProtonationMode() const

Returns the boolean of whether to fail design unit preparation if the protonation stage fails

### **GetProtonateOptions**

```
OESpruce::OEProtonateDesignUnitOptions &GetProtonateOptions()
const OESpruce:: OEProtonateDesignUnitOptions &GetProtonateOptions () const
```

Returns a reference to the stored design unit protonation options (OEProtonateDesignUnitOptions) class.

### **SetAssignPartialChargesAndRadii**

void SetAssignPartialChargesAndRadii (bool assignPartialChargesAndRadii)

Sets the boolean of whether or not to assign partial charges and radii.

### **SetBuildOptions**

void SetBuildOptions (OEDesignUnitBuildOptions buildOpts)

Sets the design unit building options class (OEDesignUnitBuildOptions).

### **SetChargeEngine**

void SetChargeEngine (OEProton:: OEDesignUnitCharges chargeEngine)

Sets the charging engine when charges are added (OEDesignUnitCharges).

### **SetEnumerateSitesOptions**

void SetEnumerateSitesOptions (OEDesignUnitEnumerateSitesOptions enumOpts)

Sets the design unit site enumeration options class (OEDesignUnitEnumerateSitesOptions).

## **SetProtonate**

|  | <b>void</b> SetProtonate (const bool protonate) |  |  |  |
|--|-------------------------------------------------|--|--|--|
|--|-------------------------------------------------|--|--|--|

Sets the boolean of whether or not to protonate the design unit.

### **SetStrictProtonationMode**

void SetStrictProtonationMode(const bool strictProtonate) const

Sets the boolean of whether or not to fail design unit preparation if the protonation stage fails

### **SetProtonateOptions**

void SetProtonateOptions (OESpruce:: OEProtonateDesignUnitOptions protonateOpts)

Sets the design unit protonation options class (OEProtonateDesignUnitOptions).

### See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitCharges class
- OEDesignUnitEnumerateSitesOptions class
- OEProtonateDesignUnitOptions class
- OEPlaceHydrogensOptions class
- OEDesignUnitBuildOptions class
- OELoopBuilderOptions class
- OESidechainBuilderOptions class
- OELoopBuilderOptions class
- OECapBuilderOptions class

# 5.1.7 OEDesignUnitSplitOptions

Attention: This API is currently available in C++ and Python.

class OEDesignUnitSplitOptions : public OESystem:: OEOptions

This class stores the optional parameter sets for design unit building for use in the OEMakeDesignUnitOptions function.

# **Constructors**

```
OEDesignUnitSplitOptions()=default
OEDesignUnitSplitOptions (const OEDesignUnitSplitOptions &) = default
```

Default and copy constructor that constructs a OEDesignUnitSplitOptions object.

#### operator=

OEDesignUnitSplitOptions & operator=(const OEDesignUnitSplitOptions &)=default

Assignment operator.

### **AddCofactorCode**

void AddCofactorCode (const std:: string argValue)

Explicitly sets the name of the molecule(s) to be considered a cofactor.

### **AddExcipientCode**

void AddExcipientCode (const std::string argValue)

Explicitly sets the name of the molecule( $s$ ) to be considered an excipient.

### **AddLipidCode**

void AddLipidCode (const std:: string argValue)

Explicitly sets the name of the molecule(s) to be considered an lipid.

#### **ClearCofactorCodes**

```
void ClearCofactorCodes()
```

Removes the name(s) of the molecules considered to be cofactors.

#### **ClearExcipientCodes**

void ClearExcipientCodes()

Removes the name(s) of the molecules considered to be excipients.

### **ClearLipidCodes**

|  | <b>void</b> ClearLipidCodes() |  |  |  |
|--|-------------------------------|--|--|--|
|--|-------------------------------|--|--|--|

Removes the name(s) of the molecules considered to be lipids.

### **GetAlternateLocationHandling**

unsigned GetAlternateLocationHandling() const

Returns the value of the alternate location handling mode, which is given by the OEAlternateLocationOption namespace.

### **GetCofactorCodes**

```
std::vector<std::string> &GetCofactorCodes()
const std::vector<std::string> &GetCofactorCodes() const
```

Returns a reference to the vector of the name(s) of the molecule(s) considered to be cofactors.

#### **GetExcipientCodes**

```
std::vector<std::string> &GetExcipientCodes()
const std::vector<std::string> &GetExcipientCodes() const
```

Returns a reference to the stored vector of strings representing names of molecules that should be considered excipients.

### **GetLipidCodes**

```
std::vector<std::string> &GetLipidCodes()
const std::vector<std::string> &GetLipidCodes() const
```

Returns a reference to the stored vector of strings representing names of molecules that should be considered lipids.

### **GetMakePackingResidues**

```
bool GetMakePackingResidues() const
```

Returns the boolean whether or not to make packing residues.

### **GetMaxLigAtoms**

unsigned GetMaxLigAtoms () const

Returns the maximum number of atoms for a molecule to still be considered a ligand.

### **GetMaxLigResidues**

unsigned GetMaxLigResidues () const

Returns the maximum number of residues for a molecule to still be considered a ligand.

### **GetMaxSystemAtoms**

unsigned GetMaxSystemAtoms () const

Returns the maximum number of atoms for a system to be split.

#### **GetMinLigAtoms**

unsigned GetMinLigAtoms () const

Returns the minimum number of atoms for a molecule to still be considered a ligand.

#### **GetTargetComponentID**

unsigned GetTargetComponentID() const

Returns the constant of the target component, which is taken from the OEDesignUnitComponents namespace.

#### SetAlternateLocationHandling

void SetAlternateLocationHandling (unsigned altLocHandling)

Sets the constant that controls how alternate location enumeration will be handled, which is taken from the OEAlternateLocationOption namespace.

### **SetCofactorCodes**

void SetCofactorCodes (const std::vector<std::string> &argValue)

Sets the vector of strings representing names of molecules that should be considered cofactors.

### **SetExcipientCodes**

void SetExcipientCodes (const std::vector<std::string> &argValue)

Sets the vector of strings representing names of molecules that should be considered excipients.

### **SetLipidCodes**

void SetLipidCodes (const std:: vector<std:: string> &argValue)

Sets the vector of strings representing names of molecules that should be considered lipids.

### **SetMakePackingResidues**

void SetMakePackingResidues (bool makePackingResidues)

Sets the boolean of whether or not to make a packing residue component.

### **SetMaxLigAtoms**

void SetMaxLigAtoms (unsigned maxLigAtoms)

Sets the maximum number of atoms for a molecule to be considered a ligand.

#### **SetMaxLigResidues**

void SetMaxLigResidues (unsigned maxLigResidues)

Sets the maximum number of residues for a molecule to be considered a ligand.

#### **SetMaxSystemAtoms**

void SetMaxSystemAtoms (unsigned maxSystemAtoms)

Sets the maximum number of atoms for a system to be split.

### **SetMinLigAtoms**

void SetMinLigAtoms (unsigned minLigAtoms)

Sets the minimum number of atoms for a molecule to be considered a ligand.

### **SetTargetComponentID**

void SetTargetComponentID (unsigned targetCompID)

Sets the constant of the target component, which is taken from the OEDesignUnitComponents namespace.

#### See also:

• OEMakeDesignUnitOptions class

# 5.1.8 OEHeterogenMetadata

Attention: This API is currently available in C++ and Python.

class OEHeterogenMetadata

This class stores the optional parameter sets involved in tautomer assignment during design unit protonation in the OEProtonateDesignUnit function.

### **Constructors**

```
OEHeterogenMetadata ()=default
OEHeterogenMetadata (const OEHeterogenMetadata &) =default
```

Default and copy constructors.

### operator=

```
OEHeterogenMetadata & operator=(const OEHeterogenMetadata &)=default
```

Assignment operator.

### **AddTautomer**

void AddTautomer (const std:: string tautomer)

Add a tautomer using a Smiles string.

### **AddTautomers**

void AddTautomers (const std:: vector<std:: string> tautomers)

Add a set of tautomers of the ligand using a *std*::*vector* of Smiles strings.

# **ClearTautomers**

```
void ClearTautomers()
```

Clears all tautomer strings.

### **GetID**

std::string GetID() const

Returns the stored ID string for the ligand.

## **GetSmiles**

std::string GetSmiles() const

Returns the stored Smiles string for the ligand.

### **GetTautomers**

```
std::vector<std::string> &GetTautomers()
const std::vector<std::string> &GetTautomers() const
```

Returns a reference of the set of stored tautomers for the ligand.

### **GetTitle**

std::string GetTitle() const

Returns the ligand's title.

### **GetType**

unsigned GetType() const

Returns the type of heterogen of the ligand as defined in the OEHeterogenType namespace.

#### **SetID**

void SetID (const std:: string id)

Sets a string of the ligand's ID.

## **SetSmiles**

```
void SetSmiles (const std:: string smiles)
```

Sets the Smiles string for the ligand.

### **SetTitle**

void SetTitle (const std:: string title)

Sets the ligand's title.

## **SetType**

void SetType (const unsigned type)

Sets the type of heterogen of the ligand as defined in the OEHeterogenType namespace.

# 5.1.9 OEIsModeledAtom

Attention: This API is currently available in C++ and Python.

class OEIsModeledAtom : public OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>

This predicate is used to identify atoms that have been built using Spruce TK either by capping terminal residues, building out partial residues, or by mutating a residue. Otherwise it returns false.

The following methods are publicly inherited from OEUnaryPredicate:

operator() CreateCopy CreatePredicateCopy

The following methods are publicly inherited from OEUnaryFunction:

operator() CreateCopy

### **Constructors**

OEIsModeledAtom()

Default constructor.

### operator()

bool operator () (const OEChem:: OEAtomBase & atom) const

Returns true if the atom has been built using **Spruce TK** either by capping terminal residues, building out partial residues, or by mutating a residue.

## **CreateCopy**

OESystem::OEUnaryFunction<OEChem::OEAtomBase, bool> \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEIsModeledAtom object is dynamically allocated and owned by the caller.

See also:

- · OECapTermini function
- · OECapCTermini function
- · OECapNTermini function
- · OEBuildSidechains function
- OEMutateResidue function

# 5.1.10 OELoopBuilderOptions

Attention: This API is currently available in C++ and Python.

class OELoopBuilderOptions : public OESystem: : OEOptions

This class stores the optional parameter sets for building loops OEBuildLoops and OEBuildSingleLoop functions.

### **Constructors**

```
OELoopBuilderOptions()=default
OELoopBuilderOptions (const OELoopBuilderOptions &) =default
```

Default and copy constructor that constructs a OELoopBuilderOptions object.

#### operator=

OELoopBuilderOptions & operator=(const OELoopBuilderOptions &)=default

Assignment operator.

#### **GetLoopDBFilename**

std::string GetLoopDBFilename() const

Returns the filename of the loop database used when searching for compatible loops.

### **GetUsePackingResidues**

bool GetUsePackingResidues() const

Returns the boolean whether or not to use crystal packing residues during loop modeling (if available).

### **GetCropLength**

unsigned GetCropLength() const

Returns the number of residues on either side of a gap to remove, since these are known to sometimes be poorly resolved and therefore have configurations that make it difficult to build loops.

### GetTransformThreshold

unsigned GetTransformThreshold() const

Returns the number of loops from the database to transform, meaning mutate from their database sequence to target sequence, if they are not 100% sequence matching. Structures with 100% sequence match are not affected by this threshold.

### **GetStrictProlineMatch**

bool GetStrictProlineMatch() const

Returns the boolean of whether or not fuzzy sequence matches have to have proline residues in the correct position. This can be relevant since they have a different backbone conformation than other amino acid residues.

### **GetConnectBufferDistance**

double GetConnectBufferDistance() const

Returns the buffer distance allowed between the anchor atoms (connection points) when searching for fuzzy sequence matches.

### GetBackboneClashRejectThreshold

double GetBackboneClashRejectThreshold() const

Returns the threshold of clashing backbone atoms. If the clash level is above this threshold a loop from the database is rejected, and is not processed further.

### GetLoopClashRejectThreshold

double GetLoopClashRejectThreshold() const

Returns the threshold of clashing loops atoms. This threshold excludes already considered clashing backbone atoms. If the clash level is above this threshold a loop from the database is rejected, and is not processed further.

### **GetOptimizationShell**

double GetOptimizationShell() const

Returns the radius of atoms being considered when minimizing the loops in place. Since multiple loops are being optimized, it is the union of atoms inside the radius around each starting loop configuration that is considered. This allows comparison of the energies between each loop conformation as the systems are of identical size.

### **GetOptimizationTolerance**

double GetOptimizationTolerance() const

Returns the tolerance used by the optimizer.

### GetOptimizationStage1IterMultiplier

unsigned GetOptimizationStage1IterMultiplier() const

Returns the multiplier of optimization steps per residue in the loop used during the initial steepest descent optimization.

### GetOptimizationStage2IterMultiplier

unsigned GetOptimizationStage2IterMultiplier() const

Returns the multiplier of optimization steps per residue in the loop used during the secondary BFGS optimization.

# GetOptimizationUseSolventModel

bool GetOptimizationUseSolventModel() const

Returns whether or not to use a simplistic solvent model during the loop optimization.

#### **GetOptimizationInclSurfaceAreaTerm**

bool GetOptimizationInclSurfaceAreaTerm() const

Returns whether or not to include the surface area term when scoring the loops after optimization.

#### **GetOptimizationMaxLoops**

unsigned GetOptimizationMaxLoops() const

Returns the number of loops to optimize, the higher the number the longer the calculation will take, but also includes more structural diversity.

### **GetAllowBuildDisulfideBridges**

**bool** GetAllowBuildDisulfideBridges() const

Returns whether or not to allow building disulfide bridges between the loop and the protein if possible, requires cystine residues in proximity.

#### **GetSeqAlignMethod**

unsigned GetSeqAlignMethod() const

Returns the sequence alignment method, from the OESeqAlignmentMethod namespace, used to compare the provided sequence and the structure for gaps.

#### **GetSeqAlignGapPenalty**

int GetSeqAlignGapPenalty() const

Returns the sequence alignment gap penalty, used to compare the provided sequence and the structure for gaps with the OEGetSimpleAlignment function.

# **GetSeqAlignExtendPenalty**

unsigned GetSeqAlignExtendPenalty() const

Returns the sequence alignment extend penalty, used to compare the provided sequence and the structure for gaps with the OEGetSimpleAlignment function.

### **GetBuildTails**

bool GetBuildTails() const

Returns whether or not to allow building missing tails at the N and C termini.

### **SetLoopDBFilename**

void SetLoopDBFilename(std::string filename)

Sets the filename of the loop database to use when searching for compatible loops.

#### **SetUsePackingResidues**

void SetUsePackingResidues (bool usePackingResidues)

Sets whether or not to use crystal packing residues during loop modeling (if available).

### **SetCropLength**

void SetCropLength (unsigned cropLength)

Returns the number of residues on either side of a gap to remove, since these are known to sometimes be poorly resolved and therefore have configurations that make it difficult to build loops.

### SetTransformThreshold

void SetTransformThreshold (unsigned transformThreshold)

Sets the number of loops from the database to transform, meaning mutate from their database sequence to target sequence, if they are not 100% sequence matching. Structures with 100% sequence match are not affected by this threshold.

### **SetStrictProlineMatch**

void SetStrictProlineMatch (bool strictProline)

Sets whether or not fuzzy sequence matches have to have proline residues in the correct position. This can be relevant since they have a different backbone conformation than other amino acid residues.

### **SetConnectBufferDistance**

void SetConnectBufferDistance (double buffer)

Sets the buffer distance allowed between the anchor atoms (connection points) when searching for fuzzy sequence matches.

#### SetBackboneClashRejectThreshold

void SetBackboneClashRejectThreshold(double bbClashThreshold)

Sets the threshold of clashing backbone atoms. If the clash level is above this threshold a loop from the database is rejected, and is not processed further.

### SetLoopClashRejectThreshold

void SetLoopClashRejectThreshold (double loopClashThreshold)

Sets the threshold of clashing loops atoms. This threshold excludes already considered clashing backbone atoms. If the clash level is above this threshold a loop from the database is rejected, and is not processed further.

### **SetOptimizationShell**

void SetOptimizationShell (double optimizationShellRadius)

Set the radius of atoms being considered when minimizing the loops in place. Since multiple loops are being optimized, it is the union of atoms inside the radius around each starting loop configuration that is considered. This allows comparison of the energies between each loop conformation as the systems are of identical size.

#### **SetOptimizationTolerance**

```
void SetOptimizationTolerance (double optimizationTolerance)
```

Sets the tolerance used by the optimizer.

### SetOptimizationStage1IterMultiplier

void SetOptimizationStage1IterMultiplier (unsigned stage1multiplier)

Sets the multiplier of optimization steps per residue in the loop used during the initial steepest descent optimization.

### SetOptimizationStage2IterMultiplier

void SetOptimizationStage2IterMultiplier (unsigned stage2multiplier)

Sets the multiplier of optimization steps per residue in the loop used during the secondary BFGS optimization.

### **SetOptimizationUseSolventModel**

void SetOptimizationUseSolventModel (bool useSolventModel)

Sets whether or not to use a simplistic solvent model during the loop optimization.

### **SetOptimizationInclSurfaceAreaTerm**

void SetOptimizationInclSurfaceAreaTerm (bool useSATerm)

Sets whether or not to include the surface area term when scoring the loops after optimization.

### **SetOptimizationMaxLoops**

void SetOptimizationMaxLoops (unsigned maxOptLoops)

Sets the number of loops to optimize, the higher the number the longer the calculation will take, but also includes more structural diversity.

### **SetAllowBuildDisulfideBridges**

void SetAllowBuildDisulfideBridges (bool allowBuildDisulfideBridges)

Sets whether or not to allow building disulfide bridges between the loop and the protein if possible, requires cystine residues in proximity.

### **SetSeqAlignMethod**

unsigned SetSeqAlignMethod (unsigned seqAlignMethod)

Sets the sequence alignment method, from the OESeqAlignmentMethod namespace, used to compare the provided sequence and the structure for gaps.

## **SetSegAlignGapPenalty**

void SetSeqAlignGapPenalty (int gapPenalty)

Set the sequence alignment gap penalty, used to compare the provided sequence and the structure for gaps with the OEGetSimpleAlignment function.

# **SetSeqAlignExtendPenalty**

void SetSeqAliqnExtendPenalty(int extendPenalty) const

Set the sequence alignment extend penalty, used to compare the provided sequence and the structure for gaps with the OEGetSimpleAlignment function.

### **SetBuildTails**

void SetBuildTails (bool BuildTails)

Sets whether or not to allow building missing tails at the C and N termini.

#### See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitBuildOptions class
- OESidechainBuilderOptions class
- OEBuildLoops function
- · OEBuildSingleLoop function
- · OESeqAlignmentMethod namespace
- OEGetSimpleAlignment function
- OESequenceAlignment class

# 5.1.11 OEMakeDesignUnitOptions

Attention: This API is currently available in C++ and Python.

The OEMakeDesignUnitOptions class holds other options classes that are used during the structure preparation processes. The organization of those options classes is illustrated in the figure below. Default constructing this options class, constructs all the necessary options classes in the illustration, which can then be accessed and modified. This class stores the optional parameter sets for design unit construction for use in the OEMakeDesignUnits and OEMakeDesignUnit functions.

![](_page_69_Figure_1.jpeg)

## **Constructors**

```
OEMakeDesignUnitOptions()=default
OEMakeDesignUnitOptions(const OEMakeDesignUnitOptions &) =default
OEMakeDesignUnitOptions(OEDesignUnitSplitOptions splitOpts,
                        OEDesignUnitPrepOptions prepOpts,
                        OEBioUnitExtractionOptions buExtractOpts)
```

Default, copy, and advanced constructor that constructs a OEMakeDesignUnitOptions object. The advanced constructor take three separate sub-options classes as arguments: an options class that controls componentization of the system (OEDesignUnitSplitOptions), an options class that controls prep (OEDesignUnitPrepOptions), and an options class that controls biounit extraction (OEBioUnitExtractionOptions).

### operator=

OEMakeDesignUnitOptions & operator=(const OEMakeDesignUnitOptions &)=default

Assignment operator.

### **GetBioUnitExtractionOptions**

```
OEBioUnitExtractionOptions &GetBioUnitExtractionOptions()
const OEBioUnitExtractionOptions &GetBioUnitExtractionOptions() const
```

Returns a reference to the stored biounit extraction options (OEBioUnitExtractionOptions) class.

### **GetPrepOptions**

```
OEDesignUnitPrepOptions &GetPrepOptions()
const OEDesignUnitPrepOptions &GetPrepOptions() const
```

Returns a reference to the stored design unit prep options (OEDesignUnitPrepOptions) class.

#### **GetSplitOptions**

```
OEDesignUnitSplitOptions &GetSplitOptions()
const OEDesignUnitSplitOptions &GetSplitOptions() const
```

Returns a reference to the stored options for splitting options (OEDesignUnitSplitOptions) class.

### **GetSuperpose**

bool GetSuperpose () const

Returns the boolean whether or not to superpose the design units onto a common reference.

#### **GetSuperpositionMethod**

unsigned GetSuperpositionMethod() const

Returns the stored superposition method taken from the OESuperpositionType namespace.

#### **SetBioUnitExtractionOptions**

void SetBioUnitExtractionOptions (OEBioUnitExtractionOptions buExtractOpts)

Sets the biounit extraction options class (OEBioUnitExtractionOptions).

### **SetPrepOptions**

void SetPrepOptions (OEDesignUnitPrepOptions prepOpts)

Sets the design unit prep options class (OEDesignUnitPrepOptions).

### **SetSplitOptions**

void SetSplitOptions (OEDesignUnitSplitOptions splitOpts)

Sets the system molecular componentization options class (OEDesignUnitSplitOptions).

### **SetSuperpose**

void SetSuperpose (bool superpose)

Sets the boolean of whether or not to superpose design units to a common reference.

### **SetSuperpositionMethod**

void SetSuperpositionMethod (unsigned superposeMethod)

Sets the superposition method from a value in the OESuperpositionType namespace.

#### See also:

- OEBioUnitExtractionOptions class
- OEDesignUnitSplitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitCharges class
- OEDesignUnitEnumerateSitesOptions class
- OEProtonateDesignUnitOptions class
- OEPlaceHydrogensOptions class
- OEDesignUnitBuildOptions class
- OELoopBuilderOptions class
- OESidechainBuilderOptions class
- OELoopBuilderOptions class
- OECapBuilderOptions class

# 5.1.12 OEPocket

Attention: This API is currently available in C++ and Python.

#### class OEPocket

This class stores the pockets resulting from running OEFindPockets function.

# **Constructors**

```
OEPocket (const OESpicoli:: OESurface& surf, OEChem:: OEMolBase& mol) ;
OEPocket (const OEPocket &)
```

Default and copy constructor that constructs a OEPocket object.

#### operator=

OEPocket& operator=(const OEPocket &)

Assignment operator.

### **GetSurfaceArea**

double GetSurfaceArea() const

Returns the surface area for the pocket surface.

#### **GetLocalDensity**

double GetLocalDensity () const

Returns the local density score for the pocket. A score  $> 50$  is considered high quality.

### **GetPocketPredicate**

const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>& GetPocketPredicate() const

Returns an atom predicate for the pocket. The pocket is residue based and can therefore be transferred to structures in the same target.

### **GetPocketSurface**

```
const OESpicoli:: OESurface& GetPocketSurface() const;
OESpicoli:: OESurface& GetPocketSurface();
```

Returns a reference to the surface of the pocket.

### **GetAtoms**

OESystem::OEIterBase<OEChem::OEAtomBase>\* GetAtoms()

Returns an iterator of the atoms making up the pocket surface.

## **GetResidues**

OESystem::OEIterBase<OEChem::OEResidue>\* GetResidues();

Returns an iterator of the OEResidues making up the pocket.

#### See also:

- · OEFindPockets function
- OEPocketOptions class
- OEMakeDesignUnitFromPocket function

# 5.1.13 OEPocketOptions

Attention: This API is currently available in C++ and Python.

class OEPocketOptions : public OESystem: : OEOptions

This class stores the optional parameter sets for pocket finding using  $OEFindPockets$  function.

### **Constructors**

```
OEPocketOptions();
OEPocketOptions (const OEPocketOptions &) = default
```

Default and copy constructor that constructs a OEPocketOptions object.

### operator=

```
OEPocketOptions &
 operator=(const OEPocketOptions &)=default
```

Assignment operator.

### **GetMinSurfaceArea**

double GetMinSurfaceArea() const

Returns the minimum surface area for a detected pocket surface. [Default:  $150$   $Angstrom^2$ ]

# **GetMaxSurfaceArea**

double GetMaxSurfaceArea() const

Returns the maximum surface area for a detected pocket surface. [Default:  $3000$  Angstrom<sup>2</sup>]

### **GetBurialFactor**

double GetBurialFactor() const

Returns the factor used to distinguish pockets from the general surface. [Default: 1.4]

## **SetMinSurfaceArea**

void SetMinSurfaceArea (double minSurfArea) const

Sets the minimum surface area for a detected pocket surface.

### **SetMaxSurfaceArea**

void SetMaxSurfaceArea (double maxSurfArea) const

Sets the maximum surface area for a detected pocket surface.

### **SetBurialFactor**

void SetBurialFactor (double burialFactor) const

Sets the factor used to distinguish pockets from the general surface.

#### See also:

- · OEFindPockets function
- OEPocket class

# 5.1.14 OEProtonateDesignUnitOptions

Attention: This API is currently available in C++ and Python.

class OEProtonateDesignUnitOptions : public OESystem:: OEOptions

This class stores the optional parameter sets used in design unit protonation for use in the OEProtonateDesignUnit function.

## **Constructors**

```
OEProtonateDesignUnitOptions()=default
OEProtonateDesignUnitOptions(OEBio::OEPlaceHydrogensOptions placeHOpts)
OEProtonateDesignUnitOptions(const OEProtonateDesignUnitOptions &rhs)=default
```

Default and copy constructors.

#### operator=

```
OEProtonateDesignUnitOptions &
  operator=(const OEProtonateDesignUnitOptions & rhs) =default
```

Assignment operator.

### **GetGenerateTautomers**

bool GetGenerateTautomers() const

Returns the boolean whether or not to generate tautomers for the ligand and cofactors.

### **GetHetGroupNbrDist**

double GetHetGroupNbrDist() const

Returns the distance cutoff for two groups to be considered within the same cluster.

### **GetOptimizeExpProtons**

**bool** GetOptimizeExpProtons() const

Returns the boolean whether or not to optimize the position of experimental protons.

### **GetPlaceHydrogensOptions**

```
OEBio:: OEPlaceHydrogensOptions& GetPlaceHydrogensOptions()
const OEBio:: OEPlaceHydrogensOptions& GetPlaceHydrogensOptions() const
```

Returns a reference to the stored place hydrogen options (OEPlaceHydrogensOptions) class.

# **SetGenerateTautomers**

void SetGenerateTautomers (const bool generateTautomers)

Sets the boolean of whether or not to generate tautomers.

### **SetHetGroupNbrDist**

void SetHetGroupNbrDist (const double hetGroupNbrDist)

Sets the distance cutoff for two groups to be considered within the same cluster.

### **SetOptimizeExpProtons**

void SetOptimizeExpProtons (const bool optimizeExpProtons)

Sets the boolean whether or not to optimize the position of experimental protons.

### **SetPlaceHydrogensOptions**

void SetPlaceHydrogensOptions (const OEBio:: OEPlaceHydrogensOptions placeHOpts)

Sets the place hydrogens options class (OEPlaceHydrogensOptions).

#### See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEPlaceHydrogensOptions class

# 5.1.15 OESidechainBuilderOptions

Attention: This API is currently available in C++ and Python.

class OESidechainBuilderOptions : public OESystem:: OEOptions

This class stores the optional parameter sets for building sidechains in the OEBuildSidechains, OEMutateResidue, OEMutateResidues, OEBuildLoops, OEBuildSingleLoop functions.

## **Constructors**

```
OESidechainBuilderOptions()=default
OESidechainBuilderOptions (const OESidechainBuilderOptions &)=default
OESidechainBuilderOptions(bool minimizeSidechainsShell)=default
```

Default and copy constructor that constructs a *OESidechainBuilderOptions* object.

#### operator=

OESidechainBuilderOptions & operator=(const OESidechainBuilderOptions &)=default

Assignment operator.

### **GetDeleteClashingSolvent**

bool GetDeleteClashingSolvent () const

Returns the boolean whether or not to delete solvent waters that clash with other atoms.

### **GetMinimizeSidechains**

bool GetMinimizeSidechains() const

Returns the boolean whether or not to minimize the sidechains of the target residues.

## GetMinimizeSidechainsShell

```
bool GetMinimizeSidechainsShell() const
```

Returns the boolean whether or not to minimize the sidechains of the residues around the target residues.

#### **GetRotamerLibrary**

unsigned GetRotamerLibrary () const

Returns the rotamer library used for side chain rebuilding.

### **GetStrictMode**

bool GetStrictMode() const

Returns the boolean whether or not to fail early if any of the partial or missings sidechain could not be built

### **SetRotamerCoverage**

void SetRotamerCoverage (double rotamerCoverage)

Sets the value for the rotamer coverage percentage to be used for side chain rebuilding.

### **SetRotamerLibrary**

void SetRotamerLibrary (unsigned rotamerLibrary)

Sets the boolean of the rotamer library.

### SetDeleteClashingSolvent

void SetDeleteClashingSolvent (bool deleteClashingSolvent)

Sets the boolean of whether or not to delete solvent waters that clash with other atoms.

## **SetMinimizeSidechains**

**bool** SetMinimizeSidechains () const

Sets the boolean whether or not to minimize the sidechains of the target residues.

## SetMinimizeSidechainsShell

bool SetMinimizeSidechainsShell() const

Sets the boolean whether or not to minimize the sidechains of the residues around the target residues.

### **SetStrictMode**

void SetStrictMode (bool strictMode) const

Sets the boolean whether or not to fail early if any of the partial or missings sidechain could not be built

See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitBuildOptions class
- OEBuildSidechains function
- OEMutateResidue function
- · OEMutateResidues function
- · OEBuildLoops function
- · OEBuildSingleLoop function

# 5.1.16 OESequenceMetadata

Attention: This API is currently available in C++ and Python.

class OESequenceMetadata

This class stores the sequence data used in biomolecule rebuilding in the  $OEMakeDesignUnits$  function.

### **Constructors**

```
OESequenceMetadata () =default
OESequenceMetadata (const OESequenceMetadata &) =default
```

Default and copy constructors.

#### operator=

OESequenceMetadata & operator= (const OESequenceMetadata &)=default

Assignment operator.

## **GetChainID**

std::string GetChainID() const

Returns the string of the chain ID of the sequence.

### **GetEndResidueInsertCode**

char GetEndResidueInsertCode() const

Returns a char representing the insertion code of the last residue.

# **GetEndResidueNumber**

int GetEndResidueNumber() const

Returns the residue number.

### **GetSequence**

std::string GetSequence() const

Returns the string sequence.

#### **GetStartResidueInsertCode**

char GetStartResidueInsertCode() const

Returns a char representing the insertion code of the first residue.

## GetStartResidueNumber

int GetStartResidueNumber() const

Returns the residue number  $(int)$  of the first residue.

## **SetChainID**

void SetChainID (const std:: string cid)

Sets the string of the chain ID of the sequence.

## **SetEndResidueInsertCode**

void SetEndResidueInsertCode (const char endInsCode)

Sets the char representing the insertion code of the last residue.

# **SetEndResidueNumber**

void SetEndResidueNumber (const int endResNum)

Sets the residue number  $(int)$  of the last residue.

### **SetSequence**

void SetSequence (const std::string seq)

Sets the string of the sequence. The format should be a three letter code per residue separated by spaces.

## **SetStartResidueInsertCode**

void SetStartResidueInsertCode (const char startInsCode)

Sets the char representing the insertion code of the first residue.

### **SetStartResidueNumber**

void SetStartResidueNumber (const int startResNum)

Sets the residue number  $(int)$  of the first residue.

# 5.1.17 OEStructureMetadata

Attention: This API is currently available in C++ and Python.

class OEStructureMetadata

This class stores structural information used in design unit preparation within the  $OEMakeDesignUnits$  function.

### **Constructors**

```
OEStructureMetadata()=default
OEStructureMetadata (const OEStructureMetadata &) =default
OEStructureMetadata (const std:: vector<OEHeterogenMetadata> &hetData)
OEStructureMetadata (const std::vector<OEHeterogenMetadata> &hetData,
                    const std::vector<OESequenceMetadata> &seqData)
```

Default, copy, and advanced constructor that constructs an OEStructureMetadata object. The advanced constructor takes a combination of two separate data classes as arguments: a class that stores the structural metadata (OEStructureMetadata), and a class that stores the heterogen metadata (OEHeterogenMetadata). A separate overload that takes a std::vector of each of those data classes is also available.

#### operator=

OEStructureMetadata & operator=(const OEStructureMetadata &)=default

Assignment operator.

### AddHeterogenMetadata

```
void AddHeterogenMetadata (const OEHeterogenMetadata & hetData)
void AddHeterogenMetadata (const std::vector<OEHeterogenMetadata> &hetData)
```

Adds the heterogen metadata (OEHeterogenMetadata) as a single object or as a std::vector of objects.

### **AddKeyword**

void AddKeyword (const std:: string keyword)

Adds a string keyword.

#### **AddKeywords**

void AddKeywords (const std:: vector<std:: string> keywords)

Adds a std::vector of string keywords.

#### **AddSequenceMetadata**

```
void AddSequenceMetadata (const OESequenceMetadata &seqData)
void AddSequenceMetadata (const std::vector<OESequenceMetadata> & seqData)
```

Adds the sequence metadata (OESequenceMetadata) as a single object or as a std::vector of objects.

#### **ClearHeterogenMetadata**

void ClearHeterogenMetadata()

Clears all heterogen metadata.

#### **ClearKeywords**

void ClearKeywords ()

Clears all keywords.

#### **ClearSequenceMetadata**

void ClearSequenceMetadata()

Clears all sequence metadata.

### **GetAuthor**

std::string GetAuthor() const

Returns the name of the author.

#### **GetExperimentDate**

std::string GetExperimentDate() const

Returns the string version of the experiment date.

### **GetExperimentType**

unsigned GetExperimentType() const

Returns the experiment type as defined by the OEExperiment Type namespace.

#### GetHeterogenMetadata

```
std::vector<OEHeterogenMetadata> &GetHeterogenMetadata()
const std::vector<OEHeterogenMetadata> &GetHeterogenMetadata() const
```

Returns a reference to the std::vector of stored heterogen metadata (OEHeterogenMetadata) objects.

### **GetIridiumData**

```
OEBio:: OEIridiumData & GetIridiumData ()
const OEBio:: OEIridiumData & GetIridiumData () const
```

Returns a reference to the Iridium data (OEIridiumData) object.

#### **GetKeywords**

```
std::vector<std::string> &GetKeywords()
const std::vector<std::string> &GetKeywords() const
```

Returns a reference to the vector of keyword strings.

### **GetRevision**

std::string GetRevision() const

Returns the revision.

# **GetRevisionDate**

std::string GetRevisionDate() const

Returns the string version of the revision date.

### **GetSequenceMetadata**

```
std::vector<OESequenceMetadata> &GetSequenceMetadata()
const std::vector<0ESequenceMetadata> &GetSequenceMetadata() const
```

### **GetStructureID**

std::string GetStructureID() const

Returns the structure's ID.

### **SetAuthor**

void SetAuthor (const std:: string author)

Sets the author's name.

#### **SetExperimentDate**

void SetExperimentDate (const std::string exptDate)

Sets the string version of the experiment date.

### SetExperimentType

void SetExperimentType (unsigned exprType)

Sets the experiment type as defined by the OEExperiment Type namespace.

### **SetIridiumData**

void SetIridiumData (const OEBio:: OEIridiumData &iridData)

Sets the Iridium data from an OEIridiumData object.

## **SetRevision**

void SetRevision (const std:: string revVersion)

Sets the revision.

### **SetRevisionDate**

void SetRevisionDate (const std:: string revDate)

Sets the string version of the revision date.

# **SetStructureID**

void SetStructureID (const std:: string structureID)

Sets the string version of the structure's ID.

# 5.1.18 OESecondaryStructureSuperposition

Warning: This is a deprecated API. Please use OESuperpose class instead.

Attention: This API is currently available in C++ and Python.

class OESecondaryStructureSuperposition

This class represents OESecondaryStructureSuperposition that performs a structural superposition on fit protein to a reference using a shape-based alignment of the secondary structure elements.

#### See also:

- OESuperpositionOptions class
- OEStructuralSuperposition class

#### **Constructors**

```
OESecondaryStructureSuperposition (const OEChem:: OEMolBase & refMol,
                                    const OEChem:: OEMolBase &fitMol,
                                    const OESuperpositionOptions& argOpts =
\rightarrowOESuperpositionOptions())
```

Constructor that superimposes the fitMol to the refMol by using a shape-based alignment to the secondary structure elements. If no OESuperpositionOptions are passed in as argOpts, then the default behavior of using a superposition to all globally matched atoms will be used.

OESecondaryStructureSuperposition (const OESecondaryStructureSuperposition & rhs)

Copy constructor.

operator=

```
OESecondaryStructureSuperposition &
 operator=(const OESecondaryStructureSuperposition &rhs)
```

Assignment operator.

### operator bool

operator bool() const

Returns whether the OESecondaryStructureSuperposition object is valid.

### **GetFitChains**

std::vector<std::string> GetFitChains() const

Returns 1-letter code of all names of fit protein chains.

#### See also:

• GetRefChains method

# **GetRefChains**

std::vector<std::string> GetRefChains() const

Returns 1-letter code of all names of reference protein chains.

#### See also:

• GetFitChains <OESpruce\_OESecondaryStructureSuperposition\_GetFitChains> method

# **GetRotMatrix**

bool GetRotMatrix (double \*rmat) const

Returns by reference the rotation matrix of the superposition.

### **GetTanimoto**

double GetTanimoto() const

Returns the Tanimoto score for the structural superposition.

# **GetTranslation**

bool GetTranslation (double \*trans) const

Returns by reference the translation vector of the superposition.

### **Transform**

void Transform (OEChem:: OEMolBase& mol)

Transforms the input molecule using the stored rotation matrix and translation vector from the superposition.

# 5.1.19 OESpruceFilter

Attention: This API is currently available in C++ and Python.

Note: Note: We strongly recommend running OESpruceFilter for standardization and filtering prior to running the design unit preparation.

class OESpruceFilter

This class represents OESpruceFilter that performs a standardization and a filter check before prepping this structure in spruce

#### See also:

OESpruceFilterOptions class OEMakeDesignUnit class OEMakeBioDesignUnit class

### **Constructors**

```
OESpruceFilter();
OESpruceFilter(const OESpruceFilterOptions&, const OEMakeDesignUnitOptions&);
```

Constructor for spruce filter given the specified options class. If no OESpruceFilterOptions and OEMakeDesignUni*tOptions* are passed in as fopts and DUOpts, then the default options class will be passed into the constructor.

```
OESpruceFilter(const OESpruceFilter& rhs);
```

Copy constructor.

#### operator=

OESuperpose& operator=(const OESuperpose& rhs);

Assignment operator.

### **StandardizeAndFilter**

```
unsigned StandardizeAndFilter (OEChem:: OEMolBase& mol, const OESystem:: OESkewGrid&
→eDensGrid, const OEStructureMetadata& mdata = OEStructureMetadata());
```

Returns a code which indicates the issues that are detected for this structure

#### **GetMessages**

```
std::string GetMessages(const unsigned errorTypes = OESpruceFilterIssueCodes::ALL); //
A Mask can help filter messages
```

Returns the error message according to the provided error code

### **GetAtoms**

```
OESystem::OEIterBase<OEChem::OEAtomBase>* GetAtoms(const unsigned errorTypes =_
→OESpruceFilterIssueCodes:: ALL); // Mask can help filter messages
```

Returns the problematic atoms that have the issues indicated by the input error code

# 5.1.20 OESpruceFilterOptions

Attention: This API is currently available in C++ and Python.

The OESpruceFilterOptions class holds options classes that are used for structural checks. Default constructing this options class, constructs all the necessary options classes, which can then be accessed and modified. This class stores the optional parameter sets for use in the OEMakeDesignUnits and OEMakeDesignUnit functions.

### **Constructors**

```
OESpruceFilterOptions()
OESpruceFilterOptions (const OESpruceFilterOptions &) = default
```

Default, copy, and advanced constructor that constructs a *OESpruceFilterOptions* object.

#### operator=

```
OESpruceFilterOptions &operator=(const OESpruceFilterOptions &)=default
```

Assignment operator.

### **GetFixBondOrder**

bool GetFixBondOrder() const

Returns the boolean whether or not to fix incorrect bond order.If FixBondOrders is set to true, spruce filter will automatically delete partial sidechains. If the sidechain atoms are not properly connected, spruce filter will reassign the bond orders.

### **SetFixBondOrder**

void SetFixBondOrder (bool FixBondOrder)

Sets the boolean of whether or not to fix incorrect bond order.

### **GetFixNames**

bool GetFixNames() const

Returns the boolean whether or not to fix incorrect names for all components. If FixNames is set to true, spruce filter function will rename ligand name "UNL" to "LIG"; residue name "NMA" to "NME". Spruce filter will fail if residue has name "UNK".

#### **SetFixNames**

void SetFixNames (bool FixNames)

Sets the boolean of whether or not to fix incorrect names for all components.

### **GetFixBondsToMetals**

bool GetFixBondsToMetals() const

Returns the boolean whether or not to fix covalent bonds to metals. If FixBondsToMetals option is set to true, spruce filter function will set bond order of the incorrect covalent bonds to metals to 0.

# **SetFixBondsToMetals**

void SetFixBondsToMetals (bool FixBondOrder)

Sets the boolean of whether or not to fix covalent bonds to metals

### **GetFixBackboneAtoms**

bool GetFixBackboneAtoms() const

Returns the boolean whether or not to fix incorrect backbone atoms. If FixBackboneAtoms is set to true, spruce filter will delete incorrect partial backbone atoms.

#### **SetFixBackboneAtoms**

void SetFixBackboneAtoms (bool FixBackboneAtoms)

Sets the boolean of whether or not to fix incorrect backbone atoms

#### **GetDeleteFloatingRes**

bool GetDeleteFloatingRes() const

Returns the boolean whether or not to delete floating residues

### **SetDeleteFloatingRes**

void SetDeleteFloatingRes (bool DeleteFloatingRes)

Sets the boolean of whether or not to delete floating residues

### **GetFixLigandState**

**bool** GetFixLigandState() const

Returns the boolean whether or not to fix ligand states

### **SetFixLigandState**

void SetFixLigandState (bool FixLigandState)

Sets the boolean of whether or not to fix ligand states

# 5.1.21 OEStructuralSuperposition

Warning: This is a deprecated API. Please use OESuperpose class instead.

Attention: This API is currently available in C++ and Python.

class OEStructuralSuperposition

This class represents OEStructuralSuperposition that performs a structural superposition on fit protein to a reference protein, using a superposition method given as an optional parameter.

See also:

- OESuperpositionOptions class
- OESecondaryStructureSuperposition class

### **Constructors**

```
OEStructuralSuperposition (const OEChem:: OEMolBase &argRefMol,
                          const OEChem:: OEMolBase &argFitMol,
                          const OESuperpositionOptions &
→argOpts=OESuperpositionOptions())
```

Constructor that superimposes the argFitMol to the argRefMol. If no OESuperpositionOptions are passed in as argOpts, then the default behavior of using a superposition to all globally matched atoms will be used.

OEStructuralSuperposition (const OEStructuralSuperposition & rhs)

Copy constructor.

#### operator=

OEStructuralSuperposition & operator=(const OEStructuralSuperposition & rhs)

Assignment operator.

#### operator bool

operator bool() const

Returns whether the OEStructuralSuperposition object is valid.

# **ConstraintsMet**

bool ConstraintsMet() const;

Returns whether or not the constraints were met.

# **GetFitChains**

std::vector<std::string> GetFitChains() const

Returns 1-letter code of all names of fit protein chains.

### See also:

· OEStructuralSuperposition.GetRefChains method

### **GetRMSD**

double GetRMSD() const

Returns the RMSD of the structural superposition.

# **GetRefChains**

std::vector<std::string> GetRefChains() const

Returns 1-letter code of all names of reference protein chains.

#### See also:

· OEStructuralSuperposition.GetFitChains method

## **GetRegion**

std::vector<int> GetRegion() const

Returns the index of all residues involved in the alignment.

### **GetRotMatrix**

void GetRotMatrix (double \*rmat) const

Returns by reference the rotation matrix of the superposition.

### **GetScore**

|--|--|

Returns the sequence alignment score for the structural superposition.

### **GetTranslation**

void GetTranslation (double \*trans) const

Returns by reference the translation vector of the superposition.

## **Transform**

void Transform (OEChem:: OEMolBase& mol)

Transforms the input molecule using the stored rotation matrix and translation vector from the superposition.

# 5.1.22 OESuperpositionOptions

Attention: This API is currently available in C++ and Python.

class OESuperpositionOptions

This class represents OESuperpositionOptions that sets the optional parameters for structural superposition using the OEStructuralSuperposition class.

#### See also:

- OEStructuralSuperposition class
- OESecondaryStructureSuperposition class

## **Constructors**

OESuperpositionOptions()

Default constructor.

OESuperpositionOptions (const OESuperpositionOptions & rhs)

Copy constructor.

### operator=

OESuperpositionOptions & operator=(const OESuperpositionOptions & argOpts)

Assignment operator.

### **AddSiteResidue**

void AddSiteResidue (const std:: string &argSiteResidue)

Add a single site residue for OESuperpositionType\_Site -based superpositions based on a site-specific string that takes the form: <residue name>:<residue number>:<insertion code>:<chain id>.

#### See also:

- · OESuperpositionOptions. SetSiteResidues method
- · OESuperpositionOptions. GetSiteResidues method
- · OESuperpositionOptions. ClearSiteResidues method

### **ClearLigandConstraints**

void ClearLigandConstraints()

Clear the stored ligand constraints, if they exist.

#### See also:

- · OESuperpositionOptions. SetLigandConstraints method
- · OESuperpositionOptions. GetLigandConstraints method
- · OESuperpositionOptions. HasLigandConstraints method

### **ClearSiteResidues**

void ClearSiteResidues()

Remove any existing site residues from the OESuperpositionOptions object that would be used in the OESuperpositionType\_Site-based superposition calculations.

#### See also:

- · OESuperpositionOptions.AddSiteResidue method
- · OESuperpositionOptions. SetSiteResidues method
- · OESuperpositionOptions.GetSiteResidues method

### **GetDist**

double GetDist() const

Get the cutoff distance used in the nearest neighbors calculation for the site residue constraints (default =  $5.0$ Angstroms) for OESuperpositionType\_Site-based superpositions.

### **GetLigandConstraints**

void GetLigandConstraints (OEChem:: OEMolBase& refLig, OEChem:: OEMolBase& fitLig) const

Returns by reference the reference and fit ligand constraints that are stored.

#### See also:

- · OESuperpositionOptions. SetLigandConstraints method
- · OESuperpositionOptions. HasLigandConstraints method
- · OESuperpositionOptions. ClearLigandConstraints method

### **GetSiteResidues**

std::vector<std::string> GetSiteResidues() const

Get the site residues used in the OESuperpositionType\_Site -based calculation.

### GetSuperpositionType

unsigned GetSuperpositionType() const

Get the type of superposition to be performed. Types are given from the constants given in OESuperpositionType. The default type is OESuperpositionType\_Default.

### **HasLigandConstraints**

**bool** HasLigandConstraints() const

Returns whether or not ligand constraints have been set.

#### See also:

- · OESuperpositionOptions. SetLigandConstraints method
- · OESuperpositionOptions. GetLigandConstraints method
- · OESuperpositionOptions. ClearLigandConstraints method

## **SetDist**

void SetDist (double argDist)

Set the cutoff distance used in the nearest neighbors calculation for the site residue constraints for OESuperpositionType\_Site-based superpositions.

### **SetLigandConstraints**

```
void SetLigandConstraints (const OEChem:: OEMolBase& refLig, const OEChem:: OEMolBase&
\rightarrowfitLig)
```

Sets the ligand constraints that will be used for the superposition.

#### See also:

- · OESuperpositionOptions.GetLigandConstraints method
- · OESuperpositionOptions. HasLigandConstraints method
- · OESuperpositionOptions. ClearLigandConstraints method

### **SetSiteResidues**

void SetSiteResidues (const std:: vector<std:: string> &argSiteResidues)

Set all site residues at once for OESuperpositionType\_Site -based superpositions using a string vector, where each string takes the form <residue name>:<residue number>:<insertion code>:<chain id>.

#### See also:

- · OESuperpositionOptions.AddSiteResidue method
- · OESuperpositionOptions.GetSiteResidues method
- · OESuperpositionOptions. ClearSiteResidues method

### SetSuperpositionType

**bool** SetSuperpositionType (unsigned type)

Set the type of superposition to be performed. Types are taken from the constants given in  $OESuperpositionType$ .

# 5.1.23 OESuperpose

**Attention:** This API is currently available in C++ and Python.

class OESuperpose

This class represents OESuperpose that performs a structural superposition on fit protein to a reference protein, using a superposition method given as an optional parameter.

### See also:

- OESuperposeOptions class
- OESuperposeResults class

### **Code Example**

• Calculating superposition example

### **Constructors**

```
OESuperpose (const OESuperposeOptions& opts =
→OESuperposeOptions(OESuperposeMethod::Default));
```

Constructor for superposing molecules given the specified method and other options. If no OESuperposeOptions are passed in as opts, then the default behavior of using a superposition to all globally matched atoms will be used.

OESuperpose (const OESuperpose& rhs);

Copy constructor.

### operator=

OESuperpose& operator=(const OESuperpose& rhs);

Assignment operator.

### **HasRef**

bool HasRef() const

Returns whether or not the reference is set.

### **HasConstraintMol**

bool HasConstraintMol() const

Returns whether or not the constraint molecule is set.

### **Clear**

 $void Clear();$ 

Clears the reference and the constraint molecule.

### **SetOptions**

**bool** SetOptions (const OESuperposeOptions& opts);

Sets the options for the superposition.

**SetupRef** 

```
bool SetupRef (const OEBio:: OEDesignUnit& refDU,
             const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowrefPred=OEChem::OEIsTrueAtom())
bool SetupRef (const OEChem:: OEMolBase& refMol,
             const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowrefPred=OEChem::OEIsTrueAtom())
bool SetupRef (const OEChem:: OEMolBase& refMol,
             const OEChem:: OEMolBase& refConstraintMol,
             const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&...
\rightarrowrefPred=OEChem::OEIsTrueAtom())
bool SetupRef (const OEChem:: OEMolBase& refMol,
             const std::vector<std::string>& siteResidues,
             const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowrefPred=OEChem::OEIsTrueAtom())
bool SetupRef (const OEChem:: OEMolBase& refMol,
             const OEChem:: OEMolBase& refConstraintMol,
             const std::vector<std::string>& siteResidues,
             const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowrefPred=OEChem::OEIsTrueAtom())
```

Sets up the reference molecule, constraint molecule, or site residues if given. A predicate (refPred) can be passed to subset the reference. If the reference is given as an OEDesignUnit object, then the constraint molecule (ligand) and the site residues will be set if such information is available in the design unit. The function returns true if the setup is successful.

### **SetMethod**

bool SetMethod (unsigned value)

Sets the type of superposition to be performed. Types are taken from the constants given in OESuperposeMethod.

Note: This switches the method used during superposition, but not the default, user defined, valid RMSD, seqScore, or Tanimoto values. This means switching between a shape and sequence based method requires the user to explicitly set proper values for these or, alternatively, reconstruct the class with a new method.

### **Superpose**

```
bool Superpose (OESuperposeResults& results,
               const OEChem:: OEMolBase& fitMol,
               const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowfitPred=OEChem::OEIsTrueAtom()) const
bool Superpose (OESuperposeResults& results,
               const OEChem:: OEMolBase& fitMol,
               const OEChem:: OEMolBase& fitConstraintMol,
               const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
→fitPred=OEChem::OEIsTrueAtom()) const
bool Superpose (OESuperposeResults& results,
               const OEBio:: OEDesignUnit& fitDU,
               const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowfitPred=OEChem::OEIsTrueAtom()) const
```

Superimposes the fit molecule onto the reference. A predicate (fitPred) can be passed to subset the reference. The results for the superposition will be stored in results. The function returns results. IsValid().

# 5.1.24 OESuperposeOptions

Attention: This API is currently available in C++ and Python.

```
class OESuperposeOptions
```

This class represents OESuperposeOptions that sets the optional parameters for structural superposition using the OESuperpose class.

#### See also:

- OESuperpose class
- OEStructuralSuperposition class
- OESecondaryStructureSuperposition class

#### **Code Example**

• Calculating superposition example

#### **Constructors**

OESuperposeOptions (const unsigned method = OESuperposeMethod:: Default)

#### Default constructor.

OESuperposeOptions (const OESuperposeOptions & rhs)

Copy constructor.

#### operator=

OESuperposeOptions & operator=(const OESuperposeOptions & argOpts)

Assignment operator.

# 5.1.25 GetMethod

unsigned GetMethod() const

Returns the type of superposition to be performed. Types are given from the constants given in OESuperposeMethod. The default type is Default.

# 5.1.26 SetMethod

bool SetMethod (unsigned value)

Sets the type of superposition to be performed. Types are taken from the constants given in OESuperposeMethod.

# 5.1.27 GetUseConstraints

unsigned GetUseConstraints () const

Returns whether or not ligand or site-residue constraints should be used to validate the superposition.

See also:

- SetUseConstraints method
- SetupRef method
- Superpose method

# 5.1.28 SetUseConstraints

**bool** SetUseConstraints (*unsigned value*)

Sets whether or not ligand or site-residue constraints should be used to validate the superposition.

See also:

- SetUseConstraints method
- SetupRef method
- Superpose method

# 5.1.29 GetValidRMSD

double GetValidRMSD() const

Returns the RMSD threshold for validating the superposition of the reference and fit molecules. OESuperposeResults. IsValid returns false if the RMSD of the superposed molecules exceeds this threshold. The default value is 10.0 Angstroms for sequence-based methods and -1.0 for shape-based methods (RMSD calculation is only applicable to sequence-based methods).

See also:

- SetValidRMSD method
- IsValid method
- GetRMSD method

# 5.1.30 SetValidRMSD

**bool** SetValidRMSD (double value)

Sets the RMSD threshold for validating the superposition of the reference and fit molecules.

**Warning:** RMSD calculation is only applicable to sequence-based methods. Please avoid using this function when running shape-based superposition.

#### See also:

• SetValidRMSD method

# 5.1.31 GetValidTanimoto

```
double GetValidTanimoto() const
```

Returns the Tanimoto threshold for validating the superposition of the reference and fit molecules. OESuperposeResults. IsValid returns false if the Tanimoto of the superposed molecules is smaller than this threshold. The default value is 0.0 for shape-based methods and -1.0 for sequence-based methods (Tanimoto calculation is only applicable to shape-based methods).

### See also:

- SetValidTanimoto method
- IsValid method
- GetTanimoto method

# 5.1.32 SetValidTanimoto

**bool** SetValidTanimoto (double value)

Sets the Tanimoto threshold for validating the superposition of the reference and fit molecules.

Warning: Tanimoto calculation is only applicable to shape-based methods. Please avoid using this function when running sequence-based superposition.

See also:

• GetValidRMSD method

# 5.1.33 GetValidSeqScore

int GetValidSeqScore() const

Returns the sequence alignment score threshold for validating the superposition of the reference and fit molecules. OESuperposeResults. IsValid returns false if the sequence alignment score of the superposed molecules is smaller than this threshold. The default value is 200 for sequence-based methods and -1000 for shape-based methods (sequence alignment score is only applicable to sequencebased methods).

### See also:

- SetValidSegScore method
- IsValid method
- GetSeqScore method

# 5.1.34 SetValidSeqScore

bool SetValidSeqScore(int value)

Sets the sequence alignment score threshold for validating the superposition of the reference and fit molecules.

Warning: sequence alignment score is only applicable to sequence-based methods. Please avoid using this function when running shape-based superposition.

### See also:

• GetValidRMSD method

# 5.1.35 OESuperposeResults

Attention: This API is currently available in C++ and Python.

class OESuperposeResults

This class stores superposition results generated by OESuperpose.

#### See also:

• OESuperpose class

### **Code Example**

• Calculating superposition example

### **Constructors**

OESuperposeResults();

### Default constructor.

```
OESuperposeResults (const OESuperposeResults& rhs);
```

#### Copy constructor.

```
OESuperposeResults (OESuperposeResults&&);
```

#### Move constructor.

#### operator=

OESuperposeResults& operator=(const OESuperposeResults& rhs) ;

Assignment operator.

#### operator bool

operator bool() const

Returns true if the superposition is valid and false if not, which can be also obtained by calling IsValid.

#### See also:

• IsValid method

### **IsValid**

bool IsValid() const

Returns true if the superposition is valid and false if not. The superposition is valid if the scores (RMSD, Tanimoto, and sequence alignment score) satisfy the thresholds set in the OESuperposeOptions class.

See also:

- GetValidRMSD method
- GetValidTanimoto method
- GetValidSeqScore method

## **Transform**

```
bool Transform (OEChem:: OEMolBase& mol) const;
bool Transform (OEBio:: OEDesignUnit& du) const;
```

Returns true and transforms the input molecule using the stored transform from the superposition if they are valid. Otherwise, the function does nothing and returns false.

#### See also:

- OETrans class
- GetTransform method

### **GetTransform**

OEChem:: OETrans& GetTransform() const

Returns the OETrans object that stores the rotation matrix and translation vector from the superposition.

### See also:

- OETrans class
- Transform method
- GetRotMatrix method
- GetTranslation method

### **GetRotMatrix**

bool GetRotMatrix (double \*rmat) const;

Returns by reference the rotation matrix of the superposition.

# **GetTranslation**

bool GetTranslation (double \*trans) const;

Returns by reference the translation vector of the superposition.

### **HasRMSD**

bool HasRMSD() const

Returns whether RMSD was calculated for the superposed molecules. RMSD is only applicable to sequence-based methods, such as Global, Site, DDM, and Weighted.

#### **HasTanimoto**

bool HasTanimoto() const

Returns whether Tanimoto was calculated for the superposed molecules. Tanimoto is only applicable to shape-based methods, such as SSE.

### **HasSeqScore**

bool HasSeqScore() const

Returns whether sequence alignment score was calculated for the superposed molecules. sequence alignment score is only applicable to sequence-based methods, such as Global, Site, DDM, and Weighted.

### **GetRMSD**

double GetRMSD() const

Returns the RMSD of the structural superposition.

### **GetTanimoto**

double GetTanimoto() const

Returns the Tanimoto of the structural superposition.

#### **GetSeqScore**

double GetSeqScore() const

Returns the sequence alignment score of the structural superposition. The score is calculated by summing the similarity scores of matched residues and gap penalties.

# **GetRefChains**

const std::vector<std::string>& GetRefChains() const

Returns 1-letter code of all names of reference protein chains.

#### See also:

• GetFitChains method

## **GetFitChains**

const std::vector<std::string>& GetFitChains() const

Returns 1-letter code of all names of fit protein chains.

### See also:

• GetRefChains method

# 5.1.36 OEValidateDesignUnit

Attention: This API is currently available in C++ and Python.

class class OESPRUCE\_API OEValidateDesignUnit

This class represents OEValidateDesignUnit that performs a structural check afte running spruce prep

## **Constructors**

OEValidateDesignUnit();

Default constructor for OEValidateDesignUnit class

OEValidateDesignUnit (const OEValidateDesignUnit& rhs);

Copy constructor.

#### operator=

OEValidateDesignUnit& operator=(const OEValidateDesignUnit& rhs);

Assignment operator.

### **Validate**

unsigned Validate (OEBio:: OEDesignUnit& du) ;

Returns a code which indicates the issues that are detected for this structure

### **GetMessages**

std::string GetMessages(const unsigned errorTypes = OEDesignUnitIssueCodes::ALL);

Returns the error message according to the provided error code

## **GetAtoms**

```
std::vector<OEChem::OEResidue> GetProblematicResidues(const unsigned errorTypes =
\rightarrowOEDesignUnitIssueCodes::ALL);
```

Returns the problematic residues that have the issues indicated by the input error code

# **5.2 OESpruce Constants**

# 5.2.1 OEAIternateLocationOption

Attention: This API is currently available in C++ and Python.

This namespace contains methods to enumerate the alternate locations of a biomolecular structure.

## **Combinatorial**

Make all possible combinations of enumerated alternate locations.

#### **Default**

Enumerate is the default option.

# **Enumerate**

Enumerate through all possible alternate locations.

### **Primary**

Use only the primary (highest occupancy) alternate location.

## **Unknown**

The alternate location method has not been set.

### **Max**

# 5.2.2 OEDesignUnitIssueCodes

Attention: This API is currently available in C++ and Python.

This namespace contains constants for Spruce filter issue codes.

#### See also:

• The OEMakeDesignUnitOptions class.

### **Success**

This issue code indicates that the design unit does not have errors.

## **PartialSideChain**

This issue code indicates that the design unit contains partial side chains.

## **MissingLoop**

This issue code indicates that the input design unit contains missing loops.

## **ImplicitH**

This issue code indicates that the input design unit contains implicit hydrogens.

### **TerminiNotCapped**

This issue code indicates that the input design unit contains incorrect terminal residues.

### **HeavyAtomsOverlap**

This issue code indicates that the design unit has heavy atoms overlapping with each other.

### **BrokenChains**

This issue code indicates the design unit contains broken chains.

### **All**

This issue code indicates that the design unit contains all the issues listed above.

# 5.2.3 OEExperimentType

Attention: This API is currently available in C++ and Python.

This namespace contains constants that describe the type of experiment from which the 3-D structure was determined.

# ElectronCrystallography

The structure was determined by X-ray crystallography.

### **ElectronMicroscopy**

The structure was determined by electron cryo-microscopy.

# **FiberDiffraction**

The structure was determined by fiber diffraction using either X-rays, electrons, or neutrons.

### **NeutronDiffraction**

The structure was determined by elastic neutron scattering.

## **PowderDiffraction**

The structure was determined by powder diffraction using either X-rays, electrons, or neutrons.

### **SolidStateNMR**

The structure was determined by NMR methods in the solid state.

### **SolutionNMR**

The structure was determined by NMR methods in the liquid state.

### **SolutionScattering**

The structure was determined by small angle X-ray scattering (SAXS) in solution.

# **TheoreticalModel**

The structure was predicted/computed using a theoretical/computational model.

### **Unknown**

The experiment type is not known.

# **XRayDiffraction**

The structure was determined using X-ray diffraction.

# 5.2.4 OEHeterogenType

Attention: This API is currently available in C++ and Python.

This namespace contains constants that define the heterogen molecule type used in the OEHeterogenMetadata class.

## **Cofactors**

The heterogen type are cofactors.

## **Counterlons**

The heterogen type are counter ions.

### **Excipients**

The heterogen type are excipients.

## **Ligand**

The heterogen type is a ligand.

# **Lipids**

The heterogen types are lipids.

## **Metals**

The heterogen type are metals.

# **Polymers**

The heterogen type are polymeric molecules.

## **Solvent**

The heterogen type are solvent molecules.

### **Sugars**

The heterogen type are sugars.

### **Unknown**

The heterogen type are not known.

# 5.2.5 OESuperpositionType

Attention: This API is currently available in C++ and Python.

This namespace contains constants for superpositioning methods.

### See also:

• OESuperpositionOptions class

## **Default**

The default superpositioning method is OESuperpositionType\_Global.

## **DDM**

Calculate superposition using the Distance Difference Matrix method.

## Global

Calculate superposition using the all matched atoms.

### **Site**

Calculate superposition using the input site residues. Site residues must be set with the OESuperpositionOptions. SetSiteResidues member function of the OESuperpositionOptions class.

### **SSE**

Calculate superposition using an overlap of Secondary Structure Elements.

## See also:

• OESecondaryStructureSuperposition class

## **Undefined**

Superposition method is undefined. No superposition will take place.

### Weighted

Calculate a weighted superposition using weights taken from the Difference Distance Matrix.

# 5.2.6 OESpruceFilterIssueCodes

Attention: This API is currently available in C++ and Python.

This namespace contains constants for Spruce filter issue codes.

### See also:

• OESpruceFilterOptions class

### **Success**

This issue code indicates that the input structure does not have errors and passes the spruce filter

### **InvalidNames**

This issue code indicates that the input structure contains invalid names.

### **InvalidResidueStates**

This issue code indicates that the input structure contains residues at invalid state.

### **InvalidMetalBond**

This issue code indicates that the input structure contains invalid covalent bonds to metals.

### **InvalidCRYST1**

This issue code indicates that the input structure does not have a valid CRYST1 header.

### **InvalidElectronDensityOverlap**

This issue code indicates that the provided electron density map does not overlap with the input structure

## **InvalidSeqAlign**

This issue code indicates that the sequence does not align with the input structure.

### **All**

This issue code indicates that the structure contains all the issues listed above.

# 5.2.7 OESuperposeMethod

Attention: This API is currently available in C++ and Python.

This namespace contains constants for superpositioning methods.

#### See also:

• OESuperposeOptions class

### **Code Example**

• Calculating superposition example

### **Default**

The default superpositioning method is GlobalCarbonAlpha.

### GlobalCarbonAlpha

Calculate superposition using the all matched alpha carbon atoms.

### **Global**

Alias for Global.

### **SiteSequence**

Calculate superposition using the input site residues. Site residues must be set with the OESuperpose. SetupRef member function of the OESuperpose class.

### **Site**

Alias for SiteSequence.

## **DifferenceDistanceMatrix**

Calculate superposition using the Distance Difference Matrix method. See Protein Superposition for more information.

### **DDM**

Alias for DifferenceDistanceMatrix.

### WeightedDifferenceDistanceMatrix

Calculate a weighted superposition using weights taken from the Difference Distance Matrix. See Protein Superposition for more information.

### Weighted

Alias for WeightedDifferenceDistanceMatrix.

### **SecondaryStructureElements**

Calculate superposition using an overlap of Secondary Structure Elements.

### See also:

• OESecondaryStructureSuperposition class

# **SSE**

Alias for SecondaryStructureElements.

### **SiteHopper**

Calculates the superposition using SiteHopper

### See also:

• Introduction

### **Undefined**

Superposition method is undefined. No superposition will take place.

# **5.3 OESpruce Functions**

# 5.3.1 OEBuildLoops

Attention: This API is currently available in C++ and Python.

These functions build missing loops and tails in protein structures. They return false if any of the loops or tails cannot be built, but it will return with as many built loops and tails as possible. The functions require a loop database be provided in the options class. Using the **loopdb\_builder** application it is possible to build your own database for a given target family, or a set of proprietary structure. OpenEye provides a database built of the structures in the entire PDB repository at the time of toolkit release. The datastamps are noted in the info table and logged during loop building. It is possible to append local/proprietary structures to this database if desired, again using the desktop application. The options class allows different behaviors for the loop builder.

Note: Explicit hydrogens are not added to the structure during the build processes, therefore no partial charges are assigned.

```
bool OEBuildLoops (OEChem:: OEMolBase& mol,
                        const OESidechainBuilderOptions&
\rightarrowscOpts=OESidechainBuilderOptions(),
                        const OELoopBuilderOptions& lOpts=OELoopBuilderOptions())
```

This function takes a molecule and builds any missing loops that can be detected based on the information in the PDB header metadata. The function also takes options classes for the loop building, but also for the side-chain re-building, in case the loop in the database is not a 100% identity match. The function calls OEOmega to generate possible conformations for tails.

```
bool OEBuildLoops (OEChem:: OEMolBase& mol,
                        const OEStructureMetadata& data,
                        const OESidechainBuilderOptions&
\rightarrowscOpts=OESidechainBuilderOptions(),
                        const OELoopBuilderOptions& lOpts=OELoopBuilderOptions())
```

This function works identically to the above function, only metadata is explicitly provided containing information about the sequence, so gaps can be detected.

### See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitBuildOptions class
- OELoopBuilderOptions class
- OESidechainBuilderOptions class
- · OERotamerLibrary namespace
- OEStructureMetadata class
- · OEBuildSingleLoop function

# 5.3.2 OEBuildSidechains

**Attention:** This API is currently available in C++ and Python.

These functions build out partial side chains using a rotamer library. The rotamer chosen is the one with the best interaction energy with the surrounding environment without taking solvent effects into account. If multiple sidechains are built that interact with one another, the energy chosen is the best collective interaction energy. The functions will return false if a sidechain can not be built due to clashes, but will still return a structure with all the ones it could build.

Note: Explicit hydrogens are not added to the structure during the build processes, therefore no partial charges are assigned.

```
bool OEBuildSidechains (OEChem:: OEMolBase &mol,
                       const OESpruce:: OESidechainBuilderOptions&
→opts=OESpruce::OESidechainBuilderOptions())
```

This function takes a molecule and builds any partial sidechain of standard protein residues determined using the OEGetPartialResidues function. An options class defining a rotamer library from the OERotamerLibrary namespace can be set, otherwise the default library from that namespace is chosen. Additionally, in the options the number of rotamers used can be reduced by picking a rotamer coverage below the default 100%. The percentage is calculated cumulatively, so the most probably rotamer is tested first, up to the rotamer that takes it above the percentage limit. The options class also defines the behavior of removing water molecules that clash with the built sidechain.

```
bool OEBuildSidechains (OEChem:: OEMolBase &mol,
                       const std::vector<OEChem::OEResidue> residues,
                       const OESpruce:: OESidechainBuilderOptions&
→opts=OESpruce::OESidechainBuilderOptions())
```

This function works identically to the above function, but only builds the residues identified in the vector residues.

See also:

- OESidechainBuilderOptions class
- · OERotamerLibrary namespace
- OEGetPartialResidues function

# 5.3.3 OEBuildSingleLoop

**Attention:** This API is currently available in C++ and Python.

This function builds a specified missing loop or tail in a protein structures. The function returns false if the loop or tail cannot be built. The function requires a loop database be provided in the options class. Using the **loopdb\_builder** application it is possible to build your own database for a given target family, or a set of proprietary structure. OpenEye provides a database built of the structures in the entire PDB repository at the time of toolkit release. The datastamps are noted in the info table and logged during loop building. It is possible to append local/proprietary structures to this database if desired, again using the desktop application. The options classes allows different behaviors for the loop builder.

Note: Explicit hydrogens are not added to the structure during the build processes, therefore no partial charges are assigned.

```
bool OEBuildSingleLoop (OEChem:: OEMCMolBase& outputMol,
                             const OEChem:: OEMolBase& inputMol,
                             const std:: string fasta,
                             const OEChem:: OEResidue& cTerminalAttachment,
                             const OEChem:: OEResidue& nTerminalAttachment,
                             const OESidechainBuilderOptions&
\rightarrowscOpts=OESidechainBuilderOptions(),
                             const OELoopBuilderOptions& lOpts=OELoopBuilderOptions());
```

The function takes an empty multi-conformer molecule which will contain the protein with the loop built if the function is successful. Multiple conformers of the loop will be returned based on the passed options, the results are sorted by a force field energy score. The remaining arguments are, the molecule with the gap, the loop protein sequence in 1-letter codes as a string (e.g. "PVHTAL"), and the c- and n-terminal attachment (or anchor) residues. The function also takes options classes for the loop building, and side-chain re-building, in case the loop in the database is not a 100% identity match. The function calls OEOmega to generate possible conformations for tails.

## See also:

- OEMakeDesignUnitOptions class
- OEDesignUnitPrepOptions class
- OEDesignUnitBuildOptions class
- OELoopBuilderOptions class
- OESidechainBuilderOptions class
- · OERotamerLibrary namespace
- OEStructureMetadata class

### • OEBuildLoops function

# 5.3.4 OECapCTermini

Attention: This API is currently available in C++ and Python.

```
bool OECapCTermini (OEChem:: OEMolBase &mol,
                     const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
\rightarrowexclude=OEChem::OEIsFalseAtom(),
                     const OESpruce:: OECapBuilderOptions& =
\rightarrowOESpruce::OECapBuilderOptions())
```

This function caps all the C-termini in a protein with an N-methyl (OEResidueIndex\_NME) group. The N-methyl is built assuming ideal backbone geometry.

A predicate can be passed to exclude certain termini from being capped, such as the true biological C-terminal residue since this should be charged to match the biophysical experiments.

The function takes an options class, where behavior can be controlled if building the cap results in a clash, and depending on the type of class what actions can be taken, e.g. a solvent molecule blocking the protein backbone is not very realistic and the solvent molecule is likely placed to account for density that should have belonged to the residue not resolved in the crystal structure.

The cap will be numbered identically to the residue number of the terminal residue, but the insertion code will be incremented. The reason for this is to avoid residue number clashes with heterogens following the protein chain in the PDB file.

Note: If the backbone of the residue being capped is incomplete, or a cap can not be built because of a clash, the residue being capped can be turned into the cap by removing atoms in the residue. A clash can either be into a non-solvent or into a solvent with the *deleteClashingSolvent* option set to false.

#### See also:

- OECapBuilderOptions class
- · OECapTermini function
- · OECapNTermini function
- OEIsCTerminalAtom predicate

# 5.3.5 OECapNTermini

Attention: This API is currently available in C++ and Python.

```
bool OECapNTermini (OEChem:: OEMolBase &mol,
                     const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
\rightarrowexclude=OEChem::OEIsFalseAtom(),
                     const OESpruce:: OECapBuilderOptions& =
\rightarrow OESpruce:: OECapBuilderOptions())
```

This function caps all the N-termini in a protein with an acetyl (OEResidueIndex ACE) group. The acetyl is built assuming ideal backbone geometry, the  $\phi$  value of the residue being capped is set to match the  $\phi$  value of the previous residue (if it's a single residue in space, a value of  $-90.0^{\circ}$  degrees, is set which is in the allowed range for both an alpha helix and beta sheet secondary structure).

A predicate can be passed to exclude certain termini from being capped, such as the true biological N-terminal residue since this should be charged to match the biophysical experiments.

The function takes an options class, where behavior can be controlled if building the cap results in a clash, and depending on the type of class what actions can be taken, e.g. a solvent molecule blocking the protein backbone is not very realistic and the solvent molecule is likely placed to account for density that should have belonged to the residue not resolved in the crystal structure.

The cap will be numbered with -1 from the residue number of the terminal residue.

Note: If the backbone of the residue being capped is incomplete, or a cap can not be built because of a clash, the residue being capped can be turned into the cap by removing atoms in the residue. A clash can either be into a non-solvent or into a solvent with the *deleteClashingSolvent* option set to false.

### See also:

- OECapBuilderOptions class
- · OECapTermini function
- OECapCTermini function
- OEIsNTerminalAtom predicate

# 5.3.6 OECapTermini

Attention: This API is currently available in C++ and Python.

```
bool OECapTermini (OEChem:: OEMolBase &mol,
                    const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
\rightarrowexclude=OEChem::OEIsFalseAtom(),
                    const OESpruce:: OECapBuilderOptions& =
\rightarrow OESpruce:: OECapBuilderOptions())
```

This function caps all the N- and C-termini in a protein with acetyl (OEResidueIndex ACE) and N-methyl (OEResidueIndex\_NME) groups, respectively.

A predicate can be passed to exclude certain termini from being capped, such as the true biological terminal residues since these should be charged to match the biophysical experiments.

The function takes an options class, where behavior can be controlled if building the cap results in a clash, and depending on the type of class what actions can be taken, e.g. a solvent molecule blocking the protein backbone is not very realistic and the solvent molecule is likely placed to account for density that should have belonged to the residue not resolved in the crystal structure.

**Note:** Explicit hydrogens are not added to the structure during the build processes.

See also:

- OECapBuilderOptions class
- OECapCTermini function
- · OECapNTermini function
- OEIsNTerminalAtom predicate
- OEIsCTerminalAtom predicate

# 5.3.7 OEEnumerateSites

**Attention:** This API is currently available in C++ and Python.

```
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEEnumerateSites(const OEBio::OEDesignUnit &bioDesignUnit,
                    const OEDesignUnitEnumerateSitesOptions &
\rightarrowopts=OEDesignUnitEnumerateSitesOptions(),
                    const std:: string siteResidue="")
OESystem::OEIterBase<OEBio::OEDesignUnit> *
  OEEnumerateSites(const OEBio::OEDesignUnit &bioDesignUnit,
                    const OESystem:: OESkewGrid &electronDensity,
                    const OESpruce:: OEDesignUnitEnumerateSitesOptions &
\rightarrow opts=0ESpruce:: 0EDesignUnitEnumerateSitesOptions())
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEEnumerateSites(const OEBio::OEDesignUnit &bioDesignUnit,
                    const OEBio:: OEDesignUnit & designUnitReference,
                    const OESpruce:: OEDesignUnitEnumerateSitesOptions &
\rightarrow opts=0ESpruce:: 0EDesignUnitEnumerateSitesOptions())
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEEnumerateSites(const OEBio::OEDesignUnit &bioDesignUnit,
                    const OEBio:: OEDesignUnit & designUnitReference,
                    const OESystem:: OESkewGrid &electronDensity,
                    const OESpruce:: OEDesignUnitEnumerateSitesOptions &
\rightarrowopts=OESpruce::OEDesignUnitEnumerateSitesOptions(),
                    const std:: string siteResidue="")
```

Return an iterator over all OEDesignUnit objects that can be produced from the input bioDesignUnit argument, which based on the componentization of the internal heterogen molecules. The *bioDesignUnit* input argument should be taken from the iterator output of *OEMakeBioDesignUnits*.

# 5.3.8 OEExtractBioUnits

**Attention:** This API is currently available in C++ and Python.

```
OESystem:: OEIterBase<OEChem:: OEMolBase>*
               OEExtractBioUnits (const OEChem:: OEMolBase& extractProtein,
                                  const OEChem:: OEMolBase& refProtein,
                                  const OEBioUnitExtractionOptions
\rightarrow opts=OEBioUnitExtractionOptions())
```

```
OESystem:: OEIterBase<OEChem:: OEMolBase>*
               OEExtractBioUnits(const OEChem:: OEMolBase& extractProtein,
                                  const OEBioUnitExtractionOptions
\rightarrow opts=OEBioUnitExtractionOptions())
```

Extracts BUs using either the PDB remarks when a single OEMolBase is provided, or a sequence alignment to a reference if two OEMolBases are provided. The OEExtractBioUnits is overloaded with to take an OEBioUni*tExtractionOptions* options class. This function returns an iterator of OEMolBase objects, one for each of the BUs.

Note: If atoms are on the symmetry axis causing them to be duplicated by symmetry expansion, they are handled specially to avoid clashes in the output. If the duplication results in atoms of a molecule that are perfectly overlapping, e.g. a water molecule oxygen, then the duplicated water is deleted. If the overlap is not complete, but instead creates partially overlapping molecules, then the BU is enumerated into multiple BUs. The nearly identical BUs are tagged in generic data with an index number used by Spruce.

### Parameters .

extractProtein The protein from which the BUs will be extracted.

*refProtein* The reference protein that will be used for sequence alignment.

**OEBioUnitExtractionOptions** OEBioUnitExtractionOptions options class defining biological unit extraction options.

### **Code Example**

- Extracting Biounits by aligning to a reference protein example
- Extracting Biounits from PDB header remarks example

# 5.3.9 OEFindPockets

**Attention:** This API is currently available in C++ and Python.

```
OESystem:: OEIterBase<OESpruce:: OEPocket> *
 OEFindPockets (OEBio:: OEDesignUnit& designUnit,
                     const unsigned
→componentMask=OEBio::OEDesignUnitComponents::Protein|OEBio::OEDesignUnitComponents::Nucleic|OEBio:
\leftrightarrowconst OEPocketOptions& opts=OESpruce::OEPocketOptions(),
                     const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&..
\rightarrowrestrictPred=OESystem::OEIsTrue<OEChem::OEAtomBase>())
OESystem:: OEIterBase<OESpruce:: OEPocket> *
 OEFindPockets (OEChem:: OEMolBase& mol,
                     const OEPocketOptions& opts=OESpruce::OEPocketOptions(),
                     const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowrestrictPred=OESystem::OEIsTrue<OEChem::OEAtomBase>())
```

Return an iterator over all OEPocket objects that can be found from the input OEMolBase or OEDesignUnit input structure. For design units, a mask can be supplied to determine, which of the internal components should be used for the pocket detection. The options input defines some parameters of the output pockets. If a specific pocket is required an atom based predicate can be supplied, the requirement is then that the one of the atom(s) in the predicate, is associated with the surface of the discovered pocket.

### See also:

- OEPocketOptions class
- OEPocket class
- OEMakeDesignUnitFromPocket function

# 5.3.10 OEFixBackbone

Attention: This API is currently available in C++ and Python.

bool OEFixBackbone (OEBio:: OEDesignUnit& du)

The function attempts to correct missing oxygen atoms on the protein backbone, O and OXT, as well as correct the charge and valence state. If any of the core backbone atoms, N, CA, or C are missing it removes the residue. The proper residue can be modeled in later using OEBuildLoops.

# 5.3.11 OEGetAlternateLocationOptionID

Attention: This API is currently available in C++ and Python.

unsigned OEGetAlternateLocationOptionID (std::string optionName)

Returns the unsigned integer version of the string option name from the OEAlternateLocationOption namespace.

# 5.3.12 OEGetAlternateLocationOptionName

Attention: This API is currently available in C++ and Python.

std::string OEGetAlternateLocationOptionName(unsigned option)

Returns the string version of the option name from the OEAlternateLocationOption namespace.

# 5.3.13 OEGetExperimentTypeID

Attention: This API is currently available in C++ and Python.

unsigned OEGetExperimentTypeID (const std:: string &expTypeName)

This function returns an unsigned integer version of the experiment type from the string argument expTypeName. The experiment types are contained in the  $OEExperiment\,Type$  namespace.

# 5.3.14 OEGetExperimentTypeName

Attention: This API is currently available in C++ and Python.

std::string OEGetExperimentTypeName(unsigned expTypeID)

This function returns a string version of the experiment type from the unsigned integer argument  $expTypeID$ . The experiment types are contained in the  $OEExperiment$   $Type$  namespace.

# 5.3.15 OEGetHeterogenTypeID

**Attention:** This API is currently available in C++ and Python.

unsigned OEGetHeterogenTypeID (const std::string& typeName)

This function returns an unsigned integer version of the heterogen type from the string argument typeName. The heterogen types are contained in the OEHeterogenType namespace.

# 5.3.16 OEGetHeterogenTypeName

**Attention:** This API is currently available in C++ and Python.

std::string OEGetHeterogenTypeName(unsigned typeID)

This function returns a string version of the heterogen type from the unsigned integer argument typeID. The heterogen types are contained in the  $OEHeterogenType$  namespace.

# 5.3.17 OEGetPartialResidues

Attention: This API is currently available in C++ and Python.

```
bool OEGetPartialResidues(std::vector<OEChem::OEResidue> &partialResidues,
                          const OEChem:: OEMolBase & mol)
```

This function looks through the molecule and generates a list of standard protein residues with partial sidechains, which can then be passed to OEBuildSidechains

#### See also:

• OEBuildSidechains function

# 5.3.18 OEMakeBioDesignUnits

Attention: This API is currently available in C++ and Python.

```
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEMakeBioDesignUnits(const OEChem:: OEMolBase & structure,
                       const OESpruce:: OEStructureMetadata &
→metadata=OESpruce::OEStructureMetadata(),
                       const OESpruce:: OEMakeDesignUnitOptions &
→opts=OESpruce::OEMakeDesignUnitOptions())
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEMakeBioDesignUnits(const OEChem:: OEMolBase & structure,
                       const OEBio:: OEDesignUnit & designUnitReference,
                       const OESpruce:: OEStructureMetadata &
→metadata=OESpruce::OEStructureMetadata(),
                       const OESpruce:: OEMakeDesignUnitOptions &
→opts=OESpruce::OEMakeDesignUnitOptions())
```

Return an iterator over all OEDesignUnit objects that can be produced from the input OEMolBase structure. A reference structure to be used for biounit extraction and structural superposition can be passed in through the *desig*nUnitReference argument, while information regarding the experimental data as well as basic options for constructing the design units themselves can be provided through the *metadata* and *opts* arguments, respectively.

Note: Note: We strongly recommend running OESpruceFilter for standardization and filtering prior to running the design unit preparation

### See also:

• OEMakeDesignUnit, and OESpruceFilter

# 5.3.19 OEMakeDesignUnit

**Attention:** This API is currently available in C++ and Python.

```
bool OEMakeDesignUnit (OEBio:: OEDesignUnit &du,
                        const OEChem:: OEMolBase & nonLigandComplex,
                        const OEChem:: OEMolBase & ligand,
                        const OESpruce:: OEMakeDesignUnitOptions &
\rightarrowopts=OESpruce::OEMakeDesignUnitOptions())
```

Constructs and populates an input OEDesignUnit object (du) from the input, a nonLigandComplex (typically a protein or DNA) and a ligand. An options OEMakeDesignUnitOptions object can be passed in to control the behavior during design unit preparation.

Note: Note: We strongly recommend running OESpruceFilter for standardization and filtering prior to running the design unit preparation.

Note: The function will construct an OED esignUnit  $(du)$ , where the system's molecules have been binned into categories given by the OEDesignUnitComponents namespace. Although an OEDesignUnitComponents\_Metals category exists, depending on the proximity of the metal to the design unit's binding site, the metal may be contained in either the OEDesignUnitComponents\_Cofactors category if it falls within a cutoff to the binding site, or in the OEDesignUnitComponents\_Metals category if not.

### **Code Example**

• Creating OEDesignUnits from a PDB file example

#### See also:

• OEMakeDesignUnitOptions, OEMakeBioDesignUnit, and OESpruceFilter

# 5.3.20 OEMakeDesignUnits

**Attention:** This API is currently available in C++ and Python.

```
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEMakeDesignUnits (const OEChem:: OEMolBase & structure,
                    const OESpruce:: OEStructureMetadata &
→metadata=OESpruce::OEStructureMetadata(),
                    const OESpruce:: OEMakeDesignUnitOptions &
→opts=OESpruce::OEMakeDesignUnitOptions(),
                    const std:: string siteResidue="")
OESystem::OEIterBase<OEBio::OEDesignUnit> *
  OEMakeDesignUnits (const OEChem:: OEMolBase &structure,
                    const OESystem:: OESkewGrid &electronDensity,
                    const OESpruce:: OEStructureMetadata &
 →metadata=OESpruce::OEStructureMetadata(),
```

```
const OESpruce:: OEMakeDesignUnitOptions &
→opts=OESpruce::OEMakeDesignUnitOptions(),
                    const std:: string siteResidue="")
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEMakeDesignUnits (const OEChem:: OEMolBase & structure,
                     const OEBio:: OEDesignUnit & designUnitReference,
                     const OESpruce:: OEStructureMetadata &
\rightarrowmetadata=OESpruce::OEStructureMetadata(),
                     const OESpruce:: OEMakeDesignUnitOptions &
→opts=OESpruce::OEMakeDesignUnitOptions()
                    const std:: string siteResidue="")
OESystem:: OEIterBase<OEBio:: OEDesignUnit> *
  OEMakeDesignUnits (const OEChem:: OEMolBase &structure,
                     const OESystem:: OESkewGrid &electronDensity,
                     const OEBio:: OEDesignUnit & designUnitReference,
                     const OESpruce:: OEStructureMetadata &
→metadata=OESpruce::OEStructureMetadata(),
                     const OESpruce:: OEMakeDesignUnitOptions &
→opts=OESpruce::OEMakeDesignUnitOptions(),
                     const std:: string siteResidue="")
```

Return an iterator over all OEDesignUnit objects that can be produced from the input OEMolBase structure. A reference structure to be used for biounit extraction and structural superposition can be passed in through the *designUnitReference* argument, while information regarding the experimental data as well as basic options for constructing the design units themselves can be provided through the OEStructureMetadata (metadata), OESkewGrid (electronDensity) and OEMakeDesignUnitOptions (opts) arguments, respectively. The input option of providing a electron density map can be used to calculate Iridium score. For more information about the Iridium score, see Iridium chapter of that toolkit. The OEStructureMetadata class stores constants for use with OEFieldMeta. These attributes (e.g. symmetry) are used to construct DUs. There is an input option to specify a binding site using a single residue specification if apo (or holo). The format is "name:num:insert code:chainid", e.g. "ASP:25: :A" indicating Aspartic acid 25 in chain A. Note: A blank/whitespace character is used for the insert code, which is a typical use case.

Note: This function will return an iterator over OEDesignUnit pointers, where the system's molecules have been binned into categories given by the OEDesignUnitComponents namespace. Although an OEDesignUnitComponents\_Metals category exists, depending on the proximity of the metal to the design unit's binding site, the metal may be contained in either the OEDesignUnitComponents\_Cofactors category if it falls within a cutoff to the binding site, or in the OEDesignUnitComponents\_Metals category if not.

### **Code Example**

• Creating OEDesignUnits from a PDB file example

## See also:

• OEMakeDesignUnitOptions class

# 5.3.21 OEMakeDesignUnitFromPocket

Attention: This API is currently available in C++ and Python.

```
bool OEMakeDesignUnitFromPocket (OEBio:: OEDesignUnit& du,
                                 const OEBio:: OEDesignUnit& designUnit,
                                 const OESpruce:: OEPocket& pocket)
```

Takes an existing OEDesignUnit object (*designunit*) and generates a new OEDesignUnit object  $(du)$ , based on the input pocket. If the input designunit has a binding site defined, it will be reset in the output designunit (du) and switched to the site specified by the pocket.

```
bool OEMakeDesignUnitFromPocket (OEBio::OEDesignUnit& du,
                                 const OEChem:: OEMolBase& mol,
                                 const OESpruce:: OEPocket& pocket)
```

Takes an existing OEMolBase object (molecule) and generates a new OEDesignUnit object (du), based on the input pocket. The molecule is not split into components but is placed as the 'protein' component of the design unit.

### See also:

- OEPocket class
- OEFindPockets function
- OEMakeDesignUnits function
- · OEMakeBioDesignUnits function
- · OEMakeDesignUnit function

# 5.3.22 OEMutateResidue

**Attention:** This API is currently available in C++ and Python.

This function mutates a single standard protein residue in the molecule to another standard amino acid residue specified by the 3 letter residue name, it currently only supports the 20 standard amino acids. The function works by deleting the residue sidechain and rebuilds the new residue using the  $OEBuildSidechains$  function, but only building the mutated sidechain. The sidechain re-building can be controlled using the OESidechainBuilderOptions options class argument opts.

Note: Explicit hydrogens are not added to the structure during the build processes, therefore no partial charges are assigned.

```
bool OEMutateResidue (OEChem:: OEMolBase &mol,
                       OEChem:: OEResidue &res,
                       const std:: string newResName,
                       const OESpruce:: OESidechainBuilderOptions&
\rightarrow opts=0ESpruce:: 0ESidechainBuilderOptions (true))
```

See also:

- · OEBuildSidechains function
- OESidechainBuilderOptions class

# 5.3.23 OEMutateResidues

Attention: This API is currently available in C++ and Python.

```
bool OEMutateResidues (OEChem:: OEMolBase& mol,
                      const std:: map<OEChem:: OEResidue, std:: string>& mutationMap,
                      const OESpruce:: OESidechainBuilderOptions&
→opts=OESpruce::OESidechainBuilderOptions(true));
```

This function takes an input OEMolBase (*mol*) and it mutates residues in the provided map. The sidechain re-building can be controlled using the OESidechainBuilderOptions options class argument opts.

See also:

- OEBuildSidechains function
- OESidechainBuilderOptions class

# 5.3.24 OEProtonateDesignUnit

**Attention:** This API is currently available in C++ and Python.

```
bool OEProtonateDesignUnit (OEBio:: OEDesignUnit &du,
                            const OESpruce:: OEProtonateDesignUnitOptions &
\rightarrow opts=0EProtonateDesignUnitOptions())
bool OEProtonateDesignUnit (OEBio:: OEDesignUnit &du,
                            std::map<std::string,
                            OEHeterogenMetadata> &metadata,
                            const OESpruce:: OEProtonateDesignUnitOptions &
→opts=OEProtonateDesignUnitOptions())
```

This function takes an input OEDesignUnit  $(du)$  and it intelligently places hydrogens across all internal molecular components. Optionally, one may pass in a OEHeterogenMetadata map keyed on the SMILES string for a given heterogen, as well as a set of general protonation options through the OEProtonateDesignUnitOptions argument, opts.

# 5.3.25 OESetPackingResidueProperties

Attention: This API is currently available in C++ and Python.

```
void OESetPackingResidueProperties (OEChem:: OEMolBase &packingMol,
                                  const std::vector<std::string> &existingChainIDs)
```

This function takes an input OEMolBase (packingMol) and a std::vector of chain ID strings (existingChainIDs), and applies them to the crystal packing molecule.

# 5.3.26 OESpruceGetArch

const char \*OESpruceGetArch()

Returns the architecture of the current version of the Spruce toolkit. Examples include:

- $\cdot$  microsoft-win32-x86
- Ubuntu-16.04- $x$ 64

# 5.3.27 OESpruceGetLicensee

**bool** OESpruceGetLicensee(std::string &licensee)

Returns the LICENSEE from the current valid Spruce TK license.

# 5.3.28 OESpruceGetPlatform

const char \*OESpruceGetPlatform()

Returns the platform, including compiler version, of the current version of the Spruce toolkit. Examples include:

- microsoft-win32-msvc9-MD-x86
- Ubuntu-16.04-x64

# 5.3.29 OESpruceGetRelease

const char \*OESpruceGetRelease()

Returns the version of this toolkit release. For example: 0.9.0.

# 5.3.30 OESpruceGetSite

```
bool OESpruceGetSite(std::string &site)
```

Returns the SITE from the current valid Spruce TK license.

# 5.3.31 OESpruceGetVersion

unsigned int OESpruceGetVersion()

Returns the build date of the toolkit as an unsigned int. For example: 20180126.

# 5.3.32 OESprucelsLicensed

bool OESpruceIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any Spruce TK functionality.

The 'feature' argument can be used to check for a valid license to **Spruce TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current **Spruce TK** license.

#### See also:

• OEChemIsLicensed function

# 5.3.33 OEGetSuperposeMethodFromName

**Attention:** This API is currently available in C++ and Python.

unsigned OEGetSuperposeMethodFromName (const std::string &name)

Returns the corresponding constant defined in the OESuperposeMethod namespace for the given superposition method name.

# 5.3.34 OEGetSuperposeMethodName

Attention: This API is currently available in C++ and Python.

std::string OEGetSuperposeMethodName(const unsigned method);

Returns the name of the superposition method as a string.

# **RELEASE HISTORY**

# **6.1 Spruce TK 1.6.1**

# 6.1.1 New features

- OEBuildSidechains now minimizes target side chains by default. Minimization can be controlled by setting minimizeSidechains and minimizeSidechainsShell options in the OESidechainBuilderOptions class.
- A feature has been added to support a next generation mmCIF feature, such that when an mmCIF file provides a connectivity record for the heterogens, **Spruce** will no longer look up the heterogen in the Chemical Component Dictionary but trust the input provided.
- A feature has been added that allows in-plane flipping of a single hydrogen on a double bonded nitrogen, when a clash is detected as part of hydrogen bond network optimization.

# 6.1.2 Major bug fixes

- An issue has been fixed related to using the OEHeterogenMetadata class, where the provided SMILES string was not respected for tautomer generation; when tautomers were not provided; and when the title (residue name) collided with existing residue names in the stored Chemical Component Dictionary.
- An issue has been fixed related to covalently bound ligands, where the pre-reaction input SMILES and related tautomers were not adjusted properly when accounting for the formed covalent bond.
- An issue has been fixed where the **Spruce** filter deleted single (disconnected) amino acid residues when they were marked HETATMs and were not real "floating" residues in part of the regular protein sequence.

# 6.1.3 Minor bug fixes

- · OEMutateResidues, OEMutateResidue, and OEBuildSidechains now reduce failures arising from clashes by using shell minimization by default.
- An issue has been fixed that caused HEME-like molecules to be excluded from the stored chemical component database.

# **6.1.4 Documentation changes**

• Information has been added about setting and getting minimizeSidechains and minimizeSidechainsShell options in the OESidechainBuilderOptions class.

# **6.2 Spruce TK 1.6.0**

# 6.2.1 New features

- The chemical components dictionary has been updated with latest structures from the wwPDB.
- A feature has been added to OEProtonateDesignUnit to detect acceptor-acceptor clashes, modify the protonation state of one of the moieties, and reoptimize the hydrogen bond network.
- The following preliminary API classes have been made permanent.
  - OECapBuilderOptions
  - OELoopBuilderOptions
  - $-$  OEPocket
  - OEPocketOptions
  - OESidechainBuilderOptions
  - OESpruceFilter
  - OESpruceFilterOptions
  - OEValidateDesignUnit
- The following preliminary API functions have been made permanent.
  - OEBuildLoops
  - OEBuildSingleLoop
  - OEFindPockets
  - OEMakeDesignUnitFromPocket

# 6.2.2 Major bug fixes

• A crash in *OESpruceFilter* has been fixed in relation to atoms that were cleaned up during the standardization process.

# 6.2.3 Minor bug fixes

• An issue has been fixed that ensures radii are assigned to all atoms in a design unit.

# **6.2.4 Documentation changes**

• An example has been added showing how to convert FASTA files to structure metadata for structures missing the SEQRES information in the PDB metadata and MMCIF equivalent.

# **6.3 Spruce TK 1.5.3**

# 6.3.1 New features

• The chemical components dictionary was updated with latest data from the RCSB.

# 6.3.2 Major bug fixes

• An issue that caused OESpruceFilter to segfault has been fixed and safeguarded.

# 6.3.3 Minor bug fixes

- An issue has been fixed that caused incorrectly built loops when the protein structure contains nonstandard amino acids, particularly in the gap needing to be built or anchoring to it.
- An issue with sequence mutation for cysteine residues, where an explicit hydrogen was left over after the mutation, has been fixed.

# **6.4 Spruce TK 1.5.2**

# 6.4.1 New features

- *OESpruceFilterOptions* has an option to automatically assign chain IDs (default is true) when they are missing either completely or partially in the structure for a structure processed by OESpruceFilter.
- The built-in heterogen database has been updated with the latest structures from the ligand-expo at the RCSB.

# 6.4.2 Major bug fixes

- An issue where tautomers passed using metadata were not respected has been fixed.
- An issue has been fixed where, in a small fraction of cases, an OXT atom was not correctly built out when needed at the protein C-terminals.
- An issue has been fixed where the option to fix the state of backbone atoms and bonds in OESpruceFilterOptions was sometimes not respected in OESpruceFilter, which led to issues such as OXT atoms being built even if the option was disabled.

# 6.4.3 Minor bug fixes

- An issue was fixed in filter options to not accept the disallowed residue names UNL and UNK. Instead, they are renamed to LIG, which is a change filter that applies in the structure upon standardization.
- An issue where the maximum number of atoms in the biological unit was not being respected has been fixed.

# **6.4.4 Documentation changes**

• Minor documentation and example improvements have been fixed.

# **6.5 Spruce TK 1.5.1**

# 6.5.1 New features

- If a site residue is provided to OEMakeDesignUnits, the output design unit title now includes the site residue in the title for apo structures. Previously, the residue in the title was the residue closest to the center of the binding site.
- Standardization using *Spruce Filter* now checks for metal chelation before forming disulfide bridges.

# 6.5.2 Major bug fixes

• An issue causing accumulation of generic data on the molecule components stored in the design unit object during prep has been fixed. This accumulation led to large memory consumption, slow preparation, and larger file size.

# **6.6 Spruce TK 1.5.0**

# 6.6.1 New features

- The new OESpruceFilter class has been added to provide checks and corrections on input to Spruce. For input it can take an OEMolBase, OEStructureMetadata, or an options class, OESpruceFilterOptions, that holds the options to turn on each of the fixing options.
- The new OEValidateDesignUnit class has been added for validation of Spruce produced design units. For input it can take an OEDesignUnit or OEStructureMetadata.

# 6.6.2 Major bug fixes

• A bug that caused memory leaks in OEBio TK has been fixed.

# 6.6.3 Minor bug fixes

- An issue was fixed in *OEBuildLoops* to allow better sequence alignment for peptides.
- An issue was fixed in *OEBuildLoops* where free amino acids, as co-factors or ligands, were incorrectly included in sequence alignments and causing mismatched alignments to the SEQRES.
- An issue was fixed in OEExtractBioUnits to be able to lower the minimum sequence alignment score threshold.

# **6.7 Spruce TK 1.4.0**

**Fall 2021** 

# 6.7.1 New features

- A new method, SetForceCapping, has been added to enable capping even if it will result in a clash.
- Two new methods, SetBuildTails and GetBuildTails, have been added to set and get an option that controls whether to build tails when there is missing residues at the N- and C- termini.
- SiteHopper is now a supported superposition method in OESuperpose, and can be set using the SetMethod method of OESuperpose.
- All Options classes have been modified to derive from OEOptions. This affects classes:
  - OEDesignUnitEnumerateSitesOptions
  - OEProtonateDesignUnitOptions
  - OEDesignUnitBuildOptions
  - OEDesignUnitPrepOptions
  - OEDesignUnitSplitOptions
  - OEBioUnitExtractionOptions
  - OEMakeDesignUnitOptions
  - OEPlaceHydrogensOptions

# 6.7.2 Major bug fixes

- An issue causing capping a nonstandard residue to fail has been fixed.
- An issue causing covalent ligands to have their covalent bond broken when there were alternate locations in the structure, has been fixed.
- An issue causing side-chains to either not be built or being built in non-optimal configurations has been fixed.
- An issue with pockets identifying liganded sites in OEMakeDesignUnitFromPocket not generating a proper design unit with a ligand bound in the identified site has been fixed.

# 6.7.3 Minor bug fixes

- An issue causing the warning message 'Truncated cap due to clash' to appear when SetAllowTruncate is False has been fixed.
- An issue caused by Heuristic score offset being added before comparing to original structure therefore unable to pick the more energy favorable conformation has been fixed.
- An issue causing the gap finding code to mis-identify gaps in the protein structure due to residues with missing backbone atoms has been fixed. The function now removes these residues prior to gap detection inside OEBuildLoops.
- An issue caused by malformed PDB Header data, specifically with regards to REMARK 300 sections, has been fixed.

# **6.8 Spruce TK 1.3.0**

July 2021

# 6.8.1 New features

- A molecule-based API for *OEMakeDesignUnitFromPocket* has been added.
- New high-level superposition APIs were added that unify the sequence-based (OEStructuralSuperposition) and shape-based (OESecondaryStructureSuperposition) APIs. This includes a new OESuperpose class that can calculate different types of structural superposition, a new OESuperposeOptions class that allows the users to control various behaviors of the superposition calculation, such as the superposition method, and a new OESuperposeResults class that holds the transformation and scores of the superposition. More detailed changes are as follows:
  - The new OESuperpose class can take either OEMol or OEDesignUnit as the reference for the fit molecule. The reference molecule can be set by using the *SetupRef* method, and the superposition can be calculated via OESuperpose with the fit molecule supplied as one of its arguments.
  - A new *OESuperposeMethod* namespace was added that contains the constants for different superposition methods. Functions OEGetSuperposeMethodName and OEGetSuperposeMethodFromName were added to obtain the superposition method's name (as a string literal) from its designated constant and vice versa.
  - Methods OESuperposeOptions, OESuperposeOptions, and OESuperposeOptions have been added. These methods can be used to set score thresholds for validating superposition results in the new OESuperposeOptions class. The validity of the superposition result can be obtained by OESuperposeResults from the new OESuperposeResults class.
  - The new OESuperpose API returns an OESuperposeResults object that can be used to transform the fit molecule to its superposed position with its *Transform* method. Alternatively, the users can use *GetRotMa*trix and GetTranslation to obtain the rotation matrix and translation vector, respectively, for their analyses. The RMSD and sequence alignment score after the superposition can be obtained using OESuperposeResults's GetRMSD and GetSeqScore methods for sequence-based superpositions, and the Tanimoto score can be obtained using GetTanimoto.

Please refer to the documentation for more information on these new superposition APIs.

# 6.8.2 Minor bug fixes

- A bug that caused the loop modeling algorithm to crash in rare instances has been fixed.
- Examples have been modified to use appropriate command-line arguments.
- An issue that caused style on OEDesignUnit objects to disappear when calling OEProtonateDesignUnit has been fixed.
- An issue with the return value of superposition when two structures cannot be superposed has been fixed. It now properly returns a -1.00 RMSD.
- An issue in OEMakeDesignUnitFromPocket that caused style to remain on both the previous binding site and the one defined from the pocket has been fixed.
- A bug in superposition that resulted in a crash when using site residues that were not present on a design unit has been fixed.
- A bug that kept the insert code from its anchor residue when there was an N-terminal cap has been fixed.

# **6.8.3 Documentation changes**

- Documentation has been added for the Iridium classification. Iridium.
- Documentation has been added for the new superposition APIs. Superposition related APIs are now fully supported. Superposition.

# **6.9 Spruce TK 1.2.0**

**Fall 2020** 

# 6.9.1 New features

- New methods have been added to OEDesignUnitSplitOptions (AddLipidCode, SetLipidCodes, ClearLipid-Codes, and GetLipidCodes). They allow users to specify the names of molecules to be considered as lipids.
- Support has been added for HEME and related cofactors in OEMakeDesignUnits. The state of HEME, contains two negatively charged nitrogens to balance the  $+2$  Fe formal charge. The nitrogens coordinating the iron atom are indicated by zero-order bonds.
- A new function, OEFindPockets, has been added that finds cavities in protein or nucleic acid complexes. The parameters for the search can be tuned with OEPocketOptions. The pockets are output as OEPocket objects in an iterator. The function can take a predicate that will control only outputting pockets with a given set of residues or atoms in it. This function is also used in *OEMakeDesignUnits* when a site residue is provided.
- A new function, OEMakeDesignUnitFromPocket, has been added that takes a prepared biological unit from an OEMakeDesignUnit and an OEPocket and coverts it into an OEDesignUnit does with a reference structure.
- New methods have been added in OELoopBuilderOptions, SetSegAlignMethod, SetSegAlignGapPenalty, SetSeqAlignExtendPenalty, GetSeqAlignMethod, GetSeqAlignGapPenalty, and GetSeqAlignExtendPenalty that allow users to control the sequence alignment done to find gaps in protein structures related to loop modeling.

# 6.9.2 Major bug fixes

- A bug that caused some modeled loops to be missing the backbone NH hydrogen where the modeled loops were attached has been fixed.
- Fragment numbers for build loops have been fixed to be consistent with the anchor residues where the loops are inserted.
- A bug in OEFixBackbone has been fixed to ensure that OXT atoms are always built on C-terminal residues.
- An issue with atom order for built pieces like loops or caps has been fixed to ensure that these are sequential with the location they are built.
- A bug in *OEBuildLoops* that in specific situations caused incorrect detection of gaps in protein structures has been fixed. Additionally, options have been exposed in OELoopBuilderOptions to allows users to control the underlying sequence alignment in the event of a failure.

# 6.9.3 Minor bug fixes

- Improvements have been made to standard amino acid residue perception when preparing structures.
- Site residues in *OEMakeDesignUnits* are now being checked against all the biological units so one can serve as a reference for the rest.
- A bug in loop modeling that caused the function to create residues with identical residue numbers has been fixed. The function now properly builds using insertion codes.
- A bug in loop modeling that caused problems for the underlying sequence alignment code and incorrect loops when a single residue was floating in space between two gaps has been fixed.
- The chemical component dictionary used internally in OEMakeDesignUnits has been updated with the latest changes from the RCSB, including some fixes for incorrect entries in the source data based on rules and literature searches.

# **6.10 Spruce TK 1.1.0**

# 6.10.1 New features

- Two new APIs, OEBuildSingleLoop and OEBuildLoops, have been added that provide loop modeling capability. This capability relies on either the SEQRES in the PDB header (or equivalent for MMCIF files) or the user passing metadata about the sequences. The functions take an options class, OELoopBuilderOptions, as an argument to specify the file name of the required loop template database. This database is available for download in a platform-independent format.
- A new parameter, siteResidue, has been added to the  $OEMakeDesignUnits$  function. This allows users to specify a single residue in the binding site for APO structures when using the OEEnumerateSites function. The function checks whether the detected site has a large enough volume and whether there is anything in the binding site that the splitter failed to identify as a potential ligand.
- The options class OEDesignUnitBuildOptions has been updated to hold options classes for the different builder options available. This also changes the options class structure for *OEMakeDesignUnitOptions*.
- A new low level class, *OECapBuilderOptions*, that determines behavior when building caps on proteins, has been added to replace passing different parameters to the functions OECapTermini, OECapNTermini, and OECapCTermini.

- OESidechainBuilderOptions, a low level class that determines the behavior when building sidechains on proteins, replaces passing different parameters to the function OEBuildSidechains.
- The preliminary API options class OEDesignUnitMutationOptions has been removed. OEMutateResidues has been added to take a map of mutations, along with OESidechainBuilderOptions to control the behavior when building the mutated residue sidechain.
- A new function,  $OEFixBackbone$ , has been added that builds  $=$ O and/or OXT, if necessary, and ensures that all formal charges and valence states are correct on all backbone atoms. The function removes a residue completely if the primary backbone atoms, N, CA, and C, are missing. The residues can be built correctly later with OEBuildLoops.
- A strict protonation mode has been added to *OEDesignUnitPrepOptions*, enforcing that when an error occurs during addition and optimization of hydrogens to the system, the preparation processes now stop and fail.
- A new options class, OEPlaceHydrogensOptions, has been added to *OEProtonateDesignUnitOptions*. This option allows users more control over the protonation processes; for example, by passing a bypass or no-flip predicate that will prevent the protonation process from altering the residues in the predicate.
- The design units produced by  $OEMakeDesignUnits$  are now ordered by the quality of the Iridium classification data.

# 6.10.2 Major bug fixes

• A bug in OEExtractBioUnits that occurred when using a reference has been fixed. Previously, it resulted in incorrect biological units being produced under certain conditions. The algorithm has also been improved to more often produce the correct biological unit based on symmetry expansion.

# 6.10.3 Minor bug fixes

- Metal co-factors previously had not been properly identified in the binding site during design unit generation due to the distance threshold from a ligand that was too strict. This has been fixed.
- Ligands with an incorrect alternate location assignment but that were in the same location were previously not correctly identified and were assigned alternate locations. This was due to the threshold being too strict and has been fixed.
- In cases where a residue is itself converted to a cap and where building a cap would result in the cap strongly clashing, the cap number no longer adds an insert code or alters the residue number. In addition, valence states resulting from the residue conversion are being more thoroughly validated and fixed, if necessary.
- Some instances of functions changing the location of the OEThrow output and their levels have been fixed.
- An issue in OEExtractBioUnits had previously occurred when structures with the historical convention of putting waters and metals into specific chain IDs (i.e., W and S, respectively) caused the molecules, after symmetry expansion, to have identical residue information. This has been fixed.
- An issue with the side-chain builder miscounting side-chain atoms when involving a residue in cross-linking has been fixed
- An issue that occurred when a single ligand atom (per design) was not properly detected as a ligand has been fixed

# **6.10.4 Documentation changes**

- Documentation and examples have been modified to omit the step where alternate locations are collapsed. The function OEMakeDesignUnits handles alternate location collapse or enumeration and should provide all available data.
- Examples in C++ and Python have been enhanced to include passing electron density maps, and a new example has been added for making APO design units using a site residue or reference structure. The examples also illustrate how to enable **Spruce TK** to build missing loops.

# **6.11 Spruce TK 1.0.0**

# 6.11.1 New features

- The OEExtractBioUnits function has become a stable API. The final implementation includes an options class, OEBioUnitExtractionOptions, to control its behavior.
- A new function, OEMakeDesignUnits, has been added that generates OEDesignUnit from structures read from PDB or mmCIF files. The function takes a number of options to control its behavior; therefore, the following options classes have been defined:
  - OEMakeDesignUnitOptions: a high-level options class that holds the options classes below.
  - OEDesignUnitPrepOptions: a high-level options class that holds other options classes, determining how a design unit is prepped.
  - OEDesignUnitBuildOptions: a low-level class that sets whether to build caps and missing sidechains.
  - OEProtonateDesignUnitOptions: a low-level class that sets whether and how to protonate the design unit, including whether to generate tautomers.
  - OEDesignUnitSplitOptions: a low-level class that determines how to handle alternate locations, how a system is split, locating the ligand, etc.

The OEMakeDesignUnits function also takes the OEStructureMetadata class as input. The OEStructureMetadata class holds experimental data if known and can be used to indicate which is the ligand, what the sequence of the protein is, and other relevant pieces of information.

- The function  $OEMakeDesign Units$  is a high-level function that works on the two intermediate functions, OEMakeBioDesignUnits and OEEnumerateSites, which can be run separately if intermediate results are desired. The high-level  $OEMakeDesignUnits$  function has a deduplication step built in; this function is highly recommended.
- A new function,  $OEMakeDesignUnit$ , has been added that creates an OEDesignUnit.
- A new function, OEP rotonateDesignUnit, has been added that ensures that protons in an OED esignUnit are optimized. The high-level function  $OEMakeDesignUnit \, s$  calls this by default unless it is turned off in options.
- The OEBuildSidechains function has been updated to allow building all possible clusters even if one fails due to clashes. The function still returns false in this case.

# 6.11.2 Major bug fixes

- An issue in the OEExtractBioUnits function that caused a segfault due to an improper PDB header format has been fixed.
- An issue in the alternate location expansion that left atoms on top of each other due to unconventional location definitions has been fixed.

# 6.11.3 Minor bug fixes

- An issue with  $OECapTermin$  i preventing caps from being built in some very specific instances has been fixed.
- OEBuildSidechains no longer builds sidechains on packing residues.

# **6.11.4 Documentation changes**

• A new example, Creating OEDesignUnits from a PDB file, has been added that illustrates the usage of the highlevel OEMakeDesignUnits function for biomolecular structure preparation. This example takes a PDB file as input and outputs a set of fully prepared OEDesignUnit objects to a temporary file.

# **6.12 Spruce TK 0.9.2**

- The product name in the license file for **Spruce TK** has been changed from spruce to sprucetk. This change does not impact the validity of current licenses, which will continue to work with this new version of the toolkit. For more information on Spruce TK licensing, please visit https://www.eyesopen.com/contact.
- Spruce TK is still preliminary.

# 6.12.1 New features

- A new predicate, OEIsModeledAtom, has been added that identifies atoms built by the Spruce TK functions.
- A new function, OEBuildSidechains, has been added to build partial or missing sidechains of standard amino acid residues in a protein.
- A new method,  $OECapCTermini$ , has been added to cap the C-termini of a protein.
- A new method,  $OECapNTermini$ , has been added to cap the N-termini of a protein.
- A new method, OECapTermini, has been added to cap both the N- and C-termini of a protein.
- A new method, OEGetPartialResidues, has been added to return a list of partial residues in a protein.
- A new method,  $OEMutateResidue$ , has been added to mutate a single residue in a protein.

# 6.12.2 Major bug fixes

• A memory leak in the OESecondaryStructureSuperposition class has been fixed.

# 6.12.3 Minor bug fixes

- $OEExtractBiolInits$  has been updated to better handle atoms placed on a symmetry axis.
- OEExtractBioUnits now more reliably assigns components to a biological unit (BU) even when they are far away.

# **6.13 Spruce TK 0.9.1**

# 6.13.1 New features

Note: Spruce TK now requires a specific license. For information on Spruce TK licensing, please visit https: //www.eyesopen.com/contact.

- The OESecondaryStructureSuperposition class can now use ligand constraints initialized in the OESuperpositionOptions option class when handled by the following new methods:
  - OESuperpositionOptions. SetLigandConstraints
  - OESuperpositionOptions.HasLigandConstraints
  - OESuperpositionOptions.GetLigandConstraints
  - OESuperpositionOptions. ClearLigandConstraints
- New OEExtractBioUnits high-level functions have been added to extract biological assemblies, replacing the OEExtractBioUnitsFromRef and OEExtractBioUnitsFromPDBRemarks functions.
- The OESecondaryStructureSuperposition class now can be initialized with the OESuperpositionOptions option class.
- The OESuperpositionType namespace now contains an entry for the SSE superposition method. The default superpositioning method is now OESuperpositionType\_Global.
- New OESStructural Superposition Transform and OESecondaryStructureSuperposition Transform methods have been added to transform a molecule based on superpositioning.
- New OESStructural Superposition operator bool and OESecondaryStructureSuperposition operator bool methods have been added to validate objects.

# 6.13.2 API changes

- The constructor of the OEStructuralSuperposition class has been changed.
- The low-level OEExtractBioUnitsFromRef and OEExtractBioUnitsFromPDBRemarks functions have been removed

# 6.13.3 Major bug fixes

- A bug that caused an issue with extracting biological assemblies has been fixed in the low-level biological assembly factory class.
- Biological assembly extraction for large proteins has been improved for memory and CPU usage.

# 6.13.4 Minor bug fixes

- Superposition methods for using OETrans instead of raw double pointers for rotation matrices and translation vectors have been improved.
- A bug that caused an issue with extracting biological assemblies if they had a blank REMARK line in the PDB file has been fixed.

# **6.14 Spruce TK 0.9.0**

# 6.14.1 New features

Spruce TK has a limited API that is in a preliminary state until the 2018. Oct release. The currently available classes in the API are OESecondaryStructureSuperposition, OEStructuralSuperposition, and OESuperpositionOptions. The currently available functions are OEExtractBioUnitsFromRef and OEExtractBioUnitsFromPDBRemarks.

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
→Fe, NM. http://www.eyesopen.com.
```

#### For example:

```
OpenEye Classic Floes 0.11.2. OpenEye, Cadence Molecular Sciences, Santa Fe, NM.
\rightarrowhttp://www.eyesopen.com.
```

The version number for a Floe package is displayed on the first page of the package's release notes. For example: https://docs.eyesopen.com/floe/modules/classic-floes/docs/source/releasenotes.html.

# 9.2 Toolkits and Applications

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

## For example:

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

### For example:

MaaS 1.0. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://www.eyesopen.com.

The MaaS version number appears on the web service's release notes.

**TEN** 

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                               | License            |
|-------------------------------|-----------------------------------------------------------------------|--------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                  | https://           |
| absl-py                       | https://github.com/abseil/abseil-py                                   | https://           |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                   | https://           |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                 | https://           |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                 | N/A                |
| AmberUtils                    | http://ambermd.org                                                    | N/A                |
| ambit                         | https://github.com/khimaros/ambit                                     | https://           |
| amqp                          | https://github.com/celery/py-amqp                                     | https://           |
| anaconda-anon-usage           | <b>Orion Floes</b>                                                    | https://           |
| angular                       | https://github.com/angular/angular.js                                 | https://           |
| angular-animate               | https://github.com/angular/angular.js                                 | https://           |
| angular-cache                 | https://github.com/jmdobry/angular-cache                              | https://           |
| angular-cookies               | https://github.com/angular/angular.js                                 | https://           |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                      | https://           |
| angular-mocks                 | https://github.com/angular/angular.js                                 | https://           |
| angular-resource              | https://github.com/angular/angular.js                                 | https://           |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                      | https://           |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                 | https://           |
| angular-ui-router             | https://github.com/angular-ui/ui-router                               | https://           |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                    | https://           |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                          | https://           |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                              | https://           |
| annotated-types               | https://github.com/annotated-types/annotated-types                    | https://           |
| anyio                         | https://github.com/agronholm/anyio                                    | https://           |
| appdirs                       | http://github.com/ActiveState/appdirs                                 | http://            |
| appengine                     | https://google.golang.org/appengine                                   | https://           |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                     | https://           |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md            | https://           |
| Name of Project               | Website                                                               | License            |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                  | https:/            |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                         | https:/            |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                            | https:/            |
| ascii85                       | https://github.com/huandu/node-ascii85                                | https:/            |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                        | https:/            |
| asgiref                       | https://github.com/django/asgiref/                                    | https:/            |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                   | https:/            |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render | https:/            |
| assertions oglematchers       | https://github.com/smartystreets/assertions/internal/oglematchers     | https:/            |
| assertions                    | https://github.com/smartystreets/assertions                           | https:/            |
| asttokens                     | https://github.com/gristlabs/asttokens                                | https:/            |
| astunparse                    | https://github.com/simonpercivall/astunparse                          | https:/            |
| async-lru                     | https://github.com/aio-libs/async-lru                                 | https:/            |
| async-timeout                 | https://github.com/aio-libs/async-timeout                             | https:/            |
| atk-1.0                       | https://docs.gtk.org/atk/                                             | https:/            |
| atomic                        | https://github.com/uber-go/atomic                                     | https:/            |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                      | https:/            |
| attrs                         | https://www.attrs.org/                                                | https:/            |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                     | https:/            |
| Babel                         | https://github.com/python-babel/babel                                 |                    |
| backcall                      | https://github.com/takluyver/backcall                                 | https:/            |
| backports                     | https://github.com/brandon-rhodes/backports                           | https:/            |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache               | https:/            |
| base62                        | https://github.com/kare/base62                                        | https:/            |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                        | https:/            |
| billiard                      | https://github.com/celery/billiard                                    | https:/            |
| biopython                     | https://biopython.org                                                 | https:/            |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst         | https:/            |
| bitset                        | https://github.com/willf/bitset                                       | https:/            |
| blas                          | https://www.netlib.org/blas/                                          | https:/            |
| bleach                        | https://github.com/mozilla/bleach                                     | https:/            |
| blessings                     | https://github.com/erikrose/blessings                                 | https:/            |
| blinker                       | https://pythonhosted.org/blinker/                                     | https:/            |
| blosc                         | https://github.com/Blosc/python-blosc                                 | https:/            |
| blosc2                        | https://github.com/Blosc/python-blosc2                                | https:/            |
| boltons                       | https://github.com/mahmoud/boltons                                    | https:/            |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html | https:/            |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html | https:/            |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                        | https:/            |
| boto3                         | https://github.com/boto/boto3                                         | https:/            |
| botocore                      | https://github.com/boto/botocore                                      | https:/            |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                | https:/            |
| Brotli                        | https://github.com/google/brotli                                      | https:/            |
| brotli-bin                    | https://github.com/google/brotli                                      | https:/            |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                  | https:/            |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                            | https:/            |
| bson                          | http://github.com/py-bson/bson                                        | https:/            |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                 |                    |
| bzip2                         | https://www.bzip.org                                                  | https:/            |
| Name of Project               | Website                                                               | License            |
| c-ares                        | https://github.com/c-ares/c-ares                                      | https:/            |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock              | https:/            |
| cached-property               | https://github.com/pydanny/cached-property                            | https:/            |
| cachetools                    | https://github.com/tkem/cachetools                                    | https:/            |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                             | https:/            |
| canvas                        | https://github.com/Automattic/node-canvas                             | https:/            |
| cctbx                         | https://github.com/cctbx/cctbx_project                                | https:/            |
| celery                        | https://github.com/celery/celery                                      | https:/            |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                           | https:/            |
| certifi                       | https://certifi.readthedocs.io/en/latest/                             | https:/            |
| cffi                          | https://github.com/python-cffi                                        | https:/            |
| cftime                        | https://pypi.org/project/cftime/                                      | https:/            |
| chardet                       | https://github.com/chardet/chardet                                    | https:/            |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                          | https:/            |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                               | https:/            |
| click                         | https://palletsprojects.com/p/click/                                  | https:/            |
| click-completion              | https://github.com/click-contrib/click-completion                     | https:/            |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                     | https:/            |
| click-plugins                 | https://github.com/click-contrib/click-plugins                        | https:/            |
| click-repl                    | https://github.com/untitaker/click-repl                               | https:/            |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                              | https:/            |
| cmake                         | https://cmake.org/                                                    | https:/            |
| colorama                      | https://github.com/tartley/colorama                                   | https:/            |
| comm                          | https://github.com/ipython/comm                                       | https:/            |
| compose                       | https://github.com/docker/compose                                     | https:/            |
| conda-content-trust           | https://github.com/conda/conda-content-trust                          | https:/            |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                        | https:/            |
| conda-package-handling        | https://github.com/conda/conda-package-handling                       | https:/            |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming              | https:/            |
| conda-token                   | https://anaconda.org/anaconda/conda-token                             | https:/            |
| confuse                       | https://github.com/beetbox/confuse                                    | https:/            |
| contourpy                     | https://github.com/contourpy/contourpy                                | https:/            |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                 | https:/            |
| cryptography                  | https://github.com/pyca/cryptography                                  | https:/            |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                  | https:/            |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                             | https:/<br>https:/ |
| cupy-cuda113                  | https://cupy.dev/                                                     | https:/            |
| curl                          | https://curl.se                                                       | https:/            |
| cycler                        | https://github.com/matplotlib/cycler                                  | https:/            |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                               | https:/            |
| Cython                        | https://cython.org                                                    | https:/            |
| d3                            | https://github.com/mbostock/d3                                        | https:/            |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                             | https:/            |
| ddsketch                      | http://github.com/datadog/sketches-py                                 | https:/            |
| debugpy                       | https://aka.ms/debugpy                                                | https:/            |
| decimal                       | https://github.com/shopspring/decimal                                 | https:/            |
| decorator                     | https://github.com/micheles/decorator                                 | https:/            |
| deepdiff                      | https://github.com/seperman/deepdiff                                  | https:/            |
| deeptime                      | https://github.com/deeptime-ml/deeptime                               | https:/            |

| Name of Project               | Website                                                                             | License                                                            |
|-------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https:/                                                            |
| dill                          | https://github.com/uqfoundation/dill                                                | https:/                                                            |
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
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/                                                            |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         | https:/                                                            |
| executing                     | https://github.com/alexmojaki/executing                                             | https:/                                                            |
| expat                         | https://libexpat.github.io                                                          | https:/                                                            |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                   | https:/                                                            |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 | https:/                                                            |
| fftw                          | https://www.fftw.org                                                                | comm                                                               |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              | https:/                                                            |
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
| gast                          | https://github.com/serge-sans-paille/gast                                           | https:/                                                            |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                | https:/                                                            |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             | https:/                                                            |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https:/                                                            |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             | https:/                                                            |
| genproto                      | https://google.golang.org/genproto/googleapis                                       | https:/                                                            |
| geometric                     | https://openbase.com/python/geometric                                               | https:/                                                            |
| giflib                        | https://giflib.sourceforge.net                                                      | https:/                                                            |
| glib                          | https://docs.gtk.org/glib/                                                          | https:/                                                            |
| glm                           | https://github.com/g-truc/glm                                                       | https:/                                                            |
| gls                           | https://github.com/jtolds/gls                                                       | https:/                                                            |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https:/                                                            |
| go-connections                | https://github.com/docker/go-connections                                            | https:/                                                            |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https:/                                                            |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https:/                                                            |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https:/                                                            |
| go-ini                        | https://github.com/go-ini/ini                                                       | https:/                                                            |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             | https:/                                                            |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https:/                                                            |
| go-netrc                      | https://github.com/bgentry/go-netrc                                                 | https:/                                                            |
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
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       |                                                                    |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https:/<br>https:/                                                 |
| google-cloud-go               | https://cloud.google.com/go                                                         |                                                                    |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 | https:/                                                            |
| google-pasta                  | https://github.com/google/pasta                                                     | https:/                                                            |
| google.golang.org/api         | https://google.golang.org/api                                                       | https:/                                                            |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  | https:/                                                            |
|                               |                                                                                     | -li                                                                |
| Name of Project               | Website                                                                             | Licen                                                              |
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https:/                                                            |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https:/                                                            |
| graphviz                      | https://graphviz.org/                                                               | https:/                                                            |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https:/                                                            |
| groupcache                    | https://github.com/golang/groupcache                                                | https:/                                                            |
| grpc                          | https://google.golang.org/grpc                                                      | https:/                                                            |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https:/                                                            |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/                                                            |
| $g$ tk2                       | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/                                                            |
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
| <b>ImmuneBuilder</b>          | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/                                                            |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https:/                                                            |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https:/                                                            |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/                                                            |
| inflection                    | https://github.com/jinzhu/inflection                                                | https:/                                                            |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https:/                                                            |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https:/                                                            |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https:/                                                            |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https:/                                                            |
| ipykernel                     | https://ipython.org                                                                 | https:/                                                            |
|                               |                                                                                     |                                                                    |
| ipython<br>ipython-genutils   | https://ipython.org                                                                 | https:/                                                            |
|                               | http://ipython.org<br>http://jupyter.org                                            | https:/                                                            |
| ipywidgets<br>isodate         | https://github.com/gweis/isodate/                                                   | https:/                                                            |
|                               |                                                                                     | https:/                                                            |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/<br>https://github.com/google/jax        | https:/                                                            |
| jax                           |                                                                                     | https:/                                                            |
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
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:                                                             |
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
| kombu                         | https://kombu.readthedocs.io                                                        | https:/                                                            |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                       | https:                                                             |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:                                                             |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:/                                                            |
| lcms2                         | https://www.littlecms.com                                                           | https:/                                                            |
| lerc                          | https://github.com/Esri/lerc                                                        | https:/                                                            |
| libarchive                    | http://www.libarchive.org                                                           | https:                                                             |
| libblas                       | https://www.netlib.org/blas/                                                        | https:                                                             |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:                                                             |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:/                                                            |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https:/                                                            |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                |
| libclang                      | <b>Orion Floes</b>                                                                  | https:                                                             |
| libcurl                       | https://curl.se/libcurl/                                                            | https:                                                             |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:                                                             |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:                                                             |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:                                                             |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://                                                            |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:                                                             |
| libffi                        | https://github.com/libffi/libffi                                                    | https:                                                             |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:                                                             |
| libgd                         | https://libgd.github.io                                                             | https:/                                                            |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:                                                             |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https:                                                             |
|                               |                                                                                     | -Li                                                                |
| Name of Project               | Website                                                                             | Licen                                                              |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https:/                                                            |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https:/                                                            |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https:/                                                            |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https:/                                                            |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https:/                                                            |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                            |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https:/                                                            |
| libopenblas                   | https://www.openblas.net/                                                           | https:/                                                            |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https:/                                                            |
| libpq                         | https://www.postgresql.org/                                                         | https:/                                                            |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https:/                                                            |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https:/                                                            |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https:/                                                            |
| libtiff                       | https://www.libtiff.org/                                                            | https:/                                                            |
| libtrust                      | https://github.com/docker/libtrust                                                  | https:/                                                            |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https:/                                                            |
| libuv                         | https://github.com/libuv/libuv                                                      | https:/                                                            |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https:/                                                            |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https:/                                                            |
| libxc                         | https://www.tddft.org/programs/libxc/                                               | https:/                                                            |
| libxcb                        | https://xcb.freedesktop.org                                                         | https:/                                                            |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https:/                                                            |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https:/                                                            |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https:/                                                            |
| libzlib                       | https://zlib.net                                                                    | https:/                                                            |
| lime                          | https://github.com/marcotcr/lime                                                    | https:/                                                            |
| $\overline{\text{lit}}$       | http://llvm.org                                                                     | https:/                                                            |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https:/                                                            |
| <b>Ilymlite</b>               | http://llvmlite.readthedocs.io                                                      | https:/                                                            |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https:/                                                            |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https:/                                                            |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https:/                                                            |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/                                                            |
| lxml                          | https://lxml.de                                                                     | https:/                                                            |
| $1z4-c$                       | https://www.lz4.org/                                                                |                                                                    |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https:/<br>https:/                                                 |
| markdown-it-py                | <b>Orion Floes</b>                                                                  | https:/                                                            |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https:/                                                            |
| matplotlib                    | https://matplotlib.org                                                              | https:/                                                            |
| matplotlib-base               | https://matplotlib.org                                                              |                                                                    |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https:/                                                            |
|                               |                                                                                     | https:/                                                            |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/                                                            |
| mdtraj                        | https://www.mdtraj.org/                                                             | https:/                                                            |
| mdurl                         | <b>Orion Floes</b>                                                                  | https:/                                                            |
| menuinst                      | <b>Orion Floes</b>                                                                  | https:/                                                            |
| mergo                         | https://github.com/imdario/mergo                                                    | https:/                                                            |
| mistune                       | https://github.com/lepture/mistune                                                  | https:/                                                            |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https:/                                                            |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
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
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https:/                                                            |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                            |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https:/                                                            |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https:/                                                            |
| networkx                      | https://networkx.org                                                                | https:/                                                            |
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
|                               |                                                                                     | T                                                                  |
| Name of Project               | Website                                                                             | Licen                                                              |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| $nvidia-nvtx-cu12$            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| $Oat++$                       | https://oatpp.io/                                                                   | https:/                                                            |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https:/                                                            |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https:/                                                            |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/                                                            |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https:/                                                            |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/                                                            |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/                                                            |
| OpenFF                        | https://openforcefield.org/                                                         | https:/                                                            |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/                                                            |
| openff-forcefields            | https://openforcefield.org                                                          | https:/                                                            |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https:/                                                            |
| openff-models                 | https://github.com/openforcefield/openff-models                                     | https:/                                                            |
| openff-toolkit                | https://openforcefield.org                                                          | https:/                                                            |
| openff-toolkit-base           | https://openforcefield.org                                                          | https:/                                                            |
| openff-units                  | https://github.com/openforcefield/openff-units                                      | https:/                                                            |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https:/                                                            |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https:/                                                            |
| openIdap                      | https://www.openldap.org/software/repo.html                                         | https:/                                                            |
| OpenMM                        | https://openmm.org                                                                  | https:/                                                            |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https:/                                                            |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https:/                                                            |
| openpyx1                      | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                                            |
| openssl                       | https://www.openssl.org                                                             | https:/                                                            |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https:/                                                            |
| OptKing                       | https://github.com/psi-rking/optking                                                | https:/                                                            |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https:/                                                            |
| overrides                     | https://github.com/mkorpela/overrides                                               | https:/                                                            |
| packaging                     | https://github.com/pypa/packaging                                                   | https:/                                                            |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                                            |
| pandas                        | https://pandas.pydata.org                                                           | https:/                                                            |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https:/                                                            |
|                               |                                                                                     |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| panedr                        | https://github.com/MDAnalysis/panedr                                                |                                                                    |
| pango                         | https://pango.gnome.org                                                             |                                                                    |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     |                                                                    |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              |                                                                    |
| parso                         | https://parso.readthedocs.io/en/latest/                                             |                                                                    |
| pathos                        | https://github.com/uqfoundation/pathos                                              |                                                                    |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             |                                                                    |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  |                                                                    |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              |                                                                    |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         |                                                                    |
| pcre                          | https://www.pcre.org                                                                |                                                                    |
| pcre2                         | https://www.pcre.org                                                                |                                                                    |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               |                                                                    |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  |                                                                    |
| pexpect                       | https://pexpect.readthedocs.io/                                                     |                                                                    |
| pgconn                        | https://github.com/jackc/pgconn                                                     |                                                                    |
| pgio                          | https://github.com/jackc/pgio                                                       |                                                                    |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 |                                                                    |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                |                                                                    |
| pgtype                        | https://github.com/jackc/pgtype                                                     |                                                                    |
| pgx                           | https://github.com/jackc/pgx/v4                                                     |                                                                    |
| phonopy                       | https://github.com/phonopy/phono3py                                                 |                                                                    |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          |                                                                    |
| Pillow                        | https://python-pillow.org                                                           |                                                                    |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              |                                                                    |
| pip                           | https://pip.pypa.io/                                                                |                                                                    |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            |                                                                    |
| pixman                        | https://pixman.org                                                                  |                                                                    |
| pkginfo                       | https://launchpad.net/pkginfo                                                       |                                                                    |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        |                                                                    |
| plotly                        | https://plotly.com/python/                                                          |                                                                    |
| plotly-orca                   | https://github.com/plotly/orca                                                      |                                                                    |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 |                                                                    |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  |                                                                    |
| pooch                         | https://github.com/fatiando/pooch                                                   |                                                                    |
| pox                           | https://github.com/uqfoundation/pox                                                 |                                                                    |
| ppft                          | https://github.com/uqfoundation/ppft                                                |                                                                    |
| pq                            | https://github.com/lib/pq                                                           |                                                                    |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       |                                                                    |
| prometheus-client             | https://github.com/prometheus/client_python                                         |                                                                    |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             |                                                                    |
| protobuf                      | https://google.golang.org/protobuf                                                  |                                                                    |
| psi4                          | https://psicode.org                                                                 |                                                                    |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            |                                                                    |
| psycopg2                      | https://psycopg.org/                                                                |                                                                    |
| PTable                        | https://github.com/kxxoling/PTable                                                  |                                                                    |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         |                                                                    |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        |                                                                    |
| pure-eval                     | https://github.com/alexmojaki/pure_eval                                             |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| py                            | https://py.readthedocs.io/en/latest/                                                | https://                                                           |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             | https://                                                           |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   | https://                                                           |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           | https://                                                           |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  | https://                                                           |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 | https://                                                           |
| pycosat                       | https://github.com/conda/pycosat                                                    | https://                                                           |
| pycparser                     | https://github.com/eliben/pycparser                                                 | https://                                                           |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 | https://                                                           |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           | https://                                                           |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                | https://                                                           |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                | https://                                                           |
| Pygments                      | https://pygments.org                                                                | https://                                                           |
| pygraphviz                    | https://pygraphviz.github.io                                                        | https://                                                           |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            | https://                                                           |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        | https://                                                           |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  | https://                                                           |
| <b>PyJWT</b>                  | https://github.com/jpadilla/pyjwt                                                   | https://                                                           |
| pymbar                        | https://pymbar.org                                                                  | https://                                                           |
| pyOpenSSL                     | https://pyopenssl.org/                                                              | https://                                                           |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https://                                                           |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    | https://                                                           |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 | https://                                                           |
| pysam                         | https://github.com/pysam-developers/pysam                                           | https://                                                           |
| PySocks                       | https://github.com/Anorov/PySocks                                                   | https://                                                           |
| pytables                      | https://www.pytables.org                                                            | https://                                                           |
| python                        | https://www.python.org/                                                             | https://                                                           |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          | https://                                                           |
| python-constraint             | https://github.com/python-constraint/python-constraint                              | https://                                                           |
| python-dateutil               | https://dateutil.readthedocs.io                                                     | https://                                                           |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         | https://                                                           |
| python-ldap                   | https://www.python-ldap.org/                                                        | https://                                                           |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            | https://                                                           |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 | https://                                                           |
| pytz                          | https://pythonhosted.org/pytz                                                       | https://                                                           |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   | https://                                                           |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  | https://                                                           |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                 | https://                                                           |
| pyyml                         | No longer available                                                                 | No license                                                         |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             | https://                                                           |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               | https://                                                           |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  | https://                                                           |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        | https://                                                           |
| ramda                         | https://github.com/ramda/ramda                                                      | https://                                                           |
| rapidjson                     | https://rapidjson.org/                                                              | https://                                                           |
| rdkit                         | https://www.rdkit.org                                                               | https://                                                           |
| re2                           | https://github.com/google/re2                                                       | https://                                                           |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             | https://                                                           |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             | https://                                                           |
|                               |                                                                                     | Ιi                                                                 |
| Name of Project               | Website                                                                             | Licen:                                                             |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https:/                                                            |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https:/                                                            |
| reportlab                     | https://www.reportlab.com                                                           | https:/                                                            |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                            |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                            |
| requests                      | https://requests.readthedocs.io                                                     | https:/                                                            |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https:/                                                            |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https:/                                                            |
| resumable                     | https://github.com/stevvooe/resumable                                               | https:/                                                            |
| retrying                      | https://github.com/rholder/retrying                                                 | https:/                                                            |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https:/                                                            |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https:/                                                            |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https:/                                                            |
| rich                          | <b>Orion Floes</b>                                                                  | https:/                                                            |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https:/                                                            |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https:/                                                            |
| rsa                           | https://stuvel.eu/rsa                                                               | https:/                                                            |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/                                                            |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/                                                            |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https:/                                                            |
| sasl                          | https://mellium.im/sasl                                                             | https:/                                                            |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https:/                                                            |
| scikit-image                  | https://scikit-image.org                                                            | https:/                                                            |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https:/                                                            |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/                                                            |
| scipy                         | https://scipy.org                                                                   | https:/                                                            |
| seaborn                       | https://seaborn.pydata.org                                                          | https:/                                                            |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https:/                                                            |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https:/                                                            |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https:/                                                            |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https:/                                                            |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https:/                                                            |
| sh                            | https://github.com/amoffat/sh                                                       | https:/                                                            |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https:/                                                            |
| simint                        | https://www.bennyp.org/research/simint/                                             | https:/                                                            |
| six                           | https://github.com/benjaminp/six                                                    | https:/                                                            |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https:/                                                            |
| snappy                        | https://github.com/google/snappy                                                    | https:/                                                            |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https:/                                                            |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https:/                                                            |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https:/                                                            |
| spglib                        | <b>Orion Floes</b>                                                                  | https:/                                                            |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                |                                                                    |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/                                                            |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/                                                            |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/                                                            |
|                               | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/                                                            |
| sphinxcontrib-jsmath          |                                                                                     | https:/                                                            |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/                                                            |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/                                                            |

| Name of Project              | Website                                                  | License  |
|------------------------------|----------------------------------------------------------|----------|
| SQLAlchemy                   | https://www.sqlalchemy.org                               | https:// |
| sqlite                       | https://sqlite.org/index.html                            | https:// |
| sqlparse                     | https://github.com/andialbrecht/sqlparse                 | https:// |
| stack-data                   | http://github.com/alexmojaki/stack_data                  | https:// |
| starfile                     | https://github.com/alisterburt/starfile                  | https:// |
| statsmodels                  | https://github.com/statsmodels/statsmodels               | https:// |
| structlog                    | https://www.structlog.org/                               | https:// |
| svglib                       | https://github.com/deeplook/svglib                       | https:// |
| sympy                        | https://sympy.org                                        | https:// |
| tables                       | https://www.pytables.org/                                | https:// |
| tabulate                     | https://github.com/astanin/python-tabulate               | https:// |
| tbb                          | https://github.com/oneapi-src/oneTBB                     | https:// |
| tenacity                     | https://github.com/jd/tenacity                           | https:// |
| tensorboard                  | https://github.com/tensorflow/tensorboard                | https:// |
| tensorboard-data-server      | https://github.com/tensorflow/tensorboard                | https:// |
| tensorboard-plugin-wit       | https://github.com/pair-code/what-if-tool                | https:// |
| tensorflow                   | https://github.com/tensorflow/tensorflow                 | https:// |
| tensorflow-estimator         | https://github.com/tensorflow/estimator                  | https:// |
| tensorflow-io-gcs-filesystem | Orion Floes                                              | https:// |
| tensorflow-probability       | https://github.com/tensorflow/probability                | https:// |
| termcolor                    | https://github.com/hugovk/termcolor                      | https:// |
| terminado                    | https://github.com/jupyter/terminado                     | https:// |
| testpath                     | https://github.com/jupyter/testpath                      | https:// |
| textangular                  | https://github.com/fraywing/textAngular                  | https:// |
| tf_keras                     | Orion Floes                                              | https:// |
| threadpoolctl                | https://github.com/joblib/threadpoolctl                  | https:// |
| three                        | https://github.com/mrdoob/three.js                       | https:// |
| tifffile                     | https://github.com/cgohlke/tifffile/                     | https:// |
| tinycss2                     | https://github.com/Kozea/tinycss2/                       | https:// |
| tinyxml2                     | https://github.com/leethomason/tinyxml2                  | https:// |
| tk                           | https://www.tcl.tk/                                      | https:// |
| toml                         | https://github.com/toml-lang/toml                        | https:// |
| tomli                        | https://github.com/hukkin/tomli                          | https:// |
| toolz                        | https://github.com/pytoolz/toolz                         | https:// |
| torch                        | https://pytorch.org/                                     | https:// |
| tornado                      | https://www.tornadoweb.org                               | https:// |
| tqdm                         | https://github.com/tqdm/tqdm                             | https:// |
| tracy                        | https://github.com/gear-genomics/tracy                   | https:// |
| traitlets                    | https://github.com/ipython/traitlets                     | https:// |
| triton                       | https://github.com/openai/triton/                        | https:// |
| truststore                   | Orion Floes                                              | https:// |
| ts-jest                      | https://github.com/kulshekhar/ts-jest                    | https:// |
| ts-loader                    | https://github.com/TypeStrong/ts-loader                  | https:// |
| twine                        | https://github.com/pypa/twine                            | https:// |
| twinj uuid                   | https://github.com/twinj/uuid                            | https:// |
| types                        | https://github.com/babel/babel                           | https:// |
| typescript                   | https://github.com/Microsoft/TypeScript                  | https:// |
| typing_extensions            | https://github.com/python/typing                         | https:// |
| tzdata                       | https://github.com/python/tzdata                         | https:// |
| Name of Project              | Website                                                  | License  |
| tzlocal                      | https://github.com/regebro/tzlocal                       | https:// |
| umi-tools                    | https://github.com/CGATOxford/UMI-tools                  | https:// |
| unicodedata2                 | https://github.com/fonttools/unicodedata2                | https:// |
| uritools                     | https://github.com/tkem/uritools/                        | https:// |
| urllib3                      | https://urllib3.readthedocs.io/                          | https:// |
| vine                         | https://github.com/celery/vine                           | https:// |
| vue                          | https://github.com/vuejs/vue                             | https:// |
| wcwidth                      | https://github.com/jquast/wcwidth                        | https:// |
| webencodings                 | https://github.com/gsnedders/python-webencodings         | https:// |
| websocket-client             | https://github.com/websocket-client/websocket-client.git | https:// |
| Werkzeug                     | https://palletsprojects.com/p/werkzeug/                  | https:// |
| westpa                       | Orion Floes                                              | http://  |
| wheel                        | https://github.com/pypa/wheel                            | https:// |
| widgetsnbextension           | https://github.com/jupyter-widgets/ipywidgets#readme     | https:// |
| wrapt                        | https://github.com/GrahamDumpleton/wrapt                 | https:// |
| wsutil                       | https://github.com/yhat/wsutil                           | https:// |
| x/lint                       | https://golang.org/x/lint                                | https:// |
| x/mod                        | https://golang.org/x/mod/semver                          | https:// |
| x/net                        | https://golang.org/x/net                                 | https:// |
| x/oauth2                     | https://golang.org/x/oauth2                              | https:// |
| x/sys                        | https://golang.org/x/sys                                 | https:// |
| x/text                       | https://golang.org/x/text                                | https:// |
| x/tools                      | https://golang.org/x/tools                               | https:// |
| x/xerrors                    | https://golang.org/x/xerrors                             | https:// |
| xhtml2pdf                    | http://github.com/xhtml2pdf/xhtml2pdf                    | https:// |
| xlrd                         | https://github.com/python-excel/xlrd                     | https:// |
| xmlsec                       | https://github.com/mehcode/python-xmlsec                 | https:// |
| xmltodict                    | https://github.com/martinblech/xmltodict                 | https:// |
| xorg-kbproto                 | https://gitlab.freedesktop.org/xorg/proto/kbproto        | https:// |
| xorg-libice                  | https://gitlab.freedesktop.org/xorg/lib/libice           | https:// |
| xorg-libsm                   | https://gitlab.freedesktop.org/xorg/lib/libsm            | https:// |
| xorg-libx11                  | https://gitlab.freedesktop.org/xorg/lib/libx11           | https:// |
| xorg-libxau                  | https://gitlab.freedesktop.org/xorg/lib/libxau           | https:// |
| xorg-libxdmcp                | https://gitlab.freedesktop.org/xorg/lib/libxdmcp         | https:// |
| xorg-libxext                 | https://gitlab.freedesktop.org/xorg/lib/libxext          | https:// |
| xorg-libxrender              | https://gitlab.freedesktop.org/xorg/lib/libxrender       | https:// |
| xorg-libxt                   | https://gitlab.freedesktop.org/xorg/lib/libxt            | https:// |
| xorg-renderproto             | https://gitlab.freedesktop.org/xorg/proto/renderproto    | https:// |
| xorg-xextproto               | https://gitlab.freedesktop.org/xorg/proto/xextproto      | https:// |
| xorg-xproto                  | https://gitlab.freedesktop.org/xorg/proto/xproto         | https:// |
| xxhash                       | https://github.com/cespare/xxhash/v2                     | https:// |
| xz                           | https://github.com/ulikunitz/xz                          | https:// |
| yaml                         | https://pyyaml.org/                                      | https:// |
| yaml-cpp                     | https://github.com/jbeder/yaml-cpp                       | https:// |
| yaml.v2                      | https://gopkg.in/yaml.v2                                 | https:// |
| yaml.v3                      | https://gopkg.in/yaml.v3                                 | https:// |
| yarl                         | https://github.com/aio-libs/yarl/                        | https:// |
| yaspin                       | https://github.com/pavdmyt/yaspin                        | https:// |
| yfiles                       | https://www.yworks.com/products/yfiles                   | comm     |
| Name of Project              | Website                                                  | License  |
| yml                          | https://pypi.org/project/yml/                            | N/A      |
| zap                          | https://go.uber.org/zap                                  |          |
| zipp                         | https://github.com/jaraco/zipp                           |          |
| zlib                         | https://zlib.net/                                        |          |
| zstandard                    | https://github.com/indygreg/python-zstandard             |          |
| zstd                         | https://facebook.github.io/zstd/                         |          |
| _libgcc_mutex                | https://github.com/conda-forge/_libgcc_mutex-feedstock   |          |
| _openmp_mutex                | https://github.com/conda-forge/_openmp_mutex-feedstock   |          |

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
This GCC Runtime Library Exception ("Exception") is an additional permission under
\rightarrowsection 7 of the GNU General Public License,
version 3 ("GPLv3"). It applies to a given file (the "Runtime Library") that bears a
→notice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

```
(continues on next page)
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

# **10.1.2 GNU GENERAL PUBLIC LICENSE**

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

# See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# A

AddCofactorCode OESpruce:: OEDesignUnitSplitOptions, 49 AddExcipientCode OESpruce:: OEDesignUnitSplitOptions, 49 AddHeterogenMetadata OESpruce:: OEStructureMetadata, 76 AddKeyword OESpruce:: OEStructureMetadata, 77 AddKeywords OESpruce:: OEStructureMetadata, 77 AddLipidCode OESpruce:: OEDesignUnitSplitOptions, 49 AddMutation OESpruce:: OEDesignUnitMutationOptions, 44 AddSequenceMetadata OESpruce:: OEStructureMetadata, 77 AddSiteResidue OESpruce:: OESuperpositionOptions, 89 AddTautomer OESpruce:: OEHeterogenMetadata, 53 AddTautomers OESpruce:: OEHeterogenMetadata, 53

# C

```
Clear
   OESpruce:: OESuperpose, 92
ClearCofactorCodes
   OESpruce:: OEDesignUnitSplitOptions,
       49
ClearExcipientCodes
   OESpruce:: OEDesignUnitSplitOptions,
       49
ClearHeterogenMetadata
   OESpruce:: OEStructureMetadata, 77
ClearKeywords
   OESpruce:: OEStructureMetadata, 77
ClearLigandConstraints
```

OESpruce:: OESuperpositionOptions, 89 ClearLipidCodes OESpruce:: OEDesignUnitSplitOptions,  $\Delta$ Q ClearMutations OESpruce:: OEDesignUnitMutationOptions, 45 ClearSequenceMetadata OESpruce:: OEStructureMetadata, 77 ClearSiteResidues OESpruce:: OESuperpositionOptions, 89 ClearTautomers OESpruce:: OEHeterogenMetadata, 53 ConstraintsMet OESpruce:: OEStructuralSuperposition, 86 Constructors OESpruce:: OEBioUnitExtractionOptions,  $35$ OESpruce:: OECapBuilderOptions, 37 OESpruce:: OEDesignUnitBuildOptions, 39 OESpruce:: OEDesignUnitEnumerateSitesOptions, 41 OESpruce:: OEDesignUnitMutationOptions, 44 OESpruce:: OEDesignUnitPrepOptions, 45 OESpruce:: OEDesignUnitSplitOptions, 48 OESpruce:: OEHeterogenMetadata, 53 OESpruce:: OEIsModeledAtom, 55 OESpruce:: OELoopBuilderOptions, 56 OESpruce:: OEMakeDesignUnitOptions, 63 OESpruce:: OEPocket, 66 OESpruce:: OEPocketOptions, 68 OESpruce:: OEProtonateDesignUnitOptions, 69 OESpruce:: OESecondaryStructureSuperposition,  $80$ OESpruce:: OESequenceMetadata, 74

```
OESpruce:: OESidechainBuilderOptions, GetAtoms
       71
   OESpruce:: OESpruceFilter, 82
   OESpruce:: OESpruceFilterOptions, 83
   OESpruce:: OEStructuralSuperposition, GetAuthor
       86
   OESpruce:: OEStructureMetadata, 76
   OESpruce:: OESuperpose, 92
   OESpruce:: OESuperposeOptions, 94
   OESpruce:: OESuperposeResults, 98
   OESpruce:: OESuperpositionOptions, 88
   OESpruce:: OEValidateDesignUnit, 101
CreateCopy
   OESpruce:: OEIsModeledAtom, 56
```

# D

du2mmcif.pv Example Code, 22

# Ε

Example Code du2mmcif.py, 22 extract\_biounits\_ref.py, 29 extract\_biounits\_remarks.py, 27 findpockets.py, 32 make\_apo\_design\_units.py,20 make\_design\_units.py, 16 superpose.py, 24 extract\_biounits\_ref.py Example Code, 29 extract\_biounits\_remarks.py Example Code, 27

# F

findpockets.py Example Code, 32

# G

```
GetCofactorCodes
GetAddInteractionHints
   OESpruce::OEDesignUnitEnumerateSitesOptiOESpruce::OEDesignUnitSplitOptions,
                                                 50
      42
                                          GetCollapseNonSiteAlts
GetAddStyle
   OESpruce::OEDesignUnitEnumerateSitesOptiOESpruce::OEDesignUnitEnumerateSitesOptions,
                                                 4242
                                          GetConnectBufferDistance
GetAllowBuildDisulfideBridges
                                             OESpruce:: OELoopBuilderOptions, 57
   OESpruce:: OELoopBuilderOptions, 59
                                          GetCropLength
GetAllowTruncate
                                             OESpruce:: OELoopBuilderOptions, 57
   OESpruce:: OECapBuilderOptions, 38
                                          GetDeleteClashingSolvent
GetAlternateLocationHandling
                                             OESpruce:: OECapBuilderOptions, 37
   OESpruce:: OEDesignUnitSplitOptions,
                                             OESpruce:: OESidechainBuilderOptions,
       50
                                                 72
GetAssignPartialChargesAndRadii
                                          GetDeleteFloatingRes
   OESpruce:: OEDesignUnitPrepOptions,
                                             OESpruce:: OESpruceFilterOptions, 85
      46
```

OESpruce:: OEPocket, 67 OESpruce:: OESpruceFilter, 83 OESpruce:: OEValidateDesignUnit, 102 OESpruce:: OEStructureMetadata, 77 GetBackboneClashRejectThreshold OESpruce:: OELoopBuilderOptions, 58 GetBioUnitExtractionOptions OESpruce:: OEMakeDesignUnitOptions, 64 GetBuildLoops OESpruce:: OEDesignUnitBuildOptions, 39 GetBuildOptions OESpruce:: OEDesignUnitPrepOptions,  $46$ GetBuildSidechains OESpruce:: OEDesignUnitBuildOptions, 39 GetBuildTails OESpruce:: OELoopBuilderOptions, 60 GetBurialFactor OESpruce:: OEPocketOptions, 69 GetCapBuilderOptions OESpruce:: OEDesignUnitBuildOptions, 40 GetCapCTermini OESpruce:: OEDesignUnitBuildOptions, 39 GetCapNTermini OESpruce:: OEDesignUnitBuildOptions, 39 GetChainID OESpruce:: OESequenceMetadata, 74 GetChargeEngine OESpruce:: OEDesignUnitPrepOptions,  $46$ 

GetDist GetLigandConstraints OESpruce:: OESuperpositionOptions, 89 OESpruce:: OESuperpositionOptions, 90 GetDuplicateRemoval GetLipidCodes OESpruce::OEDesignUnitEnumerateSitesOptiOESpruce::OEDesignUnitSplitOptions, 42 50 GetEndResidueInsertCode GetLocalDensity OESpruce:: OESequenceMetadata, 74 OESpruce:: OEPocket, 67 GetEndResidueNumber GetLoopBuilderOptions OESpruce:: OEDesignUnitBuildOptions, OESpruce:: OESequenceMetadata, 74 GetEnumerateCofactorSites 40 OESpruce::OEDesignUnitEnumerateSitesOpetiLomspClashRejectThreshold 42 OESpruce:: OELoopBuilderOptions, 58 GetEnumerateSitesOptions GetLoopDBFilename OESpruce:: OELoopBuilderOptions, 57 OESpruce:: OEDesignUnitPrepOptions, 46 GetMakePackingResidues GetExcipientCodes OESpruce:: OEDesignUnitSplitOptions, OESpruce:: OEDesignUnitSplitOptions, 50 50 GetMaxAtoms OESpruce:: OEBioUnitExtractionOptions, GetExperimentDate OESpruce:: OEStructureMetadata, 78 35 GetExperimentType GetMaxLigAtoms OESpruce:: OEStructureMetadata, 78 OESpruce:: OEDesignUnitSplitOptions, 50 GetFitChains OESpruce:: OESecondaryStructureSuperpdSeitMaxnLiqResidues OESpruce:: OEDesignUnitSplitOptions, 81 OESpruce:: OEStructuralSuperposition, 51 87 GetMaxParts OESpruce:: OESuperposeResults, 101 OESpruce:: OEBioUnitExtractionOptions, GetFixBackboneAtoms 36 OESpruce:: OESpruceFilterOptions, 85 GetMaxSurfaceArea GetFixBondOrder OESpruce:: OEPocketOptions, 68 OESpruce:: OESpruceFilterOptions, 84 GetMaxSystemAtoms GetFixBondsToMetals OESpruce:: OEDesignUnitSplitOptions, OESpruce:: OESpruceFilterOptions, 84 51 GetFixLigandState GetMessages OESpruce:: OESpruceFilterOptions, 85 OESpruce:: OESpruceFilter, 83 GetFixNames OESpruce:: OEValidateDesignUnit, 102 OESpruce:: OESpruceFilterOptions, 84 GetMethod GetForceCapping OESpruce:: OESuperposeOptions, 95 OESpruce:: OECapBuilderOptions, 38 GetMinimizeSidechains OESpruce:: OESidechainBuilderOptions, GetGenerateTautomers OESpruce:: OEProtonateDesignUnitOptions, 72 GetMinimizeSidechainsShell 70 OESpruce:: OESidechainBuilderOptions, GetHeterogenMetadata OESpruce:: OEStructureMetadata, 78 72 GetHetGroupNbrDist GetMinLigAtoms OESpruce::OEProtonateDesignUnitOptions, OESpruce::OEDesignUnitSplitOptions, 70  $51$ GetID GetMinScore OESpruce:: OEHeterogenMetadata, 54 OESpruce:: OEBioUnitExtractionOptions, GetIridiumData 36 OESpruce:: OEStructureMetadata, 78 GetMinSurfaceArea GetKeywords OESpruce:: OEPocketOptions, 68 OESpruce:: OEStructureMetadata, 78 GetMutations

OESpruce::OEDesignUnitMutationOptionsGetRevisionDate 45 OESpruce:: OEStructureMetadata, 78 GetOptimizationInclSurfaceAreaTerm GetRMSD OESpruce:: OELoopBuilderOptions, 59 OESpruce:: OEStructuralSuperposition, GetOptimizationMaxLoops 87 OESpruce:: OELoopBuilderOptions, 59 OESpruce:: OESuperposeResults, 100 GetOptimizationShell GetRotamerLibrary OESpruce:: OESidechainBuilderOptions, OESpruce:: OELoopBuilderOptions, 58 GetOptimizationStage1IterMultiplier 72 OESpruce:: OELoopBuilderOptions, 58 GetRotMatrix GetOptimizationStage2IterMultiplier OESpruce:: OESecondaryStructureSuperposition, OESpruce:: OELoopBuilderOptions, 58 81 GetOptimizationTolerance OESpruce:: OEStructuralSuperposition, OESpruce:: OELoopBuilderOptions, 58 87 GetOptimizationUseSolventModel OESpruce:: OESuperposeResults, 99 OESpruce:: OELoopBuilderOptions, 59 GetScore GetOptimizeExpProtons OESpruce:: OEStructuralSuperposition, OESpruce:: OEProtonateDesignUnitOptions, 87 70 GetSeqAlignExtendPenalty GetPlaceHydrogensOptions OESpruce:: OELoopBuilderOptions, 59 OESpruce::OEProtonateDesignUnitOptionSetSeqAlignGapPenalty OESpruce:: OELoopBuilderOptions, 59 70 GetPocketPredicate GetSeqAlignMethod OESpruce:: OEPocket, 67 OESpruce:: OELoopBuilderOptions, 59 GetPocketSurface GetSeqScore OESpruce:: OESuperposeResults, 100 OESpruce:: OEPocket, 67 GetPreferAuthorRecord GetSequence OESpruce:: OEBioUnitExtractionOptions, OESpruce:: OESequenceMetadata, 74 36 GetSequenceMetadata OESpruce:: OEStructureMetadata, 79 GetPrepOptions OESpruce:: OEMakeDesignUnitOptions, GetSidechainBuilderOptions 65 OESpruce:: OEDesignUnitBuildOptions, GetProtonate  $40$ OESpruce:: OEDesignUnitPrepOptions, GetSiteResidues OESpruce:: OESuperpositionOptions, 90 46 GetProtonateOptions GetSiteSize OESpruce:: OEDesignUnitPrepOptions, OESpruce:: OEDesignUnitEnumerateSitesOptions,  $47$ 43 GetRefChains GetSmiles OESpruce:: OESecondaryStructureSuperposit@BBpruce:: OEHeterogenMetadata, 54 81 GetSplitOptions OESpruce:: OEStructuralSuperposition, OESpruce:: OEMakeDesignUnitOptions, 87 65 OESpruce:: OESuperposeResults, 100 GetStartResidueInsertCode OESpruce:: OESequenceMetadata, 75 GetRegion OESpruce:: OEStructuralSuperposition, GetStartResidueNumber 87 OESpruce:: OESequenceMetadata, 75 GetResidues GetStrictMode OESpruce:: OESidechainBuilderOptions, OESpruce:: OEPocket, 67 GetRestrictToRefSite 72 OESpruce::OEDesignUnitEnumerateSitesOfetiStmsictProlineMatch OESpruce:: OELoopBuilderOptions, 57  $42$ GetRevision GetStrictProtonationMode OESpruce:: OEStructureMetadata, 78

OESpruce:: OEDesignUnitPrepOptions, OESpruce:: OESuperpositionOptions, 90 47 HasRef GetStructureID OESpruce:: OESuperpose, 92 OESpruce:: OEStructureMetadata, 79 HasRMSD GetSuperpose OESpruce:: OESuperposeResults, 100 OESpruce:: OEBioUnitExtractionOptions, HasSeqScore OESpruce:: OESuperposeResults, 100 36 OESpruce:: OEMakeDesignUnitOptions, HasTanimoto 65 OESpruce:: OESuperposeResults, 100 GetSuperpositionMethod OESpruce:: OEMakeDesignUnitOptions, 65 IsValid GetSuperpositionType OESpruce:: OESuperposeResults, 98 OESpruce:: OESuperpositionOptions, 90 M GetSurfaceArea OESpruce:: OEPocket, 67 make\_apo\_design\_units.py GetTanimoto Example Code, 20 OESpruce::OESecondaryStructureSuperporakite Odesign\_units.py 81 Example Code, 16 OESpruce:: OESuperposeResults, 100 Ő GetTargetComponentID OESpruce:: OEDesignUnitSplitOptions, OESpruce:: OEAlternateLocationOption, 102 51 OESpruce:: OEAlternateLocationOption:: Combinatorial, GetTautomers 102 OESpruce:: OEHeterogenMetadata, 54 OESpruce:: OEAlternateLocationOption:: Default, GetTitle 102 OESpruce:: OEHeterogenMetadata, 54 OESpruce:: OEAlternateLocationOption:: Enumerate, GetTransform 102 OESpruce:: OESuperposeResults, 99 OESpruce:: OEAlternateLocationOption:: Max, GetTransformThreshold 103 OESpruce:: OELoopBuilderOptions, 57 OESpruce:: OEAlternateLocationOption:: Primary, GetTranslation 103 OESpruce::OESecondaryStructureSuperpositione::OEAlternateLocationOption::Unknown,  $81$ 103 OESpruce:: OEStructuralSuperposition, OESpruce:: OEBioUnitExtractionOptions, 88 35 OESpruce:: OESuperposeResults, 99 Constructors, 35 GetType GetMaxAtoms, 35 OESpruce:: OEHeterogenMetadata, 54 GetMaxParts, 36 GetUseConstraints GetMinScore, 36 OESpruce:: OESuperposeOptions, 95 GetPreferAuthorRecord, 36 GetUsePackingResidues GetSuperpose, 36 OESpruce:: OELoopBuilderOptions, 57  $operatorerator =$ , 35 GetValidRMSD SetMaxAtoms, 36 OESpruce:: OESuperposeOptions, 95 SetMaxParts, 36 GetValidSeqScore SetMinScore, 36 OESpruce:: OESuperposeOptions, 97 SetPreferAuthorRecord, 37 GetValidTanimoto SetSuperpose, 37 OESpruce:: OESuperposeOptions, 96 OESpruce:: OEBuildLoops, 112 OESpruce:: OEBuildSidechains, 113 H OESpruce:: OEBuildSingleLoop, 114 HasConstraintMol OESpruce:: OECapBuilderOptions, 37 OESpruce:: OESuperpose, 92 Constructors, 37 HasLigandConstraints GetAllowTruncate, 38

GetDeleteClashingSolvent. 37 OESpruce:: OEDesignUnitIssueCodes:: MissingLoop, GetForceCapping, 38 103 operator=, 37 OESpruce::OEDesignUnitIssueCodes::PartialSideChain, SetAllowTruncate, 38 103 SetDeleteClashingSolvent, 38 OESpruce:: OEDesignUnitIssueCodes:: Success, SetForceCapping, 38 103 OESpruce:: OEDesignUnitIssueCodes:: TerminiNotCapped, OESpruce:: OECapCTermini, 115 OESpruce:: OECapNTermini, 115 104 OESpruce:: OECapTermini, 116 OESpruce:: OEDesignUnitMutationOptions, OESpruce:: OEDesignUnitBuildOptions, 38 44 Constructors, 39 AddMutation, 44 GetBuildLoops, 39 ClearMutations, 45 GetBuildSidechains, 39 Constructors, 44 GetCapBuilderOptions, 40 GetMutations, 45 GetCapCTermini, 39 operator=, 44 GetCapNTermini, 39 SetMutations, 45 GetLoopBuilderOptions, 40 OESpruce:: OEDesignUnitPrepOptions, 45 GetSidechainBuilderOptions, 40 Constructors, 45 operator=, 39 GetAssignPartialChargesAndRadii, 46 SetBuildLoops, 40 GetBuildOptions, 46 SetBuildSidechains, 40 GetChargeEngine, 46 SetCapBuilderOptions, 41 GetEnumerateSitesOptions, 46 SetCapCTermini, 40 GetProtonate, 46 SetCapNTermini, 40 GetProtonateOptions, 47 SetLoopBuilderOptions, 41 GetStrictProtonationMode, 47 SetSidechainBuilderOptions, 41 operator=, 46 OESpruce::OEDesignUnitEnumerateSitesOptions,SetAssignPartialChargesAndRadii, 47 41 SetBuildOptions, 47 Constructors, 41 SetChargeEngine, 47 GetAddInteractionHints, 42 SetEnumerateSitesOptions, 47 GetAddStyle, 42 SetProtonate, 47 GetCollapseNonSiteAlts, 42 SetProtonateOptions, 48 GetDuplicateRemoval, 42 SetStrictProtonationMode, 48 GetEnumerateCofactorSites, 42 OESpruce:: OEDesignUnitSplitOptions, 48 GetRestrictToRefSite, 42 AddCofactorCode, 49 GetSiteSize, 43 AddExcipientCode, 49 operator=, 42 AddLipidCode, 49 SetAddInteractionHints, 43 ClearCofactorCodes, 49 SetAddStyle, 43 ClearExcipientCodes, 49 ClearLipidCodes, 49 SetCollapseNonSiteAlts, 43 SetDuplicateRemoval, 43 Constructors, 48 SetEnumerateCofactorSites, 43 GetAlternateLocationHandling, 50 SetRestrictToRefSite, 43 GetCofactorCodes, 50 SetSiteSize, 44 GetExcipientCodes, 50 OESpruce:: OEDesignUnitIssueCodes, 103 GetLipidCodes, 50 OESpruce:: OEDesignUnitIssueCodes:: All, GetMakePackingResidues, 50 104 GetMaxLigAtoms, 50 OESpruce::OEDesignUnitIssueCodes::BrokenChaflexMaxLigResidues, 51 104 GetMaxSystemAtoms, 51 OESpruce::OEDesignUnitIssueCodes::HeavyAtoms@et@Mihap.gAtoms,51 104 GetTargetComponentID, 51 OESpruce::OEDesignUnitIssueCodes::ImplicitH,operator=, 49 104 SetAlternateLocationHandling, 51 SetCofactorCodes, 51

```
SetExcipientCodes, 51
                                              GetTitle, 54
   SetLipidCodes, 52
                                              GetType, 54
   SetMakePackingResidues, 52
                                              operator=, 53
   SetMaxLigAtoms, 52
                                              SetID, 54
   SetMaxLigResidues, 52
                                              SetSmiles, 54
   SetMaxSystemAtoms, 52
                                              SetTitle, 55
   SetMinLigAtoms, 52
                                              SetType, 55
   SetTargetComponentID, 52
                                           OESpruce:: OEHeterogenType, 106
OESpruce:: OEEnumerateSites, 117
                                           OESpruce:: OEHeterogenType:: Cofactors,
OESpruce:: OEExperimentType, 104
                                                  106
OESpruce::OEExperimentType::ElectronCrysOE$pogcaphQEHeterogenType::CounterIons,
       104
                                                  106
OESpruce::OEExperimentType::ElectronMicrOE6ppyce::OEHeterogenType::Excipients,
       105
                                                  106
OESpruce::OEExperimentType::FiberDiffracOE8pruce::OEHeterogenType::Ligand,106
       105
                                           OESpruce:: OEHeterogenType:: Lipids, 106
OESpruce::OEExperimentType::NeutronDiffr@E$ppnce::OEHeterogenType::Metals, 107
                                           OESpruce:: OEHeterogenType:: Polymers, 107
       105
OESpruce::OEExperimentType::PowderDiffraOE$pnuce::OEHeterogenType::Solvent,107
       105
                                           OESpruce:: OEHeterogenType:: Sugars, 107
OESpruce::OEExperimentType::SolidStateNMRESpruce::OEHeterogenType::Unknown, 107
                                           OESpruce:: OEIsModeledAtom, 55
       105
OESpruce:: OEExperimentType:: SolutionNMR,
                                              Constructors, 55
       105
                                              CreateCopy, 56
OESpruce:: OEExperimentType:: SolutionScatterimperator (), 55
       105
                                           OESpruce:: OELoopBuilderOptions, 56
OESpruce:: OEExperimentType:: TheoreticalMode Constructors, 56
       105
                                              GetAllowBuildDisulfideBridges, 59
OESpruce:: OEExperimentType:: Unknown, 106
                                              GetBackboneClashRejectThreshold, 58
OESpruce::OEExperimentType::XRayDiffraction,GetBuildTails, 60
       106
                                              GetConnectBufferDistance, 57
OESpruce:: OEExtractBioUnits, 117
                                              GetCropLength, 57
OESpruce:: OEFindPockets, 118
                                              GetLoopClashRejectThreshold, 58
OESpruce:: OEFixBackbone, 119
                                              GetLoopDBFilename, 57
OESpruce:: OEGetAlternateLocationOptionID,
                                              GetOptimizationInclSurfaceAreaTerm,
       119
                                                  59
OESpruce::OEGetAlternateLocationOptionName, GetOptimizationMaxLoops, 59
       119
                                              GetOptimizationShell, 58
OESpruce:: OEGetExperimentTypeID, 119
                                              GetOptimizationStage1IterMultiplier,
OESpruce:: OEGetExperimentTypeName, 120
                                                  58
OESpruce:: OEGetHeterogenTypeID, 120
                                              GetOptimizationStage2IterMultiplier,
OESpruce:: OEGetHeterogenTypeName, 120
                                                  58
OESpruce:: OEGetPartialResidues, 120
                                              GetOptimizationTolerance, 58
OESpruce:: OEGetSuperposeMethodFromName,
                                              GetOptimizationUseSolventModel, 59
       127
                                              GetSeqAlignExtendPenalty, 59
OESpruce:: OEGetSuperposeMethodName, 127
                                              GetSeqAliqnGapPenalty, 59
OESpruce:: OEHeterogenMetadata, 53
                                              GetSeqAlignMethod, 59
   AddTautomer.53
                                              GetStrictProlineMatch.57
                                              GetTransformThreshold, 57
   AddTautomers. 53
   ClearTautomers, 53
                                              GetUsePackingResidues, 57
   Constructors, 53
                                              operator=, 56
   GetID, 54
                                              SetAllowBuildDisulfideBridges, 62
   GetSmiles, 54
                                              SetBackboneClashRejectThreshold, 61
   GetTautomers, 54
                                              SetBuildTails, 63
```

SetConnectBufferDistance, 61 SetCropLength, 60 SetLoopClashRejectThreshold, 61 SetLoopDBFilename, 60 SetOptimizationInclSurfaceAreaTerm, 62 SetOptimizationMaxLoops, 62 SetOptimizationShell, 61 SetOptimizationStage1IterMultiplier, 61 SetOptimizationStage2IterMultiplier, 62 SetOptimizationTolerance, 61 SetOptimizationUseSolventModel, 62 SetSeqAliqnExtendPenalty, 63 SetSeqAliqnGapPenalty, 62 SetSeqAliqnMethod, 62 SetStrictProlineMatch. 60 SetTransformThreshold, 60 SetUsePackingResidues, 60 OESpruce:: OEMakeBioDesignUnits, 121 OESpruce:: OEMakeDesignUnit, 121 OESpruce:: OEMakeDesignUnitFromPocket, 123 OESpruce:: OEMakeDesignUnitOptions, 63 Constructors, 63 GetBioUnitExtractionOptions, 64 GetPrepOptions, 65 GetSplitOptions, 65 GetSuperpose, 65 GetSuperpositionMethod, 65 operator=, 64 SetBioUnitExtractionOptions, 65 SetPrepOptions, 65 SetSplitOptions, 65 SetSuperpose, 66 SetSuperpositionMethod, 66 OESpruce:: OEMakeDesignUnits, 122 OESpruce:: OEMutateResidue, 124 OESpruce:: OEMutateResidues, 125 OESpruce:: OEPocket, 66 Constructors, 66 GetAtoms, 67 GetLocalDensity, 67 GetPocketPredicate, 67 GetPocketSurface, 67 GetResidues. 67 GetSurfaceArea, 67 operator=, 67 OESpruce:: OEPocketOptions, 68 Constructors, 68 GetBurialFactor, 69 GetMaxSurfaceArea, 68 GetMinSurfaceArea, 68

operator=, 68 SetBurialFactor, 69 SetMaxSurfaceArea, 69 SetMinSurfaceArea, 69 OESpruce:: OEProtonateDesignUnit, 125 OESpruce:: OEProtonateDesignUnitOptions, 69 Constructors, 69 GetGenerateTautomers, 70 GetHetGroupNbrDist, 70 GetOptimizeExpProtons, 70 GetPlaceHydrogensOptions, 70 operator=, 70 SetGenerateTautomers, 70 SetHetGroupNbrDist, 71 SetOptimizeExpProtons, 71 SetPlaceHydrogensOptions, 71 OESpruce:: OESecondaryStructureSuperposition, 80 Constructors, 80 GetFitChains, 81 GetRefChains, 81 GetRotMatrix, 81 GetTanimoto. 81 GetTranslation, 81 operator bool, 81 operator=, 80 Transform, 82 OESpruce:: OESequenceMetadata, 73 Constructors, 74 GetChainID, 74 GetEndResidueInsertCode, 74 GetEndResidueNumber, 74 GetSequence, 74 GetStartResidueInsertCode, 75 GetStartResidueNumber, 75 operator=, 74 SetChainID, 75 SetEndResidueInsertCode, 75 SetEndResidueNumber, 75 SetSequence, 75 SetStartResidueInsertCode, 75 SetStartResidueNumber, 76 OESpruce:: OESetPackingResidueProperties, 125 OESpruce:: OESidechainBuilderOptions, 71 Constructors, 71 GetDeleteClashingSolvent, 72 GetMinimizeSidechains, 72 GetMinimizeSidechainsShell, 72 GetRotamerLibrary, 72 GetStrictMode, 72 operator=, 72 SetDeleteClashingSolvent, 73

SetMinimizeSidechains, 73 GetRefChains, 87 SetMinimizeSidechainsShell, 73 GetRegion, 87 SetRotamerCoverage, 72 GetRMSD, 87 SetRotamerLibrary, 73 GetRotMatrix, 87 SetStrictMode, 73 GetScore, 87 OESpruce:: OESpruceFilter, 82 GetTranslation, 88 Constructors. 82 operator bool, 86 GetAtoms, 83 operator=, 86 GetMessages, 83 Transform, 88 operator=, 82 OESpruce:: OEStructureMetadata, 76 StandardizeAndFilter, 83 AddHeterogenMetadata, 76 OESpruce:: OESpruceFilterIssueCodes, 108 AddKeyword, 77 OESpruce:: OESpruceFilterIssueCodes:: All, AddKeywords, 77 110 AddSequenceMetadata, 77 OESpruce::OESpruceFilterIssueCodes::InvalidCRESTHeterogenMetadata, 77 109 ClearKeywords, 77 OESpruce::OESpruceFilterIssueCodes::InvalidEllecatrSemplemsciMeChaelalap,77 109 Constructors, 76 OESpruce:: OESpruceFilterIssueCodes:: InvalidMettAlRowd, 77 109 GetExperimentDate, 78 OESpruce::OESpruceFilterIssueCodes::InvalidNemteExperimentType, 78 GetHeterogenMetadata, 78 109 OESpruce::OESpruceFilterIssueCodes::InvalidResiIdueBtuatDest,a, 78 GetKeywords, 78 109 OESpruce::OESpruceFilterIssueCodes::InvalidSeqAReiginion, 78 109 GetRevisionDate, 78 OESpruce:: OESpruceFilterIssueCodes:: Success, GetSequenceMetadata, 79 109 GetStructureID, 79 OESpruce:: OESpruceFilterOptions, 83 operator= $,76$ Constructors, 83 SetAuthor, 79 GetDeleteFloatingRes, 85 SetExperimentDate, 79 GetFixBackboneAtoms, 85 SetExperimentType, 79 GetFixBondOrder, 84 SetIridiumData, 79 GetFixBondsToMetals, 84 SetRevision, 79 GetFixLigandState, 85 SetRevisionDate, 80 GetFixNames, 84 SetStructureID, 80 operator=, 83 OESpruce:: OESuperpose, 91 SetDeleteFloatingRes, 85 Clear, 92 SetFixBackboneAtoms, 85 Constructors, 92 SetFixBondOrder, 84 HasConstraintMol, 92 SetFixBondsToMetals, 84 HasRef, 92 SetFixLigandState, 85 operator=, 92 SetFixNames, 84 SetMethod, 93 OESpruce:: OESpruceGetArch, 126 SetOptions, 93 OESpruce:: OESpruceGetLicensee, 126 SetupRef, 93 OESpruce:: OESpruceGetPlatform, 126 Superpose, 93 OESpruce:: OESpruceGetRelease, 126 OESpruce:: OESuperposeMethod, 110 OESpruce:: OESpruceGetSite, 126 OESpruce:: OESuperposeMethod:: DDM, 111 OESpruce:: OESuperposeMethod:: Default, OESpruce:: OESpruceGetVersion, 126 OESpruce:: OESpruceIsLicensed, 127 110 OESpruce:: OEStructuralSuperposition, 85 OESpruce:: OESuperposeMethod:: DifferenceDistanceMat: ConstraintsMet, 86 111 Constructors, 86 OESpruce:: OESuperposeMethod:: Global, 110 GetFitChains, 87

OESpruce::OESuperposeMethod::GlobalCarbonAlpGetSuperpositionType.90 110 HasLigandConstraints, 90 OESpruce:: OESuperposeMethod:: SecondaryStructopealatemen68, 111 SetDist, 90 OESpruce:: OESuperposeMethod:: Site, 111 SetLigandConstraints, 91 OESpruce:: OESuperposeMethod:: SiteHopper, SetSiteResidues, 91 SetSuperpositionType, 91 112 OESpruce::OESuperposeMethod::SiteSequenc@ESpruce::OESuperpositionType, 107 110 OESpruce:: OESuperpositionType:: DDM, 108 OESpruce:: OESuperposeMethod:: SSE, 111 OESpruce:: OESuperpositionType:: Default, OESpruce:: OESuperposeMethod:: Undefined, 107 112 OESpruce:: OESuperpositionType:: Global, OESpruce:: OESuperposeMethod:: Weighted, 108 111 OESpruce:: OESuperpositionType:: Site, 108 OESpruce::OESuperposeMethod::WeightedDiffBSpnueDisOESupMaposxtionType::SSE,108 111 OESpruce:: OESuperpositionType:: Undefined, OESpruce:: OESuperposeOptions, 94 108 Constructors, 94 OESpruce:: OESuperpositionType:: Weighted, GetMethod. 95 108 GetUseConstraints, 95 OESpruce:: OEValidateDesignUnit, 101 GetValidRMSD, 95 Constructors, 101 GetValidSeqScore, 97 GetAtoms, 102 GetValidTanimoto, 96 GetMessages, 102 operator=, 94 operator=,  $101$ SetMethod, 95 Validate, 101 SetUseConstraints, 95 operator bool SetValidRMSD, 96 OESpruce:: OESecondaryStructureSuperposition, SetValidSeqScore, 97 81 SetValidTanimoto, 96 OESpruce:: OEStructuralSuperposition, OESpruce:: OESuperposeResults, 97 86 Constructors, 98 OESpruce:: OESuperposeResults, 98 GetFitChains. 101 operator() GetRefChains, 100 OESpruce:: OEIsModeledAtom, 55 GetRMSD, 100 operator= GetRotMatrix, 99 OESpruce:: OEBioUnitExtractionOptions, GetSeqScore, 100 35 GetTanimoto, 100 OESpruce:: OECapBuilderOptions, 37 GetTransform, 99 OESpruce:: OEDesignUnitBuildOptions, GetTranslation, 99 39 HasRMSD, 100 OESpruce:: OEDesignUnitEnumerateSitesOptions, HasSeqScore, 100  $42.$ HasTanimoto, 100 OESpruce:: OEDesignUnitMutationOptions, IsValid. 98  $44$ operator bool, 98 OESpruce:: OEDesignUnitPrepOptions, operator=, 98 46 Transform, 99 OESpruce:: OEDesignUnitSplitOptions, OESpruce:: OESuperpositionOptions, 88 49 AddSiteResidue, 89 OESpruce:: OEHeterogenMetadata, 53 ClearLigandConstraints, 89 OESpruce:: OELoopBuilderOptions, 56 ClearSiteResidues, 89 OESpruce:: OEMakeDesignUnitOptions, Constructors, 88 64 GetDist, 89 OESpruce:: OEPocket, 67 GetLigandConstraints, 90 OESpruce:: OEPocketOptions, 68 GetSiteResidues, 90

```
OESpruce:: OEProtonateDesignUnitOptions, OESpruce:: OEPocketOptions, 69
       70
                                          SetCapBuilderOptions
   OESpruce::OESecondaryStructureSuperposit@E6pruce::OEDesignUnitBuildOptions,
                                                  41
       80
   OESpruce:: OESequenceMetadata, 74
                                          SetCapCTermini
   OESpruce:: OESidechainBuilderOptions,
                                              OESpruce:: OEDesignUnitBuildOptions,
                                                 40
       72
   OESpruce:: OESpruceFilter, 82
                                          SetCapNTermini
   OESpruce:: OESpruceFilterOptions, 83
                                              OESpruce:: OEDesignUnitBuildOptions,
   OESpruce:: OEStructuralSuperposition,
                                                 4086
                                          SetChainID
                                              OESpruce:: OESequenceMetadata, 75
   OESpruce:: OEStructureMetadata, 76
   OESpruce:: OESuperpose, 92
                                          SetChargeEngine
   OESpruce:: OESuperposeOptions, 94
                                              OESpruce:: OEDesignUnitPrepOptions,
   OESpruce:: OESuperposeResults, 98
                                                 47
   OESpruce:: OESuperpositionOptions, 88
                                          SetCofactorCodes
   OESpruce:: OEValidateDesignUnit, 101
                                              OESpruce:: OEDesignUnitSplitOptions,
                                                 51
S
                                          SetCollapseNonSiteAlts
                                              OESpruce:: OEDesignUnitEnumerateSitesOptions,
SetAddInteractionHints
   OESpruce::OEDesignUnitEnumerateSitesOptions, 43
                                          SetConnectBufferDistance
      43
                                              OESpruce:: OELoopBuilderOptions, 61
SetAddStyle
   OESpruce::OEDesignUnitEnumerateSitesOpetGreepLength
       43
                                              OESpruce:: OELoopBuilderOptions, 60
                                          SetDeleteClashingSolvent
SetAllowBuildDisulfideBridges
                                              OESpruce:: OECapBuilderOptions, 38
   OESpruce:: OELoopBuilderOptions, 62
                                              OESpruce:: OESidechainBuilderOptions,
SetAllowTruncate
                                                 73
   OESpruce:: OECapBuilderOptions, 38
                                          SetDeleteFloatingRes
SetAlternateLocationHandling
                                              OESpruce:: OESpruceFilterOptions, 85
   OESpruce:: OEDesignUnitSplitOptions,
                                          SetDist
       51
                                              OESpruce:: OESuperpositionOptions, 90
SetAssignPartialChargesAndRadii
                                          SetDuplicateRemoval
   OESpruce:: OEDesignUnitPrepOptions,
                                              OESpruce:: OEDesignUnitEnumerateSitesOptions,
      47
                                                 43
SetAuthor
                                          SetEndResidueInsertCode
   OESpruce:: OEStructureMetadata, 79
                                              OESpruce:: OESequenceMetadata, 75
SetBackboneClashRejectThreshold
                                          SetEndResidueNumber
   OESpruce:: OELoopBuilderOptions, 61
                                              OESpruce:: OESequenceMetadata, 75
SetBioUnitExtractionOptions
                                          SetEnumerateCofactorSites
   OESpruce:: OEMakeDesignUnitOptions,
                                              OESpruce:: OEDesignUnitEnumerateSitesOptions,
       65
                                                 43
SetBuildLoops
   OESpruce:: OEDesignUnitBuildOptions,
                                          SetEnumerateSitesOptions
                                              OESpruce:: OEDesignUnitPrepOptions,
       40
                                                 47
SetBuildOptions
                                          SetExcipientCodes
   OESpruce:: OEDesignUnitPrepOptions,
                                              OESpruce:: OEDesignUnitSplitOptions,
       47
                                                 51
SetBuildSidechains
                                          SetExperimentDate
   OESpruce:: OEDesignUnitBuildOptions,
                                              OESpruce:: OEStructureMetadata, 79
      40
                                          SetExperimentType
SetBuildTails
                                              OESpruce:: OEStructureMetadata, 79
   OESpruce:: OELoopBuilderOptions, 63
                                          SetFixBackboneAtoms
SetBurialFactor
```

OESpruce:: OESpruceFilterOptions, 85 OESpruce:: OESuperpose, 93 SetFixBondOrder OESpruce:: OESuperposeOptions, 95 OESpruce:: OESpruceFilterOptions, 84 SetMinimizeSidechains SetFixBondsToMetals OESpruce:: OESidechainBuilderOptions, OESpruce:: OESpruceFilterOptions, 84 73 SetFixLigandState SetMinimizeSidechainsShell OESpruce:: OESidechainBuilderOptions, OESpruce:: OESpruceFilterOptions, 85 SetFixNames 73 OESpruce:: OESpruceFilterOptions, 84 SetMinLigAtoms SetForceCapping OESpruce:: OEDesignUnitSplitOptions, OESpruce:: OECapBuilderOptions, 38 52 SetGenerateTautomers SetMinScore OESpruce::OEProtonateDesignUnitOptions, OESpruce::OEBioUnitExtractionOptions, 70 36 SetHetGroupNbrDist SetMinSurfaceArea OESpruce:: OEProtonateDesignUnitOptions, OESpruce:: OEPocketOptions, 69  $71$ SetMutations SetID OESpruce:: OEDesignUnitMutationOptions, OESpruce:: OEHeterogenMetadata, 54 45 SetIridiumData SetOptimizationInclSurfaceAreaTerm OESpruce:: OEStructureMetadata, 79 OESpruce:: OELoopBuilderOptions, 62 SetLigandConstraints SetOptimizationMaxLoops OESpruce:: OELoopBuilderOptions, 62 OESpruce:: OESuperpositionOptions, 91 SetLipidCodes SetOptimizationShell OESpruce:: OELoopBuilderOptions, 61 OESpruce:: OEDesignUnitSplitOptions, 52 SetOptimizationStage1IterMultiplier SetLoopBuilderOptions OESpruce:: OELoopBuilderOptions, 61 OESpruce:: OEDesignUnitBuildOptions, SetOptimizationStage2IterMultiplier 41 OESpruce:: OELoopBuilderOptions, 62 SetLoopClashRejectThreshold SetOptimizationTolerance OESpruce:: OELoopBuilderOptions, 61 OESpruce:: OELoopBuilderOptions, 61 SetLoopDBFilename SetOptimizationUseSolventModel OESpruce:: OELoopBuilderOptions, 60 OESpruce:: OELoopBuilderOptions, 62 SetMakePackingResidues SetOptimizeExpProtons OESpruce:: OEDesignUnitSplitOptions, OESpruce:: OEProtonateDesignUnitOptions, 52 71 SetMaxAtoms SetOptions OESpruce:: OEBioUnitExtractionOptions, OESpruce:: OESuperpose, 93 36 SetPlaceHydrogensOptions OESpruce:: OEProtonateDesignUnitOptions, SetMaxLigAtoms OESpruce:: OEDesignUnitSplitOptions, 71 52 SetPreferAuthorRecord SetMaxLigResidues OESpruce:: OEBioUnitExtractionOptions, OESpruce:: OEDesignUnitSplitOptions, 37 SetPrepOptions 52 SetMaxParts OESpruce:: OEMakeDesignUnitOptions, OESpruce:: OEBioUnitExtractionOptions, 65 36 SetProtonate SetMaxSurfaceArea OESpruce:: OEDesignUnitPrepOptions, OESpruce:: OEPocketOptions, 69  $\Delta$ 7 SetProtonateOptions SetMaxSystemAtoms OESpruce:: OEDesignUnitPrepOptions, OESpruce:: OEDesignUnitSplitOptions, 52 48 SetMethod SetRestrictToRefSite

OESpruce::OEDesignUnitEnumerateSitesOptiOESpruce::OEMakeDesignUnitOptions,  $43$ 66 SetRevision SetSuperpositionType OESpruce:: OEStructureMetadata, 79 OESpruce:: OESuperpositionOptions, 91 SetRevisionDate SetTargetComponentID OESpruce:: OEStructureMetadata, 80 OESpruce:: OEDesignUnitSplitOptions, SetRotamerCoverage 52 OESpruce:: OESidechainBuilderOptions, SetTitle 72 OESpruce:: OEHeterogenMetadata, 55 SetRotamerLibrary SetTransformThreshold OESpruce:: OESidechainBuilderOptions, OESpruce:: OELoopBuilderOptions, 60 73 SetType SetSeqAlignExtendPenalty OESpruce:: OEHeterogenMetadata, 55 OESpruce:: OELoopBuilderOptions, 63 SetupRef SetSeqAlignGapPenalty OESpruce:: OESuperpose, 93 OESpruce:: OELoopBuilderOptions, 62 SetUseConstraints SetSeqAliqnMethod OESpruce:: OESuperposeOptions, 95 OESpruce:: OELoopBuilderOptions, 62 SetUsePackingResidues OESpruce:: OELoopBuilderOptions, 60 SetSequence OESpruce:: OESequenceMetadata, 75 SetValidRMSD SetSidechainBuilderOptions OESpruce:: OESuperposeOptions, 96 OESpruce:: OEDesignUnitBuildOptions, SetValidSeqScore 41 OESpruce:: OESuperposeOptions, 97 SetSiteResidues SetValidTanimoto OESpruce:: OESuperpositionOptions, 91 OESpruce:: OESuperposeOptions, 96 SetSiteSize StandardizeAndFilter OESpruce:: OEDesignUnitEnumerateSitesOptiOESpruce:: OESpruceFilter, 83 44 Superpose SetSmiles OESpruce:: OESuperpose, 93 OESpruce:: OEHeterogenMetadata, 54 superpose.py SetSplitOptions Example Code, 24 OESpruce:: OEMakeDesignUnitOptions, Τ 65 SetStartResidueInsertCode Transform OESpruce:: OESequenceMetadata, 75 OESpruce:: OESecondaryStructureSuperposition, SetStartResidueNumber 82 OESpruce:: OESequenceMetadata, 76 OESpruce:: OEStructuralSuperposition, SetStrictMode OESpruce:: OESidechainBuilderOptions, OESpruce:: OESuperposeResults, 99 73  $\vee$ SetStrictProlineMatch OESpruce:: OELoopBuilderOptions, 60 Validate SetStrictProtonationMode OESpruce:: OEValidateDesignUnit, 101 OESpruce:: OEDesignUnitPrepOptions, 48 SetStructureID OESpruce:: OEStructureMetadata, 80 SetSuperpose OESpruce:: OEBioUnitExtractionOptions, 37 OESpruce:: OEMakeDesignUnitOptions, 66 SetSuperpositionMethod