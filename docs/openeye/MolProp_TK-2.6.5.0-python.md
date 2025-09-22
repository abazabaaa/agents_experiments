![](_page_0_Picture_0.jpeg)

**MolProp TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| Number | Title                                    | Page |
|--------|------------------------------------------|------|
| 1      | <b>Theory</b>                            | 1    |
| 1.1    | Filtering Theory                         | 1    |
| 1.1.1  | Introduction                             | 1    |
| 1.2    | Filter Pre-processing                    | 5    |
| 1.2.1  | Metal Removal                            | 6    |
| 1.2.2  | Salt Removal                             | 6    |
| 1.2.3  | Canonicalization                         | 6    |
| 1.2.4  | pKa Normalization                        | 6    |
| 1.2.5  | Normalization                            | 6    |
| 1.2.6  | Reagent Selection                        | 7    |
| 1.2.7  | Type Checking                            | 7    |
| 1.2.8  | MMFF94 Atom Type Checking                | 7    |
| 1.3    | Molecular Properties and Predictors      | 7    |
| 1.3.1  | Structural and Chemical Features         | 8    |
| 1.3.2  | Functional Groups                        | 8    |
| 1.3.3  | Dyes                                     | 9    |
| 1.3.4  | $LogP$                                   | 9    |
| 1.3.5  | $LogS$                                   | 9    |
| 1.3.6  | Polar Surface Area                       | 10   |
| 1.3.7  | Lipinski and Hydrogen-bonds              | 10   |
| 1.3.8  | Aggregators                              | 11   |
| 1.3.9  | PAINS                                    | 11   |
| 1.4    | Filter Files                             | 12   |
| 1.4.1  | Physical Property Limits                 | 12   |
| 1.4.2  | Functional Group Rules                   | 23   |
| 1.4.3  | New Rules                                | 82   |
| 1.4.4  | Selection Statements                     | 82   |
| 2      | <b>Examples</b>                          | 83   |
| 2.1    | MolProp TK Examples                      | 83   |
| 2.1.1  | Basic Filtering for a Molecule File      | 83   |
| 2.1.2  | Quiet Filtering                          | 86   |
| 2.1.3  | Molecular Property Table                 | 89   |
| 2.1.4  | Specific Molecular Properties            | 92   |
| 2.1.5  | Attach Molecular Properties as SD Data   | 94   |
| 2.1.6  | Write Molecular Properties to a CSV File | 98   |
| 2.2    | Python Cookbook Examples                 | 100  |
| 3      | <b>API</b>                               | 101  |
| 3.1    | OEMolProp Classes                        | 101  |
| Number | Description                              | Page |
| 3.1.1  | OEFilter                                 | 10   |
| 3.1.2  | OEXLogPResult                            | 10   |
| 3.2    | OEMolProp Constants                      | 10   |
| 3.2.1  | OEFilterType                             | 10   |
| 3.2.2  | OEFilterParamName                        | 10   |
| 3.2.3  | OEFilterParamSetup                       | 11   |
| 3.3    | OEMolProp Functions                      | 11   |
| 3.3.1  | OECheckXLogXType                         | 11   |
| 3.3.2  | OECheckXLogXTypes                        | 11   |
| 3.3.3  | OEConfigureFilterParams                  | 11   |
| 3.3.4  | OEConfigureFilterType                    | 11   |
| 3.3.5  | OEGet2dPSA                               | 11   |
| 3.3.6  | OEGetAnionicCarbonCount                  | 11   |
| 3.3.7  | OEGetAromaticRingCount                   | 11   |
| 3.3.8  | OEGetFilterType                          | 11   |
| 3.3.9  | OEGetFractionCsp3                        | 11   |
| 3.3.10 | OEGetHalideFraction                      | 11   |
| 3.3.11 | OEGetHBondAcceptorCount                  | 11   |
| 3.3.12 | OEGetHBondDonorCount                     | 11   |
| 3.3.13 | OEGetLipinskiAcceptorCount               | 11   |
| 3.3.14 | OEGetLipinskiDonorCount                  | 11   |
| 3.3.15 | OEGetLongestUnbranchedHeavyAtomsChain    | 11   |
| 3.3.16 | OEGetLongestUnbranchedCarbonsChain       | 11   |
| 3.3.17 | OEGetNumUnspecifiedAtomStereos           | 12   |
| 3.3.18 | OEGetNumUnspecifiedBondStereos           | 12   |
| 3.3.19 | OEGetRotatableBondCount                  | 12   |
| 3.3.20 | OEGetXLogP                               | 12   |
| 3.3.21 | OEGetXLogPResult                         | 12   |
| 3.3.22 | OEGetXLogPVersion                        | 12   |
| 3.3.23 | OEMolPropGetArch                         | 12   |
| 3.3.24 | OEMolPropGetLicensee                     | 12   |
| 3.3.25 | OEMolPropGetPlatform                     | 12   |
| 3.3.26 | OEMolPropGetRelease                      | 12   |
| 3.3.27 | OEMolPropGetSite                         | 12   |
| 3.3.28 | OEMolPropGetVersion                      | 12   |
| 3.3.29 | OEMolPropIsLicensed                      | 12   |
| 3.3.30 | OEWritePropertyDataToCSV                 | 12   |
| 4      | <b>Release History</b>                   | 12   |
| 4.1    | MolProp TK 2.6.5                         | 12   |
| 4.2    | MolProp TK 2.6.4                         | 12   |
| 4.3    | MolProp TK 2.6.3                         | 12   |
| 4.4    | MolProp TK 2.6.2                         | 12   |
| 4.5    | MolProp TK 2.6.1                         | 12   |
| 4.5.1  | New features                             | 12   |
| 4.5.2  | Minor bug fixes                          | 12   |
| 4.6    | MolProp TK 2.6.0                         | 12   |
| 4.6.1  | New features                             | 12   |
| 4.7    | MolProp TK 2.5.7                         | 12   |
| 4.7.1  | New Features                             | 12   |
| 4.8    | MolProp TK 2.5.6                         | 12   |
| 4.8.1  | Minor bug fixes                          | 12   |
| 4.9    | MolProp TK 2.5.5                         | 12   |
| 4.10   | MolProp TK 2.5.4                         | 12   |

| 4.11 MolProp TK 2.5.3        |
|------------------------------|
| 4.11.1 New features          |
| 4.11.2 Minor bug fixes       |
| 4.11.3 Documentation changes |
| 4.12 MolProp TK 2.5.2        |
| 4.12.1 New features          |
| 4.12.2 Documentation changes |
| 4.13 MolProp TK 2.5.1        |
| 4.14 MolProp TK 2.5.0        |
| 4.14.1 Bug fixes             |
| 4.15 MolProp TK 2.4.7        |
| 4.15.1 Minor bug fixes       |
| 4.16 MolProp TK 2.4.6        |
| 4.17 MolProp TK 2.4.5        |
| 4.18 MolProp TK 2.4.4        |
| 4.18.1 Minor bug fixes       |
| 4.18.2 Documentation changes |
| 4.19 MolProp TK 2.4.3        |
| 4.19.1 Major bug fixes       |
| 4.20 MolProp TK 2.4.2        |
| 4.21 MolProp TK 2.4.1        |
| 4.21.1 New features          |
| 4.21.2 Major bug fixes       |
| 4.21.3 Minor bug fixes       |
| 4.22 MolProp TK 2.4.0        |
| 4.22.1 New features          |
| 4.22.2 Bug fixes             |
| 4.23 MolProp TK 2.3.0        |
| 4.23.1 New features          |
| 4.23.2 Documentation fixes   |
| 4.24 MolProp TK 2.2.2        |
| 4.24.1 Minor bug fixes       |
| 4.24.2 Documentation fixes   |
| 4.25 MolProp TK 2.2.1        |
| 4.25.1 New features          |
| 4.25.2 Major bug fixes       |
| 4.25.3 Minor bug fixes       |
| 4.26 MolProp TK 2.2.0        |
| 4.26.1 Minor bug fixes       |
| 4.26.2 Documentation changes |
| 4.27 MolProp TK 2.1.7        |
| 4.27.1 Major bug fixes       |
| 4.28 MolProp TK 2.1.6        |
| 4.28.1 Bug fixes             |
| 4.29 MolProp TK 2.1.5        |
| 4.30 MolProp TK 2.1.4        |
| 4.31 MolProp TK 2.1.3        |
| 4.31.1 New features          |
| 4.31.2 Minor bug fixes       |
| 4.32 MolProp TK 2.1.2        |
| 4.33 MolProp TK 2.1.1        |
| 4.33.1 New features          |
| 4.33.2 Minor bug fixes       |
| 4.34 MolProp TK 2.1.0        |

| Section | Title                         | Page |
|---------|-------------------------------|------|
| 5       | Copyright and Trademarks      | 137  |
| 6       | Sample Code                   | 139  |
| 7       | Citation                      | 141  |
| 7.1     | Orion ® Floes                 | 141  |
| 7.2     | Toolkits and Applications     | 141  |
| 7.3     | OpenEye Web Services          | 143  |
| 8       | Technology Licensing          | 145  |
| 8.1     | GCC                           | 160  |
| 8.1.1   | GCC RUNTIME LIBRARY EXCEPTION | 160  |
| 8.1.2   | GNU GENERAL PUBLIC LICENSE    | 162  |
|         | Index                         | 175  |

## **CHAPTER**

# **ONE**

# **THEORY**

## **1.1 Filtering Theory**

### 1.1.1 Introduction

Filtering attempts to eliminate inappropriate or undesirable compounds from a large set before beginning to use them in modeling studies. The goal is to remove all of the compounds that should not be suggested to a medicinal chemist as a potential hit. This exercise is obviously case dependent, depending on ease of the assay, intended target, personal bias of the modeler & medicinal chemist, strengths of the company, etc.

To match this need, the default filter encapsulates many of the standard filtering principles, such as removal of unstable, reactive, and toxic moieties. In addition, MolProp TK allows the customization of the filtering criteria to fit specific needs.

The criteria for passing or failing a given molecule fall into three categories.

- Physical properties
  - Molecular weight
  - Topological polar surface area (TPSA)
  - $-$  logP
  - Bioavailability
- Atomic and functional group content
  - Absolute and relative content of heteroatoms
  - Limits on a very wide variety of functional groups
- Molecular graph topology
  - Number and size of ring systems
  - Flexibility of the molecule
  - Size and shape of non-ring chains

All of the data generated in filtering molecules can be written to a tab-separated file for easy import into a spreadsheet. This functionality allows for combining the values dynamically for a variety of purposes, including, but not limited to, determining which filter values best fit each project's needs.

### **History**

When OpenEye's work on filtering technology began in 2000, it was designed simply to remove compounds with reactive or otherwise undesirable functional groups. Over the years, the understanding of lead-like and drug-like compound selection has advanced. In addition, with the publication of Lipinski's "Rule of 5" [Lipinski-1997], more and more pharmacokinetic properties have been pushed earlier into the virtual screening process.

In addition to providing basic functional group selection, the technology is a one-stop database preparation tool aimed at generating databases suitable for high-throughput virtual screening.

- Cheminformatics quality-control
  - Valence-state validation
  - Aromaticity perception
  - Implicit hydrogen perception
  - Bond-order perception
- Database preparation
  - Setting pKa states
  - Applying normalizations (tautomers and dative or hypervalent states)
- Compound selection
  - $-$  Physical properties (see *above*)
  - Assay counter-indicators (aggregators and dyes)
  - Promiscuous actives ([Baell-2010])
  - PK ([Martin-2005], [Veber-2002], [Egan-2000], [Lipinski-1997])

Finally, it should be pointed out that in the virtual screening world, time is of the essence. Algorithms for preliminary database preparation should not take large amounts of time. Because of this, all the calculations included are 2D or graph-based algorithms. While this does occasionally limit the technology, it allows for the delivery of a product that is appropriate for the task of virtual-screening database preparation.

## **The Rant!**

Nearly every computational tool used in early drug discovery yields statistically predictive, rather than absolutely definitive results. In nearly every case, prudence demands that one consider the causes of false-positives and falsenegatives and make an attempt to optimize the area under the receiver-operator curve (ROC) for the computational tool. However, there are well known methods for improving statistical predictions of this nature that are independent of the absolute false-positive and false-negative rates. These methods include filtering the population to which a test will be applied. By applying a test to smaller populations that only contain molecules appropriate for the specific application at hand, the negative impact of the false-positive rate on the predictive results can be dramatically improved.

A familiar example from the medical world will serve to illustrate this principle. Assume we have a test for the presence of the new *foo virus* which has an exceptional ROC curve with false-positive and false-negative values (1/1,000 and 1/1,000 respectively). Let us assume that the *foo-syndrome*, caused by the *foo virus*, effects 1 person in 20,000. If we gave this test to 100,000 people from the general population, we would expect 5 to actually have the *foo syndrome*. With this test, there is only a 0.05% percent chance that any of them would not be detected (that is, be a false-negative). However, we would expect there to be 100 false positive test results. Thus of the 105 total positive test results, only 4.8% would actually have the *foo syndrome* (positive predictive value =  $4.8\%$ ).

|                           | <b>Actual Positive</b> | <b>Actual Negative</b>    |                                  |
|---------------------------|------------------------|---------------------------|----------------------------------|
| <b>Predicted Positive</b> | True Positives $= 5$   | False Positives $= 100$   | Positive Predictive Value = 4.8% |
| <b>Predicted Negative</b> | False Negatives $= 0$  | True Negatives $= 99,895$ |                                  |

Table 1: Confusion table for the **unfiltered** foo virus test (prevalence 1 in 20,000)

Alternatively, we could start by using very simple screening before applying the test. We first eliminate people who do not have any risk factors for contracting the *foo virus*. Next we may eliminate people whose blood is incompatible with the test for the foo virus. Further, we may want to eliminate people who acknowledge that they will refuse treatment for the foo virus even if we determine that they do have it. By these admittedly simple screens, we apply the test for the foo virus to a much smaller group with a decidedly higher prevalence of the virus. For instance, after the filtering, we may be left with a group of only 1,000 people who have a 1 in 200 chance of having the syndrome. Now, we still have the same 5 people who actually have the disease, but we only expect 1 false positive test. Suddenly, there are 6 total positive tests, and 83% of them actually have the syndrome! This is reflected in a much more reasonable (83%) positive predictive value.

Table 2: Confusion table for the **filtered** foo virus test (prevalence 1 in 200)

|                    | <b>Actual Positive</b> | <b>Actual Negative</b> |                                    |
|--------------------|------------------------|------------------------|------------------------------------|
| Predicted Positive | True Positives $= 5$   | False Positives $= 1$  | Positive Predictive Value = $83\%$ |
| Predicted Negative | False Negatives $= 0$  | True Negatives $= 994$ |                                    |

Bringing the discussion back to drug design, if we have a ligand-based design tool such as ROCS, we can imagine that the receiver-operator curve may have a false positive rate as low as 1 in 10,000. For this exercise, let's assume no false negatives. When using that to identify 50 inhibitors from a database of 2.5 million available compounds, we'd identify 300 potential inhibitors, and 5 out of every 6 of these would be a false positive (positive predictive value of 17%)! If we first run  $f$ ilter and eliminate 65% of the 2.5 million compounds, this leaves us with 875,000 compounds to push through ROCS. There will be about 88 false positives to go with the 50 true positives and the positive predictive value will increase over two-fold with relatively little work.

### Table 3: Confusion table for the **unfiltered** ROCS virtual screen

|                    | Actual Positive       | Actual Negative              |                                    |
|--------------------|-----------------------|------------------------------|------------------------------------|
| Predicted Positive | True Positives = $50$ | False Positives = $250$      | Positive Predictive Value = $17\%$ |
| Predicted Negative | False Negatives = $0$ | True Negatives = $2,499,700$ |                                    |

| Table 4: Confusion table for the <b>filtered</b> ROCS virtual screen |  |  |
|----------------------------------------------------------------------|--|--|
|----------------------------------------------------------------------|--|--|

|                           | <b>Actual Positive</b> | <b>Actual Negative</b>     |                                    |
|---------------------------|------------------------|----------------------------|------------------------------------|
| <b>Predicted Positive</b> | True Positives $= 50$  | False Positives $= 88$     | Positive Predictive Value = $36\%$ |
| <b>Predicted Negative</b> | False Negatives $= 0$  | True Negatives $= 874,862$ |                                    |

## **Filtering Principles**

The same principle of increasing positive predictive value by removing obvious true negatives applies to screening for lead candidates, regardless of whether it is virtual screening or high-throughput screening. While both are reasonable screens, each can be plagued by very low positive-predictive values (despite low false-positive rates), particularly when applied to all available compounds, or large virtual libraries. Simple filtering techniques focus the set of compounds passed on to more computationally intensive screening methods.

The first approach to consider is filtering based on *functional groups*. Generally speaking, there are toxic and reactive functional groups that you simply do not want to consider (alkyl-bromides, metals etc). There are also functional groups that are not strictly forbidden, but are not desired in large quantities. For instance, parafluoro-benzene, or trifluoromethyl have specific purposes, but heavily fluorinated molecules can be eliminated.

Beyond simple functional group filtering, you can consider both simple and complex physical properties which can be used to characterize the kinds of compounds you would like to keep and those you would like to eliminate. These properties attempt to consider "drug-likeness", such as bio-availability, solubility, toxicity, and synthetic accessibility even before the primary high-throughput or virtual screening, which primarily are geared toward detecting potency alone. The best known of the physical property filters is *Lipinski's "rule-of-five"*, which focuses on bioavailability [Lipinski-1997]. However, many other physical properties, such as *solubility*, *atomic content, ring structures*, and surface area ratios can also be considered. MolProp TK provides algorithms for calculating many of these properties, and applying them with filters based on literature studies.

Finally, you should eliminate the types of compounds that can be troublesome at later stages. For instance, Shoichet's aggregating compounds often produce false positives that can waste enormous resources if they were identified by virtual or high-throughput screening [McGovern-2003] [Seidler-2003]. Similarly, *dyes* can appear to be inhibitors by interfering with colorimetric or fluorometric assays or binding non-specifically to the target protein.

### **Variations of Filters**

Different types of filters are appropriate under different circumstances. Very early in a project, when little or no SAR is available, very strict drug-like filters can be applied. This prevents a project team from spending chemistry resources pursuing difficult compounds that may not be modifiable to introduce appropriate properties. However, when considering compounds for purchase for HTS, different filters can be applied. Oprea, et al, pointed out that the best molecules for initial HTS are smaller and less functionalised than drugs, but with some activity [Oprea-2000]. Therefore, strict lead-like filters can be applied to ensure that hits identified from HTS have sufficient "room" for elaboration into (usually larger and more highly functionalised) leads. However, when SAR suggests that particular compounds or series may yield valuable information, filtering criteria can be loosened, because the secondary screens (QSAR models, similarity to known actives) that are being applied are effective in detecting useful compounds. Reflecting back on the medical analogy, this is the case where an improved primary screen with a dramatically improved false-positive rate (say 1 in 100,000) can be safely applied to a larger population without terrible effects on the positive-predictive value.

MolProp TK provides the following filters:

- BlockBuster: The BlockBuster filter is based on 141 best-selling, non-antibiotic, prescription drugs. We designed the physical property portion of the filter so that it passes all of the compounds. The physical property values in this filter are quite good. However, the functional group filters in this filter are probably too restrictive because 141 compounds is not sufficient to span all acceptable functionality.
- Drug: The original Drug filter ([Oprea-2000]) is provided as well. However, experience has shown it to be too restrictive. The BlockBuster filter was developed in response to complaints about the Drug filter being too restrictive.
- Fragment
- Lead: The Lead filter corresponds to the [Oprea-2000] lead-like filters useful for preparing HTS screening databases.

• PAINS: The PAINS filter is based on [Baell-2010] which describes work to identify and filter promiscuous (nonspecific) actives across a number of screening types and targets. Unlike the other filter types, the PAINS filter consists only functional group filters; no physical property filters are included. In practice it may be desirable to combine the PAINS filter with a separate user-defined set of physical property filters.

**Hint:** We recommend the BlockBuster filter, the default, for most purposes. If your project is unusual, or you are unsatisfied with the results we recommend you review the *filter file* for your specific filtering needs.

If you decide to modify the *filter file* the depictions found in the *Functional Group Rules* section can be particularly helpful in determining what functional groups are indicated by each name in the file.

### **Accumulation of Rules**

FILTER contains numerous rules that judge the quality of molecules on many different facets. When examined individually, each of these rules seems quite reasonable and even profitable. However, when each molecule is tested against hundreds of individual filters, the fraction of molecules that pass all the filters can be surprisingly small. Sometimes less than 50% of vendor databases pass the filters. If this is unacceptable we recommend you examine the predicted aggregator, solubility, and Veber filters. In our experience, these are the most common failures. The best method of investigating failures is looking at the filter log.

The BlockBuster filter was adjusted to demonstrate this in a tangible way. For each value, rather than spanning the entire range, its properties were set to cover from the 2.5th percentile to the 97.5th percentile. The differences between the original BlockBuster filter and the adjusted filter are both in reasonable ranges. For instance, the full range of molecular weight for the BlockBuster filter spans 130 to 781, while the 2.5th percentile is 145 and the 97.5th percentile is 570. The remarkable result is that when the reduced filter is used, only 75 of the 141 original molecules pass the filter! This demonstrates how slight changes to many filters can lead to a significant reduction in the number of compounds that pass all of the filters.

Taking the opposite approach of allowing everything to pass can be equally futile. To demonstrate this a filter was designed around the "small molecule drug" file available from the DrugBank website. In order to pass every one of these molecules, including some that would not be acceptable for modern project work, many of the individual filters must be set to unreasonable values. For instance, the molecular weight range is 30 to 1500 and the hetero-atom count range is 1 to 60!

Hint: OpenEye can not magically divine the needs of every project. You should personally inspect the *filter file*. The depictions found in the *Functional Group Rules* section can be particularly helpful in discerning what functional groups are desirable and undesirable.

## **1.2 Filter Preprocessing**

Before the applying any of the *molecular property filters* a preprocessing step occurs that can alter the molecule significantly to fit the criteria needed for most modeling applications. This filtering preprocessing step is a precisely defined series of stages that occur on the molecule in the following order:

- 1. Metal Removal
- 2. Salt Removal
- 3. Canonicalization
- 4. pKa Normalization
- 5. Normalization

- **6.** Reagent Selection
- 7. Type Checking
- 8. MMFF94 Atom Type Checking

### 1.2.1 Metal Removal

Metal removal is the first stage of elemental based filtering. This stage will remove specified metal complexes from the molecule. It will not reject a molecule for having a metal complex. This allows the filter to treat atoms in the counter-ion portion of a molecule separately from the atoms in the primary portion of the molecular record.

For instance, this allows organic molecules that are complexed with silver to be eliminated based on their metal chelate even though they themselves are acceptable while at the same time eliminating a sulfate counter-ion from another molecule before it leads to elimination of the acceptable cationic molecule.

### See also:

**Elemental Filters** 

### 1.2.2 Salt Removal

This step deletes all atoms that are not part of the largest connected component of a compound. This effectively eliminates all non-covalently bound portions of the compound.

### 1.2.3 Canonicalization

This step canonicalizes the atom and bond order of the parts of the molecule that are left after the previous removal steps. This is necessary to avoid different atom orderings producing slightly different normalizations in the following normalization steps.

### 1.2.4 pKa Normalization

pKa Normalization uses a rule-based system to set the ionization state of input molecules. If pKa normalization is turned on, the molecule is set to its most energetically favorable ionization state for  $pH=7$ . 4. The rule-based nature of this calculation allows it to be very fast. Further, despite being rule-based, this approach takes into account many secondary charge interactions.

While more advanced levels of theory can be found for predicting ionization states, this method is very well suited to virtual-screening database preparation. However, this may not be appropriate for hit-to-lead or lead optimization.

### **1.2.5 Normalization**

In addition to pKa normalization, MolProp TK allows any number of additional molecular normalizations. Since normalizations are usually specific to a particular company or site, MolProp TK provides the ability for users to input normalizations, such as the nitro tautomer state, but does not provide default implementations.

### **1.2.6 Reagent Selection**

Reagent selection for small linear library synthesis or large combinatorial library synthesis is still a necessary task at many pharmaceutical companies. For a user hoping to identify a set of acyl-halide reagents, they can specify a selection parameter to require that each compound have exactly one acyl-halide. In addition they might want to modify the filter to exclude functional groups (such as primary amines) that may be acceptable for typical lead-like molecules, but are not acceptable for the specific reagent the user has in mind.

Therefore, the selection parameter is the reverse of a filtering parameter. The molecule must *include* the given substructure in order to pass the filter.

#### See also:

The select parameter in filter files.

### 1.2.7 Type Checking

This checks the valence state and formal charge of the entire molecule. The check identifies molecules that are poorly specified, or represent nonsensical chemical states, often from corrupt input data. For example, an oxygen with eight hydrogens attached or a carbon with a +9 formal charge would be rejected.

### 1.2.8 MMFF94 Atom Type Checking

This checks that all the atoms of the molecule have valid MMFF94 atom type assignments. The check identifies molecules that will fail downstream processing that depends on MMFF94 atom types (e.g. Omega).

## **1.3 Molecular Properties and Predictors**

MolProp TK provides a range of properties to predictors to be used as molecular filters. Molecular properties are distinct physical properties that can be measured such as the following:

- Structural and Chemical Features
- Functional Groups

There have been several attempts at developing fast-approximate QSAR models for bioavailability that have been published. The first of these was *Lipinski's work* ([Lipinski-1997]) and it has been followed by work at Pharmacopia [Egan-2000], Abbott [Martin-2005], and GSK [Veber-2002]. The simplest and probably most trusted is the work of LogP and PSA used by Egan. The most recent work by Martin, the Abbott Bioavailability Score (ABS) appears to be a refinement of the first generation models and is designed specifically to categorize a molecule's probability of having a bioavailability>10% in rats.

### See also:

The Pharmacokinetic Predictors section in the Filter Files chapter.

### **1.3.1 Structural and Chemical Features**

There are a number of important structural and chemical features of molecules that it is desirable to limit for virtual screening. The following simple measures are provided as filterable properties:

- Molecular weight
- Ring count
- Ring-system size
- Size of non-ring structures
- Length of unbranched chains
- Hetero-atom fraction
- Halide fraction
- Formal charges
- Rotatable bonds

It also includes slightly more complex algorithms for hydrogen-bond donors and acceptors as well as chiral centers.

### See also:

The Basic Properties section in the Filter Files chapter.

### **1.3.2 Functional Groups**

Functional group removal remains at the heart of the filter algorithm. Functional groups fall into several categories including:

- Reactive or labile groups
- Undesirable groups
- Generally acceptable groups
- Protecting groups
- User-derived groups

While reasonable defaults are provided for each functional group in all of the above categories, it is unusual to find an experienced computational or medicinal chemist who agrees with all of the default values. Examining the filter file at least once is strongly encouraged. Developing a custom filter to fit a desired design is also strongly encouraged. The filter files were designed as basic guides.

### See also:

The filter files contain only functional group names. If there is any confusion regarding the definitions, please refer to the *Functional Group Rules* section for complete descriptions.

### **1.3.3 Dyes**

Years ago, many high-throughput assays could be interfered with by colored molecules. While assay technology has continued to advance and often this is not a problem, it is recognized that most molecules that are dyes are not the type of molecules that are commonly carried forward in lead-development projects. Therefore, a pattern-based filter for dye molecules is included. While these patterns occasionally identify molecules that are considered acceptable by some users, in general, they identify molecules that the majority of chemists would rather not see at the top of their virtual screening hit lists.

### 1.3.4 LogP

The XLOGP algorithm ([Wang-R-1997]) is provided because its atom type contribution allows calculation of the XLogP contribution of any fragment in a molecule and allows minimal corrections in a simple additive form to calculate the LogP of any molecule made from combinations of fragments. Further, although the method contains many free parameters, its simple linear form allows for ready interpretation of the model, and most of the parameters in the model make rational sense.

Unfortunately, the original algorithm is difficult to implement as published. First, the internal hydrogen bond term was calculated using a single 3D conformation. It was found that this was both arbitrary and unnecessary. This arbitrary 3D calculation has been replaced with a 2D approach to recognize common internal hydrogen bonds. In tests, this 2D method worked comparably to the published 3D algorithm. Next, the training set had a few subtle atom type inconsistencies.

Both of these problems were corrected and refit to the original XLOGP training data. This implementation gives results that are quite similar to the original XLOGP algorithm, so it is called OEXLogP to distinguish it from the original method.

#### See also:

 $\bullet$  The  $XLogP$  parameter in the Filter Files chapter.

### 1.3.5 LogS

The work of [Yalkowsky-1980] at Arizona has resulted in what is now called the "generalized solvation equation." It states that the solubility of a compound can be broken into two steps, first the melting for the pure solid to pure liquid and second, the phase transfer from pure liquid into water. For many small organic molecules, this second step is somewhat related to LogP.

Because of this relation we choose to explore the use of the XLogP atom-types in solubility prediction. The expectation was that this might provide an approximate though robust and fast method for calculating solubility. We fit the XLogP atom-types to a training set of nearly 1000 public solubilities. From this we derived a linear model for solubility. The model is extremely fast and is useful for classifying compounds as insoluble, poorly soluble, slightly soluble, moderately, soluble or very soluble. The model is notable for the difficulty it has predicting solubilities for compounds with ionizable groups. Further, it is not suitable for the PK predictions that come late in a project. However, it is useful for eliminating compounds with severe solubility problems early in the virtual-screening process.

### See also:

The solubility parameter in the Filter Files chapter.

### 1.3.6 Polar Surface Area

Topological polar-surface area (TPSA) is based on the algorithm developed by Ertl et al [Ertl-2000]. In Ertl's publication, use of TPSA both with and without accounting for phosphorus and sulfur surface-area is reported. However, evidence shows that in most PK applications one is better off not counting the contributions of phosphorus and sulfur atoms toward the total TPSA for a molecule. This implementation of TPSA allows either inclusion or exclusion of phosphorus and sulfur surface area with the default being to not include it.

### See also:

Including phosphorus and sulfur surface area:

• The PSA USE SandP parameter in the filter file

Warning: TPSA values are mildly sensitive to the protonation state of a molecule. If the pKaNorm parameter is false, the TPSA value is calculated using the input structure and if pKaNorm is true, the TPSA is calculated using the pKa normalized molecular structure.

See also:

 $\bullet$  The *pKa normalization* section of the Filter Preprocessing chapter.

### 1.3.7 Lipinski and Hydrogen-bonds

The work of Lipinski ([Lipinski-1997]) introduced the application of simple filter-like rules to roughly predict latestage PK properties, in particular oral bioavailability. Unfortunately, Lipinski's "Rule-of-Five" has come into the common vernacular to such a large degree that some of the specific details are often lost in the commotion. There are two critical examples of this. First, Lipinski used "violation of 2 rules" to categorize compounds. In the subsequent analysis, a significant difference in the two populations of molecules was detected, however, little analysis of the importance of a single violation was done. However, many now consider a single violation to be bad and two violations to be worse. At this writing, there is no known evidence to support this. Second, Lipinski used well-codified and wellunderstood yet imprecise definitions of "hydrogen-bond donors" and "hydrogen-bond acceptors" in his classification model. While this makes the algorithm quite understandable and easy to implement, it sometimes causes confusion with those who prefer more refined definitions of hydrogen-bond donors and acceptors.

To address the first problem, users are allowed to set the number of Lipinski failures required to reject a molecule. In keeping with the original publication, the default value is 2. To address the second problem, two kinds of hydrogenbond donors and acceptors are calculated. In the Lipinski calculation, the published definitions are used (donor count is the number nitrogen or oxygen atoms with at least one hydrogen attached and acceptors are the number of nitrogens and oxygens). For calculation of the number of donors and acceptors in the molecule for the sake of chemical properties, a more complex algorithmic approach is taken. This approach identifies the donors and acceptors outlined in the work of Mills and Dean ([Mills-Dean-1996]) and also in the book by Jeffrey ([Jeffrey-1997]).

#### See also:

The Lipinski violations and hydrogen-bond acceptors sections in the Filter Files chapter.

### 1.3.8 Aggregators

The Shoichet lab ([McGovern-2003], [Seidler-2003]) has demonstrated the importance of small-molecule aggregation in medium and high-throughput assays. Because these small-molecule aggregates can sequester some proteins, they give the appearance of being active inhibitors. There are now several hundred published aggregators in addition to a published QSAR model for predicting aggregation propensity. The user has the ability to eliminate any of the known aggregators as well as the ability to eliminate compounds that are predicted to be aggregators using the QSAR model. In OpenEye's experience, the published QSAR model for predicting aggregators is quite aggressive. It occasionally identifies compounds that are known to be genuine small-molecule inhibitors of a specific protein. While in most cases this model can be useful, until more definitive work is published, we feel you should gain some experience with the model and judge its performance for yourself.

More recent work in industry indicates that in some cases, aggregation properties are specific to the particular experimental conditions being used. Thus we recommended caution in the interpretation of these predictions. Nevertheless, aggregation remains an important issue in HTS hit follow-up and, short of experimental validation, this flag may be the best-available.

#### See also:

The aggregators parameter in the Filter Files chapter.

### **1.3.9 PAINS**

The PAINS filters ([Baell-2010]) are a set of functional group filters created to identify and filter promiscuous (nonspecific) actives across a number of screening types and targets. The original PAINS paper includes a set of functional group prefilters, created via two iterations of their work, and three sets of structure class filters, called filter sets A, B, and C, which were used to identify and remove promiscuous actives. The OpenEye PAINS filter set is a combination of all four filter sets (the functional group prefilter set plus the three structural class sets) into a single filter set.

There are two distinct use cases for the PAINS filters. The first is the typical prefiltering of structures prior to screening or compound selection to remove undesirable molecules. One can simply eliminate any molecules which fail the PAINS filtering.

The second use case, which may ultimately be more interesting, is to use the PAINS filters retrospectively on a set of data which has been filtered (and tested) using another methodology. In this scenario the PAINS filters can be used to identify potentially problematic reactive functionality in otherwise reasonable, drug-like structures. By using the table output mode and identifying matches for the A, B, and C filter sets, one can identify fairly specific chemical functionalities that have been known to result in non-specific activity. This can be useful information for either prioritizing further lead development or for modifying lead structures to mitigate adverse reactivity.

There are approximately 650 SMARTS rules which have been converted from the SLN query strings provided in the supplemental information for the original paper. For the functional group filters, the authors do not provide identifying names for each individual filter, so our PAINS rules are named based on the comments used to describe each functional group class, prefixed with the string pains fq [classname]. For the structural class filters, the authors provided unique RegID values for each filter. For those cases our rules are named based on the PAINS group and RegID as pains [group] [RegID].

Note that in certain cases it isn't possible to exactly represent the SLN queries given in the paper with a single SMARTS, so in those cases the rules have been split out into multiple SMARTS patterns and are named pains [group] [RegID]1, pains [group] [RegID]2, etc.

**Hint:** Unlike the other filter types, the PAINS filter consists only of functional group filters; no physical property filters are included. It may be desirable to combine the PAINS filter with a separate user-defined set of physical property filters. The section *filter file* describes creating additional filter rules.

## **1.4 Filter Files**

There are two parameter files a user can provide if they would like to override or augment the default parameter sets. The first is the "filter file". It provides acceptable limits for all of the physical properties and functional groups in the default filter. The second is the "newrule file". If you have a filter you like, but would like to augment it with a set of additional rules, these can be added with a newrule file.

There are four types of statements that can occur in a filter file:

- physical property limits
- rules
- new rules
- selections

The statements should occur one-per-line in the filter file.

Note: If the appropriate line is not in the filter file, or the value is false, the respective measure will not be used in filtering and its value will not be included in any table-based output.

### **1.4.1 Physical Property Limits**

There are a large number of physical property limits. They occur as three fields on a line. For example:

MIN\_HETEROATOMS 2 "Minimum number of heteroatoms"

The first field is the property keyword, the second field is the value assigned to that keyword, and the third field is a brief informational message. There are a fixed number of physical property keywords. No additional physical property keywords can be added by the user. The current keywords and brief definitions of each are listed below.

**Hint:** The values listed below are those found in the default *BlockBuster* filter.

#### **Basic Properties**

#### **Molecular Weight**

Isotopic molecular weight

```
MIN MOLWT 130 "Minimum molecular weight"
MAX_MOLWT 781 "Maximum molecular weight"
```

#### **Heavy Atom Count**

#### Number of non-hydrogen atoms

```
MIN_NUM_HVY 9 "Minimum number of heavy atoms"
MAX_NUM_HVY 55 "Maximum number of heavy atoms"
```

#### **Carbon Count**

Number of carbons

```
MIN_CARBONS 3 "Minimum number of carbons"
MAX_CARBONS 41 "Maximum number of carbons"
```

#### **Hetero-Count**

Number of non-carbon and non-hydrogen atoms

```
MIN HETEROATOMS 1 "Minimum number of heteroatoms"
MAX_HETEROATOMS 14 "Maximum number of heteroatoms"
```

### **Hetero-Atom to Carbon Ratio**

#### Hetero-count/carbon-count

```
MIN_Het_C_Ratio 0.04 "Minimum heteroatom to carbon ratio"
MAX_Het_C_Ratio 4.0 "Maximum heteroatom to carbon ratio"
```

#### **Chiral Count**

Number of chiral atoms

```
MIN_CHIRAL_CENTERS 0 "Minimum chiral centers"
MAX_CHIRAL_CENTERS 21 "Maximum chiral centers"
```

#### **Hydrogen-bond Acceptors**

Number of atoms which match any of the following:

- degree 2, aromatic, non-positive nitrogens. An example is shown below.
- electron rich or negative, valence less than 4, non-aromatic nitrogens. An example is shown below.
- negatively charged or not electron withdrawn, neutral, non-aromatic oxygens. An example is shown below.
- degree 1, double bonded, electron rich, non-aromatic sulfur. An example is shown below.

This definition is from the work of Mills and Dean ([Mills-Dean-1996]) and also the book by Jeffrey ([Jeffrey-1997]).

MIN\_HBOND\_ACCEPTORS 0 "Minimum number of hydrogen-bond acceptors" MAX\_HBOND\_ACCEPTORS 13 "Maximum number of hydrogen-bond acceptors"

