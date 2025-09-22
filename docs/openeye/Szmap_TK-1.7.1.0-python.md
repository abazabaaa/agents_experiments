![](_page_0_Picture_0.jpeg)

**Szmap TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| Section | Title                                                        | Page                            |    |
|---------|--------------------------------------------------------------|---------------------------------|----|
| 1       | Introduction                                                 | 1                               |    |
| 1.1     | Licenses                                                     | 1                               |    |
| 2       | Theory                                                       | 2                               |    |
| 2.1     | Semi-continuum Solvation with SZMAP                          | 2                               |    |
| 2.1.1   | Energy Calculations                                          | 2                               |    |
| 2.1.2   | Uncharged Water and Difference Energies                      | 2                               |    |
| 2.1.3   | Stabilization                                                | 3                               |    |
| 2.2     | Working with Szmap TK                                        | 5                               |    |
| 2.2.1   | Preparing Protein and Ligand Molecules                       | 5                               |    |
| 2.2.2   | Calculating Energies                                         | 5                               |    |
| 2.2.3   | Generating Probe Orientations                                | 6                               |    |
| 2.3     | The Szmap TK Standard Water Model                            | 8                               |    |
| 3       | Examples                                                     | 9                               |    |
| 3.1     | Szmap TK Examples                                            | 9                               |    |
| 3.1.1   | Analyze binding site energies                                | 9                               |    |
| 3.1.2   | Generate Szmap points and probe orientations at ligand atoms | 12                              |    |
| 4       | API                                                          | 17                              |    |
| 4.1     | OESzmap Classes                                              | 17                              |    |
| 4.1.1   | OESzmapEngine                                                | 17                              |    |
| 4.1.2   | OESzmapEngineOptions                                         | 19                              |    |
| 4.1.3   | OESzmapResults                                               | 21                              |    |
| 4.2     | OESzmap Constants                                            | 25                              |    |
| 4.2.1   | OEComponent                                                  | 25                              |    |
| 4.2.2   | OEEnsemble                                                   | 27                              |    |
| 4.3     | OESzmap Functions                                            | 29                              |    |
| 4.3.1   | OECalcSzmapResults                                           | 29                              |    |
| 4.3.2   | OECalcSzmapValue                                             | 30                              |    |
| 4.3.3   | OEGetComponentName                                           | 30                              |    |
| 4.3.4   | OEGetEnsembleName                                            | 30                              |    |
| 4.3.5   | OEIsClashing                                                 | 31                              |    |
| 4.3.6   | OESzmapGetArch                                               | 31                              |    |
| 4.3.7   | OESzmapGetLicense                                            | 31                              |    |
| 4.3.8   | OESzmapGetPlatform                                           | 31                              |    |
| 4.3.9   | OESzmapGetRelease                                            | 32                              |    |
| 4.3.10  | OESzmapGetSite                                               | 32                              |    |
| 4.3.11  | OESzmapGetVersion                                            | 32                              |    |
| 4.3.12  | OESzmapIsLicensed                                            | 32                              |    |
| 5       |                                                              | <b>Release History</b>          | 33 |
|         | 5.1                                                          | Szmap TK 1.7.1                  | 33 |
|         | 5.2                                                          | Szmap TK 1.7.0                  | 33 |
|         | 5.2.1                                                        | Documentation changes           | 33 |
|         | 5.3                                                          | Szmap TK 1.6.7                  | 33 |
|         | 5.4                                                          | Szmap TK 1.6.6                  | 33 |
|         | 5.5                                                          | Szmap TK 1.6.5                  | 33 |
|         | 5.6                                                          | Szmap TK 1.6.4                  | 33 |
|         | 5.7                                                          | Szmap TK 1.6.3                  | 34 |
|         | 5.8                                                          | Szmap TK 1.6.2                  | 34 |
|         | 5.9                                                          | Szmap TK 1.6.1                  | 34 |
|         | 5.10                                                         | Szmap TK 1.6.0                  | 34 |
|         | 5.11                                                         | Szmap TK 1.4.6                  | 34 |
|         | 5.12                                                         | Szmap TK 1.4.5                  | 34 |
|         | 5.13                                                         | Szmap TK 1.4.4                  | 34 |
|         | 5.14                                                         | Szmap TK 1.4.3                  | 35 |
|         | 5.15                                                         | Szmap TK 1.4.2                  | 35 |
|         | 5.16                                                         | Szmap TK 1.4.1                  | 35 |
|         | 5.17                                                         | Szmap TK 1.4.0                  | 35 |
|         | 5.18                                                         | Szmap TK 1.3.7                  | 35 |
|         | 5.19                                                         | Szmap TK 1.3.6                  | 35 |
|         | 5.20                                                         | Szmap TK 1.3.5                  | 35 |
|         | 5.21                                                         | Szmap TK 1.3.4                  | 35 |
|         | 5.22                                                         | Szmap TK 1.3.3                  | 36 |
|         | 5.23                                                         | Szmap TK 1.3.2                  | 36 |
|         | 5.24                                                         | Szmap TK 1.3.1                  | 36 |
|         | 5.24.1                                                       | Major bug fixes                 | 36 |
|         | 5.24.2                                                       | Documentation fixes             | 36 |
|         | 5.25                                                         | Szmap TK 1.3.0                  | 36 |
|         | 5.25.1                                                       | Features                        | 36 |
| 6       |                                                              | <b>Copyright and Trademarks</b> | 37 |
| 7       |                                                              | <b>Sample Code</b>              | 39 |
| 8       |                                                              | <b>Citation</b>                 | 41 |
|         | 8.1                                                          | Orion ® Floes                   | 41 |
|         | 8.2                                                          | Toolkits and Applications       | 41 |
|         | 8.3                                                          | OpenEye Web Services            | 43 |
| 9       |                                                              | <b>Technology Licensing</b>     | 45 |
|         | 9.1                                                          | GCC                             | 60 |
|         | 9.1.1                                                        | GCC RUNTIME LIBRARY EXCEPTION   | 60 |
|         | 9.1.2                                                        | GNU GENERAL PUBLIC LICENSE      | 62 |
|         |                                                              | <b>Index</b>                    | 75 |

### **CHAPTER**

# **INTRODUCTION**

The Szmap TK provides simple access to SZMAP functionality for calculating solvent thermodynamic properties near molecular surfaces.

## 1.1 Licenses

