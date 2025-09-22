![](_page_0_Picture_0.jpeg)

# **GraphSim TK - Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

## **CONTENTS**

| <b>1 Introduction</b>                                         | 1 |
|---------------------------------------------------------------|---|
| 1.1 Visualizing Molecule Similarity                           | 1 |
| <b>2 Theory</b>                                               | 1 |
| 2.1 Fingerprint Generation                                    | 1 |
| 2.1.1 MACCS                                                   | 1 |
| 2.1.2 LINGO                                                   | 1 |
| 2.1.3 Circular                                                | 1 |
| 2.1.4 Path                                                    | 1 |
| 2.1.5 Tree                                                    | 1 |
| 2.2 Fingerprint Types                                         | 2 |
| 2.2.1 Fingerprint parameters                                  | 2 |
| 2.2.2 Fingerprint version number                              | 2 |
| 2.3 Storage and Retrieval                                     | 3 |
| 2.4 Similarity Measures                                       | 3 |
| 2.4.1 Built-in Similarity Measures                            | 3 |
| 2.4.2 Similarity Calculation                                  | 3 |
| 2.4.3 User-defined Similarity Measures                        | 3 |
| 2.5 Fingerprint Database                                      | 3 |
| 2.5.1 Sorted Search                                           | 3 |
| 2.5.2 Searching with User-defined Similarity Measures         | 4 |
| 2.6 User-defined Fingerprint                                  | 4 |
| 2.6.1 Atom and Bond Typing                                    | 4 |
| 2.6.2 Fragment Size                                           | 4 |
| 2.6.3 Fingerprint Size                                        | 4 |
| 2.7 Fingerprint Coverage                                      | 4 |
| 2.8 Fingerprint Overlap                                       | 5 |
| 2.9 Fingerprint Patterns                                      | 5 |
| <b>3 GPU Fast Fingerprints</b>                                | 5 |
| 3.1 Prerequisites                                             | 5 |
| 3.1.1 GPU-Related Requirements                                | 5 |
| 3.2 Usage                                                     | 5 |
| <b>4 Examples</b>                                             | 5 |
| 4.1 GraphSim TK Examples                                      | 5 |
| 4.1.1 Building and searching fingerprint database             | 5 |
| 4.1.2 Generating fingerprint file for fast fingerprint search | 6 |
| 4.1.3 Searching fast fingerprint database                     | 6 |
| 4.2 Python Cookbook Examples                                  | 7 |

| Section                               | Page |
|---------------------------------------|------|
| <b>5 API</b>                          | 5    |
| 5.1 OEGraphSim Classes                | 5    |
| 5.1.1 OECreateFastFPDatabaseOptions   | 5    |
| 5.1.2 OEFastFPDatabaseParams          | 5    |
| 5.1.3 OEFastFPDatabase                | 5    |
| 5.1.4 OEFingerPrint                   | 6    |
| 5.1.5 OEFPDatabase                    | 6    |
| 5.1.6 OEFPDatabaseOptions             | 7    |
| 5.1.7 OEFPHistogram                   | 7    |
| 5.1.8 OEFPPattern                     | 8    |
| 5.1.9 OEFPTypeBase                    | 8    |
| 5.1.10 OEFPTypeParams                 | 8    |
| 5.1.11 OEFPVariogram                  | 8    |
| 5.1.12 OESimFuncBase                  | 8    |
| 5.1.13 OESimScore                     | 8    |
| 5.1.14 OESimScorePair                 | 8    |
| 5.1.15 OESimSearchResult              | 8    |
| 5.1.16 OETanimotoSim                  | 9    |
| 5.1.17 OETverskySim                   | 9    |
| 5.2 OEGraphSim Constants              | 9    |
| 5.2.1 OEFastFPDatabaseMemoryType      | 9    |
| 5.2.2 OEFPAtomType                    | 9    |
| 5.2.3 OEFPBondType                    | 10   |
| 5.2.4 OEFPDatabaseOptionsSetup        | 11   |
| 5.2.5 OEFPType                        | 11   |
| 5.2.6 OEPopCountMethod                | 11   |
| 5.2.7 OESimMeasure                    | 11   |
| 5.2.8 OESimSearchStatus               | 11   |
| 5.3 OEGraphSim Functions              | 11   |
| 5.3.1 OEAreCompatibleDatabases        | 11   |
| 5.3.2 OEConfigureFingerPrint          | 11   |
| 5.3.3 OEConfigureFPDatabaseMemoryType | 11   |
| 5.3.4 OEConfigureFPDatabaseOptions    | 11   |
| 5.3.5 OECosine                        | 11   |
| 5.3.6 OECreateFastFPDatabaseFile      | 12   |
| 5.3.7 OEDice                          | 12   |
| 5.3.8 OEEuclid                        | 12   |
| 5.3.9 OEGetBitCounts                  | 12   |
| 5.3.10 OEGetCircularFPType            | 12   |
| 5.3.11 OEGetFingerPrintVersion        | 12   |
| 5.3.12 OEGetFingerPrintVersionString  | 12   |
| 5.3.13 OEGetFPAtomType                | 12   |
| 5.3.14 OEGetFPBondType                | 12   |
| 5.3.15 OEGetFPCoverage                | 12   |
| 5.3.16 OEGetFPDatabaseMemoryType      | 12   |
| 5.3.17 OEGetFPOverlap                 | 12   |
| 5.3.18 OEGetFPPatterns                | 12   |
| 5.3.19 OEGetFPType                    | 12   |
| 5.3.20 OEGetPathFPType                | 12   |
| 5.3.21 OEGetPopCountMethod            | 12   |
| 5.3.22 OEGetSimilarityMeasureName     | 12   |
| 5.3.23 OEGetTreeFPType                | 12   |
| 5.3.24 OEGraphSimGetArch              | 12   |
| 5.3.25 OEGraphSimGetLicensee          | 12   |

| 5.3.26  OEGraphSimGetPlatform    | 12 |
|----------------------------------|----|
| 5.3.27  OEGraphSimGetRelease     | 12 |
| 5.3.28  OEGraphSimGetSite        | 12 |
| 5.3.29  OEGraphSimGetVersion     | 12 |
| 5.3.30  OEGraphSimIsGPUReady     | 12 |
| 5.3.31  OEGraphSimIsLicensed     | 12 |
| 5.3.32  OEIsFastFPDatabaseReady  | 12 |
| 5.3.33  OEIsFPType               | 12 |
| 5.3.34  OEIsSameFPType           | 12 |
| 5.3.35  OEIsValidFPTypeString    | 12 |
| 5.3.36  OEMakeCircularFP         | 12 |
| 5.3.37  OEMakeFP                 | 13 |
| 5.3.38  OEMakeLingoFP            | 13 |
| 5.3.39  OEMakeMACCS166FP         | 13 |
| 5.3.40  OEMakePathFP             | 13 |
| 5.3.41  OEMakeTreeFP             | 13 |
| 5.3.42  OEManhattan              | 13 |
| 5.3.43  OESetupFingerPrint       | 13 |
| 5.3.44  OESetupFPDatabaseOptions | 13 |
| 5.3.45  OESimSearchStatusToName  | 13 |
| 5.3.46  OETanimoto               | 13 |
| 5.3.47  OETversky                | 13 |
| <b>6  Release History</b>        | 13 |
| 6.1  GraphSim TK 2.6.1           | 13 |
| 6.1.1  Minor bug fixes           | 13 |
| 6.2  GraphSim TK 2.6.0           | 13 |
| 6.3  GraphSim TK 2.5.7           | 13 |
| 6.4  GraphSim TK 2.5.6           | 13 |
| 6.5  GraphSim TK 2.5.5           | 13 |
| 6.6  GraphSim TK 2.5.4           | 13 |
| 6.7  GraphSim TK 2.5.3           | 13 |
| 6.8  GraphSim TK 2.5.2           | 13 |
| 6.9  GraphSim TK 2.5.1           | 13 |
| 6.9.1  New features              | 13 |
| 6.10  GraphSim TK 2.5.0          | 13 |
| 6.10.1  New features             | 13 |
| 6.10.2  Major bug fixes          | 13 |
| 6.10.3  Minor bug fixes          | 13 |
| 6.10.4  General Notices          | 13 |
| 6.11  GraphSim TK 2.4.3          | 13 |
| 6.11.1  New features             | 13 |
| 6.11.2  Minor bug fixes          | 13 |
| 6.12  GraphSim TK 2.4.2          | 14 |
| 6.13  GraphSim TK 2.4.1          | 14 |
| 6.13.1  New features             | 14 |
| 6.13.2  Minor bug fixes          | 14 |
| 6.14  GraphSim TK 2.4.0          | 14 |
| 6.14.1  New features             | 14 |
| 6.15  GraphSim TK 2.3.1          | 14 |
| 6.15.1  New features             | 14 |
| 6.15.2  Documentation changes    | 14 |
| 6.16  GraphSim TK 2.3.0          | 14 |
| 6.16.1  New features             | 14 |

| 6.16.2 API Change                    | 14 |
|--------------------------------------|----|
| 6.16.3 C++-specific changes          | 14 |
| 6.16.4 Java-specific changes         | 14 |
| 6.16.5 Documentation changes         | 14 |
| 6.17 GraphSim TK 2.2.6               | 14 |
| 6.17.1 New features                  | 14 |
| 6.18 GraphSim TK 2.2.5               | 14 |
| 6.19 GraphSim TK 2.2.4               | 14 |
| 6.19.1 New features                  | 14 |
| 6.19.2 Minor bug fixes               | 14 |
| 6.20 GraphSim TK 2.2.3               | 14 |
| 6.20.1 Documentation changes         | 14 |
| 6.21 GraphSim TK 2.2.2               | 14 |
| 6.22 GraphSim TK 2.2.1               | 14 |
| 6.23 GraphSim TK 2.2.0               | 14 |
| 6.23.1 Major bug fixes               | 14 |
| 6.23.2 Documentation fixes           | 14 |
| 6.24 GraphSim TK 2.1.1               | 14 |
| 6.24.1 Documentation fixes           | 14 |
| 6.25 GraphSim TK 2.1.0               | 14 |
| 6.25.1 Minor bug fixes               | 14 |
| 6.25.2 Documentation fixes           | 14 |
| 6.26 GraphSim TK 2.0.7               | 14 |
| 6.26.1 Documentation changes         | 14 |
| 6.27 GraphSim TK 2.0.6               | 14 |
| 6.27.1 Documentation changes         | 14 |
| 6.28 GraphSim TK 2.0.5               | 14 |
| 6.28.1 Major bug fixes               | 14 |
| 6.29 GraphSim TK 2.0.4               | 14 |
| 6.30 GraphSim TK 2.0.3               | 14 |
| 6.31 GraphSim TK 2.0.2               | 14 |
| 6.32 GraphSim TK 2.0.1               | 14 |
| 6.32.1 Minor bug fixes               | 14 |
| 6.33 GraphSim TK 2.0.0               | 14 |
| 6.33.1 New features                  | 14 |
| 6.33.2 Documentation changes         | 14 |
| 6.34 GraphSim TK 1.0.1               | 14 |
| 6.34.1 Documentation changes         | 14 |
| 6.35 GraphSim TK 1.0.0               | 14 |
| 7 Copyright and Trademarks           | 14 |
| 8 Sample Code                        | 15 |
| 9 Citation                           | 15 |
| 9.1 Orion ® Floes                    | 15 |
| 9.2 Toolkits and Applications        | 15 |
| 9.3 OpenEye Web Services             | 15 |
| 10 Technology Licensing              | 15 |
| 10.1 GCC                             | 17 |
| 10.1.1 GCC RUNTIME LIBRARY EXCEPTION | 17 |
| 10.1.2 GNU GENERAL PUBLIC LICENSE    | 17 |

 $\mathbf{i}\mathbf{v}$ 

## **INTRODUCTION**

This manual is to familiarize the user with the GraphSim TK functionalities. It does not provide explanations of basic **OEChem TK** classes and functions. Therefore reading the **OEChem TK** manual beforehand is highly recommended.

The GraphSim TK library provides a facility for encoding 2D molecular graph information into fingerprints. The following basic fingerprint functionalities are available:

- Generation (see *Fingerprint Generation* chapter)
- Storage (see *Storage and Retrieval* chapter)
- Comparison (see Similarity Measures chapter)

Emphasis has been placed on speed, with attention to rapid in-memory fingerprint search (see Fingerprint Database chapter).

## **1.1 Visualizing Molecule Similarity**

All images in this manual are generated utilizing the OEDepict TK and Grapheme TK.

Molecule similarity based on fingerprints is visualized by the following method: (See example in Figure: Example of depiction of molecule similarity based on fingerprints)

- The OEGetFPOverlap function is utilized to return all common fragments found between two molecules based on a given fingerprint type. These common fragments reveal the similar parts of the two molecules being compared.
- A "yellow to dark green" linear color gradient is then used to color the molecules by their similarity. Where there is similarity detected between the two molecules *i.e.* there are common fragments, the color green is used to highlight the bonds. The color gets darker with increasing similarity *i.e.* as more fragments are shared by the two molecules.
- Color pink indicates parts of the molecules that are not sharing any common fragments *i.e.* they are 2D dissimilar based on the given fingerprint type.

**Hint:** Visualizing similarity of two molecules based on their fingerprints provides insight into molecule similarity beyond a single numerical score and reveals information about the underlying fingerprint methods.

#### See also:

The Python script that visualizes molecule similarity based on fingerprints can be downloaded from the OpenEye **Python Cookbook** 

![](_page_7_Figure_1.jpeg)

Fig. 1: Example of depiction of molecule similarity based on fingerprints

## **THEORY**

## **2.1 Fingerprint Generation**

The fingerprint types implemented in the GraphSim TK encode the 2D graph features of molecules. Fingerprints can be used in applications such as similarity searches, molecular characterization, molecular diversity and chemical database clustering.

The following five types of fingerprints are implemented:

- 1. MACCS (OEFPType\_MACCS166)
- 2. LINGO (OEFPType\_Lingo)
- 3. Circular (OEFPType\_Circular)
- 4. Path (OEFPType\_Path)
- 5. Tree (OEFPType\_Tree)

## **2.1.1 MACCS**

MACCS keys are 166 bit structural key descriptors in which each bit is associated with a SMARTS pattern.

The following code snippets demonstrate two separate ways to create a MACCS keys fingerprint:

```
fp = oeqraphsim.OEFingerPrint()oegraphsim.OEMakeMACCS166FP(fp, mol)
```

oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType\_MACCS166)

## **2.1.2 LINGO**

The GraphSim TK provides fingerprint API for the LINGO similarity search method implemented in OEChem TK.

The following code snippets demonstrate two separate ways to create a LINGO fingerprint:

```
fp = oegraphsim.OEFingerPrint()oegraphsim.OEMakeLingoFP(fp, mol)
```

```
oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType_Lingo)
```

## 2.1.3 Circular

A circular fingerprint is generated by exhaustively enumerating all circular fragments grown radially from each heavy atom of the molecule up to the given radius and then hashing these fragments into a fixed-length bitvector. See Figure: Example of enumerating circular fragments with various radii.

![](_page_9_Figure_3.jpeg)

Fig. 1: Example of enumerating circular fragments with various radii

The following code snippets demonstrate two separate ways to create a circular fingerprint with default parameters:

```
fp = oeqraphsim.OEFingerPrint()oegraphsim.OEMakeCircularFP(fp, mol)
```

```
oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType_Circular)
```

## 2.1.4 Path

A path fingerprint is generated by exhaustively enumerating all linear fragments of a molecular graph up to a given size and then hashing these fragments into a fixed-length bitvector. See Figure: Example of enumerating path fragments with various lengths.

The following code snippets demonstrate two separate ways to create a path fingerprint with default parameters:

```
fp = oegraphsim.OEFingerPrint()oegraphsim.OEMakePathFP(fp, mol)
```

![](_page_10_Figure_1.jpeg)

#### Fig. 2: Example of enumerating path fragments with various lengths

oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType\_Path)

## 2.1.5 Tree

A tree fingerprint is generated by **exhaustively** enumerating all tree fragments of a molecular graph up to a given size and then hashing these fragments into a fixed-length bitvector. See Figure: Example of enumerating tree fragments with various lengths.

The following code snippets demonstrate two separate ways to create a tree fingerprint with default parameters:

```
fp = oegraphsim.OEFingerPrint()oegraphsim.OEMakeTreeFP(fp, mol)
```

oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType\_Tree)

Hint: GraphSim TK also provides the ability to parameterize the circular, path and tree fingerprint generation with arbitrary sets of properties. For more details see the *User-defined Fingerprint* chapter.

![](_page_11_Figure_1.jpeg)

#### Fig. 3: Example of enumerating tree fragments with various lengths

## **2.2 Fingerprint Types**

A fingerprint is a bitvector. To reflect this the OEFingerPrint class derives from the OEBitVector class. The difference is that OEFingerPrint has a type that represents how the fingerprint is generated. Fingerprints may only be compared if they are generated in the same way. Therefore, the following restriction is introduced:

Warning: When two fingerprints are subjected to similarity calculation their type has to be identical.

Listing 1 shows how to create different fingerprint objects (OEFingerPrint) and identify or compare their types.

#### **Listing 1: Fingerprint type**

```
f pA = oegraphsim.OEFingerPrint()f p B = o e graph sim. O E Finger Print()if not fpA.IsValid():
    print ("uninitialized fingerprint")
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "clccccc1")
oegraphsim. OEMakeFP(fpA, mol, oegraphsim. OEFPType_Path)
oegraphsim. OEMakeFP(fpB, mol, oegraphsim. OEFPType_Lingo)
```

```
if oegraphsim. OEIsFPType (fpA, oegraphsim. OEFPType_Lingo):
    print ("Lingo")
if oegraphsim. OEIsFPType (fpA, oegraphsim. OEFPType_Path) :
    print ("Path")
if oegraphsim. OEIsSameFPType(fpA, fpB):
    print ("same fingerprint types")
Also:print ("different fingerprint types")
```

The output of Listing 1 is the following:

```
uninitialized fingerprint
Path
different fingerprint types
```

Two fingerprints are considered to be equivalent only if they have the same fingerprint type (OEFPTypeBase) and have identical bit-vectors (OEBitVector). The following code snippet shows how to compare two OEFingerPrint objects.

```
if fpA == fpB:
    print ("same fingerprints")
else:
    print ("different fingerprints")
```

The following code snippet shows how to initialize a OEFingerPrint object by using the type of another fingerprint. The type of a fingerprint is accessed by the OEFingerPrint. GetFPTypeBase method.

```
f pA = oeqraphsim.OEFingerPrint()oegraphsim.OEMakePathFP(fpA, mol)
f p B = o e q r a p h s i m. 0 E F i n q e r P r i n t ()
oegraphsim. OEMakeFP(fpB, mol, fpA. GetFPTypeBase())
```

### 2.2.1 Fingerprint parameters

The User-defined Fingerprint chapter gives examples of how user defined fingerprints can be generated by defining, for example, the atom and bond properties that will be encoded into the fingerprints.

In order to ensure that only equivalent fingerprints can be compared, the fingerprint type stores the parameters being used in the generation process. The OEFPTypeBase. GetFPTypeString method returns the string representation of the fingerprint type that includes information about the parameters being used.

```
fp = oeqraphsim.OEFingerPrint()oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType_Path)
print(fp.GetFPTypeBase().GetFPTypeString())
```

The output of the preceding snippet is the following:

```
Path, ver=2.0.0, size=4096, bonds=0-5, atype=AtmNum|Arom|Chiral|FCharge|HvyDeq|Hyb|EqHalo,
btype=Order | Chiral
```

Note: The returned string does not include newline characters, the string was broken into two separate lines here only for better readability.

The following Listing 2 shows how to extract the parameters of a fingerprint from a string representation by using the OEFPTypeParams class.

#### **Listing 2: Fingerprint parameters**

```
fptype = oegraphsim. OEGetFPType (oegraphsim. OEFPType_Path)
prms = oegraphsim. OEFPTypeParams (fptype. GetFPTypeString())
print ("version = 8s" 8 oegraphsim. OEGetFingerPrintVersionString (prms. GetVersion ()))
print ("number of bits = \partial d" \partial prms. GetNumBits ())
print ("min bonds = \partial d" % prms. GetMinDistance())
print ("max bonds = \partial u" % prms. GetMaxDistance())
print ("atom types = \frac{2}{5} s" \frac{8}{5} oegraphsim. OEGetFPAtomType (prms. GetAtomTypes()))
print ("bond types = %s" % oegraphsim. OEGetFPBondType (prms. GetBondTypes()))
```

The output of Listing 2 is the following:

```
version = 2.0.0number of bits = 4096min bonds = 0
max bonds = 5
atom types = AtmNum|Arom|Chiral|FCharge|HvyDeg|Hyb|EqHalo
bond types = Order|Chiral
```

#### See also:

- User-defined Fingerprint chapter
- · OEIsValidFPTypeString function
- OEGetFPType function
- OEFPAt omType namespace
- · OEGetFPAtomType function
- OEFPBondType namespace
- OEGetFPBondType function

## 2.2.2 Fingerprint version number

Each fingerprint type additionally has a version number. Version numbers are introduced in order to keep track of changes in the fingerprint generation algorithm itself. The OEFPTypeBase. GetFPVersionString method returns the string representation of the fingerprint version.

```
fp = oegraphsim.OEFingerPrint()oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType_Path)
print(fp.GetFPTypeBase().GetFPVersionString())
```

The output of the preceding snippet is the following:

 $2.0.0$ 

Warning: The version number of the fingerprints will not be changed with each release. It will be incremented only if modifications or bug fixes to the corresponding algorithm would result in generating a different bit-vector for the same molecules.

Fingerprints with an old version number will be still readable and comparable with each other but not with fingerprints which have different version number.

## **2.3 Storage and Retrieval**

The OEFingerPrint does not store any reference to the molecule from which it was generated. The user has to keep track of which fingerprint corresponds to which molecule. One way to do this is to attach the fingerprint, as generic data, to the molecule. Listing 3 shows how store and retrieve fingerprints as generic data.

Listing 3: Storing and retrieving fingerprint as generic data

```
tag = "FP\_DATA"mol = oechem.OEGraphMol()
oechem.OESmilesToMol(mol, "clccccc1")
fp = oegraphsim.OEFingerPrint()oegraphsim.OEMakeLingoFP(fp, mol)
mol.SetData(tag, fp)
if mol. HasData (tag) :
   f = mol.GetData(taq)if f.IsValid():
        fptype = f.GetFPTypeBase().GetFPTypeString()
        print ("%s fingerprint with `%s' identifier" % (fptype, tag))
```

It is good practice to check the validity of the fingerprint after retrieving it. The OEFingerPrint . IsValid method returns true if the fingerprint was successfully initialized.

Listing 4 demonstrates how to create an OEB binary file that stores molecules along with their fingerprints. When reading the OEB file that was generated by this program, the pre-calculated fingerprints can be accessed rapidly with the PATH FP tag. This eliminates the *on-the-fly* generation of the fingerprints.

#### See also:

Additional examples in Listing 10 and Listing 12 of the Fingerprint Database chapter.

#### Listing 4: Fingerprint generation and storage in OEB

```
if len(sys.argv) != 3:
    oechem.OEThrow.Usage("%s <infile> <outfile>" % sys.argv[0])
if s = oechem. oemolistream()if not ifs.open(sys.argv[1]):
    oechem. OEThrow. Fatal ("Unable to open %s for reading" % sys. argv[1])
ofs = oechem.oemolostream()
if not ofs.open(sys.argv[2]):
    oechem. OEThrow. Fatal ("Unable to open %s for writing" % sys. argv[2])
if ofs. GetFormat() != oechem. OEFormat OEB:
   oechem. OEThrow. Fatal ("%s output file has to be an OEBinary file" % sys. argy [2])
fp = oegraphsim.OEFingerPrint()
```

```
for mol in ifs.GetOEGraphMols():
    \verb|oegraphsim.0EMakeFP(fp, mol, oegraphsim.0EFFType\_Path)||\\mol.SetData("PATH_FP", fp)
    oechem.OEWriteMolecule(ofs, mol)
```

The following code snippets shows how to generate a bitstring from an OEFingerPrint object.

#### Listing 5: Accessing a fingerprint as a bitstring

```
def GetBitString(fp):
   bitstring = ''for b in range (0, fp.Getsize()):
        if fp. IsBitOn(b):
           bitstring += '1'else:
           bitstring += 0'
    return bitstring
```

See also:

• OEBitVector class

Warning: Even though the GraphSim TK library provides a fingerprint API for the LINGO similarity search method, it is not implemented as a *real* fingerprint, so bitstrings that are generated from LINGO fingerprints are meaningless.

Fingerprints can also be stored in SDF files. The Listing 6 demonstrates how to create an SDF and store fingerprints as hexadecimal strings.

After the fingerprint is generated, it is attached to the molecule as an SD data tag. The identifier of the fingerprint in the SDF file will be the string representation of the fingerprint type. The bitvector of the fingerprint is converted to a hexadecimal string with the OEBitVector. ToHexString method.

#### Listing 6: Storing fingerprint in SDF

```
if len(sys.argv) != 3:
    oechem.OEThrow.Usage("%s <infile> <outfile>" % sys.argv[0])
if s = oechem. oemolistream()if not ifs.open(sys.argv[1]):
    oechem. OEThrow. Fatal ("Unable to open %s for reading" % sys.argv[1])
ofs = occhem.oemolostream()if not ofs.open(sys.argv[2]):
    oechem. OEThrow. Fatal ("Unable to open %s for writing" % sys. argv[2])
if ofs.GetFormat() != oechem.OEFormat_SDF:
    oechem. OEThrow. Fatal ("% soutput file has to be an SDF file" % sys. argv[2])
fp = oeqraphsim.OEFingerPrint()for mol in ifs. GetOEGraphMols():
    oegraphsim. OEMakeFP(fp, mol, oegraphsim. OEFPType_Circular)
```

```
fptypestr = fp.GetFPTypeBase().GetFPTypeString()
fphexdata = fp.ToHexString()oechem. OESetSDData (mol, fptypestr, fphexdata)
oechem.OEWriteMolecule(ofs, mol)
```

The following example (Listing 7) shows how to retrieve fingerprints from an SDF file. When looping over the SD data the OEIsValidFPTypeString functions can be used to identify SD data that stores a fingerprint. The tag of the data is the string representation of the fingerprint type. This string representation can be used to generate the corresponding OEFPTypeBase object by using the OEGetFPType function. The type of the OEFingerPrint object then has to be set by the OEFingerPrint. SetFPTypeBase method. Finally, the bitvector of the fingerprint then can be initialized from the hexadecimal string by using the OEBitVector. FromHexString method.

#### **Listing 7: Retrieving fingerprint from SDF**

```
if len(sys.argv) != 2:
    oechem.OEThrow.Usage("%s <infile>" % sys.argv[0])
if s = oechem.oemolistream()if not ifs.open(sys.argv[1]):
    oechem. OEThrow. Fatal ("Unable to open %s for reading" % sys. argv[1])
if ifs.GetFormat() != oechem.OEFormat_SDF:
    oechem. OEThrow. Fatal ("%s input file has to be an SDF file" % sys. argv[1])
molcounter = 0fpcounter = 0for mol in ifs. GetOEGraphMols():
    molcounter += 1for dp in oechem. OEGetSDDataPairs (mol) :
        if oegraphsim. OEIsValidFPTypeString(dp.GetTag()):
             fpcounter += 1fptypestr = dp.GetTag()fphexdata = dp.GetValue()fp = oegraphsim.OEFingerPrint()fptype = oegraphsim. OEGetFPType (fptypestr)
             fp.SetFPTypeBase(fptype)
             fp.FromHexString(fphexdata)
