![](_page_0_Picture_0.jpeg)

**Quacpac TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1      | <b>Theory</b>               |        | <span style="float:right;">1</span>                                                                                                      |
|--------|-----------------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------|
|        | 1.1                         |        | Introduction to Quacpac TK <span style="float:right;">1</span>                                                                           |
|        | 1.2                         |        | tautomers <span style="float:right;">1</span>                                                                                            |
|        |                             | 1.2.1  | Visualization <span style="float:right;">1</span>                                                                                        |
|        |                             | 1.2.2  | Reasonable Tautomer Ensemble <span style="float:right;">1</span>                                                                         |
|        |                             | 1.2.3  | Canonicalization <span style="float:right;">1</span>                                                                                     |
|        |                             | 1.2.4  | Complete Enumeration <span style="float:right;">1</span>                                                                                 |
|        | 1.3                         |        | pkatyper – Ligand pKa <span style="float:right;">1</span>                                                                                |
|        |                             | 1.3.1  | Introduction <span style="float:right;">1</span>                                                                                         |
|        |                             | 1.3.2  | Theory <span style="float:right;">1</span>                                                                                               |
|        | 1.4                         |        | molcharge – Partial Charges <span style="float:right;">1</span>                                                                          |
|        |                             | 1.4.1  | Introduction <span style="float:right;">1</span>                                                                                         |
|        |                             | 1.4.2  | Theory <span style="float:right;">1</span>                                                                                               |
|        | 1.5                         |        | Wiberg bond orders <span style="float:right;">1</span>                                                                                   |
|        |                             | 1.5.1  | Theory <span style="float:right;">1</span>                                                                                               |
| 2      | <b>Examples</b>             |        | <span style="float:right;">1</span>                                                                                                      |
|        | 2.1                         |        | Quacpac TK Examples <span style="float:right;">1</span>                                                                                  |
|        |                             | 2.1.1  | Assigning Charges <span style="float:right;">1</span>                                                                                    |
|        |                             | 2.1.2  | Setting a Neutral Ionization State <span style="float:right;">1</span>                                                                   |
|        |                             | 2.1.3  | Enumerating Tautomers <span style="float:right;">1</span>                                                                                |
|        |                             | 2.1.4  | Setting a Reasonable Charge State <span style="float:right;">1</span>                                                                    |
|        |                             | 2.1.5  | Obtaining Wiberg bond orders <span style="float:right;">1</span>                                                                         |
|        |                             | 2.1.6  | Applying Charges to OEDesignUnit <span style="float:right;">1</span>                                                                     |
|        |                             | 2.1.7  | Enumerate ionization states at neutral pH using OEMultistatepKaModel and OEMultistatepKaModelOptions <span style="float:right;">2</span> |
| 3      | <b>API</b>                  |        | <span style="float:right;">2</span>                                                                                                      |
|        | 3.1                         |        | OEProton Classes <span style="float:right;">2</span>                                                                                     |
|        |                             | 3.1.1  | OEAM1BCCCharges <span style="float:right;">2</span>                                                                                      |
|        |                             | 3.1.2  | OEAM1BCCELF10Charges <span style="float:right;">2</span>                                                                                 |
|        |                             | 3.1.3  | OEAM1Charges <span style="float:right;">2</span>                                                                                         |
|        |                             | 3.1.4  | OEAmberFF94Charges <span style="float:right;">2</span>                                                                                   |
|        |                             | 3.1.5  | OEChargeEngineBase <span style="float:right;">2</span>                                                                                   |
|        |                             | 3.1.6  | OEChargeEngineNoOp <span style="float:right;">3</span>                                                                                   |
|        |                             | 3.1.7  | OEClearCharges <span style="float:right;">3</span>                                                                                       |
|        |                             | 3.1.8  | OECombineChargeEngines <span style="float:right;">3</span>                                                                               |
|        |                             | 3.1.9  | OEDesignUnitCharges <span style="float:right;">3</span>                                                                                  |
|        |                             | 3.1.10 | OEELF <span style="float:right;">3</span>                                                                                                |
|        |                             | 3.1.11 | OEELFCharges <span style="float:right;">3</span>                                                                                         |
| 3.1.12 | OEELFOptions                | 3      |                                                                                                                                          |
| 3.1.13 | OEFormalChargeOptions       | 3      |                                                                                                                                          |
| 3.1.14 | OEFormalToPartialCharges    | 4      |                                                                                                                                          |
| 3.1.15 | OEGasteigerCharges          | 4      |                                                                                                                                          |
| 3.1.16 | OEInitialCharges            | 4      |                                                                                                                                          |
| 3.1.17 | OEMMFF94Charges             | 4      |                                                                                                                                          |
| 3.1.18 | OESpreadMetalCharges        | 4      |                                                                                                                                          |
| 3.1.19 | OETautomerOptions           | 4      |                                                                                                                                          |
| 3.1.20 | OETautomerMolFunction       | 4      |                                                                                                                                          |
| 3.1.21 | OETyperMolFunction          | 5      |                                                                                                                                          |
| 3.2    | OEProton Constants          | 5      |                                                                                                                                          |
| 3.2.1  | OECharges                   | 5      |                                                                                                                                          |
| 3.2.2  | OEChargingRequirement       | 5      |                                                                                                                                          |
| 3.2.3  | OEHybridizationLevel        | 5      |                                                                                                                                          |
| 3.2.4  | OERacemicType               | 5      |                                                                                                                                          |
| 3.3    | OEProton Functions          | 5      |                                                                                                                                          |
| 3.3.1  | OEAssignCharges             | 5      |                                                                                                                                          |
| 3.3.2  | OEAssignPartialCharges      | 5      |                                                                                                                                          |
| 3.3.3  | OEEnumerateFormalCharges    | 5      |                                                                                                                                          |
| 3.3.4  | OEEnumerateTautomers        | 6      |                                                                                                                                          |
| 3.3.5  | OEGetChargeTypeName         | 6      |                                                                                                                                          |
| 3.3.6  | OEGetReasonableProtomer     | 6      |                                                                                                                                          |
| 3.3.7  | OEGetReasonableProtomers    | 6      |                                                                                                                                          |
| 3.3.8  | OEGetReasonableTautomers    | 6      |                                                                                                                                          |
| 3.3.9  | OEGetUniqueProtomer         | 6      |                                                                                                                                          |
| 3.3.10 | OEHypervalentNormalization  | 6      |                                                                                                                                          |
| 3.3.11 | OEQuacPacGetArch            | 6      |                                                                                                                                          |
| 3.3.12 | OEQuacPacGetLicensee        | 6      |                                                                                                                                          |
| 3.3.13 | OEQuacPacGetPlatform        | 6      |                                                                                                                                          |
| 3.3.14 | OEQuacPacGetRelease         | 6      |                                                                                                                                          |
| 3.3.15 | OEQuacPacGetSite            | 6      |                                                                                                                                          |
| 3.3.16 | OEQuacPacGetVersion         | 6      |                                                                                                                                          |
| 3.3.17 | OEQuacPacIsLicensed         | 6      |                                                                                                                                          |
| 3.3.18 | OERemoveFormalCharge        | 6      |                                                                                                                                          |
| 3.3.19 | OESetNeutralpHModel         | 6      |                                                                                                                                          |
| 3.3.20 | OETautomersLargestZoneSize  | 6      |                                                                                                                                          |
| 3.4    | OEMolAM1 Classes            | 6      |                                                                                                                                          |
| 3.4.1  | OEAM1                       | 6      |                                                                                                                                          |
| 3.4.2  | OEAM1Options                | 6      |                                                                                                                                          |
| 3.4.3  | OEAM1Results                | 7      |                                                                                                                                          |
| 3.4.4  | OEOptimizedAM1              | 7      |                                                                                                                                          |
| 3.5    | OEMolAM1 Constants          | 7      |                                                                                                                                          |
| 3.5.1  | OEMethodType                | 7      |                                                                                                                                          |
| 3.6    | OEMolAM1 Constants          | 7      |                                                                                                                                          |
| 3.6.1  | OEBCCType                   | 7      |                                                                                                                                          |
| 3.7    | OEAM1BCC Functions          | 7      |                                                                                                                                          |
| 3.7.1  | OEBCCPartialCharges         | 7      |                                                                                                                                          |
| 3.7.2  | OESymmetrizePartialCharges  | 7      |                                                                                                                                          |
| 4      | Preliminary API             | 7      |                                                                                                                                          |
| 4.1    | Preliminary OEProton Class  | 7      |                                                                                                                                          |
| 4.1.1  | OEChargeParameter           | 7      |                                                                                                                                          |
| 4.1.2  | OEMultistatepKaModel        | 7      |                                                                                                                                          |
| 4.1.3  | OEMultistatepKaModelOptions | 7      |                                                                                                                                          |

| Section | Title                           | Page |
|---------|---------------------------------|------|
| 4.2     | Preliminary OEProton Constants  | 78   |
| 4.2.1   | OEAdjTypeAtNeutralpH            | 78   |
| 4.2.2   | OEMultistatepKaModelpH          | 79   |
| 4.2.3   | OEpKaRange                      | 80   |
| 4.3     | Preliminary OEProton Functions  | 81   |
| 4.3.1   | OEGetAtomAdjTypeAtNeutralpHName | 81   |
| 4.3.2   | OEGetAtomAdjTypeAtNeutralpHType | 81   |
| 4.3.3   | OEGetAtompKaRangeName           | 81   |
| 4.3.4   | OEGetAtompKaRangeType           | 82   |
| 4.3.5   | OEGetMultistatepKaModelpHName   | 82   |
| 4.3.6   | OEGetMultistatepKaModelpHType   | 82   |
| 5       | Release History                 | 83   |
| 5.1     | Quacpac TK 2.2.5                | 83   |
| 5.1.1   | Minor bug fixes                 | 83   |
| 5.2     | Quacpac TK 2.2.4                | 83   |
| 5.3     | Quacpac TK 2.2.3                | 83   |
| 5.4     | Quacpac TK 2.2.2                | 83   |
| 5.5     | Quacpac TK 2.2.1                | 83   |
| 5.6     | Quacpac TK 2.2.0                | 83   |
| 5.6.1   | New features                    | 83   |
| 5.7     | Quacpac TK 2.1.4                | 84   |
| 5.7.1   | New features                    | 84   |
| 5.7.2   | Major bug fixes                 | 84   |
| 5.7.3   | Minor bug fixes                 | 84   |
| 5.7.4   | Python-specific changes         | 84   |
| 5.7.5   | Java-specific changes           | 84   |
| 5.7.6   | C#-specific changes             | 84   |
| 5.7.7   | Documentation changes           | 84   |
| 5.8     | Quacpac TK 2.1.3                | 84   |
| 5.8.1   | New features                    | 84   |
| 5.9     | Quacpac TK 2.1.2                | 84   |
| 5.10    | Quacpac TK 2.1.1.2              | 84   |
| 5.11    | Quacpac TK 2.1.1                | 85   |
| 5.11.1  | New features                    | 85   |
| 5.12    | Quacpac TK 2.1.0                | 85   |
| 5.12.1  | New features                    | 85   |
| 5.12.2  | Minor bug fixes                 | 85   |
| 5.13    | Quacpac TK 2.0.2                | 86   |
| 5.13.1  | New features (Preliminary)      | 86   |
| 5.13.2  | New features                    | 86   |
| 5.14    | Quacpac TK 2.0.1                | 86   |
| 5.14.1  | Minor bug fixes                 | 86   |
| 5.15    | Quacpac TK 2.0.0                | 86   |
| 5.15.1  | New features                    | 86   |
| 5.15.2  | Major bug fixes                 | 87   |
| 5.15.3  | Minor bug fixes                 | 87   |
| 5.15.4  | Documentation changes           | 87   |
| 5.16    | Quacpac TK 1.9.3                | 87   |
| 5.16.1  | New features                    | 87   |
| 5.16.2  | Documentation changes           | 88   |
| 5.17    | Quacpac TK 1.9.2                | 88   |
| 5.17.1  | Minor bug fixes                 | 88   |
| 5.17.2  | Documentation changes           | 88   |

|      | 5.18 Quacpac TK 1.9.1              | 88 |
|------|------------------------------------|----|
|      | 5.18.1 Documentation changes       | 88 |
| 5.19 | Quacpac TK 1.9.0                   | 88 |
|      | 5.19.1<br>New features             | 88 |
|      | 5.19.2<br>Minor bug fixes          | 88 |
|      | 5.19.3<br>Documentation changes    | 88 |
| 5.20 | Quacpac TK 1.8.6                   | 89 |
| 5.21 | Quacpac TK 1.8.5                   | 89 |
| 5.22 | Quacpac TK 1.8.4                   | 89 |
|      | 5.22.1<br>New features             | 89 |
|      | 5.22.2<br>Major bug fixes          | 89 |
|      | 5.22.3<br>Deprecated functionality | 89 |
| 5.23 | Quacpac TK 1.8.3                   | 89 |
|      | 5.23.1<br>New features             | 89 |
|      | 5.23.2<br>Major bug fixes          | 90 |
| 5.24 | Quacpac TK 1.8.2                   | 90 |
|      | 5.24.1<br>Minor bug fixes          | 90 |
| 5.25 | Quacpac TK 1.8.1                   | 90 |
|      | 5.25.1<br>New features             | 90 |
|      | 5.25.2<br>Minor bug fixes          | 90 |
|      | 5.25.3<br>Documentation fixes      | 90 |
| 5.26 | Quacpac TK 1.8.0                   | 90 |
|      | 5.26.1<br>New features             | 90 |
|      | 5.26.2<br>Minor bug fixes          | 93 |
|      | 5.26.3<br>Known bugs               | 93 |
|      | 5.26.4<br>Documentation fixes      | 93 |
| 5.27 | Quacpac TK 1.7.2                   | 94 |
|      | 5.27.1<br>New features             | 94 |
|      | 5.27.2<br>Minor bug fixes          | 94 |
|      | 5.27.3<br>Documentation fixes      | 94 |
| 5.28 | Quacpac TK 1.7.1                   | 94 |
|      | 5.28.1<br>New features             | 94 |
|      | 5.28.2<br>Minor bug fixes          | 94 |
|      | 5.28.3<br>Documentation fixes      | 94 |
| 5.29 | Quacpac TK 1.7.0                   | 94 |
|      | 5.29.1<br>New features             | 94 |
| 5.30 | Quacpac TK 1.6.4                   | 95 |
|      | 5.30.1<br>New features             | 95 |
|      | 5.30.2<br>Minor bug fixes          | 95 |
| 5.31 | Quacpac TK 1.6.2                   | 95 |
|      | 5.31.1<br>Major bug fixes          | 95 |
|      | 5.31.2<br>Minor bug fixes          | 95 |
| 5.32 | Quacpac TK 1.6.1                   | 95 |
|      | 5.32.1<br>New features             | 95 |
|      | 5.32.2<br>Major bug fixes          | 96 |
|      | 5.32.3<br>Minor bug fixes          | 96 |
| 5.33 | Quacpac TK 1.6.0                   | 96 |
|      | 5.33.1<br>New features             | 96 |
|      | 5.33.2<br>Bug fixes                | 96 |
| 5.34 | Quacpac TK 1.5.2                   | 96 |
|      | 5.34.1<br>New features             | 96 |
|      | 5.34.2<br>Minor bug fixes          | 96 |
| 5.35 | Quacpac TK 1.5.1                   | 97 |
|      | 5.35.1<br>Bug fixes                | 97 |

|   | 5.36            | Quacpac TK 1.5.0                    | 97  |
|---|-----------------|-------------------------------------|-----|
|   |                 | 5.36.1 New Features                 | 97  |
|   | 5.37            | Quacpac TK 1.4.1                    | 97  |
|   |                 | 5.37.1 Bug Fixes                    | 97  |
|   | 5.38            | Quacpac TK 1.4.0                    | 97  |
|   |                 | 5.38.1 New features                 | 97  |
|   | 5.39            | Quacpac TK 1.3.1                    | 98  |
|   |                 | 5.39.1 New features                 | 98  |
|   |                 | 5.39.2 Bug fixes                    | 98  |
|   | 5.40            | Quacpac TK 1.3.0                    | 98  |
|   |                 | 5.40.1 New features                 | 98  |
|   |                 | 5.40.2 Bug fixes                    | 98  |
|   | 5.41            | Quacpac TK 1.1.0                    | 99  |
| 6 |                 | <b>Copyright and Trademarks</b>     | 101 |
| 7 |                 | <b>Sample Code</b>                  | 103 |
| 8 | <b>Citation</b> |                                     | 105 |
|   | 8.1             | Orion ® Floes                       | 105 |
|   | 8.2             | Toolkits and Applications           | 105 |
|   | 8.3             | OpenEye Web Services                | 107 |
| 9 |                 | <b>Technology Licensing</b>         | 109 |
|   | 9.1             | GCC                                 | 124 |
|   |                 | 9.1.1 GCC RUNTIME LIBRARY EXCEPTION | 124 |
|   |                 | 9.1.2 GNU GENERAL PUBLIC LICENSE    | 124 |

### **CHAPTER**

# **THEORY**

## 1.1 Introduction to Quacpac TK

The chemistry of molecular interactions is a matter of shape and electrostatics, but doing electrostatics poorly is worse than doing none at all; accurate charges are required. Even the best charge models are useless if protonation states are wrong. Quacpac TK attempts to offer everything necessary to do charges correctly. It includes pKa and tautomer enumeration in order to get correct protonation states, partial charges using multiple models that cover a range of speed and accuracy, and electrostatic potential map construction and storage.

## 1.2 tautomers

When dealing with tautomers there are four primary tasks to be addressed. These include:

- Generating a single representative tautomer suitable for molecular visualization
- Generating a list of tautomers expected to be present in aqueous phase
- Generating a unique (canonical) representation for a set of tautomers
- Generating a substantial list of most possible tautomers suitable for input to further calculations.

Each of these four tasks is covered in a section below. In every case, the tautomerization can be handled alone, but it is generally more useful to handle tautomerization in conjunction with ionization. Each function includes the potential for pKa normalization alongside the tautomer normalization or enumeration.

### 1.2.1 Visualization

While the unique or canonical tautomer generated above is useful for storage in a database, they do not necessarily represent a low-energy tautomer suitable for visualization by modelers and chemists. In order to generate a structure suitable for visualization, we recommend you use the function OEGetReasonableProtomer. This function sets the molecule into a low-energy, neutral-pH, aqueous-phase tautomeric state that should be pleasing for visualization in a scientific setting.

### 1.2.2 Reasonable Tautomer Ensemble

In the course of molecular modeling, it is often desirable to generate a small ensemble of low-energy, neutralpH, aqueous-phase tautomers. The function OEGetReasonableTautomers returns such an ensemble. In order to generate low-energy tautomers reliably, the function works with a form of the molecule that has formal charges removed. By default, each tautomer's ionization state is set to a neutral pH form, but ionization states are not enumerated.

The following depictions show some examples of tautomers that are favored as "reasonable":

• Conversion of carboxylates to diols and nitros to di-hydroxy amines is very unfavorable.

![](_page_9_Figure_5.jpeg)

• Generation of unnecessary, non-dative, formal charges is unfavorable.

![](_page_9_Figure_7.jpeg)

![](_page_10_Figure_1.jpeg)

• Exocyclic bonds adjacent to aromatic rings are accounted for.

![](_page_10_Figure_3.jpeg)

![](_page_10_Figure_4.jpeg)

favored

• Priority is given to aliphatic double bond positions.

![](_page_11_Figure_1.jpeg)

### **1.2.3 Canonicalization**

The OEGet Unique Protomer function is used for canonicalizing the tautomeric forms of a small molecule. Canonicalization converts any of the tautomeric forms of a given molecule into a single unique representation and removes all formal charges that can be appropriately neutralized. This is useful for database registration where alternate representations of tautomeric compounds often leads to duplicate entries in a database.

It is important to remember that a time limit cannot be used to control a canonical process as it might lead to hardware dependent behavior. Thus the identification of a unique protomer can take significant time when the size of the largest contiguous tautomeric atoms approaches or exceeds 30 atoms.

The tautomer returned by  $OEGetUniqueProtoner$  as the "canonical" representation often is not the physiologically preferred form. If a representative form is necessary, please use the functions referred to in the Visualization section above. If an ensemble of biologically relevant tautomers are necessary, please see the functions in the Reasonable Tautomer Ensemble section above.

OEGetUniqueProtomer is not a conformer generation function and will not create coordinates for molecules that are read in with no coordinates. When used on molecules with three-dimensional coordinates, OEGetUniqueProtomer attempts to place hydrogens in a reasonable manner. However, OEGet UniqueProt omer does not modify the heavy-atom coordinates of the molecule. In cases where the change in tautomer-state dictates a change in conformation, one will need to use a conformer-generation tool (such as OMEGA) to generate reasonable conformations for the output from *tautomers*. We recommend that in the preparation of small-molecules for study, charge-state and tautomer enumeration be performed before conformer generation.

### **1.2.4 Complete Enumeration**

The OEEnumerateTautomers function is the core algorithm used to implement all functions listed above. It is useful for enumerating the tautomeric forms of a small molecule. Using the parameters in OETautomerOptions a user can control the behavior of the OEEnumerateTautomers to yield the behavior for their particular application.

It is recommended that before passing a molecule to OEEnumerateTautomers that first any dative bonds are normalized to the hypervalent form using OEHypervalent Normalization and second, formal charges are removed using OERemoveFormalCharge. These two steps improve the tautomers that are returned.

Tautomer generation is a combinatorial process and the time and memory requirements can grow quite rapidly. There are two mechanisms to help a use control this growth. First, the number of tautomers generated and the number of tautomers returned can be controlled with the OETautomerOptions. SetMaxTautomersGenerated and OETautomerOptions. SetMaxTautomersToReturn respectively. Please be aware that if you require that few tautomers be generated, it is possible that no low energy tautomers will be generated. Second, one can limit the time the algorithm spends generating tautomers for each molecule using OETautomerOptions. SetMaxSearchTime.

OEEnumerateTautomers is not a conformer generation function and will not create coordinates for molecules that are read in with no coordinates. When used on molecules with three-dimensional coordinates, OEEnumerateTautomers attempts to place hydrogens in a reasonable manner. However, OEEnumerateTautomers does not modify the heavy-atom coordinates of the molecule. In cases where the change in tautomer-state dictates a change in conformation, one will need to use a conformer-generation tool (such as OMEGA) to generate reasonable conformations for the output from *tautomers*. We recommend that in the preparation of small-molecules for study, charge-state and tautomer enumeration be performed before conformer generation.

## 1.3 pkatyper - Ligand pKa

### 1.3.1 Introduction

Assessment of ligand pKas can be broken into two phases. The first phase is enumeration of the protonation states of interest, and the second phase is assigning a pKa value to each of these states. An intermediate phase of assigning microscopic pKas to each of the atomic-deprotonations may also be considered.

It is common in the course of modeling small-molecules to explore the conformational ensemble of the small molecule. Often structures as high as 5-8 kcal/mol above the aqueous ground-state can be important to biological processes. It is also appropriate to enumerate a protonation-state ensemble of the small molecule.

Similar to tautomers, OpenEye has a solution for enumerating reasonable protonation states, but not for assessing the energetics of the state (e.g. assigning a pKa value). OpenEye's solution for pKa enumeration seeks to enumerate all of the pKa states that fall roughly in the pH range of 2-14 in aqueous solvent. This range of pKa values generates an ensemble that includes the ground-state plus all charge states within 8 kcals/mol  $\Delta G$ . This value was chosen to correspond to the similar range that is often used for generating conformational ensembles of small molecules.

### 1.3.2 Theory

*pkatyper* enumerates charge states based on primary, secondary and tertiary atom types of each atom in a molecule. The primary atom type is based on the atom's group and its valence. The primary atom-type defines the atom's basic propensity to support a formal charge. The secondary atom-type is defined by the atom-type of the neighbors for each atom. These secondary atom-types, such as aromaticity, alpha-beta unsaturation, or electronegative-groups, modulate each atom's basic propensity to support formal charges. The tertiary atom-types assess the effects of nearby formal charges on a given atom's formal charge. The combination of the primary, secondary and tertiary atom-types determine which formal charge states are allowed for each atom in a molecule. The primary and secondary atom-types are determined once, while the tertiary atom-types are determined as part of the enumeration process.

*pkatyper* is a rudimentary approach to pKa prediction. While pkatyper is not suited for prediction of absolute pKas, it is quite amenable to enumeration of all reasonable charge states of a very wide variety of small-molecule chemistries.

*pkatyper* is not a conformer generation program and will not create coordinates for molecules that are read in without coordinates. When used on molecules with three-dimensional coordinates, *pkatyper* attempts to place new hydrogens in a reasonable manner. However, *pkatyper* does not modify the heavy-atom coordinates of the molecule. In cases where the change in protonation-state dictates a change in conformation, one will need to use a conformer-generation tool (such as OMEGA) to generate reasonable conformations for the output from *pkatyper*. We recommend that in preparation of small-molecules for study, charge-state and tautomer enumeration be performed before conformer generation.

In the future, OpenEye will release a product which assigns a pKa value to each of the enumerated states.

## 1.4 *molcharge* - Partial Charges

### 1.4.1 Introduction

The assignment of appropriate atomic partial charges, both to small molecule ligands and to biopolymers (such as proteins and nucleic acids) is essential to getting meaningful results from any electrostatics calculation.

A molecule may be considered a collection of atomic nuclei and the electrons that surround them. The number of protons in each nucleus defines its atomic number/element. If the number of electrons exactly matches the number of protons in these nuclei, the molecule is neutral and has no net charge. If there are more electrons than protons, the molecule has a net negative charge, and if there are less, the molecule has a net positive charge.

It is both the atomic nuclei and the net charge that define the identity of a molecule. Indeed, this is a representation common to quantum chemistry. Adding or removing electrons (or atoms) from a molecule produces a different molecule.

