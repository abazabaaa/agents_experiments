![](_page_0_Picture_0.jpeg)

# **Lexichem TK - Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

## **CONTENTS**

|  | 1 Theory   |        |                                                      |   |
|--|------------|--------|------------------------------------------------------|---|
|  | 1.1        |        | Input Name Representation                            |   |
|  | 1.2        |        | Output Name Representation                           |   |
|  |            | 1.2.1  | Enhanced Stereochemistry                             |   |
|  |            | 1.2.2  | Isotopes                                             |   |
|  | 1.3        |        | Output Name Styles                                   |   |
|  | 1.4        |        | Examples of Name Style Differences                   |   |
|  |            | 1.4.1  | Example OpenEye vs. IUPAC vs. Systematic Differences |   |
|  |            | 1.4.2  | Example OpenEye/IUPAC vs. CAS Differences            |   |
|  |            | 1.4.3  | Example OpenEye/IUPAC vs. Traditional Differences    |   |
|  | 2 Examples |        |                                                      | 1 |
|  | 2.1        |        | Lexichem TK Examples                                 | 1 |
|  |            | 2.1.1  | Converting Molecules to Names                        | 1 |
|  |            | 2.1.2  | Converting Names to Molecules                        | 1 |
|  |            | 2.1.3  | Translating Names Between Languages                  | 1 |
|  | 3 API      |        |                                                      | 2 |
|  | 3.1        |        | OEIUPAC Constants                                    | 2 |
|  |            | 3.1.1  | OECharSet                                            | 2 |
|  |            | 3.1.2  | OEIUPAC                                              | 2 |
|  |            | 3.1.3  | OELanguage                                           | 2 |
|  | 3.2        |        | OEIUPAC Functions                                    | 2 |
|  |            | 3.2.1  | OECapitalizeName                                     | 2 |
|  |            | 3.2.2  | OECreateIUPACName                                    | 2 |
|  |            | 3.2.3  | OEFromBritish                                        | 2 |
|  |            | 3.2.4  | OEFromChinese                                        | 3 |
|  |            | 3.2.5  | OEFromDanish                                         | 3 |
|  |            | 3.2.6  | OEFromDutch                                          | 3 |
|  |            | 3.2.7  | OEFromFrench                                         | 3 |
|  |            | 3.2.8  | OEFromGerman                                         | 3 |
|  |            | 3.2.9  | OEFromGreek                                          | 3 |
|  |            | 3.2.10 | OEFromHTML                                           | 3 |
|  |            | 3.2.11 | OEFromHungarian                                      | 3 |
|  |            | 3.2.12 | OEFromIrish                                          | 3 |
|  |            | 3.2.13 | OEFromItalian                                        | 3 |
|  |            | 3.2.14 | OEFromJapanese                                       | 3 |
|  |            | 3.2.15 | OEFromKOI8R                                          | 3 |
|  |            | 3.2.16 | OEFromLanguage                                       | 3 |
|  |            | 3.2.17 | OEFromLatin1                                         | 3 |

| 3.2.18                   | OEFromPolish        | 32 |
|--------------------------|---------------------|----|
| 3.2.19                   | OEFromRomanian      | 32 |
| 3.2.20                   | OEFromRussian       | 32 |
| 3.2.21                   | OEFromSlovak        | 33 |
| 3.2.22                   | OEFromSpanish       | 33 |
| 3.2.23                   | OEFromSwedish       | 33 |
| 3.2.24                   | OEFromUTF8          | 33 |
| 3.2.25                   | OEFromWelsh         | 33 |
| 3.2.26                   | OEGetCIPStereo      | 33 |
| 3.2.27                   | OEGetIUPACCharSet   | 34 |
| 3.2.28                   | OEGetIUPACLanguage  | 34 |
| 3.2.29                   | OEGetIUPACNameStyle | 34 |
| 3.2.30                   | OEIUPACGetArch      | 34 |
| 3.2.31                   | OEIUPACGetLicensee  | 34 |
| 3.2.32                   | OEIUPACGetPlatform  | 34 |
| 3.2.33                   | OEIUPACGetRelease   | 35 |
| 3.2.34                   | OEIUPACGetSite      | 35 |
| 3.2.35                   | OEIUPACGetVersion   | 35 |
| 3.2.36                   | OEIUPACIsLicensed   | 35 |
| 3.2.37                   | OELowerCaseName     | 35 |
| 3.2.38                   | OENameLocant        | 36 |
| 3.2.39                   | OEParseIUPACName    | 36 |
| 3.2.40                   | OEReorderIndexName  | 36 |
| 3.2.41                   | OESetCIPStereo      | 36 |
| 3.2.42                   | OEToASCII           | 36 |
| 3.2.43                   | OEToBritish         | 37 |
| 3.2.44                   | OEToChinese         | 37 |
| 3.2.45                   | OEToDanish          | 37 |
| 3.2.46                   | OEToDutch           | 37 |
| 3.2.47                   | OEToEUCJP           | 37 |
| 3.2.48                   | OEToFrench          | 38 |
| 3.2.49                   | OEToGerman          | 38 |
| 3.2.50                   | OEToGreek           | 38 |
| 3.2.51                   | OEToHTML            | 38 |
| 3.2.52                   | OEToHungarian       | 38 |
| 3.2.53                   | OEToIrish           | 38 |
| 3.2.54                   | OEToItalian         | 39 |
| 3.2.55                   | OEToJapanese        | 39 |
| 3.2.56                   | OEToLanguage        | 39 |
| 3.2.57                   | OEToLatin1          | 39 |
| 3.2.58                   | OEToPolish          | 39 |
| 3.2.59                   | OEToRomanian        | 40 |
| 3.2.60                   | OEToRussian         | 40 |
| 3.2.61                   | OEToSJIS            | 40 |
| 3.2.62                   | OEToSlovak          | 40 |
| 3.2.63                   | OEToSpanish         | 40 |
| 3.2.64                   | OEToSwedish         | 40 |
| 3.2.65                   | OEToUTF8            | 41 |
| 3.2.66                   | OEToWelsh           | 41 |
| <b>4 Release History</b> |                     | 43 |
| 4.1                      | Lexichem TK 2.9.2   | 43 |
| 4.2                      | Lexichem TK 2.9.1   | 43 |
| 4.3                      | Lexichem TK 2.9.0   | 43 |

| Section                               | Page                       |    |
|---------------------------------------|----------------------------|----|
| 4.3.1 Minor bug fixes                 | 4                          |    |
| 4.4 Lexichem TK 2.8.1                 | 4                          |    |
| 4.5 Lexichem TK 2.8.0                 | 4                          |    |
| 4.5.1 New features                    | 4                          |    |
| 4.5.2 Major bug fixes                 | 4                          |    |
| 4.5.3 Minor bug fixes                 | 4                          |    |
| 4.6 Lexichem TK 2.7.5                 | 4                          |    |
| 4.6.1 New features                    | 4                          |    |
| 4.6.2 Minor bug fixes                 | 4                          |    |
| 4.7 Lexichem TK 2.7.4                 | 4                          |    |
| 4.7.1 New features                    | 4                          |    |
| 4.7.2 Major bug fixes                 | 4                          |    |
| 4.7.3 Minor bug fixes                 | 4                          |    |
| 4.8 Lexichem TK 2.7.3                 | 4                          |    |
| 4.8.1 New features                    | 4                          |    |
| 4.8.2 Major bug fixes                 | 4                          |    |
| 4.9 Lexichem TK 2.7.2                 | 4                          |    |
| 4.9.1 Minor bug fixes                 | 4                          |    |
| 4.10 Lexichem TK 2.7.1                | 4                          |    |
| 4.11 Lexichem TK 2.7.0                | 4                          |    |
| 4.12 Lexichem TK 2.6.7                | 4                          |    |
| 4.13 Lexichem TK 2.6.6                | 4                          |    |
| 4.14 Lexichem TK 2.6.5                | 4                          |    |
| 4.14.1 Minor bug fixes                | 4                          |    |
| 4.14.2 Documentation changes          | 4                          |    |
| 4.15 Lexichem TK 2.6.4                | 4                          |    |
| 4.16 Lexichem TK 2.6.3                | 4                          |    |
| 4.16.1 Minor bug fixes                | 4                          |    |
| 4.17 Lexichem TK 2.6.2                | 4                          |    |
| 4.17.1 New features                   | 4                          |    |
| 4.18 Lexichem TK 2.6.1                | 4                          |    |
| 4.18.1 Minor bug fixes                | 4                          |    |
| 4.19 Lexichem TK 2.6.0                | 4                          |    |
| 4.19.1 New features                   | 4                          |    |
| 4.19.2 Major bug fixes                | 4                          |    |
| 4.19.3 Minor bug fixes                | 4                          |    |
| 4.19.4 Documentation changes          | 4                          |    |
| 4.20 Lexichem TK 2.5.2                | 4                          |    |
| 4.20.1 Major bug fixes                | 4                          |    |
| 4.20.2 Minor bug fixes                | 4                          |    |
| 4.21 Lexichem TK 2.5.1                | 4                          |    |
| 4.21.1 New features                   | 4                          |    |
| 4.21.2 Major bug fixes                | 4                          |    |
| 4.21.3 Minor bug fixes                | 4                          |    |
| 4.21.4 Documentation changes          | 4                          |    |
| 4.22 Lexichem TK 2.5.0                | 4                          |    |
| 4.22.1 New features                   | 4                          |    |
| 4.22.2 Bug fixes                      | 4                          |    |
| 4.23 Lexichem TK 2.4.2                | 4                          |    |
| 4.23.1 Important note                 | 4                          |    |
| 4.23.2 New features                   | 4                          |    |
| 4.23.3 Minor bug fixes                | 4                          |    |
| 4.23.4 Documentation fixes            | 4                          |    |
| 4.24 Lexichem TK 2.4.1                | 5                          |    |
| Section                               | Page                       |    |
| 4.24.1 Minor bug fixes                | 50                         |    |
| 4.25 Lexichem TK 2.4.0                | 50                         |    |
| 4.25.1 New features                   | 50                         |    |
| 4.25.2 Minor bug fixes                | 50                         |    |
| 4.26 Lexichem TK 2.3.2                | 51                         |    |
| 4.26.1 New features                   | 51                         |    |
| 4.26.2 Major bug fixes                | 51                         |    |
| 4.26.3 Minor bug fixes                | 51                         |    |
| 4.27 Lexichem TK 2.3.0                | 51                         |    |
| 4.27.1 New features                   | 51                         |    |
| 4.27.2 Minor bug fixes                | 51                         |    |
| 4.28 Lexichem TK 2.2.3                | 52                         |    |
| 4.28.1 New features                   | 52                         |    |
| 4.28.2 Minor bug fixes                | 52                         |    |
| 4.29 Lexichem TK 2.2.2                | 53                         |    |
| 4.29.1 Bug fixes                      | 53                         |    |
| 4.30 Lexichem TK 2.2.0                | 53                         |    |
| 4.30.1 Feature Requests               | 53                         |    |
| 4.30.2 Bug fixes                      | 53                         |    |
| 4.31 Lexichem TK 2.1.2                | 54                         |    |
| 4.31.1 Bug fixes                      | 54                         |    |
| 4.32 Lexichem TK 2.1.1                | 54                         |    |
| 4.32.1 Bug fixes                      | 54                         |    |
| 4.33 Lexichem TK 2.1.0                | 55                         |    |
| 4.33.1 New features                   | 55                         |    |
| 4.33.2 Bug fixes                      | 55                         |    |
| 4.34 Lexichem TK 2.0.2                | 56                         |    |
| 4.35 Lexichem TK 2.0.0                | 56                         |    |
| 4.36 Lexichem TK 1.9                  | 56                         |    |
| 4.37 Lexichem TK 1.8                  | 57                         |    |
| 4.38 Lexichem TK 1.7                  | 57                         |    |
| 4.39 Lexichem TK 1.6                  | 58                         |    |
| 4.40 Lexichem TK 1.5                  | 58                         |    |
| 4.41 Lexichem TK 1.4                  | 59                         |    |
| 4.42 Lexichem TK 1.3                  | 59                         |    |
| 4.43 Lexichem TK 1.2                  | 59                         |    |
| 4.44 Lexichem TK 1.1                  | 59                         |    |
| 4.44.1 OEParseIUPACName Improvements  | 60                         |    |
| 4.44.2 OECreateIUPACName Improvements | 60                         |    |
| 4.45 Lexichem TK 1.0                  | 60                         |    |
| 4.45.1 OEParseIUPACName Improvements  | 60                         |    |
| 4.45.2 OECreateIUPACName Improvements | 60                         |    |
| 5 Copyright and Trademarks            | 61                         |    |
| 6 Sample Code                         | 63                         |    |
| 7 Citation                            | 65                         |    |
| 7.1 Orion ® Floes                     | 65                         |    |
| 7.2 Toolkits and Applications         | 65                         |    |
| 7.3 OpenEye Web Services              | 67                         |    |
| 8 Technology Licensing                | 69                         |    |
| 8.1 GCC                               | 84                         |    |
| 8.1.1 GCC RUNTIME LIBRARY EXCEPTION   | 84                         |    |
| 8.1.2                                 | GNU GENERAL PUBLIC LICENSE | 86 |
| <b>Index</b>                          |                            | 99 |

#### **CHAPTER**

## **THEORY**

## **1.1 Input Name Representation**

The oeiupac library currently processes NULL (zero) terminated ASCII character strings; therefore Greek characters, symbols, fonts and superscripts must be transliterated into the printable subset of ASCII. When parsing compound names, the *oeiupac* library considers both spaces and tab characters as interchangeable, and any number of consecutive 'whitespace' characters are treated as a single space.

Currently, the name parsing is case insensitive, allowing arbitrary mixing of upper and lower case characters, e.g. initial letter capitalization.

| Charac-    | Friendly           | Decimal   | Hex        | Uni-          | Addl1    | Addl <sub>2</sub> | Addl3       | Addl4  |
|------------|--------------------|-----------|------------|---------------|----------|-------------------|-------------|--------|
| ter        | Code               | Code      | Code       | code          |          |                   |             |        |
| $\alpha$   | α                  | $&\#945;$ | $&\#x3B1;$ | <b>\U03B1</b> | .alpha.  | \$a               | $\{\{a\}$   | alpha  |
|            | β                  | $&\#946;$ | $&\#x3B2;$ | <b>\U03B2</b> | .beta.   | \$ <sub>b</sub>   | $\{\{b\}$   | beta   |
|            | γ                  | $&\#947;$ | $&\#x3B3;$ | <b>NU03B3</b> | .gamma.  | \$g               | $\S\{g\}$   | gamma  |
|            | δ                  | $&\#948;$ | $&\#x3B4;$ | <b>\U03B4</b> | .delta.  | \$d               | $\{\{d\}\}$ | delta  |
| $\epsilon$ | ε                  | $&\#949;$ | ε          | <b>\U03B5</b> | $e$ -ep. |                   |             | $ep-$  |
|            |                    |           |            |               | silon.   |                   |             | silon  |
| $\lambda$  | λ                  | $&\#955;$ | $&$ #x3BB; | <b>\U03BB</b> | .lambda. | \$1               | \$1]        | lambda |
| $+/-$      | <b>&amp;PLUSMN</b> | ±         | $&\#x0B1$  | <b>\U00B1</b> |          |                   |             |        |

Greek characters are understood in a number of different representations.

Note: Addl[1-4] are additional identifiers.

For example, the strings '\$a', '\${a}', 'alpha', '.alpha', 'α', 'α' and 'α' are all understood to represent the Greek character *alpha*,  $(\alpha)$ .

## **1.2 Output Name Representation**

Unrecognized functional groups, linkers or ring systems are denoted in the generated name as the string 'BLAH'. As much of the name as possible is generated resulting in compound names such as 'dichloroBLAHcarboxylic acid'. Generated compound names are entirely lower case, with no initial capitalization. Upper case characters are generated for locants and, as described above, for BLAH.

Names are generated using a set of markup tokens which can be further processed for output to the desired format.

Greek characters are indicated with the dollar character followed by a single letter. In this formalism, '\$a' represents the Greek character alpha,  $\alpha$ , '\$b' the Greek character beta,  $\beta$ , etc.

Superscripts are indicated by surrounding the superscripted text with caret and curly braces. Hence '\\$1^{5}' represents the Greek character lambda followed by a superscript five, *i.e.*  $\lambda^5$ . Similarly, 'pentacyclo[4.2.0.0^{2,5}.0^{3,8}.0^{4,7}] octane' would be the von Baeyer system name for cubane.

Subscripts are are indicated by surrounding the superscripted text with underscore and curly braces. Hence 'C<sub>1</sub>{60} Fullerene' is a generated name for Buckminsterfullerene.

Italics, used for stereochemistry and locants, are indicated with a tilde and curly braces. An example is:  $(2-\{R\})$ -butan-2-ol'.

The markup tokens are converted into appropriate markup for a particular use during the conversion of the raw name to the desired final character set.

Translation of names to alternate languages may result in characters outside of the default ASCII character set being used. In this case, the characters are encoded as escaped unicode, eg: 'u**XXXX'**. The actual output characters are generated in the final character set conversion.

