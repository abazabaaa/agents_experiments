![](_page_0_Picture_0.jpeg)

# **OEDocking TK - Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1 Introduction                                                                                 | 1   |
|------------------------------------------------------------------------------------------------|-----|
| <span style="padding-left:20px">1.1 Welcome to the Docking Toolkit documentation</span>        | 1   |
| 2 Theory                                                                                       | 1   |
| <span style="padding-left:20px">2.1 Receptors</span>                                           | 1   |
| <span style="padding-left:40px">2.1.1 Creating a Receptor</span>                               | 1   |
| <span style="padding-left:40px">2.1.2 Contents of a Receptor</span>                            | 1   |
| <span style="padding-left:20px">2.2 Scoring</span>                                             | 1   |
| <span style="padding-left:40px">2.2.1 Scoring Function Implementations</span>                  | 1   |
| <span style="padding-left:20px">2.3 Docking</span>                                             | 1   |
| <span style="padding-left:40px">2.3.1 Scoring Functions and Search Resolution</span>           | 1   |
| <span style="padding-left:40px">2.3.2 Initialization</span>                                    | 1   |
| <span style="padding-left:40px">2.3.3 Docking Molecules</span>                                 | 1   |
| <span style="padding-left:40px">2.3.4 Scoring Molecules</span>                                 | 1   |
| <span style="padding-left:40px">2.3.5 Docking Algorithm</span>                                 | 1   |
| <span style="padding-left:20px">2.4 ShapeFit</span>                                            | 1   |
| <span style="padding-left:40px">2.4.1 On Clashes</span>                                        | 1   |
| <span style="padding-left:20px">2.5 POSIT Theory</span>                                        | 1   |
| <span style="padding-left:40px">2.5.1 Handling of isomerisms and chirality</span>              | 1   |
| <span style="padding-left:40px">2.5.2 Estimated Pose Probability</span>                        | 1   |
| <span style="padding-left:40px">2.5.3 Additional MCS Constraints</span>                        | 1   |
| <span style="padding-left:40px">2.5.4 On Clashes</span>                                        | 1   |
| <span style="padding-left:40px">2.5.5 Using Multiple Receptors</span>                          | 1   |
| <span style="padding-left:40px">2.5.6 Receptor Flexibility</span>                              | 1   |
| <span style="padding-left:40px">2.5.7 TanimotoCombo</span>                                     | 1   |
| <span style="padding-left:20px">2.6 Posit How to</span>                                        | 1   |
| <span style="padding-left:40px">2.6.1 Ignore Nitrogen stereo</span>                            | 1   |
| <span style="padding-left:40px">2.6.2 Prepare molecules for Posit</span>                       | 1   |
| <span style="padding-left:40px">2.6.3 Use multiple receptors</span>                            | 1   |
| <span style="padding-left:40px">2.6.4 Obtain clash-free pose</span>                            | 1   |
| 3 OEDocking Examples                                                                           | 1   |
| <span style="padding-left:20px">3.1 Docking and Scoring Examples</span>                        | 1   |
| <span style="padding-left:40px">3.1.1 Docking Molecules</span>                                 | 1   |
| <span style="padding-left:40px">3.1.2 Rescoring Docked Molecules</span>                        | 2   |
| <span style="padding-left:20px">3.2 OEShapeFit Examples</span>                                 | 2   |
| <span style="padding-left:40px">3.2.1 Flexible Overlay Optimization with OEShapeFit API</span> | 2   |
| <span style="padding-left:20px">3.3 POSIT Examples</span>                                      | 2   |
| <span style="padding-left:40px">3.3.1 Generating Poses with POSIT</span>                       | 2   |
| <span style="padding-left:40px">3.3.2 Generating Multiple Poses with POSIT</span>              | 2   |
| 3.4 Receptor Examples                                                                          | 28  |
| 3.4.1 Making a Receptor                                                                        | 29  |
| 3.4.2 Receptor Contour Volume                                                                  | 30  |
| 3.4.3 Toggle Receptor Inner Contour                                                            | 31  |
| 3.4.4 Set Receptor Contour Volume                                                              | 32  |
| 4 OEModels Examples                                                                            | 35  |
| 4.1 Building ROCS Query Model                                                                  | 35  |
| 5 API                                                                                          | 37  |
| 5.1 OEDocking API                                                                              | 37  |
| 5.1.1 OEDocking Classes                                                                        | 37  |
| 5.1.2 OEDocking Constants                                                                      | 65  |
| 5.1.3 OEDocking Functions                                                                      | 76  |
| 5.2 Preliminary OEDocking API                                                                  | 85  |
| 5.2.1 Preliminary OEDocking Classes                                                            | 85  |
| 5.3 Deprecated OEDocking API                                                                   | 90  |
| 5.3.1 OEDocking Classes (Deprecated)                                                           | 90  |
| 5.3.2 OEDocking Functions (Deprecated)                                                         | 102 |
| 5.4 OEModels API                                                                               | 116 |
| 5.4.1 Preliminary OEModels Classes                                                             | 116 |
| 6 Release History                                                                              | 121 |
| 6.1 OEDocking TK 4.3.2                                                                         | 121 |
| 6.1.1 New features                                                                             | 121 |
| 6.1.2 Major bug fixes                                                                          | 121 |
| 6.1.3 Minor bug fixes                                                                          | 121 |
| 6.2 OEDocking TK 4.3.1                                                                         | 122 |
| 6.3 OEDocking TK 4.3.0                                                                         | 122 |
| 6.3.1 New features                                                                             | 122 |
| 6.3.2 Major bug fixes                                                                          | 122 |
| 6.3.3 Minor bug fixes                                                                          | 122 |
| 6.4 OEDocking TK 4.2.1                                                                         | 123 |
| 6.4.1 New features                                                                             | 123 |
| 6.4.2 Major bug fixes                                                                          | 123 |
| 6.4.3 Minor bug fixes                                                                          | 123 |
| 6.4.4 Documentation changes                                                                    | 123 |
| 6.5 OEDocking TK 4.2.0                                                                         | 124 |
| 6.5.1 New features                                                                             | 124 |
| 6.5.2 Major bug fixes                                                                          | 124 |
| 6.5.3 Documentation changes                                                                    | 124 |
| 6.6 OEDocking TK 4.1.2                                                                         | 124 |
| 6.7 OEDocking TK 4.1.1                                                                         | 124 |
| 6.7.1 New features                                                                             | 124 |
| 6.7.2 Minor bug fixes                                                                          | 125 |
| 6.7.3 Documentation changes                                                                    | 125 |
| 6.8 OEDocking TK 4.1.0                                                                         | 125 |
| 6.8.1 New features                                                                             | 125 |
| 6.8.2 Minor bug fixes                                                                          | 125 |
| 6.9 OEDocking TK 4.0.0.2                                                                       | 125 |
| 6.10 OEDocking TK 4.0.0                                                                        | 126 |
| 6.10.1 New features                                                                            | 126 |
| 6.10.2 Documentation changes                                                                   | 126 |
| 6.11 OEDocking TK 3.5.0.5                                                                      | 128 |
| 6.12 OEDocking TK 3.5.0                                                                        | 121 |
| 6.12.1 New features                                                                            | 121 |
| 6.12.2 Major bug fixes                                                                         | 121 |
| 6.12.3 Minor bug fixes                                                                         | 121 |
| 6.12.4 Documentation changes                                                                   | 121 |
| 6.13 OEDocking TK 1.4.1                                                                        | 122 |
| 6.13.1 New features                                                                            | 122 |
| 6.13.2 Major bug fixes                                                                         | 122 |
| 6.13.3 Minor bug fixes                                                                         | 122 |
| 6.13.4 Documentation changes                                                                   | 122 |
| 6.14 OEDocking TK 1.4.0                                                                        | 123 |
| 6.14.1 Major bug fixes                                                                         | 123 |
| 6.14.2 Minor bug fixes                                                                         | 123 |
| 6.15 OEDocking TK 1.3.7                                                                        | 124 |
| 6.16 OEDocking TK 1.3.6                                                                        | 124 |
| 6.16.1 New features                                                                            | 124 |
| 6.17 OEDocking TK 1.3.5                                                                        | 125 |
| 6.18 OEDocking TK 1.3.4                                                                        | 125 |
| 6.19 OEDocking TK 1.3.3                                                                        | 125 |
| 6.20 OEDocking TK 1.3.2                                                                        | 126 |
| 6.21 OEDocking TK 1.3.1                                                                        | 126 |
| 6.21.1 New features                                                                            | 126 |
| 6.21.2 C++-specific changes                                                                    | 126 |
| 6.22 OEDocking TK 1.3.0                                                                        | 127 |
| 6.22.1 Minor bug fixes                                                                         | 127 |
| 6.22.2 Python-specific changes                                                                 | 127 |
| 6.23 OEDocking TK 1.2.7                                                                        | 127 |
| 6.23.1 Minor bug fixes                                                                         | 127 |
| 6.24 OEDocking TK 1.2.6                                                                        | 128 |
| 6.24.1 New features                                                                            | 128 |
| 6.24.2 Minor bug fixes                                                                         | 128 |
| 6.25 OEDocking TK 1.2.5                                                                        | 129 |
| 6.25.1 New features                                                                            | 129 |
| 6.25.2 Minor bug fixes                                                                         | 129 |
| 6.26 OEDocking TK 1.2.4                                                                        | 129 |
| 6.27 OEDocking TK 1.2.3                                                                        | 130 |
| 6.27.1 New features                                                                            | 130 |
| 6.27.2 Major bug fixes                                                                         | 130 |
| 6.27.3 Minor bug fixes                                                                         | 130 |
| 6.28 OEDocking TK 1.2.2                                                                        | 131 |
| 6.28.1 New features                                                                            | 131 |
| 6.28.2 Major bug fixes                                                                         | 131 |
| 6.28.3 Minor bug fixes                                                                         | 131 |
| 6.28.4 Documentation Changes                                                                   | 132 |
| 6.29 OEDocking TK 1.2.1                                                                        | 132 |
| 6.29.1 New features                                                                            | 132 |
| 6.29.2 Major bug fixes                                                                         | 133 |
| 6.29.3 Minor bug fixes                                                                         | 133 |
| 6.30 OEDocking TK 1.2.0                                                                        | 133 |
| 6.30.1 New features                                                                            | 134 |
| 6.31 OEDocking TK 1.1.4                                                                        | 134 |
| 6.31.1 New features                                                                            | 134 |
| 6.31.2 Minor bug fixes                                                                         | 135 |
| 6.32 OEDocking TK 1.1.3                                                                        | 135 |
| 6.32.1 Bug fixes                                                                               | 136 |
| 6.33 OEDocking TK 1.1.2                                                                        | 136 |
| 6.33.1 Bug fixes                                                                               | 136 |
| 6.33.2 Improvements                                                                            | 136 |
| 6.34 OEDocking TK 1.1.1                                                                        | 136 |
| 6.34.1 Bug fixes                                                                               | 136 |
| 6.35 OEDocking TK 1.1.0                                                                        | 136 |
| 6.35.1 New Features                                                                            | 137 |
| 6.35.2 Bug fixes                                                                               | 137 |
| 6.36 OEDocking TK 1.0.0                                                                        | 137 |
| <b>7 Copyright and Trademarks</b>                                                              | 139 |
| <b>8 Sample Code</b>                                                                           | 141 |
| <b>9 Citation</b>                                                                              | 143 |
| 9.1 Orion® Floes                                                                               |     |
| 9.2 Toolkits and Applications                                                                  |     |
| 9.3 OpenEye Web Services                                                                       |     |
| <b>10 Technology Licensing</b>                                                                 | 147 |
| 10.1 GCC                                                                                       | 162 |
| 10.1.1 GCC RUNTIME LIBRARY EXCEPTION                                                           | 162 |
| 10.1.2 GNU GENERAL PUBLIC LICENSE                                                              | 162 |

# **INTRODUCTION**

## 1.1 Welcome to the Docking Toolkit documentation

The Docking Toolkit library provides a facility for docking and scoring molecules in the context of a protein active site.

The following basic functionalities are available:

- Docking (see Docking chapter)
- Pose Prediction (see POSIT Theory chapter)
- Scoring (see Scoring chapter)

The aim of this manual is to familiarize the user with the *Docking Toolkit* functionalities, however, it does not provide explanations of basic OEChem classes and functions. Therefore reading the OEChem manual beforehand is highly recommended.

## See also:

- Python Quick Start Manual for installation instructions.
- Importing Python Toolkits section

# **THEORY**

## 2.1 Receptors

In receptor objects contain information about the location and characteristics of the binding pocket, and required for docking (see *Docking*), posit (see POSIT), and scoring (see *Scoring*).

A receptor is an OEReceptor object that resides within a OEDesignUnit. The essential component of a valid receptor is the negative image that describes the shape of the active site.

### 2.1.1 Creating a Receptor

Within the Docking toolkit the OEMakeReceptor function is used to create a receptor from the structure of a target protein containing in a OEDesignUnit.

The protein structure should only include molecules the ligand is expected to interact with. In general crystallographic waters, other solvents and the bound ligand should be not be included as part of the target protein structure passed to the OEMakeReceptor function, although in certain cases, the user may wish to retain certain key molecules as part of the target protein structure  $(e.g. a crystallographic water)$ .

### 2.1.2 Contents of a Receptor

#### **Negative Image**

The negative image describes the shape of the active site. It is stored as a potential grid surrounding the active site. Potential values are always greater than or equal to zero. The negative image has high potentials where ligand atoms make many contacts with atoms of the active site without clashing and in positions some ligand atoms are likely to occupy when other atoms of the ligand make good contacts with the receptor  $(e,g, g)$  bridging positions ligand atoms will likely occupy when a ligand is stretched between two pockets).

During docking two shapes are created by contouring the negative image potential grid. The two shapes control the docking process as follows:

#### **Outer Contour Shape**

During docking any pose examined by the exhaustive search that does not fit within this shape will be rejected. A pose is considered to fit if the center of every heavy atom is within this shape. The volume of this shape is typically between 500 and 2000 cubic Angstroms.

#### **Inner Contour Shape**

During docking any pose examined by the exhaustive search that does not touch this shape is rejected. A pose is considered to touch if the center of at least one heavy atom falls within this shape. The volume of this shape is typically 50 to 100 cubic angstroms.

While neither the *outer contour* nor the *inner contour* shape are required, it is recommended that the *outer contour* always be used (docking speed will be dramatically slower without the *outer contour*). Using the *inner contour* improves docking speed slightly at the expense of sampling.

The negative image of the receptor is setup when the receptor is created with the  $OEMakeReceptor$  function (see Creating a Receptor section). The size of the outer contour and inner contour shapes are controllable by setting the contour level used to create the shape from the negative image. The  $OEMakeRecept \, or \, function$  will automatically set a reasonable contour level for both the *inner contour* and *outer contour*, however the *inner contour* will be disabled by setting the value to be negative (see below).

The negative image grid has only positive values, thus only contour levels that are positive create a shape. When either the outer contour level or inner contour level are negative that contour shape will be disabled (i.e. ignored during the docking process).

The volume of the *outer contour* shape has a significant effect on docking speed, while the volume of the *inner contour* shape has a modest effect on docking speed. In both cases the smaller volumes increase docking speed by reducing the number of poses that are scored. In general an outer and inner contour volume of between 500-2000 and 50-100 cubic Angstroms respectively is recommended.

## **Constraints**

Constraints are key interactions ligands are required to make when docking into the active site. They are optional and user defined.

Constraints do not affect how a given pose scores, however they do affect how the docking algorithm chooses poses to score during the docking process. Any pose that does not match the docking constraints will be rejected and replaced by the next best scoring pose. If no poses of a ligand match the docking constraints the ligand will not be docked. If multiple constraints are specified every constraint must be satisfied or the pose will be rejected.

**Note:** The docking process has a resolution of approximately 1 Angström, and thus the constraints have a similar resolution. Therefore it is possible that poses docked with a constraint may have small violations of the constraint distance, up to approximately 1 Ångström.

Receptors support two general classes of constraints; protein constraints and custom constraints. There may be any number of either class of constraint.

Note: Each individual custom or protein constraint has an enabled flag. A disabled constraint is ignored during the docking process.

### **Protein Constraints**

A protein constraint specifies an interaction that must be made with a **heavy atom** of the protein structure *(i.e.* protein constraints cannot be placed on hydrogen atoms). There are five types of protein constraints.

#### **Contact**

A contact constraint is satisfied when any ligand heavy atom is within 4 angstroms of the protein heavy atom.

#### Lipophilic

A lipophilic constraint is satisfied when any non-polar heavy atom on the ligand is within 4 angstroms of the protein heavy atom.

#### **Donor**

A donor constraint is satisfied when a *donor on the ligand* makes a hydrogen bond interaction with the protein heavy atom.

#### Acceptor

An acceptor constraint is satisfied when an *acceptor on the ligand* makes a hydrogen bond interaction with the protein heavy atom. Acceptor constraints must be placed on the protein heavy atom the donor hydrogen is interacting with.

#### **Chelator**

A chelator constraint is satisfied when a *chelator on the ligand* makes a metal-chelator interaction with the protein heavy atom.

Only one protein constraint is allowed per protein heavy atom. If a protein constraint is set on a protein atom that already has a protein constraint the original protein constraint will be discarded and replaced by the new constraint.

## **Custom Constraints**

A custom constraint consists of one or more spheres within the receptor active site, and optionally a list of SMARTS patterns. A custom constraint is satisfied when a matching atom on the ligand falls within any of the spheres associated with the custom constraint. If no SMARTS patterns are specified any heavy atom on the ligand can satisfy the constraint, otherwise only atoms that match one of the smarts patterns can satisfy the constraint.

## 2.2 Scoring

Scoring functions in the *Docking Toolkit* measure the fitness of ligands posed within the active site of a target protein and assign them a numerical score. Poses with better scores are more likely to be correctly docked compared to other poses of the same ligand. The score of a ligand is the best score of any pose of that ligand, and ligands with better scores are more likely to be active against the target protein compared to other ligands docked.

The following scoring functions are implemented in *Docking TK* 

- 1. Shapegauss (OEScoreType\_Shapegauss)
- 2. PLP (OEScoreType\_PLP)
- 3. Chemgauss3 (OEScoreType\_Chemgauss3)
- 4. Chemgauss4 (OEScoreType Chemgauss4)
- 5. Chemscore (OEScoreType\_Chemscore)

In the Docking Toolkit scoring, optimization and score annotation with any of these scoring functions is done using the OEScore class.

Rescoring Docked Molecules is an example program that uses the OEScore class to score, optimize and annotate poses.

## **2.2.1 Scoring Function Implementations**

### **Shapegauss**

Shapegauss [McGann-2003] is a shape based scoring function that favors poses that complement the active site well, regardless of any chemical interactions (e.g. hydrogen bonds). The Shapegauss scoring function represents the shape of each atom as a smooth Gaussian function.

The Shapegauss score is calculated by summing a pairwise potential between all protein atoms and all ligand heavy atoms. This potential is most favorable when the two atoms touch but do not overlap. A correction term is then applied to further penalize atoms which significantly overlap the protein.

For Shapegauss a lower score indicates a better result.

## **PLP**

PLP [Verkhivker-2000] or Piecewise Linear Potential scoring function calculates both the shape and hydrogen bond complementarity of poses to the active site.

The PLP score is a pairwise additive scoring function. All pairs of ligand-protein heavy atoms are assigned either a hydrogen bonding potential, if the pair is an acceptor-donor pair, or otherwise a lipophilic potential. These pairwise potentials are summed to obtain the final pose score.

The PLP implementation in the *Docking Toolkit* has also been extended to include interaction between metals on the target protein and acceptors on the ligand.

For PLP a lower score indicates a better result.

## **Chemscore**

Chemscore [Eldridge-1997] is a sum of the following interaction terms

### lipophilic

Favorable interactions that occur when two non-polar heavy atoms (one ligand atom and one protein atom) are placed near each other.

#### hydrogen bonding

Favorable interactions that occur when acceptor-donor interactions are formed between the ligand and protein.

#### metal chelator

Favorable interactions that occur when acceptor atoms on the ligand are placed near metal atoms on the protein.

#### clash

Penalty term that occurs when heavy atoms on the ligand and protein clash.

#### rotatable bond

This penalty term is proportional to the number of rotatable bonds on the ligand that are no longer free to rotate when the ligand is docked.

For Chemscore a lower score indicates a better result.

## **Chemgauss3**

The Chemgauss3 scoring function uses Gaussian smoothed potentials to measure the complementarity of ligand poses within the active site. Chemgauss3 recognizes the following types of interactions.

- Shape
- Hydrogen bonding between ligand and protein
- Hydrogen bonding interactions with implicit solvent
- Metal-chelator interactions.

All interaction potentials in Chemgauss are initially constructed using step functions to describe the interaction of atom pairs (or other chemical points) as a function of distance. These interactions are mapped onto a grid that is then convoluted with a spherical Gaussian function, which smoothes the potential making it less sensitive to small changes in the ligand position. Smoothing the score in this way serves two purposes, first docking can be run at lower resolution than would be required if the score were not smooth since small changes in position to do not cause large changes in score. Second it reduces the error associated with the rigid protein approximation by effectively accounting for the ability of the protein to make small structural re-arrangements to accommodate the ligand.

Shape interactions in Chemgauss are based on a united atom model (*i.e.* only heavy atoms are relevant to the shape calculation). Each ligand heavy atom is assigned a fixed clash penalty score if the distance between it and a protein heavy atom is less than the sum of the VdW radii, otherwise it is assigned a score proportional to the count of the number of protein heavy atoms within 1.25 and 2.5 times the sum of the VdW radii (atoms within 2.5 count one tenth as much as those within 1.25). From this score a penalty equal to two close protein atom contacts is subtracted to represent the VdW interactions with solvent water that are lost when the ligand docks. This score is pre-computed at grid points throughout the active site and the resulting grid is then smoothed.

Hydrogen bonding groups are modeled with one or more lone-pair or polar-hydrogen positions that describe the directionality of potential hydrogen bonds (with respect to the hydrogen bonding group's heavy atom). Donor groups have lone pair positions representing the possible location of the donor hydrogen atoms relative to the donating molecule, while acceptors have lone-pair positions representing the possible locations of the donated hydrogen relative to the acceptor. A hydrogen bond is detected and assigned a constant score when a hydrogen bonding position on the ligand is within 1.0 Angstroms of a complementary hydrogen bonding position on the protein (i.e. when the polar-hydrogen position of a donor overlaps the lone-pair position of an acceptor). If the ligand hydrogen bonding group has multiple polar-hydrogens and/or lone-pair positions (groups can be both donors and acceptors) then this calculation is performed for each position and the result is summed. As with all Chemgauss terms the hydrogen bond potential is pre-computed at grid points throughout the site and then smoothed.

Hydrogen bonds with solvent that break when the ligand docks into the active site are penalized by the Chemgauss scoring function. Broken protein-solvent hydrogen bonds are accounted for by calculating how many hydrogen bonds water can make with the protein at the position of each heavy atom of the docked ligand, and a penalty score is assigned which is proportional to the number of hydrogen bonds. Broken ligand-solvent hydrogen bonds are accounted for by calculating desolvation positions around each hydrogen-bonding group on the ligand that represent the positions water could occupy when making a hydrogen bonding interaction with the protein. A penalty is then assessed that is proportional to the number of desolvation positions that can no longer be occupied by water because the water in these positions would clash with the protein. As before, this potential is placed on a grid and smoothed.

Chelating interactions between protein metals and ligand chelating groups are accounted for by Chemgauss (proteinchelator and ligand-metal chelating interactions are not). For each chelator on the ligand one or more chelatingpositions are calculated. If a protein metal is within 1.0 Angstroms of any chelating-position of a chelating group then a fixed score is assigned, otherwise a zero score is assigned. As before this potential is placed on a grid and smoothed.

For Chemgauss3 a lower score indicates a better result.

## **Chemgauss4**

The Chemgauss4 is a modification of the Chemgauss3 scoring function that has improved hydrogen bonding and metal chelator (The shape and implicit solvent interaction terms are identical to those in Chemgauss3). The new hydrogen bonding and metal chelator terms have better perception of the directionality of these interactions and also account for hydrogen bond networking effects.

To calculate the hydrogen bonding score for a ligand-protein hydrogen bond two distances are measured.

- 1. How far the donor heavy atom is from the position the acceptor atom would consider to be an ideal for a hydrogen bonding to form.
- 2. How far the acceptor heavy atom is from the position the donor atom would consider to be ideal for a hydrogen bonding interaction to occur.

The score for the hydrogen bond interaction is a product of two Gaussian functions of these distances scaled by the strength of the hydrogen bonding groups involved in the interaction.

 $HBscore = strength * g(distance1) * g(distance2)$ 

To compute the total hydrogen bonding score for the ligand-protein complex the individual pairwise scores are calculated for all protein-ligand donor-acceptor. Individual HB interaction are then eliminated if either the donor or acceptor exceeds the maximum number of interactions allowed (e.g., a hydroxyl with one hydrogen is not allowed to make more than one donor interaction), with the lowest scoring interactions eliminated first. The final hydrogen bond score is then calculated by summing the scores of the remained individual acceptor-donor interactions.

For Chemgauss4 a lower score indicates a better result.

## **Chemical Gaussian Overlay (CGO)**

The Chemical Gaussian Overlay function (or CGO) is a hybrid scoring function that scores poses based on their similarity to a known bound ligand and the interactions both the docked and bound ligand make with the protein active site. This scoring function is not implemented by the OEScore class. This scoring function is used by the OEDock class during the exhaustive search (see *Docking Algorithm* section) when using the hybrid docking method (see *Hybrid* Method section).

CGO is primarily a ligand-based scoring functions although some information from the protein structure is used as well. The similarities computed are based on the overall shape of the molecules as well as the position of hydrogen bonding and metal chelating groups. This scoring function requires a bound ligand pose along with the structure of the target protein. Typically the ligand structure is obtained from X-ray crystallography along with the structure of the target protein, although a docked ligand could also, in principal, be used.

CGO represents molecules as a set of spherical Gaussian functions describing the shape and chemistry (acceptors, donors and chelators) of the molecule. The Gaussians representing the shape of the molecule are centered at the heavy atom positions, those for donors are centered on polar-hydrogen positions (i.e. positions where the donating hydrogen could be when it is involved in a hydrogen bond), those for acceptors are centered on lone-pair positions *(i.e.* positions where a donating hydrogen could be when a hydrogen bond is formed) and those for chelators are centered at chelating positions *(i.e.* locations where a metal could have a chelating interaction). The overlap of the Gaussians on the docked ligand to those on the bound ligand are computed for each type of Gaussian  $(e, g, \text{ shape})$ , donor, acceptor and chelator) by summing the overlap of individual pairs of Gaussian. The overlap of each individual pair is calculated by integrating the product of the two. To prevent chemistry not relevant to binding from contributing to the overall score, when calculating the chemistry overlaps *(i.e.* acceptor, donor and chelator) only groups that make the interaction with the protein are accounted for  $(e.g. a$  chelator that does not interact with a metal on the protein is ignored in the overlap calculation). The sum of all four types of overlaps is the CGO score.

For CGO a lower score indicates a better result.

## 2.3 Docking

Docking is the process of determining the structure of a ligand bound in the active site of a target protein. In the Docking Toolkit this is done with the OEDock class that takes a multiconformer representation of a ligand and returns the top scoring pose (or poses if desired) within the active site. Docking is done using an exhaustive search algorithm, followed by optimization of the best poses from the exhaustive search (see *Docking Algorithm* section).

Docking Molecules is an example program that uses the OEDock class to dock, score and annotate multiconformer molecules.

### 2.3.1 Scoring Functions and Search Resolution

The resolution of the exhaustive search and scoring functions are required inputs when constructing a OEDock object.

dockMethod is an unsigned int constant from the OEDockMethod namespace, that specifies the combination of scoring functions (or method) OEDock uses for the exhaustive search and optimization. The available scoring methods are:

| <b>Method</b>                  | <b>Exhaustive Search Scoring</b>       | <b>Optimization Scoring</b> |
|--------------------------------|----------------------------------------|-----------------------------|
| <i>OEDockMethod_Shapegauss</i> | <i>Shapegauss</i>                      | <i>Shapegauss</i>           |
| <i>OEDockMethod_PLP</i>        | <i>PLP</i>                             | <i>PLP</i>                  |
| <i>OEDockMethod_Chemgauss3</i> | <i>Chemgauss3</i>                      | <i>Chemgauss3</i>           |
| <i>OEDockMethod_Chemgauss4</i> | <i>Chemgauss3</i>                      | <i>Chemgauss4</i>           |
| <i>OEDockMethod_Chemscore</i>  | <i>Chemgauss3</i>                      | <i>Chemscore</i>            |
| <i>OEDockMethod_Hybrid1</i>    | <i>Chemical Gaussian Overlay (CGO)</i> | <i>Chemgauss3</i>           |
| <i>OEDockMethod_Hybrid</i>     | <i>Chemical Gaussian Overlay (CGO)</i> | <i>Chemgauss4</i>           |

dockResolution is an unsigned int constant from the OESearchResolution namespace, that specifies the docking resolution to use. The docking resolution is the rotational and translational stepsize used during the exhaustive search and optimization (the rotational stepsize is the furthest distance any heavy atom of the ligand will move in a single rotational step). The following resolutions are supported

| <b>Resolution</b>                  | <b>Exhaustive Translational</b> | <b>Exhaustive Rotational</b> |
|------------------------------------|---------------------------------|------------------------------|
| <i>OESearchResolution_High</i>     | 1.0                             | 1.0                          |
| <i>OESearchResolution_Standard</i> | 1.0                             | 1.5                          |
| <i>OESearchResolution_Low</i>      | 1.5                             | 2.0                          |

| Resolution                  | Optimization<br>Translational | Optimization<br>Rotational |
|-----------------------------|-------------------------------|----------------------------|
| OESearchResolution_High     | 0.5                           | 0.5                        |
| OESearchResolution_Standard | 0.5                           | 0.75                       |
| OESearchResolution_Low      | 0.75                          | 1.0                        |

All resolutions are in Angstroms.

### See also:

Section *Docking Algorithm* for more information docking algorithm.

## **Hybrid Method**

The hybrid (OEDockMethod\_Hybrid2) docking method is distinguished from other docking methods because it uses information present in the structure of a bound ligand to enhance docking performance.

The bound ligand information is used during the exhaustive search stage of the docking process (see Docking Algorithm section) by using the *Chemical Gaussian Overlay (CGO)* scoring function, which scores poses based on how well a docked pose overlays the shape of the bound ligand and mimics the same hydrogen bonding and interactions the bound ligand makes. After the exhaustive search, optimization is performed with *Chemgauss4* which is a standard structure based scoring function.

The final score a ligand receives using the hybrid docking method is based only on its interactions with the protein. Ligand information is used only to guide the selection of poses during the exhaustive search.

Note: In order to use the hybrid docking method the receptor OEDesignUnit must have a bound ligand (see HasLigand).

### 2.3.2 Initialization

An OEDock object must be initialized with a receptor object, prior to docking, scoring or annotating any molecules. This is done by passing a OEDesignUnit containing a receptor (see Receptors) to the OEDock. Initialize method.

### **2.3.3 Docking Molecules**

Once the *OEDock* object has been initialized molecules docked OEDock. are using the  $DockMultiIti Conference Molecule method.$ 

Docking requires a multiconformer representation of the molecule as input. Docking selects the top scoring docked pose from the provided ensemble of conformers. The score of the docked molecule can be obtained by calling the OEMolBase. GetEnergy method of pose.

OEDock can also return alternate as well as top scoring poses of the docked molecule.

### **2.3.4 Scoring Molecules**

The final score of a molecule (using the optimization scoring function) docked with the  $OEDock$ . DockMultiConformerMolecule method can be obtained by calling the OEMolBase. GetEnergy.

OEDock can also recalculate a score of a pose (using the optimization scoring function), and calculate the contribution for each individual component of the score as in the following example.

### 2.3.5 Docking Algorithm

*OEDock* docks multiconformer molecules using an exhaustive search that systematically searches rotations and translations of each conformer of the ligand within the active site. Following the exhaustive search the top scoring poses are optimized and assigned a final score. These two steps are described in more detail below

#### **Exhaustive Search**

1. Enumerates, to given resolution, every possible rotation and translation of each conformer of the ligand being docked within a box enclosing the active site. The resolution of the exhaustive search is determined by the overall resolution setting of OEDock (see Scoring Functions and Search Resolution section).

- 2. Discard out poses that either clash with the protein or extend to far from the binding site using the receptor's negative image outer contour (see *Negative Image* section).
- 3. If the negative image inner contour is enabled discard any poses that do not have at least one heavy atom that falls within the inner contour. (see Negative Image section).
- 4. Discard any poses that do no match any user specified constraints. (see *Constraints* section).
- 5. Score all remaining poses. The scoring function used here depends on what scoring method is being used (see Scoring Functions and Search Resolution section).
- 6. Sort poses by score and pass the top scoring poses to optimization. The number of posses passed to optimization depends on the search resolution (see OESearchResolution constant namespace).

#### Optimization

- 1. Each pose moved to 729 nearby positions, scored and the top scoring position become the new optimized pose. The positions are generated by having the initial pose take one positive and one negative step for each translational and rotational degree of freedom. The resolution of these steps is half that of the exhaustive search, and is determined by the overall resolution setting of OEDock (see Scoring Functions and Search Resolution section).
- 2. The best scoring pose of the 729 tests poses is selected as the final docked structure (and score) for the ligand.

# 2.4 ShapeFit

SHAPEFIT is a pose prediction method that is built up on the concept that similar ligands have similar binding modes in a protein active site. Given a molecule that is known to bind, and a ligand-protein complex containing a similar ligand or the binding pose of a similar ligand, *SHAPEFIT* overlays the docked ligand onto the known bound ligand. The approach used here is an extension of the molecular-shape-based ligand-alignment algorithm used in ROCS. Although both are shape-based ligand alignment, unlike ROCS, SHAPEFIT allows for for intra-molecular flexibility of the docked ligand. SHAPEFIT also guards against the docked ligand bumping into the protein, when using a ligand-protein complex as reference system.

When multiple receptors, or bound ligand references are provided, *SHAPEFIT* searches through XRC coordinates of ligands, determines the bound-liagnd best able to predict the pose of the molecule and then generates both a pose and the probability that the pose is correct.

SHAPEFIT's basic algorithm:

- 1. Given a set of potential complexes or bound-ligands, SHAPEFIT chooses the appropriate reference system based on the 2D/3D similarity to the bound ligand. The best reference, in general, has the highest 2D/3D similarity of the input molecule to the chosen bound ligand.
- 2. After the complex is chosen, a flexible fitting is performed that attempts to maximize the shape and color similarities between the input molecule and the bound ligand while at the same time minimizing the intramolecular force field on input molecule.

*SHAPEFIT* seeds the flexible fit by expanding the poses generated by the original 3D similarity as described in (1) and then applying the shape constraint of the bound ligand.

As shown in figure *SHAPEFIT Optimization*, *SHAPEFIT* works by first using the known bound ligand to position the input molecule and follows up by using the bound ligand as a shape constraint during force field optimization [Halgren-I-1996] [Halgren-II-1996] [Halgren-III-1996] [Halgren-IV-1996] [Halgren-V-1996] [Halgren-VI-1999] [Halgren-VII-1999]. While the input molecule is being forced into the shape constraint, the generated pose strain is monitored to avoid generating high strain poses.

3. The interactions between the generated poses and proteins are utilized to identify clash-free poses while simultaneously selecting the poses with the highest Pose probability.

This is a long winded way of saying that SHAPEFIT's optimization attempts to force the molecule into the known binding mode without creating undue strain on the molecule being placed into the protein.

![](_page_17_Figure_2.jpeg)

Use Shape Constraint to Optimize Overlay

Fig. 1: **SHAPEFIT Optimization:** Starting from an initial alignment, use the shape constraint of the bound-ligand to drive a flexible fit while simultaneously minimizing intra-molecular force field of the fit molecule

As shown in figure SHAPEFIT Cross Docking Results, analyzing the Kinase data set used in [Tuccinardi-2010] poseprediction using SHAPEFIT is seen to perform remarkably better for similar ligands than standard docking techniques at higher TanimotoCombo values:

While SHAPEFIT is not a good technique for determining the pose between known bound-ligands and fit ligands with low similarity, as the similarity increases, the probability of determining the correct pose increases rapidly. This is most likely because as the similarity increases, the active site similarity also increases.

![](_page_18_Figure_1.jpeg)

# Percent Predictions < 2.0 Angstrom to XRay

Fig. 2: SHAPEFIT Cross Docking Results: Probability of finding a good pose based on bound-ligand fit-ligand TanimotoCombo similarity. Standard docking results are essentially the same and follow the same trajectories flattening out as they hit their limit of accuracy. While SHAPEFIT performs worse at low similarities it continually increases as similarity increases.

### 2.4.1 On Clashes

Unlike the FRED and HYBRID methods, SHAPEFIT is heavily biased towards the known bound ligand. In some cases this causes the pose to clash with the protein. This is especially true if the *original bound ligand* already clashes with the protein.

## 2.5 POSIT Theory

**POSIT** is a pose-prediction tool primarily based on the assumption that similar ligands bind similarly. Pose prediction is the process of determining the structure of a ligand bound in the active site of a target protein. Pose prediction with *POSIT* assumes that the incoming ligand binds to the given protein and makes the best effort in correctly placing it in the active site. In conjunction to the predicted pose, **POSIT** also provides an estimate of confidence, in terms of an estimated probability, that the docked pose is within 2.0 Angströms of the actual binding pose.

**Note:** Note that this probability is not the probability of binding, rather, the probability that the pose is correct given the ligand actually binds to the receptor.

POSIT consists of multiple Docking or Pose Prediction methods intentionally and automatically chooses the best method to use for any particular ligand based on the 2D (graph) and 3D (structure) similarity of the docked ligand to the bound ligand. The methods *POSIT* uses to dock are:

- 1. ShapeFit Shape-guided ligand minimization into the receptor site
- 2. Hybrid hybrid method that uses ligand and protein information
- 3. Fred Standard docking method that uses no ligand information

If there is no bound ligand in the receptor, the *Fred* method is used by default since it does not rely upon the pressence of the bound ligand.

### 2.5.1 Handling of isomerisms and chirality

Stereo, and notably nitrogen aniline stereo centers, are currently somewhat problematic for POSIT. Many crystal structures have flat geometries for some stereo centers due to time-averaging during data collection. This makes stereo centers appear to have flat geometries in the 3D coordinates.

Because the POSIT algorithm internally expands conformations during the flexible fitting procedure, the full molecule must be labeled with stereo - either in the 3D coordinate sense or the 2D coordinate sense. This means that some pdb ligand structures will unfortunately be failed by the POSIT algorithm.

To get around this, posit can be told to ignore nitrogen stereo during the conformer generation phase.

**Note:** Output structures of *Posit* are not guaranteed to have the same conformations of the input molecule. This is due to the fact that force-field minimization is occasionally performed during pose prediction.

### 2.5.2 Estimated Pose Probability

During a drug discovery campaign, thousands of small molecule inhibitors are made in the course of optimizing molecular properties. For projects that have X-Ray crystallographic (XRC) coordinates, structure-based designs help guide the medicinal chemistry efforts. In many cases XRC provides a detailed picture of the binding of a smallmolecule inhibitor into the binding site.

Many techniques exist for pose-prediction and are well documented [Erickson-2004]. However, very few provide a probability that the generated pose is correct where correct is typically considered to be less than 2.0 Ångströms RMSD (root mean square distance) from experimental crystal structure. In fact, many docking scores such as Chemscore, Chemgauss3, PLP [Tuccinardi-2010] are not very correlated with correct ligand pose, and worse are not transferable between systems. The best docking score in one system may not even be close to the best docking score in another.

*POSIT* overcomes these issues by comparing predicted poses to observed bound ligands in related co-crystals. As the observed ligand becomes more similar to the the predicted pose, both the binding mode and the shape of the receptor pocket itself tends to become more similar.

The similarity measures being used are 2D path-based fingerprints and the 3D TanimotoCombo [Hawkins-2010] that compares shape and the Mills-Dean approximation of electrostatics [Mills-Dean-1996]. These similarity measures choose the most appropriate system to dock against (when multiple receptors are available) and provide a prediction of the quality of the result. The *TanimotoCombo* measure is agnostic of how the poses in question are generated; it can be used to validate and provide a pose prediction probability regardless of how the pose was generated.

POSIT probabilities were generated using a large test set containing many pose predictions and verified against an independent set of predictions that were then validated with X-Ray crystallography. It is important to note that POSIT does not give a probability of binding. Rather it gives a probability that **if the ligand does actually bind**, what is the likelihood of the *POSIT* pose being the actual pose.

Figure POSIT Probability MAP shows how the beliefs given by the 2D and 3D measures are combined into a probability of having a good pose. Remember that this probability has been generated from ligands that actually bind, hence, it is not a probability of binding.

![](_page_20_Figure_5.jpeg)

Fig. 3: **POSIT Probability Map:** Given a 2D similarity (in this case the MACCS 166 descriptor set [Durant-2002]) and a 3D similarity (TanimotoCombo) posit computes a probability of finding the correct pose based on an analysis of historical and experimental data.

This result is different from the result shown in [Tuccinardi-2010], where they reported that having a high Tanimoto-Combo to the known bound ligand did not dramatically increase the quality of the resulting pose (even for FRED). The reason is subtle: Tuccinardi et al were computing the highest TanimotoCombo that the two molecules could obtain, while Posit computes the actual, docked, in-place TanimotoCombo of the fitted pose. That is, if the docking algorithm produces an alignment of fit molecule to known bound ligand that overlaps with a given *TanimotoCombo*, one can look up the probability the docking was successful. In point of fact, *Posit* is specifically designed so that the docked pose obtains the highest *TanimotoCombo* score possible while simultaneously minimizing induced strain and maintaining interactions with the protein.

Categorically the data shown in *POSIT Probability MAP*, for each pose can be binned into the following results:

| Result          | Meaning                                                                                           |
|-----------------|---------------------------------------------------------------------------------------------------|
| <b>GREAT</b>    | Computed pose is likely (75%-100% probability) to be within 2.0 Å of experimentally-derived pose. |
| <b>GOOD</b>     | Computed pose may be (50%-75% probability) to be within 2.0 Å of experimentally-derived pose.     |
| <b>MEDIOCRE</b> | Take with a grain of salt (33%-50% probability)                                                   |
| <b>POOR</b>     | Take with a huge grain of salt (<33% probability)                                                 |

### 2.5.3 Additional MCS Constraints

Walter's et al noted that a large portion of ligands bound to the same protein kinase share a large maximum common substructure (MCS). This was the basis for their CORES algorithm [Hare-2004]. Posit can optionally identify matching regions and use them as additional constraints during conformer generation. Posit performs the MCS match to the bound ligand by default.

### 2.5.4 On Clashes

The definition of *clashes* is somewhat problematic for purposes of pose prediction. In general, serious clashes where interpenetration with the protein should be avoided at all costs. However, when docking into a rigid protein that does not have the appropriate conformation, rigid docking ignores that fact that the active site may adopt a conformation suitable to the posed ligand.

*Posit* uses the definitions from OEClashInteractionHint to identify clashes. *Posit* allows the users to specify three allowable clash levels.

| <b>Allowed Clash</b>    | Description                        |
|-------------------------|------------------------------------|
| noclashes (none)        | No clashes are allowed.            |
| hydrogen (mild clashes) | Only hydrogen clashes are allowed. |
| allclashes              | All clashes are allowed.           |

### **2.5.5 Using Multiple Receptors**

Using multiple receptors to dock or pose molecules has been shown to greatly increase the reliability of docking.

When multiple receptors are provided *Posit* chooses the appropriate reference system based on the 2D/3D similarity to the bound ligand. The best reference, in general, has the highest 2D/3D similarity of the input molecule to the chosen bound ligand. The similarity measure used here are similar to those used in determining the best docking method in Posit.

### 2.5.6 Receptor Flexibility

Incorporating multiple receptors is the simplest way to account for receptor flexibility during pose prediction. With multiple receptors, *Posit* would pick the best suitable conformer of the receptor for a particular docked ligand.

Pose generated from *Posit* with provided receptor conformers can still sometimes contain clashes. Option is available to trigger post pose prediction relaxation, that relaxes both the posed ligand and protein residues around it.

Note that optimization of a protein-ligand complex can sometimes be time consuming, especially if the target protein and associated components are large.

### 2.5.7 TanimotoCombo

Posit uses the TanimotoCombo measure to compare (and optimize) predicted and bound ligands. The TanimotoCombo measure is simply two separate Tanimoto measures added together. While most uses of Tanimoto have been to compare fingerprints together, there is a direct relation between the 1D fingerprint bit vector and 3D space:

The basic equation for a field Tanimoto between two fields A and B is:

$$
Tanimoto_{A,B} = \frac{\int A(\vec{r}) * B(\vec{r})}{\int A(\vec{r}) * A(\vec{r}) + \int B(\vec{r}) * B(\vec{r}) - \int A(\vec{r}) * B(\vec{r})}
$$

In the case of *Posit*, the field in question can be thought of as field of voxel space. For  $Tanimoto_{shape}$ , where A and B are now molecules: if two objects fill the same voxels, then the Tanimoto value is 1.0. If two objects overlap by half, the Tanimoto value is 0.5 and so on. (The term voxel is used for purposes edification, in actuality the volumes estimated using a fast approximate method)

# Overlap $(q,t)$ = Intersection of Volumes q and t

![](_page_22_Figure_7.jpeg)

Fig. 4: Voxel Representation of Shape: Similar to fingerprint bits in 1D, voxels can be used to represent 3D space and compared with the Tanimoto measure. The numerator  $\text{Overall}(q,t)$  is essentially the volume of the **intersection** of q and t and the denominator Overlap(q,q) + Overlap(t,t) - Overlap(q,t) is essentially the volume of the **union** of q and t.

The field can also contain colored representations of chemistry. For example, if two voxels are colored as hydrogen bond donors and overlap, the  $Tanimoto_{color}$  increases.

Hence, TanimotoCombo is:

 $TanimotoCombo = Tanimoto_{shape} + Tanimoto_{color}$ 

TanimotoCombo values range from 0 (no overlap) to 2.0 (full shape overlap and full color or chemistry overlap).

# 2.6 Posit How to

## 2.6.1 Ignore Nitrogen stereo

Nitrogen stereo can be ignored in *Posit* by constructing *OEPosit* with an *OEPositOptions* object that has the OEPositOptions. SetIqnoreNitrogenStereo method set to True.

## 2.6.2 Prepare molecules for Posit

With default settings, *Posit* internally generates the required input conformers and *Posit* can be used with 2D input molecules. However, if it is desired to pass a pre-generated set of conformers to *Posit*, following are the recommended ways to supply or prepare molecules for **POSIT**.

- 1. Use OMEGA or the OMEGA toolkit to prepare molecules or expand the stereo chemistry using OEFlipper. POSIT is guaranteed to work correctly if the input molecules have been generated by OMEGA.
- 2. Set the OEPositOptions fullConformationalSearch option to be false. See the section OEPositOptions for more details. This method of running POSIT is not recommended as a large portion of the flexible methodology will be deactivated.

## 2.6.3 Use multiple receptors

Multiple receptors can be passed to *Posit* by calling the  $AddReceptor$  with each of the receptors as shown in the example, Listing 5. The OEPosit will automatically detect the best receptor for the ligand in action and dock to it.

One of the difficulties of docking to multiple receptors, is that they can consume quite a large amount of memory so holding multiple docking objects at the same time can be problematic. This can be controlled with the Set PoserCacheCount method, based on the available hardware capacity and the size of the receptors in use.

## 2.6.4 Obtain clash-free pose

Pose generated from **Posit** with the default options can sometimes contain clashes. Users have the option to perform pose relaxation, either on the clashed poses or on all generated poses, with the appropriate option using the SetPoseRelaxMode method.

**THREE** 

# **OEDOCKING EXAMPLES**

The following table lists the currently available OEDocking TK examples:

| Program        | Description                      |
|----------------|----------------------------------|
| docking        | docking molecules                |
| rescoring      | rescore docked molecules         |
| shapefit       | flexible fitting with OEShapeFit |
| posing         | generating poses                 |
| posing_multi   | posing with multiple receptors   |
| make_receptor  | making a receptor                |
| contour_volume | receptor contour volume          |
| inner_contour  | toggle inner contour             |
| outer_contour  | set outer contour                |

# **3.1 Docking and Scoring Examples**

### **3.1.1 Docking Molecules**

The following code example shows how to perform docking using the  $OEDock$  object.

## See also:

- OEDockOptions class
- OEDock class
- OEHybrid class

## **Listing 1: Docking Molecules**

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
```

```
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oedocking
def main(argy=[ name ]):
   dockOpts = oedocking.OEDockOptions()
    opts = oechem. OERefInputAppOptions(dockOpts, "DockMolecules", oechem.
\rightarrowOEFileStringType_Mol3D,
                                        oechem.OEFileStringType_Mol3D, oechem.
\rightarrowOEFileStringType_DU, "-receptor")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   dockOpts. UpdateValues (opts)
    if s = oechem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   rfs = oechem.oeifstream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   du = occhem.OEDesignUnit()if not oechem. OEReadDesignUnit (rfs, du) :
        oechem. OEThrow. Fatal ("Failed to read design unit")
    if not du.HasReceptor():
        oechem. OEThrow. Fatal ("Design unit %s does not contain a receptor" % du.
\rightarrow GetTitle())
   dock = oedocking. OEDock (dockOpts)
   dock.Initialize(du)
    for mcmol in ifs. GetOEMols():
        print ("docking", mcmol.GetTitle())
        dockedMol = occhem. OEGraphMol()retCode = dock.DockMultiConformerMolecule(dockedMol, mcmol)
        if (retCode != oedocking.OEDockingReturnCode_Success):
            oechem. OEThrow. Fatal ("Docking Failed with error code " + oedocking.
→OEDockingReturnCodeGetName(retCode))
        sdtag = oedocking.OEDockMethodGetName(dockOpts.GetScoreMethod())
        oedocking. OESetSDScore(dockedMol, dock, sdtag)
        dock.AnnotatePose(dockedMol)
```

```
oechem.OEWriteMolecule(ofs, dockedMol)
   return 0
if name == " main ":
   sys.exit(main(sys.argv))
```

### **3.1.2 Rescoring Docked Molecules**

The following code example shows how to rescore previously docked molecules, using the OEScore object.

#### See also:

• OEScore class

#### **Listing 2: Rescoring Docked Molecules**

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
from openeye import oedocking
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    oedocking.OEScoreTypeConfigure(itf, "-score")
    if not oechem. OEParseCommandLine(itf, argv):
        return 1
   receptor = occhem.OEDesignUnit()if not oechem. OEReadDesignUnit(itf.GetString("-receptor"), receptor):
        oechem. OEThrow. Fatal ("Unable to read receptor")
   imstr = occhem.oemolistream()if not imstr. open (itf. GetString ("-in")):
        oechem. OEThrow. Fatal ("Unable to open input file of ligands")
```

```
omstr = occhem.oemolostream()if not omstr.open(itf.GetString("-out")):
        oechem. OEThrow. Fatal ("Unable to open out file for rescored ligands")
    scoreType = oedocking.OEScoreTypeGetValue(itf, "-score")
    score = oedocking.OEScore(scoreType)
    score. Initialize (receptor)
    for ligand in imstr. GetOEMols():
        if itf.GetBool("-optimize"):
            score.SystematicSolidBodyOptimize(ligand)
        score.AnnotatePose(ligand)
        sdtag = score. GetName()
        oedocking. OESetSDScore(ligand, score, sdtag)
        oechem.OESortConfsBySDTag(ligand, sdtag, score.GetHighScoresAreBetter())
        oechem.OEWriteMolecule(omstr, ligand)
    return <sub>0</sub>InterfaceData = """!PARAMETER -receptor
  !ALIAS -rec
 !TYPE string
 !REQUIRED true
 !LEGAL_VALUE *.oedu
 !BRIEF A receptor file the poses pass to the -in flag will be scored against
!END
!PARAMETER -in
 !TYPE string
  !REQUIRED true
  !BRIEF Input molecule file with poses to rescore
!END
!PARAMETER -out
 !TYPE string
 !REQUIRED true
 !BRIEF Rescored molecules will be written to this file
! END \,!PARAMETER -optimize
 !ALIAS -opt
 !TYPE bool
  !DEFAULT false
 !BRIEF Optimize molecules before rescoring
!END
\mathbf{H}^{\dagger} \mathbf{H}^{\dagger} \mathbf{H}if name == "_main_":
    sys.exit(main(sys.argv))
```

# **3.2 OEShapeFit Examples**

## 3.2.1 Flexible Overlay Optimization with OEShapeFit API

The following code example shows how to flexibly fit input multi conformer molecules in the design unit that contains bound ligand and get the score using the OEShapeFit and OEShapeFitResults objects.

### See also:

- · OEFlexiOverlapFunc class
- · OEFlexiOverlayOptions class

## **Listing 3: Flexible fitting with OEShapeFit**

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
# This example reads in a reference molecule and a few fit
# molecules, performs overlay optimization, sorts the results
# in Tanimoto order, and shows the single best result.
# With the default options, OEOverlay optimizes both shape and color.
import sys
from openeye import oechem
from openeye import oeshape
from openeye import oedocking
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    overlayOpts = oedocking.OEShapeFitOptions()
    opts = oechem. OERefInputAppOptions (overlayOpts, "ShapeFit", oechem.
\rightarrowOEFileStringType_Mol3D,
                                        oechem.OEFileStringType_Mol3D, oechem.
\rightarrowOEFileStringType DU, "-receptor")
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
       return 0
   overlayOpts. UpdateValues (opts)
```

```
if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    rfs = oechem.oeifstream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   receptor = occhem.OEDesignUnit()oechem.OEReadDesignUnit(rfs, receptor)
   print ("Ref. Title:", receptor. GetTitle())
    shapefit = oedocking.OEShapeFit(overlayOpts)
    shapefit.SetupRef(receptor)
    for fitmol in ifs. GetOEMols():
        results = shapefit.Fit(fitmol)for res, conf in zip(results, fitmol. GetConfs()):
            print ("Fit Title: 6-4s Score: 6.2f"
                  % (fitmol.GetTitle(), res.GetScore()))
            oechem. OESetSDData(conf, "Score", "%. 2f" % res. GetScore())
        oechem.OEWriteMolecule(ofs, fitmol)
if name == " main ":
    sys.exit(main(sys.argv))
```

# **3.3 POSIT Examples**

## 3.3.1 Generating Poses with POSIT

The following code example shows how to generate a single pose for each input ligand using the OEPosit object.

See also:

- OEPositOptions class
- OEPosit class

### **Listing 4: Generating Poses with POSIT**

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
from openeye import oedocking
def main(argv=[__name__]):
    positOpts = oedocking.OEPositOptions()
    opts = oechem.OERefInputAppOptions(positOpts, "PoseMolecules", oechem.
\rightarrowOEFileStringType_Mol3D,
                                        oechem.OEFileStringType_DU, oechem.
\rightarrowOEFileStringType_DU, "-receptor")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return <sub>0</sub>positOpts. UpdateValues (opts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open % for reading" % opts. GetInFile())
   rfs = oechem.oeifstream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
   ofs = occhem.oeofstream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open % for writing" % opts. GetOutFile())
   poser = oedocking. OEPosit (positOpts)
   du = occhem.OEDesignUnit()\text{count} = 0while oechem. OEReadDesignUnit (rfs, du) :
        if not du.HasReceptor():
            oechem. OEThrow. Fatal ("Design unit %s does not contain a receptor" % du.
\rightarrowGetTitle())
        poser.AddReceptor(du)
        count += 1if count == 0:
        oechem. OEThrow. Fatal ("Receptor input does not contain any design unit")
    for mcmol in ifs. GetOEMols():
        oechem.OEThrow.Info("posing %s" % mcmol.GetTitle())
        result = oedocking. OESinglePoseResult()
        ret\_code = poser.Dock(result, memol)if ret_code == oedocking.OEDockingReturnCode_Success:
            posedDU = result.GetDesignUnit()
            posedDU.SetDoubleData(poser.GetName(), result.GetProbability())
```

```
oechem. OEThrow. Info ("Receptor used: %s pose probability: %f" % (posedDU.
\qquad \qquad \qquad \left. \qquad \qquad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \quad \oechem.OEWriteDesignUnit(ofs, posedDU)
          else:
               errMsg = oedocking.OEDockingReturnCodeGetName(ret_code)
               oechem.OEThrow.Warning("%s: %s" % (mcmol.GetTitle(), errMsg))
     return 0
if _name
             = "_main_":
     sys.exit(main(sys.argv))
```

## 3.3.2 Generating Multiple Poses with POSIT

The following code example shows how to generate multiple poses for each input ligand, using the OEPosit object.

#### See also:

- OEPositOptions class
- OEPosit class

### Listing 5: Posit for Generating Multiple Poses for each Ligand

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
from openeye import oedocking
class MyOptions (oedocking. OEPositOptions) :
   def __init__(self):oedocking.OEPositOptions.__init__(self)
        param1 = oechem.OEUIntParameter("-numPoses", 1)
        param1.AddLegalRange("1", "20")
        param1.SetBrief("Number of poses to generate")
        self._param1 = self.AddParameter(param1)
```

```
(continued from previous page)
```

```
def GetNumPoses(self):
        if self._param1.GetHasValue():
            return int (self._param1.GetStringValue())
        return int (self. _param1.GetStringDefault())
