![](_page_0_Picture_0.jpeg)

# **Bioisostere TK - Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

## **CONTENTS**

| <b>1 Theory</b>                          |    |
|------------------------------------------|----|
| 1.1 Theory                               | 3  |
| 1.1.1 Fragment similarity searching      | 3  |
| 1.1.2 Clash detection and selectivity    | 4  |
| 1.1.3 Strain energy                      | 4  |
| 1.1.4 Fragment joining                   | 4  |
| 1.1.5 Cyclization                        | 5  |
| 1.1.6 Molecular complexity               | 5  |
| 1.1.7 Aromatic fragment comparison       | 5  |
| 1.1.8 Shape-based belief model           | 6  |
| 1.1.9 Abbott bioavailability score       | 6  |
| 1.1.10 BROOD Database Generation (CHOMP) | 6  |
| 1.1.11 BROOD Database                    | 7  |
| 1.2 Bioisostere How to                   | 7  |
| <b>2 Bioisostere Examples</b>            |    |
| 2.1 Building Brood Database (CHOMP)      | 9  |
| 2.2 Creating Brood Query                 | 11 |
| 2.3 Generating Brood Hits                | 13 |
| 2.4 Generating Brood Matches             | 16 |
| 2.5 Overlay between Fragments            | 18 |
| 2.6 Replacing a Fragment in a Molecule   | 20 |
| <b>3 API</b>                             |    |
| 3.1 OEBioisostere Classes                | 23 |
| 3.1.1 OEBroodBuildOptions                | 23 |
| 3.1.2 OEBroodDBFilter                    | 25 |
| 3.1.3 OEBroodDBPacket                    | 26 |
| 3.1.4 GetIdx                             | 27 |
| 3.1.5 GetFragCount                       | 27 |
| 3.1.6 IsValid                            | 27 |
| 3.1.7 Load                               | 27 |
| 3.1.8 ToRecord                           | 27 |
| 3.1.9 OEBroodFragPrep                    | 27 |
| 3.1.10 OEBroodGeneralOptions             | 28 |
| 3.1.11 OEBroodHit                        | 30 |
| 3.1.12 OEBroodHitlistOptions             | 36 |
| 3.1.13 OEBroodMolBuilder                 | 38 |
| 3.1.14 OEBroodOverlay                    | 38 |
| 3.1.15 OEBroodOverlayBase                | 39 |

|   |                 | 3.1.16                 | OEBroodQuery<br>4                    |
|---|-----------------|------------------------|--------------------------------------|
|   |                 | 3.1.17                 | OEBroodScore<br>4                    |
|   |                 | 3.1.18                 | OEBroodScoreOptions<br>4             |
|   |                 | 3.1.19                 | OEDBBuffer<br>4                      |
|   |                 | 3.1.20                 | OEDBBuilder<br>4                     |
|   |                 | 3.1.21                 | OEDBReader<br>5                      |
|   |                 | 3.1.22                 | OEDBScreenOptions<br>5               |
|   |                 | 3.1.23                 | OEDBWriter<br>5                      |
|   |                 | 3.1.24                 | OEFragConfReader<br>5                |
|   |                 | 3.1.25                 | OEFragmentOptions<br>5               |
|   |                 | 3.1.26                 | OEFragOverlay<br>5                   |
|   |                 | 3.1.27                 | OEHitlistBuilder<br>5                |
|   |                 | 3.1.28                 | OEMolPropertyOptions<br>6            |
|   |                 | 3.1.29                 | OEIntrinsicPropOptions<br>6          |
|   |                 | 3.1.30                 | OEExtrinsicPropOptions<br>6          |
|   | 3.2             |                        | OEBioisostere Constants<br>7         |
|   |                 | 3.2.1                  | OEBroodBuildType<br>7                |
|   |                 | 3.2.2                  | OEBroodScoreType<br>7                |
|   |                 | 3.2.3                  | OEBroodStatusCode<br>7               |
|   | 3.3             |                        | OEBioisostere Functions<br>7         |
|   |                 | 3.3.1                  | OEBioisostereGetArch<br>7            |
|   |                 | 3.3.2                  | OEBioisostereGetLicensee<br>7        |
|   |                 | 3.3.3                  | OEBioisostereGetPlatform<br>7        |
|   |                 | 3.3.4                  | OEBioisostereGetRelease<br>7         |
|   |                 | 3.3.5                  | OEBioisostereGetSite<br>7            |
|   |                 | 3.3.6                  | OEBioisostereGetVersion<br>7         |
|   |                 | 3.3.7                  | OEBioisostereIsLicensed<br>7         |
|   |                 | 3.3.8                  | OECreateBroodQuery<br>7              |
|   |                 | 3.3.9                  | OEGenerateConformers<br>7            |
|   |                 | 3.3.10                 | OEGetBroodStatus<br>7                |
|   |                 | 3.3.11                 | OEGetDBIndices<br>7                  |
|   |                 | 3.3.12                 | OEReadBroodQuery<br>7                |
|   |                 | 3.3.13                 | OEWriteBroodQuery<br>8               |
| 4 |                 | <b>Release History</b> | 8                                    |
|   | 4.1             |                        | Bioisostere TK 4.1.0<br>8            |
|   |                 | 4.1.1                  | New features<br>8                    |
|   |                 | 4.1.2                  | Major bug fixes<br>8                 |
|   |                 | 4.1.3                  | Minor bug fixes<br>8                 |
|   | 4.2             |                        | Bioisostere TK 4.0.0<br>8            |
|   |                 | 4.2.1                  | New features<br>8                    |
| 5 |                 |                        | <b>Copyright and Trademarks</b><br>8 |
| 6 |                 | <b>Sample Code</b>     | 8                                    |
| 7 | <b>Citation</b> |                        | 8                                    |
|   | 7.1             |                        | Orion® Floes<br>8                    |
|   | 7.2             |                        | Toolkits and Applications<br>8       |
|   | 7.3             |                        | OpenEye Web Services<br>8            |
| 8 |                 |                        | <b>Technology Licensing</b><br>9     |
|   | 8.1             | <b>GCC</b>             | 10                                   |
|   |                 | 8.1.1                  | GCC RUNTIME LIBRARY EXCEPTION<br>10  |
|   |                 | 8.1.2                  | GNU GENERAL PUBLIC LICENSE<br>10     |

**Index** 

Attention: Bioisostere TK is currently only available in C++ and Python.

## **CHAPTER**

## **ONE**

## **THEORY**

## 1.1 Theory

There is a long history to fragment and bioisosteric replacement (see [Chen-2003]). Most medicinal chemists are well versed in standard sets of bioisosteric fragments. Likewise, there is a long history of computational approaches to fragment replacement (see [Verloop-1987] and [Lauri-1994]). There have been several attempts to examine sets of known active compounds to empirically identify bioisosteric fragments (see [Ujváry-2003] and [Sheridan-2002]). While this is an interesting exercise, it has two drawbacks. First, it can only identify bioisosteric fragment pairs that are already known. While these provide interesting study, they are often already familiar to experienced medicinal chemists and modelers. Second, it identifies many incidental rather than meaningful fragment pairs. These result from the fact that simply because two molecules bind to the same site does not mean they differ only by bioisosteric replacement. For instance, chemists may analog a compound by substituting an N-methyl group with an N-benzyl group in order to identify new binding pockets. However, just because both of these compounds are bioactive does not mean that methyl and benzyl are similar fragments (though they would be identified as such by some methods). While one may apply various heuristics, such as size, to avoid this problem, we hope to explore methods that are more robust.

An alternative approach has been to use an algorithm that would predict whether two fragments are similar in relevant ways. Several groups including Bartlett, Verloop, and Willett (see [Lauri-1994], [Verloop-1987], and [Watson-2001]) have developed methods in this area. Here we seek to capitalize on and extend the ideas developed by these workers.

## 1.1.1 Fragment similarity searching

**BROOD** allows users to enter a single query fragment and search a very large database of known molecular fragments in order to identify fragments that are similar. Each database fragment is compared to the query fragment in 3D with regard to shape, chemistry, electrostatics, and geometric presentation of attachment vectors. The fragments that are most similar to the query fragment will appear in a hitlist.

All similar fragments in a **BROOD** hitlist are organized into clusters. The clusters are organized so that molecules with the same ring structures and core framework (reduced-graph) are placed in the same cluster. The first cluster in **BROOD** hitlists is always the molecules that are similar to the query, sharing the same core atomic framework. While some of these analogs may be obvious, they often include alternative interesting chemistries. The remaining clusters are each organized around a unique core atomic framework. Each cluster is represented by its best scoring member and the clusters themselves are ranked by the score of their best member.

## 1.1.2 Clash detection and selectivity

**BROOD** allows users to specify protein structures for the purpose of testing whether newly constructed analogs fit into the active site. When the BROOD query ligand is based upon a crystallographic co-crystal structure, BROOD builds the newly created analog molecules in the same shape and orientation as the query. If the crystallographic ligand was originally in an active site and the protein is passed to **BROOD** as the bump protein, the new analogs will be built in poses that are also in the bump protein's active site. When a bump protein is passed, **BROOD** checks for clashes between the bump protein and each analog. By default, if any ligand heavy atom is less than 2.25 Angstroms from a protein heavy atom, the analog is removed from the hitlist.

Users can also specify another protein for selectivity testing (referred to here as the selectivity protein). In order for an analog to remain in the final hitlist, it must clash with the selectivity protein. The bump protein and the selectivity protein should be aligned and the **BROOD** query should be based on a molecule that fits within the bump protein active site. In this case, analogs in the final **BROOD** hitlist will also fit into the bump protein's active site, while they will also have clashes with the selectivity protein. This combination is a simple model for analogs that have a chance to be active against the bump protein, but have a very low chance of being active against the selectivity protein. This model assumes the analog molecules bind to the bump protein in a manner that is similar to the original ligand and that the most favorable pose for the ligand class in the selectivity protein is similar to that in the bump protein.

## 1.1.3 Strain energy

**BROOD's** output includes newly constructed analog molecules that are intended to have a similar 3D shape to the query molecule. These new analogs are constructed partially from the original molecule and partially from new fragments. When these new molecules are generated and built into a conformation that has good shape and chemistry overlap with the query molecules, some strain may be introduced. To produce high-quality results, it is essential that the analogs are optimized while maintaining the query shape and that little strain is introduced in the process.

The BROOD search process guarantees that each of the molecular fragments alone is in a low energy state. After the fragments are joined, this may no longer be true. For every **BROOD** analog in the final hitlist, two optimizations are carried out to determine the local strain introduced by maintaining a shape similar to the original query. In the first optimization, the ligand is allowed to relax into a local minimum. In the second optimization, the ligand atoms are only allowed to move a fraction of an Angstrom, keeping the same overall shape of the molecule. In both calculations, the OEMMFF [Halgren-I-1996], [Halgren-II-1996], [Halgren-III-1996], [Halgren-IV-1996], [Halgren-V-1996], [Halgren-VI-1999], [Halgren-VII-1999] potential is used with a Sheffield solvation function [Grant-2007]. The local strain energy is the difference in ligand energy between the two calculations. By default, the maximum strain for any successful **BROOD** analog is limited to 6.5 kCal/M.

## 1.1.4 Fragment joining

One approach to lead identification and development is based on the identification and expansion of physically very small molecule inhibitors that are commonly termed "fragments" (see [Hajduk-2007]). Fragments in this sense are molecules with few atoms and should not be confused with the term fragment used elsewhere in this document that refers to part of a molecule. Nevertheless, the fragment replacement algorithm in **BROOD** can be useful in the modeling of fragment-based design. In fragment-based design, one strategy is to combine two non-overlapping inhibitory fragments to form a single molecule. While this is sometimes empirically done with a series of flexible linear linkers, the linkers can also be modeled.

## 1.1.5 Cyclization

One of the first applications of **BROOD** many users want to explore is the replacement of a flexible portion of a molecule with a more rigid fragment that fills the same space. **BROOD** excels at this application. This type of exercise can be considered a local cyclization. In some molecules, rather than a local cyclization, some chemists prefer to design a bridge between two portions of a molecule that do not have a local link. This is another task where **BROOD** can be quite useful. Long-distance cyclization, like fragment joining, is about finding a chemical fragment that can bridge to moieties given a particular 3D orientation.

## 1.1.6 Molecular complexity

In the early 1980's, Bertz first published a measure of the complexity of molecules and asserted that his calculated complexity could be related to synthetic ease ([Bertz-1981], [Bertz-1982]). Bertz built complexity terms that are similar to a Shannon entropy ((Shannon-1949)) but with regard to the elements in a molecule and the diversity of small fragments that make up the structure of the molecule. While the actual synthetic accessibility can be heavily influenced by the availability of complex synthetic building blocks and advances in stereo synthetic methods, molecular complexity remains a useful tool for prioritizing which compounds chemists should look at first when primary modeling methods don't readily distinguish between them.

In 2007, Boda and coworkers extended Bertz's idea and compared it to experimental chemists' predictions of synthetic accessibility ([Boda-2007]).

Boda made the significant advance of adding stereo complexity to Bertz's elemental, graph, and ring complexity. We noted in the paper that nearly all the signal was generated by the molecular complexity and stereo complexity. In fact, each of these measures, without the linear fitting presented in the paper, correlated with chemists' predictions of synthetic accessibility as well as the chemists' predictions correlated with one another. Thus, in **BROOD**, we have implemented a molecular complexity that is a normalized sum of the graph and size complexity, elemental complexity, and stereo complexity. The normalized complexity score starts at zero for the simplest, smallest molecule and grows to values that generally don't exceed 1.0 for medicinally relevant small molecules.

**BROOD** uses molecular complexity to sort analog molecules in the final hitlist that have very similar shape and color scores.

## 1.1.7 Aromatic fragment comparison

This is an example of applying **BROOD** as a technology to explore fragment similarity outside the direct context of a specific drug-discovery project. Tu and coworkers at Pfizer explored the chemical space of aromatic ring systems ([Tu-2012]). In their work, they used **BROOD** at the core of the NEAT (Novel and Electronically Equivalent Aromatic Templates) tool. This tool uses a combination of high-level QM-derived partial charges along with **BROOD**'s electrostatic similarity calculation to explore potentially aromatic system replacements. It allows medicinal chemists to explore the large space of complex aromatic ring systems for replacements that are both electronically and sterically analogous. We present this example as an illustration of the more diverse applications of **BROOD**'s fragment-matching technology.

## 1.1.8 Shape-based belief model

It is a well-known concept in medicinal chemistry that compounds with greater similarity have a higher probability of having shared properties. It is by this premise that project teams seek to explore chemical space around a lead compound in order to discover new active molecules. Based on this concept, Muchmore and colleagues at Abbott attempted to quantify the relationship between various measures of ligand similarity and binding activity ([Muchmore-2008]). A large number of ligands with activities measured across a large number and wide variety of targets were used to generate the probability that two molecules with a given similarity would have activity within one log unit of one another (the p[active]). Several well-regarded ligand similarity techniques showed sigmoidal curves where, at very low similarity, the probability of shared activity was related to the prevalence of inhibitors in the underlying data; whereas, as two molecules approached very high similarity, the probability of similar activity approached something like 35-55%. While perhaps surprising at first, both of these results are sensible. It is well known that while similar molecules are much more likely to have shared activity than two random molecules, similarity is by no means a guarantee of shared activity.

As reported in their paper, one of the similarity techniques with the highest maximum probability was the combo score (shape + color score) from the OpenEye tool ROCS. The critical change from color score to color Tanimoto occurred in ROCS since the publication of Muchmore's paper. The change to color Tanimoto resulted in an even higher maximum probability of 0.512 ([Brown-Muchmore-2008]) for shape + color Tanimoto. The curve that was refit using the Abbott data is used in **BROOD** to convert the overall shape  $+$  color Tanimoto similarity of the analog molecule to the query molecule to generate a p(Active) value that indicates the probability, according the Abbott's belief model, that the analog compound will have activity within one log unit of the query compound.

## 1.1.9 Abbott bioavailability score

In 2005, Martin published a predictive model for the probability that a compound will have bioavailability (f) > 10% in rats ([Martin-2005]). Despite attempts to identify a useful model using straightforward linear combinations of simple parameters, such as logP, logD, donors, acceptors, PSA, or flexibility, Martin noted that different predictive models were required for different ionization states. Anions require a bioavailability model that depends strongly on PSA. By contrast, neutral species, cations, and zwitterions require a model based on the rule-of-five. The combination of these models provides a single model for bioavailability in rats.

## 1.1.10 BROOD Database Generation (CHOMP)

**BROOD's** database generation program, CHOMP, fragments molecules by identifying critical bonds that can be broken. CHOMP includes three sets of bond-breaking patterns: RLF (ring, linkers & functional groups), RECAP rules [Lewell-1998], and ALL (indicating breaking all non-ring, non-resonance single bonds). By default, CHOMP breaks all bonds identified using any of these methods. Users can also specify a SMARTS file of their own bond identifiers. This file should include a series of SMARTS patterns (one per line) that each define two atoms on opposite ends of the bond to be broken. For example, a line with the SMARTS "-" will cause all single bonds to be broken, while a line with the SMARTS "[R]-[!R]" will cause all bonds between ring atoms and non-ring atoms to be broken and "[#6]-!@[!#6!#1]" will cause CHOMP to break every single non-ring bond between a carbon atom and a heteroatom.

The RLF chemical heuristics seek to break compounds into three types of primary fragments; contiguous ring systems, functional groups, and linkers. Contiguous ring systems include any set of atoms that are bonded together by at least one ring bond. Thus, fused rings and spiro rings are included as a single ring system, but biphenyl is broken into two ring systems. Functional groups are defined as any collection of bonded atoms including one or more heteroatoms or unsaturated carbons separated by at most a single fully saturated carbon atom. The linkers are the remaining saturated carbon skeletons. It should be noted that linkers, like functional groups and ring systems, can be terminal (i.e., degree  $1$ ).

**CHOMP** systematically identifies all the molecular fragments that can be generated by breaking one or more of the specified bonds. CHOMP first eliminates fragments that have more than 15 heavy atoms or that have more than three attachment points. CHOMP also filters the fragments based on commonly used molecular filters, eliminating unstable, reactive, or toxic functional groups. As a final fragment generation step, for every fragment with two attachment points, **CHOMP** generates two single attachment fragments; for every fragment with three attachment points, **CHOMP** generates six fragments with two attachment points and three fragments with single attachment points by capping the open attachment valence with hydrogens. CHOMP then eliminates any duplicate fragments.