print ("Number of molecules = \partial d" % molcounter)
print ("Number of fingerprints = \partial U'' \partial Y'' fpcounter)
```

- · OEFPTypeBase. GetFPTypeString method
- OEBitVector class
- SD Tagged Data Manipulation chapter in the OEChem TK manual

## **2.4 Similarity Measures**

The basic idea underlying similarity-based measures is that molecules that are structurally similar are likely to have similar properties. In a fingerprint the presence or absence of a structural fragment is represented by the presence or absence of a set bit. This means that two molecules are judged as being similar if they have a large number of bits in common.

Measuring molecular similarity or dissimilarity has two basic components: the representation of molecular characteristics (such as fingerprints) and the similarity coefficient that is used to quantify the degree of resemblance between two such representations.

## 2.4.1 Built-in Similarity Measures

Since different similarity coefficients quantify different types of structural resemblance, several built-in similarity measures are available in the GraphSim TK (see Table: Basic bit count terms of similarity calculation) The table below defines the four basic bit count terms that are used in fingerprint-based similarity calculations:

| Symbol           | Description                                           |                                                                                 |
|------------------|-------------------------------------------------------|---------------------------------------------------------------------------------|
| <i>onlyA</i>     | number of bits set “on” in fingerprint A but not in B | Image: illustration of fingerprints A and B with bits set only in A highlighted |
| <i>onlyB</i>     | number of bits set “on” in fingerprint B but not in A | Image: illustration of fingerprints A and B with bits set only in B highlighted |
| <i>bothAB</i>    | number of bits set “on” in both fingerprints          | Image: illustration of fingerprints A and B with common set bits highlighted    |
| <i>neitherAB</i> | number of bits set “off” in both fingerprints         | Image: illustration of fingerprints A and B with common off bits highlighted    |
| A                | number of bits set “on” in fingerprint A              |                                                                                 |
| B                | number of bits set “on” in fingerprint B              |                                                                                 |
| fpsize           | length of fingerprint in bits                         |                                                                                 |

|  |  |  |  | Table 1: Basic bit count terms of similarity calculation |  |
|--|--|--|--|----------------------------------------------------------|--|
|  |  |  |  |                                                          |  |

### **Cosine**

#### Formula:

$$
Sim_{Cosine}(A, B) = \frac{bothAB}{\sqrt{|A| * |B|}} = \frac{bothAB}{\sqrt{(onlyA + bothAB) * (onlyB + bothAB)}}
$$

### Range:

 $[0.0, 1.0]$ 

### **Example:**

![](_page_18_Figure_1.jpeg)

Calculates the ratio of the bits in common to the geometric mean of the number of "on" bits in the two fingerprints.

#### **Dice**

#### Formula:

$$
Sim_{Dice}(A, B) = \frac{2 * bothAB}{|A| + |B|} = \frac{2 * bothAB}{onlyA + onlyB + 2 * bothAB}
$$

#### Range:

 $[0.0, 1.0]$ 

#### **Example:**

![](_page_18_Figure_9.jpeg)

Calculates the ratio of the bits in common to the arithmetic mean of the number of "on" bits in the two fingerprints.

#### **Euclidean**

#### Formula:

$$
Sim_{Euclid}(A,B) = \sqrt{\frac{bothAB + neitherAB}{fpsize}} = \sqrt{\frac{bothAB + neitherAB}{onlyA + onlyB + bothAB + neitherAB}}
$$

#### Range:

 $[0.0, 1.0]$ 

#### **Example:**

![](_page_18_Figure_17.jpeg)

#### **Manhattan**

#### Formula:

$$
Sim_{Manhattan}(A, B) = \frac{onlyA + onlyB}{fpsize} = \frac{onlyA + onlyB}{onlyA + onlyB + bothAB + neitherAB}
$$

#### Range:

 $[0.0, 1.0]$ 

**Example:** 

| A | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |                                                                                                                                   |
|---|---|---|---|---|---|---|---|---|-----------------------------------------------------------------------------------------------------------------------------------|
| B | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 | $\frac{\text{only}A+\text{only}B}{\text{only}A+\text{only}B+\text{both}AB+\text{neither}AB}=\frac{1+2}{1+2+3+2}=\frac{3}{8}=0.37$ |

Note: Although  $Sim_{Manhattan}$  shares the same range with other similarity measures, it acts more like a distance measure, scoring more similar fingerprints lower. Identical fingerprints have  $Sim_{Manhattan}$  of 0.0 (as opposed to 1.0 in any other measure).

### **Tanimoto**

#### Formula:

$$
Sim_{Tanimoto}(A, B) = \frac{bothAB}{|A|+|B|-bothAB} = \frac{bothAB}{onlyA+onlyB+bothAB}
$$

Range:

 $[0.0, 1.0]$ 

#### **Example:**

![](_page_19_Figure_10.jpeg)

**Note:** The calculation of the OEFPType Lingo fingerprint is based on fragmenting canonical isomeric SMILES into overlapping four character long substrings. If any of the two SMILES being compared is shorter than four characters, then their Tanimoto score will be:

- 1.0, if the two SMILES are identical
- $\bullet$  0.0, otherwise.

### **Tversky**

#### Formula:

 $Sim_{Tversky}(A, B) = \frac{both AB}{\alpha * only A + \beta * only B + both AB}$ 

The Tversky similarity measure is asymmetric. Setting the parameters  $\alpha = \beta = 1.0$  is identical to using the Tanimoto measure.

The factor  $\alpha$  weights the contribution of the first 'reference' molecule. The larger  $\alpha$  becomes, the more weight is put on the bit setting of the reference molecule.

#### Range:

 $[0.0, 1.0]$ 

**Example:** 

| A | 1 | 0 | 1 | 1 | 1 | 0 | 0 | 0 |
|---|---|---|---|---|---|---|---|---|
| B | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |

$$
\frac{\text{both}AB}{\alpha\cdot\text{only}A + \beta\cdot\text{only}B + \text{both}AB}\;(\alpha = 2.0,\; \beta = 1.0) = \frac{3}{2.0\cdot1 + 1.0\cdot2 + 3} = \frac{3}{7} = 0.429
$$

**Note:** Although  $Sim_{Tversky}$  shares the same range with other similarity measures, its scaling can vary by orders of magnitude depending on the choice of  $\alpha$  and  $\beta$  parameters.

## **2.4.2 Similarity Calculation**

The following example demonstrates how to calculate  $Tanimoto$  similarity scores for the molecules depicted in Figure: Example molecules.

![](_page_20_Figure_6.jpeg)

**Generated by OEDepict TK** 

#### Fig. 4: Example molecules

#### **Listing 8: Calculating Tanimoto index**

```
molA = occhem.OEGraphMol()oechem.OESmilesToMol(molA, "clccc2c(c1)c(c(oc2=0)OCCSC(=N)N)Cl")
f pA = oegraphsim.OEFingerPrint()oegraphsim. OEMakeFP(fpA, molA, oegraphsim. OEFPType_MACCS166)
molB = occhem.OEGraphMol()oechem.OESmilesToMol(molB, "COc1cc2ccc(cc2c(=0)o1)NC(=N)N")
f p B = o e graph sim. O E Finger Print()oegraphsim. OEMakeFP(fpB, molB, oegraphsim. OEFPType_MACCS166)
molC = occhem.OEGraphMol()oechem. OESmilesToMol(molC, "COclc(c2ccc(cc2c(=0)o1)NC(=N)N)Cl")
fpC = oegraphsim.OEFingerPrint()oegraphsim. OEMakeFP(fpC, molC, oegraphsim. OEFPType_MACCS166)
print ("Tanimoto (A, B) = 8.3f'' % oegraphsim. OETanimoto (fpA, fpB))
```

```
print ("Tanimoto (A, C) = \frac{2}{3}. 3f" \frac{2}{3} oeqraphsim. OETanimoto (fpA, fpC))
print ("Tanimoto (B, C) = \frac{2}{3}. 3f" \frac{2}{3} oegraphsim. OETanimoto (fpB, fpC))
```

Molecules B and C (shown in Figure: Example Molecules) have the largest Tanimoto value since they share the largest number of common structural features.

For these example molecule the output of Listing  $\theta$  is the following:

```
Tanimoto (A, B) = 0.618Tanimoto (A, C) = 0.709Tanimoto (B, C) = 0.889
```

## **2.4.3 User-defined Similarity Measures**

The following code snippet demonstrates how implement the Yule similarity measure with the following formula:

```
Sim_{Yule}(A, B) = \sqrt{\frac{(both AB \cdot neither AB) - (only A \cdot only B)}{(both AB \cdot neither AB) + (only A \cdot only B)}}def CalculateYule(fpA, fpB):
     onlyA, onlyB, bothAB, neitherAB = oechem. OEGetBitCounts (fpA, fpB)
     yule = float (bothAB * neitherAB - onlyA * onlyB)
     yule /= float (bothAB * neitherAB + onlyA * onlyB)
     return yule
```

The OEGetBitCounts function returns the four basic values (namely onlyA, onlyB, bothAB and neitherAB) from which any similarity measures can be calculated. For the definition of these values see Table: Basic bit count terms

```
oegraphsim. OEMakeFP (fpA, molA, oegraphsim. OEFPType_Path)
oegraphsim. OEMakeFP(fpB, molB, oegraphsim. OEFPType_Path)
oegraphsim. OEMakeFP (fpC, molC, oegraphsim. OEFPType_Path)
print ("Yule (A, B) = 8.3f'' % CalculateYule (fpA, fpB))
print ("Yule (A, C) = \frac{2}{3}. 3f" \frac{2}{3} CalculateYule (fpA, fpC))
print ("Yule (B, C) = \frac{2}{3}. 3f" \frac{2}{3} CalculateYule (fpB, fpC))
```

Warning: User-defined similarity measures can only be used with circular, path, tree, and MACCS key fingerprints but not with LINGO (OEFPType Lingo).

## 2.5 Fingerprint Database

The following four examples perform the same task, detailed below:

- 1. reading a query structure
- 2. printing out the similarity score between the fingerprint of this query and the fingerprint generated for each molecule read from a database file.

In Listing 9, after importing the query structure and generating its path fingerprint, the program loops over the database file creating a path fingerprint for each structure. Then the program calculates the Tanimoto similarity between the fingerprint of the query and the database entry by calling the  $OETanimoto$  function.

#### Listing 9: Similarity calculation from file

```
if len(sys.argv) != 3:
    oechem.OEThrow.Usage("%s <queryfile> <targetfile>" % sys.argv[0])
if s = oechem.oemolistream()if not ifs.open(sys.argv[1]):
   oechem. OEThrow. Fatal ("Unable to open %s for reading" % sys. argv[1])
qmol = oechem. OEGraphMol()if not oechem. OEReadMolecule(ifs, qmol):
    oechem. OEThrow. Fatal ("Unable to read query molecule")
qfp = oegraphsim.OEFingerPrint()oegraphsim. OEMakeFP (qfp, qmol, oegraphsim. OEFPType_Path)
if not ifs.open(sys.argv[2]):
    oechem. OEThrow. Fatal ("Unable to open %s for reading" % sys. argv[2])
tfp = oeqraphsim.OEFingerPrint()for tmol in ifs. GetOEGraphMols():
    oegraphsim. OEMakeFP(tfp, tmol, oegraphsim. OEFPType_Path)
    print ("%.3f" % oegraphsim. OETanimoto (qfp, tfp))
```

In Listing 10 only the code block that is different from Listing 9 is shown.

In this example, it is assumed that the fingerprints are pre-calculated and stored in an OEB binary file as generic data attached to the corresponding molecules. The program loops over the file and accesses the pre-generated fingerprints or calculates them if they are not available.

The obvious advantage of this process is that the fingerprints one have to be generated once when the binary file is created. This can be significantly faster, than generating the fingerprints on-the-fly every time the program is executed.

#### See also:

The Storage and Retrieval section shows an example of how to generate an OEB binary file which stores molecule along with their corresponding fingerprints.

#### **Listing 10: Similarity calculation from OEB file**

```
tfp = oegraphsim.OEFingerPrint()for tmol in ifs. GetOEGraphMols():
   if tmol.HasData("PATH_FP"):
        tfp = tmol.GetData("PATH_FP")
   else:
        oechem. OEThrow. Warning ("Unable to access fingerprint for %s" % tmol.
\rightarrowGetTitle())
        oegraphsim. OEMakeFP(tfp, tmol, oegraphsim. OEFPType_Path)
    print ("%.3f" % oegraphsim. OETanimoto (qfp, tfp))
```

Listing 11 differs from Listing 9 in that it uses an OEFPDatabase object to store the generated fingerprints. The *OEFPDatabase* class is designed to perform in-memory fingerprint searches.

#### Listing 11: Similarity calculation with fingerprint database from file

```
fpdb = oegraphsim.OEFPDatabase(qfp.GetFPTypeBase())
for tmol in ifs. GetOEGraphMols():
    fpdb.AddFP(tmol)
for score in fpdb. GetScores (qfp) :
    print ("%. 3f" % score. GetScore ())
```

After building the fingerprint database, the scores can be accessed by the OEFPDatabase. Get Scores method. This will return an iterator over the similarity scores calculated.

Note: The OEFPDatabase only stores fingerprints and not the molecules from which they are generated. A correspondence between a molecule and its fingerprint stored in the database can be established by using the index returned by the OEFPDatabase. AddFP method.

#### See also:

Listing 13 shows how to keep track of the correspondence between a fingerprint added to a OEFPD atabase object and a molecule from which it is calculated.

In the last example (Listing 12), OEFPDatabase is used again to store the fingerprints. If the fingerprint is read from the OEB input binary file, then it is directly added to the database, otherwise the fingerprint is generated on-the-fly when passing the OEMolBase molecule itself to the OEFPDatabase. AddFP method.

#### Listing 12: Similarity calculation with fingerprint database from OEB

```
fpdb = oegraphsim. OEFPDatabase (qfp. GetFPTypeBase())
for tmol in ifs. GetOEGraphMols():
    if tmol.HasData("PATH_FP"):
        tfp = tmol. GetData("PATH FP")fpdb.AddFP(tfp)
    else:
        oechem. OEThrow. Warning ("Unable to access fingerprint for %s" % tmol.
\rightarrowGetTitle())
        fpdb.AddFP(tmol)
for score in fpdb. GetScores (qfp):
    print ("%.3f" % score. GetScore())
```

## 2.5.1 Sorted Search

Similarity searching based on a 2D representation of molecular structure (such as fingerprints) is one of the most common approaches for virtual screening. A molecule that is structurally similar to an active molecule is more likely to be active.

A virtual screening strategy involves going through a molecule database and calculating the similarity between a reference structure and each of the molecules, followed by ranking the similarity scores in descending order to identify molecules that are the most similar to the reference structure.

Listing 13 shows how to search a molecule database using the OEFPDatabase. GetSortedScores method to identify analogs based on their fingerprint similarity. First the molecules are imported using an OEMolDatabase object. Then a OEFPDatabase object is created that will store the corresponding fingerprints. Iterating over the molecules a fingerprints are added to the database by calling the OEFPDatabase. AddFP method. In case when a molecule can not be accessed from the OEMolDatabase object, an empty fingerprint is added to the OEFPDatabase object. This ensures that the indices of the two databases are synchronized. After generating the fingerprints, the program reads reference molecules (in the SMILES format) from standard input. Then the input SMILES string is parsed and the fingerprint database is searched to identify structures with the highest similarity scores. Finally, the SMILES string of the best hits are written to standard output.

#### **Listing 13: Similarity search in memory**

```
if len(sys.argv) != 2:
    oechem.OEThrow.Usage("%s <database>" % sys.argv[0])
ifs = oechem.oemolistream()
if not ifs.open(sys.argv[1]):
    oechem. OEThrow. Fatal ("Cannot open database molecule file!")
# load molecules
moldb = oechem.OEMolDatabase(ifs)
nrmols = moldb.GetMaxMolIdx()
# generate fingerprints
fpdb = oegraphsim. OEFPDatabase (oegraphsim. OEFPType Path)
emptyfp = oegraphsim.OEFingerPrint()
emptyfp.SetFPTypeBase(fpdb.GetFPTypeBase())
mol = occhem. OEGraphMol()for idx in range(0, nrmols):
    if moldb.GetMolecule(mol, idx):
        fpdb.AddFP(mol)
    else:
        fpdb.AddFP(emptyfp)
nrfps = fpdb. NumFingerPrints()timer = occhem.OEWallTimer()while True:
    # read query SMILES from stdin
    sys.stdout.write("Enter SMILES> ")
    line = sys.stdout.readline()line = line.rstrip()if len(line) == 0:
        sys.exit(0)# parse query
    query = oechem. OEGraphMol()
    if not oechem. OESmilesToMol(query, line):
        oechem. OEThrow. Warning ("Invalid SMILES string")
        continue
    # calculate similarity scores
```

```
timer. Start ()
   scores = fpdb.GetSortedScores(query, 5)
   oechem. OEThrow. Info("%5.2f seconds to search %i fingerprints" % (timer. Elapsed(),
\leftarrownrfps))
   hit = occhem.OEGraphMol()for si in scores:
       if moldb.GetMolecule(hit, si.GetIdx()):
            smi = oechem.OEMolToSmiles(hit)
            oechem. OEThrow. Info ("Tanimoto score %4.3f %s" % (si. GetScore(), smi))
```

As mentioned before, OEFPDatabase is a fingerprint container and does not store the corresponding molecule. Therefore the molecules have to be stored in a separate container in this case in an OEMolDatabase object. When the OEFPDatabase. GetSortedScores returns the iterator over the best similarity scores, the associated index can be utilized to access the corresponding structure in the OEMolDatabase object.

In the above example, the entire database was searched to identify structurally similar molecules. However, the user can also specify a segment of the database to be searched by providing a begin and end index.

See also:

- OEMolDatabase class in the **OEChem TK** manual
- Examples of fingerprint searches in the API section:
  - OEFPDatabase. GetScores method
  - OEFPDatabase, GetSortedScores method

## 2.5.2 Searching with User-defined Similarity Measures

By default, the Tanimoto similarity is used when calling either the OEFPDatabase. GetScores method or the OEFPDatabase. GetSortedScores method. The user can set other types of similarity measures to be applied by calling the OEFPDatabase. SetSimFunc method with a value from the OESimMeasure namespace. Each of the constants from this namespace corresponds to one of the built-in similarity calculation methods.

There is also a facility to use user-defined similarity measures when searching a fingerprint database. The following example shows how a similarity calculation can be implemented by deriving from the OESimFuncBase class.

```
Formula: Sim_{Simpson}(A, B) = \sqrt{\frac{bothAB}{min(onlyA + bothAB),(onlyB + bothAB))}}
```

class SimpsonSimFunc (oegraphsim. OESimFuncBase) :

```
def __call__(self, fpA, fpB):
   onlyA, onlyB, bothAB, neitherAB = oechem. OEGetBitCounts (fpA, fpB)
   if onlyA + onlyB == 0:
       return 1.0if both A = 0:
       return 0.0sim = float(bothAB)sim /= min(float(onlyA + bothAB), float(onlyB + bothAB))
   return sim
def GetSimTypeString(self):
   return "Simpson"
```

```
def CreateCopy(self):
   return SimpsonSimFunc()._disown_()
```

After implementing the similarity calculation, it can be added to an OEFPDatabase object, henceforth this new similarity calculation will be used.

```
fpdb = oegraphsim. OEFPDatabase (oegraphsim. OEFPType_Path)
fpdb.SetSimFunc(SimpsonSimFunc())
```

#### See also:

• The User-defined Similarity Measures section

## 2.6 User-defined Fingerprint

The previous *Fingerprint Generation* chapter showed how to create circular, path and tree fingerprints with default parameters. These default parameters are calibrated on the Briem-Lessel [Briem-Lessel-2000], Hert-Willett [Hert-Willett-2004] and Grant [Grant-2006] benchmarks.

However, the GraphSim TK also provides facilities to construct user-defined fingerprints. When constructing a userdefined fingerprint, the following parameters have to be considered:

- 1. Atom and bond typing that define which atom and bond properties are encoded into the fingerprints (see the Atom and Bond Typing section)
- 2. Size of the fragments that are exhaustively enumerated during the fingerprint generation (see the Fragment Size section)
- 3. Size of the generated fingerprint (in bits) (see the *Fingerprint Size* section)

The following code snippet shows how to generate a  $1024$  bit long fingerprint that encodes paths from 0 up to 5 bonds in length with default atom and bond properties defined by the OEFPAtomType\_DefaultAtom and OEFPBondType DefaultBond constants, respectively.

```
numbers = 1024minbonds = 0maxbonds = 5oegraphsim. OEMakePathFP(fp, mol, numbits, minbonds, maxbonds,
                        oegraphsim.OEFPAtomType_DefaultPathAtom,
                        oegraphsim.OEFPBondType_DefaultPathBond)
```

Warning: Two fingerprints which are generated with different parameters will have different fingerprint types!

In Listing 14, two fingerprints are generated with different parameters, namely they have a different number of bits. This means that they also have different types, therefore, no similarity value can be calculated between them.

Listing 14: Example of different path fingerprint types

```
f pA = oegraphsim.OEFingerPrint()numbits = 1024minbonds = 0maxbonds = 5oegraphsim. OEMakePathFP(fpA, mol, numbits, minbonds, maxbonds,
                         oegraphsim.OEFPAtomType_DefaultPathAtom,
                         oegraphsim.OEFPBondType_DefaultPathBond)
f p B = o e graph sim. O E Finger Print()numbers = 2048oegraphsim. OEMakePathFP(fpB, mol, numbits, minbonds, maxbonds,
                         oegraphsim.OEFPAtomType_DefaultPathAtom,
                         oegraphsim.OEFPBondType_DefaultPathBond)
print ("same fingerprint types = \frac{2}{3}r" % oegraphsim. OEIsSameFPType (fpA, fpB))
print (oegraphsim. OETanimoto (fpA, fpB))
```

The output of Listing 14 is the following:

```
same fingerprint types = False
Fatal: fingerprint type mismatch!
```

## 2.6.1 Atom and Bond Typing

Listing 15 shows how to generate fingerprints for two molecules with various atom and bond types (depicted in *Example molecules*). Reducing the number of atom and bond properties increases the similarity between the two molecules (i.e. their  $Tanimot \circ$  similarity). At the end, when only the topology of two molecules is considered, *i.e.*, whether or not their atoms and bonds belong to any ring system, the fingerprints of the two molecules become identical.

These effects are illustrated in Table: Examples of depiction molecule similarity based on fingerprints.

See also:

· Visualizing Molecule Similarity section

Listing 15: Similarity calculation with various atom/bond typing

```
def PrintTanimoto(molA, molB, atype, btype):
   f pA = oeqraphsim.OEFingerPrint()f p B = o e graph \sin .0 E F in g er Print()numbers = 2048minh = 0maxb = 5oegraphsim. OEMakePathFP (fpA, molA, numbits, minb, maxb, atype, btype)
    oegraphsim. OEMakePathFP (fpB, molB, numbits, minb, maxb, atype, btype)
    print ("Tanimoto (A, B) = 8.3f'' % oegraphsim. OETanimoto (fpA, fpB))
molA = occhem.OEGraphMol()oechem.OESmilesToMol(molA, "Oc1c2c(cc(c1)CF)CCCC2")
molB = occhem.OEGraphMol()oechem.OESmilesToMol(molB, "clccc2c(c1)c(cc(n2)CCl)N")
PrintTanimoto(molA, molB, oegraphsim.OEFPAtomType_DefaultAtom, oegraphsim.
 , OEFPBondType_DefaultBond)
```

```
PrintTanimoto(molA, molB, oegraphsim.OEFPAtomType_DefaultAtom | oegraphsim.
\small \qquad \qquad \mbox{-} {\tt OFFPatomType\_EqAromatic},oegraphsim.OEFPBondType_DefaultBond)
PrintTanimoto(molA, molB, oegraphsim.OEFPAtomType_Aromaticity, oegraphsim.
→OEFPBondType_DefaultBond)
PrintTanimoto(molA, molB, oegraphsim.OEFPAtomType_InRing, oegraphsim.OEFPBondType_
\rightarrowInRing)
```

![](_page_28_Figure_3.jpeg)

#### Fig. 5: Example molecules

The output of Listing 15 is the following:

| $\text{Tanimoto}(A, B) = 0.166$ |
|---------------------------------|
| $\text{Tanimoto}(A, B) = 0.241$ |
| $\text{Tanimoto}(A, B) = 0.592$ |
| $\text{Tanimoto}(A, B) = 1.000$ |

![](_page_29_Figure_1.jpeg)

Table 2: Examples of depiction molecule similarity based on finger-

Table: Atom typing options and Table: Bond typing options list the currently available typing options.

| Table 3: Atom typing options |  |  |
|------------------------------|--|--|
|                              |  |  |

| atom typing constant       | encoded atom property      |
|----------------------------|----------------------------|
| OEFPAtomType_Aromaticity   | OEAtomBase.IsAromatic      |
| OEFPAtomType_AtomicNumber  | OEAtomBase.GetAtomicNum    |
| OEFPAtomType_Chiral        | OEAtomBase.IsChiral        |
| OEFPAtomType_FormalCharge  | OEAtomBase.GetFormalCharge |
| OEFPAtomType_HCount        | OEAtomBase.GetTotalHCount  |
| OEFPAtomType_HvyDegree     | OEAtomBase.GetHvyDegree    |
| OEFPAtomType_Hybridization | OEAtomBase.GetHyb          |
| OEFPAtomType_InRing        | OEAtomBase.IsInRing        |

| Table 4: Atomic number modifiers |
|----------------------------------|
|----------------------------------|

| OEFPAtomType_EqAromatic      |  |
|------------------------------|--|
| OEFPAtomType_EqHalogen       |  |
| OEFPAtomType_EqHBondAcceptor |  |
| OEFPAtomType_EqHBondDonor    |  |

| bond typing constant   | encoded bond property |
|------------------------|-----------------------|
| OEFPBondType_BondOrder | GetOrder              |
| OEFPBondType_Chiral    | OEBondBase.IsChiral   |
| OEFPBondType_InRing    | OEBondBase.IsInRing   |

|  |  | Table 5: Bond typing options |
|--|--|------------------------------|
|  |  |                              |

#### See also:

- OEFPAt omType namespace
- OEFPBondType namespace

## 2.6.2 Fragment Size

Circular, path and tree-based fingerprint generation involves molecular graph traversal to identify all unique radial, linear or branched fragments, respectively. When a path or tree fingerprint is initialized, the minimum and maximum number of bonds of the fragments that are encoded into the fingerprint can be specified. See Figure: Example of enumerated path fragments with increasing number of bonds and Figure: Example of enumerated tree fragments with increasing number of bonds.

![](_page_30_Figure_8.jpeg)

#### **Generated by OEDepict TK**

#### Fig. 6: Example of enumerated path fragments with increasing number of bonds

In case of a circular fingerprint, the minimum and maximum radius of the enumerated fragments can be specified. See Figure: Example of enumerated circular fragments with increasing radius

For example, when generating a fingerprint of the molecule shown in *Figure: Example Molecule* with minimum and maximum length set to 0 and 3, respectively, only paths listed in the first four rows in Table: Enumerated Paths, are encoded into the fingerprint.

![](_page_31_Figure_1.jpeg)

**Generated by OEDepict TK** 

#### Fig. 7: Example of enumerated tree fragments with increasing number of bonds

![](_page_31_Figure_4.jpeg)

#### Fig. 8: Example of enumerated circular fragments with increasing radius

| Path length (in bonds) | <b>Generated Unique Paths</b>                                       |
|------------------------|---------------------------------------------------------------------|
| $\Omega$               | C, N, O                                                             |
|                        | $C-C, C-N, C-O$                                                     |
| $\bigcap$              | $C-C-C$ , $C-C-N$ , $C-C-O$ , $C-N-C$ , $N-C-O$                     |
|                        | $C-C-C-C$ , $C-C-C-N$ , $C-C-C-O$ , $C-C-N-C$ , $C-N-C-O$           |
| $\overline{4}$         | $C-C-C-C-C$ , $C-C-C-C-N$ , $C-C-C-C-O$ , $C-C-C-N-C$ , $C-C-N-C-C$ |
|                        | $O-C-N-C-C$                                                         |
|                        | $C-C-C-C-C-N$ , $C-C-C-C-C-0$ , $C-C-C-C-N-C$ , $C-C-C-N-C-C-N-C-C$ |
|                        | $C-C-C-N-C-O$                                                       |

|  | Table 6: Enumerated paths |  |
|--|---------------------------|--|
|--|---------------------------|--|

![](_page_32_Figure_1.jpeg)

Fig. 9: Example molecule

Figure: Example of enumerated paths depicts the six unique paths of length four that are generated for the example molecule. Each unique path is encoded only once without considering its frequency.

![](_page_32_Figure_4.jpeg)

Fig. 10: Example of enumerated paths

In the example shown in Listing 16, fingerprints with various minimum and maximum path length are generated for pyrrole and pyridine. When enumerating only paths that are shorter than four bonds, the fingerprints generated for the two molecules are identical. Since the four bond-length pattern ccccc is present in pyridine but not in pyrrole, the fingerprints become different, resulting in a smaller Tanimoto similarity score.

#### Listing 16: Similarity calculation with various path lengths

```
def PrintTanimoto(molA, molB, minb, maxb):
    f pA = oegraphsim.OEFingerPrint()f p B = o e graph \sin . 0 E F in g er Print()numbers = 2048atype = oegraphsim.OEFPAtomType_DefaultPathAtom
    btype = oegraphsim. OEFPBondType_DefaultPathBond
    oegraphsim. OEMakePathFP (fpA, molA, numbits, minb, maxb, atype, btype)
    oegraphsim. OEMakePathFP (fpB, molB, numbits, minb, maxb, atype, btype)
    print ("Tanimoto (A, B) = \frac{2}{3}. 3f" \frac{2}{3} oegraphsim. OETanimoto (fpA, fpB))
molA = occhem.OEGraphMol()oechem.OESmilesToMol(molA, "clccnccl")
```

```
molB = oechem.OEGraphMol()oechem.OESmilesToMol(molB, "clcc[nH]c1")
PrintTanimoto(molA, molB, 0, 3)
PrintTanimoto(molA, molB, 1, 3)
PrintTanimoto(molA, molB, 0, 4)
PrintTanimoto(molA, molB, 0, 5)
```

The output of Listing 16 is the following:

```
Tanimoto (A, B) = 1.000Tanimoto (A, B) = 1.000Tanimoto (A, B) = 0.950Tanimoto (A, B) = 0.731
```

## 2.6.3 Fingerprint Size

The previous sections explain how the atom and bond typing and encoded fragment size can effect the similarity scores. Selecting an adequate fingerprint size is also very crucial. The number of unique circular, path or tree fragments present in molecular structures can be extremely large, therefore the generated fragments have to be hashed into the fixed-length fingerprint. This means that a bit in a fingerprint does not correspond to a unique pattern exclusively (as it does in structural key). Also a bit has no particular structural meaning, *i.e.*, each bit represents the presence of a number of structural patterns.

The smaller the size of the fingerprints, the more dense they become, raising the probability of collisions. A collision occurs when different fragments are mapped to the same bit. This will inherently result in information loss and weaken the power to discriminate between structurally similar and dissimilar molecules. On the other hand, when the size of the fingerprints is too large they become very sparse, which will reduce information loss. However, the time spent to calculate similarity scores will increase.

The following table shows the number of unique paths generated for benzylpenicillin (depicted in Figure: Benzylpenicillin).

Note: The more atom and bond properties that are taken into account and the larger the size of paths to enumerate, the larger the size of the fingerprint has to be in order to encode the enumerated fragments without a significant number of bit collisions.

| Atom/Bond typing                                                  | path 0-3 | path 0-5 | path 0-7 |
|-------------------------------------------------------------------|----------|----------|----------|
| <i>AtomicNumber,BondOrder</i>                                     | 56       | 149      | 297      |
| <i>AtomicNumber   HvyDegree,BondOrder</i>                         | 111      | 265      | 453      |
| <i>AtomicNumber   HvyDegree   Aromaticity, BondOrder   InRing</i> | 126      | 297      | 499      |
| <i>DefaultAtom,DefaultBond</i>                                    | 147      | 362      | 617      |

| Table 7: Number of unique paths generated for Benzylpenicillin |  |  |
|----------------------------------------------------------------|--|--|
|----------------------------------------------------------------|--|--|

![](_page_34_Figure_1.jpeg)

#### Fig. 11: Benzylpenicillin

## 2.7 Fingerprint Coverage

Fingerprints are usually generated by enumerating various fragments (patterns) of a molecule and then hashing them into a fixed-length bitvector. The OEGetFPCoverage function provides access to these fragments by returning an iterator over OEAtomBondSet objects, each of which storing the atoms and bonds of a specific fragment.

#### See also:

• Fingerprint Patterns chapter that shows how to access more information about the fragments enumerated during the fingerprint generation

The following example shows how the retrieve the unique fragments that are enumerated when generating a path fingerprint. The obtained fragments are depicted in Table: Example of path fragments

#### Listing 17: Example of accessing patterns encoded into a fingerprint

```
mol = occhem.OEGraphMol()oechem.OESmilesToMol(mol, "CCNCC")
fptype = oegraphsim. OEGetFPType (oegraphsim. OEFPType_Path)
unique = Truefor idx, abset in enumerate (oegraphsim. OEGetFPCoverage (mol, fptype, unique)):
    print ("82d 8s" 8 ((idx + 1), "".join ([str(a) for a in abset. GetAtoms()])))
```

The output of Listing 17 is the following:

 $0<sup>C</sup>$  $\mathbf{1}$ 2  $0\quad C$  $1<sup>c</sup>$  $0 C$  $1\,c$  $\mathbf{3}$ 2 N  $0 C$ 1 C 2 N 3 C  $\overline{4}$  $\overline{5}$  $0 C$ 1 C 2 N 3 C 4 C  $\sqrt{6}$  $1<sup>c</sup>$  $\overline{7}$  $1\,c$ 2 N 8  $1\,c$ 2 N 3 C 2 N 3 C 4 C  $\overline{9}$  $1\,c$ 10 2 N

![](_page_35_Figure_1.jpeg)

Table 8: Example of unique path fragments. The numbers displayed next to atoms are the atom indices.

The OEGetFPCoverage function in the Listing 17 example is called with a unique options. This means that it returns only unique fragments, where a fragment (i.e. subgraph) is considered unique, if it differs from all other subgraphs identified previously by at least one atom or bond. For example, executing the same code with a non-unique option would generate five additional paths depicted in Table: Example of additional non-unique path fragments

![](_page_36_Figure_1.jpeg)

Table 9: Example of additional non-unique path fragments. The num-

See also:

- OEGetFPOverlap function
- Fingerprint Overlap chapter

## 2.8 Fingerprint Overlap

The OEGetFPOverlap function provides access to the fragments of two molecules that are considered equivalent based on a specific fingerprint type. This means that the returned fragment-pairs set the same bit "on" when fingerprints are generated. The following example shows how to retrieve the common five bond-length patterns of two molecules.

#### Listing 18: Example of accessing common patterns based on a fingerprint

```
pmol = oechem.OEGraphMol()
oechem.OESmilesToMol(pmol, "clcnc2c(c1)CC(CC2O)CF")
tmol = oechem. OEGraphMol()oechem.OESmilesToMol(tmol, "c1cc2c(cc1)CC(CC1)CC2N")
fptype = oegraphsim.OEGetFPType("Tree, ver=2.0.0, size=4096, bonds=5-5,""atype=AtmNum|HvyDeg|EqHalo,btype=Order")
for idx, match in enumerate (oegraphsim. OEGetFPOverlap (pmol, tmol, fptype)):
   ostring = "match 2d: " *(idx + 1)for mpair in match. GetAtoms () :
        p = mpair.patht = mpair.targetostring += "%d%s-%d%s " % (p. GetIdx(), oechem. OEGetAtomicSymbol(p.
\rightarrowGetAtomicNum()),
```

```
\rightarrowGetAtomicNum()))
   print (ostring)
```

t.GetIdx(), oechem.OEGetAtomicSymbol(t.

The first three matches returned by the Listing 18 are depicted in the next table. The output of code is the following:

```
match 1: 3C-2C 9C-11C 4C-3C 8C-10C 7C-7C 11C-8C
match 2: 3C-2C 4C-3C 5C-4C 6C-6C 7C-7C 8C-8C
match 3: 3C-2C 4C-3C 5C-4C 6C-6C 7C-7C 8C-10C
match 4: 3C-2C 4C-3C 5C-4C 6C-6C 7C-7C 11C-8C
match 5: 3C-2C 4C-3C 5C-4C 6C-6C 7C-7C 11C-10C
match 6: 3C-2C 9C-11C 4C-3C 6C-6C 7C-7C 11C-8C
\ldots truncated \ldots
```

![](_page_38_Figure_1.jpeg)

Table 10: Example of matches returned by the OEGetFPOverlap function. The numbers depicted next to the atoms are the atom indices.

**Warning:** Even though the  $OEGetFPOverlap$  function returns an iterator of OEMatchBase objects, they are not matches in the traditional sense, i.e. the atom-pair and bond-pair correspondences between the pattern and the target atoms and bonds are not guaranteed. See example depicted below.

![](_page_39_Figure_2.jpeg)

Fig. 12: The two highlighted patterns set the same bit when fingerprints are generated, but the returned match is not pairwise. The numbers depicted next to the atoms are the atom indices.

#### See also:

- · OEGetFPCoverage function
- Fingerprint Coverage chapter

**Hint:** The OEGetFPOverlap can be used to visualize molecule similarity based on a given fingerprint type. See more details in:

- Visualizing Molecule Similarity section
- Depicting Molecule Similarity section in OpenEye Python Cookbook

## **2.9 Fingerprint Patterns**

Fingerprints are usually generated by enumerating various fragments (patterns) of a molecule and then hashing them into a fixed-length bitvector. The OEGetFPPatterns function provides access to these patterns by returning an iterator over *OEFPPattern* objects, each of which has the atoms and bonds of a specific fragment along with the following information:

- the bit that is set when the pattern is hashed into a fixed-length bitvector
- the unhashed unique integer encoding of the pattern
- the SMARTS representation of the pattern that encodes the atom and bond properties that are specified in the given fingerprint type (OEFPTypeBase)

The following example shows how the retrieve the patterns that are enumerated when generating a tree fingerprint.

### Listing 19: Example of accessing patterns encoded into a fingerprint

```
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "NCC(=0)[0-]")
fptype = oegraphsim.OEGetFPType("Tree, ver=2.0.0, size=4096, bonds=0-4,""atype=AtmNum|Arom|FCharge|HvyDeg,btype=Order")
for idx, pattern in enumerate (oegraphsim. OEGetFPPatterns (mol, fptype)):
   atoms(r = " ".join([str(a) for a in pattern.GetAtoms())print ("82d 85d 850s 8s" 8 ((idx + 1), pattern. GetBit(), pattern. GetSmarts(),
\rightarrow atomstr) )
```

The output of Listing 19 is the following:

| 1  | 849  | [N;D1]                                  | 0 N |     |     |     |     |
|----|------|-----------------------------------------|-----|-----|-----|-----|-----|
| 2  | 1611 | [C;D2]                                  |     | 1 C |     |     |     |
| 3  | 740  | [C;D3]                                  |     |     | 2 C |     |     |
| 4  | 2841 | [O;D1]                                  |     |     |     | 3 O |     |
| 5  | 1589 | [O-;D1]                                 |     |     |     |     | 4 O |
| 6  | 2326 | [N;D1]-[C;D2]                           | 0 N | 1 C |     |     |     |
| 7  | 3764 | [C;D2](-[C;D3])-[N;D1]                  | 0 N | 1 C | 2 C |     |     |
| 8  | 2727 | [C;D2](-[C;D3]=[O;D1])-[N;D1]           | 0 N | 1 C | 2 C | 3 O |     |
| 9  | 859  | [C;D2](-[C;D3](-[O-;D1])=[O;D1])-[N;D1] | 0 N | 1 C | 2 C | 3 O | 4 O |
| 10 | 3537 | [C;D2](-[C;D3]-[O-;D1])-[N;D1]          | 0 N | 1 C | 2 C |     | 4 O |
| 11 | 3083 | [C;D3]-[C;D2]                           |     | 1 C | 2 C |     |     |
| 12 | 793  | [C;D2]-[C;D3]=[O;D1]                    |     | 1 C | 2 C | 3 O |     |
| 13 | 1574 | [C;D2]-[C;D3](-[O-;D1])=[O;D1]          |     | 1 C | 2 C | 3 O | 4 O |
| 14 | 3538 | [C;D2]-[C;D3]-[O-;D1]                   |     | 1 C | 2 C |     | 4 O |
| 15 | 1707 | [O;D1]=[C;D3]                           |     |     | 2 C | 3 O |     |
| 16 | 1472 | [C;D3](-[O-;D1])=[O;D1]                 |     |     | 2 C | 3 O | 4 O |
| 17 | 1397 | [O-;D1]-[C;D3]                          |     |     | 2 C |     | 4 O |

- OEFPPattern class
- · OEGetFPPatterns function
- OEGetFPType function
- Fingerprint Coverage chapter
- Fingerprint Overlap chapter

**THREE** 

## **GPU FAST FINGERPRINTS**

## **3.1 Prerequisites**

Fast fingerprint searching in Graphsim TK is GPU-enabled. In order to run searches on a GPU please refer to the guidelines below:

## 3.1.1 GPU-Related Requirements

The following is required in order to use GPU-accelerated OpenEye toolkits and applications:

#### **Supported Platforms**

CUDA-enabled OpenEye software is only available on supported Linux platforms. For supported Linux platforms see above and/or the Platform Support Page

### **Supported GPUs**

An NVIDIA Tesla, Quadro, or GeForce GPU with a **compute capability of 3.5** or higher is required on your system. For a comprehensive table of which GPUs fall into which compute capability category please refer to the CUDA wikipedia page.

#### **NVIDIA Drivers**

#### • Minimum NVIDIA Driver version: 450.x.

• CUDA is not required to be installed.

We recommend driver 450.80.02 and we strongly advise manually downloading and installing the appropriate NVidia driver for your system as opposed to using a package manager.

To install, root privilege is required. Follow these steps:

- 1. Download the driver to the machine you are installing it on.
- 2. chmod  $+x$  the driver package to make it executable.
- 3. Ensure you have disabled X-server by killing any running sessions. Reboot may be required if X-server is still running after this step.

Warning: Disabling X-server requires different processes to be killed depending on your Linux distribution. See Nvidia installation guide for more details.

**Warning:** The NVidia kernel module can often conflict with the open source Nouveau display drivers depending on your specific Linux distribution. The NVidia documentation is a much more complete and up-to-date source for information on how to work around this issue. See Disabling Nouveau on the NVIDIA website.

4. Install the driver by sudo ./NVIDIA-Linux-x86\_64-450.80.02.run and follow the step-by-step installation instructions.

For more details on driver installations see the CUDA Installation Guide

Note: The output of the nvidia-smi command is extremely useful when debugging GPU issues. Please include the output from nvidia-smi in any request to support@eyesopen.com.

#### **Performance Tuning**

To get the most performance out of an NVIDIA Graphics card, use the persistence daemon to switch persistence mode on across all cards on the system (root privilege required):

sudo nvidia-persistenced --user foo

This will automatically enable persistence mode after reboot.

For full instructions on persistence daemon see the Persistence daemon section of the NVIDIA docs.

## 3.2 Usage

An example of how to perform fast fingerprint searches can be found at Searching fast fingerprint database. To run using a GPU the OEFastFPDatabaseMemoryType\_CUDA constant is used to construct the OEFastFPDatabase object. If using the example script aforementioned, simply run the script with -memorytype CUDA.

- · OEFastFPDatabaseMemoryType namespace
- OEFastFPDatabase class
- OEFPDatabaseOptions class

## **FOUR**

## **EXAMPLES**

## **4.1 GraphSim TK Examples**

The following table lists the currently available GraphSim TK examples:

| Program                | Description                                             |
|------------------------|---------------------------------------------------------|
| <i>searchfp.py</i>     | building and searching fingerprint database             |
| <i>makefastfp.py</i>   | generating fingerprint file for fast fingerprint search |
| <i>searchfastfp.py</i> | searching fast fingerprint database                     |

#### **Examples:**

## 4.1.1 Building and searching fingerprint database

A program that builds a fingerprint database on-the-fly and then performs fingerprint search to identify molecules which are similar to a given query molecule

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python searchfp.py --help
```

will generate the following output:

```
Simple parameter list
fingerprint database search options
  -cutoff : Similarity cutoff value
  -descending : Order of similarity scores
  -limit : Maximum number of similarity scores
  -simfunc : Similarity measure
 fingerprint options
  -atomtype : Fingerprint atom type
  -bondtype : Fingerprint bond type
  -fptype : Fingerprint type
  -maxdistance : Maximum number of bonds/radius in path/circular/tree
   -mindistance : Minimum number of bonds/radius in path/circular/tree
  -numbits : Size of bitvector
```

```
input/output options
 -molfname : Input molecule filename
 -out : Output molecule filename
 -query : Input query filename
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
# Searching fingerprint database
######################################
import sys
from openeye import oechem
from openeye import oegraphsim
def main(argv=[__name__]):
   itf = oechem. 0EInterface()oechem. OEConfigure(itf, InterfaceData)
   defopts = oegraphsim. OEFPDatabaseOptions(10, oegraphsim. OESimMeasure_Tanimoto)
   oegraphsim.OEConfigureFPDatabaseOptions(itf, defopts)
   oegraphsim.OEConfigureFingerPrint(itf, oegraphsim.OEGetFPType(oegraphsim.OEFPType_
\rightarrowTree))
   if not oechem. OEParseCommandLine(itf, argv):
       return 0
   qfname = itf.GetString("-query")
   mfname = itf.GetString("-molfname")
   ofname = itf.GetString("-out")# initialize databases
   timer = oechem.OEWallTimer()
   timer. Start ()
```

```
if s = oechem.oemolistream()if not ifs.open(qfname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   query = oechem. OEGraphMol()
   if not oechem. OEReadMolecule(ifs, query):
       oechem. OEThrow. Fatal ("Cannot read query molecule!")
   moldb = occhem.OEMolDatabase()if not moldb. Open (mfname) :
       oechem. OEThrow. Fatal ("Cannot open molecule database!")
   ofs = occhem.oemolostream()if not ofs.open(ofname):
       oechem. OEThrow. Fatal ("Cannot open output file!")
   fptype = oeqraphsim. OESetupFingerPrint (itf)
   oechem.OEThrow.Info("Using fingerprint type %s" % fptype.GetFPTypeString())
   fpdb = oegraphsim. OEFPDatabase (fptype)
   emptyfp = oegraphsim.OEFingerPrint()emptyfp.SetFPTypeBase(fptype)
   nrmols = moldb. GetMaxMolldx()mol = occhem.OEGraphMol()for idx in range(0, nrmols):
       if moldb. GetMolecule (mol, idx) :
            fpdb.AddFP(mol)
       else:fpdb.AddFP(emptyfp)
   nrfps = fpdb. NumFingerPrints()
   oechem. OEThrow. Info("%5.2f sec to initialize databases" % timer. Elapsed())
   opts = oegraphsim. OEFPDatabaseOptions()
   oegraphsim.OESetupFPDatabaseOptions(opts, itf)
   # search fingerprint database
   timer.Start()
   scores = fpdb.GetSortedScores(query, opts)
   oechem. OEThrow. Info("$5.2f sec to search $d fingerprints" $ (timer. Elapsed(),
\rightarrownrfps))
   timer. Start ()
   hit = oechem.OEGraphMol()
   for si in scores:
       if moldb.GetMolecule(hit, si.GetIdx()):
            oechem.OEWriteMolecule(ofs, hit)
   oechem. OEThrow. Info("%5.2f sec to write %d hits" % (timer. Elapsed(), opts.
\rightarrowGetLimit()))
   return 0
```

```
InterfaceData = ""!BRIEF [-query] <molfile> [-molfname] <molfile> [-out] <molfile>
!CATEGORY "input/output options"
  !PARAMETER -query
   !ALIAS -q
   !TYPE string
   !REQUIRED true
   !KEYLESS 1
   !VISIBILITY simple
   !BRIEF Input query filename
  ! END
  !PARAMETER -molfname
   !ALIAS -mol
   !TYPE string
   !REQUIRED true
   !KEYLESS 2
    !VISIBILITY simple
   !BRIEF Input molecule filename
  ! END
 !PARAMETER -out
   !ALIAS -o
   !TYPE string
   !REQUIRED true
   KEYLESS 3
   !VISIBILITY simple
   !BRIEF Output molecule filename
  !END
!END
n \times nif __name__ == "_main_":
   sys.exit(main(sys.argv))
```

- OEFPDatabaseOptions class
- OEConfigureFPDatabaseOptions and OESetupFPDatabaseOptions functions
- · OEConfigureFingerPrint and OESetupFingerPrint functions
- OEMolDatabase class in OEChem TK manual
- OEFPDatabase class

### 4.1.2 Generating fingerprint file for fast fingerprint search

![](_page_48_Figure_2.jpeg)

![](_page_48_Figure_3.jpeg)

![](_page_48_Figure_4.jpeg)

See also:

- Example code in the Searching fast fingerprint database section
- Rapid Similarity Searching of Large Molecule File OpenEye Python Cookbook example

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python makefastfp.py --help

will generate the following output:

```
Simple parameter list
fingerprint options
  -atomtype : Fingerprint atom type
  -bondtype : Fingerprint bond type
  -fptype : Fingerprint type
  -maxdistance : Maximum number of bonds/radius in path/circular/tree
  -mindistance : Minimum number of bonds/radius in path/circular/tree
  -numbits : Size of bitvector
input/output options
  -fpdbfname : Output fingerprint database filename
  -in : Input molecule filename
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
# Generates binary fingerprint file for fast fingerprint search
#######################################
import sys
import os
from openeye import oechem
from openeye import oegraphsim
def main(argv=[_name_]):
   itf = oechem. 0EInterface()oechem.OEConfigure(itf, InterfaceData)
   oegraphsim.OEConfigureFingerPrint(itf, oegraphsim.OEGetFPType(oegraphsim.OEFPType_
\rightarrowTree))
   if not oechem. OEParseCommandLine(itf, argv):
       return 1
   ifname = \text{iff}. \text{GetString}("-in")ffname = itf. GetString(" - fpdb")if oechem. OEGetFileExtension (ffname) != "fpbin":
       oechem. OEThrow. Fatal ("Fingerprint database file should have '. fpbin' file,
\rightarrow extension!")
   idxfname = oechem.OEGetMolDatabaseIdxFileName(ifname)
   if not os.path.exists(idxfname):
       if not oechem. OECreateMolDatabaseIdx(ifname):
            oechem. OEThrow. Warning ("Unable to create %s molecule index file" %_
\rightarrowidxfname)
   oechem. OEThrow. Info ("Using %s index molecule file" % idxfname)
   moldb = oechem. OEMolDatabase()
```

```
(continued from previous page)
```

```
if not moldb. Open (ifname) :
        oechem. OEThrow. Fatal ("Cannot open molecule database file!")
   nrmols = moldb.GetMaxMolIdx()
   fptype = oegraphsim.OESetupFingerPrint(itf)
   oechem. OEThrow. Info ("Using fingerprint type %s" % fptype. GetFPTypeString())
   opts = oegraphsim. OECreateFastFPDatabaseOptions (fptype)
   opts. SetTracer(oechem. OEDots(100000, 1000, "fingerprints"))
    oechem. OEThrow. Info ("Generating fingerprints with %d threads" % opts.
\rightarrowGetNumProcessors())
   timer = occhem.OEWallTimer()if not oegraphsim. OECreateFastFPDatabaseFile(ffname, ifname, opts):
        oechem. OEThrow. Fatal ("Cannot create fingerprint database file!")
   oechem.OEThrow.Info("%5.2f secs to generate %d fingerprints" % (timer.Elapsed(),
\rightarrownrmols))
    return 0
InterfaceData = ""!BRIEF [-in] <input> [-fpdbfname] <output>
!CATEGORY "input/output options"
  !PARAMETER -in
   !ALIAS -i
   !TYPE string
   !REQUIRED true
    !KEYLESS 1
    !VISIBILITY simple
   !BRIEF Input molecule filename
  ! END
  !PARAMETER -fpdbfname
   !ALIAS -fpdb
   !TYPE string
   !REQUIRED true
   !KEYLESS 2
    !VISIBILITY simple
   !BRIEF Output fingerprint database filename
  !END
!END
H_1 and H_2if _name_ = = "_main_".sys.exit(main(sys.argv))
```

- · OEConfigureFingerPrint and OESetupFingerPrint functions
- OEGetMolDatabaseIdxFileName and OECreateMolDatabaseIdx functions in OEChem TK manual

- OEMolDatabase class in OEChem TK manual
- OECreateFastFPDatabaseOptions class
- · OECreateFastFPDatabaseFilefunction

## 4.1.3 Searching fast fingerprint database

A program that initializes a fast fingerprint database with the fingerprint file generated from the previous example and then performs a fingerprint search to identify molecules which are similar to a given query molecule.

![](_page_51_Figure_6.jpeg)

Fig. 2: Schematic representation of fast fingerprint search process

#### See also:

- Example code in the Generating fingerprint file for fast fingerprint search section
- Rapid Similarity Searching of Large Molecule File OpenEye Python Cookbook example

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python searchfastfp.py --help

will generate the following output:

Simple parameter list

```
fingerprint database options
 -memorytype : Fingerprint database memory type
fingerprint database search options
 -cutoff : Similarity cutoff value
  -descending : Order of similarity scores
 -limit : Maximum number of similarity scores
  -simfunc : Similarity measure
input/output options
 -fpdbfname : Input fast fingerprint database filename
 -molfname : Input molecule filename
 -out : Output molecule filename
 -query : Input query filename
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
# Searching fast fingerprint database
#######################################
import sys
from openeye import oechem
from openeye import oegraphsim
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface()
   oechem. OEConfigure (itf, InterfaceData)
   defopts = oegraphsim.OEFPDatabaseOptions(10, oegraphsim.OESimMeasure_Tanimoto)
   oegraphsim.OEConfigureFPDatabaseOptions(itf, defopts)
   oegraphsim.OEConfigureFPDatabaseMemoryType(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       return 0
```

```
qfname = itf.GetString("-query")
mfname = itf.GetString("-molfname")
ffname = itf.GetString("-fpdbfname")
ofname = itf.GetString("-out")
# initialize databases
timer = occhem.OEWallTimer()timer. Start ()
ifs = oechem.oemolistream()
if not ifs.open(qfname):
    oechem. OEThrow. Fatal ("Cannot open input file!")
query = occhem. OEGraphMol()if not oechem. OEReadMolecule (ifs, query) :
    oechem. OEThrow. Fatal ("Cannot read query molecule!")
moldb = occhem.OEMolDatabase()if not moldb. Open (mfname) :
    oechem. OEThrow. Fatal ("Cannot open molecule database!")
memberPhotype = oegraphsim.OEGetFPDatabaseMemoryType(itf)fpdb = oegraphsim. OEFastFPDatabase(ffname, memtype)
if not fpdb. IsValid():
    oechem. OEThrow. Fatal ("Cannot open fingerprint database!")
nrfps = fpdb. NumFinderPrints()member r = f pdb.GetMemoryTypesting()
ofs = occhem.oemolostream()if not ofs.open(ofname):
    oechem. OEThrow. Fatal ("Cannot open output file!")
if not oegraphsim. OEAreCompatibleDatabases (moldb, fpdb) :
    oechem. OEThrow. Fatal ("Databases are not compatible!")
oechem. OEThrow. Info("%5.2f sec to initialize databases" % timer. Elapsed())
fptype = fpdb.GetFPTypeBase()oechem. OEThrow. Info ("Using fingerprint type %s" % fptype. GetFPTypeString())
opts = oegraphsim. OEFPDatabaseOptions()
oegraphsim.OESetupFPDatabaseOptions(opts, itf)
# search fingerprint database
timer. Start()
scores = fpdb.GetSortedScores(query, opts)
oechem. OEThrow. Info ("%5.2f sec to search %d fingerprints %s"
                     % (timer.Elapsed(), nrfps, memtypestr))
timer.Start()
n^2 n n^2hit = occhem.OEGraphMol()for si in scores:
    if moldb.GetMolecule(hit, si.GetIdx()):
```

```
n^2 + 1oechem. OESetSDData(hit, "Similarity score", "%. 2f" % si. GetScore())
            oechem.OEWriteMolecule(ofs, hit)
    oechem. OEThrow. Info("%5.2f sec to write %d hits" % (timer. Elapsed(), nrhits))
    return 0
InterfaceData = ""!BRIEF [-query] <molfile> [-molfname] <molfile> [-fpdbfname] <fpfile> [-out]
\leftrightarrow<molfile>
!CATEGORY "input/output options"
  !PARAMETER -query
   !ALIAS -q
    !TYPE string
    !REQUIRED true
    !KEYLESS 1
    !VISIBILITY simple
    !BRIEF Input query filename
  !END
  !PARAMETER -molfname
   !ALIAS -mol
    !TYPE string
   !REQUIRED true
   !KEYLESS 2
   !VISIBILITY simple
    !BRIEF Input molecule filename
  !END
  !PARAMETER -fpdbfname
    !ALIAS -fpdb
    !TYPE string
    !REOUIRED true
    !KEYLESS 3
    !VISIBILITY simple
    !BRIEF Input fast fingerprint database filename
  ! END
  !PARAMETER -out
   !ALIAS -0
    !TYPE string
    !REQUIRED true
    !KEYLESS 4
    !VISIBILITY simple
    !BRIEF Output molecule filename
  ! END
! END
\overline{n},\overline{n},\overline{n}if name == " main ":
   sys.exit(main(sys.argv))
```

- OEFPDatabaseOptions class
- · OEConfigureFPDatabaseOptions and OESetupFPDatabaseOptions functions
- · OEConfigureFPDatabaseMemoryType and OEGetFPDatabaseMemoryType function
- OEMolDatabase class in **OEChem TK** manual
- · OEFastFPDatabaseMemoryType namespace
- OEFastFPDatabase class
- · OEAreCompatibleDatabases function

## **4.2 Python Cookbook Examples**

There are large number of code examples available in OpenEye Python Cookbook that use **OpenEye Toolkits** to solve a wide range of cheminformatics and molecular modeling problems.

- 2D Depiction chapter contains examples that illustrate how the OEDepict TK and Grapheme TK can be utilized to depict molecules and visualize properties calculated with other OpenEye toolkits.
- Visualizing 3D Information chapter contains examples that illustrate how the Grapheme TK can be utilized to project complex 3D information into the 2D molecular graph.
- Cheminformatics chapter contains examples that solve various cheminformatics problems such as similarity search, ring perception and manipulating molecular graphs.

#### **OpenEye Python Cookbook examples using OEGraphSim TK**

- Similarity Searching of Large Molecule Files
- Rapid Similarity Searching of Large Molecule File
- Finding Core Fragment of a Molecule Series
- Depicting Molecule Similarity Based on Fingerprints
- Drawing Fingerprint Score Histogram

## **FIVE**

**API** 

## **5.1 OEGraphSim Classes**

## 5.1.1 OECreateFastFPDatabaseOptions

class OECreateFastFPDatabaseOptions

This class represents the OECreateFastFPDatabaseOptions class that encapsulates properties that determine how fast fingerprints are generated when calling the OECreateFastFPDatabaseFile function.

#### See also:

- · OECreateFastFPDatabaseFile function
- Example code in Generating fingerprint file for fast fingerprint search section

#### **Constructors**

OECreateFastFPDatabaseOptions (const OEFPTypeBase \*fptype)

Constructs an OECreateFastFPDatabaseOptions object with the given fingerprints type.

#### See also:

• OEFPTypeBase class

Note: GraphSim TK currently only supports the popcount search method for fingerprints with the size of multiple of 256. This means that the OEFPType\_MACCS166 fingerprint type is currently not supported. When using other custom fingerprint types (see *User-defined Fingerprint* section) the size of the fingerprint must be a multiple of 256 in order to be able to search it with the popcount method.

#### **GetFPType**

const OEFPTypeBase \*GetFPType() const

Returns the fingerprint type in which the OECreateFastFPDatabaseOptions was constructed.

#### See also:

• OEFPTypeBase class

#### **GetNumProcessors**

unsigned int GetNumProcessors() const

generate fingerprints when calling Returns the number of threads that are used to the OECreateFastFPDatabaseFile function.

#### See also:

· OECreateFastFPDatabaseOptions. SetNumProcessors method

#### **SetNumProcessors**

void SetNumProcessors (unsigned int nrps)

Sets the number of threads used to generate fingerprints that are when calling the OECreateFastFPDatabaseFile function. When set to 0, the number of processors used will be the number returned by the OEGetNumProcessors function.

#### **SetTracer**

void SetTracer (const OESystem:: OEDots &dots)

Sets a tracer that can be used to show the progress of fingerprint generation.

#### See also:

• OEDots class in the OEChem TK manual

## 5.1.2 OEFastFPDatabaseParams

class OEFastFPDatabaseParams

This class represents the OEFastFPDatabaseParams class that can be used retrieve parameters from a binary fingerprint file that is generated with the OECreateFastFPDatabaseFile function.

#### See also:

· OECreateFastFPDatabaseFile function

### **Constructors**

OEFastFPDatabaseParams(const std::string &fpdbfname)

Constructor that parses the header of the given fingerprint file.

#### **GetFPTypeBase**

const OEFPTypeBase \*GetFPTypeBase() const

Returns the type of fingerprints stored in the file.

#### See also:

OEFPTypeBase class

#### **GetMolDatabaseFilename**

const std::string &GetMolDatabaseFilename() const

Returns the name of the molecule file from which the fingerprint file has been generated.

### **IslnLittleEndian**

bool IsInLittleEndian() const

Returns the endianness of the binary fingerprint file.

Note: Fast fingerprint search does not support endianness compatibility for performance reason. That means that a binary fingerprint file that has been generated in a little-endian computer cannot be search in a computer that uses the big-endian encoding.

#### **IsValid**

bool IsValid() const

Returns whether the header of the fingerprint file can be successfully parsed.

#### **NumFingerPrints**

size\_t NumFingerPrints() const

Returns the number of fingerprints stored in the fingerprint file.

## 5.1.3 OEFastFPDatabase

#### class OEFastFPDatabase

The OEFastFPDatabase class is designed to perform rapid CUDA-accelerated, in-memory or memory-mapped fingerprint searches using the popcount method. Each OEFastFPDatabase object is associated with a fingerprint type (OEFPTypeBase) that is set when the database is initialized from a pre-generated binary fingerprint file.

For CUDA-accelerated fingerprint searching please see the *prerequisites* for *OpenEye's GPU-accelerated software*.

Note: GraphSim TK currently only supports the popcount search method for fingerprints with the size of multiple of 256. This means that the OEFastFPDatabase class currently does not support:

- OEFPType\_MACCS166 fingerprint type
- OEFPType\_Lingo fingerprint type
- other custom fingerprint types (see *User-defined Fingerprint* section) with size that is not a multiple of 256

For the fingerprint types listed above, the original OEFPDatabase class can be utilized.

Note: OEFastFPDatabase gives identical results to OEFPDatabase. However, OEFPDatabase calculates similarity scores in single precision (float) while OEFastFPDatabase uses double precision. As a result, small similarity score differences can be observed.

#### See also:

• OEFPDatabase class

#### **Code Example**

- Example code in the *Generating fingerprint file for fast fingerprint search* section
- Example code in the Searching fast fingerprint database section
- Rapid Similarity Searching of Large Molecule File OpenEye Python Cookbook recipe
- Depicting Molecule Similarity Based on Fingerprints OpenEye Python Cookbook recipe

#### **Constructors**

OEFastFPDatabase(const std::string &dbfile, unsigned int memtype=OEFastFPDatabaseMemoryType::Default)

Constructs an *OEFastFPDatabase* object.

- **dbfile** The name of the file which contains the fingerprint data. The file has to be generated with the OECreateFastFPDatabaseFilefunction.
- memtype Defines whether the fingerprints are pre-loaded into GPU-memory, CPU-memory, or memory-mapped during the search process. This value has to be from the  $OEFastFDL \\ \text{tabaseMemoryType}$  namespace.

Note: If the OEFastFPDatabase object can not be initialized with the OEFastFPDatabaseMemoryType\_CUDA option, the following warning message will be throw:

![](_page_60_Figure_1.jpeg)

Fig. 1: Schematic representation of fast fingerprint search process

```
Warning: OEFastFPDatabase:: OEFastFPDatabase() : no CUDA-enabled
device available falling back to memory-mapped type!
```

As a rule of thumb, 1 million finger prints requires 0.6GB of GPU memory. GPU memory can be queried using the nvidia-smi command from terminal.

#### See also:

• OEFastFPDatabaseMemoryType namespace.

#### **GetAllScores**

OESystem:: OEIterBase<float> \*GetAllScores(const OEFPDatabaseOptions &opts) const

Performs  $NxN$  similarity calculations between all pairs of fingerprints stored in the OEFastFPDatabase object. It returns an iterator over the calculated similarity scores. The scores are not sorted, but returned as a flattened square matrix.

For all similarity measures other than *Tversky*, the returned 'matrix' will be symmetrical.

**opts** The OEFPDatabaseOptions object controls all the parameters that determine the search (i.e. similarity measure parameters). Cutoff and order parameters are ignored as the results are not filtered or sorted.

Note: This operation scales with  $n^2$  in memory and can easily overwhelm the system memory for larger databases. Therefore, the OEFastFPDatabase. GetRawScores method returns a single row of the similarity matrix and is the recommended usage for querying large databases.

#### See also:

• OEFPDatabaseOptions class

#### **GetFingerPrint**

bool GetFingerPrint (OEFingerPrint& fp, size\_t idx) const

Returns the  $idx^{th}$  fingerprint of the database.

Warning: This function returns false if the fingerprint index is not identical to the corresponding molecule index. This can occur if the fingerprint binary file is generated in multi-thread process. If direct access to the fingerprint is required when using the OEFastFPDatabase. GetFingerPrint method, the fingerprint file should be generated in a single-threaded mode. This can be done by setting  $SetNumProcessors(1)$  for the option class used for creating the binary file.

#### See also:

- OEFingerPrint class
- · OECreateFastFPDatabaseOptions.GetNumProcessors method
- OECreateFastFPDatabaseOptions. SetNumProcessors method

#### **GetFPTypeBase**

const OEFPTypeBase \*GetFPTypeBase() const

Returns the fingerprint type of the OEFastFPDatabase object. An OEFastFPDatabase object can only store fingerprints with identical types.

#### **GetHistogram**

OEFPHistogram \*GetHistogram (const OEFPDatabaseOptions &opts, const size\_t nrbins=200u) const

Performs similarity calculations between all pairs of fingerprints stored in the OEFastFPDatabase object. It returns the histogram over the calculated similarity scores in a OEFPHistogram object.

opts The OEFPDatabaseOptions object contains the settings available to control the search (i.e. similarity measure,  $\alpha$  and  $\beta$  parameters for *Tversky* similarity). Cutoff and order parameters are ignored as the results are not filtered or sorted.

**nrbins** Number of bins in the returned OEFPHistogram object.

Note: For all similarity measures other than Tversky, the histogram only contains the upper-triangular similarity scores (excluding the diagonal). In case of the asymmetric *Tversky* similarity measure, the histogram of the whole  $NxN$  matrix is returned.

Note: When the OEFastFPDatabase object is initialized with OEFastFPDatabaseMemoryType\_CUDA, nrbins is limited to at most 1024.

**Hint:** This method calculates similarities identically to OEFastFPDatabase. GetAllScores but is not bound by the system memory. It can be used to quickly obtain statistics on larger databases.

See also:

- OEFPDatabaseOptions class
- OEFPHistogram class

#### **GetMemoryType**

unsigned int GetMemoryType() const

Returns the memory type of the fingerprint database. The return value is taken from the OEFastFPDatabaseMemoryType namespace.

#### See also:

· OEFastFPDatabase. GetMemoryTypeString method

#### **GetMemoryTypeString**

std::string GetMemoryTypeString() const

Returns the string representation if memory type of the fingerprint database.

See also:

• OEFastFPDatabase. GetMemoryType method

#### **GetMoleculeIndex**

size t GetMoleculeIndex (const size t fpidx) const

Returns the molecule index that corresponds to the fingerprint index.

Note: When building fingerprint databases using OECreateFastFPDatabaseOptions, the molecule index is always the same as the fingerprint index. However, there are private database building APIs that allow to specify the molecule index associated with each fingerprint. This OEFastFPDatabase. GetMoleculeIndex method allows to handle these private databases.

#### **GetRawScores**

```
OESystem::OEIterBase<double> *GetRawScores(const size_t fpidx,
                                           const OEFPDatabaseOptions &opts) const
OESystem::OEIterBase<double> *GetRawScores(const OEFingerPrint &fp,
                                          const OEFPDatabaseOptions &opts) const
OESystem:: OEIterBase<double> *GetRawScores(const OEChem:: OEMolBase &mol,
                                           const OEFPDatabaseOptions &opts) const
```

Performs similarity calculations between a molecule or a fingerprint and the fingerprints stored in the OEFastFP-Database object. It returns an iterator over the calculated similarity scores. The scores are not sorted, but returned in the same order as the database. The number of elements in the returned iterator is equal to the number of fingerprints in the database.

- **fpidx** If the method is called with an integer index, the query fingerprint is taken from the OEFastFPDatabase object with the given index.
- mol If the method is called with an OEMolBase object, a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **fp** If the method is called with an OEFingerPrint object, its type has to match the type of the OEFastFPDatabase.
- **opts** The *OEFPDatabaseOptions* object contains the settings available to control the search (i.e. similarity measure parameters). Cutoff and order parameters are ignored as the results are not filtered or sorted.

See also:

- OEFPDatabaseOptions class
- OEFastFPDatabase, GetAllScores method

#### **GetScores**

```
OESystem:: OEIterBase<OESimScore> *GetScores (const size_t idx,
                                            const OEFPDatabaseOptions &opts) const
OESystem::OEIterBase<OESimScore> *GetScores(const OEFingerPrint &fp,
                                            const OEFPDatabaseOptions &opts) const
OESystem::OEIterBase<OESimScore> *GetScores(const OEChem::OEMolBase &mol,
                                            const OEFPDatabaseOptions &opts) const
```

Performs similarity calculations between a molecule or fingerprint and the fingerprints stored in the OEFastFP-Database object. It returns an iterator over the calculated similarity scores (OESimScore). The results are filtered according to the cutoff and order parameters specified in opts, but are not sorted.

- fpidx If the method is called with an integer index, the query fingerprint is taken from the OEFastFPDatabase object with the given index.
- mol If the method is called with an OEMolBase object, a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **fp** If the method is called with an OEFingerPrint object, its type has to match the type of the OEFastFPDatabase.
- opts The OEFPDatabaseOptions object controls all the parameters that determine the search (i.e. similarity measure parameters, score cutoff and order).

#### $S_{\rho\rho}$ also:

• OEFPDatabaseOptions class

### **GetSortedScores**

```
OESystem:: OEIterBase<OESimScore> *GetSortedScores (const size_t idx,
                                                      const OEFPDatabaseOptions &opts)
\leftarrowconst
OESystem::OEIterBase<OESimScore> *GetSortedScores(const OEFingerPrint &fp,
                                                      const OEFPDatabaseOptions &opts)
\rightarrow const
OESystem::OEIterBase<OESimScore> *GetSortedScores(const OEChem::OEMolBase &mol,
                                                      const OEFPDatabaseOptions &opts)
\rightarrowconst
```

Performs similarity calculations between a molecule or fingerprint and the fingerprints stored in the OEFastFP-Database object. It returns an iterator over the calculated similarity scores (OESimScore) in sorted order. Each OESimScore holds a similarity score and index of the corresponding fingerprint of the database.

- fpidx If the method is called with an integer index, the query fingerprint is taken from the OEFastFPDatabase object with the given index.
- **mol** If the method is called with an OEMolBase object, a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **fp** If the method is called with an OEFingerPrint object, its type has to match the type of the OEFastFPDatabase.
- **opts** The OEFPDatabaseOptions object controls all the parameters that determine the search (i.e. similarity measure parameters, score cutoff, order and limit).

See also:

• OEFPDatabaseOptions class

#### **GetSparseMatrix**

```
OESystem::OEIterBase<OESimScorePair> *GetSparseMatrix(const OEFPDatabaseOptions &
\rightarrow opts) const
```

Performs NxN similarity calculations between all pairs of fingerprints stored in the OEFastFPDatabase object and returns either the top K scores for each fingerprint or all scores above a cutoff for each fingerprint. The sparse matrix is returned as an iterator over *OESimScorePair* objects. The limit of scores to return can be set using OEFPDatabaseOptions. SetLimit and the cutoff of scores to return can be set using OEFPDatabaseOptions. SetCutoff. If no limit is set, all scores will be returned above the cutoff value. If a limit is set, only OEFPDatabaseOptions. GetLimit scores will be returned regardless of whether more scores fall within the cutoff range. A limit should be set for best performance.

opts The OEFPDatabaseOptions object controls all the parameters that determine the search (i.e. similarity measure parameters).

**Hint:** This operation scales with  $n^2$  in memory when limit = 0 (or when limit is not set), so it can easily overwhelm the system memory for larger databases. The best practice is to set a reasonable limit that will capture the scores of interest.

- OEFPDatabaseOptions class
- OESimScorePair class

#### GetVariogram

```
OEGraphSim::OEFPVariogram *GetVariogram(const std::vector<float>& obsdata,
                                        const OEFPDatabaseOptions &opts,
                                        const size_t nrbins=200u) const
```

Performs similarity calculations between all pairs of fingerprints stored in the OEFastFPDatabase object. It returns the empirical variogram over the calculated similarity scores with respect to the measurements provided in the obsdata parameter in a OEFPVariogram object.

obsdata User-provided empirical measurements for each fingerprint in the database.

opts The OEFPDatabase Options object controls all the parameters that determine the scoring (i.e. similarity measure parameters). Cutoff and order parameters are ignored as the results are not filtered or sorted.

nrbins Number of bins in the returned OEFPVariogram object.

Note: The empirical variogram is defined over distances rather than similarities. It is therefore not possible to calculate a variogram using *Tversky* similarity. For all other similarity measures, empirical variogram is calculated using  $distance = 1 - similarity$ .

**Hint:** This method calculates similarities identically to OEFastFPDatabase. GetAllScores but is not bound by the system memory. It can be used to quickly obtain statistics on larger databases.

Note: When the OEFastFPDatabase object is initialized with OEFastFPDatabaseMemoryType\_CUDA, nrbins is limited to at most 1024.

**Hint:** The returned OEFPVariogram object also contains a histogram, but note that this histogram is over **distances** rather than similarities.

#### See also:

- OEFPDatabaseOptions class
- OEFPVariogram class

**IsValid** 

bool IsValid() const

Returns whether the database was initialized correctly.

#### **NumFingerPrints**

```
size_t NumFingerPrints() const
```

Returns the number of OEFingerPrint objects stored in the database.

#### **SortedSearch**

```
unsigned SortedSearch (OESimSearchResult & result,
                      const OEChem:: OEMolBase &mol,
                      const OEFPDatabaseOptions &opts) const
```

Performs multi-threaded similarity calculations between a molecule and the fingerprints stored in the OEFastFP-Database object. The method combines the functionality of the OEFastFPDatabase. GetSortedScores and the OEFastFPDatabase. GetHistogram methods.

- result The OESimSearchResult object that stores the result of the search along with the progress of the search and the histogram of all scores.
- mol If the method is called with an OEMolBase object, a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **opts** The OEFPDatabaseOptions object controls all the parameters that determine the search (i.e. similarity measure parameters). The OEFastFPDatabase. SortedSearch method can use multiple threads to accelerate the search process. The number of processors used can be controlled by the OEFPDatabaseOptions. SetNumProcessors method.

The OEFastFPDatabase, SortedSearch method returns:

- OESimSearchStatus Uninitialized if the similarity search can not be executed
- OESimSearchStatus\_Finished, if the similarity search successfully finished

Note: This method is currently only available in OEFastFPDatabaseMemoryType\_MemoryMapped and OEFastFPDatabaseMemoryType InMemory modes.

**Example:** 

```
query = occhem.OEGraphMol()oechem.OESmilesToMol(query, "Cclc(c2cc(ccc2n1C(=0)c3ccc(cc3)Cl)OC)CC(=0)O")
limit = 5opts = oegraphsim.OEFPDatabaseOptions(limit, oegraphsim.OESimMeasure_Tanimoto)
nrbins = 5result = oegraphsim. OESimSearchResult (nrbins)
status = fpdb. SortedSearch (result, query, opts)
print ("Search status = \{ )". format (oegraphsim. OESimSearchStatusToName (status)))
print ("Number of searched = \{ )". format (result. NumSearched()))
```

```
# print scores
for score in result. GetSortedScores():
    print ("{:.3f}".format(score.GetScore()))
# print histogram
hist = result.GetHistogram()
bounds = hist.GetBinBoundedaries()for idx, count in enumerate (hist. GetCounts ()) :
    print (\ulcorner [\cdot : .3f] - \{ : .3f\} \urcorner = \{ \} \urcorner. format (bounds [idx], bounds [idx+1], count))
```

The output of the code snippet above might look like this:

```
Search status = Finished
Number of searched = 10000.9500.912
0.9010.886
0.859[0.000-0.200] = 428[0.200-0.400] = 312[0.400-0.600] = 225[0.600-0.800] = 25[0.800-1.000] = 10
```

See also:

- OEFastFPDatabase. GetSortedScores method
- OEFastFPDatabase. GetHistogram method
- · OESimSearchStatus namespace

## 5.1.4 OEFingerPrint

class OEFingerPrint : public OESystem:: OEBitVector

OEFingerPrint class is used to encode molecular properties. An OEFingerPrint object is a typed bitvector (OEBitVector). The type of an OEFingerPrint object is set when it is initialized.

#### See also:

- · OEFingerPrint.GetFPTypeBase
- · OEFingerPrint. SetFPTypeBase

The following methods are publicly inherited from OEBitVector:

| operator<   | FirstBit      | PrevBit     |
|-------------|---------------|-------------|
| operator=   | FromHexString | SetBitOff   |
| operator-=  | GetData       | SetBitOn    |
| operator[]  | GetSize       | SetData     |
| operator^=  | IsBitOn       | SetRangeOff |
| operator =  | IsEmpty       | SetRangeOn  |
| operator &= | LastBit       | SetSize     |
| ClearBits   | NegateBits    | ToHexString |
| CountBits   | NextBit       | ToggleBit   |

#### **Constructors**

OEFingerPrint()

Default constructor that creates an *OEFingerPrint* object with an uninitialized type, zero pointer (*OEFPTypeBase*).

OEFingerPrint (const OEFingerPrint & rhs)

Copy constructor.

#### operator=

OEFingerPrint & operator=(const OEFingerPrint & rhs)

Assignment operator that copies the data of the rhs OEFingerPrint object into the left-hand side OEFingerPrint object.

#### operator==

bool operator == (const OEFingerPrint& rhs) const

Two OEFingerPrint objects are considered to be equivalent only if they have the same fingerprint type (OEFPType-Base) and have identical bit-vectors (OEBitVector).

#### operator!=

bool operator!=(const OEFingerPrint& rhs) const

Two OEFingerPrint objects are considered to be different if either they have different fingerprint types (OEFPType-Base) or they have different bit-vectors (OEBitVector).

#### operator bool

 $IsValid() \rightarrow bool$ 

Returns whether the *OEFingerPrint* has been initialized, *i.e.*, has a valid type.

#### **GetFPTypeBase**

const OEFPTypeBase \*GetFPTypeBase() const

Returns a const pointer to the fingerprint type (OEFPTypeBase) of the OEFingerPrint object. This method will return 0 if the OEFingerPrint object has not been initialized.

#### **SetFPTypeBase**

void SetFPTypeBase (const OEFPTypeBase \*t)

Sets the fingerprint type of a OEFingerPrint object.

The following functions set the type of the fingerprint when an OEFingerPrint object is initialized:

- OEMakeFP
- · OEMakeMACCS166FP
- OEMakeLingoFP
- · OEMakePathFP
- · OEMakeCircularFP
- OEMakeTreeFP

Warning: Use this method with caution.

The type of a OEFingerPrint object (that is an OEFPTypeBase) encodes how the fingerprint is generated. Changing this type can mean that the information represented by bitvector of the fingerprint will be misinterpreted.

## 5.1.5 OEFPDatabase

#### class OEFPDatabase

The OEFPDatabase class is designed to perform rapid in-memory fingerprint searches. Each OEFPDatabase object is associated with a fingerprint type (OEFPTypeBase) that is specified when the database is constructed. An OEFP-Database object can only store fingerprints (OEFingerPrint) with this specified type.

#### See also:

• OEFastFPDatabase class

#### **Constructors**

OEFPDatabase (unsigned int fptype)

Creates an OEFPDatabase object that can store OEFingerPrint objects with a given type.

**fptype** The type of the OEFingerPrint object stored in the OEFPDatabase. This value has to be from the OEFPType namespace.

OEFPDatabase (const OEGraphSim:: OEFPTypeBase \*)

Creates an OEFPDatabase object that can store OEFingerPrint objects with OEFPTypeBase type.

Note: By default, an OEFPDatabase object is constructed with:

- no cutoff value
- Tanimoto similarity measure
- descending order to return scores when calling the OEFPDatabase. GetSortedScores method

These default values can be altered by the following methods:

- · OEFPDatabase. SetCutoff
- · OEFPDatabase. SetSimFunc

#### **AddFP**

unsigned int AddFP (const OEChem:: OEMolBase &mol)

Generates an OEFingerPrint object from the OEMolBase molecule with the fingerprint type of the OEFPDatabase. The generated OEFingerPrint object is then inserted into the database returning its index. This method will return  $-1$ , if the fingerprint generation was unsuccessful.

unsigned int AddFP (const OEGraphSim:: OEFingerPrint &fp)

Creates a copy of the OEFingerPrint object, inserts it into the database, and then returns its index. If the type of the passed fingerprint was different from the type of the database, than the insertion is unsuccessful and this method will return  $-1$ .

**Note:** The index returned by the OEFPDatabase. AddFP method is a unique number starting from zero. This index can be used as a reference number to associate the fingerprint with the molecule from which is it generated.

#### **ClearCutoff**

void ClearCutoff()

Removes the cutoff value previously set by the OEFPDatabase. Set Cutoff method. After clearing the cutoff value OEFPDatabase. HasCutoff method will return false.

#### See also:

- · OEFPDatabase. GetCutoff
- · OEFPDatabase. HasCutoff
- · OEFPDatabase. SetCutoff

#### **GetCutoff**

float GetCutoff() const

Returns the cutoff value previously set by the OEFPDatabase. SetCutoff method.

- · OEFPDatabase. ClearCutoff
- · OEFPDatabase. HasCutoff
- · OEFPDatabase. SetCutoff

#### **GetDescendingOrder**

bool GetDescendingOrder() const

Returns the order in which the calculated scores are returned by the OEFPDatabase. GetSortedScores method.

#### See also:

· OEFPDatabase. SetDescendingOrder

#### **GetFPTypeBase**

const OEGraphSim:: OEFPTypeBase \*GetFPTypeBase() const

Returns the fingerprint type of the OEFPDatabase object.

#### **GetFingerPrints**

OESystem:: OEIterBase<const OEGraphSim:: OEFingerPrint> \*GetFingerPrints() const

Returns an iterator pointer over fingerprints (OEFingerPrint) stored in the OEFPDatabase object. The returned OEFingerPrint objects can only be accessed by const methods or functions, *i.e.*, they can not be modified.

#### **GetScores**

| Link                            | Description                                                   |
|---------------------------------|---------------------------------------------------------------|
| <i>GetScores(mol, bgn, end)</i> | returns similarities for a molecule                           |
| <i>GetScores(fp, bgn, end)</i>  | returns similarities for a fingerprint                        |
| <i>GetScores(mol, opts)</i>     | returns similarities for a molecule with the given options    |
| <i>GetScores(fp, opts)</i>      | returns similarities for a fingerprint with the given options |

#### Table 1: The overloaded versions of the GetScores method

#### **Similarity calculation:**

```
OESystem:: OEIterBase<OEGraphSim:: OESimScore> *
  GetScores (const OEChem:: OEMolBase & mol, unsigned int bgn=0,
            unsigned int end=0) const
```

```
OESystem:: OEIterBase<OEGraphSim:: OESimScore> *
  GetScores (const OEGraphSim:: OEFingerPrint & fp, unsigned int bgn=0,
            unsigned int end=0) const
```

Performs similarity calculation between a given molecule or a fingerprint and the fingerprints stored in the OEFPDatabase object. It returns an iterator over the calculated similarity scores (OESimScore). Each OESimScore holds a similarity score and index of the corresponding fingerprint of the database.

- **mol** If the method is called with an OEMolBase object, then a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **fp** If the method is called with an *OEFingerPrint* object, then its type has to match with the type of the OEFPDatabase.

bgn, end The bqn and end arguments define the segment of the database on which the similarity calculation will take place. If both of these parameters are omitted (or set to zero), then the similarity calculation is performed on the entire fingerprint database.

#### Note:

- By default, the OEFPDatabase. GetScores methods calculates Tanimoto similarity scores and will always return these scores in the order in which the corresponding OEFingerPrint objects are added to the database.
- By using the OEFPDatabase. Set SimFunc method, similarity measures other than the default can be performed.
- The behavior of OEFPDatabase. GetSortedScores is also influenced by the cutoff value (OEFPDatabase. SetCutoff) of the database and the order of the scores specified by the OEFPDatabase. SetSimFunc method. If a cutoff value was set, then the OEFPDatabase. Get Scores method:
  - return scores that are equal to or larger than the specified cutoff value if the order is descending
  - return scores that are equal to or smaller than the specified cutoff value if the order is ascending

#### See also:

- OEFPDatabase. SetSimFunc method
- OEFPDatabase, SetCutoff method

#### **Examples:**

• Calculates the Tanimoto similarity on the first 100 entries of the database and returns scores that are equal to or larger than 0.1.

```
descending = Truefpdb.SetSimFunc(oegraphsim.OESimMeasure_Tanimoto, descending)
fpdb.SetCutoff(0.1)
for score in fpdb. GetScores (qfp, 0, 100):
   print ("%.3f" % score. GetScore ())
```

• Calculates the *Tversky* similarity (with  $\alpha = 0.9$  and  $\beta = 0.1$ ) on the entire database and returns all scores.

```
fpdb.SetSimFunc(oegraphsim.OETverskySim(0.9))
for score in fpdb. GetScores (qfp) :
    print ("%.3f" % score. GetScore())
```

• Calculates the  $\text{Dice}$  similarity beginning at the 100th entry of the database and returns scores that are equal to or smaller than 0.5.

```
descending = Truefpdb.SetSimFunc(oegraphsim.OESimMeasure_Dice, not descending)
fpdb.SetCutoff(0.5)
for score in fpdb. GetScores (qfp, 100):
    print ("%.3f" % score.GetScore())
```

#### Similarity calculation with an option class:

Performs similarity calculation between a given molecule or a fingerprint and the fingerprints stored in the OEFPDatabase object. It returns an iterator over the calculated similarity scores (OESimScore). Each OESimScore holds a similarity score and index of the corresponding fingerprint of the database.

- **mol** If the method is called with an OEMolBase object, then a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **fp** If the method is called with an OEFingerPrint object, then its type has to match with the type of the OEFPDatabase.
- opts The OEFPDatabaseOptions object controls all the parameters that determine the sorted search. For example, similarity measure, score cutoff, descending or ascending order etc.

#### See also:

• OEFPDatabaseOptions class

#### **Example:**

• Calculates the  $\cos$ ine similarity on the entire database and returns scores that are equal to or larger than  $0.3$ .

```
opts = oegraphsim. OEFPDatabaseOptions()
opts.SetCutoff(0.3)
opts.SetSimFunc(oegraphsim.OESimMeasure_Cosine)
for score in fpdb. GetScores (qfp, opts):
    print ("\S. 3f" \S score. Get Score ())
```

#### **GetSortedScores**

#### Table 2: The overloaded versions of the GetSortedScores method

| Link                                         | Description                                                       |
|----------------------------------------------|-------------------------------------------------------------------|
| <i>GetSortedScores(mol, limit, bgn, end)</i> | returns sorted similarities for a molecule                        |
| <i>GetSortedScores(fp, limit, bgn, end)</i>  | returns sorted similarities for a fingerprint                     |
| <i>GetSortedScores(mol, opts)</i>            | returns sorted similarities for a molecule with the given options |
| <i>GetSortedScores(fp, opts)</i>             | returns similarities for a fingerprint with the given options     |

#### **Similarity calculation:**

```
OESystem::OEIterBase<OEGraphSim::OESimScore> *
 GetSortedScores (const OEChem:: OEMolBase &mol, unsigned int limit=0,
                  unsigned int bgn=0, unsigned int end=0) const
```

```
OESystem:: OEIterBase<OEGraphSim:: OESimScore> *
 GetSortedScores (const OEGraphSim::OEFingerPrint &fp, unsigned int limit=0,
                  unsigned int bgn=0, unsigned int end=0) const
```

Performs similarity calculations between a molecule or a fingerprint and the fingerprints stored in the OEFPDatabase object. It returns an iterator over the calculated similarity scores (OESimScore) in sorted order. Each OESimScore holds a similarity score and index of the corresponding fingerprint of the database.

- mol If the method is called with an OEMolBase object, then a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **fp** If the method is called with an OEFingerPrint object, then its type has to match with the type of the OEFPDatabase.

- **bgn, end** The bgn and end arguments define the segment of the database on which the similarity calculation will take place. If both of these parameters are omitted (or set to zero), then the similarity calculation is performed on the entire fingerprint database.
- limit The value that defines the number of similarity scores returned by the OEFPDatabase. Get Sorted Scores method. If it is omitted (or set to zero) then all of the similarity scores are returned.

#### Note:

- · By default, the OEFPDatabase. GetSortedScores method calculates Tanimoto similarity scores and returns them in descending order.
- By using the OEFPDatabase. Set SimFunc method, similarity measures other than the default can be performed.
- The behavior of OEFPDatabase. GetSortedScores is also influenced by the cutoff value (OEFPDatabase, SetCutoff) of the database and the order of the scores specified by the OEFPDatabase. SetSimFunc method. If a cutoff value was set, then the OEFPDatabase. GetSortedScores method:
  - return scores that are equal to or larger than the specified cutoff value if the order is descending
  - return scores that are equal to or smaller than the specified cutoff value if the order is ascending

#### See also:

- OEFPDatabase. Set SimFunc method
- · OEFPDatabase. SetCutoff method

#### **Examples:**

• Calculates the  $Tanimoto$  similarity on the entire database and returns the 10 best scores in descending order.

```
for score in fpdb. GetSortedScores (qfp, 10):
    print ("\S. 3f" \S score. Get Score ())
```

• Calculates the  $D\acute{z}c$  similarity on the first 100 entries of the database and returns scores that are equal to or larger than 0.5 in descending order.

```
descending = Truefpdb.SetSimFunc(oegraphsim.OESimMeasure_Dice, descending)
fpdb.SetCutoff(0.5)
for score in fpdb. GetSortedScores (qfp, 0, 0, 100):
    print ("%.3f" % score. GetScore ())
```

• Calculates Manhattan similarity beginning at the 100th entry of the database and returns the "worst" 5 scores that are equal to or smaller than  $0.3$  in ascending order.

```
descending = Truefpdb.SetSimFunc(oegraphsim.OESimMeasure_Manhattan, not descending)
fpdb.SetCutoff(0.3)
for score in fpdb. GetSortedScores (qfp, 5, 100):
    print ("%. 3f" % score. GetScore())
```

Sorted similarity calculation with an option class:

```
OESystem::OEIterBase<OEGraphSim::OESimScore> *
  GetSortedScores (const OEChem:: OEMolBase & mol, const OEFPDatabaseOption &
\rightarrowopts) const
```

```
OESystem:: OEIterBase<OEGraphSim:: OESimScore> *
  GetSortedScores (const OEGraphSim:: OEFingerPrint &fp, const
→OEFPDatabaseOption &opts) const
```

Performs similarity calculations between a molecule or a fingerprint and the fingerprints stored in the OEFPDatabase object. It returns an iterator over the calculated similarity scores (OESimScore) in sorted order. Each OESimScore holds a similarity score and index of the corresponding fingerprint of the database.

- mol If the method is called with an OEMolBase object, then a fingerprint is generated from this molecule before looping over the fingerprints of the database and calculating similarities.
- **fp** If the method is called with an *OEFingerPrint* object, then its type has to match with the type of the OEFPDatabase.
- opts The OEFPDatabaseOptions object controls all the parameters that determine the sorted search. For example, similarity measure, score cutoff, descending or ascending order etc.

#### See also:

• OEFPDatabaseOptions class

#### **Example:**

• Calculates  $Tversky$  similarity on the entire database and returns the best 10 scores that are equal to or larger than 0.3 in descending order.

```
opts = oegraphsim.OEFPDatabaseOptions()
opts.SetDescendingOrder(True)
opts.SetCutoff(0.3)
opts.SetSimFunc(oegraphsim.OESimMeasure_Tversky)
opts.SetTverskyCoeffs(0.9, 0.1)
opts.SetLimit(10)
for score in fpdb. GetSortedScores (qfp, opts):
   print ("%.3f" % score. GetScore ())
```

#### **HasCutoff**

bool HasCutoff () const

Returns whether the cutoff value of the OEFPDatabase object has been set by the OEFPDatabase. Set Cutoff method.

- · OEFPDatabase. ClearCutoff
- · OEFPDatabase. GetCutoff
- · OEFPDatabase. SetCutoff

#### **NumFingerPrints**

```
unsigned int NumFingerPrints() const
```

Returns the number of OEFingerPrint objects stored in the database.

#### **SetCutoff**

void SetCutoff (float)

Sets the cutoff value of the OEFPDatabase object. The cutoff value influences the behavior of both the OEFPDatabase. GetScores and the OEFPDatabase. GetSortedScores methods.

#### See also:

- · OEFPDatabase. ClearCutoff
- · OEFPDatabase. HasCutoff
- · OEFPDatabase. SetCutoff

#### **SetDescendingOrder**

void SetDescendingOrder (bool descending)

Sets the order in which the calculated scores are returned by the OEFPDatabase. GetSortedScores method.

#### See also:

· OEFPDatabase. GetDescendingOrder

#### **SetSimFunc**

Sets the method used to evaluate fingerprint similarity when calling either the OEFPDatabase. GetScores or the OEFPDatabase. GetSortedScores methods.

void SetSimFunc (unsigned int simtype, bool descending=true)

Sets the similarity calculation by specifying a similarity method with a constant from the  $OESimMeasure$  namespace. The second argument defines the order in which the calculated scores are returned by the OEFPDatabase. GetSortedScores method.

**void** SetSimFunc (const OEGraphSim:: OESimFuncBase &, bool descending=true)

Creates a copy of the OESimFuncBase object and uses its OESimFuncBase. operator () method to evaluate similarity between two OEFingerPrint objects. The second argument defines the order in which the calculated scores are returned by the OEFPDatabase. GetSortedScores method.

Note: By default, both the OEFPDatabase. GetScores and the OEFPDatabase. GetSortedScores methods calculate Tanimoto similarity scores. While the OEFPDatabase. GetScores always returns these scores in the order in which the corresponding OEFingerPrint objects are added to the database, the latter method returns them in descending order, by default.

- Searching with User-defined Similarity Measures section
- User-defined Similarity Measures section
- · OESimMeasure namespace
- OETanimotoSim class
- OETverskySim class

## 5.1.6 OEFPDatabaseOptions

#### class OEFPDatabaseOptions

The OEFPDatabase Options class allows setting options on a per-search basis. This class is used to control the behavior of:

- the following methods of the OEFPDatabase class
  - OEFPDatabase. GetScores
  - OEFPDatabase. GetSortedScores
- the following methods of the OEFastFPDatabase class
  - OEFastFPDatabase.GetAllScores
  - OEFastFPDatabase.GetHistogram
  - OEFastFPDatabase.GetSortedScores
  - OEFastFPDatabase.GetRawScores
  - OEFastFPDatabase. SortedSearch

#### See also:

- Example code in Similarity calculation with an option class section
- Example code in Sorted similarity calculation with an option class section
- Example code in Searching fast fingerprint database section

The OEFPDatabaseOptions class stores the following properties:

| Property                                | Get method                       | Set method             | Corresponding<br>namespace /<br>type     |
|-----------------------------------------|----------------------------------|------------------------|------------------------------------------|
| cutoff value                            | GetCutoff                        | SetCutoff<br>HasCutoff | floating point number                    |
| order of sorting                        | GetDescendingOrder               | SetDescendingOrder     | boolean                                  |
| max number of scores                    | GetLimit                         | SetLimit               | integer 0 means no limit                 |
| similarity method                       | GetSimFunc                       | SetSimFunc             | OESimMeasure                             |
| $\alpha$ and $\beta$ for <i>Tversky</i> | GetTverskyAlpha / GetTverskyBeta | SetTverskyCoeffs       | floating point number                    |
| numper of processors                    | GetNumProcessors                 | SetNumProcessors       | integer<br>0 means<br>OEGetNumProcessors |

### **Constructors**

OEFPDatabaseOptions()

Default constructor.

#### Table 3: Default parameters of OEFPDatabaseOptions

| Property                       | Default value                 |
|--------------------------------|-------------------------------|
| cutoff value                   | no cutoff set                 |
| order of sorting               | true (means descending order) |
| max number of scores           | 0 (means no limit)            |
| similarity method              | OESimMeasure_Tanimoto         |
| $α$ and $β$ for <i>Tversky</i> | $α = 0.95, β = 0.05$          |
| number of processors           | 1                             |

```
OEFPDatabaseOptions (const unsigned limit,
                    const unsigned simfunc=OESimMeasure::Tanimoto)
```

Constructs an OEFPDatabaseOptions object with a limit on the number of similarity scores returned and a similarity method from the OESimMeasure namespace. The returned scores will be in descending order and applying no cutoff value.

OEFPDatabaseOptions (const OEFPDatabaseOptions & rhs)

Copy constructors.

#### operator=

OEFPDatabaseOptions & operator= (const OEFPDatabaseOptions & rhs)

Assignment operator.

### **ClearCutoff**

void ClearCutoff()

Removes the cutoff value previously set by the OEFPDatabaseOptions. SetCutoff method. After clearing the cutoff value, OEFPDatabaseOptions. HasCutoff method will return false.

- · OEFPDatabaseOptions. HasCutoff method
- · OEFPDatabaseOptions. GetCutoff method
- · OEFPDatabaseOptions. SetCutoff method

#### **GetCutoff**

|  | float GetCutoff() const |  |
|--|-------------------------|--|
|--|-------------------------|--|

Returns the cutoff value previously set by the OEFPDatabase. SetCutoff method.

#### See also:

- · OEFPDatabaseOptions. ClearCutoff method
- · OEFPDatabaseOptions. HasCutoff method
- · OEFPDatabaseOptions. SetCutoff method

#### **GetDescendingOrder**

bool GetDescendingOrder () const

Returns whether the similarity scores will be returned in descending or in ascending order.

#### See also:

· OEFPDatabaseOptions. SetDescendingOrder method

#### **GetLimit**

unsigned GetLimit() const

Returns the maximum number of similarity scores returned.

#### See also:

· OEFPDatabaseOptions. SetLimit method

#### **GetSimFunc**

unsigned GetSimFunc() const

Returns the similarity measure used to evaluate fingerprint similarities. The return value is taken from the OESimMeasure namespace.

#### See also:

• OEFPDatabaseOptions. SetSimFunc method

#### **GetNumProcessors**

unsigned GetNumProcessors()

Returns the number of threads that are used to search fingerprints when calling the OEFastFPDatabase. SortedSearch method.

#### See also:

· OEFPDatabaseOptions. SetNumProcessors method

#### **GetTverskyAlpha**

float GetTverskyAlpha() const

Returns the  $\alpha$  parameter of the *Tversky* similarity.

#### See also:

- · OEFPDatabaseOptions. SetTverskyCoeffs method
- OETverskySim class

#### **GetTverskyBeta**

float GetTverskyBeta() const

Returns the  $\beta$  parameter of the *Tversky* similarity.

#### See also:

- · OEFPDatabaseOptions. SetTverskyCoeffs method
- OETverskySim class

#### **HasCutoff**

bool HasCutoff() const

Returns whether the cutoff value of the OEFPDatabaseOptions object has been set by the OEFPDatabaseOptions. SetCutoff method.

#### See also:

- · OEFPDatabaseOptions. ClearCutoff method
- · OEFPDatabaseOptions. GetCutoff method
- · OEFPDatabaseOptions. SetCutoff method

#### **SetCutoff**

void SetCutoff (const float cutoff)

Sets the cutoff value of the OEFPDatabaseOptions object.

- · OEFPDatabaseOptions. ClearCutoff method
- · OEFPDatabaseOptions. GetCutoff method
- · OEFPDatabaseOptions. HasCutoff method

#### **SetDescendingOrder**

void SetDescendingOrder (const bool descending=true)

Sets whether the similarity scores will be returned in descending or in ascending order.

Note: This method has no effect on the OEFPDatabase. Get Scores method.

#### See also:

· OEFPDatabaseOptions. GetDescendingOrder method

#### **SetLimit**

void SetLimit (const unsigned limit)

Sets the maximum number of similarity scores returned.

limit If it is set to zero, then all similarity scores are returned.

**Note:** This method has no effect on the OEFPDatabase, Get Scores method.

#### See also:

· OEFPDatabaseOptions. GetLimit method

#### **SetSimFunc**

void SetSimFunc (const unsigned simtype)

Sets the similarity measure used to evaluate fingerprint similarities.

simitype This value has to be from the  $OESIMMeasure$  namespace.

#### See also:

· OEFPDatabaseOptions. GetSimFunc method

#### **SetNumProcessors**

void SetNumProcessors (const unsigned nrps)

Sets the number of threads that are used to search fingerprints when calling the OEFastFPDatabase. SortedSearch method. When set to 0, the number of processors used will be the number returned by the OEGetNumProcessors function.

Multi-threaded fingerprint search is currently only available in OEFastFPDatabaseMemoryType\_MemoryMapped and OEFastFPDatabaseMemoryType\_InMemory modes.

#### **SetTverskyCoeffs**

void SetTverskyCoeffs (const float alpha=0.95f, const float beta=0.05f)

Sets  $\alpha$  and  $\beta$  parameters for the *Tversky* similarity.

#### See also:

- · OEFPDatabaseOptions. GetTverskyAlphamethod
- · OEFPDatabaseOptions. GetTverskyBetamethod
- OETverskySim class

### 5.1.7 OEFPHistogram

class OEFPHistogram

The OEFPHistogram class is used to hold a histogram of similarity scores.

This class is an efficient way to obtain statistics on large databases which would be unfeasible to keep as full NxN similarity matrices.

#### The following classes derive from this class:

• OEFPVariogram

#### See also:

• OEFastFPDatabase. GetHistogram method

#### **Constructors**

OEFPHistogram (size\_t numBins=200, double min=0.0, double max=1.0)

Creates an OEFPHistogram object with given number of bins and range.

nrbins Number of bins in the histogram. (default=200)

**min** Minimum bound (inclusive) of the histogram range. (default  $= 0.0$ )

**max** Maximum bound (inclusive) of the histogram range. (default  $= 1.0$ )

Note: The default range of [0,1] covers all built-in similarity measures.

#### **AddSample**

```
size_t AddSample(const float sample)
size_t AddSample(const double sample)
```

Adds the sample into the histogram by incrementing the count in the relevant bin. Returns the bin index that the sample went into.

#### **GetBinBoundaries**

OESystem:: OEIterBase<double> \*GetBinBoundaries() const

Returns an iterator over the boundaries for each bin.

Note: The number of elements in this iterator is equal to OEFPHistogram. NumBins +1.

#### **GetBinCenters**

OESystem::OEIterBase<double> \*GetBinCenters() const

Returns an iterator over the center value for each bin.

**Note:** The number of elements in this iterator is equal to OEFPHistogram. NumBins.

**Hint:** It is generally reasonable to plot the results of OEFPHistogram. GetCounts or OEFPHistogram. Get Density against the bin centers returned by this method.

#### **GetBinldx**

```
size t GetBinIdx (const float sample) const
size_t GetBinIdx(const double sample) const
```

Returns the bin index that the sample would go into without actually adding the sample into the bin.

#### **GetBinWidth**

double GetBinWidth() const

Returns the width of bins in the histogram.

#### **GetCounts**

OESystem:: OEIterBase<unsigned int> \*GetCounts() const

Returns an iterator over the bin counts.

Note: Even though counts are returned as unsigned integers, they are internally kept as size\_t. If the counts are overflowing the unsigned int type of the system, it may be more appropriate to use the normalized OEFPHistogram. GetDensity instead.

#### **GetDensity**

OESystem::OEIterBase<double> \*GetDensity() const

Returns an iterator over the probability density for each bin.

Note: Result is equivalent to OEFPHistogram. GetCounts normalized by OEFPHistogram. NumSamples.

#### **GetMax**

double GetMax() const

Returns upper bound (inclusive) of the histogram range.

#### **GetMin**

double GetMin() const

Returns lower bound (inclusive) of the histogram range.

#### **Mean**

double Mean ()

Approximates and returns the sample mean over the histogram.

Note: This approximation is affected by number of bins in the histogram.

#### **NumBins**

size\_t NumBins() const

Returns the number of bins in the histogram.

#### **NumSamples**

size\_t NumSamples() const

Returns the total number of samples in the histogram.

#### **Std**

```
double Std()
```

Approximates and returns the sample standard deviation over the histogram.

Note: This approximation is affected by number of bins in the histogram.

## 5.1.8 OEFPPattern

```
class OEFPPattern : public OEChem: : OEAtomBondSet
```

A container that stores patterns that are enumerated when fingerprints such as OEFPType\_Path, OEFPType\_Circular and OEFPType\_Tree are generated.

#### See also:

- Fingerprint Patterns chapter
- · OEGetFPPatterns function

The following methods are publicly inherited from OEAtomBondSet:

| operator=          | ClearBonds | Remove      |
|--------------------|------------|-------------|
| Add                | CreateCopy | RemoveAtom  |
| AddAtom            | GetAtoms   | RemoveAtoms |
| AddAtoms           | GetBonds   | RemoveBond  |
| AddBond            | HasAtom    | RemoveBonds |
| AddBonds           | HasBond    | Sweep       |
| Clear              | IsEmpty    | Translate   |
| ClearAtoms         | NumAtoms   |             |
| ClearAtomsAndBonds | NumBonds   |             |

#### **Constructors**

```
OEFPPattern (OESystem:: OEIter<OEChem:: OEAtomBase> &atoms,
            OESystem::OEIter<OEChem::OEBondBase> &bonds,
            const std:: string & smarts, unsigned int unhashed,
            unsigned int setbit)
```

#### Constructor.

#### operator=

```
OEFPPattern & operator= (const OEFPPattern & rhs)
```

Assignment operator.

#### **GetBit**

unsigned int GetBit() const

Returns the bit that is set when the given pattern is hashed into fixed-length bitvector.

#### **GetSmarts**

std::string GetSmarts() const

Returns the smarts representation of the given pattern.

#### **GetUnhashed**

unsigned int GetUnhashed() const

Returns the unhashed unique integer representation of the given pattern.

## 5.1.9 OEFPTypeBase

class OEFPTypeBase

The OEFPTypeBase class is the abstract interface for representing OEFingerPrint types.

Note: When a OEFingerPrint object is initialized, its type is set to a type that is derived from this abstract base class.

#### **Constructors**

OEFPTypeBase()

Default constructor.

#### **GetFPType**

unsigned int GetFPType() const  $=0$ 

Returns the type of the OEFPTypeBase object from the OEFPType namespace.

#### **GetFPTypeString**

std::string GetFPTypeString() const =0

Returns a string representation of *OEFPTypeBase*. This string representation encodes information about the fingerprinting method and the parameters being used to generate the fingerprint.

Note: The string returned by the OEFPTypeBase. GetFPTypeString method does not include new line characters. The strings presented here were broken into separate lines only for better readability.

The string representation of the default  $OEFFType\_Circular$  fingerprint is the following:

```
Circular, ver=2.0.0, size=4096, radius=0-5,
→atype=AtmNum|Arom|Chiral|FCharge|HCount|EqHalo,
btype=Order
```

The string representation of the default  $^{OEFFType\_Lingo}$  fingerprint is the following:

Lingo,  $ver=2.0.0$ 

The string representation of the default  $OEFPType\_MACCS166$  fingerprint is the following:

MACCS166, ver=2.0.0

The string representation of the default OEFPType\_Path fingerprint is the following:

```
Path, ver=2.0.0, size=4096, bonds=0-5, atype=AtmNum|Arom|Chiral|FCharge|HvyDeg|Hyb|EqHalo,
btype=Order | Chiral
```

The string representation of the default OEFPType\_Tree fingerprint is the following:

```
Tree, ver=2.0.0, size=4096, bonds=0-4, atype=AtmNum|Arom|Chiral|FCharge|HyDeg|Hyb,
btype=Order
```

See also:

• OEFPTypeParams class

### **GetFPVersion**

unsigned short GetFPVersion() const

Returns the version number of the fingerprint.

#### **GetFPVersionString**

std::string GetFPVersionString() const

Returns the string format of the version of the fingerprint.

### 5.1.10 OEFPTypeParams

class OEFPTypeParams

This class represents OEFPTypeParams.

#### See also:

• Fingerprint parameters section

#### **Constructors**

OEFPTypeParams (const std:: string &typestr)

Constructor that parses the given string as a representation of a fingerprint and extracts the parameters that are used to generate the fingerprint.

See also:

• OEFPTypeBase. GetFPTypeString method

OEFPTypeParams (const OEFPTypeBase \*fptype)

Constructor that extracts the parameters that are used to generate the fingerprint type.

See also:

• OEFPTypeBase class

#### **GetAtomTypes**

unsigned int GetAtomTypes() const

**Returns** 

- the atom types extracted from the string for OEFPType\_Path, OEFPType\_Circular and OEFPType\_Tree fingerprint types
- zero for OEFPType\_Lingo and OEFPType\_MACCS166 fingerprint types

The return value is taken from the OEFPAt omType namespace.

• OEGetFPAtomType function

#### **GetBondTypes**

unsigned int GetBondTypes() const

Returns

- the bond types extracted from the string for OEFPType\_Path, OEFPType\_Circular and OEFPType\_Tree fingerprint types
- zero for OEFPType\_Lingo and OEFPType\_MACCS166 fingerprint types

The return value is taken from the OEFPBondType namespace.

#### See also:

• OEGetFPBondType function

#### **GetFPType**

unsigned int GetFPType () const

Returns the fingerprint type extracted from the string. The return value is taken from the  $OEFPType$  namespace.

#### **GetMaxDistance**

unsigned int GetMaxDistance() const

Returns:

- the size of the largest path fragments (in bonds), if the fingerprint type is  $OEFPType\_Path$
- the size of the largest circular fragments (in radius), if the fingerprint type is  $OEFPType\_Circular$
- the size of the largest tree fragments (in bonds), if the fingerprint type is  $OEFPType\_Tree$
- zero for OEFPType\_Lingo and OEFPType\_MACCS166 fingerprint types

#### **GetMinDistance**

unsigned int GetMinDistance() const

#### Returns:

- the size of the smallest path fragments (in bonds), if the fingerprint type is  $OEFPType\_Path$
- the size of the smallest circular fragments (in radius), if the fingerprint type is  $OEFPType\_Circular$
- the size of the smallest tree fragments (in bonds), if the fingerprint type is  $OEFFType\_Tree$
- zero for OEFPType\_Lingo and OEFPType\_MACCS166 fingerprint types

#### **GetNumBits**

unsigned int GetNumBits () const

Returns:

- the size of the fingerprint in bits for  $OEFPType\_Path$ ,  $OEFPType\_Circular$  and  $OEFPType\_Tree$  fingerprint types
- 166 for OEFPType\_MACCS166 fingerprint type
- zero for OEFPType\_Lingo fingerprint type

#### **GetVersion**

unsigned short GetVersion() const

Returns the version number.

#### See also:

· OEGetFingerPrintVersionString function

#### **IsValid**

```
bool IsValid() const
```

Returns whether the string was valid from which the OEFPTypeParams object was initialized.

## 5.1.11 OEFPVariogram

```
class OEFPVariogram : public OEFPHistogram
```

OEFPVariogram class is used to generate a variogram of similarity scores and related empirical measurements. An OEFPVariogram object is a OEFPHistogram with additional variogram data regarding user provided measurements.

The empirical variogram has the form :

$$
\hat{\gamma}(h) = \frac{1}{2|N(h)|} \sum_{(i,j) \in N(h)} |z_i - z_j|^2
$$

Where  $N(h)$  is the set of pairs that have a **distance** close to h and  $z_i$  is the measurement provided for the i th molecule.

For all of our built-in similarity measures, except for Tversky, distance is calculated a  $1-similarity$ . It is not possible to calculate an empirical variogram using Tversky similarity.

The **measurement** in the context of a variogram can be any user provided value per fingerprint e.g. bioassay data or calculated properties.

The following methods are publicly inherited from OEFPHistogram:

| AddSample        | GetCounts  | NumBins    |
|------------------|------------|------------|
| GetBinBoundaries | GetDensity | NumSamples |
| GetBinCenters    | GetMax     | Std        |
| GetBinIdx        | GetMin     |            |
| GetBinWidth      | Mean       |            |

#### See also:

• OEFastFPDatabase. GetVariogram method

#### **Constructors**

OEFPVariogram (size t numBins=200, double min=0, double max=1)

Constructors that need documenting.

#### **AddSample**

size\_t AddSample(const float sim, const float obs)

Adds a sample representing a pair of molecules into the variogram

sim Similarity between fingerprints i and j

obs Measured difference between the relevant fingerprints  $z_i - z_j$ 

**Note:** Since we are dealing with  $|z_i - z_j|^2$  this relationship is actually symmetrical.

### GetVariogram

OESystem:: OEIterBase<double> \*GetVariogram() const

Returns an iterator over the empirical variogram.

## 5.1.12 OESimFuncBase

#### class OESimFuncBase

OESimFuncBase is an abstract base class which defines the interface necessary to perform similarity calculations of OEFingerPrint objects.

#### See also:

• User-defined Similarity Measures section

The following classes derive from this class:

- $\bullet$  OETanimotoSim
- OETverskySim

### **Constructors**

OESimFuncBase()

Default constructor.

#### operator()

```
float operator () (const OEGraphSim:: OEFingerPrint &fpA,
                  const OEGraphSim:: OEFingerPrint & fpB) const =0
```

Virtual const operator that takes two OEFingerPrint objects and returns their evaluated similarity value.

#### **CreateCopy**

OESimFuncBase \*CreateCopy() const = 0

OESimFuncBase. CreateCopy is a virtual constructor which allows copying of concrete derived objects using a reference to this base class.

#### **GetSimTypeString**

std::string GetSimTypeString() const =0

Returns a string representation of the concrete derived class.

## 5.1.13 OESimScore

#### class OESimScore

This class represents OESimScore that holds a similarity value with an index that identifies the fingerprint in the OEFPDatabase object from which the score is calculated.

#### See also:

- · OEFPDatabase.GetScores
- · OEFPDatabase.GetSortedScores

#### **Constructors**

OESimScore(size\_t i, double s)

Initializes an *OESimScore* from an index i and a score s.

#### **GetIdx**

|--|--|

Returns the index of the fingerprint corresponding to the similarity score.

#### **GetScore**

double GetScore() const

Returns the similarity score of the fingerprint corresponding to the index.

## 5.1.14 OESimScorePair

class OESimScorePair

This class represents OESimScorePair that holds a similarity scores with an index  $\dot{i}$  and an index  $\dot{j}$  that identifies the fingerprints in the OEFastFPDatabase object from an  $NxN$  similarity calculation with OEFastFPDatabase. GetSparseMatrix.

#### See also:

· OEFastFPDatabase. GetSparseMatrix

#### **Constructors**

OESimScorePair(size\_t i, size\_t j, double s)

Initializes an *OESimScorePair* from an index  $\angle$ , an index  $\angle$  and a score s.

#### **GetIdxA**

size\_t GetIdxA() const

Returns the index i of the fingerprint corresponding to the similarity score.

#### **GetIdxB**

size\_t GetIdxB() const

Returns the index  $\frac{1}{3}$  of the fingerprint corresponding to the similarity score.

### **GetScore**

double GetScore() const

Returns the similarity score of the fingerprint corresponding to the index  $\pm$  and index  $\pm$  fingerprints.

### 5.1.15 OESimSearchResult

class OESimSearchResult

The OESimSearchResult class is used to store the results of a similarity search along with reporting the progress of the search and the histogram of the similarity scores.

#### See also:

· OEFastFPDatabase. SortedSearch method

#### **Constructor**

OESimSearchResult (const size\_t nrbins=50u, const double minv, const double maxv)

Constructor an empty result object with parameters for the score histogram.

nrbins Number of bins in the histogram (default = 50).

**miny** Minimum bound (inclusive) of the histogram range (default  $= 0.0$ ).

**maxy** Maximum bound (inclusive) of the histogram range (default  $= 1.0$ ).

OEFPHistogram GetHistogram () const

Returns an OEFPHistogram object that stores the histogram of similarity scores.

#### **GetSearchStatus**

unsigned GetSearchStatus() const

Returns the status of the similarity search defined in the OESimSearchStatus namespace.

#### **GetSortedScores**

OESystem:: OEIterBase<OESimScore> \*GetSortedScores()

Returns an iterator over the calculated similarity scores (OESimScore) in the sorted order. Each OESimScore holds a similarity score and index of the corresponding fingerprint of the database.

#### **IsValid**

|--|--|--|

Returns whether the OESimSearchResult object is valid.

#### **NumSearched**

size\_t NumSearched() const

Returns the number of fingerprints that have been already searched. This counter is continuously updated and provides the progress of the similarity search.

#### **NumTargets**

```
size_t NumTargets() const
```

Returns the number of targets (i.e. the number of fingerprints in the database).

## 5.1.16 OETanimotoSim

class OETanimotoSim : public OEGraphSim:: OESimFuncBase

This class represents  $OETanimotoSim$  that calculates the  $Tanimoto$  similarity score.

#### Formula:

 $Sim_{Tanimoto}(A, B) = \frac{bothAB}{|A|+|B|-bothAB} = \frac{bothAB}{onlyA+onlyB+bothAB}$ 

#### See also:

- Tanimoto section
- · OETanimoto function

The following methods are publicly inherited from OESimFuncBase:

operator() CreateCopy GetSimTypeString

#### **Constructors**

OETanimotoSim()

Default constructor.

operator()

```
float operator () (const OEGraphSim:: OEFingerPrint & fpA,
                  const OEGraphSim:: OEFingerPrint & fpB) const
```

Returns the Tanimoto similarity coefficient of the two given OEFingerPrint objects.

#### **CreateCopy**

OEGraphSim:: OESimFuncBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OETanimotoSim object is dynamically allocated and owned by the caller.

#### **GetSimTypeString**

std::string GetSimTypeString() const

Returns a string representation of the OETanimotoSim class.

### 5.1.17 OETverskySim

class OETverskySim : public OEGraphSim:: OESimFuncBase

This class represents OETverskySim that calculates the Tversky similarity score.

#### Formula:

 $Sim_{Tversky}(A, B) = \frac{both AB}{\alpha * only A + \beta * only B + both AB}$ 

See also:

- Tversky section
- · OETversky function

The following methods are publicly inherited from OESimFuncBase:

operator() CreateCopy GetSimTypeString

#### **Constructors**

OETverskySim(float a=0.95f)

Default constructor ( $\alpha = 0.95$ ,  $\beta = 1.0 - \alpha = 0.05$ )

OETverskySim(float a, float b)

Constructor with arbitrary  $\alpha$  and  $\beta$  parameters.

operator()

```
float operator () (const OEGraphSim:: OEFingerPrint & fpA,
                  const OEGraphSim:: OEFingerPrint & fpB) const
```

Returns the Tversky similarity coefficient of the two given OEFingerPrint objects.

#### **CreateCopy**

OEGraphSim:: OESimFuncBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OETverskySim object is dynamically allocated and owned by the caller.

#### **GetAlpha**

float GetAlpha () const

Returns the  $\alpha$  parameter of the *Tversky* similarity calculation.

#### **GetBeta**

float GetBeta() const

Returns the  $\beta$  parameter of the *Tversky* similarity calculation.

#### **GetSimTypeString**

std::string GetSimTypeString() const

Returns a string representation of the OETverskySim class.

## **5.2 OEGraphSim Constants**

### 5.2.1 OEFastFPDatabaseMemoryType

This namespace contains memory type constants representing how fingerprints are stored and searched for in an OEFastFPDatabase object.

See also:

• OEFastFPDatabase class

#### **Default**

The default memory type is OEFastFPDatabaseMemoryType\_MemoryMapped.

### **CUDA**

If a CUDA-enabled GPU is available, OEFastFPDatabase can take advantage of the device for similarity calculations. When an OEFastFPDatabase is initialized with the OEFastFPDatabaseMemoryType\_CUDA type, similarity calculations are performed on the device. Initialization incurs a one-time load penalty, similar to OEFastFPDatabaseMemoryType\_InMemory.

#### **Requirements:**

- Prerequisites for OpenEye's GPU-accelerated software
- Fingerprint sizes of multiples of 1024 bits.

Note: At present, multi-GPU support is not available. If there are multiple CUDA devices on the system, the first compatible device detected will be used. To enforce the use of a particular device, set the environment variable CUDA VISIBLE DEVICES.

Note: If device memory limits are exceeded or a CUDA-enabled device is not detected this implementation falls back to OEFastFPDatabaseMemoryType\_MemoryMapped

#### **InMemory**

When an OEFastFPDatabase is initialized with OEFastFPDatabaseMemoryType\_InMemory type the fingerprints are pre-loaded into memory and the similarity search performed in-memory when calling the OEFastFPDatabase.GetSortedScores method.

**Hint:** OEFastFPDatabaseMemoryType\_InMemory presents the fastest search at the expense of load time and the search is limited by the size of the memory.

#### **MemoryMapped**

When an OEFastFPDatabase is initialized with OEFastFPDatabaseMemoryType MemoryMapped type there is no load time penalty or memory limitation but the search itself is slower.

#### See also:

• Example code in Searching fast fingerprint database section

## 5.2.2 OEFPAtomType

This namespace contains atom typing options that can be used when generating Circular, Path of Tree fingerprints. Atom type options control how the atoms of the enumerated circular, path or tree fragments are encoded during the fingerprint generation.

The OEFPAt omType namespace contains the following constants:

| Constant name                      | Combination of                                                                             |
|------------------------------------|--------------------------------------------------------------------------------------------|
| OEFPAtomType_Aromaticity           |                                                                                            |
| OEFPAtomType_AtomicNumber          |                                                                                            |
| OEFPAtomType_Chiral                |                                                                                            |
| OEFPAtomType_DefaultAtom           | DefaultPathAtom                                                                            |
| <i>DefaultCircularAtom</i>         | AtomicNumber   Aromaticity   Chiral   FormalCharge   HCount   EqHalogen                    |
| OEFPAtomType_DefaultCircularVSAtom | AtomicNumber   Aromaticity   Chiral   HCount   EqHalogen                                   |
| <i>DefaultPathAtom</i>             | AtomicNumber   Aromaticity   Chiral   FormalCharge   HvyDegree   Hybridization   EqHalogen |
| OEFPAtomType_DefaultPathVSAtom     | AtomicNumber   Aromaticity   Chiral   HvyDegree   EqHalogen                                |
| <i>DefaultTreeAtom</i>             | AtomicNumber   Aromaticity   Chiral   FormalCharge   HvyDegree   Hybridization             |
| OEFPAtomType_DefaultTreeVSAtom     | AtomicNumber   Aromaticity   Chiral   HvyDegree                                            |
| OEFPAtomType_EqAromatic            |                                                                                            |
| OEFPAtomType_EqHalogen             |                                                                                            |
| OEFPAtomType_EqHBondAcceptor       |                                                                                            |
| OEFPAtomType_EqHBondDonor          |                                                                                            |
| OEFPAtomType_FormalCharge          |                                                                                            |
| OEFPAtomType_HCount                |                                                                                            |
| OEFPAtomType_HvyDegree             |                                                                                            |
| OEFPAtomType_Hybridization         |                                                                                            |
| OEFPAtomType_InRing                |                                                                                            |
| OEFPAtomType_None                  |                                                                                            |

**Note:** The constants of the *OEFPAt omType* namespace can be **combined** using the bitwise OR operation.

Note: The images in this sections visualize the effect of the various atom typing options.

See also:

• Visualizing Molecule Similarity section

- OEFPBondType namespace
- OEMakeCircularFP function
- · OEMakePathFP function
- · OEMakeTreeFP function

• Atom and Bond Typing section

Note: All explicit hydrogens are suppressed of the molecule before generating any fingerprints. (See example in Example of molecules that are considered to be equivalent due to suppressing their explicit hydrogens).

![](_page_100_Figure_3.jpeg)

![](_page_100_Figure_4.jpeg)

#### **AtomicNumber**

This flag indicates that atomic number (the value returned by the OEAtomBase. GetAtomicNum method) is encoded into the generated fingerprint, *i.e.*, if two fragments (either circular, paths or tree) are composed of atoms with different atomic numbers, then the two fragments will be mapped to different bits of the fingerprint. Table: Example of using the AtomicNumber option demonstrates the effect of using the OEFPAtomType\_AtomicNumber flag.

![](_page_100_Figure_7.jpeg)

Table 4: Example of using the OEFPAtomType\_AtomicNumber option (Path, numbits=4096, bonds=0-5, bond typing = BondOrder).

### **Aromaticity**

This flag indicates that aromaticity (the value returned by the OEAtomBase. IsAromatic method) is encoded into the generated fingerprint, *i.e.*, an aromatic and an aliphatic fragment will be mapped to different bits of the fingerprint. Table: Example of using the Aromatic option demonstrates the effect of using the  $OEFPAtomType\_Aromaticity$ flag.

![](_page_101_Figure_3.jpeg)

![](_page_101_Figure_4.jpeg)

Note: Prior to generating a fingerprint, the aromaticity of the molecule is re-perceived using the OEAroModel\_OpenEye aromaticity model.

### **Chiral**

This flag indicates that chiral and non-chiral atoms (the value returned by the OEAtomBase. IsChiral method) are distinguished during the fingerprint generation. Table: Example of using the Chiral option demonstrates the effect of using the OEFPAtomType\_Chiral flag.

![](_page_101_Figure_8.jpeg)

Table 6: Example of using the OEFPAtomType\_Chiral option  $(Path, numbits=4096, bonds=0-5, bond typing = BondOrder).$ 

**Note:** Different stereoisomers of molecules can not be distinguished when the OEFPAtomType\_Chiral flag is set. (See example in Figure: Example of molecule similarity of stereoisomers).

![](_page_102_Figure_1.jpeg)

Fig. 3: Example of molecule similarity of stereoisomers

### **FormalCharge**

This flag indicates that formal charge (the value returned by the OEAtomBase.GetFormalCharge method) is encoded into the generated fingerprint. Table: Example of using the FormalCharge option demonstrates the effect of using the OEFPAtomType\_FormalCharge flag.

![](_page_102_Figure_5.jpeg)

Table 7: Example of using the OEFPAtomType\_FormalCharge option (Path, numbits=4096, bonds=0-5, bond typing = BondOrder).

### **HvyDegree**

This flag indicates that heavy degree information (the value returned by the OEAt omBase. Get HvyDegree method) is encoded into the generated fingerprint. Table: Example of using the HvyDegree option demonstrates the effect of using the OEFPAtomType\_HvyDegree flag.

![](_page_103_Figure_3.jpeg)

![](_page_103_Figure_4.jpeg)

### **HCount**

This flag indicates that number of hydrogens (the value returned by the OEAt omBase. GetTotalHCount method) is encoded into the generated fingerprint. Table: Example of using the HCount option demonstrates the effect of using the OEFPAtomType\_HCount flag.

![](_page_103_Figure_7.jpeg)

Table 9: Example of using the OEFPAtomType\_HCount option  $(Path, numbits=4096, bonds=0-5, bond typing = InRing).$ 

### **Hybridization**

This flag indicates that hybridization (the value returned by the OEAt omBase. GetHyb method) is encoded into the generated fingerprint. Table: Example of using the Hybridization option demonstrates the effect of using the OEFPAtomType\_Hybridization flag.

![](_page_104_Figure_3.jpeg)

### **InRing**

This flag indicates that atom topology (the value returned by the OEAtomBase. Is InRing method) is encoded into the generated fingerprint, i.e., if two fragments (either circular, path or tree) are composed of atoms with different atom topology, then the two fragments will be mapped to different bits of the fingerprint. Table: Example of using the InRing option demonstrates the effect of using the OEFPAt omType\_InRing flag.

![](_page_104_Figure_6.jpeg)

![](_page_104_Figure_7.jpeg)

### **EgAromatic**

This flag modifies the meaning of the OEFPAtomType\_AtomicNumber flag.  $If$ the OEFPAtomType\_EqAromatic flag is set then aromatic atoms are considered equivalent during the fingerprint generation. Table: Example of using the EqAromatic option demonstrates the effect of using the OEFPAtomType\_EqAromatic flag.

![](_page_105_Figure_3.jpeg)

![](_page_105_Figure_4.jpeg)

### **EqHalogen**

This flag modifies the meaning of OEFPAt omType\_AtomicNumber flag. If the OEFPAt omType\_EqHalogen flag is set then halide atoms (OEE1emNo\_F, OEE1emNo\_C1, OEE1emNo\_Br, and OEE1emNo\_I) are considered equivalent during the fingerprint generation. Table: Example of using the EqHalogen option demonstrates the effect of using the OEFPAtomType\_EqHalogen flag.

![](_page_105_Figure_7.jpeg)

![](_page_105_Figure_8.jpeg)

### **EgHBondAcceptor**

This flag modifies the meaning of the OEFPAtomType\_AtomicNumber  $If$ the flag. OEFPAtomType\_EqHBondAcceptor flag is set then atoms that are perceived as hydrogen bonding acceptors are considered equivalent during the fingerprint generation. The GraphSim TK uses the same definition as the MolProp TK to identify hydrogen bond acceptors. See examples in Figure: Molecules with hydrogen bond acceptor annotation. Table: Example of using the EqHBondAcceptor option demonstrates the effect of using the OEFPAtomType\_EqHBondAcceptor flag.

![](_page_106_Figure_3.jpeg)

**Generated by Grapheme TK** 

#### Fig. 4: Example of molecules with hydrogen bond acceptor annotation

![](_page_106_Figure_6.jpeg)

![](_page_106_Figure_7.jpeg)

#### **EqHBondDonor**

**This** flag modifies the meaning of the OEFPAtomType AtomicNumber flag.  $If$ the OEFPAtomType\_EqHBondDonor flag is set then atoms that are perceived as hydrogen bonding donors are considered equivalent during the fingerprint generation. The GraphSim TK uses the same definition as the MolProp TK to identify hydrogen bond donors. See examples in Figure: Molecules with hydrogen bond donor annotation. Table: Example of using the EqHBondDonor option demonstrates the effect of using the OEFPAtomType\_EqHBondDonor flag.

![](_page_107_Figure_1.jpeg)

**Generated by Grapheme TK** 

#### Fig. 5: Molecules with hydrogen bond donor annotation

Table 15: Example of using the OEFPAtomType\_EqHBondDonor option (Path, numbits=4096, bonds=0-5, bond typing = BondOrder).

![](_page_107_Figure_5.jpeg)

#### **DefaultAtom**

Same as DefaultPathAtom constant.

#### **DefaultCircularAtom**

The bitwise OR'd value of the following atom typing options:

- · OEFPAtomType\_AtomicNumber
- OEFPAtomType\_Aromaticity
- · OEFPAtomType\_Chiral
- OEFPAtomType\_FormalCharge
- · OEFPAtomType\_HCount
- OEFPAtomType\_EqHalogen

See example in Figure: Circular fingerprint similarity with default circular atom and bond typing. This constant is used as atom typing parameter when a default  $Circular$  fingerprint is generated by the following functions:

- OEMakeFP (OEFingerPrint &, const OEMolBase &, OEFPType\_Circular)
- OEMakeCircularFP (OEFingerPrint &, const OEMolBase &)

#### See also:

· OEFPBondType\_DefaultCircularBond constant

![](_page_108_Figure_6.jpeg)

Fig. 6: Circular fingerprint similarity with default circular atom and bond typing

#### **DefaultCircularVSAtom**

The default atom typing for the circular fingerprint that is designed for virtual screening. It is the same as *DefaultCir*cularAtom without OEFPAtomType\_FormalCharge.

### **DefaultPathAtom**

The bitwise OR'd value of the following atom typing options:

- · OEFPAtomType\_AtomicNumber
- OEFPAtomType\_Aromaticity
- · OEFPAtomType\_Chiral
- · OEFPAtomType\_FormalCharge
- · OEFPAtomType HvyDegree
- · OEFPAtomType\_Hybridization

• OEFPAtomType EgHalogen

See example in Figure: Path fingerprint similarity with default path atom and bond typing. This constant is used as atom typing parameter when a default  $Path$  fingerprint is generated by the following functions:

- OEMakeFP (OEFingerPrint &, const OEMolBase &, OEFPType\_Path)
- OEMakePathFP (OEFingerPrint &, const OEMolBase &)

#### See also:

· OEFPBondType\_DefaultPathBond constant

## DefaultPathAtom & DefaultPathBond

![](_page_109_Figure_8.jpeg)

#### Fig. 7: Path fingerprint similarity with default path atom and bond typing

#### **DefaultPathVSAtom**

The default atom typing for the path fingerprint that is designed for virtual screening. It is the same as DefaultPathAtom without OEFPAtomType\_FormalCharge and OEFPAtomType\_Hybridization.

#### **DefaultTreeAtom**

The bitwise OR'd value of the following atom typing options:

- · OEFPAtomType\_AtomicNumber
- OEFPAtomType\_Aromaticity
- · OEFPAtomType\_Chiral
- OEFPAtomType FormalCharge
- · OEFPAtomType\_HvyDegree

• OEFPAtomType Hybridization

See example in Figure: Tree fingerprint similarity with default tree atom and bond typing. This constant is used as atom typing parameter when a default  $Tree$  fingerprint is generated by the following functions:

- OEMakeFP (OEFingerPrint &, const OEMolBase &, OEFPType\_Tree)
- OEMakeTreeFP (OEFingerPrint &, const OEMolBase &)

#### See also:

· OEFPBondType\_DefaultTreeBond constant

## DefaultTreeAtom & DefaultTreeBond

![](_page_110_Figure_8.jpeg)

#### Fig. 8: Tree fingerprint similarity with default tree atom and bond typing

#### **DefaultTreeVSAtom**

The default atom typing for the tree fingerprint that is designed for virtual screening. It is the same as DefaultTreeAtom without OEFPAtomType\_FormalCharge and OEFPAtomType\_Hybridization.

#### **None**

No atom properties are encoded when generating a fingerprint.

## 5.2.3 OEFPBondType

This namespace contains bond typing options that can be used when generating Circular, Path of Tree fingerprints. Bond type options control how the bonds of the enumerated circular, path or tree fragments are encoded during the fingerprint generation.

The OEFPBondType namespace contains the following constants:

| Constant name                      | Combination of   |
|------------------------------------|------------------|
| OEFPBondType_BondOrder             |                  |
| OEFPBondType_Chiral                |                  |
| OEFPBondType_DefaultBond           | DefaultPathBond  |
| OEFPBondType_DefaultCircularBond   | BondOrder        |
| OEFPBondType_DefaultCircularVSBond | BondOrder        |
| OEFPBondType_DefaultPathBond       | BondOrder Chiral |
| OEFPBondType_DefaultPathVSBond     | BondOrder Chiral |
| OEFPBondType_DefaultTreeBond       | BondOrder        |
| OEFPBondType_DefaultTreeVSBond     | BondOrder        |
| OEFPBondType_InRing                |                  |
| OEFPBondType_None                  |                  |

Note: The images in this sections visualize the effect of the various bond typing options.

#### See also:

• Visualizing Molecule Similarity section

#### See also:

- OEFPAtomType namespace
- · OEMakeCircularFP function
- · OEMakePathFP function
- · OEMakeTreeFP function
- Atom and Bond Typing section

### **BondOrder**

This flag indicates that bond order information is encoded into the generated fingerprint, i.e., if two fragments (either circular, path or tree) are composed of bonds with different bond orders (the value returned by the GetOrder method) then the two fragments will be mapped to different bits of the fingerprint. Table: Example of using the BondOrder option demonstrates the effect of using the OEFPBondType\_BondOrder flag.

![](_page_112_Figure_1.jpeg)

#### **Chiral**

This flag indicates that chiral and non-chiral bonds (the value returned by the OEBondBase. IsChiral method) are distinguished during the circular, path, the tree fingerprint generation. Table: Example of using the Chiral option demonstrates the effect of using the OEFPBondType\_Chiral flag.

![](_page_112_Figure_4.jpeg)

![](_page_112_Figure_5.jpeg)

Note: Cis and trans chiral bonds can not be distinguished when the OEFPBondType\_Chiral flag is set. Fingerprints generated for molecules  $C \subset C/C$  and  $C/C=C/C$  will always be identical. (See example in *Figure: Example* of molecule similarity of stereoisomers).

![](_page_113_Figure_1.jpeg)

Fig. 9: Example of molecule similarity of cis-trans stereoisomers

#### **InRing**

This flag indicates that bond topology information is encoded into the generated fingerprint, *i.e.*, if two fragments (either circular, path or tree) are composed of bonds with different bond topology (the value returned by the OEBondBase. IsInRing method) then the two fragments will be mapped to different bits of the fingerprint.

Table: Example of using the InRing option demonstrates the effect of using the OEFPBondType\_InRing flag.

![](_page_113_Figure_6.jpeg)

Table 18: Example of using the OEFPBondType\_InRing option (Path, numbits=4096, bonds=0-5, atom typing = AtomicNumber).

### **DefaultBond**

Same as OEFPBondType\_DefaultPathBond constant.

### **DefaultCircularBond**

Same as the OEFPBondType\_BondOrder constant.

See example in Figure: Circular fingerprint similarity with default circular atom and bond typing. This constant is used as bond typing parameter when a default  $Circular$  fingerprint is generated by the following functions:

- · OEMakeFP (OEFingerPrint &, const OEMolBase &, OEFPType\_Circular)
- · OEMakeCircularFP

#### See also:

• OEFPAtomType\_DefaultCircularAtom constant

### **DefaultCircularAtom & DefaultCircularBond**

![](_page_114_Figure_9.jpeg)

## Tanimoto score = $0.313$

**Generated by Grapheme TK** 

#### **DefaultCircularVSBond**

The default bond typing for the circular fingerprint that is designed for virtual screening. Currently it's the same as OEFPBondType\_DefaultCircularBond.

#### **DefaultPathBond**

The bitwise OR'd value of the following bond typing options:

- · OEFPBondType\_BondOrder
- · OEFPBondType\_Chiral

See example in Figure: Path fingerprint similarity with default path atom and bond typing. This constant is used as bond typing parameter when a default  $Path$  fingerprint is generated by the following functions:

• OEMakeFP (OEFingerPrint &, const OEMolBase &, OEFPType\_Path)

· OEMakePathFP

#### See also:

· OEFPAtomType\_DefaultPathAtom constant

![](_page_115_Figure_4.jpeg)

Fig. 10: Path fingerprint similarity with default tree atom and bond typing

#### **DefaultPathVSBond**

The default bond typing for the tree fingerprint that is designed for virtual screening. Currently it's the same as OEFPBondType\_DefaultPathBond.

#### **DefaultTreeBond**

Same as the OEFPBondType\_BondOrder constant.

See example in Figure: Tree fingerprint similarity with default tree atom and bond typing. This constant is used as bond typing parameter when a default  $Tree \in$  fingerprint is generated by the following functions:

- · OEMakeFP (OEFingerPrint &, const OEMolBase &, OEFPType\_Tree)
- OEMakeTreeFP

#### See also:

· OEFPAtomType\_DefaultTreeAtom constant

![](_page_116_Figure_1.jpeg)

## DefaultTreeAtom & DefaultTreeBond

Fig. 11: Tree fingerprint similarity with default tree atom and bond typing

#### **DefaultTreeVSBond**

The default bond typing for the tree fingerprint that is designed for virtual screening. Currently it's the same as OEFPBondType\_DefaultTreeBond.

#### **None**

No bond properties are encoded when generating a fingerprint.

## 5.2.4 OEFPDatabaseOptionsSetup

This namespace encodes symbolic constants used as bit-masks to indicate which highlighting interface parameters are being created when invoking the OEConfigureFPDatabaseOptions function.

The OEFPDatabaseOptionsSetup namespace contains the following constants:

#### All

#### The combination of following constants:

- · OEFPDatabaseOptionsSetup\_Cutoff
- · OEFPDatabaseOptionsSetup\_DescendingOrder
- · OEFPDatabaseOptionsSetup\_Limit
- · OEFPDatabaseOptionsSetup\_SimFunc

#### **Cutoff**

Passing this constant to the OEConfigureFPDatabaseOptions function result in generating the following default interface.

```
Contents of parameter -cutoff
  Aliases : -c
  Type : float
  Allow list : false
  Default : (parameter does not have a default)
  Simple : true
  Required : false
  Brief : Similarity cutoff value
  Detail
     API : OEFPDatabaseOptions::SetCutoff method
     By default there is no similarity cutoff
```

#### See also:

· OEFPDatabaseOptions. SetCutoff method

#### **DescendingOrder**

Passing this constant to the OEConfigureFPDatabaseOptions function result in generating the following default interface.

```
Contents of parameter -descending
  Aliases : - d
  Type : bool
  Allow list : false
  Default : true
  Simple : true
  Required : false
  Brief : Order of similarity scores
  Detail
     API : OEFPDatabaseOptions::SetDescendingOrder method
      If true scores are returned in descending order otherwise in ascending order
```

#### See also:

· OEFPDatabaseOptions. SetDescendingOrder method

#### Limit

Passing this constant to the OEConfigureFPDatabaseOptions function result in generating the following default interface.

```
Contents of parameter -limit
  Aliases : -1
  Type : int
  Allow list : false
  Default : 10
  Simple : true
  Required : false
  Legal ranges :
     100000 to 0
  Brief : Maximum number of similarity scores
  Detail
     API : OEFPDatabaseOptions::SetLimit method
      If set to zero, then all of the similarity scores are returned
```

#### See also:

· OEFPDatabaseOptions. SetLimit method

#### **SimFunc**

Passing this constant to the OEConfigureFPDatabaseOptions function result in generating the following default interface.

```
Contents of parameter -simfunc
  Aliases : -s
  Type : string
  Allow list : false
  Default : Tanimoto
  Simple : true
  Required : false
  Legal values : Tanimoto Cosine Dice Euclid Tversky Manhattan
  Brief : Similarity measure
  Detail
     API : OEFPDatabaseOptions::SetSimFunc method and OESimMeasure namespace
```

See also:

· OEFPDatabaseOptions. SetSimFunc method

## 5.2.5 OEFPType

This namespace contains constants representing various OEFingerPrint types available in the GraphSim TK.

#### See also:

• OEMakeFP

#### **Circular**

This constant represents the circular fingerprint type.

Circular fingerprints are generated by exhaustively enumerating all circular fragments grown radially from each heavy atom of the molecule up to the given radius and then hashing these fragments into a fixed-length bitvector.

#### See also:

• Circular section

#### Lingo

This constant represents the LINGO fingerprint type.

#### See also:

- LINGO section
- $\bullet$  LINGO

### MACCS166

This constant represents the MACCS key fingerprint type.

#### See also:

• MACCS section

### **Path**

This constant represents the path fingerprint type.

Path fingerprints are generated by exhaustively enumerating all linear paths of a molecular graph up to a given size and then hashing these fragments into a fixed-length bitvector.

#### See also:

• Path section

#### **Tree**

This constant represents the tree fingerprint type.

A tree fingerprint is generated by exhaustively enumerating all trees of a molecular graph up to a given size and then hashing these fragments into a fixed-length bitvector.

#### See also:

• Tree section

## 5.2.6 OEPopCountMethod

This namespace contains constants representing possible popcount methods available in GraphSim TK.

See also:

- · OEGetPopCountMethod function
- · OEIsFastFPDatabaseReady function

#### **BitCount**

The hardware does not support the popcount method but only a slower bitcount method.

#### **NoSupport**

No support available.

### **PopCount**

The fast popcount method is available.

### 5.2.7 OESimMeasure

This namespace contains constants representing the built-in similarity indices of the GraphSim TK.

- · OEFPDatabase. SetSimFunc method
- Searching with User-defined Similarity Measures section

### **Cosine**

This constant represents Cosine similarity index.

#### See also:

- Cosine section
- · OECosine function

### **Dice**

This constant represents Dice similarity index.

#### See also:

- Dice section
- OEDice function

### **Euclid**

This constant represents the Euclidean similarity index.

#### See also:

- Euclidean section
- · OEEuclid function

### **Manhattan**

This constant represents the Manhattan similarity index.

#### See also:

- Manhattan section
- OEManhattan function

### **Tanimoto**

This constant represents the Tanimoto similarity index.

- Tanimoto section
- OETanimoto function
- OETanimotoSim class

### **Tversky**

This constant represents the Tversky similarity index.

#### See also:

- Tversky section
- OETversky function
- OETverskySim class

## 5.2.8 OESimSearchStatus

This namespace contains constants representing the various status of the similarity search (OESubSearchResult. GetSearchStatus).

#### **Finished**

This constant indicates that the similarity search finished successfully.

#### **InProgress**

This constant indicates that the similarity search is in progress.

#### **Uninitialized**

This constant indicates that the similarity search can not be initialized (for example, attempting a search on an invalid OEFastFPDatabase object).

#### See also:

- · OEFastFPDatabase. SortedSearch method
- OESimSearchStatusToNamefunction

## **5.3 OEGraphSim Functions**

## 5.3.1 OEAreCompatibleDatabases

```
bool OEAreCompatibleDatabases (const OEChem:: OEMolDatabase &moldb,
                               const OEFastFPDatabase & fpdb)
```

Returns whether a molecule database and a fingerprint database are constructed from the same molecule file.

moldb The OEMolDatabase object.

fpdb The OEFastFPDatabase object.

- · OECreateFastFPDatabaseFile function
- OEFastFPDatabaseParams class
- Example code in Searching fast fingerprint database section

## 5.3.2 OEConfigureFingerPrint

```
bool OEConfigureFingerPrint (OESystem:: OEInterface &itf,
                             const OEFPTypeBase *deffptype)
```

Configures the given interface to add the following parameters for user-defined fingerprint type:

```
fingerprint options
-atomtype : Fingerprint atom type
-bondtype : Fingerprint bond type
-fptype : Fingerprint type
-maxdistance : Maximum number of bonds/radius in path/circular/tree
               fingerprint
-mindistance : Minimum number of bonds/radius in path/circular/tree
               fingerprint
-numbits : Size of bitvector
```

*itf* The interface being configured.

*deffptype* The default fingerprint type.

#### See also:

- OEInterface class in the **OEChem TK** manual
- OEFPTypeBase class
- · OESetupFingerPrint function
- Example code in Generating fingerprint file for fast fingerprint search section
- Example code in Building and searching fingerprint database section

## 5.3.3 OEConfigureFPDatabaseMemoryType

```
bool OEConfigureFPDatabaseMemoryType(OESystem::OEInterface &itf,
                                       unsigned int
\rightarrowdefvalue=OEFastFPDatabaseMemoryType::Default,
                                       std::string name="-memorytype",
                                       std::string alias="-m")
```

Adds a fingerprint database memory type parameter to the given interface.

itf The interface being configured.

defvalue Default parameter value.

name The name of the parameter.

alias The alternative *i.e.* alias name of the parameter.

#### See also:

• OEInterface class in the OEChem TK manual

- OEFastFPDatabaseMemoryType namespace
- OEGetFPDatabaseMemoryType function
- Example code in Searching fast fingerprint database section

## 5.3.4 OEConfigureFPDatabaseOptions

```
bool OEConfigureFPDatabaseOptions (OESystem:: OEInterface &itf,
                                   const OEFPDatabaseOptions &defopts)
```

Configures the given interface to add parameters for fingerprint database search options.

*itf* The interface being configured.

defopts The default fingerprint database search options.

```
bool OEConfigureFPDatabaseOptions (OESystem:: OEInterface &itf,
                                   unsigned int config=OEFPDatabaseOptionsSetup:: All)
```

Configures the given interface to add parameters for default fingerprint database search options.

*itf* The interface being configured.

config The option that specifies which parameters will be added to the interface. This value has to be from the OEFPDatabaseOptionsSetup namespace.

#### See also:

- OEInterface class in the OEChem TK manual
- OEFPDatabaseOptions class
- · OESetupFPDatabaseOptions function
- Example code in Building and searching fingerprint database section
- Example code in Searching fast fingerprint database section

## 5.3.5 OECosine

float OECosine (const OEFingerPrint & fpA, const OEFingerPrint & fpB)

Calculates the Cosine similarity value of two OEFingerPrint objects.

**Formula:**  $Sim_{Cosine}(A, B) = \frac{bothAB}{\sqrt{(onlyA + bothAB)*(onlyB + bothAB)}}$ 

See also:

• Cosine section

## 5.3.6 OECreateFastFPDatabaseFile

```
bool OECreateFastFPDatabaseFile(const std::string &fpdbfname,
                                const std:: string & molfname,
                                 const OEFPTypeBase *fptype)
bool OECreateFastFPDatabaseFile(const std::string &fpdbfname,
                                 const std:: string & molfname,
                                 const OECreateFastFPDatabaseOptions &opts)
```

Generates a binary fingerprint file for the given molecule file.

fpdbfname The name of the fingerprint file. The file name has to have a . fpbin extension.

molfname The name of the molecule file.

fptype The type of the fingerprint that will be generated to each molecule.

opts The OECreateFastFPDatabaseOptions object that encapsulates properties that determine how fingerprints are generated.

**Note:** GraphSim TK currently only supports the popcount search method for fingerprints with the size of multiple of 256. This means that the OEFPType\_MACCS166 fingerprint type is currently not supported. When using other custom fingerprint types (see *User-defined Fingerprint* section) the size of the fingerprint must be a multiple of 256 in order to be able to search it with the popcount method.

![](_page_125_Figure_9.jpeg)

Fig. 12: Schematic representation of fast fingerprint generation process

- OEFastFPDatabaseParams class
- Example code in Generating fingerprint file for fast fingerprint search section

## **5.3.7 OEDice**

float OEDice (const OEFingerPrint & fpA, const OEFingerPrint & fpB)

Calculates the Dice similarity value of two OEFingerPrint objects.

**Formula:**  $Sim_{Dice}(A, B) = \frac{2 * bothAB}{onlyA + onlyB + 2 * bothAB}$ 

#### See also:

• *Dice* section

## 5.3.8 OEEuclid

float OEEuclid (const OEFingerPrint & fpA, const OEFingerPrint & fpB)

Calculates the Euclidean similarity value of two OEFingerPrint objects.

**Formula:**  $Sim_{Euclid}(A, B) = \sqrt{\frac{bothAB + neitherAB}{onlyA + onlyB + bothAB + neitherAB}}$ 

#### See also:

• Euclidean section

### 5.3.9 OEGetBitCounts

OEGetBitCounts (OEFingerPrint fpA, OEFingerPrint fpB) -> (onlyA, onlyB, bothAB,  $\leftrightarrow$ neitherAB)

fpA, pfB The two OEFingerPrint objects being compared.

onlyA The number of bits set "on" in fingerprint  $fpA$  but not in  $fpB$ .

onlyB The number of bits set "on" in fingerprint  $fpB$  but not in  $fpA$ .

**bothAB** The number of bits set "on" in both OEFingerPrint objects.

neitherAB The number of bits unset in both OEFingerPrint objects.

See also:

• User-defined Similarity Measures section

### 5.3.10 OEGetCircularFPType

```
const OEFPTypeBase *OEGetCircularFPType (unsigned int numbits,
                                           unsigned int minradius, unsigned int
\rightarrowmaxradius,
                                           unsigned int atype, unsigned int btype)
```

Returns an OEFPType\_Circular fingerprint type generated with the given parameters.

**numbits** The size of the fingerprint in bits. This number has to be larger than or equal to  $2^4$  and smaller than  $2^{16}$ .

*minradius, maxradius* The smallest and largest circular fragments (in radius) that are enumerated during the fingerprint generation. All enumerated circular fragments are hashed into the OEFingerPrint object.

- atype Defines which atom properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPAt omType namespace.
- **btype** Defines which bond properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPBondType namespace.

#### See also:

• OEFPTypeBase class

## 5.3.11 OEGetFingerPrintVersion

unsigned short OEGetFingerPrintVersion (unsigned int fptype)

Returns the hashed number representation of the version number of a built-in fingerprint type. Please use the OEGetFingerPrintVersionString function to convert the returned number into human-readable representation.

The OEGetFingerPrintVersion function returns zero and throws a warning for unknown fingerprint type.

*fptype* The type of the fingerprint. This value has to be from the  $OEFPType$  namespace.

#### See also:

- OEGetFingerPrintVersionString function
- OEFPTypeBase. GetFPVersion method
- · OEFPTypeBase. GetFPVersionString method

## 5.3.12 OEGetFingerPrintVersionString

std::string OEGetFingerPrintVersionString (unsigned short version)

Returns the string representation of a fingerprint version number returned by either OEGetFingerPrintVersion function or OEFPTypeBase. GetFPVersion method.

#### See also:

- · OEGetFingerPrintVersion function
- · OEFPTypeBase. GetFPVersion method
- OEFPTypeBase. GetFPVersionString method

## 5.3.13 OEGetFPAtomType

std::string OEGetFPAtomType (unsigned int value)

Returns the string representation of a value that is from the OEFPAt omType namespace. For example, the string representation of OEFPAtomType\_AtomicNumber | OEFPAtomType\_Aromaticity value is the "AtmNum | Arom" string.

| Atom type                    | String representation |
|------------------------------|-----------------------|
| OEFPAtomType_AtomicNumber    | "AtmNum"              |
| OEFPAtomType_Aromaticity     | "Arom"                |
| OEFPAtomType_Chiral          | "Chiral"              |
| OEFPAtomType_FormalCharge    | "FCharge"             |
| OEFPAtomType_HvyDegree       | "HvyDeg"              |
| OEFPAtomType_Hybridization   | "Hyb"                 |
| OEFPAtomType_InRing          | "InRing"              |
| OEFPAtomType_HCount          | "HCount"              |
| OEFPAtomType_EqAromatic      | "EqArom"              |
| OEFPAtomType_EqHalogen       | "EqHalo"              |
| OEFPAtomType_EqHBondAcceptor | "EqHBAcc"             |
| OEFPAtomType_EqHBondDonor    | "EqHBDon"             |

|  | Table 19: The string representation of various fingerprint atom types |  |  |  |
|--|-----------------------------------------------------------------------|--|--|--|
|  |                                                                       |  |  |  |

unsigned int OEGetFPAtomType (const std:: string &expression)

This function is the inverse of the previous  $OEGetFPatomType$  function *i.e.* it converts the string representation into a value from the OEFPAt omType namespace.

### 5.3.14 OEGetFPBondType

```
std::string OEGetFPBondType (unsigned int value)
```

Returns the string representation of a value that is from the OEFPBOndType namespace. For example, the string representation of OEFPBondType\_BondOrder | OEFPBondType\_Chiral value is the: "Order | Chiral" string.

| Bond type                     | String representation |
|-------------------------------|-----------------------|
| <i>OEFPBondType_BondOrder</i> | “Order”               |
| <i>OEFPBondType_Chiral</i>    | “Chiral”              |
| <i>OEFPBondType_InRing</i>    | “InRing”              |

#### Table 20: The string representation of various fingerprint bond types

unsigned int OEGetFPBondType (const std:: string &expression)

This function is the inverse of the previous  $OEGetFPBondType$  function *i.e.* it converts the string representation into a value from the OEFPBondType namespace.

### 5.3.15 OEGetFPCoverage

```
OESystem::OEIterBase<OEChem::OEAtomBondSet> *
  OEGetFPCoverage (const OEChem:: OEMolBase & mol, const OEFPTypeBase *fptype,
                  bool unique=false)
```

Returns an iterator over the fragments that are generated when a fingerprint is constructed.

mol The OEMolBase objects from which the fingerprint fragments are generated.

*fptype* The type of the fingerprint that also stores the parameters that are used when the fingerprint is generated.

**unique** If true, then the OEGetFPCoverage function returns only unique fragments. A fragment (i.e. a subgraph) is considered unique if it differs from all other subgraphs identified previously by at least one atom or bond.

**Note:** The OEGetFPCoverage function is not available for the OEFPType\_Lingo fingerprint type.

#### See also:

- Fingerprint Coverage chapter
- · OEGetFPOverlap function
- · OEGetFPPatterns function

## 5.3.16 OEGetFPDatabaseMemoryType

unsigned int OEGetFPDatabaseMemoryType (OESystem::OEInterface &itf, const std:: string name="-memorytype")

Returns the fingerprint database memory type initialized in the given interface.

*itf* The interface in which the parameter is configured.

name The name of the parameter.

#### See also:

- OEInterface class in the **OEChem TK** manual
- · OEFastFPDatabaseMemoryType namespace
- OEConfigureFPDatabaseMemoryType function
- Example code in Searching fast fingerprint database section

## 5.3.17 OEGetFPOverlap

```
OESvstem::OEIterBase<OEChem::OEMatchBase> *
  OEGetFPOverlap (const OEChem:: OEMolBase &qmol, const OEChem:: OEMolBase &tmol,
                 const OEFPTypeBase *fptype)
```

Returns an iterator over all **unique** matches (common fragments) found between two molecules based on the given fingerprint type. This means that these common molecular fragments are mapped into the same bit when fingerprints are generated with the given type.

*qmol, tmol* The two OEMolBase objects from which the fingerprint overlap is generated.

fptype The type of the fingerprint that also stores the parameters that are used when the fingerprint is generated.

**Note:** The OEGetFPOverlap function is not available for the OEFPType\_Lingo fingerprint type.

Note: Two matches are considered to be equivalent only if they store the same sets of target and pattern atoms and bonds. The correspondence between the pattern and target atoms and bonds are not considered.

- Fingerprint Overlap chapter
- OEGetFPCoverage function
- · OEGetFPPatterns function

### 5.3.18 OEGetFPPatterns

```
OESystem:: OEIterBase<OEFPPattern> *
 OEGetFPPatterns (const OEChem:: OEMolBase & mol, const OEFPTypeBase *fptype)
```

Returns an iterator over the patterns (OEFPPattern) that are generated when a fingerprint is constructed.

*mol* The OEMolBase objects from which the fingerprint patterns are generated.

fptype The type of the fingerprint that also stores the parameters that are used when the fingerprint is generated.

**Note:** The OEGetFPPatterns function is not available for the OEFPType\_Lingo and OEFPType\_MACCS166 fingerprint types.

#### See also:

- Fingerprint Patterns chapter
- OEGetFPCoverage function
- OEGetFPOverlap function

### 5.3.19 OEGetFPType

const OEFPTypeBase \*OEGetFPType (const unsigned int fptype, const bool vs=false)

Returns a *const* pointer of a default fingerprint type.

**for the Theorem State** of the fingerprint. This value has to be from the  $OEFPTV\mathcal{D}e$  namespace.

vs If true and the fingerprint type is either Path, Tree or Circular, then the atom and bond typings designed for virtual screening will be used. Any other cases this parameter will be ignored.

See also:

- OEFPAt omType namespace
- OEFPBondType namespace

const OEFPTypeBase \*OEGetFPType (const std::string &fptypestring)

Returns a *const* pointer of a fingerprint type of the given valid string representation. If the string representation is not valid, it will return a NULL pointer.

- · OEIsValidFPTypeString function
- · OEFPTypeBase. GetFPTypeString method
- OEFPTypeParams class
- OEGetCircularFPType function

- OEGetPathFPType function
- OEGet TreeFPType function

## 5.3.20 OEGetPathFPType

```
const OEFPTypeBase *OEGetPathFPType (unsigned int numbits,
                                    unsigned int minbonds, unsigned int maxbonds,
                                    unsigned int atype, unsigned int btype)
```

Returns an OEFPType\_Path fingerprint type generated with the given parameters.

**numbits** The size of the fingerprint in bits. This number has to be larger than or equal to  $2^4$  and smaller than  $2^{16}$ .

- *minbonds, maxbonds* The smallest and largest paths (in bonds) that are enumerated during the fingerprint generation. All enumerated paths are hashed into the OEFingerPrint object.
- atype Defines which atom properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPAt omType namespace.
- **btype** Defines which bond properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPBondType namespace.

See also:

• OEFPTypeBase class

## 5.3.21 OEGetPopCountMethod

unsigned int OEGetPopCountMethod()

Returns whether popcount method is supported on the hardware. The return value is taken from the OEPopCountMethod namespace.

See also:

- OEPopCountMethod namespace
- OEIsFastFPDatabaseReady function

## 5.3.22 OEGetSimilarityMeasureName

std::string OEGetSimilarityMeasureName(unsigned int simtype);

Returns the string representation of a built-in similarity measure.

simtype This value has to be from the OESimMeasure namespace.

### 5.3.23 OEGetTreeFPTvpe

```
const OEFPTypeBase *OEGetTreeFPType (unsigned int numbits,
                                    unsigned int minbonds, unsigned int maxbonds,
                                    unsigned int atype, unsigned int btype)
```

Returns an  $OEFFType\_Tree$  fingerprint type generated with the given parameters.

*numbits* The size of the fingerprint in bits. This number has to be larger than or equal to  $2^4$  and smaller than  $2^{16}$ .

- *minbonds, maxbonds* The smallest and largest tree fragments (in bonds) that are enumerated during the fingerprint generation. All enumerated tree fragments are hashed into the OEFingerPrint object.
- atype Defines which atom properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPAt omType namespace.
- **btype** Defines which bond properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPBondType namespace.

#### See also:

• OEFPTypeBase class

### 5.3.24 OEGraphSimGetArch

const char \*OEGraphSimGetArch()

### 5.3.25 OEGraphSimGetLicensee

```
bool OEGraphSimGetLicensee(std::string &licensee)
```

### 5.3.26 OEGraphSimGetPlatform

const char \*OEGraphSimGetPlatform()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify a platform. The format of these strings may change over time, and future distributions may contain different values even when using the same operating system, compiler and processor. For example, on an x86\_64 Red Hat Enterprise Linux box this would return redhat-RHEL5-g++4.1-x64.

### 5.3.27 OEGraphSimGetRelease

const char \*OEGraphSimGetRelease()

Returns the release name of the GraphSim TK library being used. This returns a value similar to 1.0 for production versions of the library, and 1.0 debug for the checking version of the library.

## 5.3.28 OEGraphSimGetSite

**bool** OEGraphSimGetSite(std::string &site)

## 5.3.29 OEGraphSimGetVersion

```
unsigned int OEGraphSimGetVersion()
```

## 5.3.30 OEGraphsimIsGPUReady

**bool** OEGraphsimIsGPUReady()

Determines whether a GPU is present and available for use on the current system.

#### See also:

GPU-Related Requirements section in the OEGraphSim TK manual.

## 5.3.31 OEGraphSimIsLicensed

**bool** OEGraphSimIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any GraphSim TK functionality.

The 'feature' argument can be used to check for a valid license to GraphSim TK along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current GraphSim TK license.

#### See also:

· OEChemIsLicensed function

## 5.3.32 OEIsFastFPDatabaseReady

**bool** OEIsFastFPDatabaseReady()

Returns whether any fast fingerprint (pop count) method supported on the hardware.

#### See also:

• OEGetPopCountMethod function

### 5.3.33 OEIsFPType

**bool** OEIsFPType (const OEFingerPrint &fp, unsigned int fptype)

Returns true if the given OEFingerPrint object's fingerprint type is identical to fptype. fptype has to be a value from the OEFPType namespace.

#### See also:

• OEIsSameFPType function

## 5.3.34 OEIsSameFPType

**bool** OEIsSameFPType (const OEFingerPrint & fpA, const OEFingerPrint & fpB)

Returns whether or not the types (OEFPTypeBase) of the two OEFingerPrint objects are the same.

Note: Two user-defined path fingerprints have the same type only if they have been generated with the same parameters (i.e. number of bits, minimum and maximum path size and atom and bond typing options) and have the same version number.

**Warning:** Similarity measure functions (such as  $OETanimot \phi$ ) only work on fingerprints with identical type (OEFPTypeBase).

### 5.3.35 OEIsValidFPTypeString

bool OEIsValidFPTypeString(std::string fptypestring);

Returns true if the given string is a valid representation of any available fingerprint types.

See also:

· OEFPTypeBase. GetFPTypeString method

### 5.3.36 OEMakeCircularFP

bool OEMakeCircularFP (OEFingerPrint &fp, const OEChem:: OEMolBase &mol)

Generates the OEFingerPrint object as a Circular fingerprint using default parameters.

 $fp$  The OEFingerPrint object that is being initialized.

*mol* The OEMolBase object from which the fingerprint is generated.

The following code snippet shows how to print out the string representation of a  $OEFPType\_Circular$  fingerprint. This string encodes information about default parameters used to generate a OEFPType\_Circular fingerprint.

```
fptype = oegraphsim. OEGetFPType (oegraphsim. OEFPType_Circular)
print (fptype.GetFPTypeString())
```

#### The output of the above code snippet is:

```
Circular, ver=2.0.0, size=4096, radius=0-5,
→atype=AtmNum|Arom|Chiral|FCharge|HCount|EgHalo,btype=Order
```

#### See also:

• OEFPTypeBase. GetFPTypeString method

```
bool OEMakeCircularFP (OEFingerPrint &fp, const OEChem:: OEMolBase &mol,
                      unsigned int numbits,
                      unsigned int minradius, unsigned int maxradius,
                      unsigned int atype, unsigned int btype)
```

Generates the *OEFingerPrint* object as a *Circular* fingerprint using the given parameters.

fp The OEFingerPrint object that is being initialized.

mol The OEMolBase object from which the fingerprint is generated.

*numbits* The size of the fingerprint in bits. This number has to be larger than or equal to  $2^4$  and smaller than  $2^{16}$ .

- *minradius, maxradius* The smallest and largest circular fragments (in radius) that are enumerated during the fingerprint generation. All enumerated circular fragments are hashed into the OEFingerPrint object.
- atype Defines which atom properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPAt omType namespace.
- **btype** Defines which bond properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPBondType namespace.

Note: For an empty molecule, both *OEMakeCircularFP* function will return false and the type of the fingerprint will be set to 0 (OEFingerPrint. GetFPTypeBase).

#### See also:

- User-defined Fingerprint chapter
- OEFPAtomType namespace
- OEFPBondType namespace

## 5.3.37 OEMakeFP

```
bool OEMakeFP (OEFingerPrint & fp, const OEChem:: OEMolBase & mol,
              const unsigned fptype, const bool vs=false)
```

Generates a fingerprint from the given molecule.

 $fp$  The OEFingerPrint object that is being initialized.

mol The OEMolBase object from which the fingerprint is generated.

**fivilibrary** The type of the fingerprint. This value has to be from the  $OEFPType$  namespace.

vs If  $true$  and the fingerprint type is either Path. Tree or Circular, then the atom and bond typings designed for virtual screening will be used. Any other cases this parameter will be ignored.

See also:

- OEFPAtomType namespace
- OEFPBondType namespace

```
bool OEMakeFP (OEFingerPrint & fp, const OEChem:: OEMolBase & mol,
               const OEFPTypeBase *fptype)
```

Generates a fingerprint from the given molecule.

fp The OEFingerPrint object that is being initialized.

mol The OEMolBase object from which the fingerprint is generated.

*fptype* The type of the fingerprint specified by an OEFPTypeBase pointer.

**Note:** For an empty molecule, both *OEMakeFP* function will return  $false$  and the type of the fingerprint will be set to 0 (OEFingerPrint.GetFPTypeBase).

#### 5.3.38 OEMakeLingoFP

bool OEMakeLingoFP (OEFingerPrint & fp, const OEChem:: OEMolBase & mol)

Generates the OEFingerPrint object as a LINGO fingerprint.

fp The OEFingerPrint object that is being initialized.

mol The OEMolBase object from which the fingerprint is generated.

Note: For an empty molecule, the OEMakeLingoFP function will return false and the type of the fingerprint will be set to 0 (OEFingerPrint.GetFPTypeBase).

#### See also:

• LINGO section

### 5.3.39 OEMakeMACCS166FP

bool OEMakeMACCS166FP (OEFingerPrint & fp, const OEChem:: OEMolBase & mol)

Generates the OEFingerPrint object as a MACCS fingerprint.

 $fp$  The OEFingerPrint object that is being initialized.

mol The OEMolBase object from which the fingerprint is generated.

```
Note: For an empty molecule, the OEMakeMACCS166FP function will return false and the type of the fingerprint
will be set to 0 (OEFingerPrint. GetFPTypeBase).
```

• MACCS section

### 5.3.40 OEMakePathFP

bool OEMakePathFP (OEFingerPrint & fp, const OEChem:: OEMolBase & mol)

Generates the OEFingerPrint object as a Path fingerprint using default parameters.

 $fp$  The OEFingerPrint object that is being initialized.

*mol* The OEMolBase object from which the fingerprint is generated.

The following code snippet shows how to print out the string representation of a  $OEFPType$ -Path fingerprint. This string encodes information about default parameters used to generate a OEFPType Path fingerprint.

fptype = oegraphsim. OEGetFPType (oegraphsim. OEFPType\_Path) print (fptype.GetFPTypeString())

The output of the above code snippet is:

```
Path, ver=2.0.0, size=4096, bonds=0-5, atype=AtmNum|Arom|Chiral|FCharge|HvyDeg|Hyb|EqHalo,
→btype=Order|Chiral
```

#### See also:

• OEFPTypeBase. GetFPTypeString method

```
bool OEMakePathFP (OEFingerPrint &fp, const OEChem:: OEMolBase &mol,
                  unsigned int numbits,
                  unsigned int minbonds, unsigned int maxbonds,
                  unsigned int atype, unsigned int btype)
```

Generates the OEFingerPrint object as a Path fingerprint using the given parameters.

fp The OEFingerPrint object that is being initialized.

mol The OEMolBase object from which the fingerprint is generated.

**numbits** The size of the fingerprint in bits. This number has to be larger than or equal to  $2^4$  and smaller than  $2^{16}$ .

- *minbonds, maxbonds* The smallest and largest paths (in bonds) that are enumerated during the fingerprint generation. All enumerated paths are hashed into the *OEFingerPrint* object.
- atype Defines which atom properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPAt omType namespace.
- **btype** Defines which bond properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPBondType namespace.

Note: For an empty molecule, both OEMakePathFP function will return false and the type of the fingerprint will be set to 0 (OEFingerPrint. GetFPTypeBase).

- User-defined Fingerprint chapter
- OEFPAtomType namespace
- OEFPBondType namespace

## 5.3.41 OEMakeTreeFP

bool OEMakeTreeFP (OEFingerPrint & fp, const OEChem:: OEMolBase & mol)

Generates the *OEFingerPrint* object as a *Tree* fingerprint using default parameters.

 $fp$  The OEFingerPrint object that is being initialized.

*mol* The OEMolBase object from which the fingerprint is generated.

The following code snippet shows how to print out the string representation of a  $OEFPType\_Tree$  fingerprint. This string encodes information about default parameters used to generate a OEFPType\_Tree fingerprint.

```
fptype = oegraphsim.OEGetFPType(oegraphsim.OEFPType_Tree)
print (fptype.GetFPTypeString())
```

The output of the above code snippet is:

```
Tree, ver=2.0.0, size=4096, bonds=0-4, atype=AtmNum|Arom|Chiral|FCharge|HvyDeg|Hyb,
\rightarrowbtype=Order
```

See also:

· OEFPTypeBase. GetFPTypeString method

```
bool OEMakeTreeFP (OEFingerPrint &fp, const OEChem:: OEMolBase &mol,
                  unsigned int numbits,
                  unsigned int minbond, unsigned int maxbonds,
                  unsigned int atype, unsigned int btype)
```

fp The OEFingerPrint object that is being initialized.

*mol* The OEMolBase object from which the fingerprint is generated.

**numbits** The size of the fingerprint in bits. This number has to be larger than or equal to  $2^4$  and smaller than  $2^{16}$ .

- *minbonds, maxbonds* The smallest and largest tree fragments (in bonds) that are enumerated during the fingerprint generation. All enumerated tree fragments are hashed into the OEFingerPrint object.
- atype Defines which atom properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the  $OEFPatomType$  namespace.
- **btype** Defines which bond properties are encoded during the fingerprint generation. This value has to be either a value or a set of bitwise OR'd values from the OEFPBondType namespace.

Note: For an empty molecule, both *OEMakeTreeFP* function will return false and the type of the fingerprint will be set to 0 (OEFingerPrint. GetFPTypeBase).

- User-defined Fingerprint chapter
- OEFPAt omType namespace
- OEFPBondType namespace

### 5.3.42 OEManhattan

float OEManhattan (const OEFingerPrint & fpA, const OEFingerPrint & fpB)

Calculates the Manhattan similarity value of two OEFingerPrint objects.

**Formula:**  $Sim_{Manhattan}(A, B) = \frac{onlyA + onlyB}{onlyA + onlyB + bothAB + neitherAB}$ 

#### See also:

• Manhattan section

## 5.3.43 OESetupFingerPrint

```
const OEFPTypeBase *
 OESetupFingerPrint (const OESystem:: OEInterface &itf)
```

Initializes an OEFPTypeBase object from the parameters of a given interface.

#### See also:

- OEInterface class in the **OEChem TK** manual
- OEFPTypeBase class
- · OEConfigureFingerPrint function
- Example code in Generating fingerprint file for fast fingerprint search section
- Example code in Building and searching fingerprint database section

## 5.3.44 OESetupFPDatabaseOptions

```
bool OESetupFPDatabaseOptions (OEFPDatabaseOptions &opts,
                               const OESystem:: OEInterface &itf)
```

Initializes an OEFPDatabaseOptions object from the parameters of a given interface.

- OEInterface class in the **OEChem TK** manual
- OEFPDatabaseOptions class
- · OEConfigureFPDatabaseOptions function
- Example code in Building and searching fingerprint database section
- Example code in Searching fast fingerprint database section

## 5.3.45 OESimSearchStatusToName

std::string OESimSearchStatusToName(const unsigned status)

Returns the string representation of the constants in the OESimSearchStatus namespace.

#### See also:

· OEFastFPDatabase. SortedSearch method

### 5.3.46 OETanimoto

float OETanimoto (const OEFingerPrint & fpA, const OEFingerPrint & fpB)

Calculates the Tanimoto similarity value of two OEFingerPrint objects.

```
Formula: Sim_{Tanimoto}(A, B) = \frac{bothAB}{|A|+|B|-bothAB} = \frac{bothAB}{onlyA+onlyB+bothAB}
```

See also:

• Tanimoto section

### 5.3.47 OETversky

float OETversky (const OEFingerPrint & fpA, const OEFingerPrint & fpB, float a, float b)

Calculates the  $Tversky$  similarity value of two OEFingerPrint objects.

**Formula:**  $Sim_{Tversky}(A, B) = \frac{bothAB}{\alpha * only A + \beta * only B + both AB}$ 

See also:

• Tversky section

## **SIX**

## **RELEASE HISTORY**

## 6.1 GraphSim TK 2.6.1

## 6.1.1 Minor bug fixes

• The function OEGraphsimIsGPUReady has been safeguarded from a rare crash.

## 6.2 GraphSim TK 2.6.0

Minor internal improvements have been made.

## 6.3 GraphSim TK 2.5.7

Minor internal improvements have been made.

## 6.4 GraphSim TK 2.5.6

Minor internal improvements have been made.

## 6.5 GraphSim TK 2.5.5

Minor internal improvements have been made.

## 6.6 GraphSim TK 2.5.4

• Minor internal improvements have been made.

## 6.7 GraphSim TK 2.5.3

#### Fall 2021

• Minor internal improvements have been made.

## 6.8 GraphSim TK 2.5.2

July 2021

Minor internal improvements have been made.

## 6.9 GraphSim TK 2.5.1

**Fall 2020** 

## 6.9.1 New features

• GPU-accelerated OEFastFPDatabase searches now require a minimum NVIDIA Driver version of 450.x and a minimum GPU compute capability of 3.5. See NVIDIA Drivers and Supported GPUs for more details.

## 6.10 GraphSim TK 2.5.0

## 6.10.1 New features

- The following new APIs have been added that enable multi-threaded similarity search and access to a histogram of the similarity score distributions:
  - OEFastFPDatabase. SortedSearch method
  - OESimSearchResult method
  - OESimSearchStatus namespace
  - OESimSearchStatusToNamefunction
- . Two new methods, OEFPDatabaseOptions. SetNumProcessors and OEFPDatabaseOptions. GetNumProcessors, have been added that control the number of threads used to search fingerprints when using OEFastFPDatabase. SortedSearch.
- New atom and bond typing combinations have been added to generate  $tree$ ,  $path$ , and  $circular$  fingerprints that are optimized for virtual screening. The OEMakeFP and OEGetFPType methods can now generate these new types. See also the OEFPAt omType and OEFPBondType namespaces.
- Small optimization has been achieved by reducing cache misses during the fingerprint search when using the OEFastFPDatabase class.
- . New overloads of the OEFPHistogram. GetBinIdx and OEFPHistogram. AddSample methods have been added that take a double parameter.

## 6.10.2 Major bug fixes

• The binary fingerprint database writer had been accidentally broken in the Oct.2019 release. This has been fixed.

## 6.10.3 Minor bug fixes

• The default limit of the OEFPDatabaseOptions class has been changed from 0 (meaning no limit) to 1000. See also the OEFPDatabaseOptions. SetLimit method.

## 6.10.4 General Notices

• In the C++ GraphSim TK, Fast fingerprints with the CUDA memory type is not available on RHEL8 or Ubuntu18.

## 6.11 GraphSim TK 2.4.3

## 6.11.1 New features

• A new method, OEFastFPDatabase. GetMoleculeIndex, has been added.

## 6.11.2 Minor bug fixes

• OEIsValidFPTypeString no longer throws an error and always return false if the given string cannot be interpreted.

## **6.12 GraphSim TK 2.4.2**

• Minor internal improvements have been made.

## 6.13 GraphSim TK 2.4.1

## 6.13.1 New features

- A new OEFastFPDatabase. GetFingerPrint method has been added to allow retrieving fingerprints stored in fast fingerprint databases that are generated in a single-threaded mode.
- . New OEFPDatabaseOptionsSetup\_Cutoff and OEFPDatabaseOptionsSetup\_DescendingOrder methods have been added to help generate consistent command line interfaces.
- A new OEFastFPDatabase. GetSparseMatrix method has been added to allow retrieving a sparse matrix of similarity scores to facilitate clustering. The method will retrieve limit scores per fingerprint or all scores above a desired cutoff value. The method is available in all memory modes, including CUDA.

## 6.13.2 Minor bug fixes

• The OEGetFingerPrintVersion function no longer throws an error for an invalid fingerprint type. It now throws a warning and returns zero.

## 6.14 GraphSim TK 2.4.0

### 6.14.1 New features

- GraphSim TK now has limited GPU support for fast fingerprints. CUDA has been added to the OEFastFPDatabaseMemoryType namespace for executing large 2D searches and to have GPU devices at their disposal. This new feature comes with the following additional API points:
  - OEFastFPDatabase. GetRawScores
  - OEFastFPDatabase. GetAllScores
  - OEFastFPDatabase. GetHistogram and OEFPHistogram (preliminary)
  - OEFastFPDatabase. GetVariogram and OEFPVariogram (preliminary)
  - OEFastFPDatabase.GetMemoryType
  - OEFastFPDatabase. GetMemoryTypeString

For more information, see the documentation for OEFastFPDatabaseMemoryType CUDA.

- The following API has been added to help generate consistent command line interfaces for 2D molecule similarity examples and utilities:
  - OEFPDatabaseOptionsSetup
  - OEConfigureFPDatabaseOptions
  - OEConfigureFPDatabaseMemoryType
  - OEGetFPDatabaseMemoryType

## 6.15 GraphSim TK 2.3.1

#### 6.15.1 New features

- The following API has been added to provide access to underlying data generated for  $OEFPType\_Path$ , OEFPType\_Tree, and OEFPType\_Circular fingerprint types:
  - $-$  OEFPPattern
  - OEGetFPPatterns
- The performance of the  $OEGetFPCoverage$  function has been improved.
- The following functions have been added to help generate consistent command line interfaces for 2D molecule similarity examples and utilities:
  - OEConfigureFingerPrint and the corresponding OESetupFingerPrint
  - OEConfigureFPDatabaseOptions and the corresponding OESetupFPDatabaseOptions

Generated interfaces include correspondence between each command line option and its related entry point in **OEGraphSim TK.** 

### **6.15.2 Documentation changes**

• A new Fingerprint Patterns chapter has been added.

## 6.16 GraphSim TK 2.3.0

### 6.16.1 New features

- A new API has been added to perform rapid searching of fingerprints using the popcount method:
  - OECreateFastFPDatabaseFile function and OECreateFastFPDatabaseOptions class to generate binary fingerprint files
  - OEFastFPDatabase class and OEFastFPDatabaseMemoryType namespace to perform rapid inmemory or memory-mapped fingerprint searches using the popcount method
  - OEFastFPDatabaseParams utility class and OEAreCompatibleDatabases utility function
  - OEIsFastFPDatabaseReady OEGetPopCountMethod and functions and OEPopCountMethod namespace to check whether the popcount method is supported on the current hardware

Note: GraphSim TK currently only supports the popcount search method for fingerprints where the size is multiple of 256. This means that the  $OEFPType\_MACCS166$  fingerprint type is currently not supported. See the User-defined Fingerprint section.

OEFastFPDatabase gives identical results to OEFPDatabase. However OEFPDatabase calculates Note: similarity scores in single precision (float) while OEFastFPDatabase uses double precision. As a result small similarity score differences can be observed.

## 6.16.2 API Change

• The OESimScore class, which is utilized by both the OEFPDatabase class and the new OEFastFPDatabase class, stores a similarity value with a corresponding molecule index. This pair is now stored as "double" and "size\_t" rather than "float" and "unsigned int". This **non-breaking** API change allows **GraphSim TK** to support molecular files that contain more than  $2^{32}$  entries and supports double precision similarity scores calculated using the new OEFastFPDatabase class.

## 6.16.3 C++-specific changes

• The above-mentioned OESimScore class API change means that the following warning messages could be encountered when compiling old code with the new GraphSim TK:

```
- implicit conversion loses floating point precision: 'double' to
  'float'
```

```
for (OEIter<OESimScore> si = fpdb.GetScores(mol); si; ++si)
 float score = si->GetScore(); // GetScore() now returns double
```

- implicit conversion loses integer precision : 'size\_t' to 'unsigned int'

```
for (OEIter<OESimScore> si = fpdb.GetScores(mol); si; ++si)
 unsigned int molidx = si->GetIdx(); // GetIdx() now returns size_t
```

### 6.16.4 Java-specific changes

• The above-mentioned OESimScore class API change means that a similarity value with a corresponding molecule index is now expected to be "double" and "long", respectively.

## **6.16.5 Documentation changes**

- A new section, Building and searching fingerprint database, has been added.
- New Generating fingerprint file for fast fingerprint search and Searching fast fingerprint database sections have been added with examples showing generation and searching of fingerprints using the OEFastFPDatabase class.

## 6.17 GraphSim TK 2.2.6

## 6.17.1 New features

- Three new functions, OEGetCircularFPType, OEGetPathFPType, and OEGetTreeFPType, have been added to enable generating fingerprint types with user-defined parameters.
- A new constructor, OEFPTypeParams, has been added that takes a fingerprint type (OEFPTypeBase).
- Four functions that automatically generate standard interfaces for GraphSim TK applications have been added:
  - OEConfigureFingerPrint
  - OESetupFingerPrint
  - OEConfigureFPDatabaseOptions
  - OESetupFPDatabaseOptions
- A new constructor,  $OEFPDatabaseOption$ , has been added that takes a similarity method from the  $OESimMeasure$  namespace and a limit on the number of similarity scores returned from a query.

## 6.18 GraphSim TK 2.2.5

• Minor internal improvements have been made.

## 6.19 GraphSim TK 2.2.4

## 6.19.1 New features

- OEFPDatabaseOptions class has been added to allow simultaneous fingerprint database searches.
- OEFPDatabase. GetScores and OEFPDatabase. GetSortedScores methods have been overloaded. The new versions take an OEFPDatabaseOptions search parameter.
- · OEFPDatabase. SetDescendingOrder and OEFPDatabase. GetDescendingOrder methods have been added to allow setting the order in which the fingerprint scores are returned by the OEFPDatabase. GetSortedScores method to be set.

## 6.19.2 Minor bug fixes

· OEFPDatabase. GetScores and OEFPDatabase. GetSortedScores now throw warnings instead of error messages in the case of fingerprint type mismatches before returning an empty iterator.

## 6.20 GraphSim TK 2.2.3

• Minor internal improvements have been made.

## 6.20.1 Documentation changes

• The documentation for  $OETversky$  function has been restored.

## 6.21 GraphSim TK 2.2.2

• Minor internal improvements have been made.

## 6.22 GraphSim TK 2.2.1

• Minor internal improvements have been made.

Note: A mistake was made in the 2015. Feb release such that the OEGraphSimGetRelease function returns 2.1.2 rather than 2.2.0.

## **6.23 GraphSim TK 2.2.0**

## 6.23.1 Major bug fixes

- OEFPType\_MACCS166 fingerprints bit "91" and bit "92" have been fixed to behave properly. The previous behavior was the following:
  - Bit 91 could have been turned on by either  $[48] \sim [46]$  ( $\sim [47]$ )  $\sim [46]$  or  $[46H3] \sim [46; 141]$ .
  - Bit 92 was never turned on.

The behavior has been fixed to do the following:

- Bit 91 is now only turned on by  $[48] \sim [46]$  ( $\sim [47]$ )  $\sim [46]$ .
- Bit 92 is now turned on by  $[#6H3] \sim [#6; !#1].$

**Warning:** This change was required to revise the version of the  $OEFPType$  MACCS166 fingerprints from 2.0.0 to 2.2.0.

For more information about version numbers, see the *Fingerprint version number* section.

• The customizable fingerprints (OEFPType\_Path, OEFPType\_Tree, and OEFPType\_Circular) can now be generated without encoding any atom or bond properties by using the OEFPAtomType None or OEFPBondType\_None constants, respectively. However, a warning will be thrown if using OEFPAt omType\_None and OEFPBondType\_None constants together.

## **6.23.2 Documentation fixes**

- Code snippets have been added to the following functions that print the string representation of generated fingerprints:
  - OEMakeCircularFP function
  - OEMakePathFP function
  - OEMakeTreeFP function

**Hint:** The string representation reveals information about the fingerprinting method and the parameters being used to generate the fingerprint.

## 6.24 GraphSim TK 2.1.1

## **6.24.1 Documentation fixes**

• Explaining the hexadecimal string representation of fingerprints generated by the OEBitVector. ToHexString method.

## 6.25 GraphSim TK 2.1.0

## 6.25.1 Minor bug fixes

• Removed unbounded stack allocations.

## **6.25.2 Documentation fixes**

• The MemSimSearch documentation example demonstrates how to use a OEMolDatabase to minimize memory usage. See the Sorted Search section for a description of how this is done.

## 6.26 GraphSim TK 2.0.7

## **6.26.1 Documentation changes**

- Added a section about Visualizing Molecule Similarity.
- Added note to the OEFPAtomType\_Aromaticity constant.
- Added new images to the:
  - OEFPAt omType namespace to visualize the effect of atom typings.
  - $-$  OEFPBondType namespace to visualize the effect of bond typings.

## 6.27 GraphSim TK 2.0.6

• OEFPDatabase. AddFP in Python will now properly throw an exception on failure on 32-bit machines.

## 6.27.1 Documentation changes

Adding new images to the:

- Fingerprint Generation chapter to illustrate the enumeration of fragments of various fingerprints
- Similarity Measures chapter to show the basic bit count terms of similarity calculation
- User-defined Fingerprint chapter and OEFPAt omType namespace to visualize the effect of various atom and bond typings

## 6.28 GraphSim TK 2.0.5

## 6.28.1 Major bug fixes

- The performance of the  $OEGetFPOverlap$  function improved on average for drug-like structures:
  - $-15\%$  for OEFPType\_Path
  - 30% for OEFPType\_Tree
  - 10% for OEFPType\_Circular

The improvement is significantly more for very complex molecules such as buckyball structures.

## 6.29 GraphSim TK 2.0.4

• Minor internal improvements.

## 6.30 GraphSim TK 2.0.3

• Internal build system improvements.

## 6.31 GraphSim TK 2.0.2

• Internal build system improvements.

## 6.32 GraphSim TK 2.0.1

### 6.32.1 Minor bug fixes

- If a molecule being fingerprinted has only hydrogen atom(s), for example molecule  $[H]$ , then an empty fingerprint is generated, that is, all bits of the fingerprint are set to zero. All hydrogens of the molecule (polar, stereo, isotope, charge) are suppressed before generating its fingerprint.
- If the shell of the circular fingerprint can not be extended, for example, all atoms of the molecule are already being considered, then the search is terminated. This modification does not effect the generated circular fingerprints, it only makes the generation process faster.
- Some of the algorithms generating fingerprints can return the same fragment of a molecule more than once. For example the path fingerprint enumerates both OC and CO. These duplicates are now filtered out when calling the OEGETPOverlap function. Two overlaps are considered equivalent only if they store the same target and pattern atoms and bonds, not considering the correspondence between the pattern and target atoms and bonds.

## 6.33 GraphSim TK 2.0.0

### 6.33.1 New features

- Adding two new fingerprint types:
  - The OEFPType\_Circular fingerprint is generated by exhaustively enumerating all circular fragments grown radially from each heavy atom of the input molecule up to the given radius. (See more details in Circular Fingerprint section and OEMakeCircularFP function)
  - The OEFPType\_Tree fingerprint is generated by exhaustively enumerating all unique trees of a molecular graph. (See more details in *Tree Fingerprint* section and OEMakeTreeFP function)
- Adding the OEGetFPCoverage function that allows access to the patterns that are encoded into a fingerprint. (See example in *Fingerprint Coverage* chapter)

- Adding the OEGetFPOverlap function that returns the common patterns of two molecules based on their fingerprint. (See example in *Fingerprint Overlap* chapter)
- Adding version numbers for fingerprints that prevents the comparison of fingerprints that are generated by different versions of the algorithm. (See more details in *Fingerprint version number* section and OEGetFingerPrintVersion and OEGetFingerPrintVersionString functions)
- Adding three more atom typing options that can be used when generating path, circular or tree fingerprints:
  - OEFPAtomType HCount
  - OEFPAtomType\_EqHBondAcceptor
  - OEFPAtomType\_EqHBondDonor
- Adding the  $OEGetFPType$  function that generates a fingerprint type from a valid string representation.
- Adding the OEFPTypeParams that allow to extract the parameters of the fingerprint types from their string representation:
- Adding 9 code examples in four different languages (C++, Python, Java, C#) that demonstrate the usage of fingerprints and functionalities.

## **6.33.2 Documentation changes**

- Adding figures to the Fingerprint chapter that demonstrate how the OEFPType\_Circular, OEFPType\_Path and OEFPType\_Tree fingerprints are generated.
- Adding a new chapter *Fingerprint Types*, that gives more details about fingerprint types.
- Adding two new examples to the Storage and Retrieval chapter that demonstrate how to store and retrieve fingerprints in SDF files.
- Rewriting part of the User-defined Fingerprint chapter, since the two new fingerprint types can also be customized.
- Adding two new chapters:
  - Fingerprint Coverage chapter
  - Fingerprint Overlap chapter

## 6.34 GraphSim TK 1.0.1

## 6.34.1 Documentation changes

• Adding an example to the *Storage and Retrieval* section that demonstrate how to generate a bitstring from an OEFingerPrint object.

## 6.35 GraphSim TK 1.0.0

- Provides the following features:
  - Generate three basic fingerprint types (MACCS key, LINGO and path-based)
  - Parameterize the path-based fingerprint generation
    - \* allowing various atom/bond typing
    - \* specifying the minimum and maximum length of the enumerated paths
    - \* setting the size of fingerprint
  - Store and retrieve fingerprints as generic data
  - Save/import fingerprints to/from OEB binary file format
- Implementation of six common similarity indices (Cosine, Dice, Euclidean, Manhattan, Tanimoto, Tversky)
- Implementation of fingerprint database that provides the following methods for rapid fingerprint-based similarity search:
  - apply user-defined similarity measures
  - set similarity cutoff value
  - access similarity in sorted order

## **SEVEN**

## **COPYRIGHT AND TRADEMARKS**

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

## **EIGHT**

## **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

## **NINE**

## **CITATION**

## 9.1 Orion<sup>®</sup> Floes

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

## **9.2 Toolkits and Applications**

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

## 9.3 OpenEye Web Services

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

**TEN** 

## **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project                  | Website                                                                             | License                                                                             |
|----------------------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| abseil-cpp                       | https://github.com/abseil/abseil-cpp                                                | https://                                                                            |
| absl-py                          | https://github.com/abseil/abseil-py                                                 | https://                                                                            |
| aiohttp                          | https://docs.aiohttp.org/en/stable/                                                 | https://                                                                            |
| aiosignal                        | https://github.com/aio-libs/aiosignal                                               | https://                                                                            |
| Amazon Linux 2                   | https://aws.amazon.com/amazon-linux-2                                               | N/A                                                                                 |
| AmberUtils                       | http://ambermd.org                                                                  | N/A                                                                                 |
| ambit                            | https://github.com/khimaros/ambit                                                   | https://                                                                            |
| amqp                             | https://github.com/celery/py-amqp                                                   | https://                                                                            |
| anaconda-anon-usage              | Orion Floes                                                                         | https://                                                                            |
| angular                          | https://github.com/angular/angular.js                                               | https://                                                                            |
| angular-animate                  | https://github.com/angular/angular.js                                               | https://                                                                            |
| angular-cache                    | https://github.com/jmdobry/angular-cache                                            | https://                                                                            |
| angular-cookies                  | https://github.com/angular/angular.js                                               | https://                                                                            |
| angular-loggly-logger            | https://github.com/ajbrown/angular-loggly-logger                                    | https://                                                                            |
| angular-mocks                    | https://github.com/angular/angular.js                                               | https://                                                                            |
| angular-resource                 | https://github.com/angular/angular.js                                               | https://                                                                            |
| angular-toggle-switch            | https://github.com/cgarvis/angular-toggle-switch                                    | https://                                                                            |
| angular-ui-grid                  | https://github.com/angular-ui/ui-grid                                               | https://                                                                            |
| angular-ui-router                | https://github.com/angular-ui/ui-router                                             | https://                                                                            |
| angular-ui-tree                  | https://github.com/angular-ui-tree/angular-ui-tree                                  | https://                                                                            |
| angular-vs-repeat                | https://github.com/kamilkp/angular-vs-repeat                                        | https://                                                                            |
| aniso8601                        | https://bitbucket.org/nielsenb/aniso8601                                            | https://                                                                            |
| annotated-types                  | https://github.com/annotated-types/annotated-types                                  | https://                                                                            |
| anyio                            | https://github.com/agronholm/anyio                                                  | https://                                                                            |
| appdirs                          | http://github.com/ActiveState/appdirs                                               | http://                                                                             |
| appengine                        | https://google.golang.org/appengine                                                 | https://                                                                            |
| arabic-reshaper                  | https://github.com/mpcabd/python-arabic-reshaper/                                   | https://                                                                            |
| archspec                         | https://github.com/archspec/archspec/blob/master/README.md                          | https://                                                                            |
| Name of Project                  | Website                                                                             | License                                                                             |
| argon2-cffi                      | https://github.com/hynek/argon2-cffi                                                | https:/                                                                             |
| argon2-cffi-bindings             | https://github.com/hynek/argon2-cffi-bindings                                       | https:/                                                                             |
| arpack                           | https://www.caam.rice.edu/software/ARPACK/                                          | https:/                                                                             |
| ascii85                          | https://github.com/huandu/node-ascii85                                              | https:/                                                                             |
| ase                              | https://wiki.fysik.dtu.dk/ase/                                                      | https:/                                                                             |
| asgiref                          | https://github.com/django/asgiref/                                                  | https:/                                                                             |
| asn1crypto                       | https://github.com/wbond/asn1crypto                                                 | https:/                                                                             |
| assertions go-render             | https://github.com/smartystreets/assertions/internal/go-render/render               | https:/                                                                             |
| assertions oglmatchers           | https://github.com/smartystreets/assertions/internal/oglematchers                   | https:/                                                                             |
| assertions                       | https://github.com/smartystreets/assertions                                         | https:/                                                                             |
| asttokens                        | https://github.com/gristlabs/asttokens                                              | https:/                                                                             |
| astunparse                       | https://github.com/simonpercivall/astunparse                                        | https:/                                                                             |
| async-lru                        | https://github.com/aio-libs/async-lru                                               | https:/                                                                             |
| async-timeout                    | https://github.com/aio-libs/async-timeout                                           | https:/                                                                             |
| atk-1.0                          | https://docs.gtk.org/atk/                                                           | https:/                                                                             |
| atomic                           | https://github.com/uber-go/atomic                                                   | https:/                                                                             |
| atomicwrites                     | https://github.com/untitaker/python-atomicwrites                                    | https:/                                                                             |
| attrs                            | https://www.attrs.org/                                                              | https:/                                                                             |
| aws-sdk-go                       | https://github.com/aws/aws-sdk-go                                                   | https:/                                                                             |
| Babel                            | https://github.com/python-babel/babel                                               | https:/                                                                             |
| backcall                         | https://github.com/takluyver/backcall                                               | https:/                                                                             |
| backports                        | https://github.com/brandon-rhodes/backports                                         | https:/                                                                             |
| backports.functools-lru-cache    | https://github.com/jaraco/backports.functools_lru_cache                             | https:/                                                                             |
| base62                           | https://github.com/kare/base62                                                      | https:/                                                                             |
| beautifulsoup4                   | https://www.crummy.com/software/BeautifulSoup/                                      | https:/                                                                             |
| billiard                         | https://github.com/celery/billiard                                                  | https:/                                                                             |
| biopython                        | https://biopython.org                                                               | https:/                                                                             |
| biotite                          | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https:/                                                                             |
| bitset                           | https://github.com/willf/bitset                                                     | https:/                                                                             |
| blas                             | https://www.netlib.org/blas/                                                        | https:/                                                                             |
| bleach                           | https://github.com/mozilla/bleach                                                   | https:/                                                                             |
| blessings                        | https://github.com/erikrose/blessings                                               | https:/                                                                             |
| blinker                          | https://pythonhosted.org/blinker/                                                   | https:/                                                                             |
| blosc                            | https://github.com/Blosc/python-blosc                                               | https:/                                                                             |
| blosc2                           | https://github.com/Blosc/python-blosc2                                              | https:/                                                                             |
| boltons                          | https://github.com/mahmoud/boltons                                                  | https:/                                                                             |
| boost                            | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                                             |
| boost-cpp                        | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                                             |
| bootstrap-vue                    | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                                                             |
| boto3                            | https://github.com/boto/boto3                                                       | https:/                                                                             |
| botocore                         | https://github.com/boto/botocore                                                    | https:/                                                                             |
| Bottleneck                       | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                                                             |
| Brotli                           | https://github.com/google/brotli                                                    | https:/                                                                             |
| brotli-bin                       | https://github.com/google/brotli                                                    | https:/                                                                             |
| brotli-python                    | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                                                             |
| brotlipy                         | https://github.com/python-hyper/brotlicffi                                          | https:/                                                                             |
| bson                             | http://github.com/py-bson/bson                                                      | https:/                                                                             |
| bytefmt                          | https://code.cloudfoundry.org/bytefmt                                               | https:/                                                                             |
| bzip2                            | https://www.bzip.org                                                                | https:/                                                                             |
| Name of Project                  | Website                                                                             | License                                                                             |
| c-ares                           | https://github.com/c-ares/c-ares                                                    | https://                                                                            |
| ca-certificates                  | https://github.com/conda-forge/ca-certificates-feedstock                            | https://                                                                            |
| cached-property                  | https://github.com/pydanny/cached-property                                          | https://                                                                            |
| cachetools                       | https://github.com/tkem/cachetools                                                  | https://                                                                            |
| cairo                            | https://pycairo.readthedocs.io/en/latest/                                           | https://                                                                            |
| canvas                           | https://github.com/Automattic/node-canvas                                           | https://                                                                            |
| cctbx                            | https://github.com/cctbx/cctbx_project                                              | https://                                                                            |
| celery                           | https://github.com/celery/celery                                                    | https://                                                                            |
| Cerberus                         | https://docs.python-cerberus.org/en/stable/                                         | https://                                                                            |
| certifi                          | https://certifi.readthedocs.io/en/latest/                                           | https://                                                                            |
| cffi                             | https://github.com/python-cffi                                                      | https://                                                                            |
| cftime                           | https://pypi.org/project/cftime/                                                    | https://                                                                            |
| chardet                          | https://github.com/chardet/chardet                                                  | https://                                                                            |
| charset-normalizer               | https://github.com/ousret/charset_normalizer                                        | https://                                                                            |
| chunkreader                      | https://github.com/jackc/chunkreader/v2                                             | https://                                                                            |
| click                            | https://palletsprojects.com/p/click/                                                | https://                                                                            |
| click-completion                 | https://github.com/click-contrib/click-completion                                   | https://                                                                            |
| click-didyoumean                 | https://github.com/click-contrib/click-didyoumean                                   | https://                                                                            |
| click-plugins                    | https://github.com/click-contrib/click-plugins                                      | https://                                                                            |
| click-repl                       | https://github.com/untitaker/click-repl                                             | https://                                                                            |
| cloudpickle                      | https://github.com/cloudpipe/cloudpickle                                            | https://                                                                            |
| cmake                            | https://cmake.org/                                                                  | https://                                                                            |
| colorama                         | https://github.com/tartley/colorama                                                 | https://                                                                            |
| comm                             | https://github.com/ipython/comm                                                     | https://                                                                            |
| compose                          | https://github.com/docker/compose                                                   | https://                                                                            |
| conda-content-trust              | https://github.com/conda/conda-content-trust                                        | https://                                                                            |
| conda-libmamba-solver            | https://github.com/conda/conda-libmamba-solver                                      | https://                                                                            |
| conda-package-handling           | https://github.com/conda/conda-package-handling                                     | https://                                                                            |
| conda-package-streaming          | https://anaconda.org/conda-forge/conda-package-streaming                            | https://                                                                            |
| conda-token                      | https://anaconda.org/anaconda/conda-token                                           | https://                                                                            |
| confuse                          | https://github.com/beetbox/confuse                                                  | https://                                                                            |
| contourpy                        | https://github.com/contourpy/contourpy                                              | https://                                                                            |
| cpp-peglib                       | https://github.com/yhirose/cpp-peglib                                               | https://                                                                            |
| cryptography                     | https://github.com/pyca/cryptography                                                | https://                                                                            |
| cssselect2                       | https://github.com/Kozea/cssselect2/                                                | https://                                                                            |
| cudatoolkit                      | https://developer.nvidia.com/cuda-toolkit                                           | https://                                                                            |
| cupy-cuda113                     | https://cupy.dev/                                                                   | https://                                                                            |
| curl                             | https://curl.se                                                                     | https://                                                                            |
| cycler                           | https://github.com/matplotlib/cycler                                                | https://                                                                            |
| cyrus-sasl                       | https://github.com/cyrusimap/cyrus-sasl                                             | https://                                                                            |
| Cython                           | https://cython.org                                                                  | https://                                                                            |
| d3                               | https://github.com/mbostock/d3                                                      | https://                                                                            |
| dataclasses                      | https://github.com/ericvsmith/dataclasses                                           | https://                                                                            |
| ddsketch                         | https://github.com/datadog/sketches-py                                              | https://                                                                            |
| debugpy                          | https://aka.ms/debugpy                                                              | https://                                                                            |
| decimal                          | https://github.com/shopspring/decimal                                               | https://                                                                            |
| decorator                        | https://github.com/micheles/decorator                                               | https://                                                                            |
| deepdiff                         | https://github.com/seperman/deepdiff                                                | https://                                                                            |
| deeptime                         | https://github.com/deeptime-ml/deeptime                                             | https://                                                                            |
| Name of Project                  | Website                                                                             | License                                                                             |
| defusedxml                       | https://github.com/tiran/defusedxml                                                 |                                                                                     |
| dill                             | https://github.com/uqfoundation/dill                                                |                                                                                     |
| distro                           | Orion Flores                                                                        |                                                                                     |
| Django                           | https://www.djangoproject.com/                                                      |                                                                                     |
| django-classy-tags               | https://github.com/django-cms/django-classy-tags                                    |                                                                                     |
| django-cors-headers              | https://github.com/adamchainz/django-cors-headers                                   |                                                                                     |
| django-csp                       | https://github.com/mozilla/django-csp                                               |                                                                                     |
| django-extensions                | https://github.com/django-extensions/django-extensions                              |                                                                                     |
| django-filter                    | https://github.com/carltongibson/django-filter/tree/master                          |                                                                                     |
| django-redis                     | https://github.com/jazzband/django-redis                                            |                                                                                     |
| django-taggit                    | https://github.com/jazzband/django-taggit                                           |                                                                                     |
| django-taggit-serializer         | https://github.com/glemmaPaul/django-taggit-serializer                              |                                                                                     |
| django-taggit-templatetags2      | https://github.com/fizista/django-taggit-templatetags2                              |                                                                                     |
| djangorestframework              | https://www.django-rest-framework.org/                                              |                                                                                     |
| dkh                              | https://psicode.org/psi4manual/master/dkh.html                                      |                                                                                     |
| dm-tree                          | https://github.com/deepmind/tree                                                    |                                                                                     |
| docker-py                        | https://github.com/docker/docker-py/                                                |                                                                                     |
| docopt                           | https://docopt.org                                                                  |                                                                                     |
| docutils                         | https://docutils.sourceforge.io                                                     |                                                                                     |
| drf-dynamic-fields               | https://github.com/dbrgn/drf-dynamic-fields                                         |                                                                                     |
| editdistance                     | https://github.com/roy-ht/editdistance                                              |                                                                                     |
| eigen                            | https://eigen.tuxfamily.org/index.php?title=Main_Page                               |                                                                                     |
| einops                           | https://github.com/arogozhnikov/einops                                              |                                                                                     |
| entrypoints                      | https://github.com/takluyver/entrypoints                                            |                                                                                     |
| errors                           | https://github.com/pkg/errors                                                       |                                                                                     |
| eslint-plugin                    | https://github.com/typescript-eslint/typescript-eslint                              |                                                                                     |
| et_xmlfile                       | https://foss.heptapod.net/openpyxl/et_xmlfile                                       |                                                                                     |
| exceptiongroup                   | https://github.com/agronholm/exceptiongroup                                         |                                                                                     |
| executing                        | https://github.com/alexmojaki/executing                                             |                                                                                     |
| expat                            | https://libexpat.github.io                                                          |                                                                                     |
| fastjsonschema                   | https://github.com/horejsek/python-fastjsonschema                                   |                                                                                     |
| fastrlock                        | https://github.com/scoder/fastrlock                                                 |                                                                                     |
| fftw                             | https://www.fftw.org                                                                | comm                                                                                |
| filebuffer                       | https://github.com/mattetti/filebuffer                                              |                                                                                     |
| filelock                         | https://py-filelock.readthedocs.io/en/latest/index.html                             |                                                                                     |
| finufft                          | https://github.com/flatironinstitute/finufft                                        |                                                                                     |
| Flask                            | https://flask.palletsprojects.com/en/2.1.x/                                         |                                                                                     |
| flatbuffers                      | https://google.github.io/flatbuffers/                                               |                                                                                     |
| flit-core                        | https://github.com/pypa/flit                                                        |                                                                                     |
| FLTK                             | https://www.fltk.org/index.php                                                      |                                                                                     |
| fmt                              | https://fmt.dev/latest/index.html                                                   |                                                                                     |
| font-awesome                     | https://github.com/FortAwesome/Font-Awesome                                         |                                                                                     |
| font-ttf-dejavu-sans-mono        | https://dejavu-fonts.github.io                                                      |                                                                                     |
| font-ttf-inconsolata             | https://fonts.google.com/specimen/Inconsolata                                       |                                                                                     |
| font-ttf-source-code-pro         | https://fonts.google.com/specimen/Source+Code+Pro                                   |                                                                                     |
| font-ttf-ubuntu                  | https://fonts.google.com/specimen/Ubuntu                                            |                                                                                     |
| fontconfig                       | https://www.freedesktop.org/wiki/Software/fontconfig/                               |                                                                                     |
| fonts-conda-ecosystem            | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             |                                                                                     |
| fonts-conda-forge                | https://anaconda.org/conda-forge/fonts-conda-forge/                                 |                                                                                     |
| Name of Project                  | Website                                                                             | License                                                                             |
| fonttools                        | https://github.com/fonttools/fonttools                                              | https://                                                                            |
| freetype                         | https://freetype.org                                                                | https://                                                                            |
| fribidi                          | https://github.com/fribidi/fribidi                                                  | https://                                                                            |
| frozendict                       | Orion Floes                                                                         | https://                                                                            |
| frozenlist                       | https://github.com/aio-libs/frozenlist                                              | https://                                                                            |
| fsmlite                          | https://github.com/tkem/fsmlite                                                     | https://                                                                            |
| fsspec                           | https://github.com/fsspec/filesystem_spec                                           | https://                                                                            |
| funcy                            | https://github.com/Suor/funcy                                                       | https://                                                                            |
| gast                             | https://github.com/serge-sans-paille/gast/                                          | https://                                                                            |
| gau2grid                         | https://github.com/dgasmith/gau2grid                                                | https://                                                                            |
| gax-go                           | https://github.com/googleapis/gax-go/v2                                             | https://                                                                            |
| gdk-pixbuf                       | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https://                                                                            |
| gemmi                            | https://gemmi.readthedocs.io/en/latest/                                             | https://                                                                            |
| genproto                         | https://google.golang.org/genproto/googleapis                                       | https://                                                                            |
| geometric                        | https://openbase.com/python/geometric                                               | https://                                                                            |
| giflib                           | https://giflib.sourceforge.net                                                      | https://                                                                            |
| glib                             | https://docs.gtk.org/glib/                                                          | https://                                                                            |
| GLM Library                      | https://github.com/g-truc/glm                                                       | https://                                                                            |
| gls                              | https://github.com/jtolds/gls                                                       | https://                                                                            |
| go-cleanhttp                     | https://github.com/hashicorp/go-cleanhttp                                           | https://                                                                            |
| go-connections                   | https://github.com/docker/go-connections                                            | https://                                                                            |
| go-cpio                          | https://github.com/cavaliercoder/go-cpio                                            | https://                                                                            |
| go-getter                        | https://github.com/hashicorp/go-getter                                              | https://                                                                            |
| go-homedir                       | https://github.com/mitchellh/go-homedir                                             | https://                                                                            |
| go-ini                           | https://github.com/go-ini/ini                                                       | https://                                                                            |
| go-jmespath                      | https://github.com/jmespath/go-jmespath                                             | https://                                                                            |
| go-junit-report                  | https://github.com/jstemmer/go-junit-report                                         | https://                                                                            |
| go-netrc                         | https://github.com/bgentry/go-netrc/netrc                                           | https://                                                                            |
| go-ole                           | https://github.com/go-ole/go-ole                                                    | https://                                                                            |
| go-pg                            | https://github.com/go-pg/pg                                                         | https://                                                                            |
| go-redis                         | https://github.com/go-redis/redis/v8                                                | https://                                                                            |
| go-rendezvous                    | https://github.com/dgryski/go-rendezvous                                            | https://                                                                            |
| go-safetemp                      | https://github.com/hashicorp/go-safetemp                                            | https://                                                                            |
| go-sysconf                       | https://github.com/tklauser/go-sysconf                                              | https://                                                                            |
| go-testing-interface             | https://github.com/mitchellh/go-testing-interface                                   | https://                                                                            |
| go-units                         | https://github.com/docker/go-units                                                  | https://                                                                            |
| go-version                       | https://github.com/hashicorp/go-version                                             | https://                                                                            |
| go-zglob                         | https://github.com/mattn/go-zglob                                                   | https://                                                                            |
| go.opencensus                    | https://go.opencensus.io                                                            | https://                                                                            |
| gobrake.v2                       | https://gopkg.in/airbrake/gobrake.v2                                                | https://                                                                            |
| goconvey                         | https://github.com/smartystreets/goconvey                                           | https://                                                                            |
| golden-layout                    | https://github.com/deepstreamIO/golden-layout                                       | https://                                                                            |
| google-auth                      | https://google-auth.readthedocs.io/en/master/                                       | https://                                                                            |
| google-auth-oauthlib             | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https://                                                                            |
| google-cloud-go                  | https://cloud.google.com/go                                                         | https://                                                                            |
| google-cloud-go/storage          | https://cloud.google.com/go/storage                                                 | https://                                                                            |
| google-pasta                     | https://github.com/google/pasta                                                     | https://                                                                            |
| google.golang.org/api            | https://google.golang.org/api                                                       | https://                                                                            |
| gopsutil                         | https://github.com/shirou/gopsutil                                                  | https://                                                                            |
| Name of Project                  | Website                                                                             | License                                                                             |
| gorilla websocket                | https://github.com/gorilla/websocket                                                | https:/                                                                             |
| graphite2                        | https://github.com/silnrsi/graphite                                                 | https:/                                                                             |
| graphviz                         | https://graphviz.org/                                                               | https:/                                                                             |
| greenlet                         | https://greenlet.readthedocs.io/en/latest/                                          | https:/                                                                             |
| groupcache                       | https://github.com/golang/groupcache                                                | https:/                                                                             |
| grpc                             | https://google.golang.org/grpc                                                      | https:/                                                                             |
| grpc-cpp                         | https://github.com/grpc/grpc                                                        | https:/                                                                             |
| grpcio                           | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/                                                                             |
| gtk2                             | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/                                                                             |
| gts                              | https://sourceforge.net/projects/gts/                                               | https:/                                                                             |
| h5py                             | https://www.h5py.org                                                                | https:/                                                                             |
| harfbuzz                         | https://github.com/harfbuzz/harfbuzz                                                | https:/                                                                             |
| hdbscan                          | https://hdbscan.readthedocs.io/en/latest/                                           | https:/                                                                             |
| hdf4                             | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/                                                                             |
| hdf5                             | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/                                                                             |
| he                               | https://github.com/mathiasbynens/he                                                 | https:/                                                                             |
| html-loader                      | https://github.com/webpack-contrib/html-loader                                      | https:/                                                                             |
| html5lib                         | https://github.com/html5lib/html5lib-python                                         | https:/                                                                             |
| htslib                           | https://www.htslib.org                                                              | https:/                                                                             |
| humanize                         | https://github.com/jmoiron/humanize                                                 | https:/                                                                             |
| icu                              | https://github.com/unicode-org/icu                                                  | https:/                                                                             |
| idna                             | https://github.com/kjd/idna                                                         | https:/                                                                             |
| imageio                          | https://github.com/imageio/imageio                                                  | https:/                                                                             |
| imagesize                        | https://github.com/shibukawa/imagesize_py                                           | https:/                                                                             |
| ImmuneBuilder                    | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/                                                                             |
| importlib-metadata               | https://github.com/python/importlib_metadata                                        | https:/                                                                             |
| importlib_resources              | https://github.com/python/importlib_resources                                       | https:/                                                                             |
| InChI                            | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/                                                                             |
| inflection                       | https://github.com/jinzhu/inflection                                                | https:/                                                                             |
| ini.v1                           | https://gopkg.in/ini.v1                                                             | https:/                                                                             |
| iniconfig                        | https://github.com/pytest-dev/iniconfig                                             | https:/                                                                             |
| innersvg-polyfill                | https://github.com/dnozay/innersvg-polyfill                                         | https:/                                                                             |
| intel-openmp                     | https://github.com/hermitcore/libomp_oss                                            | https:/                                                                             |
| ipykernel                        | https://ipython.org                                                                 | https:/                                                                             |
| ipython                          | https://ipython.org                                                                 | https:/                                                                             |
| ipython-genutils                 | http://ipython.org                                                                  | https:/                                                                             |
| ipywidgets                       | http://jupyter.org                                                                  |                                                                                     |
| isodate                          | https://github.com/gweis/isodate/                                                   | https:/                                                                             |
| itsdangerous                     | https://palletsprojects.com/p/itsdangerous/                                         | https:/                                                                             |
| jax                              | https://github.com/google/jax                                                       | https:/                                                                             |
| jaxlib                           | https://github.com/google/jax                                                       | https:/                                                                             |
| jedi                             | https://jedi.readthedocs.io/en/latest/                                              | https:/                                                                             |
| Jinja2                           | https://palletsprojects.com/p/jinja/                                                | https:/                                                                             |
| jmespath                         | https://github.com/jmespath/jmespath.py                                             | https:/                                                                             |
| joblib                           | https://joblib.readthedocs.io/en/latest/                                            | https:/                                                                             |
| jpeg                             | https://www.ijg.org                                                                 | https:/                                                                             |
| json5                            | https://github.com/dpranke/pyjson5                                                  | https:/                                                                             |
| jsonfield                        | https://github.com/dmkoch/django-jsonfield/                                         | https:/                                                                             |
| jsonpatch                        | https://github.com/stefankoegl/python-json-patch                                    | https:/                                                                             |
| Name of Project                  | Website                                                                             | License                                                                             |
| jsonpickle                       | https://github.com/jsonpickle/jsonpickle                                            | https://github.com/jsonpickle/jsonpickle                                            |
| jsonpointer                      | https://github.com/stefankoegl/python-json-pointer                                  | https://github.com/stefankoegl/python-json-pointer                                  |
| jsonschema                       | https://github.com/python-jsonschema/jsonschema                                     | https://github.com/python-jsonschema/jsonschema                                     |
| jsonschema-specifications        | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst |
| jstat                            | https://github.com/jstat/jstat                                                      | https://github.com/jstat/jstat                                                      |
| jupyter-client                   | https://jupyter.org                                                                 | https://jupyter.org                                                                 |
| jupyter-core                     | https://jupyter.org                                                                 | https://jupyter.org                                                                 |
| jupyter-events                   | https://github.com/jupyter/jupyter_events                                           | https://github.com/jupyter/jupyter_events                                           |
| jupyter-lsp                      | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https://github.com/jupyter-lsp/jupyterlab-lsp                                       |
| jupyter-serverhttp://jupyter.org | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE                  |                                                                                     |
| jupyterlab                       | https://github.com/jupyterlab/jupyterlab                                            | https://github.com/jupyterlab/jupyterlab                                            |
| jupyterlab-pygments              | http://jupyter.org                                                                  | http://jupyter.org                                                                  |
| jupyterlab-widgets               | http://jupyter.org                                                                  | http://jupyter.org                                                                  |
| jupyterlab_server                | https://github.com/jupyterlab/jupyterlab_server                                     | https://github.com/jupyterlab/jupyterlab_server                                     |
| jupyter_client                   | http://jupyter.org                                                                  | http://jupyter.org                                                                  |
| jupyter_core                     | http://jupyter.org                                                                  | http://jupyter.org                                                                  |
| jupyter_server                   | https://github.com/jupyter-server/jupyter_server                                    | https://github.com/jupyter-server/jupyter_server                                    |
| jupyter_server_terminals         | https://github.com/jupyter-server/jupyter_server_terminals                          | https://github.com/jupyter-server/jupyter_server_terminals                          |
| kaleido                          | https://github.com/plotly/Kaleido                                                   | https://github.com/plotly/Kaleido                                                   |
| keras                            | https://github.com/keras-team/keras                                                 | https://github.com/keras-team/keras                                                 |
| Keras-Preprocessing              | https://github.com/keras-team/keras-preprocessing                                   | https://github.com/keras-team/keras-preprocessing                                   |
| keras-tuner                      | https://github.com/keras-team/keras-tuner                                           | https://github.com/keras-team/keras-tuner                                           |
| keyring                          | https://github.com/jaraco/keyring                                                   | https://github.com/jaraco/keyring                                                   |
| keyutils                         | https://github.com/sassoftware/python-keyutils                                      | https://github.com/sassoftware/python-keyutils                                      |
| kiwisolver                       | https://kiwisolver.readthedocs.io/en/latest/                                        | https://kiwisolver.readthedocs.io/en/latest/                                        |
| kombu                            | https://kombu.readthedocs.io                                                        | https://kombu.readthedocs.io                                                        |
| $\overline{\text{krb5}}$         | https://web.mit.edu/kerberos/                                                       | https://web.mit.edu/kerberos/                                                       |
| kt-legacy                        | https://github.com/haifeng-jin/kt-legacy                                            | https://github.com/haifeng-jin/kt-legacy                                            |
| lazy_loader                      | https://github.com/scientific-python/lazy_loader                                    | https://github.com/scientific-python/lazy_loader                                    |
| lcms2                            | https://www.littlecms.com                                                           | https://www.littlecms.com                                                           |
| lerc                             | https://github.com/Esri/lerc                                                        | https://github.com/Esri/lerc                                                        |
| libarchive                       | http://www.libarchive.org                                                           | http://www.libarchive.org                                                           |
| libblas                          | https://www.netlib.org/blas/                                                        | https://www.netlib.org/blas/                                                        |
| libbrotlicommon                  | https://github.com/google/brotli                                                    | https://github.com/google/brotli                                                    |
| libbrotlidec                     | https://github.com/google/brotli                                                    | https://github.com/google/brotli                                                    |
| libbrotlienc                     | https://github.com/google/brotli                                                    | https://github.com/google/brotli                                                    |
| libcblas                         | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                                 |
| libclang                         | Orion Floes                                                                         |                                                                                     |
| libcurl                          | https://curl.se/libcurl/                                                            | https://curl.se/libcurl/                                                            |
| libcxx                           | https://github.com/llvm-mirror/libcxx                                               | https://github.com/llvm-mirror/libcxx                                               |
| libdb                            | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https://www.oracle.com/technology/software/products/berkeley-db/index.html          |
| libdeflate                       | https://github.com/ebiggers/libdeflate                                              | https://github.com/ebiggers/libdeflate                                              |
| libedit                          | https://thrysoee.dk/editline/                                                       | https://thrysoee.dk/editline/                                                       |
| libev                            | https://software.schmorp.de/pkg/libev.html                                          | https://software.schmorp.de/pkg/libev.html                                          |
| libffi                           | https://github.com/libffi/libffi                                                    | https://github.com/libffi/libffi                                                    |
| libgcrypt                        | https://gnupg.org/software/index.html                                               | https://gnupg.org/software/index.html                                               |
| libgd                            | https://libgd.github.io                                                             | https://libgd.github.io                                                             |
| libglib                          | https://github.com/PolMine/libglib                                                  | https://github.com/PolMine/libglib                                                  |
| libiconv                         | https://www.gnu.org/software/libiconv/                                              | https://www.gnu.org/software/libiconv/                                              |
| Name of Project                  | Website                                                                             | License                                                                             |
| libint                           | https://tinyurl.com/yvw97wbw                                                        | https                                                                               |
| liblapack                        | http://www.netlib.org/lapack/                                                       | https                                                                               |
| liblapacke                       | https://anaconda.org/conda-forge/liblapacke                                         | https                                                                               |
| libmamba                         | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https                                                                               |
| libmambapy                       | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https                                                                               |
| libnetcdf                        | https://www.unidata.ucar.edu/software/netcdf/                                       | https                                                                               |
| libnghttp2                       | https://github.com/nghttp2/nghttp2                                                  | https                                                                               |
| libopenblas                      | https://www.openblas.net/                                                           | https                                                                               |
| libpng                           | https://www.libpng.org/pub/png/libpng.html                                          | https                                                                               |
| libpq                            | https://www.postgresql.org/                                                         | https                                                                               |
| librsvg                          | https://gitlab.gnome.org/GNOME/librsvg                                              | https                                                                               |
| libsolv                          | https://github.com/openSUSE/libsolv                                                 | https                                                                               |
| libssh2                          | https://github.com/libssh2/libssh2                                                  | https                                                                               |
| libtiff                          | https://www.libtiff.org/                                                            | https                                                                               |
| libtrust                         | https://github.com/docker/libtrust                                                  | https                                                                               |
| libuuid                          | https://sourceforge.net/projects/libuuid/                                           | https                                                                               |
| libuv                            | https://github.com/libuv/libuv                                                      | https                                                                               |
| libwebp                          | https://chromium.googlesource.com/?format=HTML                                      | https                                                                               |
| libwebp-base                     | https://chromium.googlesource.com/?format=HTML                                      | https                                                                               |
| libxc                            | https://www.tddft.org/programs/libxc/                                               | https                                                                               |
| libxcb                           | https://xcb.freedesktop.org                                                         | https                                                                               |
| libxml2                          | https://git.gnome.org/browse/libxml2/                                               | https                                                                               |
| libxmlsec1                       | https://github.com/lsh123/xmlsec                                                    | https                                                                               |
| libxslt                          | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https                                                                               |
| zlib                             | https://zlib.net                                                                    | https                                                                               |
| lime                             | https://github.com/marcotcr/lime                                                    | https                                                                               |
| llvm                             | http://llvm.org                                                                     | https                                                                               |
| llvm-openmp                      | https://github.com/llvm-mirror/openmp                                               | https                                                                               |
| llvmlite                         | http://llvmlite.readthedocs.io                                                      | https                                                                               |
| loader-utils                     | https://github.com/webpack/loader-utils                                             | https                                                                               |
| logomaker                        | https://logomaker.readthedocs.io/en/latest/                                         | https                                                                               |
| logrus                           | https://github.com/sirupsen/logrus                                                  | https                                                                               |
| logrus-airbrake-hook.v2          | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https                                                                               |
| lxml                             | https://lxml.de                                                                     | https                                                                               |
| lz4-c                            | https://www.lz4.org/                                                                | https                                                                               |
| markdown                         | https://github.com/evilstreak/markdown-js                                           | https                                                                               |
| markdown-it-py                   | Orion Floes                                                                         | https                                                                               |
| MarkupSafe                       | https://palletsprojects.com/p/markupsafe/                                           | https                                                                               |
| matplotlib                       | https://matplotlib.org                                                              | https                                                                               |
| matplotlib-base                  | https://matplotlib.org                                                              | https                                                                               |
| matplotlib-inline                | https://github.com/ipython/matplotlib-inline                                        | https                                                                               |
| mda-xdrlib                       | https://github.com/MDAnalysis/mda-xdrlib                                            | https                                                                               |
| mdtraj                           | https://www.mdtraj.org/                                                             | https                                                                               |
| mdurl                            | Orion Floes                                                                         | https                                                                               |
| menuinst                         | Orion Floes                                                                         | https                                                                               |
| mergo                            | https://github.com/imdario/mergo                                                    | https                                                                               |
| mistune                          | https://github.com/lepture/mistune                                                  | https                                                                               |
| mkl                              | https://github.com/rust-math/intel-mkl-src                                          | https                                                                               |
| mkl-fft                          | https://github.com/IntelPython/mkl_fft                                              | https                                                                               |
| Name of Project                  | Website                                                                             | License                                                                             |
| mkl-random                       | https://github.com/IntelPython/mkl_random                                           | https://                                                                            |
| mkl-service                      | https://github.com/IntelPython/mkl-service                                          | https://                                                                            |
| ml-dtypes                        | <b>Orion Floes</b>                                                                  | https://                                                                            |
| molecupy                         | https://molecupy.readthedocs.io/en/latest/                                          | https://                                                                            |
| moment                           | https://github.com/moment/moment                                                    | https://                                                                            |
| moment-precise-range-plugin      | https://github.com/codebox/moment-precise-range                                     | https://                                                                            |
| more-itertools                   | https://github.com/more-itertools/more-itertools                                    | https://                                                                            |
| mpiplus                          | https://github.com/choderalab/mpiplus                                               | https://                                                                            |
| mpmath                           | http://mpmath.org/                                                                  | https://                                                                            |
| mrcfile                          | https://github.com/ccpem/mrcfile                                                    | https://                                                                            |
| msgpack                          | https://msgpack.org/                                                                | https://                                                                            |
| multidict                        | https://github.com/aio-libs/multidict                                               | https://                                                                            |
| multierr                         | https://go.uber.org/multierr                                                        | https://                                                                            |
| multiprocess                     | https://github.com/uqfoundation/multiprocess                                        | https://                                                                            |
| munkres                          | https://software.clapper.org/munkres/                                               | https://                                                                            |
| myesui uuid                      | https://github.com/myesui/uuid                                                      | https://                                                                            |
| namex                            | <b>Orion Floes</b>                                                                  | https://                                                                            |
| nbclassic                        | http://jupyter.org                                                                  | https://                                                                            |
| nbclient                         | https://jupyter.org                                                                 | https://                                                                            |
| nbconvert                        | https://jupyter.org                                                                 | https://                                                                            |
| nbformat                         | http://jupyter.org                                                                  | https://                                                                            |
| ncurses                          | https://invisible-island.net/ncurses/                                               | https://                                                                            |
| nest-asyncio                     | https://github.com/erdewit/nest_asyncio                                             | https://                                                                            |
| netcdf-fortran                   | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                                            |
| netCDF4                          | http://github.com/Unidata/netcdf4-python                                            | https://                                                                            |
| nettle                           | https://git.lysator.liu.se/nettle/nettle                                            | https://                                                                            |
| networkx                         | https://networkx.org                                                                | https://                                                                            |
| nfpm                             | https://github.com/goreleaser/nfpm                                                  | https://                                                                            |
| ng-tags-input                    | https://github.com/mbenford/ngTagsInput                                             | https://                                                                            |
| ng-toast                         | https://github.com/tameraydin/ngToast                                               | https://                                                                            |
| ngdraggable                      | https://github.com/fatlinesofcode/ngDraggable                                       | https://                                                                            |
| ngVue                            | https://github.com/ngVue/ngVue                                                      | https://                                                                            |
| nlopt                            | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https://                                                                            |
| nodejs                           | https://nodejs.org/en/                                                              | https://                                                                            |
| nomkl                            | https://github.com/conda-forge/nomkl-feedstock                                      | https://                                                                            |
| notebook                         | http://jupyter.org                                                                  | https://                                                                            |
| notebook-shim                    | https://github.com/jupyter/notebook_shim                                            | https://                                                                            |
| notebook_shim                    | http://jupyter.org                                                                  | https://                                                                            |
| numba                            | https://numba.pydata.org                                                            | https://                                                                            |
| numcpus                          | https://github.com/tklauser/numcpus                                                 | https://                                                                            |
| numexpr                          | https://github.com/pydata/numexpr                                                   | https://                                                                            |
| numpy                            | https://numpy.org                                                                   | https://                                                                            |
| numpy-base                       | https://numpy.org                                                                   | https://                                                                            |
| numpydoc                         | https://numpydoc.readthedocs.io/en/latest/index.html                                | https://                                                                            |
| nvidia-cublas-cu11               | https://developer.nvidia.com/cuda-zone                                              | https://                                                                            |
| nvidia-cublas-cu12               | https://developer.nvidia.com/cuda-zone                                              | https://                                                                            |
| nvidia-cuda-cupti-cu11           | https://developer.nvidia.com/cuda-zone                                              | https://                                                                            |
| nvidia-cuda-cupti-cu12           | https://developer.nvidia.com/cuda-zone                                              | https://                                                                            |
| nvidia-cuda-nvrtc-cu11           | https://developer.nvidia.com/cuda-zone                                              | https://                                                                            |

| Name of Project          | Website                                                 |
|--------------------------|---------------------------------------------------------|
| nvidia-cuda-nvrtc-cu12   | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cuda-runtime-cu11 | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cuda-runtime-cu12 | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cudnn-cu11        | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cudnn-cu12        | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cufft-cu11        | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cufft-cu12        | https://developer.nvidia.com/cuda-zone                  |
| nvidia-curand-cu11       | https://developer.nvidia.com/cuda-zone                  |
| nvidia-curand-cu12       | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cusolver-cu11     | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cusolver-cu12     | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cusparse-cu11     | https://developer.nvidia.com/cuda-zone                  |
| nvidia-cusparse-cu12     | https://developer.nvidia.com/cuda-zone                  |
| nvidia-nccl-cu11         | https://developer.nvidia.com/cuda-zone                  |
| nvidia-nccl-cu12         | https://developer.nvidia.com/cuda-zone                  |
| nvidia-nvjitlink-cu12    | https://developer.nvidia.com/cuda-zone                  |
| nvidia-nvtx-cu11         | https://developer.nvidia.com/cuda-zone                  |
| nvidia-nvtx-cu12         | https://developer.nvidia.com/cuda-zone                  |
| Oat++                    | https://oatpp.io/                                       |
| oauthlib                 | https://github.com/oauthlib/oauthlib                    |
| ocl-icd                  | https://github.com/OCL-dev/ocl-icd                      |
| ocl-icd-system           | https://github.com/conda-forge/ocl-icd-system-feedstock |
| olefile                  | https://www.decalage.info/python/olefileio              |
| OmegaFold                | https://github.com/HeliXonProtein/OmegaFold/tree/main   |
| omnicanvas               | https://omnicanvas.readthedocs.io/en/latest/            |
| OpenFF                   | https://openforcefield.org/                             |
| openff-amber-ff-ports    | https://github.com/openforcefield/openff-amber-ff-ports |
| openff-forcefields       | https://openforcefield.org                              |
| openff-interchange       | https://github.com/openforcefield/openff-interchange    |
| openff-models            | https://github.com/openforcefield/openff-models         |
| openff-toolkit           | https://openforcefield.org                              |
| openff-toolkit-base      | https://openforcefield.org                              |
| openff-units             | https://github.com/openforcefield/openff-units          |
| openff-utilities         | https://github.com/openforcefield/openff-utilities      |
| openjpeg                 | https://github.com/uclouvain/openjpeg                   |
| openldap                 | https://www.openldap.org/software/repo.html             |
| OpenMM                   | https://openmm.org                                      |
| openmmtools              | https://github.com/choderalab/openmmtools               |
| openmoltools             | https://github.com/choderalab/openmoltools              |
| openpyxl                 | https://openpyxl.readthedocs.io/en/stable/              |
| openssl                  | https://www.openssl.org                                 |
| opt-einsum               | https://github.com/dgasmith/opt_einsum                  |
| OptKing                  | https://github.com/psi-rking/optking                    |
| oscrypto                 | https://github.com/wbond/oscrypto                       |
| overrides                | https://github.com/mkorpela/overrides                   |
| packaging                | https://github.com/pypa/packaging                       |
| packmol                  | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml   |
| pandas                   | https://pandas.pydata.org                               |
| pandocfilters            | http://github.com/jgm/pandocfilters                     |

| Name of Project               | Website                                                          | License             |
|-------------------------------|------------------------------------------------------------------|---------------------|
| panedr                        | https://github.com/MDAnalysis/panedr                             | https://            |
| pango                         | https://pango.gnome.org                                          | https://            |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                  | https://            |
| parser                        | https://github.com/typescript-eslint/typescript-eslint           | https://            |
| parso                         | https://parso.readthedocs.io/en/latest/                          | https://            |
| pathos                        | https://github.com/uqfoundation/pathos                           | https://            |
| patsy                         | https://patsy.readthedocs.io/en/latest/                          | https://            |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                               | https://            |
| pbr                           | https://docs.openstack.org/pbr/latest/                           | https://            |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                      | https://            |
| pcre                          | https://www.pcre.org                                             | https://            |
| pcre2                         | https://www.pcre.org                                             | https://            |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                            | https://            |
| pdbfixer                      | https://github.com/openmm/pdbfixer                               | https://            |
| pexpect                       | https://pexpect.readthedocs.io/                                  | https://            |
| pgconn                        | https://github.com/jackc/pgconn                                  | https://            |
| pgio                          | https://github.com/jackc/pgio                                    | https://            |
| pgpassfile                    | https://github.com/jackc/pgpassfile                              | https://            |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                             | https://            |
| pgtype                        | https://github.com/jackc/pgtype                                  | https://            |
| pgx                           | https://github.com/jackc/pgx/v4                                  | https://            |
| phonopy                       | https://github.com/phonopy/phono3py                              | https://            |
| pickleshare                   | https://github.com/pickleshare/pickleshare                       | https://            |
| Pillow                        | https://python-pillow.org                                        | https://            |
| Pint                          | https://pint.readthedocs.io/en/stable/                           | https://            |
| pip                           | https://pip.pypa.io/                                             | https://            |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                         | https://            |
| pixman                        | https://pixman.org                                               | https://            |
| pkginfo                       | https://launchpad.net/pkginfo                                    | https://            |
| platformdirs                  | https://github.com/platformdirs/platformdirs                     | https://            |
| plotly                        | https://plotly.com/python/                                       | https://            |
| plotly-orca                   | https://github.com/plotly/orca                                   | https://            |
| plotly.js                     | https://github.com/plotly/plotly.js                              | https://            |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html               | https://            |
| pooch                         | https://github.com/fatiando/pooch                                | https://            |
| pox                           | https://github.com/uqfoundation/pox                              | https://            |
| ppft                          | https://github.com/uqfoundation/ppft                             | https://            |
| pq                            | https://github.com/lib/pq                                        | https://            |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                    | https://            |
| prometheus-client             | https://github.com/prometheus/client_python                      | https://            |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/          | https://            |
| protobuf                      | https://google.golang.org/protobuf                               | https://            |
| psi4                          | https://psicode.org                                              | https://            |
| psutil                        | https://psutil.readthedocs.io/en/latest/                         | https://            |
| psycopg2                      | https://psycopg.org/                                             | https://            |
| PTable                        | https://github.com/kxxoling/PTable                               | https://            |
| pthread-stubs                 | https://xcb.freedesktop.org                                      | https://            |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                     | https://            |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                           | http://             |
| Name of Project               | Website                                                          | License             |
| py                            | https://py.readthedocs.io/en/latest/                             | https://            |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                          | https://            |
| pyasn1                        | https://github.com/etingof/pyasn1                                | https://            |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                        | https://            |
| pybind11-abi                  | https://github.com/pybind/pybind11                               | https://            |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html              | https://            |
| pycosat                       | https://github.com/conda/pycosat                                 | https://            |
| pycparser                     | https://github.com/eliben/pycparser                              | https://            |
| pydantic                      | https://pydantic-docs.helpmanual.io                              | https://            |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                        | https://            |
| pyedr                         | https://github.com/MDAnalysis/panedr                             | https://            |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                             | https://            |
| Pygments                      | https://pygments.org                                             | https://            |
| pygraphviz                    | https://pygraphviz.github.io                                     | https://            |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                         | https://            |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                     | https://            |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator               | https://            |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                | https://            |
| pymbar                        | https://pymbar.org                                               | https://            |
| pyOpenSSL                     | https://pyopenssl.org/                                           | https://            |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                 | https://            |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                 | https://            |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                              | https://            |
| pysam                         | https://github.com/pysam-developers/pysam                        | https://            |
| PySocks                       | https://github.com/Anorov/PySocks                                | https://            |
| pytables                      | https://www.pytables.org                                         | https://            |
| python                        | https://www.python.org/                                          | https://            |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                       | https://            |
| python-constraint             | https://github.com/python-constraint/python-constraint           | https://            |
| python-dateutil               | https://dateutil.readthedocs.io                                  | https://            |
| python-json-logger            | http://github.com/madzak/python-json-logger                      | https://            |
| python-ldap                   | https://www.python-ldap.org/                                     | https://            |
| python3-saml                  | https://github.com/onelogin/python3-saml                         | https://            |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock              | https://            |
| pytz                          | https://pythonhosted.org/pytz                                    | https://            |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                | https://            |
| PyWavelets                    | https://github.com/PyWavelets/pywt                               | https://            |
| <b>PyYAML</b>                 | https://pyyaml.org/                                              | https://            |
| pyyml                         | No longer available                                              | No longer available |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                          | https://            |
| qcelemental                   | https://github.com/MolSSI/QCElemental                            | https://            |
| qcengine                      | https://github.com/MolSSI/QCEngine                               | https://            |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                     | https://            |
| ramda                         | https://github.com/ramda/ramda                                   | https://            |
| rapidjson                     | https://rapidjson.org/                                           | https://            |
| rdkit                         | https://www.rdkit.org                                            | https://            |
| re2                           | https://github.com/google/re2                                    | https://            |
| readme-renderer               | https://github.com/pypa/readme_renderer                          | https://            |
| redis-py                      | https://github.com/andymccurdy/redis-py                          | https://            |
| Name of Project               | Website                                                          | License             |
| referencing                   | https://github.com/python-jsonschema/referencing                 | https://            |
| regex                         | https://github.com/mrabarnett/mrab-regex                         | https://            |
| reportlab                     | https://www.reportlab.com                                        | https://            |
| reproc                        | https://github.com/DaanDeMeyer/reproc                            | https://            |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                            | https://            |
| requests                      | https://requests.readthedocs.io                                  | https://            |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                    | https://            |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                 | https://            |
| resumable                     | https://github.com/stevvooe/resumable                            | https://            |
| retrying                      | https://github.com/rholder/retrying                              | https://            |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                    | https://            |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                        | https://            |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                    | https://            |
| rich                          | Orion Floes                                                      | https://            |
| rpds-py                       | https://github.com/crate-py/rpds                                 | https://            |
| rpmpack                       | https://github.com/google/rpmpack                                | https://            |
| rsa                           | https://stuvel.eu/rsa                                            | https://            |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/      | https://            |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/ | https://            |
| s3transfer                    | https://github.com/boto/s3transfer                               | https://            |
| sasl                          | https://mellium.im/sasl                                          | https://            |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                        | https://            |
| scikit-image                  | https://scikit-image.org                                         | https://            |
| scikit-learn                  | https://scikit-learn.org/stable/                                 | https://            |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra       | https://            |
| scipy                         | https://scipy.org                                                | https://            |
| seaborn                       | https://seaborn.pydata.org                                       | https://            |
| seaborn-base                  | https://seaborn.pydata.org                                       | https://            |
| semver                        | https://github.com/Masterminds/semver/v3                         | https://            |
| Send2Trash                    | https://github.com/arsenetar/send2trash                          | https://            |
| setuptools                    | https://github.com/pypa/setuptools                               | https://            |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                          | https://            |
| sh                            | https://github.com/amoffat/sh                                    | https://            |
| shellingham                   | https://github.com/sarugaku/shellingham                          | https://            |
| simint                        | https://www.bennyp.org/research/simint/                          | https://            |
| six                           | https://github.com/benjaminp/six                                 | https://            |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst               | https://            |
| snappy                        | https://github.com/google/snappy                                 | https://            |
| sniffio                       | https://github.com/python-trio/sniffio                           | https://            |
| snowballstemmer               | https://github.com/snowballstem/snowball                         | https://            |
| soupsieve                     | https://github.com/facelessuser/soupsieve                        | https://            |
| spglib                        | Orion Floes                                                      | https://            |
| sphinx                        | https://github.com/sphinx-doc/sphinx                             | https://            |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp            | https://            |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp              | https://            |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp             | https://            |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath               | https://            |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp               | https://            |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml      | https://            |
| Name of Project               | Website                                                          | License             |
| SQLAlchemy                    | https://www.sqlalchemy.org                                       | https:/             |
| sqlite                        | https://sqlite.org/index.html                                    | https:/             |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                         | https:/             |
| stack-data                    | http://github.com/alexmojaki/stack_data                          | https:/             |
| starfile                      | https://github.com/alisterburt/starfile                          | https:/             |
| statsmodels                   | https://github.com/statsmodels/statsmodels                       | https:/             |
| structlog                     | https://www.structlog.org/                                       | https:/             |
| svglib                        | https://github.com/deeplook/svglib                               | https:/             |
| sympy                         | https://sympy.org                                                | https:/             |
| tables                        | https://www.pytables.org/                                        | https:/             |
| tabulate                      | https://github.com/astanin/python-tabulate                       | https:/             |
| tbb                           | https://github.com/oneapi-src/oneTBB                             | https:/             |
| tenacity                      | https://github.com/jd/tenacity                                   | https:/             |
| tensorboard                   | https://github.com/tensorflow/tensorboard                        | https:/             |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                        | https:/             |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                        | https:/             |
| tensorflow                    | https://github.com/tensorflow/tensorflow                         | https:/             |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                          | https:/             |
| tensorflow-io-gcs-filesystem  | <b>Orion Floes</b>                                               | https:/             |
| tensorflow-probability        | https://github.com/tensorflow/probability                        | https:/             |
| termcolor                     | https://github.com/hugovk/termcolor                              | https:/             |
| terminado                     | https://github.com/jupyter/terminado                             | https:/             |
| testpath                      | https://github.com/jupyter/testpath                              | https:/             |
| textangular                   | https://github.com/fraywing/textAngular                          | https:/             |
| tf_keras                      | <b>Orion Floes</b>                                               | https:/             |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                          | https:/             |
| three                         | https://github.com/mrdoob/three.js                               | https:/             |
| tifffile                      | https://github.com/cgohlke/tifffile/                             | https:/             |
| tinycss2                      | https://github.com/Kozea/tinycss2/                               | https:/             |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                          | https:/             |
| tk                            | https://www.tcl.tk/                                              | https:/             |
| toml                          | https://github.com/toml-lang/toml                                | https:/             |
| tomli                         | https://github.com/hukkin/tomli                                  | https:/             |
| toolz                         | https://github.com/pytoolz/toolz                                 | https:/             |
| torch                         | https://pytorch.org/                                             | https:/             |
| tornado                       | https://www.tornadoweb.org                                       | https:/             |
| tqdm                          | https://github.com/tqdm/tqdm                                     | https:/             |
| tracy                         | https://github.com/gear-genomics/tracy                           | https:/             |
| traitlets                     | https://github.com/ipython/traitlets                             | https:/             |
| triton                        | https://github.com/openai/triton/                                | https:/             |
| truststore                    | <b>Orion Floes</b>                                               | https:/             |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                            | https:/             |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                          | https:/             |
| twine                         | https://github.com/pypa/twine                                    | https:/             |
| twinj uuid                    | https://github.com/twinj/uuid                                    | https:/             |
| types                         | https://github.com/babel/babel                                   | https:/             |
| typescript                    | https://github.com/Microsoft/TypeScript                          | https:/             |
| typing_extensions             | https://github.com/python/typing                                 | https:/             |
| tzdata                        | https://github.com/python/tzdata                                 | https:/             |

| Name of Project    | Website                                                  | License    |
|--------------------|----------------------------------------------------------|------------|
| tzlocal            | https://github.com/regebro/tzlocal                       | https:/    |
| umi-tools          | https://github.com/CGATOxford/UMI-tools                  | https:/    |
| unicodedata2       | https://github.com/fonttools/unicodedata2                | https:/    |
| uritools           | https://github.com/tkem/uritools/                        | https:/    |
| urllib3            | https://urllib3.readthedocs.io/                          | https:/    |
| vine               | https://github.com/celery/vine                           | https:/    |
| vue                | https://github.com/vuejs/vue                             | https:/    |
| wcwidth            | https://github.com/jquast/wcwidth                        | https:/    |
| webencodings       | https://github.com/gsnedders/python-webencodings         | https:/    |
| websocket-client   | https://github.com/websocket-client/websocket-client.git | https:/    |
| Werkzeug           | https://palletsprojects.com/p/werkzeug/                  | https:/    |
| westpa             | Orion Floes                                              | http://    |
| wheel              | https://github.com/pypa/wheel                            | https:/    |
| widgetsnbextension | https://github.com/jupyter-widgets/ipywidgets#readme     | https:/    |
| wrapt              | https://github.com/GrahamDumpleton/wrapt                 | https:/    |
| wsutil             | https://github.com/yhat/wsutil                           | https:/    |
| x/lint             | https://golang.org/x/lint                                | https:/    |
| x/mod              | https://golang.org/x/mod/semver                          | https:/    |
| x/net              | https://golang.org/x/net                                 | https:/    |
| x/oauth2           | https://golang.org/x/oauth2                              | https:/    |
| x/sys              | https://golang.org/x/sys                                 | https:/    |
| x/text             | https://golang.org/x/text                                | https:/    |
| x/tools            | https://golang.org/x/tools                               | https:/    |
| x/errors           | https://golang.org/x/xerrors                             | https:/    |
| xhtml2pdf          | https://github.com/xhtml2pdf/xhtml2pdf                   | https:/    |
| xlrd               | https://github.com/python-excel/xlrd                     | https:/    |
| xmlsec             | https://github.com/mehcode/python-xmlsec                 | https:/    |
| xmltodict          | https://github.com/martinblech/xmltodict                 | https:/    |
| xorg-kbproto       | https://gitlab.freedesktop.org/xorg/proto/kbproto        | https:/    |
| xorg-libice        | https://gitlab.freedesktop.org/xorg/lib/libice           | https:/    |
| xorg-libsm         | https://gitlab.freedesktop.org/xorg/lib/libsm            | https:/    |
| xorg-libx11        | https://gitlab.freedesktop.org/xorg/lib/libx11           | https:/    |
| xorg-libxau        | https://gitlab.freedesktop.org/xorg/lib/libxau           | https:/    |
| xorg-libxdmcp      | https://gitlab.freedesktop.org/xorg/lib/libxdmcp         | https:/    |
| xorg-libxext       | https://gitlab.freedesktop.org/xorg/lib/libxext          | https:/    |
| xorg-libxrender    | https://gitlab.freedesktop.org/xorg/lib/libxrender       | https:/    |
| xorg-libxt         | https://gitlab.freedesktop.org/xorg/lib/libxt            | https:/    |
| xorg-renderproto   | https://gitlab.freedesktop.org/xorg/proto/renderproto    | https:/    |
| xorg-xextproto     | https://gitlab.freedesktop.org/xorg/proto/xextproto      | https:/    |
| xorg-xproto        | https://gitlab.freedesktop.org/xorg/proto/xproto         | https:/    |
| xxhash             | https://github.com/cespare/xxhash/v2                     | https:/    |
| xz                 | https://github.com/ulikunitz/xz                          | https:/    |
| yaml               | https://pyyaml.org/                                      | https:/    |
| yaml-cpp           | https://github.com/jbeder/yaml-cpp                       | https:/    |
| yaml.v2            | https://gopkg.in/yaml.v2                                 | https:/    |
| yaml.v3            | https://gopkg.in/yaml.v3                                 | https:/    |
| yarl               | https://github.com/aio-libs/yarl/                        | https:/    |
| yaspin             | https://github.com/pavdmyt/yaspin                        | https:/    |
| yfiles             | https://www.yworks.com/products/yfiles                   | Commercial |
| Name of Project    | Website                                                  | License    |
| yml                | https://pypi.org/project/yml/                            | N/A        |
| zap                | https://go.uber.org/zap                                  |            |
| zipp               | https://github.com/jaraco/zipp                           |            |
| zlib               | https://zlib.net/                                        |            |
| zstandard          | https://github.com/indygreg/python-zstandard             |            |
| zstd               | https://facebook.github.io/zstd/                         |            |
| _libgcc_mutex      | https://github.com/conda-forge/_libgcc_mutex-feedstock   |            |
| _openmp_mutex      | https://github.com/conda-forge/_openmp_mutex-feedstock   |            |

## **10.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses GNU Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

## **10.1.1 GCC RUNTIME LIBRARY EXCEPTION**

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

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

License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. 14. Revised Versions of this License. The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. 15. Disclaimer of Warranty. THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 16. Limitation of Liability. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD

17. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided

PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF

(continues on next page)

SUCH DAMAGES.

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page)

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

#### See also:

• http://www.gnu.org/licenses/gpl.txt

## **INDEX**

## A

AddFP OEGraphSim:: OEFPDatabase, 65 AddSample OEGraphSim:: OEFPHistogram, 77 OEGraphSim:: OEFPVariogram, 86

## C

Dice

similarity measure, 13

ClearCutoff OEGraphSim:: OEFPDatabase, 65 OEGraphSim:: OEFPDatabaseOptions, 73 Constructor OEGraphSim:: OESimSearchResult, 89 Constructors OEGraphSim::OECreateFastFPDatabaseOption@EGraphSim::OEFPTypeParams, 83 51 OEGraphSim:: OEFastFPDatabase, 54 OEGraphSim:: OEFastFPDatabaseParams, 52 OEGraphSim:: OEFingerPrint, 63 OEGraphSim:: OEFPDatabase, 64 OEGraphSim:: OEFPDatabaseOptions, 72 OEGraphSim:: OEFPHistogram, 77 OEGraphSim:: OEFPPattern, 80 OEGraphSim:: OEFPTypeBase, 81 OEGraphSim:: OEFPTypeParams, 83 OEGraphSim:: OEFPVariogram, 86 OEGraphSim:: OESimFuncBase, 86 OEGraphSim:: OESimScore, 87 OEGraphSim:: OESimScorePair, 88 OEGraphSim:: OETanimotoSim, 90 OEGraphSim:: OETverskySim, 91 Cosine similarity measure, 12 CreateCopy OEGraphSim:: OESimFuncBase, 87 OEGraphSim:: OETanimotoSim, 91 OEGraphSim:: OETverskySim, 92 D

## F

Euclidean similarity measure, 13 Example Code makefastfp.py, 44 searchfastfp.py, 47 searchfp.py.40

## G

GetAllScores OEGraphSim:: OEFastFPDatabase, 55 GetAlpha OEGraphSim:: OETverskySim, 92 GetAtomTypes GetBeta OEGraphSim:: OETverskySim, 92 GetBinBoundaries OEGraphSim:: OEFPHistogram, 77 GetBinCenters OEGraphSim:: OEFPHistogram, 78 GetBinIdx OEGraphSim:: OEFPHistogram, 78 GetBinWidth OEGraphSim:: OEFPHistogram, 78 GetBit OEGraphSim:: OEFPPattern, 81 GetBondTypes OEGraphSim:: OEFPTypeParams, 84 GetCounts OEGraphSim:: OEFPHistogram, 78 GetCutoff OEGraphSim:: OEFPDatabase, 65 OEGraphSim:: OEFPDatabaseOptions, 73 GetDensity OEGraphSim:: OEFPHistogram, 78 GetDescendingOrder OEGraphSim:: OEFPDatabase, 65 OEGraphSim:: OEFPDatabaseOptions, 74 GetFingerPrint OEGraphSim:: OEFastFPDatabase, 56 GetFingerPrints

OEGraphSim:: OEFPDatabase, 66 GetFPType OEGraphSim::OECreateFastFPDatabaseOptdetnScores 51 OEGraphSim:: OEFPTypeBase, 81 OEGraphSim:: OEFPTypeParams, 84 GetFPTypeBase OEGraphSim:: OEFastFPDatabase, 56 OEGraphSim:: OEFastFPDatabaseParams, 53 OEGraphSim:: OEFingerPrint, 63 OEGraphSim:: OEFPDatabase, 66 GetFPTypeString OEGraphSim:: OEFPTypeBase, 82 GetFPVersion OEGraphSim:: OEFPTypeBase, 82 GetFPVersionString OEGraphSim:: OEFPTypeBase, 83 GetHistogram OEGraphSim:: OEFastFPDatabase, 56 GetIdx OEGraphSim:: OESimScore, 87 GetIdxA OEGraphSim:: OESimScorePair, 88 GetIdxB OEGraphSim:: OESimScorePair, 88 GetLimit OEGraphSim:: OEFPDatabaseOptions, 74 GetMax OEGraphSim:: OEFPHistogram, 79 GetMaxDistance OEGraphSim:: OEFPTypeParams, 84 GetMemoryType OEGraphSim:: OEFastFPDatabase, 57 GetMemoryTypeString OEGraphSim:: OEFastFPDatabase, 57 GetMin OEGraphSim:: OEFPHistogram, 79 GetMinDistance OEGraphSim:: OEFPTypeParams, 84 GetMolDatabaseFilename OEGraphSim:: OEFastFPDatabaseParams, 53 GetMoleculeIndex OEGraphSim:: OEFastFPDatabase, 57 GetNumBits OEGraphSim:: OEFPTypeParams, 84 GetNumProcessors OEGraphSim::OECreateFastFPDatabaseOptions, 52 OEGraphSim:: OEFPDatabaseOptions, 74 GetRawScores OEGraphSim:: OEFastFPDatabase, 57 GetScore

OEGraphSim:: OESimScore, 88 OEGraphSim:: OESimScorePair, 88 OEGraphSim:: OEFastFPDatabase, 58 OEGraphSim:: OEFPDatabase, 66 GetSearchStatus OEGraphSim:: OESimSearchResult, 89 GetSimFunc OEGraphSim:: OEFPDatabaseOptions, 74 GetSimTypeString OEGraphSim:: OESimFuncBase, 87 OEGraphSim:: OETanimotoSim, 91 OEGraphSim:: OETverskySim, 92 GetSmarts OEGraphSim:: OEFPPattern, 81 GetSortedScores OEGraphSim:: OEFastFPDatabase, 58 OEGraphSim:: OEFPDatabase, 68 OEGraphSim:: OESimSearchResult, 89 GetSparseMatrix OEGraphSim:: OEFastFPDatabase, 59 GetTverskyAlpha OEGraphSim:: OEFPDatabaseOptions, 74 GetTverskyBeta OEGraphSim:: OEFPDatabaseOptions, 75 GetUnhashed OEGraphSim:: OEFPPattern, 81 GetVariogram OEGraphSim:: OEFastFPDatabase, 59 OEGraphSim:: OEFPVariogram, 86 GetVersion OEGraphSim:: OEFPTypeParams, 85

## H

HasCutoff OEGraphSim:: OEFPDatabase, 70 OEGraphSim:: OEFPDatabaseOptions, 75

## $\mathsf{l}$

IsInLittleEndian OEGraphSim:: OEFastFPDatabaseParams, 53 IsValid OEGraphSim:: OEFastFPDatabase, 60 OEGraphSim:: OEFastFPDatabaseParams, 53 OEGraphSim:: OEFPTypeParams, 85 OEGraphSim:: OESimSearchResult, 89 M makefastfp.py

Example Code, 44 Manhattan similarity measure, 13

OEGraphSim::OEFastFPDatabaseMemoryType::CUDA,

OEGraphSim::OEFastFPDatabaseMemoryType::Default,

OEGraphSim::OEFastFPDatabaseMemoryType::InMemory,

OEGraphSim::OEFastFPDatabaseMemoryType::MemoryMappe

OEGraphSim::OEFastFPDatabaseMemoryType,

OEGraphSim:: OEFastFPDatabaseParams, 52

GetMolDatabaseFilename, 53

SortedSearch, 61

92

93

92

93

93

IsValid. 53

Constructors, 52

GetFPTypeBase, 53

IsInLittleEndian. 53

NumFingerPrints, 53

OEGraphSim:: OEFingerPrint, 62

Mean OEGraphSim:: OEFPHistogram, 79

## N

NumBins OEGraphSim:: OEFPHistogram, 79 NumFingerPrints OEGraphSim:: OEFastFPDatabase, 61 OEGraphSim:: OEFastFPDatabaseParams, 53 OEGraphSim:: OEFPDatabase, 70 NumSamples OEGraphSim:: OEFPHistogram, 79 NumSearched OEGraphSim:: OESimSearchResult, 90 NumTargets OEGraphSim:: OESimSearchResult, 90

## O

Constructors, 63 OEGraphSim::OEAreCompatibleDatabases, GetFPTypeBase, 63 117 operator bool, 63 OEGraphSim:: OEConfigureFingerPrint, 118 OEGraphSim::OEConfigureFPDatabaseMemoryType, Operator! = , 63 operator= $, 63$ 118 operator==, $63$ OEGraphSim::OEConfigureFPDatabaseOptions, SetFPTypeBase, 63 119 OEGraphSim:: OEFPAtomType, 93 OEGraphSim:: OECosine, 119 OEGraphSim::OEFPAtomType::Aromaticity, OEGraphSim:: OECreateFastFPDatabaseFile, 95 119 OEGraphSim::OECreateFastFPDatabaseOptionQFGraphSim::OEFPAtomType::AtomicNumber, 95 51 OEGraphSim:: OEFPAtomType:: Chiral, 96 Constructors, 51 OEGraphSim::OEFPAtomType::DefaultAtom, GetFPType, 51 102 GetNumProcessors, 52 OEGraphSim::OEFPAtomType::DefaultCircularAtom, SetNumProcessors, 52 102 SetTracer, 52 OEGraphSim::OEFPAtomType::DefaultCircularVSAtom, OEGraphSim:: OEDice, 120 103 OEGraphSim:: OEEuclid, 121 OEGraphSim::OEFPAtomType::DefaultPathAtom, OEGraphSim:: OEFastFPDatabase, 53 103 Constructors, 54 OEGraphSim::OEFPAtomType::DefaultPathVSAtom, GetAllScores, 55 104 GetFingerPrint, 56 OEGraphSim::OEFPAtomType::DefaultTreeAtom, GetFPTypeBase, 56 104 GetHistogram, 56 OEGraphSim::OEFPAtomType::DefaultTreeVSAtom, GetMemoryType, 57 105 GetMemoryTypeString, 57 OEGraphSim::OEFPAtomType::EqAromatic, GetMoleculeIndex, 57 99 GetRawScores, 57 OEGraphSim::OEFPAtomType::EqHalogen, 100 GetScores, 58 OEGraphSim::OEFPAtomType::EqHBondAcceptor, GetSortedScores, 58 100 GetSparseMatrix, 59 OEGraphSim::OEFPAtomType::EqHBondDonor, GetVariogram, 59 101 IsValid, 60 OEGraphSim::OEFPAtomType::FormalCharge, NumFingerPrints, 61

96 SetDescendingOrder, 75 OEGraphSim:: OEFPAtomType:: HCount, 98 SetLimit, 76 SetNumProcessors, 76 OEGraphSim::OEFPAtomType::HvyDegree, 97 OEGraphSim::OEFPAtomType::Hybridization, SetSimFunc, 76 98 SetTverskyCoeffs, 76 OEGraphSim:: OEFPAtomType:: InRing, 99 OEGraphSim::OEFPDatabaseOptionsSetup, OEGraphSim:: OEFPAtomType:: None, 105 111 OEGraphSim:: OEFPBondType, 105 OEGraphSim::OEFPDatabaseOptionsSetup::All, OEGraphSim::OEFPBondType::BondOrder, 106 111 OEGraphSim:: OEFPBondType:: Chiral, 107 OEGraphSim::OEFPDatabaseOptionsSetup::Cutoff, OEGraphSim::OEFPBondType::DefaultBond, 111 OEGraphSim::OEFPDatabaseOptionsSetup::DescendingOre 108 OEGraphSim::OEFPBondType::DefaultCircularBond, 112 108 OEGraphSim::OEFPDatabaseOptionsSetup::Limit, OEGraphSim::OEFPBondType::DefaultCircularVSBond,12 109 OEGraphSim::OEFPDatabaseOptionsSetup::SimFunc, OEGraphSim::OEFPBondType::DefaultPathBond, 113 OEGraphSim:: OEFPHistogram, 77 109 OEGraphSim::OEFPBondType::DefaultPathVSBond,AddSample, 77 110 Constructors, 77 OEGraphSim::OEFPBondType::DefaultTreeBond, GetBinBoundaries, 77 GetBinCenters, 78 110 OEGraphSim::OEFPBondType::DefaultTreeVSBond,GetBinIdx, 78 GetBinWidth.78 110 OEGraphSim::OEFPBondType::InRing, 107 GetCounts, 78 OEGraphSim::OEFPBondType::None, 111 GetDensity, 78 OEGraphSim:: OEFPDatabase, 64 GetMax, 79 AddFP, 65 GetMin, 79 Mean, 79 ClearCutoff, 65 Constructors, 64 NumBins, 79 GetCutoff, 65 NumSamples, 79 GetDescendingOrder, 65 Std. 79 GetFingerPrints, 66 OEGraphSim:: OEFPPattern, 80 GetFPTypeBase, 66 Constructors, 80 GetBit, 81 GetScores, 66 GetSortedScores. 68 GetSmarts, 81 HasCutoff, 70 GetUnhashed, 81 NumFingerPrints, 70 operator=, 80 SetCutoff, 71 OEGraphSim:: OEFPType, 113 SetDescendingOrder, 71 OEGraphSim:: OEFPType:: Circular, 114 SetSimFunc, 71 OEGraphSim:: OEFPType:: Lingo, 114 OEGraphSim:: OEFPDatabaseOptions, 72 OEGraphSim::OEFPType::MACCS166,114 ClearCutoff.73 OEGraphSim::OEFPType::Path, 114 Constructors, 72 OEGraphSim:: OEFPType::Tree, 114 GetCutoff, 73 OEGraphSim:: OEFPTypeBase, 81 Constructors, 81 GetDescendingOrder, 74 GetLimit, 74 GetFPType, 81 GetNumProcessors, 74 GetFPTypeString, 82 GetSimFunc, 74 GetFPVersion, 82 GetTverskyAlpha, 74 GetFPVersionString, 83 GetTverskyBeta, 75 OEGraphSim:: OEFPTypeParams, 83 HasCutoff, 75 Constructors, 83 operator=, 73 GetAtomTypes, 83 SetCutoff, 75 GetBondTypes, 84

GetFPType, 84 GetMaxDistance, 84 GetMinDistance, 84 GetNumBits, 84 GetVersion, 85 IsValid, 85 OEGraphSim:: OEFPVariogram, 85 AddSample, 86 Constructors, 86 GetVariogram, 86 OEGraphSim:: OEGetBitCounts, 121 OEGraphSim::OEGetCircularFPType, 121 OEGraphSim::OEGetFingerPrintVersion, 122 OEGraphSim::OEGetFingerPrintVersionStringEGraphSim::OESimMeasure::Tanimoto,116 122 OEGraphSim:: OEGetFPAtomType, 122 OEGraphSim:: OEGetFPBondType, 123 OEGraphSim:: OEGetFPCoverage, 123 OEGraphSim::OEGetFPDatabaseMemoryType, 124 OEGraphSim:: OEGetFPOverlap, 124 OEGraphSim:: OEGetFPPatterns, 125 OEGraphSim:: OEGetFPType, 125 OEGraphSim:: OEGetPathFPType, 126 OEGraphSim:: OEGetPopCountMethod, 126 OEGraphSim::OEGetSimilarityMeasureName, 126 OEGraphSim:: OEGetTreeFPType, 126 OEGraphSim:: OEGraphSimGetArch, 127 OEGraphSim:: OEGraphSimGetLicensee, 127 OEGraphSim:: OEGraphSimGetPlatform, 127 OEGraphSim:: OEGraphSimGetRelease, 127 OEGraphSim:: OEGraphSimGetSite, 127 OEGraphSim:: OEGraphSimGetVersion, 128 OEGraphSim:: OEGraphsimIsGPUReady, 128 OEGraphSim:: OEGraphSimIsLicensed, 128 OEGraphSim:: OEIsFastFPDatabaseReady, 128 OEGraphSim:: OEIsFPType, 128 OEGraphSim:: OEIsSameFPType, 129 OEGraphSim:: OEIsValidFPTypeString, 129 OEGraphSim:: OEMakeCircularFP, 129 OEGraphSim:: OEMakeFP, 130 OEGraphSim:: OEMakeLingoFP, 131 OEGraphSim:: OEMakeMACCS166FP, 131 OEGraphSim:: OEMakePathFP, 132 OEGraphSim:: OEMakeTreeFP, 132 OEGraphSim:: OEManhattan, 133 OEGraphSim:: OEPopCountMethod, 115 OEGraphSim:: OEPopCountMethod:: BitCount, 115 OEGraphSim::OEPopCountMethod::NoSupport, 115 OEGraphSim::OEPopCountMethod::PopCount, 115

OEGraphSim:: OESetupFingerPrint, 134 OEGraphSim::OESetupFPDatabaseOptions, 134 OEGraphSim:: OESimFuncBase, 86 Constructors, 86 CreateCopy, 87 GetSimTypeString, 87 operator(), 87 OEGraphSim:: OESimMeasure, 115 OEGraphSim:: OESimMeasure:: Cosine, 115 OEGraphSim:: OESimMeasure:: Dice, 116 OEGraphSim:: OESimMeasure:: Euclid, 116 OEGraphSim:: OESimMeasure:: Manhattan, 116 OEGraphSim:: OESimMeasure:: Tversky, 116 OEGraphSim:: OESimScore, 87 Constructors, 87 GetIdx, 87 GetScore, 88 OEGraphSim:: OESimScorePair, 88 Constructors, 88 GetIdxA, 88 GetIdxB, 88 GetScore, 88 OEGraphSim:: OESimSearchResult, 89 Constructor, 89 GetSearchStatus, 89 GetSortedScores, 89 IsValid, 89 NumSearched, 90 NumTargets, 90 OEGraphSim:: OESimSearchStatus, 117 OEGraphSim:: OESimSearchStatus:: Finished, 117 OEGraphSim::OESimSearchStatus::InProgress, 117 OEGraphSim::OESimSearchStatus::Uninitialized, 117 OEGraphSim:: OESimSearchStatusToName, 134 OEGraphSim:: OETanimoto, 135 OEGraphSim:: OETanimotoSim, 90 Constructors, 90 CreateCopy, 91 GetSimTypeString, 91 operator(), 90 OEGraphSim:: OETversky, 135 OEGraphSim:: OETverskySim, 91 Constructors, 91 CreateCopy, 92 GetAlpha, 92 GetBeta, 92 GetSimTypeString, 92 operator(), 91 operator bool

```
OEGraphSim:: OEFingerPrint, 63
operator! =OEGraphSim:: OEFingerPrint, 63
operator()
   OEGraphSim:: OESimFuncBase, 87
   OEGraphSim:: OETanimotoSim, 90
   OEGraphSim:: OETverskySim, 91
operator=
   OEGraphSim:: OEFingerPrint, 63
   OEGraphSim:: OEFPDatabaseOptions, 73
   OEGraphSim:: OEFPPattern, 80
operator==
   OEGraphSim:: OEFingerPrint, 63
```

## S

```
searchfastfp.py
   Example Code, 47
searchfp.py
   Example Code, 40
SetCutoff
   OEGraphSim:: OEFPDatabase, 71
   OEGraphSim:: OEFPDatabaseOptions, 75
SetDescendingOrder
   OEGraphSim:: OEFPDatabase, 71
   OEGraphSim:: OEFPDatabaseOptions, 75
SetFPTypeBase
   OEGraphSim:: OEFingerPrint, 63
SetLimit
   OEGraphSim:: OEFPDatabaseOptions, 76
SetNumProcessors
   OEGraphSim:: OECreateFastFPDatabaseOptions,
       52
   OEGraphSim:: OEFPDatabaseOptions, 76
SetSimFunc
   OEGraphSim:: OEFPDatabase, 71
   OEGraphSim:: OEFPDatabaseOptions, 76
SetTracer
   OEGraphSim::OECreateFastFPDatabaseOptions,
       52
SetTverskyCoeffs
   OEGraphSim:: OEFPDatabaseOptions, 76
similarity measure
   Cosine, 12
   Dice. 13
   Euclidean, 13
   Manhattan, 13
   Tanimoto, 14
   Tversky, 14
SortedSearch
   OEGraphSim:: OEFastFPDatabase, 61
Std
   OEGraphSim:: OEFPHistogram, 79
```

## T

```
Tanimoto
   similarity measure, 14
Tversky
   similarity measure, 14
```