def main(argv=[_name_]):
   positOpts = MyOptions()opts = oechem.OERefInputAppOptions(positOpts, "PoseMolecules", oechem.
\rightarrowOEFileStringType_Mol3D,
                                        oechem.OEFileStringType_DU, oechem.
\rightarrowOEFileStringType_DU, "-receptor")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return <sub>0</sub>positOpts. UpdateValues (opts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   rfs = oechem, oeifstream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
   ofs = occhem.oeofstream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   poser = oedocking.OEPosit(positOpts)
   du = oechem.OEDesignUnit()
    count = 0while oechem. OEReadDesignUnit (rfs, du) :
        if not du.HasReceptor():
            oechem. OEThrow. Fatal ("Design unit %s does not contain a receptor" % du.
\rightarrowGetTitle())
        poser.AddReceptor(du)
        count += 1if count == 0:
        oechem. OEThrow. Fatal ("Receptor input does not contain any design unit")
   oechem.OEThrow.Info("Number of conformers: %d" % positOpts.GetNumPoses())
    oechem. OEThrow. Info ("Best Receptor pose flag: %s" % positOpts.
→GetBestReceptorPoseOnly())
    for mcmol in ifs. GetOEMols () :
        oechem.OEThrow.Info("posing %s" % mcmol.GetTitle())
        results = oedocking.OEPositResults()ret_code = poser.Dock(results, mcmol, positOpts.GetNumPoses())
        if ret_code == oedocking.OEDockingReturnCode_Success:
            for result in results. GetSinglePoseResults():
                posedDU = result.GetDesignUnit()
                posedDU.SetDoubleData(poser.GetName(), result.GetProbability())
                oechem. OEThrow. Info ("Receptor used: %s pose probability: %f" %.
\rightarrow(posedDU.GetTitle(), result.GetProbability()))
                oechem.OEWriteDesignUnit(ofs, posedDU)
```

(continues on next page)

pass

```
Also:errMsg = oedocking.OEDockingReturnCodeGetName(ret_code)
             oechem.OEThrow.Warning("%s: %s" % (mcmol.GetTitle(), errMsg))
    return <sub>0</sub>if _name_
           = "__main__\mathbf{u}_1sys.exit(main(sys.argv))
```

## **3.4 Receptor Examples**

## 3.4.1 Making a Receptor

The following code example shows how to make a receptor.

#### See also:

- OEMakeReceptorOptions class
- · OEMakeReceptor method

#### **Listing 6: Making a Receptor**

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
from openeye import oedocking
def main(arqv=[ name ]):
   recOpts = oedocking.OEMakeReceptorOptions()
   opts = oechem.OESimpleAppOptions(recOpts, "MakeReceptor", oechem.OEFileStringType_
→DU, oechem.OEFileStringType_DU)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
                                                                         (continues on next page)
```

```
return 0
    recOpts. UpdateValues (opts)
    ifs = oechem.oeifstream()
    if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oeofstream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    du = occhem.OEDesignUnit()while oechem. OEReadDesignUnit(ifs, du):
        if oedocking. OEMakeReceptor (du, recOpts):
            oechem.OEWriteDesignUnit(ofs, du)
        else:oechem. OEThrow. Warning ("%s: %s" % (du. GetTitle(), "Failed to make receptor
\leftrightarrow<sup>"</sup>))
    return 0
if _name_ == "_main_":
    sys.exit(main(sys.argv))
```

## 3.4.2 Receptor Contour Volume

The following code example shows how to estimate a receptor outer contour volume.

#### See also:

- OEReceptor class
- OEDesignUnit class

#### **Listing 7: Receptor Contour Volume**

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

import sys

(continued from previous page)

```
from openeye import oechem
def main(argv=[__name__]):
    if len(sys.argv) != 2:
        oechem.OEThrow.Usage("ReceptorOuterContourVolume.py <receptor>")
    du = occhem. OEDesignUnit ()
   if not oechem. OEReadDesignUnit (argv[1], du) :
        oechem. OEThrow. Fatal ("Unable to open receptor design unit file")
    if not du.HasReceptor():
        oechem. OEThrow. Fatal ("Design unit %s does not have a receptor" % du.
\rightarrowGetTitle())
    receptor = du.GetReceptor()negativeImagePotential = receptor.GetNegativeImageGrid()
   outerContourLevel = receptor.GetOuterContourLevel()
   outerCount = 0for i in range (negativeImagePotential.GetSize()):
        if negativeImagePotential[i] >= outerContourLevel:
            outerCount += 1
   count ToVolume = pow(negativeImagePotential.GetSpacing(), 3)print (outerCount * countToVolume, " cubic angstroms")
if name == " main ":
    sys.exit(main(sys.argv))
```

## 3.4.3 Toggle Receptor Inner Contour

The following code example shows how to toggle receptor contour volume.

See also:

- - OEReceptor class
- OEDesignUnit class

## **Listing 8: Toggle Receptor Inner Contour**

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
def main(argv=[__name__]):
    if len(argv) != 2:
        oechem. OEThrow. Usage ("ToggleInterContour.py <receptor>")
   du = occhem.OEDesignUnit()if not oechem. OEReadDesignUnit (argv[1], du):
        oechem. OEThrow. Fatal ("Cannot read receptor du file")
    if not du. HasReceptor():
        oechem. OEThrow. Fatal ("Design unit %s does not have a receptor" % du.
\rightarrowGetTitle())
   receptor = du.GetReceptor()innerContourLevel = receptor.GetInnerContourLevel()
   receptor.SetInnerContourLevel(-innerContourLevel)
    if innerContourLevel > 0.0:
        oechem. OEThrow. Info ("Toggling inner contour off")
    else:
        oechem.OEThrow.Info("Toggling inner contour on")
    if not oechem. OEWriteDesignUnit (argv[1], du) :
        oechem. OEThrow. Fatal ("Unable to write receptor")
if name == " main ":
    sys.exit(main(sys.argv))
```

## 3.4.4 Set Receptor Contour Volume

The following code example shows how to change the receptor outer contour volume.

See also:

- $\bullet$  OEReceptor class
- OEDesignUnit class

#### **Listing 9: Set Receptor Contour Volume**

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
def main(argv=[_name_]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("SetOuterContourVolume.py <receptor> <volume>")
    du = occhem. OEDesignUnit()
   if not oechem. OEReadDesignUnit (argv[1], du) :
        oechem. OEThrow. Fatal ("Unable to open receptor design unit file")
    if not du. HasReceptor():
        oechem. OEThrow. Fatal ("Design unit %s does not have a receptor" % du.
\rightarrowGetTitle())
    outerContourVolume = float (argv[2])
    receptor = du.GetReceptor()negativeImagePotential = receptor.GetNegativeImageGrid()
    gridElement = []for i in range (negativeImagePotential.GetSize()):
        gridElement.append(negativeImagePotential[i])
    gridElement.sort()
    gridElement.reverse()
   countToVolume = pow(negativeImagePotential, GetSpacing(), 3)ilevel = int (outerContourVolume / countToVolume) + 0.5)outerContourLevel = gridElement [-1]
    if ilevel < len(gridElement):
        outerContourLevel = gridElement[ilevel]
    receptor.SetOuterContourLevel(outerContourLevel)
```

```
if not oechem. OEWriteDesignUnit (argv[1], du) :
        oechem. OEThrow. Fatal ("Unable to write updated receptor")
if __name__ == "__main__":sys.exit(main(sys.argv))
```

# **OEMODELS EXAMPLES**

The following table lists the currently available **OEModels** examples:

| Program        | Description               |
|----------------|---------------------------|
| <i>docking</i> | Building ROCS Query Model |

# **4.1 Building ROCS Query Model**

The following code example shows how to create a ROCS query model from a set of known ligands in their binding modes. The input ligands should be prepared by aligning the protein crystal structures.

#### See also:

• OEROCSQueryModelBuilder class

## **Listing 1: Building ROCS Query Model**

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
from openeye import oeshape
from openeye import oedocking
```

```
def main(argv=[_name_]):
   buildOpts = oedocking.OEROCSQueryModelOptions()
   opts = oechem. OESimpleAppOptions(buildOpts, "ROCSQueryModel", oechem.
→OEFileStringType_DU, "sq")
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   buildOpts. UpdateValues (opts)
   ifs = oechem.oeifstream()
   if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oeofstream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   builder = oedocking.OEROCSQueryModelBuilder(buildOpts)
   builder.SetLigands(ifs);
    for query in builder. Build():
        oeshape.OEWriteShapeQuery(ofs, query)
    return 0
if _name == " main":
    sys.exit(main(sys.argv))
```

# **FIVE**

**API** 

## 5.1 OEDocking API

## 5.1.1 OEDocking Classes

## **OEDockOptions**

class OEDockOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for docking with OEDock.

#### The OEDockOptions class defines the following public methods:

- GetResolution and SetResolution
- · GetScoreMethod and SetScoreMethod

#### **Constructor**

```
OEDockOptions();
OEDockOptions (const OEDockOptions &)
```

Default and copy constructors.

### operator=

OEDockOptions & operator= (const OEDockOptions &)

### **GetResolution**

unsigned GetResolution() const

See SetResolution method.

## **GetScoreMethod**

unsigned GetScoreMethod() const

See SetScoreMethod method.

## **SetResolution**

bool SetResolution (const unsigned)

Sets the search resolution for docking. Allowed resolutions are defined in the OESearchResolution namespace. Default is OESearchResolution\_Standard.

## **SetScoreMethod**

bool SetScoreMethod (const unsigned)

Sets the scoring method for docking. Allowed methods are defined in the OEDockMethod namespace. Default is OEDockMethod\_Chemgauss4.

#### **OEDock**

class OEDock

OEDock is used to dock and score multiconformer molecules in an active site.

Use the following procedure to dock and score molecules with this class.

- 1. Initialize the active site by passing a design unit containing a receptor (see chapter\_receptor chapter) to the OEDock. Initialize method.
- 2. Dock molecules using the OEDock. DockMultiConformerMolecule method.
- 3. Score docked molecules with any of the following methods
  - · OEDock. ScoreLigand
  - · OEDock. ScoreAtom
  - · OEDock. ScoreLigandComponent
  - · OEDock. ScoreAtomComponent
  - · OEDock. AnnotatePose

#### **Constructor**

```
OEDock()
OEDock (const OEDockOptions&)
OEDock (const OEDock&)
```

Default and copy constructors.

#### **Islnitialized**

```
bool IsInitialized() const
```

Returns true if this object has been successfully initialized and is ready to dock molecules.

#### **Initialize**

```
bool Initialize (const OEBio:: OEDesignUnit&)
bool Initialize (const OEChem:: OEMolBase&)
```

Sets up this object to dock molecules into a receptor. This function returns true if initialization was successful. This object does not depend upon receptor once this call is completed *(i.e.* receptor can be destroyed after calling this method). The first overload expects a design unit that contains a receptor. The second overload works on a variation of molecule that contains receptor data.

Note: This method can take several minutes to complete with larger active sites.

### **DockMultiConformerMolecule**

Both overloads of this method dock *inputMol* into the receptor passed to the OEDock. Initialize method.

The return value of this method describes the result of the docking, with a value from the OEDockingReturnCode namespace. A result of OEDockingReturnCode\_Success indicates docking was successful.

```
unsigned int DockMultiConformerMolecule (OEChem:: OEMolBase& dockedMol,
                                         const OEChem:: OEMCMolBase& inputMol)
```

This overload of OEDock. DockMultiConformerMolecule returns the top scoring pose.

dockedMol Top scoring docked pose of inputMol.

*inputMol* A multiconformer representation of a molecule to dock.

The score of the docked pose can be obtained by calling the Get Energy method of *docked Mol*.

```
unsigned int DockMultiConformerMolecule (OEChem:: OEMCMolBase& dockedMol,
                                         const OEChem:: OEMCMolBase& inputMol,
                                         unsigned int numPoses = 1)
```

This overload of OEDock. DockMultiConformerMolecule can return alternate docked poses, in addition to the top scoring pose.

dockedMol Docked poses of inputMol. Poses are stored as conformers of the OEMCMolBase and are sorted by score.

*inputMol* A multiconformer representation of a molecule to dock.

numPoses Maximum number of top scoring docked poses to return in *dockedMol*. Typically this will be the number of poses returned, however, in highly restricted sites fewer than *numPoses* may be returned. The value of *numPoses* must be greater than zero.

The score of the docked poses can be obtained by calling the GetEnergy method on the conformers of *dockedMol*.

#### **GetHighScoresAreBetter**

bool GetHighScoresAreBetter() const

Returns true if higher scores indicate a better result.

Returns false if lower scores indicate a better result.

#### **GetName**

std::string GetName() const ;

Returns the name of the scoring function docked poses are scored with.

#### **GetComponentNames**

OESystem:: OEIterBase<const std:: string>\* GetComponentNames() const

#### **ScoreLigand**

float ScoreLigand (const OEChem:: OEMolBase& pose)

Rescores a pose within the active site.

*pose* Structure of a pose within the active site

If an error occurs this function will return FLT\_MAX if OEDock. GetHighScoresAreBetter returns false or -FLT MAX otherwise.

#### **ScoreAtom**

```
float ScoreAtom (const OEChem:: OEAtomBase& atom,
                const OEChem:: OEMolBase& pose)
```

Returns the score of an atom of a given pose within the active site.

atom Atom of pose to score.

*pose* Structure of a pose within the active site

If an error occurs this function will return FLT\_MAX if OEDock. GetHighScoresAreBetter returns false or -FLT\_MAX otherwise.

## **ScoreLigandComponent**

```
float ScoreLigandComponent (const OEChem:: OEMolBase& pose,
                            std::string compName)
```

Returns the given components contribution to the total score.

*pose* Structure of a pose within the active site

compName Name of the score component to report. Name must be one returned by  $OEDOCK$ . GetComponentNames.

If an error occurs this function will return FLT\_MAX if OEDock. GetHighScoresAreBetter returns false or -FLT MAX otherwise.

#### **ScoreAtomComponent**

```
float ScoreAtomComponent (const OEChem:: OEAtomBase& atom,
                          const OEChem:: OEMolBase& pose,
                          std::string compName)
```

Returns the given components contribution to the score of a given atom score.

atom Atom of pose to score.

*pose* Structure of a pose within the active site

compName Name of the score component to report. Name must be one returned by  $OEDOCK$ . GetComponentNames.

If an error occurs this function will return FLT MAX if OEDock. GetHighScoresAreBetter returns false or -FLT MAX otherwise.

#### **AnnotatePose**

Adds VIDA scoring annotation to the *pose* or *poses* passed.

The annotated poses must be written out in either *oeb* or *oeb.gz* format and are only viewable in **VIDA**.

**bool** AnnotatePose (OEChem:: OEMolBase& pose)

This overload of OEDock. AnnotatePose annotates a single pose.

*pose* Structure of a pose within the active site

bool AnnotatePose (OEChem:: OEMCMolBase& poses)

This overload of OEDock. AnnotatePose annotates all poses of a given ligand.

*poses* An OEMCMolBase the conformers of which are poses within the active site.

## **CacheScoringSetup**

This function caches the current scoring setup of the OEDock object onto a receptor object. When another OEDock object is initialized with this receptor the it will read in the cached score data rather than recalculating it from scratch, thus improving the startup time of the OEDock object.

```
bool CacheScoringSetup(OEBio:: OEDesignUnit& receptor, bool clearOldData = true)
bool CacheScoringSetup(OEChem:: OEMolBase& receptor, bool clearOldData = true)
```

- **receptor** A receptor object. This must be the same receptor object the OEDock object was initialized with or an exact copy.
- clearOldData Flag to clear cached data from a prior call to CacheScoringSetup with this receptor. The cached data can be quite sizable (hundreds of megabytes), so leaving this flag at the default value of true is recommended.

Note: The cached score data on a receptor will be saved when the receptor is written to a file.

## **OEHybrid**

class OEHybrid : public OEDock

OEHybrid is used to dock and score multiconformer molecules in an active site using the Hybrid Method.

#### The following methods are publicly inherited from OEDock:

- · IsInitialized
- · Initialize
- · DockMultiConformerMolecule
- · GetHighScoresAreBetter
- GetName
- · GetComponentNames
- · ScoreLigand
- ScoreAtom
- · ScoreLigandComponent
- · ScoreAtomComponent
- · AnnotatePose
- · CacheScoringSetup

## **Constructor**

```
OEHybrid()
OEHybrid (const OEHybrid&)
```

Default and copy constructors.

## **OEMakeReceptorOptions**

class OEMakeReceptorOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for *OEMakeReceptor*.

The OEMakeReceptorOptions class defines the following public methods:

- · GetAutoConstraints and SetAutoConstraints
- · GetBoxExtension and SetBoxExtension
- GetBoxMol and SetBoxMol
- GetNegativeImageType and SetNegativeImageType
- · GetTargetMask and SetTargetMask
- · GetTargetPred and SetTargetPred

#### **Constructor**

```
OEMakeReceptorOptions();
OEMakeReceptorOptions (const OEMakeReceptorOptions &)
```

Default and copy constructors.

#### operator=

OEMakeReceptorOptions &operator=(const OEMakeReceptorOptions &)

## **GetAutoConstraints**

**bool** GetAutoConstraints () const

See SetAutoConstraints method.

## **GetBoxExtension**

double GetBoxExtension() const

See SetBoxExtension method.

## **GetBoxMol**

const OEChem:: OEMolBase& GetBoxMol() const

See SetBoxMol method.

#### GetNegativeImageType

unsigned GetNegativeImageType() const

See SetNegativeImageType method.

#### **GetTargetMask**

unsigned GetTargetMask() const

See SetTargetMask method.

### **GetTargetPred**

std::string GetTargetPred() const

See SetTargetPred method.

## **SetAutoConstraints**

bool SetAutoConstraints (const bool)

Sets flag if protein constraints should be automatically detected and added to the receptor. The auto generated constraints are kept as disabled. Default: True.

#### **SetBoxExtension**

bool SetBoxExtension (const double)

Sets the **amount** for each box face to be extended relative to the minimum box enclosing the  $BoxMOL$ . Default: 0.0.

## **SetBoxMol**

```
bool SetBoxMol(const OEChem::OEMolBase&)
bool SetBoxMol(OEChem::oemolistream& fstream)
```

Sets the **molecule** representing the active site on the proteinStructure. The minimum size box that encloses the molecule plus any desired extension is used as the active site encloser. For the second overload, only the first molecule from the input oemolistream is used.

#### **SetNegativeImageType**

```
bool SetNegativeImageType(const unsigned)
```

Sets the negative image type to be generated. Allowed methods are defined in the OENegativeImageType namespace. Default is OENegativeImageType\_StandardShape.

#### **SetTargetMask**

bool SetTargetMask (const unsigned)

Sets the **target mask** specifying the components of the design unit to be used as receptor target. Allowed methods are defined in the OEDesignUnitComponents namespace. Default: targetComplexNoSolvent.

#### **SetTargetPred**

bool SetTargetPred(const std::string)

Sets the **target predicate** which subsets the components in the TargetMask from the design unit if it matches anything in a specific component.

#### **OEPoseOptimizer**

class OEPoseOptimizer

The OEPoseOptimizer can be used to optimize a pose generated from OEPosit calculation, to reduce clashes.

The OEPoseOptimizer class defines the following public methods:

· Optimize

### **Constructor**

```
OEPoseOptimizer()
OEPoseOptimizer(const OEPoseOptimizerOptions &)
OEPoseOptimizer(const OEPoseOptimizer &)
```

Default and copy constructors.

#### operator=

```
OEPoseOptimizer & operator= (const OEPoseOptimizer &)
```

#### **Optimize**

```
unsigned Optimize (OEBio:: OEDesignUnit& du, const unsigned proteinMask, const unsigned
\rightarrowligandMask);
```

Optimizes the pair of protein and ligand in the posed design unit. Returns true if optimization was successful.

#### **OEPoseOptimizerOptions**

class OEPoseOptimizerOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for docking with OEDock.

The OEPoseOptimizerOptions class defines the following public methods:

- · GetFlexRange and SetFlexRange
- · GetForceField and SetForceField
- · GetNonBondCutoff and SetNonBondCutoff

#### **Constructor**

```
OEPoseOptimizerOptions();
OEPoseOptimizerOptions (const OEPoseOptimizerOptions &)
```

Default and copy constructors.

#### operator=

OEPoseOptimizerOptions & operator=(const OEPoseOptimizerOptions &)

### **GetFlexRange**

double GetFlexRange() const

See SetFlexRange method.

## **GetForceField**

const OEFF:: OEComplexFF\* GetForceField() const

See SetForceField method.

#### **GetNonBondCutoff**

double GetNonBondCutoff() const

See SetNonBondCutoff method.

#### **SetFlexRange**

bool SetFlexRange (const double)

Sets the distance from ligand defining residues that should be considered flexible during pose optimization. Default: 2.0

## **SetForceField**

```
bool SetForceField(const unsigned)
bool SetForceField(const std::string&)
bool SetForceField(const OEFF::OEComplexFF&)
```

Sets the force field for pose optimization.

## **SetNonBondCutoff**

bool SetNonBondCutoff (const double)

Sets the non-bonded interactions cutoff during pose optimization. Default: 40.0

### **OEPosit**

#### class OEPosit

OEPosit is used to pose predict multiconformer molecules in an active site.

The OEPosit class defines the following public methods:

- · AddReceptor
- · ClearReceptors
- $\bullet$  Dock
- · GetHighScoresAreBetter
- GetName
- · GetInvalidScore
- · MethodChoice
- · RankDesignUnits
- ScoreLigand

#### Deprecated methods of the class:

- · DockMultiConformerMolecule
- · Initialize
- · RankReceptors

### **Constructor**

```
OEPosit ( const OEPositOptions & options = OEPositOptions () )
OEPosit (const OEPosit &)
```

Default and copy constructors.

### operator=

OEPosit & operator= (const OEPosit &)

#### **AddReceptor**

```
bool AddReceptor (const OEBio:: OEDesignUnit&)
bool AddReceptor (const OEChem:: OEMolBase&)
```

Adds a receptor to the list of receptors to pose against. The function returns  $\tau$  rue if receptor is addded successful. The first overload expects a design unit that contains a receptor. The second overload works on a variation of molecule that contains receptor data.

**Note:** Since OEPosit can generate pose using any of the methods described in OEPositMethod, constraints present in the receptor may or may not play any role for the specific pose generation. Constraints only effect the generated pose when OEPositMethod FRED or OEPositMethod HYBRID is the underlying method.

#### **ClearReceptors**

void ClearReceptors()

Removes all existing receptors. Removing receptors will un-initialize an already initialized OEPosit instance.

#### **Dock**

```
unsigned Dock (OESinglePoseResult & res, const OEChem:: OEMCMolBase& mol) const;
unsigned Dock (OEPositResults &res, const OEChem:: OEMCMolBase& mol,
               const unsigned numPoses = 1) const
```

Dock the input molecule mol. The second overload can return alternate docked poses, in addition to the top scoring pose, with numPoses being the maximum desired number of poses.

The return value of this method describes the result of the docking, with a value from the OEDockingReturnCode namespace. A result of OEDockingReturnCode\_Success indicates docking was successful.

#### **GetHighScoresAreBetter**

bool GetHighScoresAreBetter() const

This always returns true for OEPosit.

#### GetName

std::string GetName() const

Returns the name of the scoring function docked poses are scored with.

#### **GetInvalidScore**

float GetInvalidScore() const

Returns the invalid score returned by OEPosit. These values are set up to sort invalid values in reverse order from the best reported values.

### **Islnitialized**

bool IsInitialized() const

Returns true if this object has been successfully initialized and is ready to dock molecules.

#### **MethodChoice**

unsigned MethodChoice(const unsigned recIdx, const OEChem::OEMCMolBase& mol). → const

Returns the method that would be used for pose prediction for a given ligand against a given receptor.

#### **RankDesignUnits**

```
OESystem::OEIterBase<OEBio::OEDesignUnit>* OEPosit::RankDesignUnits(const.
→OEChem::OEMCMolBase&) const
```

Rank the design units, from best to worst receptors, to pose against, for the specified ligand.

#### **DockMultiConformerMolecule**

**Warning:** This is a deprecated API. Please use  $Dock$  instead.

Both overloads of this method dock *inputMol* into the receptor added by the  $OEPosit$ . Initialize method.

The return value of this method describes the result of the docking, with a value from the OEDockingReturnCode namespace. A result of OEDockingReturnCode\_Success indicates docking was successful.

```
unsigned int DockMultiConformerMolecule (OEChem:: OEMolBase& dockedMol,
                                         const OEChem:: OEMCMolBase& inputMol)
```

This overload of OEPosit. DockMultiConformerMolecule returns the top scoring pose.

**dockedMol** Docked pose with the best pose prediction probability of *inputMol*.

*inputMol* A multiconformer representation of a molecule to dock.

The score of the docked pose can be obtained by calling the GetEnergy method of *dockedMol*.

**Initialize** 

Warning: This is a deprecated API. Please use AddReceptor instead.

bool Initialize (const OEChem:: OEMolBase& receptor)

Initializes OEPosit with receptor to pose ligand against. Calling initialize will remove any existing receptors in the current OEPosit instance. Function returns  $\tau$  rue if setup was successful and  $f$ alse otherwise.

#### **RankReceptors**

Warning: This is a deprecated API. Please use RankDesignUnits instead.

```
OESystem::OEIterBase<OEChem::OEMolBase>* OEPosit::RankReceptors(const.
→OEChem::OEMCMolBase&) const
```

Rank the receptors, from best to worst, to pose against, for the specified ligand.

#### **ScoreLigand**

This is a deprecated API. This method is only compatible with **Warning:** DockMultiConformerMolecule, for obtaining a score (pose probability) after the pose has been generated.

Method provides invalid score when called on poses generated using  $Dock$ . The scores (pose probability) from that calculation are available in the resulting OESinglePoseResult.

float ScoreLigand (const OEChem:: OEMolBase& pose) const

Rescores a pose within the active site.

If an error occurs this function will return the limiting large double in  $C++$ .

### **OEPositOptions**

class OEPositOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for performing pose prediction using POSIT.

#### The OEPositOptions class defines the following public methods:

- GetAllowedClashType and SetAllowedClashType
- GetBestReceptorPoseOnly and SetBestReceptorPoseOnly
- · GetExcludeSelf and SetExcludeSelf
- GetFlexiOverlayOptions and SetFlexiOverlayOptions

- GetFullConformationSearch and SetFullConformationSearch
- · GetIgnoreNitrogenStereo and SetIgnoreNitrogenStereo
- GetMinProbability and SetMinProbability
- · GetPoserCacheCount and SetPoserCacheCount
- GetPoseRelaxMode and SetPoseRelaxMode
- · GetPoseRelaxOptions and SetPoseRelaxOptions
- · GetPositMethods and SetPositMethods
- GetTorLib and SetTorLib

#### **Constructor**

```
OEPositOptions();
OEPositOptions (const OEPositOptions &)
```

Default and copy constructors.

#### operator=

OEPositOptions & operator= (const OEPositOptions &)

#### **GetAllowedClashType**

unsigned GetAllowedClashType() const

See SetAllowedClashType method.

#### **GetBestReceptorPoseOnly**

bool GetBestReceptorPoseOnly() const

See SetBestReceptorPoseOnly method.

### **GetExcludeSelf**

unsigned GetExcludeSelf() const

See SetExcludeSelf method.

### **GetFlexiOverlayOptions**

```
OEFlexiOverlayOptions& GetFlexiOverlayOptions()
const OEFlexiOverlayOptions& GetFlexiOverlayOptions() const
```

See SetFlexiOverlayOptions method.

## **GetFullConformationSearch**

**bool** GetFullConformationSearch() const

See SetFullConformationSearch method.

### GetIgnoreNitrogenStereo

bool GetIgnoreNitrogenStereo() const

See SetIqnoreNitrogenStereo method.

#### **GetMinProbability**

double GetMinProbability () const

See SetMinProbability method.

## **GetPoserCacheCount**

bool GetPoserCacheCount () const

See SetPoserCacheCount method.

#### **GetPoseRelaxMode**

unsigned GetPoseRelaxMode() const

See SetPoseRelaxMode method.

#### **GetPoseRelaxOptions**

```
OEPoseOptimizerOptions& GetPoseRelaxOptions()
const OEPoseOptimizerOptions& GetPoseRelaxOptions() const
```

See SetPoseRelaxOptions method.

## **GetPositMethods**

unsigned int GetPositMethods() const

See SetPositMethods method.

## **GetTorLib**

const OETorLib\* GetTorLib() const

See Set TorLib method.

## SetAllowedClashType

bool SetAllowedClashType (const unsigned)

Sets the allowed clash type between the ligand pose and the protein, for pose generation. Allowed clash types are defined in the OEAllowedClashType namespace.

The allowed clash type defines if a generated pose contains a clash or not, as reported in a pose calculation result. The allowed clash type also determines if a relaxation of the pose would be carried out when Set PoseRelaxMode is set to OEPoseRelaxMode\_CLASHED. Default is OEAllowedClashType\_HYDROGEN.

### **SetBestReceptorPoseOnly**

```
bool SetBestReceptorPoseOnly(const bool)
```

Sets flag if only the best receptor should be considered for pose prediction. If this flag set to false the pose prediction is performed using all of the receptors and the best set of poses from all of the receptors combined is provided as the results. With the default setting of true pose prediction is only performed on the best receptor for any given ligand. Note that, setting the flag to false could increase the runtime significantly depending on the number of receptors used for the calculation.

### **SetExcludeSelf**

#### bool SetExcludeSelf (const bool)

Sets flag to exclude receptor that contains a given ligand as its bound ligand, when choosing the best receptor for a ligand during pose prediction. This option is meant to be used when running cross docking validation experiments, and allows the user to prevent docking a ligand to a receptor containing itself, without having to generate a number of leave one out receptor datasets. Default: False.

## **SetFlexiOverlayOptions**

void SetFlexiOverlayOptions (const OEShapeFitOptions&)

Sets *options* related to flexible optimization with shape, color, and forcefield, relevant for pose generation with OEPositMethod\_SHAPEFIT.

### **SetFullConformationSearch**

bool SetFullConformationSearch (const bool)

Sets flag to perform full conformation search. Setting this option to false disables internal rotamer conformer searching during the flexible searching algorithm. If this option is set to false and a 3D input is not given, this setting is ignored and a full conformation search is automatically performed. Default: true.

### SetIgnoreNitrogenStereo

bool SetIgnoreNitrogenStereo (const bool)

Sets flag to ignore Nitrogen stereo specifications in input molecule. Setting this option to false ignores Nitrogen stereo specifications in the input molecule, and a value to  $\pm \text{rue}$  ensures that any specified Nitrogen stereo information is restored. A molecule would always be processed, irrespective of this setting. When Nitrogen stereo is specified in the incoming molecule, setting flag is set to true would respect those stereo specifications. Default: false.

### **SetMinProbability**

bool SetMinProbability (const double)

Sets the minimum pose probability, for poses to be of interest. Poses that has a probability below the minimum value are not relaxed even when the SetPoseRelaxMode is set to CLASHED or ALL `. Default is 0.33.

### **SetPoserCacheCount**

```
bool SetPoserCacheCount (const unsigned)
```

Sets the maximum number of posers to be kept in memory cache during **POSIT** calculation. Each poser takes  $\sim 0.75GB$ of memory. Ability to keep more poser in the cache speeds up the calculation when working with multiple receptors. Default is 10.

## **SetPoseRelaxMode**

bool SetPoseRelaxMode (const unsigned)

Sets the **trigger to perform relaxation** of the generated pose. The relaxation is performed by allowing flexibility to the ligand and parts of the receptor. Turning on relaxation can significantly slow down the calculations. Pose relaxation modes are defined in the OEPoseRelaxMode namespace. Default is OEPoseRelaxMode\_NONE.

### **SetPoseRelaxOptions**

**void** SetPoseRelaxOptions (const OEPoseOptimizerOptions&)

Sets *options* related to post-optimization of the generated pose.

#### **SetPositMethods**

bool SetPositMethods (const unsigned)

Sets the posing methods to be used. Methods are set as bits in the supplied integer, see the OEPositMethod namespace for more details. Default is OEPositMethod\_ALL.

### **SetTorLib**

```
bool SetTorLib (const unsigned)
bool setTorLib(const std::string&)
bool SetTorLib(const OEConfGen::OETorLib&)
```

Sets the torsion library that is used for torsion driving during conformer generation. The first overload takes an unsigned from the OETorlibType namespace, and the second overload takes the corresponding string values. Default: Original

#### **OEPositProbability**

#### class OEPositProbability

The OEPositProbability can be used to estimate confidence, in terms of probability, that a ligand pose can be accurately predicted, with respect to the reference ligand or design unit receptor.

This function is helpful in selecting a receptor or reference ligand to pose against from a group of receptors.

#### The OEPositProbability class defines the following public methods:

- · Estimate
- · PoseEstimate
- · SetupRef

#### **Constructor**

```
OEPositProbability()
OEPositProbability (const OEPositProbabilityOptions &)
OEPositProbability (const OEPositProbability &)
```

Default and copy constructors.

#### operator=

OEPositProbability & operator=(const OEPositProbability &)

#### **Estimate**

```
double Estimate (const OEChem:: OEMolBase& mol)
double Estimate (const OEChem:: OEMCMolBase& mol)
```

Provides the estimated probability. With the OEMolBase variation of the argument, multi-conformer molecule is generated with internal settings before producing an estimate.

#### **PoseEstimate**

```
double PoseEstimate (const OEChem:: OEMolBase& mol)
double PoseEstimate (const OEChem:: OEMolBase& mol, const unsigned poseMethod)
```

Provides estimated probability assuming that the specified ligand pose was generated with the reference used in SetupRef. The second argument poseMethod refers to specific methods from OEPositMethod.

#### **SetupRef**

```
bool SetupRef (const OEChem:: OEMolBase& ligand)
bool SetupRef (const OEBio:: OEDesignUnit& du)
```

Sets up the reference system against which the pose is to be generated.

### **OEPositResults**

```
class OEPositResults
```

This class provides results of a collection of poses, obtained from OEPosit calculation.

#### The OEPositResults class defines the following public methods:

- GetNumPoses
- · GetReturnCode
- · GetSinglePoseResults

## **Constructors**

```
OEPositResults()
OEPositResults (const OEPositResults&)
```

Default and copy constructors.

#### operator=

```
OEPositResults & operator= (const OEPositResults &)
```

#### **GetNumPoses**

unsigned GetNumPoses() const

Returns the number of poses in this collection.

## **GetReturnCode**

unsigned GetReturnCode() const

Returns the calculation return code, defined in OEDockingReturnCode namespace.

### **GetSinglePoseResults**

OESystem:: OEIterBase<OESinglePoseResult>\* GetSinglePoseResults() const

Returns an iterator over the OESinglePoseResult in this collection.

#### **OEScore**

class OEScore

OEScore is a class for scoring and optimizing poses within the active site. Use of this class is as follows:

- 1. Initialize the active site by passing either a receptor (see chapter receptor chapter) or a protein and box to the OEScore. Initialize method.
- 2. Score or optimize the molecules using:
  - · OEScore. ScoreLigand
  - · OEScore. ScoreAtom
  - · OEScore. ScoreLigandComponent
  - · OEScore. ScoreAtomComponent
  - · OEScore. SystematicSolidBodyOptimize
  - · OEScore. AnnotatePose

### **Constructor**

OEScore (const unsigned int scoring = OEScoreType::Default)

Constructs OEScore to use the specified *scoring* function from the OEScoreType namespace.

### **Islnitialized**

bool IsInitialized() const

Returns true if this object has been successfully initialized and is ready to score poses.

#### **Initialize**

```
bool Initialize (const OEBio:: OEDesignUnit& receptor)
bool Initialize (const OEChem:: OEMolBase& receptor)
bool Initialize (const OEChem:: OEMolBase& protein, const OEBoxBase& box)
```

Sets up this object to score poses within an active site. This function returns true if initialization was successful. This object does not depend upon receptor once this call is completed *(i.e.* receptor can be destroyed after calling this method). The first overload expects a design unit that contains a receptor. The second overload works on a variation of molecule that contains receptor data. The last overload works with a protein and box enclosing the active site. Method returns  $\tau$  rue if setup was successful.

#### **GetName**

std::string GetName() const

Returns the name of the scoring function.

#### **GetComponentNames**

OESystem:: OEIterBase<const std:: string>\* GetComponentNames() const

Returns the name of the scoring function components.

#### **GetHighScoresAreBetter**

bool GetHighScoresAreBetter() const

Returns true if higher scores indicate a better result.

Returns false if lower scores indicate a better result.

#### **ScoreLigand**

float ScoreLigand (const OEChem:: OEMolBase& pose)

Scores a pose within the active site.

*pose* Structure of a pose within the active site

If an error occurs this function will return FLT\_MAX if OEScore. GetHighScoresAreBetter returns false or -FLT MAX otherwise.

#### **ScoreAtom**

float ScoreAtom (const OEChem:: OEAtomBase& atom, const OEChem:: OEMolBase& pose)

Returns the score of an atom of a given pose within the active site.

atom Atom of pose to score.

*pose* Structure of a pose within the active site

If an error occurs this function will return FLT\_MAX if OEScore. GetHighScoresAreBetter returns false or -FLT MAX otherwise.

## **ScoreLigandComponent**

float ScoreLigandComponent (const OEChem:: OEMolBase& pose, std::string compName)

Returns the given component's contribution to the total score.

*pose* Structure of a pose within the active site

compName Name of the score component to report. Name must be one returned by OEScore.GetComponentNames.

If an error occurs this function will return FLT\_MAX if OEScore. GetHighScoresAreBetter returns false or -FLT MAX otherwise.

#### **ScoreAtomComponent**

```
float ScoreAtomComponent (const OEChem:: OEAtomBase& atom,
                          const OEChem:: OEMolBase& pose,
                          std::string compName)
```

Returns the given components contribution to the score of a given atom score.

atom Atom of pose to score.

*pose* Structure of a pose within the active site

**compName** Name of the score component to report. Name must be one returned by OEScore.GetComponentNames.

If an error occurs this function will return FLT\_MAX if OEScore. GetHighScoresAreBetter returns false or -FLT\_MAX otherwise.

#### **SystematicSolidBodyOptimize**

Performs a solid body optimization on the *pose* or *poses* passed. Three rotational and three translational degrees of freedom are explored, the pose (and protein) are held rigid. A plus and minus rotational step is taken for each rotational and translational degree of freedom (for a total of 3<sup>1</sup>6 or 729 positions tested for each pose).

Both overloads return true if no error occurred.

```
bool SystematicSolidBodyOptimize(OEChem:: OEMCMolBase& poses,
                                 unsigned int searchResolution
                                   = OESearchResolution::Default)
```

This overload of OEScore. SystematicSolidBodyOptimize optimizes all poses of an OEMC-MolBase.

- poses An OEMCMolBase with conformers that are poses within the active site to be optimized.
- searchResolution Search resolution of the optimization (see OESearchResolution constant namespace).

The optimized poses are returned in *poses*. This poses retain their original ordering and are not ordered by the new optimized score.

```
bool SystematicSolidBodyOptimize(OEChem::OEMolBase& pose,
                                 unsigned int searchResolution
                                   = OESearchResolution::Default)
```

This overload of OEScore. SystematicSolidBodyOptimize optimizes a single pose.

**pose** A pose within the active site to be optimized.

searchResolution Search resolution of the optimization (see OESearchResolution constant namespace).

#### **AnnotatePose**

Adds VIDA scoring annotation to the *pose* or *poses* passed.

The annotated poses must be written out in either *oeb* or *oeb.gz* format and are only viewable in **VIDA**.

bool AnnotatePose (OEChem:: OEMolBase& pose)

This overload of OEScore. AnnotatePose annotates a single pose.

*pose* Structure of a pose within the active site

**bool** AnnotatePose (OEChem:: OEMCMolBase& poses)

This overload of OEScore. AnnotatePose annotates all poses of a given ligand.

*poses* An OEMCMolBase the conformers of which are poses within the active site.

### **CacheScoringSetup**

This function caches the current scoring setup of the *OEScore* object onto a receptor object. When another OEScore object is initialized with this receptor the it will read in the cached score data rather than recalculating it from scratch, thus improving the startup time of the OEScore object.

```
bool CacheScoringSetup (OEBio::OEDesignUnit& receptor, bool clearOldData = ...
\leftrightarrowtrue)
bool CacheScoringSetup(OEChem:: OEMolBase& receptor, bool clearOldData = true)
```

- **receptor** A receptor object. This must be the same receptor object the OEScore object was initialized with or an exact copy.
- *clearOldData* Flag to clear cached data from a prior call to CacheScoringSetup with this receptor. The cached data can be quite sizable (hundreds of megabytes), so leaving this flag at the default value of true is recommended.

Note: The cached score data on a receptor will be saved when the receptor is written to a file.

#### **OESinglePoseResult**

#### class OESinglePoseResult

This class provides results of a single pose, obtained from the *OEPosit* calculation.

#### The OESinglePoseResult class defines the following public methods:

- · GetDesignUnit
- · GetTargetMask
- · GetTargetPred
- · GetHasClash
- · GetNumClashes
- · GetNumContacts
- GetPose
- · GetPositMethod
- · GetProbability
- · GetReceptorIndex
- · GetRelaxAttempted
- · GetRelaxed
- · GetRelaxStatus
- · GetRelaxStatusStr

## **Constructors**

```
OESinglePoseResult()
{\tt OESinglePoseResult}\ ({\tt const\; OESinglePoseResult\,\&})
```

Default and copy constructors.

#### operator=

OESinglePoseResult & operator=(const OESinglePoseResult &)

#### **GetDesignUnit**

const OEBio:: OEDesignUnit& GetDesignUnit() const

Returns the resulting design unit consisting of the target and the ligand pose.

#### **GetTargetMask**

unsigned GetTargetMask() const

Returns the target mask used to generate the receptor. The mask and predicate can be used with the OEDesignUnit. Get Components method to generate the molecule used in receptor generation.

### **GetTargetPred**

OEBio:: OEAtomMatchResidue GetTargetPred() const

Returns the residue based OEAtomMatchResidue predicate used with the corresponding target mask to generate the receptor. The mask and predicate can be used with the OEDesignUnit. GetComponents method to generate the molecule used in receptor generation.

#### See also:

- OEAtomMatchResidue class
- · OEDesignUnit.GetComponents method

## **GetHasClash**

bool GetHasClash() const

Returns true if the pose contains clash, false otherwise. The *clash* is defined based on the option used in the OEPosit calculation.

## **GetNumContacts**

unsigned GetNumContacts() const

Returns the *number of contacts* in the pose, based on the *clash* type defined during the *OEPosit* calculation.

#### **GetNumClashes**

unsigned GetNumClashes () const

Returns the number of clashes in the pose, based on the clash type defined during the OEPosit calculation.

#### **GetPose**

const OEChem:: OEMol& GetPose() const

Returns the ligand pose conformer.

#### **GetPositMethod**

unsigned GetPositMethod() const

Returns the method used to generate this pose. The returned values correspond to OEPositMethod.

### **GetProbability**

double GetProbability() const

Returns the **POSIT** probability corresponding to this pose.

#### **GetReceptorIndex**

unsigned GetReceptorIndex() const

Returns the receptor index corresponding to the order they were added to the OEPosit instance.

#### **GetRelaxAttempted**

bool GetRelaxAttempted() const;

Returns true if relaxation was attempted.

## **GetRelaxed**

bool GetRelaxed() const

Returns true if the pose is relaxed.

## **GetRelaxStatus**

unsigned GetRelaxStatus() const;

Returns status code corresponding to the attempted relaxation.

### **GetRelaxStatusStr**

std::string GetRelaxStatusStr() const;

Returns status corresponding to the attempted relaxation.

## **5.1.2 OEDocking Constants**

## **OEAllowedClashType**

Constants in this namespace are used to define clash types allowed in a OEPosit calculation.

### **NONE**

No clash is allowed

## **HYDROGEN**

Clash involving hydrogen is allowed, but not between heavy atoms

### **ANY**

Any clash is allowed

## **OEDockingReturnCode**

A constant from this namespace is returned by OEDock. DockMultiConformerMolecule and OEPosit. Dock to indicate the outcome of the docking or posing.

## **Aborted**

Docking was aborted by the user (via the OETracerBase. Aborted method)

## **ConformerGenError**

Typically indicates the failure of  $OEPosit$ . Dock to generate any internal conformations.

## **CoordError**

The geometry of the chemical interactions on the ligand could not be determined. This generally indicates that the ligand is broken in some way (e.g. valence errors).

## **EmptyLigand**

Docking failed because the ligand contained no atoms.

## **EmptyProtein**

The protein passed to the OEDock. Initialize or OEPosit. Initialize methods contained no atoms.

## **Failure**

All other docking failures.

## **GridSetupError**

One of the scoring grids could not be setup. This generally indicates that the protein structure is broken.

### **InvalidScore**

Calculated score is near numeric limits and not valid.

## **NoConstraintMatch**

The supplied ligand cannot match the docking constraints.

### **NotInitialized**

Docking failed because the OEDock or OEPosit object has not been initialized (see OEDock. Initialize or OEPosit. Initialize)

## **NoValidNonClashPoses**

For *OEPosit*, no poses remaining after clash removal.

### **NoValidPoses**

No ligand poses could fit within the active site. Increasing the size of the receptor's outer contour volume (see Negative *Image* section) and re-initializing the OEDock object with the new receptor may allow the ligand to dock.

## **OptimizationError**

Optimization of the ligand failed.

## **OutsideGrid**

This error code is not currently used.

## **ScoreError**

Problem assigning scores with OEMolBase. SetEnergy method.

#### **Success**

Docking was successful.

## **TypingError**

One or more of the atoms on the ligand could not be typed.

## **OEDockMethod**

Constants in this namespace are used by the constructor of OEDock and OEHybrid (see OEDock. Constructor and  $OEHybrid$ . Constructor respectively) to specify the scoring function used during the exhaustive search and optimization and final scoring.

### **Shapegauss**

**Exhaustive Search** Shapegauss **Optimization and Scoring Shapegauss** 

## **PLP**

**Exhaustive Search PLP Optimization and Scoring PLP** 

## Chemgauss3

**Exhaustive Search** Chemgauss3 **Optimization and Scoring** Chemgauss3

## Chemgauss4

**Exhaustive Search** Chemgauss3 **Optimization and Scoring Chemgauss4** 

## **Chemgauss**

Same as OEDockMethod\_Chemgauss4

## **Chemscore**

Exhaustive Search Chemgauss3 **Optimization and Scoring Chemscore** 

## **Hybrid1**

**Exhaustive Search** Chemical Gaussian Overlay (CGO) **Optimization and Scoring Chemgauss3** 

## Hybrid<sub>2</sub>

**Exhaustive Search** Chemical Gaussian Overlay (CGO) **Optimization and Scoring Chemgauss4** 

## **Hybrid**

Same as OEDockMethod\_Hybrid2

## **Default**

Same as OEDockMethod\_Chemgauss4

## **INVALID**

Return value used to indicate an error

## **OENegativeImageType**

These constants are used by the  $OEMakeRecept \, or \, function$  to specify the type of negative image it should make.

### **LargeShape**

Create a negative image designed for larger sites. This type of negative image tends to prefer solvent exposed areas over tight cavities.

### **StandardShape**

Standard negative image appropriate for most sites

### **SmallShape**

Create a negative image designed for smaller sites. This type of negative image tends to prefer tight cavities over more solvent exposed areas.

### **Default**

Same as OENegativeImageType\_StandardShape

## **INVALID**

Return value used to indicate an error

## **OEPoseRelaxMode**

Constants in this namespace are used to define pose relaxation modes (i.e., when to perform a pose relaxation) in a OEPosit calculation.

## **NONE**

Do not perform relaxation on any generated pose.

### **CLASHED**

To perform relaxation only on those poses that contain a clash.

## **ALL**

To perform relaxation on all generated poses.

### **OEPositMethod**

Constants in this namespace are used to indicate the available posing methods used by SetPositMethods and GetPositMethods.

## **ALL**

This is equivalent to "SHAPEFIT | HYBRID | FRED | MCS". This is the default.

### **FRED**

The molecule was posed using the default method. See OEDockMethod\_Chemgauss4.

## **HYBRID**

The molecule was posed using the HYBRID method. See OEDockMethod\_Hybrid2.

#### **SHAPEFIT**

The molecule was posed using the shapefit method. See PLP.

## **UNKNOWN**

The ligand was not posed.

### OEProteinConstraintType

Constants in this namespace are used by the OEProteinConstraint class to specify the type of ligand atom that is allowed to satisfy a protein docking constraint.

#### **Chelator**

A chelating heavy atom on the ligand must interact with the protein metal constraint atom to satisfy the constraint.

### **Acceptor**

A hydrogen bond acceptor on the ligand must interact with the protein donor to satisfy the constraint.

#### **Donor**

A hydrogen bond donor on the ligand must interact with the protein acceptor to satisfy the constraint.

## **Contact**

A heavy atom on the ligand must contact the protein constraint atom to satisfy the constraint.

## Lipophilic

A non-polar heavy atom on the ligand must contact the protein

## **Unknown**

Unknown constraint type. Most likely this receptor was written by a future version of this toolkit or FRED.

## **OEScoreType**

Constants in this namespace are used by the constructor of OEScore (see OEScore. Constructor) to specify the scoring function OEScore will use.

## **Shapegauss**

Shapegauss.

## **PLP**

 $PLP$ .

## Chemgauss3

Chemgauss3.

## **Chemgauss4**

Chemgauss4.

## **Chemgauss**

Same as OEScoreType\_Chemgauss4.

## **Chemscore**

Chemscore.

## **Default**

Same as OEScoreType\_Chemgauss4.

## **INVALID**

Used as a return type to indicate an error.

## **OESearchResolution**

Constants in this namespace are used by the constructor of OEDock (see OEDock. Constructor) to specify the search resolution used during the exhaustive search and optimization as well as the number of poses passed from the exhaustive search to the optimization step. It is also used by the OEScore. SystematicSolidBodyOptimize method to specify the resolution of the optimization (the exhaustive search values are ignored in this case).

Rotational stepsize is the furthest distance any atom will move in a single rotational step.

All distances are measured in angstroms.

### **High**

**Exhaustive Search Resolution** 

Translational 1.0

Rotational 1.0

**Optimization Resolution** 

Translational 0.5

Rotational 0.5

Number exhaustive search poses optimized during docking

1000

## **Standard**

**Exhaustive Search Resolution** Translational 1.0 Rotational 1.5 **Optimization Resolution** Translational 0.5 Rotational 0.75 Number exhaustive search poses optimized during docking 100

## Low

**Exhaustive Search Resolution** Translational 1.5 Rotational 2.0 **Optimization Resolution** Translational 0.75 Rotational 1.0 Number exhaustive search poses optimized during docking 100

## **Default**

Same as OESearchResolution\_Standard

## **INVALID**

Used as a return type to indicate an error

## **5.1.3 OEDocking Functions**

## **OEAddDockingInteractions**

**bool** OEAddDockingInteractions (OEBio:: OEInteractionHintContainer &asite)

Perceives interactions (contact, hydrogen bonding, chelator) between the two molecules stored in the OEInteraction-HintContainer object.

#### See also:

- · OEPerceiveInteractionHints function of OEChem TK
- Example in the Perceive and Print Protein-Ligand Interactions section of the OEChem TK manual about accessing the interactions.
- Example in the Depicting Active Site Interactions section of the Grapheme TK manual about visualizing the interactions.

## **OECreateDUFromReceptorMol**

```
bool OECreateDUFromReceptorMol(OEBio::OEDesignUnit& du, const
→OEChem::OEMolBase& recMol)
```

Create a OEDesignUnit object from receptor molecule.

#### See also:

- · OEMakeDesignUnits function
- · OEMakeReceptor function

### **OEDockingGetArch**

```
const char *OEDockingGetArch()
```

Returns the architecture of the current version of the OEDocking toolkit. Examples include:

- $\cdot$  microsoft-win32-x86
- redhat-RHEL5-x86 64

### **OEDockingGetLicensee**

```
bool OEDockingGetLicensee(std::string &licensee)
```

Returns the LICENSEE from the current valid Docking TK license.

### **OEDockingGetPlatform**

const char \*OEDockingGetPlatform()

Returns the platform, including compiler version, of the current version of the OEDocking toolkit. Examples include:

- microsoft-win32-msvc9-MD-x86
- $\cdot$  redhat-RHEL5-g++4.1-x86\_64

#### **OEDockingGetRelease**

const char \*OEDockingGetRelease()

Returns the version of this toolkit release. For example: 1.6.1.

#### **OEDockingGetSite**

**bool** OEDockingGetSite(std::string &site)

Returns the SITE from the current valid OEDocking TK license.

#### **OEDockingGetVersion**

unsigned int OEDockingGetVersion()

Returns the build date of the toolkit as an unsigned int. For example: 20090227.

#### **OEDockingReturnCodeGetName**

string OEDockingReturnCodeGetName (unsigned int returnCode)

Returns the name of the return code. *returnCode* is a constant from the  $OEDockingReturnCode$  namespace.

#### **OEDockMethodConfigure**

bool OEDockMethodConfigure(OESystem::OEInterface& itf, std::string flagName)

This function is used in conjunction with the OEDockMethodGetValue. It adds a command line flag to the *iff* to specify a dock method to use. Once the command line has been parsed (OEParseCommandLine) the *itf* and flagName are passed to OEDockMethodGetValue that will return the constant from the OEDockMethod namespace associated with the dock method the user selected (or the default scoring function if the user didn't specify one).

**Note:** The parameter added to *itf* will be of type string, name *flagName*, and have legal values associated with the dock method.

## **OEDockMethodGetName**

string OEDockMethodGetName (unsigned int method)

Returns the name of the scoring function, *method* is a constant from the *OEDockMethod* namespace.

#### **OEDockMethodGetValue**

unsigned int OEDockMethodGetValue(std::string name)

Returns the value of a constant from the OEDockMethod namespace associated with the scoring function name, or OEDockMethod\_INVALID if the name is not recognized.

```
unsigned int OEDockMethodGetValue (const OESystem:: OEInterface& itf, std:: string
\rightarrowflaqName)
```

Used in conjunction with the OEDockMethodConfigure function. Returns a constant from the OEDockMethod namespace associated with the dock method the user specified on the command line, or OEDockMethod\_Default if the user did not specify a value. itf and flagName should be the same as those passed to the OEDockMethodConfigure function and OEParseCommandLine should have been called on iff.

#### **OEGetEstimatedPositProbability**

```
double OEGetEstimatedPositProbability (
        const OEChem:: OEMCMolBase &ligand,
        const OEBio:: OEDesignUnit &du) ;
double OEGetEstimatedPositProbability (
        const OEChem:: OEMCMolBase & ligand,
        const OEChem:: OEMolBase
                                   &receptor);
```

Given a multi conformer ligand and a receptor, return the probability that, if the ligand binds to the receptor, the binding pose of the ligand can be retrieved.

This function is helpful in selecting a receptor to pose against from a group of receptors.

#### **OEGetPositMethod**

unsigned int OEGetPositMethod (const OEChem:: OEMolBase &) ;

Return the OEPositMethod used to pose the molecule. The molecule must be posed first. See the OEPositMethod namespace for more details.

#### **OEHasClash**

```
bool OEHasClash (const OEChem:: OEMolBase & ligand,
                   const OEChem:: OEMolBase & receptor,
                   const unsigned allowedType)
```

Returns true if there is clash between the supplied ligand and the receptor. Otherwise, it returns false. The third argument, allowedType, refers to definition of allowed clash type, according to the OEAllowedClashType namespace.

## **OEMakeBoxMolecule**

**bool** OEMakeBoxMolecule (OEChem:: OEMolBase& mol, const OEBoxBase& box)

Creates a molecule (*mol*) out of *box. mol* will have 8 nitrogen atoms, one at each corner of the box and a single bond between appropriate atoms.

Note that this molecule is in no way chemically valid. The purpose of this method is to create a molecule representing box that can be viewed in a molecular visualizer.

#### **OEMakeReceptor**

```
bool OEMakeReceptor (OEBio:: OEDesignUnit& du,
                     const OEMakeReceptorOptions& opts)
```

Create a *receptor* object in the *design unit*. This function returns true if successful.

#### **OENegativeImageTypeGetName**

string OENegativeImageTypeGetName (unsigned int method)

Returns the name of the scoring function. *method* is a constant from the *OENeqativeImageIype* namespace.

#### **OENegativeImageTypeGetValue**

unsigned int OENegativeImageTypeGetValue(std::string name)

Returns the value of a constant from the OENegat i ve ImageType namespace associated with the scoring function name, or OENegativeImageType INVALID if the name is not recognized.

```
unsigned int OENegativeImageTypeGetValue(const OESystem::OEInterface& itf,
                                               std::string flagName)
```

Used in conjunction with the OENegativeImageTypeConfigure function. Returns a constant from the OENegativeImageType namespace associated with the negative image type the user specified on the command line, or OENegativeImageType\_Default if the user did not specify a value. iff and flagName should be the same as those passed to the OENegativeImageTypeConfigurefunction and OEParseCommandLine should have been called on *itf*.

#### **OEPositMethodGetName**

std::string OEPositMethodGetName(unsigned)

Returns method name corresponding to constants defined in OEPositMethod namespace.

### **OEScoreTypeGetName**

string OEScoreTypeGetName (unsigned int scoring)

Returns the name of the scoring function, *scoring* is a constant from this namespace.

#### **OEScoreTypeGetValue**

unsigned int OEScoreTypeGetValue(std::string name)

Returns the value of a constant from this namespace associated with the scoring function *name*, or OEScoreType\_INVALID if the name is not recognized.

This function is defined within the OEScoreType namespace.

```
unsigned int OEScoreTypeGetValue (const OESystem:: OEInterface& itf, std:: string
\rightarrowflagName)
```

Used in conjunction with the  $OEScoreTypeConfigure$  function. Returns a constant from this namespace associated with the scoring function the user specified on the command line, or  $OEScoreType\_Default$  if the user did not specify a value. *itf* and *flagName* should be the same as those passed to the OEScoreTypeConfigure function and OEParseCommandLine should have been called on itf.

#### **OESearchResolutionGetName**

string OESearchResolutionGetName (unsigned int resolution)

Returns the name of the scoring function. *resolution* is a constant from the OESearchResolution namespace.

#### **OESearchResolutionGetValue**

unsigned int OESearchResolutionGetValue(std::string name)

Returns the value of a constant from the OESearchResolution namespace associated with the scoring function name, or OESearchResolution\_INVALID if the name is not recognized.

unsigned int OESearchResolutionGetValue (const OESystem:: OEInterface& itf, std::string flagName)

Used in conjunction with the OESearchResolutionConfigure function. Returns a constant from the OESearchResolution namespace associated with the dock resolution the user specified on the command line, or OESearchResolution\_Default if the user did not specify a value. iff and flagName should be the same as those passed to the OESearchResolutionConfigure function and should have been called on itf.

## **OESetEnergyScore**

```
bool OESetEnergyScore (OEChem:: OEMolBase& pose,
                       OEDock& dock)
```

Sets the energy of pose (OEMolBase.GetEnergy) to the score of the pose calculated with the OEDock. ScoreLigand method of dock.

```
bool OESetEnergyScore (OEChem:: OEMolBase& pose,
                       OEScore& score)
```

Sets the energy of pose (OEMolBase.GetEnergy) to the score of the pose calculated with the OEScore. ScoreLigand method of score.

bool OESetEnergyScore(OEChem:: OEMCMolBase& poses, OEDock& dock, **bool** sortPoses = false)

Sets the energy of each pose of poses (OEMolBase, GetEnergy) to the score of the pose calculated with the OEDock. ScoreLigand method of dock.

If *sortPoses* is true the poses of will also be sorted by score.

```
bool OESetEnergyScore(OEChem:: OEMCMolBase& poses,
                      OEScore& score,
                      bool sortPoses = false)
```

Sets the energy of each pose of poses (OEMolBase.GetEnergy) to the score of the pose calculated with the OEScore. ScoreLigand method of score.

If sortPoses is true the poses will also be sorted by score.

### **OESetEnergyScoreComponent**

bool OESetEnergyScoreComponent (OEChem:: OEMolBase& pose, OEDock& dock, std::string component)

Sets the energy of pose (OEMolBase. GetEnergy) to the component of the score calculated with dock's OEDock. ScoreLigandComponent method.

```
bool OESetEnergyScoreComponent (OEChem:: OEMolBase& pose,
                                OEScore& score,
                                std::string component)
```

Sets the energy of pose (OEMo1Base.GetEnergy) to the component of the score calculated with score's OEScore. ScoreLigandComponent method.

bool OESetEnergyScoreComponent (OEChem:: OEMCMolBase& pose, OEDock& dock, std:: string component, **bool** sortPoses =  $false)$ 

Sets the energy of each pose of poses (OEMolBase.GetEnergy) to the *component* of the score calculate with dock's OEDock. ScoreLigandComponent method.

If sortPoses is true the poses will also be sorted by score.

```
bool OESetEnergyScoreComponent (OEChem:: OEMCMolBase& pose,
                                OEScore& score,
                                std:: string component,
                                bool sortPoses = false)
```

Sets the energy of each pose of poses (OEMolBase. GetEnergy) to the component of the score calculated with score's OEScore. ScoreLigandComponent method.

If sortPoses is true the poses will also be sorted by score.

#### **OESetSDScore**

```
bool OESetSDScore (OEChem:: OEMolBase& pose,
                  OEDock& dock,
                   std::string sdtag)
```

Assigns the score of pose, using the OEDock. ScoreLigand method of dock, to SD data of pose with the given sdtag.

```
bool OESetSDScore (OEChem:: OEMolBase& pose,
                  OEPosit& poser,
                  std::string sdtag)
```

Assigns the score of pose, using the OEPosit. ScoreLigand method of poser, to SD data of pose with the given sdtag.

```
bool OESetSDScore (OEChem:: OEMolBase& pose,
                  OEScore& score,
                   std::string sdtag)
```

Assigns the score of pose, using the OEScore. ScoreLigand method of score, to SD data of pose with the given sdtag.

```
bool OESetSDScore (OEChem:: OEMCMolBase& poses,
                  OEDock& dock,
                  std::string sdtag,
                  bool sortPoses = false)
```

Assigns the score of each pose of poses, using the OEDock. ScoreLigand method of dock, to SD data of the pose with the given sdtag.

If sortPoses is true the poses will also be sorted by score.

```
bool OESetSDScore(OEChem:: OEMCMolBase& poses,
                  OEScore& score,
                  std::string sdtag,
                  bool sortPoses = false)
```

Assigns the score of each pose of poses, using the OEScore. ScoreLigand method of score, to SD data of the pose with the given sdtag.

If sortPoses is true the poses will also be sorted by score.

## **OESetSDScoreComponent**

```
bool OESetSDScoreComponent (OEChem:: OEMolBase& pose,
                            OEDock& dock,
                            std::string component,
                            std::string sdtag)
```

Assigns the component of pose's score, calculated with dock's OEDock. ScoreLigandComponent method, to pose's SD data (with tag sdtag).

```
bool OESetSDScoreComponent (OEChem:: OEMolBase& pose,
                            OEScore& score,
                            std::string component,
                            std::string sdtag)
```

Assigns the component of pose's score, calculated with score's OEScore. ScoreLigandComponent method, to pose's SD data (with tag sdtag).

![](_page_88_Figure_6.jpeg)

Assigns the *component* of the score of each pose of poses, calculated with dock's OEDock. ScoreLigandComponent method, to SD data (with tag sdtag) on the pose.

If sortPoses is true the poses will also be sorted by score.

```
bool OESetSDScoreComponent (OEChem:: OEMCMolBase& poses,
                           OEScoreBase& score,
                           std:: string component,
                           std::string sdtag,
                           bool sortPoses = false)
```

Assigns the component of the score of each pose of poses, calculated with score's OEScore. ScoreLigandComponent method, to SD data (with tag sdtag) on the pose.

If sortPoses is true the poses will also be sorted by score.

### **OESetScore**

```
bool OESetScore (OEChem:: OEMolBase& pose,
                OEDock& dock,
                std::string tag)
```

Assigns the score of pose, using the OEDock. ScoreLigand method of dock, to float generic data of pose with the given tag.

```
bool OESetScore (OEChem:: OEMolBase& pose,
                OEScore& score,
                std::string tag)
```

Assigns the score of pose, using the OEScore. ScoreLigand method of score, to float generic data of pose with the given tag.

```
bool OESetScore (OEChem:: OEMCMolBase& poses,
                OEDock& dock,
                std:: string tag,
                bool sortPoses = false)
```

Assigns the score of each pose of poses, using the OEDock. ScoreLigand method of dock, to float generic data of the pose with the given tag.

If sortPoses is true the poses will also be sorted by score.

```
bool OESetScore (OEChem:: OEMCMolBase& poses,
                OEScore& score,
                std::string tag,
                bool sortPoses = false)
```

Assigns the score of each pose of poses, using the OEScore. ScoreLigand method of score, to float generic data of the pose with the given tag.

If sortPoses is true the poses will also be sorted by score.

### **OESetScoreComponent**

```
bool OESetScoreComponent (OEChem:: OEMolBase& pose,
                          OEDock& dock,
                          std:: string component,
                          std::string tag)
```

Assigns the component of pose's score, calculated with dock's OEDock. ScoreLigandComponent method, to pose's float generic data (with tag tag) on pose.

```
bool OESetScoreComponent (OEChem:: OEMolBase& pose,
                          OEScore& score,
                          std::string component,
                          std::string tag)
```

Assigns the component of pose's score, calculated with score's OEScore. ScoreLigandComponent method, to pose's float generic data (with tag tag) on pose.

```
bool OESetScoreComponent (OEChem:: OEMCMolBase& pose,
                         OEDock& dock,
                         std::string component,
                         std::string tag,
                         bool sortPoses = false)
```

Assigns the *component* of the score of each pose of *poses*, calculated with *dock's* OEDOCK. ScoreLigandComponent method, to float generic data (with tag tag) on the pose.

If sortPoses is true the poses will also be sorted by score.

```
bool OESetScoreComponent (OEChem:: OEMCMolBase& poses,
                         OEScore& score,
                          std:: string component,
                          std:: string tag,
                         bool sortPoses = false)
```

Assigns the component of the score of each pose of poses, calculated with score's OEScore. ScoreLigandComponent method, to float generic data (with tag tag) on the pose.

If sortPoses is true the poses will also be sorted by score.

## **OESetupBox**

```
bool OESetupBox (OEMath:: OEBox&, const OEChem:: OEMolBase&,
                         float addbox = 0.0f);
```

This function sets up the minimum box size that encloses the passed-in molecule, with an option to extend each box face by a specified value *addbox*.

```
bool OESetupBox (OEMath:: OEBox&, const OEChem:: OEMCMolBase&,
                        float addbox = 0.0f;
```

This function sets up the minimum box size that encloses all conformers of the input molecules, with an option to extend each box face by a specified value *addbox*.

## 5.2 Preliminary OEDocking API

## 5.2.1 Preliminary OEDocking Classes

## **OEShapeFit**

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEShapeFit

**Note:** With the default settings, the *OEShapeFit* flexibly optimizes shape overlap and force field.

The OEShapeFit class provides an interface for pose generation using flexible overlay optimization between a reference bound ligand or a bound ligand present in a reference design unit and a fit molecule conformers.

### The OEShapeFit class defines the following public methods:

- SetupRef
- $•$   $Fit$

### **Constructor**

```
OEShapeFit();
OEShapeFit (const OEShapeFit&)
OEShapeFit(const OEShapeFitOptions& options = OEShapeFitOptions())
```

Default and copy constructors. The last constructor takes in an instance of a OEShapeFitOptions.

#### operator=

```
OEShapeFit & operator= (const OEShapeFit&)
```

#### **SetupRef**

```
bool SetupRef(const OEBio:: OEDesignUnit&);
bool SetupRef (const OEChem:: OEMolBase&) ;
```

This method defines the interface for setting up the reference for the OEShapeFit ShapeFit optimization process.

#### Fit

```
OESystem::OEIterBase<OEShapeFitResults>* Fit(OEChem::OEMCMolBase& fitmol, 
\rightarrow const unsigned numPoses = 1)
```

This method optimizes the shape and chemical similarity between the fit molecule and a bound ligand in the design unit, along with intra-molecular forcefield energies of the fit molecule, simultaneously. The reference design unit must be set using Set upRef method.

#### **OEShapeFitOptions**

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in  $C++$  and Python.

class OEShapeFitOptions : public OESystem: : OEOptions

This class provides an interface to setup options to generate pose conformers using **flexible overlay optimization** between the bound ligand present in the reference design unit and a fit molecule using OEShapeFit.

The OEShapeFitOptions class defines the following public methods:

- · GetFullConformationSearch and SetFullConformationSearch
- GetMaxLocalStrain and SetMaxLocalStrain
- GetMaxOptSteps and SetMaxOptSteps
- · GetTorLib and SetTorLib
- · GetFlexiOverlapOptions and SetFlexiOverlapOptions
- · GetRigidOverlayOptions and SetRigidOverlayOptions

## **Constructor**

```
OEShapeFitOptions();
OEShapeFitOptions (const OEShapeFitOptions&)
```

Default and copy constructors.

#### operator=

OEShapeFitOptions & operator=(const OEShapeFitOptions&)

## **GetFullConformationSearch**

bool GetFullConformationSearch() const

See SetFullConformationSearch method.

### **GetMaxOptSteps**

unsigned GetMaxOptSteps() const

See SetMaxOptSteps method.

### **GetTorLib**

const OETorLib\* GetTorLib() const

See Set TorLib method.

### **GetFlexiOverlapOptions**

```
OEFlexiOverlapOptions& GetFlexiOverlapOptions()
const OEFlexiOverlapOptions& GetFlexiOverlapOptions() const
```

Returns a reference to the OEFlexiOverlapOptions instance as currently set. These are options related to flexible overlap optimization using shape, color, and force field. See also SetFlexiOverlapOptions method.

## **GetMaxLocalStrain**

double GetMaxLocalStrain() const

See SetMaxLocalStrain method.

#### **GetRigidOverlayOptions**

```
OEOverlayOptions& GetRigidOverlayOptions()
const OEOverlayOptions& GetRigidOverlayOptions()
                                                 const
```

Returns a reference to the OEOverlayOptions instance as currently set. These are options related to rigid overlay optimization using shape and color. See also SetRigidOverlayOptions method.

#### **MaxLocalStrain**

double MaxLocalStrain() const

See MaxLocalStrain method.

#### **SetFullConformationSearch**

bool SetFullConformationSearch (const bool)

Sets flag to perform full conformation search. Setting this option to true enables internal rotamer conformer generation, prior to running OEShapeFit. Default: false.

### **SetMaxLocalStrain**

bool SetMaxLocalStrain (const double)

Sets the Number allowable local strain in the generated hits. Default: 6.5.

### **SetMaxOptSteps**

bool SetMaxOptSteps (const unsigned)

Sets the maximum number of optimization iteration steps in flexible overlay optimization. Default: 2000 steps.

#### **SetTorLib**

```
bool SetTorLib (const unsigned)
bool setTorLib(const std::string&)
bool SetTorLib(const OEConfGen::OETorLib&)
```

Sets the **torsion library** that is used for torsion driving during conformer generation. The first overload takes an *unsigned* from the OETorLibType namespace, and the second overload takes the corresponding string values. Default: OETorLibType\_Original

## **SetFlexiOverlapOptions**

void SetFlexiOverlapOptions (const OEFlexiOverlapOptions&)

Sets the options related to flexible overlap calculations by passing in OEFlexiOverlapOptions instance.

#### **SetRigidOverlayOptions**

**void** SetRigidOverlayOptions (const OEOverlayOptions&)

Sets the options related to overlay optimization using shape and color by passing in OEFlexiOverlapOptions instance.

#### **OEShapeFitResults**

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEShapeFitResults

#### See also:

- OEFlexiOverlapResults class
- OEOverlapResults class

The OEShapeFitResults class defines the following public method:

- GetPose
- · GetScore

### **Constructor**

```
OEShapeFitResults();
OEShapeFitResults(const OEShapeFitResults&)
```

Default and copy constructors.

#### operator=

OEShapeFitResults & operator=(const OEShapeFitResults&)

### **GetPose**

```
const OEChem:: OEMolBase& GetPose() const;
```

Returns the flexibly optimized pose.

### **GetScore**

double GetScore() const

Returns the estimated probability of accuracy of the generated pose to the bound ligand.

# **5.3 Depricated OEDocking API**

## 5.3.1 OEDocking Classes (Deprecated)

### **OEAlignReceptorFunction**

class OEAlignReceptorFunction

OEAlignReceptorFunction is a pure virtual class that defines an API for aligning two receptors.

This pure virtual class is intended to be subclassed in order to create an aligned receptor. This is necessary because the receptor has multiple components that need to be aligned properly, such as the inner and outer contours and any bound or extra molecules attached to the receptor.

### **SetupTarget**

```
virtual SetupTarget (const OEChem:: OEMolBase & target) = 0;
```

Called when setting the target molecule.

### operator()

```
virtual OESystem:: OEIterBase<const OEChem:: OETrans> *
  operator () (const OEChem:: OEMolBase&receptor_to_align) const = 0;
```

Implement to return the transformations that take receptor\_to\_align into the targets reference frame.

## **CreateCopy**

**virtual** OEAlignReceptorFunction \* CreateCopy() const = 0;

Must return a fully instantiated OEAlignReceptor.

### **OEBoxBase**

#### class OEBoxBase

OEBoxBase class represents a box aligned to the x, y and z coordinate axis.

This pure virtual class is implemented by OEBox.

The following free functions take OEBoxBase.

| OEBoxXMid         | OEBoxXDim      |
|-------------------|----------------|
| OEBoxYMid         | OEBoxYDim      |
| OEBoxZMid         | OEBoxZDim      |
| OEInBox           | OEBoxTranslate |
| OEBoxExtend       | OESetupBox     |
| OEBoxVolume       | OEBoxArea      |
| OEMakeBoxMolecule |                |

#### operator=

```
OEBoxBase& operator=(const OEBoxBase& rhs)
```

Assignment operator to another OEBoxBase

#### **Destructor**

```
virtual ~\sim OEBoxBase() {}
```

Destructor

## **GetXMax**

virtual float GetXMax() const  $= 0$ 

Returns the maximum X value of the box

## **GetYMax**

```
virtual float GetYMax() const
                               = 0
```

Returns the maximum Y value of the box

### **GetZMax**

virtual float GetZMax() const  $= 0$ 

Returns the maximum Z value of the box

#### **GetXMin**

virtual float GetXMin() const  $= 0$ 

Returns the minimum X value of the box

#### **GetYMin**

virtual float GetYMin() const  $=\;\;0$ 

Returns the minimum Y value of the box

### **GetZMin**

virtual float GetZMin() const  $= 0$ 

Returns the minimum z value of the box

### **Setup**

```
virtual bool Setup (float x1,
                   float y1,
                   float z1,
                   float x2,
                   float y2,
                   float z2)= 0
```

Sets up the box. The max and min X values are the max and min of  $xI$ ,  $x2$  respectively. Minimum and maximum values of Y and Z are selected in an analogous fashion.

## **OEBox**

class OEBox : public OEBoxBase

 $OEBox$  class represents a box aligned to the x, y and z coordinate axis.

This class is an implementation of the OEBoxBase class.

The following free functions can take OEBox objects by virtue of their inheritance from OEBoxBase.

| OEBoxXMid         | OEBoxXDim      |
|-------------------|----------------|
| OEBoxYMid         | OEBoxYDim      |
| OEBoxZMid         | OEBoxZDim      |
| OEInBox           | OEBoxTranslate |
| OEBoxExtend       | OESetupBox     |
| OEBoxVolume       | OEBoxArea      |
| OEMakeBoxMolecule |                |

#### **Constructors**

OEBox()

Default constructor. All xyz min and max values are set to 0.

OEBox (float x1, float y1, float z1, float  $x2$ , float  $y2$ ,  $float z2)$ 

Constructor that sets up the box. The max and min X values will be set to the max and min of  $x1$ ,  $x2$  respectively. Minimum and maximum values of Y and Z are selected in an analogous fashion.

OEBox (const OEChem:: OEMolBase& mol, float addbox =  $0.0f$ )

Constructs a box around the given molecule. The maximum and minimum x, y and z values are set to the maximum and minimum values x, y and z coordinates of any atom of the molecule.

If addbox is specified then each edge of the box is extended by addbox.

OEBox (const OEChem:: OEMCMolBase& mol, float addbox =  $0.0f$ )

Constructs a box around the given molecule. The maximum and minimum x, y and z values are set to the maximum and minimum values x, y and z coordinates of any atom of any pose of the molecule.

If addbox is specified then each edge of the box is extended by addbox.

OEBox (const OEBox& box)

Copy constructor.

OEBox (const OEBoxBase& box)

Constructs an *OEBox* from an *OEBoxBase*.

### operator=

OEBox& operator=(const OEBox& rhs)

Assignment operator

OEBox& operator=(const OEBoxBase& rhs)

Assignment operator for OEBoxBase.

## **GetXMax**

float GetXMax() const

Returns the maximum X value of the box

#### **GetYMax**

float GetYMax() const

Returns the maximum Y value of the box

### **GetZMax**

float GetZMax() const

Returns the maximum Z value of the box

## **GetXMin**

float GetXMin() const

Returns the minimum X value of the box

## **GetYMin**

float GetYMin() const

Returns the minimum Y value of the box

## **GetZMin**

float GetZMin() const

Returns the minimum Z value of the box

#### **Setup**

```
bool Setup (float x1,
           float y1,
           float z1,
           float x2,
           float y2,
           float z2)
```

Sets up the box. The max and min X values are the max and min of  $x1$ ,  $x2$  respectively. Minimum and maximum values of Y and Z are selected in an analogous fashion.

### **OECustomConstraints**

```
class OECustomConstraints
```

OECustomConstraints holds a set of custom docking constraints used by OEDock. Each custom constraint is defined by an OEFeature contained by this class.

To use the constraints specified by an OECustomConstraints object the object must be passed to the receptor with OEReceptorSetCustomConstraints prior to calling the OEDock. Initialize method of OEDock.

#### **Constructors**

OECustomConstraints()

Default constructor. Object contains no features in the default constructed state.

 $OECustomerConstraints$  (constraints (const OECustomConstraints&)

Copy Constructor.

#### operator=

 ${\tt OECustomConstraints\&\ operator= (const\; OECustomConstraints\&)}$ 

Assignment operator.

### **GetFeatures**

```
OESystem:: OEIterBase<
                           OEFeature>* GetFeatures (bool enabledOnly = true)
OESystem::OEIterBase<const OEFeature>* GetFeatures(bool enabledOnly = true) const
```

Returns an iterator over all features contained by this class, or all enabled features if *enabledOnly* is true (see OEFeature. GetEnabled method).

#### **AddFeature**

```
OEFeature* AddFeature()
```

Adds a new OEFeature object to this class and returns a pointer to the newly created OEFeature. The returned OEFeature object is owned by this class, and will be destroyed by the destructor of this class.

#### **DeleteFeature**

**bool** DeleteFeature (const OEFeature\* feature)

Deletes an OEFeature owned by this class. Note that after this method is called feature will no longer point to a valid OEFeature object.

#### **NumFeatures**

unsigned int NumFeatures (bool enabledOnly = true) const

Returns the number of *OEFeature* objects contained by this class.

If enabled Only is true then only OEFeature objects for which the method OEFeature. GetEnabled returns true will be counted.

#### **Clear**

bool Clear()

Returns this object to its default constructed state, deleting any OEFeature objects it may currently be holding.

#### **OEFeature**

class OEFeature

OEFeature is a pure virtual class that defines a single custom docking constraint used by OEDock.

OEFeature objects are created by the OECustomConstraints class (see OECustomConstraints. AddFeature).

To satisfy a docking constraint a pose must either have:

1. At least one atom that matches one of the SMARTS patterns returned by OEFeature. Get Smarts and falls within one of the spheres returned by OEFeature. GetSpheres.

2. At least one heavy atom that falls within one of the spheres returned by  $OEFeature$ . Get Spheres, if the OEFeature has no SMARTS patterns.

### operator=

OEFeature& operator=(const OEFeature&)

Assignment operator.

### **Destructor**

 $virtual \sim$ OEFeature() {}

Destructor.

#### **GetSpheres**

```
virtual OESystem:: OEIterBase<const OESphereBase>* GetSpheres() = 0
virtual OESystem:: OEIterBase<
                                   OESphereBase>* GetSpheres() = 0
```

Returns all spheres associated with this custom constraint feature.

#### **AddSphere**

```
virtual OESphereBase* AddSphere() = 0virtual OESphereBase* AddSphere(const OESphereBase& sph) = 0
```

Adds an OESphereBase object to this class. If sph is passed the created sphere will be a copy of sph otherwise a default constructed sphere will be created.

Note that the returned memory is owned by this class and will be destroyed by the destructor of this class.

#### **DeleteSphere**

**virtual bool** DeleteSphere(const OESphereBase\* sph) =  $0$ 

Deletes a OESphereBase held by this class. Note that after this call sph will no longer point to a valid OESphereBase object.

#### **NumSpheres**

```
virtual unsigned int NumSpheres() const = 0
```

Returns the number of spheres held by this object.

### **ClearSpheres**

**virtual bool** ClearSpheres() =  $0$ 

Returns this object to its default constructed state. Deleting all spheres and SMARTS patterns it currently holds.

#### **GetSmarts**

```
virtual OESystem:: OEIterBase<const std:: string>* GetSmarts() const = 0
virtual OESystem:: OEIterBase<
                                   std::string>* GetSmarts()
                                                                     = 0
```

Returns an iterator over all SMARTS patterns associated with this OEFeature.

#### **AddSmarts**

**virtual bool** AddSmarts (std::string smarts) = 0

Adds a SMARTS pattern to this OEFeature.

#### **DeleteSmarts**

**virtual bool** DeleteSmarts (std:: string smarts) =  $0$ 

Deletes the specified SMARTS pattern from this OEFeature.

### **NumSmarts**

**virtual unsigned int** NumSmarts() const =  $0$ 

Returns the number of SMARTS patterns held by this OEFeature.

#### **ClearSmarts**

**virtual bool** ClearSmarts() =  $0$ 

Deletes all SMARTS patterns associated with this OEFeature.

## **SetFeatureName**

```
virtual void SetFeatureName (std::string) = 0
```

Sets the name of this feature.

## **GetFeatureName**

**virtual** std:: string GetFeatureName() const =  $0$ 

Returns the name of the feature.

#### **SetEnabled**

**virtual void** SetEnabled ( $bool$  enabled) =  $0$ 

Sets whether this feature is enabled or not. If the feature is disabled the constraint will be ignored during the docking process.

### **GetEnabled**

**virtual bool** GetEnabled() const =  $0$ 

Returns whether this feature is enabled. If this function returns false this constraint will be ignored during the docking process.

#### **CreateCopy**

**virtual** OEFeature\* CreateCopy() const =  $0$ 

Creates a copy of this OEFeature. Note that the memory returned by this function is not owned by this class, and is the responsibility of the calling function.

### **OEProteinConstraint**

class OEProteinConstraint

This class holds information about a single receptor protein constraint.

## **GetAtom**

```
OEChem:: OEAtomBase* GetAtom() const
```

Hold the protein atom of the receptor the constraint is associated with.

### **GetType**

unsigned int GetType() const

Type for the constraint (see OEProteinConstraintType).

#### **GetEnabled**

bool GetEnabled() const

Returns true if the constraint is enabled and false otherwise.

#### **GetName**

std::string GetName() const

Returns the name of the constraint.

### **SetAtom**

void SetAtom (OEChem:: OEAtomBase\* atom)

Sets the atom of the receptor the constraint will be associated with.

### **SetType**

void SetType (unsigned int type)

Sets the constraint type (see OEProteinConstraintType).

#### **SetName**

void SetEnabled (bool enabled)

Sets the name of the constraint.

## **SetEnabled**

void SetName (std::string name)

Sets the enabled flag of the constraint.

### **OESphereBase**

OESphereBase class represents a sphere.

The following free functions take OESphereBase.

| OESphereVolume | OESphereArea |
|----------------|--------------|
| OEInSphere     |              |

#### **Destructor**

 $virtual \sim$ OESphereBase() {}

Destructor.

#### operator=

OESphereBase& operator=(const OESphereBase& rhs)

Assignment operator.

#### **GetX**

virtual float GetX() const  $= 0$ 

Returns the X coordinate of the center of the sphere

#### **GetY**

**virtual float**  $GetY() const = 0$ 

Returns the Y coordinate of the center of the sphere

## GetZ

virtual float GetZ() const  $= 0$ 

Return the Z coordinate of the center of the sphere

## **GetRad**

virtual float GetRad() const  $= 0$ 

Returns the radius of the sphere

#### **SetRad**

virtual bool SetRad(float rad)  $= 0$ 

Sets the radius of the sphere to *rad*. Will fail and return false if  $rad < 0$ .

### **SetCenter**

```
virtual bool SetCenter (float x,
                       float y,
                       float z)= 0
```

Sets the center of the sphere.

## 5.3.2 OEDocking Functions (Deprecated)

#### **OEAlignReceptors**

```
OESystem:: OEIterBase<const OEChem:: OEMolBase> *OEAlignReceptors (
                  const OEChem:: OEMolBase &target_receptor,
                  const OEChem:: OEMolBase & receptor_to_align) ;
```

Given two receptors (a target and a receptor to align) return an iterator of aligned receptors. In general, on success, the iterator will only contain one aligned receptor and will be empty on failure.

```
OESystem::OEIterBase<const OEChem::OEMolBase> *OEAlignReceptors (
                  const OEChem:: OEMolBase &target_receptor,
                  const OEChem:: OEMolBase & receptor_to_align
                  const OEAlignReceptorFunction &);
```

Align two receptors using the supplied OEAlignReceptorFunction.

## **OEBoxArea**

float OEBoxArea (const OEBoxBase& box)

Return the area of the box.

#### **OEBoxExtend**

bool OEBoxExtend (OEBoxBase& box, float x\_ext, float y\_ext, float z\_ext)

Extends each side of the box by the specified amount.  $x$ <sub>\_ext</sub> extends the two faces of the box normal to the x-axis. Thus the x dimension of the box will increase by 2 times  $x$ \_ext. The  $y$ \_ext and  $z$ \_ext perform the same function for the y and z faces respectively.

bool OEBoxExtend (OEBoxBase& box, float ext)

Extends every face of box by ext. Thus every dimension of the box will increase by 2 times ext.

## **OEBoxTranslate**

bool OEBoxTranslate (OEBoxBase& box, float x\_trans, float y\_trans, float z\_trans)

Translates box a distance specified by  $(x\_trans, y\_trans, z\_trans)$ 

#### **OEBoxVolume**

float OEBoxVolume (const OEBoxBase& box)

Return the volume of the box

## **OEBoxXDim**

float OEBoxXDim(const OEBoxBase& box)

Returns the X dimension of the box.

#### **OEBoxXMid**

float OEBoxXMid(const OEBoxBase& box)

Returns the X midpoint of the box.

## **OEBoxYDim**

float OEBoxYDim(const OEBoxBase& box)

Returns the Y dimension of the box.

#### **OEBoxYMid**

float OEBoxYMid(const OEBoxBase& box)

Returns the Y midpoint of the box.

## **OEBoxZDim**

float OEBoxZDim(const OEBoxBase& box)

Returns the Z dimension of the box.

#### **OEBoxZMid**

float OEBoxZMid(const OEBoxBase& box)

Returns the Z midpoint of the box.

#### **OEInBox**

bool OEInBox (const OEBoxBase& box, float x, float y, float z)

Returns true if  $(x, y, z)$  is within *box*.

Coordinates that lie on an edge of box are considered to be in box.

## **OEInSphere**

float OEInSphere(const OESphereBase& sph, float x, float y, float z)

Returns true if  $(x, y, z)$  is within the sphere sph.

Coordinates that lie on an edge of sph are considered to be in sph.

#### **OEIsReceptor**

bool OEIsReceptor (const OEChem:: OEMolBase& receptor)

Returns true if rec is a receptor.

#### **OEMakeReceptorDeprecated**

Warning: This is a deprecated API. The overloads below are deprecated. Please use OEMakeReceptor instead.

```
bool OEMakeReceptor (OEChem:: OEMolBase& receptor,
                    const OEChem:: OEMolBase& proteinStructure,
                    const OEBoxBase& box,
                    bool stripWater = true,
                    const unsigned int negImgType = OENegativeImageType::Default)
```

Creates a *receptor* object using a *box* and the protein structure.

*receptor*: The created receptor.

*proteinStructure:* Structure of a target protein.

- **box:** An OEBoxBase enclosing the active site on the *proteinStructure*. The box should enclose all possible docked ligand positions (heavy atoms of the docked pose must fit within the box). It is not necessary to enclose the protein residues the docked ligand may interact with.
- strip Water: If this flag is true water molecules present in *proteinStructure* will be stripped from the protein structure of the *receptor* and added to the extra molecules information of the *receptor*.
- **negImgType:** Specifies the type of negative image to create (see OENegativeImageType namespace).

This function returns true if successful.

```
bool OEMakeReceptor (OEChem:: OEMolBase& receptor,
                    const OEChem:: OEMolBase& proteinStructure,
                    const OEChem:: OEMolBase& boundLigand,
                    bool stripWater = true,
                    unsigned int negImgType = OENegativeImageType::Default)
```

Creates a *receptor* object using a *boundLigand* and the protein structure.

*receptor*: The created receptor.

*proteinStructure*: Structure of a target protein.

**boundLigand:** The structure of a ligand bound to the active site.

- strip Water: If this flag is true water molecules present in *proteinStructure* will be stripped from the protein structure of the *receptor* and added to the extra molecules information of the *receptor*.
- **negImgType:** Specifies the type of negative image to create (see OENegativeImageType namespace).

This function returns true if successful.

```
bool OEMakeReceptor (OEChem:: OEMolBase& receptor,
                     const OEChem:: OEMolBase& proteinStructure,
                     const OEChem:: OEAtomBase& hint,
                    bool stripWater = true,
                     unsigned int negImgType = OENegativeImageType::Default)
```

Creates a *receptor* object using the protein structure and the identity of one atom of the protein structure near the active site.

*receptor*: The created receptor.

*proteinStructure:* Structure of a target protein.

hint: An atom of *proteinStructure* that is near the binding site.

strip Water: If this flag is true water molecules present in *proteinStructure* will be stripped from the protein structure of the *receptor* and added to the extra molecules information of the *receptor*.

**negImgType:** Specifies the type of negative image to create (see  $OENeqativeImageType$  namespace).

This function returns true if successful.

```
bool OEMakeReceptor (OEChem:: OEMolBase& receptor,
                    const OEChem:: OEMolBase& proteinStructure,
                    float hintX,
                    float hinty,
                    float hintZ,
                    bool stripWater = true,
                    unsigned int negImgType = OENegativeImageType::Default)
```

Creates a *receptor* object using the protein structure and a coordinate near the active site.

*receptor*: The created receptor.

*proteinStructure*: Structure of a target protein.

hintX hintY hintZ: Coordinate near the binding site of proteinStructure.

- strip Water: If this flag is true water molecules present in *proteinStructure* will be stripped from the protein structure of the *receptor* and added to the extra molecules information of the *receptor*.
- **negImgType:** Specifies the type of negative image to create (see  $OENeqativeImageType$  namespace).

**Attention:** The below API using an OEDesignUnit is currently available in C++ and Python.

```
bool OEMakeReceptor (OEChem:: OEMolBase& receptor,
                    const OEBio:: OEDesignUnit& designUnit,
                    bool stripWater = true,
                    unsigned int negImqType = OENegativeImageType::Default)
```

Creates a *receptor* object using a *designunit*, where the binding site has already been defined

receptor: The created receptor.

*designUnit*: The designunit.

- strip Water: If this flag is true water molecules present in *designunit* will be stripped from the structure of the receptor and added to the extra molecules information of the receptor.
- **negImgType:** Specifies the type of negative image to create (see OENegativeImageType namespace).

This function returns true if successful.

#### **OENegativelmageTypeConfigure**

bool OENegativeImageTypeConfigure(OESystem::OEInterface& itf, std::string flagName)

This function is used in conjunction with the *OENegativeImageTypeGetValue*. It adds a command line flag to the *itf* to specify a negative image type to use. Once the command line has been parsed (OEParseCommandLine) the itf and flagName are passed to OENegativeImageTypeGetValue that will return the constant from the OENegative Image Type namespace associated with the negative image type the user selected (or the default scoring function if the user didn't specify one).

Note: The parameter added to *itf* will be of type string, name *flagName*, and have legal values associated with the negative image type.

#### **OEReadReceptorFile**

bool OEReadReceptorFile(OEChem:: OEMolBase& receptor, std:: string filename)

Reads a receptor from file *filename* into *receptor*.

Returns true if successful.

Note: All receptor files must be in either .oeb or .oeb.gz format.

#### **OEReadReceptorFromBytes**

```
OEReadReceptorFromBytes(OEMolBase, format, data) -> bool
OEReadReceptorFromBytes (OEMolBase, format, flavor, gzip, data) -> bool
OEReadReceptorFromBytes(OEMCMolBase, format, data) -> bool
OEReadReceptorFromBytes (OEMCMolBase, format, flavor, gzip, data) -> bool
```

Instantiates a receptor from the contents of 'data' in terms of 'format'. 'format' must be a file extension that is readable by OpenEye, for example: ".oeb.gz". Overloads which take an unsigned 'format', unsigned 'flavor' and Boolean 'gzip' parameters expect the format and corresponding flavor to be specified by one of the constants in OEFormat and OEIFlavor.

Returns 'true' if decoding was successful and the decoded molecule is identified as a receptor.

```
bytes = oedocking. OEWriteReceptorToBytes(".oeb", receptor)
receptorIO = oechem. OEGraphMol()status = oedocking.OEReadReceptorFromBytes(receptorIO, ".oeb", bytes)
```

```
bytes = oedocking. OEWriteReceptorToBytes(".oeb.gz", receptor)
receptorIO = oechem.OEGraphMol()
status = oedocking. OEReadReceptorFromBytes (receptorIO, ".oeb.gz", bytes)
```

#### $qzip = False$ bytes = oedocking.OEWriteReceptorToBytes(oechem.OEFormat OEB, oechem.OEGetDefaultOFlavor(oechem.OEFormat $\rightarrow$ OEB),

```
gzip, receptor)
receptorIO = occhem.OEGraphMol()status = oedocking.OEReadReceptorFromBytes(receptorIO, oechem.OEFormat_OEB,
                                              oechem.OEGetDefaultIFlavor(oechem.OEFormat_
\leftrightarrowOEB),
                                              gzip, bytes)
qzip = Truebytes = oedocking.OEWriteReceptorToBytes(oechem.OEFormat.OEB,oechem.OEGetDefaultOFlavor(oechem.OEFormat_
\rightarrow OEB).
                                            gzip, receptor)
receptorIO = oechem.OEGraphMol()
status = oedocking.OEReadReceptorFromBytes(receptorIO, oechem.OEFormat_OEB,
                                              oechem.OEGetDefaultIFlavor(oechem.OEFormat_
\leftrightarrowOEB).
                                              gzip, bytes)
```

## **OEReceptorAddCachedScore**

bool OEReceptorAddCachedScore(OEChem:: OEMolBase& rec, OEScore& score)

Equivalent to calling OEScore. CacheScoringSetup with clearOldData false.

bool OEReceptorAddCachedScore(OEChem::OEMolBase& rec, OEDock& dock)

Equivalent to calling OEDock. CacheScoringSetup with clearOldData false.

### **OEReceptorAddExtraMol**

```
bool OEReceptorAddExtraMol(OEChem::OEMolBase& receptor,
                           const OEChem:: OEMolBase& extraMol)
```

Adds a copy of extraMol to receptor's extra molecules.

Returns true if successful.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISRecept \, or$  returns true).

#### **OEReceptorClear**

bool OEReceptorClear (OEChem:: OEMolBase& receptor)

Clears all receptor information from *receptor*, except the structure of the protein.

## **OEReceptorClearBoundLigand**

bool OEReceptorClearBoundLigand(OEChem:: OEMolBase& receptor)

Clears any bound ligand from *receptor*.

Returns true if successful.

### **OEReceptorClearCachedScore**

bool OEReceptorClearCachedScore (const OEChem:: OEMolBase& rec)

Clears all score setup caches, from OEScore or OEDock objects, from the receptor.

#### **OEReceptorClearCustomConstraints**

bool OEReceptorClearCustomConstraints (OEChem:: OEMolBase& receptor)

Clears all custom constraints on a receptor.

Returns true if successful.

## **OEReceptorClearExtraMols**

bool OEReceptorClearExtraMols (OEChem:: OEMolBase& receptor)

Clears all extra molecules from receptor.

Returns true if successful.

#### **OEReceptorClearProteinConstraint**

bool OEReceptorClearProteinConstraints (OEChem:: OEMolBase& receptor, const OEProteinConstraint& constraint)

Clears a given protein constraint from receptor.

### **OEReceptorClearProteinConstraints**

bool OEReceptorClearProteinConstraints (OEChem:: OEMolBase& receptor)

Clears all protein constraints from receptor.

## **OEReceptorGetBoundLigand**

OEChem:: OEMolBase& OEReceptorGetBoundLigand(const OEChem:: OEMolBase& receptor)

Returns a copy of the *receptor's* bound ligand.

If the receptor does not have a bound ligand then an empty molecule will be returned

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISREceptor$  returns true).

### **OEReceptorGetCustomConstraints**

bool OEReceptorGetCustomConstraints (const OEChem:: OEMolBase& receptor, OECustomConstraintsBase& customConstraints)

Returns a copy of the *receptor's* custom constraints

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISREceptor$  returns true).

## **OEReceptorGetExtraMols**

OEIterBase<const OEMolBase>\* OEReceptorGetExtraMols(const OEChem::OEMolBase& receptor)

Returns an iterator over the extra molecules held by receptor.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISRecept \, or$  returns true).