Multiple components in a disconnected molecule, apart from common salts and counter ions, are separated from each other by a semicolon followed by a space. Mixtures containing salts are written ordering the cations before the compound name, followed by anions, followed by any common neutral molecules (e.g. hydrate or hydrochloride).

### **1.2.1 Enhanced Stereochemistry**

Note: Enhanced stereochemistry is only supported in for molecules which are represented using MDL V3000 Format.

Naming recognizes enhanced stereochemical features as embodied in the V3000 file format. V3000 allows the specification of AND and OR stereochemical atom groupings. An AND grouping corresponds to a mixture of structures with the center(s) as indicated and their inverse configuration. An  $OR$  grouping corresponds to either the isomer as indicated or its inverse configuration. Absolute, unspecified, AND, and OR stereocenters can all be present in single molecule.

Figure: Enhanced Stereochemistry illustrates enhanced stereochemical names generated using the Lexichem TK. Centers in an AND grouping are designated with "RS" or "SR". Centers in an OR grouping are designated with "R\*" or " $S^*$ ".

For chemical structures with multiple chiral centers where only some are designated as **AND** (see top left image), the descriptors "RS" and "SR" are used to denote AND centers.

For a structure where all of the stereocenters are designated as **AND**, the structure represents a molecule and its enantiomer. In that case (even though the V3000 format does not explicitly define the ratio of enantiomers), the molecule is named as a racemate, with a "rac" prefix (see bottom left image).

For chemical structures with multiple chiral centers where only some are designated as  $OR$  (see top right image), the descriptors " $R^*$ " and " $S^*$ " are used to denote the **OR** centers.

For a structure where all of the stereocenters are designated as  $OR$ , the structure represents a molecule or its relative inverse configuration. In that case the molecule is named with a "rel" prefix. (see bottom right image).

The IUPAC standard recommends naming structures so the first AND indicator and the first OR indicator in the name are "R", "RS", or "R\*" as appropriate. When generating a name from a structure, this is easily accomplished by inverting the stereo designation on every center in the stereo grouping. For example, the names "rac-(2R,4R)-4-aminopentan-2-ol" and "rac-(2S,4S)-4-aminopentan-2-ol" are equivalent since they both mean: "a mixture of the  $(2R.4R)$  and  $(2S.4S)$  isomers". In this case IUPAC conventions recommend using the "rac- $(2R.4R)$ " name.

This choice of recommended name may be a cause for confusion since the atom/bond block of the V3000 molfile indicates a particular configuration and it is possible that the generated name will not appear to correspond to the configuration as found in the atom/bond block. To mitigate the potential for confusion, only the IUPAC and Systematic

(1R\*,3R\*,5S)-3-chloro-5-nitro-cyclohexanol

![](_page_10_Figure_2.jpeg)

(1RS,3RS,5S)-3-chloro-5-nitro-cyclohexanol

![](_page_10_Figure_4.jpeg)

rel-(1R,3R,5S)-3-chloro-5-nitro-cyclohexanol

![](_page_10_Figure_6.jpeg)

rac-(1R,3R,5S)-3-chloro-5-nitro-cyclohexanol

![](_page_10_Figure_8.jpeg)

Generated by OEDepict TK

Fig. 1: Enhanced Stereochemistry

style of output names perform the inversion. This allows the user to control whether or not the inversion occurs. Comparing the IUPAC and OpenEye style names will give an indication whether or not the inversion is occurring.

For more details please refer to section P-92.1.2 and P-92.1.3 of the Nomenclature of Organic Chemistry [IUPAC-2014].

Note: IUPAC nomenclature currently only allows for a single AND group and a single OR group on a molecule. The V3000 format allows for multiple independent AND and OR groups. Names are generated as if all the AND centers are in a single AND group and all the OR centers are in a single OR group. This will be remedied when IUPAC defines a naming convention for these more complex cases.

### 1.2.2 Isotopes

![](_page_11_Figure_2.jpeg)

#### Fig. 2: Isotopes

An isotopically substituted compound has a composition such that essentially all the molecules of the compound have only the indicated nuclide at each designated position. For all other positions, the absence of nuclide indication means that the nuclide composition is the natural one [IUPAC-2014].

To name isotopically substituted compounds:

The name of an isotopically substituted compound is formed by inserting in parentheses the nuclide symbol(s), preceded by any necessary locant(s), letters and/or numerals, before the name or preferably before the denomination of that part of the compound that is isotopically substituted. Immediately after the parentheses there is neither space nor hyphen, except that when the name, or a part of a name, includes a preceding locant, a hyphen is inserted. When polysubstitution is possible, the number of atoms substituted is always specified as a right subscript to the atomic symbol(s), even in case of monosubstitution [IUPAC-2014].

For names composed of two or more words:

the isotopic descriptor is placed before the appropriate word or part of the word that includes the nuclide(s), unless unambiguous locants are available or are unnecessary [IUPAC-2014].

For more details, please refer to chapter 8 of the IUPAC Nomenclature of Organic Compounds Draft 2004 [IUPAC-2014].

## **1.3 Output Name Styles**

Naming functionality supports the generation of several *styles* of compound names. The currently predefined name styles are OpenEye (the default), IUPAC, CAS, Traditional and Systematic. OpenEye names loosely correspond to the kinds of names familiar to a medicinal chemist. These names are intended to be a subset of the IUPAC 2005 standard's acceptable names, but not necessarily the PIN (Preferred IUPAC Name). These correspond to the types of names found in a Sigma-Aldrich catalog or a Journal of Medicinal Chemistry article, for example.

IUPAC names are intended to follow the IUPAC 2005 recommendations for the Preferred IUPAC Name (PIN). Future releases may further refine this definition to provide IUPAC2005, IUPAC93 and IUPAC79 name styles that reflect the corresponding standard's preferred name.

The CAS name style is intended to follow the Chemical Abstracts Service's naming conventions, where they differ from IUPAC's.

The Traditional name style corresponds to forms of compound naming that are now no longer acceptable to the IUPAC rules. The boundary between whether a trivial/common name is considered OpenEye or Traditional when it is acceptable to IUPAC but not preferred is blurred, with OpenEye attempting to follow the more prevalent usage.

Finally, Systematic names correspond to the fully systematic IUPAC names that the IUPAC preferred names are slowly converging towards.

## **1.4 Examples of Name Style Differences**

Some of the concepts explained in the previous section are probably best clarified through some real examples.

### 1.4.1 Example OpenEye vs. IUPAC vs. Systematic Differences

- The SMILES string  $\circ$  is called 'water' by the *OpenEye* name style, but 'oxidane' by the IUPAC and Systematic name styles.
- The SMILES C#C is called 'acetylene' by the OpenEye and IUPAC name styles, but 'ethyne' by the Systematic name style.
- The SMILES prefix  $\star$ Nc1ccccc1 is called 'anilino' by the *OpenEye* and IUPAC name styles, but 'phenylamino' by the Systematic name style.
- The SMILES prefix  $\star \circ$  [N+]  $\#$  [C-] is called 'fulminato' by the *OpenEye* name style, but 'isocyanooxy' by the IUPAC and Systematic name styles.
- The SMILES prefix  $\star$ C (=0) C is called 'acetyl' in the *OpenEye* and IUPAC name styles, but 'ethanoyl' in the Systematic name style.
- The SMILES string  $CC (=0) C$  is called 'acetone" in the *OpenEye* name style, but 'propan-2-one' in the IUPAC and Systematic name styles.
- The SMILES string  $C (=0)$  o is called 'formic acid' in the *OpenEye* and IUPAC name styles, but 'methanoic acid' in the Systematic name style.

### 1.4.2 Example OpenEye/IUPAC vs. CAS Differences

- The SMILES string c1ccccc1CCCCCCC is named as '1-phenylheptane' by the OpenEye and IUPAC name styles, but as 'heptylbenzene' by the CAS name style.
- The SMILES prefix  $\star$  [BH2] is called 'boranyl' by the *OpenEye* and IUPAC name styles, but as 'boryl' by the CAS name style.

### 1.4.3 Example OpenEye/IUPAC vs. Traditional Differences

- The SMILES prefix \*S is called 'sulfanyl' by the OpenEye and IUPAC name styles, but as 'mercapto' by the Traditional name style.
- The SMILES string CCCCCCCCC  $(=0)$  O is called 'nonanoic acid' by the OpenEye and IUPAC name styles, but as 'pelargonic acid' by the Traditional name style.

### **CHAPTER**

## **TWO**

## **EXAMPLES**

## 2.1 Lexichem TK Examples

The following table lists the currently available Lexichem TK examples:

| Program                     | Description                       |
|-----------------------------|-----------------------------------|
| <i>mol2nam_example.py</i>   | convert molecules to names        |
| <i>nam2mol_example.py</i>   | convert names to molecules        |
| <i>translate_example.py</i> | translate names between languages |

#### **Examples:**

### 2.1.1 Converting Molecules to Names

Converts a file of chemical structures (specified by -in option) into chemical names (-out option), in a choice of language (-language option), encodings (-encoding option) and styles (-style option).

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python mol2nam_example.py --help
```

will generate the following output:

```
Simple parameter list
 mol2nam
   I/O-in : Input filename
     -out : Output filename
   Lexichem
      -language : Language for output names.
     -style : Style of output names
     -capitalize : Capitalize output names.
     -tag : Set name as SD data with tag
      -delim : Append name to title using "delim"
      -charset : Choose charset/encoding for output names.
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
from openeye import oeiupac
def Mol2Nam(itf):
    ifs = oechem.oemolistream()
    if not ifs.open(itf.GetString("-in")):
        oechem. OEThrow. Fatal ("Unable to open '%s' for reading" % itf. GetString ("-in"))
    ofs = occhem.oemolostream()\text{Outname} = \text{None}if itf.HasString("-out"):
        outname = itf.GetString("-out")
        if not ofs.open(outname):
            oechem. OEThrow. Fatal ("Unable to open '%s' for reading" % outname)
    language = oeiupac.OEGetIUPACLanguage(itf.GetString("-language"))
    charset = oeiupac.OEGetIUPACCharSet(itf.GetString("-encoding"))
    style = oeiupac.OEGetIUPACNamStyle(itf.GetString("-style"))
    for mol in ifs. GetOEGraphMols():
        if mol. <math>GetDimension()</math> == 3:oechem.OEPerceiveChiral(mol)
            oechem.OE3DToAtomStereo(mol)
            oechem.OE3DToBondStereo(mol)
        name = oeiupac.OECreateIUPACName(mol, style)
        if language > 0:
            name = oeiupac.OEToLanguage(name, language)
        if itf.GetBool("-capitalize"):
            name = oeiupac.OECapitalizeName(name)
        if charset == oeiupac.OECharSet_ASCII:
            name = oeiupac.OEToASCII(name)
```

```
elif charset == oeiupac.OECharSet_UTF8:
            name = oeiupac.OEToUTF8(name)
        elif charset == oeiupac.OECharSet_HTML:
           name = oeiupac.OEToHTML(name)
        elif charset == oeiupac.OECharSet_SJIS:
           name = oeiupac.OEToSJIS(name)
        elif charset == oeiupac.OECharSet_EUCJP:
           name = oeiupac.OEToEUCJP(name)
        if outname:
           if itf.HasString("-delim"):
               title = mol.GetTitle()
                name = title + itf.GetString("-delim") + nameif itf.HasString("-taq"):
                oechem. OESetSDData (mol, itf. GetString ("-tag"), name)
           mol.SetTitle(name)
           oechem.OEWriteMolecule(ofs, mol)
       else:
           print (name)
#######################################
InterfaceData = ""# mol2nam interface file
!CATEGORY mol2nam
    !CATEGORY I/O
       !PARAMETER -in 1
         !ALIAS -i
         !TYPE string
         !REQUIRED true
         !BRIEF Input filename
         IKEYLESS 1
       ! END
       !PARAMETER -out 2
         !ALIAS -o
         !TYPE string
         !BRIEF Output filename
         !KEYLESS 2
        !END
   ! END
    !CATEGORY Lexichem Features
        !PARAMETER -language 1
          !ALIAS -lang
          !TYPE string
          !DEFAULT american
          !LEGAL_VALUE american
          !LEGAL VALUE english
          !LEGAL VALUE us
           !LEGAL_VALUE british
```

!LEGAL VALUE uk

(continued from previous page)

```
!LEGAL_VALUE chinese
!LEGAL_VALUE zh
!LEGAL_VALUE cn
!LEGAL_VALUE danish
!LEGAL VALUE dk
!LEGAL VALUE da
!LEGAL_VALUE dutch
!LEGAL_VALUE nl
!LEGAL VALUE french
!LEGAL VALUE fr
!LEGAL_VALUE german
!LEGAL_VALUE de
!LEGAL_VALUE greek
!LEGAL VALUE el
!LEGAL_VALUE hungarian
!LEGAL_VALUE hu
!LEGAL_VALUE irish
!LEGAL VALUE ie
!LEGAL_VALUE ga
!LEGAL_VALUE italian
!LEGAL_VALUE it
!LEGAL_VALUE japanese
!LEGAL VALUE jp
!LEGAL_VALUE ja
!LEGAL_VALUE polish
!LEGAL_VALUE pl
!LEGAL VALUE portuguese
!LEGAL VALUE pt
!LEGAL_VALUE romanian
!LEGAL_VALUE ro
!LEGAL_VALUE russian
!LEGAL VALUE ru
!LEGAL VALUE slovak
!LEGAL_VALUE sk
!LEGAL_VALUE spanish
!LEGAL_VALUE es
!LEGAL_VALUE swedish
!LEGAL_VALUE se
!LEGAL_VALUE sv
```

```
!LEGAL_VALUE welsh
   !LEGAL_VALUE cy
   !REQUIRED false
   !BRIEF Language for output names.
!END
!PARAMETER -style 2
   !ALIAS -namestyle
   !TYPE string
   !DEFAULT openeye
   !LEGAL_VALUE openeye
   !LEGAL VALUE iupac
   !LEGAL VALUE cas
   !LEGAL VALUE traditional
    !LEGAL_VALUE systematic
    !LEGAL_VALUE casindex
    !LEGAL_VALUE casidx
    !LEGAL_VALUE autonom
    !LEGAL_VALUE iupac79
    !LEGAL_VALUE iupac93
   !LEGAL_VALUE acdname
   !BRIEF Style of output names
! END
!PARAMETER -capitalize 3
  !ALIAS -capitalise
  !TYPE bool
  !DEFAULT false
   !BRIEF Capitalize output names.
!END
!PARAMETER -tag 4
  !TYPE string
  !REOUIRED false
  !BRIEF Set name as SD data with tag
! END
!PARAMETER -delim 5
  !TYPE string
  !REQUIRED false
  !BRIEF Append name to title using 'delim'
LEND
!PARAMETER -charset 7
   !ALIAS -encoding
    !TYPE string
    !DEFAULT default
   !REQUIRED false
   !LEGAL_VALUE default
   !LEGAL_VALUE ascii
    !LEGAL_VALUE utf8
    !LEGAL VALUE html
    !LEGAL VALUE sjis
    !LEGAL_VALUE eucjp
    !BRIEF Choose charset/encoding for output names.
```

```
! END
     !END
! END
\overline{n}, \overline{n}, \overline{n}def main(argv=[_name_]):
    itf = oechem. OEInterface (InterfaceData, argv)
    Mol2Nam(itf)
if name == " main ":
    sys.exit(main(sys.argy))
```

### 2.1.2 Converting Names to Molecules

Converts a file of chemical names (specified by the -in option) of a specific language (-language option) into a file of chemical structures (specified by the *-out* option).

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python nam2mol_example.py --help
```

will generate the following output:

```
Simple parameter list
 nam2mol
   I/O-in : Input filename
     -out : Output filename
   Lexichem
     -language : Language for input names.
     -tag : Set name as SD data with tag
     -empty : Output an empty molecule for unparseable names
      -charset : Choose charset/encoding for input names.
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
```

```
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
from openeye import oeiupac
def Nam2Mol(itf):
    ifp = sys.stdoutif itf.GetString("-in") != "-":
        ifp = open(itf.GetString("in"))ofs = occhem.oemolostream()if not ofs.open(itf.GetString("-out")):
        oechem. OEThrow. Fatal ("Unable to open output file: %s" % itf. GetString ("-out"))
   language = oeiupac.OEGetIUPACLanguage(itf.GetString("-language"))
   charset = oeiupac.OEGetIUPACCharSet(itf.GetString("-charset"))
   mol = occhem.OEGraphMol()for name in ifp:
       name = name.startp()mol.Clear()
        # Speculatively reorder CAS permuted index names
        str = oeiupac.OEReorderIndexName(name)
        if len(str) == 0:
            str = nameif charset == oeiupac.OECharSet_HTML:
           str = oeiupac.OEFromHTML (str)if charset == oeiupac.OECharSet_UTF8:
            str = oeiupac. OEFromUTE8 (str)str = oeiupac.OELowerCaseName(str)
        if language != oeiupac.OELanguage_AMERICAN:
            str = oeiupac. OEFromLanguage(str, language)done = oeiupac.OEParseIUPACName(mol, str)
        if not done and itf. GetBool ("-empty") :
           mol.Clean()done = Trueif done:
            if itf.HasString("-taq"):
                oechem.OESetSDData(mol, itf.GetString("-tag"), name)
```