![](_page_19_Figure_1.jpeg)

**Generated by Grapheme TK** 

- · OEGetHBondAcceptorCount function
- Lipinski and Hydrogen-bonds section

![](_page_20_Figure_1.jpeg)

## **Hydrogen-bond Donors**

Number of hydrogen atoms on nitrogen, oxygen, or sulfur atoms. This definition is from the work of Mills and Dean ([Mills-Dean-1996]) and also the book by Jeffrey ([Jeffrey-1997]).

MIN\_HBOND\_DONORS 0 "Minimum number of hydrogen-bond donors" MAX\_HBOND\_DONORS 9 "Maximum number of hydrogen-bond donors"

See also:

· OEGetHBondDonorCount function

• Lipinski and Hydrogen-bonds section

#### **Lipinski Acceptors**

Number of nitrogens or oxygens. This definition is from the work of Lipinski ([Lipinski-1997]).

```
MIN_LIPINSKI_ACCEPTORS 1 "Minimum number of oxygen & nitrogen atoms"
MAX_LIPINSKI_ACCEPTORS 14 "Maximum number of oxygen & nitrogen atoms"
```

See also:

- · OEGetLipinskiAcceptorCount function
- Lipinski and Hydrogen-bonds section

#### **Lipinski Donors**

Number of nitrogens and oxygens with at least one hydrogen attached. This definition is from the work of Lipinski ([Lipinski-1997]).

```
MIN LIPINSKI DONORS 0 "Minimum number O & N atoms with hydrogens"
MAX_LIPINSKI_DONORS 6 "Maximum number O & N atoms with hydrogens"
```

#### See also:

- · OEGetLipinskiDonorCount function
- · Lipinski and Hydrogen-bonds section

#### **Halide Fraction**

Percent of molecular weight from halides

```
MIN_HALIDE_FRACTION 0.0 "Minimum Halide Fraction"
MAX_HALIDE_FRACTION 0.66 "Maximum Halide Fraction"
```

See also:

· OEGetHalideFraction function

## **Formal Count**

Number of atoms with a formal charge (excludes dative)

```
MIN_COUNT_FORMAL_CRG 0 "Minimum number formal charges"
MAX_COUNT_FORMAL_CRG_4 "Maximum number of formal charges"
```

### **Formal Sum**

#### Total formal charge

```
MIN_SUM_FORMAL_CRG -2 "Minimum sum of formal charges"
MAX_SUM_FORMAL_CRG 2 "Maximum sum of formal charges"
```

#### **Connected Non-Ring**

Considers sets of contiguous (bonded) non-ring atoms

```
MIN_CON_NON_RING 0 "Minimum number of connected non-ring atoms"
MAX_CON_NON_RING 19 "Maximum number of connected non-ring atoms"
```

#### **Unbranched Chains**

The size of the longest chain of either heavy atoms or of all carbons. An unbranched atom is an atom with at most two connections to other heavy atoms and is not in a ring. A set of unbranched atoms which are connected together form a chain. A molecule may contain multiple chains which are isolated from each other by non-chain atoms (e.g. ring or branched atoms). The longest chain of heavy atoms and the longest chain of carbons are identified, and the MIN and MAX parameter filters are applied.

```
MIN_UNBRANCHED 1 "Minimum number of connected unbranched non-ring atoms"
MAX_UNBRANCHED 13 "Maximum number of connected unbranched non-ring atoms"
MIN_UNBRANCHED_C 0 "Minimum number of connected unbranched non-ring carbon"
MAX_UNBRANCHED_C 6 "Maximum number of connected unbranched non-ring carbon"
```

#### See also:

- · OEGetLongestUnbranchedHeavyAtomsChain function
- · OEGetLongestUnbranchedCarbonsChain function

#### **Total Functional Group Count**

Total number of functional groups. Does not count any ring-systems as functional groups. Degree 1 heteroatoms, particularly those with double bonds or dative bonds are considered part of ring systems and do not count as a functional group.

```
MIN_FCNGRP 0 "Minimum number of functional groups"
MAX_FCNGRP 7 "Maximum number of functional groups"
```

**Note:** This is different then the functional group rules.

#### **Ring Systems**

Number of ring systems (contiguous systems of ring atoms and bonds)

```
MIN_RING_SYS 0 "Minimum number of ring systems"
MAX_RING_SYS 5 "Maximum number of ring systems"
```

#### **Ring Size**

Maximum size of any single ring system

```
MIN_RING_SIZE 0 "Minimum atoms in any ring system"
MAX_RING_SIZE 20 "Maximum atoms in any ring system"
```

#### **Rotor Count**

Number of rotatable bonds. Allows optional adjustment for aliphatic rings following the method of [Oprea-2000].

```
MIN ROT BONDS 0 "Minimum number of rotatable bonds"
MAX_ROT_BONDS 16 "Maximum number of rotatable bonds"
ADJUST_ROT_FOR_RING true "BOOLEAN for whether to estimate degrees of freedom in rings"
```

#### See also:

· OEGetRotatableBondCount function

### **Rigid Count**

Number of rigid bonds (non-rotatable bonds)

```
MIN_RIGID_BONDS 4 "Minimum number of rigid bonds"
MAX_RIGID_BONDS 55 "Maximum number of rigid bonds"
```

#### **Unspecified Atom Stereo**

Number of unspecified atom stereos

```
MIN_UNSPECIFIED_ATOM_STEREOS 0 "Minimum number of unspecified atom stereos"
MAX_UNSPECIFIED_ATOM_STEREOS 2 "Maximum number of unspecified atom stereos"
```

Note: MIN\_UNSPECIFIED\_ATOM\_STEREOS and MAX\_UNSPECIFIED\_ATOM\_STEREOS are not used for filtering in the default filters.

- · OEGetNumUnspecifiedAtomStereosfunction
- stereo atom
- Stereochemistry Perception chapter

· OEAtomBase.HasStereoSpecified

#### **Unspecified Bond Stereo**

Number of unspecified bond stereos

```
MIN_UNSPECIFIED_BOND_STEREOS 0 "Minimum number of unspecified bond stereos"
MAX_UNSPECIFIED_BOND_STEREOS 2 "Maximum number of unspecified bond stereos"
```

Note: MIN\_UNSPECIFIED\_BOND\_STEREOS and MAX\_UNSPECIFIED\_BOND\_STEREOS are not used for filtering in the default filters.

#### See also:

- OEGetNumUnspecifiedBondStereosfunction
- stereo bond
- Stereochemistry Perception chapter
- · OEBondBase.HasStereoSpecified

#### **Atom Type Checks**

Check the validity of atom charges, valences or MMFF atom types for the entire molecule.

```
TYPECHECK
              false "Screen for unusual valences or charges"
MMFFTYPECHECK false "Screen for atoms with unknown MMFF atom types"
```

#### See also:

- Type Checking
- · OEFilter. SetTypeCheck
- MMFF94 Atom Type Checking
- · OEFilter. SetMMFFTypeCheck

#### **LogP**

The logP calculation is a derivative of the published XLOGP algorithm [Wang-R-1997] but reparameterized without the dependence on 3D coordinates or the SYBYL/Mol2 aromaticity model.

#### **XLogP**

#### Calculated LogP

```
MIN_XLOGP -3.0 "Minimum XLogP"
MAX_XLOGP 6.85 "Maximum XLogP"
```

#### **Solubility**

The solubility predictions are based on using the atom types from the XLOGP algorithm (see [Wang-R-1997]) and reparameterizing them based on available solubility data. Rather than a quantitative cutoff, solubility uses categories. The six allowable categories are:

- 1. insoluble
- 2. poorly
- 3. moderately
- 4. soluble
- 5. very
- 6. highly

These categories are keywords used in the filter files as follows.

### **Solubility**

Calculated solubility class

```
MIN_SOLUBILITY insoluble "Minimum solubility"
```

## **Pharmacokinetic Predictors**

Several secondary filters that are built upon published combinations of simpler properties are available.

```
Note: All of these properties are used for filtering in the default filters.
```

## **Anionic Carbon Count**

Number of anionic carbons

```
MIN_ANION_C 0 "Minimum number of anionic carbons"
MAX_ANION_C 2 "Maximum number of anionic carbons"
```

Note: MIN\_ANION\_C and MAX\_ANION\_C are not used for filtering in the default filters.

#### See also:

· OEGetAnionicCarbonCount function

## **Lipinski Violations**

Number of allowable Lipinski violations. A single Lipinski violation is considered acceptable. The published work, [Lipinski-1997], allows compounds to pass with a single violation but not multiple violations.

MAX LIPINSKI 3 "Maximum number of Lipinski violations"

#### See also:

The Lipinski theory section in the Molecular Properties and Predictors chapter.

#### **PSA**

Peter Ertl's, [Ertl-2000], topological polar surface area (phosphorus and sulfur area is optional).

```
PSA USE SandP false "Count S and P as polar atoms"
MIN 2D PSA 0.0 "Minimum 2-Dimensional (SMILES) Polar Surface Area"
MAX_2D_PSA_205.0 "Maximum 2-Dimensional (SMILES) Polar Surface Area"
```

#### See also:

The PSA theory section in the Molecular Properties and Predictors chapter.

## **GSK/Veber**

Veber's measure of bioavailability (PSA > 140 or Rotatable bonds >10). [Veber-2002].

```
GSK_VEBER false "PSA>140 or >10 rot bonds"
```

#### **Abbott/Martin**

Yvonne Martin's Abbott Bioavailability Score. This is reported as a probability that F>10% in rats. [Martin-2005]

```
MIN_ABS 0.11 "Minimum probability F>10% in rats"
```

#### **Pharmacopia/Egan**

Egan egg measure of bioavailability (LogP > 5.88 or PSA > 131.6). [Egan-2000]

PHARMACOPIA false "LogP > 5.88 or PSA > 131.6"

#### **Aggregators**

Aggregators are small molecules that can interfere with assay results by sequestering protein in an aggregation of small molecules in solution. They appear to have activity in many assays, but in fact are usually not specific inhibitors of the protein in question. Includes two measures of whether a molecule is one of the aggregators defined by Shoichet et. al. [McGovern-2003] [Seidler-2003] The first measure, AGGREGATORS, is whether the molecule is an exact match to one of the approximately 400 published aggregators. The second measure, PRED\_AGG, is whether the molecule hits in Shoichet's QSAR model for predicting aggregators.

#### **Aggregators**

Whether a compound is known or predicted to aggregate in concentrations common in virtual screening.

```
AGGREGATORS true "Eliminate known aggregators"
PRED_AGG false "Eliminate predicted aggregators"
```

### **Elemental Filters**

The elemental filters are applied in this order:

- 1. Test for the existence of any of the metals in the ELIMINATE\_METALS filter in the molecule.
- 2. Remove salts by stripping away all the disconnected components except for the largest.
- 3. Test to make sure only atoms specified in ALLOWED\_ELEMENTS filter are in the molecule.

#### See also:

- Metal Removal
- Salt Removal

The format of the two elemental filter fields is the keyword followed by a comma delimited list of atomic symbols.

### **Eliminate Metals**

Any molecule with the atoms indicated in ELIMINATE METALS fail to pass the filter.

ELIMINATE\_METALS Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd

#### **Allowed Elements**

Molecules with atoms other than those specified by ALLOWED\_ELEMENTS fail to pass the filter.

```
ALLOWED_ELEMENTS H, C, N, O, F, P, S, Cl, Br, I
```

### **1.4.2 Functional Group Rules**

Rules statements set the limits for the maximum number of the specified type of functional group that may be allowed in the molecule.

The first field of a rule statement is the word RULE in all capital letters. The second field is a number indicating the maximum number of the group allowed in a molecule. The third field is the functional group keyword. Functionalgroup keywords are case sensitive.

```
RULE 0 acid_halide
```

The following is a list of functional groups which filter recognizes by default. Three example matches are provided with the atoms that correspond to each other highlighted.

Note: Due to the highly complex nature of the patterns, in particular recursive SMARTS, it is not possible to fully highlight every atom that was included as part of the match.

### acetal

![](_page_28_Figure_8.jpeg)

#### acid

![](_page_28_Figure_10.jpeg)

## acid chloride

![](_page_29_Figure_2.jpeg)

## acid\_halide

![](_page_29_Figure_4.jpeg)

## acyclic\_NCN

![](_page_29_Figure_6.jpeg)

## acyclic\_NS

![](_page_30_Figure_2.jpeg)

## acyl\_cyanides

![](_page_30_Picture_4.jpeg)

# acylhydrazide

![](_page_30_Figure_6.jpeg)

alcohol

![](_page_31_Figure_2.jpeg)

## aldehyde

![](_page_31_Figure_4.jpeg)

## alkene

![](_page_31_Figure_6.jpeg)

alkyl

![](_page_32_Figure_2.jpeg)

## alkyl\_halide

![](_page_32_Figure_4.jpeg)

## alkyl\_phosphate

![](_page_32_Figure_6.jpeg)

alkylaniline

![](_page_33_Figure_2.jpeg)

## alkylating\_agent

![](_page_33_Figure_4.jpeg)

## alkyne

![](_page_33_Figure_6.jpeg)

## alphahalo amine

![](_page_34_Figure_2.jpeg)

## alphahalo\_ketone

![](_page_34_Figure_4.jpeg)

## amide

![](_page_34_Figure_6.jpeg)

aminal

![](_page_35_Figure_2.jpeg)

amine

![](_page_35_Figure_4.jpeg)

amino\_acid

![](_page_35_Figure_6.jpeg)

## anhydride

![](_page_36_Figure_2.jpeg)

aniline

![](_page_36_Figure_4.jpeg)

## aniline\_unsubstituted

![](_page_36_Figure_6.jpeg)

arene

![](_page_37_Figure_2.jpeg)

## arenesulfonyl

![](_page_37_Picture_4.jpeg)

## aryl

![](_page_37_Figure_6.jpeg)

## aryl halide

![](_page_38_Figure_2.jpeg)

aryl\_mono\_Brl

![](_page_38_Figure_4.jpeg)

azide

![](_page_38_Figure_6.jpeg)

aziridine

![](_page_39_Figure_2.jpeg)

#### azo

![](_page_39_Figure_4.jpeg)

## azocyanamides

![](_page_39_Figure_6.jpeg)

base

![](_page_40_Figure_2.jpeg)

## benzyl\_ether

![](_page_40_Picture_4.jpeg)

## benzyloxycarbonyl\_CBZ

![](_page_40_Figure_6.jpeg)

## beta azo carbonyl

![](_page_41_Figure_2.jpeg)

## beta\_carbonyl\_quat\_nitrogen

![](_page_41_Picture_4.jpeg)

## beta\_halo\_carbonyl

![](_page_41_Figure_6.jpeg)

## carbamate

![](_page_42_Figure_2.jpeg)

## carbamic\_acid

![](_page_42_Figure_4.jpeg)

## carbodiimide

![](_page_42_Figure_6.jpeg)

carbonate

![](_page_43_Figure_2.jpeg)

carbonyl

![](_page_43_Picture_4.jpeg)

carboxylic\_acid

![](_page_43_Figure_6.jpeg)

# cation\_C\_CI\_I\_P\_or\_S

![](_page_44_Figure_2.jpeg)

## charge

![](_page_44_Figure_4.jpeg)

## cyanohydrins

![](_page_44_Figure_6.jpeg)

## cycloheximide derivatives

![](_page_45_Figure_2.jpeg)

# cyclopropyl

![](_page_45_Picture_4.jpeg)

## cytochalasin\_derivatives

![](_page_45_Figure_6.jpeg)

# di\_peptide

![](_page_46_Figure_2.jpeg)

## dioxane\_6MR

![](_page_46_Picture_4.jpeg)

## dioxolane\_5MR

![](_page_46_Picture_6.jpeg)

disulfide

![](_page_47_Figure_2.jpeg)

## dithioacetal

![](_page_47_Figure_4.jpeg)

## dye

![](_page_47_Figure_6.jpeg)

enamine

![](_page_48_Figure_2.jpeg)

enol\_ether

![](_page_48_Picture_4.jpeg)

epoxide

![](_page_48_Figure_6.jpeg)

ester

![](_page_49_Figure_2.jpeg)

### ether

![](_page_49_Figure_4.jpeg)

# fluorenylmethoxycarbonyl\_Fmoc

| Image: Chemical structure (naphthalene derivative with amide group; caption "Generated by OEDepict TK" visible beneath the drawing) |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------|--|--|
|-------------------------------------------------------------------------------------------------------------------------------------|--|--|

## guanidine

![](_page_50_Figure_2.jpeg)

halide

![](_page_50_Figure_4.jpeg)

halo\_alkene

![](_page_50_Figure_6.jpeg)

## halo\_amine

## halopyrimidine

![](_page_51_Figure_3.jpeg)

## hemiacetal

![](_page_51_Figure_5.jpeg)

### hemiaminal

![](_page_51_Figure_7.jpeg)

## hemiketal

![](_page_52_Figure_2.jpeg)

## hetatm

![](_page_52_Figure_4.jpeg)

## hetero\_hetero

## **HOBT\_esters**

![](_page_52_Figure_7.jpeg)

hydrazine

![](_page_53_Figure_2.jpeg)

## hydrazone

![](_page_53_Figure_4.jpeg)

## hydroxamic\_acid

![](_page_53_Figure_6.jpeg)

## hydroxyl

![](_page_54_Figure_2.jpeg)

## hydroxylamine

![](_page_54_Figure_4.jpeg)

## imidoyl\_chlorides

![](_page_54_Figure_6.jpeg)

imine

![](_page_55_Figure_2.jpeg)

imino

![](_page_55_Figure_4.jpeg)

iodine

![](_page_55_Figure_6.jpeg)

## iodoso

![](_page_56_Figure_2.jpeg)

# iodoxy

![](_page_56_Figure_4.jpeg)

## isocyanate

![](_page_56_Figure_6.jpeg)

isonitrile

![](_page_57_Figure_2.jpeg)

## isothiocyanate

![](_page_57_Figure_4.jpeg)

## ketal

![](_page_57_Figure_6.jpeg)

ketone

![](_page_58_Figure_2.jpeg)

lactam

![](_page_58_Figure_4.jpeg)

lactone

![](_page_58_Figure_6.jpeg)

## lawesson s reagent

![](_page_59_Figure_2.jpeg)

## long\_aliphatic\_chain

![](_page_59_Picture_4.jpeg)

## malonic

![](_page_59_Figure_6.jpeg)

mercapto

![](_page_60_Figure_2.jpeg)

## methoxyethoxymethyl\_MEM

![](_page_60_Picture_4.jpeg)

## methyl\_ketone

![](_page_60_Figure_6.jpeg)

## michael\_acceptor

![](_page_61_Figure_2.jpeg)

## monensin\_derivatives

![](_page_61_Picture_4.jpeg)

## mono\_alkene

![](_page_61_Figure_6.jpeg)

## mono alkyne

![](_page_62_Figure_2.jpeg)

nitrile

![](_page_62_Figure_4.jpeg)

nitro

![](_page_62_Figure_6.jpeg)

nitroso

![](_page_63_Figure_2.jpeg)

# N\_methoyl

![](_page_63_Figure_4.jpeg)

## nonacylhydrazone

