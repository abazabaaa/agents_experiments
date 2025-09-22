![](_page_0_Picture_0.jpeg)

Szybki TK - Python

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1 Introduction                    | 1  |
|-----------------------------------|----|
| 2 Theory                          | 3  |
| 2.1 SZYBKI Theory                 | 3  |
| 2.1.1 Force Field                 | 3  |
| 2.1.2 Entropy evaluation          | 3  |
| 2.2 freeform Theory               | 4  |
| 2.2.1 Conformer Free Energies     | 4  |
| 2.2.2 Solvation energy estimation | 5  |
| 3 API                             | 11 |
| 3.1 OESz Classes                  | 11 |
| 3.1.1 OESzybki                    | 11 |
| 3.1.2 SetTorsionConstraint        | 15 |
| 3.1.3 UnsetProtein                | 15 |
| 3.1.4 OESzybkiOptions             | 17 |
| 3.1.5 OESzybkiGeneralOptions      | 19 |
| 3.1.6 OESzybkiOptOptions          | 21 |
| 3.1.7 OESzybkiSolventOptions      | 23 |
| 3.1.8 OESzybkiProteinOptions      | 25 |
| 3.1.9 OESzybkiResults             | 28 |
| 3.1.10 OESzybkiEnsembleResults    | 33 |
| 3.1.11 OEProteinFlexOptions       | 35 |
| 3.1.12 OEProteinLigandOptOptions  | 36 |
| 3.1.13 OEProteinLigandOptResults  | 39 |
| 3.1.14 OEFreeFormConf             | 41 |
| 3.1.15 OEFreeFormConfAdvanced     | 42 |
| 3.1.16 OEFreeFormConfOptions      | 44 |
| 3.1.17 SetCorrSolventOptions      | 46 |
| 3.1.18 OEFreeFormSolvOptions      | 48 |
| 3.1.19 OEFreeFormSolvResults      | 50 |
| 3.1.20 OERestrictionEnergyResult  | 52 |
| 3.1.21 OESingleConfResult         | 52 |
| 3.1.22 OEFreeFormConfResults      | 55 |
| 3.1.23 OETorsionScanOptions       | 56 |
| 3.1.24 OETorsionScanResult        | 61 |
| 3.1.25 OETorsionScanner           | 62 |
| 3.1.26 GetLowestEnergyConfs       | 63 |
| 3.1.27 GetLowestEnergyResults     | 63 |
| 3.1.28 GetScannedAngles           | 63 |

| Section | Title                                  | Page |
|---------|----------------------------------------|------|
| 3.1.29  | GetSinglePointConfs                    | 63   |
| 3.1.30  | Scan                                   | 63   |
| 3.1.31  | OEBoundEntropyOptions                  | 63   |
| 3.1.32  | OELigandEntropyOptions                 | 64   |
| 3.1.33  | OEEntropyResults                       | 66   |
| 3.2     | OESz Constants                         | 67   |
| 3.2.1   | OEEntropyMethod                        | 67   |
| 3.2.2   | OEEnvType                              | 68   |
| 3.2.3   | OEForceFieldType                       | 69   |
| 3.2.4   | OEOptType                              | 71   |
| 3.2.5   | OEPotentialTerms                       | 72   |
| 3.2.6   | OEProteinElectrostatics                | 78   |
| 3.2.7   | OERunType                              | 79   |
| 3.2.8   | OESolventModel                         | 79   |
| 3.2.9   | OEAtomicRadii                          | 80   |
| 3.2.10  | OEProtFlex                             | 80   |
| 3.2.11  | OEFreeFormIonicState                   | 81   |
| 3.2.12  | OEFreeFormReturnCode                   | 82   |
| 3.2.13  | OEFreeFormWarning                      | 84   |
| 3.3     | OESz Functions                         | 85   |
| 3.3.1   | OEEstimateConfFreeEnergies             | 85   |
| 3.3.2   | OEEstimateSolvFreeEnergy               | 85   |
| 3.3.3   | OEGetEnergyTermName                    | 86   |
| 3.3.4   | OEGetFreeFormError                     | 86   |
| 3.3.5   | OEGetSzybkiError                       | 86   |
| 3.3.6   | OESzybkiGetArch                        | 86   |
| 3.3.7   | OESzybkiGetLicensee                    | 86   |
| 3.3.8   | OESzybkiGetPlatform                    | 86   |
| 3.3.9   | OESzybkiGetRelease                     | 86   |
| 3.3.10  | OESzybkiGetSite                        | 87   |
| 3.3.11  | OESzybkiGetVersion                     | 87   |
| 3.3.12  | OETorsionScan                          | 87   |
| 3.3.13  | OEBoundLigandEntropy                   | 88   |
| 3.3.14  | OELigandEntropy                        | 88   |
| 4       | Preliminary API                        | 91   |
| 4.1     | OESz Classes                           | 91   |
| 4.1.1   | OEFixedProteinLigandOptimizer          | 91   |
| 4.1.2   | Energy                                 | 92   |
| 4.1.3   | Optimize                               | 92   |
| 4.1.4   | SetProtein                             | 92   |
| 4.1.5   | OEFlexProteinLigandOptimizer           | 92   |
| 4.1.6   | Energy                                 | 93   |
| 4.1.7   | Optimize                               | 93   |
| 4.2     | OESz Constants                         | 94   |
| 4.2.1   | OEComplexFFType                        | 94   |
| 4.2.2   | OELigandChargeType                     | 95   |
| 4.2.3   | OEOptimizationType                     | 95   |
| 4.2.4   | OESzybkiReturnCode                     | 96   |
| 5       | Examples: Working with Szybki TK       | 99   |
| 5.1     | Ligand Energetics and Optimization     | 99   |
| 5.1.1   | Single ligand in vacuum                | 99   |
| 5.1.2   | Single ligand in vacuum using SMIRNOFF | 100  |

| Section         | Description                                                             | Page |
|-----------------|-------------------------------------------------------------------------|------|
| 5.1.3           | Optimization of a set of ligands                                        | 10   |
| 5.1.4           | Optimization of a single ligand with the Newton-Raphson method          | 10   |
| 5.1.5           | Optimization of all conformers of a ligand                              | 10   |
| 5.1.6           | Optimization of a single bound ligand                                   | 10   |
| 5.2             | Protein-Ligand Energetics and Optimization                              | 10   |
| 5.2.1           | Optimization of a set of bound ligands in a rigid receptor              | 10   |
| 5.2.2           | Optimization of a set of bound ligands in a partially flexible receptor | 11   |
| 5.2.3           | Optimization of a bound ligand in a partially flexible receptor         | 11   |
| 5.2.4           | Estimation of PB binding for a set of ligands                           | 11   |
| 5.2.5           | Optimization of a bound ligand using Newton-Raphson method              | 12   |
| 5.3             | DU Protein-Ligand Optimization with FF14SB-Parsley                      | 12   |
| 5.3.1           | Optimization of ligand in a rigid active site                           | 12   |
| 5.3.2           | Optimization of ligand in a partially flexible active site              | 12   |
| 5.4             | Entropy estimation                                                      | 12   |
| 5.4.1           | Estimation of solution ligand entropy                                   | 12   |
| 5.4.2           | Estimation of bound ligand entropy                                      | 12   |
| 5.5             | Solvation free energy estimation                                        | 12   |
| 5.6             | Conformations free energy estimation                                    | 12   |
| 5.6.1           | Simple free energy estimation                                           | 13   |
| 5.6.2           | Simple restriction energy estimation                                    | 13   |
| 5.6.3           | Advanced free energy estimation                                         | 13   |
| 5.6.4           | Advanced restriction energy estimation                                  | 13   |
| 5.6.5           | Finding similar conformers                                              | 13   |
| 5.6.6           | Torsion scan                                                            | 13   |
| Release History |                                                                         |      |
| 6               | Release History                                                         | 13   |
| 6.1             | Szybki TK 2.8.0                                                         | 13   |
| 6.1.1           | New features                                                            | 13   |
| 6.2             | Szybki TK 2.7.1                                                         | 13   |
| 6.3             | Szybki TK 2.7.0                                                         | 13   |
| 6.3.1           | New features                                                            | 14   |
| 6.3.2           | Major bug fixes                                                         | 14   |
| 6.3.3           | Minor bug fixes                                                         | 14   |
| 6.4             | Szybki TK 2.6.0.1                                                       | 14   |
| 6.5             | Szybki TK 2.6.0.0                                                       | 14   |
| 6.5.1           | New features                                                            | 14   |
| 6.5.2           | Major bug fixes                                                         | 14   |
| 6.5.3           | Minor bug fixes                                                         | 14   |
| 6.6             | Szybki TK 2.5.1.2                                                       | 14   |
| 6.7             | Szybki TK 2.5.1.1                                                       | 14   |
| 6.7.1           | New features                                                            | 14   |
| 6.7.2           | Major bug fixes                                                         | 14   |
| 6.7.3           | Minor bug fixes                                                         | 14   |
| 6.8             | Szybki TK 2.5.0                                                         | 14   |
| 6.8.1           | New Features                                                            | 14   |
| 6.9             | Szybki TK 2.4.0                                                         | 14   |
| 6.9.1           | New features                                                            | 14   |
| 6.9.2           | Minor bug fixes                                                         | 14   |
| 6.10            | Szybki TK 2.3.1                                                         | 14   |
| 6.10.1          | New features                                                            | 14   |
| 6.11            | Szybki TK 2.3.0                                                         | 14   |
| 6.11.1          | New features                                                            | 14   |
| 6.11.2          | Minor bug fixes                                                         | 14   |
| 6.12            | Szybki TK 2.2.0                                                         | 14   |

| 6.12.1 New features                  | 14 |
|--------------------------------------|----|
| 6.12.2 Major bug fixes               | 14 |
| 6.12.3 Minor bug fixes               | 14 |
| 6.13 Szybki TK 2.1.0                 | 14 |
| 6.13.1 New features                  | 14 |
| 6.13.2 Minor bug fixes               | 14 |
| 6.13.3 Documentation changes         | 14 |
| 6.14 Szybki TK 2.0.4                 | 14 |
| 6.14.1 Major bug fixes               | 14 |
| 6.14.2 Minor bug fixes               | 14 |
| 6.15 Szybki TK 2.0.3                 | 14 |
| 6.15.1 New features                  | 14 |
| 6.15.2 Documentation changes         | 14 |
| 6.16 Szybki TK 2.0.2                 | 14 |
| 6.16.1 New features                  | 14 |
| 6.16.2 Minor bug fixes               | 14 |
| 6.17 Szybki TK 2.0.1                 | 14 |
| 6.17.1 Minor bug fixes               | 14 |
| 6.18 Szybki TK 2.0.0                 | 14 |
| 6.18.1 Minor bug fixes               | 14 |
| 6.18.2 Documentation changes         | 14 |
| 6.19 Szybki TK 1.9.2                 | 14 |
| 6.19.1 New features                  | 14 |
| 6.19.2 Minor bug fixes               | 15 |
| 6.20 Szybki TK 1.9.1                 | 15 |
| 6.20.1 New features                  | 15 |
| 6.20.2 Minor bug fixes               | 15 |
| 6.20.3 Documentation fixes           | 15 |
| 6.21 Szybki TK 1.9.0                 | 15 |
| 6.21.1 New features                  | 15 |
| 6.21.2 Minor bug fixes               | 15 |
| 6.22 Szybki TK 1.8.7                 | 15 |
| 6.22.1 New features                  | 15 |
| 6.22.2 Major bug fixes               | 15 |
| 6.22.3 Minor bug fixes               | 15 |
| 6.23 Szybki TK 1.8.6                 | 15 |
| 6.23.1 Major bug fixes               | 15 |
| 6.23.2 Minor bug fixes               | 15 |
| 6.23.3 Documentation fixes           | 15 |
| 6.24 Szybki TK 1.8.5                 | 15 |
| 6.24.1 New features                  | 15 |
| 6.24.2 Major bug fixes               | 15 |
| 6.24.3 Minor bug fixes               | 15 |
| 6.24.4 Documentation fixes           | 15 |
| 6.25 Szybki TK 1.8.4                 | 15 |
| 6.25.1 New features                  | 15 |
| 6.25.2 Major bug fixes               | 15 |
| 6.25.3 Minor bug fixes               | 15 |
| 6.25.4 API Changes                   | 15 |
| 6.25.5 Documentation fixes           | 15 |
| 6.25.6 Java- and C#-specific changes | 15 |
| 6.26 Szybki TK 1.8.3                 | 15 |
| 6.26.1 New features                  | 15 |
| 6.26.2 Major bug fixes               | 15 |

| 6.26.3  Minor bug fixes        | 15 |
|--------------------------------|----|
| 6.26.4  Documentation fixes    | 15 |
| 6.27  Szybki TK 1.8.2          | 15 |
| 6.27.1  New features           | 15 |
| 6.27.2  Major bug fixes        | 15 |
| 6.27.3  Minor bug fixes        | 15 |
| 6.27.4  Documentation fixes    | 15 |
| 6.28  Szybki TK 1.8.1          | 15 |
| 6.28.1  New features           | 15 |
| 6.28.2  Major bug fixes        | 15 |
| 6.28.3  Minor bug fixes        | 15 |
| 6.28.4  Documentation fixes    | 15 |
| 6.29  Szybki TK 1.7.5          | 15 |
| 6.29.1  New features           | 15 |
| 6.29.2  Minor bug fixes        | 15 |
| 6.30  Szybki TK 1.7.4          | 16 |
| 6.30.1  Bug fixes              | 16 |
| 6.31  Szybki TK 1.7.3          | 16 |
| 6.31.1  New features           | 16 |
| 6.31.2  Major bug fixes        | 16 |
| 6.31.3  Minor bug fixes        | 16 |
| 6.32  Szybki TK 1.7.2          | 16 |
| 6.32.1  New features           | 16 |
| 6.32.2  Major bug fixes        | 16 |
| 6.32.3  Minor bug fixes        | 16 |
| 6.33  Szybki TK 1.7.1          | 16 |
| 6.33.1  New features           | 16 |
| 6.33.2  Bug fixes              | 16 |
| 6.34  Szybki TK 1.7.0          | 16 |
| 6.34.1  New features           | 16 |
| 6.34.2  Bug fixes              | 16 |
| 6.35  Szybki TK 1.6.0          | 16 |
| 6.35.1  New features           | 16 |
| 6.35.2  Bug fixes              | 16 |
| 6.36  Szybki TK 1.5.0          | 16 |
| 6.36.1  New features           | 16 |
| 6.36.2  Bug fixes              | 16 |
| 6.37  Szybki TK 1.4.0          | 16 |
| 6.37.1  New features           | 16 |
| 6.37.2  Bug fixes              | 16 |
| 6.38  Szybki TK 1.3.4          | 16 |
| 6.38.1  New features           | 16 |
| 6.38.2  Bug fixes              | 16 |
| 7  Copyright and Trademarks    | 16 |
| 8  Sample Code                 | 16 |
| 9  Citation                    | 17 |
| 9.1  Orion ® Floes             | 17 |
| 9.2  Toolkits and Applications | 17 |
| 9.3  OpenEye Web Services      | 17 |
| 10  Technology Licensing       | 17 |

| 10.1.1  GCC RUNTIME LIBRARY EXCEPTION | 190 |
|---------------------------------------|-----|
| 10.1.2  GNU GENERAL PUBLIC LICENSE    | 192 |

### **Index**

# **ONE**

# **INTRODUCTION**

The Szybki Toolkit library provides a facility for force field based optimization and thermodynamic property estimations of small molecule ligands or protein-ligand complexes with small molecule ligands.

The following basic functionalities are available:

- Entropy Evaluation (see *Entropy evaluation* chapter)
- Conformer free Energies (see Conformer Free Energies chapter)
- Solvation free Energies (see Solvation energy estimation chapter)

### Note: Units of energy in various Szybki TK outputs are in kcal/mol.

The aim of this manual is to familiarize the user with the Szybki Toolkit functionalities, however, it does not provide explanations of basic OEChem classes and functions. Therefore reading the OEChem manual beforehand is highly recommended.

### See also:

- Python Quick Start Manual for installation instructions.
- Importing Python Toolkits section

# **TWO**

# **THEORY**

## 2.1 SZYBKI Theory

### 2.1.1 Force Field

Theory documentation for forcefields is available from OEFF theory.

### 2.1.2 Entropy evaluation

Ligand entropy is evaluated as a sum of configurational entropy  $(S_c)$  and solvation entropy  $(\Delta S_s)$ :

$$
S = S_c + \Delta S_s
$$

## **Configurational entropy**

Configurational entropy is calculated as:

$$
S_c = kN \left[ 1 + \ln \left( \frac{q}{N} \right) + \frac{T}{q} \frac{\partial q}{\partial T} \right]
$$

where q is the conformation dependent partition function:

$$
q = q_t \sum_{i=1}^{n_c} e^{-\frac{\epsilon_i}{kT}} q_{iv} q_{ii}
$$

Here  $q_t$ ,  $q_{ir}$  and  $q_{iv}$  are the translational, rotational and vibrational partition functions respectively,  $n_c$  is the number of unique conformations in the ensemble. All 3 partition functions are calculated from the classical statistical mechanics expressions which could be found in [McQuarrie-1976]. Vibrational frequencies for each conformation, needed for evaluation of  $q_{ir}$  are derived from diagonalization of a Hessian matrix obtained from Quasi-Newton optimization when convergence is achieved. Eigenvalues  $\lambda_i$  of the mass-weighted Hessian:

$$
\mathbf{H}^m=\mathbf{M}^{-1/2}\mathbf{H}\mathbf{M}^{-1/2}
$$

are converted into wavenumbers  $\tilde{\nu}_i$  according to:

$$
\tilde{\nu}_i = \frac{1}{2\pi c} \sqrt{\lambda_i}
$$

#### **Solvation entropy**

Solvation entropy is split into electrostatic and hydrophobic parts:

$$
\Delta S_s = \Delta S_{s, elec} + \Delta S_{s,hyd}
$$

The electrostatic part of solvation entropy is divided in to the bulk component and tight electrostatic polar solute - water interactions (hydrogen bonds). The bulk contribution is estimated from the temperature dependence of the solvent dielectric constant as:

$$
\Delta S_{s,elec\_bulk} = -\bigg(\frac{\partial \Delta G_s}{\partial \epsilon_{solv}}\bigg) \bigg(\frac{\partial \epsilon_{solv}}{\partial T}\bigg)
$$

The second term of the electrostatic solvation entropy is estimated as a constant of 28 J/(mol K).

The hydrophobic term,  $\Delta S_{s, hvd}$ , is evaluated as:

$$
\Delta S_{s,hyd} = -\left(\frac{\partial \Delta G_{s,hyd}}{\partial T}\right)
$$

where  $\Delta G_{s,hyd}$  consists of 3 components:

$$
\Delta G_{s,hyd} = \Delta G_{cav} + \Delta G_{VdW} + \Delta G_{Ind}
$$

describing the free energy of cavitation, solute-solvent van der Waals and inductive terms respectively. The cavity formation term is calculated from Scaled Particle Theory [Pierotti-1976]. Analytical expressions for  $\Delta G_{VdW}$  and  $\Delta G_{Ind}$  terms are also taken from the 1976 Pierotti review.

#### **Protein-bound ligand entropy**

Configurational entropy of a protein bound ligand is calculated totally as vibrational entropy for 3N modes, assuming that 3 rotational and 3 translational degrees of freedom of a solution ligand are transformed into low-vibrational degrees of freedom for the bound ligand.

Solvation entropy for a ligand in the active site is assumed to be a sum of its fractional value in solution determined by the percentage of the ligand surface exposed to the solvent,  $f \Delta S_s$ , and a partial desolvation entropy of the protein active site,  $\Delta S_{des}$ 

$$
S_{protein} = S_v + f\Delta S_s + \Delta S_{des}
$$

where f is the fraction of ligand surface exposed to the solvent. It is important to notice that  $S_{protein}$  is not an experimentally measurable value, and that only the difference between  $S_{protein}$  and  $S = S_c + \Delta S_s$  might be compared with experimental binding entropy.

## 2.2 freeform Theory

freeform has two distinct functions:

"freeform -calc conf...": Evaluation of the conformer free energy in solution, meaning the free energy required to select a particular conformer out of the whole conformational ensemble in solution.

"freeform -calc solv...": Fast estimation of the small molecule solvation free energy and the XLogP calculated partition coefficient (with graphical representation of fragment-based contributions to these physical quantities).

### 2.2.1 Conformer Free Energies

# **Calculating the partition function**

The method is based upon combining ligand conformational search, energy minimization, and entropy estimation in the workflow shown in Figure: Stages and workflow in the conformer free energy calculation below.

![](_page_12_Figure_4.jpeg)

## Fig. 1: Stages and workflow in the conformer free energy calculation

The conformational search is done at a very high resolution using the conformation generator OMEGA [Hawkins-2010]. The energy minimization uses Halgren's MMFF94s force field [Halgren-VI-1999] and consists of several stages, all aimed at arriving at the most thorough sampling of the accessible conformational space of the ligand. Duplicate conformers are removed from the final minimized set, leaving an ensemble of  $n_c$  unique conformers which we use to create an approximation to the partition function of the unbound ligand. This is illustrated conceptually in Figure: Concept of ligand entropy as a sum-over-states of conformers.

![](_page_12_Figure_7.jpeg)

Fig. 2: Concept of ligand entropy as a sum-over-states of conformer entropies

To the molecule's gas-phase potential based on the MMFF94 force field (shown by the red line), Sheffield solvation energies are added to give a solvation-corrected potential (shown by the blue line) for which the minima are identified. The analytic second derivative of each minimum is then used to calculate the entropy contribution of each energy well according to [Wlodek-2010]. An energy minimum with a wider than average energy well will have a higher entropy, which will decrease the conformer free energy to select that conformer, while the converse will be true for a narrower than average energy well.

With this, the contribution  $Q_i$  of each energy minimum to the overall partition function  $Q$  can be calculated:

$$
Q_i = q_t q_{ir} q_{iv} e^{-\epsilon_i/RT}
$$
$$
Q = \sum_{i=1}^{n_c} Q_i
$$

Here  $\epsilon_i$  is the relative internal energy (including solvation energy) of the conformer relative to the global minimum conformation.  $q_t$ ,  $q_t r$  and  $q_t v$  are the translational, rotational and vibrational partition functions respectively, describing the entropic contributions from that conformation.  $n_c$  is the number of unique conformations in the ensemble. More details on these terms are given in the theory section of the szybki documentation.

## **Computing the conformer free energies**

Based upon this approximation to the partition function, we calculate conformer free energies: the free energy required to select a particular conformation from the unbound ensemble of all conformers equilibrating in aqueous solution. Strictly speaking, this is a Helmholtz free energy, not a Gibb's free energy, because we are neglecting the differential PV (Pressure\*Volume) contribution between conformers, but this should be negligible. Based on the above conformer and ensemble partition functions, the conformer free energy for any conformer is calculated straightforwardly as:

$$
\Delta A_i = -RT(\ln Q_i - \ln Q)
$$

In addition to the graphic output file which shows a plot of the calculated free energies of conformations vs. their relative intrinsic energies, numerical results are stored in the log and csv files. For each conformation the following data are reported: rotational and vibrational entropies, total force field energy, solvation energy, the sum of solvation energy and force field energy, relative energy, free energy, and heavy atoms RMSD displacement from the input 3D structure (the latter only when the -useInput 3D option is used).

## Ligand strain in the input 3D structure

When conformer free energies are calculated with the  $-\text{useInput 3D flag},$  free form pays attention to the 3-D structure in the input file and keeps track of it, writing out the conformer free energy quantities associated with it. The idea is that the user can input a bioactive confirmation from an x-ray crystal structure, or a hypothetical model-built structure of interest, and get a direct readout of the energy required to select that particular conformation out of the aqueous ensemble. A key issue, however, is that the input 3D coordinates may be of artificially high energy, usually due to small deviations of bond lengths and bond angles from optimum; this is often true particularly of ligands from Xray structures. For this reason a "cleanup" pre-optimization is done using harmonic constraints to the input coordinates, thus retaining the shape of the ligand but resolving the artificially high energy. This "cleanup" energy is discarded. Since conformer free energies are calculated from energy minima in order to characterize the entropy, an unconstrained minimization is now required to find the closest energy minimum to the cleaned-up structure, which we refer to as the input 3D minimum. This minimization allows the torsions in the input structure to relax away from where they may have been distorted from the nearby local minimum, for example in order to fit into the active site. freeform keeps track of this "distortion" strain energy as Estrain. From this point, *freeform* simply includes the relaxed input 3D minimum as just another energy minimum in the aqueous ensemble and calculates its conformer free energy, which is specifically reported in the pdf and log output (see examples). Keep in mind that the free energy required to adopt the input 3D minimum may be significant and probably should be considered a component of the strain energy also. Thus, within *freeform*, the overall strain energy for the input 3D structure would be considered to consists of a) the conformer free energy required to adopt the input 3D minimum (i.e. the closest local minimum to the input structure), and b) the additional energy Estrain required to distort the torsions of that minimum so the ligand can adopt the shape of the actual input 3D structure.

# 2.2.2 Solvation energy estimation

## How it is calculated

The term "Solvation energy" is defined here as the standard free energy of transferring a compound from the gaseous phase into dilute aqueous solution,  $\Delta G_{solv}^0$ .

Solvation energy is a crucial component of the solubility energetics, and is directly related to hydrophilicity/hydrophobicity of a compound, therefore one can expect it is correlated with another measure of hydrophobicity logP, as illustrated on the diagram below (Figure: Solvation, solubility and hydrophobicity). Such a correlation, particularly when functional groups contribution is considered might not exist. freeform shows side-by-side the graphical group contributions to solvation free energy and XLogP.

![](_page_14_Figure_5.jpeg)

Fig. 3: Solvation, solubility and hydrophobicity

The method is based on the continuum solvent model in which a PB solver ZAP [Grant-2001] is used. The calculation is performed on the lowest energy gas-phase conformation found with the MMFF94 force field from the optimized set of conformations generated by the conformation generator OMEGA [Hawkins-2010]. A set of atomic radii ZAP9 and AM1BCC partial charges as described in [Nicholls-2010] is applied for all PB calculations. Atomic and group contributions to the free energy of solvation for the input compound are calculated from atomic electrostatic potentials and atomic area terms representing hydrophobic part of solvation. Assuming that a functional group has  $n$  atoms, its calculated solvation free energy  $\Delta G_s$  is:

$$
\Delta G_s = \sum_{i}^{n} [(V_{i,s} - V_{i,v})q_i + S_i]
$$

where  $V_{i,s}$  and  $V_{i,v}$  are calculated electrostatic potentials on atom i in solution and in vacuum respectively,  $q_i$  is atom partial charge and  $S_i$  is atomic contribution to hydrophobic part of solvation evaluated from a simple surface area model assuming 6.3 cal/(mol Å) as a value for microscopic surface tension coefficient. Graphical representation of group (or atomic) contributions to the free energy of solvation is performed with the OE toolkits OEDepict and Grapheme.

## Counterintuitive group contributions to solvation energies

Solvation free energy for molecular ions might not be trivial to interpret because of very strong intrinsic electrostatic interactions. One can most easily begin to understand these effects by considering zwitterions. A common zwitterion will contain both a group with a positive formal charge and a group with a negative formal charge. It is well known that zwitterions, though still having high solvation energies, have significantly smaller solvation energies than compounds with two formal charges of the same sign. In fact, zwitterion solvation energies are typically smaller than the solvation energy of the analog molecule with a single charge. For instance, as the following figures show *Figure: Solvation* energy of phenylalanine, Figure: Solvation energy of amide analog of phenylalanine and Figure: Solvation energy of methoxy analog of phenylalanine the solvation energy of zwitterionic phenylalanine is -32.8 kcal/mol, while the solvation energy of the formamide analog and the methyl ester analog are -73.4 and -63.4 kcal/mol respectively.

![](_page_15_Figure_3.jpeg)

Solvation Free Energy =  $-32.8$  kcal/mol

Fig. 4: Solvation energy of phenylalanine

One can consider then, that adding a charge that is the opposite charge of the current molecular ion contributes a positive 30 to 40 kcal/mol to the solvation energy. A similar situation, perhaps even more dramatic, occurs in the case of intramolecular salt bridges, where positively and negatively charged groups are positioned in a very short distance (that kind of interaction not only exists in macromolecules: NMR and hydrogen exchange rate experiments have confirmed the presence of salt bridges between arginine or lysine and aspartate or glutamate side chains also in short peptides [Otter-1989], [Mayne-1998]). Making positive contributions to the solvation energy is generally considered a hydrophobic effect, yet here the contribution is made by a charged species – something that is somewhat counterintuitive at first. Nevertheless, in this context, one can understand how, under the right conditions, a normally hydrophilic functional group can make a significant positive contribution to the solvation energy. The more confusing circumstance is when, rather than a simple zwitterion, we see a similar effect in a molecule with either multiple charges of one type (either positive or negative) and a single charge of the opposite sign. Consider a molecule with 2 negative ions, one positive ion and a total charge of -1, like the one shown on Figure: Example of counterintuitive

![](_page_16_Figure_1.jpeg)

Solvation Free Energy = -73.4 kcal/mol

Fig. 5: Solvation energy of amide analog of phenylalanine

#### group contributions to solvation below.

In this case, the positive ion will be changing the formal charge from -2 to -1. This will make the total solvation energy significantly less negative (a positive contribution to the solvation energy). The positive ionic functional group in this case will have a large positive solvation energy. While a charged group is indeed not hydrophobic, in this instance, one can understand that it makes the solvation energy less negative in a manner similar to the way a hydrophobic group might, but to a larger degree. In more subtle cases, one can observe a similar though less dramatic hydrophobicity in a molecule with a single charge, either positive or negative and another fragment that makes a large neutralizing contribution to the partial charge of the molecule.

In order to alert the user, species which contain strong intramolecular electrostatic interactions of the nature described above are depicted on a light pink background. This should act as a reminder to users to consider the net charge of the molecule in interpreting the relative contribution of each fragment to the solvation energy.

![](_page_17_Picture_1.jpeg)

Solvation Free Energy = -63.4 kcal/mol

Fig. 6: Solvation energy of methoxy analog of phenylalanine

![](_page_17_Figure_4.jpeg)

Fig. 7: Counterintuitive group contributions to solvation

# **THREE**

**API** 

# **3.1 OESz Classes**

# 3.1.1 OESzybki

class OESzybki

This class represents OESzybki.

## **Constructors**

```
OESzybki()
OESzybki (const OESzybkiOptions& opts)
```

The default constructor builds OESzybki with the MMFF force field. The OESzybkiOptions can be provided as argument with specifying many other parameters, including other force fields supported.

#### operator()

```
OESystem::OEIterBase<OESz::OESzybkiResults> *operator()(OEChem::OEMCMolBase &m)
bool operator () (OEChem:: OEMolBase &m, OESz:: OESzybkiResults &res)
```

The first operator performs geometry optimization on all conformers in the passed molecule  $m$  and updates it with optimized coordinates. It returns an iterator whose elements are OESzybkiResults objects. OESzybkiResults contains the energy values of the relevant potential terms, total energies and gradients. The description of the OESzybkiResults structure is given below. The second operator performs the same task on a molecule in a single conformation. A reference to an instance of OESzybkiResults structure has to be passed. If the calculation fails the operator returns false.

#### **ClearFixAtoms**

```
void ClearFixAtoms()
```

Removes the fix constraint on any fixed atoms. After the use of this function, positions of all atoms could change upon optimization.

## **ClearHarmonicConstraints**

```
bool ClearHarmonicConstraints ()
```

Removes harmonic constraints. Returns true if constraints were removed and false when the action was not necessary because a constraining potential was not present.

## **ClearTorsionConstraint**

**bool** ClearTorsionConstraint()

Removes torsion constraint. Returns true if constraint is removed and false when the action was not necessary because a constraining potential was not present.

## **FixAtoms**

bool FixAtoms (std::string smarts\_pattern) bool FixAtoms (const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &)

Fixes a set of atoms at their initial positions in space. The first function fixes a set of atoms which belong to a SMARTS pattern determined by the parameter smarts\_pattern. It returns true if the SMARTS string passed is valid, false otherwise. The second function fixes only those atoms for which the predicate passed is true, and returns true if the predicate is valid.

## GetEntropy(const OEChem::OEMCMolBase&, unsigned int, unsigned int)

double GetEntropy (const OEChem:: OEMCMolBase &m, unsigned int →method=OEEntropyMethod:: QNewton, unsigned int env=OEEnvType::SolutionSPT)

Estimates and returns the entropy of a compound in different environments for an ensemble of conformations given in the input molecule m. The method does not alter the input set of conformations. The default parameter method specifies that the method of entropy evaluation is quasi-Newton. The alternative value for this parameter is OEEntropyMethod\_Analytic. The last parameter in both methods specifies ligand environment. Its default value refers to the ligand in solution where solvation entropy is handled by scaled-particle theory (SPT). The remaining possible values of the parameter env are: OEEnvType\_Gas, OEEnvType\_Protein and OEEnvType\_SolutionSA which specify gas-phase, protein-bound and solution ligand, respectively. In the case of OEEnvType\_SolutionSA the solvation entropy is evaluated with the "Surface Area" model, however we recommend the default which uses SPT.

Deprecated since version 1.8.2: Use overloaded  $OESzybki$ . GetEntropy instead.

#### **GetEntropy**

```
double GetEntropy (OEChem:: OEMCMolBase& m, OESzybkiEnsembleResults& r,
                  unsigned int method = OEEntropyMethod:: QNewton,
                  unsigned int env = OEEnvType:: SolutionSPT)
```

Estimates and returns the entropy of a compound in different environments for an ensemble of conformations given in the input molecule m. The set of optimized unique conformations is returned in the first parameter m. The method takes the reference of the OESzybkiEnsembleResults object r which carries the entropy results for the ensemble. The default parameter method specifies that the method of vibrational entropy evaluation is based on second derivatives matrix (Hessian) which is taken from the final step of quasi-Newton optimization. The alternative value for this parameter is OEEntropyMethod\_Analytic. When the latter is selected, Hessian matrix is calculated analytically. The last parameter specifies ligand environment. Its default value refers to the ligand in solution where solvation entropy is handled by scaled-particle theory (SPT). The remaining possible values of the parameter  $env$  are:  $OEEnvType_Gas$ , OEEnvType\_Protein and OEEnvType\_SolutionSA which specify gas-phase, protein-bound and solution ligand respectively. In the case of OEEnvType\_SolutionSA the solvation entropy is evaluated with the "Surface Area" model, however we recommend the default which uses SPT.

## **GetFixPattern**

const char \*GetFixPattern() const

Returns the SMARTS string used for fixing atoms.

#### **GetFixPredicate**

const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> \*GetFixPredicate() const

Returns a pointer to the predicate used to determine which atoms are fixed.

### **GetHarmonicConstraints**

```
const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>
GetHarmonicConstraints (double &kc, double &kd) const
```

Provides a method to query for the harmonic constraint used, the force constant kc, and distance kd. The function returns a pointer to a predicate which determines which atoms are constrained. If the returned pointer is 0, then no harmonic constraints are used.

#### **GetProtein**

```
bool GetProtein (OEChem:: OEMolBase &p) const
```

Copies the current protein molecule to the passed molecule object p. If the OESzybki object does not hold a protein molecule, the function will return false.

#### **GetSheffieldParameters**

void GetSheffieldParameters (double &a, double &b, double &dc) const

Returns the Sheffield solvation model parameters which are currently used.

### **LoadPotentialGrid**

void LoadPotentialGrid(std::string fname)

Reads a pre-calculated potential grid from the file name finame. For a large number of ligands to be optimized inside a single protein with the use of the electrostatic model OEProteinElectrostatics\_GridPB OESzybkiProteinOptions. OEProteinElectrostatics\_GridCoulomb function **or** (see SetProteinElectrostaticModel), this function offers a significant saving in CPU time.

### **SavePotentialGrid**

void SavePotentialGrid(std::string fname)

Saves potential grid in the file named fname. The potential grid will be generated in proteinligand calculations in which electrostatic model used is OEProteinElectrostatics GridPB or OEProteinElectrostatics\_GridCoulomb set with the function OESzybkiProteinOptions. SetProteinElectrostaticModel.

## **SetHarmonicConstraints**

```
bool SetHarmonicConstraints (double kc, double kd=0.0,
                            const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
→pred=OEChem::OEIsHeavy())
```

Adds potential term  $V = k_c (r - k_d)^2$  for every atom for which the passed predicate operator returns  $\tau$  rue. Default predicate imposes harmonic potential on every heavy atom. Parameter kc is the force constant  $k_c$  (in  $kcaI/(mol|A|^2)$ ) and kd is the constraining distance  $k_d$  in A. By default kd is set to 0. Function returns true if harmonic potential added.

## **SetProtein**

bool SetProtein (const OEChem:: OEMolBase& protein)

Sets the protein molecule for subsequent szybki calculations. The protein molecule may be modified by this operation, if needed. It returns false if the operation fails, otherwise true.

Note: To specify charging options for protein-ligand coulombic interactions, the use OESzybkiSolventOptions.SetChargeEngine method under the OESzybkiSolventOptions class. To work with the pre-existing charges, use the OEChargeEngineNoOp as the charging engine.

### **SetSheffieldParameters**

```
void SetSheffieldParameters (double a, double b, double dc=1.0)
```

Sheffield solvation energy requires two parameters a and b:  $E_{solv} = -\frac{f_e}{8\pi\epsilon_0} \sum_{i,j} \frac{q_i q_j}{\sqrt{(a R_i R_j + b r_{ij}^2)}}$  where  $q_i$  and  $q_j$  are atomic charges,  $R_i$  and  $R_j$  are vdW radii for atoms i and j, and  $r_{ij}$  is the interatomic distance. Parameter  $f_{\epsilon}$  depends on dielectric constants of the solute ( $\epsilon$ ) and the solvent ( $\epsilon_{solv}$ ):  $f_{\epsilon} = 1/\epsilon - 1/\epsilon_{solv}$ ). This function sets both parameters  $a$  and  $b$  to the required values, as well as the solute dielectric constant (which may not exceed 10). If the function not used, the solute dielectric constant is set to 1.0, and the default values of  $a = 1.553149$  and  $b = 0.735694$  are adopted  $([Grant-2007]).$ 

# 3.1.2 SetTorsionConstraint

```
bool SetTorsionConstraint (std::string tor_pattern, double k, double phi0)
bool SetTorsionConstraint (const OEChem:: OETorsion& tor, double k)
```

The method adds a potential term  $V = k_c(\cos(phi)-\cos(phi))$ <sup>2</sup> for a torsion. The first method specifies the torsion with a SMARTS pattern passed as a string tor pattern. This must be in the indexed form which show which atoms forms the torsion. For example a valid pattern is  $[{\rm C}:1]$   $[N:2]$   $[{\rm C}:3]$   $[{\rm S}:4]$ .  $k$  is the user specified force field in kcal/mol, and  $phi0$  is the torsion reference dihedral angle in radians. The function returns  $t \text{ rule}$  if a torsion constraint is added successfully.

The second method takes an instance of an OETorsion object, tor, which defines a single torsion to be constrained. k is the user specified force field in kcal/mol. The function returns true if a constrained torsion is added successfully.

# 3.1.3 UnsetProtein

void UnsetProtein() const

Removes protein context from the OESzybki object.

# 3.1.4 OESzybkiOptions

class OESzybkiOptions : public OESystem: : OEOptions

This class represents options to setup a OESzybki calculation.

## **Constructors**

```
OESzybkiOptions()
OESzybkiOptions (const OESzybkiOptions &)
```

Default and copy constructors.

#### operator=

```
OESzybkiOptions & operator=(const OESzybkiOptions &)
```

### **GetGeneralOptions**

```
OESzybkiGeneralOptions& GetGeneralOptions()
const OESzybkiGeneralOptions& GetGeneralOptions() const
```

Returns a reference to the OESzybkiGeneralOptions instance as currently set. These options are used in defining general environment for all szybki calculations.

#### **GetOptOptions**

```
OESzybkiOptOptions& GetOptOptions()
const OESzybkiOptOptions& GetOptOptions() const
```

Returns a reference to the OESzybkiOptOptions instance as currently set. These are options related to optimization in OESzybki.

### **GetProteinOptions**

```
OESzybkiProteinOptions& GetProteinOptions()
const OESzybkiProteinOptions& GetProteinOptions() const
```

Returns a reference to the OESzybkiProteinOptions instance as currently set. These are options related to proteins in OESzybki.

#### **GetRunType**

unsigned int GetRunType() const

Returns Szybki run type declared in the OESzybkiOptions object.

## **GetSolventOptions**

```
OESzybkiSolventOptions& GetSolventOptions()
const OESzybkiSolventOptions& GetSolventOptions() const
```

Returns a reference to the OESzybkiSolventOptions instance as currently set. These are options related to solvents in OESzybki.

#### **SetGeneralOptions**

**void** SetGeneralOptions (const OESzybkiGeneralOptions&)

Sets the general szybki options by passing in an OESzybkiGeneralOptions instance. These options are used in defining general environment for all szybki calculations.

#### **SetOptOptions**

**void** SetOptOptions (const OESzybkiOptOptions&)

Sets the optimization options by passing in OESzybkiOptOptions instance. These are options related to optimization in OESzybki.

#### **SetProteinOptions**

void SetProteinOptions (const OESzybkiProteinOptions&)

Sets the protein options by passing in OESzybkiProteinOptions instance. These are options related to proteins in OESzybki.

#### **SetRunType**

bool SetRunType (unsigned int run\_type)

Sets requested run type. Returns true if run was successfully set. Possible input choices are given in the namespace OERunType. Warning: Setting run\_type with OERunType\_SolidBodyOpt implies optimization of a ligand inside rigid protein receptor. An attempt of solid-body optimization inside flexible protein receptor (see method OESzybkiProteinOptions. SetProteinFlexibilityType) will result in a message: Fatal: Solid-body optimization allowed only for ligand in fixed protein.

#### **SetSolventOptions**

**void** SetSolventOptions (const OESzybkiSolventOptions&)

Sets the solvent options by passing in OESzybkiSolventOptions instance. These are options related to solvents in OESzybki.

## 3.1.5 OESzybkiGeneralOptions

class OESzybkiGeneralOptions : public OESystem:: OEOptions

This class represents general options for szybki.

## **Constructors**

```
OESzybkiGeneralOptions()
OESzybkiGeneralOptions (const OESzybkiGeneralOptions &)
```

Default and copy constructors.

#### operator=

OESzybkiGeneralOptions & operator=(const OESzybkiGeneralOptions &)

#### **GetCalculateGradients**

bool GetCalculateGradients () const

Returns the state of the calculate gradients flag. If true, OESzybki will calculate and report gradients.

## **GetForceField**

const OEMolPotential:: OEForceField\* GetForceField() const

Returns the pointer to the OEForceField object which was used in the method OESzybkiGeneralOptions. SetForceField.

#### **GetForceFieldType**

unsigned int GetForceFieldType() const

Returns the force field type to be used for OESzybki calculations, as *unsigned int* from the *OEFOrCeFieldType* namespace.

## **GetIEFFCluster**

bool GetIEFFCluster () const

Returns the state of the IEFF cluster flag. If true, OESzybki will optimize a cluster of molecules with the MMFF94-IEFF or MMFF94S-IEFF force field.

#### **GetIntramolecularVdWCutoff**

```
double GetIntramolecularVdWCutoff() const
```

Returns the value of the intramolecular vdW interactions cutoff. The intramolecular VdW interactions are considered to be zero between atoms that are separated by distances larger than the cutoff.

### **GetLigandRMSDHeavv**

bool GetLigandRMSDHeavy () const

Returns the state of the Ligand RMSD heavy flag. If true, OESzybki reports RMSD for the optimized molecular systems based on heavy atoms only.

#### **GetRemoveAttractiveVdWForces**

bool GetRemoveAttractiveVdWForces() const

Returns the state of the Remove Attractive VdW Forces terms flag. If true, OESzybki removes the attractive part of the VdW interaction terms from the force field for calculations.

#### **GetRemoveCoulombTerms**

bool GetRemoveCoulombTerms() const

Returns the state of the Remove Coloumb terms flag. If true, OESzybki removes the Coulomb terms from the force field for calculations.

## **GetSoluteDielectric**

float GetSoluteDielectric() const

Returns the value of ligand dielectric constant used for the optimization of ligand in solution.

#### **GetTemperature**

double GetTemperature() const

Returns the value of temperature to be used for entropy calculation, in units of kelvins.

## **GetVerbose**

```
bool GetVerbose() const
```

Returns the state of the verbose flag. If true, OESzybki is set for reporting optimization progress.

### **SetCalculateGradients**

bool SetCalculateGradients (const bool)

Sets the state of the calculate gradients flag. If  $true$  is passed, OESzybki will calculate and report gradients.

## **SetForceField**

**bool** SetForceField(OEMolPotential::OEForceField&)

Sets the force field to be used for OESzybki calculations, using an instance of OEForceField. This method provids an alternative to setting force field by a predefined type with OESzybkiGeneralOptions. SetForceFieldType. Method returns true when the setting is successful, false otherwise.

#### **SetForceFieldType**

bool SetForceFieldType (const unsigned int)

Sets the force field to be used for OESzybki calculations, using constants defined in the OEFOrCeFieldType This method provids an alternative to setting force field by a force field instance with namespace. OESzybkiGeneralOptions. SetForceField. Method returns true when the setting is successful, false otherwise.

#### **SetIEFFCluster**

bool SetIEFFCluster (const bool)

Sets the state of the IEFF cluster flag. If true is passed, OESzybki will optimize a cluster of molecules with the MMFF94-IEFF or MMFF94S-IEFF force field.

#### **SetIntramolecularVdWCutoff**

bool SetIntramolecularVdWCutoff(const double)

Sets the value of the intramolecular vdW interactions. The intramolecular VdW interactions are considered to be zero between atoms that are separated by distances larger than the cutoff. By default no cutoff is used.

#### **SetLigandRMSDHeavy**

bool SetLigandRMSDHeavy (const bool)

Sets the state of the Ligand RMSD heavy flag. If  $true$  is passed, OESzybki reports RMSD for the optimized molecular systems based on heavy atoms only. By default, RMSD is calculated based on all atoms.

#### **SetRemoveAttractiveVdWForces**

bool SetRemoveAttractiveVdWForces (const bool) const

Sets the state of the Remove Attractive VdW Forces terms flag. If true, OESzybki removes the attractive part of the VdW interaction terms from the force field for calculations.

## **SetRemoveCoulombTerms**

bool SetRemoveCoulombTerms (const bool)

Sets the state of the Remove Coloumb terms flag. If t rue is passed, OESzybki removes the Coulomb terms from the force field for calculations.

## **SetSoluteDielectric**

```
bool SetSoluteDielectric(const double)
```

Sets the value of ligand dielectric constant used for the optimization of ligand in solution.

#### **SetTemperature**

bool SetTemperature (const double)

Returns the value of temperature to be used for entropy calculation, in units of kelvins. The default temperature is set to 298.15K.

#### **SetVerbose**

bool SetVerbose (const bool)

Sets the state of the verbose flag. If  $true$  is passed, OESzybki is set for reporting optimization progress.

# 3.1.6 OESzybkiOptOptions

class OESzybkiOptOptions : public OESystem: : OEOptions

This class represents optimization related options for szybki.

#### **Constructors**

```
OESzybkiOptOptions()
OESzybkiOptOptions (const OESzybkiOptOptions &)
```

Default and copy constructors.

#### operator=

OESzybkiOptOptions & operator=(const OESzybkiOptOptions &)

## **GetCalculateFrozenTerms**

bool GetCalculateFrozenTerms() const

Returns the state of the calculate frozen terms flag. If true, OESzybki will include the constant energy terms in the final optimized energy.

#### **GetGradTolerance**

double GetGradTolerance() const

Returns the optimizer gradient convergence criterion defined as RMS gradient in kcal/(mol  $\AA$ ).

#### **GetMaxIter**

unsigned int GetMaxIter() const

Returns the value of maximum number of optimizer iterations.

#### **GetOptimizerType**

unsigned int GetOptimizerType() const

Returns the optimizer type to be used, as as *unsigned int* from the  $OEOptType$  namespace.

#### **SetCalculateFrozenTerms**

bool SetCalculateFrozenTerms (const bool)

Allows the omission of the energy calculation of the fixed terms at the end of the optimization. This situation occurs when adaptors are used. By default constant energy terms are calculated for the optimized structure and added to the total energy.

#### **SetGradTolerance**

```
bool SetGradTolerance (const double)
```

Sets the optimizer gradient convergence criterion defined as RMS gradient in kcal/(mol Å). If not set by the user a 0.1 value threshold for gradient norm  $\sqrt{\sum_i g_i g_i}$ , will be used as termination criteria for all optimization types but Newton-Raphson. In the case of the latter the default gradient tolerance is RMS gradient of 1e-5 kcal/(mol Å).

## **SetMaxIter**

```
bool SetMaxIter (const unsigned int)
```

Sets the value of maximum number of optimizer iterations. The default value is set to 1000.

### **SetOptimizerType**

bool SetOptimizerType (const unsigned int)

Selects the type of the optimization which will be used for optimization. The available values are defined in the  $OEOptType$  namespace. Method returns false when the invalid selection is chosen, true otherwise.

## 3.1.7 OESzybkiSolventOptions

class OESzybkiSolventOptions : public OESystem: : OEOptions

This class represents options related to solvent modeling in szybki.

### **Constructors**

```
OESzybkiSolventOptions()
OESzybkiSolventOptions (const OESzybkiSolventOptions &)
```

Default and copy constructors.

#### operator=

OESzybkiSolventOptions & operator=(const OESzybkiSolventOptions &)

## **GetAtomicRadiiType**

```
unsigned int GetAtomicRadiiType () const
```

Returns the type of atomic radii used for PB calculations, as an *unsigned int* from the OEAt omicRadii namespace.

#### **GetCavitySolventParameter**

```
double GetCavitySolventParameter() const
```

Returns the microscopic surface tension coefficient (in kcal/(mol  $A^{**2}$ )) used in hydrophobic ligand solvation model.

## **GetSaltConcentration**

double GetSaltConcentration() const

Returns the value of salt concentration in moles/liter (M).

### **GetSolventDielectric**

double GetSolventDielectric() const

Returns the value of solvent dielectric constant for the protein-ligand system.

## **GetSolventModel**

unsigned int GetSolventModel() const

Returns the type of solvent model used for the calculations of solution ligands, as an *unsigned int* from the OESolventModel namespace.

### **SetAtomicRadiiType**

bool SetAtomicRadiiType (const unsigned int)

Sets the type of atomic radii to be used for PB calculations, as an *unsigned int* from the OEAt omicRadii namespace.

#### **SetCavitySolventParameter**

bool SetCavitySolventParameter (const double)

Sets the microscopic surface tension coefficient (in kcal/(mol A\*\*2)) used in hydrophobic ligand solvation model. The default value is set to be 0.025 kcal/(mol  $A^{**}$ 2). Smaller values usually in the range 0-10 kcal/(mol  $A^{**}$ 2) usually reflects a combined hydrophobic solvation effect of cavitation and solute-solvent vdW interactions.

## **SetSaltConcentration**

bool SetSaltConcentration (const double)

Sets the value of salt concentration in moles/liter (M). By default a zero salt concentration is assumed. Values higher than 0.08 should not be used and are not supported.

## **SetSolventDielectric**

bool SetSolventDielectric(const double)

Sets the value of solvent dielectric constant for the protein-ligand systems in PB calculations. The default value of solvent dielectric constant is set to 80.0.

#### **SetSolventModel**

bool SetSolventModel (const unsigned int)

Sets the type of solvent model used for the calculations of solution ligands, as an unsigned int from the OESolventModel namespace. Method returns false when the invalid selection is chosen, true otherwise.

#### **SetChargeEngine**

void SetChargeEngine (const OEProton:: OEChargeEngineBase&)

Sets the charging engine to obtain partial charges used for solvation calculation by passing in an OEChargeEngineBase instance.

#### **SetUseCurrentCharges**

void SetUseCurrentCharges()

Sets the charging engine to work with the existing charges. This command is equivalent to using the OESzybkiSolventOptions. SetChargeEngine method with an OEChargeEngineNoOp instance as input.

## 3.1.8 OESzybkiProteinOptions

class OESzybkiProteinOptions : public OESystem:: OEOptions

This class represents options related to proteins in szybki.

### **Constructors**

```
OESzybkiProteinOptions()
OESzybkiProteinOptions (const OESzybkiProteinOptions &)
```

Default and copy constructors.

#### operator=

OESzybkiProteinOptions & operator=(const OESzybkiProteinOptions &)

## **AddFlexibleResidue**

AddFlexibleResidue(const OEChem::OEResidue&)

Adds a single residue to the list of residues which will be optimized together with the ligand. Has to be called multiple times in order to make more than one residue flexible.

#### See also:

• Example in Partially flexible protein optimization

#### **ClearFlexibleResidues**

void ClearFlexibleResidues()

Clears all of the currently set flexible residues.

#### GetExactVdWProteinLigand

bool GetExactVdWProteinLigand() const

Returns the state of the exact VdW protein-ligand flag. If true, OESzybki will be using analytical vdW protein-ligand interaction.

#### **GetIntermolecularVdWCutoff**

double GetIntermolecularVdWCutoff() const

Returns the value of the intermolecular vdW interactions cutoff in Å. The intermolecular VdW interactions are considered to be zero between atoms that are separated by distances larger than the cutoff.

## **GetProteinDielectric**

double GetProteinDielectric() const

Returns the value of protein dielectric constant.

## GetProteinElectrostaticModel

unsigned int GetProteinElectrostaticModel() const

Returns the protein electrostatics model to be used for OESzybki calculations, as *unsigned int* from the OEProteinElectrostatics namespace.

#### **GetProteinFlexibilityRange**

double GetProteinFlexibilityRange() const

Returns the value of partial protein flexibility distance from the ligand.

#### **GetProteinFlexibilityType**

unsigned int GetProteinFlexibilityType() const

Returns the type of partial protein flexibility to be used for OESzybki calculations, as *unsigned int* from the OEProtFlex namespace.

#### **HasFlexibleResidues**

bool HasFlexibleResidues() const

Returns the state of flexible residues. If true, some flexible residues are currently set.

#### SetExactVdWProteinLigand

bool SetExactVdWProteinLigand (const bool)

Sets the state of the exact VdW protein-ligand flag. If true is passed, OESzybki will be using analytical vdW protein-ligand interaction.

#### **SetIntermolecularVdWCutoff**

bool SetIntermolecularVdWCutoff (const double)

Sets the value of the intermolecular vdW interactions cutoff in Å. The intermolecular VdW interactions are considered to be zero between atoms that are separated by distances larger than the cutoff. The default value is 18 Å, however when Newton-Raphson optimization is used (see method OESzybkiOptOptions. SetOptimizerType) the default cutoff of 50  $\AA$  is used.

## **SetProteinDielectric**

bool SetProteinDielectric (const double)

Sets the value of protein dielectric constant for the calculation of protein-ligand interaction. The default value of the protein dielectric constant is 1.0.

### SetProteinElectrostaticModel

bool SetProteinElectrostaticModel(unsigned int)

Sets the protein electrostatics model to be used for OESzybki calculations, as unsigned int from the OEProteinElectrostatics namespace. Method returns false when the invalid selection is chosen, true otherwise.

#### SetProteinFlexibilityRange

bool SetProteinFlexibilityRange(const double)

Sets the value of partial protein flexibility distance from the ligand.

### SetProteinFlexibilityType

bool SetProteinFlexibilityType (const unsigned int)

Sets the type of partial protein flexibility to be used for OESzybki calculations, as *unsigned int* from the  $OEProtFileX$ namespace. Method returns false when the invalid selection is chosen, true otherwise.

# 3.1.9 OESzybkiResults

class OESzybkiResults

This class represents OESzybkiResults.

#### **Constructors**

```
OESzybkiResults()
OESzybkiResults (const OESzybkiResults &)
```

Default and copy constructors.

#### operator=

OESzybkiResults & operator=(const OESzybkiResults &)

### **Clear**

void Clear()

Removes all data from the OESzybkiResults object.

## **GetCPUTime**

float GetCPUTime () const

Returns CPU time in seconds for the optimization.

#### **GetConfldx**

unsigned int GetConfIdx() const

Returns conformer id number.

#### **GetEnergyTerm**

double GetEnergyTerm (unsigned int) const

Returns the current energy value for a specified potential term. The integer values which determine potential terms are defined in the namespace OEPotentialTerms

## **GetFinalRMSGradient**

| <b>double</b> GetFinalRMSGradient() const |
|-------------------------------------------|
|-------------------------------------------|

Returns final RMS of forces, √ ( *g* · *g* / *n\_v* ), where **g** is the gradient vector and *n\_v* the number of variables.

## **GetGradients**

bool GetGradients (double\* gradients, const OEChem:: OEAtomBase\* atom) const

Fills the passed double array with gradients for the atom passed as a second argument. Returns true if the gradients are successfully exported, false otherwise. Export of gradients is available only when the method OESzybkiGeneralOptions. SetCalculateGradients is called prior to the calculation performed with one of the OESzybki. operator () operators. Currently calculation of gradients is available only for single-point runs.

## **GetFinalTotalPotential**

double GetFinalTotalPotential() const

Returns the value of the optimized potential for the molecular system.

#### GetIntramolecularLigandEnergy

double GetIntramolecularLigandEnergy () const

Returns the value of the value of intramolecular MMFF energy.

## **GetInitialRMSGradient**

double GetInitialRMSGradient () const

Returns the initial RMS of forces,  $\sqrt{\frac{g \cdot g}{n_v}}$ , where g is the gradient vector and  $n_v$  the number of variables.

## **GetInitialTotalPotential**

double GetInitialTotalPotential() const

Returns the value of the initial potential for the molecular system to be optimized.

#### **GetInterEnergy**

double GetInterEnergy () const

Returns the interaction energy between protein (or DNA) and the ligand optimized inside the macromolecule. For ligands optimized in vacuum or in solution, this function returns 0.

#### **GetMaxDisplacement**

double GetMaxDisplacement () const

Returns the maximum atomic displacement for a single atom in Å during optimization.

#### **GetNumCycles**

unsigned int GetNumCycles() const

Returns the number of cycles performed by the optimizer.

## **GetNumFixAtoms**

unsigned int GetNumFixAtoms() const

Returns the number of atoms which will be fixed during optimization.

#### **GetNumRotors**

unsigned int GetNumRotors() const

Returns the number of rotatable bonds in the molecule.

## **GetProteinRMSD**

double GetProteinRMSD() const

In the case of a partially optimized protein (residues, side chains, polar hydrogens in proximity to the ligand) the function returns the RMS displacement of a protein from its initial structure.

#### **GetRMSD**

double GetRMSD() const

Returns the RMS displacement of the optimized structure with respect to the initial structure.

#### **GetTotalEnergy**

double GetTotalEnergy () const

Returns the total energy of the optimized system. That includes all intra and inter molecular MMFF terms, solvation energy (Sheffield or PB, if present) and protein-ligand interaction energy if a ligand is optimized inside the protein. Harmonic energy constraint energy is excluded.

#### GetTotalEnergyWithHarmConstraint

double GetTotalEnergyWithHarmConstraint() const

Returns total energy of the optimized system plus harmonic energy constraint.

#### **IsActiveTerm**

bool IsActiveTerm (unsigned int term) const

Returns t rue if the potential term specified by the parameter term is included in the potential function of the system. Possible parameters values are defined in the namespace OEPotentialTerms.

#### **GetConfFreeEnergyFromEnsemble**

double GetConfFreeEnergyFromEnsemble() const

Returns the free energy of selecting a conformation out of the ensemble calculated as:  $-RTln(q/Q)$ , where q is the partition function of a ligand conformer and  $Q$  is the partition function for the entire ensemble. The method will throw an error unless it is run following the call to OESzybki. GetEntropy method which takes the OESzybkiEnsembleResults instance as a second parameter, followed by the call to  $OESzybkiEnsembleResults$ . GetResultsForConformations on the returned OESzybkiEnsembleResults object.

### **GetVibEntropy**

double GetVibEntropy() const

Returns the vibrational entropy of a conformation in e.u.  $\text{(cal/(mol K))}$  when entropy has been calculated with one of the OESzybki.GetEntropy methods.

### **GetRotEntropy**

double GetRotEntropy () const

Returns the rotational entropy of a conformation in e.u.  $\frac{\text{cal/(mol K)}}{\text{m}}$  when entropy has been calculated with one of the OESzybki.GetEntropy methods.

#### **GetLnQvib**

double GetLnQvib() const

Returns the natural logarithm of a vibrational partition function when entropy has been calculated with one of the OESzybki.GetEntropy methods.

#### **GetLnQrot**

double GetLnQrot() const

Returns the natural logarithm of a rotational partition function when entropy has been calculated with one of the OESzybki.GetEntropy methods.

#### **IsUnique**

bool IsUnique () const

Returns true if the conformation is unique in terms of the structure. Although the method  $OESzybki$ .  $GetEntropy$  which takes a non-const OEMCMolBase object is guaranteed to return an ensemble of unique conformations, the other methods in oeszybki library do not. The method might be therefore useful to make sure if the current conformation is unique or not.

## **Print**

```
void Print (OEPlatform::oeostream &) const
void Print (OESystem:: OEErrorHandler &) const
```

Both functions allow the generation of log information on the optimized system. The following information is reported:

- Conformer id
- Number of fixed atoms (if any)
- Number of torsions (if any and if optimization in torsion space is true)
- Initial energy
- · Initial rms gradient
- Final energy
- Final rms gradient
- RMS displacement upon optimization
- Maximum displacement during optimization
- Values of potential terms at final geometry

# 3.1.10 OESzybkiEnsembleResults

class OESzybkiEnsembleResults

This class represents OESzybkiEnsembleResults.

#### **Constructors**

```
OESzybkiEnsembleResults()
OESzybkiEnsembleResults (const OESzybkiEnsembleResults &)
```

Default and copy constructors.

#### operator=

```
OESzybkiEnsembleResults & operator=(const OESzybkiEnsembleResults &)
```

## **NumConfs**

unsigned int NumConfs() const

Returns the number of unique conformations in the ensemble.

#### **GetTemperature**

double GetTemperature() const

Returns the temperature in K. This is a convenience method returning the same information as the method of the same name in the OESzybki class.

## **GetTotalEntropy**

double GetTotalEntropy() const

Returns the total entropy of the ligand in  $J/(mol \text{ K})$ .

### **GetEntropicEnergy**

double GetEntropicEnergy () const

Returns the product of total entropy and temperature, ST in kcal/mol.

### **GetChargeType**

unsigned int GetChargeType () const

Returns the type of atomic partial charges used in entropy estimation. The returned type are is either OECharges\_AM1BCCNoSymSPt or OECharges\_NoOp.

#### GetConfigurationalEntropy

double GetConfigurationalEntropy() const

Returns the ensemble configurational entropy. For gas-phase ligands that value is the same as the value returned by OESzybkiEnsembleResults.GetTotalEntropy. For solution ligands the configurational entropy made by translational-vibrational-rotational entropy, and for protein-bound ligands it represents vibrational entropy.

## GetEnsembleLigSolvEntropy

double GetEnsembleLigSolvEntropy() const

Returns the value of the ensemble solvation entropy for a ligand in solution. The method returns zero for gas-phase and protein-bound ligands.

### **GetEnsembleLigPartialSolvEntropy**

double GetEnsembleLigPartialSolvEntropy() const

Returns the value of solvation entropy for the protein-bound ligand partially exposed to solvent.

## **GetEnsembleProtDesolvEntropy**

double GetEnsembleProtDesolvEntropy () const

Returns the value of protein desolvation entropy upon ligand binding.

## **GetResultsForConformations**

OESystem::OEIterBase<OESzybkiResults>\* GetResultsForConformations() const

Returns the iterator whose elements are OESzybkiResults objects for the ensemble of conformation members optimized during the entropy estimation. Data only for unique conformations are represented in the returned set.

#### **HasEntropy**

bool HasEntropy () const

Returns true if the OESzybkiEnsembleResults object contains calculated entropy, false is returned otherwise.

## 3.1.11 OEProteinFlexOptions

class OEProteinFlexOptions : public OESystem:: OEOptions

This class provides an interface to setup protein flexibility for flexible protein optimization, as used in OEFlexProtein-LigandOptimizer.

The OEProteinFlexOptions class defines the following public methods:

- · GetFlexRange and SetFlexRange
- GetResidueID and SetResidueID

#### **Constructor**

```
OEProteinFlexOptions();
OEProteinFlexOptions (const OEProteinFlexOptions &)
```

Default and copy constructors.

#### operator=

OEProteinFlexOptions & operator=(const OEProteinFlexOptions &)

### **GetFlexRange**

double GetFlexRange() const

See SetFlexRange method.

#### **GetResiduelD**

const OEProton:: OEChargeEngineBase\* GetResidueID() const

See Set Residue ID method.

#### **SetFlexRange**

bool SetFlexRange (const double)

Sets the flexibility range for protein flexibility. All the complete residues of the protein within the specified range (distance) from the ligand are considered flexible. Default: 2.0.

#### **SetResiduelD**

**bool** SetResidueID (const std::string&)

Sets the residue ID of the residues to be treated as flexible, using regular expressions. If this is specified, the FlexRange is ignored. Default: None.

# 3.1.12 OEProteinLigandOptOptions

class OEProteinLigandOptOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for optimization with OEFixedProteinLigandOptimizer and OEFlexProteinLigandOptimizer.

The OEProteinLigandOptOptions class defines the following public methods:

- · GetGradTolerance and SetGradTolerance
- · GetLigandCharge and SetLigandCharge
- · GetForceField and SetForceField
- · GetMaxIter and SetMaxIter
- · GetNonBondCutoff and SetNonBondCutoff
- · GetOptimizationType and SetOptimizationType
- · GetSolventModel and SetSolventModel

## **Constructor**

```
OEProteinLigandOptOptions();
OEProteinLigandOptOptions (const OEProteinLigandOptOptions &)
```

Default and copy constructors.

#### operator=

OEProteinLigandOptOptions & operator=(const OEProteinLigandOptOptions &)

## **GetGradTolerance**

double GetGradTolerance() const

See SetGradTolerance method.

## GetLigandCharge

const OEProton:: OEChargeEngineBase\* GetLigandCharge() const

See SetLigandCharge method.

## **GetForceField**

const OEFF:: OEComplexFF\* GetForceField() const

See SetForceField method.

## **GetMaxIter**

unsigned GetMaxIter() const

See SetMaxIter method.

## **GetNonBondCutoff**

double GetNonBondCutoff() const

See SetNonBondCutoff method.

#### **GetOptimizationType**

unsigned GetOptimizationType() const

See SetOptimizationType method.

#### **GetSolventModel**

unsigned GetSolventModel() const

See SetSolventModel method.

## **SetGradTolerance**

bool SetGradTolerance (const double)

Sets the gradient tolerance for optimization. Default: 1.e-6.

#### SetLigandCharge

```
bool SetLigandCharge (const unsigned)
bool SetLigandCharge (const std::string&)
bool SetLigandCharge (const OEProton:: OEChargeEngineBase&)
```

Sets the charging method for the ligand. The first overload takes an *unsigned* from the *OELigandChargeType* namespace, and the second overload takes corresponding string values. The final overload allows the use of a userdefined OEChargeEngineBase. Method returns false when the invalid selection is chosen, true otherwise. Default: OELigandChargeType\_CURRENT

## **SetForceField**

```
bool SetForceField(const unsigned)
bool SetForceField(const std::string&)
bool SetForceField(const OEFF:: OEComplexFF&)
```

Sets the force field for optimization. The first overload takes an unsigned from the OEComplexFFType namespace, and the second overload takes corresponding string values. The final overload allows the use of a userdefined OEComplexFF. Method returns false when the invalid selection is chosen, true otherwise. Default: OEComplexFFType\_FF14SB\_SAGE

#### **SetMaxIter**

bool SetMaxIter (const unsigned)

Sets the maximum iterations for optimization. Default: 1000.

## **SetNonBondCutoff**

bool SetNonBondCutoff (const double)

Sets the **Non-bonded interactions cutoff** for optimization. Setting a value of  $0.0$  or less assumes that all interactions should be included without any cutoff. Default: 0.0.

### **SetOptimizationType**

bool SetOptimizationType (const unsigned)

Sets the type for optimization. Allowed methods are defined in the OEOptimizationType namespace. Default is OEOptimizationType\_Cartesian.

#### **SetSolventModel**

bool SetSolventModel (const unsigned)

Sets the solvent model to be used during optimization. Allowed methods are OESO1ventModel\_NoSo1v and OESolventModel\_Sheffield, as defined in the OESolventModel namespace. Default is OESolventModel NoSolv.

# 3.1.13 OEProteinLigandOptResults

class OEProteinLigandOptResults

This class provides results of optimization of a single conformer of a molecule, obtained from OEFixedProteinLigandOptimizer and OEFlexProteinLigandOptimizer calculations.

The OEProteinLigandOptResults class defines the following public methods:

- · GetReturnCode
- · GetInitialEnergies
- · GetFinalEnergies
- GetLigandRMSD
- · GetProteinRMSD
- · GetTotalRMSD

#### **Constructors**

```
OEProteinLigandOptResults()
OEProteinLigandOptResults (const OEProteinLigandOptResults&)
```

Default and copy constructors.

#### operator=

OEProteinLigandOptResults & operator=(const OEProteinLigandOptResults &)

## **GetReturnCode**

unsigned GetReturnCode() const

Returns the calculation return code, defined in OESzybkiReturnCode namespace.

#### **GetInitialEnergies**

const OEFF:: OEComplexEnergies& GetInitialEnergies() const

Returns initial energies of the protein-ligand system, before optimization.

#### **GetFinalEnergies**

const OEFF:: OEComplexEnergies& GetFinalEnergies() const

Returns final energies of the protein-ligand system, after optimization.

#### **GetLigandRMSD**

double GetLigandRMSD() const

Returns the RMSD between the initial and final conformations of the ligand.

## **GetProteinRMSD**

double GetProteinRMSD() const

Returns the RMSD between the initial and final conformations of the protein.

## **GetTotalRMSD**

double GetTotalRMSD() const

Returns the RMSD between the initial and final conformations of the protein-ligand complex.

# 3.1.14 OEFreeFormConf

class OEFreeFormConf

This class represents OEFreeFormConf.

The OEFreeFormConf class defines high level interface for conformer Free Energies calculation. An advanced interface for conformer Free Energies is provided through the derived class OEFreeFormConfAdvanced. All the methods of OEFreeFormConf are also available through the OEFreeFormConfAdvanced class interface.

## **Constructors**

```
OEFreeFormConf()
{\tt OEFreeFormConf}({\tt const~OEFreeFormConfOptions@})OEFreeFormConf (const OEFreeFormConf&)
```

Default and copy constructors.

#### operator=

OEFreeFormConf& operator=(const OEFreeFormConf&)

## **EstimateFreeEnergies**

```
unsigned int EstimateFreeEnergies (OEChem:: OEMCMolBase& mol) const
unsigned int EstimateFreeEnergies (OEChem::OEMCMolBase& mol, OEChem::OEMCMolBase&
→restrictedMol) const
```

Estimates the Gibbs free energy to convert an ensemble of solution conformations into a state where only a single specific conformation is present. Function returns a success or failure code as *unsigned int* from the OEFreeFormReturnCode namespace.

- *mol* Represents the input molecule to estimate the conformer free energies, and on return it is modified to represent the corresponding ensemble of solution conformers. The return ensemble also contains the estimated free energy components.
- **restrictedMol** The restricted conformers of the molecule for which to estimate the restriction energies. The estimated restriction energies are tagged on conformers on return.

## **FindSimilarConfs**

```
unsigned int FindSimilarConfs (OEChem:: OEMCMolBase& mol,
                               const OEChem:: OEMCMolBase& ensemble,
                               const OEChem:: OEConfBase& conf,
                               const OESystem:: OEBinaryPredicate<OEChem:: OEConfBase,
→OEChem::OEConfBase>& condition) const
```

Find similar conformers to the specified one from the given ensemble of conformers, based on *condition* provided. Function returns a success or failure code as *unsigned int* from the OEFreeFormReturnCode namespace. A failure is returned when no matches are found.

*mol* Contains the conformers that are found on return. The found conformers are added to any existing conformers.

ensemble Ensemble of conformers to search from. *conf* Reference conformer used for searching. condition Functor defining the similarity condition.

# 3.1.15 OEFreeFormConfAdvanced

#### class OEFreeFormConfAdvanced

This class represents OEFreeFormConfAdvanced.

The following methods are publicly inherited from OEFreeFormConf:

- · EstimateFreeEnergies
- · FindSimilarConfs

#### **Constructors**

```
OEFreeFormConfAdvanced()
OEFreeFormConfAdvanced(const OEFreeFormConfOptions&)
OEFreeFormConfAdvanced(const OEFreeFormConfAdvanced&)
```

Default and copy constructors.

#### operator=

OEFreeFormConfAdvanced& operator=(const OEFreeFormConfAdvanced&)

#### **EstimateEnergies**

unsigned int EstimateEnergies (OEChem:: OEMCMolBase& mol) const

Estimates the Gibbs free energy to convert an ensemble of solution conformations into a state where only a single specific conformation is present. This method assumes that a duplicate free solution ensemble is provided as input. Function returns a success or failure code as *unsigned int* from the *OEFreeFormReturnCode* namespace. The molecule conformers contain the estimated free energy components on return.

#### **EstimateRestrictionEnergy**

```
unsigned int EstimateRestrictionEnergy (OEChem:: OEMCMolBase& freeMol, const
→OEChem::OEMCMolBase& restrictedMol) const
```

Estimates the restriction energies on the restricted conformers. Function returns a success or failure code as *unsigned* int from the OEFreeFormReturnCode namespace.

freeMol Molecule with unrestricted conformers identified from the set of solution ensemble, corresponding to the restricted conformers. The estimated restriction energies are tagged on conformers on return.

restrictedMol Molecule with the restricted conformers for which to estimate the restriction energies.

#### **IdentifyConformer**

unsigned int IdentifyConformer (OEChem:: OEMCMolBase& mol, const OEChem:: OEMCMolBase&, →ensemble) const

Identifies the given conformers from the solution ensemble. Function returns a success or failure code as *unsigned int* from the OEFreeFormReturnCode namespace.

*mol* Molecule with conformers to be identified from the set of solution ensemble. Conformer free energies from identified conformers are tagged on these conformers on return.

*ensemble* Molecule with the solution ensemble with corresponding conformer free energies.

#### **Optimize**

unsigned int Optimize (OEChem:: OEMCMolBase& mol) const

Optimize the molecule conformers using the optimization options. Function returns a success or failure code as unsigned int from the OEF reeFormReturnCode namespace. The molecule conformers contain optimized geometry and are tagged with estimated energies on return.

#### **OptimizeRestraint**

unsigned int OptimizeRestraint (OEChem:: OEMCMolBase& mol) const

Perform restraint optimization of the molecule conformers using the optimization options. A harmonic restraint is applied to retain the shape of the given conformers. Function returns a success or failure code as *unsigned int* from the OEF reeFormReturnCode namespace. The molecule conformers contain optimized geometry and are tagged with estimated energies on return.

#### **PreOptimizeEnsemble**

unsigned int PreOptimizeEnsemble (OEChem:: OEMCMolBase& mol) const

Optimize the molecule conformers using the pre-optimization options. Function returns a success or failure code as *un*signed int from the OEFreeFormReturnCode namespace. The molecule conformers contain optimized geometry and are tagged with estimated energies on return.

#### **PrepareEnsemble**

```
unsigned int PrepareEnsemble (OEChem:: OEMCMolBase& mol) const
unsigned int PrepareEnsemble (OEChem:: OEMCMolBase& mol, OEChem:: OEMCMolBase&.
→restrictionMol, OEChem:: OEMCMolBase& freeMol) const
```

Generates a comprehensive set of conformer ensemble when desired, using OEOmega. Function returns a success or failure code as *unsigned int* from the OEFreeFormReturnCode namespace. The input molecule is filled with the generated ensemble on return.

Prepares the conformer ensemble for subsequent FreeForm calculations, this includes generation of a comprehensive set of conformers using OEOmega as desired, validation of the structures and charge assignment. The second overload is provided for preparing an ensemble that would include un-restricted (free) conformers corresponding to a set of given restriction ensemble of conformers. Charges are also assigned on the given restriction ensemble of conformers. Function returns a success or failure code as *unsigned int* from the OEFreeFormReturnCode namespace.

mol Molecule with the solution ensemble prepared for FreeFormConf calculations.

restrictionMol Molecule with the restricted conformers.

*freeMol* Molecule with the un-restricted conformers, corresponding to the restricted conformers.

### **RemoveDuplicates**

unsigned int RemoveDuplicates (OEChem:: OEMCMolBase& mol) const

Removes duplicates from the given ensemble of molecule conformers. Function returns a success or failure code as unsigned int from the OEFreeFormReturnCode namespace.

# 3.1.16 OEFreeFormConfOptions

class OEFreeFormConfOptions : public OESystem:: OEOptions

This class represents options for setting up FreeFormConf calculations.

#### **Constructors**

```
OEFreeFormConfOptions()
OEFreeFormConfOptions (const OEFreeFormConfOptions&)
```

Default and copy constructors.

#### operator=

```
OEFreeFormConfOptions& operator=(const OEFreeFormConfOptions&)
```

## **GetCorrSolventOptions**

```
OESzybkiSolventOptions& GetCorrSolventOptions()
const OESzybkiSolventOptions& GetCorrSolventOptions() const
```

Returns a reference to the OESzybkiSolventOptions instance as currently set for solvent correction. When desired, these options are used in applying energetic corrections to the free energy calculations.

#### **GetIonicState**

unsigned int GetIonicState() const

Returns the ionic state to be used for OEFreeFormConf calculations, as *unsigned int* from the OEFreeFormIonicState namespace.

#### **GetOmegaOptions**

```
OEOmegaOptions& GetOmegaOptions()
const OEOmegaOptions& GetOmegaOptions() const
```

Returns a reference to the OEOmegaOptions instance as currently set for ensemble generation. When desired, these options are used in generating the initial ensemble of conformers.

#### **GetOptimizeOptions**

```
OESzybkiOptOptions& GetOptimizeOptions()
const OESzybkiOptOptions& GetOptimizeOptions() const
```

Returns a reference to the OESzybkiOptOptions instance as currently set for tight optimization. These options are used in tight optimization of conformers.

#### **GetPreOptimizeOptions**

```
OESzybkiOptOptions& GetPreOptimizeOptions()
const OESzybkiOptOptions& GetPreOptimizeOptions() const
```

Returns a reference to the OESzybkiOptOptions instance as currently set for pre-optimization. These options are used in loose pre-optimization of conformers to pre-screen and reduce the size of conformers ensemble.

#### **GetSolventOptions**

```
OESzybkiSolventOptions& GetSolventOptions()
const OESzybkiSolventOptions& GetSolventOptions() const
```

Returns a reference to the OESzybkiSolventOptions instance as currently set for solvent. These options are used in defining the solvent for conformers minimization and subsequent entropy calculation.

#### **GetSzybkiGeneralOptions**

```
OESzybkiGeneralOptions& GetSzybkiGeneralOptions()
const OESzybkiGeneralOptions& GetSzybkiGeneralOptions() const
```

Returns a reference to the OESzybkiGeneralOptions instance as currently set. These options are used in defining general environment for all szybki calculations performed from FreeFormConf.

#### **GetUseInputEnsemble**

bool GetUseInputEnsemble() const

Returns the current state of the use input ensemble flag. If true, the input set of ensemble is used as the initial conformers ensemble and no new conformers are generated during FreeFormConf calculations.

#### **GetUseSolventCorr**

bool GetUseSolventCorr() const

Returns the current state of the use solvent correction flag. If true, energetic correction due to solvent interactions is applied after entropy calculation.

# **3.1.17 SetCorrSolventOptions**

**void** SetCorrSolventOptions (const OESzybkiSolventOptions&)

Sets the correction solvent options by passing in an *OESzybkiSolventOptions* instance. When desired, these options are used in applying energetic corrections to the free energy calculations. Default solvent model: OESolventModel\_PB, default atomic radii type: OEAtomicRadii\_ZAP9, default charge model: OEChargeEngineNoOp.

#### **SetIonicState**

bool SetIonicState (const unsigned int)

Sets the ionic state to be used for OEFreeFormConf calculations, as *unsigned int* from the OEFreeFormIonicState namespace. The method returns false when the invalid selection is chosen, true otherwise. Default: OEFreeFormIonicState PH74.

#### **SetOmegaOptions**

const OEOmegaOptions& SetOmegaOptions (const OEOmegaOptions&)

When desired, these op-Sets the omega options by passing in an OEOmegaOptions instance. tions are used in generating the initial ensemble of conformers. Default search force field: OEMMFFSheffieldFFType\_MMFF94S\_SHEFF, default EnergyWindow: 10.0, default IncludeInput: false, default MaxRotors: 20.

### **SetOptimizeOptions**

void SetOptimizeOptions (const OESzybkiOptOptions&)

Sets the optimization options by passing in an  $OESzybkiOptOfptions$  instance. These options are used in tight optimization of conformers. Default optimizer type: OEOpt Type\_NEWTON, default MaxIter: 1000.

#### **SetPreOptimizeOptions**

**void** SetPreOptimizeOptions (const OESzybkiOptOptions&)

Sets the pre-optimization options by passing in an OESzybkiOptOptions instance. These options are used in loose pre-optimization of conformers to pre-screen and reduce the size of conformers ensemble. Default optimizer type: OEOptType BFGS, default MaxIter: 1000, default GradTolerance: 0.005.

### **SetSolventOptions**

void SetSolventOptions (const OESzybkiSolventOptions&)

Sets the solvent options by passing in an OESzybkiSolventOptions instance. These options are used in defining the solvent for conformers minimization and subsequent entropy calculation. Default solvent model: OESolventModel\_Sheffield, default atomic radii type: OEAtomicRadii\_ZAP9, default charge model: OEAM1BCCELF10Charges.

#### **SetSzybkiGeneralOptions**

void SetSzybkiGeneralOptions (const OESzybkiGeneralOptions&)

Sets the general szybki options by passing in an OESzybkiGeneralOptions instance. These options are used in defining the general environment for all szybki calculations performed from FreeFormConf. Default force field: OEForceFieldType\_MMFF94S, default temperature: 298.15K.

#### SetUseInputEnsemble

bool SetUseInputEnsemble(const bool)

Sets the current state of the use input ensemble flag. If true, the input set of ensemble is used as the initial conformers ensemble and no new conformers are generated during FreeFormConf calculations. Default: false.

### **SetUseSolventCorr**

bool SetUseSolventCorr (const bool)

Sets the current state of the use solvent correction flag. If true, energetic correction due to solvent interactions is applied after entropy calculation. Default: false.

# 3.1.18 OEFreeFormSolvOptions

class OEFreeFormSolvOptions : public OESystem:: OEOptions

This class represents OEFreeFormSolvOptions.

#### **Constructors**

OEFreeFormSolvOptions() OEFreeFormSolvOptions (const OEFreeFormSolvOptions&)

Default and copy constructors.

#### operator=

OEFreeFormSolvOptions& operator=(const OEFreeFormSolvOptions&)

### **GetAtomicRadiiType**

**unsigned int** GetAtomicRadiiType() const = 0

Returns the type of atomic radii used for PB calculations. Possible values passed to the method are defined in OEAtomicRadii namespace.

## **GetChargeType**

**unsigned int** GetChargeType() const =  $0$ 

Returns the type of partial charges used for Sheffield and PB calculations.

## **GetConfGenRMS**

**double** GetConfGenRMS() const =  $0$ 

Returns the value of RMSD used by the conformation generator for conformation deduplication. The default values are  $0.6 \text{ Å}$  for solvation free energy estimation and  $0.3 \text{ Å}$  for conformation free energy estimation.

#### **GetIonicState**

**unsigned int** GetIonicState() const =  $0$ 

Returns the type of charge state. Possible values are defined in the OEFreeFormIonicState namespace. The default value is OEFreeFormIonicState PH74.

### **GetMaxConfGen**

```
unsigned int GetMaxConfGen() const = 0
```

Returns the maximum conformations number used by the conformation generator.

## GetUseInput3D

```
bool GetUseInput3D() const = 0Determines if the calculations are set to use 3D coordinates of the input molecule.
```

### **GetUseInputEnsemble**

**bool** GetUseInputEnsemble() const = 0

Determines if the calculations are set to use the input ensemble of conformations rather than generate the ensemble internally.

### **SetAtomicRadiiType**

**bool** SetAtomicRadiiType (unsigned int radii\_type) = 0

Sets the atomic radii type for all PB calculations. Possible values passed to the method are defined in OEAtomicRadii namespace.

## **SetChargeType**

```
bool SetChargeType (unsigned int charge_type) = 0
```

Sets the partial charges type. Possible values to pass to the method are defined in a subset of the 'OEPro*ton::OECharges* ` namespace (please look at the documentation of The **Quacpac TK**.) The allowed types are: OECharges\_NoOp (to use existing partial charges), OECharges\_AM1BCCSym, OECharges\_AM1BCCNoSym, OECharges\_AM1BCCSymSPt, OECharges\_AM1BCCNoSymSPt and OECharges\_MMFF94. The default values are OECharges\_AM1BCCNoSymSPt and OECharges\_AM1BCCSym for solvation free energy estimation and conformation free energy estimation respectively.

## **SetConfGenRMS**

**bool** SetConfGenRMS (**double**  $rms$ ) = 0

Sets the value of RMSD used by the conformation generator for conformation deduplication. The default values are 0.6 Å for solvation free energy estimation and 0.3 Å for conformation free energy estimation.

## **SetlonicState**

**bool** SetIonicState (unsigned int ionic\_state) = 0

Sets the charge state of the molecule. Possible values are defined in the OEF reeFormIonicState namespace. The default value is OEFreeFormIonicState\_PH74.

#### **SetMaxConfGen**

**bool** SetMaxConfGen(*unsigned int nmax*) =  $0$ 

Sets the maximum number of conformations generated by the conformation generator. The default values are 200 for solvation free energy estimation and 20000 for conformation free energy estimation.

#### SetUseInput3D

**bool** SetUseInput3D (**bool** use3D) =  $0$ 

When parameter use3D is set to true, solvation free energy is calculated just for the input structure representing specific conformation. This option allows to find what is the difference in solvation energy between different conformations.

#### **SetUseInputEnsemble**

**bool** SetUseInputEnsemble(**bool** use\_ensemble) = 0

Sets the usage of the input ensemble rather than generating it internally when the parameter use\_ensemble is set to true.

Note: The value set by the OEFreeFormSolvOptions. SetUseInput3D method takes precedence over OEFreeFormSolvOptions. SetUseInputEnsemble. In other words when the first of those methods passes boolean value true, solvation code is looking for a single 3D structure (conformation) provided by the user and determines its solvation free energy. When the value passed by this method is false or when it is not used, solvation code is selecting the lowest force field energy conformation either from the user ensemble (when medthod OEFreeFormSolvOptions. SetUseInputEnsemble passes boolean true) or from the ensemble generated internally and determines its solvation free energy.

# 3.1.19 OEFreeFormSolvResults

class OEFreeFormSolvResults

This class represents OEFreeFormSolvResults.

## **Constructors**

```
OEFreeFormSolvResults()
OEFreeFormSolvResults(const OEFreeFormSolvResults&)
```

Default and copy constructors.

#### operator=

OEFreeFormSolvResults& operator=(const OEFreeFormSolvResults&)

## **GetAtomicPotentials**

void GetAtomicPotentials (std::vector<double>& apot) const

Fills the vector passed as an arguments with calculated atomic potentials. Each calculated atomic potential is a sum of electrostatic and hydrophobic contributions.

#### **GetElectrostaticSolvationFreeEnergy**

double GetElectrostaticSolvationFreeEnergy() const

Returns electrostatic part of solvation free energy after calling OEEstimateSolvFreeEnergy function.

### GetHydrophobicSolvationFreeEnergy

double GetHydrophobicSolvationFreeEnergy() const

Returns hydrophobic part of solvation free energy after calling OEEstimateSolvFreeEnergy function.

#### **GetReturnCode**

**unsigned int** GetReturnCode() const =  $0$ 

Returns one of the values defined in the OEFreeFormReturnCode namespace.

#### **GetSolvationFreeEnergy**

double GetSolvationFreeEnergy() const

Returns total Gibbs free energy of hydration for the input compound after calling OEEstimateSolvFreeEnergy function.

#### **GetWarnings**

**void** GetWarnings (std::vector<unsigned int>& warnings) const = 0

Fills the vector passed as an argument with warning codes relevant to the calculation performed. When no warnings are generated the returned vector is empty.

# 3.1.20 OERestrictionEnergyResult

class OERestrictionEnergyResult

This class represents OERestrictionEnergyResult.

## **Constructors**

```
OERestrictionEnergyResult()
OERestrictionEnergyResult (const OEChem:: OEConfBase&)
{\tt OERestriterionEnergyResult}\ ({\tt const\; OERestriterionEnergyResult\,\&\,})
```

Default and copy constructors.

#### operator=

OERestrictionEnergyResult& operator=(const OERestrictionEnergyResult&)

## **GetGlobalStrain**

double GetGlobalStrain() const

Returns the global strain (in kcal/mol) associated with this conformer, due to being restricted.

## **GetLocalStrain**

double GetLocalStrain() const

Returns the local strain (in kcal/mol) associated with this conformer, due to being restricted.

# 3.1.21 OESingleConfResult

```
class OESingleConfResult
```

This class represents OESingleConfResult. Its purpose is to iterate over conformers in a OEFreeFormConfResults object, giving users access to per-conformer properties. When iterated over the quantities in OEFreeFormConfResults, each entity returns the value for the conformation with id return by the OESingleConfResult.GetConfIdx method.

## **Constructors**

```
OESingleConfResult()
OESingleConfResult (const OEChem:: OEConfBase&)
OESingleConfResult (const OESingleConfResult&)
```

Default and copy constructors.

#### operator=

```
OESingleConfResult& operator=(const OESingleConfResult&)
```

## **GetConfldx**

unsigned int GetConfIdx() const

Returns the conformation id for that conformation.

## **GetDeltaG**

double GetDeltaG() const

Returns the free energy of selecting that conformation from the ensemble.

#### **GetLnQrotational**

double GetLnQrotational() const

Returns the natural logarithm of the rotational partition function for that conformation.

#### **GetLnQvibrational**

```
double GetLnQvibrational() const
```

Returns the natural logarithm of the vibrational partition function for that conformation.

## **GetMMFFEnergy**

double GetMMFFEnergy() const

Returns the total intermolecular MMFF94 energy of that conformation.

### **GetProbability**

double GetProbability() const

Returns the probability of state associated with this conformation.

#### **GetRelativeEnergy**

double GetRelativeEnergy() const

Returns the total relative energy (MMFF94 + solvation energy) for that conformation with respect to the lowest energy conformer of the whole ensemble.

### **GetRelLnQ**

double GetRelLnQ() const

Returns the natural logarithm of the relative vibrational-rotational partition function with respect to the lowest free energy conformer:  $\ln q_{rel,i} = \ln q_i - \ln q_{ref}$ . In that formula the reference conformation is the one with the lowest value returned by the OESingleConfResult.GetDeltaG method. This quantity allows us to calculate conformer relative free energies analogously to conventional relative energies.

### **GetRotationalEntropy**

double GetRotationalEntropy() const

Returns the rotational entropy (in  $J/(mol K)$ ) for that conformation.

#### **GetSolvEnergy**

double GetSolvEnergy () const

Returns the solvation energy for that conformation.

#### **GetTotalEnergy**

double GetTotalEnergy () const

Returns the total energy (MMFF94 + solvation) for that conformation.

### **GetVibrationalEntropy**

double GetVibrationalEntropy() const

Returns the vibrational entropy (in  $J/(mol K)$ ) for that conformation.

# 3.1.22 OEFreeFormConfResults

class OEFreeFormConfResults

This class represents OEFreeFormConfResults.

### **Constructors**

```
OEFreeFormConfResults (const OEChem:: OEMCMolBase&)
OEFreeFormConfResults (const OEFreeFormConfResults&)
```

Default and copy constructors. The first variation of the constructor populates the object by extracting the corresponding tagged values from the molecule.

#### operator=

OEFreeFormConfResults& operator=(const OEFreeFormConfResults&)

#### **GetConfResult**

OESingleConfResult GetConfResult (const unsigned int) const

Returns the OESingleConfResult object corresponding to the specified conformer index.

#### **GetLowestdGConfldx**

unsigned int GetLowestdGConfIdx() const

Returns the conformer index corresponding to the lowest dG.

#### **GetLowestRelEneConfldx**

unsigned int GetLowestRelEneConfIdx() const

Returns the conformer index corresponding to the lowest relative energy.

#### **GetNumUniqueConfs**

unsigned int GetNumUniqueConfs() const

Returns the number of the unique conformations in the ensemble.

#### **PrintTxt**

void PrintTxt (OEPlatform::oeostream& fileStream, const std::string& molName) const

Prints the results in plain text format in the provided output filestream.

## **PrintCsv**

void PrintCsv (OEPlatform::oeostream& fileStream, const std::string& molName) const

Prints the results in comma separated values (CSV) format in the provided output filestream.

#### **GetResultsForConformations**

OESystem::OEIterBase<OESingleConfResult>\* GetResultsForConformations() const

Returns the iterator whose elements are *OESingleConfResult* objects for the ensemble of unique conformations.

#### **GetTemperature**

double GetTemperature() const

Returns temperature for which calculations have been performed.

#### **GetTotalEntropy**

double GetTotalEntropy() const

Returns estimated molar solution entropy for the input compound.

# 3.1.23 OETorsionScanOptions

class OETorsionScanOptions : public OESystem:: OEOptions

This class represents *OETorsionScanOptions*.

#### See also:

- OETorsionScanResult class
- · OETorsionScan function

## **Constructors**

```
OETorsionScanOptions()
OETorsionScanOptions (const OETorsionScanOptions &)
```

Default and copy constructors.

#### operator=

OETorsionScanOptions &operator=(const OETorsionScanOptions &)

Assignment operator.

### **GetDelta**

double GetDelta() const

Returns the value of dihedral angle increase (in degrees).

#### **GetForceFieldType**

```
unsigned int GetForceFieldType() const
```

Returns the type of force field defined.

#### **GetForceField**

const OEMolPotential:: OEGenericFF2\* GetForceField() const

Returns pointer to the user defined force field.

#### **GetMaxIter**

```
unsigned GetMaxIter() const
```

Returns the number of maximum iterations during optimization.

### **GetPenaltyForceConstant**

double GetPenaltyForceConstant () const

Returns force constant for the dihedral angle constraint used for torsion scan.

## **GetTolerance**

double GetTolerance() const

Returns the tolerance during optimization.

### **GetUseInternalCoord**

bool GetUseInternalCoord() const

Returns true if SetUseInternalCoord is set to using 3N-5 internal coordinates for optimization while the torsion selected for scanning is fixed.

### **GetSolvationType**

unsigned int GetSolvationType() const

Returns the type of solvation model used for torsion scan, see OETorsionScanOptions. SetSolvationType for more details.

#### **GetUserDefinedAngles**

std::vector<double> GetUserDefinedAngles() const

Returns vector of user defined dihedral angles for which torsion scan will be done.

### **GetUseSinglePointPB**

bool GetUseSinglePointPB() const

Returns true if the OETorsionScanOptions. SetUseSinglePointPB is set to correcting the torsion scan with a PB solvation energy.

## **GetNumStarts**

unsigned GetNumStarts() const

Returns the number of starts for the torsion scan. See OETorsionScanOptions. SetNumStarts for more details

## **GetOverlapDiv**

unsigned GetOverlapDiv() const

Returns the divisor used for determining the size of the overlaps between starts. See OETOTSionScanOptions. SetOverlapDiv for more details.

### **SetDelta**

bool SetDelta (double delta)

Determines the number of points in that is  $(360.0/delta + 1)$  in the  $[0.0^{\circ}, 360.0^{\circ}]$  range for the scan. Minimum and maximum values are 0.1 and 60.0 degrees respectively. The default value is 5.0 degrees. When the given value of delta is outside the range, false is returned.

#### **SetForceField**

**bool** SetForceField(OEMolPotential::OEGenericFF2& user\_ff)

Sets user defined force field which will be used for torsion scan.

#### **SetForceFieldType**

bool SetForceFieldType (unsigned int type)

Selects the force field for the scan. The allowed values for parameter type are  $OEForceFieldType\_MMFF94S$ (default), OEForceFieldType\_MMFF94, OEForceFieldType\_SMIRNOFF99FROSST, OEForceFieldType\_PARSLEY\_OPENFF100, OEForceFieldType\_PARSLEY\_OPENFF111, OEForceFieldType\_PARSLEY\_OPENFF121, OEForceFieldType\_PARSLEY\_OPENFF131, OEForceFieldType\_SAGE\_OPENFF200, and OEForceFieldType\_SAGE\_OPENFF210 Method returns false if other than the above values are passed.

### **SetMaxIter**

bool GetMaxIter (const unsigned)

Sets the number of maximum iterations for optimization.

#### **SetSolvationType**

bool SetSolvationType (unsigned int type)

Selects the solvation model used for the scan. The allowed values of type are: OESolventModel\_NoSolv(vacuum) and OESolventModel\_Sheffield (aqueous solution, default). Method returns false if invalid solvation model is passed.

#### **SetPenaltyForceConstant**

**bool** SetPenaltyForceConstant (double pfc)

Overwrites a default value  $(1e4)$  for force constant in dihedral angle constraint used for torsion scan. Although for most molecules a default value works fine, in some cases a molecular torsion might be overconstrained or underconstrained. This method allows to avoid those two extremes. Method returns false if invalid value of force constant is passed.

#### **SetTolerance**

bool SetTolerance (const double)

Sets the tolerance limit for optimization.

### **SetUseInternalCoord**

**bool** SetUseInternalCoord(bool useInt)

Overwrites a default method for torsion scan, which applies a large enough penalty force to keep the value of the dihedral angle constant during optimization. When the parameter use Int is set to true, optimization is performed in 3N-5 internal coordinates while the selected torsion for which a scan is done is kept frozen.

### **SetUserDefinedAngles**

**bool** SetUserDefinedAngles (const std:: vector<double>& angles)

Takes a vector of user selected dihedral angles (in deg) for which torsion scan will be done. Vector passed as argument should contain at least 2 values, otherwise false is returned.

## **SetUseSinglePointPB**

**bool** SetUseSinglePointPB (bool usePB)

Corrects the final scan values with a PB solvation energy, when the solvation model is set to OESolventModel\_Sheffield (see OETorsionScanOptions. SetSolvationType). Method returns false if the solvation model is not correctly set.

#### **SetNumStarts**

bool SetNumStarts (unsigned starts)

Sets the number of starts for the torsion scan. The default value is 2, meaning scans will start at 0 and 180 degrees. The scans are performed both forwards and backwards. This setting is not compatible with setting OETorsionScanOptions. SetUserDefinedAngles, and will be ignored in case user defined angles are supplied.

### **SetOverlapDiv**

```
bool SetOverlapDiv(unsigned overlapDiv)
```

Sets the divisor used for determining the size of the overlaps between starts. If set to zero or one, will perform full 360 forwards and backwards scans for each start, meaning the number of starts will increase the computational cost linearly. To prevent the linear increase in cost for additional starts, the overlap divisor in combination with a number of starts  $> 1$ , will first divide the angle space by the number of starts, then to ensure some overlap between the scanned angles will take the remaining space and divide by this value (default value is 4). For example with the default values of 2 starts, scans would be performed from  $0 \rightarrow 180$ ,  $0 \rightarrow -180$ ,  $180 \rightarrow 360$ , and  $180 \rightarrow 0$ . The 180 degree remainder (if a full scan would have been done) is instead divided by 4, which equals 45 degrees, which is then added to each scan to ensure overlaps of the curves. The resulting scan will look like  $0 - >225$ ,  $0 - > -225$ ,  $180 - > 45$ (through  $360$ ), and  $180 \rightarrow -45$ . The larger the overlap divisor the smaller the overlaps between curves. This setting is not compatible with setting OETOrsionScanOptions. SetUserDefinedAngles, and will be ignored in case user defined angles are supplied.

# 3.1.24 OETorsionScanResult

#### class OETorsionScanResult

This class represents OETorsionScanResult.

#### See also:

- OETorsionScanOptions class
- OETorsionScanfunction

#### **Constructors**

```
OETorsionScanResult (double dihedral_angle, double energy)
OETorsionScanResult (const OETorsionScanResult &)
```

Default and copy constructors. Default constructor takes values of torsion angle (in degrees) and corresponding energy (in kcal/mol).

#### operator=

OETorsionScanResult& operator=(const OETorsionScanOptions &)

Assignment operator.

#### **GetAngle**

double GetAngle() const

Returns the value of dihedral angle (in degrees) for a torsion scan point.

## **GetEnergy**

double GetEnergy () const

Returns the value of relative energy (in kcal/mol) for a torsion scan point.

# 3.1.25 OETorsionScanner

```
class OETorsionScanner
```

This class provides an interface to perform potential energy scanning for a selected torsion in the input molecule. Torsion scan is preformed by a series of constrained optimizations in which all internal degrees of freedom but selected torsion, are optimized.

#### See also:

- OETorsionScan method
- OETorsionScanOptions class
- OETorsionScanResult class

#### The OETorsionScanner class defines the following public methods:

- · GetLowestEnergyConfs
- · GetLowestEneResults
- · GetScannedAngles
- GetSinglePointConfs
- $\bullet$  Scan

#### **Constructor**

```
OETorsionScanner();
OETorsionScanner (const OETorsionScanOptions&);
OETorsionScanner (const OETorsionScanner&)
```

Default and copy constructors.

#### operator=

OETorsionScanner &operator=(const OETorsionScanner&)

# 3.1.26 GetLowestEnergyConfs

bool GetLowestEnergyConfs (OEChem:: OEMCMolBase& dst) const

Returns the optimized lowest energy conformers corresponding to each of the angles that scanning was performed. The *Scan* must be performed before calling this method.

# 3.1.27 GetLowestEneResults

OESystem::OEIterBase<OETorsionScanResult>\* GetLowestEneResults() const

Returns the lowest energy scan results corresponding to each of the angles that scanning was performed. The *Scan* must be performed before calling this method.

## 3.1.28 GetScannedAngles

std::vector<double> GetScannedAngles() const

Returns all the angles at which scanning was performed. The *Scan* must be performed before calling this method.

## 3.1.29 GetSinglePointConfs

bool GetSinglePointConfs (OEChem:: OEMCMolBase& mol, const double angle) const

Returns all the optimized conformers corresponding to the specified angle. The Scan must be performed before calling this method.

# 3.1.30 Scan

unsigned Scan (const OEChem:: OEMCMolBase&, const OEChem:: OETorsion&)

Perform torsion scanning for the specified torsion on the input molecule.

# 3.1.31 OEBoundEntropyOptions

class OEBoundEntropyOptions : public OESystem: : OEOptions

This class represents OEBoundEntropyOptions.

See also:

- OEEntropyResults class
- OEBoundLigandEntropy function

#### **Constructors**

```
OEBoundEntropyOptions()
OEBoundEntropyOptions (const OEBoundEntropyOptions &)
```

Default and copy constructors.

#### operator=

OEBoundEntropyOptions & operator= (const OEBoundEntropyOptions &)

Assignment operator.

#### **GetForceField**

const OEFF:: OEComplexFF\* GetForceField() const

Returns pointer to the user defined force field held in the OEBoundEntropyOptions

#### GetLigandCharge

const OEProton:: OEChargeEngineBase\* GetLigandCharge () const

See SetLigandCharge method.

#### **SetForceField**

bool SetForceField (unsigned int ftype)

Sets force field used to estimate entropy, by selecting a value of ftype from the *oe:constnamespace:* OESz::OEComplexFFType namespace. Returns false for invalid selection, true otherwise.

### SetLigandCharge

bool SetLigandCharge (const OEProton:: OEChargeEngineBase&)

Selects the method for ligand partial charges assigment. Method takes a user-defined instance of OEChargeEngineBase. It returns false when the invalid selection is chosen, true otherwise.

# 3.1.32 OELigandEntropyOptions

class OELigandEntropyOptions : public OESystem:: OEOptions

This class represents *OELigandEntropyOptions*. It is used for entropy estimation of free ligands in solution or in vacuum.

See also:

• OEEntropyResults class

• OELigandEntropy function

### **Constructors**

```
OELigandEntropyOptions()
OELigandEntropyOptions (const OELigandEntropyOptions &)
```

Default and copy constructors.

### operator=

OELigandEntropyOptions & operator=(const OELigandEntropyOptions &)

Assignment operator.

## **GetEnvironment**

unsigned int GetEnvironment () const

Returns one of 2 types of environement Gas, Solution

## **GetForceField**

const OEMolPotential:: OEForceField\* GetForceField() const

Returns pointer to the user defined force field held in the OELigandEntropyOptions

### GetLigandCharge

const OEProton:: OEChargeEngineBase\* GetLigandCharge () const

See SetLigandCharge method.

## **SetEnvironment**

bool SetEnvironment (unsigned int etype)

Selects solution (etype =  $OEEnvType\_Solution$ ) or gas (etype =  $OEEnvType\_Gas$ ) state.

## **SetForceField**

```
bool SetForceField(const unsigned)
bool SetForceField(const std::string&)
bool SetForceField(const OEMolPotential::OEForceField&)
```

Sets force field used to estimate entropy. The first two overloads accept predefined constants and the last overload allows to pass in a custom forcefield. Available predefined values are: MMFF94, MMFF94S, PARSLEY\_OPENFF, and SAGE\_OPENFF. Default: sage

#### SetLigandCharge

```
bool SetLigandCharge (const OEProton:: OEChargeEngineBase&)
```

Selects the method for ligand partial charges assigment. Method takes a user-defined instance of OEChargeEngineBase. It returns false when the invalid selection is chosen, true otherwise.

## 3.1.33 OEEntropyResults

```
class OEEntropyResults
```

This class represents OEEntropyResults.

#### See also:

- OEBoundEntropyOptions class
- OELigandEntropyOptions class
- · OEBoundLigandEntropy function
- OELigandEntropy function

### **Constructors**

```
OEEntropyResults()
OEEntropyResults (const OEEntropyResults&)
```

Default and copy constructors.

#### operator=

 ${\tt OEEntropyResults} \verb|& \texttt{operator=} (const \verb| OEEntropyResults| & \tt)$ 

Assignment operator.

## GetTotalEntropy in J/(mol K).

double GetTotalEntropy() const

Returns the value of total ligand entropy.

### GetConfigurationalEntropy

double GetConfigurationalEntropy() const

Returns the value of configurational entropy in  $J/(mol K)$ .

## **GetTranslationalEntropy**

double GetTranslationalEntropy() const

Returns the value of translational entropy in J/(mol K).

### **GetVibrationalRotationalEntropy**

double GetVibrationalRotationalEntropy() const

Returns a sum of vibrational and rotational entropy in J/(mol K).

#### **GetSolvationEntropy**

double GetSolvationEntropy () const

Returns the value of solvation entropy in  $J/(mol K)$ .

### **SetResults**

**void** SetResults (const double\* data, unsigned int nterms =  $4$ )

Allows to set the OEEntropyResults <OESz\_OEEntropyResults> object with numeric values of entropy components by passing a pointer to the array of doubles in the following order:  $data[0]$ : total entropy,  $data[1] = translational$ entropy,  $data[2]$  = rotvib entropy and  $data[3]$ : solvation entropy

# **3.2 OESz Constants**

# 3.2.1 OEEntropyMethod

This namespace contains constants describing the type of Hessian used for vibrational entropy calculations.

## **QNewton**

Hessian matrix is obtained from Quasi-Newton optimization.

#### **Analytic**

Hessian matrix is calculated analytically.

## **ExternalHessian**

Hessian matrix is imported instead of being calculated.

# 3.2.2 OEEnvType

This namespace contains constants describing the type of environment for entropy calculations to be used.

#### Gas

Gas-phase molecule.

#### **SolutionSPT**

Molecule in solution for which hydrophobic solvation is described with the Scaled Particle Theory (SPT).

## **SolutionSA**

Molecule in solution for which hydrophobic solvation is described with the Surface Area (SA) model

#### **Protein**

Molecule in the protein binding-site.

## **Solution**

Same as *oe:constant::SolutionSPT* 

# 3.2.3 OEForceFieldType

This namespace contains constants describing the force field type

## MMFF94

Standard MMFF94 force field. (String value: mmff94)

## MMFF94S

A version of MMFF94 with modified out-of-plane and torsional parameters. This force-field describes time-averaged structures mainly for trigonal nitrogen centers. (String value: mmff94s)

## **MMFF AMBER**

A combined force field which can be used for the optimization of the ligand in the rigid protein only. Can't be applied for free ligand. In this potential ligand internal degrees of freedom are handled by the MMFF94 force field, while protein-ligand interactions (vdW and Coulomb) are described by Amber force field.

## **MMFFS AMBER**

As above, but with MMFF94S forcefield applied for ligand intramolecular interactions.

## **MMFF\_IEFF**

A combined force field which can be used for the optimization of the ligand inside a protein receptor or for the optimization of a cluster of molecules. In this force field ligand internal molecular degrees of freedom are handled by the MMFF94, while all intermolecular interactions are calculated with the IEFF potential described in [Hamaguchi-2012].

## **MMFFS IEFF**

As above, but with the MMFF94S forcefield applied for all intramolecular interactions.

### SMIRNOFF99FROSST

SMIRNOFF99FROSST force field.

## PARSLEY\_OPENFF100

Parsley OpenFF1.0.0 force field.

## PARSLEY\_OPENFF111

Parsley OpenFF1.1.1 force field.

## PARSLEY\_OPENFF121

Parsley OpenFF1.2.1 force field.

## PARSLEY\_OPENFF131

Parsley OpenFF1.3.1 force field.

## PARSLEY\_OPENFF

The latest version of Parsley OpenFF force field (String value: parsley)

## SAGE\_OPENFF200

Sage OpenFF2.0.0 force field.

## **SAGE OPENFF210**

Sage OpenFF2.1.0 force field.

## **SAGE OPENFF**

The latest version of Sage OpenFF force field (String value: sage)

## FF14SB\_SMIRNOFF

Combined Amber/ff14SB - PARSLEY\_OPENFF or (Amber/ff14SB - SAGE\_OPENFF) force field which might be used to optimize a part of protein including cofactor. Protein part will be described with Amber/ff14SB parameters while cofactor with PARSLEY\_OPENFF131 or SAGE\_OPENFF200.

Note: Using SMIRNOFF99FROSST, PARSLEY\_OPENFF100, PARSLEY\_OPENFF111, PARSLEY\_OPENFF121, PARSLEY\_OPENFF131, SAGE\_OPENFF200 and FF14SB\_SMIRNOFF force fields requires that the input molecule(s) have assigned atomic partial charges. For small molecules we recommend using AMABCC-ELF10 partial charges while for proteins we suggest using AMBER partial charges.

# 3.2.4 OEOptType

This namespace contains constants describing the type of optimization method to be used.

## **BFGS**

This flag sets the Broyden–Fletcher–Goldfarb–Shanno (BFGS) optimizer. It is the default optimizer in Szybki.

## **CG**

This flag selects the conjugate gradient optimizer instead of the default  $OEOptType\_BFGS$ .

## **SD**

This flag selects the steepest descent optimizer.

### **SD BFGS**

This flag selects 5 steps of  $OEDptType\_SD$  pre-optimization followed by complete BFGS optimization.

## SD CG

This flag selects 5 steps of  $OEDp$ t Type\_SD pre-optimization followed by complete CG optimization.

### **NEWTON**

This flag selects Newton optimizer. It includes 1-20 steps of  $OEOptType\_SD$  preconditioning depending on initial gradients and the size of the input molecule.

# **3.2.5 OEPotentialTerms**

This namespace contains constants describing potential terms which might be calculated in different Szybki runs. Entries: OEPotentialTerms\_VdW, OEPotentialTerms\_Coulomb, OEPotentialTerms\_Bond, OEPotentialTerms Bend, OEPotentialTerms StretchBend, OEPotentialTerms Torsion and OEPotentialTerms\_ImproperTorsion correspond to the total MMFF94 or Smirnoff potential terms. In the case of partial optimization of the protein, entries with a prefix Ligand refer to the force field terms of the ligand (for example OEPotentialTerms\_LigandVdW), while entries with a prefix Protein (for example OEPotentialTerms\_ProteinVdW) are for the MMFF94 or Smirnoff terms of the flexible part of the protein. Force field terms describing VdW and Coulomb interactions between the ligand and the flexible part of the protein are defined with the constants OEPotentialTerms\_ProteinLigandVdW OEPotentialTerms\_ProteinLigandCoulomb and respectively. Term OEPotentialTerms\_ProteinLigandInteraction describes complete ligand-protein interaction according to the protein electrostatic model chosen. Values defined by OEPotentialTerms\_SheffieldSolvation, OEPotentialTerms PBSolvation and OEPotentialTerms\_CavitySolvation refer to solvation energies used to optimize a  $lig$ and in solution, while the term OEPotentialTerms\_HarmonicConstraint determines the he value of the imposed harmonic constraint. OEPotentialTerms\_VdWProteinLigand, Entries: OEPotentialTerms\_CoulombProteinLigand, OEPotentialTerms ProteinDesolvation, OEPotentialTerms LigandDesolvation, OEPotentialTerms SolventScreening, OEPotentialTerms\_ExactCoulomb OEPotentialTerms\_GridCoulomb and are used to break down the total protein-ligand interaction energy into components. Value of the  $% \left( \left( \mathcal{A},\mathcal{A}\right) \right) =\left( \mathcal{A},\mathcal{A}\right)$  of OEPotentialTerms\_ProteinPseudoLigandInteraction represents the interaction the flexible part of of the optimized protein-ligand system (ligand + flexible part of the protein) with the rest of the protein and as such is not an observable quantity. When Amber force field is applied for protein-ligand interaction, values of OEPotentialTerms\_ProteinLigandAmberVdW and OEPotentialTerms\_ProteinLigandAmberCoulomb are used for the corresponding vdW and Coulomb protein-ligand energies. Term OEPotentialTerms\_TorsionHarmonicConstraint is the value of Two terms: OEPotentialTerms\_IEFFInteraction and the constraint torsion harmonic potential. OEPotentialTerms\_InterLigandIEFF are IEFF energies, total and interligand respectively. The latter has nonzero value when more than one ligand are present in the active site of the protein.

## VdW

Value of vdW energy

## **Coulomb**

Value of Coulomb energy

## **Bond**

Value of bond stretch energy

## **Bend**

Value of angle bend energy

# **StretchBend**

Value of stretch-bend energy. This potential term appears only when MMFF force field is used

## **Torsion**

Value of torsion energy

## **ImproperTorsion**

Value of improper torsion energy

## LigandVdW

Value of ligand vdW energy

## **LigandCoulomb**

Value of ligand Coulomb energy

## **LigandBond**

Value of ligand bond energy

## **LigandBend**

Value of ligand angle bend energy

## **LigandStretchBend**

Value of ligand stretch-bend energy. This potential term appears only when MMFF force field is used

## **LigandTorsion**

Value of ligand torsion energy

## **LigandImproperTorsion**

Value of ligand improper torsion energy

## **ProteinVdW**

Value of protein vdW energy

## **ProteinCoulomb**

Value of protein Coulomb energy

# **ProteinBond**

Value of protein bond energy

## **ProteinBend**

Value of protein angle bend energy

# **ProteinStretchBend**

Value of protein stretch-bend energy. This potential term appears only when MMFF force field is used

## **ProteinTorsion**

Value of protein torsion energy

## **ProteinImproperTorsion**

Value of protein improper torsion energy

## ProteinLigandVdW

Value of protein-ligand vdW energy

## ProteinLigandCoulomb

Value of protein-ligand Coulomb energy

## ProteinLigandInteraction

Value of total protein-ligand interaction

# **SheffieldSolvation**

Value of Sheffield solvation energy

## **HarmonicConstraint**

Value of atom harmonic constraint energy

# **PBSolvation**

Value of PB solvation energy

## **CavitySolvation**

Value of cavity solvation energy

## VdWProteinLigand

Value of protein-ligand vdW interaction energy

## **CoulombProteinLigand**

Value of protein-ligand Coulomb interaction energy

## **ProteinDesolvation**

Value of protein desolvation energy

## **LigandDesolvation**

Value of ligand desolvation energy

## **SolventScreening**

Value of PB solvent screening energy

## **GridCoulomb**

Value of protein-ligand Coulomb energy on grid

# **ExactCoulomb**

Value of exact protein-ligand Coulomb energy

## ProteinPseudoLigandInteraction

Value of ligand and flexible protein (pseudoligand) interaction with the rest of the protein energy

## ProteinLigandAmberVdW

Value of Amber protein-ligand vdW energy

## ProteinLigandAmberCoulomb

Value of Amber protein-ligand Coulomb energy

## **TorsionHarmonicConstraint**

Value of torsion harmonic constraint energy

## **IEFFInteraction**

Value of total IEFF intermolecular energy

## **InterLigandIEFF**

Value of interligand IEFF energy

### **Max**

Number of potential terms

# 3.2.6 OEProteinElectrostatics

This namespace contains constants describing handling of protein-ligand electrostatics.

## **NoElectrostatics**

No protein-ligand electrostatic interaction included.

## **GridPB**

Protein electrostatic potential as a solution of PB equation is stored on a grid and used to calculate its electrostatic interaction with any ligand placed inside the protein.

## **GridCoulomb**

Protein Coulomb electrostatic potential is stored on a grid and used to calculate its electrostatic interaction with any ligand placed inside the protein.

## **ExactCoulomb**

Exact Coulombic potential used to calculate protein-ligand electrostatic interaction.

## **SolventPBForces**

Complete PB protein-ligand interaction in solvent is used. Electrostatic protein-ligand interaction is a sum of Coulomb, solvent screening, protein desolvation and ligand desolvation terms.

# 3.2.7 OERunType

This namespace contains constants describing the type of optimization run.

## **SinglePoint**

Indicates a single-point geometry run.

## **TorsionsOpt**

Optimization in torsional coordinates. In the case of a ligand in the protein active site, translational and rotational degrees of freedom are included in the optimization. Terms torsional coordinates defines a set of rotors in the molecules. Numerical values of torsional coordinates are dihedral angles defined by Cartesian coordinates of 4 bonded atoms  $a-b-c-d$  where the middle bond between atoms b and c is a rotatable bond. Please look at the OEChem documentation for the definition of rotatable bond. Bonds a-b and c-d are selected arbitrarily but uniquely, so a single dihedral angle is assigned to each torsional coordinate. Torsional coordinates are a subset of torsional space, however usually the latter term is used synonymously with the former.

## **CartesiansOpt**

Optimization in atomic Cartesian coordinates.

## **SolidBodyOpt**

This flag applies only for the optimization of a ligand inside the protein. Both translational and rotational degrees of freedom are optimized. Term solid body optimization means that only 6 degrees of freedom are allowed to change during optimization. Those are 3 translational and 3 rotational degrees of freedom. In our implementation 3 rotational degrees of freedom are described by 4 quaternions. Please consult any molecular physics or mechanics textbook for the definition of terms translational-rotational degrees of freedom and quaternions.

# 3.2.8 OESolventModel

This namespace contains constants describing solvation model of a molecule in solution

## **NoSolv**

No solvation. Gas-phase molecule.

## **Sheffield**

Simplified analytical electrostatic solvation model used.

## **PB**

Poisson-Boltzmann electrostatic solvation model used.

## **Cavity**

Surface Area hydrophobic solvation model used. It might be used in combination with electrostatic PB or Sheffield solvation models.

# 3.2.9 OEAtomicRadii

This namespace contains constants describing atomic radii used for PB calculations

## **Bondi**

Default set.

## ZAP9

Special set of atomic radii described in ([Nicholls-2010]).

# ZAP7

Special set of atomic radii described in ([Nicholls-2010]).

# 3.2.10 OEProtFlex

This namespace contains constants describing partial flexibility of protein receptor which are included during bound ligand optimization.

## **NoFlex**

No protein-flexibility.

## **PolarH**

Polar hydrogens (for example hydroxyl hydrogens in serine) within specified distance from a ligand will be optimized.

## **SideChains**

Residue side chains within specified distance from a bound ligand will be optimized.

## **Residues**

Complete residues within specified distance from a bound ligand will be optimized.

## **ResidueList**

Complete residues specified by the user will be optimized.

## **SideChainsList**

Residue side chains specified by the user will be optimized.

## **PolarHResList**

Polar hydrogens of residues specified by the user will be optimized.

# 3.2.11 OEFreeFormIonicState

This namespace contains constants describing the charge state of a molecule for solvation free energy estimation or conformations free energies in solution.

## **Uncharged**

Neutral molecule.

## **PH74**

Charge state corresponding to physiological  $pH = 7.4$ .

## Input

Charge state is determined in the molecular input file.

## **Default**

Same as PH74 above.

# 3.2.12 OEFreeFormReturnCode

This namespace contains constants describing the status of the FreeForm runs.

## **Success**

Normal execution.

## **AtomTypeFailure**

Failed to assign MMFF94 atom types.

## **ImplicitHydrogens**

Input molecule contains implicit hydrogens.

## **InputGeometry**

3D structure of the input molecule is badly defined.

### **No3DCoordinates**

Input molecule has no 3D coordinates.

# **ConfGenFailure**

Failed to generate conformations.

### **TooManyRotors**

Input molecule contains too many rotors.

## **ChargeMismatch**

Total formal charge of the molecule is different than the sum of partial charges.

### **NotSupportedCharges**

Attempt to use not supported by FreeForm partial charges type.

## **UnrecognizedChargeState**

Wrong charge state of the molecule.

## **UnsupportedRadiiType**

Radii type not supported by FreeForm.

## **ChargeAssignFailure**

Failed to assign atomic partial charges.

## **GraphMismatch**

Cannot use molecules with dissimilar graphs.

## **UnequalNumConfs**

Number of conformers in two MCMols are different.

## **PartnerConfNotFound**

A corresponding conformer does not exist.

## **MissingPartnerConf**

Partner conformer information does not exist.

## **MissingFFConfEne**

FreeFormConf free energies do not exist.

# 3.2.13 OEFreeFormWarning

This namespace contains constants describing warnings produced by FreeForm runs.

## **UnspecifiedStereo**

Input molecule contains chiral atoms with unspecified stereo configuration.

## **NotRemovableCharge**

Input molecule can't be neutralized.

### **HSamplingSkipped**

Hydrogen atom sampling during conformation generation was not performed.

### **Missing3DCoordinates**

Input ensemble can't be used because input molecular file has no 3D coordinates.

### **ZeroPartialCharges**

Input molecule does not contain any partial charges.

# **3.3 OESz Functions**

# 3.3.1 OEEstimateConfFreeEnergies

```
bool OEEstimateConfFreeEnergies (OEFreeFormConfResults& results,
                                 OEChem:: OEMCMolBase& moldst,
                                 const OEChem:: OEMCMolBase& molsrc,
                                 const OEFreeFormConfOptions& opts)
```

Warning: This function should not be used on 32-bit platforms because the memory requirements are too high.

Estimates the Gibbs free energy to convert an ensemble of solution conformations into a state where only a single specific conformation is present as described in the theory section. Function returns true if the calculation was successful, false otherwise. Results are accessible from the results object (see OEFreeFormConfResults). The ensemble of unique conformations is returned as a multiconformer molecule moldst. The third argument represents the input molecule, and the last one contains user selected options (see OEFreeFormConfOptions).

# 3.3.2 OEEstimateSolvFreeEnergy

bool OEEstimateSolvFreeEnergy (OEFreeFormSolvResults& results, OEChem:: OEMolBase& dst, const OEChem:: OEMCMolBase& src, const OEFreeFormSolvOptions& opts) Estimates the Gibbs energy of solvation, according to the algorithm described in the theory section. Function returns true if the calculation was successful, false otherwise. Results are accessible from the results object (see OE-FreeFormSolvResults). The second parameter returns the molecule representing the structure selected by the algorithm for solvation calculation. Third and fourth arguments are the input molecule and an object containing user options (see OEFreeFormSolvOptions) respectively.

# 3.3.3 OEGetEnergyTermName

const char \*OEGetEnergyTermName (unsigned int)

# 3.3.4 OEGetFreeFormError

std::string OEGetFreeFormError(const unsigned int)

Returns error messages corresponding to return codes defined in OEFreeFormReturnCode namespace.

# 3.3.5 OEGetSzybkiError

std::string OEGetSzybkiError(const unsigned)

Returns error messages corresponding to return codes defined in OESzybkiReturnCode namespace.

# 3.3.6 OESzybkiGetArch

const char \*OESzybkiGetArch()

# 3.3.7 OESzybkiGetLicensee

**bool** OESzybkiGetLicensee(std::string &licensee)

# 3.3.8 OESzybkiGetPlatform

const char \*OESzybkiGetPlatform()

# 3.3.9 OESzybkiGetRelease

const char \*OESzybkiGetRelease()

# 3.3.10 OESzybkiGetSite

**bool** OESzybkiGetSite(std::string &site)

# 3.3.11 OESzybkiGetVersion

```
unsigned int OESzybkiGetVersion()
```

# 3.3.12 OETorsionScan

| OESystem::OEIterBase<OETorsionScanResult>* OETorsionScan(OEChem::OEMCMolBase& dst, |
|------------------------------------------------------------------------------------|
| ↪ const OEChem::OEMCMolBase& src,                                                  |
| ↪ const OEChem::OETorsion& torsion,                                                |
| ↪ const OETorsionScanOptions& opts)                                                |

Performs potential energy scan for a selected torsion in the input molecule. Torsion scan is preformed by a series of constrained Newton optimizations in which all internal degrees of freedom but selected torsion, are optimized. Returns an iterator to the OETorsionScanResult objects from which the user can obtain actual values of the torsion angle within  $[0.0^{\circ}, 360.0^{\circ}]$  range and the corresponding relative energies.

dst The output multi-conformation molecule that stores conformations corresponding to the points on the scan.

src The input molecule of which torsion is scanned.

*torsion* The torsion of the input molecule that is being scanned.

opts The option that stores parameters for the scan such as force field, environment (vacuum or solution), and resolution (OETorsionScanOptions).

**Note:** Using multiple conformations for the input molecule (src) is not a requirement as the function will work for a single conformation. However using as many as possible conformations is recommended because it increases the probability of finding the minimum energy path for a given torsion. The indication that the torsion profile is not the minimum energy path is the occurrence of sharp drop(s) of potential energy, or/and different energy values obtained for 0.0 and 360.0 degrees. Increasing the number of the input geometries in such a situation might remove those symptoms.

Note: As the function is identifying the minimum energy path the output conformations can come from different input conformations this means the SD data from the input conformations is not passed through to the output molecule.

#### See also:

- OETorsionScanOptions class
- OETorsionScanResult class

Example to scan all torsions of a molecule:

```
outmol = oechem. OEMol()
opts = oeszybki.OETorsionScanOptions()
opts.SetDelta(30.0)
opts.SetForceFieldType(oeszybki.OEForceFieldType_MMFF94)
opts.SetSolvationType(oeszybki.OESolventModel_NoSolv)
for tor in oechem. OEGetTorsions (mol) :
    print ("Torsion: %d %d %d" %
           ({\tt tor.a.GetIdx}~()~,\verb|~tor.b.GetIdx|)~,\verb|~tor.c.GetIdx|)~,\verb|~tor.d.GetIdx())~)for res in oeszybki. OETorsionScan (outmol, mol, tor, opts):
        print ("%.2f %.2f" % (res. GetAngle(), res. GetEnergy()))
```

# 3.3.13 OEBoundLigandEntropy

```
unsigned OEBoundLigandEntropy (OEEntropyResults& res,
                               const OEChem:: OEMolBase& protein,
                               const OEChem:: OEMCMolBase& poses,
                               const OEBoundEntropyOptions& opts =
\rightarrowOEBoundEntropyOptions())
unsigned OEBoundLigandEntropy (OEEntropyResults& res,
                               const OEBio:: OEDesignUnit& du,
                               const unsigned int proteinMask,
                               const OEChem:: OEMCMolBase& poses,
                               const OEBoundEntropyOptions& opts =
→OEBoundEntropyOptions())
```

Estimates entropy of a ligand bound in the rigid protein receptor. Returns error messages corresponding to the return codes defined in OESzybkiReturnCode namespace.

res Instance or the results class from which numerical entropy values can be retrieved. OEEntropyResults.

*protein* Protein receptor object.

- du In the second overloaded function, instead of a protein molecule, a design unit object is used. The advantage of this alternative method is a possibility of including cofactors, solvent and other molecules which are present in the
- *poses* Ensemble of poses for which ligand bound entropy will be estimated.
- *opts* The option that stores parameters for entropy estimation, in particular force field and charging method used to assigned partial charges to a ligand. OEBoundEntropyOptions.

# 3.3.14 OELigandEntropy

```
unsigned OELigandEntropy (OEEntropyResults& res,
                         const OEChem:: OEMCMolBase& ensemble,
                         const OELigandEntropyOptions& opts =
→OELigandEntropyOptions())
```

Estimates entropy of a free ligand in solution or in vacuum. Returns error messages corresponding to the return codes defined in OESzybkiReturnCode namespace.

res Instance or the results class from which numerical entropy values can be retrieved. OEEntropyResults.

ensemble Ensemble of conformations for which free ligand entropy will be estimated

opts The option that stores parameters for entropy estimation, in particular force field and charging method used to assigned partial charges to a ligand. OELigandEntropyOptions.

## See also:

- OEEntropyResults class
- OEBoundEntropyOptions class
- OELigandEntropyOptions class

# **FOUR**

# **PRELIMINARY API**

# **4.1 OESz Classes**

# 4.1.1 OEFixedProteinLigandOptimizer

class OEFixedProteinLigandOptimizer

This class provides an interface to optimize a ligand in a protein active site, where the protein is kept fixed during the optimization. The protein active site can be defined either by using a OEDesignUnit or by simple passing in a protein molecule.

The OEFixedProteinLigandOptimizer class defines the following public methods:

- Energy
- · Optimize
- SetProtein

## **Constructor**

```
OEFixedProteinLigandOptimizer();
OEFixedProteinLigandOptimizer(const OEProteinLogandOptOptions&);
OEFixedProteinLigandOptimizer(const OEFixedProteinLigandOptimizer &)
```

Default and copy constructors.

### operator=

OEFixedProteinLigandOptimizer & operator=(const OEFixedProteinLigandOptimizer &)

# 4.1.2 Energy

```
OESystem:: OEIterBase<OEFF:: OEComplexEnergies>* Energy(const
→OEChem::OEMCMolBase& ligand) const
unsigned Energy (OEFF:: OEComplexEnergies& res, const OEChem:: OEMolBase&
\rightarrowligand) const
```

Calculate the single point energy of the ligand interacting with the protein. The intra-molecular protein energy components are ignored by this method. The second overload returns a value from the  $OESzybkiReturnCode$  namespace reporting the success or failure of the calculation.

# 4.1.3 Optimize

```
OESystem::OEIterBase<OESz::OEProteinLigandOptResults>*,
→Optimize (OEChem:: OEMCMolBase& ligand) const
unsigned Optimize (OESz:: OEProteinLigandOptResults& res, OEChem:: OEMolBase&
\rightarrowligand) const
```

Optimize the ligand in the protein active site. The intra-molecular protein energy components are ignored by this method. The second overload returns a value from the OESzybkiReturnCode namespace reporting the success or failure of the optimization. The return code for each conformer in the first overload can be obtained from the corresponding results object.

# 4.1.4 SetProtein

```
unsigned SetProtein (const OEBio:: OEDesignUnit& du, const unsigned
\rightarrowproteinMask);
unsigned SetProtein (const OEChem:: OEMolBase& mol) ;
```

Set the protein molecule for the calculation. In the first overload, the protein Mask define the portion of the OEDesignUnit that should be used as the target protein active site. Method returns a value from the OESzybkiReturnCode namespace reporting the success or failure. The return code for each conformer in the first overload can be obtained from the corresponding results object.

## 4.1.5 OEFlexProteinLigandOptimizer

```
class OEFlexProteinLigandOptimizer
```

This class provides an interface to optimize a ligand in a protein active site, where the protein can be treated a partially flexible. The protein active site can be defined either by using a OED esignUnit or by simple passing in a protein molecule.

The OEFlexProteinLigandOptimizer class defines the following public methods:

- Energy
- · Optimize

#### **Constructor**

```
OEFlexProteinLigandOptimizer();
OEFlexProteinLigandOptimizer(const OEProteinLogandOptOptions&);
OEFlexProteinLigandOptimizer(const OEFlexProteinLigandOptimizer &)
```

Default and copy constructors.

#### operator=

OEFlexProteinLigandOptimizer & operator= (const OEFlexProteinLigandOptimizer &)

# 4.1.6 Energy

```
unsigned Energy (OEFF:: OEComplexEnergies& res, const OEBio:: OEDesignUnit& du,
               const unsigned proteinMask, const unsigned ligandMask,
               const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
\rightarrowprotFlexPred) const;
unsigned Energy (OEFF:: OEComplexEnergies& res, const OEChem:: OEMolBase&
→protein, const OEChem:: OEMolBase& ligand,
               const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&...
→protFlexPred) const;
unsigned Energy (OEFF:: OEComplexEnergies& res, const OEBio:: OEDesignUnit& du,
               const unsigned proteinMask, const unsigned ligandMask, const
→OEProteinFlexOptions& flexOpts) const;
unsigned Energy (OEFF:: OEComplexEnergies& res, const OEChem:: OEMolBase&,
→protein, const OEChem:: OEMolBase& ligand,
               const OEProteinFlexOptions& flexOpts) const;
```

Calculate the single point energy of the protein ligand complex. Only the flexible portion of the intramolecular protein energy components are considered by this method. The methods return a value from the OESzybkiReturnCode namespace reporting the success or failure of the calculation.

# 4.1.7 Optimize

```
unsigned Optimize (OESz:: OEProteinLigandOptResults& res, OEBio:: OEDesignUnit&
\rightarrowdu.
                  const unsigned proteinMask, const unsigned ligandMask,
                   const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
→protFlexPred) const;
unsigned Optimize (OESz:: OEProteinLigandOptResults& res, OEChem:: OEMolBase&
→protein, OEChem:: OEMolBase& liqand,
                  const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>&
→protFlexPred) const;
unsigned Optimize (OESz::OEProteinLigandOptResults& res, OEBio::OEDesignUnit&
\rightarrowdu,
                  const unsigned proteinMask, const unsigned ligandMask,
→ const OEProteinFlexOptions& flexOpts) const;
unsigned Optimize (OESz:: OEProteinLigandOptResults& res, OEChem:: OEMolBase&
→protein, OEChem:: OEMolBase& ligand,
                  const OEProteinFlexOptions& flexOpts) const;
```

Optimize the protein ligand complex. Only the flexible portion of the intra-molecular protein energy components are considered by this method. The methods return a value from the OESzybkiReturnCode namespace reporting the success or failure of the calculation.

# **4.2 OESz Constants**

# 4.2.1 OEComplexFFType

This namespace contains constants describing the force field type

## MMFF94

Standard MMFF94 force field. Corresponding string value: mmff94

#### **MMFF94S**

A version of MMFF94 with modified out-of-plane and torsional parameters. This force-field describes time-averaged structures mainly for trigonal nitrogen centers. Corresponding string value: mmff94s

#### **MMFF AMBER**

A force field that combines MMFF and Amber force fields. In this potential both the protein and ligand internal degrees of freedom are handled by the MMFF94 force field, while protein-ligand interactions are described by Amber force field. Corresponding string value: mmff\_amber

#### **MMFFS AMBER**

As above, but with MMFF94S forcefield applied for intramolecular interactions. Corresponding string value: mmffs\_amber

#### **FF14SB PARSLEY**

A force field that combines FF14SB and Parsley force fields. In this potential protein internal degrees of freedom are handled by the FF14SB force field and ligand internal degrees of freedom are handled by the Parsley force field. The inter-molecular protein-ligand interactions are described by use of appropriate mixing rules for the individual atom interaction potentials. Corresponding string value: ff14sb\_parsley

### FF14SB SAGE

A force field that combines FF14SB and Sage force fields. In this potential protein internal degrees of freedom are handled by the FF14SB force field and ligand internal degrees of freedom are handled by the Sage force field. The inter-molecular protein-ligand interactions are described by use of appropriate mixing rules for the individual atom interaction potentials. Corresponding string value: ff14sb\_sage

# 4.2.2 OELigandChargeType

with This namespace contains constants describing ligand associated the the charge types OEProteinLigandOptOptions. SetLigandCharge method.

### **CURRENT**

Use the currently existing charges on the ligand. Corresponding string value: current

## **AM1BCC**

Use the OEAM1BCCCharges charges. Corresponding string value: am1bcc

#### AM1BCCELF10

Use the OEAM1BCCELF10Charges charges. Corresponding string value: am1bccelf10

#### **MMFF**

Use the OEMMFF94Charges charges. Corresponding string value: mmff

# 4.2.3 OEOptimizationType

This namespace contains constants describing the force field type

### **Cartesian**

Optimization in atomic Cartesian coordinates

## **PoseCartesian**

Constrained, to preserve the pose, optimization in atomic Cartesian coordinates. Optimization is performed in multiple steps, with ddditional harmonic constraint potentials added to restrict the motion of the heavy atoms of the ligand in the preliminary steps of optimization, followed by regular atomic cartesian coordinates optimization.

# 4.2.4 OESzybkiReturnCode

This namespace contains constants describing the force field type

#### **Success**

Success.

### **ExcessiveOverlap**

Failed due to excessive overlap.

## **IncompleteOpt**

Optimization did not reach desired gradient tolerance, and finished due to exceeding maximum iterations.

## **FFNeedHessiens**

Requires a forcefield with second derivative implementation.

## **InvalidOptions**

Invalid Options.

## **ContainsImplicitH**

Contains Implicit Hydrogens.

## **ProteinFailedFF**

Failed due to inability to assign protein force field.

## **ProteinMissing3D**

Failed due to input protein not having 3D coordinates.

### ProteinMissingCharge

Failed due to input protein not having charges assigned.

#### **ProteinNotSet**

Failed due to input protein missing.

## **LigandFailedFF**

Failed due to inability to assign ligand force field.

### LigandMissing3D

Failed due to input ligand not having 3D coordinates.

## LigandMissingCharge

Failed due to input ligand not having charges assigned.

## **LigandFailedCharge**

Failed due to inability to assign ligand charges.

# **Failed**

Failed.

# **EXAMPLES: WORKING WITH SZYBKI TK**

The basic Szybki TK API is provided to the users in the OESzybki, OESzybkiOptions, OESzybkiResults and OESzybkiEnsembleResults classes. In addition, when the purpose is to calculate compound properties, such as solvation free energy or free energy of selecting specific conformations out of the ensemble, the higher level API are defined in the free functions, OEEstimateSolvFreeEnergy and OEEstimateConfFreeEnergies.

# 5.1 Ligand Energetics and Optimization

# 5.1.1 Single ligand in vacuum

The following example illustrates how to optimize a single ligand in vacuum. As one can see assuming a molecule is successfully read, only two objects are needed to perform the optimization: OESzybki and OESzybkiResults. The latter is passed as the second parameter to the parenthesis operator  $OESzybki. operator ( )$ . Molecule with the optimized coordinates is returned as a first parameter. Optimization is done using the default MMFF94. Final energy results are available as SD tags in the returned molecule and optionally with a call of a method OESzybkiResults. Print.

## **Listing 1: Simple Ligand in a Vacuum**

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
from openeye import oeszybki
```

```
def main(args=[_name_]):
    if len(args) != 3:
        oechem.OEThrow.Usage("%s <molfile> <outfile>" % args[0])
    if s = oechem. oemolistream()if not ifs.open(arg[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   ofs = occhem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   opts = oeszybki.OESzybkiOptions()
    sz = oeszybki.OESzybki (opts)
    results = oeszybki.OESzybkiResults()if not sz (mol, results) :
        return 1
   oechem.OEWriteMolecule(ofs, mol)
    results. Print (oechem. oeout)
    return <sub>0</sub>if _name_ = "main":
    sys.exit(main(sys.argv))
```

# 5.1.2 Single ligand in vacuum using SMIRNOFF

The following example illustrates how to optimize a single ligand in vacuum using SMIRNOFF (see SMIRNOFF). Only two objects are needed to perform the optimization: OESzybki and OESzybkiResults. The latter is passed as the second parameter to the parenthesis operator  $OESzybki$ .  $operator()$ . Partial charges have to be preassigned to the input molecule. Molecule with the optimized coordinates is returned as a first parameter. Final energy results are available as SD tags in the returned molecule and optionally with a call of a method OESzybkiResults. Print.

#### **Listing 2: Simple Ligand in a Vacuum Using SMIRNOFF**

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
```

```
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeszybki
def main(args=[_name_]):
    if len(args) != 3:
        oechem.OEThrow.Usage("%s <molfile> <outfile>" % args[0])
    ifs = oechem.oemolistream()
    if not ifs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
    ofs = occhem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
    mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
    opts = oeszybki.OESzybkiOptions()
    opts.GetGeneralOptions().SetForceFieldType(oeszybki.OEForceFieldType_
\rightarrow SMIRNOFF99FROSST)
    sz = oeszybki.OESzybki (opts)
    results = oeszybki.OESzybkiResults()
    if not sz (mol, results) :
        return 1
   oechem.OEWriteMolecule(ofs, mol)
   results. Print (oechem. oeout)
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# 5.1.3 Optimization of a set of ligands

The next example illustrates the usage of Szybki TK to optimize a set of compounds with the MMFF94 force field in vacuum or in solution using Sheffield solvation model. Optionally attractive VdW can be removed. The optimization is done by default in full Cartesian coordinates, however torsion space optimization or single point calculation could be done too. A group of atoms which belong to specified SMARTS pattern might be excluded from optimization so their positions will be fixed at their initial coordinates. Note that the OESzybki object is made with a constructor which takes the instance of the OESzybkiOptions class.

#### Listing 3: Optimization of a Set of Ligands

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
from openeye import oeszybki
def main(argv=[_name_]):
    itf = oechem. 0EInterface()if not SetupInterface(argv, itf):
        return 1
    if s = oechem. oemolistream()if not ifs.open(itf.GetString("-in")):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % itf. GetString ("-in"))
   ofs = occhem.oemolostream()if not ofs.open(itf.GetString("-out")):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-out"))
   logfile = oechem.oeoutif itf.HasString("-log"):
        if not logfile.open(itf.GetString("-log")):
            oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-log
\leftrightarrow"))
    # Szybki options
    opts = oeszybki.OESzybkiOptions()
```

```
(continued from previous page)
```

```
# select run type
    if itf. GetBool ("-t"):
        opts.SetRunType(oeszybki.OERunType_TorsionsOpt)
    if itf. GetBool ("-n"):
        opts.SetRunType(oeszybki.OERunType_SinglePoint)
    # apply solvent model
    if itf. GetBool ("-s"):
        opts.GetSolventOptions().SetSolventModel(oeszybki.OESolventModel_Sheffield)
    # remove attractive VdW forces
    if itf.fGetBool("-a"):
        opts.GetGeneralOptions().SetRemoveAttractiveVdWForces(True)
    # Szybki object
    sz = oeszybki.OESzybki (opts)
    # fix atoms
    if itf.HasString("-f"):
        if not sz.FixAtoms (iff.GetString("-f")):
            oechem. OEThrow. Warning ("Failed to fix atoms for \frac{2}{5}s" % itf. GetString ("-f"))
    # process molecules
    mol = occhem. OEMol()while oechem. OEReadMolecule(ifs, mol):
        logfile.write("\nMolecule %s\n" % mol.GetTitle())
        no\_res = Truefor results in sz(mol):
            results. Print (logfile)
            no\_res = False
        if no_res:
            oechem. OEThrow. Warning ("No results processing molecule: %s" % mol.
\rightarrowGetTitle())
            continue
        else:
            oechem.OEWriteMolecule(ofs, mol)
    return 0
InterfaceData = ""!PARAMETER -in
  !TYPE string
  !REQUIRED true
  !BRIEF Input molecule file name.
!END
!PARAMETER -out
 !TYPE string
 !REOUIRED true
 !BRIEF Output molecule file name.
!\,\mathsf{END}\,!PARAMETER -log
  !TYPE string
  !REQUIRED false
```

!BRIEF Log file name. Defaults to standard out.

(continued from previous page)

```
! END
!PARAMETER -s
  !TYPE bool
  !DEFAULT false
  !REQUIRED false
  !BRIEF Optimization in solution.
! END
!PARAMETER -t
 !TYPE bool
  !DEFAULT false
 !REQUIRED false
 !BRIEF Optimization of torsions.
!END
!PARAMETER -n
  !TYPE bool
  !DEFAULT false
  !REQUIRED false
  !BRIEF Single point calculation.
! END
!PARAMETER -a
 !TYPE bool
 !DEFAULT false
 !REQUIRED false
 !BRIEF No attractive VdW forces.
! END
!PARAMETER -f
  !TYPE string
  !REQUIRED false
  !BRIEF SMARTS pattern of fixed atoms.
! END
\mathbf{u} as \mathbf{u}def SetupInterface(argv, itf):
    oechem.OEConfigure(itf, InterfaceData)
    if oechem. OECheckHelp(itf, argv):
        return False
    if not oechem. OEParseCommandLine(itf, argv):
        return False
    if not oechem. OEIsReadable (oechem. OEGetFileType (
                   oechem.OEGetFileExtension(itf.GetString("-in")))) :
        oechem. OEThrow. Warning ("%s is not a readable input file" % itf. GetString ("-in
\leftrightarrow<sup>"</sup>))
        return False
    if not oechem. OEIsWriteable (oechem. OEGetFileType (
                  oechem.OEGetFileExtension(itf.GetString("-out")))):
        oechem. OEThrow. Warning ("%s is not a writable output file" % itf. GetString ("-
\leftarrowout"))
        return False
    return True
```

```
if name == "_main_":
   sys.exit(main(sys.argv))
```

## 5.1.4 Optimization of a single ligand with the Newton-Raphson method

The next example in this section shows how to use Newton-Raphson optimization method, rather than the default BFGS:

Listing 4: Optimization of a Single Ligand with the Newton-Raphson Method

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
from openeye import oeszybki
def main (args) :
    if len(args) != 3:
        oechem. OEThrow. Usage ("%s input_molecule output_molecule" % args[0])
   if s = oechem. oemolistream()if not ifs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   ofs = oechem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   opts = oeszybki.OESzybkiOptions()
   opts.GetOptOptions().SetOptimizerType(oeszybki.OEOptType_NEWTON)
    opts.GetSolventOptions().SetSolventModel(oeszybki.OESolventModel_Sheffield)
```

```
sz = oeszybki.OESzybki (opts)
   res = oeszybki.OESzybkiResults()
    if (sz (mol, res)):
        oechem.OEWriteMolecule(ofs, mol)
        res. Print (oechem. oeout)
    return 0
if _name == " main ":
    sys.exit(main(sys.argv))
```

# 5.1.5 Optimization of all conformers of a ligand

Finally, the last example in this section shows how to use Newton-Raphson optimization method on all conformers of a ligand. The current charges of the ligand are used and will not be changed during the optimization.

#### Listing 5: Optimization of All Conformers of a Ligand

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
from openeye import oeszybki
def main (args) :
   if len(args) != 3:
        oechem. OEThrow. Usage ("%s input_molecule output_molecule" % args [0])
    ifs = oechem.oemolistream()
   if not ifs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open % for reading" % args[1])
```

```
ofs = occhem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   opts = oeszybki.OESzybkiOptions()
   opts.GetOptOptions().SetOptimizerType(oeszybki.OEOptType_NEWTON)
   opts.GetGeneralOptions().SetForceFieldType(oeszybki.OEForceFieldType_MMFF94S)
   opts.GetSolventOptions().SetSolventModel(oeszybki.OESolventModel_Sheffield)
   opts.GetSolventOptions().SetChargeEngine(oequacpac.OEChargeEngineNoOp())
   sz = oeszybki.OESzybki (opts)
   res = oeszybki.OESzybkiResults()
    for mol in ifs. GetOEMols():
        for conf in mol. GetConfs():
            if sz (conf, res):
                oechem.OESetSDData(conf, oechem.OESDDataPair('Total energy', "%0.4f"
                                                              % res.GetTotalEnergy()))
        oechem.OEWriteMolecule(ofs, mol)
    ifs.close()
   ofs.close()
   return 0if name == " main ":
   sys.exit(main(sys.argv))
```

# 5.1.6 Optimization of a single bound ligand

The simplest case is illustrated below. Notice the usage of the method  $OESzybki$ . Set Protein which tells Szybki that the ligand is placed inside the protein. Since no protein-ligand electrostatics have been specified, neither the coordinates types which should be used by the optimizer, the code below performs the optimization for a rigid ligand using 6 translational-rotational coordinates in the MMFF94 VdW potential field.

#### **Listing 5: Optimization of a Single Bound Ligand**

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
```

```
# or its use.
import sys
from openeye import oechem
from openeye import oeszybki
def main(argv=[_name_]):
    if len(argv) != 4:
        oechem.OEThrow.Usage("%s <molfile> <protein> <outfile>" % argv[0])
    lfs = oechem.oemolistream()if not lfs.open(argv[1]):oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   pfs = oechem.oemolistream()if not pfs.open(argv[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[2])
    ofs = occhem.oemolostream()if not ofs.open(argv[3]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % argv[3])
    mol = occhem.OEGraphMol()oechem.OEReadMolecule(lfs, mol)
    protein = oechem. OEGraphMol()
    oechem. OEReadMolecule (pfs, protein)
    opts = oeszybki.OESzybkiOptions()
    sz = oeszybki.OESzybki (opts)
    sz.SetProtein(protein)
    res = oeszybki.OESzybkiResults()
    if not sz (mol, res) :
        return 1
    oechem.OEWriteMolecule(ofs, mol)
    res.Print (oechem.oeout)
    return 0
if __name__ == "__main__".sys.exit(main(sys.argv))
```

# 5.2 Protein-Ligand Energetics and Optimization

Examples in this section show how to optimize a bound ligand.

# 5.2.1 Optimization of a set of bound ligands in a rigid receptor

The next example illustrates the usage of Szybki TK to optimize a set of ligands with MMFF94 force field inside a protein receptor. By default only VdW protein-ligand interaction is used. Optionally exact or grid Coulomb potential as well as PB solvent screening potentials could be added. When grid potential is selected (either Coulomb or PB) optionally it could be saved or read in when the corresponding grid file is present in the specified directory. Notice that when the exact Coulomb electrostatics is chosen, also the exact VdW potential is chosen (method OESzybkiProteinOptions. SetExactVdWProteinLiqand) which allows for tight gradients convergence (methods OESzybkiOptOptions. SetMaxIter and OESzybkiOptOptions. SetGradTolerance). By default ligand is treated as a solid body, that is only its translational and rotational degrees of freedom are optimized. Optionally also torsional degrees could be optimized. In this example protein receptor is rigid. Molecular input file should contain initial 3D coordinates of molecules in any format supported by OEChem TK. Output file is specified with the -out flag. In addition a log file containing energy data terms values is written to stdout or a file specified by  $-log.$ 

## Listing 6: Optimization of a Set of Bound Ligands in a Rigid Receptor

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
from openeye import oeszybki
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (Interface, argv)
    lfs = oechem.oemolistream()if not lfs.open(itf.GetString("-in")):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % itf. GetString ("-in"))
    pfs = oechem.oemolistream()
```

```
if not pfs.open(itf.GetString("-p")):oechem. OEThrow. Fatal ("Unable to open %s for reading", itf. GetString ("-p"))
   ofs = oechem.oemolostream()
   if not ofs.open(itf.GetString("-out")):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-out"))
   logfile = oechem.oeoutif itf.HasString("-log"):
       if not logfile.open(itf.GetString("-log")):
            oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-log
\leftrightarrow"))
   # Szybki options
   opts = oeszybki.OESzybkiOptions()
   # select optimization type
   if(itf.GetBool("t"):
       opts.SetRunType(oeszybki.OERunType_TorsionsOpt)
   else:
       opts.SetRunType(oeszybki.OERunType_CartesiansOpt)
   # select protein-electrostatic model
   emodel = itf.GetString("-e")elecModel = oeszybki.OEProteinElectrostatics_NoElectrostatics
   if emodel == "VdW":
       elecModel = oeszybki.OEProteinElectrostatics_NoElectrostatics
   elif emodel == "PB":
       elecModel = oeszybki.OEProteinElectrostatics_GridPB
   elif emodel == "Coulomb":
       elecModel = oeszybki.OEProteinElectrostatics_GridCoulomb
   clif emodel == "ExactCoulomb":
       elecModel = oeszybki.OEProteinElectrostatics_ExactCoulomb
       opts.GetProteinOptions().SetExactVdWProteinLigand(True)
       opts.GetOptOptions().SetMaxIter(1000)
       opts.GetOptOptions().SetGradTolerance(1e-6)
   opts.GetProteinOptions().SetProteinElectrostaticModel(elecModel)
   # Szybki object
   sz = oeszybki.OESzybki(opts)# read and setup protein
   protein = oechem. OEGraphMol()
   oechem. OEReadMolecule (pfs, protein)
   sz.SetProtein(protein)
   # save or load grid potential
   \textbf{if}(\text{emodel} == \texttt{"PB" or emodel} == \texttt{"Coulomb"}):if(itf.HasString("-s")):
            sz.SavePotentialGrid(itf.GetString("-s"))
       if (if. HasString(" -1");sz. LoadPotentialGrid(itf. GetString("-l"))
   # process molecules
   for mol in lfs. GetOEMols():
       logfile.write("\nMolecule %s\n" % mol.GetTitle())
       no\_res = True
```

```
for res in sz (mol) :
            res.Print(logfile)
            no\_res = Falseif no_res:
            oechem. OEThrow. Warning ("No results processing molecule: s s" % mol.
\rightarrowGetTitle())
            continue
        else:
            oechem.OEWriteMolecule(ofs, mol)
    return 0
Interface = ""!PARAMETER -in
  !TYPE string
  !REQUIRED true
  !BRIEF Input molecule file name.
! END
!PARAMETER -p
 !TYPE string
 !REQUIRED true
 !BRIEF Input protein file name.
! END
!PARAMETER -out
 !TYPE string
 !REQUIRED true
  !BRIEF Output molecule file name.
!END
!PARAMETER -log
  !TYPE string
  !REQUIRED false
  !BRIEF Log file name. Defaults to standard out.
! END
!PARAMETER -e
 !TYPE string
 !DEFAULT VdW
 !LEGAL_VALUE VdW
 !LEGAL_VALUE PB
  !LEGAL_VALUE Coulomb
  !LEGAL_VALUE ExactCoulomb
  !BRIEF Protein ligand electrostatic model.
!END
!PARAMETER -t
 !TYPE bool
 !DEFAULT false
 !REQUIRED false
 !BRIEF Torsions added to the optimized variables.
!END
!PARAMETER -1
```

```
! TYPE string
  !REQUIRED false
  !BRIEF File name of the potential grid to be read.
! END
!PARAMETER -s
  !TYPE string
  !REQUIRED false
  !BRIEF File name of the potential grid to be saved.
! END
\mathbf{u} and \mathbf{u}if name == " main ":
    sys.exit(main(sys.argy))
```

# 5.2.2 Optimization of a set of bound ligands in a partially flexible receptor

The next example is very similar with respect to the previous one, but the side chains of the protein which are within the specified range from the ligand, are made flexible during optimization (methods  $OESzybkiProteinOptions$ . SetProteinFlexibilityType and OESzybkiProteinOptions. SetProteinFlexibilityRange). Optionally, partially optimized structure can be saved to a file.

#### Listing 7: Optimization of a Set of Bound Ligands in a Partially Flexible Receptor

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
from openeye import oeszybki
def main(argv=[ name ]):
   itf = oechem. OEInterface (Interface, argv)
   lfs = oechem.oemolistream()
```

```
(continued from previous page)
```

```
if not lfs.open(itf.GetString("-in")):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % itf. GetString ("-in"))
   pfs = oechem.oemolistream()
   if not pfs.open(itf.GetString("-p")):
       oechem. OEThrow. Fatal ("Unable to open %s for reading", itf. GetString ("-p"))
   olfs = oechem.oemolostream()if not olfs.open(itf.GetString("-out")):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-out"))
   opfs = oechem.oemolostream()if itf.HasString("-s"):
       if not opfs.open(itf.GetString("-s")):
            oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-s
\leftrightarrow"))
   logfile = oechem.oeoutif itf.HasString("-loq"):
       if not logfile.open(itf.GetString("-log")):
            oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-log
\leftrightarrow"))
   # Szybki options
   opts = oeszybki.OESzybkiOptions()
   # select optimization type
   opt = \text{itf.getString("-opt")}if opt == "Cartesian":opts.SetRunType(oeszybki.OERunType_CartesiansOpt)
   if opt == "Torsion":opts.SetRunType(oeszybki.OERunType_TorsionsOpt)
   if opt == "SolidBody":opts.SetRunType(oeszybki.OERunType_SolidBodyOpt)
   # select protein-electrostatic model
   emodel = itf.GetString("-e")
   elecModel = oeszybki.OEProteinElectrostatics_NoElectrostatics
   if emodel == "VdW":
       elecModel = oeszybki.OEProteinElectrostatics_NoElectrostatics
   elif emodel == "PB":
       elecModel = oeszybki.OEProteinElectrostatics_GridPB
   elif emodel == "Coulomb":
       elecModel = oeszybki.OEProteinElectrostatics_GridCoulomb
   \text{elif} emodel == "ExactCoulomb":
       elecModel = oeszybki.OEProteinElectro statistics ExactCoulombopts.GetProteinOptions().SetProteinElectrostaticModel(elecModel)
   # use smooth potential and tight convergence
   if (emodel == "VdW" or emodel == "ExactCoulomb"):
       opts.GetProteinOptions().SetExactVdWProteinLigand(True)
       opts.GetOptOptions().SetMaxIter(1000)
       opts.GetOptOptions().SetGradTolerance(1e-6)
   # protein flexibility
   opts.GetProteinOptions().SetProteinFlexibilityType(oeszybki.OEProtFlex_SideChains)
   opts.GetProteinOptions().SetProteinFlexibilityRange(itf.GetDouble("-d"))
```

```
# Szybki object
    sz = oeszybki.OESzybki (opts)
    # read and setup protein
    protein = oechem. OEGraphMol()
    oprotein = oechem. OEGraphMol() # optimized protein
    oechem. OEReadMolecule (pfs, protein)
    sz.SetProtein(protein)
    # process molecules
    for mol in lfs. GetOEMols():
        logfile.write("\nMolecule %s\n" % mol.GetTitle())
        for res in sz(mol):
            res.Print(logfile)
        oechem.OEWriteMolecule(olfs, mol)
        if itf.HasString("-s"):
            sz.GetProtein(oprotein)
            oechem. OEWriteMolecule (opfs, oprotein)
    return 0
Interface = ""!BRIEF -in input_molecule -p protein -out output_molecule
!PARAMETER -in
  !TYPE string
 !REQUIRED true
 !BRIEF Input molecule file name.
!END
!PARAMETER -p
  !TYPE string
  !REQUIRED true
  !BRIEF Input protein file name.
!END
!PARAMETER -out
 !TYPE string
 !REOUIRED true
 !BRIEF Output molecule file name.
!END
!PARAMETER -log
  !TYPE string
  !REQUIRED false
  !BRIEF Log file name. Defaults to standard out.
! END
!PARAMETER -e
 !TYPE string
 !DEFAULT VdW
 !LEGAL VALUE VdW
 !LEGAL VALUE PB
  !LEGAL_VALUE Coulomb
  !LEGAL_VALUE ExactCoulomb
```

```
!BRIEF Protein ligand electrostatic model.
!END
!PARAMETER -opt
 !TYPE string
  !DEFAULT Cartesian
  !LEGAL_VALUE Cartesian
  !LEGAL VALUE Torsion
  !LEGAL VALUE SolidBody
  !BRIEF Optimization method
! END
!PARAMETER -d
 ITYPE double
 IDEFAULT 5 0
 !BRIEF Distance criteria from protein side-chains flexibility.
! END
!PARAMETER -s
  !TYPE string
  !REQUIRED false
 !BRIEF File name the partially optimized protein will be saved.
LEND
\mathbf{u} as \mathbf{u}if name == " main ":
    sys.exit(main(sys.argy))
```

# 5.2.3 Optimization of a bound ligand in a partially flexible receptor

The next example is very similar with respect to the previous one, but the list of residue numbers of the protein that are made flexible during optimization is specified by the  $-residues$  flag (see method  $OESzybkiProteinOptions$ . AddFlexibleResidue). Partially optimized ligand and protein structures are saved to files specified by the -outl and -outp flags, respectively.

#### Listing 8: Optimization of a Bound Ligand in a Partially Flexible Feceptor

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
from openeye import oeszybki
def main(argv=[_name_]):
   itf = oechem. OEInterface (Interface, argv)
    if s = oechem. oemolistream()if not ifs.open(itf.GetString("-in")):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % itf. GetString ("-in"))
   pfs = oechem.oemolistream()
    if not pfs.open(itf.GetString("-protein")):
        oechem. OEThrow. Fatal ("Unable to open %s for reading", itf. GetString ("-protein
\leftrightarrow"))
    ofs = occhem.oemolostream()if not ofs.open(itf.GetString("-outl")):
        oechem.OEThrow.Fatal("Unable to open %s for writing" % itf.GetString("-outl"))
   opfs = oechem.oemolostream()
    if not opfs.open(itf.GetString("-outp")):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % itf. GetString ("-outp"))
    ligand = oechem. OEGraphMol()
   oechem.OEReadMolecule(ifs, ligand)
    protein = oechem. OEGraphMol()
    oechem. OEReadMolecule(pfs, protein)
    # Szybki options
   opts = oeszybki.OESzybkiOptions()
   opts.SetRunType(oeszybki.OERunType_CartesiansOpt)
   opts.GetOptOptions().SetMaxIter(2000)
   opts.GetOptOptions().SetGradTolerance(1e-6)
   opts.GetGeneralOptions().SetForceFieldType(oeszybki.OEForceFieldType_MMFF94S)
    opts.GetProteinOptions().SetProteinFlexibilityType(oeszybki.OEProtFlex_
\rightarrowSideChainsList)
    opts.GetProteinOptions().SetProteinElectrostaticModel(
                              oeszybki.OEProteinElectrostatics_ExactCoulomb)
    res num = []for res in itf.GetStringList('-residues'):
        intres = Nonetry:
            intres = int(res)except ValueError:
            print ('Illegal residue value: {}'.format (res))
        if intres is None:
            continue
        res_num.append(intres)
```

```
for i in res_num:
        for atom in protein. GetAtoms () :
            residue = oechem. OEAtomGetResidue (atom)
            if (residue.GetResidueNumber() == i) :
                 opts.AddFlexibleResidue(residue)
                 break
    sz = oeszybki.OESzybki(opts)sz.SetProtein(protein)
    result = oeszybki.OESzybkiResults()sz(ligand, result)
    sz.GetProtein(protein)
    oechem. OEWriteMolecule (opfs, protein)
    oechem. OEWriteMolecule (ofs, ligand)
    return 0
Interface = ""!BRIEF -in ligand -protein protein -outl output_ligand -outp output_protein -residues
\leftrightarrowr1 r2 ... rn
!PARAMETER -in
  !TYPE string
 !REQUIRED true
 !BRIEF Input ligand file name.
! END
!PARAMETER -protein
 !TYPE string
 !REQUIRED true
  !BRIEF Input protein file name.
! END \,!PARAMETER -outl
  !TYPE string
  !REOUIRED true
 !BRIEF Output ligand file name.
! END
!PARAMETER -outp
 !TYPE string
 !REQUIRED true
 !BRIEF Output protein file name.
! END
!PARAMETER -residues
  !TYPE string
  !LIST true
  IREQUIRED true
 !BRIEF List of residues numbers to be optimized along with the ligand
!END
\mathbf{u} in \mathbf{u}if name == " main ":
    sys.exit(main(sys.argv))
```

# 5.2.4 Estimation of PB binding for a set of ligands

This example shows how to fast estimate binding for a set of ligands using PB electrostatics. Two OESzybki objects are instantiated: one for the optimization of bound ligands in VdW-Coulomb potential, and the second one which performs single-point PB calculations. Final results are attached as SD tags to the output molecules.

### Listing 9: Estimation of PB Binding for a Set of Ligands

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
from openeye import oeszybki
def main (args) :
    if len(aras) != 4:
        oechem. OEThrow. Usage ("%s ligand_file protein_file output_file (SDF or OEB)" %.
\leftrightarrow \arg s[0])
    lfs = oechem.oemolistream()if not lfs.open(args[1]):oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   pfs = oechem.oemolistream()
   if not pfs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open % for reading" % args [2])
    ofs = occhem.oemolostream()if not ofs.open(args[3]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [3])
    if not oechem. OEIsSDDataFormat (ofs. GetFormat ()):
        oechem. OEThrow. Fatal ("Output file does not support SD data used by this...
\rightarrowexample")
    # Szybki options for VdW-Coulomb calculations
    optsC = oeszybki.OESzybkiOptions()
    optsC.GetProteinOptions().SetProteinElectrostaticModel(
```

```
oeszybki.OEProteinElectrostatics_ExactCoulomb)
    optsC.SetRunType(oeszybki.OERunType_CartesiansOpt)
    # Szybki options for PB calculations
    optsPB = oeszybki.OESzybkiOptions()optsPB.GetProteinOptions().SetProteinElectrostaticModel(
                                oeszybki.OEProteinElectrostatics_SolventPBForces)
    optsPB.SetRunType(oeszybki.OERunType_SinglePoint)
    # Szybki objects
    szC = oeszybki.OESzybki (optsC)
    szPB = oeszybki.OESzybki (optsPB)
    # read and setup protein
   protein = occhem.OEGraphMol()oechem. OEReadMolecule (pfs, protein)
    szC.SetProtein(protein)
    szPB.SetProtein(protein)
    terms = set([oeszybki.OEPotentialTerms_ProteinLigandInteraction,
                 oeszybki.OEPotentialTerms_VdWProteinLigand,
                 oeszybki.OEPotentialTerms_CoulombProteinLigand,
                 oeszybki.OEPotentialTerms_ProteinDesolvation,
                 oeszybki.OEPotentialTerms_LigandDesolvation,
                 oeszybki.OEPotentialTerms_SolventScreening])
    # process molecules
    for mol in lfs. GetOEMols () :
        # optimize mol
        if not list(szC(mol)):
            oechem. OEThrow. Warning ("No results processing molecule: \frac{2}{3}S" % mol.
\rightarrowGetTitle())
            continue
        # do single point with better electrostatics
        for conf, results in zip(mol. GetConfs(), szPB(mol)):
            for i in terms:
                strEnergy = ("89.4f" % results.GetEnergyTerm(i))oechem. OEAddSDData (conf, oeszybki. OEGetEnergyTermName(i), strEnergy)
        oechem.OEWriteMolecule(ofs, mol)
    return <sub>0</sub>if name == " main ":
    sys.exit(main(sys.argv))
```

# 5.2.5 Optimization of a bound ligand using Newton-Raphson method

The last example in this section illustrates how to use SzybkiTK to optimize a ligand in partially flexible protein with Newton-Raphson optimization method.

### Listing 10: Optimization of a Bound Ligand Using Newton-Raphson Method

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
from openeye import oeszybki
def main (args) :
    if len(args) != 4:
        oechem. OEThrow. Usage ("%s protein input ligand output ligand" % args [0])
   pfs = oechem.oemolistream()
    if not pfs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args[1])
   lfs = oechem.oemolistream()if not lfs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [2])
   ofs = occhem.oemolostream()if not ofs.open(args[3]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [3])
   mol = occhem. OEGraphMol()protein = oechem. OEGraphMol()
   oechem.OEReadMolecule(lfs, mol)
   oechem. OEReadMolecule (pfs, protein)
   opts = oeszybki.OESzybkiOptions()
    opts.GetOptOptions().SetOptimizerType(oeszybki.OEOptType_NEWTON)
    opts.GetProteinOptions().SetProteinElectrostaticModel(
                             oeszybki.OEProteinElectrostatics_ExactCoulomb)
```

```
opts.GetProteinOptions().SetProteinFlexibilityType(oeszybki.OEProtFlex_Residues)
    opts.GetProteinOptions().SetProteinFlexibilityRange(2.0)
    sz = oeszybki.OESzybki (opts)
    sz.SetProtein(protein)
    res = oeszybki.OESzybkiResults()
    if (sz (mol, res)):
        oechem.OEWriteMolecule(ofs, mol)
        res. Print (oechem. oeout)
    return 0
if name == " main ":
    sys.exit(main(sys.argv))
```

# 5.3 DU Protein-Ligand Optimization with FF14SB-Parsley

Examples in this section show how to optimize a ligand in the protein active site using the OEFixedProteinLigandOptimizer and the OEFlexProteinLigandOptimizer classes. Both of these classes allow use of the FF14SB-Parsley forcefield, along with the MMFF and the MMFF-AMBER forcefields. These examples also demonstrate how to use design units as a source for the protein or the ligand. The first example optimizes an external ligand in a protein active site from a design unit, and the second example uses both the ligand and the protein from the same design unit.

## 5.3.1 Optimization of ligand in a rigid active site

This examples shows how to optimize a series of ligands in a rigid active site. The active site input is taken from a OEDesignUnit.

#### Listing 11: Optimization of Ligand in a Rigid Active Site

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
```

```
from openeye import oechem
from openeye import oeszybki
def main(argv=[__name__]):
    szOpts = oeszybki.OEProteinLigandOptOptions()
    opts = oechem.OERefInputAppOptions(szOpts, "OptimizeLiqandInDU", oechem.
\rightarrowOEFileStringType_Mol3D,
                                        oechem.OEFileStringType_Mol3D, oechem.
\rightarrowOEFileStringType_DU, "-du")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   szOpts.UpdateValues(opts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    rfs = oechem.oeifstream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   du = oechem.OEDesignUnit()
    if not oechem. OEReadDesignUnit (rfs, du) :
        oechem. OEThrow. Fatal ("Failed to read design unit")
    optimizer = oeszybki.OEFixedProteinLigandOptimizer(szOpts)
    optimizer.SetProtein(du, oechem.OEDesignUnitComponents_Protein)
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        conf = 0for res in optimizer. Optimize (mol) :
            conf += 1if res. GetReturnCode() == oeszybki.OESzybkiReLUnCode Success:oechem.OEThrow.Info("Conformer: %d" % conf)
                initEne = res.GetInitialEnergy()oechem. OEThrow. Info ("Initial energies:")
                oechem.OEThrow.Info(" Ligand: 80.2f'' % initEne.GetLigandEnergy())
                oechem.OEThrow.Info(" Intermolecular: %0.2f" % initEne.
\rightarrowGetInterEnergy())
                oechem.OEThrow.Info(" Total: \partial.2f" % initEne.GetTotalEnerqy())
                finalEne = res.GetFinalEnergies()oechem. OEThrow. Info ("Final energies:")
                oechem.OEThrow.Info(" Ligand: \frac{2}{3}0.2f" % finalEne.GetLigandEnergy())
                oechem.OEThrow.Info(" Intermolecular: %0.2f" % finalEne.
→GetInterEnergy())
                oechem.OEThrow.Info(" Total: \frac{2}{3}0.2f" % finalEne.GetTotalEnergy())
            else:
                oechem.OEThrow.Warning("Failed: %s" % oeszybki.OEGetSzybkiError(res.
\rightarrowGetReturnCode()))
        oechem.OEWriteMolecule(ofs, mol)
```

return 0

```
= = " main\mathbf{u}_\mathrm{d}if _name_
     sys.exit(main(sys.argv))
```

# 5.3.2 Optimization of ligand in a partially flexible active site

This examples shows how to optimize a ligand in a partially flexible active site. In this example, both the ligand and the active site is taken from a single OEDesignUnit.

#### Listing 12: Optimization of Ligand in a Rigid Active Site

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
from openeye import oeszybki
class MyOptions (oechem. OEOptions) :
   def __init__(self):oechem.OEOptions.__init__(self, "MyOption")
        self._optOpts = oeszybki.OEProteinLigandOptOptions()
        self._flexOpts = oeszybki.OEProteinFlexOptions()
        self.AddOption(self._optOpts)
        self.AddOption(self._flexOpts)
       pass
    def CreateCopy (self) :
        return self
   def GetOptOptions(self):
        return self._optOpts
    def GetFlexOptions(self):
```

return self. flexOpts

(continued from previous page)

```
def main(argv=[_name_]):
   myOpts = MyOptions()opts = oechem.OESimpleAppOptions(myOpts, "OptimizeDU", oechem.OEFileStringType_DU,
\rightarrow oechem. OEFileStringType_DU)
   if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   optOpts = myOpts.GetOptOptions()
   flexOpts = myOpts.GetFlexOptions()
   optOpts. UpdateValues (opts)
   flexOpts. UpdateValues (opts)
   if s = oechem.oeifstream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   ofs = occhem.oeofstream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
   optimizer = oeszybki. OEFlexProteinLigandOptimize r(opt0pts)du = oechem.OEDesignUnit()
   while oechem. OEReadDesignUnit(ifs, du):
        oechem.OEThrow.Info("Title: %s" % du.GetTitle())
        res = oeszybki.OEProteinLiqandOptResults()proteinMask = oechem. OEDesignUnitComponents Protein
        retCode = optimizer. Optimize (res, du, proteinMask, oechem.
→OEDesignUnitComponents_Ligand, flexOpts)
        if retCode == oeszybki.OESzybkiReturnCode_Success:
            initEne = res.GetInitialEnergy()oechem. OEThrow. Info ("Initial energies:")
            oechem. OEThrow. Info (" Ligand: 80.2f" % initEne. GetLigandEnergy())
            oechem. OEThrow. Info(" Flexible Protein: \frac{2}{r} % initEne. GetHostEnergy())
            oechem.OEThrow.Info(" Intermolecular: 80.2f'' % initEne.GetInterEnergy())
            oechem.OEThrow.Info(" Total: 80.2f" % initEne.GetTotalEnergy())
            finalEne = res.GetFinalEnergies()oechem.OEThrow.Info("Final energies:")
            oechem.OEThrow.Info(" Ligand: %0.2f" % finalEne.GetLigandEnergy())
            oechem.OEThrow.Info(" Flexible Protein: %0.2f" % finalEne.
\rightarrowGetHostEnergy())
            oechem.OEThrow.Info(" Intermolecular: \frac{2}{3}0.2f" \frac{2}{3} finalEne.GetInterEnergy())
            oechem.OEThrow.Info(" Total: %0.2f" % finalEne.GetTotalEnergy())
            oechem.OEWriteDesignUnit(ofs, du)
        else:
            oechem.OEThrow.Warning("%s: %s" % (du.GetTitle(), oeszybki.
\rightarrowOEGetSzybkiError(retCode)))
   return <sub>0</sub>if name == " main ":
   sys.exit(main(sys.argv))
```

# **5.4 Entropy estimation**

# 5.4.1 Estimation of solution ligand entropy

The following code illustrates how to estimate compound entropy in solution with Szybki TK.

## **Listing 13: Ligand Entropy**

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
from openeye import oeszybki
def main(argv=[\_name\_):
    szOpts = oeszybki.OELigandEntropyOptions()opts = oechem.OESimpleAppOptions(szOpts, "LigandEntropy", oechem.OEFileStringType_
-Mo13D)if oechem. OEConfigureOpts (opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   szOpts.UpdateValues(opts)
   ifs = occhem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        res = oeszybki.OEEntropyResults()
        ret_code = oeszybki.OELigandEntropy(res, mol, szOpts)
        if ret_code == oeszybki.OESzybkiReturnCode_Success:
            oechem. OEThrow. Info (" Configurational Entropy: \frac{2}{3}0.2f" \frac{8}{3} res.
\rightarrowGetConfigurationalEntropy())
            oechem. OEThrow. Info (" Solvation Entropy: 80.2f'' % res.
\rightarrowGetSolvationEntropy())
            oechem. OEThrow. Info (" Total Entropy: \frac{2}{3}0.2f" % res. GetTotalEntropy())
        else:
```

```
oechem.OEThrow.Warning("Failed: %s" % oeszybki.OEGetSzybkiError(ret_code))
   return 0
if name == "_main_":
   sys.exit(main(sys.argv))
```

# 5.4.2 Estimation of bound ligand entropy

The next example below shows how to calculate entropy of a bound ligand.

#### **Listing 15: Estimation of Bound Ligand Entropy**

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
from openeye import oeszybki
def main(argv=[_name_]):
    szOpts = oeszybki.OEBoundEntropyOptions()
    opts = oechem.OERefInputAppOptions(szOpts, "BoundEntropy", oechem.
\rightarrowOEFileStringType_Mol3D,
                                       oechem.OEFileStringType_DU, "-du")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
   szOpts. UpdateValues (opts)
   if s = oechem.oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   rfs = oechem.oeifstream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
```

```
du = oechem.OEDesignUnit()
    if not oechem. OEReadDesignUnit (rfs, du) :
        oechem. OEThrow. Fatal ("Failed to read design unit")
    for mol in ifs. GetOEMols():
        oechem.OEThrow.Info("Title: %s" % mol.GetTitle())
        res = oeszybki.OEEntropyResults()
        ret_code = oeszybki.OEBoundLigandEntropy(res, du, oechem.
→OEDesignUnitComponents_Protein, mol, szOpts)
        if ret_code == oeszybki.OESzybkiReturnCode_Success:
            oechem.OEThrow.Info(" Configurational Entropy: 80.2f" % res.
\rightarrowGetConfigurationalEntropy())
            oechem. OEThrow. Info (" Solvation Entropy: 80.2f'' % res.
\rightarrowGetSolvationEntropy())
            oechem. OEThrow. Info (" Total Entropy: \frac{2}{3} O. 2f" \frac{1}{3} res. GetTotalEntropy ())
        else:
            oechem. OEThrow. Warning ("Failed: %s" % oeszybki. OEGetSzybkiError (ret_code))
    return 0
if _name_ == "_main_":
    sys.exit(main(sys.argv))
```

# 5.5 Solvation free energy estimation

#### **Listing 16: Solvation Free Energy Estimation**

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
from openeye import oeszybki
def main (args) :
```

```
if len(args) != 3:
        oechem. OEThrow. Usage ("%s <input> <output>" % args [0])
    ifs = oechem.oemolistream()
    if not ifs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   ofs = occhem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   opts = oeszybki.OEFreeFormSolvOptions()
   opts.SetIonicState(oeszybki.OEFreeFormIonicState_Uncharged)
   res = oeszybki.OEFreeFormSolvResults()
    omol = oechem.OEGraphMol()
    if not oeszybki. OEEstimateSolvFreeEnergy (res, omol, mol, opts) :
        oechem. OEThrow. Error ("Failed to calculate solvation free energy for molecule
\rightarrow 8S<sup>"</sup> 8mol.GetTitle()solvenergy = res.GetSolvationFreeEnergy()
    oechem. OEThrow. Info ("Solvation free energy for compound %s is %6.2f kcal/mol" %
                         (mol.GetTitle(), solvenergy))
   oechem.OEWriteMolecule(ofs, omol)
    return 0
if _name_ == " _main
                        - n +
    sys.exit(main(sys.argv))
```

# 5.6 Conformations free energy estimation

Warning: This capability should not be used on 32-bit platforms because the memory requirements are too high.

# 5.6.1 Simple free energy estimation

The following code illustrates how to use the high level commands from OEFreeFormConf to estimate conformer free energies in solution with Szybki TK.

### **Listing 17: Simple Free Energy Estimation**

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
from openeye import oeszybki
def main (args) :
   if len(args) != 3:
        oechem.OEThrow.Usage("%s <input> <output>" % args[0])
   ifs = oechem.oemolistream()
   if not ifs.open(args[1]):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   ofs = occhem.oemolostream()if not ofs.open(args[2]):
       oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   opts = oeszybki.OEFreeFormConfOptions()
   ffconf = oeszybki.OEFreeFormConf(opts)omol = occhem. OEMol(mol)if not (ffconf.EstimateFreeEnergies(omol) == oeszybki.OEFreeFormReturnCode_
\rightarrowSuccess):
        oechem. OEThrow. Error ("Failed to estimate conformational free energies")
   res = oeszybki.OEFreeFormConfResults(omol)
   oechem. OEThrow. Info ("Number of unique conformations: %d" % res.
→GetNumUniqueConfs())
   oechem.OEThrow.Info("Conf. Delta_G Vibrational_Entropy")
    oechem.OEThrow.Info("
                              [kcal/mol][J/(mol K)]")
    for r in res. GetResultsForConformations():
        oechem.OEThrow.Info("%2d %10.2f %14.2f" % (r.GetConfIdx(), r.GetDeltaG(),
                                                    r.GetVibrationalEntropy()))
```

```
oechem.OEWriteMolecule(ofs, omol)
    return 0
if __name__ == "__main__sys.exit(main(sys.argv))
```

# 5.6.2 Simple restriction energy estimation

The following code illustrates how to use the high level commands from OEFreeFormConf to estimate restriction energies on conformers, along with conformer free energies in solution, with Szybki TK.

#### **Listing 18: Simple Restriction Energy Estimation**

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
from openeye import oeszybki
def main (args) :
   if len(args) != 3:
        oechem.OEThrow.Usage("%s <input> <output>" % args[0])
    ifs = oechem.oemolistream()
   if not ifs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   ofs = occhem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   mol = occhem. OEMol()
```

```
(continued from previous page)
```

```
oechem.OEReadMolecule(ifs, mol)
    opts = oeszybki.OEFreeFormConfOptions()
    ffconf = oeszybki.OEFreeFormConf(opts)
    omol = occhem. OEMol(mol)rmol = occhem. OEMol(mol)if not (ffconf.EstimateFreeEnergies(omol, rmol) == oeszybki.OEFreeFormReturnCode
\leftarrowSuccess):
        oechem. OEThrow. Error ("Failed to estimate conformational free energies")
    res = oeszybki.OEFreeFormConfResults(omol)
    oechem. OEThrow. Info ("Number of unique conformations: \partial d'' % res.
\rightarrowGetNumUniqueConfs())
    oechem. OEThrow. Info ("Conf. Delta G Vibrational Entropy")
    oechem.OEThrow.Info("
                                                 [J/(mol K)]")
                                [kcal/mol]for r in res. GetResultsForConformations():
        oechem.OEThrow.Info("%2d %10.2f %14.2f" % (r.GetConfIdx(), r.GetDeltaG(),
                                                      r.GetVibrationalEntropy()))
    rstrRes = oeszybki.OERestrictionEnergyResult(rmol)
    oechem.OEThrow.Info("Global strain: %d" % rstrRes.GetGlobalStrain())
    oechem. OEThrow. Info ("Local strain: \partial d" % rstrRes. GetLocalStrain())
    oechem.OEWriteMolecule(ofs, omol)
    return <sub>0</sub>= = " main " :
if _name_
    sys.exit(main(sys.argv))
```

# 5.6.3 Advanced free energy estimation

The following code illustrates how to use the low level commands from OEFreeFormConfAdvanced to estimate the conformer free energies in solution with Szybki TK. These low level methods of estimation gives an advantage over the high level methods of OEFreeFormConf in that these gives the user control over better managing certain expensive parts of the calculation.

#### **Listing 19: Advanced Free Energy Estimation**

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
```

```
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
import sys
from openeye import oechem
from openeye import oeszybki
def main (args) :
    if len(args) != 3:
        oechem.OEThrow.Usage("%s <input> <output>" % args[0])
    ifs = oechem.oemolistream()
    if not ifs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
   ofs = occhem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   opts = oeszybki.OEFreeFormConfOptions()
   ffconf = oeszybki.OEFreeFormConfAdvanced(opts)
    # Make a copy of our MCMol. We will execute the FreeFormConf commands on
    # the copied molecule so that our original molecule stays intact.
   omol = occhem. OEMol(mol)# Prepare a comprehensive ensemble of molecule conformers. This will
    # generate a comprehensive set of conformers, assign solvent charges on the,
\leftarrowmolecule
    # and check that the ensemble is otherwise ready for FreeFormConf calculations.
    if not (ffconf.PrepareEnsemble(omol) == oeszybki.OEFreeFormReturnCode_Success):
        oechem. OEThrow. Error ("Failed to prepare ensemble for FreeFormConf calculations
\leftrightarrow<sup>\pi</sup>)
    # Perform loose optimization of the ensemble conformers. We will remove
    # duplicates based on the loose optimization, to reduce the time needed for
    # tighter, more stricter optimization
    if not (ffconf.PreOptimizeEnsemble(omol) == oeszybki.OEFreeFormReturnCode
\rightarrowSuccess):
        oechem. OEThrow. Error ("Pre-optimization of the ensembles failed")
    # Remove duplicates from the pre-optimized ensemble
    if not (ffconf.RemoveDuplicates(omol) == oeszybki.OEFreeFormReturnCode_Success):
        oechem. OEThrow. Error ("Duplicate removal from the ensembles failed")
    # Perform the desired optimization. This uses a stricter convergence
    # criteria in the default settings.
    if not (ffconf.Optimize(omol) == oeszybki.OEFreeFormReturnCode_Success):
        oechem. OEThrow. Error ("Optimization of the ensembles failed")
```

```
# Remove duplicates to obtain the set of minimum energy conformers
    if not (ffconf.RemoveDuplicates(omol) == oeszybki.OEFreeFormReturnCode_Success):
        oechem. OEThrow. Error ("Duplicate removal from the ensembles failed")
    # Perform FreeFormConf free energy calculations. When all the above steps
    # have already been performed on the ensemble, this energy calculation
    # step is fast.
   if not (ffconf.EstimateEnergies(omol) == oeszybki.OEFreeFormReturnCode_Success):
        oechem. OEThrow. Error ("Estimation of FreeFormConf energies failed")
    # Gather results of calculation into a results object for ease of viewing, etc.
   res = oeszybki.OEFreeFormConfResults(omol)
   oechem. OEThrow. Info ("Number of unique conformations: %d" % res.
\rightarrowGetNumUniqueConfs())
   oechem. OEThrow. Info ("Conf. Delta G Vibrational Entropy")
   oechem.OEThrow.Info("
                               [kcal/mol][J/(mol K)]")
    for r in res. GetResultsForConformations():
        oechem.OEThrow.Info("%2d %10.2f %14.2f" % (r.GetConfIdx(), r.GetDeltaG(),
                                                   r.GetVibrationalEntropy()))
   oechem.OEWriteMolecule(ofs, omol)
    return 0
if name
          = " main ":
    sys.exit(main(sys.argy))
```

## 5.6.4 Advanced restriction energy estimation

The following code illustrates how to use the low level commands from OEFreeFormConfAdvanced to estimate the restriction energies of conformers, along with conformer free energies in solution, with Szybki TK. These low level methods of estimation gives an advantage over the high level methods of OEFreeFormConf in that these gives the user control over better managing certain expensive parts of the calculation.

#### **Listing 20: Advanced Restriction Energy Estimation**

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
from openeye import oeszybki
def main (args) :
   if len(args) != 3:
        oechem.OEThrow.Usage("%s <input> <output>" % args[0])
   ifs = occhem.oemolistream()if not ifs.open(arg[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args[1])
   ofs = oechem oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
   mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   opts = oeszybki.OEFreeFormConfOptions()
   ffconf = oeszybki.OEFreeFormConfAdvanced(opts)
    # Make a copy of our MCMol. We will execute the FreeFormConf commands on
    # the copied molecule so that our original molecule stays intact.
   omol = occhem. OEMol(mol)# Make further copies of our original molecule. The copied molecule (s) would be,
\leftrightarrowused
    # as source on which retriction energies would be calculated
   rmol = occhem. OEMol(mol)fmol = occhem.OEMol(mol)# Prepare a comprehensive ensemble of molecule conformers. For calculation
    # of restriction energies we want to make sure that all the corresponding free
    # conformers are also part of the comprehensive ensemble. This will also
    # assign solvent charges on the molecule and check that the ensemble is
    # otherwise ready for FreeFormConf calculations. The resulting `fmol'
    # contains the correspondig free conformers.
   if not (ffconf.PrepareEnsemble(omol, rmol, fmol) == oeszybki.OEFreeFormReturnCode_
\rightarrowSuccess):
        oechem. OEThrow. Error ("Failed to prepare ensemble for FreeFormConf calculations
\leftrightarrow")
    # Perform loose optimization of the ensemble conformers. We will remove
    # duplicates based on the loose optimization, to reduce the time needed for
    # tighter, more stricter optimization
   if not (ffconf.PreOptimizeEnsemble(omol) == oeszybki.OEFreeFormReturnCode_
\rightarrowSuccess):
        oechem. OEThrow. Error ("Pre-optimization of the ensembles failed")
    # Remove duplicates from the pre-optimized ensemble
    if not (ffconf.RemoveDuplicates(omol) == oeszybki.OEFreeFormReturnCode_Success):
```

```
(continues on next page)
```

```
oechem. OEThrow. Error ("Duplicate removal from the ensembles failed")
   # Perform the desired optimization. This uses a stricter convergence
    # criteria in the default settings.
   if not (ffconf.Optimize (omol) == oeszybki. OEFreeFormReturnCode_Success):
       oechem. OEThrow. Error ("Optimization of the ensembles failed")
   # Remove duplicates to obtain the set of minimum energy conformers
   if not (ffconf.RemoveDuplicates(omol) == oeszybki.OEFreeFormReturnCode_Success):
       oechem. OEThrow. Error ("Duplicate removal from the ensembles failed")
   # Perform FreeFormConf free energy calculations. When all the above steps
   # have already been performed on the ensemble, this energy calculation
   # step is fast.
   if not (ffconf.EstimateEnergies(omol) == oeszybki.OEFreeFormReturnCode Success):
       oechem. OEThrow. Error ("Estimation of FreeFormConf energies failed")
   # Gather results of calculation into a results object for ease of viewing, etc.
   res = oeszybki.OEFreeFormConfResults(omol)
   oechem. OEThrow. Info ("Number of unique conformations: %d" % res.
\rightarrowGetNumUniqueConfs())
   oechem. OEThrow. Info("Conf. Delta_G Vibrational_Entropy")
   oechem.OEThrow.Info("
                              [kcal/mol][J/(mol K)]")
   for r in res. GetResultsForConformations():
       oechem.OEThrow.Info("%2d %10.2f %14.2f" % (r.GetConfIdx(), r.GetDeltaG(),
                                                   r. GetVibrationalEntropy()))
   # Identify the corresponding conformer(s) to the free minimized conformer(s).
   # If identified, the corresponding (Conf)Free energy information is also
   # copied to the free conformers
   if not (ffconf.IdentifyConformer(fmol, omol) == oeszybki.OEFreeFormReturnCode_
\rightarrowSuccess):
       oechem. OEThrow. Error ("Identification of free conformer(s) failed")
   # Estimate restriction energies. Since both restricted and free conformer
    # energy components are already available, this operation is fast.
   if not (ffconf.EstimateRestrictionEnergy(fmol, rmol) == oeszybki.
\rightarrowOEFreeFormReturnCode_Success):
       oechem. OEThrow. Error ("Restriction energy estimation failed")
   # Gather restriction energies into a results object for ease of viewing, etc.
   rstrRes = oeszybki.OERestrictionEnergyResult(fmol)
   oechem. OEThrow. Info ("Global strain: %f" % rstrRes. GetGlobalStrain())
   oechem. OEThrow. Info ("Local strain: f'' * rstrRes. GetLocalStrain())
   # Optionally it is desired to perform a restrained optimization of the
   # restricted conformer(s) to brush out any energy differences due to
   # force field constaints or the sources of coonformer coordinates. Note: The
   # high level EstimateFreeEnergy method does not perform this opertion.
   if not (ffconf.OptimizeRestraint(rmol) == oeszybki.OEFreeFormReturnCode_Success):
       oechem. OEThrow. Error ("Restraint optimization of the conformer(s) failed")
   # Estimate restriction energies on this optimized conformers.
   # Since both restricted and free conformer energy components
   # are already available, this operation is fast.
   if not (ffconf.EstimateRestrictionEnergy(fmol, rmol) == oeszybki.
→OEFreeFormReturnCode_Success):
```

```
oechem. OEThrow. Error ("Restriction energy estimation failed")
    # Gather restriction energies into a results object for ease of viewing, etc.
    rstrRes = oeszybki.OERestrictionEnergyResult(fmol)
    oechem. OEThrow. Info ("Global strain: %f" % rstrRes. GetGlobalStrain())
    oechem. OEThrow. Info("Local strain: f'' % rstrRes. GetLocalStrain())
    oechem.OEWriteMolecule(ofs, omol)
    return 0if name == " main ":
    sys.exit(main(sys.argv))
```

## 5.6.5 Finding similar conformers

The following code illustrates how to find similar conformers to the ones at hand, from a pool of minimum energy conformers.

#### **Listing 21: Finding Similar Conformers**

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
from openeye import oeszybki
def main (args) :
   if len(args) != 3:
        oechem.OEThrow.Usage("%s <input> <output>" % args[0])
   ifs = oechem.oemolistream()
    if not ifs.open(args[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % args [1])
```

```
(continued from previous page)
```

```
ofs = occhem.oemolostream()if not ofs.open(args[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % args [2])
    mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   opts = oeszybki.OEFreeFormConfOptions()
   ffconf = oeszybki.OEFreeFormConf(opts)
    # Estimate free energies to ontain the minimum energy conformers
   omol = occhem. OEMol(mol)if not (ffconf.EstimateFreeEnergies(omol) == oeszybki.OEFreeFormReturnCode
\triangleSuccess) \cdotoechem. OEThrow. Error ("Failed to estimate conformational free energies")
    # Find similar conformers to the ones we started with, from the
    # pool of minimum energy conformers
    fmol = occhem. OEMol(mol)for conf in mol. GetConfs():
        ffconf.FindSimilarConfs(fmol, omol, conf, oechem.OESimilarByRMSD(0.05))
   oechem.OEWriteMolecule(ofs, fmol)
    return <sub>0</sub>if name == " main ":
    sys.exit(main(sys.argv))
```

# 5.6.6 Torsion scan

The following code shows how to scan all torsions in the input molecule

#### Listing 22: Perform torsion scan for all torsions in the input molecule

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
```

```
# or its use.
import sys
from openeye import oechem
from openeye import oeszybki
#######################################
# USED TO GENERATE CODE SNIPPETS FOR THE SZYBKI DOCUMENTATION
######################################
def main (argv=sys.argv) :
   if len(argv) != 2:
       oechem.OEThrow.Usage("%s <infile>" % argv[0])
   if s = oechem. oemolistream()if not ifs.open(argv[1]):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   mol = occhem. OEMol()oechem.OEReadMolecule(ifs, mol)
   outmol = occhem. OEMol()opts = oeszybki.OETorsionScanOptions()
   opts.SetDelta(30.0)
   opts.SetForceFieldType(oeszybki.OEForceFieldType_MMFF94)
   opts.SetSolvationType(oeszybki.OESolventModel_NoSolv)
   for tor in oechem. OEGetTorsions (mol) :
       print ("Torsion: %d %d %d %d" %
             (tor.a.GetIdx(), tor.b.GetIdx(), tor.c.GetIdx(), tor.d.GetIdx()))
       for res in oeszybki. OETorsionScan (outmol, mol, tor, opts):
           print ("%.2f %.2f" % (res. GetAngle(), res. GetEnergy()))
if _name_ == "_main_":
   sys.exit(main(sys.argv))
```

# **SIX**

# **RELEASE HISTORY**

# 6.1 Szybki TK 2.8.0

# 6.1.1 New features

• The constant SAGE\_OPENFF refers to the latest version of the Sage OpenFF force field.

# 6.2 Szybki TK 2.7.1

• OEFixedProteinLigandOptimizer and OEFlexProteinLigandOptimizer now propagate error better when optimization fails.

# 6.3 Szybki TK 2.7.0

# 6.3.1 New features

- The ability has been added to perform optimization in internal coordinates, with fixed torsions, during a torsion scan. Accordingly, the following additional commands have been added to OETorsionScanOptions:
  - $-$  SetUseInternalCoord
  - GetUseInternalCoord
  - SetTolerance
  - $-$  GetTolerance
  - $-$  SetMaxIter
  - $-$  GetMaxIter
- The ability to apply a nonbonded interactions cutoff in OEProteinLigandOptOptions has been added. The following two methods are also available in the class:
  - SetNonBondCutoff
  - GetNonBondCutoff
- Both OEFixedProteinLigandOptimizer and OEFlexProteinLigandOptimizer now apply a nonbonded interactions cutoff of 40.0 by default.
- A new class, *OETorsionScanner*, has been added to provide greater flexibility over the existing function *OETor*sionScan in extracting intermediate results from the scanning.

# 6.3.2 Major bug fixes

• An issue where the overloaded method SetTorsionConstraint would occasionally fail has been fixed.

# 6.3.3 Minor bug fixes

• Validation of user-selected torsion in torsion scan has been added. If a torsion passed to function OETorsionScan or method *Scan* does not exist, the torsion scan code stops with a message that the torsion does not exist in the input molecule.

# 6.4 Szybki TK 2.6.0.1

• New constant SAGE\_OPENFF210 has been introduced that refers to the Sage 2.1.0 force field. The constant SAGE\_OPENFF now refers to this latest version of Sage force field.

# 6.5 Szybki TK 2.6.0.0

## 6.5.1 New features

- Three classes have been added to facilitate using ff14SB/OpenFF potential for bound ligands and to bypass using OESzybki:
  - OEBoundEntropyOptions
  - OELigandEntropyOptions
  - OEEntropyResults
- A new function, *OEBoundLigandEntropy*, has been added to calculate the entropy of a bound ligand.
- A new function, *OELigandEntropy*, has been added to calculate the entropy of a free ligand.
- A new pair of options has been added to the *OETorsionScanOptions* to address hysteresis in torsion scanning. These provide the ability to increase the number of starts (SetNumStarts) and address the overlaps between scans (SetOverlapDiv) to avoid doing full 360-degree scans for many starts unless desired.

# 6.5.2 Major bug fixes

- An issue with the torsion scan (OETorsionScan) in solution with PB solvation has been fixed. It no longer incorrectly uses the MMFF94S potential even when scanning is done with the OpenFF force field.
- An issue with hysteresis that in certain cases caused asymmetric torsion scans has been addressed by resetting to the starting angle before starting reverse scans.

# 6.5.3 Minor bug fixes

- Better diagnostics have been added to OEFixedProteinLigandOptimizer when the optimization of a ligand in a fixed protein receptor fails due to an initial clash. An appropriate error code is now returned for such cases.
- OEFlexProteinLigandOptimizer now provides an appropriate error code when asked to optimize a design unit that does not contain a ligand.

# 6.6 Szybki TK 2.5.1.2

• Possible crashes in OEFixedProteinLigandOptimizer\_Optimize and OEFlexProteinLigandOptimizer\_Optimize methods have been fixed.

# 6.7 Szybki TK 2.5.1.1

# **6.7.1 New features**

- Optimization of bound ligands with ff14SB/Sage and ff14SB/Parsley force fields with PB solvation forces in rigid and partially flexible receptors is now available.
- Setting the force field to PARSLEY\_OPENFF131 or SAGE\_OPENFF200 now references the most recent official versions of those two parameterizations which are OpenFF\_1.3.1 and OpenFF\_2.0.0 respectively. Older versions are still available from the OEForceFieldType namespace.
- Final ligand geometry is now checked when large initial clashes occur while using OEFixedProteinLigandOptimizer and OESz\_OEFlexProteinLigandOptimizer for optimization of a ligand inside a protein receptor. In most cases, clashes are successfully relaxed; however, in some cases they can lead to a nonphysical minimum which is characterized with distorted geometry. Such results can now be detected by checking the return values of methods OEFixedProteinLigandOptimizer\_Optimize and OEFlexProteinLigandOptimizer\_Optimize.

# 6.7.2 Major bug fixes

- An issue with torsion scan for alkanes using MMFF has been fixed.
- OEFixedProteinLigandOptimizer\_Optimize and OEFlexProteinLigandOptimizer\_Optimize now fails properly when optimization leads to a nonphysical state of a molecule, characterized with distorted geometry. Such nonphysical optimization can sometimes happen when the starting configuration of a protein-ligand complex contains high overlaps.

# 6.7.3 Minor bug fixes

• A warning regarding 'invalidation of receptor' upon optimization using the OEFlexProteinLigandOptimizer class has been removed.

# 6.8 Szybki TK 2.5.0

# **6.8.1 New Features**

- The ability to use the Sheffield Solvation Model has been added to OEFlexProteinLigandOptimizer and OE-FixedProteinLigandOptimizer.
- Two additional methods have been added to the *OEP rote in LigandOptOptions* class:
  - GetSolventModel
  - SetSolventModel

# 6.9 Szybki TK 2.4.0

**Fall 2021** 

# 6.9.1 New features

- A new function, OEGetFreeFormError, is provided that returns error messages corresponding to return codes defined in OEFreeFormReturnCode namespace.
- The latest version of the Open Force Field Initiative, Sage 2.0.0, has been added to  $OEForceFieldType$  as built-in force field OEForceFieldType\_SAGE\_OPENFF200.
- Freeform for estimating free energy of conformations in the ensemble, OEFreeFormConf, now defaults to using the most recent version of the Open Force Field (OESage). Previously it was using *MMFF94S* by default.
- Protein-ligand optimization classes OEFixedProteinLigandOptimizer and OEFlexProteinLigandOptimizer now defaults to using the OEFF14SBSageComplex force field.

# 6.9.2 Minor bug fixes

defaults · OETorsionScanOptions.SetForceField  $now$ properly  $f<sub>O</sub>$ OEForceFieldType MMFF94S.

# 6.10 Szybki TK 2.3.1

July 2021

# 6.10.1 New features

- The latest version of the Open Force Field Initiative, Parsley 1.3.1, has been added to the OEForceFieldType namespace as built-in force field PARSLEY OPENFF131.
- Support for user-defined force fields has been added to the *OETorsionScan* function. Two new API points, SetForceField and GetForceField, have been added for setting and getting this value.
- Support for user defined dihedral angles has been added to *OETorsionScan*. Two new API points, SetUserDefinedAngles and GetUserDefinedAngles, have been added for setting and getting this value.

# 6.11 Szybki TK 2.3.0

**Fall 2020** 

# 6.11.1 New features

- A new SMIRNOFF force field from the Open Force Field Initiative, Parsley 1.2.1, has been added as a built-in force field. It is defined as PARSLEY\_OPENFF121.
- A protein or part of a protein can now be optimized with the FF14SB force field. Cofactors with the exception if HEME are handled by the OpenFF/Parsley force field (for example Parsley 1.2.1), while parameters for HEME are taken from Bryce Group.
- The following preliminary classes have been added that enable optimizing protein-ligand complexes, with or without partial flexibility of the proteins, using the new OEFF14SBParsleyComplex force fields, among others:
  - OEFixedProteinLigandOptimizer
  - OEFlexProteinLigandOptimizer
- A new preliminary class, *OEP roteinLigandOptResults*, has been added that represents results of a protein-ligand complex optimization.
- Two new preliminary classes, OEProteinLigandOptOptions and OEProteinFlexOptions, have been added that provide choices for protein-ligand optimization and protein flexibility.
- A new namespace, OESzybkiReturnCode, and a corresponding function, OEGetSzybkiError, have been added that correspond to return codes from the new optimizer classes.

# 6.11.2 Minor bug fixes

• Protein-ligand optimization with OpenFF/Parsley force fields using OESzybki no longer fails, even when the initial gradient norm is  $1e^{415}$  kcal/(mol A) or larger.

# 6.12 Szybki TK 2.2.0

# 6.12.1 New features

- $\bullet$  Two methods, OESzybkiGeneralOptions.SetForceField new and OESzybkiGeneralOptions.GetForceField, have been added that provide support for custom force fields in Szybki TK. These methods provide users with the ability to use SMIRNOFF force fields that are not built into Szybki TK.
- Two new SMIRNOFF force fields from the Open Force Field Initiative, namely Parsley (OpenFF-1. 0.0) and Parsley (OpenFF-1.1.1), have been added as built-in force fields. They are defined as OEForceFieldType\_PARSLEY\_OPENFF100 and OEForceFieldType\_PARSLEY\_OPENFF111, respectively.
- Potential energy terms in the namespace  $OEPotential Terms$  are now independent of the force field names. Exceptions are combined force fields in which intramolecular terms are taken from MMFF94 as well as intermolecular terms from either AMBER or OEFF.

# 6.12.2 Major bug fixes

• A bug in the entropy calculation for a ligand inside a receptor binding site has been fixed.

# 6.12.3 Minor bug fixes

- Conformer free energy calculation using OEF reeFormConf. EstimateFreeEnergies now produces results identical to performing the calculation in steps using the methods from OEFreeFormConfAdvanced.
- The following methods now return bool, instead of a void:
  - OESzybkiGeneralOptions.SetCalculateGradients
  - OESzybkiGeneralOptions.SetIEFFCluster
  - OESzybkiGeneralOptions.SetIntramolecularVdWCutoff
  - OESzybkiGeneralOptions.SetLigandRMSDHeavy
  - OESzybkiGeneralOptions. SetRemoveAttractiveVdWForces
  - OESzybkiGeneralOptions.SetRemoveCoulombTerms
  - OESzybkiGeneralOptions.SetSoluteDielectric
  - OESzybkiGeneralOptions.SetTemperature
  - OESzybkiGeneralOptions.SetVerbose
  - OESzybkiOptOptions.SetCalculateFrozenTerms
  - OESzybkiOptOptions.SetGradTolerance
  - OESzybkiOptOptions. SetMaxIter
  - OESzybkiSolventOptions.SetAtomicRadiiType
  - OESzybkiSolventOptions.SetCavitySolventParameter
  - OESzybkiSolventOptions.SetSaltConcentration
  - OESzybkiSolventOptions.SetSolventDielectric
  - OESzybkiProteinOptions.SetExactVdWProteinLigand
  - OESzybkiProteinOptions.SetIntermolecularVdWCutoff
  - OESzybkiProteinOptions.SetProteinDielectric
  - OESzybkiProteinOptions.SetProteinFlexibilityRange
  - OEFreeFormConfOptions. SetUseInputEnsemble
  - OEFreeFormConfOptions. SetUseSolventCorr
  - OEFreeFormSolvOptions. SetAtomicRadiiType
  - OEFreeFormSolvOptions. SetChargeType
  - OEFreeFormSolvOptions.SetConfGenRMS
  - OEFreeFormSolvOptions.SetIonicState
  - OEFreeFormSolvOptions. SetMaxConfGen
  - OEFreeFormSolvOptions. SetUseInput3D
  - OEFreeFormSolvOptions. SetUseInputEnsemble

- OEForceFieldType::SMIRNOFF has been renamed OEForceFieldType SMIRNOFF99FROSST for clarity.
- Perceiving residues in the input proteins are now done only when the input protein does not have them.
- Szybki TK now properly handles a hard clash between ligand and protein atoms when a SMIRNOFF force field is used to optimize a ligand inside a receptor (with a gradient norm larger than 1e15).

# 6.13 Szybki TK 2.1.0

## 6.13.1 New features

- OESzybki. SetProtein has been updated to return a Boolean, allowing failures to be handled in code.
- Szybki can now perform energy optimization using a SMIRNOFF force field (https://openforcefield.org/).

# 6.13.2 Minor bug fixes

- The default  $\text{EnergyWindow}$  for conformer generation in  $OEFreeFormConfOptions$  is now consistent with that in OEOmegaOptions in the OEOmegaSampling\_Dense mode.
- Two methods in OEFreeFormConfResults,  $PrintText$  and  $PrintCsv$ , have been modified to widen the scope of the associated streams.

# **6.13.3 Documentation changes**

- A new example program, Optimization of a bound ligand in a partially flexible receptor, has been added.
- A new example program, Single ligand in vacuum using SMIRNOFF, has been added.

# 6.14 Szybki TK 2.0.4

# 6.14.1 Major bug fixes

• OEEstimateSolvFreeEnergy has been fixed to properly calculate solvation energy when used with input molecule charges.

# 6.14.2 Minor bug fixes

· OETorsionScan no longer requires an am1bcc license when OETorsionScanOptions. SetUseSinglePointPB is set to true.

# 6.15 Szybki TK 2.0.3

# 6.15.1 New features

. New OETorsionScanOptions. SetPenaltyForceConstant and OETorsionScanOptions. GetPenaltyForceConstant methods have been added.

# **6.15.2 Documentation changes**

• The example code in the *Estimation of solution ligand entropy* section has been adjusted for solution environment by using the OESolventModel\_Sheffield constant.

# 6.16 Szybki TK 2.0.2

# 6.16.1 New features

- A new method, OESzybkiSolventOptions. SetUseCurrentCharges, has been added as a convenience function.
- Entropy calculation of a bound ligand can now be computed when an IEFF force field is selected (OEForceFieldType\_MMFF\_IEFF or OEForceFieldType\_MMFFS\_IEFF). It uses an accurate numerical Hessian.

# 6.16.2 Minor bug fixes

- An issue related to Szybki TK losing information about already perceived protein residues has been fixed.
- Previously, highly clashed protein-ligand systems that were often a result of docking were not automatically relaxed when using the default OEOptType\_BFGS optimization method. Users had to explicitly use the  $OEOptType\_SD\_BFGS$  method. Now, a clash that exceeds 1e6 (kcal/mol)/A on a gradient norm is detected and 5 steps of steepest descent optimization are automatically applied before the BFGS optimizer is run.

# 6.17 Szybki TK 2.0.1

# 6.17.1 Minor bug fixes

- A crash that occurred when adding harmonic constraint with MMFF\_IEFF has been fixed.
- A problem where the OESzybkiSolventOptions. SetChargeEngine option was not obeyed if using OESzybki. SetProtein has been fixed.

# 6.18 Szybki TK 2.0.0

# 6.18.1 Minor bug fixes

• The OESzybki. GetEntropy method now checks for consistency between the input argument for environment type and the already defined solvent method in OESzybkiOptions. This check ensures that the wrong entropy calculation is not silently performed.

# **6.18.2 Documentation changes**

• The Advanced API section has been removed. The low-level functionality offered through the advanced API has been improved and is now offered as a new toolkit named OEFF TK. The documentation is available at OEFF toolkits.

# 6.19 Szybki TK 1.9.2

# 6.19.1 New features

• Two new classes, OEFreeFormConf and OEFreeFormConfAdvanced, have been added to provide conformer free energy functionality. The methods in OEFreeFormConf provide high-level functionality; those in OE-FreeFormConfAdvanced provide finer control of the functionality.

In general, the new conformer free energy functionality provides 2 new capabilities: (1) methods to estimate restriction free energy and (2) methods to find conformers similar to the one specified from a pool of minimum energy conformers.

- The OEFreeFormConfOptions API methods have been modified and enhanced with OEOmegaOptions and various OESzybkiOptions sub-options. The enhanced API allows greater control over the details of free energy calculation.
- The OESzybkiOptions class has been simplified and now consists of various sub-options: OESzybkiGeneralOptions, OESzybkiOptOptions, OESzybkiSolventOptions, and OESzybkiProteinOptions. The specific methods to set or get option values are now provided through these sub-option classes.

The following table shows the older, deprecated option functions and their new sub-option replacements:

| Deprecated Option Method                            | New Sub-option Method                               |
|-----------------------------------------------------|-----------------------------------------------------|
| OESz::OESzybki::SetIEFFCluster                      | OESzybkiGeneralOptions.SetIEFFCluster               |
| OESz::OESzybkiOptions::SetIEFFCluster               | OESzybkiGeneralOptions.SetIEFFCluster               |
| OESz::OESzybki::GetIEFFCluster                      | OESzybkiGeneralOptions.GetIEFFCluster               |
| OESz::OESzybkiOptions::GetIEFFCluster               | OESzybkiGeneralOptions.GetIEFFCluster               |
| OESz::OESzybki::SetRemoveCoulombTerms               | OESzybkiGeneralOptions.SetRemoveCoulombTerms        |
| OESz::OESzybkiOptions::SetRemoveCoulombTerms        | OESzybkiGeneralOptions.SetRemoveCoulombTerms        |
| OESz::OESzybki::GetRemoveCoulombTerms               | OESzybkiGeneralOptions.GetRemoveCoulombTerms        |
| OESz::OESzybkiOptions::GetRemoveCoulombTerms        | OESzybkiGeneralOptions.GetRemoveCoulombTerms        |
| OESz::OESzybki::SetRemoveAttractiveVdWForces        | OESzybkiGeneralOptions.SetRemoveAttractiveVdWForces |
| OESz::OESzybkiOptions::SetRemoveAttractiveVdWForces | OESzybkiGeneralOptions.SetRemoveAttractiveVdWForces |
| OESz::OESzybki::GetRemoveAttractiveVdWForces        | OESzybkiGeneralOptions.GetRemoveAttractiveVdWForces |
| OESz::OESzybkiOptions::GetRemoveAttractiveVdWForces | OESzybkiGeneralOptions.GetRemoveAttractiveVdWForces |
| OESz::OESzybki::SetLigandRMSDHeavy                  | OESzybkiGeneralOptions.SetLigandRMSDHeavy           |
|                                                     |                                                     |
| OESz::OESzybkiOptions::SetLigandRMSDHeavy           | OESzybkiGeneralOptions.SetLigandRMSDHeavy           |
| OESz::OESzybkiOptions::GetLigandRMSDHeavy           | OESzybkiGeneralOptions.GetLigandRMSDHeavy           |
| OESz::OESzybkiOptions::GetLigandRMSDHeavy           | OESzybkiGeneralOptions.GetLigandRMSDHeavy           |
| OESz::OESzybkiOptions::SetCalculateGradients        | OESzybkiGeneralOptions.SetCalculateGradients        |
| OESz::OESzybkiOptions::SetCalculateGradients        | OESzybkiGeneralOptions.SetCalculateGradients        |
| OESz::OESzybkiOptions::GetCalculateGradients        | OESzybkiGeneralOptions.GetCalculateGradients        |
| OESz::OESzybkiOptions::GetCalculateGradients        | OESzybkiGeneralOptions.GetCalculateGradients        |
| OESz::OESzybkiOptions::SetVerbose                   | OESzybkiGeneralOptions.SetVerbose                   |
| OESz::OESzybkiOptions::SetVerbose                   | OESzybkiGeneralOptions.SetVerbose                   |
| OESz::OESzybkiOptions::GetVerbose                   | OESzybkiGeneralOptions.GetVerbose                   |
| OESz::OESzybkiOptions::GetVerbose                   | OESzybkiGeneralOptions.GetVerbose                   |
| OESz::OESzybkiOptions::SetIntramolecularVdWCutoff   | OESzybkiGeneralOptions.SetIntramolecularVdWCutoff   |
| OESz::OESzybkiOptions::SetIntramolecularVdWCutoff   | OESzybkiGeneralOptions.SetIntramolecularVdWCutoff   |
| OESz::OESzybkiOptions::GetIntramolecularVdWCutoff   | OESzybkiGeneralOptions.GetIntramolecularVdWCutoff   |
| OESz::OESzybkiOptions::GetIntramolecularVdWCutoff   | OESzybkiGeneralOptions.GetIntramolecularVdWCutoff   |
| OESz::OESzybkiOptions::SetTemperature               | OESzybkiGeneralOptions.SetTemperature               |
| OESz::OESzybkiOptions::SetTemperature               | OESzybkiGeneralOptions.SetTemperature               |
| OESz::OESzybkiOptions::GetTemperature               | OESzybkiGeneralOptions.GetTemperature               |
| OESz::OESzybkiOptions::GetTemperature               | OESzybkiGeneralOptions.GetTemperature               |
| OESz::OESzybkiOptions::SetSoluteDielectric          | OESzybkiGeneralOptions.SetSoluteDielectric          |
| OESz::OESzybkiOptions::SetSoluteDielectric          | OESzybkiGeneralOptions.SetSoluteDielectric          |
| OESz::OESzybkiOptions::GetSoluteDielectric          | OESzybkiGeneralOptions.GetSoluteDielectric          |
| OESz::OESzybkiOptions::GetSoluteDielectric          | OESzybkiGeneralOptions.GetSoluteDielectric          |
| OESz::OESzybkiOptions::SetForceFieldType            | OESzybkiGeneralOptions.SetForceFieldType            |
| OESz::OESzybkiOptions::SetForceFieldType            | OESzybkiGeneralOptions.SetForceFieldType            |
| OESz::OESzybkiOptions::GetForceFieldType            | OESzybkiGeneralOptions.GetForceFieldType            |
| OESz::OESzybkiOptions::GetForceFieldType            | OESzybkiGeneralOptions.GetForceFieldType            |
| OESz::OESzybkiOptions::SetCalculateFrozenTerms      | OESzybkiOptOptions.SetCalculateFrozenTerms          |
| OESz::OESzybkiOptions::SetCalculateFrozenTerms      | OESzybkiOptOptions.SetCalculateFrozenTerms          |
| OESz::OESzybkiOptions::GetCalculateFrozenTerms      | OESzybkiOptOptions.GetCalculateFrozenTerms          |
| OESz::OESzybkiOptions::GetCalculateFrozenTerms      | OESzybkiOptOptions.GetCalculateFrozenTerms          |
| OESz::OESzybkiOptions::SetGradTolerance             | OESzybkiOptOptions.SetGradTolerance                 |
| OESz::OESzybkiOptions::SetGradTolerance             | OESzybkiOptOptions.SetGradTolerance                 |
| OESz::OESzybkiOptions::GetGradTolerance             | OESzybkiOptOptions.GetGradTolerance                 |
| OESz::OESzybkiOptions::GetGradTolerance             | OESzybkiOptOptions.GetGradTolerance                 |
| OESz::OESzybkiOptions::SetOptimizerType             | OESzybkiOptOptions.SetOptimizerType                 |
| OESz::OESzybkiOptions::SetOptimizerType             | OESzybkiOptOptions.SetOptimizerType                 |
| OESz::OESzybkiOptions::GetOptimizerType             | OESzybkiOptOptions.GetOptimizerType                 |
| OESz::OESzybkiOptions::GetOptimizerType             | OESzybkiOptOptions.GetOptimizerType                 |
| OESz::OESzybkiOptions::SetMaxIter                   | OESzybkiOptOptions.SetMaxIter                       |
| OESz::OESzybkiOptions::SetMaxIter                   | OESzybkiOptOptions.SetMaxIter                       |
| OESz::OESzybkiOptions::GetMaxIter                   | OESzybkiOptOptions.GetMaxIter                       |
| OESz::OESzybkiOptions::GetMaxIter                   | OESzybkiOptOptions.GetMaxIter                       |
| OESz::OESzybkiOptions::SetSolventDielectric         | OESzybkiSolventOptions.SetSolventDielectric         |
| OESz::OESzybkiOptions::SetSolventDielectric         | OESzybkiSolventOptions.SetSolventDielectric         |
| OESz::OESzybkiOptions::GetSolventDielectric         | OESzybkiSolventOptions.GetSolventDielectric         |
| OESz::OESzybkiOptions::GetSolventDielectric         | OESzybkiSolventOptions.GetSolventDielectric         |
| OESz::OESzybkiOptions::SetSaltConcentration         | OESzybkiSolventOptions.SetSaltConcentration         |
| OESz::OESzybkiOptions::SetSaltConcentration         | OESzybkiSolventOptions.SetSaltConcentration         |
| OESz::OESzybkiOptions::GetSaltConcentration         | OESzybkiSolventOptions.GetSaltConcentration         |
|                                                     |                                                     |
| OESz::OESzybkiOptions::GetSaltConcentration         | OESzybkiSolventOptions.GetSaltConcentration         |
| OESz::OESzybki::SetCavitySolventParameter           | OESzybkiSolventOptions.SetCavitySolventParameter    |
| OESz::OESzybkiOptions::SetCavitySolventParameter    | OESzybkiSolventOptions.SetCavitySolventParameter    |
| OESz::OESzybki::GetCavitySolventParameter           | OESzybkiSolventOptions.GetCavitySolventParameter    |
| OESz::OESzybkiOptions::GetCavitySolventParameter    | OESzybkiSolventOptions.GetCavitySolventParameter    |
| OESz::OESzybki::SetSolventModel                     | OESzybkiSolventOptions.SetSolventModel              |
| OESz::OESzybkiOptions::SetSolventModel              | OESzybkiSolventOptions.SetSolventModel              |
| OESz::OESzybki::GetSolventModel                     | OESzybkiSolventOptions.GetSolventModel              |
| OESz::OESzybkiOptions::GetSolventModel              | OESzybkiSolventOptions.GetSolventModel              |
| OESz::OESzybki::SetAtomicRadii                      | OESzybkiSolventOptions.SetAtomicRadii               |
| OESz::OESzybkiOptions::SetAtomicRadii               | OESzybkiSolventOptions.SetAtomicRadii               |
| OESz::OESzybki::GetAtomicRadiiType                  | OESzybkiSolventOptions.GetAtomicRadiiType           |
| OESz::OESzybkiOptions::GetAtomicRadiiType           | OESzybkiSolventOptions.GetAtomicRadiiType           |
| OESz::OESzybki::SetUseCurrentCharges                | OESzybkiSolventOptions.SetChargeEngine              |
| OESz::OESzybkiOptions::SetUseCurrentCharges         | OESzybkiSolventOptions.SetChargeEngine              |
| OESz::OESzybki::GetUseCurrentCharges                | OESzybkiSolventOptions.GetChargeEngine              |
| OESz::OESzybkiOptions::GetUseCurrentCharges         | OESzybkiSolventOptions.GetChargeEngine              |
| OESz::OESzybki::SetEveryConfAM1BCCCharges           | OESzybkiSolventOptions.SetChargeEngine              |
| OESz::OESzybkiOptions::SetEveryConfAM1BCCCharges    | OESzybkiSolventOptions.SetChargeEngine              |
| OESz::OESzybki::GetEveryConfAM1BCCCharges           | OESzybkiSolventOptions.GetChargeEngine              |
| OESz::OESzybkiOptions::GetEveryConfAM1BCCCharges    | OESzybkiSolventOptions.GetChargeEngine              |
| OESz::OESzybki::SetExactVdWProteinLigand            | OESzybkiProteinOptions.SetExactVdWProteinLigand     |
| OESz::OESzybkiOptions::SetExactVdWProteinLigand     | OESzybkiProteinOptions.SetExactVdWProteinLigand     |
| OESz::OESzybki::GetExactVdWProteinLigand            | OESzybkiProteinOptions.GetExactVdWProteinLigand     |
| OESz::OESzybkiOptions::GetExactVdWProteinLigand     | OESzybkiProteinOptions.GetExactVdWProteinLigand     |
| OESz::OESzybki::SetProteinDielectric                | OESzybkiProteinOptions.SetProteinDielectric         |
| OESz::OESzybkiOptions::SetProteinDielectric         | OESzybkiProteinOptions.SetProteinDielectric         |
| OESz::OESzybki::GetProteinDielectric                | OESzybkiProteinOptions.GetProteinDielectric         |
| OESz::OESzybkiOptions::GetProteinDielectric         | OESzybkiProteinOptions.GetProteinDielectric         |
| OESz::OESzybki::SetProteinFlexibilityRange          | OESzybkiProteinOptions.SetProteinFlexibilityRange   |
| OESz::OESzybkiOptions::SetProteinFlexibilityRange   | OESzybkiProteinOptions.SetProteinFlexibilityRange   |
| OESz::OESzybki::GetProteinFlexibilityRange          | OESzybkiProteinOptions.GetProteinFlexibilityRange   |
| OESz::OESzybkiOptions::GetProteinFlexibilityRange   | OESzybkiProteinOptions.GetProteinFlexibilityRange   |
| OESz::OESzybki::SetIntermolecularVdWCutoff          | OESzybkiProteinOptions.SetIntermolecularVdWCutoff   |
| OESz::OESzybkiOptions::SetIntermolecularVdWCutoff   | OESzybkiProteinOptions.SetIntermolecularVdWCutoff   |
| OESz::OESzybki::GetIntermolecularVdWCutoff          | OESzybkiProteinOptions.GetIntermolecularVdWCutoff   |
| OESz::OESzybkiOptions::GetIntermolecularVdWCutoff   | OESzybkiProteinOptions.GetIntermolecularVdWCutoff   |
| OESz::OESzybki::SetProteinElectrostaticModel        | OESzybkiProteinOptions.SetProteinElectrostaticModel |
| OESz::OESzybkiOptions::SetProteinElectrostaticModel | OESzybkiProteinOptions.SetProteinElectrostaticModel |
| OESz::OESzybki::GetProteinElectrostaticModel        | OESzybkiProteinOptions.GetProteinElectrostaticModel |
| OESz::OESzybkiOptions::GetProteinElectrostaticModel | OESzybkiProteinOptions.GetProteinElectrostaticModel |
| OESz::OESzybki::SetProteinFlexibilityType           | OESzybkiProteinOptions.SetProteinFlexibilityType    |
| OESz::OESzybkiOptions::SetProteinFlexibilityType    | OESzybkiProteinOptions.SetProteinFlexibilityType    |
| OESz::OESzybki::GetProteinFlexibilityType           | OESzybkiProteinOptions.GetProteinFlexibilityType    |
| OESz::OESzybkiOptions::GetProteinFlexibilityType    | OESzybkiProteinOptions.GetProteinFlexibilityType    |

Table 1 - continued from previous page

cor

Table 1 - continued from previous page

# 6.19.2 Minor bug fixes

- User-defined partial charges set for the MMFFS\_AMBER or MMFF\_AMBER force field calculations had previously not been preserved. They are now passed to the optimized molecule.
- Changing the protein flexibility type from range-defined to a list of residues for an OESzybkiOptions object previously required creating a copy of the object. This issue has been fixed.
- Atomic radii for IEFF/PB calculations were previously restricted to the Bondi type. Although the default is still Bondi, ZAP7 and ZAP9 radii are now available.

# 6.20 Szybki TK 1.9.1

# 6.20.1 New features

- Zero point energy is now included in the free energy estimation of conformations.
- The accuracy of the solvation energy calculated in low dielectric solvents  $( $20$ )$  has been increased by doubling the size of the ZAP grid used in the calculation (from 4 to 8 Angstroms).

# 6.20.2 Minor bug fixes

- The API for the method OESz:: OESzybkiOptions:: SetForceFieldType has been changed. Previously, the method returned void. Now it validates the input parameter and returns true if the force field selection is valid and false otherwise.
- . When performing a constrained minimization using the OEProteinElectrostatics\_SolventPBForces electrostatic model, a clash between a protein and a ligand where the square distance exceeds  $0.1<sup>2</sup>$  Angstrom<sup>2</sup> will be detected and a warning will be issued.

# **6.20.3 Documentation fixes**

• Units of the returned values for the methods OESzybkiResults. GetVibEntropy and OESzybkiResults.GetRotEntropy had been incorrectly described as J/(mol K). In fact, both methods return entropy in cal/(mol K). This error has been fixed.

# 6.21 Szybki TK 1.9.0

# 6.21.1 New features

- Analytical second order derivatives in AMBER intermolecular interactions have been added. This new feature allows fast Newton optimization when OEFOrCeFieldType\_MMFF\_AMBER OEForceFieldType\_MMFFS\_AMBER force field is selected with method OESz:: OESzybkiOptions:: SetForceFieldType and a variable OEOptType\_NEWTON is passed to OESz:: OESzybkiOptions:: SetOptimizerType method.
- APIs for torsion scanning is available, including free function  $OETorsionScan$  and classes  $OETorsion-$ ScanOptions and OETorsionScanResult.

# 6.21.2 Minor bug fixes

• API for method OESz:: OESzybkiOptions:: SetIEFFCluster has been changed. Previously, the method had returned void; it now returns bool.

# 6.22 Szybki TK 1.8.7

# 6.22.1 New features

- OESzybkiEnsembleResults. HasEntropy has been added. This new method returns false whenever a requested entropy calculation fails.
- The default behavior of protein-ligand systems handled with MMFF or MMFF\_AMBER OEProteinElectrostatics\_NoElectrostatics force fields has changed from OEProteinElectrostatics\_ExactCoulomb. In other words, Coulomb protein-ligand interactions are included by default. Beginning with this release, removing Coulomb terms from the protein-ligand interactions requires using the OESz:: OESzybkiOptions:: SetProteinElectrostaticModel method with the OEProteinElectrostatics NoElectrostatics argument.
- Previously, the combination of IEFF force field and PB desolvation was restricted to using ESP charges calculated along with atomic multipoles. This restriction has been removed and IEFF for protein-ligand interaction can now be used together with the method OESz:: OESzybkiOptions:: SetUseCurrentCharges.

# 6.22.2 Major bug fixes

- . Return values of the methods OESz:: OESzybkiOptions:: SetExactVdWProteinLigand and OESz:: OESzybkiOptions:: SetProteinFlexibilityRange have been changed from void to bool. This change allows for verifying whether the options have been successfully set.
- When IEFF force field is selected, implying that molecular input files with pre-calculated atomic multipoles have been used, the addition of explicit hydrogens is now disabled. In very rare cases (for example, tetracyanoquinodimethane ligand), perception of bonding might not correspond to the actual ab-initio pre-calculated structure, causing the IEFF calculated energies to be incorrect.
- Using external charges (see method OESz:: OESzybkiOptions:: SetUseCurrentCharges) in the OEFOrceFieldType\_MMFF\_AMBER force field for protein-ligand Coulomb interactions was failing unless the protein was eligible for correct AMBER charging. This unnecessary condition has been removed: any atomic preassigned atomic charges can now be used in combination with AMBER vdW protein-ligand interactions.
- Entropy calculation at very low temperatures is now handled properly: at 0 Kelvin, a value of zero is always returned. At temperatures close to 0 Kelvin, calculation is attempted and a warning is issued if the calculation fails. OESzybkiEnsembleResults. HasEntropy (see above) might be used to query if the OESzybkiResults object contains valid calculated entropy.
- Using IEFF/PB potential for bound ligand optimization in torsion space when the ligand receptor is partially flexible did not always work. This issue has been fixed.

# 6.22.3 Minor bug fixes

• When attempting to use Newton optimization and IEFF force field results, an error is now thrown with the message "Second derivatives not available for IEFF ff".

# 6.23 Szybki TK 1.8.6

# 6.23.1 Major bug fixes

- A memory issue that caused periodic crash of JVM in a situation when torsion optimization was performed and Coulomb terms were removed from the MMFF94 or MMFF94S force field in Java-wrapped code has been fixed.
- Possible memory corruption in the IEFF force field has been fixed.
- making the protein partially flexible and selecting a run type • Previously,  $\sigma$ either OERunType SinglePoint or OERunType TorsionsOpt had been causing crashes. These bugs have both been fixed.
- The order of the residue names generated in the logging output for flexible polar hydrogens for the Protein-Ligand IEFF-MMFF calculation will now be consistent between runs. Previously, the order of the residue names could change in subsequent runs.
- A discontinuity in the flat-bottom harmonic potential has been fixed. The potential function generated by the method OESzybki. SetHarmonicConstraints had a discontinuity in the primary function and its first derivative that caused the optimizer to over-constrain optimizations with harmonic constraints with flat-bottom. The class OEHarmonicPotential has been reimplemented.

# 6.23.2 Minor bug fixes

- Language in the warning regarding the input of atoms with unspecified chirality is improved. It now reads: Input molecule contains chiral atoms with unspecified chirality. This warning may be generated when using the FreeForm part of the Szybki TK.
- OEEstimateConfFreeEnergies now accepts an input ensemble containing a molecule with 20 or more rotatable bonds. Previously, encountering such a molecule resulted in a warning and then that molecule was skipped.

# 6.23.3 Documentation fixes

- Documentation for constants describing optimization in torsional coordinates and translational-rotational coordinates (OERunType\_TorsionsOpt and OERunType\_SolidBodyOpt has been expanded. Specifically, short descriptions of the terms torsional coordinates, and solid-body optimization have been added.
- Missing documentation for the *OEOpt Type\_NEWTON* constant, which sets Newton type optimization, has been added.

# 6.24 Szybki TK 1.8.5

# 6.24.1 New features

- OEForceFieldType\_MMFF\_IEFF and OEForceFieldType\_MMFFS\_IEFF protein-ligand potentials can be now combined with the PB solvent energetics and forces calculated with ESP partial charges that are read from the same molecular input as atomic multipoles.
- The upper limit of the ligand size that might be charged with the AM1BCC partial charges when protein-ligand potential is set using OEForceFieldType\_MMFF\_AMBER or OEForceFieldType\_MMFFS\_AMBER types has increased from 100 to 150 heavy atoms.
- OESetForceFieldDummyAtom can be used to ignore dummy atoms in forcefield calculations if only van der Waals and Coulombic components are included. Dummy atoms are ignored in MMFF force fields and cannot be used in intramolecular components.
- OESzybkiResults. Clear has been added to reset the state of the OESzybkiResults object.

# 6.24.2 Major bug fixes

• OESzybki will no longer crash when OESz:: OESzybkiOptions:: SetForceFieldType is called with the argument OEFOrCeFieldType\_MMFFS\_AMBER and then followed by a call of OESz:: OESzybkiOptions:: SetUseCurrentCharges with true.

# 6.24.3 Minor bug fixes

- $OESzvbki$ , operator () will no longer lose SD data when operating on a single conformer OEMolBase.
- OESzybkiResults is now cleared from whenever  $OESzybki$ .  $operator()$  fails. Clearing is done by the new method OESzybkiResults. Clear. A cleared OESzybkiResults will make OESzybkiResults. Print output: OESzybkiResults object does not have data to report.
- . OESz:: OESzybki:: GetForceFieldType now properly returns OEForceFieldType\_MMFF\_AMBER or OEFOrceFieldType\_MMFF\_IEFF. Previously, they could only be returned after a calculation was performed with the OESzybki object.
- A CYS residue bonded by the sulfur to something other than another CYS residue is no longer treated as anionic by the AMBER charging system.
- Final geometry of a ligand optimized with the MMFF IEFF or MMFFS IEFF potential has been updated with the transformed multipoles attached to atoms as generic data.
- A potential memory leak when performing repeated protein-ligand minimizations has been fixed.

# **6.24.4 Documentation fixes**

- OEFuncType has been documented.
- The Optimization of all conformers of a ligand section has a new example that demonstrates how to minimize all conformers in a ligand.

# 6.25 Szybki TK 1.8.4

# 6.25.1 New features

• A new OESingleConfResult. GetRelLnQ method has been added for retrieving the logarithm of the relative vibrational-rotational partition function with respect to the minimum free-energy conformation.

# 6.25.2 Major bug fixes

• Previously, when protein-ligand systems where ligands were made of two or more molecules (for example, an inhibitor + water molecule), interligand IEFF interaction energy was not correctly calculated in two cases: (1) for single point calculations and (2) for solid-body ligand pose optimization. In both cases, the total proteinligand interaction energy was not affected. In the second case, optimization itself was not affected. This issue has been fixed.

# 6.25.3 Minor bug fixes

- Internal refactoring has been performed to improve stability.
- Memory leaks related to protein-ligand interaction and handling protein flexibility have been fixed.

# 6.25.4 API Changes

• The unused OEMMFFSubsetVdw class has been removed.

# **6.25.5 Documentation fixes**

• Cross-references have been fixed in several sections.

# 6.25.6 Java- and C#-specific changes

- The following examples were added for Java and C#:
  - Ligand in vacuum optimization
  - Optimize multiple ligands in Sheffield solvation model
  - Partially flexible protein optimization
  - Partially flexible protein with Newton-Raphson optimization
  - FreeForm Solvation
  - FreeForm Conformer
  - Entropy of a bound ligand
  - Bound ligand optimization
  - Rigid receptor optimization
  - Newton-Raphson optimization
  - Bound and solution entropy

- PB Protein-ligand binding

# 6.26 Szybki TK 1.8.3

# 6.26.1 New features

• New forcefield for ligand-ligand and protein-ligand interactions has been added. It is a combination of MMFF94S (or MMFF94) with intermolecular potential called IEFF developed at OpenEye. In this combined force field, MMFF94S is used to describe the intramolecular interactions while IEFF which has 3 components (vdW, Coulomb and Fermi repulsion) handles intermolecular interactions. Coulomb terms in IEFF require precalculated and assigned atomic multipoles to ligand and protein molecules. This task can be achieved with two OpenEye codes called MOLQM and PROTQM. IEFF has been described in the following publication:

```
N. Hamaguchi, L. Fusti-Molnar and S. Wlodek
Force-field and quantum-mechanical binding study of selected SAMPL3 host-quest
\rightarrowcomplexes
J. Comput. Aided Mol. Des. Vol. 26, pp. 577-582, 2012
```

Please contact support@eyesopen.com if you are interested in testing this new forcefield.

- New overloaded method OESzybki. Set TorsionConstraint has been added to the public API. It allows selectively constraining a specific torsion in the optimized molecule.
- A set of flexible residues in ligand optimization with partially flexible protein is no longer restricted to the specified distance from the ligand. This goal has been achieved by the expansion of the OEProtFlex namespace for new constants which might be passed to the OESz:: OESzybkiOptions:: SetProteinFlexibilityType method, and the addition of the new method OESz:: OESzybkiOptions:: AddFlexibleResidue which can be used multiple times to make a set of residues flexible.
- Added new virtual method OEOpt:: OEFunc1:: IsRedundant. It allows to check if two formally numerically different sets of coordinates indeed represent two different points in the coordinate space. This method has no trivial implementation in OEQuatAdaptor. IsRedundant.
- MMFF calculations now allow for a "DUMMY" atom type, OEMMFFType\_DUMMY to specify that an atom should be avoided during an MMFF energy calculation.
- Added a DUMMY atom type to the AMBER force field to specify that an atom should be avoided during an AMBER energy calculation.

# 6.26.2 Major bug fixes

- Fixed a rare crash when using the AMBER force field on some platforms.
- $\bullet$  A combination of Newton optimization with the use of the following methtwo ods: OESz::OESzybkiOptions::SetProteinElectrostaticModel and OESz::OESzybkiOptions::SetExactVdWProteinLigand with parameters OEProteinElectrostatics\_ExactCoulomb and true respectively caused that Coulomb potential was missing from the intermolecular interaction. That bug has been fixed.
- . OESzybkiResults. GetLnQvib and OESingleConfResult. GetLnQvibrational will no longer return negative infinity on Windows for large ligands.

# 6.26.3 Minor bug fixes

- Fixed the name of the saved electrostatic grid file when the name of the molecule is used as part of the file name, by replacing all non alpha-numeric characters with an underscore character.
- An attempt to use Newton optimization with a potential for which second derivatives are not implemented is terminated with a proper error message.
- When AM1BCC charges are selected in Sheffield or PB solvation models for multiply charged species, SCF procedure in AM1 might not converge within 20 cycles (this has been observed for methotrexate only so far). To make sure that the electron density is converged, and calculated atomic charges stable, we allow up to 1000 SCF iterations for multiply charged molecules.
- Return value of the method OESzybkiResults. GetTotalEnergy for protein-ligand system with partially flexible protein does not contain intrinsic MMFF energy of the protein.
- An attempt to use protein flexibility type which is not a member of the  $OEProtFlex$  namespace in the method OESz:: OESzybkiOptions:: SetProteinFlexibilityType' issues an error message "Unrecognized protein flexibility.
- An error message generated upon the attempt of using partially flexible protein in solid body optimization type is generated instead of warning.
- A more informative error message is generated upon the attempt of free ligand entropy estimation in the situation when protein environment is set.
- An error message is generated when trying to use Newton optimization for protein-ligand systems with protein electrostatic models different than OEProteinElectrostatics\_NoElectrostatics or OEProteinElectrostatics ExactCoulomb
- Flexible polar hydrogens are printed when residue polar hydrogens are asked to be optimized along with the ligand.

# **6.26.4 Documentation fixes**

• Documentation for the OEMo1MMFF:: OEMMFFSubsetVdw class has been removed.

# 6.27 Szybki TK 1.8.2

# 6.27.1 New features

- OEEstimateSolvFreeEnergy and OEEstimateConfFreeEnergies added to perform FreeForm calculations. Their usage requires passing instances of the following classes:
  - OEFreeFormSolvOptions
  - OEFreeFormConfOptions
  - OEFreeFormSolvResults
  - OEFreeFormConfResults
- OEOpt::OEFunc1::CheckVariablesValidity added for checking the validity of arguments for the function to be optimized. The users of the all classes derived from OEFunc1 can implement it according to specific features of their objective functions.

. OESz::OESzybki::GetSolutionEntropyandOESz::OESzybki::GetProteinBoundLigandEntropy have been officially deprecated. OESzybki. GetEntropy that returns double values by reference has also been deprecated. Users should switch to using the OESzybkiEnsembleResults object instead.

# 6.27.2 Major bug fixes

- Dangling pointer in the implementation of the  $OESzybki$ . Unset Protein has been found and fixed.
- Setting up a Newton-Raphson optimization on large systems can easily exhaust the amount of memory needed because of the  $O(n^2)$  Hessian matrix. If memory exhaustion is detected, the calculation will now error out instead of crashing.
- An exception has been added to catch the memory exhaustion upon Hessian allocation used for Newton-Raphson optimization of large systems. That could happen on some platforms with limited memory (for example Win32).
- OESzybkiOptions can now be passed to the OESzybki constructor.
- OEProtFlex namespace constants are now available in Python, Java, and C#.

# 6.27.3 Minor bug fixes

- Removed unbounded stack allocations.
- Verbose mode of some protein-ligand optimization could not report the number of cycles at the very end of optimization.
- Warning is issued upon the attempt to remove Coulomb terms from the combined force field Amber-MMFF (and Amber-MMFFS) with methods OESz:: OESzybki:: SetRemoveCoulombTerms and OESz::OESzybkiOptions::SetRemoveCoulombTerms.
- . Unnecessary and confusing warning Warning: Solid-body optimization allowed only for ligand in fixed protein is eliminated when OESzybkiOptions. SetRunType is used with the OERunType\_SolidBodyOpt argument.

# 6.27.4 Documentation fixes

- Examples added to demonstrate how to do an entropy estimation.
- Examples have been updated to use non-deprecated APIs.
- Python examples have been renamed to more accurately reflect their function. Some examples added to demonstrate additional functionality.

# 6.28 Szybki TK 1.8.1

# 6.28.1 New features

- OENewtonOpt added for Newton-Raphson optimization.
- OESzybkiOptions class added for setting all options of the OESzybki object during construction. All new functionality, starting from the mentioned above Newton-Raphson optimization, will only be available through the OESzybkiOptions class. All the OESzybki methods with the same name as their OESzybkiOptions counterpart are deprecated and will be removed in Szybki TK.
- OEOptimizer2 abstract base class added to allow optimizers that use analytical second derivatives.

- Newton-Raphson optimization method added as an option for minimization. For this release it is restricted however to the MMFF94/MMFF94S force field and Sheffield solvation model. It is available only for optimization in Cartesian coordinates.
- The string representation of the gradient norm by the OECheckpoint1 object and by the  $OESzybkiResults$ . Print method will be in scientific notation to provide better precision.
- The following methods have been added to  $OESzybkiResults$ :
  - OESzybkiResults.GetVibEntropy
  - OESzybkiResults.GetRotEntropy
  - OESzybkiResults.GetLnQvib
  - OESzybkiResults.GetLnQrot
- Efficiency of diagonalization of Hessian matrix is improved.
- Added two new example programs showing how to use Newton-Raphson optimization.

# 6.28.2 Major bug fixes

- Calculation of PB solvent forces will no longer run out of memory and crash due to violent moves of the optimizer.
- . OESzybki. LoadPotentialGrid and OESzybki. SavePotentialGrid will no longer crash due to the length of the file name passed.
- *OESzybki* will no longer allow a solid-body optimization in partially flexible protein as this was never an intended feature.

# 6.28.3 Minor bug fixes

- OESzybki. SetProtein will now fail and throw a warning if all the protein coordinates are zero.
- $OESzybkiResults. Print$  output will now include MMFF terms for a protein-ligand complex single-point calculation when OESzybki. SetProtein was called before OESz:: OESzybki:: SetRunType.

# **6.28.4 Documentation fixes**

• OESzybkiEnsembleResults. GetChargeType return type is now properly documented.

# 6.29 Szybki TK 1.7.5

# 6.29.1 New features

- User partial charges can be used in the combined AMBER-MMFF force field introduced in the version 1.7.3. This is done with the method OESz:: OESzybki:: SetUseCurrentCharges which until now could be applied only to MMFF94 force field for solvation and protein-ligand interaction.
- OEOptType\_SD\_BFGS OEOptType\_SD\_CG and can now be passed to OESz:: OESzybki:: SetOptimizerType to perform pre-optimization with 5 steps of steepest descent before either BFGS or CG optimization.

- OESzybkiEnsembleResults. GetChargeType added to return what type of partial charges were used for entropy estimation.
- · OESzybkiResults.GetTotalEnergy no longer includes the harmonic constraint energy. OESzybkiResults.GetTotalEnergyWithHarmConstraint has been added to return the total energy with the harmonic constraint energy included.

# 6.29.2 Minor bug fixes

- . OESz:: OESzybki:: SetEveryConfAM1BCCCharges will now preserve the existing partial charges from the input molecule when using AM1BCC charges for PB, Sheffield and Coulomb protein-ligand interactions. In previous versions MMFF94 charges were attached to the output molecule.
- When calculating ligand entropy, analytical calculation of second order derivatives in solution no longer misses the Hessian components coming from solvent forces.
- OESzybki. GetEntropy will no longer crash whenever a protein was set with OESzybki. SetProtein and the environment was not OEEnvType\_Protein.
- Method OESz:: OESzybki:: SetUseCurrentCharges was ignored in Sheffield solvent second derivatives (default MMFF94 partial charges were used). This issue has been fixed.

# 6.30 Szybki TK 1.7.4

# 6.30.1 Bug fixes

- OESzybkiEnsembleResults is now usable with OESzybki. GetEntropy from Python, Java, and C#
- OEOpt:: OEMaxStepLineMinimize:: SetMaxStep had its arguments in the incorrect order for inheriting from OELineMinimize.
- OEBFGSOpt now properly handles gradients approaching zero.

# 6.31 Szybki TK 1.7.3

# 6.31.1 New features

- A new forcefield for protein-ligand interactions has been added. It is a combination of MMFF94S (or MMFF94) with Amber. In this combined force field, MMFF94S is used to describe the intramolecular interactions of the ligand and the Amber force field is used for the VdW and Coulomb interactions between ligand and protein. Currently, this force field can be used only for ligands inside rigid proteins.
- Two new methods were added to the API:  $OESzybki.SetTorsionConstraint$  and  $OESzybki.$ ClearTorsionConstraint. The first one adds a single-minimum harmonic torsional constraint for a torsion which is defined by a SMARTS pattern. It uses the functional form:  $V = k_c(cos(phi) - cos(phi0))^2$ , where  $k_c$  is the user specified force constant and  $phi$  is the reference torsion dihedral angle. The second method removes the torsional constraint if it exists.
- Estimation of ligand entropy using analytical MMFF Hessian is extended for ligands bound in a rigid protein. Previously the entropy of only free ligands in vacuum or in solution could be estimated with analytical second derivatives.

# 6.31.2 Major bug fixes

• A few numerical errors in the calculation of analytical second derivatives (Hessian matrix) in MMFF torsion and out-of plane terms have been fixed.

# 6.31.3 Minor bug fixes

- Constraint energy was reported twice by the method  $OESzybkiResults.Print$ . The problem is fixed.
- $\bullet$  The OESz::OESzybki::GetExactVdWProteinLigand method was misspelled (GetExactVdEProteinLigand instead of GetExactVdWProteinLigand).
- When preoptimized ligands are used for entropy estimation it is necessary to gently move the ligand out of the minimum. The gradient normal below which such a perturbation was done was raised from 1 kcal/(mol Å) to 10 kcal/(mol A). Research showed that for some conformations the above limit was too low which resulted in overestimation of its vibrational entropy.

# 6.32 Szybki TK 1.7.2

# 6.32.1 New features

- Two new API methods added: SetIntramolecularVdWCutoff and GetIntramolecularVdWCutoff
- . Methods OESz:: OESzybki:: SetProteinVdWCutoff and OESz:: OESzybki:: GetProteinVdWCutoff have become deprecated. They have been replaced by OESz:: OESzybki:: Set IntermolecularVdWCutoff and OESz:: OESzybki:: GetIntermolecularVdWCutoff respectively.
- Steepest descent (OEOpt Type\_SD) method added as an optional optimizer instead of BFGS.

# 6.32.2 Major bug fixes

• OESzybkiEnsembleResults now accessible from Python.

# 6.32.3 Minor bug fixes

- Reusing the OESzybki object after ligand entropy estimation in the protein environment, for other, non-entropy runs of a ligand inside the same protein, required an extra call to  $OESzybki$ . Set Protein in order to set correctly the new protein-electrostatic model correctly. This is not needed anymore.
- In the rare case when ligand is moved out from the protein binding site during entropy estimation the run is terminated with the proper warning. Previously, in such a case the attempts were done to reoptimize the ligand and rebuild the Hessian. Such a strategy was wrong because even if formally successful, it would lead to physically meaningless results. The situation described here can happen when the ligand is poorly docked, or if the X-ray structure used as input is very inaccurate.
- . When the method OESz:: OESzybki:: SetUseCurrentCharges was used which causes the use of input charges for PB or Sheffield calculations, the molecule which was processed with the  $OESzybki$ .  $operator()$  methods, on exit received the mmff94 charges. That behavior has been replaced by retaining the initial charges, and zeroing the molecule's partial charges when the input molecule had none.
- Error message for the case when the input structure generates infinite initial gradients is more informative.

# 6.33 Szybki TK 1.7.1

# 6.33.1 New features

- OESzybki. GetEntropy added which takes a non-const multiconformer molecule and a reference to a new object OESzybkiEnsembleResults. The method evaluates ligand entropy in different environments as other existing methods, however in addition provides essential data on the ensemble of ligand conformations. Specifically, it returns the optimized ensemble of unique ligand conformations in its first parameter, and populates the OESzybkiEnsembleResults objects with entropy components data for the ensemble. The OESzybkiEnsembleResults also provides the data for individual unique optimized conformations in the ensemble; in particular the free energy of isolating a specific conformation from the entire ensemble. An example code explaining the usage of the new OESzybki, GetEntropy method and the OESzybkiEnsembleResults class has been added.
- OESzybkiEnsembleResults class added that is mentioned above has been added.
- Two new API methods have been added which control the temperature in the entropy estimation. These are: SetTemperature and GetTemperature. The default temperature is 298K.

# 6.33.2 Bug fixes

- OESzybki. SetHarmonicConstraints did not impose harmonic constraints on flexible part of the protein. The problem has been fixed.
- Trying to reuse an OESzybki instance after an entropy calculation sometimes (depending on the subsequent methods call order) caused a crash. To work around that problem it was necessary to use a new instance of the *OESzybki* class. This bug has been fixed.
- Method  $OESzybki$ . ClearFixAtoms did not clear the unnecessary evaluation of the complete ligand energy at the very end of optimization with a subset of atoms frozen. The problem has been fixed.
- Protection against exhausting memory upon the usage of too many Coulomb atom pairs (for example in the attempt to optimize a large protein) has been added. Also, a confusing message upon exhausting the memory with too many vdW interactions has been removed.
- A warning is now issued in the case where one of the three methods setting the protein flexibility is used (SetSideChainsFlexibility, SetPolarHFlexibility or SetResidueFlexibility) when protein is not set. Also, a request of single point calculation (using SetRunType) properly clears any previous settings of partial protein flexibility.
- In the default optimization of a ligand inside the protein receptor the convergence criteria set by the method SetOptimizerType were not consistent with the intrinsic criteria of one the optimizers used. This inconsistency has been fixed.
- Using conjugate gradient optimizer (set with the SetOptimizerType) in combination with the method SetEx*actVdWProteinLigand* did not report the number of cycles made by the optimizer. This problem has been fixed.

# 6.34 Szybki TK 1.7.0

# 6.34.1 New features

• An extension of the MMFF94 force field for tricoordinate boron compounds is offered in this release. Most compounds containing B-X bonds where X=C,N,O,S, and H are covered with the following exceptions: X=N(imine),N(sulfonamide), N(pyridinium) and N(quaternary). Also not supported are compounds in which boron is bonded to X=F,Cl,Br,I,B and Si, or makes a bond angle BYX. Compounds in which boron is a part of four-membered rings of B1CCC1 type are also not available in the current parameterization because their existence is questionable: Ab initio calculations at the MP2/6-31G<sup>\*\*</sup> level failed to identify stable structures for them (highly polar structures in which boron is four-coordinated are formed).

- NOTE WELL: Because of the partial parameterization for boron-containing compounds, users of the OEMMFF class (derived from OEGenericFF) need to pay attention to the return value of the OEMolPotential:: OEGenericFF:: Setup method: In the case where the parameters for a specific boron molecule are not available, this function returns false. Checking the return value of OEMolPotential:: OEGenericFF:: PrepMol is not enough, because it does not catch the case of missing force field parameters for a specific compound.
- Two new API methods have been added which control the salt concentration for all PB calculations with Szybki TK. These are: SetSaltConcentration and GetSaltConcentration. The first method takes salt concentration in M as a float number. The valid range is  $0 - 0.08M$ ; this method should not be used for higher salt concentrations. The second method returns the current salt concentration as a float. Default value is zero. Previous versions of Szybki TK assumed zero salt concentration.
- All PB calculations carried out with the previous Szybki TK versions used Bondi atomic radii. The current release offers two additional sets of atomic radii, called ZAP7 and ZAP9 as alternatives. They are described by Nicholls et. al. The new method: SetAtomicRadii allows the use of one of these two sets. The new method GetAtomicRadiiType returns the type of current atomic radii set.
- Better control of dielectric constants is provided. This includes a new method: SetSolventDielectric which allows change from the default value of 80. Method GetSolventDielectric returns the current value of the solvent dielectric constant. Method: SetSolventModel which determines the solvation model for a free ligand in solution, now takes an additional default parameter which sets the intrinsic dielectric constant of the ligand.
- A method which obtains gradients from the single point calculations is added. Specifically, a new method  $OESzybkiResults. GetGradients$  is added to the szybki results. h header, and two new methods to the szybki.h header file. There are: SetCalculateGradients and GetCalculateGradients.
- Enforcement of proper behavior by the  $OESzybki. operator()$  for molecules without 3D coordinates. Such molecules are not processed and a warning is issued.

# 6.34.2 Bug fixes

- Method GetProteinBoundLigandEntropy is protected from selection of an inappropriate proteinligand electrostatic model (entropy calculations for protein-bound ligands are done with the OEProteinElectrostatics\_ExactCoulomb model).
- Calling SetRunType with an argument OERunType\_CartesiansOpt immediately after a call to same method but with an argument OERunType\_TorsionsOpt caused missing potential values for bonds and bond angles. The problem is fixed.
- Method OESzybkiResults. Print was not reporting MMFF terms in the case when OESzybki. Set Protein was used. The bug is fixed. Also, some minor improvements to this method is made, so it is clear which terms contribute to the total protein-ligand interactions and which are reported only for comparison. For example the usage of *OEProteinElectrostatics* results in reporting the exact and approximated Coulomb terms, however only the latter is used in the reported protein-ligand interaction.
- Fixed a minor bug where unnecessary warnings regarding missing protein parameters were issued in an entropy calculation where the protein is held rigid. This happens when mistakes or inaccuracies in the input protein structures lead to undefined force field parameters.
- Previously, processed molecules were output with aromaticity specified according to the MMFF94 aromaticity model. Now, output molecule are converted to the OE aromaticity model.
- Entropy calculations using the quasi-Newton method now give significantly more accurate answers in the two extreme cases where the input ligand structure is a) already optimized, or b) has a very high-energy (i.e. poor) structure.

# 6.35 Szybki TK 1.6.0

# 6.35.1 New features

- The algorithm for entropy estimation has been improved, specifically the calculation of vibrational entropy. It can now handle molecules with up to 2000 atoms. The previous limit was about 200 atoms.
- Entropy calculation of protein-bound ligands has been modified. This change refers to the partial desolvation entropy of the protein receptor. In the previous version, eq. 26 in Wlodek-2010 had been used to evaluate the fraction of ligand exposed to the solvent. Recent unpublished data has shown that a much more accurate estimation can be achieved by using the direct surface calculation with Spicoli TK. This change was shown to be better at reproducing binding entropies.
- Method SetSolventModel now takes a dielectric constant as a second argument. Its default value is 80. In the previous versions dielectric constant was assumed to be 80 and the user could not change its value.
- Badly defined input molecules with very small distances between atoms (< 1e-3 A) that could generate infinite initial forces are now detected and no attempt is made to optimize such molecules. A warning "Geometry of the input protein or conformation is badly defined!" is issued so the user is forced to correct the geometry of the input molecules.
- A capability of calculating solution entropy for monoatomic ions like Na::math  $^+$  or F::math  $^+$  and noble gases is added.
- Documentation for three libraries: opt, mmff and molpotential, which in the past were called CASE, was added.

# 6.35.2 Bug fixes

• Estimation of entropy with the quasi-Newton method returned differing results (up to 6%) on different platforms. The problem was due to numerical-instability in the calculation of second derivatives. This problem has been eliminated in the current release with the use of a more stable method for line minimization (a backtrack line search).

# 6.36 Szybki TK 1.5.0

# 6.36.1 New features

• Entropy calculations of a ligand in different environments can be performed based on the methods described in the recent paper of Wlodek et. al. ([Wlodek-2010]).

New methods added to the public API are:

- OESzybki.GetEntropy
- GetSolutionEntropy
- GetProteinBoundLigandEntropy
- Default VdW protein-ligand potential used for the optimization of a ligand inside the protein binding site is precalculated in the form of a lookup table. This is done for the purpose of speed. The exact VdW proteinligand potential can be used with the new method:

- SetExactVdWProteinLigand

when boolean parameter passed is true. Passing false causes switching to the default form of the proteinligand VdW. The function:

- GetExactVdWProteinLigand

allows the querying of which form of the VdW potential is used.

- Two functions have been added to the public API in szybki.h. The first new function allows the use of conformation-dependent AM1BCC charges for every conformation in the calculation of PB and Sheffield solvation energies, for protein-ligand Coulomb interactions, and in entropy calculations.
  - SetEveryConfAM1BCCCharges

The second function returns  $t$  rue if AM1BCC are being calculated for every conformation,  $false$  otherwise.

- GetEveryConfAM1BCCCharges

# 6.36.2 Bug fixes

• In a special situation of ligand optimization in the protein binding site with the use of the electrostatics model determined by the OEProteinElectrostatics\_ExactCoulomb, constant, when the optimization was preceded by the Zap binding calculations with the same protein and the same ligand, Coulombic interaction resulted in zero value. This bug has been fixed.

# 6.37 Szybki TK 1.4.0

## 6.37.1 New features

- Starting from the current release, certain classes of divalent selenium compounds can be handled by SZYBKI. Currently only some compounds in which selenium is bonded to the hydrogen or carbon atoms can be processed. Those compounds include selenols (RSeH) and selenides (RSeR1) in which Se is bonded to alkyl or aromatic carbon atoms, with the following exceptions:
  - $-$  Se makes a bond with alkyl C which belongs to the 3- or 4-membered ring
  - Se makes a bond with aromatic C which belongs to 5-membered ring

In the restriction above the MMFF94 aromaticity model is adopted, so for example a pyridine derivative, pyridine-3-selenol can be processed, but a pyran derivative 2H-pyran-3-selenol cannot.

- Previous SZYBKI releases attempted to assign the "closest" MMFF94 atom type to those atoms for which a unique MMFF94 type could not be found. Starting from the 1.3.5 SZYBKI Application release this feature is removed, so consequently the input molecules containing such atoms will not be processed.
- Ligand RMSD which might be extracted from OESzybkiResults object, can optionally refer to heavy atoms only. A new public function:

void SetLigandRMSDHeavy (bool)

in OESzybki class has been added for that purpose.

# 6.37.2 Bug fixes

- A bug causing memory corruption when the function SetSideChainsFlexibility () was called after SetProten () was fixed.
- Memory leak in ligand torsion optimization inside the partially flexible protein receptor was removed.

# 6.38 Szybki TK 1.3.4

# 6.38.1 New features

• Calculation of the constant potential terms at the end of adapted optimization can be optionally eliminated, by the usage of the function void SetCalculateFrozenTerms (bool). This feature reduces memory and cpu usage in the case of partial optimization of large molecules.

# 6.38.2 Bug fixes

- Member function ClearFixAtoms () did not clear properly previously fixed atoms. As a result, in spite of its use some atoms were still fixed. This bug has been fixed.
- A bug which occasionally caused errors in fixing a subset of atoms was fixed.

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

#### For example:

MaaS 1.0. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://www.eyesopen.com.

The MaaS version number appears on the web service's release notes.

**TEN** 

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                                             | License                                                              |
|-------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                                | https://                                                             |
| absl-py                       | https://github.com/abseil/absl-py                                                   | https://                                                             |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                                 | https://                                                             |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                               | https://                                                             |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                               | N/A                                                                  |
| AmberUtils                    | http://ambermd.org                                                                  | N/A                                                                  |
| ambit                         | https://github.com/khimaros/ambit                                                   | https://                                                             |
| amqp                          | https://github.com/celery/py-amqp                                                   | https://                                                             |
| anaconda-anon-usage           | Orion Floes                                                                         | https://                                                             |
| angular                       | https://github.com/angular/angular.js                                               | https://                                                             |
| angular-animate               | https://github.com/angular/angular.js                                               | https://                                                             |
| angular-cache                 | https://github.com/jmdobry/angular-cache                                            | https://                                                             |
| angular-cookies               | https://github.com/angular/angular.js                                               | https://                                                             |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                                    | https://                                                             |
| angular-mocks                 | https://github.com/angular/angular.js                                               | https://                                                             |
| angular-resource              | https://github.com/angular/angular.js                                               | https://                                                             |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                                    | https://                                                             |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                               | https://                                                             |
| angular-ui-router             | https://github.com/angular-ui/ui-router                                             | https://                                                             |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                                  | https://                                                             |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                                        | https://                                                             |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                                            | https://                                                             |
| annotated-types               | https://github.com/annotated-types/annotated-types                                  | https://                                                             |
| anyio                         | https://github.com/agronholm/anyio                                                  | https://                                                             |
| appdirs                       | https://github.com/ActiveState/appdirs                                              | https://                                                             |
| appengine                     | https://google.golang.org/appengine                                                 | https://                                                             |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                                   | https://                                                             |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md                          | https://                                                             |
| Name of Project               | Website                                                                             | License                                                              |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                | https:/                                                              |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                       | https:/                                                              |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                          | https:/                                                              |
| ascii85                       | https://github.com/huandu/node-ascii85                                              | https:/                                                              |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                      | https:/                                                              |
| asgiref                       | https://github.com/django/asgiref/                                                  | https:/                                                              |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                                 | https:/                                                              |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render               | https:/                                                              |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers                   | https:/                                                              |
| assertions                    | https://github.com/smartystreets/assertions                                         | https:/                                                              |
| asttokens                     | https://github.com/gristlabs/asttokens                                              | https:/                                                              |
| astunparse                    | https://github.com/simonpercivall/astunparse                                        | https:/                                                              |
| async-lru                     | https://github.com/aio-libs/async-lru                                               | https:/                                                              |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                           | https:/                                                              |
| atk-1.0                       | https://docs.gtk.org/atk/                                                           | https:/                                                              |
| atomic                        | https://github.com/uber-go/atomic                                                   | https:/                                                              |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                    | https:/                                                              |
| attrs                         | https://www.attrs.org/                                                              | https:/                                                              |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                                   | https:/                                                              |
| Babel                         | https://github.com/python-babel/babel                                               |                                                                      |
| backcall                      | https://github.com/takluyver/backcall                                               | https:/                                                              |
| backports                     | https://github.com/brandon-rhodes/backports                                         | https:/                                                              |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                             | https:/                                                              |
| base62                        | https://github.com/kare/base62                                                      | https:/                                                              |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                      | https:/                                                              |
| billiard                      | https://github.com/celery/billiard                                                  | https:/                                                              |
| biopython                     | https://biopython.org                                                               | https:/                                                              |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https:/                                                              |
| bitset                        | https://github.com/willf/bitset                                                     | https:/                                                              |
| blas                          | https://www.netlib.org/blas/                                                        | https:/                                                              |
| bleach                        | https://github.com/mozilla/bleach                                                   | https:/                                                              |
| blessings                     | https://github.com/erikrose/blessings                                               | https:/                                                              |
| blinker                       | https://pythonhosted.org/blinker/                                                   | https:/                                                              |
| blosc                         | https://github.com/Blosc/python-blosc                                               | https:/                                                              |
| blosc2                        | https://github.com/Blosc/python-blosc2                                              | https:/                                                              |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https:/                                                              |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                              |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                                              |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                                              |
| boto3                         | https://github.com/boto/boto3                                                       | https:/                                                              |
| botocore                      | https://github.com/boto/botocore                                                    | https:/                                                              |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                                              |
| Brotli                        | https://github.com/google/brotli                                                    | https:/                                                              |
| brotli-bin                    | https://github.com/google/brotli                                                    | https:/                                                              |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                                              |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                          | https:/                                                              |
| bson                          | http://github.com/py-bson/bson                                                      | https:/                                                              |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https:/                                                              |
| bzip2                         | https://www.bzip.org                                                                | https:/                                                              |
| Name of Project               | Website                                                                             | License                                                              |
| c-ares                        | https://github.com/c-ares/c-ares                                                    | https://                                                             |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            | https://                                                             |
| cached-property               | https://github.com/pydanny/cached-property                                          | https://                                                             |
| cachetools                    | https://github.com/tkem/cachetools/                                                 | https://                                                             |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           | https://                                                             |
| canvas                        | https://github.com/Automattic/node-canvas                                           | https://                                                             |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              | https://                                                             |
| celery                        | https://github.com/celery/celery                                                    | https://                                                             |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         | https://                                                             |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                           | https://                                                             |
| cffi                          | https://github.com/python-cffi                                                      | https://                                                             |
| cftime                        | https://pypi.org/project/cftime/                                                    | https://                                                             |
| chardet                       | https://github.com/chardet/chardet                                                  | https://                                                             |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        | https://                                                             |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             | https://                                                             |
| click                         | https://palletsprojects.com/p/click/                                                | https://                                                             |
| click-completion              | https://github.com/click-contrib/click-completion                                   | https://                                                             |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   | https://                                                             |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      | https://                                                             |
| click-repl                    | https://github.com/untitaker/click-repl                                             | https://                                                             |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            | https://                                                             |
| cmake                         | https://cmake.org/                                                                  | https://                                                             |
| colorama                      | https://github.com/tartley/colorama                                                 | https://                                                             |
| comm                          | https://github.com/ipython/comm                                                     | https://                                                             |
| compose                       | https://github.com/docker/compose                                                   | https://                                                             |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        | https://                                                             |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      | https://                                                             |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     | https://                                                             |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            | https://                                                             |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           | https://                                                             |
| confuse                       | https://github.com/beetbox/confuse                                                  | https://                                                             |
| contourpy                     | https://github.com/contourpy/contourpy                                              | https://                                                             |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               | https://                                                             |
| cryptography                  | https://github.com/pyca/cryptography                                                | https://                                                             |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                                | https://                                                             |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           | https://                                                             |
| cupy-cuda113                  | https://cupy.dev/                                                                   | https://                                                             |
| curl                          | https://curl.se/                                                                    | https://                                                             |
| cycler                        | https://github.com/matplotlib/cycler                                                | https://                                                             |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             | https://                                                             |
| Cython                        | https://cython.org                                                                  | https://                                                             |
| d3                            | https://github.com/mbostock/d3                                                      | https://                                                             |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           | https://                                                             |
| ddsketch                      | http://github.com/datadog/sketches-py                                               | https://                                                             |
| debugpy                       | https://aka.ms/debugpy                                                              | https://                                                             |
| decimal                       | https://github.com/shopspring/decimal                                               | https://                                                             |
| decorator                     | https://github.com/micheles/decorator                                               | https://                                                             |
| deepdiff                      | https://github.com/seperman/deepdiff                                                | https://                                                             |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             | https://                                                             |
| Name of Project               | Website                                                                             | License                                                              |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 |                                                                      |
| dill                          | https://github.com/uqfoundation/dill                                                |                                                                      |
| distro                        | https://github.com/orionflores/distro                                               |                                                                      |
| Django                        | https://www.djangoproject.com/                                                      |                                                                      |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                    |                                                                      |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                   |                                                                      |
| django-csp                    | https://github.com/mozilla/django-csp                                               |                                                                      |
| django-extensions             | https://github.com/django-extensions/django-extensions                              |                                                                      |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                          |                                                                      |
| django-redis                  | https://github.com/jazzband/django-redis                                            |                                                                      |
| django-taggit                 | https://github.com/jazzband/django-taggit                                           |                                                                      |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                              |                                                                      |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                              |                                                                      |
| djangorestframework           | https://www.django-rest-framework.org/                                              |                                                                      |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                      |                                                                      |
| dm-tree                       | https://github.com/deepmind/tree                                                    |                                                                      |
| docker-py                     | https://github.com/docker/docker-py                                                 |                                                                      |
| docopt                        | https://docopt.org                                                                  |                                                                      |
| docutils                      | https://docutils.sourceforge.io                                                     |                                                                      |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                         |                                                                      |
| editdistance                  | https://github.com/roy-ht/editdistance                                              |                                                                      |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                               |                                                                      |
| einops                        | https://github.com/arogozhnikov/einops                                              |                                                                      |
| entrypoints                   | https://github.com/takluyver/entrypoints                                            |                                                                      |
| errors                        | https://github.com/pkg/errors                                                       |                                                                      |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                              |                                                                      |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                       |                                                                      |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         |                                                                      |
| executing                     | https://github.com/alexmojaki/executing                                             |                                                                      |
| expat                         | https://libexpat.github.io                                                          |                                                                      |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                   |                                                                      |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 |                                                                      |
| fftw                          | https://www.fftw.org                                                                |                                                                      |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              |                                                                      |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             |                                                                      |
| finufft                       | https://github.com/flatironinstitute/finufft                                        |                                                                      |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         |                                                                      |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               |                                                                      |
| flit-core                     | https://github.com/pypa/flit                                                        |                                                                      |
| FLTK                          | https://www.fltk.org/index.php                                                      |                                                                      |
| fmt                           | https://fmt.dev/latest/index.html                                                   |                                                                      |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         |                                                                      |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      |                                                                      |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       |                                                                      |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   |                                                                      |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            |                                                                      |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               |                                                                      |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             |                                                                      |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 |                                                                      |
| Name of Project               | Website                                                                             | License                                                              |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https://                                                             |
| freetype                      | https://freetype.org                                                                | https://                                                             |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https://                                                             |
| frozendict                    | <b>Orion Floes</b>                                                                  | https://                                                             |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                              | https://                                                             |
| fsmlite                       | https://github.com/tkem/fsmlite                                                     | https://                                                             |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                           | https://                                                             |
| funcy                         | https://github.com/Suor/funcy                                                       | https://                                                             |
| gast                          | https://github.com/serge-sans-paille/gast/                                          | https://                                                             |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                | https://                                                             |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             | https://                                                             |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https://                                                             |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             | https://                                                             |
| genproto                      | https://google.golang.org/genproto/googleapis                                       | https://                                                             |
| geometric                     | https://openbase.com/python/geometric                                               | https://                                                             |
| giflib                        | https://giflib.sourceforge.net                                                      | https://                                                             |
| glib                          | https://docs.gtk.org/glib/                                                          | https://                                                             |
| <b>GLM</b> Library            | https://github.com/g-truc/glm                                                       | https://                                                             |
| gls                           | https://github.com/jtolds/gls                                                       | https://                                                             |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https://                                                             |
| go-connections                | https://github.com/docker/go-connections                                            | https://                                                             |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https://                                                             |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https://                                                             |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https://                                                             |
| go-ini                        | https://github.com/go-ini/ini                                                       | https://                                                             |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             | https://                                                             |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https://                                                             |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           | https://                                                             |
| go-ole                        | https://github.com/go-ole/go-ole                                                    | https://                                                             |
| go-pg                         | https://github.com/go-pg/pg                                                         | https://                                                             |
| go-redis                      | https://github.com/go-redis/redis/v8                                                | https://                                                             |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                            | https://                                                             |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                            | https://                                                             |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                              | https://                                                             |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                                   | https://                                                             |
| go-units                      | https://github.com/docker/go-units                                                  | https://                                                             |
| go-version                    | https://github.com/hashicorp/go-version                                             | https://                                                             |
| go-zglob                      | https://github.com/mattn/go-zglob                                                   | https://                                                             |
| go.opencensus                 | https://go.opencensus.io                                                            | https://                                                             |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                | https://                                                             |
| goconvey                      | https://github.com/smartystreets/goconvey                                           | https://                                                             |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                       | https://                                                             |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       | https://                                                             |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https://                                                             |
| google-cloud-go               | https://cloud.google.com/go                                                         | https://                                                             |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 | https://                                                             |
| google-pasta                  | https://github.com/google/pasta                                                     | https://                                                             |
| google.golang.org/api         | https://google.golang.org/api                                                       | https://                                                             |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  | https://                                                             |
| Name of Project               | Website                                                                             | License                                                              |
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https://github.com/gorilla/websocket/blob/master/LICENSE             |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https://github.com/silnrsi/graphite/blob/master/COPYING              |
| graphviz                      | https://graphviz.org/                                                               | https://graphviz.org/license/                                        |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https://github.com/python-greenlet/greenlet/blob/master/LICENSE      |
| groupcache                    | https://github.com/golang/groupcache                                                | https://github.com/golang/groupcache/blob/master/LICENSE             |
| grpc                          | https://google.golang.org/grpc                                                      | https://github.com/grpc/grpc/blob/master/LICENSE                     |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https://github.com/grpc/grpc/blob/master/LICENSE                     |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https://github.com/grpc/grpc.io/blob/main/LICENSE                    |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  | https://gitlab.gnome.org/GNOME/gtk/-/blob/master/COPYING             |
| gts                           | https://sourceforge.net/projects/gts/                                               | https://sourceforge.net/p/gts/code/HEAD/tree/trunk/COPYING           |
| h5py                          | https://www.h5py.org                                                                | https://github.com/h5py/h5py/blob/master/LICENSE                     |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https://github.com/harfbuzz/harfbuzz/blob/main/COPYING               |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https://github.com/scikit-learn-contrib/hdbscan/blob/master/LICENSE  |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https://support.hdfgroup.org/ftp/HDF/releases/HDF4_2_15/src/COPYING  |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https://www.hdfgroup.org/HDF5/doc/Copyright.html                     |
| he                            | https://github.com/mathiasbynens/he                                                 | https://github.com/mathiasbynens/he/blob/master/LICENSE-MIT.txt      |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https://github.com/webpack-contrib/html-loader/blob/master/LICENSE   |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https://github.com/html5lib/html5lib-python/blob/master/LICENSE      |
| htslib                        | https://www.htslib.org                                                              | https://github.com/samtools/htslib/blob/develop/LICENSE              |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https://github.com/jmoiron/humanize/blob/master/LICENSE              |
| icu                           | https://github.com/unicode-org/icu                                                  | https://github.com/unicode-org/icu/blob/main/LICENSE                 |
| idna                          | https://github.com/kjd/idna                                                         | https://github.com/kjd/idna/blob/master/LICENSE.rst                  |
| imageio                       | https://github.com/imageio/imageio                                                  | https://github.com/imageio/imageio/blob/master/LICENSE               |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https://github.com/shibukawa/imagesize_py/blob/master/LICENSE        |
| <b>ImmuneBuilder</b>          | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https://github.com/oxpig/ImmuneBuilder/blob/main/LICENSE             |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https://github.com/python/importlib_metadata/blob/main/LICENSE       |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https://github.com/python/importlib_resources/blob/main/LICENSE      |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https://iupac.org/who-we-are/divisions/division-details/inchi/       |
| inflection                    | https://github.com/jinzhu/inflection                                                | https://github.com/jinzhu/inflection/blob/master/LICENSE             |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https://github.com/go-ini/ini/blob/master/LICENSE                    |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https://github.com/pytest-dev/iniconfig/blob/main/LICENSE            |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https://github.com/dnozay/innersvg-polyfill/blob/master/LICENSE      |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https://github.com/llvm/llvm-project/blob/main/openmp/LICENSE.txt    |
| ipykernel                     | https://ipython.org                                                                 | https://github.com/ipython/ipykernel/blob/main/LICENSE               |
| ipython                       | https://ipython.org                                                                 | https://github.com/ipython/ipython/blob/master/COPYING.md            |
| ipython-genutils              | http://ipython.org                                                                  | https://github.com/ipython/ipython_genutils/blob/master/LICENSE      |
| ipywidgets                    | http://jupyter.org                                                                  | https://github.com/jupyter-widgets/ipywidgets/blob/main/LICENSE      |
| isodate                       | https://github.com/gweis/isodate/                                                   | https://github.com/gweis/isodate/blob/master/LICENSE                 |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https://github.com/pallets/itsdangerous/blob/main/LICENSE.rst        |
| jax                           | https://github.com/google/jax                                                       | https://github.com/google/jax/blob/main/LICENSE                      |
| jaxlib                        | https://github.com/google/jax                                                       | https://github.com/google/jax/blob/main/LICENSE                      |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              | https://github.com/davidhalter/jedi/blob/master/LICENSE.txt          |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https://github.com/pallets/jinja/blob/main/LICENSE.rst               |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https://github.com/jmespath/jmespath.py/blob/develop/LICENSE.txt     |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https://github.com/joblib/joblib/blob/master/LICENSE.txt             |
| jpeg                          | https://www.ijg.org                                                                 | http://www.ijg.org/files/README                                      |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https://github.com/json5-json5/json5/blob/main/LICENSE.md            |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https://github.com/dmkoch/django-jsonfield/blob/master/LICENSE       |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https://github.com/stefankoegl/python-json-patch/blob/master/LICENSE |
| Name of Project               | Website                                                                             | License                                                              |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:                                                               |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https:                                                               |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https:                                                               |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:                                                               |
| jstat                         | https://github.com/jstat/jstat                                                      | https:                                                               |
| jupyter-client                | https://jupyter.org                                                                 | https:                                                               |
| jupyter-core                  | https://jupyter.org                                                                 | https:                                                               |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https:                                                               |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:                                                               |
| jupyter-server                | https://github.com/jupyter-server/jupyter_server                                    | https:                                                               |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:                                                               |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:                                                               |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:                                                               |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:                                                               |
| jupyter_client                | http://jupyter.org                                                                  | https:                                                               |
| jupyter_core                  | http://jupyter.org                                                                  | https:                                                               |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https:                                                               |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:                                                               |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:                                                               |
| keras                         | https://github.com/keras-team/keras                                                 | https:                                                               |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:                                                               |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:                                                               |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:                                                               |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:                                                               |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:                                                               |
| kombu                         | https://kombu.readthedocs.io                                                        | https:                                                               |
| krb5                          | https://web.mit.edu/kerberos/                                                       | https:                                                               |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:                                                               |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:                                                               |
| lcms2                         | https://www.littlecms.com                                                           | https:                                                               |
| lerc                          | https://github.com/Esri/lerc                                                        | https:                                                               |
| libarchive                    | http://www.libarchive.org                                                           | https:                                                               |
| libblas                       | https://www.netlib.org/blas/                                                        | https:                                                               |
| libbrotlicommon               | https://github.com/google/brotli                                                    |                                                                      |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:                                                               |
| libbrotlienc                  | https://github.com/google/brotli                                                    |                                                                      |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | https:                                                               |
| libclang                      | Orion Floes                                                                         | https:                                                               |
| libcurl                       | https://curl.se/libcurl/                                                            | https:                                                               |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:                                                               |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:                                                               |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:                                                               |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://                                                              |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:                                                               |
| libffi                        | https://github.com/libffi/libffi                                                    | https:                                                               |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:                                                               |
| libgd                         | https://libgd.github.io                                                             | https:                                                               |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:                                                               |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https:                                                               |
|                               |                                                                                     | J)                                                                   |
| Name of Project               | Website                                                                             | Licen                                                                |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https:/                                                              |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https:/                                                              |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https:/                                                              |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https:/                                                              |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https:/                                                              |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                              |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https:/                                                              |
| libopenblas                   | https://www.openblas.net/                                                           | https:/                                                              |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https:/                                                              |
| libpq                         | https://www.postgresql.org/                                                         | https:/                                                              |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https:/                                                              |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https:/                                                              |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https:/                                                              |
| libtiff                       | https://www.libtiff.org/                                                            | https:/                                                              |
| libtrust                      | https://github.com/docker/libtrust                                                  | https:/                                                              |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https:/                                                              |
| libuv                         | https://github.com/libuv/libuv                                                      | https:/                                                              |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https:/                                                              |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https:/                                                              |
| libxc                         | https://www.tddft.org/programs/libxc/                                               | https:/                                                              |
| libxcb                        | https://xcb.freedesktop.org                                                         | https:/                                                              |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https:/                                                              |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https:/                                                              |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https:/                                                              |
| libzlib                       | https://zlib.net                                                                    | https:/                                                              |
| lime                          | https://github.com/marcoter/lime                                                    | https:/                                                              |
| $\overline{\text{lit}}$       | http://llvm.org                                                                     | https:/                                                              |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https:/                                                              |
| <b>Ilymlite</b>               | http://llvmlite.readthedocs.io                                                      | https:/                                                              |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https:/                                                              |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https:/                                                              |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https:/                                                              |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/                                                              |
| lxml                          | https://lxml.de                                                                     | https:/                                                              |
| $1z4-c$                       | https://www.lz4.org/                                                                |                                                                      |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https:/<br>https:/                                                   |
| markdown-it-py                | <b>Orion Floes</b>                                                                  | https:/                                                              |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https:/                                                              |
| matplotlib                    | https://matplotlib.org                                                              | https:/                                                              |
| matplotlib-base               | https://matplotlib.org                                                              |                                                                      |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https:/                                                              |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/                                                              |
|                               |                                                                                     | https:/                                                              |
| mdtraj                        | https://www.mdtraj.org/<br><b>Orion Floes</b>                                       | https:/                                                              |
| mdurl                         |                                                                                     | https:/                                                              |
| menuinst                      | <b>Orion Floes</b>                                                                  | https:/                                                              |
| mergo                         | https://github.com/imdario/mergo                                                    | https:/                                                              |
| mistune                       | https://github.com/lepture/mistune                                                  | https:/                                                              |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https:/                                                              |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https:/                                                              |
|                               |                                                                                     | J.                                                                   |
| Name of Project               | Website                                                                             | Licen                                                                |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https:/                                                              |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https:/                                                              |
| ml-dtypes                     | <b>Orion Floes</b>                                                                  | https:/                                                              |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https:/                                                              |
| moment                        | https://github.com/moment/moment                                                    | https:/                                                              |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https:/                                                              |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https:/                                                              |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https:/                                                              |
| mpmath                        | http://mpmath.org/                                                                  | https:/                                                              |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https:/                                                              |
| msgpack                       | https://msgpack.org/                                                                | https:/                                                              |
| multidict                     | https://github.com/aio-libs/multidict                                               | https:/                                                              |
| multierr                      | https://go.uber.org/multierr                                                        | https:/                                                              |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https:/                                                              |
| munkres                       | https://software.clapper.org/munkres/                                               | https:/                                                              |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https:/                                                              |
| namex                         | <b>Orion Floes</b>                                                                  | https:/                                                              |
| nbclassic                     | http://jupyter.org                                                                  | https:/                                                              |
| nbclient                      | https://jupyter.org                                                                 | https:/                                                              |
| nbconvert                     | https://jupyter.org                                                                 | https:/                                                              |
| nbformat                      | http://jupyter.org                                                                  | https:/                                                              |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https:/                                                              |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https:/                                                              |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                              |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https:/                                                              |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https:/                                                              |
| networkx                      | https://networkx.org                                                                | https:/                                                              |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https:/                                                              |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             |                                                                      |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https:/<br>https:/                                                   |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       |                                                                      |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https:/                                                              |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/                                                              |
|                               | https://nodejs.org/en/                                                              | https:/                                                              |
| nodejs                        |                                                                                     | https:/                                                              |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https:/                                                              |
| notebook<br>notebook-shim     | http://jupyter.org<br>https://github.com/jupyter/notebook_shim                      | https:/                                                              |
|                               |                                                                                     | https:/                                                              |
| notebook_shim                 | http://jupyter.org                                                                  | https:/                                                              |
| numba                         | https://numba.pydata.org                                                            | https:/                                                              |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https:/                                                              |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https:/                                                              |
| numpy                         | https://numpy.org                                                                   | https:/                                                              |
| numpy-base                    | https://numpy.org                                                                   | https:/                                                              |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/                                                              |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| Name of Project               | Website                                                                             | License                                                              |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                              |
| Oat++                         | https://oatpp.io/                                                                   | https:/                                                              |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https:/                                                              |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https:/                                                              |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/                                                              |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https:/                                                              |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/                                                              |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/                                                              |
| OpenFF                        | https://openforcefield.org/                                                         | https:/                                                              |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/                                                              |
| openff-forcefields            | https://openforcefield.org                                                          | https:/                                                              |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https:/                                                              |
| openff-models                 | https://github.com/openforcefield/openff-models                                     | https:/                                                              |
| openff-toolkit                | https://openforcefield.org                                                          | https:/                                                              |
| openff-toolkit-base           | https://openforcefield.org                                                          | https:/                                                              |
| openff-units                  | https://github.com/openforcefield/openff-units                                      | https:/                                                              |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https:/                                                              |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https:/                                                              |
| openldap                      | https://www.openldap.org/software/repo.html                                         | https:/                                                              |
| OpenMM                        | https://openmm.org                                                                  | https:/                                                              |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https:/                                                              |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https:/                                                              |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                                              |
| openssl                       | https://www.openssl.org                                                             | https:/                                                              |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https:/                                                              |
| OptKing                       | https://github.com/psi-rking/optking                                                | https:/                                                              |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https:/                                                              |
| overrides                     | https://github.com/mkorpela/overrides                                               | https:/                                                              |
| packaging                     | https://github.com/pypa/packaging                                                   | https:/                                                              |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                                              |
| pandas                        | https://pandas.pydata.org                                                           | https:/                                                              |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https:/                                                              |
|                               |                                                                                     |                                                                      |
| Name of Project               | Website                                                                             | Licen                                                                |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https:/                                                              |
| pango                         | https://pango.gnome.org                                                             | https:/                                                              |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https:/                                                              |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                              |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https:/                                                              |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https:/                                                              |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https:/                                                              |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https:/                                                              |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https:/                                                              |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/                                                              |
| pcre                          | https://www.pcre.org                                                                | https:/                                                              |
| pcre2                         | https://www.pcre.org                                                                | https:/                                                              |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https:/                                                              |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https:/                                                              |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https:/                                                              |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https:/                                                              |
| pgio                          | https://github.com/jackc/pgio                                                       | https:/                                                              |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https:/                                                              |
| $pgproto\overline{3}$         | https://github.com/jackc/pgproto3/v2                                                | https:/                                                              |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https:/                                                              |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https:/                                                              |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https:/                                                              |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https:/                                                              |
| Pillow                        | https://python-pillow.org                                                           | https:/                                                              |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https:/                                                              |
| pip                           | https://pip.pypa.io/                                                                | https:/                                                              |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https:/                                                              |
| pixman                        | https://pixman.org                                                                  | https:/                                                              |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https:/                                                              |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https:/                                                              |
| plotly                        | https://plotly.com/python/                                                          | https:/                                                              |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https:/                                                              |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https:/                                                              |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/                                                              |
| pooch                         | https://github.com/fatiando/pooch                                                   | https:/                                                              |
| pox                           | https://github.com/uqfoundation/pox                                                 | https:/                                                              |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https:/                                                              |
| pq                            | https://github.com/lib/pq                                                           | https:/                                                              |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https:/                                                              |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https:/                                                              |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/                                                              |
| protobuf                      | https://google.golang.org/protobuf                                                  | https:/                                                              |
| psi4                          | https://psicode.org                                                                 | https:/                                                              |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https:/                                                              |
| psycopg2                      | https://psycopg.org/                                                                | https:/                                                              |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https:/                                                              |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         |                                                                      |
|                               | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/                                                              |
| ptyprocess<br>pure-eval       | http://github.com/alexmojaki/pure_eval                                              | https:/                                                              |
|                               |                                                                                     | http://                                                              |
| Name of Project               | Website                                                                             | License                                                              |
| py                            | https://py.readthedocs.io/en/latest/                                                | https:/                                                              |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             | https:/                                                              |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   | https:/                                                              |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           | https:/                                                              |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  | https:/                                                              |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/                                                              |
| pycosat                       | https://github.com/conda/pycosat                                                    | https:/                                                              |
| pycparser                     | https://github.com/eliben/pycparser                                                 | https:/                                                              |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 | https:/                                                              |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           | https:/                                                              |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                | https:/                                                              |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                | https:/                                                              |
| Pygments                      | https://pygments.org                                                                | https:/                                                              |
| pygraphviz                    | https://pygraphviz.github.io                                                        | https:/                                                              |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            | https:/                                                              |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        | https:/                                                              |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  | https:/                                                              |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   | https:/                                                              |
| pymbar                        | https://pymbar.org                                                                  | https:/                                                              |
| pyOpenSSL                     | https://pyopenssl.org/                                                              | https:/                                                              |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/                                                              |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    | https:/                                                              |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 | https:/                                                              |
| pysam                         | https://github.com/pysam-developers/pysam                                           | https:/                                                              |
| PySocks                       | https://github.com/Anorov/PySocks                                                   | https:/                                                              |
| pytables                      | https://www.pytables.org                                                            | https:/                                                              |
| python                        | https://www.python.org/                                                             | https:/                                                              |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          | https:/                                                              |
| python-constraint             | https://github.com/python-constraint/python-constraint                              | https:/                                                              |
| python-dateutil               | https://dateutil.readthedocs.io                                                     | https:/                                                              |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         | https:/                                                              |
| python-ldap                   | https://www.python-ldap.org/                                                        | https:/                                                              |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            | https:/                                                              |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 | https:/                                                              |
| pytz                          | https://pythonhosted.org/pytz                                                       | https:/                                                              |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/                                                              |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  | https:/                                                              |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                 | https:/                                                              |
| pyyaml                        | No longer available                                                                 | No lor                                                               |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             | https:/                                                              |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               | https:/                                                              |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  | https:/                                                              |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        | https:/                                                              |
| ramda                         | https://github.com/ramda/ramda                                                      | https:/                                                              |
| rapidjson                     | https://rapidjson.org/                                                              | https:/                                                              |
| rdkit                         | https://www.rdkit.org                                                               | https:/                                                              |
| re2                           | https://github.com/google/re2                                                       | https:/                                                              |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             | https:/                                                              |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             | https:/                                                              |
|                               |                                                                                     | J)                                                                   |
| Name of Project               | Website                                                                             | Licen                                                                |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https:/                                                              |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https:/                                                              |
| reportlab                     | https://www.reportlab.com                                                           | https:/                                                              |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                              |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                              |
| requests                      | https://requests.readthedocs.io                                                     | https:/                                                              |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https:/                                                              |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https:/                                                              |
| resumable                     | https://github.com/stevvooe/resumable                                               | https:/                                                              |
| retrying                      | https://github.com/rholder/retrying                                                 | https:/                                                              |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https:/                                                              |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https:/                                                              |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https:/                                                              |
| rich                          | <b>Orion Floes</b>                                                                  | https:/                                                              |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https:/                                                              |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https:/                                                              |
| rsa                           | https://stuvel.eu/rsa                                                               | https:/                                                              |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/                                                              |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/                                                              |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https:/                                                              |
| sasl                          | https://mellium.im/sasl                                                             | https:/                                                              |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https:/                                                              |
| scikit-image                  | https://scikit-image.org                                                            | https:/                                                              |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https:/                                                              |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/                                                              |
| scipy                         | https://scipy.org                                                                   | https:/                                                              |
| seaborn                       | https://seaborn.pydata.org                                                          | https:/                                                              |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https:/                                                              |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https:/                                                              |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https:/                                                              |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https:/                                                              |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https:/                                                              |
| sh                            | https://github.com/amoffat/sh                                                       | https:/                                                              |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https:/                                                              |
| simint                        |                                                                                     |                                                                      |
| six                           | https://www.bennyp.org/research/simint/<br>https://github.com/benjaminp/six         | https:/                                                              |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https:/                                                              |
|                               | https://github.com/google/snappy                                                    | https:/                                                              |
| snappy                        | https://github.com/python-trio/sniffio                                              | https:/                                                              |
| sniffio                       |                                                                                     | https:/                                                              |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https:/                                                              |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https:/                                                              |
| spglib                        | <b>Orion Floes</b>                                                                  | https:/                                                              |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https:/                                                              |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/                                                              |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/                                                              |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/                                                              |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/                                                              |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/                                                              |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/                                                              |
| Name of Project               | Website                                                                             | License                                                              |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          | https:/                                                              |
| sqlite                        | https://sqlite.org/index.html                                                       | https:/                                                              |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            | https:/                                                              |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             | https:/                                                              |
| starfile                      | https://github.com/alisterburt/starfile                                             | https:/                                                              |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          | https:/                                                              |
| structlog                     | https://www.structlog.org/                                                          | https:/                                                              |
| svglib                        | https://github.com/deeplook/svglib                                                  | https:/                                                              |
| sympy                         | https://sympy.org                                                                   | https:/                                                              |
| tables                        | https://www.pytables.org/                                                           | https:/                                                              |
| tabulate                      | https://github.com/astanin/python-tabulate                                          | https:/                                                              |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                | https:/                                                              |
| tenacity                      | https://github.com/jd/tenacity                                                      | https:/                                                              |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           | https:/                                                              |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           | https:/                                                              |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           | https:/                                                              |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            | https:/                                                              |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             | https:/                                                              |
| tensorflow-io-gcs-filesystem  | <b>Orion Floes</b>                                                                  | https:/                                                              |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           | https:/                                                              |
| termcolor                     | https://github.com/hugovk/termcolor                                                 | https:/                                                              |
| terminado                     | https://github.com/jupyter/terminado                                                | https:/                                                              |
| testpath                      | https://github.com/jupyter/testpath                                                 | https:/                                                              |
| textangular                   | https://github.com/fraywing/textAngular                                             | https:/                                                              |
| tf_keras                      | <b>Orion Floes</b>                                                                  | https:/                                                              |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             | https:/                                                              |
| three                         | https://github.com/mrdoob/three.js                                                  | https:/                                                              |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                | https:/                                                              |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  | https:/                                                              |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             | https:/                                                              |
| tk                            | https://www.tcl.tk/                                                                 | https:/                                                              |
| toml                          | https://github.com/toml-lang/toml                                                   | https:/                                                              |
| tomli                         | https://github.com/hukkin/tomli                                                     | https:/                                                              |
| toolz                         | https://github.com/pytoolz/toolz                                                    | https:/                                                              |
| torch                         | https://pytorch.org/                                                                | https:/                                                              |
| tornado                       | https://www.tornadoweb.org                                                          | https:/                                                              |
| tqdm                          | https://github.com/tqdm/tqdm                                                        | https:/                                                              |
| tracy                         | https://github.com/gear-genomics/tracy                                              | https:/                                                              |
| traitlets                     | https://github.com/ipython/traitlets                                                | https:/                                                              |
| triton                        | https://github.com/openai/triton/                                                   | https:/                                                              |
| truststore                    | <b>Orion Floes</b>                                                                  | https:/                                                              |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               | https:/                                                              |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             | https:/                                                              |
| twine                         | https://github.com/pypa/twine                                                       | https:/                                                              |
| twinj uuid                    | https://github.com/twinj/uuid                                                       | https:/                                                              |
| types                         | https://github.com/babel/babel                                                      | https:/                                                              |
| typescript                    | https://github.com/Microsoft/TypeScript                                             | https:/                                                              |
| typing_extensions             | https://github.com/python/typing                                                    | https:/                                                              |
| tzdata                        | https://github.com/python/tzdata                                                    | https:/                                                              |
| Name of Project               | Website                                                                             | License                                                              |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | MIT                                                                  |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | MIT                                                                  |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | MIT                                                                  |
| uritools                      | https://github.com/tkem/uritools/                                                   | MIT                                                                  |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | MIT                                                                  |
| vine                          | https://github.com/celery/vine                                                      | BSD-3-Clause                                                         |
| vue                           | https://github.com/vuejs/vue                                                        | MIT                                                                  |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | MIT                                                                  |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | BSD                                                                  |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | Apache-2.0                                                           |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | BSD-3-Clause                                                         |
| westpa                        | Orion Floes                                                                         | MIT                                                                  |
| wheel                         | https://github.com/pypa/wheel                                                       | MIT                                                                  |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | BSD-3-Clause                                                         |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | BSD-2-Clause                                                         |
| wsutil                        | https://github.com/yhat/wsutil                                                      | MIT                                                                  |
| x/lint                        | https://golang.org/x/lint                                                           | BSD-3-Clause                                                         |
| x/mod                         | https://golang.org/x/mod/semver                                                     | BSD-3-Clause                                                         |
| x/net                         | https://golang.org/x/net                                                            | BSD-3-Clause                                                         |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | BSD-3-Clause                                                         |
| x/sys                         | https://golang.org/x/sys                                                            | BSD-3-Clause                                                         |
| x/text                        | https://golang.org/x/text                                                           | BSD-3-Clause                                                         |
| x/tools                       | https://golang.org/x/tools                                                          | BSD-3-Clause                                                         |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | BSD-3-Clause                                                         |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                               | Apache-2.0                                                           |
| xlrd                          | https://github.com/python-excel/xlrd                                                | BSD-3-Clause                                                         |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | MIT                                                                  |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | MIT                                                                  |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | MIT                                                                  |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | MIT                                                                  |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | MIT                                                                  |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | MIT                                                                  |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | MIT                                                                  |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | MIT                                                                  |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | MIT                                                                  |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | MIT                                                                  |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | MIT                                                                  |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | MIT                                                                  |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | MIT                                                                  |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | MIT                                                                  |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | MIT                                                                  |
| xz                            | https://github.com/ulikunitz/xz                                                     | MIT                                                                  |
| yaml                          | https://pyyaml.org/                                                                 | MIT                                                                  |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  | MIT                                                                  |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | Apache-2.0                                                           |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | Apache-2.0                                                           |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | MIT                                                                  |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | MIT                                                                  |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | Commercial                                                           |
| Name of Project               | Website                                                                             | License                                                              |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                                                                  |
| zap                           | https://go.uber.org/zap                                                             | https://                                                             |
| zipp                          | https://github.com/jaraco/zipp                                                      | https://                                                             |
| zlib                          | https://zlib.net/                                                                   | https://                                                             |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https://                                                             |
| zstd                          | https://facebook.github.io/zstd/                                                    | https://                                                             |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https://                                                             |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https://                                                             |

# **10.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses GNU Project.

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

## See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# A

AddFlexibleResidue OESz:: OESzybkiProteinOptions, 26

# B

bound entropy.py Example Code, 126

# C

```
Clear
   OESz:: OESzybkiResults, 29
ClearFixAtoms
   OESz:: OESzybki, 11
ClearFlexibleResidues
   OESz:: OESzybkiProteinOptions, 26
ClearHarmonicConstraints
   OESz:: OESzybki, 12
ClearTorsionConstraint
   OESz:: OESzybki, 12
Constructor
   OESz:: OEFixedProteinLigandOptimizer,
       91
   OESz:: OEFlexProteinLigandOptimizer,
       92
   OESz:: OEProteinFlexOptions, 35
   OESz:: OEProteinLigandOptOptions, 36
   OESz:: OETorsionScanner, 62
Constructors
   OESz:: OEBoundEntropyOptions, 63
   OESz:: OEEntropyResults, 66
   OESz:: OEFreeFormConf, 41
   OESz:: OEFreeFormConfAdvanced, 42
   OESz:: OEFreeFormConfOptions, 44
   OESz:: OEFreeFormConfResults, 55
   OESz:: OEFreeFormSolvOptions, 48
   OESz:: OEFreeFormSolvResults, 50
   OESz:: OELigandEntropyOptions, 65
   OESz:: OEProteinLigandOptResults, 39
   OESz:: OERestrictionEnergyResult, 52
   OESz:: OESingleConfResult, 52
   OESz:: OESzybki, 11
   OESz:: OESzybkiEnsembleResults, 33
```

```
OESz:: OESzybkiGeneralOptions, 17
OESz:: OESzybkiOptions, 15
OESz:: OESzybkiOptOptions, 21
OESz:: OESzybkiProteinOptions, 25
OESz:: OESzybkiResults, 28
OESz:: OESzybkiSolventOptions, 23
OESz:: OETorsionScanOptions, 56
OESz:: OETorsionScanResult, 61
```

# F

Energy OESz:: OEFixedProteinLigandOptimizer, 92 OESz:: OEFlexProteinLigandOptimizer, 93 EstimateEnergies OESz:: OEFreeFormConfAdvanced, 42 EstimateFreeEnergies OESz:: OEFreeFormConf, 41 EstimateRestrictionEnergy OESz:: OEFreeFormConfAdvanced, 42 Example Code bound\_entropy.py, 126 findsimilarconfs.py, 136 flex\_residues.py, 115 flexible\_protein.py, 112 freeformconf.py, 128 freeformconfadvanced.py, 131 freeformconfadvrstr.py, 133 freeformconfrstr.py, 130 freeformsolv.py, 127 ligand\_entropy.py, 125 ligand\_flexprotein\_newton.py, 120 ligand\_multiple\_options.py, 102 optimizedu.py, 123 optimizeligandindu.py, 121 protein\_ligand\_pb.py, 118 protein\_multiple\_options.py, 109 simple\_conformer.py, 106 simple\_newton.py, 105 simple\_protein.py, 107 simple\_smirnoff.py, 100

simple vacuum.pv.99 torsionscan.py, 137

# F

FindSimilarConfs OESz:: OEFreeFormConf, 41 findsimilarconfs.py Example Code, 136 FixAtoms OESz:: OESzybki, 12 flex residues.py Example Code, 115 flexible\_protein.py Example Code, 112 freeformconf.py Example Code, 128 freeformconfadvanced.py Example Code, 131 freeformconfadvrstr.py Example Code, 133 freeformconfrstr.py Example Code, 130 freeformsolv.py Example Code, 127

# G

GetAngle OESz:: OETorsionScanResult. 61 GetAtomicPotentials OESz:: OEFreeFormSolvResults, 51 GetAtomicRadiiType OESz:: OEFreeFormSolvOptions, 48 OESz:: OESzybkiSolventOptions, 23 GetCalculateFrozenTerms OESz:: OESzybkiOptOptions, 21 GetCalculateGradients OESz:: OESzybkiGeneralOptions, 18 GetCavitySolventParameter OESz:: OESzybkiSolventOptions, 23 GetChargeType OESz:: OEFreeFormSolvOptions, 48 OESz:: OESzybkiEnsembleResults, 34 GetConfFreeEnergyFromEnsemble OESz:: OESzybkiResults, 31 GetConfGenRMS OESz:: OEFreeFormSolvOptions, 48 GetConfIdx OESz:: OESingleConfResult, 53 OESz:: OESzybkiResults, 29 GetConfigurationalEntropy OESz:: OEEntropyResults, 67 OESz:: OESzybkiEnsembleResults, 34 GetConfResult OESz:: OEFreeFormConfResults, 55

GetCorrSolventOptions OESz:: OEFreeFormConfOptions, 44 GetCPUTime OESz:: OESzybkiResults, 29 GetDelta OESz:: OETorsionScanOptions, 57 GetDeltaG OESz:: OESingleConfResult, 53 GetElectrostaticSolvationFreeEnergy OESz:: OEFreeFormSolvResults, 51 GetEnergy OESz:: OETorsionScanResult, 61 GetEnergyTerm OESz:: OESzybkiResults, 29 GetEnsembleLigPartialSolvEntropy OESz:: OESzybkiEnsembleResults, 34 GetEnsembleLigSolvEntropy OESz:: OESzybkiEnsembleResults, 34 GetEnsembleProtDesolvEntropy OESz:: OESzybkiEnsembleResults, 35 GetEntropicEnergy OESz:: OESzybkiEnsembleResults, 34 GetEntropy OESz:: OESzybki, 12 GetEntropy (const OEChem:: OEMCMolBase&, unsigned int, unsigned int) OESz:: OESzybki, 12 GetEnvironment OESz:: OELigandEntropyOptions, 65 GetExactVdWProteinLigand OESz:: OESzybkiProteinOptions, 26 GetFinalEnergies OESz:: OEProteinLigandOptResults, 40 GetFinalRMSGradient OESz:: OESzybkiResults, 29 GetFinalTotalPotential OESz:: OESzybkiResults, 29 GetFixPattern OESz:: OESzybki, 13 GetFixPredicate OESz:: OESzybki, 13 GetFlexRange OESz:: OEProteinFlexOptions, 36 GetForceField OESz:: OEBoundEntropyOptions, 64 OESz:: OELigandEntropyOptions, 65 OESz:: OEProteinLigandOptOptions, 37 OESz:: OESzybkiGeneralOptions, 18 OESz:: OETorsionScanOptions, 57 GetForceFieldType OESz:: OESzybkiGeneralOptions, 18 OESz:: OETorsionScanOptions, 57 GetGeneralOptions OESz:: OESzybkiOptions, 16

GetGlobalStrain OESz:: OERestrictionEnergyResult, 52 GetGradients OESz:: OESzybkiResults, 29 GetGradTolerance OESz:: OEProteinLigandOptOptions, 37 OESz:: OESzybkiOptOptions, 22 GetHarmonicConstraints OESz:: OESzybki, 13 GetHydrophobicSolvationFreeEnergy OESz:: OEFreeFormSolvResults, 51 GetIEFFCluster OESz:: OESzybkiGeneralOptions, 18 GetInitialEnergies OESz:: OEProteinLigandOptResults, 40 GetInitialRMSGradient OESz:: OESzybkiResults, 30 GetInitialTotalPotential OESz:: OESzybkiResults, 30 GetInterEnergy OESz:: OESzybkiResults, 30 GetIntermolecularVdWCutoff OESz:: OESzybkiProteinOptions, 26 GetIntramolecularLigandEnergy OESz:: OESzybkiResults, 30 GetIntramolecularVdWCutoff OESz:: OESzybkiGeneralOptions, 18 GetIonicState OESz:: OEFreeFormConfOptions, 44 OESz:: OEFreeFormSolvOptions, 48 GetLigandCharge OESz:: OEBoundEntropyOptions, 64 OESz:: OELigandEntropyOptions, 65 OESz:: OEProteinLigandOptOptions, 37 GetLigandRMSD OESz:: OEProteinLigandOptResults, 40 GetLigandRMSDHeavy OESz:: OESzybkiGeneralOptions, 18 GetLnQrot OESz:: OESzybkiResults, 32 GetLnQrotational OESz:: OESingleConfResult, 53 GetLnQvib OESz:: OESzybkiResults, 32 GetLnQvibrational OESz:: OESingleConfResult, 53 GetLocalStrain OESz:: OERestrictionEnergyResult, 52 GetLowestdGConfIdx OESz:: OEFreeFormConfResults, 55 GetLowestEneResults OESz:: OETorsionScanner, 63 GetLowestEnergyConfs OESz:: OETorsionScanner, 63

GetLowestRelEneConfIdx OESz:: OEFreeFormConfResults, 55 GetMaxConfGen OESz:: OEFreeFormSolvOptions, 48 GetMaxDisplacement OESz:: OESzybkiResults, 30 GetMaxIter OESz:: OEProteinLigandOptOptions, 37 OESz:: OESzybkiOptOptions, 22 OESz:: OETorsionScanOptions, 57 GetMMFFEnergy OESz:: OESingleConfResult, 53 GetNonBondCutoff OESz:: OEProteinLigandOptOptions, 37 GetNumCycles OESz:: OESzybkiResults, 30 GetNumFixAtoms OESz:: OESzybkiResults, 30 GetNumRotors OESz:: OESzybkiResults, 31 GetNumStarts OESz:: OETorsionScanOptions, 58 GetNumUniqueConfs OESz:: OEFreeFormConfResults, 55 GetOmegaOptions OESz:: OEFreeFormConfOptions, 45 GetOptimizationType OESz:: OEProteinLigandOptOptions, 37 GetOptimizeOptions OESz:: OEFreeFormConfOptions, 45 GetOptimizerType OESz:: OESzybkiOptOptions, 22 GetOptOptions OESz:: OESzybkiOptions, 16 GetOverlapDiv OESz:: OETorsionScanOptions, 58 GetPenaltyForceConstant OESz:: OETorsionScanOptions, 57 GetPreOptimizeOptions OESz:: OEFreeFormConfOptions, 45 GetProbability OESz:: OESingleConfResult, 53 GetProtein OESz:: OESzybki, 13 GetProteinDielectric OESz:: OESzybkiProteinOptions, 26 GetProteinElectrostaticModel OESz:: OESzybkiProteinOptions, 26 GetProteinFlexibilityRange OESz:: OESzybkiProteinOptions, 27 GetProteinFlexibilityType OESz:: OESzybkiProteinOptions, 27 GetProteinOptions OESz:: OESzybkiOptions, 16

GetProteinRMSD OESz:: OEProteinLigandOptResults, 40 OESz:: OESzybkiResults, 31 GetRelativeEnergy OESz:: OESingleConfResult, 54 GetRelLnQ OESz:: OESingleConfResult, 54 GetRemoveAttractiveVdWForces OESz:: OESzybkiGeneralOptions, 19 GetRemoveCoulombTerms OESz:: OESzybkiGeneralOptions, 19 GetResidueID OESz:: OEProteinFlexOptions, 36 GetResultsForConformations OESz:: OEFreeFormConfResults, 56 OESz:: OESzybkiEnsembleResults, 35 GetReturnCode OESz:: OEFreeFormSolvResults, 51 OESz:: OEProteinLigandOptResults, 40 GetRMSD OESz:: OESzybkiResults, 31 GetRotationalEntropy OESz:: OESingleConfResult, 54 GetRotEntropy OESz:: OESzybkiResults, 32 GetRunType OESz:: OESzybkiOptions, 16 GetSaltConcentration OESz:: OESzybkiSolventOptions, 23 GetScannedAngles OESz:: OETorsionScanner, 63 GetSheffieldParameters OESz:: OESzybki, 13 GetSinglePointConfs OESz:: OETorsionScanner, 63 GetSoluteDielectric OESz:: OESzybkiGeneralOptions, 19 GetSolvationEntropy OESz:: OEEntropyResults, 67 GetSolvationFreeEnergy OESz:: OEFreeFormSolvResults, 51 GetSolvationType OESz:: OETorsionScanOptions, 58 GetSolvEnergy OESz:: OESingleConfResult, 54 GetSolventDielectric OESz:: OESzybkiSolventOptions, 24 GetSolventModel OESz:: OEProteinLigandOptOptions, 38 OESz:: OESzybkiSolventOptions, 24 GetSolventOptions OESz:: OEFreeFormConfOptions, 45 OESz:: OESzybkiOptions, 16 GetSzybkiGeneralOptions

OESz:: OEFreeFormConfOptions, 45 GetTemperature OESz:: OEFreeFormConfResults, 56 OESz:: OESzybkiEnsembleResults, 33 OESz:: OESzybkiGeneralOptions, 19 GetTolerance OESz:: OETorsionScanOptions, 57 GetTotalEnergy OESz:: OESingleConfResult, 54 OESz:: OESzybkiResults, 31 GetTotalEnergyWithHarmConstraint OESz:: OESzybkiResults, 31 GetTotalEntropy OESz:: OEFreeFormConfResults, 56 OESz:: OESzybkiEnsembleResults, 34 GetTotalEntropy in J/(mol K). OESz:: OEEntropyResults, 66 GetTotalRMSD OESz:: OEProteinLigandOptResults, 40 GetTranslationalEntropy OESz:: OEEntropyResults, 67 GetUseInput3D OESz:: OEFreeFormSolvOptions, 49 GetUseInputEnsemble OESz:: OEFreeFormConfOptions, 45 OESz:: OEFreeFormSolvOptions, 49 GetUseInternalCoord OESz:: OETorsionScanOptions, 58 GetUserDefinedAngles OESz:: OETorsionScanOptions, 58 GetUseSinglePointPB OESz:: OETorsionScanOptions, 58 GetUseSolventCorr OESz:: OEFreeFormConfOptions, 46 GetVerbose OESz:: OESzybkiGeneralOptions, 19 GetVibEntropy OESz:: OESzybkiResults, 32 GetVibrationalEntropy OESz:: OESingleConfResult, 54 GetVibrationalRotationalEntropy OESz:: OEEntropyResults, 67 GetWarnings OESz:: OEFreeFormSolvResults, 51

# H

HasEntropy OESz:: OESzybkiEnsembleResults, 35 HasFlexibleResidues OESz:: OESzybkiProteinOptions, 27

# $\mathsf{I}$

IdentifyConformer OESz:: OEFreeFormConfAdvanced, 42

IsActiveTerm OESz:: OESzybkiResults, 31 IsUnique OESz:: OESzybkiResults, 32

# T.

```
ligand_entropy.py
   Example Code, 125
ligand_flexprotein_newton.py
   Example Code, 120
ligand_multiple_options.py
   Example Code, 102
LoadPotentialGrid
   OESz:: OESzybki, 14
```

# N

NumConfs OESz:: OESzybkiEnsembleResults, 33

# O

```
OESz:: OEAtomicRadii, 80
OESz:: OEAtomicRadii:: Bondi, 80
OESz:: OEAtomicRadii:: ZAP7, 80
OESz:: OEAtomicRadii:: ZAP9, 80
OESz:: OEBoundEntropyOptions, 63
   Constructors, 63
   GetForceField, 64
   GetLigandCharge, 64
   operator=, 64
   SetForceField, 64
   SetLigandCharge, 64
OESz:: OEBoundLigandEntropy, 88
OESz:: OEComplexFFType, 94
OESz:: OEComplexFFType::FF14SB_PARSLEY,
       94
OESz:: OEComplexFFType:: FF14SB_SAGE, 94
OESz:: OEComplexFFType:: MMFF94, 94
OESz:: OEComplexFFType:: MMFF94S, 94
OESz:: OEComplexFFType:: MMFF_AMBER, 94
OESz:: OEComplexFFType:: MMFFS_AMBER, 94
OESz:: OEEntropyMethod, 67
OESz:: OEEntropyMethod:: Analytic, 68
OESz:: OEEntropyMethod:: ExternalHessian,
       68
OESz:: OEEntropyMethod:: QNewton, 67
OESz:: OEEntropyResults, 66
   Constructors, 66
   GetConfigurationalEntropy, 67
   GetSolvationEntropy, 67
   GetTotalEntropy in J/(mol K)., 66
   GetTranslationalEntropy, 67
   GetVibrationalRotationalEntropy, 67
   operator=, 66
   SetResults, 67
```

OESz:: OEEnvType, 68 OESz:: OEEnvType:: Gas, 68 OESz:: OEEnvType:: Protein, 68 OESz:: OEEnvType:: Solution, 68 OESz:: OEEnvType:: SolutionSA, 68 OESz:: OEEnvType:: SolutionSPT, 68 OESz:: OEEstimateConfFreeEnergies, 85 OESz:: OEEstimateSolvFreeEnergy, 85 OESz:: OEFixedProteinLigandOptimizer, 91 Constructor, 91 Energy, 92 operator=, 91 Optimize, 92 SetProtein, 92 OESz:: OEFlexProteinLigandOptimizer, 92 Constructor, 92 Energy, 93 operator=, 93 Optimize, 93 OESz:: OEForceFieldType, 69 OESz::OEForceFieldType::FF14SB\_SMIRNOFF, 71 OESz:: OEForceFieldType:: MMFF94, 69 OESz:: OEForceFieldType:: MMFF94S, 69 OESz:: OEForceFieldType:: MMFF\_AMBER, 69 OESz:: OEForceFieldType:: MMFF\_IEFF, 69 OESz:: OEForceFieldType:: MMFFS\_AMBER, 69 OESz:: OEForceFieldType:: MMFFS\_IEFF, 69 OESz::OEForceFieldType::PARSLEY\_OPENFF, 70 OESz::OEForceFieldType::PARSLEY\_OPENFF100, 70 OESz::OEForceFieldType::PARSLEY\_OPENFF111, 70 OESz:: OEForceFieldType:: PARSLEY OPENFF121, 70 OESz:: OEForceFieldType:: PARSLEY OPENFF131, 70 OESz:: OEForceFieldType:: SAGE\_OPENFF, 71 OESz::OEForceFieldType::SAGE\_OPENFF200, 70 OESz::OEForceFieldType::SAGE\_OPENFF210, 70 OESz::OEForceFieldType::SMIRNOFF99FROSST, 70 OESz:: OEFreeFormConf, 40 Constructors, 41 EstimateFreeEnergies, 41 FindSimilarConfs, 41 operator=, 41 OESz:: OEFreeFormConfAdvanced, 42 Constructors, 42 EstimateEnergies, 42 EstimateRestrictionEnergy, 42

IdentifyConformer. 42 OESz:: OEFreeFormReturnCode:: ConfGenFailure, operator=, 42 83 Optimize, 43 OESz:: OEFreeFormReturnCode:: GraphMismatch, OptimizeRestraint, 43 84 PreOptimizeEnsemble, 43 OESz:: OEFreeFormReturnCode:: ImplicitHydrogens, PrepareEnsemble, 43 82 RemoveDuplicates, 44 OESz:: OEFreeFormReturnCode:: InputGeometry, OESz:: OEFreeFormConfOptions, 44 82 Constructors, 44 OESz:: OEFreeFormReturnCode:: MissingFFConfEne, GetCorrSolventOptions, 44 84 GetIonicState, 44 OESz:: OEFreeFormReturnCode:: MissingPartnerConf, GetOmegaOptions, 45 84 GetOptimizeOptions, 45 OESz:: OEFreeFormReturnCode:: No3DCoordinates, GetPreOptimizeOptions, 45 83 GetSolventOptions, 45 OESz:: OEFreeFormReturnCode:: NotSupportedCharges, GetSzybkiGeneralOptions, 45 83 GetUseInputEnsemble, 45 OESz:: OEFreeFormReturnCode:: PartnerConfNotFound, GetUseSolventCorr, 46  $84$ operator=, 44 OESz:: OEFreeFormReturnCode:: Success, 82 SetCorrSolventOptions, 46 OESz:: OEFreeFormReturnCode:: TooManyRotors, SetIonicState, 46  $83$ SetOmegaOptions, 46 OESz:: OEFreeFormReturnCode:: UnequalNumConfs, SetOptimizeOptions, 46  $84$ SetPreOptimizeOptions, 47 OESz:: OEFreeFormReturnCode:: UnrecognizedChargeState SetSolventOptions, 47 83 SetSzybkiGeneralOptions, 47 OESz:: OEFreeFormReturnCode:: UnsupportedRadiiType, SetUseInputEnsemble, 47 83 SetUseSolventCorr, 47 OESz:: OEFreeFormSolvOptions, 47 OESz:: OEFreeFormConfResults, 55 Constructors, 48 Constructors, 55 GetAtomicRadiiType, 48 GetConfResult, 55 GetChargeType, 48 GetLowestdGConfIdx.55 GetConfGenRMS, 48 GetLowestRelEneConfIdx, 55 GetIonicState, 48 GetNumUniqueConfs, 55 GetMaxConfGen, 48 GetResultsForConformations, 56 GetUseInput3D, 49 GetTemperature, 56 GetUseInputEnsemble, 49 GetTotalEntropy, 56 operator= $,48$ operator=, 55 SetAtomicRadiiType, 49 PrintCsv, 56 SetChargeType, 49 PrintTxt, 56 SetConfGenRMS, 49 OESz:: OEFreeFormIonicState, 81 SetIonicState, 49 OESz:: OEFreeFormIonicState:: Default, 82 SetMaxConfGen, 50 OESz:: OEFreeFormIonicState:: Input, 82 SetUseInput3D, 50 OESz:: OEFreeFormIonicState:: PH74, 82 SetUseInputEnsemble, 50 OESz:: OEFreeFormIonicState:: Uncharged, OESz:: OEFreeFormSolvResults, 50 81 Constructors, 50 OESz:: OEFreeFormReturnCode, 82 GetAtomicPotentials, 51 OESz::OEFreeFormReturnCode::AtomTypeFailure,GetElectrostaticSolvationFreeEnergy,  $82$ 51 OESz::OEFreeFormReturnCode::ChargeAssignFaiBet&WdrophobicSolvationFreeEnergy,  $51$ 83 OESz::OEFreeFormReturnCode::ChargeMismatch, GetReturnCode, 51 83 GetSolvationFreeEnergy, 51

GetWarnings, 51

```
operatorerator = 51OESz:: OEPotentialTerms:: HarmonicConstraint,
OESz:: OEFreeFormWarning, 84
                                                   76
OESz:: OEFreeFormWarning:: HSamplingSkippedESz:: OEPotentialTerms:: IEFFInteraction,
       85
                                                   77
OESz:: OEFreeFormWarning:: Missing3DCoordi0E6es; OEPotentialTerms:: ImproperTorsion,
       85
                                                   73
OESz::OEFreeFormWarning::NotRemovableCha0E6z::OEPotentialTerms::InterLigandIEFF,
                                                   77
       84
OESz:: OEFreeFormWarning:: UnspecifiedSter@E$z:: OEPotentialTerms:: LigandBend, 74
                                           OESz:: OEPotentialTerms:: LigandBond, 74
       84
OESz:: OEFreeFormWarning:: ZeroPartialCharQESz:: OEPotentialTerms:: LigandCoulomb,
       85
                                                   73
OESz:: OEGetEnergyTermName, 86
                                           OESz:: OEPotentialTerms:: LigandDesolvation,
OESz:: OEGetFreeFormError, 86
                                                   76
OESz:: OEGetSzybkiError, 86
                                            OESz:: OEPotentialTerms:: LigandImproperTorsion,
OESz:: OELigandChargeType, 95
                                                   74
OESz:: OELigandChargeType:: AM1BCC, 95
                                            OESz:: OEPotentialTerms:: LigandStretchBend,
OESz:: OELigandChargeType:: AM1BCCELF10.
                                                   74
       95
                                           OESz::OEPotentialTerms::LigandTorsion,
OESz:: OELigandChargeType:: CURRENT, 95
                                                   74OESz:: OELigandChargeType:: MMFF, 95
                                           OESz:: OEPotentialTerms:: LigandVdW, 73
OESz:: OELigandEntropy, 88
                                            OESz:: OEPotentialTerms:: Max, 78
OESz:: OELigandEntropyOptions, 64
                                           OESz:: OEPotentialTerms:: PBSolvation, 76
   Constructors. 65
                                            OESz:: OEPotentialTerms:: ProteinBend. 75
                                           OESz:: OEPotentialTerms:: ProteinBond, 74
   GetEnvironment, 65
   GetForceField, 65
                                            OESz:: OEPotentialTerms:: ProteinCoulomb,
   GetLigandCharge, 65
                                                   74
   operator=, 65
                                            OESz:: OEPotentialTerms:: ProteinDesolvation,
   SetEnvironment, 65
                                                   76
   SetForceField. 65
                                            OESz:: OEPotentialTerms:: ProteinImproperTorsion,
   SetLigandCharge, 66
                                                   75
OESz:: OEOptimizationType, 95
                                           OESz:: OEPotentialTerms:: ProteinLigandAmberCoulomb,
OESz:: OEOptimizationType:: Cartesian, 95
                                                   77
OESz:: OEOptimizationType:: PoseCartesian, OESz:: OEPotentialTerms:: ProteinLigandAmberVdW,
       95
                                                   77
OESz:: OEOptType, 71
                                            OESz:: OEPotentialTerms:: ProteinLigandCoulomb,
OESz:: OEOptType:: BFGS, 71
                                                   75
OESz:: OEOptType:: CG, 71
                                           OESz:: OEPotentialTerms:: ProteinLigandInteraction,
OESz:: OEOptType:: NEWTON, 72
                                                   75
OESz:: OEOptType:: SD, 71
                                           OESz:: OEPotentialTerms:: ProteinLigandVdW,
OESz:: OEOptType:: SD_BFGS, 71
                                                   75
OESz:: OEOptType:: SD_CG, 72
                                           OESz:: OEPotentialTerms:: ProteinPseudoLigandInteract
OESz:: OEPotentialTerms, 72
                                                   77
OESz:: OEPotentialTerms:: Bend, 73
                                           OESz:: OEPotentialTerms:: ProteinStretchBend,
OESz:: OEPotentialTerms:: Bond, 73
                                                   75
OESz:: OEPotentialTerms:: CavitySolvation, OESz:: OEPotentialTerms:: ProteinTorsion,
       76
                                                   75
OESz:: OEPotentialTerms:: Coulomb, 73
                                           OESz:: OEPotentialTerms:: ProteinVdW.74
OESz:: OEPotentialTerms:: CoulombProteinLiQE6d:: OEPotentialTerms:: SheffieldSolvation,
       76
                                                   75
OESz:: OEPotentialTerms:: ExactCoulomb.
                                            OESz:: OEPotentialTerms:: SolventScreening,
       77
                                                   76
OESz:: OEPotentialTerms:: GridCoulomb, 77
                                           OESz:: OEPotentialTerms:: StretchBend, 73
                                           OESz:: OEPotentialTerms:: Torsion, 73
```

```
OESz:: OEPotentialTerms:: TorsionHarmonicCOEStra0EProtFlex:: Residues, 81
                                            OESz:: OEProtFlex:: SideChains, 81
       77
OESz:: OEPotentialTerms:: VdW, 72
                                            OESz:: OEProtFlex:: SideChainsList, 81
OESz:: OEPotentialTerms:: VdWProteinLigandQESz:: OERestrictionEnergyResult, 52
       76
                                                Constructors, 52
OESz:: OEProteinElectrostatics, 78
                                                GetGlobalStrain, 52
OESz::OEProteinElectrostatics::ExactCoulomb,GetLocalStrain, 52
       78
                                                operator=, 52
OESz:: OEProteinElectrostatics:: GridCoulomBSz:: OERunType, 78
       78
                                            OESz:: OERunType:: CartesiansOpt, 79
OESz:: OEProteinElectrostatics:: GridPB,
                                            OESz:: OERunType:: SinglePoint, 79
                                            OESz:: OERunType:: SolidBodyOpt, 79
       78
OESz:: OEProteinElectrostatics:: NoElectro@E8tic@ERunType:: TorsionsOpt, 79
       78
                                            OESz:: OESingleConfResult, 52
OESz:: OEProteinElectrostatics:: SolventPBForCenstructors. 52
       78
                                                GetConfIdx, 53
OESz:: OEProteinFlexOptions, 35
                                                GetDeltaG.53
   Constructor, 35
                                                GetLnOrotational.53
   GetFlexRange, 36
                                                GetLnQvibrational, 53
   GetResidueID, 36
                                                GetMMFFEnergy, 53
   operator=, 35
                                                GetProbability, 53
   SetFlexRange, 36
                                                GetRelativeEnergy, 54
   SetResidueID, 36
                                                GetRelLnQ, 54
OESz:: OEProteinLigandOptOptions, 36
                                                GetRotationalEntropy, 54
   Constructor, 36
                                                GetSolvEnergy, 54
   GetForceField. 37
                                                GetTotalEnergy, 54
   GetGradTolerance, 37
                                                GetVibrationalEntropy, 54
   GetLigandCharge, 37
                                                operator=, 53
   GetMaxIter, 37
                                            OESz:: OESolventModel, 79
   GetNonBondCutoff, 37
                                            OESz:: OESolventModel:: Cavity, 80
   GetOptimizationType, 37
                                            OESz:: OESolventModel:: NoSolv, 79
   GetSolventModel, 38
                                            OESz::OESolventModel::PB, 80
   operator=, 37
                                            OESz:: OESolventModel:: Sheffield, 79
   SetForceField, 38
                                            OESz:: OESzybki, 11
   SetGradTolerance, 38
                                                ClearFixAtoms, 11
   SetLigandCharge, 38
                                                ClearHarmonicConstraints.12
   SetMaxIter, 38
                                                ClearTorsionConstraint, 12
   SetNonBondCutoff, 38
                                               Constructors, 11
   SetOptimizationType, 39
                                               FixAtoms, 12
   SetSolventModel, 39
                                               GetEntropy, 12
OESz:: OEProteinLigandOptResults, 39
                                                GetEntropy (const
                                                   OEChem:: OEMCMolBase&, unsigned
   Constructors, 39
   GetFinalEnergies, 40
                                                   int, unsigned int), 12
   GetInitialEnergies, 40
                                                GetFixPattern, 13
   GetLigandRMSD, 40
                                                GetFixPredicate, 13
   GetProteinRMSD, 40
                                                GetHarmonicConstraints, 13
   GetReturnCode, 40
                                                GetProtein, 13
   GetTotalRMSD, 40
                                               GetSheffieldParameters, 13
   operator=, 39
                                               LoadPotentialGrid, 14
OESz:: OEProtFlex, 80
                                                operator(), 11
OESz:: OEProtFlex:: NoFlex, 80
                                                SavePotentialGrid. 14
                                               SetHarmonicConstraints, 14
OESz:: OEProtFlex:: PolarH, 81
OESz:: OEProtFlex:: PolarHResList, 81
                                               SetProtein. 14
OESz:: OEProtFlex:: ResidueList, 81
                                                SetSheffieldParameters, 14
```

SetTorsionConstraint. 15 UnsetProtein. 15 OESz:: OESzybkiEnsembleResults, 33 Constructors, 33 GetChargeType, 34 GetConfigurationalEntropy, 34 GetEnsembleLiqPartialSolvEntropy, 34 GetEnsembleLigSolvEntropy, 34 GetEnsembleProtDesolvEntropy, 35 GetEntropicEnergy, 34 GetResultsForConformations, 35 GetTemperature, 33 GetTotalEntropy, 34 HasEntropy, 35 NumConfs, 33 operator=, 33 OESz:: OESzybkiGeneralOptions, 17 Constructors, 17 GetCalculateGradients, 18 GetForceField, 18 GetForceFieldType, 18 GetIEFFCluster, 18 GetIntramolecularVdWCutoff, 18 GetLigandRMSDHeavy, 18 GetRemoveAttractiveVdWForces, 19 GetRemoveCoulombTerms. 19 GetSoluteDielectric, 19 GetTemperature, 19 GetVerbose, 19 operator=, 18 SetCalculateGradients, 19 SetForceField. 19 SetForceFieldType, 20 SetIEFFCluster, 20 SetIntramolecularVdWCutoff, 20 SetLigandRMSDHeavy, 20 SetRemoveAttractiveVdWForces, 20 SetRemoveCoulombTerms, 20 SetSoluteDielectric, 21 SetTemperature, 21 SetVerbose, 21 OESz:: OESzybkiGetArch, 86 OESz:: OESzybkiGetLicensee, 86 OESz:: OESzybkiGetPlatform, 86 OESz:: OESzybkiGetRelease, 86 OESz:: OESzybkiGetSite, 86 OESz:: OESzybkiGetVersion, 87 OESz:: OESzybkiOptions, 15 Constructors, 15 GetGeneralOptions, 16 GetOptOptions, 16 GetProteinOptions, 16 GetRunType, 16 GetSolventOptions, 16

operator=, 15 SetGeneralOptions, 16 SetOptOptions, 17 SetProteinOptions, 17 SetRunType, 17 SetSolventOptions, 17 OESz:: OESzybkiOptOptions, 21 Constructors, 21 GetCalculateFrozenTerms.21 GetGradTolerance, 22 GetMaxIter, 22 GetOptimizerType, 22  $operatorerator =$ , 21 SetCalculateFrozenTerms, 22 SetGradTolerance, 22 SetMaxIter, 22 SetOptimizerType, 23 OESz:: OESzybkiProteinOptions, 25 AddFlexibleResidue.26 ClearFlexibleResidues, 26 Constructors, 25 GetExactVdWProteinLigand, 26 GetIntermolecularVdWCutoff, 26 GetProteinDielectric.26 GetProteinElectrostaticModel, 26 GetProteinFlexibilityRange, 27 GetProteinFlexibilityType, 27 HasFlexibleResidues, 27 operator=, 25 SetExactVdWProteinLigand, 27 SetIntermolecularVdWCutoff, 27 SetProteinDielectric.27 SetProteinElectrostaticModel, 28 SetProteinFlexibilityRange, 28 SetProteinFlexibilityType.28 OESz:: OESzybkiResults, 28 Clear. 29 Constructors, 28 GetConfFreeEnergyFromEnsemble, 31 GetConfIdx, 29 GetCPUTime, 29 GetEnergyTerm, 29 GetFinalRMSGradient, 29 GetFinalTotalPotential, 29 GetGradients, 29 GetInitialRMSGradient, 30 GetInitialTotalPotential, 30 GetInterEnergy, 30 GetIntramolecularLigandEnergy, 30 GetLnQrot, 32 GetLnOvib, 32 GetMaxDisplacement, 30 GetNumCycles, 30 GetNumFixAtoms, 30

GetNumRotors, 31 SetUseCurrentCharges, 25 GetProteinRMSD.31 OESz:: OETorsionScan. 87 GetRMSD, 31 OESz:: OETorsionScanner, 62 Constructor, 62 GetRotEntropy, 32 GetTotalEnergy, 31 GetLowestEneResults, 63 GetTotalEnergyWithHarmConstraint, 31 GetLowestEnergyConfs, 63 GetVibEntropy, 32 GetScannedAngles, 63 GetSinglePointConfs, 63 IsActiveTerm, 31 IsUnique, 32 operator=, 62 operator=, 28  $Scan, 63$ Print, 32 OESz:: OETorsionScanOptions, 56 OESz:: OESzybkiReturnCode, 96 Constructors, 56 OESz::OESzybkiReturnCode::ContainsImplicitH,GetDelta, 57 GetForceField, 57 96 OESz:: OESzybkiReturnCode:: ExcessiveOverlap, GetForceFieldType, 57 96 GetMaxIter, 57 OESz:: OESzybkiReturnCode:: Failed, 97 GetNumStarts, 58 OESz:: OESzybkiReturnCode:: FFNeedHessiens, GetOverlapDiv.58 GetPenaltyForceConstant, 57 96 OESz::OESzybkiReturnCode::IncompleteOpt, GetSolvationType, 58 GetTolerance, 57 96 OESz::OESzybkiReturnCode::InvalidOptions, GetUseInternalCoord, 58 96 GetUserDefinedAngles, 58 OESz::OESzybkiReturnCode::LigandFailedChargGetUseSinglePointPB, 58 operator=, 57 97 OESz::OESzybkiReturnCode::LigandFailedFF, SetDelta.59 97 SetForceField, 59 OESz:: OESzybkiReturnCode:: LigandMissing3D, SetForceFieldType, 59 97 SetMaxIter, 59 OESz:: OESzybkiReturnCode:: LigandMissingCharGetNumStarts, 60 97 SetOverlapDiv, 60 OESz:: OESzybkiReturnCode:: ProteinFailedFF, SetPenaltyForceConstant, 59 96 SetSolvationType.59 OESz:: OESzybkiReturnCode:: ProteinMissing3D, SetTolerance, 60 97 SetUseInternalCoord. 60 OESz:: OESzybkiReturnCode:: ProteinMissingChafGot, UserDefinedAngles, 60 97 SetUseSinglePointPB, 60 OESz:: OESzybkiReturnCode:: ProteinNotSet, OESz:: OETorsionScanResult, 61 97 Constructors, 61 OESz:: OESzybkiReturnCode:: Success, 96 GetAngle, 61 OESz:: OESzybkiSolventOptions, 23 GetEnergy, 61 Constructors, 23  $operatorerator =$ , 61 GetAtomicRadiiType, 23 operator() GetCavitySolventParameter, 23 OESz:: OESzybki, 11 GetSaltConcentration, 23 operator= GetSolventDielectric, 24 OESz:: OEBoundEntropyOptions, 64 GetSolventModel, 24 OESz:: OEEntropyResults, 66  $operatorerator = 23$ OESz:: OEFixedProteinLigandOptimizer, SetAtomicRadiiType, 24 91 SetCavitySolventParameter, 24 OESz:: OEFlexProteinLigandOptimizer, SetChargeEngine, 25 93 SetSaltConcentration, 24 OESz:: OEFreeFormConf, 41 SetSolventDielectric, 24 OESz:: OEFreeFormConfAdvanced. 42 OESz:: OEFreeFormConfOptions, 44 SetSolventModel, 25

```
OESz:: OEFreeFormConfResults, 55
   OESz:: OEFreeFormSolvOptions, 48
   OESz:: OEFreeFormSolvResults, 51
   OESz:: OELigandEntropyOptions, 65
   OESz:: OEProteinFlexOptions, 35
   OESz:: OEProteinLigandOptOptions, 37
   OESz:: OEProteinLigandOptResults, 39
   OESz:: OERestrictionEnergyResult, 52
   OESz:: OESingleConfResult, 53
   OESz:: OESzybkiEnsembleResults, 33
   OESz:: OESzybkiGeneralOptions, 18
   OESz:: OESzybkiOptions, 15
   OESz:: OESzybkiOptOptions, 21
   OESz:: OESzybkiProteinOptions, 25
   OESz:: OESzybkiResults, 28
   OESz:: OESzybkiSolventOptions, 23
   OESz:: OETorsionScanner, 62
   OESz:: OETorsionScanOptions, 57
   OESz:: OETorsionScanResult, 61
Optimize
   OESz:: OEFixedProteinLigandOptimizer, SetDelta
       92
   OESz:: OEFlexProteinLigandOptimizer,
       93
   OESz:: OEFreeFormConfAdvanced, 43
optimizedu.py
   Example Code, 123
optimizeligandindu.py
   Example Code, 121
OptimizeRestraint
   OESz:: OEFreeFormConfAdvanced, 43
```

# P

```
PreOptimizeEnsemble
   OESz:: OEFreeFormConfAdvanced, 43
PrepareEnsemble
   OESz:: OEFreeFormConfAdvanced, 43
Print
   OESz:: OESzybkiResults, 32
PrintCsv
   OESz:: OEFreeFormConfResults, 56
PrintTxt
   OESz:: OEFreeFormConfResults, 56
protein_ligand_pb.py
   Example Code, 118
protein_multiple_options.py
   Example Code, 109
```

# R.

RemoveDuplicates OESz:: OEFreeFormConfAdvanced, 44

# S

SavePotentialGrid

```
OESz:: OESzybki, 14
Scan
   OESz:: OETorsionScanner, 63
SetAtomicRadiiType
   OESz:: OEFreeFormSolvOptions, 49
   OESz:: OESzybkiSolventOptions, 24
SetCalculateFrozenTerms
   OESz:: OESzybkiOptOptions, 22
SetCalculateGradients
   OESz:: OESzybkiGeneralOptions, 19
SetCavitySolventParameter
   OESz:: OESzybkiSolventOptions, 24
SetChargeEngine
   OESz:: OESzybkiSolventOptions, 25
SetChargeType
   OESz:: OEFreeFormSolvOptions, 49
SetConfGenRMS
   OESz:: OEFreeFormSolvOptions, 49
SetCorrSolventOptions
   OESz:: OEFreeFormConfOptions, 46
   OESz:: OETorsionScanOptions, 59
SetEnvironment
   OESz:: OELigandEntropyOptions, 65
SetExactVdWProteinLigand
   OESz:: OESzybkiProteinOptions, 27
SetFlexRange
   OESz:: OEProteinFlexOptions, 36
SetForceField
   OESz:: OEBoundEntropyOptions, 64
   OESz:: OELigandEntropyOptions, 65
   OESz:: OEProteinLigandOptOptions, 38
   OESz:: OESzybkiGeneralOptions, 19
   OESz:: OETorsionScanOptions, 59
SetForceFieldType
   OESz:: OESzybkiGeneralOptions, 20
   OESz:: OETorsionScanOptions, 59
SetGeneralOptions
   OESz:: OESzybkiOptions, 16
SetGradTolerance
   OESz:: OEProteinLigandOptOptions, 38
   OESz:: OESzybkiOptOptions, 22
SetHarmonicConstraints
   OESz:: OESzybki, 14
SetIEFFCluster
   OESz:: OESzybkiGeneralOptions, 20
SetIntermolecularVdWCutoff
   OESz:: OESzybkiProteinOptions, 27
SetIntramolecularVdWCutoff
   OESz:: OESzybkiGeneralOptions, 20
SetIonicState
   OESz:: OEFreeFormConfOptions, 46
   OESz:: OEFreeFormSolvOptions, 49
SetLigandCharge
```

OESz:: OEBoundEntropyOptions, 64 OESz:: OELigandEntropyOptions, 66 OESz:: OEProteinLigandOptOptions, 38 SetLigandRMSDHeavy OESz:: OESzybkiGeneralOptions, 20 SetMaxConfGen OESz:: OEFreeFormSolvOptions, 50 SetMaxIter OESz:: OEProteinLigandOptOptions, 38 OESz:: OESzybkiOptOptions, 22 OESz:: OETorsionScanOptions, 59 SetNonBondCutoff OESz:: OEProteinLigandOptOptions, 38 SetNumStarts OESz:: OETorsionScanOptions, 60 SetOmegaOptions OESz:: OEFreeFormConfOptions, 46 SetOptimizationType OESz:: OEProteinLigandOptOptions, 39 SetOptimizeOptions OESz:: OEFreeFormConfOptions, 46 SetOptimizerType OESz:: OESzybkiOptOptions, 23 SetOptOptions OESz:: OESzybkiOptions, 17 SetOverlapDiv OESz:: OETorsionScanOptions, 60 SetPenaltyForceConstant OESz:: OETorsionScanOptions, 59 SetPreOptimizeOptions OESz:: OEFreeFormConfOptions, 47 SetProtein OESz:: OEFixedProteinLigandOptimizer, SetUseInternalCoord  $92$ OESz:: OESzybki, 14 SetProteinDielectric OESz:: OESzybkiProteinOptions, 27 SetProteinElectrostaticModel OESz:: OESzybkiProteinOptions, 28 SetProteinFlexibilityRange OESz:: OESzybkiProteinOptions, 28 SetProteinFlexibilityType OESz:: OESzybkiProteinOptions, 28 SetProteinOptions OESz:: OESzybkiOptions, 17 SetRemoveAttractiveVdWForces OESz:: OESzybkiGeneralOptions, 20 SetRemoveCoulombTerms OESz:: OESzybkiGeneralOptions, 20 SetResidueID OESz:: OEProteinFlexOptions, 36 SetResults OESz:: OEEntropyResults, 67 SetRunType

OESz:: OESzybkiOptions, 17 SetSaltConcentration OESz:: OESzybkiSolventOptions, 24 SetSheffieldParameters OESz:: OESzybki, 14 SetSoluteDielectric OESz:: OESzybkiGeneralOptions, 21 SetSolvationType OESz:: OETorsionScanOptions, 59 SetSolventDielectric OESz:: OESzybkiSolventOptions, 24 SetSolventModel OESz:: OEProteinLigandOptOptions, 39 OESz:: OESzybkiSolventOptions, 25 SetSolventOptions OESz:: OEFreeFormConfOptions, 47 OESz:: OESzybkiOptions, 17 SetSzybkiGeneralOptions OESz:: OEFreeFormConfOptions, 47 SetTemperature OESz:: OESzybkiGeneralOptions, 21 SetTolerance OESz:: OETorsionScanOptions, 60 SetTorsionConstraint OESz:: OESzybki, 15 SetUseCurrentCharges OESz:: OESzybkiSolventOptions, 25 SetUseInput3D OESz:: OEFreeFormSolvOptions, 50 SetUseInputEnsemble OESz:: OEFreeFormConfOptions, 47 OESz:: OEFreeFormSolvOptions, 50 OESz:: OETorsionScanOptions, 60 SetUserDefinedAngles OESz:: OETorsionScanOptions, 60 SetUseSinglePointPB OESz:: OETorsionScanOptions, 60 SetUseSolventCorr OESz:: OEFreeFormConfOptions, 47 SetVerbose OESz:: OESzybkiGeneralOptions, 21 simple\_conformer.py Example Code, 106 simple\_newton.py Example Code, 105 simple\_protein.py Example Code, 107 simple\_smirnoff.py Example Code, 100 simple\_vacuum.py Example Code, 99

# $\top$

torsionscan.py Example Code, 137

# $\bigcup$

UnsetProtein OESz:: OESzybki, 15