In the discrete world of cheminformatics, valence bond theory allows the electrons present in a system to be represented in terms of bonds with formal bond orders, and formal charges assigned to particular atoms. The sum of the formal charges is equal to the net charge on the molecule, but which atoms are assigned which formal charges can be to some extent arbitrary due to resonance delocalization. In such cases the same molecule may be represented by similar connection tables, but with formal charges assigned to different sets of atoms.

For example, guanidinium may be expressed as either  $N[C+](N)N$  with the formal charge assigned to the carbon, or as  $[NH2+] = C(N)N$  with the formal charge assigned arbitrarily to one of the otherwise equivalent nitrogens. A similar example is a thiocarboxylate group, where either  $C = O[(S-]$  or  $C = S[O-]$  are both equally appropriate representations of the same chemical functionality.

A zwitterion is an electrically neutral molecule that is represented as containing atoms with positive formal charge as well as atoms with negative formal charge.

Perhaps the most important fact to appreciate when considering formal charges on atoms is that they are all artificial constructs by chemists to accommodate a particular chemical model. A figment of a chemist's fevered imagination. Like valence bond theory, they are an exceptionally useful and powerful discretized model of the universe. But as with any model of reality, it has its limitations. Formal charges, for all their numerous benefits to mankind, unfortunately, are not localized on an atom.

The limitations of describing formal charges with valence bond theory is apparent even within cheminformatics. Sydnones, for example, are a class of heterocyclic compound that cannot be written using normal covalent bonds without introducing and arbitrarily assigning both positive and negative charges. Similarly, in inorganic chemistry, the ditechnetium cation,  $Te_2^{+5}$ , causes similar problems where the +5 formal charge cannot be assigned to both technetium atoms without breaking symmetry.

A better model, or approximation, of the wave function describing the distribution of electron density around a molecule is the use of atomic partial charges. A partial charge is a floating-point value assigned to each atomic center intended to model the distribution of electrons over a molecule.

Atomic partial charges are yet another approximation, much like the formal charges described above. However, partial charges provide a much better model to describe the electric field, dipole moment and other observable properties of a molecule.

A common limitation of the use of partial charges is the assumption that they are conformationally invariant. Unfortunately, the distribution of electrons around a molecule depends upon the spatial configuration of its nuclei. Some partial charge assignment algorithms, such as the method of Goddard and Rappé, consider these conformational effects, whilst others that are based on quantum mechanics, such as the RESP and AM1BCC methods of Bayly et al., go to great lengths to eliminate conformational effects, for example, by restraining and symmetrizing symmetric atom positions. This is necessary in order to be able to properly handle multiple conformations and changes in geometry (e.g. geometry optimization) with a single set of atomic charges.

### 1.4.2 Theory

#### **Marsili-Gasteiger Partial Charges**

Marsili-Gasteiger partial charges are assigned using a two stage algorithm. In the first stage, seed charges are assigned to each atom in the molecule. For example, carboxylate oxygens are each assigned the value -0.5. During the second stage, these initial charges are then shared across bonds, moving a certain amount of charge from one atom to another. The partial charge moved and its direction is determined by difference in electronegativities of the atoms on each end of the bond. The relaxation algorithm is then iterated several times (by default eight passes), attenuating the charge moved with each iteration. OpenEye does not recommend use of this charge model for intermolecular interactions; it was never intended for this purpose. The author of the method (Johann Gasteiger) developed it to compare relative reactivity of related organic chemical functional groups within different molecular contexts. Here it is included for comparison purposes.

#### **MMFF94 Partial Charges**

The partial charges used by the MMFF94 and MMFF94s force fields are assigned using a four stage algorithm. In the first stage, each atom of the molecule is assigned an MMFF94 atom type. In the second stage, an initial seed partial charge is assigned to each atom based upon its atom type. For a few atom types, the initial partial charge also depends upon the local environment. In the third stage, the initial charges assigned to aromatic rings are shared between all atoms of the aromatic ring. Finally, in the fourth stage, a table of bond charge increments (BCI) is used to move charges across bonds based upon the bond type of the bond (single, double, triple) and the atom types of the atoms at each end. Developed for the electrostatic interactions within the above-mentioned force fields, they are the appropriate charges to use with these force fields most notably for intramolecular interactions of pharmaceutical and bio-organic small molecules. They are less well-suited (but still passable) for intermolecular interactions using the common two-body additive Coulomb interactions as used in Amber, Charmm, Gromacs. For these better choices would be amber99sb charges on proteins and peptides, and am1bccsym charges on the ligand.

#### **AM1 Charges**

AM1 charges are a set of Mulliken-type charges derived from a semi-empirical quantum-mechanical calculation. For further discussion of this method, please see [Dewar-1985]. These should not be used for intermolecular interactions of force fields.

#### **AM1BCC Charges**

AM1BCC charges start with Mulliken-type partial charges derived from the AM1 semi-empirical quantum mechanical (QM) wave-function. In a second stage, bond-charge corrections (BCCs) are applied to the partial charges on each atom to generate new partial charges. Many different variants of AM1BCC charges are offered within our API because of the significant influences of several different factors on these QM-derived charges. Specifically, these factors are

- Optimization: whether or not the input geometry is optimized. QM wavefunctions in general are quite sensitive to geometry, especially bond lengths and bond angles, so this can markedly affect the partial charges. In general, optimizing the geometry is recommended. To avoid a collapse of the conformation due to strong intramolecular electrostatic interactions, light restraints to the starting geometry are applied.
- Symmetrization: whether or not topologically similar atoms (for example the two oxygens on a carboxylate) are constrained to have identical values. The true QM wavefunction is usually asymmetric around topologically similar atoms, leading to asymmetric partial charges. However, if the same partial charges are to be used on

different conformers (as with general fixed-charge force fields) it is important that these charges be symmetrized or else interconverting between formally degenerate conformers (e.g. 180 degree rotation of the carboxylate) will have non-degenerate electrostatic energies. In general, if the partial charges are to be applied to more than the single conformer used to generate them, symmetrization is strongly recommended.

Another important issue with AM1BCC charges is if highly conformer-specific charges are generated which are unsuitable for other conformers, leading to undesirable perturbed electrostatic energies for those other conformers. To address this problem, we strongly recommend the ELF conformer selection protocol described below.

"Standard" AM1BCC includes both optimization and symmetrization.

OpenEye considers AM1BCC charges to be the best partial charge model currently available. For further discussion, please see the work of Christopher I. Bayly.

### **ELF Conformer Selection**

ELF conformer selection is a method to select one or more conformers having Electrostatically Least-interacting Functional groups (ELF) from a large conformer database. The purpose of this method is to resolve important issues with QM-derived charges in general, including AM1BCC charges. The issue is that strong short-range intramolecular polarizations specific to a certain conformation, as with an intramolecular hydrogen bond or salt bridge, usually leads to strongly perturbed partial charges for the atoms involved. These charges can be very different from those found for other conformers which do not have that intramolecular polar interaction. If such partial charges are applied to all conformers, some of those other conformers are very likely to have wrongly over-stabilized solvation energies.

A second problem arising from this issue is the precision or sensitivity of the electrostatic energies resulting from QM-derived charges. By this we mean the variance in electrostatic relative energies between different conformers depending on what conformer is used for the QM-derived charges. Imagine two different sets of QM-derived partial charges for a molecule, each coming from a conformer having different strong intramolecular hydrogen bonds. Each set of partial charges will have strongly perturbed partial charges for the internally hydrogen bonded atoms, but they will be different. The relative energies between conformers will be different depending which partial charge set is used.

For these reasons it is important to avoid generating QM-derived partial charges from a conformer having electrostatically strongly interacting functional groups. This is what ELF conformer selection does.

ELF needs to start with enough conformers so that it can find a population of conformers that do not have stronglyinteracting functional groups. In the first stage, the Coulomb electrostatic energy is calculated for every conformer using the absolute value of the MMFF94 partial charges (original negative charges are replaced with their absolute values). The electrostatic energies with such charges destabilize all strong polar interactions, and thus the lowest electrostatic energies correspond to the Electrostatically Least-interacting Functional groups. The lowest-energy 2% of conformers is selected as the 2% ELF population. We find that averaging 10 diverse conformers from the 2% ELF population is sufficient to provide a well-behaved set of QM-derived partial charges even for highly polar and charged molecules.

#### Amber ff94, ff96, ff99, ff99sb, and ff99sbc0 Partial Charges

The partial charges used by the AmberFF94 force field are based on fitting quantum mechanical electrostatic potentials (esp). They were developed to address two key issues with earlier esp-fit charge sets: unrealistically high charges on charge centers and the variation of atomic charges with conformation. While the latter should have some basis in electronic structure, numerical instability in the charge fitting process was the source of both these pathologies. AmberFF94 charge sets use restrained esp-fitting (RESP) to control the numerical instabilities and simultaneous multiconformer fitting to lead to conformation-independent charges that are restricted to individual residues. Particular attention was given to ensure that backbone amides have consistent charges. The Amber force fields ff94, ff96, ff99, ff99sb, and ff99sbc0 all use the same set of RESP charges, they differ in other terms (mostly torsional).

## 1.5 Wiberg bond orders

### 1.5.1 Theory

The concept of bond order has been proposed by Wiberg [Wiberg-1966] as a calculated bond property using orthonormalized atomic orbitals which are a basis set for semi-empirical molecular orbitals. Originally it was formulated for the CNDO basis set, but it might be extended to AM1 or PM3 methods. Wiberg bond order is a measure of electron population overlap between two atoms:

$$
W_{AB}=\sum_{\mu\in A}\sum_{\nu\in B}P_{\mu\nu}^2
$$

where summation is over atomic orbitals  $\mu$  on atom A and atomic orbitals  $\nu$  on atom B, and  $P_{\mu\nu}$  is the corresponding density matrix element. For non-bonded pairs of atoms in a molecule,  $W_{AB}$  is very low but always nonzero.

#### See also:

· OEAM1Results. GetBondOrder method

### **CHAPTER**

## **TWO**

## **EXAMPLES**

## 2.1 Quacpac TK Examples

The following table lists the currently available Quacpac TK examples:

| Program                              | Description                                                                                          |
|--------------------------------------|------------------------------------------------------------------------------------------------------|
| assigncharges                        | assigning charges                                                                                    |
| neutralionization                    | setting a neutral ionization state                                                                   |
| enumeratetautomers                   | enumerating tautomers                                                                                |
| setreasonablechargestate             | setting a reasonable charge state                                                                    |
| wibergbondorders                     | obtaining Wiberg bond orders                                                                         |
| applychargesoedu                     | Apply Charges to OEDesignUnit                                                                        |
| enumerateionizationstatesatneutralph | Enumerate ionization states at neutral pH using OEMultistatepKaModel and OEMultistatepKaModelOptions |

#### **Examples:**

### 2.1.1 Assigning Charges

The following code example shows how to use the assign partial charges. The program reads all of the molecules in the input file, assigns partial charges to each based on the selected method (the default is -method mmff94) and writes each charged molecule to the output file.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python assigncharges.py --help
```

#### will generate the following output:

```
Simple parameter list
Charging options
  -method : which set of charges to apply
input/output options
  -in : Input molecule
  -out : Output molecule (usually an oeb)
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
import sys
from openeye import oechem
from openeye import oequacpac
def AssignChargesByName(mol, name):
    if name == "noop":
        return oequacpac.OEAssignCharges(mol, oequacpac.OEChargeEngineNoOp())
   elif name == "mmff" or name == "mmf94":
        return oequacpac. OEAssignCharges(mol, oequacpac. OEMMFF94Charges())
    \text{elif} name == "amlbcc":
        return oequacpac. OEAssignCharges (mol, oequacpac. OEAM1BCCCharges ())
    \text{elif} name == "amlbccnosymspt":
        optimize = Truesymmetrize = Truereturn oequacpac. OEAssignCharges (mol,
                                           oequacpac. OEAM1BCCCharges (not optimize, not
\rightarrowsymmetrize))
    elif name == "amber" or name == "amberff94":
        return oequacpac.OEAssignCharges(mol, oequacpac.OEAmberFF94Charges())
    elif name == "amlbccelf10":
        return oequacpac.OEAssignCharges(mol, oequacpac.OEAM1BCCELF10Charges())
    return False
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
   itf = oechem. OEInterface (InterfaceData)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
    ifs = oechem.oemolistream()
    inputFile = itf.GetString("-in")if not ifs.open(inputFile):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % inputFile)
```

```
(continued from previous page)
```

```
ofs = oechem.oemolostream()
   outFile = itf.GetString("-out")
   if not ofs.open(outFile):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" % outFile)
   charqeName = itf.GetString("-method")
   mol = occhem.OEMol()while oechem. OEReadMolecule(ifs, mol):
       if not AssignChargesByName(mol, chargeName):
           oechem. OEThrow. Warning ("Unable to assign %s charges to mol %s"
                                 % (chargeName, mol. GetTitle()))
       oechem.OEWriteMolecule(ofs, mol)
   ifs.close()
   ofs.close()
#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF AssignCharges.py [-options] <inmol> [<outmol>]
!CATEGORY "input/output options :"
  !PARAMETER -in
     !ALIAS -i
     !TYPE string
     !BRIEF Input molecule
     !VISIBILITY simple
     !REQUIRED true
     !KEYLESS 1
  ! END
  !PARAMETER -out
     !ALIAS -0
     !TYPE string
     !DEFAULT oeassigncharges.oeb.gz
     !BRIEF Output molecule (usually an oeb)
     !VISIBILITY simple
     !REOUIRED false
     !KEYLESS 2
  LEND
!END
!CATEGORY "Charging options :"
  !PARAMETER -method
     !TYPE string
     !LEGAL_VALUE noop
     !LEGAL_VALUE mmff
     !LEGAL VALUE mmff94
     !LEGAL VALUE am1bcc
     !LEGAL_VALUE am1bccnosymspt
     !LEGAL VALUE amber
```

```
!LEGAL VALUE amberff94
      !LEGAL_VALUE am1bccelf10
      !DEFAULT mmff94
      !BRIEF which set of charges to apply
      !SIMPLE true
      !REQUIRED false
   ! END
!END
1 - 1 - 1if _name_ == "_main_":
    sys.exit(main(sys.argv))
```

See also:

• OEAssignCharges function

### 2.1.2 Setting a Neutral Ionization State

This following example shows how to set a single dominant ionization state of a molecule at pH 7.4.

#### **Command Line Interface**

A description of the command line interface is shown as follows:

prompt> python neutralionization.py <mol-infile> <mol-outfile>

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
import sys
from openeye import oechem
from openeye import oequacpac
```

```
def main(arqv=[ name ]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <mol-infile> <mol-outfile>" % argv[0])
    if s = oechem. oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
    ofs = oechem. oemolostream()if not ofs.open(arg[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % argv[2])
   mol = occhem.OEGraphMol()while oechem. OEReadMolecule(ifs, mol):
        if oequacpac.OESetNeutralpHModel(mol):
            oechem.OEWriteMolecule(ofs, mol)
        else:
            msq = ("Unable to set a neutral pH model for molecule: %s"
                   % mol.GetTile())
            oechem.OEThrow.Warning(msq)
    return 0
if
   {\sf name} = " {\sf main} \sys.exit(main(sys.argv))
```

See also:

• OESetNeutralpHModel function

### **2.1.3 Enumerating Tautomers**

This following example shows a fast informatics technique using tautomer enumeration which is capped at 200 states per molecule. Formal charge of each input molecule is removed first, and then tautomers are enumerated. The tautomers are saved to the output file after setting a favorable ionization state at neutral pH.

#### **Command Line Interface**

A description of the command line interface is shown as follows:

prompt> python getreasonabletautomers.py <mol-infile> <mol-outfile>

Code

```
#!/usr/bin/env python
# (C) 2022 Cadence Design Systems, Inc. (Cadence)
# All rights reserved.
# TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is
# provided to current licensees or subscribers of Cadence products or
# SaaS offerings (each a "Customer").
# Customer is hereby permitted to use, copy, and modify the Sample Code,
```

```
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
from openeye import oequacpac
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <mol-infile> <mol-outfile>" % argv[0])
    if s = oechem.oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
    ofs = occhem.oemolostream()if not ofs.open(argV[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % argv[2])
    tautomerOptions = oequacpac.OETautomerOptions()
    pKaNorm = True
    for mol in ifs. GetOEGraphMols():
        for tautomer in oequacpac. OEGetReasonableTautomers (mol, tautomerOptions,
\rightarrowpKaNorm):
            oechem.OEWriteMolecule(ofs, tautomer)
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

#### See also:

· OEGetReasonableTautomers function

### 2.1.4 Setting a Reasonable Charge State

The following example shows how to use OEGetReasonableProtomer to set a favorable ionization state assuming  $pH=7.4$ .

#### **Command Line Interface**

A description of the command line interface is shown as follows:

prompt> python setreasonablechargestate.py <mol-infile> <mol-outfile>

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
import sys
from openeye import oechem
from openeye import oequacpac
def main(argv=[__name__]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <mol-infile> <mol-outfile>" % argv[0])
    ifs = oechem.oemolistream()
    if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   ofs = occhem.oemolostream()if not ofs.open(argv[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % argv[2])
    for mol in ifs. GetOEGraphMols():
        oequacpac.OEGetReasonableProtomer(mol)
        oechem.OEWriteMolecule(ofs, mol)
    return <sub>0</sub>
```

```
if __name__ == "__main__".sys.exit(main(sys.argv))
```

#### See also:

• OEGet ReasonableProtomer function

### 2.1.5 Obtaining Wiberg bond orders

The following example shows how to obtain the Wiberg bond orders from an AM1 calculation.

#### **Command Line Interface**

A description of the command line interface is shown as follows:

```
prompt> python wibergbondorders.py <mol-infile>
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
from openeye import oechem
from openeye import oequacpac
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) != 2:
        oechem.OEThrow.Usage("%s <infile>" % argv[0])
    ifs = oechem.oemolistream(sys.argv[1])am1 = oequacpac. OEAM1()results = oequacpac.OEAM1Results()
    for mol in ifs. GetOEMols():
        for conf in mol. GetConfs():
            print ("molecule: ", mol. GetTitle(), "conformer:", conf. GetIdx())
            if aml.CalcAM1 (results, mol) :
```

```
nhonds = 0for bond in mol. GetBonds (oechem. OEIsRotor ()) :
                      nhonds += 1print (results.GetBondOrder(bond.GetBgnIdx(), bond.GetEndIdx()))
                 print ("Rotatable bonds: ", nbonds)
if _name_ == " _main
                          \mathcal{M}_{\mathcal{M}}import sys
    sys.exit(main(sys.argv))
```

See also:

· OEAM1Results.GetBondOrder method

### 2.1.6 Applying Charges to OEDesignUnit

The following code example shows how to use the apply charges to an OEDesignUnit. The program reads an OEDesignUnit as the input file, apply charges to to it and writes new OEDesignUnit to specified output file.

#### **Command Line Interface**

A description of the command line interface is as following.

```
prompt> python applycharges_oedu.py [<oedu infile>] [<oedu outfile>]
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
# This program demonstrates how to apply charges to an OEDesignUnit.
#######################################
import sys
from openeye import oechem
```

```
from openeye import oequacpac
def main(argv=[_name_]):
    opts = oechem.OESimpleAppOptions("applycharges_du", oechem.OEFileStringType_DU,
                                      oechem.OEFileStringType_DU)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0if s = oechem.oeifstream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oeofstream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   du = oechem. 0EDesignUnit()while oechem. OEReadDesignUnit(ifs, du):
        charge\_engine = oequacpac. 0EDesignUnitCharges()if charge_engine.ApplyCharges(du):
            oechem.OEWriteDesignUnit(ofs, du)
        Also:oechem.OEThrow.Warning("%s: %s" % (du.GetTitle(), "Failed to assign
\rightarrowcharges"))
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

#### See also:

- OEDesignUnitCharges class
- OEDesignUnit class

### 2.1.7 Enumerate ionization states at neutral pH using OEMultistatepKaModel and **OEMultistatepKaModelOptions**

The following code example shows how to use OEMultistatepKaModel and OEMultistatepKaModelOptions classes to enumerate ionization states at neutral pH. The program reads an input molecules file, create an instance of OEMultistatepKaModelOptions class. Use it in OEMultistatepKaModel class object and writes generated ionization states at neutral pH to specified output file.

#### **Command Line Interface**

A description of the command line interface is as following.

prompt> python enumerateionizationstatesatneutralph.py [<oedu infile>] [<oedu outfile>  $\rightarrow$  1

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
import sys
from openeye import oechem
from openeye import oequacpac
def main(argv=[__name__]):
   if len(argv) != 3:
        oechem.OEThrow.Usage("%s <mol-infile> <mol-outfile>" % argv[0])
    if s = oechem.oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   ofs = occhem.oemolostream()if not ofs.open(argv[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % argv[2])
   logfs = oechem.oeofstream("enumerateionizationstatesatneutralph.log")
    # oechem. OEThrow. SetLevel (oechem. OEErrorLevel_Verbose)
    # oechem.OEThrow.SetLevel(oechem.OEErrorLevel_Info)
   oechem.OEThrow.SetLevel(oechem.OEErrorLevel_Warning)
   oechem.OEThrow.SetOutputStream(logfs)
   mol = occhem. OEGraphMol()while oechem. OEReadMolecule(ifs, mol):
        title = mol.GetTitle()opts = oequacpac.OEMultistatepKaModelOptions()
        # opts. SetMaxNumMicrostates (128)
```

```
multistatepka = oequacpac.OEMultistatepKaModel(mol, opts)
        if (multistatepka.GenerateMicrostates()):
           for a in multistatepka. GetMicrostates():
                a.SetTitle(title)
                oechem.OEWriteMolecule(ofs, a)
                ofs.flush()
        else:
           msg = ("No microstates are generated for molecule: %s"
                  % title)
            oechem.OEThrow.Warning(msg)
           oechem.OEWriteMolecule(ofs, mol)
           ofs.flush()
    return 0
if _name == " main ":
    sys.exit(main(sys.argv))
```

See also:

- OEMultistatepKaModelOptions class
- OEMultistatepKaModel class

### **CHAPTER**

## **THREE**

**API** 

## **3.1 OEProton Classes**

### 3.1.1 OEAM1BCCCharges

class OEAM1BCCCharges : public OEChargeEngineBase

Charge engine input to OEAssignCharges to assign AM1 Mulliken-type partial charges with bond-charge corrections.

The input must be a 3D molecule with a number of atoms no larger than a defined maximum. The default is 300 atoms, see constructors. Parameters must be available for each atom and bond type. If permissive BCCs are requested, no correction is applied when a BCC is missing.

The following methods are publicly inherited from OEChargeEngineBase:

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

### **Constructors**

```
OEAM1BCCCharges (bool optimize=true,
                bool symmetrize=true,
                bool permissiveBCCs=false,
                unsigned maxAtoms = 300)
```

Constructor. Parameters also have getter and setter methods.

#### **GetOptimize**

|--|

Returns true if the geometry of the input molecule will be optimized during charge assignment.

#### **GetPermissiveBCCs**

bool GetPermissiveBCCs() const

Returns true if a missing BCC will be treated as a correction of zero rather than an error.

#### **GetSizeLimit**

unsigned GetSizeLimit() const

Returns the maximum number of atoms permitted.

#### **GetSymmetrize**

bool GetSymmetrize() const

Returns true if charges will be symmetrized with respect to bond-topologically equivalent atoms.

#### **SetOptimize**

void SetOptimize (bool optimize=true)

Defines whether the geometry of the input molecule will be optimized during charge assignment. Optimization is lightly restrained to starting coordinates.

#### **SetPermissiveBCCs**

void SetPermissiveBCCs (bool permissive=true)

Defines whether a missing BCC will be treated as a correction of zero or as an error.

#### **SetSizeLimit**

void SetSizeLimit (unsigned maxAtoms)

Defines the maximum number of atoms permitted in the input molecule.

#### **SetSymmetrize**

void SetSymmetrize (bool symmetrize=true)

Defines whether charges on the molecule are symmetrized with respect to bond-topologically equivalent atoms.

### 3.1.2 OEAM1BCCELF10Charges

class OEAM1BCCELF10Charges : public OEELFCharges

Charge engine input to OEAssignCharges to assign AM1 Mulliken-type partial charges with bond-charge corrections using the electrostatically least-interacting functional group (ELF) technique.

The input must be a 3D multi-conformer molecule with a number of atoms no larger than the default AM1BCC maximum. AM1BCC parameters must be available for each atom and bond type.

Equivalent to:

OEELFCharges (OEAM1BCCCharges (), 10)

The following methods are publicly inherited from OEELFCharges:

| GetLimit | GetPercentage          | SetPercentage          |
|----------|------------------------|------------------------|
| SetLimit | GetReturnSelectedConfs | SetReturnSelectedConfs |

The following methods are publicly inherited from OEChargeEngineBase:

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

#### **Constructors**

```
OEAM1BCCELF10Charges()
OEAM1BCCELF10Charges (const OEAM1BCCELF10Charges & rhs)
```

Constructor. There are no options for this charge engine.

### 3.1.3 OEAM1Charges

class OEAM1Charges : public OEChargeEngineBase

Charge engine input to OEAssignCharges to assign AM1 Mulliken-type partial charges.

The input must be a 3D molecule with a number of atoms no larger than a defined maximum. The default is 300 atoms, see constructors. AM1 parameters must be available for each atom type.

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

OEAM1Charges (bool optimize=true, bool symmetrize=false, unsigned maxAtoms=300)

Constructor. Parameters also have getter and setter methods.

#### **GetOptimize**

bool GetOptimize() const

Returns true if the geometry of the input molecule will be optimized during charge assignment.

#### **GetSizeLimit**

unsigned GetSizeLimit() const

Returns the maximum number of atoms permitted.

#### **GetSymmetrize**

bool GetSymmetrize() const

Returns true if charges will be symmetrized with respect to bond-topologically equivalent atoms.

#### **SetOptimize**

void SetOptimize(bool optimize=true)

