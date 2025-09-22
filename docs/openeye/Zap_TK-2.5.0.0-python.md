![](_page_0_Picture_0.jpeg)

Zap TK - Python Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1                                   | <b>Theory and Examples</b>       | 1 |
|-------------------------------------|----------------------------------|---|
| 1.1                                 | The What of Zap                  | 1 |
| 1.2                                 | The Why of Zap                   | 1 |
| 1.3                                 | The Way of Zap                   |   |
| 1.3.1                               | Partial Charges and Atomic Radii | 1 |
| 1.3.2                               | Grids                            | 1 |
| 1.3.3                               | Atom Potentials                  | 1 |
| 1.3.4                               | Solvation Energies: PBSA         | 1 |
| 1.3.5                               | Binding Energies                 | 1 |
| 1.3.6                               | Focusing                         | 1 |
| 1.3.7                               | Gradients/Forces                 | 2 |
| 1.3.8                               | Electrostatic Similarity         | 2 |
| 2                                   | <b>API</b>                       | 2 |
| 2.1                                 | OEPB Classes                     | 2 |
| 2.1.1                               | OEArea                           | 2 |
| 2.1.2                               | GetArea                          | 2 |
| 2.1.3                               | GetMethod                        | 2 |
| 2.1.4                               | GetUseHydrogens                  | 2 |
| 2.1.5                               | SetMethod                        | 2 |
| 2.1.6                               | SetUseHydrogens                  | 2 |
| 2.1.7                               | OEBind                           | 2 |
| 2.1.8                               | OEBindResults                    | 3 |
| 2.1.9                               | OEET                             | 3 |
| 2.1.10                              | OESimpleBindResults              | 3 |
| 2.1.11                              | OEZap                            | 3 |
| 2.2                                 | OEPB Constants                   | 4 |
| 2.2.1                               | OEAreaMethod                     | 4 |
| 2.2.2                               | OEZapDielectricModel             | 4 |
| 2.3                                 | OEPB Functions                   | 4 |
| 2.3.1                               | OECalculateCoulombicBinding      | 4 |
| 2.3.2                               | OECoulombicAtomPotentials        | 4 |
| 2.3.3                               | OECoulombicSelfEnergy            | 4 |
| 2.3.4                               | OEMakeETGrid                     | 4 |
| 2.3.5                               | OEZapBind                        | 4 |
| 2.3.6                               | OEZapGetArch                     | 4 |
| 2.3.7                               | OEZapGetLicensee                 | 4 |
| 2.3.8                               | OEZapGetPlatform                 | 4 |
| 2.3.9                               | OEZapGetRelease                  | 4 |
| 2.3.10                              | OEZapGetSite                     | 4 |
| 2.3.11 OEZapGetVersion              | 4                                |   |
| <b>3 Release History</b>            | 4                                |   |
| 3.1  Zap TK 2.5.0                   | 4                                |   |
| 3.2  Zap TK 2.4.7                   | 4                                |   |
| 3.3  Zap TK 2.4.6                   | 4                                |   |
| 3.3.1 New features                  | 4                                |   |
| 3.4  Zap TK 2.4.5                   | 4                                |   |
| 3.5  Zap TK 2.4.4                   | 4                                |   |
| 3.6  Zap TK 2.4.3                   | 4                                |   |
| 3.7  Zap TK 2.4.2                   | 4                                |   |
| 3.8  Zap TK 2.4.1                   | 4                                |   |
| 3.9  Zap TK 2.4.0                   | 4                                |   |
| 3.10 Zap TK 2.3.7                   | 4                                |   |
| 3.11 Zap TK 2.3.6                   | 4                                |   |
| 3.11.1 Python-specific changes      | 4                                |   |
| 3.12 Zap TK 2.3.5                   | 4                                |   |
| 3.13 Zap TK 2.3.4                   | 4                                |   |
| 3.14 Zap TK 2.3.3                   | 4                                |   |
| 3.15 Zap TK 2.3.2                   | 4                                |   |
| 3.16 Zap TK 2.3.1                   | 4                                |   |
| 3.17 Zap TK 2.3.0                   | 4                                |   |
| 3.18 Zap TK 2.2.7                   | 4                                |   |
| 3.18.1 Minor bug fixes              | 4                                |   |
| 3.19 Zap TK 2.2.6                   | 4                                |   |
| 3.19.1 Minor bug fixes              | 4                                |   |
| 3.19.2 Documentation changes        | 4                                |   |
| 3.20 Zap TK 2.2.5                   | 4                                |   |
| 3.20.1 Major bug fixes              | 4                                |   |
| 3.21 Zap TK 2.2.4                   | 4                                |   |
| 3.22 Zap TK 2.2.3                   | 4                                |   |
| 3.22.1 Documentation fixes          | 4                                |   |
| 3.23 Zap TK 2.2.2                   | 4                                |   |
| 3.23.1 Minor bug fixes              | 4                                |   |
| 3.23.2 Documentation fixes          | 4                                |   |
| 3.24 Zap TK 2.2.1                   | 4                                |   |
| 3.24.1 Major Bug Fixes              | 4                                |   |
| 3.24.2 Documentation fixes          | 4                                |   |
| 3.25 Zap TK 2.2.0                   | 4                                |   |
| 3.25.1 Minor bug fixes              | 4                                |   |
| 3.26 Zap TK 2.1.7                   | 4                                |   |
| 3.27 Zap TK 2.1.6                   | 4                                |   |
| 3.27.1 New features                 | 4                                |   |
| 3.27.2 Minor bug fixes              | 4                                |   |
| 3.27.3 Documentation fixes          | 4                                |   |
| 3.28 Zap TK 2.1.5                   | 4                                |   |
| 3.28.1 Documentation fixes          | 4                                |   |
| 3.29 Zap TK 2.1.4                   | 4                                |   |
| 3.30 Zap TK 2.1.3                   | 5                                |   |
| 3.31 Zap TK 2.1.2                   | 5                                |   |
| 3.31.1 New features                 | 5                                |   |
| 3.31.2 Bug fixes                    | 5                                |   |
| 3.32 Zap TK 2.1.1                   | 5                                |   |
| 3.32.1 Bug fixes                    | 5                                |   |
| 3.32.2 Minor bug fixes              | 50                               |   |
| 3.33 Zap TK 2.1.0                   | 50                               |   |
| 3.33.1 New features                 | 50                               |   |
| 3.33.2 Bug fixes                    | 50                               |   |
| 3.34 Zap TK 2.0.0                   | 51                               |   |
| 3.34.1 New features                 | 51                               |   |
| <b>4 Copyright and Trademarks</b>   | 53                               |   |
| <b>5 Sample Code</b>                | 55                               |   |
| <b>6 Citation</b>                   | 57                               |   |
| 6.1 Orion® Floes                    | 57                               |   |
| 6.2 Toolkits and Applications       | 57                               |   |
| 6.3 OpenEye Web Services            | 59                               |   |
| <b>7 Technology Licensing</b>       | 61                               |   |
| 7.1 GCC                             | 76                               |   |
| 7.1.1 GCC RUNTIME LIBRARY EXCEPTION | 76                               |   |
| 7.1.2 GNU GENERAL PUBLIC LICENSE    | 78                               |   |
| <b>Index</b>                        | 91                               |   |

### **CHAPTER**

# **THEORY AND EXAMPLES**

## 1.1 The What of Zap

"A Smooth Permittivity Function for Poisson-Boltzmann Solvation Methods," J. Andrew Grant, Barry T. Pickup and Anthony Nicholls, J. Comp. Chem, Vol 22, No.6, pgs 608-640, April 2001.

ZAP is, at its heart, a Poisson-Boltzmann (PB) solver. The Poisson equation describes how electrostatic fields change in a medium of varying dielectric, such as an organic molecule in water. The Boltzmann bit adds in the effect of mobile charge, e.g. salt. PB is an effective way to simulate the effects of water in biological systems. It relies on a charge description of a molecule, the designation of low (molecular) and high (solvent) dielectric regions and a description of an ion-accessible volume and produces a grid of electrostatic potentials. From this, transfer energies between different solvents, binding energies, pKa shifts, pI's, solvent forces, electrostatic descriptors, solvent dipole moments, surface potentials and dielectric focusing can all be calculated. As electrostatics is one of the two principal components of molecular interaction (the other, of course, being shape), ZAP is OpenEye's attempt to get it right.

## 1.2 The Why of Zap