```
mol.SetTitle(name)
           oechem.OEWriteMolecule(ofs, mol)
#######################################
InterfaceData = ""# nam2mol interface file
!CATEGORY nam2mol
    !CATEGORY I/O
       !PARAMETER -in 1
         !ALIAS -i
         !TYPE string
         !REQUIRED true
         !BRIEF Input filename
         !KEYLESS 1
       ! END
       !PARAMETER -out 2
         !ALIAS -o
         !TYPE string
         !DEFAULT -
         !BRIEF Output filename
         !KEYLESS 2
        ! END
   ! END
    !CATEGORY Lexichem Features
        !PARAMETER -language 1
          !ALIAS -lang
          !TYPE string
          !DEFAULT american
           !LEGAL VALUE american
          !LEGAL_VALUE english
          !LEGAL VALUE us
          !LEGAL_VALUE chinese
          !LEGAL_VALUE zh
          !LEGAL VALUE cn
          !LEGAL VALUE danish
          !LEGAL_VALUE dk
          !LEGAL_VALUE da
          !LEGAL_VALUE dutch
           !LEGAL VALUE nl
           !LEGAL VALUE french
          !LEGAL_VALUE fr
           !LEGAL_VALUE german
           !LEGAL_VALUE de
           !LEGAL_VALUE greek
           !LEGAL_VALUE el
```

```
!LEGAL VALUE hungarian
   !LEGAL_VALUE hu
   !LEGAL_VALUE irish
   !LEGAL_VALUE ie
   !LEGAL_VALUE ga
   !LEGAL VALUE italian
   !LEGAL VALUE it
   !LEGAL_VALUE japanese
   !LEGAL_VALUE jp
   !LEGAL_VALUE ja
   !LEGAL VALUE polish
   !LEGAL VALUE pl
   !LEGAL_VALUE portuguese
   !LEGAL_VALUE pt
   !LEGAL VALUE romanian
   !LEGAL_VALUE ro
   !LEGAL_VALUE russian
   !LEGAL_VALUE ru
   !LEGAL VALUE slovak
   !LEGAL VALUE sk
   !LEGAL_VALUE spanish
   !LEGAL_VALUE es
   !LEGAL_VALUE swedish
   !LEGAL VALUE se
   !LEGAL_VALUE sv
  !LEGAL_VALUE welsh
  !LEGAL_VALUE cy
  !REQUIRED false
  !BRIEF Language for input names.
! END
!PARAMETER -tag 3
  !TYPE string
  !REOUIRED false
  !BRIEF Set name as SD data with tag
! END
!PARAMETER -empty 4
  !TYPE bool
  !DEFAULT false
  !BRIEF Output an empty molecule for unparseable names
! END
!PARAMETER -charset 5
   !ALIAS -encoding
   !TYPE string
```

```
!DEFAULT default
            !REQUIRED false
            !LEGAL VALUE default
            !LEGAL_VALUE ascii
            !LEGAL_VALUE utf8
            !LEGAL_VALUE html
            !BRIEF Choose charset/encoding for input names.
         !END
    !END
! END
\overline{n} \overline{n} \overline{n}def main(argv=[_name_]):
    itf = oechem. OEInterface (InterfaceData, argy)
    Nam2Mol(itf)
if _name_ == "_main_":
    sys.exit(main(sys.argv))
```

### 2.1.3 Translating Names Between Languages

Translates a file of chemical names (specified by the -in option) in a specific language (-from option) into a file of names (specified by the *-out* option) in another language (*-to* option).

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python translate_example.py --help
```

will generate the following output:

```
Simple parameter list
 translate
   -nobanner : Suppress the program banner.
   -in : Input filename
   -out : Output filename
   -from : Language for input names.
   -to : Language for input names.
    -from charset : Choose charset/encoding for input names.
   -to_charset : Choose charset/encoding for output names.
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
# Translates between languages. Internally LexichemTK uses American
# English so it will convert to/from that as an intermediate
# representation.
# By default the program inputs/outputs the internal LexichemTK
# character set representation. Optionally one can convert the
# input or output to alternate encodings, eg: HTML or UTF8.
import sys
from openeye import oechem
from openeye import oeiupac
def Translate(itf):
   ifp = sys.stdoutif itf.GetString("-in") != "-":
        ifp = open(itf.GetString("-in"))if itf.HasString("-out"):
        outname = itf.GetString("-out")
        if outname != "-":
           trv:
                ofs = open(outname, 'w')except Exception:
                oechem. OEThrow. Fatal ("Unable to open '%s' for writing" % outname)
        else:ofs = sys.stdoutfrom\_language = oe,iOEGetIUPACLanguage(itf.GetString("-from"))to_language = oeiupac.OEGetIUPACLanguage(itf.GetString("-to"))
    from_charset = oeiupac.OEGetIUPACCharSet(itf.GetString("-from_charset"))
    to_charset = oeiupac.OEGetIUPACCharSet(itf.GetString("-to_charset"))
    for name in ifp:
       name = name.startip()
```

```
# Convert from Charset to internal representation
        if from_charset == oeiupac.OECharSet_HTML:
           name = oeiupac.OEFromHTML(name)
        elif from_charset == oeiupac.OECharSet_UTF8:
            name = oeiupac.OEFromUTF8(name)
        # Translation functions all operate on lowercase names
        name = oeiupac.OELowerCaseName(name)
        if from_language != oeiupac.OELanguage_AMERICAN:
            name = oeiupac.OEFromLanguage(name, from_language)
        # At this point the name is American English in the
        # LexichemTK default internal character representation
        # Convert to output language
        if to_language != oeiupac.OELanguage_AMERICAN:
            name = oeiupac.OEToLanguage(name, to_language)
        # Convert to output charset
        if to_charset == oeiupac.OECharSet_ASCII:
            name = oeiupac.OEToASCII(name)
        elif to_charset == oeiupac.OECharSet_UTF8:
           name = oeiupac.OEToUTF8(name)
        elif to_charset == oeiupac.OECharSet_HTML:
           name = oeiupac.OEToHTML(name)
        elif to charset == oeiupac.OECharSet_SJIS:
           name = oeiupac. 0EToSJIS(name)elif to_charset == oeiupac.OECharSet_EUCJP:
            name = oeiupac.OEToEUCJP(name)
        ofs.write(name + '\n\ln')
#######################################
InterfaceData = ""# translate interface file
! CATEGORY translate
      !PARAMETER -in 1
       !ALIAS -i
       !TYPE string
       !REQUIRED true
       !BRIEF Input filename
       !KEYLESS 1
      ! END
      !PARAMETER -out 2
       IATITAS -<sub>O</sub>!TYPE string
       !DEFAULT -
       !BRIEF Output filename
       !KEYLESS 2
      !END
      !PARAMETER -from 3
         !ALIAS -from_language
```

```
!DEFAULT american
!LEGAL_VALUE american
!LEGAL_VALUE english
!LEGAL_VALUE us
!LEGAL_VALUE chinese
!LEGAL_VALUE zh
!LEGAL VALUE cn
!LEGAL_VALUE danish
!LEGAL_VALUE dk
!LEGAL_VALUE da
!LEGAL VALUE dutch
!LEGAL_VALUE nl
!LEGAL_VALUE french
!LEGAL_VALUE fr
!LEGAL VALUE german
!LEGAL_VALUE de
!LEGAL_VALUE greek
!LEGAL_VALUE el
!LEGAL VALUE hungarian
!LEGAL VALUE hu
!LEGAL_VALUE irish
!LEGAL_VALUE ie
!LEGAL_VALUE ga
!LEGAL VALUE italian
!LEGAL_VALUE it
!LEGAL_VALUE japanese
!LEGAL_VALUE jp
!LEGAL_VALUE ja
!LEGAL VALUE polish
!LEGAL VALUE pl
!LEGAL_VALUE portuguese
!LEGAL_VALUE pt
!LEGAL VALUE romanian
!LEGAL_VALUE ro
!LEGAL_VALUE russian
!LEGAL_VALUE ru
!LEGAL_VALUE slovak
!LEGAL VALUE sk
!LEGAL_VALUE spanish
!LEGAL VALUE es
```

!TYPE string

```
!LEGAL_VALUE swedish
    !LEGAL_VALUE se
    !LEGAL_VALUE sv
    !LEGAL_VALUE welsh
    !LEGAL_VALUE cy
    !REQUIRED false
    !BRIEF Language for input names.
! END
!PARAMETER -to 4
   !ALIAS -to_language
   !TYPE string
   !DEFAULT american
    !LEGAL_VALUE american
    !LEGAL_VALUE english
    !LEGAL_VALUE us
    !LEGAL_VALUE chinese
    !LEGAL_VALUE zh
    !LEGAL_VALUE cn
    !LEGAL_VALUE danish
    !LEGAL_VALUE dk
    !LEGAL VALUE da
    !LEGAL VALUE dutch
    !LEGAL_VALUE nl
    !LEGAL_VALUE french
    !LEGAL_VALUE fr
    !LEGAL_VALUE german
    !LEGAL VALUE de
    !LEGAL_VALUE greek
    !LEGAL_VALUE el
    !LEGAL VALUE hungarian
    !LEGAL VALUE hu
    !LEGAL_VALUE irish
    !LEGAL_VALUE ie
    !LEGAL_VALUE ga
    !LEGAL_VALUE italian
    !LEGAL VALUE it
    !LEGAL_VALUE japanese
    !LEGAL_VALUE jp
    !LEGAL_VALUE ja
    !LEGAL_VALUE polish
    !LEGAL_VALUE pl
```

```
!LEGAL_VALUE pt
         !LEGAL_VALUE romanian
         !LEGAL_VALUE ro
         !LEGAL_VALUE russian
         !LEGAL VALUE ru
         !LEGAL VALUE slovak
         !LEGAL_VALUE sk
         !LEGAL_VALUE spanish
         !LEGAL VALUE es
         !LEGAL VALUE swedish
         !LEGAL_VALUE se
         !LEGAL_VALUE sv
         !LEGAL_VALUE welsh
         !LEGAL_VALUE cy
         !REOUIRED false
         !BRIEF Language for input names.
     ! END
     !PARAMETER -from charset 5
        !TYPE string
         !DEFAULT default
         !REQUIRED false
         !LEGAL_VALUE default
         !LEGAL_VALUE ascii
         !LEGAL_VALUE utf8
         !LEGAL VALUE html
         !LEGAL_VALUE sjis
         !LEGAL_VALUE eucjp
         !BRIEF Choose charset/encoding for input names.
     ! END
     !PARAMETER -to_charset 6
        !ALIAS -encoding
        !ALIAS -charset
         !TYPE string
         !DEFAULT default
         !REQUIRED false
         !LEGAL_VALUE default
         !LEGAL VALUE ascii
         !LEGAL_VALUE utf8
         !LEGAL_VALUE html
         !LEGAL_VALUE sjis
         !LEGAL_VALUE eucjp
         !BRIEF Choose charset/encoding for output names.
     ! END