Defines whether the geometry of the input molecule will be optimized during charge assignment. Optimization is lightly restrained to starting coordinates.

#### **SetSizeLimit**

void SetSizeLimit (unsigned maxAtoms)

Defines the maximum number of atoms permitted in the input molecule.

#### **SetSymmetrize**

void SetSymmetrize (bool symmetrize=true)

Defines whether charges on the molecule are symmetrized with respect to bond-topologically equivalent atoms.

### 3.1.4 OEAmberFF94Charges

class OEAmberFF94Charges : public OEChargeEngineBase

Charge engine input to OEAssignCharges to assign Amber force field 94 atomic partial charges to standard amino acids.

The input molecule must have explicit hydrogens and consist of only standard Amber amino acids. Residues must be perceived or repairs permitted. The amino acid name may be altered to match the Amber naming scheme, such as HIP for a protonated histidine. Currently OpenEye supports the following Amber amino acids: ACE, ALA, ARG, ASH, ASN, ASP, CIM, CIP, CYM, CYS, CYX, GLH, GLN, GLU, GLY, HID, HIE, HIP, HIS, HOH, ILE, LEU, LYN, LYS, MET, NHE, NME, PHE, PRO, SER, THR, TRP, TYR, VAL. Amber charges are graph-based and do not require 3D coordinates.

The following methods are publicly inherited from OEChargeEngineBase:

| $operator!=$      | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| $operator==$      | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

#### **Constructors**

```
OEAmberFF94Charges()
```

Constructor. There are no options for this charge engine.

### 3.1.5 OEChargeEngineBase

#### class OEChargeEngineBase

This is the abstract base class for all charge engines, containing methods used by the function  $OEAssignCharges$ .

The following charge engine classes derive from this base class:

- OEAM1BCCCharges
- OEAM1BCCELF10Charges
- OEAM1Charges
- OEAmberFF94Charges
- OEChargeEngineNoOp
- OEClearCharges

- OECombineChargeEngines
- OEDesignUnitCharges
- OEELFCharges
- OEFormalToPartialCharges
- OEGasteigerCharges
- OEInitialCharges
- OEMMFF94Charges

#### operator!=

bool operator!=(const OEChargeEngineBase &rhs) const

Returns true if the charge engines are *not* equivalent.

#### operator==

bool operator == (const OEChargeEngineBase & rhs) const

Returns true if the charge engines are equivalent (the same class with the same parameters).

#### **CheckCharges**

```
bool CheckCharges (const OEChem:: OEMolBase & mol) const
bool CheckCharges (const OEChem:: OEMCMolBase &mcMol) const
bool CheckCharges (const OEBio:: OEDesignUnit &du) const
```

Used by  $OEAssignCharges$  to determine if the charges on the molecule are as expected.

#### **CreateCopy**

OEChargeEngineBase \*CreateCopy() const =0

Deep copy of the charge engine.

#### **GetExpectValidMol**

bool GetExpectValidMol() const

Returns true if an input molecule must be valid before OEAssignCharges attempts to assign charges.

#### **GetName**

std::string GetName() const

Returns the name of the charge engine.

#### **GetRepairRequestedHint**

bool GetRepairRequestedHint() const

Returns true if OEAssignCharges is requested to repair the input molecule before assigning charges. Examples of repairing a molecule include adding explicit hydrogens and perceiving residues.

#### **GetRequirements**

unsigned GetRequirements () const

Returns a bit mask used by OEAssignCharges describing aspects of the input molecule required for this charging method. Examples include 3D coordinates, explicit hydrogens, and PDB order.

#### **IsValid**

```
bool IsValid (OEChem:: OEMolBase &mol) const
bool IsValid (OEChem:: OEMCMolBase & mcMol) const
bool IsValid (OEBio:: OEDesignUnit &du) const
bool IsValid (const OEChem:: OEMolBase & mol) const = 0
bool IsValid (const OEChem:: OEMCMolBase &mcMol) const
bool IsValid (const OEBio:: OEDesignUnit &du) const
```

Returns true if the input molecule appears to be valid for use with this method.

#### **SetExpectValidMol**

void SetExpectValidMol(bool expect=true)

Defines whether an input molecule must be valid before  $OEAssignCharges$  attempts to assign charges. If set to false and the molecule is not valid, then OEAssignCharges attempt to charge the molecule anyway.

#### **SetRepairRequestedHint**

void SetRepairRequestedHint (bool repair=true)

Define whether OEAssignCharges is requested to repair the input molecule before assigning charges. Examples of repairing a molecule include adding explicit hydrogens and perceiving residues. If set to false and the molecule requires repairs, then OEAssignCharges will fail and return false.

#### **TransferCharge**

```
bool TransferCharge (OEChem:: OEAtomBase *dstAtom,
                    const OEChem:: OEAtomBase *srcAtom) const
```

If OEAssignCharges must make a copy of the input molecule before charges can be applied, this method is used to transfer charges back to the input molecule.

## 3.1.6 OEChargeEngineNoOp

```
class OEChargeEngineNoOp : public OEChargeEngineBase
```

Charge engine input to  $OEAssignCharges$  that does nothing to the input molecule, any existing charges are left untouched.

This charge engine can be used with any type of molecule.

Can be used as a pre-charging method for OECombineChargeEngines.

The following methods are publicly inherited from OEChargeEngineBase:

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

#### **Constructors**

| OEChargeEngineNoOp() |
|----------------------|
|                      |
|                      |

Constructor. There are no options for this charge engine.

## 3.1.7 OEClearCharges

```
class OEClearCharges : public OEChargeEngineBase
```

Charge engine input to  $OEAssignCharges$  to set partial charges on all atoms to zero. This charge engine is graphbased and does not require 3D coordinates.

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

OEClearCharges()

Constructor. There are no options for this charge engine.

## 3.1.8 OECombineChargeEngines

```
class OECombineChargeEngines : public OEChargeEngineBase
```

Charge engine input to OEAssignCharges that combines two user-specified charge engines into one. This is useful when the first charge engine is used to pre-charge a molecule and the second to adjust the charges. This allows more complicated charging schemes to be easily constructed.

The input molecule must conform to the requirements of the specified charge engines.

The following methods are publicly inherited from OEChargeEngineBase:

| $operator!=$      | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| $operator==$      | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

#### **Constructors**

```
OECombineChargeEngines (const OECombineChargeEngines &rhs)
OECombineChargeEngines (const OEChargeEngineBase &preChargeEngine,
                       const OEChargeEngineBase &adjustmentEngine)
```

Constructors. The preChargeEngine is expected to set initial charges while the adjustmentEngine is expected to modify those charges.

## 3.1.9 OEDesignUnitCharges

Attention: This API is currently available in C++ and Python.

class OEDesignUnitCharges : public OEChargeEngineBase

This charge engine charges each component in the OEDesignUnit. The various components can be charged with different charging engines, and the default behavior is to do exactly that. The default behavior is for the protein engine to use OEAmberFF94Charges for the standard protein residues. It uses OEAM1BCCCharges for nonstandard residues. The nucleic acid component uses the OEMMFF94Charges charges. The ligand and or any other heterogen in the system (e.g.g cofactors), are charged using OEAM1BCCCharges. The solvent uses OEAmberFF94Charges, but by default uses the the SZMAP water model, in which case it assigns the charges to match those described in The Szmap TK Standard Water Model. This is an option that can be turned off. Excipients is by default charged using the OEMMFF94Charges engine. The radii assignedis OERadiiType\_BondiVdw, except in cases where AM1 charges have been used, in which case the radii is of the OERadiiType\_Zap9 type. Metals in the system (often in cofactors or otherCofactors) are initially charged with the OEFormalToPartialCharges engine, and in the last step of the calculation, the metal charges are spread in the system using the OESpreadMetalCharges as part of the finalization stage. Counter ions are charged with the same metal charge engine, but are not subsequently spread. The fall back engine is the same for all components; in case an engine fails, the method will try to charge a component with the fall back engine, which by default is OEMMFF94Charges.

Note: Currently, there is a hard limit of 100 atoms for molecules being charged with the OEAM1BCCCharges charging engine.

**Warning:** It is currently not possible to use OEAM1BCCELF10Charges for the ligand, cofactors, or other components. The method requires passing a conformer ensemble of the molecule to charge, which is currently not possible with an OEDesignUnit. If a user tries to use this type of charging engine, it will be downgraded to AM1BCC with a warning. Since the OEAM1BCCELF10Charges is recommended for the molecular dynamics type of simulations, we recommend charging the ligand independently and updating it in the DesignUnit using OEUpdateDesignUnit.

The following methods are publicly inherited from OEChargeEngineBase:

| operator!=             | GetExpectValidMol | SetExpectValidMol      |
|------------------------|-------------------|------------------------|
| operator==             | GetName           | SetRepairRequestedHint |
| GetRepairRequestedHint | TransferCharge    |                        |
| CheckCharges           | GetRequirements   |                        |
| CreateCopy             | IsValid           |                        |

#### **Constructors**

```
OEDesignUnitCharges()
OEDesignUnitCharges (const OEDesignUnitCharges & rhs)
```

Default and copy constructors.

#### operator=

OEDesignUnitCharges & operator= (const OEDesignUnitCharges & rhs)

Assignment operator.

#### **ApplyCharges**

**bool** ApplyCharges (OEBio:: OEDesignUnit & du) const

Returns the boolean whether or not charges are able to be applied to the input OEDesignUnit argument  $(du)$ .

#### **CreateCopy**

OEChargeEngineBase \*CreateCopy() const

Creates a copy of the charge engine class. This class does not own the returned memory.

#### **IsValid**

```
bool IsValid (const OEChem:: OEMolBase &mol) const
bool IsValid (const OEBio:: OEDesignUnit &du) const
```

Returns the boolean whether or not the input OEMolBase or OEDesignUnit can be assigned partial charges from the charging engine.

#### **SetCoFactorChargeEngine**

void SetCoFactorChargeEngine(const OEChargeEngineBase & chargeEngine)

Sets the charge engine for the OEDesignUnitComponents\_Cofactors molecular component.

#### SetFallbackChargeEngine

void SetFallbackChargeEngine (const OEChargeEngineBase & chargeEngine)

Sets a backup charge engine for any molecular component where the charge engine cannot be applied.

#### **SetFinalizationChargeEngine**

**void** SetFinalizationChargeEngine (const OEChargeEngineBase & chargeEngine)

#### SetLigandChargeEngine

void SetLigandChargeEngine (const OEChargeEngineBase & chargeEngine)

Sets the charge engine for the OEDesignUnitComponents\_Ligand molecular component.

#### SetMetalChargeEngine

**void** SetMetalChargeEngine (const OEChargeEngineBase & chargeEngine)

**Sets** both OEDesignUnitComponents\_Metals the charge engine for the and OEDesignUnitComponents\_CounterIons molecular components.

#### **SetNucleicChargeEngine**

void SetNucleicChargeEngine (const OEChargeEngineBase & chargeEngine)

Sets the charge engine for the OEDesignUnitComponents\_Nucleic molecular component.

#### SetOtherChargeEngine

void SetOtherChargeEngine (const OEChargeEngineBase & chargeEngine)

#### **SetProteinChargeEngine**

void SetProteinChargeEngine (const OEChargeEngineBase & chargeEngine)

Sets the charge engine for the OEDesignUnitComponents\_Protein molecular component.

#### SetProteinNonStandardChargeEngine

void SetProteinNonStandardChargeEngine (const OEChargeEngineBase & chargeEngine)

Sets the charge engine for any nonstandard amino acids in the OEDesignUnitComponents\_Protein molecular component.

#### **SetSolventChargeEngine**

void SetSolventChargeEngine (const OEChargeEngineBase & chargeEngine)

Sets the charge engine for any solvent molecules in the OEDesignUnitComponents\_Solvent molecular component.

#### **TransferCharge**

```
bool TransferCharge (OEChem:: OEAtomBase *dstAtom,
                     const OEChem:: OEAtomBase *srcAtom) const
```

Returns the boolean whether or not the transfer of charges from the source atom (srcAtom) to the destination atom (dstAtom) was successful.

#### **UseSZMAPWaterModel**

void UseSZMAPWaterModel (const bool value)

Sets the boolean of whether or not to use the Szmap water model within the context of charging the system (see Introduction for more information about the water model itself).

### 3.1.10 OEELF

#### class OEELF

This class defines an interface to select conformers from a given ensemble, using the electrostatically least-interacting functional group (ELF) technique.

#### The OEELF class defines the following public methods:

• Select

#### **Constructors**

```
OEELF (const OEELFOptions& opts = OEELFOptions () )
OEELF (const OEELF&)
```

Default and copy constructors.

#### operator=

OEELF & operator=(const OEELF &)

The assignment operator.

#### **Select**

```
bool Select (OEChem:: OEMCMolBase& mol) const
```

Selects the desired ELF population. Method discards the unwanted conformers in the input molecule.

### 3.1.11 OEELFCharges

class OEELFCharges : public OEChargeEngineBase

Charge engine input to  $OEAssigma$  on  $Charges$  to assign charges with the user-specified charge engine using the electrostatically least-interacting functional group (ELF) technique.

The input must be a 3D multi-conformer molecule and conform to the requirements of the specified charge engine. Graph-based charge engines are not appropriate for use with ELF because they do not take 3D conformation into account.

The following methods are publicly inherited from OEChargeEngineBase:

| $operator!=$      | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| $operator==$      | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

The following classes derive from this class:

• OEAM1BCCELF10Charges

```
OEELFCharges (const OEELFCharges & rhs)
OEELFCharges (const OEChargeEngineBase & chargeEngine,
             unsigned limit=10,
             double percentage=2.0,
             bool selectedConfs=false)
```

Constructor. Parameters also have getter and setter methods.

#### **GetLimit**

```
unsigned GetLimit() const
```

Returns the number of diverse conformers to select from the least interacting conformers set.

#### **GetPercentage**

double GetPercentage() const

Returns the percentage of input conformers to select as the electrostatically least-interacting set.

#### **GetReturnSelectedConfs**

bool GetReturnSelectedConfs() const

Returns true if just the selected diverse conformers will be returned. Otherwise all the original conformers are returned.

#### **SetLimit**

void SetLimit (unsigned limit)

Sets the number of diverse conformers to select from the least interacting conformers set in the second step of the ELF algorithm.

#### **SetPercentage**

void SetPercentage (double pct)

Sets the percentage of input conformers to select as the electrostatically least-interacting set in the first step of the ELF algorithm.

### **SetReturnSelectedConfs**

void SetReturnSelectedConfs (bool selected=true)

Determines whether only the selected diverse conformers will be returned.

## 3.1.12 OEELFOptions

class OEELFOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for OEELF calculations.

The OEELFOptions class defines the following public methods:

- · GetElfLimit and SetElfLimit
- · GetPercent and SetPercent

#### **Constructors**

OEELFOptions() OEELFOptions (const OEELFOptions&)

Default and copy constructors.

#### operator=

```
OEELFOptions & operator=(const OEELFOptions &)
```

#### **GetElfLimit**

unsigned GetElfLimit() const

See SetElfLimit method.

#### **GetPercent**

double GetPercent () const

See SetPercent method.

#### **SetElfLimit**

bool SetElfLimit (const unsigned)

Sets the number of diverse conformers to select from the least interacting conformers set. Default: 10

#### **SetPercent**

bool SetPercent (const double)

Sets the percentage of input conformers to select as the electrostatically least-interacting set. Default: 2.0

## 3.1.13 OEFormalChargeOptions

class OEFormalChargeOptions

This class is used for setting options during tautomer enumeration with OEEnumerateFormalCharges.

#### **Constructors**

```
OEFormalChargeOptions (const OEFormalChargeOptions & rhs)
OEFormalChargeOptions (unsigned int maxCount=0u, bool verbose=false, bool warts=true))
```

Default and copy constructors.

#### operator=

OEFormalChargeOptions & operator=(const OEFormalChargeOptions & rhs)

Assignment operator.

#### **GetMaxCount**

unsigned int GetMaxCount () const

Get the maximum number of charge states to be enumerated.

#### **GetVerbose**

bool GetVerbose() const

Get whether detailed info will be printed during charge enumeration.

#### **GetWarts**

bool GetWarts () const;

Get whether to add wart to the title of each charge state.

#### **SetMaxCount**

void SetMaxCount (unsigned int max)

Set the maximum number of charge states to be enumerated.

#### **SetVerbose**

void SetVerbose (bool verbose)

Set whether detailed info is to be printed during charge enumeration. The default is false.

#### **SetWarts**

void SetWarts (bool warts);

Set whether to add wart to the title of each charge state. The default is true.

## 3.1.14 OEFormalToPartialCharges

class OEFormalToPartialCharges : public OEChargeEngineBase

Charge engine input to  $OEAssigma$  on  $Charges$  to assign atomic partial charges equal to the atomic formal charges.

The input molecule must have explicit hydrogens. These charges are graph based and do not require 3D coordinates.

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

```
OEFormalToPartialCharges()
```

Constructor. There are no options for this charge engine.

## 3.1.15 OEGasteigerCharges

```
class OEGasteigerCharges : public OEChargeEngineBase
```

Charge engine input to OEAssignCharges to assign Marsili-Gasteiger atomic partial charges.

The input molecule must have explicit hydrogens. Gasteiger charges are graph based and do not require 3D coordinates.

The following methods are publicly inherited from OEChargeEngineBase:

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

#### **Constructors**

```
OEGasteigerCharges()
```

Constructor. There are no options for this charge engine.

## 3.1.16 OEInitialCharges

class OEInitialCharges : public OEChargeEngineBase

Charge engine input to OEAssignCharges to assign atomic partial charges by smearing formal charges onto resonance shared atoms.

The input molecule must have explicit hydrogens. Initial charges are graph based and do not require 3D coordinates.

| <i>operator!=</i>        | <i>GetName</i>                | <i>SetRepairRequestedHint</i> |
|--------------------------|-------------------------------|-------------------------------|
| <i>operator==</i>        | <i>GetRepairRequestedHint</i> | <i>TransferCharge</i>         |
| <i>CheckCharges</i>      | <i>GetRequirements</i>        |                               |
| <i>CreateCopy</i>        | <i>IsValid</i>                |                               |
| <i>GetExpectValidMol</i> | <i>SetExpectValidMol</i>      |                               |

OEInitialCharges()

Constructor. There are no options for this charge engine.

### 3.1.17 OEMMFF94Charges

class OEMMFF94Charges : public OEChargeEngineBase

Charge engine input to OEAssignCharges to assign MMFF94 atomic partial charges.

The input molecule must have explicit hydrogens and MMFF94 parameters must be available for each atom. MMFF charges are graph based and do not require 3D coordinates.

The following methods are publicly inherited from OEChargeEngineBase:

| operator!=        | GetName                | SetRepairRequestedHint |
|-------------------|------------------------|------------------------|
| operator==        | GetRepairRequestedHint | TransferCharge         |
| CheckCharges      | GetRequirements        |                        |
| CreateCopy        | IsValid                |                        |
| GetExpectValidMol | SetExpectValidMol      |                        |

#### **Constructors**

OEMMFF94Charges()

Constructor. There are no options for this charge engine.

### 3.1.18 OESpreadMetalCharges

class OESpreadMetalCharges : public OEChargeEngineBase

Charge engine derived from OEChargeEngineBase that spreads partial charges from a metal to its chelation bonding parters.

| operator!=             | GetExpectValidMol | SetExpectValidMol      |
|------------------------|-------------------|------------------------|
| operator==             | GetName           | SetRepairRequestedHint |
| GetRepairRequestedHint | TransferCharge    |                        |
| CheckCharges           | GetRequirements   |                        |
| CreateCopy             | IsValid           |                        |

```
OESpreadMetalCharges (double chargeAliquot=0.25, double radiusMargin=0.25,
                     double maxNbrDist=6.0)
```

Constructor with input arguments of the incremental amount of charge that should be spread from the metal to each chelating atom (chargeAliquot), the distance beyond the radial-radial distance from which the nearest neighbors cutoff is defined (radiusMargin), and the maximum distance separating the metal and the chelating atoms (maxNbrDist). Parameters also have getter and setter methods.

#### **CreateCopy**

OEChargeEngineBase \*CreateCopy() const

Creates a copy of the charge engine class. This class does not own the returned memory.

#### **GetChargeAliquot**

double GetChargeAliquot () const

Returns the amount of the charge that will be removed from the metal per chelating atom.

#### **GetMaxNbrDist**

double GetMaxNbrDist() const

Returns the maximum nearest neighbors distance (minus the *radiusMargin*) from the metal to the chelating atoms.

#### **GetRadiusMargin**

```
double GetRadiusMargin() const
```

Returns the extra marginal amount of distance such that two atoms can be considered chelators of each other.

#### **SetChargeAliquot**

void SetChargeAliquot (double aliquot)

Sets the amount of charge that should be spread from the metal to each chelating atom.

#### **SetMaxNbrDist**

void SetMaxNbrDist (double distance)

Sets the maximum nearest neighbors distance (minus the radiusMargin) from the metal to the chelating atoms.

#### **SetRadiusMargin**

void SetRadiusMargin (double distance)

Sets the extra marginal amount of distance that two atoms can be considered chelators of each other.

### 3.1.19 OETautomerOptions

class OETautomerOptions

This class is used for setting options during tautomer enumeration with OEEnumerateTautomers.

By default, OEEnumerateTautomers will return the "canonical" tautomer, regardless of the tautomer submitted to the function. This "canonical" tautomer is extremely useful for efficient and reliable tautomer cheminformatics, such as database searching. The OETautomerOptions. SetRankTautomers method can be used to make OEEnumerateTautomers generate a tautomer more "reasonable" for depiction for chemists.

#### **Constructors**

```
OETautomerOptions (unsigned int maxGenerated=4096, bool rank=true, bool warts=false,
                  unsigned int level=0, bool carbonHybrid=true,
                  bool saveStereo=false, unsigned int maxZoneSize=35,
                  unsigned int maxTautomericAtoms = 70, float maxTime = 120,
                  bool kekule = false, bool clearCoords = false,
                  unsigned int hybridLevel = OEHybridizationLevel:: EnolEnamine,
                  unsigned int maxToReturn = 256,
                  unsigned int racemicType = OERacemicType::LocalSampled)
```

Default constructor.

OETautomerOptions (const OETautomerOptions & rhs)

Copy constructor.

#### operator=

OETautomerOptions & operator= (const OETautomerOptions & rhs)

Assignment operator.

#### **GetApplyWarts**

bool GetApplyWarts() const

