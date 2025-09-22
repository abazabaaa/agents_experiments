![](_page_0_Picture_0.jpeg)

# **OEMedChem TK - Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| Section                                          | Title                                                                            | Page                            |     |
|--------------------------------------------------|----------------------------------------------------------------------------------|---------------------------------|-----|
| 1                                                | Introduction                                                                     | 1                               |     |
| 2                                                | Theory                                                                           | 1                               |     |
| 2.1                                              | Molecule Fragmentation                                                           | 1                               |     |
| 2.2                                              | Matched Molecule Pair Analysis                                                   | 1                               |     |
| 2.2.1                                            | Introductory Usage of Matched Molecular Pair Analysis                            | 1                               |     |
| 3                                                | Examples                                                                         | 1                               |     |
| 3.1                                              | OEMedChem TK Examples                                                            | 1                               |     |
| 3.1.1                                            | Bemis Murcko perception                                                          | 1                               |     |
| 3.1.2                                            | Apply ChEMBL solubility transformations                                          | 1                               |     |
| 3.1.3                                            | Matched Pair analysis generation of a MMP index                                  | 2                               |     |
| 3.1.4                                            | Matched Pair analysis using a multi-process generation of an MMP index           | 2                               |     |
| 3.1.5                                            | Matched Pair analysis using a multi-threaded generation of a MMP index           | 3                               |     |
| 3.1.6                                            | Matched Pair analysis and transformations                                        | 4                               |     |
| 3.1.7                                            | Matched Pair analysis and listing of transformations                             | 4                               |     |
| 3.1.8                                            | Matched Pair analysis and listing of transformations related to probe structures | 5                               |     |
| 3.1.9                                            | MCS Fragment database generation                                                 | 5                               |     |
| 3.1.10                                           | MCS Similarity score reporting                                                   | 6                               |     |
| 3.1.11                                           | MCS Fragmentation API                                                            | 6                               |     |
| 3.1.12                                           | Print OEMedChem version information                                              | 7                               |     |
| 4                                                | API                                                                              | 7                               |     |
| 4.1                                              | OEMedChem API                                                                    | 7                               |     |
| 4.1.1                                            | OEMedChem Classes                                                                | 7                               |     |
| 4.1.2                                            | OEMedChem Constants                                                              | 10                              |     |
| 4.1.3                                            | OEMedChem Functions                                                              | 12                              |     |
| 5                                                | Release History                                                                  | 15                              |     |
| 5.1                                              | OEMedChem TK 1.2.3                                                               | 15                              |     |
| 5.2                                              | OEMedChem TK 1.2.2                                                               | 15                              |     |
| 5.3                                              | OEMedChem TK 1.2.1                                                               | 15                              |     |
| 5.4                                              | OEMedChem TK 1.2.0                                                               | 15                              |     |
| 5.4.1                                            | Internal changes                                                                 | 15                              |     |
| 5.5                                              | OEMedChem TK 1.1.7                                                               | 15                              |     |
| 5.6                                              | OEMedChem TK 1.1.6                                                               | 15                              |     |
| 5.7                                              | OEMedChem TK 1.1.5                                                               | 15                              |     |
| 5.8                                              | OEMedChem TK 1.1.4                                                               | 15                              |     |
| 5.8.1                                            | Minor bug fixes                                                                  | 15                              |     |
| 5.9                                              | OEMedChem TK 1.1.3                                                               | 15                              |     |
| 5.9.1 New features                               | 15                                                                               |                                 |     |
| 5.9.2 Documentation changes                      | 15                                                                               |                                 |     |
| 5.10 OEMedChem TK 1.1.2                          | 15                                                                               |                                 |     |
| 5.10.1 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.11 OEMedChem TK 1.1.1                          | 15                                                                               |                                 |     |
| 5.11.1 New features                              | 15                                                                               |                                 |     |
| 5.11.2 Documentation changes                     | 15                                                                               |                                 |     |
| 5.12 OEMedChem TK 1.1.0                          | 15                                                                               |                                 |     |
| 5.12.1 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.13 OEMedChem TK 1.0.7                          | 15                                                                               |                                 |     |
| 5.13.1 New features                              | 15                                                                               |                                 |     |
| 5.13.2 New features (Preliminary API)            | 15                                                                               |                                 |     |
| 5.13.3 API changes                               | 15                                                                               |                                 |     |
| 5.13.4 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.13.5 Python-specific changes                   | 15                                                                               |                                 |     |
| 5.13.6 Documentation changes                     | 15                                                                               |                                 |     |
| 5.14 OEMedChem TK 1.0.6                          | 15                                                                               |                                 |     |
| 5.14.1 New features                              | 15                                                                               |                                 |     |
| 5.14.2 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.15 OEMedChem TK 1.0.5                          | 15                                                                               |                                 |     |
| 5.15.1 New features                              | 15                                                                               |                                 |     |
| 5.15.2 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.15.3 Documentation changes                     | 15                                                                               |                                 |     |
| 5.16 OEMedChem TK 1.0.4                          | 15                                                                               |                                 |     |
| 5.16.1 New features                              | 15                                                                               |                                 |     |
| 5.16.2 Preliminary Fragmentation API             | 15                                                                               |                                 |     |
| 5.16.3 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.16.4 Python-specific changes                   | 15                                                                               |                                 |     |
| 5.16.5 Java-specific changes                     | 15                                                                               |                                 |     |
| 5.16.6 C#-specific changes                       | 15                                                                               |                                 |     |
| 5.16.7 Documentation changes                     | 15                                                                               |                                 |     |
| 5.17 OEMedChem TK 1.0.3                          | 15                                                                               |                                 |     |
| 5.17.1 New features                              | 15                                                                               |                                 |     |
| 5.17.2 Documentation changes                     | 15                                                                               |                                 |     |
| 5.18 OEMedChem TK 1.0.2                          | 15                                                                               |                                 |     |
| 5.18.1 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.19 OEMedChem TK 1.0.1                          | 15                                                                               |                                 |     |
| 5.19.1 Minor bug fixes                           | 15                                                                               |                                 |     |
| 5.20 OEMedChem TK 1.0.0                          | 15                                                                               |                                 |     |
| 5.20.1 Licensing changes                         | 15                                                                               |                                 |     |
| 5.20.2 OEMedChem functionalities                 | 16                                                                               |                                 |     |
| 5.20.3 Matched molecular pair analysis           | 16                                                                               |                                 |     |
| 5.20.4 Fragmentation and perception capabilities | 16                                                                               |                                 |     |
| 5.20.5 Belief theory                             | 16                                                                               |                                 |     |
| 5.20.6 Similarity                                | 16                                                                               |                                 |     |
| 5.20.7 Complexity measures                       | 16                                                                               |                                 |     |
| 5.20.8 Minor bug fixes                           | 16                                                                               |                                 |     |
| 5.20.9 Documentation changes                     | 16                                                                               |                                 |     |
| 5.21 OEMedChem TK 0.9.6                          | 16                                                                               |                                 |     |
| 5.21.1 Beta-API changes                          | 16                                                                               |                                 |     |
| 5.21.2 New features                              | 16                                                                               |                                 |     |
| 5.21.3 Minor bug fixes                           | 16                                                                               |                                 |     |
| 5.21.4 Documentation changes                     | 16                                                                               |                                 |     |
| 5.22 OEMedChem TK 0.9.5                          | 16                                                                               |                                 |     |
|                                                  |                                                                                  | 5.22.1  New features            | 163 |
|                                                  |                                                                                  | 5.22.2  Beta-API changes        | 164 |
|                                                  |                                                                                  | 5.22.3  Major bug fixes         | 164 |
|                                                  | 5.23                                                                             | OEMedChem TK 0.9.4              | 164 |
|                                                  |                                                                                  | 5.23.1  Beta-API changes        | 164 |
|                                                  |                                                                                  | 5.23.2  New features            | 164 |
|                                                  |                                                                                  | 5.23.3  Major bug fixes         | 165 |
|                                                  |                                                                                  | 5.23.4  Documentation fixes     | 166 |
|                                                  | 5.24                                                                             | OEMedChem TK 0.9.3              | 166 |
|                                                  |                                                                                  | 5.24.1  New features            | 166 |
|                                                  |                                                                                  | 5.24.2  Known bugs              | 167 |
|                                                  |                                                                                  | 5.24.3  Documentation fixes     | 167 |
|                                                  | 5.25                                                                             | OEMedChem TK 0.9.2              | 167 |
|                                                  |                                                                                  | 5.25.1  Minor bug fixes         | 167 |
|                                                  | 5.26                                                                             | OEMedChem TK 0.9.1              | 168 |
|                                                  |                                                                                  | 5.26.1  New features            | 168 |
|                                                  | 5.27                                                                             | OEMedChem TK 0.9.0              | 168 |
|                                                  |                                                                                  | 5.27.1  New features            | 168 |
| 6                                                |                                                                                  | <b>Copyright and Trademarks</b> | 169 |
| 7                                                |                                                                                  | <b>Sample Code</b>              | 171 |
| 8                                                | <b>Citation</b>                                                                  |                                 | 173 |
|                                                  | 8.1                                                                              | Orion ® Floes                   | 173 |
|                                                  | 8.2                                                                              | Toolkits and Applications       | 173 |
|                                                  | 8.3                                                                              | OpenEye Web Services            | 173 |
| 9                                                |                                                                                  | <b>Technology Licensing</b>     | 177 |
|                                                  | 9.1                                                                              | GCC                             | 192 |
|                                                  | 9.1.1                                                                            | GCC RUNTIME LIBRARY EXCEPTION   | 192 |
|                                                  | 9.1.2                                                                            | GNU GENERAL PUBLIC LICENSE      | 194 |
|                                                  | <b>Index</b>                                                                     |                                 | 207 |

## **CHAPTER**

# **ONE**

# **INTRODUCTION**

This manual is to familiarize the user with OEMedChem TK functionality.

#### **CHAPTER**

# **THEORY**

## 2.1 Molecule Fragmentation

The OEMedChem TK currently provides four ways to partition a molecule into fragments:

- OEGetRingChainFragments fragments a molecule into ring and chain components.
- OEGetRingLinkerSideChainFragments fragments a molecule into ring, linker and side-chain components as defined in [Bemis-1996].
- OEGetFuncGroupFragments fragments a molecule into ring and functional group components.
- OEGetBemisMurcko fragments a molecule into ring, linker, framework and functional group components as in [Bemis-1996].

These functions return an iterator over OEAtomBondSet objects that store the atoms and the bonds of the fragments.

The following examples (Listing 1, Listing 2) show how to fragment a molecule into ring and chain components. The code loops over the OEAtomBondSet objects returned by the OEGetRingChainFragments. Each OEAtomBondSet object is used to initialize an atom and a bond predicates. These predicates specify which atoms and bonds have to be considered when creating a subset of the molecule, *i.e* the fragment, when calling the OESubsetMol function. See the depiction of the input molecule and the generated fragments in Figure: Example of fragmentation.

### Listing 1: Example of molecule fragmentation

```
from openeye import oechem
from openeye import oemedchem
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "COclocc(ccl)CC(=0)N")
for frag in oemedchem. OEGetRingChainFragments (mol) :
    fragatompred = oechem.OEIsAtomMember(frag.GetAtoms())
    fragbondpred = oechem. OEIsBondMember (frag. GetBonds())
    fragment = oechem. OEGraphMol()
    adjustHCount = Trueoechem. OESubsetMol(fragment, mol, fragatompred, fragbondpred, adjustHCount)
    print (oechem. OEMolToSmiles (fragment))
```

The output of Listing 1 is the following:

| <b>CO</b>   |  |  |  |
|-------------|--|--|--|
| clccccc1    |  |  |  |
| $CC (=O) N$ |  |  |  |

![](_page_9_Figure_2.jpeg)

**Generated by OEDepict TK** 

Fig. 1: **Example of fragmentation** (A) input molecule (B) fragments returned by the OEGetRingChainFragments function

#### See also:

- OEAtomBondSet class and OESubsetMol function in the OEChem TK manual
- Predicate Functors chapter in the OEChem TK manual.

The following example (Listing 2) shows how to fragment a molecule into ring and chain components with annotations. See the depiction of the input molecule and the generated fragments in Figure: Example of Bemis Murcko fragmentation.

#### Listing 2: Example of molecule fragmentation with annotations

```
from openeye import oechem
from openeye import oemedchem
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "CCOclocc(ccl)CC(OC)c2ccccc2CC(=0)N")
adjustHCount = Truefor frag in oemedchem. OEGetBemisMurcko(mol):
    fragment = oechem. OEGraphMol()
    oechem. OESubsetMol (fragment, mol, frag, adjustHCount)
    print (".".join (r. GetName () for r in frag. GetRoles()), oechem.
→OEMolToSmiles(fragment))
```

The output of  $Listing\ 2$  is the following:

Framework clccc (ccl) CCc2ccccc2 Ring cloccccl.cloccccl Linker CC Sidechain CCO.CC(=0)N.CO

![](_page_10_Figure_2.jpeg)

Generated by OEDepict TK

#### Fig. 2: Example of Bemis Murcko fragmentation

The following example (Listing 3) shows how to fragment a molecule and include unsaturated hetero bonds on the main framework. See the depiction of the input molecule and the generated fragments in Figure: Example of custom Bemis Murcko fragmentation including heteroatoms.

#### Listing 3: Example of custom molecule fragmentation

```
from openeye import oechem
from openeye import oemedchem
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "CCclnc(nc(n1)OC)NC(=0)NS(=0)(=0)c2ccccc2OC")
options = oemedchem.OEBemisMurckoOptions()
options. SetUnsaturatedHeteroBonds (True)
adjustHCount = Truefor frag in oemedchem. OEGetBemisMurcko (mol, options):
    fragment = occhem.OEGraphMol()oechem. OESubsetMol (fragment, mol, frag, adjustHCount)
    print (".".join(r.GetName() for r in frag.GetRoles()), oechem.
\rightarrowOEMolToSmiles (fragment))
```

The output of  $Listing \; 3$  is the following:

```
Framework \text{c}1\text{ccc}(\text{c}1) S(=0)(=0)NC(=0)Nc2ncncn2
Ring cloccocl.clncncn1
Linker C (=0) (N) NS (=0) = 0Sidechain CC.CO.CO
```

The following example (Listing 4) shows how to fragment a molecule and include custom side chains on the main framework. See the depiction of the input molecule and the generated fragments in Figure: Example of custom Bemis Murcko fragmentation including custom substituents.

![](_page_11_Figure_1.jpeg)

#### Fig. 3: Example of Bemis Murcko fragmentation including unsaturated hetero bonds on main framework.

Listing 4: Example of custom molecule fragmentation

```
from openeye import oechem
from openeye import oemedchem
mol = occhem. OEGraphMol()oechem. OESmilesToMol(mol, "CCclnc(nc(n1)OC)NC(CC(=0)N)NS(=0)(=0)c2ccccc2CC(=0)N")
subsearch = occhem.OESubSearch()
subsearch. Init (" [ #6] - CC (=0) N")options = oemedchem.OEBemisMurckoOptions()
options. SetSubstituentSearch (subsearch)
adjustHCount = Truefor frag in oemedchem. OEGetBemisMurcko(mol, options):
    fragment = oechem. OEGraphMol()
    oechem. OESubsetMol (fragment, mol, frag, adjustHCount)
    print ("." . join(r. GetName() for r in frag.GetRoles()), oechem.
\rightarrowOEMolToSmiles (fragment))
```

The output of  $Listing \ 4$  is the following:

```
Framework \text{c}lccc(\text{c}(\text{c}l)CC(=0)N) [SH4]NC(CC(=0)N)Nc2ncncn2
Ring clccc (ccl) CC (=0) N. clncncn1
Linker C(C(N)N[SH5])C(=0)NSidechain CC.CO.O.O
```

# 2.2 Matched Molecule Pair Analysis

This overview is intended for users which have a working knowledge of matched pair analysis in the context of medicinal chemistry workflows. If the concept of matched pair analysis is unfamiliar, the following references are highly recommended as background to this powerful strategy ([Griffen-2011], [Kramer-2014], [Papadatos-2010], [Warner- $2010$ ]).

The OEMedChem TK provides the ability to index a set of input structures and identify matched molecular pairs. Matched Molecular Pair Analysis (MMPA) is becoming recognized as a powerful tool for the extraction of the effects of chemical changes on properties of interest in large data sets. One of the powers of the MMPA approach stems from the assumption that it is easier to predict differences in an activity or a property than to predict an actual value. A

![](_page_12_Figure_1.jpeg)

Fig. 4: Example of Bemis Murcko fragmentation including custom substituents on framework

matched molecular pair is considered to be a pair of compounds that differ by a small localized change in a chemical substituent. The magnitude of the localized change that is considered acceptable is highly specific to the chemist or analyst. For a given matched molecular pair, one can consider the chemical difference between two compounds to embody a virtual chemical transformation with an accompanying change in a property of interest. For a homologous series of input structures, a set of matched molecular pairs for each transformation can be identified and analyzed for statistical relevance, sorting and/or ranking. Similarly, large input data sets can be mined for interesting or desired property changes as a function of structure.

A common method of identifying matched molecular pairs is an NxM pairwise maximum common subgraph (MCS) analysis of an input data set. Owing to the complexity and performance of MCS algorithms generally, OpenEye instead chose to use a molecular fragmentation approach (cf [Hussain-2010]) to identify matched molecular pairs and to deliver robust performance characteristics over a wider variety of input data set sizes. Additionally, this approach is entirely data-driven and does not require *a priori* defined cores. A small set of fragmentation strategies are currently provided, and future releases will expose additional fragmentation types and capabilities. MMPA as a technique is relatively new and there have been spirited discussions about the applicability of the method when applied to various measured properties. OpenEye encourages users to critically examine the results available from such an analysis and to evaluate the applicability or non-applicability of property predictions with sound statistical analyses.

The general steps involved in an MMP analysis are,

- Prepare the input structures
- Prune input structure data to the property or properties of interest
- Select indexing filters to identify the desired "localized change" in structures
- Index the input structures
- Extract transformations and/or matched molecular pairs and data
- Optionally save the index for subsequent analyses

The internal index captures the common cores for the identified matched molecular pairs and the set of substituent changes associated with each core. Once the index has been generated, it can be used to,

- Extract the virtual chemical transformations and set of delta properties for the MMPs
- Extract the MCS cores of MMPs for clique or binning analysis
- Extract statistics for property changes from a series of substituents on a common core
- Identify or remove singletons or unrelated chemical frameworks from the input structures

Matched molecular pair transformations inherently have the concept of a chemical context for any given set of matched pairs. At the site (or sites) of the substituent differences in the two compounds one can consider the accompanying effects of the adjacent common core environment for the pair. To this end, the extraction of the matched pair transformations supports the ability to tune the amount of the adjacent common core to be included as part of the transformation. As more chemical context is included, more differentiation among the set of transformations occurs, generally resulting in fewer numbers of matched molecular pairs associated with each transformation. Thus, requesting a OEMatchedPairContext Bond0 context when extracting transformations from an index is likely to produce the largest set of matched pairs associated with each transform, but at the expense of coalescing possibly unrelated chemical environments into the same transformation bin. That is, a  $C1>>Br$  transformation on a ring or aromatic ring is likely quite different compared to the same transformation in a non-ring portion of the structure with regards to the properties of interest for an MMP analysis.

The OEMatchedPairAnalyzer is the utility class the provides the bulk of the Matched Pair Analysis capabilities in OEMedChem TK, see docs for additional details.

### 2.2.1 Introductory Usage of Matched Molecular Pair Analysis

As a trivial example, suppose a chemist is interested in extracting all the "simple" substituent changes in a large input set. One possible way to accomplish this is to define some limits to what constitutes a "simple" substituent change and run an MMP analysis of the input structures. Here we define a "simple" substituent change to be singly attached groups only, and where the size of the group cannot exceed  $20\%$  of the input structure heavy atom count.

```
# create options class with defaults
   mmpOpts = oemedchem.OEMatchedPairAnalyzerOptions()
   # for 'simple' pairs, alter default indexing options
   # - single cuts only, heavy atom substituents only (HMember indexing off)
   mmpOpts.SetOptions(oemedchem.OEMatchedPairOptions_SingleCuts |
                      oemedchem.OEMatchedPairOptions_ComboCuts |
                      oemedchem.OEMatchedPairOptions_UniquesOnly)
   # - limit substituent size to no more than 20% of input structure
   mmpOpts.SetIndexableFragmentRange(80., 100.)
   # create analyzer class with nondefault options
   mmpAnalyzer = oemedchem. 0EMatchedPairAnalyzer (mmp0pts)# ignore common index status returns
   sIgnoreStatus = 'FragmentRangeFilter, DuplicateStructure, '
   sIgnoreStatus += 'FragmentationLimitFilter, HeavyAtomFilter'
   # index the input structures
   for recindex, mol in enumerate (ims. GetOEGraphMols (), start=1):
       # consider only the largest input fragment
       oechem.OEDeleteEverythingExceptTheFirstLargestComponent (mol)
       # ignore stereochemistry
       oechem.OEUncolorMol(mol,
                            (oechem.OEUncolorStrategy_RemoveAtomStereo |
                            oechem.OEUncolorStrategy_RemoveBondStereo))
       # explicitly provide a 1-based index to refer to indexed structures
       # - to allow references back to external data elsewhere
       status = mmpAnalyzer.AddMol(mol, recindex)
       if status != recindex:
           if not oemedchem. OEMatchedPairIndexStatusName (status) in
→sIqnoreStatus:
               oechem. OEThrow. Warning ("{0}: molecule indexing error, status=
```

```
.format (recindex,
                                                 oemedchem.
\rightarrowOEMatchedPairIndexStatusName(status)))
        # if limiting input, quit after limit
       if maxrecs and recindex >= maxrecs:
           break
   print ("Index complete, matched pairs = {0}"
          .format(mmpAnalyzer.NumMatchedPairs()))
   # specify how transforms are extracted (direction and allowed properties)
   extractMode = (oemedchem.OEMatchedPairTransformExtractMode_Sorted |
                   oemedchem.OEMatchedPairTransformExtractMode_NoSMARTS |
                   oemedchem.OEMatchedPairTransformExtractMode
→AddMCSCorrespondence)
   extractOptions = oemedchem.OEMatchedPairTransformExtractOptions()
   # specify amount of chemical context at the site of the substituent,
\leftrightarrowchange
   # in the transform
   extractOptions.SetContext(oemedchem.OEMatchedPairContext_Bond0)
   extractOptions. SetOptions (extractMode)
   # walk the transforms and print the matched pairs
   xfmidx = 0for mmpxform in oemedchem. OEMatchedPairGetTransforms (mmpAnalyzer,
                                                           extractOptions):
       xfmidx += 1
       print ("{0:2} {1}".format (xfmidx, mmpxform.GetTransform()))
       # dump matched molecular pairs and index identifiers
           (recindex from indexing loop above)
       for mmppair in mmpxform. GetMatchedPairs():
            print ("\tmatched pair molecule indices=({0}, {1})".format (mmppair.
\rightarrowFromIndex(),
                                                                        mmppair.
\rightarrowToIndex()))
```

Sample output of the example above is the following:

```
Index complete, matched pairs = 1461 [c:1] Br \geq [c:1] Fmatched pair molecule indices=(4793,1225)
 matched pair molecule indices=(1304,9796)
 matched pair molecule indices=(9515,6129)
 matched pair molecule indices=(4201,2611)
 2 [c:1]Br>>[c:1]OCC
 matched pair molecule indices=(7846,9727)
 matched pair molecule indices=(1547,2939)
 matched pair molecule indices=(5128,8928)
3 [c:1]Cl \gg [c:1]Fmatched pair molecule indices=(8116,7661)
 matched pair molecule indices=(239,6631)
 matched pair molecule indices=(9225,8434)
4 [c:1]F>> [c:1]OCmatched pair molecule indices=(3862,8684)
 matched pair molecule indices=(1349,1434)
 matched pair molecule indices=(416,3900)
```

```
5 [c:1] Br>>[c:1] SC
 matched pair molecule indices=(6364,8527)
 matched pair molecule indices=(1999,6845)
6 [c:1] C # N>> [c:1] Fmatched pair molecule indices=(2760,5231)
 matched pair molecule indices=(6677,241)
 7 [c:1]C>> [c:1]C1matched pair molecule indices=(1191,1605)
 matched pair molecule indices=(9591,4139)
8 [c:1]F>>[c:1]N(C)C
 matched pair molecule indices=(4012,853)
 matched pair molecule indices=(1779,1233)
9 [C:1]C>> [C:1]Omatched pair molecule indices=(2072,3429)
10 [C:1]C>> [C:1]OCCmatched pair molecule indices=(9803,9538)
\sim \sim \sim
```

### **CHAPTER**

## **THREE**

## **EXAMPLES**

# 3.1 OEMedChem TK Examples

The following table lists the currently available OEMedChem TK examples:

| Program                          | Description                                                                        |
|----------------------------------|------------------------------------------------------------------------------------|
| <i>OEMedChemInfo</i>             | Print library version information                                                  |
| <i>BemisMurckoPerception</i>     | Bemis-Murcko region perception                                                     |
| <i>ChEMBLsolubility</i>          | Apply solubility transformations found from ChEMBL<br>structures                   |
| <i>CreateMMPIndex</i>            | Generation of an MMP index from a Matched Pair analysis                            |
| <i>CreateMMPIndexParallel</i>    | Multi-process generation of an MMP index from a Matched Pair analysis              |
| <i>CreateMMPIndexThreaded</i>    | Multi-threaded generation of an MMP index from a Matched Pair analysis             |
| <i>MatchedPairTransform</i>      | Load a Matched Pair index and apply transformations                                |
| <i>MatchedPairTransformList</i>  | Load a Matched Pair index and list of transformations                              |
| <i>MatchedPairTransformProbe</i> | Load a Matched Pair index and list of transformations related to a probe structure |
| <i>CreateMCSFragDatabase</i>     | Generation of an MCS fragment index from an MCS fragmentation analysis             |
| <i>MCSFragDatabase</i>           | Load an MCS fragment index and report similarity scores for probe structures       |
| <i>MCSFragOccurrence</i>         | Load an MCS fragment index and report occurrence counts for common fragments       |

**Examples:** 

## 3.1.1 Bemis Murcko perception

A program that perceives the [Bemis-1996] regions of the input structures and outputs role information and annotations as SD data in the output. Uncoloring of the fragment regions to remove atom types and properties can optionally be requested for the output SMILES string annotations.

#### See also:

· OEGetBemisMurckofunction

#### **Command Line Interface**

```
Usage: ./BemisMurckoPerception input.sdf output.sdf [ -uncolor ] [-
-unsaturatedHeteroBonds] [ -smartsSubstituents substituentsString ]
[-regionType regionTypeString]
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
+++++++++++++++++++++++++++++++++++++++
# Utility to fragment the input structures by Bemis-Murcko rules
# -------------------------------------
# BemisMurckoPerception.py [ -uncolor ] [-i] <input_mols> [-o] <output_mols>
# [-unsatHetero] [-sub] <smarts_substituents>
# input_mols: filename of molecules to fragment and uncolor
# output mols: filename of output structures annotated with SD data of perceived.
\leftrightarrowregions
# [ -uncolor ]: optional arg to request uncoloring of output fragment info
# [-unsatHetero]: optional arg to include unsaturated bonds on hetero atoms to.
\rightarrowframework
# [-sub]: optional arg to include substituents specified by SMARTS pattern on.
\rightarrowframework
#######################################
from openeye import oechem
from openeye import oemedchem
import sys
#######################################
InterfaceData = ""!BRIEF [ -uncolor ] [-i] <infile1> [-o] <infile2> [-unsatHetero] [-r] <regionType> [-
\leftrightarrowsubl \leqsmartsSubs>
!PARAMETER -i
 !ALIAS -in
 !ALIAS -input
 !TYPE string
 !REQUIRED true
 !BRIEF Input structure file name
 !KEYLESS 1
LEND
```

```
!PARAMETER -o
 !ALIAS -out
 !ALIAS -output
 !TYPE string
 !REQUIRED true
 !BRIEF Output SD file name
  !KEYLESS 2
! END
!PARAMETER -uncolor
 IATITAS - u!TYPE bool
 !DEFAULT false
 !BRIEF Uncolor output molecules
LEND
!PARAMETER -unsatHetero
 !ALIAS -uhb
 ITYPE bool
 !DEFAULT false
 !BRIEF Include sidechains on main framework if connected by unsaturated bonds to
→hetero atoms.
!END
!PARAMETER -regionType
 IATITAS -r!TYPE string
 !DEFAULT All
 !BRIEF Region type of fragments to include. Valid inputs are All, Framework, Ring,
→Linker, and Sidechain.
! END
!PARAMETER -smartsSubstituents
 !ALIAS -sub
 ! TYPE string
 !DEFAULT None
 !BRIEF SMARTS string for custom substituents to be included in framework.
!END
H/H/Hdef main(argv=[_name_]):
   itf = oechem. OEInterface (InterfaceData, argv)
    # flag on command line indicates uncoloring option or not
   bUncolor = itf.GetBool("-uncolor")# optional unsaturated hetero bonds flag
   bUnsaturatedHeteroBonds = itf.GetBool("-unsatHetero")
    # optional user-specified SMARTS strings for substituents
   smartsSubstituentsString = itf.GetString("-smartsSubstituents")
    # optional user-specified SMARTS strings for substituents
   regionTypeString = itf.GetString("-regionType")
   options = oemedchem.OEBemisMurckoOptions()
   if bUnsaturatedHeteroBonds:
        options. SetUnsaturatedHeteroBonds (True)
```

```
if smartsSubstituentsString != "None":
    ss = oechem. OESubSearch()
    if (not ss. Init (smartsSubstituentsString)):
        oechem. OEThrow. Fatal ("Invalid SMARTS for subsearch.")
    options. SetSubstituentSearch (ss)
if len (regionTypeString) :
    options.SetRegionType(regionTypeString)
# input structure(s) to transform
ifsmols = occhem.oemolistream()if not ifsmols.open(itf.GetString("-i")):
    oechem.OEThrow.Fatal(
        "Unable to open %s for reading" %
        itf.GetString(''-i''))# save output structure(s) to this file
ofs = occhem.oemolostream()if not ofs.open(itf.GetString("-o")):
    oechem.OEThrow.Fatal(
        "Unable to open %s for writing" %
        itf.GetString("-o"))
if not oechem. OEIsSDDataFormat (ofs. GetFormat ()):
    oechem.OEThrow.Fatal(
        "Output file format does not support SD data: %s" %
        itf. Getsstring("-0")\text{irec} = 0ototal = 0frag = oechem. OEGraphMol()
for mol in ifsmols. GetOEGraphMols():
    \text{irec} += 1
    oechem.OEDeleteEverythingExceptTheFirstLargestComponent (mol)
    iter = oemedchem. OEGetBemisMurcko(mol, options)
    if not iter. IsValid():
        name = mol.getTitle()if not mol. GetTitle():
            name = 'Record' + str(irec)oechem. OEThrow. Warning ("%s: no perceived regions" % name)
        continue
    for bmregion in iter:
        # create a fragment from the perceived region
        oechem. OESubsetMol (frag, mol, bmregion, True)
        if bUncolor:
             # ignore 3D stereo parities
            if (fraq.GetDimension() == 3):
                fraq.SetDimension(0)
            # uncolor the fragment
            oechem.OEUncolorMol(fraq)
        smi = oechem.OEMolToSmiles(frag)
        # annotate the input molecule with the role information
        for role in bmregion. GetRoles () :
            oechem.OEAddSDData(mol, role.GetName(), smi)
    ototal += 1oechem.OEWriteMolecule(ofs, mol)
```

if not irec:

```
oechem. OEThrow. Fatal ('No records in input structure file to perceive')
    if not ototal:
        oechem. OEThrow. Warning ('No annotated structures generated')
    print ("Input molecules=\{0:d\}, output annotated \{1:s\}molecules=\{2:d\}"
          .format(irec, ("(uncolored) " if bUncolor else ""), ototal))
    return 0
if name == "_main_":
    sys.exit(main(sys.argv))
```

### 3.1.2 Apply ChEMBL solubility transformations

A utility that reads an input set of structures and outputs transformed structures along with annotations containing of the original data based on the matched pairs discovered from indexing solubility data from the [ChEMBL24-2018] data set.

#### See also:

• OEApplyChEMBL24SolubilityTransforms function

#### **Command Line Interface**

prompt> ChEMBLsolubility.py input.sdf output.sdf

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
# Utility to apply ChEMBL24 solubility transforms to an input set of structures
# ChEMBLsolubility.py [-i] input_mols [-o] output_mols
```

```
\int -verbose \int \int -context \int \frac{1}{2} \int \int -minpairs # 1
## input_mols: filename of molecules to transform based on analysis
# output_mols: filename to collect transformed molecules
# [-verbose]: optional flag to request verbose progress
# [-context #]: optional flag to request a specific chemistry context
# [-minpairs #]: optional flag to request a minimum number of pairs to apply_
\rightarrowtransforms
#######################################
from openeye import oechem
from openeye import oemedchem
import sys
#######################################
InterfaceData = """!BRIEF [-i] <infile1> [-o] <infile2> [ -verbose ] [ -context [0|2]] [ -minpairs # ]
!PARAMETER -i
  !ALIAS -in
  !ALIAS -input
  ! TYPE string
  !REQUIRED true
  !BRIEF Input file name
 !KEYLESS 1
!END
!PARAMETER -0
 !ALIAS -out
 !ALIAS -output
 !TYPE string
 !REQUIRED true
 !BRIEF Output file name
  !KEYLESS 2
! END
!PARAMETER -verbose
  !ALIAS -v
  !TYPE bool
  !DEFAULT false
 !BRIEF Verbose output
! END
!PARAMETER -context
 !ALIAS -c!TYPE string
 !DEFAULT 0
 !BRIEF Chemistry context for output
! END
!PARAMETER -minpairs 2
  !TYPE int
   !DEFAULT 0
  !BRIEF require at least -minpairs to apply the transformations (default: all)
! END
\overline{n}, \overline{n}, \overline{n}def main (argv=[\underline{\hspace{1cm}}name\underline{\hspace{1cm}}]):
   itf = oechem. OEInterface (InterfaceData, argy)
    verbose = itf. GetBool("-verbose")
```

```
(continued from previous page)
```

```
# input structure(s) to transform
   ifsmols = occhem.oemolistream()if not ifsmols.open(itf.GetString("-i")):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % itf. GetString ("-i"))
   # save output structure(s) to this file
   ofs = occhem.oemolostream()if not ofs.open(itf.GetString("-<math>o</math>")):oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-o"))
   # request a specific context for the transform activity, here 0-bonds
   chemctxt = oemedchem. OEMatchedPairContext_Bond0
   askcontext = itf.GetString("-context")[:1]if askcontext == '0':chemctxt = oemedchem. OEMatchedPairContext Bond0
   elif askcontext == '2':chemctxt = oemedchem.OEMatchedPairContext_Bond2
   Also:oechem. OEThrow. Fatal ("Invalid context specified: " +
                              askcontext + ", only 0|2 allowed")minpairs = itf.GetInt("-minpairs")
   if minpairs > 1 and verbose:
       print ('Requiring at least \{0:d\} matched pairs to apply transformations'.
\rightarrow format (minpairs))
   \text{irec} = 0\text{cent} = 0ototal = 0for mol in ifsmols. GetOEGraphMols():
       \text{irec} += 1oechem.OEDeleteEverythingExceptTheFirstLargestComponent (mol)
        iter = oemedchem.OEApplyChEMBL24SolubilityTransforms(mol, chemctxt, minpairs)
       if not iter. IsValid():
           name = mol.getTitle()if not mol. GetTitle():
                name = 'record ' + str(irec)oechem. OEThrow. Warning ("%s: did not produce any output" % name)
            continue
       ocnt = 0for outmol in iter:
           ocnt += 1oechem.OEWriteMolecule(ofs, outmol)
       if not ocnt:
            print ('Record', irec, 'No output generated')
            print (oechem. OEMolToSmiles (mol))
       else:
            ototal += contif verbose:
                print ('Record:', "{0:4d}".format(irec),
                       'transformation count=', "(0:6d)".format(ocnt),
                       'total mols=', "(0:7d)". format (ototal))
   if not irec:
       oechem. OEThrow. Fatal ('No records in input structure file to transform')
   if not ocnt:
```

```
oechem. OEThrow. Warning ('No transformed structures generated')
   print ("Input molecules={0:d} output molecules={1:d}".format (irec, ototal))
    return 0
if __name__ == "__main__".sys.exit(main(sys.argv))
```

## 3.1.3 Matched Pair analysis generation of a MMP index

A program that performs a matched pair analysis of a set of structures for indexing and saves the generated index file for subsequent loading and querying.

![](_page_23_Figure_5.jpeg)

Fig. 1: Schematic representation of the Matched Pair Analysis process

- OEMatchedPairAnalyzer class
- OEMatchedPairAnalyzerOptions class
- · OEMatchedPairApplyTransforms function

### **Command Line Interface**

prompt> CreateMMPIndex.py index.sdf output.mmpidx

#### **Code**

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
# Utility to perform a matched pair analysis on a set of structures
# and save the index for subsequent analysis
# -------------------------------------
# CreateMMPIndex.py index_mols output_index
# index_mols: filename of input molecules to analyze
# output index: filename of MMP index
#######################################
from openeye import oechem
from openeye import oemedchem
import sys
class FilterSDData:
   def __init_(self, fields, asFloating):
       if len(fields) == 1 and '-ALLSD' in fields[0].upper():
           self.fields = None
       elif len(fields) == 1 and '-CLEARSD' in fields[0].upper():
           self.fields = []else:self.fields = fields
       self.asFloating = asFloating
   def FilterMolData(self, mol):
       if not oechem. OEHasSDData (mol) :
           return 0
       if self. fields is None:
           return -1
```

```
if len(self.fields) == 0:
            oechem.OEClearSDData(mol)
            return 0
        validdata = 0deletefields = []for dp in oechem. OEGetSDDataPairs (mol) :
            tag = dp.GetTag()if tag not in self. fields:
                 deletefields.append(tag)
                 continue
            value = oechem. OEGetSDData (mol, tag)
            if self.asFloating:
                 try:
                     float (value)
                 except ValueError:
                     oechem. OEThrow. Warning ("Failed to convert %s to numeric value (
\leftrightarrow \frac{6}{5}S) in \frac{6}{5}S" \frac{6}{5}(tag, value, mol. GetTitle()))
                     deletefields.append(taq)
                     continue
            validdata += 1if not validdata:
            oechem.OEClearSDData(mol)
        else:
            for nuke in deletefields:
                 oechem.OEDeleteSDData(mol, nuke)
        return validdata
def MMPIndex(itf):
    # output index file
    mmpindexfile = itf.GetString("-output")
    if not oemedchem. OEIsMatchedPairAnalyzerFileType (mmpindexfile) :
        oechem. OEThrow. Fatal ("Output file is not a matched pair index type - \setminusneeds .mmpidx extension: {}"
                               .format(mmpindexfile))
    # create options class with defaults
    mmpopts = oemedchem.OEMatchedPairAnalyzerOptions()
    # set up options from command line
    if not oemedchem. OESetupMatchedPairIndexOptions (mmpopts, itf) :
        oechem. OEThrow. Fatal ("Error setting matched pair indexing options!")
    # input structures to index
    if since x = occhem.oemolistream()if not ifsindex.open(itf.GetString("-input")):
        oechem. OEThrow. Fatal ("Unable to open {} for reading"
                               .format(itf.GetString("-input")))
    # get requested verbosity setting
    verbose = itf.GetBool("-verbose")
    vverbose = itf.GetBool("-vverbose")
```

```
verbose = vverbose
   maxrec = max(itf.GetInt("maxrec"), 0)statusrec = itf.GetInt("-status")
   if itf.GetBool("-exportcompress"):
        if not mmpopts. SetOptions (mmpopts. GetOptions ()
                                   oemedchem.OEMatchedPairOptions_ExportCompression):
            oechem. OEThrow. Warning ("Error enabling export compression!")
   stripstereo = itf.GetBool("-stripstereo")
   stripsalts = itf.GetBool("-stripsalts")
   keepFields = []if itf.HasString("-keepSD"):
        for field in itf.GetStringList("-keepSD"):
            keepFields.append(field)
        if verbose:
            oechem. OEThrow. Info ('Retaining SD data fields: {}'. format (' '.
\rightarrowjoin(keepFields)))
   alldata = itf.GetBool("-allSD")cleardata = itf.GetBool("-clearSD")
   if keepFields:
        if verbose and (alldata or cleardata):
            oechem.OEThrow.Info("Option -keepSD overriding -allSD, -clearSD")
        alldata = Falsecleardata = False\text{elif} cleardata:
        alldata = Falseif verbose\cdotoechem. OEThrow. Info ("Forced clearing of all input SD data")
   elif alldata:
        if verbose:
            oechem. OEThrow. Info ("Retaining all input SD data")
        cleandata = Falseelif verbose:
        oechem. OEThrow. Info ("No SD data handling option specified, -allSD assumed")
   if cleardata:
       keepFields = ['-CLEARSD']elif alldata or not keepFields:
        keepFields = ['-ALLSD']if verbose:
        if not mmpopts. Has IndexableFragmentHeavyAtomRange():
            oechem. OEThrow. Info ("Indexing all fragments")
        else:
            oechem. OEThrow. Info ("Limiting fragment cores to \{0:2f\}-\{1:2f\}" of input,
\rightarrowmolecules"
                                 .format(mmpopts.GetIndexableFragmentRangeMin(),
                                         mmpopts.GetIndexableFragmentRangeMax()))
        if statusrec:
            oechem. OEThrow. Info ("Status output after every {0} records".
\rightarrow format (statusrec))
```

(continues on next page)

if vverbose:

```
if maxrec:
            oechem. OEThrow. Info("Indexing a maximum of \{0\} records". format (maxrec))
       if itf.GetBool("-exportcompress"):
            oechem. OEThrow. Info ("Removing singleton index nodes from index")
       if stripstereo:
            oechem. OEThrow. Info ("Stripping stereo")
       if stripsalts:
            oechem. OEThrow. Info ("Stripping salts")
       if itf.GetBool("-clearSD"):
            oechem. OEThrow. Info ("Clearing all input SD data")
       elif alldata:
            oechem. OEThrow. Info ("Retaining all input SD data")
       elif keepFields:
            oechem. OEThrow. Info ('Retaining floating point SD data fields: {}'
                                 .format(''.join(keepFields)))
   # create indexing engine
   mmp = oemedchem. OEMatchedPairAnalyzer (mmpopts)
   # interpret SD fields as floating point data
   validdata = FilterSDData (keepFields, True)
   # add molecules to be indexed
   record = 0unindexed = 0for mol in ifsindex. GetOEGraphMols():
       if not alldata:
            # filter the input molecule SD data based on allowed fields
            validdata. FilterMolData (mol)
       if stripsalts:
            oechem.OEDeleteEverythingExceptTheFirstLargestComponent(mol)
       if stripstereo:
            oechem.OEUncolorMol(mol,
                                 (oechem.OEUncolorStrateqy_RemoveAtomStereo |
                                  oechem.OEUncolorStrategy RemoveBondStereo
                                  oechem.OEUncolorStrategy_RemoveGroupStereo))
       status = mmp.AddMol(mol, record)
       if status != record:
            unindexed += 1if vverbose:
                oechem. OEThrow. Info ('Input structure not added to index, record=%d
\leftrightarrowstatus=\&s' \&(record, oemedchem.
\rightarrowOEMatchedPairIndexStatusName(status)))
       record += 1if maxrec and record >= maxrec:
           break
       if statusred and (record \frac{1}{6} statusred) == 0:
            oechem. OEThrow. Info("Records: {} Indexed: {} Unindexed: {}"
                                 .format (record, (record - unindexed), unindexed))
```

```
if not <math>mmp</math>. NumMols() :oechem. OEThrow. Fatal ('No records in index structure file')
    if not mmp. NumMatchedPairs():
        oechem. OEThrow. Fatal ('No matched pairs found from indexing, ' +
                              'use -fragGe,-fragLe options to extend indexing range')
   if not oemedchem. OEWriteMatchedPairAnalyzer (mmpindexfile, mmp) :
        oechem. OEThrow. Fatal ('Error serializing MMP index: {}'
                             .format(mmpindexfile))
    # return some status information
   oechem.OEThrow.Info("Records: {}, Indexed: {}, matched pairs: {:,d}"
                        .format (record,
                                mmp.NumMols(),
                                mmp.NumMatchedPairs()))
    return <sub>0</sub>#######################################
InterfaceData = ""# createmmpindex interface file
!CATEGORY CreateMMPIndex
    !CATEGORY I/O
        !PARAMETER -input 1
         !ALIAS -in
          !TYPE string
          !REQUIRED true
          !BRIEF Input filename of structures to index
          !KEYLESS 1
        LEND
        !PARAMETER -output 2
         !ALIAS -out
         !TYPE string
          !REQUIRED true
          !BRIEF Output filename for serialized MMP index
         !KEYLESS 2
        ! END
    ! END
    !CATEGORY indexing_options
        !PARAMETER -maxrec 1
           !TYPE int
           !DEFAULT 0
           !LEGAL RANGE 0 inf
           !BRIEF process at most -maxrec records from -input (0: all)
        LEND
        !PARAMETER -status 2
           !TYPE int
          !DEFAULT 0
          !LEGAL RANGE 0 inf
           !BRIEF emit progress information every -status records (0: off)
        ! END
        !PARAMETER -exportcompress 3
```

```
!TYPE bool
           !DEFAULT 0
           !BRIEF Whether to remove singleton nodes on export of the MMP index
           !DETAIL
                True indicates no additional structures will be added to the index
         ! END
         !PARAMETER -verbose 4
            !TYPE bool
            !DEFAULT 0
           !BRIEF generate verbose output
        LEND
         !PARAMETER -vverbose 5
            !TYPE bool
            !DEFAULT 0
           !BRIEF generate very verbose output
        ! END
    ! END
    !CATEGORY molecule_SDData
        !PARAMETER -allSD 1
            !TYPE bool
            !DEFAULT 0
            !BRIEF retain all input SD data
         LEND
        !PARAMETER -clearSD 2
            !TYPE bool
           !DEFAULT 0
           !BRIEF clear all input SD data
        LEND
        !PARAMETER -keepSD 3
            !TYPE string
            !LIST true
            !BRIEF list of SD data tags of floating point data to *retain* \
                   for indexing (all other SD data is removed)
        !END
    ! END
    !CATEGORY molecule_processing
        !PARAMETER -stripstereo 1
           !TYPE bool
           !DEFAULT 0
          !BRIEF Whether to strip stereo from -input structures
        ! END
        !PARAMETER -stripsalts 2
          !TYPE bool
           !DEFAULT 0
          !BRIEF Whether to strip salt fragments from -input structures
        !END
    !END
! END
\overline{n} \overline{n} \overline{n}def main(argv=[\underline{\hspace{1cm}}name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    oemedchem.OEConfigureMatchedPairIndexOptions(itf)
```

(continues on next page)

if not oechem. OEParseCommandLine(itf, argv):

```
(continued from previous page)
         oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MMPIndex(itf)
   {\rm __name}\_ = = "{\rm __main}\_".if
    sys.exit(main(sys.argv))
```

## 3.1.4 Matched Pair analysis using a multi-process generation of an MMP index

A program that performs a multi-process matched pair analysis of a set of structures for indexing and saves the generated index file for subsequent loading and querying. This example uses the python multiprocessing module.

![](_page_30_Figure_4.jpeg)

Fig. 2: Schematic representation of the Matched Pair Analysis process

- OEMatchedPairAnalyzer class
- OEMatchedPairAnalyzerOptions class
- · OEMatchedPairApplyTransforms function

#### **Command Line Interface**

prompt> CreateMMPIndexParallel.py [ -pool num\_processes ] index.sdf output.mmpidx

#### Code

#### **Download code**

CreateMMPIndexParallel.pv

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
# Utility to perform a matched pair analysis on a set of structures
# and save the index for subsequent analysis using python multiprocessing
# _____________________________________
# CreateMMPIndexParallel.py index_mols output_index
# index_mols: filename of input molecules to analyze
# output_index: filename of MMP index
#######################################
import sys
import os
import random
import multiprocessing
from tempfile import NamedTemporaryFile
from itertools import islice, chain, repeat
from openeye import oechem
from openeye import oemedchem
BADIDS = []
# globals for slave processes
MMP_INDEX_OPTIONS = 'parallel_mmp_indexing.mmpidx'
OPTIONS_FILE = 'parallel_mmp_options.txt'
```

```
(continued from previous page)
```

```
def chunk_pad(it, size, padval=None) :
    it = chain(iter(it), repeat(padval))
    return iter (lambda: tuple (islice (it, size)), (padval,) * size)
# MMP index saving is memory intensive - (optional) lock around index serialization
# global definition of write lock
write\_lock = Nonedef global_write_lock(lck):
   global write_lock
   write lock = lckclass CustomOEErrorHandler (oechem. OEErrorHandlerImplBase) :
    def __init_(self, nowarning):
        oechem.OEErrorHandlerImplBase.__init__(self)
        self.log = str()self.nowarning = nowarningdef Msg(self, level, msg):
        if level == oechem. OEErrorLevel_Error or level == oechem. OEErrorLevel_Fatal:
            self.log += "Preventing call to exit: \{\theta\}n".format(msq)
            print("{}: {}".format(oechem.OEErrorLevelToString(level), msq))
            sys.exit(1)elif level == oechem. OEErrorLevel_Verbose:
            self.log += "Verbose: \{0\}\n".format(msg)
        elif level == oechem. OEErrorLevel_Warning:
            if not self. nowarning:
                self.log += "Warning: \{0\}\n".format(msg)
        else:
            # Info records are not retained
            print ("{}: {}".format(oechem.OEErrorLevelToString(level), msg))
   def GetLoq(self):
        return self.log
   def CreateCopy(self):
        return CustomOEErrorHandler()._disown_()
class FilterSDData:
    def __init_(self, fields, asFloating):
        if len(fields) == 1 and '-ALLSD' in fields[0].upper():
            self.fields = Noneelif len(fields) == 1 and '-CLEARSD' in fields[0].upper():
            self.fields = []else:
            self.fields = fields
        self.asFloating = asFloating
    def FilterMolData(self, mol):
        if not oechem. OEHasSDData (mol) :
```

```
return 0
        if self. fields is None:
            return -1if len(self.fields) == 0:
            oechem.OEClearSDData(mol)
            return 0
        validdata = 0deletefields = []for dp in oechem. OEGetSDDataPairs (mol) :
            tag = dp.GetTag()if tag.upper() not in self.fields:
                 deletefields.append(tag)
                 continue
            value = oechem. OEGet SDData (mol, tag)if self.asFloating:
                 try:
                     float (value)
                 except ValueError:
                     oechem. OEThrow. Warning ("Failed to convert \{ \} to numeric value \{ \}\leftrightarrow) in \{\}"
                                              .format(tag, value, mol.GetTitle()))
                     deletefields.append(tag)
                     continue
            validdata += 1if not validdata:
            oechem.OEClearSDData(mol)
        else:
            for nuke in deletefields:
                 oechem.OEDeleteSDData(mol, nuke)
        return validdata
def mmp_index_mols(args):
    idx\_opts_fname = args[0]opts_{\text{}}fname = args[1]mol_db_fname = args[2]check_pt_recs = args[3]idx\_opts = oemedchem.OEMatchedPairAnalyizer()if not oemedchem. OEReadMatchedPairAnalyzer(idx_opts_fname, idx_opts):
        oechem. OEThrow. Error ("Unable to read index file for options: \{\theta\}". format (idx_
\rightarrow opts))
        return False
    keepSD = []allSD = 1 # default
    clearSD = 0statusrec = 0stripstereo = 0
```

```
(continued from previous page)
```

```
stripsalts = 0dataasfloating = 1 # default
   slave\_verbose = 0slave_vverpose = 0nowarnings = 0with open (opts_fname, "rt") as OPTS:
       for line in OPTS:
           line = line.start(p() upper()vals = line.split('=')
           if 'KEEPFIELDS' in vals[0]:
               keepSD = vals[1].split(','')allSD = FalseclearSD = Falseelif 'STATUS' in vals[0]:
                statusrec = int(vals[1])elif 'STEREO' in vals[0]:
                stripstereo = int(vals[1])elif 'SALTS' in vals[0]:
                stripsalts = int(vals[1])elif 'ALLDATA' in vals[0]:
                allSD = int(vals[1])clearSD = not allSD
            elif 'ASFLOATING' in vals[0]:
                dataasfloating = int(vals[1])elif 'VERBOSE' in vals[0]:
                slave_verbose = int(vals[1])elif 'VVERBOSE' in vals[0]:
                slave_vverbase = int(vals[1])if slave_vverbose:
                    slave_verbose = slave_vverbose
            elif 'NOWARNINGS' in vals[0]:
                nowarnings = int(vals[1])handler = CustomOEErrorHandler(nowarnings)
   QW</math> and = <math>F</math>oechem.OEThrow.SetHandlerImpl(handler, owned)
   if allSD:
       keepSD = ['-ALLSD']if clearSD:
       keepSD = ['-CLEARSD']mol = occhem. OEGraphMol()moldb = occhem. OEMolDatabase()
   if not moldb. Open (mol_db_fname) :
       oechem. OEThrow. Error ("Unable to open molecule database: {0}". format (mol_db_
\rightarrowfname))
       return False
   # interpret floating point data if requested
   validdata = FilterSDData(keepSD, dataasfloating)
   # CREATE the index using the passed options template
   mmpidx = oemedchem.OEMatchedPairAnalyzer(idx_opts.GetOptions())
```

```
num_{mols} = 0CHECK_POINT_FILE = None
   if check_pt_recs > 0:
       CHECK_POINT_FILE = NamedTemporaryFile(prefix="checkpoint_", suffix='.mmpidx',..
\rightarrowdelete=False)
   mmpidxEXT = ' .mmpidx'# GENERATE a tempfile name to return the serialized index
   with NamedTemporaryFile(prefix="slave_", suffix=mmpidxEXT, delete=False) as MMP_
\rightarrow OUT_IDX:
       unindexed = 0\ttimer = occhem. OEStopwatch()
       numrec = 0for molid in args[4:]:
            # end of list may be padded with None
            if molid is None:
                break
            numrec += 1idx = int(molid)if not moldb. GetMolecule (mol, idx) :
                oechem. OEThrow. Warning ('Error retrieving record=\{0\}'. format(idx))
                continue
            if mol. GetTitle() and mol. GetTitle in BADIDS:
                oechem. OEThrow. Warning ('{}: skipping bad structure: {}'. format (idx, _
\rightarrowmol.GetTitle()))
                continue
            if not allSD:
                # filter the input molecule based on "keeper" SD data fields
                validdata. FilterMolData (mol)
            if stripsalts:
                oechem.OEDeleteEverythingExceptTheFirstLargestComponent (mol)
            if stripstereo:
                oechem.OEUncolorMol(mol,
                                      (oechem.OEUncolorStrategy_RemoveAtomStereo |
                                       oechem.OEUncolorStrategy_RemoveBondStereo))
            # add molecule to the index
            status = mmpidx.AddMol(mol, idx)
            if status == idx:
                num\_mols += 1else:
                oechem. OEThrow. Warning ('Error indexing molecule {}: {}: {}'
                                         .format(idx, oemedchem.
\rightarrowOEMatchedPairIndexStatusName(status),
                                                 mol.GetTitle()unindexed += 1if statusrec > 0 and (numrec \frac{1}{6} statusrec) == 0:
                if slave_verbose:
```

```
oechem.OEThrow.Info('Records: {}, Indexed: {}, Unindexed: {},
\rightarrowIndexing rate: \{f:IF\} mol/sec'
                                         .format (numrec, num_mols, unindexed,
                                                  float(numrec) / timer.Elapped())Also:oechem. OEThrow. Info('Records: {}, Indexed: {}, Unindexed: {}'
                                         .format (numrec, num_mols, unindexed))
            if check_pt_recs > 0 and (numrec % check_pt_recs) == 0:
                oechem.OEThrow.Info('Records: {}, Checkpointing: {}'
                                     .format (numrec, CHECK_POINT_FILE.name))
                if write_lock is not None:
                    write_lock.acquire()
                bcheckpt = oemedchem.OEWriteMatchedPairAnalyzer(CHECK_POINT_FILE.name,
\leftrightarrow mmpidx)
                if write_lock is not None:
                    write_lock.release()
                oechem.OEThrow.Info('Records: {}, Checkpointed: {}'
                                     .format (numrec, CHECK_POINT_FILE.name))
        if CHECK POINT FILE is not None:
            CHECK_POINT_FILE.close()
        if slave_vverbose:
            oechem. OEThrow. Info('Records: {}, serialization in progress... {}'
                                 .format (numrec, MMP_OUT_IDX.name))
        bcheckpt = oemedchem.OEWriteMatchedPairAnalyzer(MMP_OUT_IDX.name, mmpidx)
        if slave_vverbose:
            oechem. OEThrow. Info('Records: {}, serialization complete.'
                                 .format (numrec))
        if bcheckpt:
            if CHECK_POINT_FILE is not None:
                os.remove(CHECK_POINT_FILE.name)
        else:
            return (False, None, unindexed, handler. GetLoq())
        return (True, MMP_OUT_IDX.name, unindexed, handler.GetLog())
def MMPIndex(itf):
    # input structures to index
   MOL_DB_IDX = itf.GetString("-input")
   verbose = itf. GetBool("-verbose")vverbose = itf.GetBool("-vverbose")
    if vverbose:
        verbose = True# create the moldatabase index on the input structures so the slaves can access it
   if not oechem. OECreateMolDatabaseIdx (MOL_DB_IDX) :
        oechem. OEThrow. Fatal ("Unable to generate molecule database for {}"
                              .format(itf.GetString("-input")))
    # output index file
    mmpindexfile = itf.GetString("-output")
    if not oemedchem. OEIsMatchedPairAnalyzerFileType (mmpindexfile) :
```

```
oechem. OEThrow. Fatal ("Output file is not a matched pair index type - needs \
                              .mmpidx extension: \{ \}"
                              .format(mmpindexfile))
   moldb = oechem.OEMolDatabase()
   if not moldb. Open (MOL DB IDX) :
        oechem. OEThrow. Fatal ("Unable to open molecule database: {}"
                              .format (MOL DB_IDX))
    # create options class with defaults
   opts = oemedchem. OEMatchedPairAnalyzerOptions()
    # setup options from command line
   if not oemedchem. OESetupMatchedPairIndexOptions (opts, itf):
        oechem. OEThrow. Fatal ("Error setting matched pair indexing options!")
   if verbose:
        if not opts.HasIndexableFragmentHeavyAtomRange():
            oechem. OEThrow. Info ("Indexing all fragments")
        else:
            oechem. OEThrow. Info ("Limiting fragment cores to (0:2f) - (1:2f) & of input.
\leftrightarrowmolecules"
                                 .format(opts.GetIndexableFragmentRangeMin(),
                                          opts.GetIndexableFragmentRangeMax()))
   if (opts. GetOptions () &
            oemedchem.OEMatchedPairOptions_UniquesOnly) != 0 and itf.GetInt("-pool") !
ightharpoonup = 1:
        if not itf.GetBool("-uniqueinput"):
            oechem. OEThrow. Warning ("Disabling uniqueness check for multi-process
\rightarrowindexing, use -uniqueinput instead")
        if not opts. SetOptions (opts. GetOptions () & ~oemedchem. OEMatchedPairOptions_
\rightarrowUniquesOnly):
            oechem. OEThrow. Fatal ("Error disabling indexer -unique option")
    # create indexing engine
   mmpidx = oemedchem. OEMatchedPairAnalyzer (opts)
    # dump the index so the slaves can load the options from it
   if not oemedchem. OEWriteMatchedPairAnalyzer (MMP_INDEX_OPTIONS, mmpidx) :
        oechem. OEThrow. Fatal ("Unable to serialize index for %s" % MMP INDEX OPTIONS)
   maxrecOPT = max(itf.GetInt("maxrec"), 0)checkptrec = itf.GetInt("-checkpoint")
   statusrec = itf.GetInt("-status")
   stripstereo = itf.GetBool("-stripstereo")
   if stripstereo and verbose:
        oechem. OEThrow. Info ("Stripping stereo")
   stripsalts = itf.GetBool("-stripsalts")
   if stripsalts and verbose:
       oechem. OEThrow. Info ("Stripping salts")
   keepFields = []if itf.HasString("-keepSD"):
       for field in itf. GetStringList ("-keepSD"):
```

```
(continued from previous page)
```

```
keepFields.append(field)
        if verbose:
            oechem. OEThrow. Info ('Retaining SD data fields: {}'. format (' '.
\rightarrowjoin(keepFields)))
   alldata = itf.GetBool("-allSD")cleandata = itf.GetBool("-clearSD")if keepFields:
       if verbose and (alldata or cleardata):
            oechem.OEThrow.Info("Option -keepSD overriding -allSD, -clearSD")
        alldata = Falsecleandata = Falseelif cleardata:
       alldata = Falseif verbose:
            oechem. OEThrow. Info ("Forced clearing of all input SD data")
   Also:if verbose:
            if not alldata:
                oechem.OEThrow.Info("No SD data handling option specified, -allSD.
\leftrightarrowassumed")
            Also:oechem. OEThrow. Info ("Retaining all input SD data")
        alldata = Truecleandata = Falsewith open (OPTIONS FILE, "wt") as WRITE OPTS:
        if cleardata:
            \texttt{WRITE\_OPTS}.\texttt{write('ALLDATA=0}\n',\texttt{)}elif alldata:
            WRITE_OPTS.write('ALLDATA=1\n')
        elif keepFields:
            WRITE_OPTS. write('KEEPFIELDS=f0)\n n'.format(','.join(keepFields)))WRITE_OPTS.write('STATUS={0}\n'.format(statusrec))
        if stripstereo:
            WRITE_OPTS.write('STEREO=1\n')
        if stripsalts:
           WRITE_OPTS.write('SALTS=1/n')if verbose:
           WRITE OPTS.write('VERBOSE=1\n')
        if vverbose:
            WRITE_OPTS.write('VVERBOSE=1/n')if itf.GetBool("-nowarnings"):
            WRITE OPTS.write('NOWARNINGS=1\n')
    # get list of record ids
   if not maxrecOPT:
       maxrec = moldb.GetMaxMolIdx()else:maxrec = maxrecOPTif not itf.GetBool("-uniqueinput"):
       molids = [i \text{ for } i \text{ in } range(0, maxrec)]else:
       mol = occhem.OEGraphMol()umols = set()
```

```
molids = []for i in range (0, maxrec):
            if not moldb. GetMolecule (mol, i) :
                continue
            if stripsalts:
                oechem.OEDeleteEverythingExceptTheFirstLargestComponent(mol)
            if stripstereo:
                oechem.OEUncolorMol(mol,
                                     (oechem.OEUncolorStrategy_RemoveAtomStereo |
                                      oechem.OEUncolorStrategy_RemoveBondStereo))
            smi = occhem.OEMo1ToSmiles(mol)if smi in umols:
                continue
            umols.add(smi)
           molids.append(i)
   if maxrecOPT and verbose:
       oechem. OEThrow. Info ("Indexing a maximum of {} records"
                             .format(len(molids)))
   nrprocesses = itf.GetInt("-pool")
   if not nrprocesses:
       nrprocesses = oechem. OEGetNumProcessors()
   # identify warning handling, etc
   if verbose:
       if itf.GetBool("-exportcompress"):
            oechem. OEThrow. Info ("Removing singleton index nodes from index")
       if not itf.GetInt("-pool"):
            oechem. OEThrow. Info ("Using the maximum number of processes allowed ({})".
\rightarrow format (nrprocesses))
       else:
            oechem. OEThrow. Info("Limiting indexing to \{ \} process (es)".
\rightarrow format (nrprocesses))
       if itf.GetBool("-nowarnings"):
           oechem. OEThrow. Info ("Suppressing warnings during indexing")
       else:
            oechem. OEThrow. Info ("Emitting warnings during indexing")
   # randomize indices to avoid pathologicals near each other
   if not itf.GetBool("-randomize"):
       if verbose:
            oechem. OEThrow. Info ("Sequentially processing input records for indexing")
   else:
       if verbose:
            oechem. OEThrow. Info ("Randomizing input records for indexing")
       random.shuffle(molids)
   if checkptrec:
       oechem. OEThrow. Info ("Checkpointing indices after every {0} records"
                             .format(checkptrec))
   if statusrec:
       oechem. OEThrow. Info ("Status output after every {0} records"
```

```
(continued from previous page)
```

```
.format(statusrec))
   test_input = list(chunk_pad(molids,
                                 int ((len(molids) / nrprocesses) + (len(molids) \frac{1}{6}\rightarrownrprocesses))))
   # prepend the filenames to for loading and extraction index options
   test_input = [[MMP_INDEX_OPTIONS, OPTIONS_FILE, MOL_DB_IDX, checkptrec]
                  + list(i) for i in test_input]
   # begin molecule indexing
   timer = oechem.OEStopwatch()
   # creating the indexing pool - (optional)
   # lock can limit index serialization to ONE process at a time
   # mlock = multiprocessing. Lock()
   mlock = Noneprocesses = multiprocessing. Pool(nrprocesses, initializer=qlobal_write_lock,...
\rightarrowinitargs=(mlock,))
   errs = Noneif itf.GetBool("-nowarnings"):
       errs = oechem. oeosstream()oechem.OEThrow.SetOutputStream(errs)
   results = []for i, res in enumerate (processes.imap_unordered(mmp_index_mols, test_input)):
       results.append(res)
   processes.close()
   # restore OEThrow output
   oechem.OEThrow.SetOutputStream(oechem.oeout)
   # capture indexing time
   tIndexing = timer.Elapsed()
   mmpidx = oemedchem.OEMatchedPairAnalyizer()# walk the results and read in the indexed segments for the input molecules
   unindexed = 0for res in results:
       (status, idxfile, seg_unindexed, log) = res
       if vverbose:
            oechem. OEThrow. Info('status: {0} index: {1} unindexed: {2}'
                                 .format(status, idxfile, seg_unindexed))
       if verbose and log:
            oechem.OEThrow.Info(log)
       if not status:
            continue
       curmols = mmpidx.WumMols()\text{cummps} = \text{mmpidx}.\text{NumMatchedPairs}()mergetimer = occhem.OEstopwatch()if not oemedchem. OEReadMatchedPairAnalyzer(idxfile, mmpidx, True):
```

```
oechem. OEThrow. Warning ('Error reading {}'. format (idxfile))
        if errs is not None:
            errs.clear()
        os.remove(idxfile)
        if vverbose:
            oechem. OEThrow. Info("{0}: {1:.2F} sec added mols: {2:, } added unindexed:
\rightarrow {3:, } added mmps: {4:,} "
                                  .format(idxfile, mergetimer.Elapsed(),
                                          mmpidx.MumMols() - curmols,seg_unindexed,
                                          mmpidx.NumMatchedPairs() - curmmps))
        unindexed += seg_unindexed
    # capture index merge time
   tMerging = timer.Elapsed() - tIndexingif not mmpidx.NumMols():
        oechem. OEThrow. Fatal ('No records in index structure file')
   if not mmpidx.NumMatchedPairs() or unindexed == maxrec:
        oechem. OEThrow. Fatal ('No matched pairs found from indexing, ' +
                              'use -fragGe,-fragLe options to extend index range')
   numrec = len(molids)if verbose:
       oechem. OEThrow. Info ("Indexing time: \{0:2F\} indexing rate: \{1:2F\} mol/sec"
                             . format (tIndexing, float (numrec) / tIndexing))
       oechem. OEThrow. Info("Index merge time: \{0:.2F\} indexing merge rate: \{1:.2F\}_n\leftarrow \text{mol}/\text{sec}"
                             .format(tMerging, float(numrec) / tMerging))
        oechem. OEThrow. Info ("Total time: {0:.2F} total rate: {1:.1F} mol/sec"
                             .format(timer.Elapsed(), float(numrec) / timer.Elapsed()))
    # return some status information
   oechem. OEThrow. Info ("Records: {}, Indexed: {}, matched pairs: {: d}"
                         .format (numrec,
                                 mmpidx.NumMols(),
                                 mmpidx.NumMatchedPairs()))
   if itf.GetBool("-exportcompress"):
       if not mmpidx. ModifyOptions (oemedchem. OEMatchedPairOptions_ExportCompression,
\leftrightarrow 0) :
            oechem. OEThrow. Warning ("Error enabling export compression!")
    # export merged index
   if not oemedchem. OEWriteMatchedPairAnalyzer(mmpindexfile, mmpidx):
        oechem. OEThrow. Fatal ('Error serializing MMP index: {}'. format (mmpindexfile))
   # cleanup
   try:
       os.remove(MMP_INDEX_OPTIONS)
   except OSError:
       pass
   try:
       os.remove(OPTIONS_FILE)
```

```
pass
    # remove the moldatabase index on the input structures
   try:
       os.remove(oechem.OEGetMolDatabaseIdxFileName(MOL_DB_IDX))
   except OSError:
       pass
   return 0#######################################
InterfaceData = ""# createmmpindexparallel interface file
!CATEGORY CreateMMPIndexParallel
    !CATEGORY T/O
       !PARAMETER -input 1
         !ALIAS -in
          !TYPE string
          !REQUIRED true
         !BRIEF Input filename of structures to index
         !KEYLESS 1
       ! END
       !PARAMETER -output 2
         !ALIAS -out
         !TYPE string
         !REQUIRED true
         !BRIEF Output filename for serialized MMP index
         !KEYLESS 2
       ! END
    ! END
    !CATEGORY indexing options
       !PARAMETER -maxrec 1
          !TYPE int
          !DEFAULT 0
          !LEGAL RANGE 0 inf
          !BRIEF process at most -maxrec records from -input (0: all)
       ! END
        !PARAMETER -status 2
          !TYPE int
          !DEFAULT 0
          !LEGAL RANGE 0 inf
          !BRIEF emit progress information every -status records (0: off)
        ! END
        !PARAMETER -pool 3
          !TYPE int
          !DEFAULT 0
          !LEGAL RANGE 0 inf
          !BRIEF sets the number of parallel workers, \
                  (0: use value returned from OEGetNumProcessors())
        ! END
        !PARAMETER -uniqueinput 4
         !TYPE bool
```

(continues on next page)

except OSError:

```
!DEFAULT 0
          !BRIEF discard duplicate input structures after -stripsalts, -stripstereo_
\leftrightarrowactivities
        ! END
        !PARAMETER -exportcompress 5
         !TYPE bool
          !DEFAULT 0
          !BRIEF Whether to remove singleton nodes on export of the MMP index
         IDETATL
              True indicates no additional structures will be added to the index
        LEND
        !PARAMETER -randomize 6
          !TYPE bool
          !DEFAULT 0
          !BRIEF randomize input records
       ! END
        !PARAMETER -checkpoint 7
          !TYPE int
          !LEGAL_RANGE 0 inf
           !DEFAULT 0
          !BRIEF checkpoint the index segments every -checkpoint records
        ! END
        !PARAMETER -verbose 8
          !TYPE bool
          !DEFAULT 0
          !BRIEF generate verbose output
        LEND
        !PARAMETER -vverbose 9
          !TYPE bool
          !DEFAULT 0
          !BRIEF generate very verbose output
       ! END
   !END
   !CATEGORY molecule_SDData
       !PARAMETER -allSD 1
          !TYPE bool
          !DEFAULT 0
          !BRIEF retain all input SD data
       ! END
        !PARAMETER -clearSD 2
          !TYPE bool
          !DEFAULT 0
          !BRIEF clear all input SD data
       LEND
        !PARAMETER -keepSD 3
          !TYPE string
           !LIST true
          !BRIEF list of SD data tags of floating point data to \
                 *retain* for indexing (all other SD data is removed)
       ! END
   ! END
   !CATEGORY molecule processing
       !PARAMETER -stripstereo 1
          !TYPE bool
          !DEFAULT 0
```

```
(continued from previous page)
```

```
!BRIEF Whether to strip stereo from -input structures
         ! END
         !PARAMETER -stripsalts 2
           !TYPE bool
           !DEFAULT 0
           !BRIEF Whether to strip salt fragments from -input structures
         !\,\mathsf{END}\,!PARAMETER -nowarnings 3
            !TYPE bool
            !DEFAULT 1
            !BRIEF suppress warning messages from reading -input (default: True)
         ! END
    !END
!END
H/H/Hdef main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    oemedchem.OEConfigureMatchedPairIndexOptions(itf)
    if not oechem. OEParseCommandLine(itf, argv):
         oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MMPIndex(itf)
if name == " main ":
    sys.exit(main(sys.argv))
```

### 3.1.5 Matched Pair analysis using a multi-threaded generation of a MMP index

A program that performs a multi-threaded matched pair analysis of a set of structures for indexing and saves the generated index file for subsequent loading and querying.

See also:

- OEMatchedPairAnalyzer class
- OEMatchedPairAnalyzerOptions class
- · OEMatchedPairApplyTransforms function

#### **Command Line Interface**

prompt> CreateMMPIndexThreaded.py [ -threads num\_threads ] index.sdf output.mmpidx

![](_page_45_Figure_1.jpeg)

Fig. 3: Schematic representation of the Matched Pair Analysis process

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
# Utility to perform a matched pair analysis on a set of structures
# and save the index for subsequent analysis using a multithreaded API
# CreateMMPIndexThreaded.py index_mols output_index
# index_mols: filename of input molecules to analyze
# output index: filename of MMP index
######################################
```

```
from openeye import oechem
from openeye import oemedchem
import sys
def MMPIndex(itf):
    # checking input structures
    if since x = occhem.oemolistream()if not ifsindex.open(itf.GetString("-input")):
        oechem. OEThrow. Fatal ("Unable to open {} for reading"
                              .format(itf.GetString("-input")))
   ifsindex.close()
   verbose = itf.GetBool("-verbose")
   vverbose = itf.GetBool("-vverbose")
   if vverbose:
        verbose = True# output index file
    mmpindexfile = itf.GetString("-output")if not oemedchem. OEIsMatchedPairAnalyzerFileType (mmpindexfile) :
        oechem. OEThrow. Fatal ("Output file is not a matched pair index type - \setminusneeds .mmpidx extension: {}" .format(mmpindexfile))
    # create options class with defaults
   mmpopts = oemedchem. OEMatchedPairAnalyzerOptions()
    # set up options from command line
    if not oemedchem. OESetupMatchedPairIndexOptions(mmpopts, itf):
        oechem. OEThrow. Fatal ("Error setting matched pair indexing options!")
    if verbose:
        if not mmpopts. Has IndexableFragment HeavyAtomRange ():
            oechem. OEThrow. Info ("Indexing all fragments")
        else:
            oechem. OEThrow. Info ("Limiting fragment cores to \{0:2f\}-\{1:2f\} of input,
\leftarrowmolecules"
                                 .format(mmpopts.GetIndexableFragmentRangeMin(),
                                         mmpopts.GetIndexableFragmentRangeMax()))
    if itf.GetInt("-maxrec") and verbose:
        oechem. OEThrow. Info ("Indexing a maximum of {} records"
                             .format(itf.GetInt("-maxrec")))
    if itf.GetBool("-exportcompress"):
        if verbose:
            oechem. OEThrow. Info ("Removing singleton index nodes from index")
        if not mmpopts. SetOptions (mmpopts. GetOptions () |
                                   oemedchem.OEMatchedPairOptions ExportCompression):
            oechem. OEThrow. Warning ("Error enabling export compression!")
    # set indexing options
    indexopts = oemedchem.OECreateMMPIndexOptions(mmpopts)
    # set requested verbosity setting
    if vverbose:
        indexopts.SetVerbose(2)
```

elif verbose:

(continued from previous page)

```
indexopts. SetVerbose(1)
    # limit number of records to process
   indexopts. SetMaxRecord(itf.GetInt("-maxrec"))
   # set number of threads to use
   indexopts. SetNumThreads(itf.GetInt("-threads"))
   if verbose:
       if not indexopts. GetNumThreads():
            oechem. OEThrow. Info ("Using the maximum number of threads available")
       else:
            oechem. OEThrow. Info ("Limiting indexing to {} thread(s)"
                                 .format(indexopts.GetNumThreads()))
   errs = Noneif itf.GetBool("-nowarnings"):
       errs = oechem. oeosstream()oechem.OEThrow.SetOutputStream(errs)
   if verbose:
       oechem. OEThrow. Info ("Threaded indexing of {}, all SD data will be preserved".
\rightarrow format (itf. GetString ("-input")))
   # create index
   index status = oemedchem.OECreate MMPIndexFile (mmpindexfile,itf.GetString("-input"),
                                                   indexopts)
   dupes = 0if errs is not None:
       oechem.OEThrow.SetOutputStream(oechem.oeout)
       for err in errs.str().decode().split('\n'):
            err = err.rstrip()if not err:
                continue
            if verbose:
                oechem.OEThrow.Info(err)
            if 'ignoring duplicate molecule, ' in err:
                dupes += 1if not indexstatus. IsValid():
       oechem. OEThrow. Fatal ('Invalid status returned from indexing!')
   if not indexstatus. GetTotalMols():
       oechem. OEThrow. Fatal ('No records in index structure file: {}'
                              .format(itf.GetString("-input")))
   if dupes:
       oechem. OEThrow. Info('Found {} duplicate structures during indexing'
                             .format (dupes))
   if not indexstatus. GetNumMatchedPairs():
       oechem. OEThrow. Fatal ('No matched pairs found from indexing, ' +
                              'use -fragGe,-fragLe options to extend indexing range')
    # return some status information
```

```
oechem. OEThrow. Info ("Records: {}, Indexed: {}, matched pairs: \{f, d\}"
                        .format(indexstatus.GetTotalMols(),
                                indexstatus.GetNumMols(),
                                indexstatus.GetNumMatchedPairs()))
    return 0
######################################
InterfaceData = ""# createmmpindexthreaded interface file
!CATEGORY CreateMMPIndexThreaded
    !CATEGORY I/O
       !PARAMETER -input 1
         !ALIAS -in
         !TYPE string
         !REQUIRED true
         !BRIEF Input filename of structures to index
          !KEYLESS 1
        !END
       !PARAMETER -output 2
         !ALIAS -out
         !TYPE string
         !REQUIRED true
         !BRIEF Output filename for serialized MMP index
         IKEYLESS<sub>2</sub>
        !END
   ! END
    !CATEGORY indexing_options
        !PARAMETER -maxrec 1
          !TYPE int
           !DEFAULT 0
           !LEGAL RANGE 0 inf
          !BRIEF process at most -maxrec records from -input (0: all)
        ! END
        !PARAMETER -threads 2
          !TYPE int
          !DEFAULT 0
          !LEGAL RANGE 0 inf
          !BRIEF limit number of indexing threads to -threads (0:default)
        LEND
        !PARAMETER -exportcompress 3
          !TYPE bool
          !DEFAULT 0
          !BRIEF Whether to remove singleton nodes on export of the MMP index
          !DETATL
               True indicates no additional structures will be added to the index
        LEND
        !PARAMETER -nowarnings 4
          !TYPE bool
          !DEFAULT 1
          !BRIEF suppress warning messages from indexing -input (default: True)
        ! END
        !PARAMETER -verbose 5
```

```
!TYPE bool
             !DEFAULT 0
             !BRIEF generate verbose output
          ! END
          !PARAMETER -vverbose 6
             !TYPE bool
             !DEFAULT 0
             !BRIEF generate very verbose output
         LEND
     ! END
!END
\mathbf{u},\mathbf{u},\mathbf{u}def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    oemedchem.OEConfigureMatchedPairIndexOptions(itf)
    if not oechem. OEParseCommandLine(itf, argv):
         oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MMPIndex(itf)
if _name_ == "_main_":
     sys.exit(main(sys.argv))
```

## 3.1.6 Matched Pair analysis and transformations

A program that loads a previously generated Matched Pair index, then reads an input set of structures and outputs transformed structures based on the matched pairs discovered during indexing.

- OEMatchedPairAnalyzer class
- OEMatchedPairAnalyzerOptions class
- OEMatchedPairApplyTransforms function

![](_page_50_Figure_1.jpeg)

Fig. 4: Schematic representation of the Matched Pair Analysis process

#### **Command Line Interface**

```
prompt> MatchedPairTransform.py -mmpidx index.mmpidx -input input.sdf -output output.
\rightarrowsdf
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
# Utility to load a previously generated MMP index
  and use the transformations discovered to alter a second set of structures
# MatchedPairTransform.py mmp_index input_mols output_mols
3.1. OEMedChem TK Examples
                                                                                 45
   mp_index: filename of matched pair index
# input_mols: filename of molecules to transform based on analysis
# output_mols: filename to collect transformed molecules
######################################
```

```
oechem. OEThrow. Fatal ("Unable to load index / }". format (mmpimport))
   if not mmp. NumMols():
       oechem. OEThrow. Fatal ('No records in loaded MMP index file: { }'.
\rightarrowformat (mmpimport))
   if not mmp. NumMatchedPairs():
       oechem. OEThrow. Fatal ('No matched pairs found in MMP index file, ' +
                              'use -fragGe,-fragLe options to extend indexing range')
   # output (transformed) structure(s)
   ofs = occhem.oemolostream()if not ofs.open(itf.GetString("-output")):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" %
                             itf.GetString("-output"))
   # request a specific context for the transform activity, here 0-bonds
   chemctxt = oemedchem.OEMatchedPairContext_Bond0
   askcontext = itf.GetString("-context") [ : 1]if askcontext == '0':chemctxt = oemedchem. OEMatchedPairContext_Bond0
   elif askcontext == '1':chemctxt = oemedchem. OEMatchedPairContext Bond1
   elif askcontext == '2':chemctxt = oemedchem. OEMatchedPairContext_Bond2
   elif askcontext == '3':chemctxt = oemedchem. OEMatchedPairContext_Bond3
   elif askcontext == 'a' or askcontext == 'A':
       chemctxt = oemedchem. OEMatchedPairContext_AllBonds
   else:
       oechem. OEThrow. Fatal ("Invalid context specified: " +
                              askcontext + ", only 0|1|2|3|A allowed")
   verbose = itf.GetBool("-verbose")
   # return some status information
   if verbose:
       oechem.OEThrow.Info("{}: molecules: {:d}, matched pairs: {:,d}"
                             .format (mmpimport,
                                     mmp. NumMols(),
                                     mmp.NumMatchedPairs()))
   minpairs = itf.GetInt("-minpairs")
   if minpairs > 1 and verbose:
        oechem. OEThrow. Info ('Requiring at least %d matched pairs to apply_
\rightarrowtransformations'
                             % minpairs)
   errs = Noneif itf.GetBool("-nowarnings"):
       errs = oechem.oeosstream()
       oechem.OEThrow.SetOutputStream(errs)
   \text{orec} = 0ocnt = 0for mol in ifsmols. GetOEGraphMols():
       \text{over} + 1
```

```
iter = oemedchem. OEMatchedPairApplyTransforms(mol, mmp, chemctxt, minpairs)
        if not iter. IsValid():
            if verbose:
                # as minpairs increases, fewer transformed mols are generated -
\rightarrowoutput if requested
                name = mol.fettile()if not mol. GetTitle():
                   name = 'Record ' + str(orec)oechem. OEThrow. Info ("%s did not produce any output" % name)
            contimeif errs is not None:
           errs.clear()
        for outmol in iter:
           ocnt += 1oechem.OEWriteMolecule(ofs, outmol)
        if errs is not None:
           errs.clear()
   if not orec:
        oechem. OEThrow. Fatal ('No records in input structure file to transform')
   if not ocnt:
        oechem. OEThrow. Warning ('No transformed structures generated')
   print ("Input molecules={} Output molecules={}". format (orec, ocnt))
   return 0
#######################################
InterfaceData = ""# matchedpairtransform interface file
!CATEGORY MatchedPairTransform
    !CATEGORY I/O
       !PARAMETER -mmpindex 1
         !TYPE string
         !REQUIRED true
         !BRIEF Input filename of serialized matched pair index to load
        LEND
        !PARAMETER -input 2
         !ALIAS -i
         !ALIAS -in
          !TYPE string
          !REQUIRED true
          !BRIEF Input filename of structures to process using matched pairs from -
\rightarrowmmpindex
       ! END
        !PARAMETER -output 3
         !ALIAS -o
         !ALIAS -out
         !TYPE string
         !REOUIRED true
          !BRIEF Output filename
        LEND
```

```
! END
    !CATEGORY options
        !PARAMETER -context 1
            !ALIAS -c!TYPE string
            !DEFAULT 0
            !BRIEF chemistry context to use for the transformation [0|1|2|3|A]
        LEND
        !PARAMETER -minpairs 2
            !TYPE int
            !DEFAULT 0
            !BRIEF require at least -minpairs to apply the transformations (default:
\leftrightarrowall)
        ! END
        !PARAMETER -verbose 3
            !TYPE bool
            !DEFAULT 0
            !BRIEF generate verbose output
         ! END
        !PARAMETER -nowarnings 4
            !TYPE bool
            !DEFAULT 1
            !BRIEF suppress warning messages from applying transformations
         LEND
    ! END
! END
\overline{u} \overline{u} \overline{u}def main(argv=[_name_]):
    itf = oechem. OEInterface (InterfaceData)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MMPTransform(itf)
if _name_ = = "_main_ ":
    sys.exit(main(sys.argv))
```

## 3.1.7 Matched Pair analysis and listing of transformations

A program that loads a previously generated Matched Pair index, then prints the transformations and matched pairs found from the analysis. If an (optional, numeric) data field is provided, the returned transformations can also be ranked by the largest increase in the delta property found from the matched pairs that define it.

- OEMatchedPairAnalyzer class
- OEMatchedPairAnalyzerOptions class
- OEMatchedPairGetTransforms function

### **Command Line Interface**

prompt> MatchedPairTransformList.py -mmpindex index.mmpidx [ -datafield sdDataField ]

#### **Code**

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
# Utility to load a previously generated MMP index
# and dump a listing of the transformations derived from matched pairs found
#______________________________________
# MatchedPairTransformList.py index_file
## index_file: filename of MMP index
#######################################
from openeye import oechem
from openeye import oemedchem
import sys
# simple statistics
import math
def average(x):
   return (sum(x) * 1.0 / len(x))def variance(x):
    return list (map (lambda y: (y - average(x)) \rightarrow x 2, x))
def stddev(x):
   return math.sqrt(average(variance(x)))
def \text{cmp}(x, y):
   \overline{u} \overline{u} \overline{u}Replacement for built-in function cmp that was removed in Python 3
```

```
Compare the two objects x and y and return an integer according to
    the outcome. The return value is negative if x < y, zero if x == yand strictly positive if x > y.
    n \, n \, nreturn (x > y) - (x < y)class MMPXform:
   def _init_(self, xform, avg, std, num):
       self.xform = xform
        self. avg = avgself. std = stdself.num = numdef _cmp_(self, other):
        return cmp (self.avg, other.avg)
def MMPTransformList(itf):
    # check MMP index
   mmpimport = itf.GetString("-mmpindex")if not oemedchem. OEIsMatchedPairAnalyzerFileType (mmpimport) :
        oechem. OEThrow. Fatal ('Not a valid matched pair index input file, {}'.
→format (mmpimport))
    # load MMP index
   mmp = oemedchem.OEMatchedPairAnalyzer()
   if not oemedchem. OEReadMatchedPairAnalyzer (mmpimport, mmp) :
        oechem. OEThrow. Fatal ("Unable to load index {}". format (mmpimport))
    if not mmp. NumMols ():
        oechem. OEThrow. Fatal ('No records in loaded MMP index file: {}'.
→format (mmpimport))
    if not mmp. NumMatchedPairs():
        oechem. OEThrow. Fatal ('No matched pairs found in MMP index file, ' +
                              'use -fragGe,-fragLe options to extend indexing range')
    # request a specific context for the transform activity, here 0-bonds
   chemctxt = oemedchem. OEMatchedPairContext_Bond0
    askcontext = itf.GetString("-context") [ : 1]if askcontext == '0':chemctxt = oemedchem. OEMatchedPairContext_Bond0
    elif askcontext == '1':chemctxt = oemedchem. OEMatchedPairContext_Bond1
    elif askcontext == '2':chemctxt = oemedchem. OEMatchedPairContext Bond2
    elif askcontext == '3':chemctxt = oemedchem. OEMatchedPairContext Bond3
    elif askcontext == 'a' or askcontext == 'A':
        chemctxt = oemedchem. OEMatchedPairContext_AllBonds
    else:
        oechem. OEThrow. Fatal ("Invalid context specified: " +
                             askcontext + ", only 0|1|2|3|A allowed")
```

```
(continued from previous page)
```

```
bPrintTransforms = itf.GetBool("-printlist")# if a data field was specified, retrieve the SD data field name
   field = Noneif itf.HasString("-datafield"):
       field = itf.GetString("-datafield")
   if not bPrintTransforms and field is None:
       oechem. OEThrow. Info('Specify one of -datafield or -printlist, otherwise.
→nothing to do!')
       return
   extractOptions = oemedchem.OEMatchedPairTransformExtractOptions()
   # specify amount of chemical context at the site of the substituent change
   extractOptions. SetContext (chemctxt)
   # controls how transforms are extracted (direction and allowed properties)
   extractOptions.SetOptions(oemedchem.OEMatchedPairTransformExtractMode_Sorted |
                              oemedchem.OEMatchedPairTransformExtractMode_NoSMARTS)
   # walk the transforms from the indexed matched pairs
   xforms = []xfmidx = 0for mmpxform in oemedchem. OEMatchedPairGetTransforms (mmp, extractOptions):
       xfmidx += 1
       if bPrintTransforms:
           print (\sqrt[m]{0:2} / \sqrt{1})".format (xfmidx, mmpxform.GetTransform()))
        # compute delta property
       mmpidx = 0prop = []for mmppair in mmpxform. GetMatchedPairs():
           mmpidx += 1mmpinfo = "\t{0:2}: (1:2), {2:2}) ".format(mmpidx,
                                                        mmppair.FromIndex(),
                                                        mmppair.ToIndex())
            for tag in mmppair. GetDataTags():
                mmpinfo = mmpinfo + " \{0\} = (\{1\}, \{2\})".format(tag,
                                                              mmppair.
\rightarrowGetFromSDData(tag),
                                                              mmppair.GetToSDData(taq))
                if taq == field:
                    fromData = NonetoData = Nonetrv:
                        fromData = float(mmppair.GetFromSDData(tag))
                    except ValueError:
                        fromData = Nonetry:\text{tolata} = \text{float}(mmppair.\text{GetToSDData}(tag))except ValueError:
                        toData = Noneif fromData is not None and toData is not None:
                        prop.append(toData - fromData)
            if bPrintTransforms:
                print (mmpinfo)
```

```
# skip if property not found
        if len(prop):xforms.append(MMPXform(mmpxform, average(prop), stddev(prop), len(prop)))
   if not field:
       return 0
   if field and not len (xforms) :
       oechem. OEThrow. Error ("No matched pairs found with () data". format (field))
   print("")print ("*** Transforms sorted by delta ({})". format (field))
   xforms.sort(key=lambda c: -abs(float(c.avq)))
   idx = 0for xfm in xforms:
        idx += 1if (extractOptions. GetOptions() &
                oemedchem.OEMatchedPairTransformExtractMode_NoSMARTS) != 0:
            # not 'invertable' if SMARTS qualifiers were applied
            if xfm. avq < 0.:
                xfm.avg = -1. * xfm.avgxfm.xform.Invert()
        print ("{0:2} {2}=(avg={3:.2f}, stdev={4:.2f}, num={5}) {1}". format (idx,
                                                                          xfm.xform.
\rightarrowGetTransform(),
                                                                          field,
                                                                          xfm.avq,
                                                                          xfm.std,
                                                                          xfm.num))
#######################################
InterfaceData = " "# matchedpairtransformlist interface file
!BRIEF -mmpindex index.mmpidx [ -datafield sdDataField ]
!CATEGORY MatchedPairTransformList
    !CATEGORY I/O
       !PARAMETER -mmpindex 1
         !TYPE string
         !REOUIRED true
         !BRIEF Input filename of serialized matched pair index to load
        !END
   ! END
    !CATEGORY options
        !PARAMETER -context 1
           IATITAS -c!TYPE string
          !DEFAULT 0
          !BRIEF chemistry context to use for the transformation [0|1|2|3|A]
        !END
        !PARAMETER -printlist 2
           !ALIAS -p
           !TYPE bool
```

```
!DEFAULT 1
             !BRIEF print all transforms and matched pairs
         !END
         !PARAMETER -datafield 3
             !ALIAS -d
             !TYPE string
             !BRIEF sort transforms based on delta change in this property
         LEND
    ! END
!END
\mathbf{u},\mathbf{u},\mathbf{u}def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    if not oechem. OEParseCommandLine(itf, argv):
         oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MMPTransformList(itf)
if name == "_main_":
    sys.exit(main(sys.argv))
```

## 3.1.8 Matched Pair analysis and listing of transformations related to probe structures

A program that loads a previously generated Matched Pair index, then prints the transformations and matched pairs found from the analysis that are related to the provided probe structure(s). If an (optional, numeric) data field is provided, the returned transformations can also be ranked by the largest increase in the delta property found from the matched pairs that define it.

- OEMatchedPairAnalyzer class
- OEMatchedPairAnalyzerOptions class
- OEMatchedPairGetTransforms function

### **Command Line Interface**

```
prompt> MatchedPairTransformProbe.py [ -datafield sdDataField ] index.mmpidx probe_
\rightarrowmolecules.sdf
```

#### **Code**

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
# Utility to load a matched pair index
# and dump a listing of transformations related to probe molecule(s)
# ---------
           _______________________________
# MatchedPairTransformProbe.py mmp_index probe_mols
## mmp_index: filename of MMP index file
# probe mols: filename of input molecules to use as probes for related transforms
#######################################
from openeye import oechem
from openeye import oemedchem
import sys
# simple statistics
import math
def average(x):
   return (sum(x) * 1.0 / len(x))def variance(x):
    return list (map (lambda v: (y - average(x)) \rightarrow x (2, x))
def stddev(x):
   return math.sqrt(average(variance(x)))
def \text{cmp}(x, y):
   n \cdot n \cdot n
```

```
Replacement for built-in function cmp that was removed in Python 3
    Compare the two objects x and y and return an integer according to
    the outcome. The return value is negative if x < y, zero if x == yand strictly positive if x > y.
    n \overline{n}return (x > y) - (x < y)class MMPXform:
   def _init_(self, xform, avg, std, num):
        self.xform = xform
        self. avg = avgself. std = stdself.num = numdef _cmp_(self, other):
        return cmp (self.avg, other.avg)
def MMPAnalyzeProbe(itf):
    # check MMP index
   mmpimport = itf.GetString("-mmpindex")if not oemedchem. OEIsMatchedPairAnalyzerFileType(mmpimport) :
        oechem. OEThrow. Fatal ('Not a valid matched pair index input file, \{ )'.
\rightarrow format (mmpimport))
    # load MMP index
   mmp = oemedchem.OEMatchedPairAnalyzer()
   if not oemedchem. OEReadMatchedPairAnalyzer (mmpimport, mmp) :
        oechem.OEThrow.Fatal("Unable to load index {}".format(mmpimport))
    if not mmp. NumMols():
        oechem. OEThrow. Fatal ('No records in loaded MMP index file: \{}'.
\rightarrowformat (mmpimport))
    if not mmp. NumMatchedPairs():
        oechem. OEThrow. Fatal ('No matched pairs found in MMP index file, ' +
                              'use -fragGe,-fragLe options to extend indexing range')
    # input probe structure(s)
    if s = oechem. oemolistream()if not ifs.open(itf.GetString("-input")):
        oechem. OEThrow. Fatal ("Unable to open input probe molecule file: " + itf.
\rightarrowGetString ("-input"))
    # request a specific context for the transform activity, here 0-bonds
    chemctxt = oemedchem. OEMatchedPairContext_Bond0
   askcontext = itf.getString("-context")[:1]if askcontext == '0':chemctxt = oemedchem. OEMatchedPairContext_Bond0
    elif askcontext == '1':chemctxt = oemedchem. OEMatchedPairContext_Bond1
    elif askcontext == '2':chemctxt = oemedchem. OEMatchedPairContext_Bond2
```

```
elif askcontext == '3':chemctxt = oemedchem.OEMatchedPairContext_Bond3
   elif askcontext == 'a' or askcontext == 'A':
       chemctxt = oemedchem.OEMatchedPairContext_AllBonds
   else:
       oechem. OEThrow. Fatal ("Invalid context specified: " +
                             askcontext + ", only 0|1|2|3|A allowed")
   bPrintTransforms = itf.GetBool("-printlist")
   # if a data field was specified, retrieve the SD data field name
   field = Noneif itf.HasString("-datafield"):
       field = itf.GetString("-datafield")
   extraction is = oemedchem. 0EMatchedPairTransformExtractions()# specify amount of chemical context at the site of the substituent change
   extractOptions. SetContext (chemctxt)
   # controls how transforms are extracted (direction and allowed properties)
   extractOptions.SetOptions(oemedchem.OEMatchedPairTransformExtractMode_Sorted |
                              oemedchem.OEMatchedPairTransformExtractMode_NoSMARTS)
   record = 0for mol in ifs. GetOEGraphMols():
       record += 1print ("*** Probe molecule, {} record={}"
              .format(oechem.OEMolToSmiles(mol), record))
        # walk the transforms from the indexed matched pairs that are related to this.
\rightarrowprobe molecule
       xforms = []xfmidx = 0for mmpxform in oemedchem. OEMatchedPairGetTransforms (mmp,
                                                               mol.extractOptions):
            xfmidx += 1if bPrintTransforms:
                print (\sqrt[m]{0:2} / \sqrt{1}, \sqrt[m]{1}. format (xfmidx, mmpxform. GetTransform()))
            if field is None:
                continue
            # compute delta property
            mmpidx = 0prop = []for mmppair in mmpxform. GetMatchedPairs():
                mmpidx += 1mmpinfo = "\t{0:2}: (1:2), (2:2)".format(mmpidx,
                                                            mmppair.FromIndex(),
                                                            mmppair.ToIndex())
                for tag in mmppair. GetDataTags():
                    mmpinfo = mmpinfo + " \{0\} = (\{1\}, \{2\})".format(tag,
                                                                  mmppair.
\rightarrowGetFromSDData(taq),
                                                                  mmppair.
→GetToSDData(tag))
```

```
(continues on next page)
```

```
(continued from previous page)
```

```
if tag == field:
                        fromData = None
                        toData = None
                        try:
                             fromData = float(mmppair.GetFromSDData(tag))
                         except ValueError:
                             fromData = None
                        try:
                             toData = float (mmppair.GetToSDData(tag))
                        except ValueError:
                             toData = Noneif fromData is not None and toData is not None:
                             prop.append(toData - fromData)
                if bPrintTransforms:
                    print (mmpinfo)
            # skip if property not found
            if field is not None and len (prop) :
                xforms.append(MMPXform(mmpxform, average(prop), stddev(prop),
\rightarrowlen(prop)))
            else:
                xforms.append(MMPXform(mmpxform, 0.0, 0.0, 0))
        if not len (xforms) :
            if field is not None:
                print ("*** No related transforms found with", field)
        else:
            if field is not None:
                print ("*** Related transforms sorted by delta ({) ". format (field))
                xforms.sort(key=lambda c: -abs(float(c.avg)))
            else:
                print ("*** Related transforms")
            idx = 0for xfm in xforms:
                idx += 1if field is None:
                    print ("0:2) \{1\}". format (idx,
                                               xfm.xform.GetTransform()))
                else:
                     if (extractOptions.GetOptions() &
                             oemedchem.OEMatchedPairTransformExtractMode_NoSMARTS) !=
\leftrightarrow 0 :
                         # not 'invertable' if SMARTS qualifiers were applied
                         if xfm. avq < 0.:
                             xfm. avq = -1. * xfm. avq
                             xfm.xform.Invert()
                    print ("\{0:2\} \{2\} = (avg=\{3:2f\}, stdev=\{4:2f\}, num=\{5\}) \{1\}"
                           .format(idx, xfm.xform.GetTransform(), field,
                                   xfm.avq, xfm.std, xfm.num))
        print("")#######################################
InterfaceData = ""# matchedpairtransformprobe interface file
```

```
!CATEGORY MatchedPairTransformProbe
    !CATEGORY I/O
        !PARAMETER -mmpindex 1
          !TYPE string
          !REQUIRED true
           !BRIEF Input filename of serialized matched pair index to load
          !KEYLESS 1
        LEND
        !PARAMETER -input 2
          !ALIAS -in
          !TYPE string
          !REQUIRED true
          !BRIEF Input filename of probe molecule (s) to use to retrieve related
\rightarrowtransforms
          !KEYLESS 2
        ! END
    ! END
    !CATEGORY options
         !PARAMETER -context 1
            !ALIAS -c!TYPE string
           !DEFAULT 0
           !BRIEF chemistry context to use for the transformation [0|1|2|3|A]
        ! END
        !PARAMETER -printlist 2
           !ALIAS -p
           !ALIAS -pri
            !TYPE bool
           !DEFAULT 1
            !BRIEF print all transforms and matched pairs
        !END
        !PARAMETER -datafield 3
           !ALIAS -d
           !TYPE string
           !BRIEF sort transforms based on delta change in this property
        !END
    ! END
! END
\mathbf{u}u u
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MMPAnalyzeProbe(itf)
if name == " main ":
    sys.exit(main(sys.argv))
```

## 3.1.9 MCS Fragment database generation

A program that performs an MCS fragmentation analysis of a set of structures and saves the generated index file for subsequent loading and querying.

![](_page_64_Figure_3.jpeg)

Fig. 5: Schematic representation of the MCS fragment search process

#### See also:

- OEMCSFragDatabase class
- OEMCSFragDatabaseOptions class

### **Command Line Interface**

prompt> CreateMCSFragDatabase.py index.sdf output.mcsfrag

### **Code**

| #!/usr/bin/env python                                                    |
|--------------------------------------------------------------------------|
| # (C) 2022 Cadence Design Systems, Inc. (Cadence)                        |
| # All rights reserved.                                                   |
| # TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is     |
| # provided to current licensees or subscribers of Cadence products or    |
| # SaaS offerings (each a "Customer").                                    |
| # Customer is hereby permitted to use, copy, and modify the Sample Code, |
| # subject to these terms. Cadence claims no rights to Customer's         |
| # modifications. Modification of Sample Code is at Customer's sole and   |
| # exclusive risk. Sample Code may require Customer to have a then        |

```
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
#######################################
# Utility to perform an MCS fragmentation on an input set of structures
# and save the index for subsequent analysis
# CreateMCSFragDatabase index_mols output_index
#[ -verbose 1 ] // optional verbosity
# index_mols: filename of input molecules to analyze
# output_index: filename of MCS fragment index
#######################################
from openeye import oechem
from openeye import oemedchem
import sys
def MCSFragIndex(itf):
   # output index file
   mesindexfile = itf.GetString("-output")if not oemedchem. OEIsMCSFraqDatabaseFileType (mcsindexfile):
       oechem. OEThrow. Fatal ("Output file is not an mcs fragment index type \
                            - needs .mcsfrag extension: {}" .format(mcsindexfile))
    # create options class with defaults
   mcsopt = oemedchem. 0EMCSFraqDatabaseOptions()# set up options from command line
   if not oemedchem. OESetupMCSFragDatabaseOptions (mcsopt, itf) :
       oechem. OEThrow. Fatal ("Error setting MCS fragment database options")
    # input structures to index
   if \sin \text{dex} = \text{oechem.oemolistream}()if not ifsindex.open(itf.GetString("-input")):
       oechem. OEThrow. Fatal ("Unable to open {} for reading"
                            .format(itf.GetString("-input")))
    # get requested verbosity setting
   verbose = itf. GetBool("-verbose")timer = itf.GetBool("-timer")if verbose:
       timer = Truewatch = occhem.OEStopwatch()maxrec = max(itf.fetInt("maxrec"), 0)statusrec = \text{iff}. \text{GetInt}("-\text{status"})if verbose:
       if not mcsopt.HasIndexableFragmentHeavyAtomRange():
           oechem. OEThrow. Info ("Indexing all fragments")
```

```
Also:oechem.OEThrow.Info("Using index range={0:.1f}-{1:.1f}%"
                                  .format(mcsopt.GetIndexableFragmentRangeMin(),
                                          mcsopt.GetIndexableFragmentRangeMax()))
        if statusrec:
            oechem. OEThrow. Info ("Status output after every {0} records".
\rightarrowformat (statusrec))
        if maxrec:
            oechem. OEThrow. Info("Indexing a maximum of \{0\} records". format (maxrec))
    # create indexing engine
   mcsdb = oemedchem.OEMCSFragDatabase(mcsopt)
   # add molecules to be indexed
   record = 0unindexed = 0for mol in ifsindex. GetOEGraphMols():
        status = mcsdb.AddMol(mol, record)
        if status != record:
            unindexed += 1if verbose:
                oechem. OEThrow. Info ('Input structure not added to index, record=%d
\leftrightarrowstatus=\frac{2}{5}s' \frac{6}{5}(record, oemedchem.
\rightarrowOEMatchedPairIndexStatusName(status)))
       record += 1if maxrec and record >= maxrec:
            break # maximum record limit reached
        if statusred and (record \frac{1}{6} statusred) == 0:
            oechem. OEThrow. Info("Records: {} Indexed: {} Unindexed: {}"
                                  .format (record, (record - unindexed), unindexed))
   indextime = watch.Elapped()if record == 0:
        oechem. OEThrow. Fatal ("No records in input structure file for indexing")
   if not mcsdb. NumFragments():
        oechem. OEThrow. Fatal ('No fragments found from indexing, ' +
                              'use -fragGe,-fragLe options to extend indexing range')
   if timer:
        if (not verbose and not timer) or not indextime:
            oechem.OEThrow.Fatal("Processed {0} molecules, "
                                   "generating {1} fragments"
                                   .format (record, mcsdb.NumFragments()))
        else:
            oechem.OEThrow.Info("Processed {0} molecules, "
                                  "generating {1} fragments in {2:.2F} sec: "
                                  "\{3:, .1F} mols/sec \{4:, .1F} fraqs/sec"
                                  .format (record,
                                          mcsdb.NumFragments(),
                                          indextime,
                                          float (record) / float (indextime),
                                          float(mcsdb.NumFragments())/float(indextime)))
   if not oemedchem. OEWriteMCSFragDatabase (mcsindexfile, mcsdb) :
        oechem. OEThrow. Fatal ("Error serializing MCS fragment database: {}"
```

```
.format(mcsindexfile))
    # return some status information
    oechem. OEThrow. Info("Records: {}, Indexed: {}, fragments: {:, d}"
                        .format (record,
                                mcsdb.NumMols(),
                                mcsdb.NumFragments()))
    return 0
#######################################
InterfaceData = ""#createmcsfragdatabase interface file
!CATEGORY CreateMCSFraqDatabase
    !CATEGORY I/O
        !PARAMETER -input 1
          !TYPE string
          !REQUIRED true
          !BRIEF Input filename of structure(s) to index
          !KEYLESS 1
        !END
        !PARAMETER -output 2
         !TYPE string
          !REQUIRED true
          !BRIEF Output filename of MCS fragment serialized index
          !KEYLESS 2
        !END
    !END
    !CATEGORY options
        !PARAMETER -verbose 1
           !TYPE bool
           IDEFAULT 0
          !BRIEF generate verbose output
        ! END
        !PARAMETER -maxrec 2
           !TYPE int
           !DEFAULT 0
           !BRIEF limit indexing to -maxrec records from the -input structures
        ! END
        !PARAMETER -timer 3
           !TYPE bool
           !DEFAULT 0
           !BRIEF report indexing time
        !END
        !PARAMETER -status 4
           !TYPE int
           !DEFAULT 0
           !BRIEF print indexing status every -status records
        !END
    !END
! END
\mathbf{u} as \mathbf{u}
```

```
def main(argv=[_name]):
   itf = oechem. OEInterface (InterfaceData)
    oemedchem.OEConfigureMCSFragDatabaseOptions(itf)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
   MCSFragIndex(itf)
if __name__ == "__main__".sys.exit(main(sys.argv))
```

### 3.1.10 MCS Similarity score reporting

A program that loads a previously generated MCS fragment database, then returns the highest Maximum Common Substructure (Tanimoto) scores from the provided input query structures.

![](_page_68_Figure_5.jpeg)

Fig. 6: Schematic representation of the MCS fragment index and search process

- OEMCSFragDatabase class
- OEMCSFragDatabaseOptions class

#### **Command Line Interface**

prompt> MCSFragDatabase.py -indb index.mcsfrag -query queries.sdf

#### **Code**

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
# Utility to load a pregenerated index and return the highest MCS similarity
# structures from an query structure(s)
# ------------------------------
# MCSFragDatabase [ -indb index.mcsfrag ]
                 I -query query file 1
#[ -type bond -limit 10 ] // 10 Tanimoto sim bond scores
#\int -verbose 1// optional verbosity
## index.mcsfrag: filename of index file to load
# query file: filename of query to report MCS similarity results
#######################################
from openeye import oechem
from openeye import oemedchem
import sys
def MCSFraqQuery(itf):
   verbose = itf. GetBool("-verbose")\ttimer = \text{itf}.\text{GetBool}("-\text{timer''})indb = itf.GetString("-indb")if not oemedchem. OEIsMCSFraqDatabaseFileType(indb):
       oechem. OEThrow. Fatal ("Option -indb must specify a .mcsfrag filename: "
                            + indb)
   if verbose:
       oechem.OEThrow.Info("Loading index from " + indb)
   watch = occhem.OEStopwatch()watch.Start()
   mcsdb = oemedchem.OEMCSFragDatabase()
```

```
(continued from previous page)
```

```
if not oemedchem. OEReadMCSFraqDatabase(indb, mcsdb):
    oechem. OEThrow. Fatal ("Error deserializing MCS fragment database: "
                          + indb)
loadtime = watch.Elapped()if not mcsdb. NumMols():
    oechem. OEThrow. Fatal ("Loaded empty index")
if timer:
    if not loadtime:
        oechem. OEThrow. Info ("Loaded index of {0} molecules, {1} fragments"
                             .format(mcsdb.NumMols(), mcsdb.NumFragments()))
    else:oechem.OEThrow.Info("Loaded index of {0} molecules, {1} "
                             "fragments in \{2:2F\} sec: "
                             "{3:, .1F} mols/sec {4:, .1F} frags/sec"
                             .format(mcsdb.NumMols(),
                                     mcsdb.NumFragments(),
                                     loadtime,
                                     float (mcsdb.NumMols())/loadtime,
                                     float (mcsdb.NumFraqments())/loadtime))
if not mcsdb. NumFragments():
    oechem. OEThrow. Fatal ("No fragments loaded from index, "
                          "use -fragGe,-fragLe options to "
                          "extend indexable range")
queryfile = itf. Getstring("-query")if squery = occhem.oemolistream()if not ifsquery.open(queryfile):
    oechem. OEThrow. Fatal ("Unable to open query file: " + queryfile)
# process the query options
qmaxrec = 0if itf. HasInt ("-qlim"):
    qmaxrec = itf.GetInt("-qlim")numscores = 10if itf.HasInt("-limit"):
    numscores = itf.GetInt("-limit")cnttype = oemedchem.OEMCSScoreType_BondCount
if itf. HasString ("-type"):
    if "atom" in itf.GetString("-type"):
        cnttype = oemedchem.OEMCSScoreType_AtomCount
    elif "bond" in itf.GetString("-type"):
        cnttype = oemedchem.OEMCSScoreType_BondCount
    else:
        oechem. OEThrow. Warning ("Ignoring unrecognized -type option, "
                                "expecting atom or bond: " +
                                itf.GetString("-type"))
entname = "bond"if cnttype != oemedchem.OEMCSScoreType BondCount:
    cntname = "atom"# process the query (or queries)
```

```
(continued from previous page)
```

```
qmol = oechem.OEGraphMol()
    qnum = 0while oechem. OEReadMolecule (ifsquery, qmol) :
        qnum += 1numhits = 0for score in mcsdb. GetSortedScores (qmol,
                                            numscores,
                                            0<sub>r</sub>0,True,
                                            cnttype) :
            if numhits == 0:
                oechem.OEThrow.Info("Query: {0}: {1}"
                                     .format(qnum, qmol.GetTitle()))
            oechem. OEThrow. Info("\trecord: {0:6}\ttanimoto_{1}_score: "
                                 "\{2: .2f\} tmcs_core: \{3\}"
                                 .format(score.GetIdx(),
                                         cntname,
                                         score.GetScore(),
                                         score.GetMCSCore()))
            numhits += 1if numhits == 0:
            oechem. OEThrow. Warning ("Query: {0}: {1} - no hits"
                                    .format(qnum, qmol.GetTitle()))
        if qmaxrec and qnum >= qmaxrec:
            break
    if qnum == 0:
        oechem. OEThrow. Fatal ("Error reading query structure(s): " + queryfile)
#######################################
InterfaceData = ""#MCSFragmentDatabase interface file
!CATEGORY MCSFragmentDatabase
    !CATEGORY I/O
        !PARAMETER -indb 1
         !TYPE string
          !REQUIRED true
          !BRIEF Input filename of index file to load
          !KEYLESS 1
        !END
        !PARAMETER -query 2
         !ALIAS -q
         !TYPE string
         !REQUIRED true
          !BRIEF query structure file to report similarity results against
          !KEYLESS 2
        !END
```

```
LEND
```

```
(continued from previous page)
```

```
!CATEGORY options
        !PARAMETER -type 1
            !TYPE string
            !DEFAULT bond
            !BRIEF MCS core counts to use for reported scores: atom or bond
         ! END
         !PARAMETER -limit 2
            !TYPE int
            !DEFAULT 10
           !BRIEF report -limit scores for the query structure
        ! END
         !PARAMETER -verbose 3
            !TYPE bool
            !DEFAULT 0
           !BRIEF generate verbose output
        ! END
         !PARAMETER -qlim 4
            !TYPE int
            !DEFAULT 0
            !BRIEF limit query processing to -qlim records from the -query structures
         ! END
         !PARAMETER -timer 5
           !TYPE bool
           !DEFAULT 0
            !BRIEF report database loading time
         !END
    ! END
!END
\mathbf{u} and \mathbf{u}def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MCSFragQuery(itf)
if name == " main ":
    sys.exit(main(sys.argv))
```

## 3.1.11 MCS Fragmentation API

A program that loads a previously generated MCS fragment database, then reports the most common fragments identified by fragmentation from the input structure(s).

- OEMCSFragDatabase class
- · OEMCSFragDatabase.MoleculeToCores
- · OEMCSFragDatabase. CoreToMolecules
- · OEMCSFragDatabase. CoreToMoleculeCount

• OEMCSFragDatabaseOptions class

#### **Command Line Interface**

prompt> MCSFragOccurrence.py -indb index.mcsfrag -query queries.sdf

#### **Code**

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
# report common fragments from an input set of molecules
#######################################
from openeye import oechem
from openeye import oemedchem
import operator
import sys
def MCSFragOccurrence(itf):
   verbose = itf.GetBool("-verbose")
   timer = itf.GetBool("-timer")indb = itf.GetString("-indb")if not oemedchem. OEIsMCSFragDatabaseFileType(indb):
       oechem. OEThrow. Fatal ("Option -indb must specify a .mcsfrag filename: "
                            + indb)
   if verbose\cdotoechem.OEThrow.Info("Loading index from " + indb)
   watch = occhem.OEStopwatch()watch. Start ()
   mcsdb = oemedchem.OEMCSFragDatabase()
   if not oemedchem. OEReadMCSFragDatabase(indb, mcsdb):
       oechem. OEThrow. Fatal ("Error deserializing MCS fragment database: "
                            + indb)
   loadtime = watch.Elapped()
```

```
if not mcsdb. NumMols():
    oechem. OEThrow. Fatal ("Loaded empty index")
if not timer or not loadtime:
    oechem. OEThrow. Info ("Loaded index of {0} molecules, {1} fragments"
                         .format(mcsdb.NumMols(), mcsdb.NumFragments()))
Also:oechem.OEThrow.Info("Loaded index of {0} molecules, {1} "
                         "fragments in \{2: .2F\} sec: "
                         "{3:, .1F} mols/sec {4:, .1F} frags/sec"
                         .format(mcsdb.NumMols(),
                                 mcsdb.NumFragments(),
                                 loadtime,
                                  float (mcsdb.NumMols())/loadtime,
                                  float (mcsdb.NumFragments())/loadtime))
if not mcsdb. NumFragments():
    oechem. OEThrow. Fatal ("No fragments loaded from index, "
                          "use -fragGe,-fragLe options to "
                          "extend indexable range")
queryfile = itf.fetString("-query")if squery = occhem.oemolistream()if not ifsquery.open(queryfile):
    oechem. OEThrow. Fatal ("Unable to open query file: " + queryfile)
# process the query options
qmaxrec = 0if itf.HasInt("-qlim"):
    qmaxrec = itf.GetInt("-qlim")record = 0uniqueCores = set()qmol = oechem. OEGraphMol()while oechem. OEReadMolecule (ifsquery, qmol) :
    cores = mcsdb.MoleculeToCores(qmol)
    for core in cores:
        # collect unique cores with >0 counts in the index
        if not mcsdb. CoreToMoleculeCount (core) :
            continue
        uniqueCores.add(core)
    record += 1if qmaxrec and record >= qmaxrec:
        break
coreOcc = dict()for core in uniqueCores:
    coreOcc[core] = mesdb.CoreToMoleculeCount(core)oechem. OEThrow. Info ('Common fragments with occurrence >1:')
num = 0topnum = \text{iff}. \text{GetInt}(' - \text{top'}')for k, v in sorted (coreOcc.items(),
                    key=operator.itemqetter(1, 0),
                    reverse=True) :
    if v \leq 1:
```

```
break
       num += 1ids = list(mcsdb.CoreToMolecules(k))oechem.OEThrow.Info('{} {} {}'.format(v, k, ids))
        if topnum and num >= topnum:
           break
   if itf.GetBool('-uncommon'):
        oechem.OEThrow.Info('Uncommon fragments:')
        for k, v in sorted (coreOcc.items (),
                           key=operator.itemgetter(1)):
            if v > 1:
                break
            ids = list(mcsdb.CoreToMolecules(k))oechem.OEThrow.Info('{} {} {}'.format(v, k, ids))
#######################################
InterfaceData = ""#MCSFragOccurrence interface file
!CATEGORY MCSFraqOccurrence
    !CATEGORY T/O
       !PARAMETER -indb 1
         !TYPE string
          !REQUIRED true
         !BRIEF Input filename of index file to load
         IKEYLESS 1
        !END
        !PARAMETER -query 2
          !TYPE string
          !REQUIRED true
          !BRIEF query structure file to report cores against
          !KEYLESS 2
        ! END
   ! END
   !CATEGORY options
        !PARAMETER -verbose 1
           !TYPE bool
           !DEFAULT 0
          !BRIEF generate verbose output
        LEND
        !PARAMETER -timer 2
           !TYPE bool
           !DEFAULT 0
           !BRIEF report database loading time
        ! END
        !PARAMETER -top 3
           !TYPE int
           !DEFAULT 10
           !LEGAL_RANGE 0 inf
           !BRIEF print the -top number of common fragment occurrences (0:all,..
\leftrightarrow10: default)
        ! END
        !PARAMETER -uncommon 4
```

```
!TYPE bool
             !DEFAULT 0
             !BRIEF print the uncommon fragments also
          ! END
         !PARAMETER -qlim 5
             !TYPE int
             !DEFAULT 0
             !BRIEF limit query processing to -qlim records from the -query structures
         ! END
     ! END
!END
\mathbf{u},\mathbf{u},\mathbf{u}def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    if not oechem. OEParseCommandLine(itf, argv):
         oechem. OEThrow. Fatal ("Unable to interpret command line!")
    MCSFragOccurrence(itf)
if __name__ == "_main_":
    sys.exit(main(sys.argv))
```

## 3.1.12 Print OEMedChem version information

A utility to print library version information

- · OEMedChemGetRelease function
- · OEMedChemGetVersionfunction
- OEMedChemGetArch function
- · OEMedChemGetPlatform function

#### **Command Line Interface**

This simple example reports library version information

prompt> OEMedChemInfo.py

#### **Code**

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
# Print toolkit release date, platform and build information.
######################################
from openeye import oemedchem
import sys
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
   print ("OEMedChem version: %s built: %d arch: %s platform: %s" %
          (oemedchem.OEMedChemGetRelease(), oemedchem.OEMedChemGetVersion(),
          oemedchem.OEMedChemGetArch(),
                                          oemedchem.OEMedChemGetPlatform()))
if __name__ == "_main_":
   sys.exit(main(sys.argv))
```

### **CHAPTER**

## **FOUR**

**API** 

## **4.1 OEMedChem API**

### **4.1.1 OEMedChem Classes**

#### **OEBemisMurckoOptions**

class OEBemisMurckoOptions : public OESystem:: OEOptions

The functions OEGetRingLinkerSideChainFragments and OEGetBemisMurcko both return sets of Bemis-Murcko fragments. The OEBemisMurckoOptions class can be used to specify both the OERegionType of these fragments and to add sidechains that match user-specified criteria to the main Bemis-Murcko framework.

#### **Constructors**

OEBemisMurckoOptions()

Default constructor, which sets the perceived fragment type to All, as defined in the OERegionType namespace. No additional SMARTS substituents are set.

#### **CreateCopy**

OEBemisMurckoOptions\* CreateCopy() const { return new OEBemisMurckoOptions(\*this); }t

Returns a pointer to a copy of the options object.

#### **GetRegionType**

std::string GetRegionType() const

Returns the name of the OERegionType set in the options class.

### **GetSubstituentSearch**

OEChem:: OESubSearch GetSubsituentSearch() const

Returns the subsearch used to add custom substituents to the Bemis-Murcko framework.

#### **GetUnsaturatedHeteroBonds**

bool GetUnsaturatedHeteroBonds() const

Gets the boolean indicating whether sidechains beginning with unsaturated bonds to hetero atoms will be included in the main Bemis-Murcko framework.

#### **SetRegionType**

void SetRegionType (std::string regionType)

Sets the name of the OERegionType for fragments perceived.

#### **SetSubstituentSearch**

bool SetSubstituentSearch (const OEChem:: OESubSearch& subsearch)

Sets an OESubSearch for custom substituents to be added to the Bemis-Murcko framework.

#### **SetUnsaturatedHeteroBonds**

void SetUnsaturatedHeteroBonds (bool includeUnsaturatedHeteroBonds)

Sets whether side chains beginning with unsaturated bonds to hetero atoms will be included in the main Bemis-Murcko framework. To be included in the main framework when this option is true, the beginning atom of the sidechain must satisfy the OEIsHetero predicate and the bond from the framework to this sidechain must have order greater than one.

#### **Validate**

bool Validate() const

Returns true is the current settings in the options class are valid.

#### **OECreateMMPIndexOptions**

#### class OECreateMMPIndexOptions

This class represents the OECreateMMPIndexOptions class that encapsulates properties to control a matched pair indexing analysis.

#### See also:

- OEMatchedPairAnalyzer class
- OEMatchedPairAnalyzerOptions class

#### **Constructors**

```
OECreateMMPIndexOptions()
OECreateMMPIndexOptions (const OEMatchedPairAnalyzerOptions &mmpopts)
```

Constructors that initialize an OECreateMMPIndexOptions object. The default constructor provides the following properties:

#### Table 1: Default parameters of OEMatchedPairAnalyzerOptions

| Property                                                                                | Default value                         |
|-----------------------------------------------------------------------------------------|---------------------------------------|
| processor type                                                                          | <i>OEMatchedPairProcessor_Default</i> |
| options                                                                                 | <i>OEMatchedPairOptions_Default</i>   |
| bond fragmentation limit                                                                | 20                                    |
| heavy atom filter                                                                       | 100                                   |
| indexable fragment filter based on min,max heavy atom percentage of the input structure | 85-100%                               |

#### **GetMaxRecord**

unsigned int GetMaxRecord() const

Return the maximum number of records to index from the input structure file or 0 to indicate all structures should be indexed.

#### **GetMMPOptions**

const OEMatchedPairAnalyzerOptions& GetMMPOptions() const

Returns the options controlling the Matched Pair indexing information.

#### **GetNumThreads**

unsigned int GetNumThreads () const

Returns the number of threads to use during the indexing phase. If the number of threads specified is 0, OEGetNumProcessors will be used to interrogate the maximum threads allowed.

#### **GetVerbose**

unsigned int GetVerbose() const

Return the level of output verbosity during the indexing activity.

#### **SetMaxRecord**

void SetMaxRecord (unsigned int maxrec)

Sets the maximum number of records to index from the input structure file. 0 indicates all structures should be indexed.

#### **SetNumThreads**

void SetNumThreads (unsigned int nthreads) const

Sets the maximum number of threads to use during the indexing phase. If nthreads is set to 0, OEGetNumProcessors will be used to interrogate the maximum threads allowed.

#### **SetTracer**

void SetTracer (const OESystem:: OEDots &dots)

Sets a tracer that can be used to show the progress of indexing.

#### See also:

• OEDots class in the OEChem TK manual

#### **SetVerbose**

void SetVerbose (unsigned int verbose)

Sets the level of output verbosity during the indexing activity. 0 (off), 1 (verbose), or 2 (very verbose) are sufficient values for output verbosity.

### **OECreateMMPIndexStatus**

class OECreateMMPIndexStatus

This class represents the OECreateMMPIndexStatus class that encapsulates returned status information from a matched pair indexing analysis.

#### See also:

· OECreateMMPIndexFile function

#### **Constructors**

```
OECreateMMPIndexStatus (bool valid=true)
OECreateMMPIndexStatus()
```

#### operator=

OECreateMMPIndexStatus& operator=(const OECreateMMPIndexStatus & rhs);

Assignment operator that copies the data of the 'rhs' OECreateMMPIndexStatus object.

#### operator+

OECreateMMPIndexStatus& operator+=(const OECreateMMPIndexStatus &addstatus);

Summation operator that increments the current instance based on data from the 'addstatus' OECreateMMPIndexStatus object.

#### **AddIndexedMol**

unsigned int AddIndexedMol()

Increment the internal count of indexed molecule records by one.

#### **AddUnindexedMol**

unsigned int AddUnindexedMol()

Increment the internal count of unindexed molecule records by one.

#### **GetNumMatchedPairs**

unsigned int GetNumMatchedPairs() const

Return the number of Matched Pairs generated from indexing.

#### **GetNumMols**

unsigned int GetNumMols () const

Return the internal count of indexed molecule records.

#### **GetTotalMols**

unsigned int GetTotalMols() const

Return the internal count of indexed plus unindexed molecule, (i.e., total) records.

#### **GetUnindexedMols**

unsigned int GetUnindexedMols() const

Return the internal count of unindexed molecule records.

#### **SetNumMatchedPairs**

void SetNumMatchedPairs (unsigned int mmps)

Sets the internal count for the number of Matched Pairs generated from indexing.

#### **SetNumMols**

void SetNumMols (unsigned int indexed)

Sets the internal count of indexed molecule records to the specified value.

#### **SetUnindexedMols**

void SetUnindexedMols (unsigned int unindexed)

Sets the internal count of unindexed molecule records to the specified value.

#### **SetValid**

void SetValid (bool valid)

Sets the boolean validity of this status class.

#### **OEMCSFragDatabase**

```
class OEMCSFragDatabase
```

This class represents the OEMCSFragDatabase class that performs a fragmentation indexing on an input set of structures to allow an MCS similarity search for similar compounds with common cores.

#### See also:

• OEMCSFragDatabaseOptions class

#### **Constructors**

OEMCSFragDatabase()

Default constructor that initializes the fragment database with the default options defined by OEMCSFragDatabaseOptions.

OEMCSFragDatabase (const OEMCSFragDatabaseOptions &options)

Constructor that initializes the fragment database with the options defined by the OEMCSFragDatabaseOptions argument.

#### **AddConstMol**

int AddConstMol(const OEChem::OEMolBase &inmol, int recordID = $(-1)$ )

Adds the molecule to the index and returns the 0-based recordID if the structure was successfully added, or a negative index if the structure was unable to be indexed. Negative values can be used to retrieve status information for indexing failures. The optional user-defined recordID is provided to allow indexed fragments to be referenced to externally maintained data structures. If the provided recordID is less than zero, an autogenerated index is returned which is an index greater than all ids seen so far.

- · OEMatchedPairIndexStatus
- · OEMatchedPairIndexStatusName

#### **AddMol**

 $int$  AddMol(OEChem::OEMolBase &inmol,  $int$  recordID= $(-1)$ )

A high performance version of *OEMCSFragDatabase.AddConstMol* that eliminates molecule copy activities and modifies the passed molecule directly. The state of the returned structure after indexing activities is *undefined* and should generally be discarded or reinstantiated from the original source for any subsequent activities.

#### **ClearIndexedMols**

```
void ClearIndexedMols()
```

This method discards the current index contents and frees internal memory in preparation for subsequent reindexing.

#### **CoreToMolecules**

```
OESystem:: OEIterBase<unsigned int>*
    CoreToMolecules (const std:: string &core) const
```

Given a fragmentation core, return the molecule ids that have this core from the index.

#### **CoreToMoleculeCount**

unsigned int CoreToMoleculeCount (const std::string &core) const

Given a fragmentation core, return a count of the number of molecules that have this core in the index.

#### **GetMaxCoreMolecule**

unsigned int GetMaxCoreMolecule (const char delim='.') const

Return the most common core fragment(s) recorded in the index. If there are multiple cores with the same occurrence count, the specified delim character is used to delimit the strings.

#### **GetMaxCoreMoleculeCount**

unsigned int GetMaxCoreMoleculeCount () const ;

Return the maximum core occurrence count recorded in the index.

### **GetMaxMolldx**

unsigned int GetMaxMolIdx() const

Returns the highest molecule id currently present in the index.

### **GetOptions**

const OEMCSFragDatabaseOptions &GetOptions () const

Returns the currently active options for the instance. Options cannot be changed, and require the desired options to be provided when the index is instantiated.

#### **GetScores**

```
OESystem:: OEIterBase<OEMedChem:: OEMCSMolSimScore> *
          GetScores (const OEChem:: OEMolBase & query,
                    unsigned int bqn = 0,
                    unsigned int end = 0,
                    unsigned int scorecounts = OEMCSScoreType:: Default,
                    const OEMCSSimFuncBase &scorefunc = OEMCSTanimotoSim()) const
```

Performs similarity calculations between a query molecule and the fragment cores stored in the OEMCSFragDatabase object. It returns an iterator over the calculated similarity scores (OEMCSMolSimScore). Each OEMCSMolSimScore object holds a similarity score, an index of database molecule and the fragment core in common between the hit and the query.

- bgn, end The bgn and end arguments define the segment of the database on which the similarity calculation will take place. If both of these parameters are omitted (or set to zero), then the similarity calculation is performed on the entire fragment database.
- scorecounts The value that defines the type of similarity scores (atom or bond) returned by the OEMCSFragDatabase. GetScores method. The default type is OEMCSScoreType AtomCount.
- **scorefunc** A class that computes the similarity score. By default this is *OEMCSTanimotoSim* but an implementation of OEMCSTverskySim is also provided. By providing a class derived from OEMCSSimFuncBase user-defined similarity measures other than the provided versions can be generated.

#### Note:

• By default, the OEMCSFragDatabase. GetScores method calculates Tanimoto atom similarity scores.

#### **GetSortedScores**

```
OESystem:: OEIterBase<OEMedChem:: OEMCSMolSimScore> *
          GetSortedScores (const OEChem:: OEMolBase & query,
                           unsigned int limit = 0,
                           unsigned int bgn = 0,
                           unsigned int end = 0,
                           bool descending = true,
                           unsigned int scorecounts = OEMCSScoreType:: Default,
                           const OEMCSSimFuncBase &scorefunc = OEMCSTanimotoSim())
\leftarrowconst
```

Performs similarity calculations between a query molecule and the fragment cores stored in the OEMCSFragDatabase object. It returns an iterator over the calculated similarity scores (OEMCSMolSimScore) in sorted order. Each OEMC-*SMolSimScore* object holds a similarity score an index of database molecule and the fragment core in common between the hit and query.

- limit The value that defines the number of similarity scores returned by the OEMCSFragDatabase. Get Sorted Scores method. If it is omitted (or set to zero) then all of the similarity scores are returned.
- bgn, end The bgn and end arguments define the segment of the database on which the similarity calculation will take place. If both of these parameters are omitted (or set to zero), then the similarity calculation is performed on the entire fragment database.
- descending A boolean value that indicates the direction of the sort values where  $\tau$  rue requests a descending sort and false requests ascending.
- scorecounts The value that defines the type of similarity scores (atom or bond) returned  $hv$ the OEMCSFragDatabase.GetSortedScores method. The default type is OEMCSScoreType\_AtomCount.
- scorefunc A class that computes the similarity score. By default this is OEMCSTanimotoSim but an implementation of OEMCSTverskySim is also provided. By providing a class derived from OEMCSSimFuncBase user-defined similarity measures other than the provided versions can be used.

#### Note:

• By default, the OEMCSFragDatabase. GetSortedScores method calculates Tanimoto atom similarity scores and returns the highest scores first.

**IsIndexed** 

bool IsIndexed (unsigned int recordID) const

Returns whether this record id is in the index.

#### **MoleculeToCores**

```
OESystem:: OEIterBase<const std:: string>*
     MoleculeToCores (const OEChem:: OEMolBase & mol,
                           bool permuteFragments=true)
```

Given a molecule, return the fragmentation cores using either the provided fragmentation options, or using the fragmentation options from the OEMCSFragDatabase instance. If the permuteFragments argument is true, all combinations of the generated fragmentation cores are generated, otherwise a unique set of multi-fragment cores is returned representing all combinations of bond fragmentations between the min and max cut limits.

Shown below are versions for two type of examples - one that uses an OEMCSFragDatabase instance so the database index options are used to control the fragmentation behavior and the other uses the free function and custom options.

```
# create an MCS fragment database with defaults
fragdb = oemedchem.OEMCSFragDatabase()
# use the options from the frag database to fragment an arbitrary input molecule
print ('MoleculeToCores using default fragment database options:')
sortedcores = sorted([c for c in fragdb.MoleculeToCores(mol)])
for corenum, core in enumerate (sortedcores) :
    print ('}): ()'. format (corenum, core))
```

```
# set the MCS fragment database options from the command-line arguments
fragopts = oemedchem.OEMCSFragDatabaseOptions()
if not oemedchem. OEConfigureMCSFragDatabaseOptions(itf):
    oechem. OEThrow. Fatal ("Error configuring options")
if not oemedchem. OESetupMCSFragDatabaseOptions (fragopts, itf):
    oechem. OEThrow. Fatal ("Error setting options")
# use the custom options to fragment an arbitrary input molecule
print ('MoleculeToCores using command-line options:')
sortedcores = sorted([c for c in oemedchem.OEMoleculeToCores(mol, fragopts)])
for corenum, core in enumerate (sortedcores) :
    print('}): {}'. format (corenum, core))
```

#### See also:

- OEMCSFragDatabaseOptions class
- OEMoleculeToCores function

#### **NumFragments**

unsigned int NumFragments () const

Returns the total number of fragment cores present in the index.

#### **NumMols**

unsigned int NumMols() const

Returns the total number of indexed molecules present in the index.

#### **ProcessMol**

int ProcessMol(OEChem:: OEMolBase &inmol)

Since the fragmentation engine used internally to generate the index modifies the input structures (eg discarding all but the largest fragment of the input), this method is provided to force the application of the indexing modifications on the input structure. This is generally useful for depiction or reporting of the returned similarity results.

#### **OEMCSFragDatabaseOptions**

class OEMCSFragDatabaseOptions

This class represents the OEMCSFragDatabaseOptions class that encapsulates properties to control an MCS fragmentation indexing.

#### See also:

• OEMCSFragDatabase class

#### **Constructors**

OEMCSFragDatabaseOptions()

Default constructor that initializes an OEMCSFragDatabaseOptions object with the following properties:

| Property                                                                                 | Default value                         |
|------------------------------------------------------------------------------------------|---------------------------------------|
| options                                                                                  | OEMatchedPairOptions_DefaultFragIndex |
| maximum allowed fragmentation bonds for indexed molecules                                | 20                                    |
| maximum allowed heavy atoms for indexed molecules                                        | 100                                   |
| indexable fragment filter based on min, max heavy atom percentage of the input structure | 85–100%                               |

#### Table 2: Default parameters of OEMCSFragDatabaseOptions

OEMCSFragDatabaseOptions (const OEMCSFragDatabaseOptions &options)

Copy constructor.

#### operator=

OEMCSFragDatabaseOptions & operator= (const OEMCSFragDatabaseOptions & rhs)

Assignment operator.

#### operator==

**bool operator == (const OEMCSFragDatabaseOptions & rhs)** 

Equality operator.

#### **ClearIndexableFragmentRange**

void ClearIndexableFragmentRange()

Clears the min-max range, which removes the fragment range filter and results in indexing fragments of all sizes.

#### **GetFragmentationLimit**

unsigned int GetFragmentationLimit() const

Return the bond fragmentation limit value.

#### GetIndexableFragmentRangeMax

float GetIndexableFragmentRangeMax() const

Return the maximum range of the indexable fragment filter.

#### GetIndexableFragmentRangeMin

float GetIndexableFragmentRangeMin() const

Return the minimum range of the indexable fragment filter.

#### **GetMaxAtomFilter**

unsigned int GetMaxAtomFilter() const

Return the maximum heavy atom filter value. Input structures with more than this number of heavy atoms will be rejected.

#### **GetMaxFragLimit**

```
unsigned int GetMaxFragLimit() const
```

Return the maximum number of fragmentation bonds that are allowed to be cut. Structures with more than this limit are not fragmented.

#### **GetMinFragLimit**

unsigned int GetMinFragLimit() const

Return the minimum number of fragmentation bonds that are allowed to be cut. Structures with less than this limit are not fragmented.

#### **GetOptions**

unsigned int GetOptions () const

Return the options setting value. The default is OEMatchedPairOptions\_DefaultFragIndex.

#### **GetRingFragLimit**

unsigned int GetRingFragLimit () const

Return the maximum number of ring fragmentation bonds that are allowed to be cut. Structures with more possible ring bonds than this limit will not have ring bonds fragmented.

#### HasIndexableFragmentHeavyAtomRange

bool HasIndexableFragmentHeavyAtomRange() const

Returns whether a min-max range has been specified.

#### **SetFragLimits**

bool SetFragLimits (unsigned int mincut, unsigned in maxcut)

Sets the min and max range of fragmentation bond cuts.

**Warning:** Very high limits for the allowed number of fragmentation bonds will have severe performance implications for indexing due to the combinatorial explosion in the number of fragmentation cores generated.

#### **SetFragmentationLimit**

bool SetFragmentationLimit (unsigned int limit)

Set the bond fragmentation limit. Any structures that generate more fragmentation bonds than this limit are rejected.

#### SetIndexableFragmentRange

bool SetIndexableFragmentRange (float minHeavyAtomPercent, float maxHeavyAtomPercent)

Sets the min-max heavy atom percentage range to request which fragment sizes should be indexed. The default is 85-100% of the input structures.

#### **SetMaxAtomFilter**

bool SetMaxAtomFilter (unsigned int numAtoms)

Sets the maximum heavy atom filter value. Input structures with more than this number of heavy atoms will be rejected for indexing.

#### **SetOptions**

**bool** SetOptions (unsigned int opts)

Set the options value. The default is OEMatchedPairOptions\_DefaultFragIndex.

#### **SetRingFragLimit**

bool SetRingFragLimit (unsigned int maxringcuts)

Sets maximum number of ring cuts allowed. Structures with more possible ring bonds than this limit will not have ring bonds fragmented.

Warning: Very high limits for the allowed number of ring fragmentation bonds will have severe performance implications for indexing due to the combinatorial explosion in the number of fragmentation cores generated.

#### **OEMCSMolSimScore**

class OEMCSMolSimScore

This class represents OEMCSMolSimScore that holds a similarity value, an index and a fragment core that identifies the molecule in the OEMCSFragDatabase index from which the score is calculated.

- · OEMCSFragDatabase.GetScores
- · OEMCSFragDatabase.GetSortedScores

#### **Constructors**

```
OEMCSMolSimScore()
OEMCSMolSimScore(const OEMCSMolSimScore & ref)
OEMCSMolSimScore (unsigned int i, double s, const std::string &coresmi)
```

Initializes an OEMCSMolSimScore from an index i and a score s and a core coresmi, or from another OEMCSMol-SimScore instance, or with default (null) values.

#### operator=

OEMCSMolSimScore & operator= (const OEMCSMolSimScore & ref)

Assignment operator.

#### **GetIdx**

unsigned int GetIdx() const

Returns the index of the indexed molecule corresponding to the similarity score.

#### **GetMCSCore**

```
std::string GetMCSCore() const
```

Returns the SMILES core relating the query and the indexed molecule corresponding to the similarity score.

#### **GetScore**

double GetScore() const

Returns the score that relates the query and the indexed molecule.

#### **Set**

void Set (unsigned int i, double s, const std:: string & coresmi)

Initializes an OEMCSMolSimScore from an index i and a score s and a core coresmi.

### **OEMCSSimFuncBase**

#### class OEMCSSimFuncBase

OEMCSSimFuncBase is an abstract base class which defines the interface necessary to perform similarity calculations that populate OEMCSMolSimScore objects.

The following classes derive from this class:

- OEMCSTanimotoSim
- OEMCSTverskySim

#### See also:

- OEMCSFragDatabase class
- · OEMCSFragDatabase. GetScores class
- · OEMCSFragDatabase.GetSortedScores class

#### **Constructors**

OEMCSSimFuncBase()

Default constructor.

#### operator()

```
double operator () (unsigned int commonAB,
                   unsigned int totalA,
                   unsigned int totalB) const
```

Virtual const operator that takes three count values and computes the similarity value. Depending on the method, the counts provided may be either the atom or bond counts for the MCS core, query molecule and indexed molecule.

#### **CreateCopy**

OEMCSSimFuncBase \*CreateCopy() const

OEMCSSimFuncBase. CreateCopy is a virtual constructor which allows copying of concrete derived objects using a reference to this base class.

#### **GetMCSSimTypeString**

```
std::string GetMCSSimTypeString() const
```

Returns a string representation of the concrete derived class.

#### **OEMCSTanimotoSim**

class OEMCSTanimotoSim : public OEMedChem:: OEMCSSimFuncBase

This class represents *OEMCSTanimotoSim* that calculates the Tanimoto similarity score.

#### Formula:

 $Sim_{Tanimoto}(A, B) = \frac{bothAB}{|A|+|B|-bothAB} = \frac{bothAB}{onlyA+onlyB+bothAB}$ 

The following methods are publicly inherited from OEMCSSimFuncBase:

operator() CreateCopy GetMCSSimTypeString

#### **Constructors**

OEMCSTanimotoSim()

Default constructor.

#### operator()

double operator () (unsigned int commonAB, unsigned int totalA, unsigned totalB) const

Returns the Tanimoto similarity coefficient based on the fragment core counts for the fragment core, query molecule and indexed molecule.

#### **CreateCopy**

OEMedChem:: OEMCSSimFuncBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEMCSTanimotoSim object is dynamically allocated and owned by the caller.

#### **GetMCSSimTypeString**

std::string GetMCSSimTypeString() const

Returns a string representation of the OEMCSTanimotoSim class.

#### **OEMCSTverskySim**

class OEMCSTverskySim : public OEMedChem:: OEMCSSimFuncBase

This class represents OEMCSTverskySim that calculates the Tversky similarity score.

#### Formula:

 $Sim_{Tversky}(A, B) = \frac{bothAB}{\alpha * only A + \beta * only B + both AB}$ 

The following methods are publicly inherited from OEMCSSimFuncBase:

operator() CreateCopy GetMCSSimTypeString

#### **Constructors**

OEMCSTverskySim()

Default constructor ( $\alpha = 0.95$ ,  $\beta = 0.05$ )

OEMCSTverskySim(double tvAlpha =  $0.95$ , double tvBeta =  $0.05$ )

Constructor with arbitrary  $\alpha$  and  $\beta$  parameters.

#### operator()

double operator () (unsigned int commonAB, unsigned int totalA, unsigned totalB) const

Returns the Tversky similarity coefficient based on the fragment core counts for the fragment core, query molecule and indexed molecule.

#### **CreateCopy**

OEMedChem:: OEMCSSimFuncBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEMCSTverskySim object is dynamically allocated and owned by the caller.

#### **GetAlpha**

double GetAlpha() const

Returns the  $\alpha$  parameter from the *OEMCSTverskySim* class.

#### **GetBeta**

double GetBeta() const

Returns the  $\beta$  parameter from the OEMCSTverskySim class.

#### **GetMCSSimTypeString**

std::string GetMCSSimTypeString() const

Returns a string representation of the OEMCSTverskySim class.

#### **OEMatchedPairAnalyzer**

class OEMatchedPairAnalyzer

This class represents the OEMatchedPairAnalyzer class that performs a matched pair indexing analysis on an input set of structures.

#### See also:

• OEMatchedPairAnalyzerOptions class

#### **Constructors**

OEMatchedPairAnalyzer()

Default constructor that initializes the analysis engine with the default options defined by *OEMatchedPairAnalyze*rOptions.

OEMatchedPairAnalyzer(const OEMatchedPairAnalyzerOptions &options)

Constructor that initializes the analysis engine with the options defined by the OEMatchedPairAnalyzerOptions argument.

#### **AddMol**

int AddMol(const OEChem:: OEMolBase &inmol, int recordID= $(-1)$ )

Add the molecule to the index and return the 0-based recordID if the structure was successfully added, or a negative index if the structure was unable to be indexed. Negative values can be used to retrieve status information detail for indexing failures. The optional user-defined recordID is provided to allow indexed matched pairs to be referenced to externally maintained data structures. If the provided recordID is less than zero, an autogenerated index is returned which is an index greater than all ids seen so far.

- · OEMatchedPairIndexStatus
- · OEMatchedPairIndexStatusName

### **GetMaxMolldx**

```
unsigned int GetMaxMolIdx() const
```

Returns one more than the maximum molecule index this Matched Pair index currently contains.

#### **GetMolecule**

```
bool GetMolecule (OEChem::OEMolBase & mol, unsigned int molID, bool includeData=true).
\rightarrowconst
```

Returns the molecule referenced by molID in the index. An optional includeData argument controls whether generic data present on the molecule at index time is also returned.

#### **GetOptions**

const OEMatchedPairAnalyzerOptions &GetOptions () const

#### See also:

• OEMatchedPairAnalyzerOptions class

#### **GetProcessorID**

const char \*GetProcessorID() const

Returns a character string name of the processor type.

#### See also:

· OEMatchedPairProcessorName class

#### **GetProcessorType**

unsigned int GetProcessorType() const

Returns a constant representing the processor type in use.

#### See also:

• OEMatchedPairProcessor

#### **IsIndexed**

int IsIndexed (unsigned int recordID) const

Returns whether the specified record id has been indexed.

#### **NumIndexNodes**

unsigned int NumIndexNodes () const

Return a count of the number of index nodes currently present in the index.

#### **NumMatchedPairs**

unsigned int NumMatchedPairs() const

Return a count of the number of matched molecular pairs currently present in the index.

#### **NumMols**

unsigned int NumMols() const

Return a count of the number of molecules that have currently been added to the index.

#### **ModifyOptions**

bool ModifyOptions (unsigned int addopts, unsigned int delopts)

An active analyzer has a limited set of options that can be altered once it has been instantiated as many of the options affect the internal indexing contents. This method can be used to alter any options that do not affect the internal index state.

#### See also:

· OEMatchedPairOptions

#### **OEMatchedPairAnalyzerOptions**

class OEMatchedPairAnalyzerOptions

This class represents the OEMatchedPairAnalyzerOptions class that encapsulates properties to control a matched pair analysis.

#### See also:

• OEMatchedPairAnalyzer class

### **Constructors**

OEMatchedPairAnalyzerOptions()

Default constructor that initializes an OEMatchedPairAnalyzerOptions object with the following properties:

#### Table 3: Default parameters of OEMatchedPairAnalyzerOptions

| Property                                                                                   | Default value                         |
|--------------------------------------------------------------------------------------------|---------------------------------------|
| processor type                                                                             | <i>OEMatchedPairProcessor_Default</i> |
| options                                                                                    | <i>OEMatchedPairOptions_Default</i>   |
| bond fragmentation limit                                                                   | 20                                    |
| heavy atom filter                                                                          | 100                                   |
| indexable fragment filter based on min,max heavy atom<br>percentage of the input structure | $85-100\%$                            |

OEMatchedPairAnalyzerOptions (const OEMatchedPairAnalyzerOptions & rhs)

Copy constructor.

#### operator=

OEMatchedPairAnalyzerOptions & operator=(const OEMatchedPairAnalyzerOptions & rhs)

Assignment operator.

#### ClearIndexableFragmentRange

void ClearIndexableFragmentRange()

Clears the min-max range, which removes the fragment range filter and results in indexing fragments of all sizes.

#### **GetFragmentationLimit**

unsigned int GetFragmentationLimit() const

Return the bond fragmentation limit value.

#### GetIndexableFragmentRangeMax

float GetIndexableFragmentRangeMax() const

Return the maximum range of the indexable fragment filter.

#### GetIndexableFragmentRangeMin

float GetIndexableFragmentRangeMin() const

Return the minimum range of the indexable fragment filter.

#### **GetMaxAtomFilter**

unsigned int GetMaxAtomFilter() const

Return the maximum heavy atom filter value. Input structures with more than this number of heavy atoms will be rejected.

#### **GetOptions**

unsigned int GetOptions () const

Return the options setting value. The default is OEMatchedPairOptions\_Default.

#### **GetProcessorType**

unsigned int GetProcessorType() const

Return the processor type. The type using the default constructor is OEMatchedPairProcessor\_Default

#### HasIndexableFragmentHeavyAtomRange

bool HasIndexableFragmentHeavyAtomRange() const

Returns whether a min-max range has been specified.

#### **ModifyOptions**

bool ModifyOptions (unsigned int addopts, unsigned int delopts)

An active analyzer has a limited set of options that can be altered once it has been instantiated as many of the options affect the internal indexing contents. This method can be used to alter any options that do not affect the internal index state.

#### **SetFragmentationLimit**

```
bool SetFragmentationLimit (unsigned int limit)
```

Set the bond fragmentation limit. Any structures that generate more fragmentation bonds than this limit are rejected.

#### SetIndexableFragmentRange

bool SetIndexableFragmentRange (float minHeavyAtomPercent, float maxHeavyAtomPercent)

Sets the min-max heavy atom percentage range to request which fragment sizes should be indexed. The default is 85-100% of the input structures.

#### **SetMaxAtomFilter**

bool SetMaxAtomFilter (unsigned int numAtoms)

Sets the maximum heavy atom filter value. Input structures with more than this number of heavy atoms will be rejected for indexing.

#### **SetOptions**

**bool** SetOptions (unsigned int opts)

Set the options value. The default is OEMatchedPairOptions\_Default.

#### **SetProcessorType**

bool SetProcessorType (unsigned int processorType=OEMatchedPairProcessor::Default)

Sets the index processor type to the requested value.

#### See also:

· OEMatchedPairProcessor constants

#### **OEMatchedPair**

class OEMatchedPair

This class identifies a specific matched molecular pair.

#### **Constructors**

```
OEMatchedPair(const OEMatchedPair & rhs)
OEMatchedPair (unsigned int fromIndex=0u, unsigned int toIndex=0u, const char
\leftrightarrow from Smiles=0,
               const char *toSmiles=0)
```

Constructs an object from the passed arguments.

#### operator=

```
OEMatchedPair & operator= (const OEMatchedPair & rhs)
```

Assignment operator that copies the data of the 'rhs' OEMatchedPair object.

#### **AddSDData**

```
bool AddSDData (const std::string &tag, const std::string &fromValue,
               const std:: string &toValue)
```

Add SD data information to the matched pair. The tag is the field name of the SD data and the from and to arguments indicate the respective data for the molecular pair.

#### **ClearSDData**

void ClearSDData()

Deletes all SD data recorded for the molecular pair.

#### **CreateCopy**

OEMatchedPair \*CreateCopy() const

#### **FromIndex**

unsigned int FromIndex() const

This is the from index of the matched molecular pair.

#### **FromSmiles**

const std:: string & From Smiles () const

This is the from SMILES string of the matched molecular pair.

#### **GetDataTags**

OESystem:: OEIterBase<const std:: string> \*GetDataTags() const

This method returns an iterator of over the SD data field tags recorded for the matched molecular pair.

#### **GetFromSDData**

std::string GetFromSDData(const std::string &tag)

This method returns SD data with the specified 'tag' for the from structure of the matched molecular pair.

#### **GetSDData**

bool GetSDData (const std:: string &tag, std:: string &fromValue, std::string &toValue) const

This method returns SD data for the specific data field requested for the matched molecular pair. If either of the from or to structures have no data present, an empty string is returned.

#### **GetToSDData**

std::string GetToSDData(const std::string &tag)

This method returns SD data with the specified 'tag' for the to structure of the matched molecular pair.

#### **HasSDData**

bool HasSDData (const std:: string &tag) const

This method returns a boolean indicating whether SD data of field name 'tag' is present for either of the from or to structures.

#### **NumDataTags**

unsigned int NumDataTags() const

This method returns the number of SD data tags present for the molecular pair.

#### **ToIndex**

unsigned int ToIndex() const

This is the to index of the matched molecular pair.

#### **ToSmiles**

const std:: string &ToSmiles () const

This is the to SMILES string of the matched molecular pair.

#### **OEMatchedPairTransform**

class OEMatchedPairTransform

This class embodies a unique transformation that relates one or more matched molecular pairs.

#### **Constructors**

```
OEMatchedPairTransform()
OEMatchedPairTransform(const OEMatchedPairTransform & rhs)
OEMatchedPairTransform(const std::string &xformString,
                       int context=OEMatchedPairContext::Default)
OEMatchedPairTransform(const std::string &ForwardXForm,
                       const std:: string & ReverseXForm,
                       int context=OEMatchedPairContext::Default)
```

Constructs an object from the passed arguments.

#### operator=

OEMatchedPairTransform & operator= (const OEMatchedPairTransform & rhs)

Assignment operator that copies the data of the 'rhs' OEMatchedPairTransform object.

### **AddMatchedPair**

```
bool AddMatchedPair (const OEMatchedPair & mmp)
bool AddMatchedPair (unsigned int fromIndex, const std::string &fromSmiles,
                     unsigned int toIndex, const std:: string &toSmiles)
```

This method links a specific from and to structure to the transform.

#### **CreateCopy**

```
OEMatchedPairTransform *CreateCopy() const
```

#### **GetMatchedPairContext**

int GetMatchedPairContext() const

Returns the chemistry context type for the transformation.

#### See also:

· OEMatchedPairContext

#### **GetMatchedPairs**

```
OESystem::OEIterBase<OEMatchedPair> *GetMatchedPairs() const
OESystem::OEIterBase<OEMatchedPair> *GetMatchedPairs(unsigned int fromORtoIndex) const
OESystem::OEIterBase<OEMatchedPair> *GetMatchedPairs (unsigned int fromIndex, unsigned
\leftrightarrowint toIndex) const
```

Returns an iterator of the all the matched pairs associated with this transformation, or restricts the returned matched pairs that meeting the from or to index constraint.

#### See also:

• OEMatchedPair

### **GetMolecule**

```
bool GetMolecule (unsigned int index, std:: string &molsmi) const
std::string GetMolecule (unsigned int index) const
```

This method retrieves the molecule of the specified molecule id from the transform.

### **GetMoleculeTitle**

```
bool GetMoleculeTitle (unsigned int index, std::string &name)
std::string GetMoleculeTitle(unsigned int index)
```

This method returns a molecule title for the passed molecule index.

#### **GetTransform**

const std:: string & GetTransform() const

Returns the reaction transformation string that can be used to instantiate a OEUniMolecularRxn object.

#### **HasMatchedPair**

```
bool HasMatchedPair (unsigned int FromOrToIndex) const
bool HasMatchedPair (unsigned int fromIndex, unsigned int toIndex) const
```

Returns a boolean to indicate if the specific molecule pair is registered with this transformation.

#### **Invert**

bool Invert()

Reverses the direction of the transform and the matched pair information for the transformation.

If the transform was extracted with SMART query qualifiers for use in molecule **Warning:** transformation activities, the inversion of the transform will result in the query features moved to the product side of the reaction. Inverting transformations is only meaningful when using the OEMatchedPairTransformExtractMode\_NoSMARTS extraction option.

**NumMatchedPairs** 

unsigned int NumMatchedPairs () const

Returns a count of the number of matched molecular pairs registered with this transformation.

#### **SetMoleculeTitle**

bool SetMoleculeTitle (unsigned int index, const std::string &name)

This method set the molecule title for the passed molecule index.

#### **SetTransform**

```
bool SetTransform(const std::string &xform, int context=OEMatchedPairContext::Default)
bool SetTransform (const std::string &ForwardXForm, const std::string &ReverseXForm,
\rightarrowint context=OEMatchedPairContext::Default)
```

Sets the internal reaction transformation string.

#### **OEMatchedPairTransformExtractOptions**

class OEMatchedPairTransformExtractOptions

This class represents the OEMatchedPairTransformExtractOptions class that encapsulates properties that control extraction of matched molecular pair transformations.

#### See also:

- OEMatchedPairAnalyzer class
- · OEMatchedPairGetTransformsfunction

#### **Constructors**

OEMatchedPairTransformExtractOptions()

Default constructor that initializes an OEMatchedPairTransformExtractOptions object with the following properties:

#### Table 4: Default parameters of OEMatchedPairTransformExtractOptions

| Property                                                                    | Default value                                    |
|-----------------------------------------------------------------------------|--------------------------------------------------|
| transformation context                                                      | <i>OEMatchedPairContext_Default</i>              |
| extraction options                                                          | <i>OEMatchedPairTransformExtractMode_Default</i> |
| maximum matched pair core structure substituents                            | 200                                              |
| skip maximum matched pair core index nodes exceed-<br>ing substituent limit | false                                            |

OEMatchedPairTransformExtractOptions(const OEMatchedPairTransformExtractOptions & rhs)

Copy constructor.

#### operator=

```
OEMatchedPairTransformExtractOptions &operator=(const
→OEMatchedPairTransformExtractOptions & rhs)
```

Assignment operator.

#### **GetAttachmentPoints**

bool GetAttachmentPoints() const

Returns the setting that requests the addition of attachment points on the matched pair transformation.

#### **GetContext**

int GetContext () const

Returns the setting that controls the amount of core chemistry adjacent to the substituent attachment site for the matched pairs.

#### See also:

· OEMatchedPairContext Default

#### **GetDirection**

```
unsigned int GetDirection() const
```

Returns the setting that controls the direction for the returned matched pair transformation. One OEMatchedPairTransformExtractMode Forward, of OEMatchedPairTransformExtractMode\_Backward,(OEMatchedPairTransformExtractMode\_Forward | OEMatchedPairTransformExtractMode\_Backward) ' (both) or OEMatchedPairTransformExtractMode\_Sorte are supported. For OEMatchedPairTransformExtractMode\_Sorted, the transformation is lexically sorted based on the reactants and products and may need to be inverted to have the transformation represent driving an arbitrary data property associated with the matched pair in a desired direction.

#### See also:

- · OEMatchedPairTransformExtractMode Default
- · OEMatchedPairTransform. Invert

#### **GetIsotopes**

```
bool GetIsotopes () const
```

Returns the setting that controls the generalization of the returned transformations for isotopic substitutions.

#### **GetMCSCorrespondence**

bool GetMCSCorrespondence() const

Returns the setting that requests the addition of atom-atom mapping correspondence to the core of the matched pair transformation.

#### **GetMatchedPairData**

bool GetMatchedPairData() const

Returns whether the matched pair data is included in the matched pair transformation. If only the transformation itself is required, there may not be a need for extraction of related matched pair indexed data.

#### **GetMatchedPairs**

bool GetMatchedPairs() const

Returns whether the matched pair data ids are returned for the matched pair transformation. If only the transformation itself is required, there may not be a need for extraction of related matched pair indices.

#### **GetMaxMMPLimit**

unsigned int GetMaxMMPLimit() const

Returns the requested upper limit of matched pairs for the extracted transformations.

#### GetMaxSubstituentLimit

unsigned int GetMaxSubstituentLimit() const

Returns the setting for the maximum number of indexed core substituents that should be processed into matched pair transformations.

Warning: Setting this limit to 0 will suppress any core structure truncation or skipping activities, but may result in extremely poor transformation extraction performance owing to the combinatorial explosion of generating all NxM combinations of matched pairs.

#### GetMaxSubstituentLimitSkip

bool GetMaxSubstituentLimitSkip() const

Returns whether the matched pair core structures in the index that have more than the OEMatchedPairTransformExtractOptions.GetMaxSubstituentLimit number of substituents are processed into matched pair transformation entries. If the setting is true, cores that exceed the limit are skipped, and if false, the substituent list is truncated to the first OEMatchedPairTransformExtractOptions. GetMaxSubstituentLimit substituents, if non-zero.

#### **GetMinMMPLimit**

```
unsigned int GetMinMMPLimit() const
```

Returns the requested lower limit of matched pairs for the extracted transformations.

#### **GetMinSubstituentLimit**

unsigned int GetMinSubstituentLimit() const

Returns the setting for the minimum number of core structure substituents for index nodes that should be processed into matched pair transformations.

#### **GetOptions**

unsigned int GetOptions () const

Returns the bit option settings for the extraction options.

#### See also:

· OEMatchedPairTransformExtractMode

#### **GetSMARTS**

bool GetSMARTS () const

Returns whether the matched pair transformations are annotated with additional SMARTS qualifiers to make the transformations more chemically relevant when used for generating chemical transformations from extracted matched pairs.

#### **SetAttachmentPoints**

```
bool SetAttachmentPoints (bool val)
```

Set the option that controls the addition of attachment points on the matched pair transformation.

#### **SetContext**

**bool** SetContext (int context)

Sets the option that that controls the amount of core chemistry adjacent to the substituent attachment site in then matched pair transformation.

#### See also:

· OEMatchedPairContext\_Default

#### **SetDirection**

bool SetDirection (unsigned int direction)

Sets the specified transformation direction for the returned matched pair transformation. One of Forward, Backward, (Forward | Backward) (both) or Sorted are supported. For Sorted, the transformation is lexically sorted based on the reactants and products and may need to be inverted to have the transformation represent driving an arbitrary data property associated with the matched pair in a desired direction.

#### See also:

- · OEMatchedPairTransformExtractMode Default
- · OEMatchedPairTransform. Invert

#### **SetIsotopes**

**bool** SetIsotopes (bool require)

Sets the option that controls whether the transformation is allowed to be generalized for isotopic substitutions. If true, isotopic information will be included in the transformations for the chemical modifications.

#### **SetMCSCorrespondence**

```
bool SetMCSCorrespondence (bool add)
```

Sets the option that requests the addition of atom-atom mapping correspondence to the core of the matched pair transformation.

#### **SetMatchedPairData**

bool SetMatchedPairData (bool enable)

Sets the option that requests matched pair data be included in the matched pair transformation. If only the transformation itself is required, there may not be a need for extraction of related matched pair indexed data, so the data extraction can be disabled.

#### **SetMatchedPairs**

bool SetMatchedPairs (bool enable)

Sets the option that requests that matched pair structure ids are returned for the matched pair transformation. If only the transformation itself is required, there may not be a need for extraction of related matched pair structure indices.

#### SetMaxSubstituentLimitSkip

bool SetMaxSubstituentLimitSkip(bool skip)

Sets the option that controls whether the matched pair core structures in the index that have more than the OEMatchedPairTransformExtractOptions. GetMaxSubstituentLimit number of substituents are processed into matched pair transformation entries. If the setting is true, cores that exceed the limit are skipped, and if false, the substituent list is truncated to the first OEMatchedPairTransformExtractOptions. GetMaxSubstituentLimit substituents, if non-zero.

#### **SetMMPLimit**

bool SetMMPLimit (unsigned int atLeast, unsigned int atMost=0)

Sets the requested range limits for the number matched pairs in the extracted transformations.

#### **SetSubstituentLimit**

bool SetSubstituentLimit (unsigned int atLeast, unsigned int atMost=0)

Sets the requested range limits for the core structure index nodes to constrain processing to core index nodes matching the specified range.

**Warning:** Setting the maximum limit to  $\theta$  will suppress any core structure truncation or skipping activities, but may result in extremely poor transformation extraction performance owing to the combinatorial explosion of generating all NxM combinations of matched pairs and their associated transformations and data.

#### **SetOptions**

**bool** SetOptions (unsigned int options)

Sets the bit option settings that control the transformation extraction activities.

#### See also:

· OEMatchedPairTransformExtractMode

#### **SetSMARTS**

bool SetSMARTS (bool enable)

Sets the option that indicates that matched pair transformations should be annotated with additional SMARTS qualifiers to make the transformations more chemically relevant when used for generating chemical transformations from extracted matched pairs.

## **4.1.2 OEMedChem Constants**

#### **OEMCSFragDatabaseSetup**

This namespace encodes symbolic constants used as bit-masks to indicate which MCS fragmentation indexing parameters are being created when invoking the OEConfigureMCSFragDatabaseOptions function.

#### See also:

• OEMCSFragDatabaseOptions class

#### All

#### The combination of following constants:

- · OEMCSFragDatabaseSetup\_AllFrags
- · OEMCSFragDatabaseSetup\_BondFragLimit
- · OEMCSFragDatabaseSetup\_FragCutsRange
- · OEMCSFragDatabaseSetup\_FragMinMaxRange
- · OEMCSFragDatabaseSetup\_FragmentationCuts
- · OEMCSFragDatabaseSetup\_HeavyAtomLimit
- · OEMCSFragDatabaseSetup\_IndexHydrogenSites
- · OEMCSFragDatabaseSetup\_RingCuts

#### **AllFrags**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure all fragment indexing.

```
Contents of parameter -allfrags
   Aliases : -all
   Type : bool
   Allow list : false
   Default : false
   Simple : true
   Required : false
   Brief : Index all fragment sizes, ignore fragment heavy atom percentage
```

See also:

- · OEMCSFragDatabaseOptions. HasIndexableFragmentHeavyAtomRange method
- · OEMCSFragDatabaseOptions. ClearIndexableFragmentRange method
- · OESetupMCSFragDatabaseOptions

#### **BondFragLimit**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure maximum number of fragmentation bonds allowed.

```
Contents of parameter -bondfraglimit
   Aliases : -blim
   Type : int
   Allow list : false
   Default : 20
   Simple : true
   Required : false
   Brief : Bond fragmentation limit
```

#### See also:

- · OEMCSFragDatabaseOptions. SetFragmentationLimit method
- · OESetupMCSFragDatabaseOptions

#### **FragCutsRange**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure the minimum and maximum fragmentation bond cuts allowed.

```
Contents of parameter -minfragcuts
   Aliases : - mincuts
   Type : int
   Allow list : false
   Default : 1
   Simple : true
   Required : false
```

```
Legal ranges :
       1 to 100
   Brief : Minimum number of fragmentation cuts allowed
Contents of parameter -maxfragcuts
   Aliases : - maxcuts
   Type : int
   Allow list : false
   Default : 3
   Simple : true
   Required : false
   Legal ranges :
       1 to 100
   Brief : Maximum number of fragmentation cuts allowed
```

See also:

- · OEMCSFragDatabaseOptions. SetFragLimits method
- OESetupMCSFragDatabaseOptions

#### **FragMinMaxRange**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure the min and max allowed fragment sizes to be indexed.

```
Contents of parameter -fragGe
   Aliases : -ge
   Type : float
   Allow list : false
   Default : 85.0
   Simple : true
   Required : false
   Legal ranges :
       0.0 to 100.0Brief : fragments greater than or equal to this heavy atom percentage
Contents of parameter -fragLe
   Aliases : -le
   Type : float
   Allow list : false
   Default : 100.0
   Simple : true
   Required : false
   Legal ranges :
        0.0 to 100.0Brief : fragments less than or equal to this heavy atom percentage
```

- · OEMCSFragDatabaseOptions. SetIndexableFragmentRange method
- · OESetupMCSFragDatabaseOptions

#### **FragmentationCuts**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure the fragmentation bond cut combinations to be performed.

```
Contents of parameter -fragcuts
   Aliases : - cuts
   Type : string
   Allow list : true
   Default : All
   Simple : true
   Required : false
   Legal values : Single Double Triple All
   Brief : Fragmentation bond combinations
   Detail
```

See also:

- OESetupMCSFragDatabaseOptions
- OEMCSFragDatabaseOptions. SetOptions method
- · OEMatchedPairOptions\_SingleCuts constant
- · OEMatchedPairOptions\_DoubleCuts constant
- · OEMatchedPairOptions\_TripleCuts constant
- · OEMatchedPairOptions\_AllCuts constant

#### **HeavyAtomLimit**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure the limit for the maximum number of heavy atoms allowed for an indexed molecule.

```
Contents of parameter -atomlimit
   Aliases : -alim
   Type : int
   Allow list : false
   Default : 100
   Simple : true
   Required : false
   Brief : Heavy atom limit
```

- · OEMCSFragDatabaseOptions. SetMaxAtomFilter method
- · OESetupMCSFragDatabaseOptions

#### **IndexHydrogenSites**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure whether matched pairs that differ simply by hydrogen substitution is allowed.

```
Contents of parameter -indexhydsites
   Aliases : -indexh
   Type : bool
   Allow list : false
   Default : true
   Simple : true
   Required : false
   Brief : Index hydrogen sites
```

See also:

- OEMCSFragDatabaseOptions. SetOptions method
- · OEMatchedPairOptions\_IndexHSites constant
- · OESetupMCSFragDatabaseOptions

#### **RingCuts**

Passing this constant to the OEConfigureMCSFragDatabaseOptions function results in generating the following default interface to configure the maximum number of ring cuts allowed.

```
Contents of parameter -ringcuts
   Aliases : -ring
   Type : int
   Allow list : false
   Default : 0
   Simple : true
   Required : false
   Brief : Maximum number of ring fragmentation cuts allowed (0: disabled)
```

See also:

- · OEMCSFragDatabaseOptions. SetRingFragLimit method
- · OESetupMCSFragDatabaseOptions

#### **OEMCSScoreType**

This namespace contains constants representing various supported similarity computations.

### **Undefined**

This constant represents an undefined or illegal context state.

#### **AtomCount**

This constant represents a request for atom counts that relate the fragment core, query and indexed molecule.

#### **BondCount**

This constant represents a request for bond counts that relate the fragment core, query and indexed molecule.

#### **Default**

This constant represents the default score type setting of OEMCSScoreType\_AtomCount.

#### **OEMatchedPairAnalyzerFileType**

This namespace contains constants representing supported matched pair analysis serialization export types.

#### **MMPIndex**

This constant identifies the only currently supported serialization type for an OEMatchedPairAnalyzer object.

#### **MCSFrags**

This constant identifies the only currently supported serialization type for an OEMCSFragDatabase object.

#### **UNDEFINED**

This constant represents any unknown file type for index serialization.

#### **OEMatchedPairContext**

This namespace contains constants representing various supported context requests for matched pair transformations.

#### **Undefined**

This constant represents an undefined or illegal context state.

#### **AllBonds**

This constant represents a request for the most explicit chemistry context for the transformation information.

#### Bond<sub>0</sub>

This constant represents a request for 0-bonds of chemistry context in the returned transformation information. This constant represents a request for the most general context for the transformation information.

#### Bond1

This constant represents a request for 1-bond of chemistry context in the returned transformation information.

#### Bond<sub>2</sub>

This constant represents a request for 2-bonds of chemistry context in the returned transformation information.

#### Bond<sub>3</sub>

This constant represents a request for 3-bonds of chemistry context in the returned transformation information.

#### **Default**

This constant represents the default transformation context setting of OEMatchedPairContext Bond1.

#### **OEMatchedPairIndexSetup**

This namespace encodes symbolic constants used as bit-masks to indicate which matched pair indexing parameters are being created when invoking the OEConfigureMatchedPairIndexOptions function.

#### See also:

• OEMatchedPairAnalyzerOptions class

### All

#### The combination of following constants:

- · OEMatchedPairIndexSetup\_BondFragLimit
- · OEMatchedPairIndexSetup\_FragMinMaxRange
- · OEMatchedPairIndexSetup\_FragmentationCuts
- · OEMatchedPairIndexSetup\_HeavyAtomLimit
- · OEMatchedPairIndexSetup\_IndexHydrogenSites
- · OEMatchedPairIndexSetup ProcessorType
- · OEMatchedPairIndexSetup\_UniquesOnly

### **BondFragLimit**

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to configure maximum number of fragmentation bonds allowed.

```
Contents of parameter -bondfraglimit
   Aliases : - blim
   Type : int
   Allow list : false
   Default : 20
   Simple : true
    Required : false
    Brief : Bond fragmentation limit
```

See also:

· OEMatchedPairAnalyzerOptions. SetFragmentationLimit method

#### **FragMinMaxRange**

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to configure the min and max allowed fragment sizes to be indexed.

```
Contents of parameter -fragGe
   Aliases : -ge
   Type : float
   Allow list : false
   Default : 85.0
   Simple : true
   Required : false
   Legal ranges :
       0.0 to 100.0Brief : fragments greater than or equal to this heavy atom percentage
Contents of parameter -fraqLe
   Aliases : -le
   Type : float
   Allow list : false
   Default : 100.0
   Simple : true
   Required : false
   Legal ranges :
       0.0 to 100.0Brief : fragments less than or equal to this heavy atom percentage
```

#### See also:

· OEMatchedPairAnalyzerOptions. SetIndexableFragmentRange method

#### **FragmentationCuts**

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to configure the fragmentation bond cut combinations to be performed.

```
Contents of parameter -fragcuts
  Aliases : - cuts
   Type : string
   Allow list : true
  Default: All
   Simple : true
   Required : false
   Legal values : Single Double Triple All
   Brief : Fragmentation bond combinations
   Detail
```

- · OEMatchedPairAnalyzerOptions. SetOptions method
- · OEMatchedPairOptions\_SingleCuts constant
- · OEMatchedPairOptions\_DoubleCuts constant
- · OEMatchedPairOptions\_TripleCuts constant
- · OEMatchedPairOptions\_AllCuts constant

#### **HeavyAtomLimit**

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to configure the limit for the maximum number of heavy atoms allowed for an indexed molecule.

```
Contents of parameter -atomlimit
   Aliases : -alim
   Type : int
   Allow list : false
   Default : 100Simple : true
   Required : false
   Brief : Heavy atom limit
```

See also:

· OEMatchedPairAnalyzerOptions. SetMaxAtomFilter method

#### IndexHydrogenSingleCuts

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to configure whether matched pairs that differ simply by hydrogen substitution specifically at single cuts sites only.

```
Contents of parameter -indexhydlcuts
  Aliases : -indexhlcuts
  Type : bool
  Allow list : false
  Default : false
  Simple : true
  Required : false
  Brief : Index hydrogen members for single cuts only
```

See also:

- · OEMatchedPairAnalyzerOptions. SetOptions method
- · OEMatchedPairOptions\_IndexHSingleCuts constant

#### **IndexHydrogenSites**

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to configure whether matched pairs that differ simply by hydrogen substitution is allowed for all fragmentation cut types.

```
Contents of parameter -indexhydsites
   Aliases : -indexh
   Type : bool
   Allow list : false
```

```
Default : true
Simple : true
Required : false
Brief : Index hydrogen sites
```

#### See also:

- · OEMatchedPairAnalyzerOptions. SetOptions method
- · OEMatchedPairOptions\_IndexHSites constant

#### **ProcessorType**

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to select the type of fragmentation processor to be used during indexing.

```
Contents of parameter -processortype
   Aliases : -ptype
   Type : string
   Allow list : false
   Default : Default
   Simple : true
   Required : false
   Legal values : Undefined Default HussainRea BemisMurcko HR BM
   Brief : Processor type
   Detail
```

See also:

- OEMatchedPairAnalyzerOptions. SetProcessorType method
- · OEMatchedPairProcessor namespace

#### **UniquesOnly**

Passing this constant to the OEConfigureMatchedPairIndexOptions function results in generating the following default interface to configure whether duplicate structures are allowed to be indexed.

```
Contents of parameter -unique
   Aliases : -u
   Type : bool
   Allow list : false
   Default : true
   Simple : true
   Required : false
   Brief : Unique molecules only
```

- · OEMatchedPairAnalyzerOptions. SetOptions method
- · OEMatchedPairOptions\_UniquesOnly constant

### **OEMatchedPairIndexStatus**

This namespace contains constants representing status information returned from matched pair indexing.

#### **BinaryIOError**

This value indicates a serialization or deserialization issue during molecule fragmentation import or export.

#### **CopyMolError**

This value indicates that an internal error was encountered when attempting to copy the input structure for indexing manipulations.

#### **Deactivated**

This value indicates that an index loaded from serialization output encountered an internal loading failure and cannot be used as an active index.

#### **DuplicateRecordID**

This value indicates that the record id provided for the structure is already in use.

#### **DuplicateStructure**

This value indicates that the structure is already present in the index.

#### See also:

- · OEMatchedPairAnalyzerOptions. SetOptions
- · OEMatchedPairOptions\_UniquesOnly

#### **FragmentRangeFilter**

This value indicates that the structure was not added to the index as a result of exceeding the allowed range of the indexable fragment filter.

#### See also:

· OEMatchedPairAnalyzerOptions.SetIndexableFragmentRange

### **FragmentationLimitFilter**

This value indicates that the structure was not added to the index as a result of exceeding the number of allowed fragmentation bonds.

#### See also:

· OEMatchedPairAnalyzerOptions. SetFragmentationLimit

#### **HeavyAtomFilter**

This value indicates that the structure was not added to the index due to exceeding the heavy atom limit.

#### See also:

· OEMatchedPairAnalyzerOptions. SetMaxAtomFilter

#### **IncompatibleOptions**

This value indicates that an internal mismatch in fragmentation arguments and those for the target OEMatchedPair-Analyzer instance was identified. Contact support@eyesopen.com with details.

### **NoError**

This value indicates a successful indexing status.

#### **NoFragmentationBonds**

This value indicates the structure contains no fragmentation bonds.

#### **NoStructure**

This value indicates that the structure is empty, or contains no heavy atoms.

### **ProcessorError**

This value indicates that the internal processing engine has rejected the structure for unspecified reasons.

#### **ProcessorFilter**

This value indicates that the internal processing engine has rejected the structure based on the filter steps prior to indexing. One possible reason for the rejection is the presence of one or more unspecified atom types in the structure being indexed.

#### **Unspecified**

This value indicates an abnormal indexing status return of an unspecified nature.

#### **OEMatchedPairOptions**

This namespace contains constants representing various supported options to control a matched pair analysis.

#### **AllCuts**

This constant requests analysis of all fragmentation cuts from the processor-specific fragmentation strategy.

#### **ComboCuts**

This constant requests analysis of all single, double, triple combination fragmentation cuts from the processor-specific fragmentation strategy.

#### **Default**

This constant represents the default options setting for matched pair analysis which OEMatchedPairOptions\_AllCuts, OEMatchedPairOptions\_UniquesOnly, is OEMatchedPairOptions\_IndexHSites and OEMatchedPairOptions\_ExportHKeys.

#### **DefaultFragIndex**

This constant represents the default options setting for MCS fragment database indexing, which is OEMatchedPairOptions\_AllCuts and OEMatchedPairOptions\_IndexHSites.

#### **DoubleCuts**

This constant requests analysis of only double fragmentation cuts from the processor-specific fragmentation strategy.

#### **ExportCompression**

This constant affects the serialization of information from a OEMatchedPairAnalyzer instance. If enabled, singleton index nodes are not exported, thereby dramatically reducing the size of the serialized information. This option should only be used to export information from a static index since reading of this compressed index information and indexing of additional input structures miss valid matched molecular pairs.

### **ExportHKeys**

This constant affects the serialization of information from a OEMatchedPairAnalyzer instance. If enabled, extra index information that supports the OEMatchedPairOptions\_IndexHSites capability is serialized to the output file to increase index loading performance. If this information is suppressed, the serialized file size will be 10-20% smaller and this information will be regenerated as needed. If OEMatchedPairOptions IndexHSites is not enabled, this option has no effect on serialization or deserialization.

#### **IndexHSingleCuts**

This constant activates additional indexing activity in order to capture matched pairs that differ by hydrogen presence at one or more of the substitution sites for SingleCuts only.

#### **IndexHSites**

This constant activates additional indexing activity in order to capture matched pairs that differ by hydrogen presence at one or more of the substitution sites for all fragmentation cut types.

#### **SingleCuts**

This constant requests analysis of only single fragmentation cuts from the processor-specific fragmentation strategy.

#### **TripleCuts**

This constant requests analysis of only triple fragmentation cuts from the processor-specific fragmentation strategy.

#### **UniquesOnly**

This constant requests uniqueness checking using canonical SMILES of the input structures to avoid duplicated indexed fragments.

#### **ValidAlterOpts**

This constant is a bit mask of all the options that can be changed on an active OEMatchedPairAnalyzer instance.

#### **ValidFragIndexOpts**

This constant is a bit mask of all the valid read-only option values for an active OEMCSFragDatabase instance.

#### **ValidIndexOpts**

This constant is a bit mask of all the valid read-only option values for an active OEMatchedPairAnalyzer instance.

#### **ValidOptions**

This a bit mask of all the valid option values of constant  $is$ and  $i<sub>s</sub>$  $\mathbf{a}$ union OEMatchedPairOptions\_ValidAlterOpts and OEMatchedPairOptions\_ValidIndexOpts

#### **OEMatchedPairProcessor**

This namespace contains constants representing various supported processor strategies for a matched pair analysis.

### **Undefined**

This constant represents an undefined or illegal context state.

#### **Default**

This constant represents a request for the default processor type which is currently specified to be OEMatchedPairProcessor\_HussainRea

#### **HussainRea**

This constant represents a request for a [Hussain-2010] processor type.

#### **BemisMurcko**

This constant represents a request for a [Bemis-1996] processor type.

#### **Custom**

This constant identifies a custom type of processor engine that may be available in future versions.

#### **OEMatchedPairTransformExtractMode**

This namespace contains constants that control transform generation during retrieval from the matched pair index.

#### **Unspecified**

This value indicates an unspecified or null mode value.

### **Default**

This mode represents the default extraction mode of OEMatchedPairTransformExtractMode\_Forward and OEMatchedPairTransformExtractMode\_Backward.

#### **AddAttachmentPts**

This extraction mode requests that attachment point information be added to the returned transforms to indicate the number of neighbor atoms adjacent to the desired context atoms.

#### **AddMCSCorrespondence**

This extraction mode returns correspondence information for the matched pairs by annotating the maximum common substructure with atom mapping information to indicate the MCS core.

#### **Backward**

This mode requests that only backward direction transforms be returned where 'backward' indicates the direction of later indexed structures over earlier indexed structures.

#### **Forward**

This mode requests that only forward direction transforms be returned where 'forward' indicates the direction of earlier indexed structures over later indexed structures.

#### **Nolsotopes**

This mode suppresses isotopic information in the transformation to allow more general use of the transformation with mixed isotopic input structures.

#### **NoMatchedPairData**

This extraction mode suppress populating the delta data for the matched pairs in the returned transforms, for example if the transformation and the matched pair ids are all that is required.

#### **NoMatchedPairs**

This extraction mode suppress populating the transformations with matched pair id information, for example, if the transformation itself is the only information of interest.

#### **NoSMARTS**

This mode suppresses the addition of SMARTS qualifiers to the transformation which is present to ensure more accurate application of the transformation. If the transform is being used for purposes other than performing transformations, the suppression of SMARTS qualifiers may provide simplification for downstream use of the transformation information.

#### **Sorted**

Since the direction of the transformations returned is dependent on input order of the indexed structures, this mode attempts to perform a simple sorting of the right hand and left hand sides of the transformation to collapse forward and backward transformations to a more deterministic form.

#### **SubstLimitSkip**

This extraction mode option indicates that any indexed core structures that exceed the maximum substituent limit are to be entirely skipped during the extraction process. By default, any MMP cores with large numbers of substituents are truncated to the maximum value to avoid the combinatorics of generating huge numbers of matched molecular pair transformations.

#### See also:

OEMatchedPairTransformExtractOptions

#### **SuppressNodeSort**

This extraction mode option suppresses an internal sort which is used to return the largest MCS cores from the matched pairs. This is largely a debugging and analysis tool to allow examination of all matched pair cores.

#### **OERegionType**

This namespace contains constants representing various supported regions types for the OEGet BemisMurcko function.

#### See also:

[Bemis-1996]

#### **Ring**

This constant identifies a ring region from the perception.

#### **Linker**

This constant identifies linker regions from the perception.

#### **Framework**

This constant identifies the framework region from the perception.

#### Sidechain

This constant identifies sidechain regions from the perception.

### **AII**

This constant requests that all regions be returned from the perception

## **4.1.3 OEMedChem Functions**

#### OEApplyChEMBL18SolubilityTransforms

Warning: This is a deprecated API.

This version is based on older [ChEMBL18-2014] data and will be deprecated in a future version of OEMedChem TK, please use OEApplyChEMBL24SolubilityTransforms instead.

```
OESystem:: OEIterBase<OEChem:: OEMolBase> *
  OEApplyChEMBL18SolubilityTransforms(OEChem::OEMolBase &input, int context,
sunsigned int minMMPThreshold=5)
```

Given an input molecule, apply transformations derived from solubility data obtained from the [ChEMBL18-2014] database. The context argument controls the amount of chemistry information that should be included for the transformation reaction, see OEMatchedPairContext. This function supports only the OEMatchedPairContext Bond0 or OEMatchedPairContext Bond2 context values. The minMMPThreshold argument will only apply transformations that meet or exceed the specified number of matched pairs. Use a minMMPThreshold value of 0 to apply all transformations regardless of the number of matched pairs associated with them.

Note: This function does not perform any validation or filtering on the input molecule to be transformed. The caller is expected to perform validity and/or size checking to ensure sensible inputs are provided.

#### See also:

• OEApplyChEMBL24SolubilityTransforms function

#### OEApplyChEMBL24SolubilityTransforms

```
OESystem:: OEIterBase<OEChem:: OEMolBase> *
  OEApplyChEMBL24SolubilityTransforms(OEChem::OEMolBase &input, int context,
→unsigned int minMMPThreshold=5)
```

Given an input molecule, apply transformations derived from solubility data obtained from the [ChEMBL24-20181 database. The context argument controls the amount of chemistry information that should be included for the transformation reaction, see OEMatchedPairContext. This function supports only the OEMatchedPairContext\_Bond0 or OEMatchedPairContext\_Bond2 context values. The minMMPThreshold argument will only apply transformations that meet or exceed the specified number of matched pairs. Use a minMMPThreshold value of 0 to apply all transformations regardless of the number of matched pairs associated with them.

Note: This function does not perform any validation or filtering on the input molecule to be transformed. The caller is expected to perform validity and/or size checking to ensure sensible inputs are provided.

In the examples below, the input structures are transformed by the ChEMBL solubility transforms and exported to a file format that supports SD data. Each transformed structure will contain information about the solubility transform (as SMIRKS) that generated it, and the matched pair information associated with each transform (ChEMBL identifiers and solubility data). The added annotation data will contain the data fields, OEMMP normalized value (uM), OEMMP\_published\_value, OEMMP\_examples (SMILES), and OEMMP\_transform (SMILES) for subsequent analysis.

```
# number of bonds of chemistry context at site of change
    # for the applied transforms
   totalmols = 0xformctxt = oemedchem.OEMatchedPairContext_Bond2
   for molidx, mol in enumerate (ifs. GetOEGraphMols (), start=1) :
        # consider only the largest input fragment
        oechem.OEDeleteEverythingExceptTheFirstLargestComponent (mol)
        smolcnt = 0# only consider solubility transforms having at least 5 matched pairs
        for solMol in oemedchem. OEApplyChEMBL24SolubilityTransforms(mol, xformctxt,
\leftrightarrow 5):
            # compute net change in solubility from MMP data
            delrasol = []if oechem. OEHasSDData(solMol, "OEMMP_normalized_value (uM)"):
                for sditem in oechem. OEGetSDData (solMol,
                                                    "OEMMP_normalized_value (uM)").split(
\leftrightarrow'\n'):
                     # fromIndex, toIndex, fromValue, toValue
                    sdvalues = sditem.split(',')
                    if not sdvalues [2] or not sdvalues [3]:
                         continue
                     deltasol.append(float(sdvalues[3])-float(sdvalues[2]))
            if not len(deltasol):
                continue
            avgsol = deltasol[0]if len(deltasol) > 1:
                avgsol = average(deltasol)# reject examples with net decrease in solubility
            if avgsol < 0.0:
                continue
            sdev = stddev(deltasol)
            # annotate with average, stddev, num
            oechem. OEAddSDData (solMol,
                                 "OEMMP_average_delta_normalized_value",
                                "\{0:.1F\}, \{1:.2F\}, \{2\}". format (avgsol, sdev,
\rightarrowlen(deltasol)))
            # export solubility transformed molecule with SDData annotations
            if oechem. OEWriteMolecule (ofs, solMol) == oechem. OEWriteMolReturnCode_
\rightarrowSuccess:
                smolcnt += 1
```

```
oechem. OEThrow. Info("\{0\}: Exported molecule count, \{1\}". format (molidx,..
\rightarrowsmolcnt))
        totalmols += smolcnt
```

#### **OECalculateComboBelief**

float OECalculateComboBelief (float tanimotoCombo)

Note: See documentation for this function in the context of other belief function api points at OECalculateETComboBelief

#### **OECalculateETComboBelief**

```
float OECalculateComboBelief (float tanimotoCombo)
float OECalculateETComboBelief (float etCombo)
```

This pair of functions is based on [Muchmore-2008]. In that paper, the scores assessed for ROCS were the historic 'color score', in which the color was not normalized by self score, resulting in bias toward highly colored molecules. All recent versions of OEShape and ROCS use Tanimoto combo for ranking which is the sum of a shape Tanimoto and a color Tanimoto. The belief curve in OECalculateComboBelief is based on fitting of the data described in [Muchmore-2008] to ROCS Tanimoto combo scores [Brown-Muchmore-2008]. EON results are ranked on the ET combo score, which is a sum of a shape Tanimoto and an electrostatic Tanimoto. The belief curve in OECalculateETComboBelief is based on fitting of the data described in [Muchmore-2008] to ET combo scores [Brown-Muchmore-2008].

**Warning:** For use with other OpenEye toolkits, the full scores with range  $(0,2)$  should be passed into these functions.

#### **OEConfigureMatchedPairIndexOptions**

```
bool OEConfigureMatchedPairIndexOptions (OESystem:: OEInterface& itf,
                                        unsigned int config =→OEMatchedPairIndexSetup::All)
```

Configures the given interface to add matched pair indexing parameters.

*itf* The interface being configured.

config The option that specifies which parameters will be added to the interface This value has to be from the OEMatchedPairIndexSetup namespace.

- OEInterface class in the OEChem TK manual
- · OEMatchedPairIndexSetup namespace
- · OESetupMatchedPairIndexOptionsfunction

#### **OEConfigureMCSFragDatabaseOptions**

```
bool OEConfigureMCSFragDatabaseOptions (OESystem:: OEInterface &itf,
                                       unsigned int config =→OEMCSFragDatabaseSetup::All)
```

Configures the given interface to add MCS fragment database indexing parameters.

itf The interface being configured.

config The option that specifies which parameters will be added to the interface This value has to be from the OEMCSFragDatabaseSetup namespace.

#### See also:

- OEInterface class in the **OEChem TK** manual
- · OEMCSFragDatabaseSetup namespace
- OESetupMCSFragDatabaseOptionsfunction

#### **OECreateIDString**

std::string OECreateIDString(const OEChem::OEMolBase &mol)

Note: See documentation for this function in the context of other graph-edit similarity function api points at OECreateIDStrings

#### **OECreateIDStrings**

```
std::string OECreateIDString (const OEChem::OEMolBase &mol)
OESystem::OEIterBase<const std::string> * OECreateIDStrings(const OEChem::OEMolBase &
\simmol)
```

This pair of functions exposes the graph-edit similarity used in clustering BROOD hitlists. Because this is a naturally O(N^2), the API is designed for efficiency using an asymmetric approach. For any 'accepted' molecule, the OECreateIDStrings function is used to generate a set of all the canonical SMILES of fragments which would be considered similar to the input molecule (this can be stored for fast lookup). If one wants to determine if a new molecule is similar to the original molecule,  $OECreateIDString$  is called, and the single string generated is compared to all the strings previously created. If the new string is an exact match to any of the multiple strings created from the prior molecule, then the two molecules are deemed similar.

#### **OECreateMMPIndexFile**

```
OECreateMMPIndexStatus OECreateMMPIndexFile(const std::string& mmpdbfname,
                                            const std:: string& molfname,
                                            const OECreateMMPIndexOptions& opts);
```

This function reads the input structures from the provided molfname filename and generates an OEMatchedPairAnalyzer index from those structures which is saved to the provided mmpdbfname output file. Options for indexing are provided in the OECreateMMPIndexOptions argument.

In general, the provided input structures should have been thoroughly normalized, deduplicated or have data merged onto unique input structures for duplicate structures. There are no options for structure normalization or cleanup activities as part of this automatic indexing.

#### See also:

- OECreateMMPIndexStatus
- OECreateMMPIndexOptions

#### **OEDetermineConnectiveComplexity**

float OEDetermineConnectiveComplexity (const OEChem:: OEMolBase & mol)

Note: See documentation for this function in the context of other complexity api points at OEDetermineMolecularComplexity

#### **OEDetermineElementalComplexity**

float OEDetermineElementalComplexity(const OEChem:: OEMolBase &mol)

Note: See documentation for this function in the context of other complexity api points at OEDetermineMolecularComplexity

#### **OEDetermineMolecularComplexity**

float OEDetermineMolecularComplexity(const OEChem:: OEMolBase &mol)

```
float OEDetermineConnectiveComplexity (const OEChem:: OEMolBase &mol)
float OEDetermineElementalComplexity(const OEChem::OEMolBase &mol)
float OEDetermineSymmetryComplexity(const OEChem::OEMolBase &mol)
```

Note: The molecule arguments are const, so the OEPerceiveChiral perception activity must be performed prior to calling these functions.

From [Bertz-1981]. Includes connectivity and elemental complexity. Though aromaticity is not addressed in the brief literature note, aromatic bonds are not counted as double bonds for the entropy calculation in this implementation. The three additional api points return the three individual terms that make up the Molecular Complexity as defined by Bertz.

- · OEDetermineRingComplexity
- · OENormalMolecularComplexity

#### **OEDetermineRingComplexity**

float OEDetermineRingComplexity(const OEChem::OEMolBase &mol)

Note: The molecule argument is const, so this function requires that the OEFindRingAtomsAndBonds perception activity has been performed prior to calling this function.

This is a non-SSSR adaptation of the ring complexity algorithm of [Gasteiger-1979]. The values of this complexity are generally somewhat lower, but are well-correlated and follow the spirit of the SSSR method.

#### See also:

· OEDetermineMolecularComplexity

#### **OEDetermineStereoComplexity**

float OEDetermineStereoComplexity (const OEChem:: OEMolBase &mol)

Note: The molecule argument is const, so the OEPerceiveChiral perception activity must be performed prior to calling this function.

In [Boda-2007] a term was added for tetrahedral stereo complexity to the [Bertz-1981] approach. The function here reproduces that function with the addition of chiral bond stereo to the tetrahedral atom stereo.

#### See also:

· OENormalStereoComplexity

#### **OEDetermineSymmetryComplexity**

float OEDetermineSymmetryComplexity(const OEChem::OEMolBase &mol)

Note: See documentation for this function in the context of other complexity api points at OEDetermineMolecularComplexity

#### **OEGetBemisMurcko**

```
OESystem:: OEIterBase<OEChem:: OEAtomBondSet> *
   OEGetBemisMurcko (const OEChem:: OEMolBase &mol,
                    const OEBemisMurckoOptions& options=OEBemisMurckoOptions());
```

Warning: The following function is deprecated. Please use the more generic function above.

```
OESystem:: OEIterBase<OEChem:: OEAtomBondSet> *
   OEGetBemisMurcko (OEChem:: OEMolBase & mol, unsigned perceivetype);
```

The OEGet Bemi sMurcko function partitions the given molecule into ring, linker and side chain fragments as defined in [Bemis-1996]. It returns an iterator over OEAtomBondSet objects where each OEAtomBondSet container stores the atoms and the bonds of an identified region. Each OEAtomBondSet returned is tagged with a role that identifies which group the set identifies.

The OEBemisMurckoOptions class can be used to specify both the OERegionType and also add additional functional groups to fragments. The *perceiveType* parameter only allows modification of the  $OERegionType$  of the fragments returned.

#### See also:

- OEAtomBondSet and OEMolBase classes in the OEChem TK manual
- OERole in the *OEChem TK* manual
- OEBemisMurckoOptions
- OERegionType
- · OEGetRingLinkerSideChainFragments
- Molecule Fragmentation chapter

#### **OEGetFuncGroupFragments**

```
OESystem:: OEIterBase<OEChem:: OEAtomBondSet> *
  OEGetFuncGroupFragments (const OEChem:: OEMolBase & mol)
```

The OEGetFuncGroupFragments function partitions the given molecule into functional groups and returns an iterator over OEAtomBondSet objects. Each OEAtomBondSet container stores the atoms and the bonds of an identified fragment. See example in Figure: Example of fragments returned by the OEGetFuncGroupFragments function where each fragment returned by the OEGetFuncGroupFragments function is highlighted with a different color.

The OEGetFuncGroupFragments function uses the following heuristics to fragment a molecule:

- $\bullet$  rings are left intact *i.e.* considered as a unit
- exo-ring double bonds are not cleaved from adjacent rings
- hetero atoms next to each other are kept together
- sp and sp2 atoms next to each other are kept together
- in order to avoid generating one atom fragments isolated atoms are attached to the smallest neighbor fragment

Note: The molecule argument is const, so this function requires that the OEFindRingAtomsAndBonds perception activity has been performed prior to calling this function.

- OEAtomBondSet and OEMolBase classes in the OEChem TK manual
- Molecule Fragmentation chapter

![](_page_140_Figure_1.jpeg)

**Generated by OEDepict TK** 

### Fig. 1: Example of fragments returned by the OEGetFuncGroupFragments function

#### **OEGetMatchedMolecularPairs**

| OESystem::OEIterBase<OEMedChem::OEMatchedPair> *                             |
|------------------------------------------------------------------------------|
| OEGetMatchedMolecularPairs(const OEMedChem::OEMatchedPairAnalyzer &mmpindex, |
| unsigned int recID,                                                          |
| const OEMedChem::OEMatchedPairTransformExtractOptions &extractOpts)          |
|                                                                              |
| OESystem::OEIterBase<OEMedChem::OEMatchedPair> *                             |
| OEGetMatchedMolecularPairs(const OEMedChem::OEMatchedPairAnalyzer &mmpindex, |
| const OEChem::OEMolBase &probe,                                              |
| const OEChem::OEAtomBondSet &probeABSet,                                     |
| const OEMedChem::OEMatchedPairTransformExtractOptions &extractOpts)          |

The first function returns the matched pairs associated with a specific molecule ID in the OEMatchedPairAnalyzer index.

The second overloaded function returns matched molecular pairs related to changes at specific substitution point(s) on the provided probe structure. Additionally, any \*atoms (atomic number 0) on the probe structure can be used to indicate the site(s) that are open valences and which can be arbitrarily substituted.

- OEMatchedPairGetTransformsfunction
- OEMatchedPairAnalyzer class
- OEMatchedPairTransformExtractOptions class
- OEAtomBondSet class

#### **OEGetMatchedPairAnalyzerFileType**

unsigned int OEGetMatchedPairAnalyzerFileType (const char \*ext)

Returns a symbolic constant from the *OEMatchedPairAnalyzerFileType* namespace for the file extension 'ext'.

#### **OEGetRegionType**

unsigned int OEGetRegionType (const std:: string &regionName)

Given the region name, return the OERegionType value.

#### See also:

• OERegionType

#### **OEGetRegionTypeName**

const char\* OEGetRegionTypeName (unsigned int regionType)

Given the  $OERegionType$  value, return a string representation of the region name.

#### See also:

• OERegionType

#### **OEGetRingChainFragments**

```
OESystem:: OEIterBase<OEChem:: OEAtomBondSet> *
 OEGetRingChainFragments (const OEChem:: OEMolBase &mol)
```

The OEGetRingChainFragments function partitions the given molecule into ring and chain fragments and returns an iterator over OEAtomBondSet objects. Each OEAtomBondSet container stores the atoms and the bonds of an identified fragment. See example in Figure: Example of fragments returned by the OEGetRingChainFragments function where each fragment returned by the OEGetRingChainFragments function is highlighted with a different color.

The perceived regions are based upon the heavy atoms in the molecule. If the molecule contains explicit hydrogen atoms, those explicit hydrogens will be returned in the same perception set(s) as their alpha heavy atom neighbor. If the perception set(s) returned are used to subset or fragment the molecule, a mixture of implicit and explicit hydrogens may result, so care should be taken to normalize the structure for subsequent use.

Note: The molecule argument is const, so this function requires that the OEFindRingAtomsAndBonds perception activity has been performed prior to calling this function.

- OEAtomBondSet and OEMolBase classes in the OEChem TK manual
- Molecule Fragmentation chapter

![](_page_142_Picture_1.jpeg)

**Generated by OEDepict TK** 

### Fig. 2: Example of fragments returned by the OEGetRingChainFragments function

#### **OEGetRingLinkerSideChainFragments**

```
OESystem::OEIterBase<OEChem::OEAtomBondSet>* OEGetRingLinkerSideChainFragments(
 const OEChem:: OEMolBase& mol,
 const OEBemisMurckoOptions& options = OEBemisMurckoOptions());
```

Warning: The following function is deprecated. Please use the more generic function above.

```
OESystem::OEIterBase<OEChem::OEAtomBondSet>* OEGetRingLinkerSideChainFragments(
 const OEChem:: OEMolBase& mol,
 unsigned perceiveType)
```

The OEGetRingLinkerSideChainFragments function partitions the given molecule into ring, linker and side chain fragments as defined in [Bemis-1996].

The OEBemisMurckoOptions class can be used to specify both the OEReqionType and also add additional functional groups to fragments. The *perceiveType* parameter only allows modification of the  $OERegionType$  of the fragments returned.

It returns an iterator over OEAtomBondSet objects where each OEAtomBondSet container stores the atoms and the bonds of an identified fragment. See example in Figure: Example of fragments returned by the OEGetRingLinker-SideChainFragments function where each fragment returned by the OEGetRingLinkerSideChainFragments function is highlighted with a different color.

The perceived regions are based upon the heavy atoms in the molecule. If the molecule contains explicit hydrogen atoms, those explicit hydrogens will be returned in the same perception set(s) as their alpha heavy atom neighbor. If the perception set(s) returned are used to subset or fragment the molecule, a mixture of implicit and explicit hydrogens may result, so care should be taken to normalize the structure for subsequent use.

Definitions from [Bemis-1996]:

ring systems. Cycles within the graph representation of molecules and cycles sharing an edge (a connection between two atoms or a bond).

linker atoms Atoms that are on the direct path connecting two ring systems are defined as linker atoms.

side chain atoms Any nonring, nonlinker atoms are defined as side chain atoms.

Note: The molecule argument is const, so this function requires that the OEFindRingAtomsAndBonds perception activity has been performed prior to calling this function.

![](_page_143_Picture_5.jpeg)

**Generated by OEDepict TK** 

#### Fig. 3: Example of fragments returned by the OEGetRingLinkerSideChainFragments function

#### See also:

- OEAtomBondSet and OEMolBase classes in the OEChem TK manual
- Molecule Fragmentation chapter

#### **OEGetRingValue**

#### float OEGetRingValue (const OEChem:: OEMolBase &mol)

This is a function that assigns a value to a molecule or fragment based on the number and type of ring systems it contains. Ring systems that are favored by small-molecule medicinal chemistry receive higher scores. No preference is given between aromatic and aliphatic rings. Ring fusions are favored over spiro ring systems and common ring sizes (5,6) are favored over unusual ring sizes. This value is not recommended for filtering or cutoffs, yet can be useful for ordering compounds from a set of potential candidates.

#### **OEIsMatchedPairAnalyzerFileType**

```
bool OEIsMatchedPairAnalyzerFileType (unsigned int type)
bool OEIsMatchedPairAnalyzerFileType(const std::string &filename)
```

This function returns a boolean indicating whether the provided OEMatchedPairAnalyzerFileType value or filename is a serialized index type, i.e., has a file extension of .mmpidx.

#### **OEIsMCSFragDatabaseFileType**

```
bool OEIsMCSFragDatabaseFileType (unsigned int type)
bool OEIsMCSFragDatabaseFileType (const std::string &filename)
```

This function returns a boolean indicating whether the provided OEMatchedPairAnalyzerFileType value or filename is a serialized fragment index type, i.e., has a file extension of . mcsfraq.

#### **OEIsReadableMatchedPairAnalyzer**

**Warning:** The following functions are deprecated. generic Please use the more OEIsMatchedPairAnalyzerFileType to test for the appropriate file extension for a serialized index.

```
bool OEIsReadableMatchedPairAnalyzer (unsigned int type)
bool OEIsReadableMatchedPairAnalyzer (const std::string &filename)
```

This function returns a boolean indicating whether the provided OEMatchedPairAnalyzerFileType value or filename is a readable serialized index.

Warning: This function is deprecated as of 2017. Feb and will be removed in a future version of OEMedChem TK, please use OEIsMatchedPairAnalyzerFileType instead.

#### **OEIsWriteableMatchedPairAnalyzer**

The following functions are deprecated. Warning: Please use the more generic OEIsMatchedPairAnalyzerFileType to test for the appropriate file extension for a serialized index.

```
bool OEIsWriteableMatchedPairAnalyzer (unsigned int type)
bool OEIsWriteableMatchedPairAnalyzer(const std::string &filename)
```

This function returns a boolean indicating whether the provided OEMatchedPairAnalyzerFileType value or filename is a writeable serialized index.

Warning: This function is deprecated as of 2017. Feb and will be removed in a future version of OEMedChem TK, please use OEIsMatchedPairAnalyzerFileType instead.

#### **OEMatchedPairApplyTransforms**

```
OESystem:: OEIterBase<OEChem:: OEMolBase> *
OEMatchedPairApplyTransforms (const OEChem:: OEMolBase &mol, OEMatchedPairAnalyzer &mmp,
                             int chemcontext=OEMatchedPairContext::Default,
                             unsigned int minMMPThreshold=0)
```

The OEMatchedPairApplyTransforms function will take the matched pair analysis provided by the OE-MatchedPairAnalyzer engine to generate a set of transformations to apply to the input molecule. The output molecule(s) will be annotated with SD data that identifies the original pair of molecules from the matched pair indexing, any data associated with those original molecules, and the transformation that resulted in the output molecule. The context argument controls the amount of chemistry information that should be used in constructing the transformation reaction, see OEMatchedPairContext. The minMMPThreshold argument will only apply transformations that meet or exceed the specified number of matched pairs. A minMMPThreshold value of 0 will apply transformations regardless of the number of matched pairs associated with them.

#### **OEMatchedPairContextName**

const char\* OEMatchedPairContextName (int context)

Given a OEMatchedPairContext value, return a string representation of the context.

#### **OEMatchedPairContextType**

int OEMatchedPairContextType (const std:: string &scontext)

Given the context name, return the OEMatchedPairContext value.

#### **OEMatchedPairGetTransforms**

```
OESystem:: OEIterBase<OEMatchedPairTransform> *
OEMatchedPairGetTransforms (const OEMatchedPairAnalyzer &mmpindex,
                            int context,
                            unsigned int.
\rightarrowextractMode=OEMatchedPairTransformExtractMode::Default)
OESystem::OEIterBase<OEMatchedPairTransform> *
OEMatchedPairGetTransforms (const OEMatchedPairAnalyzer &mmpindex,
                            const OEChem:: OEMolBase &probemol,
                            int context,
                            unsigned int.
-extractMode=OEMatchedPairTransformExtractMode::Default)
OESystem:: OEIterBase<OEMatchedPairTransform> *
OEMatchedPairGetTransforms (const OEMatchedPairAnalyzer &mmpindex,
                            const OEMatchedPairTransformExtractOptions &extractOpts)
OESystem:: OEIterBase<OEMatchedPairTransform> *
OEMatchedPairGetTransforms (const OEMatchedPairAnalyzer & mmpindex,
                           const OEChem:: OEMolBase &probemol,
                            const OEMatchedPairTransformExtractOptions &extractOpts)
```

```
OESystem:: OEIterBase<OEMatchedPairTransform> *
OEMatchedPairGetTransforms (const OEMatchedPairAnalyzer &mmpindex,
                           const OEChem:: OEMolBase &probemol,
                           const OEMatchedPairAnalyzerOptions &probemolFragOpts,
                           const OEMatchedPairTransformExtractOptions &extractOpts)
OESystem:: OEIterBase<OEMatchedPairTransform> *
OEMatchedPairGetTransforms (const OEMatchedPairAnalyzer &mmpindex,
                           const OEChem:: OEMolBase &probemol,
                           const OEChem:: OEAtomBondSet &probesubst,
                           const OEMatchedPairTransformExtractOptions &
→extractOpts=OEMatchedPairTransformExtractOptions())
OESystem:: OEIterBase<OEMatchedPairTransform> *
OEMatchedPairGetTransforms (const OEMatchedPairAnalyzer &mmpindex,
                           const OEChem:: OEMolBase &probemol,
                           const char *probesubstDataField,
                           const OEMatchedPairTransformExtractOptions &
→extractOpts=OEMatchedPairTransformExtractOptions())
```

Given an analyzer containing indexed structures, retrieves the transformations derived from the discovered matched pair information.

Overloaded functions support the ability to pass in an arbitrary structure and return related matched molecular pair transformations that share any of the identified substituents from the probe structure. The probe molecule is not added to the index, it is only used to locate related transformations. The probe molecule is subject to the same filtering constraints as the structures present in the index. An additional overloaded function signature is provided that allows passing different fragmentation filtering constraints for the probe structure than the indexed structures to allow a more generalized extraction of transformations.

The final two overloaded functions support the ability to pass in an arbitrary structure and return related matched molecular pair transformations at one or more identified attachment site(s) on the probe structure.

The context argument controls the amount of chemistry context to include in the returned transforms. The extract mode argument provides some control over the transformation string returned. The extraction options object allows the most control over the content of the extracted transformations.

- · OEGetMatchedMolecularPairs function
- OEMatchedPairContext
- OEMatchedPairTransformExtractMode
- OEMatchedPairTransformExtractOptions
- OEMatchedPairAnalyzer
- OEMatchedPairTransform
- $\bullet$  OEMatchedPair

#### **OEMatchedPairIndexStatusName**

const char\* OEMatchedPairIndexStatusName(int status)

Given a OEMatchedPairIndexStatus value, return a string representation of the status.

#### OEMatchedPairIndexStatusType

int OEMatchedPairIndexStatusType(const std::string &scontext)

Given a status name, return the OEMatchedPairIndexStatus value.

#### **OEMatchedPairOptionsName**

const char\* OEMatchedPairOptionsName (unsigned int option)

Given a OEMatchedPairOptions value, return a string representation of the option.

#### **OEMatchedPairOptionsType**

unsigned int OEMatchedPairOptionsType (const std::string &sOption)

Given the option name, return the OEMatchedPairOptions type.

#### **OEMatchedPairProcessorName**

const char\* OEMatchedPairProcessorName (unsigned int type)

Given a OEMatchedPairProcessor type, return a string representation of the processor type.

#### **OEMatchedPairProcessorType**

unsigned int OEMatchedPairProcessorType (const std::string &sname)

Given the processor name, return the OEMatchedPairProcessor type.

#### **OEMCSFragDatabaseCoreQuery**

```
bool OEMCSFragDatabaseCoreQuery(const std::string &MCScoreSMI,
                                      std::string &MCScoreSMARTS)
```

This function can be used to convert the MCS SMILES core string into a more restrictive SMARTS query for use in highlighting or mapping activities that use the MCS core and the query or target structures.

- OEMCSMolSimScore class
- OEMCSFragDatabase class

- · OEMCSFragDatabase. GetScores method
- · OEMCSFragDatabase. GetSortedScores method

#### **OEMedChemGetArch**

const char \*OEMedChemGetArch()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify the hardware architecture. The format of these strings may change over time.

#### **OEMedChemGetLicensee**

```
std::string OEMedChemGetLicensee()
bool OEMedChemGetLicensee (std::string &licensee)
```

Returns the licensee name from the license file.

#### **OEMedChemGetPlatform**

const char \*OEMedChemGetPlatform()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify a platform. The format of these strings may change over time, and future distributions may contain different values even when using the same operating system, compiler and processor. For example, on a  $\times 86$  64 Red Hat Enterprise Linux box this would return  $redhat-RHEL5-q++4.1-x64.$ 

#### **OEMedChemGetRelease**

```
const char *OEMedChemGetRelease()
```

Returns the release name of the *OEMedChem* library being used. This returns a value similar to  $0.10.0$  for production versions of the library, and  $0.10.0$  debug for the checking version of the library.

#### **OEMedChemGetSite**

```
std::string OEMedChemGetSite()
bool OEMedChemGetSite(std::string &site)
```

Returns the physical site location of the licensee as registered in the license file.

#### **OEMedChemGetVersion**

unsigned int OEMedChemGetVersion()

Returns the version number of the library being used. This is an unsigned integer value indicating the date on which the library was built, for example 20141001, for the 1st of October 2014. This value should be used when reporting problems, and unlike the release string, may be used in comparisons if needed.

#### **OEMedChemIsLicensed**

```
bool OEMedChemIsLicensed (const char *feature=0.
                                    unsigned int *expdate=0)
```

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any OEMedChem TK functionality.

The 'feature' argument can be used to check for a valid license to **OEMedChem TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current OEMedChem TK license.

#### See also:

· OEChemIsLicensed function

#### **OEMoleculeToCores**

```
OESystem::OEIterBase<const std::string>* OEMoleculeToCores(const OEChem::OEMolBase &
\rightarrowmol,
                                                                  const
→OEMCSFragDatabaseOptions &opts,
                                                                  bool
\rightarrowpermuteFragments=true);
```

Given a molecule, return the fragmentation cores using the provided fragmentation options. If the permuteFragments argument is true, all combinations of the generated fragmentation cores are generated, otherwise a unique set of multi-fragment cores is returned representing all combinations of bond fragmentations between the min and max cut limits.

Shown below is a version that uses the free function and custom options setup from command line arguments:

```
# set the MCS fragment database options from the command-line arguments
fragopts = oemedchem.OEMCSFragDatabaseOptions()
if not oemedchem. OEConfigureMCSFragDatabaseOptions(itf):
    oechem. OEThrow. Fatal ("Error configuring options")
if not oemedchem. OESetupMCSFragDatabaseOptions (fragopts, itf):
    oechem. OEThrow. Fatal ("Error setting options")
# use the custom options to fragment an arbitrary input molecule
print ('MoleculeToCores using command-line options:')
sortedcores = sorted([c for c in oemedchem.OEMoleculeToCores(mol, fragopts)])
for corenum, core in enumerate (sortedcores) :
    print('}): })'. format (corenum, core))
```

See also:

• OEMCSFragDatabase class

• OEMCSFragDatabaseOptions class

#### **OENormalMolecularComplexity**

```
float OENormalMolecularComplexity (const OEChem:: OEMolBase &mol)
```

**Note:** The molecule argument is const, so the OEPerceiveChiral perception activity must be performed prior to calling this function.

This function is a convenience that scales the value from OEDetermineMolecularComplexity to [0-1] assuming the underlying complexity is [0-1000] which is the case from most small molecules.

#### **OENormalStereoComplexity**

float OENormalStereoComplexity (const OEChem:: OEMolBase & mol)

Note: The molecule argument is const, so the OEPerceiveChiral perception activity must be performed prior to calling this function.

This function is a convenience that scales the value from OEDetermineStereoComplexity to a range of approximately [0-1] assuming a non-normalized complexity range of [0-4.3] which corresponds to between 0 and 20 stereo centers.

#### **OEReadMatchedPairAnalyzer**

```
bool OEReadMatchedPairAnalyzer (const std::string &fname, OEMatchedPairAnalyzer &
\rightarrowmmpindex,
                                    bool enableMerge = false, bool regenHMemberKeys =.
\leftrightarrowfalse)
bool OEReadMatchedPairAnalyzer (OEPlatform::oeistream &ifs, OEMatchedPairAnalyzer &
\rightarrowmmpindex,
                                    bool enableMerge = false, bool regenHMemberKeys =
\leftrightarrowfalse)
```

This function reads the serialized contents of a matched pair index and populates the OEMatchedPairAnalyzer instance as below. An enableMerge argument of false is used to indicate that the OEMatchedPairAnalyzer instance should be cleared before the read, or  $true$  to indicate that the read index information should add (and update) existing data. If the regenHMemberKeys argument is true and the index includes extra H-member indexing information, the serialized H-member information will be ignored and regenerated during the read.

```
mmp = oemedchem. OEMatchedPairAnalyzer()
if not oemedchem. OEIsMatchedPairAnalyzerFileType (mmpimport) :
    oechem. OEThrow. Fatal ('Not a valid matched pair index input file, '+mmpimport)
elif not oemedchem. OEReadMatchedPairAnalyzer (mmpimport, mmp) :
    oechem. OEThrow. Fatal ("Index deserialization failed")
else:oechem.OEThrow.Info("Index deserialization complete")
```

- · OEIsReadableMatchedPairAnalyzer
- · OEWriteMatchedPairAnalyzer

#### **OEReadMCSFragDatabase**

```
bool OEReadMCSFraqDatabase (const std::string &fname,
                           OEMCSFragDatabase & mcsfragdb,
                           bool enableMerge = false)
bool OEReadMCSFragDatabase (OEPlatform::oeistream &ifs,
                           OEMCSFragDatabase & mcsfragdb,
                           bool enableMerge = false)
```

This function reads the serialized contents of an MCS fragment index and populates the OEMCSFragDatabase instance. An enableMerge argument of false is used to indicate that the OEMCSFragDatabase instance should be cleared before the read, or true to indicate that the read index information should add (and update) existing data.

#### See also:

- · OEIsMCSFragDatabaseFileType
- · OEWriteMCSFragDatabase

#### **OEReadMMPIndexMolecules**

```
int OEReadMMPIndexMolecules (OEPlatform::oeistream &ifs, OEMatchedPairAnalyzer &
→mmpindex, bool regenHKeys=false)
int OEReadMMPIndexMolecules (std::string &fragbytes, OEMatchedPairAnalyzer &mmpindex,.,
\rightarrowbool regenHKeys=false)
```

This function deserializes Matched Pair fragmentation information from the passed string or oeistream and adds the information to the OEMatchedPairAnalyzer provided.

The goal of this function is to stream the precomputed fragmentation information directly into the Matched Molecular Pair index with maximum efficiency.

#### See also:

• OEWriteMMPIndexMolecules

#### **OESetupMatchedPairIndexOptions**

```
bool OESetupMatchedPairIndexOptions (OEMatchedPairAnalyzerOptions &opts,
                                     const OESystem:: OEInterface& itf)
```

Initializes an OEMatchedPairAnalyzerOptions object from the parameters of a given interface.

- OEMatchedPairAnalyzerOptions class
- · OEConfigureMatchedPairIndexOptions function

#### **OESetupMCSFragDatabaseOptions**

```
bool OESetupMCSFragDatabaseOptions (OEMCSFragDatabaseOptions &opts,
                                    const OESystem:: OEInterface& itf)
```

Initializes an OEMCSFragDatabaseOptions object from the parameters of a given interface.

#### See also:

- OEMCSFragDatabaseOptions class
- OEConfigureMCSFragDatabaseOptionsfunction

#### **OETotalMolecularComplexity**

float OETotalMolecularComplexity (const OEChem:: OEMolBase &mol)

Note: The molecule argument is const, so the OEPerceiveChiral perception activity must be performed prior to calling this function.

This is the final function to use for assessing molecular complexity. OETotalMolecularComplexity OENormalMolecularComplexity + OENormalStereoComplexity.  $In$ turn. OENormalMolecularComplexity  $\equiv$ OEDetermineConnectiveComplexity  $+$ OEDetermineElementalComplexity. Ring complexity is not included because it did not contribute significantly to reproduction of chemists' notion of synthetic accessibility. Ring complexity is available in OEDetermineRingComplexity.

#### See also:

- · OEDetermineConnectiveComplexity
- · OEDetermineElementalComplexity
- · OEDetermineMolecularComplexity
- · OEDetermineRingComplexity
- OEDetermineSymmetryComplexity
- · OENormalMolecularComplexity
- · OENormalStereoComplexity

#### **OEWriteMatchedPairAnalyzer**

```
bool OEWriteMatchedPairAnalyzer(const std::string &fname, OEMatchedPairAnalyzer &
\rightarrowmmpindex)
bool OEWriteMatchedPairAnalyzer (OEPlatform::oeostream &ofs, OEMatchedPairAnalyzer &
\rightarrowmmpindex)
```

This function serializes the state of the *OEMatchedPairAnalyzer* instance argument to a file or stream as below:

```
mmp = oemedchem. 0EMatched PairAnalyizer()for recindex, mol in enumerate (ims. GetOEGraphMols()):
    status = mmp.AddMol(mol, recindex)
    if status != recindex:
```

```
oechem.OEThrow.Warning(
            "\{0\}: molecule indexing error, status=\{1\}"
            .format(recindex, oemedchem.OEMatchedPairIndexStatusName(status)))
print ("Index complete, matched pairs = \{0\}".format (mmp.NumMatchedPairs()))
# check for output filename with .mmpidx extension
mmpexport = itf.GetString("-output")
if not oemedchem. OEIsMatchedPairAnalyzerFileType (mmpexport) :
    oechem.OEThrow.Info('Not a valid matched pair index output file, '+mmpexport)
elif not oemedchem. OEWriteMatchedPairAnalyzer(mmpexport, mmp):
    oechem. OEThrow. Fatal ("Index serialization failed")
else:oechem. OEThrow. Info ("Index serialization complete")
```

If the matched pair index information being exported is complete in the sense that additional structures are not intended to be added to the index upon a subsequent descrialization, significant savings in output file size is possible by suppressing the export of singleton nodes - those index nodes which do not contain any matched pairs. Conversely, if the exported index must be able to support adding additional structures to the index after desertalization, export compression should be avoided, otherwise significant matched pairs may be missed. To enable export compression (by default, *disabled*), see the following:

```
# create analyzer class with defaults
# - compression option disabled by default
mmpAnalyzer = oemedchem.OEMatchedPairAnalyzer()
# for serialization, enable export compression to
# remove singleton index nodes by modifying analyzer
mmpAnalyzer.ModifyOptions(oemedchem.OEMatchedPairOptions_ExportCompression, 0)
```

```
# create options class with defaults
  - compression option disabled by default
mmpOpts = oemedchem. 0EMatchedPairAnalyzerOptions()# for serialization, enable export compression to
   remove singleton index nodes by modifying analyzer
mmpOpts.SetOptions(oemedchem.OEMatchedPairOptions_Default |
                   oemedchem.OEMatchedPairOptions_ExportCompression)
# create analyzer class with compression option enabled
mmpAnalyzer = oemedchem. OEMatchedPairAnalyzer (mmpOpts)
```

See also:

- · OEIsWriteableMatchedPairAnalyzer
- · OEReadMatchedPairAnalyzer

#### **OEWriteMCSFragDatabase**

```
bool OEWriteMCSFragDatabase (const std::string & fname,
                             const OEMCSFragDatabase &mcsfragdb)
bool OEWriteMCSFragDatabase(OEPlatform::oeostream &ofs,
                             const OEMCSFragDatabase & mcsfragdb)
```

This function serializes the state of the OEMCSFragDatabase instance argument to a file or stream.

- OEIsMCSFragDatabaseFileType
- · OEReadMCSFragDatabase

#### **OEWriteMMPIndexMolecules**

```
int OEWriteMMPIndexMolecules (OEPlatform::oeostream &ofs, unsigned int recID, const.
→OEChem::OEMolBase &inmol,
                               const OEMatchedPairAnalyzer &mmpindex, bool,
\rightarrowinitStream=false)
int OEWriteMMPIndexMolecules (std::string &fragbytes, unsigned int recID, const,
→OEChem::OEMolBase &inmol,
                               const OEMatchedPairAnalyzer &mmpindex, bool,
\rightarrowwriteHeader=true)
```

This function serializes Matched Pair fragmentation information from the passed molecule based on the indexing setting provided in the OEMatchedPairAnalyzer argument.

The goal of this function is to precompute all the fragmentation information needed to allow the provided input molecule to be recorded in the Matched Molecular Pair index with maximum efficiency. For multi-threaded or multiprocessing index creation, moving most of the fragmentation processing activity outside of the index creation activity results in better indexing throughput overall.

#### See also:

· OEReadMMPIndexMolecules

### **CHAPTER**

## **FIVE**

## **RELEASE HISTORY**

## 5.1 OEMedChem TK 1.2.3

Minor internal improvements have been made.

## 5.2 OEMedChem TK 1.2.2

Minor internal improvements have been made.

## 5.3 OEMedChem TK 1.2.1

Minor internal improvements have been made.

## 5.4 OEMedChem TK 1.2.0

## 5.4.1 Internal changes

• Internal functions used to constrain Matched Molecular Pair transforms by applying SMARTS constraints have been replaced with calls to the new preliminary API functions in OEChem. See OECreateAtomSmartsString, OECreateBondSmartsString, and OECreateSmartsString.

## 5.5 OEMedChem TK 1.1.7

Minor internal improvements have been made.

## 5.6 OEMedChem TK 1.1.6

• Minor internal improvements have been made.

## 5.7 OEMedChem TK 1.1.5

#### Fall 2021

• Minor internal improvements have been made.

## 5.8 OEMedChem TK 1.1.4

July 2021

## 5.8.1 Minor bug fixes

• OEMatchedPairOptions\_ComboCuts has been added by default to all cut options.

## 5.9 OEMedChem TK 1.1.3

**Fall 2020** 

## 5.9.1 New features

- . The preliminary API points, OEReadMMPIndexMolecules and OEWriteMMPIndexMolecules are now fully supported.
- Bemis-Murcko fragmentation has been extended to allow inclusion of custom substituents on the framework, using either a custom subsearch or a flag to include unsaturated bonds to hetero atoms on the framework. The class OEBemisMurckoOptions allows specification of these options. The APIs for the functions OEGetBemisMurcko and OEGetRingLinkerSideChainFragments have changed to include an options argument.
- . The versions of functions OEGetBemisMurcko and OEGetRingLinkerSideChainFragments that take a single integer argument to specify fragmentation region are now deprecated.

## **5.9.2 Documentation changes**

- Examples of custom Bemis-Murcko fragmentation have been added to the fragmentation documentation in the Molecule Fragmentation chapter.
- The BemisMurckoPerception example script has been modified to include examples of custom Bemis-Murcko fragmentation, using the flag -unsatHetero to include unsaturated bonds to hetero atoms on the framework and the flag -smartsSubstituents to include substituents specified by given SMARTS patterns.

## 5.10 OEMedChem TK 1.1.2

## 5.10.1 Minor bug fixes

- An internal issue in  $OECreateIDStrings$  that resulted in hanging processes or crashes for some simple structures has been fixed.
- A minor issue that occurred when using a combination of OEMatchedPairOptions\_IndexHSingleCuts OEMatchedPairOptions\_IndexHSites has been fixed. The and OEMatchedPairOptions\_IndexHSingleCuts option now takes precedence.

## 5.11 OEMedChem TK 1.1.1

## 5.11.1 New features

- The following APIs for fast multithreaded generation of matched pair indices, introduced in the 2018. Oct release, have graduated from preliminary API to stable API status:
  - OECreateMMPIndexFile function
  - OECreateMMPIndexStatus class
  - OECreateMMPIndexOptions class

They are now also available in Python, Java, and C#.

## 5.11.2 Documentation changes

- The following examples that create a Matched Molecule Pair index were modified to fix an issue with the SD data handling (options -keepSD, -clearSD, -allSD):
  - Matched Pair analysis generation of a MMP index
  - Matched Pair analysis using a multi-process generation of an MMP index

## 5.12 OEMedChem TK 1.1.0

## 5.12.1 Minor bug fixes

- An issue with Matched Pair index generation that occurred when input structures contained reaction mapping information has been fixed.
- Several issues in the probesite-based preliminary API function  $OEGetMatchOA2$ fixed

## 5.13 OEMedChem TK 1.0.7

### 5.13.1 New features

- The performance of appending segments of matched pair indices together has been significantly improved over previous versions. This activity is a common use-case with parallel index creation approaches.
- A new OEMatchedPairAnalyzer. GetMaxMolIdx method has been added to make identifying the largest molecule index registered to a matched pair index more convenient.
- A new OEMatchedPairAnalyzer. GetMolecule method has been added to make retrieving a molecule from the MMP index more convenient and to eliminate the need to maintain a separate OEMolDatabase for this activity.
- A new OEApplyChEMBL24SolubilityTransforms function has been added to return modified structures using ChEMBL24 solubility data. The existing OEApplyChEMBL18SolubilityTransforms API will be deprecated in future versions.
- A new indexing option, OEMatchedPairOptions\_IndexHSingleCuts, has been added to limit the H-member matched pair index information to single-cut transformations only. The current OEMatchedPairOptions\_IndexHSites option will continue to provide H-member index information for all of single-, double-, or triple-cut transformations. OEMatchedPairOptions\_IndexHSingleCuts takes precedence over OEMatchedPairOptions\_IndexHSites if both options are provided.

## 5.13.2 New features (Preliminary API)

- The following preliminary APIs have been added to provide fast multithreaded generation of matched pair indices<sup>.</sup>
  - OECreateMMPIndexFile function
  - OECreateMMPIndexOptions option class
  - OECreateMMPIndexStatus class
- . New OEReadMMPIndexMolecules and OEWriteMMPIndexMolecules functions have been implemented as preliminary APIs to support multithreaded and parallel matched pair index creation activities.
- New function overloads to *OEMatchedPairGetTransforms* have been added to allow extracting transforms and related matched molecular pairs using 1 or more identified site(s) of substitution on a probe structure.
- New free functions and overloads,  $OEGetMatchA$  chedMolecularPairs, have been added to allow extracting related matched molecular pairs using either a molecule ID or a probe structure with one or more identified  $site(s)$  of substitution.

## 5.13.3 API changes

- A public class, *OEMatchedPairTransform*, has been altered to remove unnecessary implementation details. Several of the methods exposed were previously inaccessible or unnecessary for wrapped language use. The simplified API retains the common methods for interrogating the transforms and matched pairs returned from OEMatchedPairGetTransforms. This is potentially a breaking API change. For custom code using the removed methods, please contact support@eyesopen.com for details on migration activity that might be required.
- $\bullet$  The OEMedChem::OEIsMCSFragDatabaseFiletype function has heen renamed OEISMCSFragDatabaseFileType to follow OpenEye Toolkit's naming scheme.

• The OEMCSFragDatabase. CoreToMolecules. OEMCSFragDatabase. CoreToMoleculeCount. OEMCSFragDatabase.GetMaxCoreMolecule, OEMCSFragDatabase. GetMaxCoreMoleculeCount, and OEMCSFragDatabase.MoleculeToCores methods and the OEMoleculeToCores function have graduated from preliminary API to stable API status for the 2018.Oct release.

## 5.13.4 Minor bug fixes

- The OEGetBemisMurcko function has been corrected so that chain bonds between rings are no longer returned in the OERegionType\_Ring role sets.
- OEMatchedPairGetTransforms has been fixed and no longer returns unusual matched pair transforms related to group bond-insertion changes.
- A bug that seemed to allow reactions to be added to a matched pair index has been fixed so that reaction input is now explicitly rejected. Attempting to add a reaction to the index will now return a status of OEMatchedPairIndexStatus\_NoStructure.
- New options were added to OEMatchedPairIndexStatus to return additional indexing failure conditions.
- returned · OEMatchedPairIndexStatus\_NoFragmentationBonds be may now from OEMatchedPairAnalyzer.AddMol when the input structure has no fragmentation bonds, depending on the H-member indexing option in use.

## 5.13.5 Python-specific changes

• A new match pair index example has been added to demonstrate the creation of an MMP index via parallel processing using the Python multiprocessing module.

## 5.13.6 Documentation changes

• The MCS fragment database examples and match pair index examples have been modified to separate the index creation step from database query activities. See the list of currently available examples in the OEMedChem TK Examples section.

## 5.14 OEMedChem TK 1.0.6

### 5.14.1 New features

• A new status return has been added to indicate when a molecule submitted for indexing by OEMCSFrag-Database has no fragmentation bonds (e.g., is a complete ring system without non-ring substituents). The new constant returned is OEMatchedPairIndexStatus\_NoFragmentationBonds.

## 5.14.2 Minor bug fixes

• An issue with hydrogen atoms on input molecules used with OEApplyChEMBL18SolubilityTransforms has been fixed. This function is now tolerant of explicit hydrogen atoms on the input molecule.

## 5.15 OEMedChem TK 1.0.5

### 5.15.1 New features

• OEWriteMatchedPairAnalyzer now supports a new option, OEMatchedPairOptions\_ExportHKeys, additional which will serialize information to reduce the loading time from <sub>a</sub> The saved information results in slightly larger index files OEReadMatchedPairAnalyzer call.  $(+10-20%)$  but substantially reduced load times (>10x). OEMatchedPairOptions\_ExportHKeys is enabled by default.

Warning: The change in the serialized data format requires that any existing saved matched pair analyzer index files be regenerated if they were created using a previous OpenEye Toolkit version. Indices serialized from this version cannot be read by older versions.

- OEReadMatchedPairAnalyzer now supports a new Boolean argument that controls the regeneration of index information during the read. By default, the regeneration is suppressed and index data read from the file is used.
- A new *OEMatchedPairTransformExtractOptions* option class has been added to control the transformations returned from the OEMatchedPairGetTransforms functions. Several new function overloads have been provided that use this new option class.

## 5.15.2 Minor bug fixes

- Output to st dout from within OEMatchedPairAnalyzer has been removed.
- Several tetrahedral stereo issues in the transformations extracted by OEMatchedPairGetTransforms have been fixed.
- Erroneous warnings had been thrown about duplicate structures when appending matched pair indices if duplicate structures are allowed. This has been fixed.
- An issue with exported matched pair transformations that occurred when search qualifiers were requested and matched pair core atoms contained charged atoms has been fixed. The search qualifiers erroneously duplicated charge information in the output string, causing transformation mappings to fail.

## 5.15.3 Documentation changes

• Examples have been updated to use OEDeleteEverythingExceptTheFirstLargestComponent rather than the deprecated function OETheFunctionFormerlyKnownAsStripSalts.

## 5.16 OEMedChem TK 1.0.4

## 5.16.1 New features

- A major overhaul of the fragmentation internals of *OEMCSFragDatabase* now allows an arbitrary number of fragmentation cuts. Additionally, an experimental capability for performing limited ring bond fragmentation cuts has been provided. Because of the combinatorial explosion of fragments generated with increased fragmentation cuts, care should be used when determining fragmentation cut limits. The enhanced ability to do arbitrary N-cut fragmentation makes the MCS results from the fragmentation approach much closer to an OEMCSSearch mapping result, with better overall performance than a mapping approach. To specify the fragmentation cut limits, see OEMCSFragDatabaseOptions. SetFragLimits, OEMCSFragDatabaseOptions.GetMinFragLimit, OEMCSFragDatabaseOptions. GetMaxFragLimit, OEMCSFragDatabaseOptions.SetRingFragLimit, and OEMCSFragDatabaseOptions.GetRingFragLimit.
- A new method, OEMCSFragDatabase. IsIndexed, has been added to determine whether a particular molecule index has been registered in the database. Depending on the indexing option settings, a particular molecule may be rejected from indexing. This method allows that condition to be interrogated.
- A new method, OEMatchedPairAnalyzerOptions. HasIndexableFragmentHeavyAtomRange, has been added to allow an options object to indicate that a min-max range has been specified via OEMatchedPairAnalyzerOptions.SetIndexableFragmentRange.
- The OEMatchedPairAnalyzerOptions options class now supports the operator== comparison to more easily determine the equality of two options objects.
- OEConfigureMatchedPairIndexOptions and OEConfigureMCSFragDatabaseOptions now support an -allfrags option to clear the min-max indexing constraint and to allow the indexing of all fragments. Indexing all fragments has indexing size and indexing performance implications for OEMCSFrag-Database and OEMatchedPairAnalyzer objects.
- The OEConfigureMCSFragDatabaseOptions function now supports the newly added -minfrageuts,-maxfrageuts, and-ringeuts options.
- OEReadMatchedPairAnalyzer now supports the ability to merge indices generated from segments of a large set of input structures. This capability can be used in a parallel processing approach to increase the throughput of the time-consuming structure indexing phase.

## 5.16.2 Preliminary Fragmentation API

- $\bullet$  New Preliminary API methods have been added to allow the interrogation of intermediate fragmentation output and internal index information from the OEMCSFragDatabase OEMCSFragDatabase. object. See OEMCSFragDatabase.MoleculeToCores, CoreToMolecules, OEMCSFragDatabase.CoreToMoleculeCount, OEMCSFragDatabase. GetMaxCoreMolecule, and OEMCSFragDatabase. GetMaxCoreMoleculeCount.
- A new example has been provided to demonstrate using the new experimental fragment API of OEMCSFrag-Database. See MCSFragOccurrence.py.

## 5.16.3 Minor bug fixes

- A bug that resulted in the return of [R1] [R2] fragments in the Matched Molecular Pair transforms returned by OEMatchedPairGetTransforms has been fixed.
- The OEMCSFragDatabase. GetScores has been changed to make the API more consistent with OEFP-Database. The end range argument is now exclusive instead of inclusive when a non-zero value is specified.
- . The OEMCSFragDatabase. GetScores and OEMCSFragDatabase. GetSortedScores methods previously returned an arbitrary OEMCSMolSimScore when different identified cores had the same score (in particular for OEMCSScoreType\_AtomCount scoring). This has been fixed.
- The undocumented internal debugging method OEMedChem:: OEMCSFragDatabase:: Dump has been removed from the public API.

## 5.16.4 Python-specific changes

• Minor changes to some examples were made to synchronize the behavior and output with other wrapped language examples.

## 5.16.5 Java-specific changes

• Minor changes to some examples were made to synchronize the behavior and output with other wrapped language examples.

## 5.16.6 C#-specific changes

• Minor changes to some examples were made to synchronize the behavior and output with other wrapped language examples.

## 5.16.7 Documentation changes

• New methods have been documented in their respective classes.

## 5.17 OEMedChem TK 1.0.3

### 5.17.1 New features

- A new class, OEMCSFragDatabase, has been implemented that supports an MCS fragmentation approach for returning Tanimoto and Tversky MCS similarity scores from a query against an indexed set of input structures. This approach is similar to the OEMatchedPairAnalyzer and the API is functionally equivalent to the OEFP-Database API for ease of use. Because the indexing phase of the input structures can be time-consuming, new functions to capture and reload the MCS fragmentation index are provided as OEReadMCSFragDatabase and OEWriteMCSFragDatabase.
- A new options class, OEMCSFragDatabaseOptions, has been added to control the indexing phase of OEMCS-FragDatabase usage.
- A new constant, MCSFrags, has been added to support OEMCSFragDatabase serialization and may be returned by OEGetMatchedPairAnalyzerFileType.

- $\bullet$  Two new functions, OEConfigureMCSFragDatabaseOptions and OESetupMCSFragDatabaseOptions, have been added to allow configuration of indexing parameters from the command line for *OEMCSFragDatabaseOptions*.
- A new function, OEMCSFragDatabaseCoreQuery, has been added to annotate MCS fragment SMILES cores returned from OEMCSFragDatabase. GetSortedScores and OEMCSMolSimScore with SMARTS qualifiers. This allows more restrictive and meaningful mapping highlights to be applied for depicting similarity hit results.
- The OEMCSFragDatabase class now supports user-customization of the similarity score returned by implementing a class derived from OEMCSSimFuncBase. Two concrete implementations of scoring functions, OEM-CSTanimotoSim and OEMCSTverskySim, have been added.
- The indexing performance of *OEMatchedPairAnalyzer* has been significantly improved. While this is highly dependent on the input structures and the requested indexing parameters, the provided default indexing settings with a drug-like set of structures show an indexing improvement of  $\sim 25\%$ .
- A new overloaded function, OEIsMatchedPairAnalyzerFileType, has been added to simplify the validation of matched pair index files. The now unnecessary OEIsReadableMatchedPairAnalyzer and OEIsWriteableMatchedPairAnalyzer functions have been deprecated.

## 5.17.2 Documentation changes

• New documentation has been added for the OEMCSFragDatabase API and the ancillary support functions, classes, and constants.

## 5.18 OEMedChem TK 1.0.2

## 5.18.1 Minor bug fixes

- An issue that could lead to corrupted stereochemistry alpha to fragmentation bonds during Matched Pair analysis has been repaired.
- Minor internal improvements have been made.

## 5.19 OEMedChem TK 1.0.1

### 5.19.1 Minor bug fixes

• The OECreateIDStrings function has been repaired and will no longer crash.

# 5.20 OEMedChem TK 1.0.0

### 5.20.1 Licensing changes

• In preparation for new licensing requirements for **OEMedChem TK**, license checks have been added to  $OE$ MatchedPairAnalyzer constructor. Visit https://www.eyesopen.com/contact if you need a license for matched pair activities.

## 5.20.2 OEMedChem functionalities

This is the first official release of OEMedChem functionalities, previously released in beta form. An overview of its capabilities is provided below.

## 5.20.3 Matched molecular pair analysis

A powerful analysis engine and functions support the identification of matched molecular pairs that differ by both heavy-atom and hydrogen-atom substitutions. Additionally, the analyzer supports the ability to be saved and restored to disk or stream. The analyzer includes the following functions:

- OEMatchedPairAnalyzer
- OEMatchedPairApplyTransforms
- · OEReadMatchedPairAnalyzer
- · OEWriteMatchedPairAnalyzer
- OEMatchedPairAnalyzerOptions
- · OEConfigureMatchedPairIndexOptions
- · OESetupMatchedPairIndexOptions

Functions and classes are provided to allow extraction and inspection of transformations based on matched molecular pairs found during structure indexing as well as the specific matched pairs and data associated with those transformations:

- OEMatchedPair
- OEMatchedPairTransform
- · OEMatchedPairGetTransforms

ChEMBL18 solubility data has been indexed with the matched pair analyzer to modify input structures according to the solubility transforms and to annotate modified structures with the net change in solubility data from ChEMBL:

· OEApplyChEMBL18SolubilityTransforms

## 5.20.4 Fragmentation and perception capabilities

The following functions are provided to return perceived regions for fragmentation strategies:

- OEGetBemisMurcko
- OEGetFuncGroupFragments
- OEGetRegionTypeName
- OEGetRegionType
- · OEGetRingChainFragments
- · OEGetRingLinkerSideChainFragments

## 5.20.5 Belief theory

Functions are provided to return information for belief theory usage based on [Muchmore-2008]:

- · OECalculateComboBelief
- OECalculateETComboBelief

## 5.20.6 Similarity

Functions are provided to return the graph-edit similarity used in clustering BROOD hitlists:

- · OECreateIDString
- · OECreateIDStrings

## 5.20.7 Complexity measures

Functions are provided to return individual terms that make up the molecular complexity as defined by [Bertz-1981]:

- · OEDetermineConnectiveComplexity
- · OEDetermineElementalComplexity
- · OEDetermineMolecularComplexity
- OEDetermineSymmetryComplexity
- · OENormalMolecularComplexity

Functions are provided to return a ring complexity measure similar to that defined by [Gasteiger-1979]:

- · OEDetermineRingComplexity
- · OEGetRingValue

Functions are provided to return a measure of stereo complexity as defined by [Boda-2007]:

- · OEDetermineStereoComplexity
- · OENormalStereoComplexity

A function is provided to return a measure of the total molecular complexity, which is a sum of the provided individual complexity measures:

· OETotalMolecularComplexity

### 5.20.8 Minor bug fixes

• As a result of a minor bug fix in OEChem TK, OEDetermineStereoComplexity, OENormalStereoComplexity, and OENormalStereoComplexity functions might return slightly different values for molecules containing transition metals, lanthanides, or actinides.

## 5.20.9 Documentation changes

- New documentation code snippets for C++, Java, and C# have been added to demonstrate matched pair index creation, serialization, and deserialization.
- Examples have been updated to allow explicit specification of the mmpMinPairThreshold arguments for OEMatchedPairApplyTransforms and OEApplyChEMBL18SolubilityTransforms.
- Several molecular complexity functions that were inadvertently removed from the documentation have been re-added.
- The Matched Pair analysis and transformations example has been modified to reduce the amount of output that is typical for a general indexing activity.

## 5.21 OEMedChem TK 0.9.6

## 5.21.1 Beta-API changes

- New functions have been added support matched pair index  $\overline{f}$ serialization (see OEGetMatchedPairAnalyzerFileType, OEIsReadableMatchedPairAnalyzer, OEIsWriteableMatchedPairAnalyzer, OEReadMatchedPairAnalyzer, OEWriteMatchedPairAnalyzer).
- A new option to remove unnecessary index node information during the index export activity is now available (see OEMatchedPairOptions\_ExportCompression).
- New methods have been added to the analyzer and option classes to allow altering options that do not invalidate an active index (see OEMatchedPairOptions\_ValidAlterOpts, OEMatchedPairOptions\_ValidIndexOpts, OEMatchedPairAnalyzer.ModifyOptions, OEMatchedPairAnalyzerOptions.ModifyOptions).
- A new method has been added to the analyzer options class to support command-line specification of options (see OEMatchedPairAnalyzerOptions. SetProcessorType).
- A new argument has been added to the functions that apply matched pair transformations that limits application of transformations only to those that meet or exceed the specified number of matched pairs (see OEApplyChEMBL18SolubilityTransforms and OEMatchedPairApplyTransforms).

## 5.21.2 New features

- The matched pair analyzer now supports the ability to be saved and restored to disk or stream. This allows checkpoint backups during a long analysis run or a long analysis run to be restored from disk for subsequent use without the need to re-run the analysis (see OEReadMatchedPairAnalyzer and OEWriteMatchedPairAnalyzer).
- The ChEMBL18 solubility data has been re-indexed with the latest version of the matched pair analyzer to include hydrogen-member transformations. The result is a larger number of transformations and potentially a larger number of transformed and annotated structures returned For a 10K test set of structures, using from OEApplyChEMBL18SolubilityTransforms. OEMatchedPairContext\_Bond0 resulted in an average of three times more output structures and  $OEMatchedPairContext\_Bond2$  produced an average of 4.5 times the number of output structures as the previous release when applying all transformations by overriding the default value of minMMPThreshold parameter with 0. Using the default value (5) for the minMMPThreshold parameter, the number of annotated structures from the 10K test set compared to the previous version is approximately the same for the OEMatchedPairContext\_Bond0 context and approximately 25% less structures for the

OEMatchedPairContext Bond2 context. The number of structures produced is input dataset-dependent, so tuning of the minMMPThreshold parameter is highly encouraged.

- New functions to configure matched pair indexing options and to set indexing options from the command line have been added (see OEConfigureMatchedPairIndexOptions and OESetupMatchedPairIndexOptions). Example scripts have been updated to demonstrate the use of these new functions.
- A new method has been added to return a count of the number of active index nodes (see OEMatchedPairAnalyzer.NumIndexNodes).

## 5.21.3 Minor bug fixes

• Structures returned from the application of matched pair transformations will now have their coordinates cleared. Previously, newly added atoms were simply placed at the origin, possibly affecting stereochemistry and generating odd depiction output.

## 5.21.4 Documentation fixes

- Documentation of the serialization available for new is support  $now$ OEGetMatchedPairAnalyzerFileType, OEIsReadableMatchedPairAnalvzer. OEIsWriteableMatchedPairAnalyzer, OEReadMatchedPairAnalyzer, OEWriteMatchedPairAnalyzer, OEMatchedPairAnalyzer.ModifyOptions, OEMatchedPairOptions\_ExportCompression, OEMatchedPairAnalyzerFileType, OEMatchedPairOptions\_ValidAlterOpts and OEMatchedPairOptions\_ValidIndexOpts.
- Documentation of the new command-line configuration support is now available for OEConfigureMatchedPairIndexOptions and OESetupMatchedPairIndexOptions.

## 5.22 OFMedChem TK 0.9.5

### 5.22.1 New features

- The matched pair analyzer now supports the identification of matched molecular pairs that differ by heavyatom and hydrogen-atom substitutions. This additional indexing activity returns significantly more matched molecular pairs than the previous version. The hydrogen-atom indexing activity has been enabled by default. To perform heavy-atom indexing only, remove the OEMatchedPairOptions IndexHSites option from OEMatchedPairOptions\_Default and set the desired option(s) explicitly via OEMatchedPairAnalyzerOptions.SetOptions.
- The matched pair analyzer now supports single bond insertion differences between matched molecular pairs. Previously, a minimum change of 1-atom was identified in the substituent change between the matched pairs.

### 5.22.2 Beta-API changes

- OEMatchedPairOptions\_IndexHSites is a new option that enables hydrogen-atom indexing support to the default indexing activities.
- OEMatchedPairTransformExtractMode\_SuppressNodeSort is a new option that suppresses the internal sorting of index nodes prior to extraction of transformations and matched pairs for debugging and analysis of indexing problems.
- · OEMatchedPairTransformExtractMode\_AddMCSCorrespondence is a new extraction option that returns the maximum common substructure correspondence between the matched molecular pairs in the form of atom-mapping information applied to the MCS cores.
- OEMatchedPairTransformExtractMode\_AddAttachmentPts is a new extraction option that requests the addition of Rgroup attachment points on the returned matched molecular pair transforms.

### 5.22.3 Major bug fixes

- A number of bugs related to the identification of the maximum common substructure for matched molecular pairs have been corrected.
- The ChEMBL solubility data has been re-indexed to capture indexing fixes, potentially impacting the results returned from OEApplyChEMBL18SolubilityTransforms.
- An internal index node sort now includes the number of fragmentation cuts in the sort criterion to preferentially return single > double > triple cuts for the largest maximum common substructures.
- A significant refactoring of internal activities has been performed to prepare for additional public API exposure in future versions.

## 5.23 OEMedChem TK 0.9.4

### 5.23.1 Beta-API changes

• The OEMatchedPairAnalyzer. AddMol return value has been changed. Negative return values no longer indicate a duplicate record ID in the index, but instead return various status values to indicate specific details of an indexing failure.

**Note:** The interpretation of return values from this method in user-coded scripts may need to be altered.

### 5.23.2 New features

- The indexing of structures now supports the specification of a zero or positive integer record ID to be used for referencing the input structures. This simplifies cross-referencing to externally maintained or managed data structures. For example, see changes to following:
  - OEMatchedPairAnalyzer
  - OEMatchedPairAnalyzer.AddMol
  - OEMatchedPairAnalyzer. IsIndexed
  - OEMatchedPairIndexStatus

- OEMatchedPairIndexStatusName
- OEMatchedPairIndexStatusType
- Prioritization of matched pair index nodes is now performed based on the size of the MCS for the indexed pair(s). This results in a significant reduction of redundant and less interesting transformations extracted from the index. The ChEMBL solubility data was reanalyzed with this optimization and results in approximately 1/3 fewer (redundant) transformations to be applied via OEApplyChEMBL18SolubilityTransforms.
- A function has been provided to allow extraction and inspection of transformations based on the matched molecular pairs found during indexing as well as the specific matched pairs and data associated with those transformations. For example, see changes to the following:
  - OEMatchedPairGetTransforms
  - OEMatchedPairTransform
  - $-$  OEMatchedPair
- A new overload of *OEMatchedPairGetTransforms* now provides the ability to retrieve related transformations and matched molecular pairs based on a probe molecule. The probe molecule is fragmented based on the analyzer indexing strategy; matched pair index nodes that have common cores to the provided probe are used to retrieve related matched pair transformations.

## 5.23.3 Major bug fixes

- Stereoisomers are now indexed properly by OEMatchedPairAnalyzer. Previously, stereoisomers were incorrectly considered duplicates and were rejected during indexing.
- . The perceived regions from OEGetRingChainFragments and OEGetRingLinkerSideChainFragments are based on the heavy atoms in the molecule. If the molecule contains explicit hydrogen atoms, those atoms will be returned in the same perception set(s) as their alpha-heavy atom neighbors. The documentation for these functions has been altered to reflect the new behavior as well as noting the requirement of the OEFindRingAtomsAndBonds perception activity prior to use of these functions.
- A crash in  $OETotalMolecularComplexity$  for highly bridged ring systems has been fixed. An issue that caused OEDetermineSymmetryComplexity to crash when the required call to OEPerceiveChiral had not been performed on the input molecule has also been fixed.
- The complexity computation functions have been altered to verify that the required perceptions have been performed. Due to the const arguments to these functions, the perceptions cannot be performed internally and will now throw an error if the perception state is out of date for the provided input molecule. The functions affected are:
  - OEDetermineRingComplexity
  - OEDetermineSymmetryComplexity
  - OEDetermineStereoComplexity
  - OENormalStereoComplexity
  - OETotalMolecularComplexity

## 5.23.4 Documentation fixes

- New examples have been added to demonstrate the new API functions.
- New examples have been added for C++, Python, Java, and C#.
- Minor naming changes to constants for the beta matched pair API were made for consistency.
- Minor fixes have been made to the complexity function documentation to reflect the correct API points.

## 5.24 OEMedChem TK 0.9.3

### 5.24.1 New features

- New experimental classes and a new function for Matched Molecular Pair analysis were added. These APIs are experimental and they will likely change in future versions.
  - OEMatchedPairAnalyzer
  - OEMatchedPairAnalyzerOptions
  - OEMatchedPairApplyTransforms
- New functions were added to return type to name conversions for new parameterized constants.
  - OEMatchedPairContextName
  - OEMatchedPairContextType
  - OEMatchedPairProcessorName
  - OEMatchedPairProcessorType
  - OEMatchedPairOptionsName
  - OEMatchedPairOptionsType
- New functions were added to return information for belief theory usage based on [Muchmore-2008].
  - OECalculateComboBelief
  - OECalculateETComboBelief
- New functions were added based on the implementation in OEGetRingLinkerSideChainFragments to return annotated Bemis Murcko regions and types from the perception as defined in [Bemis-1996].
  - OEGetBemisMurcko
  - OEGetRegionType
  - OEGetRegionTypeName
- New functions were added to return the graph-edit similarity used in clustering BROOD hitlists.
  - OECreateIDString
  - OECreateIDStrings
- New functions were added which return individual terms that make up the Molecular Complexity as defined by [Bertz-1981].
  - OEDetermineConnectiveComplexity
  - OEDetermineElementalComplexity

- OEDetermineMolecularComplexity
- OEDetermineSymmetryComplexity
- OENormalMolecularComplexity
- New functions were added for a ring complexity measure similar to that defined by [Gasteiger-1979].
  - OEDetermineRingComplexity
  - OEGetRingValue
- New functions were added which return a measure of stereo complexity as defined by [Boda-2007].
  - OEDetermineStereoComplexity
  - OENormalStereoComplexity
- A new function was added to return a measure of the total molecular complexity which is a sum of individual complexity measures above.
  - OETotalMolecularComplexity

### 5.24.2 Known bugs

- The beta Matched Pair analyzer api internally removes stereochemistry from the internally indexed structures. It should more properly treat the presence of stereochemistry for duplicate checking and indexing equivalently. This issue will be repaired in the next release.
  - OEMatchedPairAnalyzer

### 5.24.3 Documentation fixes

- Added documentation for
  - OEMedChemGetArch
  - OEMedChemGetLicensee
  - OEMedChemGetPlatform
  - OEMedChemGetRelease
  - OEMedChemGetSite
  - OEMedChemGetVersion
  - OEMedChemIsLicensed

## 5.25 OEMedChem TK 0.9.2

### 5.25.1 Minor bug fixes

· OEGetRingChainFragments, OEGetRingLinkerSideChainFragments, OEGetFuncGroupFragments will now OEThrow.Error whenever the molecule passed in does not have RingAtomsAndBonds perceived.

## 5.26 OEMedChem TK 0.9.1

## 5.26.1 New features

• Several new experimental APIs added. These APIs are not officially supported yet and they will likely change in a future revision.

## 5.27 OEMedChem TK 0.9.0

## 5.27.1 New features

Providing the following fragmentation functions:

- · OEGetRingChainFragments
- · OEGetRingLinkerSideChainFragments
- · OEGetFuncGroupFragments

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

## **CHAPTER**

## **SEVEN**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

### **CHAPTER**

## **EIGHT**

## **CITATION**

# 8.1 Orion<sup>®</sup> Floes

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

## **8.2 Toolkits and Applications**

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

# **8.3 OpenEye Web Services**

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

## **NINE**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project       | Website                                                    | License |
|-----------------------|------------------------------------------------------------|---------|
| abseil-cpp            | https://github.com/abseil/abseil-cpp                       | https:/ |
| absl-py               | https://github.com/abseil/abseil-py                        | https:/ |
| aiohttp               | https://docs.aiohttp.org/en/stable/                        | https:/ |
| aiosignal             | https://github.com/aio-libs/aiosignal                      | https:/ |
| Amazon Linux 2        | https://aws.amazon.com/amazon-linux-2                      | N/A     |
| AmberUtils            | http://ambermd.org                                         | N/A     |
| ambit                 | https://github.com/khimaros/ambit                          | https:/ |
| amqp                  | https://github.com/celery/py-amqp                          | https:/ |
| anaconda-anon-usage   | <b>Orion Floes</b>                                         | https:/ |
| angular               | https://github.com/angular/angular.js                      | https:/ |
| angular-animate       | https://github.com/angular/angular.js                      | https:/ |
| angular-cache         | https://github.com/jmdobry/angular-cache                   | https:/ |
| angular-cookies       | https://github.com/angular/angular.js                      | https:/ |
| angular-loggly-logger | https://github.com/ajbrown/angular-loggly-logger           | https:/ |
| angular-mocks         | https://github.com/angular/angular.js                      | https:/ |
| angular-resource      | https://github.com/angular/angular.js                      | https:/ |
| angular-toggle-switch | https://github.com/cgarvis/angular-toggle-switch           | https:/ |
| angular-ui-grid       | https://github.com/angular-ui/ui-grid                      | https:/ |
| angular-ui-router     | https://github.com/angular-ui/ui-router                    | https:/ |
| angular-ui-tree       | https://github.com/angular-ui-tree/angular-ui-tree         | https:/ |
| angular-vs-repeat     | https://github.com/kamilkp/angular-vs-repeat               | https:/ |
| aniso8601             | https://bitbucket.org/nielsenb/aniso8601                   | https:/ |
| annotated-types       | https://github.com/annotated-types/annotated-types         | https:/ |
| anyio                 | https://github.com/agronholm/anyio                         | https:/ |
| appdirs               | http://github.com/ActiveState/appdirs                      | http:// |
| appengine             | https://google.golang.org/appengine                        | https:/ |
| arabic-reshaper       | https://github.com/mpcabd/python-arabic-reshaper/          | https:/ |
| archspec              | https://github.com/archspec/archspec/blob/master/README.md | https:/ |

| Name of Project               | Website                                                                             | License                                                                          |
|-------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                | https:/                                                                          |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                       | https:/                                                                          |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                          | https:/                                                                          |
| ascii85                       | https://github.com/huandu/node-ascii85                                              | https:/                                                                          |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                      | https:/                                                                          |
| asgiref                       | https://github.com/django/asgiref/                                                  | https:/                                                                          |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                                 | https:/                                                                          |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render               | https:/                                                                          |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers                   | https:/                                                                          |
| assertions                    | https://github.com/smartystreets/assertions                                         | https:/                                                                          |
| asttokens                     | https://github.com/gristlabs/asttokens                                              | https:/                                                                          |
| astunparse                    | https://github.com/simonpercivall/astunparse                                        | https:/                                                                          |
| async-lru                     | https://github.com/aio-libs/async-lru                                               | https:/                                                                          |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                           | https:/                                                                          |
| atk-1.0                       | https://docs.gtk.org/atk/                                                           | https:/                                                                          |
| atomic                        | https://github.com/uber-go/atomic                                                   | https:/                                                                          |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                    | https:/                                                                          |
| attrs                         | https://www.attrs.org/                                                              | https:/                                                                          |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                                   | https:/                                                                          |
| Babel                         | https://github.com/python-babel/babel                                               |                                                                                  |
| backcall                      | https://github.com/takluyver/backcall                                               | https:/                                                                          |
| backports                     | https://github.com/brandon-rhodes/backports                                         | https:/                                                                          |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                             | https:/                                                                          |
| base62                        | https://github.com/kare/base62                                                      | https:/                                                                          |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                      | https:/                                                                          |
| billiard                      | https://github.com/celery/billiard                                                  | https:/                                                                          |
| biopython                     | https://biopython.org                                                               | https:/                                                                          |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https:/                                                                          |
| bitset                        | https://github.com/willf/bitset                                                     | https:/                                                                          |
| blas                          | https://www.netlib.org/blas/                                                        | https:/                                                                          |
| bleach                        | https://github.com/mozilla/bleach                                                   | https:/                                                                          |
| blessings                     | https://github.com/erikrose/blessings                                               | https:/                                                                          |
| blinker                       | https://pythonhosted.org/blinker/                                                   | https:/                                                                          |
| blosc                         | https://github.com/Blosc/python-blosc                                               | https:/                                                                          |
| blosc2                        | https://github.com/Blosc/python-blosc2                                              | https:/                                                                          |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https:/                                                                          |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                                          |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                                          |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                                                          |
| boto3                         | https://github.com/boto/boto3                                                       | https:/                                                                          |
| botocore                      | https://github.com/boto/botocore                                                    | https:/                                                                          |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                                                          |
| Brotli                        | https://github.com/google/brotli                                                    | https:/                                                                          |
| brotli-bin                    | https://github.com/google/brotli                                                    | https:/                                                                          |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                                                          |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                          | https:/                                                                          |
| bson                          | http://github.com/py-bson/bson                                                      | https:/                                                                          |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https:/                                                                          |
| bzip2                         | https://www.bzip.org                                                                | https:/                                                                          |
| Name of Project               | Website                                                                             | License                                                                          |
| c-ares                        | https://github.com/c-ares/c-ares                                                    | https://                                                                         |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            | https://                                                                         |
| cached-property               | https://github.com/pydanny/cached-property                                          | https://                                                                         |
| cachetools                    | https://github.com/tkem/cachetools/                                                 | https://                                                                         |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           | https://                                                                         |
| canvas                        | https://github.com/Automattic/node-canvas                                           | https://                                                                         |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              | https://                                                                         |
| celery                        | https://github.com/celery/celery                                                    | https://                                                                         |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         | https://                                                                         |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                           | https://                                                                         |
| cffi                          | https://github.com/python-cffi/cffi                                                 | https://                                                                         |
| cftime                        | https://pypi.org/project/cftime/                                                    | https://                                                                         |
| chardet                       | https://github.com/chardet/chardet                                                  | https://                                                                         |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        | https://                                                                         |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             | https://                                                                         |
| click                         | https://palletsprojects.com/p/click/                                                | https://                                                                         |
| click-completion              | https://github.com/click-contrib/click-completion                                   | https://                                                                         |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   | https://                                                                         |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      | https://                                                                         |
| click-repl                    | https://github.com/untitaker/click-repl                                             | https://                                                                         |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            | https://                                                                         |
| cmake                         | https://cmake.org/                                                                  | https://                                                                         |
| colorama                      | https://github.com/tartley/colorama                                                 | https://                                                                         |
| comm                          | https://github.com/ipython/comm                                                     | https://                                                                         |
| compose                       | https://github.com/docker/compose                                                   | https://                                                                         |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        | https://                                                                         |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      | https://                                                                         |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     | https://                                                                         |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            | https://                                                                         |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           | https://                                                                         |
| confuse                       | https://github.com/beetbox/confuse                                                  | https://                                                                         |
| contourpy                     | https://github.com/contourpy/contourpy                                              | https://                                                                         |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               | https://                                                                         |
| cryptography                  | https://github.com/pyca/cryptography                                                | https://                                                                         |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                                | https://                                                                         |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           | https://                                                                         |
| cupy-cuda113                  | https://cupy.dev/                                                                   | https://                                                                         |
| curl                          | https://curl.se                                                                     | https://                                                                         |
| cycler                        | https://github.com/matplotlib/cycler                                                | https://                                                                         |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             | https://                                                                         |
| Cython                        | https://cython.org                                                                  | https://                                                                         |
| d3                            | https://github.com/mbostock/d3                                                      | https://                                                                         |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           | https://                                                                         |
| ddsketch                      | http://github.com/datadog/sketches-py                                               | https://                                                                         |
| debugpy                       | https://aka.ms/debugpy                                                              | https://                                                                         |
| decimal                       | https://github.com/shopspring/decimal                                               | https://                                                                         |
| decorator                     | https://github.com/micheles/decorator                                               | https://                                                                         |
| deepdiff                      | https://github.com/seperman/deepdiff                                                | https://                                                                         |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             | https://                                                                         |
| Name of Project               | Website                                                                             | License                                                                          |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 |                                                                                  |
| dill                          | https://github.com/uqfoundation/dill                                                |                                                                                  |
| distro                        | Orion Floes                                                                         |                                                                                  |
| Django                        | https://www.djangoproject.com/                                                      |                                                                                  |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                    |                                                                                  |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                   |                                                                                  |
| django-csp                    | https://github.com/mozilla/django-csp                                               |                                                                                  |
| django-extensions             | https://github.com/django-extensions/django-extensions                              |                                                                                  |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                          |                                                                                  |
| django-redis                  | https://github.com/jazzband/django-redis                                            |                                                                                  |
| django-taggit                 | https://github.com/jazzband/django-taggit                                           |                                                                                  |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                              |                                                                                  |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                              |                                                                                  |
| djangorestframework           | https://www.django-rest-framework.org/                                              |                                                                                  |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                      |                                                                                  |
| dm-tree                       | https://github.com/deepmind/tree                                                    |                                                                                  |
| docker-py                     | https://github.com/docker/docker-py/                                                |                                                                                  |
| docopt                        | https://docopt.org                                                                  |                                                                                  |
| docutils                      | https://docutils.sourceforge.io                                                     |                                                                                  |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                         |                                                                                  |
| editdistance                  | https://github.com/roy-ht/editdistance                                              |                                                                                  |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                               |                                                                                  |
| einops                        | https://github.com/arogozhnikov/einops                                              |                                                                                  |
| entrypoints                   | https://github.com/takluyver/entrypoints                                            |                                                                                  |
| errors                        | https://github.com/pkg/errors                                                       |                                                                                  |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                              |                                                                                  |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                       |                                                                                  |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         |                                                                                  |
| executing                     | https://github.com/alexmojaki/executing                                             |                                                                                  |
| expat                         | https://libexpat.github.io                                                          |                                                                                  |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                   |                                                                                  |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 |                                                                                  |
| fftw                          | https://www.fftw.org                                                                |                                                                                  |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              |                                                                                  |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             |                                                                                  |
| finufft                       | https://github.com/flatironinstitute/finufft                                        |                                                                                  |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         |                                                                                  |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               |                                                                                  |
| flit-core                     | https://github.com/pypa/flit                                                        |                                                                                  |
| FLTK                          | https://www.fltk.org/index.php                                                      |                                                                                  |
| fmt                           | https://fmt.dev/latest/index.html                                                   |                                                                                  |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         |                                                                                  |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      |                                                                                  |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       |                                                                                  |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   |                                                                                  |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            |                                                                                  |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               |                                                                                  |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             |                                                                                  |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 |                                                                                  |
| Name of Project               | Website                                                                             | License                                                                          |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https:/                                                                          |
| freetype                      | https://freetype.org                                                                | https:/                                                                          |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https:/                                                                          |
| frozendict                    | Orion Floes                                                                         | https:/                                                                          |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                              | https:/                                                                          |
| fsmlite                       | https://github.com/tkem/fsmlite                                                     | https:/                                                                          |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                           | https:/                                                                          |
| funcy                         | https://github.com/Suor/funcy                                                       | https:/                                                                          |
| gast                          | https://github.com/serge-sans-paille/gast/                                          | https:/                                                                          |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                | https:/                                                                          |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             | https:/                                                                          |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https:/                                                                          |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             | https:/                                                                          |
| genproto                      | https://google.golang.org/genproto/googleapis                                       | https:/                                                                          |
| geometric                     | https://openbase.com/python/geometric                                               | https:/                                                                          |
| giflib                        | https://giflib.sourceforge.net                                                      | https:/                                                                          |
| glib                          | https://docs.gtk.org/glib/                                                          | https:/                                                                          |
| GLM Library                   | https://github.com/g-truc/glm                                                       | https:/                                                                          |
| gls                           | https://github.com/jtolds/gls                                                       | https:/                                                                          |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https:/                                                                          |
| go-connections                | https://github.com/docker/go-connections                                            | https:/                                                                          |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https:/                                                                          |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https:/                                                                          |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https:/                                                                          |
| go-ini                        | https://github.com/go-ini/ini                                                       | https:/                                                                          |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             | https:/                                                                          |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https:/                                                                          |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           | https:/                                                                          |
| go-ole                        | https://github.com/go-ole/go-ole                                                    | https:/                                                                          |
| go-pg                         | https://github.com/go-pg/pg                                                         | https:/                                                                          |
| go-redis                      | https://github.com/go-redis/redis/v8                                                | https:/                                                                          |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                            | https:/                                                                          |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                            | https:/                                                                          |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                              | https:/                                                                          |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                                   | https:/                                                                          |
| go-units                      | https://github.com/docker/go-units                                                  | https:/                                                                          |
| go-version                    | https://github.com/hashicorp/go-version                                             | https:/                                                                          |
| go-zglob                      | https://github.com/mattn/go-zglob                                                   | https:/                                                                          |
| go.opencensus                 | https://go.opencensus.io                                                            | https:/                                                                          |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                | https:/                                                                          |
| goconvey                      | https://github.com/smartystreets/goconvey                                           | https:/                                                                          |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                       | https:/                                                                          |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       | https:/                                                                          |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https:/                                                                          |
| google-cloud-go               | https://cloud.google.com/go                                                         | https:/                                                                          |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 | https:/                                                                          |
| google-pasta                  | https://github.com/google/pasta                                                     | https:/                                                                          |
| google.golang.org/api         | https://google.golang.org/api                                                       | https:/                                                                          |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  | https:/                                                                          |
|                               |                                                                                     |                                                                                  |
| Name of Project               | Website                                                                             | License                                                                          |
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https:/                                                                          |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https:/                                                                          |
| graphviz                      | https://graphviz.org/                                                               | https:/                                                                          |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https:/                                                                          |
| groupcache                    | https://github.com/golang/groupcache                                                | https:/                                                                          |
| grpc                          | https://google.golang.org/grpc                                                      | https:/                                                                          |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https:/                                                                          |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/                                                                          |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/                                                                          |
| gts                           | https://sourceforge.net/projects/gts/                                               | https:/                                                                          |
| h5py                          | https://www.h5py.org                                                                | https:/                                                                          |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https:/                                                                          |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https:/                                                                          |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/                                                                          |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/                                                                          |
| he                            | https://github.com/mathiasbynens/he                                                 | https:/                                                                          |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https:/                                                                          |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https:/                                                                          |
| htslib                        | https://www.htslib.org                                                              | https:/                                                                          |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https:/                                                                          |
| icu                           | https://github.com/unicode-org/icu                                                  | https:/                                                                          |
| idna                          | https://github.com/kjd/idna                                                         | https:/                                                                          |
| imageio                       | https://github.com/imageio/imageio                                                  | https:/                                                                          |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https:/                                                                          |
| ImmuneBuilder                 | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/                                                                          |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https:/                                                                          |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https:/                                                                          |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/                                                                          |
| inflection                    | https://github.com/jinzhu/inflection                                                | https:/                                                                          |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https:/                                                                          |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https:/                                                                          |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https:/                                                                          |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https:/                                                                          |
| ipykernel                     | https://ipython.org                                                                 | https:/                                                                          |
| ipython                       | https://ipython.org                                                                 | https:/                                                                          |
| ipython-genutils              | http://ipython.org                                                                  | https:/                                                                          |
| ipywidgets                    | http://jupyter.org                                                                  | https:/                                                                          |
| isodate                       | https://github.com/gweis/isodate/                                                   | https:/                                                                          |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https:/                                                                          |
| jax                           | https://github.com/google/jax                                                       | https:/                                                                          |
| jaxlib                        | https://github.com/google/jax                                                       | https:/                                                                          |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              | https:/                                                                          |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https:/                                                                          |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https:/                                                                          |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https:/                                                                          |
| jpeg                          | https://www.ijg.org                                                                 | https:/                                                                          |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https:/                                                                          |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https:/                                                                          |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https:/                                                                          |
| Name of Project               | Website                                                                             | License                                                                          |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https://github.com/jsonpickle/jsonpickle/blob/master/LICENSE                     |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https://github.com/stefankoegl/python-json-pointer/blob/master/LICENSE           |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https://github.com/python-jsonschema/jsonschema/blob/main/COPYING                |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/LICENSE |
| jstat                         | https://github.com/jstat/jstat                                                      | https://github.com/jstat/jstat/blob/master/LICENSE                               |
| jupyter-client                | https://jupyter.org                                                                 | https://github.com/jupyter/jupyter_client/blob/main/LICENSE                      |
| jupyter-core                  | https://jupyter.org                                                                 | https://github.com/jupyter/jupyter_core/blob/main/LICENSE                        |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https://github.com/jupyter/jupyter_events/blob/main/LICENSE                      |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https://github.com/jupyter-lsp/jupyterlab-lsp/blob/main/LICENSE                  |
| jupyter-server                | https://github.com/jupyter-server/jupyter_server                                    | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE               |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https://github.com/jupyterlab/jupyterlab/blob/main/LICENSE                       |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https://github.com/jupyterlab/pygments/blob/main/LICENSE                         |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https://github.com/jupyter-widgets/ipywidgets/blob/main/LICENSE                  |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https://github.com/jupyterlab/jupyterlab_server/blob/main/LICENSE                |
| jupyter_client                | http://jupyter.org                                                                  | https://github.com/jupyter/jupyter_client/blob/main/LICENSE                      |
| jupyter_core                  | http://jupyter.org                                                                  | https://github.com/jupyter/jupyter_core/blob/main/LICENSE                        |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE               |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https://github.com/jupyter-server/jupyter_server_terminals/blob/main/LICENSE     |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https://github.com/plotly/Kaleido/blob/main/LICENSE                              |
| keras                         | https://github.com/keras-team/keras                                                 | https://github.com/keras-team/keras/blob/master/LICENSE                          |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https://github.com/keras-team/keras-preprocessing/blob/master/LICENSE            |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https://github.com/keras-team/keras-tuner/blob/master/LICENSE                    |
| keyring                       | https://github.com/jaraco/keyring                                                   | https://github.com/jaraco/keyring/blob/main/LICENSE                              |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https://github.com/sassoftware/python-keyutils/blob/main/LICENSE                 |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https://github.com/scipy/kiwisolver/blob/master/LICENSE                          |
| kombu                         | https://kombu.readthedocs.io                                                        | https://github.com/celery/kombu/blob/master/LICENSE                              |
| krb5                          | https://web.mit.edu/kerberos/                                                       | https://web.mit.edu/kerberos/krb5-current/doc/mitK5license.html                  |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https://github.com/haifeng-jin/kt-legacy/blob/master/LICENSE                     |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https://github.com/scientific-python/lazy_loader/blob/main/LICENSE               |
| lcms2                         | https://www.littlecms.com                                                           | https://github.com/mm2/Little-CMS/blob/master/COPYING                            |
| lerc                          | https://github.com/Esri/lerc                                                        | https://github.com/Esri/lerc/blob/master/LICENSE                                 |
| libarchive                    | http://www.libarchive.org                                                           | https://github.com/libarchive/libarchive/blob/master/COPYING                     |
| libblas                       | https://www.netlib.org/blas/                                                        | https://www.netlib.org/blas/blasfaq.html                                         |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https://github.com/google/brotli/blob/master/LICENSE                             |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https://github.com/google/brotli/blob/master/LICENSE                             |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https://github.com/google/brotli/blob/master/LICENSE                             |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                              |
| libclang                      | https://github.com/llvm/llvm-project                                                | https://github.com/llvm/llvm-project/blob/main/clang/LICENSE.TXT                 |
| libcurl                       | https://curl.se/libcurl/                                                            | https://raw.githubusercontent.com/curl/curl/master/COPYING                       |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https://github.com/llvm-mirror/libcxx/blob/master/LICENSE.TXT                    |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https://download.oracle.com/otndocs/products/berkeleydb/html/license4.html       |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https://github.com/ebiggers/libdeflate/blob/master/COPYING                       |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://www.thrysoee.dk/editline/COPYING                                          |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https://software.schmorp.de/pkg/libev.html#license                               |
| libffi                        | https://github.com/libffi/libffi                                                    | https://raw.githubusercontent.com/libffi/libffi/master/LICENSE                   |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=COPYING  |
| libgd                         | https://libgd.github.io                                                             | https://raw.githubusercontent.com/libgd/libgd/master/COPYING                     |
| libglib                       | https://github.com/PolMine/libglib                                                  | https://github.com/PolMine/libglib/blob/master/COPYING                           |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https://www.gnu.org/licenses/lgpl-2.1.html                                       |
| Name of Project               | Website                                                                             | License                                                                          |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https://                                                                         |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https://                                                                         |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https://                                                                         |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https://                                                                         |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https://                                                                         |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                                         |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https://                                                                         |
| libopenblas                   | https://www.openblas.net/                                                           | https://                                                                         |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https://                                                                         |
| libpq                         | https://www.postgresql.org/                                                         | https://                                                                         |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https://                                                                         |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https://                                                                         |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https://                                                                         |
| libtiff                       | https://www.libtiff.org/                                                            | https://                                                                         |
| libtrust                      | https://github.com/docker/libtrust                                                  | https://                                                                         |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https://                                                                         |
| libuv                         | https://github.com/libuv/libuv                                                      | https://                                                                         |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https://                                                                         |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https://                                                                         |
| libxc                         | https://www.tddft.org/programs/libxc/                                               | https://                                                                         |
| libxcb                        | https://xcb.freedesktop.org                                                         | https://                                                                         |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https://                                                                         |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https://                                                                         |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https://                                                                         |
| zlib                          | https://zlib.net                                                                    | https://                                                                         |
| lime                          | https://github.com/marcotcr/lime                                                    | https://                                                                         |
| lit                           | http://llvm.org                                                                     | https://                                                                         |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https://                                                                         |
| llvmlite                      | http://llvmlite.readthedocs.io                                                      | https://                                                                         |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https://                                                                         |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https://                                                                         |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https://                                                                         |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https://                                                                         |
| lxml                          | https://lxml.de                                                                     | https://                                                                         |
| lz4-c                         | https://www.lz4.org/                                                                | https://                                                                         |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https://                                                                         |
| markdown-it-py                | Orion Floes                                                                         | https://                                                                         |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https://                                                                         |
| matplotlib                    | https://matplotlib.org                                                              | https://                                                                         |
| matplotlib-base               | https://matplotlib.org                                                              | https://                                                                         |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https://                                                                         |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https://                                                                         |
| mdtraj                        | https://www.mdtraj.org/                                                             | https://                                                                         |
| mdurl                         | Orion Floes                                                                         | https://                                                                         |
| menuinst                      | Orion Floes                                                                         | https://                                                                         |
| mergo                         | https://github.com/imdario/mergo                                                    | https://                                                                         |
| mistune                       | https://github.com/lepture/mistune                                                  | https://                                                                         |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https://                                                                         |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https://                                                                         |
| Name of Project               | Website                                                                             | License                                                                          |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https://                                                                         |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https://                                                                         |
| ml-dtypes                     | Orion Floes                                                                         | https://                                                                         |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https://                                                                         |
| moment                        | https://github.com/moment/moment                                                    | https://                                                                         |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https://                                                                         |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https://                                                                         |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https://                                                                         |
| mpmath                        | http://mpmath.org/                                                                  | https://                                                                         |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https://                                                                         |
| msgpack                       | https://msgpack.org/                                                                | https://                                                                         |
| multidict                     | https://github.com/aio-libs/multidict                                               | https://                                                                         |
| multierr                      | https://go.uber.org/multierr                                                        | https://                                                                         |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https://                                                                         |
| munkres                       | https://software.clapper.org/munkres/                                               | https://                                                                         |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https://                                                                         |
| namex                         | Orion Floes                                                                         | https://                                                                         |
| nbclassic                     | http://jupyter.org                                                                  | https://                                                                         |
| nbclient                      | https://jupyter.org                                                                 | https://                                                                         |
| nbconvert                     | https://jupyter.org                                                                 | https://                                                                         |
| nbformat                      | http://jupyter.org                                                                  | https://                                                                         |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https://                                                                         |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https://                                                                         |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                                         |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https://                                                                         |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https://                                                                         |
| networkx                      | https://networkx.org                                                                | https://                                                                         |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https://                                                                         |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https://                                                                         |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https://                                                                         |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https://                                                                         |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https://                                                                         |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https://                                                                         |
| nodejs                        | https://nodejs.org/en/                                                              | https://                                                                         |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https://                                                                         |
| notebook                      | http://jupyter.org                                                                  | https://                                                                         |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https://                                                                         |
| notebook_shim                 | http://jupyter.org                                                                  | https://                                                                         |
| numba                         | https://numba.pydata.org                                                            | https://                                                                         |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https://                                                                         |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https://                                                                         |
| numpy                         | https://numpy.org                                                                   | https://                                                                         |
| numpy-base                    | https://numpy.org                                                                   | https://                                                                         |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https://                                                                         |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://                                                                         |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://                                                                         |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https://                                                                         |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https://                                                                         |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https://                                                                         |
| Name of Project               | Website                                                                             | License                                                                          |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                          |
| Oat++                         | https://oatpp.io/                                                                   | https:/                                                                          |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https:/                                                                          |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https:/                                                                          |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/                                                                          |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https:/                                                                          |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/                                                                          |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/                                                                          |
| OpenFF                        | https://openforcefield.org/                                                         | https:/                                                                          |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/                                                                          |
| openff-forcefields            | https://openforcefield.org                                                          | https:/                                                                          |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https:/                                                                          |
| openff-models                 | https://github.com/openforcefield/openff-models                                     | https:/                                                                          |
| openff-toolkit                | https://openforcefield.org                                                          | https:/                                                                          |
| openff-toolkit-base           | https://openforcefield.org                                                          | https:/                                                                          |
| openff-units                  | https://github.com/openforcefield/openff-units                                      | https:/                                                                          |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https:/                                                                          |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https:/                                                                          |
| openldap                      | https://www.openldap.org/software/repo.html                                         | https:/                                                                          |
| OpenMM                        | https://openmm.org                                                                  | https:/                                                                          |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https:/                                                                          |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https:/                                                                          |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                                                          |
| openssl                       | https://www.openssl.org                                                             | https:/                                                                          |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https:/                                                                          |
| OptKing                       | https://github.com/psi-rking/optking                                                | https:/                                                                          |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https:/                                                                          |
| overrides                     | https://github.com/mkorpela/overrides                                               | https:/                                                                          |
| packaging                     | https://github.com/pypa/packaging                                                   | https:/                                                                          |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                                                          |
| pandas                        | https://pandas.pydata.org                                                           | https:/                                                                          |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https:/                                                                          |
| Name of Project               | Website                                                                             | License                                                                          |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https:/                                                                          |
| pango                         | https://pango.gnome.org                                                             | https:/                                                                          |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https:/                                                                          |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                                          |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https:/                                                                          |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https:/                                                                          |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https:/                                                                          |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https:/                                                                          |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https:/                                                                          |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/                                                                          |
| pcre                          | https://www.pcre.org                                                                | https:/                                                                          |
| pcre2                         | https://www.pcre.org                                                                | https:/                                                                          |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https:/                                                                          |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https:/                                                                          |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https:/                                                                          |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https:/                                                                          |
| pgio                          | https://github.com/jackc/pgio                                                       | https:/                                                                          |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https:/                                                                          |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https:/                                                                          |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https:/                                                                          |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https:/                                                                          |
| phonopy                       | https://github.com/phonopy/phonopy                                                  | https:/                                                                          |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https:/                                                                          |
| Pillow                        | https://python-pillow.org                                                           | https:/                                                                          |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https:/                                                                          |
| pip                           | https://pip.pypa.io/                                                                | https:/                                                                          |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https:/                                                                          |
| pixman                        | https://pixman.org                                                                  | https:/                                                                          |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https:/                                                                          |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https:/                                                                          |
| plotly                        | https://plotly.com/python/                                                          | https:/                                                                          |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https:/                                                                          |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https:/                                                                          |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/                                                                          |
| pooch                         | https://github.com/fatiando/pooch                                                   | https:/                                                                          |
| pox                           | https://github.com/uqfoundation/pox                                                 | https:/                                                                          |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https:/                                                                          |
| pq                            | https://github.com/lib/pq                                                           | https:/                                                                          |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https:/                                                                          |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https:/                                                                          |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/                                                                          |
| protobuf                      | https://google.golang.org/protobuf                                                  | https:/                                                                          |
| psi4                          | https://psicode.org                                                                 | https:/                                                                          |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https:/                                                                          |
| psycopg2                      | https://psycopg.org/                                                                | https:/                                                                          |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https:/                                                                          |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https:/                                                                          |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/                                                                          |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http://                                                                          |
| Name of Project               | Website                                                                             | License                                                                          |
| py                            | https://py.readthedocs.io/en/latest/                                                | MIT                                                                              |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             | MIT                                                                              |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   | BSD-2-Clause                                                                     |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           | BSD-2-Clause                                                                     |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  | BSD-3-Clause                                                                     |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 | LGPL-2.1-or-later                                                                |
| pycosat                       | https://github.com/conda/pycosat                                                    | MIT                                                                              |
| pycparser                     | https://github.com/eliben/pycparser                                                 | BSD-3-Clause                                                                     |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 | MIT                                                                              |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           | MIT                                                                              |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                | LGPL-3.0-or-later                                                                |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                | LGPL-3.0-or-later                                                                |
| Pygments                      | https://pygments.org                                                                | BSD-2-Clause                                                                     |
| pygraphviz                    | https://pygraphviz.github.io                                                        | BSD-3-Clause                                                                     |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            | LGPL-2.1-or-later                                                                |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        | Apache-2.0                                                                       |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  | Apache-2.0                                                                       |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   | MIT                                                                              |
| pymbar                        | https://pymbar.org                                                                  | MIT                                                                              |
| pyOpenSSL                     | https://pyopenssl.org/                                                              | Apache-2.0                                                                       |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    | MIT                                                                              |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    | BSD-3-Clause                                                                     |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 | MIT                                                                              |
| pysam                         | https://github.com/pysam-developers/pysam                                           | MIT                                                                              |
| PySocks                       | https://github.com/Anorov/PySocks                                                   | BSD-3-Clause                                                                     |
| pytables                      | https://www.pytables.org                                                            | BSD-3-Clause                                                                     |
| python                        | https://www.python.org/                                                             | Python-2.0                                                                       |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          | LGPL-3.0-or-later                                                                |
| python-constraint             | https://github.com/python-constraint/python-constraint                              | BSD-3-Clause                                                                     |
| python-dateutil               | https://dateutil.readthedocs.io                                                     | BSD-3-Clause                                                                     |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         | BSD-3-Clause                                                                     |
| python-ldap                   | https://www.python-ldap.org/                                                        | Python-2.0                                                                       |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            | MIT                                                                              |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 | BSD-3-Clause                                                                     |
| pytz                          | https://pythonhosted.org/pytz                                                       | MIT                                                                              |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   | MIT                                                                              |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  | MIT                                                                              |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                 | MIT                                                                              |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             | LGPL-3.0-or-later                                                                |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               | BSD-3-Clause                                                                     |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  | BSD-3-Clause                                                                     |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        | BSD-3-Clause                                                                     |
| ramda                         | https://github.com/ramda/ramda                                                      | MIT                                                                              |
| rapidjson                     | https://rapidjson.org/                                                              | MIT                                                                              |
| rdkit                         | https://www.rdkit.org                                                               | BSD-3-Clause                                                                     |
| re2                           | https://github.com/google/re2                                                       | BSD-3-Clause                                                                     |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             | Apache-2.0                                                                       |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             | MIT                                                                              |
| Name of Project               | Website                                                                             | License                                                                          |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https:/                                                                          |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https:/                                                                          |
| reportlab                     | https://www.reportlab.com                                                           | https:/                                                                          |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                                          |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                                          |
| requests                      | https://requests.readthedocs.io                                                     | https:/                                                                          |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https:/                                                                          |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https:/                                                                          |
| resumable                     | https://github.com/stevvooe/resumable                                               | https:/                                                                          |
| retrying                      | https://github.com/rholder/retrying                                                 | https:/                                                                          |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https:/                                                                          |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https:/                                                                          |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https:/                                                                          |
| rich                          | <b>Orion Floes</b>                                                                  | https:/                                                                          |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https:/                                                                          |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https:/                                                                          |
| rsa                           | https://stuvel.eu/rsa                                                               | https:/                                                                          |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/                                                                          |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/                                                                          |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https:/                                                                          |
| sasl                          | https://mellium.im/sasl                                                             | https:/                                                                          |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https:/                                                                          |
| scikit-image                  | https://scikit-image.org                                                            | https:/                                                                          |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https:/                                                                          |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/                                                                          |
| scipy                         | https://scipy.org                                                                   | https:/                                                                          |
| seaborn                       | https://seaborn.pydata.org                                                          | https:/                                                                          |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https:/                                                                          |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https:/                                                                          |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https:/                                                                          |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https:/                                                                          |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https:/                                                                          |
| sh                            | https://github.com/amoffat/sh                                                       | https:/                                                                          |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https:/                                                                          |
| simint                        | https://www.bennyp.org/research/simint/                                             | https:/                                                                          |
| six                           | https://github.com/benjaminp/six                                                    | https:/                                                                          |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https:/                                                                          |
| snappy                        | https://github.com/google/snappy                                                    | https:/                                                                          |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https:/                                                                          |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https:/                                                                          |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https:/                                                                          |
| spglib                        | <b>Orion Floes</b>                                                                  | https:/                                                                          |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https:/                                                                          |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/                                                                          |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/                                                                          |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/                                                                          |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/                                                                          |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/                                                                          |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/                                                                          |
| Name of Project               | Website                                                                             | License                                                                          |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          | https://                                                                         |
| sqlite                        | https://sqlite.org/index.html                                                       | https://                                                                         |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            | https://                                                                         |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             | https://                                                                         |
| starfile                      | https://github.com/alisterburt/starfile                                             | https://                                                                         |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          | https://                                                                         |
| structlog                     | https://www.structlog.org/                                                          | https://                                                                         |
| svglib                        | https://github.com/deeplook/svglib                                                  | https://                                                                         |
| sympy                         | https://sympy.org                                                                   | https://                                                                         |
| tables                        | https://www.pytables.org/                                                           | https://                                                                         |
| tabulate                      | https://github.com/astanin/python-tabulate                                          | https://                                                                         |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                | https://                                                                         |
| tenacity                      | https://github.com/jd/tenacity                                                      | https://                                                                         |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           | https://                                                                         |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           | https://                                                                         |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           | https://                                                                         |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            | https://                                                                         |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             | https://                                                                         |
| tensorflow-io-gcs-filesystem  | Orion Floes                                                                         | https://                                                                         |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           | https://                                                                         |
| termcolor                     | https://github.com/hugovk/termcolor                                                 | https://                                                                         |
| terminado                     | https://github.com/jupyter/terminado                                                | https://                                                                         |
| testpath                      | https://github.com/jupyter/testpath                                                 | https://                                                                         |
| textangular                   | https://github.com/fraywing/textAngular                                             | https://                                                                         |
| tf_keras                      | Orion Floes                                                                         | https://                                                                         |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             | https://                                                                         |
| three                         | https://github.com/mrdoob/three.js                                                  | https://                                                                         |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                | https://                                                                         |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  | https://                                                                         |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             | https://                                                                         |
| tk                            | https://www.tcl.tk/                                                                 | https://                                                                         |
| toml                          | https://github.com/toml-lang/toml                                                   | https://                                                                         |
| tomli                         | https://github.com/hukkin/tomli                                                     | https://                                                                         |
| toolz                         | https://github.com/pytoolz/toolz                                                    | https://                                                                         |
| torch                         | https://pytorch.org/                                                                | https://                                                                         |
| tornado                       | https://www.tornadoweb.org                                                          | https://                                                                         |
| tqdm                          | https://github.com/tqdm/tqdm                                                        | https://                                                                         |
| tracy                         | https://github.com/gear-genomics/tracy                                              | https://                                                                         |
| traitlets                     | https://github.com/ipython/traitlets                                                | https://                                                                         |
| triton                        | https://github.com/openai/triton/                                                   | https://                                                                         |
| truststore                    | Orion Floes                                                                         | https://                                                                         |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               | https://                                                                         |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             | https://                                                                         |
| twine                         | https://github.com/pypa/twine                                                       | https://                                                                         |
| twinj uuid                    | https://github.com/twinj/uuid                                                       | https://                                                                         |
| types                         | https://github.com/babel/babel                                                      | https://                                                                         |
| typescript                    | https://github.com/Microsoft/TypeScript                                             | https://                                                                         |
| typing_extensions             | https://github.com/python/typing                                                    | https://                                                                         |
| tzdata                        | https://github.com/python/tzdata                                                    | https://                                                                         |
| Name of Project               | Website                                                                             | License                                                                          |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | https:/                                                                          |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | https:/                                                                          |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | https:/                                                                          |
| uritools                      | https://github.com/tkem/uritools/                                                   | https:/                                                                          |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | https:/                                                                          |
| vine                          | https://github.com/celery/vine                                                      | https:/                                                                          |
| vue                           | https://github.com/vuejs/vue                                                        | https:/                                                                          |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | https:/                                                                          |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | https:/                                                                          |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | https:/                                                                          |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | https:/                                                                          |
| westpa                        | Orion Floes                                                                         | http://                                                                          |
| wheel                         | https://github.com/pypa/wheel                                                       | https:/                                                                          |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | https:/                                                                          |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | https:/                                                                          |
| wsutil                        | https://github.com/yhat/wsutil                                                      | https:/                                                                          |
| x/lint                        | https://golang.org/x/lint                                                           | https:/                                                                          |
| x/mod                         | https://golang.org/x/mod/semver                                                     | https:/                                                                          |
| x/net                         | https://golang.org/x/net                                                            | https:/                                                                          |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | https:/                                                                          |
| x/sys                         | https://golang.org/x/sys                                                            | https:/                                                                          |
| x/text                        | https://golang.org/x/text                                                           | https:/                                                                          |
| x/tools                       | https://golang.org/x/tools                                                          | https:/                                                                          |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | https:/                                                                          |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                               | https:/                                                                          |
| xlrd                          | https://github.com/python-excel/xlrd                                                | https:/                                                                          |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | https:/                                                                          |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | https:/                                                                          |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https:/                                                                          |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https:/                                                                          |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https:/                                                                          |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https:/                                                                          |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https:/                                                                          |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https:/                                                                          |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https:/                                                                          |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https:/                                                                          |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https:/                                                                          |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https:/                                                                          |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https:/                                                                          |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https:/                                                                          |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | https:/                                                                          |
| xz                            | https://github.com/ulikunitz/xz                                                     | https:/                                                                          |
| yaml                          | https://pyyaml.org/                                                                 | https:/                                                                          |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  | https:/                                                                          |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | https:/                                                                          |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | https:/                                                                          |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | https:/                                                                          |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | https:/                                                                          |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | comm                                                                             |
| Name of Project               | Website                                                                             | License                                                                          |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                                                                              |
| zap                           | https://go.uber.org/zap                                                             | https:/                                                                          |
| zipp                          | https://github.com/jaraco/zipp                                                      | https:/                                                                          |
| zlib                          | https://zlib.net/                                                                   | https:/                                                                          |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https:/                                                                          |
| zstd                          | https://facebook.github.io/zstd/                                                    | https:/                                                                          |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:/                                                                          |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:/                                                                          |

## **9.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses GNU Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

## 9.1.1 GCC RUNTIME LIBRARY EXCEPTION

```
Version 3.1, 31 March 2009
Copyright © 2009 Free Software Foundation, Inc. http://fsf.org/
Everyone is permitted to copy and distribute verbatim copies of this license document,
\rightarrow but changing it is not allowed.
This GCC Runtime Library Exception ("Exception") is an additional permission under.
\rightarrow section 7 of the GNU General Public License,
version 3 ("GPLv3"). It applies to a given file (the "Runtime Library") that bears a
→notice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise  $\rightarrow$ based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

## 9.1.2 GNU GENERAL PUBLIC LICENSE

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

License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. 14. Revised Versions of this License. The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. 15. Disclaimer of Warranty. THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 16. Limitation of Liability. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),

17. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided

EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF

(continues on next page)

SUCH DAMAGES.

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page) 9.1. GCC

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

#### See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# A

AddConstMol OEMedChem:: OEMCSFragDatabase, 79 AddIndexedMol OEMedChem:: OECreateMMPIndexStatus,  $77$ AddMatchedPair OEMedChem:: OEMatchedPairTransform, 100 AddMol OEMedChem:: OEMatchedPairAnalyzer, 92 OEMedChem:: OEMCSFraqDatabase, 79 AddSDData OEMedChem:: OEMatchedPair, 98 AddUnindexedMol OEMedChem:: OECreateMMPIndexStatus, 77

# <sub>B</sub>

bemismurckoperception.py Example Code, 12

# C

```
chemblsolubility.py
   Example Code, 15
ClearIndexableFragmentRange
   affluesablerragmenters...<br>OEMedChem::OEMatchedPairAnalyzerOptions, createmmpindex.py
       95
   OEMedChem:: OEMCSFragDatabaseOptions,
       85
ClearIndexedMols
   OEMedChem:: OEMCSFraqDatabase, 80
ClearSDData
   OEMedChem:: OEMatchedPair, 98
Constructors
   OEMedChem:: OEBemisMurckoOptions, 73
   OEMedChem:: OECreateMMPIndexOptions,
       75
   OEMedChem:: OECreateMMPIndexStatus.
       77
   OEMedChem:: OEMatchedPair, 97
   OEMedChem:: OEMatchedPairAnalyzer, 92
```

OEMedChem:: OEMatchedPairAnalyzerOptions,  $Q\Delta$ OEMedChem:: OEMatchedPairTransform, 100 OEMedChem:: OEMatchedPairTransformExtractOptions 103 OEMedChem:: OEMCSFraqDatabase, 79 OEMedChem:: OEMCSFragDatabaseOptions, 84 OEMedChem:: OEMCSMolSimScore, 87 OEMedChem:: OEMCSSimFuncBase. 89 OEMedChem:: OEMCSTanimotoSim, 90 OEMedChem:: OEMCSTverskySim, 91 CoreToMoleculeCount OEMedChem:: OEMCSFraqDatabase, 80 CoreToMolecules OEMedChem:: OEMCSFragDatabase, 80 CreateCopy OEMedChem:: OEBemisMurckoOptions, 73 OEMedChem:: OEMatchedPair, 98 OEMedChem::OEMatchedPairTransform.  $101$ OEMedChem:: OEMCSSimFuncBase. 89 OEMedChem:: OEMCSTanimotoSim, 90 OEMedChem:: OEMCSTverskySim, 91 createmcsfragdatabase.py Example Code, 59 Example Code, 19 createmmpindexparallel.py Example Code, 26 createmmpindexthreaded.py Example Code, 40

## F

```
Example Code
   bemismurckoperception.py, 12
   chemblsolubility.py.15
   createmcsfragdatabase.py, 59
   createmmpindex.py, 19
   createmmpindexparallel.py, 26
   createmmpindexthreaded.py, 40
```

```
matchedpairtransform.py.45
                                          GetMatchedPairData
   matchedpairtransformlist.py, 49
                                              OEMedChem:: OEMatchedPairTransformExtractOptions
   matchedpairtransformprobe.py, 54
                                                 105
   mcsfragdatabase.py, 64
                                          GetMatchedPairs
   mcsfragoccurrence.py, 68
                                              OEMedChem:: OEMatchedPairTransform,
   oemedcheminfo.py, 72
                                                 101
                                              OEMedChem:: OEMatchedPairTransformExtractOptions
F
                                                 105
                                          GetMaxAtomFilter
FromIndex
   OEMedChem:: OEMatchedPair, 98
                                              OEMedChem:: OEMatchedPairAnalyzerOptions,
                                                 96
FromSmiles
                                              OEMedChem:: OEMCSFragDatabaseOptions,
   OEMedChem:: OEMatchedPair, 98
                                                 85
G
                                          GetMaxCoreMolecule
                                              OEMedChem:: OEMCSFragDatabase, 80
GetAlpha
                                          GetMaxCoreMoleculeCount
   OEMedChem:: OEMCSTverskySim, 91
                                              OEMedChem:: OEMCSFragDatabase, 80
GetAttachmentPoints
   OEMedChem::OEMatchedPairTransformExtrattMaxEGagLimit
                                              OEMedChem:: OEMCSFragDatabaseOptions,
       10485
GetBeta
                                          GetMaxMMPLimit
   OEMedChem:: OEMCSTverskySim, 91
                                              OEMedChem::OEMatchedPairTransformExtractOptions
GetContext
   OEMedChem::OEMatchedPairTransformExtractOptions,
                                          GetMaxMolIdx
       104
                                              OEMedChem:: OEMatchedPairAnalyzer, 92
GetDataTags
                                              OEMedChem:: OEMCSFragDatabase, 80
   OEMedChem:: OEMatchedPair, 99
                                          GetMaxRecord
GetDirection
   OEMedChem::OEMatchedPairTransformExtract0BMqgGgem::OECreateMMPIndexOptions,
                                                 75
       104
                                          GetMaxSubstituentLimit
GetFragmentationLimit
   OEMedChem::OEMatchedPairAnalyzerOptions, OEMedChem::OEMatchedPairTransformExtractOptions
                                                  105
      95
   OEMedChem:: OEMCSFragDatabaseOptions, GetMaxSubstituentLimitSkip
                                              OEMedChem:: OEMatchedPairTransformExtractOptions
       85
                                                 105
GetFromSDData
                                          GetMCSCore
   OEMedChem:: OEMatchedPair, 99
                                              OEMedChem:: OEMCSMolSimScore, 88
GetIdx
                                          GetMCSCorrespondence
   OEMedChem:: OEMCSMolSimScore, 88
                                              OEMedChem::OEMatchedPairTransformExtractOptions
GetIndexableFragmentRangeMax
                                                  104
   OEMedChem:: OEMatchedPairAnalyzerOptions,
                                          GetMCSSimTypeString
       95
                                              OEMedChem:: OEMCSSimFuncBase, 89
   OEMedChem:: OEMCSFraqDatabaseOptions,
                                              OEMedChem:: OEMCSTanimotoSim, 90
       85
                                              OEMedChem:: OEMCSTverskySim, 92
GetIndexableFragmentRangeMin
   OEMedChem:: OEMatchedPairAnalyzerOptionstMinFragLimit
                                              OEMedChem:: OEMCSFragDatabaseOptions,
       95
                                                 86
   OEMedChem:: OEMCSFragDatabaseOptions,
                                          GetMinMMPLimit
       85
                                              OEMedChem:: OEMatchedPairTransformExtractOptions
GetIsotopes
   OEMedChem::OEMatchedPairTransformExtractOpti<sup>10</sup>As,
                                          GetMinSubstituentLimit
       104
                                              OEMedChem:: OEMatchedPairTransformExtractOptions
GetMatchedPairContext
                                                 106
   OEMedChem:: OEMatchedPairTransform,
                                          GetMMPOptions
       101
```

OEMedChem::OECreateMMPIndexOptions, OEMedChem:: OECreateMMPIndexStatus, 75 78 GetMolecule GetTransform OEMedChem:: OEMatchedPairAnalyzer, 93 OEMedChem:: OEMatchedPairTransform, OEMedChem:: OEMatchedPairTransform,  $102$ 101 GetUnindexedMols GetMoleculeTitle OEMedChem:: OECreateMMPIndexStatus. OEMedChem:: OEMatchedPairTransform, 78 101 GetUnsaturatedHeteroBonds GetNumMatchedPairs OEMedChem:: OEBemisMurckoOptions, 74 OEMedChem:: OECreateMMPIndexStatus, GetVerbose 77 OEMedChem::OECreateMMPIndexOptions, GetNumMols 76 OEMedChem:: OECreateMMPIndexStatus, H 78 GetNumThreads HasIndexableFragmentHeavyAtomRange OEMedChem:: OECreateMMPIndexOptions, OEMedChem:: OEMatchedPairAnalyzerOptions, 75 96 GetOptions OEMedChem:: OEMCSFragDatabaseOptions, OEMedChem:: OEMatchedPairAnalyzer, 93 86 OEMedChem::OEMatchedPairAnalyzerOptionssMatchedPair 96 OEMedChem:: OEMatchedPairTransform, OEMedChem:: OEMatchedPairTransformExtractOpti02s, 106 HasSDData OEMedChem:: OEMCSFraqDatabase, 81 OEMedChem:: OEMatchedPair, 99 OEMedChem:: OEMCSFragDatabaseOptions, 86 GetProcessorID Invert OEMedChem:: OEMatchedPairAnalyzer, 93 OEMedChem:: OEMatchedPairTransform. GetProcessorType  $102$ OEMedChem:: OEMatchedPairAnalyzer, 93 IsIndexed OEMedChem:: OEMatchedPairAnalyzerOptions, OEMedChem:: OEMatchedPairAnalyzer, 93 96 OEMedChem:: OEMCSFragDatabase, 82 GetRegionType M OEMedChem:: OEBemisMurckoOptions, 73 GetRingFragLimit matchedpairtransform.py OEMedChem:: OEMCSFraqDatabaseOptions, Example Code, 45 86 matchedpairtransformlist.py GetScore Example Code, 49 OEMedChem:: OEMCSMolSimScore, 88 matchedpairtransformprobe.py GetScores Example Code, 54 OEMedChem:: OEMCSFragDatabase, 81 mcsfragdatabase.py GetSDData Example Code, 64 OEMedChem:: OEMatchedPair, 99 mcsfragoccurrence.py GetSMARTS Example Code, 68 OEMedChem::OEMatchedPairTransformExtnaGdpptdpPsons 106 OEMedChem:: OEMatchedPairAnalyzer, 94 GetSortedScores OEMedChem:: OEMatchedPairAnalyzerOptions, OEMedChem:: OEMCSFragDatabase, 81 96 GetSubstituentSearch MoleculeToCores OEMedChem:: OEBemisMurckoOptions, 73 OEMedChem:: OEMCSFragDatabase, 83 GetToSDData N OEMedChem:: OEMatchedPair, 99 GetTotalMols NumDataTags

OEMedChem:: OEMatchedPair, 99 GetUnindexedMols, 78 operator+,77 NumFragments OEMedChem:: OEMCSFraqDatabase, 83 operator=, 77 SetNumMatchedPairs, 78 NumIndexNodes OEMedChem:: OEMatchedPairAnalyzer, 94 SetNumMols, 78 SetUnindexedMols, 78 NumMatchedPairs OEMedChem:: OEMatchedPairAnalyzer, 94 SetValid.78 OEMedChem:: OEMatchedPairTransform, OEMedChem::OEDetermineConnectiveComplexity, 102 132 NumMols OEMedChem::OEDetermineElementalComplexity, OEMedChem:: OEMatchedPairAnalyzer, 94 132 OEMedChem:: OEMCSFragDatabase, 83 OEMedChem:: OEDetermineMolecularComplexity, 132  $\Omega$ OEMedChem::OEDetermineRingComplexity, OEMedChem:: OEApplyChEMBL18SolubilityTransforms, 132 OEMedChem:: OEDetermineStereoComplexity, 128 OEMedChem:: OEApplyChEMBL24SolubilityTransforms, 133 OEMedChem::OEDetermineSymmetryComplexity, 128 133 OEMedChem:: OEBemisMurckoOptions, 73 OEMedChem:: OEGetBemisMurcko, 133 Constructors, 73 OEMedChem:: OEGetFuncGroupFragments, 134 CreateCopy, 73 OEMedChem:: OEGetMatchedMolecularPairs, GetRegionType, 73 134 GetSubstituentSearch, 73 OEMedChem::OEGetMatchedPairAnalyzerFileType, GetUnsaturatedHeteroBonds, 74 135 SetRegionType, 74 OEMedChem:: OEGetRegionType, 136 SetSubstituentSearch.74 OEMedChem:: OEGetRegionTypeName, 136 SetUnsaturatedHeteroBonds, 74 OEMedChem:: OEGetRingChainFragments, 136 Validate, 74 OEMedChem:: OEGetRingLinkerSideChainFragments, OEMedChem::OECalculateComboBelief, 130 136 OEMedChem:: OECalculateETComboBelief, 130 OEMedChem::OEConfigureMatchedPairIndexOp@EMggChem::OEGetRingValue, 138 OEMedChem:: OEIsMatchedPairAnalvzerFileType, 130 138 OEMedChem::OEConfigureMCSFragDatabaseOptions, OEMedChem:: OEIsMCSFragDatabaseFileType, 130 139 OEMedChem:: OECreateIDString, 131 OEMedChem::OEIsReadableMatchedPairAnalyzer, OEMedChem:: OECreateIDStrings, 131 139 OEMedChem:: OECreateMMPIndexFile, 131 OEMedChem::OEIsWriteableMatchedPairAnalyzer, OEMedChem:: OECreateMMPIndexOptions, 74 139 Constructors, 75 OEMedChem:: OEMatchedPair, 97 GetMaxRecord, 75 AddSDData, 98 GetMMPOptions, 75 ClearSDData. 98 GetNumThreads, 75 Constructors. 97 GetVerbose, 76 CreateCopy, 98 SetMaxRecord, 76 FromIndex, 98 SetNumThreads, 76 FromSmiles, 98 SetTracer.76 GetDataTags, 99 SetVerbose, 76 GetFromSDData, 99 OEMedChem:: OECreateMMPIndexStatus, 76 GetSDData, 99 AddIndexedMol, 77 GetToSDData, 99 AddUnindexedMol, 77 HasSDData, 99 Constructors.77 NumDataTags, 99 GetNumMatchedPairs, 77 operator=, 98 GetNumMols.78 ToIndex, 100 GetTotalMols, 78

ToSmiles. 100 OEMedChem:: OEMatchedPairContext:: Default, OEMedChem:: OEMatchedPairAnalyzer, 92 115 OEMedChem::OEMatchedPairContext::Undefined, AddMol, 92 Constructors, 92 115 GetMaxMolIdx, 92 OEMedChem:: OEMatchedPairContextName, 140 GetMolecule, 93 OEMedChem:: OEMatchedPairContextType, 140 GetOptions, 93 OEMedChem:: OEMatchedPairGetTransforms, GetProcessorID, 93 140 GetProcessorType, 93 OEMedChem:: OEMatchedPairIndexSetup, 115 IsIndexed, 93 OEMedChem:: OEMatchedPairIndexSetup:: All, ModifyOptions, 94 116 NumIndexNodes, 94 OEMedChem::OEMatchedPairIndexSetup::BondFraqLimit, NumMatchedPairs, 94 116 NumMols, 94 OEMedChem::OEMatchedPairIndexSetup::FragmentationC OEMedChem::OEMatchedPairAnalyzerFileType, 117 114 OEMedChem::OEMatchedPairIndexSetup::FragMinMaxRang OEMedChem::OEMatchedPairAnalyzerFileType::MCSFrblogs, OEMedChem::OEMatchedPairIndexSetup::HeavyAtomLimit. 114 OEMedChem::OEMatchedPairAnalyzerFileType::MMPInbl&x, 114 OEMedChem::OEMatchedPairIndexSetup::IndexHydrogenS OEMedChem::OEMatchedPairAnalyzerFileType::UNDEFIM&ED, OEMedChem:: OEMatchedPairIndexSetup:: IndexHydrogenS 114 OEMedChem:: OEMatchedPairAnalyzerOptions, 118 94 OEMedChem::OEMatchedPairIndexSetup::ProcessorType, ClearIndexableFragmentRange, 95 119 Constructors, 94 OEMedChem::OEMatchedPairIndexSetup::UniquesOnly, GetFragmentationLimit, 95 119 GetIndexableFragmentRangeMax, 95 OEMedChem:: OEMatchedPairIndexStatus, 119 GetIndexableFragmentRangeMin, 95 OEMedChem::OEMatchedPairIndexStatus::BinaryIOError, GetMaxAtomFilter, 96 120 GetOptions, 96 OEMedChem::OEMatchedPairIndexStatus::CopyMolError, GetProcessorType, 96 120 HasIndexableFragmentHeavyAtomRange, OEMedChem::OEMatchedPairIndexStatus::Deactivated. 96 120 ModifyOptions, 96 OEMedChem::OEMatchedPairIndexStatus::DuplicateReco operator=, 95 120 SetFragmentationLimit, 96 OEMedChem::OEMatchedPairIndexStatus::DuplicateStru SetIndexableFragmentRange, 97  $120$ SetMaxAtomFilter, 97 OEMedChem:: OEMatchedPairIndexStatus:: Fragmentation SetOptions, 97 120 OEMedChem::OEMatchedPairIndexStatus::FragmentRangel SetProcessorType, 97 OEMedChem:: OEMatchedPairApplyTransforms, 120 139 OEMedChem::OEMatchedPairIndexStatus::HeavyAtomFilt OEMedChem:: OEMatchedPairContext, 114 121 OEMedChem::OEMatchedPairContext::AllBond@EMedChem::OEMatchedPairIndexStatus::IncompatibleO 115 121 OEMedChem::OEMatchedPairContext::Bond0, OEMedChem::OEMatchedPairIndexStatus::NoError, 115 121 OEMedChem::OEMatchedPairContext::Bond1, OEMedChem::OEMatchedPairIndexStatus::NoFragmentati 115 121 OEMedChem::OEMatchedPairContext::Bond2, OEMedChem::OEMatchedPairIndexStatus::NoStructure, 115 121 OEMedChem::OEMatchedPairContext::Bond3, OEMedChem::OEMatchedPairIndexStatus::ProcessorErro 115 121

OEMedChem::OEMatchedPairIndexStatus::ProOBMedChente@EMatchedPairProcessorName, 142. 122 OEMedChem::OEMatchedPairIndexStatus::Uns@EMedChem::OEMatchedPairProcessorType, 122 142 OEMedChem::OEMatchedPairIndexStatusName, OEMedChem::OEMatchedPairTransform, 100 141 AddMatchedPair, 100 OEMedChem::OEMatchedPairIndexStatusType, Constructors, 100 142 CreateCopy, 101 GetMatchedPairContext, 101 OEMedChem:: OEMatchedPairOptions, 122 OEMedChem::OEMatchedPairOptions::AllCuts, GetMatchedPairs, 101 122 GetMolecule, 101 OEMedChem::OEMatchedPairOptions::ComboCuts, GetMoleculeTitle, 101 122 GetTransform, 102 OEMedChem::OEMatchedPairOptions::Default, HasMatchedPair, 102 122 Invert, 102 OEMedChem::OEMatchedPairOptions::DefaultFraqNImmMaxtchedPairs, 102  $122.$ operator=, 100 OEMedChem::OEMatchedPairOptions::DoubleCuts,SetMoleculeTitle, 103 123 SetTransform, 103 OEMedChem::OEMatchedPairOptions::ExportCOMMedGhemm:OEMatchedPairTransformExtractMode, 123 125 OEMedChem::OEMatchedPairOptions::ExportHMBMedChem::OEMatchedPairTransformExtractMode::AddAt 123 125 OEMedChem::OEMatchedPairOptions::IndexHS@EM@dChem,:OEMatchedPairTransformExtractMode::AddM 123 126 OEMedChem::OEMatchedPairOptions::IndexHS@EMedChem::OEMatchedPairTransformExtractMode::Back 123 126 OEMedChem::OEMatchedPairOptions::SingleCOEMedChem::OEMatchedPairTransformExtractMode::Defa 123 125 OEMedChem::OEMatchedPairOptions::TripleCOEMedChem::OEMatchedPairTransformExtractMode::Forw 124 126 OEMedChem::OEMatchedPairOptions::UniquesOEMgdChem::OEMatchedPairTransformExtractMode::NoIs 124 126 OEMedChem::OEMatchedPairOptions::ValidAlOEM@pChem::OEMatchedPairTransformExtractMode::NoMat 124 126 OEMedChem::OEMatchedPairOptions::ValidFr@EMed@k@mt\$OEMatchedPairTransformExtractMode::NoMat 124 126 OEMedChem::OEMatchedPairOptions::ValidIndEM@pChem::OEMatchedPairTransformExtractMode::NoSM 124 126 OEMedChem::OEMatchedPairOptions::ValidOpOEMedChem::OEMatchedPairTransformExtractMode::Sort 124 126 OEMedChem::OEMatchedPairOptionsName, 142 OEMedChem::OEMatchedPairTransformExtractMode::Subst OEMedChem:: OEMatchedPairOptionsType, 142 127 OEMedChem::OEMatchedPairProcessor, 124 OEMedChem::OEMatchedPairTransformExtractMode::Supp: OEMedChem:: OEMatchedPairProcessor:: BemisMurcko, 127 125 OEMedChem::OEMatchedPairTransformExtractMode::Unspe OEMedChem::OEMatchedPairProcessor::Custom, 125 125 OEMedChem::OEMatchedPairTransformExtractOptions, OEMedChem:: OEMatchedPairProcessor:: Default, 103 125 Constructors, 103 OEMedChem:: OEMatchedPairProcessor:: HussainRestAttachmentPoints, 104 125 GetContext, 104 OEMedChem::OEMatchedPairProcessor::UndefineGetDirection, 104 124 GetIsotopes, 104

GetMatchedPairData, 105 GetMatchedPairs, 105 GetMaxMMPLimit, 105 GetMaxSubstituentLimit, 105 GetMaxSubstituentLimitSkip, 105 GetMCSCorrespondence, 104 GetMinMMPLimit. 106 GetMinSubstituentLimit, 106 GetOptions, 106 GetSMARTS, 106 operator=, 103 SetAttachmentPoints, 106 SetContext, 107 SetDirection, 107 SetIsotopes, 107 SetMatchedPairData, 107 SetMatchedPairs, 108 SetMaxSubstituentLimitSkip, 108 SetMCSCorrespondence, 107 SetMMPLimit, 108 SetOptions, 108 SetSMARTS, 109 SetSubstituentLimit, 108 OEMedChem:: OEMCSFraqDatabase, 79 AddConstMol, 79 AddMol.79 ClearIndexedMols, 80 Constructors, 79 CoreToMoleculeCount, 80 CoreToMolecules, 80 GetMaxCoreMolecule, 80 GetMaxCoreMoleculeCount, 80 GetMaxMolIdx, 80 GetOptions, 81 GetScores, 81 GetSortedScores. 81 IsIndexed, 82 MoleculeToCores, 83 NumFragments, 83 NumMols, 83 ProcessMol, 84 OEMedChem:: OEMCSFragDatabaseCoreQuery, 142 OEMedChem:: OEMCSFragDatabaseOptions, 84 ClearIndexableFragmentRange, 85 Constructors, 84 GetFragmentationLimit, 85 GetIndexableFragmentRangeMax, 85 GetIndexableFragmentRangeMin, 85 GetMaxAtomFilter, 85 GetMaxFragLimit, 85 GetMinFragLimit, 86 GetOptions, 86 GetRingFragLimit, 86

HasIndexableFragmentHeavyAtomRange, 86 operator=, 84 operator==, 85 SetFragLimits, 86 SetFragmentationLimit, 86 SetIndexableFragmentRange, 87 SetMaxAtomFilter, 87 SetOptions, 87 SetRingFragLimit, 87 OEMedChem:: OEMCSFragDatabaseSetup, 109 OEMedChem:: OEMCSFragDatabaseSetup:: All, 109 OEMedChem:: OEMCSFragDatabaseSetup:: AllFrags, 109 OEMedChem:: OEMCSFragDatabaseSetup:: BondFragLimit, 110 OEMedChem:: OEMCSFragDatabaseSetup:: FragCutsRange, 110 OEMedChem::OEMCSFragDatabaseSetup::FragmentationCut 111 OEMedChem:: OEMCSFragDatabaseSetup:: FragMinMaxRange, 111 OEMedChem:: OEMCSFraqDatabaseSetup:: HeavyAtomLimit, 112 OEMedChem:: OEMCSFragDatabaseSetup:: IndexHydrogenSit 112 OEMedChem:: OEMCSFragDatabaseSetup:: RingCuts, 113 OEMedChem:: OEMCSMolSimScore, 87 Constructors, 87 GetIdx, 88 GetMCSCore, 88 GetScore, 88 operator=, 88 Set, 88 OEMedChem:: OEMCSScoreType, 113 OEMedChem:: OEMCSScoreType:: AtomCount, 114 OEMedChem:: OEMCSScoreType:: BondCount, 114 OEMedChem:: OEMCSScoreType:: Default, 114 OEMedChem::OEMCSScoreType::Undefined, 113 OEMedChem:: OEMCSSimFuncBase, 88 Constructors, 89 CreateCopy, 89 GetMCSSimTypeString, 89 operator(), 89 OEMedChem:: OEMCSTanimotoSim, 89 Constructors, 90 CreateCopy, 90 GetMCSSimTypeString, 90 operator(), 90

```
OEMedChem:: OEMCSTverskySim, 90
                                               OEMedChem:: OEMatchedPairTransform,
   Constructors, 91
                                                  100
   CreateCopy, 91
                                               OEMedChem:: OEMatchedPairTransformExtractOptions
   GetAlpha, 91
                                                  103GetBeta, 91
                                               OEMedChem:: OEMCSFragDatabaseOptions,
   GetMCSSimTypeString, 92
                                                  84
                                               OEMedChem:: OEMCSMolSimScore. 88
   operator(), 91
OEMedChem:: OEMedChemGetArch, 143
                                           operator==
OEMedChem:: OEMedChemGetLicensee, 143
                                               OEMedChem:: OEMCSFragDatabaseOptions,
OEMedChem:: OEMedChemGetPlatform, 143
                                                  85
OEMedChem:: OEMedChemGetRelease, 143
                                           \mathsf{P}OEMedChem:: OEMedChemGetSite, 143
OEMedChem:: OEMedChemGetVersion, 143
                                           ProcessMol
OEMedChem:: OEMedChemIsLicensed, 144
                                               OEMedChem:: OEMCSFragDatabase, 84
OEMedChem:: OEMoleculeToCores, 144
                                           S
OEMedChem:: OENormalMolecularComplexity,
       145
                                           Set
OEMedChem:: OENormalStereoComplexity, 145
                                               OEMedChem:: OEMCSMolSimScore, 88
OEMedChem:: OEReadMatchedPairAnalyzer,
                                           SetAttachmentPoints
       145
                                               OEMedChem:: OEMatchedPairTransformExtractOptions
OEMedChem:: OEReadMCSFragDatabase, 146
                                                  106
OEMedChem:: OEReadMMPIndexMolecules, 146
                                           SetContext
OEMedChem:: OERegionType, 127
                                               OEMedChem:: OEMatchedPairTransformExtractOptions
OEMedChem::OERegionType::All, 128
                                                  107
OEMedChem:: OERegionType:: Framework, 127
                                           SetDirection
OEMedChem:: OERegionType:: Linker, 127
                                               OEMedChem:: OEMatchedPairTransformExtractOptions
OEMedChem:: OERegionType:: Ring, 127
                                                  107
OEMedChem:: OERegionType:: Sidechain, 127
                                           SetFragLimits
OEMedChem::OESetupMatchedPairIndexOptions,
                                              OEMedChem:: OEMCSFragDatabaseOptions,
       146
                                                  86
OEMedChem::OESetupMCSFragDatabaseOptionsgetFragmentationLimit
       146
                                               OEMedChem:: OEMatchedPairAnalyzerOptions,
OEMedChem:: OETotalMolecularComplexity,
                                                  96
       147
                                               OEMedChem:: OEMCSFragDatabaseOptions,
OEMedChem:: OEWriteMatchedPairAnalyzer,
                                                  86
       147
                                           SetIndexableFragmentRange
OEMedChem:: OEWriteMCSFraqDatabase, 148
                                               OEMedChem:: OEMatchedPairAnalyzerOptions,
OEMedChem:: OEWriteMMPIndexMolecules, 149
                                                  97
oemedcheminfo.py
                                               OEMedChem:: OEMCSFragDatabaseOptions,
   Example Code, 72
                                                  87
operator()
                                           SetIsotopes
   OEMedChem:: OEMCSSimFuncBase, 89
                                               OEMedChem:: OEMatchedPairTransformExtractOptions
   OEMedChem:: OEMCSTanimotoSim, 90
                                                  107
   OEMedChem:: OEMCSTverskySim, 91
                                           SetMatchedPairData
operator+
                                               OEMedChem:: OEMatchedPairTransformExtractOptions
   OEMedChem:: OECreateMMPIndexStatus,
                                                  10777
                                           SetMatchedPairs
operator=
                                               OEMedChem:: OEMatchedPairTransformExtractOptions
   OEMedChem:: OECreateMMPIndexStatus,
                                                  108
       77SetMaxAtomFilter
   OEMedChem:: OEMatchedPair, 98
                                               OEMedChem:: OEMatchedPairAnalyzerOptions,
   OEMedChem:: OEMatchedPairAnalyzerOptions,
                                                  97
       95
                                               OEMedChem:: OEMCSFragDatabaseOptions,
                                                  87
```

SetMaxRecord OEMedChem:: OECreateMMPIndexStatus, OEMedChem:: OECreateMMPIndexOptions, 78 SetUnsaturatedHeteroBonds 76 SetMaxSubstituentLimitSkip OEMedChem:: OEBemisMurckoOptions, 74 OEMedChem::OEMatchedPairTransformExtrettCptidns, OEMedChem:: OECreateMMPIndexStatus, 108 78 SetMCSCorrespondence OEMedChem::OEMatchedPairTransformExtrettVerthoses, 107 OEMedChem::OECreateMMPIndexOptions, SetMMPLimit 76 OEMedChem:: OEMatchedPairTransformExtractOptions, 108 SetMoleculeTitle ToIndex OEMedChem:: OEMatchedPairTransform, OEMedChem:: OEMatchedPair, 100  $103$ ToSmiles SetNumMatchedPairs OEMedChem:: OEMatchedPair, 100 OEMedChem:: OECreateMMPIndexStatus,  $\mathsf{V}$ 78 SetNumMols Validate OEMedChem:: OECreateMMPIndexStatus, OEMedChem:: OEBemisMurckoOptions, 74 78 SetNumThreads OEMedChem:: OECreateMMPIndexOptions, 76 SetOptions OEMedChem:: OEMatchedPairAnalyzerOptions, 97 OEMedChem:: OEMatchedPairTransformExtractOptions, 108 OEMedChem:: OEMCSFragDatabaseOptions, 87 SetProcessorType OEMedChem:: OEMatchedPairAnalyzerOptions, 97 SetRegionType OEMedChem:: OEBemisMurckoOptions, 74 SetRingFragLimit OEMedChem:: OEMCSFragDatabaseOptions, 87 SetSMARTS OEMedChem:: OEMatchedPairTransformExtractOptions, 109 SetSubstituentLimit OEMedChem:: OEMatchedPairTransformExtractOptions, 108 SetSubstituentSearch OEMedChem:: OEBemisMurckoOptions, 74 SetTracer OEMedChem:: OECreateMMPIndexOptions, 76 SetTransform OEMedChem:: OEMatchedPairTransform, 103 SetUnindexedMols