ZAP happened by surprise. It had always been at the back of my mind that Something Should Be Done About DelPhi, the program written at Columbia University in the lab of Barry Honig by Barry, Kim Sharp, Mike Gilson, Shridhara Shridharan and me. While a very useful program, it was getting harder and harder to develop, partly because it was written in FORTRAN (not that there's anything wrong with that), partly because that's just the way academic code is. We don't know how to program but we want answers and we want them now.

ZAP really came about because of Andrew Grant. Andy was in the Scheraga lab struggling, as most of us do, with the nonlinear PB equation. He left to join AstraZeneca in 1993 but we kept in contact. In '95, he and Barry Pickup at the University of Sheffield published a remarkable paper (J. Comp. Chem.). They reported the hard-sphere volume of a molecule could be calculated to 0.1% accuracy by using atom-centered Gaussians. The correspondence between a discrete and a smooth, continuous function was nothing short of remarkable. Since the dielectric approach of PB is essentially volumetric because molecules are low-dielectric and solvent high, it occurred to us that this was the bedrock on which to build a new PB approach. That approach became ZAP.

There were several reasons to be excited about the Gaussian based approach. A smooth-function dielectric mapped onto a grid has few of the numerical problems plaguing DelPhi - instability with respect to grid placement, sensitivity to grid spacing. Also it is an interesting alternative physical model to most PB implementations. Typically it is assumed that the dielectric changes from molecular to solvent "discretely," or infinitely fast. Why? As there was no experimental information on the variation of dielectric it was the simplest assumption and also the simplest to implement. As is often the way with a successful scientific approach, these early decisions become ossified over time.

Another ossification is the choice of molecular surface as the dielectric threshold, as first proposed by BH (J. Phys. Chem). It is not a bad choice. If a water molecule is excluded from some crevice of a molecule that ought to be reflected in a lower dielectric in the crevice: a molecular surface-delimited volume reflects this where an atomic surface does not. There was also a numerical issue. When Mike Gilson first applied DelPhi to proteins (PROTEINS: Vol 17...), the atomic approach would place grid points randomly in tiny solvent crevices. Moving the protein relative to the grid shuffled the grid representation of the protein interior leading to large, unphysical changes in energy. The molecular surface removed these crevices unless they were large enough to fit a whole water molecule, in which case a high dielectric assignment was not unreasonable.

In retrospect, however, the molecular surface is a terrible choice! It's difficult to calculate and unstable with respect to small displacements of atoms or to the choice of a radius for water. And there is always the question of what dielectric should be assigned to the volume that lies between the molecular and the atomic surfaces.

The Gaussian approach answers several of the physical objections. First and foremost, the dielectric varies smoothly from interior to exterior. Although we made no attempt to correlate this variation with empirical evidence, choosing instead to match our method to DelPhi energies, the variation of polarizability over a span of about one Angstrom is physically appealing. Secondly, we achieve much of the crevice exclusion that the molecular surface produces. Because the Gaussian functions spread out beyond the hard sphere radius of each atom, a crevice receives density contributions from all neighboring atoms, lowering its dielectric to molecular levels. Thirdly, we do not see water "pops", those large changes in dielectric from small atomic displacements (or, worse, small changes of the protein placement on the grid) that occur in active sites. The Gaussian effectively interpolates between water absence and presence.

An advantage to this approach that we did not anticipate was its correspondence to DelPhi when applied to proteins. We parameterized the dielectric variation in ZAP so that it agrees with DelPhi for small molecules ("we" meaning Christine Kitchen's heroic work for her Ph.D. thesis). Given that the difference between the molecular surface and Gaussian model will be much larger for proteins with concavities, crevices and internal water pockets, we wondered how well the two would agree. The remarkable finding was that ZAP applied to proteins looks like DelPhi with twice the polarizability: ZAP with internal dielectric set to 2.0 looks like DelPhi set to 4.0. Why is this useful? Because there is circumstantial and theoretical evidence that 4.0 is a good dielectric to use with DelPhi for proteins, but that always left a loose thread in applying the method to protein-drug interactions - small molecules should have a dielectric of 2.0, proteins 4.0, but DelPhi only allows you to choose one internal dielectric. With ZAP it appears you get the best of both worlds. Protein and drug are set to internal dielectrics of 2.0 and because the protein is a little more "hydrated" in ZAP, it acts like the dielectric is set to 4.0. Please note that while 2.0 is the historic value for the inner dielectric, the current recommended value for the inner dielectric while using ZAP is 1.0.

On the numerical side, every advantage we had hoped for in ZAP came to pass. As mentioned in the previous section, we saw faster convergence, remarkable stability with respect to grid placement and much improved asymptotic behavior with decreasing grid spacing. We also, for the first time, had gradients that could be applied in dynamics or minimization.

## 1.3 The Way of Zap

There follow a dozen or so examples of using ZAP. The list is always growing because the toolkit philosophy really does work. Most of the examples use OEInterface to provide consistent command-line argument handling.

### 1.3.1 Partial Charges and Atomic Radii

There are three essential quantities for any PB calculation: coordinates, dielectric model (including radii), and charge. Coordinates will come from the atomic coordinates of the input molecule, but partial charges and the dielectric model deserve some extra attention.

Charges and radii can be calculated at run-time using functions provided by OEChem or other OpenEye toolkits (AM1-BCC charges from Quacpac TK for example). The dielectric model consists of both the value of the inner and outer dielectric, as well as how the dielectric adjusts from one to the other. ZAP uses atomic radii as the basis for its dielectric algorithm. By default, we recommend using Bondi VdW radii which can be set on a molecule using the function OEAssignBondiVdWRadii Or you can set specific radii on an atom-by-atom basis using the OEAtomBase::SetRadius function.

The current recommended value for the inner and outer dielectrics for a molecule in an aqueous solution are 1.0 and 80.0. Therefore, these are the default values for the OEZap and OEBind implementations. The historic value for the inner dielectric is 2.0, and this value may be set using the SetInnerDielectric method. Additionally, the default value for the inner dielectric of the OEET implementation remains at 2.0 for the time being.

Accurate PB calculations also depend on quality atomic charges. In OEChem, we provide MMFF94 partial charges as the lowest level of charges that we consider usable in PB. The examples that follow will use these charges, so that they don't depend on any toolkits beside ZAP and OEChem. But for production use, we recommend AM1-BCC charges

If your input file format can store partial charges and/or radii, you can use those values instead of calculating them at run time. OEB files can store radii and partial charges, so they serve as a useful intermediate file between many OpenEye programs. Note that charges and radii will only be written to an OEB file if they are present on the molecule when written.

Atomic charges can come in a PDB file, along with atomic radii, in the form of the extra fields added after the coordinates. This style originated with DelPhi. Note that to get OEChem to read charges and radii from these fields in a PDB file, you need to set a specific flavor on the input oemolistream before reading any molecules from the stream.

#### Example of using OEChem to read charges and radii from PDB

```
if s = oechem.oemolistream()ifs.SetFlavor(oechem.OEFormat_PDB, oechem.OEIFlavor_PDB_Default | oechem.OEIFlavor_
\rightarrowPDB DELPHI)
```

### 1.3.2 Grids

ZAP uses regular cubic lattices, or grids, to solve the PB equation. The examples here illustrate how to retrieve such from the calculation and to manipulate and store the information held by each. Typically, grids are not used per se but information is extracted, such as the potential at particular points in space, as is illustrated in the next section. However, some programs, such as VIDA, can read grids and display their properties. Also, having direct access to grids allows for manipulations of the potential map that may not have been anticipated.

This first example shows the simplest method of generating a grid of potentials using ZAP. We save the grid in OpenEye GRD (\*.grd) format which is a compact, binary format that can be visualized in VIDA. Alternatively, the grid can be written into GRASP format (\*.phi), which means that the grid stored will be 65 cubed regardless of the size of the grid used in the calculation. A  $65<sup>3</sup>$  grid is obtained by interpolation to a grid with that many points that fits over the largest dimension of the grid calculated.

#### **Listing 1: Calculating a potential grid**

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
from openeye import oegrid
from openeye import oezap
def main(argv=[_name_]):
    if len(argv) != 2:
        oechem.OEThrow.Usage("%s <molfile>" % argv[0])
    if s = oechem. oemolistream()if not ifs.open(argv[1]):
       oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   mol = occhem. OEGraphMol()oechem.OEReadMolecule(ifs, mol)
   oechem.OEAssignBondiVdWRadii(mol)
   oechem.OEMMFFAtomTypes(mol)
   oechem.OEMMFF94PartialCharges(mol)
   epsin = 1.0zap = oezap.OEZap()zap.SetInnerDielectric(epsin)
    zap.SetMolecule(mol)
   grid = oegrid.OEScalarGrid()if zap.CalcPotentialGrid(grid):
       oegrid.OEWriteGrid("zap.grd", grid)
if _name == " main":
    sys.exit(main(sys.argv))
```

The next example is an elaboration of the previous simple version where we add in control of the parameters of the calculation. Options are provided to set the internal and external (solute and solvent) dielectric constants, the distance between the molecule and the edges of the grid (boundary spacing or buffer) and the grid spacing. A smaller grid spacing implies a more dense and accurate grid, but it does come with a larger memory footprint.

Listing 2: Calculating potential grid with optional parameters

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
from openeye import oegrid
from openeye import oezap
def main(argv=[_name_]):
    itf = oechem. 0EInterface()if not SetupInterface(argv, itf):
       return 1
   zap = oezap. OEZap()
   zap.SetInnerDielectric(itf.GetFloat("-epsin"))
   zap.SetOuterDielectric(itf.GetFloat("-epsout"))
   zap.SetGridSpacing(itf.GetFloat("-grid_spacing"))
   zap.SetBoundarySpacing(itf.GetFloat("-buffer"))
   mol = occhem.OEGraphMol()ifs = oechem.oemolistream()
    if not ifs.open(itf.GetString("-in")):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % itf. GetString ("-in"))
   oechem.OEReadMolecule(ifs, mol)
   oechem.OEAssignBondiVdWRadii(mol)
   oechem.OEMMFFAtomTypes(mol)
   oechem.OEMMFF94PartialCharges(mol)
    zap.SetMolecule(mol)
   grid = oegrid.OEScalarGrid()if zap.CalcPotentialGrid(grid):
       if itf.GetBool("-mask"):
            oegrid.OEMaskGridByMolecule(grid, mol)
        oegrid.OEWriteGrid(itf.GetString("-out"), grid)
    return 0
```

InterfaceData =  $""$ 

(continued from previous page)

```
#zap_grid2 interface definition
!PARAMETER -in
 !TYPE string
 !BRIEF Input molecule file
  !REQUIRED true
!END
!PARAMETER -out
 !TYPE string
 !BRIEF Output grid file
 !REQUIRED true
!END
!PARAMETER -epsin
  !TYPE float
  !BRIEF Inner dielectric
  !DEFAULT 1.0
  !LEGAL_RANGE 0.0 100.0
!END
!PARAMETER -epsout
 !TYPE float
 !BRIEF Outer dielectric
 !DEFAULT 80.0
 !LEGAL RANGE 0.0 100.0
!END
!PARAMETER -grid_spacing
 !TYPE float
  !DEFAULT 0.5
  !BRIEF Spacing between grid points (Angstroms)
  !LEGAL RANGE 0.1 2.0
!END
!PARAMETER -buffer
 !TYPE float
  !DEFAULT 2.0
 !BRIEF Extra buffer outside extents of molecule.
 !LEGAL RANGE 0.1 10.0
!END
!PARAMETER -mask
 !TYPE bool
 !DEFAULT false
 !BRIEF Mask potential grid by the molecule
!END
\mathbf{u} and \mathbf{u}def SetupInterface(argv, itf):
   oechem. OEConfigure (itf, InterfaceData)
    if oechem. OECheckHelp(itf, argv):
        return False
    if not oechem. OEParseCommandLine(itf, argv):
        return False
```

```
infile = itf.GetString("-in")if not oechem. OEIsReadable (oechem. OEGetFileType (oechem.
\rightarrowOEGetFileExtension(infile))):
        oechem. OEThrow. Warning ("%s is not a readable input file" % infile)
        return False
    outfile = itf.GetString("-out")if not oegrid. OEIsWriteableGrid (oegrid. OEGetGridFileType (oechem.
\rightarrowOEGetFileExtension(outfile))):
        oechem. OEThrow. Warning ("%s is not a writable grid file" % outfile)
        return False
    return True
if name == " main ":
    sys.exit(main(sys.argy))
```

Here we show how to calculate a difference-map, that is to say the potential difference between a standard, two dielectric, calculation and a single dielectric calculation (approximating pure Coulombic potentials). These difference potentials represent the electrostatic response of the solvent to the charges within the solute molecule. If we mask away everything outside the molecule, we can see the contributions from the charges inside the molecule.

#### Listing 3: Calculating potential grid with optional parameters

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
from openeye import oegrid
from openeye import oezap
def main(argv=[_name_]):
    if len(argv) != 2:
        oechem.OEThrow.Usage("%s <molfile>" % argv[0])
    if s = oechem. oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   mol = occhem. OEGraphMol()
```

```
oechem.OEReadMolecule(ifs, mol)
   oechem.OEAssignBondiVdWRadii(mol)
    oechem.OEMMFFAtomTypes(mol)
    oechem.OEMMFF94PartialCharges(mol)
   zap = oezap. OEZap()
    zap.SetInnerDielectric(1.0)
    zap.SetGridSpacing(0.5)
   zap.SetMolecule(mol)
    # calculate standard 2-dielectric grid
   grid1 = oegrid.OEScalarGrid()zap.CalcPotentialGrid(grid1)
    # calculate grid with single dielectric
    grid2 = oegrid.OEScalarGrid()zap.SetOuterDielectric(zap.GetInnerDielectric())
    zap.CalcPotentialGrid(grid2)
    # take the difference
   oegrid.OESubtractScalarGrid(grid1, grid2)
    # mask out everything outside the molecule
   oegrid.OEMaskGridByMolecule(grid1, mol, oegrid.OEGridMaskType_GaussianMinus)
    oegrid.OEWriteGrid("zap_diff.grd", grid1)
if _name_ = "main":
    sys.exit(main(sys.argv))
```

### 1.3.3 Atom Potentials

The potentials at any charge, as calculated by PB, can be decomposed into three forms

- 1. Induced solvent potential: the potential produced by the polarization of the solvent.
- 2. Inter-charge Coulombic energy: the potential that would be produced if the solvent had the same dielectric as the solute molecule from all other charges.
- 3. Self potential: the potential produced by a charge at itself. Of course, as mentioned above, this is infinite analytically, but PB will produce an "approximation" to this infinity because the grid spacing is finite.

This example program shows how to calculate each of these quantities. In addition to command line flags to control dielectric, grid spacing, etc., there are three flags that affect the type of potentials calculated:

- -calc\_type solvent\_only
- -calc\_type remove\_self
- -calc\_type coulombic

With none of these flags, the code executes a single PB calculation, interpolates the potentials from the grid produced, reports the sum of these potentials multiplied by the charge on the respective atoms and outputs these potentials and charges in a table. This potential corresponds to  $(a)+(b)+(b)$  above.

Using the -calc type solvent only option executes two PB calculations, the standard calculation plus a second calculation where the external dielectric has been set to the solute dielectric. The atom potentials are then formed from the difference of these two calculations such that the remaining potential is that produced by the solvent alone. The sum of this set of atomic potentials multiplied by atomic charges all multiplied by 0.5 is the electrostatic component of transferring from a media of the same dielectric as the solute to water. These potentials correspond to (a) above.

The -calc type remove self flag for the example program below executes an internal algorithm in the ZAP toolkit that extracts from each atom potential that potential produced by that atom, if it is charged. This it removes the artifactual energy from the grid, i.e. energy that is not actually physical but a manifestation of the finite resolution of the grids used. The remaining potential is then that from the solvent and that from all the other charges, that is (a)+(b) above.

The -calc\_type coulombic flag actually prevents any PB calculation. It merely uses Coulomb's Law to calculate the potential (b), the inner-atomic Coulombic potential.

### **Listing 4: Calculating atom potentials**

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
from openeye import oezap
def Output (mol, apot, showAtomTable) :
   print ("Title: %s" % mol. GetTitle())
   if showAtomTable:
       print ("Atom potentials")
       print ("Index Elem Charge
                                         Potential")
    energy = 0.0for atom in mol. GetAtoms () :
        energy += atom. GetPartialCharge () *apot [atom. GetIdx ()]
        if showAtomTable:
            print ("%3d
                          82s86.3f$8.3f'' $(atom.GetIdx(),
                   oechem.OEGetAtomicSymbol(atom.GetAtomicNum()),
                   atom.GetPartialCharge(),
                   apot[atom.GetIdx() ])print ("Sum of {Potential * Charge over all atoms * 0.5} in kT = \frac{9f}{m}" %
          (0.5*energy))
```

```
def CalcAtomPotentials(itf):
   mol = occhem.OEGraphMol()if s = oechem. oemolistream()if not ifs.open(itf.GetString("-in")):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % itf. GetString ("-in"))
   oechem.OEReadMolecule(ifs, mol)
   oechem.OEAssignBondiVdWRadii(mol)
    if not itf.GetBool("-file_charges"):
        oechem.OEMMFFAtomTypes(mol)
        oechem.OEMMFF94PartialCharges(mol)
    zap = oezap.OEZap()zap.SetMolecule(mol)
    zap.SetInnerDielectric(itf.GetFloat("-epsin"))
    zap.SetBoundarySpacing(itf.GetFloat("-boundary"))
    zap.SetGridSpacing(itf.GetFloat("-grid_spacing"))
    showAtomTable = itf.GetBool("-atomtable")
    calcType = itf.GetString("-calc_type")
    if calcType == "default":apot = oechem.OEFloatArray(mol.GetMaxAtomIdx())
        zap.CalcAtomPotentials(apot)
        Output (mol, apot, showAtomTable)
    elif calcType == "solvent-only":apot = oechem.OEFloatArray(mol.GetMaxAtomIdx())
        zap.CalcAtomPotentials(apot)
        apot2 = oechem. OEFloatArray (mol. GetMaxAtomIdx())zap.SetOuterDielectric(zap.GetInnerDielectric())
        zap.CalcAtomPotentials(apot2)
        # find the differences
        for atom in mol. GetAtoms () :
            idx = atom.GetIdx()apot[idx] = apot2[idx]Output (mol, apot, showAtomTable)
    elif calcType == "remove_self":
        apot = oechem. OEFloatArray (mol. GetMaxAtomIdx())zap.CalcAtomPotentials(apot, True)
        Output (mol, apot, showAtomTable)
    elif calcType == "coulombic":epsin = itf.GetFloat("-epsin")x = oezap. OECoulombicSelfEnergy (mol, epsin)
        print ("Coulombic Assembly Energy")
        print (" = Sum of {Potential * Charge over all atoms * 0.5} in kT = f'' % x)
        apot = oechem.OEFloatArray(mol.GetMaxAtomIdx())
        oezap.OECoulombicAtomPotentials(mol, epsin, apot)
        Output (mol, apot, showAtomTable)
```

```
return 0
def SetupInterface(itf, InterfaceData):
   oechem. OEConfigure(itf, InterfaceData)
   if oechem. OECheckHelp(itf, sys.argv):
        return False
   if not oechem. OEParseCommandLine(itf, sys.argv):
       return False
   return True
def main(InterfaceData):
   itf = oechem. 0EInterface()if not SetupInterface(itf, InterfaceData):
        return 1
    return CalcAtomPotentials(itf)
InterfaceData = ""#zap_atompot interface definition
!PARAMETER -in
 !TYPE string
 !BRIEF Input molecule file.
 !REQUIRED true
 !KEYLESS 1
!END
!PARAMETER -file_charges
  !TYPE bool
  !DEFAULT false
  !BRIEF Use partial charges from input file rather than calculating with MMFF.
! END
!PARAMETER -calc_type
 !TYPE string
 !DEFAULT default
 !LEGAL VALUE default
 !LEGAL_VALUE solvent_only
 !LEGAL_VALUE remove_self
 !LEGAL_VALUE coulombic
  !LEGAL_VALUE breakdown
  !BRIEF Choose type of atom potentials to calculate
! END
!PARAMETER -atomtable
 !TYPE bool
 !DEFAULT false
 !BRIEF Output a table of atom potentials
! END
!PARAMETER -epsin
 !TYPE float
  !BRIEF Inner dielectric
```

```
!DEFAULT 1.0
  !LEGAL_RANGE 0.0 100.0
LEND
!PARAMETER -grid_spacing
  !TYPE float
  !DEFAULT 0.5
  !BRIEF Spacing between grid points (Angstroms)
  !LEGAL RANGE 0.1 2.0
! END
!PARAMETER -boundary
  !ALIAS -buffer
  ITYPE float
  IDEFAULT 2 0
  !BRIEF Extra buffer outside extents of molecule.
  !LEGAL_RANGE 0.1 10.0
! END
\overline{n} \overline{n} \overline{n}if __name__ == "__main__\mathbf{m}_{\mathrm{B}}sys.exit(main(InterfaceData))
```

### 1.3.4 Solvation Energies: PBSA

A principle use of PB is to calculate the energy stored in the exterior dielectric, for example the partial alignment of water dipoles. This corresponds to the difference between a calculation with uniform dielectric and one with a different external dielectric. In the examples for atom potentials this would be the sum of the solvent potentials at each atom, multiplied by the charges on that atom all multiplied by 0.5.

However, we know water also has an energy component due to hydrophobicity, which is typically estimated as a constant (approximately 10-25 calories per square Angstrom) multiplied by the accessible area of the molecule. This value is an open scientific question. We recommend using 10 for vacuum-water transfer energies and 25 for protein calculations, but ultimately your own scientific judgment should be used. These examples include an area calculation. Taken together these numbers are an approximation of the transfer energy from a low dielectric medium (alkane solvent, protein interior) into water.

The following examples use the OEArea object to calculate the accessible surface area of the molecule. The area is calculated using the same grid based Gaussians that ZAP uses. Therefore, it will not give the same results as triangle summation methods for calculating surface area, which are used in OESpicoli.

### **Listing 5: Calculating solvation energies**

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
from openeye import oezap
KCalsPerKT = 0.59KCalsPerSqAngstrom = 0.025def PrintHeader():
   print ("Title
                       Solv(kcal) Area(Ang^2) Total(kcal) Int.Coul(kcal)\ln")
def PrintLine(title, solv, area, coul):
    total = KCalsPerKT*solv + KCalsPerSqAngstrom*area
    print ("\frac{8-12s}{s} \frac{86.2f}{s}86.2f86.2f%6.2f'' &
          (title, KCalsPerKT*solv, area, total, KCalsPerKT*coul))
def main (argv=[\_name\_]):
    if len(argv) != 2:
        oechem.OEThrow.Usage("%s <molfile>" % argv[0])
    epsin = 1.0zap = oezap. OEZap()
    zap.SetInnerDielectric(epsin)
    zap.SetGridSpacing(0.5)
   area = oezap.OEArea()PrintHeader()
   mol = occhem. OEGraphMol()ifs = occhem.oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
    while oechem. OEReadMolecule(ifs, mol):
        oechem.OEAssignBondiVdWRadii(mol)
        oechem.OEMMFFAtomTypes(mol)
        oechem.OEMMFF94PartialCharges(mol)
        zap.SetMolecule(mol)
        solv = zap.CalcSolvationEnergy()aval = area.GetArea(mol)coul = oezap.OECoulombicSelfEnergy(mol, epsin)
        PrintLine(mol.GetTitle(), solv, aval, coul)
    return 0
   {\sf name} == {\sf "main" :}if.
```

sys.exit(main(sys.argv))

This next solvation example calculates the transfer energy from vacuum to water.

### Listing 6: Calculating vacuum-water transfer energies

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
from openeye import oezap
KCalsPerKT = 0.59KCalsPerSqAngstrom = 0.010def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) != 2:
        oechem.OEThrow.Usage("%s <molfile>" % argv[0])
    epsin = 1.0zap = oezap.OEZap()zap.SetInnerDielectric(epsin)
    zap.SetGridSpacing(0.5)
    area = oezap.OEArea()mol = occhem.OEGraphMol()ifs = occhem.oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open % for reading" % argv[1])
    oechem.OEThrow.Info("%-20s %6s\n" % ("Title", "Vacuum->Water(kcal)"))
    while oechem. OEReadMolecule (ifs, mol):
        oechem.OEAssignBondiVdWRadii(mol)
        oechem.OEMMFFAtomTypes(mol)
        oechem.OEMMFF94PartialCharges(mol)
        zap.SetMolecule(mol)
```

```
solv = zap.CalcSolvationEnergy()aval = area.GetArea(mol)oechem.OEThrow.Info("%-20s
                                       %6.2f" % (mol. GetTitle(),
→KCalsPerKT*solv+KCalsPerSqAngstrom*aval))
    return 0
if _name
            = "_main
                         \langle \mathbf{u} \ranglesys.exit(main(sys.argv))
```

### 1.3.5 Binding Energies

Binding energies and other binding related properties can be calculated using the OEBind class. The OEBind class serves two primary purposes: 1) to have a class in place for users to easily calculate binding related data, and 2) to show how binding related data may be calculated. OEBind is not particularly well-suited for extremely efficient calculations required by simulations. This is because some of the data available from OEBind may be considered uninteresting for the project and there is no need to spend time calculating it, or because OEBind calculates the unbound protein and ligand properties every time, which is unnecessary if the same protein and ligand appear in multiple calculations. The API section for OEBind is detailed with regard to implementation, so the user can see how to create their own class or set of function calls if needed.

There are two classes that store the results of a binding calculation, OEBindResults and OESimpleBindResults. OE-BindResults is a superset of OESimpleBindResults. For an in-depth understanding of what is calculated, the electrostatics portion of the algorithm for the SimpleBind function is shown in the API section.

The following is a sample program for using the OEBind class that is provided in the distribution.

#### **Listing 7: Bind example**

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
from openeye import oezap
```

```
def main(argv=[_name_]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <protein> <ligands>" % argv[0])
    protein = oechem. OEMol()
    ifs = oechem.oemolistream()
    if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
    oechem. OEReadMolecule(ifs, protein)
    oechem. OEAssignBondiVdWRadii (protein)
    oechem.OEMMFFAtomTypes(protein)
    oechem.OEMMFF94PartialCharges(protein)
    print ("protein: " + protein. GetTitle())
    epsin = 1.0bind = oezap.OEBind()bind.GetZap().SetInnerDielectric(epsin)
    bind.SetProtein(protein)
    results = oezap.OEBindResults()if not ifs.open(argv[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[2])
    ifs.SetConfTest(oechem.OEIsomericConfTest())
    ligand = oechem. <math>OEMol()</math>while oechem. OEReadMolecule(ifs, ligand):
        oechem.OEAssignBondiVdWRadii(ligand)
        oechem.OEMMFFAtomTypes(ligand)
        oechem.OEMMFF94PartialCharges(ligand)
        print ("ligand: %s has %d conformers" %
               (ligand.GetTitle(), ligand.NumConfig())for conf in ligand. GetConfs():
            bind. Bind (conf, results)
            print (" conf# \partial d be = \partial f'' \partial(conf.GetIdx(), results.GetBindingEnergy()))
    return 0
if __name__ == "__main__".sys.exit(main(sys.argv))
```

### 1.3.6 Focusing

Focusing is a way to achieve the desired precision around a target (such as a ligand) while maintaining reasonable time and memory limits for the calculation. The target for focusing is set using the OEZap. SetFocusTarget method.

For a typical ZAP electrostatics calculation, a consistent grid spacing is used for the entire system, where the default value is 0.5 Angstroms but it may be set to a custom value using  $OEZap$ .  $SetGridSpacing$ . This method is entirely appropriate for certain calculations, such as solvation energy calculations for small molecules. For other types of calculations, such as a binding energy calculation for a protein and ligand, a consistent grid spacing may cause the calculation to be either prohibitively expensive or insufficiently precise around the binding area.

Focusing alleviates this problem by using a fine grid for the target volume, and coarser grids away from the target. The grid spacing setting for ZAP is applied to the target volume, and the grid spacing is doubled for each addition coarse grid surrounding the target. A quadratic interpolation is used for the grid intersections. The implementation of the bind uses the SetFocusTarget() method to set the ligand as the target for focusing.

The following example program computes the binding energy of a protein and ligand twice, once without focusing and once with the ligand as the focusing target. The values of the binding energy and the time it took to calculate them are displayed. For a focused atom potential calculation, the full electrostatics for the protein and complex would each be computed with multiple electrostatics calculations. The first calculation would create the potential grid for the target volume with a grid spacing of 0.5 (assuming the default spacing is being used). An additional calculation with a grid spacing of 1.0 would be done on a larger volume volume, and then additional calculations with grid spacings of 2.0, 4.0, and so on would be done until the grid is large enough to contain the entire volume of the system.

### **Listing 8: Focusing example**

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
from openeye import oezap
def PrintHeader (protTitle, ligTitle) :
   oechem. OEThrow. Info("\nBinding Energy and Wall Clock Time for %s and %s" %
                        (protTitle, ligTitle))
    oechem.OEThrow.Info("%15s %15s %10s" % ("Focused?", "Energy(kT)", "Time(s)"))
```

def PrintInfo(focussed, energy, time):

```
oechem. OEThrow. Info("%15s %15.3f %10.1f" % (focussed, energy, time))
def CalcBindingEnergy (zap, protein, ligand, cmplx) :
    stopwatch = oechem. OEStopwatch()
    stopwatch. Start ()
   ppot = oechem. OEFloatArray (protein. GetMaxAtomIdx())
    zap.SetMolecule(protein)
    zap.CalcAtomPotentials(ppot)
   proteinEnergy = 0.0for atom in protein. GetAtoms () :
        proteinEnergy += ppot[atom.GetIdx()] *atom.GetPartialCharge()
   proteinEnergy *= 0.5lpot = oechem. OEFloatArray (ligand. GetMaxAtomIdx())
    zap.SetMolecule(ligand)
    zap.CalcAtomPotentials(lpot)
    ligandEnergy = 0.0for atom in ligand. GetAtoms () :
        ligandEnergy += lpot[atom.GetIdx()]*atom.GetPartialCharge()
    ligandEnergy *= 0.5cpot = oechem.OEFloatArray(cmplx.GetMaxAtomIdx())
    zap.SetMolecule(cmplx)
    zap.CalcAtomPotentials(cpot)
    cmplxEnergy = 0.0for atom in cmplx. GetAtoms () :
        cmplxEnergy += cpot[atom.GetIdx()]*atom.GetPartialCharge()
    cmplxEnergy *= 0.5energy = cmplxEnergy - ligandEnergy - proteinEnergy
    time = stopwatch.Elapped()if zap. IsFocusTargetSet():
        focused = "Yes"else:focused = "No"PrintInfo(focused, energy, time)
def main(argv=[_name_]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <protein> <ligand>" % argv[0])
    if s = oechem. oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
   protein = oechem. OEGraphMol()
   oechem.OEReadMolecule(ifs, protein)
    if not ifs.open(argv[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[2])
    ligand = oechem. OEGraphMol()oechem. OEReadMolecule(ifs, ligand)
```

```
oechem. OEAssignBondiVdWRadii (protein)
    oechem.OEMMFFAtomTypes(protein)
    oechem. OEMMFF94PartialCharges (protein)
    oechem.OEAssignBondiVdWRadii(ligand)
    oechem.OEMMFFAtomTypes(ligand)
    oechem.OEMMFF94PartialCharges(ligand)
    cmplx = oechem. OEGraphMol(protein)
    oechem.OEAddMols(cmplx, ligand)
    epsin = 1.0spacing = 0.5\text{zap} = \text{oezap} \cdot \text{OEZap}()zap.SetInnerDielectric(epsin)
    zap.SetGridSpacing(spacing)
    PrintHeader(protein.GetTitle(), ligand.GetTitle())
    CalcBindingEnergy(zap, protein, ligand, cmplx)
    zap.SetFocusTarget(ligand)
    CalcBindingEnergy(zap, protein, ligand, cmplx)
    return 0
if name
            = " main ":
    sys.exit(main(sys.argy))
```

### 1.3.7 Gradients/Forces

The solvent forces acting on the atoms in a molecule may be calculated using the  $OEZap$ . CalcForces method. The components of the forces are set to a float array of length 3N, where N is the number of atoms. The components of the gradient are equal in magnitude to the force, but have the opposite sign.

#### **Listing 9: Calculating solvation forces**

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
from openeye import oezap
def PrintHeader(title):
    oechem. OEThrow. Info("\nForce Components for %s, in kT/Angstrom" % title)
    oechem. OEThrow. Info("%6s %8s %8s %8s %8s" % ("Index", "Element", "-dE/dx",
                                                   "-dE/dy", "-dE/dz"))
def PrintForces(mol, forces):
    for atom in mol. GetAtoms () :
        oechem. OEThrow. Info ("%6d %8s %8.2f %8.2f %8.2f" %
                             (atom.GetIdx(),
                              oechem.OEGetAtomicSymbol(atom.GetAtomicNum()),
                              forces[atom.GetIdx()],
                              forces[atom.GetIdx()+1],
                              forces [atom. GetIdx() + 2]) )
def main(argv=[_name_]):
    if len(argv) != 2:
        oechem.OEThrow.Usage("%s <molfile>" % argv[0])
    epsin = 1.0\text{zap} = \text{oezap}.\text{OEZap}()zap.SetInnerDielectric(epsin)
    mol = occhem. OEGraphMol()if s = oechem.oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
    while oechem. OEReadMolecule(ifs, mol):
        PrintHeader(mol.GetTitle())
        forces = oechem.OEFloatArray(mol.GetMaxAtomIdx() *3)oechem.OEAssignBondiVdWRadii(mol)
        oechem.OEMMFFAtomTypes(mol)
        oechem.OEMMFF94PartialCharges(mol)
        zap.SetMolecule(mol)
        zap.CalcForces(forces)
        PrintForces(mol, forces)
    return 0
if name == "_main_":
    sys.exit(main(sys.argv))
```

### 1.3.8 Electrostatic Similarity

Electrostatic similarity may be calculated using the OEET class. The following example program shows how to obtain the electrostatic Tanimoto between a reference molecule and a trial molecule. The electrostatic Tanimoto is affected by the partial charges of the molecules as well as the three-dimensional structure, including the tautomer state, spacial orientation, and conformation. In the example program shown below, MMFF charges are assigned to the molecules, but it is assumed that they have already been spatially aligned.

### **Listing 10: Calculating electrostatic tanimoto**

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
from openeye import oezap
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("calc_et.py <reffile> <fitfile>")
    refmol = occhem.OEGraphMol()if s = oechem. oemolistream()if not ifs.open(argv[1]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[1])
    oechem.OEReadMolecule(ifs, refmol)
    oechem.OEAssignBondiVdWRadii(refmol)
    oechem.OEMMFFAtomTypes(refmol)
    oechem.OEMMFF94PartialCharges(refmol)
    et = oezap.OEET()et.SetRefMol(refmol)
    oechem.OEThrow.Info("dielectric: %.4f" % et.GetDielectric())
    oechem. OEThrow. Info ("inner mask: %. 4f" % et. GetInnerMask())
    oechem. OEThrow. Info ("outer mask: \frac{2}{3}. 4f" \frac{2}{3} et. GetOuterMask())
    oechem. OEThrow. Info ("salt conc : %. 4f" % et. GetSaltConcentration () )
    oechem.OEThrow.Info("join
                                  : \mathcal{E} d'' \mathcal{E} et. GetJoin ())
```

```
if not ifs.open(argv[2]):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % argv[2])
    fitmol = oechem.OEGraphMol()
   while oechem. OEReadMolecule(ifs, fitmol):
        oechem.OEAssignBondiVdWRadii(fitmol)
        oechem.OEMMFFAtomTypes(fitmol)
        oechem.OEMMFF94PartialCharges(fitmol)
        oechem. OEThrow. Info ("Title: %s, ET %4.2f" %
                            (fitmol.GetTitle(), et.Tanimoto(fitmol)))
   return 0
if _name_ == "_main_":
   sys.exit(main(sys.argv))
```

### **CHAPTER**

## **TWO**

# API

## 2.1 OEPB Classes

### 2.1.1 OEArea

#### class OEArea

This class represents OEArea. OEArea is a simple object that calculates surface area using the same grid-based Gaussians that Zap uses. This class is mostly used for calculating the area term in solvation calculations or the buried area term in bind calculations.

#### Constructors

```
OEArea()
OEArea (const OEArea &)
```

Default and copy constructors.

#### operator=

```
OEArea & operator= (const OEArea &)
```

Assignment operator.

### 2.1.2 GetArea

```
float GetArea (const OEChem:: OEMolBase &mol)
bool GetArea (const OEChem:: OEMolBase &mol, float *atomArea)
float GetArea (const OEChem:: OEMolBase & mol, const OEChem:: OEResidue & res)
float GetArea (const OEChem:: OEMolBase &mol, const float *atomArea, const
\rightarrow OEChem:: OEResidue & res)
```

Calculate the surface area of the passed-in molecule. The first version calculates the surface area of the entire molecule. The second version takes an array sized by OEMolBase:: GetMaxAtomIdx to return the contribution of each atom to the total surface area. The third and fourth versions calculates and returns the surface area of the residue passed into the function. The fourth version differs from the third version by taking a already calculated atom area array, which avoids calculating atom area repeatedly.

Note that whether or not hydrogens are included in these calculations is controlled by  $OEArea$ . SetUseHydrogens which is set to false by default.

The following demonstrates how to calculate the area of a molecule:

#### Example of calculating the surface area of a molecule

```
area = oezap.OEArea()a = area.GetArea (mol)
print ("Molecule area =", a)
```

The following demonstrates how to retrieve the individual atom contributions to the surface area:

#### Example of calculating the surface area contribution of individual atoms

```
atomArea = occhem.OEFloatArray(mol.GetMaxAtomIdx())area = oezap.OEArea()area.GetArea(mol, atomArea)
for atom in mol. GetAtoms () :
    idx = atom.FetIdx()print(idx, atomArea[idx])
```

The following demonstrates how to retrieve the per residue contributions to the surface area:

#### Example of calculating the surface area contribution of indivdual residues

```
area = oezap.OEArea()for res in oechem. OEGetResidues (mol) :
    print (area.GetArea(mol, res))
```

The following demonstrates how to retrieve the per residue contributions to the surface area, in an optimized way where the per atom contributions are pre-calculated and used for the residue based calculation. This is particularly important if this calculation is done on a large set of residues:

#### Example of calculating the surface area contribution of indivdual residues

```
atomArea = occhem.OEFloatArray(mol.GetMaxAtomIdx())area = oezap.OEArea()area.GetArea(mol, atomArea)
for res in oechem. OEGetResidues (mol) :
    print (area.GetArea(mol, atomArea, res))
```

## 2.1.3 GetMethod

unsigned int GetMethod() const

Returns an inti ndicating the method that is used to model the area of the molecule. The two possible return values are OEAreaMethod\_Gaussian and OEAreaMethod\_Discrete.

## 2.1.4 GetUseHydrogens

bool GetUseHydrogens () const

Returns a bool where true means explicit hydrogens are turned on and false means they are turned off for the area calculation.

## 2.1.5 SetMethod

bool SetMethod (const unsigned int method)

Takes an int with the value of OEAreaMethod\_Gaussian of OEAreaMethod\_Discrete

## 2.1.6 SetUseHydrogens

bool SetUseHydrogens (bool state)

This method takes a bool where true turns on explicit hydrogens for calculating area and false turn them off.

## 2.1.7 OEBind

| class OEBind |  |
|--------------|--|
|--------------|--|

This class represents OEBind. OEBind is used to calculate protein-ligand binding properties. The protein may either be passed in as an argument during construction or set with OEBind. Set Protein. The ligand is passed in as an argument to OEBind. Bind as well as an OEBindResults instance.

### **Constructors**

```
OEBind()
OEBind (const OEBind & rhs)
OEBind (const OEChem:: OEMolBase & protein)
```

Default and copy constructors. Besides the default and copy constructors, OEBind includes a constructor that takes the protein to be used in binding calculations. Constructing an OEBind object with the protein is identical to using the default constructor and then calling OEBind. SetProtein.

#### operator=

OEBind & operator= (const OEBind & rhs)

Assignment operator.

#### **Bind**

```
bool Bind (const OEChem:: OEMolBase & ligand, OEBindResults & results)
OESystem::OEIterBase<OEBindResults> *Bind(const OEChem::OEMCMolBase &ligand)
```

Calculate full binding results, including Coulombic terms. For a single molecule, pass in the molecule and the OE-BindResults class will be filled in. The following is a simple example of how Bind is used.

### **Example of using the OEBind object**

```
bind = oezap.OEBind()bind.SetProtein(protein)
results = oezap. OEBindResults()bind. Bind (ligand, results)
results. Print (oechem. OEThrow)
```

#### **GetZap**

```
OEZap & GetZap()
const OEZap & GetZap () const
```

Get a reference to the internal OEZap object contained in an OEBind instance. With the non-const version, you can adjust OEZap parameters that affect the OEBind calculation. For example, to use an OEBind instance with a specific grid spacing:

#### Example of setting the grid spacing of a OEBind object

```
bind = oezap.OEBind()bind.GetZap().SetGridSpacing(0.6)
```

Note that some properties of the OEZap object are not controllable via this mechanism.

#### **SetProtein**

bool SetProtein (const OEChem:: OEMolBase &protein)

Set the protein molecule to be used by the OEBind object. Note that the protein should have radii and partial charges pre-calculated before passing to OEBind. SetProtein.

### **SetZap**

```
bool SetZap (const OEZap &zap)
```

Update the internal OEZap object. Note that some properties of the OEZap object are not controllable via this mechanism.

### **SimpleBind**

```
bool SimpleBind(const OEChem:: OEMolBase &ligand, OESimpleBindResults &results)
OESystem:: OEIterBase<OESimpleBindResults> *
  SimpleBind(const OEChem:: OEMCMolBase & liqand)
```

Calculate simple binding results, without the Coulombic terms. See the discussion in Binding Energies about the differences between OEBind. Bind and OEBind. SimpleBind. See OESimpleBindResults to see all the values available.

Additionally, both the SimpleBind and OEBind. Bind methods calculate area contributions.

## 2.1.8 OEBindResults

class OEBindResults : public OESimpleBindResults

This class represents OEBindResults. All energy results are in units of kT.

The following methods are publicly inherited from OESimpleBindResults:

| operator=                 | GetBuriedArea              | GetUnboundLigandZapEnergy   |
|---------------------------|----------------------------|-----------------------------|
| GetBindingEnergy          | GetBuriedAreaEnergy        | GetUnboundProteinArea       |
| GetBoundLigandArea        | GetComplexArea             | GetUnboundProteinAreaEnergy |
| GetBoundLigandAreaEnergy  | GetComplexAreaEnergy       | GetUnboundProteinZapEnergy  |
| GetBoundLigandZapEnergy   | GetComplexZapEnergy        | GetZapEnergy                |
| GetBoundProteinArea       | GetConf                    | Print                       |
| GetBoundProteinAreaEnergy | GetUnboundLigandArea       |                             |
| GetBoundProteinZapEnergy  | GetUnboundLigandAreaEnergy |                             |

### **Constructors**

```
OEBindResults()
OEBindResults (const OEBindResults &)
```

Default and copy constructors.

#### operator=

OEBindResults & operator= (const OEBindResults &)

Assignment operator.

#### **GetAnalyticCoulombicBindingEnergy**

float GetAnalyticCoulombicBindingEnergy () const

This returns the value of the analytic binding energy for the ligand and protein that have been set to the OEBind object. This is equivalent to calling OECalculateCoulombicBinding where the same ligand and protein and inner dielectric are the arguments.

#### **GetBoundLigandCoulombEnergy**

float GetBoundLigandCoulombEnergy () const

Returns the grid-based coulomb energy for the ligand in the bound state, including self-interaction. Specially, it returns the boundLigandCoulombEnergy variable shown in the OEBind. Bind API section.

#### **GetBoundProteinCoulombEnergy**

float GetBoundProteinCoulombEnergy () const

Returns the grid-based coulomb energy for the protein in the bound state, including self-interaction. Specially, it returns the boundProteinCoulombEnergy variable shown in the OEBind. Bind API section.

#### **GetComplexCoulombEnergy**

float GetComplexCoulombEnergy () const

Returns the grid-based coulomb energy for the complex, including self-interaction. Specially, it returns the complexCoulombEnergy variable shown in the OEBind. Bind API section. This is equivalent to the sum of the results returned by OEBindResults. GetBoundLigandCoulombEnergy and OEBindResults. GetBoundProteinCoulombEnergy.

#### **GetCoulombEnergy**

float GetCoulombEnergy () const

Returns the difference in Coulomb energy between the complex and the unbound ligand and protein. This is equivalent to OEBindResults.GetComplexCoulombEnergy - OEBindResults. GetUnboundProteinCoulombEnergy - OEBindResults.GetUnboundLigandCoulombEnergy.

#### **GetDesolvationEnergy**

float GetDesolvationEnergy () const

This is equivalent to OESimpleBindResults. GetZapEnergy - OEBindResults. GetCoulombEnergy.

#### GetLigandDesolvationEnergy

float GetLigandDesolvationEnergy () const

This is equivalent to OESimpleBindResults. GetBoundLigandZapEnergy - OEBindResults. GetBoundLigandCoulombEnergy - OESimpleBindResults.GetUnboundLigandZapEnergy + OEBindResults.GetUnboundLigandCoulombEnergy.

#### GetProteinDesolvationEnergy

float GetProteinDesolvationEnergy() const

This is equivalent to OESimpleBindResults.GetBoundProteinZapEnergy - OEBindResults. GetBoundProteinCoulombEnergy - OESimpleBindResults.GetUnboundProteinZapEnergy + OEBindResults.GetUnboundProteinCoulombEnergy.

#### GetUnboundLigandCoulombEnergy

float GetUnboundLigandCoulombEnergy () const

Returns the grid-based coulomb energy for the ligand in the unbound state, including self-interaction. Specially, it returns the unboundLigandCoulombEnergy variable shown in the OEBind. Bind API section.

#### **GetUnboundProteinCoulombEnergy**

float GetUnboundProteinCoulombEnergy () const

Returns the grid-based coulomb energy for the protein in the unbound state, including self-interaction. Specially, it returns the unboundProteinCoulombEnergy variable shown in the OEBind. Bind API section.

#### **Print**

```
void Print (OEPlatform:: oeostream &ofs) const
void Print (OESystem:: OEErrorHandler &log) const
```

Prints out all of the available data to the oeostream of the OEErrorHandle passed in.

## **2.1.9 OEET**

### class OEET

This class represents OEET, which is used to calculated electrostatic similarity.

#### **Constructors**

```
OEET (const OEET & rhs)
OEET (float dielectric=80.0f)
```

Default and copy constructors.

#### operator=

```
OEET & operator= (const OEET & rhs)
```

Assignment operator

### **GetDielectric**

float GetDielectric() const

Returns the setting for the outer dielectric constant.

### **GetGridBuffer**

float GetGridBuffer() const

Returns the setting for the amount of space between the molecule and the edge of the grid.

#### **GetGridSpacing**

```
float GetGridSpacing() const
```

Returns the setting for the grid spacing.

#### **GetInnerDielectric**

```
float GetInnerDielectric() const
```

Returns the value for the inner dielectric.

### **GetInnerMask**

float GetInnerMask() const

Returns the value for the inner mask.

#### **GetJoin**

bool GetJoin() const

Returns the setting for whether or not to join the molecules for masking.

### **GetOuterMask**

float GetOuterMask() const

Returns the value for the outer mask.

#### **GetSaltConcentration**

```
float GetSaltConcentration() const
```

```
Returns the setting for the salt concentration
```

#### **SetDielectric**

void SetDielectric (float d)

Sets the outer dielectric constant

#### **SetGridBuffer**

```
void SetGridBuffer (float f)
```

Sets the grid buffer, or boundary spacing, which is the amount of distance between the molecule and the edge of the grid. The default value is 6.0.

### **SetGridSpacing**

void SetGridSpacing (float f)

Sets the grid spacing. The default value is 0.75.

### **SetInnerDielectric**

void SetInnerDielectric (float d)

Sets the inner dielectric constant

### **SetInnerMask**

void SetInnerMask (float f)

Sets the inner mask for electrostatic comparison. The default value is set to 0.05. The inner mask is used to mask out the inner part of a molecule. The inner part of the molecule is masked out so that the important regions surrounding the molecule dominate the electrostatic comparison.

### **SetJoin**

void SetJoin (bool j)

Turns molecular joining on  $(true)$  or off  $f$  alse). The default value is true, which uses the combine reference molecule and trial molecule when applying the inner and outer mask.

### **SetOuterMask**

void SetOuterMask (float f)

Sets the outer mask for electrostatic comparison. The default value is set to 0.0005. The outer mask is used to mask out regions far from the molecule.

### **SetRefMol**

bool SetRefMol(const OEChem:: OEMolBase &mol)

Sets the reference molecule.

### **SetSaltConcentration**

void SetSaltConcentration (float conc)

Sets the salt concentration. The default value is 0.04.

### **Tanimoto**

float Tanimoto (const OEChem:: OEMolBase & mol)

Returns the electrostatic Tanimoto between the reference molecule that has been set and the trial molecule that is passed in as an argument.

## 2.1.10 OESimpleBindResults

```
class OESimpleBindResults
```

This class represents OESimpleBindResults. The Zap calculations used for the SimpleBindResults are performed with the 2 separate dielectric constants, the internal for the molecule and the external for the solvent. All energy results are in units of kT.

#### The following classes derive from this class:

• OEBindResults

#### **Constructors**

```
OESimpleBindResults()
OESimpleBindResults (const OESimpleBindResults &)
```

Default and copy constructors.

#### operator=

OESimpleBindResults & operator=(const OESimpleBindResults &)

#### Assignment operator

#### **GetBindingEnergy**

```
float GetBindingEnergy () const
```

Returns the binding energy of the ligand and protein. Equivalent to OESimpleBindResults. GetBuriedAreaEnergy + OESimpleBindResults.GetZapEnergy.

### **GetBoundLigandArea**

float GetBoundLigandArea() const

Returns the boundLigandArea variable shown in the OEBind. SimpleBind API section. The bound ligand area is the area of the ligand exposed to the solvent while in the bound state.

#### **GetBoundLigandAreaEnergy**

float GetBoundLigandAreaEnergy() const

Returns the boundLigandAreaEnergy variable shown in the OEBind. SimpleBind API section. This is the energy associated with the bound ligand area.

#### GetBoundLigandZapEnergy

float GetBoundLigandZapEnergy() const

Returns the boundLigandZapEnergy variable shown in the OEBind. SimpleBind API section. This is the ligand grid energy obtained from a Zap calculation of the complex.

#### **GetBoundProteinArea**

float GetBoundProteinArea() const

Returns the boundProteinArea variable shown in the OEBind. SimpleBind API section. This is the area of the protein exposed to the solvent while in the bound state.

#### **GetBoundProteinAreaEnergy**

float GetBoundProteinAreaEnergy () const

Returns the boundProteinAreaEnergy variable shown in the OEBind. SimpleBind API section. This is the energy associated with the bound protein area.

#### **GetBoundProteinZapEnergy**

float GetBoundProteinZapEnergy() const

Returns the boundProteinZapEnergy variable shown in the OEBind. SimpleBind API section. This is the protein grid energy obtained from a Zap calculation of the complex.

#### **GetBuriedArea**

float GetBuriedArea() const

Returns the amount of area that has become buried as a result of binding. Equivalent to OESimpleBindResults. GetUnboundProteinArea OESimpleBindResults.GetUnboundLigandArea  $+$ OESimpleBindResults.GetComplexArea.

#### **GetBuriedAreaEnergy**

float GetBuriedAreaEnergy() const

Returns the energy penalty associated with the buried area of the complex. Equivalent to OESimpleBindResults. GetComplexAreaEnergy  $\sim$ OESimpleBindResults.GetUnboundProteinAreaEnergy OESimpleBindResults.GetUnboundLigandAreaEnergy.

#### **GetComplexArea**

float GetComplexArea() const

Returns the complexArea variable shown in the OEBind. SimpleBind API section. This is the solvent accessible surface area of the complex.

### **GetComplexAreaEnergy**

float GetComplexAreaEnergy() const

Returns the complexAreaEnergy variable shown in the OEBind. SimpleBind API section. This is the energy of the solvent accessible surface area of the complex.

### **GetComplexZapEnergy**

float GetComplexZapEnergy() const

Returns the grid energy of the complex. This is equivalent to OESimpleBindResults. GetBoundProteinZapEnergy + OESimpleBindResults.GetBoundLigandZapEnergy.

### **GetConf**

```
OEChem:: OEConfBase *GetConf()
const OEChem:: OEConfBase *GetConf () const
```

Returns a pointer to the active conformer.

#### GetUnboundLigandArea

float GetUnboundLigandArea () const

Returns the unboundLigandArea variable shown in the OEBind. SimpleBind API section. This is the solvent accessible surface area of the unbound ligand.

#### GetUnboundLigandAreaEnergy

float GetUnboundLigandAreaEnergy() const

Returns the unboundLigandAreaEnergy variable shown in the OEBind. SimpleBind API section. This is the energy of the solvent accessible surface area of the unbound ligand.

### GetUnboundLigandZapEnergy

float GetUnboundLigandZapEnergy() const

Returns the unboundLigandZapEnergy variable shown in the OEBind. SimpleBind API section. This is the grid energy of the unbound ligand obtained from a Zap calculation.

#### **GetUnboundProteinArea**

float GetUnboundProteinArea() const

Returns the unboundProteinArea variable shown in the OEBind. SimpleBind API section. This is the solvent accessible surface area of the unbound protein.

#### **GetUnboundProteinAreaEnergy**

float GetUnboundProteinAreaEnergy () const

Returns the unboundProteinAreaEnergy variable shown in the OEBind. SimpleBind API section. This is the energy of the solvent accessible surface area of the unbound protein.

### **GetUnboundProteinZapEnergy**

float GetUnboundProteinZapEnergy() const

Returns the unboundProteinZapEnergy variable shown in the OEBind. SimpleBind API section. This is the grid energy of the unbound protein obtained from a Zap calculation.

#### **GetZapEnergy**

float GetZapEnergy () const

Returns the difference in grid energy between the complex and the unbound ligand and protein. This is equivalent to OESimpleBindResults. GetComplexZapEnergy - OESimpleBindResults. GetUnboundProteinZapEnerqy - OESimpleBindResults.GetUnboundLiqandZapEnerqy.

**Print** 

```
void Print (OEPlatform:: oeostream &ofs) const
void Print (OESystem:: OEErrorHandler &log) const
```

Prints out all of the available data to the oeostream of the OEErrorHandle passed in.

## 2.1.11 OEZap

### class OEZap

This class represents OEZap.

### **Constructors**

```
OEZap()
OEZap (const OEZap & rhs)
```

Default and copy constructors.

### operator=

```
OEZap & operator = (const OEZap & rhs)
```

Assignment operator.

### **CalcAtomPotentials**

bool CalcAtomPotentials (float \*pot, bool no\_grid=false)

Calculates the atom potentials and fills the float array with their values. The float array should be of length N, where N is the number of atoms.

### **CalcForces**

bool CalcForces (float \*forces)

Calculates the forces on the atoms and fills the float array with the values of their x, y, and z components. The float array should be of length 3N, where N is the number of atoms.

### **CalcPotentialGrid**

**bool** CalcPotentialGrid(OESystem::OEScalarGrid &grid)

Calculates the potential grid and updates the OEScalarGrid with the values. The calculated electrostatic potential is a dimensionless value defined as  $eV/kT$  where  $eV$  is the electric work, in kcal/mol, of bringing an electron charge to the point with potential V, and  $kT = 0.59$  kcal/mol (value of kT at room temperature).

### **CalcSolvationEnergy**

float CalcSolvationEnergy ()

Returns the solvation energy in kT of the molecule that has been set. This result does not include an area term.

### **ClearFocusTarget**

void ClearFocusTarget()

Clears the target setting for focusing.

### **GetBoundarySpacing**

float GetBoundarySpacing() const

Returns the boundary spacing setting, which is the amount of distance between the molecule and the edge of the grid. The default setting is 4.0.

### **GetDielectricModel**

unsigned int GetDielectricModel() const

Returns an int representing the dielectric model being used. The two available models are OEZapDielectricModel\_Gaussian and OEZapDielectricModel\_Molecular.

### **GetError**

float GetError() const

Returns the error setting. See OEZap. SetError.

### **GetFocusTarget**

const OEChem:: OEMolBase \*GetFocusTarget() const

Returns a pointer to the molecule that has been set as the focus target.

### **GetGridSpacing**

float GetGridSpacing() const

Returns the setting for the grid spacing. The default value is 0.5.

### **GetInnerDielectric**

float GetInnerDielectric() const

Returns the setting for the internal dielectric constant. The default value is 1.0.

#### **GetIterations**

unsigned int GetIterations () const

Returns the maximum number of iterations allowed for the zap calculation. The default value is 10.

### **GetMolecule**

const OEChem:: OEMolBase \*GetMolecule() const

Returns a pointer to the molecule that has been set to Zap.

### **GetOuterDielectric**

float GetOuterDielectric() const

Returns the setting for the outer dielectric constant. The default value is 80.0.

#### **GetProbeRadius**

float GetProbeRadius() const

Returns the setting for the probe radius. The default value is 1.4.

### **GetVerbose**

bool GetVerbose() const

Returns the setting for very low-level verbosity. The default value is false.

#### **GetSaltConcentration**

float GetSaltConcentration() const

Returns the setting for the salt concentration. The default value is 0.0.

#### **IsFocusTargetSet**

```
bool IsFocusTargetSet()
```

Returns a bool for whether the focus target is currently set. See the section of focusing for more information.

#### **SetBoundarySpacing**

**bool** SetBoundarySpacing (float spacing)

Sets the boundary spacing, which is the amount of distance between the molecule and the edge of the grid. The default setting is 4.0.

#### **SetDielectricModel**

bool SetDielectricModel (unsigned int model)

Sets the dielectric model. The two available models are OEZapDielectricModel\_Gaussian and OEZapDielectricModel\_Molecular. The default is the Gaussian model.

### **SetError**

bool SetError (float zaperr)

Rather than setting the grid spacing, the acceptable error may be set instead using this method. The default value is set to 0.0, which means that the grid spacing is set explicitly.

#### **SetFocusTarget**

bool SetFocusTarget (const OEChem:: OEMolBase &mol)

Sets the focus target. See the section of *Focusing* for more information.

### **SetGridSpacing**

bool SetGridSpacing (float spacing)

Sets the grid spacing. The default value is 0.5.

#### **SetInnerDielectric**

bool SetInnerDielectric (float epsin)

Sets the internal dielectric constant. The default value is 1.0.

### **SetIterations**

**bool** SetIterations (*unsigned int iters*)

Sets the maximum number of iterations allowed for the zap calculation. The default value is 10

#### **SetMolecule**

bool SetMolecule (const OEChem:: OEMolBase &mol)

Sets the molecule to Zap. Partial charges, 3-D coordinates, and radii need to be set to the molecule before the molecule is set to Zap.

#### **SetOuterDielectric**

bool SetOuterDielectric(float epsout)

Sets the external dielectric constant. The default value is 80.0.

### **SetProbeRadius**

```
bool SetProbeRadius (float radius)
```

Sets the probe radius, the default value is 1.4.

#### **SetSaltConcentration**

bool SetSaltConcentration (float conc)

Sets the salt concentration. The default value is 0.0.

### **SetVerbose**

bool SetVerbose (bool verbose)

Sets very low-level verbosity. The default value is false.

# **2.2 OEPB Constants**

## 2.2.1 OEAreaMethod

This namespace contains constants.

### **Undefined**

This value represents an unset OEAreaMethod.

### **Gaussian**

This method uses Gaussians to compute area and is faster and less sensitive to rotation and translation on the grid.

### **Discrete**

This method uses a hard sphere model to compute area.

### **Default**

The default is set to Gaussian.

## 2.2.2 OEZapDielectricModel

This namespace contains constants.

### Gaussian

This model uses Gaussians to represent atoms and is faster and less sensitive to rotation and translation on the grid.

#### **Molecular**

This model uses hard spheres to represent atoms.

### **Default**

The default model is Gaussian.

# **2.3 OEPB Functions**

## 2.3.1 OECalculateCoulombicBinding

```
float OECalculateCoulombicBinding(const OEChem:: OEMolBase &protein,
                                   const OEChem:: OEMolBase & ligand,
                                   float dielectric)
```

Returns the analytic binding energy in kT for the ligand and protein in the specified dielectric using Coulomb's Law.

## 2.3.2 OECoulombicAtomPotentials

```
bool OECoulombicAtomPotentials (const OEChem:: OEMolBase &mol, float D,
                                float *apot)
```

Calculates the Coulombic atom potentials with the dielectric constant  $D$  and fills the float array apot with the values. apot should be of length N, where N is the number of atoms.

## 2.3.3 OECoulombicSelfEnergy

float OECoulombicSelfEnergy (const OEChem:: OEMolBase &mol, float D)

Returns the integral energy in kT of a molecule from its partial charges in universal dielectric D using Coulomb's Law.

## 2.3.4 OEMakeETGrid

```
bool OEMakeETGrid (OESystem:: OEScalarGrid &grid, const OEChem:: OEMolBase &mol,
                  const OEET &et)
```

Calculates the electrostatic Tanimoto grid for the mol passed in and the reference molecule that needs to be already set to the OEET instance.

## 2.3.5 OEZapBind

```
bool OEZapBind (const OEChem:: OEMolBase &protein,
               const OEChem:: OEMolBase & ligand, OEBindResults & results)
bool OEZapBind (const OEChem:: OEMolBase &protein,
               const OEChem:: OEMolBase &ligand, OESimpleBindResults &results)
```

Convenience functions for obtaining OEBindResults or OESimpleBindResults of a ligand and protein.

## 2.3.6 OEZapGetArch

const char \*OEZapGetArch()

Returns the architecture on which the release was built

## 2.3.7 OEZapGetLicensee

**bool** OEZapGetLicensee(std::string &licensee)

Fills the parameter string & licensee with the licensee of the license file being used

## 2.3.8 OEZapGetPlatform

const char \*OEZapGetPlatform()

Returns the platform on which the release was built

## 2.3.9 OEZapGetRelease

const char \*OEZapGetRelease()

Returns the version number as a const char \* in major.minor.bugfix form

## 2.3.10 OEZapGetSite

**bool** OEZapGetSite(std::string &site)

Fills the parameter string alicensee with the site on the license file being used

## 2.3.11 OEZapGetVersion

unsigned int OEZapGetVersion()

Returns the build date of the release

## **CHAPTER**

# **THREE**

# **RELEASE HISTORY**

# 3.1 Zap TK 2.5.0

Minor internal improvements have been made.

# 3.2 Zap TK 2.4.7

Minor internal improvements have been made.

# 3.3 Zap TK 2.4.6

## 3.3.1 New features

• New overloads of GetArea have been added that return solvent accessible surface areas for specific residues.

# 3.4 Zap TK 2.4.5

Minor internal improvements have been made.

# 3.5 Zap TK 2.4.4

Minor internal improvements have been made.

# 3.6 Zap TK 2.4.3

• Minor internal improvements have been made.

# 3.7 Zap TK 2.4.2

### Fall 2021

• Minor internal improvements have been made.

# 3.8 Zap TK 2.4.1

### July 2021

Minor internal improvements have been made.

# 3.9 Zap TK 2.4.0

• Minor internal improvements have been made.

# 3.10 Zap TK 2.3.7

• Minor internal improvements have been made.

# 3.11 Zap TK 2.3.6

# 3.11.1 Python-specific changes

• The runtime error that occurred when using  $OEMakeE TGrid$  in Python has been fixed.

# 3.12 Zap TK 2.3.5

• Minor internal improvements have been made.

# 3.13 Zap TK 2.3.4

• Minor internal improvements have been made.

# 3.14 Zap TK 2.3.3

• Minor internal improvements have been made.

# 3.15 Zap TK 2.3.2

• Minor internal improvements have been made.

# 3.16 Zap TK 2.3.1

• Minor internal improvements have been made.

# 3.17 Zap TK 2.3.0

• Minor internal improvements have been made.

# 3.18 Zap TK 2.2.7

## 3.18.1 Minor bug fixes

• A bug that resulted in a crash when attempting to use the OEZapDielectricModel\_Molecular model on Windows has been fixed.

# 3.19 Zap TK 2.2.6

# 3.19.1 Minor bug fixes

• A single atom identified as 3D but centered at the origin previously returned an incorrect warning about 3D coordinates being required. The internal coordinate checking has been overhauled to validate the input coordinates more systematically. Accordingly, the dimensionality of the input molecule must now be explicitly set to 3D.

# 3.19.2 Documentation changes

• The example *Calculating potential grid with optional parameters* is now synchronized for all supported languages.

# 3.20 Zap TK 2.2.5

## 3.20.1 Major bug fixes

• A serious memory leak in Zap TK was discovered and has been fixed. The leak was introduced in the 2015. Jun toolkit release and affected Zap TK and its dependent toolkits (e.g., Szmap TK).

# 3.21 Zap TK 2.2.4

• Minor internal improvements have been made.

# 3.22 Zap TK 2.2.3

## 3.22.1 Documentation fixes

• New Java and C# snippets have been added to the documentation.

# 3.23 Zap TK 2.2.2

## 3.23.1 Minor bug fixes

• Internal refactoring has been performed to improve stability.

## **3.23.2 Documentation fixes**

• Cross-references have been fixed.

# 3.24 Zap TK 2.2.1

## 3.24.1 Major Bug Fixes

• Potential buffer overrun that could cause crashes fixed.

# **3.24.2 Documentation fixes**

• The Python documentation no longer contains C++ code snippets. Those snippets have been ported to Python and included in the distribution.

# 3.25 Zap TK 2.2.0

## 3.25.1 Minor bug fixes

- Removed unbounded stack allocations.
- . OEZap. SetIterations and OEZap. GetIterations now deal with unsigned intinstead of int.

# 3.26 Zap TK 2.1.7

• Minor internal improvements.

# 3.27 Zap TK 2.1.6

## 3.27.1 New features

· OEET. Get InnerDielectric and OEET. Set InnerDielectric have been added to allow custom inner dielectric settings.

## 3.27.2 Minor bug fixes

• Warnings for missing coordinates and missing charges has been separated for better warning messages.

## **3.27.3 Documentation fixes**

• Documentation has been updated to specify units of kT.

# 3.28 Zap TK 2.1.5

## **3.28.1 Documentation fixes**

- The documentation has been updated to clarify that energies are reported in units of kT unless otherwise specified.
- A documentation mistake in OESimpleBindResults. GetUnboundLigandZapEnergy has been fixed.

# 3.29 Zap TK 2.1.4

• Internal build system improvements.

# 3.30 Zap TK 2.1.3

• Internal build system improvements.

# 3.31 Zap TK 2.1.2

## 3.31.1 New features

• Added new methods OEZap. Get Verbose and OEZap. Set Verbose to enable Zap to print out an abundance of low-level information.

# **3.31.2 Bug fixes**

- Fixed memory leak that occurred with multiple calls to OEArea. GetArea
- OEMakeETGrid now properly wrapped in Python.

# 3.32 Zap TK 2.1.1

## 3.32.1 Bug fixes

- OEZap. GetMolecule and OEZap. GetFocusTarget now return a pointer instead of a reference. This is a breaking change and any code that calls these methods will have to be updated. These methods will return a null pointer if an acceptable molecule has not been set for them.
- A warning has been added for molecules passed into Zap TK that do not return 3 when GetDimension is called. The dimension must be 3 for all molecules passed into Zap TK. The dimension is set automatically when using OEReadMolecule but a warning will be thrown and the molecule will not be accepted by Zap TK if the molecule has been made from scratch in the toolkits and SetDimension (3) has not been called on it.

# 3.32.2 Minor bug fixes

• Fixed a memory bug related to extremely large files on Windows.

# 3.33 Zap TK 2.1.0

## 3.33.1 New features

- Internal defaults have been changed for the  $OEZap$  object. The internal dielectric now has a default of 1.0, the boundary spacing now has a default of 4.0, and the default number of iterations has been set to 10. The change from 2.0 to 1.0 for the internal dielectric led to dramatically improved results when we performed tests with the Rizzo set, with the RMS error for vacuum-water transfer energy decreasing by more than half.
- Large manual update with complete examples and API documentation.
- OEZap. IsFocusTargetSet has been added, which returns a bool which indicates whether the focus target has been set.

- New examples for focusing and forces have been added
- All examples have been ported across all three languages (C++, Java, Python)
- Examples assign MMFF94 charges by default

## 3.33.2 Bug fixes

- Internal and external dielectrics are now properly reset each time the OEBind instance is used.
- Internal error checking has been added so that no internal calculations will be attempted if  $OEZap$ . SetMolecule fails. (OEZap. SetMolecule most often fails because all charges are equal to zero.) Calls to methods that would attempt to run internal calculations (e.g. OEZap. CalcSolvationEnergy) will return zero or false.
- Internal summations in *OEBind* use doubles now instead of floats for appropriate precision
- Charges are properly assigned to both the refmol and fitmol in the calc\_et.cpp example.
- Examples perform error checking when opening files

# 3.34 Zap TK 2.0.0

## 3.34.1 New features

• This is the first official release of the C++ version of Zap TK. Note that this is a significant change in the API as we migrate from the C API to the new C++ API built on top of OEChem.

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

### **CHAPTER**

## **SIX**

# **CITATION**

# 6.1 Orion<sup>®</sup> Floes

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

# **6.2 Toolkits and Applications**

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

# **6.3 OpenEye Web Services**

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

# **SEVEN**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                                         | License                                                                                     |
|-------------------------------|---------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                            |                                                                                             |
| absl-py                       | https://github.com/abseil/abseil-py                                             |                                                                                             |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                             |                                                                                             |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                           |                                                                                             |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                           | N/A                                                                                         |
| AmberUtils                    | http://ambermd.org                                                              | N/A                                                                                         |
| ambit                         | https://github.com/khimaros/ambit                                               |                                                                                             |
| amqp                          | https://github.com/celery/py-amqp                                               |                                                                                             |
| anaconda-anon-usage           | Orion Floes                                                                     |                                                                                             |
| angular                       | https://github.com/angular/angular.js                                           |                                                                                             |
| angular-animate               | https://github.com/angular/angular.js                                           |                                                                                             |
| angular-cache                 | https://github.com/jmdobry/angular-cache                                        |                                                                                             |
| angular-cookies               | https://github.com/angular/angular.js                                           |                                                                                             |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                                |                                                                                             |
| angular-mocks                 | https://github.com/angular/angular.js                                           |                                                                                             |
| angular-resource              | https://github.com/angular/angular.js                                           |                                                                                             |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                                |                                                                                             |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                           |                                                                                             |
| angular-ui-router             | https://github.com/angular-ui/ui-router                                         |                                                                                             |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                              |                                                                                             |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                                    |                                                                                             |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                                        |                                                                                             |
| annotated-types               | https://github.com/annotated-types/annotated-types                              |                                                                                             |
| anyio                         | https://github.com/agronholm/anyio                                              |                                                                                             |
| appdirs                       | http://github.com/ActiveState/appdirs                                           |                                                                                             |
| appengine                     | https://google.golang.org/appengine                                             |                                                                                             |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                               |                                                                                             |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md                      |                                                                                             |
| Name of Project               | Website                                                                         | License                                                                                     |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                            | https://                                                                                    |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                   | https://                                                                                    |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                      | https://                                                                                    |
| ascii85                       | https://github.com/huandu/node-ascii85                                          | https://                                                                                    |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                  | https://                                                                                    |
| asgiref                       | https://github.com/django/asgiref/                                              | https://                                                                                    |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                             | https://                                                                                    |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render           | https://                                                                                    |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers               | https://                                                                                    |
| assertions                    | https://github.com/smartystreets/assertions                                     | https://                                                                                    |
| asttokens                     | https://github.com/gristlabs/asttokens                                          | https://                                                                                    |
| astunparse                    | https://github.com/simonpercivall/astunparse                                    | https://                                                                                    |
| async-lru                     | https://github.com/aio-libs/async-lru                                           | https://                                                                                    |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                       | https://                                                                                    |
| atk-1.0                       | https://docs.gtk.org/atk/                                                       | https://                                                                                    |
| atomic                        | https://github.com/uber-go/atomic                                               | https://                                                                                    |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                | https://                                                                                    |
| attrs                         | https://www.attrs.org/                                                          | https://                                                                                    |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                               | https://                                                                                    |
| Babel                         | https://github.com/python-babel/babel                                           | https://                                                                                    |
| backcall                      | https://github.com/takluyver/backcall                                           | https://                                                                                    |
| backports                     | https://github.com/brandon-rhodes/backports                                     | https://                                                                                    |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                         | https://                                                                                    |
| base62                        | https://github.com/kare/base62                                                  | https://                                                                                    |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                  | https://                                                                                    |
| billiard                      | https://github.com/celery/billiard                                              | https://                                                                                    |
| biopython                     | https://biopython.org                                                           | https://                                                                                    |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                   | https://                                                                                    |
| bitset                        | https://github.com/willf/bitset                                                 | https://                                                                                    |
| blas                          | https://www.netlib.org/blas/                                                    | https://                                                                                    |
| bleach                        | https://github.com/mozilla/bleach                                               | https://                                                                                    |
| blessings                     | https://github.com/erikrose/blessings                                           | https://                                                                                    |
| blinker                       | https://pythonhosted.org/blinker/                                               | https://                                                                                    |
| blosc                         | https://github.com/Blosc/python-blosc                                           | https://                                                                                    |
| blosc2                        | https://github.com/Blosc/python-blosc2                                          | https://                                                                                    |
| boltons                       | https://github.com/mahmoud/boltons                                              | https://                                                                                    |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html           | https://                                                                                    |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html           | https://                                                                                    |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                  | https://                                                                                    |
| boto3                         | https://github.com/boto/boto3                                                   | https://                                                                                    |
| botocore                      | https://github.com/boto/botocore                                                | https://                                                                                    |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                          | https://                                                                                    |
| Brotli                        | https://github.com/google/brotli                                                | https://                                                                                    |
| brotli-bin                    | https://github.com/google/brotli                                                | https://                                                                                    |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                            | https://                                                                                    |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                                      | https://                                                                                    |
| bson                          | http://github.com/py-bson/bson                                                  | https://                                                                                    |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                           | https://                                                                                    |
| bzip2                         | https://www.bzip.org                                                            | https://                                                                                    |
| Name of Project               | Website                                                                         | License                                                                                     |
| c-ares                        | https://github.com/c-ares/c-ares                                                | https:/                                                                                     |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                        | https:/                                                                                     |
| cached-property               | https://github.com/pydanny/cached-property                                      | https:/                                                                                     |
| cachetools                    | https://github.com/tkem/cachetools/                                             | https:/                                                                                     |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                       | https:/                                                                                     |
| canvas                        | https://github.com/Automattic/node-canvas                                       | https:/                                                                                     |
| cctbx                         | https://github.com/cctbx/cctbx_project                                          | https:/                                                                                     |
| celery                        | https://github.com/celery/celery                                                | https:/                                                                                     |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                     | https:/                                                                                     |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                       | https:/                                                                                     |
| cffi                          | https://github.com/python-cffi/cffi                                             | https:/                                                                                     |
| cftime                        | https://pypi.org/project/cftime/                                                | https:/                                                                                     |
| chardet                       | https://github.com/chardet/chardet                                              | https:/                                                                                     |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                    | https:/                                                                                     |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                         | https:/                                                                                     |
| click                         | https://palletsprojects.com/p/click/                                            | https:/                                                                                     |
| click-completion              | https://github.com/click-contrib/click-completion                               | https:/                                                                                     |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                               | https:/                                                                                     |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                  | https:/                                                                                     |
| click-repl                    | https://github.com/untitaker/click-repl                                         | https:/                                                                                     |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                        | https:/                                                                                     |
| cmake                         | https://cmake.org/                                                              | https:/                                                                                     |
| colorama                      | https://github.com/tartley/colorama                                             | https:/                                                                                     |
| comm                          | https://github.com/ipython/comm                                                 | https:/                                                                                     |
| compose                       | https://github.com/docker/compose                                               | https:/                                                                                     |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                    | https:/                                                                                     |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                  | https:/                                                                                     |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                 | https:/                                                                                     |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                        | https:/                                                                                     |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                       | https:/                                                                                     |
| confuse                       | https://github.com/beetbox/confuse                                              | https:/                                                                                     |
| contourpy                     | https://github.com/contourpy/contourpy                                          | https:/                                                                                     |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                           | https:/                                                                                     |
| cryptography                  | https://github.com/pyca/cryptography                                            | https:/                                                                                     |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                            | https:/                                                                                     |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                       | https:/                                                                                     |
| cupy-cuda113                  | https://cupy.dev/                                                               | https:/                                                                                     |
| curl                          | https://curl.se                                                                 | https:/                                                                                     |
| cycler                        | https://github.com/matplotlib/cycler                                            | https:/                                                                                     |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                         | https:/                                                                                     |
| Cython                        | https://cython.org                                                              | https:/                                                                                     |
| d3                            | https://github.com/mbostock/d3                                                  | https:/                                                                                     |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                       | https:/                                                                                     |
| ddsketch                      | https://github.com/datadog/sketches-py                                          | https:/                                                                                     |
| debugpy                       | https://aka.ms/debugpy                                                          | https:/                                                                                     |
| decimal                       | https://github.com/shopspring/decimal                                           | https:/                                                                                     |
| decorator                     | https://github.com/micheles/decorator                                           | https:/                                                                                     |
| deepdiff                      | https://github.com/seperman/deepdiff                                            | https:/                                                                                     |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                         | https:/                                                                                     |
| Name of Project               | Website                                                                         | License                                                                                     |
| defusedxml                    | https://github.com/tiran/defusedxml                                             | https:/                                                                                     |
| dill                          | https://github.com/uqfoundation/dill                                            | https:/                                                                                     |
| distro                        | Orion Flores                                                                    | https:/                                                                                     |
| Django                        | https://www.djangoproject.com/                                                  | https:/                                                                                     |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                | https:/                                                                                     |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                               | https:/                                                                                     |
| django-csp                    | https://github.com/mozilla/django-csp                                           | https:/                                                                                     |
| django-extensions             | https://github.com/django-extensions/django-extensions                          | https:/                                                                                     |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                      | https:/                                                                                     |
| django-redis                  | https://github.com/jazzband/django-redis                                        | https:/                                                                                     |
| django-taggit                 | https://github.com/jazzband/django-taggit                                       | https:/                                                                                     |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                          | https:/                                                                                     |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                          | https:/                                                                                     |
| djangorestframework           | https://www.django-rest-framework.org/                                          | https:/                                                                                     |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                  | https:/                                                                                     |
| dm-tree                       | https://github.com/deepmind/tree                                                | https:/                                                                                     |
| docker-py                     | https://github.com/docker/docker-py/                                            | https:/                                                                                     |
| docopt                        | https://docopt.org                                                              | https:/                                                                                     |
| docutils                      | https://docutils.sourceforge.io                                                 | https:/                                                                                     |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                     |                                                                                             |
| editdistance                  | https://github.com/roy-ht/editdistance                                          | https:/                                                                                     |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                           | https:/                                                                                     |
| einops                        | https://github.com/arogozhnikov/einops                                          | https:/                                                                                     |
| entrypoints                   | https://github.com/takluyver/entrypoints                                        | https:/                                                                                     |
| errors                        | https://github.com/pkg/errors                                                   | https:/                                                                                     |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                          | https:/                                                                                     |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                   | https:/                                                                                     |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                     | https:/                                                                                     |
| executing                     | https://github.com/alexmojaki/executing                                         | https:/                                                                                     |
| expat                         | https://libexpat.github.io                                                      | https:/                                                                                     |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                               | https:/                                                                                     |
| fastrlock                     | https://github.com/scoder/fastrlock                                             | https:/                                                                                     |
| fftw                          | https://www.fftw.org                                                            | comm                                                                                        |
| filebuffer                    | https://github.com/mattetti/filebuffer                                          | https:/                                                                                     |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                         | https:/                                                                                     |
| finufft                       | https://github.com/flatironinstitute/finufft                                    | https:/                                                                                     |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                     | https:/                                                                                     |
| flatbuffers                   | https://google.github.io/flatbuffers/                                           | https:/                                                                                     |
| flit-core                     | https://github.com/pypa/flit                                                    | https:/                                                                                     |
| FLTK                          | https://www.fltk.org/index.php                                                  | https:/                                                                                     |
| fmt                           | https://fmt.dev/latest/index.html                                               | https:/                                                                                     |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                     | https:/                                                                                     |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                  | https:/                                                                                     |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                   | https:/                                                                                     |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                               | https:/                                                                                     |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                        | https:/                                                                                     |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                           | https:/                                                                                     |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                         | https:/                                                                                     |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                             | https:/                                                                                     |
| Name of Project               | Website                                                                         | License                                                                                     |
| fonttools                     | https://github.com/fonttools/fonttools                                          | https:/                                                                                     |
| freetype                      | https://freetype.org                                                            | https:/                                                                                     |
| fribidi                       | https://github.com/fribidi/fribidi                                              | https:/                                                                                     |
| frozendict                    | https://github.com/Marco-Sulla/frozendict                                       | https:/                                                                                     |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                          | https:/                                                                                     |
| fsmlite                       | https://github.com/tkem/fsmlite                                                 | https:/                                                                                     |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                       | https:/                                                                                     |
| funcy                         | https://github.com/Suor/funcy                                                   | https:/                                                                                     |
| gast                          | https://github.com/serge-sans-paille/gast                                       | https:/                                                                                     |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                            | https:/                                                                                     |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                         | https:/                                                                                     |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                       | https:/                                                                                     |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                         | https:/                                                                                     |
| genproto                      | https://google.golang.org/genproto/googleapis                                   | https:/                                                                                     |
| geometric                     | https://openbase.com/python/geometric                                           | https:/                                                                                     |
| giflib                        | https://giflib.sourceforge.net                                                  | https:/                                                                                     |
| glib                          | https://docs.gtk.org/glib/                                                      | https:/                                                                                     |
| <b>GLM</b> Library            | https://github.com/g-truc/glm                                                   | https:/                                                                                     |
| gls                           | https://github.com/jtolds/gls                                                   | https:/                                                                                     |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                       | https:/                                                                                     |
| go-connections                | https://github.com/docker/go-connections                                        | https:/                                                                                     |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                        | https:/                                                                                     |
| go-getter                     | https://github.com/hashicorp/go-getter                                          | https:/                                                                                     |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                         | https:/                                                                                     |
| go-ini                        | https://github.com/go-ini/ini                                                   | https:/                                                                                     |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                         | https:/                                                                                     |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                     | https:/                                                                                     |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                       | https:/                                                                                     |
| go-ole                        | https://github.com/go-ole/go-ole                                                | https:/                                                                                     |
| go-pg                         | https://github.com/go-pg/pg                                                     | https:/                                                                                     |
| go-redis                      | https://github.com/go-redis/redis/v8                                            | https:/                                                                                     |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                        | https:/                                                                                     |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                        | https:/                                                                                     |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                          | https:/                                                                                     |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                               | https:/                                                                                     |
| go-units                      | https://github.com/docker/go-units                                              | https:/                                                                                     |
| go-version                    | https://github.com/hashicorp/go-version                                         | https:/                                                                                     |
| go-zglob                      | https://github.com/mattn/go-zglob                                               | https:/                                                                                     |
| go.opencensus                 | https://go.opencensus.io                                                        | https:/                                                                                     |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                            | https:/                                                                                     |
| goconvey                      | https://github.com/smartystreets/goconvey                                       | https:/                                                                                     |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                   | https:/                                                                                     |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                   | https:/                                                                                     |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib               | https:/                                                                                     |
| google-cloud-go               | https://cloud.google.com/go                                                     | https:/                                                                                     |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                             | https:/                                                                                     |
| google-pasta                  | https://github.com/google/pasta                                                 | https:/                                                                                     |
| google.golang.org/api         | https://google.golang.org/api                                                   | https:/                                                                                     |
| gopsutil                      | https://github.com/shirou/gopsutil                                              | https:/                                                                                     |
| Name of Project               | Website                                                                         | License                                                                                     |
| gorilla websocket             | https://github.com/gorilla/websocket                                            |                                                                                             |
| graphite2                     | https://github.com/silnrsi/graphite                                             |                                                                                             |
| graphviz                      | https://graphviz.org/                                                           |                                                                                             |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                      |                                                                                             |
| groupcache                    | https://github.com/golang/groupcache                                            |                                                                                             |
| grpc                          | https://google.golang.org/grpc                                                  |                                                                                             |
| grpc-cpp                      | https://github.com/grpc/grpc                                                    |                                                                                             |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                               |                                                                                             |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                              |                                                                                             |
| gts                           | https://sourceforge.net/projects/gts/                                           |                                                                                             |
| h5py                          | https://www.h5py.org                                                            |                                                                                             |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                            |                                                                                             |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                       |                                                                                             |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                        |                                                                                             |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                        |                                                                                             |
| he                            | https://github.com/mathiasbynens/he                                             |                                                                                             |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                  |                                                                                             |
| html5lib                      | https://github.com/html5lib/html5lib-python                                     |                                                                                             |
| htslib                        | https://www.htslib.org                                                          |                                                                                             |
| humanize                      | https://github.com/jmoiron/humanize                                             |                                                                                             |
| icu                           | https://github.com/unicode-org/icu                                              |                                                                                             |
| idna                          | https://github.com/kjd/idna                                                     |                                                                                             |
| imageio                       | https://github.com/imageio/imageio                                              |                                                                                             |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                       |                                                                                             |
| ImmuneBuilder                 | https://github.com/oxpig/ImmuneBuilder/tree/main                                |                                                                                             |
| importlib-metadata            | https://github.com/python/importlib_metadata                                    |                                                                                             |
| importlib_resources           | https://github.com/python/importlib_resources                                   |                                                                                             |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                  |                                                                                             |
| inflection                    | https://github.com/jinzhu/inflection                                            |                                                                                             |
| ini.v1                        | https://gopkg.in/ini.v1                                                         |                                                                                             |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                         |                                                                                             |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                     |                                                                                             |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                        |                                                                                             |
| ipykernel                     | https://ipython.org                                                             |                                                                                             |
| ipython                       | https://ipython.org                                                             |                                                                                             |
| ipython-genutils              | http://ipython.org                                                              |                                                                                             |
| ipywidgets                    | https://jupyter.org                                                             |                                                                                             |
| isodate                       | https://github.com/gweis/isodate/                                               |                                                                                             |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                     |                                                                                             |
| jax                           | https://github.com/google/jax                                                   |                                                                                             |
| jaxlib                        | https://github.com/google/jax                                                   |                                                                                             |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                          |                                                                                             |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                            |                                                                                             |
| jmespath                      | https://github.com/jmespath/jmespath.py                                         |                                                                                             |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                        |                                                                                             |
| jpeg                          | https://www.ijg.org                                                             |                                                                                             |
| json5                         | https://github.com/dpranke/pyjson5                                              |                                                                                             |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                     |                                                                                             |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                |                                                                                             |
| Name of Project               | Website                                                                         | License                                                                                     |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                        | https://github.com/jsonpickle/jsonpickle/blob/master/LICENSE                                |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                              | https://github.com/stefankoegl/python-json-pointer/blob/master/LICENSE                      |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                 | https://github.com/python-jsonschema/jsonschema/blob/main/LICENSE                           |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications                  | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/LICENSE            |
| jstat                         | https://github.com/jstat/jstat                                                  | https://github.com/jstat/jstat/blob/master/LICENSE                                          |
| jupyter-client                | https://jupyter.org                                                             | https://github.com/jupyter/jupyter_client/blob/main/LICENSE                                 |
| jupyter-core                  | https://jupyter.org                                                             | https://github.com/jupyter/jupyter_core/blob/main/LICENSE                                   |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                       | https://github.com/jupyter/jupyter_events/blob/main/LICENSE                                 |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                   | https://github.com/jupyter-lsp/jupyterlab-lsp/blob/main/LICENSE                             |
| jupyter-server                | https://jupyter.org                                                             | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE                          |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                        | https://github.com/jupyterlab/jupyterlab/blob/master/LICENSE                                |
| jupyterlab-pygments           | http://jupyter.org                                                              | https://github.com/jupyterlab/pygments/blob/main/LICENSE                                    |
| jupyterlab-widgets            | http://jupyter.org                                                              | https://github.com/jupyter-widgets/ipywidgets/blob/main/LICENSE                             |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                 | https://github.com/jupyterlab/jupyterlab_server/blob/main/LICENSE                           |
| jupyter-server                | https://github.com/jupyter-server/jupyter_server                                | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE                          |
| jupyter-server-terminals      | https://github.com/jupyter-server/jupyter_server_terminals                      | https://github.com/jupyter-server/jupyter_server_terminals/blob/main/LICENSE                |
| kaleido                       | https://github.com/plotly/Kaleido                                               | https://github.com/plotly/Kaleido/blob/master/LICENSE                                       |
| keras                         | https://github.com/keras-team/keras                                             | https://github.com/keras-team/keras/blob/master/LICENSE                                     |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                               | https://github.com/keras-team/keras-preprocessing/blob/master/LICENSE                       |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                       | https://github.com/keras-team/keras-tuner/blob/master/LICENSE                               |
| keyring                       | https://github.com/jaraco/keyring                                               | https://github.com/jaraco/keyring/blob/main/LICENSE                                         |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                  | https://github.com/sassoftware/python-keyutils/blob/main/LICENSE                            |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                    | https://github.com/nucleic/kiwi/blob/master/LICENSE                                         |
| kombu                         | https://kombu.readthedocs.io                                                    | https://github.com/celery/kombu/blob/master/LICENSE                                         |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                   | https://web.mit.edu/kerberos/krb5.html                                                      |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                        | https://github.com/haifeng-jin/kt-legacy/blob/master/LICENSE                                |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                | https://github.com/scientific-python/lazy_loader/blob/main/LICENSE                          |
| lcms2                         | https://www.littlecms.com                                                       | https://github.com/mm2/Little-CMS/blob/master/COPYING                                       |
| lerc                          | https://github.com/Esri/lerc                                                    | https://github.com/Esri/lerc/blob/master/LICENSE                                            |
| libarchive                    | http://www.libarchive.org                                                       | https://github.com/libarchive/libarchive/blob/master/COPYING                                |
| libblas                       | https://www.netlib.org/blas/                                                    | https://netlib.org/blas/faq.html#license                                                    |
| libbrotlicommon               | https://github.com/google/brotli                                                | https://github.com/google/brotli/blob/master/LICENSE                                        |
| libbrotlidec                  | https://github.com/google/brotli                                                | https://github.com/google/brotli/blob/master/LICENSE                                        |
| libbrotlienc                  | https://github.com/google/brotli                                                | https://github.com/google/brotli/blob/master/LICENSE                                        |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                       | N/A                                                                                         |
| libclang                      | https://github.com/llvm/llvm-project                                            | https://github.com/llvm/llvm-project/blob/main/llvm/LICENSE.TXT                             |
| libcurl                       | https://curl.se/libcurl/                                                        | https://github.com/curl/curl/blob/master/COPYING                                            |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                           | https://github.com/llvm-mirror/libcxx/blob/master/LICENSE.TXT                               |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html      | https://download.oracle.com/otn-pub/oss/berkeley-db/LICENSE                                 |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                          | https://github.com/ebiggers/libdeflate/blob/master/COPYING                                  |
| libedit                       | https://thrysoee.dk/editline/                                                   | http://thrysoee.dk/editline/COPYING                                                         |
| libev                         | https://software.schmorp.de/pkg/libev.html                                      | https://github.com/enki/libev/blob/master/LICENSE                                           |
| libffi                        | https://github.com/libffi/libffi                                                | https://github.com/libffi/libffi/blob/master/LICENSE                                        |
| libgcrypt                     | https://gnupg.org/software/index.html                                           | https://git.gnupg.org/cgi-bin/gitweb.cgi?p=libgcrypt.git;a=blob_plain;f=COPYING.LIB;hb=HEAD |
| libgd                         | https://libgd.github.io                                                         | https://github.com/libgd/libgd/blob/master/COPYING                                          |
| libglib                       | https://github.com/PolMine/libglib                                              | https://github.com/PolMine/libglib/blob/master/COPYING                                      |
| libiconv                      | https://www.gnu.org/software/libiconv/                                          | https://git.savannah.gnu.org/gitweb/?p=libiconv.git;a=blob_plain;f=COPYING.LIB;hb=HEAD      |
| Name of Project               | Website                                                                         | License                                                                                     |
| libint                        | https://tinyurl.com/yvw97wbw                                                    | https:/                                                                                     |
| liblapack                     | http://www.netlib.org/lapack/                                                   | https:/                                                                                     |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                     | https:/                                                                                     |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23 | https:/                                                                                     |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community            | https:/                                                                                     |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                   | https:/                                                                                     |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                              | https:/                                                                                     |
| libopenblas                   | https://www.openblas.net/                                                       | https:/                                                                                     |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                      | https:/                                                                                     |
| libpq                         | https://www.postgresql.org/                                                     | https:/                                                                                     |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                          | https:/                                                                                     |
| libsolv                       | https://github.com/openSUSE/libsolv                                             | https:/                                                                                     |
| libssh2                       | https://github.com/libssh2/libssh2                                              | https:/                                                                                     |
| libtiff                       | https://www.libtiff.org/                                                        | https:/                                                                                     |
| libtrust                      | https://github.com/docker/libtrust                                              | https:/                                                                                     |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                       | https:/                                                                                     |
| libuv                         | https://github.com/libuv/libuv                                                  | https:/                                                                                     |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                  | https:/                                                                                     |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                  | https:/                                                                                     |
| libxc                         | https://www.tddft.org/programs/libxc/                                           | https:/                                                                                     |
| libxcb                        | https://xcb.freedesktop.org                                                     | https:/                                                                                     |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                           | https:/                                                                                     |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                | https:/                                                                                     |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                             | https:/                                                                                     |
| libzlib                       | https://zlib.net                                                                | https:/                                                                                     |
| lime                          | https://github.com/marcotor/lime                                                | https:/                                                                                     |
| lit                           | http://llvm.org                                                                 | https:/                                                                                     |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                           | https:/                                                                                     |
| llvmlite                      | http://llvmlite.readthedocs.io                                                  | https:/                                                                                     |
| loader-utils                  | https://github.com/webpack/loader-utils                                         | https:/                                                                                     |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                     | https:/                                                                                     |
| logrus                        | https://github.com/sirupsen/logrus                                              | https:/                                                                                     |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                              | https:/                                                                                     |
| lxml                          | https://lxml.de                                                                 | https:/                                                                                     |
| lz4-c                         | https://www.lz4.org/                                                            | https:/                                                                                     |
| markdown                      | https://github.com/evilstreak/markdown-js                                       | https:/                                                                                     |
| markdown-it-py                | Orion Floes                                                                     | https:/                                                                                     |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                       | https:/                                                                                     |
| matplotlib                    | https://matplotlib.org                                                          | https:/                                                                                     |
| matplotlib-base               | https://matplotlib.org                                                          | https:/                                                                                     |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                    | https:/                                                                                     |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                        | https:/                                                                                     |
| mdtraj                        | https://www.mdtraj.org/                                                         | https:/                                                                                     |
| mdurl                         | Orion Floes<br>Orion Floes                                                      | https:/                                                                                     |
| menuinst                      |                                                                                 | https:/                                                                                     |
| mergo                         | https://github.com/imdario/mergo                                                | https:/                                                                                     |
| mistune                       | https://github.com/lepture/mistune                                              | https:/                                                                                     |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                      | https:/                                                                                     |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                          | https:/                                                                                     |
| Name of Project               | Website                                                                         | License                                                                                     |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                       | https:/                                                                                     |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                      | https:/                                                                                     |
| ml-dtypes                     | Orion Floes                                                                     | https:/                                                                                     |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                      | https:/                                                                                     |
| moment                        | https://github.com/moment/moment                                                |                                                                                             |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                 | https:/                                                                                     |
| more-itertools                | https://github.com/more-itertools/more-itertools                                | https:/<br>https:/                                                                          |
| mpiplus                       | https://github.com/choderalab/mpiplus                                           |                                                                                             |
| mpmath                        | http://mpmath.org/                                                              | https:/                                                                                     |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                | https:/                                                                                     |
| msgpack                       | https://msgpack.org/                                                            | https:/                                                                                     |
| multidict                     | https://github.com/aio-libs/multidict                                           | https:/                                                                                     |
| multierr                      | https://go.uber.org/multierr                                                    | https:/                                                                                     |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                    | https:/                                                                                     |
| munkres                       | https://software.clapper.org/munkres/                                           | https:/                                                                                     |
| myesui uuid                   | https://github.com/myesui/uuid                                                  | https:/                                                                                     |
| namex                         | Orion Floes                                                                     | https:/                                                                                     |
| nbclassic                     | http://jupyter.org                                                              | https:/                                                                                     |
| nbclient                      | https://jupyter.org                                                             | https:/                                                                                     |
| nbconvert                     | https://jupyter.org                                                             | https:/                                                                                     |
| nbformat                      | http://jupyter.org                                                              | https:/                                                                                     |
| ncurses                       | https://invisible-island.net/ncurses/                                           | https:/                                                                                     |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                         | https:/                                                                                     |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                   | https:/                                                                                     |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                        | https:/                                                                                     |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                        | https:/                                                                                     |
| networkx                      | https://networkx.org                                                            | https:/                                                                                     |
| nfpm                          | https://github.com/goreleaser/nfpm                                              | https:/                                                                                     |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                         | https:/                                                                                     |
| ng-toast                      | https://github.com/tameraydin/ngToast                                           | https:/                                                                                     |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                   | https:/                                                                                     |
| ngVue                         | https://github.com/ngVue/ngVue                                                  | https:/                                                                                     |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                  | https:/                                                                                     |
| nodejs                        | https://nodejs.org/en/                                                          | https:/                                                                                     |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                  | https:/                                                                                     |
| notebook                      | http://jupyter.org                                                              | https:/                                                                                     |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                        | https:/                                                                                     |
| notebook_shim                 | http://jupyter.org                                                              | https:/                                                                                     |
| numba                         | https://numba.pydata.org                                                        | https:/                                                                                     |
| numcpus                       | https://github.com/tklauser/numcpus                                             | https:/                                                                                     |
| numexpr                       | https://github.com/pydata/numexpr                                               | https:/                                                                                     |
| numpy                         | https://numpy.org                                                               | https:/                                                                                     |
| numpy-base                    | https://numpy.org                                                               | https:/                                                                                     |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                            | https:/                                                                                     |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| Name of Project               | Website                                                                         | License                                                                                     |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                          | https:/                                                                                     |
| Oat++                         | https://oatpp.io/                                                               | https:/                                                                                     |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                            | https:/                                                                                     |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                              | https:/                                                                                     |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                         | https:/                                                                                     |
| olefile                       | https://www.decalage.info/python/olefileio                                      | https:/                                                                                     |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                           | https:/                                                                                     |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                    | https:/                                                                                     |
| OpenFF                        | https://openforcefield.org/                                                     | https:/                                                                                     |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                         | https:/                                                                                     |
| openff-forcefields            | https://openforcefield.org                                                      | https:/                                                                                     |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                            | https:/                                                                                     |
| openff-models                 | https://github.com/openforcefield/openff-models                                 | https:/                                                                                     |
| openff-toolkit                | https://openforcefield.org                                                      | https:/                                                                                     |
| openff-toolkit-base           | https://openforcefield.org                                                      | https:/                                                                                     |
| openff-units                  | https://github.com/openforcefield/openff-units                                  | https:/                                                                                     |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                              | https:/                                                                                     |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                           | https:/                                                                                     |
| openldap                      | https://www.openldap.org/software/repo.html                                     | https:/                                                                                     |
| OpenMM                        | https://openmm.org                                                              | https:/                                                                                     |
| openmmtools                   | https://github.com/choderalab/openmmtools                                       | https:/                                                                                     |
| openmoltools                  | https://github.com/choderalab/openmoltools                                      | https:/                                                                                     |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                      | https:/                                                                                     |
| openssl                       | https://www.openssl.org                                                         | https:/                                                                                     |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                          | https:/                                                                                     |
| OptKing                       | https://github.com/psi-rking/optking                                            | https:/                                                                                     |
| oscrypto                      | https://github.com/wbond/oscrypto                                               | https:/                                                                                     |
| overrides                     | https://github.com/mkorpela/overrides                                           | https:/                                                                                     |
| packaging                     | https://github.com/pypa/packaging                                               | https:/                                                                                     |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                           | https:/                                                                                     |
| pandas                        | https://pandas.pydata.org                                                       | https:/                                                                                     |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                             | https:/                                                                                     |
|                               |                                                                                 | -li                                                                                         |
| Name of Project               | Website                                                                         | Licen                                                                                       |
| panedr                        | https://github.com/MDAnalysis/panedr                                            | https:/                                                                                     |
| pango                         | https://pango.gnome.org                                                         | https:/                                                                                     |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                 | https:/                                                                                     |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                          | https:/                                                                                     |
| parso                         | https://parso.readthedocs.io/en/latest/                                         | https:/                                                                                     |
| pathos                        | https://github.com/uqfoundation/pathos                                          | https:/                                                                                     |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                         | https:/                                                                                     |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                              | https:/                                                                                     |
| pbr                           | https://docs.openstack.org/pbr/latest/                                          | https:/                                                                                     |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                     | https:/                                                                                     |
| pcre                          | https://www.pcre.org                                                            | https:/                                                                                     |
| pcre2                         | https://www.pcre.org                                                            | https:/                                                                                     |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                           | https:/                                                                                     |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                              | https:/                                                                                     |
| pexpect                       | https://pexpect.readthedocs.io/                                                 | https:/                                                                                     |
| pgconn                        | https://github.com/jackc/pgconn                                                 | https:/                                                                                     |
| pgio                          | https://github.com/jackc/pgio                                                   | https:/                                                                                     |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                             | https:/                                                                                     |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                            | https:/                                                                                     |
| pgtype                        | https://github.com/jackc/pgtype                                                 | https:/                                                                                     |
| pgx                           | https://github.com/jackc/pgx/v4                                                 | https:/                                                                                     |
| phonopy                       | https://github.com/phonopy/phono3py                                             | https:/                                                                                     |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                      | https:/                                                                                     |
| Pillow                        | https://python-pillow.org                                                       | https:/                                                                                     |
| Pint                          | https://pint.readthedocs.io/en/stable/                                          | https:/                                                                                     |
| pip                           | https://pip.pypa.io/                                                            | https:/                                                                                     |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                        | https:/                                                                                     |
| pixman                        | https://pixman.org                                                              | https:/                                                                                     |
| pkginfo                       | https://launchpad.net/pkginfo                                                   | https:/                                                                                     |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                    | https:/                                                                                     |
| plotly                        | https://plotly.com/python/                                                      | https:/                                                                                     |
| plotly-orca                   | https://github.com/plotly/orca                                                  | https:/                                                                                     |
| plotly.js                     | https://github.com/plotly/plotly.js                                             | https:/                                                                                     |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                              | https:/                                                                                     |
| $\overline{\text{pooch}}$     | https://github.com/fatiando/pooch                                               | https:/                                                                                     |
| pox                           | https://github.com/uqfoundation/pox                                             | https:/                                                                                     |
| ppft                          | https://github.com/uqfoundation/ppft                                            | https:/                                                                                     |
| pq                            | https://github.com/lib/pq                                                       | https:/                                                                                     |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                   | https:/                                                                                     |
| prometheus-client             | https://github.com/prometheus/client_python                                     | https:/                                                                                     |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                         | https:/                                                                                     |
| protobuf                      | https://google.golang.org/protobuf                                              | https:/                                                                                     |
| psi4                          | https://psicode.org                                                             | https:/                                                                                     |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                        | https:/                                                                                     |
| psycopg2                      | https://psycopg.org/                                                            | https:/                                                                                     |
| PTable                        | https://github.com/kxxoling/PTable                                              | https:/                                                                                     |
| pthread-stubs                 | https://xcb.freedesktop.org                                                     | https:/                                                                                     |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                    | https:/                                                                                     |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                          | http://                                                                                     |
|                               |                                                                                 |                                                                                             |
| Name of Project               | Website                                                                         | License                                                                                     |
| py                            | https://py.readthedocs.io/en/latest/                                            | https:/                                                                                     |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                         | https:/                                                                                     |
| pyasn1                        | https://github.com/etingof/pyasn1                                               | https:/                                                                                     |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                       | https:/                                                                                     |
| pybind11-abi                  | https://github.com/pybind/pybind11                                              | https:/                                                                                     |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                             | https:/                                                                                     |
| pycosat                       | https://github.com/conda/pycosat                                                | https:/                                                                                     |
| pycparser                     | https://github.com/eliben/pycparser                                             | https:/                                                                                     |
| pydantic                      | https://pydantic-docs.helpmanual.io                                             | https:/                                                                                     |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                       | https:/                                                                                     |
| pyedr                         | https://github.com/MDAnalysis/panedr                                            | https:/                                                                                     |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                            | https:/                                                                                     |
| Pygments                      | https://pygments.org                                                            | https:/                                                                                     |
| pygraphviz                    | https://pygraphviz.github.io                                                    | https:/                                                                                     |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                        | https:/                                                                                     |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                    | https:/                                                                                     |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                              | https:/                                                                                     |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                               | https:/                                                                                     |
| pymbar                        | https://pymbar.org                                                              | https:/                                                                                     |
| pyOpenSSL                     | https://pyopenssl.org/                                                          | https:/                                                                                     |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                | https:/                                                                                     |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                | https:/                                                                                     |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                             | https:/                                                                                     |
| pysam                         | https://github.com/pysam-developers/pysam                                       | https:/                                                                                     |
| PySocks                       | https://github.com/Anorov/PySocks                                               | https:/                                                                                     |
| pytables                      | https://www.pytables.org                                                        | https:/                                                                                     |
| python                        | https://www.python.org/                                                         | https:/                                                                                     |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                      | https:/                                                                                     |
| python-constraint             | https://github.com/python-constraint/python-constraint                          | https:/                                                                                     |
| python-dateutil               | https://dateutil.readthedocs.io                                                 | https:/                                                                                     |
| python-json-logger            | http://github.com/madzak/python-json-logger                                     | https:/                                                                                     |
| python-ldap                   | https://www.python-ldap.org/                                                    | https:/                                                                                     |
| python3-saml                  | https://github.com/onelogin/python3-saml                                        | https:/                                                                                     |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                             | https:/                                                                                     |
| pytz                          | https://pythonhosted.org/pytz                                                   | https:/                                                                                     |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                               | https:/                                                                                     |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                              | https:/                                                                                     |
| PyYAML                        | https://pyyaml.org/                                                             | https:/                                                                                     |
| pyyaml                        | No longer available                                                             | No lor                                                                                      |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                         | https:/                                                                                     |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                           | https:/                                                                                     |
| qcengine                      | https://github.com/MolSSI/QCEngine                                              | https:/                                                                                     |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                    | https:/                                                                                     |
| ramda                         | https://github.com/ramda/ramda                                                  | https:/                                                                                     |
| rapidjson                     | https://rapidjson.org/                                                          | https:/                                                                                     |
| rdkit                         | https://www.rdkit.org                                                           | https:/                                                                                     |
| re2                           | https://github.com/google/re2                                                   | https:/                                                                                     |
| readme-renderer               | https://github.com/pypa/readme_renderer                                         |                                                                                             |
| redis-py                      | https://github.com/andymccurdy/redis-py                                         | https:/                                                                                     |
| Name of Project               | Website                                                                         | License                                                                                     |
| referencing                   | https://github.com/python-jsonschema/referencing                                | https:/                                                                                     |
| regex                         | https://github.com/mrabarnett/mrab-regex                                        | https:/                                                                                     |
| reportlab                     | https://www.reportlab.com                                                       | https:/                                                                                     |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                           | https:/                                                                                     |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                           | https:/                                                                                     |
| requests                      | https://requests.readthedocs.io                                                 | https:/                                                                                     |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                   | https:/                                                                                     |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                | https:/                                                                                     |
| resumable                     | https://github.com/stevvooe/resumable                                           | https:/                                                                                     |
| retrying                      | https://github.com/rholder/retrying                                             | https:/                                                                                     |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                   | https:/                                                                                     |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                       | https:/                                                                                     |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                   | https:/                                                                                     |
| rich                          | Orion Floes                                                                     | https:/                                                                                     |
| rpds-py                       | https://github.com/crate-py/rpds                                                | https:/                                                                                     |
| rpmpack                       | https://github.com/google/rpmpack                                               | https:/                                                                                     |
| rsa                           | https://stuvel.eu/rsa                                                           | https:/                                                                                     |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                     | https:/                                                                                     |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                | https:/                                                                                     |
| s3transfer                    | https://github.com/boto/s3transfer                                              | https:/                                                                                     |
| sasl                          | https://mellium.im/sasl                                                         | https:/                                                                                     |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                       | https:/                                                                                     |
| scikit-image                  | https://scikit-image.org                                                        | https:/                                                                                     |
| scikit-learn                  | https://scikit-learn.org/stable/                                                | https:/                                                                                     |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                      | https:/                                                                                     |
| scipy                         | https://scipy.org                                                               | https:/                                                                                     |
| seaborn                       | https://seaborn.pydata.org                                                      | https:/                                                                                     |
| seaborn-base                  | https://seaborn.pydata.org                                                      | https:/                                                                                     |
| semver                        | https://github.com/Masterminds/semver/v3                                        | https:/                                                                                     |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                         | https:/                                                                                     |
| setuptools                    | https://github.com/pypa/setuptools                                              | https:/                                                                                     |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                         | https:/                                                                                     |
| sh                            | https://github.com/amoffat/sh                                                   | https:/                                                                                     |
| shellingham                   | https://github.com/sarugaku/shellingham                                         | https:/                                                                                     |
| simint                        | https://www.bennyp.org/research/simint/                                         | https:/                                                                                     |
| six                           | https://github.com/benjaminp/six                                                | https:/                                                                                     |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                              | https:/                                                                                     |
| snappy                        | https://github.com/google/snappy                                                | https:/                                                                                     |
| sniffio                       | https://github.com/python-trio/sniffio                                          | https:/                                                                                     |
| snowballstemmer               | https://github.com/snowballstem/snowball                                        | https:/                                                                                     |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                       | https:/                                                                                     |
| spglib                        | Orion Floes                                                                     | https:/                                                                                     |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                            | https:/                                                                                     |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                           | https:/                                                                                     |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                             | https:/                                                                                     |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                            | https:/                                                                                     |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                              | https:/                                                                                     |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                              | https:/                                                                                     |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                     | https:/                                                                                     |
| Name of Project               | Website                                                                         |                                                                                             |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                      |                                                                                             |
| sqlite                        | https://sqlite.org/index.html                                                   |                                                                                             |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                        |                                                                                             |
| stack-data                    | https://github.com/alexmojaki/stack_data                                        |                                                                                             |
| starfile                      | https://github.com/alisterburt/starfile                                         |                                                                                             |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                      |                                                                                             |
| structlog                     | https://www.structlog.org/                                                      |                                                                                             |
| svglib                        | https://github.com/deeplook/svglib                                              |                                                                                             |
| sympy                         | https://sympy.org                                                               |                                                                                             |
| tables                        | https://www.pytables.org/                                                       |                                                                                             |
| tabulate                      | https://github.com/astanin/python-tabulate                                      |                                                                                             |
| tbb                           | https://github.com/oneapi-src/oneTBB                                            |                                                                                             |
| tenacity                      | https://github.com/jd/tenacity                                                  |                                                                                             |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                       |                                                                                             |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                       |                                                                                             |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                       |                                                                                             |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                        |                                                                                             |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                         |                                                                                             |
| tensorflow-io-gcs-filesystem  | https://github.com/tensorflow/io-gcs-filesystem                                 |                                                                                             |
| tensorflow-probability        | https://github.com/tensorflow/probability                                       |                                                                                             |
| termcolor                     | https://github.com/hugovk/termcolor                                             |                                                                                             |
| terminado                     | https://github.com/jupyter/terminado                                            |                                                                                             |
| testpath                      | https://github.com/jupyter/testpath                                             |                                                                                             |
| textangular                   | https://github.com/fraywing/textAngular                                         |                                                                                             |
| tf_keras                      | Orion Floes                                                                     |                                                                                             |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                         |                                                                                             |
| three                         | https://github.com/mrdoob/three.js                                              |                                                                                             |
| tifffile                      | https://github.com/cgohlke/tifffile/                                            |                                                                                             |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                              |                                                                                             |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                         |                                                                                             |
| tk                            | https://www.tcl.tk/                                                             |                                                                                             |
| toml                          | https://github.com/toml-lang/toml                                               |                                                                                             |
| tomli                         | https://github.com/hukkin/tomli                                                 |                                                                                             |
| toolz                         | https://github.com/pytoolz/toolz                                                |                                                                                             |
| torch                         | https://pytorch.org/                                                            |                                                                                             |
| tornado                       | https://www.tornadoweb.org                                                      |                                                                                             |
| tqdm                          | https://github.com/tqdm/tqdm                                                    |                                                                                             |
| tracy                         | https://github.com/gear-genomics/tracy                                          |                                                                                             |
| traitlets                     | https://github.com/ipython/traitlets                                            |                                                                                             |
| triton                        | https://github.com/openai/triton/                                               |                                                                                             |
| truststore                    | Orion Floes                                                                     |                                                                                             |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                           |                                                                                             |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                         |                                                                                             |
| twine                         | https://github.com/pypa/twine                                                   |                                                                                             |
| twinj uuid                    | https://github.com/twinj/uuid                                                   |                                                                                             |
| types                         | https://github.com/babel/babel                                                  |                                                                                             |
| typescript                    | https://github.com/Microsoft/TypeScript                                         |                                                                                             |
| typing_extensions             | https://github.com/python/typing                                                |                                                                                             |
| tzdata                        | https://github.com/python/tzdata                                                |                                                                                             |
| Name of Project               | Website                                                                         | License                                                                                     |
| tzlocal                       | https://github.com/regebro/tzlocal                                              | https:/                                                                                     |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                         | https:/                                                                                     |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                       | https:/                                                                                     |
| uritools                      | https://github.com/tkem/uritools/                                               | https:/                                                                                     |
| urllib3                       | https://urllib3.readthedocs.io/                                                 | https:/                                                                                     |
| vine                          | https://github.com/celery/vine                                                  | https:/                                                                                     |
| vue                           | https://github.com/vuejs/vue                                                    | https:/                                                                                     |
| wcwidth                       | https://github.com/jquast/wcwidth                                               | https:/                                                                                     |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                | https:/                                                                                     |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                        | https:/                                                                                     |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                         | https:/                                                                                     |
| westpa                        | Orion Floes                                                                     | http://                                                                                     |
| wheel                         | https://github.com/pypa/wheel                                                   | https:/                                                                                     |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                            | https:/                                                                                     |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                        | https:/                                                                                     |
| wsutil                        | https://github.com/yhat/wsutil                                                  | https:/                                                                                     |
| x/lint                        | https://golang.org/x/lint                                                       | https:/                                                                                     |
| x/mod                         | https://golang.org/x/mod/semver                                                 | https:/                                                                                     |
| x/net                         | https://golang.org/x/net                                                        | https:/                                                                                     |
| x/oauth2                      | https://golang.org/x/oauth2                                                     | https:/                                                                                     |
| x/sys                         | https://golang.org/x/sys                                                        | https:/                                                                                     |
| x/text                        | https://golang.org/x/text                                                       | https:/                                                                                     |
| x/tools                       | https://golang.org/x/tools                                                      | https:/                                                                                     |
| x/xerrors                     | https://golang.org/x/xerrors                                                    | https:/                                                                                     |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                           | https:/                                                                                     |
| xlrd                          | https://github.com/python-excel/xlrd                                            | https:/                                                                                     |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                        | https:/                                                                                     |
| xmltodict                     | https://github.com/martinblech/xmltodict                                        | https:/                                                                                     |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                               | https:/                                                                                     |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                  | https:/                                                                                     |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                   | https:/                                                                                     |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                  | https:/                                                                                     |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                  | https:/                                                                                     |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                | https:/                                                                                     |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                 | https:/                                                                                     |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                              | https:/<br>https:/                                                                          |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                   | https:/                                                                                     |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                           |                                                                                             |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                             | https:/                                                                                     |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                | https:/                                                                                     |
| xxhash                        | https://github.com/cespare/xxhash/v2                                            | https:/                                                                                     |
| xz                            | https://github.com/ulikunitz/xz                                                 | https:/                                                                                     |
| yaml                          | https://pyyaml.org/                                                             | https:/                                                                                     |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                              | https:/                                                                                     |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                        | https:/                                                                                     |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                        | https:/                                                                                     |
| yarl                          | https://github.com/aio-libs/yarl/                                               | https:/                                                                                     |
| yaspin                        | https://github.com/pavdmyt/yaspin                                               | https:/                                                                                     |
| yfiles                        | https://www.yworks.com/products/yfiles                                          | comm                                                                                        |
| Name of Project               | Website                                                                         | License                                                                                     |
| yml                           | https://pypi.org/project/yml/                                                   | N/A                                                                                         |
| zap                           | https://go.uber.org/zap                                                         | https://                                                                                    |
| zipp                          | https://github.com/jaraco/zipp                                                  | https://                                                                                    |
| zlib                          | https://zlib.net/                                                               | https://                                                                                    |
| zstandard                     | https://github.com/indygreg/python-zstandard                                    | https://                                                                                    |
| zstd                          | https://facebook.github.io/zstd/                                                | https://                                                                                    |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                          | https://                                                                                    |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                          | https://                                                                                    |

# **7.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses GNU Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

# **7.1.1 GCC RUNTIME LIBRARY EXCEPTION**

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the  $\rightarrow$  Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

## **7.1.2 GNU GENERAL PUBLIC LICENSE**

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

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee.

END OF TERMS AND CONDITIONS

How to Apply These Terms to Your New Programs

If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms.

To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found.

<one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode:

<program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details.

The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box".

You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>.

The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

### See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# <sub>B</sub>

Bind OEPB:: OEBind, 26 bind.py Example Code, 15

# C

calc\_et.py Example Code, 21 CalcAtomPotentials OEPB:: OEZap, 37 CalcForces OEPB:: OEZap, 37 CalcPotentialGrid OEPB:: OEZap, 37 CalcSolvationEnergy OEPB:: OEZap, 38 ClearFocusTarget OEPB:: OEZap, 38 Constructors OEPB:: OEArea, 23 OEPB:: OEBind, 25 OEPB:: OEBindResults, 27 OEPB:: OEET, 30 OEPB:: OESimpleBindResults, 33 OEPB:: OEZap, 37

# F

```
Example Code
   bind.py, 15
   calc_et.py, 21
   transfer.py, 14
   zap atompot.pv.9
   zap_focussing.py, 17
   zap_forces.py, 19
   zap_grid1.py, 3
   zap_grid2.py,4
   zap_grid3.py,7
   zap_solv1.py, 12
```

# G

GetAnalyticCoulombicBindingEnergy

OEPB:: OEBindResults, 28 GetArea OEPB:: OEArea, 23 GetBindingEnergy OEPB:: OESimpleBindResults, 33 GetBoundarySpacing OEPB:: OEZap, 38 GetBoundLigandArea OEPB:: OESimpleBindResults, 33 GetBoundLigandAreaEnergy OEPB:: OESimpleBindResults, 33 GetBoundLigandCoulombEnergy OEPB:: OEBindResults, 28 GetBoundLigandZapEnergy OEPB:: OESimpleBindResults, 34 GetBoundProteinArea OEPB:: OESimpleBindResults, 34 GetBoundProteinAreaEnergy OEPB:: OESimpleBindResults, 34 GetBoundProteinCoulombEnergy OEPB:: OEBindResults, 28 GetBoundProteinZapEnergy OEPB:: OESimpleBindResults, 34 GetBuriedArea OEPB:: OESimpleBindResults, 34 GetBuriedAreaEnergy OEPB:: OESimpleBindResults, 34 GetComplexArea OEPB:: OESimpleBindResults, 35 GetComplexAreaEnergy OEPB:: OESimpleBindResults, 35 GetComplexCoulombEnergy OEPB:: OEBindResults, 28 GetComplexZapEnergy OEPB:: OESimpleBindResults, 35 GetConf OEPB:: OESimpleBindResults, 35 GetCoulombEnergy OEPB:: OEBindResults, 28 GetDesolvationEnergy OEPB:: OEBindResults, 28 GetDielectric

OEPB:: OEET, 30 GetDielectricModel OEPB:: OEZap, 38 GetError OEPB:: OEZap, 38 GetFocusTarget OEPB:: OEZap, 38 GetGridBuffer OEPB:: OEET. 30 GetGridSpacing OEPB: : OEET, 30 OEPB:: OEZap, 39 GetInnerDielectric OEPB: : OEET, 30 OEPB:: OEZap, 39 GetInnerMask OEPB:: OEET, 30 GetIterations OEPB:: OEZap, 39 GetJoin OEPB: : OEET, 31 GetLigandDesolvationEnergy OEPB:: OEBindResults, 29 GetMethod OEPB:: OEArea, 24 GetMolecule OEPB:: OEZap, 39 GetOuterDielectric  $OEPB$ :  $OEZap$ , 39 GetOuterMask OEPB:: OEET, 31 GetProbeRadius OEPB:: OEZap, 39 GetProteinDesolvationEnergy OEPB:: OEBindResults, 29 GetSaltConcentration OEPB:: OEET, 31 OEPB: : OEZap, 40 GetUnboundLigandArea OEPB:: OESimpleBindResults, 35 GetUnboundLigandAreaEnergy OEPB:: OESimpleBindResults, 35 GetUnboundLigandCoulombEnergy OEPB:: OEBindResults, 29 GetUnboundLigandZapEnergy OEPB:: OESimpleBindResults, 36 GetUnboundProteinArea OEPB:: OESimpleBindResults, 36 GetUnboundProteinAreaEnergy OEPB:: OESimpleBindResults, 36 GetUnboundProteinCoulombEnergy OEPB:: OEBindResults, 29 GetUnboundProteinZapEnergy OEPB:: OESimpleBindResults, 36 GetUseHydrogens OEPB:: OEArea, 25 GetVerbose OEPB:: OEZap, 39 GetZap OEPB:: OEBind, 26 GetZapEnergy OEPB:: OESimpleBindResults, 36

# $\mathbf{I}$

IsFocusTargetSet  $OEPB$ :  $OEZap, 40$ 

# O

OEPB:: OEArea, 23 Constructors, 23 GetArea. 23 GetMethod, 24 GetUseHydrogens, 25 operator=, 23 SetMethod, 25 SetUseHydrogens, 25 OEPB:: OEAreaMethod, 42 OEPB:: OEAreaMethod:: Default, 42 OEPB:: OEAreaMethod:: Discrete, 42 OEPB:: OEAreaMethod:: Gaussian, 42 OEPB:: OEAreaMethod:: Undefined. 42 OEPB:: OEBind. 25 Bind, 26 Constructors, 25 GetZap, 26 operator=, 25 SetProtein, 26 SetZap, 26 SimpleBind, 27 OEPB:: OEBindResults, 27 Constructors, 27 GetAnalyticCoulombicBindingEnergy, 28 GetBoundLigandCoulombEnergy, 28 GetBoundProteinCoulombEnergy, 28 GetComplexCoulombEnergy, 28 GetCoulombEnergy, 28 GetDesolvationEnergy, 28 GetLigandDesolvationEnergy, 29 GetProteinDesolvationEnergy, 29 GetUnboundLigandCoulombEnergy, 29 GetUnboundProteinCoulombEnergy, 29 operator=, 27 Print. 29 OEPB:: OECalculateCoulombicBinding, 43 OEPB:: OECoulombicAtomPotentials, 43 OEPB:: OECoulombicSelfEnergy, 43 OEPB: : OEET, 29

Constructors, 30 GetDielectric. 30 GetGridBuffer, 30 GetGridSpacing, 30 GetInnerDielectric, 30 GetInnerMask, 30 GetJoin. 31 GetOuterMask, 31 GetSaltConcentration, 31  $operatorerator =$ , 30 SetDielectric, 31 SetGridBuffer, 31 SetGridSpacing, 31 SetInnerDielectric, 31 SetInnerMask, 32 SetJoin, 32 SetOuterMask, 32 SetRefMol, 32 SetSaltConcentration, 32 Tanimoto, 32 OEPB:: OEMakeETGrid, 43 OEPB:: OESimpleBindResults, 33 Constructors, 33 GetBindingEnergy, 33 GetBoundLigandArea, 33 GetBoundLigandAreaEnergy, 33 GetBoundLigandZapEnergy, 34 GetBoundProteinArea, 34 GetBoundProteinAreaEnergy, 34 GetBoundProteinZapEnergy, 34 GetBuriedArea, 34 GetBuriedAreaEnergy, 34 GetComplexArea, 35 GetComplexAreaEnergy, 35 GetComplexZapEnergy. 35 GetConf, 35 GetUnboundLigandArea, 35 GetUnboundLigandAreaEnergy, 35 GetUnboundLigandZapEnergy, 36 GetUnboundProteinArea, 36 GetUnboundProteinAreaEnergy, 36 GetUnboundProteinZapEnergy, 36 GetZapEnergy, 36 operator=, 33 Print, 36 OEPB:: OEZap, 37 CalcAtomPotentials, 37 CalcForces, 37 CalcPotentialGrid. 37 CalcSolvationEnergy, 38 ClearFocusTarget, 38 Constructors, 37 GetBoundarySpacing, 38 GetDielectricModel, 38

GetError, 38 GetFocusTarget, 38 GetGridSpacing, 39 GetInnerDielectric, 39 GetIterations, 39 GetMolecule, 39 GetOuterDielectric. 39 GetProbeRadius, 39 GetSaltConcentration, 40 GetVerbose, 39 IsFocusTargetSet, 40  $operatorerator =$ , 37 SetBoundarySpacing, 40 SetDielectricModel, 40 SetError, 40 SetFocusTarget, 40 SetGridSpacing, 40 SetInnerDielectric.41 SetIterations, 41 SetMolecule, 41 SetOuterDielectric, 41 SetProbeRadius, 41 SetSaltConcentration, 41 SetVerbose. 41 OEPB:: OEZapBind, 43 OEPB:: OEZapDielectricModel, 42 OEPB::OEZapDielectricModel::Default, 42 OEPB:: OEZapDielectricModel:: Gaussian, 42 OEPB::OEZapDielectricModel::Molecular,  $42$ OEPB:: OEZapGetArch, 43 OEPB:: OEZapGetLicensee, 44 OEPB:: OEZapGetPlatform, 44 OEPB:: OEZapGetRelease, 44 OEPB:: OEZapGetSite, 44 OEPB:: OEZapGetVersion, 44 operator= OEPB:: OEArea, 23 OEPB:: OEBind, 25 OEPB:: OEBindResults, 27 OEPB:: OEET, 30 OEPB:: OESimpleBindResults, 33 OEPB:: OEZap, 37

# $\mathsf{P}$

```
Print
   OEPB:: OEBindResults, 29
   OEPB:: OESimpleBindResults, 36
```

# S

SetBoundarySpacing  $OEPB$ :  $OEZap, 40$ SetDielectric

OEPB:: OEET, 31 SetDielectricModel  $OEPB$ :  $OEZap, 40$ SetError OEPB:: OEZap, 40 SetFocusTarget OEPB:: OEZap, 40 SetGridBuffer OEPB:: OEET, 31 SetGridSpacing OEPB: : OEET, 31  $OEPB$ : :  $OEZap$ , 40 SetInnerDielectric OEPB:: OEET, 31 OEPB:: OEZap, 41 SetInnerMask OEPB:: OEET, 32 SetIterations OEPB:: OEZap, 41 SetJoin OEPB: : OEET, 32 SetMethod OEPB:: OEArea, 25 SetMolecule OEPB:: OEZap, 41 SetOuterDielectric OEPB:: OEZap, 41 SetOuterMask OEPB:: OEET, 32 SetProbeRadius OEPB:: OEZap, 41 SetProtein OEPB:: OEBind, 26 SetRefMol OEPB:: OEET, 32 SetSaltConcentration OEPB:: OEET, 32 OEPB: : OEZap, 41 SetUseHydrogens OEPB:: OEArea, 25 SetVerbose OEPB:: OEZap, 41 SetZap OEPB:: OEBind, 26 SimpleBind OEPB:: OEBind, 27

# Τ

Tanimoto OEPB:: OEET, 32 transfer.py Example Code, 14

# Z

zap\_atompot.py Example Code, 9 zap\_focussing.py Example Code, 17 zap\_forces.py Example Code, 19 zap\_grid1.py Example Code, 3 zap\_grid2.py Example Code, 4 zap\_grid3.py Example Code, 7 zap\_solv1.py Example Code, 12