!END
\overline{n},\overline{n},\overline{n}
```

!LEGAL VALUE portuquese

```
def main(argv=[\underline{\hspace{1cm}}name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface(InterfaceData, argv)
    Translate(itf)
if __name__ == "__main__".sys.exit(main(sys.argv))
```

## **CHAPTER**

## **THREE**

**API** 

## **3.1 OEIUPAC Constants**

### 3.1.1 OECharSet

This namespace contains constants for defining the character set for character conversion.

### **DEFAULT**

No character conversion.

### **ASCII**

See OETOASCII for format details.

#### **HTML**

See OETOHTML for format details.

#### UTF8

See OETOUTF8 for format details.

#### **SJIS**

See OETOSJIS for format details.

#### **EUCJP**

See OETOEUCJP for format details.

### 3.1.2 OEIUPAC

This namespace contains constants.

#### **OENamStyleOpenEye**

This constant is used to specify the (default) predefined OpenEye name style to the OECreateIUPACName function.

#### **OENamStyleTraditional**

This constant is used to specify the predefined traditional name style to the  $OECreate IUPACName$  function.

#### **OENamStyleSystematic**

This constant is used to specify the predefined systematic name style to the OECreateIUPACName function.

#### **OENamStyleIUPAC**

This constant is used to specify the predefined IUPAC 2005 name style to the  $OECreate IUPACName$  function.

#### **OENamStyleCAS**

This constant is used to specify the predefined Chemical Abstracts Service (CAS) name style to the OECreateIUPACNamefunction.

#### **OENamStyleCASIndex**

This constant is used to specify the predefined Chemical Abstracts Service (CAS) permuted index name style to the OECreateIUPACNamefunction.

#### **OENamStyleAutoNom**

This constant is used to specify the predefined MDL/Beilstein AutoNom name style to the  $OECreate IUPACName$ function.

#### **OENamStyleIUPAC79**

This constant is used to specify the predefined IUPAC 1979 name style to the  $OECreate IUPACName$  function.

#### **OENamStyleIUPAC93**

This constant is used to specify the predefined IUPAC 1993 name style to the  $OECreate IUPACName$  function.

#### **OENamStyleACDName**

This constant is used to specify the predefined ACD name style to the OECreateIUPACName function.

### 3.1.3 OELanguage

This namespace contains constants for defining which language to translate to/from using  $DEFromLanguage$  and OEToLanquage.

Depending on the language, the translation functions may expect \u escaped Unicode characters. In general the translations only use characters in the Basic Multilingual Plane (BMP). Each language below indicates the range of Unicode characters which are handled. Character set conversion should take into account the range of Unicode expected.

#### **ENGLISH**

This constant is used to specify the American dialect of English. This is currently a synonym of the constant OELanguage\_AMERICAN. Uses only ASCII characters.

#### **AMERICAN**

This constant is used to specify the American dialect of English to This is currently a synonym of the constant OELanguage\_ENGLISH. Uses only ASCII characters.

#### **BRITISH**

This constant is used to specify the traditional British dialect of English. Uses only ASCII characters.

#### **INTERNATIONAL**

This constant is used to specify the international dialect of English. Uses only ASCII characters.

#### **CHINESE**

This constant is used to specify the Chinese language. Uses CJK characters in the Unicode BMP.

#### **DANISH**

This constant is used to specify the Danish language. Uses ASCII and Latin-1 Unicode characters in the \u00a0 to \u00ff range.

#### **DUTCH**

This constant is used to specify the Dutch language. Uses ASCII and Latin-1 Unicode characters in the \u00a0 to \u00ff range.

#### **FRENCH**

This constant is used to specify the French language. Uses ASCII and Latin-1 Unicode characters in the \u00a0 to \u00ff range.

#### **GERMAN**

This constant is used to specify the German language. Uses ASCII and Latin-1 Unicode characters in the \u00a0 to \u00ff range.

#### **GREEK**

This constant is used to specify the Greek language. Uses ASCII and Greek Unicode characters in the \u0370 to \u03ff range.

#### **HUNGARIAN**

This constant is used to specify the Hungarian language. Uses ASCII, Latin-1 Unicode characters in the \u00a0 to \u00ff range and Latin Extended-A Unicode characters in the \u0100 to \u017f range.

#### **IRISH**

This constant is used to specify the Irish language. Uses ASCII and Latin-1 Unicode characters in the  $\u00a0$  to \u00ff range.

#### **ITALIAN**

This constant is used to specify the Italian language. Uses ASCII and Latin-1 Unicode characters in the \u00a0 to \u00ff range.

#### **JAPANESE**

This constant is used to specify the Japanese language. Uses CJK characters in the Unicode BMP.

#### **POLISH**

This constant is used to specify the Polish language. Uses ASCII, Latin-1 Unicode characters in the \u00a0 to \u00ff range and Latin Extended-A Unicode characters in the \u0100 to \u017f range.

#### **PORTUGUESE**

This constant is used to specify the Portuguese language. Uses ASCII and Latin-1 Unicode characters in the  $\u00a0$ to \u00ff range.

#### **ROMANIAN**

This constant is used to specify the Romanian language. Uses ASCII, Latin-1 Unicode characters in the  $\u00a0$  to \u00ff range and Latin Extended-A Unicode characters in the \u0100 to \u017f range.

#### **RUSSIAN**

This constant is used to specify the Russian language. Uses ASCII and Cyrillic Unicode characters in the \u0400 to \u04ff range.

#### **SLOVAK**

This constant is used to specify the Slovak language. Uses ASCII, Latin-1 Unicode characters in the \u00a0 to \u00ff range and Latin Extended-A Unicode characters in the \u0100 to \u017f range.

#### **SPANISH**

This constant is used to specify the Spanish language. Uses ASCII and Latin-1 Unicode characters in the \u00a0 to \u00ff range.

#### **SWEDISH**

This constant is used to specify the Swedish language. Uses ASCII and Latin-1 Unicode characters in the \u00a0 to \u00ff range.

#### **WELSH**

This constant is used to specify the Welsh language. Uses ASCII, Latin-1 Unicode characters in the \u00a0 to \u00ff range and Latin Extended-A Unicode characters in the \u0100 to \u017f range.

## **3.2 OEIUPAC Functions**

## 3.2.1 OECapitalizeName

std::string OECapitalizeName(const char \*ptr)

Capitalize the appropriate first letter of a name generated by OECreateIUPACName. This function should be called after translating the name to a foreign language, but before converting the character set encoding.

## 3.2.2 OECreateIUPACName

```
std::string OECreateIUPACName(const OEChem::OEMolBase &mol,
                              const unsigned char *style=OENamStyleOpenEye)
```

This function attempts to generate a 'reasonable' IUPAC name for the given molecule, mol, and return the result in a string. These 'reasonable' names attempts to be one of the recommended IUPAC names for a compound, however occasionally this function may fall back to using IUPAC 'systematic' naming for parts of a molecule. Any parts of a molecule that cannot be named result in the substring BLAH appearing in the returned string.

The optional style argument can be used to control and customize the style of the names generated by this function. The nine currently predefined name styles are

- · OEIUPAC\_OENamStyleOpenEye (the default),
- · OEIUPAC\_OENamStyleIUPAC,
- OEIUPAC\_OENamStyleIUPAC79,
- · OEIUPAC\_OENamStyleIUPAC93,
- · OEIUPAC OENamStyleTraditional,
- · OEIUPAC\_OENamStyleAutoNom,
- · OEIUPAC OENamStyleCAS,
- · OEIUPAC OENamStyleCASIndex and
- · OEIUPAC\_OENamStyleSystematic.

After the name has been generated it may be translated into one of several languages, for example using the OETOGerman or OETOJapanese functions, then optionally capitalized using OECapitalizeName, and finally converted into a final character encoding, for example using OETOUTF8 or OETOHTML.

## 3.2.3 OEFromBritish

std::string OEFromBritish(const char \*ptr)

Convert the chemical name specified by 'ptr' from British English to American English.

See OELanguage for character set information.

## 3.2.4 OEFromChinese

std::string OEFromChinese(const char \*ptr)

Convert the chemical name specified by 'ptr' from simplified or traditional Chinese to English.

See OELanguage for character set information.

#### 3.2.5 OEFromDanish

std::string OEFromDanish(const char \*ptr)

Convert the chemical name specified by 'ptr' from Danish to English.

See OELanguage for character set information.

### 3.2.6 OEFromDutch

std::string OEFromDutch(const char \*ptr)

Convert the chemical name specified by 'ptr' from Dutch to English.

See OELanguage for character set information.

### 3.2.7 OEFromFrench

std::string OEFromFrench (const char \*ptr)

Convert the chemical name specified by 'ptr' from French to English.

See OELanguage for character set information.

### 3.2.8 OEFromGerman

std::string OEFromGerman (const char \*ptr)

Convert the chemical name specified by 'ptr' from German to English.

See OELanguage for character set information.

#### 3.2.9 OEFromGreek

std::string OEFromGreek (const char \*ptr)

Convert the chemical name specified by 'ptr' from Greek to English.

See OELanguage for character set information.

### 3.2.10 OEFromHTML

std::string OEFromHTML (const char \*ptr)

Convert the string 'ptr' from the HTML character encoding to Lexichem's internal encoding, which uses \u escapes to represent non-ASCII characters. Handles conversion of HTML markup to the to internal markup representation.

### 3.2.11 OEFromHungarian

std::string OEFromHungarian (const char \*ptr)

Convert the chemical name specified by 'ptr' from Hungarian to English.

See OELanguage for character set information.

### 3.2.12 OEFromlrish

std::string OEFromIrish (const char \*ptr)

Convert the chemical name specified by 'ptr' from Irish to English.

See OELanguage for character set information.

### 3.2.13 OEFromItalian

std::string OEFromItalian(const char \*ptr)

Convert the chemical name specified by 'ptr' from Italian to English.

See OELanguage for character set information.

#### 3.2.14 OEFromJapanese

std::string OEFromJapanese (const char \*ptr)

Convert the chemical name specified by 'ptr' from Japanese to English.

See OELanguage for character set information.

### 3.2.15 OEFromKOI8R

std::string OEFromKOI8R(const char \*ptr)

Convert the string 'ptr' from the Russian KOI-8 character encoding to the internal string encoding using \u escapes to represent non-ASCII unicode characters.

## 3.2.16 OEFromLanguage

std::string OEFromLanguage (const char \*ptr, unsigned int lang)

This is a helper wrapper function that can be used to convert the chemical name specified by 'ptr' from the language specified by 'lang' to English. The languages are specified by the constants in the  $OELanguage$  namespace.

## 3.2.17 OEFromLatin1

std::string OEFromLatin1 (const char \*ptr)

Convert the string 'ptr' from the Latin1 character encoding to Lexichem's internal encoding, which uses  $\iota$ u escapes to represent non-ASCII characters.

Note: This function is not available in Java or Python as those language environments use other character sets.

## 3.2.18 OEFromPolish

 $\texttt{std::string } {\texttt{OEFromPolish}}(\textbf{const } \textbf{char } \texttt{~\texttt{+ptr}})$ 

Convert the chemical name specified by 'ptr' from Polish to English.

See OELanguage for character set information.

## 3.2.19 OEFromRomanian

std::string OEFromRomanian(const char \*ptr)

Convert the chemical name specified by 'ptr' from Romanian to English.

See OELanguage for character set information.

### 3.2.20 OEFromRussian

std::string OEFromRussian(const char \*ptr)

Convert the chemical name specified by 'ptr' from Russian to English.

See OELanguage for character set information.

### 3.2.21 OEFromSlovak

std::string OEFromSlovak (const char \*ptr)

Convert the chemical name specified by 'ptr' from Slovak to English.

See OELanguage for character set information.

### 3.2.22 OEFromSpanish

std::string OEFromSpanish(const char \*ptr)

Convert the chemical name specified by 'ptr' from Spanish to English.

See OELanguage for character set information.

### 3.2.23 OEFromSwedish

std::string OEFromSwedish (const char \*ptr)

Convert the chemical name specified by 'ptr' from Swedish to English.

See OELanguage for character set information.

### 3.2.24 OEFromUTF8

std::string OEFromUTF8 (const char \*ptr)

Convert the string 'ptr' from the UTF-8 character encoding to Lexichem's internal encoding, which uses \u escapes to represent non-ASCII characters.

### 3.2.25 OEFromWelsh

std::string OEFromWelsh (const char \*ptr)

Convert the chemical name specified by 'ptr' from simplified or traditional Welsh to English.

See OELanguage for character set information.

### 3.2.26 OEGetCIPStereo

```
char OEGetCIPStereo (const OEChem:: OEMolBase &mol,
                     const OEChem:: OEAtomBase *atm)
char OEGetCIPStereo (const OEChem:: OEMolBase & mol,
                     const OEChem:: OEBondBase *bnd)
```

These functions return the Cahn-Ingold-Prelog descriptor for the given atom or bond stereo center, from the stereochemistry set on the OEMolBase. For chiral atom centers, the OEAtomBase form of this function returns either 'R' or 'S' for specified CIP stereo centers, 'N' for CIP stereo centers that don't have stereo specified (*i.e.* OEAt omBase. Has Stereo Specified returns false), and 'X' for atoms that are not CIP stereo centers. For double bonds, the OEBondBase form of this function returns either 'E' or 'Z' specified CIP stereo centers, 'N' for CIP stereo centers that don't have stereo specified (i.e. OEBondBase.HasStereoSpecified returns false), and 'X' for bonds that are not CIP stereo centers.

### 3.2.27 OEGetIUPACCharSet

unsigned int OEGetIUPACCharSet (std::string &name)

Returns a constant in the OECharSet namespace based on the value of the name.

## 3.2.28 OEGetIUPACLanguage

unsigned int OEGetIUPACLanguage (std::string &name)

Returns a constant in the OELanguage namespace based on the value of the name. Name can be a language name or two-letter country code.

## 3.2.29 OEGetIUPACNamStyle

const unsigned char\* OEGetIUPACNamStyle (const std::string &style);

Returns a pointer to the style ( $OEIUPAC$ ) associated with the given name.

### 3.2.30 OEIUPACGetArch

const char \*OEIUPACGetArch()

Returns the system architecture.

## 3.2.31 OEIUPACGetLicensee

**bool** OEIUPACGetLicensee (std::string &licensee)

Determines the valid licensee.

## 3.2.32 OEIUPACGetPlatform

const char \*OEIUPACGetPlatform()

Returns the system platform.

### 3.2.33 OEIUPACGetRelease

const char \*OEIUPACGetRelease()

Returns the *Lexichem* toolkit release number.

## 3.2.34 OEIUPACGetSite

**bool** OEIUPACGetSite(std::string &site)

Determines whether a valid site is present.

### 3.2.35 OEIUPACGetVersion

unsigned int OEIUPACGetVersion()

Returns *Lexichem* toolkit build date.

### 3.2.36 OEIUPACISLicensed

**bool** OEIUPACIsLicensed (const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any Lexichem TK functionality.

The 'feature' argument can be used to check for a valid license to Lexichem TK along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current Lexichem TK license.

See also:

· OEChemIsLicensed function

## 3.2.37 OELowerCaseName

```
std::string OELowerCaseName(const char *ptr)
```

Convert the specified compound name to lower-case. This function understands chemical nomenclature and foreign alphabets. This function should be called prior to translating a name from a foreign language, as the language translation routines assume that the name is lower-case.

### 3.2.38 OENameLocant

std::string OENameLocant (unsigned int loc, bool iupac=false)

Generate the lexical form of a *Lexichem* locant index. The molecules created by the function OEParseIUPACName are annotated with locant information in each atom's integer atom type field. These locant indices may be retrieved using OEChem's Get IntType method.

#### 3.2.39 OEParseIUPACName

bool OEParseIUPACName(OEChem:: OEMolBase &mol, const char \*name)

This function parses the compound name (not necessarily a systematic or preferred IUPAC name) from the NULLterminated string given by name, and places the processed molecule in mol. This function returns  $true$  if the name could be parsed without problems and false otherwise. If the function returns false, the mol will contain as much of the name as could be processed.

#### 3.2.40 OEReorderIndexName

std::string OEReorderIndexName(const char \*ptr)

Attempt to reorder the specified permuted index name. This permute strings such as "benzene, chloro-" into the form "chloro-benzene" which can then be processed by the  $OEParseIUPACName$  function.

This function returns an empty string (or the original input string) if its argument is not recognized as a permuted index name.

### 3.2.41 OESetCIPStereo

```
bool OESetCIPStereo (OEChem:: OEMolBase &mol,
                     OEChem:: OEAtomBase *atm, char s)
bool OESetCIPStereo (OEChem:: OEMolBase &mol,
                     OEChem::OEBondBase *bnd, char s)
```

Set the internal OEChem stereochemistry from the given CIP stereo descriptor. For OEAtomBase the descriptor must be either 'R' or 'S', and for OEBondBase the descriptor must be either 'E' or 'Z'. Returns  $t$  rue if the stereochemistry was successfully set, and false otherwise: i.e. the descriptor was invalid or the specified atom or bond was not a CIP stereo center.

### 3.2.42 OEToASCII

```
std::string OETOASCII (const char *ptr,
                      const bool remove_markup = true)
```

Convert the string 'ptr', typically the output of the function  $OECreateIUPACName$  optionally post-processed by a language translation function, from the internal encoding, which uses \u escapes to represent non-ASCII characters, into a reduced 7-bit ASCII representation by mapping accented 8-bit characters into their ASCII counterparts.

The 'remove\_markup' flag controls the disposition of italics, superscript, and subscript markup. If the value is true (the default), the markup is removed. If false, the markup is left in the output string, which should be post-processed.

### 3.2.43 OEToBritish

std::string OEToBritish(const char \*ptr, bool sulph)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from the default American output, to either British spelling (when 'sulph' is  $true$ ) or IUPAC international spelling (when 'sulph' is  $false$ ).

See OELanguage for character set information.

### 3.2.44 OEToChinese

std::string OEToChinese(const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreateIDPACName$ , from English to simplified Chinese.

See OELanguage for character set information.

### 3.2.45 OEToDanish

std::string OEToDanish (const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreateIUPACName$ , from English to Danish.

See OELanguage for character set information.

## 3.2.46 OEToDutch

std::string OEToDutch (const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to Dutch.

See OELanguage for character set information.

## 3.2.47 OEToEUCJP

```
std::string OETOEUCJP (const char *ptr)
```

Convert the string 'ptr', typically the output of the function OECreateIUPACName post-processed by a call to OEToJapanese, from the default encoding which uses \u escapes to represent unicode characters to instead use the EUC-JP character encoding for Japanese characters.

### 3.2.48 OEToFrench

std::string OEToFrench (const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to French. See OELanguage for character set information.

#### 3.2.49 OEToGerman

std::string OEToGerman(const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreate IUPACName$ , from English to German. See OELanguage for character set information.

### 3.2.50 OEToGreek

std::string OEToGreek (const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to Greek.

See OELanguage for character set information.

### 3.2.51 OEToHTML

std::string OETOHTML(const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreateIDACName$  optionally post-processed by a language translation function, from the default internal encoding, which uses \u escapes to represent non-ASCII characters, to use HTML mark-up to represent Latin1 characters, unicode characters, italics, superscripts, and subscripts.

#### 3.2.52 OEToHungarian

std::string OEToHungarian (const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreateIUPACName$ , from English to Hungarian.

See OELanguage for character set information.

### 3.2.53 OETolrish

std::string OEToIrish (const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreateIUPACName$ , from English to Irish.

See OELanguage for character set information.

### 3.2.54 OEToltalian

std::string OEToItalian (const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreate IUPACName$ , from English to Italian. See OELanguage for character set information.

### 3.2.55 OEToJapanese

std::string OEToJapanese(const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to Japanese.

See OELanguage for character set information.

### 3.2.56 OEToLanguage

std::string OEToLanguage (const char \*ptr, unsigned int lang)

This is a helper wrapper function that can be used to convert the chemical name specified by 'ptr' from English to the language specified by 'lang'. The languages are specified by the constants in the  $OELanguage$  namespace.

## 3.2.57 OEToLatin1

```
std::string OEToLatin1 (const char *ptr,
                       const bool remove_markup = true)
```

Convert the string 'ptr', typically the output of the function  $OECreate IUPACName$  optionally post-processed by a language translation function, from the internal encoding, which uses \u escapes to represent non-ASCII characters, to Latin1 character encoding.

the 'remove markup' flag controls the disposition of italics, superscript, and subscript markup. If the value is 'true' (the default), the markup is removed. If 'false', the markup is left in the output string, which should be post-processed.

Note: This function is not available in Java or Python as those language environments use other character sets.

### 3.2.58 OEToPolish

std::string OEToPolish(const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to Polish.

See OELanguage for character set information.

### 3.2.59 OEToRomanian

std::string OEToRomanian (const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to Romanian. See OELanguage for character set information.

#### 3.2.60 OEToRussian

std::string OEToRussian(const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreateIUPACName$ , from English to Russian.

See OELanguage for character set information.

## 3.2.61 OEToSJIS

std::string OEToSJIS (const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName post-processed by a call to  $OEToJapanes$  from the default encoding which uses \u escapes to represent unicode characters to instead use the Shift-JIS character encoding for Japanese characters.

### 3.2.62 OEToSlovak

std::string OEToSlovak (const char \*ptr)

Convert the string 'ptr', typically the output of the function *OECreateIUPACName*, from English to Slovak.

See OELanguage for character set information.

### 3.2.63 OEToSpanish

std::string OEToSpanish(const char \*ptr)

Convert the string 'ptr', typically the output of the function  $OECreateIUPACName$ , from English to Spanish. See OELanguage for character set information.

### 3.2.64 OEToSwedish

std::string OEToSwedish(const char \*ptr)

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to Swedish.

See OELanquage for character set information.

## **3.2.65 OEToUTF8**

```
std::string OETOUTF8 (const char *ptr,
                     const bool remove_markup = true)
```

Convert the string 'ptr', typically the output of the function  $OECreateIUPACName$  optionally post-processed by a language translation function, from the internal encoding, which uses \u escapes to represent non-ASCII characters, to UTF-8 character encoding.

The 'remove\_markup' flag controls the disposition of italics, superscript, and subscript markup. If the value is 'true' (the default), the markup is removed. If 'false', the markup is left in the output string, which should be post-processed.

## 3.2.66 OEToWelsh

```
std::string OEToWelsh (const char *ptr)
```

Convert the string 'ptr', typically the output of the function OECreateIUPACName, from English to Welsh.

See OELanguage for character set information.

### **CHAPTER**

## **FOUR**

## **RELEASE HISTORY**

## 4.1 Lexichem TK 2.9.2

Minor internal improvements have been made.

## 4.2 Lexichem TK 2.9.1

Minor internal improvements have been made.

## **4.3 Lexichem TK 2.9.0**

#### 4.3.1 Minor bug fixes

- Custom polymer naming was added in the molecule-to-name workflow to avoid memory overflow when reading in large polymers.
- Kekulization was added in the molecule-to-name workflow to ensure that the same aromatic structures produce the same names.
- · Support was added for some cases of complex (bis-, tris-, tetrakis-, etc.) multipliers in the molecule-to-name and name-to-molecule workflows.

## 4.4 Lexichem TK 2.8.1

Minor internal improvements have been made.

## 4.5 Lexichem TK 2.8.0

### 4.5.1 New features

- Many conventional names for inorganic salts have been added to the name parser.
- Parsing for some non-IUPAC names, including DMF and beta-alanine, have been added.

## 4.5.2 Major bug fixes

- Parsing of many common conventional inorganic salt names, such as calcium chloride, was corrected to include the correct number of anions in the resulting salt.
- Simple salt names no longer include a semicolon between parts of the name.

## 4.5.3 Minor bug fixes

- An issue with ketone oxime stereochemistry naming has been fixed.
- An issue in cycloalkane stereochemistry naming has been fixed.
- An issue in parsing of carbonate salt names has been fixed.

## **4.6 Lexichem TK 2.7.5**

### 4.6.1 New features

• Some new antiviral drug names are now supported in the name to molecule workflow.

## 4.6.2 Minor bug fixes

• A bug with IUPAC naming of pyridine ring substitution has been fixed.

## 4.7 Lexichem TK 2.7.4

Fall 2021

## 4.7.1 New features

• Support for common alkaloid name conversion to SMILES was added.

## 4.7.2 Major bug fixes

• A bug where isotopes were not labeled on certain ring substituents when naming molecules or SMILES has been fixed.

## 4.7.3 Minor bug fixes

- A bug where pyrazole ring substituents were not numbered correctly has been fixed.
- A bug where reaction input was incorrectly parsed into a single molecule has been fixed so that reaction input is now rejected as invalid in the name to molecule workflow.
- A bug where primary amines with non-IUPAC names, such as methylethylamine, were incorrectly parsed into SMILES has been fixed.

## **4.8 Lexichem TK 2.7.3**

July 2021

### 4.8.1 New features

- Support for input of many common drug names has been added.
- Support for SMILES input of disubstituted alkenes when unknown subsituents are marked as \* has been added. For example, SMILES input of  $CCC*$  is now parsed and named as 1,3-disubstituted propylene.

## 4.8.2 Major bug fixes

• An issue with naming of highly branched carbons structures has been fixed.

## 4.9 Lexichem TK 2.7.2

**Fall 2020** 

## 4.9.1 Minor bug fixes

- An issue that caused the function *OEParseIUPACName* to incorrectly interpret elemental halogens as aromatic molecules due to their suffix "ine" has been fixed. Previously, the function failed to kekulize the halogens and therefore failed to parse them.
- An issue that caused the function *OEParseIUPACName* to fail to parse non-IUPAC names of carboxamide derivatives, such as benzimidazole-5-carboxylic acid, due to a failure to kekulize the benzimidazole rings has been fixed. 1H hydrogen is now added by default to benzimidazole if a prefix is not included to specify hydrogen locations.
- An issue that caused the function OEParseIUPACName to fail to parse names, such as carboxylic acid methyl amide, where methyl amide is used as a suffix has been fixed.

## 4.10 Lexichem TK 2.7.1

• Minor internal improvements have been made.

## 4.11 Lexichem TK 2.7.0

• Minor internal improvements have been made.

## 4.12 Lexichem TK 2.6.7

• Minor internal improvements have been made.

## 4.13 Lexichem TK 2.6.6

• Minor internal improvements have been made.

## 4.14 Lexichem TK 2.6.5

### 4.14.1 Minor bug fixes

- The name-to-structure conversion for amino acids has been improved.
- Recognition of several additional unnatural amino acids has been added.
- Problems with stereo handling and substituent numbering of some unnatural amino acids have been corrected.

## **4.14.2 Documentation changes**

• Example documentation has been updated and a -debuq flag has been added to the mol2nam and nam2mol examples.

## 4.15 Lexichem TK 2.6.4

• Minor internal improvements have been made.

## 4.16 Lexichem TK 2.6.3

## 4.16.1 Minor bug fixes

• Previously, redundant cis-trans stereochemistry for certain multi-ring aromatic systems was not suppressed, resulting in names with erroneous E-Z specifications. The stereo perception for these systems has been fixed.

## 4.17 Lexichem TK 2.6.2

## 4.17.1 New features

• The template-based Von Baeyer ring-naming scheme has been replaced with an algorithmic approach. This significantly improves the naming of complex ring systems.

## 4.18 Lexichem TK 2.6.1

## 4.18.1 Minor bug fixes

• A number of new high-frequency von Baeyer ring templates have been added.

## 4.19 Lexichem TK 2.6.0

## 4.19.1 New features

• OEFromBritish function has been added for completeness. The name perception code already handled British-style input names without this conversion function; however, it is useful to have the function available for use by higher-level APIs that dispatch based on input language.

## 4.19.2 Major bug fixes

• Handling of character sets for non-English language names has been improved. The internal string representation of all non-ASCII characters is now their  $\u$  escaped Unicode codepoints. Previously, Latin-1 characters (e.g., the output of the  $OETOFrench)$ ) were encoded as their Latin-1 bytes (0x80 - 0xff). Now they are encoded as escaped unicode. This eliminates character encoding problems for the Java and Python language wrappers that occurred when intermediate name strings were being processed. Now, only the following final character set encoding/decoding functions need to handle non-ASCII bytes: OEFromHTML, OEFromKOI8R, OEFromLatin1, OEFromUTF8, OETOEUCJP, OETOHTML, OETOSJIS, OETOLatin1, and OETOUTF8.

## 4.19.3 Minor bug fixes

• Name-to-structure conversions for certain uncommon functional groups (nitramide, nitrile oxide, oxycyano) previously resulted in structures with 5-valent nitrogen. These now result in charge-separated N(III) structures, consistent with other nitrogen functional groups.

## **4.19.4 Documentation changes**

- The documentation has been updated to indicate the range of Unicode codepoints that are handled for each of the language translation functions. This allows users to determine the appropriate output character set conversion. For example, the Chinese language translation results in CJK characters in the Unicode Basic Multilingual Plane (BMP). Therefore, it is only appropriate to convert Chinese language names to UTF8 or HTML, which can handle the full Unicode BMP. Since the French language translation results in ASCII and Latin-1 characters, it is reasonable to use Latin1, UTF8, or HTML as the output character set.
- The example programs have been updated to better illustrate character set conversions.

## 4.20 Lexichem TK 2.5.2

## 4.20.1 Major bug fixes

• The perception of certain complex ring systems has been changed. Ring systems with three separate fused components are now named using VonBaeyer nomenclature rather than fusion nomenclature. In all but a few cases, these are more closely aligned with the IUPAC preferred names, and the resulting names round trip correctly.

## 4.20.2 Minor bug fixes

• A bug affecting several specific VonBaeyer ring system numberings has been fixed.

## 4.21 Lexichem TK 2.5.1

### 4.21.1 New features

• Approximately 150 additional dictionary entries, including 2014 FDA small-molecule NDA approvals and some isotopic fragments for name suffixes, have been added.

## 4.21.2 Major bug fixes

- The naming of Von Baeyer ring systems has been reworked to fix the numbering assignment. Previously, the substituent ordering was sometimes incorrectly perceived, resulting in names with non-preferred numberings of substituents on rings.
- The naming of Von Baeyer polycyclic systems has been improved.

## 4.21.3 Minor bug fixes

- The handling of vowel elision for certain complex ring systems has been fixed.
- The naming of sulfur stereochemistry has been improved. Instances in which the sulfur stereo is in the suffix of the name  $(e.g., "methyl (S)-methansulfinate")$  are now correctly handled.

## **4.21.4 Documentation changes**

- All examples have been rewritten (see the *Examples* chapter).
- The *translate* examples have been restructured to better handle the input and output character sets.
- Missing documentation for functions OEGetIUPACCharSet, OEGet IUPACLanguage, OEGetIUPACNamStyle, and constants OECharSet has been added. Documentation for other constants has been reworked.

## 4.22 Lexichem TK 2.5.0

### 4.22.1 New features

- Support for text markup (italics, superscripts, subscripts, special characters) has been improved and unified.
  - $-$  OECreateIUPACName function now generates names with the appropriate new text markup tokens (inspired by LaTeX):
    - \* Italics as:  $\sim$ {}
    - \* Subscript as:  $_{\leq}$  { }
    - \* Superscript as:  $\wedge$ {}
  - OETOHTML and OETOUTF8 functions now properly handle the new markup tokens. OETOUTF8 function has a new optional Boolean parameter that controls markup annotations. Set the new parameter to false in order to get the old behavior.
  - $-$  OEF rOMHTML function has been created to properly convert the markup to HTML tags.

## 4.22.2 Bug fixes

- The handling of molecules with relative stereochemistry has been improved. Relative stereochemistry is a feature of the V3000 file format encapsulated in the OEChem TK. See the OEGroupBase class.
- Name generation for molecules with stereochemistry is better due to improvements to the Cahn-Ingold-Prelog stereochemistry perception in **OEChem TK**.

## **4.23 Lexichem TK 2.4.2**

### 4.23.1 Important note

• Custom dictionary entry points added in version 2.4.0 (but not documented) have been removed pending redesign/reimplementation.

## 4.23.2 New features

• New translate examples have been added for all languages (C++, C#, Java, Python).

## 4.23.3 Minor bug fixes

- A memory leak that occurred when naming certain structures with Von Baeyer rings has been fixed.
- String length overflows in language translation code have been fixed. These overflows were functionally benign but did show up with certain sanitizing compilers.
- The internal name dictionary has been cleaned up:
  - The dictionary lookup for names for which one entry is a strict substring of another(eg: AZT and AZTRE-ONAM) has been fixed.
  - All nitro groups are now charge-separated (4-valent).

- Dash vs. space separators are now handled gracefully. Dictionary entries with spaces now also match input names containing dashes.
- Warnings for name conversion failures have been modified. When a name cannot be converted, the warning is now "Failed to parse name: BADNAME". Additional developer-oriented messages about "unexpected tokens" are now debug-level messages and are not seen by default.

## **4.23.4 Documentation fixes**

• PDF documentation will no longer throw a warning about "Arial-Bold bad BBox" in some PDF readers.

## 4.24 Lexichem TK 2.4.1

### 4.24.1 Minor bug fixes

• Tramadol removed from the dictionary since it is actually a racemic structure that was previously being returned as an absolute enantiomer.

## 4.25 Lexichem TK 2.4.0

### 4.25.1 New features

• Support for racemates and enhanced stereochemical name parsing.

## 4.25.2 Minor bug fixes

- Removed unbounded stack allocations.
- Corrected the form of metformin in the dictionary.
- Fixed an issue with names like p/m/o-bis(trifluoromethyl)benzene that were defaulting to the ortho form.
- Fixed parsing of (R,S)-3-ethyl 5-methyl 2-[(2-aminoethoxy)methyl]-4-(2-chlorophenyl)-6-methyl-1,4dihydropyridine-3,5-dicarboxylate.
- Fixed an issue with an unnecessary isotopic prefix in the suffix for peroxycarboxylic acid esters.
- Added a number of ring templates.
- Fixed English to French translations that move the suffixes acetate, chloride, sulfate, and trisulfate to be prefixes connected with the "de" particle.

## 4.26 Lexichem TK 2.3.2

## 4.26.1 New features

- Added phosphorous oxychloride, and gleevec to the dictionary.
- Added a number of additional ring templates.
- Added support for isotopes in naming metal linking groups.
- Added structure to name support for deuterated water and phosphoryl trichloride.
- OEParseIUPACName and OECreateIUPACName will now release the Python global interpreter lock while running.

## 4.26.2 Major bug fixes

• Fixed a memory leak in structure to name generation for simple tricyclic fused ring systems.

## 4.26.3 Minor bug fixes

- Reverted a regression in names like (R)-2-(1H-indol-1-yl)propanoic acid, where the locant position for the CIP stereo center was previously automatically determined.
- Updated the dictionary entry for lipitor to have two atorvastatin molecules and the water of crystallization.
- Updated anthramycin's representation to be canonical and isomeric.
- Tweaked the parser to correctly parse cyclosporin A without a warning.

## 4.27 Lexichem TK 2.3.0

## 4.27.1 New features

- Name generation for racemic structures when the 'MDL AND' group is present in the MDL V3000 format. Stereodescriptors 'rac', 'RS' and 'SR'. (Section P-92.1.3 of the IUPAC Nomenclature of Organic Compounds, Draft 2004 - Racemates and meso compounds). Racemic stereogenic centers are labeled with 'RS' if the CIP stereo descriptor is 'R' and has the MDL AND group present, else 'SR' if the stereogenic center has the CIP stereo descriptor 'S' and an MDL AND group present. The prefix 'rac' is used in front of a set of descriptors or locants, if all stereogenic centers in the molecule are racemic.
- Support has been added for name generation for isotopic carbon atoms in chains (e.g. the SMILES: C[15CH2]C[13CH2]C[15CH2]CCC will generate the name  $(4^{(13)}C, 2, 6^{-(15)}C_{(2)})$  nonane), simple rings and simple suffixes (e.g. the SMILES:  $[13NH2]C = [150]C = C[14CH] = CC = C1$  will generate the name  $(3 \{14\}C)$  cyclohexatriene  $(\{13\}N, \{15\}O)$  carboxamide). The chemical structures generated from parsing the example SMILES strings into a molecule object are depicted in *Figure: Isotope* **Example Depictions.**
- Support for simple rings and simple suffixes in isotopic name generation e.g. **SMILES:**  $[13NH2]C$  (= [150]) C1=C [14CH] = CC=C1 will generate the the name  $(3^{(14)}C)$  cyclohexatriene  $(13)N$ ,  $(15)$ O) carboxamide

(4^{13}C,2,6-^{15}C {2})nonane (3^{14}C)cyclohexatriene(^{13}N,^{15}O)carboxamide  $13NH<sub>2</sub>$ Generated by OEDepict TK

Fig. 1: Isotope Example Depictions

## 4.27.2 Minor bug fixes

- Fixed Lexichem's thread safety. A global variable in Lexichem that has persisted since its first release in 2005, has been removed. This global variable affected the function OEParseIUPACName, used in name to structure conversion. Two thread safety issues used in structure to name conversion, namely: double bond (E/Z) CIP stereo (thread safety broken in the June 2012TK release) and enhanced relative stereochemistry (thread safety broken in the June 2013TK release), that affected the function OECreateIUPACName, have been resolved.
- OEParseIUPACName will no longer access invalid memory for names of the form '(di/tri/tetra)BLAH (ester/hydrazone/oxime/selenoxime/telluroxime/thioxime)'.

## 4.28 Lexichem TK 2.2.3

### 4.28.1 New features

• Added support for relative configuration (P-92.1.2 of IUPAC Nomenclature of Organic Compounds, Draft 2004). The stereodescriptors "rel", "R\*" and "S\*".

## 4.28.2 Minor bug fixes

• The synonym "english" now returns OELanguage:: AMERICAN.

## 4.29 Lexichem TK 2.2.2

## 4.29.1 Bug fixes

- Fixed a number of dictionary entries: arestin, klinomycin, minocin, tetrodotoxin and vectrin.
- Added ring template. For a tetracyclic triaza ring system.
- Added support for automatically determining R/S stereo center position for molecules with 1 stereo center e.g. (R)-2-(1H-indol-1-yl)propanoic acid would set the R on position 2.
- Added the ability to parse names with benzylamide in.

## 4.30 Lexichem TK 2.2.0

## **4.30.1 Feature Requests**

- Added an OEThrow. Warning, warning that names generated with BLAH are incorrect.
- Added support for the token BOC (tert-Butyloxycarbonyl).
- 'OEIUPAC::OEMatchDictionaryNames' added to extract names from Lexichem's dictionary.

### 4.30.2 Bug fixes

- Fixed a number of name failures concerning acenaphthoquinone derivatives.
- Added a number of ring templates and fixed an issue regarding loss of stereochemistry for the name N-[(E)-(1,3-dimethyl-4-piperidylidene)amino]-1,3-dimethyl-piperidin-4-imine on round-tripping.
- Added support for the name 7-chloro-1,3-dihydro-1-methyl-5-phenyl-1,4-benzodiazepin-2(3H)-one.
- Fixed a problem with locant numbering of bicyclic ring systems of the form bicyclo[3.1.0] hexane.
- Fixed rendering of cisplatin.
- Fixed a number of hydrazone entries.
- Removed all duplicates in dictionary.
- Fixed an issue with the name dicyclopentynyl acrylate.
- Fixed crashes on a number of malformed von Baeyer names.
- Fixed bug with sunitinib and triprolidine dictionary entries.
- Fixed 12H-benzo[g]pyrido[2,1-b]quinazoline ring system.

## 4.31 Lexichem TK 2.1.2

### 4.31.1 Bug fixes

- 4-methylimidazole now explicitly adds a hydrogen atom to the nitrogen atom in position 1.
- Added imidazole ring template.
- Added explicit hydrogen to 6 dictionary entries: arestin, klinomycin, minocin, parsalmide, tetrodotoxin and vectrin.
- Fixed crash with name bis(methacryloyloxymethyl)tricyclo[5.2,1,0^{2,6}.
- Fixed crash in name tetraethyn.
- Added ring template: iindeno[7,1-de:1',7'-fg][1,3,2]dioxaphosphocine.
- Corrected dictionary entry: O-orsellinic acid, o-phenanthroline and syrosing opine.

## 4.32 Lexichem TK 2.1.1

### 4.32.1 Bug fixes

- Fixed a bug with structure generation for tetramethylammonium pyrrolidine-2-carboxylate trihydrate.
- Components of salts are now separated by semi-colons.
- Added numerous dictionary entries.
- Added additional ring templates.
- Fixed a bug with names including benzene) or benzene}, the appropriate substitution should have been phenyl.
- Fixed an issue when incorrect von Baeyer names are parsed to Lexichem, Lexichem now fails silently.
- Fixed dictionary lookup algorithm.

- Fixed a crash in Mol2Nam when a H-atom was part of the main ring system in simple spiro compounds.
- Fixed a bug in names like sulfuric acid mono $(x)$  ester.

## 4.33 Lexichem TK 2.1.0

• Performance benchmark results: conversion of canonical isomeric smiles to names and back to the same canonical isomeric smiles. Size of the databases are given in brackets after the name.

|                   | V2.0.2         | V2.1.0         |
|-------------------|----------------|----------------|
| Database          | Round Tripping | Round Tripping |
| Maybridge (63872) | 88.94%         | 98.69%         |
| MDDR (111171)     | 48.69%         | 88.54%         |
| NCI (250251)      | 84.54%         | 92.32%         |
| Wombat (53214)    | 52.80%         | 89.54%         |

### 4.33.1 New features

- Added support for converting von Baeyer names to structures e.g. tricyclo[5.2.2.0^{3,5}] undecane is converted to:C1CC2CCC1CC3CC3C2.
- Added basic support for a number of steroid, alkaloid and terpene parent structures.
- Added support for L/D-amino acids.
- Added support for R-groups for name to structure conversion.
- Added support for both linear and branched polyspiro alicyclic hydrocarbons.
- Activated stereochemistry support for name to structure.
- Added a number of dictionary entries.
- Added a number of ring templates.
- Added partial support for von Baeyer name generation from structures.

## 4.33.2 Bug fixes

- Added support for names: 2H-imidazol-4-thiol and 1,2-dihydroimidazole-5-imine.
- Added support for barium $(2+)$ , sodium $(1+)$ .
- LEXICHEM now understands trifluoroneodymium.
- Added support for dihydrides e.g. calcium dihydride, magnesium dihydride.
- LEXICHEM now supports multi-ammonium salts and multi-derivative ethynyl pyridines.
- Added support for oxoarsinite based compounds.
- Added support for a number of additional metal linking groups e.g. Mg, K, La, Dy, Er, V, Ni etc.
- Fixed a bug in the name: 3-acetyl-8-bromo-1,2,3,6-tetrahydro-azepino[4,5-b]indole-2,5-dicarboxylic acid diethyl ester.
- Corrected unicode conversion for: acetate, glycinate, nitrite and iodide.

## 4.34 Lexichem TK 2.0.2

- Updated ring numbering templates that catch a significant fraction of ring naming failures in the NCBI's Pub-Chem database.
- Updated the rules we use for naming the prefix "2-carboxyethyl" and friends, which we'd previously name "3-hydroxy-3-oxopropyl" (or similar).
- Added parsing support for the traditional prefix "phenethoxy".
- Removed the insertion of a single explicit space after a semi-colon. We now prefer to preserve the original input string, rather than beautify it. This also plays nicer with HTML style input, where "λ" really doesn't need an explicit space character after it.
- Added several minor tweaks to AutoNom-style naming, such as "isophthalic acid" and "benzene-1,2carbaldehyde".
- Updated some erroneous SMILES in the dictionary including sulfamethoxazole and tinidazole.

## 4.35 Lexichem TK 2.0.0

- The applications have a new, standardized command line interface. Please have a look at the updated documentation for mol2nam, nam2mol and translate.
- This release includes the ability to parse stereo on input names. Previously it was read and ignored.
- Fixed a bug where, in rare cases, the output name depended on input atom ordering.
- Fixed a crash in determining CIP stereo for very large, pathological molecules.

## 4.36 Lexichem TK 1.9

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 234297 structures (93.62%) to names without BLAH. Of these 234297 names, nam2mol is able to convert 231566 (98.83%) back into structures.
- This release includes a significant number of improvements to both name generation and name parsing. Several bugs have also been fixed. The name parsing conversion rate for the 71367 compound names in the 2003 Maybridge catalog is now up to 95.24%.
- Several improvements have been made to the specification of CIP stereochemistry during name generation. For example, previously linking groups such as amidino, carbamimidoyl and diazenyl would forget to specify E/Z descriptors if they contained a chiral double bond with specified stereochemistry. We would also fail to place some chiral prefixes such as  $(E)$  -styrl and  $(Z)$  -cinnamyl in brackets which can lead to ambiguity when interpreting the generated name.

## 4.37 Lexichem TK 1.8

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 234296 structures  $(93.62\%)$  to names without BLAH. Of these 234296 names, nam2mo1 is able to convert 228102 (97.36%) back into structures.
- This release includes a significant number of improvements to both name generation and name parsing. Several bugs have also been fixed. The name parsing conversion rate for the 71367 compound names in the 2003 Maybridge catalog is now up to 95.12%.
- One of the major parsing improvements in this release is the much improved support for handling von Baeyer ring nomenclature. We can now parse names such as:
  - '1, 4-dithioniabicyclo[2.2.2] octane',
  - 'bicyclo[4.2.0]octa-1(6), 2, 4-triene' and
  - '2, 4-diazaspiro [4.4] nonane-1, 3-dione'.

## 4.38 Lexichem TK 1.7

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 234155 structures (93.57%) to names without BLAH. Of these 234155 names, nam2mo1 is able to convert 223246 (95.34%) back into structures.
- This release includes a significant number of improvements to both name generation and name parsing. Several bugs have also been fixed. The name parsing conversion rate for the 71367 compound names in the 2003 Maybridge catalog is now up to 93.81%.
- A new OELOWETCaseName function has been added to the Lexichem toolkit API. This function converts the input chemical name to lower-case, whilst preserving the case sensitive aspects of IUPAC names. This functionality allows uppercase and mixed case names to be translated into English, as the OEFrom <Foo> functions assume their input is lowercase. For example, this feature allows AGUA to be recognized via OEFromSpanish.
- A new OEReorderIndexName function has been added to the Lexichem toolkit API. This function attempts to reorder the given permuted index name into a form that can be handled by the OEParseIUPACName function. For example, this will convert the string 'benzene, chloro-' into 'chloro-benzene'.
- A number of improvements and bug fixes have been made to *Lexichem's* naming styles. For example, AutoNom and CAS permuted index styles are now far more AutoNom-like and CAS-like respectively. Naming of metallocenes and fullerenes is much improved.
- Some dramatic improvements have been made with foreign language support. On the 250251 compounds in the NCI00 database mentioned above, we now round-trip 100% to German and back without any differences. Japanese, Spanish and Swedish rates are all currently above 99%. Support for Hungarian and Polish has been dramatically improved.

## 4.39 Lexichem TK 1.6

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 233010 structures (93.11%) to names without BLAH. Of these 233010 names, nam2mo1 is able to convert 221331 (94.99%) back into structures.
- This release includes a significant number of improvements to both name generation and name parsing. For example, both name generation and parsing now do a much better job on ring fusion nomenclature, for names like '5, 6, 7, 8-tetrahydro [1, 2, 4] triazolo [4, 3-a] pyridine'. There's also much improved handling of charged ring systems. The name parsing conversion rate for the 71367 compound names in the 2003 Maybridge catalog is now 93.25% in v1.6, up from 80.80% in v1.5.
- In name generation, new naming styles have been added for MDL/Beilstein AutoNom style names, for CAS permuted index style names (and there are new placeholder styles for IUPAC79 and IUPAC93 naming). A large number of improvements have been made to names generated using the 'traditional' naming style. A new OECapitalizeName API function is available to capitalizing the appropriate first letter of a generated name, such as 'p-tert-Butylbenzoic acid'.
- Several bug fixes have been made to the Cahn-Ingold-Prelog (CIP) chirality perception implementation.
- The OEParseIUPACName function is now able return supplementary locant annotations for each atom. This function now stores an integer locant code/identifier in the integer atom type field of each atom, which may be retrieved using the OEAtomBase. Get IntType method and converted into a readable/displayable string using the recently exposed *OENameLocant* function. This functionality is a recent addition (obviously), and most but not all supported ring systems and parents have locant annotations in this initial release.
- Finally, for the adventurous, new APIs for translating compound names from foreign languages into English are available as the experimental OEFromJapanese, OEFromSwedish and OEFromSpanish functions. Additionally, a OEF romUTF8 function is available for converting UTF-8 encoded strings into the escaped sequences expected by these functions (effectively the inverse of  $OETOUTF8$ ).

## 4.40 Lexichem TK 1.5

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 223066 structures (89.14%) to names without BLAH. Of these 223066 names, nam2mol is able to convert 192487 (86.29%) back into structures.
- This release includes a significant number of improvements to both name generation and name parsing. For example, nam2mol now supports more numbered locants, such as 'N1-methylaniline' and for 'Maybridgestyle' locant names such as  $N'1$  (interpreted as the more common  $N1'$ ). These and similar changes have increased the conversion rate for the 71367 compound names in the 2003 Maybridge catalog, from 69.51% in v1.4 to 80.80% in v1.5.
- This release includes the ability to generate compound names in Japanese, and much improved Spanish and Polish naming support. In order to better support internationalization, APIs are now available to map from the default ISO-8859-1 output to either 7-bit ASCII, UTF-8, HTML and for Japanese locales, Shift-JIS or EUC-JP.
- Although impossible in the general case, several improvements have been made to *Lexichem's* compound naming such that the assigned names are now more stable under arbitrary input ordering of atoms and bonds.

## 4.41 Lexichem TK 1.4

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 221254 structures (88.41%) to names without BLAH. Of these 221254 names, nam2mol is able to convert 192345 (86.93%) back into structures.
- Lexichem v1.4 is predominantly a maintenance to provide a version of the *oeiupac* library that is compatible with *OEChem* v1.4. However, there have been a number of significant improvements to name parsing, and minor improvements to name generation since last month's v1.3 release.
- This release also includes the ability to generate compound names in several languages. In addition, to British spellings, *Lexichem* can now generate German, Italian, French, Spanish, Swedish, Dutch and Polish names. Whilst the translations for German, Italian, Swedish and Polish are quite comprehensive, those for French, Spanish and Dutch are less complete.
- A potential ambiguity with the ring names 'oxazole' and 'thiazole' has also been resolved. The IUPAC documentation states that it is permissible to omit locants from Hantzsch-Widman names when the locants are consecutive, *i.e.* '1, 2, 3, 4-tetrazole' may be written as 'tetrazole', and '1, 2-oxazirene' is preferred as 'oxazirene'. Unfortunately, this conflicts with the traditional interpretations of 'oxazole' as meaning '1, 3-oxazole' and 'thiazole' as '1, 3-thiazole'. Instead the traditional names 'isoxazole' and 'isothiazole' denote the '1, 2-' forms. This ambiguity, that affected IUPAC-style (but not OpenEye-style) names, has been resolved by preserving the locants, so that the IUPAC names '1, 2-oxazole', '1, 3-oxazole', '1, 2-thiazole' and '1, 3-thiazole' are now generated for 'isoxazole', 'oxazole', 'isothiazole' and 'thiazole' respectively.

## 4.42 Lexichem TK 1.3

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 221205 structures  $(88.39%)$  to names without BLAH. Of these 221205 names, nam2mo1 is able to convert 183444 (82.93%) back into structures.
- The major announcement of this release is the support for stereochemistry in compound naming. The CIP rules for assigning R/S descriptors to tetrahedral chiral centers, and E/Z descriptors to double bonds are used during name generation.

## 4.43 Lexichem TK 1.2

On a benchmark of 250251 compounds in the NCI00 database, mol2nam is able to convert 220949 structures  $(88.29%)$  to names without BLAH. Of these 220949 names, nam2mol is able to convert 182438 (82.57%) back into structures.

## 4.44 Lexichem TK 1.1

- On a benchmark of 250251 compounds in the NCI00 database, mollanm is able to convert 220924 structures (88.28%) to names without BLAH. Of these 220924 names, nam2mol is able to convert 177145 (80.18%) back into structures.
- A new OEIUPACI sLicensed API has been added so allow applications to check whether Lexichem's parsing and naming functionality can safely be used.

### 4.44.1 OEParseIUPACName Improvements

The Lexichem name parsing routines now handle a small number of structural abbreviations when parsing names. For example, it can now handle names like '3-CF3-5-NO2-benzoic acid'. The usual improvements in name parsing, including more entries for common names in the Lexichem dictionary. Support for names containing multiple explicit hydrogen locants, such as 'pyrimidine-2, 4 (1H, 3H)-dione' and '2, 4 (1H, 3H)-pyrimidinedione'.

### 4.44.2 OECreateIUPACName Improvements

A serious bug that could cause a core dump when naming thioperoxoic acids has been fixed. The performance of compound naming has been improved. The usual improvements in the names generated (following the IUPAC standards more closely).

## 4.45 Lexichem TK 1.0

On a benchmark of 250251 compounds in the NCI00 database, mol2nam is able to convert 220922 structures  $(88.28%)$  to names without BLAH. Of these 220922 names, nam2mol is able to convert 177032 (80.13%) back into structures.

## 4.45.1 OEParseIUPACName Improvements

In addition to a great many other improvements to the name parsing code, the Lexichem parser now contains an internal dictionary allowing the recognition of common non-systematic names, such as 'ranitidine' and 'zantac'.

## 4.45.2 OECreateIUPACName Improvements

In addition to a great many improvements to the name generation code, the *Lexichem* naming functionality now allows the specification of a naming style, allowing the compound to be named in either a traditional, OpenEye, IUPAC, CAS or systematic naming style.

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

### **CHAPTER**

## **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

#### **CHAPTER**

## **SEVEN**

## **CITATION**

## 7.1 Orion<sup>®</sup> Floes

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

### **CHAPTER**

## **EIGHT**

## **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                                             | License            |
|-------------------------------|-------------------------------------------------------------------------------------|--------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                                | https://           |
| absl-py                       | https://github.com/abseil/abseil-py                                                 | https://           |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                                 | https://           |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                               | https://           |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                               | N/A                |
| AmberUtils                    | http://ambermd.org                                                                  | N/A                |
| ambit                         | https://github.com/khimaros/ambit                                                   | https://           |
| amqp                          | https://github.com/celery/py-amqp                                                   | https://           |
| anaconda-anon-usage           | Orion Floes                                                                         | https://           |
| angular                       | https://github.com/angular/angular.js                                               | https://           |
| angular-animate               | https://github.com/angular/angular.js                                               | https://           |
| angular-cache                 | https://github.com/jmdobry/angular-cache                                            | https://           |
| angular-cookies               | https://github.com/angular/angular.js                                               | https://           |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                                    | https://           |
| angular-mocks                 | https://github.com/angular/angular.js                                               | https://           |
| angular-resource              | https://github.com/angular/angular.js                                               | https://           |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                                    | https://           |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                               | https://           |
| angular-ui-router             | https://github.com/angular-ui/ui-router                                             | https://           |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                                  | https://           |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                                        | https://           |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                                            | https://           |
| annotated-types               | https://github.com/annotated-types/annotated-types                                  | https://           |
| anyio                         | https://github.com/agronholm/anyio                                                  | https://           |
| appdirs                       | http://github.com/ActiveState/appdirs                                               | http://            |
| appengine                     | https://google.golang.org/appengine                                                 | https://           |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                                   | https://           |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md                          | https://           |
| Name of Project               | Website                                                                             | License            |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                | https://           |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                       | https://           |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                          | https://           |
| ascii85                       | https://github.com/huandu/node-ascii85                                              | https://           |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                      | https://           |
| asgiref                       | https://github.com/django/asgiref/                                                  | https://           |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                                 | https://           |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render               | https://           |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers                   | https://           |
| assertions                    | https://github.com/smartystreets/assertions                                         | https://           |
| asttokens                     | https://github.com/gristlabs/asttokens                                              | https://           |
| astunparse                    | https://github.com/simonpercivall/astunparse                                        | https://           |
| async-lru                     | https://github.com/aio-libs/async-lru                                               | https://           |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                           | https://           |
| atk-1.0                       | https://docs.gtk.org/atk/                                                           | https://           |
| atomic                        | https://github.com/uber-go/atomic                                                   | https://           |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                    | https://           |
| attrs                         | https://www.attrs.org/                                                              | https://           |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                                   | https://           |
| Babel                         | https://github.com/python-babel/babel                                               | https://           |
| backcall                      | https://github.com/takluyver/backcall                                               | https://           |
| backports                     | https://github.com/brandon-rhodes/backports                                         | https://           |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                             | https://           |
| base62                        | https://github.com/kare/base62                                                      | https://           |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                      | https://           |
| billiard                      | https://github.com/celery/billiard                                                  | https://           |
| biopython                     | https://biopython.org                                                               | https://           |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https://           |
| bitset                        | https://github.com/willf/bitset                                                     | https://           |
| blas                          | https://www.netlib.org/blas/                                                        | https://           |
| bleach                        | https://github.com/mozilla/bleach                                                   | https://           |
| blessings                     | https://github.com/erikrose/blessings                                               | https://           |
| blinker                       | https://pythonhosted.org/blinker/                                                   | https://           |
| blosc                         | https://github.com/Blosc/python-blosc                                               | https://           |
| blosc2                        | https://github.com/Blosc/python-blosc2                                              | https://           |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https://           |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://           |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://           |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https://           |
| boto3                         | https://github.com/boto/boto3                                                       | https://           |
| botocore                      | https://github.com/boto/botocore                                                    | https://           |
| <b>Bottleneck</b>             | https://bottleneck.readthedocs.io/en/latest/index.html                              | https://           |
| <b>Brotli</b>                 | https://github.com/google/brotli                                                    | https://           |
| brotli-bin                    | https://github.com/google/brotli                                                    | https://           |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | https://           |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                          | https://           |
| bson                          | http://github.com/py-bson/bson                                                      | https://           |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https://           |
| bzip2                         | https://www.bzip.org                                                                | https://           |
|                               | Website                                                                             | J.                 |
| Name of Project               |                                                                                     | Licen              |
| c-ares                        | https://github.com/c-ares/c-ares                                                    | https:/            |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/            |
| cached-property               | https://github.com/pydanny/cached-property                                          | https:/            |
| cachetools                    | https://github.com/tkem/cachetools/                                                 | https:/            |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           | https:/            |
| canvas                        | https://github.com/Automattic/node-canvas                                           | https:/            |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              | https:/            |
| celery                        | https://github.com/celery/celery                                                    | https:/            |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         | https:/            |
| certifi                       | https://certifiio.readthedocs.io/en/latest/                                         | https:/            |
| cffi                          | https://github.com/python-cffi                                                      | https:/            |
| cftime                        | https://pypi.org/project/cftime/                                                    | https:/            |
| chardet                       | https://github.com/chardet/chardet                                                  | https:/            |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        | https:/            |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             | https:/            |
| click                         | https://palletsprojects.com/p/click/                                                | https:/            |
| click-completion              | https://github.com/click-contrib/click-completion                                   | https:/            |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   | https:/            |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      | https:/            |
| click-repl                    | https://github.com/untitaker/click-repl                                             | https:/            |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            | https:/            |
| $c$ make                      | https://cmake.org/                                                                  | https:/            |
| colorama                      | https://github.com/tartley/colorama                                                 | https:/            |
| comm                          | https://github.com/ipython/comm                                                     | https:/            |
| compose                       | https://github.com/docker/compose                                                   | https:/            |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        | https:/            |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      | https:/            |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     | https:/            |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/            |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           | https:/            |
| confuse                       | https://github.com/beetbox/confuse                                                  | https:/            |
|                               | https://github.com/contourpy/contourpy                                              |                    |
| contourpy<br>cpp-peglib       | https://github.com/yhirose/cpp-peglib                                               | https:/            |
| cryptography                  | https://github.com/pyca/cryptography                                                | https:/            |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                                | https:/            |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           | https:/            |
|                               | https://cupy.dev/                                                                   | https:/            |
| $cupy-cuda113$                | https://curl.se                                                                     | https:/            |
| curl                          |                                                                                     | https:/            |
| cycler                        | https://github.com/matplotlib/cycler                                                | https:/            |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             | https:/            |
| Cython                        | https://cython.org                                                                  | https:/            |
| $\overline{d3}$               | https://github.com/mbostock/d3                                                      | https:/            |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           | https:/            |
| ddsketch                      | http://github.com/datadog/sketches-py                                               | https:/            |
| debugpy                       | https://aka.ms/debugpy                                                              | https:/            |
| decimal                       | https://github.com/shopspring/decimal                                               | https:/            |
| decorator                     | https://github.com/micheles/decorator                                               | https:/            |
| deepdiff                      | https://github.com/seperman/deepdiff                                                | https:/            |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             | https:/            |
| Name of Project               | Website                                                                             | License            |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https:/            |
| dill                          | https://github.com/uqfoundation/dill                                                | https:/            |
| distro                        | <b>Orion Floes</b>                                                                  | https:/            |
| Django                        | https://www.djangoproject.com/                                                      | https:/            |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                    | https:/            |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                   | https:/            |
| django-csp                    | https://github.com/mozilla/django-csp                                               | https:/            |
| django-extensions             | https://github.com/django-extensions/django-extensions                              | https:/            |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                          | https:/            |
| django-redis                  | https://github.com/jazzband/django-redis                                            | https:/            |
| django-taggit                 | https://github.com/jazzband/django-taggit                                           | https:/            |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/            |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                              | https:/            |
| djangorestframework           | https://www.django-rest-framework.org/                                              | https:/            |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                      | https:/            |
| dm-tree                       | https://github.com/deepmind/tree                                                    | https:/            |
| docker-py                     | https://github.com/docker/docker-py/                                                | https:/            |
| docopt                        | https://docopt.org                                                                  | https:/            |
| docutils                      | https://docutils.sourceforge.io                                                     | https:/            |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/            |
| editdistance                  | https://github.com/roy-ht/editdistance                                              | https:/            |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/            |
| einops                        | https://github.com/arogozhnikov/einops                                              | https:/            |
| entrypoints                   | https://github.com/takluyver/entrypoints                                            | https:/            |
| errors                        | https://github.com/pkg/errors                                                       | https:/            |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                              | https:/            |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/            |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         | https:/            |
| executing                     | https://github.com/alexmojaki/executing                                             | https:/            |
| expat                         | https://libexpat.github.io                                                          | https:/            |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                   | https:/            |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 | https:/            |
| fftw                          | https://www.fftw.org                                                                | comm               |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              | https:/            |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/            |
| finufft                       | https://github.com/flatironinstitute/finufft                                        | https:/            |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/            |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               | https:/            |
| flit-core                     | https://github.com/pypa/flit                                                        | https:/            |
| <b>FLTK</b>                   | https://www.fltk.org/index.php                                                      | https:/            |
| fmt                           | https://fmt.dev/latest/index.html                                                   | https:/            |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         | https:/            |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      | https:/            |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       | https:/            |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/            |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            | https:/            |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/            |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/            |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/            |
|                               |                                                                                     | Ţ,                 |
| Name of Project               | Website                                                                             | Licen              |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https:/            |
| freetype                      | https://freetype.org                                                                | https:/            |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https:/            |
| frozendict                    | <b>Orion Floes</b>                                                                  | https:/            |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                              | https:/            |
| fsmlite                       | https://github.com/tkem/fsmlite                                                     | https:/            |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                           | https:/            |
| funcy                         | https://github.com/Suor/funcy                                                       | https:/            |
| gast                          | https://github.com/serge-sans-paille/gast/                                          | https:/            |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                | https:/            |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             | https:/            |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https:/            |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             | https:/            |
| genproto                      | https://google.golang.org/genproto/googleapis                                       | https:/            |
| geometric                     | https://openbase.com/python/geometric                                               | https:/            |
| giflib                        | https://giflib.sourceforge.net                                                      | https:/            |
| $g$ lib                       | https://docs.gtk.org/glib/                                                          | https:/            |
| <b>GLM</b> Library            | https://github.com/g-truc/glm                                                       | https:/            |
| gls                           | https://github.com/jtolds/gls                                                       | https:/            |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https:/            |
| go-connections                | https://github.com/docker/go-connections                                            | https:/            |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https:/            |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https:/            |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https:/            |
| go-ini                        | https://github.com/go-ini/ini                                                       | https:/            |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             |                    |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https:/<br>https:/ |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           |                    |
| go-ole                        | https://github.com/go-ole/go-ole                                                    | https:/            |
|                               | https://github.com/go-pg/pg                                                         | https:/            |
| go-pg<br>go-redis             | https://github.com/go-redis/redis/v8                                                | https:/            |
|                               | https://github.com/dgryski/go-rendezvous                                            | https:/            |
| go-rendezvous                 | https://github.com/hashicorp/go-safetemp                                            | https:/            |
| go-safetemp                   |                                                                                     | https:/            |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                              | https:/            |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                                   | https:/            |
| go-units                      | https://github.com/docker/go-units                                                  | https:/            |
| go-version                    | https://github.com/hashicorp/go-version                                             | https:/            |
| go-zglob                      | https://github.com/mattn/go-zglob                                                   | https:/            |
| go.opencensus                 | https://go.opencensus.io                                                            | https:/            |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                | https:/            |
| goconvey                      | https://github.com/smartystreets/goconvey                                           | https:/            |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                       | https:/            |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       | https:/            |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https:/            |
| google-cloud-go               | https://cloud.google.com/go                                                         | https:/            |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 | https:/            |
| google-pasta                  | https://github.com/google/pasta                                                     | https:/            |
| google.golang.org/api         | https://google.golang.org/api                                                       | https:/            |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  | https:/            |
| Name of Project               | Website                                                                             | License            |
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https:/            |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https:/            |
| graphviz                      | https://graphviz.org/                                                               | https:/            |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https:/            |
| groupcache                    | https://github.com/golang/groupcache                                                | https:/            |
| grpc                          | https://google.golang.org/grpc                                                      | https:/            |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https:/            |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/            |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/            |
| gts                           | https://sourceforge.net/projects/gts/                                               | https:/            |
| h5py                          | https://www.h5py.org                                                                | https:/            |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https:/            |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https:/            |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/            |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/            |
| he                            | https://github.com/mathiasbynens/he                                                 | https:/            |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https:/            |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https:/            |
| htslib                        | https://www.htslib.org                                                              | https:/            |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https:/            |
| icu                           | https://github.com/unicode-org/icu                                                  | https:/            |
| idna                          | https://github.com/kjd/idna                                                         | https:/            |
| imageio                       | https://github.com/imageio/imageio                                                  | https:/            |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https:/            |
| ImmuneBuilder                 | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/            |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https:/            |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https:/            |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/            |
| inflection                    | https://github.com/jinzhu/inflection                                                | https:/            |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https:/            |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https:/            |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https:/            |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https:/            |
| ipykernel                     | https://ipython.org                                                                 | https:/            |
| ipython                       | https://ipython.org                                                                 | https:/            |
| ipython-genutils              | http://ipython.org                                                                  | https:/            |
| ipywidgets                    | http://jupyter.org                                                                  | https:/            |
| isodate                       | https://github.com/gweis/isodate/                                                   | https:/            |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https:/            |
| jax                           | https://github.com/google/jax                                                       | https:/            |
| jaxlib                        | https://github.com/google/jax                                                       | https:/            |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              | https:/            |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https:/            |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https:/            |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https:/            |
| jpeg                          | https://www.ijg.org                                                                 | https:/            |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https:/            |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https:/            |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https:/            |
| Name of Project               | Website                                                                             | License            |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:             |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https:             |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https:             |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:             |
| jstat                         | https://github.com/jstat/jstat                                                      | https:             |
| jupyter-client                | https://jupyter.org                                                                 | https:             |
| jupyter-core                  | https://jupyter.org                                                                 | https:             |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https:             |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:             |
| jupyter-server                | https://github.com/jupyter-server/jupyter_server                                    | https:             |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:             |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:             |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:             |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:             |
| jupyter_client                | http://jupyter.org                                                                  | https:             |
| jupyter_core                  | http://jupyter.org                                                                  | https:             |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:             |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:             |
| keras                         | https://github.com/keras-team/keras                                                 | https:             |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:             |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:             |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:             |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:             |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:             |
| kombu                         | https://kombu.readthedocs.io                                                        | https:             |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                       | https:             |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:             |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:             |
| lcms2                         | https://www.littlecms.com                                                           | https:             |
| lerc                          | https://github.com/Esri/lerc                                                        | https:             |
| libarchive                    | http://www.libarchive.org                                                           |                    |
| libblas                       | https://www.netlib.org/blas/                                                        | https:             |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:             |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:             |
| libbrotlienc                  | https://github.com/google/brotli                                                    |                    |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                |
| libclang                      |                                                                                     | https:             |
| libcurl                       | https://curl.se/libcurl/                                                            | https:             |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:             |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:             |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:             |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://            |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:             |
| libffi                        | https://github.com/libffi/libffi                                                    | https:             |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:             |
| libgd                         | https://libgd.github.io                                                             | https:             |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:             |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https:             |
|                               |                                                                                     | J.                 |
| Name of Project               | Website                                                                             | Licen              |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https:/            |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https:/            |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https:/            |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https:/            |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https:/            |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/            |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https:/            |
| libopenblas                   | https://www.openblas.net/                                                           | https:/            |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https:/            |
| libpq                         | https://www.postgresql.org/                                                         | https:/            |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https:/            |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https:/            |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https:/            |
| libtiff                       | https://www.libtiff.org/                                                            | https:/            |
| libtrust                      | https://github.com/docker/libtrust                                                  | https:/            |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https:/            |
| libuv                         | https://github.com/libuv/libuv                                                      | https:/            |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https:/            |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https:/            |
| libxc                         | https://www.tddft.org/programs/libxc/                                               | https:/            |
| libxcb                        | https://xcb.freedesktop.org                                                         | https:/            |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https:/            |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https:/            |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https:/            |
| libzlib                       | https://zlib.net                                                                    | https:/            |
| lime                          | https://github.com/marcoter/lime                                                    | https:/            |
| $\overline{\text{lit}}$       | http://llvm.org                                                                     | https:/            |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https:/            |
| <b>Ilymlite</b>               | http://llvmlite.readthedocs.io                                                      | https:/            |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https:/            |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https:/            |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https:/            |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/            |
| 1xml                          | https://lxml.de                                                                     | https:/            |
| $1z4-c$                       | https://www.lz4.org/                                                                | https:/            |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https:/            |
| markdown-it-py                | <b>Orion Floes</b>                                                                  | https:/            |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https:/            |
| matplotlib                    | https://matplotlib.org                                                              | https:/            |
| matplotlib-base               | https://matplotlib.org                                                              | https:/            |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https:/            |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/            |
| mdtraj                        | https://www.mdtraj.org/                                                             | https:/            |
| mdurl                         | <b>Orion Floes</b>                                                                  | https:/            |
| menuinst                      | <b>Orion Floes</b>                                                                  |                    |
|                               | https://github.com/imdario/mergo                                                    | https:/            |
| mergo                         | https://github.com/lepture/mistune                                                  | https:/            |
| mistune                       | https://github.com/rust-math/intel-mkl-src                                          | https:/            |
| mkl                           |                                                                                     | https:/            |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https:/            |
| Name of Project               | Website                                                                             | License            |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https://           |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https://           |
| ml-dtypes                     | <b>Orion Floes</b>                                                                  | https://           |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https://           |
| moment                        | https://github.com/moment/moment                                                    | https://           |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https://           |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https://           |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https://           |
| mpmath                        | http://mpmath.org/                                                                  | https://           |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https://           |
| msgpack                       | https://msgpack.org/                                                                | https://           |
| multidict                     | https://github.com/aio-libs/multidict                                               | https://           |
| multierr                      | https://go.uber.org/multierr                                                        | https://           |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https://           |
| munkres                       | https://software.clapper.org/munkres/                                               | https://           |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https://           |
| namex                         | <b>Orion Floes</b>                                                                  | https://           |
| nbclassic                     | http://jupyter.org                                                                  | https://           |
| nbclient                      | https://jupyter.org                                                                 | https://           |
| nbconvert                     | https://jupyter.org                                                                 | https://           |
| nbformat                      | http://jupyter.org                                                                  | https://           |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https://           |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https://           |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https://           |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https://           |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https://           |
| networkx                      | https://networkx.org                                                                | https://           |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https://           |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https://           |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https://           |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https://           |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https://           |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https://           |
| nodejs                        | https://nodejs.org/en/                                                              | https://           |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https://           |
| notebook                      | http://jupyter.org                                                                  | https://           |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https://           |
| notebook_shim                 | http://jupyter.org                                                                  | https://           |
| numba                         | https://numba.pydata.org                                                            | https://           |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https://           |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https://           |
| numpy                         | https://numpy.org                                                                   | https://           |
| numpy-base                    | https://numpy.org                                                                   | https://           |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https://           |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://           |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://           |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https://           |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https://           |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https://           |
| Name of Project               | Website                                                                             | License            |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| Oat++                         | https://oatpp.io/                                                                   | https:/            |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https:/            |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https:/            |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/            |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https:/            |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/            |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/            |
| OpenFF                        | https://openforcefield.org/                                                         | https:/            |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/            |
| openff-forcefields            | https://openforcefield.org                                                          | https:/            |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https:/            |
| openff-models                 | https://github.com/openforcefield/openff-models                                     | https:/            |
| openff-toolkit                | https://openforcefield.org                                                          | https:/            |
| openff-toolkit-base           | https://openforcefield.org                                                          | https:/            |
| openff-units                  | https://github.com/openforcefield/openff-units                                      | https:/            |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https:/            |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https:/            |
| openldap                      | https://www.openldap.org/software/repo.html                                         | https:/            |
| OpenMM                        | https://openmm.org                                                                  | https:/            |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https:/            |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https:/            |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https:/            |
| openssl                       | https://www.openssl.org                                                             | https:/            |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https:/            |
| OptKing                       | https://github.com/psi-rking/optking                                                | https:/            |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https:/            |
| overrides                     | https://github.com/mkorpela/overrides                                               | https:/            |
| packaging                     | https://github.com/pypa/packaging                                                   | https:/            |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/            |
| pandas                        | https://pandas.pydata.org                                                           | https:/            |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https:/            |
| Name of Project               | Website                                                                             | License            |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https:/            |
| pango                         | https://pango.gnome.org                                                             | https:/            |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https:/            |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https:/            |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https:/            |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https:/            |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https:/            |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https:/            |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https:/            |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/            |
| pcre                          | https://www.pcre.org                                                                | https:/            |
| pcre2                         | https://www.pcre.org                                                                | https:/            |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https:/            |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https:/            |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https:/            |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https:/            |
| pgio                          | https://github.com/jackc/pgio                                                       | https:/            |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https:/            |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https:/            |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https:/            |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https:/            |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https:/            |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https:/            |
| Pillow                        | https://python-pillow.org                                                           | https:/            |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https:/            |
| pip                           | https://pip.pypa.io/                                                                | https:/            |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https:/            |
| pixman                        | https://pixman.org                                                                  | https:/            |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https:/            |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https:/            |
| plotly                        | https://plotly.com/python/                                                          | https:/            |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https:/            |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https:/            |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/            |
| pooch                         | https://github.com/fatiando/pooch                                                   | https:/            |
| pox                           | https://github.com/uqfoundation/pox                                                 | https:/            |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https:/            |
| pq                            | https://github.com/lib/pq                                                           | https:/            |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https:/            |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https:/            |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/            |
| protobuf                      | https://google.golang.org/protobuf                                                  | https:/            |
| psi4                          | https://psicode.org                                                                 | https:/            |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https:/            |
| psycopg2                      | https://psycopg.org/                                                                | https:/            |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https:/            |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https:/            |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/            |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http://            |
|                               |                                                                                     | Ъ                  |
| Name of Project               | Website                                                                             | Licen              |
| py                            | https://py.readthedocs.io/en/latest/                                                | https:/            |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             | https:/            |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   | https:/            |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           | https:/            |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  | https:/            |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/            |
| pycosat                       | https://github.com/conda/pycosat                                                    | https:/            |
| pycparser                     | https://github.com/eliben/pycparser                                                 | https:/            |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 | https:/            |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           | https:/            |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                | https:/            |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                | https:/            |
| Pygments                      | https://pygments.org                                                                | https:/            |
| pygraphviz                    | https://pygraphviz.github.io                                                        | https:/            |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            | https:/            |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        | https:/            |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  | https:/            |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   | https:/            |
| pymbar                        | https://pymbar.org                                                                  | https:/            |
| pyOpenSSL                     | https://pyopenssl.org/                                                              | https:/            |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/            |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    | https:/            |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 | https:/            |
| pysam                         | https://github.com/pysam-developers/pysam                                           | https:/            |
| PySocks                       | https://github.com/Anorov/PySocks                                                   | https:/            |
| pytables                      | https://www.pytables.org                                                            | https:/            |
| python                        | https://www.python.org/                                                             | https:/            |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          | https:/            |
| python-constraint             | https://github.com/python-constraint/python-constraint                              | https:/            |
| python-dateutil               | https://dateutil.readthedocs.io                                                     | https:/            |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         | https:/            |
| python-Idap                   | https://www.python-ldap.org/                                                        | https:/            |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            | https:/            |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 | https:/            |
| $pyt\bar{z}$                  | https://pythonhosted.org/pytz                                                       | https:/            |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/            |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  | https:/            |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                 |                    |
|                               | No longer available                                                                 | https:/<br>No lor  |
| pyyml                         | https://pyzmq.readthedocs.io/en/latest/                                             |                    |
| pyzmq<br>qcelemental          | https://github.com/MolSSI/QCElemental                                               | https:/            |
|                               | https://github.com/MolSSI/QCEngine                                                  | https:/            |
| qcengine                      | https://github.com/lincolnloop/python-qrcode                                        | https:/            |
| qrcode                        |                                                                                     | https:/            |
| ramda                         | https://github.com/ramda/ramda                                                      | https:/            |
| rapidjson                     | https://rapidjson.org/                                                              | https:/            |
| rdkit                         | https://www.rdkit.org                                                               | https:/            |
| re2                           | https://github.com/google/re2                                                       | https:/            |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             | https:/            |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             | https:/            |
| Name of Project               | Website                                                                             | License            |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https:/            |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https:/            |
| reportlab                     | https://www.reportlab.com                                                           | https:/            |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https:/            |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https:/            |
| requests                      | https://requests.readthedocs.io                                                     | https:/            |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https:/            |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https:/            |
| resumable                     | https://github.com/stevvooe/resumable                                               | https:/            |
| retrying                      | https://github.com/rholder/retrying                                                 | https:/            |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https:/            |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https:/            |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https:/            |
| rich                          | Orion Floes                                                                         | https:/            |
| rpds-py                       | https://github.com/crate/rpds                                                       | https:/            |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https:/            |
| rsa                           | https://stuvel.eu/rsa                                                               | https:/            |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/            |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/            |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https:/            |
| sasl                          | https://mellium.im/sasl                                                             | https:/            |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https:/            |
| scikit-image                  | https://scikit-image.org                                                            | https:/            |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https:/            |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/            |
| scipy                         | https://scipy.org                                                                   | https:/            |
| seaborn                       | https://seaborn.pydata.org                                                          | https:/            |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https:/            |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https:/            |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https:/            |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https:/            |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https:/            |
| sh                            | https://github.com/amoffat/sh                                                       | https:/            |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https:/            |
| simint                        | https://www.bennyop.org/research/simint/                                            | https:/            |
| six                           | https://github.com/benjaminp/six                                                    | https:/            |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https:/            |
| snappy                        | https://github.com/google/snappy                                                    | https:/            |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https:/            |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https:/            |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https:/            |
| spglib                        | Orion Floes                                                                         | https:/            |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https:/            |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/            |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/            |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/            |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/            |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/            |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/            |
|                               |                                                                                     | Ţ,                 |
| Name of Project               | Website                                                                             | Licen              |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          | https:/            |
| sqlite                        | https://sqlite.org/index.html                                                       | https:/            |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            | https:/            |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             | https:/            |
| starfile                      | https://github.com/alisterburt/starfile                                             | https:/            |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          | https:/            |
| structlog                     | https://www.structlog.org/                                                          | https:/            |
| svglib                        | https://github.com/deeplook/svglib                                                  | https:/            |
| sympy                         | https://sympy.org                                                                   | https:/            |
| tables                        | https://www.pytables.org/                                                           | https:/            |
| tabulate                      | https://github.com/astanin/python-tabulate                                          | https:/            |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                | https:/            |
| tenacity                      | https://github.com/jd/tenacity                                                      | https:/            |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           | https:/            |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           | https:/            |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           | https:/            |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            | https:/            |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             | https:/            |
| tensorflow-io-gcs-filesystem  | <b>Orion Floes</b>                                                                  | https:/            |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           | https:/            |
| termcolor                     | https://github.com/hugovk/termcolor                                                 | https:/            |
| terminado                     | https://github.com/jupyter/terminado                                                | https:/            |
| testpath                      | https://github.com/jupyter/testpath                                                 | https:/            |
| textangular                   | https://github.com/fraywing/textAngular                                             | https:/            |
| tf_keras                      | <b>Orion Floes</b>                                                                  | https:/            |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             | https:/            |
| three                         | https://github.com/mrdoob/three.js                                                  | https:/            |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                | https:/            |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  | https:/            |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             | https:/            |
| tk                            | https://www.tcl.tk/                                                                 | https:/            |
| toml                          | https://github.com/toml-lang/toml                                                   | https:/            |
| tomli                         | https://github.com/hukkin/tomli                                                     | https:/            |
| toolz                         | https://github.com/pytoolz/toolz                                                    | https:/            |
| torch                         | https://pytorch.org/                                                                | https:/            |
| tornado                       | https://www.tornadoweb.org                                                          | https:/            |
| tqdm                          | https://github.com/tqdm/tqdm                                                        | https:/            |
| tracy                         | https://github.com/gear-genomics/tracy                                              | https:/            |
| traitlets                     | https://github.com/ipython/traitlets                                                | https:/            |
| triton                        | https://github.com/openai/triton/                                                   | https:/            |
| truststore                    | Orion Floes                                                                         | https:/            |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               | https:/            |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             | https:/            |
| twine                         | https://github.com/pypa/twine                                                       | https:/            |
| twinj uuid                    | https://github.com/twinj/uuid                                                       | https:/            |
| types                         | https://github.com/babel/babel                                                      | https:/            |
| typescript                    | https://github.com/Microsoft/TypeScript                                             | https:/            |
| typing_extensions             | https://github.com/python/typing                                                    | https:/            |
| tzdata                        | https://github.com/python/tzdata                                                    | https:/            |
|                               |                                                                                     |                    |
|                               |                                                                                     | J.                 |
| Name of Project               | Website                                                                             | Licen              |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | https:/            |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | https:/            |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | https:/            |
| uritools                      | https://github.com/tkem/uritools/                                                   | https:/            |
| urli <b>b3</b>                | https://urllib3.readthedocs.io/                                                     | https:/            |
| vine                          | https://github.com/celery/vine                                                      | https:/            |
| vue                           | https://github.com/vuejs/vue                                                        | https:/            |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | https:/            |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | https:/            |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | https:/            |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | https:/            |
| westpa                        | <b>Orion Floes</b>                                                                  | http://            |
| wheel                         | https://github.com/pypa/wheel                                                       | https:/            |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | https:/            |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | https:/            |
| wsutil                        | https://github.com/yhat/wsutil                                                      | https:/            |
| $x/$ lint                     | https://golang.org/x/lint                                                           | https:/            |
| x/mod                         | https://golang.org/x/mod/semver                                                     | https:/            |
| x/net                         | https://golang.org/x/net                                                            | https:/            |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | https:/            |
| x/sys                         | https://golang.org/x/sys                                                            | https:/            |
| x/text                        | https://golang.org/x/text                                                           | https:/            |
| x/tools                       | https://golang.org/x/tools                                                          | https:/            |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | https:/            |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                               | https:/            |
| xlrd                          | https://github.com/python-excel/xlrd                                                | https:/            |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | https:/            |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | https:/            |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https:/            |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https:/            |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https:/            |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https:/            |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https:/            |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https:/            |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https:/            |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https:/            |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https:/            |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https:/            |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https:/            |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https:/            |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | https:/            |
| $\mathbf{X} \mathbf{Z}$       | https://github.com/ulikunitz/xz                                                     | https:/            |
| yaml                          | https://pyyaml.org/                                                                 | https:/            |
|                               | https://github.com/jbeder/yaml-cpp                                                  |                    |
| yaml-cpp                      | https://gopkg.in/yaml.v2                                                            | https:/            |
| yaml.v2                       |                                                                                     | https:/            |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | https:/            |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | https:/            |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | https:/            |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | comm               |
| Name of Project               | Website                                                                             | License            |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                |
| zap                           | https://go.uber.org/zap                                                             | https://           |
| zipp                          | https://github.com/jaraco/zipp                                                      | https://           |
| zlib                          | https://zlib.net/                                                                   | https://           |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https://           |
| zstd                          | https://facebook.github.io/zstd/                                                    | https://           |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https://           |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https://           |

π

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
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

### **8.1.2 GNU GENERAL PUBLIC LICENSE**

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

## F

```
Example Code
   mol2nam_example.py, 8
   nam2mol_example.py, 12
   translate_example.py, 17
```

## M

mol2nam example.py Example Code, 8

## N

nam2mol\_example.py Example Code, 12

## $\Omega$

OEIUPAC:: OECapitalizeName, 29 OEIUPAC:: OECharSet, 23 OEIUPAC:: OECharSet:: ASCII, 23 OEIUPAC:: OECharSet:: DEFAULT, 23 OEIUPAC:: OECharSet:: EUCJP, 24 OEIUPAC:: OECharSet:: HTML, 23 OEIUPAC:: OECharSet:: SJIS, 23 OEIUPAC:: OECharSet:: UTF8, 23 OEIUPAC:: OECreateIUPACName, 29 OEIUPAC:: OEFromBritish, 29 OEIUPAC:: OEFromChinese, 29 OEIUPAC:: OEFromDanish.30 OEIUPAC:: OEFromDutch, 30 OEIUPAC:: OEFromFrench, 30 OEIUPAC:: OEFromGerman, 30 OEIUPAC:: OEFromGreek, 30 OEIUPAC:: OEFromHTML, 30 OEIUPAC:: OEFromHungarian, 31 OEIUPAC:: OEFromIrish, 31 OEIUPAC:: OEFromItalian, 31 OEIUPAC:: OEFromJapanese, 31 OEIUPAC:: OEFromKOI8R, 31 OEIUPAC:: OEFromLanguage, 31 OEIUPAC:: OEFromLatin1, 32 OEIUPAC:: OEFromPolish, 32 OEIUPAC:: OEFromRomanian, 32 OEIUPAC:: OEFromRussian, 32

OEIUPAC:: OEFromSlovak, 32 OEIUPAC:: OEFromSpanish, 33 OEIUPAC:: OEFromSwedish, 33 OEIUPAC:: OEFromUTF8, 33 OEIUPAC:: OEFromWelsh.33 OEIUPAC:: OEGetCIPStereo, 33 OEIUPAC:: OEGetIUPACCharSet, 34 OEIUPAC:: OEGetIUPACLanguage, 34 OEIUPAC:: OEGetIUPACNamStyle, 34 OEIUPAC:: OEIUPAC, 24 OEIUPAC:: OEIUPAC:: OENamStyleACDName, 25 OEIUPAC:: OEIUPAC:: OENamStyleAutoNom, 25 OEIUPAC:: OEIUPAC:: OENamStyleCAS, 24 OEIUPAC:: OEIUPAC:: OENamStyleCASIndex, 24 OEIUPAC:: OEIUPAC:: OENamStyleIUPAC, 24 OEIUPAC:: OEIUPAC:: OENamStyleIUPAC79, 25 OEIUPAC:: OEIUPAC:: OENamStyleIUPAC93, 25 OEIUPAC:: OEIUPAC:: OENamStyleOpenEye, 24 OEIUPAC:: OEIUPAC:: OENamStyleSystematic,  $24$ OEIUPAC:: OEIUPAC:: OENamStyleTraditional,  $24$ OEIUPAC:: OEIUPACGetArch, 34 OEIUPAC:: OEIUPACGetLicensee, 34 OEIUPAC:: OEIUPACGetPlatform, 34 OEIUPAC:: OEIUPACGetRelease, 34 OEIUPAC:: OEIUPACGetSite.35 OEIUPAC:: OEIUPACGetVersion, 35 OEIUPAC:: OEIUPACIsLicensed, 35 OEIUPAC:: OELanguage, 25 OEIUPAC:: OELanguage:: AMERICAN, 25 OEIUPAC:: OELanguage:: BRITISH, 26 OEIUPAC:: OELanguage:: CHINESE, 26 OEIUPAC:: OELanguage:: DANISH, 26 OEIUPAC:: OELanguage:: DUTCH, 26 OEIUPAC:: OELanguage:: ENGLISH, 25 OEIUPAC:: OELanguage:: FRENCH, 26 OEIUPAC:: OELanquage:: GERMAN, 26 OEIUPAC:: OELanguage:: GREEK, 27 OEIUPAC:: OELanquage:: HUNGARIAN, 27 OEIUPAC:: OELanguage:: INTERNATIONAL, 26

OEIUPAC:: OELanquage:: IRISH, 27 OEIUPAC:: OELanguage:: ITALIAN, 27 OEIUPAC:: OELanquage:: JAPANESE, 27 OEIUPAC:: OELanguage:: POLISH, 27 OEIUPAC:: OELanguage:: PORTUGUESE, 27 OEIUPAC:: OELanquage:: ROMANIAN, 28 OEIUPAC:: OELanguage:: RUSSIAN, 28 OEIUPAC:: OELanguage:: SLOVAK, 28 OEIUPAC:: OELanguage:: SPANISH, 28 OEIUPAC:: OELanguage:: SWEDISH, 28 OEIUPAC:: OELanguage:: WELSH, 28 OEIUPAC:: OELOwerCaseName, 35 OEIUPAC:: OENameLocant, 35 OEIUPAC:: OEParseIUPACName, 36 OEIUPAC:: OEReorderIndexName, 36 OEIUPAC:: OESetCIPStereo, 36 OEIUPAC:: OETOASCII, 36 OEIUPAC:: OEToBritish, 36 OEIUPAC:: OEToChinese, 37 OEIUPAC:: OEToDanish, 37 OEIUPAC:: OEToDutch, 37 OEIUPAC:: OETOEUCJP, 37 OEIUPAC:: OEToFrench, 37 OEIUPAC:: OEToGerman. 38 OEIUPAC:: OEToGreek, 38 OEIUPAC:: OETOHTML, 38 OEIUPAC:: OETOHungarian, 38 OEIUPAC:: OEToIrish, 38 OEIUPAC:: OEToItalian, 38 OEIUPAC:: OEToJapanese, 39 OEIUPAC:: OEToLanguage, 39 OEIUPAC:: OEToLatin1.39 OEIUPAC:: OEToPolish, 39 OEIUPAC:: OEToRomanian, 39 OEIUPAC:: OEToRussian, 40 OEIUPAC:: OETOSJIS, 40 OEIUPAC:: OEToSlovak, 40 OEIUPAC:: OEToSpanish, 40 OEIUPAC:: OEToSwedish, 40 OEIUPAC:: OETOUTF8, 40 OEIUPAC:: OETOWelsh, 41

## Т

translate\_example.py Example Code, 17