### **OEReceptorGetInnerContourLevel**

float OEReceptorGetInnerContourLevel(const OEChem:: OEMolBase& receptor, float& level)

Returns the inner contour level of the receptor.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISReceptor$  returns true).

### **OEReceptorGetNegativeImageGrid**

```
OESystem::OEGrid<float> OEReceptorGetNegativeImageGrid(const OEChem::OEMolBase&
\rightarrowreceptor)
```

Returns a copy of the *receptor*'s negative image grid.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISRECEPTOT$  returns true).

### OEReceptorGetOuterContourLevel

float OEReceptorGetOuterContourLevel(const OEChem:: OEMolBase& receptor)

Returns the outer contour level of the receptor.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISReceptor$  returns true).

#### **OEReceptorGetProteinConstraints**

```
OEIterBase<OEProteinConstraint>*
OEReceptorGetProteinConstraint (const OEChem:: OEMolBase& receptor,
                               bool enabled Only = true)
```

Returns an iterator over the *receptor's* protein constraints. If *enabledOnly* is true then only enabled constraints will be returned.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISREceptor$  returns true).

### **OEReceptorHasBoundLigand**

bool OEReceptorHasBoundLigand (const OEChem:: OEMolBase& receptor)

Returns true if *receptor* is a valid receptor and has a bound ligand.