This first portion of the CHOMP algorithm involves only graph processing and can proceed very quickly. Please note, however, that when processing molecular databases of more than a few million compounds, CHOMP will use significant amounts of memory. Memory usage is especially aggressive early in the execution, when many new fragments are being identified, and slows somewhat as the algorithm progresses.

The next stage of the CHOMP algorithm is to generate 3D conformers using a specialized version of the OMEGA algorithm. CHOMP's version of OMEGA has a modified TORLIB in order to sample more generously around the attachment points. It also differs from default OMEGA parameters in having tighter constraints for removal of RMSD duplicates (as the measure is very sensitive to size) and for having scaled MAXCONFS and EWINDOW parameters based on the size of the fragments. Finally, CHOMP writes the fragments into a BROOD database. To accomplish this, **CHOMP** carries out several precalculations, including generating physical properties and adding color atoms. CHOMP also segregates the fragment conformers into groups that are likely to match the same types of queries. All these processes help **BROOD** search the databases more quickly.

## 1.1.11 BROOD Database

**BROOD** databases are currently in the format of a directory or folder that contains many files. The databases can be easily compressed and uncompressed with standard compression algorithms. They can also be moved, but not easily renamed. To rename the BROOD database, you must also rename all the files contained within it. Consistency is required to prevent confusion between the name of the database and the files being searched under that name.

Of the files in the database directory, only one is human-readable. This is the . info file. If you open the . info file with a text reader, you will see some information about the database, its version, and a manifest of the files that are supposed to be in the database. Whenever a database is read, the manifest is checked to ensure the database has not been corrupted.

## 1.2 Bioisostere How to

## **CHAPTER**

**TWO** 

## **BIOISOSTERE EXAMPLES**

The following table lists the currently available Bioisostere TK examples:

| Program                 | Description                        |
|-------------------------|------------------------------------|
| <i>brood_database</i>   | Building Brood Database (CHOMP)    |
| <i>brood_query</i>      | Creating Brood Query               |
| <i>brood_hitlist</i>    | Generating Brood Hits              |
| <i>brood_matches</i>    | Generating Brood Matches           |
| <i>fragment_overlay</i> | Overlay between Fragments          |
| <i>replace_fragment</i> | Replacing a Fragment in a Molecule |

## 2.1 Building Brood Database (CHOMP)

The following code example shows how to build a Brood database from a library of molecules.

#### See also:

- OEFragmentOptions class
- OEDBScreenOptions class
- OEDBBuilder class
- OEDBWriter class
- OEGenerateConformers function

#### **Listing 1: Building Brood Database (CHOMP)**

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
from openeye import oechem
from openeye import oebioisostere
from openeye import oemolprop
class ChompOptions (oechem. OEOptions) :
    def __init__(self):oechem.OEOptions.__init__(self, "ChompOptions")
        dbParam = occhem.OEstringParameter('--out")dbParam.SetVisibility(oechem.OEParamVisibility_Simple)
        dbParam. SetBrief ("Output database folder name")
        dbParam.SetRequired(True)
        dbParam.SetKeyless(2)
        self._dbParam = self.AddParameter(dbParam)
        self. fragOpts = oebioisostere. ToFragmentOptions(self.AddOption(oebioisostere.
\rightarrowOEFragmentOptions()))
        self._screenOpts = oebioisostere.ToDBScreenOptions(self.
→AddOption(oebioisostere.OEDBScreenOptions()))
        pass
    def CreateCopy(self):
        return self
    def GetDBName(self):
        return self._dbParam.GetStringValue()
   def GetFraqOpts(self):
        return self. _fragOpts
    def GetScreenOpts(self):
        return self._screenOpts
def main(argy=[ name ]):
   chompOpts = ChompOptions()opts = oechem. OESimpleAppOptions (chompOpts, "BroodDataBase", oechem.
\rightarrowOEFileStringType_Mol)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    chompOpts. UpdateValues (opts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   print ("Generating fragments...")
   builder = oebioisostere. OEDBBuilder (chompOpts.GetFraqOrts())for mol in ifs. GetOEMols () :
        builder.Generate(mol)
```

```
print ("Building 2D fragments library...")
   builder.Filter(oebioisostere.OECreateFragFilter())
   builder. Expand (oebioisostere. OECreateFlipperOptions ())
   builder. Screen (chompOpts. GetScreenOpts())
    print ("Generating fragment conformers...")
    writer = oebioisostere.OEDBWriter()
   writer. Init (chompOpts. GetDBName ())
    count = 0for frag in builder. GetFrags():
        if oebioisostere. OEGenerateConformers(frag):
            writer. Write (frag)
            count += 1writer.Finish()
    print ("Generated fragments: %d" % count)
if name == "_main_":
    import sys
    sys.exit(main(sys.argv))
```

## **2.2 Creating Brood Query**

The following code example shows how to create a Brood Query from a molecule that could be used for Bioisosteric fragment replacements using Brood.

#### See also:

- OEBroodQuery class
- OECreateBroodQuery function

#### **Listing 2: Creating Brood Query**

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

(continues on next page)

from openeye import oechem

from openeye import oebioisostere

```
class QueryOptions (oechem. OEOptions) :
    def __init__(self):oechem. OEOptions.__init__(self, "QueryOptions")
        idxParam = oechem.OEUIntParameter("-atomIndices")
        idxParam.SetIsList(True)
        idxParam.SetRequired(True)
        idxParam.SetBrief("Index of atoms in fragment")
        self._idxParam = self.AddParameter(idxParam)
        duParam = oechem.OEFileStringParameter("-du", oechem.OEFileStringType_DU)
        duParam.SetBrief ("Design unit containing protein target for bump check")
        self. duParam = self.AddParameter(duParam)
        maskParam = oechem. OEUIntParameter ("-proteinMask", oechem.
\rightarrowOEDesignUnitComponents_TargetComplex)
        maskParam. SetBrief ("Design unit mask to identify protein target")
        self._maskParam = self.AddParameter(maskParam)
    def CreateCopy(self):
        return self
    def GetIndices (self) :
        indices = \lceil]
        for idx in self. _idxParam.GetStringValues():
            indices.append(int(idx))
        return indices
    def GetDU(self):
        if s = oechem.oeifstream()if not self._duParam.GetHasValue():
            return None
        if not ifs.open(self._duParam.GetStringValue()):
            oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
        du = oechem.OEDesignUnit()
        if not oechem. OEReadDesignUnit(ifs, du):
            oechem. OEThrow. Fatal ("Unable to read design unit")
        return du
    def GetProteinMask (self) :
        mask = self._maskParam.GetStringValue()
        if \text{mask} == \text{""}:
            mask = self._maskParam.GetStringDefault()
        return int (mask)
def main(argv=[_name_]):
   queryOpts = QueryOptions()
    opts = oechem.OESimpleAppOptions(queryOpts, "BroodQuery", oechem.OEFileStringType_
-Mol3D, "oeb")if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    queryOpts. UpdateValues (opts)
```

(continues on next page)

 $if s = oechem.oemolistream()$ 

```
(continued from previous page)
```

```
if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = oechem.oemolostream()
    if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    queryMol = ochem. OEMol()if not oechem. OEReadMolecule(ifs, queryMol):
        oechem. OEThrow. Fatal ("Unable to load molecule")
    indices = queryOrts.GetIndices()atoms = []for idx in indices:
        atom = queryMol.GetAtom(oechem.OEHasAtomIdx(idx))if not atom:
            oechem. OEThrow. Fatal ("Invalid atom index %d" % idx)
        atoms.append(atom)
    selection = oechem. OEAtomBondSet()
    selection.AddAtoms(atoms)
   query = oebioisostere. OEBroodQuery()
   du = queryOrts.GetDU()if du is None:
        retCode = oebioisostere.OECreateBroodQuery(query, queryMol, selection)
    Also:retCode = oebioisostere.OECreateBroodQuery(query, queryMol, selection, du,
→queryOpts.GetProteinMask())
    if retCode != oebioisostere. OEBroodStatusCode_Success:
        oechem.OEThrow.Fatal("%s" % oebioisostere.OEGetBroodStatus(retCode))
    oebioisostere.OEWriteBroodQuery(ofs, query)
if _name_ == "_main_":
   import sys
    sys.exit(main(sys.argv))
```

## **2.3 Generating Brood Hits**

The following code example shows how to perform Bioisosteric fragment replacements on a Brood Query and generate a hitlist.

See also:

- OEBroodGeneralOptions class
- OEBroodScoreOptions class
- OEBroodHitlistOptions class
- OEBroodOverlay class
- OEHitlistBuilder class

#### **Listing 3: Generating Brood Hits**

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
from openeye import oechem
from openeye import oebioisostere
class BroodOptions (oechem. OEOptions) :
    def __init__(self):oechem.OEOptions.__init__(self, "BroodOptions")
        dbParam = oechem. OESTringParameter("db")dbParam. SetRequired (True)
        dbParam.SetVisibility(oechem.OEParamVisibility_Simple)
        dbParam.SetBrief("Database folder")
        self._dbParam = self.AddParameter(dbParam)
        self._genOpts = oebioisostere.ToGeneralOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodGeneralOptions()))
        self._scoreOpts = oebioisostere.ToScoreOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodScoreOptions()))
        self. hitOpts = oebioisostere. ToHitlistOptions (self. AddOption (oebioisostere.
\rightarrowOEBroodHitlistOptions()))
        pass
    def CreateCopy(self):
        return self
    def GetDatabase(self):
        return self._dbParam.GetStringValue()
    def GetGenOpts(self):
        return self._genOpts
    def GetScoreOpts(self):
        return self._scoreOpts
    def GetHitlistOpts(self):
        return self._hitOpts
```

```
(continued from previous page)
```

```
def main(argv=[_name_]):
    broadOpts = BroodOptions()opts = oechem. OESimpleAppOptions (broodOpts, "BroodHitlist", oechem.
\rightarrowOEFileStringType_Mol3D,
                                       oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    broodOpts.UpdateValues(opts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    query = oebioisostere. OEBroodQuery()
    retCode = oebioisostere. OEReadBroodQuery(ifs, query)
    if retCode != oebioisostere. OEBroodStatusCode_Success:
        oechem. OEThrow. Fatal ("Failed: %s" % oebioisostere. OEGetBroodStatus (retCode))
    reader = oebioisostere. OEDBReader()
    if not reader. Init (broodOpts.GetDatabase(), query, broodOpts.GetGenOpts()):
        oechem. OEThrow. Fatal ("Unable to load Brood database")
    overlay = oebioisostere. OEBroodOverlay (broodOpts. GetGenOpts (), broodOpts.
\rightarrowGetScoreOpts())
    overlay. SetupRef (query);
    hlist = oebioisostere. OEHitlistBuilder (query, broodOpts. GetGenOpts (), broodOpts.
\rightarrowGetHitlistOpts())
    packetCount = 0packet = oebioisostere. OEBroodDBPacket ()
    while reader. GetNextPacket (packet) :
        packetCount += 1
        print ("Processing packet %d with %d fragments" % (packetCount, packet.
\rightarrowGetFraqCount()))
        vecScore = overlap. Overlay (packet)hlist.AddScores(vecScores);
    print ("Generating hitlist...")
    hlist.Build();
    print ("Total number of fragments overlayed: %d" % hlist. GetAddCount ())
    print ("Number of final hits: \frac{2}{3}d" % hlist. GetHitCount ())
    for idx, hit in enumerate (hlist. GetHits()):
        oechem.OEWriteMolecule(ofs, hit.GetMol())
        cobmoscore = hit.getComboscore()if broodOpts.GetGenOpts().GetScoreType() == oebioisostere.OEBroodScoreType_ET:
            cobmoscore = hit {GetETComboscore( )}print ("Hit: %d %s Combo Score: %2f Belief Score: %.2f Complexity: %2f"
               % (idx+1, hit.GetMol().GetTitle(), cobmoScore, hit.GetBeliefScore(),
\rightarrowhit.GetComplexity()))
```

```
if
   name
           == " main ":
   import sys
   sys.exit(main(sys.argv))
```

## **2.4 Generating Brood Matches**

The following code example shows how to perform Bioisosteric fragment replacements on a Brood Query and generate all possible matches. This could be a use case when generating all possible design ideas using BROOD and post processing them with other tools.

#### See also:

- OEBroodGeneralOptions class
- OEBroodScoreOptions class
- OEBroodOverlay class
- OEBroodMolBuilder class

#### **Listing 4: Generating Brood Matches**

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
from openeye import oebioisostere
class BroodOptions (oechem. OEOptions) :
   def __init__(self):oechem.OEOptions.__init__(self, "BroodOptions")
        dbParam = oechem. OESTringParameter('--db")dbParam. SetRequired (True)
        dbParam.SetVisibility(oechem.OEParamVisibility Simple)
        dbParam.SetBrief("Database folder")
        self._dbParam = self.AddParameter(dbParam)
```

```
self._genOpts = oebioisostere.ToGeneralOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodGeneralOptions()))
        self._scoreOpts = oebioisostere.ToScoreOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodScoreOptions()))
        self. _buildOpts = oebioisostere. ToBuildOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodBuildOptions()))
        pass
    def CreateCopy(self):
        return self
    def GetDatabase(self):
        return self. _ dbParam. GetStringValue()
    def GetGenOpts(self):
        return self._genOpts
    def GetScoreOpts(self):
        return self._scoreOpts
    def GetBuildOpts(self):
        return self. buildOpts
def main(argv=[__name__]):
    broadOpts = BroodOptions()opts = oechem.OESimpleAppOptions(broodOpts, "BroodMatching", oechem.
\rightarrowOEFileStringType_Mol3D,
                                       oechem.OEFileStringType_Mol3D)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return <sub>0</sub>broodOpts. UpdateValues (opts)
    ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    query = oebioisostere. OEBroodQuery()
    retCode = oebioisostere. OEReadBroodQuery(ifs, query)
    if retCode != oebioisostere. OEBroodStatusCode_Success:
        oechem.OEThrow.Fatal("Failed: %s" % oebioisostere.OEGetBroodStatus(retCode))
    reader = oebioisostere.OEDBReader()
    if not reader. Init (broodOpts.GetDatabase(), query, broodOpts.GetGenOpts()):
        oechem. OEThrow. Fatal ("Unable to load Brood database")
    overlay = oebioisostere.OEBroodOverlay(broodOpts.GetGenOpts(), broodOpts.
\rightarrowGetScoreOpts())
    overlay. SetupRef (query);
    builder = oebioisostere.OEBroodMolBuilder(query, broodOpts.GetGenOpts(),
\rightarrowbroodOpts.GetBuildOpts())
```

```
packetCount = 0packet = oebioisostere. OEBroodDBPacket ()
   totalCount = 0successCount = 0while reader.GetNextPacket (packet) :
        packetCount += 1
        print ("Processing packet %d with %d fragments" % (packetCount, packet.
\rightarrowGetFraqCount()))
        vecScores = overlay. Overlay (packet)
        for score in vecScores:
            totalCount += 1if score. GetStatus() == oebioisostere. OEBroodStatusCode_Success:
                hit = oebioisostere.OEBroodHit()
                if builder.Build(score, hit) == oebioisostere.OEBroodStatusCode
\rightarrowSuccess:
                    oechem.OEWriteMolecule(ofs, hit.GetMol())
                    successCount += 1print ("Total number of fragments overlayed: %d" % totalCount)
    print ("Number of successful matches: %d" % successCount)
if _name_ = = "_main_".import sys
    sys.exit(main(sys.argv))
```

## 2.5 Overlay between Fragments

The following code example shows how to overlay a fragment against a query fragment. This could be a use case when working with synthons and trying to find similar synthon based on 3D similarity.

See also:

- OEBroodGeneralOptions class
- OEBroodScoreOptions class
- OEFragOverlay class

#### **Listing 5: Overlay between Fragments**

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
```

```
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oebioisostere
def main(argv=[_name_]):
    genOpts = oebioisostere. OEBroodGeneralOptions()
    opts = oechem.OERefInputAppOptions(genOpts, "FragmentOverlay", oechem.
\rightarrowOEFileStringType_Mol3D,
                                      oechem.OEFileStringType Mol3D, oechem.
→OEFileStringType_Mol3D, "-queryFrag")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return <sub>0</sub>genOpts. UpdateValues (opts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   rfs = oechem.oemolistream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   query = occhem. 0EMol()if not oechem. OEReadMolecule (rfs, query) :
        oechem. OEThrow. Fatal ("Failed to read Query fragment")
   prep = oebioisostere. OEBroodFragPrep()
   overlay = oebioisostere. OEFragOverlay (genOpts, oebioisostere.
\rightarrowOEBroodScoreOptions())
   overlay. SetupRef (query);
    for fraq in ifs. GetOEMols():
        oechem. OEThrow. Info("Overlaying %s" % frag. GetTitle())
        prep.Prep(frag)
        score = oebioisostere. OEBroodScore()
        ret\_code = overlap.Overlay(frag, score)if ret_code == oebioisostere. OEBroodStatusCode_Success:
            outmol = oechem. OEGraphMol()
            score.GetFraqMol(outmol)
            overlay. Transform (outmol)
            comboScore = score.GetComboScore()
            if genOpts. GetScoreType() == oebioisostere. OEBroodScoreType_ET:
                comboScore = score.GetETComboScore()
            print ("Fragment: %s Combo Score: %2f" % (frag.GetTitle(), comboScore))
            oechem.OEWriteMolecule(ofs, outmol)
        else:
            errMsg = oebioisostere.OEGetBroodStatus(ret_code)
```

```
oechem.OEThrow.Warning("%s: %s" % (frag.GetTitle(), errMsg))
   return 0
if name == "_main_":
   import sys
   sys.exit(main(sys.argv))
```

## 2.6 Replacing a Fragment in a Molecule

The following code example shows how to replace a fragment in a molecule defined in the form of a BROOD Query.

See also:

- OEBroodGeneralOptions class
- OEBroodScoreOptions class
- OEBroodOverlay class
- OEBroodMolBuilder class

