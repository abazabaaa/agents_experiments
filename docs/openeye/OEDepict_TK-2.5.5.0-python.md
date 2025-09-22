![](_page_0_Picture_0.jpeg)

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| Section | Title                             | Page |
|---------|-----------------------------------|------|
| 1       | <b>Introduction</b>               | 1    |
| 2       | <b>Theory</b>                     | 3    |
| 2.1     | Basic Drawing Primitives          | 6    |
| 2.2     | Molecule Depiction                | 21   |
| 2.3     | Highlighting                      | 27   |
| 2.4     | Molecule Layouts                  | 34   |
| 2.5     | Multi Page Images                 | 36   |
| 2.6     | MDL Query Depiction               | 43   |
| 2.7     | MDL Reaction Depiction            | 44   |
| 2.8     | Molecule Alignment                | 48   |
| 2.9     | Generating Interactive SVG Images | 53   |
| 3       | <b>Examples</b>                   | 59   |
| 3.1     | OEDepict Examples                 | 59   |
| 3.2     | Python Cookbook Examples          | 103  |
| 4       | <b>API</b>                        | 105  |
| 4.1     | OEDepict Classes                  | 105  |
| 4.2     | OEDepict Constants                | 372  |
| 4.3     | OEDepict Functions                | 504  |
| 5       | <b>Appendices</b>                 | 571  |
| 5.1     | Appendix: Element coloring (CPK)  | 571  |
| 6       | <b>Release History</b>            | 575  |
| 6.1     | OEDepict TK 2.5.5                 | 575  |
| 6.2     | OEDepict TK 2.5.4                 | 575  |
| 6.3     | OEDepict TK 2.5.3                 | 575  |
| 6.4     | OEDepict TK 2.5.2                 | 575  |
| 6.5     | OEDepict TK 2.5.1                 | 575  |
| 6.6     | OEDepict TK 2.5.0                 | 575  |
| 6.7     | OEDepict TK 2.4.7                 | 576  |
| 6.8     | OEDepict TK 2.4.6                 | 576  |
| 6.9     | OEDepict TK 2.4.5                 | 576  |
| 6.10    | OEDepict TK 2.4.4                 | 576  |
| 6.11    | OEDepict TK 2.4.3                 | 577  |
| 6.12    | OEDepict TK 2.4.2                 | 577  |
| 6.13    | OEDepict TK 2.4.1                 | 578  |
| 6.14    | OEDepict TK 2.4.0                 | 579  |
| 6.15    | OEDepict TK 2.3.6                 | 579  |
| Section | Title                             | Page |
| 6.16    | OEDepict TK 2.3.5                 | 58   |
| 6.17    | OEDepict TK 2.3.4                 | 58   |
| 6.18    | OEDepict TK 2.3.3                 | 58   |
| 6.19    | OEDepict TK 2.3.2                 | 58   |
| 6.20    | OEDepict TK 2.3.1                 | 58   |
| 6.21    | OEDepict TK 2.3.0                 | 58   |
| 6.22    | OEDepict TK 2.2.6                 | 59   |
| 6.23    | OEDepict TK 2.2.5                 | 59   |
| 6.24    | OEDepict TK 2.2.4                 | 59   |
| 6.25    | OEDepict TK 2.2.3                 | 59   |
| 6.26    | OEDepict TK 2.2.2                 | 60   |
| 6.27    | OEDepict TK 2.2.1                 | 60   |
| 6.28    | OEDepict TK 2.2.0                 | 60   |
| 6.29    | OEDepict TK 2.1.0                 | 60   |
| 6.30    | OEDepict TK 2.0.4                 | 60   |
| 6.31    | OEDepict TK 2.0.3                 | 60   |
| 6.32    | OEDepict TK 2.0.2                 | 60   |
| 6.33    | OEDepict TK 2.0.1                 | 61   |
| 6.34    | OEDepict TK 2.0.0                 | 61   |
| 7       | Copyright and Trademarks          | 61   |
| 8       | Sample Code                       | 61   |
| 9       | Citation                          | 61   |
| 9.1     | Orion ® Floes                     | 61   |
| 9.2     | Toolkits and Applications         | 62   |
| 9.3     | OpenEye Web Services              | 62   |
| 10      | Technology Licensing              | 62   |
| 10.1    | GCC                               | 63   |
| Index   |                                   | 65   |

# **ONE**

# **INTRODUCTION**

OEDepict TK provides functionalities to render chemical structures and output molecule depictions to a wide range of graphical file formats.

In addition to standard depiction routines, OEDepict TK provides a powerful graphics engine which supports:

- Basic shape drawing
- · Highly customizable molecule depiction
- Variety of highlighting styles
- Customizable layout options
- Depictions aligned by MCS or substructure
- MDL Query and MDL Reaction depictions

## **THEORY**

## **2.1 Basic Drawing Primitives**

The following example introduces how an image can be created in OEDepict TK to generate a single black line across an image:

- 1. Create an *OEImage* object with a specific width and height.
- 2. Specify the two end points of the line with OE2DPoint objects.
- 3. Draw the line with the OEImage. DrawLine method using the OEDepict\_OEBlackPen to specify the graphical properties of the line.
- 4. Write the image into a file by calling the  $OEWriteImage$  function.

The OEImage class is implemented as a container of drawing commands. When a method such as  $OEImage$ .  $DrawLine$  is called, rather than immediately drawing the line specified by the parameters, a line drawing operation is created in the OEImage class for later execution.

#### **Listing 1: Example of line drawing**

```
width, height = 100, 100# Create image
image = oedepict. OEImage (width, height)
# Draw line with default pen
bgn = oedepict.OE2DPoint(10.0, 10.0)end = oedepict. OE2DPoint(90.0, 90.0)image.DrawLine(bgn, end, oedepict.OEBlackPen)
# Write image to SVG file
oedepict.OEWriteImage("DrawLine.svg", image)
```

The image created by  $Listing$  1 is shown in Figure: Example of line drawing.

- OEPen class
- OEImage class
- OEWriteImage function

![](_page_7_Picture_1.jpeg)

Fig. 1: Example of line drawing

## 2.1.1 Coordinate System

The coordinate system used in OEDepict TK has the origin  $(x=0.0, y=0.0)$  at the top left with the x-axis pointing to the right and the y-axis pointing down.

![](_page_7_Figure_5.jpeg)

Fig. 2: 2D coordinate system  $(X = horizontal, Y = vertical)$ 

## See also:

• OE2DPoint class

# 2.1.2 Basic Shapes

![](_page_8_Figure_2.jpeg)

**OEDepict TK** supports drawing the following basic shapes:

## 2.1.3 Image File Formats

OEDepict TK natively supports a variety of graphical file formats. OEWriteImage automatically detects the desired file format from the file name passed to the function. The following table lists the file formats natively supported in **OEDepict TK** and their associated file extensions:

| Graphics File Format            | Format Type  | File Extension |
|---------------------------------|--------------|----------------|
| PNG (Portable Network Graphics) | raster image | .png           |
| SVG (Scalable Vector Graphics)  | vector image | .svg           |
| bare SVG (with no header)       | vector image | .bsvg          |
| Postscript                      | vector image | .ps            |
| Encapsulated PostScript         | vector image | .eps           |
| PDF (Portable Document Format)  | vector image | .pdf           |

The OEIsRegisteredImageFile function can be used to query whether a given file extension is supported by **OEDepict TK**. All the supported file formats can be queried using the OEGetSupportedImageFileExtensionsfunction.

# **2.2 Molecule Depiction**

The previous chapter introduced how to create images and draw basic geometric elements (such as text, lines rectangles, etc.) Drawing these basic graphical elements provides a framework to construct more complex images such as molecular diagrams.

The molecule depiction is divided into two separate steps (see Figure: Process of Molecule Depiction):

- 1. Generating 2D coordinates
- 2. Rendering molecule that involves
  - transforming and scaling coordinates in order to fit the molecule into an image with a specific width and height
  - setting atom and bond display properties based on depiction style
  - creating an image (such as drawing lines for bonds, drawing text for atomic labels)

The next example (Listing 1) demonstrates how easy is to depict a molecule using the **OEDepict TK**. After creating a molecule (for example by parsing a SMILES string) the image can be generated by calling two functions.

- 1. The OEPrepareDepiction function prepares the molecule for depiction. This process may involve perceiving atom and bond stereo information and suppressing or adding hydrogens. It also calls the  $OEDepictCoordinates$  function to generate the 2D coordinates of the molecule.
- 2. The OERenderMolecule function generates the image of the molecule using the default depiction styles and then writes the image into the given file.

The image created by  $Listing$  1 is shown in Figure: Example of depicting a molecule.

![](_page_10_Figure_1.jpeg)

Fig. 3: Process of molecule depiction

## Listing 1: Example of molecule depiction

```
mol = occhem. OEGraphMol()oechem. OESmilesToMol(mol, "c1cc(N)cc(S(=0)(=0)0)c1 3-aminobenzenesulfonic acid")
oedepict.OEPrepareDepiction(mol)
oedepict.OERenderMolecule("DepictMolSimple.png", mol)
```

## 3-aminobenzenesulfonic acid

![](_page_10_Figure_6.jpeg)

Fig. 4: Example of molecule depiction

See also:

· OEPrepareDepiction function

· OERenderMolecule function

## 2.2.1 Customizing Molecule Depiction

The previous example showed how to generate a molecule diagram with default parameters. OEDepict TK provides the ability to customize molecule depiction. The Listing 2 example shows how to depict a molecule width specific width and height parameters.

#### Listing 2: Example of depicting a molecule

```
mol = oechem.OEGraphMol()
oechem.OESmilesToMol(mol, "clcc(N)cc(S(=0)(=0)0)cl 3-aminobenzenesulfonic acid")
oedepict.OEPrepareDepiction(mol)
width, height = 300, 300opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
disp = oedepict. OE2DMolDisplay (mol, opts)
oedepict.OERenderMolecule("DepictMolSize.png", disp)
```

#### See also:

- OE2DMolDisplayOptions class
- OE2DMolDisplay class

Apart from defining the dimensions of a depicted molecule, the OE2DMolDisplayOptions class stores all properties that determine how a molecule is depicted. The following example shows how to set various depiction styles before initializing the OE2DMolDisplay object. The image created by Listing 3 is shown in Figure: Example of customizing depiction style.

#### Listing 3: Example of customizing the depiction style

```
mol = occhem. OEGraphMol()oechem. OESmilesToMol(mol, "clcc(N)cc(S(=0)(=0)0)cl 3-aminobenzenesulfonic acid")
oedepict.OEPrepareDepiction(mol)
width, height = 200, 200opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetAromaticStyle(oedepict.OEAromaticStyle_Circle)
opts.SetAtomColorStyle(oedepict.OEAtomColorStyle_BlackCPK)
opts.SetTitleLocation(oedepict.OETitleLocation_Bottom)
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OERenderMolecule("DepictMolStyle.png", disp)
```

Apart from controlling the depiction style through the OE2DMolDisplayOptions class, OEDepict TK also provides access to manipulate individual atom and bond 2D display properties. The OE2DMolDisplay. GetAtomDisplays method returns an iterator over OE2DAtomDisplay objects that store atom display information. Similarly, the OE2DMolDisplay. GetBondDisplays method returns an iterator over OE2DBondDisplay objects that store bond display information.

The following example demonstrates how to change atom and bond display properties and depict the graph of the molecule by ignoring atom labels and setting bond display styles. The image created by  $Listing\ 4$  is shown in Figure: Example of molecule graph depiction.

![](_page_12_Figure_1.jpeg)

Fig. 5: Example of customizing the depiction style

## Listing 4: Example of molecule graph depiction

```
mol = occhem.OEGraphMol()oechem. OESmilesToMol(mol, "c1cc(N)cc(S(=0) (=0) 0)c1")oedepict.OEPrepareDepiction(mol)
width, height = 200, 200opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetAtomColorStyle(oedepict.OEAtomColorStyle_WhiteMonochrome)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
opts.SetAtomColor(oechem.OEElemNo_C, oechem.OEDarkGreen)
pen = oedepict.OEPen(oechem.OEBlack, oechem.OEBlack, oedepict.OEFill On, 3.0)
opts.SetDefaultBondPen(pen)
disp = oedepict.OE2DMolDisplay(mol, opts)
for adisp in disp. GetAtomDisplays():
   adisp.SetLabel("")
for bdisp in disp.GetBondDisplays():
   bdisp.SetDisplayType(oedepict.OEBondDisplayType_Single)
oedepict.OERenderMolecule("DepictMolGraph.png", disp)
```

Hint: Even though OEDepict TK provides the ability to manipulate atom and bond display properties of after the OE2DMolDisplay object is constructed, it is highly recommended to set the depiction properties using the OE2DMolDisplayOptions class. Only by knowing all properties (such as labels, font styles and sizes etc.) in advance can one ensure the **best depiction layout** *i.e.* that the molecule diagram is rendered without any label clippings and the labels are displayed with the minimum number of overlaps.

#### See also:

• OE2DAtomDisplay class

![](_page_13_Picture_1.jpeg)

Fig. 6: Example of molecule graph depiction

• OE2DBondDisplay class

## 2.2.2 Controlling the Size of Depicted Molecules

The dimensions of a depicted molecule are controlled by the width, height and scale parameters of the  $OE2DMolDisplayOptions$  that is used to initialized the OE2DMolDisplay object. (See example in Listing 2)

#### See also:

- · OE2DMolDisplayOptions. SetDimensions method
- · OE2DMolDisplayOptions. SetHeight method
- · OE2DMolDisplayOptions. SetScale method
- · OE2DMolDisplayOptions. SetWidth method

If the width and the height of the image is not specified (set to be zero), then scaling value determine the dimensions of the image. (See examples in *Examples of image scaling*). The default scale is defined to be OEScale\_Default constant, and the image may be enlarged or shrunk by specifying a floating point scaling value. For example, the scaling OEScale\_Default \* 0.5 generates an image a half of the default size, and scaling OEScale\_Default \* 1.5 generates an image one and a half times the default.

| OEScale::Default * 0.5           | OEScale::Default                    | OEScale::Default * 1.5           |
|----------------------------------|-------------------------------------|----------------------------------|
| Image: benzene ring (scale 0.5×) | Image: benzene ring (default scale) | Image: benzene ring (scale 1.5×) |

Table 1: **Examples of image scaling** (width = 0.0, height = 0.0)

If an OE2DMolDisplayOptions object is initialized with zero width and / or height, then the real dimensions of the image can be accessed after creating an OE2DMolDisplay object.

```
width, height, scale = 0.0, 0.0, 50.0
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
disp = oedefict.OE2DMolDisplay(mol, opts)print ("width %.1f" % disp.GetWidth())
print ("height %.1f" % disp.GetHeight ())
print ("scale %.1f" % disp.GetScale())
```

The output of the preceding snippet is the following:

width 137.0 height 181.0 scale 50.0

#### See also:

OE2DMolDisplay.GetHeight method OE2DMolDisplay.GetWidth method OE2DMolDisplay. GetScale method

If both the width and the height of are specified, then OEScale AutoScale scaling indicates that the molecule is scaled to maximally fit the given dimensions. The specified width and height will not be altered, not even if the given scaling would require it *i.e* if necessary the scaling will be reduced in order to fit the molecule into the given dimension. (See examples in *Examples of image scaling*).

| OEScale::Default * 0.5               | OEScale::Default                        | OEScale::Default * 1.5               |
|--------------------------------------|-----------------------------------------|--------------------------------------|
| Image: benzene molecule (scaled 0.5) | Image: benzene molecule (default scale) | Image: benzene molecule (scaled 1.5) |

Table 2: **Examples of fixed sized image** (width =  $120.0$ , height =  $120.0$ )

Note: Specifying a width and / or height larger than what is required by the scale, causes the molecule to float in the middle of the image of the requested size.

If only either the width or the height of the image is specified, then the unspecified dimension will be set based on the scaling and the specified width / height, respectively.

| OEScale::Default, width = 250.0, height = 0.0 | OEScale::Default, width = 0.0, height = 250.0 |
|-----------------------------------------------|-----------------------------------------------|
|                                               | Image: benzene ring diagram                   |
| Image: benzene ring diagram                   |                                               |

## 2.2.3 Molecule Depiction with Transparent Background

The following code snippet shows how to generate a molecule depiction with transparent background. First, the OEImage object, onto which the depiction is going to be rendered, has to be constructed with the OETransparentColor color. Then the OERenderMolecule function has to be called with a parameter that ensures that the background in not cleared prior to rendering the molecule.

```
width, height, scale = 200.0, 200.0, oedepict.OEScale_AutoScale
image = oedepict.OEImage(width, height, oechem.OETransparentColor)
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
disp = oedepict.OE2DMolDisplay(mol, opts)
clearbackground = Trueoedepict.OERenderMolecule("DepictMolTransparent.pnq", disp, not clearbackground)
```

## 2.2.4 Displaying Atom Properties

**OEDepict TK** provides ability the display atom properties as strings. When a OE2DMolDisplay object is created, the positions where atom properties can be displayed are calculated. (see Figure: Example of generating atom property *positions.*)

![](_page_16_Figure_3.jpeg)

### Fig. 7: Example of generating atom property positions

The following example shows how to display the atom indices by using the OEDisplayAtomIdx functor. The font used to depict the atom property strings also can be modified by using the OE2DMolDisplayOptions. SetAtomPropLabelFont method. The image created by Listing 5 is shown in Figure: Example of displaying atom indices.

## **Listing 5: Example of depicting atom indices**

```
mol = occhem. OEGraphMol()oechem. OESmilesToMol(mol, "c1cc(N)cc(S(=0) (=0) 0)c1")oedepict.OEPrepareDepiction(mol)
width, height = 300, 200
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetAtomPropertyFunctor(oedepict.OEDisplayAtomIdx())
opts.SetAtomPropLabelFont(oedepict.OEFont(oechem.OEDarkGreen))
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OERenderMolecule("AtomPropIndex.png", disp)
```

Hint: It is recommended to use the OE2DMolDisplayOptions. SetAtomPropertyFunctor method to define the atom property labels when the OE2DMolDisplay object is constructed. All labels displayed on the molecule diagram have to be known in advance in order to be able to minimize the number of label clashes and clippings when calculating the positions of the atom property labels.

### See also:

**OEDepict TK** provides the following built-in atom property functors:

- OEDisplayAtomIdx class
- OEDisplayAtomMapIdx class
- OEDisplayNoAtomProp class

![](_page_17_Figure_1.jpeg)

Fig. 8: Example of displaying atom indices

In order to display user-defined atom properties, the functor that is passed to the OE2DMolDisplayOptions. SetAtomPropertyFunctor method has to be derived from the OEDisplayAtomPropBase abstract base class. The Listing 6 example shows how to implement a user-defined functor that marks aromatic atoms. The image created by Listing  $6$  is shown in Figure: Example of displaying user-defined atom properties.

### Listing 6: Example of depicting user-defined atom properties

```
class LabelAromaticAtoms (oedepict. OEDisplayAtomPropBase) :
    def __init_(self):
        oedepict.OEDisplayAtomPropBase.__init_(self)
    def __call__(self, atom):
        if atom. IsAromatic():
           return "(A)"
        return ""
   def CreateCopy(self):
        # _disown_ is required to allow C++ to take
        # ownership of this object and its memory
        copy = LabelAromaticAtoms()return copy.__disown__()
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "clcc(N)cc(S(=0)(=0)0)cl")
oedepict.OEPrepareDepiction(mol)
width, height = 300, 200
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
atomlabel = LabelAromaticAtoms()
opts.SetAtomPropertyFunctor(atomlabel)
```

```
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OERenderMolecule("AtomPropUser.png", disp)
```

![](_page_18_Figure_3.jpeg)

Fig. 9: Example of displaying user-defined atom properties

#### See also:

• OEDisplayAtomPropBase class

## 2.2.5 Displaying Bond Properties

Similarly to atom properties, bond properties can be displayed as strings. (see Figure: Example of generating bond property positions.)

![](_page_18_Figure_9.jpeg)

Fig. 10: Example of generating bond property positions

The Listing 7 demonstrates how to display bond indices by using the OEDisplayBondIdx functor. The font used to depict the bond property strings can be set by using the OE2DMolDisplayOptions. SetBondPropLabelFont method. The image created by Listing 7 is shown in Figure: Example of displaying bond indices.

## Listing 7: Example of depicting bond indices

![](_page_19_Figure_2.jpeg)

![](_page_19_Figure_3.jpeg)

Fig. 11: Example of displaying bond indices

Hint: It is recommended to use the OE2DMolDisplayOptions. SetBondPropertyFunctor method to define the bond property labels when the OE2DMolDisplay object is constructed. All labels displayed on the molecule diagram have to be known in advance in order to be able to minimize the number of label clashes and clippings when calculating the positions of the bond property labels.

### See also:

**OEDepict TK** provides the following built-in bond property functors:

- OEDisplayBondIdx class
- OEDisplayNoBondProp class

In order to display user-defined bond properties, the functor that is passed to the OE2DMolDisplayOptions. SetBondPropertyFunctor method has to be derived from the OEDisplayBondPropBase abstract base class. The Listing 8 example shows how to implement a user-defined functor that marks chain and ring bonds. The image created by  $Listing \; 8$  is shown in Figure: Example of displaying user-defined bond properties.

![](_page_20_Figure_1.jpeg)

#### Listing 8: Example of depicting user-defined bond properties

![](_page_20_Figure_3.jpeg)

Fig. 12: Example of displaying user-defined bond properties

#### See also:

• OEDisplayBondPropBase class

## 2.2.6 Hiding Atoms and Bonds

**OEDepict TK** provides ability the suppress the display of specific atom and bonds. When a OE2DMolDisplay object is created, the visibility of every atom is evaluated. Bonds with both atom endpoints visible are also displayed. (see Figure: Example of hiding a portion of a structure.)

The following example shows how to selectively display only a portion of the structure by using a custom class derived from the OEUnaryAtomPred functor. The images created by Listing  $9$  is shown in Figure: Example of hiding a portion of a structure.

Hint: It is recommended to use the OE2DMolDisplayOptions. SetAtomVisibilityFunctor method to identify the visible atoms when the  $OE2DMolDisplay$  object is constructed. All objects displayed on the molecule diagram have to be known in advance in order to be able to correctly size and scale the molecule.

#### Listing 9: Example of selectively displaying atoms

```
class OEAtomVisibilityShowRxnRole(oechem.OEUnaryAtomPred):
   def _init_(self, role):
       self.rxnrole = role
        oechem.OEUnaryAtomPred.__init__(self)
   def _call_(self, atom):
        # return True if the atom should be visible, otherwise return False
        if self.rxnrole == oechem.OERxnRole_None:
            return True
       return (self.rxnrole == atom.GetRxnRole())def CreateCopy(self):
        # _disown_ is required to allow C++ to take
        # ownership of this object and its memory
       return OEAtomVisibilityShowRxnRole(self.rxnrole)._disown_()
if len(sys.argv) != 3:
    oechem.OEThrow.Usage("%s <rxnfile> <imagefile>" % sys.argv[0])
ifs = oechem.oemolistream(sys.argv[1])
mol = occhem. OEGraphMol()if not oechem. OEReadRxnFile(ifs, mol):
   oechem. OEThrow. Fatal ("%s error reading reaction file" % sys. argv[0])
oedepict.OEPrepareDepiction(mol)
image = odeplot.OEImage(900, 100)rows, \text{cols} = 1, 3
grid = oedepict.OEImageGrid(image, rows, cols)
opts = oedepict.OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(),
                                      oedepict.OEScale_AutoScale)
cell = grid.GetCell(1, 1)mol. SetTitle ("Reaction display")
```

```
opts.SetAtomVisibilityFunctor(oechem.OEIsTrueAtom()) # explicitly set the default
disp = oedepict.OE2DMolDisplay(mol, opts)
rxnscale = disp.Getscale()oedepict.OERenderMolecule(cell, disp)
cell = grid.GetCell(1, 2)mol.SetTitle("Reactant display")
opts.SetAtomVisibilityFunctor(OEAtomVisibilityShowRxnRole(oechem.OERxnRole_Reactant))
opts.SetScale(rxnscale)
disp = oedefict.OE2DMolDisplay(mol, opts)oedepict.OERenderMolecule(cell, disp)
cell = grid.GetCell(1, 3)mol.SetTitle("Product display")
opts.SetAtomVisibilityFunctor(OEAtomVisibilityShowRxnRole(oechem.OERxnRole Product))
opts.SetScale(rxnscale)
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OERenderMolecule(cell, disp)
```

![](_page_22_Figure_3.jpeg)

Fig. 13: Example of hiding a portion of a structure

## 2.2.7 Configuring Molecule Display

**OEDepict TK** provides a mechanism to generate a standard interface that allows configuration of molecule displays. By calling the OEConfigureImageOptions function, "-height" and "width" parameters are added to the interface (OEInterface), at run-time the value of these parameters can be obtained by calling the OEGet ImageHeight and OEGet ImageWidth functions, respectively. (See the standard interface displayed when calling the Listing 10 example with the "-help" parameter)

The OEConfigure2DMolDisplayOptions function generates an interface that allows setting of various molecule display options (such as aromatic style, atom and bond coloring etc.) The OE2DMolDisplayOptions object, that stores properties determine the molecule depiction style, can initialized based on to the command line parameters by calling the OESetup2DMolDisplayOptions function.

### Listing 10: Example of configuring mol display

```
def main(argv=[_name_]):
    # import configuration file
    itf = oechem. 0EInterface()oechem. OEConfigure(itf, InterfaceData)
    # add configuration for image size and display options
    oedepict.OEConfigureImageOptions(itf)
   oedepict.OEConfigure2DMolDisplayOptions(itf)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
```

```
ifname = itf.fctString("in")ofname = itf.GetString("-out")ifs = oechem.oemolistream(ifname)
   mol = occhem.OEGraphMol()oechem.OEReadMolecule(ifs, mol)
   oedepict.OEPrepareDepiction(mol)
   width, height = oedepict.OEGetImageWidth(itf), oedepict.OEGetImageHeight(itf)
   opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
    # set up display options from command line parameters
   oedepict.OESetup2DMolDisplayOptions(opts, itf)
   disp = oedefict.OE2DMolDisplay(mol, opts)oedepict.OERenderMolecule(ofname, disp)
InterfaceData = """"!CATEGORY "input/output options :"
  !PARAMETER -in
   !ALIAS -i
   !TYPE string
   !REQUIRED true
   !BRIEF Input filename
  !END
  !PARAMETER -out
   !ALIAS -0
   !TYPE string
   !REQUIRED true
    !BRIEF Output filename
  !END
! END
\mathbf{u} u \mathbf{u}if _name == " main ":
   sys.exit(main(sys.argv))
```

prompt> python DepictMolConfigure.py --help

will generate the following standard interface:

```
Simple parameter list
   image options
     -height : Height of output image
     -width : Width of output image
   input/output
     -in : Input filename
     -out : Output filename
   molecule display options
     -aromstyle : Aromatic ring display style
```

```
-atomcolor : Atom coloring style
-atomprop : Atom property display
-atomstereostyle : Atom stereo display style
-bondcolor : Bond coloring style
-bondprop : Bond property display
-bondstereostyle : Bond stereo display style
-hydrstyle : Hydrogen display style
-linewidth : Default bond line width
-protgroupdisp : Protective group display style
-scale : Scaling of the depicted molecule
-superdisp : Super atom display style
-titleloc : Location of the molecule title
```

See also:

- OEInterface class in the **OEChem TK** manual
- OEDepict Examples chapter

**OEDepict TK** provides the following high-level functions to build standard interface of depiction applications:

| Function name                      | Builds standard interface for ..     |
|------------------------------------|--------------------------------------|
| OEConfigure2DMolDisplayOptions     | molecule depiction style             |
| OEConfigureHighlightParams         | highlighting                         |
| OEConfigureImageGridParams         | image grid                           |
| OEConfigureImageOptions            | image                                |
| OEConfigureMultiPageParams         | multi-page image                     |
| OEConfigurePrepareDepictionOptions | preparing molecules for 2D depiction |
| OEConfigureReportOptions           | multi-page report                    |

# 2.3 Highlighting

Atoms and bonds of a molecule can be highlighted by using the OEAddHighlighting functions. OEDepict TK provides four built-in highlighting styles:

color This style is associated with the OEHighlight Style\_Color constant. See Figure: Example of highlighting using the 'color' style.

![](_page_24_Figure_11.jpeg)

Fig. 14: Example of highlighting using the 'color' style

stick This style is associated with the OEHighlight Style\_Stick constant. See Figure: Example of highlighting using the 'stick' style.

![](_page_25_Picture_1.jpeg)

## Fig. 15: Example of highlighting using the 'stick' style

ball and stick This style is associated with the OEHighlightStyle\_BallAndStick constant. See Figure: Example of highlighting using the 'ball and stick' style.

![](_page_25_Figure_4.jpeg)

### Fig. 16: Example of highlighting using the 'ball and stick' style

cogwheel This style is associated with the OEHighlight Style\_Cogwheel constant. See Figure: Example of highlighting using the 'cogwheel' style.

![](_page_25_Figure_7.jpeg)

Fig. 17: Example of highlighting using the 'cogwheel' style

lasso This style is associated with the OEHighlight Style\_Lasso constant. See Figure: Example of highlighting using the 'lasso' style.

![](_page_26_Picture_1.jpeg)

### Fig. 18: Example of highlighting using the 'lasso' style

## 2.3.1 Using Highlighting Styles

The following example (Listing 1) shows how to use the built-in highlighting styles. The OEAddHighlighting function takes an OEMatchBase object and highlights each of its target atoms and bonds using the given style. In this case, the two pyridine rings in the target structure are highlighted by red color using the stick style. The image created by  $Listing 1$  is shown in Figure: Example of using 'stick' highlighting style.

## Listing 1: Example of using highlighting style

```
mol = occhem. OEGraphMol()oechem. OESmilesToMol(mol, "clancc2c1cc3c(cncc3)c2")
oedepict.OEPrepareDepiction(mol)
subs = occhem. OESubSearch("cIncccc1")disp = oedefict.OE2DMolDisplay(mol)unique = Truefor match in subs. Match (mol, unique) :
    oedepict.OEAddHighlighting(disp, oechem.OEColor(oechem.OERed),
                               oedepict.OEHighlightStyle Stick, match)
```

oedepict.OERenderMolecule("HighlightSimple.png", disp)

![](_page_26_Picture_8.jpeg)

Fig. 19: Example of using 'stick' highlighting style

- · OEHighlightStyle namespace
- · OEAddHighlighting function
- Depicting Substructure Search Match example

## 2.3.2 Using Highlighting Classes

**OEDepict TK** also provides the highlighting classes that correspond to the highlighting styles. Each highlighting style can be customized by using the corresponding class:

- OEHighlightByColor
- OEHighlightByStick
- OEHighlightByBallAndStick
- OEHighlightByCogwheel
- OEHighlightByLasso

The next example (Listing 2) shows how the **stick** style can be customized by using the corresponding OE-HighlightByStick class. The image created by  $Listing$  2 is shown in Figure: Example of customizing the 'stick' highlighting style.

## **Listing 2: Example of using highlighting class**

```
mol = occhem.OEGraphMol()oechem.OESmilesToMol(mol, "cloncc2c1cc3c(cncc3)c2")
oedepict.OEPrepareDepiction(mol)
subs = occhem. OESubSearch('lncccc1")opts = oedepict.OE2DMolDisplayOptions(240.0, 100.0, oedepict.OEScale_AutoScale)
opts. SetMargins (10.0)
disp = oedefict.OE2DMolDisplay(mol, opts)stickWidthScale = 6.0monochrome = Truehighlight = oedepict.OEHighlightByStick(oechem.OEColor(oechem.OERed),
                                        stickWidthScale, not monochrome)
unique = Truefor match in subs. Match (mol, unique):
    oedepict.OEAddHighlighting(disp, highlight, match)
```

![](_page_27_Picture_11.jpeg)

![](_page_27_Picture_12.jpeg)

Fig. 20: Example of customizing the 'stick' highlighting style

See also:

· OEAddHighlighting function

## 2.3.3 Highlighting Overlapped Patterns

If more than one part of a molecule is highlighted, these highlights can overlap resulting in loss of information. For example, highlighting the matches of the  $clcc[c,n]cc1$  SMARTS pattern will produce the following image.

![](_page_28_Figure_3.jpeg)

Fig. 21: Example of highlighting multiple matches in the same image

There are two ways how this can be avoided and correctly highlight overlapping parts of a molecule. The first example demonstrates how to depict multiple matches in different image cells one by one. The image created by Listing 3 is shown in Figure: Example of highlighting multiple matches one by one.

## Listing 3: Example of highlighting multiple matches one by one

```
mol = occhem. OEGraphMol()oechem. OESmilesToMol(mol, "clancc2c1cc3c(cncc3)c2")
oedepict.OEPrepareDepiction(mol)
subs = occhem.OESubSearch('rرc[c,n]cc1")width, height = 350, 250
image = oedepict. OEImage (width, height)
rows, \cosh = 2, 2
grid = oedepict.OEImageGrid(image, rows, cols)
opts = oedepict.OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(),
                                      oedepict.OEScale_AutoScale)
unique = Truefor match, cell in zip(subs.Match(mol, unique), grid.GetCells()):
   disp = oedepict.OE2DMolDisplay(mol, opts)
   oedepict.OEAddHighlighting(disp, oechem.OEColor(oechem.OEPink),
                               oedepict.OEHighlightStyle_Color, match)
    oedepict.OERenderMolecule(cell, disp)
oedepict.OEWriteImage("HighlightMulti.png", image)
```

### See also:

- OEImageGrid class
- Depicting Molecules in a Grid section

The second example (Listing 4) illustrates how to highlight overlapping matches at once using the OEHighlightOverlayByBallAndStick class. In this example, the OEAddHighlightOverlay function takes all matches being highlighted and colors the overlapped atoms and bonds using the colors by turn. The colors used for high-

![](_page_29_Picture_1.jpeg)

## Fig. 22: Example of highlighting multiple matches one by one

lighting are determined when the OEHighlightOverlayByBallAndStick object is constructed. The image created by Listing 4 is shown in Figure: Example of highlighting overlapping matches at once.

#### Listing 4: Example of highlighting multiple matches simultaneously

```
mol = occhem.OEGraphMol()oechem. OESmilesToMol(mol, "clancc2c1cc3c(cncc3)c2")
oedepict.OEPrepareDepiction(mol)
subs = occhem. OESubSearch("clec[c,n]cc1")opts = oedepict.OE2DMolDisplayOptions(240.0, 100.0, oedepict.OEScale_AutoScale)
opts.SetMargins(10.0)
disp = oedepict. OE2DMolDisplay (mol, opts)
highlight = oedepict.OEHighlightOverlayByBallAndStick(oechem.OEGetContrastColors())
unique = Trueoedepict.OEAddHighlightOverlay(disp, highlight, subs.Match(mol, unique))
oedepict.OERenderMolecule("HighlightOverlay.png", disp)
```

- OEHighlightOverlayBase base class
- OEHighlightOverlayByBallAndStick class
- · OEHighlightOverlayStyle namespace
- · OEGetColors, OEGetContrastColors, OEGetDeepColors, OEGetLightColors and OEGetVividColors functions

![](_page_30_Picture_1.jpeg)

Fig. 23: Example of highlighting overlapping matches at once

# **2.4 Molecule Layouts**

The previous chapters described how to depict a single molecule in an image. This chapter provides examples for drawing multiple molecular diagrams into the same image.

## 2.4.1 Depicting Molecules in an Arbitrary Position

The OEImageFrame class provides a general framework to display a molecule in a specific region of the image by defining the following parameters:

- the reference of the *parent* image
- the width and height of the generated frame
- the offset of the frame relative to the top-left corner of its parent (OE2DPoint)

The Listing 1 examples generates an image where the same molecule is depicted in different regions of the image. The molecular diagrams are automatically resized in order to fit into the specific frame, since the corresponding OE2DMolDisplay object is constructed with the width and height of the OEImageFrame object. When the OERenderMolecule function is called, the offset of the OEImageFrame object is added to the coordinates stored in OE2DMolDisplay in order to transfer the molecule into the specific region of the image. The image created by Listing 1 is shown in Figure: Example of using OEImageFrame.

### **Listing 1: Example of using OEImageFrame**

```
def DrawMolecule(image, mol, width, height, offset):
    frame = oedepict. OEImageFrame (image, width, height, offset)
   oedepict.OEDrawBorder(frame, oedepict.OELightGreyPen)
    opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
   disp = oedefict.OE2DMolDisplay(mol, opts)clearbackground = Trueoedepict.OERenderMolecule(frame, disp, not clearbackground)
image = odeplot.OEImage(400, 400)mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "C1CC(O)CNC1")
```

```
oedepict.OEPrepareDepiction(mol)
DrawMolecule(image, mol, 60, 60, oedepict.OE2DPoint(50.0, 40.0))
DrawMolecule(image, mol, 180, 180, oedepict.OE2DPoint(180.0, 120.0))
DrawMolecule(image, mol, 80, 80, oedepict.OE2DPoint(300.0, 20.0))
DrawMolecule(image, mol, 50, 50, oedepict.OE2DPoint(150.0, 320.0))
DrawMolecule(image, mol, 20, 20, oedepict.OE2DPoint(360.0, 360.0))
oedepict.OEWriteImage("ImageFrame.png", image)
```

![](_page_31_Figure_3.jpeg)

![](_page_31_Figure_4.jpeg)

![](_page_31_Figure_5.jpeg)

Fig. 24: Example of using OEImageFrame

## See also:

- OEImageFrame class
- OEDrawBorder function
- · OERenderMolecule function
- · OEWriteImage function

m

## 2.4.2 Depicting Molecules in a Grid

The OEImageGrid class allows molecules to be aligned into rows and columns. After generating an OEImageGrid object by specifying its number of rows and columns, the cells of the grid can be accessed (from left to right, top to bottom order) by calling the OEImageGrid. GetCells method. The image created by Listing 2 is shown in Figure: Example of using OEImageGrid.

## **Listing 2: Example of using OEImageGrid**

```
smiles = [TCLCC(C) CC1", TCLCC(O) CC1", TCLCC(C1) CC1"]image = odeplot.OEImage (200, 200)rows, \cosh = 2, 2
grid = oedepict.OEImageGrid(image, rows, cols)
opts = oedepict.OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(),
                                      oedepict.OEScale AutoScale)
for smi, cell in zip(smiles, grid. GetCells()):
   mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smi)
   oedepict.OEPrepareDepiction(mol)
   disp = oedepict.OE2DMolDisplay(mol, opts)
   oedepict.OERenderMolecule(cell, disp)
oedepict.OEWriteImage("ImageGridSimple.png", image)
```

![](_page_32_Figure_5.jpeg)

Fig. 25: Example of using OEImageGrid

### See also:

• OEImageGrid class

When an OE2DMolDisplay object is initialized, the dimensions of the depicted molecule is controlled by the width, height and scale parameters of the OE2DMolDisplayOptions object.

When only one molecule is depicted then auto scaling of this molecule is preferred (i.e. scaling the molecule in order to maximally fit it to the given dimensions). However, when more that one molecule, that are quite different in sizes, are depicted next to each other, auto scaling of each molecule can be visually misleading because it emphasizes molecules with greater scaling factors. See example in Figure: Example of using OEImageGrid that is generated by Listing 3.

## Listing 3: Example of auto scaling of molecules

```
smiles = ["clccccc1", "clcccc2clccnc2", "clccc2c(c1)cc3ccccc3n2"]
image = odeplot.OEImage(400, 200)rows, \text{cols} = 1, 3
grid = oedepict.OEImageGrid(image, rows, cols)
opts = oedepict.OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(),
                                       oedepict.OEScale_AutoScale)
for smi, cell in zip(smiles, grid. GetCells()):
   mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smi)
    oedepict.OEPrepareDepiction(mol)
    disp = oedepict.OE2DMolDisplay(mol, opts)
    oedepict.OERenderMolecule(cell, disp)
oedepict.OEWriteImage("ImageGridAutoScale.png", image)
```

![](_page_33_Figure_4.jpeg)

Fig. 26: Example of auto scaling of molecules

### See also:

### Controlling the Size of Depicted Molecules section

The following example (Listing 4) shows how to ensure that all molecules are depicted using the same scaling factor. After initializing the molecules, the minimum scaling factor is determined by looping over the molecules being depicted and calling the OEGetMoleculeScale function. This function returns the scaling factor of the molecule considering the depiction options stored in the given OE2DMolDisplayOptions object. After determining the minimum scaling factor, the molecules are rendered to the cells of the grid by using this fixed scaling factor. The image created by  $Listing$  4 is shown in Figure: Example of using OEImageGrid.

### Listing 4: Example of identical scaling of molecules

```
smiles = ["clccccc1", "clcccc2clccnc2", "clccc2c(c1)cc3ccccc3n2"]
molecules = []for smi in smiles:
   mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smi)
   oedepict.OEPrepareDepiction(mol)
   molecules.append(oechem.OEGraphMol(mol))
image = odeplot.OEImage(400, 200)rows, \cosh = 1, 3
grid = oedepict.OEImageGrid(image, rows, cols)
opts = oedepict.OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(),
                                      oedepict.OEScale_AutoScale)
minscale = float("inf")for mol in molecules:
   minscale = min(minscale, oedepict.OEGetMoleculeScale(mol, opts))
opts.SetScale(minscale)
for idx, cell in enumerate (grid. GetCells()):
   disp = oedepict.OE2DMolDisplay(molecules[idx], opts)
   oedepict.OERenderMolecule(cell, disp)
oedepict.OEWriteImage("ImageGridFixedScale.png", image)
```

![](_page_34_Figure_4.jpeg)

Fig. 27: Example of identical scaling of molecules

- · OEImageGrid. GetCellHeight method
- · OEImageGrid.GetCellWidth method

## 2.4.3 Depicting Molecules in a Table

The following example demonstrates how to depict molecules and display data alongside them by using the OEImageTable. The individual cells of an OEImageTable object can be accessed by calling the any of the following methods:

- · OEImageTable.GetCell
- · OEImageTable.GetBodyCell
- · OEImageTable.GetHeaderCell
- · OEImageTable.GetStubColumnCell

These methods return an image (OEImageBase) on which molecule can be drawn or text can be displayed using the OEImageTable. DrawText method. The image created by Listing 5 is shown in Figure: Example of depicting molecules and data using image table.

#### Listing 5: Example of depicting molecules and data using image table

```
from openeye import oechem
from openeye import oedepict
smiles = ["clcccccl benzene", "clcccncl pyridine", "clcncncl pyrimidine"]
imagewidth, imageheight = 350, 250image = oedepict.OEImage(imagewidth, imageheight)
mainrows, maincols = 3, 2
maintableopts = oedepict.OEImageTableOptions(mainrows, maincols, oedepict.
\rightarrowOEImageTableStyle_NoStyle)
maintableopts. SetHeader (False)
maintableopts.SetColumnWidths([10, 20])
maintable = oedepict.OEImageTable(image, maintableopts)
datarows, datacols = 4, 2
datatableopts = odeplot.OEImageTableOptions (datarows, datacols,
                                              oedepict.OEImageTableStyle LightGreen)
datatableopts. SetStubColumn (True)
datatableopts. SetMargins (5.0)
datatableopts. SetColumnWidths ([10, 20])
for r in range (min (len (smiles), maintable. NumRows())):
    # depict molecule in first column
   cell = maintable.GetBodyCell(r + 1, 1)
   opts = oedepict.OE2DMolDisplayOptions(cell.GetWidth(), cell.GetHeight(),
                                           oedepict.OEScale_AutoScale)
   opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
   mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smiles[r])
    oedepict.OEPrepareDepiction(mol)
```

```
disp = oedepict.OE2DMolDisplay(mol, opts)
   oedepict.OERenderMolecule(cell, disp)
   # depicting data in table
   cell = maintable.GetBodyCell(r + 1, 2)
   table = oedepict.OEImageTable(cell, datatableopts)
   table.DrawText(table.GetHeaderCell(1, False), "Property")
   table. DrawText (table. GetHeaderCell(1), "Value")
   table. DrawText (table. GetStubColumnCell(1), "Name")
   table.DrawText(table.GetBodyCell(1, 1), mol.GetTitle())
   table. DrawText (table. GetStubColumnCell(2), "SMILES")
   table.DrawText(table.GetBodyCell(2, 1), oechem.OEMolToSmiles(mol))
   table.DrawText(table.GetStubColumnCell(3), "MV")
   table.DrawText(table.GetBodyCell(3, 1), "%.3f" % oechem.
→OECalculateMolecularWeight(mol))
```

oedepict.OEWriteImage("ImageTable.png", image)

| Property | Value      |
|----------|------------|
| Name     | benzene    |
| SMILES   | c1ccccc1   |
| MV       | 78.112     |
| Property | Value      |
| Name     | pyridine   |
| SMILES   | c1ccncc1   |
| MV       | 79.100     |
| Property | Value      |
| Name     | pyrimidine |
| SMILES   | c1cncnc1   |
| MV       | 80.088     |

Fig. 28: Example of depicting molecules and data using image table

# 2.5 Multi Page Images

Multi-page images can be generated by the usage of the OEMultiPageImageFile class. After generating a multi-page object by specifying the orientation and the size of its pages, the individual pages can be accessed by calling the  $OEMultiPageImageFile$ . NewPage method. The returned OEImage then can be used to depict molecule(s) as demonstrated in the previous chapters. The image created by Listing 1 is shown in Figure: Example multi-page depiction.

## Listing 1: Example of multi-page depiction

```
smiles = [TCICC(C) CCCl", TCICC(O) CCCl", TCICC(Cl) CCCl","C1CC(F)CCC1", "C1CC(Br)CCC1", "C1CC(N)CCC1"]
multi = oedepict.OEMultiPageImageFile(oedepict.OEPageOrientation_Landscape,
                                       oedepict.OEPageSize_US_Letter)
image = multi.NewPage()opts = oedepict.OE2DMolDisplayOptions()
rows, \cosh = 2, 2
grid = oedepict.OEImageGrid(image, rows, cols)
qrid.SetCellGap(20)
grid.SetMargins(20)
citer = grid.GetCells()for smi in smiles:
    if not citer. IsValid():
        # go to next page
        image = multi.NewPage()grid = oedepict.OEImageGrid(image, rows, cols)
        grid.SetCellGap(20)
        grid. SetMargins (20)
        citer = grid.GetCells()cell = citer.Target()mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smi)
    oedepict.OEPrepareDepiction(mol)
    opts. SetDimensions(cell. GetWidth(), cell. GetHeight(), oedepict. OEScale_AutoScale)
    disp = oedefict.OE2DMolDisplay(mol, opts)oedepict.OERenderMolecule(cell, disp)
    oedepict.OEDrawBorder(cell, oedepict.OEPen(oedepict.OERedPen))
    citer.Next()
oedepict.OEWriteMultiPageImage("MultiPage.pdf", multi)
```

![](_page_38_Figure_1.jpeg)

![](_page_38_Figure_2.jpeg)

The Listing 1 example creates a PDF multi-page image file, the multi-page image types supported by OEDepict TK can be accessed by calling the OEGetSupportedMultiPageImageFileExtensions function. It returns an iterator over the file extensions that can be used when writing a multi-page image file by the OEWriteMultiPageImagefunction.

## 2.5.1 Multi Page Reports

The Listing 1 example illustrates how depict a set of molecules in a multi-page PDF using the OEImageGrid and OEMultiPageImageFile classes. OEDepict TK also provides the OEReport class to do this task in a more convenient way. The OEReport class is a multi-page layout manager that handles the page generation and the positioning of information (such as text and molecule depiction).

In the Listing 2 example, first a OEReportOptions object is created that stores all properties that determine the layout of a documentation. After generating the OEReport object a molecule can be positioned on a cell that is returned by the OEReport. NewCell method. The OEReport. NewCell method creates cells from left to right and top to bottom order on each page. If no more cells are left on the page, then a new page is created before returning the first cell of this new page.

After the document is generated, *i.e* all molecule are depicted, the *OEWriteReport* function writes the multi-page documentation into into a file with the given name. The image created by the Listing 2 example is the same as depicted in Figure: Example multi-page depiction.

#### Listing 2: Example of multi-page depiction using OEReport

```
smiles = ['C1CC(C)CCC1", 'C1CC(O)CCC1", 'C1CC(Cl)CCC1","C1CC(F)CCC1", "C1CC(Br)CCC1", "C1CC(N)CCC1"]
rows, \cosh = 2, 2
reportopts = oedepict.OEReportOptions(rows, cols)
reportopts.SetPageOrientation(oedepict.OEPageOrientation_Landscape)
reportopts.SetCellGap(20)
reportopts. SetPageMargins (20)
report = oedepict.OEReport (reportopts)
```

```
opts = oedepict.OE2DMolDisplayOptions(report.GetCellWidth(),
                                       report.GetCellHeight(), oedepict.OEScale_
\rightarrowAutoScale)
for smi in smiles:
   mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smi)
   oedepict.OEPrepareDepiction(mol)
   cell = report.MewCell()disp = oedepict.OE2DMolDisplay(mol, opts)
   oedepict.OERenderMolecule(cell, disp)
   oedepict.OEDrawBorder(cell, oedepict.OERedPen)
oedepict.OEWriteReport("MultiPageReport.pdf", report)
```

See also:

- OEReportOptions class
- OEReport class

# **2.6 MDL Query Depiction**

In order to depict an MDL query the query molecule has to be imported by calling the OEReadMDLQueryFile function. The rest of the process is identical to depicting a molecule. First the OEP repareDepiction function has to be called to generate the 2D atom coordinates, then the image can be created by rendering the molecule (OERenderMolecule).

### Listing 1: Example of MDL query depiction

```
if len(sys.argv) != 3:
    oechem.OEThrow.Usage("%s <mdlquery> <imagefile>" % sys.argv[0])
ifs = oechem.oemolistream(sys.argv[1])
qmol = oechem. OEGraphMol()
oechem.OEReadMDLQueryFile(ifs, qmol)
oedepict.OEPrepareDepiction(qmol)
oedepict.OERenderMolecule(sys.argv[2], qmol)
```

- OEReadMDLQueryFile function in the OEChem TK manual
- Table: Summary of supported MDL query features

## 2.6.1 Atom Query Features

The depiction of the following MDL atom query features is supported:

- 1. The 8th column in the atom block in the V2K format file (or HCOUNT= in the V3K format file) is used to define the number of allowed hydrogens for an atom. (See examples in Table: Example of depicting hydrogen count)
  - (H0) means no hydrogen atoms allowed unless explicitly drawn.
  - $\bullet$  (Hn) means atom must have n or more implicit hydrogen(s)

![](_page_40_Figure_6.jpeg)

#### Table 4: Examples of depicting hydrogen count

- 2. Query atom types:
  - $A = any atom type except hydrogen$
  - $Q =$  any atom type except hydrogen and carbon
  - $\bullet$  L = atom list

The M ALS line in the property block in the V2K format file (or  $[aaa, bbb, \ldots]$  in the V3K format) is used to list alternative atom types for an atom. (See examples in Table: Examples of depicting query atom types)

![](_page_41_Figure_1.jpeg)

![](_page_41_Figure_2.jpeg)

3. M CHG line in the property block in the V2K format file (or CHG= in the V3K format) is used to define atom formal charges. (See examples in *Table: Example of depicting formal charge*)

| Table 6: Examples of depicting formal charge |  |  |
|----------------------------------------------|--|--|
|                                              |  |  |

![](_page_41_Figure_5.jpeg)

- 4. M RBC line in the property block in the V2K format file (or RBCNT= in the V3K format) is used to limit the number of allowed ring bonds attached to an atom. (See examples in Table: Example of depicting ring count)
  - (r0) means no ring bond allowed
  - $(r*)$  means as drawn
  - (rn) means n number of ring bonds allowed

![](_page_42_Figure_5.jpeg)

#### Table 7: Examples of depicting ring count

- 5. M SUB line in the property block in the V2K format file (or SUBST= in the V3K format) is used to set the number of allowed substitutions of an atom. (See examples in Table: Examples of depicting substitution count)
  - (s0) means no substitution allowed
  - $(s \star)$  means as drawn
  - (sn) means n number of substitution(s) allowed

![](_page_43_Figure_1.jpeg)

Table 8: Examples of depicting substitution count

6. M UNS line in the property block in the V2K format file (or UNSAT= in the V3K format) is used to specify whether or not an atom is unsaturated, *i.e.*, having at least one multiple bond. (See examples in *Table: Examples* of depicting unsaturated property)

![](_page_43_Figure_4.jpeg)

Table 9: Examples of depicting unsaturated property

## **2.6.2 Bond Query Features**

The depiction of the following MDL bond query features is supported:

1. Alternative bond types in the bond block (4 = aromatic, 5 = single or double, 6 = single or aromatic, 7 = double or aromatic,  $8 =$  any bond). (See examples in *Table: Examples of depicting query bond types*)

![](_page_44_Figure_1.jpeg)

Table 10: Examples of depicting query bond types

- OEBondDisplayType namespace
- 2. The 6th column in the atom block in the V2K format file (or TOPO= in the V3K format) describes bond topology. (See examples in Table: Examples of depicting bond topology)
  - (rn) means that it can only mapped to ring bond
  - (ch) means that it can only mapped to chain bond

![](_page_45_Figure_1.jpeg)

Table 11: Examples of depicting bond topology

3. Double bond stereochemistry is considered if both ends of the bond are marked with stereo care flags in the atom block in the V2K format file ( or STBOX= in the V3K format). (See examples in Table: Examples of depicting bond stereo care)

![](_page_45_Figure_4.jpeg)

Table 12: Examples of depicting bond stereo care

### See also:

• Depicting MDL Query example

## 2.6.3 R-group Depiction

**OEDepict TK** can also depict R-group information by interpreting the  $M$  RGP line in the property block of an MDL file (See examples in Table: Examples of depicting R-groups)

![](_page_46_Figure_3.jpeg)

|  |  | Table 13: Examples of depicting R-groups |  |  |  |
|--|--|------------------------------------------|--|--|--|
|--|--|------------------------------------------|--|--|--|

# **2.7 MDL Reaction Depiction**

**OEDepict TK** also supports MDL reaction depiction. The reaction being depicted has to be imported by calling the OEReadMDLReactionQueryFile function. The rest of the process is identical to depicting a molecule. First the OEPrepareDepiction function has to be called to generate the 2D atom coordinates, then the image can be created by rendering the imported reaction (OERenderMolecule) (See examples in Figure: Example of MDL reaction depiction)

## Listing 1: Example of reaction depiction

```
if len(sys.argv) != 3:
    oechem.OEThrow.Usage("%s <mdlreaction> <imagefile>" % sys.argv[0])
ifs = oechem.oemolistream(sys.argv[1])qmol = oechem.OEGraphMol()
oechem.OEReadMDLReactionQueryFile(ifs, qmol)
oedepict.OEPrepareDepiction(qmol)
oedepict.OERenderMolecule(sys.argv[2], qmol)
```

![](_page_46_Figure_9.jpeg)

Fig. 29: Example of MDL reaction depiction

## See also:

· OEReadMDLReactionQueryFile function in the OEChem TK manual

• Depicting MDL Reaction example

The atom map information read from the reaction file can be depicted as atom properties by using the OEDisplay-AtomMapIdx class. (See examples in Figure: Example of MDL reaction depiction with atom mapping)

Listing 2: Example of reaction depiction with map indices

```
if len(sys.argv) != 3:
   oechem.OEThrow.Usage("%s <mdlreaction> <imagefile>" % sys.argv[0])
ifile = sys.argv[1]ofile = sys. array[2]ifs = oechem.oemolistream(ifile)
qmol = oechem.OEGraphMol()
oechem.OEReadMDLReactionQueryFile(ifs, qmol)
oedepict.OEPrepareDepiction(qmol)
opts = oedepict.OE2DMolDisplayOptions()
opts.SetAtomPropertyFunctor(oedepict.OEDisplayAtomMapIdx())
disp = oedepict.OE2DMolDisplay(qmol, opts)
oedepict.OERenderMolecule(ofile, disp)
```

![](_page_47_Figure_5.jpeg)

Fig. 30: Example of MDL reaction depiction with atom mapping

See also:

- · OE2DMolDisplayOptions. SetAtomPropertyFunctor method
- Listing 5 example in the Molecule Depiction chapter

# 2.8 Molecule Alignment

The following three code examples demonstrate how to align molecules either based on:

- maximum common substructure (Listing 1),
- substructure matches (Listing 2), or
- molecular similarity (Listing 3).

## 2.8.1 Molecule Alignment Based on MCS

The Figure: Example of depiction without alignment is generated by highlighting the maximum common substructure of two molecules (MCS), but keeping the original orientation of the compounds.

![](_page_48_Figure_3.jpeg)

#### Fig. 31: Example of depiction without alignment

The Listing 1 code example shows how to align these two molecules by their maximum common substructures *(i.e. by the highlighted atoms and bonds in Figure: Example of depiction without alignment).* 

- First, two molecules are initialized from SMILES string and prepared for depiction.
- A OEMCSSearch object is initialized with the *reference* 2D molecule onto which the *fit* molecule will be aligned.
- An *OEImageGrid* object is constructed that allows to render the two molecules in a grid next to each other.
- The fit molecule is then aligned to the reference by calling the  $OEPreparalleledDepiction$  function that performs MCS search and then aligns the *fit* molecule to the *reference* based on the detected common substructure(s).
- An OE2DMolDisplayOptions object is initialized that stores the properties determine how the molecules are rendered. In order to render the molecules in equal size the smallest depiction scaling factor is calculated.
- If the molecule alignment was successful *(i.e*  $OEA1$ *ignmentResult.IsValid* is *true)*, then the correspondence between the two molecules stored in the OEAlignmentResult returned by the OEPrepareAlignedDepiction function. This OEAlignmentResult object can be used to highlight the matched common substructure by invoking the OEAddHighlighting function.
- After both molecules are rendered into the separate cells of the grid layout, the image is written into a pnq file.

After initializing the two molecules and the OEMCSSearch object, the OEMCSSearch. Match method is called to perform the search and return an iterator over the identified maximum common substructures. The first match is then utilized to call the OEPrepareAlignedDepiction function that aligns one molecule to the other based on the given match. After the alignment, the common atoms and bonds are highlighted by invoking the OEAddHighlighting function. The image created by Listing 1 is shown in Figure: Example of depiction with alignment based on MCS.

Listing 1: Example of molecule alignment based on MCS

```
refmol = occhem.OEGraphMol()oechem.OESmilesToMol(refmol, "clcc(c2cc(cnc2c1)CCCO)C(=0)CCO")
oedepict.OEPrepareDepiction(refmol)
fitmol = occhem. OEGraphMol()oechem. OESmilesToMol(fitmol, "clcc2ccc(cc2c(c1)C(=0)0)CCO")
oedepict.OEPrepareDepiction(fitmol)
mcss = oechem.OEMCSSearch(oechem.OEMCSType_Approximate)
atomexpr = oechem. OEExprOpts_DefaultAtoms
bondexpr = oechem.OEExprOpts_DefaultBonds
mcss. Init (refmol, atomexpr, bondexpr)
mcss.SetMCSFunc(oechem.OEMCSMaxBondsCompleteCycles())
alignres = oedepict. OEPrepareAlignedDepiction (fitmol, mcss)
image = odeplot.OEImage(400, 200)rows, \text{cols} = 1, 2
grid = oedepict.OEImageGrid(image, rows, cols)
opts = oedepict.OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(),
                                       oedepict.OEScale_AutoScale)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
refscale = oedepict.OEGetMoleculeScale(refmol, opts)
fitscale = oedepict.OEGetMoleculeScale(fitmol, opts)
opts.SetScale(min(refscale, fitscale))
refdisp = oedefict.OE2DMolDisplay(mcss.GetPattern(), opts)fitdisp = oedepict.OE2DMolDisplay(fitmol, opts)
if alignres. IsValid():
    refabset = oechem. OEAtomBondSet (alignres. GetPatternAtoms (), alignres.
\rightarrowGetPatternBonds())
    oedepict.OEAddHighlighting(refdisp, oechem.OEBlueTint,
                                oedepict.OEHighlightStyle_BallAndStick, refabset)
    fitabset = oechem. OEAtomBondSet(alignres. GetTargetAtoms(), alignres.
\rightarrowGetTargetBonds())
    oedepict.OEAddHighlighting(fitdisp, oechem.OEBlueTint,
                                oedepict.OEHighlightStyle_BallAndStick, fitabset)
refcell = grid.GetCell(1, 1)oedepict.OERenderMolecule(refcell, refdisp)
fitted1 = grid.GetCell(1, 2)oedepict.OERenderMolecule(fitcell, fitdisp)
oedepict.OEWriteImage("MCSAlign.png", image)
```

- OEMCSSearch class in the **OEChem TK** manual
- OEImageGrid class

![](_page_50_Figure_1.jpeg)

#### Fig. 32: Example of depiction with alignment based on maximum common substructure

- · OEAddHighlighting function
- · OERenderMolecule function
- · OEWriteImage function
- Aligning Molecule Based on MCS example

## 2.8.2 Molecule Alignment Based on Substructure Search

The Figure: Example of depiction without alignment is generated by highlighting the " $O=C(O)C(N)$ " substructures in four amino acids, but keeping the original orientation of the compounds.

The Listing 2 code example shows how to align these molecules by their matched substructures *(i.e.* by the highlighted atoms and bonds in Figure: Example of depiction without alignment).

- First, the OESubSearch object is initialized with the reference 2D molecule onto which all amino acid structures will be aligned.
- Each amino acids structure is initialized from a SMILES string and prepared for depiction.
- An *OEImageGrid* object is constructed that allows to render the molecules into a grid layout.
- An OE2DMolDisplayOptions object is initialized that stores the properties determine how the molecules are rendered. In order to render the molecules in equal size the smallest depiction scaling factor is calculated.
- Looping over the amino acids:
  - Each molecule is aligned to the reference molecule by calling the  $OEPreparedDepiction$ function that performs the alignment based on the detected substructure search match(es).
  - If the molecule alignment was successful (i.e  $OEALigmmentResult. IsValid$  is true), then the correspondence between the two molecules stored in the OEAlignmentResult returned by the OEPrepareAlignedDepiction function. This OEAlignmentResult object can be used to highlight the matched substructure by invoking the OEAddHighlighting function.
  - The aligned (and highlighted) molecule is then rendered to a next cell of the  $OEImageGrid$  object.
- Finally, the image is written into a png file.

![](_page_51_Figure_1.jpeg)

Fig. 33: Example of depiction without alignment

The image created by Listing 2 is shown in Figure: Example of depiction with alignment based on substructure search.

### Listing 2: Example of molecule alignment based on substructure search

```
refmol = occhem. OEGraphMol()oechem.OESmilesToMol(refmol, "O=C(O)C(N)")
oedepict.OEPrepareDepiction(refmol)
ss = oechem. OESubSearch (refmol, oechem. OEExprOpts_DefaultAtoms, oechem. OEExprOpts_
\rightarrowDefaultBonds)
aminosmiles = ["0=C(0) [C@H] (N) Cclc[nH] cn1 Histidine","CC(C)[C@@H](C(=O)O)N Valine",
                "C[C@H] ([C@@H] (C(=O)O)N)O Threonine",
                "C1C[C@H] (NC1)C(=0)O Proline"]
```

```
(continued from previous page)
```

```
amino acids = []for smi in aminosmiles:
   mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smi)
    oedepict.OEPrepareDepiction(mol)
    aminoacids.append(oechem.OEGraphMol(mol))
image = odeplot.OEImage(400, 400)rows, \cosh = 2, 2
grid = oedepict.OEImageGrid(image, rows, cols)
opts = odeplot.OE2DMolDisplayOptions (grid.GetCellWidth(),grid.GetCellHeight(), oedepict.OEScale
\leftrightarrowAutoScale)
opts.SetAtomStereoStyle(oedepict.OEAtomStereoStyle_Display_All)
minscale = float("inf")for amino in aminoacids:
    minscale = min(minscale, oedepict.OEGetMoleculeScale(amino, opts))
opts.SetScale(minscale)
for amino, cell in zip(aminoacids, grid.GetCells()):
   alignres = oedepict.OEPrepareAlignedDepiction(amino, ss)
    disp = oedepict.OE2DMolDisplay(amino, opts)
    if alignres. IsValid():
        oedepict.OEAddHighlighting(disp, oechem.OELightGreen,
                                    oedepict.OEHighlightStyle_Stick, alignres)
    oedepict.OERenderMolecule(cell, disp)
oedepict.OEWriteImage("SubSearchAlign.png", image)
```

#### See also:

- OESubSearch class in the OEChem TK manual
- OEImageGrid class
- · OEAddHighlighting function
- OERenderMolecule function
- OEWriteImage function
- Aligning Molecules Based on Substructure Search example

## 2.8.3 Molecule Alignment Based on Molecular Similarity

The Figure: Example of depiction without alignment is generated by keeping the original orientation of the compounds.

The Listing 3 code example shows how to align these molecules based on their molecular similarity.

- First, two molecules are initialized from SMILES string and prepared for depiction.
- An OEImageGrid object is constructed that allows to render the two molecules in a grid next to each other.
- The fit molecule is then aligned to the reference. The OEGetFPOverlap function is utilized to return all common fragments found between two molecules based on a given fingerprint type. These

![](_page_53_Figure_1.jpeg)

Fig. 34: Example of depiction with alignment based on substructure match

common fragments reveal the similar parts of the two molecules being compared that are used by the OEPrepareMultiAlignedDepiction function to find the best alignment between the molecules. See more fingerprint types in the Fingerprint Types chapter of the GraphSim TK manual.

- An OE2DMolDisplayOptions object is initialized that stores the properties determine how the molecules are rendered. In order to render the molecules in equal size the smallest depiction scaling factor is calculated.
- Then both molecules are rendered into the separate cells of the grid layout, the image is written into a png file.

The image created by Listing 3 is shown in Figure: Example of depiction with alignment based on molecular similarity.

**Note:** GraphSim TK license in not required to run the Listing 3 example.

![](_page_54_Figure_1.jpeg)

Fig. 35: Example of depiction without alignment

```
Listing 3: Example of molecule alignment based on molecular similarity
```

```
refmol = occhem. OEGraphMol()oechem.OESmilesToMol(refmol, "C[C@H](C(=0)N1CCC[C@H]1C(=0)0)OC(=0)[C@@H](Cc2ccccc2)S")
oedepict.OEPrepareDepiction(refmol)
fitmol = oechem.OEGraphMol()
oechem.OESmilesToMol(fitmol, "C[C@H](C(=O)N1CCC[C@H]1C(=O)O)NC(=O)[C@@H](Cc2ccccn2)S")
oedepict.OEPrepareDepiction(fitmol)
image = odeplot.OEImage(500, 300)rows, \text{cols} = 1, 2
grid = oedepict.OEImageGrid(image, rows, cols)
overlaps = oegraphsim. OEGetFPOverlap (refmol, fitmol,
                                     oegraphsim.OEGetFPType(oegraphsim.OEFPType_Tree))
oedepict.OEPrepareMultiAlignedDepiction(fitmol, refmol, overlaps)
opts = oedepict.OE2DMolDisplayOptions(grid.GetCellWidth(), grid.GetCellHeight(),
                                      oedepict.OEScale_AutoScale)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
refscale = oedepict.OEGetMoleculeScale(refmol, opts)
fitscale = oedepict.OEGetMoleculeScale(fitmol, opts)
opts. SetScale(min(refscale, fitscale))
refdisp = oedepict.OE2DMolDisplay(refmol, opts)
```

```
fitdisp = oedepict.OE2DMolDisplay(fitmol, opts)
refcell = grid.GetCell(1, 1)oedepict.OERenderMolecule(refcell, refdisp)
fitted1 = grid.GetCell(1, 2)oedepict.OERenderMolecule(fitcell, fitdisp)
```

oedepict.OEWriteImage("FPAlign.png", image)

![](_page_55_Figure_3.jpeg)

Fig. 36: Example of depiction with alignment based on molecule similarity

#### See also:

- OEImageGrid class
- · OERenderMolecule function
- · OEWriteImage function

### See also:

The Python script that visualizes molecule similarity based on fingerprints can be downloaded from the OpenEye Python Cookbook

(continued from previous page)

![](_page_56_Figure_1.jpeg)

# **2.9 Generating Interactive SVG Images**

## 2.9.1 SVG group

SVG group is a container for grouping and naming collections of SVG drawing elements. In OEDepict TK, the OESVGGroup class is to used for grouping drawing instructions together.

The code snippet below shows how to create and use an OESVGGroup object.

```
svg_group_circ = image.NewSVGGroup("circle")
image.PushGroup(svg_group_circ)
image.DrawCircle(oedepict.OEGetCenter(image), 30, oedepict.OERedBoxPen)
image.PopGroup(svg_group_circ)
oedepict.OEWriteImage("CreateSVGGroup.svg", image)
```

- First an OESVGGroup object is created on the image by calling the OEImageBase. NewSVGGroup method.
- The OESVGGroup object is the can be utilized by invoking the OEImageBase. PushGroup method. This result in writing the  $\leq q$  id='circle' > line into the syq image.
- Each push has to be coupled with a corresponding pop. When the OEImageBase. PopGroup method is invoked the  $\langle \rangle$  g> closing line will be written into the image file.

The above snippet will generate the following svg image:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
 "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
→viewBox="0.00 0.00 100.00 100.00">
<!-- Created by OpenEye Scientific Software -->
<!-- Creation Date Fri Mar 3 16:37:06 2017 -->
<rect width="100.00" height="100.00" fill="white" />
```

```
<q id='circle'>
<circle cx="50.00" cy="50.00" r="30.00" fill="red" stroke="red" stroke-linejoin="round
\rightarrow" stroke-linecap="round" />
</g>
\langle/svq>
```

The guideline below should be followed when using SVG groups in OEDepict TK:

- The name of the OESVGGroup has to be unique for the given image and it can only contain alphanumeric,  $\alpha$  or - characters.
- An OESVGGroup object can be used (pushed / popped) only once.
- *OESVGGroup* objects can be nested. They should be used in LIFO (for last in, first out) i.e. the group that has been pushed last should be popped first.

See also:

- Group SVG element section in MDN
- Grouping section in W3C

## 2.9.2 SVG class

In **OEDepict TK**, the *OESVGClass* class can be used to add class attributes to group containers.

The code snippet below shows how to create and use an OESVGClass object.

```
svq_qroup_circ = image. NewSVGGroup("circle")svg_group_rect = image.NewSVGGroup("rectangle")
svg_class_objs = image.NewSVGClass("object")
svg_group_circ.AddSVGClass(svg_class_objs)
svg_group_rect.AddSVGClass(svg_class_objs)
image.PushGroup(svg_group_circ)
image.DrawCircle(oedepict.OEGetCenter(image), 30, oedepict.OERedBoxPen)
image.PopGroup(svg_group_circ)
image.PushGroup(svg_group_rect)
image.DrawRectangle(oedepict.OE2DPoint(10, 10), oedepict.OE2DPoint(90, 90), oedepict.
\rightarrowOELightGreyPen)
image.PopGroup(svg_group_rect)
```

- oedepict.OEWriteImage("CreateSVGClass.svg", image)
  - First two OESVGGroup objects are created on the image, followed by creating a OESVGClass object by calling the OEImageBase. NewSVGClass method.
  - The OESVGClass object then can be added to any groups by calling  $OESVGGroup$ . AddSVGClass method.
  - When a OESVGGroup object is pushed classes associated with it will be written into the syq file:  $\leq q$ id='circle' class='object'> and <q id='rectangle' class='object'>.

The above snippet will generate the following svg image:

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
```

```
"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"
→viewBox="0.00 0.00 100.00 100.00">
<!-- Created by OpenEye Scientific Software -->
<!-- Creation Date Fri Mar 3 17:22:19 2017 -->
<rect width="100.00" height="100.00" fill="white" />
<q id='circle' class='object'>
<circle cx="50.00" cy="50.00" r="30.00" fill="red" stroke="red" stroke-linejoin="round
\rightarrow" stroke-linecap="round" />
</\alpha<g id='rectangle' class='object'>
<rect x="10" y="10" width="80" height="80" fill="none" stroke="#bfbfbf" stroke-
→linejoin="round" stroke-linecap="round" />
</q>
\langle/svq>
```

The guideline below should be followed when using SVG classes in OEDepict TK:

- The name of the OESVGClass has to be unique for the given image and it can only contain alphanumeric, or - characters.
- An OESVGClass object can be associated with multiple OESVGGroup objects.
- An OESVGGroup object can be associated with multiple OESVGClass objects.

#### See also:

- MDN Class attribute section in MDN
- WSC Class attribute section in WSC

## 2.9.3 Examples of Generating Interactive SVG Images

**OEDepict TK** also provides high-level APIs that are not only group SVG elements together but also adds styles and events to them to generate interactive images.

See the following **OEDepict TK** API:

- OEAddSVGHover and OEAddSVGToggle low-level functions that allow to add effects to any objects.
- OEAddSVGC1ickEvent low-level functions that allows to add click event to any objects.
- OEDrawSVGHoverText function that displays a text associated with an atom or bond when the mouse is hovering over their position on the image.
- OEDrawSVGToggleText function that displays a text associated with an atom or bond when clicking at their position on the image.

See also the following **OEGrapheme TK** APIs that generate interactive SVG images:

- OERenderContactMap function that generated an interactive protein-ligand contact map image. Clicking on any residue will highlight those ligand atoms that are interacting with the residue.
- · OEDrawIridiumData function
- OEDrawPeptide function
- OERenderRamachandranPlot function
- · OERenderBFactorMap function

## 2.9.4 Inserting SVG Images into HTML

The interactive svg image generated by OEDepict TK and Grapheme TK can inserted into HTML files with the SVG MIME type:

```
<object data="<imagename>.svg" type="image/svg+xml"></object>
```

The following example inserts two svg images into an HTML table:

```
<!DOCTYPE html>
\verb|thtml|><head>
  <title>test</title>
\langle/head>
<body>
<h2>Examples of interactive SVG images inserted into HTML</h2>
<table style="width:100%">
  <tr>
    <th>hover atom text</th>
    <th>toggle atom text</th>
  \langle/tr>
  <+ r >
  <td><object data="hover-atom-text.svg" type="image/svg+xml" width = "400" ></
→object></td>
  <td><object data="toqqle-atom-text.svq" type="image/svq+xml" width = "400" ></
→object></td>
  \langle/tr>
</table>
\langle/body>
\langle/html>
```

Download the following three files and open the insert-index.html file in a browser.

## 2.9.5 How to Catch SVG Events

The example in this section illustrates how to throw a mouse event in an . svq image and how to catch it in a html  $filA$ 

The code below shows how to create an . svq image where each atom is associated with an SVG event. When clicking on an atom in the image, a click event is fired with the message specified in the OEAddSVGC1ickEvent function.

```
width, height = 400, 200
image = oedepict. OEImage (width, height)
mol = occhem.OEGraphMol()smiles = "Cclccencl/C=C/[C@H] (C(=0) 0) 0"oechem.OESmilesToMol(mol, smiles)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetMargins(10)
disp = oedepict.OE2DMolDisplay(mol, opts)
```

```
for adisp in disp. GetAtomDisplays():
   atom = adisp.GetAtom()message = "atom idx = *s" * atom. GetIdx ()
   oedepict.OEAddSVGClickEvent(disp, adisp, message)
oedepict.OERenderMolecule("AddAtomClickEvent.svg", disp)
```

The events thrown by the AddAtomClickEvent. svg image can be caught in the html file that contains the image. The following html file illustrates how to catch the events and display the messages that were associated with the atoms using the OEAddSVGClickEvent function.

```
<! DOCTYPE htm1><html>
<head>
  <title>test</title>
  <script type="text/javascript">
    window.addEventListener("load", init);
    function init() {
      var svg = document.getElementById('depictsvg');
      svg.contentDocument.addEventListener('OEDepictSVGEvent', function(evt) {
        var logarea = document.querySelector('.svg-event-log');
        logarea.innerHTML = evt.detail.message;
      \});
  \langle/script>
\langle/head>
<body>
<h2> Image </h2>
<object data="AddAtomClickEvent.svg" type="image/svg+xml" id="depictsvg" width = "400
\leftrightarrow" ></object>
<h2>Event log message:</h2>
<h4 class="svg-event-log">
\langle/h4>
\langle /body>
```

To try it out follow the instructions below:

 $\langle$ /html>

- 1. Generate a directory (such as test) that contains both the AddAtomClickEvent.svg and the index. html file (click on them to download).
- 2. Start up a HTTP server inside test directory

prompt> python -m http.server

- 3. Open http://0.0.0.0.8000 in your browser (see image below)
- 4. Click on any atom on the image and the message specified by the OEAddSVGC1ickEvent function will be displayed below the image.

![](_page_61_Picture_1.jpeg)

# **Image**

![](_page_61_Figure_3.jpeg)

# Event log message:

atom idx=6

Fig. 37: Screenshot of the OEAddSVGClickEvent example in the browser

## **THREE**

# **EXAMPLES**

# **3.1 OEDepict Examples**

The following table lists the currently available OEDepict TK examples:

| Program                   | Description                                     |
|---------------------------|-------------------------------------------------|
| <i>depict.py</i>          | generating 2D coordinates                       |
| <i>match2img.py</i>       | depicting substructure search match             |
| <i>mcsalign2D.py</i>      | aligning molecules based on MCS                 |
| <i>mdlquery2img.py</i>    | depicting MDL query                             |
| <i>mdlreaction2img.py</i> | depicting MDL reaction                          |
| <i>mol2img.py</i>         | depicting a single molecule                     |
| <i>mols2pdf.py</i>        | depicting molecules in a multi-page image       |
| <i>mols2img.py</i>        | depicting molecules in a grid                   |
| <i>ringdict2pdf.py</i>    | generating 2D ring dictionary report            |
| <i>smartsalign2D.py</i>   | aligning molecules based on substructure search |
| <i>viewmdlsearch.py</i>   | depicting MDL query substructure search hits    |

### **Examples:**

## 3.1.1 Generating 2D coordinates

A program that assigns 2D coordinates to molecule(s).

## **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python depict.py --help
```

## will generate the following output:

```
Simple parameter list
input/output options :
  -in : Input filename
  -out : Output filename
  -ringdict : User-defined 2D ring dictionary
prepare depiction options :
```

```
-orientation : Set the preferred orientation of 2D coordinates
-suppressH : Suppress explicit hydrogens of molecule(s)
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
# Generates 2D coordinates
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[_name_]):
    itf = oechem. OEInterface(InterfaceData)
    oedepict.OEConfigurePrepareDepictionOptions(itf,
                                               oedepict.OEPrepareDepictionSetup_
→SuppressHydrogens |
                                               oedepict.OEPrepareDepictionSetup_
\rightarrowDepictOrientation)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = itf. GetString("in")ifs = oechem.oemolistream()
   if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   ofs = oechem.oemolostream(".sdf")
    if itf.HasString("-out"):
       oname = \text{iff}. \text{GetString}("-out")if not ofs.open(oname):
           oechem. OEThrow. Fatal ("Cannot open output file!")
       if not oechem. OEIs2DFormat (ofs. GetFormat ()) :
```

```
oechem. OEThrow. Fatal ("Invalid output format for 2D coordinates")
   if itf.HasString("-ringdict"):
       rdfname = itf.GetString("-ringdict")
       if not oechem. OEInit2DRingDictionary (rdfname) :
           oechem. OEThrow. Warning ("Cannot use user-defined ring dictionary!")
   popts = oedepict.OEPrepareDepictionOptions()
   oedepict.OESetupPrepareDepictionOptions(popts, itf)
   popts.SetClearCoords(True)
   for mol in ifs. GetOEGraphMols():
       oedepict.OEPrepareDepiction(mol, popts)
       oechem.OEWriteMolecule(ofs, mol)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = ""!BRIEF [-in] <input> [-out] <output> [-ringdict] <rd file>
!CATEGORY "input/output options :"
 !PARAMETER -in
   !ALIAS -i!TYPE string
   !REQUIRED true
   !KEYLESS 1
   !VISIBILITY simple
   !BRIEF Input filename
 ! END
 !PARAMETER -out
   !ALIAS -o
   !TYPE string
   !REQUIRED false
   IKEYLESS<sub>2</sub>
   !VISIBILITY simple
   !BRIEF Output filename
 ! END
 !PARAMETER -ringdict
   !ALIAS -rd
   !TYPE string
   !REQUIRED false
   !VISIBILITY simple
   !BRIEF User-defined 2D ring dictionary
   !DETAIL
       2D ring dictionaries can be generated by the following OEChem examples:
       C++ - createringdict.cpp
       Python - createringdict.py
       Java - CreateRingDict.java
             - CreateRingDict.cs
       C#
```

```
! END
! END
\mathbf{u} as \mathbf{u}{\rm __name}\_ = = "{\rm __main}\_".if
      sys.exit(main(sys.argv))
```

#### See also:

- · OEConfigurePrepareDepictionOptionsfunction
- OEIs2DFormat function
- OEPrepareDepictionOptions class
- · OESetupPrepareDepictionOptionsfunction
- · OEPrepareDepiction function

#### **Example**

```
prompt> python depict.py .ism .mol
C (=0) N
```

will generate the following output:

```
-OEChem-07031123462D3 \quad 2 \quad 00 0 0 0 0 0 0999 V2000
  0.0000 0.0000 0.0000 C 0 0 0 0 0 0 0 0 0
  1.0000 0.0000 0.0000 0 0 0 0 0 0 0 0 0 0 0 0 
  -0.5000 -0.86600.0000 N 0 0 0 0 0 0 0 0 0 0 0 0 0
 1 \t2 \t2 \t0 \t0 \t0 \t01 \t3 \t1 \t0 \t0 \t0 \t0END
M
```

Note: The above program can generate 2D coordinates with user-defined 2D ring layouts when using the -ringdict parameter.

See also the 2D coordinate generation examples section of the OEChem TK manual that shows examples about how to generate and utilize user-defined ring dictionaries.

## 3.1.2 Depicting Substructure Search Match

A program that performs a substructure search initialized with the given SMARTS pattern and highlights the identified matches on the depicted molecule.

## **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python match2imq.py --help

will generate the following output:

```
Simple parameter list
highlight options :
   -highlightcolor : Highlighting color
   -highlightstyle : Highlighting style
image options :
  -height : Height of output image
  -width : Width of output image
input/output options :
  -in : Input filename
  -out : Output filename
  -smarts : SMARTS pattern
molecule display options :
  -aromstyle : Aromatic ring display style
  -atomcolor : Atom coloring style
  -atomlabelfontscale : Atom label font scale
  -atomprop : Atom property display
  -atomstereostyle : Atom stereo display style
  -bondcolor : Bond coloring style
  -bondprop : Bond property display
  -bondstereostyle : Bond stereo display style
  -hydrstyle : Hydrogen display style
  -linewidth : Default bond line width
  -protgroupdisp : Protective group display style
  -scale : Scaling of the depicted molecule
  -superdisp : Super atom display style
  -titleloc : Location of the molecule title
prepare depiction options :
  -clearcoords : Clear and regenerate 2D coordinates of molecule(s)
  -orientation : Set the preferred orientation of 2D coordinates
  -suppressH : Suppress explicit hydrogens of molecule(s)
```

### **Code**

#!/usr/bin/env python # (C) 2022 Cadence Design Systems, Inc. (Cadence) # All rights reserved. # TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is # provided to current licensees or subscribers of Cadence products or # SaaS offerings (each a "Customer"). # Customer is hereby permitted to use, copy, and modify the Sample Code, # subject to these terms. Cadence claims no rights to Customer's # modifications. Modification of Sample Code is at Customer's sole and # exclusive risk. Sample Code may require Customer to have a then # current license or subscription to the applicable Cadence offering.

```
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
#######################################
# Depict a molecule and highlight the substructure specified by
# the given SMARTS pattern
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData)
    oedepict.OEConfigureImageOptions(itf)
    oedepict.OEConfigurePrepareDepictionOptions(itf)
    oedepict.OEConfigure2DMolDisplayOptions(itf)
   oedepict.OEConfigureHighlightParams(itf)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = \text{itf}.\text{GetString}("-in")oname = \text{itf}.\text{GetString}("-out")ext = oechem. OEGetFileExtension (oname)
    if not oedepict. OEIsRegisteredImageFile(ext):
        oechem. OEThrow. Fatal ("Unknown image type!")
   if s = oechem. oemolistream()if not ifs.open(iname):
        oechem. OEThrow. Fatal ("Cannot open input file!")
   ofs = occhem.oeofstream()if not ofs.open(oname):
        oechem. OEThrow. Fatal ("Cannot open output file!")
   mol = occhem.OEGraphMol()if not oechem. OEReadMolecule(ifs, mol):
        oechem. OEThrow. Fatal ("Cannot read input file!")
   smarts = itf.GetString("-smarts")
    ss = oechem. OESubSearch()
    if not ss. Init (smarts):
        oechem. OEThrow. Fatal ("Cannot parse smarts: %s" % smarts)
   popts = oedepict.OEPrepareDepictionOptions()
   oedepict.OESetupPrepareDepictionOptions(popts, itf)
    oedepict.OEPrepareDepiction(mol, popts)
```

```
(continued from previous page)
```

```
width, height = oedepict.OEGetImageWidth(itf), oedepict.OEGetImageHeight(itf)
   dopts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
   oedepict.OESetup2DMolDisplayOptions(dopts, itf)
   dopts. SetMargins (10.0)
   disp = oedepict.OE2DMolDisplay(mol, dopts)
   hstyle = oedepict.OEGetHighlightStyle(itf)
   hcolor = oedepict.OEGetHighlightColor(itf)
   oechem.OEPrepareSearch(mol, ss)
   unique = Truefor match in ss. Match (mol, unique):
       oedepict.OEAddHighlighting(disp, hcolor, hstyle, match)
   oedepict.OERenderMolecule(ofs, ext, disp)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = \n'!BRIEF [-in] <input> [-smarts] <smarts> [-out] <output image>
!CATEGORY "input/output options :"
   !PARAMETER -in
     !ALIAS -i
     !TYPE string
     !REQUIRED true
     !KEYLESS 1
     !VISIBILITY simple
     !BRIEF Input filename
   ! END
   !PARAMETER -smarts
     !TYPE string
     !REOUIRED true
     !KEYLESS 2
     !VISIBILITY simple
     !BRIEF SMARTS pattern
   ! END
   !PARAMETER -out
     IATITAS -<sub>O</sub>!TYPE string
     !REQUIRED true
     !KEYLESS 3
     !VISIBILITY simple
     !BRIEF Output filename
   !END
! END
```

```
if name == " main ":
   sys.exit(main(sys.argv))
```

#### See also:

r i i

- · OEConfigureImageOptionsfunction
- · OEConfigurePrepareDepictionOptionsfunction
- · OEConfigure2DMolDisplayOptions function
- OEConfigureHighlightParams function
- · OESetup2DMolDisplayOptions function
- OESubSearch class
- OEPrepareDepictionOptions class
- OESetupPrepareDepictionOptionsfunction
- · OEPrepareDepiction function
- · OEGetImageWidth and OEGetImageHeight functions
- OE2DMolDisplayOptions class
- OESetup2DMolDisplayOptions function
- OE2DMolDisplay class
- · OEGetHighlightStyle and OEGetHighlightColor functions
- OEPrepareSearch function
- · OEAddHighlighting function
- OERenderMolecule function

### **Examples**

prompt> python match2img.py -in indole.ism -out image.png -smarts "clccccc1"

will generate the image shown in Figure: Example of using the program with default highlighting

![](_page_69_Picture_24.jpeg)

Fig. 1: Example of using the program with default highlighting

prompt> python match2img.py -in indole.ism -out image.png -smarts "clcccccl" -→highlightcolor green

will generate the image shown in Figure: Example of using the program with green highlighting

![](_page_70_Figure_1.jpeg)

#### Fig. 2: Example of using the program with green highlighting

```
prompt> python match2img.py -in indole.ism -out image.png -smarts "clccccc1" -
→highlightstyle BallAndStick
```

will generate the image shown in Figure: Example of using the program with ball and stick

![](_page_70_Picture_5.jpeg)

Fig. 3: Example of using the program with ball and stick highlighting

See also:

```
• Highlighting chapter
```

## 3.1.3 Aligning Molecule Based on MCS

A program that aligns molecules based on their maximum common substructure.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python mcsalign2D.py --help
```

#### will generate the following output:

```
Simple parameter list
input/output options :
  -fit : Align filename
  -out : Output filename
  -ref : Ref filename
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
# Aligns the fit molecule(s) based on their maximum common substructure
# with the reference molecule.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[_name_]):
   itf = oechem. OEInterface(InterfaceData)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   {\ttаrname = itf.GetString("-ref")
   fname = itf.fetString("-fit")oname = itf.GetString("-out")rifs = oechem.oemolistream()if not rifs.open(rname):
       oechem. OEThrow. Fatal ("Cannot open reference molecule file!")
   refmol = occhem.OEGraphMol()if not oechem. OEReadMolecule (rifs, refmol) :
       oechem. OEThrow. Fatal ("Cannot read reference molecule!")
   fits = occhem.oemolistream()if not fifs.open(fname):
       oechem. OEThrow. Fatal ("Cannot open align molecule file!")
   ofs = occhem.oemolostream()if not ofs.open(oname):
       oechem. OEThrow. Fatal ("Cannot open output file!")
   if not oechem. OEIs2DFormat (ofs. GetFormat ()):
```

```
oechem. OEThrow. Fatal ("Invalid output format for 2D coordinates")
   oedepict.OEPrepareDepiction(refmol)
   mcss = oechem.OEMCSSearch(oechem.OEMCSType_Approximate)
   atomexpr = oechem. OEExprOpts_DefaultAtoms
   bondexpr = oechem. OEExprOpts_DefaultBonds
   mcss. Init (refmol, atomexpr, bondexpr)
   mcss.SetMCSFunc(oechem.OEMCSMaxBondsCompleteCycles())
   oechem.OEWriteConstMolecule(ofs, refmol)
   for fitmol in fifs. GetOEGraphMols():
       alignres = oedepict. OEPrepareAlignedDepiction (fitmol, mcss)
       if alignres. IsValid():
           oechem. OEThrow. Info ("%s mcs size: %d" % (fitmol. GetTitle (), alignres.
\rightarrowNumAtoms()))
           oechem.OEWriteMolecule(ofs, fitmol)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-ref] <input> [-fit] <input> [-out] <output>
!CATEGORY "input/output options :"
   !PARAMETER -ref
     !ALIAS -r!TYPE string
     !REQUIRED true
     IKEYLESS 1
     !VISIBILITY simple
     !BRIEF Ref filename
   ! END
   IPARAMETER - fit!ALIAS -f!TYPE string
     !REQUIRED true
     !KEYLESS 2
     !VISIBILITY simple
     !BRIEF Align filename
   ! END
   !PARAMETER -out
     !ALIAS -o
     !TYPE string
     !REQUIRED true
     !KEYLESS 3
     !VISIBILITY simple
     !BRIEF Output filename
    LEND
```

```
! END
\mathbf{Y} \in \mathbf{Y} \times \mathbf{Y}name_ = = "_main__".if
      sys.exit(main(sys.argv))
```

#### See also:

- Molecule Alignment chapter
- OEIs2DFormat function
- · OEPrepareDepiction function
- OEMCSSearch class
- · OEPrepareAlignedDepiction function

### **Example**

prompt> python mcsalign2D.py -ref ace1.ism -fit ace2.ism -out out.mol

taking the output coordinates and generating the images with the mol2img program will produce the images shown in Table: Example of using the program to align two molecules based on MCS.

![](_page_73_Figure_12.jpeg)

![](_page_73_Figure_13.jpeg)

See also:

• Molecule Alignment chapter

## **3.1.4 Depicting MDL Query**

A program that converts an MDL query structure into an image file.

### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python mdlquery2img.py --help
```

will generate the following output:

```
Simple parameter list
image options :
  -height : Height of output image
  -width : Width of output image
input/output options :
  -in : Input filename
  -out : Output filename
molecule display options :
  -aromstyle : Aromatic ring display style
  -atomcolor : Atom coloring style
  -atomlabelfontscale : Atom label font scale
  -atomprop : Atom property display
  -atomstereostyle : Atom stereo display style
  -bondcolor : Bond coloring style
  -bondprop : Bond property display
  -bondstereostyle : Bond stereo display style
  -hydrstyle : Hydrogen display style
  -linewidth : Default bond line width
  -protgroupdisp : Protective group display style
   -scale: Scaling of the depicted molecule
  -superdisp : Super atom display style
   -titleloc : Location of the molecule title
```

#### **Code**

#!/usr/bin/env python # (C) 2022 Cadence Design Systems, Inc. (Cadence) # All rights reserved. # TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is # provided to current licensees or subscribers of Cadence products or # SaaS offerings (each a "Customer"). # Customer is hereby permitted to use, copy, and modify the Sample Code, # subject to these terms. Cadence claims no rights to Customer's # modifications. Modification of Sample Code is at Customer's sole and # exclusive risk. Sample Code may require Customer to have a then # current license or subscription to the applicable Cadence offering. # THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, # EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT # NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A # PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be # liable for any damages or liability in connection with the Sample Code

# or its use.

(continued from previous page)

```
#######################################
# Converts an MDL query structure into an image file.
# The output file format depends on its file extension.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[_name_]):
   itf = oechem. OEInterface (InterfaceData)
   oedepict.OEConfigureImageOptions(itf)
   oedepict.OEConfigure2DMolDisplayOptions(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = itf.GetString("in")oname = \text{itf}.\text{GetString}("-out")ext = oechem.OEGetFileExtension(oname)
   if not oedepict. OEIsRegisteredImageFile(ext):
       oechem. OEThrow. Fatal ("Unknown image type!")
   ifs = occhem.oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   if ifs.GetFormat() != oechem.OEFormat_MDL:
       oechem. OEThrow. Fatal ("Input file is not an MDL query file")
   ofs = occhem.oeofstream()if not ofs.open(oname):
       oechem. OEThrow. Fatal ("Cannot open output file!")
   mol = occhem.OEGraphMol()if not oechem. OEReadMDLOuervFile(ifs, mol):
       oechem. OEThrow. Fatal ("Cannot read mdl query input file!")
   clearcoords, suppressH = False, False
   oedepict.OEPrepareDepiction(mol, clearcoords, suppressH)
   width, height = oedepict.OEGetImageWidth(itf), oedepict.OEGetImageHeight(itf)
   opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
   oedepict.OESetup2DMolDisplayOptions(opts, itf)
   disp = oedepict.OE2DMolDisplay(mol, opts)
   oedepict.OERenderMolecule(ofs, ext, disp)
   return 0
######################################
```

```
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-in] <input> [-out] <output image>
!CATEGORY "input/output options :"
   !PARAMETER -in
     IATITAS -i!TYPE string
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
! END
\mathbf{r} \cdot \mathbf{r} \cdot \mathbf{r}if _name_ = = "_main_".sys.exit(main(sys.argv))
```

- MDL Query Depiction chapter
- · OEConfigureImageOptionsfunction
- · OEConfigure2DMolDisplayOptions function
- · OEIsRegisteredImageFilefunction
- · OEReadMDLQueryFile function
- · OEPrepareDepiction function
- · OEGet ImageWidth and OEGet ImageHeight functions
- OE2DMolDisplayOptions class
- · OESetup2DMolDisplayOptions function
- OE2DMolDisplay class
- · OERenderMolecule function

#### **Examples**

prompt> python mdlquery2imq.py -in mdlquery.mol -out image.png

will generate the image shown in Figure: Example of depicting an MDL query

![](_page_77_Figure_4.jpeg)

Fig. 4: Example of depicting an MDL query

### See also:

• MDL Query Depiction chapter

## 3.1.5 Depicting MDL Reaction

A program that converts an MDL reaction into an image file.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python mdlreaction2img.py --help
```

will generate the following output:

```
Simple parameter list
image options :
  -height : Height of output image
  -width : Width of output image
input/output options :
  -in : Input filename
  -out : Output filename
molecule display options :
  -aromstyle : Aromatic ring display style
  -atomcolor : Atom coloring style
  -atomlabelfontscale : Atom label font scale
  -atomprop : Atom property display
  -atomstereostyle : Atom stereo display style
  -bondcolor : Bond coloring style
  -bondprop : Bond property display
  -bondstereostyle : Bond stereo display style
```

```
-hydrstyle : Hydrogen display style
-linewidth : Default bond line width
-protgroupdisp : Protective group display style
-scale : Scaling of the depicted molecule
-superdisp : Super atom display style
-titleloc : Location of the molecule title
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
#######################################
# Converts an MDL reaction into an image file.
# The output file format is depends on its file extension.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[__name__]):
   itf = oechem. 0EInterface()oechem. OEConfigure(itf, InterfaceData)
   oedepict.OEConfigureImageOptions(itf)
   oedepict.OEConfigure2DMolDisplayOptions(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = itf.GetString("-in")oname = itf.GetString("-out")
   ext = oechem.OEGetFileExtension(oname)
   if not oedepict. OEIsRegisteredImageFile(ext):
       oechem. OEThrow. Fatal ("Unknown image type!")
   if s = oechem.oemolistream()
```

```
if not ifs.open(iname):
        oechem. OEThrow. Fatal ("Cannot open input file!")
   ofs = occhem.oeofstream()if not ofs.open(oname):
        oechem. OEThrow. Fatal ("Cannot open output file!")
   mol = occhem.OEGraphMol()if not oechem. OEReadMDLReactionQueryFile(ifs, mol):
       oechem. OEThrow. Fatal ("Cannot read mdl reaction!")
   clearcoords, suppressH = False, False
   oedepict.OEPrepareDepiction(mol, clearcoords, suppressH)
   width, height = oedepict.OEGetImageWidth(itf), oedepict.OEGetImageHeight(itf)
   opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
   oedepict.OESetup2DMolDisplayOptions(opts, itf)
   disp = oedepict.OE2DMolDisplay(mol, opts)
   oedepict.OERenderMolecule(ofs, ext, disp)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-in] <input> [-out] <output image>
!CATEGORY "input/output options :"
    !PARAMETER -in
     !ALIAS -i
      !TYPE string
     !REQUIRED true
     !KEYLESS 1
     !VISIBILITY simple
     !BRIEF Input filename
   !END
   !PARAMETER -out
     !ALIAS -o
      !TYPE string
     !REQUIRED true
     !KEYLESS 2
     !VISIBILITY simple
     !BRIEF Output filename
    LEND
!END
\mathbf{r} \cdot \mathbf{r} \cdot \mathbf{r}if name == " main ":
   sys.exit(main(sys.argv))
```

### See also:

- MDL Reaction Depiction chapter
- · OEConfigureImageOptionsfunction
- · OEConfigure2DMolDisplayOptions function
- · OEIsRegisteredImageFilefunction
- · OEReadMDLReactionQueryFile function
- · OEPrepareDepiction function
- · OEGet ImageWidth and OEGet ImageHeight functions
- OE2DMolDisplayOptions class
- · OESetup2DMolDisplayOptions function
- OE2DMolDisplay class
- · OERenderMolecule function

### **Examples**

prompt> python mdlreaction2img.py -in mdlreaction.sdf -out image.png

will generate the following image: Figure: Example of depicting an MDL reaction

![](_page_80_Figure_16.jpeg)

Fig. 5: Example of depicting an MDL reaction

prompt> python mdlreaction2img.py -in mdlreaction.sdf -out image.png -atomprop MapIdx

will generate the following image: Figure: Example of depicting an MDL reaction with atom map indices

![](_page_80_Figure_20.jpeg)

Fig. 6: Example of depicting an MDL reaction with atom map indices

### See also:

• MDL Reaction Depiction chapter

## 3.1.6 Depicting a Single Molecule

A program that converts a molecular structure into an image file.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python mol2img.py --help

will generate the following output:

```
Simple parameter list
image options :
  -height : Height of output image
  -width : Width of output image
input/output options :
  -in : Input filename
  -out : Output filename
  -ringdict : User-defined 2D ring dictionary
molecule display options :
  -aromstyle : Aromatic ring display style
  -atomcolor : Atom coloring style
  -atomlabelfontscale : Atom label font scale
  -atomprop : Atom property display
  -atomstereostyle : Atom stereo display style
  -bondcolor : Bond coloring style
  -bondprop : Bond property display
  -bondstereostyle : Bond stereo display style
  -hydrstyle : Hydrogen display style
  -linewidth : Default bond line width
  -protgroupdisp : Protective group display style
  -scale : Scaling of the depicted molecule
  -superdisp : Super atom display style
   -titleloc : Location of the molecule title
prepare depiction options :
  -clearcoords : Clear and regenerate 2D coordinates of molecule(s)
  -orientation : Set the preferred orientation of 2D coordinates
   -suppressH : Suppress explicit hydrogens of molecule(s)
```

### **Code**

#!/usr/bin/env python # (C) 2022 Cadence Design Systems, Inc. (Cadence) # All rights reserved. # TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is # provided to current licensees or subscribers of Cadence products or # SaaS offerings (each a "Customer"). # Customer is hereby permitted to use, copy, and modify the Sample Code, # subject to these terms. Cadence claims no rights to Customer's # modifications. Modification of Sample Code is at Customer's sole and # exclusive risk. Sample Code may require Customer to have a then

```
# current license or subscription to the applicable Cadence offering.
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
#######################################
# Converts a molecule structure into an image file.
# The output file format depends on its file extension.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[__name__]):
    itf = oechem. OEInterface (InterfaceData)
    oedepict.OEConfigureImageOptions(itf)
    oedepict.OEConfigurePrepareDepictionOptions(itf)
    oedepict.OEConfigure2DMolDisplayOptions(itf)
    if not oechem. OEParseCommandLine(itf, argv):
        oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = \text{itf}.\text{GetString}("-in")oname = \text{itf}.\text{GetString}("-out")ext = oechem.OEGetFileExtension(oname)
    if not oedepict. OEIsRegisteredImageFile(ext):
       oechem. OEThrow. Fatal ("Unknown image type!")
    if s = oechem. oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   ofs = occhem.oeofstream()if not ofs.open(oname):
       oechem. OEThrow. Fatal ("Cannot open output file!")
   mol = occhem.OEGraphMol()if not oechem. OEReadMolecule (ifs, mol) :
        oechem. OEThrow. Fatal ("Cannot read input file!")
    if itf.HasString("-ringdict"):
        rdfname = itf. GetString("-ringdict")if not oechem. OEInit2DRingDictionary (rdfname) :
            oechem. OEThrow. Warning ("Cannot use user-defined ring dictionary!")
   popts = oedepict.OEPrepareDepictionOptions()
   oedepict.OESetupPrepareDepictionOptions(popts, itf)
    oedepict.OEPrepareDepiction(mol, popts)
```

```
width, height = oedepict.OEGetImageWidth(itf), oedepict.OEGetImageHeight(itf)
   dopts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
   oedepict.OESetup2DMolDisplayOptions(dopts, itf)
   disp = oedepict.OE2DMolDisplay(mol, dopts)
   oedepict.OERenderMolecule(ofs, ext, disp)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = ""!BRIEF [-in] <input> [-out] <output image> [-ringdict] <rd file>
!CATEGORY "input/output options :"
  !PARAMETER -in
   !ALIAS -i!TYPE string
   !REOUIRED true
   IKEYLESS 1
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
  !PARAMETER -ringdict
   !ALIAS -rd
   !TYPE string
   !REQUIRED false
   !VISIBILITY simple
   !BRIEF User-defined 2D ring dictionary
   !DETAIL
       2D ring dictionaries can be generated by the following OEChem examples:
       C++ - createringdict.cpp
       Python - createringdict.py
       Java - CreateRingDict.java
       C#- CreateRingDict.cs
    !END
!END
\mathbf{u},\mathbf{u},\mathbf{u}if name == " main ":
   sys.exit(main(sys.argv))
```

#### See also:

- Molecule Depiction chapter
- · OEConfigureImageOptionsfunction
- · OEConfigurePrepareDepictionOptions function
- OEConfigure2DMolDisplayOptions function
- · OEIsRegisteredImageFilefunction
- OEPrepareDepictionOptions class
- · OESetupPrepareDepictionOptionsfunction
- · OEPrepareDepiction function
- OEGet ImageWidth and OEGet ImageHeight functions
- OE2DMolDisplayOptions class
- OESetup2DMolDisplayOptions function
- OE2DMolDisplay class
- OERenderMolecule function

### **Examples**

prompt> python mol2img.py -in nexium.ism -out image.png

will generate the image shown in Figure: Example of using the program with default parameters.

![](_page_84_Figure_18.jpeg)

Fig. 7: Example of using the program with default parameters

prompt> python mol2img.py -in nexium.ism -out image.png -atomcolor WhiteMonochrome

will generate the image shown in Figure: Example of using the program with the white monochrome atom coloring style.

prompt> python mol2img.py -in nexium.ism -out image.png -aromstyle Circle

will generate the image shown in Figure: Example of using the program with aromaticity style 'Circle'.

```
prompt> python mol2img.py -in nexium.ism -out image.png -atomstereostyle
→ "AtomStereo | CIPAtomStereo"
```

will generate the image shown in Figure: Example of the mol2img program with CIP atom stereo option.

![](_page_85_Figure_1.jpeg)

Fig. 8: Example of using the program with the white monochrome atom coloring style

![](_page_85_Figure_3.jpeg)

Fig. 9: Example of using the program with aromaticity style 'Circle'

![](_page_85_Figure_5.jpeg)

Fig. 10: Example of using the program with CIP atom stereo option

```
prompt> python mol2img.py -in nexium.ism -out image.png -linewidth 4
```

will generate the image shown in Figure: Example of using the program with user-defined line width.

![](_page_85_Figure_9.jpeg)

Fig. 11: Example of using the program with user-defined line width

prompt> python mol2img.py -in nexium.ism -out image.png -superdisp All

will generate the image shown in Figure: Example of using the program with superatom style.

![](_page_86_Figure_1.jpeg)

Fig. 12: Example of using the program with superatom style

Note: The above program can generate 2D coordinates with user-defined 2D ring layouts when using the -ringdict parameter.

See also the 2D coordinate generation examples section of the OEChem TK manual that shows examples about how to generate and utilize user-defined ring dictionaries.

#### See also:

• Molecule Depiction chapter

## 3.1.7 Depicting Molecules In a Grid

A program that converts molecular structures into an image with a grid layout. By default the input molecules are depicted in a 3x2 grid.

### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python mols2img.py --help

will generate the following output:

```
Simple parameter list
-height : Height of output image
-width : Width of output image
image grid options :
  -cols : Number of columns
  -rows : Number of rows
input/output options :
  -in : Input filename(s)
  -out : Output filename
molecule display options :
  -aromstyle : Aromatic ring display style
  -atomcolor : Atom coloring style
  -atomlabelfontscale : Atom label font scale
  -atomprop : Atom property display
  -atomstereostyle : Atom stereo display style
```

```
-bondcolor : Bond coloring style
  -bondprop : Bond property display
 -bondstereostyle : Bond stereo display style
 -hydrstyle : Hydrogen display style
  -linewidth : Default bond line width
  -protgroupdisp : Protective group display style
  -scale : Scaling of the depicted molecule
  -superdisp : Super atom display style
  -titleloc : Location of the molecule title
prepare depiction options :
 -clearcoords : Clear and regenerate 2D coordinates of molecule(s)
 -orientation : Set the preferred orientation of 2D coordinates
 -suppressH : Suppress explicit hydrogens of molecule(s)
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
# Converts molecules into an image with grid layout.
# The output file format depends on its file extension.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[_name_]):
   itf = oechem. 0EInterface()oechem. OEConfigure(itf, InterfaceData)
   oedepict.OEConfigureImageWidth(itf, 400.0)
   oedepict.OEConfigureImageHeight(itf, 400.0)
   oedepict.OEConfigureImageGridParams(itf)
   oedepict.OEConfigurePrepareDepictionOptions(itf)
   oedepict.OEConfigure2DMolDisplayOptions(itf)
```

```
(continued from previous page)
```

```
if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   oname = itf.GetString("-out")
   ext = oechem.OEGetFileExtension(oname)
   if not oedepict. OEIsRegisteredImageFile(ext):
       oechem. OEThrow. Fatal ("Unknown image type!")
   ofs = occhem.oeofstream()if not ofs.open(oname):
       oechem. OEThrow. Fatal ("Cannot open output file!")
   width, height = oedepict. OEGetImageWidth(itf), oedepict. OEGetImageHeight(itf)
   image = odeplot.OEImage (width, height)rows = oedepict.OEGetImageGridNumRows(itf)
   cols = oedepict.OEGetImageGridNumColumns(itf)
   grid = oedepict.OEImageGrid(image, rows, cols)
   popts = oedepict.OEPrepareDepictionOptions()
   oedepict.OESetupPrepareDepictionOptions(popts, itf)
   dopts = oedepict.OE2DMolDisplayOptions()
   oedepict.OESetup2DMolDisplayOptions(dopts, itf)
   dopts. SetDimensions(grid. GetCellWidth(), grid. GetCellHeight(), oedepict. OEScale_
\rightarrowAutoScale)
   celliter = grid.GetCells()for iname in itf.GetStringList("-in"):
       if s = oechem.oemolistream()if not ifs.open(iname):
           oechem. OEThrow. Warning ("Cannot open %s input file!" % iname)
           continue
       for mol in ifs.GetOEGraphMols():
           if not celliter. IsValid():
               break
           oedepict.OEPrepareDepiction(mol, popts)
           disp = oederict.OE2DMolDisplay(mol, dots)oedepict.OERenderMolecule(celliter.Target(), disp)
           celliter.Next()
   oedepict.OEWriteImage(ofs, ext, image)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = '''
!BRIEF -in <input1> [ <input2> .. ] -out <output image>
!CATEGORY "input/output options :"
```

```
!PARAMETER -in
      !ALIAS -i!TYPE string
      !LIST true
      !REQUIRED true
      !VISIBILITY simple
      !BRIEF Input filename(s)
    !END
    !PARAMETER -out
      !ALIAS -o
      !TYPE string
      !REQUIRED true
      !VISIBILITY simple
      !BRIEF Output filename
    !END
! END
\mathbf{r} \cdot \mathbf{r} .
if __name__ == "_main_":
    sys.exit(main(sys.argv))
```

- Molecule Layouts chapter
- · OEConfigureImageWidth function
- · OEConfigureImageHeight function
- · OEConfigureImageGridParamsfunction
- · OEConfigurePrepareDepictionOptions function
- · OEConfigure2DMolDisplayOptions function
- · OEGetImageWidth and OEGetImageHeight functions
- OEGet ImageGridNumRows and OEGet ImageGridNumColumns functions
- OEImageGrid class
- OEPrepareDepictionOptions class
- · OESetupPrepareDepictionOptionsfunction
- OE2DMolDisplayOptions class
- · OESetup2DMolDisplayOptions function
- · OEPrepareDepiction function
- · OERenderMolecule function
- · OEWriteImage function

## **Examples**

prompt> python mols2img.py -in amino.ism -out image.png

will generate the image shown in Figure: Example of using the program with default parameters.

![](_page_90_Figure_4.jpeg)

![](_page_90_Figure_5.jpeg)

Note: By default the program depicts molecules in a 3x2 grid

prompt> python mols2img.py -in amino.ism -out image.png -rows 2 -cols 3

will generate the image shown in Figure: Example of using the program with user-defined number of rows and columns.

prompt> python mols2img.py -in amino.ism -out image.png -rows 2 -cols 2 -titleloc\_  $\rightarrow$ Bottom

will generate the image shown in Figure: Example of using the program with molecule titles displayed at the bottom.

See also:

• Depicting Molecules in a Grid section

![](_page_91_Figure_1.jpeg)

Fig. 14: Example of using the program with user-defined number of rows and columns

![](_page_91_Figure_3.jpeg)

Fig. 15: Example of using the program with molecule titles displayed at the bottom

## 3.1.8 Depicting Molecules in Multi-Page

A program that converts molecular structures into a multi-page PDF image.

## **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python mols2pdf.py --help

#### will generate the following output:

```
Simple parameter list
input/output options :
 -in : Input filename
 -out : Output filename
 -ringdict : User-defined 2D ring dictionary
molecule display options :
 -aromstyle : Aromatic ring display style
 -atomcolor : Atom coloring style
 -atomlabelfontscale : Atom label font scale
 -atomprop : Atom property display
 -atomstereostyle : Atom stereo display style
 -bondcolor : Bond coloring style
 -bondprop : Bond property display
 -bondstereostyle : Bond stereo display style
 -hydrstyle : Hydrogen display style
 -linewidth : Default bond line width
 -protgroupdisp : Protective group display style
 -scale : Scaling of the depicted molecule
 -superdisp : Super atom display style
 -titleloc : Location of the molecule title
prepare depiction options :
 -clearcoords : Clear and regenerate 2D coordinates of molecule(s)
 -orientation : Set the preferred orientation of 2D coordinates
 -suppressH : Suppress explicit hydrogens of molecule(s)
report options :
 -colsperpage : Number of columns per page
 -pageheight : Page height
 -pageorientation : Page orientation
 -pagesize : Page size
 -pagewidth : Page width
 -rowsperpage : Number of rows per page
```

#### See also:

• Multi Page Reports chapter

Note: The above program can generate 2D coordinates with user-defined 2D ring layouts when using the -ringdict parameter.

See also the 2D coordinate generation examples section of the OEChem TK manual that shows examples about how to generate and utilize user-defined ring dictionaries.

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
# Converts molecules into a multi-page PDF document.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[__name__]):
   itf = oechem. OEInterface (InterfaceData)
   oedepict.OEConfigureReportOptions(itf)
   oedepict.OEConfigurePrepareDepictionOptions(itf)
   oedepict.OEConfigure2DMolDisplayOptions(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       return 1iname = itf.GetString("-in")if s = oechem. oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
   oname = itf.GetString("-out")ext = oechem.OEGetFileExtension(oname)
   if ext != "pdf":
       oechem. OEThrow. Fatal ("Output must be PDF format.")
   ofs = ochem.oeofstream()if not ofs.open(oname):
       oechem. OEThrow. Fatal ("Cannot open output file!")
    if itf.HasString("-ringdict"):
        rdfname = itf. GetString("-ringdict")if not oechem. OEInit2DRingDictionary (rdfname) :
           oechem. OEThrow. Warning ("Cannot use user-defined ring dictionary!")
```

```
ropts = oedepict.OEReportOptions()
   oedepict.OESetupReportOptions(ropts, itf)
   ropts.SetFooterHeight(25.0)
   report = oedepict.OEReport (ropts)
   popts = oedepict.OEPrepareDepictionOptions()
   oedepict.OESetupPrepareDepictionOptions(popts, itf)
   dopts = oedepict.OE2DMolDisplayOptions()
   oedepict.OESetup2DMolDisplayOptions(dopts, itf)
   dopts. SetDimensions (report. GetCellWidth (), report. GetCellHeight (), oedepict.
\rightarrowOEScale_AutoScale)
   for mol in ifs.GetOEGraphMols():
       cell = report.MewCell()oedepict.OEPrepareDepiction(mol, popts)
       disp = oedefict.OE2DMolDisplay(mol, dopts)oedepict.OERenderMolecule(cell, disp)
   font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Bold,
-12,
                          oedepict.OEAlignment_Center, oechem.OEBlack)
   for pagenum, footer in enumerate (report. GetFooters ()) :
       text = "Page %d of %d" % (pagenum + 1, report. NumPages())
       oedepict.OEDrawTextToCenter(footer, text, font)
   oedepict.OEWriteReport(ofs, ext, report)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-in] <input> [-out] <output pdf> [-ringdict] <rd file>
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
   !REOUIRED true
   !KEYLESS 2
   !VISIBILITY simple
   !BRIEF Output filename
```

```
!PARAMETER -ringdict
   !ALIAS -rd
   !TYPE string
   !REQUIRED false
    !VISIBILITY simple
    !BRIEF User-defined 2D ring dictionary
    !DETAIL
        2D ring dictionaries can be generated by the following OEChem examples:
        C++ - createringdict.cpp
       Python - createringdict.py
       Java - CreateRingDict.java
       C# - CreateRingDict.cs
    ! END
! END
\mathbf{r} \cdot \mathbf{r}if __name__ == '__main__".sys.exit(main(sys.argv))
```

#### See also:

! END

- Multi Page Images chapter
- · OEConfigureReportOptionsfunction
- · OEConfigurePrepareDepictionOptionsfunction
- · OEConfigure2DMolDisplayOptions function
- OEReportOptions class
- · OESetupReportOptions function
- OEReport class
- OEPrepareDepictionOptions class
- · OESetupPrepareDepictionOptionsfunction
- OE2DMolDisplayOptions class
- · OESetup2DMolDisplayOptions function
- · OEPrepareDepiction function
- OE2DMolDisplay class
- · OERenderMolecule function
- OEFont class
- · OEDrawTextToCenter function
- · OEWriteReport function

## 3.1.9 Generating 2D Ring Dictionary Report

A program that generate a multi-page PDF report of the 2D ring dictionary.

### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python ringdict2pdf.py --help

Will generate the following output:

```
Simple parameter list
   input/output options :
     -out : Output filename
     -ringdict : Input ring dictionary filename
   report options :
     -colsperpage : Number of columns per page
     -pageheight : Page height
     -pageorientation : Page orientation
     -pagesize : Page size
     -pagewidth : Page width
     -rowsperpage : Number of rows per page
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
# Converts a ring dictionary into a multi-page PDF document.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[_name_]):
```

```
itf = oechem. OEInterface(InterfaceData)
   oedepict.OEConfigureReportOptions(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   ifname = itf. Getsuring("-ringdict")ofname = itf. GetString("-out")if not oechem. OEIsValid2DRingDictionary(ifname):
       oechem. OEThrow. Fatal ("Invalid ring dictionary file!")
   ringdict = oechem. OE2DRingDictionary (ifname)
   ropts = oedepict.OEReportOptions()
   oedepict.OESetupReportOptions(ropts, itf)
   oedepict.OEWrite2DRingDictionaryReport(ofname, ringdict, ropts)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = ""!BRIEF [-ringdict] <input ringdict> [-out] <output pdf>
!CATEGORY "input/output options :"
   !PARAMETER -ringdict
     !ALIAS -rd
     !TYPE string
     !REOUIRED true
     !KEYLESS 1
     !VISIBILITY simple
     !BRIEF Input ring dictionary filename
     IDETATL
       2D ring dictionaries can be generated by the following OEChem examples:
       C++ - createringdict.cpp
       Python - createringdict.py
       Java - CreateRingDict.java
             - CreateRingDict.cs
       C#! END
   !PARAMETER -out
     IATITAS -<sub>O</sub>!TYPE string
     !REQUIRED true
     !KEYLESS 2
     !VISIBILITY simple
     !BRIEF Output filename
   !END
```

!END

```
\overline{n} \overline{n} \overline{n}if
        name
                     == "__main__".sys.exit(main(sys.argv))
```

#### See also:

- 2D coordinate generation examples section in the OEChem TK manual
- OE2DRingDictionary class
- · OEIsValid2DRingDictionary function
- OEWrite2DRingDictionaryReport function

#### **Example**

prompt> python ringdict2pdf.py -ringdict rtd.oeb -out rtd.pdf

will generate a multi-page PDF report similar to the one shown in Table: Example of ring dictionary report.

![](_page_98_Figure_11.jpeg)

#### Table 2: Example of ring dictionary report (The pages are reduced here for visualization convenience)

- OE2DRingDictionary class in the OEChem TK manual
- 2D coordinate generation examples section in the OEChem TK manual that shows examples about how to create and manipulate user-defined ring dictionaries.

## 3.1.10 Aligning Molecules Based on Substructure Search

A program that aligns the molecules based on a substructure search initialized with the given SMARTS pattern.

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python smartsalign2D.py --help
```

#### Will generate the following output:

```
Simple parameter list
input/output options :
  -in : Filename of input molecules
  -out : Output filename
  -smarts : SMARTS for alignment match
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
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
#######################################
# Aligns molecules to a smarts pattern
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main (argv=[\_name]):
   itf = oechem. OEInterface (InterfaceData)
   if not oechem. OEParseCommandLine(itf, argv):
       oechem. OEThrow. Fatal ("Unable to interpret command line!")
   iname = itf.GetString("-in")
```

```
(continued from previous page)
```

```
oname = \text{itf}.\text{GetString}("-out")smarts = itf.GetString("-smarts")
   qmol = oechem.OEQMol()if not oechem. OEParseSmarts (qmol, smarts):
       oechem. OEThrow. Fatal ("Invalid SMARTS: %s" % smarts)
   oechem.OEGenerate2DCoordinates(qmol)
   ss = oechem.OESubSearch(qmol)
   if not ss. IsValid():
       oechem. OEThrow. Fatal ("Unable to initialize substructure search!")
   if s = oechem. oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input molecule file!")
   ofs = oechem.oemolostream()
   if not ofs.open(oname):
       oechem. OEThrow. Fatal ("Cannot open output file!")
   if not oechem. OEIs2DFormat (ofs. GetFormat ()):
       oechem. OEThrow. Fatal ("Invalid output format for 2D coordinates")
   for mol in ifs.GetOEGraphMols():
       oechem.OEPrepareSearch(mol, ss)
       alignres = oedepict.OEPrepareAlignedDepiction(mol, ss)
       if not alignres. IsValid():
           oechem. OEThrow. Warning ("Substructure is not found in input molecule!")
           oedepict.OEPrepareDepiction(mol)
       oechem.OEWriteMolecule(ofs, mol)
    return 0
#######################################
# INTERFACE
#######################################
InterfaceData = '''
!BRIEF [-in] <input> [-smarts] <smarts> [-out] <output>
!CATEGORY "input/output options :"
    !PARAMETER -in
     !ALIAS -i
      !TYPE string
     !REOUIRED true
     IKEYLESS 1
     !VISIBILITY simple
     !BRIEF Filename of input molecules
    ! END
    !PARAMETER -smarts
     !ALIAS -s! TYPE string
      !REQUIRED true
```

```
!KEYLESS 2
       !VISIBILITY simple
       !BRIEF SMARTS for alignment match
     ! END
     !PARAMETER -out
       !ALIAS -o
       !TYPE string
       !REQUIRED true
       !KEYLESS 3
       !VISIBILITY simple
       !BRIEF Output filename
     !END
! END
\mathbf{Y} \in \mathbf{Y} \times \mathbf{Y}if _name_ = = "_main_".sys.exit(main(sys.argv))
```

#### See also:

- Molecule Alignment chapter
- OESubSearch class
- OEGenerate2DCoordinates function
- OEIs2DFormat function
- OEPrepareSearch function
- OEPrepareAlignedDepiction function
- · OEPrepareDepiction function

## **Examples**

```
prompt> python smartsalign2D.py -in test.sdf -out aligned.sdf -smarts "clcc[c,
→n]c2c1ncc2" -out out.mol
```

Taking the output coordinates and generating the images with the *molling* program will produce the images shown in Table: Example of using the program to align molecule

![](_page_101_Figure_14.jpeg)

## Table 3: Example of using the program to align molecules

See also:

• Molecule Alignment chapter

## 3.1.11 Depicting MDL Query Substructure Search Hits

A program that performs substructure search on a molecule using an MDL query and generates an image file one match per molecule.

### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python viewmdlsearch.py --help
```

Will generate the following output:

```
Simple parameter list
general options :
  -align : Align hits to query
highlight options :
  -highlightcolor : Highlighting color
  -highlightstyle : Highlighting style
input/output options :
  -out : Output image filename
  -query : Input query filename
  -target : Input target filename
molecule display options :
  -aromstyle : Aromatic ring display style
  -atomcolor : Atom coloring style
  -atomlabelfontscale : Atom label font scale
  -atomprop : Atom property display
  -atomstereostyle : Atom stereo display style
  -bondcolor : Bond coloring style
  -bondprop : Bond property display
  -bondstereostyle : Bond stereo display style
  -hydrstyle : Hydrogen display style
  -linewidth : Default bond line width
  -protgroupdisp : Protective group display style
  -scale : Scaling of the depicted molecule
  -superdisp : Super atom display style
  -titleloc : Location of the molecule title
 report options :
  -colsperpage : Number of columns per page
  -pageheight : Page height
  -pageorientation : Page orientation
  -pagesize : Page size
  -pagewidth : Page width
   -rowsperpage : Number of rows per page
```

#### See also:

• Multi Page Reports chapter

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
# Performs substructure search on a molecule using a MDL query and
# generates an image file depicting one match per molecule.
# The output file format depends on its file extension.
#######################################
import sys
from openeye import oechem
from openeye import oedepict
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
   itf = oechem. OEInterface (InterfaceData)
   oedepict.OEConfigureReportOptions(itf)
   oedepict.OEConfigure2DMolDisplayOptions(itf)
   oedepict.OEConfigureHighlightParams(itf)
   if not oechem. OEParseCommandLine(itf, argv):
       return 1
   \text{qname} = \text{itf}.\text{GetString}("-query"){\tt thame} = {\tt itf.GetString("-target")}oname = itf.GetString("-out")ext = oechem.OEGetFileExtension(oname)
   if not oedepict. OEIsRegisteredMultiPageImageFile(ext):
        oechem. OEThrow. Fatal ("Unknown multipage image type!")
   qfile = oechem, oemolistream()if not qfile.open(qname):
        oechem. OEThrow. Fatal ("Cannot open mdl query file!")
    if qfile.GetFormat() != oechem.OEFormat_MDL and qfile.GetFormat() != oechem.
→OEFormat_SDF:
        oechem. OEThrow. Fatal ("Query file has to be an MDL file!")
```

```
(continues on next page)
```

ifs = oechem.oemolistream()

```
(continued from previous page)
```

```
if not ifs.open(tname):
       oechem. OEThrow. Fatal ("Cannot open target input file!")
   depictquery = oechem. OEGraphMol()
   if not oechem. OEReadMDLQueryFile(qfile, depictquery):
       oechem. OEThrow. Fatal ("Cannot read query molecule!")
   oedepict.OEPrepareDepiction(depictquery)
   queryopts = oechem. OEMDLQueryOpts_Default | oechem. OEMDLQueryOpts_
\rightarrowSuppressExplicitH
   qmol = oechem.OEQMol()oechem.OEBuildMDLQueryExpressions(qmol, depictquery, queryopts)
   ss = oechem. OESubSearch()
   if not ss. Init (qmol):
       oechem. OEThrow. Fatal ("Cannot initialize substructure search!")
   hstyle = oedepict.OEGetHighlightStyle(itf)
   hcolor = oedepict.OEGetHighlightColor(itf)
   align = itf.GetBool("-align")
   ropts = oedefict.OEReportOptions()oedepict.OESetupReportOptions(ropts, itf)
   ropts.SetHeaderHeight(140.0)
   report = oedepict.OEReport (ropts)
   dopts = odeplot.OE2DMolDisplayOptions()oedepict.OESetup2DMolDisplayOptions(dopts, itf)
   cellwidth, cellheight = report.GetCellWidth(), report.GetCellHeight()
   dopts. SetDimensions (cellwidth, cellheight, oedepict. OEScale_AutoScale)
   unique = Truefor mol in ifs. GetOEGraphMols():
       oechem.OEPrepareSearch(mol, ss)
       miter = ss.Match(mol, unique)if not miter. IsValid():
           continue # no match
       alignres = oedepict.OEAlignmentResult(miter.Target())
       if align:
           alignres = oedepict.OEPrepareAlignedDepiction(mol, ss)
       else:
           oedepict.OEPrepareDepiction(mol)
       cell = report. NewCell()disp = oedefict.OE2DMolDisplay(mol, dopts)if alignres. IsValid():
           oedepict. OEAddHighlighting(disp, hcolor, hstyle, alignres)
       oedepict.OERenderMolecule(cell, disp)
       oedepict.OEDrawBorder(cell, oedepict.OELightGreyPen)
   # render query structure in each header
   headwidth, headheight = report.GetHeaderWidth(), report.GetHeaderHeight()
   dopts. SetDimensions (headwidth, headheight, oedepict. OEScale_AutoScale)
   disp = oedepict.OE2DMolDisplay(depictquery, dopts)
   for header in report. GetHeaders () :
```

```
(continued from previous page)
```

```
oedepict.OERenderMolecule(header, disp)
       oedepict.OEDrawBorder(header, oedepict.OELightGreyPen)
   oedepict.OEWriteReport(oname, report)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = \n'!BRIEF [-query] <input> [-target] <input> [-out] <output multipage image> [-align]
!CATEGORY "input/output options :"
 !PARAMETER -query
   !ALIAS -q
   !TYPE string
   !REQUIRED true
   !KEYLESS 1
   !VISIBILITY simple
   !BRIEF Input query filename
 ! END
 !PARAMETER -target
   !ALIAS -t
   !TYPE string
   !REQUIRED true
   !KEYLESS 2
   !VISIBILITY simple
   !BRIEF Input target filename
 ! END
 !PARAMETER -out
   !ALIAS -o
   !TYPE string
   !REQUIRED true
   !KEYLESS 3
   !VISIBILITY simple
   !BRIEF Output image filename
 ! END
!END
!CATEGORY "general options :"
 !PARAMETER -align
   !TYPE bool
   !REQUIRED false
   !DEFAULT false
   !VISIBILITY simple
   !BRIEF Align hits to query
 !END
! END
```

```
name == " main ":
if
   sys.exit(main(sys.argv))
```

#### See also:

i i i

- Multi Page Images and MDL Query Depiction chapters
- · OEConfigureReportOptionsfunction
- · OEConfigure2DMolDisplayOptions function
- OEConfigureHighlightParams function
- · OEIsRegisteredMultiPageImageFilefunction
- · OEReadMDLQueryFile function
- · OEPrepareDepiction function
- · OEBuildMDLQueryExpressions function
- OESubSearch class
- · OEGetHighlightStyle and OEGetHighlightColor functions
- OEReportOptions class
- OESetupReportOptions function
- OEReport class
- OE2DMolDisplayOptions class
- · OESetup2DMolDisplayOptions function
- OEPrepareSearch function
- · OEPrepareAlignedDepiction function
- · OEPrepareDepiction function
- OE2DMolDisplay class
- · OEAddHighlighting function
- · OERenderMolecule function
- · OEDrawBorder function
- · OEWriteReport function

# **3.2 Python Cookbook Examples**

There are large number of code examples available in OpenEye Python Cookbook that use OpenEye Toolkits to solve a wide range of cheminformatics and molecular modeling problems.

- 2D Depiction chapter contains examples that illustrate how the OEDepict TK and Grapheme TK can be utilized to depict molecules and visualize properties calculated with other OpenEye toolkits.
- Visualizing 3D Information chapter contains examples that illustrate how the Grapheme TK can be utilized to project complex 3D information into the 2D molecular graph.

• Cheminformatics chapter contains examples that solve various cheminformatics problems such as similarity search, ring perception and manipulating molecular graphs.

### OpenEye Python Cookbook examples using OEDepict TK

- Depicting Reaction Components
- Depicting Multiple Matches
- Depicting Library Generation
- Depicting Molecular Graph Symmetry
- Highlighting Fragments

# **FOUR**

**API** 

# **4.1 OEDepict Classes**

## 4.1.1 OE2DAtomDisplay

class OE2DAtomDisplay : public OEAtomDisplayBase

This class stores 2D depiction information of an atom. See Figure: OEDepict TK atom display class hierarchy.

![](_page_108_Figure_7.jpeg)

Fig. 1: OEDepict TK atom display class hierarchy

The following figure (Figure: Example of the layout of an atom) illustrates how atoms are rendered in the OEDepict TK.

- The atom label is positioned at the coordinates returned by the  $OE2DLtombisplay$ . GetCoords method. The string that is rendered as an atom label is returned by the OE2DAtomDisplay. GetLabel method.
- If the atom has a charge, then it is rendered as a super-script on the right side of the atomic label.

See also:

- OE2DAtomDisplay.GetCharge method
- If the atom has isotope information, then it is rendered as a super-script on the left side of the atomic label.

See also:

- OE2DAtomDisplay.GetMass method

• If the atom has implicit hydrogen(s), then the *hydrogen label* is positioned in a cardinal direction relative to the atomic label. The number of implicit hydrogens and the position can be accessed by calling the OE2DAtomDisplay.GetHCount and the OE2DAtomDisplay.GetHPosition methods, respectively.

#### See also:

- OEHydrogenStyle namespace
- OEHydrogenPos namespace
- All labels (isotope, atomic, charge and explicit hydrogen) has the same color that is associated with the atomic number.

## See also:

- OEAtomColorStyle namespace
- Appendix: Element coloring (CPK) chapter

![](_page_109_Figure_9.jpeg)

Fig. 2: Example of the layout of an atom

The following methods are publicly inherited from OEAtomDisplayBase:

| GetDataType | IsDataType | SetVisible |
|-------------|------------|------------|
| GetAtom     | IsVisible  |            |

The OE2DAtomDisplay class stores the following properties:

| Property                    | Get method        | Set method        | Corresponding namespace / class / type |
|-----------------------------|-------------------|-------------------|----------------------------------------|
| rendered formal charge      | GetCharge         | SetCharge         | integer                                |
| position of the atom label  | GetCoords         | SetCoords         | OE2DPoint class                        |
| hydrogen count              | GetHCount         | SetHCount         | unsigned int                           |
| position of hydrogen label  | GetHPosition      | SetHPosition      | OEHydrogenPos namespace                |
| rendered atom label         | GetLabel          | SetLabel          | string                                 |
| font of atom label          | GetLabelFont      | SetLabelFont      | OEFont class                           |
| rendered isotope number     | GetMass           | SetMass           | integer                                |
| rendered string as property | GetProperty       | SetProperty       | string                                 |
| font of property string     | GetPropertyFont   | SetPropertyFont   | OEFont class                           |
| position of property label  | GetPropertyOffset | SetPropertyOffset | OE2DPoint class                        |
| rendered radical type       | GetRadical        | SetRadical        | OERadicalDisplayType namespace         |

## **Constructors**

```
OE2DAtomDisplay (const OEChem:: OEAtomBase* atom)
```

Construct an OE2DAtomDisplay object that contains the style information for atom.

```
OE2DAtomDisplay (const OE2DAtomDisplay & rhs)
```

Copy constructor.

#### operator=

OE2DAtomDisplay & operator=(const OE2DAtomDisplay & rhs)

Assignment operator.

## **CreateCopy**

OESystem:: OEBase \*CreateCopy() const

Deep copy constructor that returns a pointer to a copy of the object. The memory returned is dynamically allocated and owned by the caller.

#### **GetCharge**

```
int GetCharge () const
```

Returns the charge rendered next to the atomic label. See example in Figure: Example of charge representation. The number will be rendered in the following ways:

- 0 nothing is rendered
- -1 negative sign "-" is rendered
- 1 positive sign "+" is rendered
- less than  $-1$  " $-\langle n \rangle$ " is rendered

greater than  $1$  "+<n>" is rendered

![](_page_111_Picture_9.jpeg)

Fig. 3: Example of charge representation

#### See also:

· OE2DAtomDisplay. SetCharge method

### **GetCoords**

const OE2DPoint &GetCoords () const

Returns the coordinates of the atom in the coordinate system that is defined when a OE2DMolDisplay object is constructed with a specific width and height. This is the exact location of the atom when it is rendered into an image.

- · OE2DAtomDisplay. SetCoords method
- OE2DPoint method

## **GetHCount**

![](_page_112_Figure_2.jpeg)

Returns the hydrogen count to render for this atom. See example in Figure: Example of hydrogen count representation. The number will be rendered in the following ways:

0 no "H" label is rendered

1 "H" is rendered next to the atomic label

greater than 1 this number is rendered as a sub-script of the "H" label

![](_page_112_Figure_7.jpeg)

### Fig. 4: Example of hydrogen count representation

#### See also:

- · OE2DAtomDisplay. SetHCount method
- · OE2DAtomDisplay. SetHPosition method

### **GetHPosition**

unsigned int GetHPosition() const

Returns the position of the hydrogen label relative to the atomic label. The return value is taken from the OEHydrogenPos namespace.

- · OE2DAtomDisplay. SetHPosition method
- · OE2DAtomDisplay. SetHCount method
- · OEHydrogenPos namespace

### **GetLabel**

```
const std:: string & GetLabel() const
```

Returns the string that is rendered as the atomic label at the coordinates returned by the  $OE2DAtombisplay$ . Get Coords method. The color of the font is set by the

### See also:

· OE2DAtomDisplay. SetLabel method

## **GetLabelFont**

```
const OEFont &GetLabelFont () const
```

Returns the font that is used when rendering the atomic label string of the OE2DAtomDisplay object.

#### See also:

- · OE2DAtomDisplay. SetLabelFont method
- · OE2DAtomDisplay. SetLabel method
- OEFont class

### **GetMass**

```
unsigned int GetMass() const
```

Returns the isotope information rendered as a super-script next to the atomic label. If zero, nothing is rendered. See example in Figure: Example of isotope representation.

![](_page_113_Figure_16.jpeg)

Fig. 5: Example of isotope representation

#### See also:

· OE2DAtomDisplay. SetMass method

#### **GetProperty**

const std:: string & GetProperty () const

Returns the string rendered next to the atom. If the string is empty, nothing is rendered.

#### See also:

- · OE2DAtomDisplay. SetProperty method
- · OE2DAtomDisplay. SetPropertyFont method

### **GetPropertyFont**

const OEFont & GetPropertyFont () const

Returns the font that is used when rendering the property string of the OE2DAtomDisplay object.

#### See also:

- · OE2DAtomDisplay. SetPropertyFont method
- · OE2DAtomDisplay. SetProperty method
- OEFont class

### **GetPropertyOffset**

const OE2DPoint &GetPropertyOffset() const

Returns the offset vector relative to the coordinates returned by OE2DAtomDisplay. GetCoords that is used to position the property label of the atom. These vectors are calculated during OE2DMolDisplay construction to minimize potentially clashing with the rest of the depiction. See Figure: The property offset vector is relative to coordinates returned by the GetCoords method.

![](_page_114_Figure_17.jpeg)

#### Fig. 6: The property offset vector is relative to coordinates returned by the OE2DAtomDisplay::GetCoords method

This allows for any string representable information to be rendered at a logical location near the atom. See example in Example of indices as an atom property.

- · OE2DAtomDisplay. SetPropertyOffset method
- OE2DPoint class

![](_page_115_Figure_1.jpeg)

### Fig. 7: Example of indices as an atom property

#### **GetRadical**

unsigned int GetRadical() const

Returns the radical display type of the atom. The return value is taken from the OERadicalDisplayType namespace. See example in *Example of rendering radicals*.

![](_page_115_Figure_6.jpeg)

Fig. 8: Example of rendering radicals

#### See also:

- · OE2DAtomDisplay. SetRadical method
- · OERadicalDisplayType namespace

### **HasLabel**

bool HasLabel() const

Returns whether or not the atomic label string of the OE2DAtomDisplay object is empty.

- · OE2DAtomDisplay.GetLabel method
- · OE2DAtomDisplay. SetLabel method

### **HasProperty**

bool HasProperty () const

Returns whether or not the property string of the OE2DAtomDisplay object is empty.

#### See also:

- · OE2DAtomDisplay. GetProperty method
- · OE2DAtomDisplay. SetProperty method

### **SetCharge**

void SetCharge (int charge)

Sets the charge rendered next to the atomic label.

#### See also:

· OE2DAtomDisplay. GetCharge method

#### **SetCoords**

void SetCoords (const OE2DPoint & coords)

Sets the exact coordinates of the atom in the rendered image.

#### See also:

- · OE2DAtomDisplay. GetCoords method
- OE2DPoint method

## **SetHCount**

void SetHCount (unsigned int hoount)

Set the hydrogen count to render for this atom.

#### See also:

• OE2DAt omDisplay. GetHCount method for more information on the meaning of various input integers.

### **SetHPosition**

void SetHPosition (unsigned int hpos)

Sets the position of hydrogen label relative to the atomic label.

**hpos** This value has to be from the  $OEHydrogenPos$  namespace.

- · OE2DAtomDisplay.GetHPosition method
- OEHydrogenPos namespace

### **SetLabel**

void SetLabel (const std::string &label)

Sets the string that is rendered as the "atomic" label at the position returned by the  $OE2DAtomDisplay$ . GetCoords method.

#### See also:

· OE2DAtomDisplay.GetLabel method

## **SetLabelFont**

void SetLabelFont (const OEFont & font)

Sets the font that is used when rendering the atomic label of the OE2DAtomDisplay object.

#### See also:

· OE2DAtomDisplay.GetLabelFont method

#### **SetMass**

void SetMass (unsigned int mass)

Sets the isotope information rendered next to the atomic label.

#### See also:

· OE2DAtomDisplay. GetMass method

#### **SetProperty**

void SetProperty (const std:: string &label)

Sets the string rendered next to the atom.

**Warning:** The preferred way to set the atom property strings is to use the  $OE2DMolDisplays$ SetAtomPropertyFunctor method. See example in the Displaying Atom Properties section.

- · OE2DAtomDisplay. SetProperty method
- · OE2DAtomDisplay. SetPropertyFont method
- · OE2DMolDisplayOptions. SetAtomPropertyFunctor method

## **SetPropertyFont**

void SetPropertyFont (const OEFont & font)

Sets the font that is used when rendering the property string of the OE2DAtomDisplay object.

**Warning:** The preferred way to set the font of the atom property strings is to use the OE2DMolDisplayOptions. SetAtomPropLabelFont method.

#### See also:

- OE2DAtomDisplay.GetPropertyFont method
- · OE2DAtomDisplay.GetProperty method
- OEFont class
- OE2DMolDisplayOptions. SetAtomPropLabelFont method

#### **SetPropertyOffset**

void SetPropertyOffset (const OE2DPoint & offset)

Sets the offset vector that is used to position the property label of the atom.

#### See also:

- · OE2DAtomDisplay.GetPropertyOffset method
- OE2DPoint class

## **SetRadical**

void SetRadical (*unsigned int radical*)

Sets the radical type of the atom.

radical This value has to be from the OERadicalDisplayType namespace.

See also:

- · OE2DAtomDisplay.GetRadical method
- · OERadicalDisplayType namespace

## 4.1.2 OE2DBondDisplay

class OE2DBondDisplay : public OEBondDisplayBase

This class stores 2D depiction information of a bond. See Figure: OEDepict TK bond display class hierarchy.

The following methods are publicly inherited from OEBondDisplayBase:

| GetDataType | IsDataType | SetVisible |
|-------------|------------|------------|
| GetBond     | IsVisible  |            |

![](_page_119_Figure_1.jpeg)

Fig. 9: OEDepict TK bond display class hierarchy

The OE2DBondDisplay class stores the following properties:

| Property                                  | Get method        | Set method        | Corresponding namespace / class / type |
|-------------------------------------------|-------------------|-------------------|----------------------------------------|
| pen used to draw the<br>begin of the bond | GetBgnPen         | SetBgnPen         | <i>OEPen</i> class                     |
| pen used to draw the<br>end of the bond   | GetEndPen         | SetEndPen         | <i>OEPen</i> class                     |
| position of multi-line bonds              | GetDisplayPos     | SetDisplayPos     | OEBondDisplayPosition namespace        |
| rendered bond type                        | GetDisplayType    | SetDisplayType    | OEBondDisplayType namespace            |
| rendered string as property               | GetProperty       | SetProperty       | string                                 |
| font of property string                   | GetPropertyFont   | SetPropertyFont   | <i>OEFont</i> class                    |
| position of property label                | GetPropertyOffset | SetPropertyOffset | OE2DPoint class                        |

## **Constructors**

OE2DBondDisplay(const OEChem::OEBondBase\* bond)

Construct an OE2DBondDisplay object that contains the style information for bond.

OE2DBondDisplay (const OE2DBondDisplay & rhs)

Copy constructor.

#### operator=

```
OE2DBondDisplay &operator=(const OE2DBondDisplay &rhs)
```

Assignment operator.

### **CreateCopy**

OESystem:: OEBase \*CreateCopy() const

Deep copy constructor that returns a pointer to a copy of the object. The memory returned is dynamically allocated and owned by the caller.

#### **GetBgnPen**

const OEPen & GetBgnPen() const

Returns the pen used to draw the bond from the "begin" atom coordinates to the middle of the bond.

![](_page_120_Figure_10.jpeg)

#### See also:

- · OE2DBondDisplay. SetBgnPen method
- OEPen class

## **GetDisplayPos**

unsigned int GetDisplayPos() const

Returns how multi-line bonds should be rendered. The return value is taken from the OEBondDisplayPosition namespace.

Note: The OEBondDisplayPosition namespace only affects bonds of the following types (as returned by OE2DBondDisplay.GetDisplayType):

- OEBondDisplayType\_Double
- · OEBondDisplayType\_AromaticDash
- · OEBondDisplayType\_SingleDouble
- · OEBondDisplayType\_SingleArom
- OEBondDisplayType\_DoubleArom

· OEBondDisplayType\_Aromatic

#### See also:

- · OE2DBondDisplay. SetDisplayPos method
- OEBondDisplayPosition namespace

## **GetDisplayType**

unsigned int GetDisplayType() const

Returns how bond orders, stereochemistry, and aromaticity is rendered for the bond. The return value is taken from the OEBondDisplayType namespace.

#### See also:

- · OE2DBondDisplay. SetDisplayType method
- OEBondDisplayType namespace

### **GetEndPen**

const OEPen & GetEndPen() const

Returns the pen used to draw the bond from the "end" atom coordinates to the middle of the bond.

![](_page_121_Picture_14.jpeg)

bond.GetEnd()bond.GetBgn()

#### See also:

- · OE2DBondDisplay. SetEndPen method
- OEPen class

#### **GetProperty**

const std:: string & GetProperty () const

### Returns the string displayed next to the bond.

- · OE2DBondDisplay. SetProperty method
- · OE2DBondDisplay. SetPropertyFont method

### **GetPropertyFont**

const OEFont & GetPropertyFont () const

Returns the font that is used when displaying the property string of the OE2DBondDisplay object.

#### See also:

- · OE2DBondDisplay. SetPropertyFont method
- · OE2DBondDisplay. SetProperty method
- OEFont class

## **GetPropertyOffset**

const OE2DPoint &GetPropertyOffset() const

Returns the offset vector (relative to the middle of the bond) that is used to position the property label of the bond. See Figure: The property offset vector is relative to the middle of the displayed bond.

![](_page_122_Figure_11.jpeg)

#### Fig. 10: The property offset vector is relative to the middle of the displayed bond

This allows for any string representable information to be rendered at a logical location near the bond. See example in Example of displaying indices as bond property.

![](_page_122_Figure_14.jpeg)

#### Fig. 11: Example of displaying indices as bond property

- · OE2DBondDisplay. SetPropertyOffset method
- OE2DPoint class

### **HasProperty**

|  | <b>bool</b> HasProperty() const |  |
|--|---------------------------------|--|
|--|---------------------------------|--|

Return whether or not the property string of the OE2DBondDisplay object is empty.

#### See also:

- · OE2DBondDisplay. GetProperty method
- · OE2DBondDisplay. SetProperty method

### **SetBgnPen**

**void** SetBgnPen (const OEPen &pen)

Sets the pen used to draw the bond from the "begin" atom coordinates to the middle of the bond.

#### See also:

- · OE2DBondDisplay.GetBgnPen method
- $\bullet$  OEPen class

## **SetDisplayPos**

void SetDisplayPos (unsigned int pos)

Sets the display position of the bond.

pos This value has to be from the OEBondDisplayPosition namespace.

#### See also:

- · OE2DBondDisplay.GetDisplayPosmethod
- · OEBondDisplayPosition namespace

## **SetDisplayType**

void SetDisplayType (unsigned int type)

Sets the display style of the bond.

type This value has to be from the  $OEBondDisplayType$  namespace.

- · OE2DBondDisplay.GetDisplayType method
- OEBondDisplayType namespace

## **SetEndPen**

void SetEndPen (const OEPen &pen)

Sets the pen used to draw the bond from the "end" atom coordinates to the middle of the bond.

#### See also:

- · OE2DBondDisplay.GetEndPen method
- OEPen class

#### **SetProperty**

void SetProperty (const std:: string & label)

Sets the string displayed next to the bond.

**Warning:** The preferred way to set the bond property strings is to use  $OE2DMolDisplayOptions$ . SetBondPropertyFunctor method. See example in the Displaying Bond Properties section.

#### See also:

- · OE2DBondDisplay. SetProperty method
- · OE2DBondDisplay. SetPropertyFont method
- · OE2DMolDisplayOptions. SetBondPropertyFunctor method

#### **SetPropertyFont**

void SetPropertyFont (const OEFont & font)

Sets the font that is used when displaying the property string of the OE2DBondDisplay object.

**Warning:** The preferred way to set the font of the bond property strings is to use  $OE2DMolDisplayOptions$ . SetBondPropLabelFont method.

- · OE2DBondDisplay.GetPropertyFont method
- · OE2DBondDisplay. GetProperty method
- $\bullet$  *OEFont* class
- · OE2DMolDisplayOptions. SetBondPropLabelFont method

## **SetPropertyOffset**

void SetPropertyOffset (const OE2DPoint& offset)

Sets the offset vector (relative to the middle of the bond) that is used to position the property label of the bond.

#### See also:

- · OE2DBondDisplay.GetPropertyOffset method
- OE2DPoint class

## 4.1.3 OE2DMolDisplay

```
class OE2DMolDisplay : public OEMolDisplayBase
```

This class represents OE2DMolDisplay that stores the depiction information (such as atom coordinates, molecule scaling, representation styles etc.) of a molecule. See Figure: OEDepict TK molecule display class hierarchy.

![](_page_125_Figure_10.jpeg)

### Fig. 12: OEDepict TK molecule display class hierarchy

### See also:

- OE2DMolDisplayOptions class
- OE2DAtomDisplay class
- OE2DBondDisplay class

The following methods are publicly inherited from *OEMolDisplayBase*:

GetDataType GetMolecule IsDataType

## **Constructors**

OE2DMolDisplay (const OEChem:: OEMolBase & mol)

Initializes an *OE2DMolDisplay* object using default display options.

**mol** The molecule for which display information is stored in the OE2DMolDisplay object.

#### See also:

- OE2DMolDisplayOptions. Constructors method for the list of default display options
- · OE2DMolDisplay. IsValid method

OE2DMolDisplay (const OEChem:: OEMolBase &mol, const OE2DMolDisplayOptions &opts)

Initializes an OE2DMolDisplay object using the given display options.

**mol** The molecule for which display information is stored in the OE2DMolDisplay object.

*opts* The  $OE2DMolDisplayOptions object that stores properties that determine the styles of the molecule depiction.$ 

#### **Warning:**

- An OE2DMolDisplay object does not make a copy of the OEMolBase object from which it is initialized but only stores its pointer. Therefore, the user responsibility is to not let the molecule go out of scope, before the corresponding OE2DMolDisplay object.
- Changing the OEMolBase object from which OE2DMolDisplay object is initialized has no effect on the display itself after initialization. However, the OE2DMolDisplay object become invalid if the molecule graph is modified (atoms or bonds added or deleted).

#### Note:

- A warning is thrown when an *OE2DMolDisplay* object is initialized with a molecule with 3D coordinates.
- An OE2DMolDisplay object is considered invalid and an error is thrown when it is initialized:
  - $-$  with an empty molecule (*i.e.* molecule with no atoms)
  - with a molecule that has neither 2D nor 3D coordinates

See also: OE2DMolDisplay. IsValid method

OE2DMolDisplay (const OE2DMolDisplay & rhs)

Copy constructor.

#### operator=

```
OE2DMolDisplay & operator= (const OE2DMolDisplay & rhs)
```

Assignment operator.

#### **CreateCopy**

OESystem:: OEBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OE2DMolDisplay object is dynamically allocated and owned by the caller.

#### **GetAtomDisplay**

OE2DAtomDisplay \*GetAtomDisplay(const OEChem::OEAtomBase \*atom)

Returns the pointer of the OE2DAtomDisplay object that stores the depiction information of the given atom.

const OE2DAtomDisplay \*GetAtomDisplay(const OEChem::OEAtomBase \*atom) const

Returns the const pointer of the OE2DAtomDisplay object that stores the depiction information of the given atom.

**Note:** The OE2DMolDisplay. GetAtomDisplay methods returns a zero pointer if the given atom does not correspond to any display atom stored in the OE2DMolDisplay object. It is a good programming practice to check the returned pointer before using it. See code snippet below.

```
adisp = disp.GetAtomDisplay(atom)if adisp is not None and adisp. IsVisible():
    # do something
    pass
```

#### See also:

• OE2DAtomDisplay class

#### **GetAtomDisplays**

OESystem::OEIterBase<OE2DAtomDisplay> \*GetAtomDisplays() const

Returns an iterator over all *OE2DAtomDisplay* objects stored in the *OE2DMolDisplay* object.

```
OESystem::OEIterBase<OE2DAtomDisplay> *
 GetAtomDisplays(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> &pred) const
```

Returns an iterator over only those OE2DAtomDisplay objects for which the corresponding atom passes the given predicate. For example, the following code snippet shows how to access the atom displays of oxygen atoms:

```
for adisp in disp. GetAtomDisplays (oechem. OEHasAtomicNum (oechem. OEElemNo_0)):
    if adisp. IsVisible():
        # do something
        pass
```

#### See also:

- OE2DAtomDisplay class
- Listing 4 example in the Customizing Molecule Depiction section

#### **GetBondDisplay**

OE2DBondDisplay \*GetBondDisplay(const OEChem::OEBondBase \*bond)

Returns the pointer of the OE2DBondDisplay object, that stores the depiction information of the given bond.

const OE2DBondDisplay \*GetBondDisplay(const OEChem::OEBondBase \*bond) const

Returns the const pointer of the OE2DBondDisplay object, that stores the depiction information of the given bond.

#### See also:

• OE2DBondDisplay class

**Note:** The OE2DMolDisplay. GetBondDisplay methods returns a zero pointer if the given bond does not correspond to any display bond stored in the OE2DMolDisplay object. It is a good programming practice to check the returned pointer before using it. See code snippet below.

```
bdisp = disp.GetBondDisplay(bond)
if bdisp is not None and bdisp. IsVisible():
    # do something
   pass
```

#### See also:

• OE2DBondDisplay class

### **GetBondDisplays**

OESystem::OEIterBase<OE2DBondDisplay> \*GetBondDisplays() const

Returns an iterator over all OE2DBondDisplay objects stored in the OE2DMolDisplay object.

```
OESystem:: OEIterBase<OE2DBondDisplay> *
 GetBondDisplays(const OESystem::OEUnaryPredicate<OEChem::OEBondBase> &pred) const
```

See also:

• OE2DBondDisplay class

Returns an iterator over only those OE2DBondDisplay objects for which the corresponding bond passes the given predicate. For example, the following code snippet shows how to access the bond displays of aromatic bonds:

```
for bdisp in disp.GetBondDisplays(oechem.OEIsAromaticBond()):
   if bdisp.IsVisible():
        # do something
       pass
```

#### See also:

- OE2DBondDisplay class
- Listing 4 example in the Customizing Molecule Depiction section

## **GetDataType**

const void \*GetDataType() const

This function is used to perform run-time type identification.

#### See also:

· OEBase. GetDataType method in the OEChem TK manual

#### **GetHeight**

double GetHeight () const

Returns the height of the displayed molecule.

#### See also:

- Controlling the Size of Depicted Molecules section
- · OE2DMolDisplay. GetScale method
- · OE2DMolDisplay. GetWidth method

### **GetLayer**

```
OEImage &GetLayer (unsigned int position, unsigned int idx=0)
const OEImage &GetLayer (unsigned int position, unsigned int idx=0) const
```

Provides access to the layers of the OE2DMolDisplay object. Currently, an OE2DMolDisplay object has two layers (one OELayerPosition\_Above and one OELayerPosition\_Below) that allows drawing of objects over or underneath the molecular structure, respectively.

*position* This value has to be from the OELayerPosition namespace.

idx This parameter is currently not used.

- OEImage class
- · OELayerPosition namespace

## **GetOptions**

const OE2DMolDisplayOptions &GetOptions () const

Returns the options used to initialized the OE2DMolDisplay object.

#### See also:

• OE2DMolDisplayOptions class

### **GetScale**

double GetScale() const

Returns the scaling factor of the displayed molecule.

#### See also:

- Controlling the Size of Depicted Molecules section
- · OE2DMolDisplay.GetHeight method
- · OE2DMolDisplay. GetWidth method

## **GetWidth**

double GetWidth() const

Returns the width of the displayed molecule.

#### See also:

- Controlling the Size of Depicted Molecules section
- · OE2DMolDisplay.GetHeight method
- · OE2DMolDisplay.GetScale method

## **IsDataType**

bool IsDataType (const void \*) const

Returns whether type is the same as the instance this method is called on.

#### See also:

· OEBase. IsDataType method in the OEChem TK manual

**IsValid** 

bool IsValid() const

Returns whether the OE2DMolDisplay object was initialized successfully. If initialization was attempted with an empty molecule or a molecule with no coordinates (neither 2D nor 3D), then this method returns false. An OE2DMolDisplay object becomes invalid if the molecule, from which it was initialized, is modified. For example, atom or bonds added to or deleted from the molecule.

**Hint:** It is highly recommend to check whether a molecule display is valid after initialization.

## 4.1.4 OE2DMolDisplayOptions

class OE2DMolDisplayOptions

This class represents the OE2DMolDisplayOptions class that encapsulates properties that determine how a molecule is depicted.

The OE2DMolDisplayOptions class stores the following properties:

| Property                       | Get method                          | Set method                          | Corresponding namespace / class / type                           |
|--------------------------------|-------------------------------------|-------------------------------------|------------------------------------------------------------------|
| aromatic style                 | <i>GetAromaticStyle</i>             | <i>SetAromaticStyle</i>             | OEAromaticStyle                                                  |
| atomic number colors           | <i>GetAtomColor</i>                 | <i>SetAtomColor</i>                 | OEColor                                                          |
| atom color style               | <i>GetAtomColorStyle</i>            | <i>SetAtomColorStyle</i>            | OEAtomColorStyle                                                 |
| atom label font                | <i>GetAtomLabelFont</i>             | <i>SetAtomLabelFont</i>             | OEFont                                                           |
| atom label font scale          | <i>GetAtomLabelFontScale</i>        | <i>SetAtomLabelFontScale</i>        | positive floating point number in the range of [0.5, 3.0] or 0.0 |
| atom property font             | <i>GetAtomPropLabelFont</i>         | <i>SetAtomPropLabelFont</i>         | OEFont                                                           |
| atom property label font scale | <i>GetAtomPropLabelFontScale</i>    | <i>SetAtomPropLabelFontScale</i>    | positive floating point number in the range of [0.5, 2.0]        |
| atom property initializer      | <i>GetAtomPropertyFunctor</i>       | <i>SetAtomPropertyFunctor</i>       | OEHDisplayAtomPropBase                                           |
| atom stereo style              | <i>GetAtomStereoStyle</i>           | <i>SetAtomStereoStyle</i>           | OEAtomStereoStyle                                                |
| atom SVG markup                | <i>GetAtomSVGMarkupFunc</i>         | <i>SetAtomSVGMarkupFunc</i>         | OEAtomSVGMarkupBase                                              |
| atom visibility initializer    | <i>GetAtomVisibilityFunc</i>        | <i>SetAtomVisibilityFunc</i>        | OEUnaryAtomPred                                                  |
| background color               | <i>GetBackgroundColor</i>           | <i>SetBackgroundColor</i>           | OEColor                                                          |
| bond color style               | <i>GetBondColorStyle</i>            | <i>SetBondColorStyle</i>            | OEBondColorStyle                                                 |
| bond line gap scale            | <i>GetBondLineGapScale</i>          | <i>SetBondLineGapScale</i>          | positive floating point number in the range of [0.5, 2.0]        |
| bond line atom label gap scale | <i>GetBondLineAtomLabelGapScale</i> | <i>SetBondLineAtomLabelGapScale</i> | positive floating point number in the range of [0.5, 2.0]        |
| bond property font             | <i>GetBondPropLabelFont</i>         | <i>SetBondPropLabelFont</i>         | OEFont                                                           |
| bond property label font scale | <i>GetBondPropLabelFontScale</i>    | <i>SetBondPropLabelFontScale</i>    | positive floating point number in the range of [0.5, 2.0]        |
| bond property initializer      | <i>GetBondPropertyFunctor</i>       | <i>SetBondPropertyFunctor</i>       | OEHDisplayBondPropBase                                           |
| bond stereo style              | <i>GetBondStereoStyle</i>           | <i>SetBondStereoStyle</i>           | OEBondStereoStyle                                                |
| bond pen                       | <i>GetDefaultBondPen</i>            | <i>SetDefaultBondPen</i>            | OEPen                                                            |

| Property                       | Get method                  | Set method                  | Corresponding namespace / class / type                           |
|--------------------------------|-----------------------------|-----------------------------|------------------------------------------------------------------|
| bond width scaling             | GetBondWidthScaling         | SetBondWidthScaling         | boolean                                                          |
| bond SVG markup                | GetBondSVGMarkup            | SetBondSVGMarkup            | OEBondSVGMarkupBase                                              |
| explicit atom label angle      | GetExplicitAtomLabelAngle   | SetExplicitAtomLabelAngle   | positive floating point number in the range of [120.0, 180.0]    |
| height                         | GetHeight                   | SetHeight                   | positive floating point number                                   |
| hydrogen style                 | GetHydrogenStyle            | SetHydrogenStyle            | OEHydrogenStyle                                                  |
| margin(s)                      | GetMargin                   | SetMargin, SetMargins       | positive floating point number in the range of [2.5, 25.0]       |
| scale                          | GetScale                    | SetScale                    | positive floating point number                                   |
| super atom label font          | GetSuperAtomLabelFont       | SetSuperAtomLabelFont       | OEFont                                                           |
| super atom display style       | GetSuperAtomStyle           | SetSuperAtomStyle           | OESuperAtomStyle                                                 |
| protective group label font    | GetProtectiveGroupLabelFont | SetProtectiveGroupLabelFont | OEFont                                                           |
| protective group display style | HasProtectiveGroupStyle     | SetProtectiveGroupStyle     | OEProtectiveGroupStyle                                           |
| title font                     | GetTitleFont                | SetTitleFont                | OEFont                                                           |
| title font scale               | GetTitleFontScale           | SetTitleFontScale           | positive floating point number in the range of [0.5, 2.0] or 0.0 |
| title height                   | GetTitleHeight              | SetTitleHeight              | positive floating point number                                   |
| title location                 | GetTitleLocation            | SetTitleLocation            | OETitleLocation                                                  |
| width                          | GetWidth                    | SetWidth                    | positive floating point number                                   |

|  | Table $1$ – continued from previous page |  |  |  |
|--|------------------------------------------|--|--|--|
|--|------------------------------------------|--|--|--|

The images below illustrate the three possible molecule display layouts depending on the position of the title. These layouts can be controlled by the following parameters:

- The width and the height can be set either by the constructor of the OE2DMolDisplayOptions class, by calling the OE2DMolDisplayOptions. SetDimensions method or by the SetWidth and SetHeight methods, respectively.
- The location of the title area (blue box) can be set by the  $SetTitleLocation$  method. The height of the title area (blue arrows) can be modified by invoking the  $SetTitleHeight$  method.
- The padding around the molecule (red arrows) can be changed by calling either the  $SetMargin$  or the SetMargins methods.

![](_page_132_Figure_7.jpeg)

#### Table 2: Example of molecule display layouts depending on position of the title

- OE2DMolDisplay class
- Controlling the Size of Depicted Molecules section

Hint: Even though OEDepict TK provides access to manipulate the properties of the atom and bond displays after the OE2DMolDisplay object is constructed, it is highly recommended to determine the style of the depiction by using the OE2DMolDisplayOptions class. Only by knowing all properties (such as labels, font styles and sizes etc.) in advance can ensure the **best depiction layout** *i.e.* that the molecule diagram is rendered without any label clippings and the labels are displayed with the minimum number of overlaps.

## **Constructors**

OE2DMolDisplayOptions()

Default constructor that initializes an OE2DMolDisplayOptions object with the following properties:

See example in Molecule depiction with default options)

### Table 3: Default parameters of OE2DMolDisplayOptions

| Property                       | Default value                                                                                             |
|--------------------------------|-----------------------------------------------------------------------------------------------------------|
| aromatic style                 | OEAromaticStyle_Default                                                                                   |
| atomic number colors           | initialized based on OEAtomColorStyle_Default                                                             |
| atom color style               | OEAtomColorStyle_Default                                                                                  |
| atom label font                | OEDepict_OEDefaultFont                                                                                    |
| atom label font scale          | 1.0                                                                                                       |
| atom property font             | OEFont(OEColor(75, 75, 75))                                                                               |
| atom property label font scale | 1.0                                                                                                       |
| atom property initializer      | OEDisplayNoAtomProp                                                                                       |
| atom stereo style              | OEAtomStereoStyle_Default                                                                                 |
| atom SVG markup                | OEAtomSVGNoMarkup                                                                                         |
| atom visibility initializer    | OEIsTrueAtom                                                                                              |
| background color               | OEDepict_OELightBackgroundColor initialized based on OEAtomColorStyle_Default                             |
| bond color style               | OEBondColorStyle_Default                                                                                  |
| bond line gap scale            | 1.0                                                                                                       |
| bond line atom label gap scale | 1.0                                                                                                       |
| bond property font             | OEFont(OEColor(75, 75, 75))                                                                               |
| bond property label font scale | 1.0                                                                                                       |
| bond property initializer      | OEDisplayNoBondProp                                                                                       |
| bond stereo style              | OEBondStereoStyle_Default                                                                                 |
| bond pen                       | OEDepict_OEBlackPen                                                                                       |
| bond width scaling             | false                                                                                                     |
| bond SVG markup                | OEBondSVGNoMarkup                                                                                         |
| explicit atom label angle      | 170.0 (degree)                                                                                            |
| height                         | 0.0 (initialized based on scale)                                                                          |
| hydrogen style                 | OEHydrogenStyle_Default                                                                                   |
| margins                        | left and right margin 5.0% of the width; top and bottom margin 5.0% of the height of the molecule display |
| scale                          | OEScale_AutoScale                                                                                         |

| Property                       | Default value                             |
|--------------------------------|-------------------------------------------|
| super atom display style       | OESuperAtomStyle_Default                  |
| protective group label font    | OEFont(OEPink)                            |
| protective group display style | OEProtectiveGroupStyle_Default            |
| title font                     | OEDepict_OEDefaultFont                    |
| title font scale               | 1.0                                       |
| title location                 | OETitleLocation_Default                   |
| title height                   | 10% of the height of the molecule display |
| width                          | 0.0 (initialized based on scale)          |

Table 3 - continued from previous page

![](_page_134_Figure_3.jpeg)

Fig. 13: Molecule depiction with default options

OE2DMolDisplayOptions (double scale)

Creates an OE2DMolDisplayOptions object with the specified scaling.

scale A non-negative number that controls the magnification of the depicted molecule.

OE2DMolDisplayOptions (double width, double height, double scale)

Creates an OE2DMolDisplayOptions object with the specified dimension and scaling.

OE2DMolDisplayOptions (const OE2DMolDisplayOptions & rhs)

Copy constructor.

#### operator=

OE2DMolDisplayOptions & operator=(const OE2DMolDisplayOptions & rhs)

Assignment operator.

#### **GetAromaticStvle**

unsigned int GetAromaticStyle() const

Returns the style that controls how aromatic rings are displayed. The return value is taken from the OEAromaticStyle namespace.

#### See also:

- · OE2DMolDisplayOptions. SetAromaticStyle method
- · OEAromaticStyle namespace

#### **GetAtomSVGMarkupFunctor**

const OEAtomSVGMarkupBase &GetAtomSVGMarkupFunctor () const

Returns the functor that defines how atoms are marked in svg image. By default, residues are not marked (OEAtomSVGNoMarkup).

#### See also:

· OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method

#### **GetAtomColor**

const OESystem:: OEColor &GetAtomColor (unsigned int atomic) const

Returns the color associated with a specific atomic number.

#### See also:

- OE2DMolDisplayOptions. SetAtomColor method
- OEColor class
- Appendix: Element coloring (CPK) section

#### **GetAtomColorStyle**

unsigned int GetAtomColorStyle() const

Returns the style that is used to define the color of the background and the default color of atom labels. The return value is taken from the OEAtomColorStyle namespace.

- · OE2DMolDisplayOptions. SetAtomColorStyle method
- · OEAtomColorStyle namespace

## **GetAtomLabelFont**

```
const OEFont &GetAtomLabelFont () const
```

Returns the font that is used to initialize the depiction style of the atom labels (OE2DAtomDisplay. GetLabelFont).

See also:

- · OE2DMolDisplayOptions. SetAtomLabelFont method
- · OE2DMolDisplayOptions. SetAtomLabelFontScale method
- OEFont class

#### **GetAtomLabelFontScale**

double GetAtomLabelFontScale() const

Returns the multiplier that can be used to increase or decrease the size of the atom label fonts.

#### See also:

- · OE2DMolDisplayOptions. SetAtomLabelFont method
- · OE2DMolDisplayOptions. SetAtomLabelFontScale method

#### **GetAtomPropLabelFont**

const OEFont & GetAtomPropLabelFont () const

Returns the font that is used to initialize the depiction style of the atom property labels (OE2DAt  $\sigma mD$ isplay. GetPropertyFont).

See also:

- · OE2DMolDisplayOptions. SetAtomPropLabelFont method
- OEFont class

#### **GetAtomPropLabelFontScale**

double GetAtomPropLabelFontScale() const

Returns the multiplier that can be used to increase or decrease the size of the atom property label fonts.

- · OE2DMolDisplayOptions. SetAtomPropLabelFont method
- · OE2DMolDisplayOptions. SetAtomPropLabelFontScale method

### **GetAtomPropertyFunctor**

const OEDisplayAtomPropBase &GetAtomPropertyFunctor() const

Returns the functor that is used to initialize the atom property labels (OE2DAt omDisplay. GetProperty).

#### See also:

- · OE2DMolDisplayOptions. SetAtomPropertyFunctor method
- OEDisplayAtomPropBase class
- OEDisplayAtomIdx class
- OEDisplayAtomMapIdx class
- OEDisplayNoAtomProp class

#### **GetAtomVisibilityFunctor**

const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> &GetAtomVisibilityFunctor() const

Returns the functor that is used to identify visible atoms. The default functor is the OEIsTrueAtom class which results in all atoms being displayed.

#### See also:

- · OE2DMolDisplayOptions. SetAtomVisibilityFunctor method
- · OEUnaryAtomPred

#### **GetAtomStereoStyle**

unsigned int GetAtomStereoStyle() const

Returns the style that controls what atom stereo information is displayed. The return value is taken from the OEAtomStereoStylenamespace.

#### See also:

- · OE2DMolDisplayOptions. SetAtomStereoStyle method
- · OEAtomStereoStyle namespace

### **GetBackgroundColor**

const OESystem:: OEColor & GetBackgroundColor() const

Returns the color that is used to clear the background of an image (by calling  $OEImageBase$ . Clear method) before rendering the molecule.

- · OE2DMolDisplayOptions. SetBackgroundColor method
- OEColor class
- OERenderMolecule function

### **GetBondColorStyle**

unsigned int GetBondColorStyle() const

Returns the style that controls how bonds are colored. The return value is taken from the OEBondColorStyle namespace.

#### See also:

- · OE2DMolDisplayOptions. SetBondColorStyle method
- · OEBondColorStyle namespace

#### **GetBondLineGapScale**

double GetBondLineGapScale() const

Returns the multiplier that can be used to increase or decrease the gap between the lines of double and triple bonds.

#### See also:

· OE2DMolDisplayOptions. SetBondLineGapScale method

### GetBondLineAtomLabelGapScale

double GetBondLineAtomLabelGapScale() constant

Returns the multiplier that can be used to increase or decrease the gap between the line(s) of bonds and the adjacent atom labels.

#### See also:

· OE2DMolDisplayOptions. SetBondLineAtomLabelGapScale method

### **GetBondPropLabelFont**

const OEFont & GetBondPropLabelFont () const

Returns the font that is used to initialize the depiction style of the bond property labels (OE2DBondDisplay. GetPropertyFont).

- · OE2DMolDisplayOptions. SetBondPropLabelFont method
- OEFont class

#### **GetBondPropLabelFontScale**

double GetBondPropLabelFontScale() const

Returns the multiplier that can be used to increase or decrease the size of the bond property label fonts.

#### See also:

- · OE2DMolDisplayOptions. SetBondPropLabelFont method
- · OE2DMolDisplayOptions. SetBondPropLabelFontScale method

#### **GetBondPropertyFunctor**

const OEDisplayBondPropBase &GetBondPropertyFunctor () const

Returns the functor that is used to initialize the bond property labels (OE2DBondDisplay. GetProperty).

#### See also:

- · OE2DMolDisplayOptions. SetBondPropertyFunctor method
- OEDisplayBondPropBase class
- OEDisplayBondIdx class
- OEDisplayNoBondProp class

#### **GetBondStereoStyle**

unsigned int GetBondStereoStyle() const

Returns the style that controls what bond stereo information is displayed. The return value is taken from the OEBondStereoStyle namespace.

#### See also:

- OE2DMolDisplayOptions. SetBondStereoStyle method
- · OEBondStereoStyle namespace

#### **GetBondSVGMarkupFunctor**

const OEBondSVGMarkupBase &GetBondSVGMarkupFunctor () const

Returns the functor that defines how bonds are marked in  $svg$  image. By default, residues are not marked (OE-BondSVGNoMarkup).

#### See also:

· OE2DMolDisplayOptions. SetBondSVGMarkupFunctor method

### **GetBondWidthScaling**

**bool** GetBondWidthScaling() const

Returns whether the line width of the bond are increase or decreased based on the molecule scaling factor (OE2DMolDisplayOptions.GetScale)

### See also:

· OE2DMolDisplayOptions. SetBondWidthScaling method

## **GetDefaultBondPen**

const OEPen & GetDefaultBondPen() const

Returns the pen that is used to initialize the bond pens (OE2DBondDisplay.GetBgnPen and OE2DBondDisplay.GetBgnPen).

#### See also:

- · OE2DMolDisplayOptions. SetDefaultBondPen method
- $\bullet$  OEPen class

### **GetExplicitAtomLabelAngle**

double GetExplicitAtomLabelAngle() const

In the case of an almost linear X-C-X bond, an explicit "C" label will be drawn if the angle is more that the returned value of this function. 180.0 degree means that the "C" label will never be drawn.

#### See also:

· OE2DMolDisplayOptions. SetExplicitAtomLabelAngle method

### **GetHeight**

double GetHeight () const

Returns the vertical limit into which the molecule has to be fitted.

- · OE2DMolDisplayOptions. SetDimensions method
- · OE2DMolDisplayOptions. SetHeight method

#### **GetHydrogenStyle**

unsigned int GetHydrogenStyle() const

Returns the style that controls of how implicit and explicit hydrogens are displayed. The return value is taken from the OEHydrogenStyle namespace.

#### See also:

- · OE2DMolDisplayOptions. SetHydrogenStyle method
- · OEHydrogenStyle namespace

#### **GetMargin**

double GetMargin (unsigned int margin) const

Returns the ratio of a specific margin of the OE2DMolDisplayOptions object.

margin This value has to be from the OEMargin namespace.

#### See also:

- · OE2DMolDisplayOptions. SetMargin method
- · OE2DMolDisplayOptions. SetMargins method
- · OEMargin namespace

### **GetProtectiveGroupLabelFont**

const OEFont &GetProtectiveGroupLabelFont () const

Returns the font that is used to display the protective group labels.

#### See also:

- · OE2DMolDisplayOptions. SetProtectiveGroupLabelFont method
- · OE2DMolDisplayOptions. SetProtectiveGroupStyle method
- · OE2DMolDisplayOptions. SetSuperAtomStyle method
- OEFont class

### **GetProtectiveGroupStyle**

unsigned int GetProtectiveGroupStyle() const

Returns the style that controls whether or not specific pre-defined protective group are contracted and labeled with corresponding abbreviations. The return value is taken from the OEP rotective GroupStyle namespace.

- · OE2DMolDisplayOptions. HasProtectiveGroupStyle method
- · OE2DMolDisplayOptions. SetProtectiveGroupStyle method
- OE2DMolDisplayOptions. SetProtectiveGroupLabelFont method

- OE2DMolDisplayOptions. SetSuperAtomStyle method
- · OESuperAtomStyle namespace

**Warning:** This is a deprecated API. Please use OE2DMolDisplayOptions. HasProtectiveGroupStyle to determine which protective groups are set.

#### **GetScale**

double GetScale() const

Returns the scaling factor used to magnify a molecule.

#### See also:

- · OE2DMolDisplayOptions. SetDimensions method
- · OE2DMolDisplayOptions. SetScale method

#### **GetSuperAtomLabelFont**

const OEFont & GetSuperAtomLabelFont () const

Returns the font that is used to display the abbreviations of contracted functional groups.

#### See also:

- · OE2DMolDisplayOptions. SetSuperAtomLabelFont method
- · OE2DMolDisplayOptions. SetSuperAtomStyle method
- · OE2DMolDisplayOptions. SetProtectiveGroupStyle method
- OEFont class

#### **GetSuperAtomStyle**

unsigned int GetSuperAtomStyle() const

Returns the style that controls whether or not specific pre-defined functional groups are contracted and labeled with corresponding abbreviations. The return value is taken from the OESuperAtomStyle namespace.

- · OE2DMolDisplayOptions. SetSuperAtomStyle method
- OE2DMolDisplayOptions. SetSuperAtomLabelFont method
- · OE2DMolDisplayOptions. SetProtectiveGroupStyle method
- · OESuperAtomStyle namespace

## **GetTitleFont**

Returns the font that is used to display the title of the molecule *(i.e.* the string returned by the  $OEMOIBase$ . GetTitle method).

const OEFont & GetTitleFont () const

### See also:

- · OE2DMolDisplayOptions. SetTitleFont method
- · OE2DMolDisplayOptions. SetTitleFontScale method
- OEFont class

## **GetTitleFontScale**

Returns the multiplier that can be used to increase or decrease the size of the title font.

double GetTitleFontScale() const

#### See also:

- · OE2DMolDisplayOptions. SetTitleFontScale method
- · OE2DMolDisplayOptions. SetTitleFont method

## **GetTitleLocation**

unsigned int GetTitleLocation() const

Returns the position of the molecule title. The return value is taken from the  $OETitleLocation$  namespace.

#### See also:

- · OE2DMolDisplayOptions. SetTitleLocation method
- · OETitleLocation namespace

## **GetTitleHeight**

double GetTitleHeight() const

Returns the height of the title area.

#### See also:

· OE2DMolDisplayOptions. SetTitleHeight method

## **GetWidth**

double GetWidth() const

Returns the horizontal limit into which the molecule has to be fitted.

#### See also:

- · OE2DMolDisplayOptions. SetDimensions method
- · OE2DMolDisplayOptions. SetWidth method

### **HasProtectiveGroupStyle**

**bool** HasProtectiveGroupStyle (unsigned int style)

Returns true if the specific pre-defined protective group style is contracted and labeled with corresponding abbreviations.

style This value has to be from the OEP rotective GroupStyle namespace.

### **SetAromaticStyle**

void SetAromaticStyle (unsigned int style)

Sets the style that controls how aromatic rings are displayed.

style This value has to be from the OEAromaticStyle namespace.

**Example:** (Figure: Example of using the SetAromaticStyle method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetAromaticStyle(oedepict.OEAromaticStyle_Circle)
```

![](_page_144_Figure_17.jpeg)

![](_page_144_Figure_18.jpeg)

Fig. 14: Example of using the SetAromaticStyle method

- OE2DMolDisplayOptions. GetAromaticStyle method
- · OEAromaticStyle namespace

#### **SetAtomColor**

void SetAtomColor (unsigned int atomic, const OESystem:: OEColor &color)

Sets the color associated with a specific atomic number.

atomic This value has to be from the OEE1emNo namespace of OEChem TK.

*color* The color being associated with the given atomic number.

**Example:** (Figure: Example of using the SetAtomColor method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetAtomColor(oechem.OEElemNo_O, oechem.OEColor(80, 0, 0)) # very dark red
opts.SetAtomColor(oechem.OEElemNo_N, oechem.OEColor(0, 0, 80)) # very dark blue
```

![](_page_145_Figure_10.jpeg)

Fig. 15: Example of using the SetAtomColor method

#### See also:

- · OE2DMolDisplayOptions.GetAtomColor method
- OEColor class
- Appendix: Element coloring (CPK) section

#### Note:

- The color of the atom also depends on the atom color style  $(OE2DMOLDisplayOptions$ . GetAtomColorStyle).
- Setting atom color style (OE2DMolDisplayOptions. SetAtomColorStyle) to WhiteMonochrome sets white background and black color for all atoms. Likewise, setting atom color style to BlackMonochrome sets black background and white color for all atoms. But, user can choose to have another color for

all atoms (in monochrome atom color style) by setting another atom color ( $OE2DM01DisplavOptions$ . Set AtomColor) for Carbon atoms. The example in Listing 4 demonstrates setting non-default atom colors in monochrome mode. Setting atom color for other than Carbon atoms sets color of only specified atom types, not for all atoms.

### **SetAtomColorStyle**

void SetAtomColorStyle (unsigned int style)

Sets the style that is used to define the color of the background and the default color of atom labels.

style This value has to be from the  $OEAtomColorStyle$  namespace.

**Example:** (Figure: Example of using the SetAtomColorStyle method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetAtomColorStyle(oedepict.OEAtomColorStyle BlackMonochrome)
```

![](_page_146_Figure_8.jpeg)

Fig. 16: Example of using the SetAtomColorStyle method

- · OE2DMolDisplayOptions.GetAtomColorStyle method
- · OEAtomColorStyle namespace

### **SetAtomLabelFont**

```
void SetAtomLabelFont (const OEFont & font)
```

Sets the font that is used to initialize the depiction style of the atom labels ( $OE2DAtomDisplay$ ,  $GetLabelFont$ ).

**Example:** (Figure: Example of using the SetAtomLabelFont method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
font = <code>oedepict.OEFont()</code>font.SetFamily(oedepict.OEFontFamily_Courier)
font.SetStyle(oedepict.OEFontStyle_Bold)
opts.SetAtomLabelFont(font)
```

![](_page_147_Figure_6.jpeg)

Fig. 17: Example of using the SetAtomLabelFont method

#### Note:

- The color of the atom label fonts also depends on the atom color style  $(\text{OE2DMolDisplayOptions.})$ GetAtomColorStyle).
- The size of fonts of the atom labels also depends on:
  - the scaling factor used to fit a molecule to a given dimension  $(OE2DMOLDisplayOptions$ . GetScale)
  - the multiplier set by the OE2DMolDisplayOptions. SetAtomLabelFontScale method

See example in Figure: Example of scaling the font of the atom label along with the molecule

- · OE2DMolDisplayOptions.GetAtomLabelFont method
- OEFont class

![](_page_148_Figure_1.jpeg)

Fig. 18: Example of scaling the font of the atom label along with the molecule

### **SetAtomLabelFontScale**

void SetAtomLabelFontScale (double scale)

Sets the multiplier that can be used increase or decrease the size of the fonts of the atom labels.

scale This value has to be either 0.0 or in a range of [0.5, 3.0]. See examples in Figure: Examples of scaling the font of the atom label relative to the molecule

In case of  $0.0$ , the atom labels are not scaled with the molecule but rather fixed font size are used regardless of the size of the molecule. See example in Figure: Example of atom labels with fixed font size

![](_page_148_Figure_8.jpeg)

Fig. 19: Examples of scaling the font of the atom label relative to the molecule

**Example:** (Figure: Example of using the SetAtomLabelFontScale method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetAtomLabelFontScale(1.5)
```

See also:

· OE2DMolDisplayOptions.GetAtomLabelFontScale method

![](_page_149_Figure_1.jpeg)

Fig. 20: Example of atom labels with fixed font size

![](_page_149_Figure_3.jpeg)

Fig. 21: Example of using the SetAtomLabelFontScale method

### **SetAtomPropLabelFont**

void SetAtomPropLabelFont (const OEFont &font)

Sets the font that is used to initialize the depiction style of the atom property labels (OE2DAtomDisplay. GetPropertyFont).

**Example:** (Figure: Example of using the SetAtomPropLabelFont method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
font = oedepict.OEFont()
font.SetStyle(oedepict.OEFontStyle_Bold)
font.SetColor(oechem.OEDarkGreen)
opts.SetAtomPropLabelFont(font)
opts.SetAtomPropertyFunctor(oedepict.OEDisplayAtomIdx())
```

Note:

![](_page_150_Figure_1.jpeg)

Fig. 22: Example of using the SetAtomPropLabelFont method

· The size of the atom property label fonts also depends on the scaling factor used to fit a molecule to a given dimension (OE2DMolDisplayOptions. GetScale) and the multiplier set by the OE2DMolDisplayOptions. SetAtomPropLabelFontScale method. See example in Figure: Example of scaling the font of the atom property labels along with the molecule

![](_page_150_Figure_4.jpeg)

Fig. 23: Example of scaling the font of the atom property labels along with the molecule

- · OE2DMolDisplayOptions.GetAtomPropLabelFont method
- OEFont class

### **SetAtomPropLabelFontScale**

void SetAtomPropLabelFontScale(double scale)

Sets the multiplier that can be used increase or decrease the size of the fonts of the atom property labels.

scale This value has to be in the range of  $[0.5, 2.0]$ . See examples in Figure: Examples of scaling the font of the atom property labels relative to the molecule

![](_page_151_Figure_5.jpeg)

![](_page_151_Figure_6.jpeg)

**Example:** (Figure: Example of using the SetAtomPropLabelFontScale method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetAtomPropLabelFontScale(1.5)
opts.SetAtomPropertyFunctor(oedepict.OEDisplayAtomIdx())
```

![](_page_151_Figure_9.jpeg)

Fig. 25: Example of using the SetAtomPropLabelFontScale method

### See also:

· OE2DMolDisplayOptions.GetAtomPropLabelFontScale method

## **SetAtomPropertyFunctor**

void SetAtomPropertyFunctor (const OEDisplayAtomPropBase & func)

Sets the functor that is used to initialize the atom property labels (OE2DAt  $\text{onDisplay}.$  Get Property)

**Example:** (Figure: Example of using the SetAtomPropertyFunctor method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetAtomPropertyFunctor(oedepict.OEDisplayAtomIdx())
```

![](_page_152_Figure_6.jpeg)

Fig. 26: Example of using the SetAtomPropertyFunctor method

Hint: It is recommended to use the OE2DMolDisplayOptions. SetAtomPropertyFunctor method to define the atom property labels when the OE2DMolDisplay object is constructed. All labels displayed on the molecule diagram have to be known in advance in order to be able to minimize the number of label clashes and clippings when calculating the positions of the bond property labels.

See example of user-defined atom properties in Displaying Atom Properties section.

- OE2DMolDisplayOptions. GetAtomPropertyFunctor method
- OEDisplayAtomPropBase class
- OEDisplayAtomIdx class
- OEDisplayAtomMapIdx class
- OEDisplayNoAtomProp class

### **SetAtomStereoStvle**

void SetAtomStereoStyle (unsigned int style)

Sets the style that controls what atom stereo information is displayed.

style This value has to be from the OEAtomStereoStyle namespace.

**Example:** (Figure: Example of using the SetAtomStereoStyle method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetAtomStereoStyle(oedepict.OEAtomStereoStyle_Display_All |
                        oedepict.OEAtomStereoStyle_HashWedgeStyle_Standard)
```

![](_page_153_Figure_7.jpeg)

![](_page_153_Figure_8.jpeg)

Fig. 27: Example of using the SetAtomStereoStyle method

#### See also:

- · OE2DMolDisplayOptions.GetAtomStereoStyle method
- · OEAtomStereoStyle namespace

#### **SetAtomSVGMarkupFunctor**

void SetAtomSVGMarkupFunctor (const OEAtomSVGMarkupBase & func)

Sets the functor that defines how atoms are marked in svg image. Drawing elements representing atoms in svg image are grouped together in the following format in which the <group id> and <class name> strings are defined by the given functor:

```
<g id='<group id>' class='<class name>'>
list of drawing elements
\ddot{\phantom{a}}\mathord{<}/\,g\mathord{>}
```

Note: This setting has only effect when generating . svg images.

#### See also:

- OEAtomSVGMarkupBase abstract base class
- OEAtomSVGNoMarkup class
- OEAtomSVGAtomIdxMarkup class
- OEAtomSVGResidueMarkup class
- · OE2DMolDisplayOptions. GetAtomSVGMarkupFunctor method

### **SetAtomVisibilityFunctor**

```
void SetAtomVisibilityFunctor (const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> &
\rightarrowfunc)
```

Sets the functor that is used to identify visible atoms.

**Example:** (Figure: Example of using the SetAtomVisibilityFunctor method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetAtomVisibilityFunctor(oechem.OEAtomIsInRing())
```

![](_page_154_Figure_13.jpeg)

Fig. 28: Example of using the SetAtomVisibilityFunctor method to only display rings

Hint: It is recommended to use the OE2DMolDisplayOptions. SetAtomVisibilityFunctor method to identify the visible atoms when the OE2DMolDisplay object is constructed. All objects displayed in the molecule diagram have to be known in advance in order to be able to correctly size and scale the molecule.

See additional examples of atom visibility control in the Displaying Atom Properties section.

- · OE2DMolDisplayOptions.GetAtomVisibilityFunctor method
- · OEUnaryAtomPred

#### SetBackgroundColor

void SetBackgroundColor (const OESystem:: OEColor &color)

Sets the color that is used to clear the background of an image (by calling OEImageBase. Clear method) before rendering the molecule.

**Example:** (Figure: Example of using the SetBackgroundColor method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetBackgroundColor(oechem.OEYellowTint)
```

![](_page_155_Figure_8.jpeg)

Fig. 29: Example of using the SetBackgroundColor method

### See also:

- · OE2DMolDisplayOptions.GetBackgroundColor method
- OEColor class

#### **SetBondColorStyle**

void SetBondColorStyle (unsigned int style)

Sets the style that controls how bonds are colored.

style This value has to be from the OEBondColorStyle namespace.

**Example:** (Figure: Example of using the SetBondColorStyle method)

![](_page_156_Figure_1.jpeg)

#### Fig. 30: Example of using the SetBondColorStyle method

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetBondColorStyle(oedepict.OEBondColorStyle_Monochrome)
```

#### See also:

- · OE2DMolDisplayOptions.GetBondColorStyle method
- · OEBondColorStyle namespace

#### **SetBondLineGapScale**

void SetBondLineGapScale (double scale)

Sets the multiplier that can be used increase or decrease the gap between the lines of double and triple bonds.

scale This value has to be in the range of [0.5, 2.0]. See examples in Figure: Examples of altering the gap between the lines of double and triple bonds

**Example:** (Figure: Example of using the SetBondLineGapScale method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetBondLineGapScale(0.5)
```

#### See also:

· OE2DMolDisplayOptions.GetBondLineGapScalemethod

![](_page_157_Figure_1.jpeg)

Fig. 31: Examples of altering the gap between the lines of double and triple bonds

![](_page_157_Figure_3.jpeg)

Fig. 32: Example of using the SetBondLineGapScale method

#### SetBondLineAtomLabelGapScale

void SetBondLineAtomLabelGapScale(double scale)

Sets the multiplier that can be used to increase or decrease the gap between the line(s) of bonds and the adjacent atom labels.

scale This value has to be in the range of [0.5, 2.0]. See examples in Figure: Examples of altering the gap between the line( $s$ ) of bonds and adjacent atom labels

**Example:** (Figure: Example of using the SetBondLineAtomLabelGapScale method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetBondLineAtomLabelGapScale(2.0)
```

See also:

· OE2DMolDisplayOptions.GetBondLineAtomLabelGapScale method

![](_page_158_Figure_1.jpeg)

Fig. 33: Examples of altering the gap between the line(s) of bonds and adjacent atom labels

![](_page_158_Figure_3.jpeg)

Fig. 34: Example of using the SetBondLineAtomLabelGapScale method

### **SetBondPropLabelFont**

void SetBondPropLabelFont (const OEFont &color)

Sets the font that is used to initialize the depiction style of the bond property labels (OE2DBondDisplay. GetPropertyFont).

**Example:** (Figure: Example of using the SetBondPropLabelFont method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
font = oedepict.OEFont()
font.SetStyle(oedepict.OEFontStyle_Bold)
font.SetColor(oechem.OEDarkGreen)
opts.SetBondPropLabelFont(font)
opts.SetBondPropertyFunctor(oedepict.OEDisplayBondIdx())
```

Note:

![](_page_159_Figure_1.jpeg)

![](_page_159_Figure_2.jpeg)

Fig. 35: Example of using the SetBondPropLabelFont method

· The size of the bond property label fonts also depends on the scaling factor used to fit a molecule to a given dimension (OE2DMolDisplayOptions. GetScale) and the multiplier set by the OE2DMolDisplayOptions. SetBondPropLabelFontScale method. See example in Figure: Example of scaling the font of the bond property labels along with the molecule

![](_page_159_Figure_5.jpeg)

Fig. 36: Example of scaling the font of the bond property labels along with the molecule

- · OE2DMolDisplayOptions.GetBondPropLabelFont method
- OEFont class

## **SetBondPropLabelFontScale**

void SetBondPropLabelFontScale(double scale)

Sets the multiplier that can be used increase or decrease the size of the fonts of the bond property labels.

scale This value has to be in the range of [0.5, 2.0]. See examples in Figure:\*Examples of scaling the font of the bond property labels relative to the molecule SetBondPropLabelFontScale method

![](_page_160_Figure_5.jpeg)

![](_page_160_Figure_6.jpeg)

**Example:** (Figure: Example of using the SetBondPropLabelFontScale method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetBondPropLabelFontScale(1.5)
opts.SetBondPropertyFunctor(oedepict.OEDisplayBondIdx())
```

![](_page_160_Figure_9.jpeg)

Fig. 38: Example of using the SetBondPropLabelFontScale method

#### See also:

· OE2DMolDisplayOptions.GetBondPropLabelFontScale method

## **SetBondPropertyFunctor**

void SetBondPropertyFunctor (const OEDisplayBondPropBase & func)

Sets the functor that is used to initialize the bond property labels (OE2DBondDisplay, GetProperty)

**Example:** (Figure: Example of using the SetBondPropertyFunctor method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetBondPropertyFunctor(oedepict.OEDisplayBondIdx())
```

# title

![](_page_161_Figure_7.jpeg)

Fig. 39: Example of using the SetBondPropertyFunctor method

Hint: It is recommended to use the OE2DMolDisplayOptions. SetBondPropertyFunctor method to define the bond property labels when the OE2DMolDisplay object is constructed. All labels displayed on the molecule diagram have to be known in advance in order to be able to minimize the number of label clashes and clippings when calculating the positions of the bond property labels.

See example of user-defined bond properties in Displaying Bond Properties section.

- · OE2DMolDisplayOptions.GetBondPropertyFunctor method
- OEDisplayBondPropBase class
- OEDisplayBondIdx class
- OEDisplayNoBondProp class

### **SetBondStereoStyle**

```
void SetBondStereoStyle (unsigned int style)
```

Sets the style that controls what bond stereo information is displayed.

style This value has to be from the OEBondStereoStyle namespace.

**Example:** (Figure: Example of using the SetBondStereoStyle method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetBondStereoStyle(oedepict.OEBondStereoStyle_Display_All)
```

![](_page_162_Figure_7.jpeg)

Fig. 40: Example of using the SetBondStereoStyle method

#### See also:

- OE2DMolDisplayOptions.GetBondStereoStylemethod
- · OEBondStereoStyle namespace

### **SetBondSVGMarkupFunctor**

void SetBondSVGMarkupFunctor (const OEBondSVGMarkupBase & func)

Sets the functor that defines how bonds are marked in svg image. Drawing elements representing bonds in svg image are grouped together in the following format in which the <group id> and <class name> strings are defined by the given functor:

```
<g id='<group id>' class='<class name>'>
list of drawing elements
\ddot{\phantom{a}}\mathord{<}/\,g\mathord{>}
```

**Note:** This setting has only effect when generating . svg images.

#### See also:

- OEBondSVGMarkupBase abstract base class
- OEBondSVGNoMarkup class
- OEBondSVGBondIdxMarkup class
- · OE2DMolDisplayOptions.GetBondSVGMarkupFunctormethod

#### **SetBondWidthScaling**

void SetBondWidthScaling (bool scale)

Sets whether the line width of the bond are increase or decreased based on the molecule scaling factor (OE2DMolDisplayOptions. GetScale). See examples in Figure: Examples of bond line width.

#### Note:

• The line width of the bonds also depends on the default bond pen that can be set by using the OE2DMolDisplayOptions. SetDefaultBondPen method.

**Example:** (Figure: Example of using the SetBondWithScaling method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts. SetBondWidthScaling (True)
```

#### See also:

· OE2DMolDisplayOptions. GetBondWidthScaling method

### **SetDefaultBondPen**

void SetDefaultBondPen (const OEPen &pen)

Sets the pen that is used to initialize the bond pens (OE2DBondDisplay. GetBgnPen and OE2DBondDisplay. GetEndPen)

**Example:** (Figure: Example of using the SetDefaultBondPen method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
pen = oedepict.OEPen(oechem.OEBlack, oechem.OEBlack, oedepict.OEFill_On, 5.0)
opts.SetDefaultBondPen(pen)
```

Note:

• The style of the pens being used to draw bonds also depends on the bond display style  $(\textit{OE2DBondDisplay})$ 

![](_page_164_Figure_1.jpeg)

Fig. 41: Examples of bond line width: (A) scaling the line width of the bonds relative to the molecule; (B) using constant line width that does not depend on the molecule scaling

![](_page_164_Figure_3.jpeg)

Fig. 42: Example of using the SetBondWidthScaling method

![](_page_165_Figure_1.jpeg)

#### Fig. 43: Example of using the SetDefaultBondPen method

· The color of the pens being used to draw bonds also depends on the given atom and bond color styles (OE2DMolDisplayOptions. SetAtomColorStyle and OE2DMolDisplayOptions. SetBondColorStyle, respectively)

#### See also:

- OE2DMolDisplayOptions.GetDefaultBondPen method
- OEPen class

### **SetDimensions**

void SetDimensions (double width, double height, double scale)

Sets parameters that control the size of the depicted molecule.

width A non-negative number that controls the horizontal limit.

height A non-negative number that controls the vertical limit.

scale A non-negative number that controls the magnification of the depicted molecule. OEScale\_AutoScale scaling means that the molecule is scaled to maximally fit the given dimensions.

**Example:** (Figure: Example of using the SetDimensions method)

```
opts = oedepict.OE2DMolDisplayOptions()
width, height, scale = 300.0, 300.0, 20.0opts. SetDimensions (width, height, scale)
```

- · OE2DMolDisplayOptions. GetHeight and OE2DMolDisplayOptions. SetHeight method
- . OE2DMolDisplayOptions. GetScale and OE2DMolDisplayOptions. SetScale method
- · OE2DMolDisplayOptions. GetWidth and OE2DMolDisplayOptions. SetWidth method
- Controlling the Size of Depicted Molecules section

![](_page_166_Figure_1.jpeg)

Fig. 44: Example of using the SetDimensions method

## SetExplicitAtomLabelAngle

void SetExplicitAtomLabelAngle(const double angle)

In the case of an almost linear X-C-X bond, an explicit "C" label will be drawn if the angle is more that the given angle. 180.0 degree means that the "C" label will never be drawn.

![](_page_166_Figure_6.jpeg)

Fig. 45: Example of using the SetExplicitAtomLabelAngle method

### See also:

· OE2DMolDisplayOptions.GetExplicitAtomLabelAngle method

#### **SetHeight**

void SetHeight (double height)

Sets the vertical limit into which the molecule has to be fitted.

*height* This number has to be non-negative number.

**Example:** (Figure: Example of using the SetHeight method)

```
opts = oedepict.OE2DMolDisplayOptions()
opts.SetHeight(150.0)
```

![](_page_167_Figure_7.jpeg)

#### Fig. 46: Example of using the SetHeight method

#### See also:

- · OE2DMolDisplayOptions. GetHeight method
- · OE2DMolDisplayOptions. SetDimensions method
- Controlling the Size of Depicted Molecules section

#### SetHydrogenStyle

void SetHydrogenStyle (unsigned int style)

Sets the style that controls how implicit and explicit hydrogens are displayed.

style This value has to be from the  $OEHydrogenStyle$  namespace.

**Example:** (Figure: Example of using the SetHydrogenStyle method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetHydrogenStyle(oedepict.OEHydrogenStyle_ImplicitTerminal)
```

- · OE2DMolDisplayOptions.GetHydrogenStyle method
- · OEHydrogenStyle namespace

![](_page_168_Figure_1.jpeg)

Fig. 47: Example of using the SetHydrogenStyle method

### **SetMargin**

void SetMargin (unsigned int marginloc, double margin)

Sets the size of a specific margin of the OE2DMolDisplayOptions object.

marginloc This value has to be from the OEMargin namespace.

- *margin* This number is considered as a percentage of either the width or the height of the molecule display and has to be in the range of  $[2.5\%$ ,  $25.0\%]$ . See example in Table: Example of setting specific margins to 5% (default), 15% and 25%. For example, when setting a margin to 15.0%:
  - in case of the top or the bottom margins, it means that the margin will be 15% of the total height of the molecule display
  - in case of the left or the right margins, it means that the margin will be 15% of the total width of the molecule display

![](_page_168_Figure_10.jpeg)

Table 4: Example of setting specific margins to 5% (default), 15% and  $25%$ 

**Example:** (Figure: Example of using the SetMargin method)

```
width, height, scale = 240.0, 180.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetMargin(oedepict.OEMargin_Bottom, 25.0)
```

![](_page_169_Figure_3.jpeg)

Fig. 48: Example of using the SetMargin method

#### See also:

- · OE2DMolDisplayOptions. GetMargin method
- OEMargin namespace

#### **SetMargins**

void SetMargins (double margin)

Sets the size of all margins of the OE2DMolDisplayOptions object.

*margin* This number is considered as a percentage of either the width or the height of the molecule display and has to be in the range of  $[2.5\%$ ,  $25.0\%$ ]. For example, 15.0% means, that the left and right margin are 15% of the total width of the molecule display, and the top and bottom margins are 15% of the total height of the molecule display. See example in Figure: Example of setting all margins to 5% (default), 15% and 25%.

**Example:** (Figure: Example of using the SetMargin method)

```
width, height, scale = 240.0, 180.0, oedepict.OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetMargins(25.0)
```

- · OE2DMolDisplayOptions. GetMargin method
- · OEMargin namespace

![](_page_170_Figure_1.jpeg)

Fig. 49: Example of setting all margins to 5% (default), 15% and 25%

![](_page_170_Figure_3.jpeg)

Fig. 50: Example of using the SetMargins method

### **SetProtectiveGroupLabelFont**

```
void SetProtectiveGroupLabelFont (const OEFont & font)
```

Sets the font that is used to display the abbreviations of contracted functional groups.

**Example:** (Figure: Example of using the ProtectiveGroupLabelFont method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
font = <code>oedepict.OEFont()</code>font.SetColor(oechem.OEDarkRed)
opts.SetProtectiveGroupLabelFont(font)
opts.SetProtectiveGroupStyle(oedepict.OEProtectiveGroupStyle_All)
```

- · OE2DMolDisplayOptions.GetProtectiveGroupLabelFont method
- · OE2DMolDisplayOptions.GetProtectiveGroupStylemethod
- · OE2DMolDisplayOptions. GetSuperAtomStyle method

![](_page_171_Figure_1.jpeg)

### Fig. 51: Example of using the SetProtectiveGroupLabelFont method

• OEFont class

#### Note:

• The size of the protective group fonts also depends on the scaling factor used to fit a molecule to a given dimension (OE2DMolDisplayOptions. SetScale).

### **SetProtectiveGroupStyle**

void SetProtectiveGroupStyle (unsigned int style)

Sets the style that controls whether or not specific pre-defined protective group are contracted and labeled with corresponding abbreviations.

style This value has to be from the OEProtectiveGroupStyle namespace.

**Example:** (Figure: Example of using the SetProtectiveGroupStyle method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetProtectiveGroupStyle(oedepict.OEProtectiveGroupStyle_All)
```

- · OE2DMolDisplayOptions. HasProtectiveGroupStyle method
- · OE2DMolDisplayOptions.GetProtectiveGroupLabelFont method
- · OE2DMolDisplayOptions.GetSuperAtomStylemethod
- · OEProtectiveGroupStyle namespace

![](_page_172_Figure_1.jpeg)

Fig. 52: Example of using the SetProtectiveGroupStyle method

## **SetScale**

void SetScale (double scale)

Sets the scaling factor used to magnify a molecule.

scale This number has to be non-negative number.

**Example:** (Figure: Example of using the SetScale method)

```
opts = oedepict.OE2DMolDisplayOptions()
opts.SetScale(20.0)
```

![](_page_172_Figure_9.jpeg)

Fig. 53: Example of using the SetScale method

- · OE2DMolDisplayOptions.GetScalemethod
- · OE2DMolDisplayOptions. SetDimensions method
- Controlling the Size of Depicted Molecules section

## **SetSuperAtomLabelFont**

void SetSuperAtomLabelFont (const OEFont &font)

Sets the font that is used to display the abbreviations of contracted functional groups.

**Example:** (Figure: Example of using the SetSuperAtomLabelFont method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
font = <code>oedepict.OEFont()</code>font.SetColor(oechem.OEDarkRed)
opts.SetSuperAtomLabelFont(font)
opts.SetSuperAtomStyle(oedepict.OESuperAtomStyle_All)
```

![](_page_173_Figure_6.jpeg)

Fig. 54: Example of using the SetSuperAtomLabelFont method

### See also:

- · OE2DMolDisplayOptions.GetSuperAtomLabelFont method
- · OE2DMolDisplayOptions.GetSuperAtomStylemethod
- OEFont class

#### Note:

• The size of the super atom fonts also depends on the scaling factor used to fit a molecule to a given dimension (OE2DMolDisplayOptions.SetScale).

### **SetSuperAtomStyle**

```
void SetSuperAtomStyle (unsigned int style)
```

Sets the style that controls whether or not specific pre-defined functional groups are contracted and labeled with corresponding abbreviations.

style This value has to be from the  $OESuperAtomStyle$  namespace.

**Example:** (Figure: Example of using the SetSuperAtomStyle method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetSuperAtomStyle(oedepict.OESuperAtomStyle_All)
```

![](_page_174_Figure_7.jpeg)

Fig. 55: Example of using the SetSuperAtomStyle method

### See also:

- · OE2DMolDisplayOptions.GetSuperAtomStylemethod
- · OE2DMolDisplayOptions.GetSuperAtomLabelFont method
- · OESuperAtomStyle namespace

### **SetTitleFont**

void SetTitleFont (const OEFont & font)

Sets the font that is used to display the title of the molecule  $(i.e.$  the string returned by the OEMO1Base. GetTitle method).

**Example:** (Figure: Example of using the SetTitleFont method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
font = oedepict.OEFont()
font.SetStyle(oedepict.OEFontStyle_Bold)
```

![](_page_175_Figure_2.jpeg)

![](_page_175_Figure_3.jpeg)

Fig. 56: Example of using the SetTitleFont method

Note: The size of the title font also depends on:

- the width and height of the molecule display
- the height of the title area that can be set by OE2DMolDisplayOptions. SetTitleHeight method
- the multiplier that can be set by the OE2DMolDisplayOptions. Set TitleFontScale method

See example in Figure: Example of scaling the title along with the molecule

![](_page_175_Figure_10.jpeg)

Fig. 57: Example of scaling the title along with molecule

- · OE2DMolDisplayOptions.GetTitleFont method
- · OE2DMolDisplayOptions. SetTitleFontScale method
- · OE2DMolDisplayOptions. SetTitleHeight method

• OEFont class

## **SetTitleFontScale**

```
void SetTitleFontScale (double scale)
```

Sets the multiplier that can be used increase or decrease the size of the fonts of the atom labels.

scale This value has to be either  $0.0$  or in a range of  $[0.5, 2.0]$ . See examples in *Examples of scaling the font* of title relative to the molecule In case of  $0.0$ , the title is not scaled with the molecule but rather fixed font size is used regardless of dimensions of the image. See example in Figure: Example of titles with fixed font size

![](_page_176_Figure_6.jpeg)

Fig. 58: Examples of scaling the font of title relative to the molecule

![](_page_176_Figure_8.jpeg)

Fig. 59: Example of titles with fixed font size

**Example:** (Figure: Example of using the SetTitleFontScale method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetTitleFontScale(0.5)
```

#### See also:

· OE2DMolDisplayOptions.GetTitleFontScale method

![](_page_177_Figure_1.jpeg)

Fig. 60: Example of using the SetTitleFontScale method

### **SetTitleLocation**

```
void SetTitleLocation (unsigned int loc)
```

Sets the position of the molecule title.

loc This value has to be from the OETitleLocation namespace.

**Example:** (Figure: Example of using the SetTitleLocation method)

```
width, height, scale = 300.0, 200.0, oedepict. OEScale_AutoScale
opts = oedepict. OE2DMolDisplayOptions (width, height, scale)
opts.SetTitleLocation(oedepict.OETitleLocation_Bottom)
```

![](_page_177_Figure_9.jpeg)

title

Fig. 61: Example of using the SetTitleLocation method

- OE2DMolDisplayOptions. GetTitleLocation method
- · OETitleLocation namespace

#### **SetTitleHeight**

void SetTitleHeight (double height)

Sets the height of the title area of the OE2DMolDisplayOptions object.

**height** This number is considered as a percentage of the height of the molecule display and has to be in the range of [5.0%, 25.0%]. See example in Figure: Example of setting height of the title area to 5%, 10% (default) and 25%.

![](_page_178_Figure_7.jpeg)

Fig. 62: Example of setting height of the title area to 5%, 10% (default) and 25%

Note: A molecule display has a title area only if the title location is not hidden. See also OETitleLocation namespace.

**Example:** (Figure: Example of using the SetTitleHeight method)

```
width, height, scale = 300.0, 200.0, oedepict.OEScale_AutoScale
opts = oedepict.OE2DMolDisplayOptions(width, height, scale)
opts.SetTitleHeight(20.0)
```

See also:

· OE2DMolDisplayOptions. GetTitleHeight method

#### **SetWidth**

void SetWidth (double width)

Sets the horizontal limit into which the molecule has to be fitted.

width This number has to be non-negative number.

**Example:** (Figure: Example of using the SetWidth method)

![](_page_179_Figure_1.jpeg)

![](_page_179_Figure_2.jpeg)

Fig. 63: Example of using the SetTitleHeight method

```
opts = oedepict.OE2DMolDisplayOptions()
opts.SetWidth(150.0)
```

![](_page_179_Figure_5.jpeg)

Fig. 64: Example of using the SetWidth method

## See also:

- · OE2DMolDisplayOptions.GetWidth method
- · OE2DMolDisplayOptions. SetDimensions method
- Controlling the Size of Depicted Molecules section

## 4.1.5 OE2DPath

#### class OE2DPath

A sequence of lines and curves.

### See also:

· OEImageBase. DrawPath

![](_page_180_Figure_1.jpeg)

Fig. 65: Example of path

### **Constructors**

OE2DPath()

Default constructor. The starting point of the path have to be defined using the OE2DPath. AddStartPoint method.

OE2DPath (const OE2DPoint & start, bool closed=true)

Create a new path with a starting point.

start The current point that will be starting point of the first line or curve.

closed If true, than a line segment will be added from the starting point to the end point of the last line or curve segment of the path. See examples in Table: Examples of closed and open paths.

**Note:** The starting point of the path will be associated with the OE2DPathPoint Type\_Start type when returned by the OE2DPath. GetPoints method.

![](_page_180_Figure_11.jpeg)

|  | Table 5: Examples of closed and open paths |  |  |  |  |  |
|--|--------------------------------------------|--|--|--|--|--|
|--|--------------------------------------------|--|--|--|--|--|

OE2DPath (const OE2DPath & rhs)

Copy constructor.

OE2DPath (const OE2DPath &rhs, double scale)

Copy constructor with scaling.

scale The scaling factor is used to create a new image from the given one. The scaling factor has to be a positive (non-zero) number.

OE2DPath (const OE2DPath & rhs, const OE2DPoint & offset)

Copy constructor with offset.

offset The offset of new path relative to the copied one.

OE2DPath (const OE2DPath & rhs, const OE2DPoint & center, double degrees)

Copy constructor with rotation.

center The center of the rotation.

degree The rotation in degrees.

#### operator=

OE2DPath & operator=(const OE2DPath & rhs)

Assignment operator.

#### **AddCurveSegment**

void AddCurveSeqment (const OE2DPoint &c1, const OE2DPoint &c2, const OE2DPoint &end)

Adds a cubic Bézier curve to the path from the end point of the last line or curve segment of the path to the position end using c1 and c2 control points.

 $c1$ ,  $c2$  The control points of the curve.

end The end point of the curve segment.

![](_page_181_Figure_18.jpeg)

Fig. 66: Example of adding a curve segment to a path

Note: Points added to the path with the OE2DPath. AddCurveSeqment method will be associated with the following types when returned by the  $OE2DPath$ . GetPoints method:

- · OE2DPathPointType\_CurveC1
- · OE2DPathPointType\_CurveC2

```
· OE2DPathPointType_CurveEnd
```

#### See also:

- OE2DPoint class
- · OEImageBase. DrawCubicBezier method
- · OE2DPath. GetPoints method

## **AddLineSegment**

void AddLineSegment (const OE2DPoint & end)

Adds a line to the path from the end point of the last line or curve segment of the path to the position end.

end The end point of the line segment.

![](_page_182_Figure_10.jpeg)

## Fig. 67: Example of adding a line segment to a path

Note: Points added to the path with the OE2DPath. AddLineSegment method will be associated with the OE2DPathPointType\_LineEndtype when returned by the OE2DPath. GetPoints method.

### See also:

- OE2DPoint class
- · OEImageBase. DrawLine method

## **AddStartPoint**

void AddStartPoint (const OE2DPoint& start);

Adds the starting point of the path. If clears all previously added line or curve segments.

#### **GetEnd**

OE2DPoint GetEnd() const;

Returns the end position of the path.

### See also:

• OE2DPath, GetStart method

### **GetPoints**

OESystem::OEIterBase<OE2DPathPoint> \*GetPoints() const

Returns an iterator over all points of the path. Each point is associated with a type from the OE2DPathPointType namespace.

#### **Example:**

```
for p in path.GetPoints():
     pos = p \cdot GetPoint()print (" \frac{2}{3}.1f \frac{2}{3}.1f \frac{2}{3}d" \frac{2}{3} (pos.GetX(), pos.GetY(), p.GetPointType()))
```

See also:

- OE2DPathPoint class
- OE2DPathPointType namespace

### **GetStart**

OE2DPoint GetStart () const;

Returns the starting position of the path.

#### See also:

· OE2DPath. GetEnd method

#### **IsClosed**

bool IsClosed() const

Returns whether a line segment will be added from the starting point to the end point of the last line or curve segment of the path. See examples in Table: Examples of closed and open paths.

#### See also:

· OE2DPath. SetClosed method

### **IsValid**

|--|

Returns whether the OE2DPath object is valid. A path is considered valid if it has a starting point.

## **SetClosed**

```
void SetClosed (bool closed)
```

Sets whether a line segment will be added from the starting point to the end point of the last line or curve segment of the path.

## 4.1.6 OE2DPathPoint

```
class OE2DPathPoint
```

Represent a 2D point of a path with associated type from the  $OE2DPathPointType$  namespace.

![](_page_184_Figure_10.jpeg)

See also:

· OE2DPath. GetPoints method

### **Constructors**

OE2DPathPoint (const OE2DPoint &point, unsigned int ptype)

Constructs an OE2DPathPoint object with a given type from the OE2DPathPointType namespace.

```
OE2DPathPoint (const OE2DPathPoint & rhs)
```

Copy constructor.

#### operator=

```
OE2DPathPoint & operator=(const OE2DPathPoint & rhs)
```

Assignment operator.

### **GetPoint**

const OE2DPoint &GetPoint () const

Returns the 2D coordinates of the point.

## **GetPointType**

unsigned int GetPointType() const

Returns the type of the point from the OE2DPathPointType namespace.

## 4.1.7 OE2DPoint

class OE2DPoint

This class represents OE2DPoint that stores an x (horizontal), y (vertical) coordinate pair.

The coordinate system used in OEDepict TK has the origin  $(x=0.0, y=0.0)$  at the top/left with the x-axis pointing to the right and the y-axis pointing down. See Figure: 2D coordinate system.

![](_page_185_Figure_14.jpeg)

Fig. 68: 2D coordinate system  $(X = horizontal, Y = vertical)$ 

### **Constructors**

OE2DPoint()

Default constructor that initializes an *OE2DPoint* object with  $x = 0.0$ ,  $y = 0.0$  coordinates.

OE2DPoint (double x, double y)

Constructor that initializes an OE2DPoint object with the give x, y coordinates.

OE2DPoint (const OE2DPoint & rhs)

Copy constructor.

#### operator=

OE2DPoint & operator= (const OE2DPoint & rhs)

Assignment operator.

#### operator+

OE2DPoint operator+ (const OE2DPoint & rhs) const

Addition operator:  $(a_x, a_y) + (b_x, b_y) = (a_x + b_x, a_y + b_y)$ 

#### operator-

OE2DPoint operator-(const OE2DPoint & rhs) const

Subtraction operator:  $(a_x, a_y) - (b_x, b_y) = (a_x - b_x, a_y - b_y)$ 

#### operator/

OE2DPoint operator/(double) const

Division operator:  $(a_x, a_y)/D = (a_x/D, a_y/D)$ 

#### operator \*

OE2DPoint operator \* (double) const

Multiplication operator:  $(a_x, a_y) * D = (a_x * D, a_y * D)$ 

### operator+=

```
OE2DPoint & operator+=(const OE2DPoint & p)
```

Addition assignment operator.

#### operator-=

OE2DPoint & operator-=(const OE2DPoint & p)

Subtraction assignment operator.

### $operator/=$

OE2DPoint & operator/=(double)

Division assignment operator.

### operator\*=

OE2DPoint & operator \*= (double)

Multiplication assignment operator.

## **GetX**

double GetX() const

Returns the x (horizontal) coordinate of the OE2DPoint object.

#### See also:

· OE2DPoint. SetY method

### **GetY**

double GetY() const

Returns the y (vertical) coordinate of the OE2DPoint object.

#### See also:

· OE2DPoint. SetY method

## **SetX**

void SetX(double x)

Sets the x (horizontal) coordinate of the OE2DPoint object.

#### See also:

· OE2DPoint.GetX method

## **SetY**

void SetY (double y)

Sets the y (vertical) coordinate of the OE2DPoint object.

#### See also:

· OE2DPoint.GetY method

## **4.1.8 OEAlignmentOptions**

### class OEAlignmentOptions

This class represents OEAlignmentOptions and stores the following parameters which are used when performing molecule alignment.

| Property                                              | Get method                   | Set method                   |
|-------------------------------------------------------|------------------------------|------------------------------|
| re-generating 2D coordinates                          | GetClearCoords               | SetClearCoords               |
| adding depiction hydrogens                            | GetAddDepictionHydrogens     | SetAddDepictionHydrogens     |
| starting from the 2D coords of the reference molecule | GetFixedCoords               | SetFixedCoords               |
| max number of allowed atom pair clashes               | GetMaxAllowedAtomPairClashes | SetMaxAllowedAtomPairClashes |
| max number of bond rotations                          | GetMaxBondRotations          | SetMaxBondRotations          |
| max number of pattern matches                         | GetMaxPatternMatches         | SetMaxPatternMatches         |
| RMSD cutoff                                           | GetRMSDCutoff                | SetRMSDCutoff                |
| rotation around bonds                                 | GetRotateAroundBonds         | SetRotateAroundBonds         |
| suppressing hydrogens                                 | GetSuppressHydrogens         | SetSuppressHydrogens         |

#### See also:

· OEPrepareAlignedDepiction function

### **Constructors**

OEAlignmentOptions()

Default constructor that initializes an OEAlignmentOptions object with the following properties:

| Property                                                   | Default value                                                 |
|------------------------------------------------------------|---------------------------------------------------------------|
| re-generating 2D coordinates                               | true                                                          |
| adding depiction hydrogens                                 | true                                                          |
| starting from the 2D coordinates of the reference molecule | false                                                         |
| max number of allowed atom pair clashes                    | 0 (means an alignment is rejected if there is any atom clash) |
| max number of bond rotations                               | $2^{16} = 65536$ (max allowed number is $2^{31}$ )            |
| max number of pattern matches                              | 0 (means no limit)                                            |
| RMSD cutoff                                                | 0.1                                                           |
| rotation around bonds                                      | true                                                          |
| suppressing hydrogens                                      | true                                                          |

OEAlignmentOptions (bool rotatebonds, bool clearcoords, bool suppressH)

Creates an OEAlignmentOptions object with the specified parameters.

rotatebonds See the OEAlignmentOptions. SetRotateAroundBonds method.

clearcoords See the OEAlignmentOptions. SetClearCoords method.

suppressH See the OEAlignmentOptions. Set SuppressHydrogens method.

By default, the RMSD cutoff is 0.1 (see the OEAlignment Options. Set RMSDCutoff method) and maximum number of bond rotations is  $2^{16} = 65536$  (see the OEAlignmentOptions. SetMaxBondRotations method).

OEAlignmentOptions (const OEAlignmentOptions & rhs)

Copy constructor.

#### operator=

OEAlignmentOptions & operator= (const OEAlignmentOptions & rhs)

Assignment operator.

### **GetAddDepictionHydrogens**

**bool** GetAddDepictionHydrogens() const

Returns whether the depiction hydrogens are kept/added during the molecule alignment.

#### See also:

• OEAlignmentOptions. SetAddDepictionHydrogens method

## **GetClearCoords**

bool GetClearCoords() const

Returns whether the 2D coordinates of the  $fit$  molecule will be re-calculated prior to the alignment process.

#### See also:

- · OEDepictCoordinates function
- · OEAlignmentOptions. SetClearCoords method

## **GetFixedCoords**

**bool** GetFixedCoords() const

Returns whether the OEP repareAlignedDepiction function can start the alignment process by copying over the coordinates of the *reference* molecule to the *fit* molecule.

#### See also:

· OEAlignmentOptions. SetFixedCoords method

#### **GetMaxAllowedAtomPairClashes**

unsigned int GetMaxAllowedAtomPairClashes() const

Returns the maximum number of atom pair clashes allowed in fix coordinate mode.

#### See also:

· OEAlignmentOptions. SetMaxAllowedAtomPairClashes method

### **GetMaxBondRotations**

unsigned int GetMaxBondRotations () const

Returns the maximum number of bond rotations performed during the alignment process.

The default value for maximum number of bond rotations is  $2^{16} = 65536$ . This means that by default only the first 16 single bonds of the fit molecule will be rotated to maximize molecule alignment. The max allowed number is  $2^{31}$  that allows the rotate  $31$  bonds independently to find the best alignment.

#### See also:

· OEAlignmentOptions. SetMaxBondRotations method

## **GetMaxPatternMatches**

unsigned int GetMaxPatternMatches() const

Returns the maximum number of matches utilized to performed molecule alignments.

#### See also:

· OEAlignmentOptions. SetMaxPatternMatches method

## **GetRMSDCutoff**

double GetRMSDCutoff() const

Returns the RMSD cutoff value used to identify acceptable alignments.

#### See also:

· OEAlignmentOptions. SetRMSDCutoff method

### **GetRotateAroundBonds**

bool GetRotateAroundBonds() const

Returns whether rotation around the bonds of the *fit* molecule is allowed.

#### See also:

· OEAlignmentOptions. SetRotateAroundBonds method

### GetSuppressHydrogens

bool GetSuppressHydrogens() const

Returns whether the explicit hydrogens are suppressed in the *fit* molecule prior to the alignment process.

#### See also:

· OEAlignmentOptions. SetSuppressHydrogens method

#### **SetAddDepictionHydrogens**

void SetAddDepictionHydrogens (bool)

Sets whether depiction hydrogens are kept/added during alignment.

- · OEAddDepictionHydrogens function
- · OEPrepareDepictionOptions.GetAddDepictionHydrogens method

## **SetClearCoords**

```
void SetClearCoords (bool clearcoords)
```

Sets whether the 2D coordinates of the *fit* molecule will be re-calculated prior to the alignment process by calling the OEPrepareDepiction function.

#### See also:

- · OEDepictCoordinates function
- OEAlignmentOptions.GetClearCoords method

### **SetFixedCoords**

void SetFixedCoords (bool fixed)

Sets whether the OEPrepareAlignedDepiction function can start the alignment process by copying over the coordinates of the *reference* molecule to the *fit* molecule based on the provided match.

If the alignment process based of 'fixed' coordinates can not be performed or it is unsuccessful *i.e.* no alignment is found without atom clashes than the OEPrepareAliqnedDepiction function falls back to maximizing the overlap between the *fit* and the *reference* 2D molecules by rotating around single bonds. See also OEAlignmentOptions. SetMaxAllowedAtomPairClashes method that can be used to allow some atom clashes.

The alignment process based on 'fixed' coordinates currently can only be performed if:

- neither the *reference* nor the *fit* molecule have more than one component
- there is no partial ring match *i.e.* if a ring atom of the  $fit$  molecule is matched for alignment than all of the atom of the same ring systems have to be matched for alignment

#### See also:

• OEAlignmentOptions.GetFixedCoords method

### **SetMaxAllowedAtomPairClashes**

void SetMaxAllowedAtomPairClashes (unsigned int maxclashes) const

Sets the number of atom pair clashes allowed after the 'fixed' coordinates alignment process (see OEAlignmentOptions. SetFixedCoords method). The default value is 0, i.e. no atom clashes are allowed. If the number of clashes exceeds this limit the alignment is rejected and process falls back to maximizing the overlap between the *fit* and the *reference* 2D molecules by rotating around single bonds.

#### See also:

· OEAlignmentOptions. SetMaxAllowedAtomPairClashes method

## **SetMaxBondRotations**

void SetMaxBondRotations (unsigned int maxrotations)

Sets the maximum number of bond rotations performed during the alignment process.

*maxrotations* The zero value means that there is no limit. Upon reaching this limit, the alignment process terminates and returns the best alignment identified up to that point.

**Hint:** The default value for maximum number of bond rotations is  $2^{16} = 65536$ . This means that by default only the first 16 single bonds of the  $fit$  molecule will be rotated to maximize molecule alignment.

It is recommended to use this parameter in the following cases:

- $\bullet$  if the *fit* molecule being aligned has a large number of rotatable bonds
- if the match that determines the atoms of the *fit* molecule that will be aligned to the atoms of the *reference* molecule has a large number of rotatable bonds

#### See also:

· OEAlignmentOptions.GetMaxBondRotations method

## **SetMaxPatternMatches**

void SetMaxPatternMatches (unsigned int maxmatches)

Sets the maximum number of matches utilized to perform molecule alignments.

*maxmatches* The zero value means that there is no limit. If the molecule alignment is based on more than one matches, then upon reaching this limit, the alignment process terminates and returns the best alignment identified up to that point.

Hint: It is recommended to use this parameter in the following cases:

• if the alignment is based on substructure or maximum common substructure matches and the *reference* or/and fit molecules are highly symmetrical i.e. a large number of matches returned by the substructure or maximum common substructure search algorithms, respectively.

#### See also:

· OEAlignmentOptions.GetMaxPatternMatches method

#### **SetRMSDCutoff**

void SetRMSDCutoff (double rmsdcutoff)

Sets the RMSD cutoff value used to identify acceptable alignments.

*rmsdcutoff* This number has to be non-negative number. The alignment procedure terminates when the *rmsdcutoff* between the *fit* and the *reference* molecule is below this limit and there is no internal clash detected between the atoms of the *fit* molecule.

· OEAlignmentOptions. GetRMSDCutoff method

## **SetRotateAroundBonds**

void SetRotateAroundBonds (bool rotatebonds)

Sets whether rotation around the bonds of the *fit* molecule is allowed.

*rotatebonds* If 'true', then bond of the *fit* molecule will be rotated to find the best alignment between molecules. If 'false', then only 2D rotation and translation of the fit molecule is allowed (i.e. no rotations around bonds) in order to align it to the reference molecule

#### See also:

· OEAlignmentOptions.GetRotateAroundBonds method

#### SetSuppressHydrogens

void SetSuppressHydrogens (bool)

Sets whether the explicit hydrogens are suppressed in the *fit* molecule prior to the alignment process. Only hydrogens that are necessary to faithfully represent tetrahedral stereochemistry will be kept.

#### See also:

- · OEAddDepictionHydrogens function
- · OEHasDepictionHydrogens function
- · OEAlignmentOptions. GetSuppressHydrogens method

## 4.1.9 OEAlignmentResult

class OEAlignmentResult : public OEChem:: OEMatchBase

The OEAlignmentResult class is a concrete instance of the OEMatchBase abstract base class. An OEAlignmentResult object represents a pairwise correspondence between atoms and/or bonds in two different molecules being aligned by the OEP repareAlignedDepiction function.

The following methods are publicly inherited from OEMatchBase:

| operator bool | GetBonds        | GetTargetBonds |
|---------------|-----------------|----------------|
| Clear         | GetPatternAtoms | IsValid        |
| CreateCopy    | GetPatternBonds | NumAtoms       |
| GetAtoms      | GetTargetAtoms  | NumBonds       |

- OEMatchBase class in the **OEChem TK** manual
- · OEPrepareAlignedDepiction function
- Molecule Alignment chapter

## **Constructors**

OEAlignmentResult()

#### Default constructor.

OEAlignmentResult (const OEChem:: OEMatchBase &match)

Constructors an OEAlignmentResult object from a match.

OEAlignmentResult (const OEAlignmentResult & rhs)

Copy constructor.

#### operator=

OEAlignmentResult & operator= (const OEAlignmentResult & rhs)

Assignment operator.

#### Clear

void Clear()

Removes all atom and bond of pairs from the OEAlignmentResult object.

#### **CreateCopy**

OEMatchBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned object derived from OEMatch-Base is dynamically allocated and owned by the caller.

#### **GetAtoms**

OESystem::OEIterBase<OEChem::OEMatchPair<OEChem::OEAtomBase>>><CetAtoms() const

Returns an iterator over OEMatchPair which contain the atom to atom correspondences in the OEAlignmentResult object.

See also:

OEMatchPair class in the **OEChem TK** manual

## **GetBonds**

```
OESystem::OEIterBase<OEChem::OEMatchPair<OEChem::OEBondBase>> > +GetBonds() const
```

Returns an iterator over OEMatchPair which contain the bond to bond correspondences in the OEAlignmentResult object.

### See also:

OEMatchPair class in the **OEChem TK** manual

### **GetRMSD**

double GetRMSD() const

Returns the RMSD of the alignment based on the correspondence stored in the OEAlignmentResult object.

#### **IsValid**

bool IsValid() const

Returns true if there at least one atom to atom or bond to bonds correspondence is stored in the OEAlignmentResult object *i.e.* whether the alignment performed by the *OEAlignmentResult* function was successful.

#### **NumAtoms**

unsigned int NumAtoms () const

Returns the number of atom equivalences in the OEAlignmentResult object.

#### **NumBonds**

unsigned int NumBonds () const

Returns the number of bond equivalences in the OEAlignmentResult object.

## 4.1.10 OEAtomDisplayBase

class OEAtomDisplayBase : public OESystem:: OEBase

The OEAtomDisplayBase class is the abstract interface for representing atom display information within OEDepict TK. See Figure: OEDepict TK atom display class hierarchy.

#### The following classes derive from this class:

• OE2DAtomDisplay

![](_page_197_Figure_1.jpeg)

![](_page_197_Figure_2.jpeg)

## **GetDataType**

const void \*GetDataType() const

This function is used to perform run-time type identification.

#### See also:

· OEBase. GetDataType method in the OEChem TK manual

### **GetAtom**

const OEChem:: OEAtomBase \*GetAtom() const

Returns the const pointer of the OEAtomBase object for which display properties are stored in the class derived from the OEAtomDisplayBase abstract class.

### **IsDataType**

bool IsDataType (const void \*) const

Returns whether type is the same as the instance this method is called on.

### See also:

• OEBase. IsDataType method in the OEChem TK manual

### **IsVisible**

bool IsVisible() const

Returns whether or not the atom is depicted  $(i.e.$  visible).

### **SetVisible**

void SetVisible (bool visible)

Sets the visibility of an atom.

## 4.1.11 OEAtomSVGAtomIdxMarkup

class OEAtomSVGAtomIdxMarkup : public OEAtomSVGMarkupBase

This class represents the OEAtomSVGAtomIdxMarkup atom SVG markup functor. If this functor is passed to the OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method, the atoms will be not marked in the svg image when calling the OERenderMolecule function.

#### See also:

- Generating Interactive SVG Images chapter
- · OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method
- OEAtomSVGNoMarkup class
- OEAtomSVGResidueMarkup class

The following methods are publicly inherited from OEAtomSVGMarkupBase:

CreateCopy GetClassName GetGroupId

#### **Constructors**

OEAtomSVGAtomIdxMarkup (const std::string prefix="", const std:: string classname="atom")

Creates an OEAtomSVGAtomIdxMarkup object.

- **prefix** The string that will be added at the beginning of each atom  $q_{\text{f}}$  *oup* id. For information about valid ids see OEIsValidSVGGroupId function. By default, no prefix will be added.
- classname The class name that is going to be used to mark atoms. For information about valid names see OEIsValidSVGClassName function.

By default, the svg image for the first atom of a molecule will be marked as follows:

```
<g id='idx=0' class='atom'>
list of drawing elements
\bar{z} .
\langle \text{circle } \dots \rangle</g>
```

The transparent circle will be drawn with the atom position OE2DAtomDisplay. GetCoords center. This can be used to manipulate the generated . svg image and associate event with the SVG groups.

#### **CreateCopy**

OEAtomSVGMarkupBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEAtomSVGAtomIdxMarkup object is dynamically allocated and owned by the caller.

#### **GetClassName**

std::string GetClassName(const OEChem::OEAtomBase &) const

Returns the string that specifies the  $group$  id of an atom in an svg image.

### **GetGroupId**

std::string GetGroupId(const OEChem::OEAtomBase &) const

Returns the string that specifies the  $class$  name of an atom in an syq image.

## 4.1.12 OEAtomSVGMarkupBase

class OEAtomSVGMarkupBase

OEAtomSVGMarkupBase is an abstract base class. Concrete classes derived from the base class define the markup of the atoms in . svg images that are generated when calling the OERenderMolecule function. Drawing elements representing atoms in the . svg images are grouped together in the following format in which the <group id> and <class name> strings can be defined in the derived concrete classes.

```
<g id='<group id>' class='<class name>'>
list of drawing elements
\ddot{\phantom{a}}</g>
```

The following classes derive from this class:

- OEAtomSVGAtomIdxMarkup
- OEAtomSVGNoMarkup
- OEAtomSVGResidueMarkup

See also:

- · OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method
- Generating Interactive SVG Images chapter

Note: User defined SVG atom marking can be implemented by deriving from this class and implementing all the methods listed below.

Example of using user defined SVG atom markings

```
class UserDataSVGAtomIdxMarkup (oedepict. OEAtomSVGMarkupBase) :
   def GetClassName(self, atom):
       return "user-def-atom-class"
   def GetGroupId(self, atom):
        return "used-def-atom-{}".format(atom.GetIdx())
   def CreateCopy(self):
        return UserDataSVGAtomIdxMarkup()._disown_()
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetAtomSVGMarkupFunctor(UserDataSVGAtomIdxMarkup())
disp = oedepict.OE2DMolDisplay(mol, opts)
```

## **CreateCopy**

OEAtomSVGMarkupBase \*CreateCopy() const =0

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

#### **GetClassName**

std::string GetClassName(const OEChem::OEAtomBase &) const =0

Returns the <class name> associated with a specific atom group in the .svg image. This is a virtual method that has to be implemented in the concrete derived classes. The return string will be verified by the OEIsValidSVGClassName function. Invalid SVG class names will be ignored.

#### See also:

• OEIsValidSVGClassName function

### **GetGroupId**

 $\verb|std::string GetGroupId|(\verb|const OEChem::OEAtomBase >) \verb|const =0$ 

Returns the  $\langle \text{group } id \rangle$  associated with a specific atom group in the . svg image. This is a virtual method that has to be implemented in the concrete derived classes. The return string will be verified by the OEIsValidSVGGroupId function. Invalid SVG group ids will be ignored.

#### See also:

· OEIsValidSVGGroupId function

## 4.1.13 OEAtomSVGNoMarkup

class OEAtomSVGNoMarkup : public OEAtomSVGMarkupBase

This class represents the OEAtomSVGNoMarkup atom SVG markup functor. If this functor is passed to the OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method, the atoms will be not marked in the svg image when calling the OERenderMolecule function.

See also:

- Generating Interactive SVG Images chapter
- · OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method
- OEAtomSVGAtomIdxMarkup class
- OEAtomSVGResidueMarkup class

The following methods are publicly inherited from OEAtomSVGMarkupBase:

CreateCopy GetClassName GetGroupId

#### **Constructors**

OEAtomSVGNoMarkup()

Default constructor.

#### **CreateCopy**

OEAtomSVGMarkupBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEAtomSVGNoMarkup object is dynamically allocated and owned by the caller.

#### **GetClassName**

std::string GetClassName(const OEChem::OEAtomBase &) const

Returns an empty string.

#### **GetGroupId**

std::string GetGroupId(const OEChem::OEAtomBase &) const

Returns an empty string.

## 4.1.14 OEAtomSVGResidueMarkup

class OEAtomSVGResidueMarkup : public OEAtomSVGMarkupBase

This class represents the OEAtomSVGResidueMarkup atom SVG markup functor. If this functor is passed to the OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method, the atoms will be not marked in the svg image when calling the OERenderMolecule function.

See also:

- Generating Interactive SVG Images chapter
- · OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor method
- OEAtomSVGAtomIdxMarkup class
- OEAtomSVGNoMarkup class

The following methods are publicly inherited from OEAtomSVGMarkupBase:

CreateCopy GetClassName GetGroupId

#### **Constructors**

```
OEAtomSVGResidueMarkup (const std::string prefix="",
                       const std:: string classname="ligand-atom",
                       const char separator = '-')
```

Creates an OEAtomSVGResidueMarkup object.

- **prefix** The string that will be added at the beginning of each atom  $q_{\text{f}}$  oup id. For information about valid ids see OEIsValidSVGGroupId function. By default, no prefix will be added.
- classname The class name that is going to be used to mark atoms. For information about valid names see OEIsValidSVGClassName function.
- separator. The character used to separate the components (residue name, chain id, residue number, atom name) of the group id

By default, the following will be showed in svg image for marking of the first atom of molecule NC (CCCNC (N) = N) C (O) = O with residue information:

By default, the svg image for the first atom of molecule  $NC$  (CCCNC (N) =N) C (O) =O with residue information will be marked as follows:

```
<g id='ARG-A-1-_N__' class='ligand-atom'>
\simlist of drawing elements
\ddot{\phantom{a}} .
\langlecircle ... >
</g>
```

If there is no residue information attached to the atom the UNK label will be used for the residue name. The residue information can be perceived by calling the OEPerceiveResidues function.

Since a valid group id can not have a space character, each space character of the atom name (returned by OEAtomBase.GetName) is replaces by an \_(underline).

The transparent circle will be drawn with the atom position OE2DAtomDisplay. GetCoords center. This can be used to manipulate the generated . svg image and associate event with the SVG groups.

## **CreateCopy**

OEAtomSVGMarkupBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEAtomSVGResidueMarkup object is dynamically allocated and owned by the caller.

### **GetClassName**

std::string GetClassName(const OEChem::OEAtomBase &) const

Returns the string that specifies the  $q_{\text{roup}}$  id of an atom in an svq image.

## **GetGroupId**

std::string GetGroupId(const OEChem::OEAtomBase &) const

Returns the string that specifies the  $class$  name of an atom in an svg image.

## 4.1.15 OEBondDisplayBase

class OEBondDisplayBase : public OESystem:: OEBase

The OEBondDisplayBase class is the abstract interface for representing bond display information within OEDepict **TK.** See Figure: OEDepict TK bond display class hierarchy.

![](_page_203_Figure_14.jpeg)

Fig. 70: OEDepict TK bond display class hierarchy

#### The following classes derive from this class:

• OE2DBondDisplay

### **GetDataType**

const void \*GetDataType() const

This function is used to perform run-time type identification.

#### See also:

· OEBase. GetDataType method in the OEChem TK manual

#### **GetBond**

const OEChem:: OEBondBase \*GetBond() const

Returns the const pointer of the OEBondBase object for which display properties are stored in the class derived from the *OEBondDisplayBase* abstract class.

#### **IsDataType**

bool IsDataType (const void \*) const

Returns whether type is the same as the instance this method is called on.

#### See also:

• OEBase. IsDataType method in the OEChem TK manual

#### **IsVisible**

bool IsVisible() const

Returns whether or not the bond is depicted (*i.e.* visible).

#### **SetVisible**

void SetVisible (bool visible)

Sets the visibility of a bond.

## 4.1.16 OEBondSVGBondIdxMarkup

class OEBondSVGBondIdxMarkup : public OEBondSVGMarkupBase

This class represents the OEBondSVGBondIdxMarkup bond SVG markup functor. If this functor is passed to the OE2DMolDisplayOptions. SetBondSVGMarkupFunctor method, the bonds will be not marked in the svg image when calling the OERenderMolecule function.

- Generating Interactive SVG Images chapter
- · OE2DMolDisplayOptions. SetBondSVGMarkupFunctor method

• OEBondSVGNoMarkup class

The following methods are publicly inherited from OEBondSVGMarkupBase:

```
GetClassName
CreateCopy
                          GetGroupId
```

#### **Constructors**

```
OEBondSVGBondIdxMarkup(const std::string prefix="",
                       const std:: string classname="bond)
```

Creates an OEBondSVGBondIdxMarkup object.

- **prefix** The string that will be added at the beginning of each bond  $q_{\text{f}}$  and  $q_{\text{f}}$  and  $q_{\text{f}}$  and  $q_{\text{f}}$  and  $q_{\text{f}}$  and  $q_{\text{f}}$  are information about valid ids see OEIsValidSVGGroupId function. By default, no prefix will be added.
- classname. The class name that is going to be used to mark bonds. For information about valid names see OEIsValidSVGClassNamefunction.

By default, the svg image for the first bond of a molecule will be marked as follows:

```
<q id='idx=0' class='bond'>
list of drawing elements
\ddot{\phantom{a}}\langle \text{circle } \dots \rangle\langle / g >
```

The transparent circle will be drawn at the middle of the bond. This can be used to manipulate the generated . svg image and associate event with the SVG groups.

### **CreateCopy**

OEBondSVGMarkupBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondSVGBondIdxMarkup object is dynamically allocated and owned by the caller.

### **GetClassName**

std::string GetClassName(const OEChem::OEBondBase &) const

Returns the string that specifies the  $group$  id of an bond in an svg image.

### **GetGroupId**

std::string GetGroupId(const OEChem::OEBondBase &) const

Returns the string that specifies the  $\text{class}$  name of an bond in an svq image.

## 4.1.17 OEBondSVGMarkupBase

#### class OEBondSVGMarkupBase

OEBondSVGMarkupBase is an abstract base class. Concrete classes derived from the base class define the markup of the bonds in . svq images that are generated when calling the *OERenderMolecule* function. Drawing elements representing bonds in the . svq images are grouped together in the following format in which the <qroup id> and <class name> strings can be defined in the derived concrete classes.

```
<q id='<qroup id>' class='<class name>'>
list of drawing elements
\ddot{\phantom{a}}\mathord{<}/\,g\mathord{>}
```

The following classes derive from this class:

- OEBondSVGBondIdxMarkup
- OEBondSVGNoMarkup

#### See also:

- · OE2DMolDisplayOptions. SetBondSVGMarkupFunctor method
- Generating Interactive SVG Images chapter

Note: User defined SVG atom marking can be implemented by deriving from this class and implementing all the methods listed below.

#### **Example of using user defined SVG atom markings**

```
class UserDataSVGBondIdxMarkup (oedepict.OEBondSVGMarkupBase):
   def GetClassName(self, bond):
        return "user-def-bond-class"
    def GetGroupId(self, bond):
        return "user-def-bond-\{\}".format(bond.GetIdx())
   def CreateCopy(self):
        return UserDataSVGBondIdxMarkup()._disown_()
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetBondSVGMarkupFunctor(UserDataSVGBondIdxMarkup())
disp = oederict.OE2DMolDisplay(mol, opts)
```

### **CreateCopy**

```
OEBondSVGMarkupBase *CreateCopy() const = 0
```

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

### **GetClassName**

std::string GetClassName(const OEChem::OEBondBase &) const = 0

Returns the <class name> associated with a specific bond group in the .svg image. This is a virtual method that has to be implemented in the concrete derived classes. The return string will be verified by the OEIsValidSVGClassName function. Invalid SVG class names will be ignored.

#### See also:

• OEIsValidSVGClassName function

### **GetGroupId**

std::string GetGroupId(const OEChem::OEBondBase &) const =0

Returns the  $\langle \text{group } id \rangle$  associated with a specific bond group in the . svg image. This is a virtual method that has to be implemented in the concrete derived classes. The return string will be verified by the OEIsValidSVGGroupId function. Invalid SVG group ids will be ignored.

See also:

· OEIsValidSVGGroupId function

## 4.1.18 OEBondSVGNoMarkup

class OEBondSVGNoMarkup : public OEBondSVGMarkupBase

This class represents the OEBondSVGNoMarkup bond SVG markup functor. If this functor is passed to the OE2DMolDisplayOptions. SetBondSVGMarkupFunctor method, the bonds will be not marked in the svg image when calling the OERenderMolecule function.

#### See also:

- Generating Interactive SVG Images chapter
- · OE2DMolDisplayOptions. SetBondSVGMarkupFunctor method
- OEBondSVGBondIdxMarkup class

The following methods are publicly inherited from OEBondSVGMarkupBase:

CreateCopy GetClassName GetGroupId

## **Constructors**

OEBondSVGNoMarkup()

Default constructor.

### **CreateCopy**

OEBondSVGMarkupBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondSVGNoMarkup object is dynamically allocated and owned by the caller.

#### **GetClassName**

std::string GetClassName(const OEChem::OEBondBase &) const

Returns an empty string.

#### **GetGroupId**

std::string GetGroupId(const OEChem::OEBondBase &) const

Returns an empty string.

## 4.1.19 OEDisplayAtomIdx

class OEDisplayAtomIdx : public OEDisplayAtomPropBase

This class represents OEDisplayAtomIdx atom property label functor.

See also:

- · OE2DMolDisplayOptions. SetAtomPropertyFunctor method
- OEDisplayAtomMapIdx class
- OEDisplayNoAtomProp class
- Listing 5 example in the Molecule Depiction chapter

The following methods are publicly inherited from OEDisplayAtomPropBase:

CreateCopy operator()

## **Constructors**

```
OEDisplayAtomIdx()
```

Default constructor.

#### operator()

std::string operator()(const OEChem::OEAtomBase &atom) const

Returns the string representation of the index of the atom (i.e. the number returned by the OEAtomBase.GetIdx method).

## **CreateCopy**

base\_type \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDisplayAtomIdx object is dynamically allocated and owned by the caller.

## 4.1.20 OEDisplayAtomMapIdx

class OEDisplayAtomMapIdx : public OEDisplayAtomPropBase

This class represents OEDisplayAtomMapIdx atom property label functor.

#### See also:

- · OE2DMolDisplayOptions. SetAtomPropertyFunctor method
- OEDisplayAtomIdx class
- OEDisplayNoAtomProp class
- Listing 2 example in the MDL Reaction Depiction chapter

The following methods are publicly inherited from OEDisplayAtomPropBase:

operator() CreateCopy

### **Constructors**

OEDisplayAtomMapIdx()

Default constructor.

#### operator()

std::string operator()(const OEChem::OEAtomBase &atom) const

Returns the string representation of the *reaction map index* property of the atom. (i.e. the number returned by the OEAtomBase.GetMapIdx method). The reaction map index is used for tracking equivalent atom positions in the reaction. If the reaction map index is zero, meaning that the atom isn't mapped in the reaction, than this function returns an empty string.

### **CreateCopy**

```
base_type *CreateCopy() const
```

Deep copy constructor that returns a copy of the object. The memory for the returned OEDisplayAtomMapIdx object is dynamically allocated and owned by the caller.

## 4.1.21 OEDisplayAtomPropBase

```
OESystem:: OEUnaryFunction<OEChem:: OEAtomBase, std:: string, true, true>
OEDisplayAtomPropBase
```

OEDisplayAtomPropBase is an abstract class that defines the API used for setting atom property labels.

#### See also:

- · OE2DMolDisplayOptions. SetAtomPropertyFunctor method
- Listing 6 example in the Molecule Depiction chapter

The following classes derive from this class:

- OEDisplayAtomIdx class
- OEDisplayAtomMapIdx class
- OEDisplayNoAtomProp class

### operator()

std::string operator() (const OEChem::OEAtomBase &atom) const = 0

It is a virtual const method that is implemented in the concrete derived classes to set atom property labels.

atom The OEAtomBase object for which the display label is set.

### **CreateCopy**

```
base_type *CreateCopy() const =0
```

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

## 4.1.22 OEDisplayBondldx

class OEDisplayBondIdx : public OEDisplayBondPropBase

This class represents OEDisplayBondIdx.

#### See also:

- · OE2DMolDisplayOptions. SetBondPropertyFunctor method
- OEDisplayNoBondProp class
- Listing 7 example in the Molecule Depiction chapter

The following methods are publicly inherited from OEDisplayBondPropBase:

CreateCopy operator()

#### **Constructors**

OEDisplayBondIdx()

Default constructor.

### operator()

std::string operator()(const OEChem::OEBondBase &bond) const

Returns the string representation of the index of the bond (i.e. the number returned by the OEBondBase.GetIdx method)

### **CreateCopy**

base\_type \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDisplayBondIdx object is dynamically allocated and owned by the caller.

## 4.1.23 OEDisplayBondPropBase

```
OESystem::OEUnaryFunction<OEChem::OEBondBase,std::string,true,true>
class OEDisplayBondPropBase
```

OEDisplayBondPropBase is an abstract class that defines the API used for setting bond property labels.

### See also:

- · OE2DMolDisplayOptions. SetBondPropertyFunctor method
- Listing  $\theta$  example in the Molecule Depiction chapter

#### The following classes derive from this class:

- OEDisplayBondIdx class
- OEDisplayNoBondProp class

### operator()

std::string operator()(const OEChem::OEBondBase &bond) const = 0

It is a virtual const method that is implemented in the concrete derived classes to set bond property labels.

**bond** The OEBondBase object for which the display label is set.

### **CreateCopy**

```
base_type *CreateCopy() const =0
```

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

## 4.1.24 OEDisplayNoAtomProp

class OEDisplayNoAtomProp : public OEDisplayAtomPropBase

This class represents OEDisplayNoAtomProp atom property label functor.

#### See also:

- OE2DMolDisplayOptions. SetAtomPropertyFunctor method
- OEDisplayAtomIdx class
- OEDisplayAtomMapIdx class

The following methods are publicly inherited from OEDisplayAtomPropBase:

CreateCopy operator()

## **Constructors**

```
OEDisplayNoAtomProp()
```

Default constructor.

#### operator()

std::string operator()(const OEChem::OEAtomBase & atom) const

Returns an empty string which means no atom property is displayed.

### **CreateCopy**

```
base_type *CreateCopy() const
```

Deep copy constructor that returns a copy of the object. The memory for the returned OEDisplayNoAtomProp object is dynamically allocated and owned by the caller.

## 4.1.25 OEDisplayNoBondProp

class OEDisplayNoBondProp : public OEDisplayBondPropBase

This class represents OEDisplayNoBondProp.

The following methods are publicly inherited from OEDisplayBondPropBase:

CreateCopy operator()

#### See also:

- · OE2DMolDisplayOptions. SetBondPropertyFunctor method
- OEDisplayBondIdx class

### **Constructors**

OEDisplayNoBondProp()

Default constructor.

### operator()

std::string operator()(const OEChem::OEBondBase & bond) const

Returns an empty string, which means that no bond property is displayed.

## **CreateCopy**

base\_type \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDisplayNoBondProp object is dynamically allocated and owned by the caller.

## 4.1.26 OEFont

class OEFont

The OEFont class encapsulates properties that determine the display style of texts.

Currently the *OEFont* class stores the following properties:

| Property       | Get method                                | Set method              | Corresponding<br>names-<br>pace/class/type                       |
|----------------|-------------------------------------------|-------------------------|------------------------------------------------------------------|
| alignment      | <i>GetAlignment</i>                       | <i>SetAlignment</i>     | <i>OEAlignment</i>                                               |
| color          | <i>GetColor</i>                           | <i>SetColor</i>         | <i>OEColor</i>                                                   |
| font family    | <i>GetFamily</i>                          | <i>SetFamily</i>        | <i>OEFontFamily</i>                                              |
| font size      | <i>GetSize</i>                            | <i>SetSize</i>          | None                                                             |
| font style     | <i>GetStyle</i>                           | <i>SetStyle</i>         | <i>OEFontStyle</i>                                               |
| hyperlink      | <i>GetHyperlink</i> / <i>HasHyperlink</i> | <i>SetHyperlink</i>     | string                                                           |
| rotation angle | <i>GetRotationAngle</i>                   | <i>SetRotationAngle</i> | floating point number in range of $[0.0^{\circ}, 360.0^{\circ}]$ |

#### See also:

· OEImageBase. DrawText method

## **Constructors**

| OEFont () |  |  |  |
|-----------|--|--|--|
|           |  |  |  |

Default constructor that initializes an OEFont object with the following properties: See example in Figure: Example of drawing text with default OEFont object.

| Property        | Default value                    |
|-----------------|----------------------------------|
| alignment       | OEAlignment_Default              |
| color           | OEBlack = OEColor(0,0,0)         |
| font family     | OEFontFamily_Default             |
| font size       | 12                               |
| hyperlink       | empty string (i.e. no hyperlink) |
| font style      | OEFontStyle_Default              |
| rotation angles | 0.0 (i.e. no rotation)           |

```
OEFont (const OESystem:: OEColor &color)
```

Constructor that initializes an OEFont object with the default parameters and the given OEColor.

## Hello World!

#### Fig. 71: Example of drawing text with default OEFont object

```
OEFont (unsigned int family, unsigned int style, unsigned int size,
       unsigned int align, const OESystem:: OEColor &color,
       double rotangle = 0.0)
```

Constructor that initializes an *OEFont* object with the given parameters.

- **family** The family of the font. This value has to be from the OEF ont Family namespace. See also OEF ont. SetFamily method.
- style The style of the font. This value has to be from the  $OEFontStyle$  namespace. See also  $OEFont. SetSize$ method.
- size The size of the font. See also  $OEFont$ . Set Size method.
- **align** The alignment of the text. This value has to be from the *OEA1i qnment* namespace. See also *OEF* ont. SetAlignment method.
- *color* The color of the font. See also OEFont. Set Color method.
- *rotangle* The rotation angle of the text. The default value is 0.0 which means no rotation is applied *i.e.* the text using the OEFont object is rendered horizontally. See also OEFont . Set RotationAngle method.

OEFont (const OEFont & rhs)

Copy constructors.

#### operator=

OEFont & operator= (const OEFont & rhs)

Assignment operator.

#### operator!=

bool operator! = (const OEFont & rhs) const

Determines whether two OEFont objects are different. Two OEFont objects are considered different if any of their properties (such as color, size, etc.) are different.

#### operator==

bool operator == (const OEFont & rhs) const

Determines whether two OEFont objects are equal. Two OEFont objects are considered equivalent only if all of their properties (such as color, size, etc.) are identical.

#### **GetAlignment**

unsigned int GetAlignment () const

Returns the *alignment* property of the OEFont object. The returned value is taken from the OEA1ignment namespace.

#### See also:

- · OEFont. SetAlignment method
- · OEAlignment namespace

#### **GetColor**

const OESystem:: OEColor &GetColor() const

Returns the color of the OEFont object.

#### See also:

- · OEFont. SetColor method
- OEColor class

#### **GetFamily**

unsigned int GetFamily () const

Returns the *font family* property of the *OEFont* object. The returned value is taken from the *OEF* ont *Family* namespace.

#### See also:

- · OEFont. SetFamily method
- OEFontFamily namespace

#### **GetHyperlink**

const std:: string& GetHyperlink() const

Returns the URI string associated with the OEFont object.

- · OEFont. HasHyperlink method
- · OEFont. SetHyperlink method

#### **GetRotationAngle**

double GetRotationAngle() const

Returns the angle of the rotation that is used to render a text when using the OEFont object.

#### See also:

· OEFont. SetRotationAngle method

### **GetSize**

unsigned int GetSize() const

Returns the size of the OEFont object.

#### See also:

· OEFont. SetSize method

#### **GetStyle**

unsigned int GetStyle() const

Returns the font style property of the OEFont object. The returned value is taken from the OEFont Style namespace.

#### See also:

- · OEFont. Set Style method
- OEFontStyle namespace

### **HasHyperlink**

bool HasHyperlink () const

Returns whether an URI string is associated with the OEFont object.

#### See also:

- · OEFont.GetHyperlink method
- · OEFont. SetHyperlink method

#### **SetAlignment**

void SetAlignment (unsigned int align)

Sets the *alignment* property of the OEFont object.

**align** This value has to be from the  $OEA1$  i gnment namespace.

Example (Figure: Example of using the SetAlignment method)

![](_page_218_Figure_1.jpeg)

#### Fig. 72: Example of using the SetAlignment method

```
font = oedepict.OEFont()
font.SetAlignment(oedepict.OEAlignment_Right)
```

#### See also:

- · OEFont.GetAlignment method
- OEAlignment namespace

#### **SetColor**

void SetColor (const OESystem:: OEColor &color)

Sets the color of the OEFont object.

Example (Figure: Example of using the SetColor method)

 $font = `oedefict.OEFont()`$ font.SetColor(oechem.OERed)

![](_page_218_Picture_12.jpeg)

### Fig. 73: Example of using the SetColor method

## See also:

- · OEFont. GetColor method
- OEColor class

#### **SetFamily**

void SetFamily (unsigned int family)

Sets the font family property of the OEFont object.

family This value has to be from the OEFontFamily namespace.

Example (Figure: Example of using the SetFamily method)

### Hello World!

#### Fig. 74: Example of using the SetFamily method

```
font = <code>oedepict.OEFont()</code>font.SetFamily(oedepict.OEFontFamily_Times)
```

#### See also:

- · OEFont. GetFamily method
- OEFontFamily namespace

#### **SetHyperlink**

void SetHyperlink (const string& uri)

Associates URI string with the *OEFont* object.

*uri* After associating a valid URI with a OEFont object, texts drawn with the given font become "click-able" and by clicking on them will send you to the given address.

**Example** (Figure: Example of using the SetHyperlink method)

```
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "OC(=0)clccccc1")
oedepict.OEPrepareDepiction(mol)
width, height = 150.0, 150.0image = oedepict. OEImage (width, height)
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetTitleLocation(oedepict.OETitleLocation_Bottom)
# associate font with URI
font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
-10.oedepict.OEAlignment_Center, oechem.OEBlue)
font.SetHyperlink("http://www.eyesopen.com/oedepict-tk")
opts.SetTitleFont(font)
mol.SetTitle("Generated by OEDepict")
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OERenderMolecule(image, disp)
oedepict.OEWriteImage("DepictMolWithHyperlink.pdf", image)
oedepict.OEWriteImage("DepictMolWithHyperlink.svg", image)
```

Note: Associating texts with hyperlinks is only available for . pdf and . svg image formats.

![](_page_220_Figure_1.jpeg)

Generated by GLEPlot

Fig. 75: Example of using the SetHyperlink method (Clicking on the blue text at the bottom send you to the OEDepict TK web page)

Warning: OEDepict TK does not check whether the given string is a valid URI.

It is recommended to always keep the URI scheme prefix of the URI string for the sake of compatibility. For example, some application can interpret the www.eyesopen.com string as a valid URI, others only work when using http://www.eyesopen.com.

#### See also:

- · OEFont.GetHyperlink method
- · OEFont.GetHyperlink method

### **SetRotationAngle**

void SetRotationAngle (double angle)

Sets the rotation angle of the OEFont object.

*angle* The rotation angle of the text (in degrees). The value of the angle has to be in a range of  $[0.0^{\circ}, 360.0^{\circ}]$ .

Example (Figure: Example of using the SetRotationAngle method)

```
font = <code>oedefict.OEFont()</code>font.SetRotationAngle(180.0)
```

**Note:** The angles are interpreted in an anti-clockwise direction. The  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 3 o'clock position *i.e.* the text is rendered horizontally. While the  $180.0^{\circ}$  degrees corresponds to rendering the text upside down.

![](_page_221_Picture_1.jpeg)

#### Fig. 76: Example of using the SetRotationAngle method

See examples in Figure: Example of drawing texts with various rotation angle.

![](_page_221_Figure_4.jpeg)

### Fig. 77: Example of drawing texts with various rotation angles

See also:

· OEFont. GetRotationAngle method

### **SetSize**

void SetSize (unsigned int size)

Sets the size of the OEFont object.

Example (Figure: Example of using the SetSize method)

 $font = `oedefict.OEFont()`$ font.SetSize(30)

# **Hello World!**

Fig. 78: Example of using the SetSize method

#### See also:

· OEFont.GetSize method

## **SetStyle**

void SetStyle (unsigned int style)

Sets the font style property (such as **bold**, *italic* etc.) of the OEFont object.

style This value has to be from the  $OEFontStyle$  namespace.

**Example** (Figure: Example of using the SetStyle method)

```
font = oedepict.OEFont()
font.SetStyle(oedepict.OEFontStyle_Bold | oedepict.OEFontStyle_Italic)
```

## **Hello World!**

Fig. 79: Example of using the SetStyle method

#### See also:

- · OEFont.GetStyle method
- OEFontStyle namespace

## 4.1.27 OEHighlightBase

#### class OEHighlightBase

OEHighlightBase is an abstract class used for highlighting atoms and/or bonds.

#### See also:

· OEAddHighlighting function.

The following classes derive from this class:

- · OEHighlightByBallAndStick
- OEHighlightByColor
- OEHighlightByCogwheel
- OEHighlightByLasso
- OEHighlightByStick

## **Constructors**

```
OEHighlightBase()
OEHighlightBase(OEHighlightBaseImpl *impl)
```

Default constructors.

### **CreateCopy**

virtual OEHighlightBase \*CreateCopy() const =0

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

## 4.1.28 OEHighlightByBallAndStick

class OEHighlightByBallAndStick : public OEHighlightBase

The OEHighlightByBallAndStick class allows the customization of the **ball and stick** highlighting style that is associated with the OEHighlightStyle\_BallAndStick constant. See example in Figure: Example of highlighting using the 'ball and stick' style.

![](_page_223_Figure_10.jpeg)

#### Fig. 80: Example of highlighting using the 'ball and stick' style

The OEHighlightByBallAndStick class stores the following properties:

| Property          | Get method                    | Set method                    | Corresponding<br>namespace /<br>class / type |
|-------------------|-------------------------------|-------------------------------|----------------------------------------------|
| atom label        | <i>GetAtomLabelMonochrome</i> | <i>SetAtomLabelMonochrome</i> | boolean                                      |
| ball radius scale | <i>GetBallRadiusScale</i>     | <i>SetBallRadiusScale</i>     | floating point number                        |
| color             | <i>GetColor</i>               | <i>SetColor</i>               | <b>OEColor</b>                               |
| stick width scale | <i>GetStickWidthScale</i>     | <i>SetStickWidthScale</i>     | floating point number                        |

- · OEAddHighlighting function
- · OEHighlightStyle namespace
- OEHighlightByColor class
- OEHighlightByCogwheel class
- OEHighlightByLasso class

- OEHighlightByStick class
- Highlighting chapter

#### **Constructors**

```
OEHighlightByBallAndStick (const OESystem:: OEColor &c,
                          double stickWidthScale=3.0, double ballRadiusScale=3.0,
                          bool monochrome=true)
```

Creates an OEHighlightByBallAndStick object with the specified parameters.

color The color used for highlighting. See also OEHighlightByBallAndStick. SetColor method.

- stickWidthScale The multiplier that can be used to increase or decrease the stick width of the highlighted bond(s). See also OEHighlightByBallAndStick.SetStickWidthScale method.
- **ballRadiusScale** The multiplier that can be used to increase or decrease the ball radius of the highlighted atom(s). See also OEHighlightByBallAndStick. SetBallRadiusScale method.
- *monochrome* Defines whether or not to change the color of the atom label of the highlighted atom(s). See also OEHighlightByBallAndStick.SetAtomLabelMonochrome method.

OEHighlightByBallAndStick(const OEHighlightByBallAndStick &rhs)

#### Copy constructor.

#### operator=

OEHighlightByBallAndStick & operator=(const OEHighlightByBallAndStick & rhs)

Assignment operator.

### **CreateCopy**

OEHighlightBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEHighlightByBallAndStick object is dynamically allocated and owned by the caller.

#### GetAtomLabelMonochrome

bool GetAtomLabelMonochrome() const

Returns whether or not the color of the atom label of the highlighted atom(s) is changed.

#### See also:

· OEHighlightByBallAndStick.SetAtomLabelMonochrome method

## **GetBallRadiusScale**

double GetBallRadiusScale() const

Returns the multiplier that can be used to increase or decrease the ball radius of the highlighted atom(s).

#### See also:

· OEHighlightByBallAndStick.SetBallRadiusScale method

#### **GetColor**

const OESystem:: OEColor & GetColor () const

#### See also:

- · OEHighlightByBallAndStick. SetColor method
- OEColor class

#### **GetStickWidthScale**

double GetStickWidthScale() const

Returns the multiplier that can be used to increase or decrease the stick width of the highlighted bond(s).

#### See also:

· OEHighlightByBallAndStick.SetStickWidthScale method

## **SetAtomLabelMonochrome**

void SetAtomLabelMonochrome (bool monochrome)

Sets whether or not to change the color of the atom label of the highlighted atom(s).

**Example** (Figure: Example of using the SetAtomLabelMonochrome method)

highlight = oedepict.OEHighlightByBallAndStick(oechem.OEPinkTint) highlight.SetAtomLabelMonochrome(False)

#### See also:

· OEHighlightByBallAndStick.GetAtomLabelMonochrome method

#### **SetBallRadiusScale**

void SetBallRadiusScale (double ballRadiusScale)

Sets the multiplier that can be used to increase or decrease the ball radius of the highlighted atom(s).

Example (Figure: Example of using the SetBallRadiusScale method)

![](_page_226_Figure_1.jpeg)

Fig. 81: Example of using the SetAtomLabelMonochrome method

![](_page_226_Picture_3.jpeg)

Fig. 82: Example of using the SetBallRadiusScale method

```
highlight = oedepict.OEHighlightByBallAndStick(oechem.OEPinkTint)
highlight.SetBallRadiusScale(4.0)
```

#### See also:

· OEHighlightByBallAndStick.GetBallRadiusScale method

## **SetColor**

void SetColor (const OESystem:: OEColor &color)

Sets the color of the highlighting.

Example (Figure: Example of using the SetColor method)

highlight.SetColor(oechem.OEPinkTint)

- · OEHighlightByBallAndStick.GetColor method
- OEColor class

![](_page_227_Picture_1.jpeg)

Fig. 83: Example of using the SetColor method

## **SetStickWidthScale**

void SetStickWidthScale(double stickWidthScale)

Sets the multiplier that can be used to increase or decrease the stick width of the highlighted bond(s).

Example (Figure: Example of using the SetStickWidthScale method)

highlight = oedepict.OEHighlightByBallAndStick(oechem.OEPinkTint) highlight.SetStickWidthScale(5.0)

![](_page_227_Picture_8.jpeg)

Fig. 84: Example of using the SetStickWidthScale method

#### See also:

· OEHighlightByBallAndStick.GetStickWidthScale method

## 4.1.29 OEHighlightByCogwheel

class OEHighlightByCogwheel : public OEHighlightBase

The OEHighlightByCogwheel class allows the customization of the cogwheel highlighting style that is associated with the OEHighlightStyle\_Cogwheel constant. See example in Figure: Example of highlighting using the 'cogwheel' style.

![](_page_228_Picture_4.jpeg)

### Fig. 85: Example of highlighting using the color style

The OEHighlightByCogwheel class stores the following properties:

| Property          | Get method                    | Set method                    | Corresponding<br>namespace / class / type |
|-------------------|-------------------------------|-------------------------------|-------------------------------------------|
| atom label        | <i>GetAtomLabelMonochrome</i> | <i>SetAtomLabelMonochrome</i> | boolean                                   |
| ball radius scale | <i>GetBallRadiusScale</i>     | <i>SetBallRadiusScale</i>     | floating point number                     |
| color             | <i>GetColor</i>               | <i>SetColor</i>               | <b>OEColor</b>                            |
| inner contour     | <i>GetInnerContour</i>        | <i>SetInnerContour</i>        | boolean                                   |
| line width scale  | <i>GetLineWidthScale</i>      | <i>SetLineWidthScale</i>      | floating point number                     |
| stick width scale | <i>GetStickWidthScale</i>     | <i>SetStickWidthScale</i>     | floating point number                     |

- · OEAddHighlighting function
- · OEHighlightStyle namespace
- OEHighlightByBallAndStick class
- OEHighlightByColor class
- · OEHighlightByLasso class
- OEHighlightByStick class
- Highlighting chapter

#### **Constructors**

```
OEHighlightByCogwheel(const OESystem::OEColor &color, double lineWidthScale=1.5,
                      double stickWidthScale=2.0, double ballRadiusScale=2.0,
                      bool innerContour=true, bool monochrome=true)
```

Creates an OEHighlightByCogwheel object with the specified parameters.

color The color used for highlighting. See also OEHighlightByCogwheel. SetColor method.

- *line WidthScale* The multiplier that can be used to increase or decrease the line width of the 'cogwheel'. See also OEHighlightByCogwheel.SetLineWidthScale method.
- stick Width Scale The multiplier that can be used to increase or decrease the stick width of the 'cogwheel' of the highlighted bond(s). See also OEHighlightByCogwheel. SetStickWidthScale method.
- **ballRadiusScale** The multiplier that can be used to increase or decrease the ball radius of the 'cogwheel' of the highlighted atom(s). See also OEHighlightByCogwheel. SetBallRadiusScale method.
- *innerContour* Defines whether the inner contour of the 'cogwheel' is drawn or committed. See also OEHighlightByCogwheel. SetInnerContour method.
- *monochrome* Defines whether or not to change the color of the atom label of the highlighted atom(s). See also OEHighlightByCogwheel.SetAtomLabelMonochrome method.

OEHighlightByCogwheel(const OEHighlightByCogwheel & rhs)

Copy constructor.

#### operator=

OEHighlightByCogwheel & operator=(const OEHighlightByCogwheel & rhs)

Assignment operator.

### **CreateCopy**

OEHighlightBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEHighlightByCogwheel object is dynamically allocated and owned by the caller.

#### **GetAtomLabelMonochrome**

bool GetAtomLabelMonochrome() const

Returns whether or not the color of the atom label of the highlighted atom(s) is changed.

### See also:

· OEHighlightByCogwheel.SetAtomLabelMonochrome method

## **GetBallRadiusScale**

```
double GetBallRadiusScale() const
```

Returns the multiplier that can be used to increase or decrease the ball radius of the 'cogwheel' of the highlighted  $atom(s)$ .

### See also:

· OEHighlightByCogwheel.SetBallRadiusScale method

## **GetColor**

const OESystem:: OEColor & GetColor () const

Returns the color of the highlighting.

#### See also:

- · OEHighlightByCogwheel.SetColor method
- OEColor class

### **GetInnerContour**

bool GetInnerContour() const

Returns whether the inner contour of the 'cogwheel' is drawn or committed.

#### See also:

· OEHighlightByCogwheel.SetInnerContour method

#### **GetLineWidthScale**

double GetLineWidthScale() const

Returns the multiplier that can be used to increase or decrease the line width of the 'cogwheel'

### See also:

· OEHighlightByCogwheel. SetLineWidthScale method

#### **GetStickWidthScale**

double GetStickWidthScale() const

Returns the multiplier that can be used to increase or decrease the stick width of the 'cogwheel' of the highlighted  $bond(s)$ .

#### See also:

· OEHighlightByCogwheel.SetStickWidthScale method

## SetAtomLabelMonochrome

void SetAtomLabelMonochrome (bool monochrome)

Sets whether or not to change the color of the atom label of the highlighted atom(s).

Example (Figure: Example of using the SetAtomLabelMonochrome method)

highlight = oedepict.OEHighlightByCogwheel(oechem.OEDarkPurple) highlight.SetAtomLabelMonochrome(False)

![](_page_231_Picture_6.jpeg)

#### Fig. 86: Example of using the SetAtomLabelMonochrome method

See also:

· OEHighlightByCogwheel.GetAtomLabelMonochrome method

#### **SetBallRadiusScale**

void SetBallRadiusScale (double ballRadiusScale)

Sets the multiplier that can be used to increase or decrease the ball radius of the 'cogwheel' of the highlighted atom(s).

Example (Figure: Example of using the SetBallRadiusScale method)

```
highlight = oedepict.OEHighlightByCogwheel(oechem.OEDarkPurple)
highlight.SetBallRadiusScale(5.0)
```

#### See also:

· OEHighlightByCogwheel.GetBallRadiusScale method

![](_page_232_Picture_1.jpeg)

Fig. 87: Example of using the SetBallRadiusScale method

## **SetColor**

void SetColor (const OESystem:: OEColor &color)

Sets the color of the highlighting.

Example (Figure: Example of using the SetColor method)

highlight.SetColor(oechem.OEDarkPurple)

![](_page_232_Picture_8.jpeg)

Fig. 88: Example of using the SetColor method

- · OEHighlightByCogwheel.GetColor method
- OEColor class

## **SetInnerContour**

void SetInnerContour (bool innerContour)

Sets whether the inner contour of the 'cogwheel' is drawn or omitted.

**Example** (Figure: Example of using the SetInnerContour method)

```
highlight = oedepict.OEHighlightByCogwheel(oechem.OEDarkPurple)
highlight. SetInnerContour (False)
```

![](_page_233_Picture_6.jpeg)

![](_page_233_Figure_7.jpeg)

#### See also:

· OEHighlightByCogwheel.GetInnerContour method

#### **SetLineWidthScale**

```
void SetLineWidthScale(double lineWidthScale)
```

Sets the multiplier that can be used to increase or decrease the line width of the 'cogwheel'

Example (Figure: Example of using the SetLineWidthScale method)

```
highlight = oedepict.OEHighlightByCogwheel(oechem.OEDarkPurple)
highlight.SetLineWidthScale(3.0)
```

#### See also:

· OEHighlightByCogwheel.GetLineWidthScale method

![](_page_234_Picture_1.jpeg)

Fig. 90: Example of using the SetLineWidthScale method

## **SetStickWidthScale**

void SetStickWidthScale(double stickWidthScale)

Sets the multiplier that can be used to increase or decrease the stick width of the 'cogwheel' of the highlighted bond(s).

Example (Figure: Example of using the SetStickWidthScale method)

highlight = oedepict.OEHighlightByCogwheel(oechem.OEDarkPurple) highlight.SetStickWidthScale(5.0)

![](_page_234_Picture_8.jpeg)

Fig. 91: Example of using the SetStickWidthScale method

#### See also:

· OEHighlightByCogwheel.GetStickWidthScale method

## 4.1.30 OEHighlightByColor

class OEHighlightByColor : public OEHighlightBase

The OEHighlightByColor class allows the customization of the color highlighting style that is associated with the OEHighlightStyle\_Color constant. See example in Figure: Example of highlighting using the 'color' style.

![](_page_235_Figure_4.jpeg)

### Fig. 92: Example of highlighting using the 'color' style

The OEHighlightByColor class stores the following properties:

| Property           | Get method                      | Set method                      | Corresponding class / type |
|--------------------|---------------------------------|---------------------------------|----------------------------|
| external highlight | <i>GetAtomExternalHighlight</i> | <i>SetAtomExternalHighlight</i> | boolean                    |
| color              | <i>GetColor</i>                 | <i>SetColor</i>                 | <b>OEColor</b>             |
| line width scale   | <i>GetLineWidthScale</i>        | <i>SetLineWidthScale</i>        | floating point             |

#### See also:

- · OEAddHighlighting function
- · OEHighlightStyle namespace
- OEHighlightByBallAndStick class
- OEHighlightByCogwheel class
- OEHighlightByLasso class
- OEHighlightByStick class
- Highlighting chapter

### **Constructors**

OEHighlightByColor (const OESystem:: OEColor &color, double lineWidthScale=1.5, **bool** atomExternalHighlight =  $false$ )

Creates an OEHighlightByColor object with the specified parameters.

color The color used for highlighting. See also OEHighlightByColor. SetColor method.

- **line WidthScale** The multiplier that can be used to increase or decrease the line width of highlighted bond(s). See also OEHighlightByColor. SetLineWidthScale method.
- atomExternalHighlight Sets whether atom highlights are extended to bonds not being highlighted. See also OEHighlightByColor.SetAtomExternalHighlight method.

OEHighlightByColor (const OEHighlightByColor & rhs)

Copy constructor.

#### operator=

OEHighlightByColor & operator= (const OEHighlightByColor & rhs)

Assignment operator.

### **CreateCopy**

OEHighlightBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEHighlightByColor object is dynamically allocated and owned by the caller.

#### GetAtomExternalHighlight

bool GetAtomExternalHighlight () const

Returns whether external atom highlight is applied.

### See also:

· OEHighlightByColor. SetAtomExternalHighlight method

### **GetColor**

const OESystem:: OEColor & GetColor () const

Returns the color of the highlighting.

#### See also:

- · OEHighlightByColor.GetColor method
- OEColor class

### **GetLineWidthScale**

double GetLineWidthScale() const

Returns the multiplier that can be used to increase or decrease the line width of highlighted bond(s).

### See also:

· OEHighlightByColor. SetLineWidthScale method

## SetAtomExternalHighlight

void SetAtomExternalHighlight (bool set)

Sets whether atom highlights are extended to bonds not being highlighted.

Example (Figure: Example of using the SetAtomExternalHighlight method)

highlight = oedepict.OEHighlightByColor(oechem.OELightOrange) highlight.SetAtomExternalHighlight(True)

![](_page_237_Picture_6.jpeg)

#### Fig. 93: Example of using the SetAtomExternalHighlight method

#### See also:

· OEHighlightByColor.GetAtomExternalHighlight method

#### **SetColor**

void SetColor (const OESystem:: OEColor &color)

Sets the color of the highlighting.

**Example** (Figure: Example of using the SetColor method)

highlight.SetColor(oechem.OEDarkRed)

- · OEHighlightByColor.GetColor method
- OEColor class

![](_page_238_Picture_1.jpeg)

Fig. 94: Example of using the SetColor method

## **SetLineWidthScale**

void SetLineWidthScale(double lineWidthScale)

Sets the multiplier that can be used to increase or decrease the line width of highlighted bond(s).

Example (Figure: Example of using the SetLineWidthScale method)

highlight = oedepict.OEHighlightByColor(oechem.OEDarkRed) highlight.SetLineWidthScale(3.0)

![](_page_238_Picture_8.jpeg)

Fig. 95: Example of using the SetLineWidthScale method

#### See also:

· OEHighlightByColor.GetLineWidthScale method

## 4.1.31 OEHighlightByLasso

class OEHighlightByLasso : public OEHighlightBase

The OEHighlightByLasso class allows the customization of the lasso highlighting style that is associated with the OEHighlightStyle\_Lasso constant. See example in Figure: Example of highlighting using the 'lasso' style.

![](_page_239_Figure_4.jpeg)

### Fig. 96: Example of highlighting using the 'lasso' style

The OEHighlightByLasso class stores the following properties:

| Property         | Get method                      | Set method                      | Corresponding namespace / class / type |
|------------------|---------------------------------|---------------------------------|----------------------------------------|
| atom label color | GetAtomLabelMonochrome          | SetAtomLabelMonochrome          | boolean                                |
| atom label box   | GetConsiderAtomLabelBoundingBox | SetConsiderAtomLabelBoundingBox | boolean                                |
| color            | GetColor                        | SetColor                        | OEColor                                |
| pen              | GetPen                          | SetPen                          | OEPen                                  |
| position         | GetPosition                     | SetPosition                     | OELayerPosition namespace              |
| lasso scale      | GetLassoScale                   | SetLassoScale                   | floating point number                  |
| line width scale | GetLineWidthScale               | SetLineWidthScale               | floating point number                  |

- · OEAddHighlighting function
- · OEHighlightStyle namespace
- OEHighlightByBallAndStick class
- OEHighlightByColor class
- OEHighlightByCogwheel class
- OEHighlightByStick class
- Highlighting chapter

#### **Constructors**

```
OEHighlightByLasso (const OESystem:: OEColor &color,
                   double lassoScale=3.0,
                   bool monochrome=true,
                   bool considerAtomLabelBox = false,
                   unsigned int position = OELayerPosition:: Below,
                   double lineWidthScale = 1.0)
```

Creates an *OEHighlightByLasso* object with the specified parameters.

color The color used for highlighting. See also  $OEHighLightBylASSO$ .  $SetColor$  method.

- lassoScale The multiplier that can be used to increase or decrease the distance of the "lasso" from the highlighted atom(s) and bond(s). See also OEHighlightByLasso. SetLassoScale method.
- *monochrome* Defines whether or not to change the color of the atom label of the highlighted atom(s). See also OEHighlightByLasso. SetAtomLabelMonochrome method.
- considerAtomLabelBox Determines whether or not to consider the atom label bounding boxes when generating the 'lasso' highlights. See also OEHighlightByLasso. SetConsiderAtomLabelBoundingBox method.
- *position* Defines whether the 'lasso' highlight is going to be rendered below or above the molecule. See also OEHighlightByLasso. SetPosition method.
- *line Width Scale* The multiplier that can be used to increase or decrease the line width of lasso. See also OEHighlightByLasso. SetLineWidthScale method.

OEHighlightByLasso (const OEHighlightByLasso & rhs)

Copy constructor.

#### operator=

OEHighlightByLasso &operator=(const OEHighlightByLasso &rhs)

Assignment operator.

#### **CreateCopy**

OEHighlightBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEHighlightByLasso object is dynamically allocated and owned by the caller.

#### **GetAtomLabelMonochrome**

bool GetAtomLabelMonochrome() const

Returns whether or not the color of the atom label of the highlighted atom(s) is changed.

### See also:

• OEHighlightByLasso. SetAtomLabelMonochrome method

## GetConsiderAtomLabelBoundingBox

bool GetConsiderAtomLabelBoundingBox() const

Returns whether or not to consider the atom label bounding boxes when generating the 'lasso' highlights.

#### See also:

· OEHighlightByLasso. SetConsiderAtomLabelBoundingBox method

## **GetLassoScale**

double GetLassoScale() const

Returns the multiplier that can be used to increase or decrease the distance of the line of the 'lasso' from the highlighted  $atom(s)$  and bonds $(s)$ .

#### See also:

· OEHighlightByLasso. SetLassoScale method

#### **GetLineWidthScale**

double GetLineWidthScale() const

Returns the multiplier that can be used to increase or decrease the line width of the lasso.

#### See also:

· OEHighlightByLasso. SetLineWidthScale method

#### **GetColor**

const OESystem:: OEColor & GetColor () const

Returns the foreground color of the highlighting.

#### See also:

- · OEHighlightByLasso.GetColor method
- OEColor class

#### **GetPen**

const OEPen & GetPen() const

Returns the pen of the highlighting.

- · OEHighlightByLasso. SetPen method
- OEPen class

## **GetPosition**

unsigned int GetPosition() const

Returns whether the 'lasso' highlight is going to be render above or below the molecule. The return value is taken from the OELayerPosition namespace.

### See also:

- · OEHighlightByLasso. SetPosition method
- · OELayerPosition namespace

#### SetAtomLabelMonochrome

void SetAtomLabelMonochrome (bool monochrome)

Sets whether or not to change the color of the atom label of the highlighted atom(s).

Example (Figure: Example of using the SetAtomLabelMonochrome method)

```
highlight = oedepict.OEHighlightByLasso(oechem.OEDarkGreen)
highlight.SetAtomLabelMonochrome(False)
```

![](_page_242_Picture_12.jpeg)

Fig. 97: Example of using the SetAtomLabelMonochrome method

#### See also:

· OEHighlightByLasso.GetAtomLabelMonochrome method

#### SetConsiderAtomLabelBoundingBox

void SetConsiderAtomLabelBoundingBox (bool consider)

Sets whether or not to consider the atom label bounding boxes when generating the 'lasso' highlights. By considering the bounding boxes, the number cases when the lines of the highlight clash with the atom label can be reduced.

Example (Figure: Example of using the SetConsiderAtomLabelBoundingBox method)

highligh = oedepict.OEHighlightByLasso(oechem.OEDarkGreen) highlight.SetConsiderAtomLabelBoundingBox(True)

![](_page_243_Picture_2.jpeg)

#### Fig. 98: Example of using the SetConsiderAtomLabelBoundingBox method

#### See also:

· OEHighlightByLasso. SetConsiderAtomLabelBoundingBox method

### **SetLassoScale**

```
void SetLassoScale (double lassoScale)
```

Sets the multiplier that can be used to increase or decrease the distance of the line of the 'lasso' from the highlighted  $atom(s)$  and bond $(s)$ .

Example (Figure: Example of using the SetLassoScale method)

```
highlight = oedepict.OEHighlightByLasso(oechem.OEDarkGreen)
highlight.SetLassoScale(6.0)
```

![](_page_243_Picture_11.jpeg)

Fig. 99: Example of using the SetLassoScale method

· OEHighlightByLasso.GetLassoScale method

### **SetLineWidthScale**

void SetLineWidthScale (double lineWidthScale)

Sets the multiplier that can be used to increase or decrease the line width of the lasso.

Example (Figure: Example of using the SetLineWidthScale method)

```
highligh = oedepict.OEHighlightByLasso(oechem.OEDarkGreen)
highlight.SetLineWidthScale(3.0)
```

![](_page_244_Picture_7.jpeg)

Fig. 100: Example of using the SetLineWidthScale method

#### See also:

· OEHighlightByLasso.GetLineWidthScale method

## **SetColor**

void SetColor (const OESystem:: OEColor &color)

Sets the foreground color of the highlighting.

Example (Figure: Example of using the SetColor method)

highlight.SetColor(oechem.OEDarkGreen)

- · OEHighlightByLasso. GetColor method
- OEColor class

![](_page_245_Picture_1.jpeg)

Fig. 101: Example of using the SetColor method

## **SetPen**

void SetPen (const OEPen &pen)

Sets the pen of the highlighting.

Example (Figure: Example of using the SetPen method)

pen = oedepict. OEPen (oechem. OEGreenTint, oechem. OEDarkGreen, oedepict.OEFill\_On, 3.0, oedepict.OEStipple\_Dot) highlight.SetPen(pen)

![](_page_245_Picture_8.jpeg)

Fig. 102: Example of using the SetPen method

- · OEHighlightByLasso.GetPen method
- OEPen class

## **SetPosition**

void SetPosition (unsigned int position)

Sets whether the 'lasso' highlight is going to be render above or below the molecule.

*position* This value has to be from the OELayerPosition namespace.

#### See also:

· OEHighlightByLasso.GetPosition method

## 4.1.32 OEHighlightByStick

class OEHighlightByStick : public OEHighlightBase

The OEHighlightByStick class allows the customization of the stick highlighting style that is associated with the OEHighlightStyle\_Stick constant. See example in Figure: Example of highlighting using the 'stick' style.

![](_page_246_Picture_10.jpeg)

Fig. 103: Example of highlighting using the 'stick' style

The OEHighlightByStick class stores the following properties:

| Property           | Get method                           | Set method                           | Corresponding namespace / class / type |
|--------------------|--------------------------------------|--------------------------------------|----------------------------------------|
| external highlight | <i>GetAtomExternalHighlightRatio</i> | <i>SetAtomExternalHighlightRatio</i> | floating point number                  |
| atom label         | <i>GetAtomLabelMonochrome</i>        | <i>SetAtomLabelMonochrome</i>        | boolean                                |
| color              | <i>GetColor</i>                      | <i>SetColor</i>                      | <b>OEColor</b>                         |
| stick width scale  | <i>GetStickWidthScale</i>            | <i>SetStickWidthScale</i>            | floating point number                  |

- · OEAddHighlighting function
- · OEHighlightStyle namespace
- · OEHighlightByBallAndStick class
- OEHighlightByColor class
- OEHighlightByCogwheel class
- OEHighlightByLasso class
- Highlighting chapter

### **Constructors**

```
OEHighlightByStick(const OESystem:: OEColor &color, double stickWidthScale=3.0,
                   bool monochrome=true, double atomExternalHighlightRatio=0.0)
```

Creates an OEHighlightByStick object with the specified parameters.

color The color used for highlighting. See also OEHighlightByStick. SetColor method.

- stickWidthScale The multiplier that can be used to increase or decrease the stick width of the highlighted bond(s). See also OEHighlightByStick. SetStickWidthScale method.
- *monochrome* Defines whether or not to change the color of the atom label of the highlighted atom(s). See also OEHighlightByStick.SetAtomLabelMonochrome method.
- atomExternalHighlightRatio A ratio that can be used to extend atom highlights to bonds not being highlighted. See also OEHighlightByStick.SetAtomExternalHighlightRatio method.

OEHighlightByStick (const OEHighlightByStick & rhs)

Copy constructor.

#### operator=

OEHighlightByStick & operator=(const OEHighlightByStick & rhs)

Assignment operator.

#### **CreateCopy**

OEHighlightBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEHighlightByStick object is dynamically allocated and owned by the caller.

### GetAtomExternalHighlightRatio

double GetAtomExternalHighlightRatio() const

Returns the ratio of the external highlight of the atoms.

#### See also:

· OEHighlightByStick.SetAtomExternalHighlightRatio method

## GetAtomLabelMonochrome

bool GetAtomLabelMonochrome() const

Returns whether or not the color of the atom label of the highlighted atom(s) is changed.

#### See also:

· OEHighlightByStick. SetAtomLabelMonochrome method

### **GetColor**

const OESystem:: OEColor & GetColor () const

Returns the color of the highlighting.

#### See also:

- · OEHighlightByStick. SetColor method
- OEColor class

#### **GetStickWidthScale**

double GetStickWidthScale() const

Returns the multiplier that can be used to increase or decrease the stick width of the highlighted bond(s).

#### See also:

· OEHighlightByStick. SetStickWidthScale method

### SetAtomExternalHighlightRatio

void SetAtomExternalHighlightRatio (bool ratio)

Sets the ratio of the external highlight of the atoms *i.e.* atom highlights are extended to bonds not being highlighted.

*ratio* This value has to be in the range of  $[0.0, 0.5]$ .

Example (Figure: Example of using the SetAtomExternalHighlightRatio method)

highlight = oedepict.OEHighlightByStick(oechem.OELightOrange) highlight.SetAtomExternalHighlightRatio(0.33)

#### See also:

· OEHighlightByStick.GetColor method

![](_page_249_Picture_1.jpeg)

Fig. 104: Example of using the SetAtomExternalHighlightRatio method

![](_page_249_Figure_3.jpeg)

Fig. 105: Example of scaling the 'Stick' style highlighting along with the molecule

### SetAtomLabelMonochrome

void SetAtomLabelMonochrome (bool monochrome)

Sets whether or not to change the color of the atom label of the highlighted atom(s).

Example (Figure: Example of using the SetAtomLabelMonochrome method)

```
highlight = oedepict.OEHighlightByStick(oechem.OELightOrange)
highlight.SetAtomLabelMonochrome(False)
```

#### See also:

· OEHighlightByStick.GetAtomLabelMonochrome method

![](_page_250_Picture_1.jpeg)

### Fig. 106: Example of using the SetAtomLabelMonochrome method

## **SetColor**

void SetColor (const OESystem:: OEColor &color)

Sets the color of the highlighting.

Example (Figure: Example of using the SetColor method)

highlight.SetColor(oechem.OELightOrange)

![](_page_250_Picture_8.jpeg)

Fig. 107: Example of using the SetColor method

- · OEHighlightByStick.GetColor method
- OEColor class

## **SetStickWidthScale**

void SetStickWidthScale(double stickWidthScale)

Sets the multiplier that can be used to increase or decrease the stick width of the highlighted bond(s).

Example (Figure: Example of using the SetStickWidthScale method)

```
highlight = oedepict.OEHighlightByStick(oechem.OELightOrange)
highlight.SetStickWidthScale(5.0)
```

![](_page_251_Picture_6.jpeg)

![](_page_251_Figure_7.jpeg)

See also:

· OEHighlightByStick.GetStickWidthScale method

## 4.1.33 OEHighlightLabel

class OEHighlightLabel

The OEHighlightLabel class allows the customization the style of the label that can be position on molecule depiction by calling the OEAddLabe1 function.

The OEHighlightLabel class stores the following properties:

| Property         | Get method               | Set method                                     | Corresponding<br>namespace<br>class / type                            |
|------------------|--------------------------|------------------------------------------------|-----------------------------------------------------------------------|
| text             | <i>GetText</i>           | <i>OEHighlightLabel</i><br><i>constructors</i> | string                                                                |
| bounding box pen | <i>GetBoundingBoxPen</i> | <i>SetBoundingBoxPen</i>                       | <i>OEPen</i>                                                          |
| label font       | <i>GetFont</i>           | <i>SetFont</i>                                 | <i>OEFont</i>                                                         |
| label font scale | <i>GetFontScale</i>      | <i>SetFontScale</i>                            | positive floating point number in the range of $[0.25, 1.5]$ or $0.0$ |

## **Constructors**

OEHighlightLabel (const std::string &text)

Creates an OEHighlightLabel object with default style.

text The text that is going to be positioned on the molecule depiction.

#### **Example:**

```
label = oedepict.OEHighlightLabel('match')
```

![](_page_252_Picture_7.jpeg)

#### Fig. 109: Example of adding label with default style

OEHighlightLabel (const std:: string &text, const OEFont &font)

Creates an OEHighlightLabel object with user-defined font.

text The text that is going to be positioned on the molecule depiction.

font The OEFont object that encapsulates properties that determine the display style of text.

#### See also:

• OEFont class

#### **Example:**

```
font = oedepict.OEFont(oedepict.OEFontFamily_Courier, oedepict.OEFontStyle_Bold, 12,
                       oedepict.OEAlignment_Center, oechem.OEDarkRed)
label = oedepict.OEHighlightLabel('match', font)
```

OEHighlightLabel (const std::string &text, const OESystem::OEColor &color)

Creates an OEHighlightLabel object with user-defined border color.

text The text that is going to be positioned on the molecule depiction.

color The color of the border around the label.

#### **Example:**

![](_page_253_Figure_1.jpeg)

Fig. 110: Example of adding label with user-defined font

![](_page_253_Figure_3.jpeg)

Fig. 111: Example of adding label with user-defined border color

label = oedepict.OEHighlightLabel('match', oechem.OEDarkRed)

#### See also:

• OEColor class

## **GetBoundingBoxPen**

const OEPen & GetBoundingBoxPen() const

Returns the pen that is used to draw a border around the label.

- OEPen class
- · SetBoundingBoxPen method

## **GetFont**

const OEFont & GetFont () const

Returns the font of the label.

### See also:

- OEFont class
- · OEHighlightLabel. SetFont method

## **GetFontScale**

```
double GetFontScale() const
```

Returns the multiplier that can be used to increase or decrease the font size of the label relative to the font size used to render labels of the of the depicted molecule. The default value is 0.75.

#### See also:

- OEFont class
- · OEHighlightLabel. SetFontScale method

## **GetText**

std::string GetText() const

Returns the text of the label.

#### **SetBoundingBoxPen**

void SetBoundingBoxPen (const OEPen &pen)

Sets the pen that is used to draw a border around the label.

#### **Example:**

```
label = oedepict.OEHighlightLabel('match')
pen = oedepict.OEPen(oechem.OEColor(255, 220, 220), oechem.OEDarkRed, oedepict.OEFill_
\rightarrowOn, 16.0,
                      oedepict.OEStipple_ShortDash)
label.SetBoundingBoxPen(pen)
```

#### See also:

• OEPen class

![](_page_255_Picture_1.jpeg)

Fig. 112: Example of adding label with user-defined border

## **SetFont**

void SetFont (const OEFont & font)

Set the font of the label.

#### **Example:**

```
label = oederiot. OEHighthightLabel('match')font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
\leftrightarrow12,
                        oedepict.OEAlignment_Center, oechem.OEDarkRed)
label.SetFont(font)
```

![](_page_255_Picture_8.jpeg)

Fig. 113: Example of adding label with user-defined font

Note: The size of fonts of the label depends on:

- the size of the font used to render atom labels of the the depicted molecule
- the multiplier set by the OEHighlightLabel. SetFontScale method

• OEFont class

## **SetFontScale**

```
void SetFontScale (double scale)
```

Sets the multiplier that can be used to increase or decrease the font size of the label relative to the font size used to render atom labels of the of the depicted molecule.

scale This value has to be either  $0.0$  or in a range of  $[0.25, 1.50]$ . The default value is  $0.75$ .

In case of  $0.0$ , the label is not scaled with the molecule but rather fixed font size is used regardless of the size of the depicted molecule.

#### **Example:**

```
label = oedepict.OEHighlightLabel('match')
label.SetFontScale(1.2)
```

![](_page_256_Figure_9.jpeg)

Fig. 114: Example of adding label with user-defined font scaling

## 4.1.34 OEHighlightOverlayBase

#### class OEHighlightOverlayBase

The OEHighlightOverlayBase is an abstract class used for highlighting a set of atoms and/or bonds.

The following classes derive from this class:

• OEHighlightOverlayByBallAndStick

- · OEAddHighlightOverlay function
- Highlighting Overlapped Patterns section

### **Constructors**

```
OEHighlightOverlayBase()
OEHighlightOverlayBase(OEHighlightOverlayBaseImpl *impl)
```

Default constructors.

### **GetColors**

OESystem::OEIterBase<OESystem::OEColor> \*GetColors() const

Returns an iterator over the colors used for highlighting.

### **SetColors**

```
void SetColors (OESystem:: OEIter<OESystem:: OEColor> &colors)
void SetColors (OESystem::OEIterBase<OESystem::OEColor> *colors)
```

Sets the colors used for highlighting.

## 4.1.35 OEHighlightOverlayByBallAndStick

class OEHighlightOverlayByBallAndStick : public OEHighlightOverlayBase

The OEHighlightOverlayByBallAndStick class allows the customization of the **ball and stick** highlighting style that is associated with the OEHighlightOverlayStyle\_BallAndStick constant. This style enables the highlighting of overlapping patterns. See example in Figure: Example of overlay highlighting using the 'ball and stick' style.

![](_page_257_Picture_13.jpeg)

Fig. 115: Example of overlay highlighting using the 'ball and stick' style

#### See also:

- · OEAddHighlightOverlay function.
- · OEHighlightOverlayStyle namespace
- Highlighting Overlapped Patterns section

Note: It is recommended to select colors with high contrast when highlighting overlapped patterns with the OEHighlightOverlayByBallAndStick class.

· OEGetContrastColors function

The following methods are publicly inherited from OEHighlightOverlayBase:

GetColors SetColors

### **Constructors**

```
OEHighlightOverlayByBallAndStick(OESystem::OEIter<OESystem::OEColor>&colors,
                                 double stickWidthScale=3.0,
                                 double ballRadiusScale=3.0,
                                 bool monochrome=true)
OEHighlightOverlayByBallAndStick(OESystem::OEIterBase<OESystem::OEColor> *colors,
                                 double stickWidthScale=3.0,
                                 double ballRadiusScale=3.0,
                                 bool monochrome=true)
```

Creates an OEHighlightOverlayByBallAndStick object with the specified parameters

colors The colors used for highlighting. See also OEHighlightOverlayBase. SetColors method.

- stick Width Scale The multiplier that can be used to increase or decrease the stick width of the highlighted bond(s). See also OEHighlightOverlayByBallAndStick.SetStickWidthScale method.
- **ballRadiusScale** The multiplier that can be used to increase or decrease the ball radius of the highlighted atoms(s). See also OEHighlightOverlayByBallAndStick. SetBallRadiusScale method.
- *monochrome* Defines whether or not to change the color of the atom label of the highlighted atom(s). See also OEHighlightOverlayByBallAndStick.SetAtomLabelMonochrome method.

OEHighlightOverlayByBallAndStick(const OEHighlightOverlayByBallAndStick & rhs)

Copy constructor.

#### operator=

```
OEHighlightOverlayByBallAndStick &
 operator=(const OEHighlightOverlayByBallAndStick & rhs)
```

Assignment operator.

#### **GetAtomLabelMonochrome**

bool GetAtomLabelMonochrome() const

Returns whether or not the color of the atom label of the highlighted atom(s) is changed.

See also:

· OEHighlightOverlayByBallAndStick.SetAtomLabelMonochrome method

### **GetBallRadiusScale**

double GetBallRadiusScale() const

Returns the multiplier that can be used to increase or decrease the ball radius of the highlighted atoms(s).

#### See also:

· OEHighlightOverlayByBallAndStick.SetBallRadiusScale method

### **GetStickWidthScale**

double GetStickWidthScale() const

Returns the multiplier that can be used to increase or decrease the stick width of the highlighted bond(s).

#### See also:

· OEHighlightOverlayByBallAndStick.SetStickWidthScale method

#### **SetAtomLabelMonochrome**

void SetAtomLabelMonochrome (bool monochrome)

Sets whether or not to change the color of the atom label of the highlighted atom(s).

Example (Figure: Example of using the SetAtomLabelMonochrome method)

```
highlight = oedepict.OEHighlightOverlayByBallAndStick(oechem.OEGetVividColors())
highlight.SetAtomLabelMonochrome(False)
```

![](_page_259_Picture_16.jpeg)

#### Fig. 116: Example of using the SetAtomLabelMonochrome method

### See also:

· OEHighlightOverlayByBallAndStick.GetAtomLabelMonochrome method

## **SetBallRadiusScale**

void SetBallRadiusScale (double ballRadiusScale)

Sets the multiplier that can be used to increase or decrease the ball radius of the highlighted atoms(s).

**Example** (Figure: Example of using the SetBallRadiusScale method)

```
highlight = oedepict.OEHighlightOverlayByBallAndStick(oechem.OEGetVividColors())
highlight.SetBallRadiusScale(4.0)
```

![](_page_260_Picture_6.jpeg)

Fig. 117: Example of using the SetBallRadiusScale method

#### See also:

· OEHighlightOverlayByBallAndStick.GetBallRadiusScale method

### **SetStickWidthScale**

```
void SetStickWidthScale(double stickWidthScale)
```

Sets the multiplier that can be used to increase or decrease the stick width of the highlighted bond(s).

Example (Figure: Example of using the SetStickWidthScale method)

```
highlight = oedepict.OEHighlightOverlayByBallAndStick(oechem.OEGetVividColors())
highlight.SetStickWidthScale(5.0)
```

#### See also:

· OEHighlightOverlayByBallAndStick.GetStickWidthScale method

![](_page_261_Picture_1.jpeg)

### Fig. 118: Example of using the SetStickWidthScale method

## 4.1.36 OEImage

#### class OEImage : public OEImageBase

OEImage class is implemented as a **display list** i.e. a container of drawing commands. For example, when the  $OEImage$ .  $DrawLine$  method is called, rather than immediately drawing a line specified by the parameters, a line drawing operation is created that copies all parameters for later execution.

When the OEImage. Render method is invoked, the drawing commands stored in the OEImage object are executed in the same order in which they were issued.

| Clear           | DrawPie             | DrawTriangle    |
|-----------------|---------------------|-----------------|
| DrawArc         | DrawPoint           | GetGlobalOffset |
| DrawCircle      | DrawPolygon         | GetHeight       |
| DrawCubicBezier | DrawQuadraticBezier | GetMinFontSize  |
| DrawLine        | DrawRectangle       | GetWidth        |
| DrawPath        | DrawText            | GetSVGClass     |
| GetSVGGroup     | GetSVGGroups        | NewSVGClass     |
| NewSVGGroup     | PopGroup            | PushGroup       |
| SetMinFontSize  |                     |                 |

The following methods are publicly inherited from OEImageBase:

### **Constructors**

OEImage (double width, double height, const OESystem:: OEColor& bgColor =  $\rightarrow$  OESystem: : OEWhite) ;

Default constructor that creates an OEImage with the specified width and height.

width, height The dimensions of the image, both have to be positive (non-zero) numbers.

**bgColor** The color that is used to clear the image upon construction. The default background color is OEWhite. A .png image with transparent background can be generated by passing the OETransparent Color as the background color.

OEImage (const OEImage & rhs)

Copy constructor.

OEImage (const OEImage &src, double scale)

Copy constructor with scaling.

scale The scaling factor is used to create a new image from the given one. The scaling factor has to be a positive (non-zero) number.

The following code snippet shows how to half and double the size of an image.

```
image = odeplot.OEImage(100.0, 100.0)image.DrawCircle(oedepict.OEGetCenter(image), 40.0, oedepict.OEBlackPen)
image.DrawText(oedepict.OEGetCenter(image), "circle", oedepict.OEDefaultFont)
oedepict.OEDrawBorder(image, oedepict.OELightGreyPen)
oedepict.OEWriteImage("image.png", image)
halfimage = oedepict.OEImage(image, 0.5)oedepict.OEWriteImage("halfimage.png", halfimage)
doubleimage = oedepict. OEImage (image, 2.0)
oedepict.OEWriteImage("doubleimage.png", doubleimage)
```

![](_page_262_Figure_8.jpeg)

#### Table 7: Examples of image scaling

**Clear** 

void Clear (const OESystem:: OEColor &color)

Appends a clear command to the display list of the OEImage object.

- · OEImageBase. Clear method
- OEColor class

### **DrawArc**

```
void DrawArc (const OE2DPoint &center, double bgnAngle, double endAngle,
             double radius, const OEPen &pen)
```

Appends an arc drawing command to the display list of the OEImage object. See example in Figure: Example of drawing an arc.

![](_page_263_Figure_4.jpeg)

#### Fig. 119: Example of drawing an arc

#### See also:

- · OEImageBase. DrawArc method
- OE2DPoint class
- OEPen class

## **DrawCircle**

void DrawCircle (const OE2DPoint & center, double radius, const OEPen & pen)

Appends a circle drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a circle.

![](_page_263_Figure_13.jpeg)

Fig. 120: Example of drawing a circle

- · OEImageBase. DrawCircle method
- OE2DPoint class
- OEPen class

## **DrawCubicBezier**

```
void DrawCubicBezier (const OE2DPoint &bgn, const OE2DPoint &c1,
                     const OE2DPoint &c2, const OE2DPoint &end, const OEPen &pen)
```

Appends a cubic Bézier curve drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a cubic Bezier curve.

![](_page_264_Figure_4.jpeg)

#### Fig. 121: Example of drawing a cubic Bezier curve

#### See also:

- · OEImageBase. DrawCubicBezier method
- OE2DPoint class
- OEPen classes

### **DrawLine**

void DrawLine (const OE2DPoint &bgn, const OE2DPoint &end, const OEPen &pen)

Appends a line drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a line.

![](_page_264_Figure_13.jpeg)

Fig. 122: Example of drawing a line

- · OEImageBase. DrawLine method
- OE2DPoint class
- OEPen class

## **DrawPath**

void DrawPath (const OE2DPath& path, const OEPen& pen) ;

Appends a path drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a path.

![](_page_265_Figure_4.jpeg)

### Fig. 123: Example of drawing a path

### See also:

- · OEImageBase. DrawPath method
- OE2DPath class
- OEPen class

### **DrawPie**

![](_page_265_Figure_11.jpeg)

Appends a pie drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a pie.

![](_page_265_Figure_13.jpeg)

#### Fig. 124: Example of drawing a pie

- · OEImageBase. DrawPie method
- OE2DPoint class
- OEPen class

## **DrawPoint**

void DrawPoint (const OE2DPoint &p, const OESystem:: OEColor &color)

Appends a point drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a point.

![](_page_266_Figure_4.jpeg)

#### Fig. 125: Example of drawing a point

#### See also:

- · OEImageBase. DrawPoint method
- OE2DPoint class
- OEColor class

## **DrawPolygon**

void DrawPolygon (const std::vector<OE2DPoint> &points, const OEPen &pen)

Appends a polygon drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a polygon.

![](_page_266_Figure_13.jpeg)

Fig. 126: Example of drawing a polygon

- · OEImageBase. DrawPolygon method
- OE2DPoint class
- OEPen class

### **DrawQuadraticBezier**

```
void DrawQuadraticBezier (const OE2DPoint &bgn, const OE2DPoint &c,
                         const OE2DPoint & end, const OEPen & pen)
```

Appends a quadratic Bézier curve drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a quadratic Bezier curve.

![](_page_267_Figure_4.jpeg)

### Fig. 127: Example of drawing a quadratic Bezier curve

#### See also:

- · OEImageBase. DrawQuadraticBezier method
- OE2DPoint class
- OEPen classes

#### **DrawRectangle**

void DrawRectangle (const OE2DPoint &tl, const OE2DPoint &br, const OEPen &pen)

Appends a polygon drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a rectangle.

![](_page_267_Figure_13.jpeg)

#### Fig. 128: Example of drawing a rectangle

- · OEImageBase. DrawRectangle method
- OE2DPoint class
- OEPen class

## **DrawText**

```
void DrawText (const OE2DPoint &c, const std::string &text, const OEFont &font,
              double maxwidth=0.0)
```

Appends a text drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a text.

![](_page_268_Picture_4.jpeg)

#### Fig. 129: Example of drawing a text

#### See also:

- · OEImageBase. DrawText method
- OE2DPoint class
- OEFont class

#### **DrawTriangle**

```
void DrawTriangle (const OE2DPoint &a, const OE2DPoint &b, const OE2DPoint &c,
                  const OEPen &pen)
```

Appends a triangle drawing command to the display list of the OEImage object. See example in Figure: Example of drawing a triangle.

![](_page_268_Figure_13.jpeg)

Fig. 130: Example of drawing a triangle

- · OEImageBase. DrawTriangle method
- OE2DPoint class
- OEPen class

### **GetHeight**

double GetHeight () const

Returns the height of the OEImage object.

#### **GetWidth**

double GetWidth() const

Returns the width of the OEImage object.

### **IsEmpty**

bool IsEmpty() const

Returns whether or not the display list of the OEImage object is empty.

#### **Render**

**bool** Render (OEImageBase &image) const

Renders the image stored in the OEImage object by executing the stored drawing commands in the order in which they were issued.

## 4.1.37 OEImageBase

class OEImageBase

The OEImageBase is an abstract class that provides methods for drawing basic geometric shapes such as lines, circles, rectangles etc.

The following classes derive from this class:

- OEImage
- OEImageFrame

### **Constructors**

OEImageBase(double width=200.0, double height=200.0)

Default constructor that creates an image with the specified width and height.

width, height The dimensions of the image, both have to be positive (non-zero) numbers.

**Clear** 

void Clear (const OESystem:: OEColor &color=OESystem:: OEWhite)

Clears the image with the given color.

#### See also:

• OEColor class

#### **DrawArc**

```
void DrawArc (const OE2DPoint &center, double bgnAngle, double endAngle,
             double radius, const OEPen &pen)
```

Draws the outline of an arc. See example in Figure: Example of arc.

![](_page_270_Figure_9.jpeg)

![](_page_270_Figure_10.jpeg)

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc (in degrees). Both angles are in degrees and their values have to be in a range of  $[0.0^\circ, 360.0^\circ]$ . Angles are interpreted such that  $0.0^\circ$  and  $360.0^\circ$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

**pen** The graphical properties of the curve (such as color, line width, etc). See examples in *Figure: Example of drawing* arcs with various pens.

![](_page_270_Figure_15.jpeg)

Fig. 132: Example of drawing arcs with various pens

**Note:** OEImageBase.DrawArc supports all the OEPen properties (i.e. color, line width, line stipple) except the fill property. See also OEImageBase. DrawPie method.

Arcs are always drawn in a clockwise direction. This means that  $\text{bgn} = 0.0^{\circ}$ , end = 90.0° angle pair is not the same as bgn =  $90.0^{\circ}$ , end =  $0.0^{\circ}$  angle pair. See examples in Table: Example of interpreting the begin and end angles of the arc.

![](_page_271_Figure_1.jpeg)

Table 8: Example of interpreting the begin and end angles of the arc

#### See also:

- OE2DPoint class
- OEPen class

## **DrawCircle**

void DrawCircle (const OE2DPoint &center, double radius, const OEPen &pen)

Draws a circle. See example in Figure: Example of circle.

![](_page_271_Figure_9.jpeg)

Fig. 133: Example of circle

center The center of the circle.

*radius* The radius of the circle.

pen The graphical properties of the circle (such as color, line width, etc). See examples in Figure: Example of drawing circles with various pens.

![](_page_271_Figure_14.jpeg)

Fig. 134: Example of drawing circles with various pens

### See also:

• OE2DPoint class

• OEPen class

## **DrawCubicBezier**

```
void DrawCubicBezier (const OE2DPoint & bgn, const OE2DPoint &c1,
                     const OE2DPoint &c2, const OE2DPoint &end, const OEPen &pen)
```

Draws a cubic Bézier curve. See example in Figure: Example of cubic Bezier curve.

![](_page_272_Figure_5.jpeg)

Fig. 135: Example of cubic Bezier curve

- bgn, end The end points of the Bezier curve.
- $c1$ ,  $c2$  The control points of the curve.
- **pen** The graphical properties of the Bézier curve (such as color, line width, etc). See examples in Figure: Example of drawing cubic Bezier curves with various pens.

![](_page_272_Figure_10.jpeg)

Fig. 136: Example of drawing cubic Bezier curves with various pens

Example (Figure: Example of drawing a cubic Bezier curve)

```
image = odeplot.OEImage(100, 100)b = oedepict. OE2DPoint (20, 70)
e = oedepict. OE2DPoint (60, 70)
c1 = b + oedgepicture.CE2DPoint(50, -60)c2 = e + oedepict.OE2DPoint (50, -60)pen = oedepict.OEPen(oechem.OELightGreen, oechem.OEBlack, oedepict.OEFill_On, 2.0)
image.DrawCubicBezier(b, c1, c2, e, pen)
```

- OE2DPoint class
- OEPen classes

![](_page_273_Picture_1.jpeg)

## Fig. 137: Example of drawing a cubic Bezier curve

### **DrawLine**

void DrawLine (const OE2DPoint &bgn, const OE2DPoint &end, const OEPen &pen)

Draws a line. See example in Figure: Example of line.

![](_page_273_Figure_6.jpeg)

Fig. 138: Example of line

bgn, end The two endpoints of the line.

pen The graphical properties of the line (such as color, line width, etc). See examples in Figure: Example of drawing lines with various pens.

![](_page_273_Figure_10.jpeg)

Fig. 139: Example of drawing lines with various pens

- OE2DPoint class
- OEPen class

### **DrawPath**

![](_page_274_Figure_2.jpeg)

Fig. 140: Example of path

- **path** The OE2DPath object that defines a path as a sequence of lines and curves.
- pen The graphical properties of the pie (such as color, line width, etc). See examples in Figure: Example of drawing paths with various pens.

![](_page_274_Figure_6.jpeg)

Fig. 141: Example of drawing paths with various pens

Example (Figure: Example of drawing a path)

```
image = odeplot.OEImage(100, 100)path = oedepict. OE2DPath (oedepict. OE2DPoint (20, 80))
path.AddLineSegment(oedepict.OE2DPoint(80, 80))
path.AddLineSegment(oedepict.OE2DPoint(80, 40))
path.AddCurveSegment(oedepict.OE2DPoint(80, 10), oedepict.OE2DPoint(20, 10),
                     oedepict.OE2DPoint(20, 40))
pen = oedepict.OEPen(oechem.OELightGreen, oechem.OEBlack, oedepict.OEFill_On, 2.0)
image.DrawPath(path, pen)
```

- OE2DPath class
- OEPen class

![](_page_275_Picture_1.jpeg)

### Fig. 142: Example of drawing a path

### **DrawPie**

```
void DrawPie (const OE2DPoint & center, double bgnAngle, double endAngle,
             double radius, const OEPen &pen)
```

Draws a pie. See example in Figure: Example of drawing a pie.

![](_page_275_Figure_6.jpeg)

center The center of the pie.

bgnAngle, endAngle The two endpoints of the pie (in degrees). Both angles are in degrees and their values have to be in a range of  $[0.0^\circ, 360.0^\circ]$ . Angles are interpreted such that  $0.0^\circ$  and  $360.0^\circ$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the pie.

**pen** The graphical properties of the pie (such as color, line width, etc). See examples in *Figure: Example of drawing* pies with various pens.

![](_page_275_Figure_11.jpeg)

Fig. 143: Example of drawing pies with various pens

Pies are always drawn in a clockwise direction. This means that  $\text{bgn} = 0.0^{\circ}$ , end = 90.0° angle pair is not the same as bgn =  $90.0^{\circ}$ , end =  $0.0^{\circ}$  angle pair. See examples in Table: Example of interpreting the begin and end angles of the pie.

![](_page_276_Figure_1.jpeg)

Table 9: Example of interpreting the begin and end angles of the pie

#### See also:

- OE2DPoint class
- OEPen class

#### **DrawPoint**

**void** DrawPoint (const OE2DPoint &p, const OESystem:: OEColor &color) = 0

Draws a point. See example in Figure: Example of point.

![](_page_276_Figure_9.jpeg)

![](_page_276_Figure_10.jpeg)

**p** The position of the point, where  $p =$  OE2DPoint(x, y).

color The color of the point.

#### See also:

• OEColor class

### **DrawPolygon**

void DrawPolygon (const std:: vector<OE2DPoint> &points, const OEPen &pen)

Draws a closed polygon. See example in Figure: Example of polygon.

- *points* The series of points that defines the polygon. The polygon will be closed *i.e.* the first connected with the last point.
- **pen** The graphical properties of the polygon (such as color, line width, etc). See examples in Figure: Example of polygons lines with various pens.

![](_page_277_Figure_1.jpeg)

Fig. 146: Example of drawing polygons with various pens

Example (Figure: Example of drawing a polygon)

```
image = odeplot.OEImage(100, 100)polygon = []polygon.append(oedepict.OE2DPoint(20, 20))
polygon.append(oedepict.OE2DPoint(40, 40))
polygon.append(oedepict.OE2DPoint(60, 20))
polygon.append(oedepict.OE2DPoint(80, 40))
polygon.append(oedepict.OE2DPoint(80, 80))
polygon.append(oedepict.OE2DPoint(20, 80))
pen = oedepict.OEPen(oechem.OELightGreen, oechem.OEBlack, oedepict.OEFill_On, 2.0)
image.DrawPolygon(polygon, pen)
```

![](_page_277_Picture_5.jpeg)

Fig. 147: Example of drawing a polygon

- $\bullet$  *OE2DPoint* class
- OEPen class

## **DrawQuadraticBezier**

```
void DrawQuadraticBezier (const OE2DPoint & bgn, const OE2DPoint &c,
                         const OE2DPoint &end, const OEPen &pen)
```

Draws a quadratic Bézier curve. See example in Figure: Example of quadratic Bezier curve.

![](_page_278_Figure_4.jpeg)

Fig. 148: Example of quadratic Bezier curve

bgn, end The end points of the Bézier curve.

- $c$  The control point of the curve.
- **pen** The graphical properties of the Bézier curve (such as color, line width, etc). See examples in Figure: Example of drawing quadratic Bezier curves with various pens.

![](_page_278_Figure_9.jpeg)

Fig. 149: Example of drawing quadratic Bezier curves with various pens

Example (Figure: Example of drawing a polygon)

```
image = odeplot.OEImage(100, 100)b = oedepict. OE2DPoint (20, 70)
e = oedepict. OE2DPoint (80, 70)
c = b + oedgepicture.CE2DPoint(30, -80)pen = oedepict.OEPen(oechem.OELightGreen, oechem.OEBlack, oedepict.OEFill_On, 2.0)
image.DrawQuadraticBezier(b, c, e, pen)
```

- OE2DPoint class
- OEPen classes

![](_page_279_Picture_1.jpeg)

## Fig. 150: Example of drawing a quadratic Bezier

## **DrawRectangle**

void DrawRectangle (const OE2DPoint &tl, const OE2DPoint &br, const OEPen &pen)

Draws a rectangle. See example in Figure: Example of rectangle.

![](_page_279_Figure_6.jpeg)

Fig. 151: Example of rectangle

- $tl$  The top left corner of the rectangle.
- br The bottom right corner of the rectangle.
- **pen** The graphical properties of the rectangle (such as color, line width, etc). See examples in *Figure: Example of* polygons rectangles with various pens.

![](_page_279_Figure_11.jpeg)

Fig. 152: Example of drawing rectangles with various pens

- OE2DPoint class
- OEPen class

### **DrawText**

```
void DrawText (const OE2DPoint &center, const std::string &text, const OEFont &font,
              double maxwidth=0.0)
```

Draws a text. See example in Figure: Example of text.

# $<sub>C</sub>$ </sub>

#### Fig. 153: Example of text

*center* The position of the text.

text The characters to be displayed.

- font The graphical properties of the displayed text (such as color, font size, etc). See examples in Figure: Example of drawing texts with various fonts.
- *maxwidth* If *maxwidth* is specified and the width of the text would exceed the given limit, than the size of the font used to display the text is automatically reduced.

Note: The displayed position of the text not only depends on 'c' position but also the alignment style of the given OEFont.

![](_page_280_Picture_11.jpeg)

#### Fig. 154: Example of drawing texts with various fonts

- OE2DPoint class
- OEAlignment namespace
- OEFont class

## **DrawTriangle**

```
void DrawTriangle (const OE2DPoint &a, const OE2DPoint &b, const OE2DPoint &c,
                  const OEPen &pen)
```

Draws a triangle. See example in Figure: Example of triangle.

![](_page_281_Figure_4.jpeg)

Fig. 155: Example of triangle

- $a, b, c$  The three corners of the triangle.
- pen The graphical properties of the triangle (such as color, line width, etc). See examples in Figure: Example of polygons triangles with various pens.

![](_page_281_Figure_8.jpeg)

Fig. 156: Example of drawing triangles with various fonts

## See also:

- OE2DPoint class
- OEPen class

## **GetGlobalOffset**

const OE2DPoint& GetGlobalOffset() const

Returns the offset from the origin  $(x=0.0, y=0.0)$  to the top-left corner of the given image.

#### **GetHeight**

double GetHeight () const

Returns the height of the OEImageBase object.

### **GetMinFontSize**

unsigned int GetMinFontSize() const

Returns the minimum size of the font that can be displayed.

#### **GetWidth**

double GetWidth() const

Returns the width of the OEImageBase object.

#### **SetMinFontSize**

void SetMinFontSize (unsigned int fontsize)

Sets the minimum size of the font that can be displayed.

## **GetSVGClass**

```
OESVGClass *GetSVGClass (const std::string &name)
const OESVGClass *GetSVGClass (const std::string &name) const
```

Returns the OESVGClass object with the given name. Null pointer will be returned if no class exists on the image with the given name.

- Generating Interactive SVG Images chapter
- OESVGClass class

#### **GetSVGGroup**

```
OESVGGroup *GetSVGGroup (const std::string &id)
const OESVGGroup *GetSVGGroup (const std::string &id) const
```

Returns the OESVGGroup object with the given name. Null pointer will be returned if no group exists on the image with the given name.

#### See also:

- Generating Interactive SVG Images chapter
- OESVGGroup class

### **GetSVGGroups**

OESystem:: OEIterBase<OESVGGroup>\* GetSVGGroups()

Returns an iterator over the SVG groups (OESVGGroup) of the image.

#### **Example:**

```
for g in image. GetSVGGroups () :
    print(q.CetId())
```

#### See also:

- Generating Interactive SVG Images chapter
- OESVGGroup class

### **NewSVGClass**

OESVGClass \*NewSVGClass (const std::string &name)

Creates a new OESVGClass on the given image. A null pointer will be returned and warning message will be thrown if the SVG class can not be created.

name The name of the OESVGClass object. For information about valid group names see the documentation of the OEIsValidSVGClassName function.

#### See also:

- Generating Interactive SVG Images chapter
- OESVGClass class

#### **NewSVGGroup**

OESVGGroup \*NewSVGGroup (const std:: string &id)

Creates a new OESVGGroup on the given image. A null pointer will be returned and warning message will be thrown if the SVG group can not be created.

**name** The name of the OESVGGroup object. For information about valid group names see the documentation of the OEIsValidSVGGroupId function.

See also:

- Generating Interactive SVG Images chapter
- OESVGGroup class

### **PopGroup**

**bool** PopGroup (const OESVGGroup \*)

Pops the OESVGGroup object.

Note: An OESVGGroup object can be used (pushed / popped) only once. OESVGGroup objects can be nested. They should be used in LIFO (for last in, first out) i.e. the group that has been pushed last should be popped first.

#### See also:

- Generating Interactive SVG Images chapter
- OESVGGroup class
- OEImageBase. PushGroup method

### **PushGroup**

**bool** PushGroup (const OESVGGroup \*)

Pushes the OESVGGroup object.

**Note:** An *OESVGGroup* object can be used (pushed / popped) only once. *OESVGGroup* objects can be nested. They should be used in LIFO (for last in, first out) i.e. the group that has been pushed last should be popped first.

#### See also:

- Generating Interactive SVG Images chapter
- OESVGGroup class
- · OEImageBase. PopGroup method

## 4.1.38 OEImageFileBase

class OEImageFileBase : public OEImageBase

The OEImageFileBase is an abstract class that is used to write concrete image files.

|  |  |  |  |  | The following methods are publicly inherited from OEImageBase: |
|--|--|--|--|--|----------------------------------------------------------------|
|--|--|--|--|--|----------------------------------------------------------------|

| Clear           | DrawPoint           | GetHeight      |
|-----------------|---------------------|----------------|
| DrawArc         | DrawPolygon         | GetMinFontSize |
| DrawCircle      | DrawQuadraticBezier | GetWidth       |
| DrawCubicBezier | DrawRectangle       | SetMinFontSize |
| DrawLine        | DrawText            |                |
| DrawPie         | DrawTriangle        |                |

## **Constructors**

OEImageFileBase(double width, double height)

Default constructors that creates an image file with the given dimensions.

### **GetExtension**

std::string GetExtension() const =0

Returns the file extension associated with the concrete image file type.

### **IsVisible**

virtual bool IsVisible() const;

Returns whether the top active SVG group is visible i.e. returns OESVGGroup. IsVisible.

#### **PopGroup**

virtual bool PopGroup (const OESVGGroup\*)

Pops the OESVGGroup object.

### See also:

- Generating Interactive SVG Images chapter
- OESVGGroup class
- · OEImageFileBase. PushGroup method

### **PushGroup**

virtual bool PushGroup (const OESVGGroup\*)

Pushes the OESVGGroup object.

- Generating Interactive SVG Images chapter
- OESVGGroup class
- · OEImageFileBase. PopGroup method

### Write

**bool** Write (OEPlatform:: oeostream &os) = 0

The OEImageFileBase. Write is a virtual method that has to be implemented in the concrete derived classes and it writes the image into the given output stream.

## 4.1.39 OEImageFileCreatorBase

class OEImageFileCreatorBase

The OEImageFileCreatorBase is an abstract class that is used to register concrete image types.

#### See also:

· OERegisterImageFilefunction

#### **Constructors**

OEImageFileCreatorBase(const std::string &ext, bool multi=false)

Default constructor.

ext The file extension that will be used to identify the concrete image type. For example, the Portable Document Format (PDF) is registered with the "pdf" file extension.

*multi* Determines whether the specific image type can be used to create multi-page images.

#### **CreateCopy**

OEImageFileCreatorBase \*CreateCopy() const =0

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

#### **CreateImage**

OEImageFileBase \*CreateImage(double width, double height) const =0

The OEImageFileCreatorBase. CreateImage is a virtual method that has to be implemented in the concrete derived classes and it returns a pointer of concrete image with the given dimensions.

width The width of the returned image.

*height* The height of the returned image.

## **GetExtension**

```
const std:: string GetExtension() const
```

Return the file extension of which the concrete image type is being registered.

## **IsMultiPage**

```
bool IsMultiPage() const
```

Returns whether the image type registered as multi-page image.

## 4.1.40 OEImageFrame

class OEImageFrame : public OEImageBase

OEImageFrame class provides a convenient way to create a frame with a specific dimension and offset relative to an OEImageBase object. See Figure: Schematic representation of OEImageFrame objects.

![](_page_287_Figure_10.jpeg)

Fig. 157: Schematic representation of OEImageFrame objects

#### See also:

• Depicting Molecules in an Arbitrary Position section

The following methods are publicly inherited from OEImageBase:

| Clear           | DrawPie             | DrawTriangle    |
|-----------------|---------------------|-----------------|
| DrawArc         | DrawPoint           | GetGlobalOffset |
| DrawCircle      | DrawPolygon         | GetHeight       |
| DrawCubicBezier | DrawQuadraticBezier | GetMinFontSize  |
| DrawLine        | DrawRectangle       | GetWidth        |
| DrawPath        | DrawText            | GetSVGClass     |
| GetSVGGroup     | GetSVGGroups        | NewSVGClass     |
| NewSVGGroup     | PopGroup            | PushGroup       |
| SetMinFontSize  |                     |                 |

### **Constructors**

OEImageFrame (OEImageBase &parent, double width, double height, const OE2DPoint & offset)

Creates an OEImageFrame object with the given dimension.

parent The parent OEImageBase object in which the OEImageFrame object is placed.

width The width of the OEImageFrame object.

height The height of the OEImageFrame object.

offset The offset of the OEImageFrame object relative to top/left corner of its OEImageBase parent.

OEImageFrame (OEImageBase& parent, double padding)

Creates an OEImageFrame object equal paddings around the given image positioning the image frame to the center of the image.

parent The parent OEImageBase object in which the OEImageFrame object is placed.

*padding* The padding that applied in all four sides around the parent image. The padding is capped by the  $\frac{1}{3}$  of width and height of the **parent** image.

### **Clear**

```
void Clear (const OESystem:: OEColor &color)
```

Clears the image with the given color.

- · OEImageBase. Clear method
- OEColor class

### **DrawArc**

```
void DrawArc (const OE2DPoint &center, double bgnAngle, double endAngle,
             double radius, const OEPen &pen)
```

Draws the outline of an arc. See example in Figure: Example of drawing an arc.

![](_page_289_Figure_4.jpeg)

#### Fig. 158: Example of drawing an arc

#### See also:

- · OEImageBase. DrawArc method
- OE2DPoint class
- OEPen class

## **DrawCircle**

void DrawCircle (const OE2DPoint & center, double radius, const OEPen & pen)

Draws a circle. See example in Figure: Example of drawing a circle.

![](_page_289_Figure_13.jpeg)

Fig. 159: Example of drawing a circle

- · OEImageBase. DrawCircle method
- OE2DPoint class
- OEPen class

## **DrawCubicBezier**

```
void DrawCubicBezier (const OE2DPoint &bgn, const OE2DPoint &c1,
                     const OE2DPoint &c2, const OE2DPoint &end, const OEPen &pen)
```

Draws a cubic Bézier curve. See example in Figure: Example of drawing a cubic Bezier curve.

![](_page_290_Figure_4.jpeg)

### Fig. 160: Example of drawing a cubic Bezier curve

#### See also:

- · OEImageBase. DrawCubicBezier method
- OE2DPoint class
- OEPen classes

## **DrawLine**

void DrawLine (const OE2DPoint &bgn, const OE2DPoint &end, const OEPen &pen)

Draws a line. See example in Figure: Example of drawing a line.

![](_page_290_Figure_13.jpeg)

Fig. 161: Example of drawing a line

- · OEImageBase. DrawLine method
- OE2DPoint class
- OEPen classes

## **DrawPath**

void DrawPath (const OE2DPath& path, const OEPen& pen) ;

Draws a path. See example in Figure: Example of drawing a path.

![](_page_291_Figure_4.jpeg)

![](_page_291_Figure_5.jpeg)

#### See also:

- · OEImageBase. DrawPath methods
- OE2DPath class
- OEPen classes

### **DrawPie**

```
void DrawPie (const OE2DPoint & center, double bgnAngle, double endAngle,
             double radius, const OEPen &pen)
```

Draws a pie. See example in Figure: Example of drawing a pie.

![](_page_291_Figure_13.jpeg)

Fig. 163: Example of drawing a pie

- OEImageBase. DrawPie methods
- OE2DPoint class
- OEPen classes

## **DrawPoint**

![](_page_292_Figure_2.jpeg)

Fig. 164: Example of drawing a point

#### See also:

- · OEImageBase. DrawPoint method
- OE2DPoint class
- OEColor class

## **DrawPolygon**

void DrawPolygon (const std:: vector<OE2DPoint> &points, const OEPen &pen)

Draws a closed polygon. See example in Figure: Example of drawing a polygon.

![](_page_292_Figure_11.jpeg)

Fig. 165: Example of drawing a polygon

- · OEImageBase. DrawPolygon method
- OE2DPoint class
- OEPen class

## **DrawQuadraticBezier**

```
void DrawQuadraticBezier (const OE2DPoint &bgn, const OE2DPoint &c,
                         const OE2DPoint & end, const OEPen & pen)
```

Draws a quadratic Bézier curve. See example in Figure: Example of drawing a quadratic Bezier curve.

![](_page_293_Figure_4.jpeg)

#### Fig. 166: Example of drawing a quadratic Bezier curve

#### See also:

- · OEImageBase. DrawQuadraticBezier methods
- OE2DPoint class
- OEPen classes

## **DrawRectangle**

void DrawRectangle (const OE2DPoint &tl, const OE2DPoint &br, const OEPen &pen)

Draws a rectangle. See example in Figure: Example of drawing a rectangle.

![](_page_293_Picture_13.jpeg)

#### Fig. 167: Example of drawing a rectangle

- · OEImageBase. DrawRectangle method
- OE2DPoint class
- OEPen class

## **DrawText**

```
void DrawText (const OE2DPoint &c, const std::string &text, const OEFont &font,
              double maxwidth=0.0)
```

Draws a text. See example in Figure: Example of drawing a text.

![](_page_294_Picture_4.jpeg)

#### Fig. 168: Example of drawing a text

#### See also:

- · OEImageBase. DrawText method
- OE2DPoint class
- OEFont class

## **DrawTriangle**

```
void DrawTriangle (const OE2DPoint &a, const OE2DPoint &b, const OE2DPoint &c,
                  const OEPen &pen)
```

Draws a triangle. See example in Figure: Example of drawing a triangle.

![](_page_294_Figure_13.jpeg)

Fig. 169: Example of drawing a triangle

- · OEImageBase. DrawTriangle method
- OE2DPoint class
- OEPen classes

#### **GetHeight**

double GetHeight () const

Returns the height of the OEImageFrame object.

### **GetOffset**

const OE2DPoint &GetOffset() const

Returns the offset of the OEImageFrame object relative to its OEImageBase parent.

### **GetWidth**

double GetWidth() const

Returns the width of the OEImageFrame object.

## 4.1.41 OEImageGrid

#### class OEImageGrid

This class represents OEImageGrid which is a layout manager that aligns cells into rows and columns. The cells of the grid are equal-sized and evenly spaced. See Figure: Schematic representation of an OEImageGrid object.

Note: In the image grid, each cell has the same width and height. The width and height of the cells are calculated based on the height and width of the OEImageGrid, its margins and gap set between the cells.

#### See also:

- Depicting Molecules in a Grid section
- OEImageTable class

#### **Constructors**

OEImageGrid (OEImageBase &parent, unsigned int rows, unsigned int cols)

Creates an OEImageGrid object with the specified number of rows and columns.

parent The OEImageBase object on which the OEImageGrid object is placed.

rows The number of rows in the OEImageGrid object.

cols The number of columns in the OEImageGrid object.

Note: The width and the height of the OEImageGrid object are identical to the width and height of the parent OEImageBase, respectively.

![](_page_296_Figure_1.jpeg)

Fig. 170: Schematic representation of an OEImageGrid object

- · OEImageGrid. NumCols method
- · OEImageGrid. NumRows method

## **GetCell**

OEImageBase \*GetCell(unsigned int r, unsigned int c)

Returns the *OEImageBase* pointer for the cell positioned in the  $r^{th}$  row and  $c^{th}$  columns.

- r This value has to be in the range from 1 to  $OEImageGrid$ . NumRows ().
- c This value has to be in the range from 1 to  $OEImageGrid$ . NumCols ().

### **GetCellGap**

double GetCellGap() const

Returns the space between the cells of the OEImageGrid object.

## See also:

· OEImageGrid. SetCellGap method

### **GetCellHeight**

double GetCellHeight () const

Returns the height of the cells of the OEImageGrid object.

#### **GetCellWidth**

double GetCellWidth() const

Returns the width of the cells of the OEImageGrid object.

### **GetCells**

```
OESystem::OEIterBase<OEImageBase> *GetCells(unsigned int row=0,
                                            unsigned int col=0)
```

Returns an iterator over the cells of the OEImageGrid object. The cells are returned from left to right and top to bottom order.

row This value has to be in the range from  $0$  to  $OEImageGrid$ . NumRows ().

col This value has to be in the range from  $0$  to  $OEImageGrid$ . NumCols ().

**Example** (Figure Example of accessing all cells of the grid)

```
for cell in grid. GetCells():
    pass
```

| (1) | (2) | (3) |
|-----|-----|-----|
| (4) | (5) | (6) |
| (7) | (8) | (9) |

Fig. 171: Example of accessing all cells of the grid.

(The numbers inside the cells represent the order in which the cells are returned)

If the col number is zero then  $OEImageGrid$ . Get Cells returns an iterator over the cells of the specified row.

**Example** (Figure Example of accessing a specific row of the grid)

```
row = 2for cell in grid. GetCells (row, 0) :
    pass
```

If the row number is zero then  $OEImageGrid$ . Get Cells returns an iterator over the cells of the specified column.

**Example** (Figure Example of accessing a specific column of the grid)

![](_page_298_Figure_1.jpeg)

Fig. 172: Example of accessing a specific row of the grid. (The numbers inside the cells represent the order in which the cells are returned)

```
col = 2for cell in grid. GetCells (0, col) :
    pass
```

![](_page_298_Figure_4.jpeg)

Fig. 173: Example of accessing a specific column of the grid. (The numbers inside the cells represent the order in which the cells are returned)

### **GetMargin**

double GetMargin (unsigned int margin) const

Returns the size of a specific margin of the OEImageGrid object.

margin This value has to be from the OEMargin namespace.

#### See also:

- · OEImageGrid. SetMargin method
- · OEImageGrid. SetMargins method

### **NumCols**

unsigned int NumCols() const

Returns the number of columns of the OEImageGrid object.

### **NumRows**

unsigned int NumRows () const

Returns the number of rows of the OEImageGrid object.

#### **SetCellGap**

bool SetCellGap (double size)

Sets the space between the cells of the OEImageGrid object to the given size.

size This value has to be a positive number.

#### See also:

· OEImageGrid.GetCellGap method

#### **SetMargin**

bool SetMargin (unsigned int margin, double size)

Sets the size of a specific margin of the OEImageGrid object.

*margin* This value has to be from the  $OEMargin$  namespace.

size This value has to be a positive number.

#### See also:

· OEImageGrid. GetMargin method

### **SetMargins**

bool SetMargins (double size)

Sets the size of all margins of the OEImageGrid object.

size This value has to be a positive number.

See also:

· OEImageGrid. GetMargin method

## 4.1.42 OEImageTable

#### class OEImageTable

This class represents OEImageTable which is a layout manager that allows to arrange information in rows and columns with variable height and width, respectively.

- Depicting Molecules in a Table section
- OEImageTableOptions class

| <b>Property</b> | Value      |
|-----------------|------------|
| <b>Name</b>     | benzene    |
| <b>SMILES</b>   | c1ccccc1   |
| <b>MV</b>       | 78.112     |
|                 |            |
| <b>Property</b> | Value      |
| <b>Name</b>     | pyridine   |
| <b>SMILES</b>   | c1ccncc1   |
| <b>MV</b>       | 79.100     |
|                 |            |
| <b>Property</b> | Value      |
| <b>Name</b>     | pyrimidine |
| <b>SMILES</b>   | c1cncnc1   |
| <b>MV</b>       | 80.088     |

## Fig. 174: Example of using image table

- · OEImageTableStylenamespace
- OEImageGrid class

#### **Constructors**

OEImageTable(OEImageBase &parent, const OEImageTableOptions &opts)

Creates an OEImageTable object with the specified options.

parent The OEImageBase object on which the OEImageTable object is placed.

opts The OEImageTableOptions object that defines the properties and style of the table.

- · OEImageTable.GetOptions method
- · OEImageTable.NumColumns method
- · OEImageTable. NumRows method

## **DrawText**

bool DrawText (OEImageBase\* cell, const std::string& text, double padding = 5.0)

Draws a text to the given table cell. Returns false if the given image does not belong to the table.

*padding* Defines the padding used on the left and right of the given cell as a percentage of the width of the cell.

**Note:** The font that is used to render the text is defined in the *OEImageTableOptions* class.

#### See also:

- OEFont class
- · OEImageTableOptions. SetCellFont method
- · OEImageTableOptions. SetHeaderFont method
- · OEImageTableOptions. SetStubColumnFont method

#### **GetBodyCell**

OEImageBase \*GetBodyCell(unsigned int row, unsigned int col)

Returns the OEImageBase for the cell positioned in the  $r^{th}$  row and  $c^{th}$  columns of the 'body' of the table. A cell is considered to be part of the 'body' of the table if it is neither in the header nor in the stub column.

row This value has to be in the range from 1 to  $OEImageTable$ . NumRows (true).

col This value has to be in the range from 1 to  $OEImageTable$ . NumColumns (true).

Note: A null pointer is returned if the row or the col parameters are outside the acceptable range.

#### **Example**

The image below marks the cell returned by OEImageTable. GetBodyCell method for row = 1 and col = 2 parameters.

| $(r=1, c=2)$ |              | $(r=1, c=2)$ |              |
|--------------|--------------|--------------|--------------|
|              | $(r=1, c=2)$ |              | $(r=1, c=2)$ |
|              |              |              |              |

#### Fig. 175: Example of accessing a specific 'body' cell of the table.

### See also:

· OEImageTable.GetCell method

## **GetBodyCells**

```
OESystem::OEIterBase<OEImageBase> *GetBodyCells (unsigned int row=0,
                                                 unsigned int col=0)
```

Returns an iterator over the 'body' cells of the OEImageTable object. A cell is considered to be part of the 'body' of the table if it is neither in the header nor in the stub column. The cells are returned from left to right and top to bottom order.

row This value has to be in the range from 0 to  $OEImageTable$ . NumRows (true).

col This value has to be in the range from 0 to  $OEImageTable$ . NumColumns (true).

Note: An empty iterator is returned if the row or the col parameters are outside the acceptable range.

#### **Examples**

If the OEImageTable. GetBodyCells method is invoked without any parameter, then all 'body cells' are returned.

| $(1)$ $(2)$ $(3)$ |                                     |     |  | $(1)$ $(2)$ |     |     |
|-------------------|-------------------------------------|-----|--|-------------|-----|-----|
|                   | $(4)$ $(5)$ $(6)$ $(1)$ $(2)$ $(3)$ |     |  | $(3)$ $(4)$ | (1) | (2) |
|                   | $(7)$ $(8)$ $(9)$ $(4)$ $(5)$       | (6) |  | $(5)$ $(6)$ | (3) | (4) |

### Fig. 176: Example of accessing all 'body' cells of the table

(The numbers inside the cells represent the order in which the cells are returned)

If the row parameter is zero, then the  $OEImageTable$ . GetBodyCells method returns an iterator over the 'body' cells of the specified column. The image below marks the cells returned by  $OEImageTable \cdot GetBodyCell$ method for row = 0 and col = 2 parameters.

| (1) | (1) | (1) |     |
|-----|-----|-----|-----|
| (2) | (1) | (2) | (1) |
| (3) | (2) | (3) | (2) |

#### Fig. 177: Example of accessing 'body' cells of a specific columns in the table

(The numbers inside the cells represent the order in which the cells are returned)

If the column parameter is zero, then the OEImageTable. GetBodyCells method returns an iterator over the 'body' cells of the specified column. The image below marks the cells returned by OEImageTable. GetBodyCell method for row = 2 and col = 0 parameters.

| $(1)$ $(2)$ $(3)$ |  |                   |  | $(1)$ | $(2)$ |     |
|-------------------|--|-------------------|--|-------|-------|-----|
|                   |  | $(1)$ $(2)$ $(3)$ |  |       | (1)   | (2) |

![](_page_303_Figure_2.jpeg)

#### See also:

· OEImageTable.GetCells method

## **GetCell**

OEImageBase \*GetCell (unsigned int row, unsigned int col)

Returns the OEImageBase pointer for the cell positioned in the  $r^{th}$  row and  $c^{th}$  columns.

row This value has to be in the range from 1 to  $OEImageTable$ . NumRows ().

col This value has to be in the range from 1 to  $OEImageTable$ . NumColumns ().

Note: A null pointer is returned if the row or the col parameters are outside the acceptable range.

#### **Example**

The image below marks the cell returned by  $OEImageTable$ . GetCell method for row = 1 and col = 2 parameters.

| $(r=1, c=2)$ | $(r=1, c=2)$ | $(r=1, c=2)$ | $(r=1, c=2)$ |
|--------------|--------------|--------------|--------------|
|              |              |              |              |
|              |              |              |              |

#### Fig. 179: Example of accessing a specific cell of the table

## See also:

· OEImageTable.GetBodyCell method

## **GetCells**

```
OESystem::OEIterBase<OEImageBase> *GetCells(unsigned int row=0,
                                            unsigned int col=0)
```

Returns an iterator over the cells of the OEImageTable object. The cells are returned from left to right and top to bottom order.

row This value has to be in the range from 0 to  $OEImageTable$ . NumRows ().

col This value has to be in the range from 0 to  $OEImageTable$ . NumColumns ().

Note: An empty iterator is returned if the row or the col parameters are outside the acceptable range.

### **Examples**

If the OEImageTable. GetCells method is invoked without any parameter, then all cells of the table are returned.

|  | (1) (2) (3) (1) (2) (3) (1) (2) (3) (1) (2) (3) (4) (2) (3) |  |  |  |  |
|--|-------------------------------------------------------------|--|--|--|--|
|  | (4) (5) (6) (4) (5) (6) (4) (5) (6) (4) (5) (6) (4) (5) (6) |  |  |  |  |
|  | (7) (8) (9) (7) (8) (9) (7) (8) (9) (7) (8) (9) (7) (8) (9) |  |  |  |  |

### Fig. 180: Example of accessing all cells of the table

(The numbers inside the cells represent the order in which the cells are returned)

If the row parameter is zero, then the  $OEImageTable \cdot GetCells$  method returns an iterator over the cells of the specified column. The image below marks the cells returned by  $OEImageTable$ . GetCell method for row = 0 and  $col = 2$  parameters.

| (1)<br>(2)<br>(3) | (1) (2)<br>(3) |  |  | (1)<br>(2)<br>(3) |  |  | (1)    (2)<br>(3) |  |  |  |  |
|-------------------|----------------|--|--|-------------------|--|--|-------------------|--|--|--|--|
|-------------------|----------------|--|--|-------------------|--|--|-------------------|--|--|--|--|

### Fig. 181: Example of accessing all cells of a specific columns of the table.

(The numbers inside the cells represent the order in which the cells are returned)

If the column parameter is zero, then the OEImageTable. GetCells method returns an iterator over the cells of the specified row. The image below marks the cells returned by  $OEImageTable$ . Get Cell method for row = 2 and  $col = 0$  parameters.

|  |  |  | (1) (2) (3) (1) (2) (3) (1) (2) (3) (1) (2) (3) (1) (2) (3) |  |  |  |
|--|--|--|-------------------------------------------------------------|--|--|--|
|  |  |  |                                                             |  |  |  |

#### Fig. 182: Example of accessing all cells of a specific row of the table.

(The numbers inside the cells represent the order in which the cells are returned)

• OEImageTable.GetBodyCells method

## **GetHeaderCell**

OEImageBase \*GetHeaderCell (unsigned int col, bool skipstub=true)

Returns the OEImageBase for the cell positioned in the  $c<sup>th</sup>$  columns of the 'header' of the table.

col This value has to be in the range:

- $\bullet$  from 1 to OEImageTable. NumColumns (false) if skipstub is true.
- from 1 to OEImageTable. NumColumns (true) if skipstub is false.
- skipstub The parameter that determines whether to consider the stub column. If skipstub is false and the table has a stub column, than that stub column is considered as the first column.

Note: A null pointer is returned if the table has no header or if the col parameters is outside the acceptable range.

#### **Example**

The image below marks the cell returned by OEImageTable. GetHeaderCell method for col = 2 and skipstub  $=$  true parameters.

![](_page_305_Figure_15.jpeg)

Fig. 183: Example of accessing a specific header cell of the table

## **GetHeaderCells**

OESystem:: OEIterBase<OEImageBase> \*GetHeaderCells (bool skipstub=true)

Returns an iterator over the header cells of the OEImageTable object. The cells are returned from left to right order.

skipstub The parameter that determines whether to consider the stub column. If skipstub is false and the table has a stub column, than that stub column is considered as the first column.

Note: An empty iterator is returned if table has no header row.

#### **Example**

The image below marks the cells returned by  $OEImageTable$ . GetHeaderCells for skipstub = true parameter.

![](_page_306_Figure_8.jpeg)

Fig. 184: Example of accessing header cells of the table

(The numbers inside the cells represent the order in which the cells are returned)

### **GetOptions**

const OEImageTableOptions &GetOptions () const

Returns the options used to initialized the OEImageTable object.

#### See also:

• OEImageTableOptions class

#### **GetStubColumnCell**

OEImageBase \*GetStubColumnCell(unsigned int row)

Returns the OEImageBase for the cell positioned in the  $r^{th}$  row of the 'stub column' of the table.

row This value has to be in the range from 1 to  $OEImageTable$ . NumRows (true).

Note: A null pointer is returned if the table has no stub column or if the row parameters is outside the acceptable range.

**Example** 

The image below marks the cell returned by OEImageTable. GetStubColumnCell method for row=1 parameter.

![](_page_307_Picture_2.jpeg)

## Fig. 185: Example of accessing a specific stub column cell of the table

## **GetStubColumnCells**

OESystem::OEIterBase<OEImageBase> \*GetStubColumnCells()

Returns an iterator over the stub column cells of the OEImageTable object. The cells are returned from top to bottom order.

Note: An empty iterator is returned if table has no stub column.

#### **Example**

The image below marks the cells returned by OEImageTable. GetStubColumnCells method.

![](_page_307_Figure_10.jpeg)

#### Fig. 186: Example of accessing stub column cells of the table

(The numbers inside the cells represent the order in which the cells are returned)

## **NumColumns**

unsigned int NumColumns (bool onlybody=false) const

Returns the number of columns of the OEImageTable object.

onlybody If this parameter is 'true', than stub column is not counted if exists.

#### **NumRows**

unsigned int NumRows (bool onlybody=false) const

Returns the number of rows of the OEImageTable object.

onlybody If this parameter is 'true', than header row is not counted if exists.

## 4.1.43 OEImageTableOptions

class OEImageTableOptions

This class represents the OEImageTableOptions class that encapsulates properties that determine how an image table is depicted.

The OEImageTableOptions class stores the following properties:

| Property              | Get method         | Set method                | Corresponding namespace /<br>class / type                       |
|-----------------------|--------------------|---------------------------|-----------------------------------------------------------------|
| number of columns     | <i>NumColumns</i>  |                           | integer greater than 0                                          |
| number of rows        | <i>NumRows</i>     |                           | integer greater than 1                                          |
| width of columns      |                    | SetColumnWidths           | vector of non-zero integers                                     |
| height of rows        |                    | SetRowHeights             | vector of non-zero integers                                     |
| cell font size        |                    | SetBaseFontSize           | positive non-zero integer                                       |
| pen used around cells | GetCellBorderPen   | SetCellBorderPen          | <b><i>OEPen</i></b>                                             |
| table cell color      | GetCellColor       | SetCellColor              | <b>OEColor</b>                                                  |
| table cell font       | GetCellFont        | SetCellFont               | <b>OEFont</b>                                                   |
| header                | HasHeader          | SetHeader                 | boolean                                                         |
| header color          | GetHeaderColor     | SetHeaderColor            | <b>OEColor</b>                                                  |
| header font           | GetHeaderFont      | SetHeaderFont             | <b>OEFont</b>                                                   |
| table margins         | GetMargin          | SetMargin /<br>SetMargins | positive floating point number in the<br>range of $[0.0, 25.0]$ |
| stub column           | HasStubColumn      | SetStubColumn             | boolean                                                         |
| stub column color     | GetStubColumnColor | SetStubColumnColor        | <b>OEColor</b>                                                  |
| stub column font      | GetStubColumnFont  | SetStubColumnFont         | <b>OEFont</b>                                                   |

- Depicting Molecules in a Table section
- OEImageTable class

## **Constructors**

OEImageTableOptions (unsigned int rows, unsigned int cols, unsigned int style=OEImageTableStyle::Default)

Creates an OEImageTableOptions object with the given parameters.

rows The total number of rows in the table including the header.

cols The total number of columns in the table including the stub column.

style This value has to be from the  $OEImageTableStyle$  namespace.

Note: By default, the columns and rows of a table are created with equal widths and heights. The relative width and height ratio of the columns and rows can be adjusted using the OEImageTableOptions. SetColumnWidths and OEImageTableOptions. SetRowHeights methods, respectively.

**Example** (*Example of generating a 4 x 4 image table with header and 'MediumBlue' style*)

 $tableopts = oedgeict. 0EImageTableOptions (4, 4, oedgeict. 0EImageTableStyle\_MedianBlue)$ 

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

![](_page_309_Figure_11.jpeg)

#### See also:

- · OEImageTableStyle namespace
- · OEImageTableOptions. NumRows method
- · OEImageTableOptions. NumColumns method

OEImageTableOptions (const OEImageTableOptions & rhs)

Copy constructor.

#### operator=

```
OEImageTableOptions & operator= (const OEImageTableOptions &)
```

Assignment operator.

#### **GetCellBorderPen**

const OEPen &GetCellBorderPen() const

Returns the pen that is used to mark the border of the cells in the table.

#### See also:

- OEPen class
- · OEImageTableOptions. SetCellBorderPen method

#### **GetCellColor**

const OESystem:: OEColor GetCellColor (bool even-true) const

#### See also:

· OEImageTableOptions. SetCellColor method

Returns the color used to highlight the 'body' cells in the table. A cell is considered to be part of the 'body' of the table if it is neither in the header nor in the stub column.

even This parameter determines whether to return the color of the even or odd rows in the table.

#### See also:

- OEColor class
- · OEImageTableOptions. SetCellColor method

### **GetCellFont**

const OEFont GetCellFont () const

Returns the font used by the OEImageTable. DrawText method to draw text on the 'body' cells.

- OEFont class
- · OEImageTableOptions. SetCellFont method

## **GetHeaderColor**

const OESystem:: OEColor GetHeaderColor () const

Returns the color used to highlight the 'header' cells in the table.

#### See also:

- OEColor class
- · OEImageTableOptions. SetHeaderColor method

## **GetHeaderFont**

const OEFont GetHeaderFont () const

Returns the font used by the OEImageTable. DrawText method to draw text on the 'header' cells.

#### See also:

- OEFont class
- · OEImageTableOptions. SetHeaderFont method

#### **GetMargin**

double GetMargin (unsigned int margin) const

Returns the ratio of a specific margin of the table.

**margin** This value has to be from the OEMargin namespace.

#### See also:

- · OEImageTableOptions. SetMargin method
- · OEImageTableOptions. SetMargins method

## **GetStubColumnColor**

const OESystem:: OEColor GetStubColumnColor() const

Returns the color used to highlight the 'stub column' cells in the table.

- OEColor class
- · OEImageTableOptions. SetStubColumnColor method

## **GetStubColumnFont**

const OEFont GetStubColumnFont () const

Returns the font used by the OEImageTable. DrawText method to draw text on the 'stub column' cells.

#### See also:

- OEFont class
- · OEImageTableOptions. SetStubColumnFont method

### **HasHeader**

bool HasHeader () const

Returns whether a table has a 'header' row. By default, a table is generated with a 'header' row.

#### See also:

- · OEImageTableOptions. SetHeader method
- · OEImageTableOptions. HasStubColumn method
- · OEImageTableOptions. SetStubColumn method

## **HasStubColumn**

bool HasStubColumn() const

Returns whether the table has a 'stub' column. By default, a table is generated without a 'stub' column.

#### See also:

- · OEImageTableOptions. SetStubColumn method
- · OEImageTableOptions. HasHeader method
- · OEImageTableOptions. SetHeader method

## **NumColumns**

unsigned int NumColumns () const

Returns the total number of columns in the table including the stub column.

#### **NumRows**

unsigned int NumRows () const

Returns the total number of rows in the table including the header row.

## **SetBaseFontSize**

void SetBaseFontSize (unsigned int fontsize)

Controls the font size in add table cells (including cells of header, stub column and body).

#### See also:

The other properties of the used fonts can be controlled with the following methods:

- · OEImageTableOptions. SetCellFont method
- · OEImageTableOptions. SetHeaderFont method
- · OEImageTableOptions. SetStubColumnFont method

## **SetCellBorderPen**

void SetCellBorderPen (const OEPen &pen)

Sets the pen that is used to mark the border of the cells in the table.

**Example** (*Example of using the SetCellBorderPen method*)

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
pen = oedepict.OEPen(oechem.OEBlack, oechem.OEDarkBlue, oedepict.OEFill_Off, 2.0)
tableopts.SetCellBorderPen(pen)
```

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

#### Fig. 188: Example of using the SetCellBorderPen method

- OEPen class
- · OEImageTableOptions.GetCellBorderPen method

## **SetCellColor**

void SetCellColor (const OESystem:: OEColor &color, bool even=true)

Sets the color used to highlight the 'body' cells in the table. A cell is considered to be part of the 'body' of the table if it is neither in the header nor in the stub column.

color The color of the cells.

even This parameter determines whether the color is applied to the even or to the odd rows of the table.

**Example** (*Example of using the SetCellColor method*)

tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle\_MediumBlue) evenrow =  $True$ tableopts. SetCellColor (oechem. OELightGrey, not evenrow)

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

#### Fig. 189: Example of using the SetCellColor method

#### See also:

- OEColor class
- · OEImageTableOptions.GetCellColor method

## **SetCellFont**

void SetCellFont (const OEFont & font)

Sets the font used by the  $OEImageTable$ . DrawText method to draw text on the 'body' cells. A cell is considered to be part of the 'body' of the table if it is neither in the header nor in the stub column.

**Example** (*Example of using the SetCellFont method*)

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
font = oedepict.OEFont(oedepict.OEFontFamily_Default,
                       oedepict.OEFontStyle_Italic | oedepict.OEFontStyle_Bold,
                       8, oedepict.OEAlignment_Left, oechem.OEDarkRed)
tableopts. SetCellFont (font)
```

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

### Fig. 190: Example of using the SetCellFont method

#### See also:

· OEImageTableOptions.GetCellFont method

### **SetColumnWidths**

**bool** SetColumnWidths (const std::vector<unsigned int> &widths)

Sets the relative widths of the columns.

widths The relative widths of the columns. The size of the vector has to be  $OEImageTableOptions$ . NumColumns().

**Example** (*Example of using the SetColumnWidths method*)

The following example show how to adjust the width ratio of the columns.

tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle\_MediumBlue) tableopts. SetColumnWidths([20, 10, 20, 10])

See also:

· OEImageTableOptions. SetRowHeights method

#### **SetHeader**

bool SetHeader (bool has)

Sets whether to have a 'header' row in the table.

**Example** (*Example of using the SetHeader method*)

By default, a table is generated with a header row on the top. The following example show how to remove the header.

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

Fig. 191: Example of using the SetColumnWidths method

| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
|-------------|-------------|-------------|-------------|
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |
| (body 4, 1) | (body 4, 2) | (body 4, 3) | (body 4, 4) |

### Fig. 192: Example of using the SetHeader method

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts. SetHeader (False)
```

- · OEImageTableOptions. HasHeader method
- · OEImageTableOptions. HasStubColumn method
- · OEImageTableOptions. SetStubColumn method

## **SetHeaderColor**

void SetHeaderColor (const OESystem:: OEColor &color)

Sets the color used to highlight the 'header' cells in the table.

**Example** (*Example of using the SetHeaderColor method*)

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts.SetHeaderColor(oechem.OELightGrey)
```

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

#### Fig. 193: Example of using the SetHeaderColor method

#### See also:

- OEColor class
- · OEImageTableOptions.GetHeaderColor method

## **SetHeaderFont**

void SetHeaderFont (const OEFont & font)

Sets the font used by the OEImageTable. DrawText method to draw text on the 'header' cells.

**Example** (*Example of using the SetHeaderFont method*)

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
\texttt{font = } \texttt{o} \texttt{e} \texttt{e} \texttt{p} \texttt{i} \texttt{.0}\texttt{E} \texttt{Font} \texttt{.0}\texttt{E} \texttt{F} \texttt{on} \texttt{t} \texttt{F} \texttt{am} \texttt{1} \texttt{y\_De} \texttt{fault, } \texttt{o} \texttt{e} \texttt{de} \texttt{p} \texttt{t} \texttt{.0}\texttt{E} \texttt{F} \texttt{on} \texttt{t} \texttt{y} \texttt{l} \texttt{e\_De} \texttt{fault, } \texttt{u} \texttt{b} \texttt{-12.
                                                      oedepict.OEAlignment_Right, oechem.OEPinkTint)
tableopts. SetHeaderFont (font)
```

- OEFont class
- · OEImageTableOptions. GetHeaderFont method

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

|  |  |  |  | Fig. 194: Example of using the SetHeaderFont method |
|--|--|--|--|-----------------------------------------------------|
|--|--|--|--|-----------------------------------------------------|

#### **SetMargin**

bool SetMargin (unsigned int marginloc, double margin)

Sets the size of a specific margin of the table.

marginloc This value has to be from the OEMargin namespace.

*margin* This number is considered as a percentage of either the width or the height of image on which the table will be drawn and has to be in the range of  $[0.0, 25.0]$ . For example, 10.0% means, that the left and right margin are 10% of the total width of the image, and the top and bottom margins are 10% of the total height of the image.

**Example** (*Example of using the SetMargin method*)

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts. SetMargin (oedepict. OEMargin_Left, 10.0)
tableopts. SetMargin (oedepict. OEMargin_Right, 10.0)
```

See also:

- · OEImageTableOptions. GetMargin method
- · OEImageTableOptions. SetMargins method

#### **SetMargins**

bool SetMargins (double margin)

Sets the size of all margins of the table.

*margin* This number is considered as a percentage of either the width or the height of image on which the table will be drawn and has to be in the range of  $[0.0, 25.0]$ . For example, 10.0% means, that the left and right margin are 10% of the total width of the image, and the top and bottom margins are 10% of the total height of the image.

**Example** (*Example of using the SetMargins method*)

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

Fig. 195: Example of using the SetMargin method

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts. SetMargins (10.0)
```

|  | (header 1)   (header 2)   (header 3)   (header 4)           |  |
|--|-------------------------------------------------------------|--|
|  | $($ body 1, 1) $($ body 1, 2) $($ body 1, 3) $($ body 1, 4) |  |
|  | $(body 2, 1)$ $(body 2, 2)$ $(body 2, 3)$ $(body 2, 4)$     |  |
|  | $(body 3, 1)$ $(body 3, 2)$ $(body 3, 3)$ $(body 3, 4)$     |  |

Fig. 196: Example of using the SetMargins method

- · OEImageTableOptions.GetMargin method
- · OEImageTableOptions. SetMargin method

### **SetRowHeights**

**bool** SetRowHeights (const std::vector<unsigned int> &heights)

Sets the relative heights of the rows.

**heights** The relative heights of the rows. The size of the vector has to be  $OEImageTableOptions$ . NumRows ().

**Example** (*Example of using the SetRowHeights method*)

The following example show how to adjust the height ratio of the rows.

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts. SetRowHeights ([10, 20, 30, 40])
```

| (header 1)  | (header 2)  | (header 3)  | (header 4)  |
|-------------|-------------|-------------|-------------|
| (body 1, 1) | (body 1, 2) | (body 1, 3) | (body 1, 4) |
| (body 2, 1) | (body 2, 2) | (body 2, 3) | (body 2, 4) |
| (body 3, 1) | (body 3, 2) | (body 3, 3) | (body 3, 4) |

#### Fig. 197: Example of using the SetRowHeights method

#### See also:

· OEImageTableOptions. SetColumnWidths method

#### **SetStubColumn**

bool SetStubColumn (bool has)

Sets whether to have a 'stub' column in the table.

**Example** (*Example of using the SetStubColumn method*)

By default, a table is generated without a 'stub' column. The following example show how to add one on the left.

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts. SetStubColumn (True)
```

- · OEImageTableOptions. HasStubColumn method
- · OEImageTableOptions. HasHeader method

|          | (header 1)  | (header 2)  | (header 3)  |
|----------|-------------|-------------|-------------|
| (stub 1) | (body 1, 1) | (body 1, 2) | (body 1, 3) |
| (stub 2) | (body 2, 1) | (body 2, 2) | (body 2, 3) |
| (stub 3) | (body 3, 1) | (body 3, 2) | (body 3, 3) |

### Fig. 198: Example of using the SetStubColumn method

· OEImageTableOptions. SetHeader method

## **SetStubColumnColor**

```
void SetStubColumnColor(const OESystem::OEColor & color)
```

Sets the color used to highlight the 'stub' cells in the table.

**Example** (Example of using the SetStubColumnColor method)

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts. SetStubColumn (True)
```

tableopts.SetStubColumnColor(oechem.OELightGrey)

|          | (header 1)  | (header 2)  | (header 3)  |
|----------|-------------|-------------|-------------|
| (stub 1) | (body 1, 1) | (body 1, 2) | (body 1, 3) |
| (stub 2) | (body 2, 1) | (body 2, 2) | (body 2, 3) |
| (stub 3) | (body 3, 1) | (body 3, 2) | (body 3, 3) |

Fig. 199: Example of using the SetStubColumnColor method

See also:

- OEColor class
- · OEImageTableOptions.GetStubColumnColor method

## **SetStubColumnFont**

void SetStubColumnFont (const OEFont &font)

Sets the font used by the  $OEImageTable$ .  $DrawText$  method to draw text on the 'stub column' cells.

**Example** (Example of using the SetStubColumnFont method)

```
tableopts = oedepict.OEImageTableOptions(4, 4, oedepict.OEImageTableStyle_MediumBlue)
tableopts. SetStubColumn (True)
font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
-12,
                       oedepict.OEAlignment_Right, oechem.OEPinkTint)
```

```
tableopts. SetStubColumnFont (font)
```

|          | (header 1)  | (header 2)  | (header 3)  |
|----------|-------------|-------------|-------------|
| (stub 1) | (body 1, 1) | (body 1, 2) | (body 1, 3) |
| (stub 2) | (body 2, 1) | (body 2, 2) | (body 2, 3) |
| (stub 3) | (body 3, 1) | (body 3, 2) | (body 3, 3) |

### Fig. 200: Example of using the SetStubColumnFont method

- OEFont class
- · OEImageTableOptions.GetStubColumnFont method

## 4.1.44 OELegendLayout

#### class OELegendLayout

This class represents OELegendLayout which is a layout manager that allows to create interactive legends in SVG image format.

See also:

- OELegendLayoutOptions class
- · OEDrawLegendLayout function
- · OELegendLayoutStylenamespace
- · OELegendColorStyle namespace
- · OELegendInteractiveStylenamespace

### **Constructors**

```
OELegendLayout (OEImageBase &parent, const std::string &text,
               const OELegendLayoutOptions &opts)
```

Creates an OELegendLayout object with the specified options.

parent The OEImageBase object on which the OELegendLayout object is placed.

text The text of the button of the legend.

opts The OELegendLayoutOptions object that defines the properties and style of the legend layout.

See also:

· OELegendLayout. GetOptions method

### GetLegendArea

OEImage &GetLegendArea()

Provides access to the legend area of the OELegendLayout object.

#### See also:

• OEImage class

### **GetOptions**

const OELegendLayoutOptions &GetOptions () const

Returns the options used to initialized the OELegendLayout object.

#### See also:

• OELegendLayoutOptions class

## 4.1.45 OELegendLayoutOptions

### class OELegendLayoutOptions

This class represents the OELegendLayoutOptions class that encapsulates properties that determine how an legend layout is depicted.

The OELegendLayoutOptions class stores the following properties:

| Property                 | Get method                  | Set method                           | Corresponding namespace / class / type                     |
|--------------------------|-----------------------------|--------------------------------------|------------------------------------------------------------|
| legend layout style      | <i>GetLayoutStyle</i>       | (set by the constructor)             | OELegendLayoutStyle<br>namespace                           |
| legend color style       | <i>GetColorStyle</i>        | (set by the constructor)             | OELegendColorStyle<br>namespace                            |
| legend interactive style | <i>GetInteractiveStyle</i>  | (set by the constructor)             | OELegendInteractiveStyle<br>namespace                      |
| button label font        | <i>GetButtonFont</i>        | <i>SetButtonFont</i>                 | OEFont                                                     |
| button pen(s)            | <i>GetButtonPen</i>         | <i>SetButtonPen</i>                  | OEPen                                                      |
| button height scale      | <i>GetButtonHeightScale</i> | <i>SetButtonHeightScale</i>          | positive floating point number in the range of [0.5, 3.0]  |
| button width scale       | <i>GetButtonWidthScale</i>  | <i>SetButtonWidthScale</i>           | positive floating point number in the range of [0.5, 5.0]  |
| legend box pen           | <i>GetLegendBoxPen</i>      | <i>SetLegendBoxPen</i>               | OEPen                                                      |
| layout margins           | <i>GetMargin</i>            | <i>SetMargin</i> / <i>SetMargins</i> | positive floating point number in the range of [0.0, 90.0] |

### See also:

• OELegendLayout class

## **Constructors**

OELegendLayoutOptions (unsigned int layout=OELegendLayoutStyle::Default, unsigned int color=OELegendColorStyle::Default, unsigned int inter=OELegendInteractiveStyle::Default)

See also:

- · OELegendLayoutStylenamespace
- · OELegendColorStyle namespace
- · OELegendInteractiveStylenamespace

OELegendLayoutOptions (const OELegendLayoutOptions & rhs)

Copy constructor.

### operator=

OELegendLayoutOptions & operator= (const OELegendLayoutOptions & rhs)

Assignment operator.

## **GetButtonFont**

const OEFont& GetButtonFont() const

#### See also:

- OEFont class
- · OELegendLayoutOptions. SetButtonFont method

### **GetButtonHeightScale**

double GetButtonHeightScale() const

#### See also:

· OELegendLayoutOptions. SetButtonHeightScale method

### **GetButtonPen**

const OEPen& GetButtonPen (bool on) const

#### See also:

- OEPen class
- · OELegendLayoutOptions. SetButtonPen method

## **GetButtonWidthScale**

double GetButtonWidthScale() const

#### See also:

· OELegendLayoutOptions. SetButtonWidthScale method

### **GetColorStyle**

unsigned int GetColorStyle() const

#### See also:

· OELegendColorStyle namespace

## **GetInteractiveStyle**

unsigned int GetInteractiveStyle() const

#### See also:

· OELegendInteractiveStylenamespace

#### **GetLayoutStyle**

unsigned int GetLayoutStyle() const

#### See also:

· OELegendLayoutStylenamespace

### **GetLegendBoxPen**

const OEPen& GetLegendBoxPen() const

#### See also:

- $\bullet$  OEPen class
- · OELegendLayoutOptions. SetLegendBoxPen method

### **GetMargin**

double GetMargin (unsigned int percent) const

Returns the ratio of a specific margin of the legend layout.

margin This value has to be from the OEMargin namespace.

#### See also:

- · OELegendLayoutOptions. SetMargin method
- · OELegendLayoutOptions. SetMargins method

## **SetButtonFont**

void SetButtonFont (const OEFont & font)

- OEFont class
- · OELegendLayoutOptions. GetButtonFont method

#### **SetButtonHeightScale**

void SetButtonHeightScale (double scale)

#### See also:

· OELegendLayoutOptions. GetButtonHeightScale method

#### **SetButtonPen**

void SetButtonPen (const OEPen &pen, bool on)

#### See also:

- OEPen class
- · OELegendLayoutOptions. GetButtonPen method

#### **SetButtonWidthScale**

void SetButtonWidthScale(double s)

#### See also:

· OELegendLayoutOptions.GetButtonWidthScalemethod

#### **SetLegendBoxPen**

void SetLegendBoxPen (const OEPen &pen)

#### See also:

- OEPen class
- · OELegendLayoutOptions. GetLegendBoxPen method

#### **SetMargin**

bool SetMargin (unsigned int margin, double percent)

Sets the size of a specific margin of the legend layout.

**marginloc** This value has to be from the OEMargin namespace.

margin This number is considered as a percentage of either the width or the height of image on which the legend layout will be drawn and has to be in the range of  $[0.0, 90.0]$ . For example, 10.0% means, that the left and right margin are  $10\%$  of the total width of the image, and the top and bottom margins are  $10\%$  of the total height of the image.

- · OELegendLayoutOptions. GetMargin method
- · OELegendLayoutOptions. SetMargins method

## **SetMargins**

bool SetMargins (double margin)

Sets the size of all margins of the legend layout.

*margin* This number is considered as a percentage of either the width or the height of image on which the legend layout will be drawn and has to be in the range of [0.0, 90.0]. For example, 10.0% means, that the left and right margin are  $10\%$  of the total width of the image, and the top and bottom margins are  $10\%$  of the total height of the image.

See also:

- · OELegendLayoutOptions. GetMargin method
- · OELegendLayoutOptions. SetMargin method

## 4.1.46 OEMolDisplayBase

class OEMolDisplayBase : public OESystem:: OEBase

The OEMolDisplayBase class is the abstract interface for representing molecule display information within OEDepict TK. See Figure: OEDepict TK molecule display class hierarchy.

![](_page_328_Figure_11.jpeg)

Fig. 201: OEDepict TK molecule display class hierarchy

See also:

- OEAtomDisplayBase class
- OEBondDisplayBase class

The following classes derive from this class:

• OE2DMolDisplay

#### **GetDataType**

const void \*GetDataType() const

This function is used to perform run-time type identification.

#### See also:

• OEBase. GetDataType method in the OEChem TK manual

#### **GetMolecule**

const OEChem:: OEMolBase \*GetMolecule () const

Returns the const pointer of the OEMolBase object for which the display properties are stored in the class derived from the OEMolDisplayBase abstract class.

#### **IsDataType**

bool IsDataType (const void \*) const

Returns whether type is the same as the instance this method is called on.

#### See also:

• OEBase. IsDataType method in the OEChem TK manual

## 4.1.47 OEMultiPageImageFile

#### class OEMultiPageImageFile

The OEMultiPageImageFile class supports the creation of multi-page images. The dimensions and orientation of the pages are determined when an OEMultiPageImageFile object is created. Pages are created by calling the OEMultiPageImageFile.NewPage method. See Figure: Schematic representation of an OEMultiPageImage-File object.

#### See also:

- Multi Page Images chapter
- OEGetSupportedMultiPageImageFileExtensionsfunction

Hint: We highly recommend to usage of the more convenient high-level OEReport class when generating multi-page images.

- Multi Page Reports section
- Depicting Molecules in Multi-Page example
- Depicting MDL Query Substructure Search Hits example

![](_page_330_Figure_1.jpeg)

Fig. 202: Schematic representation of an OEMultiPageImageFile object

## **Constructors**

OEMultiPageImageFile(double pagewidth, double pageheight)

Creates an OEMultiPageImageFile object with a specified page width and height. Both the width and the height parameters have to be positive (non-zero) numbers.

OEMultiPageImageFile(unsigned int orientation, unsigned int imagesize)

Creates an OEMultiPageImageFile object with the given orientation and size.

**orientation** Determine the orientation of the pages. This value has to be from the  $OEPageOrientation$  namespace.

*imagesize* Determine the width and height of the pages. This value has to be from the  $OEPageSize$  namespace.

#### See also:

- · OEGetPageHeight function
- · OEGetPageWidth function

### **GetOrientation**

unsigned int GetOrientation() const

Returns the orientation of the pages. The return value is taken from the OEPageOrientation namespace.

### **GetPage**

```
OEImage *GetPage (unsigned int page)
const OEImage *GetPage(unsigned int page) const
```

Returns the  $p^{th}$  page.

p This value has to be in the range from 1 to OEMultiPageImageFile. NumPages().

Note: If p page index is out of range, then the OEMultiPageImageFile. GetPage method returns a NULL pointer.

## **GetPageHeight**

double GetPageHeight () const

Returns the height of the pages.

## **GetPageWidth**

double GetPageWidth() const

Returns the width of the pages.

## **GetPages**

```
OESystem:: OEIterBase<OEImage> *GetPages()
OESystem:: OEIterBase<const OEImage> *GetPages() const
```

Returns an iterator over all pages stored in the OEMultiPageImageFile object.

### **NewPage**

OEImage &NewPage()

Returns a new page as an OEImage object.

#### **NumPages**

unsigned int NumPages () const

Returns the number of pages stored in the OEMultiPageImageFile object.

## 4.1.48 OENearestAtom

class OENearestAtom

The OENearestAtom class that is used by OEGetNearestAtom and OEGetNearbyAtom functions. It stores an atom pointer, an associated distance and the display position of the atom.

### **Constructors**

```
OENearestAtom (const OEChem:: OEAtomBase *atom, double distance)
OENearestAtom (const OEChem:: OEAtomBase *atom, double distance,
              const OE2DPoint &displaypos)
```

Constructors.

If no display position is given then it will be initialized to  $OE2DPoint(0.0, 0.0)$ .

#### **GetAtom**

const OEChem:: OEAtomBase \*GetAtom() const

Returns the atom pointer stored in the OENearestAtom object.

### **GetDisplayPosition**

const OE2DPoint& GetDisplayPosition() const;

Returns the display position of the nearest atom.

#### **GetDist**

double GetDist() const

Returns the distance associated with the atom.

### **IsValid**

bool IsValid() const

Returns whether the OENearestAtom object is initialized correctly.

## 4.1.49 OENearestBond

class OENearestBond

The OENearestBond class, used by OEGetNearestBond and OEGetNearbyBond functions. It stores a bond pointer, the associated distance and the display position of the bond.

### **Constructors**

```
OENearestBond(const OEChem:: OEBondBase *bond, double distance)
OENearestAtom (const OEChem:: OEBondBase *bond, double distance,
             const OE2DPoint &displaypos)
```

Constructors.

If no display position is given then it will be initialized to  $OE2DPoint(0.0, 0.0)$ .

#### **GetBond**

const OEChem:: OEBondBase \*GetBond() const

Returns the bond pointer stored in the OENearestBond object.

#### **GetDisplayPosition**

const OE2DPoint& GetDisplayPosition() const;

Returns the display position of the middle of the nearest bond.

### **GetDist**

double GetDist() const

Returns the distance associated with the bond.

## **IsValid**

bool IsValid() const

Returns whether the OENearestBond object is initialized correctly.

## 4.1.50 OEPen

class OEPen

The OEPen class encapsulates properties that determine the way various lines, curves and shapes are drawn.

Currently the OEPen class stores the following properties:

| Property         | Get method             | Set method             | Corresponding<br>namespace/class |
|------------------|------------------------|------------------------|----------------------------------|
| background color | OEPen.GetBackColor     | OEPen.SetBackColor     | <b>OEColor</b>                   |
| foreground color | OEPen.GetForeColor     | OEPen.SetForeColor     | <b>OEColor</b>                   |
| fill             | OEPen.GetFill          | OEPen.SetFill          | OEFill                           |
| line join        | OEPen.GetLineJoin      | OEPen.SetLineJoin      | OELineJoin                       |
| line cap         | OEPen.GetLineCap       | OEPen.SetLineCap       | OELineCap                        |
| line width       | OEPen.GetLineWidth     | OEPen.SetLineWidth     | none                             |
| line stipple     | OEPen.SetLineStipple   | OEPen.GetLineStipple   | OEStipple                        |
| stipple factor   | OEPen.SetStippleFactor | OEPen.GetStippleFactor | none                             |

## **Constructors**

OEPen()

Default constructor that initializes an OEPen object with the following properties:

| Property         | Default value                    |
|------------------|----------------------------------|
| background color | OEWhite = $OEColor(255,255,255)$ |
| foreground color | OEBlack = $OEColor(0,0,0)$       |
| fill             | OEFill_Default                   |
| line join        | OELineJoin_Default               |
| line cap         | OELineCap_Default                |
| line width       | 1.0                              |
| line stipple     | OEStipple_Default                |
| stipple factor   | 1                                |

### Table 10: Default parameters of OEPen

```
OEPen (const OESystem:: OEColor & bq, const OESystem:: OEColor & fq,
      unsigned int fill=OEFill::Off, double linewidth=1.0)
```

Creates and initializes an OEPen object with the given parameters. The other properties of the pen are set to the default values (see table above).

 $bg, fg$  The background and foreground color of the pen.

*fill* The *fill* property of the pen.

linewidth The line width property of the pen.

```
OEPen (const OEPen & rhs)
```

Copy constructor.

#### operator=

OEPen & operator= (const OEPen & rhs)

Assignment operator.

#### operator!=

bool operator! = (const OEPen &) const

Determines whether two OEPen objects are different. Two OEPen objects are considered different, if any of their properties (such as line width, background color, etc.) are different.

#### operator==

bool operator == (const OEPen &) const

Determines whether two OEPen objects are equal. Two OEPen objects are considered equivalent only if all of their properties (such as line width, background color, etc.) are identical.

## **GetBackColor**

const OESystem:: OEColor & GetBackColor() const

Returns the background color of the OEPen object that is used to fill shapes.

- · OEPen. SetBackColor method
- · OEPen. SetFill method
- OEColor class

### **GetFill**

unsigned int GetFill() const

If the returned value is  $OEFill$  On, than shapes drawn with the OEPen object are filled with the background color of the pen. If the returned value is  $OEFill\_Off$ , than shapes drawn with the *OEPen* object are left "empty" *i.e.* only their outlines are drawn using the foreground color of the pen.

See also:

- OEPen. SetFill method
- · OEPen. SetBackColor method
- OEFill namespace

### **GetForeColor**

const OESystem:: OEColor & GetForeColor () const

Returns the foreground color of the OEPen object that controls the color of the strokes when drawing lines, curves and outlines of shapes.

#### See also:

- · OEPen. SetForeColor method
- OEColor class

#### **GetLineCap**

unsigned int GetLineCap() const

Returns the *line cap* property of the OEPen object that controls how the endpoints of lines are drawn. The return value is taken from the *OELineCap* namespace.

#### See also:

- · OEPen. SetLineCap method
- $\bullet$  OELineCap namespace

#### **GetLineJoin**

unsigned int GetLineJoin() const

Returns the *line join* property of the *OEPen* object that controls how lines connect at corners when drawing outlines. The return value is taken from the  $OELineJoin$  namespace.

- · OEPen. SetLineJoin method
- · OELineJoin namespace

#### **GetLineStipple**

unsigned short GetLineStipple() const

Returns the *line stipple* property of the *OEPen* object that controls the pattern of dashes and gaps used to draw lines and outlines. The return value is taken from the  $OESLipple$  namespace.

See also:

- · OEPen. SetLineStipple method
- · OEPen. SetStippleFactor method
- OEStipple namespace

### **GetLineWidth**

double GetLineWidth() const

Returns the line width of the OEPen object that controls the width of strokes used when drawing lines, curves and outlines of shapes.

#### See also:

• OEPen, Set LineWidth method

#### **GetStippleFactor**

unsigned short GetStippleFactor() const

Returns the *stipple factor* of the *OEPen* object. The stipple factor is a multiplier that is used when drawing stipple patterns. For example, if the factor is three, then the stipple pattern is stretched to three times of its original size.

See also:

- OEPen. SetStippleFactor method
- · OEPen. SetLineStipple method

#### **SetBackColor**

void SetBackColor (const OESystem:: OEColor &col)

Sets the background color of the OEPen object that is used to fill shapes.

Example (Figure: Example of using the SetBackColor method)

```
pen = oedepict.OEPen()
pen.SetFill(oedepict.OEFill_On)
pen.SetBackColor(oechem.OEBlueTint)
```

Note: In order to fill a shape using the background color, the fill property of the OEPen has to be turned on (OEFill\_On). (See OEPen. SetFill method and OEFill namespace)

![](_page_339_Figure_1.jpeg)

### Fig. 203: Example of using the SetBackColor method

- · OEPen. GetBackColor method
- · OEPen. GetFill method
- OEColor class

#### **SetFill**

void SetFill (unsigned int fill)

Sets the fill property of the OEPen object.

*fill* This value has to be from the  $OEFill$  namespace.

#### See also:

- · OEPen. GetFill method
- · OEPen. GetBackColor method
- OEFill namespace

#### **SetForeColor**

void SetForeColor (const OESystem:: OEColor &col)

Sets the foreground color of the OEPen object that controls the color of the stroke when drawing lines, curves and outlines of shapes.

Example (Figure: Example of using the SetForeColor method)

```
pen = oedepict.OEPen()
pen.SetForeColor(oechem.OERed)
```

![](_page_339_Picture_19.jpeg)

Fig. 204: Example of using the SetForeColor method

### See also:

· OEPen. GetForeColor method

• OEColor class

### **SetLineCap**

```
void SetLineCap (unsigned int cap)
```

Sets the *line cap* property of the OEPen object that controls how the endpoints of lines are drawn.

*cap* This value has to be from the  $OELineCap$  namespace.

Example (Figure: Example of using the SetLineCap method)

```
pen = oedepict.OEPen()
pen.SetLineWidth(4)
pen.SetLineCap(oedepict.OELineCap_Square)
```

![](_page_340_Picture_8.jpeg)

#### Fig. 205: Example of using the SetLineCap method

### See also:

- · OEPen. GetLineCap method
- · OELineCap namespace

### **SetLineJoin**

void SetLineJoin (unsigned int join)

Sets the *line join* property of the OEPen object that controls how lines connect at corners when drawing outlines.

*join* This value has to be from the  $OELineJoin$  namespace.

Example (Figure: Example of using the SetLineJoin method)

```
pen = oedepict.OEPen()
pen.SetLineWidth(4)
pen.SetLineJoin(oedepict.OELineJoin_Miter)
```

![](_page_340_Picture_19.jpeg)

Fig. 206: Example of using the SetLineJoin method

#### See also:

- · OEPen. GetLineJoin method
- · OELineJoin namespace

#### **SetLineStipple**

```
void SetLineStipple (unsigned short pattern)
```

Sets the line stipple property of the OEPen object that controls the pattern of dashes and gaps used to draw lines and outlines.

*pattern* This value has to be from the  $OESLipple$  namespace.

**Example** (Figure: Example of using the SetLineStipple method)

```
pen = oedepict.OEPen()
pen.SetLineStipple(oedepict.OEStipple_ShortDash)
```

![](_page_341_Figure_10.jpeg)

![](_page_341_Figure_11.jpeg)

#### See also:

- · OEPen. SetLineStipple method
- · OEPen. SetStippleFactor method
- OEStipple namespace

### **SetLineWidth**

```
void SetLineWidth (double width)
```

Sets the line width of the OEPen object that controls the width of strokes used when drawing lines, curves and outlines of shapes.

width This value has to be a positive number.

Example (Figure: Example of using the SetLineWidth method)

```
pen = oedepict.OEPen()
pen.SetLineWidth(5.0)
```

#### See also:

· OEPen. GetLineWidth method

![](_page_342_Picture_1.jpeg)

### Fig. 208: Example of using the SetLineWidth method

### **SetStippleFactor**

void SetStippleFactor (unsigned short factor)

Sets the *stipple factor* of the *OEPen* object. The stipple factor is a multiplier that is used when drawing stipple patterns.

Example (Figure: Example of using the SetStippleFactor method)

```
pen = oedepict.OEPen()
pen.SetLineStipple(oedepict.OEStipple_ShortDash)
pen.SetStippleFactor(2)
```

![](_page_342_Figure_8.jpeg)

### Fig. 209: Example of using the SetStippleFactor method

#### See also:

- · OEPen. GetStippleFactor method
- · OEPen. GetLineStipple method

## 4.1.51 OEPrepareDepictionOptions

class OEPrepareDepictionOptions

This class represents OEPrepareDepictionOptions that stores the following parameters that are used when preparing a molecule for depiction.

| Property                                       | Get method                      | Set method                      | Corresponding namespace / type |
|------------------------------------------------|---------------------------------|---------------------------------|--------------------------------|
| re-generating 2D coordinates                   | <i>GetClearCoords</i>           | <i>SetClearCoords</i>           | boolean                        |
| adding depiction hydrogens                     | <i>GetAddDepictionHydrogens</i> | <i>SetAddDepictionHydrogens</i> | boolean                        |
| perceiving MDL bond stereo (wedge/hash)        | <i>GetPerceiveBondStereo</i>    | <i>SetPerceiveBondStereo</i>    | boolean                        |
| suppressing explicit (non-depiction) hydrogens | <i>GetSuppressHydrogens</i>     | <i>SetSuppressHydrogens</i>     | boolean                        |
| depiction orientation                          | <i>GetDepictOrientation</i>     | <i>SetDepictOrientation</i>     | DepictOrientation              |

## See also:

· OEPrepareDepiction function

See the effect of the above parameters in Table: Depictions generated with various parameter combinations when depiction are generated from the following input:

- SMILES Parsing the "CC([C@@H]1C[C@@H]2C[C@H]1NC2)N(H)(H)" string with three explicit hydrogens necessary to define tetrahedral stereo centers and two additional explicit hydrogens.
- MDL Reading an MDL file with 2D coordinates and pre-assigned wedge/hash bonds. It also includes two explicit hydrogens.

| $in-$<br>dex                             | clear coor-<br>dinates                      | suppress<br>explicit H                 | add depict<br>$\boldsymbol{\mathsf{H}}$ | perceive<br>wedge/hash        | from SMILES                      | from MDL                               |
|------------------------------------------|---------------------------------------------|----------------------------------------|-----------------------------------------|-------------------------------|----------------------------------|----------------------------------------|
|                                          | $\boldsymbol{\mathrm{F}}$                   | $\mathbf F$                            | $\mathbf F$                             | $\boldsymbol{\mathrm{F}}$     | н<br>$\mathsf{H}^{\bullet}$<br>н | н                                      |
| (1)<br>$\overline{(2)}$                  | $\overline{F}$                              | $\overline{F}$                         | $\overline{\mathrm{F}}$                 | $\overline{\mathbf{T}}$       |                                  |                                        |
| $\overline{(3)}$                         | $\overline{F}$                              | $\overline{F}$                         | $\overline{\mathbf{T}}$                 | $\overline{F}$                |                                  |                                        |
| (4)                                      | $\boldsymbol{\mathrm{F}}$                   | $\rm F$                                | $\mathbf T$                             | $\mathbf T$                   | Н<br>⊣⇒N                         | $_{\rm s}^{\rm H}$                     |
| $\overline{(5)}$                         | $\overline{F}$                              | $\overline{\mathbf{T}}$                | $\overline{F}$                          | $\overline{F}$                |                                  |                                        |
| $\overline{\boldsymbol{\left(6\right)}}$ | $\overline{F}$                              | $\overline{\mathbf{T}}$                | $\overline{F}$                          | $\overline{\mathbf{T}}$       |                                  |                                        |
| $\overline{(7)}$                         | $\overline{F}$                              | $\overline{\mathbf{T}}$                | $\overline{\mathbf{T}}$                 | $\overline{F}$                |                                  |                                        |
| (8)<br>$\overline{(9)}$                  | $\boldsymbol{\mathrm{F}}$<br>$\overline{T}$ | $\mathbf T$<br>$\overline{\mathrm{F}}$ | $\mathbf T$<br>$\overline{\mathrm{F}}$  | $\mathbf T$<br>$\overline{F}$ | $H_2N$                           | NH <sub>2</sub>                        |
| (10)                                     | $\mathbf T$                                 | $\boldsymbol{\mathrm{F}}$              | $\boldsymbol{\mathrm{F}}$               | $\mathbf T$                   | ا م ر                            | Н                                      |
| $\overline{(11)}$<br>(12)                | $\overline{\text{T}}$<br>$\mathbf T$        | $\overline{F}$<br>$\mathbf F$          | $\overline{\mathbf{T}}$<br>$\mathbf T$  | $\overline{F}$<br>$\mathbf T$ | Н<br>$H \bullet N$               | $\mathop{\mathbb{H}}\limits^{\bullet}$ |
| $\overline{(13)}$                        | $\overline{\mathbf{T}}$                     | $\overline{\mathbf{T}}$                | $\overline{F}$                          | $\overline{F}$                |                                  |                                        |
| $\overline{(14)}$                        | $\overline{T}$                              | $\overline{\mathbf{T}}$                | $\overline{F}$                          | $\overline{\mathbf{T}}$       |                                  |                                        |
| $\overline{(15)}$                        | $\overline{\mathbf{T}}$                     | $\overline{\mathbf{T}}$                | $\overline{\mathbf{T}}$                 | $\overline{F}$                |                                  |                                        |
| (16)                                     | $\mathbf T$                                 | $\mathbf T$                            | $\mathbf T$                             | $\mathbf T$                   | H<br>$H_2N$                      | Н<br>$H_2N$                            |

Table 11: Depictions generated with various parameter combinations

#### **Comments:**

- (1)  $MDL = no$  op;  $SMILES = generating 2D coordinates is necessary$
- (4) MDL = keeping original 2D coordinates, adding depiction hydrogens, re-perceiving wedge/hash bonds; SMILES = generating 2D coordinates, depiction hydrogens are kept; perceiving wedge/hash bonds
- (8) Default parameters; MDL = keeping original 2D coordinates, re-perceiving all other information; SMILES = generating 2D coordinates, regenerating all other information;
- (10) MDL = regenerating 2D coordinates and re-perceiving wedge/hash bonds (since no depiction hydrogens are added the wedge/hash bonds are on ring bonds); SMILES generating 2D coordinates and perceiving wedge/hash bonds;
- (12) Regenerating all information and keeping all explicit hydrogens
- (16) Regenerating all information; the depiction of identical molecules imported from SMILES and MDL will be identical

## **Constructors**

OEPrepareDepictionOptions (bool clearcoords=false, bool suppressH=true)

Default constructor that initializes an OEPrepareDepictionOptions object with the following properties:

clearcoords See the OEP repareDepictionOptions. SetClearCoords method.

suppressH See the OEPrepareDepictionOptions. SetSuppressHydrogens method.

#### Table 12: Default parameters of the OEPrepareDepictionOptions

| class                                          |                             |
|------------------------------------------------|-----------------------------|
| Property                                       | Default value               |
| re-generating 2D coordinates                   | false                       |
| adding depiction hydrogens                     | true                        |
| perceiving MDL bond stereo (wedge/hash)        | true                        |
| suppressing explicit (non-depiction) hydrogens | true                        |
| depiction orientation                          | OEDepictOrientation_Default |

OEPrepareDepictionOptions (const OEPrepareDepictionOptions & rhs)

Copy constructor.

#### operator=

OEPrepareDepictionOptions & operator=(const OEPrepareDepictionOptions & rhs)

Assignment operator.

### **GetAddDepictionHydrogens**

**bool** GetAddDepictionHydrogens() const

Returns whether the depiction hydrogens are kept/added.

#### See also:

· OEPrepareDepictionOptions. SetAddDepictionHydrogens method

### **GetClearCoords**

bool GetClearCoords() const

Returns whether the 2D coordinates of a molecule are re-calculated.

#### See also:

· OEPrepareDepictionOptions. SetClearCoords method

### **GetDepictOrientation**

unsigned int GetDepictOrientation() const

Returns the preferred orientation of the 2D coordinates. The return value is taken from the OEDepictOrientation namespace.

#### See also:

· OEPrepareDepictionOptions. SetDepictOrientation method

#### **GetPerceiveBondStereo**

bool GetPerceiveBondStereo() const

Returns whether the hash/wedge bonds are re-assigned.

#### See also:

· OEPrepareDepictionOptions. SetPerceiveBondStereo method

### GetSuppressHydrogens

bool GetSuppressHydrogens() const

Returns whether the explicit (non-depiction) hydrogens are suppressed.

#### See also:

· OEPrepareDepictionOptions. SetSuppressHydrogens method

### **SetAddDepictionHydrogens**

void SetAddDepictionHydrogens (bool)

Sets whether depiction hydrogens are kept/added.

#### See also:

- · OEAddDepictionHydrogens function
- · OEPrepareDepictionOptions.GetAddDepictionHydrogens method

## **SetClearCoords**

void SetClearCoords (bool clearcoords)

Sets whether the 2D coordinates of the molecule are re-calculated. If the molecule has no 2D coordinates, then the 2D coordinates are always calculated by calling the OEDepictCoordinates regardless of this setting.

#### See also:

- · OEDepictCoordinates function
- OEPrepareDepictionOptions.GetClearCoords method

### **SetDepictOrientation**

void SetDepictOrientation (unsigned int orientation)

Sets the preferred orientation of the 2D coordinates.

orientation This value has to be from the OEDepictOrientation namespace.

#### See also:

- OEPrepareDepictionOptions.GetDepictOrientation method
- · OEDepictOrientation namespace

## **SetPerceiveBondStereo**

void SetPerceiveBondStereo (bool)

Sets whether to re-assign the wedge and hash bonds by calling the OEMDLPerceiveBondStereo function.

- · OEMDLPerceiveBondStereo function in the OEChem TK manual
- · OEPrepareDepictionOptions.GetPerceiveBondStereo method

#### **SetSuppressHydrogens**

void SetSuppressHydrogens (bool)

Sets whether the explicit (non-depiction) hydrogens are suppressed in the molecule. Only hydrogens that are necessary to faithfully represent tetrahedral stereo-chemistry will be kept.

#### See also:

- OESuppressHydrogens function in the OEChem TK manual
- OEPrepareDepictionOptions. GetSuppressHydrogens method

## 4.1.52 OEReport

#### class OEReport

This class represents a layout manager that allows generation of multi-page images with two types of page layouts:

- **body** The *body* page layout provides a convenient way to position information in the middle of the page relative to the page footers and headers. For example, see the  $1^{st}$  page in Figure: Schematic representation of documents that can be created using the OEReport class.
- grid The grid page layout provides a convenient way to organize information (such as text and molecule depiction) into rows and columns. For example, see the  $2^{nd}$  and  $3^{rd}$  pages in Figure: Schematic representation of documents that can be created using the OEReport class.

#### See also:

- Multi Page Reports section
- Depicting Molecules in Multi-Page example
- Depicting MDL Query Substructure Search Hits example
- OEReportOptions class
- · OEWriteReport function
- · OEWriteReportToString function

#### **Constructors**

OEReport (const OEReportOptions &opts)

Initializes an OEReport object using the given options.

**opts** The OEReportOptions object that stores parameters determining the layout of the body and the grid pages of the report.

OEReport (unsigned int rowsperpage, unsigned int colsperpage)

Initializes an *OEReport* object with the given parameters.

rowsperpage The number of rows on each grid layout page.

*colsperpage* The number of columns on each *grid* layout page.

![](_page_349_Figure_1.jpeg)

#### Fig. 210: Schematic representation of documents that can be created using the OEReport class

Note: When a report is initialized with only the number of rows and columns per page parameter, all other parameters defining the layout of the pages will be initialized from the default constructor of the OEReportOptions class.

### See also:

• OEReportOptions class

#### **GetBodies**

OESystem::OEIterBase<OEImageBase> \*GetBodies()

Returns an iterator over all page bodies that have been created by calling the OEReport. NewBody method.

Note: If no page has been created by the OEReport. NewBody method, then the OEReport. GetBodies method returns an empty iterator.

See example in Figure: Example of accessing all page bodies of the report, where body areas in the  $1^{st}$  and  $5^{th}$  page are returned.

```
for body in report. GetBodies():
   pass
```

| page 1                                                           | page 2                                                                    | page 3                                                                    | page 4                                                                    | page 5                                                           |
|------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------------------------------------|
| Image: page layout with large grey central rectangle labeled (1) | Image: page layout with six small grey rectangles arranged in two columns | Image: page layout with six small grey rectangles arranged in two columns | Image: page layout with six small grey rectangles arranged in two columns | Image: page layout with large grey central rectangle labeled (2) |

### Table 13: Example of accessing all page bodies of the report. (The numbers inside the cells represent the order in which they are returned)

#### See also:

- · OEReport. GetBody method
- · OEReport. NewBody method

#### **GetBody**

OEImageBase \*GetBody (unsigned int p)

Returns the OEImageBase pointer of the body area of the  $p^{th}$  page.

**p** This value has to be in the range from *l* to  $OEReport$ . NumPages ().

Note: If the  $p^{th}$  page of the report was not created by the OEReport. NewBody method or the p page index is out of range, then the OEReport. GetBody method returns a NULL pointer.

#### See also:

- · OEReport. GetBodies method
- · OEReport. NewBody method

#### **GetCell**

OEImageBase \*GetCell(unsigned int p, unsigned int r, unsigned int c)

Returns the OEImageBase pointer for the cell positioned in the  $r^{th}$  row and  $c^{th}$  columns on the  $p^{th}$  page.

**p** This value has to be in the range from  $I$  to OEReport. NumPages ().

r This value has to be in the range from  $I$  to  $OEReport$ . NumRowsPerPage().

c This value has to be in the range from  $I$  to OEReport. NumColsPerPage ().

Note: If the cell positioned in the  $r^{th}$  row and  $c^{th}$  columns on the  $p^{th}$  page has not been created by the OEReport. NewCell method, then the OEReport. GetCell method returns a NULL pointer.

- · OEReport. GetCells method
- · OEReport. NewCell method

## **GetCellHeight**

double GetCellHeight () const

Returns the height of the cells on the grid page of the OEReport object.

### **GetCellWidth**

double GetCellWidth() const

Returns the width of the cells on the grid page of the OEReport object.

### **GetCells**

```
OESystem:: OEIterBase<OEImageBase> *GetCells (unsigned int page=0,
                                              unsigned int row=0,
                                              unsigned int col=0)
```

Returns an iterator over cells that have been created by calling the OEReport. NewCell method. The cells are returned in the order in which they have been created *i.e.* from left to right and top to bottom order on each grid page.

*page* This value has to be in the range from  $\theta$  to OEReport. NumPages ().

row This value has to be in the range from  $0$  to OEReport. NumRowsPerPage ().

col This value has to be in the range from  $0$  to OEReport. NumColsPerPage ().

Example (Figure: Example of accessing all cells of the report)

```
for cell in report. GetCells():
   pass
```

| Table 14: <b>Example of accessing all cells of the report</b> . (The numbers |  |  |
|------------------------------------------------------------------------------|--|--|
| inside the cells represent the order in which they are returned)             |  |  |

| page 1 | page 2 |     | page 3 |      | page 4 |      | page 5 |
|--------|--------|-----|--------|------|--------|------|--------|
|        |        |     |        |      |        |      |        |
|        | (1)    | (2) | (7)    | (8)  | (13)   | (14) |        |
|        | (3)    | (4) | (9)    | (10) | (15)   | (16) |        |
|        | (5)    | (6) | (11)   | (12) | (17)   | (18) |        |
|        |        |     |        |      |        |      |        |

**Example** (Figure: Example of accessing all cells on the given row on each page)

```
row = 2for cell in report. GetCells(0, row, 0):
    pass
```

Table 15: Example of accessing all cells on the given row on each page. (The numbers inside the cells represent the order in which they are returned)

![](_page_352_Figure_3.jpeg)

**Example** (Figure: Example of accessing all cells on the given column on each page)

```
col = 2for cell in report. GetCells(0, 0, col):
    pass
```

## Table 16: Example of accessing all cells on the given column on each

page. (The numbers inside the cells represent the order in which they are returned)

| page 1 | page 2 | page 3 | page 4 | page 5 |
|--------|--------|--------|--------|--------|
|        | (1)    | (4)    | (7)    |        |
|        | (2)    | (5)    | (8)    |        |
|        | (3)    | (6)    | (9)    |        |

Example (Figure: Example of accessing all cells on the given row and column on each page)

```
row = 2col = 2for cell in report. GetCells (0, row, col):
    pass
```

Table 17: Example of accessing all cells on the given row and column on each page. (The numbers inside the cells represent the order in which they are returned)

![](_page_353_Figure_3.jpeg)

**Example** (Figure: Example of accessing all cells on the given row and page)

```
page = 3row = 2for cell in report. GetCells (page, row, 0) :
    pass
```

## Table 18: Example of accessing all cells on the given row and page.

(The numbers inside the cells represent the order in which they are returned)

| page 1 | page 2 | page 3   | page 4 | page 5 |
|--------|--------|----------|--------|--------|
|        |        | (1)  (2) |        |        |

**Example** (Figure: Example of accessing all cells on the given column and page)

```
page = 3col = 2for cell in report. GetCells (page, 0, col):
    pass
```

![](_page_354_Figure_1.jpeg)

Table 19: Example of accessing all cells on the given column and page. (The numbers inside the cells represent the order in which they are returned)

Example (Figure: Example of accessing a cell on the given row, column and page)

page =  $3$ row =  $2$  $col = 2$ for cell in report. GetCells (page, row, col): pass

## Table 20: Example of accessing a cell on the given row, column and

page. (The numbers inside the cells represent the order in which they are returned)

| page 1 | page 2 | page 3 | page 4 | page 5 |
|--------|--------|--------|--------|--------|
|        |        | (1)    |        |        |

- · OEReport.GetCell method
- · OEReport. NewCell method

### **GetFooter**

OEImageBase \*GetFooter (unsigned int p)

Returns the *OEImageBase* pointer of the footer on the  $p^{th}$  page.

**p** This value has to be in the range from *l* to  $OEReport$ . NumPages ().

Note: If the OEReport object was initialized with footer height 0.0 or the  $p$  page index is out of range, then the OEReport. GetFooter method returns a NULL pointer.

#### See also:

- · OEReport.GetFooterHeight method
- · OEReport. GetFooterWidth method
- · OEReport. GetFooters methods

### **GetFooterHeight**

double GetFooterHeight() const

Returns the height of the footer at the bottom of each page.

#### See also:

· OEReport. GetFooterWidth method

## **GetFooterWidth**

double GetFooterWidth() const

Returns the width of the footer at the bottom of each page.

#### See also:

· OEReport. GetFooterHeight methods

## **GetFooters**

OESystem:: OEIterBase<OEImageBase> \*GetFooters()

Returns an iterator over all footers of the OEReport object.

Note: If the OEReport object was initialized with footer height 0.0, then the OEReport. GetFooters method returns an empty iterator.

Example (Figure: Example of accessing all page footers of the report)

```
for footer in report. GetFooters():
   pass
```

Table 21: Example of accessing all page footers of the report. (The numbers inside the footer areas represent the order in which they are returned)

| page 1 | page 2 | page 3 | page 4 | page 5 |
|--------|--------|--------|--------|--------|
|        |        |        |        |        |
| (1)    | (2)    | (3)    | (4)    | (5)    |

See also:

- · OEReport. GetFooter method
- · OEReport.GetFooterHeight method
- · OEReport. GetFooterWidth method

#### **GetHeader**

OEImageBase \*GetHeader (unsigned int p)

Returns the OEImageBase pointer of the header on the  $p^{th}$  page.

**p** This value has to be in the range from  $I$  to OEReport. NumPages ().

**Note:** If the OEReport object was initialized with header height  $0.0$  or the p page index is out of range, then the OEReport. GetHeader method returns a NULL pointer.

- · OEReport.GetHeaderHeight method
- · OEReport.GetHeaderWidth method
- · OEReport. GetHeaders method

### **GetHeaderHeight**

double GetHeaderHeight () const

Returns the height of the header at the top of each page.

#### See also:

· OEReport.GetHeaderWidth method

### **GetHeaderWidth**

double GetHeaderWidth() const

Returns the width of the header at the top of each page.

#### See also:

· OEReportOptions. GetHeaderHeight methods

#### **GetHeaders**

OESystem:: OEIterBase<OEImageBase> \*GetHeaders()

Returns an iterator over all headers of the OEReport object.

Note: If the OEReport object was initialized with header height 0.0, then the OEReport. GetHeaders method returns an empty iterator.

Example (Figure: Example of accessing all page headers of the report)

```
for header in report. GetHeaders () :
    pass
```

## Table 22: Example of accessing all page headers of the report. (The

numbers inside the header areas represent the order in which they are returned)

#### See also:

· OEReport. GetHeader method

- · OEReport.GetHeaderHeight method
- · OEReport.GetHeaderWidth method

## **GetOptions**

const OEReportOptions &GetOptions () const

Returns the options used to initialize the OEReport object.

#### See also:

• OEReportOptions class

## **GetPage**

OEImageBase \*GetPage(unsigned int p)

Returns the *OEImageBase* pointer of the  $p^{th}$  page.

**p** This value has to be in the range from *l* to  $OEReport$ . NumPages ().

Note: If  $p$  page index is out of range, then the OEReport. GetPage method returns a NULL pointer.

#### See also:

· OEReport. GetPages method

### **GetPageHeight**

double GetPageHeight () const

Returns the height of the pages of the report.

### See also:

· OEReportOptions. SetPageHeight method

## **GetPageWidth**

double GetPageWidth() const

#### Returns the width of the pages of the report.

#### See also:

· OEReportOptions. SetPageWidth method

## **GetPages**

OESystem:: OEIterBase<OEImageBase> \*GetPages()

Returns an iterator over all the pages of the OEReport object.

#### See also:

· OEReport. GetPage method

### **IsBodyPage**

bool IsBodyPage (unsigned int p) const

Returns whether the  $p^{th}$  page of the report is created by calling the OEReport. NewBody method.

 $p$  This value has to be in the range from  $l$  to OEReport. NumPages ().

For example, the OEReport. IsBodyPage method returns true for the  $1^{st}$  and  $5^{th}$  pages of the report shown in Figure: Example of report layout.

|            | page 1                  | page 2                  | page 3                  | page 4                  | page 5                  |
|------------|-------------------------|-------------------------|-------------------------|-------------------------|-------------------------|
|            | Image: page-1 thumbnail | Image: page-2 thumbnail | Image: page-3 thumbnail | Image: page-4 thumbnail | Image: page-5 thumbnail |
| IsBodyPage | true                    | false                   | false                   | false                   | true                    |

Table 23: Example of report layout

#### See also:

- · OEReport. IsGridPage method
- · OEReport. NewBody method

### **IsGridPage**

bool IsGridPage(unsigned int p) const

Returns whether the  $p^{th}$  page of the report is created by calling the OEReport. NewCell method.

 $p$  This value has to be in the range from  $l$  to OEReport. NumPages ().

For example, the OEReport. Is GridPage method returns true for the  $2^{nd}$ ,  $3^{rd}$ , and  $4^{th}$  pages of the report shown in Figure: Example of report layout.

|                   | page 1                                                        | page 2                                        | page 3                                        | page 4                                        | page 5                                                        |
|-------------------|---------------------------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|---------------------------------------------------------------|
|                   | Image: single-column page layout (header, large body, footer) | Image: grid page layout with six small panels | Image: grid page layout with six small panels | Image: grid page layout with six small panels | Image: single-column page layout (header, large body, footer) |
| <b>IsGridPage</b> | false                                                         | true                                          | true                                          | true                                          | false                                                         |

Table 24: Example of report layout

#### See also:

- · OEReport. IsBodyPage method
- · OEReport. NewCell method

#### **NewBody**

OEImageBase \*NewBody()

Creates a new body layout page and returns the area between the header and the footer. See example in Figure: Example of creating a new body page.

Note: The height and width of the returned area depend on the options with which the OEReport object was constructed: page margins, gap between the cells, and the height of the header and footer.

| $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ and $\mu$ |        |        |  |  |  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|--------|--|--|--|
| page 1                                                                                                                                                                                                                                                | page 2 | page 3 |  |  |  |
|                                                                                                                                                                                                                                                       |        |        |  |  |  |

Table 25: **Example of creating a new body page** (The area returned by the NewBody method is highlighted by red color)

- · OEReport. IsBodyPage method
- · OEReport. GetBody method
- · OEReport. GetBodies method

### **NewCell**

```
OEImageBase *NewCell()
```

Creates and returns a new cell. If the last page of the report is a *grid* page, then a new cell is created from left to right and top to bottom order. If no more cells are left on the *grid* page or the last page is a *body* page, then a new *grid* page is created before returning the first cell of this new page. See example in Figure: Example of creating a new cell.

Note: The cells of a grid page are equal-sized and evenly spaced. The height and width of the cells depend on the options with which the OEReport object was constructed: the number of rows and columns per page, page margins, gap between the cells, and the height of the header and footer.

![](_page_361_Figure_5.jpeg)

Table 26: Example of creating a new cell (The area *i.e.* the cell returned by the NewCell method is highlighted by red color)

### See also:

- · OEReport. IsGridPage method
- · OEReport.GetCell method
- · OEReport. GetCells method

### **NumBodyPages**

unsigned int NumBodyPages() const

Returns the number of *body* pages of the *OEReport* object, *i.e.* the number of pages for which the *OEReport*. IsBodyPage method returns true.

- · OEReport. IsBodyPage method
- OEReport. NumGridPages method
- · OEReport. NumPages method

#### **NumColsPerPage**

unsigned int NumColsPerPage() const

Returns the number of columns on each *grid* page of the *OEReport* object.

#### See also:

· OEReport. NumRowsPerPage method

### **NumGridPages**

unsigned int NumGridPages () const

Returns the number of grid pages of the OEReport object, i.e. the number of pages for which the OEReport. IsGridPage method returns true.

#### See also:

- · OEReport. IsGridPage method
- · OEReport. NumBodyPages method
- OEReport. NumPages method

#### **NumPages**

unsigned int NumPages () const

Returns the number of pages of the OEReport object. This is the sum of the numbers returned by the OEReport. NumBodyPages and OEReport. NumGridPages methods.

#### See also:

- · OEReport. NumBodyPages method
- · OEReport. NumGridPages method

#### **NumRowsPerPage**

unsigned int NumRowsPerPage() const

Returns the number of rows on each grid page of the OEReport object.

#### See also:

· OEReport. NumColsPerPage method

## **4.1.53 OEReportOptions**

## class OEReportOptions

This class represents the OEReportOptions class that encapsulates properties that determine the layout of a OEReport object.

See Figure: Schematic representation of documents that can be created using the OEReport class.

![](_page_363_Figure_5.jpeg)

### Fig. 211: Schematic representation of documents that can be created using the OEReport class

The OEReportOptions class stores the following properties:

| Property            | Get method                                    | Set method                                                              | Corresponding<br>namespace /<br>class / type                           |
|---------------------|-----------------------------------------------|-------------------------------------------------------------------------|------------------------------------------------------------------------|
| rows per<br>page    | <i>NumRowsPerPage</i>                         | Set upon construction                                                   | integer greater than 0                                                 |
| columns per<br>page | <i>NumColsPerPage</i>                         | Set upon construction                                                   | integer greater than 0                                                 |
| page width          | <i>GetPageWidth</i>                           | <i>SetPageWidth</i><br><i>SetPageSize</i><br><i>SetPageOrientation</i>  | floating point number<br><i>OEPageSize</i><br><i>OEPageOrientation</i> |
| page height         | <i>GetPageHeight</i>                          | <i>SetPageHeight</i><br><i>SetPageSize</i><br><i>SetPageOrientation</i> | floating point number<br><i>OEPageSize</i><br><i>OEPageOrientation</i> |
| page<br>margins     | <i>GetPageMargin</i><br><i>GetPageMargins</i> | <i>SetPageMargin</i><br><i>SetPageMargins</i>                           | <i>OEMargin</i>                                                        |
| cell gap            | <i>GetCellGap</i>                             | <i>SetCellGap</i>                                                       | floating point number                                                  |
| header height       | <i>GetHeaderHeight</i>                        | <i>SetHeaderHeight</i>                                                  | floating point number                                                  |
| header width        | <i>GetHeaderWidth</i>                         | N/A                                                                     | floating point number                                                  |
| footer height       | <i>GetFooterHeight</i>                        | <i>SetFooterHeight</i>                                                  | floating point number                                                  |
| footer width        | <i>GetFooterWidth</i>                         | N/A                                                                     | floating point number                                                  |

## See also:

• OEReport class

## **Constructors**

```
OEReportOptions (unsigned int rowsperpage = 3, unsigned int colsperpage = 2)
```

rowsperpage The number of rows on each grid page of the report.

colsperpage The number of columns on each grid page of the report.

Note: Both the number of rows and columns per page have to be greater than 0.

| Property         | Default value                                        |
|------------------|------------------------------------------------------|
| rows per page    | 3                                                    |
| columns per page | 2                                                    |
| page width       | <i>OEGetPageWidth(OEPageSize_US_Letter)</i>          |
| page height      | <i>OEGetPageHeight(OEPageSize_US_Letter)</i>         |
| margins          | 20.0 (for each margins: top, bottom, left and right) |
| cell gap         | 5.0                                                  |
| header height    | 0.0 (no header is generated by default)              |
| footer height    | 0.0 (no footer is generated by default)              |

Example (Figure: Example of report generation with default options)

opts = oedepict.OEReportOptions(3, 2)

Table 28: Example of report generation with default options (The scale of the shown pages is 1:4)

OEReportOptions (const OEReportOptions & rhs)

#### Copy constructor.

### operator=

OEReportOptions & operator=(const OEReportOptions & rhs)

Assignment operator.

### **GetCellGap**

double GetCellGap() const

Returns the space between the cells of the report.

#### See also:

· OEReportOptions. SetCellGap method

### **GetCellHeight**

double GetCellHeight () const

Returns the height of the cells on the *grid* pages of the report.

Note: The height of the cells depends on the number of rows per page, the top and bottom margins, header and footer heights, and the gap between the cells

## **GetCellWidth**

double GetCellWidth() const

Returns the width of the cells on the *grid* pages of the report.

Note: The width of the cells depends on the number of columns per page, the left and right margins, and the gap between the cells.

#### **GetFooterHeight**

double GetFooterHeight() const

Returns the height of the footer at the bottom of each page.

#### See also:

· OEReportOptions. SetFooterHeight method

#### **GetFooterWidth**

double GetFooterWidth() const

Returns the width of the footer at the bottom of each page.

#### **GetHeaderHeight**

double GetHeaderHeight () const

Returns the height of the header at the top of each page.

#### See also:

· OEReportOptions. SetHeaderHeight method

## **GetHeaderWidth**

double GetHeaderWidth() const

Returns the width of the header at the top of each page.

### **GetPageHeight**

double GetPageHeight () const

Returns the height of the page of the report.

#### See also:

· OEReportOptions. SetPageHeight method

### **GetPageMargin**

double GetPageMargin (unsigned int margin) const

Returns the size of a specific page margin of the report.

**margin** This value has to be from the OEMargin namespace.

### See also:

- · OEReportOptions. SetPageMargin method
- · OEReportOptions. SetPageMargins method

## **GetPageWidth**

double GetPageWidth() const

Returns the width of the page of the report.

#### See also:

· OEReportOptions. SetPageWidth method

#### **NumColsPerPage**

unsigned int NumColsPerPage() const

Returns the number of columns on each grid page of the report.

#### See also:

• OEReportOptions. NumRowsPerPage method

## **NumRowsPerPage**

unsigned int NumRowsPerPage() const

Returns the number of rows on each grid page of the report.

#### See also:

· OEReportOptions. NumColsPerPage method

## **SetCellGap**

void SetCellGap (double size)

Sets the space between the cells of the report.

size This value has to be a non-negative number.

Example (Figure: Example of using the SetCellGap method)

opts = oedepict.OEReportOptions(3, 2) opts.SetCellGap(100)

### Table 29: Example of using the SetCellGap method (The scale of the shown pages is 1:4)

![](_page_368_Figure_13.jpeg)

#### See also:

· OEReportOptions. GetCellGap method

## **SetFooterHeight**

void SetFooterHeight (double height)

Sets the height of the footer at the bottom of each page.

height This value has to be a non-negative number.

Note: 0.0 means that a footer is **not** going to be created on the pages.

Example (Figure: Example of using the SetFooterHeight method)

 $opts = odepict.OEReportOptions (3, 2)$ opts.SetFooterHeight(100)

> Table 30: Example of using the SetFooterHeight method (The scale of the shown pages is  $1:4$ )

![](_page_369_Figure_9.jpeg)

#### See also:

· OEReportOptions.GetFooterHeight method

### **SetHeaderHeight**

void SetHeaderHeight (double height)

Sets the height of the header at the top of each page.

*height* This value has to be a non-negative number.

Note:  $0.0$  means that a header is **not** going to be created on the pages.

Example (Figure: Example of using the SetHeaderHeight method)

```
opts = oedepict.OEReportOptions(3, 2)
opts.SetHeaderHeight(100)
```

| Left-hand table |  |  | Right-hand table |  |  |  |  |  |  |  |  |
|-----------------|--|--|------------------|--|--|--|--|--|--|--|--|
|-----------------|--|--|------------------|--|--|--|--|--|--|--|--|

### Table 31: Example of using the SetHeaderHeight method (The scale of the shown pages is $1:4$ )

#### See also:

· OEReportOptions.GetHeaderHeight method

## **SetPageHeight**

void SetPageHeight (double height)

Sets the height of the pages of the report.

*height* This number has to be greater than 0.0.

Example (Figure: Example of using the SetPageHeight method)

```
opts = oedepict.OEReportOptions(3, 2)
opts.SetPageHeight(opts.GetPageHeight() * 0.50)
```

## Table 32: Example of using the SetPageHeight method (The scale of

the shown pages is  $1:4$ )

![](_page_370_Figure_14.jpeg)

- · OEReportOptions. SetPageOrientation method
- · OEReportOptions. SetPageSize method
- · OEReportOptions. GetPageWidth method

## **SetPageMargin**

void SetPageMargin (unsigned int margin, double size)

Sets the size of a specific page margin of the report.

**margin** This value has to be from the OEMargin namespace.

size This value has to be a non-negative number.

Example (Figure: Example of using the SetPageMargin method)

```
opts = oedepict.OEReportOptions(3, 2)
opts.SetPageMargin(oedepict.OEMargin_Left, 100)
opts.SetPageMargin(oedepict.OEMargin_Right, 100)
```

## Table 33: Example of using the SetPageMargin method (The scale of

the shown pages is  $1:4$ )

|  |  | _______________________________________                                    |  |
|--|--|----------------------------------------------------------------------------|--|
|  |  | the control of the control of the control of the control of the control of |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |
|  |  |                                                                            |  |

- · OEReportOptions. GetPageMargin method
- · OEReportOptions. SetPageMargins method

## **SetPageMargins**

void SetPageMargins (double size)

Sets the size of all the margins of the report.

size This value has to be a non-negative number.

Example (Figure: Example of using the SetPageMargins method)

```
opts = oedepict.OEReportOptions(3, 2)
opts.SetPageMargins(100)
```

## Table 34: Example of using the SetPageMargins method (The scale of

the shown pages is 1:4)

![](_page_372_Figure_9.jpeg)

See also:

- · OEReportOptions. GetPageMargin method
- · OEReportOptions. SetPageMargin method

### **SetPageOrientation**

void SetPageOrientation (unsigned int orientation)

Sets the orientation of the pages of the report.

orientation This value has to be from the OEPageOrientation namespace.

Example (Figure: Example of using the SetPageOrientation method)

```
opts = oedepict.OEReportOptions(3, 2)
opts.SetPageOrientation(oedepict.OEPageOrientation_Landscape)
```

## Table 35: Example of using the SetPageOrientation method (The scale of the shown pages is 1:4)

## See also:

- · OEReportOptions. SetPageHeight method
- · OEReportOptions. SetPageSize method
- · OEReportOptions. SetPageWidth method

## **SetPageSize**

void SetPageSize (unsigned int pagesize)

Sets the width and height of the pages of the report.

*pagesize* This value has to be from the  $OEPageSize$  namespace.

Example (Figure: Example of using the SetPageSize method)

```
opts = oedepict.OEReportOptions(3, 2)
opts.SetPageSize(oedepict.OEPageSize_US_Legal)
```

![](_page_374_Figure_1.jpeg)

## Table 36: Example of using the SetPageSize method (The scale of the shown pages is 1:4)

## See also:

- · OEReportOptions. SetPageOrientation method
- · OEReportOptions. SetPageHeight method
- · OEReportOptions. SetPageWidth method

## **SetPageWidth**

void SetPageWidth (double width)

Sets the width of the pages of the report.

width This number has to be greater than 0.0.

Example (Figure: Example of using the SetPageWidth method)

```
opts = oedepict.OEReportOptions(3, 2)
opts.SetPageWidth(opts.GetPageWidth() * 0.50)
```

*(No text in the image.)*

## Table 37: Example of using the SetPageWidth method (The scale of the shown pages is $1:4$ )

#### See also:

- · OEReportOptions. SetPageOrientation method
- · OEReportOptions. SetPageHeight method
- · OEReportOptions. SetPageSize method

## 4.1.54 OESVGClass

#### class OESVGClass

SVG class is a name that can be assigned with SVG elements.

- · OEIsValidSVGClassName function
- Generating Interactive SVG Images chapter
- OESVGGroup class

## **Constructors**

To create an OESVGClass object on an image use the OEImageBase. NewSVGClass method.

#### **GetName**

std::string GetName() const

Returns the name of the OESVGClass object.

## 4.1.55 OESVGGroup

#### class OESVGGroup

SVG group is a container for grouping and naming collections of SVG drawing elements.

#### See also:

- · OEIsValidSVGGroupId function
- Generating Interactive SVG Images chapter
- OESVGClass class

### **Constructors**

To create an OESVGGroup object on an image use the OEImageBase. NewSVGGroup method.

### **AddSVGClass**

bool AddSVGClass (const OESVGClass \*svg\_class)

Adds an OESVGClass object to the group. The SVG class and the SVG group have to be created on the same image.

### **GetId**

std::string GetId() const

Returns the name of the OESVGGroup object.

### **IsVisible**

```
bool IsVisible() const
```

Returns whether the objects drawn inside the given OESVGGroup will be visible when the image is opened.

# **4.2 OEDepict Constants**

## 4.2.1 OE2DMolDisplaySetup

This namespace encodes symbolic constants used as bit-masks to indicate which molecule depiction parameters are being created when invoking the OEConfigure2DMolDisplayOptions function.

#### See also:

• OE2DMolDisplayOptions class

## All

The combination of following constants:

- · OE2DMolDisplaySetup\_AromaticStyle
- · OE2DMolDisplaySetup\_AtomColorStyle
- OE2DMolDisplaySetup\_AtomPropDisplay
- · OE2DMolDisplaySetup\_AtomStereoStyle
- · OE2DMolDisplaySetup\_BondColorStyle
- · OE2DMolDisplaySetup\_BondPropDisplay
- · OE2DMolDisplaySetup\_BondStereoStyle
- · OE2DMolDisplaySetup DefaultLineWidth
- · OE2DMolDisplaySetup\_HydrogenStyle
- · OE2DMolDisplaySetup\_ProtectiveGroupStyle
- · OE2DMolDisplaySetup\_Scale
- · OE2DMolDisplaySetup\_SuperAtomStyle

### **AromaticStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the aromatic ring style.

```
Contents of parameter -aromstyle
   Aliases : -astl
   Type : string
   Allow list : false
   Default : Kekule
   Simple : true
   Required : false
   Legal values : Kekule Circle Dash
   Brief : Aromatic ring display style
   Detail
        API : OE2DMolDisplayOptions::SetAromaticStyle method and OEAromaticStyle.
  namesna
```

#### See also:

- · OEAromaticStyle namespace
- · OE2DMolDisplayOptions. SetAromaticStyle method

#### **AtomColorStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the atom color style.

```
Contents of parameter -atomcolor
   Aliases : -acolor
   Type : string
   Allow list : false
   Default : WhiteCPK
   Simple : true
   Required : false
   Legal values : WhiteCPK BlackCPK WhiteMonochrome BlackMonochrome cow cob bow wob
   Brief : Atom coloring style
   Detail
      API : OE2DMolDisplayOptions::SetAtomColorStyle method and OEAtomColorStyle
\rightarrownamespace
                    - (color on white) same as WhiteCPK
       COW
       \cosh- (color on black) same as BlackCPK
      how
                    - (black on white) same as WhiteMonochrome
       wob
                    - (white on black) same as BlackMonochrome
```

#### See also:

- · OEAtomColorStyle namespace
- · OE2DMolDisplayOptions. SetAtomColorStyle method

#### **AtomPropDisplay**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the atom property display.

```
Contents of parameter -atomprop
   Aliases : -aprop
   Type : string
   Allow list : false
   Default : Hidden
   Simple : true
   Required : false
   Legal values : Hidden AtomIdx MapIdx
   Brief : Atom property display
   Detail
```

```
API : OE2DMolDisplayOptions::SetAtomPropertyFunctor method,
→OEDisplayNoAtomProp, OEDisplayAtomIdx, and OEDisplayAtomMapIdx functors
```

See also:

- OEDisplayAtomIdx class
- OEDisplayAtomMapIdx class
- OEDisplayNoAtomProp class
- · OE2DMolDisplayOptions. SetBondPropertyFunctor method

#### **AtomStereoStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the atom stereo display style.

```
Contents of parameter -atomstereostyle
   Aliases : -atomsstl
   Type : string
   Allow list : false
   Default : AtomStereo | MDLStereoCenter | FancyStyle
   Simple : true
   Required : false
   Brief : Atom stereo display style
   Detail
        API : OE2DMolDisplayOptions::SetAtomStereoStyle method and OEAtomStereoStyle
\rightarrownamespace
        Primitive expressions :
                    - no atom stereo information is displayed
        Hidden
        AtomStereo - display wedge/hash bonds
        CIPAtomStereo - display S/R CIP stereo labels
        MDLStereoCenter - display ABS/AND/OR stereo labels
        StandardStyle - standard hash/wedge style
        FancyStyle - fancy hash/wedge style
        Combined expressions :
        Created by combining primitive tokens with |
```

- · OEAtomStereoStyle namespace
- · OE2DMolDisplayOptions. SetAtomStereoStyle method

### **BondColorStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the bond color style.

```
Contents of parameter -bondcolor
   Aliases : - bcolor
   Type : string
   Allow list : false
   Default : ByElement
   Simple : true
   Required : false
   Legal values : ByElement Monochrome
   Brief : Bond coloring style
   Detail
      API : OE2DMolDisplayOptions::SetBondColorStyle method and OEBondColorStyle
\rightarrownamespace
```

#### See also:

- · OEBondColorStyle namespace
- OE2DMolDisplayOptions. SetBondColorStyle method

### **BondPropDisplay**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the bond property display.

```
Contents of parameter -bondprop
  Aliases : -bprop
   Type : string
   Allow list : false
  Default : Hidden
  Simple : true
  Required : false
  Legal values : Hidden BondIdx
   Brief : Bond property display
   Detail
      API : OE2DMolDisplayOptions::SetBondPropertyFunctor method,
OEDisplayNoBondProp and OEDisplayBondIdx functors
```

- OEDisplayBondIdx class
- OEDisplayNoBondProp class
- · OE2DMolDisplayOptions. SetBondPropertyFunctor method

#### **BondStereoStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the bond stereo display style.

```
Contents of parameter -bondstereostyle
   Aliases : - bondsstl
   Type : string
   Allow list : false
   Default : BondStereo
   Simple : true
   Required : false
   Brief : Bond stereo display style
   Detail
       API : OE2DMolDisplayOptions::SetBondStereoStyle method and OEBondStereoStyle
\rightarrownamespace
       Primitive expressions :
       Hidden
       BondStereo
       CIPBondStereo
        Combined expressions :
        Created by combining primitive tokens with |
```

See also:

- · OEBondStereoStyle namespace
- · OE2DMolDisplayOptions. SetBondStereoStyle method

## **DefaultLineWidth**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the default bond line width.

```
Contents of parameter -linewidth
   Aliases : -linew
   Type : int
   Allow list : false
   Default : 2
   Simple : true
   Required : false
   Legal ranges :
       8 to 1
   Brief : Default bond line width
   Detail
      API : OE2DMolDisplayOptions::SetDefaultBondPen method and OEPen class
```

- · OE2DMolDisplayOptions. SetDefaultBondPen method
- OEPen class

## **HydrogenStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the hydrogen display style.

```
Contents of parameter -hydrstyle
   Aliases : - hstl
   Type : string
   Allow list : false
   Default : ImplicitHetero | ExplicitAll
   Simple : true
   Required : false
   Brief : Hydrogen display style
   Detail
       API : OE2DMolDisplayOptions::SetHydrogenStyle method and OEHydrogenStyle
\rightarrownamespace
       Primitive expressions :
       Hidden
       ImplicitHetero
       ImplicitTerminal
       ImplicitAll
       ExplicitHetero
       ExplicitTerminal
        ExplicitAll
        Combined expressions :
        Created by combining primitive tokens with |
```

#### See also:

- · OEHydrogenStyle namespace
- · OE2DMolDisplayOptions. SetHydrogenStyle method

### **ProtectiveGroupStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the protective group display style.

```
Contents of parameter -protgroupdisp
   Aliases : -pgroup
   Type : string
   Allow list : false
   Default : Off
   Simple : true
   Required : false
   Brief : Protective group display style
   Detail
       API : OE2DMolDisplayOptions::SetProtectiveGroupStyle method and
→OEProtectiveGroupStyle namespace
```

(continues on next page)

(continued from previous page)

| Primitive expressions :       |                          |                                                             |
|-------------------------------|--------------------------|-------------------------------------------------------------|
| Off                           | $ \,$                    | no protective group detection                               |
| All                           | $ \,$                    | detect all protective groups                                |
| Ac                            |                          | $-$ R-C (=0) C                                              |
| Ad                            |                          | $-$ R-C12CC3CC (C1) CC (C3) C2                              |
| Alloc                         |                          | $-$ R-C (=0) OCC=C                                          |
| Bn, Bzl, Benzyl - R-Cclccccc1 |                          |                                                             |
| <b>BOC</b>                    |                          | $-$ R-C (=0) OC (C) (C) (C)                                 |
| Bom                           |                          | - R-COCclecccc1                                             |
| Bpoc                          |                          | $-$ R-C (=0) OC (C) (C) clccc (cc1) c2ccccc2                |
| Bs                            |                          | $-$ R-S(=0)(=0)clccc(ccl)Br                                 |
| <b>Bt</b>                     |                          | $-$ R-n1c2ccccc2nn1                                         |
| <b>Btm</b>                    |                          | $-$ R-CScleccccl                                            |
| Bz, Benzoyl                   |                          | $-$ R-C (=0) clccccc1                                       |
| Bzh                           |                          | $-$ R-C (cleccecl) c2ccccc2                                 |
| BzOM                          |                          | $-$ R-COcleccccl                                            |
| CHX                           |                          | $-$ R-C1CCCCC1                                              |
|                               |                          |                                                             |
| Dan, Dansyl                   |                          | $-$ R-S (=0) (=0) clcccc2clcccc2N (C) C                     |
| DCB                           |                          | $-$ R-Cc1c (cccc1C1) C1                                     |
| DDE                           | $ \,$                    | $R-C$ (=C1C (=O) CC (CC1=O) (C) C) C                        |
| DDIV                          | $\overline{\phantom{a}}$ | $R-C$ (=C1C (=O) CC (CC1=O) (C) C) CC (C) C                 |
| DEIPS                         |                          | $-$ R-[Si] (CC) (CC) C(C) C                                 |
| DMAB                          |                          | $-$ R-Cc1ccc (cc1) NC (=C2C (=0) CC (CC2=0) (C) C) CC (C) C |
| DMIPS                         |                          | $-$ R-[Si](C)(C)C(C)C                                       |
| DMPM                          |                          | $-$ R-Cc1ccc(c(c1)OC)OC                                     |
| <b>DMPS</b>                   | $ \,$                    | $R-[Si](C)(C)$ cleccccl                                     |
| DMTr                          |                          | $-$ R-C (cleececl) (c2cec (ec2) OC) c3cec (ec3) OC          |
| DNBZ                          |                          | - R-C (=0) clcc (cc (c1) [N+] (=0) [O-]) [N+] (=0) [O-]     |
| DNP                           |                          | - R-clccc (ccl [N+] (=0) [O-]) [N+] (=0) [O-]               |
| DOC.                          |                          | $-$ R-C (=0) OC (C (C) C) C (C) C                           |
| DPIPS                         |                          | $-$ R-[Si] (clcccccl) (c2ccccc2) OC(C)C                     |
| Dpp                           | $\overline{\phantom{m}}$ | $R-P (=0)$ (cleccccl) c2ccccc2                              |
| DTBMS                         |                          | $-$ R-[Si](C)(C(C)(C)C)C(C)(C)C                             |
| ЕE                            |                          | $-$ R-C (C) OCC                                             |
| ESC                           |                          | $-$ R-C (=0) OCCS (=0) (=0) CC                              |
| Fmoc                          |                          | $-$ R-C (=0) OCC3c1ccccc1c2ccccc23                          |
| FourOMeBz                     |                          | $-$ R-C (=0) clccc (cc1) OC                                 |
| FPMP                          | $ \,$                    | R-C1 (CCN (CC1) c2ccccc2F) OC                               |
| Im                            |                          | $-$ R-n1ccnc1                                               |
| Lev                           |                          | $-$ R-C (=0) CCC (=0) C                                     |
| MDIPS                         |                          | $R-[Si](C)(C(C)C)(C(C)C)$                                   |
| MDPS                          |                          | $R-[Si](C)$ (cleccocl) c2ccccc2                             |
| MEM                           |                          | R-COCCOC                                                    |
| Mes                           | $\overline{\phantom{0}}$ | $R-\text{clc}(\text{cc}(\text{cclC})\text{C})\text{C}$      |
| MMTR                          | $\overline{\phantom{0}}$ | R-C (cleececl) (c2ecece2) c3ecc (ec3) OC                    |
| MOM                           | $\overline{\phantom{m}}$ | $R-COC$                                                     |
| Moz                           |                          | $R-C (=0)$ OCclccc (ccl) OC                                 |
| MPC                           |                          | $R-C (=0)$ OC(C)(C)clccc(cc1)C                              |
| MPM                           | $\overline{\phantom{m}}$ | R-clccccclOC                                                |
| МS                            |                          | $R-S (=0) (=0) C$                                           |
| MTHP                          | $\overline{\phantom{a}}$ | R-C1 (CCOCC1) OC                                            |
| MTM                           |                          | $R-CSC$                                                     |
| MTr                           |                          | $R-S (=0) (=0)$ clc (cc (c (c1C) C) OC) C                   |
| NPE                           | $\overline{\phantom{m}}$ | $R-CCc1ccc(cc1) [N+] (=0) [0-]$                             |
| NPEOC                         | $\overline{\phantom{0}}$ | $R-C (=0)$ OCCclccc (ccl) $[N+]$ (=0) $[0-]$                |
| NPES                          |                          | $R-S (=0) (=0) CCc1ccc (cc1) [N+] (=0) [0-]$                |
|                               |                          |                                                             |
| Np                            | -                        | R-c1ccc(cc1)[N+](=O)[O-]                                    |
| NPS                           | -                        | R-Sc1ccccc1[N+](=O)[O-]                                     |
| NVOC                          | -                        | R-C(=O)OOCc1cc(c(cc1[N+](=O)[O-])OC)OC                      |
| OBzl                          | -                        | R-OCc1ccccc1                                                |
| ONOS                          | -                        | R-S(=O)(=O)c1ccccc1[N+](=O)[O-]                             |
| OtBu                          | -                        | R-OC(C)(C)C                                                 |
| OTf                           | -                        | R-S(=O)(=O)C(F)(F)F                                         |
| PAC                           | -                        | R-CC(=O)c1ccccc1                                            |
| PBF                           | -                        | R-S(=O)(=O)c1c(c(c2c(c1C)CC(O2)(C)C)C)C                     |
| PCB                           | -                        | R-c1ccc(cc1)Cl                                              |
| PHF                           | -                        | R-C1(c2cccc2-c3c1cccc3)c4ccccc4                             |
| Pht                           | -                        | R-C(=O)c1cccc1C=O                                           |
| Piv                           | -                        | R-C(=O)C(C)(C)C                                             |
| PMB                           | -                        | R-Cc1ccc(cc1)OC                                             |
| PMBM                          | -                        | R-COCc1ccc(cc1)OC                                           |
| Poc                           | -                        | R-C(=O)OC1CCCC1                                             |
| PPi                           | -                        | R-P(=O)([O-])OP(=O)([O-])[O-]                               |
| SEM                           | -                        | R-COOCH2[Si](C)(C)C                                         |
| SES                           | -                        | R-S(=O)(=O)CC[Si](C)(C)C                                    |
| StBu                          | -                        | R-SC(C)(C)C                                                 |
| TBDPS                         | -                        | R-[Si](C(C)(C)C)(c1ccccc1)(c1ccccc1)                        |
| TBMPS                         | -                        | R-[Si](c1ccccc1)(C(C)(C)C)C(C)(C)C                          |
| TBS, TBDMS                    | -                        | R-[Si](C)(C)C(C)(C)C                                        |
| TCP                           | -                        | R-c1cc(c(c1Cl)Cl)Cl                                         |
| Teoc                          | -                        | R-C(=O)OCC[Si](C)(C)C                                       |
| TES                           | -                        | R-[Si](CC)(CC)CC                                            |
| TFA                           | -                        | R-C(=O)C(F)(F)F                                             |
| Thexyl                        | -                        | R-C(C)(C)C(C)C                                              |
| THF                           | -                        | R-C1CCCO1                                                   |
| THP                           | -                        | R-C1CCCCO1                                                  |
| TIPS                          | -                        | R-[Si](C(C)C)(C(C)C)C(C)C                                   |
| TMOB                          | -                        | R-Cc1c(cc(cc1OC)OC)OC                                       |
| TMS                           | -                        | R-[Si](C)(C)C                                               |
| transCinnamyl                 | -                        | R-C/C=C/c1ccccc1                                            |
| Trisyl                        | -                        | R-S(=O)(=O)c1c(c(cc(c1C(C)C)C(C)C)C(C)C)C(C)C               |
| Troc                          | -                        | R-C(=O)OCC(Cl)(Cl)Cl                                        |
| TRT                           | -                        | R-C(c1ccccc1)(c2ccccc2)c3ccccc3                             |
| TS, Tos                       | -                        | R-S(=O)(=O)c1ccc(cc1)C                                      |
| Xyl                           | -                        | R-c1c(cccc1C)C                                              |
| Z, Cbz                        | -                        | R-C(=O)OCc1ccccc1                                           |

### **Scale**

```
Contents of parameter -scale
  Aliases : -s
  Type : float
  Allow list : false
  Default : 0.0
   Simple : true
   Required : false
   Legal ranges :
      500.0 to 0.0Brief : Scaling of the depicted molecule
```

```
Detail
   API : OE2DMolDisplayOptions::SetScale method
   0.0 value means that the molecule is scaled to
   auto-fit the (width/height) dimensions of the image
```

#### See also:

- OE2DMolDisplayOptions. SetScale method
- Controlling the Size of Depicted Molecules section

#### **SuperAtomStyle**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the super atom display style.

```
Contents of parameter -superdisp
Aliases : -super
Type : string
Allow list : false
Default : Off
Simple : true
Required : false
Brief : Super atom display style
Detail
   API : OE2DMolDisplayOptions::SetSuperAtomStyle method and OESuperAtomStyle
\rightarrownamespace
   Primitive expressions :
   Off - no super atom detection
                 - R-C (=0) OH
   COOH
                 - R-C (=0) [O-]
   COO- R-C (=0) H
   CHO
                  - R-C#[NX1]
   NC- R-[N+] #[C-]
   \mathrm{CN}\label{eq:R} \begin{array}{ll} - & \mbox{R} = \left[ \mbox{ N} + \mbox{ } \right] = \left[ \mbox{ N} - \mbox{ } \right] \end{array}N2N3
                  - R-N=[N+]=[N-]
                  - R-N=C=O
   NCO
   NO2
                  - R-N(=0)(=0) or R-[N+]([O-])(=0)
   CNO
                  - R - C \# [N+]-[O-]ONO
                  - R-O-N=0
   SO3H
                 - R-S (=0) (=0) (-0H)
                 - R-S (=0) (=0) (-[0-])
   SO3- R-P (=0) (-OH) (-OH)
   PO3H2
                  - R-C (-F) (-F) (-F)
   CF3CC13- R-C (-Cl) (-Cl) (-Cl)
                  - R-CH3
   Me
   Et
                  - R-CH2-CH3
   Pr- R-CH2-CH2-CH3
                  - R-CH2-CH2-CH2-CH3
   Bu
                  - R-CH2-CH(-CH3)(-CH3)
   iBu
```

```
- R-CH(-CH2-CH3)(-CH3)
sBu
             - R-C (-CH3) (-CH3) (-CH3)
t. Bu
             - R-O-CH3OMe
             - R-O-CH2-CH3
OEt
             - R-O-CH2-CH2-CH3
OPr.
             - R-O-CH2-CH2-CH2-CH3
OBu
             - Detect all super atoms
All
Combined expressions :
Created by combining primitive tokens with |
```

#### See also:

- · OESuperAtomStyle namespace
- · OE2DMolDisplayOptions. SetSuperAtomStyle method

#### **TitleLocation**

Passing this constant to the OEConfigure2DMolDisplayOptions function result in generating the following default interface to configure the location of the molecule title.

```
Contents of parameter -titleloc
   Aliases : -tloc
   Type : string
   Allow list : false
   Default : Top
   Simple : true
   Required : false
   Legal values : Hidden Top Bottom
   Brief : Location of the molecule title
   Detail
      API : OE2DMolDisplayOptions::SetTitleLocation method and OETitleLocation
\rightarrownamespace
```

See also:

- · OETitleLocation namespace
- · OE2DMolDisplayOptions. SetTitleLocation method

## 4.2.2 OE2DPathPointType

This namespace contains constants representing types of points added to a OE2DPath object.

- OE2DPathPoint class
- · OE2DPath. GetPoints method

## **CurveC1**

The first control point of a curve segment added to a path with the OE2DPath. AddCurveSegment method. See point marked as 'c1' in Figure: Example of the points of a curve segment.

## CurveC<sub>2</sub>

The second control point of a curve segment added to a path with the OE2DPath. AddCurveSegment method. See point marked as 'c2' in Figure: Example of the points of a curve segment.

## **CurveEnd**

The end point of a curve segment added to a path with the OE2DPath. AddCurveSegment method. See point marked as 'end' in Figure: Example of the points of a curve segment.

![](_page_387_Figure_7.jpeg)

Fig. 212: Example of the points of a curve segment

### **LineEnd**

Represents the end point of a line segment added to a path with the OE2DPath. AddLineSeqment method. See point marked as 'end' in Figure: Example of the points of a line segment.

![](_page_387_Figure_11.jpeg)

Fig. 213: Example of the point of a line segment

## **Start**

Represents the first point of a path.

## 4.2.3 OEAlignment

This namespace contains constants that control how texts are aligned.

See also:

- · OEFont.GetAlignment method
- · OEFont. SetAlignment method
- · OEImageBase. DrawText

The OEAlignment namespace contains the following constants:

## **Default**

The default text alignment style is OEAlignment\_Center.

### **Center**

The text is aligned to the center of the position passed as the first parameter of the OEImageBase. DrawText method. (This position is marked with a red dot in Figure: Example of using the 'Center' alignment)

## Hello World!

### Fig. 214: Example of using the 'Center' alignment

### Left

The text is left adjusted to the position passed as the first parameter of the OEImageBase. DrawText method. (This position is marked with a red dot in Figure: Example of using the 'Left' alignment)

Hello World!

Fig. 215: Example of using the 'Left' alignment

## **Right**

The text is right adjusted to the position passed as the first parameter of the OEImageBase. DrawText method. (This position is marked with a red dot in Figure: Example of using the 'Right' alignment)

![](_page_389_Picture_3.jpeg)

Fig. 216: Example of using the 'Right' alignment

## 4.2.4 OEAromaticStyle

This namespace contains constants representing various styles of aromatic ring depictions.

|           | <i>OEAromaticStyle_Kekule</i><br>(default) | <i>OEAromaticStyle_Circle</i>            | <i>OEAromaticStyle_Dash</i>            |
|-----------|--------------------------------------------|------------------------------------------|----------------------------------------|
| example A | Image: Example A molecule — Kekule style   | Image: Example A molecule — Circle style | Image: Example A molecule — Dash style |
| example B | Image: Example B molecule — Kekule style   | Image: Example B molecule — Circle style | Image: Example B molecule — Dash style |
| example C | Image: Example C molecule — Kekule style   | Image: Example C molecule — Circle style | Image: Example C molecule — Dash style |
| example D | Image: Example D molecule — Kekule style   | Image: Example D molecule — Circle style | Image: Example D molecule — Dash style |

#### Table 38: Examples of aromatic display styles

#### See also:

- Aromaticity Perception chapter in OEChem TK manual
- · OE2DMolDisplayOptions.GetAromaticStyle
- · OE2DMolDisplayOptions. SetAromaticStyle

The OEAromaticStyle namespace contains the following constants:

## **Default**

The default aromatic style is OEAromaticStyle\_Kekule.

## **Circle**

Aromatic rings up to 6-membered are depicted by drawing a circle inside. See example in Figure: Example of using the 'Circle' aromaticity style.

![](_page_390_Figure_5.jpeg)

Fig. 217: Examples of using the 'Circle' aromaticity style

Note: OEDepict TK applies the "circle" style only for rings up to 6-membered. The remaining aromatic bonds are depicted using the "dash" style. See example B and C in Table Examples of aromatic display styles. OEDepict TK does not apply the "circle" style either if not all bonds of the rings are perceived as aromatic. See example A and D in Table Examples of aromatic display styles

## **Dash**

See example in Figure: Example of using the 'Dash' aromaticity style.

![](_page_390_Figure_10.jpeg)

Fig. 218: Example of using the 'Dash' aromaticity style

### Kekule

See example in Figure: Example of using the 'Kekule' aromaticity style.

![](_page_391_Figure_3.jpeg)

Fig. 219: Example of using the 'Kekule' aromaticity style

## 4.2.5 OEAtomColorStyle

This namespace contains constants representing various atom coloring styles of molecule depiction.

See also:

- · OE2DMolDisplayOptions. GetAtomColorStyle method
- · OE2DMolDisplayOptions. SetAtomColorStyle method
- OEGetDefaultAtomColor function

After setting the atom color style of an OE2DMolDisplayOptions object:

- The color of the background can be changed by using the OE2DMolDisplayOptions. SetBackgroundColor method.
- The color that is associated with a specific atomic number can be changed by using the OE2DMolDisplayOptions. SetAtomColor method.

The OEAtomColorStyle namespace contains the following constants:

### **Default**

The default atom color style is OEAtomColorStyle\_WhiteCPK.

### **BlackCPK**

The color of the background is OEDarkBackgroundColor. The atoms are colored using the CPK color convention. See example in Figure: Example of using the 'BlackCPK' atom color style.

#### See also:

• Appendix: Element coloring (CPK) chapter

![](_page_392_Figure_1.jpeg)

Fig. 220: Example of using the 'BlackCPK' atom color style

## **BlackMonochrome**

The color of the background is OEDarkBackgroundColor. Atoms and bonds are depicted using the OEWhite color. See example in Figure: Example of using the 'BlackMonochrome' atom color style.

![](_page_392_Figure_5.jpeg)

Fig. 221: Example of using the 'BlackMonochrome' atom color style

### **WhiteCPK**

The color of the background is OELightBackgroundColor. The atoms are colored using the CPK color convention. See example in Figure: Example of using the 'WhiteCPK' atom color style.

![](_page_392_Figure_9.jpeg)

Fig. 222: Example of using the 'WhiteCPK' atom color style

## See also:

• Appendix: Element coloring (CPK) chapter

## **WhiteMonochrome**

The color of the background is OELightBackgroundColor. Atoms and bonds are depicted using the OEBlack color. See example in Figure: Example of using the WhiteMonochrome' atom color style.

![](_page_393_Picture_3.jpeg)

Fig. 223: Example of using the 'WhiteMonochrome' atom color style

## 4.2.6 OEAtomStereoStyle

This namespace encodes symbolic constants used as bit-masks to indicate what and how atom stereo information is displayed.

#### See also:

- · OE2DMolDisplayOptions.GetAtomStereoStyle
- · OE2DMolDisplayOptions.SetAtomStereoStyle

The OEAtomStereoStyle namespace contains the following constants and nested namespaces:

## **Default**

The combination of the following flags:

- · OEAtomStereoStyle\_Display\_Default
- · OEAtomStereoStyle\_HashWedgeStyle\_Default

See example in Figure: Example of using the 'Default' atom stereo style.

![](_page_393_Figure_16.jpeg)

Fig. 224: Example of using the 'Default' atom stereo style

## **Hidden**

Displays no atom stereo information. See example in Figure: Example of using the 'Hidden' atom stereo style.

![](_page_394_Figure_3.jpeg)

Fig. 225: Example of using the 'Hidden' atom stereo style

## **OEAtomStereoStyle::Display**

This nested namespace encodes symbolic constants used as bit-masks to indicate what atom stereo information is displayed.

## **Default**

The combination of the following flags:

- · OEAtomStereoStyle\_Display\_AtomStereo
- · OEAtomStereoStyle\_Display\_MDLStereoCenter

## **AtomStereo**

Displays atom stereo information in the form of hash/wedge bonds. See example in Table: Example of using the 'AtomStereo' display style.

![](_page_394_Figure_13.jpeg)

## Table 39: Example of using the 'AtomStereo' display style

If the molecule is imported from an MOL or SDF file with an "either" stereo than it is depicted as a wavy bond. See example in Figure: Example of depiction of up, down and either (wavy) bonds.

![](_page_395_Figure_2.jpeg)

Fig. 226: Example of depiction of up, down and either (wavy) bonds

## **CIPAtomStereo**

Displays the CIP atom stereo information next to the corresponding atom. See example in Table: Example of using the 'CIPAtomStereo' display style.

![](_page_395_Figure_6.jpeg)

Table 40: Example of using the 'CIPAtomStereo' display style

## **MDLStereoCenter**

| Table 41: Example of using the 'MDLStereoCenter' display style |                                                   |                                                           |                                                             |
|----------------------------------------------------------------|---------------------------------------------------|-----------------------------------------------------------|-------------------------------------------------------------|
| MDL stereo group type                                          | Absolute                                          | AND                                                       | OR                                                          |
| Label in molfile                                               | STEABS                                            | STERACn                                                   | STERELn                                                     |
| Display label                                                  | 'abs'                                             | '&n'                                                      | 'orn'                                                       |
| Example                                                        | Image: Molecule with Cl, OH, NH2 and 'abs' labels | Image: Molecule with Cl, OH, NH2 and '&1' and '&2' labels | Image: Molecule with Cl, OH, NH2 and 'or1' and 'or2' labels |

Displays the MDL enhanced stereochemical atom labels.

## All

The combination of the following flags:

- · OEAtomStereoStyle\_Display\_AtomStereo
- · OEAtomStereoStyle\_Display\_CIPAtomStereo
- · OEAtomStereoStyle\_Display\_MDLStereoCenter

## OEAtomStereoStyle::HashWedgeStyle

This nested namespace encodes symbolic constants used to indicate the style of the hash/wedge bonds that depict atom stereo information.

### **Default**

The default hash/wedge display style is OEAtomStereoStyle\_HashWedgeStyle\_Fancy

### **Fancy**

See example in Figure: Example of using the 'Fancy' hash/wedge style.

![](_page_397_Figure_1.jpeg)

Fig. 227: Example of using the 'Fancy' hash/wedge style

## **Standard**

See example in Figure: Example of using the 'Standard' hash/wedge style.

![](_page_397_Figure_5.jpeg)

Fig. 228: Example of using the 'Standard' hash/wedge style

## 4.2.7 OEBondColorStyle

This namespace contains constants representing various bond coloring styles of molecule depiction.

### See also:

- · OE2DMolDisplayOptions.GetBondColorStyle
- · OE2DMolDisplayOptions. SetBondColorStyle

The OEBondColorStyle namespace contains the following constants:

## **Default**

The default bond color style is OEBondColorStyle\_ByElement

## **ByElement**

See example in Figure: Example of using the 'ByElement' bond color style.

![](_page_398_Figure_5.jpeg)

Fig. 229: Example of using the 'ByElement' bond color style

#### **Monochrome**

See example in Figure: Example of using the 'Monochrome' bond color style.

![](_page_398_Figure_9.jpeg)

Fig. 230: Example of using the 'Monochrome' bond color style

## **4.2.8 OEBondDisplayPosition**

This namespace controls how multi-line bonds are rendered. The OEBondDisplayPosition only affects bonds of the following types (as returned by OE2DBondDisplay.GetDisplayType):

- · OEBondDisplayType\_Double
- · OEBondDisplayType\_AromaticDash
- · OEBondDisplayType\_SingleDouble
- · OEBondDisplayType\_SingleArom
- · OEBondDisplayType\_DoubleArom
- · OEBondDisplayType\_Aromatic

The concept of Left and Right are relative to the "begin" and "end" atoms of the associated OEBondBase. The side of  $Left$  and  $Right$  is defined by standing on the "begin" atom and looking towards the "end" atom.

The following figure shows how both  $Left$  and  $Right$  double bonds can appear in a benzene ring.

![](_page_399_Figure_3.jpeg)

Fig. 231: Example of various multi-line bond positions

Note: The OE2DBondDisplay does not store pointers to the "begin" and "end" atoms. The "begin" and "end" atoms can be retrieved by accessing the associated OEBondBase through the OEBondDisplayBase. GetBond method and then calling the OEBondBase. GetBgn and OEBondBase. GetEnd methods respectively.

### See also:

- · OE2DBondDisplay.GetDisplayPos method
- · OE2DBondDisplay. SetDisplayPos method

The OEBondDisplayPosition namespace contains the following constants:

### **Center**

Renders a double bond so that the "begin" and "end" atom coordinates end up between each line of the double bond. See example in Figure: Example of a double bond rendered in the center.

![](_page_399_Figure_12.jpeg)

Fig. 232: Example of a double bond rendered in the center

### Left

Renders a double bond by drawing a line between the "begin" and "end" atom coordinates, and then drawing a parallel line to the left of that line. See example in Figure: Example of a double bond rendered with its parallel line to the left.

![](_page_400_Figure_3.jpeg)

Fig. 233: Example of a double bond rendered with its parallel line to the left

## **Right**

Renders a double bond by drawing a line between the "begin" and "end" atom coordinates, and then drawing a parallel line to the right of that line. See example in Figure: Example of a double bond rendered with its parallel line to the right.

![](_page_400_Figure_7.jpeg)

Fig. 234: Example of a double bond rendered with its parallel line to the right

## 4.2.9 OEBondDisplayType

This namespace contains constants representing various styles of bond representations.

### See also:

- · OE2DBondDisplay.GetDisplayType method
- · OE2DBondDisplay. SetDisplayType method

The OEBondDisplayType namespace contains the following constants:

### **Single**

The OEBondDisplayType\_Single type is used to represent single bonds. See example in Figure: Example of depicting a 'Single' bond type.

## - 0

## Fig. 235: Example of depicting a 'Single' bond type

## **Double**

The OEBondDisplayType\_Double type is used to represent double bonds. See example in Figure: Example of depicting a 'Double' bond type.

![](_page_401_Figure_5.jpeg)

Fig. 236: Example of depicting a 'Double' bond type

## **Triple**

The OEBondDisplayType\_Triple type is used to represent triple bonds. See example in Figure: Example of depicting a 'Triple' bond type.

![](_page_401_Picture_9.jpeg)

Fig. 237: Example of depicting a 'Triple' bond type

### Quadruple

The OEBondDisplayType\_Quadruple type is used to represent quadruple bonds. See example in Figure: Example of depicting a 'Quadruple' bond type.

![](_page_401_Picture_13.jpeg)

Fig. 238: Example of depicting a 'Quadruple' bond type

## Wedge

See example in Figure: Example of depicting a 'Wedge' bond type.

![](_page_402_Figure_3.jpeg)

Fig. 239: Example of depicting a 'Wedge' bond type

## **Hash**

See example in Figure: Example of depicting a 'Hash' bond type.

## **HIIIO**

Fig. 240: Example of depicting a 'Hash' bond type

## **Wavy**

See example in Figure: Example of depicting a 'Wavy' bond type.

## ∽∧∧M ∩

## Fig. 241: Example of depicting a 'Wavy' bond type

## **AromaticDash**

The OEBondDisplayType\_AromaticDash type is used to represent aromatic rings when the OEAromaticStyle\_Dash style is turned on. See example in Figure: Example of depicting an 'Aromatic-Dash' bond type.

![](_page_402_Figure_15.jpeg)

Fig. 242: Example of depicting an 'AromaticDash' bond type

## **DoubleBowTie**

See example in Figure: Example of depicting an 'DoubleBowTie' bond type.

$$
\boldsymbol{>=}\mathbf{0}
$$

## Fig. 243: Example of depicting a 'DoubleBowTie' bond type

## **SingleDouble**

The OEBondDisplayType\_SingleDouble type is used to represent MDL query bonds that can be matched to any single or double bonds in the target molecule(s) (*i.e.* bond type  $5$  in the MDL query files) See example in *Figure:* Example of depicting an 'SingleDouble' bond type.

![](_page_403_Picture_7.jpeg)

Fig. 244: Example of depicting a 'SingleDouble' bond type

## **SingleArom**

The OEBondDisplayType\_SingleArom type is used to represent MDL query bonds that can be matched to any single or aromatic bonds in the target molecule(s) (i.e. bond type  $6$  in the MDL query files) See example in *Figure*: Example of depicting an 'SingleDouble' bond type.

![](_page_403_Picture_11.jpeg)

Fig. 245: Example of depicting a 'SingleArom' bond type

## **DoubleArom**

The OEBondDisplayType\_DoubleArom type is used to represent MDL query bonds that can be matched to any double or aromatic bonds in the target molecule(s) (*i.e.* bond type  $7$  in the MDL query files) See example in *Figure*: Example of depicting an 'DoubleArom' bond type.

![](_page_404_Figure_3.jpeg)

Fig. 246: Example of depicting a 'DoubleArom' bond type

## **Aromatic**

The OEBondDisplayType\_Aromatic type is used to represent MDL query bonds that can be matched to any aromatic bonds in the target molecule(s) (i.e. bond type 4 in the MDL query files) See example in Figure: Example of depicting an 'Aromatic' bond type.

![](_page_404_Picture_7.jpeg)

Fig. 247: Example of depicting an 'Aromatic' bond type

## Any

The OEBondDisplayType\_Any type is used to represent MDL query bonds that can be matched to any bonds in the target molecule(s) (i.e. bond type 8 in the MDL query files) See example in Figure: Example of depicting an 'Any' bond type.

![](_page_404_Figure_11.jpeg)

Fig. 248: Example of depicting an 'Any' bond type

## **Hidden**

The bond is not displayed.

# 4.2.10 OEBondStereoStyle

This namespace encodes symbolic constants used as bit-masks to indicate what bond stereo information is displayed.

See also:

- · OE2DMolDisplayOptions.GetBondStereoStyle
- · OE2DMolDisplayOptions.SetBondStereoStyle

The OEBondStereoStyle namespace contains the following constants and nested namespaces:

## **Default**

The default bond stereo style is OEBondStereoStyle\_Display\_Default. See example in Figure: Example of using the 'Default' bond stereo style.

![](_page_405_Figure_11.jpeg)

Fig. 249: Example of using the 'Default' bond stereo style

### **Hidden**

Displays no bond stereo information. See example in Figure: Example of using the 'Hidden' bond stereo style.

![](_page_405_Figure_15.jpeg)

Fig. 250: Example of using the 'Hidden' bond stereo style

## OEBondStereoStyle::Display

This nested namespace encodes symbolic constants used as bit-masks to indicate what bond stereo information is displayed.

## **Default**

The default bond stereo display style is OEBondStereoStyle\_Display\_BondStereo.

## **BondStereo**

See example in Table: Example of using the 'BondStereo' display style.

![](_page_406_Figure_7.jpeg)

#### Table 42: Example of using the 'BondStereo' display style

## **CIPBondStereo**

Displays the CIP bond stereo information next to the corresponding bond. See example in Table: Example of using the 'CIPBondStereo' display style.

![](_page_406_Figure_11.jpeg)

Table 43: Example of using the 'CIPBondStereo' display style

## All

The combination of the following flags:

- · OEBondStereoStyle\_Display\_CIPBondStereo
- · OEBondStereoStyle\_Display\_BondStereo

See example in Table: Example of using the 'All' display style.

 $O$  $C=C$  $C(O)$ = $C(C)N$ 

![](_page_407_Figure_7.jpeg)

Fig. 251: Example of using the 'All' display style

## 4.2.11 OEDepict

This namespace contains constants.

#### **OEDarkBackgroundColor**

This color is used as a background color for the OEAtomColorStyle\_BlackMonochrome and the OEAtomColorStyle\_BlackCPK atom color styles.

#### **OELightBackgroundColor**

This color is used as a background color for the OEAtomColorStyle\_WhiteMonochrome and the OEAtomColorStyle\_WhiteCPK atom color styles.

#### **OEBlackBoxPen**

See example in Figure: Example of using the 'OEBlackBoxPen' pen to draw a rectangle.

![](_page_407_Picture_17.jpeg)

Fig. 252: Example of using the 'OEBlackBoxPen' pen to draw a rectangle

## **OEBlackPen**

See example in Figure: Example of using the 'OEBlackPen' pen to draw a rectangle.

![](_page_408_Figure_3.jpeg)

Fig. 253: Example of using the 'OEBlackPen' pen to draw a rectangle

## **OEBlueBoxPen**

See example in Figure: Example of using the 'OEBlueBoxPen' pen to draw a rectangle.

![](_page_408_Picture_7.jpeg)

Fig. 254: Example of using the 'OEBlueBoxPen' pen to draw a rectangle

## **OEBluePen**

See example in Figure: Example of using the 'OEBluePen' pen to draw a rectangle.

![](_page_408_Picture_11.jpeg)

Fig. 255: Example of using the 'OEBluePen' pen to draw a rectangle

**OEDefaultFont** 

### **OEGreenBoxPen**

See example in Figure: Example of using the 'OEGreenBoxPen' pen to draw a rectangle.

![](_page_408_Picture_16.jpeg)

Fig. 256: Example of using the 'OEGreenBoxPen' pen to draw a rectangle

## **OEGreenPen**

See example in Figure: Example of using the 'OEGreenPen' pen to draw a rectangle.

![](_page_409_Figure_3.jpeg)

Fig. 257: Example of using the 'OEGreenPen' pen to draw a rectangle

## **OELightGreyBoxPen**

See example in Figure: Example of using the 'OELightGreyBoxPen' pen to draw a rectangle.

![](_page_409_Figure_7.jpeg)

![](_page_409_Figure_8.jpeg)

## **OERedBoxPen**

See example in Figure: Example of using the 'OERedBoxPen' pen to draw a rectangle.

![](_page_409_Picture_11.jpeg)

Fig. 260: Example of using the 'OERedBoxPen' pen to draw a rectangle

## **OERedPen**

See example in Figure: Example of using the 'OERedPen' pen to draw a rectangle.

![](_page_410_Figure_3.jpeg)

Fig. 261: Example of using the 'OERedPen' pen to draw a rectangle

## **OETransparentPen**

Pen with fully transparent foreground and background colors.

## **OESVGAreaPen**

Pen with almost transparent foreground and background colors.

## **OEWhiteBoxPen**

See example in Figure: Example of using the 'OEWhiteBoxPen' pen to draw a rectangle.

![](_page_410_Figure_11.jpeg)

### Fig. 262: Example of using the 'OEWhiteBoxPen' pen to draw a rectangle

## **OEWhitePen**

See example in Figure: Example of using the 'OEWhitePen' pen to draw a rectangle.

![](_page_410_Picture_15.jpeg)

Fig. 263: Example of using the 'OEWhitePen' pen to draw a rectangle

## **4.2.12 OEDepictOrientation**

This namespace contains constants that control the preferred orientation of the 2D coordinates when calling the OEPrepareDepiction function.

### See also:

- · OEPrepareDepictionOptions.GetDepictOrientation method
- · OEPrepareDepictionOptions. SetDepictOrientation method
- · OEPrepareDepiction function

The OEDepictOrientation namespace contains the following constants:

## **Default**

The default orientation is OEDepictOrientation\_Original.

## **Horizontal**

The orientation of the 2D coordinates is changed in order to maximize the scaling of the molecule for horizontal images. See example above of depicting molecules with OEDepictOrientation\_Default and OEDepictOrientation Horizontal orientations.

![](_page_411_Figure_12.jpeg)

## Original

No-op *i.e* the orientation of the 2D coordinates are not optimized in order to maximize the molecule scaling.

## **Square**

The orientation of the 2D coordinates is changed in order to maximize the scaling of the molecule for square images. See example above of depicting molecules with OEDepictOrientation\_Default and OEDepictOrientation\_Square orientations.

![](_page_412_Figure_5.jpeg)

## **Vertical**

The orientation of the 2D coordinates is changed in order to maximize the scaling of the molecule for vertical images. See example above of depicting molecules with OEDepictOrientation\_Default and OEDepictOrientation\_Vertical orientations.

![](_page_413_Figure_3.jpeg)

## **4.2.13 OEFill**

This namespace contains constants representing whether or not background color of an OEPen object is used to fill a shape that is being drawn.

#### See also:

- · OEPen. GetFill method
- · OEPen. SetFill method

The OEFill namespace contains the following constants:

## **Default**

The default fill style is OEFill\_Off.

## Off

If the fill property of an *OEPen* object is **off** than the interior of the shape being drawn will be unfilled. See example in Figure: Example of turning the object filling off.

![](_page_414_Figure_3.jpeg)

#### Fig. 264: Example of turning the object filling off

### On

If the fill property of an OEPen object is on than its background color is used to fill the interior of the shape being drawn. See example in Figure: Example of turning the object filling off.

![](_page_414_Picture_7.jpeg)

#### Fig. 265: Example of turning the object filling on

## 4.2.14 OEFontFamily

This namespace contains constants representing various font family styles of the OEFont class.

#### See also:

- OEFont. GetFamily method
- · OEFont. SetFamily method

The OEF ontFamily namespace contains the following constants:

### **Default**

The default font family is OEFontFamily\_Arial.

#### **Arial**

Sans-serif typeface. See example in Figure: Example of drawing text with 'Arial' font family.

## Hello World!

### Fig. 266: Example of drawing text with 'Arial' font family

## **Courier**

Mono-spaced slab serif typeface See example in Figure: Example of drawing text with 'Courier' font family.

Hello World!

## Fig. 267: Example of drawing text with 'Courier' font family

### **Helvetica**

Sans-serif typeface. See example in Figure: Example of drawing text with 'Helvetica' font family.

## Hello World!

### Fig. 268: Example of drawing text with 'Helvetica' font family

## **Times**

Serif typeface. See example in Figure: Example of drawing text with 'Times' font family.

## Hello World!

### Fig. 269: Example of drawing text with 'Times' font family

## 4.2.15 OEFontStyle

This namespace encodes symbolic constants used as bit-masks to indicate the style of an OEFont object.

### See also:

- · OEFont.GetStyle method
- · OEFont. SetStyle method

The  $OEFontStyl$  e namespace contains the following constants:

## **Default**

The default font style is OEFont Style\_Normal.

## **Bold**

See example in Figure: Example of drawing text with 'Bold' font style.

## **Hello World!**

Fig. 270: Example of drawing text with 'Bold' font style

### **Italic**

See example in Figure: Example of drawing text with 'Italic' font style.

Hello World!

Fig. 271: Example of drawing text with 'Italic' font style

## **Normal**

See example in Figure: Example of drawing text with 'Normal' font style.

Hello World!

Fig. 272: Example of drawing text with 'Normal' font style

## 4.2.16 OEHighlightOverlayStyle

This namespace contains constants representing various styles of overlay highlighting.

### See also:

- · OEAddHighlightOverlay function
- OEHighlightOverlayBase class
- Highlighting Overlapped Patterns section

The OEHighlightOverlayStyle namespace contains the following constants:

## **Default**

The default highlighting style is OEHighlightOverlayStyle\_BallAndStick.

## **BallAndStick**

See example in Figure: Example of overlay highlighting using the 'BallAndStick' style.

- Atoms are highlighted by depicting spheres underneath them. If an atom is part of more than one patterns, then all the colors associated with the patterns are used by turns to color pie segments of the sphere.
- Bonds are highlighted by depicting sticks underneath them. If a bond is part of more than one patterns, then all the colors associated with the patterns are used by turns to color line segments of the stick.

![](_page_417_Picture_7.jpeg)

#### Fig. 273: Example of overlay highlighting using the 'BallAndStick' style

The radius of the spheres and the width of the sticks are automatically scaled with the molecule. See example in Figure: Example of scaling the 'BallAndStick' style highlighting along with the molecule.

![](_page_417_Picture_10.jpeg)

Fig. 274: Example of scaling the 'BallAndStick' style highlighting along with the molecule

#### See also:

· OEHighlightOverlayByBallAndStick class

It is recommended to select colors with high contrast when highlighting overlapped patterns with the Note: OEHighlightOverlayStyle\_BallAndStick style.

### See also:

· OEGetContrastColors function

Even though there is no limit on the number of overlapping patterns that can be highlighted simultaneously, attempting to highlight too many patterns will result in a complex image that will be difficult to visually interpret. See example in Figure: Example of highlighting extremely overlapping patterns In this image, all unique 'phenol' substructures of a molecule are highlighted simultaneously.

![](_page_418_Figure_2.jpeg)

## Fig. 275: Example of highlighting extremely overlapping patterns

## 4.2.17 OEHighlightParamName

This namespace contains the default parameter names used when the interface generated by invoking the OEConfigureHighlightParamsfunction.

### See also:

· OEHighlightSetup namespace.

The OEHighlightParamName namespace contains the following constants:

## **Color**

The default name of highlight color parameter is "-highlightcolor".

- · OEHighlightSetup\_Color constant
- · OEConfigureHighlightColor function
- · OEGetHighlightColor function

### **Style**

The default name of highlight stylecolor parameter is "-highlightstyle".

#### See also:

- · OEHighlightSetup\_Style constant
- OEConfigureHighlightStylefunction
- · OEGetHighlightStylefunction

## 4.2.18 OEHighlightSetup

This namespace encodes symbolic constants used as bit-masks to indicate which highlighting interface parameters are being created when invoking the OEConfigureHighlightParams function.

#### See also:

· OEHighlightParamName namespace

The OEHighlightSetup namespace contains the following constants:

### All

#### The combination of following constants:

- · OEHighlightSetup\_Color
- · OEHighlightSetup\_Style

### **Color**

Passing this constant to the OEConfigure Highlight Params function result in generating the following default interface to configure the color of the highlighting by invoking the OEConfigure HighlightColor function.

```
Contents of parameter -highlightcolor
   Aliases : - hcolor
   Type : string
   Allow list : false
   Default : red
   Simple : true
   Required : false
   Legal values : black blue bluetint brass brown copper cyan darkblue
     darkbrown darkcyan darkgreen darkgrey darkmagenta darkorange
     darkpurple darkred darkrose darksalmon darkyellow gold green
     greenblue greentint grey hotpink lightblue lightbrown lightgreen
     lightgrey lightorange lightpurple lightsalmon limegreen magenta
     mediumblue mediumbrown mediumgreen mediumorange mediumpurple
     mediumsalmon mediumyellow olivebrown olivegreen olivegrey pewter
     orange pink pinktint purple red redorange royalblue seagreen silver
      skyblue violet white yellow yellowtint
```

#### See also:

· OEHighlightParamName\_Color constant

- · OEConfigureHighlightColor function
- · OEGetHighlightColor function

## **Style**

Passing this constant to the OEConfigureHighlightParams function result in generating the following default interface to configure the style of the highlighting by invoking the OEConfigureHighlightStyle function.

```
Contents of parameter -highlightstyle
   Aliases : - hstyle
   Type : string
   Allow list : false
   Default : Color
   Simple : true
   Required : false
   Legal values : Color Stick BallAndStick Cogwheel Lasso
   Brief : Highlighting style
```

See also:

- · OEHighlightParamName\_Style constant
- · OEConfigureHighlightStyle function
- · OEGetHighlightStylefunction

## 4.2.19 OEHighlightStyle

This namespace contains constants representing various styles of highlighting.

#### See also:

- · OEAddHighlighting function
- OEHighlightBase class
- Highlighting chapter

The OEHighlight Style namespace contains the following constants:

#### **Default**

The default highlighting style is OEHighlightStyle\_Color.

## **BallAndStick**

See example in Figure: Example of highlighting using the 'ball and stick' style.

- Atoms are highlighted by depicting spheres underneath them.
- Bonds are highlighted by depicting sticks underneath them.

![](_page_421_Figure_5.jpeg)

Fig. 276: Example of highlighting using the 'ball and stick' style

The radius of the spheres and the width of the sticks are automatically scaled with the molecule. See example in Figure: Example of scaling the 'ball and stick' style highlighting along with the molecule.

![](_page_421_Picture_8.jpeg)

Fig. 277: Example of scaling the 'ball and stick' style highlighting along with the molecule

#### See also:

• OEHighlightByBallAndStick class

### **Color**

See example in Figure: Example of highlighting using the 'color' style.

- Atoms are highlighted by changing the color of their label, if present. If the atom being highlighted is an isolated carbon atom, then its atom label is explicitly displayed. See example in Figure: Example of highlighting isolated atoms using the 'color' style.
- Bonds are highlighted by changing their color.

#### See also:

• OEHighlightByColor class

![](_page_422_Figure_1.jpeg)

Fig. 278: Example of highlighting using the 'color' style

![](_page_422_Figure_3.jpeg)

![](_page_422_Figure_4.jpeg)

## **Cogwheel**

See example in Figure: Example of highlighting using the 'cogwheel' style.

![](_page_422_Figure_7.jpeg)

Fig. 280: Example of highlighting using the 'cogwheel' style

The radius of the spheres and the width of the sticks are automatically scaled with the molecule. See example in Figure: Example of scaling the 'cogwheel' style highlighting along with the molecule.

### See also:

• OEHighlightByCogwheel class

![](_page_423_Picture_1.jpeg)

Fig. 281: Example of scaling the 'cogwheel' style highlighting along with the molecule

#### **Lasso**

See example in Figure: Example of highlighting using the 'lasso' style.

Atoms and bond are highlighted by drawing a "curved" convex hull around them.

![](_page_423_Figure_6.jpeg)

Fig. 282: Example of highlighting using the 'lasso' style

The width of "lasso" line is automatically scaled with the molecule. See example in Figure: Example of scaling the 'lasso' style highlighting along with the molecule.

![](_page_423_Figure_9.jpeg)

Fig. 283: Example of scaling the 'lasso' style highlighting along with the molecule

See also:

· OEHighlightByLasso class

## **Stick**

See example in Figure: Example of highlighting using the 'stick' style.

- Atoms are highlighted by changing the color of their label to be monochrome, if present. Isolated atoms are highlighted by depicting spheres underneath them. See example in Figure: Example of highlighting isolated atoms using the 'stick' style.
- Bonds are highlighted by depicting sticks underneath them.

![](_page_424_Picture_5.jpeg)

Fig. 284: Example of highlighting using the 'stick' style

![](_page_424_Figure_7.jpeg)

Fig. 285: Example of highlighting isolated atoms using the 'stick' style

The width of the sticks is automatically scaled with the molecule. See example in Figure: Example of scaling the 'stick' style highlighting along with the molecule.

![](_page_424_Picture_10.jpeg)

Fig. 286: Example of scaling the 'stick' style highlighting along with the molecule

See also:

• OEHighlightByStick class

## 4.2.20 OEHydrogenPos

This namespace contains constants representing the position of hydrogen relative to the atomic label.

### See also:

- · OE2DAtomDisplay.GetHPosition method
- · OE2DAtomDisplay. SetHPosition method

![](_page_425_Figure_6.jpeg)

![](_page_425_Figure_7.jpeg)

The OEHydrogenPos namespace contains the following constants:

## **Undefined**

The position of the hydrogen is not calculated yet.

#### **East**

See atom with index 4 in Figure: Example of various hydrogen positions

## **North**

See atom with index 14 in Figure: Example of various hydrogen positions

## **South**

See atom with index 2 in Figure: Example of various hydrogen positions

### **West**

See atom with index 6 in Figure: Example of various hydrogen positions

## 4.2.21 OEHydrogenStyle

This namespace contains constants that control how explicit and implicit hydrogen information is depicted.

#### See also:

- · OE2DMolDisplayOptions.GetHydrogenStyle method
- · OE2DMolDisplayOptions. SetHydrogenStyle method

The OEHydrogenStyle namespace contains the following constants:

#### **Default**

The default hydrogen display style is the combination of OEHydrogenStyle\_ImplicitHetero and OEHydrogenStyle\_ExplicitAll. See example in Figure: Example of the default hydrogens depiction.

![](_page_426_Figure_13.jpeg)

Fig. 288: Example of the default hydrogens depiction

#### **ExplicitAll**

Depicts all explicit hydrogens. See example in Figure: Example of depicting all explicit hydrogens.

![](_page_427_Figure_1.jpeg)

## Fig. 289: Example of depicting all explicit hydrogens

## **ExplicitHetero**

Depicts explicit hydrogens attached to hetero atoms. See example in Figure: Example of depicting explicit hydrogens attached to hetero atoms.

![](_page_427_Figure_5.jpeg)

Fig. 290: Example of depicting explicit hydrogens attached to hetero atoms

## **ExplicitTerminal**

Depicts explicit hydrogens attached to terminal atoms. See example in Figure: Example of depicting explicit hydrogens attached to terminal atoms.

![](_page_428_Figure_1.jpeg)

Fig. 291: Example of depicting explicit hydrogens attached to terminal atoms

### **Hidden**

No hydrogen information is displayed. See example in Figure: Example of hiding all hydrogens.

![](_page_428_Picture_5.jpeg)

Fig. 292: Example of hiding all hydrogens

## **ImplicitAll**

Depicts all implicit hydrogens. See example in Figure: Example of depicting all implicit hydrogens.

#### **ImplicitHetero**

Depicts implicit hydrogens attached to hetero atoms. See example in Figure: Example of depicting implicit hydrogens attached to hetero atoms.

![](_page_429_Figure_1.jpeg)

Fig. 293: Example of depicting all implicit hydrogens

![](_page_429_Figure_3.jpeg)

Fig. 294: Example of depicting implicit hydrogens attached to hetero atoms

## **ImplicitTerminal**

Depicts implicit hydrogens attached to terminal atoms. See example in Figure: Example of depicting implicit hydrogens attached to terminal atoms.

![](_page_429_Figure_7.jpeg)

Fig. 295: Example of depicting implicit hydrogens attached to terminal atoms

## 4.2.22 OElconLocation

This namespace contains constants representing the position of the logo when using the OEAddOpenEyeIcon and OEAddInteractiveIconfunctions. The OEIconLocation namespace contains the following constants:

## **Default**

The default title location is OEIconLocation\_BottomRight.

## **BottomLeft**

![](_page_430_Picture_6.jpeg)

**BottomRight** 

![](_page_430_Picture_8.jpeg)

**TopLeft** 

![](_page_430_Picture_10.jpeg)

## **TopRight**

![](_page_431_Figure_2.jpeg)

## 4.2.23 OEImageGridParamName

This namespace contains the default parameter names used when the interface generated by invoking the OEConfigureImageGridParamsfunction.

#### See also:

· OEImageGridSetup namespace.

The OEImageGridParamName namespace contains the following constants:

#### **NumColumns**

The default name of number of grid columns parameter is "-cols".

#### See also:

- · OEImageGridSetup\_NumColumns constant
- · OEConfigureImageGridNumColumnsfunction
- · OEGet ImageGridNumColumns function

### **NumRows**

The default name of number of grid rows parameter is "-rows".

#### See also:

- · OEImageGridSetup\_NumRows constant
- · OEConfigureImageGridNumRowsfunction
- · OEGet ImageGridNumRows function

## 4.2.24 OEImageGridSetup

This namespace encodes symbolic constants used as bit-masks to indicate which image grid interface parameters are being created when invoking the OEConfigureImageGridParams function.

#### See also:

· OEImageGridParamName namespace.

The OEImageGridSetup namespace contains the following constants:

## All

The combination of following constants:

- · OEImageGridSetup\_NumColumns
- OEImageGridSetup\_NumRows

### **NumColumns**

Passing this constant to the OEConfigureImageGridParams function result in generating the following default interface to configure the number of columns of image grid by invoking the OEConfigureImageGridNumColumnsfunction.

```
Contents of parameter -cols
   Aliases : -cols
   Type : int
   Allow list : false
   Default : 2
   Simple : true
   Required : false
   Legal ranges :
       10 to 1Brief : Number of columns
```

See also:

- OEImageGridParamName NumColumns constant
- · OEConfigureImageGridNumColumnsfunction
- · OEGet ImageGridNumColumns function

## **NumRows**

Passing this constant to the OEConfigure ImageGridParams function result in generating the following default interface to configure the number of row of image grid by invoking the OEConfigureImageGridNumRows function.

```
Contents of parameter -rows
   Aliases : -rows
   Type : int
   Allow list : false
   Default : 3
   Simple : true
   Required : false
   Legal ranges :
       10 to 1Brief : Number of rows
```

- · OEImageGridParamName\_NumRows constant
- OEConfigureImageGridNumRowsfunction

· OEGet ImageGridNumRows function

## 4.2.25 OEImageParamName

This namespace contains the default parameter names used when the interface generated by invoking the OEConfigureImageOptionsfunction.

#### See also:

· OEImageSetup namespace.

The OEMultiPageParamName namespace contains the following constants:

## **Height**

The default name of the image height parameter is "-height".

#### See also:

- · OEImageSetup\_Height constant
- · OEConfigureImageOptionsfunction
- · OEGet ImageHeight function

### **Width**

The default name of the image width parameter is "-width".

#### See also:

- · OEImageSetup\_Width constant
- · OEConfigureImageOptionsfunction
- · OEGet ImageWidth function

## 4.2.26 OEImageSetup

This namespace encodes symbolic constants used as bit-masks to indicate which image interface parameters are being created when invoking the OEConfigure ImageOptions function.

#### See also:

· OEImageParamName namespace.

The OEImageSetup namespace contains the following constants:

## All

The combination of following constants:

- · OEImageSetup\_Width
- · OEImageSetup\_Height

#### **Height**

Passing this constant to the OEConfigure ImageOptions function result in generating the following default interface to configure image width.

```
Contents of parameter -width
   Aliases : -w
   Type : int
   Allow list : false
   Default : 0
   Simple : true
   Required : false
   Legal ranges :
       5000 to 0Brief : Width of output image
```

See also:

- · OEImageParamName\_Height function
- · OEConfigureImageOptionsfunction
- · OEGet ImageHeight function

#### **Width**

Passing this constant to the OEConfigureImageOptions function result in generating the following default interface to configure image width.

```
Contents of parameter -height
   Aliases : - h
   Type : int
   Allow list : false
   Default : 0
   Simple : true
   Required : false
   Legal ranges :
       5000 to 0
   Brief : Height of output image
```

- · OEImageParamName\_Width function
- · OEConfigureImageOptionsfunction
- · OEGet ImageWidth function

## 4.2.27 OEImageTableStyle

This namespace contains constants that define built-in image table styles.

## See also:

- OEImageTable class
- OEImageTableOptions class

## **Default**

The default image table style is OEImageTableStyle\_NoStyle.

## **LightBlue**

| (1, 1) | (1, 2) | (1, 3) | row 1 | (1, 1) | (1, 2) | column 1 | column 2 | column 3 |       | column 1 | column 2 |
|--------|--------|--------|-------|--------|--------|----------|----------|----------|-------|----------|----------|
| (2, 1) | (2, 2) | (2, 3) | row 2 | (2, 1) | (2, 2) | (1, 1)   | (1, 2)   | (1, 3)   | row 1 | (1, 1)   | (1, 2)   |
| (3, 1) | (3, 2) | (3, 3) | row 3 | (3, 1) | (3, 2) | (2, 1)   | (2, 2)   | (2, 3)   | row 2 | (2, 1)   | (2, 2)   |
| (4, 1) | (4, 2) | (4, 3) | row 4 | (4, 1) | (4, 2) | (3, 1)   | (3, 2)   | (3, 3)   | row 3 | (3, 1)   | (3, 2)   |
| (5, 1) | (5, 2) | (5, 3) | row 5 | (5, 1) | (5, 2) | (4, 1)   | (4, 2)   | (4, 3)   | row 4 | (4, 1)   | (4, 2)   |

Fig. 296: Examples of using the 'LightBlue' image table style

## **LightGreen**

| (1, 1) | (1, 2) | (1, 3) | row 1 | (1, 1) | (1, 2) | column 1 | column 2 | column 3 |       | column 1 | column 2 |
|--------|--------|--------|-------|--------|--------|----------|----------|----------|-------|----------|----------|
| (2, 1) | (2, 2) | (2, 3) | row 2 | (2, 1) | (2, 2) | (1, 1)   | (1, 2)   | (1, 3)   | row 1 | (1, 1)   | (1, 2)   |
| (3, 1) | (3, 2) | (3, 3) | row 3 | (3, 1) | (3, 2) | (2, 1)   | (2, 2)   | (2, 3)   | row 2 | (2, 1)   | (2, 2)   |
| (4, 1) | (4, 2) | (4, 3) | row 4 | (4, 1) | (4, 2) | (3, 1)   | (3, 2)   | (3, 3)   | row 3 | (3, 1)   | (3, 2)   |
| (5, 1) | (5, 2) | (5, 3) | row 5 | (5, 1) | (5, 2) | (4, 1)   | (4, 2)   | (4, 3)   | row 4 | (4, 1)   | (4, 2)   |

Fig. 297: Examples of using the 'LightGreen' image table style

## **LightGrey**

| (1, 1) | (1, 2) | (1, 3) | row 1 | (1, 1) | (1, 2) | column 1 | column 2 | column 3 |       | column 1 | column 2 |
|--------|--------|--------|-------|--------|--------|----------|----------|----------|-------|----------|----------|
| (2, 1) | (2, 2) | (2, 3) | row 2 | (2, 1) | (2, 2) | (1, 1)   | (1, 2)   | (1, 3)   | row 1 | (1, 1)   | (1, 2)   |
| (3, 1) | (3, 2) | (3, 3) | row 3 | (3, 1) | (3, 2) | (2, 1)   | (2, 2)   | (2, 3)   | row 2 | (2, 1)   | (2, 2)   |
| (4, 1) | (4, 2) | (4, 3) | row 4 | (4, 1) | (4, 2) | (3, 1)   | (3, 2)   | (3, 3)   | row 3 | (3, 1)   | (3, 2)   |
| (5, 1) | (5, 2) | (5, 3) | row 5 | (5, 1) | (5, 2) | (4, 1)   | (4, 2)   | (4, 3)   | row 4 | (4, 1)   | (4, 2)   |

## Fig. 298: Examples of using the 'LightGrey' image table style

## **MediumBlue**

| Table 1: 5 rows, 3 columns, no headers (1, 1)(1, 2)(1, 3) (2, 1)(2, 2)(2, 3) (3, 1)(3, 2)(3, 3) (4, 1)(4, 2)(4, 3) (5, 1)(5, 2)(5, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Table 2: Row headers, two data columns row 1(1, 1)(1, 2) row 2(2, 1)(2, 2) row 3(3, 1)(3, 2) row 4(4, 1)(4, 2) row 5(5, 1)(5, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Table 3: Column headers, 4 data rows column 1column 2column 3 (1, 1)(1, 2)(1, 3) (2, 1)(2, 2)(2, 3) (3, 1)(3, 2)(3, 3) (4, 1)(4, 2)(4, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Table 4: Both row and column headers column 1column 2 row 1(1, 1)(1, 2) row 2(2, 1)(2, 2) row 3(3, 1)(3, 2) row 4(4, 1)(4, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|---------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|----------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|-------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|-------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|---------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|----------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|-------------------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|-------------------------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

Fig. 299: Examples of using the 'MediumBlue' image table style

## **MediumGreen**

| (1, 1) | (1, 2) | (1, 3) | row 1 | (1, 1) | (1, 2) | column 1 | column 2 | column 3 |                  | column 1 | column 2 |
|--------|--------|--------|-------|--------|--------|----------|----------|----------|------------------|----------|----------|
| (2, 1) | (2, 2) | (2, 3) | row 2 | (2, 1) | (2, 2) | (1, 1)   | (1, 2)   | (1, 3)   | row 1            | (1, 1)   | (1, 2)   |
| (3, 1) | (3, 2) | (3, 3) | row 3 | (3, 1) | (3, 2) | (2, 1)   | (2, 2)   | (2, 3)   | row <sub>2</sub> | (2, 1)   | (2, 2)   |
| (4, 1) | (4, 2) | (4, 3) | row 4 | (4, 1) | (4, 2) | (3, 1)   | (3, 2)   | (3, 3)   | row 3            | (3, 1)   | (3, 2)   |
| (5, 1) | (5, 2) | (5, 3) | row 5 | (5, 1) | (5, 2) | (4, 1)   | (4, 2)   | (4, 3)   | row 4            | (4, 1)   | (4, 2)   |

Fig. 300: Examples of using the 'MediumGreen' image table style

## **MediumGrey**

| Table 1 (1, 1)(1, 2)(1, 3) (2, 1)(2, 2)(2, 3) (3, 1)(3, 2)(3, 3) (4, 1)(4, 2)(4, 3) (5, 1)(5, 2)(5, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Table 2 row 1(1, 1)(1, 2) row 2(2, 1)(2, 2) row 3(3, 1)(3, 2) row 4(4, 1)(4, 2) row 5(5, 1)(5, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Table 3 column 1column 2column 3 (1, 1)(1, 2)(1, 3) (2, 1)(2, 2)(2, 3) (3, 1)(3, 2)(3, 3) (4, 1)(4, 2)(4, 3) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Table 4 column 1column 2 row 1(1, 1)(1, 2) row 2(2, 1)(2, 2) row 3(3, 1)(3, 2) row 4(4, 1)(4, 2) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
|--------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|---------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
|--------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|---------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--------------------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--------------------------------------------------------------------------------------------------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|

Fig. 301: Examples of using the 'MediumGrey' image table style

## **NoStyle**

| (1, 1) | (1, 2) | (1, 3) | row 1 | (1, 1) | (1, 2) | column 1 | column 2 | column 3 | column 1 | column 2 |        |
|--------|--------|--------|-------|--------|--------|----------|----------|----------|----------|----------|--------|
| (2, 1) | (2, 2) | (2, 3) | row 2 | (2, 1) | (2, 2) | (1, 1)   | (1, 2)   | (1, 3)   | row 1    | (1, 1)   | (1, 2) |
| (3, 1) | (3, 2) | (3, 3) | row 3 | (3, 1) | (3, 2) | (2, 1)   | (2, 2)   | (2, 3)   | row 2    | (2, 1)   | (2, 2) |
| (4, 1) | (4, 2) | (4, 3) | row 4 | (4, 1) | (4, 2) | (3, 1)   | (3, 2)   | (3, 3)   | row 3    | (3, 1)   | (3, 2) |
| (5, 1) | (5, 2) | (5, 3) | row 5 | (5, 1) | (5, 2) | (4, 1)   | (4, 2)   | (4, 3)   | row 4    | (4, 1)   | (4, 2) |

Fig. 302: Examples of using the 'NoStyle' image table style

## **SantaFe**

| (1, 1) | (1, 2) | (1, 3) | row 1 | (1, 1) | (1, 2) | column 1 | column 2 | column 3 |       | column 1 | column 2 |
|--------|--------|--------|-------|--------|--------|----------|----------|----------|-------|----------|----------|
| (2, 1) | (2, 2) | (2, 3) | row 2 | (2, 1) | (2, 2) | (1, 1)   | (1, 2)   | (1, 3)   | row 1 | (1, 1)   | (1, 2)   |
| (3, 1) | (3, 2) | (3, 3) | row 3 | (3, 1) | (3, 2) | (2, 1)   | (2, 2)   | (2, 3)   | row 2 | (2, 1)   | (2, 2)   |
| (4, 1) | (4, 2) | (4, 3) | row 4 | (4, 1) | (4, 2) | (3, 1)   | (3, 2)   | (3, 3)   | row 3 | (3, 1)   | (3, 2)   |
| (5, 1) | (5, 2) | (5, 3) | row 5 | (5, 1) | (5, 2) | (4, 1)   | (4, 2)   | (4, 3)   | row 4 | (4, 1)   | (4, 2)   |

## 4.2.28 OELayerPosition

This namespace contains constants representing the position of layers available for an OE2DMolDisplay class.

See also:

· OE2DMolDisplay.GetLayer

The OELayerPosition namespace contains the following constants:

### **Above**

Provides access to above image (OEImage) of a OE2DMolDisplay object. Everything drawn to this image will be rendered last when calling the OERenderMolecule function, as a result the image will appear above the molecule depiction. See example in Figure: Example of drawing a triangle into the above layer.

![](_page_438_Picture_8.jpeg)

Fig. 304: Example of drawing a triangle into the above layer

### **Below**

Provides access to **below** image (OEImage) of a OE2DMolDisplay object. Everything drawn to this image will be rendered first when calling the OERenderMolecule function, as a result the image will appear below the molecule depiction.

For example, the sticks drawn to highlighting bonds when using the OEHighlight Style Stick style all drawn into a below layer. See example in Figure: Example of drawing a triangle into the below layer.

![](_page_438_Picture_13.jpeg)

Fig. 305: Example of drawing a triangle into the below layer

## **SVG**

This layer is used internally when generating interactive SVG images.

# 4.2.29 OELegendColorStyle

This namespace contains constants that define built-in legend color styles.

See also:

- OELegendLayout class
- OELegendLayoutOptions class
- · OELegendLayoutStylenamespace
- · OELegendInteractiveStylenamespace

## **Default**

The default legend color style is OELegendColorStyle\_NoStyle.

## **LightBlue**

![](_page_439_Figure_13.jpeg)

Fig. 306: Example of using the 'LightBlue' color style

## **LightGreen**

![](_page_440_Figure_1.jpeg)

Fig. 307: Example of using the 'LightGreen' color style

## **LightGrey**

![](_page_440_Figure_4.jpeg)

Fig. 308: Example of using the 'LightGrey' color style

## **NoStyle**

![](_page_440_Figure_7.jpeg)

Fig. 309: Example of using the 'NoStyle' color style

## 4.2.30 OELegendInteractiveStyle

This namespace contains constants that define built-in legend interactive styles.

## See also:

- OELegendLayout class
- OELegendLayoutOptions class
- · OELegendLayoutStylenamespace
- · OELegendColorStyle namespace

## **Default**

The default legend interactive style is OELegendInteractiveStyle\_Hover.

### **Hover**

Note: This style is only available for . svg image format.

### **Permanent**

### **Toggle**

Note: This style is only available for . svg image format.

## 4.2.31 OELegendLayoutStyle

This namespace contains constants that define built-in legend layout styles.

- OELegendLayout class
- OELegendLayoutOptions class
- · OELegendColorStyle namespace
- · OELegendInteractiveStylenamespace

## **Default**

The default legend layout style is OELegendLayoutStyle\_HorizontalTopLeft.

## **HorizontalBottomLeft**

![](_page_442_Picture_4.jpeg)

![](_page_442_Figure_5.jpeg)

## **HorizontalBottomRight**

![](_page_442_Figure_7.jpeg)

Fig. 311: Example of using the 'HorizontalBottomRight' layout style

## **HorizontalTopLeft**

![](_page_443_Picture_1.jpeg)

Fig. 312: Example of using the 'HorizontalTopLeft' layout style

## **HorizontalTopRight**

*This is the legend area*

Legend

Fig. 313: Example of using the 'HorizontalTopRight' layout style

**VerticalBottomLeft** 

![](_page_443_Figure_7.jpeg)

![](_page_443_Figure_8.jpeg)

## VerticalBottomRight

![](_page_444_Figure_2.jpeg)

Fig. 315: Example of using the 'VerticalBottomRight' layout style

## **VerticalTopLeft**

![](_page_444_Picture_5.jpeg)

Fig. 316: Example of using the 'VerticalTopLeft' layout style

## **VerticalTopRight**

![](_page_444_Picture_8.jpeg)

Fig. 317: Example of using the 'VerticalTopRight' layout style

## 4.2.32 OELineCap

This namespace contains constants that control how the endpoints of lines are drawn.

## See also:

- · OEPen. GetLineCap method
- OEPen. SetLineCap method

The  $OELineCap$  namespace contains the following constants:

## **Default**

The default line cap style is OELineCap\_Round.

## **Butt**

Closes the line off with a straight edge that's normal (at 90 degrees to) the direction of the stroke and crosses its end. See example in Figure: Example of line drawing with 'Butt' line cap style.

![](_page_445_Figure_11.jpeg)

Fig. 318: Example of line drawing with 'Butt' line cap style

## **Round**

Produces a rounded effect on the end of the line. See example in Figure: Example of line drawing with 'Round' line cap style.

![](_page_445_Figure_15.jpeg)

Fig. 319: Example of line drawing with 'Round' line cap style

### **Square**

Has the same appearance as the OELineCap\_Butt style, but stretches the line slightly beyond the actual path. See example in Figure: Example of line drawing with 'Square' line cap style.

![](_page_446_Picture_3.jpeg)

Fig. 320: Example of line drawing with 'Square' line cap style

## 4.2.33 OELineJoin

The line join style controls how lines connect at corners when drawing outlines.

### See also:

- · OEPen. GetLineJoin method
- · OEPen. SetLineJoin method

The OELineJoin namespace contains the following constants:

## **Default**

The default line join style is OELineJoin\_Round.

## **Bevel**

See example in Figure: Example of line drawing with 'Bevel' line join style.

![](_page_446_Picture_15.jpeg)

Fig. 321: Example of line drawing with 'Bevel' line join style

### **Miter**

See example in Figure: Example of line drawing with 'Miter' line join style.

![](_page_447_Picture_3.jpeg)

## Fig. 322: Example of line drawing with 'Miter' line join style

## **Round**

See example in Figure: Example of line drawing with 'Round' line join style.

![](_page_447_Picture_7.jpeg)

## Fig. 323: Example of line drawing with 'Round' line join style

## 4.2.34 OEMargin

This namespace contains constants representing the position of margins for the OEImageGrid and the OE2DMolDisplayOptions classes.

#### See also:

- · OE2DMolDisplayOptions. SetMargin
- · OE2DMolDisplayOptions.GetMargin
- · OEImageGrid. SetMargin
- · OEImageGrid.GetMargin

The  $OEMargin$  namespace contains the following constants:

## **Top**

## **Bottom**

Left

### **Right**

## 4.2.35 OEMultiPageParamName

This namespace contains the default parameter names used when the interface generated by invoking the OEConfigureMultiPageParamsfunction.

#### See also:

· OEMultiPageSetup namespace.

The OEMultiPageParamName namespace contains the following constants:

### **PageOrientation**

The default name of the page orientation parameter is "-pageorientation".

#### See also:

- · OEMultiPageSetup\_PageOrientation constant
- · OEConfigureMultiPageOrientation function
- · OEGetMultiPageOrientation function

### **PageSize**

The default name of the page size parameter is "-pagesize".

- · OEMultiPageSetup\_PageSize constant
- · OEConfigureMultiPageSizefunction
- · OEGetMultiPageSizefunction

## 4.2.36 OEMultiPageSetup

This namespace encodes symbolic constants used as bit-masks to indicate which multi page interface parameters are being created when invoking the OEConfigureMultiPageParams function.

#### See also:

· OEMultiPageParamName namespace.

The OEMultiPageSetup namespace contains the following constants:

### All

The combination of following constants:

- · OEMultiPageSetup\_PageOrientation
- OEMultiPageSetup\_PageSize

### **PageOrientation**

Passing this constant to the OEConfigureMultiPageParams function result in generating the following default interface to configure the page orientation by invoking the OEConfigureMultiPageOrientation function.

```
Contents of parameter -pageorientation
   Aliases : -pori
   Type : string
   Allow list : false
   Default : Portrait
   Simple : true
   Required : false
   Legal values : Portrait Landscape
   Brief : Page orientation
```

#### See also:

- · OEMultiPageParamName\_PageOrientation constant
- OEConfigureMultiPageOrientation function
- · OEGetMultiPageOrientation function

### **PageSize**

Passing this constant to the OEConfigureMultiPageParams function result in generating the following default interface to configure the page size by invoking the  $OEConfigureMultiPageSize$  function.

```
Contents of parameter -pagesize
   Aliases : - psize
   Type : string
   Allow list : false
   Default : US_Letter
   Simple : true
   Required : false
```

```
Legal values : ISO_A4 US_Letter US_Legal Custom
Brief : Page size
```

#### See also:

- · OEMultiPageParamName PageSize constant
- · OEConfigureMultiPageSizefunction
- · OEGetMultiPageSizefunction

## 4.2.37 OEPageOrientation

This namespace contains constants representing two page orientations defined for multi-page images.

#### See also:

• OEMultiPageImageFile class

The OEP ageSize namespace contains the following constants:

## **Default**

The default page orientation is OEPageOrientation\_Portrait.

#### **Portrait**

Orientation where the height of the page is greater than its width.

#### Landscape

Orientation where the width of the page is greater than its height.

## 4.2.38 OEPageSize

This namespace contains constants representing various page sizes defined for multi-page images.

### See also:

- OEMultiPageImageFile class
- · OEGetPageWidth function
- · OEGetPageHeight function

The  $OEPageSize$  namespace contains the following constants:

## **Default**

The default page size is OEPageSize\_US\_Letter.

## ISO A4

Dimensions: 210 mm  $\times$  297 mm (8.27 in  $\times$  11.69 in)

## **US Letter**

Dimensions: 216 mm  $\times$  279 mm (8.5 in  $\times$  11.0 in)

## US\_Legal

Dimension: 216 mm  $\times$  356 mm (8.5 in  $\times$  14.0 in)

## **Custom**

Custom size

## 4.2.39 OEPrepareDepictionSetup

This namespace encodes symbolic constants used as bit-masks to indicate which parameters are being created when invoking the OEConfigurePrepareDepictionOptions function.

### See also:

- OEPrepareDepictionOptions class
- · OEPrepareDepiction function

## All

#### The combination of following constants:

- · OEPrepareDepictionSetup\_ClearCoords
- · OEPrepareDepictionSetup\_DepictOrientation
- OEPrepareDepictionSetup\_SuppressHydrogens

## **ClearCoords**

Passing this constant to the OEConfigurePrepareDepictionOptions result in generating the following default interface to configure whether the 2D coordinates of the molecule have to cleared and re-generated prior to molecule depiction.

```
Contents of parameter -clearcoords
   Aliases : -clear
   Type : bool
   Allow list : false
   Default : false
   Simple : true
   Required : false
   Brief : Clears and regenerates 2D coordinates of depicted molecule
```

### **DepictOrientation**

Passing this constant to the OEConfigurePrepareDepictionOptions result in generating the following default interface to configure the preferred orientation of the 2D coordinates of the molecules.

```
Contents of parameter -orientation
   Aliases : -orient
   Type : string
   Allow list : false
   Default : Original
   Simple : true
   Required : false
   Legal values : Original Square Vertical Horizontal
   Brief : Set the preferred orientation of 2D coordinates
   Detail
        Original
                    - no-opSquare - orient the molecule for square images<br>Vertical - orient the molecule vertically
        Horizontal - orient the molecule horizontally
```

#### **SuppressHydrogens**

Passing this constant to the OEConfigurePrepareDepictionOptions result in generating the following default interface to configure whether the hydrogens have to be suppressed prior to molecule depiction.

```
Contents of parameter -suppressH
   Aliases : -sh
   Type : bool
   Allow list : false
  Default : false
   Simple : true
   Required : false
   Brief : Suppress explicit hydrogens of depicted molecule
   Detail
       Explicit hydrogens that are necessary to represent tetrahedral.
→stereochemistry are kept
```

## 4.2.40 OEProtectiveGroupStyle

This namespace contains constants representing the various protective group styles supported by OEDepict TK.

## See also:

- · OE2DMolDisplayOptions.GetProtectiveGroupStyle method
- · OE2DMolDisplayOptions. SetProtectiveGroupStyle method
- · OESuperAtomStyle namespace

The OEP rotective Group Style namespace contains the following constants. For some protective groups, more than one abbreviation can be used. The default is listed first.

## **Default**

The default protective group style is OEProtectiveGroupStyle\_Off.

## Off

No structural abbreviation is performed.

## All

The combination of all protective group flags.

![](_page_453_Figure_14.jpeg)

| OEProtectiveGroupStyle_Off                                                                     | OEProtectiveGroupStyle_Ac                                                                |
|------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Image: Benzyl acetate structural formula showing the full acetyl group (carbonyl with methyl). | Image: Benzyl alcohol with a magenta “Ac” protective-group label attached to the oxygen. |

## Ad

![](_page_454_Figure_3.jpeg)

## **Alloc**

![](_page_454_Figure_5.jpeg)

### **Ac**

**Bn** 

## **Bzl**

## **Benzyl**

| OEProtectiveGroupStyle_Off                                                   | OEProtectiveGroupStyle_Bn                                                                           |
|------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|                                                                              | OEProtectiveGroupStyle_Bzl                                                                          |
|                                                                              | OEProtectiveGroupStyle_Benzyl                                                                       |
| Image: benzyl ether with full benzyl ring shown (protective group style off) | Image: benzyl ether with magenta "Bn" label indicating protective group (protective group style on) |

## **Boc**

![](_page_455_Figure_6.jpeg)

## **Bom**

| OEProtectiveGroupStyle_Off                                                                 | OEProtectiveGroupStyle_Bom                                                         |
|--------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Image: molecule with two phenyl rings connected by an ester linkage (protective group off) | Image: phenyl ring attached via oxygen to a protective group labelled "Bom"<br>Bom |

## **Bpoc**

![](_page_456_Picture_4.jpeg)

## **Bs**

![](_page_456_Figure_6.jpeg)

## **Bt**

| OEProtectiveGroupStyle_Off                                                                       | OEProtectiveGroupStyle_Bt                                                                   |
|--------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Image: Chemical structure showing a benzotriazole-derived carboxylic acid (protective group off) | Image: Chemical structure showing a Bt-protected carboxylic acid with “Bt” label in magenta |

## **Btm**

![](_page_457_Figure_4.jpeg)

 $Bz$ 

## **Benzoyl**

| OEProtectiveGroupStyle_Off                                              | OEProtectiveGroupStyle_Bz                                                                               |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
|                                                                         | OEProtectiveGroupStyle_Benzoyl                                                                          |
| Image: Benzoyl-protected aniline structure (protective group style off) | Image: Benzoyl-protected aniline structure (Bz style) with the label "Benzoyl" shown beneath the N atom |

## **Bzh**

![](_page_458_Picture_4.jpeg)

## **BzOM**

![](_page_458_Figure_6.jpeg)

## cHx

![](_page_459_Figure_2.jpeg)

## Dan

## **Dansyl**

| OEProtectiveGroupStyle_Off                                                   | OEProtectiveGroupStyle_Dan                                                                |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
|                                                                              | OEProtectiveGroupStyle_Dansyl                                                             |
| Image: structure of a sulfonamide dansyl protecting group on a naphthyl ring | Image: structure of a dansyl protecting group attached to an aniline, label “Dan” in pink |

## **DCB**

![](_page_460_Figure_2.jpeg)

## **DDE**

![](_page_460_Figure_4.jpeg)

## **DDIV**

![](_page_460_Figure_6.jpeg)

## **DEIPS**

![](_page_461_Figure_2.jpeg)

## **DMAB**

![](_page_461_Figure_4.jpeg)

## **DMIPS**

![](_page_461_Figure_6.jpeg)

## **DMPM**

![](_page_462_Figure_2.jpeg)

## **DMPS**

![](_page_462_Picture_4.jpeg)

## **DMTr**

![](_page_462_Figure_6.jpeg)

## **DNBZ**

![](_page_463_Figure_2.jpeg)

## **DNP**

![](_page_463_Picture_4.jpeg)

## **DOC**

![](_page_463_Figure_6.jpeg)

## **DPIPS**

![](_page_464_Figure_2.jpeg)

## **Dpp**

![](_page_464_Picture_4.jpeg)

## **DTBMS**

![](_page_464_Figure_6.jpeg)

## EE

![](_page_465_Figure_2.jpeg)

## **ESC**

![](_page_465_Figure_4.jpeg)

## **Fmoc**

![](_page_465_Figure_6.jpeg)

## **FourOMeBz**

![](_page_466_Figure_2.jpeg)

## **FPMP**

![](_page_466_Figure_4.jpeg)

## $Im$

![](_page_466_Figure_6.jpeg)

## Lev

![](_page_467_Figure_2.jpeg)

## **MDIPS**

![](_page_467_Figure_4.jpeg)

## **MDPS**

![](_page_467_Figure_6.jpeg)

## **MEM**

![](_page_468_Figure_2.jpeg)

## **Mes**

![](_page_468_Figure_4.jpeg)

## **MMTR**

![](_page_468_Figure_6.jpeg)

## **MOM**

![](_page_469_Figure_2.jpeg)

## **Moz**

![](_page_469_Figure_4.jpeg)

## **MPC**

![](_page_469_Figure_6.jpeg)

## **MPM**

| OEProtectiveGroupStyle_Off                                           | OEProtectiveGroupStyle_MPM                                               |
|----------------------------------------------------------------------|--------------------------------------------------------------------------|
| Image: molecule drawn with protective group style off (benzyl ester) | Image: molecule drawn with MPM protective group (label "MPM" in magenta) |

## **MS**

![](_page_470_Picture_4.jpeg)

## **MTHP**

![](_page_470_Figure_6.jpeg)

## **MTM**

![](_page_471_Figure_2.jpeg)

## **MTr**

![](_page_471_Figure_4.jpeg)

## **Np**

![](_page_471_Figure_6.jpeg)

![](_page_472_Picture_1.jpeg)

## **NPES**

![](_page_472_Picture_3.jpeg)

## **NPEOC**

![](_page_472_Figure_5.jpeg)

## **NPE**

## **NPS**

![](_page_473_Figure_2.jpeg)

## **NVOC**

![](_page_473_Picture_4.jpeg)

## **OBzl**

![](_page_473_Figure_6.jpeg)

## **ONOS**

![](_page_474_Figure_2.jpeg)

## **OtBu**

![](_page_474_Figure_4.jpeg)

## **PAC**

![](_page_474_Figure_6.jpeg)

## **PBF**

![](_page_475_Figure_2.jpeg)

## **PCB**

![](_page_475_Picture_4.jpeg)

## **PHF**

![](_page_475_Figure_6.jpeg)

![](_page_476_Figure_1.jpeg)

## **Piv**

![](_page_476_Figure_3.jpeg)

## **PMB**

![](_page_476_Figure_5.jpeg)

### Pht

## **PMBM**

![](_page_477_Figure_2.jpeg)

## Poc

![](_page_477_Figure_4.jpeg)

## **PPi**

![](_page_477_Figure_6.jpeg)

## **SEM**

![](_page_478_Figure_2.jpeg)

## **SES**

![](_page_478_Figure_4.jpeg)

## **StBu**

![](_page_478_Figure_6.jpeg)

## **TBMPS**

![](_page_479_Figure_2.jpeg)

## **TBDPS**

![](_page_479_Picture_4.jpeg)

## **TBDMS**

| <i>OEProtectiveGroupStyle_Off</i>                                                        | <i>OEProtectiveGroupStyle_TBDMS</i>                                             |
|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
|                                                                                          | <i>OEProtectiveGroupStyle_TBS</i>                                               |
| Image: benzyl alcohol protected with a fully drawn tert-butyldimethylsilyl (TBDMS) group | Image: benzyl alcohol protected with a “TBS” abbreviated protective group label |

## **TBS**

## **TCP**

![](_page_480_Figure_4.jpeg)

## **Teoc**

![](_page_480_Figure_6.jpeg)

## **TES**

![](_page_481_Figure_2.jpeg)

## **Tf**

![](_page_481_Figure_4.jpeg)

## **TFA**

![](_page_481_Figure_6.jpeg)

## **Thexyl**

![](_page_482_Figure_2.jpeg)

## **THF**

![](_page_482_Picture_4.jpeg)

## **THP**

![](_page_482_Figure_6.jpeg)

## **TIPS**

![](_page_483_Figure_2.jpeg)

## **TMOB**

![](_page_483_Figure_4.jpeg)

## **TMS**

![](_page_483_Figure_6.jpeg)

## transCinnamyl

![](_page_484_Figure_2.jpeg)

## **Trisyl**

![](_page_484_Figure_4.jpeg)

## **Troc**

![](_page_484_Figure_6.jpeg)

## **TRT**

![](_page_485_Figure_2.jpeg)

## **TS**

## **Tos**

![](_page_485_Figure_5.jpeg)

![](_page_486_Figure_2.jpeg)

## $\mathsf{z}$

## Cbz

| OEProtectiveGroupStyle_Off                                                             | OEProtectiveGroupStyle_Z<br>OEProtectiveGroupStyle_Cbz                                      |
|----------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| Image: [Molecule with benzyl carbamate protecting group shown in full structural form] | Image: [Molecule with benzyl carbamate protecting group; abbreviated with pink "Cbz" label] |

## 4.2.41 OERadicalDisplayType

The OERadicalDisplayType namespace contains the following constants:

See also:

- · OE2DAtomDisplay.GetRadical method
- · OE2DAtomDisplay. SetRadical method

## Xyl

### Off

The atom is not a radical *i.e.* no information is rendered.

#### **Diradical**

Atom with two unpaired electrons. Either electron-paired (singlet state) or electron-unpaired (triplet state). See example in Figure: Example of a diradical carbon depiction.

#### dichlorocarbene

![](_page_487_Figure_6.jpeg)

#### Fig. 324: Example of a diradical carbon depiction

### **Monoradical**

Atom with one unpaired electron. See example in Figure: Example of a monoradical carbon depiction.

![](_page_487_Figure_10.jpeg)

Fig. 325: Example of a monoradical carbon depiction

## 4.2.42 OEReportSetup

This namespace encodes symbolic constants used as bit-masks to indicate which image report layout parameters are being created when invoking the OEConfigureReportOptions function.

- OEReport class
- OEReportOptions class

## All

#### The combination of following constants:

- · OEReportSetup\_NumColsPerPage
- · OEReportSetup\_NumRowsPerPage
- · OEReportSetup\_PageHeight
- · OEReportSetup\_PageOrientation
- · OEReportSetup\_PageSize
- · OEReportSetup PageWidth

#### **NumColsPerPage**

Passing this constant to the OEConfigureReportOptions function result in generating the following default interface to configure the number of columns per page.

```
Contents of parameter -colsperpage
   Aliases : -cols
   Type : int
   Allow list : false
   Default : 2
   Simple : true
   Required : false
   Legal ranges :
       10 to 1Brief : Number of columns per page
```

#### See also:

· OEReportOptions. NumColsPerPage method

#### **NumRowsPerPage**

Passing this constant to the OEConfigureReportOptions function result in generating the following default interface to configure the number of rows per page.

```
Contents of parameter -rowsperpage
   Aliases : -rows
   Type : int
   Allow list : false
   Default : 3Simple : true
   Required : false
   Legal ranges :
       10 to 1Brief : Number of rows per page
```

### See also:

· OEReportOptions. NumRowsPerPage method

## **PageHeight**

Passing this constant to the OEConfigureReportOptions function result in generating the following default interface to configure the page height of the report.

```
Contents of parameter -pageheight
   Aliases : -h
   Type : double
   Allow list : false
   Default : (parameter does not have a default)
   Simple : true
   Required : false
   Legal ranges :
       2000.0 to 100.0
   Brief : Page height
```

#### See also:

· OEReportOptions. SetPageHeight method

### **PageOrientation**

Passing this constant to the OEConfigureReportOptions function result in generating the following default interface to configure the page orientation of the report.

```
Contents of parameter -pageorientation
   Aliases : - pori
   Type : string
   Allow list : false
   Default : Portrait
   Simple : true
   Required : false
   Legal values : Portrait Landscape
   Brief : Page orientation
```

- · OEReportOptions. SetPageOrientation method
- · OEPageOrientation namespace

#### **PageSize**

Passing this constant to the OEConfigureReportOptions function result in generating the following default interface to configure the page size of the report.

```
Contents of parameter -pagesize
   Aliases : - psize
   Type : string
   Allow list : false
   Default : US_Letter
   Simple : true
   Required : false
   Legal values : ISO_A4 US_Letter US_Legal Custom
   Brief : Page size
```

See also:

- · OEReportOptions. SetPageSize method
- OEPageSize namespace

#### **PageWidth**

Passing this constant to the OEConfigureReportOptions function result in generating the following default interface to configure the page width of the report.

```
Contents of parameter -pagewidth
   Aliases : -w
   Type : double
   Allow list : false
   Default : (parameter does not have a default)
   Simple : true
   Required : false
   Legal ranges :
       2000.0 to 100.0
   Brief : Page width
```

See also:

· OEReportOptions. SetPageWidth method

## **4.2.43 OEScale**

This namespace contains constants that determine the scaling factor of a molecule when positioned in an image.

See also:

- · OE2DMolDisplayOptions.GetScale
- · OE2DMolDisplayOptions.SetScale
- · OE2DMolDisplayOptions. SetDimensions

The OEScale namespace contains the following constants:

### **Default**

Specifies the default scaling of a molecule.

![](_page_491_Figure_3.jpeg)

Fig. 326: Default scaling of benzene

## **AutoScale**

Auto scaling means that a depicted molecule is scaled to maximally fit the given image dimensions.

#### See also:

• Controlling the Size of Depicted Molecules section

## 4.2.44 OEStipple

This namespace contains constants representing various stipple patterns.

#### See also:

- · OEPen. GetLineStipple method
- · OEPen. SetLineStipple method
- · OEPen.GetStippleFactor method
- · OEPen. SetStippleFactor method

The OEStipple namespace contains the following constants:

## **Default**

The default line stipple style is OEStipple\_Solid.

### **Dot**

See example in Figure: Example of line drawing with 'Dot' stipple style.

. . . . . . . . .

### Fig. 327: Example of line drawing with 'Dot' stipple style

## **DotDash**

See example in Figure: Example of line drawing with 'DotDash' stipple style.

-.-.-.-.-

Fig. 328: Example of line drawing with 'DotDash' stipple style

## **DotDashDash**

See example in Figure: Example of line drawing with 'DotDashDash' stipple style.

#### .............

Fig. 329: Example of line drawing with 'DotDashDash' stipple style

### **LongDash**

See example in Figure: Example of line drawing with 'LongDash' stipple style.

 $\qquad \qquad \qquad -$ 

Fig. 330: Example of line drawing with 'LongDash' stipple style

### **NoLine**

See example in Table: Example of drawing rectangles with various stipple styles.

| <i>OEStipple_Solid</i>                           | <i>OEStipple_Dot</i>                              | <i>OEStipple_NoLine</i>                 |
|--------------------------------------------------|---------------------------------------------------|-----------------------------------------|
| Image: light blue square with solid black border | Image: light blue square with dotted black border | Image: light blue square with no border |

#### Table 44: Example of drawing rectangles with various stipple styles

## **ShortDash**

See example in Figure: Example of line drawing with 'ShortDash' stipple style.

---------

Fig. 331: Example of line drawing with 'ShortDash' stipple style

### **Solid**

See example in Figure: Example of line drawing with 'Solid' stipple style.

### Fig. 332: Example of line drawing with 'Solid' stipple style

## 4.2.45 OESuperAtomStyle

This namespace contains constants representing the various super atom styles supported by OEDepict TK. Super atoms are representing specific functional groups that are contracted into a single label.

See also:

- · OE2DMolDisplayOptions.GetSuperAtomStyle method
- · OE2DMolDisplayOptions. SetSuperAtomStyle method
- · OEProtectiveGroupStyle namespace

The OESuperAtomStyle namespace contains the following constants:

### **Default**

The default super atom display style is OESuperAtomStyle\_Off.

## All

The combination of all super atom flags.

![](_page_494_Figure_3.jpeg)

## Off

No structural abbreviation is performed.

## **COOH**

![](_page_494_Figure_7.jpeg)

## $\overline{\text{coo}}$

![](_page_495_Figure_2.jpeg)

## **CHO**

![](_page_495_Figure_4.jpeg)

## **NC**

![](_page_495_Figure_6.jpeg)

## **CN**

| OESuperAtomStyle_Off                                                                              | OESuperAtomStyle_CN                                                                |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| Image: Benzene ring with two nitrile (–C≡N) groups explicitly drawn; nitrogen atoms colored blue. | Image: Benzene ring with two superatom "NC" groups; labels and bonds colored pink. |

## $N<sub>2</sub>$

![](_page_496_Figure_4.jpeg)

## **N3**

![](_page_496_Figure_6.jpeg)

## **NCO**

![](_page_497_Figure_2.jpeg)

## **NO2**

![](_page_497_Figure_4.jpeg)

## **CNO**

![](_page_497_Figure_6.jpeg)

## **ONO**

| OESuperAtomStyle_Off                                                    | OESuperAtomStyle_ONO                                                                  |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| Image: Benzene ring with two nitro (NO2) substituents drawn explicitly. | Image: Benzene ring with two superatom "ONO" substituents shown as pink "ONO" labels. |

## SO<sub>3</sub>H

![](_page_498_Figure_4.jpeg)

## **SO3\_**

![](_page_498_Figure_6.jpeg)

## PO3H<sub>2</sub>

![](_page_499_Figure_2.jpeg)

## CF<sub>3</sub>

![](_page_499_Figure_4.jpeg)

## CCI<sub>3</sub>

![](_page_499_Figure_6.jpeg)

| OESuperAtomStyle_Off                              | OESuperAtomStyle_Me                                                  |
|---------------------------------------------------|----------------------------------------------------------------------|
| Image: Dimethylbenzene skeleton without Me labels | Me<br>Me<br>Image: Dimethylbenzene skeleton with Me labels (magenta) |

Et

![](_page_500_Figure_4.jpeg)

Pr

![](_page_500_Figure_6.jpeg)

## **Bu**

![](_page_501_Figure_2.jpeg)

## **iBu**

![](_page_501_Figure_4.jpeg)

## sBu

![](_page_501_Figure_6.jpeg)

tBu

| OESuperAtomStyle_Off                                                             | OESuperAtomStyle_tBu                                     |
|----------------------------------------------------------------------------------|----------------------------------------------------------|
| Image: benzene ring with two tert-butyl groups drawn explicitly in skeletal form | Image: benzene ring with two pink "tBu" superatom labels |

## **OMe**

![](_page_502_Figure_4.jpeg)

## **OEt**

![](_page_502_Figure_6.jpeg)

## OPr

![](_page_503_Figure_2.jpeg)

## **OBu**

![](_page_503_Figure_4.jpeg)

## Oxygen

The combination of following super atom flags:

- · OESuperAtomStyle\_COOH
- · OESuperAtomStyle\_COO\_
- · OESuperAtomStyle\_CHO

## **Nitrogen**

The combination of the following super atom flags:

- · OESuperAtomStyle\_NC
- · OESuperAtomStyle\_CN
- · OESuperAtomStyle\_N2
- · OESuperAtomStyle\_N3

## **OxygenAndNitrogen**

The combination of the following super atom flags:

- · OESuperAtomStyle\_NCO
- · OESuperAtomStyle\_NO2
- · OESuperAtomStyle\_CNO
- · OESuperAtomStyle\_ONO

## **Sulfur**

The combination of the following super atom flags:

- · OESuperAtomStyle\_SO3H
- · OESuperAtomStyle\_SO3\_

### **Phosphorus**

The combination of the following super atom flags:

· OESuperAtomStyle\_PO3H2

## **Halide**

The combination of the following super atom flags:

- · OESuperAtomStyle\_CF3
- · OESuperAtomStyle\_CC13

## Carbon

The combination of the following super atom flags:

- · OESuperAtomStyle\_Me
- · OESuperAtomStyle\_Et
- · OESuperAtomStyle\_Pr
- · OESuperAtomStyle\_Bu
- · OESuperAtomStyle\_iBu
- · OESuperAtomStyle\_sBu
- · OESuperAtomStyle\_tBu

## **Ether**

The combination of the following super atom flags:

- · OESuperAtomStyle\_OMe
- · OESuperAtomStyle\_OEt
- · OESuperAtomStyle\_OPr
- · OESuperAtomStyle\_OBu

## 4.2.46 OETitleLocation

This namespace contains constants representing the position of the molecule title:

### See also:

- · OE2DMolDisplayOptions.GetTitleLocation
- · OE2DMolDisplayOptions.SetTitleLocation

The OETitleLocation namespace contains the following constants:

## **Default**

The default title location is OETitleLocation\_Top.

## **Bottom**

See example in Figure: Example of displaying molecule title at the bottom.

![](_page_506_Figure_3.jpeg)

Fig. 333: Example of displaying molecule title at the bottom

## **Hidden**

See example in Figure: Example of displaying molecule with no title.

![](_page_506_Figure_7.jpeg)

Fig. 334: Example of displaying molecule with no title

## **Top**

See example in Figure: Example of displaying molecule title at the top.

![](_page_506_Figure_11.jpeg)

Fig. 335: Example of displaying molecule title at the top

# **4.3 OEDepict Functions**

## 4.3.1 OEAddBuiltInHiddenSVGClass

const OESVGClass \*OEAddBuiltInHiddenSVGClass (OEImageBase & image)

Adds an OESVGClass to the given image that can be used to mark up a group of SVG elements to be hidden.

### See also:

- OESVGClass class
- OEImage class
- OEAddBuiltInVisibleSVGClass function
- OEGetBuiltInHiddenSVGClass function
- OEGetBuiltInVisibleSVGClass function

## 4.3.2 OEAddBuiltInVisibleSVGClass

const OESVGClass \*OEAddBuiltInVisibleSVGClass (OEImageBase & image)

Adds an OESVGClass to the given image that can be used to mark up a group of SVG elements to be visible.

#### See also:

- OESVGClass class
- OEImage class
- OEAddBuiltInHiddenSVGClass function
- · OEGetBuiltInHiddenSVGClass function
- · OEGetBuiltInVisibleSVGClass function

## **4.3.3 OEAddDepictionHydrogens**

**bool** OEAddDepictionHydrogens (OEChem:: OEMolBase &mol)

Adds explicit "depiction" hydrogens to the specified OEMolBase. Depiction hydrogens are hydrogens that need to be explicitly drawn in a 2D depiction to faithfully represent tetrahedral atom stereochemistry or cis/trans bond stereochemistry.

The OEAddDepictionHydrogens function identifies all implicit depiction hydrogens (using the OEHasDepictionHydrogens function), and converts them into explicit hydrogens using the OEAddExplicitHydrogens function. This function returns true if any depiction hydrogens were converted into explicit atoms.

- · OEHasDepictionHydrogens function
- OESuppressNonDepictionHydrogens function

## 4.3.4 OEAddHighlighting

Highlights atoms and/or bonds of the displayed molecule.

### Table 45: The overloaded versions of the OEAddHighlighting function using OEHighlightBase

| Link                                                                   | Description                                                             |
|------------------------------------------------------------------------|-------------------------------------------------------------------------|
| OEAddHighlighting(disp, highlight, <i>atompred</i> )                   | highlights atoms with OEHighlightBase                                   |
| OEAddHighlighting(disp, highlight, <i>bondpred</i> )                   | highlights bonds with OEHighlightBase                                   |
| OEAddHighlighting(disp, highlight, <i>atompred</i> , <i>bondpred</i> ) | highlights atoms and bonds with OEHighlightBase                         |
| OEAddHighlighting(disp, highlight, <i>match</i> )                      | highlights atoms and bonds of a match with OEHighlightBase              |
| OEAddHighlighting(disp, highlight, <i>abset</i> )                      | highlights atoms and bonds of a set with OEHighlightBase                |
| OEAddHighlighting(disp, highlight, <i>subsearch</i> )                  | highlights atoms and bonds of substructure matches with OEHighlightBase |

### Table 46: The overloaded versions of the OEAddHighlighting function using color and style

| Link                                                              | Description                                                |
|-------------------------------------------------------------------|------------------------------------------------------------|
| <i>OEAddHighlighting</i> (disp, color, style, atompred)           | highlights atoms with color and style                      |
| <i>OEAddHighlighting</i> (disp, color, style, bondpred)           | highlights bonds with color and style                      |
| <i>OEAddHighlighting</i> (disp, color, style, atompred, bondpred) | highlights atoms and bonds with color and style            |
| <i>OEAddHighlighting</i> (disp, color, style, match)              | highlights atoms and bonds of a match with color and style |
| <i>OEAddHighlighting</i> (disp, color, style, abset)              | highlights atoms and bonds of a set with color and style   |
| <i>OEAddHighlighting</i> (disp, color, style, subsearch)          | highlights atoms and bonds of substructure matches         |

### **Parameters:**

disp The OE2DMolDisplay object of which atoms add/or bonds being highlighted.

highlight The OEHighlightBase object that specifies the style of the highlighting.

color The OEColor object that specifies the color of the highlighting.

style The style of the highlighting from the  $OEHighlightStyle$  namespace.

atompred OEAddHighlighting function highlights only atoms for which the given atom predicate returns true.

**bondpred** OEAddHighlighting function highlights only bonds for which the given bond predicate returns true.

**match** OEAddHighlighting function highlights the target atoms and bonds of the OEMatchBase object.

abset Stores the atoms and bonds being highlighted.

subsearch The substructure search object of the matches being highlighted.

#### Highlights atom and/or bonds with the style implemented in the given OEHighlightBase object

The atoms and bonds being highlighted can be specified either by a predicate or an OEMatchBase object or an OEAtomBondSet object.

The following code snippets show different ways to highlight any 6 membered aromatic ring in a molecule using the OEHighlightByBallAndStick highlighting class. They all generate the image shown in Figure: Example of highlighting 6-membered aromatic rings.

#### 1. Highlighting using atom and bond predicates:

```
void OEAddHighlighting(OE2DMolDisplay &disp, const OEHighlightBase &highlight,
                         const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
\rightarrow atompred)
```

Highlights atoms with the style implemented in the given OEHighlightBase object. The atoms being highlighted are specified by given atom predicate.

```
void OEAddHighlighting (OE2DMolDisplay &disp, const OEHighlightBase &highlight,
                         const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &
\rightarrowbondpred)
```

Highlights bonds with the style implemented in the given OEHighlightBase object. The bonds being highlighted are specified by given bond predicates.

```
void OEAddHighlighting (OE2DMolDisplay& disp, const OEHighlightBase& highlight,
                         const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
\rightarrowatompred,
                         const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &
\rightarrowbondpred)
```

Highlights atoms and bonds with the style implemented in the given OEHighlightBase object. The atoms and bonds being highlighted are specified by given atom and bond predicates, respectively.

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
class Pred6MemAromAtom (oechem. OEUnaryAtomPred) :
    def call (self, atom):
        return atom. IsAromatic() and oechem. OEAtomIsInAromaticRingSize(atom, 6)
class Pred6MemAromBond(oechem.OEUnaryBondPred):
    def \_{call_{s}}(self, bond):return bond. IsAromatic() and oechem. OEBondIsInAromaticRingSize(bond, 6)
def OEAddHighlighting Predicate (disp):
    highlightstyle = oedepict.OEHighlightByBallAndStick(oechem.OELightGreen)
    oedepict.OEAddHighlighting(disp, highlightstyle, Pred6MemAromAtom())
    oedepict.OEAddHighlighting(disp, highlightstyle, Pred6MemAromBond())
def OEAddHighlighting_AtomAndBondPredicate(disp):
    highlightstyle = oedepict.OEHighlightByBallAndStick(oechem.OELightGreen)
    oedepict.OEAddHighlighting(disp, highlightstyle, Pred6MemAromAtom(),
\rightarrowPred6MemAromBond())
```

2. Highlighting using an OEMatchBase object that is initialized by substructure search or maximum common substructure search:

```
void OEAddHighlighting (OE2DMolDisplay &disp, const OEHighlightBase &highlight,
                       const OEChem:: OEMatchBase &match)
```

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
def OEAddHighlighting OEMatch (disp):
    subs = occhem. OESubSearch('lalaaaa1")unique = Truehighlightstyle = oedepict.OEHighlightByBallAndStick(oechem.OELightGreen)
    for match in subs. Match (disp. GetMolecule (), unique):
        oedepict.OEAddHighlighting(disp, highlightstyle, match)
```

3. Highlighting using an OEAtomBondSet object that stores the atoms and bonds being highlighted:

void OEAddHighlighting (OE2DMolDisplay &disp, const OEHighlightBase &highlight, const OEChem:: OEAtomBondSet &abset)

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
def OEAddHighlighting_OEAtomBondSet(disp):
   mol = disp.GetMolecule()abset = oechem. OEAtomBondSet (mol. GetAtoms (Pred6MemAromAtom(),)mol.GetBonds(Pred6MemAromBond()))
   highlightstyle = oedepict.OEHighlightByBallAndStick(oechem.OELightGreen)
    oedepict.OEAddHighlighting(disp, highlightstyle, abset)
```

4. Highlighting using an OESubSearch of which matches are being highlighted:

```
void OEAddHighlighting (OE2DMolDisplay &disp, const OEHighlightBase &highlight,
                        const OEChem:: OESubSearch & subsearch)
```

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
def OEAddHighlighting_OESubSearch(disp):
    subsearch = oechem. OESubSearch ("alaaaaa1")
    highlightstyle = oedepict.OEHighlightByBallAndStick(oechem.OELightGreen)
    oedepict.OEAddHighlighting(disp, highlightstyle, subsearch)
```

![](_page_510_Figure_12.jpeg)

Fig. 336: Example of highlighting 6-membered aromatic rings

#### See also:

- OEHighlightByColor class
- OEHighlightByCogwheel class
- OEHighlightByBallAndStick class
- OEHighlightByStick class
- OEHighlightByLasso class
- · OEDrawHighlighting function
- Highlighting chapter

#### Highlights atoms and/or bonds with the given color and style

The atoms and bonds being highlighted can be specified either by a predicate or an OEMatchBase object or an OEAtomBondSet object.

The following code snippets show three different ways to highlight any 6 membered aromatic ring in a molecule using the built-in highlighting styles. They all generate the image shown in Figure: Example of highlighting 6-membered aromatic rings.

1. Highlighting using atom and bond predicates:

```
void OEAddHighlighting (OE2DMolDisplay &disp, const OESystem::OEColor &color,
                         unsigned int style,
                         const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
\rightarrow atompred)
```

Highlights atoms with the given color and style. The atoms being highlighted are specified by given atom predicate.

```
void OEAddHighlighting (OE2DMolDisplay &disp, const OESystem::OEColor &color,
                         unsigned int style,
                         const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &
\rightarrowbondpred)
```

Highlights bonds with the given color and style. The bonds being highlighted are specified by given bonds predicate.

| <b>void</b> OEAddHighlighting(OE2DMolDisplay& disp, const OESystem::OEColor& color, |
|-------------------------------------------------------------------------------------|
| unsigned int style,                                                                 |
| const OESystem::OEUnaryPredicate<OEChem::OEAtomBase> &                              |
| $\rightarrow$ atompred,                                                             |
| const OESystem::OEUnaryPredicate<OEChem::OEBondBase> &                              |
| $\rightarrow$ bondpred)                                                             |

Highlights atoms and bonds with the given color and style. The atoms and bonds being highlighted are specified by given atom and bond predicates, respectively.

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
class Pred6MemAromAtom (oechem. OEUnaryAtomPred) :
    def _call_(self, atom):
        return atom. IsAromatic() and oechem. OEAtomIsInAromaticRingSize(atom, 6)
class Pred6MemAromBond(oechem.OEUnaryBondPred):
    def __call__(self, bond):
```

```
return bond. IsAromatic() and oechem. OEBondIsInAromaticRingSize(bond, 6)
def OEAddHighlighting_Predicate(disp):
    oedepict.OEAddHighlighting(disp, oechem.OEDarkGreen,
                                 oedepict.OEHighlightStyle_Color,
\rightarrowPred6MemAromAtom())
    oedepict.OEAddHighlighting(disp, oechem.OEDarkGreen,
                                 oedepict.OEHighlightStyle_Color,
\rightarrowPred6MemAromBond())
def OEAddHighlighting_AtomAndBondPredicate(disp):
    oedepict.OEAddHighlighting(disp, oechem.OEDarkGreen, oedepict.
\rightarrowOEHighlightStyle Color,
                                 Pred6MemAromAtom(), Pred6MemAromBond())
```

2. Highlighting using an OEMatchBase object that is initialized by substructure search or maximum common substructure search:

```
void OEAddHighlighting (OE2DMolDisplay &disp, const OESystem::OEColor &color,
                       unsigned int style, const OEChem:: OEMatchBase &match)
```

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
def OEAddHighlighting_OEMatch(disp):
    subs = oechem. OESubSearch ("alaaaaa1")
   unique = Truefor match in subs. Match (disp. GetMolecule (), unique) :
        oedepict.OEAddHighlighting(disp, oechem.OEDarkGreen, oedepict.
→OEHighlightStyle_Color, match)
```

3. Highlighting using an OEAtomBondSet object that stores the atoms and bonds being highlighted:

void OEAddHighlighting (OE2DMolDisplay &disp, const OESystem::OEColor &color, unsigned int style, const OEChem:: OEAtomBondSet &abset)

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
def OEAddHighlighting_OEAtomBondSet(disp):
    abset = oechem. OEAtomBondSet (mol. GetAtoms (Pred6MemAromAtom()),
                                 mol.GetBonds(Pred6MemAromBond()))
    oedepict.OEAddHighlighting(disp, oechem.OEDarkGreen, oedepict.
→OEHighlightStyle_Color, abset)
```

4. Highlighting using an OESubSearch of which matches are being highlighted:

```
void OEAddHighlighting (OE2DMolDisplay &disp, const OESystem:: OEColor& color,
                         unsigned int style, const OEChem:: OESubSearch &
\rightarrowsubsearch);
```

**Example:** (See image generated in *Example of highlighting 6-membered aromatic rings*)

```
def OEAddHighlighting_OESubSearch(disp):
    subsearch = oechem. OESubSearch('lalaaaaal")
```

```
oedepict.OEAddHighlighting(disp, oechem.OEDarkGreen, oedepict.
+OEHighlightStyle_Color, subsearch)
```

![](_page_513_Figure_3.jpeg)

![](_page_513_Figure_4.jpeg)

#### See also:

- OEColor class
- · OEHighlightStyle namespace
- Highlighting chapter

## 4.3.5 OEAddHighlightOverlay

```
void OEAddHighlightOverlay (OE2DMolDisplay &disp,
                           const OEHighlightOverlayBase &highlight,
                           OESystem::OEIter<OEChem::OEMatchBase> &matches)
void OEAddHighlightOverlay (OE2DMolDisplay &disp,
                           const OEHighlightOverlayBase &highlight,
                           OESystem::OEIter<OEChem::OEAtomBondSet> &absets)
void OEAddHighlightOverlay (OE2DMolDisplay &disp,
                           const OEHighlightOverlayBase &highlight,
                           OESystem::OEIterBase<OEChem::OEMatchBase> *matches)
void OEAddHighlightOverlay (OE2DMolDisplay &disp,
                           const OEHighlightOverlayBase &highlight,
                           OESystem::OEIterBase<OEChem::OEAtomBondSet> *absets)
void OEAddHighlightOverlay (OE2DMolDisplay& disp, const OEHighlightOverlayBase&
\rightarrowhighlight,
                           const std::vector<OEChem::OEAtomBondSet>& absets)
```

Highlights a set of atoms and/or bonds of the displayed molecule.

## **Parameters:**

disp The OE2DMolDisplay object of which atoms add/or bonds being highlighted.

**highlight** The OEHighlightOverlayBase object that specifies the style of the highlighting.

*matches* The iterator of OEMatchBase objects of which target atoms and bonds being highlighted.

**absets** The iterator of OEAtomBondSet objects of which atoms and bonds being highlighted.

Note: Each pattern will be highlighted with a different color returned by the OEHighlightOverlayBase. GetColors method.

See also:

- OEHighlightOverlayBase class
- · OEHighlightOverlayStyle namespace
- Highlighting Overlapped Patterns section

## 4.3.6 OEAddInteractivelcon

```
void OEAddInteraciveIcon (OEImageBase & image,
                         unsigned int loc=OEIconLocation::Default,
                         double scale=1.0)
void OEAddInteraciveIcon (OE2DMolDisplay &disp,
                         unsigned int loc=OEIconLocation::Default,
                         double scale=1.0)
```

Adds an icon to an image or a molecule display that indicates that the image is interactive.

loc This value has to be from the OEIconLocation namespace.

scale The multiplier that can be used to increase or decrease the size of the icon. This value has to be in the range of  $[0.5, 2.0].$ 

## 4.3.7 OEAddLabel

Adds label to an image or molecule display.

| Link                                      | Description                                    |
|-------------------------------------------|------------------------------------------------|
| <i>OEAddLabel(image, position, label)</i> | adding label to an image                       |
| <i>OEAddLabel(disp, label, match)</i>     | adding label to atoms of a match               |
| <i>OEAddLabel(disp, label, abset)</i>     | adding label to set of atoms                   |
| <i>OEAddLabel(disp, label, atompred)</i>  | adding label to atoms specified by a predicate |

Table 47: The overloaded versions of the OEAddLabel function

When adding label associated with atoms it is recommended to use the OEAddLabel along with the Note: OEAddHighlighting function for visual clarity.

void OEAddLabel (OEImageBase& image, const OE2DPoint& center, const OEHighlightLabel& label)

*image* The image in which the label is drawn.

center The center of the label on the image.

label The OEHighlightLabel object that stores properties that determine the styles of the label along with the text of the label itself.

#### **Example:**

```
def OEAddLabel_OEImage(image):
    label = oedepict.OEHighlightLabel("Hello!")
   oedepict.OEAddLabel(image, oedepict.OE2DPoint(50, 50), label)
   label.SetBoundingBoxPen(oedepict.OETransparentPen)
   oedepict.OEAddLabel(image, oedepict.OE2DPoint(100, 50), label)
   label.SetBoundingBoxPen(oedepict.OELightGreyPen)
   oedepict.OEAddLabel(image, oedepict.OE2DPoint(150, 50), label)
```

![](_page_515_Picture_3.jpeg)

## Fig. 338: Example of adding labels to an image

```
void OEAddLabel (OE2DMolDisplay &disp,
                const OEHighlightLabel &label,
                const OEChem:: OEMatchBase &match)
```

Adds label to atoms of an OEMatchBase object that can be initialized by substructure search or maximum common substructure search.

**disp** The OE2DMolDisplay object on which the label is going to be positioned.

label The OEHighlightLabel object that stores properties that determine the styles of the label along with the text of the label itself.

match The label is positioned based on the target atoms of the OEMatchBase object.

**Example:** 

```
def OEAddLabel_OEMatch(disp):
   subs = oechem. OESubSearch ("alaaaaa1")
   unique = Truehighlightstyle = oedepict.OEHighlightByBallAndStick(oechem.OELightGreen)
    for match in subs. Match (disp. GetMolecule (), unique) :
        oedepict.OEAddHighlighting(disp, highlightstyle, match)
        label = oedepict.OEHighlightLabel("aromatic", oechem.OELightGreen)
        oedepict.OEAddLabel(disp, label, match)
```

```
void OEAddLabel (OE2DMolDisplay &disp,
                const OEHighlightLabel &label,
                const OEChem:: OEAtomBondSet &abset)
```

Adds label to atoms stored in the OEAtomBondSet object.

disp The OE2DMolDisplay object on which the label is going to be positioned.

![](_page_516_Figure_1.jpeg)

Fig. 339: Example of adding label to 6-membered aromatic ring

label The OEHighlightLabel object that stores properties that determine the styles of the label along with the text of the label itself.

**abset** The label is positioned based on the atoms stored in the OEAtomBondSet object.

**Example:** 

```
def OEAddLabel OEAtomBondSet(disp):
   mol = disp.GetMolecule()ringset = occhem.OEAtomBondSet (mol. GetAtoms (occhem.OEAtomIsInRing())mol.GetBonds(oechem.OEBondIsInRing()))
   ringhighlight = oedepict.OEHighlightByBallAndStick(oechem.OELightGreen)
   oedepict.OEAddHighlighting(disp, ringhighlight, ringset)
   ringlabel = oedepict.OEHighlightLabel("ring", oechem.OELightGreen)
   oedepict.OEAddLabel(disp, ringlabel, ringset)
   chainset = oechem. OEAtomBondSet (mol. GetAtoms (oechem. OEAtomIsInChain()),
                                    mol.GetBonds(oechem.OEBondIsInChain()))
   chainhighlight = oedepict.OEHighlightByBallAndStick(oechem.OEBlueTint)
   oedepict.OEAddHighlighting(disp, chainhighlight, chainset)
   chainlabel = oedefict.OEH1qhlightLabel("chain", oechem.OEBlueTint)oedepict.OEAddLabel(disp, chainlabel, chainset)
```

void OEAddLabel (OE2DMolDisplay &disp, const OEHighlightLabel &label, const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &atompred)

Adds label to atoms for which the given atom predicate returns true.

disp The OE2DMolDisplay object on which the label is going to be positioned.

label The OEHighlightLabel object that stores properties that determine the styles of the label along with the text of the label itself.

atompred The label is positioned based on the atoms for which the given atom predicate returns true.

**Example:** 

![](_page_517_Figure_1.jpeg)

Fig. 340: Example of adding label to ring and chain components of a molecule

![](_page_517_Figure_3.jpeg)

![](_page_517_Figure_4.jpeg)

Fig. 341: Example of adding label to ring and chain components of a molecule

## 4.3.8 OEAddOpenEyelcon

```
void OEAddOpenEyeIcon (OEImageBase & image,
                      unsigned int loc=OEIconLocation::Default,
                      double scale=1.0)
void OEAddOpenEyeIcon (OE2DMolDisplay &disp,
                      unsigned int loc=OEIconLocation::Default,
                      double scale=1.0)
```

Adds an OpenEye logo to an image or a molecule display.

loc This value has to be from the OEIconLocation namespace.

scale. The multiplier that can be used to increase or decrease the size of the icon. This value has to be in the range of  $[0.5, 2.0].$ 

![](_page_518_Figure_6.jpeg)

Fig. 342: Example of using the OEAddOpenEyeIcon function

## **4.3.9 OEAddSVGClickEvent**

|          |  |  | Table 48: The overloaded versions of the OEAddSVGClickEvent |
|----------|--|--|-------------------------------------------------------------|
| function |  |  |                                                             |

| Link                                            | Description                                                  |
|-------------------------------------------------|--------------------------------------------------------------|
| <i>OEAddSVGClickEvent(disp, adisp, message)</i> | adding click event to <i>OE2DAtomDisplay</i>                 |
| <i>OEAddSVGClickEvent(disp, bdisp, message)</i> | adding click event to <i>OE2DBondDisplay</i>                 |
| <i>OEAddSVGClickEvent(svggroup, message)</i>    | adding click event to <i>OESVGGroup</i> (low-level function) |

bool OEAddSVGClickEvent (OE2DMolDisplay& disp, OE2DAtomDisplay\* adisp, const std:: string& message); bool OEAddSVGClickEvent (OE2DMolDisplay& disp, OE2DBondDisplay\* bdisp, const std:: string& message) ;

Adds a click event to an atom or bond in an . svg image. When clicking at the position defined by the given atom or bond display, an event is triggered with the given message.

**Note:** This functionality is **only available** for . svq image format.

### See also:

• Generating Interactive SVG Images chapter including the How to Catch SVG Events section

**disp** The OE2DMolDisplay object that holds the data necessary to depict the molecule with which it is initialized.

**adisp** The OE2DAtomDisplay object that defines the mouse click position.

**bdisp** The OE2DBondDisplay object that defines the mouse click position

*message* The text that will be emitted when an event is triggered on mouse click.

**Example for adding event for atom displays** 

```
width, height = 400, 200
image = oedepict. OEImage (width, height)
mol = occhem.OEGraphMol()smiles = "Cc1cccnc1/C=C/[C@H] (C(=0)0)0"
oechem.OESmilesToMol(mol, smiles)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetMargins(10)
disp = oedepict.OE2DMolDisplay(mol, opts)
for adisp in disp. GetAtomDisplays():
   atom = adisp.GetAtom()message = "atom idx = <i>s</i> s" % atom. GetIdx ()
    oedepict.OEAddSVGClickEvent(disp, adisp, message)
oedepict.OERenderMolecule("AddAtomClickEvent.svg", disp)
```

**Example for adding event for bond displays** 

```
width, height = 400, 200
image = oedepict. OEImage(width, height)
mol = occhem. OEGraphMol()smiles = "Cclccencl/C=C/[C@H] (C(=0) 0) 0"oechem.OESmilesToMol(mol, smiles)
oedepict.OEPrepareDepiction(mol)
opts = oedepict. OE2DMolDisplayOptions (width, height, oedepict. OEScale_AutoScale)
opts.SetMargins(10)
disp = oedepict.OE2DMolDisplay(mol, opts)
for bdisp in disp. GetBondDisplays():
   bond = bdisp.GetBond()message = "bond idx = *s" * bond.getIdx()oedepict.OEAddSVGClickEvent(disp, bdisp, message)
oedepict.OERenderMolecule("AddBondClickEvent.svg", disp)
```

#### See also:

- OE2DMolDisplay class
- OE2DAtomDisplay and OE2DBondDisplay classes

bool OEAddSVGClickEvent (OESVGGroup\* svggroup, const std::string& message);

Adds a click event to a specific SVG group in . svg image. When clicking at the elements drawn inside the given OESVGGroup object, an event is triggered with the given message

**Note:** This functionality is **only available** for . svq image format.

**Hint:** The OEAddSVGC1ickEvent function should always be called prior to pushing / popping the OESVGGroup object.

#### **Example:**

The following example creates an . svg image with a red rectangle and a blue circle. Both drawing elements are rendered inside OESVGGroup objects that are associated with messages clicked on rectangle and clicked on circle, respectively. When the generated . svq image is displayed in a HTTP server, clicking on the rectangle and the circle triggers events with the corresponding messages.

```
group_rectangle = image.NewSVGGroup("rectangle")
message = "clicked on rectangle"
oedepict.OEAddSVGClickEvent(group_rectangle, message)
image.PushGroup(group_rectangle)
image.DrawRectangle(oedepict.OE2DPoint(30, 30), oedepict.OE2DPoint(70, 70), oedepict.
\rightarrowOERedBoxPen)
image.PopGroup(group_rectangle)
group_circle = image.NewSVGGroup("circle")
message = "clicked on circle"
oedepict.OEAddSVGClickEvent(group_circle, message)
image.PushGroup(group_circle)
image.DrawCircle(oedepict.OE2DPoint(150, 50), 30, oedepict.OEBlueBoxPen)
image.PopGroup(group_circle)
oedepict.OEWriteImage("AddSVGClickEvent.svg", image)
```

#### See also:

- Generating Interactive SVG Images chapter including the How to Catch SVG Events section that shows how to test the . svg image file generated by this example.
- OEAddSVGHover function
- · OEAddSVGToggle function

## 4.3.10 OEAddSVGHover

bool OEAddSVGHover (OESVGGroup \*area, OESVGGroup \*target)

Adds a hover effect to the objects drawn between the two given groups. While hovering the mouse over objects drawn inside the area group the objects drawn in the target group are displayed.

**Note:** This functionality is **only available** for . svg image format.

- Generating Interactive SVG Images chapter
- OESVGGroup class
- · OEAddSVGClickEvent function
- · OEAddSVGToggle function

**Example:** 

```
hover_area = image.NewSVGGroup("hover_area")
target_area = image.NewSVGGroup("hover_target_area")
oedepict.OEAddSVGHover(hover_area, target_area)
image.PushGroup(hover_area)
image.DrawRectangle(oedepict.OE2DPoint(30, 30),
                    oedepict. OE2DPoint (70, 70), oedepict. OERedBoxPen)
image.PopGroup(hover_area)
image.PushGroup(target_area)
image.DrawCircle(oedepict.OE2DPoint(150, 50), 30, oedepict.OEBlueBoxPen)
image.PopGroup(target_area)
oedepict.OEAddInteractiveIcon(image)
oedepict.OEWriteImage("AddSVGHover.svg", image)
```

**Hint:** The OEAddSVGHover function should always be called prior to pushing / popping the OESVGGroup objects.

## 4.3.11 OEAddSVGToggle

**bool** OEAddSVGToggle (OESVGGroup \*area, OESVGGroup \*target, bool on = false)

Adds a toggle effect to the objects drawn between the two given groups. When clicking on the objects drawn inside the area group the objects drawn in the target group appear / disappear.

on The parameter that determine whether the objects drawn inside the **target** group are displayed initially.

Note: This functionality is only available for . svg image format.

See also:

- Generating Interactive SVG Images chapter
- OESVGGroup class
- · OEAddSVGClickEvent function
- OEAddSVGHover function

**Example:** 

```
toggle_area = image.NewSVGGroup("toggle_area")
target_area = image.NewSVGGroup("toggle_target_area")
```

```
oedepict.OEAddSVGToggle(toggle_area, target_area)
image.PushGroup(toggle_area)
image.DrawRectangle(oedepict.OE2DPoint(30, 30),
                    oedepict.OE2DPoint(70, 70), oedepict.OERedBoxPen)
image.PopGroup(toggle_area)
image.PushGroup(target_area)
image.DrawCircle(oedepict.OE2DPoint(150, 50), 30, oedepict.OEBlueBoxPen)
image.PopGroup(target_area)
oedepict.OEAddInteractiveIcon(image)
oedepict.OEWriteImage("AddSVGToggle.svg", image)
```

The OEAddSVGToggle function should always be called prior to pushing / popping the OESVGGroup Hint: objects.

## 4.3.12 OEAddWatermark

```
void OEAddWatermark (OEImageBase &image, const std::string &text,
                    double scale=1.0)void OEAddWatermark (OE2DMolDisplay &disp, const std::string &text,
                    double scale=1.0)
```

Adds a watermark to an image or a molecule display.

text The text of the watermark.

scale. The multiplier that can be used to increase or decrease the font size of the watermark text. This value has to be in the range of  $[0.5, 2.0]$ .

## 4.3.13 OEAnnotateDepictionProblems

**bool** OEAnnotateDepictionProblems (OE2DMolDisplay &disp)

Annotates various depiction problems on the molecule. Currently it can mark double bonds which are not depicted correctly according to their cis/trans stereo specifications.

**disp** The *OE2DMolDisplay* object being annotated.

The following code snippet show how to use the OEAnnotateDepictionProblems function. See the generated image in Figure: Example of incorrect trans double bond depiction. The highlighting indicates that the double bond specified in the input SMILES string as trans is depicted as cis.

```
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "C1CCC2C/C=C/CCCC2C1")
oedepict.OEPrepareDepiction(mol)
width, height = 200, 200opts = oedepict. OE2DMolDisplayOptions (width, height, oedepict. OEScale_AutoScale)
disp = oedepict.OE2DMolDisplay(mol, opts)
```

```
(continued from previous page)
oedepict.OEAnnotateDepictionProblems(disp)
oedepict.OERenderMolecule("OEAnnotateDepictionProblems.png", disp)
```

![](_page_523_Picture_2.jpeg)

### Fig. 343: Example of incorrect trans double bond depiction

Note: OEDepict TK uses built-in ring system templates when generating 2D coordinates. Generating 2D coordinates which are inconsistent with cis/trans stereo bond specification can occur due to a missing ring template. The OEP repareDepiction function throws a warning when this problem occurs.

## 4.3.14 OEAnnotateValenceProblems

**bool** OEAnnotateValenceProblems (OE2DMolDisplay &disp)

Annotates potential valence problems on the molecule.

disp The OE2DMolDisplay object being annotated.

The following code snippet show how to use the OEAnnotateValenceProblems function. See the generated image in Figure: Example of molecule with incorrect valences.

```
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "C[N+](=C)(C)C1CCCC11")
oedepict.OEPrepareDepiction(mol)
width, height = 200, 200opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OEAnnotateValenceProblems(disp)
oedepict.OERenderMolecule("OEAnnotateValenceProblems.png", disp)
```

![](_page_524_Picture_1.jpeg)

Fig. 344: Example of molecule with incorrect valences

Note: The OEAnnotateValenceProblems function uses the MDL Valence Model.

## 4.3.15 OEConfigure2DMolDisplayOptions

```
bool OEConfigure2DMolDisplayOptions (OESystem:: OEInterface &itf,
                                     unsigned int config=OE2DMolDisplaySetup:: All)
```

Configures the given interface to add molecule depiction style parameters.

*itf* The interface being configured.

config The option that specifies which parameters will be added to the interface This value has to be from the OE2DMolDisplaySetup namespace.

### See also:

- OEInterface class in the **OEChem TK** manual
- · OE2DMolDisplaySetup namespace
- OESetup2DMolDisplayOptions function

 $OEConfigure2DMolDisplayOptions$  is the utility function that allows to easily generate consistent command line interface for depiction examples and applications. For each command line options the generated interface will include information about related APIs in OEDepict TK, For example:

prompt> python mol2img.py --help -aromstyle

will reveals that the *-aromstyle* command line parameter is related to the OE2DMolDisplayOptions. SetAromaticStyle method and the OEAromaticStyle namespace (see the "Details" section below):

```
Contents of parameter -aromstyle
Aliases : -astl
Type : string
```

```
Allow list : false
Default : Kekule
Simple : true
Required : false
Legal values : Kekule Circle Dash
Brief : Aromatic ring display style
Detail
```

API : OE2DMolDisplayOptions::SetAromaticStyle method and OEAromaticStyle namespace

#### When generating an html help file:

```
prompt> python mol2img.py --help html
Creating 'mol2img.py_help.html'
```

The generated 'mol2img.py\_help.html' file will contain hyperlinks to related APIs in the OEDepict TK documentation.

#### See also:

• Depicting a Single Molecule

## 4.3.16 OEConfigureColor

```
bool OEConfigureColor (OESystem:: OEInterface &itf, const std:: string &name,
                      const std:: string &alias, const std:: string &brief,
                       std::string defcolor="red")
```

Adds a *color* parameter to the given interface.

*itf* The interface being configured.

*name* The name of the color parameter.

alias The alternative *i.e.* alias name of the parameter.

brief The brief description of the parameter.

defcolor The default color of the parameter.

### **Example:**

```
itf = oechem. OEInterface()
oedepict.OEConfigureColor(itf, "mycolor", "c", "Example of using OEConfigureColor",
\leftrightarrow"blue")
```

The above snippet will generate the following parameter:

```
Contents of parameter mycolor
   Aliases : c
   Type : string
   Allow list : false
   Default : blue
   Simple : true
   Required : false
   Legal values : black blue bluetint brass brown copper cyan darkblue
      darkbrown darkcyan darkgreen darkgrey darkmagenta darkorange
```

```
darkpurple darkred darkrose darksalmon darkyellow gold green
  greenblue greentint grey hotpink lightblue lightbrown lightgreen
  lightgrey lightorange lightpurple lightsalmon limegreen magenta
  mediumblue mediumbrown mediumgreen mediumorange mediumpurple
  mediumsalmon mediumyellow olivebrown olivegreen olivegrey pewter
  orange pink pinktint purple red redorange royalblue seagreen silver
  skyblue violet white yellow yellowtint
Brief : Example of using OEConfigureColor
```

See also:

- OEInterface class in the **OEChem TK** manual
- OEGetColor function
- OEColor class

## 4.3.17 OEConfigureHighlightColor

```
bool OEConfigureHighlightColor(OESystem::OEInterface &itf,
                               std::string name=OEHighlightParamName::Color,
                               std::string alias="-hcolor")
```

Adds a *highlighting color* parameter to the given interface.

*itf* The interface being configured.

name The name of the color parameter.

alias The alternative *i.e.* alias name of the parameter.

See also:

- OEInterface class in the **OEChem TK** manual
- OEColor class
- · OEHighlightSetup\_Color constant
- · OEHighlightParamName\_Color constant
- · OEGetHighlightColor function

## 4.3.18 OEConfigureHighlightParams

```
bool OEConfigureHighlightParams (OESystem:: OEInterface &itf,
                                 unsigned int config=OEHighlightSetup:: All)
```

Configures the given interface to add highlight style parameters.

*itf* The interface being configured.

```
config The option that specifies which parameters will be added to the interface. This value has to be from the
     OEHighlightSetup namespace.
```

- OEInterface class in the **OEChem TK** manual
- · OEHighlightSetup namespace

- · OEGetHighlightColor function
- OEGetHighlightStylefunction

## 4.3.19 OEConfigureHighlightStyle

```
bool OEConfigureHighlightStyle(OESystem:: OEInterface &itf,
                                std::string name=OEHighlightParamName::Style,
                               std::string alias="-hstyle")
```

Adds a highlighting style parameter to the given interface.

*itf* The interface being configured.

*name* The name of the style parameter.

*alias* The alternative *i.e.* alias name of the parameter.

### See also:

- OEInterface class in the OEChem TK manual
- OEHighlightSetup Style constant
- · OEHighlightParamName\_Style constant
- · OEGetHighlightStylefunction
- · OEHighlightStyle namespace

## 4.3.20 OEConfigureImageGridNumColumns

```
bool OEConfigureImageGridNumColumns (OESystem:: OEInterface &itf,
                                     std::string name=OEImageGridParamName::NumColumns,
                                     std::string alias="-cols")
bool OEConfigureImageGridNumColumns (OESystem:: OEInterface &itf,
                                     unsigned int defnumcols,
                                     std::string=OEImageGridParamName::NumColumns,
                                     std::string alias="-cols")
```

Adds a parameter to the given interface to allows the configuration of the number of grid columns.

*itf* The interface being configured.

defnumcols The default number of columns.

*name* The name of the parameter.

alias The alternative *i.e.* alias name of the parameter.

- OEInterface class in the **OEChem TK** manual
- · OEImageGridSetup\_NumColumns constant
- · OEImageGridParamName\_NumColumns constant
- · OEConfigureImageGridParamsfunction
- · OEGet ImageGridNumColumns function

## 4.3.21 OEConfigureImageGridNumRows

```
bool OEConfigureImageGridNumRows(OESystem::OEInterface &itf,
                                 std::string name=OEImageGridParamName::NumRows,
                                 std::string alias="-rows")
bool OEConfigureImageGridNumRows(OESystem::OEInterface &itf,
                                 unsigned int defnumrows,
                                 std::string=OEImageGridParamName::NumRows,
                                 std::string alias="-rows")
```

Adds a parameter to the given interface to allows the configuration of the number of grid rows.

itf The interface being configured.

defnumrows The default number of rows.

name The name of the parameter.

*alias* The alternative *i.e.* alias name of the parameter.

#### See also:

- OEInterface class in the OEChem TK manual
- OEImageGridSetup NumRows constant
- · OEImageGridParamName\_NumRows constant
- · OEConfigureImageGridParamsfunction
- · OEGet ImageGridNumRows function

## 4.3.22 OEConfigureImageGridParams

```
bool OEConfigureImageGridParams (OESystem:: OEInterface &itf,
                                 unsigned int config=OEImageGridSetup:: All)
```

Configures the given interface to add highlight style parameters.

itf The interface being configured.

config The option that specifies which parameters will be added to the interface. This value has to be from the OEImageSetup namespace.

- OEInterface class in the OEChem TK manual
- · OEImageSetup namespace
- OEConfigureImageGridNumColumnsfunction
- OEConfigureImageGridNumRowsfunction

## 4.3.23 OEConfigureImageHeight

```
bool OEConfigureImageHeight (OESystem::OEInterface &itf, double defheight=200.0,
                            std::string=OEImageParamName::Height,
                            std::string alias="-h")
```

Adds a parameter to the given interface to allows the configuration of the image height.

itf The interface being configured.

defheight Default height value.

*name* The name of the parameter.

*alias* The alternative *i.e.* alias name of the parameter.

#### See also:

- OEInterface class in the **OEChem TK** manual
- · OEImageSetup\_Height constant
- · OEImageParamName\_Height constant
- · OEConfigureImageOptionsfunction
- · OEGet ImageHeight function

## 4.3.24 OEConfigureImageOptions

```
bool OEConfigureImageOptions (OESystem:: OEInterface &itf,
                              unsigned int config=OEImageSetup:: All)
```

Configures the given interface to add image parameters.

*itf* The interface being configured.

```
config The option that specifies which parameters will be added to the interface. This value has to be from the
     OEImageSetup namespace.
```

### See also:

- OEInterface class in the **OEChem TK** manual
- · OEImageSetup namespace

## 4.3.25 OEConfigureImageWidth

```
bool OEConfigureImageWidth(OESystem::OEInterface &itf, double defwidth=200.0,
                           std::string=OEImageParamName::Width,
                           std::string alias="-w")
```

Adds a parameter to the given interface to allows the configuration of the image width.

*itf* The interface being configured.

defwidth Default width value.

*name* The name of the parameter.

*alias* The alternative *i.e.* alias name of the parameter.

#### See also:

- OEInterface class in the **OEChem TK** manual
- · OEImageSetup\_Width constant
- · OEImageParamName\_Width constant
- OEConfigureImageOptionsfunction
- · OEGetImageWidth function

## 4.3.26 OEConfigureMultiPageOrientation

```
bool OEConfigureMultiPageOrientation (OESystem:: OEInterface &itf,
                                        std::string
\rightarrowname=OEMultiPageParamName::PageOrientation,
                                        std::string alias="-pori")
```

Adds a parameter to the given interface to allows the configuration of the page orientation.

*itf* The interface being configured.

name The name of the parameter.

alias The alternative *i.e.* alias name of the parameter.

#### See also:

- OEInterface class in the **OEChem TK** manual
- OEMultiPageSetup PageOrientation constant
- · OEMultiPageParamName\_PageOrientation constant
- · OEConfigureMultiPageParams function
- · OEGetMultiPageOrientation function

## 4.3.27 OEConfigureMultiPageParams

```
bool OEConfigureMultiPageParams (OESystem:: OEInterface &itf,
                                 unsigned int config=OEMultiPageSetup:: All)
```

Configures the given interface to add multi-page parameters.

*itf* The interface being configured.

config The option that specifies which parameters will be added to the interface. This value has to be from the OEMultiPageSetup namespace.

- OEInterface class in the OEChem TK manual
- · OEMultiPageSetup namespace
- · OEConfigureMultiPageOrientation function
- · OEConfigureMultiPageSizefunction

## 4.3.28 OEConfigureMultiPageSize

```
bool OEConfigureMultiPageSize(OESystem:: OEInterface &itf,
                              std::string name=OEMultiPageParamName::PageSize,
                              std::string alias="-psize")
```

Adds a parameter to the given interface to allows the configuration of the page size.

itf The interface being configured.

name The name of the parameter.

*alias* The alternative *i.e.* alias name of the parameter.

#### See also:

• OEInterface class in the **OEChem TK** manual

- · OEMultiPageSetup\_PageSize constant
- · OEMultiPageParamName PageSize constant
- OEConfigureMultiPageParams function
- · OEGetMultiPageSizefunction

## 4.3.29 OEConfigurePrepareDepictionOptions

bool OEConfigurePrepareDepictionOptions(OESystem::OEInterface &itf,

```
\rightarrowconfig=OEPrepareDepictionSetup::All)
```

Configures the given interface to add parameters for preparing molecules for depiction.

*itf* The interface being configured.

```
config The option that specifies which parameters will be added to the interface This value has to be from the
     OEPrepareDepictionSetup namespace.
```

unsigned int

#### See also:

- OEInterface class in the **OEChem TK** manual
- · OEPrepareDepictionSetup namespace
- · OESetupPrepareDepictionOptionsfunction

## 4.3.30 OEConfigureReportOptions

```
bool OEConfigureReportOptions (OESystem:: OEInterface &itf,
                               unsigned int config=OEReportSetup:: All)
```

Configures the given interface to add parameters for the report layout.

*itf* The interface being configured.

config The option that specifies which parameters will be added to the interface This value has to be from the OEReportSetup namespace.

- OEInterface class in the OEChem TK manual
- · OEReportSetup namespace
- · OESetupReportOptions function

## 4.3.31 OECreateWin32GraphicsImage

Note: This function is only available on the Windows operating system through C++.

## 4.3.32 OEDepictCoordinates

**bool** OEDepictCoordinates (OEChem:: OEMolBase &mol)

Assigns 2D coordinates to the given OEMolBase object by invoking the OEGenerate2DCoordinates function. The coordinates of each explicit atom are assigned using the OEMo1Base. Set Coords method. This function automatically sets the dimensionality of the molecule to two, using the OEMolBase. SetDimension method.

Warning: OEDepictCoordinates is considered deprecated and will be removed in OEDepict 3.0. Please switch to using OEGenerate2DCoordinates.

## 4.3.33 OEDepictGetArch

const char \*OEDepictGetArch()

## 4.3.34 OEDepictGetLicensee

**bool** OEDepictGetLicensee(std::string &licensee)

## 4.3.35 OEDepictGetPlatform

const char \*OEDepictGetPlatform()

## 4.3.36 OEDepictGetRelease

const char \*OEDepictGetRelease()

## 4.3.37 OEDepictGetSite

**bool** OEDepictGetSite(std::string &site)

## 4.3.38 OEDepictGetVersion

unsigned int OEDepictGetVersion()

## 4.3.39 OEDepictIsLicensed

**bool** OEDepictIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any OEDepict TK functionality.

The 'feature' argument can be used to check for a valid license to OEDepict TK along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current OEDepict TK license.

#### See also:

· OEChemIsLicensed function

## 4.3.40 OEDrawBorder

void OEDrawBorder (OEImageBase &image, const OEPen &pen)

Draws a border around the image with the given pen.

*image* The image around which the border is drawn.

*pen* The graphical properties of the border.

See code snippet below and the corresponding image in Figure: Example of using the OEDrawBorder function.

```
width, height = 100, 50
image = odeplot.OEImage (width, height)pen = oedepict.OEPen(oechem.OEWhite, oechem.OELightGreen, oedepict.OEFill_Off, 4.0)
oedepict.OEDrawBorder(image, pen)
```

oedepict.OEWriteImage("OEDrawBorder.png", image)

![](_page_533_Picture_20.jpeg)

Fig. 345: Example of using the OEDrawBorder function

#### See also:

• OEImageBase class

### • OEPen class

• OEDrawCurvedBorder function

## 4.3.41 OEDrawChevronArrow

```
void OEDrawChevronArrow (OEImageBase& image, const OE2DPoint& bgn, const OE2DPoint&
\rightarrowend,
                         const OEPen& pen, double width = 5.0, double gapScale = 1.0);
```

Draws a chevron arrow. See example in Figure: Example of drawing a chevron arrows.

### >>>>>>>>>>>>>

### Fig. 346: Example of drawing a chevron arrow

*image* The image in which the arrow is drawn.

bgn, end The begin and end points of the arrow.

*pen* The graphical properties of the arrow.

width The width of the arrow.

gapScale The multiplier that defines the space between the lines of the chevron.

See also:

- OEImageBase class
- OE2DPoint class
- OEPen class

## 4.3.42 OEDrawCurvedArrow

```
void OEDrawCurvedArrow (OEImageBase& image, const OE2DPoint& center,
                       double bgnAngle, double endAngle, double radius,
                       bool clockwise, const OEPen& pen);
```

Draws a curved arrow. See example in Figure: Example of drawing curved arrows.

![](_page_534_Figure_20.jpeg)

Fig. 347: Example of drawing curved arrows

*image* The image in which the arrow is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc (in degrees). Both angles are in degrees and their values have to be in a range of  $[0.0^\circ, 360.0^\circ]$ . Angles are interpreted such that  $0.0^\circ$  and  $360.0^\circ$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

clockwise The direction of the arrow.

*pen* The graphical properties of the curved arrow.

See also:

- OEImageBase class
- OE2DPoint class
- OEPen class

## 4.3.43 OEDrawCurvedBorder

void OEDrawCurvedBorder (OEImageBase & image, const OEPen & pen, double radius);

Draws a round rectangle around the image with the given pen.

*image* The image around which the border is drawn.

*pen* The graphical properties of the border.

*radius* The parameter that determines the roundedness of the corners of the rectangle.

See code snippet below and the corresponding image in Figure: Example of using the OEDrawCurvedBorder function.

```
width, height = 100, 50
image = oedepict. OEImage (width, height)
pen = oedepict.OEPen(oechem.OEWhite, oechem.OELightGreen, oedepict.OEFill_Off, 4.0)
oedepict.OEDrawCurvedBorder(image, pen, 15)
oedepict.OEWriteImage("OEDrawCurvedBorder.png", image)
```

---

![](_page_535_Picture_18.jpeg)

### Fig. 348: Example of using the OEDrawCurvedBorder function

- OEImageBase class
- OEPen class
- · OEDrawBorder function
- OEDrawCurvedRectangle function

## 4.3.44 OEDrawCurvedRectangle

void OEDrawCurvedRectangle (OEImageBase& image, const OE2DPoint& tl, const OE2DPoint& br, const OEPen& pen, double radius);

Draws a round rectangle with the given pen.

*image* The image around which the border is drawn.

 $t\mathbf{l}$ ,  $b\mathbf{r}$  The position of the top-left and bottom-right corner of the rectangle.

*pen* The graphical properties of the border.

*radius* The parameter that determines the roundedness of the corners of the rectangle.

#### See also:

- OEImageBase class
- OEPen class
- · OEDrawBorder function
- · OEDrawCurvedBorder function

## 4.3.45 OEDrawEquilibriumArrow

```
void OEDrawEquilibriumArrow (OEImageBase & image, const OE2DPoint & bgn,
                             const OE2DPoint & end, const OEPen & pen)
```

Draws an equilibrium arrow between two points using the given pen. See example in Figure: Example of drawing an equilibrium arrow.

![](_page_536_Figure_16.jpeg)

## Fig. 349: Example of drawing an equilibrium arrow

*image* The image in which the arrow is drawn.

bgn, end The begin and end points of the arrow.

*pen* The graphical properties of the arrow.

- OEImageBase class
- OE2DPoint class
- OEPen class

## 4.3.46 OEDrawHighlighting

void OEDrawHighlighting (OEImageBase &image, const OE2DMolDisplay &disp, const OEHighlightBase &highlight, const OEChem:: OEAtomBondSet &abset)

Draws atom and bond highlighting into the image.

*image* The image in which the highlighting is drawn.

disp The OE2DMolDisplay object of which atoms add/or bonds being highlighted.

*highlight* The OEHighlightBase object that specifies the style of the highlighting.

abset Stores the atoms and bonds being highlighted.

This function renders the highlighting into an image rather than into the molecule display as does the Note: OEAddHighlighting function. Since this function does not change the molecule display it is not available for the *OEHighlightByColor* highlighting style.

#### See also:

· OEAddHighlighting function

## 4.3.47 OEDrawLegendLayout

**bool** OEDrawLegendLayout (OELegendLayout & layout)

Draws the legend layout.

**Note:** Interactive legend can only be used in . svq image format.

### See also:

- OELegendLayout class
- OELegendLayoutOptions class
- · OELegendLayoutStylenamespace
- · OELegendColorStyle namespace
- · OELegendInteractiveStyle namespace

#### **Example**

```
opts = oedepict.OELegendLayoutOptions(oedepict.OELegendLayoutStyle_VerticalTopRight,
                                      oedepict.OELegendColorStyle_LightGreen,
                                      oedepict.OELegendInteractiveStyle_Toggle)
opts.SetButtonWidthScale(1.5)
opts.SetButtonHeightScale(1.5)
legend = oedepict. OELegendLayout (image, "Legend", opts)
legend_area = legend.GetLegendArea()
oedepict. OEAddWatermark (legend_area, "This is the legend area")
oedepict.OEAddInteractiveIcon(image, oedepict.OEIconLocation_BottomRight, 0.75)
oedepict.OEDrawLegendLayout (legend)
```

```
oedepict.OEWriteImage("LegendLayout.svg", image)
```

**Hint:** The *OEDrawLegendLavout* function should be called after rendering all other information to the image.

## 4.3.48 OEDrawReactionArrow

```
void OEDrawReactionArrow (OEImageBase &image, const OE2DPoint &bgn,
                         const OE2DPoint &end, const OEPen &pen)
```

Draws a reaction arrow between two points using the given pen. See example in Figure: Example of drawing a reaction arrow.

#### Fig. 350: Example of drawing a reaction arrow

*image* The image in which the arrow is drawn.

bgn, end The begin and end points of the arrow.

*pen* The graphical properties of the arrow.

#### See also:

- OEImageBase class
- OE2DPoint class
- $\bullet$  OEPen class

## 4.3.49 OEDrawResonanceArrow

![](_page_538_Figure_16.jpeg)

Draws a resonance arrow between two points using the given pen. See example in Figure: Example of drawing a resonance arrow.

![](_page_538_Figure_18.jpeg)

#### Fig. 351: Example of drawing a resonance arrow

*image* The image in which the arrow is drawn.

bgn, end The begin and end points of the arrow.

*pen* The graphical properties of the arrow.

- OEImageBase class
- OE2DPoint class
- $\bullet$  OEPen class

## 4.3.50 OEDrawSVGHoverText

```
bool OEDrawSVGHoverText (OE2DMolDisplay &disp, OE2DAtomDisplay *adisp,
                        const std:: string & text, const OEFont & font)
bool OEDrawSVGHoverText (OE2DMolDisplay &disp, OE2DBondDisplay *bdisp,
                        const std:: string &text, const OEFont &font)
```

Creates and interactive effect in . svg images. The given text will appear when the mouse is hovering over the position defined by the given atom / bond display.

**Note:** This functionality is **only available** for . svg image format. In other image formats it has no effect.

The generated syq image should be included into and HTML page with the SVG MIME type.

<object data="<imagename>.svg" type="image/svg+xml"></object>

#### See also:

• Generating Interactive SVG Images chapter

disp The OE2DMolDisplay object that holds the data necessary to depict the molecule with which it is initialized.

adisp The OE2DAtomDisplay object that defines where the text will appear.

**bdisp** The OE2DBondDisplay object that defines where the text will appear.

text The text that appears when the cursor is hovered over the given position.

font The graphical properties of the font used to draw the text.

```
width, height = 400, 200
image = oedepict. OEImage (width, height)
mol = occhem. OEGraphMol()smiles = "Cclccencl/C=C/[C@H] (C(=0) 0) 0"oechem.OESmilesToMol(mol, smiles)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetMargins(10)
disp = oedepict.OE2DMolDisplay(mol, opts)
font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
\rightarrow12,
                       oedepict.OEAlignment_Center, oechem.OEDarkRed)
for adisp in disp. GetAtomDisplays():
   atom = adisp.GetAtom()hovertext = "atom idx = %s" % atom. GetIdx()
    oedepict.OEDrawSVGHoverText(disp, adisp, hovertext, font)
```

```
oedepict.OERenderMolecule("HoverAtomText.svg", disp)
```

There is no image available for the PDF version of this book.

```
width, height = 400, 200
image = oedepict. OEImage (width, height)
mol = occhem.OEGraphMol()smiles = "Cclccencl/C=C/[C@H] (C(=0) 0) 0"oechem.OESmilesToMol(mol, smiles)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetMargins(10)
disp = oedepict.OE2DMolDisplay(mol, opts)
font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
-12,
                       oedepict.OEAlignment_Center, oechem.OEDarkRed)
for bdisp in disp. GetBondDisplays():
   bond = bdisp.GetBond()hovertext = "bond idx = *s" * bond. GetIdx()
   oedepict.OEDrawSVGHoverText(disp, bdisp, hovertext, font)
oedepict.OERenderMolecule("HoverBondText.svg", disp)
```

There is no image available for the PDF version of this book.

See also:

- OE2DMolDisplay class
- OE2DAtomDisplay and OE2DBondDisplay classes
- OEFont class
- · OEDrawSVGToggleText function

## 4.3.51 OEDrawSVGToggleText

```
bool OEDrawSVGToggleText (OE2DMolDisplay &disp, OE2DAtomDisplay *adisp,
                        const std:: string &text, const OEFont &font)
bool OEDrawSVGToggleText (OE2DMolDisplay &disp, OE2DBondDisplay *bdisp,
                        const std:: string &text, const OEFont &font)
```

Creates and interactive effect in . svg images. The given text will appear / disappear when clicking at the position defined by the given atom / bond display.

Note: This functionality is only available for . svg image format. In other image formats it has no effects.

The generated svg image should be included into and HTML page with the SVG MIME type.

<object data="<imagename>.svg" type="image/svg+xml"></object>

#### See also:

• Generating Interactive SVG Images chapter

disp The OE2DMolDisplay object that holds the data necessary to depict the molecule with which it is initialized.

adisp The OE2DAtomDisplay object that defines where the text will appear.

*bdisp* The OE2DBondDisplay object that defines where the text will appear.

text The text that appears/disappears on mouse clicks.

font The graphical properties of the font used to draw the text.

```
width, height = 400, 200
image = oedepict. OEImage (width, height)
mol = occhem. OEGraphMol()smiles = "Cclccencl/C=C/[C@H] (C(=0) 0) 0"oechem.OESmilesToMol(mol, smiles)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetMargins(10)
disp = oedefict.OE2DMolDisplay(mol, opts)font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
-12oedepict.OEAlignment_Center, oechem.OEDarkRed)
for adisp in disp. GetAtomDisplays():
   atom = adisp.GetAtom()toggletext = "atom idx = %s" % atom. GetIdx()
   oedepict.OEDrawSVGToggleText(disp, adisp, toggletext, font)
oedepict.OERenderMolecule("ToggleAtomText.svg", disp)
```

There is no image available for the PDF version of this book.

```
width, height = 400, 200
image = oedepict. OEImage (width, height)
mol = oechem.OEGraphMol()
smiles = "Cclccencl/C=C/[C@H] (C(=0) 0) 0"oechem.OESmilesToMol(mol, smiles)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetMargins(10)
disp = oedepict.OE2DMolDisplay(mol, opts)
font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_Default,
\rightarrow12,
                       oedepict.OEAlignment_Center, oechem.OEDarkRed)
for bdisp in disp. GetBondDisplays():
   bond = bdisp.GetBond()toggletext = "bond idx = %s" % bond. GetIdx()
```

```
oedepict.OEDrawSVGToggleText(disp, bdisp, toggletext, font)
```

```
oedepict.OERenderMolecule("ToggleBondText.svg", disp)
```

There is no image available for the PDF version of this book.

See also:

- OE2DMolDisplay class
- OE2DAtomDisplay and OE2DBondDisplay classes
- OEFont class
- OEDrawSVGHoverText function

## 4.3.52 OEDrawText

```
void OEDrawText (OEImageBase &image, const std::string &text,
                const OEFont & font, double padding=5.0)
```

Draws the given text to the image respecting the font alignment.

text The text that is going to be rendered into the given image.

font The OEFont object that encapsulates properties that determine the display style of text.

*padding* Defines the padding used on the left and right of the given cell as a percentage of the width of the cell.

See also:

- OEImageBase class
- OEFont class
- · OEDrawTextToCenter function

## 4.3.53 OEDrawTextToCenter

```
void OEDrawTextToCenter (OEImageBase &image, const std::string &text,
                                             const OEFont & font)
```

Draws the given text to the center of the image.

See code snippet below and the corresponding image in Figure: Example of using the OEDrawTextToCenter function.

```
width, height = 100, 50
image = oedepict. OEImage (width, height)
oedepict.OEDrawTextToCenter(image, "center", oedepict.OEDefaultFont)
oedepict.OEDrawBorder(image, oedepict.OELightGreyPen)
oedepict.OEWriteImage("OEDrawTextToCenter.png", image)
```

- OEImageBase class
- OEFont class

![](_page_543_Picture_1.jpeg)

#### Fig. 352: Example of using the OEDrawTextToCenter function

- OEDrawBorder function
- OEDrawText function

## 4.3.54 OEEstimateTextWidth

double OEEstimateTextWidth(const std::string &text, const OEFont &font)

Estimates the width of string depicted with a specific style.

text The string of which width is being estimated.

font The OEFont object that defines the style of the depiction.

#### See also:

- · OEReduceFontSizeToFit function
- OEFont class

## 4.3.55 OEGetAverageBondLengthInDispCoords

double OEGetAverageBondLengthInDispCoords (const OE2DMolDisplay &disp)

Returns the average bond length of the molecule in "display" coordinate system.

## 4.3.56 OEGetBuiltInHiddenSVGClass

const OESVGClass \*OEGetBuiltInHiddenSVGClass (OEImageBase & image)

Returns an OESVGClass that have been previously added to the given image by calling the OEAddBuiltInHiddenSVGClassfunction.

- OESVGClass class
- OEImage class
- OEAddBuiltInHiddenSVGClassfunction
- OEAddBuiltInVisibleSVGClassfunction
- · OEGetBuiltInVisibleSVGClass function

## 4.3.57 OEGetBuiltInVisibleSVGClass

const OESVGClass \*OEGetBuiltInVisibleSVGClass (OEImageBase &image)

Returns an OESVGClass that have been previously added to the given image by calling the OEAddBuiltInVisibleSVGClassfunction.

#### See also:

- OESVGClass class
- *OEImage* class
- · OEAddBuiltInHiddenSVGClass function
- · OEAddBuiltInVisibleSVGClass function
- · OEGetBuiltInHiddenSVGClass function

## 4.3.58 OEGetCenter

OE2DPoint OEGetCenter (const OEImageBase &image)

Returns the center of the image.

#### See also:

• OE2DPoint class

## 4.3.59 OEGetColor

```
OESystem:: OEColor OEGetColor (const OESystem:: OEInterface &itf,
                               const std:: string & name)
```

Returns the color initialized in the given interface.

*itf* The interface in which the parameter is configured.

*name* The name of the parameter.

See also:

- · OEConfigureColor function
- OEColor class

## 4.3.60 OEGetDefaultAtomColor

```
OESystem:: OEColor OEGetDefaultAtomColor (unsigned int atomic,
                                         unsigned int style=OEAtomColorStyle:: WhiteCPK)
```

Returns the default color associated with an atomic number for the given atom color style.

*atomic* Atomic number.

style This value has to be from the OEAtomColorStyle namespace.

See also:

Appendix: Element coloring (CPK) chapter

## 4.3.61 OEGetDisplayCoords

OE2DPoint OEGetDisplayCoords (const OE2DMolDisplay &disp, const OE2DPoint &p)

Converts a 2D point from the "molecule" 2D coordinate system" to "display" 2D coordinate system.

This is the reverse operation from OEGetDisplayCoords.

#### See also:

· OEGetMoleculeCoords function

## 4.3.62 OEGetHighlightColor

OESystem:: OEColor OEGetHighlightColor(const OESystem:: OEInterface &itf, std::string name=OEHighlightParamName::Color)

Returns the highlight color initialized in the given interface.

*itf* The interface in which the parameter is configured.

*name* The name of the parameter.

#### See also:

- · OEConfigureHighlightParams function
- · OEConfigureHighlightColor function
- OEColor class

## 4.3.63 OEGetHighlightStyle

```
unsigned int OEGetHighlightStyle (const OESystem:: OEInterface &itf,
                                  std::string name=OEHighlightParamName::Style)
```

Returns the highlight style initialized in the given interface. The return value is taken from the OEHighlight Style namespace.

*itf* The interface in which the parameter is configured.

name The name of the parameter.

- · OEConfigureHighlightParams function
- · OEConfigureHighlightStylefunction
- · OEHighlightStyle namespace

## 4.3.64 OEGetImageGridNumColumns

```
unsigned int OEGetImageGridNumColumns (const OESystem:: OEInterface &itf,
                                      std::string
→name=OEImageGridParamName::NumColumns)
```

Returns the number of grid columns initialized in the given interface.

*itf* The interface in which the parameter is configured.

name The name of the parameter.

#### See also:

• OEConfigureImageGridNumColumnsfunction

## 4.3.65 OEGetImageGridNumRows

```
unsigned int OEGetImageGridNumRows (const OESystem:: OEInterface &itf,
                                    std::string name=OEImageGridParamName::NumRows)
```

Returns the number of grid rows initialized in the given interface.

*itf* The interface in which the parameter is configured.

*name* The name of the parameter.

#### See also:

· OEConfigureImageGridNumRowsfunction

## 4.3.66 OEGetImageHeight

```
double OEGetImageHeight (const OESystem:: OEInterface &itf,
                         std::string name=OEImageParamName::Height)
```

Returns the height of the image initialized in the given interface.

*itf* The interface in which the parameter is configured.

*name* The name of the parameter.

#### See also:

• OEConfigureImageHeight function

## 4.3.67 OEGetImageWidth

```
double OEGetImageWidth (const OESystem:: OEInterface &itf,
                       std::string name=OEImageParamName::Width)
```

Returns the width of the image initialized in the given interface.

itf The interface in which the parameter is configured.

*name* The name of the parameter.

• OEConfigureImageWidth function

## 4.3.68 OEGetLabelPosition

Returns the position used to add a label to an image or molecule display.

#### Table 49: The overloaded versions of the OEGetLabelPosition func-

| tion |  |
|------|--|
|      |  |

| Link                                             | Description                                                      |
|--------------------------------------------------|------------------------------------------------------------------|
| <i>OEGetLabelPosition(disp, label, match)</i>    | getting label position related to atoms of a match               |
| <i>OEGetLabelPosition(disp, label, abset)</i>    | getting label position related to set of atoms                   |
| <i>OEGetLabelPosition(disp, label, atompred)</i> | getting label position related to atoms specified by a predicate |

Note: When adding label associated with atoms it is recommended to use the OEAddLabel along with the OEAddHighlighting function for visual clarity.

OE2DPoint OEGetLabelPosition (const OE2DMolDisplay &disp, const OEHighlightLabel &label, const OEChem:: OEAtomBondSet &abset);

disp The OE2DMolDisplay object on which the label is going to be positioned.

label The OEHighlightLabel object that stores properties that determine the styles of the label along with the text of the label itself.

**abset** The label is positioned based on the atoms stored in the OEAtomBondSet object.

OE2DPoint OEGetLabelPosition (const OE2DMolDisplay &disp, const OEHighlightLabel &label, const OEChem:: OEMatchBase &match) ;

Adds label to atoms of an OEMatchBase object that can be initialized by substructure search or maximum common substructure search.

disp The OE2DMolDisplay object on which the label is going to be positioned.

label The OEHighlightLabel object that stores properties that determine the styles of the label along with the text of the label itself.

*match* The label is positioned based on the target atoms of the OEMatchBase object.

```
OE2DPoint OEGetLabelPosition (const OE2DMolDisplay &disp, const OEHighlightLabel &label,
                               const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &
\rightarrowatompred);
```

**disp** The OE2DMolDisplay object on which the label is going to be positioned.

label The OEHighlightLabel object that stores properties that determine the styles of the label along with the text of the label itself.

atompred The label is positioned based on the atoms for which the given atom predicate returns true.

## 4.3.69 OEGetMoleculeCoords

```
OE2DPoint OEGetMoleculeCoords (const OE2DMolDisplay &disp,
                              const OE2DPoint &p)
```

Converts a 2D point from the "display" 2D coordinate system" to "molecule" 2D coordinate system.

This is the reverse operation from OEGetMoleculeCoords.

#### See also:

· OEGetMoleculeCoords function

## 4.3.70 OEGetMoleculeScale

```
double OEGetMoleculeScale (const OEChem:: OEMolBase &mol,
                           const OE2DMolDisplayOptions &opts)
```

Estimates the scaling factor of the molecule depiction based on the parameters stored in given OE2DMolDisplayOptions object.

*mol* The molecule of which scaling factor is determined.

opts The OE2DMolDisplayOptions object that stores the parameters that determine the scaling factor (such as width and height).

See also:

• Controlling the Size of Depicted Molecules section

## 4.3.71 OEGetMultiPageOrientation

```
unsigned int OEGetMultiPageOrientation (const OESystem:: OEInterface &itf,
                                       std::string
→name=OEMultiPageParamName::PageOrientation)
```

Returns the page orientation initialized in the given interface. The return value is taken from the OEPageOrientation namespace.

*itf* The interface in which the parameter is configured.

*name* The name of the parameter.

See also:

· OEConfigureMultiPageOrientation function

## 4.3.72 OEGetMultiPageSize

```
unsigned int OEGetMultiPageSize (const OESystem:: OEInterface &itf,
                                 std::string name=OEMultiPageParamName::PageSize)
```

Returns the page orientation initialized in the given interface. The return value is taken from the  $OEPageSize$ namespace.

*itf* The interface in which the parameter is configured.

*name* The name of the parameter.

#### See also:

· OEConfigureMultiPageSizefunction

## 4.3.73 OEGetNearbyAtom

```
OENearestAtom OEGetNearbyAtom (const OE2DMolDisplay &disp, const OE2DPoint &point,
                              double radiusscale=1.0)
```

Returns an OENearestAtom object that stores a pointer of the atom which is depicted nearest to a given 2D display coordinates. By default, only atoms that are no further than half bond away from the given point will be considered.

disp The OE2DMolDisplay object of which atoms are being considered. Only atoms of which atom display is visible are examined (OEAtomDisplayBase. IsVisible)

*point* Specifies the 2D display coordinates.

*radiusscale* The multiplier that can be used to increase or to decrease the radius around the given point to be considered. This value has to be in a range of  $[0.25, 2.0]$ .

Note: If there is no atom close to the given display coordinates, then the OENearestAtom. IsValid method returns false.

#### See also:

- OENearestAtom class
- · OEGetNearestAtom function
- · OEGetNearbyBond function

## 4.3.74 OEGetNearbyBond

OENearestBond OEGetNearbyBond(const OE2DMolDisplay &disp, const OE2DPoint &point, double radiusscale=1.0)

Returns an OENearestAtom object that stores a pointer of the bond which is depicted nearest to a given 2D display coordinates. By default, only bonds that are no further than half bond away from the given point will be considered.

disp The OE2DMolDisplay object of which bonds are being considered. Only bonds of which bond display is visible are examined (OEBondDisplayBase. IsVisible)

*point* Specifies the 2D display coordinates.

*radiusscale* The multiplier that can be used to increase or to decrease the radius around the given point to be considered. This value has to be in a range of  $[0.25, 2.0]$ .

**Note:** If there is no bond close to the given display coordinates, then the OENearest Bond. IsValid method returns false.

#### See also:

• OENearestBond class

- · OEGetNearestBond function
- OEGetNearbyAtom function

## 4.3.75 OEGetNearestAtom

OENearestAtom OEGetNearestAtom (const OE2DMolDisplay &disp, const OE2DPoint &point)

Returns an OENearestAtom object that stores a pointer of the atom which is depicted nearest to a given 2D display coordinates.

![](_page_550_Figure_6.jpeg)

### Fig. 353: Example of using the OEGetNearestAtom function to determine the nearest atom to a specific 2D point on the canvas

disp The OE2DMolDisplay object of which atoms are being considered. Only atoms of which atom display is visible are examined (OEAtomDisplayBase. IsVisible)

*point* Specifies the 2D display coordinates.

#### See also:

- OENearestAtom class
- · OEGetNearbyAtom function

## 4.3.76 OEGetNearestBond

OENearestBond OEGetNearestBond (const OE2DMolDisplay &disp, const OE2DPoint &point)

Returns an OENearestBond object that stores a pointer of the bond which is depicted nearest to a given 2D display coordinates.

disp The OE2DMolDisplay object of which bonds are being considered. Only bonds of which bond display is visible are examined (OEBondDisplayBase. IsVisible)

*point* Specifies the 2D display coordinates.

- OENearestBond class
- · OEGetNearbyBond function

![](_page_551_Figure_1.jpeg)

Fig. 354: Example of using the OEGetNearestBond function to determine the nearest bond to a specific 2D point on the canvas

## 4.3.77 OEGetPageHeight

double OEGetPageHeight (unsigned int size)

Returns the page height for the given size.

size This value has to be from the  $OEPageSize$  namespace.

#### See also:

- OEPageSize namespace
- · OEGetPageWidth function

## 4.3.78 OEGetPageWidth

double OEGetPageWidth (unsigned int size)

Returns the page width for the given size.

size This value has to be from the  $OEPageSize$  namespace.

See also:

- OEPageSize namespace
- · OEGetPageHeight function

## 4.3.79 OEGetSupportedImageFileExtensions

OESystem::OEIterBase<std::string> \*OEGetSupportedImageFileExtensions()

Returns an iterator over the file extensions of the supported image file formats.

| <b>Graphics File Format</b>            | <b>File Extension</b> |
|----------------------------------------|-----------------------|
| <b>PNG</b> (Portable Network Graphics) | .png                  |
| SVG (Scalable Vector Graphics)         | .svg                  |
| <i>bare SVG</i> (with no header)       | .bsvg                 |
| Postscript                             | .ps                   |
| Encapsulated PostScript                | .eps                  |
| PDF (Portable Document Format)         | .pdf                  |

## 4.3.80 OEGetSupportedMultiPageImageFileExtensions

OESystem::OEIterBase<std::string> \*OEGetSupportedMultiPageImageFileExtensions()

Returns an iterator over the file extensions of the supported multi-page image file formats.

| Multi-page Image File Format   | File Extension |
|--------------------------------|----------------|
| Postscript                     | .ps            |
| PDF (Portable Document Format) | .pdf           |

## 4.3.81 OEHasDepictionHydrogens

**bool** OEHasDepictionHydrogens (const OEChem:: OEAtomBase \*)

Determines whether the specified heavy atom has a "depiction" hydrogen. Depiction hydrogens are hydrogens that need to be explicitly drawn in a 2D depiction to faithfully represent tetrahedral atom stereochemistry or cis/trans bond stereochemistry.

### Table 50: Example of molecules with "depiction" hydrogen(s)

![](_page_552_Figure_10.jpeg)

See also:

· OEAddDepictionHydrogens function

## 4.3.82 OEIsRegisteredImageFile

**bool** OEIsReqisteredImageFile(const std::string &ext)

Returns whether or not an image file format is registered *(i.e.* supported) with the given extension. The following snippet of code demonstrates how to check whether a file name is a supported file format.

```
filename = sys.argv[1]ext = oechem.OEGetFileExtension(filename)
if not oedepict. OEIsRegisteredImageFile(ext):
    oechem. OEThrow. Fatal ("Unknown image type!")
```

## 4.3.83 OEIsRegisteredMultiPageImageFile

bool OEIsRegisteredMultiPageImageFile(const std::string &ext)

Returns whether or not a multi-page image file format is registered (*i.e.* supported) with the given extension.

## 4.3.84 OEIsValidSVGClassName

**bool** OEIsValidSVGClassName (const std::string &name)

Returns whether the given string can be used as an SVG class name.

The rules of **valid** SVG classes names (OESVGClass) in **OEDepict TK** are:

- It must start with an alphabetic character.
- It must not contain any space characters.
- It may contain any alphanumeric characters,  $-$  (hyphen) and  $-$  (underscore).
- The size of the SVG class name should not exceed 64 characters.

**Note:** SVG class names starting with oedepict are reserved by **OEDepict TK** for internal usage.

## 4.3.85 OEIsValidSVGGroupId

**bool** OEIsValidSVGGroupId(const std::string &id)

Returns whether the given string can be used as an SVG group identifier.

The rules of valid SVG group ids (OESVGClass) in OEDepict TK are:

- It must start with an alphabetic character.
- It must not contain any space characters.
- It may contain alphanumeric character and (hyphen), \_ (underscore), ; (semi-colon) or . (period).
- The size of the SVG group id should not exceed 64 characters.

Note: The group id must be unique amongst all the ids in the document. This condition is not checked by the OEIsValidSVGGroupId function.

## 4.3.86 OELengthenVector

OE2DPoint OELengthenVector (const OE2DPoint &vect, double length)

Lengthen the given vector.

## See also:

- OE2DPoint class
- · OERotateVector function

## 4.3.87 OEOffsetMolDisplay

```
void OEOffsetMolDisplay (OE2DMolDisplay &disp, const OE2DPoint &offset)
void OEOffsetMolDisplay (OE2DMolDisplay &disp, const OE2DMolDisplay &refdisp)
```

When an OE2DMolDisplay object is created, the depicted molecule is positioned in the middle of the canvas. The OEOffsetMolDisplay function can be used to translate the depicted molecule either by specifying an offset vector or another OE2DMolDisplay object that is used as a reference that defines the translation.

![](_page_554_Figure_11.jpeg)

Fig. 355: Example of translating the depiction of a molecule by using offset vector (red arrows)

## 4.3.88 OEPrepareAlignedDepiction

| Link                                                                                      | Description                                                                    |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| <i>OEPrepareAlignedDepic-<br/>tion(fitmol, refmol, match, clearcoords,<br/>suppressH)</i> | aligns a molecule to the reference                                             |
| <i>OEPrepareAlignedDepic-<br/>tion(fitmol, refmol, match, opts)</i>                       | aligns a molecule to the reference according to options                        |
| <i>OEPrepareAlignedDepic-<br/>tion(fitmol, mcss, opts)</i>                                | aligns a molecule to the reference based on maximum common substructure search |
| <i>OEPrepareAlignedDepic-<br/>tion(fitmol, subsrc, opts)</i>                              | aligns a molecule to the reference based on substructure search                |
| <i>OEPrepareAlignedDepic-<br/>tion(fitmol, refmol, matches, opts)</i>                     | aligns a molecule to the reference based on matches                            |

Table 51: The overloaded versions of the OEPrepareAlignedDepiction function

```
bool OEPrepareAlignedDepiction (OEChem:: OEMolBase &fitmol,
                                const OEChem:: OEMolBase & refmol,
                                const OEChem:: OEMatchBase &match,
                                bool clearCoords=true, bool suppressH=true)
```

Generates the 2D coordinates of a molecule by maximizing its overlap with a reference 2D molecule based on the given match between the two molecules.

*fitmol* The molecule being fitted to be aligned to the reference molecule.

refmol The reference molecule of which 2D coordinates are remain unchanged.

- *match* The match determines the atoms of the *fitmol* that will be aligned to the atoms of the *refmol*. The match can be generated by hand, or with any of **OEChem TK**'s matching algorithms such as OESubSearch or OEMC-SSearch.
- clearcoords If true, than the 2D coordinates of the fitted molecule are re-calculated by calling the OEP repareDepiction function. After generating the coordinates, the alignment between the two molecules is maximized by rotating the single bonds of the fitted molecule while avoiding atom clashes. See example (C) in Figure: Example of the molecule alignment.

If clearcoords is false and the fitmol has 2D coordinates than these coordinates are kept. In this case only 2D rotation and translation of the fitted molecule is allowed (i.e. no rotations around bonds) in order to align it to the reference molecule. See example (B) in Figure: Example of the molecule alignment.

suppressH If true, than explicit hydrogens are suppressed in the input molecule by calling the OESuppressNonDepictionHydrogens function.

See also:

• Molecule Alignment chapter

```
bool OEPrepareAlignedDepiction (OEChem:: OEMolBase &fitmol,
                                const OEChem:: OEMolBase & refmol,
                                const OEChem:: OEMatchBase &match,
                                const OEAlignmentOptions &opts)
```

Generates the 2D coordinates of a molecule by maximizing its overlap with a reference 2D molecule based on the given match between the two molecules.

![](_page_556_Figure_1.jpeg)

Fig. 356: Example of the molecule alignment

(A) molecule with no alignment; (B) aligning the fit molecule to the reference molecule by allowing only 2D rotations (original coordinates are kept); (C) aligning the fit molecule to the reference by allowing rotation around single bonds (coordinates are regenerate)

*fitmol* The molecule being fitted to be aligned to the reference molecule.

refmol The reference molecule of which 2D coordinates are remain unchanged.

*match* The match determines the atoms of the *fitmol* that will be aligned to the atoms of the *refmol*. The match can be generated by hand, or with any of OEChem TK's matching algorithms such as OESubSearch or OEMC-SSearch.

opts The OEAlignmentOptions object that stores properties that influence how the molecule alignment is performed.

#### See also:

• Molecule Alignment chapter

```
OEAlignmentResult OEPrepareAlignedDepiction (OEChem:: OEMolBase &fitmol,
                                                 const OEChem:: OEMCSSearch & mcss,
                                                 const OEAlignmentOptions &
\rightarrow opts=OEAlignmentOptions())
```

Generates the 2D coordinates of a molecule by maximizing its overlap based on the maximum common substructure initialized with a reference 2D molecule.

fitmol The molecule being fitted to be aligned to the reference molecule.

mcss The OEMCSSearch object stores the reference molecule. The molecule alignments are performed based on the

maximum common substructure(s) detected between the fit and the reference molecule.

**opts** The OEAlignmentOptions object that stores properties that influence how the molecule alignment is performed.

**Warning:** The reference molecule has to have 2D coordinates prior to initializing the OEMCSSearch object.

#### See also:

- OEMCSSearch class in the **OEChem TK** manual
- Listing 1 example code in Molecule Alignment chapter

```
OEAlignmentResult OEPrepareAlignedDepiction (OEChem:: OEMolBase &fitmol,
                                                const OEChem:: OESubSearch & subsrc,
                                                const OEAlignmentOptions &
\rightarrow opts=0EAlignmentOptions())
```

Generates the 2D coordinates of a molecule by maximizing its overlap based on substructure search initialized with a reference 2D molecule.

In case of a successful alignment, the returned OEAlignmentResult object stores the match between fit and reference molecules.

*fitmol* The molecule being fitted to be aligned to the reference molecule.

- subsrc The OESubSearch object stores the reference molecule. The molecule alignments are performed based on the substructure(s) detected between the fit and the reference molecule.
- **opts** The OEAlignmentOptions object that stores properties that influence how the molecule alignment is performed.

**Warning:** The reference molecule has to have 2D coordinates prior to initializing the OESubSearch object.

#### See also:

- OESubSearch class in the **OEChem TK** manual
- Listing 2 code example in Molecule Alignment chapter

```
OEAlignmentResult OEPrepareAlignedDepiction (OEChem:: OEMolBase &fitmol,
                             const OEChem:: OEMolBase &refmol,
                             OESystem:: OEIter<const OEChem:: OEMatchBase> &miter,
                             const OEAlignmentOptions &opts=OEAlignmentOptions())
OEAlignmentResult OEPrepareAlignedDepiction (OEChem::OEMolBase &fitmol,
                             const OEChem:: OEMolBase & refmol,
                             OESystem:: OEIterBase<const OEChem:: OEMatchBase> *miter,
                             const OEAlignmentOptions &opts=OEAlignmentOptions())
```

Generates the 2D coordinates of a molecule by maximizing its overlap with a reference 2D molecule based on the given matches between the two molecules.

fitmol The molecule being fitted to be aligned to the reference molecule.

*refmol* The reference molecule of which 2D coordinates are remain unchanged.

*miter* The iterator that stores the matches on which the molecule alignment is based on.

opts The OEAlignmentOptions object that stores properties that influence how the molecule alignment is performed.

## • Molecule Alignment chapter

# 4.3.89 OEPrepareDepiction

tion

## Table 52: The overloaded versions of the OEPrepareDepiction func-

| Link                                                         | Description                            |
|--------------------------------------------------------------|----------------------------------------|
| <i>OEPrepareDepiction(mol, clearc-<br/>cords, suppressH)</i> | prepare depiction                      |
| <i>OEPrepareDepiction(mol, opts)</i>                         | prepare depiction according to options |

bool OEPrepareDepiction (OEChem:: OEMolBase &mol, bool clearcoords=false, **bool** suppressH=true)

Prepares a molecule before depiction that involves suppressing or adding explicit hydrogens, perceiving atom and bond stereo information and calculating 2D coordinates.

*mol* The molecule being manipulated.

*clearcoords* If true, than the 2D coordinates of the molecule are re-calculated. If false and the molecule has 2D coordinates than these coordinates are kept.

If the molecule has no 2D coordinates, then the 2D coordinates are always generated by calling the OEDepictCoordinates function regardless of the value of the clearcoords parameter.

suppressH If true, than explicit hydrogens are suppressed in the input molecule by calling the OESuppressNonDepictionHydrogens function. See example in Figure: Example of the molecule depictions with kept and suppressed hydrogens.

![](_page_558_Figure_11.jpeg)

Fig. 357: Example of the molecule depictions with kept and suppressed hydrogens

**Note:** The OEP repareDepiction function generates canonical 2D coordinates (when the *clearco*ords parameter is true) i.e. the layout of the same molecules will be identical regardless of their atom and bond orderings.

The following code shows how to generate non-canonical 2D coordinates:

```
def PrepareDepiction(mol, clearcoords=False, suppressH=True):
   oechem.OESetDimensionFromCoords(mol)
   oechem.OEPerceiveChiral(mol)
   if mol. GetDimension() != 2 or clearcoords:
        if mol. <math>GetDimension()</math> == 3:oechem.OE3DToBondStereo(mol)
            oechem.OE3DToAtomStereo(mol)
        if suppressH:
            oechem.OESuppressHydrogens(mol)
        oechem.OEAddDepictionHydrogens(mol)
        oechem.OEDepictCoordinates(mol)
        oechem.OEMDLPerceiveBondStereo(mol)
   mol.SetDimension(2)
    return True
```

#### See also:

- · OEAddDepictionHydrogens function
- OEDepictCoordinates function

bool OEPrepareDepiction (OEChem:: OEMolBase & mol, const →OEPrepareDepictionOptions& opts)

Prepares a molecule before depiction.

*mol* The molecule being manipulated.

**opts** The OEPrepareDepictionOptions object that stores properties that influence how the molecule is prepared.

## 4.3.90 OEPrepareMultiAlignedDepiction

```
bool OEPrepareMultiAlignedDepiction (OEChem:: OEMolBase &fitmol,
                             const OEChem:: OEMolBase &refmol,
                             OESystem:: OEIter<const OEChem:: OEMatchBase> &miter)
bool OEPrepareMultiAlignedDepiction (OEChem:: OEMolBase &fitmol,
                             const OEChem:: OEMolBase & refmol,
                             OESystem:: OEIterBase<const OEChem:: OEMatchBase> *miter)
```

Generates the 2D coordinates of a molecule by maximizing its overlay with a reference 2D molecule based on multiple overlaps between the two molecules.

fitmol The molecule being fitted to be aligned to the reference molecule.

*refmol* The reference molecule of which 2D coordinates are remain unchanged.

*miter* The iterator that stores the matches on which the molecule alignment is based on.

Hint: The overlap between two molecules can be generated by the OEGetFPOverlap function of GraphSim TK. The OEGetFPOverlap returns matched fragments of two molecules that are considered equivalent based on a specific fingerprint type.

![](_page_560_Figure_1.jpeg)

#### Fig. 358: Example of the molecule alignment based on multiple fragments

(left) - depiction of a reference molecule (middle) - default depiction of a fit molecule (right) - depiction of the fit molecule aligned to the reference based on multiple fragments

![](_page_560_Figure_4.jpeg)

The Python script that visualizes molecule similarity based on fingerprints can be downloaded from the OpenEye Python Cookbook

- Molecule Alignment chapter
- · Fingerprint Overlap chapter in GraphSim TK
- · OEPrepareAlignedDepiction function

• Listing 3 example code in Molecule Alignment chapter

## 4.3.91 OEReduceFontSizeToFit

```
unsigned int OEReduceFontSizeToFit(const std::string &text, const OEFont &font,
                                   unsigned int minfontsize, double maxwidth)
```

The OEReduceFont SizeToFit function gradually reduces the font size until the specified string can be drawn without exceeding the width limit.

text The string for which the font size is calculated.

font The OEFont object that defines the style of the depiction.

*minfontsize* The minimum font size that can be returned.

*maxwidth* The width that can not be exceeded when drawing the string.

#### See also:

- · OEEstimateTextWidth function
- OEFont class

## 4.3.92 OERegisterImageFile

**bool** OERegisterImageFile(const OEImageFileCreatorBase &)

Registers an OEImageFileCreatorBase object that handles a specific image file type.

#### See also:

- OEImageFileCreatorBase class
- · OEIsRegisteredImageFilefunction
- · OEIsRegisteredMultiPageImageFilefunction

## 4.3.93 OERenderMolecule

#### Table 53: The overloaded versions of the OERenderMolecule func-

tion

| Link                                       | Description                                                                      |
|--------------------------------------------|----------------------------------------------------------------------------------|
| <i>OERenderMolecule(image, disp)</i>       | renders a molecule display into an image                                         |
| <i>OERenderMolecule(image, mol)</i>        | renders molecule into an image using the <b>default</b> depiction style          |
| <i>OERenderMolecule(filename, disp)</i>    | writes a molecule display into a file                                            |
| <i>OERenderMolecule(filename, mol)</i>     | writes a molecule into a file using the <b>default</b> depiction style           |
| <i>OERenderMolecule(stream, ext, disp)</i> | writes a molecule display into an output stream                                  |
| <i>OERenderMolecule(stream, ext, mol)</i>  | writes a molecule into an output stream using the <b>default</b> depiction style |

```
bool OERenderMolecule (OEImageBase &image, const OE2DMolDisplay &disp,
                      bool clearbackground=true)
```

Renders the molecule display into an image.

*image* The image in which the molecule is drawn.

disp The OE2DMolDisplay object that holds the data necessary to depict the molecule with which it is initialized.

clearbackground Determines whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the molecule rendering.

**Example:** 

```
oedepict.OEPrepareDepiction(mol)
image = odeplot.OEImage(200.0, 200.0)opts = oedepict.OE2DMolDisplayOptions(image.GetWidth(), image.GetHeight(),
                                      oedepict.OEScale_AutoScale)
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OERenderMolecule(image, disp)
```

See also:

- OEImageBase class
- OE2DMolDisplay class

```
bool OERenderMolecule (OEImageBase &image, const OEChem:: OEMolBase &mol,
                      bool clearbackground=true)
```

Renders a molecule into an image using the **default** depiction style.

*image* The image in which the molecule is drawn.

- **mol** The molecule being rendered has to have valid 2D coordinates before calling the OERenderMolecule function.
- clearbackground Determines whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the molecule rendering.

#### **Example:**

```
oedepict.OEPrepareDepiction(mol)
image = odeplot.OEImage(200.0, 200.0)oedepict.OERenderMolecule(image, mol)
```

#### See also:

• OEImageBase class

```
bool OERenderMolecule (const std:: string & filename, const OE2DMolDisplay & disp,
                       bool clearbackground=true)
```

Writes the molecule display into a file.

- *filename* The name of the file into which the molecule display is being written. The extension of the filename determine the type of the image.
- disp The OE2DMolDisplay object that holds the data necessary to depict the molecule with which it is initialized.

*clearbackground* Determines whether or not the image is cleared (by calling  $OEImageBase$ ,  $Clear$  method) prior to the molecule rendering.

#### **Example:**

```
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(200.0, 200.0, oedepict.OEScale AutoScale)
disp = oedepict.OE2DMolDisplay(mol, opts)
oedepict.OERenderMolecule("OERenderMolecule-fname-disp.pnq", disp)
```

#### See also:

• OE2DMolDisplay class

```
bool OERenderMolecule (const std::string &filename, const OEChem::OEMolBase &mol,
                      bool clearbackground=true)
```

Writes a molecule into a file using the default depiction style.

- *filename* The name of the file into which the molecule is written. The extension of the filename determine the type of the image.
- **mol** The molecule being rendered has to have valid 2D coordinates before calling the OERenderMolecule function.
- *clearbackground* Determines whether or not the image is cleared (by calling  $OEImageBase$ . Clear method) prior to the molecule rendering.

### **Example:**

```
oedepict.OEPrepareDepiction(mol)
```

```
oedepict.OERenderMolecule("OERenderMolecule-fname-mol.png", mol)
```

```
bool OERenderMolecule (OEPlatform::oeostream &os, const std::string &extension,
                      const OE2DMolDisplay &disp, bool clearbackground=true)
```

Writes the molecule display into a stream.

os The stream into which the molecule display is being written.

ext The extension which determine the type of the image.

disp The OE2DMolDisplay object that holds the data necessary to depict the molecule with which it is initialized.

clearbackground Determines whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the molecule rendering.

#### **Example:**

```
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(200.0, 200.0, oedepict.OEScale_AutoScale)
disp = oedepict.OE2DMolDisplay(mol, opts)
ofs = oechem.oeofstream("OERenderMolecule-stream-disp.png")
oedepict.OERenderMolecule(ofs, "pnq", disp)
```

#### See also:

• oeostream class in the **OEChem TK** manual

• OE2DMolDisplay class

```
bool OERenderMolecule (OEPlatform:: oeostream &os, const std:: string &extension,
                       const OEChem:: OEMolBase & mol, bool clearbackground=true)
```

Writes a molecule into a stream using the **default** depiction style.

- os The stream into which the molecule is being written.
- ext The extension which determine the type of the image.
- **mol** The molecule being rendered has to have valid 2D coordinates before calling the OERenderMolecule function.
- **clearbackground** Determines whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the molecule rendering.

**Example:** 

```
oedepict.OEPrepareDepiction(mol)
ofs = oechem.oeofstream("OERenderMolecule-stream-mol.pnq")
oedepict.OERenderMolecule(ofs, "pnq", mol)
```

See also:

• oeostream class in the **OEChem TK** manual

## 4.3.94 OERenderMoleculeToBytes

```
OERenderMoleculeToBytes(ext: str, disp: OE2DMolDisplay, clearbackground: bool = True)
\leftrightarrow \rightarrow bytes
OERenderMoleculeToBytes(ext: str, mol: OEMolBase, clearbackground: bool = True) \rightarrow\rightarrowbytes
```

Same as the OERenderMoleculeToString function.

## 4.3.95 OERenderMoleculeToString

#### Table 54: The overloaded versions of the OERenderMolecule-**ToString function**

| Link                                       | Description                                                                           |
|--------------------------------------------|---------------------------------------------------------------------------------------|
| <i>OERenderMoleculeToString(ext, disp)</i> | writes a molecule display into a string (byte array)                                  |
| <i>OERenderMoleculeToString(ext, mol)</i>  | writes a molecule into a string (byte array) using the <b>default</b> depiction style |

```
std::string OERenderMoleculeToString (const std::string &ext,
                                      const OE2DMolDisplay &disp,
                                     bool clearbackground=true)
```

Writes a molecule display into a string.

ext The extension which determine the type of the image.

- **disp** The OE2DMolDisplay object that holds the data necessary to depict the molecule with which it is initialized.
- **clearbackground** Determines whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the molecule rendering.

#### See also:

· OEIsRegisteredImageFilefunction

```
std::string OERenderMoleculeToString(const std::string &ext,
                                      const OEChem:: OEMolBase &mol,
                                     bool clearbackground=true)
```

Writes a molecule into a string using the **default** depiction style.

ext The extension which determine the type of the image.

*mol* The molecule being rendered.

*clearbackground* Determines whether or not the image is cleared (by calling  $OEImageBase$ ,  $Clear$ method) prior to the molecule rendering.

#### **Example:**

```
mol = occhem.OEGraphMol()oechem.OESmilesToMol(mol, "clcccccl")
oedepict.OEPrepareDepiction(mol)
data = oedepict.OERenderMoleculeToString("svg", mol)
```

Note: In Python 3 the OERenderMoleculeToString function returns bytes.

#### See also:

- · OEIsRegisteredImageFilefunction
- · OERenderMoleculeToBytes function

## 4.3.96 OERotateVector

OE2DPoint OERotateVector (const OE2DPoint &vect, double degree)

Rotates the vector with the given degree.

- OE2DPoint class
- · OELengthenVector function

## 4.3.97 OESetup2DMolDisplayOptions

```
bool OESetup2DMolDisplayOptions (OE2DMolDisplayOptions &opts,
                                 const OESystem:: OEInterface &itf)
```

Initializes an OE2DMolDisplayOptions object from the parameters of a given interface.

### See also:

- OE2DMolDisplayOptions class
- OEConfigure2DMolDisplayOptionsfunction

## 4.3.98 OESetupPrepareDepictionOptions

```
bool OESetupPrepareDepictionOptions (OEPrepareDepictionOptions& opts,
                                     const OESystem:: OEInterface & itf)
```

Initializes an OEPrepareDepictionOptions object from the parameters of a given interface.

#### See also:

- OEPrepareDepictionOptions class
- · OEConfigurePrepareDepictionOptionsfunction

## 4.3.99 OESetupReportOptions

```
bool OESetupReportOptions (OEReportOptions &opts,
                           const OESystem:: OEInterface &itf)
```

Initializes an OEReportOptions object from the parameters of a given interface.

### See also:

- OEReportOptions class
- · OEConfigureReportOptionsfunction

## 4.3.100 OESuppressNonDepictionHydrogens

bool OESuppressNonDepictionHydrogens (OEChem:: OEMolBase& mol)

The OESuppressNonDepictionHydrogens function suppresses all non-essential hydrogens of the molecule. Only the following hydrogens will be kept:

- hydrogens with (non-zero) isotopic mass
- hydrogens that are necessary to faithfully represent tetrahedral atom stereochemistry or cis/trans bond stereochemistry (defined by the OEHasDepictionHydrogens function).

![](_page_567_Figure_1.jpeg)

See also:

• OEHasDepictionHydrogens function

## 4.3.101 OEWrite2DRingDictionaryReport

```
bool OEWrite2DRingDictionaryReport (const std::string &filename,
                                    const OEChem:: OE2DRingDictionary &ringdict,
                                    const OEReportOptions &opts)
bool OEWrite2DRingDictionaryReport (OEPlatform::oeostream &os,
                                    const std:: string & extension,
                                    const OEChem:: OE2DRingDictionary &ringdict,
                                    const OEReportOptions &opts)
```

Writes a report of the 2D ring layouts stored in the given ring dictionary. See example in Table Example of ring dictionary report.

- *filename* The filename into which the report is written. The file extension determines the type of the multi-page image.
- os The stream into which the report is written.

ext The extension which determine the type of the multi-page report.

ringdict The OE2DRingDictionary object that stores ring 2D layouts that can be used to plug into the 2D coordinate generation system.

**opts** The OEReportOptions object that determines the layout of the pages of the report.

The report depicts each ring systems stored in the ring dictionary.

- The string at the top is the canonical isomeric SMILES that is used as the identifier for the given ring system.
- The larger depiction on the left shows the user-defined layout of the ring system
- The smaller depiction on the right illustrates the default layout of the ring system *i.e.* when the 2D coordinates are generated by OEChem TK without utilizing the given user-defined ring dictionary.
  - The blue box indicates that OEChem  $TK$  has already have a built-in layout for the given ring system.
  - The pink box indicates that the layout of that ring system would be generated on the fly by default without utilizing any built-in templates.
- There are cases when cis/trans bonds are marked on the macro-cycles depicted inside the blue/pink boxes. These annotations indicate potential depiction problem in OEChem TK.

| cover page                                                          | page 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | page 2                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <b>2D Ring Dictionary Report</b><br>Ring Dictionary Version : 1.0.0 | <span style="color:blue;">▭</span> OEChem built‑in <span style="color:red;">▭</span> OEChem generated<br><br>C1C/C=C/CCCC2CC2C1 — Image: bicyclic ring drawing<br>C1C2C3C4C2C5C1C3C5C4 — Image: cage-like ring drawing<br>C1CC23CCC2C=C/C=C/C1C3 — Image: macrocyclic ring drawing<br>C1CC/C=C/C/C=C/CC1 — Image: cyclodecadiene ring drawing<br>C1CC2CC/C=C/CCC3CC3C2C1 — Image: fused bicyclic ring drawing<br>C1CC2CC3CC4CCCC4C3CC2C1 — Image: polycyclic ring drawing | <span style="color:blue;">▭</span> OEChem built‑in <span style="color:red;">▭</span> OEChem generated<br><br>C1CC2CC3CCC4C3C24C1 — Image: bicyclic ring drawing<br>C1CCC/C=C/C/C=C/CC1 — Image: cyclooctadiene ring drawing<br>C1CCC2CCC23CCC(C1)C3 — Image: tricyclic ring drawing<br>C1CCCC2CC2C3CCCC3CC1 — Image: fused polycyclic ring drawing<br>C1CCCCC2CC2CCC1 — Image: bridged bicyclic ring drawing<br>C1CCCCCCCCC1 — Image: decalin-like ring drawing |

#### Table 55: Example of ring dictionary report (The pages are reduced here for visualization convenience)

#### See also:

- OE2DRingDictionary class
- · OEAnnotateDepictionProblems function
- 2D coordinate generation examples section of the OEChem TK manual that shows examples about how to generate and utilize user-defined ring dictionaries.

## 4.3.102 OEWriteImage

|  |  |  |  | Table 56: The overloaded versions of the OEWriteImage function |  |
|--|--|--|--|----------------------------------------------------------------|--|
|--|--|--|--|----------------------------------------------------------------|--|

| Link                                    | Description                     |
|-----------------------------------------|---------------------------------|
| <i>OEWriteImage(filename, image)</i>    | writes image into file          |
| <i>OEWriteImage(stream, ext, image)</i> | writes image into output stream |

bool OEWriteImage(const std::string &filename, const OEImage &image)

Writes the image into a file with the given name.

*filename* The name of the file into which the image is written. The extension of the filename determine the type of the image.

image The OEImage object which is being written into the given file.

#### See also:

• OEIsRegisteredImageFilefunction

```
bool OEWriteImage(OEPlatform::oeostream &os, const std::string &ext,
                  const OEImage & image)
```

Writes the image into the given output stream.

os The stream into which the image is written.

ext The extension which determine the type of the image.

*image* The *OEImage* object which is being written into the stream.

See also:

· OEIsRegisteredImageFilefunction

## 4.3.103 OEWriteImageToBytes

OEWriteImageToBytes(ext: str, image: OEImage) -> bytes

Same as the OEWriteImageToString function.

## 4.3.104 OEWriteImageToString

```
std::string OEWriteImageToString(const std::string &ext,
                                  const OEImage & image)
```

Writes the image into a string.

ext The extension which determine the type of the image.

*image* The OEImage object which is being written into the string.

#### **Example:**

```
mol = occhem.OEGraphMol()oechem.OESmilesToMol(mol, "clcccccl")
oedepict.OEPrepareDepiction(mol)
image = odeplot.OEImage (200, 200)oedepict.OERenderMolecule(image, mol)
data = oedepict.OEWriteImageToString("svg", image)
```

Note: In Python 3 the OEWriteImageToString function returns bytes.

#### See also:

- · OEIsRegisteredImageFilefunction
- · OEWriteImageToBytesfunction

## 4.3.105 OEWriteMultiPageImage

```
bool OEWriteMultiPageImage(const std::string &filename,
                           const OEMultiPageImageFile &image)
```

Writes the multi-page image into a file with the given name.

*filename* The name of the file into which the image is written. The extension of the filename determine the type of the image.

*image* The OEMultiPageImageFile object which is being written into the given file.

· OEIsRegisteredMultiPageImageFilefunction

```
bool OEWriteMultiPageImage(OEPlatform::oeostream &os,
                            const std:: string & extension,
                            const OEMultiPageImageFile &image)
```

Writes the multi-page image into the given output stream.

os The stream into which the multi-page image is written.

ext The extension which determine the type of the image.

*image* The OEMultiPageImageFile object which is being written into the stream.

#### See also:

· OEIsRegisteredMultiPageImageFilefunction

## 4.3.106 OEWriteReport

#### Table 57: The overloaded versions of the OEWriteReport function

| Link                                      | Description                      |
|-------------------------------------------|----------------------------------|
| <i>OEWriteReport(filename, report)</i>    | writes report into file          |
| <i>OEWriteReport(stream, ext, report)</i> | writes report into output stream |

```
bool OEWriteReport (const std:: string & filename,
                    const OEReport & report, unsigned int pagenum = 0)
```

Writes page(s) of the report into a file with the given name.

- *filename* The filename into which the page(s) of the report are written. The file extension determines the type of the multi-page image.
- **report** The OEReport object of which page(s) is/are being written into the given file.

*pageidx* This value has to be in the range from  $\theta$  to OEReport. NumPages ().

**Note:** If pageidx is a valid page number *i.e* in the range from *l* to OEReport. NumPages (), then only the *paqeidx*<sup>th</sup> page of the report is written into the file. If *paqeidx* is zero and the file extension is recognized as a multi-page format, than all pages of the report are written into the file.

## See also:

- · OEIsRegisteredImageFilefunction
- · OEIsRegisteredMultiPageImageFilefunction

```
bool OEWriteReport (OEPlatform:: oeostream &os,
                    const std:: string &ext,
                    const OEReport & report, unsigned int page=0)
```

Writes  $page(s)$  of the report into the given stream.

 $\boldsymbol{\omega}$  os The stream into which the page(s) of the report are written.

ext The extension which determine the type of the image.

**report** The OEReport object of which page(s) is/are being written into the given file.

**pageidx** This value has to be in the range from 0 to OEReport, NumPages ().

**Note:** If pageidx is a valid page number *i.e* in the range from 1 to OEReport. NumPages (), then only the *pageidx<sup>th</sup>* page of the report is written into the stream. If *pageidx* is zero and the file extension is recognized as a multi-page format, than all pages of the report are written into the stream.

#### See also:

- · OEIsRegisteredImageFilefunction
- · OEIsRegisteredMultiPageImageFilefunction
- OEWriteReportPageByPage function

## 4.3.107 OEWriteReportPageByPage

```
bool OEWriteReportPageByPage(const std::string &filename,
                             const OEReport & report)
```

A convenient function that writes pages of the report into the separate numbered files.

*filename* The filename that serves as a prefix to write the report page by page. For example, if filename test. svg is given, the pages of the report will be written page by page into files:  $test-01$ . svg,  $test-02$ . svg... The extension of file determines the type of the image.

**report** The OEReport object of which pages are being written into the separate files.

#### See also:

- · OEIsRegisteredImageFilefunction
- · OEIsRegisteredMultiPageImageFilefunction
- OEWriteReport function

## 4.3.108 OEWriteReportToBytes

OEWriteReportToBytes(ext: str, report: OEReport) -> bytes

Same as the OEWriteReportToString function.

## 4.3.109 OEWriteReportToString

```
std::string OEWriteReportToString(const std::string &ext,
                                  const OEReport & report, unsigned int page=0)
```

Writes the report into a string.

ext The extension which determine the type of the image.

**report** The OEReport object of which page(s) is/are being written into the string.

**pageidx** This value has to be in the range from 0 to  $OEReport$ . NumPages ().

**Note:** If pageidx is a valid page number *i.e* in the range from *I* to OEReport. NumPages (), then only the pageid $x^{th}$  page of the report is written into the string. If pageidx is zero and the file extension is recognized as a multi-page format, than all pages of the report are written into the string.

### **Example:**

```
mol = oechem.OEGraphMol()
oechem.OESmilesToMol(mol, "clccccc1")
oedepict.OEPrepareDepiction(mol)
report = oedepict. OEReport (3, 1)oedepict.OERenderMolecule(report.NewCell(), mol)
data = oedepict.OEWriteReportToString("pdf", report)
```

Note: In Python 3 the OEWriteReportToString function returns bytes.

- · OEIsRegisteredMultiPageImageFilefunction
- · OEWriteReportToBytesfunction

# **FIVE**

# **APPENDICES**

# 5.1 Appendix: Element coloring (CPK)

The following two images show the default colors associated with various elements when using the OEAtomColorStyle\_WhiteCPK style.

| <Periodic Table> |          |          |           |           |           |           |           |           |          |          |          |          |          |          |          |          |          |
|------------------|----------|----------|-----------|-----------|-----------|-----------|-----------|-----------|----------|----------|----------|----------|----------|----------|----------|----------|----------|
| 1<br>H           |          |          |           |           |           |           |           |           |          |          |          |          |          |          |          |          | 2<br>He  |
| 3<br>Li          | 4<br>Be  |          |           |           |           |           |           |           |          | 5<br>B   | 6<br>C   | 7<br>N   | 8<br>O   | 9<br>F   | 10<br>Ne |          |          |
| 11<br>Na         | 12<br>Mg |          |           |           |           |           |           |           |          | 13<br>Al | 14<br>Si | 15<br>P  | 16<br>S  | 17<br>Cl | 18<br>Ar |          |          |
| 19<br>K          | 20<br>Ca | 21<br>Sc | 22<br>Ti  | 23<br>V   | 24<br>Cr  | 25<br>Mn  | 26<br>Fe  | 27<br>Co  | 28<br>Ni | 29<br>Cu | 30<br>Zn | 31<br>Ga | 32<br>Ge | 33<br>As | 34<br>Se | 35<br>Br | 36<br>Kr |
| 37<br>Rb         | 38<br>Sr | 39<br>Y  | 40<br>Zr  | 41<br>Nb  | 42<br>Mo  | 43<br>Tc  | 44<br>Ru  | 45<br>Rh  | 46<br>Pd | 47<br>Ag | 48<br>Cd | 49<br>In | 50<br>Sn | 51<br>Sb | 52<br>Te | 53<br>I  | 54<br>Xe |
| 55<br>Cs         | 56<br>Ba |          | 72<br>Hf  | 73<br>Ta  | 74<br>W   | 75<br>Re  | 76<br>Os  | 77<br>Ir  | 78<br>Pt | 79<br>Au | 80<br>Hg | 81<br>Tl | 82<br>Pb | 83<br>Bi | 84<br>Po | 85<br>At | 86<br>Rn |
| 87<br>Fr         | 88<br>Ra |          | 104<br>Rf | 105<br>Db | 106<br>Sg | 107<br>Bh | 108<br>Hs | 109<br>Mt |          |          |          |          |          |          |          |          |          |

| 57<br>La | 58<br>Cе | 59<br>D, | 60<br>1d | 61        | 62<br>Sm | 63<br>Eu   | 64<br>Gd | 65       | 66       | 67 | 68<br>ы | 69<br>ı m | 70                |     |
|----------|----------|----------|----------|-----------|----------|------------|----------|----------|----------|----|---------|-----------|-------------------|-----|
| 89<br>Ac | 90       | 91<br>⊃∼ | 92       | 93<br>NIJ | 94<br>Pu | 95<br>AIII | 96<br>Сm | 97<br>Bk | 98<br>Сf | 99 | 100     | 101<br>Md | 102<br><b>INU</b> | 103 |

## Fig. 1: Default CPK colors for white background

The following two images show the default colors associated with various elements when using the OEAtomColorStyle\_BlackCPK style.

![](_page_575_Figure_1.jpeg)

Fig. 2: Example of molecule depiction with default CPK colors in a white background

| $\mathbf{1}$    |                 |                                                                                                                                                                                  |                                                                                                                                                                                         |              |           |                 |           |           |          |                 |          |          |           |           |                 |           | 2               |
|-----------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|-----------|-----------------|-----------|-----------|----------|-----------------|----------|----------|-----------|-----------|-----------------|-----------|-----------------|
| Н               |                 | <periodic table=""></periodic>                                                                                                                                                   |                                                                                                                                                                                         |              |           |                 |           |           |          | He              |          |          |           |           |                 |           |                 |
| 3<br>Li         | 4<br>Be         |                                                                                                                                                                                  |                                                                                                                                                                                         |              |           |                 |           |           |          |                 |          | 5<br>B   | 6<br>C    | Ν         | 8<br>$\Omega$   | 9<br>F    | 10<br><b>Ne</b> |
| 11<br><b>Na</b> | 12<br><b>Mg</b> |                                                                                                                                                                                  |                                                                                                                                                                                         |              |           |                 |           |           |          |                 |          | 13<br>Al | 14<br>Si  | 15<br>P   | 16<br>S         | 17<br>CI  | 18<br>Ar        |
| 19<br>K         | 20<br>Ca        | 21<br>Sc                                                                                                                                                                         | 22<br>Ti                                                                                                                                                                                | 23<br>$\vee$ | 24<br>Cr  | 25<br>Mn        | 26<br>Fe  | 27<br>Co  | 28<br>Ni | 29<br>Cu        | 30<br>Zn | 31<br>Ga | 32<br>Ge  | 33<br>As  | 34<br><b>Se</b> | 35<br>Br  | 36<br>Kr        |
| 37<br><b>Rb</b> | 38<br>Sr        | 39<br>v                                                                                                                                                                          | 52<br>53<br>42<br>47<br>48<br>50<br>51<br>40<br>41<br>43<br>44<br>45<br>46<br>49<br>Zr<br><b>Rh</b><br>Pd<br>Sn<br>Sb<br><b>N<sub>b</sub></b><br>Ru<br>Cd<br>Mo<br>Тc<br>Ag<br>Te<br>In |              |           |                 |           |           |          |                 |          | 54<br>Xe |           |           |                 |           |                 |
| 55<br>Cs        | 56<br><b>Ba</b> |                                                                                                                                                                                  | 72<br>Hf                                                                                                                                                                                | 73<br>Ta     | 74<br>W   | 75<br>Re        | 76<br>Os  | 77<br>1r  | 78<br>Pt | 79<br>Au        | 80<br>Hg | 81<br>т  | 82<br>Pb  | 83<br>Bi  | 84<br>Po        | 85<br>At  | 86<br><b>Rn</b> |
| 87<br>Fr        | 88<br>Ra        |                                                                                                                                                                                  | 104<br>Rf                                                                                                                                                                               | 105<br>Db    | 106<br>Sg | 107<br>Bh       | 108<br>Hs | 109<br>Mt |          |                 |          |          |           |           |                 |           |                 |
|                 |                 |                                                                                                                                                                                  |                                                                                                                                                                                         |              |           |                 |           |           |          |                 |          |          |           |           |                 |           |                 |
|                 |                 | 59<br>62<br>63<br>65<br>66<br>68<br>69<br>70<br>71<br>58<br>60<br>61<br>64<br>67<br>57<br>Ce<br>Eu<br>Gd<br>Yb<br>Nd<br>Sm<br>Tb<br>Dv<br>Ho<br>Er<br>Tm<br>Pr<br>Pm<br>La<br>Lu |                                                                                                                                                                                         |              |           |                 |           |           |          |                 |          |          |           |           |                 |           |                 |
|                 |                 | 89<br>Ac                                                                                                                                                                         | 90<br>Th                                                                                                                                                                                | 91<br>Pa     | 92<br>٥   | 93<br><b>Np</b> | 94<br>Pu  | 95<br>Am  | 96<br>Cm | 97<br><b>Bk</b> | 98<br>Cf | 99<br>Es | 100<br>Fm | 101<br>Md | 102<br>No       | 103<br>Lr |                 |

Fig. 3: Default CPK colors for black background

![](_page_576_Figure_1.jpeg)

Fig. 4: Example of molecule depiction with default CPK colors in a black background

## **SIX**

# **RELEASE HISTORY**

## 6.1 OEDepict TK 2.5.5

Minor internal improvements have been made.

# 6.2 OEDepict TK 2.5.4

Minor internal improvements have been made.

# 6.3 OEDepict TK 2.5.3

Minor internal improvements have been made.

# 6.4 OEDepict TK 2.5.2

Minor internal improvements have been made.

# 6.5 OEDepict TK 2.5.1

Minor internal improvements have been made.

# 6.6 OEDepict TK 2.5.0

• Minor internal improvements have been made.

# 6.7 OEDepict TK 2.4.7

## Fall 2021

• Minor internal improvements have been made.

# 6.8 OEDepict TK 2.4.6

July 2021

Minor internal improvements have been made.

# 6.9 OEDepict TK 2.4.5

**Fall 2020** 

## 6.9.1 New features

- A new function, OEGetLabelPosition, that identifies the position where atoms labels are added.
- Approximately 40 new protective groups have been added to the namespace OEProtectiveGroupStyle.
- A new function, HasProtectiveGroupStyle, has been added that determines whether a given protective group style has been set in OE2DMolDisplayOptions.
- The function GetProtectiveGroupStyle has been deprecated. It can no longer be used to determine if multiple protective group styles from OEProtectiveGroupStyle have been set. HasProtectiveGroupStyle can now be used instead.

## 6.9.2 Minor bug fixes

- An issue that caused OEPrepareAlignedDepiction to generate incorrect stereo depictions when SetClearCoords was set to false has been fixed.
- Figures have been added to show depiction with and without the new protective groups to OEProtectiveGroup-Style.

# **6.10 OEDepict TK 2.4.4**

## 6.10.1 New features

 $\bullet$  Two new methods, OE2DMolDisplayOptions.SetExplicitAtomLabelAngle and OE2DMolDisplayOptions.GetExplicitAtomLabelAngle, have been added that control when explicit "C" labels will be displayed on the molecule graph.

# 6.11 OEDepict TK 2.4.3

## 6.11.1 Minor bug fixes

- The signature of the OECreateWin32GraphicsImage function has been changed to use std::shared\_ptr.
- SVG group IDs and names are now limited to 64 characters.

## 6.11.2 Python-specific changes

• User-defined atom and bond SVG markings are now supported in Python. See the examples in the OEAtomSVG-MarkupBase and OEBondSVGMarkupBase base classes.

# 6.12 OEDepict TK 2.4.2

## 6.12.1 New features

- An option has been added to the molecule alignment process that allows it to accept alignments with a limited number of atom pair clashes in the fixed coordinates mode. See also the OEAlignmentOptions.GetMaxAllowedAtomPairClashes and OEAlignmentOptions. SetMaxAllowedAtomPairClashes methods of the OEAlignmentOptions class.
- In fixed coordinate alignment mode (see the OEAlignment Options. SetFixedCoords method), the order in which single bonds are rotated in order to eliminate atom clashes has been improved.
- A new constructor has been added that allows the OEAlignmentResult class to be initialized from an OEMatch-Base object.

## 6.12.2 Major bug fixes

• A bug in the alignment process that occurred when the number of rotatable bonds of the fit molecule exceeded the built-in limit has been fixed

## 6.12.3 Minor bug fixes

- A minor memory leak in the molecule alignment process has been fixed.
- . On macOS, the deprecated kCTLeftTextAlignment, kCTRightTextAlignment, and kCTCenterTextAlignment Core Graphics constants have been replaced with new APIs. These constants are used to handle text alignment when drawing in PNG images.

## **6.12.4 Documentation changes**

• The example in the Depicting MDL Query Substructure Search Hits section has been revised.

# **6.13 OEDepict TK 2.4.1**

## 6.13.1 New features

- The following APIs have been added to generate consistent legend layouts:
  - OELegendLayoutStyle namespace
  - OELegendColorStyle namespace
  - OELegendInteractiveStyle namespace
  - OELegendLayoutOptions class
  - OELegendLayout class
  - OEDrawLegendLayout function
- The following APIs have been added to depict common protective groups:
  - OEProtectiveGroupStyle namespace
  - OE2DMolDisplayOptions. SetProtectiveGroupLabelFont
  - OE2DMolDisplayOptions.GetProtectiveGroupLabelFont
  - OE2DMolDisplayOptions.SetProtectiveGroupStyle
  - OE2DMolDisplayOptions.GetProtectiveGroupStyle

![](_page_581_Figure_18.jpeg)

- The following APIs have been added to mark up the bonds in SVG images generated by the OERenderMolecule functions:
  - OE2DMolDisplayOptions. SetBondSVGMarkupFunctor
  - OE2DMolDisplayOptions.GetAtomSVGMarkupFunctor
  - OEBondSVGMarkupBase
  - OEBondSVGNoMarkup
  - OEBondSVGBondIdxMarkup

- A new *OEDrawHighlighting* function has been added to render molecule highlights into a separate image rather than into the molecule display.
- New OEAddHighlighting function overloads have been added that take an OESubSearch object and highlight its matches on the molecule display.
- New OEAddWatermark functions have been added that render a light gray watermark onto an image or a molecule display.
- A new OEImageBase. Get SVGGroups method has been added to return the SVG groups associated with the image.
- New OERotateVector and OELengthenVector functions have been added.
- A new OEAddSVGHover function has been added that takes two target SVG groups to create a "hover" effect.

## 6.13.2 Minor bug fixes

- The minimum margin allowed for *OE2DMolDisplayOptions* has been reduced from 5.0% to 2.5%.
- A duplicate SVG group warning is no longer thrown when transferring built-in SVG groups from one image to another.

# **6.14 OEDepict TK 2.4.0**

## 6.14.1 New features

- The following API for marking up SVG images, introduced in the 2017. Jun and 2017. Oct releases, is no longer preliminary. It is now also available in both Java and C#:
  - OESVGClass class
  - OESVGGroup class
  - OEAtomSVGAtomIdxMarkup class
  - OEAtomSVGMarkupBase class
  - OEAtomSVGNoMarkup class
  - OEAtomSVGResidueMarkup class
  - OEAddBuiltInHiddenSVGClassfunction
  - OEAddBuiltInVisibleSVGClassfunction
  - OEAddSVGClickEvent function
  - OEDrawSVGHoverText function
  - OEDrawSVGToggleText function
  - OEGetBuiltInHiddenSVGClassfunction
  - OEGetBuiltInVisibleSVGClass function
- Two new functions, OEIsValidSVGGroupId and OEIsValidSVGClassName, have been added.
- Two new low-level functions, OEAddSVGHover and OEAddSVGToqq1e, have been added to generate hover and toggle effects, respectively, between two SVG groups.
- The OEAtomSVGResidueMarkup class now takes a separator option.

- A new function,  $OEAddLabe1$ , has been added to render a label on an image at a user-defined location.
- Two new functions, OEAddOpenEyeIcon and OEAddInteractiveIcon, and the namespace OEIconLocation have been added.
- Two new methods, OE2DPath. GetStart and OE2DPath. GetEnd, have been added.
- Two new pens, OETransparentPen and OESVGAreaPen, have been added.

## 6.14.2 Java-specific changes

• The API for marking up SVG images is now fully supported in Java (see the list above).

## 6.14.3 C#-specific changes

• The API for marking up SVG images is now fully supported in C# (see the list above).

# **6.15 OEDepict TK 2.3.6**

## 6.15.1 New features

- The following API has been added to increase the reporting capabilities of OEDepict TK:
  - $-$  OEImageTable class
  - OEImageTableOptions class
  - OEImageTableStylenamespace

![](_page_583_Figure_15.jpeg)

Fig. 1: Example of depicting molecules and data using image table

- The following API has been added to render labels associated with certain parts of the depicted molecule:
  - OEHighlightLabel class
  - OEAddLabel function

![](_page_584_Figure_4.jpeg)

#### Fig. 2: Example of adding labels on molecule depiction

- A new function,  $OED$ *rawText*, has been added.
- The constructor of the  $OEHighlightByLasso$  class now takes a parameter that determines the width of the "lasso" used for highlighting. The corresponding GetLineWidthScale and SetLineWidthScale methods have been added.
- A new constructor has been added to the  $OEImageFrame$  class that generates a new image with equal padding around it.
- A new function, OEWriteReportPageByPage, has been added.
- A new constructor has been added to the  $OE2DPath$  class that copies and rotates an already existing path.

## 6.15.2 Preliminary API - New Functionalities

- A new overload of the function  $OEAddSVGClickEvent$  has been added that allows associating any  $OESVG$ Group object with an SVG click event.
- A new Preliminary API has been added to generate and access built-in visibility SVG classes (OESVGClass):
  - OEAddBuiltInHiddenSVGClass
  - OEGetBuiltInHiddenSVGClass
  - OEAddBuiltInVisibleSVGClass
  - OEGetBuiltInVisibleSVGClass
- A new Preliminary API has been added to mark up the atoms in SVG images generated by the OERenderMolecule function:
  - OE2DMolDisplayOptions. SetAtomSVGMarkupFunctor
  - OE2DMolDisplayOptions.GetAtomSVGMarkupFunctor
  - OEAtomSVGMarkupBase
  - OEAtomSVGNoMarkup

- OEAtomSVGAtomIdxMarkup
- OEAtomSVGResidueMarkup
- A new constant, OELayerPosition\_SVG, has been added to the OELayerPosition namespace.
- The following virtual methods have been added to the OEImageFileBase class:
  - OEImageFileBase. PushGroup
  - OEImageFileBase. PopGroup
  - OEImageFileBase. IsVisible
- A new method, OESVGGroup. IsVisible, has been added.

## 6.15.3 Preliminary API - API Changes

- The atom and bond display parameters of the following functions are no longer const:
  - OEDrawSVGToggleText
  - OEDrawSVGHoverText
  - OEAddSVGClickEvent

## 6.15.4 Major bug fixes

• Objects that have been drawn in hidden SVG groups are no longer visible in other image file formats. For example, when adding hover text to atoms (using the  $OEDTawSVGHOVPTText$  function), the text will only be visible in SVG images when the mouse is moved over a displayed atom. If the image is written into any other image file format, the hover text is no longer visible.

![](_page_585_Figure_16.jpeg)

• When generating interactive SVG images, hover text (OEDrawSVGToggleText) and click events (OEAddSVGClickEvent) can both be added to atoms and bonds.

## 6.15.5 Minor bug fixes

• The Ogham API, deprecated since 2014, is no longer available.

## **6.15.6 Documentation changes**

• A new section, *Depicting Molecules in a Table*, has been added.

# **6.16 OEDepict TK 2.3.5**

## 6.16.1 New features

- A new function,  $OEConfigure2DMolDisplays$   $options$ , has been added to help generate consistent command line interfaces for depiction examples and utilities. Generated interfaces now include correspondence between each command line option and its related entrypoint in OEDepict TK. For more details see the documentation for OEConfigure2DMolDisplayOptions.
- A position property has been added to the "lasso" highlighting style that allows drawing the highlights either below or above the depicted molecules. This property can be set either by the constructor of the OEHighlightByLasso class or via the OEHighlightByLasso. SetPosition method.
- The OE2DPath class has been extended to handle "empty" 2D paths:
  - $-$  OE2DPath default constructor
  - OE2DPath.AddStartPoint method
  - OE2DPath. SetClosed method
  - OE2DPath. IsValid method

## **6.16.2 Preliminary API**

- A new Preliminary API has been added to support the generation of interactive SVG images:
  - OESVGClass and OESVGGroup classes
  - OEImageBase. PushGroup, OEImageBase. PopGroup, OEImageBase.NewSVGGroup, OEImageBase.NewSVGClass, OEImageBase.GetSVGGroup, and OEImageBase. Get SVGC Lass methods of the OEImageBase base class and its derived classes
  - OEDrawSVGHoverText, OEDrawSVGToggleText, and OEAddSVGClickEvent functions

## 6.16.3 Major bug fixes

. On OSX, the deprecated CGContextSelectFont and CGContextShowTextAtPoint Core Graphics functions have been replaced. These function were used to handle fonts when drawing text in PNG images. **OEDepict TK** currently supports the following font mapping on OSX for PNG images:

| OpenEye Font Family Type | Font Name       |
|--------------------------|-----------------|
| OEFontFamily_Arial       | Arial           |
| OEFontFamily_Courier     | CourierNewPS    |
| OEFontFamily_Helvetica   | Helvetica       |
| OEFontFamily_Times       | TimesNewRomanPS |

## 6.16.4 Minor bug fixes

- When performing fixed coordinate molecule alignment (see OEAlignment Options. SetFixedCoords), only the set of atoms considered during the alignment are now used to evaluate the quality of the alignment. As a result, fixed coordinate alignment succeeds more frequently, circumventing the need to fall back to the more exhaustive alignment method.
- Bond stereo information is now re-perceived by calling the OEMDLPerceiveBondStereo function after finding the best 2D alignment with the OEPrepareAlignedDepiction function when the alignment is defined by either an OESubSearch or an OEMCSSearch object.

## 6.16.5 Python-specific changes

- The following Python functions have been added:
  - OERenderMoleculeToBytes
  - OEWriteImageToBytes
  - OEWriteReportToBytes

## **6.16.6 Documentation changes**

- A new chapter, *Generating Interactive SVG Images*, has been added.
- A new section, *Python Cookbook Examples*, has been added.

# 6.17 OEDepict TK 2.3.4

## 6.17.1 New features

- A new function, *OEP repareMultiAlignedDepiction*, has been added that performs 2D molecule alignment based on common fragments between two molecules.
- A new method,  $CreateCopy$ , has been added to the OEHighlightBase base class and all of its derived classes.
- A new function, *OEDrawCurvedRectangle*, has been added that renders a rectangle with rounded corners.

## 6.17.2 Major bug fixes

- The OE2DMolDisplay constructor previously threw an error when initialized with an empty molecule or with a molecule with no coordinates. A warning is now thrown and the object is marked invalid (e.g., the OE2DMolDisplay. IsValid method will return false). In addition, an OE2DMolDisplay object becomes invalid if the molecule from which it was initialized is modified (e.g., when atoms/bonds are added or deleted). All OEDepict TK functions handling an OE2DMolDisplay object now check the validity of the object prior to use.
- Reactions with only product or only reactant components are now depicted correctly with a reaction arrow and the "+" sign between the components.
- The methods OEImageBase. DrawArc and OEImageBase. DrawPie have been unified when generating PDF images. As a result, arc and pie objects in PDF images appear more seamless.

![](_page_588_Figure_1.jpeg)

Fig. 3: Example of depiction with alignment based on molecule similarity

## 6.17.3 Minor bug fixes

- When generating an SVG image, the opacity of the background is now written into the file. This allows generating images with a semi-transparent background.
- For the molecules C#C and C=C, the carbon atom labels are now always explicitly depicted.
- When determining the scaling of a depicted molecule, the bounding box of each multi-line bond is now considered to ensure that no bond is rendered outside the canvas.
- A minor molecule scaling issue that occurred when using fixed atom label fonts has been fixed.
- The function  $OEDrawChevronArrow$  has been improved to handle very short arrows. In addition, the default parameters of the function have been changed.

## **6.17.4 Documentation changes**

- A new section, Molecule Alignment Based on Molecular Similarity, has been added to demonstrate the new OEPrepareMultiAlignedDepiction function.
- Warnings have been added to OEWriteReportToString, OERenderMoleculeToString, and OEWriteImageToString to alert that these functions return bytes in Python 3.

# 6.18 OEDepict TK 2.3.3

## 6.18.1 New features

- The following APIs have been added to allow the interrogation of the OE2DPath class:
  - OE2DPath. GetPoints and OE2DPath. IsClosed methods
  - OE2DPathPoint class
  - OE2DPathPointType namespace

## 6.18.2 Minor bug fixes

- OEP repareDepiction has been fixed to correctly suppress all hydrogens when requested. Previously, it retained depiction hydrogens for some molecules.
- OEPrepareDepiction no longer crashes when used on OEMolBaseType\_OEMiniMol molecule implementations.

## **6.18.3 Documentation changes**

• All images in the OEDepict TK documentation have been regenerated to reflect the changes made since the 2016.Jun release.

# **6.19 OEDepict TK 2.3.2**

## 6.19.1 New features

- OE2DMolDisplayOptions. GetAtomVisibilityFunctor and OE2DMolDisplayOptions. SetAtomVisibilityFunctor methods have been added to support the ability to selectively hide portions of a structure from depictions.
- OEAlignmentOptions. SetAddDepictionHydrogens and OEAlignmentOptions. GetAddDepictionHydrogens methods have been added to control depiction hydrogens added during molecule alignment.
- · OEGetAverageBondLengthInDispCoords function has been added.
- OEGetNearbyAtom and OEGetNearbyBond functions have been added.
- OENearestAtom and OENearestBond classes now store the display position of the nearest atom and bond, respectively.

## 6.19.2 Major bug fixes

• A memory issue that caused OEP repareAlignedDepiction function to crash has been fixed. The performance of molecule alignment has been also improved.

## 6.19.3 Minor bug fixes

• Clashes between atom labels and inside bond lines of rings have been eliminated in cases when font scales larger than the default value were used. See the example below.

![](_page_590_Figure_5.jpeg)

## 6.19.4 C#-specific changes

OEImageBase. DrawArc method no longer throws an "Out Of Memory" error message when drawing an arc with a small angle and/or small radius. For more details, see Graphics. DrawArc Method.

## **6.19.5 Documentation changes**

• All images in the OEDepict TK documentation were automatically regenerated to reflect the changes made since the previous release.

# **6.20 OEDepict TK 2.3.1**

## 6.20.1 New features

· OEHighlightByLasso. SetConsiderAtomLabelBoundingBox method has been added to keep lines of highlighting from clashing with the atom labels.

![](_page_591_Figure_1.jpeg)

Table 1: Examples of highlighting using the lasso style

## 6.20.2 Minor bug fixes

· Bonds with the OEBondStereo\_DoubleEither property are now always depicted with the OEBondDisplayType\_DoubleBowTie style.

# **6.21 OEDepict TK 2.3.0**

## 6.21.1 New features

- Functionalities have been added to customize the general layout of the molecule display:
  - $-$  the margin(s) around the molecule can now be changed (for more details, see OE2DMolDisplayOptions.SetMargin and OE2DMolDisplayOptions.SetMargins methods)
  - the height of the title area can now be changed (for more details, see  $OE2DMolDisplayOptions$ . SetTitleHeight method)

![](_page_591_Figure_10.jpeg)

#### Table 2: Example of molecule display layouts depending on position of the title

• A new highlighting style, OEHighlightStyle\_Lasso, has been added along with the corresponding highlighting class OEHighlightByLasso. See the example in Figure: Example of highlighting using the "lasso" style. below.

![](_page_592_Figure_1.jpeg)

Fig. 4: Example of highlighting using the "lasso" style

- Text can now be associated with hyperlinks via the *OEFont* class. This functionality is only available for PDF and SVG image formats. For more details and an example see the OEFont. Set Hyperlink method.
- The title of the molecule is now scaled along with the size of the image by default. The OE2DMolDisplayOptions. SetTitleFontScale method was added to enable changing the scaling factor or allowing a fixed font size to be used regardless of the dimensions of the image. See also the OE2DMolDisplayOptions. SetTitleFont method.
- The OE2DMolDisplayOptions. SetAtomLabelFontScale method now allows using a fixed font size regardless of size of the molecule. Previously, the atom labels of the molecule were scaled along with the size of molecule.
- In case of the OEBondColorStyle ByElement style, the wedge/hash stereo bonds are also colored by the corresponding element types. See the effect of this change in Table: Example of bond coloring below.

![](_page_592_Figure_7.jpeg)

Table 3: Example of bond coloring

- If the width or the height of a molecule display is not specified it will be set to 50.0.
- · OEWriteReportToString function has been added.
- OEDrawCurvedBorder function has been added.

## 6.21.2 Major bug fixes

• The layout of the molecule depiction has been improved to eliminate atom label clippings. These label clippings used to occur in cases when font scales larger than the default value were used. See the effect of this change in Table: Improved depiction layout below.

![](_page_593_Figure_3.jpeg)

Table 4: Improved depiction layout

• The bounding boxes of labels are now considered when positioning atom properties. As a result, the number of overlaps is reduced in cases where font scales larger than the default value are used. See the effect of this change in Table: Example of improving the positioning of atom properties below.

![](_page_593_Figure_6.jpeg)

Table 5: Example of improving the positioning of atom properties

## 6.21.3 Minor bug fixes

- The default parameter for the maximum number of bond rotations of the OEAlignmentOptions class is  $2^{16}$  = 65536. This means that by default only the first 16 single bonds of the  $fit$  molecule will be rotated to maximize molecule alignment when invoking the OEPrepareAlignedDepiction function.
- OEPrepareAlignedDepiction has been optimized to be 10% faster on average. The algorithm was also revised to reduce the accumulation of floating point errors.
- The atom mapping index is no longer displayed (redundantly) in the case of R-groups. See the effect of this change in Table: Example of displaying atom map indices below. See also the OEDisplayAtomMapIdx class.

![](_page_594_Figure_1.jpeg)

Table 6: Example of displaying atom map indices

• OEAromaticStyle\_Circle depiction style has been improved. See the effect of this change in Table: Example of Kekule (default) and circle aromatic depiction styles below.

![](_page_594_Figure_4.jpeg)

![](_page_594_Figure_5.jpeg)

- If a bond display style cannot be determined for example, in case of a broken molecule the bond is now displayed using the  $OEBondDisplayType\_Any$  style and no error message will be thrown.
- OEAddHighlightOverlay function no longer generates different images on different platforms.

## 6.21.4 Python-specific changes

• The deprecated Ogham API is no longer tested in Python. See also *Deprecated Ogham* section.

## 6.21.5 Documentation changes

- Molecule Depiction with Transparent Background section was added to show how to generate molecule depiction with a transparent background.
- Code snippets have been added to the following functions:
  - OERenderMoleculeToString
  - OEWriteImageToString
- All images in this documentation have been automatically regenerated to reflect the changes made since the previous release.

# 6.22 OEDepict TK 2.2.6

## 6.22.1 New features

- The following changes have been made to improve the SVG images containing certain geometries (especially those made by the OE2DPropMap class):
  - OELineCap Butt (the default line cup) and OELineJoin Miter (the default line join) parameters for shapes (lines, rectangles, etc.) are no longer written into the SVG images.
  - OEImageBase. DrawRectangle for SVG will now trim the trailing zeros and the decimal point.

The above changes resulted in 40% smaller images and 10% faster image writing without any visual difference.

- *OE2DPath* class has been added to allow drawing more complex lines connected by a series of points. The following methods were added to accept OE2DPath objects:
  - OEImageBase. DrawPath
  - OEImage.DrawPath
  - OEImageFrame. DrawPath
- · OEHighlightByColor. SetAtomExternalHighlight was added to generate better highlighting for small images.
- OEAnnotateValenceProblems function was added to highlight potential atom valence problems on the molecule diagram.
- · OEWrite2DRingDictionaryReport function was added to generate a multi-page report for user-defined ring dictionaries. See also the 2D Coordinate Generation chapter in the OEChem TK manual.
- OEImageBase. GetGlobalOffset method was added to return the global position of the image. This is currently only useful for subframes of an OEImageFrame object.

## 6.22.2 Major bug fixes

• OEPrepareAlignedDepiction has been optimized to be twice as fast on average.

## 6.22.3 Minor bug fixes

- OEAnnotateDepictionProblems style has been redesigned to be more visually pleasing.
- The positioning of  $+$  signs for reactions has been improved. The  $+$  signs and the arrow of the reactions now scale with the default line width of the molecule.

## **6.22.4 Documentation changes**

- $ringdict2pdf$  example has been added to generate a multi-page ring dictionary report.
- - ringdict parameter has been added to the following examples to utilize user-defined ring dictionaries:
  - $-$  *depict* example
  - $-$  mol2img example
  - $-$  mols2pdf example
- All images in this documentation were automatically regenerated to reflect the changes made since the previous release.

# **6.23 OEDepict TK 2.2.5**

## 6.23.1 New features

- $OEImage$  allows users to easily rescale images without having to re-render all the drawing commands.
- OEPrepareDepictionOptions. SetDepictOrientation allows users to control the preferred orientation of the 2D coordinates. This allows optimizing 2D coordinate generation for a particular orientation: horizontal, vertical, or square. For example, OEDepictOrientation Horizontal should be preferred when vertical space is expensive, as on web pages and spreadsheets.
- · OEHighlightByStick.SetAtomExternalHighlightRatio been added has to generate better highlighting for very small images. See the image in the *OEHighlightByStick*. SetAtomExternalHighlightRatio documentation for an example.
- OEConfigurePrepareDepictionOptions provides a convenient way to translate command line parameters into options on a OEP repareDepictionOptions object. All **OEDepict TK** examples have been updated to use these functions for building consistent command line interfaces. See the examples in the OEDepict *Examples Summary section.*
- OEGetCenter and OEDrawTextToCenter are convenience functions added to ensure that text is drawn vertically and horizontally in the center of an OEImageBase.
- Two new pens,  $OELight GreyBoxPen$  and  $OELight GreyPen$ , have been added.

## 6.23.2 Major bug fixes

- OEP repareDepiction now automatically regenerates 2D coordinates when the current 2D coordinates are not in the XY plane. OEPrepareDepiction now clears coordinates when any of the following conditions are true:
  - OEPrepareDepictionOptions. GetClearCoords returns true.
  - OEMolBase. GetDimension does not return 2.
  - $-$  Any Z coordinate is not 0.0.

This protects against corrupted coordinate states that may be caused by file formats not normally used for depiction, such as PDB.

• PNG images generated on Linux will now have properly filled objects and will no longer look different than those generated on OSX or Windows, as shown in the following images:

![](_page_597_Figure_8.jpeg)

• The cubic and quadratic curves drawn on OSX PNG images are no longer closed and are now consistent with PNG images generated on other platforms.

![](_page_597_Figure_10.jpeg)

![](_page_597_Figure_11.jpeg)

• PDF files should no longer cause the following warning message when read into Adobe Acrobat:

The font "Times" contains a bad/BBox.

## 6.23.3 Minor bug fixes

- A new OE2DMolDisplay. IsValid method has been added. A molecule display is considered valid only if it was initialized with a non-empty molecule with either 2D or 3D coordinates. An invalid molecule display cannot be rendered by the OERenderMolecule or the OERenderMoleculeToString functions.
- The OEHydrogenStyle\_Hidden style will no longer show any hydrogen labels, even if the hydrogen has a charge, isotopic mass, or is a radical.
- The OEAnnotateDepictionProblems function now displays E/Z CIP bond labels rather than C/T in cases where double bonds are not correctly depicted according to their cis/trans stereo specifications.

## **6.23.4 Documentation changes**

- All images in this documentation were automatically regenerated to reflect the changes made since the previous release.
- The documentation of all deprecated Ogham classes, functions, and namespaces has been removed:

Deprecated Ogham classes:

- OE8BitImage
- OEAtomStyle
- OEBondStyle
- OEDepictBase
- OEDepictColor
- OEDepictView
- OEPSImage
- OEPoly
- OEPolyF
- OESVGImage
- OEVert
- OEVertF

Deprecated Ogham functions:

- OEWriteBMP
- OEWriteEPS
- OEWriteGIF
- OEWritePPM
- OEWriteRGB
- OEWriteXPM

Deprecated Ogham namespace:

- OENamedColor
- Minor changes have been made to the documentation and examples for consistency and/or spelling errors.
- More C# examples have been added.

## 6.23.5 C++-specific changes

• OECreateWin32GraphicsImage now allows interoperability with the Windows GDI+ Graphics class object. This function is only available on the Windows operating system through C++.

## 6.23.6 Python-specific changes

- OEDepict TK no longer provides Python wrapping for the following methods of the deprecated OEDepictView class:
  - GetViewCoords
  - GetForeColor and SetForeColor
  - GetBackColor and SetBackColor

# 6.24 OEDepict TK 2.2.4

## 6.24.1 New features

- OEAnnotateDepictionProblems added to mark atom and bond stereo coordinate generation problems on output images.
- · Added OEDrawChevronArrow function.
- Added OESuppressNonDepictionHydrogens function.

## 6.24.2 Major bug fixes

- The OEP repareDepiction function now throws a warning in cases when 2D coordinates are generated that are inconsistent with the cis/trans bond stereo configuration of the molecule.
- OEPrepareAlignedDepiction can now handle molecules with more than 32 rotatable bonds. Previously, if the number of rotatable bonds was greater than 32, not enough sampling would be done to achieve a good alignment. Additionally, the set of bonds to rotate is decided in a dynamic fashion to mitigate the expense of fitting large flexible molecules.

## 6.24.3 Minor bug fixes

- Added the metal colors introduced in the 2014. Jun release to the parameters generated by the OEConfigureHighlightParams function.
- Fixed potential memory leak in the OERenderMolecule functions.

## **6.24.4 Documentation changes**

• All images in this documentation were automatically regenerated to reflect the changes made since the previous release.

# 6.25 OEDepict TK 2.2.3

## 6.25.1 New features

- OEPrepareDepictionOptions added to allow finer grained control of the OEPrepareDepiction function.
- OEGetMoleculeCoords and OEGetDisplayCoords functions added that convert 2D points between the molecule and the display coordinate systems.
- OEAddHighlightOverlay added to elegantly highlight overlapping sections of a molecule.
- Added the following functions to *OESystem* to provide predefined sets of colors:
  - OEGetColors
  - OEGetContrastColors
  - OEGetDeepColors
  - OEGetLightColors
  - OEGetVividColors
- Added the following colors to OESystem :
  - OESystem\_OEBrass
  - OESystem\_OECopper
  - OESystem\_OEGold (the original color was renamed OESystem\_OEMandarin)
  - OESystem\_OESilver
  - OESystem\_OEPewter

## 6.25.2 Major bug fixes

- Fixed Linux thread safety when writing . png files. The Cairo graphics library (http://cairographics.org) used to draw. png images on Linux is not thread safe. OEDepict TK now performs its own mutual exclusion when calling into the Cairo graphics library to ensure thread safety. It is strongly recommended to use the. svq file format when speed and server throughput is a concern. Web browser support for . svq has improved significantly in recent years and it is more effective at representing molecule graphs since they are mostly vector graphics. The only time . png is preferable over . svg is when rendering heavy raster graphics like property maps from Grapheme TK.
- Fixed thread safety of creating . svg images.
- Increased the default font size of the atom label and atom property label. See the effect of this change in Table: Example of increasing the default font size.

![](_page_601_Figure_1.jpeg)

![](_page_601_Figure_2.jpeg)

- The reaction role of hydrogens will no longer be thrown away during the depiction process. Specifically, all information present on explicit hydrogens will be preserved during the depiction process.
- OEDepict TK generated . pdf files opened by several PDF viewers would show the file as edited due to an internal representation problem. PDF viewers should no longer modify OEDepict TK generated. pdf files.
- OEDepict TK generated . pdf files should no longer cause the following warning messages when read into Adobe Acrobat:

'Arial-Bold' contains a bad /BBox. The font

The Helvetica font will now be used as the default font in . pdf files. The OEF ont Family\_Arial constant will now map to Helvetica as well in . pdf files.

## 6.25.3 Minor bug fixes

- Isotope hydrogens are never suppressed by the OEP repareDepiction function.
- . svq and . bsvq image dimensions are now specified by the "viewBox" parameter rather than the "width" and "height" parameters. This allows scaling the images in web applications.
- Functions and constructors of classes of Ogham API will now throw warning messages about being deprecated.
- Removed unbounded stack allocations.
- · Fixed the problem when wedge bonds were not highlighted correctly when using the OEHighlightStyle\_Color highlighting style. See the effect of this change in Table: Example of highlighting wedge bonds with "Color" style.

![](_page_602_Figure_1.jpeg)

Table 11: Example of highlighting wedge bonds with "Color" style

- DrawPolygon will now properly throw an exception when passed incorrect arguments.
- Adding the following division operators to the *OE2DPoint* class to be compatible with Python 3.x:
  - $-$  \_truediv\_
  - $-$  itruediv
  - $-$  \_\_floordiv\_\_
  - $-$  \_\_ifloordiv\_\_

## **6.25.4 Documentation changes**

- Updated the Highlighting Overlapped Patterns section and added a new code example that shows how to highlight overlapping matches using the new OEAddHighlightOverlay function.
- Documentation updated to reflect that OE2DMolDisplayOptions. SetAtomPropertyFunctor and OE2DMolDisplayOptions.SetBondPropertyFunctor are preferred over using OE2DAtomDisplay.SetProperty and OE2DBondDisplay.SetProperty directly to ensure molecule scaling fully accounts for the size of the labels.
- All images in this documentation were automatically regenerated to reflect the changes made since the previous release.
- Added the missing documentation for the following OESystem colors:
  - OESystem\_OEGreenBlue
  - OESystem\_OEGreenTint
- The example for a python-based web interface and web service have been moved to our Python Cookbook.

# **6.26 OEDepict TK 2.2.2**

## 6.26.1 New features

- OEPrepareAlignedDepiction can now take a OESubSearch or OEMCSSearch object to allow the layout to be driven by multiple atom mappings at the same time. The mapping that generates the best alignment will be returned in an OEAlignmentResult object.
- OEGetDefaultAtomColor added to return the default color associated with an atomic number for the given atom color style.
- · OEGreenBoxPen and OEGreenPen pens added.
- OEDepictCoordinates is now deprecated. 2D coordinate generation is now included in OEChem as the OEGenerate2DCoordinates function. Please switch to using that function instead.

## 6.26.2 Major bug fixes

• Improved the positioning of atom properties by considering the position of implicit hydrogen labels. See the effect of this change in Table: Example of improving the positioning of atom properties.

![](_page_603_Figure_9.jpeg)

Table 12: Example of improving the positioning of atom properties

## 6.26.3 Minor bug fixes

- OEDepict will automatically render enhanced Pre-TK stereo by default now. OEConfigure2DMolDisplayOptions function would viously. the  $not$  $211$ tomatically enable rendering enhanced stereo information. The behavior can be changed by the OEAtomStereoStyle\_Display\_MDLStereoCenter and OE2DMolDisplaySetup\_AtomStereoStyle constants.
- Increased the gap between the bond end and the atomic label for iodine (atomic label "I").
- Added "BRIEF" line to interfaces of OEDepict TK examples.
- OEWriteImage and OERenderMolecule that take an oeostream no longer call the stream's close method. It is the responsibility of the caller to call close on the stream if it is appropriate.

## **6.26.4 Documentation changes**

• All images in this documentation were automatically regenerated to reflect the changes made since the previous release.

# **6.27 OEDepict TK 2.2.1**

## 6.27.1 New features

- Added cubic Bézier drawing method to the following classes:
  - OEImageBase
  - $-$  OEImage
  - OEImageFrame
- Added quadratic Bézier drawing method to the following classes:
  - OEImageBase
  - $-$  OEImage
  - OEImageFrame
- Added rotation angle property to the *OEFont* class that allows to render text in various angles when calling the OEImageBase. DrawText method.
  - OEFont.GetRotationAngle
  - OEFont. SetRotationAngle

## 6.27.2 Major bug fixes

- When aligning a molecule to a template, atom clashes between the template atoms are ignored.
- OEPrepareDepiction will now suppress hydrogens even when 2D coordinates are not generated, i.e.,  $clearcoords = false.$

## 6.27.3 Minor bug fixes

- Highlighting a single atom with the  $OEHighLightStyle\_Stock$  will now work if that atom is bonded to a highlighted atom.
- Fixed problem when the scaling of small molecules resulted in depicting atom labels outside the canvas.
- Fixed problem that incorrectly positioned the "+" sign between reaction components introduced by the last **OEDepict TK** release, 2.2.0.

## **6.27.4 Documentation changes**

• All images in this documentation were automatically regenerated to reflect the changes made since the previous release.

# **6.28 OEDepict TK 2.2.0**

## 6.28.1 New features

• OEP repareDepiction now generates canonical depiction coordinates, i.e., the same 2D coordinates are generated regardless of the atom and bond ordering in the molecule. See the effect of this change in Table: Example of default element color changes.

Table 13: Example of generating depiction coordinates by the **OEPrepareDepiction function** 

| <b>OEDepict TK 2.1.0</b>                                                                                              | <b>OEDepict TK 2.2.0</b>                                                               |
|-----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| HO<br>O.<br>$\Omega$ <sup>-</sup><br>$\mathcal{L}_{\mathcal{U}_{\bullet}}$<br>°он<br>HO<br>'ОН<br>OH<br>HO<br>$\circ$ | $\Omega$ <sup>-</sup><br>n-<br>$-$ OH<br>$-$ OH<br>$\rightarrow$ OH<br>'он<br>OH<br>он |

- Added the following non-linear color gradient to OESystem:
  - OEExponentColorGradient
  - OEExponentialColorGradient
  - OELogarithmicColorGradient

These classes along with the OELinearColorGradient class now derive from the OEColorGradientBase base class.

- OEAddHighlighting function overloads added that take both atom and bond predicates.
- · OEAlignmentOptions. SetFixedCoords the method added that forces OEPrepareAlignedDepiction function to use the coordinates in the reference molecule instead of depicting them from scratch.
- OE2DMolDisplayOptions. SetBondLineGapScale method added for changing the gap between the lines of double and triple bonds.
- OE2DMolDisplayOptions. SetBondLineAtomLabelGapScale method added for changing the gap between the atom labels and the end of the bond lines.

## 6.28.2 Minor bug fixes

- OEStipple\_NoLine and OEFill\_On pen fixed on Windows when drawing a pie.
- Refined the method that is used to calculate the gap between the atom labels and the lines of the bonds when there is a charge or there are more than 3 explicit hydrogen neighbors.
- Additional warning messages are thrown when either the OE3DToBondStereo or the OE3DToAtomStereo functions fail during OEP repareDepiction.

## **6.28.3 Documentation changes**

- All images in the documentation were automatically regenerated to reflect the changes made since the previous release.
- Added several code snippets to the OERenderMolecule function.

# **6.29 OEDepict TK 2.1.0**

## 6.29.1 New features

- Added a new highlighting style,  $OEHighLightStyle\_Cogwheel$ , and the corresponding highlighting class OEHighlightByCogwheel.
- Added accessor methods for many parameters to the following highlighting classes:
  - OEHighlightByBallAndStick
  - OEHighlightByColor
  - OEHighlightByStick
- Added OE2DMolDisplayOptions. SetBondWidthScaling method that allows line width of the bonds to be increased or decreased based upon the molecule scaling factor.
- Added the following classes and functions to provide a convenient way to generate multi-page reports.
  - OEReportOptions and OEReport classes
  - OEConfigureReportOptions and OESetupReportOptions functions
  - OEWriteReport function
- Reimplemented the following Python OEDepict TK examples by utilizing the new OEReport class:
  - $-$  mols2pdf.py
  - $-$  viewmdlsearch.py
- Added the OEMultiPageImageFile. GetPage method that provides access to the individual pages of a multi-page image file.
- Added the OEConfigure ImageGridNumColumns and OEConfigure ImageGridNumRows functions to take the default number of columns and rows.
- OEPrepareAlignedDepiction has been improved the generate better 2D molecule alignments by:
  - Allowing rotations around unspecified cis/trans double bonds
  - Refining the method that scores alignments based on internal atom clashes

## 6.29.2 Major bug fixes

• Added darker default colors for some of the elements for the OEAtomColorStyle\_WhiteCPK color scheme. See the effect of these changes in Table: Example of default element color changes.

![](_page_607_Figure_3.jpeg)

![](_page_607_Figure_4.jpeg)

## 6.29.3 Minor bug fixes

- Fixed the coordinate system to start from the top-left corner for raster images on OS X when using the OEImageBase. DrawPoint method. This was causing images to appear flipped around the y-axis.
- The colors for  $OEGetHighlightColor$  were sometimes not initialized properly due to undefined library initialization order. This was causing the function to always return white.
- Atoms that have both the atomic number and the atom map index of zero will now be rendered as  $\star$ .
- Synchronized code examples in all four supported languages (C++, Python, Java and C#) to ensure that they have the same behavior and generate identical images.
- OEPrepareDepiction and OEDepictCoordinates could crash or generate random coordinates for molecules with adjacent spiro centers.
- Methods that return a OE2DPoint reference, e.g. OE2DAt omDisplay. Get Coords, will now return a copy of the OE2DPoint instead in Python to avoid destructor ordering problems.
- Wrapping the following methods in Python:
  - OE2DPoint.operator+=
  - OE2DPoint.operator-=
  - $-$  OE2DPoint.operator\*=
  - OE2DPoint.operator/=

## **6.29.4 Documentation changes**

- Added the *Multi Page Reports* section to document the usage of the OEReport object.
- All images in the documentation were automatically regenerated to reflect the changes made since the previous release.

# **6.30 OEDepict TK 2.0.4**

## 6.30.1 New features

- Pie drawing, semi-circle, methods added to the following classes:
  - OEImageBase
  - $-$  OEImage
  - OEImageFrame
- An example of a python-based web interface and web service have been added. The code for this example was on GitHub, as it required multiple files.
- Enabling the depiction of MDL's enhanced stereochemical representation by default. See the OEAtomStereoStyle\_Display\_MDLStereoCenter constant.

## 6.30.2 Major bug fixes

- The following molecule depiction defaults have been changed:
  - The background color is now pure white instead of a very light grey.
  - $-$  The bond width is now 2.0 instead of 1.0.

See the effect of these changes in Table: Example of default molecule depictions.

![](_page_608_Figure_14.jpeg)

#### Table 15: Example of default molecule depictions

## 6.30.3 Minor bug fixes

• Adding the depiction of R-groups for molecules that have not been initialized from a MDL query file. See the example the in the Table: Example of depicting R-Groups.

![](_page_609_Figure_3.jpeg)

![](_page_609_Figure_4.jpeg)

- Fixed a bug that would erroneously hide the following types of hydrogens in a depiction:
  - isolated hydrogens
  - charged hydrogens
  - hydrogen isotopes
- Fused ring system templates added for 29 different types of complex depiction cases.
- OE2DAtomDisplay. SetHCount method will now place the hydrogen position correctly as returned by OE2DAtomDisplay.GetHPosition, i.e., the position relative to the heavy atom. An incorrect position was possible when generating 2D coordinates with OEP repareDepiction with the parameter suppressH set to false.
- The stipple factor of a line in now based on the line width instead of the scaling factor of the molecule display.

![](_page_609_Figure_12.jpeg)

Table 17: Example of line width affecting the stipple factor

• Atom stereo depiction improved:

- The number of individual lines used in the  $OEBondDisplayType\_Hash$  and the OEBondDisplayType\_Wavy stereo bonds now depends on the bond width.
- Heuristic used to shorten hash and wedge stereo bonds improved.

See the effect of these improvements in Table: Example of depicting atom stereo.

![](_page_610_Figure_4.jpeg)

![](_page_610_Figure_5.jpeg)

- OEBondDisplayType\_Any bond type will now properly set the stipple factor for the end pen of that bond.
- Fixing the problem when the default atom label colors were not updated after atom color style change. For example when setting the atom color style to OEAtomColorStyle\_WhiteMonochrome the super atoms remained pink rather than changed to black. See the effect of fix in Table: Example of using the 'White-Monochrome' atom color style.

![](_page_610_Figure_8.jpeg)

Table 19: Example of using the 'WhiteMonochrome' atom color style

## **6.30.4 Documentation changes**

• All images are automatically regenerated to reflect the changes made since the previous release.

# 6.31 OEDepict TK 2.0.3

## 6.31.1 New features

- OEDrawCurvedArrow function added.
- OEPrepareAlignedDepiction now allows more advanced customization of the alignment process through the OEAlignmentOptions class.
- OEChem TK's new RMSD method is used in the molecule alignment process to improvement alignment performance

## 6.31.2 Major bug fixes

- · OEPrepareAlignedDepiction performance improvement of 10% on average.
- Windows png images have been improved in the following ways:
  - Dash patterns for line drawing corrected.
  - Gamma correction turned off when colors are blended with background colors. As a result the generated png images look sharper.
  - Text anti-aliasing methodology is now dependent on the font size to ensure fonts look good at all sizes. The method of anti-aliasing changes when increasing the font size from 8 to 9.
- The following atom label layout changes:
  - If the atom has a charge, then it is rendered as a super-script on the right side of the atomic label. In the case when the implicit hydrogen symbol is placed on the right side of the atom, then the charge also follows the hydrogen symbol. (See section GR 5.1 in [Brecher-2008])
  - $-$  The dot(s) representing the radical atom follows the atoms' element symbol on the left side. In the case when the implicit hydrogen symbol is placed on the right side of the atom, then the radical dot(s) also follows the hydrogen symbol. (See section GR 5.3 in [Brecher-2008])
- Atom labels clashing with bonds have been improved by shortening the length of the depicted bond in certain cases.
- MDL query molecule atom label rendering has been improved.
- · OEDepictCoordinates clash detection has been improved to avoid unnecessary stretching of the bonds of explicit hydrogens. A tolerance has been introduced that allows smaller distances between hydrogen atoms.

## 6.31.3 Minor bug fixes

- OE2DMolDisplayOptions. SetAtomLabelFontScale upper limit has been increased from 2.0 to 3.0.
- New fused ring system templates added.
- Atom and bond highlighting now scales with the molecule instead of the dimension of the image.
- Aromatic circles now ignore the fill style of the circle.
- The following methods will now throw warnings if given nonsensical arguments:
  - OEImage. DrawCircle
  - OEImage. DrawArc
  - OEImage. DrawLine
  - OEImage. DrawPolygon
  - OEImage.DrawRectangle
  - OEImage. DrawText
  - OEImage. DrawTriangle

This should make drawing mistakes appear earlier in development, instead of only when they are rendered to a specific file format.

- OE2DMolDisplay.GetAtomDisplay and OE2DMolDisplay.GetBondDisplay no longer incorrectly check the atom and bond indices.
- OE2DMolDisplay constructors now throw a warning when a molecule being depicted has 3D coordinates and throw an error if the molecule has no coordinates.
- OEImage. Clear is now called when constructing a new OEImage object.

## **6.31.4 Documentation changes**

• All images are automatically regenerated to reflect the changes made since the previous release.

# 6.32 OEDepict TK 2.0.2

## 6.32.1 New features

- Adding a scaling factor that can be used to increase or decrease the size of the fonts used to depict atom properties. (OE2DMolDisplayOptions. SetAtomPropLabelFontScale)
- Adding a scaling factor that can be used to increase or decrease the size of the fonts used to depict bond properties. (OE2DMolDisplayOptions. SetBondPropLabelFontScale)
- Adding the following examples:
  - $-$  depict.py
  - $-$  match2img.py
  - $-$  mcsalign2D.py
  - $-$  mdlquery2img.py
  - $-$  mdlreaction2img.py

- $-$  mols2pdf.py
- $-$  mols2img.py
- smartsalign2D.py
- $-$  viewmdlsearch.py
- The constructor of the *OEImage* class now takes a background color that is used to clear the image upon construction. A . png image with transparent background can be generated by using the OETransparent Color color as a background color when constructing an OEImage object.
- Fixing the run-time initialization of the color that is used to depict super atoms.

## 6.32.2 Major bug fixes

- The cairo graphics library (http://cairographics.org) used to draw, png images on Linux has a bug where it is not thread safe when rendering text. OEDepict TK now performs its own mutual exclusion when calling into the cairo graphics library for text rendering to ensure thread safety.
- Improving the depiction of super atoms (See examples in the  $OESuperAtomStyle$  namespace)

## 6.32.3 Minor bug fixes

- OERenderMolecule called with an image and a molecule now uses the width and height of the image being passed.
- Fixing a problem where isolated atoms were not highlighted when using the OEHighlightStyle\_Color and OEHighlightStyle\_Stick highlighting styles.
- OEDepictCoordinates throws a warning when trying to generate 2D coordinates for a two member ring, for example, C1N1. The function will then fall back to trying to generate coordinates for those atoms as a chain.
- The OEDisassembleExpressions function tags atoms and bonds of the query molecule that can later be used by the OE2DMolDisplay constructor when creating atom and bond displays.
- Throwing a warning when attempting to draw a line or an arc with the OEStipple\_NoLine pen property. Throwing a warning when attempting to draw a rectangle, circle, triangle or a polygon with OEStipple\_NoLine and OEFill\_Off pen properties.
- Making sure that no radical dots are displayed for a query atom that has implicit hydrogen count information.
- Before registering an aromatic ring for the OEAromaticStyle\_Circle style, a check is performed to ensure that the detected ring is not a fused ring of two smaller rings.
- Making the background color consistent for the monochrome atom color styles. (See: OEAtomColorStyle\_WhiteMonochrome and OEAtomColorStyle\_BlackMonochrome)
- When two molecules are aligned by calling the *OEP* reparaligned Depiction function, the fit molecule is scaled by the average bond length of the reference molecule.

## 6.32.4 Deprecated Ogham

• Deprecating the OEDepictFixedCoordinates function. For molecule alignment, please use the OEPrepareAlignedDepiction function.

## **6.32.5 Documentation changes**

- Renaming the Application chapter to OEDepict Examples Summary and inserting the source code of the examples into the *Examples* chapter.
- Adding code snippets for the OEAddHighlighting function.
- Describing the layout of a depicted atom in the  $OE2DAtomDisplay$  class.
- All images in this manual are now automatically generated as part of the release process and tested against benchmark images on all supported platforms.

# **6.33 OEDepict TK 2.0.1**

## 6.33.1 Minor bug fixes

- On creation of an OE2DMolDisplay object its scale is adjusted by the average bond length of the original 2D coordinates of the molecule. This affected any rendering where the 2D coordinates are not generated by OEDepict.
- Speed optimization of the OEP repareAlignedDepiction function were added.
- Adding mol2img python example

# 6.34 OEDepict TK 2.0.0

## 6.34.1 New features

- Using *OE2DPoint* that represents coordinates
- Using OEColor that handles transparency
- Adding OELinearColorGradient class that allows color ramping
- Supporting various font properties (OEFont)
  - $-$  size
  - $-$  color
  - style (italic, bold) (OEFontStyle)
  - family (Arial, Helvetica, etc.) (OEF ont Family)
- Supporting various line properties  $(OEPen)$ 
  - $-$  line width
  - background, foreground color
  - various stipple styles ( $OEStipple$ )
  - standard line join, line cup styles (OELineJoin, OELineCap)

- Providing convenient molecule depiction that is highly customizable  $(OE2DMolDisplayOptions)$ 
  - different aromatic ring representations ( $OEAromaticstype$ )
  - atom coloring (monochrome, CPK) (OEAtomColorStyle)
  - bond coloring (atom-based, monochrome) (OEBondColorStyle)
  - various atom stereo representations ( $OEAtomStereoStyle$ )
  - various bond stereo representations ( $OEBondStepC$
  - various explicit/implicit hydrogen representations (OEHydrogenStyle)
  - depicting atom properties (OEDisplayAtomPropBase)
  - depicting bond properties (OEDisplayBondPropBase)
  - setting atom label, atom and bond property label font styles
  - various super atom styles ( $OESuperAtomStyle$ )
- Depicting atom radicals (OERadicalDisplayType)
- Adding the *OEP repareDepiction* function that prepares a molecule before depiction.
- Adding the *OEPrepareAlignedDepiction* function that generates 2D-coordinates of a molecule to maximize its alignment to a reference molecule.
- Introducing the OEImageFrame and the OEImageGrid classes that allows various molecule layouts (see the Molecule Layouts chapter)
- Implementing three customizable highlighting styles and allowing to utilize user-defined ones (see also the Highlighting chapter) - ball and stick (OEHighlightByBallAndStick) - color (OEHighlightByColor) - stick (OE-HighlightByStick)
- Adding the OEAddHighlighting function that helps to highlight atoms and/or bonds
- OEDrawEquilibriumArrow  $\ast$ • Implementing three arrow drawing functions: OEDrawReactionArrow \* OEDrawResonanceArrow
- Adding functions that automatically generate standard interfaces for OEDepict applica-OEConfigure2DMolDisplayOptions - OEConfigureHighlightParams tions: OEConfigureImageGridParams-OEConfigureMultiPageParams
- Adding various rendering functions (OERenderMolecule)
- Adding functions to write images ( $OEWriteImage$ )
- Supporting the following image file formats:

| Graphics File Format            | File Extension |
|---------------------------------|----------------|
| PNG (Portable Network Graphics) | .png           |
| SVG (Scalable Vector Graphics)  | .svg           |
| bare SVG (with no header)       | .bsvg          |
| Postscript                      | .ps            |
| Encapsulated PostScript         | .eps           |
| PDF (Portable Document Format)  | .pdf           |

Note: PNG support is based upon the cairo graphics library on Linux. Most linux distributions install this shared library by default, but it may be possible for a super stripped down installation to not include it. OEDepict TK has

no specific version requirement for this library, so the *cairo* package can be installed through traditional distribution specific means: rpm, yum, yast, zypper, etc.

- Supporting multi-page images (see the Multi Page Image chapter)
- Supporting to depict MDL queries (see the MDL Query Depiction chapter)
- Supporting MDL reaction depiction (see the MDL Reaction Depiction chapter)
- Providing more than 40 example codes in four different languages  $(C++, Python, Java, C#)$  that demonstrate the functionalities of the the new toolkit.
- Providing 10 C++ applications (see the OEDepict Examples Summary chapter)

## 6.34.2 Deprecated Ogham

The following classes, functions and namespaces are **not** going to be supported any longer and will be deprecated in the future:

Deprecated Ogham classes:

- · OE8BitImage
- · OEAtomStyle
- · OEBondStyle
- · OEDepictBase
- · OEDepictColor
- · OEDepictView
- · OEPSImage
- · OEPoly
- · OEPolyF
- OESVGImage
- · OEVert
- · OEVertF

#### Deprecated Ogham functions:

- · OEWriteBMP
- · OEWriteEPS
- · OEWriteGIF
- · OEWritePPM
- · OEWriteRGB
- · OEWriteXPM

#### Deprecated Ogham namespace:

· OENamedColor

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

| Name of Project               | Website                                                               | License  |
|-------------------------------|-----------------------------------------------------------------------|----------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                  | https:// |
| absl-py                       | https://github.com/abseil/abseil-py                                   | https:// |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                   | https:// |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                 | https:// |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                 | N/A      |
| AmberUtils                    | http://ambermd.org                                                    | N/A      |
| ambit                         | https://github.com/khimaros/ambit                                     | https:// |
| amqp                          | https://github.com/celery/py-amqp                                     | https:// |
| anaconda-anon-usage           | Orion Floes                                                           | https:// |
| angular                       | https://github.com/angular/angular.js                                 | https:// |
| angular-animate               | https://github.com/angular/angular.js                                 | https:// |
| angular-cache                 | https://github.com/jmdobry/angular-cache                              | https:// |
| angular-cookies               | https://github.com/angular/angular.js                                 | https:// |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                      | https:// |
| angular-mocks                 | https://github.com/angular/angular.js                                 | https:// |
| angular-resource              | https://github.com/angular/angular.js                                 | https:// |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                      | https:// |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                 | https:// |
| angular-ui-router             | https://github.com/angular-ui/ui-router                               | https:// |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                    | https:// |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                          | https:// |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                              | https:// |
| annotated-types               | https://github.com/annotated-types/annotated-types                    | https:// |
| anyio                         | https://github.com/agronholm/anyio                                    | https:// |
| appdirs                       | http://github.com/ActiveState/appdirs                                 | http://  |
| appengine                     | https://google.golang.org/appengine                                   | https:// |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                     | https:// |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md            | https:// |
| Name of Project               | Website                                                               | License  |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                  | https:// |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                         | https:// |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                            | https:// |
| ascii85                       | https://github.com/huandu/node-ascii85                                | https:// |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                        | https:// |
| asgiref                       | https://github.com/django/asgiref/                                    | https:// |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                   | https:// |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render | https:// |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers     | https:// |
| assertions                    | https://github.com/smartystreets/assertions                           | https:// |
| asttokens                     | https://github.com/gristlabs/asttokens                                | https:// |
| astunparse                    | https://github.com/simonpercivall/astunparse                          | https:// |
| async-lru                     | https://github.com/aio-libs/async-lru                                 | https:// |
| async-timeout                 | https://github.com/aio-libs/async-timeout                             | https:// |
| atk-1.0                       | https://docs.gtk.org/atk/                                             | https:// |
| atomic                        | https://github.com/uber-go/atomic                                     | https:// |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                      | https:// |
| attrs                         | https://www.attrs.org/                                                | https:// |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                     | https:// |
| Babel                         | https://github.com/python-babel/babel                                 | https:// |
| backcall                      | https://github.com/takluyver/backcall                                 | https:// |
| backports                     | https://github.com/brandon-rhodes/backports                           | https:// |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache               | https:// |
| base62                        | https://github.com/kare/base62                                        | https:// |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                        | https:// |
| billiard                      | https://github.com/celery/billiard                                    | https:// |
| biopython                     | https://biopython.org                                                 | https:// |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst         | https:// |
| bitset                        | https://github.com/willf/bitset                                       | https:// |
| blas                          | https://www.netlib.org/blas/                                          | https:// |
| bleach                        | https://github.com/mozilla/bleach                                     | https:// |
| blessings                     | https://github.com/erikrose/blessings                                 | https:// |
| blinker                       | https://pythonhosted.org/blinker/                                     | https:// |
| blosc                         | https://github.com/Blosc/python-blosc                                 | https:// |
| blosc2                        | https://github.com/Blosc/python-blosc2                                | https:// |
| boltons                       | https://github.com/mahmoud/boltons                                    | https:// |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html | https:// |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html | https:// |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                        | https:// |
| boto3                         | https://github.com/boto/boto3                                         | https:// |
| botocore                      | https://github.com/boto/botocore                                      | https:// |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                | https:// |
| Brotli                        | https://github.com/google/brotli                                      | https:// |
| brotli-bin                    | https://github.com/google/brotli                                      | https:// |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                  | https:// |
| brotlipy                      | https://github.com/python-hyper/brotlipy                              | https:// |
| bson                          | http://github.com/py-bson/bson                                        | https:// |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                 | https:// |
| bzip2                         | https://www.bzip.org                                                  | https:// |
| Name of Project               | Website                                                               | License  |
| c-ares                        | https://github.com/c-ares/c-ares                                      |          |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock              |          |
| cached-property               | https://github.com/pydanny/cached-property                            |          |
| cachetools                    | https://github.com/tkem/cachetools/                                   |          |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                             |          |
| canvas                        | https://github.com/Automattic/node-canvas                             |          |
| cctbx                         | https://github.com/cctbx/cctbx_project                                |          |
| celery                        | https://github.com/celery/celery                                      |          |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                           |          |
| certifi                       | https://certifi.readthedocs.io/en/latest/                             |          |
| cffi                          | https://github.com/python-cffi/cffi                                   |          |
| cftime                        | https://pypi.org/project/cftime/                                      |          |
| chardet                       | https://github.com/chardet/chardet                                    |          |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                          |          |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                               |          |
| click                         | https://palletsprojects.com/p/click/                                  |          |
| click-completion              | https://github.com/click-contrib/click-completion                     |          |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                     |          |
| click-plugins                 | https://github.com/click-contrib/click-plugins                        |          |
| click-repl                    | https://github.com/untitaker/click-repl                               |          |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                              |          |
| cmake                         | https://cmake.org/                                                    |          |
| colorama                      | https://github.com/tartley/colorama                                   |          |
| comm                          | https://github.com/ipython/comm                                       |          |
| compose                       | https://github.com/docker/compose                                     |          |
| conda-content-trust           | https://github.com/conda/conda-content-trust                          |          |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                        |          |
| conda-package-handling        | https://github.com/conda/conda-package-handling                       |          |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming              |          |
| conda-token                   | https://anaconda.org/anaconda/conda-token                             |          |
| confuse                       | https://github.com/beetbox/confuse                                    |          |
| contourpy                     | https://github.com/contourpy/contourpy                                |          |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                 |          |
| cryptography                  | https://github.com/pyca/cryptography                                  |          |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                  |          |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                             |          |
| cupy-cuda113                  | https://cupy.dev/                                                     |          |
| curl                          | https://curl.se                                                       |          |
| cycler                        | https://github.com/matplotlib/cycler                                  |          |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                               |          |
| Cython                        | https://cython.org                                                    |          |
| d3                            | https://github.com/mbostock/d3                                        |          |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                             |          |
| ddsketch                      | http://github.com/datadog/sketches-py                                 |          |
| debugpy                       | https://aka.ms/debugpy                                                |          |
| decimal                       | https://github.com/shopspring/decimal                                 |          |
| decorator                     | https://github.com/micheles/decorator                                 |          |
| deepdiff                      | https://github.com/seperman/deepdiff                                  |          |
| deeptime                      | https://github.com/deeptime-ml/deeptime                               |          |

| Name of Project               | Website                                                                             | License            |
|-------------------------------|-------------------------------------------------------------------------------------|--------------------|
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https:/            |
| dill                          | https://github.com/uqfoundation/dill                                                | https:/            |
| distro                        | Orion Floes                                                                         | https:/            |
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
| fftw                          | https://www.fftw.org                                                                | https:/            |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              | https:/            |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/            |
| finufft                       | https://github.com/flatironinstitute/finufft                                        | https:/            |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/            |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               | https:/            |
| flit-core                     | https://github.com/pypa/flit                                                        | https:/            |
| FLTK                          | https://www.fltk.org/index.php                                                      | https:/            |
| fmt                           | https://fmt.dev/latest/index.html                                                   | https:/            |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         | https:/            |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      | https:/            |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       | https:/            |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/            |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            | https:/            |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/            |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/            |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/            |
| Name of Project               | Website                                                                             | License            |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https:/            |
| freetype                      | https://freetype.org                                                                | https:/            |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https:/            |
| frozendict                    | Orion Floes                                                                         | https:/            |
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
| glib                          | https://docs.gtk.org/glib/                                                          | https:/            |
| GLM Library                   | https://github.com/g-truc/glm                                                       | https:/            |
| gls                           | https://github.com/jtolds/gls                                                       | https:/            |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https:/            |
| go-connections                | https://github.com/docker/go-connections                                            | https:/            |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https:/            |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https:/            |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https:/            |
| go-ini                        | https://github.com/go-ini/ini                                                       | https:/            |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             | https:/            |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https:/            |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           | https:/            |
| go-ole                        | https://github.com/go-ole/go-ole                                                    | https:/            |
| go-pg                         | https://github.com/go-pg/pg                                                         | https:/            |
| go-redis                      | https://github.com/go-redis/redis/v8                                                | https:/            |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                            | https:/            |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                            | https:/            |
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
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https://           |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https://           |
| graphviz                      | https://graphviz.org/                                                               | https://           |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https://           |
| groupcache                    | https://github.com/golang/groupcache                                                | https://           |
| grpc                          | https://google.golang.org/grpc                                                      | https://           |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https://           |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https://           |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  | https://           |
| gts                           | https://sourceforge.net/projects/gts/                                               | https://           |
| h5py                          | https://www.h5py.org                                                                | https://           |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https://           |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https://           |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https://           |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https://           |
| he                            | https://github.com/mathiasbynens/he                                                 | https://           |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https://           |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https://           |
| htslib                        | https://www.htslib.org                                                              | https://           |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https://           |
| icu                           | https://github.com/unicode-org/icu                                                  | https://           |
| idna                          | https://github.com/kjd/idna                                                         | https://           |
| imageio                       | https://github.com/imageio/imageio                                                  | https://           |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https://           |
| <b>ImmuneBuilder</b>          | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https://           |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https://           |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https://           |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https://           |
| inflection                    | https://github.com/jinzhu/inflection                                                | https://           |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https://           |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https://           |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https://           |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https://           |
| ipykernel                     | https://ipython.org                                                                 | https://           |
| ipython                       | https://ipython.org                                                                 | https://           |
| ipython-genutils              | http://ipython.org                                                                  | https://           |
| ipywidgets                    | http://jupyter.org                                                                  | https://           |
| isodate                       | https://github.com/gweis/isodate/                                                   | https://           |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https://           |
| jax                           | https://github.com/google/jax                                                       | https://           |
| jaxlib                        | https://github.com/google/jax                                                       | https://           |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              | https://           |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https://           |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https://           |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https://           |
| jpeg                          | https://www.ijg.org                                                                 | https://           |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https://           |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https://           |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https://           |
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
| jupyter-server                | http://jupyter.org                                                                  | https:             |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:             |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:             |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:             |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:             |
| jupyter_client                | http://jupyter.org                                                                  | https:             |
| jupyter_core                  | http://jupyter.org                                                                  | https:             |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https:             |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:             |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:             |
| keras                         | https://github.com/keras-team/keras                                                 | https:             |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:             |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:             |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:             |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:             |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:             |
| kombu                         | https://kombu.readthedocs.io                                                        | https:             |
| krb5                          | https://web.mit.edu/kerberos/                                                       | https:             |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:             |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:             |
| lcms2                         | https://www.littlecms.com                                                           | https:             |
| lerc                          | https://github.com/Esri/lerc                                                        | https:             |
| libarchive                    | http://www.libarchive.org                                                           | https:             |
| libblas                       | https://www.netlib.org/blas/                                                        | https:             |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:             |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:             |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https:             |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                |
| libclang                      | <b>Orion Floes</b>                                                                  | https:             |
| libcurl                       | https://curl.se/libcurl/                                                            | https:             |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:             |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:             |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:             |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://            |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:             |
| libffi                        | https://github.com/libffi/libffi                                                    |                    |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:             |
| libgd                         | https://libgd.github.io                                                             | https:             |
| libglib<br>libiconv           | https://github.com/PolMine/libglib<br>https://www.gnu.org/software/libiconv/        | https:             |
| Name of Project               | Website                                                                             |                    |
| libint                        | https://tinyurl.com/yvw97wbw                                                        |                    |
| liblapack                     | http://www.netlib.org/lapack/                                                       |                    |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         |                    |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     |                    |
| libmambaforge                 | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                |                    |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       |                    |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  |                    |
| libopenblas                   | https://www.openblas.net/                                                           |                    |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          |                    |
| libpq                         | https://www.postgresql.org/                                                         |                    |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              |                    |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 |                    |
| libssh2                       | https://github.com/libssh2/libssh2                                                  |                    |
| libtiff                       | https://www.libtiff.org/                                                            |                    |
| libtrust                      | https://github.com/docker/libtrust                                                  |                    |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           |                    |
| libuv                         | https://github.com/libuv/libuv                                                      |                    |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      |                    |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      |                    |
| libxc                         | https://www.tddft.org/programs/libxc/                                               |                    |
| libxcb                        | https://xcb.freedesktop.org                                                         |                    |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               |                    |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    |                    |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 |                    |
| libzlib                       | https://zlib.net                                                                    |                    |
| lime                          | https://github.com/marcoter/lime                                                    |                    |
| lit                           | http://llvm.org                                                                     |                    |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               |                    |
| llvmlite                      | http://llvmlite.readthedocs.io                                                      |                    |
| loader-utils                  | https://github.com/webpack/loader-utils                                             |                    |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         |                    |
| logrus                        | https://github.com/sirupsen/logrus                                                  |                    |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  |                    |
| lxml                          | https://lxml.de                                                                     |                    |
| lz4-c                         | https://www.lz4.org/                                                                |                    |
| markdown                      | https://github.com/evilstreak/markdown-js                                           |                    |
| markdown-it-py                | Orion Floes                                                                         |                    |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           |                    |
| matplotlib                    | https://matplotlib.org                                                              |                    |
| matplotlib-base               | https://matplotlib.org                                                              |                    |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        |                    |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            |                    |
| mdtraj                        | https://www.mdtraj.org/                                                             |                    |
| mdurl                         | Orion Floes                                                                         |                    |
| mergo                         | https://github.com/imdario/mergo                                                    |                    |
| mistune                       | https://github.com/lepture/mistune                                                  |                    |
| intel-mkl-src                 | https://github.com/rust-math/intel-mkl-src                                          |                    |
| mkl_fft                       | https://github.com/IntelPython/mkl_fft                                              |                    |
| Name of Project               | Website                                                                             | License            |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https:/            |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https:/            |
| ml-dtypes                     | <b>Orion Floes</b>                                                                  | https:/            |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https:/            |
| moment                        | https://github.com/moment/moment                                                    | https:/            |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https:/            |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https:/            |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https:/            |
| mpmath                        | http://mpmath.org/                                                                  | https:/            |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https:/            |
| msgpack                       | https://msgpack.org/                                                                | https:/            |
| multidict                     | https://github.com/aio-libs/multidict                                               | https:/            |
| multierr                      | https://go.uber.org/multierr                                                        | https:/            |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https:/            |
| munkres                       | https://software.clapper.org/munkres/                                               | https:/            |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https:/            |
| namex                         | <b>Orion Floes</b>                                                                  | https:/            |
| nbclassic                     | http://jupyter.org                                                                  | https:/            |
| nbclient                      | https://jupyter.org                                                                 | https:/            |
| nbconvert                     | https://jupyter.org                                                                 | https:/            |
| nbformat                      | http://jupyter.org                                                                  | https:/            |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https:/            |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https:/            |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/            |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https:/            |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https:/            |
| networkx                      | https://networkx.org                                                                | https:/            |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https:/            |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https:/            |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https:/            |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https:/            |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https:/            |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/            |
| nodejs                        | https://nodejs.org/en/                                                              | https:/            |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https:/            |
| notebook                      | http://jupyter.org                                                                  | https:/            |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https:/            |
| notebook_shim                 | http://jupyter.org                                                                  | https:/            |
| numba                         | https://numba.pydata.org                                                            | https:/            |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https:/            |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https:/            |
| numpy                         | https://numpy.org                                                                   | https:/            |
| numpy-base                    | https://numpy.org                                                                   | https:/            |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/            |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| Name of Project               | Website                                                                             |                    |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              |                    |
| Oat++                         | https://oatpp.io/                                                                   |                    |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                |                    |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  |                    |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             |                    |
| olefile                       | https://www.decalage.info/python/olefileio                                          |                    |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               |                    |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        |                    |
| OpenFF                        | https://openforcefield.org/                                                         |                    |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             |                    |
| openff-forcefields            | https://openforcefield.org                                                          |                    |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                |                    |
| openff-models                 | https://github.com/openforcefield/openff-models                                     |                    |
| openff-toolkit                | https://openforcefield.org                                                          |                    |
| openff-toolkit-base           | https://openforcefield.org                                                          |                    |
| openff-units                  | https://github.com/openforcefield/openff-units                                      |                    |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  |                    |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               |                    |
| openldap                      | https://www.openldap.org/software/repo.html                                         |                    |
| OpenMM                        | https://openmm.org                                                                  |                    |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           |                    |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          |                    |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          |                    |
| openssl                       | https://www.openssl.org                                                             |                    |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              |                    |
| OptKing                       | https://github.com/psi-rking/optking                                                |                    |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   |                    |
| overrides                     | https://github.com/mkorpela/overrides                                               |                    |
| packaging                     | https://github.com/pypa/packaging                                                   |                    |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               |                    |
| pandas                        | https://pandas.pydata.org                                                           |                    |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 |                    |
| Name of Project               | Website                                                                             | License            |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https://           |
| pango                         | https://pango.gnome.org                                                             | https://           |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https://           |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https://           |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https://           |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https://           |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https://           |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https://           |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https://           |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https://           |
| pcre                          | https://www.pcre.org                                                                | https://           |
| pcre2                         | https://www.pcre.org                                                                | https://           |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https://           |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https://           |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https://           |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https://           |
| pgio                          | https://github.com/jackc/pgio                                                       | https://           |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https://           |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https://           |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https://           |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https://           |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https://           |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https://           |
| Pillow                        | https://python-pillow.org                                                           | https://           |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https://           |
| pip                           | https://pip.pypa.io/                                                                | https://           |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https://           |
| pixman                        | https://pixman.org                                                                  | https://           |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https://           |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https://           |
| plotly                        | https://plotly.com/python/                                                          | https://           |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https://           |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https://           |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https://           |
| pooch                         | https://github.com/fatiando/pooch                                                   | https://           |
| pox                           | https://github.com/uqfoundation/pox                                                 | https://           |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https://           |
| pq                            | https://github.com/lib/pq                                                           | https://           |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https://           |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https://           |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https://           |
| protobuf                      | https://google.golang.org/protobuf                                                  | https://           |
| psi4                          | https://psicode.org                                                                 | https://           |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https://           |
| psycopg2                      | https://psycopg.org/                                                                | https://           |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https://           |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https://           |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https://           |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http://            |
| Name of Project               | Website                                                                             | License            |
| py                            | https://py.readthedocs.io/en/latest/                                                |                    |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             |                    |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   |                    |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           |                    |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  |                    |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 |                    |
| pycosat                       | https://github.com/conda/pycosat                                                    |                    |
| pycparser                     | https://github.com/eliben/pycparser                                                 |                    |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 |                    |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           |                    |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                |                    |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                |                    |
| Pygments                      | https://pygments.org                                                                |                    |
| pygraphviz                    | https://pygraphviz.github.io                                                        |                    |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            |                    |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        |                    |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  |                    |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   |                    |
| pymbar                        | https://pymbar.org                                                                  |                    |
| pyOpenSSL                     | https://pyopenssl.org/                                                              |                    |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    |                    |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    |                    |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 |                    |
| pysam                         | https://github.com/pysam-developers/pysam                                           |                    |
| PySocks                       | https://github.com/Anorov/PySocks                                                   |                    |
| pytables                      | https://www.pytables.org                                                            |                    |
| python                        | https://www.python.org/                                                             |                    |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          |                    |
| python-constraint             | https://github.com/python-constraint/python-constraint                              |                    |
| python-dateutil               | https://dateutil.readthedocs.io                                                     |                    |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         |                    |
| python-ldap                   | https://www.python-ldap.org/                                                        |                    |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            |                    |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 |                    |
| pytz                          | https://pythonhosted.org/pytz                                                       |                    |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   |                    |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  |                    |
| PyYAML                        | https://pyyaml.org/                                                                 |                    |
| pyyml                         | No longer available                                                                 |                    |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             |                    |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               |                    |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  |                    |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        |                    |
| ramda                         | https://github.com/ramda/ramda                                                      |                    |
| rapidjson                     | https://rapidjson.org/                                                              |                    |
| rdkit                         | https://www.rdkit.org                                                               |                    |
| re2                           | https://github.com/google/re2                                                       |                    |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             |                    |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             |                    |
| Name of Project               | Website                                                                             | License            |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https://           |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https://           |
| reportlab                     | https://www.reportlab.com                                                           | https://           |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https://           |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https://           |
| requests                      | https://requests.readthedocs.io                                                     | https://           |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https://           |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https://           |
| resumable                     | https://github.com/stevvooe/resumable                                               | https://           |
| retrying                      | https://github.com/rholder/retrying                                                 | https://           |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https://           |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https://           |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https://           |
| rich                          | Orion Floes                                                                         | https://           |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https://           |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https://           |
| rsa                           | https://stuvel.eu/rsa                                                               | https://           |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https://           |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https://           |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https://           |
| sasl                          | https://mellium.im/sasl                                                             | https://           |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https://           |
| scikit-image                  | https://scikit-image.org                                                            | https://           |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https://           |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https://           |
| scipy                         | https://scipy.org                                                                   | https://           |
| seaborn                       | https://seaborn.pydata.org                                                          | https://           |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https://           |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https://           |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https://           |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https://           |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https://           |
| sh                            | https://github.com/amoffat/sh                                                       | https://           |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https://           |
| simint                        | https://www.bennyp.org/research/simint/                                             | https://           |
| six                           | https://github.com/benjaminp/six                                                    | https://           |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https://           |
| snappy                        | https://github.com/google/snappy                                                    | https://           |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https://           |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https://           |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https://           |
| spglib                        | Orion Floes                                                                         | https://           |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https://           |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https://           |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https://           |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https://           |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https://           |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https://           |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https://           |
| Name of Project               | Website                                                                             |                    |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          |                    |
| sqlite                        | https://sqlite.org/index.html                                                       |                    |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            |                    |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             |                    |
| starfile                      | https://github.com/alisterburt/starfile                                             |                    |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          |                    |
| structlog                     | https://www.structlog.org/                                                          |                    |
| svglib                        | https://github.com/deeplook/svglib                                                  |                    |
| sympy                         | https://sympy.org                                                                   |                    |
| tables                        | https://www.pytables.org/                                                           |                    |
| tabulate                      | https://github.com/astanin/python-tabulate                                          |                    |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                |                    |
| tenacity                      | https://github.com/jd/tenacity                                                      |                    |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           |                    |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           |                    |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           |                    |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            |                    |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             |                    |
| tensorflow-io-gcs-filesystem  | Orion Floes                                                                         |                    |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           |                    |
| termcolor                     | https://github.com/hugovk/termcolor                                                 |                    |
| terminado                     | https://github.com/jupyter/terminado                                                |                    |
| testpath                      | https://github.com/jupyter/testpath                                                 |                    |
| textangular                   | https://github.com/fraywing/textAngular                                             |                    |
| tf_keras                      | Orion Floes                                                                         |                    |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             |                    |
| three                         | https://github.com/mrdoob/three.js                                                  |                    |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                |                    |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  |                    |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             |                    |
| tk                            | https://www.tcl.tk/                                                                 |                    |
| toml                          | https://github.com/toml-lang/toml                                                   |                    |
| tomli                         | https://github.com/hukkin/tomli                                                     |                    |
| toolz                         | https://github.com/pytoolz/toolz                                                    |                    |
| torch                         | https://pytorch.org/                                                                |                    |
| tornado                       | https://www.tornadoweb.org                                                          |                    |
| tqdm                          | https://github.com/tqdm/tqdm                                                        |                    |
| tracy                         | https://github.com/gear-genomics/tracy                                              |                    |
| traitlets                     | https://github.com/ipython/traitlets                                                |                    |
| triton                        | https://github.com/openai/triton/                                                   |                    |
| truststore                    | Orion Floes                                                                         |                    |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               |                    |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             |                    |
| twine                         | https://github.com/pypa/twine                                                       |                    |
| twinj uuid                    | https://github.com/twinj/uuid                                                       |                    |
| types                         | https://github.com/babel/babel                                                      |                    |
| typescript                    | https://github.com/Microsoft/TypeScript                                             |                    |
| typing                        | https://github.com/python/typing                                                    |                    |
| typing_extensions             | https://github.com/python/typing_extensions                                         |                    |
| tzdata                        | https://github.com/python/tzdata                                                    |                    |
| Name of Project               | Website                                                                             | License            |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | MIT License        |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | MIT License        |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | MIT License        |
| uritools                      | https://github.com/tkem/uritools/                                                   | MIT License        |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | MIT License        |
| vine                          | https://github.com/celery/vine                                                      | BSD License        |
| vue                           | https://github.com/vuejs/vue                                                        | MIT License        |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | MIT License        |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | BSD License        |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | Apache License 2.0 |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | BSD License        |
| westpa                        | Orion Floes                                                                         | MIT License        |
| wheel                         | https://github.com/pypa/wheel                                                       | MIT License        |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | BSD License        |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | BSD License        |
| wsutil                        | https://github.com/yhat/wsutil                                                      | MIT License        |
| x/lint                        | https://golang.org/x/lint                                                           | BSD License        |
| x/mod                         | https://golang.org/x/mod/semver                                                     | BSD License        |
| x/net                         | https://golang.org/x/net                                                            | BSD License        |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | BSD License        |
| x/sys                         | https://golang.org/x/sys                                                            | BSD License        |
| x/text                        | https://golang.org/x/text                                                           | BSD License        |
| x/tools                       | https://golang.org/x/tools                                                          | BSD License        |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | BSD License        |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                               | Apache License 2.0 |
| xlrd                          | https://github.com/python-excel/xlrd                                                | BSD License        |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | MIT License        |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | MIT License        |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | MIT License        |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | MIT License        |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | MIT License        |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | MIT License        |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | MIT License        |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | MIT License        |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | MIT License        |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | MIT License        |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | MIT License        |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | MIT License        |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | MIT License        |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | MIT License        |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | BSD License        |
| xz                            | https://github.com/ulikunitz/xz                                                     | BSD License        |
| yaml                          | https://pyyaml.org/                                                                 | MIT License        |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  | MIT License        |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | Apache License 2.0 |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | Apache License 2.0 |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | MIT License        |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | MIT License        |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | Commercial         |
| Name of Project               | Website                                                                             | License            |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                |
| zap                           | https://go.uber.org/zap                                                             | https:             |
| zipp                          | https://github.com/jaraco/zipp                                                      | https:             |
| zlib                          | https://zlib.net/                                                                   | https:             |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https:             |
| zstd                          | https://facebook.github.io/zstd/                                                    | https:             |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:             |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:             |

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
→notice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

```
(continues on next page)
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

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

# A

```
AddCurveSeqment
   OEDepict:: OE2DPath, 178
AddLineSegment
   OEDepict:: OE2DPath, 179
AddStartPoint
   OEDepict:: OE2DPath, 179
AddSVGClass
   OEDepict:: OESVGGroup, 373
```

# C

```
Clear
   OEDepict:: OEAlignmentResult, 192
   OEDepict:: OEImage, 259
   OEDepict:: OEImageBase, 266
   OEDepict:: OEImageFrame, 285
Constructors
   OEDepict:: OE2DAtomDisplay, 107
   OEDepict:: OE2DBondDisplay, 116
   OEDepict:: OE2DMolDisplay, 122
   OEDepict:: OE2DMolDisplayOptions, 130
   OEDepict:: OE2DPath, 176
   OEDepict:: OE2DPathPoint, 181
   OEDepict:: OE2DPoint, 182
   OEDepict:: OEAlignmentOptions, 185
   OEDepict:: OEAlignmentResult, 191
   OEDepict:: OEAtomSVGAtomIdxMarkup,
       195
   OEDepict:: OEAtomSVGNoMarkup, 198
   OEDepict:: OEAtomSVGResidueMarkup,
       199
   OEDepict:: OEBondSVGBondIdxMarkup,
       202
   OEDepict:: OEBondSVGNoMarkup, 204
   OEDepict:: OEDisplayAtomIdx, 205
   OEDepict:: OEDisplayAtomMapIdx, 206
   OEDepict:: OEDisplayBondIdx, 208
   OEDepict:: OEDisplayNoAtomProp, 209
   OEDepict:: OEDisplayNoBondProp, 210
   OEDepict:: OEFont, 211
   OEDepict:: OEHighlightBase, 219
```

OEDepict:: OEHighlightByBallAndStick,  $221$ OEDepict:: OEHighlightByCogwheel, 225 OEDepict:: OEHighlightByColor, 232 OEDepict:: OEHighlightByLasso, 236 OEDepict:: OEHighlightByStick, 243 OEDepict:: OEHighlightLabel, 248 OEDepict:: OEHighlightOverlayBase, 253 OEDepict::OEHighlightOverlayByBallAndStick, 255 OEDepict:: OEImage, 258 OEDepict:: OEImageBase, 266 OEDepict:: OEImageFileBase, 282 OEDepict:: OEImageFileCreatorBase, 283 OEDepict:: OEImageFrame, 285 OEDepict:: OEImageGrid, 292 OEDepict:: OEImageTable, 297 OEDepict:: OEImageTableOptions, 305 OEDepict:: OELegendLayout, 320 OEDepict:: OELegendLayoutOptions, 321 OEDepict:: OEMultiPageImageFile, 326 OEDepict:: OENearestAtom, 330 OEDepict:: OENearestBond, 331 OEDepict:: OEPen, 332 OEDepict:: OEPrepareDepictionOptions, 342 OEDepict:: OEReport, 345 OEDepict:: OEReportOptions, 361 OEDepict:: OESVGClass, 372 OEDepict:: OESVGGroup, 373 CreateCopy OEDepict:: OE2DAtomDisplay, 107 OEDepict:: OE2DBondDisplay, 117 OEDepict:: OE2DMolDisplay, 124 OEDepict:: OEAlignmentResult, 192 OEDepict:: OEAtomSVGAtomIdxMarkup, 196 OEDepict:: OEAtomSVGMarkupBase, 197 OEDepict:: OEAtomSVGNoMarkup, 198 OEDepict:: OEAtomSVGResidueMarkup,

```
200
   OEDepict:: OEBondSVGBondIdxMarkup,
       202
   OEDepict:: OEBondSVGMarkupBase, 203
   OEDepict:: OEBondSVGNoMarkup, 205
   OEDepict:: OEDisplayAtomIdx, 206
   OEDepict:: OEDisplayAtomMapIdx, 207
   OEDepict:: OEDisplayAtomPropBase, 207
   OEDepict:: OEDisplayBondIdx, 208
   OEDepict:: OEDisplayBondPropBase, 209
   OEDepict:: OEDisplayNoAtomProp, 210
   OEDepict:: OEDisplayNoBondProp, 210
   OEDepict:: OEHighlightBase, 220
   OEDepict:: OEHighlightByBallAndStick,
       221
   OEDepict:: OEHighlightByCogwheel, 226
   OEDepict:: OEHighlightByColor, 233
   OEDepict:: OEHighlightByLasso, 237
   OEDepict:: OEHighlightByStick, 244
   OEDepict:: OEImageFileCreatorBase,
       283
CreateImage
   OEDepict:: OEImageFileCreatorBase,
       283
```

# D

depict.py Example Code, 60 DrawArc OEDepict:: OEImage, 259 OEDepict:: OEImageBase, 267 OEDepict:: OEImageFrame, 285 DrawCircle OEDepict:: OEImage, 260 OEDepict:: OEImageBase, 268 OEDepict:: OEImageFrame, 286 DrawCubicBezier OEDepict:: OEImage, 260 OEDepict:: OEImageBase, 269 OEDepict:: OEImageFrame, 286 DrawLine OEDepict:: OEImage, 261 OEDepict:: OEImageBase, 269 OEDepict:: OEImageFrame, 287 DrawPath OEDepict:: OEImage, 261 OEDepict:: OEImageBase, 270 OEDepict:: OEImageFrame, 287 DrawPie OEDepict:: OEImage, 262 OEDepict:: OEImageBase, 271 OEDepict:: OEImageFrame, 288 DrawPoint OEDepict:: OEImage, 262

```
OEDepict:: OEImageBase, 273
   OEDepict:: OEImageFrame, 288
DrawPolygon
   OEDepict:: OEImage, 263
   OEDepict:: OEImageBase, 273
   OEDepict:: OEImageFrame, 289
DrawQuadraticBezier
   OEDepict:: OEImage, 263
   OEDepict:: OEImageBase, 274
   OEDepict:: OEImageFrame, 289
DrawRectangle
   OEDepict:: OEImage, 264
   OEDepict:: OEImageBase, 275
   OEDepict:: OEImageFrame, 290
DrawText
   OEDepict:: OEImage, 264
   OEDepict:: OEImageBase, 276
   OEDepict:: OEImageFrame, 290
   OEDepict:: OEImageTable, 297
DrawTriangle
   OEDepict:: OEImage, 265
   OEDepict:: OEImageBase, 277
   OEDepict:: OEImageFrame, 291
```

# Е

```
Example Code
   depict.py, 60
   match2img.py, 63
   mcsalign2d.py, 68
   mdlquery2img.py,71
   mdlreaction2img.py,75
   mol2img.py,78
   mols2img.py, 84
   mols2pdf.py, 90
   ringdict2pdf.py,93
   smartsalign2d.py, 96
   viewmdlsearch.py, 100
```

# G

```
GetAddDepictionHydrogens
   OEDepict:: OEAlignmentOptions, 186
   OEDepict:: OEPrepareDepictionOptions,
       342
GetAlignment
   OEDepict:: OEFont, 213
GetAromaticStyle
   OEDepict:: OE2DMolDisplayOptions, 132
GetAtom
   OEDepict:: OEAtomDisplayBase, 194
   OEDepict:: OENearestAtom, 330
GetAtomColor
   OEDepict:: OE2DMolDisplayOptions, 132
GetAtomColorStyle
   OEDepict:: OE2DMolDisplayOptions, 132
```

GetAtomDisplay OEDepict:: OE2DMolDisplay, 124 GetAtomDisplays OEDepict:: OE2DMolDisplay, 124 GetAtomExternalHighlight OEDepict:: OEHighlightByColor, 233 GetAtomExternalHighlightRatio OEDepict:: OEHighlightByStick, 244 GetAtomLabelFont OEDepict:: OE2DMolDisplayOptions, 132 GetAtomLabelFontScale OEDepict:: OE2DMolDisplayOptions, 133 GetAtomLabelMonochrome OEDepict::OEHighlightByBallAndStick, GetBondPropertyFunctor 221 OEDepict:: OEHighlightByCogwheel, 226 OEDepict:: OEHighlightByLasso, 237 OEDepict:: OEHighlightByStick, 244 OEDepict::OEHighlightOverlayByBallAndStiOKDepict::OE2DMolDisplayOptions, 135 255 GetAtomPropertyFunctor OEDepict:: OE2DMolDisplayOptions, 133 GetAtomPropLabelFont OEDepict:: OE2DMolDisplayOptions, 133 GetAtomPropLabelFontScale OEDepict:: OE2DMolDisplayOptions, 133 GetAtoms OEDepict:: OEAlignmentResult, 192 GetAtomStereoStyle OEDepict:: OE2DMolDisplayOptions, 134 GetAtomSVGMarkupFunctor OEDepict:: OE2DMolDisplayOptions, 132 GetAtomVisibilityFunctor OEDepict:: OE2DMolDisplayOptions, 134 GetBackColor OEDepict:: OEPen, 333 GetBackgroundColor OEDepict:: OE2DMolDisplayOptions, 134 GetBallRadiusScale OEDepict:: OEHighlightByBallAndStick, 221 OEDepict:: OEHighlightByCogwheel, 226 OEDepict::OEHighlightOverlayByBallAndStiOEDepict::OEImageTableOptions, 307 255 GetBgnPen OEDepict:: OE2DBondDisplay, 117 GetBodies OEDepict:: OEReport, 346 GetBody OEDepict:: OEReport, 347 GetBodyCell OEDepict:: OEImageTable, 298 GetBodyCells OEDepict:: OEReportOptions, 362 OEDepict:: OEImageTable, 298

GetBond OEDepict:: OEBondDisplayBase, 201 OEDepict:: OENearestBond, 331 GetBondColorStyle OEDepict:: OE2DMolDisplayOptions, 134 GetBondDisplay OEDepict:: OE2DMolDisplay, 125 GetBondDisplays OEDepict:: OE2DMolDisplay, 125 GetBondLineAtomLabelGapScale OEDepict:: OE2DMolDisplayOptions, 135 GetBondLineGapScale OEDepict:: OE2DMolDisplayOptions, 135 OEDepict:: OE2DMolDisplayOptions, 136 GetBondPropLabelFont OEDepict:: OE2DMolDisplayOptions, 135 GetBondPropLabelFontScale GetBonds OEDepict:: OEAlignmentResult, 192 GetBondStereoStyle OEDepict:: OE2DMolDisplayOptions, 136 GetBondSVGMarkupFunctor OEDepict:: OE2DMolDisplayOptions, 136 GetBondWidthScaling OEDepict:: OE2DMolDisplayOptions, 136 GetBoundingBoxPen OEDepict:: OEHighlightLabel, 250 GetButtonFont OEDepict:: OELegendLayoutOptions, 322 GetButtonHeightScale OEDepict:: OELegendLayoutOptions, 322 GetButtonPen OEDepict:: OELegendLayoutOptions, 322 GetButtonWidthScale OEDepict:: OELegendLayoutOptions, 322 GetCell OEDepict:: OEImageGrid, 293 OEDepict:: OEImageTable, 300 OEDepict:: OEReport, 347 GetCellBorderPen GetCellColor OEDepict:: OEImageTableOptions, 307 GetCellFont OEDepict:: OEImageTableOptions, 307 GetCellGap OEDepict:: OEImageGrid, 293 OEDepict:: OEReportOptions, 362 GetCellHeight OEDepict:: OEImageGrid, 293 OEDepict:: OEReport, 348

GetCells OEDepict:: OEImageGrid, 294 OEDepict:: OEImageTable, 300 OEDepict:: OEReport, 348 GetCellWidth OEDepict:: OEImageGrid, 294 OEDepict:: OEReport, 348 OEDepict:: OEReportOptions, 363 GetCharge OEDepict:: OE2DAtomDisplay, 107 GetClassName OEDepict:: OEAtomSVGAtomIdxMarkup, 196 OEDepict:: OEAtomSVGMarkupBase, 197 OEDepict:: OEAtomSVGNoMarkup, 198 OEDepict:: OEAtomSVGResidueMarkup, 200 OEDepict:: OEBondSVGBondIdxMarkup, 202 OEDepict:: OEBondSVGMarkupBase, 204 OEDepict:: OEBondSVGNoMarkup, 205 GetClearCoords OEDepict:: OEAlignmentOptions, 186 OEDepict:: OEPrepareDepictionOptions, 343 GetColor OEDepict:: OEFont, 213 OEDepict:: OEHighlightByBallAndStick, 222 OEDepict:: OEHighlightByCogwheel, 227 OEDepict:: OEHighlightByColor, 233 OEDepict:: OEHighlightByLasso, 238 OEDepict:: OEHighlightByStick, 245 GetColors OEDepict:: OEHighlightOverlayBase, 254 GetColorStyle OEDepict:: OELegendLayoutOptions, 322 GetConsiderAtomLabelBoundingBox OEDepict:: OEHighlightByLasso, 237 GetCoords OEDepict:: OE2DAtomDisplay, 108 GetDataType OEDepict:: OE2DMolDisplay, 126 OEDepict:: OEAtomDisplayBase, 193 OEDepict:: OEBondDisplayBase, 200 OEDepict:: OEMolDisplayBase, 326 GetDefaultBondPen OEDepict:: OE2DMolDisplayOptions, 137 GetDepictOrientation OEDepict:: OEPrepareDepictionOptions, 343 GetDisplayPos OEDepict:: OE2DBondDisplay, 117

GetDisplayPosition OEDepict:: OENearestAtom, 330 OEDepict:: OENearestBond, 331 GetDisplayType OEDepict:: OE2DBondDisplay, 118 GetDist OEDepict:: OENearestAtom, 330 OEDepict:: OENearestBond, 331 GetEnd OEDepict:: OE2DPath, 180 GetEndPen OEDepict:: OE2DBondDisplay, 118 GetExplicitAtomLabelAngle OEDepict:: OE2DMolDisplayOptions, 137 GetExtension OEDepict:: OEImageFileBase, 282 OEDepict:: OEImageFileCreatorBase, 283 GetFamily OEDepict:: OEFont, 213 GetFill OEDepict:: OEPen, 333 GetFixedCoords OEDepict:: OEAlignmentOptions, 187 GetFont OEDepict:: OEHighlightLabel, 250 GetFontScale OEDepict:: OEHighlightLabel, 251 GetFooter OEDepict:: OEReport, 351 GetFooterHeight OEDepict:: OEReport, 352 OEDepict:: OEReportOptions, 363 GetFooters OEDepict:: OEReport, 352 GetFooterWidth OEDepict:: OEReport, 352 OEDepict:: OEReportOptions, 363 GetForeColor OEDepict:: OEPen, 334 GetGlobalOffset OEDepict:: OEImageBase, 278 GetGroupId OEDepict:: OEAtomSVGAtomIdxMarkup, 196 OEDepict:: OEAtomSVGMarkupBase, 197 OEDepict:: OEAtomSVGNoMarkup, 198 OEDepict:: OEAtomSVGResidueMarkup, 200 OEDepict:: OEBondSVGBondIdxMarkup, 202 OEDepict:: OEBondSVGMarkupBase, 204 OEDepict:: OEBondSVGNoMarkup, 205 GetHCount

OEDepict:: OE2DAtomDisplay, 108 GetHeader OEDepict:: OEReport, 353 GetHeaderCell OEDepict:: OEImageTable, 302 GetHeaderCells OEDepict:: OEImageTable, 302 GetHeaderColor OEDepict:: OEImageTableOptions, 307 GetHeaderFont OEDepict:: OEImageTableOptions, 308 GetHeaderHeight OEDepict:: OEReport, 353 OEDepict:: OEReportOptions, 363 GetHeaders OEDepict:: OEReport, 354 GetHeaderWidth OEDepict:: OEReport, 354 OEDepict:: OEReportOptions, 363 GetHeight OEDepict:: OE2DMolDisplay, 126 OEDepict:: OE2DMolDisplayOptions, 137 OEDepict:: OEImage, 265 OEDepict:: OEImageBase, 279 OEDepict:: OEImageFrame, 291 GetHPosition OEDepict:: OE2DAtomDisplay, 109 GetHydrogenStyle OEDepict:: OE2DMolDisplayOptions, 137 GetHyperlink OEDepict:: OEFont, 213 GetId OEDepict:: OESVGGroup, 373 GetInnerContour OEDepict:: OEHighlightByCogwheel, 227 GetInteractiveStyle OEDepict:: OELegendLayoutOptions, 322 GetLabel OEDepict:: OE2DAtomDisplay, 109 GetLabelFont OEDepict:: OE2DAtomDisplay, 110 GetLassoScale OEDepict:: OEHighlightByLasso, 238 GetLayer OEDepict:: OE2DMolDisplay, 126 GetLayoutStyle OEDepict:: OELegendLayoutOptions, 323 GetLegendArea OEDepict:: OELegendLayout, 320 GetLegendBoxPen OEDepict:: OELegendLayoutOptions, 323 GetLineCap OEDepict:: OEPen, 334 GetLineJoin

OEDepict:: OEPen, 334 GetLineStipple OEDepict:: OEPen, 334 GetLineWidth OEDepict:: OEPen, 335 GetLineWidthScale OEDepict:: OEHighlightByCogwheel, 227 OEDepict:: OEHighlightByColor, 233 OEDepict:: OEHighlightByLasso, 238 GetMargin OEDepict:: OE2DMolDisplayOptions, 138 OEDepict:: OEImageGrid, 295 OEDepict:: OEImageTableOptions, 308 OEDepict:: OELegendLayoutOptions, 323 GetMass OEDepict:: OE2DAtomDisplay, 110 GetMaxAllowedAtomPairClashes OEDepict:: OEAlignmentOptions, 187 GetMaxBondRotations OEDepict:: OEAlignmentOptions, 187 GetMaxPatternMatches OEDepict:: OEAlignmentOptions, 187 GetMinFontSize OEDepict:: OEImageBase, 279 GetMolecule OEDepict:: OEMolDisplayBase, 326 GetName OEDepict:: OESVGClass, 373 GetOffset OEDepict:: OEImageFrame, 292 GetOptions OEDepict:: OE2DMolDisplay, 126 OEDepict:: OEImageTable, 303 OEDepict:: OELegendLayout, 320 OEDepict:: OEReport, 355 GetOrientation OEDepict:: OEMultiPageImageFile, 327 GetPage OEDepict:: OEMultiPageImageFile, 328 OEDepict:: OEReport, 355 GetPageHeight OEDepict:: OEMultiPageImageFile, 328 OEDepict:: OEReport, 355 OEDepict:: OEReportOptions, 364 GetPageMargin OEDepict:: OEReportOptions, 364 GetPages OEDepict:: OEMultiPageImageFile, 329 OEDepict:: OEReport, 355 GetPageWidth OEDepict:: OEMultiPageImageFile, 329 OEDepict:: OEReport, 355 OEDepict:: OEReportOptions, 364 GetPen

OEDepict:: OEHighlightByLasso, 238 GetPerceiveBondStereo OEDepict:: OEPrepareDepictionOptions,  $343$ GetPoint OEDepict:: OE2DPathPoint, 182 GetPoints OEDepict:: OE2DPath, 180 GetPointType OEDepict:: OE2DPathPoint, 182 GetPosition OEDepict:: OEHighlightByLasso, 238 GetProperty OEDepict:: OE2DAtomDisplay, 110 OEDepict:: OE2DBondDisplay, 118 GetPropertyFont OEDepict:: OE2DAtomDisplay, 111 OEDepict:: OE2DBondDisplay, 118 GetPropertyOffset OEDepict:: OE2DAtomDisplay, 111 OEDepict:: OE2DBondDisplay, 119 GetProtectiveGroupLabelFont OEDepict:: OE2DMolDisplayOptions, 138 GetProtectiveGroupStyle OEDepict:: OE2DMolDisplayOptions, 138 GetRadical OEDepict:: OE2DAtomDisplay, 111 GetRMSD OEDepict:: OEAlignmentResult, 193 GetRMSDCutoff OEDepict:: OEAlignmentOptions, 188 GetRotateAroundBonds OEDepict:: OEAlignmentOptions, 188 GetRotationAngle OEDepict:: OEFont, 213 GetScale OEDepict:: OE2DMolDisplay, 127 OEDepict:: OE2DMolDisplayOptions, 139 GetSize OEDepict:: OEFont, 214 GetStart OEDepict:: OE2DPath, 180 GetStickWidthScale OEDepict::OEHighlightByBallAndStick, HasHeader 222 OEDepict:: OEHighlightByCogwheel, 227 OEDepict:: OEHighlightByStick, 245 OEDepict::OEHighlightOverlayByBallAnd\$dsIGdoel 256 GetStippleFactor OEDepict:: OEPen, 335 GetStubColumnCell OEDepict:: OEImageTable, 303 GetStubColumnCells

OEDepict:: OEImageTable, 304 GetStubColumnColor OEDepict:: OEImageTableOptions, 308 GetStubColumnFont OEDepict:: OEImageTableOptions, 308 GetStyle OEDepict:: OEFont, 214 GetSuperAtomLabelFont OEDepict:: OE2DMolDisplayOptions, 139 GetSuperAtomStyle OEDepict:: OE2DMolDisplayOptions, 139 GetSuppressHydrogens OEDepict:: OEAlignmentOptions, 188 OEDepict:: OEPrepareDepictionOptions, 343 GetSVGClass OEDepict:: OEImageBase, 279 GetSVGGroup OEDepict:: OEImageBase, 279 GetSVGGroups OEDepict:: OEImageBase, 280 GetText OEDepict:: OEHighlightLabel, 251 GetTitleFont OEDepict:: OE2DMolDisplayOptions, 139 GetTitleFontScale OEDepict:: OE2DMolDisplayOptions, 140 GetTitleHeight OEDepict:: OE2DMolDisplayOptions, 140 GetTitleLocation OEDepict:: OE2DMolDisplayOptions, 140 GetWidth OEDepict:: OE2DMolDisplay, 127 OEDepict:: OE2DMolDisplayOptions, 140 OEDepict:: OEImage, 266 OEDepict:: OEImageBase, 279 OEDepict:: OEImageFrame, 292 GetX OEDepict:: OE2DPoint, 184 GetY OEDepict:: OE2DPoint, 184

# H

OEDepict:: OEImageTableOptions, 309 HasHyperlink OEDepict:: OEFont, 214 OEDepict:: OE2DAtomDisplay, 112 HasProperty OEDepict:: OE2DAtomDisplay, 112 OEDepict:: OE2DBondDisplay, 119 HasProtectiveGroupStyle OEDepict:: OE2DMolDisplayOptions, 141

```
HasStubColumn
   OEDepict:: OEImageTableOptions, 309
\mathsf{I}IsBodyPage
   OEDepict:: OEReport, 356
IsClosed
   OEDepict:: OE2DPath, 180
IsDataType
   OEDepict:: OE2DMolDisplay, 127
   OEDepict:: OEAtomDisplayBase, 194
   OEDepict:: OEBondDisplayBase, 201
   OEDepict:: OEMolDisplayBase, 326
IsEmpty
   OEDepict:: OEImage, 266
IsGridPage
   OEDepict:: OEReport, 356
IsMultiPage
   OEDepict:: OEImageFileCreatorBase,
       284IsValid
   OEDepict:: OE2DMolDisplay, 127
   OEDepict:: OE2DPath, 180
   OEDepict:: OEAlignmentResult, 193
   OEDepict:: OENearestAtom, 330
   OEDepict:: OENearestBond, 331
IsVisible
   OEDepict:: OEAtomDisplayBase, 194
   OEDepict:: OEBondDisplayBase, 201
   OEDepict:: OEImageFileBase, 282
   OEDepict:: OESVGGroup, 373
```

# M

```
match2img.py
   Example Code, 63
mcsalign2d.pv
   Example Code, 68
mdlquery2imq.py
   Example Code, 71
mdlreaction2imq.py
   Example Code, 75
mol2img.py
   Example Code, 78
mols2img.py
   Example Code, 84
mols2pdf.py
   Example Code, 90
```

# N

NewBody OEDepict:: OEReport, 357 NewCell OEDepict:: OEReport, 357 NewPage

```
OEDepict:: OEMultiPageImageFile, 329
NewSVGClass
   OEDepict:: OEImageBase, 280
NewSVGGroup
   OEDepict:: OEImageBase, 280
NumAtoms
   OEDepict:: OEAlignmentResult, 193
NumBodyPages
   OEDepict:: OEReport, 358
NumBonds
   OEDepict:: OEAlignmentResult, 193
NumCols
   OEDepict:: OEImageGrid, 295
NumColsPerPage
   OEDepict:: OEReport, 358
   OEDepict:: OEReportOptions, 364
NumColumns
   OEDepict:: OEImageTable, 304
   OEDepict:: OEImageTableOptions, 309
NumGridPages
   OEDepict:: OEReport, 359
NumPages
   OEDepict:: OEMultiPageImageFile, 329
   OEDepict:: OEReport, 359
NumRows
   OEDepict:: OEImageGrid, 295
   OEDepict:: OEImageTable, 305
   OEDepict:: OEImageTableOptions, 309
NumRowsPerPage
   OEDepict:: OEReport, 359
   OEDepict:: OEReportOptions, 364
```

# $\bigcap$

```
OEDepict:: OE2DAtomDisplay, 105
   Constructors, 107
   CreateCopy, 107
   GetCharge, 107
   GetCoords, 108
   GetHCount, 108
   GetHPosition, 109
   GetLabel, 109
   GetLabelFont, 110
   GetMass, 110
   GetProperty, 110
   GetPropertyFont, 111
   GetPropertyOffset, 111
   GetRadical, 111
   HasLabel, 112
   HasProperty, 112
   operator=, 107SetCharge, 113
   SetCoords, 113
   SetHCount, 113
   SetHPosition, 113
```

SetLabel, 113 SetLabelFont, 114 SetMass, 114 SetProperty, 114 SetPropertyFont, 114 SetPropertyOffset, 115 SetRadical, 115 OEDepict:: OE2DBondDisplay, 115 Constructors, 116 CreateCopy, 117 GetBgnPen, 117 GetDisplayPos, 117 GetDisplayType, 118 GetEndPen, 118 GetProperty, 118 GetPropertyFont, 118 GetPropertyOffset, 119 HasProperty, 119 operator=, 116 SetBqnPen, 120 SetDisplayPos, 120 SetDisplayType, 120 SetEndPen, 120 SetProperty, 121 SetPropertyFont, 121 SetPropertyOffset, 121 OEDepict:: OE2DMolDisplay, 122 Constructors, 122 CreateCopy, 124 GetAtomDisplay, 124 GetAtomDisplays, 124 GetBondDisplay, 125 GetBondDisplays, 125 GetDataType, 126 GetHeight, 126 GetLayer, 126 GetOptions, 126 GetScale, 127 GetWidth, 127 IsDataType, 127 IsValid, 127 operator=, 123 OEDepict:: OE2DMolDisplayOptions, 128 Constructors, 130 GetAromaticStyle, 132 GetAtomColor, 132 GetAtomColorStyle, 132 GetAtomLabelFont, 132 GetAtomLabelFontScale, 133 GetAtomPropertyFunctor, 133 GetAtomPropLabelFont, 133 GetAtomPropLabelFontScale, 133 GetAtomStereoStyle, 134 GetAtomSVGMarkupFunctor, 132

GetAtomVisibilityFunctor, 134 GetBackgroundColor, 134 GetBondColorStyle, 134 GetBondLineAtomLabelGapScale, 135 GetBondLineGapScale, 135 GetBondPropertyFunctor, 136 GetBondPropLabelFont, 135 GetBondPropLabelFontScale, 135 GetBondStereoStyle, 136 GetBondSVGMarkupFunctor, 136 GetBondWidthScaling, 136 GetDefaultBondPen, 137 GetExplicitAtomLabelAngle, 137 GetHeight, 137 GetHydrogenStyle, 137 GetMargin, 138 GetProtectiveGroupLabelFont, 138 GetProtectiveGroupStyle, 138 GetScale, 139 GetSuperAtomLabelFont, 139 GetSuperAtomStyle, 139 GetTitleFont, 139 GetTitleFontScale, 140 GetTitleHeight, 140 GetTitleLocation, 140 GetWidth, 140 HasProtectiveGroupStyle, 141 operator=, 131 SetAromaticStyle, 141 SetAtomColor, 142 SetAtomColorStyle, 143 SetAtomLabelFont, 143 SetAtomLabelFontScale, 144 SetAtomPropertyFunctor, 148 SetAtomPropLabelFont, 145 SetAtomPropLabelFontScale, 147 SetAtomStereoStyle, 149 SetAtomSVGMarkupFunctor, 150 SetAtomVisibilityFunctor, 151 SetBackgroundColor, 152 SetBondColorStyle, 152 SetBondLineAtomLabelGapScale, 153 SetBondLineGapScale, 153 SetBondPropertyFunctor, 157 SetBondPropLabelFont, 154 SetBondPropLabelFontScale, 156 SetBondStereoStyle, 158 SetBondSVGMarkupFunctor, 159 SetBondWidthScaling, 160 SetDefaultBondPen, 160 SetDimensions, 162 SetExplicitAtomLabelAngle, 162 SetHeight, 163 SetHydrogenStyle, 164

SetMargin, 164 GetPoint, 182 SetMargins, 166 GetPointType, 182 SetProtectiveGroupLabelFont, 166 operator=, 181 SetProtectiveGroupStyle, 168 OEDepict:: OE2DPathPointType, 383 SetScale, 168 OEDepict:: OE2DPathPointType:: CurveC1, SetSuperAtomLabelFont, 169 383 SetSuperAtomStyle, 170 OEDepict:: OE2DPathPointType:: CurveC2, SetTitleFont, 171 384 SetTitleFontScale.173 OEDepict:: OE2DPathPointType:: CurveEnd, SetTitleHeight, 175 384 SetTitleLocation, 173 OEDepict:: OE2DPathPointType:: LineEnd, SetWidth, 175 384 OEDepict:: OE2DMolDisplaySetup, 374 OEDepict:: OE2DPathPointType:: Start, 384 OEDepict:: OE2DMolDisplaySetup:: All, 374 OEDepict:: OE2DPoint, 182 OEDepict:: OE2DMolDisplaySetup:: AromaticStyl@onstructors, 182 374 GetX, 184 OEDepict:: OE2DMolDisplaySetup:: AtomColorStyDetY, 184 375 operator  $\star$ , 183 OEDepict:: OE2DMolDisplaySetup:: AtomPropDispbppgrator\*=, 184 375 operator+, 183 OEDepict:: OE2DMolDisplaySetup:: AtomStereoStypegrator+=, 183 operator/, 183 376 OEDepict:: OE2DMolDisplaySetup:: BondColorStybeperator/=, 184 376 operator= $, 183$ OEDepict::OE2DMolDisplaySetup::BondPropDispbpggrator-,183 377 operator-=,  $184$ OEDepict:: OE2DMolDisplaySetup:: BondStereoStySbet,X, 184 377 SetY, 185 OEDepict::OE2DMolDisplaySetup::DefaultLi0BWedtht::OEAddBuiltInHiddenSVGClass, 504 378 OEDepict::OE2DMolDisplaySetup::HydrogenSOWDepict::OEAddBuiltInVisibleSVGClass, 379 504 OEDepict::OE2DMolDisplaySetup::Protectiv@EDepp8tyl@EAddDepictionHydrogens,504 379 OEDepict:: OEAddHighlighting, 504 OEDepict:: OE2DMolDisplaySetup:: Scale, OEDepict:: OEAddHighlightOverlay, 510 381 OEDepict:: OEAddInteractiveIcon, 511 OEDepict::OE2DMolDisplaySetup::SuperAtomGEDepict::OEAddLabel, 511 382 OEDepict:: OEAddOpenEyeIcon, 514 OEDepict::OE2DMolDisplaySetup::TitleLocaOEDepict::OEAddSVGClickEvent, 515 383 OEDepict:: OEAddSVGHover, 517 OEDepict:: OE2DPath, 176 OEDepict:: OEAddSVGToggle, 518 AddCurveSeqment, 178 OEDepict:: OEAddWatermark, 519 AddLineSeqment, 179 OEDepict:: OEAlignment, 385 AddStartPoint, 179 OEDepict:: OEAlignment:: Center, 385 Constructors, 176 OEDepict:: OEAlignment:: Default, 385 GetEnd, 180 OEDepict:: OEAlignment:: Left, 385 GetPoints, 180 OEDepict:: OEAlignment:: Right, 385 GetStart, 180 OEDepict:: OEAlignmentOptions, 185 IsClosed. 180 Constructors, 185 IsValid, 180 GetAddDepictionHydrogens, 186 operator=, 178 GetClearCoords, 186 GetFixedCoords, 187 SetClosed, 181 OEDepict:: OE2DPathPoint, 181 GetMaxAllowedAtomPairClashes, 187 Constructors, 181 GetMaxBondRotations, 187

```
GetMaxPatternMatches, 187
                                            OEDepict:: OEAtomStereoStyle:: Display:: All,
   GetRMSDCutoff. 188
                                                   393
   GetRotateAroundBonds, 188
                                            OEDepict::OEAtomStereoStyle::Display::AtomStereo,
   GetSuppressHydrogens, 188
                                                   391
   operator=, 186
                                            OEDepict::OEAtomStereoStyle::Display::CIPAtomStere
   SetAddDepictionHydrogens, 188
                                                   392
   SetClearCoords. 188
                                            OEDepict:: OEAtomStereoStyle:: Display:: Default,
   SetFixedCoords, 189
                                                   391
   SetMaxAllowedAtomPairClashes, 189
                                            OEDepict::OEAtomStereoStyle::Display::MDLStereoCent
   SetMaxBondRotations, 189
                                                   392
   SetMaxPatternMatches, 190
                                            OEDepict::OEAtomStereoStyle::HashWedgeStyle,
   SetRMSDCutoff, 190
                                                   393
   SetRotateAroundBonds, 191
                                            OEDepict::OEAtomStereoStyle::HashWedgeStyle::Defau
   SetSuppressHydrogens, 191
                                                   393
OEDepict:: OEAlignmentResult, 191
                                            OEDepict::OEAtomStereoStyle::HashWedgeStyle::Fancy,
   Clear, 192
                                                   393
   Constructors, 191
                                            OEDepict::OEAtomStereoStyle::HashWedgeStyle::Standa
                                                   393
   CreateCopy, 192
   GetAtoms, 192
                                            OEDepict:: OEAtomStereoStyle:: Hidden, 390
   GetBonds, 192
                                            OEDepict:: OEAtomSVGAtomIdxMarkup, 195
   GetRMSD, 193
                                               Constructors, 195
   IsValid, 193
                                               CreateCopy, 196
   NumAtoms, 193
                                               GetClassName, 196
   NumBonds, 193
                                               GetGroupId, 196
   operator=, 192
                                            OEDepict:: OEAtomSVGMarkupBase, 196
OEDepict:: OEAnnotateDepictionProblems,
                                               CreateCopy, 197
       519
                                               GetClassName, 197
OEDepict:: OEAnnotateValenceProblems, 520
                                               GetGroupId, 197
OEDepict:: OEAromaticStyle, 386
                                            OEDepict:: OEAtomSVGNoMarkup, 197
                                               Constructors, 198
OEDepict:: OEAromaticStyle:: Circle, 387
OEDepict:: OEAromaticStyle:: Dash, 387
                                               CreateCopy, 198
OEDepict:: OEAromaticStyle:: Default, 386
                                               GetClassName, 198
OEDepict:: OEAromaticStyle:: Kekule, 387
                                               GetGroupId, 198
OEDepict:: OEAtomColorStyle, 388
                                            OEDepict:: OEAtomSVGResidueMarkup, 198
OEDepict:: OEAtomColorStyle:: BlackCPK,
                                               Constructors, 199
       388
                                               CreateCopy, 200
OEDepict::OEAtomColorStyle::BlackMonochrome,GetClassName, 200
       388
                                               GetGroupId, 200
OEDepict::OEAtomColorStyle::Default, 388
                                           OEDepict:: OEBondColorStyle, 394
OEDepict:: OEAtomColorStyle:: WhiteCPK,
                                            OEDepict::OEBondColorStyle::ByElement,
                                                   395
       389
OEDepict::OEAtomColorStyle::WhiteMonochrOmDepict::OEBondColorStyle::Default, 394
       389
                                            OEDepict:: OEBondColorStyle:: Monochrome,
OEDepict:: OEAtomDisplayBase, 193
                                                   395
   GetAtom, 194
                                            OEDepict:: OEBondDisplayBase, 200
   GetDataType, 193
                                               GetBond, 201
   IsDataType, 194
                                               GetDataType, 200
   IsVisible, 194
                                               IsDataType, 201
   SetVisible, 195
                                               IsVisible, 201
OEDepict:: OEAtomStereoStyle, 390
                                               SetVisible, 201
OEDepict:: OEAtomStereoStyle:: Default,
                                            OEDepict:: OEBondDisplayPosition, 395
                                            OEDepict::OEBondDisplayPosition::Center,
       390
OEDepict:: OEAtomStereoStyle:: Display,
                                                   396
       391
```

OEDepict:: OEBondDisplayPosition:: Left, GetGroupId. 205 396 OEDepict::OEConfigure2DMolDisplayOptions, OEDepict:: OEBondDisplayPosition:: Right, 521 397 OEDepict:: OEConfigureColor, 522 OEDepict:: OEBondDisplayType, 397 OEDepict:: OEConfigureHighlightColor, 523 OEDepict:: OEBondDisplayType:: Any, 401 OEDepict:: OEConfigureHighlightParams, OEDepict:: OEBondDisplayType:: Aromatic, 523 401 OEDepict:: OEConfigureHighlightStyle, 524 OEDepict::OEBondDisplayType::AromaticDasbEDepict::OEConfigureImageGridNumColumns, 399 524 OEDepict::OEBondDisplayType::Double, 397 OEDepict::OEConfigureImageGridNumRows, OEDepict::OEBondDisplayType::DoubleArom, 524 400 OEDepict:: OEConfigureImageGridParams, OEDepict::OEBondDisplayType::DoubleBowTie, 525 OEDepict:: OEConfigureImageHeight, 525 399 OEDepict:: OEBondDisplayType:: Hash, 399 OEDepict:: OEConfigureImageOptions, 526 OEDepict::OEBondDisplayType::Hidden, 401 OEDepict::OEConfigureImageWidth, 526 OEDepict::OEBondDisplayType::Ouadruple, OEDepict::OEConfigureMultiPageOrientation, 398 527 OEDepict::OEBondDisplayType::Single,397 OEDepict::OEConfigureMultiPageParams, OEDepict:: OEBondDisplayType:: SingleArom, 527 400 OEDepict:: OEConfigureMultiPageSize, 527 OEDepict::OEBondDisplayType::SingleDoubl@EDepict::OEConfigurePrepareDepictionOptions, 400 528 OEDepict:: OEBondDisplayType:: Triple, 398 OEDepict:: OEConfigureReportOptions, 528 OEDepict:: OEBondDisplayType:: Wavy, 399 OEDepict:: OECreateWin32GraphicsImage, OEDepict:: OEBondDisplayType:: Wedge, 398 529 OEDepict:: OEDepict, 404 OEDepict:: OEBondStereoStyle, 402 OEDepict:: OEBondStereoStyle:: Default, OEDepict:: OEDepict:: OEBlackBoxPen, 404 402 OEDepict:: OEDepict:: OEBlackPen, 404 OEDepict:: OEBondStereoStyle:: Display, OEDepict:: OEDepict:: OEBlueBoxPen, 405 402 OEDepict:: OEDepict:: OEBluePen, 405 OEDepict::OEBondStereoStyle::Display::Al@EDepict::OEDepict::OEDarkBackgroundColor, 403 404 OEDepict::OEBondStereoStyle::Display::Bo0EBebreb::OEDepict::OEDefaultFont.405 403 OEDepict:: OEDepict:: OEGreenBoxPen, 405 OEDepict::OEBondStereoStyle::Display::CI**DEDedStereO**EDepict::OEGreenPen, 405 403 OEDepict::OEDepict::OELightBackgroundColor, OEDepict:: OEBondStereoStyle:: Display:: Default, 404 OEDepict::OEDepict::OELightGreyBoxPen, 403 OEDepict:: OEBondStereoStyle:: Hidden, 402 406 OEDepict:: OEBondSVGBondIdxMarkup, 201 OEDepict:: OEDepict:: OELightGreyPen, 406 OEDepict:: OEDepict:: OERedBoxPen, 406 Constructors, 202 CreateCopy, 202 OEDepict:: OEDepict:: OERedPen, 406 GetClassName, 202 OEDepict:: OEDepict:: OESVGAreaPen, 407 GetGroupId, 202 OEDepict:: OEDepict:: OETransparentPen, OEDepict:: OEBondSVGMarkupBase, 203 407 CreateCopy, 203 OEDepict:: OEDepict:: OEWhiteBoxPen, 407 GetClassName. 204 OEDepict:: OEDepict:: OEWhitePen, 407 GetGroupId, 204 OEDepict:: OEDepictCoordinates, 529 OEDepict:: OEBondSVGNoMarkup, 204 OEDepict:: OEDepictGetArch, 529 Constructors, 204 OEDepict:: OEDepictGetLicensee, 529 CreateCopy, 205 OEDepict:: OEDepictGetPlatform, 529 GetClassName, 205 OEDepict:: OEDepictGetRelease, 529

```
OEDepict:: OEDepictGetSite, 529
                                            OEDepict:: OEEstimateTextWidth, 540
OEDepict:: OEDepictGetVersion, 530
                                            OEDepict:: OEFill, 410
OEDepict:: OEDepictIsLicensed, 530
                                            OEDepict:: OEFill:: Default, 410
OEDepict:: OEDepictOrientation, 407
                                            OEDepict::OEFill::Off, 410
OEDepict:: OEDepictOrientation:: Default,
                                            OEDepict:: OEFill:: On, 411
                                            OEDepict:: OEFont, 211
       408
OEDepict::OEDepictOrientation::Horizontal,
                                                Constructors, 211
       408
                                                GetAlignment, 213
OEDepict:: OEDepictOrientation:: Original,
                                                GetColor, 213
       408
                                                GetFamily, 213
OEDepict:: OEDepictOrientation:: Square,
                                                GetHyperlink, 213
       409
                                                GetRotationAngle, 213
                                                GetSize, 214
OEDepict::OEDepictOrientation::Vertical,
                                                GetStyle, 214
       409
OEDepict:: OEDisplayAtomIdx, 205
                                                HasHyperlink, 214
   Constructors, 205
                                                operator! = , 212CreateCopy, 206
                                                operator=, 212
   operator(1, 206)operator==, 212OEDepict:: OEDisplayAtomMapIdx, 206
                                                SetAlignment, 214
   Constructors, 206
                                                SetColor, 215
   CreateCopy, 207
                                                SetFamily, 215
                                                SetHyperlink, 216
   operator(), 206
OEDepict:: OEDisplayAtomPropBase, 207
                                                SetRotationAngle, 217
                                                SetSize.218
   CreateCopy, 207
   operator(1, 207)SetStyle, 218
OEDepict:: OEDisplayBondIdx, 208
                                            OEDepict:: OEFontFamily, 411
   Constructors, 208
                                            OEDepict::OEFontFamily::Arial, 411
   CreateCopy, 208
                                            OEDepict:: OEFontFamily:: Courier, 411
   operator(), 208
                                            OEDepict::OEFontFamily::Default, 411
OEDepict:: OEDisplayBondPropBase, 208
                                            OEDepict::OEFontFamily::Helvetica, 412
                                            OEDepict:: OEFontFamily:: Times, 412
   CreateCopy, 209
   operator(), 209
                                            OEDepict:: OEFontStyle, 412
OEDepict:: OEDisplayNoAtomProp, 209
                                            OEDepict:: OEFontStyle:: Bold, 413
   Constructors, 209
                                            OEDepict:: OEFontStyle:: Default, 412
   CreateCopy, 210
                                            OEDepict:: OEFontStyle:: Italic. 413
   operator(), 210
                                            OEDepict:: OEFontStyle:: Normal, 413
OEDepict:: OEDisplayNoBondProp, 210
                                            OEDepict::OEGetAverageBondLengthInDispCoords,
   Constructors, 210
                                                    540
                                            OEDepict:: OEGetBuiltInHiddenSVGClass,
   CreateCopy, 210
                                                    540
   operator(), 210
                                            OEDepict:: OEGetBuiltInVisibleSVGClass,
OEDepict:: OEDrawBorder, 530
OEDepict:: OEDrawChevronArrow, 531
                                                    540
OEDepict:: OEDrawCurvedArrow, 531
                                            OEDepict:: OEGetCenter, 541
OEDepict:: OEDrawCurvedBorder, 532
                                            OEDepict:: OEGetColor, 541
OEDepict:: OEDrawCurvedRectangle, 532
                                            OEDepict:: OEGetDefaultAtomColor, 541
OEDepict:: OEDrawEquilibriumArrow, 533
                                            OEDepict::OEGetDisplayCoords, 541
OEDepict:: OEDrawHighlighting, 533
                                            OEDepict:: OEGetHighlightColor, 542
OEDepict:: OEDrawLegendLayout, 534
                                            OEDepict:: OEGetHighlightStyle, 542
OEDepict:: OEDrawReactionArrow, 535
                                            OEDepict:: OEGetImageGridNumColumns, 542
OEDepict:: OEDrawResonanceArrow, 535
                                            OEDepict:: OEGetImageGridNumRows, 543
OEDepict:: OEDrawSVGHoverText, 536
                                            OEDepict:: OEGetImageHeight, 543
OEDepict:: OEDrawSVGToggleText, 537
                                            OEDepict:: OEGetImageWidth, 543
OEDepict:: OEDrawText, 539
                                            OEDepict:: OEGetLabelPosition, 544
OEDepict:: OEDrawTextToCenter, 539
                                            OEDepict:: OEGetMoleculeCoords, 544
```

OEDepict:: OEGetMoleculeScale, 545 SetLineWidthScale, 234 OEDepict::OEGetMultiPageOrientation, 545 OEDepict::OEHighlightByLasso, 235 OEDepict:: OEGetMultiPageSize, 545 OEDepict:: OEGetNearbyAtom, 546 OEDepict:: OEGetNearbyBond, 546 OEDepict:: OEGetNearestAtom, 547 OEDepict:: OEGetNearestBond, 547 OEDepict:: OEGetPageHeight, 547 OEDepict:: OEGetPageWidth, 548 OEDepict:: OEGetSupportedImageFileExtensions, GetPen, 238 548 OEDepict::OEGetSupportedMultiPageImageFileExtpensitons, 237 549 OEDepict:: OEHasDepictionHydrogens, 549 OEDepict:: OEHighlightBase, 219 Constructors, 219 CreateCopy, 220 OEDepict:: OEHighlightByBallAndStick, 220 SetPen, 241 Constructors, 221 CreateCopy, 221 GetAtomLabelMonochrome, 221 GetBallRadiusScale, 221 GetColor, 222 GetStickWidthScale, 222 operator= $, 221$ SetAtomLabelMonochrome, 222 SetBallRadiusScale, 222 SetColor, 223 SetStickWidthScale, 223 OEDepict:: OEHighlightByCogwheel, 224 Constructors, 225 CreateCopy, 226 GetAtomLabelMonochrome, 226 GetBallRadiusScale, 226 GetColor, 227 GetInnerContour. 227 GetLineWidthScale, 227 GetStickWidthScale, 227 operator=, 226 SetAtomLabelMonochrome, 227 SetBallRadiusScale, 228 SetColor, 228 SetInnerContour. 229 SetLineWidthScale, 230 SetStickWidthScale, 230 OEDepict:: OEHighlightByColor, 231 254 Constructors, 232 CreateCopy, 233 GetAtomExternalHighlight, 233 GetColor, 233 GetLineWidthScale, 233 operator=, 233 SetAtomExternalHighlight, 233 SetColor, 234

Constructors, 236 CreateCopy, 237 GetAtomLabelMonochrome, 237 GetColor, 238 GetConsiderAtomLabelBoundingBox, 237 GetLassoScale, 238 GetLineWidthScale, 238 GetPosition, 238 SetAtomLabelMonochrome, 239 SetColor, 241 SetConsiderAtomLabelBoundingBox, 239 SetLassoScale, 240 SetLineWidthScale, 241 SetPosition, 242 OEDepict:: OEHighlightByStick, 243 Constructors, 243 CreateCopy, 244 GetAtomExternalHighlightRatio, 244 GetAtomLabelMonochrome. 244 GetColor. 245 GetStickWidthScale, 245 operator=, 244 SetAtomExternalHighlightRatio, 245 SetAtomLabelMonochrome, 245 SetColor, 246 SetStickWidthScale, 247 OEDepict:: OEHighlightLabel, 248 Constructors, 248 GetBoundingBoxPen, 250 GetFont, 250 GetFontScale, 251 GetText, 251 SetBoundingBoxPen, 251 SetFont, 251 SetFontScale, 253 OEDepict:: OEHighlightOverlayBase, 253 Constructors, 253 GetColors. 254 SetColors, 254 OEDepict::OEHighlightOverlayByBallAndStick, Constructors, 255 GetAtomLabelMonochrome, 255 GetBallRadiusScale, 255 GetStickWidthScale, 256 operator=, 255 SetAtomLabelMonochrome, 256 SetBallRadiusScale, 256 SetStickWidthScale, 257

```
OEDepict:: OEHighlightOverlayStyle, 413
                                                Constructors, 258
OEDepict::OEHighlightOverlayStyle::BallAndStDirakuArc, 259
       414
                                                DrawCircle, 260
OEDepict:: OEHighlightOverlayStyle:: Default, DrawCubicBezier, 260
       413
                                                DrawLine, 261
OEDepict:: OEHighlightParamName, 415
                                                DrawPath, 261
OEDepict:: OEHighlightParamName:: Color,
                                                DrawPie.262
       415
                                                DrawPoint, 262
OEDepict:: OEHighlightParamName:: Style,
                                                DrawPolygon, 263
       415
                                                DrawQuadraticBezier, 263
OEDepict:: OEHighlightSetup, 416
                                                DrawRectangle, 264
OEDepict:: OEHighlightSetup:: All, 416
                                                DrawText, 264
OEDepict:: OEHighlightSetup:: Color, 416
                                                DrawTriangle, 265
OEDepict:: OEHighlightSetup:: Style, 417
                                                GetHeight, 265
OEDepict:: OEHighlightStyle, 417
                                                GetWidth, 266
OEDepict:: OEHighlightStyle:: BallAndStick,
                                                IsEmpty, 266
       417
                                                Render, 266
OEDepict::OEHighlightStyle::Cogwheel,
                                            OEDepict:: OEImageBase, 266
       418
                                                Clear, 266
OEDepict:: OEHighlightStyle:: Color, 418
                                                Constructors, 266
OEDepict:: OEHighlightStyle:: Default, 417
                                                DrawArc, 267
OEDepict:: OEHighlightStyle:: Lasso, 419
                                                DrawCircle, 268
                                                DrawCubicBezier, 269
OEDepict:: OEHighlightStyle:: Stick, 420
OEDepict:: OEHydrogenPos, 421
                                                DrawLine.269
OEDepict:: OEHydrogenPos:: East, 422
                                                DrawPath, 270
OEDepict:: OEHydrogenPos:: North, 422
                                                DrawPie.271
OEDepict:: OEHydrogenPos:: South, 422
                                                DrawPoint, 273
OEDepict:: OEHydrogenPos:: Undefined, 422
                                                DrawPolygon, 273
OEDepict:: OEHydrogenPos:: West, 423
                                                DrawQuadraticBezier, 274
OEDepict:: OEHydrogenStyle, 423
                                                DrawRectangle, 275
OEDepict:: OEHydrogenStyle:: Default, 423
                                                DrawText, 276
OEDepict:: OEHydrogenStyle:: ExplicitAll,
                                                DrawTriangle, 277
                                                GetGlobalOffset, 278
       423
OEDepict::OEHydrogenStyle::ExplicitHetero,
                                                GetHeight, 279
                                                GetMinFontSize, 279
       423
OEDepict::OEHydrogenStyle::ExplicitTerminal,GetSVGClass, 279
       424
                                                GetSVGGroup, 279
OEDepict:: OEHydrogenStyle:: Hidden, 424
                                                GetSVGGroups, 280
OEDepict:: OEHydrogenStyle:: ImplicitAll,
                                                GetWidth, 279
       425
                                                NewSVGClass, 280
OEDepict::OEHydrogenStyle::ImplicitHetero,
                                                NewSVGGroup, 280
       425
                                                PopGroup, 281
OEDepict::OEHydrogenStyle::ImplicitTerminal,PushGroup, 281
       425
                                                SetMinFontSize, 279
OEDepict:: OEIconLocation, 426
                                            OEDepict:: OEImageFileBase, 281
                                                Constructors, 282
OEDepict:: OEIconLocation:: BottomLeft,
       427
                                                GetExtension, 282
OEDepict:: OEIconLocation:: BottomRight,
                                                IsVisible, 282
       427
                                                PopGroup, 282
OEDepict:: OEIconLocation:: Default, 427
                                                PushGroup, 282
OEDepict:: OEIconLocation:: TopLeft, 427
                                                Write, 282
OEDepict:: OEIconLocation:: TopRight, 427
                                            OEDepict:: OEImageFileCreatorBase, 283
OEDepict:: OEImage, 257
                                                Constructors, 283
   Clear, 259
                                                CreateCopy, 283
```

CreateImage, 283 GetExtension. 283 IsMultiPage, 284 OEDepict:: OEImageFrame, 284 Clear, 285 Constructors, 285 DrawArc. 285 DrawCircle, 286 DrawCubicBezier, 286 DrawLine, 287 DrawPath, 287 DrawPie, 288 DrawPoint, 288 DrawPolygon, 289 DrawQuadraticBezier, 289 DrawRectangle, 290 DrawText, 290 DrawTriangle, 291 GetHeight, 291 GetOffset, 292 GetWidth, 292 OEDepict:: OEImageGrid, 292 Constructors, 292 GetCell. 293 GetCellGap, 293 GetCellHeight, 293 GetCells, 294 GetCellWidth, 294 GetMargin, 295 NumCols, 295 NumRows, 295 SetCellGap. 296 SetMargin, 296 SetMargins, 296 OEDepict:: OEImageGridParamName, 428 OEDepict:: OEImageGridParamName:: NumColumns, SetMargins, 315 428 OEDepict::OEImageGridParamName::NumRows, 428 OEDepict:: OEImageGridSetup, 428 OEDepict:: OEImageGridSetup:: All, 428 OEDepict:: OEImageGridSetup:: NumColumns, 429 OEDepict:: OEImageGridSetup:: NumRows, 429 OEDepict:: OEImageParamName, 430 OEDepict:: OEImageParamName:: Height, 430 OEDepict:: OEImageParamName:: Width, 430 OEDepict:: OEImageSetup, 430 OEDepict:: OEImageSetup:: All, 430 OEDepict:: OEImageSetup:: Height, 431 OEDepict:: OEImageSetup:: Width, 431 OEDepict:: OEImageTable, 296 Constructors, 297 DrawText, 297

GetBodyCell, 298 GetBodyCells, 298 GetCell, 300 GetCells, 300 GetHeaderCell, 302 GetHeaderCells, 302 GetOptions, 303 GetStubColumnCell, 303 GetStubColumnCells, 304 NumColumns, 304 NumRows, 305 OEDepict:: OEImageTableOptions, 305 Constructors, 305 GetCellBorderPen, 307 GetCellColor. 307 GetCellFont, 307 GetHeaderColor, 307 GetHeaderFont, 308 GetMargin, 308 GetStubColumnColor, 308 GetStubColumnFont, 308 HasHeader, 309 HasStubColumn, 309 NumColumns. 309 NumRows, 309 operator=, 306 SetBaseFontSize, 309 SetCellBorderPen, 310 SetCellColor, 310 SetCellFont, 311 SetColumnWidths, 312 SetHeader, 312 SetHeaderColor, 313 SetHeaderFont, 314 SetMargin, 314 SetRowHeights, 316 SetStubColumn, 317 SetStubColumnColor, 318 SetStubColumnFont, 319 OEDepict:: OEImageTableStyle, 431 OEDepict:: OEImageTableStyle:: Default, 432 OEDepict:: OEImageTableStyle:: LightBlue, 432 OEDepict:: OEImageTableStyle:: LightGreen, 432 OEDepict:: OEImageTableStyle:: LightGrey, 432 OEDepict::OEImageTableStyle::MediumBlue, 433 OEDepict:: OEImageTableStyle:: MediumGreen, 433

OEDepict:: OEImageTableStyle:: MediumGrey, SetButtonWidthScale, 324 433 SetLegendBoxPen, 324 OEDepict:: OEImageTableStyle:: NoStyle, SetMargin, 324 434 SetMargins, 324 OEDepict:: OEImageTableStyle:: SantaFe, OEDepict:: OELegendLayoutStyle, 438 434 OEDepict:: OELeqendLayoutStyle:: Default, OEDepict:: OEIsRegisteredImageFile, 549 438 OEDepict::OEIsRegisteredMultiPageImageFi@BDepict::OELegendLayoutStyle::HorizontalBottomLef 550 439 OEDepict:: OEIsValidSVGClassName, 550 OEDepict::OELegendLayoutStyle::HorizontalBottomRigl OEDepict:: OEIsValidSVGGroupId, 550 439 OEDepict:: OELayerPosition, 434 OEDepict:: OELegendLayoutStyle:: HorizontalTopLeft, OEDepict:: OELayerPosition:: Above, 435 439 OEDepict:: OELayerPosition:: Below, 435 OEDepict::OELegendLayoutStyle::HorizontalTopRight, OEDepict:: OELayerPosition:: SVG, 435 439 OEDepict:: OELegendColorStyle, 436 OEDepict::OELegendLayoutStyle::VerticalBottomLeft, OEDepict:: OELegendColorStyle:: Default, 440 OEDepict::OELegendLavoutStyle::VerticalBottomRight. 436 OEDepict:: OELegendColorStyle:: LightBlue, 440 OEDepict::OELegendLayoutStyle::VerticalTopLeft, 436 OEDepict:: OELegendColorStyle:: LightGreen, 441 436 OEDepict::OELegendLayoutStyle::VerticalTopRight, OEDepict:: OELegendColorStyle:: LightGrey, 441 436 OEDepict:: OELengthenVector, 551 OEDepict:: OELegendColorStyle:: NoStyle, OEDepict:: OELineCap, 441 437 OEDepict:: OELineCap:: Butt, 442 OEDepict:: OELegendInteractiveStyle, 437 OEDepict:: OELineCap:: Default, 442 OEDepict::OELegendInteractiveStyle::Defa0EDepict::OELineCap::Round, 442 OEDepict:: OELineCap:: Square, 442 438 OEDepict:: OELegendInteractiveStyle:: Hove@EDepict:: OELineJoin, 443 438 OEDepict:: OELineJoin:: Bevel, 443 OEDepict:: OELegendInteractiveStyle:: Perm@EDepict:: OELineJoin:: Default, 443 438 OEDepict:: OELineJoin:: Miter, 443 OEDepict::OELegendInteractiveStyle::Togg@EDepict::OELineJoin::Round, 444 438 OEDepict:: OEMargin, 444 OEDepict:: OELegendLayout, 319 OEDepict:: OEMargin:: Bottom, 444 Constructors, 320 OEDepict:: OEMargin:: Left, 445 GetLegendArea, 320 OEDepict:: OEMargin:: Right, 445 GetOptions, 320 OEDepict:: OEMargin:: Top, 444 OEDepict:: OELegendLayoutOptions, 320 OEDepict:: OEMolDisplayBase, 325 Constructors, 321 GetDataType, 326 GetButtonFont, 322 GetMolecule, 326 GetButtonHeightScale, 322 IsDataType, 326 GetButtonPen, 322 OEDepict:: OEMultiPageImageFile, 326 GetButtonWidthScale, 322 Constructors, 326 GetColorStyle, 322 GetOrientation, 327 GetInteractiveStyle, 322 GetPage, 328 GetLayoutStyle, 323 GetPageHeight, 328 GetLegendBoxPen, 323 GetPages, 329 GetMargin, 323 GetPageWidth, 329 operator=, 321 NewPage, 329 SetButtonFont, 323 NumPages, 329 SetButtonHeightScale, 323 OEDepict:: OEMultiPageParamName, 445 SetButtonPen, 324

```
OEDepict::OEMultiPageParamName::PageOrientatSetmLineStipple.338
       445
                                               SetLineWidth, 338
OEDepict:: OEMultiPageParamName:: PageSize,
                                               SetStippleFactor, 338
       445
                                            OEDepict::OEPrepareAlignedDepiction, 551
OEDepict:: OEMultiPageSetup, 445
                                            OEDepict:: OEPrepareDepiction, 555
OEDepict:: OEMultiPageSetup:: All, 446
                                            OEDepict:: OEPrepareDepictionOptions, 339
OEDepict:: OEMultiPageSetup:: PageOrientation,Constructors, 342
                                               GetAddDepictionHydrogens, 342
       446
OEDepict:: OEMultiPageSetup:: PageSize,
                                               GetClearCoords, 343
       446
                                               GetDepictOrientation, 343
OEDepict:: OENearestAtom, 330
                                               GetPerceiveBondStereo, 343
   Constructors, 330
                                               GetSuppressHydrogens, 343
   GetAtom, 330
                                               operator=, 342
   GetDisplayPosition, 330
                                               SetAddDepictionHydrogens, 343
   GetDist, 330
                                               SetClearCoords, 344
   IsValid, 330
                                               SetDepictOrientation, 344
OEDepict:: OENearestBond, 331
                                               SetPerceiveBondStereo, 344
   Constructors, 331
                                               SetSuppressHydrogens, 344
   GetBond, 331
                                            OEDepict:: OEPrepareDepictionSetup, 448
   GetDisplayPosition, 331
                                            OEDepict:: OEPrepareDepictionSetup:: All,
   GetDist, 331
                                                   448
   IsValid, 331
                                            OEDepict:: OEPrepareDepictionSetup:: ClearCoords,
OEDepict:: OEOffsetMolDisplay, 551
                                                   448
OEDepict:: OEPageOrientation, 447
                                            OEDepict::OEPrepareDepictionSetup::DepictOrientatio
OEDepict:: OEPageOrientation:: Default,
                                                   449
       447
                                            OEDepict::OEPrepareDepictionSetup::SuppressHydroge
OEDepict:: OEPageOrientation:: Landscape,
                                                   449
       447
                                            OEDepict:: OEPrepareMultiAlignedDepiction,
OEDepict:: OEPageOrientation:: Portrait,
                                                   556
       447
                                            OEDepict:: OEProtectiveGroupStyle, 449
OEDepict:: OEPageSize, 447
                                            OEDepict:: OEProtectiveGroupStyle:: Ac.
OEDepict:: OEPageSize:: Custom, 448
                                                   450
OEDepict:: OEPageSize:: Default, 447
                                            OEDepict:: OEProtectiveGroupStyle:: Ad,
OEDepict:: OEPageSize:: ISO_A4, 448
                                                   451
OEDepict:: OEPageSize:: US Legal, 448
                                            OEDepict:: OEProtectiveGroupStyle:: All,
OEDepict:: OEPageSize:: US_Letter, 448
                                                   450
OEDepict:: OEPen, 332
                                            OEDepict::OEProtectiveGroupStyle::Alloc,
   Constructors, 332
                                                   451
   GetBackColor, 333
                                            OEDepict::OEProtectiveGroupStyle::Benzoyl,
   GetFill, 333
                                                   454
   GetForeColor, 334
                                            OEDepict::OEProtectiveGroupStyle::Benzyl,
   GetLineCap, 334
                                                   452
   GetLineJoin, 334
                                            OEDepict:: OEProtectiveGroupStyle:: Bn,
   GetLineStipple, 334
                                                   451
   GetLineWidth, 335
                                            OEDepict:: OEProtectiveGroupStyle:: Boc,
   GetStippleFactor, 335
                                                   452
   operator!=, 333OEDepict:: OEProtectiveGroupStyle:: Bom,
   operator=, 333
                                                   452
   operator==, 333
                                            OEDepict::OEProtectiveGroupStyle::Bpoc,
   SetBackColor, 335
                                                   453
   SetFill. 336
                                            OEDepict::OEProtectiveGroupStyle::Bs,
   SetForeColor, 336
                                                   453
   SetLineCap, 337
                                            OEDepict:: OEProtectiveGroupStyle:: Bt,
   SetLineJoin, 337
                                                   453
```

| OEDepict::OEProtectiveGroupStyle::Btm,           | OEDepict::OEProtectiveGroupStyle::Fmoc,                 |
|--------------------------------------------------|---------------------------------------------------------|
| 454                                              | 462                                                     |
| OEDepict::OEProtectiveGroupStyle::Bz,            | OEDepict::OEProtectiveGroupStyle::FourOMeBz,            |
| 454                                              | 462                                                     |
| OEDepict::OEProtectiveGroupStyle::Bzh,           | OEDepict::OEProtectiveGroupStyle::FPMP,                 |
| 455                                              | 463                                                     |
| OEDepict::OEProtectiveGroupStyle::Bzl,           | OEDepict::OEProtectiveGroupStyle::Im,                   |
| 452                                              | 463                                                     |
| OEDepict::OEProtectiveGroupStyle::BzOM,          | OEDepict::OEProtectiveGroupStyle::Lev,                  |
| 455                                              | 463                                                     |
| OEDepict::OEProtectiveGroupStyle::Cbz,           | OEDepict::OEProtectiveGroupStyle::MDIPS,                |
| 483                                              | 464                                                     |
| OEDepict::OEProtectiveGroupStyle::cHx,           | OEDepict::OEProtectiveGroupStyle::MDPS,                 |
| 455                                              | 464                                                     |
| OEDepict::OEProtectiveGroupStyle::Dan,           | OEDepict::OEProtectiveGroupStyle::MEM,                  |
| 456                                              | 464                                                     |
| OEDepict::OEProtectiveGroupStyle::Dansyl,        | OEDepict::OEProtectiveGroupStyle::Mes,                  |
| 456                                              | 465                                                     |
| OEDepict::OEProtectiveGroupStyle::DCB,           | OEDepict::OEProtectiveGroupStyle::MMTR,                 |
| 456                                              | 465                                                     |
| OEDepict::OEProtectiveGroupStyle::DDE,           | OEDepict::OEProtectiveGroupStyle::MOM,                  |
| 457                                              | 465                                                     |
| OEDepict::OEProtectiveGroupStyle::DDIV,          | OEDepict::OEProtectiveGroupStyle::Moz,                  |
| 457                                              | 466                                                     |
| OEDepict::OEProtectiveGroupStyle::Default,       | OEDepict::OEProtectiveGroupStyle::MPC,                  |
| 450                                              | 466                                                     |
| OEDepict::OEProtectiveGroupStyle::DEIPS,         | OEDepict::OEProtectiveGroupStyle::MPM,                  |
| 457                                              | 466                                                     |
| OEDepict::OEProtectiveGroupStyle::DMAB,          | OEDepict::OEProtectiveGroupStyle::MS,                   |
| 458                                              | 467                                                     |
| OEDepict::OEProtectiveGroupStyle::DMIPS,         | OEDepict::OEProtectiveGroupStyle::MTHP,                 |
| 458                                              | 467                                                     |
| OEDepict::OEProtectiveGroupStyle::DMPM,          | OEDepict::OEProtectiveGroupStyle::MTM,                  |
| 458                                              | 467                                                     |
| OEDepict::OEProtectiveGroupStyle::DMPS,          | OEDepict::OEProtectiveGroupStyle::MTr,                  |
| 459                                              | 468                                                     |
| OEDepict::OEProtectiveGroupStyle::DMTr,          | OEDepict::OEProtectiveGroupStyle::Np,                   |
| 459                                              | 468                                                     |
| OEDepict::OEProtectiveGroupStyle::DNBZ,          | OEDepict::OEProtectiveGroupStyle::NPE,                  |
| 459                                              | 468                                                     |
| OEDepict::OEProtectiveGroupStyle::DNP,           | OEDepict::OEProtectiveGroupStyle::NPEOC,                |
| 460                                              | 469                                                     |
| OEDepict::OEProtectiveGroupStyle::DOC,           | OEDepict::OEProtectiveGroupStyle::NPES,                 |
| 460                                              | 469                                                     |
| OEDepict::OEProtectiveGroupStyle::DPIPS,         | OEDepict::OEProtectiveGroupStyle::NPS,                  |
| 460                                              | 469                                                     |
| OEDepict::OEProtectiveGroupStyle::Dpp,           | OEDepict::OEProtectiveGroupStyle::NVOC,                 |
| 461                                              | 470                                                     |
| OEDepict::OEProtectiveGroupStyle::DTBMS,         | OEDepict::OEProtectiveGroupStyle::OBzl,                 |
| 461                                              | 470                                                     |
| OEDepict::OEProtectiveGroupStyle::EE,            | OEDepict::OEProtectiveGroupStyle::Off,                  |
| 461                                              | 450                                                     |
| OEDepict::OEProtectiveGroupStyle::ESC,           | OEDepict::OEProtectiveGroupStyle::ONOS,                 |
| 462                                              | 470                                                     |
| OEDepict::OEProtectiveGroupStyle::OtBu,<br>471   | OEDepict::OEProtectiveGroupStyle::TMOB,<br>480          |
| OEDepict::OEProtectiveGroupStyle::PAC,<br>471    | OEDepict::OEProtectiveGroupStyle::TMS,<br>480           |
| OEDepict::OEProtectiveGroupStyle::PBF,<br>471    | OEDepict::OEProtectiveGroupStyle::Tos,<br>482           |
| OEDepict::OEProtectiveGroupStyle::PCB,<br>472    | OEDepict::OEProtectiveGroupStyle::transCinnamyl,<br>480 |
| OEDepict::OEProtectiveGroupStyle::PHF,<br>472    | OEDepict::OEProtectiveGroupStyle::Trisyl,<br>481        |
| OEDepict::OEProtectiveGroupStyle::Pht,<br>472    | OEDepict::OEProtectiveGroupStyle::Troc,<br>481          |
| OEDepict::OEProtectiveGroupStyle::Piv,<br>473    | OEDepict::OEProtectiveGroupStyle::TRT,<br>481           |
| OEDepict::OEProtectiveGroupStyle::PMB,<br>473    | OEDepict::OEProtectiveGroupStyle::TS,<br>482            |
| OEDepict::OEProtectiveGroupStyle::PMBM,<br>473   | OEDepict::OEProtectiveGroupStyle::Xyl,<br>482           |
| OEDepict::OEProtectiveGroupStyle::Poc,<br>474    | OEDepict::OEProtectiveGroupStyle::Z,<br>483             |
| OEDepict::OEProtectiveGroupStyle::PPi,<br>474    | OEDepict::OERadicalDisplayType,<br>483                  |
| OEDepict::OEProtectiveGroupStyle::SEM,<br>474    | OEDepict::OERadicalDisplayType::Diradical,<br>484       |
| OEDepict::OEProtectiveGroupStyle::SES,<br>475    | OEDepict::OERadicalDisplayType::Monoradical,<br>484     |
| OEDepict::OEProtectiveGroupStyle::StBu,<br>475   | OEDepict::OERadicalDisplayType::Off,<br>483             |
| OEDepict::OEProtectiveGroupStyle::TBDMS,<br>476  | OEDepict::OEReduceFontSizeToFit,<br>558                 |
| OEDepict::OEProtectiveGroupStyle::TBDPS,<br>476  | OEDepict::OERegisterImageFile,<br>558                   |
| OEDepict::OEProtectiveGroupStyle::TBMPS,<br>475  | OEDepict::OERenderMolecule,<br>558                      |
| OEDepict::OEProtectiveGroupStyle::TBS,<br>476    | OEDepict::OERenderMoleculeToBytes,<br>561               |
| OEDepict::OEProtectiveGroupStyle::TCP,<br>477    | OEDepict::OERenderMoleculeToString,<br>561              |
| OEDepict::OEProtectiveGroupStyle::Teoc,<br>477   | OEDepict::OEReport,<br>345                              |
| OEDepict::OEProtectiveGroupStyle::TES,<br>477    | Constructors,<br>345                                    |
| OEDepict::OEProtectiveGroupStyle::Tf,<br>478     | GetBodies,<br>346                                       |
| OEDepict::OEProtectiveGroupStyle::TFA,<br>478    | GetBody,<br>347                                         |
| OEDepict::OEProtectiveGroupStyle::Thexyl,<br>478 | GetCell,<br>347                                         |
| OEDepict::OEProtectiveGroupStyle::THF,<br>479    | GetCellHeight,<br>348                                   |
| OEDepict::OEProtectiveGroupStyle::THP,<br>479    | GetCells,<br>348                                        |
| OEDepict::OEProtectiveGroupStyle::TIPS,<br>479   | GetCellWidth,<br>348                                    |
|                                                  | GetFooter,<br>351                                       |
|                                                  | GetFooterHeight,<br>352                                 |
|                                                  | GetFooters,<br>352                                      |
|                                                  | GetFooterWidth,<br>352                                  |
|                                                  | GetHeader,<br>353                                       |
|                                                  | GetHeaderHeight,<br>353                                 |
|                                                  | GetHeaders,<br>354                                      |
|                                                  | GetHeaderWidth,<br>354                                  |
|                                                  | GetOptions,<br>355                                      |
|                                                  | GetPage,<br>355                                         |
|                                                  | GetPageHeight,<br>355                                   |
|                                                  | GetPages,<br>355                                        |
|                                                  | GetPageWidth,<br>355                                    |
|                                                  | IsBodyPage,<br>356                                      |
|                                                  | IsGridPage,<br>356                                      |
|                                                  | NewBody,<br>357                                         |

```
NewCell, 357
                                            OEDepict:: OEStipple:: DotDashDash, 489
   NumBodyPages, 358
                                            OEDepict:: OEStipple:: LongDash, 489
   NumColsPerPage, 358
                                            OEDepict:: OEStipple:: NoLine, 489
   NumGridPages, 359
                                            OEDepict:: OEStipple:: ShortDash, 489
   NumPages, 359
                                            OEDepict:: OEStipple:: Solid, 490
   NumRowsPerPage, 359
                                            OEDepict:: OESuperAtomStyle, 490
OEDepict:: OEReportOptions, 359
                                            OEDepict:: OESuperAtomStyle:: All, 490
   Constructors, 361
                                            OEDepict:: OESuperAtomStyle:: Bu, 497
   GetCellGap, 362
                                            OEDepict:: OESuperAtomStyle:: Carbon, 501
   GetCellHeight, 362
                                            OEDepict:: OESuperAtomStyle:: CC13, 496
   GetCellWidth, 363
                                            OEDepict:: OESuperAtomStyle:: CF3, 496
   GetFooterHeight, 363
                                            OEDepict:: OESuperAtomStyle:: CHO, 492
   GetFooterWidth, 363
                                            OEDepict:: OESuperAtomStyle:: CN, 492
   GetHeaderHeight, 363
                                            OEDepict:: OESuperAtomStyle:: CNO, 494
   GetHeaderWidth, 363
                                            OEDepict::OESuperAtomStyle::COO_, 491
   GetPageHeight, 364
                                            OEDepict:: OESuperAtomStyle:: COOH, 491
   GetPageMargin, 364
                                            OEDepict:: OESuperAtomStyle:: Default, 490
   GetPageWidth, 364
                                            OEDepict:: OESuperAtomStyle:: Et, 497
   NumColsPerPage, 364
                                            OEDepict:: OESuperAtomStyle:: Ether, 502
                                            OEDepict:: OESuperAtomStyle:: Halide, 501
   NumRowsPerPage, 364
   operator=, 362
                                            OEDepict:: OESuperAtomStyle:: iBu, 498
   SetCellGap, 365
                                            OEDepict:: OESuperAtomStyle:: Me, 496
   SetFooterHeight, 365
                                            OEDepict:: OESuperAtomStyle:: N2, 493
   SetHeaderHeight, 366
                                            OEDepict:: OESuperAtomStyle:: N3, 493
   SetPageHeight, 367
                                            OEDepict:: OESuperAtomStyle:: NC, 492
   SetPageMargin, 368
                                            OEDepict:: OESuperAtomStyle:: NCO, 493
   SetPageMargins, 368
                                            OEDepict:: OESuperAtomStyle:: Nitrogen,
   SetPageOrientation, 369
                                                   500
   SetPageSize, 370
                                            OEDepict:: OESuperAtomStyle:: NO2, 494
   SetPageWidth, 371
                                            OEDepict:: OESuperAtomStyle:: OBu, 500
OEDepict:: OEReportSetup, 484
                                            OEDepict:: OESuperAtomStyle:: OEt, 499
OEDepict:: OEReportSetup:: All, 484
                                            OEDepict:: OESuperAtomStyle:: Off, 491
OEDepict::OEReportSetup::NumColsPerPage,OEDepict::OESuperAtomStyle::OMe,499
       485
                                            OEDepict:: OESuperAtomStyle:: ONO, 494
OEDepict::OEReportSetup::NumRowsPerPage.OEDepict::OESuperAtomStyle::OPr.499
       485
                                            OEDepict:: OESuperAtomStyle:: Oxygen, 500
OEDepict::OEReportSetup::PageHeight,486 OEDepict::OESuperAtomStyle::OxygenAndNitrogen,
OEDepict:: OEReportSetup:: PageOrientation,
                                                   501
       486
                                            OEDepict:: OESuperAtomStyle:: Phosphorus,
OEDepict:: OEReportSetup:: PageSize, 486
                                                   501
OEDepict:: OEReportSetup:: PaqeWidth, 487
                                            OEDepict:: OESuperAtomStyle:: PO3H2, 495
OEDepict:: OERotateVector, 562
                                            OEDepict:: OESuperAtomStyle:: Pr, 497
                                            OEDepict:: OESuperAtomStyle:: sBu, 498
OEDepict:: OEScale, 487
OEDepict:: OEScale:: AutoScale, 488
                                            OEDepict:: OESuperAtomStyle:: SO3_, 495
OEDepict:: OEScale:: Default, 487
                                            OEDepict:: OESuperAtomStyle:: SO3H, 495
OEDepict:: OESetup2DMolDisplayOptions,
                                            OEDepict:: OESuperAtomStyle:: Sulfur, 501
       562
                                            OEDepict:: OESuperAtomStyle:: tBu, 498
OEDepict::OESetupPrepareDepictionOptionsOEDepict::OESuppressNonDepictionHydrogens,
       563
                                                   563
OEDepict:: OESetupReportOptions, 563
                                            OEDepict:: OESVGClass, 372
OEDepict:: OEStipple, 488
                                                Constructors, 372
OEDepict:: OEStipple:: Default, 488
                                                GetName, 373
OEDepict:: OEStipple:: Dot, 488
                                            OEDepict:: OESVGGroup, 373
OEDepict:: OEStipple:: DotDash, 488
                                                AddSVGClass, 373
```

```
Constructors, 373
   GetId. 373
   IsVisible, 373
OEDepict:: OETitleLocation, 502
OEDepict:: OETitleLocation:: Bottom, 502
OEDepict:: OETitleLocation:: Default, 502
OEDepict:: OETitleLocation:: Hidden, 503
OEDepict:: OETitleLocation:: Top, 503
OEDepict:: OEWrite2DRingDictionaryReport,
       564
OEDepict:: OEWriteImage, 565
OEDepict:: OEWriteImageToBytes, 566
OEDepict:: OEWriteImageToString, 566
OEDepict:: OEWriteMultiPageImage, 566
OEDepict:: OEWriteReport, 567
OEDepict:: OEWriteReportPageByPage, 568
OEDepict:: OEWriteReportToBytes, 568
OEDepict:: OEWriteReportToString, 568
operator *
   OEDepict:: OE2DPoint, 183
operator! =OEDepict:: OEFont, 212
   OEDepict:: OEPen, 333
operator()
   OEDepict:: OEDisplayAtomIdx, 206
   OEDepict:: OEDisplayAtomMapIdx, 206
   OEDepict:: OEDisplayAtomPropBase, 207
   OEDepict:: OEDisplayBondIdx, 208
   OEDepict:: OEDisplayBondPropBase, 209
   OEDepict:: OEDisplayNoAtomProp, 210
   OEDepict:: OEDisplayNoBondProp, 210
operator*{error*}=OEDepict:: OE2DPoint, 184
operator+
   OEDepict:: OE2DPoint, 183
operator+=
   OEDepict:: OE2DPoint, 183
operator/
   OEDepict:: OE2DPoint, 183
operator/=OEDepict:: OE2DPoint, 184
operator=
   OEDepict:: OE2DAtomDisplay, 107
   OEDepict:: OE2DBondDisplay, 116
   OEDepict:: OE2DMolDisplay, 123
   OEDepict:: OE2DMolDisplayOptions, 131
   OEDepict:: OE2DPath, 178
   OEDepict:: OE2DPathPoint, 181
   OEDepict:: OE2DPoint, 183
   OEDepict:: OEAlignmentOptions, 186
   OEDepict:: OEAlignmentResult, 192
   OEDepict:: OEFont, 212
   OEDepict:: OEHighlightByBallAndStick,
       221
```

```
OEDepict:: OEHighlightByCogwheel, 226
   OEDepict:: OEHighlightByColor, 233
   OEDepict:: OEHighlightByLasso, 237
   OEDepict:: OEHighlightByStick, 244
   OEDepict::OEHighlightOverlayByBallAndStick,
       255
   OEDepict:: OEImageTableOptions, 306
   OEDepict:: OELegendLayoutOptions, 321
   OEDepict:: OEPen, 333
   OEDepict:: OEPrepareDepictionOptions,
       342
   OEDepict:: OEReportOptions, 362
operator==
   OEDepict:: OEFont, 212
   OEDepict:: OEPen, 333
operator-
   OEDepict:: OE2DPoint, 183
operator-=
   OEDepict:: OE2DPoint, 184
```

# $\mathsf{P}$

```
PopGroup
   OEDepict:: OEImageBase, 281
   OEDepict:: OEImageFileBase, 282
PushGroup
   OEDepict:: OEImageBase, 281
   OEDepict:: OEImageFileBase, 282
```

# R

Render OEDepict:: OEImage, 266 ringdict2pdf.py Example Code, 93

# S

```
SetAddDepictionHydrogens
   OEDepict:: OEAlignmentOptions, 188
   OEDepict:: OEPrepareDepictionOptions,
       343
SetAlignment
   OEDepict:: OEFont, 214
SetAromaticStyle
   OEDepict:: OE2DMolDisplayOptions, 141
SetAtomColor
   OEDepict:: OE2DMolDisplayOptions, 142
SetAtomColorStyle
   OEDepict:: OE2DMolDisplayOptions, 143
SetAtomExternalHighlight
   OEDepict:: OEHighlightByColor, 233
SetAtomExternalHighlightRatio
   OEDepict:: OEHighlightByStick, 245
SetAtomLabelFont
   OEDepict:: OE2DMolDisplayOptions, 143
SetAtomLabelFontScale
```

OEDepict:: OE2DMolDisplayOptions, 144 SetAtomLabelMonochrome OEDepict:: OEHighlightByBallAndStick,  $222$ OEDepict:: OEHighlightByCogwheel, 227 OEDepict:: OEHighlightByLasso, 239 OEDepict:: OEHighlightByStick, 245 OEDepict:: OEHighlightOverlayByBallAndSttLEukt,tonWidthScale 256 SetAtomPropertyFunctor OEDepict:: OE2DMolDisplayOptions, 148 SetAtomPropLabelFont OEDepict:: OE2DMolDisplayOptions, 145 SetAtomPropLabelFontScale OEDepict:: OE2DMolDisplayOptions, 147 SetAtomStereoStyle OEDepict:: OE2DMolDisplayOptions, 149 SetAtomSVGMarkupFunctor OEDepict:: OE2DMolDisplayOptions, 150 SetAtomVisibilityFunctor OEDepict:: OE2DMolDisplayOptions, 151 SetBackColor OEDepict:: OEPen, 335 SetBackgroundColor OEDepict:: OE2DMolDisplayOptions, 152 SetBallRadiusScale OEDepict:: OEHighlightByBallAndStick, SetColor 222 OEDepict:: OEHighlightByCogwheel, 228 OEDepict::OEHighlightOverlayByBallAndStick, 223 256 SetBaseFontSize OEDepict:: OEImageTableOptions, 309 SetBgnPen OEDepict:: OE2DBondDisplay, 120 SetBondColorStyle OEDepict:: OE2DMolDisplayOptions, 152 SetBondLineAtomLabelGapScale OEDepict:: OE2DMolDisplayOptions, 153 SetBondLineGapScale OEDepict:: OE2DMolDisplayOptions, 153 SetBondPropertyFunctor OEDepict:: OE2DMolDisplayOptions, 157 SetBondPropLabelFont OEDepict:: OE2DMolDisplayOptions, 154 SetBondPropLabelFontScale OEDepict:: OE2DMolDisplayOptions, 156 SetBondStereoStyle OEDepict:: OE2DMolDisplayOptions, 158 SetBondSVGMarkupFunctor OEDepict:: OE2DMolDisplayOptions, 159 SetBondWidthScaling OEDepict:: OE2DMolDisplayOptions, 160 SetBoundingBoxPen

OEDepict:: OEHighlightLabel, 251 SetButtonFont OEDepict:: OELegendLayoutOptions, 323 SetButtonHeightScale OEDepict:: OELegendLayoutOptions, 323 SetButtonPen OEDepict:: OELegendLayoutOptions, 324 OEDepict:: OELegendLayoutOptions, 324 SetCellBorderPen OEDepict:: OEImageTableOptions, 310 SetCellColor OEDepict:: OEImageTableOptions, 310 SetCellFont OEDepict:: OEImageTableOptions, 311 SetCellGap OEDepict:: OEImageGrid, 296 OEDepict:: OEReportOptions, 365 SetCharge OEDepict:: OE2DAtomDisplay, 113 SetClearCoords OEDepict:: OEAlignmentOptions, 188 OEDepict:: OEPrepareDepictionOptions, 344 SetClosed OEDepict:: OE2DPath, 181 OEDepict:: OEFont, 215 OEDepict:: OEHighlightByBallAndStick, OEDepict:: OEHighlightByCogwheel, 228 OEDepict:: OEHighlightByColor, 234 OEDepict:: OEHighlightByLasso, 241 OEDepict:: OEHighlightByStick, 246 SetColors OEDepict:: OEHighlightOverlayBase, 254 SetColumnWidths OEDepict:: OEImageTableOptions, 312 SetConsiderAtomLabelBoundingBox OEDepict:: OEHighlightByLasso, 239 SetCoords OEDepict:: OE2DAtomDisplay, 113 SetDefaultBondPen OEDepict:: OE2DMolDisplayOptions, 160 SetDepictOrientation OEDepict:: OEPrepareDepictionOptions, 344 SetDimensions OEDepict:: OE2DMolDisplayOptions, 162 SetDisplayPos OEDepict:: OE2DBondDisplay, 120 SetDisplayType OEDepict:: OE2DBondDisplay, 120

SetEndPen OEDepict:: OE2DBondDisplay, 120 SetExplicitAtomLabelAngle OEDepict:: OE2DMolDisplayOptions, 162 SetFamily OEDepict:: OEFont, 215 SetFill OEDepict:: OEPen, 336 SetFixedCoords OEDepict:: OEAlignmentOptions, 189 SetFont OEDepict:: OEHighlightLabel, 251 SetFontScale OEDepict:: OEHighlightLabel, 253 SetFooterHeight OEDepict:: OEReportOptions, 365 SetForeColor OEDepict:: OEPen, 336 SetHCount OEDepict:: OE2DAtomDisplay, 113 SetHeader OEDepict:: OEImageTableOptions, 312 SetHeaderColor OEDepict:: OEImageTableOptions, 313 SetHeaderFont OEDepict:: OEImageTableOptions, 314 SetHeaderHeight OEDepict:: OEReportOptions, 366 SetHeight OEDepict:: OE2DMolDisplayOptions, 163 SetHPosition OEDepict:: OE2DAtomDisplay, 113 SetHydrogenStyle OEDepict:: OE2DMolDisplayOptions, 164 SetHyperlink OEDepict:: OEFont, 216 SetInnerContour OEDepict:: OEHighlightByCogwheel, 229 SetLabel OEDepict:: OE2DAtomDisplay, 113 SetLabelFont OEDepict:: OE2DAtomDisplay, 114 SetLassoScale OEDepict:: OEHighlightByLasso, 240 SetLegendBoxPen OEDepict:: OELegendLayoutOptions, 324 SetLineCap OEDepict:: OEPen, 337 SetLineJoin OEDepict:: OEPen, 337 SetLineStipple OEDepict:: OEPen, 338 SetLineWidth OEDepict:: OEPen, 338

SetLineWidthScale OEDepict:: OEHighlightByCogwheel, 230 OEDepict:: OEHighlightByColor, 234 OEDepict:: OEHighlightByLasso, 241 SetMargin OEDepict:: OE2DMolDisplayOptions, 164 OEDepict:: OEImageGrid, 296 OEDepict:: OEImageTableOptions, 314 OEDepict:: OELegendLayoutOptions, 324 SetMargins OEDepict:: OE2DMolDisplayOptions, 166 OEDepict:: OEImageGrid, 296 OEDepict:: OEImageTableOptions, 315 OEDepict:: OELegendLayoutOptions, 324 SetMass OEDepict:: OE2DAtomDisplay, 114 SetMaxAllowedAtomPairClashes OEDepict:: OEAlignmentOptions, 189 SetMaxBondRotations OEDepict:: OEAlignmentOptions, 189 SetMaxPatternMatches OEDepict:: OEAlignmentOptions, 190 SetMinFontSize OEDepict:: OEImageBase, 279 SetPageHeight OEDepict:: OEReportOptions, 367 SetPageMargin OEDepict:: OEReportOptions, 368 SetPageMargins OEDepict:: OEReportOptions, 368 SetPageOrientation OEDepict:: OEReportOptions, 369 SetPageSize OEDepict:: OEReportOptions, 370 SetPageWidth OEDepict:: OEReportOptions, 371 SetPen OEDepict:: OEHighlightByLasso, 241 SetPerceiveBondStereo OEDepict:: OEPrepareDepictionOptions, 344 SetPosition OEDepict:: OEHighlightByLasso, 242 SetProperty OEDepict:: OE2DAtomDisplay, 114 OEDepict:: OE2DBondDisplay, 121 SetPropertyFont OEDepict:: OE2DAtomDisplay, 114 OEDepict:: OE2DBondDisplay, 121 SetPropertyOffset OEDepict:: OE2DAtomDisplay, 115 OEDepict:: OE2DBondDisplay, 121 SetProtectiveGroupLabelFont OEDepict:: OE2DMolDisplayOptions, 166

SetProtectiveGroupStyle OEDepict:: OE2DMolDisplayOptions, 168 SetRadical OEDepict:: OE2DAtomDisplay, 115 SetRMSDCutoff OEDepict:: OEAlignmentOptions, 190 SetRotateAroundBonds OEDepict:: OEAlignmentOptions, 191 SetRotationAngle OEDepict:: OEFont, 217 SetRowHeights OEDepict:: OEImageTableOptions, 316 SetScale OEDepict:: OE2DMolDisplayOptions, 168 SetSize OEDepict:: OEFont, 218 SetStickWidthScale OEDepict:: OEHighlightByBallAndStick, 223 OEDepict:: OEHighlightByCogwheel, 230 OEDepict:: OEHighlightByStick, 247 OEDepict::OEHighlightOverlayByBallAndStick, 257 SetStippleFactor OEDepict:: OEPen, 338 SetStubColumn OEDepict:: OEImageTableOptions, 317 SetStubColumnColor OEDepict:: OEImageTableOptions, 318 SetStubColumnFont OEDepict:: OEImageTableOptions, 319 SetStyle OEDepict:: OEFont, 218 SetSuperAtomLabelFont OEDepict:: OE2DMolDisplayOptions, 169 SetSuperAtomStyle OEDepict:: OE2DMolDisplayOptions, 170 SetSuppressHydrogens OEDepict:: OEAlignmentOptions, 191 OEDepict:: OEPrepareDepictionOptions, 344 SetTitleFont OEDepict:: OE2DMolDisplayOptions, 171 SetTitleFontScale OEDepict:: OE2DMolDisplayOptions, 173 SetTitleHeight OEDepict:: OE2DMolDisplayOptions, 175 SetTitleLocation OEDepict:: OE2DMolDisplayOptions, 173 SetVisible OEDepict:: OEAtomDisplayBase, 195 OEDepict:: OEBondDisplayBase, 201 SetWidth OEDepict:: OE2DMolDisplayOptions, 175

SetX OEDepict:: OE2DPoint, 184 SetY OEDepict:: OE2DPoint, 185 smartsalign2d.py Example Code, 96

## $\mathsf{V}$

viewmdlsearch.py Example Code, 100

## W

Write OEDepict:: OEImageFileBase, 282