#### **OEReceptorHasCachedScore**

bool OEReceptorHasCachedScore (const OEChem:: OEMolBase& rec)

Returns true if rec has a score setup cache for any OEScore or OEDock object.

#### **OEReceptorHasCustomConstraints**

```
bool OEReceptorHasCustomConstraints (const OEChem:: OEMolBase& receptor,
                                     bool enabled Only = true)
```

Returns true if receptor has custom constraints. If enabledOnly is true then at least one of the constraints must be enabled.

#### **OEReceptorHasExtraMols**

bool OEReceptorHasExtraMols(const OEChem:: OEMolBase& receptor)

Returns true if the *receptor* is a valid receptor and has one or more extra molecules.

#### **OEReceptorHasInnerContourLevel**

bool OEReceptorHasInnerContourLevel(const OEChem:: OEMolBase& receptor)

Returns true if the *receptor* has an inner contour level set.

Note: This function will return true even if the inner contour is disabled  $(i.e.$  even if the level is negative).

#### OEReceptorHasNegativeImageGrid

bool OEReceptorHasNegativeImageGrid(const OEChem:: OEMolBase& receptor)

Returns true if the *receptor* has a negative image grid.

## OEReceptorHasOuterContourLevel

bool OEReceptorHasOuterContourLevel(const OEChem:: OEMolBase& receptor)

Returns true if the *receptor* has an outer contour level set.

**Note:** This function will return true even if the outer contour is disabled  $(i.e.$  even if the level is negative).

#### **OEReceptorHasProteinConstraints**

```
bool OEReceptorHasProteinConstraints (const OEChem:: OEMolBase& receptor,
                                      bool enabled Only = true)
```

Returns true if *receptor* is a valid receptor and has one or more protein constraints. If *enabledOnly* the constraint(s) must also be enabled.

#### **OEReceptorSetBoundLigand**

bool OEReceptorSetBoundLigand(OEChem:: OEMolBase& receptor, const OEChem:: OEMolBase& boundLigand)

Sets the bound ligand on *receptor* to be a copy of *boundLigand*.

Returns true if successful.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISReceptor$  returns true).

### **OEReceptorSetCachedScore**

bool OEReceptorSetCachedScore(OEChem:: OEMolBase& rec, OEScore& score)

Equivalent to calling OEScore. CacheScoringSetup with clearOldData true.

bool OEReceptorSetCachedScore(OEChem::OEMolBase& rec, OEDock& dock)

Equivalent to calling OEDock. CacheScoringSetup with clearOldData true.

#### **OEReceptorSetCustomConstraints**

```
bool OEReceptorSetCustomConstraints (OEChem:: OEMolBase& receptor,
                                     const OECustomConstraintsBase& customConstraints)
```

Sets the receptor's custom constraints (copied from customConstraints).

Returns true if successful.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISReceptor$  returns true).

### **OEReceptorSetInnerContourLevel**

bool OEReceptorSetInnerContourLevel(OEChem:: OEMolBase& receptor, float level)

Sets the inner contour *level* on the *receptor*.

Returns true if successful

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISReceptor$  returns true).

#### OEReceptorSetOuterContourLevel

bool OEReceptorSetOuterContourLevel(OEChem:: OEMolBase& receptor, float level)

Sets the outer contour *level* on the *receptor*.

Returns true if successful.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISReceptor$  returns true).

#### **OEReceptorSetProteinConstraint**

```
bool OEReceptorSetProteinConstraint (OEChem:: OEMolBase& receptor,
                                     OEProteinConstraint& proteinConstraint)
```

Sets a protein constraint. If the receptor already has a constraint on OEProteinConstraint. GetAtom the constraint will be replaced, otherwise a new one will be created.

Returns true if successful.

It is only valid to call this function if *receptor* is a valid receptor (i.e.,  $OEISREceptor$  returns true).

## **OEScoreTypeConfigure**

bool OEScoreTypeConfigure(OESystem::OEInterface& itf, std::string flagName)