To perform calculations with  $Szmap TK$  you will need to obtain a license file for  $szmapck$  and  $oechem$  from OpenEye, Cadence Molecular Sciences (https://www.eyesopen.com/contact). If you wish to incorporate additional OpenEye functionality into software you develop, other licenses may also be required.

The license file should be in a file pointed to by the OE\_LICENSE environment variable. On Windows, the environment variables can be set under the system Control Panel.

This manual is to familiarize the user with *Szmap TK* functionality. It does not provide an explanation of basic OEChem classes and functions. Therefore reading the OEChem TK manual beforehand is highly recommended.

Another source of information is the "OpenEye SZMAP" manual, which describes the szmap and qameplan applications and associated utilities, along with the theory behind SZMAP.

Finally, the "OpenEye Zap" manual is a good source of information on the theory and practice of Poisson-Boltzmann calculations.

### See also:

- Python Quick Start Manual for installation instructions.
- How to Import the Toolkits section

## **CHAPTER**

## **TWO**

# **THEORY**

# 2.1 Semi-continuum Solvation with SZMAP

![](_page_6_Picture_4.jpeg)

Fig. 1: Water Probe Orientations

SZMAP is a technology—based on semi-continuum Poisson-Boltzmann theory—for analyzing proteins and/or ligands using an explicit probe water molecule to estimate various thermodynamic properties.

The Poisson-Boltzmann (PB) continuum model of water [Grant-2001], [Gilson-1988], and [Sharp-1990] is simple, effective, and with OpenEve's OEZap, fast. But, near strong charges or in regions of constrained geometry PB can be too good at solvating a surface, leading to over-estimates of solvation free energies [Sharp-1991]. PB also fails to model hydrogen bonds, "structured waters", and other geometric considerations important to drug design.

One common approach to capturing these geometric aspects of solvation is to use all-atom simulations such as molecular dynamics with explicit solvent. For some molecular properties this may be a good way to go. But the very heavy sampling cost is often not repaid in improved results [Nicholls-2008], [Nicholls-2009].

For solvation, a more efficient approach is to probe the region of interest with a single explicit all-atom solvent molecule, embedded in and interacting with continuum solvent and with the molecular surface.

SZMAP is just such a semi-continuum solvation model. It uses OEZap to perform the PB calculations. Because the

continuum solvent responds to the charges and geometry of the solvent probe water-water interactions are captured. Because the probe is constrained by its physical size and shape, structural details of solvent to solute interactions are captured.

### **2.1.1 Energy Calculations**

By sampling a full range of orientations for the probe at any position, thermodynamic properties are calculated using statistical mechanics.

For the purposes of discussion, we'll assume the solute being analyzed is a protein. The energy for each probe water orientation  $j$  is the sum of the ZAP protein: water Coulombic interaction energy, the protein and water desolvation penalties and the van der Waals energy. For speed, the protein desolvation term is not computed for each orientation, but is instead computed once per point using a spherical united-atom representation of the probe water.

$$
E_j = ZAP_{int}(P:W) + P_{desolv}^* + W_{desolv} + VDW \{j = 1 \cdots N_{orient}\}
$$

The partition function  $Q$  is the usual sum:

$$
Q = \sum_{j=1}^{N_{orient}} e^{-\frac{E_j}{kT}}
$$

The probability of each orientation is then:

$$
prob_j = \frac{e^{-\frac{E_j}{kT}}}{Q}
$$

The probe water orientation entropy difference from continuum water is:

$$
T\Delta S = \left(-kT\sum_{j=1}^{N_{orient}} prob_j \ln prob_j\right) - kT \ln N_{orient}
$$

Likewise, the probe water free energy difference from continuum water is:

$$
\Delta G = -(kT \ln Q - kT \ln N_{orient})
$$

And of course, the enthalpy difference is the sum:

$$
\Delta H = \Delta G + T \Delta S
$$

### 2.1.2 Uncharged Water and Difference Energies

The values Szmap TK calculates for  $\Delta G$ ,  $\Delta H$  and  $T\Delta S$  represent differences between the explicit probe water and the continuum water. In other words, a positive  $\Delta G$  indicates that the continuum model over-estimates the cost of displacing water at that position. When trying to decide which modifications are most likely to increase binding affinity, we would prefer to compare the water probe to the ligand atom that displaces it, or at least a proxy for the ligand atom. In SZMAP, this proxy is the water probe without any of the energy terms that involve a charge on the water (leaving only  $P_{desolv} + VDW$ ). Because these energy terms have already been determined, calculating the properties for this "uncharged" or "neutral" water requires no additional time, it's free. The difference in free energy between standard and uncharged water is negative where standard water is more favored and positive where the uncharged water, our hydrophobic group proxy, is more favored.

This OEEnsemble NeutralDiffDeltaG energy and the OEEnsemble VDW energy (which is subtracted out of the difference calculation above) are the primary SZMAP terms relevant to drug design.

Szmap TK can also calculate the difference between our probe and a vacuum bubble of the same size (defined as just the  $P_{desolv}$  term). Because protein desolvation is treated as constant over all probe orientations only the vacuum free energy and enthalpy differences are calculated, not the entropy differences.

Regions are said to *clash* if the sum of the van der Waals and interaction energies is greater than a cutoff (by default  $0$  kcal  $mol^{-1}$ ). Calculated ensemble energies in clashing regions are usually not very meaningful.

When interpreting these difference energies, it should be beneficial for a hydrophobic ligand atom to overlap a region where the neutral free energy difference is positive because this involves displacing water that is less favorable than the neutral probe. Overlapping a region where the neutral free energy difference is negative, on the other hand, requires the overlapping group to be at least as polar as water and making a similar level of interactions.

### 2.1.3 Stabilization

It is possible to use *Szmap TK* to calculate *stabilization* energies as a reaction energy

 $(holo-complex + bulk-solvent) - (apo-pocket + free-ligand)$ 

where bulk-solvent is defined as  $0kcal \ mol^{-1}$ , by subtracting neutral difference free energies from a point near the protein/ligand complex, the protein alone, and the ligand alone.

Negative stabilization free energy values indicate water is stabilized at that location in the complex, over and above the same location in the ligand and the *apo* pocket. Positive values are found where the water is destabilized in the complex. The stabilization or destabilization says nothing about the actual level of stability, so these energies need to be compared to others such as the  $apo$  or complex neutral difference free energy.

## 2.2 Working with Szmap TK

The *Szmap TK* has a simple API, consisting of a few basic *API* and a couple of objects to configure the calculations (OESzmapEngine and OESzmapEngineOptions) and hold calculated results (OESzmapResults).

### 2.2.1 Preparing Protein and Ligand Molecules

To perform the necessary electrostatics calculations, a protein or any other molecular context being analyzed with SZMAP must already have all hydrogens explicitly represented as well as have charges and radii assigned before it can be used. This is done automatically as part of protein preparation with Spruce TK (see OEMakeDesignUnits). Charges can also be assigned using Quacpac TK (see OEAssignCharges).

### **2.2.2 Calculating Energies**

To calculate probe energies, we initialize a OESzmapEngine with a molecular context, test if the point of interest is clashing, and if not, calculate the energies. In the example below, the energies at each ligand atom coordinate are returned in a OESzmapResults object, which is accessed for specific values. Alternatively, OECalcSzmapValue could be used to get a single OEEnsemble value directly.

```
def GetSzmapEnergies(lig, prot):
    n \, n \, nrun szmap at ligand coordinates in the protein context
    @rtype : None
    @param lig: mol defining coordinates for szmap calcs
    @param prot: context mol for szmap calcs (must have charges and radii)
```

 $n \, n \, n$ 

(continued from previous page)

```
print("num\tatom\t%s\t%s\t%s\t%s\t%s"
      % (oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_NeutralDiffDeltaG),
         oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_PSolv),
         oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_WSolv),
         oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_VDW),
         oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_OrderParam)))
coord = oechem. OEFloatArray(3)sz = oeszmap.OESzmapEngine(prot)
rslt = oeszmap.OESzmapResults()for i, atom in enumerate (liq. GetAtoms ()):
    lig.GetCoords(atom, coord)
    if not oeszmap. OEIsClashing (sz, coord):
        oeszmap.OECalcSzmapResults(rslt, sz, coord)
        print ("%2d\t%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f"
              % (i, atom. GetName (),
                 rslt.GetEnsembleValue(oeszmap.OEEnsemble_NeutralDiffDeltaG),
                 rslt.GetEnsembleValue(oeszmap.OEEnsemble_PSolv),
                 rslt.GetEnsembleValue(oeszmap.OEEnsemble_WSolv),
                 rslt.GetEnsembleValue(oeszmap.OEEnsemble_VDW),
                 rslt.GetEnsembleValue(oeszmap.OEEnsemble_OrderParam)))
    Also.print ("%2d\t%s CLASH" % (i, atom. GetName()))
```

The five OEEnsemble values in the example above are the primary ones for understanding solvent/ligand competition.

#### See also:

• GetSzmapEnergies example

### **2.2.3 Generating Probe Orientations**

In addition to energy calculations, the  $Szmap TK$  can be used to generate 3D conformations of probe molecules at calculated points, annotated with OEComponent energies for each conformation. In the example below, individual atoms are also generated at calculation points, each annotated with OEEnsemble values.

```
def GenerateSzmapProbes(oms, cumulativeProb, lig, prot):
    generate multiconf probes and data-rich points at ligand coords
    @rtype : None
    @param oms: output mol stream for points and probes
    @param cumulativeProb: cumulative probability for cutoff of point set
    @param lig: mol defining coordinates for szmap calcs
    @param prot: context mol for szmap calcs (must have charges and radii)
    n \, n \, ncoord = oechem. OEFloatArray (3)
    sz = oeszmap.OESzmapEngine(prot)
```

```
rslt = oeszmap. OESzmapResults()
points = oechem.OEGraphMol()
points.SetTitle("points %s" % lig.GetTitle())
probes = oechem. <math>OEMol()</math>for i, atom in enumerate (lig. GetAtoms ()) :
    lig.GetCoords(atom, coord)
    if not oeszmap. OEIsClashing (sz, coord) :
        oeszmap.OECalcSzmapResults(rslt, sz, coord)
        rslt.PlaceNewAtom(points)
        clear = Falserslt.PlaceProbeSet(probes, cumulativeProb, clear)
oechem. OEWriteMolecule (oms, points)
oechem.OEWriteMolecule(oms, probes)
```

![](_page_10_Figure_3.jpeg)

Fig. 2: High Probability Probe Orientations and Points with Generic Data Annotation

#### See also:

• SzmapBestOrientations example

## 2.3 The Szmap TK Standard Water Model

A standard SZMAP water has "TIP" geometry:  $r(OH) = 0.9572$  Å and  $HOH$  angle = 104.52°. Point charges for hydrogen and oxygen are +0.327 and -0.654, respectively, scaled from AM1BCC charges to reproduce the vacuum dipole of water. And we use Bondi radii (H: 1.20 Å and O: 1.52 Å). See the *Theory* section of the "OpenEye SZMAP" application manual for more information of how these values were derived.

### **CHAPTER**

## **THREE**

# **EXAMPLES**

## **3.1 Szmap TK Examples**

The following table lists the currently available Szmap TK examples:

| Program                         | Description                                                  |
|---------------------------------|--------------------------------------------------------------|
| <i>GetSzmapEnergies.py</i>      | Analyze binding site energies                                |
| <i>SzmapBestOrientations.py</i> | Generate Szmap points and probe orientations at ligand atoms |

### **Examples:**

### 3.1.1 Analyze binding site energies

A program that calculates energies at each ligand atom coordinate.

#### See also:

- OESzmapEngine class
- OESzmapResults class
- · OECalcSzmapValue function
- · OEIsClashing function
- · OEEnsemble namespace

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python SzmapEnergies.py --help

will generate the following output:

```
Simple parameter list
-high_res : If true, increase the number of orientations to 360
-1 : Input ligand coordinates for calculations
 -p : Input protein (or other) context mol
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
# analyze binding site energies with szmaptk
import sys
from openeye import oechem
from openeye import oeszmap
InterfaceData = ""!BRIEF SzmapEnergies.py [-high_res] [-du] <designunitfile>
!PARAMETER -du
  !TYPE string
  !BRIEF Input designunit
 !REQUIRED true
 !KEYLESS 1
! END
!PARAMETER -high res
 !TYPE bool
 !DEFAULT false
 !BRIEF If true, increase the number of rotations to 360
 !REQUIRED false
! END
n \times ndef GetSzmapEnergies(lig, prot, highRes):
    run szmap at ligand coordinates in the protein context
    Qrtype : None
    @param lig: mol defining coordinates for szmap calcs
    @param prot: context mol for szmap calcs (must have charges and radii)
    @param highRes: if true, use 360 rotations rather than the default of 60
    n \, n \, nopt = oeszmap.OESzmapEngineOptions()
    if highRes:
        opt.SetProbe(360)
    sz = oeszmap.OESzmapEngine(prot, opt)
```

```
coord = oechem. OEFloatArray(3)
    rslt = oeszmap.OESzmapResults()print ("num\tatom\t%s\t%s\t%s\t%s\t%s"
          % (oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_NeutralDiffDeltaG),
             oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_PSolv),
             oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_WSolv),
             oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_VDW),
             oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_OrderParam)))
    for i, atom in enumerate (lig. GetAtoms ()) :
        lig.GetCoords(atom, coord)
        if not oeszmap. OEIsClashing (sz, coord):
            oeszmap.OECalcSzmapResults(rslt, sz, coord)
            print ("%2d\t%s\t%.3f\t%.3f\t%.3f\t%.3f\t%.3f"
                   % (i, atom.GetName(),
                     rslt.GetEnsembleValue(oeszmap.OEEnsemble_NeutralDiffDeltaG),
                     rslt.GetEnsembleValue(oeszmap.OEEnsemble_PSolv),
                     rslt.GetEnsembleValue(oeszmap.OEEnsemble_WSolv),
                     rslt.GetEnsembleValue(oeszmap.OEEnsemble_VDW),
                     rslt.GetEnsembleValue(oeszmap.OEEnsemble OrderParam)))
        else:print ("%2d\t%s CLASH" % (i, atom. GetName()))
def main(argv = ( name )):H, H, Hthe protein should have charges and radii but the ligand need not
    itf = oechem. 0EInterface()if not oechem. OEConfigure (itf, InterfaceData):
        oechem. OEThrow. Fatal ("Problem configuring OEInterface!")
   if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to parse command line")
   durile = itf.GetString("-du")du = oechem. OEDesignUnit ()
   if not oechem. OEReadDesignUnit (duFile, du) :
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % duFile)
    if not du. HasLigand():
        oechem. OEThrow. Fatal ("Input designunit % does not have a ligand bound" % du.
\rightarrowGetTitle())
    lig = oechem. OEGraphMol()du.GetLigand(lig)
   prot = oechem. OEGraphMol()
   du.GetComponents(prot, oechem.OEDesignUnitComponents_Protein)
   highRes = itf.GetBool("-high res")
    GetSzmapEnergies(lig, prot, highRes)
```

```
name = " main "if
   sys.exit(main(sys.argv))
```

#### **Examples**

```
prompt> python SzmapEnergies.py -1 4std_lig.oeb.gz -p 4std_prot.oeb.gz
```

### 3.1.2 Generate Szmap points and probe orientations at ligand atoms

A program that generates 3D conformations of probe molecules and Szmap points at each ligand atom coordinate.

See also:

- OESzmapEngine class
- OESzmapResults class
- OECalcSzmapValue function
- OEIsClashing function
- · OEEnsemble namespace
- OEComponent namespace

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

python SzmapBestOrientations.py --help

will generate the following output:

```
Simple parameter list
-1 : Input ligand coordinates for calculations
-o : Output file for points and probes molecules
-p : Input protein (or other) context mol
-prob : Cutoff for cumulative probability of probes
```

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
```

```
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
# generate szmap points and probe orientations at ligand atoms
import sys
from openeye import oechem
from openeye import oeszmap
InterfaceData = """!BRIEF SzmapBestOrientations.py [-prob #.#] [-du] <designunitfile> [-o] <molfile>
!PARAMETER -du
  !TYPE string
 !BRIEF Input designunit
  !REQUIRED true
  !KEYLESS 1
!END
!PARAMETER -0
  ! TYPE string
  !BRIEF Output file for points and probes molecules
 !REQUIRED true
 !KEYLESS 2
LEND
!PARAMETER -prob
  ! TYPE double
  !DEFAULT 0.5
 !BRIEF Cutoff for cumulative probability of probes
  !REQUIRED false
! END
\overline{n} \overline{n} \overline{n}def GenerateSzmapProbes(oms, cumulativeProb, lig, prot):
    \pi \pi \pigenerate multiconf probes and data-rich points at ligand coords
    @rtype : None
    @param oms: output mol stream for points and probes
    @param cumulativeProb: cumulative probability for cutoff of point set
    @param lig: mol defining coordinates for szmap calcs
    @param prot: context mol for szmap calcs (must have charges and radii)
    n \overline{n}sz = oeszmap. OESzmapEngine (prot)
    rslt = oeszmap. OESzmapResults()
    points = oechem. OEGraphMol()
    points.SetTitle("points %s" % lig.GetTitle())
    probes = occhem. OEMol()coord = occhem. OEFloatArray(3)
    for i, atom in enumerate (lig. GetAtoms ()):
```

```
lig.GetCoords(atom, coord)
        if not oeszmap. OEIsClashing (sz, coord) :
            oeszmap.OECalcSzmapResults(rslt, sz, coord)
            rslt.PlaceNewAtom(points)
            clear = Falserslt.PlaceProbeSet(probes, cumulativeProb, clear)
            name = oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_NeutralDiffDeltaG)
            nddG = rslt.GetEnsembleValue(oeszmap.OEEnsemble_NeutralDiffDeltaG)
            print ("$2d ($7.3f, $7.3f, $7.3f): $s = $.3f"
                   % (i, coord[0], coord[1], coord[2], name, nddG))
        Also:print ("%2d (%7.3f, %7.3f, %7.3f): CLASH"
                   % (i, coord[0], coord[1], coord[2]))oechem. OEWriteMolecule (oms, points)
    oechem.OEWriteMolecule(oms, probes)
def main(argv=(_name_)):
    the protein should have charges and radii but the ligand need not
    itf = oechem. 0EInterface()if not oechem. OEConfigure (itf, InterfaceData) :
        oechem. OEThrow. Fatal ("Problem configuring OEInterface!")
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to parse command line")
   durile = itf.GetString("-du")du = oechem. 0EDesignUnit()if not oechem. OEReadDesignUnit (duFile, du) :
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % duFile)
    if not du. HasLigand():
        oechem. OEThrow. Fatal ("Input designunit % does not have a ligand bound" % du.
\rightarrowGetTitle())
   lig = oechem.OEGraphMol()
   du.GetLigand(lig)
    prot = occhem.OEGraphMol()du. GetComponents (prot, oechem. OEDesignUnitComponents Protein)
   outputFile = itf.GetString("-<math>\circ</math>")if not oechem. OEIsWriteable (outputFile) :
        oechem. OEThrow. Fatal ("Invalid file extension for output %s" % outputFile)
   oms = oechem.oemolostream()
    if not oms.open(outputFile):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % outputFile)
    GenerateSzmapProbes(oms, itf.GetDouble("-prob"), lig, prot)
```

```
if _name_ = = "_main":
   sys.exit(main(sys.argv))
```

### **Examples**

```
prompt> python SzmapBestOrientations.py -1 4std_lig.oeb.gz -p 4std_prot.oeb.gz -o
→SzmapBestOrientations.oeb.gz
```

### **CHAPTER**

## **FOUR**

**API** 

## **4.1 OESzmap Classes**

### 4.1.1 OESzmapEngine

#### class OESzmapEngine

This class represents OESzmapEngine, an object used to perform SZMAP calculations. It stores the context molecule, the configuration options (including the probe molecule), and an OEZap object used to perform the Poisson-Boltzmann electrostatics calculations by OECalcSzmapResults, OECalcSzmapValue, and OEIsClashing. A OESzmapEngine may cache the results of a calculation at a given 3D point to improve efficiency.

#### See also:

- GetSzmapEnergies example
- SzmapBestOrientations example

### **Constructors**

```
OESzmapEngine (const OESzmapEngine & rhs)
OESzmapEngine (const OESzmapEngineOptions & opt=OESzmapEngineOptions())
OESzmapEngine (const OEChem:: OEMolBase &context,
              const OESzmapEngineOptions &opt=OESzmapEngineOptions())
```

Default and copy constructors, along with constructors that take a context molecule (typically a properly prepared protein, see OESzmapEngine. SetContext) and/or a OESzmapEngineOptions object.

```
sz = oeszmap. OESzmapEngine (prot, opt)
```

#### operator=

OESzmapEngine & operator= (const OESzmapEngine & rhs)

Assignment operator.

#### operator bool

operator bool() const

Returns true if this object is valid for use in OESzmap calculations. A context molecule—either at construction or through a call to  $OESzmapEngine$ . Set Context— must be provided to establish validity.

#### **CheckAtomTypes**

bool CheckAtomTypes() const

Returns *true* if atom types could be applied to the molecular context and probe molecules.

#### **GetContext**

const OEChem:: OEMolBase & GetContext () const

Returns a reference to the molecular context for OESzmap calculations (see OESzmapEngine. SetContext).

```
mol = sz.GetContext()print ("context mol: %s" % mol. GetTitle())
```

#### **GetOptions**

const OESzmapEngineOptions &GetOptions () const

Returns a reference to the OESzmapEngineOptions used to construct this OESzmapEngine. It can be used to construct another OESzmapEngine object and to access details of the probe and other settings.

#### **SetContext**

bool SetContext (const OEChem:: OEMolBase &context)

Updates the molecular context used for any OESzmap calculations based on this object (see OESzmapEngine. SetContext and OESzmapEngine. operator bool).

Note: A context molecule is required to have partial charges already associated with each atom. Atomic radii are also necessary, but will be generated if not supplied.

Returns *true* if the context molecule is acceptable, with 3D coordinates and partial charges.

### 4.1.2 OESzmapEngineOptions

#### class OESzmapEngineOptions

This class represents OESzmapEngineOptions, an object used to set one or more options when constructing an OESzmapEngine.

```
opt.SetProbe(24).SetMaskCutoff(999.99)
```

When returned by OESzmapEngine. GetOptions, can be used to determine the settings used for a given set of calculations.

```
opt = sz.getOptions()print ("norient= %d" % opt. NumOrientations ())
print ("name = \frac{e}{6}S" \frac{e}{6} opt. GetProbeName ())
print ("cutoff = \frac{2}{3}. 3f" \frac{2}{3} opt. GetMaskCutoff())
```

#### **Constructors**

```
OESzmapEngineOptions()
OESzmapEngineOptions (const OESzmapEngineOptions & rhs)
```

Default and copy constructors. The default OESzmapEngineOptions object defines the probe to be a standard SZMAP water with 60 orientations.

```
opt = oeszmap.OESzmapEngineOptions()
```

#### operator=

OESzmapEngineOptions & operator=(const OESzmapEngineOptions & rhs)

Assignment operator.

#### **GetMaskCutoff**

```
double GetMaskCutoff() const
```

Returns the energy cutoff (in kcal/mol) defining a *clash* (by default, 0.0; see OEIsClashing and OESzmapEngineOptions. SetMaskCutoff). A clash means every orientation of the probe had a combined OEComponent\_Interaction+OEComponent\_VDW energy total greater than the cutoff.

#### **GetProbe**

const OEChem:: OEMCMolBase & GetProbe () const

Returns a reference to the current multi-conformer probe molecule (see OESzmapEngineOptions. SetProbe).

```
p = opt.GetProbe()print ("probe nconf = d" \gamma p. NumConfs ())
```

#### **GetProbeMol**

```
void GetProbeMol(OEChem:: OEMolBase &outputMol,
                 unsigned int orientation=0u) const
```

Updates output Mol to contain a specific orientation of the current multi-conformer probe (see OESzmapEngineOptions. SetProbe). By default, the first orientation is returned.

```
mol = occhem. OEGraphMol()opt.GetProbeMol(mol)
```

#### **GetProbeName**

const char \*GetProbeName() const

Returns the standard name of the current probe type (e.g. "water").

#### **NumOrientations**

unsigned int NumOrientations () const

Returns the number of orientations for the current probe (see OESzmapEngineOptions. SetProbe).

#### **SetMaskCutoff**

OESzmapEngineOptions &SetMaskCutoff(double cutoff)

Set the energy cutoff (in kcal/mol) defining a clash (by default, 0.0; see OEIsClashing and OESzmapEngineOptions.GetMaskCutoff). A clash means every orientation of the probe had a combined OEComponent\_Interaction+OEComponent\_VDW energy total greater than the cutoff.

### **SetProbe**

OESzmapEngineOptions &SetProbe (unsigned int numOrientations)

Define the current multi-conformation probe molecule to be a standard SZMAP water molecule with the specified number of orientations (see The Szmap TK Standard Water Model for more information on the geometry and charges used).

If numOrientations is set to 24, 60, 216, 360, or 648 then the set of orientations will be symmetric. Otherwise, it will include random orientations and may have lopsided gaps in coverage. For most purposes, 60 is the minimum required for reliable energy calculations and 360 generates higher-precision results, although with a speed penalty due to the additional Zap calculations.

```
opt.SetProbe(360)
```

The default OESzmapEngineOptions standard SZMAP water has 60 orientations.

### **4.1.3 OESzmapResults**

#### class OESzmapResults

This class represents OESzmapResults, a container for the results of OESzmap calculations with the function OECalcSzmapResults.

#### See also:

- GetSzmapEnergies example
- SzmapBestOrientations example

#### **Constructors**

```
OESzmapResults()
OESzmapResults (const OESzmapResults & rhs)
```

Default and copy constructors. Typically an empty, default OESzmapResults is passed to OECalcSzmapResults where it is filled with the calculated results.

```
rslt = oeszmap.OESzmapResults()
```

#### operator=

```
OESzmapResults & operator= (const OESzmapResults & rhs)
```

Assignment operator.

#### operator bool

operator bool() const

True indicates that OECalcSzmapResults was called with a valid OESzmapEngine when this object was created.

#### **Clear**

```
void Clear()
```

Resets this object to an uninitialized, empty state.

#### **GetComponent**

```
bool GetComponent (double *compArray, unsigned int componentType) const
OESystem::OEIterBase<double> *GetComponent (unsigned int componentType) const
```

Returns the calculated values of a particular OEComponent, specified by component Type, for the 3D point provided to OECalcSzmapResults. Component values for each probe orientation are the low-level data used to compose OEEnsemble values (see OESzmapResults. GetEnsembleValue). The number of values in the output compArray or the iterator is OESzmapResults. NumOrientations and values are returned in the same order as the probe orientations.

```
coulomb = rslt.GetComponent(oeszmap.OEComponent_Interaction)
print ("interaction:")
print (" ".join ("\S. 3f" \S c for c in coulomb))
```

Returns false or an empty iterator if the OEComponent type is not recognized.

### **GetCoords**

```
bool GetCoords (float *xyz) const
bool GetCoords (double *xyz) const
```

Returns the coordinates of the 3D point where calculations were performed by  $OECalcSzmapResults$  to create this object.

The point is passed back in a float or double array of size three with coordinates in  $\{x,y,z\}$  order.

```
point = occhem.OEFloatArray(3)rslt.GetCoords(point)
```

Returns false if this OESzmapResults is uninitialized.

### **GetEnsembleValue**

double GetEnsembleValue (unsigned int ensembleType) const

Returns the calculated value of a particular OEEnsemble, specified by ensembleType, for the 3D point provided to OECalcSzmapResults. Ensemble values are the results of calculations over all orientations of the probe. In general, these are built by Boltzmann summation of various combinations of OEComponent values (see OESzmapResults.GetComponent).

nddg = rslt.GetEnsembleValue(oeszmap.OEEnsemble NeutralDiffDeltaG)

Returns 0.0 if the  $OEEnsemble$  type is not recognized or this  $OESzmapResults$  is uninitialized.

#### **GetProbabilities**

```
bool GetProbabilities (double *probArray) const
OESystem::OEIterBase<double> *GetProbabilities() const
```

Returns the statistical mechanical probabilities for each probe orientation at the 3D point provided to OECalcSzmapResults. Probability values can be used to Boltzmann weight OEComponent values and are used to select which probe orientations are returned by OESzmapResults. PlaceProbeSet. The number of values in the output probArray or the iterator is OESzmapResults. NumOrientations and values are returned in the same order as the probe orientations.

```
prob = rslt.GetProbabilities()print ("greatest prob = \frac{2}{3}. 3f" \frac{8}{3} prob[order[0]])
```

Returns false or an empty iterator if this OESzmapResults is uninitialized.

#### GetProbabilityOrder

```
bool GetProbabilityOrder (unsigned int *orderArray) const
OESystem::OEIterBase<unsigned int> *GetProbabilityOrder() const
```

Returns an array or iterator of indices referring to probe orientations or associated OEComponent and probability values, sorted in the order of increasing probability (see OESzmapResults. GetProbabilities). Hence, the first (orderArray [0]) is the index of the orientation with the greatest probability (probArray [orderArray [0]]). The number of values in the output order Array or the iterator is OESzmapResults. NumOrientations.

```
order = rslt.GetProbabilityOrder()
print ("conf with greatest prob = \partial u'' % order [0])
```

Returns *false* or an empty iterator if this *OESzmapResults* is uninitialized.

#### **NumOrientations**

unsigned int NumOrientations () const

Returns the number of orientations for the probe molecule used in the calculation. Equals the number of values returned by calls to OESzmapResults.GetComponent, OESzmapResults.GetProbabilities, or OESzmapResults.GetProbabilityOrder.

### **PlaceNewAtom**

```
OEChem:: OEAtomBase *PlaceNewAtom (OEChem:: OEMolBase &mol,
                                  unsigned int element=OEChem::OEElemNo::0) const
```

Adds a new atom to the input molecule with atomic coordinates of the 3D point provided to OECalcSzmapResults when the object was created.

```
amol = occhem.OEGraphMol()atom = rslt.PlaceNewAtom(amol)
print ("vdw = \frac{6}{6} s" % atom. GetData ("vdw"))
```

The new atom has been annotated with ensemble values for this point as generic data. String versions of the data have been formatted to two decimal places for convenient display.

| Generic Data Tag            | Type   | Value (energies in kcal/mol)                 |
|-----------------------------|--------|----------------------------------------------|
| szmap_neut_diff_free_energy | double | Probe - neutral probe free energy difference |
| szmap_order                 | double | Fractional entropy loss from electrostatics  |
| szmap_vdw                   | double | Van der Waals energy                         |
| free-energy                 | string | Formatted szmap_neut_diff_free_energy        |
| order-param                 | string | Formatted szmap_order                        |
| vdw                         | string | Formatted szmap_vdw                          |

The atom type can be controlled through the optional element parameter, which defaults to oxygen.

Returns a pointer to the newly created atom to facilitate further customization.

![](_page_27_Figure_1.jpeg)

#### Fig. 1: Atoms Placed at Calculation Points with Generic Data Annotation

### **PlaceProbeMol**

bool PlaceProbeMol(OEChem:: OEMolBase &outputMol, unsigned int orientation=0u, bool annotate=true) const

Modifies the outputMol to be a copy of one probe orientation, placed at the 3D point provided to  $OECalcSzmapResults$  when the object was created. The probe orientation can be controlled through the optional orientation parameter (the default value of 0 refers to the first probe conformation).

```
pmol = oechem.OEGraphMol()
rslt.PlaceProbeMol(pmol, order[0])
```

If the optional parameter annotate is *true* (the default), the molecule will be annotated with OEComponent data for that orientation. See OESzmapResults. PlaceProbeSet for more information on this annotation.

Returns false if this OESzmapResults is uninitialized.

#### **PlaceProbeSet**

```
double PlaceProbeSet (OEChem:: OEMCMolBase &probeSet, double probCutoff,
                     bool clear=true) const
double PlaceProbeSet (OEChem:: OEMCMolBase &probeSet, unsigned int maxConfs=0u,
                     bool clear=true) const
```

Modifies the multi-conformer probeset to contain one or more orientations of the probe, each placed at the 3D point provided to OECalcSzmapResults when the object was created. The probe set is returned in probability order (see OESzmapResults.GetProbabilityOrder).

There are three ways to select which probe orientations are placed in the probe Set:

• If just the probeset parameter is provided, without other options, all probe orientations will be returned.

```
mcmol = occhem. OEMol()
rslt.PlaceProbeSet(mcmol)
```

• If the real number parameter  $probCutoff$  is used, probe orientations will be added until the total cumulative probability is at least that amount. Cumulative probabilities are  $> 0.0$  and  $\leq 1.0$ .

```
probCutoff = 0.5rslt.PlaceProbeSet(mcmol, probCutoff)
print ("nconf to yield 50pct = \partial d'' \partial mcmol. NumConfs ())
```

• Finally, if the integer parameter maxConfs is used, no more than number of probe orientations will be returned. A value of  $\theta$  is a special signal to return all orientations.

```
clear = FalsecumulativeProb = rslt.PlaceProbeSet(mcmol, 10, clear)
print ("best 10 cumulative prob = \frac{2}{3}. 3f" \frac{8}{3} cumulativeProb)
```

If the optional parameter clear is set to *false*, any previous orientations in the probeset will not be cleared, allowing conformers for multiple 3D points as well as multiple orientations to be stored in the probeset. By default, previous orientations *are* cleared away before the new orientations are added.

Each orientation has been annotated with OEComponent data for that orientation. In addition, the total interac $tion + psolv + wsolv + vdw$  energy of each is recorded as the energy of the conformation (accessible using the Get Energy () method of the conformer). String versions of the data have been formatted to two decimal places for convenient display. String data is also stored as SD data, so they are included in VIDA's spreadsheet and can be saved to, sd files.

| Generic/SD Data Tag | Type   | SD  | Value (energies in kcal/mol)                |
|---------------------|--------|-----|---------------------------------------------|
| szmap_interaction   | double | no  | Poisson-Boltzmann probe/context interaction |
| szmap_psolv         | double | no  | (Protein) context desolvation penalty       |
| szmap_wsolv         | double | no  | (Water) probe desolvation penalty           |
| szmap_vdw           | double | no  | Van der Waals energy                        |
| szmap_probability   | double | no  | Boltzmann probability                       |
| total-energy        | string | yes | $szmap\_interaction + psolv + wsolv + vdw$  |
| interaction         | string | yes | Formatted szmap_interaction                 |
| psolv               | string | yes | Formatted szmap_psolv                       |
| wsolv               | string | yes | Formatted szmap_wsolv                       |
| vdw                 | string | yes | Formatted szmap_vdw                         |
| prob                | string | yes | Formatted szmap_probability                 |

Returns the cumulative probability of all the orientations returned, or 0.0 if this OESzmapResults is uninitialized.

## **4.2 OESzmap Constants**

### 4.2.1 OEComponent

The OEComponent namespace encodes symbolic constants representing various types of OESzmap calculation component values (the results of calculations on individual orientations of the probe). These components are used to determine OEEnsemble values.

#### See also:

• SzmapBestOrientations example

![](_page_29_Figure_1.jpeg)

Fig. 2: SD Annotation in the VIDA Spreadsheet

### **Interaction**

Poisson-Boltzmann electrostatic probelcontext interaction energy (kcal/mol).

### **PSolv**

(Protein) context desolvation penalty (kcal/mol).

### **WSolv**

(Water) probe desolvation penalty (kcal/mol).

### **VDW**

Van der Waals energy (kcal/mol, MMFF94).

### **ProbeBurial**

Fractional probe burial. Value ranges from 0.0 (exposed) to 1.0 (completely buried).

### **NumTypes**

Number of OEComponent types.

### 4.2.2 OEEnsemble

The OEEnsemble namespace encodes symbolic constants representing various types of OESzmap calculation ensemble values (the results of calculations over all orientations of the probe). In general, these are built by Boltzmann summation of OEComponent values.

#### See also:

- GetSzmapEnergies example
- SzmapBestOrientations example

### **Interaction**

Poisson-Boltzmann electrostatic probelcontext interaction energy (kcal/mol).

### **PSolv**

(Protein) context desolvation penalty (kcal/mol).

### **WSolv**

(Water) probe desolvation penalty (kcal/mol).

### **VDW**

Van der Waals energy (kcal/mol, MMFF94).

### **ProbeBurial**

Fractional probe burial. Value ranges from 0.0 (exposed) to 1.0 (completely buried).

### **InteractionPlusVDW**

Minimum value of the sum of the interaction energy and the van der Waals energy (kcal/mol). This value is used to determine if a point is clashing.

### **OrderParam**

Fractional entropy loss from electrostatics. Value ranges from 0.0 (unconstrained, all orientations equivalent) to 1.0 (completely fixed, single orientation dominates).

### **CalcPoint**

Calculations performed: 1.0; no calculation: 0.0.

#### **Mask**

Clash: 0.0; not a clash: 1.0.

### **NeutralDiffDeltaH**

Charged probe - neutral probe enthalpy difference (kcal/mol).

### **NeutralDiffTDeltaS**

Charged probe - neutral probe entropy difference (kcal/mol).

### **NeutralDiffDeltaG**

Charged probe - neutral probe free energy difference (kcal/mol).

#### **NeutralDeltaH**

Enthalpy of neutral probe vs continuum (kcal/mol).

### **NeutralTDeltaS**

Entropy of neutral probe vs continuum (kcal/mol).

### **NeutralDeltaG**

Free energy of neutral probe vs continuum (kcal/mol).

### **VacuumDiffDeltaH**

Probe - vacuum probe enthalpy difference (kcal/mol).

### **VacuumDiffDeltaG**

Probe - vacuum probe free energy difference (kcal/mol).

### **DeltaH**

Enthalpy of probe vs continuum (kcal/mol).

### **TDeltaS**

Entropy of probe vs continuum (kcal/mol).

### **DeltaG**

Free energy of probe vs continuum (kcal/mol).

### **NumTypes**

Number of OEEnsemble types.

### **Default**

Default type. Same as OEEnsemble\_NeutralDiffDeltaG.

## **4.3 OESzmap Functions**

### **4.3.1 OECalcSzmapResults**

```
bool OECalcSzmapResults (OESzmap:: OESzmapResults & results,
                             OESzmap:: OESzmapEngine &szmap,
                             \textbf{const } \textbf{float } \star \texttt{xyz)}bool OECalcSzmapResults (OESzmap:: OESzmapResults & results,
                             OESzmap:: OESzmapEngine &szmap,
                             const double *xyz)
```

Update a OESzmapResults object by performing SZMAP calculations at the specified 3D point, using the OESzmapEngine provided. The OESzmapResults provides access to all of the OEEnsemble and OEComponent values as well as orientation probabilities and geometry.

```
if not oeszmap. OEIsClashing (sz, coord):
   oeszmap.OECalcSzmapResults(rslt, sz, coord)
    nddg = rslt.GetEnsembleValue(oeszmap.OEEnsemble NeutralDiffDeltaG)
```

Returns false if calculations were not performed because the OESzmapEngine was not initialized.

The 3D point is a float or double array of size three with coordinates in  $\{x,y,z\}$  order.

 $coord = oechem. OEFloatArray(3)$ 

### 4.3.2 OECalcSzmapValue

```
double OECalcSzmapValue (OESzmap:: OESzmapEngine &szmap,
                        const float *xyz,
                        unsigned int ensembleType=OESzmap::OEEnsemble::Default)
double OECalcSzmapValue (OESzmap:: OESzmapEngine &szmap,
                        const double *xyz,
                        unsigned int ensembleType=OESzmap::OEEnsemble::Default)
```

Returns one of the OEEnsemble values at the specified 3D point, using the OESzmapEngine provided. See OEEnsemble Default for a description of the default energy value.

nddg = oeszmap.OECalcSzmapValue(sz, coord)

The 3D point is a float or double array of size three with coordinates in  $\{x,y,z\}$  order.

See also:

- GetSzmapEnergies example
- SzmapBestOrientations example

### 4.3.3 OEGetComponentName

const char \*OEGetComponentName (unsigned int componentType)

Returns a character string of the standard name for the specified OEComponent type.

name = oeszmap.OEGetComponentName(oeszmap.OEComponent\_Interaction)

### 4.3.4 OEGetEnsembleName

```
const char *OEGetEnsembleName (unsigned int ensembleType,
                              bool longName=false)
```

Returns a character string of the standard name for the specified OEEnsemble type.

By default, a short form of the name, suitable for column headings, is provided. If the optional longName argument is set to *true*, a more readable name is provided.

```
longName = Truename = oeszmap.OEGetEnsembleName(oeszmap.OEEnsemble_NeutralDiffDeltaG, longName)
```

### 4.3.5 OEIsClashing

```
bool OEIsClashing (OESzmap:: OESzmapEngine &szmap, const float *xyz)
bool OEIsClashing (OESzmap:: OESzmapEngine &szmap, const double *xyz)
```

Determines whether the probe associated with the OESzmapEngine provided clashes with the context molecule at the specified 3D point. A clash means every orientation of the probe had a combined OEComponent Interaction + OEComponent\_VDW energy total greater than the cutoff defined in the OESzmapEngine at the specified point. See OESzmapEngineOptions.GetMaskCutoff and OESzmapEngineOptions.SetMaskCutoff.

The 3D point is a float or double array of size three with coordinates in  $\{x,y,z\}$  order.

It is recommended you call this function before calling OECalcSzmapValue or OECalcSzmapResults, as data for clashing points is generally meaningless.

```
if not oeszmap. OEIsClashing (sz, coord):
    oeszmap.OECalcSzmapResults(rslt, sz, coord)
    \# ...
```

See also:

- GetSzmapEnergies example
- SzmapBestOrientations example

### 4.3.6 OESzmapGetArch

const char \*OESzmapGetArch()

Returns a character string describing the operating system and hardware.

### 4.3.7 OESzmapGetLicensee

```
std::string OESzmapGetLicensee()
bool OESzmapGetLicensee(std::string &licensee)
```

Returns the name of the licensee from the active user license.

### 4.3.8 OESzmapGetPlatform

const char \*OESzmapGetPlatform()

Returns a character string describing the operating system, hardware and the compiler used to build this version of OESzmap.

### 4.3.9 OESzmapGetRelease

const char \*OESzmapGetRelease()

Returns the release number string for this version of OESzmap.

### 4.3.10 OESzmapGetSite

```
std::string OESzmapGetSite()
bool OESzmapGetSite(std::string &site)
```

Returns the name of the site from the active user license.

### 4.3.11 OESzmapGetVersion

unsigned int OESzmapGetVersion()

Returns the release date of this version of OESzmap as an integer in YYYYMMDD format.

### 4.3.12 OESzmapIsLicensed

bool OESzmapIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any Szmap TK functionality.

The 'feature' argument can be used to check for a valid license to **Szmap TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current **Szmap TK** license.

#### See also:

· OEChemIsLicensed function

### **CHAPTER**

## **FIVE**

# **RELEASE HISTORY**

## 5.1 Szmap TK 1.7.1

Minor internal improvements have been made.

## 5.2 Szmap TK 1.7.0

## 5.2.1 Documentation changes

• Examples have been updated to use design units as inputs.

## 5.3 Szmap TK 1.6.7

Minor internal improvements have been made.

## 5.4 Szmap TK 1.6.6

Minor internal improvements have been made.

## 5.5 Szmap TK 1.6.5

Minor internal improvements have been made.

## 5.6 Szmap TK 1.6.4

• Minor internal improvements have been made.

## 5.7 Szmap TK 1.6.3

#### Fall 2021

• Minor internal improvements have been made.

## 5.8 Szmap TK 1.6.2

July 2021

Minor internal improvements have been made.

## 5.9 Szmap TK 1.6.1

### Fall 2020

• Minor internal improvements have been made.

## 5.10 Szmap TK 1.6.0

As part of the integration of OEToolkits and OEApplications into a single release, the version number of Szmap TK has been upgraded to 1.6.0 to make it consistent with that of the **SZMAP** application.

## 5.11 Szmap TK 1.4.6

• Minor internal improvements have been made.

## 5.12 Szmap TK 1.4.5

• Minor internal improvements have been made.

## 5.13 Szmap TK 1.4.4

• Minor internal improvements have been made.

## 5.14 Szmap TK 1.4.3

• Minor internal improvements have been made.

## 5.15 Szmap TK 1.4.2

• Minor internal improvements have been made.

## 5.16 Szmap TK 1.4.1

• Minor internal improvements have been made.

## 5.17 Szmap TK 1.4.0

• Minor internal improvements have been made.

## 5.18 Szmap TK 1.3.7

• Minor internal improvements have been made.

## 5.19 Szmap TK 1.3.6

• Minor internal improvements have been made.

## 5.20 Szmap TK 1.3.5

• Minor internal improvements have been made.

## 5.21 Szmap TK 1.3.4

Minor internal improvements have been made.

## 5.22 Szmap TK 1.3.3

• Minor internal cleanup has been performed.

## 5.23 Szmap TK 1.3.2

• Minor internal improvements

## 5.24 Szmap TK 1.3.1

### 5.24.1 Major bug fixes

- Fixed a critical problem that was causing crashes when duplicating OESzmapResults objects using the copy constructor or assignment operator.
- . Molecules returned from OESzmapEngineOptions.GetProbe, OESzmapEngineOptions. GetProbeMol OESzmapResults. PlaceProbeSet, OESzmapResults. PlaceProbeMol, and OESzmapResults. PlaceNewAtom, are now all explicitly marked as three-dimensional. This allows the coordinates to be written properly in . sdf format.

### **5.24.2 Documentation fixes**

• Fixed minor typos in the examples.

## 5.25 Szmap TK 1.3.0

• First release of Szmap toolkit.

### 5.25.1 Features

- Calculates solvent energies and probabilities at arbitrary points in space.
- Provides access to probe geometry for output and display.

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

## **SEVEN**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

### **CHAPTER**

## **EIGHT**

# **CITATION**

# 8.1 Orion<sup>®</sup> Floes

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

### **CHAPTER**

## **NINE**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
|----------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| abseil-cpp                                   | https://github.com/abseil/abseil-cpp                                                |                                                                                                                                                                    |
| absl-py                                      | https://github.com/abseil/abseil-py                                                 |                                                                                                                                                                    |
| aiohttp                                      | https://docs.aiohttp.org/en/stable/                                                 |                                                                                                                                                                    |
| aiosignal                                    | https://github.com/aio-libs/aiosignal                                               |                                                                                                                                                                    |
| Amazon Linux 2                               | https://aws.amazon.com/amazon-linux-2                                               | N/A                                                                                                                                                                |
| AmberUtils                                   | http://ambermd.org                                                                  | N/A                                                                                                                                                                |
| ambit                                        | https://github.com/khimaros/ambit                                                   |                                                                                                                                                                    |
| amqp                                         | https://github.com/celery/py-amqp                                                   |                                                                                                                                                                    |
| anaconda-anon-usage                          | Orion Floes                                                                         |                                                                                                                                                                    |
| angular                                      | https://github.com/angular/angular.js                                               |                                                                                                                                                                    |
| angular-animate                              | https://github.com/angular/angular.js                                               |                                                                                                                                                                    |
| angular-cache                                | https://github.com/jmdobry/angular-cache                                            |                                                                                                                                                                    |
| angular-cookies                              | https://github.com/angular/angular.js                                               |                                                                                                                                                                    |
| angular-loggly-logger                        | https://github.com/ajbrown/angular-loggly-logger                                    |                                                                                                                                                                    |
| angular-mocks                                | https://github.com/angular/angular.js                                               |                                                                                                                                                                    |
| angular-resource                             | https://github.com/angular/angular.js                                               |                                                                                                                                                                    |
| angular-toggle-switch                        | https://github.com/cgarvis/angular-toggle-switch                                    |                                                                                                                                                                    |
| angular-ui-grid                              | https://github.com/angular-ui/ui-grid                                               |                                                                                                                                                                    |
| angular-ui-router                            | https://github.com/angular-ui/ui-router                                             |                                                                                                                                                                    |
| angular-ui-tree                              | https://github.com/angular-ui-tree/angular-ui-tree                                  |                                                                                                                                                                    |
| angular-vs-repeat                            | https://github.com/kamilkp/angular-vs-repeat                                        |                                                                                                                                                                    |
| aniso8601                                    | https://bitbucket.org/nielsenb/aniso8601                                            |                                                                                                                                                                    |
| annotated-types                              | https://github.com/annotated-types/annotated-types                                  |                                                                                                                                                                    |
| anyio                                        | https://github.com/agronholm/anyio                                                  |                                                                                                                                                                    |
| appdirs                                      | http://github.com/ActiveState/appdirs                                               |                                                                                                                                                                    |
| appengine                                    | https://google.golang.org/appengine                                                 |                                                                                                                                                                    |
| arabic-reshaper                              | https://github.com/mpcabd/python-arabic-reshaper/                                   |                                                                                                                                                                    |
| archspec                                     | https://github.com/archspec/archspec/blob/master/README.md                          |                                                                                                                                                                    |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| argon2-cffi                                  | https://github.com/hynek/argon2-cffi                                                | https://                                                                                                                                                           |
| argon2-cffi-bindings                         | https://github.com/hynek/argon2-cffi-bindings                                       | https://                                                                                                                                                           |
| arpack                                       | https://www.caam.rice.edu/software/ARPACK/                                          | https://                                                                                                                                                           |
| ascii85                                      | https://github.com/huandu/node-ascii85                                              | https://                                                                                                                                                           |
| ase                                          | https://wiki.fysik.dtu.dk/ase/                                                      | https://                                                                                                                                                           |
| asgiref                                      | https://github.com/django/asgiref/                                                  | https://                                                                                                                                                           |
| asn1crypto                                   | https://github.com/wbond/asn1crypto                                                 | https://                                                                                                                                                           |
| assertions go-render                         | https://github.com/smartystreets/assertions/internal/go-render/render               | https://                                                                                                                                                           |
| assertions oglmatchers                       | https://github.com/smartystreets/assertions/internal/oglematchers                   | https://                                                                                                                                                           |
| assertions                                   | https://github.com/smartystreets/assertions                                         | https://                                                                                                                                                           |
| asttokens                                    | https://github.com/gristlabs/asttokens                                              | https://                                                                                                                                                           |
| astunparse                                   | https://github.com/simonpercivall/astunparse                                        | https://                                                                                                                                                           |
| async-lru                                    | https://github.com/aio-libs/async-lru                                               | https://                                                                                                                                                           |
| async-timeout                                | https://github.com/aio-libs/async-timeout                                           | https://                                                                                                                                                           |
| atk-1.0                                      | https://docs.gtk.org/atk/                                                           | https://                                                                                                                                                           |
| atomic                                       | https://github.com/uber-go/atomic                                                   | https://                                                                                                                                                           |
| atomicwrites                                 | https://github.com/untitaker/python-atomicwrites                                    | https://                                                                                                                                                           |
| attrs                                        | https://www.attrs.org/                                                              | https://                                                                                                                                                           |
| aws-sdk-go                                   | https://github.com/aws/aws-sdk-go                                                   | https://                                                                                                                                                           |
| Babel                                        | https://github.com/python-babel/babel                                               | https://                                                                                                                                                           |
| backcall                                     | https://github.com/takluyver/backcall                                               | https://                                                                                                                                                           |
| backports                                    | https://github.com/brandon-rhodes/backports                                         | https://                                                                                                                                                           |
| backports.functools-lru-cache                | https://github.com/jaraco/backports.functools_lru_cache                             | https://                                                                                                                                                           |
| base62                                       | https://github.com/kare/base62                                                      | https://                                                                                                                                                           |
| beautifulsoup4                               | https://www.crummy.com/software/BeautifulSoup/                                      | https://                                                                                                                                                           |
| billiard                                     | https://github.com/celery/billiard                                                  | https://                                                                                                                                                           |
| biopython                                    | https://biopython.org                                                               | https://                                                                                                                                                           |
| biotite                                      | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https://                                                                                                                                                           |
| bitset                                       | https://github.com/willf/bitset                                                     | https://                                                                                                                                                           |
| blas                                         | https://www.netlib.org/blas/                                                        | https://                                                                                                                                                           |
| bleach                                       | https://github.com/mozilla/bleach                                                   | https://                                                                                                                                                           |
| blessings                                    | https://github.com/erikrose/blessings                                               | https://                                                                                                                                                           |
| blinker                                      | https://pythonhosted.org/blinker/                                                   | https://                                                                                                                                                           |
| blosc                                        | https://github.com/Blosc/python-blosc                                               | https://                                                                                                                                                           |
| blosc2                                       | https://github.com/Blosc/python-blosc2                                              | https://                                                                                                                                                           |
| boltons                                      | https://github.com/mahmoud/boltons                                                  | https://                                                                                                                                                           |
| boost                                        | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://                                                                                                                                                           |
| boost-cpp                                    | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://                                                                                                                                                           |
| bootstrap-vue                                | https://github.com/bootstrap-vue/bootstrap-vue                                      | https://                                                                                                                                                           |
| boto3                                        | https://github.com/boto/boto3                                                       | https://                                                                                                                                                           |
| botocore                                     | https://github.com/boto/botocore                                                    | https://                                                                                                                                                           |
| Bottleneck                                   | https://bottleneck.readthedocs.io/en/latest/index.html                              | https://                                                                                                                                                           |
| Brotli                                       | https://github.com/google/brotli                                                    | https://                                                                                                                                                           |
| brotli-bin                                   | https://github.com/google/brotli                                                    | https://                                                                                                                                                           |
| brotli-python                                | http://python-hyper.org/projects/brotlipy/en/latest/                                | https://                                                                                                                                                           |
| brotlipy                                     | https://github.com/python-hyper/brotlipy                                            | https://                                                                                                                                                           |
| bson                                         | https://github.com/py-bson/bson                                                     | https://                                                                                                                                                           |
| bytefmt                                      | https://code.cloudfoundry.org/bytefmt                                               | https://                                                                                                                                                           |
| bzip2                                        | https://www.bzip.org                                                                | https://                                                                                                                                                           |
|                                              |                                                                                     | J.                                                                                                                                                                 |
| Name of Project                              | Website                                                                             | Licen                                                                                                                                                              |
| c-ares                                       | https://github.com/c-ares/c-ares                                                    | https:/                                                                                                                                                            |
| ca-certificates                              | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/                                                                                                                                                            |
| cached-property                              | https://github.com/pydanny/cached-property                                          | https:/                                                                                                                                                            |
| cachetools                                   | https://github.com/tkem/cachetools/                                                 | https:/                                                                                                                                                            |
| cairo                                        | https://pycairo.readthedocs.io/en/latest/                                           | https:/                                                                                                                                                            |
| canvas                                       | https://github.com/Automattic/node-canvas                                           | https:/                                                                                                                                                            |
| cctbx                                        | https://github.com/cctbx/cctbx_project                                              | https:/                                                                                                                                                            |
| celery                                       | https://github.com/celery/celery                                                    | https:/                                                                                                                                                            |
| Cerberus                                     | https://docs.python-cerberus.org/en/stable/                                         | https:/                                                                                                                                                            |
| certifi                                      | https://certifiio.readthedocs.io/en/latest/                                         | https:/                                                                                                                                                            |
| $\overline{\text{cffi}}$                     | https://github.com/python-cffi                                                      | https:/                                                                                                                                                            |
| cftime                                       | https://pypi.org/project/cftime/                                                    | https:/                                                                                                                                                            |
| chardet                                      | https://github.com/chardet/chardet                                                  | https:/                                                                                                                                                            |
| charset-normalizer                           | https://github.com/ousret/charset_normalizer                                        | $\frac{https://n>http://n>http://n>http://n>http://n>http://n>http://n>http://n/http://n/http://n/http://n/http://n/http://n/http://n/http://n/http://n/http://n/$ |
| chunkreader                                  | https://github.com/jackc/chunkreader/v2                                             | https:/                                                                                                                                                            |
| click                                        | https://palletsprojects.com/p/click/                                                | https:/                                                                                                                                                            |
| click-completion                             | https://github.com/click-contrib/click-completion                                   | https:/                                                                                                                                                            |
| click-didyoumean                             | https://github.com/click-contrib/click-didyoumean                                   | https:/                                                                                                                                                            |
| click-plugins                                | https://github.com/click-contrib/click-plugins                                      | https:/                                                                                                                                                            |
| click-repl                                   | https://github.com/untitaker/click-repl                                             | https:/                                                                                                                                                            |
| cloudpickle                                  | https://github.com/cloudpipe/cloudpickle                                            | https:/                                                                                                                                                            |
| cmake                                        | https://cmake.org/                                                                  | https:/                                                                                                                                                            |
| colorama                                     | https://github.com/tartley/colorama                                                 | https:/                                                                                                                                                            |
| comm                                         | https://github.com/ipython/comm                                                     |                                                                                                                                                                    |
|                                              | https://github.com/docker/compose                                                   | https:/                                                                                                                                                            |
| compose                                      | https://github.com/conda/conda-content-trust                                        | https:/                                                                                                                                                            |
| conda-content-trust<br>conda-libmamba-solver | https://github.com/conda/conda-libmamba-solver                                      | https:/                                                                                                                                                            |
|                                              |                                                                                     | https:/                                                                                                                                                            |
| conda-package-handling                       | https://github.com/conda/conda-package-handling                                     | https:/                                                                                                                                                            |
| conda-package-streaming                      | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/                                                                                                                                                            |
| conda-token                                  | https://anaconda.org/anaconda/conda-token                                           | https:/                                                                                                                                                            |
| confuse                                      | https://github.com/beetbox/confuse                                                  | https:/                                                                                                                                                            |
| contourpy                                    | https://github.com/contourpy/contourpy                                              | https:/                                                                                                                                                            |
| cpp-peglib                                   | https://github.com/yhirose/cpp-peglib                                               | https:/                                                                                                                                                            |
| cryptography                                 | https://github.com/pyca/cryptography                                                | https:/                                                                                                                                                            |
| cssselect2                                   | https://github.com/Kozea/cssselect2/                                                | https:/                                                                                                                                                            |
| cudatoolkit                                  | https://developer.nvidia.com/cuda-toolkit                                           | https:/                                                                                                                                                            |
| $cupy-cuda113$                               | https://cupy.dev/                                                                   | https:/                                                                                                                                                            |
| curl                                         | https://curl.se                                                                     | https:/                                                                                                                                                            |
| cycler                                       | https://github.com/matplotlib/cycler                                                | https:/                                                                                                                                                            |
| cyrus-sasl                                   | https://github.com/cyrusimap/cyrus-sasl                                             | https:/                                                                                                                                                            |
| Cython                                       | https://cython.org                                                                  | https:/                                                                                                                                                            |
| $\overline{d3}$                              | https://github.com/mbostock/d3                                                      | https:/                                                                                                                                                            |
| dataclasses                                  | https://github.com/ericvsmith/dataclasses                                           | https:/                                                                                                                                                            |
| ddsketch                                     | http://github.com/datadog/sketches-py                                               | https:/                                                                                                                                                            |
| debugpy                                      | https://aka.ms/debugpy                                                              | https:/                                                                                                                                                            |
| decimal                                      | https://github.com/shopspring/decimal                                               | https:/                                                                                                                                                            |
| decorator                                    | https://github.com/micheles/decorator                                               | https:/                                                                                                                                                            |
| deepdiff                                     | https://github.com/seperman/deepdiff                                                | https:/                                                                                                                                                            |
| deeptime                                     | https://github.com/deeptime-ml/deeptime                                             | https:/                                                                                                                                                            |
|                                              |                                                                                     |                                                                                                                                                                    |
|                                              |                                                                                     | J.                                                                                                                                                                 |
| Name of Project                              | Website                                                                             | Licen                                                                                                                                                              |
| defusedxml                                   | https://github.com/tiran/defusedxml                                                 | https:/                                                                                                                                                            |
| $di$ <sup><math>11</math></sup>              | https://github.com/uqfoundation/dill                                                | https:/                                                                                                                                                            |
| distro                                       | <b>Orion Floes</b>                                                                  | https:/                                                                                                                                                            |
| Django                                       | https://www.djangoproject.com/                                                      | https:/                                                                                                                                                            |
| django-classy-tags                           | https://github.com/django-cms/django-classy-tags                                    | https:/                                                                                                                                                            |
| django-cors-headers                          | https://github.com/adamchainz/django-cors-headers                                   | https:/                                                                                                                                                            |
| django-csp                                   | https://github.com/mozilla/django-csp                                               | https:/                                                                                                                                                            |
| django-extensions                            | https://github.com/django-extensions/django-extensions                              | https:/                                                                                                                                                            |
| django-filter                                | https://github.com/carltongibson/django-filter/tree/master                          | https:/                                                                                                                                                            |
| django-redis                                 | https://github.com/jazzband/django-redis                                            | https:/                                                                                                                                                            |
| django-taggit                                | https://github.com/jazzband/django-taggit                                           | https:/                                                                                                                                                            |
| django-taggit-serializer                     | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/                                                                                                                                                            |
| django-taggit-templatetags2                  | https://github.com/fizista/django-taggit-templatetags2                              | https:/                                                                                                                                                            |
| djangorestframework                          | https://www.django-rest-framework.org/                                              | https:/                                                                                                                                                            |
| dkh                                          | https://psicode.org/psi4manual/master/dkh.html                                      | https:/                                                                                                                                                            |
| dm-tree                                      | https://github.com/deepmind/tree                                                    | https:/                                                                                                                                                            |
| docker-py                                    | https://github.com/docker/docker-py/                                                | https:/                                                                                                                                                            |
| docopt                                       | https://docopt.org                                                                  | https:/                                                                                                                                                            |
| docutils                                     | https://docutils.sourceforge.io                                                     | https:/                                                                                                                                                            |
| drf-dynamic-fields                           | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/                                                                                                                                                            |
| editdistance                                 | https://github.com/roy-ht/editdistance                                              |                                                                                                                                                                    |
|                                              | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/                                                                                                                                                            |
| eigen                                        | https://github.com/arogozhnikov/einops                                              | https:/                                                                                                                                                            |
| einops                                       |                                                                                     | https:/                                                                                                                                                            |
| entrypoints                                  | https://github.com/takluyver/entrypoints                                            | https:/                                                                                                                                                            |
| errors                                       | https://github.com/pkg/errors                                                       | https:/                                                                                                                                                            |
| eslint-plugin                                | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                                                                                                                            |
| et_xmlfile                                   | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/                                                                                                                                                            |
| exceptiongroup                               | https://github.com/agronholm/exceptiongroup                                         | https:/                                                                                                                                                            |
| executing                                    | https://github.com/alexmojaki/executing                                             | https:/                                                                                                                                                            |
| expat                                        | https://libexpat.github.io                                                          | https:/                                                                                                                                                            |
| fastjsonschema                               | https://github.com/horejsek/python-fastjsonschema                                   | https:/                                                                                                                                                            |
| fastrlock                                    | https://github.com/scoder/fastrlock                                                 | https:/                                                                                                                                                            |
| fftw                                         | https://www.fftw.org                                                                | comm                                                                                                                                                               |
| filebuffer                                   | https://github.com/mattetti/filebuffer                                              | https:/                                                                                                                                                            |
| filelock                                     | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/                                                                                                                                                            |
| finufft                                      | https://github.com/flatironinstitute/finufft                                        | https:/                                                                                                                                                            |
| Flask                                        | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/                                                                                                                                                            |
| flatbuffers                                  | https://google.github.io/flatbuffers/                                               | https:/                                                                                                                                                            |
| flit-core                                    | https://github.com/pypa/flit                                                        | https:/                                                                                                                                                            |
| <b>FLTK</b>                                  | https://www.fltk.org/index.php                                                      | https:/                                                                                                                                                            |
| fmt                                          | https://fmt.dev/latest/index.html                                                   | https:/                                                                                                                                                            |
| font-awesome                                 | https://github.com/FortAwesome/Font-Awesome                                         | https:/                                                                                                                                                            |
| font-ttf-dejavu-sans-mono                    | https://dejavu-fonts.github.io                                                      | https:/                                                                                                                                                            |
| font-ttf-inconsolata                         | https://fonts.google.com/specimen/Inconsolata                                       | https:/                                                                                                                                                            |
| font-ttf-source-code-pro                     | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/                                                                                                                                                            |
| font-ttf-ubuntu                              | https://fonts.google.com/specimen/Ubuntu                                            | https:/                                                                                                                                                            |
| fontconfig                                   | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/                                                                                                                                                            |
| fonts-conda-ecosystem                        | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/                                                                                                                                                            |
| fonts-conda-forge                            | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/                                                                                                                                                            |
|                                              |                                                                                     |                                                                                                                                                                    |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| fonttools                                    | https://github.com/fonttools/fonttools                                              | https://                                                                                                                                                           |
| freetype                                     | https://freetype.org                                                                | https://                                                                                                                                                           |
| fribidi                                      | https://github.com/fribidi/fribidi                                                  | https://                                                                                                                                                           |
| frozendict                                   | <b>Orion Floes</b>                                                                  | https://                                                                                                                                                           |
| frozenlist                                   | https://github.com/aio-libs/frozenlist                                              | https://                                                                                                                                                           |
| fsmlite                                      | https://github.com/tkem/fsmlite                                                     | https://                                                                                                                                                           |
| fsspec                                       | https://github.com/fsspec/filesystem_spec                                           | https://                                                                                                                                                           |
| funcy                                        | https://github.com/Suor/funcy                                                       | https://                                                                                                                                                           |
| gast                                         | https://github.com/serge-sans-paille/gast/                                          | https://                                                                                                                                                           |
| gau2grid                                     | https://github.com/dgasmith/gau2grid                                                | https://                                                                                                                                                           |
| gax-go                                       | https://github.com/googleapis/gax-go/v2                                             | https://                                                                                                                                                           |
| gdk-pixbuf                                   | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https://                                                                                                                                                           |
| gemmi                                        | https://gemmi.readthedocs.io/en/latest/                                             | https://                                                                                                                                                           |
| genproto                                     | https://google.golang.org/genproto/googleapis                                       | https://                                                                                                                                                           |
| geometric                                    | https://openbase.com/python/geometric                                               | https://                                                                                                                                                           |
| giflib                                       | https://giflib.sourceforge.net                                                      | https://                                                                                                                                                           |
| glib                                         | https://docs.gtk.org/glib/                                                          | https://                                                                                                                                                           |
| <b>GLM</b> Library                           | https://github.com/g-truc/glm                                                       | https://                                                                                                                                                           |
| gls                                          | https://github.com/jtolds/gls                                                       | https://                                                                                                                                                           |
| go-cleanhttp                                 | https://github.com/hashicorp/go-cleanhttp                                           | https://                                                                                                                                                           |
| go-connections                               | https://github.com/docker/go-connections                                            | https://                                                                                                                                                           |
| go-cpio                                      | https://github.com/cavaliercoder/go-cpio                                            | https://                                                                                                                                                           |
| go-getter                                    | https://github.com/hashicorp/go-getter                                              | https://                                                                                                                                                           |
| go-homedir                                   | https://github.com/mitchellh/go-homedir                                             | https://                                                                                                                                                           |
| go-ini                                       | https://github.com/go-ini/ini                                                       | https://                                                                                                                                                           |
| go-jmespath                                  | https://github.com/jmespath/go-jmespath                                             | https://                                                                                                                                                           |
| go-junit-report                              | https://github.com/jstemmer/go-junit-report                                         | https://                                                                                                                                                           |
| go-netrc                                     | https://github.com/bgentry/go-netrc/netrc                                           | https://                                                                                                                                                           |
| go-ole                                       | https://github.com/go-ole/go-ole                                                    | https://                                                                                                                                                           |
| go-pg                                        | https://github.com/go-pg/pg                                                         | https://                                                                                                                                                           |
| go-redis                                     | https://github.com/go-redis/redis/v8                                                | https://                                                                                                                                                           |
| go-rendezvous                                | https://github.com/dgryski/go-rendezvous                                            | https://                                                                                                                                                           |
| go-safetemp                                  | https://github.com/hashicorp/go-safetemp                                            | https://                                                                                                                                                           |
| go-sysconf                                   | https://github.com/tklauser/go-sysconf                                              | https://                                                                                                                                                           |
| go-testing-interface                         | https://github.com/mitchellh/go-testing-interface                                   | https://                                                                                                                                                           |
| go-units                                     | https://github.com/docker/go-units                                                  | https://                                                                                                                                                           |
| go-version                                   | https://github.com/hashicorp/go-version                                             | https://                                                                                                                                                           |
| go-zglob                                     | https://github.com/mattn/go-zglob                                                   | https://                                                                                                                                                           |
| go.opencensus                                | https://go.opencensus.io                                                            | https://                                                                                                                                                           |
| gobrake.v2                                   | https://gopkg.in/airbrake/gobrake.v2                                                | https://                                                                                                                                                           |
| goconvey                                     | https://github.com/smartystreets/goconvey                                           | https://                                                                                                                                                           |
| golden-layout                                | https://github.com/deepstreamIO/golden-layout                                       | https://                                                                                                                                                           |
| google-auth                                  | https://google-auth.readthedocs.io/en/master/                                       | https://                                                                                                                                                           |
| google-auth-oauthlib                         | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https://                                                                                                                                                           |
| google-cloud-go                              | https://cloud.google.com/go                                                         | https://                                                                                                                                                           |
| google-cloud-go/storage                      | https://cloud.google.com/go/storage                                                 | https://                                                                                                                                                           |
| google-pasta                                 | https://github.com/google/pasta                                                     | https://                                                                                                                                                           |
| google.golang.org/api                        | https://google.golang.org/api                                                       | https://                                                                                                                                                           |
| gopsutil                                     | https://github.com/shirou/gopsutil                                                  | https://                                                                                                                                                           |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| gorilla websocket                            | https://github.com/gorilla/websocket                                                | https://                                                                                                                                                           |
| graphite2                                    | https://github.com/silnrsi/graphite                                                 | https://                                                                                                                                                           |
| graphviz                                     | https://graphviz.org/                                                               | https://                                                                                                                                                           |
| greenlet                                     | https://greenlet.readthedocs.io/en/latest/                                          | https://                                                                                                                                                           |
| groupcache                                   | https://github.com/golang/groupcache                                                | https://                                                                                                                                                           |
| grpc                                         | https://google.golang.org/grpc                                                      | https://                                                                                                                                                           |
| grpc-cpp                                     | https://github.com/grpc/grpc                                                        | https://                                                                                                                                                           |
| grpcio                                       | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https://                                                                                                                                                           |
| gtk2                                         | https://gitlab.gnome.org/GNOME/gtk                                                  | https://                                                                                                                                                           |
| gts                                          | https://sourceforge.net/projects/gts/                                               | https://                                                                                                                                                           |
| h5py                                         | https://www.h5py.org                                                                | https://                                                                                                                                                           |
| harfbuzz                                     | https://github.com/harfbuzz/harfbuzz                                                | https://                                                                                                                                                           |
| hdbscan                                      | https://hdbscan.readthedocs.io/en/latest/                                           | https://                                                                                                                                                           |
| hdf4                                         | https://www.hdfgroup.org/solutions/hdf4/                                            | https://                                                                                                                                                           |
| hdf5                                         | https://www.hdfgroup.org/solutions/hdf5/                                            | https://                                                                                                                                                           |
| he                                           | https://github.com/mathiasbynens/he                                                 | https://                                                                                                                                                           |
| html-loader                                  | https://github.com/webpack-contrib/html-loader                                      | https://                                                                                                                                                           |
| html5lib                                     | https://github.com/html5lib/html5lib-python                                         | https://                                                                                                                                                           |
| htslib                                       | https://www.htslib.org                                                              | https://                                                                                                                                                           |
| humanize                                     | https://github.com/jmoiron/humanize                                                 | https://                                                                                                                                                           |
| icu                                          | https://github.com/unicode-org/icu                                                  | https://                                                                                                                                                           |
| idna                                         | https://github.com/kjd/idna                                                         | https://                                                                                                                                                           |
| imageio                                      | https://github.com/imageio/imageio                                                  | https://                                                                                                                                                           |
| imagesize                                    | https://github.com/shibukawa/imagesize_py                                           | https://                                                                                                                                                           |
| ImmuneBuilder                                | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https://                                                                                                                                                           |
| importlib-metadata                           | https://github.com/python/importlib_metadata                                        | https://                                                                                                                                                           |
| importlib_resources                          | https://github.com/python/importlib_resources                                       | https://                                                                                                                                                           |
| InChI                                        | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https://                                                                                                                                                           |
| inflection                                   | https://github.com/jinzhu/inflection                                                | https://                                                                                                                                                           |
| ini.v1                                       | https://gopkg.in/ini.v1                                                             | https://                                                                                                                                                           |
| iniconfig                                    | https://github.com/pytest-dev/iniconfig                                             | https://                                                                                                                                                           |
| innersvg-polyfill                            | https://github.com/dnozay/innersvg-polyfill                                         | https://                                                                                                                                                           |
| intel-openmp                                 | https://github.com/hermitcore/libomp_oss                                            | https://                                                                                                                                                           |
| ipykernel                                    | https://ipython.org                                                                 | https://                                                                                                                                                           |
| ipython                                      | https://ipython.org                                                                 | https://                                                                                                                                                           |
| ipython-genutils                             | http://ipython.org                                                                  | https://                                                                                                                                                           |
| ipywidgets                                   | http://jupyter.org                                                                  | https://                                                                                                                                                           |
| isodate                                      | https://github.com/gweis/isodate/                                                   | https://                                                                                                                                                           |
| itsdangerous                                 | https://palletsprojects.com/p/itsdangerous/                                         | https://                                                                                                                                                           |
| jax                                          | https://github.com/google/jax                                                       | https://                                                                                                                                                           |
| jaxlib                                       | https://github.com/google/jax                                                       | https://                                                                                                                                                           |
| jedi                                         | https://jedi.readthedocs.io/en/latest/                                              | https://                                                                                                                                                           |
| Jinja2                                       | https://palletsprojects.com/p/jinja/                                                | https://                                                                                                                                                           |
| jmespath                                     | https://github.com/jmespath/jmespath.py                                             | https://                                                                                                                                                           |
| joblib                                       | https://joblib.readthedocs.io/en/latest/                                            | https://                                                                                                                                                           |
| jpeg                                         | https://www.ijg.org                                                                 | https://                                                                                                                                                           |
| json5                                        | https://github.com/dpranke/pyjson5                                                  | https://                                                                                                                                                           |
| jsonfield                                    | https://github.com/dmkoch/django-jsonfield/                                         | https://                                                                                                                                                           |
| jsonpatch                                    | https://github.com/stefankoegl/python-json-patch                                    | https://                                                                                                                                                           |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| jsonpickle                                   | https://github.com/jsonpickle/jsonpickle                                            | https:/                                                                                                                                                            |
| jsonpointer                                  | https://github.com/stefankoegl/python-json-pointer                                  | https:/                                                                                                                                                            |
| jsonschema                                   | https://github.com/python-jsonschema/jsonschema                                     | https:/                                                                                                                                                            |
| jsonschema-specifications                    | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:/                                                                                                                                                            |
| jstat                                        | https://github.com/jstat/jstat                                                      | https:/                                                                                                                                                            |
| jupyter-client                               | https://jupyter.org                                                                 | https:/                                                                                                                                                            |
| jupyter-core                                 | https://jupyter.org                                                                 | https:/                                                                                                                                                            |
| jupyter-events                               | https://github.com/jupyter/jupyter_events                                           | https:/                                                                                                                                                            |
| jupyter-lsp                                  | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:/                                                                                                                                                            |
| jupyter-server                               | http://jupyter.org                                                                  | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE                                                                                                 |
| jupyterlab                                   | https://github.com/jupyterlab/jupyterlab                                            | https:/                                                                                                                                                            |
| jupyterlab-pygments                          | http://jupyter.org                                                                  | https:/                                                                                                                                                            |
| jupyterlab-widgets                           | http://jupyter.org                                                                  | https:/                                                                                                                                                            |
| jupyterlab_server                            | https://github.com/jupyterlab/jupyterlab_server                                     | https:/                                                                                                                                                            |
| jupyter_client                               | http://jupyter.org                                                                  | https:/                                                                                                                                                            |
| jupyter_core                                 | http://jupyter.org                                                                  | https:/                                                                                                                                                            |
| jupyter_server                               | https://github.com/jupyter-server/jupyter_server                                    | https:/                                                                                                                                                            |
| jupyter_server_terminals                     | https://github.com/jupyter-server/jupyter_server_terminals                          | https:/                                                                                                                                                            |
| kaleido                                      | https://github.com/plotly/Kaleido                                                   | https:/                                                                                                                                                            |
| keras                                        | https://github.com/keras-team/keras                                                 | https:/                                                                                                                                                            |
| Keras-Preprocessing                          | https://github.com/keras-team/keras-preprocessing                                   | https:/                                                                                                                                                            |
| keras-tuner                                  | https://github.com/keras-team/keras-tuner                                           | https:/                                                                                                                                                            |
| keyring                                      | https://github.com/jaraco/keyring                                                   | https:/                                                                                                                                                            |
| keyutils                                     | https://github.com/sassoftware/python-keyutils                                      | https:/                                                                                                                                                            |
| kiwisolver                                   | https://kiwisolver.readthedocs.io/en/latest/                                        | https:/                                                                                                                                                            |
| kombu                                        | https://kombu.readthedocs.io                                                        | https:/                                                                                                                                                            |
| $\overline{\text{krb5}}$                     | https://web.mit.edu/kerberos/                                                       | https:/                                                                                                                                                            |
| kt-legacy                                    | https://github.com/haifeng-jin/kt-legacy                                            | https:/                                                                                                                                                            |
| lazy_loader                                  | https://github.com/scientific-python/lazy_loader                                    | https:/                                                                                                                                                            |
| lcms2                                        | https://www.littlecms.com                                                           | https:/                                                                                                                                                            |
| lerc                                         | https://github.com/Esri/lerc                                                        | https:/                                                                                                                                                            |
| libarchive                                   | http://www.libarchive.org                                                           | https:/                                                                                                                                                            |
| libblas                                      | https://www.netlib.org/blas/                                                        | https:/                                                                                                                                                            |
| libbrotlicommon                              | https://github.com/google/brotli                                                    | https:/                                                                                                                                                            |
| libbrotlidec                                 | https://github.com/google/brotli                                                    | https:/                                                                                                                                                            |
| libbrotlienc                                 | https://github.com/google/brotli                                                    | https:/                                                                                                                                                            |
| libcblas                                     | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                                                                                                                |
| libclang                                     | <b>Orion Floes</b>                                                                  | https:/                                                                                                                                                            |
| libcurl                                      | https://curl.se/libcurl/                                                            | https:/                                                                                                                                                            |
| libcxx                                       | https://github.com/llvm-mirror/libcxx                                               | https:/                                                                                                                                                            |
| libdb                                        | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:/                                                                                                                                                            |
| libdeflate                                   | https://github.com/ebiggers/libdeflate                                              | https:/                                                                                                                                                            |
| libedit                                      | https://thrysoee.dk/editline/                                                       | http://                                                                                                                                                            |
| libev                                        | https://software.schmorp.de/pkg/libev.html                                          | https:/                                                                                                                                                            |
| libffi                                       | https://github.com/libffi/libffi                                                    | https:/                                                                                                                                                            |
| libgcrypt                                    | https://gnupg.org/software/index.html                                               | https:/                                                                                                                                                            |
| libgd                                        | https://libgd.github.io                                                             | https:/                                                                                                                                                            |
| libglib                                      | https://github.com/PolMine/libglib                                                  | https:/                                                                                                                                                            |
| libiconv                                     | https://www.gnu.org/software/libiconv/                                              | https:/                                                                                                                                                            |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| libint                                       | https://tinyurl.com/yvw97wbw                                                        | https://                                                                                                                                                           |
| liblapack                                    | http://www.netlib.org/lapack/                                                       | https://                                                                                                                                                           |
| liblapacke                                   | https://anaconda.org/conda-forge/liblapacke                                         | https://                                                                                                                                                           |
| libmamba                                     | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https://                                                                                                                                                           |
| libmambapy                                   | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https://                                                                                                                                                           |
| libnetcdf                                    | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                                                                                                                           |
| libnghttp2                                   | https://github.com/nghttp2/nghttp2                                                  | https://                                                                                                                                                           |
| libopenblas                                  | https://www.openblas.net/                                                           | https://                                                                                                                                                           |
| libpng                                       | https://www.libpng.org/pub/png/libpng.html                                          | https://                                                                                                                                                           |
| libpq                                        | https://www.postgresql.org/                                                         | https://                                                                                                                                                           |
| librsvg                                      | https://gitlab.gnome.org/GNOME/librsvg                                              | https://                                                                                                                                                           |
| libsolv                                      | https://github.com/openSUSE/libsolv                                                 | https://                                                                                                                                                           |
| libssh2                                      | https://github.com/libssh2/libssh2                                                  | https://                                                                                                                                                           |
| libtiff                                      | https://www.libtiff.org/                                                            | https://                                                                                                                                                           |
| libtrust                                     | https://github.com/docker/libtrust                                                  | https://                                                                                                                                                           |
| libuuid                                      | https://sourceforge.net/projects/libuuid/                                           | https://                                                                                                                                                           |
| libuv                                        | https://github.com/libuv/libuv                                                      | https://                                                                                                                                                           |
| libwebp                                      | https://chromium.googlesource.com/?format=HTML                                      | https://                                                                                                                                                           |
| libwebp-base                                 | https://chromium.googlesource.com/?format=HTML                                      | https://                                                                                                                                                           |
| libxc                                        | https://www.tddft.org/programs/libxc/                                               | https://                                                                                                                                                           |
| libxcb                                       | https://xcb.freedesktop.org                                                         | https://                                                                                                                                                           |
| libxml2                                      | https://git.gnome.org/browse/libxml2/                                               | https://                                                                                                                                                           |
| libxmlsec1                                   | https://github.com/lsh123/xmlsec                                                    | https://                                                                                                                                                           |
| libxslt                                      | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https://                                                                                                                                                           |
| libzlib                                      | https://zlib.net                                                                    | https://                                                                                                                                                           |
| lime                                         | https://github.com/marcoter/lime                                                    | https://                                                                                                                                                           |
| lit                                          | http://llvm.org                                                                     | https://                                                                                                                                                           |
| llvm-openmp                                  | https://github.com/llvm-mirror/openmp                                               | https://                                                                                                                                                           |
| llvmlite                                     | http://llvmlite.readthedocs.io                                                      | https://                                                                                                                                                           |
| loader-utils                                 | https://github.com/webpack/loader-utils                                             | https://                                                                                                                                                           |
| logomaker                                    | https://logomaker.readthedocs.io/en/latest/                                         | https://                                                                                                                                                           |
| logrus                                       | https://github.com/sirupsen/logrus                                                  | https://                                                                                                                                                           |
| logrus-airbrake-hook.v2                      | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https://                                                                                                                                                           |
| lxml                                         | https://lxml.de                                                                     | https://                                                                                                                                                           |
| lz4-c                                        | https://www.lz4.org/                                                                | https://                                                                                                                                                           |
| markdown                                     | https://github.com/evilstreak/markdown-js                                           | https://                                                                                                                                                           |
| markdown-it-py                               | https://orionflo.es                                                                 | https://                                                                                                                                                           |
| MarkupSafe                                   | https://palletsprojects.com/p/markupsafe/                                           | https://                                                                                                                                                           |
| matplotlib                                   | https://matplotlib.org                                                              | https://                                                                                                                                                           |
| matplotlib-base                              | https://matplotlib.org                                                              | https://                                                                                                                                                           |
| matplotlib-inline                            | https://github.com/ipython/matplotlib-inline                                        | https://                                                                                                                                                           |
| mda-xdrlib                                   | https://github.com/MDAnalysis/mda-xdrlib                                            | https://                                                                                                                                                           |
| mdtraj                                       | https://www.mdtraj.org/                                                             | https://                                                                                                                                                           |
| mdurl                                        | https://orionflo.es                                                                 | https://                                                                                                                                                           |
| menuinst                                     | https://orionflo.es                                                                 | https://                                                                                                                                                           |
| mergo                                        | https://github.com/imdario/mergo                                                    | https://                                                                                                                                                           |
| mistune                                      | https://github.com/lepture/mistune                                                  | https://                                                                                                                                                           |
| mkl                                          | https://github.com/rust-math/intel-mkl-src                                          | https://                                                                                                                                                           |
| mkl-fft                                      | https://github.com/IntelPython/mkl_fft                                              | https://                                                                                                                                                           |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| mkl-random                                   | https://github.com/IntelPython/mkl_random                                           | https://                                                                                                                                                           |
| mkl-service                                  | https://github.com/IntelPython/mkl-service                                          | https://                                                                                                                                                           |
| ml-dtypes                                    | Orion Floes                                                                         | https://                                                                                                                                                           |
| molecupy                                     | https://molecupy.readthedocs.io/en/latest/                                          | https://                                                                                                                                                           |
| moment                                       | https://github.com/moment/moment                                                    | https://                                                                                                                                                           |
| moment-precise-range-plugin                  | https://github.com/codebox/moment-precise-range                                     | https://                                                                                                                                                           |
| more-itertools                               | https://github.com/more-itertools/more-itertools                                    | https://                                                                                                                                                           |
| mpiplus                                      | https://github.com/choderalab/mpiplus                                               | https://                                                                                                                                                           |
| mpmath                                       | http://mpmath.org/                                                                  | https://                                                                                                                                                           |
| mrcfile                                      | https://github.com/ccpem/mrcfile                                                    | https://                                                                                                                                                           |
| msgpack                                      | https://msgpack.org/                                                                | https://                                                                                                                                                           |
| multidict                                    | https://github.com/aio-libs/multidict                                               | https://                                                                                                                                                           |
| multierr                                     | https://go.uber.org/multierr                                                        | https://                                                                                                                                                           |
| multiprocess                                 | https://github.com/uqfoundation/multiprocess                                        | https://                                                                                                                                                           |
| munkres                                      | https://software.clapper.org/munkres/                                               | https://                                                                                                                                                           |
| myesui uuid                                  | https://github.com/myesui/uuid                                                      | https://                                                                                                                                                           |
| namex                                        | Orion Floes                                                                         | https://                                                                                                                                                           |
| nbclassic                                    | http://jupyter.org                                                                  | https://                                                                                                                                                           |
| nbclient                                     | https://jupyter.org                                                                 | https://                                                                                                                                                           |
| nbconvert                                    | https://jupyter.org                                                                 | https://                                                                                                                                                           |
| nbformat                                     | http://jupyter.org                                                                  | https://                                                                                                                                                           |
| ncurses                                      | https://invisible-island.net/ncurses/                                               | https://                                                                                                                                                           |
| nest-asyncio                                 | https://github.com/erdewit/nest_asyncio                                             | https://                                                                                                                                                           |
| netcdf-fortran                               | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                                                                                                                           |
| netCDF4                                      | http://github.com/Unidata/netcdf4-python                                            | https://                                                                                                                                                           |
| nettle                                       | https://git.lysator.liu.se/nettle/nettle                                            | https://                                                                                                                                                           |
| networkx                                     | https://networkx.org                                                                | https://                                                                                                                                                           |
| nfpm                                         | https://github.com/goreleaser/nfpm                                                  | https://                                                                                                                                                           |
| ng-tags-input                                | https://github.com/mbenford/ngTagsInput                                             | https://                                                                                                                                                           |
| ng-toast                                     | https://github.com/tameraydin/ngToast                                               | https://                                                                                                                                                           |
| ngdraggable                                  | https://github.com/fatlinesofcode/ngDraggable                                       | https://                                                                                                                                                           |
| ngVue                                        | https://github.com/ngVue/ngVue                                                      | https://                                                                                                                                                           |
| nlopt                                        | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https://                                                                                                                                                           |
| nodejs                                       | https://nodejs.org/en/                                                              | https://                                                                                                                                                           |
| nomkl                                        | https://github.com/conda-forge/nomkl-feedstock                                      | https://                                                                                                                                                           |
| notebook                                     | http://jupyter.org                                                                  | https://                                                                                                                                                           |
| notebook-shim                                | https://github.com/jupyter/notebook_shim                                            | https://                                                                                                                                                           |
| numba                                        | https://numba.pydata.org                                                            | https://                                                                                                                                                           |
| numcpus                                      | https://github.com/tklauser/numcpus                                                 | https://                                                                                                                                                           |
| numexpr                                      | https://github.com/pydata/numexpr                                                   | https://                                                                                                                                                           |
| numpy                                        | https://numpy.org                                                                   | https://                                                                                                                                                           |
| numpy-base                                   | https://numpy.org                                                                   | https://                                                                                                                                                           |
| numpydoc                                     | https://numpydoc.readthedocs.io/en/latest/index.html                                | https://                                                                                                                                                           |
| nvidia-cublas-cu11                           | https://developer.nvidia.com/cuda-zone                                              | https://                                                                                                                                                           |
| nvidia-cublas-cu12                           | https://developer.nvidia.com/cuda-zone                                              | https://                                                                                                                                                           |
| nvidia-cuda-cupti-cu11                       | https://developer.nvidia.com/cuda-zone                                              | https://                                                                                                                                                           |
| nvidia-cuda-cupti-cu12                       | https://developer.nvidia.com/cuda-zone                                              | https://                                                                                                                                                           |
| nvidia-cuda-nvrtc-cu11                       | https://developer.nvidia.com/cuda-zone                                              | https://                                                                                                                                                           |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| nvidia-cuda-nvrtc-cu12                       | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cuda-runtime-cu11                     | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cuda-runtime-cu12                     | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cudnn-cu11                            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cudnn-cu12                            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cufft-cu11                            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cufft-cu12                            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-curand-cu11                           | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-curand-cu12                           | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cusolver-cu11                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cusolver-cu12                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cusparse-cu11                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-cusparse-cu12                         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-nccl-cu11                             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-nccl-cu12                             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-nvjitlink-cu12                        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-nvtx-cu11                             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| nvidia-nvtx-cu12                             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                                                                                                            |
| Oat++                                        | https://oatpp.io/                                                                   | https:/                                                                                                                                                            |
| oauthlib                                     | https://github.com/oauthlib/oauthlib                                                | https:/                                                                                                                                                            |
| ocl-icd                                      | https://github.com/OCL-dev/ocl-icd                                                  | https:/                                                                                                                                                            |
| ocl-icd-system                               | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/                                                                                                                                                            |
| olefile                                      | https://www.decalage.info/python/olefileio                                          | https:/                                                                                                                                                            |
| OmegaFold                                    | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/                                                                                                                                                            |
| omnicanvas                                   | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/                                                                                                                                                            |
| OpenFF                                       | https://openforcefield.org/                                                         | https:/                                                                                                                                                            |
| openff-amber-ff-ports                        | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/                                                                                                                                                            |
| openff-forcefields                           | https://openforcefield.org                                                          | https:/                                                                                                                                                            |
| openff-interchange                           | https://github.com/openforcefield/openff-interchange                                | https:/                                                                                                                                                            |
| openff-models                                | https://github.com/openforcefield/openff-models                                     | https:/                                                                                                                                                            |
| openff-toolkit                               | https://openforcefield.org                                                          | https:/                                                                                                                                                            |
| openff-toolkit-base                          | https://openforcefield.org                                                          | https:/                                                                                                                                                            |
| openff-units                                 | https://github.com/openforcefield/openff-units                                      | https:/                                                                                                                                                            |
| openff-utilities                             | https://github.com/openforcefield/openff-utilities                                  | https:/                                                                                                                                                            |
| openjpeg                                     | https://github.com/uclouvain/openjpeg                                               | https:/                                                                                                                                                            |
| openldap                                     | https://www.openldap.org/software/repo.html                                         | https:/                                                                                                                                                            |
| OpenMM                                       | https://openmm.org                                                                  | https:/                                                                                                                                                            |
| openmmtools                                  | https://github.com/choderalab/openmmtools                                           | https:/                                                                                                                                                            |
| openmoltools                                 | https://github.com/choderalab/openmoltools                                          | https:/                                                                                                                                                            |
| openpyxl                                     | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                                                                                                                                            |
| openssl                                      | https://www.openssl.org                                                             | https:/                                                                                                                                                            |
| opt-einsum                                   | https://github.com/dgasmith/opt_einsum                                              | https:/                                                                                                                                                            |
| OptKing                                      | https://github.com/psi-rking/optking                                                | https:/                                                                                                                                                            |
| oscrypto                                     | https://github.com/wbond/oscrypto                                                   | https:/                                                                                                                                                            |
| overrides                                    | https://github.com/mkorpela/overrides                                               | https:/                                                                                                                                                            |
| packaging                                    | https://github.com/pypa/packaging                                                   | https:/                                                                                                                                                            |
| packmol                                      | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                                                                                                                                            |
| pandas                                       | https://pandas.pydata.org                                                           | https:/                                                                                                                                                            |
| pandocfilters                                | http://github.com/jgm/pandocfilters                                                 | https:/                                                                                                                                                            |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| panedr                                       | https://github.com/MDAnalysis/panedr                                                | https://                                                                                                                                                           |
| pango                                        | https://pango.gnome.org                                                             | https://                                                                                                                                                           |
| ParmEd                                       | https://parmed.github.io/ParmEd/html/index.html                                     | https://                                                                                                                                                           |
| parser                                       | https://github.com/typescript-eslint/typescript-eslint                              | https://                                                                                                                                                           |
| parso                                        | https://parso.readthedocs.io/en/latest/                                             | https://                                                                                                                                                           |
| pathos                                       | https://github.com/uqfoundation/pathos                                              | https://                                                                                                                                                           |
| patsy                                        | https://patsy.readthedocs.io/en/latest/                                             | https://                                                                                                                                                           |
| pbkdf2                                       | https://golang.org/x/crypto/pbkdf2                                                  | https://                                                                                                                                                           |
| pbr                                          | https://docs.openstack.org/pbr/latest/                                              | https://                                                                                                                                                           |
| pcmsolver                                    | https://pcmsolver.readthedocs.io/en/stable/                                         | https://                                                                                                                                                           |
| pcre                                         | https://www.pcre.org                                                                | https://                                                                                                                                                           |
| pcre2                                        | https://www.pcre.org                                                                | https://                                                                                                                                                           |
| pdb4amber                                    | https://github.com/Amber-MD/pdb4amber                                               | https://                                                                                                                                                           |
| pdbfixer                                     | https://github.com/openmm/pdbfixer                                                  | https://                                                                                                                                                           |
| pexpect                                      | https://pexpect.readthedocs.io/                                                     | https://                                                                                                                                                           |
| pgconn                                       | https://github.com/jackc/pgconn                                                     | https://                                                                                                                                                           |
| pgio                                         | https://github.com/jackc/pgio                                                       | https://                                                                                                                                                           |
| pgpassfile                                   | https://github.com/jackc/pgpassfile                                                 | https://                                                                                                                                                           |
| pgproto3                                     | https://github.com/jackc/pgproto3/v2                                                | https://                                                                                                                                                           |
| pgtype                                       | https://github.com/jackc/pgtype                                                     | https://                                                                                                                                                           |
| pgx                                          | https://github.com/jackc/pgx/v4                                                     | https://                                                                                                                                                           |
| phonopy                                      | https://github.com/phonopy/phonopy                                                  | https://                                                                                                                                                           |
| pickleshare                                  | https://github.com/pickleshare/pickleshare                                          | https://                                                                                                                                                           |
| Pillow                                       | https://python-pillow.org                                                           | https://                                                                                                                                                           |
| Pint                                         | https://pint.readthedocs.io/en/stable/                                              | https://                                                                                                                                                           |
| pip                                          | https://pip.pypa.io/                                                                | https://                                                                                                                                                           |
| pip-licenses                                 | https://github.com/raimon49/pip-licenses                                            | https://                                                                                                                                                           |
| pixman                                       | https://pixman.org                                                                  | https://                                                                                                                                                           |
| pkginfo                                      | https://launchpad.net/pkginfo                                                       | https://                                                                                                                                                           |
| platformdirs                                 | https://github.com/platformdirs/platformdirs                                        | https://                                                                                                                                                           |
| plotly                                       | https://plotly.com/python/                                                          | https://                                                                                                                                                           |
| plotly-orca                                  | https://github.com/plotly/orca                                                      | https://                                                                                                                                                           |
| plotly.js                                    | https://github.com/plotly/plotly.js                                                 | https://                                                                                                                                                           |
| pluggy                                       | https://pluggy.readthedocs.io/en/stable/index.html                                  | https://                                                                                                                                                           |
| pooch                                        | https://github.com/fatiando/pooch                                                   | https://                                                                                                                                                           |
| pox                                          | https://github.com/uqfoundation/pox                                                 | https://                                                                                                                                                           |
| ppft                                         | https://github.com/uqfoundation/ppft                                                | https://                                                                                                                                                           |
| pq                                           | https://github.com/lib/pq                                                           | https://                                                                                                                                                           |
| ProDy                                        | http://www.csb.pitt.edu/ProDy                                                       | https://                                                                                                                                                           |
| prometheus-client                            | https://github.com/prometheus/client_python                                         | https://                                                                                                                                                           |
| prompt-toolkit                               | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https://                                                                                                                                                           |
| protobuf                                     | https://google.golang.org/protobuf                                                  | https://                                                                                                                                                           |
| psi4                                         | https://psicode.org                                                                 | https://                                                                                                                                                           |
| psutil                                       | https://psutil.readthedocs.io/en/latest/                                            | https://                                                                                                                                                           |
| psycopg2                                     | https://psycopg.org/                                                                | https://                                                                                                                                                           |
| PTable                                       | https://github.com/kxxoling/PTable                                                  | https://                                                                                                                                                           |
| pthread-stubs                                | https://xcb.freedesktop.org                                                         | https://                                                                                                                                                           |
| ptyprocess                                   | https://ptyprocess.readthedocs.io/en/latest/                                        | https://                                                                                                                                                           |
| pure-eval                                    | http://github.com/alexmojaki/pure_eval                                              | http://                                                                                                                                                            |
|                                              |                                                                                     |                                                                                                                                                                    |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| pу                                           | https://py.readthedocs.io/en/latest/                                                | https:/                                                                                                                                                            |
| py-cpuinfo                                   | https://github.com/workhorsy/py-cpuinfo                                             | https:/                                                                                                                                                            |
| pyasn1                                       | https://github.com/etingof/pyasn1                                                   | https:/                                                                                                                                                            |
| pyasn1-modules                               | https://github.com/etingof/pyasn1-modules                                           | https:/                                                                                                                                                            |
| pybind11-abi                                 | https://github.com/pybind/pybind11                                                  | https:/                                                                                                                                                            |
| pycairo                                      | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/                                                                                                                                                            |
| pycosat                                      | https://github.com/conda/pycosat                                                    | https:/                                                                                                                                                            |
| pycparser                                    | https://github.com/eliben/pycparser                                                 | https:/                                                                                                                                                            |
| pydantic                                     | https://pydantic-docs.helpmanual.io                                                 | https:/                                                                                                                                                            |
| pydantic-core                                | https://github.com/pydantic/pydantic-core                                           | https:/                                                                                                                                                            |
| pyedr                                        | https://github.com/MDAnalysis/panedr                                                | https:/                                                                                                                                                            |
| pyEMMA                                       | http://github.com/markovmodel/PyEMMA                                                | https:/                                                                                                                                                            |
| Pygments                                     | https://pygments.org                                                                | https:/                                                                                                                                                            |
| pygraphviz                                   | https://pygraphviz.github.io                                                        | https:/                                                                                                                                                            |
| pygtop                                       | https://pygtop.readthedocs.io/en/latest/                                            | https:/                                                                                                                                                            |
| pyHanko                                      | https://github.com/MatthiasValvekens/pyHanko                                        | https:/                                                                                                                                                            |
| pyhanko-certvalidator                        | https://github.com/MatthiasValvekens/certvalidator                                  | https:/                                                                                                                                                            |
| PyJWT                                        | https://github.com/jpadilla/pyjwt                                                   | https:/                                                                                                                                                            |
| pymbar                                       | https://pymbar.org                                                                  | https:/                                                                                                                                                            |
| pyOpenSSL                                    | https://pyopenssl.org/                                                              | https:/                                                                                                                                                            |
| pyparsing                                    | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/                                                                                                                                                            |
| PyPDF3                                       | https://github.com/sfneal/PyPDF3                                                    | https:/                                                                                                                                                            |
| pyrsistent                                   | http://github.com/tobgu/pyrsistent/                                                 | https:/                                                                                                                                                            |
| pysam                                        | https://github.com/pysam-developers/pysam                                           | https:/                                                                                                                                                            |
| PySocks                                      | https://github.com/Anorov/PySocks                                                   | https:/                                                                                                                                                            |
| pytables                                     | https://www.pytables.org                                                            | https:/                                                                                                                                                            |
| python                                       | https://www.python.org/                                                             | https:/                                                                                                                                                            |
| python-bidi                                  | https://github.com/MeirKriheli/python-bidi                                          | https:/                                                                                                                                                            |
| python-constraint                            | https://github.com/python-constraint/python-constraint                              | https:/                                                                                                                                                            |
| python-dateutil                              | https://dateutil.readthedocs.io                                                     | https:/                                                                                                                                                            |
| python-json-logger                           | http://github.com/madzak/python-json-logger                                         | https:/                                                                                                                                                            |
| python-ldap                                  | https://www.python-ldap.org/                                                        | https:/                                                                                                                                                            |
| python3-saml                                 | https://github.com/onelogin/python3-saml                                            | https:/                                                                                                                                                            |
| python_abi                                   | https://github.com/conda-forge/python_abi-feedstock                                 | https:/                                                                                                                                                            |
| pytz                                         | https://pythonhosted.org/pytz                                                       | https:/                                                                                                                                                            |
| pytz-deprecation-shim                        | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/                                                                                                                                                            |
| PyWavelets                                   | https://github.com/PyWavelets/pywt                                                  | https:/                                                                                                                                                            |
| <b>PyYAML</b>                                | https://pyyaml.org/                                                                 | https:/                                                                                                                                                            |
| pyyml                                        | No longer available                                                                 | No lor                                                                                                                                                             |
| pyzmq                                        | https://pyzmq.readthedocs.io/en/latest/                                             | https:/                                                                                                                                                            |
| qcelemental                                  | https://github.com/MolSSI/QCElemental                                               | https:/                                                                                                                                                            |
| qcengine                                     | https://github.com/MolSSI/QCEngine                                                  | https:/                                                                                                                                                            |
| qrcode                                       | https://github.com/lincolnloop/python-qrcode                                        | https:/                                                                                                                                                            |
| ramda                                        | https://github.com/ramda/ramda                                                      | https:/                                                                                                                                                            |
| rapidjson                                    | https://rapidjson.org/                                                              | https:/                                                                                                                                                            |
| rdkit                                        | https://www.rdkit.org                                                               | https:/                                                                                                                                                            |
| re2                                          | https://github.com/google/re2                                                       | https:/                                                                                                                                                            |
| readme-renderer                              | https://github.com/pypa/readme_renderer                                             | https:/                                                                                                                                                            |
| redis-py                                     | https://github.com/andymccurdy/redis-py                                             | https:/                                                                                                                                                            |
|                                              |                                                                                     | -li                                                                                                                                                                |
| Name of Project                              | Website                                                                             | Licen                                                                                                                                                              |
| referencing                                  | https://github.com/python-jsonschema/referencing                                    | https:/                                                                                                                                                            |
| regex                                        | https://github.com/mrabarnett/mrab-regex                                            | https:/                                                                                                                                                            |
| reportlab                                    | https://www.reportlab.com                                                           | https:/                                                                                                                                                            |
| reproc                                       | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                                                                                                                            |
| reproc-cpp                                   | https://github.com/DaanDeMeyer/reproc                                               | https:/                                                                                                                                                            |
| requests                                     | https://requests.readthedocs.io                                                     | https:/                                                                                                                                                            |
| requests-oauthlib                            | https://github.com/requests/requests-oauthlib                                       | https:/                                                                                                                                                            |
| requests-toolbelt                            | https://toolbelt.readthedocs.org                                                    | https:/                                                                                                                                                            |
| resumable                                    | https://github.com/stevvooe/resumable                                               | https:/                                                                                                                                                            |
| retrying                                     | https://github.com/rholder/retrying                                                 | https:/                                                                                                                                                            |
| rfc3339-validator                            | https://github.com/naimetti/rfc3339-validator                                       | https:/                                                                                                                                                            |
| rfc3986                                      | https://rfc3986.readthedocs.io/en/latest/                                           | https:/                                                                                                                                                            |
| rfc3986-validator                            | https://github.com/naimetti/rfc3986-validator                                       | https:/                                                                                                                                                            |
| rich                                         | <b>Orion Floes</b>                                                                  | https:/                                                                                                                                                            |
| rpds-py                                      | https://github.com/crate-py/rpds                                                    | https:/                                                                                                                                                            |
| rpmpack                                      | https://github.com/google/rpmpack                                                   | https:/                                                                                                                                                            |
| rsa                                          | https://stuvel.eu/rsa                                                               | https:/                                                                                                                                                            |
| ruamel-yaml                                  | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/                                                                                                                                                            |
| ruamel.yaml.clib                             | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/                                                                                                                                                            |
| s3transfer                                   | https://github.com/boto/s3transfer                                                  | https:/                                                                                                                                                            |
| sasl                                         | https://mellium.im/sasl                                                             | https:/                                                                                                                                                            |
| scikit-gstat                                 | https://mmaelicke.github.io/scikit-gstat/                                           | https:/                                                                                                                                                            |
| scikit-image                                 | https://scikit-image.org                                                            | https:/                                                                                                                                                            |
| scikit-learn                                 | https://scikit-learn.org/stable/                                                    | https:/                                                                                                                                                            |
| scikit-learn-extra                           | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/                                                                                                                                                            |
| scipy                                        | https://scipy.org                                                                   | https:/                                                                                                                                                            |
| seaborn                                      | https://seaborn.pydata.org                                                          | https:/                                                                                                                                                            |
| seaborn-base                                 | https://seaborn.pydata.org                                                          | https:/                                                                                                                                                            |
| semver                                       | https://github.com/Masterminds/semver/v3                                            | https:/                                                                                                                                                            |
| Send2Trash                                   | https://github.com/arsenetar/send2trash                                             | https:/                                                                                                                                                            |
| setuptools                                   | https://github.com/pypa/setuptools                                                  | https:/                                                                                                                                                            |
| setuptools-scm                               | https://github.com/pypa/setuptools_scm/                                             | https:/                                                                                                                                                            |
| sh                                           | https://github.com/amoffat/sh                                                       | https:/                                                                                                                                                            |
| shellingham                                  | https://github.com/sarugaku/shellingham                                             | https:/                                                                                                                                                            |
| simint                                       | https://www.bennyp.org/research/simint/                                             |                                                                                                                                                                    |
| six                                          | https://github.com/benjaminp/six                                                    | https:/<br>https:/                                                                                                                                                 |
| smirnoff99frosst                             | https://github.com/openforcefield/smirnoff99frosst                                  | https:/                                                                                                                                                            |
| snappy                                       | https://github.com/google/snappy                                                    | https:/                                                                                                                                                            |
| sniffio                                      | https://github.com/python-trio/sniffio                                              | https:/                                                                                                                                                            |
| snowballstemmer                              | https://github.com/snowballstem/snowball                                            |                                                                                                                                                                    |
|                                              | https://github.com/facelessuser/soupsieve                                           | https:/                                                                                                                                                            |
| soupsieve                                    |                                                                                     | https:/                                                                                                                                                            |
| spglib                                       | <b>Orion Floes</b>                                                                  | https:/                                                                                                                                                            |
| sphinx                                       | https://github.com/sphinx-doc/sphinx                                                | https:/                                                                                                                                                            |
| sphinxcontrib-applehelp                      | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/                                                                                                                                                            |
| sphinxcontrib-devhelp                        | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/                                                                                                                                                            |
| sphinxcontrib-htmlhelp                       | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/                                                                                                                                                            |
| sphinxcontrib-jsmath                         | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/                                                                                                                                                            |
| sphinxcontrib-qthelp                         | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/                                                                                                                                                            |
| sphinxcontrib-serializinghtml                | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/                                                                                                                                                            |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| SQLAlchemy                                   | https://www.sqlalchemy.org                                                          | https://                                                                                                                                                           |
| sqlite                                       | https://sqlite.org/index.html                                                       | https://                                                                                                                                                           |
| sqlparse                                     | https://github.com/andialbrecht/sqlparse                                            | https://                                                                                                                                                           |
| stack-data                                   | http://github.com/alexmojaki/stack_data                                             | https://                                                                                                                                                           |
| starfile                                     | https://github.com/alisterburt/starfile                                             | https://                                                                                                                                                           |
| statsmodels                                  | https://github.com/statsmodels/statsmodels                                          | https://                                                                                                                                                           |
| structlog                                    | https://www.structlog.org/                                                          | https://                                                                                                                                                           |
| svglib                                       | https://github.com/deeplook/svglib                                                  | https://                                                                                                                                                           |
| sympy                                        | https://sympy.org                                                                   | https://                                                                                                                                                           |
| tables                                       | https://www.pytables.org/                                                           | https://                                                                                                                                                           |
| tabulate                                     | https://github.com/astanin/python-tabulate                                          | https://                                                                                                                                                           |
| tbb                                          | https://github.com/oneapi-src/oneTBB                                                | https://                                                                                                                                                           |
| tenacity                                     | https://github.com/jd/tenacity                                                      | https://                                                                                                                                                           |
| tensorboard                                  | https://github.com/tensorflow/tensorboard                                           | https://                                                                                                                                                           |
| tensorboard-data-server                      | https://github.com/tensorflow/tensorboard                                           | https://                                                                                                                                                           |
| tensorboard-plugin-wit                       | https://github.com/pair-code/what-if-tool                                           | https://                                                                                                                                                           |
| tensorflow                                   | https://github.com/tensorflow/tensorflow                                            | https://                                                                                                                                                           |
| tensorflow-estimator                         | https://github.com/tensorflow/estimator                                             | https://                                                                                                                                                           |
| tensorflow-io-gcs-filesystem                 | <b>Orion Floes</b>                                                                  | https://                                                                                                                                                           |
| tensorflow-probability                       | https://github.com/tensorflow/probability                                           | https://                                                                                                                                                           |
| termcolor                                    | https://github.com/hugovk/termcolor                                                 | https://                                                                                                                                                           |
| terminado                                    | https://github.com/jupyter/terminado                                                | https://                                                                                                                                                           |
| testpath                                     | https://github.com/jupyter/testpath                                                 | https://                                                                                                                                                           |
| textangular                                  | https://github.com/fraywing/textAngular                                             | https://                                                                                                                                                           |
| tf_keras                                     | <b>Orion Floes</b>                                                                  | https://                                                                                                                                                           |
| threadpoolctl                                | https://github.com/joblib/threadpoolctl                                             | https://                                                                                                                                                           |
| three                                        | https://github.com/mrdoob/three.js                                                  | https://                                                                                                                                                           |
| tifffile                                     | https://github.com/cgohlke/tifffile/                                                | https://                                                                                                                                                           |
| tinycss2                                     | https://github.com/Kozea/tinycss2/                                                  | https://                                                                                                                                                           |
| tinyxml2                                     | https://github.com/leethomason/tinyxml2                                             | https://                                                                                                                                                           |
| tk                                           | https://www.tcl.tk/                                                                 | https://                                                                                                                                                           |
| toml                                         | https://github.com/toml-lang/toml                                                   | https://                                                                                                                                                           |
| tomli                                        | https://github.com/hukkin/tomli                                                     | https://                                                                                                                                                           |
| toolz                                        | https://github.com/pytoolz/toolz                                                    | https://                                                                                                                                                           |
| torch                                        | https://pytorch.org/                                                                | https://                                                                                                                                                           |
| tornado                                      | https://www.tornadoweb.org                                                          | https://                                                                                                                                                           |
| tqdm                                         | https://github.com/tqdm/tqdm                                                        | https://                                                                                                                                                           |
| tracy                                        | https://github.com/gear-genomics/tracy                                              | https://                                                                                                                                                           |
| traitlets                                    | https://github.com/ipython/traitlets                                                | https://                                                                                                                                                           |
| triton                                       | https://github.com/openai/triton/                                                   | https://                                                                                                                                                           |
| truststore                                   | <b>Orion Floes</b>                                                                  | https://                                                                                                                                                           |
| ts-jest                                      | https://github.com/kulshekhar/ts-jest                                               | https://                                                                                                                                                           |
| ts-loader                                    | https://github.com/TypeStrong/ts-loader                                             | https://                                                                                                                                                           |
| twine                                        | https://github.com/pypa/twine                                                       | https://                                                                                                                                                           |
| twinj uuid                                   | https://github.com/twinj/uuid                                                       | https://                                                                                                                                                           |
| types                                        | https://github.com/babel/babel                                                      | https://                                                                                                                                                           |
| typescript                                   | https://github.com/Microsoft/TypeScript                                             | https://                                                                                                                                                           |
| typing_extensions                            | https://github.com/python/typing                                                    | https://                                                                                                                                                           |
| tzdata                                       | https://github.com/python/tzdata                                                    | https://                                                                                                                                                           |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| tzlocal                                      | https://github.com/regebro/tzlocal                                                  | https://                                                                                                                                                           |
| umi-tools                                    | https://github.com/CGATOxford/UMI-tools                                             | https://                                                                                                                                                           |
| unicodedata2                                 | https://github.com/fonttools/unicodedata2                                           | https://                                                                                                                                                           |
| uritools                                     | https://github.com/tkem/uritools/                                                   | https://                                                                                                                                                           |
| urllib3                                      | https://urllib3.readthedocs.io/                                                     | https://                                                                                                                                                           |
| vine                                         | https://github.com/celery/vine                                                      | https://                                                                                                                                                           |
| vue                                          | https://github.com/vuejs/vue                                                        | https://                                                                                                                                                           |
| wcwidth                                      | https://github.com/jquast/wcwidth                                                   | https://                                                                                                                                                           |
| webencodings                                 | https://github.com/gsnedders/python-webencodings                                    | https://                                                                                                                                                           |
| websocket-client                             | https://github.com/websocket-client/websocket-client.git                            | https://                                                                                                                                                           |
| Werkzeug                                     | https://palletsprojects.com/p/werkzeug/                                             | https://                                                                                                                                                           |
| westpa                                       | Orion Floes                                                                         | http://                                                                                                                                                            |
| wheel                                        | https://github.com/pypa/wheel                                                       | https://                                                                                                                                                           |
| widgetsnbextension                           | https://github.com/jupyter-widgets/ipywidgets#readme                                | https://                                                                                                                                                           |
| wrapt                                        | https://github.com/GrahamDumpleton/wrapt                                            | https://                                                                                                                                                           |
| wsutil                                       | https://github.com/yhat/wsutil                                                      | https://                                                                                                                                                           |
| x/lint                                       | https://golang.org/x/lint                                                           | https://                                                                                                                                                           |
| x/mod                                        | https://golang.org/x/mod/semver                                                     | https://                                                                                                                                                           |
| x/net                                        | https://golang.org/x/net                                                            | https://                                                                                                                                                           |
| x/oauth2                                     | https://golang.org/x/oauth2                                                         | https://                                                                                                                                                           |
| x/sys                                        | https://golang.org/x/sys                                                            | https://                                                                                                                                                           |
| x/text                                       | https://golang.org/x/text                                                           | https://                                                                                                                                                           |
| x/tools                                      | https://golang.org/x/tools                                                          | https://                                                                                                                                                           |
| x/xerrors                                    | https://golang.org/x/xerrors                                                        | https://                                                                                                                                                           |
| xhtml2pdf                                    | https://github.com/xhtml2pdf/xhtml2pdf                                              | https://                                                                                                                                                           |
| xlrd                                         | https://github.com/python-excel/xlrd                                                | https://                                                                                                                                                           |
| xmlsec                                       | https://github.com/mehcode/python-xmlsec                                            | https://                                                                                                                                                           |
| xmltodict                                    | https://github.com/martinblech/xmltodict                                            | https://                                                                                                                                                           |
| xorg-kbproto                                 | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https://                                                                                                                                                           |
| xorg-libice                                  | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https://                                                                                                                                                           |
| xorg-libsm                                   | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https://                                                                                                                                                           |
| xorg-libx11                                  | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https://                                                                                                                                                           |
| xorg-libxau                                  | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https://                                                                                                                                                           |
| xorg-libxdmcp                                | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https://                                                                                                                                                           |
| xorg-libxext                                 | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https://                                                                                                                                                           |
| xorg-libxrender                              | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https://                                                                                                                                                           |
| xorg-libxt                                   | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https://                                                                                                                                                           |
| xorg-renderproto                             | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https://                                                                                                                                                           |
| xorg-xextproto                               | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https://                                                                                                                                                           |
| xorg-xproto                                  | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https://                                                                                                                                                           |
| xxhash                                       | https://github.com/cespare/xxhash/v2                                                | https://                                                                                                                                                           |
| xz                                           | https://github.com/ulikunitz/xz                                                     | https://                                                                                                                                                           |
| yaml                                         | https://pyyaml.org/                                                                 | https://                                                                                                                                                           |
| yaml-cpp                                     | https://github.com/jbeder/yaml-cpp                                                  | https://                                                                                                                                                           |
| yaml.v2                                      | https://gopkg.in/yaml.v2                                                            | https://                                                                                                                                                           |
| yaml.v3                                      | https://gopkg.in/yaml.v3                                                            | https://                                                                                                                                                           |
| yarl                                         | https://github.com/aio-libs/yarl/                                                   | https://                                                                                                                                                           |
| yaspin                                       | https://github.com/pavdmyt/yaspin                                                   | https://                                                                                                                                                           |
| yfiles                                       | https://www.yworks.com/products/yfiles                                              | comm                                                                                                                                                               |
| Name of Project                              | Website                                                                             | License                                                                                                                                                            |
| yml                                          | https://pypi.org/project/yml/                                                       | N/A                                                                                                                                                                |
| zap                                          | https://go.uber.org/zap                                                             | https:/                                                                                                                                                            |
| zipp                                         | https://github.com/jaraco/zipp                                                      | https:/                                                                                                                                                            |
| zlib                                         | https://zlib.net/                                                                   | https:/                                                                                                                                                            |
| zstandard                                    | https://github.com/indygreg/python-zstandard                                        | https:/                                                                                                                                                            |
| zstd                                         | https://facebook.github.io/zstd/                                                    | https:/                                                                                                                                                            |
| _libgcc_mutex                                | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:/                                                                                                                                                            |
| _openmp_mutex                                | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:/                                                                                                                                                            |

## **9.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

### 9.1.1 GCC RUNTIME LIBRARY EXCEPTION

```
Version 3.1, 31 March 2009
Copyright © 2009 Free Software Foundation, Inc. http://fsf.org/
Everyone is permitted to copy and distribute verbatim copies of this license document,
\rightarrow but changing it is not allowed.
This GCC Runtime Library Exception ("Exception") is an additional permission under.
\rightarrowsection 7 of the GNU General Public License,
version 3 ("GPLv3"). It applies to a given file (the "Runtime Library") that bears a
→notice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

### 9.1.2 GNU GENERAL PUBLIC LICENSE

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

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page) 9.1. GCC

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

### See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# C

CheckAtomTypes OESzmap:: OESzmapEngine, 18 Clear OESzmap:: OESzmapResults, 21 Constructors OESzmap:: OESzmapEngine, 17 OESzmap:: OESzmapEngineOptions, 19 OESzmap:: OESzmapResults, 21

# F

environment variable OE LICENSE, 1 Example Code szmapbestorientations.py, 12 szmapenergies.py, 10

# G

GetComponent OESzmap:: OESzmapResults, 21 GetContext OESzmap:: OESzmapEngine, 18 GetCoords OESzmap:: OESzmapResults, 22 GetEnsembleValue OESzmap:: OESzmapResults, 22 GetMaskCutoff OESzmap:: OESzmapEngineOptions, 19 GetOptions OESzmap:: OESzmapEngine, 18 GetProbabilities OESzmap:: OESzmapResults, 22 GetProbabilityOrder OESzmap:: OESzmapResults, 22 GetProbe OESzmap:: OESzmapEngineOptions, 19 GetProbeMol OESzmap:: OESzmapEngineOptions, 19 GetProbeName OESzmap:: OESzmapEngineOptions, 20

# $\mathsf{N}$

NumOrientations OESzmap:: OESzmapEngineOptions, 20 OESzmap:: OESzmapResults, 23

# O

OE LICENSE, 1 OESzmap:: OECalcSzmapResults, 29 OESzmap:: OECalcSzmapValue, 30 OESzmap:: OEComponent, 25 OESzmap:: OEComponent:: Interaction, 26 OESzmap:: OEComponent:: NumTypes, 27 OESzmap:: OEComponent:: ProbeBurial, 27 OESzmap:: OEComponent:: PSolv, 26 OESzmap:: OEComponent:: VDW, 26 OESzmap:: OEComponent:: WSolv, 26 OESzmap:: OEEnsemble, 27 OESzmap:: OEEnsemble:: CalcPoint, 28 OESzmap:: OEEnsemble:: Default, 29 OESzmap:: OEEnsemble:: DeltaG, 29 OESzmap:: OEEnsemble:: DeltaH, 29 OESzmap:: OEEnsemble:: Interaction, 27 OESzmap:: OEEnsemble:: InteractionPlusVDW, 28 OESzmap:: OEEnsemble:: Mask, 28 OESzmap:: OEEnsemble:: NeutralDeltaG, 28 OESzmap:: OEEnsemble:: NeutralDeltaH, 28 OESzmap:: OEEnsemble:: NeutralDiffDeltaG, 28 OESzmap:: OEEnsemble:: NeutralDiffDeltaH,  $28$ OESzmap:: OEEnsemble:: NeutralDiffTDeltaS,  $28$ OESzmap:: OEEnsemble:: NeutralTDeltaS. 28 OESzmap:: OEEnsemble:: NumTypes, 29 OESzmap:: OEEnsemble:: OrderParam, 28 OESzmap:: OEEnsemble:: ProbeBurial, 27 OESzmap:: OEEnsemble:: PSolv, 27 OESzmap:: OEEnsemble:: TDeltaS, 29 OESzmap:: OEEnsemble:: VacuumDiffDeltaG, 29

```
OESzmap:: OEEnsemble:: VacuumDiffDeltaH.
       29
OESzmap:: OEEnsemble:: VDW, 27
OESzmap:: OEEnsemble:: WSolv, 27
OESzmap:: OEGetComponentName, 30
OESzmap:: OEGetEnsembleName, 30
OESzmap:: OEIsClashing, 30
OESzmap:: OESzmapEngine, 17
   CheckAtomTypes, 18
   Constructors, 17
   GetContext, 18
   GetOptions, 18
   operator bool, 17
   operator=, 17
   SetContext, 18
OESzmap:: OESzmapEngineOptions, 18
   Constructors, 19
   GetMaskCutoff, 19
   GetProbe. 19
   GetProbeMol, 19
   GetProbeName, 20
   NumOrientations, 20
   operator=, 19
   SetMaskCutoff, 20
   SetProbe, 20
OESzmap:: OESzmapGetArch, 31
OESzmap:: OESzmapGetLicensee, 31
OESzmap:: OESzmapGetPlatform, 31
OESzmap:: OESzmapGetRelease, 31
OESzmap:: OESzmapGetSite, 32
OESzmap:: OESzmapGetVersion, 32
OESzmap:: OESzmapIsLicensed, 32
OESzmap:: OESzmapResults, 20
   Clear, 21
   Constructors, 21
   GetComponent, 21
   GetCoords, 22
   GetEnsembleValue, 22
   GetProbabilities, 22
   GetProbabilityOrder, 22
   NumOrientations, 23
   operator bool, 21
   operatorerator =, 21
   PlaceNewAtom, 23
   PlaceProbeMol, 23
   PlaceProbeSet, 24
operator bool
   OESzmap:: OESzmapEngine, 17
   OESzmap:: OESzmapResults, 21
operator=
   OESzmap:: OESzmapEngine, 17
   OESzmap:: OESzmapEngineOptions, 19
   OESzmap:: OESzmapResults, 21
```

## P

```
PlaceNewAtom
   OESzmap:: OESzmapResults, 23
PlaceProbeMol
   OESzmap:: OESzmapResults, 23
PlaceProbeSet
   OESzmap:: OESzmapResults, 24
```

# S

```
SetContext
   OESzmap:: OESzmapEngine, 18
SetMaskCutoff
   OESzmap:: OESzmapEngineOptions, 20
SetProbe
   OESzmap:: OESzmapEngineOptions, 20
szmapbestorientations.py
   Example Code, 12
szmapenergies.py
   Example Code, 10
```