![](_page_63_Figure_6.jpeg)

noxide

![](_page_64_Figure_2.jpeg)

# N\_P\_S\_Halides

![](_page_64_Picture_4.jpeg)

## NS\_beta\_halothyl

![](_page_64_Figure_6.jpeg)

nucleophile

![](_page_65_Figure_2.jpeg)

organometallic

![](_page_65_Figure_4.jpeg)

oxalyl

![](_page_65_Figure_6.jpeg)

## oxaziridine

![](_page_66_Figure_2.jpeg)

### oxime

![](_page_66_Figure_4.jpeg)

## oxygen\_cation

![](_page_66_Figure_6.jpeg)

## paranitrophenyl\_esters

![](_page_67_Figure_2.jpeg)

## pentafluorophenyl\_esters

![](_page_67_Picture_4.jpeg)

## perhalo\_ketone

![](_page_67_Figure_6.jpeg)

## peroxide

![](_page_68_Figure_2.jpeg)

phenol

![](_page_68_Figure_4.jpeg)

## phosphanes

![](_page_68_Figure_6.jpeg)

# phosphinic\_acid

![](_page_69_Figure_2.jpeg)

## phosphonamide

![](_page_69_Figure_4.jpeg)

## phosphonic\_acid

![](_page_69_Figure_6.jpeg)

## phosphonic\_ester

![](_page_70_Figure_2.jpeg)

# phosphonylnitrile

![](_page_70_Picture_4.jpeg)

## phosphoramides

![](_page_70_Figure_6.jpeg)

## phosphoranes

![](_page_71_Figure_2.jpeg)

## phosphoric\_acid

![](_page_71_Figure_4.jpeg)

## phosphoric\_ester

![](_page_71_Figure_6.jpeg)

# phosphoryl

![](_page_72_Figure_2.jpeg)

# phosphoryl

![](_page_72_Figure_4.jpeg)

## phthalimides\_PHT

![](_page_72_Figure_6.jpeg)

polyenes

![](_page_73_Figure_2.jpeg)

## primary\_amine

![](_page_73_Figure_4.jpeg)

## propiolactones

![](_page_73_Figure_6.jpeg)

## pseudo amine

![](_page_74_Figure_2.jpeg)

## quinone

![](_page_74_Picture_4.jpeg)

## ring

![](_page_74_Figure_6.jpeg)

## saponin\_derivatives

![](_page_75_Figure_2.jpeg)

## SCN<sub>2</sub>

![](_page_75_Figure_4.jpeg)

## secondary\_amine

![](_page_75_Figure_6.jpeg)

## squalestatin\_derivatives

| Image: chemical structure<br><i>Generated by OEDepict TK</i> |  |  |
|--------------------------------------------------------------|--|--|
|--------------------------------------------------------------|--|--|

## sulfide

![](_page_76_Picture_4.jpeg)

## sulfinimine

![](_page_76_Figure_6.jpeg)

# sulfinylthio

![](_page_77_Figure_2.jpeg)

## sulfonamide

![](_page_77_Figure_4.jpeg)

## sulfone

![](_page_77_Figure_6.jpeg)

## sulfonic acid

![](_page_78_Figure_2.jpeg)

## sulfonic\_ester

![](_page_78_Figure_4.jpeg)

## sulfonimine

![](_page_78_Figure_6.jpeg)

## sulfonyl halide

![](_page_79_Figure_2.jpeg)

## sulfonylnitrile

![](_page_79_Picture_4.jpeg)

## sulfonylurea

![](_page_79_Figure_6.jpeg)

## sulfoxide

![](_page_80_Figure_2.jpeg)

## t\_butyldimethylsilyl\_TBDMS

![](_page_80_Picture_4.jpeg)

## t\_butyIdiphenyIsilyI\_TBDPS

![](_page_80_Picture_6.jpeg)

# t\_butyl\_ether

![](_page_81_Figure_2.jpeg)

# t\_butoxycarbonyl\_tBOC

![](_page_81_Picture_4.jpeg)

## terminal\_vinyl

![](_page_81_Figure_6.jpeg)

## tertiary amine

![](_page_82_Figure_2.jpeg)

## tetrahydropyran\_THP

![](_page_82_Picture_4.jpeg)

## thioamide

![](_page_82_Figure_6.jpeg)

## thiocarbamate

![](_page_83_Figure_2.jpeg)

## thiocarbonyl

![](_page_83_Figure_4.jpeg)

## thioester

![](_page_83_Figure_6.jpeg)

thiol

![](_page_84_Figure_2.jpeg)

## thiourea

![](_page_84_Picture_4.jpeg)

## triacyloxime

![](_page_84_Figure_6.jpeg)

triazine

![](_page_85_Figure_2.jpeg)

## tricarbo\_phosphene

![](_page_85_Picture_4.jpeg)

## triflates

## triisopropylsilyl\_TIPS

![](_page_85_Figure_7.jpeg)

## trimethylsilyl TMS

![](_page_86_Figure_2.jpeg)

## unbranched\_chain

![](_page_86_Figure_4.jpeg)

### urea

![](_page_86_Figure_6.jpeg)

### 1.4.3 New Rules

New rules specify additional functional groups or substructures that may be used. They must specify a substructure definition in the form of a SMARTS in addition to the substructure name and maximum limit. For example:

NEWRULE norbornane 1 C1CC2CCC1C2

The first field is the NEWRULE keyword. The second field defines the name associated with the substructure (primarily for logging purposes). The third field indicates the maximum number of the substructure that can be allowed. The fourth field is the SMARTS string for the substructure, norbornane in this case. This example rule would indicate that molecules with a single norbornane substructure would be allowable, but that those with 2 or more norbornanes would be eliminated.

New rules that have a name that is identical with one of the original rules take precedence over the original rule.

### **1.4.4 Selection Statements**

The select statement allows a filter file to specify the required number of substructures in order to be able to pass the filter. These statements are similar to new rules except that they list a required range for passing the filter rather than the range for failing to pass the filter. For example:

SELECT amine 1 1 [N; ! $$(*-*[!#6; !#1])$ ; ! $$(*-a)$ ; ! $$(*=, **)]$ 

The first field is the SELECT keyword. The second field indicates the name for the selection (again for logging purposes). The third field is the minimum number of substructures required to be in the molecule. The fourth field is the maximum number of substructures allowed in the molecule. The fifth field is the substructure defined by a SMARTS pattern. The example requires that molecules contain exactly one amine. Currently, only a single SELECT statement is allowed in the filter file. Any complex boolean substructure statements can be incorporated directly into the SMARTS. If multiple SELECT statements occur in a filter file, only the final one will be applied.

## **CHAPTER**

# **TWO**

# **EXAMPLES**

# 2.1 MolProp TK Examples

The following table lists the currently available MolProp TK examples:

| Program                   | Description                                                       |
|---------------------------|-------------------------------------------------------------------|
| <i>molfilter.py</i>       | basic filtering for a molecule file                               |
| <i>quietfilter.py</i>     | silencing OEFilter logging messages                               |
| <i>molproptable.py</i>    | generating tabular output of all molecular properties             |
| <i>specificmolprop.py</i> | extract specific property (Lipinski violations) from table output |
| <i>molpropsddata.py</i>   | attach molecular properties as SD data                            |
| <i>molpropcsv.py</i>      | write molecular properties to a CSV file                          |

**Examples:** 

# 2.1.1 Basic Filtering for a Molecule File

All filtering operations are controlled via the OEFilter object. The OEFilter object is typically configured with a specified filter and then applied iteratively over a molecule file. This example demonstrates configuring the OEFilter object with the lead-like filter and then writes out the molecules that pass the filter. The OEFilter. operator () method is used to test whether the molecule passes the filter.

Note: The molecule will also be altered by all the specified Filter Preprocessing steps.

### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python molfilter.py --help
```

will generate the following output:

```
Simple parameter list
filter options :
   -filtertype : filter type
```

```
input/output options :
  -in : Input filename
  -out : Output filename
```

Usage: ./molfilter <input> <output>

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
# Filter a molecule file for "Lead-like" molecules
#######################################
import sys
from openeye import oechem
from openeye import oemolprop
def main(argy=[ name ]):
    itf = oechem. OEInterface (InterfaceData)
   oemolprop.OEConfigureFilterParams(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = \text{iff}. \text{GetString}("-in")oname = \text{itf}.\text{GetString}("-out")if s = oechem. oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   ofs = occhem.oemolostream()if not ofs.open(oname):
       oechem. OEThrow. Fatal ("Cannot create output file!")
    ftype = oemolprop.OEGetFilterType(itf)
    filt = oemolprop.OEFilter(ftype)
```

```
(continued from previous page)
```

```
filt.SetErrorLevel(oechem.OEErrorLevel_Info)
   for mol in ifs.GetOEGraphMols():
       if filt (mol):
           oechem.OEWriteMolecule(ofs, mol)
#######################################
# INTERFACE
#######################################
InterfaceData = \n'!BRIEF [-in] <input> [-out] <output>
!CATEGORY "input/output options :"
   !PARAMETER -in
     !ALIAS -i
     !TYPE string
     !REQUIRED true
     !KEYLESS 1
     !VISIBILITY simple
     !BRIEF Input filename
   ! END
   !PARAMETER -out
     !ALIAS -o
     !TYPE string
     !REQUIRED true
     !KEYLESS 2
     !VISIBILITY simple
     !BRIEF Output filename
   ! END
!END
\mathbf{r} \cdot \mathbf{r} .
if _name_ == "_main_":
   sys.exit(main(sys.argv))
```

- OEFilter class
- OEConfigureFilterParams and OEConfigureFilterType functions
- · OEGetFilterType function

#### **Examples**

prompt> python molfilter.py -in mcss.smi.gz -out .smi -filtertype Lead

The following is an example of the output:

```
CC1 = CC (=0) C = CC1 = 0NSC 1, Minimum atom count (10) not reached: 9
                                     NSC 2, Maximum disulfide (0) exceeded: 1
clecc2c(c1)nc(s2)SSc3nc4ccccc4s3
c1c (cc (c (c1 [N+] (=0) [O-]) [O-]) C1) [N+] (=0) [O-]
                                                   NSC 3, Maximum heteroatom to carbon.
\rightarrowratio(1.10) exceeded: 1.33
clc(sc(n1)N)[N+](=0)[O-] NSC 4, Minimum atom count (10) not reached: 9
c1ccc2c(c1) C (=0) c3ccc (cc3C2=0) N = 0NSC 5, Maximum dye(0) exceeded: 2
clccc (c (c1) c2c3ccc (c (c3oc-4c (c (=0) ccc24) Br) Br) 0) C (=0) [0-]
                                                                  NSC 6, Maximum atom.
\rightarrowcount (25) exceeded: 27
C[NH+] (C)C1=C(C(=0)c2ccccc2C1=0)C1 NSC 7, Maximum alkyl_halide(0) exceeded: 1
Cc1ccc2c(c1[N+](=0)[0-])C(=0)c3ccccc3C2=0
                                                NSC 8, Maximum nitro(0) exceeded: 1
CC(C) (C) clcc (c (cc10) C(C) (C) C) 0 NSC 11, Pass
CC1=NN(C(=0)C1)c2ccccc2 NSC
                               12, Pass
```

By default the OEFilter. operator () method will emit information to OEThrow about every molecule passed to it. This example prints that to the screen. The next example, *quietfilter*, shows how to suppress that output. Only the molecules that pass the filter will be written to the output file. The following is the format for what is emitted:

[Isomeric SMILES]\t[Title], [Pass|Reason for failure]

## 2.1.2 Quiet Filtering

Log output can be superfluous when using the OEFilter object in a more complex program. Since all the log output is written to the OEThrow object, the verbosity level can be lowered by using the OEThrow. Set Level method. This example demonstrates setting the OEThrow error level to OEErrorLevel\_Warning. This will only allow messages at the level of Warning or above to be emitted, thereby silencing the OEFilter object's logging output. The -verbose option can be used to change the OEThrow error level.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python quietfilter.py --help
```

#### will generate the following output:

```
Simple parameter list
filter options :
   -filtertype : filter type
input/output options :
   -in : Input filename
   -out : Output filename
other options :
   -verbose : Error level of messages
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
######################################
# Quietly filter a molecule file
#######################################
import sys
from openeye import oechem
from openeye import oemolprop
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
   itf = oechem. OEInterface (InterfaceData)
   oemolprop.OEConfigureFilterParams(itf)
   if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = \text{itf.}GetString("-in")oname = \text{itf}.\text{GetString}("-out")if s = occhem.oemolistream()if not ifs.open(iname):
        oechem. OEThrow. Fatal ("Cannot open input file!")
   ofs = occhem.oemolostream()if not ofs.open(oname):
        oechem. OEThrow. Fatal ("Cannot create output file!")
    ftype = oemolprop.OEGetFilterType(itf)
   filt = oemolprop.OEFilter(ftype)
   ver = itf.GetString("-verbose")if ver == "Verbose":oechem.OEThrow.SetLevel(oechem.OEErrorLevel_Verbose)
   elif ver == "Info":oechem.OEThrow.SetLevel(oechem.OEErrorLevel_Info)
    elif ver == "Warning":oechem. OEThrow. SetLevel (oechem. OEErrorLevel_Warning)
    elif ver == "Error":
```

```
(continued from previous page)
       oechem.OEThrow.SetLevel(oechem.OEErrorLevel_Error)
   else:
       oechem. OEThrow. Fatal ("Unrecognized error level!")
   for mol in ifs.GetOEGraphMols():
       if filt (mol) :
           oechem.OEWriteMolecule(ofs, mol)
#######################################
# INTERFACE
#######################################
InterfaceData = '''
!BRIEF [-verbose <verbose>] [-in] <input> [-out] <output>
!CATEGORY "input/output options :"
    !PARAMETER -in
     !ALIAS -i
     !TYPE string
     !REQUIRED true
     IKEYLESS 1
     !VISIBILITY simple
     !BRIEF Input filename
   ! END
   !PARAMETER -out
     !ALIAS -0
     !TYPE string
     !REQUIRED true
     !KEYLESS 2
     !VISIBILITY simple
     !BRIEF Output filename
   ! END
!END
!CATEGORY "other options :"
   !PARAMETER -verbose
   !TYPE string
   !REQUIRED false
   !DEFAULT Warning
    !LEGAL VALUE Verbose
    !LEGAL_VALUE Info
    !LEGAL VALUE Warning
   !LEGAL_VALUE Error
    !VISIBILITY simple
   !BRIEF Error level of messages
    !DETAIL
       Verbose
       Info
       Warning
       Error
  ! END
```

```
! END
\mathbf{r} \cdot \mathbf{r} \cdot \mathbf{r}{\sf name} == {\sf "main" :}if
       sys.exit(main(sys.argv))
```

See also:

- · OEFilter class
- OEConfigureFilterParams and OEConfigureFilterType functions
- · OEGetFilterType function
- OEErrorHandler class

#### **Examples**

prompt> python quietfilter.py -in mcss.smi.gz -out .smi -filtertype Lead

## 2.1.3 Molecular Property Table

The OEFilter object allows for the calculation of all the molecular properties it uses during the filtering process without actually applying the filter. This may be useful for caching the OEFilter object results into a database. The OEFilter. SetTable method can be used to specify where to write a tab-delimited table of every property in the associated filter file. This example demonstrates how to write the tabular output to standard out.

Note: A tab-delimited file format was chosen to integrate better with Unix commandline utilities. For example, this allows for quick and easy filter experimentation with the awk command line utility. The following snippet will print the number of molecules (plus one for the header) with a molecular weight greater than 200.

```
> python molproptable.py -in drugs.sdf -filtertype Lead > drugs.txt
> cat drugs.txt | awk -F\t '{if ($12 > 200) { print $12 }}' | wc -1
```

Furthermore, all database programs have utilities for importing tab-delimited files. Loading the filter results into a third-party database would provide very speedy filter experimentation since the properties would only have to be calculated once and then cached in the database.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python molproptable.py --help
```

will generate the following output:

```
Simple parameter list
filter options :
   -filtertype : filter type
 input/output options :
```

```
-in : Input filename
```

```
other options :
  -verbose : Error level of messages
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
# Generate a tabular output of molecular properties
#######################################
import sys
from openeye import oechem
from openeye import oemolprop
def main(argv=[_name_]):
   itf = oechem. OEInterface (InterfaceData)
   oemolprop.OEConfigureFilterParams(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = itf.GetString("-in")ifs = occhem.oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   ftype = oemolprop.OEGetFilterType(itf)
   filt = oemolprop.OEFilter(ftype)
   ver = itf.GetInt("-verbose")oechem.OEThrow.SetLevel(ver)
   pwnd = Falsefilt.SetTable(oechem.oeout, pwnd)
```

```
for mol in ifs. GetOEGraphMols():
       fit(mol)#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-in] <input> [-verbose] <verbose>
!CATEGORY "input/output options :"
   !PARAMETER -in
     !ALIAS -i
     !TYPE string
     !REQUIRED true
     !KEYLESS 1
     !VISIBILITY simple
     !BRIEF Input filename
   !END
! END
!CATEGORY "other options :"
   !PARAMETER -verbose
   !TYPE int
   !REQUIRED false
   !LEGAL_RANGE 2 5
   !DEFAULT 4
   !VISIBILITY simple
   !BRIEF Error level of messages
   !DETAIL
       2 is Verbose
       3 is Info
       4 is Warning
       5 is Error
 ! END
!END
\mathbf{t} , \mathbf{t} , \mathbf{t}if __name__ == "__main__".sys.exit(main(sys.argv))
```

- · OEFilter class
- OEConfigureFilterParams and OEConfigureFilterType functions
- · OEGetFilterType function

#### **Examples**

prompt> python molpropsdtable.py -in drugs.sdf -filtertype Lead

## **2.1.4 Specific Molecular Properties**

The OEFilter object table can also be used to retrieve specific molecular properties or filtering terms for which a free function does not exist. The number of molecular properties is large. In addition, some properties are more experimental than others. For these reasons *free functions* are not provided for everything that can be calculated. This example demonstrates how to extract a property, the number of Lipinski violations, from the OEFilter object molecular property table by writing the table to a oeosstream.

**Warning:** The exact number of fields the *OEFilter* object outputs depends on the *filter file* being used. The field will only be output if the filter rule is turned on. That is why this example will search the header line for the position of the "Lipinski violations" field. This key-value lookup is recommended for extracting specific fields from the filter table.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python specificmolprop.py --help
```

will generate the following output:

```
Simple parameter list
filter options :
  -filtertype : filter type
input/output options :
  -in : Input filename
   -out : Output filename
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
```

```
# liable for any damages or liability in connection with the Sample Code
# or its use.
#######################################
# Extract the number of Lipinski violations from the table output
#######################################
import sys
from openeye import oechem
from openeye import oemolprop
def main(argv=[__name__]):
   itf = oechem. OEInterface (InterfaceData)
   oemolprop.OEConfigureFilterParams(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = \text{itf}.\text{GetString}("-in")if s = oechem. oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   ftype = oemolprop.OEGetFilterType(itf)
   filt = oemolprop.OEFilter(ftype)
   ver = itf.getInt("-verbose")oechem.OEThrow.SetLevel(ver)
   ostr = oechem.oeosstream()
   pwnd = Falsefilt.SetTable(ostr, pwnd)
   headers = ostr.str() .split(b' \t')ostr.clear() # remove the header row from the stream
   for mol in ifs. GetOEGraphMols():
       filt (mol)
       fields = ostr.str(). decode ("UTF-8"). split ('\t')
       ostr. clear() # remove this row from the stream
       tmpdet = dict(zip(headers, fields))print (mol.GetTitle(), tmpdct [b"Lipinski violations"])
#######################################
# INTERFACE
#######################################
InterfaceData = \n'!BRIEF [-in] <input> [-verbose] <verbose>
!CATEGORY "input/output options :"
   !PARAMETER -in
```

```
!ALIAS -i
      ! TYPE string
      !REQUIRED true
      !KEYLESS 1
      !VISIBILITY simple
      !BRIEF Input filename
    ! END
!END
!CATEGORY "other options :"
    !PARAMETER -verbose
    ITYPE int
    !REOUIRED false
   !LEGAL RANGE 2 5
    !DEFAULT 4
    !VISIBILITY simple
    !BRIEF Error level of messages
    !DETAIL
        2 is Verbose
        3 is Info
        4 is Warning
        5 is Error
  !END
!END
1 - 1 - 1{\sf name} == {\sf "main" :}if
    sys.exit(main(sys.argv))
```

#### See also:

- · OEFilter class
- OEConfigureFilterParams and OEConfigureFilterType functions
- · OEGetFilterType function

#### **Examples**

```
prompt> python specificmolprop.py -in mcss.smi.qz -filtertype Lead
```

# 2.1.5 Attach Molecular Properties as SD Data

The molecular properties calculated by OEFilter can be attached as SD data to the molecule. The OEFilter.  $SetSDTag$  method is used to attach the calculated molecular properties to molecules passed to the filter object.

SD tag data corresponds to the *tabular data* functionality. The SD data tag names are exactly the same as the names found in the table header. The SD data values are exactly what is output in the data table. The only exceptions are the "SMILES", "Name", and "Filter" columns since this information can be obtained other ways.

This example demonstrates how to set the table output to the oenul output stream to allow all properties to be attached as SD data, and write the tabular data to an output in the OEFormat\_SDF, OEFormat\_OEB, or the OEFormat\_CSV format. To specifically write to the OEFOrmat\_CSV format, also see the MolPropCSV example.

Warning: By default, only the properties up to the failing property will be attached to each molecule. Use OEFilter. SetTable to force every property to be attached as SD data. The same rule applies to SD data as tabular output data, only the properties specified in the filter file will be attached as SD data.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python molpropsddata.py --help
```

will generate the following output:

```
Simple parameter list
filter options :
  -filtertype : filter type
input/output options :
  -in : Input filename
   -out : Output filename
other options :
  -verbose : Error level of messages
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
# Attach molecular properties as SD data
#######################################
import sys
from openeye import oechem
from openeye import oemolprop
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
```

```
oemolprop.OEConfigureFilterParams(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = itf.GetString("-in")oname = itf.GetString("-out")if s = oechem. oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   ofs = oechem.oemolostream()
   if not ofs.open(oname):
       oechem.OEThrow.Fatal("Cannot create output file!")
   fmt = ofs.GetFormat()if fmt not in [oechem. OEFormat_SDF, oechem. OEFormat_OEB, oechem. OEFormat_CSV]:
       oechem. OEThrow. Fatal ("Only SD, OEB, and CSV formats preserve SD data")
   ftype = oemolprop.OEGetFilterType(itf)
   filt = oemolprop.OEFilter(ftype)
   ver = itf.GetInt("-verbose")oechem.OEThrow.SetLevel(ver)
   pwnd = Falsefilt.SetTable(oechem.oenul, pwnd)
   filt.SetSDTag(True)
   for mol in ifs.GetOEGraphMols():
       filt(mol)oechem.OEWriteMolecule(ofs, mol)
#######################################
# INTERFACE
#######################################
InterfaceData = \cdots!BRIEF [-in] <input> [-out] <output> [-verbose] <verbose>
!CATEGORY "input/output options :"
   !PARAMETER -in
     !ALIAS -i
     !TYPE string
     !REQUIRED true
     IKEYLESS 1
     !VISIBILITY simple
     !BRIEF Input filename
   ! END
   !PARAMETER -out
     !ALIAS -<sub>o</sub>!TYPE string
     !REQUIRED true
```

```
!KEYLESS 2
      !VISIBILITY simple
      !BRIEF Output filename
    !END
!END
!CATEGORY "other options :"
   !PARAMETER -verbose
    !TYPE int
   !REQUIRED false
   !LEGAL_RANGE 2 5
   !DEFAULT 4
   !VISIBILITY simple
   !BRIEF Error level of messages
    !DETAIL
        2 is Verbose
        3 is Info
        4 is Warning
        5 is Error
  !END
!END
\mathbf{r} \cdot \mathbf{r} \cdot \mathbf{r} .
if name == " main ":
    sys.exit(main(sys.argv))
```

### See also:

- · OEFilter class
- OEConfigureFilterParams and OEConfigureFilterType functions
- · OEGetFilterType function

#### **Examples**

prompt> python molpropsddata.py -in drugs.sdf -out out\_mpsd.sdf -filtertype Lead

## 2.1.6 Write molecular properties to a CSV file

The molecular properties calculated by OEFilter can be written to a file in the OEFOrmat\_CSV format as described in the CSV File Format section. Every property specified in the *filter file* will be writtern in the tabular file.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python molpropcsv.py --help

will generate the following output:

```
Simple parameter list
filter options :
   -filtertype : filter type
input/output options :
   -in : Input filename
   -out : Output filename
other options :
   -verbose : Error level of messages
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
# Attach molecular properties as SD data
#######################################
import sys
from openeye import oechem
from openeye import oemolprop
def main(argv=[_name_]):
   itf = oechem. OEInterface(InterfaceData)
   oemolprop.OEConfigureFilterParams(itf)
```

```
(continued from previous page)
```

```
if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = itf.GetString("-in")oname = itf.GetString("-out")ifs = occhem.oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   ftype = oemolprop.OEGetFilterType(itf)
   filt = oemolprop.OEFilter(ftype)
   ver = itf.getInt("-verbose")oechem.OEThrow.SetLevel(ver)
   oemolprop.OEWritePropertyDataToCSV(oname, ifs, filt)
#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-in] <input> [-out] <output> [-verbose] <verbose>
!CATEGORY "input/output options :"
   !PARAMETER -in
     !ALIAS -i
     !TYPE string
     !REQUIRED true
     !KEYLESS 1
     !VISIBILITY simple
     !BRIEF Input filename
   LEND
   !PARAMETER -out
     !ALIAS -o
     !TYPE string
     !REOUIRED true
     !KEYLESS 2
     !VISIBILITY simple
     !BRIEF Output filename
   ! END
!END
!CATEGORY "other options :"
   !PARAMETER -verbose
   !TYPE int
   !REOUIRED false
   !LEGAL RANGE 2 5
   !DEFAULT 4
   !VISIBILITY simple
```

```
!BRIEF Error level of messages
    !DETAIL
        2 is Verbose
        3 is Info
        4 is Warning
        5 is Error
  !END
!END
1 - 1 - 1if _name_ = "main_":
    sys.exit(main(sys.argv))
```

See also:

- OEFilter class
- · OEConfigureFilterParams and OEConfigureFilterType functions
- · OEWritePropertyDataToCSV function

#### **Examples**

prompt> python molpropcsv.py -in drugs.sdf -out out\_drugs.csv -filtertype Lead

# 2.2 Python Cookbook Examples

There are large number of code examples available in OpenEye Python Cookbook that use OpenEye Toolkits to solve a wide range of cheminformatics and molecular modeling problems.

- 2D Depiction chapter contains examples that illustrate how the OEDepict TK and Grapheme TK can be utilized to depict molecules and visualize properties calculated with other OpenEye toolkits.
- Visualizing 3D Information chapter contains examples that illustrate how the Grapheme TK can be utilized to project complex 3D information into the 2D molecular graph.
- Cheminformatics chapter contains examples that solve various cheminformatics problems such as similarity search, ring perception and manipulating molecular graphs.

#### **OpenEye Python Cookbook examples using MolProp TK**

- Depicting Atom Contributions of XLogP
- Depicting Fragment Contributions of XLogP
- Depicting Topological Polar Surface Area
- Depicting Molecular Properties

## **CHAPTER**

# **THREE**

**API** 

# **3.1 OEMolProp Classes**

## 3.1.1 OEFilter

#### class OEFilter

This class represents a set of filters as initialized from a *filter file*. The primary use of this class is  $DEFitler$ .  $operator$  () method which will return whether the molecule passes or fails the filter.

#### **Constructors**

OEFilter (unsigned int type=OEFilterType::Default)

The OEFilter object is usually constructed from an unsigned integer from the OEFilterType constant namespace. The default constructor will initialize the object to the OEFilterType\_Default filter. The default filter is an alias for the OEFilterType\_BlockBuster filter.

#### See also:

The Variations of Filters section.

OEFilter (OEPlatform:: oeistream &filterstr)

Fine grained filter control is provided by allowing a custom filter file to be passed to the OEFilter object as the filterstr argument.

OEFilter (const OEFilter & filter)

The OEFilter object can be copy constructed from another OEFilter object.

#### operator()

call (OEMolBase mol)  $->$ bool

Returns whether the molecule mol passes the OEFilter object's set of filter rules. This function has been optimized by applying the filter rules in order of how expensive they are to calculate. For example, molecular weight is much easier to calculate than any of the functional group rules.

However, if an output stream has been specified using the OEFilter. Set Table method all the filter rules will be checked. This is the only way to ensure that all the fields are filled in the tabular data output to the stream specified in Set Table method.

Note: The molecule may be altered by the steps described in the Filter Preprocessing chapter.

#### See also:

This method will write logging data to OEThrow as described in this example.

#### operator bool

 $IsValid() \rightarrow bool$ 

Returns whether the OEFilter object is in a valid state ready to accept molecules to its OEFilter. operator () method.

**Note:** It is nearly impossible for an end user to create an invalid filter. This method is here for future API design to allow for greater programmatic control of the OEFilter object.

### **AddNormalizationRule**

**bool** AddNormalizationRule (const OEChem:: OEUniMolecularRxn &rxn)

Add a OEUniMolecularRxn to apply to the molecule. Special note should be taken about what preprocessing has already occurred on the molecule before generic normalizations are applied as described by the Filter Preprocessing chapter.

#### See also:

The *OEChem* manual has a chapter devoted to reactions.

#### **ClearNormalizationRules**

```
void ClearNormalizationRules()
```

Remove all normalizations previously added with OEFilter. AddNormalizationRule.

## **GetCanonOrder**

**bool** GetCanonOrder() const

Returns whether to canonicalize the atom and bond order after salt removal but before the molecule is altered into a neutral pH model.

#### See also:

```
OEFilter.SetCanonOrder
```

### **GetFilterType**

```
unsigned int GetFilterType() const
```

Return the unsigned integer constant from the OEFilterType namespace corresponding to the type of filter used to construct this object.

#### **GetFlagTableFailures**

```
bool GetFlagTableFailures() const
```

Return whether values in tabular data output are flagged with an asterisk marking them as outside the valid range for that filter rule. This is useful for figuring out why particular molecules have failed a given filter.

#### See also:

- Molecular Property Table
- · OEFilter. SetFlagTableFailures

#### **GetMessage**

```
std::string GetMessage(OEChem::OEMolBase &);
std::string GetMessage(OEChem::OEMCMolBase &);
```

Return a message that is "Pass" if the molecule passes the filter, and a reason for failure if it does not.

#### **GetMMFFTypeCheck**

bool GetMMFFTypeCheck () const

Return whether molecules sent to OEFilter. operator () will be MMFF atom type checked before any other filtering criteria are applied. The default is false.

- MMFF94 Atom Type Checking
- · OEFilter. SetMMFFTypeCheck

#### **GetSDTag**

```
bool GetSDTag() const
```

Return whether to attach every molecular property checked by the filter as SD data to the molecule passed to the OEFilter. operator () method. By default the the OEFilter object will not attach SD data.

#### See also:

```
OEFilter. SetSDTag
```

## **GetTable**

```
OEPlatform::oeostream *GetTable() const
```

Return the oeostream object that tabular data is sent to. Will return a zero-pointer, the default, if no output stream has been specified.

#### See also:

- Molecular Property Table
- · OEFilter. SetTable

## **GetTypeCheck**

```
bool GetTypeCheck() const
```

Return whether molecules sent to  $DEFiIter. operator()$  will be type checked before any other filtering criteria are applied. The default is false.

#### See also:

- Type Checking
- · OEFilter. SetTypeCheck

### **GetpKaNormalize**

```
bool GetpKaNormalize() const
```

Return whether the pKa state of molecules sent to  $DEFitter.\operatorname{operator}(t)$  will be normalized to a neutral pH. The default is false.

- · pKa Normalization
- · OEFilter. SetpKaNormalize

## **ParseNewRules**

**bool** ParseNewRules (OEPlatform:: oeistream &rulefile)

Parse the data from the rulefile oeistream as a NEWRULE file. These rules will override any rules specified by the filter file given to the OEFilter constructors.

#### See also:

**New Rules** 

### **PrintConfig**

```
void PrintConfig (OEPlatform::oeostream &log)
```

Print a human readable configuration of the object to the oeostream log.

#### **SetCanonOrder**

void SetCanonOrder (bool b)

Specify whether the molecule atom and bond order should be canonicalized after salt removal but before the molecule is altered into a neutral pH model.

#### See also:

```
OEFilter.GetCanonOrder
```

### **SetErrorLevel**

void SetErrorLevel (unsigned int level)

Sets the verbosity of warnings, using a level in the OEErrorLevel namespace, that are output when calling the operator OEFilter. operator () or the function GetMessage on the filter object.

#### **SetFlagTableFailures**

```
void SetFlagTableFailures (bool b)
```

Specify whether tabular output data should be marked with an asterisk if that value exceeds the limits specified by the filter.

- Molecular Property Table
- · OEFilter.GetFlagTableFailures

#### **SetMMFFTypeCheck**

```
void SetMMFFTypeCheck (bool b)
```

Specify whether molecules sent to  $DEFiIter$ . operator () will be MMFF atom type checked before any other filtering criteria are applied.

See also:

- MMFF94 Atom Type Checking
- Atom Type Checks subsection describing filter files
- · OEFilter.GetMMFFTypeCheck

### **SetSDTag**

void SetSDTag(bool b)

Specify whether to attach every molecular property checked by the filter as SD data to the molecule passed to the OEFilter.operator() method.

**Warning:** Only the properties up to the failing property will be attached by default. Use OEFilter. Set Table to force every property to be attached as SD data. The same rule applies to SD data as tabular output data, only the properties specified in the *filter file* will be attached as SD data.

#### See also:

- Attach Molecular Properties as SD Data
- OEFilter. GetSDTag

#### **SetTable**

void SetTable (OEPlatform:: oeostream \*table, bool owned)

Specify the oeostream object that tabular data is sent to. The owned parameter specifies whether the OEFilter object should take ownership of the table pointer. If owned is true the OEFilter destructor will delete the table pointer, otherwise, it is the user's responsibility.

Specifying a zero-pointer will effectively turn off tabular output data.

Note: The owned parameter must always be false for extension languages.

- Molecular Property Table
- · OEFilter. GetTable

### **SetTypeCheck**

```
void SetTypeCheck (bool b)
```

Specify whether molecules sent to  $DEFiIter. operator()$  will be type checked before any other filtering criteria are applied.

See also:

- Type Checking
- Atom Type Checks subsection describing filter files
- · OEFilter.GetTypeCheck

#### **SetpKaNormalize**

void SetpKaNormalize (bool b)

Specify whether the pKa state of molecules sent to  $DEFiIter. operator()$  will be normalized to a neutral pH.

#### See also:

- pKa Normalization
- · OEFilter.GetpKaNormalize

# 3.1.2 OEXLogPResult

class OEXLogPResult

Used by OEGetXLogPResult function to return the computed XLogP and result status.

#### **Constructors**

OEXLogPResult (bool valid, float value)

Constructor. Since this class is mainly used to return values and status from the OEGEtXLogPResult function, this is generally not used.

#### IsValid()

```
bool IsValid() const
```

Returns whether the computed value is valid for the molecule. The main reason that the computation fails is that the molecule has one or more atoms that are not parameterized.

### **GetValue**

```
float GetType () const
```

Returns the computed XLogP value.

# **3.2 OEMolProp Constants**

# 3.2.1 OEFilterType

This namespace contains built-in filters that can be passed to the OEFilter constructor.

Warning: Go look at the Filter Files before using any of the following default filters.

#### See also:

Variations of Filters

## **BlockBuster**

This is the recommended default filter. We encourage you to use it unless you are familiar with filtering or not satisfied with your initial results.

#### See also:

The development of this filter is described in the Variations of Filters section.

## **Default**

An alias for the current default value of OEFilterType\_BlockBuster.

### **Drug**

Corresponds to the [Oprea-2000] drug-like filters useful for later stage drug development. This is provided as a backwards compatible option. Experience has shown it to be too restrictive, the  $OEFilterType\_BlockButer$ filter is recommended.

## **Fragment**

Filter for extracting small molecules from a database.

#### Lead

Corresponds to the [Oprea-2000] lead-like filters useful for preparing HTS databases.

#### **PAINS**

Corresponds to the [Baell-2010] filter useful for removing common substructures that interfere with bioassays.

#### See also:

PAINS section

#### **BlockBusterPAINS**

Combines the filtering criteria of BlockBuster and PAINS.

### **Max**

Current maximum number of provided built-in filter types.

## 3.2.2 OEFilterParamName

This namespace contains the default parameter names used when the interface generated by invoking the OEConfigureFilterParamsfunction.

#### See also:

· OEFilterParamSetup namespace.

The OEFilterParamName namespace contains the following constant:

#### **Type**

The default name of filter type parameter is "-filtertype".

- · OEFilterParamSetup\_Type constant
- · OEConfigureFilterType function
- OEGetFilterType function

# 3.2.3 OEFilterParamSetup

This namespace encodes symbolic constants used as bit-masks to indicate which filter interface parameters are being created when invoking the OEConfigureFilterParams function.

#### See also:

· OEFilterParamName namespace

The OEFilterParamSetup namespace contains the following constants:

## All

The combination of following constant:

· OEFilterParamSetup\_Type

## **Type**

Passing this constant to the OEConfigureFilterParams function result in generating the following default interface to configure the filter type by invoking the  $OEConfigureFilterType$  function.

```
Contents of parameter -filtertype
   Aliases : -ftype
   Type : string
   Allow list : false
   Default : BlockBuster
   Simple : true
   Required : false
   Legal values : Lead Drug BlockBuster Fragment PAINS Custom Max
   Brief : filter type
```

#### See also:

- OEFilterParamName\_Type constant
- · OEConfigureFilterType function
- · OEGetFilterType function

# **3.3 OEMolProp Functions**

# 3.3.1 OECheckXLogXType

OECheckXLogXType(OEAtomBase atom) -> bool

Returns true if a given atom or has a valid XLogP type as referenced in the LogP section, or if the atom is a hydrogen.

### See also:

OEGetXLogP function OECheckXLogXTypes function LogP section

## 3.3.2 OECheckXLogXTypes

OECheckXLogXTypes(OEMolBase mol)  $\rightarrow$  bool

Returns true if each atom excluding hydrogens in the given molecule has a valid XLogP type as referenced in the  $LogP$ section. Invalid types for hydrogens are ignored.

See also:

OEGetXLogP function OECheckXLogXType function LogP section

## 3.3.3 OEConfigureFilterParams

```
bool OEConfigureFilterParams (OESystem:: OEInterface& itf,
                             unsigned int config = DEFilterParamSetup::All)
```

Configures the given interface to add filter parameters.

*itf* The interface being configured.

config The option that specifies which parameters will be added to the interface. This value has to be from the OEFilterParamSetup namespace.

#### See also:

- OEInterface class in the OEChem TK manual
- · OEFilterParamSetup namespace
- OEGetFilterType function

## 3.3.4 OEConfigureFilterType

```
bool OEConfigureFilterType (OESystem:: OEInterface& itf,
                         std::string name = OEFilterParamName::Type,
                         std::string alias = "-ftype")
```

Configures the given interface to add filter type parameter.

*itf* The interface being configured.

name The name of the filter type parameter.

*alias* The alternative *i.e.* alias name of the parameter.

- OEInterface class in the **OEChem TK** manual
- · OEGetFilterType function
- · OEFilterParamSetup namespace
- · OEFilterParamName namespace
- OEFilterType namespace

# 3.3.5 OEGet2dPSA

OEGet2dPSA (OEMolBase mol, OEFloatArray atomPSA=None, bool SandP=False) float  $->\,$ 

Returns the topological polar surface area for a given molecule as described in the *Polar Surface Area* section. The SandP parameter controls whether sulfur and phosphorus should be counted towards the total surface area. See example in Figure: Example of depicting the atom contributions of the polar surface area.

Warning: TPSA values are mildly sensitive to the protonation state of a molecule.

The atomPSA parameter can be used to retrieve the contribution of each atom to the total polar surface area as shown in Listing 1.

Listing 1: Example of retrieving individual atom contributions to PSA

```
atomPSA = oechem. OEFloatArray(mol. GetMaxAtomIdx())psa = oemolprop.OEGet2dPSA(mol, atomPSA)
print ("PSA =", psa)
for atom in mol. GetAtoms () :
    idx = atom.GetIdx()print(idx, atomPSA[idx])
```

-- Polar Surface Area =  $150.16$  -- Polar Surface Area =  $83.12$ 

![](_page_117_Figure_9.jpeg)

Fig. 1: Example of depicting the atom contributions of the polar surface area (ignoring S and P atoms) (Darker colors and longer spikes indicate larger PSA atom contributions)

#### See also:

The Python script that visualizes the polar surface area of a molecule can be downloaded from the OpenEye Python Cookbook

![](_page_118_Figure_1.jpeg)

Fig. 2: Example of depicting the atom contributions of the polar surface area (considering S and P atoms) (Darker colors and longer spikes indicate larger PSA atom contributions)

#### See also:

Polar Surface Area section

## 3.3.6 OEGetAnionicCarbonCount

unsigned int OEGetAnionicCarbonCount (const OEChem:: OEMolBase &mol)

Returns the number of anionic carbons in a molecule. Anionic carbon is defined as an aromatic carbon that has negative 'formal charge'.

#### See also:

- Anionic Carbon Count subsection describing filter files
- OEAtomBase. IsAromatic and OEAtomBase. GetFormalCharge methods in the OEChem TK manual

## 3.3.7 OEGetAromaticRingCount

unsigned OEGetAromaticRingCount (const OEChem:: OEMolBase &mol)

Returns the number of aromatic rings in a molecule as defined in [Ritchie-2009]. The article describes the method as the following:

```
The terminology 'number of aromatic rings' (or aromatic ring
count) is used generically and encompasses both benzenoid
aromatic rings and heteroaromatics (including, e.g. pyridine and
imidazole). ... Each ring in a fused system is counted
```

```
individually; thus, indole and naphthalene are each defined as
having two aromatic rings.
```

# 3.3.8 OEGetFilterType

```
unsigned int OEGetFilterType (const OESystem:: OEInterface& itf,
                                 std::string name = OEFilterParamName::Type)
```

Returns the filter type initialized in the given interface. The return value is taken from the OEFilterType namespace.

*itf* The interface in which the parameter is configured.

name The name of the parameter.

#### See also:

- · OEConfigureFilterParams function
- · OEConfigureFilterType function
- · OEFilterType namespace

# 3.3.9 OEGetFractionCsp3

float OEGetFractionCsp3(const OEChem:: OEMolBase &mol)

Returns the number of  $sp^3$  carbons divided by the total number of carbons as described in [Lovering-2009].

# 3.3.10 OEGetHalideFraction

double OEGetHalideFraction (const OEChem:: OEMolBase &mol, bool isotopic = false)

Returns the percent of molecular weight from halides.

*isotopic* This parameter determines whether the isotopic information is taken into account when calculating the molecule weight.

- . OECalculateMolecularWeight function in the OEChem TK manual
- Halide Fraction subsection describing filter files

# 3.3.11 OEGetHBondAcceptorCount

```
unsigned int OEGetHBondAcceptorCount (const OEChem:: OEMolBase & mol)
```

Returns the number of hydrogen-bond acceptors in a molecule based on the definition in the work of Mills and Dean ([Mills-Dean-1996]) and also in the book by Jeffrey (JJeffrey-1997]). It is defined to be the number of atoms which match any of the following:

• degree 2, aromatic, non-positive nitrogens. An example is shown below.

![](_page_120_Figure_5.jpeg)

• electron rich or negative, valence less than 4, non-aromatic nitrogens. An example is shown below.

![](_page_120_Figure_7.jpeg)

• negatively charged or not electron withdrawn, neutral, non-aromatic oxygens. An example is shown below.

![](_page_120_Figure_9.jpeg)

• degree 1, double bonded, electron rich, non-aromatic sulfur. An example is shown below.

- · OEGetHBondDonorCount function
- · OEGetLipinskiAcceptorCount function
- · Lipinski and Hydrogen-bonds section
- Hydrogen-bond Acceptors subsection describing filter files

![](_page_121_Figure_1.jpeg)

### **Example**

The OEGetHBondAcceptorCount function returns 3 for the molecule below.

![](_page_121_Figure_4.jpeg)

# 3.3.12 OEGetHBondDonorCount

unsigned int OEGetHBondDonorCount (const OEChem:: OEMolBase &mol)

Returns the number of hydrogen-bond donors in a molecule based on the definition in the work of Mills and Dean ([Mills-Dean-1996]) and also in the book by Jeffrey ([Jeffrey-1997]). It is defined to be the number of hydrogen atoms on nitrogen, oxygen, or sulfur atoms.

### See also:

- · OEGetHBondAcceptorCount function
- · OEGetLipinskiDonorCount function
- · Lipinski and Hydrogen-bonds section
- Hydrogen-bond Donors subsection describing filter files

#### **Example**

The OEGetHBondDonorCount function returns 2 for the molecule below.

![](_page_122_Figure_1.jpeg)

# 3.3.13 OEGetLipinskiAcceptorCount

unsigned int OEGetLipinskiAcceptorCount (const OEChem:: OEMolBase &mol)

Returns the number of acceptors in a molecule based on the definition from the work of Lipinski ([Lipinski-1997]). It is defined to be the number of nitrogens or oxygens.

#### See also:

- · OEGetLipinskiDonorCount function
- · OEGetHBondAcceptorCount function
- · Lipinski and Hydrogen-bonds section
- Lipinski Acceptors subsection describing filter files

#### **Example**

The OEGetLipinskiAcceptorCount function returns 5 for the molecule below.

![](_page_122_Figure_12.jpeg)

## 3.3.14 OEGetLipinskiDonorCount

unsigned int OEGetLipinskiDonorCount (const OEChem:: OEMolBase &mol)

Returns the number of donors in a molecule based on the definition from the work of Lipinski ([Lipinski-1997]). It is defined to be the number of nitrogens and oxygens with at least one hydrogen attached.

#### See also:

- · OEGetLipinskiAcceptorCount function
- OEGetHBondDonorCount function
- Lipinski and Hydrogen-bonds section
- Lipinski Donors subsection describing filter files

#### **Example**

The OEGetLipinskiDonorCount function returns 2 for the molecule below.

![](_page_123_Figure_11.jpeg)

# 3.3.15 OEGetLongestUnbranchedHeavyAtomsChain

unsigned int OEGetLongestUnbranchedHeavyAtomsChain (const OEChem:: OEMolBase &mol)

Returns the size of the longest chain of heavy atoms in a molecule. This is defined to be the maximum number of connected, unbranched, and non-ring heavy atoms. An unbranched atom is a chain atom with maximum two connections to other heavy chain atoms. A set of unbranched atoms which are connected together form a chain. A molecule may contain multiple chains which are isolated from each other by non-chain atoms (e.g. ring or branched atoms).

#### See also:

- · OEGetLongestUnbranchedCarbonsChain function
- Unbranched Chains subsection describing filter files

#### **Examples**

The OEGetLongestUnbranchedHeavyAtomsChain function returns 4 for the molecule below.

The OEGetLongestUnbranchedHeavyAtomsChain function returns 4 for the molecule below.

![](_page_124_Figure_1.jpeg)

Generated by Grapheme TK

# 3.3.16 OEGetLongestUnbranchedCarbonsChain

unsigned int OEGetLongestUnbranchedCarbonsChain (const OEChem::OEMolBase &mol)

Returns the size of the longest chain of all carbons in a molecule. An unbranched atom is a chain atom with maximum two connections to other heavy chain atoms. A set of unbranched atoms which are connected together form a chain. A molecule may contain multiple chains which are isolated from each other by non-chain atoms (e.g. ring or branched atoms).

#### See also:

- · OEGetLongestUnbranchedHeavyAtomsChain function
- Unbranched Chains subsection describing filter files

#### **Examples**

The OEGetLongestUnbranchedCarbonsChain function returns 4 for the molecule below.

![](_page_124_Figure_11.jpeg)

Generated by Grapheme TK

The OEGetLongestUnbranchedCarbonsChain function returns 0 for the molecule below. It is because the unbranched chain does not contain all carbons.

![](_page_125_Figure_2.jpeg)

# 3.3.17 OEGetNumUnspecifiedAtomStereos

unsigned int OEGetNumUnspecifiedAtomStereos (OEChem:: OEMolBase &mol)

Returns the number of unspecified stereo atoms in a molecule. The OEPerceiveChiral function will be called to perceive chiral atoms in the molecule.

#### See also:

- Unspecified Atom Stereo subsection describing filter files
- Stereochemistry Perception chapter in the OEChem TK manual
- . OEAtomBase.HasStereoSpecified method in the OEChem TK manual
- · OEGetNumUnspecifiedBondStereosfunction

## 3.3.18 OEGetNumUnspecifiedBondStereos

unsigned int OEGetNumUnspecifiedBondStereos (OEChem:: OEMolBase &mol)

Returns the number of unspecified stereo bonds in a molecule. The OEPerceiveChiral function will be called to perceive chiral bonds in the molecule.

- Unspecified Bond Stereo subsection describing filter files
- Stereochemistry Perception chapter in the OEChem TK manual
- . OEBondBase. HasStereoSpecified method in the OEChem TK manual
- · OEGetNumUnspecifiedAtomStereosfunction

# 3.3.19 OEGetRotatableBondCount

unsigned int OEGetRotatableBondCount (const OEChem:: OEMolBase &mol, bool adjust = ...  $\leftrightarrow$ false)

Returns the number of rotatable bond counts in a molecule. Rotatable bond is defined as any single non-ring bond, bounded to nonterminal heavy (i.e., non-hydrogen) atom. In addition, It considers the carbon-carbon triple bond in acetylene rotatable. The function excludes single bonds observed in a certain groups, such as sulfonamides, esters, and amidine.

**adjust** This parameter allows optional adjustment for aliphatic rings following the method of [Oprea-2000]. In this case, it also estimates the number of flexible bonds in aliphatics rings.

Note: The Oprea's method is individual ring based. Since Smallest set of smallest rings perception is not available in **OEChem TK** (see section Smallest Set of Smallest Rings (SSSR) Considered Harmful for more details), we modified Oprea's method to be ring system based (Ring Systems Identification), and implemented the function relatively closed to Oprea's definition. The function works for various complex fused ring-systems and simple bridge ring-systems.

### **Examples**

The number of rotatable bonds calculated for the molecule below is 0. When considering the flexibility of the aliphatic ring (setting the adjust parameter to true), the OEGetRotatableBondCount function returns 3, based on Oprea's method that considers the amide bonds as non-rotatable.

![](_page_126_Figure_8.jpeg)

Fig. 3: Example of aliphatic ring

The number of rotatable bonds calculated for the molecule below is 7. When considering the flexibility of the aliphatic ring (setting the adjust parameter to true), the OEGetRotatableBondCount function returns 11, adjusting the rotatable bond count by 2 from each of the two aliphatic rings.

#### See also:

• Rotor Count subsection describing filter files

![](_page_127_Picture_1.jpeg)

Fig. 4: Example of rotatable bond count adjustment for aliphatic rings

- rotatable bond definition in **OEChem TK**
- OEIsRotor functor in OEChem TK
- Smallest Set of Smallest Rings (SSSR) Considered Harmful and Ring Systems Identification sections in **OEChem TK**

## 3.3.20 OEGetXLogP

OEGetXLogP(OEMolBase mol, OEFloatArray atomxlogps=None) -> float xlogp

Returns the XLogP for a given molecule as described in the  $LogP$  section. The returned value will be equal to the sum on the individual atom contributions plus the linear regression constant  $-0.127$ .

Note: The C++ version of this function uses a pointer-to-argument to indicate the success or failure of the computation. This idiom doesn't map directly to the wrapped languages, so the wrapped versions of  $OEGetXLoop$  use exceptions to signal failure. This is not optimal. Hence, for the wrapped languages, the **preferred method for com**puting XLogP is OEGetXLogPResult. It does not use exceptions and is much cleaner to use in the wrapped languages.

Hint: XLogP should be calculated on the neutral form of the molecule. Therefore, calling the OERemoveFormalCharge function of Quacpac TK is highly recommended prior to the XLogP calculation.

#### See also:

OEGetXLogPResult function LogP section

## 3.3.21 OEGetXLogPResult

OEGetXLogPResult (OEMolBase mol, OEFloatArray atomxlogps=None) -> OEXLogPResult

Returns an OEXLogPResult object. The object contains the XLogP for the given molecule as described in the  $LogP$ section and a boolean flag indicating whether or not the computation is valid. The main reason the computation may fail is if one or more atoms are not parameterized. The returned value will be equal to the sum on the individual atom contributions plus the linear regression constant  $-0.127$ .

Hint: XLogP should be calculated on the neutral form of the molecule. Therefore, calling the OERemoveFormalCharge function of Quacpac TK is highly recommended prior to the XLogP calculation.

The atomxlogps parameter can be used to retrieve the contribution of each atom to the total XLogP as shown in Listing 2. See example in Figure: Example of depicting the atom contributions of the  $XLogP$ .

This function exists to make the calling by wrapped languages more convenient. This function should be **preferred** over the original OEGetXLogP function for wrapped languages.

#### Listing 2: Example of retrieving individual atom contributions to XLogP

```
atomXLogP = occhem.OEFloatArray(mol.GetMaxAtomIdx())result = oemolprop.OEGetXLoqPResult(mol, atomXLoqP)
if (result. IsValid()):
   print("XLogP =", result.GetValue())for atom in mol. GetAtoms ():
       idx = atom.FetIdx()print(idx, atomXLogP[idx])
else:
    print ("XLogP failed for molecule")
```

#### See also:

OEXLogPResult class LogP section

#### **Code Example**

- Depicting Atom Contributions of XLogP OpenEye Python Cookbook recipe
- Depicting Fragment Contributions of XLogP OpenEye Python Cookbook recipe

## 3.3.22 OEGetXLogPVersion

std::string OEGetXLogPVersion()

Returns the version number for the current XLogP computation as a string.

![](_page_129_Figure_1.jpeg)

Fig. 5: Example of depicting the atom contributions of the XLogP

# 3.3.23 OEMolPropGetArch

```
const char *OEMolPropGetArch()
```

# 3.3.24 OEMolPropGetLicensee

```
bool OEMolPropGetLicensee(std::string &licensee)
```

# 3.3.25 OEMolPropGetPlatform

```
const char *OEMolPropGetPlatform()
```

# 3.3.26 OEMolPropGetRelease

const char \*OEMolPropGetRelease()

# 3.3.27 OEMolPropGetSite

```
bool OEMolPropGetSite(std::string &site)
```

# 3.3.28 OEMolPropGetVersion

unsigned int OEMolPropGetVersion()

# 3.3.29 OEMolPropIsLicensed

bool OEMolPropIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any MolProp TK functionality.

The 'feature' argument can be used to check for a valid license to **MolProp TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current MolProp TK license.

### See also:

• OEChemIsLicensed function

# 3.3.30 OEWritePropertyDataToCSV

```
bool OEWritePropertyDataToCSV(const std::string &fname, OEChem::oemolistream &ifs,
→OEMolProp::OEFilter &filter)
bool OEWritePropertyDataToCSV (OEChem::oemolostream &ofs, OEChem::oemolistream &ifs,
\rightarrowOEMolProp::OEFilter &filter);
```

Write the molecular properties calculated by OEFilter to the output file frame or to the stream of s in the OEFormat\_CSV format. Returns true if the output CSV file was successfully written, false otherwise.

Molecules are read in from the input stream ifs. The output CSV file can be read by the OEReadCSVFile function.

#### See also:

• CSV File Format section

#### **Code Example**

• Write molecular properties to a CSV file example

## **CHAPTER**

# **FOUR**

# **RELEASE HISTORY**

# 4.1 MolProp TK 2.6.5

Minor internal improvements have been made.

# 4.2 MolProp TK 2.6.4

Minor internal improvements have been made.

# 4.3 MolProp TK 2.6.3

Minor internal improvements have been made.

# 4.4 MolProp TK 2.6.2

Minor internal improvements have been made.

# 4.5 MolProp TK 2.6.1

## 4.5.1 New features

- A new free function, OECheckXLogXType, that returns true if an atom has a valid XLogPType has been added.
- A new free function, *OECheckXLogXTypes*, that returns  $\tau$  rue if all atoms excluding hydrogen in a molecule have valid XLogP types has been added.

## 4.5.2 Minor bug fixes

• An issue with filter output failure reporting, where failure due to the rules ALLOWED\_ELEMENTS and ELIMI-NATE\_METALS was not included in the output table, has been fixed.

# 4.6 MolProp TK 2.6.0

## 4.6.1 New features

• The ability to filter based on aromatic ring count and fraction of CSP3 carbons has been added.

# 4.7 MolProp TK 2.5.7

Fall 2021

## **4.7.1 New Features**

- A method, GetMessage, was added to the OEFilter class to be able to retrieve information on whether the filter passed a molecule, or why it failed a specific molecule.
- A method, SetErrorLevel, was added to the OEFilter class to add explicit control of warnings output by the filter class and the filter application.
- A BlockBusterPAINS filter was added in the OEFilterType namespace, which combines filtering criteria for the BlockBuster and PAINS filters.
- Excess warning output that was causing large log files is now suppressed by default, and can be switched on using the new SetErrorLevel method. See OEFilterType.

# **4.8 MolProp TK 2.5.6**

July 2021

## 4.8.1 Minor bug fixes

• An issue with *OEGetRotatableBondCount* counting carbamates and ureas as rotatable has been fixed.

# 4.9 MolProp TK 2.5.5

Fall 2020

• Minor internal improvements have been made.

# 4.10 MolProp TK 2.5.4

• Minor internal improvements have been made.

# 4.11 MolProp TK 2.5.3

## 4.11.1 New features

- Two new functions, OEGetHBondDonorCount and OEGetHBondAcceptorCount, have been added that count the number of hydrogen-bond donors and acceptors in a molecule.
- . Two new functions, OEGetLipinskiDonorCount and OEGetLipinskiAcceptorCount, have been added that determine the number of donors and acceptors in a molecule based on the definition from the work of Lipinski ([Lipinski-1997]).
- A new function, OEGetLongestUnbranchedHeavyAtomsChain, has been added that determines the size of the longest chain of heavy atoms in a molecule.
- A new function, OEGet Longest UnbranchedCarbonsChain, has been added that determines the size of the longest chain of all carbons in a molecule.
- A new function, OEGetHalideFraction, has been added that determines the percentage of molecular weight from halides.
- A new function,  $OEGetAnionicCarbonCount$ , has been added that determines the number of anionic carbons in a molecule. New filter options, MIN\_ANION\_C and MAX\_ANION\_C, have also been added that filter out anionic carbons.
- A new function,  $OEWritePropertyDataToCSV$ , has been added that writes molecular properties to the output in the OEFormat CSV format.
- . Two new functions, OEGetNumUnspecifiedAtomStereos and OEGetNumUnspecifiedBondStereos, have been added that filter out molecules with unspecified atom and bond stereos. New fil-MIN\_UNSPECIFIED\_ATOM\_STEREOS, MAX\_UNSPECIFIED\_ATOM\_STEREOS, ter options, MIN UNSPECIFIED BOND STEREOS, and MAX UNSPECIFIED BOND STEREOS, have also been added.

# 4.11.2 Minor bug fixes

• The XLogP calculation by the  $OEGetXLogPResult$  function for molecules with explicit hydrogens has been fixed.

# **4.11.3 Documentation changes**

• A new program, Write molecular properties to a CSV file, has been added that demonstrates writing molecular properties to an output file in the OEFormat\_CSV format.

# 4.12 MolProp TK 2.5.2

# 4.12.1 New features

- A new OEGetRotatableBondCount function has been added that can calculate either the number of rotatable bonds in the molecule or the molecule flexibility, taking into consideration the flexibility of aliphatic rings.
- New OEConfigureFilterParams and OEConfigureFilterType functions have been added to configure the given interface.
- A new  $OEGetFilterType$  function has been added to retrieve the filter type initialized in the given interface.
- New OEFilterParamSetup, OEFilterParamName, and OEFilterType namespaces have been added to provide options for the choice of filter interface parameters, filter parameter names, and filter types, respectively.

# **4.12.2 Documentation changes**

- The following five example programs have been updated to allow switching filter types through the command line option:
  - Basic Filtering for a Molecule File
  - Quiet Filtering
  - Molecular Property Table
  - Specific Molecular Properties
  - Attach Molecular Properties as SD Data

# 4.13 MolProp TK 2.5.1

• Minor internal improvements have been made.

# 4.14 MolProp TK 2.5.0

# 4.14.1 Bug fixes

• The aminal and hemiaminal SMARTS rules have been modified to be slightly more general. Both rules now match 1,1-diamines as well as hydroxyl amines.

# 4.15 MolProp TK 2.4.7

# 4.15.1 Minor bug fixes

• The pains\_pre\_aminal1 rule has been removed from the PAINS filter. The SMARTS for the rule was incorrectly defined and was overly general. The rules pains basic amine1, pains basic amine2, and pains\_basic\_amine3 cover the same general structural classes in a more precise manner. A SMARTS issue with the pains\_basic\_amine3, uncovered after removing the pains\_pre\_aminal1 rule, has also been corrected.

# 4.16 MolProp TK 2.4.6

• Minor internal improvements have been made.

# 4.17 MolProp TK 2.4.5

• Minor internal improvements have been made.

# 4.18 MolProp TK 2.4.4

# 4.18.1 Minor bug fixes

• The definition for the SMARTS for the CBoring (straight-chain alkane) fragment in the filter fragment set has been changed from [CR0H2] [CH2] [CH2] [CH2, H3] to [CR0H2] [CH2] [CH2] [CH2, CH3]. Previously, it could erroneously match a heteroatom at the last position.

# **4.18.2 Documentation changes**

• Minor corrections to the bibliography have been made.

# 4.19 MolProp TK 2.4.3

# 4.19.1 Major bug fixes

- An issue that affected XLogP values depending on the aromaticity model perception has been repaired.  $OEGetXLogP$  function now re-perceives the **OpenEye** aromaticity model when necessary before calculating XLogP values.
- A filter with a non-zero MIN\_UNBRANCHED\_C had previously failed and now is properly calculated.

# 4.20 MolProp TK 2.4.2

• Minor internal improvements have been made.

# 4.21 MolProp TK 2.4.1

## 4.21.1 New features

• A new built-in filter for MMFF atom types has been added that can identify and eliminate molecules that have one or more unknown MMFF atom type assignments. The MMFFTYPECHECK directive in rule files controls the behavior. The OEFilter. SetMMFFTypeCheck and OEFilter. GetMMFFTypeCheck methods control the behavior when using an OEFilter object.

# 4.21.2 Major bug fixes

• OEFilter. operator () now handles multi-conformer molecules.

## 4.21.3 Minor bug fixes

• The pattern for beta\_carbonyl\_quat\_nitrogen had previously incorrectly matched tertiary amines as well as quaternary amines. This has been fixed.

# 4.22 MolProp TK 2.4.0

## 4.22.1 New features

• OEFilterType\_PAINS is a new filter for removing substructures that commonly cause problems in bioassays. The SMARTS patterns used in this filter have been adapted from the SLN patterns in the original paper:

Baell, J.B. and Holloway G.A.,

New Substructure Filters for Removal of Pan Assay Interference Compounds (PAINS) from Screening Libraries and for Their Exclusion in Bioassays, Journal of Medicinal Chemistry, Vol 53, pp. 2719-2740, 2010

#### See also:

The PAINS section.

# 4.22.2 Bug fixes

- The displayed precision of the numerical values output in log messages are more realistic and now match the table output precision.
- OEFilter. operator () method now skips the calculation of certain physical properties if the filter being used does not require them and a table is not being generated. This quiets erroneous warnings for molecules that could be generated by those property calculations.

# 4.23 MolProp TK 2.3.0

## 4.23.1 New features

• A new OEFilter. GetFilterType method has been added for retrieving the filter used to construct the OEFilter object.

# **4.23.2 Documentation fixes**

- The *Functional Group Rules* section has been updated with much better **OEDepict TK 2.x**-generated images of functional groups. The section should be significantly easier to read with the updated style.
- The example program Attach Molecular Properties as SD Data will now allow output to the .  $c$ sv file format.

# 4.24 MolProp TK 2.2.2

## 4.24.1 Minor bug fixes

• Typecheck functionality, OEFilter. Set TypeCheck, has been changed such that hexavalent sulfur (matching SMARTS [Sv6D6]) will now be an acceptable atom type.

## **4.24.2 Documentation fixes**

- The linear regression constant used by  $OEGetXLogP$  is now documented.
- PDF documentation should no longer throw warnings about "bad /BBox" in some PDF readers.

# 4.25 MolProp TK 2.2.1

## 4.25.1 New features

• OEGetXLogP is now thread safe.

# 4.25.2 Major bug fixes

- OEGetXLoqP will no longer return garbage data in the per atom data array whenever molecules with deleted atoms are passed to the function.
- OEFilter carboxylic acid pattern will now match formic acid, formic esters, and formic thioesters with implicit hydrogens. Previously, explicit hydrogens were required on the molecule.

# 4.25.3 Minor bug fixes

• Removed unbounded stack allocations.

# 4.26 MolProp TK 2.2.0

# 4.26.1 Minor bug fixes

• Based on new, more reliable pKa data, the "malonic" keyword was refined to identify malonic acid specifically ( $p$ Ka 2.9, 5.7) rather than generic di-carbonyl carbon acids, which typically have  $p$ Ka values in the 8.9-11.5 range. This improves the reliability of the "acid" pattern as well, which is dependent on the "malonic" keyword.

# 4.26.2 Documentation changes

• Lipinski H-Bond donor is now properly described in the documentation. The implementation was already correct.

# 4.27 MolProp TK 2.1.7

# 4.27.1 Major bug fixes

• "MIN\_\*" and "MAX\_\*" properties filter rules file no longer have to both be specified to work. Previously, if a property filter was specified with "MAX\_\*", then the corresponding "MIN\_\*" filter rule had to also be set for the rule to properly function. Now, "MIN\_\*" and "MAX\*" filter rules operate independent of the other.

# 4.28 MolProp TK 2.1.6

# 4.28.1 Bug fixes

• OEFilter. operator () will now call OEP repareSearch on the molecule to ensure the molecule has all the proper properties initialized for OEFilter SMARTS matches.

# 4.29 MolProp TK 2.1.5

• Minor internal improvements.

# 4.30 MolProp TK 2.1.4

• The OEFilter object will now canonicalize atom and bond order by default. This avoids the problem of the normalization and duplicate removal steps being dependent on input atom order.

# 4.31 MolProp TK 2.1.3

## 4.31.1 New features

- Adding pictures to describe  $OEGetXLogP$  and  $OEGet2dPSA$  in documentation.
- OEFilter through its dependence on Neutral pH model (OESetNeutralpHModel) has been refined to reflect feedback from collaborators. In particular isoxazoles and oxadiazoles were added while pyrazoles and aryl sulfonamides were refined. Aryl sulfonamide refinement also incorporated changes based on newly obtained experimental data.

# 4.31.2 Minor bug fixes

• Through its dependence on OESetNeutralpHModel OEFilter now correctly addresses beta di-amino groups so that if all other considerations are equivalent, secondary amines are treated as most basic, followed by primary amines, with tertiary amine being treated as least basic.

# 4.32 MolProp TK 2.1.2

• Minor documentation fixes.

# 4.33 MolProp TK 2.1.1

## 4.33.1 New features

- Added several halide that are more strict to the fragment filter.
- Added several rules to remove bad ring systems to the fragment filter.

**Note:** The proper way to override a RULE line is to use a NEWRULE line.

# 4.33.2 Minor bug fixes

• Removing duplicate nitroso and phosphoryl filter file RULES from the default filters.

# 4.34 MolProp TK 2.1.0

This is the first release of the OEMolProp toolkit. Its version number corresponds to version number of the Filter application.

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

## **CHAPTER**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

## **CHAPTER**

# **SEVEN**

# **CITATION**

# 7.1 Orion<sup>®</sup> Floes

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

# **7.2 Toolkits and Applications**

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

# **7.3 OpenEye Web Services**

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

# **EIGHT**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project       | Website                                                    | License  |
|-----------------------|------------------------------------------------------------|----------|
| abseil-cpp            | https://github.com/abseil/abseil-cpp                       | https:// |
| absl-py               | https://github.com/abseil/abseil-py                        | https:// |
| aiohttp               | https://docs.aiohttp.org/en/stable/                        | https:// |
| aiosignal             | https://github.com/aio-libs/aiosignal                      | https:// |
| Amazon Linux 2        | https://aws.amazon.com/amazon-linux-2                      | N/A      |
| AmberUtils            | http://ambermd.org                                         | N/A      |
| ambit                 | https://github.com/khimaros/ambit                          | https:// |
| amqp                  | https://github.com/celery/py-amqp                          | https:// |
| anaconda-anon-usage   | Orion Floes                                                | https:// |
| angular               | https://github.com/angular/angular.js                      | https:// |
| angular-animate       | https://github.com/angular/angular.js                      | https:// |
| angular-cache         | https://github.com/jmdobry/angular-cache                   | https:// |
| angular-cookies       | https://github.com/angular/angular.js                      | https:// |
| angular-loggly-logger | https://github.com/ajbrown/angular-loggly-logger           | https:// |
| angular-mocks         | https://github.com/angular/angular.js                      | https:// |
| angular-resource      | https://github.com/angular/angular.js                      | https:// |
| angular-toggle-switch | https://github.com/cgarvis/angular-toggle-switch           | https:// |
| angular-ui-grid       | https://github.com/angular-ui/ui-grid                      | https:// |
| angular-ui-router     | https://github.com/angular-ui/ui-router                    | https:// |
| angular-ui-tree       | https://github.com/angular-ui-tree/angular-ui-tree         | https:// |
| angular-vs-repeat     | https://github.com/kamilkp/angular-vs-repeat               | https:// |
| aniso8601             | https://bitbucket.org/nielsenb/aniso8601                   | https:// |
| annotated-types       | https://github.com/annotated-types/annotated-types         | https:// |
| anyio                 | https://github.com/agronholm/anyio                         | https:// |
| appdirs               | http://github.com/ActiveState/appdirs                      | http://  |
| appengine             | https://google.golang.org/appengine                        | https:// |
| arabic-reshaper       | https://github.com/mpcabd/python-arabic-reshaper/          | https:// |
| archspec              | https://github.com/archspec/archspec/blob/master/README.md | https:// |

| Name of Project               | Website                                                                             | License                                                            |
|-------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                | https:/                                                            |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                       | https:/                                                            |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                          | https:/                                                            |
| ascii85                       | https://github.com/huandu/node-ascii85                                              | https:/                                                            |
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
| atk-1.0                       | https://docs.gtk.org/atk/                                                           | https:/                                                            |
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
| blosc2                        | https://github.com/Blosc/python-blosc2                                              | https:/                                                            |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https:/                                                            |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                            |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                            |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                                            |
| boto3                         | https://github.com/boto/boto3                                                       | https:/                                                            |
| botocore                      | https://github.com/boto/botocore                                                    | https:/                                                            |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                                            |
| Brotli                        | https://github.com/google/brotli                                                    | https:/                                                            |
| brotli-bin                    | https://github.com/google/brotli                                                    | https:/                                                            |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                                            |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                          | https:/                                                            |
| bson                          | http://github.com/py-bson/bson                                                      | https:/                                                            |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https:/                                                            |
| bzip2                         | https://www.bzip.org                                                                | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| c-ares                        | https://github.com/c-ares/c-ares                                                    | https://                                                           |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            | https://                                                           |
| cached-property               | https://github.com/pydanny/cached-property                                          | https://                                                           |
| cachetools                    | https://github.com/tkem/cachetools                                                  | https://                                                           |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           | https://                                                           |
| canvas                        | https://github.com/Automattic/node-canvas                                           | https://                                                           |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              | https://                                                           |
| celery                        | https://github.com/celery/celery                                                    | https://                                                           |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         | https://                                                           |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                           | https://                                                           |
| cffi                          | https://github.com/python-cffi/cffi                                                 | https://                                                           |
| cftime                        | https://pypi.org/project/cftime/                                                    | https://                                                           |
| chardet                       | https://github.com/chardet/chardet                                                  | https://                                                           |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        | https://                                                           |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             | https://                                                           |
| click                         | https://palletsprojects.com/p/click/                                                | https://                                                           |
| click-completion              | https://github.com/click-contrib/click-completion                                   | https://                                                           |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   | https://                                                           |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      | https://                                                           |
| click-repl                    | https://github.com/untitaker/click-repl                                             | https://                                                           |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            | https://                                                           |
| cmake                         | https://cmake.org/                                                                  | https://                                                           |
| colorama                      | https://github.com/tartley/colorama                                                 | https://                                                           |
| comm                          | https://github.com/ipython/comm                                                     | https://                                                           |
| compose                       | https://github.com/docker/compose                                                   | https://                                                           |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        | https://                                                           |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      | https://                                                           |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     | https://                                                           |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            | https://                                                           |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           | https://                                                           |
| confuse                       | https://github.com/beetbox/confuse                                                  | https://                                                           |
| contourpy                     | https://github.com/contourpy/contourpy                                              | https://                                                           |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               | https://                                                           |
| cryptography                  | https://github.com/pyca/cryptography                                                | https://                                                           |
| cssselect2                    | https://github.com/Kozea/cssselect2                                                 | https://                                                           |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           | https://                                                           |
| cupy-cuda113                  | https://cupy.dev/                                                                   | https://                                                           |
| curl                          | https://curl.se                                                                     | https://                                                           |
| cycler                        | https://github.com/matplotlib/cycler                                                | https://                                                           |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             | https://                                                           |
| Cython                        | https://cython.org                                                                  | https://                                                           |
| d3                            | https://github.com/mbostock/d3                                                      | https://                                                           |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           | https://                                                           |
| ddsketch                      | http://github.com/datadog/sketches-py                                               | https://                                                           |
| debugpy                       | https://aka.ms/debugpy                                                              | https://                                                           |
| decimal                       | https://github.com/shopspring/decimal                                               | https://                                                           |
| decorator                     | https://github.com/micheles/decorator                                               | https://                                                           |
| deepdiff                      | https://github.com/seperman/deepdiff                                                | https://                                                           |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https:/                                                            |
| dill                          | https://github.com/uqfoundation/dill                                                | https:/                                                            |
| distro                        | Orion Floes                                                                         | https:/                                                            |
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
| FLTK                          | https://www.fltk.org/index.php                                                      | https:/                                                            |
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
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https://                                                           |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https://                                                           |
| graphviz                      | https://graphviz.org/                                                               | https://                                                           |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https://                                                           |
| groupcache                    | https://github.com/golang/groupcache                                                | https://                                                           |
| grpc                          | https://google.golang.org/grpc                                                      | https://                                                           |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https://                                                           |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https://                                                           |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  | https://                                                           |
| gts                           | https://sourceforge.net/projects/gts/                                               | https://                                                           |
| h5py                          | https://www.h5py.org                                                                | https://                                                           |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https://                                                           |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https://                                                           |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https://                                                           |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https://                                                           |
| he                            | https://github.com/mathiasbynens/he                                                 | https://                                                           |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https://                                                           |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https://                                                           |
| htslib                        | https://www.htslib.org                                                              | https://                                                           |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https://                                                           |
| icu                           | https://github.com/unicode-org/icu                                                  | https://                                                           |
| idna                          | https://github.com/kjd/idna                                                         | https://                                                           |
| imageio                       | https://github.com/imageio/imageio                                                  | https://                                                           |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https://                                                           |
| ImmuneBuilder                 | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https://                                                           |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https://                                                           |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https://                                                           |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https://                                                           |
| inflection                    | https://github.com/jinzhu/inflection                                                | https://                                                           |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https://                                                           |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https://                                                           |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https://                                                           |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https://                                                           |
| ipykernel                     | https://ipython.org                                                                 | https://                                                           |
| ipython                       | https://ipython.org                                                                 | https://                                                           |
| ipython-genutils              | http://ipython.org                                                                  | https://                                                           |
| ipywidgets                    | http://jupyter.org                                                                  | https://                                                           |
| isodate                       | https://github.com/gweis/isodate/                                                   | https://                                                           |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https://                                                           |
| jax                           | https://github.com/google/jax                                                       | https://                                                           |
| jaxlib                        | https://github.com/google/jax                                                       | https://                                                           |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              | https://                                                           |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https://                                                           |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https://                                                           |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https://                                                           |
| jpeg                          | https://www.ijg.org                                                                 | https://                                                           |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https://                                                           |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https://                                                           |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:/                                                            |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https:/                                                            |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https:/                                                            |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:/                                                            |
| jstat                         | https://github.com/jstat/jstat                                                      | https:/                                                            |
| jupyter-client                | https://jupyter.org                                                                 | https:/                                                            |
| jupyter-core                  | https://jupyter.org                                                                 | https:/                                                            |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https:/                                                            |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:/                                                            |
| jupyter-server                | http://jupyter.org                                                                  | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:/                                                            |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:/                                                            |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:/                                                            |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:/                                                            |
| jupyter_client                | http://jupyter.org                                                                  | https:/                                                            |
| jupyter_core                  | http://jupyter.org                                                                  | https:/                                                            |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https:/                                                            |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:/                                                            |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:/                                                            |
| keras                         | https://github.com/keras-team/keras                                                 | https:/                                                            |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:/                                                            |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:/                                                            |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:/                                                            |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:/                                                            |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:/                                                            |
| kombu                         | https://kombu.readthedocs.io                                                        | https:/                                                            |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                       | https:/                                                            |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:/                                                            |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:/                                                            |
| lcms2                         | https://www.littlecms.com                                                           | https:/                                                            |
| lerc                          | https://github.com/Esri/lerc                                                        | https:/                                                            |
| libarchive                    | http://www.libarchive.org                                                           | https:/                                                            |
| libblas                       | https://www.netlib.org/blas/                                                        | https:/                                                            |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:/                                                            |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:/                                                            |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https:/                                                            |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                |
| libclang                      | <b>Orion Floes</b>                                                                  | https:/                                                            |
| libcurl                       | https://curl.se/libcurl/                                                            | https:/                                                            |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:/                                                            |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:/                                                            |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:/                                                            |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://                                                            |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:/                                                            |
| libffi                        | https://github.com/libffi/libffi                                                    | https:/                                                            |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:/                                                            |
| libgd                         | https://libgd.github.io                                                             | https:/                                                            |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:/                                                            |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
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
| zlib                          | https://zlib.net                                                                    | https:/                                                            |
| lime                          | https://github.com/marcoter/lime                                                    |                                                                    |
| lit                           | http://llvm.org                                                                     | https:/<br>https:/                                                 |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               |                                                                    |
| llvmlite                      | http://llvmlite.readthedocs.io                                                      | https:/                                                            |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https:/                                                            |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https:/                                                            |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https:/                                                            |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/                                                            |
| lxml                          | https://lxml.de                                                                     | https:/                                                            |
| lz4-c                         | https://www.lz4.org/                                                                | https:/                                                            |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https:/                                                            |
| markdown-it-py                | Orion Floes                                                                         | https:/                                                            |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https:/                                                            |
| matplotlib                    | https://matplotlib.org                                                              | https:/                                                            |
| matplotlib-base               | https://matplotlib.org                                                              | https:/                                                            |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https:/                                                            |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/                                                            |
| mdtraj                        | https://www.mdtraj.org/                                                             | https:/                                                            |
| mdurl                         | Orion Floes                                                                         | https:/                                                            |
| menuinst                      | Orion Floes                                                                         | https:/                                                            |
| mergo                         | https://github.com/imdario/mergo                                                    | https:/                                                            |
| mistune                       | https://github.com/lepture/mistune                                                  | https:/                                                            |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https:/                                                            |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https:/                                                            |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https:/                                                            |
| ml-dtypes                     | Orion Floes                                                                         | https:/                                                            |
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
| namex                         | Orion Floes                                                                         | https:/                                                            |
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
|                               |                                                                                     | Ъ                                                                  |
| Name of Project               | Website                                                                             | Licen                                                              |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https:/                                                            |
| pango                         | https://pango.gnome.org                                                             | https:/                                                            |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https:/                                                            |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                            |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https:/                                                            |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https:/                                                            |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https:/                                                            |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https:/                                                            |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https:/                                                            |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/                                                            |
| pcre                          | https://www.pcre.org                                                                | https:/                                                            |
| pcre2                         | https://www.pcre.org                                                                | https:/                                                            |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https:/                                                            |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https:/                                                            |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https:/                                                            |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https:/                                                            |
| pgio                          | https://github.com/jackc/pgio                                                       | https:/                                                            |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https:/                                                            |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https:/                                                            |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https:/                                                            |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https:/                                                            |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https:/                                                            |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https:/                                                            |
| Pillow                        | https://python-pillow.org                                                           | https:/                                                            |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https:/                                                            |
| pip                           | https://pip.pypa.io/                                                                | https:/                                                            |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https:/                                                            |
| pixman                        | https://pixman.org                                                                  | https:/                                                            |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https:/                                                            |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https:/                                                            |
| plotly                        | https://plotly.com/python/                                                          | https:/                                                            |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https:/                                                            |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https:/                                                            |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/                                                            |
| pooch                         | https://github.com/fatiando/pooch                                                   | https:/                                                            |
| pox                           | https://github.com/uqfoundation/pox                                                 | https:/                                                            |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https:/                                                            |
| pq                            | https://github.com/lib/pq                                                           | https:/                                                            |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https:/                                                            |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https:/                                                            |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/                                                            |
| protobuf                      | https://google.golang.org/protobuf                                                  | https:/                                                            |
| psi4                          | https://psicode.org                                                                 | https:/                                                            |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https:/                                                            |
| psycopg2                      | https://psycopg.org/                                                                | https:/                                                            |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https:/                                                            |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https:/                                                            |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/                                                            |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http://                                                            |
|                               |                                                                                     |                                                                    |
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
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   | https://                                                           |
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
| pyyaml                        | No longer available                                                                 | No license                                                         |
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
| Name of Project               | Website                                                                             | License                                                            |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https://                                                           |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https://                                                           |
| reportlab                     | https://www.reportlab.com                                                           | https://                                                           |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https://                                                           |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https://                                                           |
| requests                      | https://requests.readthedocs.io                                                     | https://                                                           |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https://                                                           |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https://                                                           |
| resumable                     | https://github.com/stevvooe/resumable                                               | https://                                                           |
| retrying                      | https://github.com/rholder/retrying                                                 | https://                                                           |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https://                                                           |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https://                                                           |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https://                                                           |
| rich                          | https://github.com/Textualize/rich                                                  | https://                                                           |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https://                                                           |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https://                                                           |
| rsa                           | https://stuvel.eu/rsa                                                               | https://                                                           |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https://                                                           |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https://                                                           |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https://                                                           |
| sasl                          | https://mellium.im/sasl                                                             | https://                                                           |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https://                                                           |
| scikit-image                  | https://scikit-image.org                                                            | https://                                                           |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https://                                                           |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https://                                                           |
| scipy                         | https://scipy.org                                                                   | https://                                                           |
| seaborn                       | https://seaborn.pydata.org                                                          | https://                                                           |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https://                                                           |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https://                                                           |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https://                                                           |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https://                                                           |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https://                                                           |
| sh                            | https://github.com/amoffat/sh                                                       | https://                                                           |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https://                                                           |
| simint                        | https://www.bennyp.org/research/simint/                                             | https://                                                           |
| six                           | https://github.com/benjaminp/six                                                    | https://                                                           |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https://                                                           |
| snappy                        | https://github.com/google/snappy                                                    | https://                                                           |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https://                                                           |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https://                                                           |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https://                                                           |
| spglib                        | https://github.com/spglib/spglib                                                    | https://                                                           |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https://                                                           |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https://                                                           |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https://                                                           |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https://                                                           |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https://                                                           |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https://                                                           |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          | https://                                                           |
| sqlite                        | https://sqlite.org/index.html                                                       | https://                                                           |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            | https://                                                           |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             | https://                                                           |
| starfile                      | https://github.com/alisterburt/starfile                                             | https://                                                           |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          | https://                                                           |
| structlog                     | https://www.structlog.org/                                                          | https://                                                           |
| svglib                        | https://github.com/deeplook/svglib                                                  | https://                                                           |
| sympy                         | https://sympy.org                                                                   | https://                                                           |
| tables                        | https://www.pytables.org/                                                           | https://                                                           |
| tabulate                      | https://github.com/astanin/python-tabulate                                          | https://                                                           |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                | https://                                                           |
| tenacity                      | https://github.com/jd/tenacity                                                      | https://                                                           |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           | https://                                                           |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           | https://                                                           |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           | https://                                                           |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            | https://                                                           |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             | https://                                                           |
| tensorflow-io-gcs-filesystem  | Orion Floes                                                                         | https://                                                           |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           | https://                                                           |
| termcolor                     | https://github.com/hugovk/termcolor                                                 | https://                                                           |
| terminado                     | https://github.com/jupyter/terminado                                                | https://                                                           |
| testpath                      | https://github.com/jupyter/testpath                                                 | https://                                                           |
| textangular                   | https://github.com/fraywing/textAngular                                             | https://                                                           |
| tf_keras                      | Orion Floes                                                                         | https://                                                           |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             | https://                                                           |
| three                         | https://github.com/mrdoob/three.js                                                  | https://                                                           |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                | https://                                                           |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  | https://                                                           |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             | https://                                                           |
| tk                            | https://www.tcl.tk/                                                                 | https://                                                           |
| toml                          | https://github.com/toml-lang/toml                                                   | https://                                                           |
| tomli                         | https://github.com/hukkin/tomli                                                     | https://                                                           |
| toolz                         | https://github.com/pytoolz/toolz                                                    | https://                                                           |
| torch                         | https://pytorch.org/                                                                | https://                                                           |
| tornado                       | https://www.tornadoweb.org                                                          | https://                                                           |
| tqdm                          | https://github.com/tqdm/tqdm                                                        | https://                                                           |
| tracy                         | https://github.com/gear-genomics/tracy                                              | https://                                                           |
| traitlets                     | https://github.com/ipython/traitlets                                                | https://                                                           |
| triton                        | https://github.com/openai/triton/                                                   | https://                                                           |
| truststore                    | Orion Floes                                                                         | https://                                                           |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               | https://                                                           |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             | https://                                                           |
| twine                         | https://github.com/pypa/twine                                                       | https://                                                           |
| twinj uuid                    | https://github.com/twinj/uuid                                                       | https://                                                           |
| types                         | https://github.com/babel/babel                                                      | https://                                                           |
| typescript                    | https://github.com/Microsoft/TypeScript                                             | https://                                                           |
| typing_extensions             | https://github.com/python/typing                                                    | https://                                                           |
| tzdata                        | https://github.com/python/tzdata                                                    | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | https://                                                           |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | https://                                                           |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | https://                                                           |
| uritools                      | https://github.com/tkem/uritools                                                    | https://                                                           |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | https://                                                           |
| vine                          | https://github.com/celery/vine                                                      | https://                                                           |
| vue                           | https://github.com/vuejs/vue                                                        | https://                                                           |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | https://                                                           |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | https://                                                           |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | https://                                                           |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | https://                                                           |
| westpa                        | Orion Floes                                                                         | http://                                                            |
| wheel                         | https://github.com/pypa/wheel                                                       | https://                                                           |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | https://                                                           |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | https://                                                           |
| wsutil                        | https://github.com/yhat/wsutil                                                      | https://                                                           |
| x/lint                        | https://golang.org/x/lint                                                           | https://                                                           |
| x/mod                         | https://golang.org/x/mod/semver                                                     | https://                                                           |
| x/net                         | https://golang.org/x/net                                                            | https://                                                           |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | https://                                                           |
| x/sys                         | https://golang.org/x/sys                                                            | https://                                                           |
| x/text                        | https://golang.org/x/text                                                           | https://                                                           |
| x/tools                       | https://golang.org/x/tools                                                          | https://                                                           |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | https://                                                           |
| xhtml2pdf                     | https://github.com/xhtml2pdf/xhtml2pdf                                              | https://                                                           |
| xlrd                          | https://github.com/python-excel/xlrd                                                | https://                                                           |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | https://                                                           |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | https://                                                           |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https://                                                           |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https://                                                           |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https://                                                           |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https://                                                           |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https://                                                           |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https://                                                           |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https://                                                           |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https://                                                           |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https://                                                           |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https://                                                           |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https://                                                           |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https://                                                           |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | https://                                                           |
| xz                            | https://github.com/ulikunitz/xz                                                     | https://                                                           |
| yaml                          | https://pyyaml.org/                                                                 | https://                                                           |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  | https://                                                           |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | https://                                                           |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | https://                                                           |
| yarl                          | https://github.com/aio-libs/yarl                                                    | https://                                                           |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | https://                                                           |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                                                                |
| zap                           | https://go.uber.org/zap                                                             | https:/                                                            |
| zipp                          | https://github.com/jaraco/zipp                                                      | https:/                                                            |
| zlib                          | https://zlib.net/                                                                   | https:/                                                            |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https:/                                                            |
| zstd                          | https://facebook.github.io/zstd/                                                    | https:/                                                            |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:/                                                            |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:/                                                            |

# **8.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

# **8.1.1 GCC RUNTIME LIBRARY EXCEPTION**

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise  $\rightarrow$ based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

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

License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. 14. Revised Versions of this License. The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. 15. Disclaimer of Warranty. THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 16. Limitation of Liability. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF

17. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided

(continues on next page)

SUCH DAMAGES.

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page)

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

## See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# A

AddNormalizationRule OEMolProp:: OEFilter, 102

# $\mathsf{C}$

ClearNormalizationRules OEMolProp:: OEFilter, 102 Constructors OEMolProp:: OEFilter, 101 OEMolProp:: OEXLogPResult, 107

# F

```
Example Code
   molfilter.py, 84
   molpropcsv.py, 98
   molpropsddata.py, 95
   molproptable.py, 90
   quietfilter.py, 87
   specificmolprop.py, 92
```

# G

GetCanonOrder OEMolProp:: OEFilter, 102 GetFilterType OEMolProp:: OEFilter, 103 GetFlagTableFailures OEMolProp:: OEFilter, 103 GetMessage OEMolProp:: OEFilter, 103 GetMMFFTypeCheck OEMolProp:: OEFilter, 103 GetpKaNormalize OEMolProp:: OEFilter, 104 GetSDTag OEMolProp:: OEFilter, 103 GetTable OEMolProp:: OEFilter, 104 GetTypeCheck OEMolProp:: OEFilter, 104 GetValue OEMolProp:: OEXLogPResult, 107

# I

```
IsValid()
   OEMolProp:: OEXLogPResult, 107
```

# M

molfilter.pv Example Code, 84 molpropcsv.py Example Code, 98 molpropsddata.py Example Code, 95 molproptable.py Example Code, 90

# $\Omega$

OEMolProp:: OECheckXLogXType, 110 OEMolProp:: OECheckXLogXTypes, 110 OEMolProp:: OEConfigureFilterParams, 111 OEMolProp:: OEConfigureFilterType, 111 OEMolProp:: OEFilter, 101 AddNormalizationRule, 102 ClearNormalizationRules. 102 Constructors, 101 GetCanonOrder, 102 GetFilterType, 103 GetFlagTableFailures, 103 GetMessage, 103 GetMMFFTypeCheck, 103 GetpKaNormalize, 104 GetSDTag, 103 GetTable, 104 GetTypeCheck, 104 operator bool, 102 operator(), 101 operator=,  $101$ ParseNewRules, 104 PrintConfig, 105 SetCanonOrder, 105 SetErrorLevel. 105 SetFlagTableFailures, 105 SetMMFFTypeCheck, 105 SetpKaNormalize, 107

SetSDTag, 106 operator bool SetTable, 106 OEMolProp:: OEFilter, 102 SetTypeCheck, 106 operator() OEMolProp:: OEFilterParamName, 109 OEMolProp:: OEFilter, 101 OEMolProp:: OEFilterParamName:: Type, 109 operator= OEMolProp:: OEFilterParamSetup, 109 OEMolProp:: OEFilter, 101 OEMolProp:: OEFilterParamSetup:: All, 110 P OEMolProp:: OEFilterParamSetup:: Type, 110 OEMolProp:: OEFilterType, 108 ParseNewRules OEMolProp:: OEFilterType:: BlockBuster, OEMolProp:: OEFilter, 104 108 PrintConfig OEMolProp::OEFilterType::BlockBusterPAINS, OEMolProp::OEFilter, 105 109  $\Omega$ OEMolProp::OEFilterType::Default, 108 OEMolProp:: OEFilterType:: Drug, 108 quietfilter.py OEMolProp:: OEFilterType:: Fragment, 108 Example Code, 87 OEMolProp:: OEFilterType:: Lead, 109 OEMolProp:: OEFilterType:: Max, 109 S OEMolProp:: OEFilterType:: PAINS, 109 SetCanonOrder OEMolProp:: OEGet2dPSA, 111 OEMolProp:: OEFilter, 105 OEMolProp:: OEGetAnionicCarbonCount, 113 SetErrorLevel OEMolProp:: OEGetAromaticRingCount, 113 OEMolProp:: OEFilter, 105 OEMolProp:: OEGetFilterType, 114 SetFlagTableFailures OEMolProp:: OEGetFractionCsp3, 114 OEMolProp:: OEFilter, 105 OEMolProp:: OEGetHalideFraction, 114 SetMMFFTypeCheck OEMolProp:: OEGetHBondAcceptorCount, 114 OEMolProp:: OEFilter, 105 OEMolProp:: OEGetHBondDonorCount, 116 SetpKaNormalize OEMolProp:: OEGetLipinskiAcceptorCount, OEMolProp:: OEFilter, 107 116 SetSDTag OEMolProp:: OEGetLipinskiDonorCount, 117 OEMolProp:: OEFilter, 106 OEMolProp::OEGetLongestUnbranchedCarbonsChainable 118 OEMolProp::OEGetLongestUnbranchedHeavyAtemsChain. OEMolProp:: OEFilter, 106 118 OEMolProp:: OEFilter, 106 OEMolProp::OEGetNumUnspecifiedAtomStereos.com/specificmolprop.py 120 Example Code, 92 OEMolProp:: OEGetNumUnspecifiedBondStereos, 120 OEMolProp:: OEGetRotatableBondCount, 120 OEMolProp:: OEGetXLogP, 122 OEMolProp:: OEGetXLoqPResult, 122 OEMolProp:: OEGetXLoqPVersion, 123 OEMolProp:: OEMolPropGetArch, 123 OEMolProp:: OEMolPropGetLicensee, 124 OEMolProp:: OEMolPropGetPlatform, 124 OEMolProp:: OEMolPropGetRelease, 124 OEMolProp:: OEMolPropGetSite, 125 OEMolProp:: OEMolPropGetVersion, 125 OEMolProp:: OEMolPropIsLicensed, 125 OEMolProp:: OEWritePropertyDataToCSV, 125 OEMolProp:: OEXLogPResult, 107 Constructors, 107 GetValue. 107  $IsValid()$ , 107