This function is used in conjunction with the OEScoreTypeGetValue. It adds a command line flag to the itf to specify a scoring function to use. Once the command line has been parsed (OEParseCommandLine) the *itf* and flagName are passed to OEScoreTypeGetValue that will return the constant from this namespace associated with the scoring function the user selected (or the default scoring function if the user didn't specify one).

Note: The parameter added to *itf* will be of type string, name *flagName*, and have legal values associated with the scoring functions.

#### **OESearchResolutionConfigure**

bool OESearchResolutionConfigure (OESystem:: OEInterface& itf, std:: string flagName)

This function is used in conjunction with the OESearchResolutionGetValue. It adds a command line flag to the *itf* to specify a dock resolution to use. Once the command line has been parsed (OEParseCommandLine) the *itf* and *flagName* are passed to OESearchResolutionGetValue that will return the constant from the OESearchResolution namespace associated with the dock resolution the user selected (or the default scoring function if the user didn't specify one).

Note: The parameter added to *itf* will be of type string, name *flagName*, and have legal values associated with the dock resolutions.

#### **OESetupBox**

**bool** OESetupBox (OEBoxBase& box, float\* xyz, unsigned int N, bool addbox =  $0.0f$ )

Sets up box to contain the minimum size box that encloses all coordinates in the xyz array and then extends each box face by addbox.

box Box to setup

- $xyz$  Array of coordinates
- N Number of coordinates in  $xyz$  array
- addbox Optional parameter to extend each box face by a specified amount relative to the minimum box enclosing the xyz coordinates.

Returns true if setup was successful.

**bool** OESetupBox (OEBoxBase& box, const OEChem:: OEMolBase& mol, float addbox =  $0.0f$ )

Sets up *box* to be the minimum size box that encloses *mol* and then extends each box face by *addbox*.

**box** Box to setup

*mol* A molecule the box will be setup around

addbox Optional parameter to extend each box face by a specified amount relative to the minimum box enclosing the *mol*.

Returns true if setup was successful.

**bool** OESetupBox (OEBoxBase& box, const OEChem::OEMCMolBase& mol, float addbox =  $0.0f$ )

Sets up box to be the minimum size box that encloses all conformers of *mol* and then extends each box face by *addbox*.

**box** Box to setup

*mol* A multiconformer molecule the box will be setup around

addbox Optional parameter to extend each box face by a specified amount relative to the minimum box enclosing the *mol*.

Returns true if setup was successful.

#### **OESetupBoxCenterAndExtents**

bool OESetupBoxCenterAndExtents (OEBoxBase& box, float\* center, float\* extents)

Sets up *box* using a center coordinate and the dimension of the box.

**box** Box to setup

center A length 3 array holds the coordinate of the box center

extends A length 3 array holding the x, y and z dimensions of the box.

Returns true if setup was successful.

#### **OESphereArea**

float OESphereArea (const OESphereBase& sph)

#### **OESphereVolume**

float OESphereVolume (const OESphereBase& sph)

#### **OEWriteReceptorFile**

bool OEWriteReceptorFile(const OEChem::OEMolBase& receptor, std::string filename) bool OEWriteReceptorFile(OEChem::OEMolBase& receptor, std::string filename)

Writes a receptor to file filename

Returns true if successful.

Note: All receptor files must be in either .oeb or .oeb.gz format.

## **OEWriteReceptorToBytes**

```
OEWriteReceptorToBytes(format, oemol) -> bytes
OEWriteReceptorToBytes(format, flavor, gzip, oemol) -> bytes
```

Encodes a receptor in terms of 'format'. 'format' must be a file extension that is writeable by OpenEye, for example: ".oeb.gz". Overloads which take an unsigned 'format', unsigned 'flavor' and Boolean 'gzip' parameters expect the format and flavor to be specified by one of the constants in OEFormat and OEOFlavor.

Returns bytes if the molecule to encode is identified as a receptor and encoding was successful, otherwise, "None".

```
bytes = oedocking.OEWriteReceptorToBytes(".oeb", receptor)
receptorIO = oechem. OEGraphMol()status = oedocking.OEReadReceptorFromBytes(receptorIO, ".oeb", bytes)
```

```
bytes = oedocking. OEWriteReceptorToBytes(".oeb.gz", receptor)
receptorIO = occhem.OEGraphMol()status = oedocking. OEReadReceptorFromBytes (receptorIO, ".oeb.gz", bytes)
```

```
gzip = Falsebytes = oedocking.OEWriteReceptorToBytes(oechem.OEFormat_OEB,oechem.OEGetDefaultOFlavor(oechem.OEFormat
\rightarrow OEB),
                                            gzip, receptor)
receptorIO = occhem.OEGraphMol()status = oedocking.OEReadReceptorFromBytes(receptorIO, oechem.OEFormat_OEB,
                                              oechem.OEGetDefaultIFlavor(oechem.OEFormat_
\leftrightarrowOEB),
                                              gzip, bytes)
qzip = True
```

```
bytes = oedocking. OEWriteReceptorToBytes (oechem. OEFormat_OEB,
                                             oechem.OEGetDefaultOFlavor(oechem.OEFormat
\rightarrow OEB),
                                             qzip, receptor)
receptorIO = occhem.OEGraphMol()status = oedocking.OEReadReceptorFromBytes(receptorIO, oechem.OEFormat_OEB,
                                               oechem.OEGetDefaultIFlavor(oechem.OEFormat_
\leftrightarrowOEB),
                                               gzip, bytes)
```

# 5.4 OEModels API

## **5.4.1 Preliminary OEModels Classes**

### **OEROCSQueryModelBuilder**

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

#### class OEROCSQueryModelBuilder

The OEROCSQueryModelBuilder is used to build models of OEShapeQuery that can be used as reference systems for ROCS, OEROCS, OEOverlay, and other similar functions.

The OEROCSQueryModelBuilder can be used for building a query from known ligands in their binding modes. The input ligands should be prepared by aligning the protein crystal structures. The prepared OEDesignUnit structures can be used directly, or the ligands can be extracted and used, as input to the query model builder. The query model builder constructs a ROCS query employing a few of the ligands that are most representative of the set as a whole.

#### The OEROCSQueryModelBuilder class defines the following public methods:

- · AddLigand
- $\bullet$  Build
- · ClearLigands
- GetROCSQueryModelOptions
- · SetLigands

#### **Constructor**

```
OEROCSOueryModelBuilder();
OEROCSQueryModelBuilder(const OEROCSQueryModelOptions& options);
OEROCSQueryModelBuilder (const OEROCSQueryModelBuilder&)
```

Default and copy constructors.

#### operator=

OEROCSQueryModelBuilder & operator=(const OEROCSQueryModelBuilder &)

### **AddLigand**

```
bool AddLigand (const OEBio:: OEDesignUnit& du) ;
bool AddLigand (const OEChem:: OEMolBase& mol) ;
```

Adds the specified ligand to the set of ligands from which the query model(s) would be build. The first overload of the method adds the bound ligand from the design unit. Method returns True if a ligand is added sccessfully.

#### **Build**

```
OESystem:: OEIterBase<OEShape:: OEShapeQuery>* Build(OESystem:: OETracerBase* tracer = \&\rightarrow OESystem:: NullTracer)
```

Build the query model(s). Method returns an itertator over the generated OEShapeQuery.

## **ClearLigands**

```
bool ClearLigands();
```

Clears set of ligands from which the query model(s) would be build. Method returns True if all the ligands are removed successfully.

### **GetROCSQueryModelOptions**

const OEROCSQueryModelOptions& GetROCSQueryModelOptions() const;

Get the OEROCSQueryModelOptions associated with this builder.

### **SetLigands**

```
bool SetLigands (OEChem:: oemolistream& ifs);
bool SetLigands (OEPlatform:: oeistream& ifs);
```

Sets the ligands from which the query model(s) would be build. Calling this method would clear any existing ligand that were previously added. The first overload adds all the OEMolBase from the specified oemolistream, and the second overload adds the bound ligands from all the OEDesignUnit of the specified oeistream. Method returns True if ligand are added sccessfully.

### **OEROCSQueryModelOptions**

Attention: This is a preliminary API and may be improved based on user feedback. It is currently available in C++ and Python.

class OEROCSQueryModelOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for building a ROCS query model using OEROCSQuery-ModelBuilder.

The OEROCSOueryModelOptions class defines the following public methods:

- · GetColorForceField and SetColorForceField
- · GetMergeColorAtoms and SetMergeColorAtoms
- · GetMaxMoleculesPerModel and SetMaxMoleculesPerModel
- GetNumModels and SetNumModels

## **Constructor**

```
OEROCSQueryModelOptions();
OEROCSQueryModelOptions (const OEROCSQueryModelOptions &)
```

Default and copy constructors.

#### operator=

OEROCSQueryModelOptions & operator= (const OEROCSQueryModelOptions &)

## **GetColorForceField**

const OEColorForceField\* GetColorForceField() const

See Set ColorForceField method.

#### **GetMergeColorAtoms**

bool GetMergeColorAtoms() const

See SetMergeColorAtoms method.

#### **GetMaxMoleculesPerModel**

unsigned GetMaxMoleculesPerModel() const

See SetMaxMoleculesPerModel method.

## **GetNumModels**

unsigned GetNumModels() const

See SetNumModels method.

## **SetColorForceField**

```
bool SetColorForceField (unsigned int type)
bool SetColorForceField(OEPlatform::oeistream &is)
bool SetColorForceField(const std::string &filename)
bool SetColorForceField(const OEColorForceField &cff)
```

Sets the color force field to be used. By default the ImplicitMillsDean color force field is used.

## **SetMergeColorAtoms**

bool SetMergeColorAtoms (const bool)

Sets flag if color atoms should be merged if applicable. Default: True

## **SetMaxMoleculesPerModel**

bool SetMaxMoleculesPerModel (const unsigned)

Sets the maximum number of molecules to be combined in creating a single query. Default: 3

#### **SetNumModels**

bool SetNumModels (const unsigned)

Sets the maximum number query model to be returned from modeling building. Default: 1

## **SIX**

# **RELEASE HISTORY**

# 6.1 OEDocking TK 4.3.2

## 6.1.1 New features

- The method *Optimize* in *OEPoseOptimizer* now returns an unsigned code corresponding to any possible failure, instead of a bool. The method also takes additional arguments for protein and ligand masks in the OEDesignUnit.
- $\bullet$  The following methods have been added to the OESinglePoseResult:
  - GetRelaxAttempted
  - $GetRelaxStatus$
  - $GetRelaxStatusStr$
- A new method, MethodChoice, has been added to OEPosit that provides information on the method that would be used for the pose prediction of a given ligand against a given receptor.
- The new methods GetTorLib and SetTorLib have been added to OEPositOptions to provide a choice for the torsion library that would be used for conformer generation during pose prediction.
- The following methods have been added to the OEShapeFitOptions:
  - $-$  GetMaxLocalStrain
  - SetMaxLocalStrain
  - GetTorLib
  - $-$  SetTorLib

## 6.1.2 Major bug fixes

- The method *Optimize* in *OEPoseOptimizer* is now more robust in optimizing a docked pose. Accordingly, Docking with relaxation in OEPosit is also now more robust.
- The function OEHasClash now properly recognizes all clashes between a ligand and a protein that were previously mistaken because of some misidentification of covalent bonds.

## 6.1.3 Minor bug fixes

- Selection of the best receptor has been improved in  $OEPosit$ , ensuring that the correct receptor will always be picked in case of a self-docking.
- $\bullet$  The internal algorithm has been optimized to improve time requirements for *OEPosit* when working with many receptors and a few ligands.

# 6.2 OEDocking TK 4.3.1

- An issue has been fixed that would occasionally cause segmentation faults when OEPosit would internally fail to generate conformers.
- New methods, GetPoseRelaxOptions and SetPoseRelaxOptions, have been added to OEPositOptions to allow more flexibility in relaxing the OEPosit generated poses.
- Internal algorithms have been improved in  $OEShapeFit$  to improve strain in generated poses.

# 6.3 OEDocking TK 4.3.0

## 6.3.1 New features

- Flexible Posit now uses FF14SB-SAGE force field for the protein/ligand complex optimization.
- A new overload of SetupRef has been added that allows using OEShapeFit with a bound ligand as the reference.
- The following new methods have been added to enable internal conformation generation in  $OEShapeFitOptions$ :
  - SetFullConformationSearch
  - GetFullConformationSearch
- A new class, OEShapeFitOptions, has been added that allows estimating pose prediction confidence against different reference systems. This new class is complementary to the existing function OEGetEstimatedPosit-Probability.

## 6.3.2 Major bug fixes

- An issue has been fixed where relaxation failed in *OEPosit* when the pose relaxation mode was set to either ALL or CLASHED.
- An issue causing generation of bent ring structures and high strain poses when performing OEPosit has been fixed
- An issue has been fixed that caused flexible *OEPosit* with *ALL* relaxation mode to fail while generating nonclashing poses when *NONE* was successful.

## 6.3.3 Minor bug fixes

- An issue where  $Dock$  passed too many conformers for flexible optimization with relaxation in OEPosit has been fixed. Now, OEShapeFit no longer passes too many conformers for flexible optimization that could occasionally cause a less accurate conformer to become the top predicted pose.
- The *Dock* method with relaxation has been modified to be more aligned with other modes of failure when ligand charge assignments fail.

# 6.4 OEDocking TK 4.2.1

## 6.4.1 New features

• A new preliminary API class, OEShapeFitOptions, has been added to allow better control over option parameters for OEShapeFit. The constructor for the preliminary class OEShapeFit now takes OEShapeFitOptions as an argument instead of OEFlexiOverlayOptions. Also, SetFlexiOverlayOptions and GetFlexiOverlayOptions now accept and return OEShapeFitOptions.

## 6.4.2 Major bug fixes

- The *Dock* method in *OEPosit* now returns poses instead of a failure, if there is a failure during flexible optimization.
- An issue that caused intermittent crash for specific calculations on specific platforms when working with  $OE$ Posit has been fixed.
- OEPosit now accurately returns NoValidNonClashPoses as status when the predicted pose contains clashes based on the *defined clash allowed type*. Note that the clashed poses can still be retrieved from the resulting OESinglePoseResult if desired.

## 6.4.3 Minor bug fixes

• The RankDesignUnits method is now properly wrapped in python.

## **6.4.4 Documentation changes**

- Documentation has been added for the function OEGetEstimatedPositProbability, which works with OEDesignUnit.
- Documentation has been added for the function OESetupBox, which supports OEMolBase and OEMCMolBase.

# 6.5 OEDocking TK 4.2.0

## 6.5.1 New features

- Two new preliminary API classes, OEShapeFit and OEShapeFitResults have been added which provides functionality for pose generation based on flexible fitting with Shape/Color and Forcefield.
- The adiabatic optimization algorithm of  $\text{ShapeFit}$  method for pose generation in *OEPosit* has been replaced by a new simultaneous flexible fitting algorithm, as implemented in  $OEShapeFit$ . The new algorithm uses Sage as the default forcefield, instead of MMFF.
- Two new methods, SetFlexiOverlayOptions and GetFlexiOverlayOptions, have been added to OEPositOptions to expose parameters related to OEShapeFit in OEPosit.

## 6.5.2 Major bug fixes

• An issue that caused a segmentation fault when using *CacheScoringSetup* has been fixed.

## **6.5.3 Documentation changes**

• New C++ and Python examples have been added to the Flexible Overlay Optimization with OEShapeFit API section that demonstrate how to flexibly fit input multi-conformer molecules into a design unit that contains a bound ligand.

# 6.6 OEDocking TK 4.1.2

Spring 2022

• Minor internal improvements have been made.

# 6.7 OEDocking TK 4.1.1

Fall 2021

## 6.7.1 New features

- OEPosit can now generate poses using all the provided receptors. This can be controlled via a new method  $SetBestRecentorPoseOnly$ . The default behavior remains posing with the best receptor only.
- A new preliminary API class, OEROCSQueryModelBuilder, has been added that builds an OEShapeQuery from structure-based data, and can be used as a query to perform an OEOverlay or **ROCS** calculation.
- A new preliminary API class, OEROCSQueryModelOptions, has been added that provides choices for OEROC-SQueryModelBuilder calculations.

## 6.7.2 Minor bug fixes

• An issue with redundant SD data after docking a multi conformer molecule using the  $OEDock$ . DockMultiConformerMolecule method has been fixed.

## **6.7.3 Documentation changes**

- Two new examples have been added to the section, Using Multiple Receptors that handle multiple input receptors and generate single or multiple poses for each ligand.
- · Example PoseMolsMultiReceptor has removed.

# 6.8 OEDocking TK 4.1.0

July 2021

## 6.8.1 New features

- A predicate string can now be supplied to *OEMakeReceptorOptions* using *SetTargetPred*. This povides a way to specify a select set of water molecules in an OEDesignUnit to be part of the receptor when the docking grid is constructed and used in subsequent docking calculations.
- OEMakeReceptor now autogenerates protein constraints. The constraints are left disabled by default for the docking calculations. These can be enabled using the toolkits, or the Make Receptor GUI application. The auto-generation of the constraints can be turned off using the SetAutoConstraints method in OEMakeReceptorOptions.

## 6.8.2 Minor bug fixes

• The default value for the  $SetBoxMol$  has been set to 0.0 in the OEMakeReceptorOptions class.

# 6.9 OEDocking TK 4.0.0.2

### March 2021

- Default value of Target Mask has been changed to OEDesignUnitComponents TargetComplexNoSolvent, to reflect best practices for receptor generation.
- Target Mask in OEMakeReceptorOptions now provides added flexibility to create user defined mask.
- An issue causing *OEPosit* to occasionally ignore the  $\text{Posit}$  Methods has been fixed.
- Constraints (both protein constraints and custom constraints) are now properly serialized in the OER eceptor in a .OEDU file.
- All of the protein constraints, custom constraints, and extra molecules are now properly transferred in the OEReceptor and the OEDesignUnit, when OEB format receptors are used.

# 6.10 OEDocking TK 4.0.0

Fall 2020

## 6.10.1 New features

- A new class, *OEMakeReceptorOptions*, has been added that provides choices for making an OEReceptor inside an OEDesignUnit.
- The OEMakeReceptor function now takes an OEDesignUnit and an OEMakeReceptorOptions, and adds an OEReceptor inside the OEDesignUnit object.
- A new class, OEDockOptions, has been introduced that provides choices for OEDockMethod and OESearchResolution in the OEDock class.
- The OEDock class constructor now has an overload that takes an OEDockOptions argument.
- The following methods now have an overload that accepts as an argument an OEDesignUnit containing an OEReceptor:
  - OEDock. Initialize
  - OEDock. CacheScoringSetup
  - OEScore. Initialize
  - OEScore. CacheScoringSetup
  - OEPosit.AddReceptor
- A new method, OESinglePoseResult. GetDesignUnit, has been added added that returns the resulting design unit containing the pose ligand and the target.
- A new class, OEPoseOptimizerOptions, has been added that provides choices for force fields and flexibility in performing pose optimization with *OEPoseOptimizer*.
- The OEPoseOptimizer class constructor now has an overload that takes an OEPoseOptimizerOptions.
- The OEPoseOptimizer. Optimize method now takes an OEDesignUnit to optimize.
- Flexible **POSIT** with *OEPosit*. Dock now uses the OEFF14SBParsley for pose optimization.
- A new method,  $OEPosit$ , RankDesignUnits, has been added that ranks an OEDesignUnit containing an OEReceptor for posing with multiple receptors.
- With the introduction of the new OEReceptor class and the corresponding behavior of the OEDocking TK, several previously existing APIs have been deprecated. The following table shows the deprecated APIs and their replacements:

| Deprecated API                  | New API                     |
|---------------------------------|-----------------------------|
| OEDocking:: OEBoxBase           | <b>OEBox</b>                |
| OEDocking:: OEBox               |                             |
| OEDocking:: OECustomConstraints | OEReceptorCustomConstraints |
| OEDocking:: OEFeature           | OEReceptorConstraintFeature |
| OEDocking:: OEProteinConstraint | OEReceptorProteinConstraint |
| OEDocking:: OESphereBase        | <b>OESphere</b>             |
| OEDocking:: OEAlignReceptors    | OEStructuralSuperposition   |
| OEDocking:: OEIsReceptor        | OEDesignUnit.HasReceptor    |
| OEDocking:: OEReceptorClear     | OEReceptor.Clear            |

| OEDocking::OEReceptorClearCustomConstraints  | OEReceptor.ClearCustomConstraints  |
|----------------------------------------------|------------------------------------|
| OEDocking::OEReceptorClearProteinConstraints | OEReceptor.ClearProteinConstraints |
| OEDocking::OEReceptorGetBoundLigand          | OEDesignUnit.GetLigand             |
| OEDocking::OEReceptorGetCustomConstraints    | GetCustomConstraints               |
| OEDocking::OEReceptorGetInnerContourLevel    | OEReceptor.GetInnerContourLevel    |
| OEDocking::OEReceptorGetOuterContourLevel    | OEReceptor.GetOuterContourLevel    |
| OEDocking::OEReceptorHasBoundLigand          | OEDesignUnit.HasLigand             |
| OEDocking::OEReceptorHasCustomConstraints    | OEReceptor.HasCustomConstraints    |
| OEDocking::OEReceptorHasInnerContourLevel    | OEReceptor.HasInnerContourLevel    |
| OEDocking::OEReceptorHasNegativeImageGrid    | OEReceptor.HasNegativeImageGrid    |
| OEDocking::OEReceptorHasOuterContourLevel    | OEReceptor.HasOuterContourLevel    |
| OEDocking::OEReceptorHasProteinConstraints   | OEReceptor.HasProteinConstraints   |
| OEDocking::OEReceptorSetCustomConstraints    | OEReceptor.SetCustomConstraints    |
| OEDocking::OEReceptorSetInnerContourLevel    | OEReceptor.SetInnerContourLevel    |
| OEDocking::OEReceptorSetOuterContourLevel    | OEReceptor.SetOuterContourLevel    |
| OEDocking::OEReceptorAddCachedScore          | OEDock.CacheScoringSetup           |
| OEDocking::OEReceptorSetCachedScore          | OEScore.CacheScoringSetup          |
| OEDocking::OEReadReceptorFile                | OEReadDesignUnit                   |
| OEDocking::OEReadReceptorToBytes             |                                    |
| OEDocking::OEWriteReceptorFile               | OEWriteDesignUnit                  |
| OEDocking::OEWriteReceptorToBytes            |                                    |
| OEDocking::OEBoxArea                         | OEBoxArea                          |
| OEDocking::OEBoxExtend                       | OEBoxExtend                        |
| OEDocking::OEBoxTranslate                    | OEBoxTranslate                     |
| OEDocking::OEBoxVolume                       | OEBoxVolume                        |
| OEDocking::OEBoxXDim                         | OEBoxXDim                          |
| OEDocking::OEBoxYDim                         | OEBoxYDim                          |
| OEDocking::OEBoxZDim                         | OEBoxZDim                          |
| OEDocking::OEBoxXMid                         | OEBoxXMid                          |
| OEDocking::OEBoxYMid                         | OEBoxYMid                          |
| OEDocking::OEBoxZMid                         | OEBoxZMid                          |
| OEDocking::OEInBox                           | OEInBox                            |
| OEDocking::OESetupBox                        | OESetupBox                         |
| OEDocking::OESetupBoxCenterAndExtents        |                                    |
| OEDocking::OEInSphere                        | OEInSphere                         |
| OEDocking::OESphereArea                      | OESphereArea                       |
| OEDocking::OESphereVolume                    | OESphereVolume                     |

Table 1 - continued from previous page

- With the introduction of the new APIs, several obsolete functionalities have been deprecated without any suitable replacements. These functionalities were added in the early development days of OEDocking TK and are no longer deemed useful:
  - OEDocking:: OEAlignReceptorFunction
  - OEDocking:: OEReceptorAddExtraMols
  - OEDocking:: OEReceptorClearBoundLigand
  - OEDocking:: OEReceptorClearExtraMols
  - OEDocking:: OEReceptorHasExtraMols

## **6.10.2 Documentation changes**

- The OEHybrid class documentation has been modified to clarify that it is derived from OEDock.
- Documentation for OEDocking:: OEDockBase and OEDocking:: OEScoreBase has been removed.
- All the OEDocking TK examples have been reorganized to reflect the modified API behavior.

# 6.11 OEDocking TK 3.5.0.5

• The OEZ file format now correctly persists receptor information.

# 6.12 OEDocking TK 3.5.0

As part of the integration of OEToolkits and OEApplications into a single release, the version number of OEDocking **TK** has been upgraded to 3.5.0 to make it consistent with that of the **OEDocking** applications suite.

## 6.12.1 New features

- $\bullet$  Two methods. OEPositOptions.SetExcludeSelf new and OEPositOptions.  $GetExcludeSelf$ , have been added to simplify cross-docking validation experiments with OEPosit.
- A new method, OEP osit. RankReceptors, has been added that can rank receptors when posing with multiple receptors.
- The method OEMakeReceptor has been overloaded to take an OEDesignUnit object as input.

## 6.12.2 Major bug fixes

• Memory management for  $OEDosit$ . Dock has been improved to handle up to 100 receptors when posing with multiple receptors.

## 6.12.3 Minor bug fixes

- The following methods now return bool instead of a void:
  - OEPositOptions. SetAllowedClashType
  - OEPositOptions. SetFullConformationSearch
  - OEPositOptions. SetIgnoreNitrogenStereo
  - OEPositOptions. SetMinProbability
  - OEPositOptions. SetPoserCacheCount
  - OEPositOptions. SetPoseRelaxMode
- OEPosit. Dock now fails gracefully when a single atom ligand is passed for posing.
- OEMakeBoxMolecule now sets the output molecule as 3D.

## **6.12.4 Documentation changes**

- The PoseMolsMultiReceptor example has been updated.
- An example has been added to the *Receptors* section showing how to convert an OEDesignUnit object to a receptor.

# 6.13 OEDocking TK 1.4.1

## 6.13.1 New features

- Two new result classes, OESinglePoseResult and OEPositResults, have been added that better report OEPositgenerated pose results.
- A new class, *OEPoseOptimizer*, has been added that optimizes an already generated pose to reduce clashes.
- A new method,  $Dock$ , has been introduced that provides greater flexibility in reporting the generated pose results. The OEDocking:: OEPosit:: DockMultiConformerMolecule method is now deprecated.
- Two new methods,  $AddReceptor$  and  $ClearReceptors$ , have been added to the *OEPosit* class that enable using multiple receptors in a single calculation.
- A new function,  $OEHASCIASh$ , has been added that allows clash detection.
- The following new methods have been added to the *OEPositOptions* class that enable working with multiple receptors as well as further refinement of generated poses:
  - GetAllowedClashType
  - SetAllowedClashType
  - GetMinProbability
  - SetMinProbability
  - GetPoserCacheCount
  - Set PoserCacheCount
  - GetPoseRelaxMode
  - SetPoseRelaxMode
- A new namespace, OEAllowedClashType, has been added that defines constants for various allowed clash types.
- A new namespace, OEPoseRelaxMode, has been added that defines if and when a relaxation should be performed.
- A new constant, OEDockingReturnCode\_NoValidNonClashPoses, has been added that indicates that no nonclashing poses are found.
- OEDockingReturnCodeGetName,  $\bullet$  A new function, has been added that converts OEDockingReturnCode to a meaningful string.
- A new function, OEPositMethodGetName, has been added that returns the name of an OEPositMethod in a string format.

## 6.13.2 Major bug fixes

- A rare crash that occurred during docking calculations in  $DockMultiConformer Molecule$  has been fixed.
- OEPosit no longer fails to generate poses due to unspecified stereo in the input molecule.

## 6.13.3 Minor bug fixes

- OEMakeReceptor now returns an empty receptor molecule when it fails.
- OEGetEstimatedPositProbability no longer crashes when a failure occurs during conformer generation.

## **6.13.4 Documentation changes**

- Two new examples have been added in the sections, Using Multiple Receptors and Receptor Flexibility, that demonstrate new POSIT features for working with multiple receptors and for further refining generated poses, respectively.
- Docking examples have been updated for better coding practices that check the return code status of docking and print out any errors.

# 6.14 OEDocking TK 1.4.0

## 6.14.1 Major bug fixes

- OEDocking::OEPosit::DockMultiConformerMolecule now correctly uses the FRED method when there is no bound ligand in the receptor.
- . OEDocking::OEPosit::DockMultiConformerMolecule now correctly uses the FRED method when the similarity between the bound ligand and the posed ligand is very low.

## 6.14.2 Minor bug fixes

. OEDocking::OEDock::DockMultiConformerMolecule now returns a failure code when the best scoring pose for a molecule has an unreasonable score.

# 6.15 OEDocking TK 1.3.7

• Minor internal improvements have been made.

# 6.16 OEDocking TK 1.3.6

## 6.16.1 New features

• Language-specific functions have been added to export receptors to bytes and read receptors from bytes. For Python, see OEReadReceptorFromBytes and OEWriteReceptorToBytes.

# 6.17 OEDocking TK 1.3.5

• Minor internal improvements have been made.

# 6.18 OEDocking TK 1.3.4

• Minor internal improvements have been made.

# 6.19 OEDocking TK 1.3.3

• Minor internal improvements have been made.

# 6.20 OEDocking TK 1.3.2

• Minor internal improvements have been made.

# 6.21 OEDocking TK 1.3.1

## 6.21.1 New features

• OEAddDockingInteractions function has been overloaded and can now take an OEInteractionHintContainer object. The previous OEFragmentNetwork version has been deprecated and will throw a warning upon calling.

## 6.21.2 C++-specific changes

• PoseMolsWithBestReceptor.cpp example has been rewritten to improve performance.

# 6.22 OEDocking TK 1.3.0

## 6.22.1 Minor bug fixes

• A bug that caused the docking toolkit to crash if OEDock or OEScore were given a receptor that contained an arginine with a negatively charged nitrogen has been fixed.

## 6.22.2 Python-specific changes

- PoseMolsWithBestReceptor.py now avoids redundantly calculating the similarity of the docking and crystallographic ligand multiple times, improving the speed of this script when using multiple receptors.
- *OEDock* and *OEScore* methods will now release the global interpreter lock while performing expensive computations.

# 6.23 OEDocking TK 1.2.7

## 6.23.1 Minor bug fixes

• OEAddDockingInteractions has been updated after implementation changes were made to the  $OE$ -Bio::OEFragmentNetwork class. An example has been added to OEBio TK that illustrates how to access the protein-ligand interactions perceived by the OEAddDockingInteractions function.

# 6.24 OEDocking TK 1.2.6

## 6.24.1 New features

• OEFormat OEB now supports the reading and writing of receptor information on OEMCMolBase conformers. Previously, only OEMolBase receptors were supported. The receptor APIs should still be used only on the active conformer of multi-conformer molecules; see OEMCMolBase. GetActive.

## 6.24.2 Minor bug fixes

• OEFormat\_OEB will no longer have receptor data written to it twice. This caused the receptor OEBs to be approximately twice as large but was otherwise harmless.

# 6.25 OEDocking TK 1.2.5

## 6.25.1 New features

• A new OEAddDockingInteractions function works with Grapheme's new active-site rendering functionality to perceive all necessary interactions.

## 6.25.2 Minor bug fixes

- OEPosit will no longer leak memory.
- An issue with hydrogen bonding groups on the protein being ignored when the available volume for an interacting molecule near the hydrogen bond group was less than 100 cubic angstroms has been fixed. Previously, the scoring function was set up with a protein and box, rather than a receptor object.
- Internal refactoring has been added to improve stability.
- A bug in the hydrogen bonding geometry perception of primary planar amines with interaction directions perpendicular to the plane has been fixed. Under this bug, such an interacting group had a 50% chance of selecting the wrong perpendicular direction.

# 6.26 OEDocking TK 1.2.4

• Minor internal improvements.

# 6.27 OEDocking TK 1.2.3

## 6.27.1 New features

The following improvements have been made to OEPosit:

- Graph comparison is used to identify when default OEOmega sampling may not produce appropriate conformers. If this is detected, the ShapeFit methodology is used to further sample conformation space.
- The initial overlays for ShapeFit are now chosen with the best TanimotoCombo overlay to the bound ligand prior to optimization.
- The choice of fitting routine (ShapeFit, Hybrid, or FRED) now take into account both the TanimotoCombo overlay and the graph similarity of the molecule. The graph similarity helps during cases where OMEGA undersamples and by sampling more conformations, better overlays can be generated.
- When generating conformer ensembles, the maximum number of conformers is set to 100 times the number of rotatable bonds with a minimum number of 200 conformers. This allows better sampling of floppy conformations.
- The maximum MMFF94s induced strain is increased to 20 kCal for molecules with more than 12 rotatable bonds.
- When FRED or HYBRID can not fit a molecule into the receptor, ShapeFit is automatically chosen regardless of the expected probability.
- If the input conformations include 3D coordinates, they are retained even when generating conformations.

## 6.27.2 Major bug fixes

- . OEDocking::OEPosit::DockMultiConformerMolecule would previously only generate one pose. Now up to numPoses poses will be generated.
- SDData is retained from the input molecule. In the case of an input conformer ensemble, the SDData is chosen from the conformer with the closest RMSD to the final optimized pose.

## 6.27.3 Minor bug fixes

- A GOOD pose has been set to a probability of  $\ge$  = 0.5 not  $>$  0.5 to be the same as specified by the documentation.
- Removed unbounded stack allocations.
- Removed annotation of optimization steps when writing to . oeb format.
- Rare crash in ShapeFit fixed for C++ and Python toolkits on OSX 10.8 and 10.9.

# 6.28 OEDocking TK 1.2.2

## 6.28.1 New features

- OEPositMethod constants added to select which OEPosit to use at runtime.
- OEDocking::OEPositMethod::SHAPEFIT\_EXHAUSTIVE search method added for better support of matching substructures of already posed ligands in binding sites. This has been accomplished by incorporating the Subrocs algorithm for initial starting points.
- · OEPositOptions. SetIgnoreNitrogenStereo added to allow OEPosit to ignore nitrogen stereo centers in conformer enumeration.
- *OEPosit* now annotates clashed molecules.

## 6.28.2 Major bug fixes

- OEPosit now retains SD data of the input molecule.
- Debugging information removed from *OEPosit* docked molecules.
- OEGetEstimatedPositProbability is more robust with molecules missing explicit hydrogens.

## 6.28.3 Minor bug fixes

• Fixed an issue where secondary sp3 hydrogen bonding groups had slightly skewed geometry. In practice this causes the relevant HB angles to be about 15 degrees off, and the net effect on the score was minimal.

## **6.28.4 Documentation Changes**

- OECustomConstraints class was improperly referred to as OECustomConstraint, without the s, in the documentation.
- OEPositMethod\_UNKNOWN capitalization in the documentation was wrong in previous versions.
- OEPositOptions class has been updated with new settings: select the methods OEPosit will run ignore nitrogen stereo centers when making internal conformations

# 6.29 OEDocking TK 1.2.1

## 6.29.1 New Features

• OEPosit - When full conformer search is turned off, OMEGA is automatically run when the docked ligand is not a 3D conformer.

## 6.29.2 Major bug fixes

• OEPosit - Fixed a crash when setting full conformer search to false and docking a ligand with missing hydrogens.

## 6.29.3 Minor bug fixes

· Uses of OEThrow. Fatal changed to OEThrow. Error.

# 6.30 OEDocking TK 1.2.0

## 6.30.1 New features

The POSIT posing algorithm has been integrated into the OEDocking toolkit. The algorithm uses known bound reference ligands to generate a probability that, if the query ligand actually binds, the generated pose is within 2.0 Angströms of the experimentally derived structure. This probability also guides the selection of the appropriate receptors (if multiple are provided) for docking as well as determining which docking methodology to use: SHAPEFIT, HYBRID, or FRED. Specific details on each methodology can be found in OEDocking's pose prediction chapter.

# 6.31 OEDocking TK 1.1.4

## 6.31.1 New features

• Hydrogen bond protein constraints now have improved recognition of appropriate hydrogen bond geometry. This should result in few false positives (i.e., there should be few docked poses that make poor hydrogen bond interactions with the hydrogen bond constraint atom on the protein).

## 6.31.2 Minor bug fixes

- Fixed a minor bug where the OEDock object could use more memory than needed.
- Fixed a potential out of memory error when calling OEMakeReceptor on a very large protein.

# 6.32 OEDocking TK 1.1.3

## 6.32.1 Bug fixes

• Fixed a rare one time initialization race condition that could only occur when using the *Docking TK* OEInterface convenience functions.

# 6.33 OEDocking TK 1.1.2

## 6.33.1 Bug fixes

where OEDocking::OEDockBase::DockMultiConformerMolecule  $\bullet$  Fixed bug incorrectly returned OEDockingReturnCode\_Success in cases where no poses of the molecule that fit in the active site could be found. This method now correctly returns OEDockingReturnCode\_NoValidPoses in this case.

## 6.33.2 Improvements

• Slightly increased speed of *Chemgauss4* in both docking and optimization.

# 6.34 OEDocking TK 1.1.1

## 6.34.1 Bug fixes

- Fixed bug where SD data on the input molecules was not copied to the docked output molecule.
- Fixed memory leak when scoring a molecule that does not fit within the receptor site.
- Fixed an invalid memory access bug that occurred in rare cases when docking molecules.

# 6.35 OEDocking TK 1.1.0

• The behavior of OEDockMethod\_Hybrid from version 1.0 has been changed. OEDockMethod\_Hybrid is now an alias for the most up to date docking method, currently OEDockMethod Hybrid2. OEDockMethod\_Hybrid1 now provides the same functionality that OEDockMethod\_Hybrid did in version 1.0 of *OEDocking TK*.

## 6.35.1 New Features

- OEDocking TK is now thread safe. For details on thread safety see the "Thread Safety" section of the OEChem toolkit.
- Chemgauss4 scoring function, available both as a docking method (OEDockMethod\_Chemgauss4) and scoring method (OEScoreType\_Chemgauss4).
- Hybrid 2 docking method (OEDockMethod\_Hybrid2), that uses Chemgauss4 for the structure based portion of the docking.
- OEHybrid class for doing hybrid docking added for convenience. OEHybrid is identical to OEDock, except that the default method is OEDockMethod Hybrid rather than OEDockMethod Chemgauss.
- Scoring function setup information from OEDock, OEHybrid and OEScore objects can now be saved on receptor files, decreasing the setup time for future runs.
- Fixed a bug where OEB handlers were not setup correctly sometimes due to link ordering problems.

## 6.35.2 Bug fixes

- Fixed bug generating negative image grids, that caused the negative image to extend further from the protein and penetrate less deeply into pockets than was intended.
- Fixed a bug in the local optimization (done during docking or with a call to OEScore. SystematicSolidBodyOptimize) that caused the local rotations to be less evenly spaced than they could be. This bug also affected the optimization done by the OEDock class.

# 6.36 OEDocking TK 1.0.0

- Docking features
  - Exhaustive Search docking followed by pose optimization
  - Hybrid docking (uses the structure a known bound active to guide docking)
  - Docking constraints (e.g., require specific hydrogen bonding interactions)
- Scoring features
  - Score optimization (systematic solid body optimization)
  - Break down of score by atom and/or scoring function component
  - Score annotating (stores score breakdown on molecule for visualization in VIDA)
- Implementation of four scoring functions
  - $-$  Chemgauss3
  - Chemscore
  - $-$  PLP
  - Shapegauss

## **SEVEN**

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

## **EIGHT**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

## **NINE**

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

# 9.3 OpenEye Web Services

To cite use of the Macromolecular Data Service (MMDS) web service, please use the syntax:

Macromolecular Data Service <version-number>. OpenEye, Cadence Molecular Sciences, -Santa Fe, NM. http://www.eyesopen.com.

### For example:

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

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|--------------------------------------------|-------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abseil-cpp                                 | https://github.com/abseil/abseil-cpp                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| absl-py                                    | https://github.com/abseil/abseil-py                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| aiohttp                                    | https://docs.aiohttp.org/en/stable/                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| aiosignal                                  | https://github.com/aio-libs/aiosignal                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Amazon Linux 2                             | https://aws.amazon.com/amazon-linux-2                                               | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| AmberUtils                                 | http://ambermd.org                                                                  | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ambit                                      | https://github.com/khimaros/ambit                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| amqp                                       | https://github.com/celery/py-amqp                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| anaconda-anon-usage                        | Orion Floes                                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular                                    | https://github.com/angular/angular.js                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-animate                            | https://github.com/angular/angular.js                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-cache                              | https://github.com/jmdobry/angular-cache                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-cookies                            | https://github.com/angular/angular.js                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-loggly-logger                      | https://github.com/ajbrown/angular-loggly-logger                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-mocks                              | https://github.com/angular/angular.js                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-resource                           | https://github.com/angular/angular.js                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-toggle-switch                      | https://github.com/cgarvis/angular-toggle-switch                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-ui-grid                            | https://github.com/angular-ui/ui-grid                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-ui-router                          | https://github.com/angular-ui/ui-router                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-ui-tree                            | https://github.com/angular-ui-tree/angular-ui-tree                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| angular-vs-repeat                          | https://github.com/kamilkp/angular-vs-repeat                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| aniso8601                                  | https://bitbucket.org/nielsenb/aniso8601                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| annotated-types                            | https://github.com/annotated-types/annotated-types                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| anyio                                      | https://github.com/agronholm/anyio                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| appdirs                                    | http://github.com/ActiveState/appdirs                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| appengine                                  | https://google.golang.org/appengine                                                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| arabic-reshaper                            | https://github.com/mpcabd/python-arabic-reshaper/                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| archspec                                   | https://github.com/archspec/archspec/blob/master/README.md                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| argon2-cffi                                | https://github.com/hynek/argon2-cffi                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| argon2-cffi-bindings                       | https://github.com/hynek/argon2-cffi-bindings                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| arpack                                     | https://www.caam.rice.edu/software/ARPACK/                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ascii85                                    | https://github.com/huandu/node-ascii85                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ase                                        | https://wiki.fysik.dtu.dk/ase/                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| asgiref                                    | https://github.com/django/asgiref/                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| asn1crypto                                 | https://github.com/wbond/asn1crypto                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| assertions go-render                       | https://github.com/smartystreets/assertions/internal/go-render/render               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| assertions oglmatchers                     | https://github.com/smartystreets/assertions/internal/oglematchers                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| assertions                                 | https://github.com/smartystreets/assertions                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| asttokens                                  | https://github.com/gristlabs/asttokens                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| astunparse                                 | https://github.com/simonpercivall/astunparse                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| async-lru                                  | https://github.com/aio-libs/async-lru                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| async-timeout                              | https://github.com/aio-libs/async-timeout                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| atk-1.0                                    | https://docs.gtk.org/atk/                                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| atomic                                     | https://github.com/uber-go/atomic                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| atomicwrites                               | https://github.com/untitaker/python-atomicwrites                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| attrs                                      | https://www.attrs.org/                                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| aws-sdk-go                                 | https://github.com/aws/aws-sdk-go                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Babel                                      | https://github.com/python-babel/babel                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| backcall                                   | https://github.com/takluyver/backcall                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| backports                                  | https://github.com/brandon-rhodes/backports                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| backports.functools-lru-cache              | https://github.com/jaraco/backports.functools_lru_cache                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| base62                                     | https://github.com/kare/base62                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| beautifulsoup4                             | https://www.crummy.com/software/BeautifulSoup/                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| billiard                                   | https://github.com/celery/billiard                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| biopython                                  | https://biopython.org                                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| biotite                                    | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bitset                                     | https://github.com/willf/bitset                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| blas                                       | https://www.netlib.org/blas/                                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bleach                                     | https://github.com/mozilla/bleach                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| blessings                                  | https://github.com/erikrose/blessings                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| blinker                                    | https://pythonhosted.org/blinker/                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| blosc                                      | https://github.com/Blosc/python-blosc                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| blosc2                                     | https://github.com/Blosc/python-blosc2                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| boltons                                    | https://github.com/mahmoud/boltons                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| boost                                      | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| boost-cpp                                  | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bootstrap-vue                              | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| boto3                                      | https://github.com/boto/boto3                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| botocore                                   | https://github.com/boto/botocore                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Bottleneck                                 | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Brotli                                     | https://github.com/google/brotli                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| brotli-bin                                 | https://github.com/google/brotli                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| brotli-python                              | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| brotlipy                                   | https://github.com/python-hyper/brotlicffi                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bson                                       | http://github.com/py-bson/bson                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bytefmt                                    | https://code.cloudfoundry.org/bytefmt                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| bzip2                                      | https://www.bzip.org                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                            |                                                                                     | J.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Name of Project                            | Website                                                                             | Licen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| c-ares                                     | https://github.com/c-ares/c-ares                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ca-certificates                            | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cached-property                            | https://github.com/pydanny/cached-property                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cachetools                                 | https://github.com/tkem/cachetools/                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cairo                                      | https://pycairo.readthedocs.io/en/latest/                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| canvas                                     | https://github.com/Automattic/node-canvas                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cctbx                                      | https://github.com/cctbx/cctbx_project                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| celery                                     | https://github.com/celery/celery                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cerberus                                   | https://docs.python-cerberus.org/en/stable/                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| certifi                                    | https://certifiio.readthedocs.io/en/latest/                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cffi                                       | https://github.com/python-cffi                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cftime                                     | https://pypi.org/project/cftime/                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| chardet                                    | https://github.com/chardet/chardet                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| charset-normalizer                         | https://github.com/ousret/charset_normalizer                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| chunkreader                                | https://github.com/jackc/chunkreader/v2                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| click                                      | https://palletsprojects.com/p/click/                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| click-completion                           | https://github.com/click-contrib/click-completion                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| click-didyoumean                           | https://github.com/click-contrib/click-didyoumean                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| click-plugins                              | https://github.com/click-contrib/click-plugins                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| click-repl                                 | https://github.com/untitaker/click-repl                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cloudpickle                                | https://github.com/cloudpipe/cloudpickle                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cmake                                      | https://cmake.org/                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| colorama                                   | https://github.com/tartley/colorama                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| comm                                       | https://github.com/ipython/comm                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| compose                                    | https://github.com/docker/compose                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| conda-content-trust                        | https://github.com/conda/conda-content-trust                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| conda-libmamba-solver                      | https://github.com/conda/conda-libmamba-solver                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| conda-package-handling                     | https://github.com/conda/conda-package-handling                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| conda-package-streaming                    | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| conda-token                                | https://anaconda.org/anaconda/conda-token                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| confuse                                    | https://github.com/beetbox/confuse                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| contourpy                                  | https://github.com/contourpy/contourpy                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cpp-peglib                                 | https://github.com/yhirose/cpp-peglib                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cryptography                               | https://github.com/pyca/cryptography                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cssselect2                                 | https://github.com/Kozea/cssselect2/                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cudatoolkit                                | https://developer.nvidia.com/cuda-toolkit                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cupy-cuda113                               | https://cupy.dev/                                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| curl                                       | https://curl.se                                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cycler                                     | https://github.com/matplotlib/cycler                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| cyrus-sasl                                 | https://github.com/cyrusimap/cyrus-sasl                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Cython                                     | https://cython.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| $\overline{d3}$                            | https://github.com/mbostock/d3                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dataclasses                                | https://github.com/ericvsmith/dataclasses                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ddsketch                                   | http://github.com/datadog/sketches-py                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| debugpy                                    | https://aka.ms/debugpy                                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| decimal                                    | https://github.com/shopspring/decimal                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| decorator                                  | https://github.com/micheles/decorator                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| deepdiff                                   | https://github.com/seperman/deepdiff                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| deeptime                                   | https://github.com/deeptime-ml/deeptime                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                            |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|                                            |                                                                                     | J.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Name of Project                            | Website                                                                             | Licen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| defusedxml                                 | https://github.com/tiran/defusedxml                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| $di$ <sup>111</sup>                        | https://github.com/uqfoundation/dill                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| distro                                     | <b>Orion Floes</b>                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Django                                     | https://www.djangoproject.com/                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-classy-tags                         | https://github.com/django-cms/django-classy-tags                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-cors-headers                        | https://github.com/adamchainz/django-cors-headers                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-csp                                 | https://github.com/mozilla/django-csp                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-extensions                          | https://github.com/django-extensions/django-extensions                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-filter                              | https://github.com/carltongibson/django-filter/tree/master                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-redis                               | https://github.com/jazzband/django-redis                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-taggit                              | https://github.com/jazzband/django-taggit                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-taggit-serializer                   | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| django-taggit-templatetags2                | https://github.com/fizista/django-taggit-templatetags2                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| djangorestframework                        | https://www.django-rest-framework.org/                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dkh                                        | https://psicode.org/psi4manual/master/dkh.html                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| dm-tree                                    | https://github.com/deepmind/tree                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| docker-py                                  | https://github.com/docker/docker-py/                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| docopt                                     | https://docopt.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| docutils                                   | https://docutils.sourceforge.io                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| drf-dynamic-fields                         | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| editdistance                               | https://github.com/roy-ht/editdistance                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| eigen                                      | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| einops                                     | https://github.com/arogozhnikov/einops                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| entrypoints                                | https://github.com/takluyver/entrypoints                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                            | https://github.com/pkg/errors                                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| errors                                     | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| eslint-plugin<br>$et$ <sub>_</sub> xmlfile |                                                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                            | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| exceptiongroup                             | https://github.com/agronholm/exceptiongroup                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| executing                                  | https://github.com/alexmojaki/executing                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| expat                                      | https://libexpat.github.io                                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fastjsonschema                             | https://github.com/horejsek/python-fastjsonschema                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fastrlock                                  | https://github.com/scoder/fastrlock                                                 | $\frac{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https://n.7}{https$ |
| fftw                                       | https://www.fftw.org                                                                | comm                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| filebuffer                                 | https://github.com/mattetti/filebuffer                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| filelock                                   | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| finufft                                    | https://github.com/flatironinstitute/finufft                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Flask                                      | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| flatbuffers                                | https://google.github.io/flatbuffers/                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| flit-core                                  | https://github.com/pypa/flit                                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <b>FLTK</b>                                | https://www.fltk.org/index.php                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fmt                                        | https://fmt.dev/latest/index.html                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| font-awesome                               | https://github.com/FortAwesome/Font-Awesome                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| font-ttf-dejavu-sans-mono                  | https://dejavu-fonts.github.io                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| font-ttf-inconsolata                       | https://fonts.google.com/specimen/Inconsolata                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| font-ttf-source-code-pro                   | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| font-ttf-ubuntu                            | https://fonts.google.com/specimen/Ubuntu                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fontconfig                                 | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fonts-conda-ecosystem                      | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fonts-conda-forge                          | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fonttools                                  | https://github.com/fonttools/fonttools                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| freetype                                   | https://freetype.org                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fribidi                                    | https://github.com/fribidi/fribidi                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| frozendict                                 | Orion Floes                                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| frozenlist                                 | https://github.com/aio-libs/frozenlist                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fsmlite                                    | https://github.com/tkem/fsmlite                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| fsspec                                     | https://github.com/fsspec/filesystem_spec                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| funcy                                      | https://github.com/Suor/funcy                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gast                                       | https://github.com/serge-sans-paille/gast/                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gau2grid                                   | https://github.com/dgasmith/gau2grid                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gax-go                                     | https://github.com/googleapis/gax-go/v2                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gdk-pixbuf                                 | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gemmi                                      | https://gemmi.readthedocs.io/en/latest/                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| genproto                                   | https://google.golang.org/genproto/googleapis                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| geometric                                  | https://openbase.com/python/geometric                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| giflib                                     | https://giflib.sourceforge.net                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| glib                                       | https://docs.gtk.org/glib/                                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| GLM Library                                | https://github.com/g-truc/glm                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gls                                        | https://github.com/jtolds/gls                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-cleanhttp                               | https://github.com/hashicorp/go-cleanhttp                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-connections                             | https://github.com/docker/go-connections                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-cpio                                    | https://github.com/cavaliercoder/go-cpio                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-getter                                  | https://github.com/hashicorp/go-getter                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-homedir                                 | https://github.com/mitchellh/go-homedir                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-ini                                     | https://github.com/go-ini/ini                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-jmespath                                | https://github.com/jmespath/go-jmespath                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-junit-report                            | https://github.com/jstemmer/go-junit-report                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-netrc                                   | https://github.com/bgentry/go-netrc/netrc                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-ole                                     | https://github.com/go-ole/go-ole                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-pg                                      | https://github.com/go-pg/pg                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-redis                                   | https://github.com/go-redis/redis/v8                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-rendezvous                              | https://github.com/dgryski/go-rendezvous                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-safetemp                                | https://github.com/hashicorp/go-safetemp                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-sysconf                                 | https://github.com/tklauser/go-sysconf                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-testing-interface                       | https://github.com/mitchellh/go-testing-interface                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-units                                   | https://github.com/docker/go-units                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-version                                 | https://github.com/hashicorp/go-version                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go-zglob                                   | https://github.com/mattn/go-zglob                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| go.opencensus                              | https://go.opencensus.io                                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gobrake.v2                                 | https://gopkg.in/airbrake/gobrake.v2                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| goconvey                                   | https://github.com/smartystreets/goconvey                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| golden-layout                              | https://github.com/deepstreamIO/golden-layout                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| google-auth                                | https://google-auth.readthedocs.io/en/master/                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| google-auth-oauthlib                       | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| google-cloud-go                            | https://cloud.google.com/go                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| google-cloud-go/storage                    | https://cloud.google.com/go/storage                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| google-pasta                               | https://github.com/google/pasta                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| google.golang.org/api                      | https://google.golang.org/api                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gopsutil                                   | https://github.com/shirou/gopsutil                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gorilla websocket                          | https://github.com/gorilla/websocket                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| graphite2                                  | https://github.com/silnrsi/graphite                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| graphviz                                   | https://graphviz.org/                                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| greenlet                                   | https://greenlet.readthedocs.io/en/latest/                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| groupcache                                 | https://github.com/golang/groupcache                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| grpc                                       | https://google.golang.org/grpc                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| grpc-cpp                                   | https://github.com/grpc/grpc                                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| grpcio                                     | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gtk2                                       | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| gts                                        | https://sourceforge.net/projects/gts/                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| h5py                                       | https://www.h5py.org                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| harfbuzz                                   | https://github.com/harfbuzz/harfbuzz                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| hdbscan                                    | https://hdbscan.readthedocs.io/en/latest/                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| hdf4                                       | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| hdf5                                       | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| he                                         | https://github.com/mathiasbynens/he                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| html-loader                                | https://github.com/webpack-contrib/html-loader                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| html5lib                                   | https://github.com/html5lib/html5lib-python                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| htslib                                     | https://www.htslib.org                                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| humanize                                   | https://github.com/jmoiron/humanize                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| icu                                        | https://github.com/unicode-org/icu                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| idna                                       | https://github.com/kjd/idna                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| imageio                                    | https://github.com/imageio/imageio                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| imagesize                                  | https://github.com/shibukawa/imagesize_py                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| <b>ImmuneBuilder</b>                       | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| importlib-metadata                         | https://github.com/python/importlib_metadata                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| importlib_resources                        | https://github.com/python/importlib_resources                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| InChI                                      | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| inflection                                 | https://github.com/jinzhu/inflection                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ini.v1                                     | https://gopkg.in/ini.v1                                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| iniconfig                                  | https://github.com/pytest-dev/iniconfig                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| innersvg-polyfill                          | https://github.com/dnozay/innersvg-polyfill                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| intel-openmp                               | https://github.com/hermitcore/libomp_oss                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ipykernel                                  | https://ipython.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ipython                                    | https://ipython.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ipython-genutils                           | http://ipython.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ipywidgets                                 | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| isodate                                    | https://github.com/gweis/isodate/                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| itsdangerous                               | https://palletsprojects.com/p/itsdangerous/                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jax                                        | https://github.com/google/jax                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jaxlib                                     | https://github.com/google/jax                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jedi                                       | https://jedi.readthedocs.io/en/latest/                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Jinja2                                     | https://palletsprojects.com/p/jinja/                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jmespath                                   | https://github.com/jmespath/jmespath.py                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| joblib                                     | https://joblib.readthedocs.io/en/latest/                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jpeg                                       | https://www.ijg.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| json5                                      | https://github.com/dpranke/pyjson5                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jsonfield                                  | https://github.com/dmkoch/django-jsonfield/                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jsonpatch                                  | https://github.com/stefankoegl/python-json-patch                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jsonpickle                                 | https://github.com/jsonpickle/jsonpickle                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jsonpointer                                | https://github.com/stefankoegl/python-json-pointer                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jsonschema                                 | https://github.com/python-jsonschema/jsonschema                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jsonschema-specifications                  | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jstat                                      | https://github.com/jstat/jstat                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter-client                             | https://jupyter.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter-core                               | https://jupyter.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter-events                             | https://github.com/jupyter/jupyter_events                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter-lsp                                | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter-server                             | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyterlab                                 | https://github.com/jupyterlab/jupyterlab                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyterlab-pygments                        | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyterlab-widgets                         | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyterlab_server                          | https://github.com/jupyterlab/jupyterlab_server                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter_client                             | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter_core                               | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter_server                             | https://github.com/jupyter-server/jupyter_server                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| jupyter_server_terminals                   | https://github.com/jupyter-server/jupyter_server_terminals                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| kaleido                                    | https://github.com/plotly/Kaleido                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| keras                                      | https://github.com/keras-team/keras                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Keras-Preprocessing                        | https://github.com/keras-team/keras-preprocessing                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| keras-tuner                                | https://github.com/keras-team/keras-tuner                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| keyring                                    | https://github.com/jaraco/keyring                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| keyutils                                   | https://github.com/sassoftware/python-keyutils                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| kiwisolver                                 | https://kiwisolver.readthedocs.io/en/latest/                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| kombu                                      | https://kombu.readthedocs.io                                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| krb5                                       | https://web.mit.edu/kerberos/                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| kt-legacy                                  | https://github.com/haifeng-jin/kt-legacy                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| lazy_loader                                | https://github.com/scientific-python/lazy_loader                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| lcms2                                      | https://www.littlecms.com                                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| lerc                                       | https://github.com/Esri/lerc                                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libarchive                                 | http://www.libarchive.org                                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libblas                                    | https://www.netlib.org/blas/                                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libbrotlicommon                            | https://github.com/google/brotli                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libbrotlidec                               | https://github.com/google/brotli                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libbrotlienc                               | https://github.com/google/brotli                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libcblas                                   | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| libclang                                   | <b>Orion Floes</b>                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libcurl                                    | https://curl.se/libcurl/                                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libcxx                                     | https://github.com/llvm-mirror/libcxx                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libdb                                      | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libdeflate                                 | https://github.com/ebiggers/libdeflate                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libedit                                    | https://thrysoee.dk/editline/                                                       | http://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libev                                      | https://software.schmorp.de/pkg/libev.html                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libffi                                     | https://github.com/libffi/libffi                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libgcrypt                                  | https://gnupg.org/software/index.html                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libgd                                      | https://libgd.github.io                                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libglib                                    | https://github.com/PolMine/libglib                                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| libiconv                                   | https://www.gnu.org/software/libiconv/                                              | https:/<br>https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| libint                                     | https://tinyurl.com/yvw97wbw                                                        | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| liblapack                                  | http://www.netlib.org/lapack/                                                       | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| liblapacke                                 | https://anaconda.org/conda-forge/liblapacke                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libmamba                                   | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libmambapy                                 | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libnetcdf                                  | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libnghttp2                                 | https://github.com/nghttp2/nghttp2                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libopenblas                                | https://www.openblas.net/                                                           | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libpng                                     | https://www.libpng.org/pub/png/libpng.html                                          | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libpq                                      | https://www.postgresql.org/                                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| librsvg                                    | https://gitlab.gnome.org/GNOME/librsvg                                              | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libsolv                                    | https://github.com/openSUSE/libsolv                                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libssh2                                    | https://github.com/libssh2/libssh2                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libtiff                                    | https://www.libtiff.org/                                                            | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libtrust                                   | https://github.com/docker/libtrust                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libuuid                                    | https://sourceforge.net/projects/libuuid/                                           | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libuv                                      | https://github.com/libuv/libuv                                                      | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libwebp                                    | https://chromium.googlesource.com/?format=HTML                                      | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libwebp-base                               | https://chromium.googlesource.com/?format=HTML                                      | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libxc                                      | https://www.tddft.org/programs/libxc/                                               | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libxcb                                     | https://xcb.freedesktop.org                                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libxml2                                    | https://git.gnome.org/browse/libxml2/                                               | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libxmlsec1                                 | https://github.com/lsh123/xmlsec                                                    | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libxslt                                    | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| libzlib                                    | https://zlib.net                                                                    | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| lime                                       | https://github.com/marcotcr/lime                                                    | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| lit                                        | http://llvm.org                                                                     | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| llvm-openmp                                | https://github.com/llvm-mirror/openmp                                               | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| llvmlite                                   | http://llvmlite.readthedocs.io                                                      | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| loader-utils                               | https://github.com/webpack/loader-utils                                             | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| logomaker                                  | https://logomaker.readthedocs.io/en/latest/                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| logrus                                     | https://github.com/sirupsen/logrus                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| logrus-airbrake-hook.v2                    | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| lxml                                       | https://lxml.de                                                                     | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| lz4-c                                      | https://www.lz4.org/                                                                | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| markdown                                   | https://github.com/evilstreak/markdown-js                                           | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| markdown-it-py                             | Orion Floes                                                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MarkupSafe                                 | https://palletsprojects.com/p/markupsafe/                                           | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| matplotlib                                 | https://matplotlib.org                                                              | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| matplotlib-base                            | https://matplotlib.org                                                              | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| matplotlib-inline                          | https://github.com/ipython/matplotlib-inline                                        | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| mda-xdrlib                                 | https://github.com/MDAnalysis/mda-xdrlib                                            | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| mdtraj                                     | https://www.mdtraj.org/                                                             | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| mdurl                                      | Orion Floes                                                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| menuinst                                   | Orion Floes                                                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| mergo                                      | https://github.com/imdario/mergo                                                    | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| mistune                                    | https://github.com/lepture/mistune                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| mkl                                        | https://github.com/rust-math/intel-mkl-src                                          | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| mkl-fft                                    | https://github.com/IntelPython/mkl_fft                                              | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| mkl-random                                 | https://github.com/IntelPython/mkl_random                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| mkl-service                                | https://github.com/IntelPython/mkl-service                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ml-dtypes                                  | Orion Floes                                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| molecupy                                   | https://molecupy.readthedocs.io/en/latest/                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| moment                                     | https://github.com/moment/moment                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| moment-precise-range-plugin                | https://github.com/codebox/moment-precise-range                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| more-itertools                             | https://github.com/more-itertools/more-itertools                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| mpiplus                                    | https://github.com/choderalab/mpiplus                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| mpmath                                     | http://mpmath.org/                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| mrcfile                                    | https://github.com/ccpem/mrcfile                                                    | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| msgpack                                    | https://msgpack.org/                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| multidict                                  | https://github.com/aio-libs/multidict                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| multierr                                   | https://go.uber.org/multierr                                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| multiprocess                               | https://github.com/uqfoundation/multiprocess                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| munkres                                    | https://software.clapper.org/munkres/                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| myesui uuid                                | https://github.com/myesui/uuid                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| namex                                      | Orion Floes                                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nbclassic                                  | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nbclient                                   | https://jupyter.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nbconvert                                  | https://jupyter.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nbformat                                   | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ncurses                                    | https://invisible-island.net/ncurses/                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nest-asyncio                               | https://github.com/erdewit/nest_asyncio                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| netcdf-fortran                             | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| netCDF4                                    | http://github.com/Unidata/netcdf4-python                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nettle                                     | https://git.lysator.liu.se/nettle/nettle                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| networkx                                   | https://networkx.org                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nfpm                                       | https://github.com/goreleaser/nfpm                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ng-tags-input                              | https://github.com/mbenford/ngTagsInput                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ng-toast                                   | https://github.com/tameraydin/ngToast                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ngdraggable                                | https://github.com/fatlinesofcode/ngDraggable                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ngVue                                      | https://github.com/ngVue/ngVue                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nlopt                                      | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nodejs                                     | https://nodejs.org/en/                                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nomkl                                      | https://github.com/conda-forge/nomkl-feedstock                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| notebook                                   | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| notebook-shim                              | https://github.com/jupyter/notebook_shim                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| notebook_shim                              | http://jupyter.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| numba                                      | https://numba.pydata.org                                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| numcpus                                    | https://github.com/tklauser/numcpus                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| numexpr                                    | https://github.com/pydata/numexpr                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| numpy                                      | https://numpy.org                                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| numpy-base                                 | https://numpy.org                                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| numpydoc                                   | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cublas-cu11                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cublas-cu12                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cuda-cupti-cu11                     | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cuda-cupti-cu12                     | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cuda-nvrtc-cu11                     | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cuda-nvrtc-cu12                     | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cuda-runtime-cu11                   | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cuda-runtime-cu12                   | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cudnn-cu11                          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cudnn-cu12                          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cufft-cu11                          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cufft-cu12                          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-curand-cu11                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-curand-cu12                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cusolver-cu11                       | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cusolver-cu12                       | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cusparse-cu11                       | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-cusparse-cu12                       | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-nccl-cu11                           | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-nccl-cu12                           | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-nvjitlink-cu12                      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-nvtx-cu11                           | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| nvidia-nvtx-cu12                           | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Oat++                                      | https://oatpp.io/                                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| oauthlib                                   | https://github.com/oauthlib/oauthlib                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ocl-icd                                    | https://github.com/OCL-dev/ocl-icd                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ocl-icd-system                             | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| olefile                                    | https://www.decalage.info/python/olefileio                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OmegaFold                                  | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| omnicanvas                                 | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OpenFF                                     | https://openforcefield.org/                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-amber-ff-ports                      | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-forcefields                         | https://openforcefield.org                                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-interchange                         | https://github.com/openforcefield/openff-interchange                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-models                              | https://github.com/openforcefield/openff-models                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-toolkit                             | https://openforcefield.org                                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-toolkit-base                        | https://openforcefield.org                                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-units                               | https://github.com/openforcefield/openff-units                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openff-utilities                           | https://github.com/openforcefield/openff-utilities                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openjpeg                                   | https://github.com/uclouvain/openjpeg                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openldap                                   | https://www.openldap.org/software/repo.html                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OpenMM                                     | https://openmm.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openmmtools                                | https://github.com/choderalab/openmmtools                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openmoltools                               | https://github.com/choderalab/openmoltools                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openpyxl                                   | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| openssl                                    | https://www.openssl.org                                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| opt-einsum                                 | https://github.com/dgasmith/opt_einsum                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OptKing                                    | https://github.com/psi-rking/optking                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| oscrypto                                   | https://github.com/wbond/oscrypto                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| overrides                                  | https://github.com/mkorpela/overrides                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| packaging                                  | https://github.com/pypa/packaging                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| packmol                                    | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pandas                                     | https://pandas.pydata.org                                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pandocfilters                              | http://github.com/jgm/pandocfilters                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                            |                                                                                     | Ъ                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Name of Project                            | Website                                                                             | Licen                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| panedr                                     | https://github.com/MDAnalysis/panedr                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pango                                      | https://pango.gnome.org                                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ParmEd                                     | https://parmed.github.io/ParmEd/html/index.html                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parser                                     | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| parso                                      | https://parso.readthedocs.io/en/latest/                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pathos                                     | https://github.com/uqfoundation/pathos                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| patsy                                      | https://patsy.readthedocs.io/en/latest/                                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pbkdf2                                     | https://golang.org/x/crypto/pbkdf2                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pbr                                        | https://docs.openstack.org/pbr/latest/                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pcmsolver                                  | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pcre                                       | https://www.pcre.org                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pcre2                                      | https://www.pcre.org                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pdb4amber                                  | https://github.com/Amber-MD/pdb4amber                                               | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pdbfixer                                   | https://github.com/openmm/pdbfixer                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pexpect                                    | https://pexpect.readthedocs.io/                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pgconn                                     | https://github.com/jackc/pgconn                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pgio                                       | https://github.com/jackc/pgio                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pgpassfile                                 | https://github.com/jackc/pgpassfile                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pgproto3                                   | https://github.com/jackc/pgproto3/v2                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pgtype                                     | https://github.com/jackc/pgtype                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pgx                                        | https://github.com/jackc/pgx/v4                                                     | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| phonopy                                    | https://github.com/phonopy/phono3py                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pickleshare                                | https://github.com/pickleshare/pickleshare                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pillow                                     | https://python-pillow.org                                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Pint                                       | https://pint.readthedocs.io/en/stable/                                              | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pip                                        | https://pip.pypa.io/                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pip-licenses                               | https://github.com/raimon49/pip-licenses                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pixman                                     | https://pixman.org                                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pkginfo                                    | https://launchpad.net/pkginfo                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| platformdirs                               | https://github.com/platformdirs/platformdirs                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| plotly                                     | https://plotly.com/python/                                                          | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| plotly-orca                                | https://github.com/plotly/orca                                                      | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| plotly.js                                  | https://github.com/plotly/plotly.js                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pluggy                                     | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pooch                                      | https://github.com/fatiando/pooch                                                   | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pox                                        | https://github.com/uqfoundation/pox                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ppft                                       | https://github.com/uqfoundation/ppft                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pq                                         | https://github.com/lib/pq                                                           | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ProDy                                      | http://www.csb.pitt.edu/ProDy                                                       | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| prometheus-client                          | https://github.com/prometheus/client_python                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| prompt-toolkit                             | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| protobuf                                   | https://google.golang.org/protobuf                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| psi4                                       | https://psicode.org                                                                 | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| psutil                                     | https://psutil.readthedocs.io/en/latest/                                            | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| psycopg2                                   | https://psycopg.org/                                                                | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PTable                                     | https://github.com/kxxoling/PTable                                                  | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pthread-stubs                              | https://xcb.freedesktop.org                                                         | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ptyprocess                                 | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pure-eval                                  | http://github.com/alexmojaki/pure_eval                                              | http://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|                                            |                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Name of Project                            | Website                                                                             | License                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| py                                         | https://py.readthedocs.io/en/latest/                                                | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| py-cpuinfo                                 | https://github.com/workhorsy/py-cpuinfo                                             | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyasn1                                     | https://github.com/etingof/pyasn1                                                   | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyasn1-modules                             | https://github.com/etingof/pyasn1-modules                                           | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pybind11-abi                               | https://github.com/pybind/pybind11                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pycairo                                    | https://pycairo.readthedocs.io/en/latest/index.html                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pycosat                                    | https://github.com/conda/pycosat                                                    | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pycparser                                  | https://github.com/eliben/pycparser                                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pydantic                                   | https://pydantic-docs.helpmanual.io                                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pydantic-core                              | https://github.com/pydantic/pydantic-core                                           | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyedr                                      | https://github.com/MDAnalysis/panedr                                                | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyEMMA                                     | http://github.com/markovmodel/PyEMMA                                                | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Pygments                                   | https://pygments.org                                                                | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pygraphviz                                 | https://pygraphviz.github.io                                                        | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pygtop                                     | https://pygtop.readthedocs.io/en/latest/                                            | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyHanko                                    | https://github.com/MatthiasValvekens/pyHanko                                        | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyhanko-certvalidator                      | https://github.com/MatthiasValvekens/certvalidator                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PyJWT                                      | https://github.com/jpadilla/pyjwt                                                   | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pymbar                                     | https://pymbar.org                                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyOpenSSL                                  | https://pyopenssl.org/                                                              | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyparsing                                  | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PyPDF3                                     | https://github.com/sfneal/PyPDF3                                                    | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyrsistent                                 | http://github.com/tobgu/pyrsistent/                                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pysam                                      | https://github.com/pysam-developers/pysam                                           | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PySocks                                    | https://github.com/Anorov/PySocks                                                   | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pytables                                   | https://www.pytables.org                                                            | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python                                     | https://www.python.org/                                                             | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python-bidi                                | https://github.com/MeirKriheli/python-bidi                                          | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python-constraint                          | https://github.com/python-constraint/python-constraint                              | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python-dateutil                            | https://dateutil.readthedocs.io                                                     | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python-json-logger                         | http://github.com/madzak/python-json-logger                                         | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python-ldap                                | https://www.python-ldap.org/                                                        | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python3-saml                               | https://github.com/onelogin/python3-saml                                            | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| python_abi                                 | https://github.com/conda-forge/python_abi-feedstock                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pytz                                       | https://pythonhosted.org/pytz                                                       | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pytz-deprecation-shim                      | https://github.com/pganssle/pytz-deprecation-shim                                   | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| PyWavelets                                 | https://github.com/PyWavelets/pywt                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| <b>PyYAML</b>                              | https://pyyaml.org/                                                                 | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| pyyml                                      | No longer available                                                                 | No license                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| pyzmq                                      | https://pyzmq.readthedocs.io/en/latest/                                             | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| qcelemental                                | https://github.com/MolSSI/QCElemental                                               | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| qcengine                                   | https://github.com/MolSSI/QCEngine                                                  | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| qrcode                                     | https://github.com/lincolnloop/python-qrcode                                        | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ramda                                      | https://github.com/ramda/ramda                                                      | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| rapidjson                                  | https://rapidjson.org/                                                              | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| rdkit                                      | https://www.rdkit.org                                                               | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| re2                                        | https://github.com/google/re2                                                       | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| readme-renderer                            | https://github.com/pypa/readme_renderer                                             | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| redis-py                                   | https://github.com/andymccurdy/redis-py                                             | https://                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

| Name of Project               | Website                                                          |
|-------------------------------|------------------------------------------------------------------|
| referencing                   | https://github.com/python-jsonschema/referencing                 |
| regex                         | https://github.com/mrabarnett/mrab-regex                         |
| reportlab                     | https://www.reportlab.com                                        |
| reproc                        | https://github.com/DaanDeMeyer/reproc                            |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                            |
| requests                      | https://requests.readthedocs.io                                  |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                    |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                 |
| resumable                     | https://github.com/stevvooe/resumable                            |
| retrying                      | https://github.com/rholder/retrying                              |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                    |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                        |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                    |
| rich                          | Orion Floes                                                      |
| rpds-py                       | https://github.com/crate-py/rpds                                 |
| rpmpack                       | https://github.com/google/rpmpack                                |
| rsa                           | https://stuvel.eu/rsa                                            |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/      |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/ |
| s3transfer                    | https://github.com/boto/s3transfer                               |
| sasl                          | https://mellium.im/sasl                                          |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                        |
| scikit-image                  | https://scikit-image.org                                         |
| scikit-learn                  | https://scikit-learn.org/stable/                                 |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra       |
| scipy                         | https://scipy.org                                                |
| seaborn                       | https://seaborn.pydata.org                                       |
| seaborn-base                  | https://seaborn.pydata.org                                       |
| semver                        | https://github.com/Masterminds/semver/v3                         |
| Send2Trash                    | https://github.com/arsenetar/send2trash                          |
| setuptools                    | https://github.com/pypa/setuptools                               |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                          |
| sh                            | https://github.com/amoffat/sh                                    |
| shellingham                   | https://github.com/sarugaku/shellingham                          |
| simint                        | https://www.bennyp.org/research/simint/                          |
| six                           | https://github.com/benjaminp/six                                 |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst               |
| snappy                        | https://github.com/google/snappy                                 |
| sniffio                       | https://github.com/python-trio/sniffio                           |
| snowballstemmer               | https://github.com/snowballstem/snowball                         |
| soupsieve                     | https://github.com/facelessuser/soupsieve                        |
| spglib                        | Orion Floes                                                      |
| sphinx                        | https://github.com/sphinx-doc/sphinx                             |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp            |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp              |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp             |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath               |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp               |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml      |

| Name of Project              | Website                                                  | License |
|------------------------------|----------------------------------------------------------|---------|
| SQLAlchemy                   | https://www.sqlalchemy.org                               | https:/ |
| sqlite                       | https://sqlite.org/index.html                            | https:/ |
| sqlparse                     | https://github.com/andialbrecht/sqlparse                 | https:/ |
| stack-data                   | https://github.com/alexmojaki/stack_data                 | https:/ |
| starfile                     | https://github.com/alisterburt/starfile                  | https:/ |
| statsmodels                  | https://github.com/statsmodels/statsmodels               | https:/ |
| structlog                    | https://www.structlog.org/                               | https:/ |
| svglib                       | https://github.com/deeplook/svglib                       | https:/ |
| sympy                        | https://sympy.org                                        | https:/ |
| tables                       | https://www.pytables.org/                                | https:/ |
| tabulate                     | https://github.com/astanin/python-tabulate               | https:/ |
| tbb                          | https://github.com/oneapi-src/oneTBB                     | https:/ |
| tenacity                     | https://github.com/jd/tenacity                           | https:/ |
| tensorboard                  | https://github.com/tensorflow/tensorboard                | https:/ |
| tensorboard-data-server      | https://github.com/tensorflow/tensorboard-data-server    | https:/ |
| tensorboard-plugin-wit       | https://github.com/pair-code/what-if-tool                | https:/ |
| tensorflow                   | https://github.com/tensorflow/tensorflow                 | https:/ |
| tensorflow-estimator         | https://github.com/tensorflow/estimator                  | https:/ |
| tensorflow-io-gcs-filesystem | https://github.com/tensorflow/io                         | https:/ |
| tensorflow-probability       | https://github.com/tensorflow/probability                | https:/ |
| termcolor                    | https://github.com/hugovk/termcolor                      | https:/ |
| terminado                    | https://github.com/jupyter/terminado                     | https:/ |
| testpath                     | https://github.com/jupyter/testpath                      | https:/ |
| textangular                  | https://github.com/fraywing/textAngular                  | https:/ |
| tf_keras                     | https://github.com/tensorflow/keras                      | https:/ |
| threadpoolctl                | https://github.com/joblib/threadpoolctl                  | https:/ |
| three                        | https://github.com/mrdoob/three.js                       | https:/ |
| tifffile                     | https://github.com/cgohlke/tifffile                      | https:/ |
| tinycss2                     | https://github.com/Kozea/tinycss2                        | https:/ |
| tinyxml2                     | https://github.com/leethomason/tinyxml2                  | https:/ |
| tk                           | https://www.tcl.tk/                                      | https:/ |
| toml                         | https://github.com/toml-lang/toml                        | https:/ |
| tomli                        | https://github.com/hukkin/tomli                          | https:/ |
| toolz                        | https://github.com/pytoolz/toolz                         | https:/ |
| torch                        | https://pytorch.org/                                     | https:/ |
| tornado                      | https://www.tornadoweb.org                               | https:/ |
| tqdm                         | https://github.com/tqdm/tqdm                             | https:/ |
| tracy                        | https://github.com/gear-genomics/tracy                   | https:/ |
| traitlets                    | https://github.com/ipython/traitlets                     | https:/ |
| triton                       | https://github.com/openai/triton                         | https:/ |
| truststore                   | https://github.com/orion-flores/truststore               | https:/ |
| ts-jest                      | https://github.com/kulshekhar/ts-jest                    | https:/ |
| ts-loader                    | https://github.com/TypeStrong/ts-loader                  | https:/ |
| twine                        | https://github.com/pypa/twine                            | https:/ |
| twinj uuid                   | https://github.com/twinj/uuid                            | https:/ |
| types                        | https://github.com/babel/babel                           | https:/ |
| typescript                   | https://github.com/Microsoft/TypeScript                  | https:/ |
| typing_extensions            | https://github.com/python/typing                         | https:/ |
| tzdata                       | https://github.com/python/tzdata                         | https:/ |
| Name of Project              | Website                                                  | License |
| tzlocal                      | https://github.com/regebro/tzlocal                       | https:/ |
| umi-tools                    | https://github.com/CGATOxford/UMI-tools                  | https:/ |
| unicodedata2                 | https://github.com/fonttools/unicodedata2                | https:/ |
| uritools                     | https://github.com/tkem/uritools/                        | https:/ |
| urllib3                      | https://urllib3.readthedocs.io/                          | https:/ |
| vine                         | https://github.com/celery/vine                           | https:/ |
| vue                          | https://github.com/vuejs/vue                             | https:/ |
| wcwidth                      | https://github.com/jquast/wcwidth                        | https:/ |
| webencodings                 | https://github.com/gsnedders/python-webencodings         | https:/ |
| websocket-client             | https://github.com/websocket-client/websocket-client.git | https:/ |
| Werkzeug                     | https://palletsprojects.com/p/werkzeug/                  | https:/ |
| westpa                       | Orion Floes                                              | http:// |
| wheel                        | https://github.com/pypa/wheel                            | https:/ |
| widgetsnbextension           | https://github.com/jupyter-widgets/ipywidgets#readme     | https:/ |
| wrapt                        | https://github.com/GrahamDumpleton/wrapt                 | https:/ |
| wsutil                       | https://github.com/yhat/wsutil                           | https:/ |
| x/lint                       | https://golang.org/x/lint                                | https:/ |
| x/mod                        | https://golang.org/x/mod/semver                          | https:/ |
| x/net                        | https://golang.org/x/net                                 | https:/ |
| x/oauth2                     | https://golang.org/x/oauth2                              | https:/ |
| x/sys                        | https://golang.org/x/sys                                 | https:/ |
| x/text                       | https://golang.org/x/text                                | https:/ |
| x/tools                      | https://golang.org/x/tools                               | https:/ |
| x/xerrors                    | https://golang.org/x/xerrors                             | https:/ |
| xhtml2pdf                    | http://github.com/xhtml2pdf/xhtml2pdf                    | https:/ |
| xlrd                         | https://github.com/python-excel/xlrd                     | https:/ |
| xmlsec                       | https://github.com/mehcode/python-xmlsec                 | https:/ |
| xmltodict                    | https://github.com/martinblech/xmltodict                 | https:/ |
| xorg-kbproto                 | https://gitlab.freedesktop.org/xorg/proto/kbproto        | https:/ |
| xorg-libice                  | https://gitlab.freedesktop.org/xorg/lib/libice           | https:/ |
| xorg-libsm                   | https://gitlab.freedesktop.org/xorg/lib/libsm            | https:/ |
| xorg-libx11                  | https://gitlab.freedesktop.org/xorg/lib/libx11           | https:/ |
| xorg-libxau                  | https://gitlab.freedesktop.org/xorg/lib/libxau           | https:/ |
| xorg-libxdmcp                | https://gitlab.freedesktop.org/xorg/lib/libxdmcp         | https:/ |
| xorg-libxext                 | https://gitlab.freedesktop.org/xorg/lib/libxext          | https:/ |
| xorg-libxrender              | https://gitlab.freedesktop.org/xorg/lib/libxrender       | https:/ |
| xorg-libxt                   | https://gitlab.freedesktop.org/xorg/lib/libxt            | https:/ |
| xorg-renderproto             | https://gitlab.freedesktop.org/xorg/proto/renderproto    | https:/ |
| xorg-xextproto               | https://gitlab.freedesktop.org/xorg/proto/xextproto      | https:/ |
| xorg-xproto                  | https://gitlab.freedesktop.org/xorg/proto/xproto         | https:/ |
| xxhash                       | https://github.com/cespare/xxhash/v2                     | https:/ |
| xz                           | https://github.com/ulikunitz/xz                          | https:/ |
| yaml                         | https://pyyaml.org/                                      | https:/ |
| yaml-cpp                     | https://github.com/jbeder/yaml-cpp                       | https:/ |
| yaml.v2                      | https://gopkg.in/yaml.v2                                 | https:/ |
| yaml.v3                      | https://gopkg.in/yaml.v3                                 | https:/ |
| yarl                         | https://github.com/aio-libs/yarl/                        | https:/ |
| yaspin                       | https://github.com/pavdmyt/yaspin                        | https:/ |
| yfiles                       | https://www.yworks.com/products/yfiles                   | comm    |
| Name of Project              | Website                                                  | License |
| yml                          | https://pypi.org/project/yml/                            | N/A     |
| zap                          | https://go.uber.org/zap                                  | https:/ |
| zipp                         | https://github.com/jaraco/zipp                           | https:/ |
| zlib                         | https://zlib.net/                                        | https:/ |
| zstandard                    | https://github.com/indygreg/python-zstandard             | https:/ |
| zstd                         | https://facebook.github.io/zstd/                         | https:/ |
| _libgcc_mutex                | https://github.com/conda-forge/_libgcc_mutex-feedstock   | https:/ |
| _openmp_mutex                | https://github.com/conda-forge/_openmp_mutex-feedstock   | https:/ |

# **10.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

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

# $\mathsf{A}$

AddFeature OEDocking:: OECustomConstraints, 96 AddLigand OEModels:: OEROCSOueryModelBuilder, 117 AddReceptor OEDocking:: OEPosit, 48 AddSmarts OEDocking:: OEFeature, 98 AddSphere OEDocking:: OEFeature, 97 AnnotatePose OEDocking:: OEDock, 41 OEDocking:: OEScore, 61

# <sub>B</sub>

Build OEModels:: OEROCSQueryModelBuilder, 117

# C

CacheScoringSetup OEDocking:: OEDock, 41 OEDocking:: OEScore, 61 Clear OEDocking:: OECustomConstraints, 96 ClearLigands OEModels:: OEROCSQueryModelBuilder, 117 ClearReceptors OEDocking:: OEPosit, 49 ClearSmarts OEDocking:: OEFeature, 98 ClearSpheres OEDocking:: OEFeature, 98 Constructor OEDocking:: OEDock, 38 OEDocking:: OEDockOptions, 37 OEDocking:: OEHybrid, 42 OEDocking:: OEMakeReceptorOptions, 43 OEDocking:: OEPoseOptimizer, 45

OEDocking:: OEPoseOptimizerOptions,  $46$ OEDocking:: OEPosit, 48 OEDocking:: OEPositOptions, 52 OEDocking:: OEPositProbability, 56 OEDocking:: OEScore, 58 OEDocking:: OEShapeFit, 85 OEDocking:: OEShapeFitOptions, 86 OEDocking:: OEShapeFitResults, 89 OEModels:: OEROCSQueryModelBuilder, 117 OEModels:: OEROCSQueryModelOptions, 118 Constructors OEDocking:: OEBox, 93 OEDocking:: OECustomConstraints, 95 OEDocking:: OEPositResults, 57 OEDocking:: OESinglePoseResult, 62 CreateCopy OEDocking:: OEAlignReceptorFunction, 90 OEDocking:: OEFeature, 99

# D

```
DeleteFeature
   OEDocking:: OECustomConstraints, 96
DeleteSmarts
   OEDocking:: OEFeature, 98
DeleteSphere
   OEDocking:: OEFeature, 97
Destructor
   OEDocking:: OEBoxBase, 91
   OEDocking:: OEFeature, 97
   OEDocking:: OESphereBase, 101
Dock
   OEDocking:: OEPosit, 49
dockmolecules.py
   Example Code, 19
DockMultiConformerMolecule
   OEDocking:: OEDock, 39
   OEDocking:: OEPosit, 50
```

## E

Estimate OEDocking:: OEPositProbability, 57 Example Code dockmolecules.py, 19 generatemultiplepose.py, 26 makereceptor.py, 28 posemolecules.py, 24 receptoroutercontourvolume.py, 29 rescoreposes.py, 21 rocsquerymodelbuilder.py, 35 setoutercontourvolume.py, 31 shapefit.py, 23 toggleinnercontour.py, 30

# F

Fit OEDocking:: OEShapeFit, 86

# G

generatemultiplepose.py Example Code, 26 GetAllowedClashType OEDocking:: OEPositOptions, 52 GetAtom OEDocking:: OEProteinConstraint, 99 GetAutoConstraints OEDocking:: OEMakeReceptorOptions, 43 GetBestReceptorPoseOnly OEDocking:: OEPositOptions, 52 GetBoxExtension OEDocking:: OEMakeReceptorOptions, 43 GetBoxMol OEDocking:: OEMakeReceptorOptions, 44 GetColorForceField OEModels:: OEROCSQueryModelOptions, 119 GetComponentNames OEDocking:: OEDock, 40 OEDocking:: OEScore, 59 GetDesignUnit OEDocking:: OESinglePoseResult, 63 GetEnabled OEDocking:: OEFeature, 99 OEDocking:: OEProteinConstraint, 100 GetExcludeSelf OEDocking:: OEPositOptions, 52 GetFeatureName OEDocking:: OEFeature, 99 GetFeatures OEDocking:: OECustomConstraints, 95 GetFlexiOverlapOptions OEDocking:: OEShapeFitOptions, 87 GetFlexiOverlayOptions

OEDocking:: OEPositOptions, 52 GetFlexRange OEDocking:: OEPoseOptimizerOptions, 46 GetForceField OEDocking:: OEPoseOptimizerOptions, 47 GetFullConformationSearch OEDocking:: OEPositOptions, 53 OEDocking:: OEShapeFitOptions, 87 GetHasClash OEDocking:: OESinglePoseResult, 63 GetHighScoresAreBetter OEDocking:: OEDock, 40 OEDocking:: OEPosit, 49 OEDocking:: OEScore, 59 GetIqnoreNitrogenStereo OEDocking:: OEPositOptions. 53 GetInvalidScore OEDocking:: OEPosit, 49 GetMaxLocalStrain OEDocking:: OEShapeFitOptions, 87 GetMaxMoleculesPerModel OEModels:: OEROCSQueryModelOptions, 119 GetMaxOptSteps OEDocking:: OEShapeFitOptions, 87 GetMergeColorAtoms OEModels:: OEROCSQueryModelOptions, 119 GetMinProbability OEDocking:: OEPositOptions, 53 GetName OEDocking:: OEDock, 40 OEDocking:: OEPosit, 49 OEDocking:: OEProteinConstraint, 100 OEDocking:: OEScore, 59 GetNegativeImageType OEDocking:: OEMakeReceptorOptions, 44 GetNonBondCutoff OEDocking:: OEPoseOptimizerOptions,  $47$ GetNumClashes OEDocking:: OESinglePoseResult, 64 GetNumContacts OEDocking:: OESinglePoseResult, 63 GetNumModels OEModels:: OEROCSQueryModelOptions, 119 GetNumPoses OEDocking:: OEPositResults, 58 GetPose OEDocking:: OEShapeFitResults, 89 OEDocking:: OESinglePoseResult, 64

GetPoserCacheCount OEDocking:: OEPositOptions, 53 GetPoseRelaxMode OEDocking:: OEPositOptions, 53 GetPoseRelaxOptions OEDocking:: OEPositOptions, 53 GetPositMethod OEDocking:: OESinglePoseResult, 64 GetPositMethods OEDocking:: OEPositOptions, 53 GetProbability OEDocking:: OESinglePoseResult, 64 GetRad OEDocking:: OESphereBase, 102 GetReceptorIndex OEDocking:: OESinglePoseResult, 64 GetRelaxAttempted OEDocking:: OESinglePoseResult, 64 GetRelaxed OEDocking:: OESinglePoseResult, 64 GetRelaxStatus OEDocking:: OESinglePoseResult, 65 GetRelaxStatusStr OEDocking:: OESinglePoseResult, 65 GetResolution OEDocking:: OEDockOptions, 37 GetReturnCode OEDocking:: OEPositResults, 58 GetRigidOverlayOptions OEDocking:: OEShapeFitOptions, 87 GetROCSQueryModelOptions OEModels:: OEROCSQueryModelBuilder, 118 GetScore OEDocking:: OEShapeFitResults, 90 GetScoreMethod OEDocking:: OEDockOptions, 37 GetSinglePoseResults OEDocking:: OEPositResults, 58 GetSmarts OEDocking:: OEFeature, 98 GetSpheres OEDocking:: OEFeature, 97 GetTargetMask OEDocking:: OEMakeReceptorOptions, 44 OEDocking:: OESinglePoseResult, 63 GetTargetPred OEDocking:: OEMakeReceptorOptions, 44 OEDocking:: OESinglePoseResult, 63 GetTorLib OEDocking:: OEPositOptions, 54 OEDocking:: OEShapeFitOptions, 87 GetType OEDocking:: OEProteinConstraint, 100

GetX OEDocking:: OESphereBase, 101 GetXMax OEDocking:: OEBox, 94 OEDocking:: OEBoxBase, 91 GetXMin OEDocking:: OEBox, 94 OEDocking:: OEBoxBase, 92 GetY OEDocking:: OESphereBase, 101 GetYMax OEDocking:: OEBox, 94 OEDocking:: OEBoxBase, 91 GetYMin OEDocking:: OEBox, 94 OEDocking:: OEBoxBase, 92 GetZ OEDocking:: OESphereBase, 101 GetZMax OEDocking:: OEBox, 94 OEDocking:: OEBoxBase, 92 GetZMin OEDocking:: OEBox, 94 OEDocking:: OEBoxBase, 92

# $\mathbf{I}$

Initialize OEDocking:: OEDock, 39 OEDocking:: OEPosit, 50 OEDocking:: OEScore, 59 IsInitialized OEDocking:: OEDock, 39 OEDocking:: OEPosit, 49 OEDocking:: OEScore, 59

## M

makereceptor.py Example Code, 28 MaxLocalStrain OEDocking:: OEShapeFitOptions, 88 MethodChoice OEDocking:: OEPosit, 50

# N

NumFeatures OEDocking:: OECustomConstraints, 96 NumSmarts OEDocking:: OEFeature, 98 NumSpheres OEDocking:: OEFeature, 97

# $\Omega$

OEDocking:: OEAddDockingInteractions, 76 OEDocking:: OEAlignReceptorFunction, 90

CreateCopy, 90 operator(), 90 SetupTarget, 90 OEDocking:: OEAlignReceptors, 102 OEDocking:: OEAllowedClashType, 65 OEDocking:: OEAllowedClashType:: ANY, 65 OEDocking:: OEAllowedClashType:: HYDROGEN, 65 OEDocking:: OEAllowedClashType:: NONE, 65 OEDocking:: OEBox, 92 Constructors, 93 GetXMax, 94 GetXMin, 94 GetYMax, 94 GetYMin, 94 GetZMax, 94 GetZMin, 94 operator=, 93 Setup, 95 OEDocking:: OEBoxArea, 102 OEDocking:: OEBoxBase, 91 Destructor, 91 GetXMax, 91 GetXMin. 92 GetYMax, 91 GetYMin. 92 GetZMax, 92 GetZMin, 92 operator=, 91 Setup, 92 OEDocking:: OEBoxExtend, 103 OEDocking:: OEBoxTranslate, 103 OEDocking:: OEBoxVolume, 103 OEDocking:: OEBoxXDim, 103 OEDocking:: OEBoxXMid. 103 OEDocking:: OEBoxYDim, 103 OEDocking:: OEBoxYMid, 104 OEDocking:: OEBoxZDim, 104 OEDocking:: OEBoxZMid, 104 OEDocking:: OECreateDUFromReceptorMol, 76 OEDocking:: OECustomConstraints, 95 AddFeature, 96 Clear, 96 Constructors, 95 DeleteFeature, 96 GetFeatures, 95 NumFeatures, 96 operator=, 95 OEDocking:: OEDock, 38 AnnotatePose, 41 CacheScoringSetup, 41 Constructor, 38 DockMultiConformerMolecule, 39

GetComponentNames, 40 GetHighScoresAreBetter, 40 GetName, 40 Initialize, 39 IsInitialized, 39 ScoreAtom, 40 ScoreAtomComponent, 41 ScoreLigand, 40 ScoreLigandComponent, 40 OEDocking:: OEDockingGetArch, 76 OEDocking:: OEDockingGetLicensee, 76 OEDocking:: OEDockingGetPlatform, 76 OEDocking:: OEDockingGetRelease, 77 OEDocking:: OEDockingGetSite, 77 OEDocking:: OEDockingGetVersion, 77 OEDocking:: OEDockingReturnCode, 65 OEDocking:: OEDockingReturnCode:: Aborted, 66 OEDocking::OEDockingReturnCode::ConformerGenError, 66 OEDocking::OEDockingReturnCode::CoordError, 66 OEDocking:: OEDockingReturnCode:: EmptyLigand, 66 OEDocking::OEDockingReturnCode::EmptyProtein, 66 OEDocking::OEDockingReturnCode::Failure, 66 OEDocking:: OEDockingReturnCode:: GridSetupError, 66 OEDocking::OEDockingReturnCode::InvalidScore, 67 OEDocking::OEDockingReturnCode::NoConstraintMatch, 67 OEDocking::OEDockingReturnCode::NotInitialized, 67 OEDocking::OEDockingReturnCode::NoValidNonClashPose 67 OEDocking::OEDockingReturnCode::NoValidPoses, 67 OEDocking::OEDockingReturnCode::OptimizationError, 67 OEDocking::OEDockingReturnCode::OutsideGrid, 67 OEDocking:: OEDockingReturnCode:: ScoreError, 68 OEDocking:: OEDockingReturnCode:: Success, 68 OEDocking::OEDockingReturnCode::TypingError, 68 OEDocking:: OEDockingReturnCodeGetName, 77 OEDocking:: OEDockMethod, 68 OEDocking:: OEDockMethod:: Chemgauss, 69

```
OEDocking:: OEDockMethod:: Chemgauss3.68
OEDocking:: OEDockMethod:: Chemgauss4, 69
OEDocking:: OEDockMethod:: Chemscore, 69
OEDocking:: OEDockMethod:: Default, 70
OEDocking:: OEDockMethod:: Hybrid, 69
OEDocking:: OEDockMethod:: Hybrid1, 69
OEDocking:: OEDockMethod:: Hybrid2, 69
OEDocking:: OEDockMethod:: INVALID, 70
OEDocking:: OEDockMethod:: PLP, 68
OEDocking:: OEDockMethod:: Shapegauss, 68
OEDocking:: OEDockMethodConfigure, 77
OEDocking:: OEDockMethodGetName, 77
OEDocking:: OEDockMethodGetValue, 78
OEDocking:: OEDockOptions, 37
   Constructor. 37
   GetResolution. 37
   GetScoreMethod, 37
   operator=, 37
   SetResolution. 38
   SetScoreMethod, 38
OEDocking:: OEFeature, 96
   AddSmarts, 98
   AddSphere, 97
   ClearSmarts.98
   ClearSpheres, 98
   CreateCopy, 99
   DeleteSmarts, 98
   DeleteSphere, 97
   Destructor, 97
   GetEnabled, 99
   GetFeatureName, 99
   GetSmarts. 98
   GetSpheres, 97
   NumSmarts, 98
   NumSpheres, 97
   operator=, 97
   SetEnabled, 99
   SetFeatureName, 98
OEDocking::OEGetEstimatedPositProbability, SetFlexRange, 47
       78
OEDocking:: OEGetPositMethod, 78
OEDocking:: OEHasClash, 78
OEDocking:: OEHybrid, 42
   Constructor, 42
OEDocking:: OEInBox, 104
OEDocking:: OEInSphere, 104
OEDocking:: OEIsReceptor, 104
OEDocking:: OEMakeBoxMolecule, 78
OEDocking:: OEMakeReceptor, 79
OEDocking:: OEMakeReceptorDeprecated, 104
OEDocking:: OEMakeReceptorOptions, 43
   Constructor, 43
   GetAutoConstraints. 43
   GetBoxExtension, 43
```

```
GetBoxMol, 44
   GetNegativeImageType, 44
   GetTargetMask, 44
   GetTargetPred, 44
   operator=, 43SetAutoConstraints, 44
   SetBoxExtension. 44
   SetBoxMol, 44
   SetNegativeImageType, 45
   SetTargetMask, 45
   SetTargetPred, 45
OEDocking:: OENegativeImageType, 70
OEDocking:: OENegativeImageType:: Default,
       70
OEDocking:: OENegativeImageType:: INVALID,
       70
OEDocking::OENegativeImageType::LargeShape,
       70
OEDocking::OENegativeImageType::SmallShape,
       70
OEDocking:: OENegativeImageType:: StandardShape,
       70
OEDocking:: OENegativeImageTypeConfigure,
       106
OEDocking:: OENegativeImageTypeGetName,
       79
OEDocking:: OENegativeImageTypeGetValue,
       79
OEDocking:: OEPoseOptimizer, 45
   Constructor, 45
   operator=, 46
   Optimize, 46
OEDocking:: OEPoseOptimizerOptions, 46
   Constructor, 46
   GetFlexRange, 46
   GetForceField, 47
   GetNonBondCutoff, 47
   operator=, 46
   SetForceField, 47
   SetNonBondCutoff, 47
OEDocking:: OEPoseRelaxMode, 71
OEDocking:: OEPoseRelaxMode:: ALL, 71
OEDocking:: OEPoseRelaxMode:: CLASHED, 71
OEDocking:: OEPoseRelaxMode:: NONE, 71
OEDocking:: OEPosit, 47
   AddReceptor, 48
   ClearReceptors, 49
   Constructor, 48
   Dock, 49
   DockMultiConformerMolecule, 50
   GetHighScoresAreBetter, 49
   GetInvalidScore, 49
   GetName, 49
```

Initialize, 50 IsInitialized. 49 MethodChoice, 50 operator=, 48 RankDesignUnits, 50 RankReceptors, 51 ScoreLigand, 51 OEDocking:: OEPositMethod, 71 OEDocking:: OEPositMethod:: ALL, 71 OEDocking:: OEPositMethod:: FRED, 71 OEDocking:: OEPositMethod:: HYBRID, 71 OEDocking:: OEPositMethod:: SHAPEFIT, 72 OEDocking:: OEPositMethod:: UNKNOWN, 72 OEDocking:: OEPositMethodGetName, 79 OEDocking:: OEPositOptions, 51 Constructor, 52 GetAllowedClashType, 52 GetBestReceptorPoseOnly, 52 GetExcludeSelf, 52 GetFlexiOverlayOptions, 52 GetFullConformationSearch, 53 GetIgnoreNitrogenStereo, 53 GetMinProbability, 53 GetPoserCacheCount. 53 GetPoseRelaxMode, 53 GetPoseRelaxOptions, 53 GetPositMethods, 53 GetTorLib, 54 operator= $, 52$ SetAllowedClashType, 54 SetBestReceptorPoseOnly, 54 SetExcludeSelf, 54 SetFlexiOverlayOptions, 54 SetFullConformationSearch, 55 SetIqnoreNitrogenStereo.55 SetMinProbability, 55 SetPoserCacheCount, 55 SetPoseRelaxMode, 55 SetPoseRelaxOptions, 56 SetPositMethods, 56 SetTorLib, 56 OEDocking:: OEPositProbability, 56 Constructor, 56 Estimate, 57 operator=, 57 PoseEstimate, 57 SetupRef, 57 OEDocking:: OEPositResults, 57 Constructors, 57 GetNumPoses, 58 GetReturnCode.58 GetSinglePoseResults, 58 operator=, 58 OEDocking:: OEProteinConstraint, 99

GetAtom, 99 GetEnabled. 100 GetName, 100 GetType, 100 SetAtom, 100 SetEnabled, 100 SetName. 100 SetType, 100 OEDocking:: OEProteinConstraintType, 72 OEDocking:: OEProteinConstraintType:: Acceptor, 72 OEDocking:: OEProteinConstraintType:: Chelator, 72 OEDocking::OEProteinConstraintType::Contact, 72 OEDocking::OEProteinConstraintType::Donor, 72 OEDocking:: OEProteinConstraintType:: Lipophilic, 72 OEDocking:: OEProteinConstraintType:: Unknown,  $73$ OEDocking:: OEReadReceptorFile, 107 OEDocking:: OEReadReceptorFromBytes, 107 OEDocking:: OEReceptorAddCachedScore, 108 OEDocking:: OEReceptorAddExtraMol, 108 OEDocking:: OEReceptorClear, 108 OEDocking:: OEReceptorClearBoundLigand, 108 OEDocking::OEReceptorClearCachedScore, 109 OEDocking:: OEReceptorClearCustomConstraints, 109 OEDocking:: OEReceptorClearExtraMols, 109 OEDocking::OEReceptorClearProteinConstraint, 109 OEDocking:: OEReceptorClearProteinConstraints, 109 OEDocking:: OEReceptorGetBoundLigand, 109 OEDocking:: OEReceptorGetCustomConstraints, 110 OEDocking:: OEReceptorGetExtraMols, 110 OEDocking:: OEReceptorGetInnerContourLevel, 110 OEDocking:: OEReceptorGetNegativeImageGrid, 110 OEDocking::OEReceptorGetOuterContourLevel, 110 OEDocking:: OEReceptorGetProteinConstraints, 111 OEDocking:: OEReceptorHasBoundLigand, 111 OEDocking:: OEReceptorHasCachedScore, 111 OEDocking:: OEReceptorHasCustomConstraints, 111 OEDocking:: OEReceptorHasExtraMols, 111

OEDocking::OEReceptorHasInnerContourLeve@EDocking::OESearchResolutionConfigure, 111 114 OEDocking::OEReceptorHasNegativeImageGridEDocking::OESearchResolutionGetName, 112  $80$ OEDocking::OEReceptorHasOuterContourLeve@EDocking::OESearchResolutionGetValue, 112  $80$ OEDocking:: OEReceptorHasProteinConstrain0EDocking:: OESetEnergyScore, 80 OEDocking:: OESetEnergyScoreComponent, 112 OEDocking:: OEReceptorSetBoundLigand, 112 81 OEDocking:: OEReceptorSetCachedScore, 112 OEDocking:: OESetScore, 83 OEDocking::OEReceptorSetCustomConstraint@EDocking::OESetScoreComponent, 84 OEDocking:: OESetSDScore, 82 113 OEDocking::OEReceptorSetInnerContourLeveQEDocking::OESetSDScoreComponent, 82 OEDocking:: OESetupBox, 85, 114 113 OEDocking::OEReceptorSetOuterContourLeveOEDocking::OESetupBoxCenterAndExtents, 115 113 OEDocking:: OEReceptorSetProteinConstrainOEDocking:: OEShapeFit, 85 113 Constructor, 85 OEDocking:: OEScore, 58  $Fit.86$ AnnotatePose, 61 operator=, 85 CacheScoringSetup, 61 SetupRef, 86 Constructor, 58 OEDocking:: OEShapeFitOptions, 86 GetComponentNames, 59 Constructor, 86 GetHighScoresAreBetter, 59 GetFlexiOverlapOptions, 87 GetName, 59 GetFullConformationSearch, 87 GetMaxLocalStrain. 87 Initialize.59 IsInitialized, 59 GetMaxOptSteps, 87 ScoreAtom, 60 GetRigidOverlayOptions, 87 ScoreAtomComponent, 60 GetTorLib, 87 ScoreLigand, 59 MaxLocalStrain, 88 ScoreLigandComponent, 60 operator=, 87 SetFlexiOverlapOptions, 88 SystematicSolidBodyOptimize, 60 OEDocking:: OEScoreType, 73 SetFullConformationSearch, 88 OEDocking:: OEScoreType:: Chemgauss, 73 SetMaxLocalStrain, 88 OEDocking:: OEScoreType:: Chemgauss3.73 SetMaxOptSteps, 88 OEDocking:: OEScoreType:: Chemgauss4,73 SetRigidOverlayOptions, 89 OEDocking::OEScoreType::Chemscore, 73 SetTorLib, 88 OEDocking:: OEScoreType:: Default, 74 OEDocking:: OEShapeFitResults, 89 OEDocking:: OEScoreType:: INVALID, 74 Constructor, 89 OEDocking:: OEScoreType:: PLP, 73 GetPose, 89 OEDocking:: OEScoreType:: Shapeqauss, 73 GetScore, 90 OEDocking:: OEScoreTypeConfigure, 113 operator=, 89 OEDocking:: OEScoreTypeGetName, 79 OEDocking:: OESinglePoseResult, 62 OEDocking:: OEScoreTypeGetValue, 80 Constructors, 62 OEDocking:: OESearchResolution, 74 GetDesignUnit, 63 OEDocking::OESearchResolution::Default, GetHasClash, 63 75 GetNumClashes, 64 OEDocking::OESearchResolution::High, 74 GetNumContacts, 63 OEDocking::OESearchResolution::INVALID, GetPose, 64 75 GetPositMethod, 64 OEDocking::OESearchResolution::Low, 75 GetProbability, 64 OEDocking:: OESearchResolution:: Standard, GetReceptorIndex, 64 74 GetRelaxAttempted, 64 GetRelaxed, 64

GetRelaxStatus, 65 GetRelaxStatusStr, 65 GetTargetMask, 63 GetTargetPred, 63 operator= $, 63$ OEDocking:: OESphereArea, 115 OEDocking:: OESphereBase, 101 Destructor, 101 GetRad. 102 GetX, 101 GetY, 101 GetZ, 101 operator=, 101 SetCenter, 102 SetRad. 102 OEDocking:: OESphereVolume, 115 OEDocking:: OEWriteReceptorFile, 115 OEDocking:: OEWriteReceptorToBytes, 115 OEModels:: OEROCSQueryModelBuilder, 116 AddLigand, 117 Build, 117 ClearLigands, 117 Constructor, 117 GetROCSQueryModelOptions, 118 operator= $, 117$ SetLigands, 118 OEModels:: OEROCSQueryModelOptions, 118 Constructor, 118 GetColorForceField, 119 GetMaxMoleculesPerModel, 119 GetMergeColorAtoms, 119 GetNumModels, 119 operator=, 119 SetColorForceField, 119 SetMaxMoleculesPerModel, 120 SetMergeColorAtoms, 119 SetNumModels, 120 operator() OEDocking:: OEAlignReceptorFunction, 90 operator= OEDocking:: OEBox, 93 OEDocking:: OEBoxBase, 91 OEDocking:: OECustomConstraints, 95 OEDocking:: OEDockOptions, 37 OEDocking:: OEFeature, 97 OEDocking:: OEMakeReceptorOptions, 43 OEDocking:: OEPoseOptimizer, 46 OEDocking:: OEPoseOptimizerOptions, 46 OEDocking:: OEPosit, 48 OEDocking:: OEPositOptions, 52 OEDocking:: OEPositProbability, 57 OEDocking:: OEPositResults, 58

OEDocking:: OEShapeFit, 85 OEDocking:: OEShapeFitOptions, 87 OEDocking:: OEShapeFitResults, 89 OEDocking:: OESinglePoseResult, 63 OEDocking:: OESphereBase, 101 OEModels:: OEROCSQueryModelBuilder, 117 OEModels:: OEROCSQueryModelOptions, 119 Optimize OEDocking:: OEPoseOptimizer, 46

## P

PoseEstimate OEDocking:: OEPositProbability, 57 posemolecules.py Example Code, 24

# R.

RankDesignUnits OEDocking:: OEPosit, 50 RankReceptors OEDocking:: OEPosit, 51 receptoroutercontourvolume.py Example Code, 29 rescoreposes.py Example Code, 21 rocsquerymodelbuilder.py Example Code, 35

# S

ScoreAtom OEDocking:: OEDock, 40 OEDocking:: OEScore, 60 ScoreAtomComponent OEDocking:: OEDock, 41 OEDocking:: OEScore, 60 ScoreLigand OEDocking:: OEDock, 40 OEDocking:: OEPosit, 51 OEDocking:: OEScore, 59 ScoreLigandComponent OEDocking:: OEDock, 40 OEDocking:: OEScore, 60 SetAllowedClashType OEDocking:: OEPositOptions, 54 SetAtom OEDocking:: OEProteinConstraint, 100 SetAutoConstraints OEDocking:: OEMakeReceptorOptions, 44 SetBestReceptorPoseOnly OEDocking:: OEPositOptions, 54 SetBoxExtension OEDocking:: OEMakeReceptorOptions, 44 SetBoxMol OEDocking:: OEMakeReceptorOptions, 44 SetCenter OEDocking:: OESphereBase, 102 SetColorForceField OEModels:: OEROCSQueryModelOptions, 119 SetEnabled OEDocking:: OEFeature, 99 OEDocking:: OEProteinConstraint, 100 SetExcludeSelf OEDocking:: OEPositOptions, 54 SetFeatureName OEDocking:: OEFeature, 98 SetFlexiOverlapOptions OEDocking:: OEShapeFitOptions, 88 SetFlexiOverlayOptions OEDocking:: OEPositOptions, 54 SetFlexRange OEDocking:: OEPoseOptimizerOptions, 47 SetForceField OEDocking:: OEPoseOptimizerOptions, 47 SetFullConformationSearch OEDocking:: OEPositOptions, 55 OEDocking:: OEShapeFitOptions, 88 SetIgnoreNitrogenStereo OEDocking:: OEPositOptions, 55 SetLigands OEModels:: OEROCSQueryModelBuilder, 118 SetMaxLocalStrain OEDocking:: OEShapeFitOptions, 88 SetMaxMoleculesPerModel OEModels:: OEROCSQueryModelOptions, 120 SetMaxOptSteps OEDocking:: OEShapeFitOptions, 88 SetMergeColorAtoms OEModels:: OEROCSQueryModelOptions, 119 SetMinProbability OEDocking:: OEPositOptions, 55 SetName OEDocking:: OEProteinConstraint, 100 SetNegativeImageType OEDocking:: OEMakeReceptorOptions, 45 SetNonBondCutoff OEDocking:: OEPoseOptimizerOptions, 47 SetNumModels OEModels:: OEROCSQueryModelOptions, 120

setoutercontourvolume.pv Example Code, 31 SetPoserCacheCount OEDocking:: OEPositOptions, 55 SetPoseRelaxMode OEDocking:: OEPositOptions, 55 SetPoseRelaxOptions OEDocking:: OEPositOptions, 56 SetPositMethods OEDocking:: OEPositOptions, 56 SetRad OEDocking:: OESphereBase, 102 SetResolution OEDocking:: OEDockOptions, 38 SetRigidOverlayOptions OEDocking:: OEShapeFitOptions, 89 SetScoreMethod OEDocking:: OEDockOptions, 38 SetTargetMask OEDocking:: OEMakeReceptorOptions, 45 SetTargetPred OEDocking:: OEMakeReceptorOptions, 45 SetTorLib OEDocking:: OEPositOptions, 56 OEDocking:: OEShapeFitOptions, 88 SetType OEDocking:: OEProteinConstraint, 100 Setup OEDocking:: OEBox, 95 OEDocking:: OEBoxBase, 92 SetupRef OEDocking:: OEPositProbability, 57 OEDocking:: OEShapeFit, 86 SetupTarget OEDocking:: OEAlignReceptorFunction, 90 shapefit.py Example Code, 23 SystematicSolidBodyOptimize OEDocking:: OEScore, 60

# Т

toggleinnercontour.py Example Code, 30