#### Listing 6: Replacing a Fragment in a Molecule

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
from openeye import oebioisostere
class BroodOptions (oechem. OEOptions) :
    def __init__(self):oechem.OEOptions.__init__(self, "BroodOptions")
        self._genOpts = oebioisostere.ToGeneralOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodGeneralOptions()))
        self._scoreOpts = oebioisostere.ToScoreOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodScoreOptions()))
```

```
self. buildOpts = oebioisostere.ToBuildOptions(self.AddOption(oebioisostere.
\rightarrowOEBroodBuildOptions()))
        pass
    def CreateCopy(self):
        return self
    def GetGenOpts(self):
        return self._genOpts
    def GetScoreOpts(self):
        return self._scoreOpts
    def GetBuildOpts(self):
        return self. buildOpts
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    broadOpts = BroodOptions()opts = oechem. OERefInputAppOptions (broodOpts, "ReplaceFragment", oechem.
\rightarrowOEFileStringType Mol3D,
                                       oechem.OEFileStringType_Mol3D, oechem.
\rightarrowOEFileStringType Mol3D, "-query")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    broodOpts. UpdateValues (opts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    rfs = oechem.oemolistream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   query = oebioisostere.OEBroodQuery()retCode = oebioisostere. OEReadBroodQuery(rfs, query)if retCode != oebioisostere.OEBroodStatusCode_Success:
        oechem.OEThrow.Fatal("Failed: %s" % oebioisostere.OEGetBroodStatus(retCode))
    prep = oebioisostere.OEBroodFraqPrep()
    overlay = oebioisostere. OEBroodOverlay (broodOpts. GetGenOpts (), broodOpts.
\rightarrowGetScoreOpts())
    overlay. SetupRef (query);
    builder = oebioisostere. OEBroodMolBuilder (query, broodOpts. GetGenOpts(),
\rightarrowbroodOpts.GetBuildOpts())
    for fraq in ifs. GetOEMols():
        print ("Replacement fragment %s" % frag. GetTitle())
        prep.Prep(fraq)
        score = oebioisostere. OEBroodScore()
        ret_code = overlay.Overlay(frag, score)
        if ret_code == oebioisostere. OEBroodStatusCode_Success:
```

```
comboScore = score.GetComboScore()
            if broodOpts.GetGenOpts().GetScoreType() == oebioisostere.
\rightarrowOEBroodScoreType_ET:
                comboScore = score.GetETComboScore()
            print ("Fragment: %s Combo Score: %2f" % (frag.GetTitle(), comboScore))
            hit = oebioisostere.OEBroodHit()
            if builder.Build(score, hit) == oebioisostere.OEBroodStatusCode_Success:
                oechem.OEWriteMolecule(ofs, hit.GetMol())
        else:
            errMsg = oebioisostere. OEGetBroodStatus (ret_code)
            oechem.OEThrow.Warning("%s: %s" % (frag.GetTitle(), errMsg))
    return 0
if _name == " main ":
    import sys
    sys.exit(main(sys.argv))
```

## **CHAPTER**

## **THREE**

**API** 

## 3.1 OEBioisostere Classes

## 3.1.1 OEBroodBuildOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodBuildOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for building molecules with replaced fragments. These options are used both from OEBroodMolBuilder and OEHitlistBuilder.

The OEBroodBuildOptions class defines the following public methods:

- GetBuildType and SetBuildType
- · GetNeutralPH and SetNeutralPH
- · GetTautomers and SetTautomers
- · GetCheckBond and SetCheckBond
- · GetMaxLocalStrain and SetMaxLocalStrain

#### **Constructors**

```
OEBroodBuildOptions()
OEBroodBuildOptions (const OEBroodBuildOptions &)
```

Default and copy constructors.

#### operator=

OEBroodBuildOptions & operator=(const OEBroodBuildOptions &)

Assignment operator.

#### **GetBuildType**

unsigned GetBuildType() const

See SetBuildType method.

#### **GetNeutralPH**

bool GetNeutralPH() const

See SetNeutralPH method.

#### **GetTautomers**

bool GetTautomers() const

See Set Tautomers method.

#### **GetCheckBond**

bool GetCheckBond() const

See SetCheckBond method.

#### **GetMaxLocalStrain**

double GetMaxLocalStrain() const

See SetMaxLocalStrain method.

#### **SetBuildType**

bool SetBuildType (const unsigned)

Sets if Build Type to be applied in constructing the new analogs. Possible choices of methods are described in OEBroodBuildType. Default: Optimize3D.

#### **SetNeutralPH**

bool SetNeutralPH (const bool)

Sets if Neutral pH model to be applied on newly constructed analogs. Default: True.

#### **SetTautomers**

bool SetTautomers (const bool)

Sets if Reasonable tautomer model to be applied on newly constructed analogs. Default: False.

#### **SetCheckBond**

bool SetCheckBond()

Sets if Bond stability should be checked in generating hitlist. Default: True.

#### **SetMaxLocalStrain**

bool SetMaxLocalStrain(const double)

Sets the Number allowable local strain in the generated hits. Default: 6.5.

### 3.1.2 OEBroodDBFilter

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodDBFilter

This class defines objects that can be used to check if a *database packet* contains fragments relevant to a certain OEBroodQuery.

The OEBroodDBFilter class defines the following public methods:

 $• Set up$ 

#### **Constructors**

```
OEBroodDBFilter()
OEBroodDBFilter (const OEBroodDBFilter &)
```

Default and copy constructors.

#### operator=

```
OEBroodDBFilter & operator=(const OEBroodDBFilter &)
```

Assignment operator.

#### **Setup**

```
bool Setup (const OEBroodQuery & query,
           const OEBroodGeneralOptions &scoreOpts=OEBroodGeneralOptions())
```

Associate the filter with a specific OEBroodQuery.

## 3.1.3 OEBroodDBPacket

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

```
class OEBroodDBPacket
```

This class defines objects that holds a chunk of fragment data corresponding to a Brood database. The packet contain additional metadata information that can be used to check its relevance for bioisosteric replacement of a specific OEBroodQuery.

#### The OEBroodDBPacket class defines the following public methods:

- $\bullet$  GetIdx
- GetFragCount
- IsValid
- $\bullet$  Load
- ToRecord

#### **Constructors**

```
OEBroodDBPacket()
OEBroodDBPacket (const OEBroodDBPacket &)
```

Default and copy constructors.

#### operator=

OEBroodDBPacket & operator=(const OEBroodDBPacket &)

Assignment operator.

## **3.1.4 GetIdx**

unsigned GetIdx() const

Returns the index corresponding to database storage.

## 3.1.5 GetFragCount

unsigned GetFragCount () const

Returns the number of fragments contained in the packet.

## 3.1.6 IsValid

**bool** IsValid(const OEBroodDBFilter &filter)

Returns if the packet contents are relevant for OEBroodQuery associated with the OEBroodDBFilter.

### 3.1.7 Load

**bool** Load (const OEDataFlow:: OERecord &)

Loads the contents of packet from a OERecord.

## 3.1.8 ToRecord

**bool** ToRecord (OEDataFlow:: OERecord &) const

Saves the contents of packet into a OERecord.

## 3.1.9 OEBroodFragPrep

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodFragPrep

This class provides facilities to prepare fragments for overlay calculations with OEBroodFragPrep.

The OEBroodFragPrep class defines the following public methods:

 $\bullet$  Prep

#### **Constructors**

OEBroodFragPrep()

Constructor.

#### **Prep**

bool Prep (OEChem:: OEMCMolBase & fragment)

Prepares the specified fragment for overlay optimization.

## 3.1.10 OEBroodGeneralOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodGeneralOptions : public OESystem:: OEOptions

This class provides an interface to setup basic options related to biosiostereic fragment replacement.

The OEBroodGeneralOptions class defines the following public methods:

- · GetAttachScale and SetAttachScale
- · GetBumpRadius and SetBumpRadius
- · GetScoreType and SetScoreType

#### **Constructors**

```
OEBroodGeneralOptions()
OEBroodGeneralOptions (const OEBroodGeneralOptions &)
```

Default and copy constructors.

#### operator=

OEBroodGeneralOptions & operator= (const OEBroodGeneralOptions &)

Assignment operator.

### **GetAttachScale**

double GetAttachScale() const

See SetAttachScale method.

#### **GetBumpRadius**

double GetBumpRadius () const

See SetBumpRadius method.

#### **GetScoreType**

unsigned GetScoreType() const

See Set ScoreType method.

#### **SetAttachScale**

bool SetAttachScale (const double)

Sets the scaling factor for attachment point scores. This value determines the balance between the chemical color score and the attachment point scores. Higher values indicate more weighting for the attachment-point alignment. Default: 1.5.

#### **SetBumpRadius**

bool SetBumpRadius (const double)

Sets the minimum distance defining clash between ligand heavy atoms and protein heavy atoms. New analogs with atoms closer than this cutoff to the active-site protein are marked as clashing, and eventually discarded from the hitlist. Default: 2.25.

#### **SetScoreType**

bool SetScoreType (const unsigned)

Sets the method to be used for scoring overlap between the query fragment and the replacement fragment. Possible choices of methods are described in OEBroodScoreType. Default: ROCS.

## 3.1.11 OEBroodHit

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

#### class OEBroodHit

This class defines objects that contains results corresponding to a generated Brood hit from bioisosteric replacement.

#### The OEBroodHit class defines the following public methods:

- · GetAbbottBioScore
- · GetAromaticRingCount
- · GetAttachScore
- GetBeliefScore
- · GetColorScore
- · GetComboScore
- GetComplexity
- · GetETAttachScore
- · GetETComboScore
- GetETPBScore
- GetETShapeScore
- · GetEgan
- GetFragSmiles
- · GetFrequency
- · GetHeavyCount
- · GetIdeaGroup
- · GetIdeaRank
- · GetLipinskiAcc
- · GetLipinskiDon
- · GetLipinskiFail
- · GetLocalStrain
- GetMol
- · GetMolTanimotoCombo
- · GetMolWt
- · GetRingCount
- · GetRingRatio
- · GetRotorCount
- · GetShapeScore

- · GetSourceMolLabel
- · GetSourceMolSmiles
- $\bullet$  Get TPSA
- · GetVeber
- · GetXLogP
- · Getfsp3C

```
OEBroodHit()
OEBroodHit (const OEBroodHit &)
```

Default and copy constructors.

#### operator=

OEBroodHit & operator= (const OEBroodHit &)

Assignment operator.

#### **GetAbbottBioScore**

double GetAbbottBioScore() const

Returns the Abbott bioavailability socre of the generated molecule.

#### **GetAromaticRingCount**

unsigned GetAromaticRingCount () const

Returns the number of aromatic rings in the generated molecule.

#### **GetAttachScore**

double GetAttachScore() const

Returns the attachment score corresponding to fragment matching.

#### **GetBeliefScore**

double GetBeliefScore() const

Returns the Belief score of the generated molecule.

#### **GetColorScore**

double GetColorScore() const

Returns the color score corresponding to fragment matching.

#### **GetComboScore**

double GetComboScore() const

Returns the combo (shape+color) score corresponding to fragment matching.

#### **GetComplexity**

double GetComplexity() const

Returns the complexity of the generated molecule.

#### **GetETAttachScore**

double GetETAttachScore() const

Returns the electrostatic attachment score corresponding to fragment matching. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### **GetETComboScore**

double GetETComboScore() const

Returns the electrostatic combo (shape+et) score corresponding to fragment matching. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### **GetETPBScore**

double GetETPBScore() const

Returns the electrostatic Possion-Boltzmann score corresponding to fragment matching. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### **GetETShapeScore**

double GetETShapeScore() const

Returns the electrostatic shape score corresponding to fragment matching. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### GetEgan

unsigned GetEgan () const

Returns the Egan bioavailability score of the generated molecule.

#### **GetFragSmiles**

std::string GetFragSmiles() const

Returns the SMILES string corresponding to the replacement fragment.

#### **GetFrequency**

unsigned GetFrequency () const

Returns the frequency of the replacement fragment, in the database.

#### **GetHeavyCount**

unsigned GetHeavyCount () const

Returns the number of heavy atoms in the generated molecule.

#### **GetIdeaGroup**

unsigned GetIdeaGroup() const

Returns the index of the idea group the generated molecule belongs to.

#### **GetIdeaRank**

unsigned GetIdeaRank() const

Returns the rank of generated molecule, within the idea group it belongs to.

#### **GetLipinskiAcc**

unsigned GetLipinskiAcc() const

Returns the number of Lipinski donors in the generated molecule.

#### **GetLipinskiDon**

unsigned GetLipinskiDon() const

Returns the number of Lipinski acceptors in the generated molecule

#### **GetLipinskiFail**

unsigned GetLipinskiFail() const

Returns the number of Lipinski rule-of-five failures in the generated molecule

#### **GetLocalStrain**

double GetLocalStrain() const

Returns the calculated local strain in the genrated molecule.

#### **GetMol**

const OEChem:: OEGraphMol & GetMol() const

Returns the generated hit molecule.

#### **GetMolTanimotoCombo**

double GetMolTanimotoCombo() const

Returns the tanimoto combo (Shape+color) score of the molecule against the query molecule.

#### **GetMolWt**

double GetMolWt () const

Returns the molecular weight of the genrated molecule.

### **GetRingCount**

unsigned GetRingCount () const

Returns the number of rings in the genrated molecule.

#### **GetRingRatio**

double GetRingRatio() const

Returns the ratio of ring atoms vs heavy atoms in the genrated molecule.

#### **GetRotorCount**

unsigned GetRotorCount () const

Returns the number of rotors in the genrated molecule.

#### **GetShapeScore**

double GetShapeScore() const

Returns the shape score corresponding to fragment matching.

#### **GetSourceMolLabel**

std::string GetSourceMolLabel() const

Returns the labels of the source molecules, associated with the replacement fragment.

#### **GetSourceMolSmiles**

std::string GetSourceMolSmiles() const

Returns the SMILES of the source molecules, associated with the replacement fragment.

#### **GetTPSA**

double GetTPSA() const

Returns the calculated topological polar surface area of the genrated molecule.

#### **GetVeber**

unsigned GetVeber() const

Returns the Veber bioavailability score of the genrated molecule.

#### **GetXLogP**

double GetXLogP() const

Returns the calculated LogP of the genrated molecule.

#### Getfsp3C

double Getfsp3C() const

Returns the fraction of sp3 hybridized carbon atoms in the generated molecule.

### 3.1.12 OEBroodHitlistOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodHitlistOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for generating a hitlist in OEHitlistBuilder from a set of brood scores.

The OEBroodHitlistOptions class defines the following public methods:

- · GetBuildOptions and SetBuildOptions
- · GetGenerateIdea and SetGenerateIdea
- GetMaxHits and SetMaxHits

#### **Constructors**

```
OEBroodHitlistOptions()
OEBroodHitlistOptions (const OEBroodHitlistOptions &)
```

Default and copy constructors.

#### operator=

OEBroodHitlistOptions &operator=(const OEBroodHitlistOptions &)

Assignment operator.

#### **GetBuildOptions**

OEBroodBuildOptions& GetBuildOptions() const OEBroodBuildOptions& GetBuildOptions() const

See SetBuildOptions method.

#### **GetGenerateIdea**

bool GetGenerateIdea() const

See SetGenerateIdea method.

#### **GetMaxHits**

unsigned GetMaxHits() const

See SetMaxHits method.

#### **SetBuildOptions**

**void** SetBuildOptions (const OEBroodBuildOptions&)

Sets *options* related to building molecule with replaced fragment.

#### **SetGenerateIdea**

bool SetGenerateIdea (const bool)

Sets if Cluster information should be created on created hitlist. Default: True.

#### **SetMaxHits**

bool SetMaxHits (const unsigned)

Sets the Number of maximum hits to be generated. Default: 1000.

## 3.1.13 OEBroodMolBuilder

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in  $C++$  and Python.

class OEBroodMolBuilder

This class defines interface for building a fragment replaced molecule with 3D coordinates, from a OEBroodScore.

The OEBroodMolBuilder class defines the following public methods:

 $\bullet$  Build

#### **Constructors**

```
OEBroodMolBuilder (const OEBroodQuery &query)
OEBroodMolBuilder (const OEBroodQuery & query,
                 const OEBroodGeneralOptions&)
OEBroodMolBuilder (const OEBroodQuery & query,
                 const OEBroodGeneralOptions &, const OEBroodBuildOptions&)
```

Constructors.

#### **Build**

```
unsigned Build (const OEBroodScore& score, OEBroodHit& hit)
unsigned Build (OEChem:: OEMolBase& mol) ;
```

Builds a fragment replaced 3D Molecule. The first overload generates a corresponding hit data from the specified OEBroodScore. The second overload works directly with a fragment replaced molecule.

. meta::

keywords OEBroodOverlay, BroodOverlay

## 3.1.14 OEBroodOverlay

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodOverlay: public OEBroodOverlayBase

This class defines interface for fragment overlay optimization against a *Brood Query*.

The OEBroodOverlay class defines the following public methods:

- · Overlay
- SetupRef

```
OEBroodOverlay()
OEBroodOverlay (const OEBroodGeneralOptions&)
OEBroodOverlay(const OEBroodGeneralOptions&, const OEBroodScoreOptions&)
```

Constructors.

#### **Overlay**

```
std::vector<OEBroodScore> Overlay(const OEBroodDBPacket&)
unsigned Overlay (std::vector<OEBroodScore>&, const OEBroodDBPacket&)
unsigned Overlay (OEChem:: OEMCMolBase & fragment, OEBroodScore& score)
```

Performs overlay optimization against the fragments specified. The first two overloads perform optimization against all the fragments in the contained OEBroodDBPacket, and returns a vector of OEBroodScore corresponding to optimization and scoring. The third overload performs optimization against the specified fragment and populates the specified OEBroodScore with optimization results. Both the second and third overloads return the status of optimization corresponding to OEBroodStatusCode.

#### **SetupRef**

unsigned SetupRef (const OEBroodQuery & query)

Sets overlay optimization with the desired *OEBroodQuery.* Method returns up the OEBroodStatusCode\_Success if the initialization is successful, otherwise returns an error code from the OEBroodStatusCode namespace.

. meta::

keywords OEBroodOverlayBase, BroodOverlayBase

## 3.1.15 OEBroodOverlayBase

**Attention:** This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodOverlayBase

This is a base class for fragment overlay optimization.

The OEBroodOverlayBase class defines the following public methods:

- · Overlay
- · Transform

#### **Overlay**

unsigned Overlay (OEChem:: OEMCMolBase & fragment, OEBroodScore& score)

Performs overlay optimization of the fragment specified. Method populates the specified OEBroodScore with optimization results. The returns value if the status of optimization corresponding to  $OEBroodStatusCode$ .

#### **Transform**

```
bool Transform (OEChem:: OEMCMolBase & fragment)
```

Transforms the fragment to optimized overlay position.

### 3.1.16 OEBroodQuery

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodQuery

This class defines objects that represent a Brood query.

#### The OEBroodQuery class defines the following public methods:

- · GetAttachCount
- · GetHeavyCount
- · HasProtein
- $\bullet$  *Init*

#### **Constructors**

```
OEBroodQuery()
OEBroodQuery(const OEBroodQuery &)
```

Default and copy constructors.

#### operator=

OEBroodQuery & operator=(const OEBroodQuery &)

Assignment operator.

#### **GetAttachCount**

unsigned GetAttachCount () const

Returns the number of attachment points in the query fragment.

#### **GetHeavyCount**

unsigned GetHeavyCount () const

Returns the number of heavy atoms in the query fragment.

#### **HasProtein**

bool HasProtein() const

Returns true if the query contains an associated protein.

#### Init

unsigned Init (const OEChem:: OEMCMolBase & queryMol)

Initializes the query from contents in the specified *query molecule*. A *query molecule* is an OEMol containing a set of specific data tags. The method returns OEBroodStatusCode\_Success if the initialization is successful, otherwise it returns an error code from the OEBroodStatusCode namespace.

### 3.1.17 OEBroodScore

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodScore

This class defines objects that contains results corresponding to a bioisosteric fragment overlap.

The OEBroodScore class defines the following public methods:

- · GetAttachCount
- · GetAttachScore
- · GetColorScore
- · GetComboScore
- · GetETAttachScore
- · GetETComboScore
- · GetETPBScore
- · GetETShapeScore

- GetEnergy
- GetFrag
- GetFragMol
- · GetShapeScore
- · GetStatus
- $-Load$
- ToRecord
- · GetShapeScore

```
OEBroodScore()
OEBroodScore(const OEBroodScore &)
```

Default and copy constructors.

#### operator=

```
OEBroodScore & operator=(const OEBroodScore &)
```

Assignment operator.

#### **GetAttachCount**

unsigned GetAttachCount () const

#### **GetAttachScore**

double GetAttachScore() const

Returns the attachment score corresponding to fragment overlay.

#### **GetColorScore**

double GetColorScore() const

Returns the color score corresponding to fragment overlay.

#### **GetComboScore**

double GetComboScore() const

Returns the combo (shape+color) score corresponding to fragment overlay.

#### **GetETAttachScore**

double GetETAttachScore() const

Returns the electrostatic attachment score corresponding to fragment overlay. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### **GetETComboScore**

double GetETComboScore() const

Returns the electrostatic combo (shape+et) score corresponding to fragment overlay. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### **GetETPBScore**

double GetETPBScore() const

Returns the electrostatic Possion-Boltzmann score corresponding to fragment overlay. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### **GetETShapeScore**

```
double GetETShapeScore() const
```

Returns the electrostatic shape score corresponding to fragment overlay. This value would be 0.0 is the ET mode was not used during overlay and/or scoring.

#### **GetEnergy**

double GetEnergy () const

#### **GetFrag**

const OEMol& GetFrag()

Returns the generated molecule with fragment replacement.

#### **GetFragMol**

```
bool GetFragMol(OEChem:: OEMolBase&) const
```

Returns a bool and loads the input (with the generated molecule with fragment replacement).

#### **GetShapeScore**

double GetShapeScore() const

Returns the shape score corresponding to fragment overlay.

#### **GetStatus**

```
unsigned GetStatus() const
```

Returns the status of fragment overlay. Method returns OEBroodStatusCode\_Success if the overlay was successful, otherwise returns an error code from the OEBroodStatusCode namespace.

#### Load

```
bool Load(const OEDataFlow:: OERecord &)
```

Loads contents of OEBroodScore from OERecord.

#### **ToRecord**

**bool** ToRecord (OEDataFlow:: OERecord &) const

Saves the contents of OEBroodScore into a OERecord.

## 3.1.18 OEBroodScoreOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEBroodScoreOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for finding bioisosteric fragment replacement matches, used with scoring fragments while performing overlay optimization with OEBroodOverlay.

The OEBroodScoreOptions class defines the following public methods:

- · GetUseBondOrder and SetUseBondOrder
- · GetUseProperty and SetUseProperty
- · GetCheckGeometry and SetCheckGeometry
- · GetAttachCutoff and SetAttachCutoff

- GetShapeCutoff and SetShapeCutoff
- GetRingOnly and SetRingOnly
- · GetPropertyOptions and SetPropertyOptions

```
OEBroodScoreOptions()
OEBroodScoreOptions (const OEBroodScoreOptions &)
```

Default and copy constructors.

#### operator=

OEBroodScoreOptions &operator=(const OEBroodScoreOptions &)

Assignment operator.

#### **GetUseBondOrder**

bool GetUseBondOrder() const

See SetUseBondOrder method.

#### **GetUseProperty**

bool GetUseProperty() const

See SetUseProperty method.

### **GetCheckGeometry**

bool GetCheckGeometry () const

See SetCheckGeometry method.

#### **GetAttachCutoff**

double GetAttachCutoff() const

See SetAttachCutoff method.

#### **GetShapeCutoff**

double GetShapeCutoff() const

See Set ShapeCut of f method.

#### **GetRingOnly**

int GetRingOnly() const

See SetRingOnly method.

#### **GetPropertyOptions**

```
OEMolPropertyOptions& GetPropertyOptions()
const OEMolPropertyOptions& GetPropertyOptions() const
```

See SetPropertyOptions method.

#### **SetUseBondOrder**

bool SetUseBondOrder (const bool)

Sets if Same attachment bond order should be required for a possible match. Default: True.

#### **SetUseProperty**

bool SetUseProperty (const bool)

Sets if Fragment proterty should be checked for a possible match. Default: False.

#### **SetCheckGeometry**

bool SetCheckGeometry (const bool)

Sets if Minimal geometric difference should be required for a possible match. Default: True.

#### **SetAttachCutoff**

bool SetAttachCutoff (const double)

Sets the Minimum acceptable attachment tanimoto for a possible match. Default: 0.78.

#### **SetShapeCutoff**

bool SetShapeCutoff (const double)

Sets the Minimum acceptable shape tanimoto for a possible match. Default: 0.6.

#### **SetRingOnly**

bool SetRingOnly (const int)

Sets the requirement for rings in selecting a fragment. This flag has to do with a count of the number of ring atoms in the shortest path between attachment points in a fragment. In cases with more than 2 attachment points, all shortest paths are calculated and the number of ring atoms is summed. Default: -2

#### **SetPropertyOptions**

void SetPropertyOptions (const OEMolPropertyOptions&)

Sets *options* related to required molecular property values.

## 3.1.19 OEDBBuffer

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

#### class OEDBBuffer

This class defines objects representing a Brood database held in memory. This is suitable for generating a database from a small set of molecules, to be used on-the-fly, without storing it on disk.

#### The OEDBBuffer class defines the following public methods:

- $\bullet$  Add
- Finalize
- · GetPackets

#### **Constructors**

OEDBBuffer()

Constructor.

#### **Add**

**bool** Add (OEChem:: OEMCMolBase &mol)

Adds the specified fragment into the database.

#### **Finalize**

bool Finalize()

Finalizes the database. This method must be called before packets can be retrieved from the database.

#### **GetPackets**

const std::vector<OEBroodDBPacket> &GetPackets() const

Returns the data packets from the database.

### 3.1.20 OEDBBuilder

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

#### class OEDBBuilder

This class defines interface for building two-dimensional Brood fragments database.

#### The OEDBBuilder class defines the following public methods:

- $\bullet$  Add
- · AddCSV
- · Expand
- $•$  Filter
- Generate
- GetFrag
- · GetFragSmiles
- · GetFragSmilesCSV
- · GetFrags
- · NumFrags
- Screen

OEDBBuilder()

Constructor.

#### **Add**

```
bool Add (OEChem:: OEMCMolBase & frag)
bool Add(OESystem::OEIter<OEChem::OEMCMolBase> &frag)
bool Add (const std:: string& smiles);
bool Add (const std:: vector<std:: string>& vecSmiles) ;
```

Add the specified fragment(s) to the database. In the SMILES based overloads, fragment SMILES in the format as obtained from GetFragSmiles are expected.

#### **AddCSV**

bool AddCSV (const std:: vector<std:: string>& vecSmiles) ;

Add fragments from the specified CSV SMILES strings, SMILES as obtained from GetFragSmilesCSV is expected.

#### **Expand**

bool Expand (const OEConfGen:: OEFlipperOptions& opts);

Expands the database by stereo-enumerating the fragments curently contained.

#### **Filter**

bool Filter (OEMolProp:: OEFilter& filter);

Filters the database fragments curently contained.

#### Generate

bool Generate (const OEChem:: OEMolBase& mol) ;

Generate fragment from the specified molecule and add the generated fragment(s) to the database.

#### **GetFrad**

bool GetFrag (OEChem:: OEMCMolBase &mol, const std:: string &smiles) const

Obtains the fragment defined by the specified SMILES string. Method returns false if a fragment with specified SMILES does not exist. SMILES in the format as obtained from  $GetFragSmiles$  is expected.

#### **GetFragSmiles**

```
std::vector<std::string> GetFragSmiles() const
bool GetFragSmiles(std::vector<std::string>&) const
```

Returns the SMILES strings corresponding to the current database.

#### **GetFragSmilesCSV**

```
std::vector<std::string> GetFragSmilesCSV() const
bool GetFragSmilesCSV(std::vector<std::string>&) const
```

Returns the CSV SMILES strings corresponding to the current database. The CSV SMILES contains SMILES of the fragment in a special comma-separated string format.

#### **GetFrags**

OESystem:: OEIterBase<OEChem:: OEMCMolBase> \*GetFrags() const

Returns the two-dimensional fragments corresponding to the current database.

#### **NumFrags**

unsigned NumFrags() const

Returns the number of fragments corresponding to the current database.

#### **Screen**

**bool** Screen (const OEDBScreenOptions& opts)

Screens the fragments in the current database.

## 3.1.21 OEDBReader

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEDBReader

This class defines interface accessing a Brood fragments database from disk.

#### The OEDBReader class defines the following public methods:

- GetFragCount
- GetIndices
- · GetNextPacket
- $\bullet$  Tnit

#### **Constructors**

OEDBReader()

Constructor.

#### **GetFragCount**

unsigned GetFragCount () const

Returns the number of fragments in the database, the reader is currently initialized with.

#### **GetIndices**

const std::vector<unsigned> &GetIndices() const

Returns the indices of the databse, the reader is currently initialized with.

#### **GetNextPacket**

**bool** GetNextPacket (OEBroodDBPacket&)

Obtains the next available database packet to be processed.

Init

```
bool Init (const std:: string &prefix,
          const std:: vector<unsigned> &vecIdx)
bool Init (const std:: string &prefix, OEBroodQuery &query,
          const OEBroodGeneralOptions& GeneralOpts = OEBroodGeneralOptions())
```

Initializes the reader with database specified by *prefix* folder name. The first overload sets up the reader to load all of the data packets available from the segments of database specified by the indices. The second overload identifies the database indices relevent to the *query* and the general options, and sets up the reader to only load the corresponding data packets.

## 3.1.22 OEDBScreenOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEDBScreenOptions : public OESystem: : OEOptions

This class provides an interface to setup options related to screening two-dimensional Brood databases in OEDB-Builder.

#### The OEDBScreenOptions class defines the following public methods:

- GetMinFreqHeavy and SetMinFreqHeavy
- GetMinFrequency and SetMinFrequency

#### **Constructors**

```
OEDBScreenOptions()
OEDBScreenOptions (const OEDBScreenOptions&)
```

Default and copy constructors.

#### operator=

OEDBScreenOptions & operator= (const OEDBScreenOptions&)

Assignment operator.

#### **GetMinFregHeavy**

unsigned GetMinFreqHeavy () const

See SetMinFreqHeavy method.

#### **GetMinFrequency**

unsigned GetMinFrequency () const

See SetMinFrequency method.

#### **SetMinFreqHeavy**

bool SetMinFreqHeavy (const unsigned)

Sets the fragment size defined by the number of heavy atoms affecting minimum frequency. The minimum fre*quency* is only applicable to fragments larger this size defined here. **Default: 1.** 

#### **SetMinFrequency**

bool SetMinFrequency (const unsigned)

Sets the Minimum frequency required for a fragment to be kept. The Minimum frequency is only applicable to fragments larger than size defined in SetMinFreqHeavy. The frequency is the number of parent molecule a specific fragment belongs to, in a database. A value of zero indicates that all fragments should be kept. Default: 0.

### 3.1.23 OEDBWriter

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEDBWriter

This class defines interface for writing a Brood database into a disk.

The OEDBWriter class defines the following public methods:

- $•$  Finish
- $\bullet$  Init
- $Write$

OEDBWriter()

Constructor.

#### **Finish**

bool Finish()

Close database files and finalize the database. Method must be called to have a proper database.

#### Init

bool Init (const std:: string &prefix, unsigned maxBufferSize)

Initialize the database for writing. The parameter prefix refers to the database folder name and file prefixes, and maxBufferSize refers to the maximum size of buffer for contents of each file before flashing.

#### **Write**

**bool** Write (OEChem:: OEMCMolBase & mol)

Write the fragment in the database.

## 3.1.24 OEFragConfReader

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

#### class OEFragConfReader

This class defines interface to perfom fragment conformer sampling from provided 3D molecule structures.

#### The OEFragConfReader class defines the following public methods:

- $\bullet$  Init
- $\bullet$  Tnit
- ReadConformers

OEFragConfReader()

Constructor.

Init

**bool** Init (OEChem:: oemolistream &ifs)

Initializes the reader with 3D molecules from which to sample fragment conformers.

#### **NumMols**

unsigned NumMols () const

Returns the numbers of molecules obtained during initialization.

#### **ReadConformers**

**bool** ReadConformers (OEChem:: OEMCMolBase & mol) const

Reads fragment conformers from obtained molecule structures and generates fragment conformers.

## 3.1.25 OEFragmentOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEFragmentOptions : public OESystem:: OEOptions

This class provides an interface to setup basic options related to bioisosteric fragment overlap scoring.

The OEFragmentOptions class defines the following public methods:

- · GetMaxChiral and SetMaxChiral
- GetMaxDegree and SetMaxDegree
- GetMaxHeavy and SetMaxHeavy
- · GetMaxMolWt and SetMaxMolWt
- · GetMinDegree and SetMinDegree
- GetMinHeavy and SetMinHeavy
- · GetSingleSourceMol and SetSingleSourceMol
- GetSmarts and SetSmarts
- · SetSmartsFile

```
OEFragmentOptions()
OEFragmentOptions (const OEFragmentOptions &)
```

Default and copy constructors.

#### operator=

OEFragmentOptions & operator=(const OEFragmentOptions &)

Assignment operator.

#### **GetMaxChiral**

unsigned GetMaxChiral() const

See SetMaxChiral method.

#### **GetMaxDegree**

unsigned GetMaxDegree() const

See SetMaxDegree method.

#### **GetMaxHeavy**

unsigned GetMaxHeavy () const

See SetMaxHeavy method.

#### **GetMaxMolWt**

double GetMaxMolWt () const

See SetMaxMolWt method.

#### **GetMinDegree**

unsigned GetMinDegree() const

See SetMinDegree method.

#### **GetMinHeavy**

unsigned GetMinHeavy () const

See SetMinHeavy method.

#### **GetSingleSourceMol**

bool GetSingleSourceMol() const

See SetSingleSourceMol method.

#### **GetSmarts**

std::string GetSmarts() const

See SetSmarts method.

#### **SetMaxChiral**

bool SetMaxChiral (const unsigned)

Sets the maximum allowable number of chiral centers (both atom and bond centers) in the generated fragments. Default: 3.

#### **SetMaxDegree**

bool SetMaxDegree (const unsigned)

Sets the maximum allowable number of attachment points in the generated fragments. Default: 3.

#### **SetMaxHeavy**

bool SetMaxHeavy (const unsigned)

Sets the maximum allowable number of heavy atoms in the generated fragments. Default: 15.

#### **SetMaxMolWt**

bool SetMaxMolWt (const double)

Sets the maximum allowable molecular weight in the generated fragments. Default: 350.

#### **SetMinDegree**

bool SetMinDegree (const unsigned)

Sets the minimum required number of attachment points in the generated fragments. Default: 1.

#### **SetMinHeavy**

bool SetMinHeavy (const unsigned)

Sets the minimum required number of heavy atoms in the generated fragments. Default: 1.

#### **SetSingleSourceMol**

bool SetSingleSourceMol(const bool) const

Sets flag if only a single source molecule is to be stored per fragment. The alternative is to store upto 5 source molecule information. Default: false

#### **SetSmarts**

bool SetSmarts (const std:: string&) const

Sets the SMARTS definition for bonds to break. Built-in methods are recap, rlf, both (both rlf and recap), and all. User-defined set of rules can also be used by passing in a file with the desired SMARTS patterns. Default: all

#### **SetSmartsFile**

bool SetSmartsFile(const OEPlatform::oeostream&) const

Sets the SMARTS definition for bonds to break by passing in a file with the desired SMARTS patterns. This method takes precedence over the Set Smarts method.

 $.$  meta $:$ 

keywords OEFragOverlay, FragOverlay

### 3.1.26 OEFragOverlay

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEFragOverlay: public OEBroodOverlayBase

This class defines interface for fragment overlay optimization against another fragment.

The OEFragOverlay class defines the following public methods:

• GetRefFraq

• SetupRef

The following methods are publicly inherited from OEBroodOverlayBase:

- · Overlay
- · Transform

#### **Constructors**

```
OEFragOverlay()
OEFragOverlay (const OEBroodGeneralOptions&)
OEFragOverlay (const OEBroodGeneralOptions&, const OEBroodScoreOptions&)
```

Constructors.

#### **GetRefFrag**

bool GetRefFrag(OEChem:: OEMolBase& fragment)

Gets the reference fragment currently set to perform overlay. Method returns False if a reference was not currently set.

#### **SetupRef**

unsigned SetupRef (const OEChem:: OEMolBase& fragment)

Sets up the overlay optimization with the desired fragment molecule. Method returns OEBroodStatusCode\_Success if the initialization is successful, otherwise returns an error code from the OEBroodStatusCode namespace.

## 3.1.27 OEHitlistBuilder

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

#### class OEHitlistBuilder

This class defines interface for generating a hitlist from calculated :ref: Brood scores <OE-Bioisostere\_OEBroodScore>.

The OEHitlistBuilder class defines the following public methods:

- · AddScores
- $\bullet$  Build
- · GetAddCount
- · GetBumpCount
- · GetDeleteCount

- · GetDuplicateCount
- · GetHitCount
- $\bullet$  GetHits
- · GetInitHitCount
- · GetSecDuplicateCount
- · GetStrainCount
- · GetUnstableCount

```
OEHitlistBuilder (const OEBroodQuery &query)
OEHitlistBuilder (const OEBroodQuery & query,
                 const OEBroodGeneralOptions&)
OEHitlistBuilder (const OEBroodQuery & query,
                 const OEBroodGeneralOptions&, const OEBroodHitlistOptions&)
```

Constructors.

#### **AddScores**

```
bool AddScores (const std:: vector<OEBroodScore> &)
```

Adds the specified scores for building hitlist.

#### **Build**

 $bool$  Build()

Builds the hitlist. Method should be called after all the scores have been added via AddScores.

#### **GetAddCount**

unsigned GetAddCount () const

Returns the total number of scores added.

#### **GetBumpCount**

unsigned GetBumpCount () const

Returns the total number of matches that were rejected due to bumping with protein.

#### **GetDeleteCount**

unsigned GetDeleteCount () const

Returns the total number of matches that were deleted.

#### **GetDuplicateCount**

unsigned GetDuplicateCount () const

Returns the total number of matches that were marked as duplicate.

#### **GetHitCount**

unsigned GetHitCount () const

Returns the total number of generated hits in the hitlist.

#### **GetHits**

```
std::vector<OEBroodHit> GetHits() const
bool GetHits(std::vector<OEBroodHit>&) const
```

Returns the generated hits.

#### **GetInitHitCount**

unsigned GetInitHitCount () const

Returns the initial size of the hitlist.

#### **GetMatchCount**

unsigned GetMatchCount () const

Returns the total number of matches found.

#### **GetSecDuplicateCount**

unsigned GetSecDuplicateCount () const

Returns the number of secondary duplicates.

#### **GetStrainCount**

unsigned GetStrainCount () const

Returns the number of matches rejected due to strain.

#### **GetUnstableCount**

unsigned GetUnstableCount () const

Returns the number of matches rejected due to unstable bonds.

## 3.1.28 OEMolPropertyOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEMolPropertyOptions : public OESystem: : OEOptions

This class provides an interface to set up options related to medicinal chemistry property limits during fragment replacement scoring.

#### The OEMolPropertyOptions class defines the following public methods:

- · GetEganEgg and SetEganEgg
- · GetExtrinsicMaxOptions and SetExtrinsicMaxOptions
- GetExtrinsicMinOptions and SetExtrinsicMinOptions
- · GetIntrinsicMaxOptions and SetIntrinsicMaxOptions
- · GetIntrinsicMinOptions and SetIntrinsicMinOptions
- · GetVeber and SetVeber

#### **Constructors**

```
OEMolPropertyOptions (const unsigned)
OEMolPropertyOptions (const OEMolPropertyOptions \&)
```

Default and copy constructors.

#### operator=

OEMolPropertyOptions &operator=(const OEMolPropertyOptions &)=default

Assignment operator.

#### **GetEganEgg**

bool GetEganEgg() const

See SetEganEgg method.

#### **GetExtrinsicMaxOptions**

```
OEExtrinsicPropOptions& GetExtrinsicMaxOptions()
const OEExtrinsicPropOptions& GetExtrinsicMaxOptions() const
```

See SetExtrinsicMaxOptions method.

#### **GetExtrinsicMinOptions**

```
OEExtrinsicPropOptions& GetExtrinsicMinOptions()
const OEExtrinsicPropOptions& GetExtrinsicMinOptions() const
```

See SetExtrinsicMinOptions method.

#### **GetIntrinsicMaxOptions**

```
OEIntrinsicPropOptions& GetIntrinsicMaxOptions()
const OEIntrinsicPropOptions& GetIntrinsicMaxOptions() const
```

See SetIntrinsicMaxOptions method.

#### **GetIntrinsicMinOptions**

```
OEIntrinsicPropOptions& GetIntrinsicMinOptions()
const OEIntrinsicPropOptions& GetIntrinsicMinOptions() const
```

See Set IntrinsicMinOptions method.

#### **GetVeber**

bool GetVeber() const

See Set Veber method.

#### **SetEganEgg**

bool SetEganEgg (const bool)

Sets the requirement to fulfill the "Egan egg" measure of bioavailability for any selected analog. This measure was published by Bill Egan while at Pharmacopia [Egan-2000] and rejects compounds with a  $LogP > 5.88$  or a PSA > 131.6. Default: true

#### **SetExtrinsicMaxOptions**

**void** SetExtrinsicMaxOptions (const OEExtrinsicPropOptions&)

Sets *options* related to maximum values of the extrinsic molecule properties.

#### **SetExtrinsicMinOptions**

void SetExtrinsicMinOptions (const OEExtrinsicPropOptions&)

Sets *options* related to minimum values of the extrinsic molecule properties.

#### **SetIntrinsicMaxOptions**

**void** SetIntrinsicMaxOptions (const OEIntrinsicPropOptions&)

Sets *options* related to maximum values of the intrinsic molecule properties.

#### **SetIntrinsicMinOptions**

**void** SetIntrinsicMinOptions (const OEIntrinsicPropOptions&)

Sets *options* related to minimum values of the intrinsic molecule properties.

#### **SetVeber**

bool SetVeber (const bool)

Sets the requirement to fulfill the measure of Veber bioavailability for any selected analog. This eliminates compounds with a PSA  $>$  140 or more than 10 rotatable bonds. Veber measured bioavailability during his time at GSK [Veber-2002]. Default: False

## 3.1.29 OEIntrinsicPropOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEIntrinsicPropOptions : public OESystem:: OEOptions

This class provides an interface to set up options related to medicinal chemistry property limits during fragment replacement scoring.

The OEIntrinsicPropOptions class defines the following public methods:

- · GetAromaticJCT and SetAromaticJCT
- GetHeavyAtomCount and SetHeavyAtomCount
- · GetMolWt and SetMolWt
- · GetRotorCount and SetRotorCount
- GetSp3CFrac and SetSp3CFrac
- · GetTPSA and SetTPSA

#### **Constructors**

```
OEIntrinsicPropOptions (const unsigned)
OEIntrinsicPropOptions (const OEIntrinsicPropOptions &)
```

Default and copy constructors.

#### operator=

```
OEIntrinsicPropOptions & operator= (const OEIntrinsicPropOptions &)=default
```

Assignment operator.

#### **GetAromaticJCT**

unsigned GetAromaticJCT() const

See Set Aromatic JCT method.

#### **GetHeavyAtomCount**

unsigned GetHeavyAtomCount() const

See SetHeavyAtomCount method.

#### **GetMolWt**

double GetMolWt () const

See SetMolWt method.

#### **GetRotorCount**

unsigned GetRotorCount() const

See SetRotorCount method.

#### GetSp3CFrac

double GetSp3CFrac() const

See Set Sp3CFrac method.

#### **GetTPSA**

unsigned GetTPSA() const

See Set TPSA method.

#### **SetAromaticJCT**

bool SetAromaticJCT (const unsigned)

Sets the aromatic ring count for any selected analog. The number of aromatic rings is defined as the number of aromatic rings is #aromatic bonds - #aromatic atoms + 1 Default: [Min: 0, Max: 5]

#### **SetHeavyAtomCount**

bool SetHeavyAtomCount (const unsigned)

Sets the number of heavy atoms for any selected analog. Default: [Min: 7, Max: 35]

#### **SetMolWt**

bool SetMolWt (const double)

Sets the required molecular weight for any selected analog. Default: [Min: 100, Max: 500]

#### **SetRotorCount**

bool SetRotorCount (const unsigned)

Sets the required number of rotatable bonds for any selected analog. Default: [Min: 0, Max: 13]

#### SetSp3CFrac

bool SetSp3CFrac(const double)

Sets the required fraction of carbons that are  $sp<sup>3</sup>$  for any selected analog. There is some evidence that increasing the fraction of carbons in a series that are  $sp<sup>3</sup>$  (escaping from "Flatland") improved success in clinical trials [Lovering-2009]. Default: [Min: 0.3, Max: 1.0]

#### **SetTPSA**

bool SetTPSA (const unsigned)

Sets the required topological polar surface area (TPSA) for any selected analog. Default: [Min: 60, Max: 150]

## 3.1.30 OEExtrinsicPropOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEExtrinsicPropOptions : public OESystem: : OEOptions

This class provides an interface to setup options related to medicinal chemistry property limits during fragment replacement scoring.

The OEExtrinsicPropOptions class defines the following public methods:

- GetComplexity and SetComplexity
- · GetFrequency and SetFrequency

- · GetLipinski and SetLipinski
- · GetLipinskiAcc and SetLipinskiAcc
- · GetLipinskiDon and SetLipinskiDon
- · GetLogP and SetLogP
- GetMartin and SetMartin

```
OEExtrinsicPropOptions (const unsigned)
OEExtrinsicPropOptions (const OEExtrinsicPropOptions &)
```

Default and copy constructors.

#### operator=

OEExtrinsicPropOptions & operator=(const OEExtrinsicPropOptions &)=default

Assignment operator.

#### **GetComplexity**

double GetComplexity() const

See SetComplexity method.

#### **GetFrequency**

unsigned GetFrequency () const

See SetFrequency method.

#### **GetLipinski**

unsigned GetLipinski () const

See SetLipinski method.

#### **GetLipinskiAcc**

unsigned GetLipinskiAcc() const

See SetLipinskiAcc method.

#### **GetLipinskiDon**

unsigned GetLipinskiDon() const

See SetLipinskiDon method.

#### **GetLogP**

double GetLogP() const

See SetLogP method.

#### **GetMartin**

double GetMartin() const

See SetMartin method.

#### **SetComplexity**

bool SetComplexity (const double)

Sets the molecular complexity range for any selected analog. Default: [Min: 0.0, Max: 1.0]

#### **SetFrequency**

bool SetFrequency (const unsigned)

Sets the fragment frequency in the database for any selected analog. The frequency is a percentile number indicating the frequency of each fragment normalized relative to the frequency of fragments in the database. Frequency as assessed here is a measure of how common each fragment is among the source molecules. The most commonly occurring fragment would be in the 99th percentile, while the least commonly occurring fragments would be in the 1st percentile. Default: [Min: 0, Max: 100]

#### **SetLipinski**

bool SetLipinski (const unsigned)

Sets the allowed Lipinski violations for any selected analog. In order to segregate molecules that progressed through clinical trials, Lipinski determined that one violation was acceptable, but two were not [Lipinski-1997]. Default: [Min: 0 Max: 1]

#### **SetLipinskiAcc**

bool SetLipinskiAcc(const unsigned)

Sets the required number of Lipinski hydrogen bond acceptors for any selected analog. For the purpose of this measure, H-bond acceptors are determined by the method of Lipinski [Lipinski-1997]. Default: [Min: 2, Max: 11]

#### **SetLipinskiDon**

bool SetLipinskiDon (const unsigned)

Sets the required number of Lipinski hydrogen bond donors for any selected analog. For the purpose of this measure, H-bond donors are determined by the method of Lipinski [Lipinski-1997]. Default: [Min: 1, Max: 8]

#### **SetLogP**

bool SetLogP (const double)

Sets the required calculated LogP for any selected analog. Default: [Min: -1.0, Max: 5.0]

#### **SetMartin**

bool SetMartin (const double)

Sets the required Abbott Bioavailability Score (ABS) for any selected analog. This floating point ABS parameter (range  $0.0-1.0$ ) indicates the minimum allowable probability that F will be  $>10\%$  in rats according the QSAR model developed and published by Yvonne Martin [Martin-2005]. A value of 0.0 will allow all compounds to pass. Default: [Min: 0.2, Max: 1.0]

## **3.2 OEBioisostere Constants**

### 3.2.1 OEBroodBuildType

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

This namespace contains constants.

### Optimize3D

Build 3D molecule with replaced fragment, and optimize

### NoOpt3D

Build 3D molecule with replaced fragment, but skip optimization

### **TwoD**

Build 2D molecule with replaced fragment

## 3.2.2 OEBroodScoreType

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

This namespace contains constants.

## ET

Scoring based on shape and electrostatics

### **LinkOnly**

Scoring based on attachments only

### **ROCS**

Scoring based on shape and color

## 3.2.3 OEBroodStatusCode

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

This namespace contains constants. The error code number can be extracted using OEGetBroodStatus.

#### **BondOrderMismatch**

Mismatch attachment bond orders

### **ExcessStrain**

Excess strain

### **Failed**

Failed

### **Failed2DConstr**

Failed to pass 2D constraint

### **FailedAttachCut**

Failed to pass attachment cutoff

#### **FailedConstraints**

Failed to pass 3D constraints & receptor clash

### **FailedETAttach**

ET attach failure

#### **FailedInit**

Failed to initialize database fragment

### **FailedPropFilter**

Failed to pass property filter

#### **FailedProteinSelect**

Protein receptor/selection failure

#### **FailedQueryInit**

Failed query initialization

#### **FailedQueryMolRead**

Failed to read query molecule

### **FailedRMSCut**

Failed to pass rms Cutoff

#### **FailedShapeCut**

Failed to pass shape Cutoff

#### **HasRingAtoms**

Has ring atoms

#### **InsuffRingAtoms**

Insufficient ring atoms

### **InvalidOptions**

**Invalid Options** 

#### **InvalidScore**

**Invalid Score** 

#### InvalidQuery3D

Query molecule must have 3D coordinates

#### **InvalidQueryAttach**

Query selection contains none or more than 3 attachments

#### **InvalidQueryMol**

Invalid query molecule

#### InvalidQueryNoHeavyAtoms

Query selection contains no heavy atoms

### **InvalidQueryProtein**

Invalid query protein

#### **InvalidQueryRing**

Query selection contains invalid partial ring

#### **InvalidQuerySel**

Query selection does not match molecule

#### **InvalidQuerySelProt**

Invalid query selectivity protein

#### **MissingQueryFrag**

Missing query fragment

#### **NoAttachPt**

No attachment points in database fragment

#### **NoConformers**

No conformers available in DB fragment

#### **NoRingAtoms**

No ring atoms

### **NoSelectionClash**

No selection clash

#### **ProteinBump**

Molecule clashes with protein

#### **ReceptorClash**

Receptor clash

#### **SelectFail**

Molecule not clashing with selection protein

#### **Success**

**Success** 

#### **UnequalAttachPt**

Different number of attachments

#### **UnstableBonds**

Unstable bonds

## **3.3 OEBioisostere Functions**

## 3.3.1 OEBioisostereGetArch

```
const char *OEBioisostereGetArch()
```

Returns the architecture of the current version of the Bioisostere toolkit. Examples include:

- microsoft-win32-x86
- redhat-RHEL5-x86\_64

### 3.3.2 OEBioisostereGetLicensee

```
std::string OEBioisostereGetLicensee()
bool OEBioisostereGetLicensee(std::string &licensee)
```

Returns the LICENSEE from the current valid Bioisostere TK license.

## 3.3.3 OEBioisostereGetPlatform

const char \*OEBioisostereGetPlatform()

Returns the platform, including compiler version, of the current version of the Bioisostere toolkit. Examples include:

- microsoft-win32-msvc9-MD-x86
- redhat-RHEL5-g++4.1-x86  $64$

### 3.3.4 OEBioisostereGetRelease

const char \*OEBioisostereGetRelease()

Returns the version of this toolkit release. For example: 4.0.0.

## 3.3.5 OEBioisostereGetSite

```
std::string OEBioisostereGetSite()
bool OEBioisostereGetSite(std::string &site)
```

Returns the SITE from the current valid Bioisostere TK license.

## 3.3.6 OEBioisostereGetVersion

unsigned int OEBioisostereGetVersion()

Returns the build date of the toolkit as an unsigned int. For example: 20240227.

### 3.3.7 OEBioisosterelsLicensed

```
bool OEBioisostereIsLicensed(const char *feature=0,
                                              unsigned int *expdate=0)
```

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any Bioisostere TK functionality.

The 'feature' argument can be used to check for a valid license to Bioisostere TK along with the following features: 'python'.

The 'expdate' argument can be used to obtain the expiration date of the current Bioisostere TK license.

See also:

· OEChemIsLicensed function

## 3.3.8 OECreateBroodQuery

#### **Query creation without protein**

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

```
unsigned OECreateBroodQuery (OEBroodQuery & query,
                             const OEChem:: OEMolBase &mol,
                             const OEChem:: OEMatchBase & selection)
unsigned OECreateBroodQuery (OEBroodQuery &query,
                             const OEChem:: OEMCMolBase &mol,
                             const OEChem:: OEAtomBondSet &selection)
```

Creates a BROOD Query. The function returns a status code from OEBroodStatusCode.

query

The OEBroodQuery to be created.

mol

The input molecule from which a query is to be created by replacing a fragment of the molecule.

selection

Criteria for selecting atoms and bonds of the molecule that becomes the fragment to be replaced. The atoms and bonds must collectively become a single fragment.

**Query creation with associated protein** 

```
unsigned OECreateBroodQuery (OEBroodQuery & query,
                             const OEChem:: OEMolBase &mol,
                             const OEChem:: OEMatchBase & selection,
                             const OEBio:: OEDesignUnit &du,
                             const unsigned proteinMask)
unsigned OECreateBroodQuery (OEBroodQuery & query,
                             const OEChem:: OEMCMolBase &mol,
                             const OEChem:: OEAtomBondSet &selection,
                             const OEBio:: OEDesignUnit & du,
                             const unsigned proteinMask)
```

Creates a BROOD Query. The function returns a status code from OEBroodStatusCode.

 $du$ 

The OEDesignUnit corresponding to the protein target.

#### proteinMask

Mask to be applied with the OEDesignUnit to determine the protein target.

## 3.3.9 OEGenerateConformers

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

**bool** OEGenerateConformers (OEChem:: OEMCMolBase &mol)

Generates conformers for the specified fragment molecule. Method returns *true* if conformer generation was successful.

### 3.3.10 OEGetBroodStatus

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

std::string OEGetBroodStatus (const unsigned code)

Returns description of *status* corresponding to constants defined in OEBroodStatusCode.

## 3.3.11 OEGetDBIndices

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

```
std::vector<unsigned> OEGetDBIndices(OEBroodQuery &query)
std::vector<unsigned> OEGetDBIndices(OEBroodQuery &query,
                                     onst OEBroodGeneralOptions& opts)
```

Method returns Brood database indices corresponding to the specified OEBroodQuery.

## 3.3.12 OEReadBroodQuery

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

```
unsigned OEReadBroodQuery (OEChem::oemolistream &ifs,
                           OEBroodQuery & query)
```

Reads a OEBroodQuery from the specified stream. Method returns a status code from OEBroodStatusCode.

## 3.3.13 OEWriteBroodQuery

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

```
unsigned OEWriteBroodQuery (OEChem::oemolostream &ofs,
                           const OEBroodQuery & query)
```

Writes a OEBroodQuery to the specified stream. Method returns a status code from OEBroodStatusCode.

## **CHAPTER**

## **FOUR**

## **RELEASE HISTORY**

## 4.1 Bioisostere TK 4.1.0

## 4.1.1 New features

• A new algorithm, based on OEFlexiOverlay, has been adapted in *Build* for optimization of generated poses for molecules obtained from fragment replacement. The new algorithm is more robust for optimization of poses for all geometries, including cyclic peptides.

## 4.1.2 Major bug fixes

- Query building algorithms in OECreateBroodQuery have been improved for robustness. The improved API automatically includes any associated hydrogen atoms as part of the query fragment. Behavior has also been improved to provide better error behavior against invalid selections.
- The new methods SetSingleSourceMol and GetSingleSourceMol have been added to OEFragmentOptions to provide flexibility regarding source molecule storage during database building.

## 4.1.3 Minor bug fixes

• Some memory management issues have been fixed in Build and Generate.

## 4.2 Bioisostere TK 4.0.0

This is the first commercial release of **Bioisostere TK**.

## 4.2.1 New features

The following classes are available as preliminary API with the first release of this toolkit.

- OEBroodBuildOptions
- $\bullet$  OEBroodDBFilter
- OEBroodDBPacket
- OEBroodFragPrep
- OEBroodGeneralOptions

- OEBroodHit
- OEBroodHitlistOptions
- OEBroodOverlay
- OEBroodOverlayBase
- OEBroodQuery
- OEBroodScore
- OEBroodScoreOptions
- OEDBBuffer
- OEDBBuilder
- OEDBReader
- OEDBScreenOptions
- OEDBWriter
- OEFragConfReader
- OEFragmentOptions
- OEFragOverlay
- OEHitlistBuilder
- OEMolPropertyOptions
- OEIntrinsicPropOptions
- OEExtrinsicPropOptions

The following functions are available as preliminary API with the first release of this toolkit.

- OEBioisostereGetArch
- OEBioisostereGetLicensee
- OEBioisostereGetPlatform
- OEBioisostereGetRelease
- OEBioisostereGetSite
- OEBioisostereGetVersion
- OEBioisostereIsLicensed
- OECreateBroodQuery
- OEGenerateConformers
- OEGetBroodStatus
- OEGetDBIndices
- OEReadBroodQuery
- OEWriteBroodQuery

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

## **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

## **CHAPTER**

## **SEVEN**

## **CITATION**

## 7.1 Orion<sup>®</sup> Floes

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

## **7.2 Toolkits and Applications**

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

## **7.3 OpenEye Web Services**

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

## **CHAPTER**

## **EIGHT**

## **TECHNOLOGY LICENSING**

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
|                               |                                                                                     | J,                                                                 |
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
| Babel                         | https://github.com/python-babel/babel                                               | https:/                                                            |
| backcall                      | https://github.com/takluyver/backcall                                               | https:/                                                            |
| backports                     | https://github.com/brandon-rhodes/backports                                         | https:/                                                            |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                             | https:/                                                            |
| base62                        | https://github.com/kare/base62                                                      | https:/                                                            |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                      | https:/                                                            |
| billiard                      | https://github.com/celery/billiard                                                  | https:/                                                            |
| biopython                     | https://biopython.org                                                               | https:/                                                            |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https:/                                                            |
| bitset                        | https://github.com/willf/bitset                                                     | https:/                                                            |
| blas                          | https://www.netlib.org/blas/                                                        | https:/                                                            |
| bleach                        | https://github.com/mozilla/bleach                                                   | https:/                                                            |
| blessings                     | https://github.com/erikrose/blessings                                               | https:/                                                            |
| blinker                       | https://pythonhosted.org/blinker/                                                   | https:/                                                            |
| blosc                         | https://github.com/Blosc/python-blosc                                               | https:/                                                            |
| blosc2                        | https://github.com/Blosc/python-blosc2                                              |                                                                    |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https:/<br>https:/                                                 |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                            |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               |                                                                    |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                                            |
| boto3                         | https://github.com/boto/boto3                                                       | https:/                                                            |
| botocore                      | https://github.com/boto/botocore                                                    | https:/                                                            |
|                               |                                                                                     | https:/                                                            |
| <b>Bottleneck</b>             | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                                            |
| <b>Brotli</b>                 | https://github.com/google/brotli                                                    | https:/                                                            |
| brotli-bin                    | https://github.com/google/brotli                                                    | https:/                                                            |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                                            |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                          | https:/                                                            |
| bson                          | http://github.com/py-bson/bson                                                      | https:/                                                            |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https:/                                                            |
| bzip2                         | https://www.bzip.org                                                                | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| c-ares                        | https://github.com/c-ares/c-ares                                                    |                                                                    |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            |                                                                    |
| cached-property               | https://github.com/pydanny/cached-property                                          |                                                                    |
| cachetools                    | https://github.com/tkem/cachetools                                                  |                                                                    |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           |                                                                    |
| canvas                        | https://github.com/Automattic/node-canvas                                           |                                                                    |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              |                                                                    |
| celery                        | https://github.com/celery/celery                                                    |                                                                    |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         |                                                                    |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                           |                                                                    |
| cffi                          | https://github.com/python-cffi/cffi                                                 |                                                                    |
| cftime                        | https://pypi.org/project/cftime/                                                    |                                                                    |
| chardet                       | https://github.com/chardet/chardet                                                  |                                                                    |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        |                                                                    |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             |                                                                    |
| click                         | https://palletsprojects.com/p/click/                                                |                                                                    |
| click-completion              | https://github.com/click-contrib/click-completion                                   |                                                                    |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   |                                                                    |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      |                                                                    |
| click-repl                    | https://github.com/untitaker/click-repl                                             |                                                                    |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            |                                                                    |
| cmake                         | https://cmake.org/                                                                  |                                                                    |
| colorama                      | https://github.com/tartley/colorama                                                 |                                                                    |
| comm                          | https://github.com/ipython/comm                                                     |                                                                    |
| compose                       | https://github.com/docker/compose                                                   |                                                                    |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        |                                                                    |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      |                                                                    |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     |                                                                    |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            |                                                                    |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           |                                                                    |
| confuse                       | https://github.com/beetbox/confuse                                                  |                                                                    |
| contourpy                     | https://github.com/contourpy/contourpy                                              |                                                                    |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               |                                                                    |
| cryptography                  | https://github.com/pyca/cryptography                                                |                                                                    |
| cssselect2                    | https://github.com/Kozea/cssselect2                                                 |                                                                    |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           |                                                                    |
| cupy-cuda113                  | https://cupy.dev/                                                                   |                                                                    |
| curl                          | https://curl.se                                                                     |                                                                    |
| cycler                        | https://github.com/matplotlib/cycler                                                |                                                                    |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             |                                                                    |
| Cython                        | https://cython.org                                                                  |                                                                    |
| d3                            | https://github.com/mbostock/d3                                                      |                                                                    |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           |                                                                    |
| ddsketch                      | https://github.com/datadog/sketches-py                                              |                                                                    |
| debugpy                       | https://aka.ms/debugpy                                                              |                                                                    |
| decimal                       | https://github.com/shopspring/decimal                                               |                                                                    |
| decorator                     | https://github.com/micheles/decorator                                               |                                                                    |
| deepdiff                      | https://github.com/seperman/deepdiff                                                |                                                                    |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             |                                                                    |
|                               |                                                                                     | J.                                                                 |
| Name of Project               | Website                                                                             | Licen                                                              |
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
|                               |                                                                                     |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https:/                                                            |
| freetype                      | https://freetype.org                                                                | https:/                                                            |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https:/                                                            |
| frozendict                    | <b>Orion Floes</b>                                                                  | https:/                                                            |
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
| $gts$                         | https://sourceforge.net/projects/gts/                                               | https:/                                                            |
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
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            |                                                                    |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  |                                                                    |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     |                                                                    |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst |                                                                    |
| jstat                         | https://github.com/jstat/jstat                                                      |                                                                    |
| jupyter-client                | https://jupyter.org                                                                 |                                                                    |
| jupyter-core                  | https://jupyter.org                                                                 |                                                                    |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           |                                                                    |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       |                                                                    |
| jupyter-server                | http://jupyter.org                                                                  | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            |                                                                    |
| jupyterlab-pygments           | http://jupyter.org                                                                  |                                                                    |
| jupyterlab-widgets            | http://jupyter.org                                                                  |                                                                    |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     |                                                                    |
| jupyter_client                | http://jupyter.org                                                                  |                                                                    |
| jupyter_core                  | http://jupyter.org                                                                  |                                                                    |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    |                                                                    |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          |                                                                    |
| kaleido                       | https://github.com/plotly/Kaleido                                                   |                                                                    |
| keras                         | https://github.com/keras-team/keras                                                 |                                                                    |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   |                                                                    |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           |                                                                    |
| keyring                       | https://github.com/jaraco/keyring                                                   |                                                                    |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      |                                                                    |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        |                                                                    |
| kombu                         | https://kombu.readthedocs.io                                                        |                                                                    |
| krb5                          | https://web.mit.edu/kerberos/                                                       |                                                                    |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            |                                                                    |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    |                                                                    |
| lcms2                         | https://www.littlecms.com                                                           |                                                                    |
| lerc                          | https://github.com/Esri/lerc                                                        |                                                                    |
| libarchive                    | http://www.libarchive.org                                                           |                                                                    |
| libblas                       | https://www.netlib.org/blas/                                                        |                                                                    |
| libbrotlicommon               | https://github.com/google/brotli                                                    |                                                                    |
| libbrotlidec                  | https://github.com/google/brotli                                                    |                                                                    |
| libbrotlienc                  | https://github.com/google/brotli                                                    |                                                                    |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                |
| libclang                      |                                                                                     |                                                                    |
| libcurl                       | https://curl.se/libcurl/                                                            |                                                                    |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               |                                                                    |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          |                                                                    |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              |                                                                    |
| libedit                       | https://thrysoee.dk/editline/                                                       |                                                                    |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          |                                                                    |
| libffi                        | https://github.com/libffi/libffi                                                    |                                                                    |
| libgcrypt                     | https://gnupg.org/software/index.html                                               |                                                                    |
| libgd                         | https://libgd.github.io                                                             |                                                                    |
| libglib                       | https://github.com/PolMine/libglib                                                  |                                                                    |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              |                                                                    |
|                               |                                                                                     | J.                                                                 |
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
| lime                          | https://github.com/marcoter/lime                                                    | https:/                                                            |
| $\overline{\text{lit}}$       | http://llvm.org                                                                     |                                                                    |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https:/                                                            |
| <b>Ilymlite</b>               | http://llvmlite.readthedocs.io                                                      | https:/                                                            |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https:/                                                            |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https:/                                                            |
|                               | https://github.com/sirupsen/logrus                                                  | https:/                                                            |
| logrus                        | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/                                                            |
| logrus-airbrake-hook.v2       |                                                                                     | https:/                                                            |
| 1xml                          | https://lxml.de                                                                     | https:/                                                            |
| $1z4-c$                       | https://www.lz4.org/                                                                | https:/                                                            |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https:/                                                            |
| markdown-it-py                | <b>Orion Floes</b>                                                                  | https:/                                                            |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https:/                                                            |
| matplotlib                    | https://matplotlib.org                                                              | https:/                                                            |
| matplotlib-base               | https://matplotlib.org                                                              | https:/                                                            |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https:/                                                            |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/                                                            |
| mdtraj                        | https://www.mdtraj.org/                                                             | https:/                                                            |
| mdurl                         | <b>Orion Floes</b>                                                                  | https:/                                                            |
| menuinst                      | <b>Orion Floes</b>                                                                  | https:/                                                            |
| mergo                         | https://github.com/imdario/mergo                                                    | https:/                                                            |
| mistune                       | https://github.com/lepture/mistune                                                  | https:/                                                            |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https:/                                                            |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https://                                                           |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https://                                                           |
| ml-dtypes                     | https://github.com/google/ml_dtypes                                                 | https://                                                           |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https://                                                           |
| moment                        | https://github.com/moment/moment                                                    | https://                                                           |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https://                                                           |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https://                                                           |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https://                                                           |
| mpmath                        | http://mpmath.org/                                                                  | https://                                                           |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https://                                                           |
| msgpack                       | https://msgpack.org/                                                                | https://                                                           |
| multidict                     | https://github.com/aio-libs/multidict                                               | https://                                                           |
| multierr                      | https://go.uber.org/multierr                                                        | https://                                                           |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https://                                                           |
| munkres                       | https://software.clapper.org/munkres/                                               | https://                                                           |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https://                                                           |
| namex                         | https://github.com/namex                                                            | https://                                                           |
| nbclassic                     | http://jupyter.org                                                                  | https://                                                           |
| nbclient                      | https://jupyter.org                                                                 | https://                                                           |
| nbconvert                     | https://jupyter.org                                                                 | https://                                                           |
| nbformat                      | http://jupyter.org                                                                  | https://                                                           |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https://                                                           |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https://                                                           |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                           |
| netCDF4                       | https://github.com/Unidata/netcdf4-python                                           | https://                                                           |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https://                                                           |
| networkx                      | https://networkx.org                                                                | https://                                                           |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https://                                                           |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https://                                                           |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https://                                                           |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https://                                                           |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https://                                                           |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https://                                                           |
| nodejs                        | https://nodejs.org/en/                                                              | https://                                                           |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https://                                                           |
| notebook                      | http://jupyter.org                                                                  | https://                                                           |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https://                                                           |
| notebook_shim                 | http://jupyter.org                                                                  | https://                                                           |
| numba                         | https://numba.pydata.org                                                            | https://                                                           |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https://                                                           |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https://                                                           |
| numpy                         | https://numpy.org                                                                   | https://                                                           |
| numpy-base                    | https://numpy.org                                                                   | https://                                                           |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https://                                                           |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://                                                           |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://                                                           |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https://                                                           |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https://                                                           |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
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
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| Oat++                         | https://oatpp.io/                                                                   | https:/                                                            |
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
| openldap                      | https://www.openldap.org/software/repo.html                                         | https:/                                                            |
| OpenMM                        | https://openmm.org                                                                  | https:/                                                            |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https:/                                                            |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https:/                                                            |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                                            |
| openssl                       | https://www.openssl.org                                                             | https:/                                                            |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https:/                                                            |
| OptKing                       | https://github.com/psi-rking/optking                                                | https:/                                                            |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https:/                                                            |
| overrides                     | https://github.com/mkorpela/overrides                                               | https:/                                                            |
| packaging                     | https://github.com/pypa/packaging                                                   | https:/                                                            |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                                            |
| pandas                        | https://pandas.pydata.org                                                           | https:/                                                            |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https://                                                           |
| pango                         | https://pango.gnome.org                                                             | https://                                                           |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https://                                                           |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https://                                                           |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https://                                                           |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https://                                                           |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https://                                                           |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https://                                                           |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https://                                                           |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https://                                                           |
| pcre                          | https://www.pcre.org                                                                | https://                                                           |
| pcre2                         | https://www.pcre.org                                                                | https://                                                           |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https://                                                           |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https://                                                           |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https://                                                           |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https://                                                           |
| pgio                          | https://github.com/jackc/pgio                                                       | https://                                                           |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https://                                                           |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https://                                                           |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https://                                                           |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https://                                                           |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https://                                                           |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https://                                                           |
| Pillow                        | https://python-pillow.org                                                           | https://                                                           |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https://                                                           |
| pip                           | https://pip.pypa.io/                                                                | https://                                                           |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https://                                                           |
| pixman                        | https://pixman.org                                                                  | https://                                                           |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https://                                                           |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https://                                                           |
| plotly                        | https://plotly.com/python/                                                          | https://                                                           |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https://                                                           |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https://                                                           |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https://                                                           |
| pooch                         | https://github.com/fatiando/pooch                                                   | https://                                                           |
| pox                           | https://github.com/uqfoundation/pox                                                 | https://                                                           |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https://                                                           |
| pq                            | https://github.com/lib/pq                                                           | https://                                                           |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https://                                                           |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https://                                                           |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https://                                                           |
| protobuf                      | https://google.golang.org/protobuf                                                  | https://                                                           |
| psi4                          | https://psicode.org                                                                 | https://                                                           |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https://                                                           |
| psycopg2                      | https://psycopg.org/                                                                | https://                                                           |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https://                                                           |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https://                                                           |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https://                                                           |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http://                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| py                            | https://py.readthedocs.io/en/latest/                                                | https:/                                                            |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             | https:/                                                            |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   | https:/                                                            |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           | https:/                                                            |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  | https:/                                                            |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/                                                            |
| pycosat                       | https://github.com/conda/pycosat                                                    | https:/                                                            |
| pycparser                     | https://github.com/eliben/pycparser                                                 | https:/                                                            |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 | https:/                                                            |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           | https:/                                                            |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                | https:/                                                            |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                | https:/                                                            |
| Pygments                      | https://pygments.org                                                                | https:/                                                            |
| pygraphviz                    | https://pygraphviz.github.io                                                        | https:/                                                            |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            | https:/                                                            |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        | https:/                                                            |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  | https:/                                                            |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   | https:/                                                            |
| pymbar                        | https://pymbar.org                                                                  | https:/                                                            |
| pyOpenSSL                     | https://pyopenssl.org/                                                              | https:/                                                            |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/                                                            |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    | https:/                                                            |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 | https:/                                                            |
| pysam                         | https://github.com/pysam-developers/pysam                                           | https:/                                                            |
| PySocks                       | https://github.com/Anorov/PySocks                                                   | https:/                                                            |
| pytables                      | https://www.pytables.org                                                            | https:/                                                            |
| python                        | https://www.python.org/                                                             | https:/                                                            |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          | https:/                                                            |
| python-constraint             | https://github.com/python-constraint/python-constraint                              | https:/                                                            |
| python-dateutil               | https://dateutil.readthedocs.io                                                     | https:/                                                            |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         | https:/                                                            |
| python-ldap                   | https://www.python-ldap.org/                                                        | https:/                                                            |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            | https:/                                                            |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 | https:/                                                            |
| pytz                          | https://pythonhosted.org/pytz                                                       | https:/                                                            |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/                                                            |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  | https:/                                                            |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                 | https:/                                                            |
| pyyaml                        | No longer available                                                                 | https:/                                                            |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             | https:/                                                            |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               | https:/                                                            |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  | https:/                                                            |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        | https:/                                                            |
| ramda                         | https://github.com/ramda/ramda                                                      | https:/                                                            |
| rapidjson                     | https://rapidjson.org/                                                              | https:/                                                            |
| rdkit                         | https://www.rdkit.org                                                               | https:/                                                            |
| re2                           | https://github.com/google/re2                                                       | https:/                                                            |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             | https:/                                                            |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
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
| rich                          | Orion Floes                                                                         | https:/                                                            |
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
| spglib                        | Orion Floes                                                                         | https:/                                                            |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https:/                                                            |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/                                                            |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/                                                            |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/                                                            |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/                                                            |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/                                                            |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          |                                                                    |
| sqlite                        | https://sqlite.org/index.html                                                       |                                                                    |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            |                                                                    |
| stack-data                    | https://github.com/alexmojaki/stack_data                                            |                                                                    |
| starfile                      | https://github.com/alisterburt/starfile                                             |                                                                    |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          |                                                                    |
| structlog                     | https://www.structlog.org/                                                          |                                                                    |
| svglib                        | https://github.com/deeplook/svglib                                                  |                                                                    |
| sympy                         | https://sympy.org                                                                   |                                                                    |
| tables                        | https://www.pytables.org/                                                           |                                                                    |
| tabulate                      | https://github.com/astanin/python-tabulate                                          |                                                                    |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                |                                                                    |
| tenacity                      | https://github.com/jd/tenacity                                                      |                                                                    |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           |                                                                    |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           |                                                                    |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           |                                                                    |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            |                                                                    |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             |                                                                    |
| tensorflow-io-gcs-filesystem  | https://github.com/tensorflow/io-gcs-filesystem                                     |                                                                    |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           |                                                                    |
| termcolor                     | https://github.com/hugovk/termcolor                                                 |                                                                    |
| terminado                     | https://github.com/jupyter/terminado                                                |                                                                    |
| testpath                      | https://github.com/jupyter/testpath                                                 |                                                                    |
| textangular                   | https://github.com/fraywing/textAngular                                             |                                                                    |
| tf_keras                      | https://github.com/tensorflow/tf_keras                                              |                                                                    |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             |                                                                    |
| three                         | https://github.com/mrdoob/three.js                                                  |                                                                    |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                |                                                                    |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  |                                                                    |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             |                                                                    |
| tk                            | https://www.tcl.tk/                                                                 |                                                                    |
| toml                          | https://github.com/toml-lang/toml                                                   |                                                                    |
| tomli                         | https://github.com/hukkin/tomli                                                     |                                                                    |
| toolz                         | https://github.com/pytoolz/toolz                                                    |                                                                    |
| torch                         | https://pytorch.org/                                                                |                                                                    |
| tornado                       | https://www.tornadoweb.org                                                          |                                                                    |
| tqdm                          | https://github.com/tqdm/tqdm                                                        |                                                                    |
| tracy                         | https://github.com/gear-genomics/tracy                                              |                                                                    |
| traitlets                     | https://github.com/ipython/traitlets                                                |                                                                    |
| triton                        | https://github.com/openai/triton/                                                   |                                                                    |
| truststore                    | https://github.com/python/truststore                                                |                                                                    |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               |                                                                    |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             |                                                                    |
| twine                         | https://github.com/pypa/twine                                                       |                                                                    |
| twinj uuid                    | https://github.com/twinj/uuid                                                       |                                                                    |
| types                         | https://github.com/babel/babel                                                      |                                                                    |
| typescript                    | https://github.com/Microsoft/TypeScript                                             |                                                                    |
| typing_extensions             | https://github.com/python/typing                                                    |                                                                    |
| tzdata                        | https://github.com/python/tzdata                                                    |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | https:/                                                            |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | https:/                                                            |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | https:/                                                            |
| uritools                      | https://github.com/tkem/uritools/                                                   | https:/                                                            |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | https:/                                                            |
| vine                          | https://github.com/celery/vine                                                      | https:/                                                            |
| vue                           | https://github.com/vuejs/vue                                                        | https:/                                                            |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | https:/                                                            |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | https:/                                                            |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | https:/                                                            |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | https:/                                                            |
| westpa                        | Orion Floes                                                                         | http:/                                                             |
| wheel                         | https://github.com/pypa/wheel                                                       | https:/                                                            |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | https:/                                                            |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | https:/                                                            |
| wsutil                        | https://github.com/yhat/wsutil                                                      | https:/                                                            |
| x/lint                        | https://golang.org/x/lint                                                           | https:/                                                            |
| x/mod                         | https://golang.org/x/mod/semver                                                     | https:/                                                            |
| x/net                         | https://golang.org/x/net                                                            | https:/                                                            |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | https:/                                                            |
| x/sys                         | https://golang.org/x/sys                                                            | https:/                                                            |
| x/text                        | https://golang.org/x/text                                                           | https:/                                                            |
| x/tools                       | https://golang.org/x/tools                                                          | https:/                                                            |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | https:/                                                            |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                               | https:/                                                            |
| xlrd                          | https://github.com/python-excel/xlrd                                                | https:/                                                            |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | https:/                                                            |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | https:/                                                            |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https:/                                                            |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https:/                                                            |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https:/                                                            |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https:/                                                            |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https:/                                                            |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https:/                                                            |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https:/                                                            |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https:/                                                            |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https:/                                                            |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https:/                                                            |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https:/                                                            |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https:/                                                            |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | https:/                                                            |
| xz                            | https://github.com/ulikunitz/xz                                                     | https:/                                                            |
| yaml                          | https://pyyaml.org/                                                                 | https:/                                                            |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  | https:/                                                            |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | https:/                                                            |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | https:/                                                            |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | https:/                                                            |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | https:/                                                            |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | comm                                                               |
| Name of Project               | Website                                                                             | License                                                            |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                                                                |
| zap                           | https://go.uber.org/zap                                                             | https:/                                                            |
| zipp                          | https://github.com/jaraco/zipp                                                      | https:/                                                            |
| zlib                          | https://zlib.net/                                                                   | https:/                                                            |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https:/                                                            |
| zstd                          | https://facebook.github.io/zstd/                                                    | https:/                                                            |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:/                                                            |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:/                                                            |

## **8.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

## **8.1.1 GCC RUNTIME LIBRARY EXCEPTION**

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
                                                                              (continues on next page)
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

## **8.1.2 GNU GENERAL PUBLIC LICENSE**

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

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page)

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

#### See also:

• http://www.gnu.org/licenses/gpl.txt

## **INDEX**

## $\mathsf{A}$

```
Add
   OEBioisostere:: OEDBBuffer, 47
   OEBioisostere:: OEDBBuilder, 49
AddCSV
   OEBioisostere:: OEDBBuilder, 49
AddScores
   OEBioisostere:: OEHitlistBuilder, 60
```

## <sub>R</sub>

brood\_database.py Example Code, 9 brood hitlist.py Example Code, 13 brood\_matching.py Example Code, 16 brood query.py Example Code, 11 Build OEBioisostere:: OEBroodMolBuilder, 38 OEBioisostere:: OEHitlistBuilder, 60

## C

```
Constructors
   OEBioisostere:: OEBroodBuildOptions,
       23OEBioisostere:: OEBroodDBFilter, 25
   OEBioisostere:: OEBroodDBPacket, 26
   OEBioisostere:: OEBroodFragPrep, 28
   OEBioisostere:: OEBroodGeneralOptions,
       28
   OEBioisostere:: OEBroodHit, 31
   OEBioisostere:: OEBroodHitlistOptions, fragment_overlay.py
       36
   OEBioisostere:: OEBroodMolBuilder, 38
   OEBioisostere:: OEBroodOverlay, 38
   OEBioisostere:: OEBroodQuery, 40
   OEBioisostere:: OEBroodScore, 42
   OEBioisostere:: OEBroodScoreOptions,
      45
   OEBioisostere:: OEDBBuffer, 47
   OEBioisostere:: OEDBBuilder, 48
```

```
OEBioisostere:: OEDBReader, 51
OEBioisostere:: OEDBScreenOptions, 52
OEBioisostere:: OEDBWriter, 53
OEBioisostere:: OEExtrinsicPropOptions,
   68
OEBioisostere:: OEFragConfReader, 54
OEBioisostere:: OEFragmentOptions, 55
OEBioisostere:: OEFragOverlay, 59
OEBioisostere:: OEHitlistBuilder, 60
OEBioisostere:: OEIntrinsicPropOptions,
   65
OEBioisostere:: OEMolPropertyOptions,
   62
```

## F

```
Example Code
   brood_database.py, 9
   brood_hitlist.py, 13
   brood_matching.py, 16
   brood_query.py, 11
   fragment_overlay.py, 18
   replace_fragment.py, 20
Expand
   OEBioisostere:: OEDBBuilder, 49
```

## E

```
Filter
   OEBioisostere:: OEDBBuilder, 49
Finalize
   OEBioisostere:: OEDBBuffer, 48
Finish
   OEBioisostere:: OEDBWriter, 54
   Example Code, 18
```

## G

```
Generate
   OEBioisostere:: OEDBBuilder, 49
GetAbbottBioScore
   OEBioisostere:: OEBroodHit, 31
GetAddCount
   OEBioisostere:: OEHitlistBuilder, 60
```

GetAromaticJCT OEBioisostere:: OEIntrinsicPropOptions, 65 GetAromaticRingCount OEBioisostere:: OEBroodHit, 31 GetAttachCount OEBioisostere:: OEBroodQuery, 40 OEBioisostere:: OEBroodScore, 42 GetAttachCutoff OEBioisostere:: OEBroodScoreOptions,  $45$ GetAttachScale OEBioisostere:: OEBroodGeneralOptions, 28 GetAttachScore OEBioisostere:: OEBroodHit, 31 OEBioisostere:: OEBroodScore, 42 GetBeliefScore OEBioisostere:: OEBroodHit, 31 GetBuildOptions OEBioisostere:: OEBroodHitlistOptions, 37 GetBuildType OEBioisostere:: OEBroodBuildOptions, 24 GetBumpCount OEBioisostere:: OEHitlistBuilder, 60 GetBumpRadius OEBioisostere:: OEBroodGeneralOptions, GetFraqMol 29 GetCheckBond OEBioisostere:: OEBroodBuildOptions,  $24$ GetCheckGeometry OEBioisostere:: OEBroodScoreOptions,  $45$ GetColorScore OEBioisostere:: OEBroodHit, 32 OEBioisostere:: OEBroodScore, 42 GetComboScore OEBioisostere:: OEBroodHit, 32 OEBioisostere:: OEBroodScore, 42 GetComplexity OEBioisostere:: OEBroodHit, 32 OEBioisostere:: OEExtrinsicPropOptions, OEBioisostere:: OEBroodHitlistOptions, 68 GetDeleteCount OEBioisostere:: OEHitlistBuilder, 60 GetDuplicateCount OEBioisostere:: OEHitlistBuilder, 61 GetEgan OEBioisostere:: OEBroodHit, 33 GetEganEgg

OEBioisostere:: OEMolPropertyOptions, 63 GetEnergy OEBioisostere:: OEBroodScore, 43 GetETAttachScore OEBioisostere:: OEBroodHit, 32 OEBioisostere:: OEBroodScore, 43 GetETComboScore OEBioisostere:: OEBroodHit, 32 OEBioisostere:: OEBroodScore, 43 GetETPBScore OEBioisostere:: OEBroodHit, 32 OEBioisostere:: OEBroodScore, 43 GetETShapeScore OEBioisostere:: OEBroodHit, 32 OEBioisostere:: OEBroodScore, 43 GetExtrinsicMaxOptions OEBioisostere:: OEMolPropertyOptions, 63 GetExtrinsicMinOptions OEBioisostere:: OEMolPropertyOptions, 63 GetFrag OEBioisostere:: OEBroodScore. 43 OEBioisostere:: OEDBBuilder, 49 GetFragCount OEBioisostere:: OEBroodDBPacket, 27 OEBioisostere:: OEDBReader, 51 OEBioisostere:: OEBroodScore, 43 GetFrags OEBioisostere:: OEDBBuilder, 50 GetFragSmiles OEBioisostere:: OEBroodHit, 33 OEBioisostere:: OEDBBuilder, 50 GetFraqSmilesCSV OEBioisostere:: OEDBBuilder, 50 GetFrequency OEBioisostere:: OEBroodHit, 33 OEBioisostere:: OEExtrinsicPropOptions, 68 Getfsp3C OEBioisostere:: OEBroodHit, 36 GetGenerateIdea 37 GetHeavyAtomCount OEBioisostere:: OEIntrinsicPropOptions, 66 GetHeavyCount OEBioisostere:: OEBroodHit, 33 OEBioisostere:: OEBroodQuery, 41 GetHitCount OEBioisostere:: OEHitlistBuilder, 61

OEBioisostere:: OEFragmentOptions, 56 GetHits GetMinDeqree OEBioisostere:: OEHitlistBuilder, 61 GetIdeaGroup OEBioisostere:: OEFragmentOptions, 56 OEBioisostere:: OEBroodHit, 33 GetMinFreqHeavy GetIdeaRank OEBioisostere:: OEDBScreenOptions, 53 OEBioisostere:: OEBroodHit, 33 GetMinFrequency OEBioisostere:: OEDBScreenOptions, 53 Get Idx OEBioisostere:: OEBroodDBPacket, 27 GetMinHeavy GetIndices OEBioisostere:: OEFragmentOptions, 56 OEBioisostere:: OEDBReader, 51 GetMol GetInitHitCount OEBioisostere:: OEBroodHit, 34 OEBioisostere:: OEHitlistBuilder, 61 GetMolTanimotoCombo GetIntrinsicMaxOptions OEBioisostere:: OEBroodHit, 34 OEBioisostere:: OEMolPropertyOptions, GetMolWt 63 OEBioisostere:: OEBroodHit, 34 GetIntrinsicMinOptions OEBioisostere:: OEIntrinsicPropOptions, OEBioisostere:: OEMolPropertyOptions, 66 63 GetNeutralPH OEBioisostere:: OEBroodBuildOptions, GetLipinski OEBioisostere:: OEExtrinsicPropOptions, 24 68 GetNextPacket GetLipinskiAcc OEBioisostere:: OEDBReader, 51 OEBioisostere:: OEBroodHit, 33 GetPackets OEBioisostere:: OEExtrinsicPropOptions, OEBioisostere:: OEDBBuffer, 48 68 GetPropertyOptions GetLipinskiDon OEBioisostere:: OEBroodScoreOptions, OEBioisostere:: OEBroodHit, 34 46 OEBioisostere:: OEExtrinsicPropOptionsGetRefFrag 68 OEBioisostere:: OEFragOverlay, 59 GetRingCount GetLipinskiFail OEBioisostere:: OEBroodHit, 34 OEBioisostere:: OEBroodHit, 34 GetLocalStrain GetRingOnly OEBioisostere:: OEBroodHit, 34 OEBioisostere:: OEBroodScoreOptions, GetLogP 46 OEBioisostere:: OEExtrinsicPropOptionsGetRingRatio OEBioisostere:: OEBroodHit. 35 69 GetMartin GetRotorCount OEBioisostere:: OEExtrinsicPropOptions, OEBioisostere:: OEBroodHit, 35 69 OEBioisostere:: OEIntrinsicPropOptions, GetMatchCount 66 GetScoreType OEBioisostere:: OEHitlistBuilder, 61 GetMaxChiral OEBioisostere:: OEBroodGeneralOptions, OEBioisostere:: OEFragmentOptions, 56  $29$ GetSecDuplicateCount GetMaxDegree OEBioisostere:: OEFragmentOptions, 56 OEBioisostere:: OEHitlistBuilder, 61 GetMaxHeavy GetShapeCutoff OEBioisostere:: OEFragmentOptions, 56 OEBioisostere:: OEBroodScoreOptions, 45 GetMaxHits OEBioisostere:: OEBroodHitlistOptions, GetShapeScore  $37$ OEBioisostere:: OEBroodHit, 35 GetMaxLocalStrain OEBioisostere:: OEBroodScore, 44 OEBioisostere:: OEBroodBuildOptions, GetSingleSourceMol 24 OEBioisostere:: OEFragmentOptions, 57 GetMaxMolWt GetSmarts

| OEBioisostere::OEFragmentOptions, 57      | OEBioisostere::OEDBBuilder, 50                  |
|-------------------------------------------|-------------------------------------------------|
| GetSourceMolLabel                         | NumMols                                         |
| OEBioisostere::OEBroodHit, 35             | OEBioisostere::OEFragConfReader, 55             |
| GetSourceMolSmiles                        |                                                 |
| OEBioisostere::OEBroodHit, 35             |                                                 |
| GetSp3CFrac                               | OEBioisostere::OEBioisostereGetArch, 76         |
| OEBioisostere::OEIntrinsicPropOptions, 66 | OEBioisostere::OEBioisostereGetLicensee, 76     |
| GetStatus                                 | OEBioisostere::OEBioisostereGetPlatform, 77     |
| OEBioisostere::OEBroodScore, 44           | 77                                              |
| GetStrainCount                            | OEBioisostere::OEBioisostereGetRelease, 77      |
| OEBioisostere::OEHitlistBuilder, 61       | OEBioisostere::OEBioisostereGetSite, 77         |
| GetTautomers                              | OEBioisostere::OEBioisostereGetVersion, 77      |
| OEBioisostere::OEBroodBuildOptions, 24    | OEBioisostere::OEBioisostereIsLicensed, 77      |
| GetTPSA                                   | OEBioisostere::OEBroodBuildOptions, 23          |
| OEBioisostere::OEBroodHit, 35             | Constructors, 23                                |
| GetUnstableCount                          | GetBuildType, 24                                |
| OEBioisostere::OEHitlistBuilder, 62       | GetCheckBond, 24                                |
| GetUseBondOrder                           | GetMaxLocalStrain, 24                           |
| OEBioisostere::OEBroodScoreOptions, 45    | GetNeutralPH, 24                                |
| GetUseProperty                            | GetTautomers, 24                                |
| OEBioisostere::OEBroodScoreOptions, 45    | operator=, 23                                   |
| GetVeber                                  | SetBuildType, 24                                |
| OEBioisostere::OEBroodHit, 35             | SetCheckBond, 25                                |
| OEBioisostere::OEMolPropertyOptions, 63   | SetMaxLocalStrain, 25                           |
| GetXLogP                                  | SetNeutralPH, 24                                |
| OEBioisostere::OEBroodHit, 36             | SetTautomers, 25                                |
| HasProtein                                | OEBioisostere::OEBroodBuildType, 70             |
| OEBioisostere::OEBroodQuery, 41           | OEBioisostere::OEBroodBuildType::NoOpt3D, 71    |
|                                           | OEBioisostere::OEBroodBuildType::Optimize3D, 70 |
|                                           | OEBioisostere::OEBroodBuildType::TwoD, 71       |
|                                           | OEBioisostere::OEBroodDBFilter, 25              |
|                                           | Constructors, 25                                |

Setup, 26

GetIdx, 27

Load,  $27$ 

Prep, 28

28

```
Init
   OEBioisostere:: OEBroodQuery, 41
   OEBioisostere:: OEDBReader, 51
   OEBioisostere:: OEDBWriter, 54
   OEBioisostere:: OEFragConfReader, 55
IsValid
   OEBioisostere:: OEBroodDBPacket, 27
```

## $\mathsf{L}$

Load OEBioisostere:: OEBroodDBPacket, 27 OEBioisostere:: OEBroodScore, 44

## $\mathsf{N}$

NumFrags

operator=, 25 OEBioisostere:: OEBroodDBPacket, 26 Constructors, 26 GetFragCount, 27 IsValid, 27 operator=, 26 ToRecord, 27 OEBioisostere:: OEBroodFragPrep, 27 Constructors, 28 OEBioisostere:: OEBroodGeneralOptions, **Index** 

Constructors, 28 GetAttachScale.28 GetBumpRadius, 29 GetScoreType, 29 operator=, 28 SetAttachScale, 29 SetBumpRadius, 29 SetScoreType, 29 OEBioisostere:: OEBroodHit, 29 Constructors, 31 GetAbbottBioScore, 31 GetAromaticRingCount, 31 GetAttachScore, 31 GetBeliefScore, 31 GetColorScore, 32 GetComboScore, 32 GetComplexity, 32 GetEgan, 33 GetETAttachScore. 32 GetETComboScore, 32 GetETPBScore, 32 GetETShapeScore, 32 GetFragSmiles, 33 GetFrequency, 33 Getfsp3C, 36 GetHeavyCount, 33 GetIdeaGroup, 33 GetIdeaRank, 33 GetLipinskiAcc, 33 GetLipinskiDon, 34 GetLipinskiFail, 34 GetLocalStrain, 34 GetMol, 34 GetMolTanimotoCombo, 34 GetMolWt, 34 GetRingCount, 34 GetRingRatio, 35 GetRotorCount, 35 GetShapeScore, 35 GetSourceMolLabel, 35 GetSourceMolSmiles, 35 GetTPSA, 35 GetVeber, 35 GetXLogP, 36 operator=, 31 OEBioisostere:: OEBroodHitlistOptions, 36 Constructors, 36 GetBuildOptions, 37 GetGenerateIdea, 37 GetMaxHits, 37 operator=, 36 SetBuildOptions, 37 SetGenerateIdea, 37

SetMaxHits, 37 OEBioisostere:: OEBroodMolBuilder, 37 Build. 38 Constructors, 38 OEBioisostere:: OEBroodOverlay, 38 Constructors, 38 Overlay, 39 SetupRef, 39 OEBioisostere:: OEBroodOverlayBase, 39 Overlay, 39 Transform, 40 OEBioisostere:: OEBroodQuery, 40 Constructors, 40 GetAttachCount, 40 GetHeavyCount, 41 HasProtein, 41 Init. 41 operator= $, 40$ OEBioisostere:: OEBroodScore, 41 Constructors, 42 GetAttachCount, 42 GetAttachScore, 42 GetColorScore, 42 GetComboScore. 42 GetEnergy, 43 GetETAttachScore, 43 GetETComboScore, 43 GetETPBScore, 43 GetETShapeScore, 43 GetFrag, 43 GetFragMol, 43 GetShapeScore, 44 GetStatus, 44 Load, 44 operator=, 42 ToRecord, 44 OEBioisostere:: OEBroodScoreOptions, 44 Constructors, 45 GetAttachCutoff, 45 GetCheckGeometry, 45 GetPropertyOptions, 46 GetRingOnly, 46 GetShapeCutoff, 45 GetUseBondOrder, 45 GetUseProperty, 45 operator=, 45 SetAttachCutoff, 46 SetCheckGeometry, 46 SetPropertyOptions, 47 SetRingOnly, 47 SetShapeCutoff, 46 SetUseBondOrder, 46 SetUseProperty, 46 OEBioisostere:: OEBroodScoreType, 71

OEBioisostere::OEBroodScoreType::ET.71 OEBioisostere::OEBroodStatusCode::InvalidOuerySelP OEBioisostere:: OEBroodScoreType:: LinkOnly, 75 OEBioisostere:: OEBroodStatusCode:: InvalidScore, 71 OEBioisostere:: OEBroodScoreType:: ROCS,  $74$  $71$ OEBioisostere:: OEBroodStatusCode:: MissingQueryFrag, OEBioisostere:: OEBroodStatusCode, 71 75 OEBioisostere::OEBroodStatusCode::BondOrdEBMosmatchre::OEBroodStatusCode::NoAttachPt. 72 75 OEBioisostere::OEBroodStatusCode::ExcessOEBadmsostere::OEBroodStatusCode::NoConformers,  $72$ 75 OEBioisostere::OEBroodStatusCode::FailedQEBioisostere::OEBroodStatusCode::NoRingAtoms,  $72$ 75 OEBioisostere::OEBroodStatusCode::Failed0BBonstostere::OEBroodStatusCode::NoSelectionClash,  $72$ 75 OEBioisostere:: OEBroodStatusCode:: Failed@EBach6ustere:: OEBroodStatusCode:: ProteinBump, 72 76 OEBioisostere::OEBroodStatusCode::FailedOEB\$tra@atere::OEBroodStatusCode::ReceptorClash,  $72$ 76 OEBioisostere::OEBroodStatusCode::FailedDEAtoisbstere::OEBroodStatusCode::SelectFail,  $72$ 76 OEBioisostere::OEBroodStatusCode::Failed0HBioisostere::OEBroodStatusCode::Success, 73 76 OEBioisostere::OEBroodStatusCode::FailedDEBpbEi\$betere::OEBroodStatusCode::UnequalAttachPt, 73 76 OEBioisostere::OEBroodStatusCode::FailedDEBtein6efere::OEBroodStatusCode::UnstableBonds,  $73$ 76 OEBioisostere::OEBroodStatusCode::FailedQEBrgIaottere::OECreateBroodQuery,77 73 OEBioisostere:: OEDBBuffer, 47 OEBioisostere:: OEBroodStatusCode:: FailedQue AyMb 4Read, Constructors, 47 73 OEBioisostere:: OEBroodStatusCode:: FailedRMSCTutualize, 48  $73$ GetPackets, 48 OEBioisostere::OEBroodStatusCode::FailedGEBpeCabstere::OEDBBuilder, 48  $73$ Add. 49 OEBioisostere:: OEBroodStatusCode:: HasRingAt&mdslCSV, 49 Constructors. 48 73 OEBioisostere:: OEBroodStatusCode:: InsuffRindTAdpammsl, 49  $74$ Filter. 49 OEBioisostere:: OEBroodStatusCode:: InvalidOptGemexate, 49  $74$ GetFrag, 49 OEBioisostere:: OEBroodStatusCode:: InvalidQueetIDags, 50  $74$ GetFragSmiles, 50 OEBioisostere:: OEBroodStatusCode:: InvalidQueetAttanSmilesCSV, 50 NumFrags, 50 74 OEBioisostere:: OEBroodStatusCode:: InvalidQu&cyMech, 50 OEBioisostere:: OEDBReader, 50 74 OEBioisostere::OEBroodStatusCode::InvalidQueCoyNstHeurtyAtsofis, 74 GetFragCount.51 OEBioisostere:: OEBroodStatusCode:: InvalidQueeyHnotiers, 51  $74$ GetNextPacket.51 OEBioisostere::OEBroodStatusCode::InvalidQudmyRing, 75 OEBioisostere:: OEDBScreenOptions, 52 OEBioisostere:: OEBroodStatusCode:: InvalidQuecoySthuctors, 52 75 GetMinFreqHeavy, 53

GetMinFrequency, 53 operator=, 52 SetMinFreqHeavy, 53 SetMinFrequency, 53 OEBioisostere:: OEDBWriter, 53 Constructors, 53 Finish. 54 Init, 54 Write.54 OEBioisostere:: OEExtrinsicPropOptions, 67 Constructors, 68 GetComplexity, 68 GetFrequency, 68 GetLipinski, 68 GetLipinskiAcc, 68 GetLipinskiDon, 68 GetLogP. 69 GetMartin, 69 operator=, 68 SetComplexity, 69 SetFrequency, 69 SetLipinski, 69 SetLipinskiAcc, 69 SetLipinskiDon, 70 SetLogP, 70 SetMartin, 70 OEBioisostere:: OEFragConfReader, 54 Constructors, 54 Init.55 NumMols.55 ReadConformers. 55 OEBioisostere:: OEFragmentOptions, 55 Constructors, 55 GetMaxChiral, 56 GetMaxDeqree, 56 GetMaxHeavy, 56 GetMaxMolWt, 56 GetMinDegree, 56 GetMinHeavy, 56 GetSingleSourceMol, 57 GetSmarts, 57 operator=, 56 SetMaxChiral, 57 SetMaxDegree, 57 SetMaxHeavy, 57 SetMaxMolWt.57 SetMinDegree, 57 SetMinHeavy, 58 SetSingleSourceMol.58 SetSmarts.58 SetSmartsFile, 58 OEBioisostere:: OEFragOverlay, 58 Constructors, 59

GetRefFrag, 59 SetupRef, 59 OEBioisostere:: OEGenerateConformers, 78 OEBioisostere:: OEGetBroodStatus, 79 OEBioisostere:: OEGetDBIndices, 79 OEBioisostere:: OEHitlistBuilder, 59 AddScores. 60 Build. 60 Constructors. 60 GetAddCount, 60 GetBumpCount, 60 GetDeleteCount, 60 GetDuplicateCount, 61 GetHitCount, 61 GetHits.61 GetInitHitCount, 61 GetMatchCount, 61 GetSecDuplicateCount, 61 GetStrainCount. 61 GetUnstableCount, 62 OEBioisostere:: OEIntrinsicPropOptions, 65 Constructors, 65 GetAromaticJCT. 65 GetHeavyAtomCount, 66 GetMolWt.66 GetRotorCount, 66 GetSp3CFrac, 66 GetTPSA, 66 operator=, 65 SetAromaticJCT.66 SetHeavyAtomCount, 66 SetMolWt, 67 SetRotorCount, 67 SetSp3CFrac. 67 SetTPSA, 67 OEBioisostere:: OEMolPropertyOptions, 62 Constructors, 62 GetEganEgg, 63 GetExtrinsicMaxOptions, 63 GetExtrinsicMinOptions, 63 GetIntrinsicMaxOptions, 63 GetIntrinsicMinOptions, 63 GetVeber, 63 operator=, 62 SetEganEgg, 64 SetExtrinsicMaxOptions, 64 SetExtrinsicMinOptions, 64 SetIntrinsicMaxOptions, 64 SetIntrinsicMinOptions, 64 SetVeber, 64 OEBioisostere:: OEReadBroodQuery, 79 OEBioisostere:: OEWriteBroodQuery, 79 operator=

```
OEBioisostere:: OEBroodBuildOptions,
       23
   OEBioisostere:: OEBroodDBFilter, 25
   OEBioisostere:: OEBroodDBPacket, 26
   OEBioisostere:: OEBroodGeneralOptions,
       28
   OEBioisostere:: OEBroodHit.31
   OEBioisostere:: OEBroodHitlistOptions,
       36
   OEBioisostere:: OEBroodQuery, 40
   OEBioisostere:: OEBroodScore, 42
   OEBioisostere:: OEBroodScoreOptions,
       45
   OEBioisostere:: OEDBScreenOptions, 52
   OEBioisostere:: OEExtrinsicPropOptions,
       68
   OEBioisostere:: OEFragmentOptions, 56
   OEBioisostere:: OEIntrinsicPropOptions,
       65
   OEBioisostere:: OEMolPropertyOptions,
       62
Overlay
   OEBioisostere:: OEBroodOverlay, 39
   OEBioisostere:: OEBroodOverlayBase,
       39
```

## P

Prep OEBioisostere:: OEBroodFragPrep, 28

## R

ReadConformers OEBioisostere:: OEFragConfReader, 55 replace\_fragment.py Example Code, 20

## S

Screen OEBioisostere:: OEDBBuilder, 50 SetAromaticJCT OEBioisostere:: OEIntrinsicPropOptions, 66 SetAttachCutoff OEBioisostere:: OEBroodScoreOptions, 46 SetLogP SetAttachScale OEBioisostere:: OEBroodGeneralOptions, 29 SetBuildOptions OEBioisostere:: OEBroodHitlistOptions, 37 SetBuildType OEBioisostere:: OEBroodBuildOptions, 24

SetBumpRadius OEBioisostere:: OEBroodGeneralOptions,  $29$ SetCheckBond OEBioisostere:: OEBroodBuildOptions,  $25$ SetCheckGeometry OEBioisostere:: OEBroodScoreOptions, 46 SetComplexity OEBioisostere:: OEExtrinsicPropOptions, 69 SetEganEgg OEBioisostere:: OEMolPropertyOptions, 64 SetExtrinsicMaxOptions OEBioisostere:: OEMolPropertyOptions, 64 SetExtrinsicMinOptions OEBioisostere:: OEMolPropertyOptions, 64 SetFrequency OEBioisostere:: OEExtrinsicPropOptions, 69 SetGenerateIdea OEBioisostere:: OEBroodHitlistOptions, 37 SetHeavyAtomCount OEBioisostere:: OEIntrinsicPropOptions, 66 SetIntrinsicMaxOptions OEBioisostere:: OEMolPropertyOptions, 64 SetIntrinsicMinOptions OEBioisostere:: OEMolPropertyOptions, 64 SetLipinski OEBioisostere:: OEExtrinsicPropOptions, 69 SetLipinskiAcc OEBioisostere:: OEExtrinsicPropOptions, 69 SetLipinskiDon OEBioisostere:: OEExtrinsicPropOptions, 70 OEBioisostere:: OEExtrinsicPropOptions, 70 SetMartin OEBioisostere:: OEExtrinsicPropOptions, 70 SetMaxChiral OEBioisostere:: OEFragmentOptions, 57 SetMaxDeqree

OEBioisostere:: OEFragmentOptions, 57 SetMaxHeavy Setup OEBioisostere:: OEFragmentOptions, 57 SetMaxHits OEBioisostere:: OEBroodHitlistOptions, SetupRef 37 SetMaxLocalStrain OEBioisostere:: OEBroodBuildOptions, 25 SetMaxMolWt OEBioisostere:: OEFragmentOptions, 57 SetMinDegree OEBioisostere:: OEFragmentOptions, 57 SetMinFreqHeavy OEBioisostere:: OEDBScreenOptions, 53 SetMinFrequency OEBioisostere:: OEDBScreenOptions, 53 Τ SetMinHeavy OEBioisostere:: OEFragmentOptions, 58 SetMolWt OEBioisostere:: OEIntrinsicPropOptions, 67 Transform SetNeutralPH OEBioisostere:: OEBroodOverlayBase, OEBioisostere:: OEBroodBuildOptions,  $40$ 24 W SetPropertyOptions OEBioisostere:: OEBroodScoreOptions, Write 47 OEBioisostere:: OEDBWriter, 54 SetRingOnly OEBioisostere:: OEBroodScoreOptions,  $\Delta$ 7 SetRotorCount OEBioisostere:: OEIntrinsicPropOptions, 67 SetScoreType OEBioisostere:: OEBroodGeneralOptions, 29 SetShapeCutoff OEBioisostere:: OEBroodScoreOptions,  $46$ SetSingleSourceMol OEBioisostere:: OEFragmentOptions, 58 SetSmarts OEBioisostere:: OEFragmentOptions, 58 SetSmartsFile OEBioisostere:: OEFragmentOptions, 58 SetSp3CFrac OEBioisostere:: OEIntrinsicPropOptions, 67 SetTautomers OEBioisostere:: OEBroodBuildOptions, 25 SetTPSA

```
OEBioisostere:: OEIntrinsicPropOptions,
       67
   OEBioisostere:: OEBroodDBFilter, 26
   OEBioisostere:: OEBroodOverlay, 39
   OEBioisostere:: OEFragOverlay, 59
SetUseBondOrder
   OEBioisostere:: OEBroodScoreOptions,
       46
SetUseProperty
   OEBioisostere:: OEBroodScoreOptions,
       46
SetVeber
   OEBioisostere:: OEMolPropertyOptions,
       64
ToRecord
   OEBioisostere:: OEBroodDBPacket, 27
   OEBioisostere:: OEBroodScore, 44
```