Returns setting for warts application of  $\{title\}$ ,  $\{title\}$ ,  $\{etc., on tautomers.$ 

#### GetCarbonHybridization

bool GetCarbonHybridization() const

Returns setting for whether or not carbon hybridization changes are allowed. Allowing sp2-sp3 changes of carbon atoms can significantly increase computation time.

#### **GetClearCoordinates**

bool GetClearCoordinates () const

Returns whether input coordinates are cleared. The default value is false.

#### **GetHybridizationLevel**

unsigned int GetHybridizationLevel() const

Returns setting for the level of hybridization changes allowed when carbon hybridization is allowed. Allowing carbon hybridization significantly increase computation time. The returned value is from the OEHybridizationLevel namespace.

#### See also:

· OEHybridizationLevel namespace

#### **GetKekule**

bool GetKekule() const

Returns setting for whether or not generated tautomers are kekule or have aromaticity perceived.

#### **GetLevel**

```
unsigned int GetLevel() const
```

Returns level for tautomerization. Higher levels allow less likely atomic transitions to occur.

#### **GetMaxSearchTime**

float GetMaxSearchTime() const

Returns the maximum search time in seconds allowed for a molecule.

#### **GetMaxTautomericAtoms**

unsigned int GetMaxTautomericAtoms () const

Returns the maximum number of tautomeric atoms allowed in a molecule. The default value is 70.

#### **GetMaxTautomersGenerated**

unsigned int GetMaxTautomersGenerated() const

Returns setting for maximum number of tautomers that may be generated for each input molecule.

#### See also:

· OETautomerOptions. GetMaxTautomersToReturn method

#### **GetMaxTautomersToReturn**

unsigned int GetMaxTautomersToReturn() const

Returns setting for maximum number of tautomers that may be returned for each input molecule.

#### See also:

· OETautomerOptions. GetMaxTautomersGenerated method

#### **GetMaxZoneSize**

unsigned int GetMaxZoneSize() const

Returns setting for maximum number of atoms allowed in a continuous tautomerization zone. The default zone size is 35.

#### **GetRacemicType**

```
unsigned int GetRacemicType () const
```

Returns setting for the way to handle loss of stereocenters, if the OETautomerOptions. GetSaveStereo method returns false. If the OETautomerOptions. GetSaveStereo method returns true, this option is irrelevant. The returned value is from the  $OERACemicType$  namespace. The default value is OERacemicType\_LocalSampled.

#### See also:

- · OETautomerOptions. GetSaveStereo method
- OERacemicType namespace

#### **GetRankTautomers**

```
bool GetRankTautomers() const
```

Returns setting for whether or not tautomers are ranked and ordered before being returned. By default, this is false, i.e., the canonical tautomer is returned as the first molecule in the iterator. As opposed to the most "reasonable" tautomer being returned first.

#### **GetSaveStereo**

bool GetSaveStereo() const

Returns setting for whether atoms and bonds with labeled stereochemistry are fixed or allowed to participate in tautomerization.

#### See also:

· OETautomerOptions. GetRacemicType method

#### **SetApplyWarts**

void SetApplyWarts (bool warts)

Sets whether warts of  $\{\text{title}\}$ \_1,  $\{\text{title}\}$ \_2, etc., are added to tautomers.

#### SetCarbonHybridization

void SetCarbonHybridization (bool carbonHybrid)

Sets whether carbon hybridization changes are allowed. Allowing sp2-sp3 changes of carbon atoms can significantly increase computation time.

#### See also:

• OETautomerOptions. SetHybridizationLevel method

#### **SetClearCoordinates**

void SetClearCoordinates (bool clear\_coordinates)

Sets whether input coordinates are cleared from generated tautomers.

#### **SetHybridizationLevel**

void SetHybridizationLevel (unsigned int level)

Sets level of hybridization changes allowed for carbon atoms if the OETautomerOptions. GetCarbonHybridization method returns true.  $If$ the OETautomerOptions. GetCarbonHybridization method returns false, this option is irrelevant.

level This value has to be from the OEHybridizationLevel namespace.

Note: The level of hybridization can have significantly impact on the computation time.

#### See also:

- · OETautomerOptions. SetCarbonHybridization method
- · OEHybridizationLevel namespace

#### **SetKekule**

void SetKekule (bool kekule)

Sets whether tautomers are returned in kekule format or have aromaticity perceived.

#### **SetLevel**

```
void SetLevel (unsigned int level)
```

Sets level for tautomerization. Higher levels allow less likely atomic transitions to occur.

#### **SetMaxSearchTime**

void SetMaxSearchTime (float maxSearchTime)

Sets the maximum search time in seconds allowed for a molecule.

#### **SetMaxTautomericAtoms**

void SetMaxTautomericAtoms (unsigned int maxTautomerAtoms)

Sets the maximum number of tautomeric atoms allowed in a molecule.

#### **SetMaxTautomersGenerated**

void SetMaxTautomersGenerated (unsigned int max)

Sets the maximum number of tautomers that may be generated per input molecule.

#### See also:

· OETautomerOptions. SetMaxTautomersToReturn method

#### **SetMaxTautomersToReturn**

void SetMaxTautomersToReturn (unsigned int max)

Sets the maximum number of tautomers that may be returned per input molecule.

#### See also:

· OETautomerOptions. SetMaxTautomersGenerated method

#### **SetMaxZoneSize**

void SetMaxZoneSize (unsigned int maxZoneSize)

Sets the maximum number of atoms allowed in a continuous tautomerization zone.

#### **SetRacemicType**

void SetRacemicType (unsigned int racemicType)

Sets the racemic type for loss of stereocenters if the OETautomerOptions. GetSaveStereo method returns false. If the OETautomerOptions. GetSaveStereo method returns true, this option is irrelevant.

**racemicType** This value has to be from the  $OERACemiCType$  namespace.

#### See also:

- · OETautomerOptions. SetSaveStereo method
- OERacemicType namespace

#### **SetRankTautomers**

void SetRankTautomers (bool rank)

Sets whether or not tautomers are ranked and ordered before being returned. Setting this argument to true will cause the most "reasonable" tautomer to be returned as the first tautomer, opposed to the "canonical" tautomer being returned first.

The "canonical" tautomer may or may not be a suitable representative tautomer for depiction. To fill this role, the SetRankTautomers (true) provides "reasonable" tautomer forms for any input molecule.

#### **SetSaveStereo**

void SetSaveStereo (bool saveStereo)

Sets whether atoms and bonds with labeled stereochemistry are fixed or allowed to participate in tautomerization.

#### See also:

· OETautomerOptions. SetRacemicType method

### 3.1.20 OETautomerMolFunction

class OETautomerMolFunction : public OEMolFunctionBase

Warning: This class is deprecated. Use OETautomerOptions instead.

This class represents OETautomerMolFunction. Currently OETautomerMolFunction and OETyperMol-*Function* are similar, however it is expected that they will diverge more over time. They share the same first four arguments. The first argument is the oemolstream where the enumerated molecules will be placed. The second argument is a boolean indicating whether aromaticity should be calculated for the enumerated structure. The third argument is a boolean indicating whether the enumerated states should only be counted (rather than actually listed). The fourth argument is an unsigned int indicating the maximum number of states that should be enumerated for any single input molecule. The fifth argument for OETautomerMolFunction states whether a 'reasonable' type calculation is being setup and only the most aromatic tautomer should be stored. After the calculation, the most aromatic tautomer can be retrieved using OETautomerMolFunction. GetMolecule. The sixth argument will label the output tautomer titles with @`number` appended. When using the same OETautomerMolFunction instance for multiple tautomer runs, remember to call OETautomerMolFunction. Reset in between each run.

#### **Constructors**

```
OETautomerMolFunction (OEChem::oemolostream & ofp, bool arom, bool ct=false,
                      unsigned int max=0, bool mostAro=false, bool warts=true)
```

Default and copy constructors.

#### operator()

```
bool operator () (const OEChem:: OEMolBase &inmol)
```

#### **CreateCopy**

base\_type \*CreateCopy() const

#### **GetCount**

unsigned int GetCount () const

Returns the number of tautomers generated. Calling OETautomerMolFunction. Reset will reset this number to zero.

#### **GetMolecule**

const OEChem:: OEMolBase &GetMolecule () const

This method is used in conjunction with the most Aro flag to retrieve a reasonable looking tautomer.

#### **Reset**

void Reset ()

This method resets the count to zero and clears the stored molecule that OETautomerMolFunction. GetMolecule has access to.

### 3.1.21 OETyperMolFunction

class OETyperMolFunction : public OEMolFunctionBase

This class represents OETyperMolFunction. Currently OETyperMolFunction and OETautomerMolFunction are similar, however it is expected that they will diverge more over time. They share the same first four arguments. The first argument is the oemolstream where the enumerated molecules will be placed. The second argument is a boolean indicating whether aromaticity should be calculated for the enumerated structure. The third argument is a boolean indicating whether the enumerated states should only be counted (rather than actually listed). The fourth argument is an unsigned int indicating the maximum number of states that should be enumerated for any single input molecule.

#### **Constructors**

```
OETyperMolFunction (OEChem::oemolostream & ofp, bool arom, bool ct=false,
                   unsigned int max=0)
```

Default and copy constructors.

#### operator()

bool operator () (const OEChem:: OEMolBase &inmol)

#### **CreateCopy**

base\_type \*CreateCopy() const

#### **Reset**

void Reset ()

This method will reset the internal counter and should be called before reusing an OETyperMolFunction instance.

# **3.2 OEProton Constants**

## 3.2.1 OECharges

This namespace contains constants used by the deprecated function OEAssignPartialCharges to define which charge model to apply. This function is being replaced by  $OEAssignCharges$  which uses an object that defines the charge model and any required pre-processing.

#### **AM1**

AM1 Mulliken-type charges. A full AM1 geometry optimization is done.

#### **AM1BCC**

AM1 Mulliken-type charges with bond-charge corrections. The AM1 optimization is lightly restrained to starting coordinates but no partial charge symmetrization is done (same as OECharges\_AM1BCCNoSym).

Note: Note that this differs from the "standard" AMIBCC charging scheme as published, where symmetrization is done (same as OECharges\_AM1BCCSym).

#### **AM1BCCNoSym**

AM1 Mulliken-type charges with bond-charge corrections. The AM1 optimization is lightly restrained to starting coordinates but no partial charge symmetrization is done.

#### **AM1BCCNoSymSPt**

AM1 Mulliken-type charges with bond-charge corrections. Neither AM1 geometry optimization nor partial charge symmetrization is done.

#### **AM1BCCSPt**

AM1 Mulliken-type charges with bond-charge corrections. Neither AM1 geometry optimization nor partial charge symmetrization is done. (same as OECharges\_AM1BCCNoSymSPt).

#### **AM1BCCSym**

AM1 Mulliken-type charges with bond-charge corrections. The AM1 optimization is lightly restrained to starting coordinates and partial charges are symmetrized with respect to bond-topologically equivalent atoms.

#### **AM1BCCSymSPt**

AM1 Mulliken-type charges with bond-charge corrections; no AM1 geometry optimization is done. Partial charges are symmetrized with respect to bond-topologically equivalent atoms.

#### **AM1SPt**

AM1 Mulliken-type charges; no AM1 geometry optimization is done.

#### AmberFF94

Amber force field 94 charges for standard amino acids.

#### AmberFF99

Amber force field 99 charges (same charges as OECharges\_AmberFF94).

### AmberFF99SB

Amber force field 99SB charges (same charges as OECharges\_AmberFF94).

#### AmberFF99bsc0

Amber force field 99bc0 charges (same charges as OECharges\_AmberFF94).

### **Default**

The current default charges, which are OECharges\_MMFF94.

#### **Formal**

Copies the formal charge field of atoms into the partial charge field.

#### Gasteiger

Assigns Gasteiger partial charges.

#### **Initial**

Smears unit charges in the partial charge field onto resonance shared atoms.

#### MMFF94

Assigns MMFF94 partial charges.

#### **Max**

Number of charge type constants.

#### **NoOp**

No operation is performed. This setting is useful for indicating that charges originated elsewhere, such as user input, and have not been changed.

#### **None**

Remove all partial charges.

#### **OPLS**

OPLS protein dictionary charges.

**Warning:** This charging model is deprecated. The OEAssignPartialCharges function will throw a deprecated warning message when calling it with this charging model.

## 3.2.2 OEChargingRequirement

This namespace contains constants that describe requirements of charge model objects derived from the OEChargeEngineBase abstract base class.

#### **AltersResidueName**

**BondedResidues** 

**Compact** 

**Coords3D** 

## **ExplicitHydrogens**

**MolComplexPrep** 

**MultiConfOnly** 

**Nothing** 

**PDBOrder** 

**Parameters** 

Precharged

**ResPerceived** 

**ReturnSelectedConfs** 

**SetsAromaticity** 

### **SetsType**

#### **SizeWithinLimits**

#### **StandardResidues**

## 3.2.3 OEHybridizationLevel

This namespace contains constants used by the class OETautomerOptions to store the level of carbon hybridization.

#### See also:

- OETautomerOptions class
- · OETautomerOptions. GetHybridizationLevel method
- · OETautomerOptions. SetHybridizationLevel method

### **Default**

The default value is OEHybridizationLevel\_EnolEnamine.

#### **Original**

If carbon hybridization is set, then extensive carbon hybridization will take place.

#### **DoubleBondNbr**

If carbon hybridization is set, then only localized carbon hybridzation will take place, allowing generation of keto-enol tautomers without generating as many extreme tautomers as the default parameter.

#### **EnolEnamine**

If carbon hybridization is set, then local hybridization will take place to allow keto-enol and enol-enamine tautomerization while generating fewer tautomers than other options above.

## 3.2.4 OERacemicType

This namespace contains constants used by the class OETautomerOptions that stores the stereo loss behavior when the OETautomerOptions. GetSaveStereo method returns false.

**Note:** If the OETautomerOptions. GetSaveStereo method returns true, this flag is irrelevant.

#### See also:

- OETautomerOptions class
- · OETautomerOptions. GetSaveStereo method
- · OETautomerOptions. SetSaveStereo method

#### **Default**

The default value is OERacemicType\_LocalSampled.

#### **None**

This option indicates that no racemic type will be set.

#### **LocalSampled**

This option indicates that individual tautomers that have double bonds to tetrahedral stereocenters will have the stereo removed.

#### **EverSampled**

This option indicates that if an atom which are tetrahedral stereocenters has a double bonds in any of the tautomers returned by the function, then those tetrahedral stereocenters will have the stereo removed in ALL of the returned tautomers.

## **3.3 OEProton Functions**

### 3.3.1 OEAssignCharges

```
bool OEAssignCharges (OEChem:: OEMolBase &mol,
                      const OEChargeEngineBase & chargeEngine)
bool OEAssignCharges (OEChem:: OEMCMolBase & mcMol,
                      const OEChargeEngineBase & chargeEngine)
```

**Note:** This function is designed to replace the legacy function OEAssignPartialCharges.

This function sets the charge of each atom in the molecule mol based on the specific nature of the *chargeEngine* object passed as the second argument. In general, charge engine implementations place scalar partial charges on atoms, but could be implemented to perform other roles such as assign multi-pole charges.

#### Listing 1: Assigning MMFF Partial Charges to a Molecule

```
if oequacpac. OEAssignCharges (mol, oequacpac. OEMMFF94Charges () ) :
    \# ...
```

Another example:

#### **Listing 2: Assigning Unoptimized AM1 Partial Charges**

```
optimizationSetting = False
if oequacpac. OEAssignCharges (mol, oequacpac. OEAM1Charges (optimizationSetting)) :
    \# ...
```

The objects used by this function, derived from the abstract base class OEChargeEngineBase, can be thought of as "options objects" which describe the details of a specific charge model. OEAssignCharges analyzes these options and may need to add explicit hydrogens or perceive residues before assigning charges.

#### **Listing 3: Assigning Non-symmetrized AM1BCC Partial Charges**

```
chargeEngine = oequacpac.OEAM1BCCCharges()chargeEngine.SetSymmetrize(False)
if oequacpac. OEAssignCharges (mol, chargeEngine) :
    # . . .
```

Some prerequisites, such as setting the aromaticity model, would alter the input molecule in ways that are incidental to the calculation. In this case, a copy of the input molecule is made before the alterations are made and the charges are transferred back to the input molecule after the calculation. This ensures that only charges, explicit hydrogens, residue perception, residue names, and the number of conformations returned can change on the input molecule.

This function returns false if does not succeed.

#### See also:

- · OEAssignPartialCharges function
- OEChargeEngineBase abstract base class
- Assigning Charges code example

## **3.3.2 OEAssignPartialCharges**

```
bool OEAssignPartialCharges (OEChem:: OEMolBase &mol,
                             unsigned int method=OECharges::Default,
                            bool noHydrogen=false, bool debug=false)
bool OEAssignPartialCharges (OEChem:: OEMCMolBase &mol,
                            unsigned int method=OECharges::Default,
                            bool noHydrogen=false, bool debug=false)
```

**Note:** This deprecated function will not be developed further. It is being replaced by OEAssignCharges which provides more control and greater expandability.

This function sets the partial charge value of each atom in a molecule. The molecule to be charged is passed as the first argument. The second argument is the charge model to be used. These values should be selected from the OECharges namespace. The third argument is a boolean for whether the final molecule should have explicit hydrogens. If noHydrogen is set to true, all hydrogens will be made implicit, and the charge on each heavy atom with attached hydrogens will be adjusted to be the sum of its original partial charge and all of the attached hydrogen partial charges. The debug flag controls the volume of debug information written to standard error. This function returns a boolean value evaluating the success of the calculation.

This function is overloaded to accept an OEMolBase or an OEMCMolBase. Currently, only AM1 and AM1BCC charges have specialized multiconformer implementations in the OEMCMolBase overload. For all other charges, the OEMCMolBase and OEMolBase implementations are identical.

#### See also:

• OEAssignCharges function

## 3.3.3 OEEnumerateFormalCharges

```
OESystem:: OEIterBase<OEChem:: OEMolBase> *
  OEEnumerateFormalCharges (const OEChem:: OEMolBase &mol,
                            const OEFormalChargeOptions &formalChargeOptions
                                                        =OEFormalChargeOptions())
OESystem:: OEIterBase<OEChem:: OEMolBase> *
  OEEnumerateFormalCharges (const OEChem:: OEMCMolBase &mol,
                            const OEFormalChargeOptions &formalChargeOptions
                                                        =OEFormalChargeOptions())
```

This function takes a const input molecule and variants of that molecule different formal charges are returned as an OESystem::OEIterBase<OEChem::OEMolBase> \*. Options are set with an OEFormalChargeOptions, a parameter that is not required. See the corresponding documentation for descriptions of options.

Warning: The following version of OEEnumerateFormalCharges is deprecated. Use the above OEFormalChargeOptions version instead.

unsigned int OEEnumerateFormalCharges (OEChem:: OEMolBase &mol, OEMolFunctionBase &mfb, **bool** verbose=false)

This function has three arguments. The first is the non-const molecule whose formal charges are to be enumerated. For details of the enumeration process, please see *pkatyper - Ligand pKa*. The second argument is a functor call-back. The functor's operator () is called with each new protonation state enumerated. The enumeration will continue until the functor returns false or until the enumeration is complete. The third argument determines if verbose atomtype information should be written to standard out. The function will return the total number of states which were enumerated.

## 3.3.4 OEEnumerateTautomers

```
OESystem:: OEIterBase<OEChem:: OEMolBase> *
  OEEnumerateTautomers(const OEChem:: OEMolBase &mol,
                       const OETautomerOptions &tautomerOptions)
OESystem:: OEIterBase<OEChem:: OEMolBase> *
  OEEnumerateTautomers(const OEChem:: OEMCMolBase &mol,
                       const OETautomerOptions &tautomerOptions)
```

This function takes a const input molecule that is to be tautomerized and the tautomers are returned as an OESystem::OEIterBase<OEChem::OEMolBase> \*. Options are set with an OETautomerOptions. See the corresponding documentation for descriptions of options.

```
unsigned int OEEnumerateTautomers (OEChem:: OEMolBase &mol,
                                  OEMolFunctionBase &mfb, unsigned int allflag=0,
                                  bool ch3flag=false
                                  bool saveStereo = false, float maxTime = 120)
```

Warning: This version of OEEnumerateTautomers is deprecated. Use the above OETautomerOptions version above instead.

This function has four arguments. The first argument in a non-const molecule that will be the basis for the tautomer enumeration. For details of the enumeration process, please see *tautomers*. The second argument is a functor callback. The functor's operator () is called with each new tautomer state enumerated. The enumeration will continue until the functor returns false or until the enumeration is complete. The third argument is an unsigned int which indicates the maximum acceptable energetic category of enumerated tautomers. The function will return all categories of tautomers from the lowest available up to this cutoff. If the only available level is higher than the cutoff, that single level of tautomers will be enumerated. This control is in addition to the call-back control. Finally, the bool ch3flaq argument controls whether tautomer enumeration should include tautomerization of methyl and methylene groups adjacent to a conjugated system. This allows cyclohexa-2,4-dien-1-one,  $O=C1CC=CC=CL$ , to be canonicalized as a tautomer of phenol, Oc1ccccc1. Unfortunately, the combinatorial explosion from tautomerizing across the alpha carbon of amino acids means that this option should not be used when enumerating the tautomers of proteins and large peptides. This function returns the total number of tautomers enumerated.

A setting of saveStereo=true will prevent associated atoms or bonds from taking part in tautomerization if they have stereochemistry set. Stereochemistry can naturally be lost with the creation and removal of double bonds.

### 3.3.5 OEGetChargeTypeName

const char\* OEGetChargeTypeName (unsigned int chargeType)

This function returns the corresponding  $OECharges$  name for the *unsigned int chargeType* method.

## 3.3.6 OEGetReasonableProtomer

```
bool OEGetReasonableProtomer(OEChem::OEMolBase &mol)
bool OEGetReasonableProtomer(OEChem::OEMCMolBase &mol)
```

This function will attempt to produce a single protomer that will be a suitable representation of the molecule in a biological system. This state is defined as an aqueous environment with  $pH-7.4$  and a tautomer from among the predominate tautomers that is favored by medicinal chemists. This function is intended to be suitable for preparing molecules to display to chemists. The molecules are quite consistent, but should not be considered a canonical form in this version.

See also:

• OEGetReasonableProtomers function

## 3.3.7 OEGetReasonableProtomers

```
OESystem::OEIterBase<OEChem::OEMolBase> *OEGetReasonableProtomers(const
\rightarrow OEChem:: OEMolBase & mol) :
OESystem::OEIterBase<OEChem::OEMCMolBase> *OEGetReasonableProtomers(const
\rightarrow OEChem:: OEMCMolBase & mol);
```

This function will attempt to produce a series of protomers that will be a suitable ensemble of the molecule in a biological system. This state is defined as an aqueous environment with  $pH-7.4$ . The tautomers of the molecule are enumerated. For each enumerated tautomer a single charge state representing the predominate ionization at pH 7.4 is chosen. Ionization states of each charge state are NOT enumerated in this version.

#### See also:

- · OEGetReasonableProtomer function
- · OEGetReasonableTautomers function

## 3.3.8 OEGetReasonableTautomers

```
OESystem:: OEIterBase<OEChem:: OEMolBase> *
  OEGetReasonableTautomers(const OEChem:: OEMolBase &mol,
                           const OETautomerOptions &opts=OETautomerOptions(),
                           bool pKaNorm=true);
OESystem::OEIterBase<OEChem::OEMCMolBase> *
  OEGetReasonableTautomers (const OEChem:: OEMCMolBase &mol,
                            const OETautomerOptions &opts=OETautomerOptions(),
                           bool pKaNorm=true);
```

This function takes a const input molecule that is to be tautomerized and the tautomers are returned as an iterator over molecules. The function is overloaded to handle both single (OEMolBase) and multi-conformer (OEMCMolBase) molecules.

- *mol* The molecule being tautomerized.
- **opts** The OETautomerOptions object that stores properties that influence tautomerization process.
- *pKaNorm* This parameter determines whether to apply pKa normalization. If true the ionization state of each tautomer will be assigned to a predominate state at pH~7.4.

#### **Example of tautomerizing a molecule**

```
tautomer_options = oequacpac.OETautomerOptions()
tautomer_options.SetMaxTautomersGenerated(4096)
tautomer_options.SetMaxTautomersToReturn(16)
tautomer_options.SetCarbonHybridization(True)
tautomer_options.SetMaxZoneSize(50)
tautomer_options.SetApplyWarts(True)
pKa\_norm = Truefor mol in ifs. GetOEGraphMols():
    for tautomer in oequacpac. OEGetReasonableTautomers (mol, tautomer_options, pKa_
\rightarrownorm):
        # work with tautomer
```

#### See also:

- OEEnumerateTautomers function
- OEGetReasonableProtomer function
- · OEGetReasonableProtomers function

#### See also:

• Enumerating Tautomers code example

### 3.3.9 OEGetUniqueProtomer

bool OEGetUniqueProtomer(OEChem::OEMolBase &dst, const OEChem::OEMolBase &mol) bool OEGetUniqueProtomer(OEChem::OEMCMolBase &dst, const OEChem::OEMCMolBase &mol)

This function will attempt to produce a single protomer that can be used to generate a canonical representation of all tautomers of this molecule. All charge states or tautomer representations of a molecule should generate the same unique tautomer.

**Note:** The unique protomer is NOT necessarily the low energy tautomer, or a scientifically reasonable tautomer. It is a tautomer useful for generating canonical hash strings. The unique protomer can be used to generate single or multiple protomers suitable for visualization by passing then through the  $OEGetReasonableTautomers$  functions.

#### See also:

• OEGetReasonableTautomers function

### 3.3.10 OEHypervalentNormalization

void OEHypervalentNormalization (OEChem:: OEMolBase &mol);

This function should be used in conjunction with OEREMOVEFOrMalCharge to prepare a molecule to be passed to the OEEnumerateTautomers function. These two normalization help the tautomer enumeration yield a higher proportion of lower-energy tautomers.

See also:

- · OEEnumerateTautomers
- · OERemoveFormalCharge

### 3.3.11 OEQuacPacGetArch

const char \*OEQuacPacGetArch()

Returns the architecture on which the release was built

## 3.3.12 OEQuacPacGetLicensee

**bool** OEQuacPacGetLicensee(std::string &licensee)

Fills the parameter string alicensee with the licensee of the license file being used

### 3.3.13 OEQuacPacGetPlatform

const char \*OEQuacPacGetPlatform()

Returns the platform on which the release of built

## 3.3.14 OEQuacPacGetRelease

const char \*OEQuacPacGetRelease()

Returns the version number as a const char \* in major.minor.bugfix form

## 3.3.15 OEQuacPacGetSite

**bool** OEOuacPacGetSite(std::string &site)

Fills the parameter string & licensee with the site on the license file being used

### 3.3.16 OEQuacPacGetVersion

unsigned int OEQuacPacGetVersion()

Returns the build date of the release.

## 3.3.17 OEQuacPacIsLicensed

bool OEQuacPacIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any **Quacpac TK** functionality.

The 'feature' argument can be used to check for a valid license to **Quacpac TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current **Quacpac TK** license.

#### See also:

• OEChemIsLicensed function

## 3.3.18 OERemoveFormalCharge

```
bool OERemoveFormalCharge (OEChem:: OEMolBase &mol)
bool OERemoveFormalCharge (OEChem:: OEMCMolBase & mol)
```

This function will attempt to remove all formal charges from mol in a manner that is consistent with adding and removing implicit or explicit protons. This method will not create radicals and will not attach more protons to an atom than is acceptable in that atom's standard valence form. Please note that the formal charge of quaternary amines is not removed with this command.

## 3.3.19 OESetNeutralpHModel

```
bool OESetNeutralpHModel (OEChem:: OEMolBase &mol)
bool OESetNeutralpHModel (OEChem::OEMCMolBase &mol)
```

This function will attempt to set mol to the most energetically favorable ionization state for pH=7.4 using a rule-based system. This function does not enumerate multiple states for any molecule. In cases where the ionization is near 7.4 and could be represented by a mixture of states, the state that is likely to be most populated is chosen.

#### See also:

• Setting a Neutral Ionization State code example

## 3.3.20 OETautomersLargestZoneSize

```
unsigned int OETautomersLargestZoneSize(const OEChem:: OEMolBase &mol,
                                        const OETautomerOptions &tautomerOptions)
unsigned int OETautomersLargestZoneSize(const OEChem:: OEMolBase &mol,
                                        unsigned maxZone = 0)
```

This function returns the largest number of atoms in a continuous tautomerization zone for the molecule and OETautomerOptions instance passed in as arguments. The later function provides a convenient function that relies on the default tautomer options other than potentially the maxZone size. The return value of this function plays a significant role in determining the upper bounds of the runtime for tautomer calculations on the molecule.

## **3.4 OEMoIAM1 Classes**

### 3.4.1 OEAM1

class OEAM1 : public OEMolPotential:: OEMolFunc1

Note: This is a low level api class that allows access to advanced functionality from semi-empirical method calculations. It is recommended that you use the high level api method OEAssignCharges with OEAMICharges options to assign AM1 charges on a molecule.

The OEAM1 class calculates Mulliken-type partial charges and other relevant quantities in a molecule using AM1 type semi-empirical quantum mechanical methods.

The input must be a 3D molecule, and the AM1 parameters must be available for each atom type in the molecule.

#### The following methods are publicly inherited from OEFunc0:

- · operator()
- · GetFComponents
- NumVar

#### The following methods are publicly inherited from OEFunc1:

• operator()

#### The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

#### The OEAM1 class defines the following public methods:

- $\bullet$  CalcAM1
- · GetOptions
- · GetResults

```
OEAM1()
OEAM1 (const OEAM1Options&)
OEAM1 (const OEAM1&)
```

Default and copy constructors.

Constructs an *OEAM1* instance using the specified set of parameters.

#### operator=

OEAM1 & operator= (const OEAM1 &)

The assignment operator.

#### CalcAM1

bool CalcAM1 (OEAM1Results&, const OEMolBase&) const

Performs AM1 calculation on the specified molecule and fills up the specified OEAM1Results with calculated results. Returns false if calculation was not successful.

#### **GetOptions**

const OEAM1Options& GetOptions() const

Returns a reference to the OEAM1Options instance as currently set for this OEAM1.

#### **GetResults**

bool GetResults (OEAM1Results&) const

Fills up the specified OEAMIResults with results from the last calculation. Returns false if a valid set of results does not exist.

### 3.4.2 OEAM1Options

class OEAM1Options : public OESystem: : OEOptions

This class provides an interface to setup options required for OEAM1 calculations.

#### The OEAM10ptions class defines the following public methods:

- · GetMaxScfIter
- GetNumericGradDelta
- · GetSCFTolerance
- · GetSemiMethod
- · SetMaxScfIter

- · SetNumericGradDelta
- SetSCFTolerance
- · SetSemiMethod

```
OEAM1Options()
OEAM1Options (const OEAM1Options&)
```

Default and copy constructors.

#### operator=

```
OEAM1Options & operator= (const OEAM1Options &)
```

#### **GetMaxScfIter**

unsigned int GetMaxScfIter() const

Gets the maximum number of self-consistent field iterations to be used.

#### **GetNumericGradDelta**

double GetNumericGradDelta() const

Gets the current value of the numerical gradients delta to be used for gradients calculation.

#### **GetSCFTolerance**

double GetSCFTolerance() const

Gets the current value of the self-consistent field calculation tolerance.

#### **GetSemiMethod**

unsigned int GetSemiMethod() const

Gets the current value of the semi-empirical method to be used.

#### **SetMaxScfIter**

bool SetMaxScfIter (const unsigned int)

Sets the maximum number of self-consistent field iterations to be used.

#### **SetNumericGradDelta**

bool SetNumericGradDelta (const double)

Sets the value of the numerical gradients delta to be used for gradients calculation.

#### **SetSCFTolerance**

bool SetSCFTolerance (const double)

Sets the value of the self-consistent field calculation tolerance.

#### **SetSemiMethod**

bool SetSemiMethod (const unsigned int)

Sets the semi-empirical method to be used for the calculations. The default is  $OEMethodType\_AM1$ . Alternatives are defined in the OEMethodType namespace.

### 3.4.3 OEAM1Results

class OEAM1Results

This class represents OEAM1 calculation results.

The OEAM1Results class defines the following public methods:

- · GetAtomicBondOrder
- · GetBondOrder
- · GetBondOrders
- GetCharges
- GetEnergy
- · GetNumSCFCycles
- · IsConverged

```
OEAM1Results()
OEAM1Results (const OEAM1Results&)
```

Default and copy constructors.

#### operator=

OEAM1Results & operator= (const OEAM1Results &)

#### **GetAtomicBondOrder**

double GetAtomicBondOrder (const unsigned int index) const

Returns the atomic bond order of the atom with specified index.

#### **GetBondOrder**

double GetBondOrder (const unsigned int index1, const unsigned int index2) const

Returns the bond order between the two atoms with specified indices.

#### See also:

· Wiberg bond orders chapter

#### **GetBondOrders**

const std:: vector<double>& GetBondOrders() const

Returns the bond orders on all bondss. Bond orders are stored in the vector according to the bond indices.

#### See also:

• Wiberg bond orders chapter

#### **GetCharges**

const std:: vector<double>& GetCharges() const

Returns the AM1 charges on all atoms. Charges are stored in the vector according to the atom indices.

#### **GetEnergy**

double GetEnergy () const

Returns the AM1 calculated energy of the molecule.

#### **GetNumSCFCycles**

unsigned int GetNumSCFCycles() const

Returns the number of self-consistent field cycles used during calculation.

#### **IsConverged**

bool IsConverged() const

Returns if the OEAM1 self-consistent field calculation converged.

## 3.4.4 OEOptimizedAM1

class OEOptimizedAM1

Note: This is a low level api class that allows access to advanced functionality from semi-empirical method calculations. It is recommended that you use the high level api method OEAssignCharges with OEAMICharges options to assign AM1 charges on a molecule.

The OEOptimizedAM1 class optimizes OEAM1 followed by calculation of Mulliken-type partial charges and other relevant quantities.

The input must be a 3D molecule, and the AM1 parameters must be available for each atom type in the molecule.

The OEOptimizedAM1 class defines the following public methods:

· CalcAM1

#### **Constructors**

```
OEOptimizedAM1 (unsigned int wvnFnType = OEMethodType:: AM1)
OEOptimizedAM1 (const OEOptimizedAM1&)
```

Default and copy constructors.

The wave functype could be any value defined in OEMethodType namespace.

#### operator=

```
OEOptimizedAM1 & operator= (const OEOptimizedAM1 &)
```

The assignment operator.

#### CalcAM1

```
bool CalcAM1 (OEAM1Results& results, const OEChem:: OEMolBase& mol)
bool CalcAM1 (OEAM1Results& results, const OEChem:: OEMCMolBase& mol)
```

Optimizes and performs AM1 calculation on the specified molecule and fills up the specified OEAM1Results with calculated results. Returns false if calculation was not successful.

## **3.5 OEMoIAM1 Constants**

### 3.5.1 OEMethodType

This namespace contains constants which define the type of semi-empirical methods that can be used for OEAM1 calculation.

#### AM<sub>1</sub>

AM1 semi-empirical method.

#### PM<sub>3</sub>

PM3 semi-empirical method.

## **3.6 OEMoIAM1 Constants**

### 3.6.1 OEBCCType

This namespace contains constants which define the type of bond charge correction models that can be used for OEBCCPartialCharges calculation.

### **AM1**

AM1 semi-empirical method.

#### PM<sub>3</sub>

PM3 semi-empirical method.

# **3.7 OEAM1BCC Functions**

## 3.7.1 OEBCCPartialCharges

```
bool OEBCCPartialCharges (OEChem:: OEMolBase& mol,
                         unsigned int BCCModel = OEBCCType::AMI,bool permissive = false,
                         bool verbose = false)
```

This function calculates the bond correction partial charges on the specified molecule. Calculated charges are set as the partial charges of the molecule.

mol Molecule to calculate BCC partial charges.

**BCCModel** Bond charge correction semi-empirical model defined in  $OEBCCType$  namespace

*permissive* TODO - Need help.

verbose Flag if verbose information should be provided

## 3.7.2 OESymmetrizePartialCharges

bool OESymmetrizePartialCharges (OEChem:: OEMolBase& mol)

This function makes the partial charges on the molecule symmetric based on molecule topology.

### **CHAPTER**

## **FOUR**

# **PRELIMINARY API**

# **4.1 Preliminary OEProton Class**

## 4.1.1 OEChargeParameter

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEChargeParameter : public OESystem:: OEMultiParameter →<OEProton:: OEChargeEngineBase>

The OEChargeParameter represents parameter that has a value of type OEChargeEngineBase.

### Following methods are publicly inherited from OEParameter:

- · AddAlias and GetAliases
- · AddDetail and GetDetail
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

Following methods are publicly inherited from OEMultiParameter:

- · AddLegalEntry
- · GetDefault and SetDefault
- · GetSetting
- · GetValue and SetValue

#### **Constructors**

```
OEChargeParameter()
OEChargeParameter(const std::string& name, const bool customAllowed)
OEChargeParameter (const OEChargeParameter&)
```

#### Default and copy constructors.

Constructs an OEChargeParameter instance using the specified set of parameters. The second argument in the second constructor represents if a custom forcefield can be used.

#### operator=

OEChargeParameter &operator=(const OEChargeParameter &)

The assignment operator.

### 4.1.2 OEMultistatepKaModel

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEMultistatepKaModel

This class provides functionality to assess the atomic pKa of a given molecule and enumerate ionization states at neutral pH. The options required for this class can be set using the OEMultistatepKaModelOptions class.

The OEMultistatepKaModel class defines the following public methods:

- $\bullet$  Tnit
- · CalculateNumOfMicrostates
- · SetAllAtomspKaData
- · GetModelMolecule
- · GetAtompKaRange
- · GenerateMicrostates

- · GetMicrostates
- · HasAdjTypeAtNeutralpH
- · HaspKaRange

#### Constructors.

```
OEMultistatepKaModel()
OEMultistatepKaModel(OEChem::OEMolBase &mol)
OEMultistatepKaModel (OEChem:: OEMolBase &mol, OEMultistatepKaModelOptions &opts)
```

Copy constructor.

```
OEMultistatepKaModel (const OEMultistatepKaModel & rhs)
```

Copy assignment constructor.

#### operator=

OEMultistatepKaModel& operator=(const OEMultistatepKaModel & rhs)

#### Init

```
void Init (OEChem:: OEMolBase & mol)
void Init (OEChem:: OEMolBase & mol, OEMultistatepKaModelOptions & opts)
```

If a user has initialized the OEMultistatepKaModel instance with default constructor (without molecule and options object), they can add a molecule and OEMultistatepKaModelOptions instance later by the Init method.

#### **CalculateNumOfMicrostates**

int CalculateNumOfMicrostates()

This method calculates the number of microstates possible for given molecule. It uses the information (generic pKa data) assessed and set by the method SetAllAtomspKaData. It returns -1 if either OEMultistatepKaModel failed to assess all atomic pKa on the molecule (probably due to unknown atoms present), or it halted assessing pKa data because the projected number of microstates exceeded the provided limit of microstates to be generated.

#### **GetModelMolecule**

```
const OEChem:: OEMolBase& GetModelMolecule()
```

This method returns the copy of the internal molecule object from the OEMultistatepKaModel class on which all atomic pKa data are assessed and set as generic data.

#### **GetAtompKaRange**

unsigned int GetAtompKaRange (const OEChem:: OEAtomBase\* atom)

This method allows a user to assess and get the pKa range (OEpKaRange\_Acidic, OEpKaRange\_Neutral, OEpKaRange\_Basic or OEpKaRange\_Unidentified) for an individual atom.

#### GetAtomAdjTypeAtNeutralpH

unsigned int GetAtomAdjTypeAtNeutralpH(const OEChem:: OEAtomBase\* atom)

This method allows a user to assess and get the adjustment type to be done at neutral OEAdjTypeAtNeutralpH\_NoChange,  $pH$  $\left($ OEAdjTypeAtNeutralpH\_Protonation, OEAdjTypeAtNeutralpH\_Deprotonation, OEAdjTypeAtNeutralpH\_NoChangeAndProtonation, OEAdjTypeAtNeutralpH\_NoChangeAndDeprotonation) for an individual atom.

#### **GenerateMicrostates**

bool GenerateMicrostates()

This method generates all possible microstates (up to the limit specified by the options class). These generated microstates can be accessed by the method GetMicrostates.

#### **GetMicrostates**

OESystem:: OEIterBase<OEChem:: OEMolBase>\* GetMicrostates()

Microstates generated by the method GenerateMicrostates can be accessed by this method. It returns an iterator over the generated microstates molecule objects.

#### HasAdjTypeAtNeutralpH

HasAdjTypeAtNeutralpH()

This is a predicate functor, which allows a user to filter atoms with the desired OEAdjTypeAtNeutralpH generic data attached

#### **HaspKaRange**

HaspKaRange()

This is a predicate functor, which allows a user to filter atoms with the desired  $OEpKARange$  generic data attached.

#### **SetAllAtomspKaData**

bool SetAllAtomspKaData()

This method assesses the atomic pKa for all heavy/hetero atoms and sets generic pKa data for these atoms. If an OEMultistatepKaModelOptions class object is specified with the parameter processcarbons = true, it assesses all heavy atoms. If an OEMultistatepKaModelOptions class object is specified with the parameter processcarbons = false, then only hetero atoms are assessed.

### 4.1.3 OEMultistatepKaModelOptions

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in  $C++$  and Python.

class OEMultistatepKaModelOptions

This class provides an interface to set up options required for OEMultistatepKaModel.

The OEMultistatepKaModelOptions class defines the following public methods:

- · GetpH and SetpH
- · GetProcessCarbons and SetProcessCarbons
- · GetMaxNumMicrostates and SetMaxNumMicrostates

#### **Constructors**

```
OEMultistatepKaModelOptions()
OEMultistatepKaModelOptions (bool processcarbons, unsigned int maxnummicrostates)
```

Copy constructor.

OEMultistatepKaModelOptions (const OEMultistatepKaModelOptions&)

#### Copy assignment constructor.

```
OEMultistatepKaModelOptions& operator=(const OEMultistatepKaModelOptions &rhs);
```

#### **GetpH**

unsigned int GetpH()

Gets the value of the pH parameters at which a user wants to assess ionization states of the molecule. Only a neutral pH can be set. This option is defined in anticipation of a wider pKa model at different pH environments.

#### **SetpH**

Sets the pH to be used to assess the ionization states of the molecule. Only a neutral pH can be set. This option is defined in anticipation of a wider pKa model at different pH environments.

#### **GetProcessCarbons**

**bool** GetProcessCarbons()

Returns the parameter setting requesting the pKa assessment of carbon atoms. Default is true.

#### **SetProcessCarbons**

bool SetProcessCarbons (bool pc)

Sets whether a user wants to assess the pKa of carbon atoms, true or false.

#### **GetMaxNumMicrostates**

unsigned int GetMaxNumMicrostates()

Gets the value of maximum number of microstates to generate; the parameter is set by default or by the method SetMaxNumMicrostates.

#### **SetMaxNumMicrostates**

bool SetMaxNumMicrostates (unsigned int maxnummicrostates)

Sets the maximum number of microstates to generate. If the projected number of microstates is more than the maximum limit set by this function, the model will not generate any microstates.

## **4.2 Preliminary OEProton Constants**

### 4.2.1 OEAdjTypeAtNeutralpH

This namespace contains constants used by the class OEMultistatepKaModel to define what adjustment is to apply to the atom according to the multistate model.

#### See also:

- OEMultistatepKaModel class
- OEpKaRange constants namespace
- · OEMultistatepKaModelpH constants namespace
- OEGetAtomAdjTypeAtNeutralpHName function
- OEGetAtomAdjTypeAtNeutralpHType function

#### **Deprotonation**

The atom with this tag will be deprotonated to generate a favored ionization state.

#### **NoChange**

The atom with this tag will not be modified in generated ionization state.

#### NoChangeAndDeprotonation

Two different ionization states will be generated for the atom with this tag. In one of them atom will not be changed and in another state the atom will be deprotonated.

#### **NoChangeAndProtonation**

Two different ionization states will be generated for the atom with this tag. In one of them atom will not be changed and in another state the atom will be protonated.

#### **Protonation**

The atom with this tag will be protonated to generate a favored ionization state.

#### **Unknown**

This constant represents an undefined or illegal context state.

### 4.2.2 OEMultistatepKaModelpH

This namespace contains constants used by the class OEMultistatepKaModel and OEMultistatepKaModelOptions to define the pH at which the multistate model assesses the pKa.

#### See also:

- OEMultistatepKaModelOptions class
- OEMultistatepKaModel class
- OEAdjTypeAtNeutralpH constants namespace
- · OEMultistatepKaModelpH constants namespace
- · OEGetMultistatepKaModelpHNamefunction

• OEGetMultistatepKaModelpHType function

#### **Neutral**

MultistatepKaModel assesses the pKa at Neutral pH (physiological pH i.e. 7.4).

#### **Unknown**

This constant represents an undefined or illegal context state.

## 4.2.3 OEpKaRange

This namespace contains constants used by the class OEMultistatepKaModel to define what is the assessed atomic pKa range of the atom according to the multistate model.

See also:

- OEMultistatepKaModel class
- OEAdjTypeAtNeutralpH constants namespace
- OEMultistatepKaModelpH constants namespace
- · OEGetAtompKaRangeName function
- · OEGetAtompKaRangeTypefunction

#### **Acidic**

The atom has Acidic pka range  $( $6.4$ ).$ 

#### **Basic**

The atom has Basic pka range  $(>8.4)$ .

#### **Neutral**

The atom has Neutral pka range (between 6.4 and 8.4).

#### **Unidentified**

The atom's pKa range is unidentified by the multistate pka model.

#### **Unknown**

This constant represents an undefined or illegal context state.

## **4.3 Preliminary OEProton Functions**

## 4.3.1 OEGetAtomAdjTypeAtNeutralpHName

std::string OEGetAtomAdjTypeAtNeutralpHName(const unsigned int adjTypeID)

This function returns a corresponding name for the given *adjTypeID* value from the *OEAdjTypeAtNeutralpH* namespace.

See also:

· OEGetAtomAdjTypeAtNeutralpHTypefunction

## 4.3.2 OEGetAtomAdjTypeAtNeutralpHType

unsigned int OEGetAtomAdjTypeAtNeutralpHType(const std::string& adjTypeName)

This function returns the constant from the OEAdjTypeAtNeutralpH namespace for the provided *adjTypeName*.

See also:

· OEGetAtomAdjTypeAtNeutralpHNamefunction

## 4.3.3 OEGetAtompKaRangeName

std::string OEGetAtompKaRangeName(const unsigned int pKaRangeID)

This function returns a corresponding name for the given *pKaRangeID* value from the *OEpKaRange* namespace.

See also:

• OEGetAtompKaRangeType function

## 4.3.4 OEGetAtompKaRangeType

unsigned int OEGetAtompKaRangeType (const std::string& pKaRangeName)

This function returns the constant from the  $OEpKaRange$  namespace for the provided  $pKaRangeName$ .

#### See also:

· OEGetAtompKaRangeName function

## 4.3.5 OEGetMultistatepKaModelpHName

std::string OEGetMultistatepKaModelpHName(const unsigned int pHType)

This function returns a corresponding name for the given  $pHType$  value from the  $OEMultistatepKaModelpH$ namespace.

#### See also:

• OEGetMultistatepKaModelpHTypefunction

## 4.3.6 OEGetMultistatepKaModelpHType

unsigned int OEGetMultistatepKaModelpHType (const std::string& pHName)

This function returns the constant from the OEMultistatepKaModelpH namespace for the provided pHName.

#### See also:

• OEGetMultistatepKaModelpHNamefunction

### **CHAPTER**

## **FIVE**

# **RELEASE HISTORY**

# **5.1 Quacpac TK 2.2.5**

## 5.1.1 Minor bug fixes

• Some issues with primary amines processing in *OEMultistatepKaModel* have been fixed.

# **5.2 Quacpac TK 2.2.4**

Minor internal improvements have been made.

# **5.3 Quacpac TK 2.2.3**

Minor internal improvements have been made.

# **5.4 Quacpac TK 2.2.2**

Minor internal improvements have been made.

# **5.5 Quacpac TK 2.2.1**

Minor internal improvements have been made.

# **5.6 Quacpac TK 2.2.0**

## 5.6.1 New features

• New preliminary API classes, OEMultistatepKaModel and OEMultistatepKaModelOptions, have been added to assess atomic pKa ranges for atoms of a given molecule, and to enumerate all possible ionization states of input molecules at neutral/physiological pH (7.4) based on a multistate heuristic pKa model.

# **5.7 Quacpac TK 2.1.4**

## 5.7.1 New features

• [QUACPAC-599] New preliminary classes, OEMultistatepKaModel and OEMultistatepKaModelOptions, have been added to asses atomic pKa ranges for atoms of given molecule and enumerate all possible ionization states of input molecule at neutral/physiological pH $(7.4)$  based on a heuristic pKa model.

## 5.7.2 Major bug fixes

- 5.7.3 Minor bug fixes
- 5.7.4 Python-specific changes
- 5.7.5 Java-specific changes
- 5.7.6 C#-specific changes
- **5.7.7 Documentation changes**

## **5.8 Quacpac TK 2.1.3**

Fall 2021

## 5.8.1 New features

• OEChargeParameter now accepts case-insensitive string input values.

# **5.9 Quacpac TK 2.1.2**

**July 2021** Minor internal improvements have been made.

# 5.10 Quacpac TK 2.1.1.2

### **March 2021**

- OEOptimizedAM1 no longer requires a special am1bcc license.
- The function OEBCCPartialCharges no longer requires a special am1bcc license.

## 5.11 Quacpac TK 2.1.1

**Fall 2020** 

## 5.11.1 New features

• A new preliminary class, *OEChargeParameter*, has been added as part of the extended set of OEParameter classes. The new parameter class works with predefined charge engines using OEChargeEngineBase object.

## **5.12 Quacpac TK 2.1.0**

## 5.12.1 New features

- The OEDesignUnitComponents\_CounterIons molecule components are now charged with the metal charge engine for design unit charges.
- A new class, *OEOptimizedAM1*, has been added that obtains optimized *OEAM1* Mulliken-type partial charges.
- Two new classes, OEELF and OEELFOptions, have been added that allow selecting conformers from a given ensemble using the electrostatically least-interacting functional group (ELF) technique.
- A new method, OEBCCP artial Charges, has been added that calculates bond correction partial charges.
- A new method, OESymmetrizePartialCharges, has been added that makes partial charges symmetric based on molecule topology.
- A new method, OEAM1Results, GetBondOrders, has been added to OEAM1Results that provides access to all the bond orders in a list.

## 5.12.2 Minor bug fixes

- The following methods now return bool instead of a void:
  - OEAM1Options. SetMaxScfIter
  - OEAM1Options. SetNumericGradDelta
  - OEAM1Options. SetSCFTolerance
  - OEAM1Options. SetSemiMethod
- OEAssignCharges with OEELFCharges now outputs the correct set of conformers selected using the ELF technique.
- The number of diverse conformers needed to select and use for charge calculation is now automatically adjusted when the desired OEELFOptions. SetElfLimit is higher than the number of initial conformers selected based on OEELFOptions. SetPercent and the input number of conformers in the molecule.
- OEEnumerateTautomers no longer throws a fatal error when when no tautomers are found.

## **5.13 Quacpac TK 2.0.2**

### 5.13.1 New features (Preliminary)

• A new preliminary class, *OEDesignUnitCharges*, has been added that charges an OEDesignUnit.

### 5.13.2 New features

• A new optional argument, warts, has been added to the OEFormalChargeOptions constructor. Two new methods, OEFormalChargeOptions. GetWarts and OEFormalChargeOptions. SetWarts, have also been added that control whether to add wart to the title of each charge state.

## **5.14 Quacpac TK 2.0.1**

## 5.14.1 Minor bug fixes

- $\bullet$  The definition OEHybridizationLevel Default of has been changed from OEHybridizationLevel Original to OEHybridizationLevel EnolEnamine for consistency with the behavior of the default OETautomerOptions class constructor.
- OEAssignCharges no longer requires a case license when used with OEELFCharges.
- OEEnumerateTautomers has been fixed to output multiple tautomers when OETautomerOptions. SetRankTautomers is false.
- OEAssignCharges no longer crashes for molecules where the distance between atoms is less than 0.5 Angstrom.

## 5.15 Quacpac TK 2.0.0

### 5.15.1 New features

- A new OEGetReasonableTautomers function has been added that generates an ensemble of biologically relevant tautomers.
- A new OEGetUniqueProtomer function has been added that generates a canonical representation of a molecule.
- A new OEGetReasonableProtomers function has been added that generates an ensemble of reasonable protomers.
- The handling of keto-enol tautomerization by default has been improved. The improvement extends to include imine-enamine tautomerization and related analogs. The keto and imine forms are favored except in the case of 1,3 diketones, where the internal hydrogen bond can be formed.
- Controlling the interaction between tautomerization and tetrahedral stereochemistry has been improved. The method OETautomerOptions. SetSaveStereo can still be set to true in order to prevent any stereo atom from ever becoming an sp2 center. However, the behavior when the vale is set to false can now be controlled by passing a constant from the new  $OERacemi\ cType$  namespace to the method OETautomerOptions. SetRacemicType. This functionality allows users to control which stereochemistry will be cleared on each generated tautomer.

- Reasonable tautomers for many simple and complex pyridone analogs, pyrrole analogs, and pyridine analogs have been improved.
- A new OEHypervalent Normalization function has been added to prepare molecules for tautomer enumeration (OEEnumerateTautomers).
- The user control of the algorithms memory and CPU usage by separately exposing the number of tautomers generated and the number of tautomers returned by the methods OETautomerOptions. SetMaxTautomersGenerated and OETautomerOptions. SetMaxTautomersToReturn, respectively, has been improved.
- The default parameters of the OETautomerOptions class have been updated to reflect the underlying improved tautomer generation algorithm.

### 5.15.2 Major bug fixes

- Several issues that caused double bonds and hydrogens to be allowed to move too far through a series of sp3 centers have been fixed.
- The default behavior of peptide tautomers and peptide stereochemistry has been improved.
- Keto-enol tautomerization by default has been added to improve the canonical grouping of unique molecules by their representative tautomers.

### 5.15.3 Minor bug fixes

• Aromatic bond count has been added to scoring to improve the handling of fused pyrrole and pyrazine chemistries when estimating low-energy tautomers.

### 5.15.4 Documentation changes

• The tautomers theory chapter has been rewritten to reflect common usages of the tautomer library.

## **5.16 Quacpac TK 1.9.3**

#### 5.16.1 New features

- A new class, *OEAM1*, has been added to provide AM1-like semi-empirical method functionality.
- A new class, *OEAM10ptions*, has been added to set up *OEAM1* calculation options.
- A new class, OEAM1Results, has been added to obtain OEAM1 calculation results.
- The class OETautomerOptions now exposes settings to allow control of Kekule results, clearing of coordinates, and the degree of carbon hybridization.

## 5.16.2 Documentation changes

• An example that displays obtaining Wiberg bond orders from an AM1 calculation has been added.

# **5.17 Quacpac TK 1.9.2**

## 5.17.1 Minor bug fixes

- OEAssignPartialCharges, deprecated since the 2017. Feb release, now throws a deprecated warning.
- OEEnumerateTautomers now obeys the maximum tautomers option set in the OETautomerOptions class.

## 5.17.2 Documentation changes

• The functions OEEnumerateTautomers and OEGetReasonableProtomer remove molecule coordinates during their processing since changing the tautomer state may invalidate the 3D structure. This behavior change was introduced in the 2017. Feb release.

## **5.18 Quacpac TK 1.9.1**

## 5.18.1 Documentation changes

- The behavior of the OEChargeEngineBase. SetExpectValidMol method is now documented correctly.
- Code examples in the Quacpac TK Examples chapter have been revised.

# **5.19 Quacpac TK 1.9.0**

## 5.19.1 New features

• A new charging function,  $OEBssignCharges$ , has been developed to replace the more limited legacy function OEAssignPartialCharges. This new function uses charge engines, an open-ended options class, to define the charging method. Charge engines can be configured as required and new charge engines can be developed independently. Charge engines have been written for every supported charging method, as well as for the new method OEAM1BCCELF10Charges.

## 5.19.2 Minor bug fixes

• Warning messages from AM1BCC charging functions have been made more informative.

## 5.19.3 Documentation changes

• The documentation has been updated to describe the new charge engine approach to charging and to show examples of its use.

# **5.20 Quacpac TK 1.8.6**

• Minor internal improvements have been made.

## **5.21 Quacpac TK 1.8.5**

• Minor internal improvements have been made.

## **5.22 Quacpac TK 1.8.4**

### 5.22.1 New features

- The number of methods available for use with OEAssignPartialCharges is now defined as OECharges\_Max.
- A timer has been added to tautomer enumeration. OETautomerOptions. SetMaxSearchTime and OETautomerOptions. GetMaxSearchTime can be used to set and get a time limit for searching tautomers, respectively.

## 5.22.2 Major bug fixes

• Calling OEAssignPartialCharges on a molecule with no formal charges with the method OECharges Initial no longer returns false.

## 5.22.3 Deprecated functionality

• OECharges\_OPLS charging model is no longer supported with OEAssignPartialCharges function.

## **5.23 Quacpac TK 1.8.3**

## 5.23.1 New features

- . OEGetReasonableProtomer and OEEnumerateTautomers with OETautomerOptions with the OETautomerOptions. SetRankTautomers set to true have improved handling of diols and nitro groups in recognition of the most reasonable tautomers.
- . OEGetReasonableProtomer and OEEnumerateTautomers with OETautomerOptions with the OETautomerOptions. SetRankTautomers set to true now employ a second-stage approach in cases where the first set of generated tautomers produces no desirable tautomeric states.

## 5.23.2 Major bug fixes

• OEGetReasonableProtomer will no longer have the side-effect of resetting the atomic coordinates to the origin.

## **5.24 Quacpac TK 1.8.2**

### 5.24.1 Minor bug fixes

- OESetNeutralpHModel and OERemoveFormalCharge will now produce a planar geometry when deprotonating an N-protonated amide. Previously, this was incorrectly producing a pyrimidal geometry.
- OECharges\_AmberFF94 will no longer identify a CYS residue as anionic when it is bonded by a sulfur to something other than another CYS residue.
- OEGetReasonableProtomer will now preserve molecule title, SD data, and atom coordinates.

## **5.25 Quacpac TK 1.8.1**

### 5.25.1 New features

• TIP3P water charges are now assigned when using Amber charge sets on molecules containing waters. The application of OEAssignPartialCharges using OECharges\_AmberFF94 or any of the other Amber charge sets to waters with explicit hydrogens will produce oxygen charges of -0.834 and hydrogen charges of  $+0.417.$ 

### 5.25.2 Minor bug fixes

• The default behavior of OETautomerOptions has been changed from true to false when applying warts to titles.

### 5.25.3 Documentation fixes

• OEEnumerateTautomers now includes a snippet of code in the documentation to make using the function easier.

## **5.26 Quacpac TK 1.8.0**

## 5.26.1 New features

• Passing true to OETautomerOptions. SetRankTautomers was dramatically improved to provide a low-energy, medicinally-relevant "reasonable" tautomeric form that is suitable for depiction for chemists. Significant improvements were made to the "reasonable" tautomer algorithm that effect the aliphatic and nonaromatic resonance portions of tautomers.

- Made conversion of carboxylates to diols and nitros to di-hydroxy amines very unfavorable.

![](_page_98_Figure_2.jpeg)

- Made generation of unnecessary, non-dative, formal charges unfavorable.

![](_page_98_Figure_4.jpeg)

![](_page_98_Figure_5.jpeg)

favored

![](_page_99_Figure_1.jpeg)

- Improved accounting for exocyclic bonds adjacent to aromatic rings.

![](_page_99_Figure_3.jpeg)

- Set priority for aliphatic double bond position that could be arbitrary in prior versions.

![](_page_100_Figure_1.jpeg)

- OEGetReasonableProtomer added to provide a convenient "best practices" function to generate a most chemically reasonable tautomerization and ionization state for a molecule. The function yields a low-energy medicinally relevant protomer suitable for depiction for chemists.
- OETautomersLargestZoneSize now overloaded with a more convenient function that does not require constructing a OETautomerOptions object to explore the maximum zone size considered for tautomerization of a molecule.

## 5.26.2 Minor bug fixes

- OESetNeutralpHModel consistency has been improved by forcing the molecule to use the OpenEye aromaticity model before applying pH rules (pattern matching) to molecules from heterogeneous source or file formats.
- OECharges\_Default constant is now the exact same value as OECharges\_MMFF94. Previously, it was a different numerical value, making comparison un-necessarily difficult. Note, the default charging model is still the same.

## 5.26.3 Known bugs

• OEGetReasonableProtomer title warting is not working correctly. All titles will be output "\_1". This will be fixed for the next release, 2015.Feb.

## 5.26.4 Documentation fixes

• The tautomers theory chapter has been made more specific to the toolkit.

## **5.27 Quacpac TK 1.7.2**

### 5.27.1 New features

### 5.27.2 Minor bug fixes

• Calling OEGetChargeTypeName with the constant OECharges\_Default, now returns the name of the default charge method, OECharges\_MMFF94.

## 5.27.3 Documentation fixes

## **5.28 Quacpac TK 1.7.1**

### 5.28.1 New features

• OETyperMolFunction and OEFormalChargeOptions is now the preferred way to set options for the OEEnumerateFormalCharges function. The new form of OEEnumerateFormalCharges returns an iterator of molecules.

## 5.28.2 Minor bug fixes

• Removed unbounded stack allocations.

### **5.28.3 Documentation fixes**

- Quacpac TK examples have been renamed to more accurately reflect their function.
- Documented the Amber force field constants OECharges\_AmberFF94, OECharges\_AmberFF99, OECharges\_AmberFF99SB, and OECharges\_AmberFF99bsc0.
- Documented the AM1BCC constant OECharges\_AM1BCCSymSPt and fixed a mistake in the description of the constant OECharges\_AM1BCCSPt.

## **5.29 Quacpac TK 1.7.0**

### 5.29.1 New features

- OETautomerMolFunction has been deprecated and OETautomerOptions is now the preferred way to set options for the OEEnumerateTautomers function. OEEnumerateTautomers will now return an iterator of molecules optionally ordered by favorableness of the tautomer. Therefore, the first tautomer in the iterator is the same as what was previously returned by OETautomerMolFunction. GetMolecule.
- A hard limit on the total number of atoms participating in tautomerization is now adjustable in OETautomerOptions. Additionally, an adjustable parameter maxZoneSize has been added for setting the maximum number of atoms that are allowed in a continuous tautomerization zone. Any molecule that exceeds either of these limits will cause OEEnumerateTautomers to return the input tautomer.
- OETautomersLargestZoneSize function added to return the largest number of atoms in a continuous tautomerization zone for a particular molecule.

## **5.30 Quacpac TK 1.6.4**

### 5.30.1 New features

- The new function OERemoveFormalCharge has been added. This function sets the formal charges on a molecule to zero while maintaining a standard valence state.
- The new function  $OEGetChapter$   $TypeName$  has been added. This function returns the corresponding OECharges name for the *unsigned int* passed in.

### 5.30.2 Minor bug fixes

• The wart symbol has been changed from @ to in order to help with parsing SMILES formatting.

## **5.31 Quacpac TK 1.6.2**

### 5.31.1 Major bug fixes

- OEEnumerateTautomers was removing stereochemistry from all atoms that did not have a valence of 4. This has been fixed so that other types of atoms with legitimate stereochemistry, such as nitrogen and hypervalent atoms, no longer lose their stereochemistry information.
- · OEEnumerateFormalCharges has been fixed to properly handle 3D input. Previously, 3D input would cause an incorrect number of hydrogen atoms and an incorrect valence state on adjusted heavy atoms.

## 5.31.2 Minor bug fixes

- OESetNeutralpHModel will no longer ionize difluoro, dichloro, and N-methyl acetamide.
- OESetNeutralpHModel will now use the molecule title when available instead of a smiles string for warning messages.
- OESetNeutralpHModel warning messages for bad valence have been clarified.
- OEAssignPartialCharges will no longer exit when using OECharges\_AM1BCCNoSym with multiconformer molecules.

## 5.32 Quacpac TK 1.6.1

### 5.32.1 New features

- OEEnumerateTautomers will now allow interconversion of  $[NH2+] =$  and  $[NH3+]$ .
- *OETautomerMolFunction* now has a warts option. Enabling this options will number the output molecules with an @ symbol.

## 5.32.2 Major bug fixes

## 5.32.3 Minor bug fixes

- OEEnumerateTautomers will now properly set stereochemistry on planar carbon to OEAtom-Stereo::Undefined. Previously, planar carbon could inherit stereochemistry from an input molecule with stereochemistry set on a tetrahedral carbon.
- A few bugs have been fixed in  $OESetNeutralpHModel$  involving quaternary nitrogen and protonated aromatic nitrogens.

## 5.33 Quacpac TK 1.6.0

### 5.33.1 New features

• The default AM1BCC charge model OECharges\_AM1BCC now lightly restrains the AM1 geometry optimization to the starting coordinates. This allows the important relaxation of bond and angle degrees of freedom while greatly reducing the potential to alter the molecule's conformation away from its starting coordinates. AM1 geometry optimization can be suppressed with OECharges\_AM1BCCSPt or OECharges AM1BCCNoSymSPt.

## 5.33.2 Bug fixes

• The AM1BCC charge models OECharges\_AM1BCCSym and OECharges\_AM1BCCSPt now symmetrize the partial charges over bond-topologically equivalent atoms, e.g. methyl hydrogens, in keeping with the original model. This is especially important with conformationally flexible molecules. This behavior can be suppressed by using the default OECharges\_AM1BCC or the non-default models OECharges\_AM1BCCNoSym or OECharges AM1BCCNoSymSPt.

## 5.34 Quacpac TK 1.5.2

### 5.34.1 New features

• Refined Neutral pH model (OESetNeutralpHModel) to reflect feedback from collaborators. In particular isoxazoles and oxadiazoles were added while pyrazoles and aryl sulfonamides were refined. Aryl sulfonamide refinement also incorporated changes based on newly obtained experimental data.

## 5.34.2 Minor bug fixes

- OESetNeutralpHModel now correctly addresses beta di-amino groups so that if all other considerations are equivalent, secondary amines are treated as most basic, followed by primary amines, with tertiary amine being treated as least basic.
- OETautomerMolFunction. GetMolecule has been fixed so that 3D molecules have 3D hydrogens instead of implicit hydrogens.
- OEAssignPartialCharges no longer inadvertently converts reduced cysteine residues (CYS) to the oxidized form (CYX) when  $OECharges\_AmberFF94$  is used to assign Amber partial charges to protein residues.

## 5.35 Quacpac TK 1.5.1

### 5.35.1 Bug Fixes

• A bug has been fixed where tautomers were not guaranteed to be in a canonical form during output. In rare circumstances this could lead to tautomers with the same unique tautomer to print it in different non-canonical forms.

# 5.36 Quacpac TK 1.5.0

### 5.36.1 New Features

- Major improvement for carbon hybridization. Now carbon atoms with bonds to one, two, or three heavy atoms are able to change hybridization state. However, only carbons close to an appropriate heteroatom are allowed to change hybridization state. Additionally, unreasonable charge states of carbon have been removed. Now the enabling the  $ch3flag$  option will only generate tautomers appropriate for the given level.
- Improvement of the  $most\text{A}ro$  option, particularly involving exocyclic heteroatoms.
- Added stereo preservation flag to OEEnumerateTautomers with a default of false. Stereo chemistry can be lost during creation and removal of double bonds, but if the user desires a certain stereo setting to be preserved this flag will prevent the associated atoms and bonds from taking part in tautomerization.
- Improvements to pka states.
- AmberFF94 charges can now be applied to standard protein residues.
- The Quacpac TK versioning APIs (OEQuacPacGetRelease, OEQuacPacIsLicensed, etc) are now properly wrapped in Python.

## **5.37 Quacpac TK 1.4.1**

## 5.37.1 Bug Fixes

- OESetNeutralpHModel has been added to the Java and Python wrappers.
- Bug has been fixed in OEAssignPartialCharges where it sometimes did not return false after a failure to assign charges. Now this function should always return false if charges are not set.
- Fixed tetronic acid rule in OESetNeutralpHModel to allow matching of aromatic bonds.

## **5.38 Quacpac TK 1.4.0**

### 5.38.1 New features

• OESetNeutralpHModel has been added. This function may be used to set a molecule to an energetically favorable ionization state for  $pH=7.4$ . This is the same  $pH$  model that was available in the Filter application. Additionally, the perception of acceptable valence states has been improved to include phosphorus as well as aromatic oxygen and sulfur with +1 formal charge.

- OEEnumerateFormalCharges now implicitly uses the mostAro=true parameter on the OETautomer-MolFunction it uses when choosing a tautomer. This provides a better reference tautomer when enumerating pKa states.
- Aromaticity settings on molecules are now unchanged when  $OEAs signal in Lcharges$  is called. Aromaticity may be temporarily changed inside the function while charges are being calculated, but the molecule will have the same aromaticity after the function as before.

## 5.39 Quacpac TK 1.3.1

### 5.39.1 New features

• The distribution and installation of Quacpac has been modified. The Windows distribution is now a standard EXE installer, and the OS X distribution is a dmg containing a standard pkg installer. The executables are now scripts that chose the correct version of the program at runtime. Please see the Application Installation section for details.

## 5.39.2 Bug fixes

• The previous version had a license failure when AM1 charges were calculated. This bug has been fixed.

## **5.40 Quacpac TK 1.3.0**

This release represents the first major reworking of the Quacpac TK and applications in several years. Any users of prior versions of Quacpac will quickly notice several significant changes. First, this version of Quacpac does not contain a new release of protein pKa program. We are in the midst of a major rewrite of the protein pKa program. We hope that this work will bring major improvements in the usability, science and analysis of the protein pKa program, yet we do not want to delay the release of the entire Quacpac package waiting for the protein pKa program. The current Quacpac release does not contain protein pKa, but it will be included in a future release when the rewrite is complete. In the interim, we hope you find the bug fixes and new features included in this release useful.

The preps and qpd programs will no longer be supported future versions of Quacpac.

### 5.40.1 New features

- A reasonable looking tautomer may be calculated by setting the most Aro boolean to true in OETautomer-MolFunction. After the max number of tautomers have been attempted, the most aromatic looking molecule may be retrieved using the OETautomerMolFunction. GetMolecule method.
- An OEMCMolBase version of OEAssignPartialCharges has been added for calculating multiconformer AM1BCC charges

## 5.40.2 Bug fixes

- Library has changed names from liboeproton to liboequacpac
- Memory leak related to OETyperMolFunction and OETautomerMolFunction is fixed.
- SMILES map indexes and names are no longer lost when outputting molecules.

# **5.41 Quacpac TK 1.1.0**

- Special Note: Version 1.4 of Molcharge and version 1.2b of the library have been released and inserted into version 1.1 of Quacpac. Both of these have removed support for the VC2003 partial charging method.
- Version 1.1 is the first full stable release of Quacpac. Quacpac remains a heterogeneous release including five primary applications and a programming library with a C++ api.
- Tautomers is in version 2.0. It provides enumeration of energetically reasonable tautomers of input molecules.
- pKaTyper is in version 1.1. pKaTyper provides enumeration of protonation states (pKa  $\sim$  2- $\sim$ 14).
- Molcharge is in version 1.3. Molcharge provides MMFF, AM1, AM1BCC, VC2003 and other partial charges on small molecules.
- Protein pka is in version 1.3. Protein pKa carries out PB calculations to assess the shifts in protein residue pKa's.
- This release includes the oeproton library. The oeproton library exposes the features of pKaTyper, tautomers and molcharge in three high level C++ api points. The version of the library in this release is 1.1b. However, the beta moniker signifies only that at this time, OpenEye reserves the right to modify this api. We believe the quality of the code in this library is very solid and the beta designation does not reflect its quality.

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

## **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

#### **CHAPTER**

## **EIGHT**

## **CITATION**

## 8.1 Orion<sup>®</sup> Floes

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

## **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                                             | Licen                                                                 |
|-------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                                | https:/                                                               |
| absl-py                       | https://github.com/abseil/abseil-py                                                 | https:/                                                               |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                                 | https:/                                                               |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                               | https:/                                                               |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                               | N/A                                                                   |
| AmberUtils                    | http://ambermd.org                                                                  | N/A                                                                   |
| ambit                         | https://github.com/khimaros/ambit                                                   | https:/                                                               |
| amqp                          | https://github.com/celery/py-amqp                                                   | https:/                                                               |
| anaconda-anon-usage           | <b>Orion Floes</b>                                                                  | https:/                                                               |
| angular                       | https://github.com/angular/angular.js                                               | https:/                                                               |
| angular-animate               | https://github.com/angular/angular.js                                               | https:/                                                               |
| angular-cache                 | https://github.com/jmdobry/angular-cache                                            | https:/                                                               |
| angular-cookies               | https://github.com/angular/angular.js                                               | https:/                                                               |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                                    | https:/                                                               |
| angular-mocks                 | https://github.com/angular/angular.js                                               | https:/                                                               |
| angular-resource              | https://github.com/angular/angular.js                                               | https:/                                                               |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                                    | https:/                                                               |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                               | https:/                                                               |
| angular-ui-router             | https://github.com/angular-ui/ui-router                                             | https:/                                                               |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                                  | https:/                                                               |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                                        | https:/                                                               |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                                            | https:/                                                               |
| annotated-types               | https://github.com/annotated-types/annotated-types                                  | https:/                                                               |
| anyio                         | https://github.com/agronholm/anyio                                                  | https:/                                                               |
| appdirs                       | http://github.com/ActiveState/appdirs                                               | http://                                                               |
| appengine                     | https://google.golang.org/appengine                                                 | https:/                                                               |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                                   | https:/                                                               |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md                          | https:/                                                               |
| Name of Project               | Website                                                                             | License                                                               |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                | https://github.com/hynek/argon2-cffi                                  |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                       | https://github.com/hynek/argon2-cffi-bindings                         |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                          | https://www.caam.rice.edu/software/ARPACK/                            |
| ascii85                       | https://github.com/huandu/node-ascii85                                              | https://github.com/huandu/node-ascii85                                |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                      | https://wiki.fysik.dtu.dk/ase/                                        |
| asgiref                       | https://github.com/django/asgiref/                                                  | https://github.com/django/asgiref/                                    |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                                 | https://github.com/wbond/asn1crypto                                   |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render               | https://github.com/smartystreets/assertions/internal/go-render/render |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers                   | https://github.com/smartystreets/assertions/internal/oglematchers     |
| assertions                    | https://github.com/smartystreets/assertions                                         | https://github.com/smartystreets/assertions                           |
| asttokens                     | https://github.com/gristlabs/asttokens                                              | https://github.com/gristlabs/asttokens                                |
| astunparse                    | https://github.com/simonpercivall/astunparse                                        | https://github.com/simonpercivall/astunparse                          |
| async-lru                     | https://github.com/aio-libs/async-lru                                               | https://github.com/aio-libs/async-lru                                 |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                           | https://github.com/aio-libs/async-timeout                             |
| atk-1.0                       | https://docs.gtk.org/atk/                                                           | https://docs.gtk.org/atk/                                             |
| atomic                        | https://github.com/uber-go/atomic                                                   | https://github.com/uber-go/atomic                                     |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                    | https://github.com/untitaker/python-atomicwrites                      |
| attrs                         | https://www.attrs.org/                                                              | https://www.attrs.org/                                                |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                                   | https://github.com/aws/aws-sdk-go                                     |
| Babel                         | https://github.com/python-babel/babel                                               | https://github.com/python-babel/babel                                 |
| backcall                      | https://github.com/takluyver/backcall                                               | https://github.com/takluyver/backcall                                 |
| backports                     | https://github.com/brandon-rhodes/backports                                         | https://github.com/brandon-rhodes/backports                           |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                             | https://github.com/jaraco/backports.functools_lru_cache               |
| base62                        | https://github.com/kare/base62                                                      | https://github.com/kare/base62                                        |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                      | https://www.crummy.com/software/BeautifulSoup/                        |
| billiard                      | https://github.com/celery/billiard                                                  | https://github.com/celery/billiard                                    |
| biopython                     | https://biopython.org                                                               | https://biopython.org                                                 |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https://github.com/biotite-dev/biotite/blob/master/README.rst         |
| bitset                        | https://github.com/willf/bitset                                                     | https://github.com/willf/bitset                                       |
| blas                          | https://www.netlib.org/blas/                                                        | https://www.netlib.org/blas/                                          |
| bleach                        | https://github.com/mozilla/bleach                                                   | https://github.com/mozilla/bleach                                     |
| blessings                     | https://github.com/erikrose/blessings                                               | https://github.com/erikrose/blessings                                 |
| blinker                       | https://pythonhosted.org/blinker/                                                   | https://pythonhosted.org/blinker/                                     |
| blosc                         | https://github.com/Blosc/python-blosc                                               | https://github.com/Blosc/python-blosc                                 |
| blosc2                        | https://github.com/Blosc/python-blosc2                                              | https://github.com/Blosc/python-blosc2                                |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https://github.com/mahmoud/boltons                                    |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https://github.com/bootstrap-vue/bootstrap-vue                        |
| boto3                         | https://github.com/boto/boto3                                                       | https://github.com/boto/boto3                                         |
| botocore                      | https://github.com/boto/botocore                                                    | https://github.com/boto/botocore                                      |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                              | https://bottleneck.readthedocs.io/en/latest/index.html                |
| Brotli                        | https://github.com/google/brotli                                                    | https://github.com/google/brotli                                      |
| brotli-bin                    | https://github.com/google/brotli                                                    | https://github.com/google/brotli                                      |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | http://python-hyper.org/projects/brotlipy/en/latest/                  |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                          | https://github.com/python-hyper/brotlicffi                            |
| bson                          | http://github.com/py-bson/bson                                                      | http://github.com/py-bson/bson                                        |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https://code.cloudfoundry.org/bytefmt                                 |
| bzip2                         | https://www.bzip.org                                                                | https://www.bzip.org                                                  |
|                               |                                                                                     | J.                                                                    |
| Name of Project               | Website                                                                             | Licen                                                                 |
| c-ares                        | https://github.com/c-ares/c-ares                                                    | https:/                                                               |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/                                                               |
| cached-property               | https://github.com/pydanny/cached-property                                          | https:/                                                               |
| cachetools                    | https://github.com/tkem/cachetools/                                                 | https:/                                                               |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           | https:/                                                               |
| canvas                        | https://github.com/Automattic/node-canvas                                           | https:/                                                               |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              | https:/                                                               |
| celery                        | https://github.com/celery/celery                                                    | https:/                                                               |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         | https:/                                                               |
| certifi                       | https://certifiio.readthedocs.io/en/latest/                                         | https:/                                                               |
| $\overline{\text{eff}}$       | https://github.com/python-cffi                                                      | https:/                                                               |
| cftime                        | https://pypi.org/project/cftime/                                                    | https:/                                                               |
| chardet                       | https://github.com/chardet/chardet                                                  | https:/                                                               |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        | https:/                                                               |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             | https:/                                                               |
| click                         | https://palletsprojects.com/p/click/                                                | https:/                                                               |
| click-completion              | https://github.com/click-contrib/click-completion                                   | https:/                                                               |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   | https:/                                                               |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      | https:/                                                               |
| click-repl                    | https://github.com/untitaker/click-repl                                             | https:/                                                               |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            | https:/                                                               |
| cmake                         | https://cmake.org/                                                                  | https:/                                                               |
| colorama                      | https://github.com/tartley/colorama                                                 | https:/                                                               |
| comm                          | https://github.com/ipython/comm                                                     | https:/                                                               |
| compose                       | https://github.com/docker/compose                                                   | https:/                                                               |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        | https:/                                                               |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      | https:/                                                               |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     | https:/                                                               |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/                                                               |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           | https:/                                                               |
| confuse                       | https://github.com/beetbox/confuse                                                  | https:/                                                               |
| contourpy                     | https://github.com/contourpy/contourpy                                              | https:/                                                               |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               | https:/                                                               |
| cryptography                  | https://github.com/pyca/cryptography                                                |                                                                       |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                                | https:/                                                               |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           | https:/                                                               |
| cupy-cuda113                  | https://cupy.dev/                                                                   | https:/                                                               |
| curl                          | https://curl.se                                                                     | https:/                                                               |
|                               | https://github.com/matplotlib/cycler                                                | https:/                                                               |
| cycler                        |                                                                                     | https:/                                                               |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             | https:/                                                               |
| Cython                        | https://cython.org                                                                  | https:/                                                               |
| $\overline{d3}$               | https://github.com/mbostock/d3                                                      | https:/                                                               |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           | https:/                                                               |
| ddsketch                      | http://github.com/datadog/sketches-py                                               | https:/                                                               |
| debugpy                       | https://aka.ms/debugpy                                                              | https:/                                                               |
| decimal                       | https://github.com/shopspring/decimal                                               | https:/                                                               |
| decorator                     | https://github.com/micheles/decorator                                               | https:/                                                               |
| deepdiff                      | https://github.com/seperman/deepdiff                                                | https:/                                                               |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             | https:/                                                               |
|                               |                                                                                     | J.                                                                    |
| Name of Project               | Website                                                                             | Licen                                                                 |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https:/                                                               |
| dill                          | https://github.com/uqfoundation/dill                                                | https:/                                                               |
| distro                        | <b>Orion Floes</b>                                                                  | https:/                                                               |
| Django                        | https://www.djangoproject.com/                                                      | https:/                                                               |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                    | https:/                                                               |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                   | https:/                                                               |
| django-csp                    | https://github.com/mozilla/django-csp                                               | https:/                                                               |
| django-extensions             | https://github.com/django-extensions/django-extensions                              | https:/                                                               |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                          | https:/                                                               |
| django-redis                  | https://github.com/jazzband/django-redis                                            | https:/                                                               |
| django-taggit                 | https://github.com/jazzband/django-taggit                                           | https:/                                                               |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/                                                               |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                              | https:/                                                               |
| djangorestframework           | https://www.django-rest-framework.org/                                              | https:/                                                               |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                      | https:/                                                               |
| dm-tree                       | https://github.com/deepmind/tree                                                    | https:/                                                               |
| docker-py                     | https://github.com/docker/docker-py/                                                | https:/                                                               |
| docopt                        | https://docopt.org                                                                  | https:/                                                               |
| docutils                      | https://docutils.sourceforge.io                                                     | https:/                                                               |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/                                                               |
| editdistance                  | https://github.com/roy-ht/editdistance                                              | https:/                                                               |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/                                                               |
| einops                        | https://github.com/arogozhnikov/einops                                              | https:/                                                               |
|                               | https://github.com/takluyver/entrypoints                                            |                                                                       |
| entrypoints                   | https://github.com/pkg/errors                                                       | https:/                                                               |
| errors                        |                                                                                     | https:/                                                               |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                               |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/                                                               |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         | https:/                                                               |
| executing                     | https://github.com/alexmojaki/executing                                             | https:/                                                               |
| expat                         | https://libexpat.github.io                                                          | https:/                                                               |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                   | https:/                                                               |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 | https:/                                                               |
| fftw                          | https://www.fftw.org                                                                | comm                                                                  |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              | https:/                                                               |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/                                                               |
| finufft                       | https://github.com/flatironinstitute/finufft                                        | https:/                                                               |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/                                                               |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               | https:/                                                               |
| flit-core                     | https://github.com/pypa/flit                                                        | https:/                                                               |
| <b>FLTK</b>                   | https://www.fltk.org/index.php                                                      | https:/                                                               |
| fmt                           | https://fmt.dev/latest/index.html                                                   | https:/                                                               |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         | https:/                                                               |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      | https:/                                                               |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       | https:/                                                               |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/                                                               |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            | https:/                                                               |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/                                                               |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/                                                               |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/                                                               |
| Name of Project               | Website                                                                             | License                                                               |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https://                                                              |
| freetype                      | https://freetype.org                                                                | https://                                                              |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https://                                                              |
| frozendict                    | Orion Floes                                                                         | https://                                                              |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                              | https://                                                              |
| fsmlite                       | https://github.com/tkem/fsmlite                                                     | https://                                                              |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                           | https://                                                              |
| funcy                         | https://github.com/Suor/funcy                                                       | https://                                                              |
| gast                          | https://github.com/serge-sans-paille/gast/                                          | https://                                                              |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                | https://                                                              |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             | https://                                                              |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https://                                                              |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             | https://                                                              |
| genproto                      | https://google.golang.org/genproto/googleapis                                       | https://                                                              |
| geometric                     | https://openbase.com/python/geometric                                               | https://                                                              |
| giflib                        | https://giflib.sourceforge.net                                                      | https://                                                              |
| glib                          | https://docs.gtk.org/glib/                                                          | https://                                                              |
| GLM Library                   | https://github.com/g-truc/glm                                                       | https://                                                              |
| gls                           | https://github.com/jtolds/gls                                                       | https://                                                              |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https://                                                              |
| go-connections                | https://github.com/docker/go-connections                                            | https://                                                              |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https://                                                              |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https://                                                              |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https://                                                              |
| go-ini                        | https://github.com/go-ini/ini                                                       | https://                                                              |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             | https://                                                              |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https://                                                              |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           | https://                                                              |
| go-ole                        | https://github.com/go-ole/go-ole                                                    | https://                                                              |
| go-pg                         | https://github.com/go-pg/pg                                                         | https://                                                              |
| go-redis                      | https://github.com/go-redis/redis/v8                                                | https://                                                              |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                            | https://                                                              |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                            | https://                                                              |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                              | https://                                                              |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                                   | https://                                                              |
| go-units                      | https://github.com/docker/go-units                                                  | https://                                                              |
| go-version                    | https://github.com/hashicorp/go-version                                             | https://                                                              |
| go-zglob                      | https://github.com/mattn/go-zglob                                                   | https://                                                              |
| go.opencensus                 | https://go.opencensus.io                                                            | https://                                                              |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                | https://                                                              |
| goconvey                      | https://github.com/smartystreets/goconvey                                           | https://                                                              |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                       | https://                                                              |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       | https://                                                              |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https://                                                              |
| google-cloud-go               | https://cloud.google.com/go                                                         | https://                                                              |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 | https://                                                              |
| google-pasta                  | https://github.com/google/pasta                                                     | https://                                                              |
| google.golang.org/api         | https://google.golang.org/api                                                       | https://                                                              |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  | https://                                                              |
| Name of Project               | Website                                                                             | License                                                               |
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https://                                                              |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https://                                                              |
| graphviz                      | https://graphviz.org/                                                               | https://                                                              |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https://                                                              |
| groupcache                    | https://github.com/golang/groupcache                                                | https://                                                              |
| grpc                          | https://google.golang.org/grpc                                                      | https://                                                              |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https://                                                              |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https://                                                              |
| $g$ tk2                       | https://gitlab.gnome.org/GNOME/gtk                                                  | https://                                                              |
| gts                           | https://sourceforge.net/projects/gts/                                               | https://                                                              |
| h5py                          | https://www.h5py.org                                                                | https://                                                              |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https://                                                              |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https://                                                              |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https://                                                              |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https://                                                              |
| he                            | https://github.com/mathiasbynens/he                                                 | https://                                                              |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https://                                                              |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https://                                                              |
| htslib                        | https://www.htslib.org                                                              | https://                                                              |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https://                                                              |
| icu                           | https://github.com/unicode-org/icu                                                  | https://                                                              |
| idna                          | https://github.com/kjd/idna                                                         | https://                                                              |
| imageio                       | https://github.com/imageio/imageio                                                  | https://                                                              |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https://                                                              |
| <b>ImmuneBuilder</b>          | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https://                                                              |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https://                                                              |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https://                                                              |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https://                                                              |
| inflection                    | https://github.com/jinzhu/inflection                                                | https://                                                              |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https://                                                              |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https://                                                              |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https://                                                              |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https://                                                              |
| ipykernel                     | https://ipython.org                                                                 | https://                                                              |
| ipython                       | https://ipython.org                                                                 | https://                                                              |
| ipython-genutils              | http://ipython.org                                                                  | https://                                                              |
| ipywidgets                    | http://jupyter.org                                                                  | https://                                                              |
| isodate                       | https://github.com/gweis/isodate/                                                   | https://                                                              |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https://                                                              |
| jax                           | https://github.com/google/jax                                                       | https://                                                              |
| jaxlib                        | https://github.com/google/jax                                                       | https://                                                              |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              | https://                                                              |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https://                                                              |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https://                                                              |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https://                                                              |
| jpeg                          | https://www.ijg.org                                                                 | https://                                                              |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https://                                                              |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https://                                                              |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https://                                                              |
| Name of Project               | Website                                                                             | License                                                               |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:/                                                               |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https:/                                                               |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https:/                                                               |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:/                                                               |
| jstat                         | https://github.com/jstat/jstat                                                      | https:/                                                               |
| jupyter-client                | https://jupyter.org                                                                 | https:/                                                               |
| jupyter-core                  | https://jupyter.org                                                                 | https:/                                                               |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https:/                                                               |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:/                                                               |
| jupyter-server                | http://jupyter.org                                                                  | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE    |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:/                                                               |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:/                                                               |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:/                                                               |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:/                                                               |
| jupyter_client                | http://jupyter.org                                                                  | https:/                                                               |
| jupyter_core                  | http://jupyter.org                                                                  | https:/                                                               |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https:/                                                               |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:/                                                               |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:/                                                               |
| keras                         | https://github.com/keras-team/keras                                                 | https:/                                                               |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:/                                                               |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:/                                                               |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:/                                                               |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:/                                                               |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:/                                                               |
| kombu                         | https://kombu.readthedocs.io                                                        | https:/                                                               |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                       | https:/                                                               |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:/                                                               |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:/                                                               |
| lcms2                         | https://www.littlecms.com                                                           | https:/                                                               |
| lerc                          | https://github.com/Esri/lerc                                                        | https:/                                                               |
| libarchive                    | http://www.libarchive.org                                                           | https:/                                                               |
| libblas                       | https://www.netlib.org/blas/                                                        | https:/                                                               |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:/                                                               |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:/                                                               |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https:/                                                               |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                   |
| libclang                      | Orion Floes                                                                         | https:/                                                               |
| libcurl                       | https://curl.se/libcurl/                                                            | https:/                                                               |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:/                                                               |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:/                                                               |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:/                                                               |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://                                                               |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:/                                                               |
| libffi                        | https://github.com/libffi/libffi                                                    | https:/                                                               |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:/                                                               |
| libgd                         | https://libgd.github.io                                                             | https:/                                                               |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:/                                                               |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https:/                                                               |
| Name of Project               | Website                                                                             | License                                                               |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https:/                                                               |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https:/                                                               |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https:/                                                               |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https:/                                                               |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https:/                                                               |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                               |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https:/                                                               |
| libopenblas                   | https://www.openblas.net/                                                           | https:/                                                               |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https:/                                                               |
| libpq                         | https://www.postgresql.org/                                                         | https:/                                                               |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https:/                                                               |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https:/                                                               |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https:/                                                               |
| libtiff                       | https://www.libtiff.org/                                                            | https:/                                                               |
| libtrust                      | https://github.com/docker/libtrust                                                  | https:/                                                               |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https:/                                                               |
| libuv                         | https://github.com/libuv/libuv                                                      | https:/                                                               |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https:/                                                               |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https:/                                                               |
| libxc                         | https://www.tddft.org/programs/libxc/                                               | https:/                                                               |
| libxcb                        | https://xcb.freedesktop.org                                                         | https:/                                                               |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https:/                                                               |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https:/                                                               |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https:/                                                               |
| libzlib                       | https://zlib.net                                                                    | https:/                                                               |
| lime                          | https://github.com/marcoter/lime                                                    | https:/                                                               |
| llvm                          | http://llvm.org                                                                     | https:/                                                               |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https:/                                                               |
| llvmlite                      | http://llvmlite.readthedocs.io                                                      | https:/                                                               |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https:/                                                               |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https:/                                                               |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https:/                                                               |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/                                                               |
| lxml                          | https://lxml.de                                                                     | https:/                                                               |
| lz4-c                         | https://www.lz4.org/                                                                | https:/                                                               |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https:/                                                               |
| markdown-it-py                | Orion Floes                                                                         | https:/                                                               |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https:/                                                               |
| matplotlib                    | https://matplotlib.org                                                              | https:/                                                               |
| matplotlib-base               | https://matplotlib.org                                                              | https:/                                                               |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https:/                                                               |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/                                                               |
| mdtraj                        | https://www.mdtraj.org/                                                             | https:/                                                               |
| mdurl                         | Orion Floes                                                                         | https:/                                                               |
| menuinst                      | Orion Floes                                                                         | https:/                                                               |
| mergo                         | https://github.com/imdario/mergo                                                    | https:/                                                               |
| mistune                       | https://github.com/lepture/mistune                                                  | https:/                                                               |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https:/                                                               |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https:/                                                               |
| Name of Project               | Website                                                                             | License                                                               |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https:/                                                               |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https:/                                                               |
| ml-dtypes                     | Orion Floes                                                                         | https:/                                                               |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https:/                                                               |
| moment                        | https://github.com/moment/moment                                                    | https:/                                                               |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https:/                                                               |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https:/                                                               |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https:/                                                               |
| mpmath                        | http://mpmath.org/                                                                  | https:/                                                               |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https:/                                                               |
| msgpack                       | https://msgpack.org/                                                                | https:/                                                               |
| multidict                     | https://github.com/aio-libs/multidict                                               | https:/                                                               |
| multierr                      | https://go.uber.org/multierr                                                        | https:/                                                               |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https:/                                                               |
| munkres                       | https://software.clapper.org/munkres/                                               | https:/                                                               |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https:/                                                               |
| namex                         | Orion Floes                                                                         | https:/                                                               |
| nbclassic                     | http://jupyter.org                                                                  | https:/                                                               |
| nbclient                      | https://jupyter.org                                                                 | https:/                                                               |
| nbconvert                     | https://jupyter.org                                                                 | https:/                                                               |
| nbformat                      | http://jupyter.org                                                                  | https:/                                                               |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https:/                                                               |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https:/                                                               |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                               |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https:/                                                               |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https:/                                                               |
| networkx                      | https://networkx.org                                                                | https:/                                                               |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https:/                                                               |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https:/                                                               |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https:/                                                               |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https:/                                                               |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https:/                                                               |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/                                                               |
| nodejs                        | https://nodejs.org/en/                                                              | https:/                                                               |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https:/                                                               |
| notebook                      | http://jupyter.org                                                                  | https:/                                                               |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https:/                                                               |
| notebook_shim                 | http://jupyter.org                                                                  | https:/                                                               |
| numba                         | https://numba.pydata.org                                                            | https:/                                                               |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https:/                                                               |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https:/                                                               |
| numpy                         | https://numpy.org                                                                   | https:/                                                               |
| numpy-base                    | https://numpy.org                                                                   | https:/                                                               |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/                                                               |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                               |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                               |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                               |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                               |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                               |
| Name of Project               | Website                                                                             | License                                                               |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https://                                                              |
| Oat++                         | https://oatpp.io/                                                                   | https://                                                              |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https://                                                              |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https://                                                              |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https://                                                              |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https://                                                              |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https://                                                              |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https://                                                              |
| OpenFF                        | https://openforcefield.org/                                                         | https://                                                              |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https://                                                              |
| openff-forcefields            | https://openforcefield.org                                                          | https://                                                              |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https://                                                              |
| openff-models                 | https://github.com/openforcefield/openff-models                                     | https://                                                              |
| openff-toolkit                | https://openforcefield.org                                                          | https://                                                              |
| openff-toolkit-base           | https://openforcefield.org                                                          | https://                                                              |
| openff-units                  | https://github.com/openforcefield/openff-units                                      | https://                                                              |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https://                                                              |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https://                                                              |
| openldap                      | https://www.openldap.org/software/repo.html                                         | https://                                                              |
| OpenMM                        | https://openmm.org                                                                  | https://                                                              |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https://                                                              |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https://                                                              |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https://                                                              |
| openssl                       | https://www.openssl.org                                                             | https://                                                              |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https://                                                              |
| OptKing                       | https://github.com/psi-rking/optking                                                | https://                                                              |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https://                                                              |
| overrides                     | https://github.com/mkorpela/overrides                                               | https://                                                              |
| packaging                     | https://github.com/pypa/packaging                                                   | https://                                                              |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https://                                                              |
| pandas                        | https://pandas.pydata.org                                                           | https://                                                              |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https://                                                              |
| Name of Project               | Website                                                                             | License                                                               |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https:/                                                               |
| pango                         | https://pango.gnome.org                                                             | https:/                                                               |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https:/                                                               |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                               |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https:/                                                               |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https:/                                                               |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https:/                                                               |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https:/                                                               |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https:/                                                               |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/                                                               |
| pcre                          | https://www.pcre.org                                                                | https:/                                                               |
| pcre2                         | https://www.pcre.org                                                                | https:/                                                               |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https:/                                                               |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https:/                                                               |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https:/                                                               |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https:/                                                               |
| pgio                          | https://github.com/jackc/pgio                                                       | https:/                                                               |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https:/                                                               |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https:/                                                               |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https:/                                                               |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https:/                                                               |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https:/                                                               |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https:/                                                               |
| Pillow                        | https://python-pillow.org                                                           | https:/                                                               |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https:/                                                               |
| pip                           | https://pip.pypa.io/                                                                | https:/                                                               |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https:/                                                               |
| pixman                        | https://pixman.org                                                                  | https:/                                                               |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https:/                                                               |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https:/                                                               |
| plotly                        | https://plotly.com/python/                                                          | https:/                                                               |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https:/                                                               |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https:/                                                               |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/                                                               |
| pooch                         | https://github.com/fatiando/pooch                                                   | https:/                                                               |
| pox                           | https://github.com/uqfoundation/pox                                                 | https:/                                                               |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https:/                                                               |
| pq                            | https://github.com/lib/pq                                                           | https:/                                                               |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https:/                                                               |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https:/                                                               |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/                                                               |
| protobuf                      | https://google.golang.org/protobuf                                                  | https:/                                                               |
| psi4                          | https://psicode.org                                                                 | https:/                                                               |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https:/                                                               |
| psycopg2                      | https://psycopg.org/                                                                | https:/                                                               |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https:/                                                               |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https:/                                                               |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/                                                               |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http://                                                               |
|                               |                                                                                     | Ь                                                                     |
| Name of Project               | Website                                                                             | Licen                                                                 |
| pу                            | https://py.readthedocs.io/en/latest/                                                | https:/                                                               |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             | https:/                                                               |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   | https:/                                                               |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           | https:/                                                               |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  | https:/                                                               |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/                                                               |
| pycosat                       | https://github.com/conda/pycosat                                                    | https:/                                                               |
| pycparser                     | https://github.com/eliben/pycparser                                                 | https:/                                                               |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 | https:/                                                               |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           | https:/                                                               |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                | https:/                                                               |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                | https:/                                                               |
| Pygments                      | https://pygments.org                                                                | https:/                                                               |
| pygraphviz                    | https://pygraphviz.github.io                                                        | https:/                                                               |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            | https:/                                                               |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        | https:/                                                               |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  | https:/                                                               |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   | https:/                                                               |
| pymbar                        | https://pymbar.org                                                                  | https:/                                                               |
| pyOpenSSL                     | https://pyopenssl.org/                                                              | https:/                                                               |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/                                                               |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    | https:/                                                               |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 | https:/                                                               |
| pysam                         | https://github.com/pysam-developers/pysam                                           | https:/                                                               |
| PySocks                       | https://github.com/Anorov/PySocks                                                   | https:/                                                               |
| pytables                      | https://www.pytables.org                                                            | https:/                                                               |
| python                        | https://www.python.org/                                                             | https:/                                                               |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          | https:/                                                               |
| python-constraint             | https://github.com/python-constraint/python-constraint                              | https:/                                                               |
| python-dateutil               | https://dateutil.readthedocs.io                                                     | https:/                                                               |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         | https:/                                                               |
| python-Idap                   | https://www.python-ldap.org/                                                        | https:/                                                               |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            | https:/                                                               |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 | https:/                                                               |
| pytz                          | https://pythonhosted.org/pytz                                                       | https:/                                                               |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/                                                               |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  | https:/                                                               |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                 | https:/                                                               |
| pyyml                         | No longer available                                                                 | No lor                                                                |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             | https:/                                                               |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               | https:/                                                               |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  | https:/                                                               |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        | https:/                                                               |
| ramda                         | https://github.com/ramda/ramda                                                      | https:/                                                               |
| rapidjson                     | https://rapidjson.org/                                                              | https:/                                                               |
| rdkit                         | https://www.rdkit.org                                                               | https:/                                                               |
| re2                           | https://github.com/google/re2                                                       | https:/                                                               |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             | https:/                                                               |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             | https:/                                                               |
|                               |                                                                                     |                                                                       |
| Name of Project               | Website                                                                             | License                                                               |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https:/                                                               |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https:/                                                               |
| reportlab                     | https://www.reportlab.com                                                           | https:/                                                               |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                               |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                               |
| requests                      | https://requests.readthedocs.io                                                     | https:/                                                               |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https:/                                                               |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https:/                                                               |
| resumable                     | https://github.com/stevvooe/resumable                                               | https:/                                                               |
| retrying                      | https://github.com/rholder/retrying                                                 | https:/                                                               |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https:/                                                               |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https:/                                                               |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https:/                                                               |
| rich                          | <b>Orion Floes</b>                                                                  | https:/                                                               |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https:/                                                               |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https:/                                                               |
| rsa                           | https://stuvel.eu/rsa                                                               | https:/                                                               |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/                                                               |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/                                                               |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https:/                                                               |
| sasl                          | https://mellium.im/sasl                                                             | https:/                                                               |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https:/                                                               |
| scikit-image                  | https://scikit-image.org                                                            | https:/                                                               |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https:/                                                               |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/                                                               |
| scipy                         | https://scipy.org                                                                   | https:/                                                               |
| seaborn                       | https://seaborn.pydata.org                                                          | https:/                                                               |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https:/                                                               |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https:/                                                               |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https:/                                                               |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https:/                                                               |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https:/                                                               |
| sh                            | https://github.com/amoffat/sh                                                       | https:/                                                               |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https:/                                                               |
| simint                        | https://www.bennyp.org/research/simint/                                             | https:/                                                               |
| six                           | https://github.com/benjaminp/six                                                    | https:/                                                               |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https:/                                                               |
| snappy                        | https://github.com/google/snappy                                                    | https:/                                                               |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https:/                                                               |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https:/                                                               |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https:/                                                               |
| spglib                        | <b>Orion Floes</b>                                                                  | https:/                                                               |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https:/                                                               |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/                                                               |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/                                                               |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/                                                               |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/                                                               |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/                                                               |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/                                                               |
| Name of Project               | Website                                                                             | License                                                               |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          | https:/                                                               |
| sqlite                        | https://sqlite.org/index.html                                                       | https:/                                                               |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            | https:/                                                               |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             | https:/                                                               |
| starfile                      | https://github.com/alisterburt/starfile                                             | https:/                                                               |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          | https:/                                                               |
| structlog                     | https://www.structlog.org/                                                          | https:/                                                               |
| svglib                        | https://github.com/deeplook/svglib                                                  | https:/                                                               |
| sympy                         | https://sympy.org                                                                   | https:/                                                               |
| tables                        | https://www.pytables.org/                                                           | https:/                                                               |
| tabulate                      | https://github.com/astanin/python-tabulate                                          | https:/                                                               |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                | https:/                                                               |
| tenacity                      | https://github.com/jd/tenacity                                                      | https:/                                                               |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           | https:/                                                               |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           | https:/                                                               |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           | https:/                                                               |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            | https:/                                                               |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             | https:/                                                               |
| tensorflow-io-gcs-filesystem  | <b>Orion Floes</b>                                                                  | https:/                                                               |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           | https:/                                                               |
| termcolor                     | https://github.com/hugovk/termcolor                                                 | https:/                                                               |
| terminado                     | https://github.com/jupyter/terminado                                                | https:/                                                               |
| testpath                      | https://github.com/jupyter/testpath                                                 | https:/                                                               |
| textangular                   | https://github.com/fraywing/textAngular                                             | https:/                                                               |
| tf_keras                      | <b>Orion Floes</b>                                                                  | https:/                                                               |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             | https:/                                                               |
| three                         | https://github.com/mrdoob/three.js                                                  | https:/                                                               |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                | https:/                                                               |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  | https:/                                                               |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             | https:/                                                               |
| tk                            | https://www.tcl.tk/                                                                 | https:/                                                               |
| toml                          | https://github.com/toml-lang/toml                                                   | https:/                                                               |
| tomli                         | https://github.com/hukkin/tomli                                                     | https:/                                                               |
| toolz                         | https://github.com/pytoolz/toolz                                                    | https:/                                                               |
| torch                         | https://pytorch.org/                                                                | https:/                                                               |
| tornado                       | https://www.tornadoweb.org                                                          | https:/                                                               |
| tqdm                          | https://github.com/tqdm/tqdm                                                        | https:/                                                               |
| tracy                         | https://github.com/gear-genomics/tracy                                              | https:/                                                               |
| traitlets                     | https://github.com/ipython/traitlets                                                | https:/                                                               |
| triton                        | https://github.com/openai/triton/                                                   | https:/                                                               |
|                               | <b>Orion Floes</b>                                                                  | https:/                                                               |
| truststore                    |                                                                                     | https:/                                                               |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               | https:/                                                               |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             | https:/                                                               |
| twine                         | https://github.com/pypa/twine                                                       | https:/                                                               |
| twinj uuid                    | https://github.com/twinj/uuid                                                       | https:/                                                               |
| types                         | https://github.com/babel/babel                                                      | https:/                                                               |
| typescript                    | https://github.com/Microsoft/TypeScript                                             | https:/                                                               |
| typing_extensions             | https://github.com/python/typing                                                    | https:/                                                               |
| tzdata                        | https://github.com/python/tzdata                                                    | https:/                                                               |
| Name of Project               | Website                                                                             | License                                                               |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | https://                                                              |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | https://                                                              |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | https://                                                              |
| uritools                      | https://github.com/tkem/uritools/                                                   | https://                                                              |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | https://                                                              |
| vine                          | https://github.com/celery/vine                                                      | https://                                                              |
| vue                           | https://github.com/vuejs/vue                                                        | https://                                                              |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | https://                                                              |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | https://                                                              |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | https://                                                              |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | https://                                                              |
| westpa                        | Orion Floes                                                                         | https://                                                              |
| wheel                         | https://github.com/pypa/wheel                                                       | https://                                                              |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | https://                                                              |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | https://                                                              |
| wsutil                        | https://github.com/yhat/wsutil                                                      | https://                                                              |
| x/lint                        | https://golang.org/x/lint                                                           | https://                                                              |
| x/mod                         | https://golang.org/x/mod/semver                                                     | https://                                                              |
| x/net                         | https://golang.org/x/net                                                            | https://                                                              |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | https://                                                              |
| x/sys                         | https://golang.org/x/sys                                                            | https://                                                              |
| x/text                        | https://golang.org/x/text                                                           | https://                                                              |
| x/tools                       | https://golang.org/x/tools                                                          | https://                                                              |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | https://                                                              |
| xhtml2pdf                     | https://github.com/xhtml2pdf/xhtml2pdf                                              | https://                                                              |
| xlrd                          | https://github.com/python-excel/xlrd                                                | https://                                                              |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | https://                                                              |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | https://                                                              |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https://                                                              |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https://                                                              |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https://                                                              |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https://                                                              |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https://                                                              |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https://                                                              |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https://                                                              |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https://                                                              |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https://                                                              |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https://                                                              |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https://                                                              |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https://                                                              |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | https://                                                              |
| xz                            | https://github.com/ulikunitz/xz                                                     | https://                                                              |
| yaml                          | https://pyyaml.org/                                                                 | https://                                                              |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  | https://                                                              |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | https://                                                              |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | https://                                                              |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | https://                                                              |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | https://                                                              |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | Commercial                                                            |
| Name of Project               | Website                                                                             | License                                                               |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                                                                   |
| zap                           | https://go.uber.org/zap                                                             | https://                                                              |
| zipp                          | https://github.com/jaraco/zipp                                                      | https://                                                              |
| zlib                          | https://zlib.net/                                                                   | https://                                                              |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https://                                                              |
| zstd                          | https://facebook.github.io/zstd/                                                    | https://                                                              |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https://                                                              |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https://                                                              |

## **9.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

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
\rightarrownotice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

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

#### See also:

• http://www.gnu.org/licenses/gpl.txt

## **INDEX**

# A

ApplyCharges OEProton:: OEDesignUnitCharges, 32 applycharges\_oedu.py Example Code, 19 assigncharges.py Example Code, 12

# C

CalcAM1 OEMolAM1:: OEAM1, 66 OEMolAM1::OEOptimizedAM1,71 CalculateNumOfMicrostates OEProton:: OEMultistatepKaModel, 75 CheckCharges OEProton:: OEChargeEngineBase, 28 Constructors OEMolAM1:: OEAM1, 65 OEMolAM1:: OEAM1Options, 67 OEMolAM1:: OEAM1Results, 68 OEMolAM1::OEOptimizedAM1,70 OEProton:: OEAM1BCCCharges, 23 OEProton:: OEAM1BCCELF10Charges, 25 OEProton:: OEAM1Charges, 26 OEProton:: OEAmberFF94Charges, 27 OEProton:: OEChargeEngineNoOp, 30 OEProton:: OEChargeParameter, 74 OEProton:: OEClearCharges, 30 OEProton:: OECombineChargeEngines, 31 OEProton:: OEDesignUnitCharges, 32 OEProton:: OEELF, 35 OEProton:: OEELFCharges, 35 OEProton:: OEELFOptions, 37 OEProton:: OEFormalChargeOptions, 38 OEProton:: OEFormalToPartialCharges, 39 OEProton:: OEGasteigerCharges, 40 OEProton:: OEInitialCharges, 40 OEProton:: OEMMFF94Charges, 41 OEProton:: OEMultistatepKaModel, 75 OEProton:: OEMultistatepKaModelOptions, 77

OEProton:: OESpreadMetalCharges, 41 OEProton:: OETautomerMolFunction, 49 OEProton:: OETautomerOptions, 43 OEProton:: OETyperMolFunction, 50 CreateCopy OEProton:: OEChargeEngineBase, 28 OEProton:: OEDesignUnitCharges, 32 OEProton:: OESpreadMetalCharges, 42 OEProton:: OETautomerMolFunction, 49 OEProton:: OETyperMolFunction, 50

## F

enumerateionizationstatesatneutralph.py Example Code, 21 Example Code applycharges\_oedu.py, 19 assigncharges.py, 12 enumerateionizationstatesatneutralph.py, 21 getreasonabletautomers.py, 15 neutralionization.py.14 setreasonablechargestate.py, 17 wibergbondorders.py, 18

## G

GenerateMicrostates OEProton:: OEMultistatepKaModel, 76 GetApplyWarts OEProton:: OETautomerOptions, 43 GetAtomAdjTypeAtNeutralpH OEProton:: OEMultistatepKaModel, 76 GetAtomicBondOrder OEMolAM1:: OEAM1Results, 69 GetAtompKaRange OEProton:: OEMultistatepKaModel, 75 GetBondOrder OEMolAM1:: OEAM1Results, 69 GetBondOrders OEMolAM1:: OEAM1Results, 69 GetCarbonHybridization OEProton:: OETautomerOptions, 44 GetChargeAliquot

OEProton:: OESpreadMetalCharges, 42 GetCharges OEMolAM1:: OEAM1Results, 69 GetClearCoordinates OEProton:: OETautomerOptions, 44 GetCount OEProton:: OETautomerMolFunction, 49 GetElfLimit OEProton:: OEELFOptions, 37 GetEnergy OEMolAM1:: OEAM1Results, 69 GetExpectValidMol OEProton:: OEChargeEngineBase, 28 GetHybridizationLevel OEProton:: OETautomerOptions, 44 GetKekule OEProton:: OETautomerOptions, 44 GetLevel OEProton:: OETautomerOptions, 44 GetLimit OEProton:: OEELFCharges, 36 GetMaxCount OEProton:: OEFormalChargeOptions, 38 GetMaxNbrDist OEProton:: OESpreadMetalCharges, 42 GetMaxNumMicrostates OEProton:: OEMultistatepKaModelOptions, 78 GetMaxScfIter OEMolAM1:: OEAM1Options, 67 GetMaxSearchTime OEProton:: OETautomerOptions, 44 GetMaxTautomericAtoms OEProton:: OETautomerOptions, 45 GetMaxTautomersGenerated OEProton:: OETautomerOptions, 45 GetMaxTautomersToReturn OEProton:: OETautomerOptions, 45 GetMaxZoneSize OEProton:: OETautomerOptions, 45 GetMicrostates OEProton:: OEMultistatepKaModel, 76 GetModelMolecule OEProton:: OEMultistatepKaModel, 75 GetMolecule OEProton:: OETautomerMolFunction, 50 GetName OEProton:: OEChargeEngineBase, 28 GetNumericGradDelta OEMolAM1:: OEAM1Options, 67 GetNumSCFCycles OEMolAM1:: OEAM1Results, 70 GetOptimize OEProton:: OEAM1BCCCharges, 23

OEProton:: OEAM1Charges, 26 GetOptions OEMolAM1:: OEAM1, 66 GetPercent OEProton:: OEELFOptions, 37 GetPercentage OEProton:: OEELFCharges, 36 GetPermissiveBCCs OEProton:: OEAM1BCCCharges, 24 GetpH OEProton:: OEMultistatepKaModelOptions, 77 GetProcessCarbons OEProton::OEMultistatepKaModelOptions, 78 GetRacemicType OEProton:: OETautomerOptions, 45 GetRadiusMargin OEProton:: OESpreadMetalCharges, 42 GetRankTautomers OEProton:: OETautomerOptions, 45 getreasonabletautomers.py Example Code, 15 GetRepairRequestedHint OEProton:: OEChargeEngineBase, 29 GetRequirements OEProton:: OEChargeEngineBase, 29 GetResults OEMolAM1::OEAM1,66 GetReturnSelectedConfs OEProton:: OEELFCharges, 36 GetSaveStereo OEProton:: OETautomerOptions, 46 GetSCFTolerance OEMolAM1:: OEAM1Options, 67 GetSemiMethod OEMolAM1:: OEAM1Options, 67 GetSizeLimit OEProton:: OEAM1BCCCharges, 24 OEProton:: OEAM1Charges, 26 GetSymmetrize OEProton:: OEAM1BCCCharges, 24 OEProton:: OEAM1Charges, 26 GetVerbose OEProton:: OEFormalChargeOptions, 38 GetWarts OEProton:: OEFormalChargeOptions, 38

## H

HasAdjTypeAtNeutralpH OEProton:: OEMultistatepKaModel, 76 HaspKaRange OEProton:: OEMultistatepKaModel, 76

# $\mathbf{I}$

Init OEProton:: OEMultistatepKaModel, 75 IsConverged OEMolAM1:: OEAM1Results, 70 IsValid OEProton:: OEChargeEngineBase, 29 OEProton:: OEDesignUnitCharges, 33

## N

neutralionization.py Example Code, 14

## O

OEAM1BCC:: OEBCCPartialCharges, 72 OEAM1BCC:: OEBCCType, 71 OEAM1BCC:: OEBCCType:: AM1, 71 OEAM1BCC:: OEBCCType::PM3,72 OEAM1BCC:: OESymmetrizePartialCharges, 72 OEMolAM1:: OEAM1, 65 CalcAM1, 66 Constructors, 65 GetOptions, 66 GetResults, 66 operator= $,66$ OEMolAM1:: OEAM1Options, 66 Constructors, 67 GetMaxScfIter, 67 GetNumericGradDelta. 67 GetSCFTolerance, 67 GetSemiMethod, 67 operator=, 67 SetMaxScfIter, 67 SetNumericGradDelta, 68 SetSCFTolerance, 68 SetSemiMethod, 68 OEMolAM1:: OEAM1Results, 68 Constructors, 68 GetAtomicBondOrder, 69 GetBondOrder, 69 GetBondOrders, 69 GetCharges, 69 GetEnergy, 69 GetNumSCFCycles, 70 IsConverged, 70 operator=, 69 OEMolAM1:: OEMethodType, 71 OEMolAM1::OEMethodType::AM1,71 OEMolAM1::OEMethodType::PM3,71 OEMolAM1:: OEOptimizedAM1, 70 CalcAM1, 71 Constructors, 70 operator=, 70

OEProton:: OEAdjTypeAtNeutralpH, 78 OEProton:: OEAdjTypeAtNeutralpH:: Deprotonation, 79 OEProton::OEAdjTypeAtNeutralpH::NoChange, 79 OEProton::OEAdjTypeAtNeutralpH::NoChangeAndDeprotor 79 OEProton::OEAdjTypeAtNeutralpH::NoChangeAndProtonat 79 OEProton:: OEAdjTypeAtNeutralpH:: Protonation, 79 OEProton:: OEAdjTypeAtNeutralpH:: Unknown, 79 OEProton:: OEAM1BCCCharges, 23 Constructors, 23 GetOptimize, 23 GetPermissiveBCCs, 24 GetSizeLimit, 24 GetSymmetrize, 24 SetOptimize, 24 SetPermissiveBCCs, 24 SetSizeLimit, 24 SetSymmetrize, 24 OEProton:: OEAM1BCCELF10Charges, 25 Constructors, 25 OEProton:: OEAM1Charges, 25 Constructors, 26 GetOptimize, 26 GetSizeLimit, 26 GetSymmetrize, 26 SetOptimize, 26 SetSizeLimit, 26 SetSymmetrize, 26 OEProton:: OEAmberFF94Charges, 27 Constructors, 27 OEProton:: OEAssignCharges, 57 OEProton:: OEAssignPartialCharges, 58 OEProton:: OEChargeEngineBase, 27 CheckCharges, 28 CreateCopy, 28 GetExpectValidMol, 28 GetName, 28 GetRepairRequestedHint, 29 GetRequirements, 29 IsValid, 29 operator!=,  $28$ operator==,  $28$ SetExpectValidMol, 29 SetRepairRequestedHint, 29 TransferCharge, 29 OEProton:: OEChargeEngineNoOp, 30 Constructors, 30 OEProton:: OEChargeParameter, 73 Constructors, 74

operator=, 74 OEProton::OEChargingRequirement::SizeWithinLimits, OEProton:: OECharges, 51 56 OEProton:: OEChargingRequirement:: StandardResidues, OEProton:: OECharges:: AM1, 51 OEProton:: OECharges:: AM1BCC, 51 56 OEProton:: OECharges:: AM1BCCNoSym, 51 OEProton:: OEClearCharges, 30 OEProton:: OECharges:: AM1BCCNoSymSPt, 51 Constructors, 30 OEProton:: OECharges:: AM1BCCSPt, 52 OEProton:: OECombineChargeEngines, 31 OEProton:: OECharges:: AM1BCCSym, 52 Constructors, 31 OEProton:: OECharges:: AM1BCCSymSPt, 52 OEProton:: OEDesignUnitCharges, 31 OEProton:: OECharges:: AM1SPt, 52 ApplyCharges, 32 OEProton:: OECharges:: AmberFF94, 52 Constructors, 32 OEProton:: OECharges:: AmberFF99, 52 CreateCopy, 32 OEProton:: OECharges:: AmberFF99bsc0, 53 IsValid, 33 operator=, 32 OEProton:: OECharges:: AmberFF99SB, 52 OEProton:: OECharges:: Default, 53 SetCoFactorChargeEngine, 33 OEProton:: OECharges:: Formal, 53 SetFallbackChargeEngine, 33 OEProton:: OECharges:: Gasteiger, 53 SetFinalizationChargeEngine, 33 OEProton:: OECharges:: Initial, 53 SetLigandChargeEngine, 33 OEProton:: OECharges:: Max, 53 SetMetalChargeEngine, 33 OEProton:: OECharges:: MMFF94, 53 SetNucleicChargeEngine, 33 OEProton:: OECharges:: None, 54 SetOtherChargeEngine, 34 OEProton:: OECharges:: NoOp, 53 SetProteinChargeEngine, 34 OEProton:: OECharges:: OPLS, 54 SetProteinNonStandardChargeEngine, OEProton:: OEChargingRequirement, 54 34 OEProton::OEChargingRequirement::AltersResidSuetNscmlexentChargeEngine, 34 54 TransferCharge, 34 OEProton::OEChargingRequirement::BondedResidUsesSZMAPWaterModel, 34 54 OEProton:: OEELF, 34 OEProton::OEChargingRequirement::Compact, Constructors, 35 operator=, 35 54 OEProton:: OEChargingRequirement:: Coords3D, Select, 35 54 OEProton:: OEELFCharges, 35 OEProton:: OEChargingRequirement:: ExplicitHydrompermsuctors, 35 54 GetLimit, 36 OEProton:: OEChargingRequirement:: MolComplexEeepRercentage. 36 GetReturnSelectedConfs, 36 55 OEProton:: OEChargingRequirement:: MultiConfOnSextLimit, 36 55 SetPercentage, 36 OEProton:: OEChargingRequirement:: Nothing, SetReturnSelectedConfs, 36 55 OEProton:: OEELFOptions, 37 OEProton:: OEChargingRequirement:: Parameters, Constructors, 37 55 GetElfLimit, 37 OEProton:: OEChargingRequirement:: PDBOrder, GetPercent, 37 55 operator=, 37 OEProton:: OEChargingRequirement:: Precharged, SetElfLimit, 37 SetPercent, 38 55 OEProton::OEChargingRequirement::ResPerc@EDedton::OEEnumerateFormalCharges, 59 OEProton:: OEEnumerateTautomers, 60 55 OEProton::OEChargingRequirement::ReturnS@EBrotedfonfingFormalChargeOptions, 38 55 Constructors, 38 OEProton:: OEChargingRequirement:: SetsAromatfetMaxCount, 38 55 GetVerbose, 38 OEProton:: OEChargingRequirement:: SetsType, GetWarts, 38 55 operator=, 38

```
SetMaxCount, 39
                                               GetpH, 77
   SetVerbose. 39
                                               GetProcessCarbons, 78
   SetWarts, 39
                                               SetMaxNumMicrostates, 78
OEProton:: OEFormalToPartialCharges, 39
                                               SetpH, 77
   Constructors, 39
                                               SetProcessCarbons, 78
OEProton:: OEGasteigerCharges, 40
                                           OEProton:: OEMultistatepKaModelpH, 79
   Constructors, 40
                                           OEProton:: OEMultistatepKaModelpH:: Neutral,
OEProton::OEGetAtomAdjTypeAtNeutralpHName,
                                                   80
       81
                                           OEProton::OEMultistatepKaModelpH::Unknown,
OEProton::OEGetAtomAdjTypeAtNeutralpHType,
                                                   80
       81
                                           OEProton:: OEpKaRange, 80
OEProton:: OEGetAtompKaRangeName, 81
                                           OEProton:: OEpKaRange:: Acidic, 80
OEProton:: OEGetAtompKaRangeType, 81
                                           OEProton:: OEpKaRange:: Basic, 80
                                           OEProton:: OEpKaRange:: Neutral, 80
OEProton:: OEGetChargeTypeName, 60
OEProton:: OEGetMultistatepKaModelpHName, OEProton:: OEpKaRange:: Unidentified, 80
       82
                                           OEProton:: OEpKaRange:: Unknown, 81
OEProton::OEGetMultistatepKaModelpHType, OEProton::OEQuacPacGetArch, 63
                                           OEProton:: OEQuacPacGetLicensee, 63
       82
OEProton:: OEGetReasonableProtomer. 61
                                           OEProton:: OEQuacPacGetPlatform, 63
OEProton:: OEGetReasonableProtomers, 61
                                           OEProton:: OEQuacPacGetRelease, 63
OEProton:: OEGetReasonableTautomers, 61
                                           OEProton:: OEQuacPacGetSite, 63
OEProton:: OEGetUniqueProtomer, 62
                                           OEProton:: OEQuacPacGetVersion, 63
OEProton:: OEHybridizationLevel, 56
                                           OEProton:: OEQuacPacIsLicensed, 64
OEProton:: OEHybridizationLevel:: Default. OEProton:: OERacemicType. 56
       56
                                           OEProton:: OERacemicType:: Default, 57
OEProton::OEHybridizationLevel::DoubleBofidNbwton::OERacemicType::EverSampled,
       56
                                                   57
OEProton::OEHybridizationLevel::EnolEnam@E@poton::OERacemicType::LocalSampled,
       56
                                                   57
OEProton::OEHybridizationLevel::OriginalQEProton::OERacemicType::None, 57
       56
                                           OEProton:: OERemoveFormalCharge, 64
OEProton:: OEHypervalentNormalization,
                                           OEProton:: OESetNeutralpHModel, 64
                                           OEProton:: OESpreadMetalCharges, 41
       62
OEProton:: OEInitialCharges, 40
                                               Constructors, 41
   Constructors, 40
                                               CreateCopy, 42
OEProton:: OEMMFF94Charges, 41
                                               GetChargeAliquot, 42
   Constructors, 41
                                               GetMaxNbrDist, 42
OEProton:: OEMultistatepKaModel, 74
                                               GetRadiusMargin, 42
   CalculateNumOfMicrostates, 75
                                               SetChargeAliquot, 42
   Constructors, 75
                                               SetMaxNbrDist, 42
   GenerateMicrostates, 76
                                               SetRadiusMargin, 43
                                           OEProton:: OETautomerMolFunction, 49
   GetAtomAdjTypeAtNeutralpH, 76
   GetAtompKaRange, 75
                                               Constructors, 49
   GetMicrostates, 76
                                               CreateCopy, 49
   GetModelMolecule, 75
                                               GetCount, 49
   HasAdjTypeAtNeutralpH, 76
                                               GetMolecule, 50
   HaspKaRange, 76
                                               operator(), 49
   Init.75
                                               Reset. 50
   operator=,75OEProton:: OETautomerOptions, 43
   SetAllAtomspKaData, 76
                                               Constructors, 43
OEProton:: OEMultistatepKaModelOptions,
                                               GetApplyWarts, 43
                                               GetCarbonHybridization, 44
       77
   Constructors.77
                                               GetClearCoordinates, 44
                                               GetHybridizationLevel, 44
   GetMaxNumMicrostates, 78
```

GetKekule, 44 GetLevel. 44 GetMaxSearchTime, 44 GetMaxTautomericAtoms, 45 GetMaxTautomersGenerated, 45 GetMaxTautomersToReturn, 45 GetMaxZoneSize.45 GetRacemicType, 45 GetRankTautomers, 45 GetSaveStereo, 46 operator=, 43 SetApplyWarts, 46 SetCarbonHybridization, 46 SetClearCoordinates, 46 SetHybridizationLevel, 46 SetKekule, 47 SetLevel, 47 SetMaxSearchTime, 47 SetMaxTautomericAtoms, 47 SetMaxTautomersGenerated, 47 SetMaxTautomersToReturn, 48 SetMaxZoneSize, 48 SetRacemicType, 48 SetRankTautomers. 48 SetSaveStereo, 48 OEProton:: OETautomersLargestZoneSize, 64 OEProton:: OETyperMolFunction, 50 Constructors, 50 CreateCopy, 50 operator $($ ), 50 Reset. 51  $operator! =$ OEProton:: OEChargeEngineBase, 28 operator() OEProton:: OETautomerMolFunction, 49 OEProton:: OETyperMolFunction, 50 operator= OEMolAM1:: OEAM1, 66 OEMolAM1:: OEAM1Options, 67 OEMolAM1:: OEAM1Results, 69 OEMolAM1::OEOptimizedAM1,70 OEProton:: OEChargeParameter, 74 OEProton:: OEDesignUnitCharges, 32 OEProton:: OEELF, 35 OEProton:: OEELFOptions, 37 OEProton:: OEFormalChargeOptions, 38 OEProton:: OEMultistatepKaModel, 75 OEProton:: OETautomerOptions, 43 operator== OEProton:: OEChargeEngineBase, 28

## R

Reset

OEProton:: OETautomerMolFunction, 50 OEProton:: OETyperMolFunction, 51

## S

Select OEProton:: OEELF, 35 SetAllAtomspKaData OEProton:: OEMultistatepKaModel, 76 SetApplyWarts OEProton:: OETautomerOptions, 46 SetCarbonHybridization OEProton:: OETautomerOptions, 46 SetChargeAliquot OEProton:: OESpreadMetalCharges, 42 SetClearCoordinates OEProton:: OETautomerOptions, 46 SetCoFactorChargeEngine OEProton:: OEDesignUnitCharges, 33 SetElfLimit OEProton:: OEELFOptions, 37 SetExpectValidMol OEProton:: OEChargeEngineBase, 29 SetFallbackChargeEngine OEProton:: OEDesignUnitCharges, 33 SetFinalizationChargeEngine OEProton:: OEDesignUnitCharges, 33 SetHybridizationLevel OEProton:: OETautomerOptions, 46 SetKekule OEProton:: OETautomerOptions, 47 SetLevel OEProton:: OETautomerOptions, 47 SetLigandChargeEngine OEProton:: OEDesignUnitCharges, 33 SetLimit OEProton:: OEELFCharges, 36 SetMaxCount OEProton:: OEFormalChargeOptions, 39 SetMaxNbrDist OEProton:: OESpreadMetalCharges, 42 SetMaxNumMicrostates OEProton:: OEMultistatepKaModelOptions, 78 SetMaxScfIter OEMolAM1:: OEAM1Options, 67 SetMaxSearchTime OEProton:: OETautomerOptions, 47 SetMaxTautomericAtoms OEProton:: OETautomerOptions, 47 SetMaxTautomersGenerated OEProton:: OETautomerOptions, 47 SetMaxTautomersToReturn OEProton:: OETautomerOptions, 48 SetMaxZoneSize

OEProton:: OETautomerOptions, 48 SetMetalChargeEngine OEProton:: OEDesignUnitCharges, 33 SetNucleicChargeEngine OEProton:: OEDesignUnitCharges, 33 SetNumericGradDelta OEMolAM1:: OEAM1Options, 68 SetOptimize OEProton:: OEAM1BCCCharges, 24 OEProton:: OEAM1Charges, 26 SetOtherChargeEngine OEProton:: OEDesignUnitCharges, 34 SetPercent OEProton:: OEELFOptions, 38 SetPercentage OEProton:: OEELFCharges, 36 SetPermissiveBCCs OEProton:: OEAM1BCCCharges, 24 SetpH OEProton:: OEMultistatepKaModelOptions, 77 SetProcessCarbons OEProton:: OEMultistatepKaModelOptions, 78 SetProteinChargeEngine OEProton:: OEDesignUnitCharges, 34 SetProteinNonStandardChargeEngine OEProton:: OEDesignUnitCharges, 34 SetRacemicType OEProton:: OETautomerOptions, 48 SetRadiusMargin OEProton:: OESpreadMetalCharges, 43 SetRankTautomers OEProton:: OETautomerOptions, 48 setreasonablechargestate.py Example Code, 17 SetRepairRequestedHint OEProton:: OEChargeEngineBase, 29 SetReturnSelectedConfs OEProton:: OEELFCharges, 36 SetSaveStereo OEProton:: OETautomerOptions, 48 SetSCFTolerance OEMolAM1:: OEAM1Options, 68 SetSemiMethod OEMolAM1:: OEAM1Options, 68 SetSizeLimit OEProton:: OEAM1BCCCharges, 24 OEProton:: OEAM1Charges, 26 SetSolventChargeEngine OEProton:: OEDesignUnitCharges, 34 SetSymmetrize OEProton:: OEAM1BCCCharges, 24 OEProton:: OEAM1Charges, 26

SetVerbose OEProton:: OEFormalChargeOptions, 39 SetWarts OEProton:: OEFormalChargeOptions, 39

## Т

TransferCharge OEProton:: OEChargeEngineBase, 29 OEProton:: OEDesignUnitCharges, 34

## $\mathbf{U}$

UseSZMAPWaterModel OEProton:: OEDesignUnitCharges, 34

## W

wibergbondorders.py Example Code, 18