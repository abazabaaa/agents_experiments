![](_page_0_Picture_0.jpeg)

# **Grapheme TK - Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| Section                                       | Page                                 |    |
|-----------------------------------------------|--------------------------------------|----|
| 1 Introduction                                | 1                                    |    |
| 2 Theory                                      | 2                                    |    |
| 2.1 Annotating Atoms and Bonds                | 2                                    |    |
| 2.2 Drawing a Molecule Surface                | 3                                    |    |
| 2.3 Drawing a Ligand-Protein Complex Surface  | 7                                    |    |
| 2.4 Depicting Property Maps                   | 22                                   |    |
| 3 Examples                                    | 27                                   |    |
| 3.1 Grapheme Examples                         | 27                                   |    |
| 3.1.1 Depicting BFactor                       | 27                                   |    |
| 3.1.2 Depicting Active Site Interactions      | 36                                   |    |
| 3.1.3 Depicting Shape and Color Atom Overlaps | 39                                   |    |
| 3.2 Python Cookbook Examples                  | 47                                   |    |
| 4 Preliminary API                             | 49                                   |    |
| 4.1 OEDrawIridiumData                         | 49                                   |    |
| 5 API                                         | 51                                   |    |
| 5.1 OEGrapheme Classes                        | 51                                   |    |
| 5.1.1 OE2DActiveSiteDisplay                   | 51                                   |    |
| 5.1.2 OE2DActiveSiteDisplayOptions            | 53                                   |    |
| 5.1.3 OE2DActiveSiteLegendDisplayOptions      | 57                                   |    |
| 5.1.4 OE2DPropMap                             | 58                                   |    |
| 5.1.5 OEAlignedDepictionFrom3DOptions         | 68                                   |    |
| 5.1.6 OEAtomGlyphBase                         | 70                                   |    |
| 5.1.7 OEAtomGlyphCircle                       | 71                                   |    |
| 5.1.8 OEBondGlyphArrow                        | 72                                   |    |
| 5.1.9 OEBondGlyphBase                         | 74                                   |    |
| 5.1.10 OEBondGlyphCircle                      | 75                                   |    |
| 5.1.11 OEBondGlyphCross                       | 76                                   |    |
| 5.1.12 OEBondGlyphCurvedArrow                 | 78                                   |    |
| 5.1.13 OEBondGlyphScissors                    | 79                                   |    |
| 5.1.14 OEBondGlyphStitch                      | 81                                   |    |
| 5.1.15 OEBondGlyphZigZag                      | 82                                   |    |
| 5.1.16 OEColorGradientDisplayOptions          | 84                                   |    |
| 5.1.17 OEColorGradientLabel                   | 96                                   |    |
| 5.1.18 OEColorForceFieldDisplay               | 97                                   |    |
| 5.1.19 OEColorForceFieldLegendDisplayOptions  | 99                                   |    |
| 5.1.20 OEColorOverlapDisplayOptions           | 100                                  |    |
| 5.1.21                                        | OEDepictionFrom3DOptions             | 10 |
| 5.1.22                                        | OENearestResidue                     | 10 |
| 5.1.23                                        | OEPeptideDisplayOptions              | 10 |
| 5.1.24                                        | OEPlotMarker                         | 10 |
| 5.1.25                                        | OERamachandranPlot                   | 11 |
| 5.1.26                                        | OEResidueSVGMarkupBase               | 11 |
| 5.1.27                                        | OEResidueSVGNoMarkup                 | 11 |
| 5.1.28                                        | OEResidueSVGStandardMarkup           | 11 |
| 5.1.29                                        | OEShapeOverlapDisplay                | 11 |
| 5.1.30                                        | OEShapeOverlapDisplayOptions         | 11 |
| 5.1.31                                        | OEShapeQueryDisplay                  | 12 |
| 5.1.32                                        | OEShapeQueryDisplayOptions           | 12 |
| 5.1.33                                        | OESurfaceArc                         | 12 |
| 5.2                                           | OEGrapheme Basic Arc Drawing Classes | 13 |
| 5.2.1                                         | OEAlphaRainbowArcFxn                 | 13 |
| 5.2.2                                         | OEBrickRoadArcFxn                    | 13 |
| 5.2.3                                         | OECastleArcFxn                       | 13 |
| 5.2.4                                         | OECogArcFxn                          | 13 |
| 5.2.5                                         | OEComplexSurfaceArcFxnBase           | 13 |
| 5.2.6                                         | OEDefaultArcFxn                      | 13 |
| 5.2.7                                         | OEDefaultBuriedArcFxn                | 13 |
| 5.2.8                                         | OEDefaultCavityArcFxn                | 13 |
| 5.2.9                                         | OEDefaultSolventArcFxn               | 14 |
| 5.2.10                                        | OEDefaultVoidArcFxn                  | 14 |
| 5.2.11                                        | OEEyelashArcFxn                      | 14 |
| 5.2.12                                        | OEFlowerArcFxn                       | 14 |
| 5.2.13                                        | OENecklaceArcFxn                     | 14 |
| 5.2.14                                        | OENullArcFxn                         | 14 |
| 5.2.15                                        | OEOliveBranchArcFxn                  | 14 |
| 5.2.16                                        | OEPearlsArcFxn                       | 14 |
| 5.2.17                                        | OERaceTrackArcFxn                    | 15 |
| 5.2.18                                        | OERailroadTrackArcFxn                | 15 |
| 5.2.19                                        | OESawArcFxn                          | 15 |
| 5.2.20                                        | OESimpsonArcFxn                      | 15 |
| 5.2.21                                        | OEStitchArcFxn                       | 15 |
| 5.2.22                                        | OESunArcFxn                          | 15 |
| 5.2.23                                        | OESurfaceArcFxnBase                  | 15 |
| 5.2.24                                        | OEWreathArcFxn                       | 16 |
| 5.3                                           | OEGrapheme Constants                 | 16 |
| 5.3.1                                         | OE2DPropMapSetup                     | 16 |
| 5.3.2                                         | OEActiveSiteRenderStyle              | 16 |
| 5.3.3                                         | OECircleStyle                        | 16 |
| 5.3.4                                         | OEColorAtomStyle                     | 17 |
| 5.3.5                                         | OELegendLocation                     | 17 |
| 5.3.6                                         | OEPatternDirection                   | 17 |
| 5.3.7                                         | OEPeptideLabelStyle                  | 17 |
| 5.3.8                                         | OEPlotMarkerStyle                    | 18 |
| 5.3.9                                         | OEShapeOverlapDisplayStyle           | 18 |
| 5.3.10                                        | OESurfaceArcScale                    | 18 |
| 5.3.11                                        | OESurfaceArcStyle                    | 18 |
| 5.4                                           | OEGrapheme Functions                 | 18 |
| 5.4.1                                         | OEAddComplexSurfaceArcs              | 18 |
| 5.4.2                                         | OEAddGlyph                           | 18 |
| 5.4.3                                         | OEAddLigandHighlighting              | 18 |

| Section | Function                                          | Page |
|---------|---------------------------------------------------|------|
| 5.4.4   | OEAddResidueHighlighting                          | 19   |
| 5.4.5   | OEClearSurfaceArcFxn                              | 19   |
| 5.4.6   | OEConfigure2DPropMap                              | 19   |
| 5.4.7   | OEDraw2DSurface                                   | 19   |
| 5.4.8   | OEDrawActiveSiteLegend                            | 19   |
| 5.4.9   | OEDrawBFactorMapLegend                            | 20   |
| 5.4.10  | OEDrawCircle                                      | 20   |
| 5.4.11  | OEDrawColorForceFieldLegend                       | 20   |
| 5.4.12  | OEDrawColorGradient                               | 20   |
| 5.4.13  | OEDrawPeptide                                     | 20   |
| 5.4.14  | OEDrawResidues                                    | 20   |
| 5.4.15  | OEDrawROCSScores                                  | 20   |
| 5.4.16  | OEDrawSurfaceArc                                  | 20   |
| 5.4.17  | OEDrawUnpairedInteractionMapLegend                | 20   |
| 5.4.18  | OEGet2DSurfaceArcs                                | 20   |
| 5.4.19  | OEGetMoleculeSurfaceScale                         | 21   |
| 5.4.20  | OEGetNearbyAtom                                   | 21   |
| 5.4.21  | OEGetNearbyBond                                   | 21   |
| 5.4.22  | OEGetNearbyResidue                                | 21   |
| 5.4.23  | OEGetNearestAtom                                  | 21   |
| 5.4.24  | OEGetNearestBond                                  | 21   |
| 5.4.25  | OEGetNearestResidue                               | 21   |
| 5.4.26  | OEGetSurfaceArcFxn                                | 21   |
| 5.4.27  | OEGraphemeGetArch                                 | 214  |
| 5.4.28  | OEGraphemeGetLicensee                             | 214  |
| 5.4.29  | OEGraphemeGetPlatform                             | 214  |
| 5.4.30  | OEGraphemeGetRelease                              | 214  |
| 5.4.31  | OEGraphemeGetSite                                 | 214  |
| 5.4.32  | OEGraphemeGetVersion                              | 214  |
| 5.4.33  | OEGraphemeIsLicensed                              | 215  |
| 5.4.34  | OEHasSurfaceArcFxn                                | 213  |
| 5.4.35  | OEPrepareActiveSiteDepiction                      | 215  |
| 5.4.36  | OEPrepareAlignedDepictionFrom3D                   | 216  |
| 5.4.37  | OEPrepareDepictionFrom3D                          | 218  |
| 5.4.38  | OERenderActiveSite                                | 219  |
| 5.4.39  | OERenderActiveSiteMaps                            | 222  |
| 5.4.40  | OERenderBFactorMap                                | 223  |
| 5.4.41  | OERenderContactMap                                | 224  |
| 5.4.42  | OERenderColorOverlap                              | 225  |
| 5.4.43  | OERenderRamachandranPlot                          | 226  |
| 5.4.44  | OERenderShapeOverlap                              | 227  |
| 5.4.45  | OERenderShapeQuery                                | 229  |
| 5.4.46  | OERenderUnpairedInteractionMap                    | 230  |
| 5.4.47  | OESetSurfaceArcFxn                                | 231  |
| 5.4.48  | OESetup2DPropMap                                  | 232  |
| 5.5     | OEGrapheme Basic Circle and Arc Drawing Functions | 232  |
| 5.5.1   | OEDrawAlphaRainbowCircle                          | 232  |
| 5.5.2   | OEDrawAlphaRainbowSurfaceArc                      | 233  |
| 5.5.3   | OEDrawBrickRoadCircle                             | 233  |
| 5.5.4   | OEDrawBrickRoadSurfaceArc                         | 234  |
| 5.5.5   | OEDrawCastleCircle                                | 235  |
| 5.5.6   | OEDrawCastleSurfaceArc                            | 236  |
| 5.5.7   | OEDrawCogCircle                                   | 237  |
| 5.5.8   | OEDrawCogSurfaceArc                               |      |
| Section | Title                                             | Page |
| 5.5.9   | OEDrawDefaultCircle                               | 23   |
| 5.5.10  | OEDrawDefaultSurfaceArc                           | 23   |
| 5.5.11  | OEDrawEyelashCircle                               | 23   |
| 5.5.12  | OEDrawEyelashSurfaceArc                           | 24   |
| 5.5.13  | OEDrawFlowerCircle                                | 24   |
| 5.5.14  | OEDrawFlowerSurfaceArc                            | 24   |
| 5.5.15  | OEDrawGreekKeyCircle                              | 24   |
| 5.5.16  | OEDrawNecklaceCircle                              | 24   |
| 5.5.17  | OEDrawNecklaceSurfaceArc                          | 24   |
| 5.5.18  | OEDrawOliveBranchCircle                           | 24   |
| 5.5.19  | OEDrawOliveBranchSurfaceArc                       | 24   |
| 5.5.20  | OEDrawPearlsCircle                                | 24   |
| 5.5.21  | OEDrawPearlsSurfaceArc                            | 24   |
| 5.5.22  | OEDrawRaceTrackCircle                             | 24   |
| 5.5.23  | OEDrawRaceTrackSurfaceArc                         | 24   |
| 5.5.24  | OEDrawRailroadTrackCircle                         | 24   |
| 5.5.25  | OEDrawRailroadTrackSurfaceArc                     | 25   |
| 5.5.26  | OEDrawSawCircle                                   | 25   |
| 5.5.27  | OEDrawSawSurfaceArc                               | 25   |
| 5.5.28  | OEDrawSimpsonCircle                               | 25   |
| 5.5.29  | OEDrawSimpsonSurfaceArc                           | 25   |
| 5.5.30  | OEDrawStitchCircle                                | 25   |
| 5.5.31  | OEDrawStitchSurfaceArc                            | 25   |
| 5.5.32  | OEDrawSunCircle                                   | 25   |
| 5.5.33  | OEDrawSunSurfaceArc                               | 25   |
| 5.5.34  | OEDrawWreathCircle                                | 25   |
| 5.5.35  | OEDrawWreathSurfaceArc                            | 25   |
| 6       | <b>Release History</b>                            | 26   |
| 6.1     | Grapheme TK 1.5.2                                 | 26   |
| 6.1.1   | New features                                      | 26   |
| 6.1.2   | Minor bug fixes                                   | 26   |
| 6.2     | Grapheme TK 1.5.1                                 | 26   |
| 6.3     | Grapheme TK 1.5.0                                 | 26   |
| 6.4     | Grapheme TK 1.4.7                                 | 26   |
| 6.5     | Grapheme TK 1.4.6                                 | 26   |
| 6.6     | Grapheme TK 1.4.5                                 | 26   |
| 6.7     | Grapheme TK 1.4.4                                 | 26   |
| 6.8     | Grapheme TK 1.4.3                                 | 26   |
| 6.8.1   | New features                                      | 26   |
| 6.9     | Grapheme TK 1.4.2                                 | 26   |
| 6.9.1   | New features                                      | 26   |
| 6.9.2   | Minor bug fixes                                   | 26   |
| 6.10    | Grapheme TK 1.4.1                                 | 26   |
| 6.11    | Grapheme TK 1.4.0                                 | 26   |
| 6.11.1  | New features                                      | 26   |
| 6.12    | Grapheme TK 1.3.7                                 | 26   |
| 6.12.1  | New features                                      | 26   |
| 6.12.2  | Minor bug fixes                                   | 26   |
| 6.13    | Grapheme TK 1.3.6                                 | 26   |
| 6.13.1  | New features                                      | 26   |
| 6.13.2  | New features (Preliminary API)                    | 26   |
| 6.13.3  | Major bug fixes                                   | 26   |
| 6.13.4  | Minor bug fixes                                   | 26   |

| 6.13.5 Documentation changes | 266 |
|------------------------------|-----|
| 6.14 GraphemeTM TK 1.3.5     | 268 |
| 6.14.1 New features          | 268 |
| 6.14.2 Minor bug fixes       | 268 |
| 6.14.3 Java-specific changes | 268 |
| 6.14.4 C#-specific changes   | 268 |
| 6.15 GraphemeTM TK 1.3.4     | 268 |
| 6.15.1 New features          | 268 |
| 6.15.2 Minor bug fixes       | 268 |
| 6.16 GraphemeTM TK 1.3.3     | 269 |
| 6.16.1 New features          | 269 |
| 6.16.2 Preliminary API       | 269 |
| 6.16.3 Major bug fixes       | 269 |
| 6.16.4 Minor bug fixes       | 270 |
| 6.16.5 Documentation changes | 270 |
| 6.17 GraphemeTM TK 1.3.2     | 271 |
| 6.17.1 New features          | 271 |
| 6.17.2 Minor bug fixes       | 271 |
| 6.18 Grapheme TK 1.3.1       | 272 |
| 6.18.1 New features          | 272 |
| 6.18.2 Minor bug fixes       | 273 |
| 6.18.3 Documentation changes | 273 |
| 6.19 Grapheme TK 1.3.0       | 274 |
| 6.19.1 New features          | 274 |
| 6.19.2 Documentation changes | 274 |
| 6.20 Grapheme TK 1.2.3       | 276 |
| 6.20.1 Minor bug fixes       | 276 |
| 6.20.2 Documentation changes | 276 |
| 6.21 Grapheme TK 1.2.2       | 276 |
| 6.21.1 New features          | 276 |
| 6.21.2 Major bug fixes       | 277 |
| 6.21.3 Minor bug fixes       | 277 |
| 6.21.4 Documentation changes | 278 |
| 6.22 Grapheme TK 1.2.1       | 278 |
| 6.22.1 Major bug fixes       | 278 |
| 6.22.2 Documentation changes | 278 |
| 6.23 Grapheme TK 1.2.0       | 278 |
| 6.23.1 New features          | 278 |
| 6.23.2 Major bug fixes       | 279 |
| 6.23.3 Minor bug fixes       | 279 |
| 6.23.4 Documentation changes | 279 |
| 6.24 Grapheme TK 1.1.3       | 279 |
| 6.24.1 New features          | 279 |
| 6.24.2 Major bug fixes       | 280 |
| 6.24.3 Minor bug fixes       | 280 |
| 6.24.4 Documentation changes | 280 |
| 6.25 Grapheme TK 1.1.2       | 280 |
| 6.25.1 New features          | 280 |
| 6.25.2 Major bug fixes       | 280 |
| 6.25.3 Documentation changes | 280 |
| 6.26 Grapheme TK 1.1.1       | 281 |
| 6.26.1 New features          | 281 |
| 6.26.2 Minor bug fixes       | 281 |
| 6.26.3 Documentation changes | 281 |

| Section                              | Page |
|--------------------------------------|------|
| 6.27 Grapheme TK 1.1.0               | 281  |
| 6.27.1 New features                  | 281  |
| 6.27.2 Major bug fixes               | 283  |
| 6.27.3 Documentation changes         | 283  |
| 6.28 Grapheme TK 1.0.6               | 283  |
| 6.28.1 New features                  | 283  |
| 6.28.2 Major bug fixes               | 284  |
| 6.28.3 Minor bug fixes               | 284  |
| 6.28.4 Documentation changes         | 284  |
| 6.29 Grapheme TK 1.0.5               | 284  |
| 6.29.1 New features                  | 284  |
| 6.30 Grapheme TK 1.0.4               | 285  |
| 6.30.1 New features                  | 285  |
| 6.30.2 Major bug fixes               | 285  |
| 6.30.3 Minor bug fixes               | 285  |
| 6.30.4 Documentation changes         | 286  |
| 6.31 Grapheme TK 1.0.3               | 286  |
| 6.31.1 New features                  | 286  |
| 6.31.2 Minor bug fixes               | 286  |
| 6.31.3 Documentation changes         | 286  |
| 6.32 Grapheme TK 1.0.2               | 286  |
| 6.32.1 Minor bug fix                 | 286  |
| 6.32.2 Documentation changes         | 287  |
| 6.33 Grapheme TK 1.0.1               | 287  |
| 6.33.1 Minor bug fixes               | 287  |
| 6.34 Grapheme TK 1.0.0               | 287  |
| 6.34.1 New features                  | 287  |
| <b>7 Copyright and Trademarks</b>    | 289  |
| <b>8 Sample Code</b>                 | 291  |
| <b>9 Citation</b>                    | 293  |
| 9.1 Orion ® Floes                    |      |
| 9.2 Toolkits and Applications        |      |
| 9.3 OpenEye Web Services             | 295  |
| <b>10 Technology Licensing</b>       | 297  |
| 10.1 GCC                             |      |
| 10.1.1 GCC RUNTIME LIBRARY EXCEPTION |      |
| 10.1.2 GNU GENERAL PUBLIC LICENSE    | 314  |
| <b>Index</b>                         | 327  |

# **INTRODUCTION**

2D structure diagrams can be considered to be the "natural language" of chemists, since the graphical representation allows molecules to be instantly conceivable.

Historically, 2D representations have mainly been used to visualize the connection table of molecular graphs. However, projecting 3D information into the 2D layout and displaying various atom and bond properties on the molecular diagram open up a novel way to present information to chemists.

The Grapheme TK provides several representation schemes that allow visualization of complex molecular interactions and properties in a clear and coherent 2D format that is the most natural to chemists.

#### **Oxford dictionary definition**

#### grapheme /'grafem/

The smallest meaningful contrastive unit in a writing system.

#### **Wiki definition**

A grapheme is the smallest semantically distinguishing unit in a written language, analogous to the phonemes of spoken languages. A grapheme may or may not carry meaning by itself, and may or may not correspond to a single phoneme.

Graphemes include alphabetic letters, typographic ligatures, Chinese characters, numerical digits, punctuation marks, and other individual symbols of any of the world's writing systems. The word grapheme is derived from Greek gráphō ("write"), and the suffix -eme, by analogy with phoneme and other names of emic units.

Note: This manual provides examples about molecule annotations, drawing 2D molecule surfaces and displaying atom properties on a property map. However, the basic concepts of molecule depiction and image handling are discussed in the OEDepict TK manual. Therefore, studying the OEDepict TK manual is highly recommended prior to reading this documentation.

# **THEORY**

# **2.1 Annotating Atoms and Bonds**

The Grapheme TK provides a framework to annotate atoms and bonds *i.e.* mark them based on their properties. The following Listing 1 example shows how to mark  $sp^2$  and  $sp^3$  hybridized atoms of depicted molecules. After preparing the molecule for 2D depiction and calculating the atom hybridizations, the molecule display object is created (OE2DMolDisplay) that stores the depiction information of a molecule The  $OEAddGJyph$  function is then called to add *glyph* to those atoms for which the given OEIsAtomHybridization functor returns *true*. In this example, the built-in OEAtomGlyphCircle class is used to mark atoms by drawings a circle around them with a specific style  $(OECircleStyle)$ . Finally, the image is written out to a file by calling the OEWriteImage function. The image created by Listing 1 example is shown in Figure: Example of atom annotation.

#### Listing 1: Example of using a built-in atom annotation style

```
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "c1cc(N)cc(S(=0)(=0)0)c1")
oechem.OEAssignHybridization(mol)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(350, 250, oedepict.OEScale_AutoScale)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
disp = oedepict. OE2DMolDisplay(mol, opts)
sp2pen = oedepict.OEPen(oechem.OEWhite, oechem.OEBlueTint, oedepict.OEFill_Off, 1.5)
qlyphSP2 = oegrapheme.OEAtomGlyphCircle(sp2pen, oegrapheme.OECircleStyle Sun, 1.2)
oegrapheme. OEAddGlyph (disp, glyphSP2, oechem. OEIsAtomHybridization (oechem.
→OEHybridization_sp2))
sp3pen = oedepict.OEPen(oechem.OEWhite, oechem.OEPinkTint, oedepict.OEFill_Off, 1.5)
qlyphSP3 = oegrapheme.OEAtomGlyphCircle(sp3pen, oegrapheme.OECircleStyle_Eyelash, 1.2)
oegrapheme. OEAddGlyph(disp, qlyphSP3, oechem. OEIsAtomHybridization(oechem.
\rightarrowOEHybridization_sp3))
oedepict.OERenderMolecule("AnnotateAtomPredicate.png", disp)
```

- OEAddGlyph function
- OEAtomGlyphCircle class
- · OECircleStyle namespace
- OE2DMolDisplay class and OEWriteImage function in the OEDepict TK manual

![](_page_11_Figure_1.jpeg)

Fig. 1: Example of atom annotation

Similarly, the following example shows how to annotate bonds. The bonds being highlighted are specified by the bond predicate passed to the OEAddG1yph function. For each bond the predicate returns  $true$ , *i.e.* if it is a rotatable bond, the OEBondGlyphArrow. RenderGlyph method is invoked that draws an arrow across the middle of the specific bond. The image created by  $Listing$  2 is shown in Figure: Example of bond annotation.

#### Listing 2: Example of using a built-in bond annotation style

```
mol = occhem. OEGraphMol()oechem. OESmilesToMol(mol, "c1cc(NCC)cc(CS (=0) (=0) 0)c1")oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(400, 250, oedepict.OEScale_AutoScale)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
disp = oedepict.OE2DMolDisplay(mol, opts)
pen = oedepict.OEPen(oechem.OEDarkPurple, oechem.OEDarkPurple, oedepict.OEFill_Off, 2.
\leftrightarrow 0)
glyph = oegrapheme. OEBondGlyphArrow (pen, 0.5)
oegrapheme. OEAddGlyph(disp, glyph, oechem. OEIsRotor())
oedepict.OERenderMolecule("AnnotateBondPredicate.png", disp)
```

The following table lists the customizable bond glyphs that are currently available in Grapheme TK.

![](_page_12_Figure_1.jpeg)

Fig. 2: Example of bond annotation

![](_page_12_Figure_3.jpeg)

#### Table 1: Supported bond glyphs

#### See also:

· OEAddGlyph function

The last example shows how to depict non-boolean properties by implementing a user-defined annotation style. User-defined atom and bond annotations can be implemented by deriving from the OEAtomGlyphBase and the OEBondGlyphBase abstract classes and implementing the OEAtomGlyphBase.RenderGlyph and the OEBondGlyphBase. RenderGlyph methods, respectively.

In the Listing 3 example, after calculating the MMFF charges, the atoms are annotated by their charge using the OELinearColorGradient class that interpolates colors. Atoms with negative and positive charge are highlighted by red and blue colors, respectively. The image created by Listing 3 is shown in Figure: Example of user-defined annotation.

#### Listing 3: Example of user-defined annotation

```
class ColorCharge (oegrapheme. OEAtomGlyphBase) :
   def __init__(self, cg):oegrapheme.OEAtomGlyphBase.__init__(self)
        self.colorq = cqdef RenderGlyph (self, disp, atom) :
        adisp = disp.GetAtomDisplay(atom)
        if adisp is None or not adisp. IsVisible():
            return False
        charge = atom.GetPartialChange()if charge == 0.0:
           return True
        color = self.colorg.GetColorAt(charge)
        pen = odeplot. OEPen()pen.SetForeColor(oechem.OEColor(color))
        color.SetA(100)
        pen.SetBackColor(oechem.OEColor(color))
        pen.SetFill(oedepict.OEFill On)
        radius = disp.GetScale() / 2.5layer = disp.GetLayer(oedepict.OELayerPosition_Below)
        oegrapheme. OEDrawCircle(layer, oegrapheme. OECircleStyle_Simpson,
                                adisp.GetCoords(), radius, pen)
        return True
   def CreateCopy(self):
        return ColorCharge(self.colorg)._disown_()
mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, "Cclcc(cc(cl[N+](=0)[O-])F)[N+]#C")
oechem.OEMMFFAtomTypes(mol)
oechem.OEMMFF94PartialCharges(mol)
oedepict.OEPrepareDepiction(mol)
opts = oedepict.OE2DMolDisplayOptions(350, 250, oedepict.OEScale_AutoScale)
opts.SetAtomColorStyle(oedepict.OEAtomColorStyle_WhiteMonochrome)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
disp = oedepict.OE2DMolDisplay(mol, opts)
coloranion = oechem.OEColorStop(-1.0, oechem.OEColor(oechem.OEDarkRed))coloration = occhem.OEColorStop (+1.0, occhem.OEColor (occhem.OEDarkBlue))colorg = oechem. OELinearColorGradient (coloranion, colorcation)
colorg.AddStop(oechem.OEColorStop(0.0, oechem.OEColor(oechem.OEWhite)))
```

colorcharge = ColorCharge(colorg) oegrapheme. OEAddGlyph(disp, colorcharge, oechem. OEIsTrueAtom()) oedepict.OERenderMolecule("AnnotatePartialCharge.png", disp)

![](_page_14_Figure_3.jpeg)

Fig. 3: Example of user-defined annotation

#### See also:

- OEAtomGlyphBase class
- OEBondGlyphBase class
- · OEAddGlyph function
- OELinearColorGradient class

# 2.2 Drawing a Molecule Surface

The 2D representation of the molecule surface is calculated by first drawing circles around each atom of the molecule and then identifying the external arc segments that define a continuous surface around the molecule. This process is illustrated in the table Table: Calculation of the 2D representation of a molecule surface

![](_page_15_Figure_1.jpeg)

Table 2: Calculation of the 2D representation of a molecule surface

The following Listing 1 example shows how to the display a molecule surface. After creating an image object and preparing the molecule for 2D depiction, an arc drawing functor is added to each atom of the molecule by using the OESet SurfaceArcFxn function. The surface then can be drawn by calling the OEDraw2DSurface function that calculates the arc segments that form a continuous curve around the molecule. The image created by Listing 1 is shown in Figure: Example of surface drawing.

## Listing 1: Example of surface drawing

```
opts = oedepict.OE2DMolDisplayOptions(imagewidth, imageheight, oedepict.OEScale_
\rightarrowAutoScale)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
opts.SetScale(oegrapheme.OEGetMoleculeSurfaceScale(mol, opts))
arcfxn = oegrapheme.OEEyelashArcFxn(oedepict.OEPen(oechem.OEGrey, oechem.OEGrey))
for atom in mol. GetAtoms () :
    oegrapheme. OESetSurfaceArcFxn(mol, atom, arcfxn)
disp = oedepict.OE2DMolDisplay(mol, opts)
oegrapheme.OEDraw2DSurface(disp)
```

![](_page_16_Picture_3.jpeg)

Fig. 4: Example of surface drawing

The Listing 1 example uses the OESurfaceArcStyle\_Eyelash style to draw the molecule surface. The following table lists all surface drawing styles that are available in Grapheme TK.

| <b>OEAlphaRainbowArcFxn</b> | <b>OEBrickRoadArcFxn</b>   | <b>OECastleArcFxn</b> | <b>OECogArcFxn</b>           |
|-----------------------------|----------------------------|-----------------------|------------------------------|
| <b>OEDefaultArcFxn</b>      | <b>OEEyelashArcFxn</b>     | <b>OEFlowerArcFxn</b> | <b>OENecklaceArcFxn</b>      |
| <b>OENullArcFxn</b>         | <b>OEOliveBranchArcFxn</b> | <b>OEPearlsArcFxn</b> | <b>OERaceTrackArcFxn</b>     |
| <b>OEStitchArcFxn</b>       | <b>OESunArcFxn</b>         | <b>OEWreathArcFxn</b> | <b>OERailroadTrackArcFxn</b> |

Table 3: Supported surface drawing styles

User-defined surface drawing functors can be implemented by deriving from the OESurfaceArcFxnBase abstract base class. In the Listing 2 example, a user defined arc drawing functor is implemented that colors the eyelash arcs according to the atom they belong to. The image created by Listing 2 is shown in Figure: Example of user-defined surface drawing.

#### Listing 2: Example of user-defined surface drawing

```
class AtomColorArcFxn (oegrapheme. OESurfaceArcFxnBase) :
    def __call_(self, image, arc):
        adisp = arc.GetAtomDisplay()
        if adisp is None or not adisp. IsVisible():
            return False
        color = adisp.GetLabelFont().GetColor()
        pen = oedepict.OEPen(color, color, oedepict.OEFill_Off, 1.0)
        center = arc.GetCenter()radius = arc.GetRadius()
        bgnAngle = arc.GetBgnAngle()
        endAngle = arc.GetEndAngle()oegrapheme. OEDrawEyelashSurfaceArc(image, center, bgnAngle, endAngle, radius,
\rightarrowpen)
        return True
def Draw2DSurface(image, mol):
   oedepict.OEPrepareDepiction(mol)
    opts = oedepict.OE2DMolDisplayOptions(image.GetWidth(), image.GetHeight(),
                                           oedepict.OEScale_AutoScale)
    opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
    opts.SetScale(oegrapheme.OEGetMoleculeSurfaceScale(mol, opts))
    arcfxn = AtomColorArcFxn()for atom in mol. GetAtoms () :
        oegrapheme. OESetSurfaceArcFxn(mol, atom, arcfxn)
   disp = oedepict.OE2DMolDisplay(mol, opts)
    oegrapheme.OEDraw2DSurface(disp)
    oedepict.OERenderMolecule(image, disp)
```

The Listing 3 example shows how to project atom properties, such as partial charges into the molecule surface. The image created by  $Listing$  3 is shown in Figure: Example of depicting atom properties.

#### Listing 3: Example of depicting atom properties on the molecule surface

```
class AtomPartialChargeArcFxn (oegrapheme. OESurfaceArcFxnBase) :
   def _init_(self, colorg):
       oegrapheme.OESurfaceArcFxnBase.__init__(self)
       self.colorg = colorg
   def _call_(self, image, arc):
       adisp = arc.GetAtomDisplay()if adisp is None or not adisp. IsVisible():
           return False
       atom = adisp.GetAtom()if atom is None:
```

![](_page_19_Figure_1.jpeg)

Fig. 5: Example of user-defined surface drawing

#### return False

```
charge = atom.GetPartialCharge()
        if charge == 0.0:
            return True
        color = self.colorg.GetColorAt(charge)
        pen = oedepict.OEPen()
        pen.SetForeColor(color)
        pen.SetLineWidth(2.0)
        center = arc.GetCenter()
        radius = arc.GetRadius()bAngle = arc.GetBgnAngle()
        eAngle = arc.GetEndAngle()
        edgeAngle = 5.0dir = oegrapheme.OEPatternDirection_Outside
        patternAngle = 10.0oegrapheme. OEDrawBrickRoadSurfaceArc(image, center, bAngle, eAngle, radius,
\rightarrowpen,
                                              edgeAngle, dir, patternAngle)
        return True
    def CreateCopy(self):
        return AtomPartialChargeArcFxn(self.colorg)._disown_()
def Draw2DSurfacePartialCharge(image, mol):
```

(continues on next page)

(continued from previous page)

```
oedepict.OEPrepareDepiction(mol)
oechem.OEMMFFAtomTypes(mol)
oechem.OEMMFF94PartialCharges(mol)
opts = oedepict.OE2DMolDisplayOptions(image.GetWidth(), image.GetHeight(),
                                      oedepict.OEScale_AutoScale)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
opts.SetScale(oegrapheme.OEGetMoleculeSurfaceScale(mol, opts))
coloranion = oechem.OEColorStop(-1.0, oechem.OEColor(oechem.OEDarkRed))
colorcation = oechem.OEColorStop(+1.0, oechem.OEColor(oechem.OEDarkBlue))
colorg = oechem. OELinearColorGradient (coloranion, colorcation)
colorg.AddStop(oechem.OEColorStop(0.0, oechem.OEColor(oechem.OEWhite)))
arcfxn = AtomPartialChargeArcFxn (colorg)for atom in mol. GetAtoms () :
    oegrapheme. OESetSurfaceArcFxn(mol, atom, arcfxn)
disp = oedefict.OE2DMolDisplay(mol, opts)oegrapheme.OEDraw2DSurface(disp)
oedepict.OERenderMolecule(image, disp)
```

![](_page_20_Figure_3.jpeg)

Fig. 6: Example of depicting atom properties

#### See also:

• OELinearColorGradient class in the OEDepict TK manual

It is also possible to draw multiple 2D surfaces arc-by-arc. In the Listing 4 example below the arcs returned by the OEGet2DSurfaceArcs function for the given atom display and radius are directly rendered below the molecule diagram. In this case it is important to call the OEGetMoleculeSurfaceScale function with the largest radius

scale of the 2D surfaces drawn. This reduces the scaling of the molecule in order to able to fit the molecule diagram and all of the arcs of the 2D surfaces into the image. The image created by Listing 4 is shown in Figure: Example of drawing multiple 2D surfaces.

```
Listing 4: Example of drawing multiple 2D surfaces
```

```
def Draw2DSurface(disp, atompred, radius, color):
    penA = oedepict.OEPen(color, color, oedepict.OEFill_Off, 2.0)
    arcfxnA = oeqrapheme.OEDefaultArcFan(penA)penB = oedepict.OEPen(oechem.OELightGrey, oechem.OELightGrey, oedepict.OEFill Off,
\rightarrow 2.0oedepict.OEStipple_ShortDash)
    arcfxnB = oegrapheme.OEDefaultArcFxn(penB)
    layer = disp.GetLayer(oedepict.OELayerPosition_Below)
    for adisp in disp. GetAtomDisplays():
        for arc in oegrapheme. OEGet2DSurfaceArcs(disp, adisp, radius):
            if atompred(adisp.GetAtom()):
                arcfxnA(layer, arc)
            else:
                arcfxnB(layer, arc)
def Draw2DSurfaces(image, mol):
   oedepict.OEPrepareDepiction(mol)
    opts = oedepict.OE2DMolDisplayOptions(image.GetWidth(), image.GetHeight(),
                                           oedepict.OEScale_AutoScale)
    opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
    opts.SetScale(oegrapheme.OEGetMoleculeSurfaceScale(mol, opts, 1.50))
   disp = oedepict.OE2DMolDisplay(mol, opts)
    Draw2DSurface(disp, oechem.OEHasAtomicNum(oechem.OEElemNo_C), 1.00, oechem.
\rightarrowOEBlack)
    Draw2DSurface(disp, oechem.OEHasAtomicNum(oechem.OEElemNo_N), 1.25, oechem.
\rightarrowOEDarkBlue)
   Draw2DSurface(disp, oechem.OEHasAtomicNum(oechem.OEElemNo_O), 1.50, oechem.
\rightarrowOEDarkRed)
    oedepict.OERenderMolecule(image, disp)
```

See also:

OESurfaceArcScale namespace

The last Listing 5 example shows how to draw a 2D surface with various radii. It draws two surfaces one with a minimum radius scale and one with various radius depending on the covalent radius of the atoms. The OEGetMoleculeSurfaceScale function has to be called in this example too with the largest radius scale in order to able to fit the molecule diagram and all of the arcs of the 2D surfaces into the image. The image created by Listing 5 is shown in Figure: Example of drawing 2D surface with various radii.

![](_page_22_Figure_1.jpeg)

Fig. 7: Example of drawing multiple 2D surfaces

#### Listing 5: Example of drawing 2D surface with various radii

```
def DrawSurfaces(image, mol):
   oechem.OEAssignCovalentRadii(mol)
   minradius = oechem.OEGetCovalentRadius(oechem.OEElemNo_H)
    radiusScales = oechem.OEDoubleVector(mol.GetMaxAtomIdx(), 0.0)
   maxrscale = float("-inf")for atom in mol. GetAtoms () :
       rscale = (atom.GetRadius() - minradius) + oegrapheme.OESurfaceArcScale_Minimum
       radiusScales[atom.GetIdx()] = rscalemaxrscale = max(maxrscale, rscale)opts = oedepict.OE2DMolDisplayOptions(image.GetWidth(), image.GetHeight(),
                                          oedepict.OEScale_AutoScale)
   opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
   opts.SetScale(oegrapheme.OEGetMoleculeSurfaceScale(mol, opts, maxrscale))
   disp = oedepict.OE2DMolDisplay(mol, opts)
    layer = disp.GetLayer(oedepict.OELayerPosition_Below)
   penA = oedepict.OEPen(oechem.OELightGrey, oechem.OELightGrey, oedepict.OEFill_Off,
\rightarrow 2.0,
                          oedepict.OEStipple_ShortDash)
    arcfxnA = oegrapheme.OEDefaultArcFixn(penA)for arc in oegrapheme. OEGet2DSurfaceArcs(disp, oegrapheme. OESurfaceArcScale_
```

```
\rightarrowMinimum):
```

```
arcfxnA(layer, arc)
penB = oedepict.OEPen(oechem.OEGrey, oechem.OEGrey, oedepict.OEFill_Off, 2.0)
arcfxnB = oegrapheme.OEDefaultArcFxn(penB)
for arc in oegrapheme. OEGet2DSurfaceArcs(disp, radiusScales):
    arcfxnB(layer, arc)
oedepict.OERenderMolecule(image, disp)
```

![](_page_23_Figure_3.jpeg)

Fig. 8: Example of drawing 2D surface with various radii

#### See also:

OEGetCovalentRadius function in the OEChem TK manual

# 2.3 Drawing a Ligand-Protein Complex Surface

The previous chapter demonstrates how to draw and customize 2D molecule surfaces. Grapheme TK also provides a method that depicts a ligand-protein complex in which the arcs of the 2D surface of the molecule are annotated based on the distance between the accessible surfaces of the ligand and the surrounding protein (OEMakeAccessibleSurface). Based on this calculation, the atoms of the ligand are divided into four categories which are then inherited by the corresponding arcs when the 2D molecule surface of the ligand is drawn. These four types are the following:

1. Solvent (OEDefaultSolventArcFxn)

A surface arc is depicted using the *solvent* style if the corresponding atom is accessible to a solvent. (See *Figure*: Example of the 'solvent' arc style)

2. Cavity (OEDefaultCavityArcFxn)

![](_page_24_Picture_1.jpeg)

Fig. 9: Example of the 'solvent' arc style

A surface arc is depicted using the *cavity* style if in the region of the corresponding atom, a cavity is detected between the ligand and the receptor molecule surfaces. The cavity is large enough to allow expanding the ligand in this region without bumping into the receptor. (See Figure: Example of the cavity arc style)

![](_page_24_Picture_4.jpeg)

Fig. 10: Example of the 'cavity' arc style

#### 3. Void (OEDefaultVoidArcFxn)

A surface arc is depicted using the *void* style, if in the region of the corresponding atom a small interstice is detected between the ligand and the receptor molecule surfaces. (See Figure: OEDefaultBuriedArcFxn)

![](_page_24_Picture_8.jpeg)

Fig. 11: Example of the 'void' arc style

#### 4. Buried (OEDefaultBuriedArcFxn)

A surface arc is depicted using the *buried* style, if in the region of the corresponding atom the ligand is tightly fit to the receptor. (See Figure: Example of the buried arc style)

![](_page_24_Figure_12.jpeg)

Fig. 12: Example of the 'buried' arc style

Note: Even though, Spicoli TK is used to generate the accessible surfaces of the ligand and the receptor, no Spicoli

**TK** license is required to call the *OEAddComplexSurfaceArcs* function.

The following Listing 1 example show how to display the surface of the ligand-protein complex. After importing the ligand and the receptor structures, the OEAddComplexSurfaceArcs function is called to generate the accessible molecule surfaces (using Spicoli TK) and assign the surface drawing styles (solvent, buried, void, or cavity) for the atoms of the ligand. These styles are the used to draw the arcs of the molecule surface when the OEDraw2DSurface function is invoked. The OEGetMoleculeSurfaceScale function is used to reduce the scaling of the molecule in order to be able to fit both the molecule diagram and the molecule surface into the image.

#### Listing 1: Example of complex surface drawing

```
def ImportMolecule(filename):
    if s = oechem. oemolistream()if not ifs.open(filename):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % filename)
   mol = occhem.OEGraphMol()if not oechem. OEReadMolecule(ifs, mol):
        oechem. OEThrow. Fatal ("Unable to read molecule in %s" % filename)
    oechem.OEAssignBondiVdWRadii(mol)
    oechem.OESuppressHydrogens(mol)
    return mol
if len(sys.argv) != 3:
   oechem.OEThrow.Usage("%s <receptor> <ligand>" % sys.argv[0])
receptor = ImportMolecule(sys.argv[1])ligand = ImportMolecule(sys.argv[2])
oegrapheme. OEAddComplexSurfaceArcs(ligand, receptor)
oegrapheme.OEPrepareDepictionFrom3D(ligand)
width, height = 450, 350
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts. SetScale(oegrapheme. OEGetMoleculeSurfaceScale(ligand, opts))
disp = oedepict.OE2DMolDisplay(ligand, opts)
oegrapheme.OEDraw2DSurface(disp)
oedepict.OERenderMolecule("DrawComplexSurface.png", disp)
```

The following snapshot (*Figure: Dihydrofolate reductase*) displays the ligand of the 2w3a PDB complex in VIDA with the accessible surface of the protein. The image shown in the Figure: The Grapheme representation of the  $2w3a$ complex is created by Listing 1 code for the same ligand-protein complex.

User-defined solvent and buried surface drawing styles can be implemented by deriving from the OESurfaceArcFxn-Base base class. Similarly, user-defined *cavity* and *void* surface drawing styles can be implemented by deriving from the OEComplexSurfaceArcFxnBase base class. This later abstract class also stores the relative distance calculated between the ligand and the receptor. The following code snippet shows how to use this *depth* to emphasize the volume of the cavity by adjusting the size of the *spikes* when drawing the surface arcs using the *OEDrawSunSurfaceArc* function

![](_page_26_Picture_1.jpeg)

Fig. 13: Dihydrofolate reductase complexed with trimethoprim in VIDA (PDB 2w3a)

```
def DrawSurfaceArc(image, depth, arc, pen):
   edgeAngle = 5.0patternAngle = 5.0minPatternWidthRatio = 0.05maxPatternWidthRatio = 0.10 * depthpatternDirection = oegrapheme.OEPatternDirection_Outside
   oegrapheme.OEDrawSunSurfaceArc(image, arc.GetCenter(), arc.GetBgnAngle(), arc.
\rightarrowGetEndAngle(),
                                   arc.GetRadius(), pen, edgeAngle,
                                   patternDirection, patternAngle,
                                   minPatternWidthRatio, maxPatternWidthRatio)
class SolventArcFxn (oegrapheme. OESurfaceArcFxnBase) :
   def _call_(self, image, arc):
        pen = oedepict.OEPen(oechem.OELightGrey, oechem.OELightGrey)
        pen.SetLineWidth(0.5)
        oegrapheme.OEDrawDefaultSurfaceArc(image, arc.GetCenter(), arc.GetBgnAngle(),
                                           arc.GetEndAngle(), arc.GetRadius(), pen)
        return True
class BuriedArcFxn (oegrapheme. OESurfaceArcFxnBase) :
   def __call_(self, image, arc):
```

# Trimethoprim NΗ, $NH<sub>2</sub>$

Fig. 14: The Grapheme representation of the 2w3a complex

(continued from previous page)

```
pen = oedepict. OEPen (oechem. OEGrey, oechem. OEGrey)
        pen.SetLineWidth(2.0)
        oegrapheme.OEDrawDefaultSurfaceArc(image, arc.GetCenter(), arc.GetBgnAngle(),
                                            arc.GetEndAngle(), arc.GetRadius(), pen)
        return True
class CavityArcFxn (oegrapheme. OEComplexSurfaceArcFxnBase) :
    def _call_(self, image, arc):
        pen = oedepict. OEPen (oechem. OEBlack, oechem. OEBlack)
        pen.SetLineWidth(2.0)
        DrawSurfaceArc(image, self.GetDepth(), arc, pen)
        return True
class VoidArcFxn (oegrapheme. OEComplexSurfaceArcFxnBase) :
   def _call_(self, image, arc):
        pen = oedepict. OEPen (oechem. OEDarkGrey, oechem. OEDarkGrey)
        pen.SetLineWidth(2.0)
        DrawSurfaceArc(image, self.GetDepth(), arc, pen)
        return True
```

These arc drawing predicates then can be used to draw the surface of the ligand-protein complex when calling the OEAddComplexSurfaceArcs function. The image created is shown in Figure: Example of user-defined surface drawing.

 $sfxn = SolventArcFxn()$  $bfan = BuriedArcFan()$  $cfxn = CavityArcFxn()$  $vfxn = VoidArcFxn()$ oegrapheme. OEAddComplexSurfaceArcs(ligand, receptor, sfxn, bfxn, cfxn, vfxn)

# Trimethoprim

![](_page_28_Figure_4.jpeg)

Fig. 15: Example of user-defined surface drawing

#### See also:

• Surface Generation chapter in the Spicoli TK manual

# **2.4 Depicting Property Maps**

The previous chapters give examples about how to depict atom properties either by using glyphs (see Annotating Atoms and Bonds chapter) or projecting them into a 2D molecule surface (see Drawing a Molecule Surface chapter). **Grapheme TK** can also map atom properties into a 2D grid, called a property map, using a Gaussian function. After the grid is generated, colors are rendered to each cell using the OELinearColorGradient class that interpolates colors between a specified range.

The following Listing 1 example demonstrates how to depict partial charges using the property map. After constructing the molecule and preparing it for depiction, the MMFF partial charges are calculated. These partial charges are attached to the corresponding atom as generic data with a specific tagname. A OE2DPropMap object is then generated by specifying three colors:

- the background color of the property map
- one that represents negative values (in this case charges), and
- the color that represents positive values in the property map

When the OE2DPropMap. Render method is called with the *tagname*, the properties that were attached to the atoms as generic data are retrieved and a 2D grid is generated along with an OELinearColorGradient object that is used to assign colors to the cells of the grid. The colored grid is then rendered into the below layer of the OE2DMolDisplay object, *i.e.*, it appears underneath the molecular diagram. The image created by  $Listing \, 1$  is shown in *Figure*: Example of depicting a property map.

#### Listing 1: Depicting partial charges using property map

```
def SetPartialCharge(mol, tagname):
    oechem.OEMMFFAtomTypes(mol)
    oechem.OEMMFF94PartialCharges(mol)
    tag = oechem. OEGetTag (tagname)
    for atom in mol. GetAtoms () :
        atom. SetData (tag, atom. GetPartialCharge () )
mol = oechem.OEGraphMol()
oechem.OESmilesToMol(mol, "Cclcc(cc(cl[N+](=0)[O-])F)[N+]#C")
oedepict.OEPrepareDepiction(mol)
tagname = "PartialChange"SetPartialCharge(mol, tagname)
width, height = 450, 350
opts = oedepict.OE2DMolDisplayOptions(width, height, oedepict.OEScale_AutoScale)
opts.SetAtomColorStyle(oedepict.OEAtomColorStyle_WhiteMonochrome)
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
opts.SetScale(oegrapheme.OEGetMoleculeSurfaceScale(mol, opts))
disp = oedepict.OE2DMolDisplay(mol, opts)
propmap = oegrapheme. OE2DPropMap(opts. GetBackgroundColor())
propmap.SetNegativeColor(oechem.OEDarkRed)
propmap.SetPositiveColor(oechem.OEDarkBlue)
propmap. Render (disp, tagname)
oedepict.OERenderMolecule("Draw2DPropMapPartialCharge.pnq", disp)
```

![](_page_30_Figure_1.jpeg)

Fig. 16: Example of depicting a property map

## See also:

• Generic Data chapter in the OEChem TK manual.

When the  $OE2DPropMap$ . Render method is called, the color gradient is initialized by searching for the minimum and maximum values by the given *tagname*. This means that when more than one molecule is depicted, each depiction will have its own independent value range. (See Figure: Example of depicting a property map).

In the Listing 2 example, the value range of the property map is pre-set by identifying the minimum and maximum atom partial charges for a whole molecule set. See the result in *Figure: Example of depicting property maps in the* same value range. Each black box around the color gradient legend indicates the range of the atom partial charges for the corresponding molecule.

![](_page_31_Figure_1.jpeg)

![](_page_31_Figure_2.jpeg)

![](_page_31_Figure_3.jpeg)

```
def SetPartialCharge (mol, tagname, minvalue, maxvalue) :
    oechem.OEMMFFAtomTypes(mol)
    oechem.OEMMFF94PartialCharges(mol)
    tag = oechem. OEGetTag (tagname)
    for atom in mol. GetAtoms () :
        charge = atom.GetPartialChange()atom. SetData (tag, charge)
        minvalue = min(minvalue, charge)maxvalue = max(maxvalue, charge)return minvalue, maxvalue
smiles = ["c1cenc(c1) [N+] (=0) [0-]","cleecee1F",
          "clccc(ccl) S (=0) (=0) [0-]"]minvalue = float("inf")maxvalue = float("-inf")tagname = "PartialCharge"
molecules = []for smi in smiles:
   mol = occhem. OEGraphMol()oechem.OESmilesToMol(mol, smi)
    oedepict.OEPrepareDepiction(mol)
    minvalue, maxvalue = SetPartialCharge(mol, tagname, minvalue, maxvalue)
    molecules.append(oechem.OEGraphMol(mol))
width, height = 750, 250
image = oedepict. OEImage (width, height)
rows, \text{cols} = 1, 3
grid = oedepict.OEImageGrid(image, rows, cols)
opts = \text{oederict.OE2DMolDisplayOptions (grid. GetCellWidth(), grid. GetCellHeight(),
```

![](_page_32_Figure_2.jpeg)

![](_page_32_Figure_3.jpeg)

Fig. 18: Example of depicting a property maps in the same value range

#### See also:

• OEImageGrid class in the **OEDepict TK** manual

The above examples show how to project atom properties (such as partial charges) into the property map. However, the OE2DPropMap class can also be used to visualize bond properties by attaching a value to each bond as a generic data using a *tagname*. When the *OE2DPropMap*. Render method is called with the same *tagname*, the property that was attached to a bond is retrieved and projected at the middle of that bond before applying a Gaussian function to blur out the 2D grid underneath the molecular graph. The Table: Depicting atom or/and bond properties table shows the differences between visualizing atom or/and bond properties using the OE2DPropMap class.

![](_page_33_Figure_1.jpeg)

Table 4: Depicting atom or/and bond properties

## **THREE**

# **EXAMPLES**

## 3.1 Grapheme Examples

The following table lists the currently available Grapheme TK examples:

| Program                 | Description                             |
|-------------------------|-----------------------------------------|
| <i>bfactor2img</i>      | depicting BFactor                       |
| <i>complex2img</i>      | depicting active site interactions      |
| <i>shapeoverlap2pdf</i> | depicting shape and color atom overlaps |

#### **Examples:**

## 3.1.1 Depicting BFactor

A program that depicts the B-factor of a ligand and its environment.

See also:

- Visualizing Protein-Ligand B-Factor OpenEye Python Cookbook example
- Visualizing Protein-Ligand B-Factor Map OpenEye Python Cookbook example

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python bfactor2img.py --help

will generate the following output:

```
[-complex] <input> [-out] <output pdf>
Simple parameter list
   -height : Height of output image
   -width : Width of output image
   SplitMolComplex options :
     -ligandname : Ligand name
    input/output options
      -complex : Input filename of the protein complex
```

```
-out : Output filename
```

```
molecule display options
  -aromstyle : Aromatic ring display style
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
# Depicts the BFactor of a ligand and its environment
#######################################
import sys
from openeye import oechem
from openeye import oedepict
from openeye import oegrapheme
def main(argv=[__name__]):
   itf = oechem. 0EInterface()oechem. OEConfigure(itf, InterfaceData)
   oedepict.OEConfigureImageWidth(itf, 600.0)
   oedepict.OEConfigureImageHeight(itf, 600.0)
   oedepict.OEConfigure2DMolDisplayOptions(itf, oedepict.OE2DMolDisplaySetup_
\rightarrowAromaticStyle)
   oechem.OEConfigureSplitMolComplexOptions(itf, oechem.OESplitMolComplexSetup_
\rightarrowLiqName)
   if not oechem. OEParseCommandLine(itf, argv):
       return 1
    iname = itf.GetString("-complex")oname = \text{iff}. \text{GetString}("-out")if s = oechem. oemolistream()if not ifs.open(iname):
       oechem. OEThrow. Fatal ("Cannot open input file!")
```

```
ext = oechem.OEGetFileExtension(oname)
   if not oedepict. OEIsRegisteredImageFile(ext):
        oechem. OEThrow. Fatal ("Unknown image type!")
   ofs = occhem.oeofstream()if not ofs.open(oname):
        oechem. OEThrow. Fatal ("Cannot open output file!")
   complexmol = oechem. OEGraphMol()
   if not oechem. OEReadMolecule(ifs, complexmol):
        oechem. OEThrow. Fatal ("Unable to read molecule from %s" % iname)
   if not oechem. OEHasResidues (complexmol) :
        oechem.OEPerceiveResidues(complexmol, oechem.OEPreserveResInfo All)
    # Separate ligand and protein
   sopts = oechem.OESplitMolComplexOptions()
   oechem.OESetupSplitMolComplexOptions(sopts, itf)
   ligand = oechem. OEGraphMol()
   protein = oechem. OEGraphMol()
   water = oechem. OEGraphMol()
   other = oechem. OEGraphMol()
   oechem. OESplitMolComplex (ligand, protein, water, other, complexmol, sopts)
   if ligand. NumAtoms () == 0:
        oechem. OEThrow. Fatal ("Cannot separate complex!")
    # Calculate average BFactor of the whole complex
   avgbfactor = GetAverageBractor(complexmol)# Calculate minimum and maximum BFactor of the ligand and its environment
   minbfactor, maxbfactor = GetMinAndMaxBFactor(ligand, protein)
    # Attach to each ligand atom the average BFactor of the nearby protein atoms
   stag = "avg residue BFactor"itag = oechem. OEGetTag (stag)
   SetAverageBFactorOfNearbyProteinAtoms(ligand, protein, itag)
   oechem. OEThrow. Info ("Average BFactor of the complex = *+. 3f'' * avgbfactor)
   oechem. OEThrow. Info ("Minimum BFactor of the ligand and its environment = *+3f" *.
\rightarrowminbfactor)
   oechem. OEThrow. Info ("Maximum BFactor of the ligand and its environment = \frac{8}{5} + .3f" \frac{8}{5}.
\rightarrowmaxbfactor)
    # Create image
   imagewidth, imagcheight = oedepict.OEGetImageWidth(itf), oedepict.\rightarrow OEGet Image Height (itf)
   image = oedepict.OEImage(imagewidth, imageheight)
```

```
(continued from previous page)
```

```
mframe = oedepict.OEImageFrame(image, imagewidth,
                                  imageheight * 0.90, oedepict. OE2DPoint (0.0, 0.0))
   lframe = oedepict. OEImageFrame(image, imagewidth, imageheight * 0.10,
                                  oedepict.OE2DPoint(0.0, imageheight * 0.90))
   opts = oedepict.OE2DMolDisplayOptions(mframe.GetWidth(), mframe.GetHeight(),
                                         oedepict.OEScale_AutoScale)
   oedepict.OESetup2DMolDisplayOptions(opts, itf)
   opts.SetAtomColorStyle(oedepict.OEAtomColorStyle_WhiteMonochrome)
    # Create BFactor color gradient
   colorg = oechem. OELinearColorGradient()
   colorg.AddStop(oechem.OEColorStop(0.0, oechem.OEDarkBlue))
   colorg.AddStop(oechem.OEColorStop(10.0, oechem.OELightBlue))
   colorg.AddStop(oechem.OEColorStop(25.0, oechem.OEYellowTint))
   colorg.AddStop(oechem.OEColorStop(50.0, oechem.OERed))
   colorg.AddStop(oechem.OEColorStop(100.0, oechem.OEDarkRose))
    # Prepare ligand for depiction
   oegrapheme.OEPrepareDepictionFrom3D(ligand)
   arcfxn = BFactorArcFxn (colorq, itaq)for atom in ligand. GetAtoms () :
       oegrapheme. OESetSurfaceArcFxn(ligand, atom, arcfxn)
   opts.SetScale(oegrapheme.OEGetMoleculeSurfaceScale(ligand, opts))
    # Render ligand and visualize BFactor
   disp = oedepict.OE2DMolDisplay(ligand, opts)
   colorbfactor = ColorLigandAtomByBFactor(colorg)
   oegrapheme. OEAddGlyph (disp, colorbfactor, oechem. OEIsTrueAtom () )
   oegrapheme.OEDraw2DSurface(disp)
   oedepict.OERenderMolecule(mframe, disp)
    # Draw color gradient
   opts = oegrapheme.OEColorGradientDisplayOptions()
   opts.SetColorStopPrecision(1)
   opts.AddMarkedValue(avgbfactor)
   opts.SetBoxRange(minbfactor, maxbfactor)
   oegrapheme.OEDrawColorGradient(lframe, colorg, opts)
   oedepict.OEWriteImage(oname, image)
   return 0
   #######################################
######################################
def GetAverageBFactor(mol):
   sumbfactor = 0.0for atom in mol. GetAtoms () :
```

```
res = oechem.OEAtomGetResidue(atom)
        sumbfactor += res. GetBFactor()
    avgbfactor = sumbfactor / mol.WumAtoms()return avgbfactor
def ConsiderResidueAtom(atom, res):
   if atom.GetAtomicNum() == oechem.OEElemNo_H:
        return False
    if res.GetName() == "HOH":return False
    return True
def GetMinAndMaxBFactor(ligand, protein, maxdistance=4.0):
   minbfactor = float("inf")maxbfactor = float("-inf")# Ligand atoms
    for latom in ligand. GetAtoms (oechem. OEIsHeavy ()) :
        res = oechem.OEAtomGetResidue(latom)
        minbfactor = min(minfactor, res.GetBFactor())maxbfactor = max(maxbfactor, res.GetBFactor())
    # Protein atoms close to ligand atoms
   nn = oechem. OENearestNbrs (protein, maxdistance)
    for latom in ligand. GetAtoms (oechem. OEIsHeavy ()) :
        for neigh in nn. GetNbrs (latom) :
            ratom = neigh.GetBgn()res = oechem.OEAtomGetResidue(ratom)
            if ConsiderResidueAtom(ratom, res):
                minbfactor = min(minbfactor, res.GetBFactor())maxbfactor = max(maxbfactor, res.GetBFactor())
    return minbfactor, maxbfactor
def SetAverageBFactorOfNearbyProteinAtoms(ligand, protein, itag, maxdistance=4.0):
   nn = oechem. OENearestNbrs (protein, maxdistance)
    for latom in ligand. GetAtoms (oechem. OEIsHeavy ()) :
        sumbfactor = 0.0neights = []for neigh in nn. GetNbrs (latom) :
            ratom = neigh.GetBqn()res = oechem. OEAtomGetResidue (ratom)
            if ConsiderResidueAtom(ratom, res):
                sumbfactor += res. GetBFactor()
                neighs.append(ratom)
        avgbfactor = 0.0if len(neighs) > 0:
            avqbfactor = sumbfactor / len(neighs)latom.SetDoubleData(itag, avgbfactor)
```

```
#######################################
#######################################
class BFactorArcFxn (oegrapheme. OESurfaceArcFxnBase) :
   def __init_(self, colorg, itag):
       oegrapheme.OESurfaceArcFxnBase.__init__(self)
       self.colorg = colorg
       self.itag = itag
   def _call_(self, image, arc):
       adisp = arc.GetAtomDisplay()if adisp is None or not adisp. IsVisible():
          return False
       atom = adisp.GetAtom()if atom is None:
           return False
       avgresiduebfactor = atom.GetDoubleData(self.itag)
       if avgresiduebfactor == 0.0:
           return True
       color = self.colorg.GetColorAt(avgresiduebfactor)
       pen = oedepict.OEPen(color, color, oedepict.OEFill_Off, 5.0)
       center = arc.GetCenter()bAngle = arc.GetBgnAngle()
       eAngle = arc.GetEndAngle()
       radius = arc.GetRadius()
       oegrapheme. OEDrawDefaultSurfaceArc(image, center, bAngle, eAngle, radius, pen)
       return True
   def CreateCopy (self) :
       return BFactorArcFxn(self.colorg, self.itag)._disown_()
#######################################
#######################################
class ColorLigandAtomByBFactor (oegrapheme. OEAtomGlyphBase) :
   def _init_(self, colorg):
       oegrapheme.OEAtomGlyphBase.__init__(self)
       self.colorg = colorg
   def RenderGlyph (self, disp, atom) :
       adisp = disp.GetAtomDisplay(atom)if adisp is None or not adisp. IsVisible():
          return False
       res = oechem. OEAtomGetResidue (atom)
       bfactor = res. GetBFactor()
       color = self.colorg.GetColorAt (bfactor)
```

```
pen = oedepict. OEPen(color, color, oedepict. OEFill_On, 1.0)
       radius = disp.Getscale() / 3.0layer = disp.GetLayer(oedepict.OELayerPosition_Below)
       oegrapheme. OEDrawCircle(layer, oegrapheme. OECircleStyle_Default,
                               adisp.GetCoords(), radius, pen)
       return True
   def CreateCopy(self):
       return ColorLigandAtomByBFactor(self.colorg)._disown_()
#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-complex] <input> [-out] <output pdf>
!CATEGORY "input/output options :"
 !PARAMETER -complex
   !ALIAS -c!TYPE string
   !KEYLESS 1
   !REQUIRED true
   !VISIBILITY simple
   !BRIEF Input filename of the protein complex
  !END
  !PARAMETER -out
   !ALIAS -0
    !TYPE string
   !REOUIRED true
   IKEYLESS<sub>2</sub>
   !VISIBILITY simple
   !BRIEF Output filename
 ! END
! END
\mathbf{Y} \in \mathbf{Y} \times \mathbf{Y}if _name_ = = "_main_".sys.exit(main(sys.argv))
```

- OESplitMolComplex function in OEChem TK
- OENearestNbrs class in OEChem TK
- OEPrepareDepictionFrom3D function
- OESurfaceArcFxnBase class and OEDraw2DSurface function
- OEAtomGlyphBase class and OEAddGlyph function

#### **Examples**

prompt> python bfactor2img.py -complex 1MEH.pdb -ligandname MOA -out MOA.png

will generate the following output:

```
Average BFactor of the complex = +32.721Minimum BFactor of the ligand and its environment = +21.500Maximum BFactor of the ligand and its environment = +72.060
```

and the image shown in Figure: Example of depicting the BFactor of MOA and its environment.

![](_page_41_Figure_6.jpeg)

Fig. 1: Example of depicting the BFactor of MOA and its environment

prompt> python bfactor2img.py -complex 1LEE.pdb -ligandname R36 -out R36.png

will generate the following output:

```
Average BFactor of the complex = +23.754Minimum BFactor of the ligand and its environment = +6.040Maximum BFactor of the ligand and its environment = +32.050
```

and the image shown in Figure: Example of depicting the BFactor of R36 and its environment.

![](_page_42_Figure_5.jpeg)

Fig. 2: Example of depicting the BFactor of R36 and its environment

## 3.1.2 Depicting Active Site Interactions

A program that depicts receptor-ligand interactions.

#### See also:

• Visualizing Protein-Ligand Interactions OpenEye Python Cookbook example

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python complex2img.py --help

will generate the following output:

```
[-complex] <input> [-out] <output image>
Simple parameter list
   -height : Height of output image
   -width : Width of output image
   SplitMolComplex options :
     -ligandname : Ligand name
    input/output options
     -complex : Input filename of the protein complex
     -out : Output filename
   molecule display options
     -aromstyle : Aromatic ring display style
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
# Depicts the interactions of an active site
#######################################
```

```
import sys
from openeye import oechem
from openeye import oedepict
from openeye import oegrapheme
def main(arqv=[ name ]):
   itf = oechem. 0EInterface()oechem. OEConfigure(itf, InterfaceData)
   oedepict.OEConfigureImageWidth(itf, 900.0)
   oedepict.OEConfigureImageHeight(itf, 600.0)
   oedepict.OEConfigure2DMolDisplayOptions(itf, oedepict.OE2DMolDisplaySetup_
\rightarrowAromaticStyle)
    oechem.OEConfigureSplitMolComplexOptions(itf, oechem.OESplitMolComplexSetup_
\rightarrowLigName)
    if not oechem. OEParseCommandLine(itf, argv):
        return 1
    iname = itf.GetString("-complex")oname = itf.GetString("-out")if s = oechem.oemolistream()if not ifs.open(iname):
        oechem. OEThrow. Fatal ("Cannot open input file!")
    ext = oechem.OEGetFileExtension(oname)
    if not oedepict. OEIsRegisteredImageFile(ext):
        oechem. OEThrow. Fatal ("Unknown image type!")
    ofs = occhem.oeofstream()if not ofs.open(oname):
        oechem. OEThrow. Fatal ("Cannot open output file!")
    complexmol = oechem.OEGraphMol()
    if not oechem. OEReadMolecule(ifs, complexmol) :
        oechem. OEThrow. Fatal ("Unable to read molecule from %s" % iname)
    if not oechem. OEHasResidues (complexmol):
        oechem.OEPerceiveResidues(complexmol, oechem.OEPreserveResInfo_All)
    # Separate ligand and protein
    sopts = oechem.OESplitMolComplexOptions()
    oechem.OESetupSplitMolComplexOptions(sopts, itf)
    ligand = oechem. OEGraphMol()protein = oechem. OEGraphMol()
    water = occhem.OEGraphMol()other = oechem. OEGraphMol()
   pfilter = sopts.GetProteinFilter()
   wfilter = spots.GetWaterFilter()sopts.SetProteinFilter(oechem.OEOrRoleSet(pfilter, wfilter))
    sopts.SetWaterFilter(oechem.OEMolComplexFilterFactory(
```

```
(continued from previous page)
                        oechem.OEMolComplexFilterCategory_Nothing))
   oechem.OESplitMolComplex(ligand, protein, water, other, complexmol, sopts)
   if ligand. NumAtoms () == 0:
       oechem. OEThrow. Fatal ("Cannot separate complex!")
    # Perceive interactions
   asite = oechem. 0EInteractionHintCondition (protein, ligand)if not asite. IsValid():
       oechem. OEThrow. Fatal ("Cannot initialize active site!")
   asite.SetTitle(ligand.GetTitle())
   oechem.OEPerceiveInteractionHints(asite)
   oegrapheme.OEPrepareActiveSiteDepiction(asite)
    # Depict active site with interactions
   width, height = oedepict. OEGetImageWidth(itf), oedepict. OEGetImageHeight(itf)
   image = oedepict.OEImage(width, height)
   cframe = oedepict.OEImageFrame(image, width * 0.80, height, oedepict.OE2DPoint(0.
\rightarrow 0, 0.0)lframe = oedepict. OEImageFrame (image, width * 0.20, height,
                                  oedepict.OE2DPoint(width * 0.80, 0.0))
   opts = oegrapheme.OE2DActiveSiteDisplayOptions(cframe.GetWidth(), cframe.
\rightarrowGetHeight())
   oedepict.OESetup2DMolDisplayOptions(opts, itf)
    adisp = oegrapheme. OE2DActiveSiteDisplay(asite, opts)oegrapheme.OERenderActiveSite(cframe, adisp)
   lopts = oegrapheme. OE2DActiveSizeLegendDisplayOptions (10, 1)oegrapheme. OEDrawActiveSiteLegend(lframe, adisp, lopts)
   oedepict.OEWriteImage(oname, image)
   return 0
#######################################
# INTERFACE
#######################################
InterfaceData = ''''!BRIEF [-complex] <input> [-out] <output image>
!CATEGORY "input/output options :"
 !PARAMETER -complex
   !ALIAS -c!TYPE string
    !KEYLESS 1
    !REQUIRED true
```

```
!VISIBILITY simple
    !BRIEF Input filename of the protein complex
  !END
  !PARAMETER -out
    !ALIAS -0
    !TYPE string
    !REQUIRED true
    !KEYLESS 2
    !VISIBILITY simple
    !BRIEF Output filename
  ! END
!END
\mathbf{r} \cdot \mathbf{r} \cdot \mathbf{r}if _name_ = = "_main_".sys.exit(main(sys.argv))
```

#### See also:

- · OESplitMolComplex function in OEChem TK
- OEInteractionHintContainer class in OEChem TK
- OEPerceiveInteractionHints function in OEChem TK
- · OEPrepareActiveSiteDepiction function
- OE2DActiveSiteDisplayOptions class
- OE2DActiveSiteDisplay class and OERenderActiveSite function
- · OEDrawActiveSiteLegend function

#### **Examples**

prompt> python complex2img.py -complex pdblbr6.ent -out 1br6-PT1.png

will generate the image shown in Figure: Example of depicting the receptor-ligand interaction (PDB: 1br6).

prompt> python complex2img.py -complex pdbleoc.ent -out 1eoc-4NC.png

will generate the image shown in Figure: Example of depicting the receptor-ligand interaction (PDB: 1eoc).

## 3.1.3 Depicting Shape and Color Atom Overlaps

A program that depicts the shape and the color overlap between a 3D reference structure and a sets of pre-aligned 3D fit molecules. It is implemented to visualize the output of ROCS but can be used to visualize the shape and color similarities of any molecules that have been pre-aligned with other applications.

Note: OEShape TK license is not required to run this example.

![](_page_47_Figure_1.jpeg)

Fig. 3: Example of depicting the receptor-ligand interactions (PDB: 1br6)

#### **Command Line Interface**

A description of the command line interface can be obtained by executing the program with the -help argument.

```
prompt> python shapeoverlap2pdf.py --help
```

will generate the following output:

```
[-in] <input> [-out] <output pdf>
Simple parameter list
    input/output options:
      -in : Input molecule filename
      -out : Output image filename
    general options:
      -maxhits : Maximum number of hits depicted
```

![](_page_48_Figure_1.jpeg)

Fig. 4: Example of depicting the receptor-ligand interactions (PDB: 1eoc)

#### **Code**

| #!/usr/bin/env python                                                                     |
|-------------------------------------------------------------------------------------------|
| # (C) 2022 Cadence Design Systems, Inc. (Cadence)                                         |
| # All rights reserved.                                                                    |
| # TERMS FOR USE OF SAMPLE CODE The software below ("Sample Code") is                      |
| # provided to current licensees or subscribers of Cadence products or                     |
| # SaaS offerings (each a "Customer").                                                     |
| # Customer is hereby permitted to use, copy, and modify the Sample Code,                  |
| # subject to these terms. Cadence claims no rights to Customer's                          |
| # modifications. Modification of Sample Code is at Customer's sole and                    |
| # exclusive risk. Sample Code may require Customer to have a then                         |
| # current license or subscription to the applicable Cadence offering.                     |
| # THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,                      |
| # EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT                    |
| # NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A                            |
| # PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be                    |
| # liable for any damages or liability in connection with the Sample Code<br># or its use. |
| ############################################################                              |
| # Depicts shape and color overlap between a 3D reference structure and                    |
| # a sets of 3D fit molecules. The molecules have to be pre-aligned.                       |
| # The first molecule is expected to be the reference.                                     |
| ############################################################                              |

```
import sys
from openeye import oechem
from openeye import oedepict
from openeye import oegrapheme
from openeye import oeshape
def main(argv=[_name_]):
   itf = oechem. OEInterface(InterfaceData)
    if not oechem. OEParseCommandLine(itf, argv):
        return 1
   iname = itf.GetString("-in")oname = itf.GetString("-out")
   maxhits = \text{iff}. \text{GetInt}("-maxhits")ext = oechem.OEGetFileExtension(oname)
    if not oedepict. OEIsReqisteredMultiPaqeImaqeFile(ext):
        oechem. OEThrow. Fatal ("Unknown multipage image type!")
    if s = oechem. oemolistream()if not ifs.open(iname):
        oechem. OEThrow. Fatal ("Cannot open input molecule file!")
   refmol = occhem.OEGraphMol()if not oechem. OEReadMolecule(ifs, refmol):
        oechem. OEThrow. Fatal ("Cannot read reference molecule!")
    ropts = oedepict.OEReportOptions(3, 1)
    ropts.SetHeaderHeight(40.0)
    ropts.SetFooterHeight(20.0)
    report = oedepict.OEReport(ropts)
   cff = oeshape.OEColorForceField()
    cff.Init(oeshape.OEColorFFType_ImplicitMillsDean)
    cffdisplay = oegrapheme.OEColorForceFieldDisplay(cff)
   qopts = GetShapeQueryDisplayOptions()
    sopts = GetShapeOverlapDisplayOptions()
    copts = GetColorOverlapDisplayOptions()
    refdisp = oegrapheme. 0EShapeQueryDisplay(refmol, cff, qopts)dots = occhem.OEDots(100, 10, "shape overlaps")for fitmol in ifs.GetOEGraphMols():
        if maxhits > 0 and dots. GetCounts () >= maxhits:
            break
        dots. Update ()
        maincell = report. NewCell()grid = oedepict.OEImageGrid(maincell, 1, 3)
```

```
(continued from previous page)
```

```
grid.SetCellGap(5.0)
        # TITLE + SCORE GRAPH + QUERY
       cell = grid.GetCell(1, 1)cellw, cellh = cell. GetWidth(), cell. GetHeight()
       font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_
\rightarrowBold, 10,
                               oedepict.OEAlignment_Left, oechem.OEBlack)
       pos = oedefict.OE2DPoint(10.0, 10.0)cell. DrawText (pos, fitmol. GetTitle(), font, cell. GetWidth())
       rframe = oedepict.OEImageFrame(cell, cellw, cellh * 0.35,
                                       oedepict. OE2DPoint (0.0, cellh * 0.10))
       mframe = oedepict. OEImageFrame(cell, cellw, cellh * 0.50,
                                       oedepict.OE2DPoint(0.0, cellh * 0.50))
       RenderScoreRadial(rframe, fitmol)
       oegrapheme.OERenderShapeQuery(mframe, refdisp)
       font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_
\rightarrowBold, 8,
                               oedepict.OEAlignment_Center, oechem.OEGrey)
       pos = oedepict.OE2DPoint(20.0, 10.0)mframe. DrawText (pos, "query", font)
       oedepict.OEDrawCurvedBorder(mframe, oedepict.OELightGreyPen, 10.0)
       odisp = oegrapheme. OEShapeOverlapDisplay(refdisp, fitmol, sopts, copts)
        # SHAPE OVERLAP
       cell = grid.GetCell(1, 2)oegrapheme.OERenderShapeOverlap(cell, odisp)
       RenderScore(cell, fitmol, "ROCS_ShapeTanimoto", "Shape Tanimoto")
       # COLOR OVERLAP
       cell = grid.GetCell(1, 3)oegrapheme.OERenderColorOverlap(cell, odisp)
       RenderScore(cell, fitmol, "ROCS_ColorTanimoto", "Color Tanimoto")
       oedepict.OEDrawCurvedBorder(maincell, oedepict.OELightGreyPen, 10.0)
   dots. Total()
   cffopts = oegrapheme. OEColorForceFieldLegendDisplayOptions(1, 6)for header in report. GetHeaders () :
       oegrapheme. OEDrawColorForceFieldLegend(header, cffdisplay, cffopts)
       oedepict.OEDrawCurvedBorder(header, oedepict.OELightGreyPen, 10.0)
   font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_
\rightarrowDefault, 12,
                           oedepict.OEAlignment_Center, oechem.OEBlack)
   for idx, footer in enumerate (report. GetFooters()):
       oedepict.OEDrawTextToCenter(footer, "-" + str(idx + 1) + "-", font)
   oedepict.OEWriteReport(oname, report)
```

grid.SetMargins(5.0)

```
return 0
def AddCommonDisplayOptions(opts):
   opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
    opts.SetAtomLabelFontScale(1.5)
    pen = oedepict.OEPen(oechem.OEBlack, oechem.OEBlack, oedepict.OEFill_Off, 1.5)
    opts.SetDefaultBondPen(pen)
def GetShapeQueryDisplayOptions():
   qopts = oegrapheme.OEShapeQueryDisplayOptions()
   AddCommonDisplayOptions(qopts)
   arcpen = oedepict.OEPen(oedepict.OELightGreyPen)
   qopts.SetSurfaceArcFxn(oegrapheme.OEDefaultArcFxn(arcpen))
    qopts.SetDepictOrientation(oedepict.OEDepictOrientation_Square)
    return gopts
def GetShapeOverlapDisplayOptions():
    sopts = oegrapheme. OEShapeOverlapDisplayOptions()
   AddCommonDisplayOptions(sopts)
   arcpen = oedepict.OEPen(oechem.OEGrey, oechem.OEGrey, oedepict.OEFill_Off, 1.0,
\leftrightarrow 0x1111)
    sopts.SetQuerySurfaceArcFxn(oegrapheme.OEDefaultArcFxn(arcpen))
    sopts.SetOverlapColor(oechem.OEColor(110, 110, 190))
    return sopts
def GetColorOverlapDisplayOptions():
   copts = oegrapheme.OEColorOverlapDisplayOptions()
   AddCommonDisplayOptions(copts)
   arepen = oedgepicture.OEPen(oechem.OEGrey, oechem.OEGrey, oedgepicture).OEFil1_0ff, 1.0,\leftrightarrow 0x1111)
   copts.SetQuerySurfaceArcFxn(oegrapheme.OEDefaultArcFxn(arcpen))
   return copts
def GetScore(mol, sdtag):
    if oechem. OEHasSDData (mol, sdtag):
        return float (oechem. OEGetSDData (mol, sdtag))
    return 0.0def RenderScoreRadial(image, mol):
    sscore = max(min(GetScore(mol, "ROCS_BhaperTanimoto"), 1.0), 0.00)cscore = max(min(GetScore(mol, "ROCS ColorTanimoto"), 1.0), 0.00)if sscore > 0.0 or cscore > 0.0:
        scores = oechem. OEDoubleVector ([sscore, cscore])
        oegrapheme. OEDrawROCSScores (image, scores)
```

```
(continued from previous page)
```

```
def RenderScore(image, mol, sdtag, label):
    score = GetScore(mol, std)if score == 0.0:
       return
   w, h = \text{image}. \text{GetWidth}(), image. GetHeight ()
   frame = oedepict.OEImageFrame(image, w, h \star 0.10, oedepict.OE2DPoint(0.0, h \star 0.
\leftrightarrow90))
   font = oedepict.OEFont(oedepict.OEFontFamily_Default, oedepict.OEFontStyle_
\rightarrowDefault, 9,
                          oedepict.OEAlignment_Center, oechem.OEBlack)
   oedepict.OEDrawTextToCenter(frame, label + " = " + str(score), font)
#######################################
# INTERFACE
#######################################
InterfaceData = '''
!BRIEF [-in] <input> [-out] <output pdf>
!CATEGORY "input/output options:" 0
  !PARAMETER -in
   !ALIAS -i
   !TYPE string
   !REQUIRED true
   !KEYLESS 1
    !VISIBILITY simple
    !BRIEF Input molecule filename
    !DETAIL
        The first molecule in the file is expected to be the reference
        molecule
  ! END
  !PARAMETER -out
   !ALIAS -0
   !TYPE string
   !REOUIRED true
   !KEYLESS 2
   !VISIBILITY simple
    !BRIEF Output image filename
  ! END
! END
!CATEGORY "general options:" 1
  !PARAMETER -maxhits
   !ALIAS -mhits
   !TYPE int
   !REOUIRED false
    !DEFAULT 0
    !LEGAL RANGE 0 500
```

```
!VISIBILITY simple
    !BRIEF Maximum number of hits depicted
    !DETAIL
            The default of 0 means there is no limit.
  ! END
! END
\tau , \tauif __name__ == "_main_":
    sys.exit(main(sys.argv))
```

See also:

- OEColorForceField class in the OEShape TK
- OEShapeQueryDisplay and OEShapeQueryDisplayOptions classes
- · OERenderShapeQuery function
- OEShapeOverlapDisplay, OEShapeOverlapDisplayOptions, and OEColorOverlapDisplayOptions classes
- · OERenderShapeOverlapfunction
- · OERenderColorOverlap function
- · OEDrawColorForceFieldLegend function
- · OEDrawROCSScores function

#### **Examples**

prompt> python shapeoverlap2pdf.py -in rocs.sdf -out overlaps.pdf

![](_page_53_Figure_14.jpeg)

Table 1: Example of depicting the shape and color atom overlaps (The pages are reduced here for visualization convenience)

# **3.2 Python Cookbook Examples**

There are large number of code examples available in OpenEye Python Cookbook that use OpenEye Toolkits to solve a wide range of cheminformatics and molecular modeling problems.

- 2D Depiction chapter contains examples that illustrate how the **OEDepict TK** and **Grapheme TK** can be utilized to depict molecules and visualize properties calculated with other OpenEye toolkits.
- Visualizing 3D Information chapter contains examples that illustrate how the Grapheme TK can be utilized to project complex 3D information into the 2D molecular graph.
- Cheminformatics chapter contains examples that solve various cheminformatics problems such as similarity search, ring perception and manipulating molecular graphs.

#### **OpenEye Python Cookbook examples using OEGrapheme TK**

- Visualizing Torsional Angle Distribution
- Visualizing Electron Density
- Visualizing Molecular Dipole Moment
- Depicting Peptides
- Depicting Molecular Properties
- Visualizing Shape and Color Overlap

#### Protein-ligand visualization:

- Visualizing Protein-Ligand Interactions
- Visualizing Protein-Ligand Unpaired Interactions
- Visualizing Protein-Ligand B-Factor
- Visualizing Protein-Ligand B-Factor Map
- Visualizing Protein-Ligand Contacts
- Visualizing Protein-Ligand Maps
- Ramachandran Plot

## **FOUR**

# **PRELIMINARY API**

# **4.1 OEDrawlridiumData**

Attention: This API is currently available in C++ and Python.

```
bool OEDrawIridiumData (OEDepict:: OEImageBase &image,
                        const OEBio:: OEDesignUnit &du)
bool OEDrawIridiumData (OEDepict:: OEImageBase &image,
                        const OEBio:: OEIridiumData &iridium)
```

Renders the Iridium data into an easily interpretable graph.

*image* The image on which the Iridium data graph is drawn.

**du** The OEDesignUnit object of which Iridium data is being rendered.

*iridium* The OEIridiumData object that is being rendered.

## **Example:**

The following code snippet shows how to use the *OEDrawIridiumData* function. The image created is shown in Figure: Example of using the OEDrawIridiumData function.

```
du = oechem. OEDesignUnit()
if not oechem. OEReadDesignUnit (filename, du) :
    oechem. OEThrow. Fatal ("Cannot read design unit!")
image = odeplot.OEImage (250, 250)oegrapheme. OEDrawIridiumData (image, du)
oedepict.OEDrawBorder(image, oedepict.OELightGreyPen)
oedepict.OEWriteImage("DrawIridiumData.svg", image)
```

**Note:** When generating . svg image, the output will be interactive. With any other image file format it will be static. See also Generating Interactive SVG Images chapter in OEDepict TK manual.

- Iridium chapter in OESpruce TK manual
- OEDesignUnit class
- OEIridiumData class

![](_page_57_Figure_1.jpeg)

Fig. 1: Example of using the OEDrawIridiumData function

## **FIVE**

**API** 

# **5.1 OEGrapheme Classes**

## 5.1.1 OE2DActiveSiteDisplay

class OE2DActiveSiteDisplay

This class represents OE2DActiveSiteDisplay that stores the depiction information (such as 2D coordinates, representation styles etc.) of an active site.

An active site display can be rendered into an image using the OEPrepareActiveSiteDepiction and OERenderActiveSite functions.

#### **Code Example**

- Depicting Active Site Interactions example
- Visualizing Protein-Ligand Interactions OpenEye Python Cookbook recipe

## **Constructors**

OE2DActiveSiteDisplay(const OEBio::OEInteractionHintContainer &asite, const OE2DActiveSiteDisplayOptions &opts)

Initializes an OE2DActiveSiteDisplay object using the given display options.

**asite** The active site for which display information is stored in the OE2DActiveSiteDisplay object.

opts The OE2DActiveSiteDisplayOptions object that stores properties that determine the styles of the active site depiction.

#### **Warning:**

• An *OE2DActiveSiteDisplay* object does not make a copy of the *OEInteractionHintContainer* object from which it is initialized but only stores its pointer. Therefore, the user responsibility is to not let the interaction container object go out of scope, before the corresponding OE2DActiveSiteDisplay object.

#### See also:

· OEIsValidActiveSite function

· OE2DActiveSiteDisplay. IsValid method

#### GetDisplayedLigand

const OEChem:: OEMolBase \*GetDisplayedLigand() const

Returns a pointer to the display ligand of the active site.

#### **GetDisplayedResidues**

```
OESystem::OEIterBase<OEChem::OEResidue> *
  GetDisplayedResidues(unsigned int renderstyle=OEActiveSiteRenderStyle::Default)
\rightarrow const
```

Returns an iterator over the displayed residues of the given style.

renderstyle This value has to be from the OEActiveSiteRenderStyle namespace.

#### **GetHeight**

double GetHeight () const

Returns the height of the displayed active site.

#### **GetOptions**

const OE2DActiveSiteDisplayOptions &GetOptions () const

Returns the options used to initialized the OE2DActiveSiteDisplay object.

#### **GetWidth**

double GetWidth() const

#### **IsValid**

bool IsValid() const

Returns whether the OE2DActiveSiteDisplay object was initialized successfully.

**Hint:** It is highly recommend to check whether an active site display is valid after initialization.

## 5.1.2 OE2DActiveSiteDisplayOptions

class OE2DActiveSiteDisplayOptions: public OEDepict::OE2DMolDisplayOptions

This class represents the OE2DActiveSiteDisplayOptions class that encapsulates properties that determine how an active site is depicted.

The following methods are publicly inherited from OE2DMolDisplayOptions:

| operator=                    | GetDefaultBondPen         | SetBondColorStyle            |
|------------------------------|---------------------------|------------------------------|
| GetAromaticStyle             | GetHeight                 | SetBondLineAtomLabelGapScale |
| GetAtomColor                 | GetHydrogenStyle          | SetBondLineGapScale          |
| GetAtomColorStyle            | GetScale                  | SetBondPropLabelFont         |
| GetAtomLabelFont             | GetSuperAtomLabelFont     | SetBondPropLabelFontScale    |
| GetAtomLabelFontScale        | GetSuperAtomStyle         | SetBondPropertyFunctor       |
| GetAtomPropLabelFont         | GetTitleFont              | SetBondStereoStyle           |
| GetAtomPropLabelFontScale    | GetTitleLocation          | SetBondWidthScaling          |
| GetAtomPropertyFunctor       | GetWidth                  | SetDefaultBondPen            |
| GetAtomStereoStyle           | SetAromaticStyle          | SetDimensions                |
| GetBackgroundColor           | SetAtomColor              | SetHeight                    |
| GetBondColorStyle            | SetAtomColorStyle         | SetHydrogenStyle             |
| GetBondLineAtomLabelGapScale | SetAtomLabelFont          | SetScale                     |
| GetBondLineGapScale          | SetAtomLabelFontScale     | SetSuperAtomLabelFont        |
| GetBondPropLabelFont         | SetAtomPropLabelFont      | SetSuperAtomStyle            |
| GetBondPropLabelFontScale    | SetAtomPropLabelFontScale | SetTitleFont                 |
| GetBondPropertyFunctor       | SetAtomPropertyFunctor    | SetTitleLocation             |
| GetBondStereoStyle           | SetAtomStereoStyle        | SetWidth                     |
| GetBondWidthScaling          | SetBackgroundColor        |                              |

#### **Code Example**

- Depicting Active Site Interactions example
- Visualizing Protein-Ligand Interactions OpenEye Python Cookbook recipe

#### **Constructors**

OE2DActiveSiteDisplayOptions(double width, double height)

Creates an OE2DActiveSiteDisplayOptions object with the specified dimension.

width, height The width and height of the active site display. Both numbers have to be at least 200.0.

OE2DActiveSiteDisplayOptions(const OE2DActiveSiteDisplayOptions & rhs)

Copy constructor.

#### operator=

OE2DActiveSiteDisplayOptions &operator=(const OE2DActiveSiteDisplayOptions &rhs)

Assignment operator.

#### GetRenderInteractiveLegend

bool GetRenderInteractiveLegend() const

Returns whether and interactive legend is rendered only when mouse is hovered over the "Legend" button depicted on the right top corner on the active site depiction.

See also:

· OE2DActiveSiteDisplayOptions. SetRenderInteractiveLegend method

#### **GetResidueSVGMarkupFunctor**

const OEResidueSVGMarkupBase &GetResidueSVGMarkupFunctor() const

Returns the functor that defines how the residues are marked in svq image. By default, residues are not marked (OEResidueSVGNoMarkup).

#### See also:

· OE2DActiveSiteDisplayOptions. SetResidueSVGMarkupFunctor method

#### GetSVGMagnifyResidueInHover

double GetSVGMagnifyResidueInHover() const

Returns the scaling factor that is used to magnify residue glyphs when mouse is hover over them.

#### See also:

· OE2DActiveSiteDisplayOptions.SetSVGMagnifyResidueInHover method

#### **SetBackgroundColor**

void SetBackgroundColor (const OESystem:: OEColor &)

This is a no-op method. The background of the active site display is always OEWhite

#### **SetDimensions**

void SetDimensions (double width, double height, double scale)

This is a no-op method. The dimension of the active site display only be specified with the OE2DActiveSiteDisplayOptions constructor.

#### **SetHeight**

void SetHeight (double)

This is a no-op method. The height of the active site display can only be specified with the OE2DActiveSiteDisplayOptions constructor.

#### SetRenderInteractiveLegend

void SetRenderInteractiveLegend (bool render)

Sets whether and interactive legend is rendered only when mouse is hovered over the "Legend" button depicted on the right top corner on the active site depiction.

**Note:** This functionality is **only available** for  $. s \vee q$  image format. In other image formats it has no effect.

#### **SetResidueSVGMarkupFunctor**

void SetResidueSVGMarkupFunctor (const OEResidueSVGMarkupBase & func)

Sets the functor that defines how the residues are marked in svq image. Drawing elements representing residues in syq image are grouped together in the following format in which the  $\langle \text{qrow } \text{ id} \rangle$  and  $\langle \text{class } \text{name} \rangle$  strings are defined by the given functor:

```
<q id='<qroup id>' class='<class name>'>
list of drawing elements
\ddot{\phantom{a}}< / q>
```

Note: This setting has only effect when generating . svq images.

**Example:** 

```
asite = oechem. OEInteractionHintContainer (protein, ligand)
oechem. OEPerceiveInteractionHints (asite)
oegrapheme.OEPrepareActiveSiteDepiction(asite)
opts = oegrapheme. OE2DActiveSiteDisplayOptions (800.0, 600.0)
opts.SetResidueSVGMarkupFunctor(oegrapheme.OEResidueSVGStandardMarkup())
adisp = oegrapheme. OE2DActiveSiteDisplay(asite, opts)
```

oegrapheme. OERenderActiveSite ("SVGMarkResidues.svg", adisp)

#### See also:

- OEResidueSVGMarkupBase abstract base class
- OEResidueSVGNoMarkup class
- OEResidueSVGStandardMarkup class
- · OE2DActiveSiteDisplayOptions.GetResidueSVGMarkupFunctor method

#### SetSVGMagnifyResidueInHover

void SetSVGMagnifyResidueInHover (double scale)

Sets the scaling factor that is used to magnify residue glyphs when mouse is hover over them.

scale This value has to be in a range of  $[1.00, 3.00]$ . The default value is 1.00 which has has no effect.

**Hint:** This is a very useful feature when generating an active site image with residue labels that are too small to read.

**Note:** This functionality is **only available** for . svg image format. In other image formats it has no effect.

#### **SetScale**

void SetScale (double)

This is a no-op method. The active site display can not be scaled.

#### **SetSuperAtomStyle**

```
void SetSuperAtomStyle (unsigned int)
```

This is a no-op method. The super atom style can not be used when depicting an active site.

#### **SetWidth**

```
void SetWidth (double)
```

This is a no-op method. The width of the active site display can only be specified with the OE2DActiveSiteDisplayOptions constructor.

## 5.1.3 OE2DActiveSiteLegendDisplayOptions

#### class OE2DActiveSiteLegendDisplayOptions

This class represents OE2DActiveSiteLegendDisplayOptions that encapsulates properties that determine how the legend of a color force field is depicted by the OEDrawActiveSiteLegend function.

#### See also:

- · OE2DActiveSiteDisplay class
- · OEDrawActiveSiteLegend function

#### **Code Example**

- Depicting Active Site Interactions example
- Visualizing Protein-Ligand Interactions OpenEye Python Cookbook recipe

#### **Constructors**

OE2DActiveSiteLegendDisplayOptions (unsigned int rows, unsigned int cols)

Creates an OE2DActiveSiteLegendDisplayOptions object with the specified number of rows and columns..

rows The number of rows in the legend.

cols The number of columns in the legend.

OE2DActiveSiteLegendDisplayOptions(const OE2DActiveSiteLegendDisplayOptions &rhs)

Copy constructor.

#### operator=

```
OE2DActiveSiteLegendDisplayOptions &
 operator=(const OE2DActiveSiteLegendDisplayOptions &rhs)
```

Assignment operator.

#### **NumCols**

unsigned int NumCols() const

Returns the number of columns of the legend.

#### **NumRows**

unsigned int NumRows () const

## 5.1.4 OE2DPropMap

class OE2DPropMap

The OE2DPropMap class maps atom properties into a 2D grid and then blurs the image by using a Gaussian function. The points of the 2D grid are then colored using the OELinearColorGradient class that interpolates colors between a specified range.

#### See also:

• Depicting Property Maps chapter

#### **Code Example**

• Visualizing Molecular Dipole Moment OpenEye Python Cookbook recipe

The OE2DPropMap class can be customized with the following properties:

| Property          | Get method         | Set method         | Corresponding<br>namespace/class |
|-------------------|--------------------|--------------------|----------------------------------|
| legend font       | GetLegendFont      | SetLegendFont      | <b>OEFont</b>                    |
| legend font scale | GetLegendFontScale | SetLegendFontScale |                                  |
| legend location   | GetLegendLocation  | SetLegendLocation  | <b>OELegendLocation</b>          |
| maximum value     | GetMaxValue        | SetMaxValue        |                                  |
| minimum value     | GetMinValue        | SetMinValue        |                                  |
| negative color    | GetNegativeColor   | SetNegativeColor   | <b>OEColor</b>                   |
| positive color    | GetPositiveColor   | SetPositiveColor   | <b>OEColor</b>                   |
| radius ratio      | GetRadiusRatio     | SetRadiusRatio     |                                  |
| grid resolution   | GetResolution      | SetResolution      |                                  |

#### **Constructors**

OE2DPropMap(const OESystem::OEColor &bqColor=OESystem::OEColor(250, 250, 250))

#### Default constructor.

OE2DPropMap(const OE2DPropMap & rhs)

Copy constructor.

#### operator=

OE2DPropMap & operator= (const OE2DPropMap &)

Assignment operator.

#### **Render**

bool Render (OEDepict:: OE2DMolDisplay &disp, const std:: string &tagname)

Renders the property map into a molecule display.

disp The molecule display that holds the molecule for which the property map is calculated and on which the property map is drawn. The property map is drawn onto the *below* layer of the molecule display *i.e.*, it appears underneath the molecular diagram.

*tagname* The generic data identifier that is used to retrieve the properties being depicted on the property map.

```
bool Render (OEDepict:: OEImageBase &image, const OEDepict:: OE2DMolDisplay &disp,
            const std:: string & tagname)
```

Renders the property map into an image.

*image* The image on which the property map is drawn.

*disp* The molecule display that holds the molecule for which the property map is calculated.

*tagname* The generic data identifier that is used to retrieve the properties being depicted on the property map.

```
bool Render (OEDepict:: OE2DMolDisplay &disp,
            const OEDepict:: OE2DMolDisplay & refdisp, const std:: string & tagname)
```

Renders the property map calculated for one display, onto another display.

disp The molecule display on which the property map is drawn. The property map is drawn onto the below layer of the molecule display *i.e.*, it appears underneath the molecular diagram.

*refdisp* The molecule display that holds the molecule for which the property map is calculated.

*tagname* The generic data identifier that used to retrieve the properties being depicted on the property map.

#### **GetLegendFont**

const OEDepict:: OEFont& GetLegendFont () const

Returns the font that is used to render the title of the legend and the color stops of the linear color gradient.

- · OE2DPropMap. SetLegendFont method
- OEFont class

#### **GetLegendFontScale**

double GetLegendFontScale() const

Returns the multiplier that can be used to increase or decrease the size of the legend fonts.

#### See also:

· OE2DPropMap. SetLegendFontScale method

#### GetLegendLocation

unsigned int GetLegendLocation() const

Returns the position of the legend. The return value is taken from the OELegendLocation namespace.

#### See also:

- · OE2DPropMap. SetLegendLocation method
- · OELegendLocation namespace

#### **GetMaxValue**

double GetMaxValue() const

Returns the maximum value that is used to construct the color gradient of the property map.

#### See also:

· OE2DPropMap. SetMaxValue method

#### **GetMinValue**

double GetMinValue() const

Returns the minimum value that is used to construct the color gradient of the property map.

#### See also:

· OE2DPropMap. SetMinValue method

#### **GetNegativeColor**

const OESystem:: OEColor &GetNegativeColor() const

Returns the color that is used to represent negative atom property values.

- · OE2DPropMap.SetNegativeColor method
- OEColor class

#### **GetPositiveColor**

const OESystem:: OEColor &GetPositiveColor() const

Returns the color that is used to represent positive atom property values.

#### See also:

- · OE2DPropMap. SetPositiveColor method
- OEColor class

#### **GetRadiusRatio**

double GetRadiusRatio() const

Returns he ratio that is used to scale the Gaussian radius.

#### See also:

· OE2DPropMap. SetRadiusRatio method

#### **GetResolution**

unsigned int GetResolution () const

Returns the resolution of the property grid.

#### See also:

· OE2DPropMap. SetResolution method

#### **SetLegendFont**

void SetLegendFont (const OEDepict:: OEFont &font)

Sets the font that is used to render the title of the legend and the color stops of the linear color gradient.

Note: The size of fonts of the legend also depends on the scaling factor used to fit the linear color gradient into the given dimensions and the multiplier set by the  $OE2DP$ ropMap. Set LegendFont Scale method.

Example (see Figure: Example of using the SetLegendFont method)

```
propmap = oeqrapheme.OE2DPropMap()font = <code>oederict.OEFont()</code>font.SetStyle(oedepict.OEFontStyle_Bold)
font.SetColor(oechem.OEDarkBlue)
propmap.SetLegendFont(font)
```

- · OE2DPropMap.GetLegendFont method
- OEFont class

![](_page_69_Figure_1.jpeg)

Fig. 1: Example of using the SetLegendFont method

## **SetLegendFontScale**

void SetLegendFontScale(double scale)

Sets the multiplier that can be used to increase or decrease the size of the legend fonts.

scale This value has to be in the range of  $[0.5, 2.0]$ .

Example (see Figure: Example of using the SetLegendFontScale method)

```
propmap = oegrapheme. OE2DPropMap()
propmap.SetLegendFontScale(1.5)
```

#### See also:

· OE2DPropMap.GetLegendFontScale method

#### **SetLegendLocation**

void SetLegendLocation (unsigned int loc)

Sets the position of the legend.

loc This value has to be from the OELegendLocation namespace.

Example (see Figure: Example of using the SetLegendLocation method)

```
propmap = oegrapheme. OE2DPropMap()
propmap.SetLegendLocation(oegrapheme.OELegendLocation_Left)
```

![](_page_70_Figure_1.jpeg)

Fig. 2: Example of using the SetLegendFontScale method

![](_page_70_Figure_3.jpeg)

Fig. 3: Example of using the SetLegendLocation method

- · OE2DPropMap.GetLegendLocation method
- · OELegendLocation namespace

#### **SetMaxValue**

```
void SetMaxValue (double maxv)
```

Sets the maximum value that is used to construct the color gradient of the property map. If no maximum value is specified prior to calling the  $OE2DPYopMap$ . Render method, then the maximum value will be the largest atom property value.

**Example (see Figure: Example of using the SetMaxValue method)** 

```
propmap = oegrapheme. OE2DPropMap()
propmap.SetMaxValue(0.0)
```

![](_page_71_Figure_6.jpeg)

Fig. 4: Example of using the SetMaxValue method

#### See also:

· OE2DPropMap.GetMaxValue method

#### **SetMinValue**

void SetMinValue (double minv)

Sets the minimum value that is used to construct the color gradient of the property map. If no minimum value is specified prior to calling the  $OE2DPropMap$ . Render method, then the minimum value will be the smallest atom property value.

Example (see Figure: Example of using the SetMinValue method)

```
propmap = oegrapheme. OE2DPropMap()
propmap.SetMinValue(0.0)
```

![](_page_72_Figure_1.jpeg)

#### Fig. 5: Example of using the SetMinValue method

· OE2DPropMap.GetMinValue method

#### **SetNegativeColor**

```
void SetNegativeColor (const OESystem:: OEColor &color)
```

Sets the color that is used to represent negative atom property values.

Example (see Figure: Example of using the SetNegativeColor method)

```
propmap = oeqrapheme.OE2DPropMap()propmap.SetNegativeColor(oechem.OEDarkGreen)
```

#### See also:

- · OE2DPropMap.GetNegativeColor method
- OEColor class

## **SetPositiveColor**

void SetPositiveColor(const OESystem::OEColor &color)

Sets the color that is used to represent positive atom property values.

Example (see Figure: Example of using the SetPositiveColor method)

```
propmap = oegrapheme. OE2DPropMap()
propmap.SetPositiveColor(oechem.OEDarkGreen)
```

![](_page_73_Figure_1.jpeg)

Fig. 6: Example of using the SetNegativeColor method

![](_page_73_Figure_3.jpeg)

Fig. 7: Example of using the SetPositiveColor method

- · OE2DPropMap.GetPositiveColor method
- OEColor class

#### **SetRadiusRatio**

void SetRadiusRatio (double ratio)

Sets the ratio that is used to scale the Gaussian radius.

*ratio* This value has to be in the range of  $[0.5, 2.0]$ .

Example (see Figure: Example of using the SetRadiusRatio method)

 $propmap = oeqrapheme.OE2DPropMap()$ propmap.SetRadiusRatio(0.75)

![](_page_74_Figure_7.jpeg)

Fig. 8: Example of using the SetRadiusRatio method

#### See also:

· OE2DPropMap.GetRadiusRatiomethod

#### **SetResolution**

void SetResolution (unsigned int resolution)

Sets the resolution of the property grid.

*resolution* This value has to be in the range of  $[2, 20]$ .

Example (see Figure: Example of using the SetResolution method)

```
propmap = oegrapheme. OE2DPropMap()
propmap.SetResolution(5)
```

#### See also:

· OE2DPropMap.GetResolution method.

![](_page_75_Figure_1.jpeg)

#### Fig. 9: Example of using the SetResolution method

## 5.1.5 OEAlignedDepictionFrom3DOptions

#### class OEAlignedDepictionFrom3DOptions

This class represents OEAlignedDepictionFrom3DOptions that stores parameters that are used when generating 2D coordinates by calling the OEP repareAlignedDepictionFrom3D function.

| Property                     | Get method                  | Set method                  |
|------------------------------|-----------------------------|-----------------------------|
| clear coords                 | <i>GetClearCoords</i>       | <i>SetClearCoords</i>       |
| max number of bond rotations | <i>GetMaxBondRotations</i>  | <i>SetMaxBondRotations</i>  |
| suppressing hydrogens        | <i>GetSuppressHydrogens</i> | <i>SetSuppressHydrogens</i> |

#### **Constructors**

OEAlignedDepictionFrom3DOptions (bool clearCoords=true, bool suppressH=true)

Default constructor that initializes an OEAlignedDepictionFrom3DOptions object with the following properties:

#### Table 1: Default parameters of the OEAlignedDepiction-**From3DOptions class**

| Property                     | Default value    |
|------------------------------|------------------|
| clear coordinates            | true             |
| max number of bond rotations | $2^{16} = 65536$ |
| suppressing hydrogens        | true             |

OEAlignedDepictionFrom3DOptions (const OEAlignedDepictionFrom3DOptions & rhs)

Copy constructor.

#### operator=

```
OEAlignedDepictionFrom3DOptions &
  operator=(const OEAlignedDepictionFrom3DOptions & rhs)
```

Assignment operator.

#### **GetClearCoords**

bool GetClearCoords () const

#### See also:

· OEAlignedDepictionFrom3DOptions. SetClearCoords method

#### **GetMaxBondRotations**

unsigned int GetMaxBondRotations() const

#### See also:

· OEAlignedDepictionFrom3DOptions.SetSuppressHydrogens method

#### GetSuppressHydrogens

bool GetSuppressHydrogens() const

Returns whether the explicit hydrogens are suppressed in the molecule prior to generating the 2D coordinates.

#### See also:

· OEAlignedDepictionFrom3DOptions.SetSuppressHydrogens method

#### **SetClearCoords**

void SetClearCoords (bool clearcoords)

If false and the fit molecule has 2D coordinates, then these coordinates are used for the alignment. Otherwise the 2D coordinates of the fitted molecule are generated by calling the OEP repareDepictionFrom3D function.

#### See also:

· OEAlignedDepictionFrom3DOptions.GetClearCoords method

#### **SetMaxBondRotations**

void SetMaxBondRotations (unsigned int maxrotations)

Sets the maximum number of bond rotations performed during the 2D coordinate generation process.

maxrotations

The zero value means that there is no limit. Upon reaching this limit, the process terminates and returns the "best" aligned 2D coordinates.

**Hint:** The default value for maximum number of bond rotations is  $2^{16} = 65536$ . This means that by default only the first 16 single bonds of the molecule will be rotated to find the "best" aligned 2D layout.

It is recommended to use this parameter if the input 3D molecule has a large number of rotatable bonds.

#### See also:

· OEAlignedDepictionFrom3DOptions.GetMaxBondRotations method

#### SetSuppressHydrogens

void SetSuppressHydrogens (bool)

Sets whether the explicit hydrogens are suppressed in the molecule prior to generating the 2D coordinates. Only hydrogens that are necessary to faithfully represent tetrahedral stereochemistry will be kept.

#### See also:

· OEAlignedDepictionFrom3DOptions.GetSuppressHydrogens method

## 5.1.6 OEAtomGlyphBase

#### class OEAtomGlyphBase

OEAtomGlyphBase is an abstract class that defines the interface used for atom annotation.

#### See also:

- Annotating Atoms and Bonds chapter
- OEAddGlyph function.

The following classes derive from this class:

• OEAtomGlyphCircle

#### **Constructors**

OEAtomGlyphBase()

Default constructor.

#### **CreateCopy**

**virtual** OEAtomGlyphBase \*CreateCopy() const =  $0$ 

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

#### **RenderGlyph**

```
bool RenderGlyph (OEDepict::OE2DMolDisplay &disp, const OEChem::OEAtomBase *atom)
\rightarrowconst = 0
```

It is a virtual const method that is implemented in the concrete derived classes to annotate the given atom (i.e. to draw a glyph to mark the atom).

disp The OE2DMolDisplay object that is modified to annotate the specified atom.

atom The OEAtomBase object being annotated.

## 5.1.7 OEAtomGlyphCircle

class OEAtomGlyphCircle : public OEAtomGlyphBase

By using the OEAtomGlyphCircle class, atoms can be annotated by drawing a circle around them.

#### See also:

- Annotating Atoms and Bonds chapter
- · OECircleStyle namespace

The following methods are publicly inherited from OEAtomGlyphBase:

CreateCopy RenderGlyph

#### **Constructors**

```
OEAtomGlyphCircle(const OEDepict:: OEPen &pen,
                  unsigned int circlestyle=OECircleStyle::Default,
                  double circleRadiusScale=1.0,
                  unsigned int layer=OEDepict:: OELayerPosition:: Below)
```

Creates an OEAtomGlyphCircle object with the specified parameters

**pen** The pen used when drawing a circle around an atom.

See example (A) and (B) in Figure: Example of atom annotations.

![](_page_79_Figure_1.jpeg)

Fig. 10: Example of atom annotations

*circlestyle* The style of the drawn circle from the  $OECircleStvle$  namespace.

See examples (C) and (D) in Figure: Example of atom annotations.

circleRadiusScale The multiplier used to modify the radius of the drawn circles

See examples (D) and (E) in Figure: Example of atom annotations.

*layer* Specifies whether the circle is drawn above (OELayerPosition\_Above) below <sub>or</sub> (OELayerPosition Below) the molecule.

See examples (B) and (F) in Figure: Example of atom annotations.

#### **CreateCopy**

OEAtomGlyphBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEAtomGlyphCircle object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

bool RenderGlyph (OEDepict:: OE2DMolDisplay &disp, const OEChem:: OEAtomBase \*atom) const

Draws a glyph (in this case a circle) around the given atom.

disp The OE2DMolDisplay object that is modified to annotate the specified atom.

atom The OEAtomBase object being annotated.

## 5.1.8 OEBondGlyphArrow

```
class OEBondGlyphArrow : public OEBondGlyphBase
```

By using the OEBondGlyphArrow class, bonds can be annotated by drawing an arrow across them.

- Annotating Atoms and Bonds chapter
- OEBondGlyphCircle class
- OEBondGlyphCross class
- OEBondGlyphCurvedArrow class

- OEBondGlyphScissors class
- OEBondGlyphStitch class
- OEBondGlyphZigZag class

The following methods are publicly inherited from OEBondGlyphBase:

CreateCopy RenderGlyph

#### **Constructors**

```
OEBondGlyphArrow(const OEDepict::OEPen &, double arrowLengthScale=1.0,
                 unsigned int layer=OEDepict:: OELayerPosition:: Above)
```

Creates an OEBondGlyphArrow object with the specified parameters.

![](_page_80_Figure_9.jpeg)

Fig. 11: Example of bond annotations

**pen** The pen used when drawing an arrow across the middle of the bond.

See examples (A) and (B) in Figure: Example of bond annotations.

arrowLengthScale The multiplier used to modify the length of the drawn arrows.

See examples (A) and (C) in Figure: Example of bond annotations.

layer Specifies whether the arrow is drawn above (OELayerPosition Above) below or (OELayerPosition\_Below) the molecule.

See examples (B) and (D) in *Figure: Example of bond annotations*.

#### **CreateCopy**

OEBondGlyphBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondGlyphArrow object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

bool RenderGlyph (OEDepict:: OE2DMolDisplay &disp, const OEChem:: OEBondBase \*bond) const

Draws a glyph (in this case a straight arrow) in the middle of the given bond.

disp The OE2DMolDisplay object that is modified to annotate the specified bond.

**bond** The OEBondBase object being annotated.

## 5.1.9 OEBondGlyphBase

#### class OEBondGlyphBase

OEBondGlyphBase is an abstract class that defines the interface used for bond annotation.

#### See also:

- Annotating Atoms and Bonds chapter
- OEAddGlyph function.

The following classes derive from this class:

- OEBondGlyphArrow
- OEBondGlyphCircle
- OEBondGlyphCross class
- OEBondGlyphCurvedArrow class
- OEBondGlyphScissors class
- OEBondGlyphStitch class
- OEBondGlyphZigZag class

#### **Constructors**

OEBondGlyphBase()

Default constructor.

#### **CreateCopy**

```
virtual OEBondGlyphBase *CreateCopy() const = 0
```

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

#### **RenderGlyph**

**bool** RenderGlyph (OEDepict::OE2DMolDisplay &, const OEChem::OEBondBase \*) const =0

It is a virtual const method that is implemented in the concrete derived classes to annotate the given bond (*i.e.* to draw a glyph to mark the bond).

disp The OE2DMolDisplay object that is modified to annotate the specified bond.

atom The OEBondBase object being annotated.

## 5.1.10 OEBondGlyphCircle

class OEBondGlyphCircle : public OEBondGlyphBase

By using the OEBondGlyphCircle class, bonds can be annotated by drawing a circle in the middle of them.

#### See also:

- Annotating Atoms and Bonds chapter
- · OECircleStyle namespace
- OEBondGlyphArrow class
- OEBondGlyphCross class
- OEBondGlyphCurvedArrow class
- OEBondGlyphScissors class
- OEBondGlyphStitch class
- OEBondGlyphZigZag class

The following methods are publicly inherited from OEBondGlyphBase:

CreateCopy RenderGlyph

#### **Constructors**

```
OEBondGlyphCircle(const OEDepict:: OEPen &,
                  unsigned int circlestyle=OECircleStyle::Default,
                  double circleRadiusScale=1.0,
                  unsigned int layer=OEDepict:: OELayerPosition:: Above)
```

Creates an OEBondGlyphCircle object with the specified parameters.

**pen** The pen used when drawing a circle in the middle of a bond.

See examples (A) and (B) in *Figure: Example of bond annotations*.

*circlestyle* The style of the drawn circle from the  $OECircleStyl$ e namespace.

See examples (C) and (D) in Figure: Example of bond annotations.

#### circleRadiusScale The multiplier used to modify the radius of the drawn circles.

See examples (D) and (E) in Figure: Example of bond annotations.

![](_page_83_Figure_1.jpeg)

![](_page_83_Figure_2.jpeg)

laver Specifies whether the circle  $is$ (OELayerPosition Above) below drawn above  $\alpha$ (OELayerPosition\_Below) the molecule.

See examples (B) and (F) in Figure: Example of bond annotations.

#### **CreateCopy**

OEBondGlyphBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondGlyphCircle object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

bool RenderGlyph (OEDepict:: OE2DMolDisplay &disp, const OEChem:: OEBondBase \*bond) const

Draws a glyph (in this case a circle) in the middle of the given bond.

disp The OE2DMolDisplay object that is modified to annotate the specified bond.

**bond** The OEBondBase object being annotated.

## 5.1.11 OEBondGlyphCross

class OEBondGlyphCross : public OEBondGlyphBase

By using the OEBondGlyphCross class, bonds can be annotated by drawing a cross in the middle of them.

- Annotating Atoms and Bonds chapter
- · OECircleStyle namespace
- OEBondGlyphArrow class
- OEBondGlyphCircle class
- OEBondGlyphCurvedArrow class
- OEBondGlyphScissors class
- OEBondGlyphStitch class
- OEBondGlyphZigZag class

The following methods are publicly inherited from OEBondGlyphBase:

RenderGlyph CreateCopy

#### **Constructors**

```
OEBondGlyphCross(const OEDepict:: OEPen &pen, double crossLengthScale=1.0,
                 unsigned int layer=OEDepict:: OELayerPosition:: Above)
```

Creates an OEBondGlyphCross object with the specified parameters.

![](_page_84_Figure_6.jpeg)

#### Fig. 13: Example of bond annotations

**pen** The pen used when drawing a cross across the middle of the bond.

See examples (A) and (B) in Figure: Example of bond annotations.

crossLengthScale The multiplier used to modify the length of the drawn cross.

See examples (A) and (C) in Figure: Example of bond annotations.

layer Specifies whether the cross drawn above (OELayerPosition Above) below <sub>or</sub> (OELayerPosition\_Below) the molecule.

See examples (B) and (D) in Figure: Example of bond annotations.

#### **CreateCopy**

OEBondGlyphBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondGlyphCross object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

```
bool RenderGlyph (OEDepict::OE2DMolDisplay &disp, const OEChem::OEBondBase *bond)
\rightarrowconst
```

Draws a glyph (in this case a cross) in the middle of the given bond.

disp The OE2DMolDisplay object that is modified to annotate the specified bond.

**bond** The OEBondBase object being annotated.

## 5.1.12 OEBondGlyphCurvedArrow

```
class OEBondGlyphCurvedArrow : public OEBondGlyphBase
```

By using the OEBondGlyphCurvedArrow class, bonds can be annotated by drawing a curved arrow across them.

#### See also:

- Annotating Atoms and Bonds chapter
- OEBondGlyphArrow class
- OEBondGlyphCircle class
- OEBondGlyphCross class
- OEBondGlyphScissors class
- OEBondGlyphStitch class
- OEBondGlyphZigZag class

The following methods are publicly inherited from OEBondGlyphBase:

CreateCopy RenderGlyph

#### **Constructors**

```
OEBondGlyphCurvedArrow(const OEDepict::OEPen &pen, double arrowRadiusScale=1.0,
                       bool clockwise=true, double arcAngle=270.0,
                       unsigned int layer=OEDepict:: OELayerPosition:: Above)
```

Creates an OEBondGlyphCurvedArrow object with the specified parameters.

![](_page_85_Figure_22.jpeg)

Fig. 14: Example of bond annotations

**pen** The pen used when drawing a curved arrow at the middle of the bond.

See examples (A) and (B) in *Figure: Example of bond annotations*.

arrowRadiusScale The multiplier used to modify the radius of the drawn arc.

See examples (A) and (C) in Figure: Example of bond annotations.

*clockwise* The direction of the arrow.

See examples (A) and (D) in Figure: Example of bond annotations.

**arcAngle** The angel of the arc in degrees. The value has to be in a range of  $[0.0^{\circ}, 360.0^{\circ}]$ .

See examples (A) and (E) in *Figure: Example of bond annotations*.

layer Specifies whether the curved arrow is drawn above (OELayerPosition\_Above) or below (OELayerPosition\_Below) the molecule.

See examples (B) and (F) in Figure: Example of bond annotations.

#### **CreateCopy**

OEBondGlyphBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondGlyphCurvedArrow object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

bool RenderGlyph (OEDepict:: OE2DMolDisplay &disp, const OEChem:: OEBondBase \*bond) const

Draws a glyph (in this case a curved arrow) in the middle of the given bond.

**disp** The OE2DMolDisplay object that is modified to annotate the specified bond.

**bond** The OEBondBase object being annotated.

## 5.1.13 OEBondGlyphScissors

class OEBondGlyphScissors : public OEBondGlyphBase

By using the OEBondGlyphCross class, bonds can be annotated by drawing a cross in the middle of them.

- Annotating Atoms and Bonds chapter
- · OECircleStyle namespace
- OEBondGlyphArrow class
- OEBondGlyphCircle class
- OEBondGlyphCross class
- OEBondGlyphCurvedArrow class
- OEBondGlyphStitch class

• OEBondGlyphZigZag class

The following methods are publicly inherited from OEBondGlyphBase:

CreateCopy RenderGlyph

#### **Constructors**

OEBondGlyphScissors (const OEDepict:: OEPen &pen, double scissorsLengthScale=1.0, unsigned int layer=OEDepict:: OELayerPosition:: Above)

Creates an OEBondGlyphCross object with the specified parameters.

![](_page_87_Figure_7.jpeg)

Fig. 15: Example of bond annotations

**pen** The pen used when drawing scissors across the middle of the bond.

See examples (A) and (B) in Figure: Example of bond annotations.

scissorsLengthScale The multiplier used to modify the length of the drawn scissors.

See examples (A) and (C) in Figure: Example of bond annotations.

layer Specifies whether the scissors are drawn above (OELayerPosition\_Above) or below (OELayerPosition\_Below) the molecule.

See examples (B) and (D) in Figure: Example of bond annotations.

#### **CreateCopy**

OEBondGlyphBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondGlyphScissors object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

```
bool RenderGlyph (OEDepict::OE2DMolDisplay &disp,
                                                        const OEChem:: OEBondBase *bond)
\rightarrow const
```

Draws a glyph (in this case a scissors) in the middle of the given bond.

disp The OE2DMolDisplay object that is modified to annotate the specified bond.

**bond** The OEBondBase object being annotated.

## 5.1.14 OEBondGlyphStitch

class OEBondGlyphStitch : public OEBondGlyphBase

By using the *OEBondGlyphStitch* class, bonds can be annotated by drawing perpendicular lines across them.

See also:

- Annotating Atoms and Bonds chapter
- OEBondGlyphArrow class
- OEBondGlyphCircle class
- OEBondGlyphCross class
- OEBondGlyphCurvedArrow class
- OEBondGlyphScissors class
- OEBondGlyphZigZag class

The following methods are publicly inherited from OEBondGlyphBase:

CreateCopy RenderGlyph

#### **Constructors**

```
OEBondGlyphStitch (const OEDepict:: OEPen &pen, unsigned int nrstitches=2u,
                  double stitchLengthScale=1.0,
                  unsigned int layer=OEDepict:: OELayerPosition:: Above)
```

Creates an OEBondGlyphZigZag object with the specified parameters.

*pen* The pen used when drawing the perpendicular lines across the bond.

See examples (A) and (B) in Figure: Example of bond annotations.

*nrstitches* The number of perpendicular lines drawn across the bond. This value has to be in the range of [1, 5].

See examples (A) and (C) in Figure: Example of bond annotations.

stitchLengthScale The multiplier used to modify the length of the drawn perpendicular lines.

See examples (A) and (D) in Figure: Example of bond annotations.

layer Specifies whether the perpendicular lines are drawn above (OELayerPosition\_Above) or below (OELayerPosition\_Below) the molecule.

See examples (B) and (E) in Figure: Example of bond annotations.

![](_page_89_Figure_1.jpeg)

![](_page_89_Figure_2.jpeg)

#### **CreateCopy**

```
OEBondGlyphBase *CreateCopy() const
```

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondGlyphStitch object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

```
bool RenderGlyph (OEDepict:: OE2DMolDisplay & disp,
                  const OEChem:: OEBondBase *bond) const
```

## 5.1.15 OEBondGlyphZigZag

```
class OEBondGlyphZigZag : public OEBondGlyphBase
```

By using the OEBondGlyphZigZag class, bonds can be annotated by drawing a zig-zag line across them.

See also:

- Annotating Atoms and Bonds chapter
- OEBondGlyphArrow class
- OEBondGlyphCircle class
- OEBondGlyphCross class
- OEBondGlyphCurvedArrow class
- OEBondGlyphScissors class
- OEBondGlyphStitch class

The following methods are publicly inherited from OEBondGlyphBase:

RenderGlyph CreateCopy

#### **Constructors**

```
OEBondGlyphZiqZaq(const OEDepict::OEPen &pen, double ziqzaqLengthScale=1.0,
                  unsigned int layer=OEDepict:: OELayerPosition:: Above,
                  bool diagonal= false)
```

Creates an OEBondGlyphZigZag object with the specified parameters.

![](_page_90_Figure_4.jpeg)

Fig. 17: Example of bond annotations

**pen** The pen used when drawing a zig-zag line across bond.

See examples (A) and (B) in *Figure: Example of bond annotations*.

zigzagLengthScale The multiplier used to modify the length of the drawn zig-zag line.

See examples (A) and (C) in Figure: Example of bond annotations.

layer Specifies whether the zig-zag line is drawn above (OELayerPosition\_Above) or below (OELayerPosition\_Below) the molecule.

See examples (B) and (D) in Figure: Example of bond annotations.

*diagonal* Specifies whether the zig-zag line is drawn across the bond or in parallel with it.

See examples (A) and (E) in Figure: Example of bond annotations.

#### **CreateCopy**

OEBondGlyphBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBondGlyphZigZag object is dynamically allocated and owned by the caller.

#### **RenderGlyph**

bool RenderGlyph (OEDepict:: OE2DMolDisplay &disp, const OEChem:: OEBondBase \*bond) const

Draws a glyph (in this case a zig-zag line) across the given bond.

disp The OE2DMolDisplay object that is modified to annotate the specified bond.

**bond** The OEBondBase object being annotated.

## 5.1.16 OEColorGradientDisplayOptions

#### class OEColorGradientDisplayOptions

This class represents the OEColorGradientDisplayOptions class that holds properties that determine how a color gradient is rendered.

#### See also:

· OEDrawColorGradient function

#### **Constructors**

```
OEColorGradientDisplayOptions()
```

Default constructor.

![](_page_91_Picture_9.jpeg)

#### Fig. 18: Example of drawing a color gradient with default options

OEColorGradientDisplayOptions(const OEColorGradientDisplayOptions & rhs)

Copy constructor.

#### operator=

```
OEColorGradientDisplayOptions &
 operator=(const OEColorGradientDisplayOptions &rhs)
```

Assignment operator.

#### **AddLabel**

void AddLabel (const OEColorGradientLabel &label)

Adds an additional label that will be rendered on the strip of the color gradient.

label The OEColorGradientLabel object that defines the label and the position where the label is going to be rendered to the color gradient.

#### **Example:**

![](_page_92_Figure_1.jpeg)

Fig. 19: Example of using the AddLabel method

#### See also:

- OEColorGradientLabel class
- · OEColorGradientDisplayOptions. GetLabels method
- · OEColorGradientDisplayOptions. ClearLabels method

#### **AddMarkedValue**

void AddMarkedValue (double value)

Adds an additional value that will be marked on the strip of the color gradient along with the label of the value above the strip.

**Example:** 

![](_page_92_Figure_11.jpeg)

![](_page_92_Figure_12.jpeg)

Fig. 20: Example of using the AddMarkedValue method

- · OEColorGradientDisplayOptions.AddMarkedValues method
- · OEColorGradientDisplayOptions.GetMarkedValues method
- · OEColorGradientDisplayOptions. SetMarkedValues method

· OEColorGradientDisplayOptions. ClearMarkedValues method

#### **AddMarkedValues**

```
void AddMarkedValues (const std::vector<double> &values)
```

Adds additional values that will be marked on the strip of the color gradient along with their labels above the strip.

#### **Example:**

![](_page_93_Figure_6.jpeg)

Fig. 21: Example of using the AddMarkedValues method

#### See also:

- · OEColorGradientDisplayOptions.AddMarkedValue method
- · OEColorGradientDisplayOptions. ClearMarkedValues method
- · OEColorGradientDisplayOptions.GetMarkedValues method
- · OEColorGradientDisplayOptions. SetMarkedValues method

#### **ClearBoxRange**

void ClearBoxRange()

Removes the range previously set to be marked on the color gradient.

- · OEColorGradientDisplayOptions. SetBoxRange method
- · OEColorGradientDisplayOptions. GetBoxRangeMax method
- · OEColorGradientDisplayOptions.GetBoxRangeMin method

#### **ClearLabels**

void ClearLabels()

Removes labels previously set by the OEColorGradientDisplayOptions. AddLabel method to be marked on the color gradient.

#### See also:

- · OEColorGradientDisplayOptions.AddLabel method
- · OEColorGradientDisplayOptions.GetLabels method

#### **ClearMarkedValues**

void ClearMarkedValues()

Removes any values previously set to be marked on the color gradient.

#### See also:

- · OEColorGradientDisplayOptions.AddMarkedValue method
- · OEColorGradientDisplayOptions.AddMarkedValues method
- · OEColorGradientDisplayOptions.GetMarkedValues method
- · OEColorGradientDisplayOptions. SetMarkedValues method

#### **GetBoxRangeMax**

double GetBoxRangeMax () const

Returns the minimum value of the range being marked on the color gradient.

#### See also:

- · OEColorGradientDisplayOptions. ClearBoxRange method
- · OEColorGradientDisplayOptions. SetBoxRange method

#### **GetBoxRangeMin**

double GetBoxRangeMin() const

Returns the maximum value of the range being marked on the color gradient.

- · OEColorGradientDisplayOptions. ClearBoxRange method
- · OEColorGradientDisplayOptions. SetBoxRange method

#### **GetBoxRangePen**

Returns the pen used to draw the box to mark the range set by the OEColorGradientDisplayOptions. SetBoxRange method.

const OEDepict:: OEPen & GetBoxRangePen() const

See also:

- OEPen class
- · OEColorGradientDisplayOptions.SetBoxRange
- · OEColorGradientDisplayOptions. SetBoxRangePen method

#### **GetColorStopLabelFont**

const OEDepict:: OEFont & GetColorStopLabelFont () const

Returns the font that is used to render the color stops of the color gradient.

#### See also:

- OEFont class
- · OEColorGradientDisplayOptions.SetColorStopLabelFont method

#### **GetColorStopLabelFontScale**

double GetColorStopLabelFontScale() const

Returns the multiplier that can be used to increase or decrease the size of the color stop label fonts.

#### See also:

· OEColorGradientDisplayOptions.SetColorStopLabelFontScale method

#### **GetColorStopPrecision**

unsigned int GetColorStopPrecision() const

Returns the precision of the color stop labels *i.e.* the number of digits that is written to express the floating-point values.

#### See also:

· OEColorGradientDisplayOptions.GetColorStopPrecision method

#### **GetColorStopVisibility**

bool GetColorStopVisibility() const

Returns whether the color stop labels are rendered.

#### See also:

· OEColorGradientDisplayOptions.SetColorStopVisibility method

#### **GetLabels**

OESystem:: OEIterBase<OEColorGradientLabel> \*GetLabels() const

Returns an iterator over the labels that are being rendered onto the color gradient.

#### See also:

- OEColorGradientLabel class
- · OEColorGradientDisplayOptions.AddLabel method
- · OEColorGradientDisplayOptions. ClearLabels method

#### **GetMarkedValuePen**

const OEDepict:: OEPen &GetMarkedValuePen() const

Returns the pen that is used to draw the lines for the marked values.

#### See also:

- OEPen class
- · OEColorGradientDisplayOptions.SetMarkedValuePen method

#### **GetMarkedValuePrecision**

unsigned int GetMarkedValuePrecision() const

Returns the precision of the marked value labels *i.e.* the number of digits that is written to express the floating-point values.

#### See also:

· OEColorGradientDisplayOptions.SetMarkedValuePrecision method

#### **GetMarkedValues**

OESystem:: OEIterBase<double> \*GetMarkedValues() const

Returns an iterator over the values that are being marked on the color gradient.

#### See also:

- · OEColorGradientDisplayOptions.AddMarkedValue method
- · OEColorGradientDisplayOptions.AddMarkedValues method
- · OEColorGradientDisplayOptions. ClearMarkedValues method
- · OEColorGradientDisplayOptions. SetMarkedValues method

#### **SetBoxRange**

void SetBoxRange (double minvalue, double maxvalue)

Sets the range being marked on the color gradient.

*minvalue, maxvalue* The minimum and maximum value of the range.

#### **Example:**

```
opts = oegrapheme.OEColorGradientDisplayOptions()
opts.SetBoxRange(-0.5, 0.5)
oegrapheme. OEDrawColorGradient (image, colorg, opts)
```

![](_page_97_Picture_15.jpeg)

#### Fig. 22: Example of using the SetBoxRange method

- · OEColorGradientDisplayOptions. ClearBoxRange method
- · OEColorGradientDisplayOptions. GetBoxRangeMax method
- · OEColorGradientDisplayOptions.GetBoxRangeMin method
- · OEColorGradientDisplayOptions. SetBoxRange method

#### **SetBoxRangePen**

void SetBoxRangePen (const OEDepict:: OEPen &pen)

Sets the pen used to mark a specified range on the color gradient.

#### **Example:**

![](_page_98_Figure_5.jpeg)

![](_page_98_Figure_6.jpeg)

Fig. 23: Example of using the SetBoxRangePen method

#### See also:

- OEPen class
- · OEColorGradientDisplayOptions.GetBoxRangePen method
- · OEColorGradientDisplayOptions. SetBoxRange method

#### **SetColorStopLabelFont**

void SetColorStopLabelFont (const OEDepict:: OEFont &font)

Sets the font that is used to render color stops of the color gradient.

#### **Example:**

```
opts = oegrapheme.OEColorGradientDisplayOptions()
font = <code>oedepict.OEFont()</code>font.SetColor(oechem.OEDarkGreen)
font.SetStyle(oedepict.OEFontStyle_Bold)
opts.SetColorStopLabelFont(font)
oegrapheme.OEDrawColorGradient(image, colorg, opts)
```

Note: The size of font also depends on dimensions of the image into which the color gradient is rendered. See also OEDrawColorGradient function.

#### See also:

• OEFont class

![](_page_99_Figure_1.jpeg)

Fig. 24: Example of using the SetColorStopLabelFont method

· OEColorGradientDisplayOptions.GetColorStopLabelFont method

#### **SetColorStopLabelFontScale**

void SetColorStopLabelFontScale(double scale)

Sets the multiplier that can be used increase or decrease the size of the fonts of the color stop labels.

```
scale This value has to be in the range of [0.5, 3.0].
```

#### **Example:**

```
opts = oegrapheme. OEColorGradientDisplayOptions()
opts.SetColorStopLabelFontScale(0.5)
oegrapheme. OEDrawColorGradient (image, colorg, opts)
```

![](_page_99_Figure_10.jpeg)

#### Fig. 25: Example of using the SetColorStopLabelFontScale method

- · OEColorGradientDisplayOptions.GetColorStopLabelFontScale method
- · OEColorGradientDisplayOptions.GetColorStopLabelFont method
- · OEColorGradientDisplayOptions.SetColorStopLabelFont method

#### **SetColorStopPrecision**

void SetColorStopPrecision (unsigned int precision)

Sets the precision of the color stop labels *i.e.* the number of digits that is written to express the floating-point values.

*precision* The zero value means that the precision is determined by the lowest significant digits of the color stop values that is in the range of  $[1,4]$ .

#### **Example:**

![](_page_100_Figure_6.jpeg)

![](_page_100_Figure_7.jpeg)

#### See also:

· OEColorGradientDisplayOptions.GetColorStopPrecision method

#### **SetColorStopVisibility**

void SetColorStopVisibility (bool visible)

Sets whether the color stop labels are rendered.

#### **Example:**

```
opts = oegrapheme.OEColorGradientDisplayOptions()
opts.SetColorStopVisibility(False)
oegrapheme. OEDrawColorGradient (image, colorg, opts)
```

![](_page_100_Picture_15.jpeg)

Fig. 27: Example of using the SetColorStopVisibility method

· OEColorGradientDisplayOptions.GetColorStopVisibility method

#### **SetMarkedValuePen**

```
void SetMarkedValuePen (const OEDepict:: OEPen &pen)
```

Sets the pen that is used to draw the lines for the marked values.

#### **Example:**

![](_page_101_Figure_6.jpeg)

![](_page_101_Figure_7.jpeg)

Fig. 28: Example of using the SetMarkedValuePen method

#### See also:

- OEPen class
- · OEColorGradientDisplayOptions.GetMarkedValuePen method

#### **SetMarkedValuePrecision**

void SetMarkedValuePrecision (unsigned int precision)

Sets the precision of the marked value labels *i.e.* the number of digits that is written to express the floating-point values. Decreasing the precision can result in collapsing that labels of two or more distinct values into one label.

#### **Example:**

```
opts = oegrapheme.OEColorGradientDisplayOptions()
markedvalues = oechem. 0EDoubleVector([0.20, 0.70, 0.72])opts.AddMarkedValues(markedvalues)
opts.SetMarkedValuePrecision(1)
oegrapheme. OEDrawColorGradient (image, colorg, opts)
```

#### See also:

· OEColorGradientDisplayOptions.GetMarkedValuePrecision method

![](_page_102_Figure_1.jpeg)

#### Fig. 29: Example of using the SetMarkedValuePrecision method

#### **SetMarkedValues**

```
void SetMarkedValues (const std:: vector<double> &values)
```

Initializes values that will be marked on the strip of the color gradient along with the value labels above the strip. OEColorGradientDisplayOptions. SetMarkedValues method discards the list of values set in prior calls.

#### **Example:**

![](_page_102_Figure_7.jpeg)

Fig. 30: Example of using the SetMarkedValues method

- · OEColorGradientDisplayOptions.AddMarkedValue method
- · OEColorGradientDisplayOptions.AddMarkedValues method
- · OEColorGradientDisplayOptions. ClearMarkedValues method

## 5.1.17 OEColorGradientLabel

#### class OEColorGradientLabel

The OEColorGradientLabel class stores a value (double) and label (string) pair that is used by the OEColorGradient-DisplayOptions class to render user defined labels into the color gradients.

![](_page_103_Figure_4.jpeg)

#### Fig. 31: Example of depicting labels above the color gradient

#### See also:

· OEColorGradientDisplayOptions.AddLabel method

#### **Constructors**

```
OEColorGradientLabel (double value, const std::string &label)
```

*value* Defines the position of the string being rendered.

label Defines the string being rendered.

Constructor.

```
OEColorGradientLabel (const OEColorGradientLabel & rhs)
```

Copy constructor.

#### operator=

OEColorGradientLabel & operator=(const OEColorGradientLabel & rhs)

Assignment operator.

#### GetLabel

std::string GetLabel() const

Returns the string stored in the OEColorGradientLabel object that will be rendered into the color gradient.

#### **GetValue**

double GetValue() const

Returns the value stored in the OEColorGradientLabel object that defined the position of the associated label on the color gradient.

## 5.1.18 OEColorForceFieldDisplay

```
class OEColorForceFieldDisplay
```

This class represents OEColorForceFieldDisplay that stores the depiction information of a OEColorForceField object. See example in Figure: Example of depicting a color force field in a legend.

See also:

- The Theory chapter of the Shape TK manual.
- OEColorForceFieldLegendDisplayOptions class
- · OEDrawColorForceFieldLegend function

![](_page_104_Figure_11.jpeg)

Fig. 32: Example of depicting a color force field in a legend

#### **Code Example**

• Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

#### **Constructors**

```
OEColorForceFieldDisplay(const OEShape::OEColorForceField &cff, bool
→preserveQueryColors=false)
```

Creates an OEColorForceFieldDisplay object with a given color force field and an option to preserve colors on input query molecules.

```
OEColorForceFieldDisplay(const OEColorForceFieldDisplay &rhs)
```

Copy constructor.

#### operator=

```
OEColorForceFieldDisplay & operator=(const OEColorForceFieldDisplay & rhs)
```

Assignment operator.

#### **GetColor**

const OESystem:: OEColor &GetColor (unsigned int type) const

Returns the color that is associated with the given color atom type.

#### **GetColorTypes**

OESystem:: OEIterBase<unsigned int> \*GetColorTypes() const

Returns the iterator over the color atom types.

#### **GetName**

std::string GetName (unsigned int type) const

Returns the name that is associated with the given color atom type.

#### **NumColorTypes**

unsigned int NumColorTypes () const

Returns the number of color atom types.

#### **SetColor**

void SetColor (unsigned int type, const OEDepict:: OEColor& color)

Sets the color that is associated with the given color atom type.

#### **SetName**

void SetName (unsigned int type, const std::string& name)

Sets the name that is associated with the given color atom type.

## 5.1.19 OEColorForceFieldLegendDisplayOptions

#### class OEColorForceFieldLegendDisplayOptions

This class represents OEColorForceFieldLegendDisplayOptions that encapsulates properties that determine how the legend of a color force field is depicted by the OEDrawColorForceFieldLegend function.

#### See also:

- OEColorForceFieldDisplay class
- · OEDrawColorForceFieldLegend function

#### **Constructors**

OEColorForceFieldLegendDisplayOptions (unsigned int rows, unsigned int cols)

Creates an OEColorForceFieldLegendDisplayOptions object with the specified number of rows and columns..

rows The number of rows in the legend.

cols The number of columns in the legend.

```
OEColorForceFieldLegendDisplayOptions(const OEColorForceFieldLegendDisplayOptions &
\rightarrowrhs)
```

Copy constructor.

#### operator=

```
OEColorForceFieldLegendDisplayOptions &
 operator=(const OEColorForceFieldLegendDisplayOptions &rhs)
```

Assignment operator.

#### **NumCols**

unsigned int NumCols() const

Returns the number of columns of the legend.

#### **NumRows**

unsigned int NumRows () const

Returns the number of rows of the legend.

## 5.1.20 OEColorOverlapDisplayOptions

class OEColorOverlapDisplayOptions : public OEDepict::OE2DMolDisplayOptions

This class represents OEColorOverlapDisplayOptions that encapsulates properties that determine how the color atom overlap between the reference and the fit molecule is depicted by the  $OERenderColorOverlap$  function.

#### See also:

- OEShapeOverlapDisplay class
- · OERenderColorOverlap function

#### **Code Example**

• Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

The following methods are publicly inherited from OE2DMolDisplayOptions:

| operator=                    | GetHydrogenStyle          | SetBondLineAtomLabelGapScale |
|------------------------------|---------------------------|------------------------------|
| GetAromaticStyle             | GetMargin                 | SetBondLineGapScale          |
| GetAtomColor                 | GetScale                  | SetBondPropLabelFont         |
| GetAtomColorStyle            | GetSuperAtomLabelFont     | SetBondPropLabelFontScale    |
| GetAtomLabelFont             | GetSuperAtomStyle         | SetBondPropertyFunctor       |
| GetAtomLabelFontScale        | GetTitleFont              | SetBondStereoStyle           |
| GetAtomPropLabelFont         | GetTitleFontScale         | SetBondWidthScaling          |
| GetAtomPropLabelFontScale    | GetTitleHeight            | SetDefaultBondPen            |
| GetAtomPropertyFunctor       | GetTitleLocation          | SetDimensions                |
| GetAtomStereoStyle           | GetWidth                  | SetHeight                    |
| GetBackgroundColor           | SetAromaticStyle          | SetHydrogenStyle             |
| GetBondColorStyle            | SetAtomColor              | SetMargin                    |
| GetBondLineAtomLabelGapScale | SetAtomColorStyle         | SetMargins                   |
| GetBondLineGapScale          | SetAtomLabelFont          | SetScale                     |
| GetBondPropLabelFont         | SetAtomLabelFontScale     | SetSuperAtomLabelFont        |
| GetBondPropLabelFontScale    | SetAtomPropLabelFont      | SetSuperAtomStyle            |
| GetBondPropertyFunctor       | SetAtomPropLabelFontScale | SetTitleFont                 |
| GetBondStereoStyle           | SetAtomPropertyFunctor    | SetTitleFontScale            |
| GetBondWidthScaling          | SetAtomStereoStyle        | SetTitleHeight               |
| GetDefaultBondPen            | SetBackgroundColor        | SetTitleLocation             |
| GetHeight                    | SetBondColorStyle         | SetWidth                     |

#### **Constructors**

OEColorOverlapDisplayOptions()

#### Default constructor.

OEColorOverlapDisplayOptions(const OEColorOverlapDisplayOptions & rhs)

Copy constructor.

#### operator=

OEColorOverlapDisplayOptions & operator=(const OEColorOverlapDisplayOptions & rhs)

Assignment operator.

#### **ClearQuerySurfaceArcFxn**

void ClearQuerySurfaceArcFxn()

Removes the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule around the fit molecule.

See also:

- · OEColorOverlapDisplayOptions.GetQuerySurfaceArcFxn
- · OEColorOverlapDisplayOptions.SetQuerySurfaceArcFxn

#### **GetClearBackground**

bool GetClearBackground() const

Returns whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the rendering of the color overlap.

#### See also:

· OEColorOverlapDisplayOptions.SetClearBackground

#### **GetQuerySurfaceArcFxn**

const OESurfaceArcFxnBase \*GetQuerySurfaceArcFxn() const

Returns the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule around the fit molecule.

#### See also:

- · OEColorOverlapDisplayOptions.ClearQuerySurfaceArcFxn
- · OEColorOverlapDisplayOptions.SetQuerySurfaceArcFxn

#### **SetClearBackground**

void SetClearBackground (bool clear)

Returns whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the rendering of the color overlap.

See also:

· OEColorOverlapDisplayOptions.GetClearBackground

#### **SetQuerySurfaceArcFxn**

void SetQuerySurfaceArcFxn (const OESurfaceArcFxnBase &arcfxn)

Sets the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule around the fit molecule when calling the OERenderColorOverlap function to depict the atom color overlap.

#### See also:

- · OEColorOverlapDisplayOptions.ClearQuerySurfaceArcFxn
- · OEColorOverlapDisplayOptions.GetQuerySurfaceArcFxn

## 5.1.21 OEDepictionFrom3DOptions

```
class OEDepictionFrom3DOptions
```

This class represents OEDepictionFrom3DOptions that stores parameters that are used when generating 2D coordinates by calling the OEPrepareDepictionFrom3D function.

| Property                     | Get method               | Set method               |
|------------------------------|--------------------------|--------------------------|
| inertial frame               | GetCoordsToInertialFrame | SetCoordsToInertialFrame |
| max number of bond rotations | GetMaxBondRotations      | SetMaxBondRotations      |
| rotate to 2D reference       | GetRotateTo2DReference   | SetRotateTo2DReference   |
| suppressing hydrogens        | GetSuppressHydrogens     | SetSuppressHydrogens     |

#### **Constructors**

OEDepictionFrom3DOptions (bool suppressH=true)

Default constructor that initializes an OEDepictionFrom3DOptions object with the following properties:

#### Table 2: Default parameters of the OEDepictionFrom3DOptions

class

| Property                     | Default value    |
|------------------------------|------------------|
| inertial frame               | false            |
| max number of bond rotations | $2^{16} = 65536$ |
| rotate to 2D reference       | false            |
| suppressing hydrogens        | true             |

OEDepictionFrom3DOptions (const OEDepictionFrom3DOptions & rhs)

Copy constructor.

#### operator=

OEDepictionFrom3DOptions & operator=(const OEDepictionFrom3DOptions & rhs)

Assignment operator.

#### **GetCoordsToInertialFrame**

**bool** GetCoordsToInertialFrame() const

Returns whether the 3D molecule is moved to its inertial frame before generating the 2D coordinates.

#### See also:

· OEDepictionFrom3DOptions. SetCoordsToInertialFrame method

#### **GetMaxBondRotations**

unsigned int GetMaxBondRotations () const

Returns the maximum number of bond rotations performed during the 2D coordinate generation process.

The default value for maximum number of bond rotations is  $2^{16} = 65536$ . This means that by default only the first 16 single bonds of the molecule will be rotated to find the 'closest' 2D layout to the original 3D conformation.

#### See also:

· OEDepictionFrom3DOptions. SetMaxBondRotations method

#### GetRotateTo2DReference

bool GetRotateTo2DReference() const

Returns whether after the 2D coordinate generation a final rotation is performed to orient the 2D coordinates according to the 3D conformation.

#### See also:

· OEDepictionFrom3DOptions.SetRotateTo2DReference method

#### GetSuppressHydrogens

bool GetSuppressHydrogens() const

Returns whether the explicit hydrogens are suppressed in the molecule prior to generating the 2D coordinates.

#### See also:

· OEDepictionFrom3DOptions. SetSuppressHydrogens method

#### **SetCoordsToInertialFrame**

void SetCoordsToInertialFrame (bool)

Sets whether the 3D molecule is moved to its inertial frame before generating the 2D coordinates.

#### See also:

· OEDepictionFrom3DOptions.SetCoordsToInertialFrame method

#### **SetMaxBondRotations**

void SetMaxBondRotations (unsigned int maxrotations)

Sets the maximum number of bond rotations performed during the 2D coordinate generation process.

maxrotations

The zero value means that there is no limit. Upon reaching this limit, the process terminates and returns the 2D coordinates that is the "closest" to the original 3D coordinates up to that point.

**Hint:** The default value for maximum number of bond rotations is  $2^{16} = 65536$ . This means that by default only the first 16 single bonds of the molecule will be rotated to find the 2D layout that is the 'closest' to the original 3D conformation.

It is recommended to use this parameter if the input 3D molecule has a large number of rotatable bonds.

#### See also:

· OEDepictionFrom3DOptions.GetMaxBondRotations method

#### SetRotateTo2DReference

void SetRotateTo2DReference (bool)

Sets whether after the 2D coordinate generation a final rotation is performed to orient the 2D coordinates according to the 3D conformation. This can be used to ensure that 2D molecules are oriented similarly when they 3D conformations were similar.

#### See also:

· OEDepictionFrom3DOptions.GetRotateTo2DReference method

#### **SetSuppressHydrogens**

void SetSuppressHydrogens (bool suppressH)

Sets whether the explicit hydrogens are suppressed in the molecule prior to generating the 2D coordinates. Only hydrogens that are necessary to faithfully represent tetrahedral stereochemistry will be kept.

#### See also:

· OEDepictionFrom3DOptions.GetSuppressHydrogens method

## 5.1.22 OENearestResidue

#### class OENearestResidue

The OENearestResidue class that is used by OEGetNearestResidue and OEGetNearbyResidue functions. It stores an atom pointer, an associated distance and the display position of the atom.

#### **Constructors**

```
OENearestResidue (const OEChem:: OEResidue & residue, double dist,
                 const OEDepict:: OE2DPoint &pos)
```

Constructor.

#### **GetDisplayPosition**

const OEDepict:: OE2DPoint & GetDisplayPosition() const

Returns the display position of the nearest residue.

#### **GetDist**

double GetDist() const

Returns the distance associated with the residue.

#### **GetResidue**

const OEChem:: OEResidue & GetResidue () const

Returns the residue stored in the OENearestResidue object.

#### **IsValid**

bool IsValid() const

Returns whether the OENearestResidue object is initialized correctly.

## 5.1.23 OEPeptideDisplayOptions

#### class OEPeptideDisplayOptions

This class represents the OEPeptideDisplayOptions class that encapsulates properties that determine how a peptide is depicted.

#### See also:

· OEDrawPeptide function

#### **Code Example**

• Depicting Peptides OpenEye Python Cookbook recipe

#### **Constructors**

OEPeptideDisplayOptions (unsigned int style=OEPeptideLabelStyle::Default)

Default constructor.

![](_page_113_Figure_6.jpeg)

#### Fig. 33: Peptide depiction with default options

OEPeptideDisplayOptions(const OEPeptideDisplayOptions & rhs)

Copy constructor.

operator=

OEPeptideDisplayOptions & operator= (const OEPeptideDisplayOptions & rhs)

Assignment operator.

#### **GetAminoAcidScale**

double GetAminoAcidScale() const

Returns the scaling factor of amino-acid components in interactive mode.

#### See also:

• OEPeptideDisplayOptions. SetAminoAcidScale method

#### GetInteractive

bool GetInteractive() const

Returns whether the generated svg image will be interactive.

#### See also:

· OEPeptideDisplayOptions. SetInteractive method

#### **GetLabelStyle**

unsigned int GetLabelStyle() const

Returns the style that controls the label of the amino acid circles are displayed. The return value is taken from the OEPeptideLabelStylenamespace.

#### See also:

- · OEPeptideDisplayOptions. SetLabelStyle method
- · OEPeptideLabelStyle namespace

#### **SetAminoAcidScale**

void SetAminoAcidScale (double scale)

Sets the scaling factor of amino-acid components in interactive mode.

scale This value has to be in a range of  $[0.25, 0.75]$ . The default value is 0.50.

Note: This option has to be used along with the OEPeptideDisplayOptions. SetInteractive method

#### **Example:**

```
opts = oegrapheme. OEPeptideDisplayOptions()
opts.SetInteractive(True)
opts.SetAminoAcidScale(0.75)
```

There is no image available for the PDF version of this book.

**Note:** This functionality is **only available** for . svg image format. In other image formats it has no effect.

#### **SetInteractive**

void SetInteractive (bool interactive)

Sets whether the generated svq image will be interactive. In interactive mode the amino acid components of the compact peptide representation are depicted on mouse over.

#### **Example:**

```
opts = oegrapheme.OEPeptideDisplayOptions()
opts. SetInteractive (True)
```

There is no image available for the PDF version of this book.

**Note:** This functionality is **only available** for  $. s \vee q$  image format. In other image formats it has no effect.

#### **SetLabelStyle**

void SetLabelStyle (unsigned int style)

Sets the style that controls how labels inside the amino acid circles are displayed.

style This value has to be from the OEPeptideLabelStyle namespace.

#### **Example:**

```
opts = oegrapheme.OEPeptideDisplayOptions()
opts.SetLabelStyle(oegrapheme.OEPeptideLabelStyle_SingleLetter)
```

See also:

• OEPeptideLabelStyle namespace

## 5.1.24 OEPlotMarker

```
class OEPlotMarker
```

This class represents the OEPlotMarker class that encapsulates properties that determine how a plot is depicted.

#### See also:

• OERamachandranPlot class

![](_page_116_Figure_1.jpeg)

#### Fig. 34: Peptide depiction with single letter style

#### **Constructors**

OEPlotMarker (const OEDepict:: OEPen &pen, unsigned int style=OEPlotMarkerStyle::Circle, double scale=1.0)

Creates and initializes an OEPlotMarker object with the given parameters.

**pen** The OEPen object that is used to draw the plot marker.

- style The property that determine the style of the plot marker. This value has to be from the OEP1otMarkerStyle namespace.
- scale The multiplier that can be used to increase or to decrease the size of the plot market. This value has to be in the range of  $[0.25, 4.0]$ .

OEPlotMarker (const OEPlotMarker & rhs)

Copy constructor.

#### operator=

OEPlotMarker & operator=(const OEPlotMarker & rhs)

Assignment operator.

#### operator!=

bool operator! = (const OEPlotMarker &) const

Determines whether two OEPlotMarker objects are different. Two OEPlotMarker objects are considered different, if any of their properties (such as pen, style or scale) are different.

#### operator==

| <b>bool operator==(const OEPlotMarker &amp;) const</b> |
|--------------------------------------------------------|
|--------------------------------------------------------|

Determines whether two OEPlotMarker objects are equal. Two OEPlotMarker objects are considered equivalent only if all of their properties (such as pen, style or scale) are identical.

#### **GetPen**

```
const OEDepict:: OEPen & GetPen() const
```

Returns the pen of the plot marker.

#### See also:

• OEPen class

#### **GetScale**

double GetScale() const

Returns the multiplier that is used to increase or to decrease size of the plot marker.

#### **GetStyle**

unsigned int GetStyle() const

Returns the style of the plot marker. The return value is taken from the  $OEPlotMatrixExtyle$  namespace.

#### See also:

· OEPlotMarkerStyle namespace

## 5.1.25 OERamachandranPlot

class OERamachandranPlot

This class represents OERamachandranPlot that stores data of a Ramachandran plot.

There is no image available for the PDF version of this book.

#### See also:

- · OERenderRamachandranPlot function
- OERamachandranAnalysis class in OEChem TK manual

#### **Code Example**

• Ramachandran Plot OpenEye Python Cookbook recipe

#### **Constructors**

```
OERamachandranPlot()
```

Default constructor that creates an empty OERamachandranPlot object.

OERamachandranPlot (const OERamachandranPlot & rhs)

Copy constructor.

#### operator=

OERamachandranPlot & operator= (const OERamachandranPlot & rhs)

Assignment operator.

#### **AddMolecule**

bool AddMolecule (const OEChem:: OEMolBase & mol)

Adds the molecule to the plot with default style.

*mol* The macro-peptide of which backbone dihedral phi  $(\phi)$  and psi  $(\psi)$  angle pairs are added to the plot. The residues of the molecule have to be perceived beforehand.

```
bool AddMolecule (const OEChem:: OEMolBase &mol,
                 const OEPlotMarker &outmarker,
                 const OEPlotMarker &inmarker)
```

Adds the mol to the plot with the given style.

*mol* The macro-peptide of which backbone dihedral phi  $(\phi)$  and psi  $(\psi)$  angle pairs are added to the plot. The residues of the molecule have to be perceived beforehand.

outmarker The style that is used to render data points with OERamaCategory\_Outlier category.

*inmarker* The style that is used to render data points with OERamaCategory\_Favored or OERamaCategory\_Allowed category.

#### **AddRamachandran**

```
bool AddRamachandran (const OEBio:: OERamachandranAnalysis & rama,
                      const std:: string &label,
                      const OEPlotMarker &marker)
```

Adds the data of the given OERamachandranAnalysis object to the plot with the given style and interactive label.

rama The OERamachandranAnalysis object

**label** The label that will be displayed in hover mode if the  $(\phi, \psi)$  value pair stored in the OERamachandranAnalysis object is an outlier.

*marker* The style that is used to render the data point on the plot.

See also:

• OERamachandranAnalysis class

#### **NumDataPoints**

unsigned int NumDataPoints (unsigned int ramatype, unsigned int category) const

Returns the number of data points stored in the OERamachandranPlot object with the given type and category.

ramatype This value has to be from the OERamaType namespace.

category This value has to be from the OERamaCategory namespace.

## 5.1.26 OEResidueSVGMarkupBase

class OEResidueSVGMarkupBase

OEResidueSVGMarkupBase is an abstract base class. Concrete class derived from this base class defines the markup of the residues in . svq images generated when calling the OERenderActiveSite function. Drawing elements representing residues in . svq image are grouped together in the following format in which the <qroup id> and <class name> strings can be defined in the derived concrete classes.

```
<g id='<group id>' class='<class name>'>
list of drawing elements
\sim \sim< / g >
```

The following classes derive from this class:

- OEResidueSVGNoMarkup
- OEResidueSVGStandardMarkup

See also:

- · OE2DActiveSiteDisplayOptions. SetResidueSVGMarkupFunctor method
- Generating Interactive SVG Images chapter in OEDepict TK manual

#### **CreateCopy**

OEResidueSVGMarkupBase \*CreateCopy() const =0

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

#### **GetClassName**

std::string GetClassName(const OEChem::OEResidue &) const =0

Returns the <class name> associated with a specific residue group in the .svg image. This is a virtual method that has to be implemented in the concrete derived classes.

#### **GetGroupId**

std::string GetGroupId(const OEChem::OEResidue &) const =0

Returns the  $\langle \text{group } id \rangle$  associated with a specific residue group in the . svq image. This is a virtual method that has to be implemented in the concrete derived classes.

## 5.1.27 OEResidueSVGNoMarkup

class OEResidueSVGNoMarkup : public OEResidueSVGMarkupBase

This class represents OEResidueSVGNoMarkup residue SVG markup functor. If this functor is passed to the OE2DActiveSiteDisplayOptions.SetResidueSVGMarkupFunctor method, the residues will be not marked in the svg image when calling the OERenderActiveSite function.

#### See also:

- Generating Interactive SVG Images chapter in OEDepict TK manual
- · OE2DActiveSiteDisplayOptions. SetResidueSVGMarkupFunctor method
- OEResidueSVGStandardMarkup functor

The following methods are publicly inherited from OEResidueSVGMarkupBase:

CreateCopy GetClassName GetGroupId

#### **Constructors**

```
OEResidueSVGNoMarkup()
```

Default constructor.

#### **CreateCopy**

OEResidueSVGMarkupBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEResidueSVGNoMarkup object is dynamically allocated and owned by the caller.

#### **GetClassName**

std::string GetClassName(const OEChem::OEResidue &residue) const

Returns an empty string.

#### **GetGroupId**

std::string GetGroupId(const OEChem::OEResidue &residue) const

Returns an empty string.

## 5.1.28 OEResidueSVGStandardMarkup

class OEResidueSVGStandardMarkup : public OEResidueSVGMarkupBase

This class represents OEResidueSVGStandardMarkup residue SVG markup functor. If this functor is passed to the OE2DActiveSiteDisplayOptions. SetResidueSVGMarkupFunctor method, the residues will be in svq image when calling the *OERenderActiveSite* function.

#### See also:

- Generating Interactive SVG Images chapter in OEDepict TK manual
- · OE2DActiveSiteDisplayOptions. SetResidueSVGMarkupFunctor method
- OEResidueSVGNoMarkup functor

The following methods are publicly inherited from OEResidueSVGMarkupBase:

CreateCopy GetClassName GetGroupId

#### **Constructors**

```
OEResidueSVGStandardMarkup (const std::string prefix="",
                           const std:: string classname="residue",
                           const char separator='-')
```

Creates an OEResidueSVGStandardMarkup object.

- **prefix** The string that will be added at the beginning of each residue group id. For information about valid ids see OEIsValidSVGGroupId function. By default, no prefix will be added.
- classname. The class name that is going to be used to mark residues. For information about valid names see OEIsValidSVGClassName function.
- separator The character used to separate the components (residue name, chain id, residue number) of the group id

By default, the following will be showed in svg image for marking a Leucine residue with chain id 'A' and residue number 715:

```
<q id='LEU-A-715' class='residue'>
list of drawing elements
\ddot{\phantom{a}}< / g>
```

#### **CreateCopy**

OEResidueSVGMarkupBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEResidueSVGNoMarkup object is dynamically allocated and owned by the caller.

#### **GetClassName**

std::string GetClassName(const OEChem::OEResidue &residue) const

Returns the string that specifies the group id of a residue in an svg image.

#### **GetGroupId**

std::string GetGroupId(const OEChem::OEResidue & residue) const

Returns the string that specifies the class name of a residue in an svg image.

## 5.1.29 OEShapeOverlapDisplay

class OEShapeOverlapDisplay

This class represents OEShapeOverlapDisplay that stores the depiction information of depicting the for molecule of shape overlap. See example in Table: Example of depicting the shape and the color overlap.

#### See also:

- The Theory chapter of the Shape TK manual.
- · OERenderColorOverlap function
- · OERenderShapeOverlapfunction

#### Table 3: Example of depicting the shape and the color overlap

![](_page_123_Figure_18.jpeg)

#### **Code Example**

• Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

#### **Constructors**

OEShapeOverlapDisplay(const OEShapeQueryDisplay &refdisp, const OEChem:: OEMolBase &fitmol)

Constructs an OEShapeOverlapDisplay object with default depiction options.

refdisp The OEShapeQueryDisplay object that stores the reference molecule of the shape overlap.

*fitmol* The 3D molecule that is overlaid to the reference molecule.

Warning: No overlay is performed to maximize the shape and color overlap between the reference and the fit molecule *i.e.* the *fitmol* has to be pre-aligned to the reference molecule stored in the OEShapeQueryDisplay object.

```
OEShapeOverlapDisplay(const OEShapeQueryDisplay &refdisp,
                      const OEChem:: OEMolBase &fitmol,
                      const OEColorOverlapDisplayOptions &copts)
OEShapeOverlapDisplay(const OEShapeQueryDisplay &refdisp,
                      const OEChem:: OEMolBase &fitmol,
                      const OEShapeOverlapDisplayOptions &sopts)
OEShapeOverlapDisplay(const OEShapeQueryDisplay &refdisp,
                      const OEChem:: OEMolBase &fitmol,
                      const OEShapeOverlapDisplayOptions &sopts,
                      const OEColorOverlapDisplayOptions &copts)
```

Constructs an OEShapeOverlapDisplay object with given depiction options.

refdisp The OEShapeQueryDisplay object that stores the reference molecule of the shape overlap.

*fitmol* The 3D molecule that is overlaid to the reference molecule.

- copts The OEColorOverlapDisplayOptions object that defines how the color atom overlap between the reference and the fit molecule is depicted.
- sopts The OEShapeOverlapDisplayOptions object that defines how the shape overlap between the reference and the fit molecule is depicted.

Warning: No overlay is performed to maximize the shape and color overlap between the reference and the fit molecule *i.e.* the *fitmol* has to be pre-aligned to the reference molecule stored in the OEShapeQueryDisplay object.

OEShapeOverlapDisplay(const OEShapeOverlapDisplay & rhs)

Copy constructor.

#### operator=

OEShapeOverlapDisplay & operator=(const OEShapeOverlapDisplay & rhs)

Assignment operator.

#### **GetTitle**

std::string GetTitle() const

Returns the title of the molecule the OEShapeOverlapDisplay object was initialized.

#### **IsValid**

bool IsValid() const

Returns whether the OEShapeOverlapDisplay object was initialized successfully. If initialization was attempted either with an invalid OEShapeOverlapDisplay object, an empty fit molecule or a fit molecule without 3D coordinates, then this method returns false.

## 5.1.30 OEShapeOverlapDisplayOptions

class OEShapeOverlapDisplayOptions : public OEDepict::OE2DMolDisplayOptions

This class represents OEShapeOverlapDisplayOptions that encapsulates properties that determine how the color atom overlap between the reference and the fit molecule is depicted by the OERenderShapeOverlap function.

#### See also:

- OEShapeOverlapDisplay class
- · OERenderShapeOverlap function

#### **Code Example**

• Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

The following methods are publicly inherited from OE2DMolDisplayOptions:

| operator=                    | GetHydrogenStyle          | SetBondLineAtomLabelGapScale |
|------------------------------|---------------------------|------------------------------|
| GetAromaticStyle             | GetMargin                 | SetBondLineGapScale          |
| GetAtomColor                 | GetScale                  | SetBondPropLabelFont         |
| GetAtomColorStyle            | GetSuperAtomLabelFont     | SetBondPropLabelFontScale    |
| GetAtomLabelFont             | GetSuperAtomStyle         | SetBondPropertyFunctor       |
| GetAtomLabelFontScale        | GetTitleFont              | SetBondStereoStyle           |
| GetAtomPropLabelFont         | GetTitleFontScale         | SetBondWidthScaling          |
| GetAtomPropLabelFontScale    | GetTitleHeight            | SetDefaultBondPen            |
| GetAtomPropertyFunctor       | GetTitleLocation          | SetDimensions                |
| GetAtomStereoStyle           | GetWidth                  | SetHeight                    |
| GetBackgroundColor           | SetAromaticStyle          | SetHydrogenStyle             |
| GetBondColorStyle            | SetAtomColor              | SetMargin                    |
| GetBondLineAtomLabelGapScale | SetAtomColorStyle         | SetMargins                   |
| GetBondLineGapScale          | SetAtomLabelFont          | SetScale                     |
| GetBondPropLabelFont         | SetAtomLabelFontScale     | SetSuperAtomLabelFont        |
| GetBondPropLabelFontScale    | SetAtomPropLabelFont      | SetSuperAtomStyle            |
| GetBondPropertyFunctor       | SetAtomPropLabelFontScale | SetTitleFont                 |
| GetBondStereoStyle           | SetAtomPropertyFunctor    | SetTitleFontScale            |
| GetBondWidthScaling          | SetAtomStereoStyle        | SetTitleHeight               |
| GetDefaultBondPen            | SetBackgroundColor        | SetTitleLocation             |
| GetHeight                    | SetBondColorStyle         | SetWidth                     |

## **Constructors**

OEShapeOverlapDisplayOptions()

#### Default constructor.

OEShapeOverlapDisplayOptions(const OEShapeOverlapDisplayOptions & rhs)

#### Copy constructors.

#### operator=

OEShapeOverlapDisplayOptions & operator=(const OEShapeOverlapDisplayOptions & rhs)

Assignment operator.

## **ClearQuerySurfaceArcFxn**

```
void ClearQuerySurfaceArcFxn()
```

Removes the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule around the fit molecule.

- · OEShapeOverlapDisplayOptions.GetQuerySurfaceArcFxn method
- · OEShapeOverlapDisplayOptions. SetQuerySurfaceArcFxn method

#### **GetClearBackground**

bool GetClearBackground() const

Returns whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the rendering of the shape overlap.

#### See also:

· OEShapeOverlapDisplayOptions. SetClearBackground method

#### **GetOverlapColor**

const OESystem:: OEColor & GetOverlapColor() const

Returns the color of the property map that is used to visualize shape overlap between the reference and the fit molecule.

#### See also:

· OEShapeOverlapDisplayOptions. SetOverlapColor method

#### **GetOverlapDisplayStyle**

unsigned int GetOverlapDisplayStyle() const

Returns the style that defines how shape overlay is depicted by the OERenderShapeOverlap function. The return value is taken from the OEShapeOverlapDisplayStyle namespace.

#### See also:

- · OEShapeOverlapDisplayOptions. SetOverlapDisplayStyle method
- · OEShapeOverlapDisplayStyle namespace

#### **GetQuerySurfaceArcFxn**

const OESurfaceArcFxnBase \*GetQuerySurfaceArcFxn() const

Returns the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule around the fit molecule.

- · OEShapeOverlapDisplayOptions. ClearQuerySurfaceArcFxn method
- · OEShapeOverlapDisplayOptions. SetQuerySurfaceArcFxn method

#### **SetClearBackground**

```
void SetClearBackground (bool clear)
```

Sets whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the rendering of the shape overlap.

#### See also:

· OEShapeOverlapDisplayOptions.GetClearBackground method

#### **SetOverlapColor**

void SetOverlapColor (const OESystem:: OEColor &color)

Sets the color of the property map that is used to visualize shape overlap between the reference and the fit molecule.

#### See also:

· OEShapeOverlapDisplayOptions.GetOverlapColor method

#### SetOverlapDisplayStyle

void SetOverlapDisplayStyle(unsigned int style)

Sets the style that defines how shape overlay is depicted by the  $OERendershapeOverlap$  function.

style This value has to be from the OEShapeOverlapDisplayStyle namespace.

#### See also:

- · OEShapeOverlapDisplayOptions.GetOverlapDisplayStyle method
- · OEShapeOverlapDisplayStyle namespace

#### **SetQuerySurfaceArcFxn**

void SetQuerySurfaceArcFxn (const OESurfaceArcFxnBase &arcfxn)

Sets the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule around the fit molecule when calling the OERenderShapeOverlap function to depict the shape overlap.

- · OEShapeOverlapDisplayOptions. ClearQuerySurfaceArcFxn method
- · OEShapeOverlapDisplayOptions.GetQuerySurfaceArcFxn method

## 5.1.31 OEShapeQueryDisplay

#### class OEShapeQueryDisplay

This class represents OEShapeQueryDisplay that stores the depiction information of a shape query *i.e.* shape reference molecule. See example in Figure: Example of depicting a shape query.

#### See also:

- The Theory chapter of the Shape TK manual.
- · OERenderShapeQuery function

![](_page_129_Figure_7.jpeg)

Fig. 35: Example of depicting a shape query

#### **Code Example**

• Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

#### **Constructors**

```
OEShapeQueryDisplay(const OEChem:: OEMolBase &refmol,
                    const OEShape:: OEColorForceField &cff)
```

Constructs an OEShapeQueryDisplay object with default depiction options.

refmol The 3D reference molecule of the shape overlap.

cff The OEColorForceField object that defines various chemical centers and their interactions.

```
OEShapeQueryDisplay(const OEChem:: OEMolBase &refmol,
                    const OEShape:: OEColorForceField &cff,
                    const OEShapeQueryDisplayOptions &opts)
```

Constructs an OEShapeQueryDisplay object with given depiction options.

refmol The 3D reference molecule of the shape overlap.

*cff* The OEColorForceField object that defines various chemical centers and their interactions.

**opts** The OEShapeQueryDisplayOptions object that defines how the shape query *i.e.* reference molecule is depicted.

```
OEShapeQueryDisplay(const OEChem::OEMolBase &refmol,
                    const OEColorForceFieldDisplay &cffdisp)
```

Constructs an OEShapeQueryDisplay object with default depiction options.

*refmol* The 3D reference molecule of the shape overlap.

cffdisp The OEColorForceFieldDisplay object that stores the depiction information of an OEColorForceField object.

```
OEShapeOueryDisplay(const OEChem:: OEMolBase &refmol,
                    const OEColorForceFieldDisplay &cffdisp,
                    const OEShapeQueryDisplayOptions &opts)
```

Constructs an *OEShapeQueryDisplay* object with given depiction options.

refmol The 3D reference molecule of the shape overlap.

cffdisp The OEColorForceFieldDisplay object that stores the depiction information of an OEColorForceField object.

**opts** The OEShapeQueryDisplayOptions object that defines how the shape query *i.e.* reference molecule is depicted.

#### operator=

OEShapeQueryDisplay & operator=(const OEShapeQueryDisplay & rhs)

Assignment operator.

#### **GetTitle**

std::string GetTitle() const

Returns the title of the molecule the OEShapeQueryDisplay object was initialized.

#### **IsValid**

```
bool IsValid() const
```

Returns whether the OEShapeQueryDisplay object was initialized successfully. If initialization was attempted with either an empty molecule or a molecule without 3D coordinates, then this method returns false.

## 5.1.32 OEShapeQueryDisplayOptions

class OEShapeQueryDisplayOptions : public OEDepict::OE2DMolDisplayOptions

This class represents OEShapeQueryDisplayOptions that encapsulates properties that determine how the reference molecule of a shape overlap is depicted by the OERenderShapeQuery function.

#### See also:

- OEShapeQueryDisplay class
- · OERenderShapeQuery function

#### **Code Example**

• Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

The following methods are publicly inherited from OE2DMolDisplayOptions:

| operator=                    | GetHydrogenStyle          | SetBondLineAtomLabelGapScale |
|------------------------------|---------------------------|------------------------------|
| GetAromaticStyle             | GetMargin                 | SetBondLineGapScale          |
| GetAtomColor                 | GetScale                  | SetBondPropLabelFont         |
| GetAtomColorStyle            | GetSuperAtomLabelFont     | SetBondPropLabelFontScale    |
| GetAtomLabelFont             | GetSuperAtomStyle         | SetBondPropertyFunctor       |
| GetAtomLabelFontScale        | GetTitleFont              | SetBondStereoStyle           |
| GetAtomPropLabelFont         | GetTitleFontScale         | SetBondWidthScaling          |
| GetAtomPropLabelFontScale    | GetTitleHeight            | SetDefaultBondPen            |
| GetAtomPropertyFunctor       | GetTitleLocation          | SetDimensions                |
| GetAtomStereoStyle           | GetWidth                  | SetHeight                    |
| GetBackgroundColor           | SetAromaticStyle          | SetHydrogenStyle             |
| GetBondColorStyle            | SetAtomColor              | SetMargin                    |
| GetBondLineAtomLabelGapScale | SetAtomColorStyle         | SetMargins                   |
| GetBondLineGapScale          | SetAtomLabelFont          | SetScale                     |
| GetBondPropLabelFont         | SetAtomLabelFontScale     | SetSuperAtomLabelFont        |
| GetBondPropLabelFontScale    | SetAtomPropLabelFont      | SetSuperAtomStyle            |
| GetBondPropertyFunctor       | SetAtomPropLabelFontScale | SetTitleFont                 |
| GetBondStereoStyle           | SetAtomPropertyFunctor    | SetTitleFontScale            |
| GetBondWidthScaling          | SetAtomStereoStyle        | SetTitleHeight               |
| GetDefaultBondPen            | SetBackgroundColor        | SetTitleLocation             |
| GetHeight                    | SetBondColorStyle         | SetWidth                     |

#### **Constructors**

OEShapeQueryDisplayOptions()

#### Default constructor.

OEShapeQueryDisplayOptions(const OEShapeQueryDisplayOptions & rhs)

Copy constructors.

#### operator=

OEShapeQueryDisplayOptions & operator=(const OEShapeQueryDisplayOptions & rhs)

Assignment operator.

#### **ClearSurfaceArcFxn**

void ClearSurfaceArcFxn()

Removes the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule.

#### See also:

- · OEShapeQueryDisplayOptions.GetSurfaceArcFxn
- · OEShapeQueryDisplayOptions. SetSurfaceArcFxn

#### **GetClearBackground**

bool GetClearBackground() const

Returns whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the rendering of the shape query.

#### See also:

· OEShapeQueryDisplayOptions.SetClearBackground

#### **GetColorAtomStyle**

unsigned int GetColorAtomStyle() const

Returns the style that is used to define how color atoms are depicted by the OERenderShapeQuery function. The return value is taken from the  $OEColorAtomStyle$  namespace.

#### See also:

- · OEShapeQueryDisplayOptions.SetColorAtomStyle
- OEColorAtomStyle namespace

#### **GetDepictOrientation**

unsigned int GetDepictOrientation() const

Returns the preferred orientation of 2D layout if the shape query. The return value is taken from the OEDepictOrientation namespace.

#### See also:

· OEShapeQueryDisplayOptions. SetDepictOrientation method

#### **GetSurfaceArcFxn**

const OESurfaceArcFxnBase \*GetSurfaceArcFxn() const

Returns the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule.

#### See also:

- · OEShapeQueryDisplayOptions.ClearSurfaceArcFxn
- · OEShapeQueryDisplayOptions. SetSurfaceArcFxn

#### **SetClearBackground**

void SetClearBackground (bool clear)

Sets whether or not the image is cleared (by calling OEImageBase. Clear method) prior to the rendering of the shape query.

#### See also:

· OEShapeQueryDisplayOptions.GetClearBackground

#### **SetColorAtomStyle**

void SetColorAtomStyle (unsigned int style)

Sets the style that defines how color atoms are depicted by the OERenderShapeQuery function.

style This value has to be from the  $OEColorAtomStyle$  namespace.

#### See also:

- · OEShapeQueryDisplayOptions.GetColorAtomStyle
- · OEColorAtomStyle namespace

#### **SetDepictOrientation**

void SetDepictOrientation (unsigned int orientation)

Sets the preferred orientation of 2D layout of the shape query.

orientation This value has to be from the OEDepictOrientation namespace.

Note: Changing the orientation of the layout of the shape query consequently effects the orientation of the shape and color overlaps mapped to the given shape query.

- · OEShapeQueryDisplayOptions.GetDepictOrientation method
- · OEDepictOrientation namespace

#### **SetSurfaceArcFxn**

void SetSurfaceArcFxn (const OESurfaceArcFxnBase &arcfxn)

Sets the surface drawing functor that is drawn to represent the 2D molecule surface of the reference molecule when calling the OERenderShapeQuery function.

#### See also:

- · OEShapeQueryDisplayOptions.ClearSurfaceArcFxn
- · OEShapeQueryDisplayOptions.GetSurfaceArcFxn

## 5.1.33 OESurfaceArc

#### class OESurfaceArc

This class represents OESurfaceArc that stores data for drawing the arcs of molecule surface. See Figure: Example of the data stored in the OESurfaceArc class.

![](_page_134_Figure_10.jpeg)

#### Fig. 36: Example of the data stored in the OESurfaceArc class

Note: Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position,  $90.0^{\circ}$  degree corresponds to 3 o'clock, etc.

- OESurfaceArcFxnBase class
- · OEGet2DSurfaceArcs function

#### **Constructors**

```
OESurfaceArc()
```

Default constructor.

```
OESurfaceArc(const OEDepict:: OE2DAtomDisplay *adisp,
             const OEDepict:: OE2DPoint &center, double bgnAngle, double endAngle,
             double radius)
```

Creates an OESurfaceArc object with the given parameters.

OESurfaceArc(const OESurfaceArc & rhs)

Copy constructor.

#### operator=

OESurfaceArc & operator= (const OESurfaceArc & rhs)

Assignment operator.

#### **GetAtomDisplay**

const OEDepict:: OE2DAtomDisplay \*GetAtomDisplay() const

Returns the pointer of the OE2DAtomDisplay object the given arc belongs to.

#### See also:

• OE2DAtomDisplay class in the OEDepict TK manual

#### **GetBgnAngle**

double GetBgnAngle() const

Returns the angle (in degrees) where the arc of the surface starts.

#### **GetCenter**

const OEDepict:: OE2DPoint & GetCenter () const

Returns the  $(x,y)$  coordinates of the center of the surface arc.

#### See also:

• OE2DPoint class in the OEDepict TK manual

#### **GetEndAngle**

double GetEndAngle() const

Returns the angle (in degrees) where the arc of the surface ends.

#### **GetRadius**

double GetRadius () const

Returns the radius of the arc.

#### **SetAtomDisplay**

**bool** SetAtomDisplay (const OEDepict:: OE2DAtomDisplay \*adisp)

Sets the atom display to which the arc belongs.

#### See also:

• OE2DAtomDisplay class in the OEDepict manual

#### **SetBgnAngle**

bool SetBgnAngle(double angle)

Sets the angle where the arc of the surface begins.

```
angle The angle has to in the range of [0.0^{\circ}, 360.0^{\circ}]
```

#### **SetCenter**

bool SetCenter (const OEDepict:: OE2DPoint & center)

Sets the  $(x,y)$  coordinates of the center of the surface arc.

#### **SetEndAngle**

bool SetEndAngle(double angle)

Sets the angle where the arc of the surface ends.

*angle* The angle has to in the range of  $[0.0^{\circ}, 360.0^{\circ}]$ 

#### **SetRadius**

```
bool SetRadius (double radius)
```

Sets the radius of the arc.

# 5.2 OEGrapheme Basic Arc Drawing Classes

## 5.2.1 OEAlphaRainbowArcFxn

class OEAlphaRainbowArcFxn : public OESurfaceArcFxnBase

This class represents OEAlphaRainbowArcFxn. See example in Figure: Example of drawing molecule surface using OEAlphaRainbowArcFxn.

![](_page_137_Picture_8.jpeg)

Fig. 37: Example of drawing molecule surface using OEAlphaRainbowArcFxn

#### See also:

- · OEDrawAlphaRainbowSurfaceArc function
- · OESetSurfaceArcFxnfunction
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OEAlphaRainbowArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_AlphaRainbow style.

See example in Figure: Example of drawing molecule surface using OEAlphaRainbowArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEAlphaRainbowArcFxn object is dynamically allocated and owned by the caller.

## 5.2.2 OEBrickRoadArcFxn

class OEBrickRoadArcFxn : public OESurfaceArcFxnBase

This class represents OEBrickRoadArcFxn. See example in Figure: Example of drawing molecule surface using OEBrickRoadArcFxn.

#### See also:

- · OEDrawBrickRoadSurfaceArc function
- OESetSurfaceArcFxn function
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

![](_page_139_Picture_1.jpeg)

Fig. 38: Example of drawing molecule surface using OEBrickRoadArcFxn

#### **Constructors**

OEBrickRoadArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_BrickRoad style.

See example in Figure: Example of drawing molecule surface using OEBrickRoadArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEBrickRoadArcFxn object is dynamically allocated and owned by the caller.

## 5.2.3 OECastleArcFxn

class OECastleArcFxn : public OESurfaceArcFxnBase

This class represents OECastleArcFxn. See example in Figure: Example of drawing molecule surface using OE-CastleArcFxn.

![](_page_140_Picture_4.jpeg)

#### Fig. 39: Example of drawing molecule surface using OECastleArcFxn

#### See also:

- · OEDrawCastleSurfaceArcfunction
- · OESetSurfaceArcFxnfunction
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OECastleArcFxn(const OEDepict::OEPen &pen=OEDepict::OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Castle style.

See example in Figure: Example of drawing molecule surface using OECastleArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OECastleArcFxn object is dynamically allocated and owned by the caller.

## 5.2.4 OECogArcFxn

class OECogArcFxn : public OESurfaceArcFxnBase

This class represents OECogArcFxn. See example in Figure: Example of drawing molecule surface using OECogAr $cFxn.$ 

![](_page_141_Picture_15.jpeg)

#### Fig. 40: Example of drawing molecule surface using OECogArcFxn

- · OEDrawCogSurfaceArc function
- · OESetSurfaceArcFxn function

• OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OECogArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Cog style.

See example in Figure: Example of drawing molecule surface using OECogArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OECogArcFxn object is dynamically allocated and owned by the caller.

## 5.2.5 OEComplexSurfaceArcFxnBase

class OEComplexSurfaceArcFxnBase : public OESurfaceArcFxnBase

This class represents OEComplexSurfaceArcFxnBase which is an abstract class that defines the interface used for drawing molecule surfaces. The OEComplexSurfaceArcFxnBase class also stores a depth parameter that reflects the relative distance between the ligand and the receptor when drawing the complex surface.

See also:

Drawing a Ligand-Protein Complex Surface chapter

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

The following classes derive from this class:

- OEDefaultCavityArcFxn
- OEDefaultVoidArcFxn

#### **Constructors**

```
OEComplexSurfaceArcFxnBase()
OEComplexSurfaceArcFxnBase(double depth)
OEComplexSurfaceArcFxnBase(const OEComplexSurfaceArcFxnBase & rhs)
```

Default and copy constructors.

#### operator=

OEComplexSurfaceArcFxnBase &operator=(const OEComplexSurfaceArcFxnBase &rhs)

Assignment operator.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const = 0

It is a virtual const method that is implemented in the concrete derived classes to draw surface arcs.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### **CreateComplexCopy**

OEComplexSurfaceArcFxnBase \*CreateComplexCopy() const

Virtual const constructor which allows copying of concrete derived objects using a reference to the OEComplexSurfaceArcFxnBase base class.

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const = 0

Virtual const constructor which allows copying of concrete derived objects using a reference to the OESurfaceArcFxn-Base base class.

#### **GetDepth**

double GetDepth() const

Returns the *depth* parameter of the surface arc.

#### **SetDepth**

void SetDepth (double depth)

Sets the *depth* parameter of the surface arc.

## 5.2.6 OEDefaultArcFxn

class OEDefaultArcFxn : public OESurfaceArcFxnBase

This class represents OEDefaultArcFxn. See example in Figure: Example of drawing molecule surface using OEDefaultArcFxn.

![](_page_144_Picture_10.jpeg)

#### Fig. 41: Example of drawing molecule surface using OEDefaultArcFxn

#### See also:

- · OEDrawDefaultSurfaceArcfunction
- · OESetSurfaceArcFxn function
- OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

![](_page_144_Picture_17.jpeg)

#### **Constructors**

OEDefaultArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Default style.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDefaultArcFxn object is dynamically allocated and owned by the caller.

## 5.2.7 OEDefaultBuriedArcFxn

```
class OEDefaultBuriedArcFxn : public OESurfaceArcFxnBase
```

This class represents OEDefaultBuriedArcFxn functor that is used to draw the arc segment of the 2D molecule surface, where the ligand and the protein tightly fit in the 3D complex. See example in Figure: Example of drawing an arc using OEDefaultBuriedArcFxn.

![](_page_145_Figure_18.jpeg)

#### Fig. 42: Example of drawing an arc using OEDefaultBuriedArcFxn

- Drawing a Ligand-Protein Complex Surface chapter
- · OEAddComplexSurfaceArcs function
- OEDefaultBuriedArcFxn class
- OEDefaultCavityArcFxn class

• OEDefaultSolventArcFxn class

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OEDefaultBuriedArcFxn()

Default constructor.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &a) const

Draws a surface arc with the OESurfaceArcStyle\_Default style using a black pen.

*image* The image on which the *buried* surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

- · OEAddComplexSurfaceArcs function
- · OEDrawEyelashSurfaceArc function

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDefaultBuriedArcFxn object is dynamically allocated and owned by the caller.

## 5.2.8 OEDefaultCavityArcFxn

```
class OEDefaultCavityArcFxn : public OEComplexSurfaceArcFxnBase
```

This class represents OEDefaultCavityArcFxn functor that is used to draw the arc segment of the 2D molecule surface, where there is a cavity detected between the ligand and the protein in the 3D complex. See example in *Figure: Example* of drawing an arc using OEDefaultCavityArcFxn.

![](_page_146_Figure_21.jpeg)

![](_page_146_Figure_22.jpeg)

#### See also:

- Drawing a Ligand-Protein Complex Surface chapter
- · OEAddComplexSurfaceArcs function
- OEDefaultBuriedArcFxn class
- OEDefaultSolventArcFxn class
- OEDefaultVoidArcFxn class

The following methods are publicly inherited from OEComplexSurfaceArcFxnBase:

| <i>operator=</i>  | CreateComplexCopy | GetDepth |
|-------------------|-------------------|----------|
| <i>operator()</i> | CreateCopy        | SetDepth |

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OEDefaultCavityArcFxn()

Default constructors.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &a) const

Draws a surface arc with the OESurfaceArcStyle\_Cog style using a black pen.

*image* The image on which the *cavity* surface arc is drawn.

arc The object that stores the parameters of the surface arc.

See also:

- · OEAddComplexSurfaceArcs function
- · OEDrawCogSurfaceArc function

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDefaultCavityArcFxn object is dynamically allocated and owned by the caller.

## 5.2.9 OEDefaultSolventArcFxn

class OEDefaultSolventArcFxn : public OESurfaceArcFxnBase

This class represents OEDefaultSolventArcFxn functor that is used to draw the arc segment of the 2D molecule surface, where the ligand is exposed to the solvent in the 3D complex. See example in Figure: Example of drawing an arc using OEDefaultSolventArcFxn.

![](_page_148_Picture_4.jpeg)

#### Fig. 44: Example of drawing an arc using OEDefaultSolventArcFxn

#### See also:

- Drawing a Ligand-Protein Complex Surface chapter
- · OEAddComplexSurfaceArcs function
- OEDefaultBuriedArcFxn class
- OEDefaultCavityArcFxn class
- OEDefaultVoidArcFxn class

The following methods are publicly inherited from OESurfaceArcFxnBase:

 $operator()$ CreateCopy

#### **Constructors**

OEDefaultSolventArcFxn()

Default constructor.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &a) const

Draws a surface arc with the OESurfaceArcStyle\_Default style using a grey pen.

*image* The image on which the *solvent* surface arc is drawn.

arc The object that stores the parameters of the surface arc.

- · OEAddComplexSurfaceArcs function
- · OEDrawDefaultSurfaceArc function

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDefaultSolventArcFxn object is dynamically allocated and owned by the caller.

## 5.2.10 OEDefaultVoidArcFxn

```
class OEDefaultVoidArcFxn : public OEComplexSurfaceArcFxnBase
```

This class represents OEDefaultVoidArcFxn functor that is used to draw the arc segment of the 2D molecule surface, where there is a small gap detected between the ligand and the protein in the 3D complex. See example in *Figure:* Example of drawing an arc using OEDefaultVoidArcFxn.

![](_page_149_Picture_7.jpeg)

#### Fig. 45: Example of drawing an arc using OEDefaultVoidArcFxn

#### See also:

- Drawing a Ligand-Protein Complex Surface chapter
- · OEAddComplexSurfaceArcs function
- OEDefaultBuriedArcFxn class
- OEDefaultCavityArcFxn class
- OEDefaultSolventArcFxn class

The following methods are publicly inherited from OEComplexSurfaceArcFxnBase:

| <i>operator=</i>  | CreateComplexCopy | GetDepth |
|-------------------|-------------------|----------|
| <i>operator()</i> | CreateCopy        | SetDepth |

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

## **Constructors**

OEDefaultVoidArcFxn()

Default constructor.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Eyelash style using a black pen.

image The image on which the void surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

- · OEAddComplexSurfaceArcs function
- · OEDrawEyelashSurfaceArc function

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEDefaultVoidArcFxn object is dynamically allocated and owned by the caller.

## 5.2.11 OEEyelashArcFxn

class OEEyelashArcFxn : public OESurfaceArcFxnBase

This class represents OEEyelashArcFxn. See example in Example of drawing molecule surface using OEEyelashAr $cFxn.$ 

#### See also:

- · OEDrawEyelashSurfaceArc function
- · OESetSurfaceArcFxn function
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

![](_page_151_Picture_1.jpeg)

#### Fig. 46: Example of drawing molecule surface using OEEyelashArcFxn

#### **Constructors**

OEEyelashArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Eyelash style.

See example in Example of drawing molecule surface using OEEyelashArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEEyelashArcFxn object is dynamically allocated and owned by the caller.

## 5.2.12 OEFlowerArcFxn

class OEFlowerArcFxn : public OESurfaceArcFxnBase

This class represents OEFlowerArcFxn. See example in Example of drawing molecule surface using OEFlowerAr $cFxn.$ 

![](_page_152_Picture_4.jpeg)

#### Fig. 47: Example of drawing molecule surface using OEFlowerArcFxn

#### See also:

- OEDrawFlowerSurfaceArcfunction
- · OESetSurfaceArcFxnfunction
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OEFlowerArcFxn(const OEDepict::OEPen &pen=OEDepict::OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Flower style.

See example in *Example of drawing molecule surface using OEFlowerArcFxn*.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEFlowerArcFxn object is dynamically allocated and owned by the caller.

## 5.2.13 OENecklaceArcFxn

class OENecklaceArcFxn : public OESurfaceArcFxnBase

This class represents OENecklaceArcFxn. See example in Example of drawing molecule surface using OENecklaceArcFxn.

![](_page_153_Picture_15.jpeg)

#### Fig. 48: Example of drawing molecule surface using OENecklaceArcFxn

- · OEDrawNecklaceSurfaceArc function
- · OESetSurfaceArcFxn function

• OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OENecklaceArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Necklace style.

See example in Example of drawing molecule surface using OENecklaceArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OENecklaceArcFxn object is dynamically allocated and owned by the caller.

## 5.2.14 OENullArcFxn

class OENullArcFxn : public OESurfaceArcFxnBase

This class represents OENullArcFxn.

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### operator()

```
bool operator () (OEDepict:: OEImageBase &, const OESurfaceArc &) const
```

No-op *i.e.* no surface arc is drawn.

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OENullArcFxn object is dynamically allocated and owned by the caller.

## 5.2.15 OEOliveBranchArcFxn

class OEOliveBranchArcFxn : public OESurfaceArcFxnBase

This class represents OEOliveBranchArcFxn. See example in Example of drawing molecule surface using OEOlive-BranchArcFxn.

![](_page_155_Picture_10.jpeg)

#### Fig. 49: Example of drawing molecule surface using OEOliveBranchArcFxn

#### See also:

- · OEDrawOliveBranchSurfaceArcfunction
- · OESetSurfaceArcFxn function
- OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OEOliveBranchArcFxn(const OEDepict::OEPen &pen=OEDepict::OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_OliveBranch style.

See example in Example of drawing molecule surface using OEOliveBranchArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEOliveBranchArcFxn object is dynamically allocated and owned by the caller.

## 5.2.16 OEPearlsArcFxn

class OEPearlsArcFxn : public OESurfaceArcFxnBase

This class represents OEPearlsArcFxn. See example in Example of drawing molecule surface using OEPearlsArcFxn.

See also:

- OEDrawPearlsSurfaceArcfunction
- · OESetSurfaceArcFxn function
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

![](_page_156_Picture_24.jpeg)

![](_page_157_Picture_1.jpeg)

#### Fig. 50: Example of drawing molecule surface using OEPearlsArcFxn

#### **Constructors**

OEPearlsArcFxn(const OEDepict::OEPen &pen=OEDepict::OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Pearls style.

See example in Example of drawing molecule surface using OEPearlsArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEPearlsArcFxn object is dynamically allocated and owned by the caller.

## 5.2.17 OERaceTrackArcFxn

class OERaceTrackArcFxn : public OESurfaceArcFxnBase

This class represents OERaceTrackArcFxn. See example in Example of drawing molecule surface using OERace-TrackArcFxn.

![](_page_158_Picture_4.jpeg)

#### Fig. 51: Example of drawing molecule surface using OERaceTrackArcFxn

#### See also:

- OEDrawRaceTrackSurfaceArcfunction
- · OESetSurfaceArcFxnfunction
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OERaceTrackArcFxn(const OEDepict:: OEPen & pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_RaceTrack style.

See example in Example of drawing molecule surface using OERaceTrackArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OERaceTrackArcFxn object is dynamically allocated and owned by the caller.

## 5.2.18 OERailroadTrackArcFxn

class OERailroadTrackArcFxn : public OESurfaceArcFxnBase

This class represents OERailroadTrackArcFxn. See example in Example of drawing molecule surface using OERailroadTrackArcFxn.

![](_page_159_Picture_15.jpeg)

#### Fig. 52: Example of drawing molecule surface using OERailroadTrackArcFxn

- · OEDrawRailroadTrackSurfaceArcfunction
- · OESetSurfaceArcFxn function

• OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OERailroadTrackArcFxn(const OEDepict::OEPen &pen=OEDepict::OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_RailroadTrack style.

See example in Example of drawing molecule surface using OERailroadTrackArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OERailroadTrackArcFxn object is dynamically allocated and owned by the caller.

## 5.2.19 OESawArcFxn

class OESawArcFxn : public OESurfaceArcFxnBase

This class represents OESawArcFxn. See example in Example of drawing molecule surface using OESawArcFxn.

#### See also:

- · OEDrawSawSurfaceArc function
- · OESetSurfaceArcFxnfunction
- OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

![](_page_161_Picture_1.jpeg)

#### Fig. 53: Example of drawing molecule surface using OESawArcFxn

#### **Constructors**

OESawArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Saw style.

See example in Example of drawing molecule surface using OESawArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OESawArcFxn object is dynamically allocated and owned by the caller.

## 5.2.20 OESimpsonArcFxn

class OESimpsonArcFxn : public OESurfaceArcFxnBase

This class represents OESimpsonArcFxn. See example in Example of drawing molecule surface using OESimpsonAr $cFxn$ .

![](_page_162_Figure_4.jpeg)

#### Fig. 54: Example of drawing molecule surface using OESimpsonArcFxn

#### See also:

- · OEDrawSimpsonSurfaceArc function
- · OESetSurfaceArcFxnfunction
- · OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OESimpsonArcFxn(const OEDepict::OEPen &pen=OEDepict::OEBlackPen)

Default constructor.

pen The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Simpson style.

See example in Example of drawing molecule surface using OESimpsonArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OESimpsonArcFxn object is dynamically allocated and owned by the caller.

## 5.2.21 OEStitchArcFxn

class OEStitchArcFxn : public OESurfaceArcFxnBase

This class represents OEStitchArcFxn. See example in Example of drawing molecule surface using OEStitchArcFxn.

![](_page_163_Figure_15.jpeg)

#### Fig. 55: Example of drawing molecule surface using OEStitchArcFxn

- · OEDrawStitchSurfaceArcfunction
- OESetSurfaceArcFxnfunction
- OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

#### **Constructors**

OEStitchArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Stitch style.

See example in Example of drawing molecule surface using OEStitchArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEStitchArcFxn object is dynamically allocated and owned by the caller.

## 5.2.22 OESunArcFxn

class OESunArcFxn : public OESurfaceArcFxnBase

This class represents OESunArcFxn. See example in Example of drawing molecule surface using OESunArcFxn.

See also:

- · OEDrawSunSurfaceArc function
- · OESetSurfaceArcFxn function
- OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

![](_page_165_Picture_1.jpeg)

#### Fig. 56: Example of drawing molecule surface using OESunArcFxn

#### **Constructors**

OESunArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Sun style.

See example in Example of drawing molecule surface using OESunArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OESunArcFxn object is dynamically allocated and owned by the caller.

## 5.2.23 OESurfaceArcFxnBase

#### class OESurfaceArcFxnBase

This class represents OESurfaceArcFxnBase which is an abstract class that defines the interface used for drawing molecule surfaces.

### The following classes derive from this class:

- OEAlphaRainbowArcFxn
- OEBrickRoadArcFxn
- $\bullet$  OECastleArcFxn
- $\bullet$  OECogArcFxn
- OEDefaultArcFxn
- OEEyelashArcFxn
- OEFlowerArcFxn
- OENecklaceArcFxn
- $\bullet$  OENullArcFxn
- $\bullet$  OEOliveBranchArcFxn
- $\bullet$  OEPearlsArcFxn
- $\bullet$  OERaceTrackArcFxn
- OERailroadTrackArcFxn
- OESawArcFxn
- OESimpsonArcFxn
- OEStitchArcFxn
- OESunArcFxn
- $\bullet$  OEWreathArcFxn

#### operator()

**bool operator** () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const = 0

It is a virtual const method that is implemented in the concrete derived classes to draw surface arcs.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

See also:

• OESurfaceArc class

## **CreateCopy**

```
OESurfaceArcFxnBase *CreateCopy() const =0
```

Virtual const constructor which allows copying of concrete derived objects using a reference to this base class.

## 5.2.24 OEWreathArcFxn

class OEWreathArcFxn : public OESurfaceArcFxnBase

This class represents OEWreathArcFxn. See example in Example of drawing molecule surface using OEWreathAr $cFxn$ .

![](_page_167_Picture_7.jpeg)

Fig. 57: Example of drawing molecule surface using OEWreathArcFxn

#### See also:

- · OEDrawWreathSurfaceArcfunction
- · OESetSurfaceArcFxn function
- OEDraw2DSurface function

The following methods are publicly inherited from OESurfaceArcFxnBase:

operator() CreateCopy

## **Constructors**

OEWreathArcFxn(const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)

Default constructor.

*pen* The graphical properties of the arc.

#### operator()

bool operator () (OEDepict:: OEImageBase &image, const OESurfaceArc &arc) const

Draws a surface arc with the OESurfaceArcStyle\_Wreath style.

See example in Example of drawing molecule surface using OEWreathArcFxn.

*image* The image on which the surface arc is drawn.

arc The object that stores the parameters of the surface arc.

#### See also:

• OESurfaceArc class

#### **CreateCopy**

OESurfaceArcFxnBase \*CreateCopy() const

Deep copy constructor that returns a copy of the object. The memory for the returned OEWreathArcFxn object is dynamically allocated and owned by the caller.

# **5.3 OEGrapheme Constants**

## 5.3.1 OE2DPropMapSetup

This namespace encodes symbolic constants used as bit-masks to indicate which property map parameters are being created when invoking the OEConfigure2DPropMap function.

#### All

#### The combination of following constants:

- · OE2DPropMapSetup\_Legend
- · OE2DPropMapSetup\_MaxValue
- · OE2DPropMapSetup\_MinValue
- · OE2DPropMapSetup\_NegativeColor
- · OE2DPropMapSetup\_PositiveColor
- · OE2DPropMapSetup\_RadiusRatio
- · OE2DPropMapSetup\_Resolution

#### **Legend**

Passing this constant to the OEConfigure 2DPropMap function results in generating the following default interface to configure the location of the legend.

```
Contents of parameter -legend
   Aliases : -1
   Type : string
   Allow list : false
   Default : Bottom
   Simple : true
   Required : false
   Legal values : Hidden Top Bottom Left Right
   Brief : Location of the legend
   Detail
```

See also:

- · OELegendLocation namespace
- OE2DPropMap. SetLegendLocation method

#### **MaxValue**

Passing this constant to the OEConfigure2DPropMap function results in generating the following default interface to configure the maximum value of the property map.

```
Contents of parameter -maxvalue
   Aliases : - maxv
   Type : float
   Allow list : false
   Default : (parameter does not have a default)
   Simple : true
   Required : false
   Brief : Maximum property limit
```

#### See also:

• OE2DPropMap. SetMaxValue method

#### **MinValue**

Passing this constant to the OEConfigure2DPropMap function results in generating the following default interface to configure the minimum value of the property map.

```
Contents of parameter -minvalue
   Aliases : - minv
   Type : float
   Allow list : false
   Default : (parameter does not have a default)
   Simple : true
   Required : false
   Brief : Minimum property limit
```

See also:

• OE2DPropMap. SetMinValue method

#### **NegativeColor**

Passing this constant to the OEConfigure 2DPropMap function results in generating the following default interface to configure the color used to represent negative values in the property map.

```
Contents of parameter -negcolor
   Aliases : - nego
   Type : string
   Allow list : false
   Default : red
   Simple : true
   Required : false
   Legal values : black blue bluetint brown cyan darkblue darkbrown
   darkcyan darkgreen darkgrey darkmagenta darkorange darkpurple darkred
   darkrose darksalmon darkyellow gold green greenblue greentint grey
   hotpink lightblue lightbrown lightgreen lightgrey lightorange
   lightpurple lightsalmon limegreen magenta mediumblue mediumbrown
   mediumgreen mediumorange mediumpurple mediumsalmon mediumyellow
   olivebrown olivegreen olivegrey orange pink pinktint purple red
   redorange royalblue seagreen skyblue violet white yellow yellowtint
   Brief : Color of the negative values
```

See also:

• OE2DPropMap. SetNegativeColor method

#### **PositiveColor**

Passing this constant to the OEConfigure2DPropMap function results in generating the following default interface to configure the color used to represent positive values in the property map.

```
Contents of parameter -poscolor
   Aliases : - posc
   Type : string
   Allow list : false
   Default : blue
   Simple : true
   Required : false
   Legal values : black blue bluetint brown cyan darkblue darkbrown
   darkcyan darkgreen darkgrey darkmagenta darkorange darkpurple darkred
   darkrose darksalmon darkyellow gold green greenblue greentint grey
   hotpink lightblue lightbrown lightgreen lightgrey lightorange
   lightpurple lightsalmon limegreen magenta mediumblue mediumbrown
   mediumgreen mediumorange mediumpurple mediumsalmon mediumyellow
   olivebrown olivegreen olivegrey orange pink pinktint purple red
    redorange royalblue seagreen skyblue violet white yellow yellowtint
   Brief : Color of the positive values
```

· OE2DPropMap. SetPositiveColor method

## **RadiusRatio**

Passing this constant to the OEConfigure2DPropMap function results in generating the following default interface to configure the Gaussian radius of the property map.

```
Contents of parameter -radiusratio
   Aliases : -rad
   Type : float
   Allow list : false
   Default : 1.0
   Simple : true
   Required : false
   Legal ranges :
       2.0 to 0.5Brief : Ratio to scale the gaussian radius
```

See also:

· OE2DPropMap. SetRadiusRatio method

#### **Resolution**

Passing this constant to the OEConfigure2DPropMap function results in generating the following default interface to configure the resolution of the property map.

```
Contents of parameter -resolution
   Aliases : -res
   Type : int
   Allow list : false
   Default : 2
   Simple : true
   Required : false
   Legal ranges :
       20 to 2Brief : Resolution of the property map
```

See also:

· OE2DPropMap. SetResolution method

## 5.3.2 OEActiveSiteRenderStyle

This namespace contains constants representing various active site representation styles.

#### See also:

· OERenderActiveSiteMaps function

## **Default**

The label style is OEActiveSiteRenderStyle\_InteractionMap.

#### **BFactorMap**

![](_page_172_Figure_4.jpeg)

#### See also:

- · OERenderBFactorMap function
- · OEDrawBFactorMapLegend function

#### **Code Example**

• Visualizing Protein-Ligand B-Factor Map OpenEye Python Cookbook recipe

#### **ContactMap**

There is no image available for the PDF version of this book.

## See also:

· OERenderContactMap function

#### **Code Example**

• Visualizing Protein-Ligand Contacts OpenEye Python Cookbook recipe

#### **InteractionMap**

![](_page_173_Figure_8.jpeg)

![](_page_173_Figure_9.jpeg)

- · OERenderActiveSite function
- · OEDrawActiveSiteLegend function
- Depicting Active Site Interactions example

#### **Code Example**

• Visualizing Protein-Ligand Interactions OpenEye Python Cookbook recipe

#### **UnpairedMap**

# Legend

![](_page_174_Figure_5.jpeg)

#### See also:

- · OERenderUnpairedInteractionMap function
- · OEDrawUnpairedInteractionMapLegend function

#### **Code Example**

• Visualizing Protein-Ligand Unpaired Interactions OpenEye Python Cookbook recipe

## 5.3.3 OECircleStyle

This namespace contains constants representing various circle styles.

#### See also:

· OEDrawCircle function

The  $OECircleStyle$  namespace contains the following constants:

#### **AlphaRainbow**

See Figure: Example of a circle drawn with the 'AlphaRainbow' style.

![](_page_175_Picture_8.jpeg)

#### Fig. 58: Example of a circle drawn with the 'AlphaRainbow' style

See also:

· OEDrawAlphaRainbowCircle function

#### **BrickRoad**

See Figure: Example of a circle drawn with the 'BrickRoad' style.

![](_page_175_Picture_14.jpeg)

Fig. 59: Example of a circle drawn with the 'BrickRoad' style

#### See also:

· OEDrawBrickRoadCirclefunction

## **Castle**

See Figure: Example of a circle drawn with the 'Castle' style.

![](_page_176_Figure_3.jpeg)

#### Fig. 60: Example of a circle drawn with the 'Castle' style

#### See also:

· OEDrawCastleCirclefunction

## Cog

See Figure: Example of a circle drawn with the 'Cog' style.

![](_page_176_Picture_9.jpeg)

Fig. 61: Example of a circle drawn with the 'Cog' style

#### See also:

· OEDrawCogCircle function

## **Default**

See Figure: Example of a circle drawn with the 'Default' style.

![](_page_176_Figure_15.jpeg)

## Fig. 62: Example of a circle drawn with the 'Default' style

#### See also:

· OEDrawDefaultCirclefunction

#### **Eyelash**

See Figure: Example of a circle drawn with the 'Eyelash' style.

![](_page_177_Figure_3.jpeg)

#### Fig. 63: Example of a circle drawn with the 'Eyelash' style

#### See also:

· OEDrawEyelashCirclefunction

#### **Flower**

See Figure: Example of a circle drawn with the 'Flower' style.

![](_page_177_Figure_9.jpeg)

Fig. 64: Example of a circle drawn with the 'Flower' style

#### See also:

· OEDrawFlowerCirclefunction

#### **GreekKey**

See Figure: Example of a circle drawn with the 'GreekKey' style.

![](_page_177_Picture_15.jpeg)

#### Fig. 65: Example of a circle drawn with the 'GreekKey' style

#### See also:

· OEDrawGreekKeyCircle function

#### **Necklace**

See Figure: Example of a circle drawn with the 'Necklace' style.

![](_page_178_Figure_3.jpeg)

#### Fig. 66: Example of a circle drawn with the 'Necklace' style

#### See also:

· OEDrawNecklaceCirclefunction

## **OliveBranch**

See Figure: Example of a circle drawn with the 'OliveBranch' style.

![](_page_178_Picture_9.jpeg)

## Fig. 67: Example of a circle drawn with the 'OliveBranch' style

#### See also:

· OEDrawOliveBranchCircle function

#### **Pearls**

See Figure: Example of a circle drawn with the 'Pearls' style.

![](_page_178_Picture_15.jpeg)

## Fig. 68: Example of a circle drawn with the 'Pearls' style

#### See also:

· OEDrawPearlsCirclefunction

#### **RaceTrack**

See Figure: Example of a circle drawn with the 'RaceTrack' style.

![](_page_179_Figure_3.jpeg)

#### Fig. 69: Example of a circle drawn with the 'RaceTrack' style

See also:

· OEDrawRaceTrackCirclefunction

#### **RailroadTrack**

See Figure: Example of a circle drawn with the 'RailroadTrack' style.

![](_page_179_Picture_9.jpeg)

Fig. 70: Example of a circle drawn with the 'RailroadTrack' style

#### See also:

· OEDrawRailroadTrackCirclefunction

#### **Saw**

See Figure: Example of a circle drawn with the 'Saw' style.

![](_page_179_Picture_15.jpeg)

Fig. 71: Example of a circle drawn with the 'Saw' style

See also:

· OEDrawSawCircle function

#### **Simpson**

See Figure: Example of a circle drawn with the 'Simpson' style.

![](_page_180_Figure_3.jpeg)

#### Fig. 72: Example of a circle drawn with the 'Simpson' style

#### See also:

· OEDrawSimpsonCirclefunction

## **Stitch**

See Figure: Example of a circle drawn with the 'Stitch' style.

![](_page_180_Picture_9.jpeg)

Fig. 73: Example of a circle drawn with the 'Stitch' style

#### See also:

· OEDrawStitchCirclefunction

#### Sun

See Figure: Example of a circle drawn with the 'Sun' style.

![](_page_180_Picture_15.jpeg)

Fig. 74: Example of a circle drawn with the 'Sun' style

See also:

· OEDrawSunCircle function

#### **Wreath**

See Figure: Example of a circle drawn with the 'Wreath' style.

![](_page_181_Picture_3.jpeg)

#### Fig. 75: Example of a circle drawn with the 'Wreath' style

See also:

· OEDrawWreathCirclefunction

## 5.3.4 OEColorAtomStyle

This namespace contains constants representing various styles color atoms can be depicted by the OERenderShapeQuery function.

#### **Default**

The default color atom style is OEColorAtomStyle\_Circle.

#### **Hidden**

No color atoms are depicted.

#### **Circle**

Each color atom is represented by a circle on the query (*i.e.* reference) molecule. If more than one color atom occupies the same space in 3D, the color atoms are represented by half, third, etc circles accordingly. See image in Figure: Example of visualizing color atoms by circles. The color of each circle is defined by the OEColorForceFieldDisplay object.

## 5.3.5 OELegendLocation

This namespace contains constants representing the position of the legend displayed with the property map:

#### See also:

- · OE2DPropMap.GetLegendLocation method
- · OE2DPropMap. SetLegendLocation method

The OELegendLocation namespace contains the following constants:

![](_page_182_Figure_1.jpeg)

Fig. 76: Example of visualizing color atoms by circles

## **Default**

The default legend location is OELegendLocation\_Bottom.

#### **Bottom**

See example in Figure: Example of property map with its legend located at the bottom.

![](_page_182_Figure_7.jpeg)

![](_page_182_Figure_8.jpeg)

#### **Hidden**

See example in Figure: Example of property map with no legend.

![](_page_183_Picture_3.jpeg)

## Fig. 78: Example of property map with no legend

#### Left

See example in Figure: Example of property map with its legend located on the left.

![](_page_183_Figure_7.jpeg)

Fig. 79: Example of property map with the legend located on the left

## **Right**

See example in Figure: Example of property map with its legend located on the right.

![](_page_184_Figure_3.jpeg)

## Fig. 80: Example of property map with the legend located on the right

## **Top**

See example in Figure: Example of property map with its legend located at the top

![](_page_184_Figure_7.jpeg)

Fig. 81: Example of property map with the legend located at the top

## 5.3.6 OEPatternDirection

The OEPatternDirection namespace is used to customize various circle and arc drawing functions.

#### See also:

- · OEDrawBrickRoadCirclefunction
- · OEDrawEyelashCirclefunction
- · OEDrawBrickRoadSurfaceArcfunction
- · OEDrawEyelashSurfaceArc function

The OEPatternDirection namespace contains the following constants:

#### **Default**

The default pattern direction is OEPatternDirection\_Outside.

#### **Inside**

See example in Figure: Example of circle and arc drawing with patterns 'inside'.

![](_page_185_Figure_13.jpeg)

Fig. 82: Example of circle and arc drawing with patterns 'inside'

#### **Outside**

See example in Figure: Example of circle and arc drawing with patterns 'outside'.

![](_page_185_Figure_17.jpeg)

Fig. 83: Example of circle and arc drawing with patterns 'outside'

## 5.3.7 OEPeptideLabelStyle

This namespace contains constants representing various label styles for peptide depiction.

#### See also:

- · OEPeptideDisplayOptions.GetLabelStylemethod
- · OEPeptideDisplayOptions. SetLabelStyle method
- · OEDrawPeptide function

#### **Code Example**

• Depicting Peptides OpenEye Python Cookbook recipe

#### **Default**

The label style is OEPeptideLabelStyle\_ThreeLetters.

## **SingleLetter**

See example in Figure: Example of peptide depiction with 'SingleLetter' label style.

**Dxytocin** 

![](_page_186_Figure_14.jpeg)

Fig. 84: Example of peptide depiction with 'SingleLetter' label style

## **ThreeLetters**

See example in Figure: Example of peptide depiction with 'ThreeLetters' label style.

![](_page_187_Figure_3.jpeg)

![](_page_187_Figure_4.jpeg)

#### Fig. 85: Example of peptide depiction with 'ThreeLetters' label style

## 5.3.8 OEPlotMarkerStyle

This namespace contains constants representing various plot marker styles.

#### See also:

• OEPlotMarker class

The OEPlotMarkerStyle namespace contains the following constants:

This namespace contains constants.

#### **Default**

The default marker style is OEPlotMarkerStyle\_Circle.

#### **Circle**

#### **Square**

## 5.3.9 OEShapeOverlapDisplayStyle

This namespace contains constants representing various styles that can be used to depict shape overlays when calling the OERenderShapeQuery function.

#### See also:

· OEShapeOverlapDisplayOptions.SetOverlapDisplayStylemethod

#### **Default**

The default shape overlap display style is OEShapeOverlapDisplayStyle\_PropertyMap.

#### **PropertyCloud**

![](_page_188_Picture_9.jpeg)

#### Fig. 86: Example of visualizing shape overlaps with PropertyCloud style

## PropertyMap

## 5.3.10 OESurfaceArcScale

This namespace contains constants that determine the range of the radius scaling factor that can be used to generate the arcs of 2D molecule surfaces.

- · OEGet2DSurfaceArcs function
- · OEGetMoleculeSurfaceScale function

![](_page_189_Picture_1.jpeg)

Fig. 87: Example of visualizing shape overlaps with PropertyMap style

![](_page_189_Figure_3.jpeg)

Fig. 88: Example of various radius scales used to generate arcs

#### **Default**

Specifies the default radius scaling used to generate the arcs of the molecule surface when calling the OEGet2DSurfaceArcs function.

#### **Maximum**

Specifies the maximum radius scaling that can be used to generate the arcs of the molecule surface of a specific atom when calling the OEGet2DSurfaceArcs function.

#### **Minimum**

Specifies the minimum radius scaling that can be used to generate the arcs of the molecule surface of a specific atom when calling the OEGet2DSurfaceArcs function.

## 5.3.11 OESurfaceArcStyle

This namespace contains constants representing various arc styles.

#### See also:

· OEDrawSurfaceArc function

The OESurfaceArcStyle namespace contains the following constants:

#### **AlphaRainbow**

See Figure: Example of an arc drawn with the 'AlphaRainbow' style.

![](_page_190_Picture_12.jpeg)

#### Fig. 89: Example of an arc drawn with the 'AlphaRainbow' style

#### See also:

· OEDrawAlphaRainbowSurfaceArcfunction

#### **BrickRoad**

See Figure: Example of an arc drawn with the 'BrickRoad' style.

![](_page_190_Picture_18.jpeg)

Fig. 90: Example of an arc drawn with the 'BrickRoad' style

· OEDrawBrickRoadSurfaceArcfunction

#### **Castle**

See Figure: Example of an arc drawn with the 'Castle' style.

![](_page_191_Picture_4.jpeg)

#### Fig. 91: Example of an arc drawn with the 'Castle' style

#### See also:

· OEDrawCastleSurfaceArcfunction

#### Cog

See Figure: Example of an arc drawn with the 'Cog' style.

![](_page_191_Picture_10.jpeg)

Fig. 92: Example of an arc drawn with the 'Cog' style

#### See also:

· OEDrawCogSurfaceArc function

#### **Default**

See Figure: Example of an arc drawn with the 'Default' style.

![](_page_191_Figure_16.jpeg)

Fig. 93: Example of an arc drawn with the 'Default' style

· OEDrawDefaultSurfaceArcfunction

#### **Eyelash**

See Figure: Example of an arc drawn with the 'Eyelash' style.

![](_page_192_Figure_4.jpeg)

#### Fig. 94: Example of an arc drawn with the 'Eyelash' style

#### See also:

· OEDrawEyelashSurfaceArc function

#### **Flower**

See Figure: Example of an arc drawn with the 'Flower' style.

![](_page_192_Picture_10.jpeg)

Fig. 95: Example of an arc drawn with the 'Flower' style

#### See also:

· OEDrawFlowerSurfaceArc function

#### **Necklace**

See Figure: Example of an arc drawn with the 'Necklace' style.

![](_page_192_Figure_16.jpeg)

Fig. 96: Example of an arc drawn with the 'Necklace' style

· OEDrawNecklaceSurfaceArcfunction

#### **OliveBranch**

See Figure: Example of an arc drawn with the 'OliveBranch' style.

![](_page_193_Picture_4.jpeg)

#### Fig. 97: Example of an arc drawn with the 'OliveBranch' style

#### See also:

· OEDrawOliveBranchSurfaceArcfunction

#### **Pearls**

See Figure: Example of an arc drawn with the 'Pearls' style.

![](_page_193_Picture_10.jpeg)

Fig. 98: Example of an arc drawn with the 'Pearls' style

#### See also:

· OEDrawPearlsSurfaceArcfunction

#### **RaceTrack**

See Figure: Example of an arc drawn with the 'RaceTrack' style.

![](_page_193_Figure_16.jpeg)

Fig. 99: Example of an arc drawn with the 'RaceTrack' style

· OEDrawRaceTrackSurfaceArc function

#### **RailroadTrack**

See Figure: Example of an arc drawn with the 'RailroadTrack' style.

![](_page_194_Picture_4.jpeg)

#### Fig. 100: Example of an arc drawn with the 'RailroadTrack' style

#### See also:

· OEDrawRailroadTrackSurfaceArcfunction

#### **Saw**

See Figure: Example of an arc drawn with the 'Saw' style.

![](_page_194_Picture_10.jpeg)

Fig. 101: Example of an arc drawn with the 'Saw' style

#### See also:

· OEDrawSawSurfaceArc function

#### **Simpson**

See Figure: Example of an arc drawn with the 'Simpson' style.

![](_page_194_Picture_16.jpeg)

Fig. 102: Example of an arc drawn with the 'Simpson' style

· OEDrawSimpsonSurfaceArc function

#### **Stitch**

See Figure: Example of an arc drawn with the 'Stitch' style.

![](_page_195_Picture_4.jpeg)

#### Fig. 103: Example of an arc drawn with the 'Stitch' style

#### See also:

· OEDrawStitchSurfaceArcfunction

#### Sun

See Figure: Example of an arc drawn with the 'Sun' style.

![](_page_195_Picture_10.jpeg)

Fig. 104: Example of an arc drawn with the 'Sun' style

#### See also:

· OEDrawSunSurfaceArc function

#### Wreath

See Figure: Example of an arc drawn with the 'Wreath' style.

![](_page_195_Picture_16.jpeg)

Fig. 105: Example of an arc drawn with the 'Wreath' style

#### See also:

· OEDrawWreathSurfaceArc function

# **5.4 OEGrapheme Functions**

## 5.4.1 OEAddComplexSurfaceArcs

```
bool OEAddComplexSurfaceArcs (OEChem:: OEMolBase &ligand,
                  const OEChem:: OEMolBase &protein,
                  const OESurfaceArcFxnBase &
\rightarrowsolventExposedFxn=OEDefaultSolventArcFxn(),
                  const OESurfaceArcFxnBase &buriedFxn=OEDefaultBuriedArcFxn(),
                  const OEComplexSurfaceArcFxnBase &cavityFxn=OEDefaultCavityArcFxn(),
                  const OEComplexSurfaceArcFxnBase &voidFxn=OEDefaultVoidArcFxn())
```

Takes a ligand-protein complex and generates the 2D molecule surface of the ligand, where the arcs of the surface are annotated based on the distance calculated between the accessible surface of the ligand and the protein. See Figure: Example of surface drawing with the OEAddComplexSurfaceArcs function.

*ligand* The molecule for which the 2D surface is generated.

*protein* The macromolecule whose contact with the ligand influences the surface drawing.

- solventExposedFxn This functor is used to draw those arc segments of the 2D molecule surface where the ligand is exposed to the solvent in the 3D complex. By default, the OEDefaultSolventArcFxn functor is used.
- **buriedFxn** This functor is used to draw those arc segments of the 2D molecule surface where the ligand and the protein tightly fit in the 3D complex. By default, the *OEDefaultBuriedArcFxn* functor is used.
- cavity Fxn This functor is used to draw those arc segments of the 2D molecule surface where there is a cavity detected between the ligand and the protein in the 3D complex. By default, the OEDefaultCavityArcFxn functor is used.
- *voidFxn* This functor is used to draw those arc segments of the 2D molecule surface where there is a small gap detected between the ligand and the protein in the 3D complex. By default, the OEDefaultVoidArcFxn functor is used.

#### See also:

• Drawing a Ligand-Protein Complex Surface chapter

## 5.4.2 OEAddGlyph

```
void OEAddGlyph (OEDepict:: OE2DMolDisplay &disp,
                const OEAtomGlyphBase &atomglyph,
                const OEChem:: OEMatchBase &match)
void OEAddGlyph (OEDepict:: OE2DMolDisplay &disp,
                const OEAtomGlyphBase &atomglyph,
                const OEChem:: OEAtomBondSet &abset)
void OEAddGlyph (OEDepict:: OE2DMolDisplay &disp,
                const OEAtomGlyphBase &atomglyph,
                const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase> &pred)
```

Annotates atoms with the style implemented in the given OEAtomGlyphBase object. The atoms being annotated can be specified either by an OEMatchBase or an OEAtomBondSet object or by an atom predicate.

disp The OE2DMolDisplay object whose atoms are being annotated.

**atomglyph** Specifies the style of the annotation. Each atom is being annotated by calling the OEAt omGlyphBase. RenderGlyph method.

# Trimethoprim NΗ, $NH<sub>2</sub>$

Fig. 106: Example of surface drawing with the OEAddComplexSurfaceArcs function

match OEAddGlyph function annotates the target atoms of the OEMatchBase object.

**abset** OEAddGlyph function annotates the atoms returned by the GetAtoms method.

 $pred$   $OEAddGlyph$  function annotates only atoms for which the given atom predicate returns *true*.

- Annotating Atoms and Bonds chapter
- OEAtomGlyphBase class
- OEAtomGlyphCircle class

```
void OEAddGlyph (OEDepict:: OE2DMolDisplay &disp,
                const OEBondGlyphBase &bondglyph,
                const OEChem:: OEMatchBase &match)
void OEAddGlyph (OEDepict:: OE2DMolDisplay &disp,
                const OEBondGlyphBase &bondglyph,
                const OEChem:: OEAtomBondSet &abset)
void OEAddGlyph (OEDepict:: OE2DMolDisplay &disp,
                const OEBondGlyphBase &bondglyph,
                const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase> &pred)
```

Annotates bonds with the style implemented in the given OEBondGlyphBase object. The bond being annotated can be specified either by an OEMatchBase or an OEAtomBondSet object or by a bond predicate.

disp The OE2DMolDisplay object whose bonds are being annotated.

- **bondglyph** Specifies the style of the annotation. Each bond is being annotated by calling the OEBondGlyphBase. RenderGlyph method.
- match OEAddG1yph function annotates the target bonds of the OEMatchBase object.

**abset** OEAddGlyph function annotates the bonds returned by the GetBonds method.

 $pred$   $OEAddGlyph$  function annotates only bonds for which the given bond predicate returns true.

See also:

- Annotating Atoms and Bonds chapter
- OEBondGlyphBase class
- OEBondGlyphArrow
- OEBondGlyphCircle
- OEBondGlyphCross class
- OEBondGlyphCurvedArrow class
- OEBondGlyphScissors class

## 5.4.3 OEAddLigandHighlighting

Highlights atoms and/or bonds of the displayed ligand.

#### Table 4: The overloaded versions of the OEAddLigandHighlighting function

| Link                                                          | Description                                                       |
|---------------------------------------------------------------|-------------------------------------------------------------------|
| OEAddLigandHighlighting(disp, highlight, atompred)            | highlights ligand atoms with OEHighlightBase                      |
| OEAddLigandHighlighting(adisp, highlight, bondpred)           | highlights ligand bonds with OEHighlightBase                      |
| OEAddLigandHighlighting(adisp, highlight, atompred, bondpred) | highlights ligand atoms and bonds with OEHighlightBase            |
| OEAddLigandHighlighting(adisp, highlight, match)              | highlights ligand atoms and bonds of a match with OEHighlightBase |
| OEAddLigandHighlighting(adisp, highlight, abset)              | highlights ligand atoms and bonds of a set with OEHighlightBase   |

#### **Parameters:**

adisp The OE2DActiveSiteDisplay object of which ligand atoms add/or ligand bonds being highlighted.

highlight The OEHighlightBase object that specifies the style of the highlighting.

- atompred OEAddLigandHighlighting function highlights only ligand atoms for which the given atom predicate returns true.
- bondpred OEAddLigandHighlighting function highlights only ligand bonds for which the given bond predicate returns true.
- **match** OEAddLigandHighlighting function highlights the target atoms and bonds of the OEMatchBase object.

*abset* Stores the ligand atoms and bonds being highlighted.

#### See also:

- OEHighlightByColor class
- OEHighlightByCogwheel class
- OEHighlightByBallAndStick class
- OEHighlightByStick class
- OEHighlightByLasso class
- 1. Highlighting using atom and bond predicates:

```
void OEAddLigandHighlighting (OE2DActiveSiteDisplay &adisp, const
→OEDepict::OEHighlightBase &highlight,
                             const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>
→&atompred)
```

Highlights ligand atoms with the style implemented in the given OEHighlightBase object. The atoms being highlighted are specified by given atom predicate.

```
void OEAddLigandHighlighting (OE2DActiveSiteDisplay &adisp, const
→OEDepict::OEHighlightBase &highlight,
                               const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase>
\leftrightarrow & bondpred)
```

Highlights ligand bonds with the style implemented in the given OEHighlightBase object. The bonds being highlighted are specified by given bond predicates.

```
void OEAddLigandHighlighting (OE2DActiveSiteDisplay &adisp, const
→OEDepict::OEHighlightBase &highlight,
                                 const OESystem:: OEUnaryPredicate<OEChem:: OEAtomBase>...
\leftrightarrow & atompred,
                                 const OESystem:: OEUnaryPredicate<OEChem:: OEBondBase>...
\rightarrow & bondpred)
```

Highlights ligand atoms and bonds with the style implemented in the given OEHighlightBase object. The atoms and bonds being highlighted are specified by given atom and bond predicates, respectively.

**Example:** (See image generated in *Example of highlighting 6-membered rings of a ligand using 'ball and stick'* style and Example of highlighting 6-membered rings of a ligand using 'color' style)

```
class Pred6MemAromAtom (oechem. OEUnaryAtomPred) :
    def _call_(self, atom):
        return atom. IsAromatic() and oechem. OEAtomIsInAromaticRingSize(atom, 6)
class Pred6MemAromBond(oechem.OEUnaryBondPred):
    def _call_(self, bond):
        return bond. IsAromatic() and oechem. OEBondIsInAromaticRingSize(bond, 6)
def OEAddHighlighting_Predicate(adisp):
   highlight = oedepict.OEHighlightByBallAndStick(oechem.OEBlueTint)
    oegrapheme.OEAddLigandHighlighting(adisp, highlight, Pred6MemAromAtom())
    oegrapheme.OEAddLigandHighlighting(adisp, highlight, Pred6MemAromBond())
```

![](_page_200_Figure_2.jpeg)

![](_page_200_Figure_3.jpeg)

Fig. 107: Example of highlighting 6-membered rings of a ligand using 'ball and stick' style

#### See also:

- Predicate Functors chapter in the OEChem TK manual
- 1. Highlighting using an OEMatchBase object that is initialized by substructure search or maximum common substructure search:

```
void OEAddLigandHighlighting (OE2DActiveSiteDisplay &adisp, const
→OEDepict::OEHighlightBase &highlight,
                             const OEChem:: OEMatchBase &match)
```

**Example:** (See image generated in *Example of highlighting 6-membered rings of a ligand using 'lasso' style*)

```
def OEAddHighlighting_OEMatch(adisp):
    ligand = adisp.GetDisplayedLigand()
   subs = occhem. OESubSearch('lalaaaa1")colors = oechem.OEGetVividColors()
   unique = Truefor match, color in zip (subs. Match (ligand, unique), colors):
```

![](_page_201_Figure_1.jpeg)

Fig. 108: Example of highlighting 6-membered rings of a ligand using 'color' style

```
highlight = oedepict.OEHighlightByLasso(color)
highlight.SetConsiderAtomLabelBoundingBox(True)
oegrapheme. OEAddLigandHighlighting(adisp, highlight, match)
```

1. Highlighting using an OEAtomBondSet object that stores the atoms and bonds being highlighted:

```
void OEAddLigandHighlighting (OE2DActiveSiteDisplay &adisp, const.
→OEDepict::OEHighlightBase &highlight,
                             const OEChem:: OEAtomBondSet &abset)
```

**Example:** (See image generated in *Example of highlighting 6-membered rings of a ligand using 'cogwheel'* style)

```
def OEAddHighlighting_OEAtomBondSet(adisp):
    ligand = adisp.GetDisplayedLigand()
    highlight = oedepict.OEHighlightByCogwheel(oechem.OEPinkTint)
    highlight. SetInnerContour (False)
    abset = oechem. OEAtomBondSet (ligand.GetAtoms(Pred6MemAromAtom());ligand.GetBonds(Pred6MemAromBond()))
    oegrapheme. OEAddLigandHighlighting(adisp, highlight, abset)
```

![](_page_202_Figure_1.jpeg)

Fig. 109: Example of highlighting 6-membered rings of a ligand using 'lasso' style

## 5.4.4 OEAddResidueHighlighting

```
void OEAddResidueHighlighting (OE2DActiveSiteDisplay &adisp,
                               const OEDepict:: OEPen &pen,
                               const OEChem:: OEResidue & residue)
```

Highlights the given residues in the active site display.

adisp The OE2DActiveSiteDisplay object of which residues being highlighted.

pen The OEPen object that specifies the style of the highlighting.

residue The residue being highlighted.

**Example:** (See image generated in *Example of highlighting residues*)

The OEGetLightColors function in the below example returns eight colors that is used to highlight only the first eight residues in the generated image.

![](_page_203_Figure_1.jpeg)

Fig. 110: Example of highlighting 6-membered rings of a ligand using 'cogwheel' style

```
def OEAddHighlighting_OEResidue(adisp):
   for res, color in zip(adisp.GetDisplayedResidues(), oechem.OEGetLightColors()):
       pen = oedepict. OEPen(color, color, oedepict. OEFill_On, 1.0)
       oegrapheme. OEAddResidueHighlighting(adisp, pen, res)
```

## 5.4.5 OEClearSurfaceArcFxn

void OEClearSurfaceArcFxn(OEChem::OEAtomBase \*atom)

Removes the surface drawing functor previously added to the atom.

- · OEGet2DSurfaceArcs function
- OEGetSurfaceArcFxnfunction
- · OEHasSurfaceArcFxn function
- · OESetSurfaceArcFxn function

![](_page_204_Figure_1.jpeg)

Fig. 111: Example of highlighting residues

## 5.4.6 OEConfigure2DPropMap

```
bool OEConfigure2DPropMap(OESystem::OEInterface &itf,
                          unsigned int config=OE2DPropMapSetup::All)
```

Configures the given interface to add property map style parameters.

*itf* The interface being configured.

config The option that specifies which parameters will be added to the interface This value has to be from the OE2DPropMapSetup namespace.

- OEInterface class in the OEChem TK manual
- · OE2DPropMapSetup namespace

## 5.4.7 OEDraw2DSurface

**bool** OEDraw2DSurface(OEDepict::OE2DMolDisplay &disp)

Calculates the arc segments of the molecule surface and draws the arcs into the molecule display using the functor previously added to the atoms (by calling OESet SurfaceArcFxn). See Figure: Example of drawing a molecule surface using the OEDraw2DSurface function.

*disp* The molecule display on which the 2D molecule surface is drawn.

**Note:** If no surface drawing functor is set to the atoms, then the OEDefaultArcFxn functor will be used by default.

![](_page_205_Picture_6.jpeg)

#### Fig. 112: Example of drawing a molecule surface using the OEDraw2DSurface function

#### See also:

- Drawing a Molecule Surface chapter
- OESetSurfaceArcFxn

```
bool OEDraw2DSurface(OEDepict::OE2DMolDisplay &disp,
                     const OEDepict:: OE2DMolDisplay & refdisp)
```

Allows a molecule surface to be generated on one molecule display but drawn into another display. See Figure: Example of using OEDraw2DSurface with reference molecule display.

*disp* The molecule display on which the 2D molecule surface is drawn.

*refdisp* The molecule display for which the 2D molecule surface is calculated.

![](_page_205_Figure_15.jpeg)

Fig. 113: Example of using OEDraw2DSurface with reference molecule display

See also:

- Drawing a Molecule Surface chapter
- · OESetSurfaceArcFxn

## 5.4.8 OEDrawActiveSiteLegend

```
void OEDrawActiveSiteLegend(OEDepict::OEImageBase &image,
                            const OE2DActiveSiteDisplay &adisp,
                            const OE2DActiveSiteLegendDisplayOptions &opts)
```

Draws legend for active site interaction map.

*image* The image on which the color force field legend is drawn.

adisp The OE2DActiveSiteDisplay object that holds the data necessary to depict the interactions of an active site.

opts The OE2DActiveSiteLegendDisplayOptions object that determines how the legend is depicted.

The following code snippet shows how to use the OEDrawActiveSiteLegend function. The image created is shown in Figure: Example of using the OEDrawActiveSiteLegend function.

```
# initializing adisp OE2DActiveSiteDisplay object
rows, \cosh = 2, 4
opts = oegrapheme. OE2DActiveSiteLegendDisplayOptions (rows, cols)
image = odeplot.OEImage(600, 150)oegrapheme. OEDrawActiveSiteLegend(image, adisp, opts)
```

![](_page_206_Figure_12.jpeg)

Fig. 114: Example of using the OEDrawActiveSiteLegend function

**Note:** The OEDrawActiveSiteLegend function renders only those residue "glyphs" that are used to depict the interactions of the given active site when calling the OERenderActiveSite function.

#### See also:

- OE2DActiveSiteDisplay class
- OE2DActiveSiteLegendDisplayOptions class

#### **Code Example**

• Visualizing Protein-Ligand Interactions OpenEye Python Cookbook recipe

• Depicting Active Site Interactions example

## 5.4.9 OEDrawBFactorMapLegend

```
bool OEDrawBFactorMapLegend (OEDepict:: OEImageBase &image,
                            const OE2DActiveSiteDisplay &adisp)
```

Draws the color gradient that is used to visualize B-factor information of an active site by the OERenderBFactorMap function.

*image* The image in which the color gradient is drawn.

adisp The OE2DActiveSiteDisplay object that holds the data necessary to depict the B-factor information of an active site.

#### **Example:**

![](_page_207_Figure_8.jpeg)

![](_page_207_Figure_9.jpeg)

#### Fig. 115: Example of using the OEDrawBFactorMapLegend function

#### See also:

- · OERenderBFactorMap function
- OEDrawColorGradient function

#### **Code Example**

• Visualizing Protein-Ligand B-Factor OpenEye Python Cookbook recipe

## 5.4.10 OEDrawCircle

```
bool OEDrawCircle (OEDepict:: OEImageBase & image, unsigned int style,
                  const OEDepict:: OE2DPoint &center, double radius,
                  const OEDepict:: OEPen &pen=OEDepict:: OEBlackPen)
```

Draws a circle with the given style.

*image* The image on which the circle is drawn.

style Specifies the style of the circle. This value has to be from the  $OECircleStyle$  namespace.

*center* The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

## 5.4.11 OEDrawColorForceFieldLegend

```
void OEDrawColorForceFieldLegend (OEDepict:: OEImageBase & image,
                                  const OEColorForceFieldDisplay &cffdisp,
                                  const OEColorForceFieldLegendDisplayOptions &opts)
```

Draws a legend of the color force field.

*image* The image on which the color force field legend is drawn.

cffdisp The OEColorForceFieldDisplay object that holds the data necessary to depict the color force field.

opts The OEColorForceFieldLegendDisplayOptions object that determine how the legend of color force field is depicted.

The following code snippet shows how to use the *OEDrawColorForceFieldLegend* function. The image created is shown in Figure: Example of using the OEDrawColorForceFieldLegend function.

```
cff = oeshape.OEColorForceField()
cff.Init(oeshape.OEColorFFType ImplicitMillsDean)
cffdisp = oeqrapheme.OEColorForceFieldDisplay(cff)rows, \cosh = 2, 3
opts = oegrapheme.OEColorForceFieldLegendDisplayOptions(rows, cols)
image = odeplot.OEImage(450, 150)oegrapheme.OEDrawColorForceFieldLegend(image, cffdisp, opts)
```

- OEColorForceFieldDisplay class
- OEColorForceFieldLegendDisplayOptions class

![](_page_209_Figure_1.jpeg)

Fig. 116: Example of using the OEDrawColorForceFieldLegend function

## 5.4.12 OEDrawColorGradient

```
void OEDrawColorGradient (OEDepict:: OEImageBase &image,
                          const OESystem:: OEColorGradientBase &colorg)
void OEDrawColorGradient (OEDepict:: OEImageBase &image,
                          const OESystem:: OEColorGradientBase &colorg,
                          const OEColorGradientDisplayOptions &opts)
```

Draws a color gradient.

*image* The image on which the color gradient is drawn.

colorg The color gradient being drawn.

**opts** The OEColorGradientDisplayOptions object that stores the parameters that determine how the color gradient is drawn.

The following code snippet shows how to use the *OEDrawColorGradient* function. The image created is shown in Figure: Example of using the OEDrawColorGradient function.

![](_page_209_Figure_10.jpeg)

![](_page_209_Figure_11.jpeg)

The orientation (*i.e.*, whether the color gradient is rendered vertically or horizontally) depends on the width and height of the OEImageBase object. If the width is greater than the height, then the color gradient is drawn horizontally; otherwise it is rendered vertically. See examples in Figure: Example of rendering the same color gradient into different dimensions.

![](_page_210_Figure_2.jpeg)

Fig. 118: Example of rendering the same color gradient into different dimensions

The OED rawColorGradient function can depict any color gradient derived from the OEColorGradientBase base class. See examples in Figure: Example of rendering various color gradients.

#### See also:

- OEColorGradientDisplayOptions class
- OEColorGradientBase base class
- · OELinearColorGradient, OEExponentialColorGradient, OELogarithmicColorGradient, and OEExponentColorGradient concrete classes

## 5.4.13 OEDrawPeptide

```
bool OEDrawPeptide(OEDepict::OEImageBase& image, const OEChem::OEMolBase& mol)
bool OEDrawPeptide(OEDepict::OEImageBase &image, const OEChem::OEMolBase &mol,
                   const OEPeptideDisplayOptions &opts)
```

Draws a molecule after performing substitutions in which standard amino acids components identified in the molecule are replaced by corresponding circular glyphs.

*image* The image on which the molecule is drawn.

![](_page_211_Figure_1.jpeg)

Fig. 119: Example of rendering various color gradients

*mol* The molecule being draw.

**opts** The OEPeptideDisplayOptions object that stores properties that determine the styles of the peptide depiction.

**Note:** The OEDrawPeptide implementation does not support visualizing large proteins. The number of heavy atoms is limited to 250.

#### **Example:**

The following code snippet shows how to use the  $OEDrawPeptide$  function to generate an interactive SVG image. The image created is shown in Figure: Example of using the OEDrawPeptide function.

```
if s = oechem.oemolistream()flavor = (oechem.OEIFlavor_Generic_Default | oechem.OEIFlavor_FASTA_EmbeddedSMILES)
ifs.SetFlavor(oechem.OEFormat_FASTA, flavor)
ifs.SetFormat(oechem.OEFormat_FASTA)
```

```
fasta = """"FAVS [ [R4 ] COCC (C (=0) 0) Cclcccccl ] """
ifs.openstring(fasta)
mol = occhem. OEGraphMol()oechem.OEReadMolecule(ifs, mol)
image = odeplot.OEImage(400, 250)opts = oegrapheme.OEPeptideDisplayOptions()
opts. SetInteractive (True)
oegrapheme. OEDrawPeptide(image, mol, opts)
oedepict.OEWriteImage("DrawPeptide.svg", image)
```

![](_page_212_Figure_3.jpeg)

Fig. 120: Example of using the OEDrawPeptide function

Note: This *interactive* functionality is only available for . svg image format.

The generated svg image should be included into and HTML page with the SVG MIME type.

<object data="<imagename>.svg" type="image/svg+xml"></object>

#### See also:

- OEPeptideDisplayOptions class
- OEDrawResidues function to visualize nonstandard amino acids
- Generating Interactive SVG Images chapter in OEDepict TK manual

#### **Code Example**

• Depicting Peptides OpenEve Python Cookbook recipe

## 5.4.14 OEDrawResidues

```
bool OEDrawResidues (OEDepict:: OEImageBase& image, const OEChem:: OEMolBase& mol,
                    const bool interactive = false)
```

Draws a molecule after performing substitutions in which standard amino acids components identified in the molecule are replaced by corresponding circular glyphs.

*image* The image on which the molecule is drawn.

*mol* The molecule being draw.

*interactive* The parameter that determines whether the generated image will be interactive (only available for SVG images) revealing the residue on mouse hover.

```
Note: The OEDrawResidues does not support visualizing large proteins. The number of heavy atoms is limited to
250.
```

#### **Example:**

The following code snippet shows how to use the  $OEDrawResidues$  function to generate an interactive SVG image. The image created is shown in Figure: Example of using the OEDrawResidues function. If the molecule has no residue information, if the OEHasResidues function returns false, then a warning will be throw and no image will be generated.

```
image = odeplot.OEImage(400, 250)interactive = True
oegrapheme. OEDrawResidues (image, mol, interactive)
oedepict.OEWriteImage("DrawResidues.svg", image)
```

The OEDrawResidues function allows the visualization of nonstandard amino acids. Nonstandard amino acid residues are represented with a black jagged circle with the residue labels shown at the center.

Note: This *interactive* functionality is only available for . svg image format.

The generated svg image should be included into and HTML page with the SVG MIME type.

<object data="<imagename>.svg" type="image/svg+xml"></object>

- OEDrawPeptide function
- Generating Interactive SVG Images chapter in **OEDepict TK** manual

![](_page_214_Figure_1.jpeg)

#### Fig. 121: Example of using the OEDrawResidues function

## 5.4.15 OEDrawROCSScores

void OEDrawROCSScores (OEDepict:: OEImageBase& image, const std:: vector<double>& scores)

Renders the scores into a radial graph.

*image* The image on which the radial graph of the scores is drawn.

scores The vector of scores. The scores will expected in the following order - shape overlap score - color overlap score - 2D similarity score (optional)

**Note:** All scores are expected to be in the range of [0.0, 1.0]. This [0.0, 1.0] range is transformed to  $[0.0^{\circ} - 360.0^{\circ}]$ angles when representing the scores in the diagram.

```
image = odeplot.OEImage (200, 150)scores = occhem. OEDoubleVector([0.75, 0.25, 0.50])oegrapheme. OEDrawROCSScores (image, scores)
oedepict.OEWriteImage("DrawROCSScores.png", image)
```

#### **Code Example**

- Depicting Shape and Color Atom Overlaps example
- Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

![](_page_215_Figure_1.jpeg)

Fig. 122: Example of using the OEDrawROCSScores function

## 5.4.16 OEDrawSurfaceArc

```
bool OEDrawSurfaceArc(OEDepict:: OEImageBase &image, unsigned int style,
                       const OEDepict:: OE2DPoint & center,
                       double bgnAngle, double endAngle, double radius,
                       const OEDepict:: OEPen &pen)
```

Draws an arc with the given style.

*image* The image on which the arc is drawn.

style Specifies the style of the arc. This value has to be from the  $OESurfaces / E1e$  namespace.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

## 5.4.17 OEDrawUnpairedInteractionMapLegend

```
bool OEDrawUnpairedInteractionMapLegend(OEDepict:: OEImageBase &image,
                                  const OE2DActiveSiteDisplay &adisp,
                                  const OE2DActiveSiteLegendDisplayOptions &opts)
```

Draws legend for unpaired interaction map.

*image* The image in which the color gradient is drawn.

adisp The OE2DActiveSiteDisplay object that holds the data necessary to depict the B-factor information of an active site.

**opts** The OE2DActiveSiteLegendDisplayOptions object that determines how the legend is depicted.

#### **Example:**

![](_page_216_Figure_1.jpeg)

![](_page_216_Figure_2.jpeg)

Fig. 123: Example of using the OEDrawUnpairedInteractionMapLegend function

#### See also:

· OERenderUnpairedInteractionMapfunction

#### **Code Example**

• Visualizing Protein-Ligand Unpaired Interactions OpenEye Python Cookbook recipe

## 5.4.18 OEGet2DSurfaceArcs

```
OESystem:: OEIterBase<OESurfaceArc> *
 OEGet2DSurfaceArcs(const OEDepict::OE2DMolDisplay &disp,
                     double radiusScale = OESurfaceArcScale::Default)
```

Returns an iterator over the OESurfaceArc objects from which a continuous 2D molecule surface can be drawn. See Figure: Example of the data stored in the OESurfaceArc class.

disp The OE2DMolDisplay object for which the arcs of the 2D molecule surface are generated.

*radiusScale* The multiplier used to modify the radius of the returned arcs. The scaling factor has to be in the range of [OESurfaceArcScale\_Minimum, OESurfaceArcScale\_Maximum].

```
OESystem:: OEIterBase<OESurfaceArc> *
 OEGet2DSurfaceArcs(const OEDepict::OE2DMolDisplay &mdisp,
                     const OEDepict:: OE2DAtomDisplay &adisp,
                     double radiusScale = OESurfaceArcScale::Default)
```

![](_page_217_Figure_1.jpeg)

#### Fig. 124: Example of the data stored in the OESurfaceArc class

Returns an iterator over the OESurfaceArc object(s) generated for the given atom display. See Figure: Example of the arcs returned for an atom display with various radius scales.

*mdisp* The OE2DMolDisplay object to which the OE2DAtomDisplay object belongs.

**adisp** The OE2DAtomDisplay object for which the arc(s) of the 2D molecule surface are generated.

radius Scale The multiplier used to modify the radius of the returned arcs. The scaling factor has to be in the range of [OESurfaceArcScale\_Minimum, OESurfaceArcScale\_Maximum].

OESystem:: OEIterBase<OESurfaceArc> \* OEGet2DSurfaceArcs(const OEDepict::OE2DMolDisplay &disp, const std:: vector<double> &radiusScales)

Returns an iterator over the OESurfaceArc objects from which a continuous 2D molecule surface can be drawn.

disp The OE2DMolDisplay object for which the arcs of the 2D molecule surface are generated.

radiusScales The multipliers used to modify the radius of the returned arcs. The vector has to be OEMOLBase. GetMaxAtomIdx long. Each scaling factor has to be in the range of [OESurfaceArcScale\_Minimum, OESurfaceArcScale\_Maximum].

- Drawing a Molecule Surface chapter
- OESurfaceArc classes
- · OESurfaceArcScale namespace

## 5.4.19 OEGetMoleculeSurfaceScale

```
double OEGetMoleculeSurfaceScale(const OEChem:: OEMolBase &mol,
                                 const OEDepict:: OE2DMolDisplayOptions &opts,
                                 double maxRadiusScale = OESurfaceArcScale::Default)
```

Estimates the scaling factor of the molecule depiction considering the size of the molecule surface being drawn around the molecule diagram. See Figure: Example of using the OEGetMoleculeSurfaceScale function.

*mol* The molecule for which the scaling factor is determined.

**opts** The OE2DMolDisplayOptions object that stores the parameters which influence the calculated scaling factor (such as the width and the height of the image).

maxRadiusScale The maximum radius multiplier used to generate the arcs of the 2D molecule surface.

![](_page_218_Figure_7.jpeg)

Fig. 125: Example of using the OEGetMoleculeSurfaceScale function

#### See also:

· OESurfaceArcScale namespace

## 5.4.20 OEGetNearbyAtom

OEDepict::OENearestAtom OEGetNearbyAtom (const OE2DActiveSiteDisplay &disp, const OEDepict:: OE2DPoint &point, double radiusscale=1.0)

Returns an OENearestAtom object that stores a pointer of the atom which is depicted nearest to a given 2D display coordinates. By default, only atoms that not further than half bond away from the given point will be considered.

disp The OE2DActiveSiteDisplay object of which atoms are being considered.

*point* Specifies the 2D display coordinates.

*radiusscale* The multiplier that can be used to increase or to decrease the radius around the given point to be considered. This value has to be in a range of  $[0.25, 2.0]$ .

Note: If there is no atom close to the given display coordinates, then the OENearestBond. IsValid method returns false.

- OENearestAtom class
- OEGetNearestAtom function

## 5.4.21 OEGetNearbyBond

```
OEDepict::OENearestBond OEGetNearbyBond(const OE2DActiveSiteDisplay &disp,
                  const OEDepict:: OE2DPoint &point, double radiusscale=1.0)
```

Returns an OENearestBond object that stores a pointer of the bond which is depicted nearest to a given 2D display coordinates. By default, only atoms that not further than half bond away from the given point will be considered.

disp The OE2DActiveSiteDisplay object of which atoms are being considered.

*point* Specifies the 2D display coordinates.

*radiusscale* The multiplier that can be used to increase or to decrease the radius around the given point to be considered. This value has to be in a range of  $[0.25, 2.0]$ .

Note: If there is no bond close to the given display coordinates, then the OENearestBond. IsValid method returns false.

#### See also:

- OENearestBond class
- · OEGetNearestBond function

## 5.4.22 OEGetNearbyResidue

OENearestResidue OEGetNearbyResidue (const OE2DActiveSiteDisplay &disp, const OEDepict:: OE2DPoint &point, double radiusscale=1.0)

Returns an OENearestResidue object that stores the residue which is depicted nearest to a given 2D display coordinates. By default, only residues that not further than a radius distance from the given point will be considered.

disp The OE2DActiveSiteDisplay object of which atoms are being considered.

*point* Specifies the 2D display coordinates.

*radiusscale* The multiplier that can be used to increase or to decrease the radius around the given point to be considered. This value has to be in a range of  $[0.75, 3.0]$ .

**Note:** If there is no residue close to the given display coordinates, then the *OENearestResidue.IsValid* method returns false.

- OENearestResidue class
- OEGetNearestResidue function

## 5.4.23 OEGetNearestAtom

```
OEDepict:: OENearestAtom OEGetNearestAtom (const OE2DActiveSiteDisplay &disp,
                                          const OEDepict:: OE2DPoint &point)
```

Returns an OENearestAtom object that stores a pointer of the atom which is depicted nearest to a given 2D display coordinates.

disp The OE2DActiveSiteDisplay object of which atoms are being considered.

*point* Specifies the 2D display coordinates.

See also:

- OENearestAtom class
- · OEGetNearbyAtom function

## 5.4.24 OEGetNearestBond

```
OEDepict:: OENearestBond OEGetNearestBond (const OE2DActiveSiteDisplay &disp,
                                          const OEDepict:: OE2DPoint &point)
```

Returns an OENearestBond object that stores a pointer of the bond which is depicted nearest to a given 2D display coordinates.

disp The OE2DActiveSiteDisplay object of which bonds are being considered.

*point* Specifies the 2D display coordinates.

See also:

- OENearestBond class
- · OEGetNearbyBond function

## 5.4.25 OEGetNearestResidue

```
OENearestResidue OEGetNearestResidue (const OE2DActiveSiteDisplay &disp,
                                      const OEDepict:: OE2DPoint &point)
```

Returns an OENearestResidue object that stores a residue which is depicted nearest to a given 2D display coordinates.

disp The OE2DActiveSiteDisplay object of which residues are being considered.

*point* Specifies the 2D display coordinates.

- OENearestResidue class
- · OEGetNearbyResidue function

## 5.4.26 OEGetSurfaceArcFxn

const OESurfaceArcFxnBase &OEGetSurfaceArcFxn(const OEChem::OEAtomBase \*atom)

Returns the surface drawing functor that is associated with the given atom, i.e., when calling the OEDraw2DSurface function this return functor is used to draw the arc segment of the given atom.

See also:

- · OEClearSurfaceArcFxn function
- OEGet2DSurfaceArcs function
- · OEHasSurfaceArcFxn function
- · OESetSurfaceArcFxn function

## 5.4.27 OEGraphemeGetArch

const char \*OEGraphemeGetArch()

## 5.4.28 OEGraphemeGetLicensee

**bool** OEGraphemeGetLicensee(std::string &licensee)

## 5.4.29 OEGraphemeGetPlatform

```
const char *OEGraphemeGetPlatform()
```

## 5.4.30 OEGraphemeGetRelease

const char \*OEGraphemeGetRelease()

## 5.4.31 OEGraphemeGetSite

```
bool OEGraphemeGetSite(std::string &site)
```

## 5.4.32 OEGraphemeGetVersion

unsigned int OEGraphemeGetVersion()

## 5.4.33 OEGraphemelsLicensed

```
bool OEGraphemeIsLicensed(const char *feature=0,
                          unsigned int *expdate=0)
```

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any Grapheme TK functionality.

The 'feature' argument can be used to check for a valid license to Grapheme TK along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current Grapheme TK license.

See also:

· OEChemIsLicensed function

## 5.4.34 OEHasSurfaceArcFxn

bool OEHasSurfaceArcFxn(const OEChem:: OEAtomBase \*atom)

Returns whether or not a surface drawing functor is associated with the given atom.

#### See also:

- · OEClearSurfaceArcFxn function
- · OEGetSurfaceArcFxn function
- OESetSurfaceArcFxnfunction

## 5.4.35 OEPrepareActiveSiteDepiction

**bool** OEPrepareActiveSiteDepiction(OEBio::OEInteractionHintContainer &asite)

Prepares an active site before depiction that involves suppressing hydrogens and calculate distances between the accessible surfaces of the ligand and the surrounding protein.

#### See also:

• Depicting Active Site Interactions example

## 5.4.36 OEPrepareAlignedDepictionFrom3D

Table 5: The overloaded versions of the OERenderActiveSite function

| Link                                                                               | Description                                    |
|------------------------------------------------------------------------------------|------------------------------------------------|
| OEPrepareAlignedDepiction-<br>From3D(fitmol2D, fitmol3D, refmol2D, refmol3D)       | 2D molecule alignment based on 3D              |
| OEPrepareAlignedDepiction-<br>From3D(fitmol2D, fitmol3D, refmol2D, refmol3D, opts) | 2D molecule alignment based on 3D with options |
| OEPrepareAlignedDepiction-<br>From3D(fitmol2D, fitmol3D, <i>shapequery</i> )       | 2D molecule alignment to 3D shape query        |

```
bool OEPrepareAliqnedDepictionFrom3D (OEChem:: OEMolBase &fitmol2D,
                                      const OEChem:: OEMolBase &fitmol3D,
                                      const OEChem:: OEMolBase & refmol2D,
                                       const OEChem:: OEMolBase & refmol3D,
                                      bool clearCoords=true, bool suppressH=true)
```

Generates the 2D coordinates of a molecule driven by the 3D overlay of the 3D reference and the 3D fit molecules and the orientation of the 2D reference molecule.

*fitmol2D* The molecule for which 2D coordinates are generated.

*refmol2D* The 2D molecule whose orientation drives the 2D coordinate generation.

*fitmol3D, refmol3D* The 3D molecule whose overlay drives the 2D coordinate generation.

- clearCoords If false and the fitmol2D has 2D coordinates, then these coordinates are used for the alignment. Otherwise the 2D coordinates of the fitted molecule are generated by calling the OEP repareDepictionFrom3D function.
- *suppressH* If true, then explicit hydrogens are suppressed when generating the 2D coordinates of the fitted molecule. Only hydrogens that are necessary to faithfully represent tetrahedral stereochemistry will be kept.

| <b>bool</b> OEPrepareAlignedDepictionFrom3D(OEChem::OEMolBase &fitmol2D, |
|--------------------------------------------------------------------------|
| const OEChem::OEMolBase &fitmol3D,                                       |
| const OEChem::OEMolBase &refmol2D,                                       |
| const OEChem::OEMolBase &refmol3D,                                       |
| const OEAlignedDepictionFrom3DOptions &opts)                             |

Generates the 2D coordinates of a molecule driven by the 3D overlay of the 3D reference and the 3D fit molecules and the orientation of the 2D reference molecule.

*fitmol2D* The molecule for which 2D coordinates are generated.

refmol2D The 2D molecule whose orientation drives the 2D coordinate generation.

*fitmol3D, refmol3D* The 3D molecules whose overlay drives the 2D coordinate generation.

opts The OEAlignedDepictionFrom3DOptions object that stores options controlling the generation of 2D coordinates.

The following code snippet shows how to use the *OEP repareal ignedDepictionFrom3D* function. See generated images in Table: 2D depiction based on 3D molecule overlay.

![](_page_224_Figure_1.jpeg)

![](_page_224_Figure_2.jpeg)

Table 6: 2D depiction based on 3D molecule overlay

```
bool OEPrepareAliqnedDepictionFrom3D (OEChem:: OEMolBase& fitmol2D,
                                      const OEChem:: OEMolBase& fitmol3D,
                                      const OEShapeOueryDisplay& qdisp);
```

Generates the 2D coordinates of a molecule driven by the 3D overlay of the shape query display object.

*fitmol2D* The molecule for which 2D coordinates are generated.

*refmol2D* The 2D molecule whose orientation drives the 2D coordinate generation.

*gdisp* The *OEShapeQueryDisplay* object that drives the layout of the 2D coordinate generation.

See also:

• OEShapeQueryDisplay class

## 5.4.37 OEPrepareDepictionFrom3D

bool OEPrepareDepictionFrom3D (OEChem:: OEMolBase &mol, bool suppressH=true)

Takes a 3D molecule and generates its 2D coordinates. The layout and orientation of the 2D coordinates are driven by the 3D coordinates.

mol The 3D molecule for which 2D coordinates are generated.

suppressH If true, then explicit hydrogens are suppressed in the input molecule. Only hydrogens that are necessary to faithfully represent tetrahedral stereochemistry will be kept.

**bool** OEPrepareDepictionFrom3D(OEChem::OEMolBase &mol, const OEDepictionFrom3DOptions &  $\leftrightarrow$ opts)

Takes a 3D molecule and generates its 2D coordinates using the given options. The layout and orientation of the 2D coordinates are driven by the 3D coordinates.

mol The 3D molecule for which 2D coordinates are generated.

opts The OEDepictionFrom3DOptions object that stores options controlling the generation of 2D coordinates.

See the 2D molecule depictions in Table: 2D representation of the 3D molecule and the corresponding 3D molecule in Figure: Example of 3D molecule displayed in VIDA.

![](_page_225_Figure_18.jpeg)

#### Table 7: 2D representation of the 3D molecule

![](_page_226_Picture_1.jpeg)

Fig. 126: Example of 3D molecule displayed in VIDA

## 5.4.38 OERenderActiveSite

tion

|  |  |  | Table 8: The overloaded versions of the OERenderActiveSite func- |  |
|--|--|--|------------------------------------------------------------------|--|
|--|--|--|------------------------------------------------------------------|--|

| Link                                          | Description                                         |
|-----------------------------------------------|-----------------------------------------------------|
| <i>OERenderActiveSite(image, adisp)</i>       | renders an active site into an image                |
| <i>OERenderActiveSite(filename, adisp)</i>    | writes an active site display into a file           |
| <i>OERenderActiveSite(stream, ext, adisp)</i> | writes an active site display into an output stream |

## See also:

- · OEDrawActiveSiteLegend function
- · OERenderActiveSiteMaps function
- · OERenderBFactorMap function
- · OERenderContactMap function
- · OERenderUnpairedInteractionMap function

#### **Code Example**

- Depicting Active Site Interactions example
- Visualizing Protein-Ligand Interactions OpenEye Python Cookbook recipe

![](_page_227_Figure_1.jpeg)

![](_page_227_Figure_2.jpeg)

![](_page_227_Figure_3.jpeg)

```
bool OERenderActiveSite(OEDepict::OEImageBase &image,
                        const OE2DActiveSiteDisplay &adisp)
```

Renders the active site display into an image.

*image* The image in which the active site is drawn.

adisp The OE2DActiveSiteDisplay object that holds the data necessary to depict the interactions of an active site.

**Example:** 

```
# initializing asite oechem. OEInteractionHintContainer (receptor, ligand) object
image = odeplot.OEImage(800.0, 600.0)opts = oegrapheme.OE2DActiveSiteDisplayOptions(image.GetWidth(), image.GetHeight())
opts.SetRenderInteractiveLegend(True)
adisp = oegrapheme. OE2DActiveSiteDisplay(asite, opts)
oegrapheme. OERenderActiveSite(image, adisp)
oedepict.OEWriteImage("OERenderActiveSite-image-adisp.svg", image)
```

- OE2DActiveSiteDisplay class
- OE2DActiveSiteDisplayOptions class

```
bool OERenderActiveSite(const std::string &filename,
                        const OE2DActiveSiteDisplay &adisp)
```

Writes the active site display into a file.

*filename* The name of the file into which the active site display is being written. The extension of the filename determine the type of the image.

**adisp** The OE2DActiveSiteDisplay object that holds the data necessary to depict the interactions of an active site.

**Example:** 

```
# initializing asite oechem.OEInteractionHintContainer(receptor, ligand) object
opts = oegrapheme. OE2DActiveSiteDisplayOptions(800.0, 600.0)
opts.SetRenderInteractiveLegend(True)
adisp = oeqrapheme. OE2DActiveSiteDisplay(asite, opts)oegrapheme.OERenderActiveSite("OERenderActiveSite-fname-adisp.svg", adisp)
```

#### See also:

- OE2DActiveSiteDisplay class
- OE2DActiveSiteDisplayOptions class

```
bool OERenderActiveSite(OEPlatform::oeostream &os,
                        const std:: string & extension,
                        const OE2DActiveSiteDisplay &adisp)
```

Writes the active site display into a stream.

os The stream into which the active site is being written.

ext The extension which determine the type of the image.

adisp The OE2DActiveSiteDisplay object that holds the data necessary to depict the interactions of an active site.

#### **Example:**

```
# initializing asite oechem. OEInteractionHintContainer (receptor, ligand) object
opts = oegrapheme. OE2DActiveSiteDisplayOptions (800.0, 600.0)
opts.SetRenderInteractiveLegend(True)
adisp = oegrapheme. OE2DActiveSiteDisplay(asite, opts)
ofs = oechem.oeofstream("OERenderActiveSite-stream-adisp.svq")
oegrapheme. OERenderActiveSite(ofs, "svg", adisp)
```

- OE2DActiveSiteDisplay class
- OE2DActiveSiteDisplayOptions class

## 5.4.39 OERenderActiveSiteMaps

```
bool OERenderActiveSiteMaps (OEDepict::OEImageBase &image,
                             const OEBio:: OEInteractionHintContainer &asite)
```

Renders four protein-ligand maps (interaction, unpaired, b-factor and contact) into separate tabs of an image.

*image* The image in which the active site is drawn.

asite The OEInteractionHintContainer object that holds the data for the active site.

Note: This functionality is only available for . svg image format.

#### **Example:**

```
asite = oechem. OEInteractionHintContainer (protein, ligand)
oechem. OEPerceiveInteractionHints (asite)
oegrapheme.OEPrepareActiveSiteDepiction(asite)
image = odeplot.OEImage(800.0, 600.0)oegrapheme.OERenderActiveSiteMaps(image, asite)
oedepict.OEWriteImage("RenderActiveSiteMaps.svg", image)
```

There is no image available for the PDF version of this book.

#### See also:

- · OERenderActiveSite function
- OERenderBFactorMap function
- OERenderContactMap function
- · OERenderUnpairedInteractionMapfunction

#### **Code Example**

• Visualizing Protein-Ligand Maps OpenEve Python Cookbook recipe

## 5.4.40 OERenderBFactorMap

```
bool OERenderBFactorMap (OEDepict:: OEImageBase &image,
                         const OE2DActiveSiteDisplay &adisp)
```

Renders the B-factor information of an active site display into an image.

*image* The image in which the active site is drawn.

adisp The OE2DActiveSiteDisplay object that holds the data necessary to depict the B-Factor information of an active site.

**Example:** 

```
asite = oechem. OEInteractionHintContainer (protein, ligand)
oechem.OEPerceiveInteractionHints(asite)
oegrapheme.OEPrepareActiveSiteDepiction(asite)
image = odeplot.OEImage(800.0, 600.0)opts = oegrapheme.OE2DActiveSiteDisplayOptions(image.GetWidth(), image.
\rightarrowGetHeight())
opts.SetRenderInteractiveLegend(True)
adisp = oegrapheme. OE2DActiveSiteDisplay(asite, opts)
oegrapheme. OERenderBFactorMap (image, adisp)
oedepict.OEWriteImage("RenderBFactorMap.svg", image)
```

## Legend

![](_page_230_Figure_3.jpeg)

Fig. 128: Example of using the OERenderBfactorMap function

- · OEDrawBFactorMapLegend function
- · OERenderActiveSite function
- · OERenderActiveSiteMaps function

- OERenderContactMapfunction
- OERenderUnpairedInteractionMapfunction

#### **Code Example**

- Visualizing Protein-Ligand B-Factor OpenEye Python Cookbook example
- Visualizing Protein-Ligand B-Factor Map OpenEye Python Cookbook example

## 5.4.41 OERenderContactMap

bool OERenderContactMap (OEDepict:: OEImageBase& image, const OE2DActiveSiteDisplay& adisp);

Renders the protein-ligand contact map with *residue* toggle buttons. Clicking on any residue will highlight those ligand atoms that interact with the residue.

**Note:** This functionality is **only available** for . svq image format. In all other image formats it only depicts the residue circles.

The generated svq image should be included into and HTML page with the SVG MIME type.

<object data="<imagename>.svg" type="image/svg+xml"></object>

*image* The image on which the contact map is rendered.

adisp The OE2DActiveSiteDisplay object that holds the data necessary to depict the interactions of an active site.

The following code snippet shows how to use the OERenderContactMap function. The image created is shown in Figure: Example of using the OERenderContactMap function.

**Example:** 

```
asite = oechem. OEInteractionHintContainer (protein, ligand)
oechem. OEPerceiveInteractionHints (asite)
oegrapheme.OEPrepareActiveSiteDepiction(asite)
image = odeplot.OEImage(800.0, 600.0)opts = oegrapheme.OE2DActiveSiteDisplayOptions(image.GetWidth(), image.GetHeight())
adisp = oegrapheme. OE2DActiveSiteDisplay(asite, opts)oegrapheme. OERenderContactMap(image, adisp)
oedepict.OEWriteImage("RenderContactMap.svg", image)
```

There is no image available for the PDF version of this book.

- · OERenderActiveSite function
- OERenderActiveSiteMaps function
- OERenderBFactorMap function
- · OERenderUnpairedInteractionMap function

**Code Example** 

• Visualizing Protein-Ligand Contacts OpenEye Python Cookbook recipe

## 5.4.42 OERenderColorOverlap

```
void OERenderColorOverlap (OEDepict:: OEImageBase &image,
                           const OEShapeOverlapDisplay &odisp)
```

Renders the color overlap between a reference and a fit molecule.

- *image* The image on which the fit molecule is rendered along with circles representing the satisfied and missed color atoms of the reference molecule.
- odisp The OEShapeOverlapDisplay object that holds the data necessary to depict the color overlap between the reference and the fit molecules.

The following code snippet shows how to use the OERenderColorOverlap function. The image created is shown in Table: Example of using the OERenderColorOverlap function.

```
cff = oeshape.OEColorForceField()
cff.Init(oeshape.OEColorFFType_ImplicitMillsDean)
qdisp = oeqrapheme.OEShapeQueryDisplay(refmol, cff)
opts = oegrapheme.OEColorOverlapDisplayOptions()
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
arcpen = oedepict.OEPen(oechem.OEGrey, oechem.OEGrey, oedepict.OEFill_Off,
                        2.0, oedepict.OEStipple_ShortDash)
opts.SetQuerySurfaceArcFxn(oegrapheme.OEDefaultArcFxn(arcpen))
odisp = oegrapheme. OEShapeOverlapDisplay(qdisp, fitmol, opts)
image = odeplot.OEImage(420.0, 280.0)oegrapheme.OERenderColorOverlap(image, odisp)
```

Note: The color atom matches between the reference and the fit molecule are represented by circles (or half circles if two color atoms occupy the same space in 3D). Each circle corresponds to a color atom in the reference molecule. The color of the circle indicates the fitness of the color atom match in 3D. The lighter the color, the smaller the overlap between the reference and fit color atoms in 3D. Unfilled circles represent unmatched reference color atoms. If there is a good color atom match exist for a reference color atom in 3D, then the circle representing the color atom is positioned to the matching fit color atom in 2D.

![](_page_233_Figure_1.jpeg)

Table 9: Example of using the OERenderColorOverlap function

**Warning:** When calling the OERenderColorOverlap function **no overlay is performed to maximize the** color overlap between the reference and the fit molecule, *i.e.*, the function simply calculates the color overlap using the given 3D coordinates.

#### See also:

- OEColorOverlapDisplayOptions class
- · OERenderShapeQuery function
- · OERenderShapeOverlap function

#### **Code Example**

- Depicting Shape and Color Atom Overlaps example
- Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

## 5.4.43 OERenderRamachandranPlot

bool OERenderRamachandranPlot (OEDepict:: OEImageBase &image, const OERamachandranPlot &plot)

Renders the six Ramachandran plots into separate tabs of the given image.

*image* The image on which the Ramachandran plots are rendered.

plot The OERamachandranPlot object that stores the data of a Ramachandran plot.

Note: This functionality is only available for . svg image format.

#### **Example:**

```
image = odeplot.OEImage(800, 600)ramaplot = oegrapheme. OERamachandranPlot()
ramaplot.AddMolecule(protein)
oegrapheme. OERenderRamachandranPlot (image, ramaplot)
```

## 5.4.44 OERenderShapeOverlap

Table 10: The overloaded versions of the OERenderShapeOverlap function

| Link                                                             | Description                               |
|------------------------------------------------------------------|-------------------------------------------|
| <i>OERenderShapeOverlap(image, overlapdisp)</i>                  | render shape overlap                      |
| <i>OERenderShapeOverlap(molimage, overlapimage, overlapdisp)</i> | render shape overlap into separate images |

```
void OERenderShapeOverlap(OEDepict:: OEImageBase &image,
                          const OEShapeOverlapDisplay &odisp)
```

Renders the shape overlap between a reference and a fit molecule.

- *image* The image on which the fit molecule is rendered along with the property map and the molecule surface of the reference molecule representing the shape overlap.
- odisp The OEShapeOverlapDisplay object that holds the data necessary to depict the shape overlap between the reference and the fit molecules.

The following code snippet shows how to use the *OERenderShapeOverlap* function. The image created is shown in Table: Example of using the OERenderShapeOverlap function.

```
cff = oeshape.OEColorForceField()
cff.Init(oeshape.OEColorFFType_ImplicitMillsDean)
qdisp = oegrapheme.OEShapeQueryDisplay(refmol, cff)
opts = oegrapheme.OEShapeOverlapDisplayOptions()
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
arcpen = oedepict.OEPen(oechem.OEGrey, oechem.OEGrey, oedepict.OEFill_Off,
                        2.0, oedepict.OEStipple_ShortDash)
opts.SetQuerySurfaceArcFxn(oegrapheme.OEDefaultArcFxn(arcpen))
odisp = oegrapheme. OEShapeOverlapDisplay(qdisp, fitmol, opts)
image = odeplot.OEImage(420.0, 280.0)oegrapheme.OERenderShapeOverlap(image, odisp)
```

Note: The shape overlap between the reference and the fit molecule is visualized by using a property map ( $OE2DPropMap$ ), i.e., a 2D grid, laid underneath the molecule structure, where the cells of the grid that are colored brown indicate good 3D shape overlap between the reference and the fit molecules. Additionally, clashes between the molecular graph of the fit molecule and 2D molecule surface of the reference structure imply shape mismatch in 3D.

![](_page_235_Figure_1.jpeg)

Table 11: Example of using the OERenderShapeOverlap function

**Warning:** When calling the OERenderShapeOverlap function no overlay is performed to maximize the color overlap between the reference and the fit molecule, *i.e.*, the function simply calculates the shape overlap using the given 3D coordinates.

void OERenderShapeOverlap (OEDepict:: OEImageBase& molimage, OEDepict:: OEImageBase& overlapimage, const OEShapeOverlapDisplay& odisp);

Renders the shape overlap between a reference and a fit molecule into to separate images.

*molimage* The image on which the fit molecule is rendered along with the surface of the reference molecule.

*overlapimage* The image on which the property map is rendered representing the shape overlap.

odisp The OEShapeOverlapDisplay object that holds the data necessary to depict the shape overlap between the reference and the fit molecules.

Note: The background of the molecule image is transparent. By superimposing the two images (molecule image on top), the result would be as visualizing the shape overlay in one image.

#### See also:

- OEShapeOverlapDisplayOptions class
- · OERenderShapeQuery function
- · OERenderColorOverlap function

#### **Code Example**

- Depicting Shape and Color Atom Overlaps example
- Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

## 5.4.45 OERenderShapeQuery

```
void OERenderShapeQuery (OEDepict:: OEImageBase &image,
                         const OEShapeQueryDisplay &disp)
```

Renders the reference molecule of the shape overlap.

*image* The image on which the reference molecule is rendered.

disp The OEShapeQueryDisplay object that holds the data necessary to depict the reference molecule of a shape overlap.

The following code snippet shows how to use the OERenderShapeQuery function. The image created is shown in Figure: Example of using the OERenderShapeQuery function.

```
opts = oegrapheme.OEShapeQueryDisplayOptions()
opts.SetTitleLocation(oedepict.OETitleLocation_Hidden)
arcpen = oedepict.OEPen(oechem.OEWhite, oechem.OELightGrey, oedepict.OEFill_On, 2.0)
opts.SetSurfaceArcFxn(oegrapheme.OEDefaultArcFxn(arcpen))
cff = oeshape.OEColorForceField()
cff.Init(oeshape.OEColorFFType_ImplicitMillsDean)
disp = oegrapheme. OEShapeQueryDisplay(refmol, cff, opts)
image = odeplot.OEImage(420.0, 280.0)oegrapheme.OERenderShapeOuery(image, disp)
```

![](_page_236_Figure_8.jpeg)

Fig. 129: Example of using the OERenderShapeQuery function

#### See also:

• OEShapeOueryDisplayOptions class

- OERenderColorOverlap function
- OERenderShapeOverlap function

#### **Code Example**

- Depicting Shape and Color Atom Overlaps example
- Visualizing Shape and Color Overlap OpenEye Python Cookbook recipe

## 5.4.46 OERenderUnpairedInteractionMap

```
bool OERenderUnpairedInteractionMap (OEDepict:: OEImageBase &image,
                                     const OE2DActiveSiteDisplay &adisp)
```

Renders the protein-ligand map with clash and unpaired interactions.

*image* The image in which the active site is drawn.

**adisp** The OE2DActiveSiteDisplay object that holds the data necessary to depict the interactions of an active site.

The OERenderUnpairedInteractionMap function currently visualizes the following interactions:

- Atom clash interaction (see OEClashInteractionHint class)
- Unpaired and clash types of the hydrogen bonding interaction (see OEHBondInteractionHint class OEHBondInteractionHintType namespace)
- Unpaired types of the salt-bridge interaction (see OESaltBridgeInteractionHint class and OESaltBridgeInteractionHintType namespace)

The following code snippet shows how to use the OERenderUnpairedInteractionMap function. The image created is shown in Figure: Example of using the OERenderUnpairedInteraction function.

```
asite = oechem. OEInteractionHintContainer (protein, ligand)
oechem. OEPerceiveInteractionHints (asite)
oegrapheme.OEPrepareActiveSiteDepiction(asite)
image = odeplot.OEImage(800.0, 600.0)opts = oegrapheme.OE2DActiveSiteDisplayOptions(image.GetWidth(), image.GetHeight())
opts.SetRenderInteractiveLegend(True)
adisp = oegrapheme. OE2DActiveSiteDisplay(asite, opts)
oegrapheme.OERenderUnpairedInteractionMap(image, adisp)
oedepict.OEWriteImage("RenderUnpairedMap.svg", image)
```

Note: Please note that unpaired interactions have no direction in 3D, therefore the *linker* representing these unpaired interactions in 2D have no real spatial meaning either. Ligand linkers are directed away from the ligand, while protein linkers are directed towards the ligand when rendered in 2D.

- · OEDrawUnpairedInteractionMapLegend function
- OERenderActiveSite function

# Legend

![](_page_238_Figure_2.jpeg)

#### Fig. 130: Example of using the OERenderUnpairedInteraction function

- · OERenderActiveSiteMaps function
- · OERenderContactMap function
- · OERenderBFactorMap function

#### **Code Example**

• Visualizing Protein-Ligand Unpaired Interactions OpenEye Python Cookbook recipe

## 5.4.47 OESetSurfaceArcFxn

```
bool OESetSurfaceArcFxn(OEChem:: OEMolBase& mol,
                        OEChem:: OEAtomBase *atom,
                         const OESurfaceArcFxnBase &func)
```

Attaches the arc drawing functor to the given atom.

mol The molecule the atom belongs to.

atom The atom to which the functor will be attached.

*func* The functor that will be used to draw the arc segment(s) of the molecule surface that correspond(s) to the given atom when the *OEDraw2DSurface* function in invoked.

#### See also:

- · OEClearSurfaceArcFxn function
- · OEGetSurfaceArcFxn function
- · OEHasSurfaceArcFxn function

## 5.4.48 OESetup2DPropMap

bool OESetup2DPropMap (OE2DPropMap &propmap, const OESystem:: OEInterface &itf)

Initializes an OE2DPropMap object from the parameters of a given interface.

# 5.5 OEGrapheme Basic Circle and Arc Drawing Functions

## 5.5.1 OEDrawAlphaRainbowCircle

```
bool OEDrawAlphaRainbowCircle(OEDepict:: OEImageBase &image,
                              const OEDepict:: OE2DPoint &center, double radius,
                              const OEDepict:: OEPen &pen,
                              unsigned int
→patternDirection=OEPatternDirection::Outside)
```

Draws a circle with the OECircleStyle\_AlphaRainbow style. See Figure: OEDrawAlphaRainbowCircle.

![](_page_239_Figure_13.jpeg)

Fig. 131: OEDrawAlphaRainbowCircle

*image* The image on which the circle is drawn.

*center* The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See example (A) and (B) in Figure: OEDrawAlphaRainbowCircle.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the circle. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawAlphaRainbowCircle.

## 5.5.2 OEDrawAlphaRainbowSurfaceArc

| <b>bool</b> OEDrawAlphaRainbowSurfaceArc(OEDepict::OEImageBase &image, |
|------------------------------------------------------------------------|
| const OEDepict::OE2DPoint &center,                                     |
| double bgnAngle, double endAngle, double radius,                       |
| const OEDepict::OEPen &pen,                                            |
| double edgeAngle=10.0,                                                 |
| unsigned int                                                           |
| ↪patternDirection=OEPatternDirection::Outside)                         |

Draws an arc with the OESurfaceArcStyle\_AlphaRainbow style. See Figure: OEDrawAlphaRainbowSurfaceArc.

![](_page_240_Figure_4.jpeg)

Fig. 132: OEDrawAlphaRainbowSurfaceArc

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawAlphaRainbowSurfaceArc.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the arc. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawAlphaRainbowSurfaceArc.

See also:

• OEAlphaRainbowArcFxn class

## 5.5.3 OEDrawBrickRoadCircle

```
bool OEDrawBrickRoadCircle(OEDepict::OEImageBase &image,
                           const OEDepict:: OE2DPoint &center, double radius,
                           const OEDepict:: OEPen &pen,
                           unsigned int patternDirection=OEPatternDirection::Outside,
                           double patternAngle=20.0,
                           double patternWidthRatio=0.15)
```

Draws a circle with the OECircleStyle\_BrickRoad style. See Figure: OEDrawBrickRoadCircle.

![](_page_241_Figure_1.jpeg)

Fig. 133: OEDrawBrickRoadCircle

- *image* The image on which the circle is drawn.
- center The center of the circle.
- *radius* The radius of the circle.
- *pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawBrickRoadCircle.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the circle. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawBrickRoadCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawBrickRoadCircle.

**pattern Width Ratio** Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (E) in Figure: OEDrawBrickRoadCircle.

## 5.5.4 OEDrawBrickRoadSurfaceArc

![](_page_241_Figure_15.jpeg)

Draws an arc with the OESurfaceArcStyle BrickRoad style.

![](_page_241_Figure_17.jpeg)

Fig. 134: OEDrawBrickRoadSurfaceArc

*image* The image on which the arc is drawn.

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

- *pen* The graphical properties of the arc.
- *edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawBrickRoadSurfaceArc.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the arc. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawBrickRoadSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawBrickRoadSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (E) and (F) in Figure: OEDrawBrickRoadSurfaceArc.

#### See also:

• OEBrickRoadArcFxn class

## 5.5.5 OEDrawCastleCircle

```
bool OEDrawCastleCircle(OEDepict::OEImageBase &image,
                        const OEDepict:: OE2DPoint & center, double radius,
                        const OEDepict:: OEPen &pen, double patternAngle=15.0,
                        double patternWidthRatio=0.20)
```

Draws a circle with the *OECircleStyle\_Castle* style.

![](_page_242_Figure_19.jpeg)

Fig. 135: OEDrawCastleCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in *Figure: OEDrawCastleCircle*.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawCastleCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawCastleCircle.

## 5.5.6 OEDrawCastleSurfaceArc

![](_page_243_Figure_8.jpeg)

Draws an arc with the OESurfaceArcStyle\_Castle style.

![](_page_243_Figure_10.jpeg)

Fig. 136: OEDrawCastleSurfaceArc

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawCastleSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawCastleSurfaceArc.

minPattern Width Ratio, maxPattern Width Ratio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawCastleSurfaceArc.

#### See also:

• OECastleArcFxn class

## 5.5.7 OEDrawCogCircle

```
bool OEDrawCogCircle(OEDepict:: OEImageBase &image,
                     const OEDepict:: OE2DPoint & center, double radius,
                     const OEDepict:: OEPen &pen,
                     double patternAngle=15.0, double patternWidthRatio=0.20)
```

Draws a circle with the OECircleStyle\_Cog style.

![](_page_244_Figure_7.jpeg)

#### Fig. 137: OEDrawCogCircle

*image* The image on which the circle is drawn.

*center* The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawCogCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawCogCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawCogCircle.

## 5.5.8 OEDrawCogSurfaceArc

```
bool OEDrawCogSurfaceArc(OEDepict:: OEImageBase &image,
                         const OEDepict:: OE2DPoint & center,
                          double bgnAngle, double endAngle, double radius,
                          const OEDepict:: OEPen &pen, double edgeAngle=10.0,
                          double patternAngle=15.0,
                          double minPatternWidthRatio=0.20,
                          double maxPatternWidthRatio=0.20)
```

Draws an arc with the OESurfaceArcStyle\_Cog style.

*image* The image on which the arc is drawn.

![](_page_245_Figure_1.jpeg)

Fig. 138: OEDrawCogSurfaceArc

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to  $3$  o'clock, etc.

*radius* The radius of the arc.

pen The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawCogSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawCogSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawCogSurfaceArc.

#### See also:

• OECogArcFxn class

## 5.5.9 OEDrawDefaultCircle

```
bool OEDrawDefaultCircle(OEDepict:: OEImageBase &image,
                          const OEDepict:: OE2DPoint & center, double radius,
                          const OEDepict:: OEPen &pen)
```

Draws a circle with the OECircleStyle\_Default style.

![](_page_245_Figure_18.jpeg)

Fig. 139: OEDrawDefaultCircle

*image* The image on which the circle is drawn.

*center* The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples in Figure: OEDrawDefaultCircle.

## 5.5.10 OEDrawDefaultSurfaceArc

```
bool OEDrawDefaultSurfaceArc(OEDepict:: OEImageBase &image,
                             const OEDepict:: OE2DPoint &center,
                             double bgnAngle, double endAngle, double radius,
                              const OEDepict:: OEPen &pen)
```

Draws an arc with the OESurfaceArcStyle\_Default style.

![](_page_246_Picture_9.jpeg)

Fig. 140: OEDrawDefaultSurfaceArc

*image* The image on which the arc is drawn.

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

See also:

• OEDefaultArcFxn class

## 5.5.11 OEDrawEyelashCircle

```
bool OEDrawEyelashCircle(OEDepict:: OEImageBase &image,
                         const OEDepict:: OE2DPoint & center, double radius,
                          const OEDepict:: OEPen &pen,
                          unsigned int patternDirection=OEPatternDirection::Outside,
                          double patternAngle=10.0,
                         double patternWidthRatio=0.15)
```

Draws a circle with the OECircleStyle\_Eyelash style.

*image* The image on which the circle is drawn.

![](_page_247_Figure_1.jpeg)

Fig. 141: OEDrawEyelashCircle

- *center* The center of the circle.
- *radius* The radius of the circle.
- *pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawEyelashCircle.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the circle. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawEyelashCircle.

**patternAngle** Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawEyelashCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (E) in Figure: OEDrawEyelashCircle.

## 5.5.12 OEDrawEyelashSurfaceArc

![](_page_247_Figure_14.jpeg)

Draws an arc with the OESurfaceArcStyle\_Eyelash style.

![](_page_247_Figure_16.jpeg)

Fig. 142: OEDrawEyelashSurfaceArc

*image* The image on which the arc is drawn.

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

- *pen* The graphical properties of the arc.
- *edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawEyelashSurfaceArc.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the arc. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawEyelashSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawEyelashSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (E) and (F) in Figure: OEDrawEyelashSurfaceArc.

#### See also:

• OEEyelashArcFxn class

## 5.5.13 OEDrawFlowerCircle

```
bool OEDrawFlowerCircle(OEDepict:: OEImageBase &image,
                        const OEDepict:: OE2DPoint & center, double radius,
                        const OEDepict:: OEPen &pen, double patternAngle=30.0)
```

Draws a circle with the OECircleStyle\_Flower style.

![](_page_248_Figure_19.jpeg)

Fig. 143: OEDrawFlowerCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawFlowerCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawFlowerCircle.

## 5.5.14 OEDrawFlowerSurfaceArc

| <b>bool</b> OEDrawFlowerSurfaceArc(OEDepict::OEImageBase &image,      |
|-----------------------------------------------------------------------|
| const OEDepict::OE2DPoint &center,                                    |
| <b>double</b> bgnAngle, <b>double</b> endAngle, <b>double</b> radius, |
| const OEDepict::OEPen &pen, <b>double</b> edgeAngle=10.0,             |
| <b>double</b> patternAngle=30.0,                                      |
| <b>double</b> minPatternWidthRatio=0.20,                              |
| <b>double</b> maxPatternWidthRatio=0.20)                              |

Draws an arc with the OESurfaceArcStyle\_Flower style.

![](_page_249_Figure_8.jpeg)

Fig. 144: OEDrawFlowerSurfaceArc

*image* The image on which the arc is drawn.

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

- *pen* The graphical properties of the arc.
- *edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawFlowerSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawFlowerSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawFlowerSurfaceArc.

#### See also:

• OEFlowerArcFxn class

## 5.5.15 OEDrawGreekKeyCircle

```
bool OEDrawGreekKeyCircle(OEDepict:: OEImageBase &image,
                          const OEDepict:: OE2DPoint & center, double radius,
                           const OEDepict:: OEPen &pen, double patternAngle=15.0,
                          double patternWidthRatio=0.20)
```

Draws a circle with the OECircleStyle\_GreekKey style.

![](_page_250_Figure_4.jpeg)

Fig. 145: OEDrawGreekKeyCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawGreekKeyCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawGreekKeyCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawGreekKeyCircle.

## 5.5.16 OEDrawNecklaceCircle

```
bool OEDrawNecklaceCircle(OEDepict::OEImageBase &image,
                          const OEDepict:: OE2DPoint & center, double radius,
                          const OEDepict:: OEPen &pen, double patternAngle=20.0,
                          double patternWidthRatio=0.15)
```

Draws a circle with the OECircleStyle\_Necklace style.

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawNecklaceCircle.

![](_page_251_Figure_1.jpeg)

Fig. 146: OEDrawNecklaceCircle

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawNecklaceCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawNecklaceCircle.

## 5.5.17 OEDrawNecklaceSurfaceArc

```
bool OEDrawNecklaceSurfaceArc(OEDepict:: OEImageBase &image,
                               const OEDepict:: OE2DPoint & center,
                               double bgnAngle, double endAngle, double radius,
                               const OEDepict:: OEPen &pen, double edgeAngle=10.0,
                               double patternAngle=20.0,
                               double minPatternWidthRatio=0.15,
                               double maxPatternWidthRatio=0.15)
```

Draws an arc with the OESurfaceArcStyle Necklace style.

![](_page_251_Figure_10.jpeg)

Fig. 147: OEDrawNecklaceSurfaceArc

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

pen The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawNecklaceSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawNecklaceSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawNecklaceSurfaceArc.

See also:

 $\bullet$  OENecklaceArcFxn class

## 5.5.18 OEDrawOliveBranchCircle

```
bool OEDrawOliveBranchCircle (OEDepict:: OEImageBase &image,
                              const OEDepict:: OE2DPoint & center, double radius,
                              const OEDepict:: OEPen &pen,
                              double patternAngle=15.0,
                              double patternWidthRatio=0.15)
```

Draws a circle with the OECircleStyle\_OliveBranch style.

![](_page_252_Figure_11.jpeg)

Fig. 148: OEDrawOliveBranchCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawOliveBranchCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawOliveBranchCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawOliveBranchCircle.

#### See also:

• OEOliveBranchArcFxn class

## 5.5.19 OEDrawOliveBranchSurfaceArc

| <b>bool</b> OEDrawOliveBranchSurfaceArc(OEDepict::OEImageBase ℑ, |
|------------------------------------------------------------------|
| const OEDepict::OE2DPoint &center,                               |
| double bgnAngle, double endAngle, double radius,                 |
| const OEDepict::OEPen &pen,                                      |
| double edgeAngle = 10.0, double patternAngle = 15.0,             |
| double minPatternWidthRatio = 0.15,                              |
| double maxPatternWidthRatio = 0.15)                              |

Draws an arc with the OESurfaceArcStyle OliveBranch style.

![](_page_253_Figure_4.jpeg)

Fig. 149: OEDrawOliveBranchSurfaceArc

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

radius The radius of the arc.

**pen** The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawOliveBranchSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawOliveBranchSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawOliveBranchSurfaceArc.

## 5.5.20 OEDrawPearlsCircle

```
bool OEDrawPearlsCircle(OEDepict::OEImageBase &image,
                        const OEDepict:: OE2DPoint &center, double radius,
                        const OEDepict:: OEPen &pen, double patternAngle=15.0)
```

Draws a circle with the *OECircleStyle\_Pearls* style.

![](_page_254_Figure_4.jpeg)

Fig. 150: OEDrawPearlsCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawPearlsCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawPearlsCircle.

## 5.5.21 OEDrawPearlsSurfaceArc

```
bool OEDrawPearlsSurfaceArc(OEDepict:: OEImageBase &image,
                             const OEDepict:: OE2DPoint & center,
                             double bgnAngle, double endAngle, double radius,
                             const OEDepict:: OEPen &pen, double edgeAngle=10.0,
                             double patternAngle=25.0,
                             double minPatternWidthRatio=0.20,
                             double maxPatternWidthRatio=0.20)
```

Draws an arc with the OESurfaceArcStyle\_Pearls style.

![](_page_254_Figure_16.jpeg)

Fig. 151: OEDrawPearlsSurfaceArc

*image* The image on which the arc is drawn.

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

- *pen* The graphical properties of the arc.
- *edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawPearlsSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawPearlsSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawPearlsSurfaceArc.

See also:

• OEPearlsArcFxn class

## 5.5.22 OEDrawRaceTrackCircle

```
bool OEDrawRaceTrackCircle(OEDepict::OEImageBase &image,
                            const OEDepict:: OE2DPoint & center, double radius,
                            const OEDepict:: OEPen &pen)
```

Draws a circle with the OECircleStyle\_RaceTrack style.

![](_page_255_Figure_17.jpeg)

Fig. 152: OEDrawRaceTrackCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawRaceTrackCircle.

## 5.5.23 OEDrawRaceTrackSurfaceArc

```
bool OEDrawRaceTrackSurfaceArc(OEDepict:: OEImageBase &image,
                                const OEDepict:: OE2DPoint & center,
                                double bgnAngle, double endAngle, double radius,
                                const OEDepict:: OEPen &pen,
                                double edgeAngle=10.0)
```

Draws an arc with the OESurfaceArcStyle RaceTrack style.

![](_page_256_Figure_4.jpeg)

Fig. 153: OEDrawRaceTrackSurfaceArc

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

**pen** The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawRaceTrackSurfaceArc.

See also:

• OERaceTrackArcFxn class

## 5.5.24 OEDrawRailroadTrackCircle

```
bool OEDrawRailroadTrackCircle(OEDepict::OEImageBase &image,
                               const OEDepict:: OE2DPoint &center, double radius,
                                const OEDepict:: OEPen &pen,
                               double patternAngle=10.0,
                               double patternWidthRatio=0.15)
```

Draws a circle with the OECircleStyle\_RailroadTrack style.

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawRailroadTrackCircle.

![](_page_257_Figure_1.jpeg)

Fig. 154: OEDrawRailroadTrackCircle

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawRailroadTrackCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawRailroadTrackCircle.

## 5.5.25 OEDrawRailroadTrackSurfaceArc

![](_page_257_Figure_8.jpeg)

Draws an arc with the OESurfaceArcStyle\_RailroadTrack style.

![](_page_257_Figure_10.jpeg)

Fig. 155: OEDrawRailroadTrackSurfaceArc

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawRailroadTrackSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawRailroadTrackSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawRailroadTrackSurfaceArc.

See also:

•  $OERalroadTrackArcFxn$  class

## 5.5.26 OEDrawSawCircle

![](_page_258_Figure_10.jpeg)

Draws a circle with the OECircleStyle\_Saw style.

![](_page_258_Figure_12.jpeg)

Fig. 156: OEDrawSawCircle

*image* The image on which the circle is drawn.

*center* The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawSawCircle.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the circle. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawSawCircle.

**patternAngle** Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawSawCircle.

**pattern Width Ratio** Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (E) in Figure: OEDrawSawCircle.

## 5.5.27 OEDrawSawSurfaceArc

```
bool OEDrawSawSurfaceArc(OEDepict:: OEImageBase &image,
                         const OEDepict:: OE2DPoint & center,
                         double bgnAngle, double endAngle, double radius,
                         const OEDepict:: OEPen &pen, double edgeAngle=10.0,
                         unsigned int patternDirection=OEPatternDirection::Outside,
                         double patternAngle=15.0,
                         double minPatternWidthRatio=0.15,
                         double maxPatternWidthRatio=0.15)
```

Draws an arc with the OESurfaceArcStyle\_Saw style.

![](_page_259_Figure_6.jpeg)

Fig. 157: OEDrawSawSurfaceArc

*image* The image on which the arc is drawn.

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to  $3$  o'clock, etc.

*radius* The radius of the arc.

**pen** The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawSawSurfaceArc.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the arc. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawSawSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawSawSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (E) and (F) in Figure: OEDrawSawSurfaceArc.

#### • OESawArcFxn class

## 5.5.28 OEDrawSimpsonCircle

```
bool OEDrawSimpsonCircle(OEDepict:: OEImageBase &image,
                         const OEDepict:: OE2DPoint & center, double radius,
                         const OEDepict:: OEPen &pen, double patternAngle=10.0,
                         double patternWidthRatio=0.20)
```

Draws a circle with the OECircleStyle\_Simpson style.

![](_page_260_Figure_5.jpeg)

Fig. 158: OEDrawSimpsonCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawSimpsonCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawSimpsonCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawSimpsonCircle.

## 5.5.29 OEDrawSimpsonSurfaceArc

```
bool OEDrawSimpsonSurfaceArc(OEDepict:: OEImageBase &image,
                              const OEDepict:: OE2DPoint &center,
                              double bgnAngle, double endAngle, double radius,
                              const OEDepict:: OEPen &pen, double edgeAngle=10.0,
                              double patternAngle=15.0,
                              double minPatternWidthRatio=0.20,
                              double maxPatternWidthRatio=0.20)
```

Draws an arc with the OESurfaceArcStyle\_Simpson style.

*image* The image on which the arc is drawn.

*center* The center of the arc.

![](_page_261_Figure_1.jpeg)

Fig. 159: OEDrawSimpsonSurfaceArc

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

edgeAngle The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawSimpsonSurfaceArc.

**patternAngle** Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawSimpsonSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawSimpsonSurfaceArc.

#### See also:

• OESimpsonArcFxn class

## 5.5.30 OEDrawStitchCircle

![](_page_261_Figure_15.jpeg)

Draws a circle with the OECircleStyle\_Stitch style.

![](_page_261_Figure_17.jpeg)

Fig. 160: OEDrawStitchCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawStitchCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawStitchCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawStitchCircle.

## 5.5.31 OEDrawStitchSurfaceArc

```
bool OEDrawStitchSurfaceArc(OEDepict::OEImageBase &image,
                            const OEDepict:: OE2DPoint &center,
                            double bgnAngle, double endAngle, double radius,
                            const OEDepict:: OEPen &pen, double edgeAngle=10.0,
                            double patternAngle=10.0,
                            double minPatternWidthRatio=0.20,
                            double maxPatternWidthRatio=0.20)
```

Draws an arc with the OESurfaceArcStyle\_Stitch style.

![](_page_262_Figure_13.jpeg)

Fig. 161: OEDrawStitchSurfaceArc

*image* The image on which the arc is drawn.

*center* The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3 o'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawStitchSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawStitchSurfaceArc.

*minPatternWidthRatio, maxPatternWidthRatio* Specifies the width of the *pattern* of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawStitchSurfaceArc.

#### See also:

• OEStitchArcFxn class

## 5.5.32 OEDrawSunCircle

```
bool OEDrawSunCircle (OEDepict:: OEImageBase &image,
                     const OEDepict:: OE2DPoint & center, double radius,
                     const OEDepict:: OEPen &pen,
                     unsigned int patternDirection=OEPatternDirection::Outside,
                     double patternAngle=15.0, double patternWidthRatio=0.15)
```

Draws a circle with the OECircleStyle\_Sun style.

![](_page_263_Figure_9.jpeg)

Fig. 162: OEDrawSunCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawSunCircle.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the circle. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawSunCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawSunCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (E) in Figure: OEDrawSunCircle.

## 5.5.33 OEDrawSunSurfaceArc

| <b>bool</b> OEDrawSunSurfaceArc(OEDepict::OEImageBase &image, |
|---------------------------------------------------------------|
| const OEDepict::OE2DPoint &center,                            |
| double bgnAngle, double endAngle, double radius,              |
| const OEDepict::OEPen &pen, double edgeAngle=10.0,            |
| unsigned int patternDirection=OEPatternDirection::Outside,    |
| double patternAngle=15.0,                                     |
| double minPatternWidthRatio=0.15,                             |
| double maxPatternWidthRatio=0.15)                             |

Draws an arc with the OESurfaceArcStyle\_Sun style.

![](_page_264_Figure_4.jpeg)

Fig. 163: OEDrawSunSurfaceArc

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to 3  $o$ 'clock, etc.

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawSunSurfaceArc.

*patternDirection* Specifies whether the pattern is drawn inside or outside of the arc. This value has to be from the OEPatternDirection namespace.

See example (C) in Figure: OEDrawSunSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (D) in Figure: OEDrawSunSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (E) and (F) in Figure: OEDrawSunSurfaceArc.

#### See also:

• OESunArcFxn class

## 5.5.34 OEDrawWreathCircle

```
bool OEDrawWreathCircle(OEDepict::OEImageBase &image,
                        const OEDepict:: OE2DPoint &center, double radius,
                        const OEDepict:: OEPen &pen, double patternAngle=15.0,
                        double patternWidthRatio=0.20)
```

Draws a circle with the OECircleStyle\_Wreath style.

![](_page_265_Figure_4.jpeg)

Fig. 164: OEDrawWreathCircle

*image* The image on which the circle is drawn.

center The center of the circle.

*radius* The radius of the circle.

*pen* The graphical properties of the circle.

See examples (A) and (B) in Figure: OEDrawWreathCircle.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the circle. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawWreathCircle.

*pattern Width Ratio* Specifies the width of the *pattern* of the circle relative to its radius. The ratio has to be in a range of  $[0.01 - 1.00]$ .

See example (D) in Figure: OEDrawWreathCircle.

## 5.5.35 OEDrawWreathSurfaceArc

```
bool OEDrawWreathSurfaceArc(OEDepict::OEImageBase &image,
                            const OEDepict:: OE2DPoint &center,
                            double bgnAngle, double endAngle, double radius,
                            const OEDepict:: OEPen &pen, double edgeAngle=10.0,
                            double patternAngle=20.0,
                            double minPatternWidthRatio=0.15,
                            double maxPatternWidthRatio=0.15)
```

Draws an arc with the OESurfaceArcStyle\_Wreath style.

*image* The image on which the arc is drawn.

center The center of the arc.

**bgnAngle, endAngle** The two endpoints of the arc. Both angles are in degrees and their values have to be in a range of  $[0.0^{\circ} - 360.0^{\circ}]$ . Angles are interpreted such that  $0.0^{\circ}$  and  $360.0^{\circ}$  degrees are at the 12 o'clock position, 90.0° degrees corresponds to  $3$  o'clock, etc.

![](_page_266_Figure_1.jpeg)

Fig. 165: OEDrawWreathSurfaceArc

*radius* The radius of the arc.

*pen* The graphical properties of the arc.

*edgeAngle* The angle (in degrees) between the end points of the arc and the points where the *pattern* of the arc starts.

See example (B) in Figure: OEDrawWreathSurfaceArc.

*patternAngle* Specifies the angle (in degrees) between the *patterns* of the arc. The angle has to be in a range of  $[1.0^{\circ} - 90.0^{\circ}]$ 

See example (C) in Figure: OEDrawWreathSurfaceArc.

minPatternWidthRatio, maxPatternWidthRatio Specifies the width of the pattern of the arc relative to its radius. The *min* ratio is applied to the end of the arc while the *max* ratio specifies the width of the patterns at the middle of the arc. Both ratios have to be in a range of  $[0.01 - 1.00]$ .

See examples (D) and (E) in Figure: OEDrawWreathSurfaceArc.

#### See also:

• OEWreathArcFxn class

**SIX** 

# **RELEASE HISTORY**

# 6.1 Grapheme TK 1.5.2

## 6.1.1 New features

- An option has been added to the *OEColorForceFieldDisplay* to preserve input query color atoms instead of applying them from the defined color force field. There are two new methods and one new constructor, taking that argument along with the color force field.
  - SetPreserveQueryColors
  - GetPreserveQueryColors
  - Constructors

## 6.1.2 Minor bug fixes

• An issue has been fixed which incorrectly used the ligand density value for the active site density value when depicting the Iridium classification.

# 6.2 Grapheme TK 1.5.1

Minor internal improvements have been made.

# 6.3 Grapheme TK 1.5.0

Minor internal improvements have been made.

# 6.4 Grapheme TK 1.4.7

Minor internal improvements have been made.

# 6.5 Grapheme TK 1.4.6

Minor internal improvements have been made.

# 6.6 Grapheme TK 1.4.5

• Minor internal improvements have been made.

# 6.7 Grapheme TK 1.4.4

## Fall 2021

• Minor internal improvements have been made.

# 6.8 Grapheme TK 1.4.3

July 2021

## **6.8.1 New features**

• Rendering of protein-ligand binding sites has been improved to handle new intramolecule types in the OEPerceiveInteractionHints function.

# 6.9 Grapheme ™ TK 1.4.2

Fall 2020

## **6.9.1 New features**

• A new function,  $OEDrawResidues$ , has been added that visualizes residue information for peptides.

![](_page_270_Figure_1.jpeg)

#### Fig. 1: Example of using the OEDrawResidues function

## 6.9.2 Minor bug fixes

• A bug related to drawing interaction hints spanning multiple residues has been fixed.

# 6.10 Grapheme ™ TK 1.4.1

• Minor internal improvements have been made.

# 6.11 Grapheme ™ TK 1.4.0

## 6.11.1 New features

- New OEDrawIridiumData functions have been added to visualize OEIridiumData.
- A new function, OERenderActiveSite, has been added that depicts the new non-ideal hydrogen bonds. For more details about these interactions, see the OEIsNonIdealHBondInteractionHint functor.
- A new overload of OEP repareAlignedDepictionFrom3D has been added that generates 2D coordinates of a molecule driven by the 3D overlay of the shape query display object.

![](_page_271_Figure_1.jpeg)

Fig. 2: Example of visualizing Iridium data

![](_page_271_Figure_3.jpeg)

Fig. 3: Example of visualizing non-ideal hydrogen bond (PDB:1LEE)

# 6.12 Grapheme™ TK 1.3.7

## 6.12.1 New features

- The following APIs have been added to depict Ramachandran plots:
  - OERamachandranPlot class
  - OEPlotMarker class and OEPlotMarkerStyle namespace
  - OERenderRamachandranPlot function

## 6.12.2 Minor bug fixes

• OEResidueSVGStandardMarkup.GetGroupId now replaces spaces with an underscore character to generate valid SVG group IDs.

# 6.13 Grapheme™ TK 1.3.6

## 6.13.1 New features

- New OERenderBFactorMap and OEDrawBFactorMapLegend functions have been added to visualize the B-factor of a ligand and its protein environment.
- A new OEDrawUnpairedInteractionMapLegend function has been added to depict the legend of the interactions depicted in an unpaired map. (See also the OERenderUnpairedInteractionMap function).
- The OE2DActiveSiteDisplay. GetDisplayedResidues function now takes a parameter from the new OEActiveSiteRenderStyle namespace.
- OEColorGradientDisplayOptions.GetColorStopVisibility and • Two new methods, OEColorGradientDisplayOptions.SetColorStopVisibility, have been added to customize color gradient depiction.

## 6.13.2 New features (Preliminary API)

• A new OERenderActiveSiteMaps function has been added that generates an interactive image of proteinligand maps.

There is no image available for the PDF version of this book.

## 6.13.3 Major bug fixes

- When rendering ligand-protein maps with **Grapheme TK**, molecule surfaces are generated to depict the overall shape of the pocket. In the case of a large protein, this process can be both computationally expensive and can require a large amount of memory. In order to avoid these issues, only protein atoms that are no more than 20A away from any ligand atoms are now considered and the resolution of the surface is reduced.
- Rendering active site maps to an image with less than a 200.0 width or height parameter is now disabled to avoid generating very tiny, incomprehensible images.
- When rendering ligand-protein maps (e.g., active site, unpaired), interactions between the ligand and more than 1 residue is now ignored and a warning is thrown.

• Scaling of legend labels for large images has been fixed. All Grapheme TK legends of ligand-protein depictions now have a consistent style.

## 6.13.4 Minor bug fixes

- A problem that occurred when coloring hexagon glyphs representing DNA/RNA residues with more than 1 interaction type has been fixed.
- An issue with depicting an interaction type in a legend when that interaction type is missing from the corresponding active site map has been fixed.
- A small improvement has been made to help to generate residue layouts that are platform-independent.
- A small improvement has been made to generate better residue layout: the space around the ligand for potential residue positions is now better sampled to allow positioning residues close to edge of the canvas.
- The text associated with the color stops when depicting color gradients vertically using the OEDrawColorGradient function is now right-adjusted.

## **6.13.5 Documentation changes**

• The shapeoverlap2pdf.py example has been fixed.

# 6.14 Grapheme™ TK 1.3.5

## 6.14.1 New features

• A new function, OERenderUnpairedInteractionMap, has been added to visualize clash and unpaired interactions.

![](_page_273_Figure_13.jpeg)

Table 1: Examples of visualizing clash and unpaired interactions

- OERenderActiveSite now depicts covalent and cation-pi interactions.
- The style for depicting stacking interactions has been simplified.

|          | T-stacking                | Pi-stacking                |
|----------|---------------------------|----------------------------|
| 2017.Oct | Image: T-stacking diagram | Image: Pi-stacking diagram |
| 2018.Feb | Image: T-stacking diagram | Image: Pi-stacking diagram |

Table 2: Examples of stacking interaction depiction

• The color scheme used to visualize interaction types when depicting protein-ligand interactions has been updated to accommodate the two new interaction types.

![](_page_274_Figure_4.jpeg)

#### Fig. 4: New interactions color scheme

- A new method, OE2DActiveSiteDisplay. IsValid, has been added that is checked by all Grapheme TK API points.
- The OEResidueSVGStandardMarkup class now takes a separator option.
- The following API, introduced in the 2017. Jun release for marking up residue circles in SVG images generated by the OERenderActiveSite function, is no longer preliminary and is now also available in both Java and C#:
  - OEResidueSVGMarkupBase class
  - OEResidueSVGNoMarkup class
  - OEResidueSVGStandardMarkup class

## 6.14.2 Minor bug fixes

- The algorithm used by the OE2DActiveSiteDisplay function to scale and position residues around ligands has been improved.
- · OERenderActiveSite is now able to generate images when some ligand atoms have identical 2D coordinates.
- OERenderActiveSite now throws a warning if an interaction cannot be rendered.

## 6.14.3 Java-specific changes

• The API for marking up residues in SVG images is now fully supported in Java (see the list above).

## 6.14.4 C#-specific changes

• The API for marking up residues in SVG images is now fully supported in C# (see the list above).

# 6.15 Grapheme™ TK 1.3.4

## 6.15.1 New features

- The following new API has been added to customize peptide depiction:
  - *OEPeptideDisplayOptions* class
  - OEPeptideLabelStyle namespace
  - OEDrawPeptide function that takes an option class

The main feature is that  $OEDrawPeptide$  now can generate interactive SVG images where the amino acid components of the compact peptide representation are depicted on mouse-over.

- The following new API has been added to customize active site depiction:
  - OE2DActiveSiteDisplayOptions.GetSVGMagnifyResidueInHover
  - OE2DActiveSiteDisplayOptions.SetSVGMagnifyResidueInHover
  - OE2DActiveSiteDisplayOptions.GetRenderInteractiveLegend
  - OE2DActiveSiteDisplayOptions.SetRenderInteractiveLegend

These new options allow users to generate interactive SVG images when calling the OERenderActiveSite function.

- The OEBondGlyphZigZag constructor now takes a parameter that allows drawing diagonal zig-zag lines across a bond.
- OEGrapheme TK now uses the new thread-safe OEShape TK API to generate shape and color overlaps for OEShapeQueryDisplay and OEShapeOverlapDisplay classes.

![](_page_276_Figure_1.jpeg)

#### Fig. 5: Example of using the OEBondGlyphZigZag class

## 6.15.2 Minor bug fixes

. OEResidueSVGStandardMarkup.GetGroupId now returns group id for a residue that includes the insert code (see also OEResidue.GetInsertCode)

# 6.16 Grapheme™ TK 1.3.3

## 6.16.1 New features

• A new function, OERenderContactMap, has been added that generates interactive SVG images. Clicking on any residue circle will highlight those ligand atoms that interact with the given residue.

## **6.16.2 Preliminary API**

- A new Preliminary API has been added to mark up the residue circles in SVG images generated by the OERenderActiveSite function:
  - OE2DActiveSiteDisplayOptions.SetResidueSVGMarkupFunctor and OE2DActiveSiteDisplayOptions.GetResidueSVGMarkupFunctor methods
  - OEResidueSVGMarkupBase base class and OEResidueSVGNoMarkup and OEResidueSVGStandard-Markup concrete classes

## 6.16.3 Major bug fixes

- Several problems in the OERenderActiveSite function have been fixed:
  - When depicting protein-ligand interactions, grey lines represent the shape of the binding pocket. The absence of lines indicates solvent-accessible regions. In order visualize the solvent-accessible areas more realistically, waters are now ignored when calculating the molecule surfaces that determine the 2D representation (compare images below).
  - The rare case where the ligand is completely surrounded by water is now handled correctly.
  - The following heuristics are now used to improve the positioning of residue glyphs around the ligand:
    - \* Waters are more likely to be positioned in solvent-exposed regions.
    - \* Other residues are only positioned in solvent-exposed regions if it results in a more visually pleasing layout.

![](_page_277_Figure_1.jpeg)

Table 3: Example of visualizing solvent-accessible regions and water positioning (PDB: 3E3D)

## 6.16.4 Minor bug fixes

• OEDrawPeptide has been fixed and now allows only amide and disulfide bonds when identifying standard amino acids. No alpha-carbon substitutions are allowed.

![](_page_277_Figure_5.jpeg)

Table 4: Example of visualizing peptides with OEDrawPeptide

## **6.16.5 Documentation changes**

• A new Python Cookbook Examples section has been added.

# 6.17 Grapheme™ TK 1.3.2

## 6.17.1 New features

• A new function, OEDrawPeptide, has been added that identifies standard amino acid components in molecules and substitutes them with circular glyphs and corresponding labels. The figure below illustrates this functionality for oxytocin.

![](_page_278_Figure_6.jpeg)

#### Fig. 6: Example of visualizing oxytocin

(left) depiction of oxytocin highlighting its amino acid fragments (right) depiction of oxytocin using the OEDrawPeptide function

- OERenderActiveSite can now visualize halogen bond interactions (represented by a brown wavy arrow).
- The legend of the protein-ligand depiction has been improved by separating and labeling residue styles and interaction styles (see image above).

## 6.17.2 Minor bug fixes

• The label "only contact" has been changed to "contact only" in the legend of the protein-label depiction (see image above).

![](_page_279_Figure_1.jpeg)

Fig. 7: Example of visualizing halogen bond interaction (PDB 3EQB)

## 6.18 Grapheme TK 1.3.1

## 6.18.1 New features

• The algorithm that determines the position of residues around a ligand has been improved. Residues are no longer placed the same distance from the ligand but are positioned closer to the ligand atoms they interact with and farther away if they have only contact interactions with the ligand.

![](_page_279_Figure_6.jpeg)

![](_page_279_Figure_7.jpeg)

· Clash interactions perceived by the OEPerceiveInteractionHints function are now visualized when

rendering protein-ligand interactions.

![](_page_280_Figure_2.jpeg)

#### Fig. 8: Example of visualizing Clash interactions

- The color scheme used to visualize interaction types when depicting protein-ligand interactions has been updated.
  - The acceptor | donor color style no longer exists since OEPerceiveInteractionHints now perceives possible hydrogen bonding interactions between ligand and water. If no such interaction exists, the glyph representing a specific water residue will be left uncolored, indicating an only contact interaction.
  - Clash interactions are now colored dark red.

| Table 6: Color schemes                                 |                                                        |
|--------------------------------------------------------|--------------------------------------------------------|
| 2016.Jun color scheme                                  | 2016.Oct color scheme                                  |
| Image: lavender circle<br>ligand acceptor              | Image: lavender circle<br>ligand acceptor              |
| Image: pink circle<br>ligand donor                     | Image: pink circle<br>ligand donor                     |
| Image: cyan circle<br>acceptor   donor                 |                                                        |
| Image: pale orange circle<br>chelator                  | Image: pale orange circle<br>chelator                  |
| Image: white circle with black outline<br>only contact | Image: white circle with black outline<br>only contact |
| Image: green circle<br>stacking                        | Image: green circle<br>stacking                        |
| Image: blue circle<br>salt-bridge ligand+              | Image: blue circle<br>salt-bridge ligand(+)            |
| Image: dark pink circle<br>salt-bridge ligand-         | Image: dark pink circle<br>salt-bridge ligand(-)       |
|                                                        | Image: red circle outline<br>clash                     |

## 6.18.2 Minor bug fixes

• A problem that caused the glyph that represents a residue in a receptor-ligand interaction plot to be incorrectly colored based on its interaction type has been fixed.

## **6.18.3 Documentation changes**

• All images in the Grapheme TK documentation have been regenerated to reflect the changes made since the previous release.

# 6.19 Grapheme TK 1.3.0

## 6.19.1 New features

- Due to the deprecation of *OEFragmentNetwork* and related classes in **OEBio, Grapheme TK** has introduced the following overloads:
  - OEPrepareActiveSiteDepiction function has been overloaded. The new version takes an OEInteractionHintContainer object.
  - OE2DActiveSiteDisplay class now should be constructed with an OEInteractionHintContainer object.

All functions and methods using *OEFragmentNetwork* are deprecated in **Grapheme TK** and will throw a warning when called. Active site depictions generated with the deprecated API will have a "deprecated" watermark (see the example below).

![](_page_281_Figure_9.jpeg)

In order to avoid the "deprecated" watermark from appearing in the image, use

asite = OEInteractionHintContainer(protein, ligand)

#### instead of

asite = OEFragmentNetwork(protein, ligand)

#### See also:

For more details about the deprecated classes and functions, see the Deprecated OEFragmentNetwork and related API section.

- OE2DActiveSiteDisplay now can visualize salt-bridge and aromatic ring stacking interactions.
- The color scheme used to visualize different interaction types when depicting protein-ligand interaction has been changed to accommodate the new types (Pi- and T-stacking and salt-bridge).

OE2DActiveSiteDisplay.

| 2016.Feb color scheme |                 |                  | 2016.Jun color scheme |              |                     |                     |
|-----------------------|-----------------|------------------|-----------------------|--------------|---------------------|---------------------|
| ligand acceptor       | ligand donor    | acceptor & donor | ligand acceptor       | ligand donor | acceptor   donor    | chelator            |
| acceptor   donor      | ligand chelator | contact          | only contact          | stacking     | salt-bridge ligand+ | salt-bridge ligand- |

- · OE2DActiveSiteDisplay.GetDisplayedLigand and GetDisplayedResidues methods have been added.
- . OEAddLigandHighlighting and OEAddResidueHighlighting functions have been added to allow highlighting in active site depiction. See the example below.

![](_page_282_Figure_4.jpeg)

Fig. 9: Example of ligand highlighting

- OEShapeOverlapDisplayStyle\_PropertyCloud style has been added to visualize shape overlays along with the following APIs:
  - OEShapeOverlapDisplayStylenamespace
  - OEShapeOverlapDisplayOptions.SetOverlapDisplayStyle OEShapeOverlapDisplayOptions.SetOverlapDisplayStylemethods

and

Using this new style can result in a 10-times performance increase when generating shape overlay images; the generated images will also be significantly smaller (PNG 50%, SVG 60-times, PDF 9-times).

- The following APIs have been added to identify ligand atoms and bonds, along with residues of an OE2DActiveSiteDisplay object that are close to a given 2D display coordinate:
  - OEGetNearestAtom and OEGetNearbyAtom functions
  - OEGetNearestBond and OEGetNearbyBond functions
  - OEGetNearestResidue and OEGetNearbyResidue functions along with the OENearestResidue class

![](_page_283_Picture_1.jpeg)

#### Fig. 10: Example of visualizing shape overlaps with PropertyCloud style

## **6.19.2 Documentation changes**

- All images in the Grapheme TK documentation were automatically regenerated to reflect the changes made since the previous release.
- The example in *Depicting Active Site Interactions* has been updated to use the new OEInteractionHintContainer class instead of the deprecated OEFragmentNetwork.

# 6.20 Grapheme TK 1.2.3

## 6.20.1 Minor bug fixes

• Minor internal improvements have been made.

## **6.20.2 Documentation changes**

• The *Depicting BFactor* has been updated to perceive residues when necessary.

# 6.21 Grapheme TK 1.2.2

## 6.21.1 New features

- OEDrawROCSScores function has been added to visualize scores.
- OEAlignedDepictionFrom3DOptions has been added  $\overline{\mathbf{t}}$ allow more customization of the OEPrepareAlignedDepictionFrom3D function.
- · OEShapeQueryDisplayOptions.GetDepictOrientationandOEShapeQueryDisplayOptions. SetDepictOrientation methods have been added to allow the shape query to orient horizontal, vertical, or square.
- . OEShapeQueryDisplay.GetTitle and OEShapeOverlapDisplay.GetTitle methods were added to access the title of the objects.

![](_page_284_Figure_1.jpeg)

- · OEShapeQueryDisplay. IsValid and OEShapeOverlapDisplay. IsValid methods were added to determine whether the objects have been initialized correctly.
- OERenderShapeOverlap function has been overloaded to enable rendering of shape overlap into two images: one image containing the fit molecule with transparent background and the other image showing the property map of the shape overlap. By superimposing the two images (molecule image on top), the result would be similar to visualizing the shape overlay in one image.
- OE2DActiveSiteDisplay class was rewritten to use the new implementation of the OEBio::OEFragmentNetwork class.

## 6.21.2 Major bug fixes

• OEPrepareDepictionFrom3D function has been improved to use a better scoring function in cases of atom clashes.

## 6.21.3 Minor bug fixes

- The default parameter for the maximum number of bond rotations of the OEDepictionFrom3DOptions class is now  $2^{16} = 65536$ . This means that by default only the first 16 single bonds of molecule will be rotated to find the "closest" 2D layout from the original 3D conformation when invoking the OEP repareDepictionFrom3D function.
- OEShapeOverlapDisplay now limits the maximum number of bond rotations to  $2^{14} = 16384$  when calling the OEPrepareAlignedDepictionFrom3D function to generate 2D coordinates aligned to the query molecule. This limit provides a reasonable trade-off between speed and the quality of the alignments.
- OEPrepareDepictionFrom3D and OEPrepareAlignedDepictionFrom3D have been optimized to be 10% faster on average. The algorithms were also revised to reduce the accumulation of floating point errors.
- Constructing OEShapeQueryDisplay and OEShapeOverlapDisplay objects is now significantly faster due to code optimization and constraining the 2D layout generations.
- OERenderActiveSite function was fixed to depict the OEResidueIndex\_I residue with the DNA/RNA style.
- OEShapeOverlapDisplay and OEShapeOverlapDisplay now can handle queries without any color atoms.
- OERenderShapeQuery and OERenderColorOverlap now scale the line width of the pens used to render the circles representing color atom matches.
- OEP repareDepictionFrom3D can now handle molecules containing atoms with an unknown atomic number (PDB examples: 1S9R, 3KXA, 1I1W).

- OEGetMoleculeSurfaceScale has been improved to capitalize on the molecule layout enhancements done in OEDepict TK in this release.
- OERenderColorOverlap was fixed to render the molecule surface of the query molecule as OERenderShapeOverlap does.

## **6.21.4 Documentation changes**

- The Depicting Shape and Color Atom Overlaps example has been updated to visualize shape and color atom scores.
- The Depicting Active Site Interactions and Depicting BFactor examples have been updated to perceive residues in cases when it is not done by the molecule reader (for example, in the case of  $mod 2$ ).
- All images in this documentation have been automatically regenerated to reflect the changes made since the previous release.

## **6.22 Grapheme TK 1.2.1**

## 6.22.1 Major bug fixes

• OEPrepareDepictionFrom3D has been optimized to be twice as fast on average.

## **6.22.2 Documentation changes**

- The following examples have been updated to use OESplitMolComplex for separating the ligand and protein:
  - $-$  bfactor2img example
  - $-$  complex2img example
- All images in this documentation were automatically regenerated to reflect the changes made since the previous release.

## **6.23 Grapheme TK 1.2.0**

## 6.23.1 New features

- The following classes and functions have been added for visualizing ligand-receptor interactions:
  - OE2DActiveSiteDisplay class
  - OE2DActiveSiteDisplayOptions class
  - OE2DActiveSiteLegendDisplayOptions class
  - OEPrepareActiveSiteDepictionfunction
  - OERenderActiveSite function
  - OEDrawActiveSiteLegend function
- A new Grapheme TK example that visualizes receptor-ligand interactions has been added. For more details, see the Depicting Active Site Interactions section.

## 6.23.2 Major bug fixes

• When generating a 2D layout from a 3D conformation by using the OEPrepareDepictionFrom3D function, the configuration of the amide bonds are now always respected.

| Grapheme TK version 1.1.3                         |                              | Grapheme TK version 1.2.0                         |
|---------------------------------------------------|------------------------------|---------------------------------------------------|
| Image: 2D chemical structure (Grapheme TK v1.1.3) | Image: 3D chemical structure | Image: 2D chemical structure (Grapheme TK v1.2.0) |

Table 7: Example of generating a 2D layout from a 3D conformation

## 6.23.3 Minor bug fixes

· The memory leak has been fixed and a check has been added to prevent division-by-zero in the OEAddComplexSurfaceArcs function.

## **6.23.4 Documentation changes**

- All images in this documentation were automatically regenerated to reflect the changes made since the previous release.
- More C# examples have been added.

# 6.24 Grapheme TK 1.1.3

## 6.24.1 New features

- OEGet2DSurfaceArcs now has a radius scale parameter that allows the radii of the arcs to be easily scaled to different sizes.
- OEGet2DSurfaceArcs now allows the generation of molecule surfaces with a different radius for every atom. See Listing 5 in Drawing a Molecule Surface chapter.
- The following classes do not require a valid Shape TK license any longer.
  - OEColorForceFieldDisplay class
  - OEShapeQueryDisplay class
  - $-$  OEShapeOverlapDisplay class

## 6.24.2 Major bug fixes

• When atom clashes are checked during the molecule alignment of the OEPrepareAlignedDepictionFrom3D function, every atom is now considered not just the heavy atoms.

## 6.24.3 Minor bug fixes

- OEShapeOverlapDisplay, OEShapeOueryDisplay, OERenderColorOverlap, OERenderShapeOverlap will no longer crash when dealing with improperly initialized objects.
- OEPrepareDepictionFrom3D performance has been improved.
- OEP repareDepictionFrom3D will now just alter coordinates in-place, and not invalidate all OEA tomBase and OEBondBase pointers.
- Added parameter checks to the OEAddComplexSurfaceArcs function

## **6.24.4 Documentation changes**

• All images in this documentation were automatically regenerated to reflect the changes made since the previous release.

# 6.25 Grapheme TK 1.1.2

## 6.25.1 New features

- Added OEBondGlyphZigZag and OEBondGlyphStitch bond annotation classes.
- Added the following methods to control the color of the property map generated by OERenderShapeOverlap:
  - OEShapeOverlapDisplayOptions.GetOverlapColor
  - OEShapeOverlapDisplayOptions.SetOverlapColor
- The maximum number of bond rotations performed by  $OEPrepareDepictionFrom3D$  when 2D depiction coordinates are generated based on 3D can be controlled by the following methods:
  - OEDepictionFrom3DOptions.GetMaxBondRotations
  - OEDepictionFrom3DOptions.SetMaxBondRotations

## 6.25.2 Major bug fixes

- The following classes and functions were made thread safe:
  - $-$  OEShapeOueryDisplay
  - OERenderShapeQuery
  - OEShapeOverlapDisplay
  - OERenderShapeOverlap
  - OERenderColorOverlap

These functions were introduced in 2013.Oct and were not thread safe for the 2013.Oct and 2014.Feb releases.

## **6.25.3 Documentation changes**

- All images were automatically regenerated to reflect the changes made since the previous release.
- Multiple examples migrated to the OpenEye Python Cookbook.

# 6.26 Grapheme TK 1.1.1

## 6.26.1 New features

• Added the following setter and getter methods that control whether a background color is cleared prior to rendering. This allows to generate an image with transparent background.

| - OEShapeQueryDisplayOptions.GetClearBackground<br>OEShapeQueryDisplayOptions.SetClearBackground     | and |
|------------------------------------------------------------------------------------------------------|-----|
| - OEShapeOverlapDisplayOptions.GetClearBackground<br>OEShapeOverlapDisplayOptions.SetClearBackground | and |
| - OEColorOverlapDisplayOptions.GetClearBackground<br>OEColorOverlapDisplayOptions.SetClearBackground | and |

## 6.26.2 Minor bug fixes

- OEDepict TK symbols are no longer imported along with the oegrapheme module.
- Added "BRIEF" line to interfaces of Grapheme TK examples.

## **6.26.3 Documentation changes**

- Added example of drawing multiple 2D surfaces in the Drawing a Molecule Surface chapter.
- All images were automatically regenerated to reflect the changes made since the previous release.

# **6.27 Grapheme TK 1.1.0**

## 6.27.1 New features

- Added the following to visualize color forcefields:
  - OEColorForceFieldDisplay
  - OEColorForceFieldLegendDisplayOptions
  - OEDrawColorForceFieldLegend
- Added the following to visualize the reference molecule of a color and shape overlap:
  - $-$  OEShapeOverlapDisplay
  - OEShapeOverlapDisplayOptions

- OERenderShapeOuery
- Added the following to visualize shape and color overlaps:
  - OEShapeOverlapDisplay
  - OEShapeOverlapDisplayOptions
  - OERenderShapeOverlap
  - OEColorOverlapDisplayOptions
  - OERenderColorOverlap

**Note:** A valid **shape** license is required to use any of these new shape or color APIs.

- Added the OEDepiction From 3DO ptions class that allows more advanced customization of the generation of 2D coordinates driven by the 3D conformation when calling the OEP repareDepictionFrom3D function. By default, OEPrepareDepictionFrom3D is tuned for generating 2D coordinates for representing 3D overlays in 2D. This class allows the 2D coordinate generation to choose a set of 2D coordinates that are much closer to how the molecule would look in a 3D viewer.
- Added the following to render user-defined labels when depicting color gradients:
  - OEColorGradientDisplayOptions.AddLabel
  - OEColorGradientDisplayOptions.ClearLabels
  - OEColorGradientDisplayOptions.GetLabels
- Added OEColorGradientDisplayOptions. ClearBoxRange method to remove the box range previously set to a color gradient.
- Added OEGet2DSurfaceArcs function to return the arcs of the molecule surface of a specific atom with the given radius. Varying radii can be passed to generate multiple surfaces in the range specified by the OESurfaceArcScale namespace. OEGetMoleculeSurfaceScale can be used to determine the appropriate scale for the molecule with the specified radius.
- Implemented the shapeoverlap2pdf.py Python Grapheme TK example.

## 6.27.2 Major bug fixes

• Molecule surface arcs inside macrocycles are no longer returned. See the effect of this change in Table: Example of depicting molecule surface.

![](_page_290_Figure_3.jpeg)

Table 8: Example of depicting molecule surface

## **6.27.3 Documentation changes**

• All images were automatically regenerated to reflect the changes made since the previous release.

## **6.28 Grapheme TK 1.0.6**

## 6.28.1 New features

- OEPrepareAlignedDepictionFrom3D performance improvement of 10% on average.
- The OE2DPropMap class now allows rendering bond properties along with atom ones. See examples in the Table: Depicting atom or/and bond properties.
- Implemented the bfactor2img.py Python Grapheme TK example.

## 6.28.2 Major bug fixes

- The OEDrawColorGradient functions now takes an OEColorGradientBase object allowing to depict the following color gradients derived from the OEColorGradientBase base class:
  - OEExponentColorGradient
  - OEExponentialColorGradient
  - OELinearColorGradient
  - OELogarithmicColorGradient

## 6.28.3 Minor bug fixes

- Using a pen with miter line join in order to make the transition between grid cells smoother when rendering the property map by the OE2DPropMap. Render method.
- The OE2DPropMap. SetResolution lower limit has been reduced from 2 to 1. Using resolution 1 will result in a very smooth property grid, however it significantly increase the size of vector images (such as . pdf and  $.py$ s).

## **6.28.4 Documentation changes**

- Importing the following OESystem classes from the OEChem TK documentation.
  - OEColor
  - OEColorGradientBase
  - OEColorStop
  - OEExponentColorGradient
  - OEExponentialColorGradient
  - OELinearColorGradient
  - OELogarithmicColorGradient
- All images were automatically regenerated to reflect the changes made since the previous release.

# **6.29 Grapheme TK 1.0.5**

## 6.29.1 New features

- Added the following methods to the OEColorGradientDisplayOptions class that allow the customization of the gradient visualization.
  - OEColorGradientDisplayOptions. SetBoxRange and OEColorGradientDisplayOptions. SetBoxRangePen

| - OEColorGradientDisplayOptions.SetMarkedValuePen     | and |
|-------------------------------------------------------|-----|
| OEColorGradientDisplayOptions.SetMarkedValuePrecision |     |
| - OEColorGradientDisplayOptions.AddMarkedValues       | and |

OEColorGradientDisplayOptions.SetMarkedValues - OEColorGradientDisplayOptions.SetColorStopLabelFontScale • Added the OEBondGlyphCross and the OEBondGlyphScissors bond glyphs.

# **6.30 Grapheme TK 1.0.4**

## 6.30.1 New features

• OEDrawColorGradient function and OEColorGradientDisplayOptions class added to visualize color gradients.

## 6.30.2 Major bug fixes

• OEPrepareAlignedDepictionFrom3D improved to produce better alignments in many cases.

## 6.30.3 Minor bug fixes

- OEPrepareDepictionFrom3D improved to produce 2D coordinates that align better with the input 3D coordinates.
- *OE2DPropMap* default background color changed from a very light grey to pure white.

See the effect of this change in Table: Example of depicting a property map.

![](_page_292_Figure_11.jpeg)

Table 9: Example of depicting a property map

## **6.30.4 Documentation changes**

• All images were automatically regenerated to reflect the changes made since the previous release.

# 6.31 Grapheme TK 1.0.3

## 6.31.1 New features

- OEBondGlyphCurvedArrow added as a new bond annotation style.
- · OE2DPropMap. GetLegendFont and OE2DPropMap. GetLegendFontScale methods added in order to customize the legend font of the property map.

## 6.31.2 Minor bug fixes

- OE2DPropMap legend layout improved.
- OE2DPropMap will now display at least one decimal number when rendering the value of the linear color gradient of the class.
- OE2DPropMap will now set the line width of the box around the linear color gradient to the default bond line width of the molecule.
- Increased the line width of the following complex arc styles: OEDefaultSolventArcFxn, OEDefaultCavityArcFxn, and OEDefaultVoidArcFxn.
- Atoms that are not visible are now not considered for the minimum and maximum range of the linear color gradient.
- Fixed cases where the property value of adjacent atoms had opposite signs and the colors were not blurred smoothly by increasing the size of the box used to blur the values.
- · OEDraw2DSurface and OEAddGlyph will  $no$ longer crash due  $\mathbf{t}$ the Swig::DirectorTypeMismatchException C++ exception being thrown. A Python RuntimeError exception will now be thrown instead indicating that the call nethods of the class deriving from OESurfaceArcFxnBase, OEAtomGlyphBase, or OEBondGlyphBase needs to return a boolean value.

## **6.31.3 Documentation changes**

• All images were automatically regenerated to reflect the changes made since the previous release.

# **6.32 Grapheme TK 1.0.2**

## 6.32.1 Minor bug fix

• Avoiding extraneous runtime warnings from OEDrawPearlsCircle and OEDrawFlowerCircle when the pen's fill is turned off.

## **6.32.2 Documentation changes**

- Some examples and images were updated in order to consistently use red and blue color for representing negative and positive values respectively when using the OELinearColorGradient class.
- All images in this manual are now automatically generated as part of the release process and tested against benchmark images on all supported platforms.

# **6.33 Grapheme TK 1.0.1**

## 6.33.1 Minor bug fixes

• Scaling the fonts of the legend of the OE2DPropMap class based upon the scale of the OE2DMolDisplay object.

# **6.34 Grapheme TK 1.0.0**

## 6.34.1 New features

- Providing a mechanism to annotate atoms and bonds in the depicted molecule (see also Annotating Atoms and *Bonds* chapter)
- Implementing the OEAtomGlyphCircle atom annotation style and allowing user-defined styles that derive from the OEAtomGlyphBase abstract class
- Implementing the OEBondGlyphArrow and the OEBondGlyphBase bond annotation styles and allowing userdefined styles that derive from the: OEBondGlyphBase abstract class
- Adding 18 default circle drawing styles (*OECircleStyle*) that can be customized (see for example the OEDrawCastleCircle function)
- Adding 17 default arc drawing styles (OESurfaceArcStyle) that can be customized (see for example the OEDrawCastleSurfaceArcfunction)
- Adding the OE2DPropMap class that generates a 2D grid of user-defined atom properties (see Depicting Atom Property Map chapter).
- Adding functions that automatically generate standard interfaces for *Grapheme* applications (see OEConfigure2DPropMap and OESetup2DPropMap functions)
- Adding the OEPrepareDepictionFrom3D and the OEPrepareAlignedDepictionFrom3D functions in which the generation of the 2D coordinates of a molecule is driven by a given 3D reference molecule.
- Drawing molecule surfaces OEDraw2DSurface (see Drawing Molecule Surface chapter)
- Providing 18 built-in surface drawing styles and allowing to the implementation of user-defined ones.
- Drawing complex molecule surfaces where the distance between the ligand and the receptor is projected into the 2D molecule surface (OEAddComplexSurfaceArcs) Implementing the four default styles for drawing complex surfaces (OEDefaultBuriedArcFxn, OEDefaultCavityArcFxn, OEDefaultSolventArcFxn and OEDefault-VoidArcFxn) and handling user-defined ones (see Drawing Ligand-Protein Complex Surface chapter).

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
-Fe, NM. http://www.eyesopen.com.
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

**TEN** 

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project                 | Website                                                                             | Licen                                                                       |
|---------------------------------|-------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| abseil-cpp                      | https://github.com/abseil/abseil-cpp                                                | https:/                                                                     |
| absl-py                         | https://github.com/abseil/abseil-py                                                 | https:/                                                                     |
| aiohttp                         | https://docs.aiohttp.org/en/stable/                                                 | https:/                                                                     |
| aiosignal                       | https://github.com/aio-libs/aiosignal                                               | https:/                                                                     |
| Amazon Linux 2                  | https://aws.amazon.com/amazon-linux-2                                               | N/A                                                                         |
| AmberUtils                      | http://ambermd.org                                                                  | N/A                                                                         |
| ambit                           | https://github.com/khimaros/ambit                                                   | https:/                                                                     |
| amqp                            | https://github.com/celery/py-amqp                                                   | https:/                                                                     |
| anaconda-anon-usage             | Orion Floes                                                                         | https:/                                                                     |
| angular                         | https://github.com/angular/angular.js                                               | https:/                                                                     |
| angular-animate                 | https://github.com/angular/angular.js                                               | https:/                                                                     |
| angular-cache                   | https://github.com/jmdobry/angular-cache                                            | https:/                                                                     |
| angular-cookies                 | https://github.com/angular/angular.js                                               | https:/                                                                     |
| angular-loggly-logger           | https://github.com/ajbrown/angular-loggly-logger                                    | https:/                                                                     |
| angular-mocks                   | https://github.com/angular/angular.js                                               | https:/                                                                     |
| angular-resource                | https://github.com/angular/angular.js                                               | https:/                                                                     |
| angular-toggle-switch           | https://github.com/cgarvis/angular-toggle-switch                                    | https:/                                                                     |
| angular-ui-grid                 | https://github.com/angular-ui/ui-grid                                               | https:/                                                                     |
| angular-ui-router               | https://github.com/angular-ui/ui-router                                             | https:/                                                                     |
| angular-ui-tree                 | https://github.com/angular-ui-tree/angular-ui-tree                                  | https:/                                                                     |
| angular-vs-repeat               | https://github.com/kamilkp/angular-vs-repeat                                        | https:/                                                                     |
| aniso8601                       | https://bitbucket.org/nielsenb/aniso8601                                            | https:/                                                                     |
| annotated-types                 | https://github.com/annotated-types/annotated-types                                  | https:/                                                                     |
| anyio                           | https://github.com/agronholm/anyio                                                  | https:/                                                                     |
| appdirs                         | http://github.com/ActiveState/appdirs                                               | http://                                                                     |
| appengine                       | https://google.golang.org/appengine                                                 | https:/                                                                     |
| arabic-reshaper                 | https://github.com/mpcabd/python-arabic-reshaper/                                   | https:/                                                                     |
| archspec                        | https://github.com/archspec/archspec/blob/master/README.md                          | https:/                                                                     |
| Name of Project                 | Website                                                                             | License                                                                     |
| argon2-cffi                     | https://github.com/hynek/argon2-cffi                                                | https://github.com/hynek/argon2-cffi/blob/master/LICENSE                    |
| argon2-cffi-bindings            | https://github.com/hynek/argon2-cffi-bindings                                       | https://github.com/hynek/argon2-cffi-bindings/blob/master/LICENSE           |
| arpack                          | https://www.caam.rice.edu/software/ARPACK/                                          | https://www.caam.rice.edu/software/ARPACK/license                           |
| ascii85                         | https://github.com/huandu/node-ascii85                                              | https://github.com/huandu/node-ascii85/blob/master/LICENSE                  |
| ase                             | https://wiki.fysik.dtu.dk/ase/                                                      | https://wiki.fysik.dtu.dk/ase/LICENSE                                       |
| asgiref                         | https://github.com/django/asgiref/                                                  | https://github.com/django/asgiref/blob/master/LICENSE                       |
| asn1crypto                      | https://github.com/wbond/asn1crypto                                                 | https://github.com/wbond/asn1crypto/blob/master/LICENSE                     |
| assertions go-render            | https://github.com/smartystreets/assertions/internal/go-render/render               | https://github.com/smartystreets/assertions/blob/master/LICENSE             |
| assertions oglmatchers          | https://github.com/smartystreets/assertions/internal/oglematchers                   | https://github.com/smartystreets/assertions/blob/master/LICENSE             |
| assertions                      | https://github.com/smartystreets/assertions                                         | https://github.com/smartystreets/assertions/blob/master/LICENSE             |
| asttokens                       | https://github.com/gristlabs/asttokens                                              | https://github.com/gristlabs/asttokens/blob/master/LICENSE                  |
| astunparse                      | https://github.com/simonpercivall/astunparse                                        | https://github.com/simonpercivall/astunparse/blob/master/LICENSE            |
| async-lru                       | https://github.com/aio-libs/async-lru                                               | https://github.com/aio-libs/async-lru/blob/master/LICENSE                   |
| async-timeout                   | https://github.com/aio-libs/async-timeout                                           | https://github.com/aio-libs/async-timeout/blob/master/LICENSE               |
| atk-1.0                         | https://docs.gtk.org/atk/                                                           | https://docs.gtk.org/atk/license.html                                       |
| atomic                          | https://github.com/uber-go/atomic                                                   | https://github.com/uber-go/atomic/blob/master/LICENSE                       |
| atomicwrites                    | https://github.com/untitaker/python-atomicwrites                                    | https://github.com/untitaker/python-atomicwrites/blob/master/LICENSE        |
| attrs                           | https://www.attrs.org/                                                              | https://github.com/python-attrs/attrs/blob/master/LICENSE                   |
| aws-sdk-go                      | https://github.com/aws/aws-sdk-go                                                   | https://github.com/aws/aws-sdk-go/blob/master/LICENSE.txt                   |
| Babel                           | https://github.com/python-babel/babel                                               | https://github.com/python-babel/babel/blob/master/LICENSE                   |
| backcall                        | https://github.com/takluyver/backcall                                               | https://github.com/takluyver/backcall/blob/master/LICENSE                   |
| backports                       | https://github.com/brandon-rhodes/backports                                         | https://github.com/brandon-rhodes/backports/blob/master/LICENSE             |
| backports.functools-lru-cache   | https://github.com/jaraco/backports.functools_lru_cache                             | https://github.com/jaraco/backports.functools_lru_cache/blob/master/LICENSE |
| base62                          | https://github.com/kare/base62                                                      | https://github.com/kare/base62/blob/master/LICENSE                          |
| beautifulsoup4                  | https://www.crummy.com/software/BeautifulSoup/                                      | https://www.crummy.com/software/BeautifulSoup/LICENSE                       |
| billiard                        | https://github.com/celery/billiard                                                  | https://github.com/celery/billiard/blob/master/LICENSE                      |
| biopython                       | https://biopython.org                                                               | https://github.com/biopython/biopython/blob/master/LICENSE.rst              |
| biotite                         | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https://github.com/biotite-dev/biotite/blob/master/LICENSE                  |
| bitset                          | https://github.com/willf/bitset                                                     | https://github.com/willf/bitset/blob/master/LICENSE                         |
| blas                            | https://www.netlib.org/blas/                                                        | https://www.netlib.org/blas/blas-license.txt                                |
| bleach                          | https://github.com/mozilla/bleach                                                   | https://github.com/mozilla/bleach/blob/master/LICENSE                       |
| blessings                       | https://github.com/erikrose/blessings                                               | https://github.com/erikrose/blessings/blob/master/LICENSE                   |
| blinker                         | https://pythonhosted.org/blinker/                                                   | https://github.com/pallets-eco/blinker/blob/master/LICENSE                  |
| blosc                           | https://github.com/Blosc/python-blosc                                               | https://github.com/Blosc/python-blosc/blob/master/LICENSES/License.txt      |
| blosc2                          | https://github.com/Blosc/python-blosc2                                              | https://github.com/Blosc/python-blosc2/blob/master/LICENSES/License.txt     |
| boltons                         | https://github.com/mahmoud/boltons                                                  | https://github.com/mahmoud/boltons/blob/master/LICENSE.txt                  |
| boost                           | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://www.boost.org/users/license.html                                    |
| boost-cpp                       | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://www.boost.org/users/license.html                                    |
| bootstrap-vue                   | https://github.com/bootstrap-vue/bootstrap-vue                                      | https://github.com/bootstrap-vue/bootstrap-vue/blob/dev/LICENSE             |
| boto3                           | https://github.com/boto/boto3                                                       | https://github.com/boto/boto3/blob/develop/LICENSE                          |
| botocore                        | https://github.com/boto/botocore                                                    | https://github.com/boto/botocore/blob/develop/LICENSE.txt                   |
| Bottleneck                      | https://bottleneck.readthedocs.io/en/latest/index.html                              | https://github.com/pydata/bottleneck/blob/master/LICENSE.txt                |
| Brotli                          | https://github.com/google/brotli                                                    | https://github.com/google/brotli/blob/master/LICENSE                        |
| brotli-bin                      | https://github.com/google/brotli                                                    | https://github.com/google/brotli/blob/master/LICENSE                        |
| brotli-python                   | http://python-hyper.org/projects/brotlipy/en/latest/                                | https://github.com/python-hyper/brotlipy/blob/master/LICENSE                |
| brotlipy                        | https://github.com/python-hyper/brotlicffi                                          | https://github.com/python-hyper/brotlicffi/blob/master/LICENSE              |
| bson                            | http://github.com/py-bson/bson                                                      | http://github.com/py-bson/bson/blob/master/LICENSE                          |
| bytefmt                         | https://code.cloudfoundry.org/bytefmt                                               | https://github.com/cloudfoundry/bytefmt/blob/master/LICENSE                 |
| bzip2                           | https://www.bzip.org                                                                | https://www.bzip.org/license.html                                           |
|                                 |                                                                                     | J)                                                                          |
| Name of Project                 | Website                                                                             | Licen                                                                       |
| c-ares                          | https://github.com/c-ares/c-ares                                                    | https:/                                                                     |
| ca-certificates                 | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/                                                                     |
| cached-property                 | https://github.com/pydanny/cached-property                                          | https:/                                                                     |
| cachetools                      | https://github.com/tkem/cachetools/                                                 | https:/                                                                     |
| cairo                           | https://pycairo.readthedocs.io/en/latest/                                           | https:/                                                                     |
| canvas                          | https://github.com/Automattic/node-canvas                                           | https:/                                                                     |
| cctbx                           | https://github.com/cctbx/cctbx_project                                              | https:/                                                                     |
| celery                          | https://github.com/celery/celery                                                    | https:/                                                                     |
| Cerberus                        | https://docs.python-cerberus.org/en/stable/                                         | https:/                                                                     |
| certifi                         | https://certifiio.readthedocs.io/en/latest/                                         | https:/                                                                     |
| $\overline{\text{cffi}}$        | https://github.com/python-cffi                                                      | https:/                                                                     |
| cftime                          | https://pypi.org/project/cftime/                                                    | https:/                                                                     |
| chardet                         | https://github.com/chardet/chardet                                                  | https:/                                                                     |
| charset-normalizer              | https://github.com/ousret/charset_normalizer                                        | https:/                                                                     |
| chunkreader                     | https://github.com/jackc/chunkreader/v2                                             | https:/                                                                     |
| click                           | https://palletsprojects.com/p/click/                                                | https:/                                                                     |
| click-completion                | https://github.com/click-contrib/click-completion                                   | https:/                                                                     |
| click-didyoumean                | https://github.com/click-contrib/click-didyoumean                                   | https:/                                                                     |
| click-plugins                   | https://github.com/click-contrib/click-plugins                                      | https:/                                                                     |
| click-repl                      | https://github.com/untitaker/click-repl                                             |                                                                             |
| cloudpickle                     | https://github.com/cloudpipe/cloudpickle                                            | https:/                                                                     |
| cmake                           | https://cmake.org/                                                                  | https:/                                                                     |
| colorama                        | https://github.com/tartley/colorama                                                 | https:/                                                                     |
|                                 |                                                                                     | https:/                                                                     |
| comm                            | https://github.com/ipython/comm                                                     | https:/                                                                     |
| compose                         | https://github.com/docker/compose                                                   | https:/                                                                     |
| conda-content-trust             | https://github.com/conda/conda-content-trust                                        | https:/                                                                     |
| conda-libmamba-solver           | https://github.com/conda/conda-libmamba-solver                                      | https:/                                                                     |
| conda-package-handling          | https://github.com/conda/conda-package-handling                                     | https:/                                                                     |
| conda-package-streaming         | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/                                                                     |
| conda-token                     | https://anaconda.org/anaconda/conda-token                                           | https:/                                                                     |
| confuse                         | https://github.com/beetbox/confuse                                                  | https:/                                                                     |
| contourpy                       | https://github.com/contourpy/contourpy                                              | https:/                                                                     |
| cpp-peglib                      | https://github.com/yhirose/cpp-peglib                                               | https:/                                                                     |
| cryptography                    | https://github.com/pyca/cryptography                                                | https:/                                                                     |
| cssselect2                      | https://github.com/Kozea/cssselect2/                                                | https:/                                                                     |
| cudatoolkit                     | https://developer.nvidia.com/cuda-toolkit                                           | https:/                                                                     |
| $cupy-cuda113$                  | https://cupy.dev/                                                                   | https:/                                                                     |
| curl                            | https://curl.se                                                                     | https:/                                                                     |
| cycler                          | https://github.com/matplotlib/cycler                                                | https:/                                                                     |
| cyrus-sasl                      | https://github.com/cyrusimap/cyrus-sasl                                             | https:/                                                                     |
| Cython                          | https://cython.org                                                                  | https:/                                                                     |
| $\overline{d3}$                 | https://github.com/mbostock/d3                                                      | https:/                                                                     |
| dataclasses                     | https://github.com/ericvsmith/dataclasses                                           | https:/                                                                     |
| ddsketch                        | http://github.com/datadog/sketches-py                                               | https:/                                                                     |
| debugpy                         | https://aka.ms/debugpy                                                              | https:/                                                                     |
| decimal                         | https://github.com/shopspring/decimal                                               | https:/                                                                     |
| decorator                       | https://github.com/micheles/decorator                                               | https:/                                                                     |
| deepdiff                        | https://github.com/seperman/deepdiff                                                | https:/                                                                     |
| deeptime                        | https://github.com/deeptime-ml/deeptime                                             | https:/                                                                     |
|                                 |                                                                                     |                                                                             |
|                                 |                                                                                     | L                                                                           |
| Name of Project                 | Website                                                                             | Licen                                                                       |
| defusedxml                      | https://github.com/tiran/defusedxml                                                 | https:/                                                                     |
| $di$ <sup><math>11</math></sup> | https://github.com/uqfoundation/dill                                                | https:/                                                                     |
| distro                          | <b>Orion Floes</b>                                                                  | https:/                                                                     |
| Django                          | https://www.djangoproject.com/                                                      | https:/                                                                     |
| django-classy-tags              | https://github.com/django-cms/django-classy-tags                                    | https:/                                                                     |
| django-cors-headers             | https://github.com/adamchainz/django-cors-headers                                   | https:/                                                                     |
| django-csp                      | https://github.com/mozilla/django-csp                                               | https:/                                                                     |
| django-extensions               | https://github.com/django-extensions/django-extensions                              | https:/                                                                     |
| django-filter                   | https://github.com/carltongibson/django-filter/tree/master                          | https:/                                                                     |
| django-redis                    | https://github.com/jazzband/django-redis                                            | https:/                                                                     |
| django-taggit                   | https://github.com/jazzband/django-taggit                                           | https:/                                                                     |
| django-taggit-serializer        | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/                                                                     |
| django-taggit-templatetags2     | https://github.com/fizista/django-taggit-templatetags2                              | https:/                                                                     |
| djangorestframework             | https://www.django-rest-framework.org/                                              | https:/                                                                     |
| dkh                             | https://psicode.org/psi4manual/master/dkh.html                                      | https:/                                                                     |
| dm-tree                         | https://github.com/deepmind/tree                                                    | https:/                                                                     |
| docker-py                       | https://github.com/docker/docker-py/                                                | https:/                                                                     |
| docopt                          | https://docopt.org                                                                  | https:/                                                                     |
| docutils                        | https://docutils.sourceforge.io                                                     | https:/                                                                     |
| drf-dynamic-fields              | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/                                                                     |
| editdistance                    | https://github.com/roy-ht/editdistance                                              | https:/                                                                     |
| eigen                           | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/                                                                     |
| einops                          | https://github.com/arogozhnikov/einops                                              |                                                                             |
|                                 | https://github.com/takluyver/entrypoints                                            | https:/                                                                     |
| entrypoints                     | https://github.com/pkg/errors                                                       | https:/                                                                     |
| errors                          | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                                     |
| eslint-plugin                   |                                                                                     | https:/                                                                     |
| et_xmlfile                      | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/                                                                     |
| exceptiongroup                  | https://github.com/agronholm/exceptiongroup                                         | https:/                                                                     |
| executing                       | https://github.com/alexmojaki/executing                                             | https:/                                                                     |
| expat                           | https://libexpat.github.io                                                          | https:/                                                                     |
| fastjsonschema                  | https://github.com/horejsek/python-fastjsonschema                                   | https:/                                                                     |
| fastrlock                       | https://github.com/scoder/fastrlock                                                 | https:/                                                                     |
| fftw                            | https://www.fftw.org                                                                | comm                                                                        |
| filebuffer                      | https://github.com/mattetti/filebuffer                                              | https:/                                                                     |
| filelock                        | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/                                                                     |
| finufft                         | https://github.com/flatironinstitute/finufft                                        | https:/                                                                     |
| Flask                           | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/                                                                     |
| flatbuffers                     | https://google.github.io/flatbuffers/                                               | https:/                                                                     |
| flit-core                       | https://github.com/pypa/flit                                                        | https:/                                                                     |
| <b>FLTK</b>                     | https://www.fltk.org/index.php                                                      | https:/                                                                     |
| fmt                             | https://fmt.dev/latest/index.html                                                   | https:/                                                                     |
| font-awesome                    | https://github.com/FortAwesome/Font-Awesome                                         | https:/                                                                     |
| font-ttf-dejavu-sans-mono       | https://dejavu-fonts.github.io                                                      | https:/                                                                     |
| font-ttf-inconsolata            | https://fonts.google.com/specimen/Inconsolata                                       | https:/                                                                     |
| font-ttf-source-code-pro        | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/                                                                     |
| font-ttf-ubuntu                 | https://fonts.google.com/specimen/Ubuntu                                            | https:/                                                                     |
| fontconfig                      | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/                                                                     |
| fonts-conda-ecosystem           | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/                                                                     |
| fonts-conda-forge               | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/                                                                     |
| Name of Project                 | Website                                                                             | License                                                                     |
| fonttools                       | https://github.com/fonttools/fonttools                                              |                                                                             |
| freetype                        | https://freetype.org                                                                |                                                                             |
| fribidi                         | https://github.com/fribidi/fribidi                                                  |                                                                             |
| frozendict                      | Orion Floes                                                                         |                                                                             |
| frozenlist                      | https://github.com/aio-libs/frozenlist                                              |                                                                             |
| fsmlite                         | https://github.com/tkem/fsmlite                                                     |                                                                             |
| fsspec                          | https://github.com/fsspec/filesystem_spec                                           |                                                                             |
| funcy                           | https://github.com/Suor/funcy                                                       |                                                                             |
| gast                            | https://github.com/serge-sans-paille/gast/                                          |                                                                             |
| gau2grid                        | https://github.com/dgasmith/gau2grid                                                |                                                                             |
| gax-go                          | https://github.com/googleapis/gax-go/v2                                             |                                                                             |
| gdk-pixbuf                      | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           |                                                                             |
| gemmi                           | https://gemmi.readthedocs.io/en/latest/                                             |                                                                             |
| genproto                        | https://google.golang.org/genproto/googleapis                                       |                                                                             |
| geometric                       | https://openbase.com/python/geometric                                               |                                                                             |
| giflib                          | https://giflib.sourceforge.net                                                      |                                                                             |
| glib                            | https://docs.gtk.org/glib/                                                          |                                                                             |
| GLM Library                     | https://github.com/g-truc/glm                                                       |                                                                             |
| gls                             | https://github.com/jtolds/gls                                                       |                                                                             |
| go-cleanhttp                    | https://github.com/hashicorp/go-cleanhttp                                           |                                                                             |
| go-connections                  | https://github.com/docker/go-connections                                            |                                                                             |
| go-cpio                         | https://github.com/cavaliercoder/go-cpio                                            |                                                                             |
| go-getter                       | https://github.com/hashicorp/go-getter                                              |                                                                             |
| go-homedir                      | https://github.com/mitchellh/go-homedir                                             |                                                                             |
| go-ini                          | https://github.com/go-ini/ini                                                       |                                                                             |
| go-jmespath                     | https://github.com/jmespath/go-jmespath                                             |                                                                             |
| go-junit-report                 | https://github.com/jstemmer/go-junit-report                                         |                                                                             |
| go-netrc                        | https://github.com/bgentry/go-netrc/netrc                                           |                                                                             |
| go-ole                          | https://github.com/go-ole/go-ole                                                    |                                                                             |
| go-pg                           | https://github.com/go-pg/pg                                                         |                                                                             |
| go-redis                        | https://github.com/go-redis/redis/v8                                                |                                                                             |
| go-rendezvous                   | https://github.com/dgryski/go-rendezvous                                            |                                                                             |
| go-safetemp                     | https://github.com/hashicorp/go-safetemp                                            |                                                                             |
| go-sysconf                      | https://github.com/tklauser/go-sysconf                                              |                                                                             |
| go-testing-interface            | https://github.com/mitchellh/go-testing-interface                                   |                                                                             |
| go-units                        | https://github.com/docker/go-units                                                  |                                                                             |
| go-version                      | https://github.com/hashicorp/go-version                                             |                                                                             |
| go-zglob                        | https://github.com/mattn/go-zglob                                                   |                                                                             |
| go.opencensus                   | https://go.opencensus.io                                                            |                                                                             |
| gobrake.v2                      | https://gopkg.in/airbrake/gobrake.v2                                                |                                                                             |
| goconvey                        | https://github.com/smartystreets/goconvey                                           |                                                                             |
| golden-layout                   | https://github.com/deepstreamIO/golden-layout                                       |                                                                             |
| google-auth                     | https://google-auth.readthedocs.io/en/master/                                       |                                                                             |
| google-auth-oauthlib            | https://github.com/googleapis/google-auth-library-python-oauthlib                   |                                                                             |
| google-cloud-go                 | https://cloud.google.com/go                                                         |                                                                             |
| google-cloud-go/storage         | https://cloud.google.com/go/storage                                                 |                                                                             |
| google-pasta                    | https://github.com/google/pasta                                                     |                                                                             |
| google.golang.org/api           | https://google.golang.org/api                                                       |                                                                             |
| gopsutil                        | https://github.com/shirou/gopsutil                                                  |                                                                             |
| Name of Project                 | Website                                                                             | License                                                                     |
| gorilla websocket               | https://github.com/gorilla/websocket                                                | https:/                                                                     |
| graphite2                       | https://github.com/silnrsi/graphite                                                 | https:/                                                                     |
| graphviz                        | https://graphviz.org/                                                               | https:/                                                                     |
| greenlet                        | https://greenlet.readthedocs.io/en/latest/                                          | https:/                                                                     |
| groupcache                      | https://github.com/golang/groupcache                                                | https:/                                                                     |
| grpc                            | https://google.golang.org/grpc                                                      | https:/                                                                     |
| grpc-cpp                        | https://github.com/grpc/grpc                                                        | https:/                                                                     |
| grpcio                          | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/                                                                     |
| gtk2                            | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/                                                                     |
| gts                             | https://sourceforge.net/projects/gts/                                               | https:/                                                                     |
| h5py                            | https://www.h5py.org                                                                | https:/                                                                     |
| harfbuzz                        | https://github.com/harfbuzz/harfbuzz                                                | https:/                                                                     |
| hdbscan                         | https://hdbscan.readthedocs.io/en/latest/                                           | https:/                                                                     |
| hdf4                            | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/                                                                     |
| hdf5                            | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/                                                                     |
| he                              | https://github.com/mathiasbynens/he                                                 | https:/                                                                     |
| html-loader                     | https://github.com/webpack-contrib/html-loader                                      | https:/                                                                     |
| html5lib                        | https://github.com/html5lib/html5lib-python                                         | https:/                                                                     |
| htslib                          | https://www.htslib.org                                                              | https:/                                                                     |
| humanize                        | https://github.com/jmoiron/humanize                                                 | https:/                                                                     |
| icu                             | https://github.com/unicode-org/icu                                                  | https:/                                                                     |
| idna                            | https://github.com/kjd/idna                                                         | https:/                                                                     |
| imageio                         | https://github.com/imageio/imageio                                                  | https:/                                                                     |
| imagesize                       | https://github.com/shibukawa/imagesize_py                                           | https:/                                                                     |
| ImmuneBuilder                   | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/                                                                     |
| importlib-metadata              | https://github.com/python/importlib_metadata                                        | https:/                                                                     |
| importlib_resources             | https://github.com/python/importlib_resources                                       | https:/                                                                     |
| InChI                           | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/                                                                     |
| inflection                      | https://github.com/jinzhu/inflection                                                | https:/                                                                     |
| ini.v1                          | https://gopkg.in/ini.v1                                                             | https:/                                                                     |
| iniconfig                       | https://github.com/pytest-dev/iniconfig                                             | https:/                                                                     |
| innersvg-polyfill               | https://github.com/dnozay/innersvg-polyfill                                         | https:/                                                                     |
| intel-openmp                    | https://github.com/hermitcore/libomp_oss                                            | https:/                                                                     |
| ipykernel                       | https://ipython.org                                                                 | https:/                                                                     |
| ipython                         | https://ipython.org                                                                 | https:/                                                                     |
| ipython-genutils                | http://ipython.org                                                                  | https:/                                                                     |
| ipywidgets                      | http://jupyter.org                                                                  | https:/                                                                     |
| isodate                         | https://github.com/gweis/isodate/                                                   | https:/                                                                     |
| itsdangerous                    | https://palletsprojects.com/p/itsdangerous/                                         | https:/                                                                     |
| jax                             | https://github.com/google/jax                                                       | https:/                                                                     |
| jaxlib                          | https://github.com/google/jax                                                       | https:/                                                                     |
| jedi                            | https://jedi.readthedocs.io/en/latest/                                              | https:/                                                                     |
| Jinja2                          | https://palletsprojects.com/p/jinja/                                                | https:/                                                                     |
| jmespath                        | https://github.com/jmespath/jmespath.py                                             | https:/                                                                     |
| joblib                          | https://joblib.readthedocs.io/en/latest/                                            | https:/                                                                     |
| jpeg                            | https://www.ijg.org                                                                 | https:/                                                                     |
| json5                           | https://github.com/dpranke/pyjson5                                                  | https:/                                                                     |
| jsonfield                       | https://github.com/dmkoch/django-jsonfield/                                         | https:/                                                                     |
| jsonpatch                       | https://github.com/stefankoegl/python-json-patch                                    | https:/                                                                     |
| Name of Project                 | Website                                                                             | License                                                                     |
| jsonpickle                      | https://github.com/jsonpickle/jsonpickle                                            | https:/                                                                     |
| jsonpointer                     | https://github.com/stefankoegl/python-json-pointer                                  | https:/                                                                     |
| jsonschema                      | https://github.com/python-jsonschema/jsonschema                                     | https:/                                                                     |
| jsonschema-specifications       | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:/                                                                     |
| jstat                           | https://github.com/jstat/jstat                                                      | https:/                                                                     |
| jupyter-client                  | https://jupyter.org                                                                 | https:/                                                                     |
| jupyter-core                    | https://jupyter.org                                                                 | https:/                                                                     |
| jupyter-events                  | https://github.com/jupyter/jupyter_events                                           | https:/                                                                     |
| jupyter-lsp                     | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:/                                                                     |
| jupyter-server                  | http://jupyter.org                                                                  | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE          |
| jupyterlab                      | https://github.com/jupyterlab/jupyterlab                                            | https:/                                                                     |
| jupyterlab-pygments             | http://jupyter.org                                                                  | https:/                                                                     |
| jupyterlab-widgets              | http://jupyter.org                                                                  | https:/                                                                     |
| jupyterlab_server               | https://github.com/jupyterlab/jupyterlab_server                                     | https:/                                                                     |
| jupyter_client                  | http://jupyter.org                                                                  | https:/                                                                     |
| jupyter_core                    | http://jupyter.org                                                                  | https:/                                                                     |
| jupyter_server                  | https://github.com/jupyter-server/jupyter_server                                    | https:/                                                                     |
| jupyter_server_terminals        | https://github.com/jupyter-server/jupyter_server_terminals                          | https:/                                                                     |
| kaleido                         | https://github.com/plotly/Kaleido                                                   | https:/                                                                     |
| keras                           | https://github.com/keras-team/keras                                                 | https:/                                                                     |
| Keras-Preprocessing             | https://github.com/keras-team/keras-preprocessing                                   | https:/                                                                     |
| keras-tuner                     | https://github.com/keras-team/keras-tuner                                           | https:/                                                                     |
| keyring                         | https://github.com/jaraco/keyring                                                   | https:/                                                                     |
| keyutils                        | https://github.com/sassoftware/python-keyutils                                      | https:/                                                                     |
| kiwisolver                      | https://kiwisolver.readthedocs.io/en/latest/                                        | https:/                                                                     |
| kombu                           | https://kombu.readthedocs.io                                                        | https:/                                                                     |
| krb5                            | https://web.mit.edu/kerberos/                                                       | https:/                                                                     |
| kt-legacy                       | https://github.com/haifeng-jin/kt-legacy                                            | https:/                                                                     |
| lazy_loader                     | https://github.com/scientific-python/lazy_loader                                    | https:/                                                                     |
| lcms2                           | https://www.littlecms.com                                                           | https:/                                                                     |
| lerc                            | https://github.com/Esri/lerc                                                        | https:/                                                                     |
| libarchive                      | http://www.libarchive.org                                                           | https:/                                                                     |
| libblas                         | https://www.netlib.org/blas/                                                        | https:/                                                                     |
| libbrotlicommon                 | https://github.com/google/brotli                                                    | https:/                                                                     |
| libbrotlidec                    | https://github.com/google/brotli                                                    | https:/                                                                     |
| libbrotlienc                    | https://github.com/google/brotli                                                    | https:/                                                                     |
| libcblas                        | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                         |
| libclang                        | <b>Orion Floes</b>                                                                  | https:/                                                                     |
| libcurl                         | https://curl.se/libcurl/                                                            | https:/                                                                     |
| libcxx                          | https://github.com/llvm-mirror/libcxx                                               | https:/                                                                     |
| libdb                           | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:/                                                                     |
| libdeflate                      | https://github.com/ebiggers/libdeflate                                              | https:/                                                                     |
| libedit                         | https://thrysoee.dk/editline/                                                       | http://                                                                     |
| libev                           | https://software.schmorp.de/pkg/libev.html                                          | https:/                                                                     |
| libffi                          | https://github.com/libffi/libffi                                                    | https:/                                                                     |
| libgcrypt                       | https://gnupg.org/software/index.html                                               | https:/                                                                     |
| libgd                           | https://libgd.github.io                                                             | https:/                                                                     |
| libglib                         | https://github.com/PolMine/libglib                                                  | https:/                                                                     |
| libiconv                        | https://www.gnu.org/software/libiconv/                                              | https:/                                                                     |
| Name of Project                 | Website                                                                             | License                                                                     |
| libint                          | https://tinyurl.com/yvw97wbw                                                        |                                                                             |
| liblapack                       | http://www.netlib.org/lapack/                                                       |                                                                             |
| liblapacke                      | https://anaconda.org/conda-forge/liblapacke                                         |                                                                             |
| libmamba                        | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     |                                                                             |
| libmambapy                      | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                |                                                                             |
| libnetcdf                       | https://www.unidata.ucar.edu/software/netcdf/                                       |                                                                             |
| libnghttp2                      | https://github.com/nghttp2/nghttp2                                                  |                                                                             |
| libopenblas                     | https://www.openblas.net/                                                           |                                                                             |
| libpng                          | https://www.libpng.org/pub/png/libpng.html                                          |                                                                             |
| libpq                           | https://www.postgresql.org/                                                         |                                                                             |
| librsvg                         | https://gitlab.gnome.org/GNOME/librsvg                                              |                                                                             |
| libsolv                         | https://github.com/openSUSE/libsolv                                                 |                                                                             |
| libssh2                         | https://github.com/libssh2/libssh2                                                  |                                                                             |
| libtiff                         | https://www.libtiff.org/                                                            |                                                                             |
| libtrust                        | https://github.com/docker/libtrust                                                  |                                                                             |
| libuuid                         | https://sourceforge.net/projects/libuuid/                                           |                                                                             |
| libuv                           | https://github.com/libuv/libuv                                                      |                                                                             |
| libwebp                         | https://chromium.googlesource.com/webm/libwebp                                      |                                                                             |
| libwebp-base                    | https://chromium.googlesource.com/webm/libwebp                                      |                                                                             |
| libxc                           | https://www.tddft.org/programs/libxc/                                               |                                                                             |
| libxcb                          | https://xcb.freedesktop.org/                                                        |                                                                             |
| libxml2                         | https://git.gnome.org/browse/libxml2/                                               |                                                                             |
| libxmlsec1                      | https://github.com/lsh123/xmlsec                                                    |                                                                             |
| libxslt                         | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 |                                                                             |
| libzlib                         | https://zlib.net/                                                                   |                                                                             |
| lime                            | https://github.com/marcotcr/lime                                                    |                                                                             |
| lit                             | http://llvm.org                                                                     |                                                                             |
| llvm-openmp                     | https://github.com/llvm-mirror/openmp                                               |                                                                             |
| llvmlite                        | http://llvmlite.readthedocs.io                                                      |                                                                             |
| loader-utils                    | https://github.com/webpack/loader-utils                                             |                                                                             |
| logomaker                       | https://logomaker.readthedocs.io/en/latest/                                         |                                                                             |
| logrus                          | https://github.com/sirupsen/logrus                                                  |                                                                             |
| logrus-airbrake-hook.v2         | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  |                                                                             |
| lxml                            | https://lxml.de/                                                                    |                                                                             |
| lz4-c                           | https://www.lz4.org/                                                                |                                                                             |
| markdown                        | https://github.com/evilstreak/markdown-js                                           |                                                                             |
| markdown-it-py                  | https://github.com/executablebooks/markdown-it-py                                   |                                                                             |
| MarkupSafe                      | https://palletsprojects.com/p/markupsafe/                                           |                                                                             |
| matplotlib                      | https://matplotlib.org/                                                             |                                                                             |
| matplotlib-base                 | https://matplotlib.org/                                                             |                                                                             |
| matplotlib-inline               | https://github.com/ipython/matplotlib-inline                                        |                                                                             |
| mda-xdrlib                      | https://github.com/MDAnalysis/mda-xdrlib                                            |                                                                             |
| mdtraj                          | https://www.mdtraj.org/                                                             |                                                                             |
| mdurl                           | https://github.com/executablebooks/mdurl                                            |                                                                             |
| menuinst                        | https://github.com/ContinuumIO/menuinst                                             |                                                                             |
| mergo                           | https://github.com/imdario/mergo                                                    |                                                                             |
| mistune                         | https://github.com/lepture/mistune                                                  |                                                                             |
| mkl                             | https://github.com/rust-math/intel-mkl-src                                          |                                                                             |
| mkl-fft                         | https://github.com/IntelPython/mkl_fft                                              |                                                                             |
| Name of Project                 | Website                                                                             | Licen                                                                       |
| mkl-random                      | https://github.com/IntelPython/mkl_random                                           | https:/                                                                     |
| mkl-service                     | https://github.com/IntelPython/mkl-service                                          | https:/                                                                     |
| ml-dtypes                       | <b>Orion Floes</b>                                                                  | https:/                                                                     |
| molecupy                        | https://molecupy.readthedocs.io/en/latest/                                          | https:/                                                                     |
| moment                          | https://github.com/moment/moment                                                    | https:/                                                                     |
| moment-precise-range-plugin     | https://github.com/codebox/moment-precise-range                                     | https:/                                                                     |
| more-itertools                  | https://github.com/more-itertools/more-itertools                                    | https:/                                                                     |
| mpiplus                         | https://github.com/choderalab/mpiplus                                               | https:/                                                                     |
| mpmath                          | http://mpmath.org/                                                                  | https:/                                                                     |
| mrcfile                         | https://github.com/ccpem/mrcfile                                                    | https:/                                                                     |
| msgpack                         | https://msgpack.org/                                                                | https:/                                                                     |
| multidict                       | https://github.com/aio-libs/multidict                                               | https:/                                                                     |
| multierr                        | https://go.uber.org/multierr                                                        | https:/                                                                     |
| multiprocess                    | https://github.com/uqfoundation/multiprocess                                        | https:/                                                                     |
| munkres                         | https://software.clapper.org/munkres/                                               | https:/                                                                     |
| myesui uuid                     | https://github.com/myesui/uuid                                                      | https:/                                                                     |
| namex                           | <b>Orion Floes</b>                                                                  | https:/                                                                     |
| nbclassic                       | http://jupyter.org                                                                  | https:/                                                                     |
| nbclient                        | https://jupyter.org                                                                 | https:/                                                                     |
| nbconvert                       | https://jupyter.org                                                                 | https:/                                                                     |
| nbformat                        | http://jupyter.org                                                                  | https:/                                                                     |
| ncurses                         | https://invisible-island.net/ncurses/                                               | https:/                                                                     |
| nest-asyncio                    | https://github.com/erdewit/nest_asyncio                                             | https:/                                                                     |
| netcdf-fortran                  | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                                     |
| netCDF4                         | http://github.com/Unidata/netcdf4-python                                            | https:/                                                                     |
| nettle                          | https://git.lysator.liu.se/nettle/nettle                                            | https:/                                                                     |
| networkx                        | https://networkx.org                                                                | https:/                                                                     |
| nfpm                            | https://github.com/goreleaser/nfpm                                                  | https:/                                                                     |
| ng-tags-input                   | https://github.com/mbenford/ngTagsInput                                             | https:/                                                                     |
| ng-toast                        | https://github.com/tameraydin/ngToast                                               | https:/                                                                     |
| ngdraggable                     | https://github.com/fatlinesofcode/ngDraggable                                       | https:/                                                                     |
| ngVue                           | https://github.com/ngVue/ngVue                                                      | https:/                                                                     |
| nlopt                           | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/                                                                     |
| nodejs                          | https://nodejs.org/en/                                                              |                                                                             |
| nomkl                           | https://github.com/conda-forge/nomkl-feedstock                                      | https:/                                                                     |
| notebook                        | http://jupyter.org                                                                  | https:/                                                                     |
| notebook-shim                   | https://github.com/jupyter/notebook_shim                                            | https:/                                                                     |
| notebook_shim                   | http://jupyter.org                                                                  | https:/                                                                     |
| numba                           | https://numba.pydata.org                                                            |                                                                             |
| numcpus                         | https://github.com/tklauser/numcpus                                                 | https:/                                                                     |
| numexpr                         | https://github.com/pydata/numexpr                                                   | https:/                                                                     |
| numpy                           | https://numpy.org                                                                   | https:/                                                                     |
| numpy-base                      | https://numpy.org                                                                   | https:/                                                                     |
| numpydoc                        | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/                                                                     |
| nvidia-cublas-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                     |
| nvidia-cublas-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                     |
| nvidia-cuda-cupti-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                     |
| nvidia-cuda-cupti-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                     |
| nvidia-cuda-nvrtc-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                                     |
| Name of Project                 | Website                                                                             | License                                                                     |
| nvidia-cuda-nvrtc-cu12          | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cuda-runtime-cu11        | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cuda-runtime-cu12        | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cudnn-cu11               | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cudnn-cu12               | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cufft-cu11               | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cufft-cu12               | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-curand-cu11              | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-curand-cu12              | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cusolver-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cusolver-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cusparse-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-cusparse-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-nccl-cu11                | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-nccl-cu12                | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-nvjitlink-cu12           | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-nvtx-cu11                | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| nvidia-nvtx-cu12                | https://developer.nvidia.com/cuda-zone                                              | https://developer.nvidia.com/cuda-zone                                      |
| Oat++                           | https://oatpp.io/                                                                   | https://oatpp.io/                                                           |
| oauthlib                        | https://github.com/oauthlib/oauthlib                                                | https://github.com/oauthlib/oauthlib                                        |
| ocl-icd                         | https://github.com/OCL-dev/ocl-icd                                                  | https://github.com/OCL-dev/ocl-icd                                          |
| ocl-icd-system                  | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https://github.com/conda-forge/ocl-icd-system-feedstock                     |
| olefile                         | https://www.decalage.info/python/olefileio                                          | https://www.decalage.info/python/olefileio                                  |
| OmegaFold                       | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https://github.com/HeliXonProtein/OmegaFold/tree/main                       |
| omnicanvas                      | https://omnicanvas.readthedocs.io/en/latest/                                        | https://omnicanvas.readthedocs.io/en/latest/                                |
| OpenFF                          | https://openforcefield.org/                                                         | https://openforcefield.org/                                                 |
| openff-amber-ff-ports           | https://github.com/openforcefield/openff-amber-ff-ports                             | https://github.com/openforcefield/openff-amber-ff-ports                     |
| openff-forcefields              | https://openforcefield.org                                                          | https://openforcefield.org                                                  |
| openff-interchange              | https://github.com/openforcefield/openff-interchange                                | https://github.com/openforcefield/openff-interchange                        |
| openff-models                   | https://github.com/openforcefield/openff-models                                     | https://github.com/openforcefield/openff-models                             |
| openff-toolkit                  | https://openforcefield.org                                                          | https://openforcefield.org                                                  |
| openff-toolkit-base             | https://openforcefield.org                                                          | https://openforcefield.org                                                  |
| openff-units                    | https://github.com/openforcefield/openff-units                                      | https://github.com/openforcefield/openff-units                              |
| openff-utilities                | https://github.com/openforcefield/openff-utilities                                  | https://github.com/openforcefield/openff-utilities                          |
| openjpeg                        | https://github.com/uclouvain/openjpeg                                               | https://github.com/uclouvain/openjpeg                                       |
| openldap                        | https://www.openldap.org/software/repo.html                                         | https://www.openldap.org/software/repo.html                                 |
| OpenMM                          | https://openmm.org                                                                  | https://openmm.org                                                          |
| openmmtools                     | https://github.com/choderalab/openmmtools                                           | https://github.com/choderalab/openmmtools                                   |
| openmoltools                    | https://github.com/choderalab/openmoltools                                          | https://github.com/choderalab/openmoltools                                  |
| openpyxl                        | https://openpyxl.readthedocs.io/en/stable/                                          | https://openpyxl.readthedocs.io/en/stable/                                  |
| openssl                         | https://www.openssl.org                                                             | https://www.openssl.org                                                     |
| opt-einsum                      | https://github.com/dgasmith/opt_einsum                                              | https://github.com/dgasmith/opt_einsum                                      |
| OptKing                         | https://github.com/psi-rking/optking                                                | https://github.com/psi-rking/optking                                        |
| oscrypto                        | https://github.com/wbond/oscrypto                                                   | https://github.com/wbond/oscrypto                                           |
| overrides                       | https://github.com/mkorpela/overrides                                               | https://github.com/mkorpela/overrides                                       |
| packaging                       | https://github.com/pypa/packaging                                                   | https://github.com/pypa/packaging                                           |
| packmol                         | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                       |
| pandas                          | https://pandas.pydata.org                                                           | https://pandas.pydata.org                                                   |
| pandocfilters                   | http://github.com/jgm/pandocfilters                                                 | http://github.com/jgm/pandocfilters                                         |
| Name of Project                 | Website                                                                             | License                                                                     |
| panedr                          | https://github.com/MDAnalysis/panedr                                                | https://                                                                    |
| pango                           | https://pango.gnome.org                                                             | https://                                                                    |
| ParmEd                          | https://parmed.github.io/ParmEd/html/index.html                                     | https://                                                                    |
| parser                          | https://github.com/typescript-eslint/typescript-eslint                              | https://                                                                    |
| parso                           | https://parso.readthedocs.io/en/latest/                                             | https://                                                                    |
| pathos                          | https://github.com/uqfoundation/pathos                                              | https://                                                                    |
| patsy                           | https://patsy.readthedocs.io/en/latest/                                             | https://                                                                    |
| pbkdf2                          | https://golang.org/x/crypto/pbkdf2                                                  | https://                                                                    |
| pbr                             | https://docs.openstack.org/pbr/latest/                                              | https://                                                                    |
| pcmsolver                       | https://pcmsolver.readthedocs.io/en/stable/                                         | https://                                                                    |
| pcre                            | https://www.pcre.org                                                                | https://                                                                    |
| pcre2                           | https://www.pcre.org                                                                | https://                                                                    |
| pdb4amber                       | https://github.com/Amber-MD/pdb4amber                                               | https://                                                                    |
| pdbfixer                        | https://github.com/openmm/pdbfixer                                                  | https://                                                                    |
| pexpect                         | https://pexpect.readthedocs.io/                                                     | https://                                                                    |
| pgconn                          | https://github.com/jackc/pgconn                                                     | https://                                                                    |
| pgio                            | https://github.com/jackc/pgio                                                       | https://                                                                    |
| pgpassfile                      | https://github.com/jackc/pgpassfile                                                 | https://                                                                    |
| pgproto3                        | https://github.com/jackc/pgproto3/v2                                                | https://                                                                    |
| pgtype                          | https://github.com/jackc/pgtype                                                     | https://                                                                    |
| pgx                             | https://github.com/jackc/pgx/v4                                                     | https://                                                                    |
| phonopy                         | https://github.com/phonopy/phono3py                                                 | https://                                                                    |
| pickleshare                     | https://github.com/pickleshare/pickleshare                                          | https://                                                                    |
| Pillow                          | https://python-pillow.org                                                           | https://                                                                    |
| Pint                            | https://pint.readthedocs.io/en/stable/                                              | https://                                                                    |
| pip                             | https://pip.pypa.io/                                                                | https://                                                                    |
| pip-licenses                    | https://github.com/raimon49/pip-licenses                                            | https://                                                                    |
| pixman                          | https://pixman.org                                                                  | https://                                                                    |
| pkginfo                         | https://launchpad.net/pkginfo                                                       | https://                                                                    |
| platformdirs                    | https://github.com/platformdirs/platformdirs                                        | https://                                                                    |
| plotly                          | https://plotly.com/python/                                                          | https://                                                                    |
| plotly-orca                     | https://github.com/plotly/orca                                                      | https://                                                                    |
| plotly.js                       | https://github.com/plotly/plotly.js                                                 | https://                                                                    |
| pluggy                          | https://pluggy.readthedocs.io/en/stable/index.html                                  | https://                                                                    |
| pooch                           | https://github.com/fatiando/pooch                                                   | https://                                                                    |
| pox                             | https://github.com/uqfoundation/pox                                                 | https://                                                                    |
| ppft                            | https://github.com/uqfoundation/ppft                                                | https://                                                                    |
| pq                              | https://github.com/lib/pq                                                           | https://                                                                    |
| ProDy                           | http://www.csb.pitt.edu/ProDy                                                       | https://                                                                    |
| prometheus-client               | https://github.com/prometheus/client_python                                         | https://                                                                    |
| prompt-toolkit                  | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https://                                                                    |
| protobuf                        | https://google.golang.org/protobuf                                                  | https://                                                                    |
| psi4                            | https://psicode.org                                                                 | https://                                                                    |
| psutil                          | https://psutil.readthedocs.io/en/latest/                                            | https://                                                                    |
| psycopg2                        | https://psycopg.org/                                                                | https://                                                                    |
| PTable                          | https://github.com/kxxoling/PTable                                                  | https://                                                                    |
| pthread-stubs                   | https://xcb.freedesktop.org                                                         | https://                                                                    |
| ptyprocess                      | https://ptyprocess.readthedocs.io/en/latest/                                        | https://                                                                    |
| pure-eval                       | http://github.com/alexmojaki/pure_eval                                              | http://                                                                     |
|                                 |                                                                                     | J)                                                                          |
| Name of Project                 | Website                                                                             | Licen                                                                       |
| pу                              | https://py.readthedocs.io/en/latest/                                                | https:/                                                                     |
| py-cpuinfo                      | https://github.com/workhorsy/py-cpuinfo                                             | https:/                                                                     |
| pyasn1                          | https://github.com/etingof/pyasn1                                                   | https:/                                                                     |
| pyasn1-modules                  | https://github.com/etingof/pyasn1-modules                                           | https:/                                                                     |
| pybind11-abi                    | https://github.com/pybind/pybind11                                                  | https:/                                                                     |
| pycairo                         | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/                                                                     |
| pycosat                         | https://github.com/conda/pycosat                                                    | https:/                                                                     |
| pycparser                       | https://github.com/eliben/pycparser                                                 | https:/                                                                     |
| pydantic                        | https://pydantic-docs.helpmanual.io                                                 | https:/                                                                     |
| pydantic-core                   | https://github.com/pydantic/pydantic-core                                           | https:/                                                                     |
| pyedr                           | https://github.com/MDAnalysis/panedr                                                | https:/                                                                     |
| pyEMMA                          | http://github.com/markovmodel/PyEMMA                                                | https:/                                                                     |
| Pygments                        | https://pygments.org                                                                | https:/                                                                     |
| pygraphviz                      | https://pygraphviz.github.io                                                        | https:/                                                                     |
| pygtop                          | https://pygtop.readthedocs.io/en/latest/                                            | https:/                                                                     |
| pyHanko                         | https://github.com/MatthiasValvekens/pyHanko                                        | https:/                                                                     |
| pyhanko-certvalidator           | https://github.com/MatthiasValvekens/certvalidator                                  | https:/                                                                     |
| PyJWT                           | https://github.com/jpadilla/pyjwt                                                   | https:/                                                                     |
| pymbar                          | https://pymbar.org                                                                  | https:/                                                                     |
| pyOpenSSL                       | https://pyopenssl.org/                                                              | https:/                                                                     |
| pyparsing                       | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/                                                                     |
| PyPDF3                          | https://github.com/sfneal/PyPDF3                                                    | https:/                                                                     |
| pyrsistent                      | http://github.com/tobgu/pyrsistent/                                                 | https:/                                                                     |
| pysam                           | https://github.com/pysam-developers/pysam                                           | https:/                                                                     |
| PySocks                         | https://github.com/Anorov/PySocks                                                   | https:/                                                                     |
| pytables                        | https://www.pytables.org                                                            | https:/                                                                     |
| python                          | https://www.python.org/                                                             | https:/                                                                     |
| python-bidi                     | https://github.com/MeirKriheli/python-bidi                                          | https:/                                                                     |
| python-constraint               | https://github.com/python-constraint/python-constraint                              | https:/                                                                     |
| python-dateutil                 | https://dateutil.readthedocs.io                                                     | https:/                                                                     |
| python-json-logger              | http://github.com/madzak/python-json-logger                                         | https:/                                                                     |
| python-Idap                     | https://www.python-ldap.org/                                                        | https:/                                                                     |
| python3-saml                    | https://github.com/onelogin/python3-saml                                            | https:/                                                                     |
| python_abi                      | https://github.com/conda-forge/python_abi-feedstock                                 | https:/                                                                     |
| pytz                            | https://pythonhosted.org/pytz                                                       | https:/                                                                     |
| pytz-deprecation-shim           | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/                                                                     |
| PyWavelets                      | https://github.com/PyWavelets/pywt                                                  | https:/                                                                     |
| <b>PyYAML</b>                   | https://pyyaml.org/                                                                 | https:/                                                                     |
| pyyml                           | No longer available                                                                 | No lor                                                                      |
| pyzmq                           | https://pyzmq.readthedocs.io/en/latest/                                             | https:/                                                                     |
| qcelemental                     | https://github.com/MolSSI/QCElemental                                               | https:/                                                                     |
| qcengine                        | https://github.com/MolSSI/QCEngine                                                  | https:/                                                                     |
| qrcode                          | https://github.com/lincolnloop/python-qrcode                                        | https:/                                                                     |
| ramda                           | https://github.com/ramda/ramda                                                      | https:/                                                                     |
| rapidjson                       | https://rapidjson.org/                                                              | https:/                                                                     |
| rdkit                           | https://www.rdkit.org                                                               | https:/                                                                     |
| re2                             | https://github.com/google/re2                                                       | https:/                                                                     |
| readme-renderer                 | https://github.com/pypa/readme_renderer                                             | https:/                                                                     |
| redis-py                        | https://github.com/andymccurdy/redis-py                                             | https:/                                                                     |
|                                 |                                                                                     |                                                                             |
| Name of Project                 | Website                                                                             | License                                                                     |
| referencing                     | https://github.com/python-jsonschema/referencing                                    | https://                                                                    |
| regex                           | https://github.com/mrabarnett/mrab-regex                                            | https://                                                                    |
| reportlab                       | https://www.reportlab.com                                                           | https://                                                                    |
| reproc                          | https://github.com/DaanDeMeyer/reproc                                               | https://                                                                    |
| reproc-cpp                      | https://github.com/DaanDeMeyer/reproc                                               | https://                                                                    |
| requests                        | https://requests.readthedocs.io                                                     | https://                                                                    |
| requests-oauthlib               | https://github.com/requests/requests-oauthlib                                       | https://                                                                    |
| requests-toolbelt               | https://toolbelt.readthedocs.org                                                    | https://                                                                    |
| resumable                       | https://github.com/stevvooe/resumable                                               | https://                                                                    |
| retrying                        | https://github.com/rholder/retrying                                                 | https://                                                                    |
| rfc3339-validator               | https://github.com/naimetti/rfc3339-validator                                       | https://                                                                    |
| rfc3986                         | https://rfc3986.readthedocs.io/en/latest/                                           | https://                                                                    |
| rfc3986-validator               | https://github.com/naimetti/rfc3986-validator                                       | https://                                                                    |
| rich                            | <b>Orion Floes</b>                                                                  | https://                                                                    |
| rpds-py                         | https://github.com/crate-py/rpds                                                    | https://                                                                    |
| rpmpack                         | https://github.com/google/rpmpack                                                   | https://                                                                    |
| rsa                             | https://stuvel.eu/rsa                                                               | https://                                                                    |
| ruamel-yaml                     | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https://                                                                    |
| ruamel.yaml.clib                | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https://                                                                    |
| s3transfer                      | https://github.com/boto/s3transfer                                                  | https://                                                                    |
| sasl                            | https://mellium.im/sasl                                                             | https://                                                                    |
| scikit-gstat                    | https://mmaelicke.github.io/scikit-gstat/                                           | https://                                                                    |
| scikit-image                    | https://scikit-image.org                                                            | https://                                                                    |
| scikit-learn                    | https://scikit-learn.org/stable/                                                    | https://                                                                    |
| scikit-learn-extra              | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https://                                                                    |
| scipy                           | https://scipy.org                                                                   | https://                                                                    |
| seaborn                         | https://seaborn.pydata.org                                                          | https://                                                                    |
| seaborn-base                    | https://seaborn.pydata.org                                                          | https://                                                                    |
| semver                          | https://github.com/Masterminds/semver/v3                                            | https://                                                                    |
| Send2Trash                      | https://github.com/arsenetar/send2trash                                             | https://                                                                    |
| setuptools                      | https://github.com/pypa/setuptools                                                  | https://                                                                    |
| setuptools-scm                  | https://github.com/pypa/setuptools_scm/                                             | https://                                                                    |
| sh                              | https://github.com/amoffat/sh                                                       | https://                                                                    |
| shellingham                     | https://github.com/sarugaku/shellingham                                             | https://                                                                    |
| simint                          | https://www.bennyp.org/research/simint/                                             | https://                                                                    |
| six                             | https://github.com/benjaminp/six                                                    | https://                                                                    |
| smirnoff99frosst                | https://github.com/openforcefield/smirnoff99frosst                                  | https://                                                                    |
| snappy                          | https://github.com/google/snappy                                                    | https://                                                                    |
| sniffio                         | https://github.com/python-trio/sniffio                                              | https://                                                                    |
| snowballstemmer                 | https://github.com/snowballstem/snowball                                            | https://                                                                    |
| soupsieve                       | https://github.com/facelessuser/soupsieve                                           | https://                                                                    |
| spglib                          | <b>Orion Floes</b>                                                                  | https://                                                                    |
| sphinx                          | https://github.com/sphinx-doc/sphinx                                                | https://                                                                    |
| sphinxcontrib-applehelp         | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https://                                                                    |
| sphinxcontrib-devhelp           | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https://                                                                    |
| sphinxcontrib-htmlhelp          | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https://                                                                    |
| sphinxcontrib-jsmath            | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https://                                                                    |
| sphinxcontrib-qthelp            | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https://                                                                    |
| sphinxcontrib-serializinghtml   | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https://                                                                    |
| Name of Project                 | Website                                                                             | License                                                                     |
| SQLAlchemy                      | https://www.sqlalchemy.org                                                          | https:/                                                                     |
| sqlite                          | https://sqlite.org/index.html                                                       | https:/                                                                     |
| sqlparse                        | https://github.com/andialbrecht/sqlparse                                            | https:/                                                                     |
| stack-data                      | http://github.com/alexmojaki/stack_data                                             | https:/                                                                     |
| starfile                        | https://github.com/alisterburt/starfile                                             | https:/                                                                     |
| statsmodels                     | https://github.com/statsmodels/statsmodels                                          | https:/                                                                     |
| structlog                       | https://www.structlog.org/                                                          | https:/                                                                     |
| svglib                          | https://github.com/deeplook/svglib                                                  | https:/                                                                     |
| sympy                           | https://sympy.org                                                                   | https:/                                                                     |
| tables                          | https://www.pytables.org/                                                           | https:/                                                                     |
| tabulate                        | https://github.com/astanin/python-tabulate                                          | https:/                                                                     |
| tbb                             | https://github.com/oneapi-src/oneTBB                                                | https:/                                                                     |
| tenacity                        | https://github.com/jd/tenacity                                                      | https:/                                                                     |
| tensorboard                     | https://github.com/tensorflow/tensorboard                                           | https:/                                                                     |
| tensorboard-data-server         | https://github.com/tensorflow/tensorboard                                           | https:/                                                                     |
| tensorboard-plugin-wit          | https://github.com/pair-code/what-if-tool                                           | https:/                                                                     |
| tensorflow                      | https://github.com/tensorflow/tensorflow                                            | https:/                                                                     |
| tensorflow-estimator            | https://github.com/tensorflow/estimator                                             | https:/                                                                     |
| tensorflow-io-gcs-filesystem    | <b>Orion Floes</b>                                                                  | https:/                                                                     |
| tensorflow-probability          | https://github.com/tensorflow/probability                                           | https:/                                                                     |
| termcolor                       | https://github.com/hugovk/termcolor                                                 | https:/                                                                     |
| terminado                       | https://github.com/jupyter/terminado                                                | https:/                                                                     |
| testpath                        | https://github.com/jupyter/testpath                                                 | https:/                                                                     |
| textangular                     | https://github.com/fraywing/textAngular                                             | https:/                                                                     |
| tf_keras                        | <b>Orion Floes</b>                                                                  | https:/                                                                     |
| threadpoolctl                   | https://github.com/joblib/threadpoolctl                                             | https:/                                                                     |
| three                           | https://github.com/mrdoob/three.js                                                  | https:/                                                                     |
| tifffile                        | https://github.com/cgohlke/tifffile/                                                | https:/                                                                     |
| tinycss2                        | https://github.com/Kozea/tinycss2/                                                  | https:/                                                                     |
| tinyxml2                        | https://github.com/leethomason/tinyxml2                                             | https:/                                                                     |
| tk                              | https://www.tcl.tk/                                                                 | https:/                                                                     |
| toml                            | https://github.com/toml-lang/toml                                                   | https:/                                                                     |
| tomli                           | https://github.com/hukkin/tomli                                                     | https:/                                                                     |
| toolz                           | https://github.com/pytoolz/toolz                                                    | https:/                                                                     |
| torch                           | https://pytorch.org/                                                                | https:/                                                                     |
| tornado                         | https://www.tornadoweb.org                                                          | https:/                                                                     |
| tqdm                            | https://github.com/tqdm/tqdm                                                        | https:/                                                                     |
| tracy                           | https://github.com/gear-genomics/tracy                                              | https:/                                                                     |
| traitlets                       | https://github.com/ipython/traitlets                                                | https:/                                                                     |
| triton                          | https://github.com/openai/triton/                                                   | https:/                                                                     |
| truststore                      | <b>Orion Floes</b>                                                                  | https:/                                                                     |
| ts-jest                         | https://github.com/kulshekhar/ts-jest                                               | https:/                                                                     |
| ts-loader                       | https://github.com/TypeStrong/ts-loader                                             | https:/                                                                     |
| twine                           | https://github.com/pypa/twine                                                       | https:/                                                                     |
| twinj uuid                      | https://github.com/twinj/uuid                                                       | https:/                                                                     |
| types                           | https://github.com/babel/babel                                                      | https:/                                                                     |
| typescript                      | https://github.com/Microsoft/TypeScript                                             | https:/                                                                     |
| typing_extensions               | https://github.com/python/typing                                                    | https:/                                                                     |
| tzdata                          | https://github.com/python/tzdata                                                    | https:/                                                                     |
|                                 |                                                                                     |                                                                             |
| Name of Project                 | Website                                                                             | License                                                                     |
| tzlocal                         | https://github.com/regebro/tzlocal                                                  | https:/                                                                     |
| umi-tools                       | https://github.com/CGATOxford/UMI-tools                                             | https:/                                                                     |
| unicodedata2                    | https://github.com/fonttools/unicodedata2                                           | https:/                                                                     |
| uritools                        | https://github.com/tkem/uritools/                                                   | https:/                                                                     |
| urllib3                         | https://urllib3.readthedocs.io/                                                     | https:/                                                                     |
| vine                            | https://github.com/celery/vine                                                      | https:/                                                                     |
| vue                             | https://github.com/vuejs/vue                                                        | https:/                                                                     |
| wcwidth                         | https://github.com/jquast/wcwidth                                                   | https:/                                                                     |
| webencodings                    | https://github.com/gsnedders/python-webencodings                                    | https:/                                                                     |
| websocket-client                | https://github.com/websocket-client/websocket-client.git                            | https:/                                                                     |
| Werkzeug                        | https://palletsprojects.com/p/werkzeug/                                             | https:/                                                                     |
| westpa                          | <b>Orion Floes</b>                                                                  | http://                                                                     |
| wheel                           | https://github.com/pypa/wheel                                                       | https:/                                                                     |
| widgetsnbextension              | https://github.com/jupyter-widgets/ipywidgets#readme                                | https:/                                                                     |
| wrapt                           | https://github.com/GrahamDumpleton/wrapt                                            | https:/                                                                     |
| wsutil                          | https://github.com/yhat/wsutil                                                      | https:/                                                                     |
| x/lint                          | https://golang.org/x/lint                                                           | https:/                                                                     |
| x/mod                           | https://golang.org/x/mod/semver                                                     | https:/                                                                     |
| x/net                           | https://golang.org/x/net                                                            | https:/                                                                     |
| x/oauth2                        | https://golang.org/x/oauth2                                                         | https:/                                                                     |
| x/sys                           | https://golang.org/x/sys                                                            | https:/                                                                     |
| x/text                          | https://golang.org/x/text                                                           | https:/                                                                     |
| x/tools                         | https://golang.org/x/tools                                                          | https:/                                                                     |
| x/xerrors                       | https://golang.org/x/xerrors                                                        | https:/                                                                     |
| xhtml2pdf                       | http://github.com/xhtml2pdf/xhtml2pdf                                               | https:/                                                                     |
| xlrd                            | https://github.com/python-excel/xlrd                                                | https:/                                                                     |
| xmlsec                          | https://github.com/mehcode/python-xmlsec                                            | https:/                                                                     |
| xmltodict                       | https://github.com/martinblech/xmltodict                                            | https:/                                                                     |
| xorg-kbproto                    | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https:/                                                                     |
| xorg-libice                     | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https:/                                                                     |
| xorg-libsm                      | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https:/                                                                     |
| xorg-libx11                     | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https:/                                                                     |
| xorg-libxau                     | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https:/                                                                     |
| xorg-libxdmcp                   | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https:/                                                                     |
| xorg-libxext                    | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https:/                                                                     |
| xorg-libxrender                 | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https:/                                                                     |
| xorg-libxt                      | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https:/                                                                     |
| xorg-renderproto                | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https:/                                                                     |
| xorg-xextproto                  | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https:/                                                                     |
| xorg-xproto                     | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https:/                                                                     |
| xxhash                          | https://github.com/cespare/xxhash/v2                                                | https:/                                                                     |
| xz                              | https://github.com/ulikunitz/xz                                                     | https:/                                                                     |
| yaml                            | https://pyyaml.org/                                                                 | https:/                                                                     |
| yaml-cpp                        | https://github.com/jbeder/yaml-cpp                                                  | https:/                                                                     |
| yaml.v2                         | https://gopkg.in/yaml.v2                                                            | https:/                                                                     |
| yaml.v3                         | https://gopkg.in/yaml.v3                                                            | https:/                                                                     |
| yarl                            | https://github.com/aio-libs/yarl/                                                   | https:/                                                                     |
| yaspin                          | https://github.com/pavdmyt/yaspin                                                   | https:/                                                                     |
| yfiles                          | https://www.yworks.com/products/yfiles                                              | comm                                                                        |
| Name of Project                 | Website                                                                             | License                                                                     |
| yml                             | https://pypi.org/project/yml/                                                       | N/A                                                                         |
| zap                             | https://go.uber.org/zap                                                             | https:                                                                      |
| zipp                            | https://github.com/jaraco/zipp                                                      | https:                                                                      |
| zlib                            | https://zlib.net/                                                                   | https:                                                                      |
| zstandard                       | https://github.com/indygreg/python-zstandard                                        | https:                                                                      |
| zstd                            | https://facebook.github.io/zstd/                                                    | https:                                                                      |
| _libgcc_mutex                   | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:                                                                      |
| _openmp_mutex                   | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:                                                                      |

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

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

# **INDEX**

# A

OEGrapheme:: OE2DActiveSiteDisplayOptions, AddLabel OEGrapheme::OEColorGradientDisplayOptiongEGrapheme::OE2DActiveSiteLegendDisplayOptions, 57 84 OEGrapheme:: OE2DPropMap, 58 AddMarkedValue OEGrapheme::OEColorGradientDisplayOptionQEGrapheme::OEAlignedDepictionFrom3DOptions, 68  $85$ OEGrapheme:: OEAlphaRainbowArcFxn, AddMarkedValues 130 OEGrapheme::OEColorGradientDisplayOptions, OEGrapheme:: OEAtomGlyphBase, 70 86 OEGrapheme:: OEAtomGlyphCircle, 71 AddMolecule OEGrapheme:: OEBondGlyphArrow, 73 OEGrapheme:: OERamachandranPlot, 112 OEGrapheme:: OEBondGlyphBase, 74

AddRamachandran OEGrapheme:: OEBondGlyphCircle, 75 OEGrapheme:: OERamachandranPlot, 112 OEGrapheme:: OEBondGlyphCross, 77 B OEGrapheme:: OEBondGlyphCurvedArrow, 78 bfactor2imq.py OEGrapheme:: OEBondGlyphScissors, 80 Example Code, 28 OEGrapheme:: OEBondGlyphStitch, 81 OEGrapheme:: OEBondGlyphZiqZaq, 82 C OEGrapheme:: OEBrickRoadArcFxn, 131 ClearBoxRange diboxnanye<br>OEGrapheme::OEColorGradientDisplayOptionSLurapheme::OECogArcFxn,135 OEGrapheme:: OECastleArcFxn, 133 OEGrapheme:: OEColorForceFieldDisplay, ClearLabels OEGrapheme::OEColorGradientDisplayOptions.......<br>OEGrapheme::OEColorGradientDisplayOption&Grapheme::OEColorForceFieldLegendDisplayOptio  $Q<sub>7</sub>$ 99 ClearMarkedValues OEGrapheme:: OEColorGradientDisplayOptions, OEGrapheme::OEColorGradientDisplayOptions,  $84$ 87 OEGrapheme:: OEColorGradientLabel, 96 ClearQuerySurfaceArcFxn OEGrapheme::OEColorOverlapDisplayOptions, OEGrapheme::OEColorOverlapDisplayOptions, OEGrapheme::OEShapeOverlapDisplayOptions, OEGrapheme::OEComplexSurfaceArcFxnBase, 101 119 OEGrapheme:: OEDefaultArcFxn, 137 ClearSurfaceArcFxn OEGrapheme:: OEDefaultBuriedArcFxn, OEGrapheme:: OEShapeQueryDisplayOptions, 139 125 OEGrapheme:: OEDefaultCavityArcFxn, complex2imq.py 140 Example Code, 36 OEGrapheme:: OEDefaultSolventArcFxn, Constructors 141 OEGrapheme:: OE2DActiveSiteDisplay, OEGrapheme:: OEDefaultVoidArcFxn, 142 51

```
OEGrapheme:: OEDepictionFrom3DOptions,
                                               OEGrapheme:: OEDefaultArcFxn, 138
       102
                                               OEGrapheme:: OEDefaultBuriedArcFxn,
   OEGrapheme:: OEEyelashArcFxn, 143
                                                   139
   OEGrapheme:: OEFlowerArcFxn, 145
                                               OEGrapheme:: OEDefaultCavityArcFxn,
   OEGrapheme:: OENearestResidue, 105
                                                   140
   OEGrapheme:: OENecklaceArcFxn, 147
                                               OEGrapheme:: OEDefaultSolventArcFxn,
   OEGrapheme:: OEOliveBranchArcFxn, 148
                                                   141
   OEGrapheme:: OEPearlsArcFxn, 149
                                               OEGrapheme:: OEDefaultVoidArcFxn, 143
   OEGrapheme:: OEPeptideDisplayOptions,
                                               OEGrapheme:: OEEyelashArcFxn, 144
       106
                                               OEGrapheme:: OEFlowerArcFxn, 146
   OEGrapheme:: OEPlotMarker, 108
                                               OEGrapheme:: OENecklaceArcFxn, 147
   OEGrapheme:: OERaceTrackArcFxn, 151
                                               OEGrapheme:: OENullArcFxn, 148
   OEGrapheme:: OERailroadTrackArcFxn,
                                               OEGrapheme:: OEOliveBranchArcFxn, 149
                                               OEGrapheme:: OEPearlsArcFxn, 150
       153
   OEGrapheme:: OERamachandranPlot, 111
                                               OEGrapheme:: OERaceTrackArcFxn, 152
   OEGrapheme:: OEResidueSVGNoMarkup,
                                               OEGrapheme:: OERailroadTrackArcFxn,
       114
                                                   153
   OEGrapheme:: OEResidueSVGStandardMarkup,
                                               OEGrapheme:: OEResidueSVGMarkupBase,
       115
                                                   113
   OEGrapheme:: OESawArcFxn, 153
                                               OEGrapheme:: OEResidueSVGNoMarkup,
   OEGrapheme:: OEShapeOverlapDisplay,
                                                   114
                                               OEGrapheme:: OEResidueSVGStandardMarkup,
       117
   OEGrapheme:: OEShapeOverlapDisplayOptions,
                                                   115
       119
                                               OEGrapheme:: OESawArcFxn, 154
   OEGrapheme:: OEShapeQueryDisplay, 122
                                               OEGrapheme:: OESimpsonArcFxn, 156
   OEGrapheme:: OEShapeQueryDisplayOptions,
                                               OEGrapheme:: OEStitchArcFxn, 157
       124
                                               OEGrapheme:: OESunArcFxn, 158
   OEGrapheme:: OESimpsonArcFxn, 155
                                               OEGrapheme:: OESurfaceArcFxnBase, 159
   OEGrapheme:: OEStitchArcFxn, 157
                                               OEGrapheme:: OEWreathArcFxn, 161
   OEGrapheme:: OESunArcFxn, 157
                                           Е
   OEGrapheme:: OESurfaceArc, 127
   OEGrapheme:: OEWreathArcFxn, 160
                                           Example Code
CreateComplexCopy
                                               bfactor2img.py, 28
   OEGrapheme:: OEComplexSurfaceArcFxnBase,
                                               complex2imq.py, 36
       136
                                               shapeoverlap2pdf.py.41
CreateCopy
                                           G
   OEGrapheme:: OEAlphaRainbowArcFxn,
       131
                                           GetAminoAcidScale
   OEGrapheme:: OEAtomGlyphBase, 71
                                               OEGrapheme:: OEPeptideDisplayOptions,
   OEGrapheme:: OEAtomGlyphCircle, 72
                                                   107
   OEGrapheme:: OEBondGlyphArrow, 73
                                           GetAtomDisplay
   OEGrapheme:: OEBondGlyphBase, 74
                                               OEGrapheme:: OESurfaceArc, 128
   OEGrapheme:: OEBondGlyphCircle, 76
                                           GetBgnAngle
   OEGrapheme:: OEBondGlyphCross, 77
                                               OEGrapheme:: OESurfaceArc, 128
   OEGrapheme:: OEBondGlyphCurvedArrow,
                                           GetBoxRangeMax
       79
                                               OEGrapheme:: OEColorGradientDisplayOptions,
   OEGrapheme:: OEBondGlyphScissors, 80
                                                   87OEGrapheme:: OEBondGlyphStitch, 81
                                           GetBoxRangeMin
   OEGrapheme:: OEBondGlyphZiqZaq, 83
                                               OEGrapheme:: OEColorGradientDisplayOptions,
   OEGrapheme:: OEBrickRoadArcFxn, 132
                                                   87
   OEGrapheme:: OECastleArcFxn, 134
                                           GetBoxRangePen
   OEGrapheme:: OECogArcFxn, 135
                                               OEGrapheme:: OEColorGradientDisplayOptions,
   OEGrapheme:: OEComplexSurfaceArcFxnBase,
                                                   87
       136
                                           GetCenter
```

OEGrapheme:: OESurfaceArc, 128 GetDisplayPosition GetClassName OEGrapheme:: OENearestResidue, 105 OEGrapheme:: OEResidueSVGMarkupBase, GetDist OEGrapheme:: OENearestResidue, 105 113 OEGrapheme:: OEResidueSVGNoMarkup, GetEndAngle 114 OEGrapheme:: OESurfaceArc, 128 OEGrapheme:: OEResidueSVGStandardMarkuGetGroupId 116 OEGrapheme:: OEResidueSVGMarkupBase, GetClearBackground 113 OEGrapheme::OEColorOverlapDisplayOptionsOEGrapheme::OEResidueSVGNoMarkup, 101 114 OEGrapheme::OEShapeOverlapDisplayOptionsOEGrapheme::OEResidueSVGStandardMarkup, 119 116 OEGrapheme::OEShapeQueryDisplayOptionGetHeight  $125$ OEGrapheme:: OE2DActiveSiteDisplay, 52 GetClearCoords OEGrapheme:: OEAlignedDepictionFrom3DO6etiEmtseractive 69 OEGrapheme:: OEPeptideDisplayOptions, 107 GetColor OEGrapheme::OEColorForceFieldDisplay,GetLabel  $Q\Omega$ OEGrapheme:: OEColorGradientLabel, 96 GetColorAtomStyle GetLabels OEGrapheme::OEShapeQueryDisplayOptions, OEGrapheme::OEColorGradientDisplayOptions, 125 89 GetColorStopLabelFont GetLabelStyle OEGrapheme::OEColorGradientDisplayOption@EGrapheme::OEPeptideDisplayOptions, 107 GetColorStopLabelFontScale GetLegendFont OEGrapheme::OEColorGradientDisplayOption@EGrapheme::OE2DPropMap, 59 88 GetLegendFontScale GetColorStopPrecision OEGrapheme:: OE2DPropMap, 59 OEGrapheme::OEColorGradientDisplayOptdetnLseqendLocation 88 OEGrapheme:: OE2DPropMap, 60 GetColorStopVisibility GetMarkedValuePen OEGrapheme::OEColorGradientDisplayOption@EGrapheme::OEColorGradientDisplayOptions, 88 89 GetColorTypes GetMarkedValuePrecision OEGrapheme:: OEColorForceFieldDisplay, OEGrapheme:: OEColorGradientDisplayOptions, 98 89 GetCoordsToInertialFrame GetMarkedValues OEGrapheme:: OEDepictionFrom3DOptions, OEGrapheme::OEColorGradientDisplayOptions, 103 89 GetDepictOrientation GetMaxBondRotations OEGrapheme::OEShapeQueryDisplayOptions, OEGrapheme::OEAlignedDepictionFrom3DOptions, 125 69 GetDepth OEGrapheme:: OEDepictionFrom3DOptions, OEGrapheme:: OEComplexSurfaceArcFxnBase, 103 GetMaxValue 136 OEGrapheme:: OE2DPropMap, 60 GetDisplayedLigand OEGrapheme:: OE2DActiveSiteDisplay, GetMinValue 52 OEGrapheme:: OE2DPropMap, 60 GetDisplayedResidues GetName OEGrapheme:: OE2DActiveSiteDisplay, OEGrapheme:: OEColorForceFieldDisplay, 52 98

OEGrapheme:: OEShapeOverlapDisplay, GetNegativeColor OEGrapheme:: OE2DPropMap, 60 118 GetOptions OEGrapheme:: OEShapeQueryDisplay, 123 OEGrapheme:: OE2DActiveSiteDisplay, GetValue 52 OEGrapheme:: OEColorGradientLabel, 96 GetOverlapColor GetWidth OEGrapheme::OEShapeOverlapDisplayOptionsOEGrapheme::OE2DActiveSiteDisplay, 120 52 GetOverlapDisplayStyle OEGrapheme:: OEShapeOverlapDisplayOptions, 120 IsValid GetPen OEGrapheme:: OE2DActiveSiteDisplay, OEGrapheme:: OEPlotMarker, 110 52 GetPositiveColor OEGrapheme:: OENearestResidue, 105 OEGrapheme:: OE2DPropMap, 60 OEGrapheme:: OEShapeOverlapDisplay, GetQuerySurfaceArcFxn 118 OEGrapheme::OEColorOverlapDisplayOptionsOEGrapheme::OEShapeOueryDisplay.123 101  $OEGrapheme::OEShapeOverlapDisplayOpti<sup>0</sup>ms,$ 120 NumColorTypes GetRadius OEGrapheme:: OEColorForceFieldDisplay, OEGrapheme:: OESurfaceArc, 129  $Q\overline{Q}$ GetRadiusRatio NumCols OEGrapheme:: OE2DPropMap, 61 OEGrapheme:: OE2DActiveSiteLegendDisplayOptions, GetRenderInteractiveLegend 57 OEGrapheme::OE2DActiveSiteDisplayOptionsOEGrapheme::OEColorForceFieldLegendDisplayOptio 54 99 GetResidue NumDataPoints OEGrapheme:: OENearestResidue, 105 OEGrapheme:: OERamachandranPlot, 112 GetResidueSVGMarkupFunctor NumRows OEGrapheme::OE2DActiveSiteDisplayOptionsOEGrapheme::OE2DActiveSiteLegendDisplayOptions, 54 57 GetResolution OEGrapheme:: OEColorForceFieldLegendDisplayOptio OEGrapheme:: OE2DPropMap, 61 99 GetRotateTo2DReference OEGrapheme::OEDepictionFrom3DOptions,  $O$ 103 OEGrapheme:: OE2DActiveSiteDisplay, 51 GetScale Constructors, 51 OEGrapheme:: OEPlotMarker, 111 GetDisplayedLigand.52 GetStyle GetDisplayedResidues, 52 OEGrapheme:: OEPlotMarker, 111 GetHeight, 52 GetSuppressHydrogens GetOptions, 52 OEGrapheme::OEAlignedDepictionFrom3DOptigaewidth.52 69 IsValid, 52 OEGrapheme::OEDepictionFrom3DOptions, OEGrapheme::OE2DActiveSiteDisplayOptions, 103 52 GetSurfaceArcFxn Constructors, 53 OEGrapheme::OEShapeQueryDisplayOptions, GetRenderInteractiveLegend, 54 125 GetResidueSVGMarkupFunctor, 54 GetSVGMagnifyResidueInHover GetSVGMagnifyResidueInHover, 54 OEGrapheme:: OE2DActiveSiteDisplayOptions<sub>operator=, 53</sub> 54 SetBackgroundColor, 54 GetTitle SetDimensions, 54 SetHeight, 55

SetRenderInteractiveLegend.55 OEGrapheme:: OEActiveSiteRenderStyle:: ContactMap, SetResidueSVGMarkupFunctor, 55 165 SetScale, 56 OEGrapheme:: OEActiveSiteRenderStyle:: Default, SetSuperAtomStyle, 56 164 SetSVGMagnifyResidueInHover, 56 OEGrapheme:: OEActiveSiteRenderStyle:: InteractionMap SetWidth, 56 166 OEGrapheme::OE2DActiveSiteLeqendDisplayOpEGpapheme::OEActiveSiteRenderStyle::UnpairedMap, 167 56 Constructors, 57 OEGrapheme:: OEAddComplexSurfaceArcs, 189 NumCols, 57 OEGrapheme:: OEAddGlyph, 189 NumRows, 57 OEGrapheme:: OEAddLigandHighlighting, 191 operator=, 57 OEGrapheme:: OEAddResidueHighlighting, OEGrapheme:: OE2DPropMap, 58 194 Constructors, 58 OEGrapheme:: OEAlignedDepictionFrom3DOptions, GetLegendFont, 59 67 GetLegendFontScale, 59 Constructors. 68 GetLegendLocation, 60 GetClearCoords, 69 GetMaxValue, 60 GetMaxBondRotations, 69 GetMinValue, 60 GetSuppressHydrogens, 69 GetNegativeColor, 60 operator= $, 69$ GetPositiveColor, 60 SetClearCoords, 69 GetRadiusRatio, 61 SetMaxBondRotations, 69 GetResolution, 61 SetSuppressHydrogens, 70 operator=, 58 OEGrapheme:: OEAlphaRainbowArcFxn, 130 Render, 59 Constructors, 130 SetLegendFont, 61 CreateCopy, 131 SetLegendFontScale, 61 operator(), 131 SetLegendLocation, 62 OEGrapheme:: OEAtomGlyphBase, 70 SetMaxValue, 63 Constructors, 70 SetMinValue, 64 CreateCopy, 71 SetNegativeColor, 65 RenderGlyph, 71 SetPositiveColor. 65 OEGrapheme:: OEAtomGlyphCircle, 71 SetRadiusRatio, 66 Constructors, 71 SetResolution, 67 CreateCopy, 72 OEGrapheme:: OE2DPropMapSetup, 161 RenderGlyph, 72 OEGrapheme:: OE2DPropMapSetup:: All, 161 OEGrapheme:: OEBondGlyphArrow, 72 OEGrapheme:: OE2DPropMapSetup:: Legend, Constructors, 73 161 CreateCopy, 73 OEGrapheme:: OE2DPropMapSetup:: MaxValue, RenderGlyph, 73 OEGrapheme:: OEBondGlyphBase, 74 162 OEGrapheme:: OE2DPropMapSetup:: MinValue, Constructors, 74 162 CreateCopy, 74 OEGrapheme:: OE2DPropMapSetup:: NegativeColor, RenderGlyph, 74 OEGrapheme:: OEBondGlyphCircle, 75 163 OEGrapheme:: OE2DPropMapSetup:: PositiveColor,Constructors, 75 163 CreateCopy, 76 OEGrapheme:: OE2DPropMapSetup:: RadiusRatio, RenderGlyph, 76 164 OEGrapheme:: OEBondGlyphCross, 76 OEGrapheme:: OE2DPropMapSetup:: Resolution, Constructors, 77 164 CreateCopy, 77 RenderGlyph, 77 OEGrapheme:: OEActiveSiteRenderStyle, 164 OEGrapheme::OEActiveSiteRenderStyle::BFaOEGrMpheme::OEBondGlyphCurvedArrow,78 165 Constructors, 78 CreateCopy, 79

```
RenderGlyph. 79
OEGrapheme:: OEBondGlyphScissors, 79
   Constructors, 80
   CreateCopy, 80
   RenderGlyph, 80
OEGrapheme:: OEBondGlyphStitch, 81
   Constructors. 81
   CreateCopy, 81
   RenderGlyph, 82
OEGrapheme:: OEBondGlyphZigZag, 82
   Constructors, 82
   CreateCopy, 83
   RenderGlyph, 83
OEGrapheme:: OEBrickRoadArcFxn, 131
   Constructors, 131
   CreateCopy, 132
   operator(), 132
OEGrapheme:: OECastleArcFxn, 132
   Constructors, 133
   CreateCopy, 134
   operator(), 133
OEGrapheme:: OECircleStyle, 167
OEGrapheme:: OECircleStyle:: AlphaRainbow,
       168
OEGrapheme:: OECircleStyle:: BrickRoad,
       168
OEGrapheme:: OECircleStyle:: Castle, 168
OEGrapheme:: OECircleStyle:: Cog, 169
OEGrapheme:: OECircleStyle:: Default, 169
OEGrapheme:: OECircleStyle:: Eyelash, 169
OEGrapheme:: OECircleStyle:: Flower, 170
OEGrapheme:: OECircleStyle:: GreekKey, 170
OEGrapheme:: OECircleStyle:: Necklace, 170
OEGrapheme:: OECircleStyle:: OliveBranch,
       171
OEGrapheme:: OECircleStyle:: Pearls, 171
OEGrapheme:: OECircleStyle:: RaceTrack,
       171
OEGrapheme:: OECircleStyle:: RailroadTrack,
       172
OEGrapheme:: OECircleStyle:: Saw, 172
OEGrapheme:: OECircleStyle:: Simpson, 172
OEGrapheme:: OECircleStyle:: Stitch, 173
OEGrapheme:: OECircleStyle:: Sun, 173
OEGrapheme:: OECircleStyle:: Wreath, 173
OEGrapheme:: OEClearSurfaceArcFxn, 196
OEGrapheme:: OECogArcFxn, 134
   Constructors, 135
   CreateCopy, 135
   operator(), 135
OEGrapheme:: OEColorAtomStyle, 174
OEGrapheme:: OEColorAtomStyle:: Circle,
       174
```

OEGrapheme:: OEColorAtomStyle:: Default, 174 OEGrapheme:: OEColorAtomStyle:: Hidden, 174 OEGrapheme:: OEColorForceFieldDisplay, 97 Constructors. 97 GetColor, 98 GetColorTypes, 98 GetName, 98 NumColorTypes, 98 operator=, 97 SetColor, 98 SetName, 98 OEGrapheme::OEColorForceFieldLegendDisplayOptions, 98 Constructors, 99 NumCols, 99 NumRows, 99 operator=, 99 OEGrapheme:: OEColorGradientDisplayOptions, 83 AddLabel, 84 AddMarkedValue. 85 AddMarkedValues, 86 ClearBoxRange, 86 ClearLabels, 86 ClearMarkedValues, 87 Constructors, 84 GetBoxRangeMax, 87 GetBoxRangeMin, 87 GetBoxRangePen, 87 GetColorStopLabelFont, 88 GetColorStopLabelFontScale, 88 GetColorStopPrecision, 88 GetColorStopVisibility, 88 GetLabels, 89 GetMarkedValuePen, 89 GetMarkedValuePrecision, 89 GetMarkedValues, 89 operator=, 84 SetBoxRange, 90 SetBoxRangePen, 90 SetColorStopLabelFont, 91 SetColorStopLabelFontScale, 92 SetColorStopPrecision, 92 SetColorStopVisibility, 93 SetMarkedValuePen, 94 SetMarkedValuePrecision, 94 SetMarkedValues, 94 OEGrapheme:: OEColorGradientLabel, 95 Constructors, 96 GetLabel, 96 GetValue, 96

operator=, 96 OEGrapheme:: OEColorOverlapDisplayOptions,  $QQ$ ClearQuerySurfaceArcFxn, 101 Constructors, 100 GetClearBackground, 101 GetQuerySurfaceArcFxn, 101 operator= $, 100$ SetClearBackground, 101 SetQuerySurfaceArcFxn, 101 OEGrapheme:: OEComplexSurfaceArcFxnBase, 135 Constructors, 136 CreateComplexCopy, 136 CreateCopy, 136 GetDepth, 136 operator(), 136 operator= $, 136$ SetDepth, 137 OEGrapheme:: OEConfigure2DPropMap, 196 OEGrapheme:: OEDefaultArcFxn, 137 Constructors, 137 CreateCopy, 138 operator $($ ), 138 OEGrapheme:: OEDefaultBuriedArcFxn, 138 Constructors, 139 CreateCopy, 139 operator(), 139 OEGrapheme:: OEDefaultCavityArcFxn, 139 Constructors, 140 CreateCopy, 140 operator $($ ), 140 OEGrapheme:: OEDefaultSolventArcFxn, 140 Constructors, 141 CreateCopy, 141 operator(), 141 OEGrapheme:: OEDefaultVoidArcFxn, 142 Constructors, 142 CreateCopy, 143 operator(), 143 OEGrapheme:: OEDepictionFrom3DOptions, 102 Constructors, 102 GetCoordsToInertialFrame, 103 GetMaxBondRotations, 103 GetRotateTo2DReference, 103 GetSuppressHydrogens, 103 operator= $, 102$ SetCoordsToInertialFrame, 103 SetMaxBondRotations, 104 SetRotateTo2DReference, 104 SetSuppressHydrogens, 104 OEGrapheme:: OEDraw2DSurface, 197 OEGrapheme:: OEDrawActiveSiteLegend, 199

OEGrapheme:: OEDrawAlphaRainbowCircle, 232 OEGrapheme:: OEDrawAlphaRainbowSurfaceArc, 232 OEGrapheme:: OEDrawBFactorMapLegend, 200 OEGrapheme:: OEDrawBrickRoadCircle, 233 OEGrapheme:: OEDrawBrickRoadSurfaceArc, 234 OEGrapheme:: OEDrawCastleCircle, 235 OEGrapheme:: OEDrawCastleSurfaceArc, 236 OEGrapheme:: OEDrawCircle, 200 OEGrapheme:: OEDrawCogCircle, 237 OEGrapheme:: OEDrawCogSurfaceArc, 237 OEGrapheme:: OEDrawColorForceFieldLegend, 201 OEGrapheme:: OEDrawColorGradient, 201 OEGrapheme:: OEDrawDefaultCircle, 238 OEGrapheme:: OEDrawDefaultSurfaceArc, 239 OEGrapheme:: OEDrawEyelashCircle, 239 OEGrapheme:: OEDrawEyelashSurfaceArc, 240 OEGrapheme:: OEDrawFlowerCircle, 241 OEGrapheme:: OEDrawFlowerSurfaceArc, 242 OEGrapheme:: OEDrawGreekKeyCircle, 242 OEGrapheme:: OEDrawIridiumData, 49 OEGrapheme:: OEDrawNecklaceCircle, 243 OEGrapheme:: OEDrawNecklaceSurfaceArc, 244 OEGrapheme:: OEDrawOliveBranchCircle, 245 OEGrapheme:: OEDrawOliveBranchSurfaceArc, 245 OEGrapheme:: OEDrawPearlsCircle, 246 OEGrapheme:: OEDrawPearlsSurfaceArc, 247 OEGrapheme:: OEDrawPeptide, 203 OEGrapheme:: OEDrawRaceTrackCircle, 248 OEGrapheme:: OEDrawRaceTrackSurfaceArc. 248 OEGrapheme:: OEDrawRailroadTrackCircle, 249 OEGrapheme:: OEDrawRailroadTrackSurfaceArc, 250 OEGrapheme:: OEDrawResidues, 206 OEGrapheme:: OEDrawROCSScores, 206 OEGrapheme:: OEDrawSawCircle, 251 OEGrapheme:: OEDrawSawSurfaceArc, 252 OEGrapheme:: OEDrawSimpsonCircle, 253 OEGrapheme:: OEDrawSimpsonSurfaceArc, 253 OEGrapheme:: OEDrawStitchCircle, 254 OEGrapheme:: OEDrawStitchSurfaceArc, 255 OEGrapheme:: OEDrawSunCircle, 256 OEGrapheme:: OEDrawSunSurfaceArc, 256 OEGrapheme:: OEDrawSurfaceArc, 207 OEGrapheme:: OEDrawUnpairedInteractionMapLeqend, 208 OEGrapheme:: OEDrawWreathCircle, 257

```
OEGrapheme:: OEDrawWreathSurfaceArc, 258
OEGrapheme:: OEEyelashArcFxn, 143
   Constructors, 143
   CreateCopy, 144
   operator(), 144
OEGrapheme:: OEFlowerArcFxn, 144
   Constructors. 145
   CreateCopy, 146
   operator(), 145
OEGrapheme:: OEGet2DSurfaceArcs, 209
OEGrapheme:: OEGetMoleculeSurfaceScale,
       210
OEGrapheme:: OEGetNearbyAtom, 211
OEGrapheme:: OEGetNearbyBond, 211
OEGrapheme:: OEGetNearbyResidue, 212
OEGrapheme:: OEGetNearestAtom, 212
OEGrapheme:: OEGetNearestBond, 213
OEGrapheme:: OEGetNearestResidue, 213
OEGrapheme:: OEGetSurfaceArcFxn, 213
OEGrapheme:: OEGraphemeGetArch, 214
OEGrapheme:: OEGraphemeGetLicensee, 214
OEGrapheme:: OEGraphemeGetPlatform, 214
OEGrapheme:: OEGraphemeGetRelease, 214
OEGrapheme:: OEGraphemeGetSite, 214
OEGrapheme:: OEGraphemeGetVersion, 214
OEGrapheme:: OEGraphemeIsLicensed, 214
OEGrapheme:: OEHasSurfaceArcFxn, 215
OEGrapheme:: OELegendLocation, 174
OEGrapheme:: OELegendLocation:: Bottom,
       175
OEGrapheme:: OELegendLocation:: Default,
       174
OEGrapheme:: OELegendLocation:: Hidden,
       176
OEGrapheme:: OELegendLocation:: Left, 176
OEGrapheme:: OELegendLocation:: Right, 176
OEGrapheme:: OELegendLocation:: Top, 177
OEGrapheme:: OENearestResidue, 104
   Constructors, 105
   GetDisplayPosition, 105
   GetDist, 105
   GetResidue. 105
   IsValid. 105
OEGrapheme:: OENecklaceArcFxn, 146
   Constructors, 147
   CreateCopy, 147
   operator(), 147
OEGrapheme:: OENullArcFxn, 147
   CreateCopy, 148
   operator(), 147
OEGrapheme:: OEOliveBranchArcFxn, 148
   Constructors, 148
   CreateCopy, 149
   operator(), 149
```

OEGrapheme:: OEPatternDirection, 177 OEGrapheme:: OEPatternDirection:: Default, 178 OEGrapheme:: OEPatternDirection:: Inside, 178 OEGrapheme:: OEPatternDirection:: Outside, 178 OEGrapheme:: OEPearlsArcFxn, 149 Constructors, 149 CreateCopy, 150 operator(), 150 OEGrapheme:: OEPeptideDisplayOptions, 105 Constructors, 106 GetAminoAcidScale, 107 GetInteractive, 107 GetLabelStyle, 107 operator=, 106 SetAminoAcidScale, 107 SetInteractive, 108 SetLabelStyle, 108 OEGrapheme:: OEPeptideLabelStyle, 178 OEGrapheme:: OEPeptideLabelStyle:: Default, 179 OEGrapheme:: OEPeptideLabelStyle:: SingleLetter, 179 OEGrapheme:: OEPeptideLabelStyle:: ThreeLetters, 179 OEGrapheme:: OEPlotMarker, 108 Constructors, 108 GetPen, 110 GetScale, 111 GetStyle, 111 operator! =,  $110$ operator=, 109 operator==,  $110$ OEGrapheme:: OEPlotMarkerStyle, 180 OEGrapheme:: OEPlotMarkerStyle:: Circle, 180 OEGrapheme:: OEPlotMarkerStyle:: Default, 180 OEGrapheme:: OEPlotMarkerStyle:: Square, 180 OEGrapheme:: OEPrepareActiveSiteDepiction, 215 OEGrapheme:: OEPrepareAlignedDepictionFrom3D, 215 OEGrapheme:: OEPrepareDepictionFrom3D, 218 OEGrapheme:: OERaceTrackArcFxn, 150 Constructors, 151 CreateCopy, 152 operator $($ ), 151 OEGrapheme:: OERailroadTrackArcFxn, 152 Constructors, 153

CreateCopy, 153 SetClearBackground, 120 operator(), 153 SetOverlapColor, 121 OEGrapheme:: OERamachandranPlot, 111 SetOverlapDisplayStyle, 121 AddMolecule, 112 SetQuerySurfaceArcFxn, 121 AddRamachandran, 112 OEGrapheme:: OEShapeOverlapDisplayStyle, Constructors, 111 181 OEGrapheme:: OEShapeOverlapDisplayStyle:: Default, NumDataPoints, 112 operator=, 112 181 OEGrapheme:: OERenderActiveSite, 218 OEGrapheme::OEShapeOverlapDisplayStyle::PropertyClo OEGrapheme:: OERenderActiveSiteMaps, 221 181 OEGrapheme:: OERenderBFactorMap, 222 OEGrapheme::OEShapeOverlapDisplayStyle::PropertyMap OEGrapheme:: OERenderColorOverlap, 225 181 OEGrapheme:: OERenderContactMap, 224 OEGrapheme:: OEShapeQueryDisplay, 121 OEGrapheme:: OERenderRamachandranPlot, Constructors, 122 226 GetTitle, 123 OEGrapheme:: OERenderShapeOverlap, 227 IsValid, 123 OEGrapheme:: OERenderShapeQuery, 228 operator=, 123 OEGrapheme::OERenderUnpairedInteractionM@pGrapheme::OEShapeQueryDisplayOptions, 230 123 OEGrapheme:: OEResidueSVGMarkupBase, 113 ClearSurfaceArcFxn, 125 CreateCopy, 113 Constructors, 124 GetClassName, 113 GetClearBackground, 125 GetColorAtomStyle, 125 GetGroupId, 113 OEGrapheme:: OEResidueSVGNoMarkup, 114 GetDepictOrientation, 125 Constructors, 114 GetSurfaceArcFxn, 125 CreateCopy, 114 operator=, 124 GetClassName, 114 SetClearBackground, 126 GetGroupId, 114 SetColorAtomStyle, 126 OEGrapheme:: OEResidueSVGStandardMarkup, SetDepictOrientation, 126 115 SetSurfaceArcFxn, 126 Constructors, 115 OEGrapheme:: OESimpsonArcFxn, 154 CreateCopy, 115 Constructors, 155 GetClassName, 116 CreateCopy, 156 GetGroupId, 116 operator $($ ), 155 OEGrapheme:: OESawArcFxn, 153 OEGrapheme:: OEStitchArcFxn, 156 Constructors, 153 Constructors, 157 CreateCopy, 154 CreateCopy, 157 operator(), 154 operator(), 157 OEGrapheme:: OESetSurfaceArcFxn, 231 OEGrapheme:: OESunArcFxn, 157 OEGrapheme:: OESetup2DPropMap, 232 Constructors, 157 OEGrapheme:: OEShapeOverlapDisplay, 116 CreateCopy, 158 Constructors, 117 operator(), 158 GetTitle, 118 OEGrapheme:: OESurfaceArc, 127 IsValid, 118 Constructors, 127 GetAtomDisplay, 128 operator=, 117 OEGrapheme:: OEShapeOverlapDisplayOptions, GetBgnAngle, 128 118 GetCenter, 128 ClearQuerySurfaceArcFxn, 119 GetEndAngle, 128 Constructors, 119 GetRadius, 129 GetClearBackground, 119 operator=, 128 GetOverlapColor, 120 SetAtomDisplay, 129 GetOverlapDisplayStyle, 120 SetBgnAngle, 129 GetQuerySurfaceArcFxn, 120 SetCenter, 129 operator=, 119 SetEndAngle, 129

SetRadius, 129 OEGrapheme:: OECogArcFxn, 135 OEGrapheme:: OESurfaceArcFxnBase, 158 OEGrapheme:: OEComplexSurfaceArcFxnBase, CreateCopy, 159 136 OEGrapheme:: OEDefaultArcFxn, 138 operator(), 159 OEGrapheme:: OESurfaceArcScale, 181 OEGrapheme:: OEDefaultBuriedArcFxn, OEGrapheme:: OESurfaceArcScale:: Default, 139 OEGrapheme:: OEDefaultCavityArcFxn, 181 OEGrapheme:: OESurfaceArcScale:: Maximum, 140 182 OEGrapheme:: OEDefaultSolventArcFxn, OEGrapheme:: OESurfaceArcScale:: Minimum, 141 183 OEGrapheme:: OEDefaultVoidArcFxn, 143 OEGrapheme:: OESurfaceArcStyle, 183 OEGrapheme:: OEEyelashArcFxn, 144 OEGrapheme::OESurfaceArcStyle::AlphaRainbow,OEGrapheme::OEFlowerArcFxn, 145 OEGrapheme:: OENecklaceArcFxn, 147 183 OEGrapheme:: OESurfaceArcStyle:: BrickRoad, OEGrapheme:: OENullArcFxn, 147 183 OEGrapheme:: OEOliveBranchArcFxn, 149 OEGrapheme:: OESurfaceArcStyle:: Castle, OEGrapheme:: OEPearlsArcFxn, 150 184 OEGrapheme:: OERaceTrackArcFxn, 151 OEGrapheme:: OESurfaceArcStyle:: Cog, 184 OEGrapheme:: OERailroadTrackArcFxn, OEGrapheme:: OESurfaceArcStyle:: Default, 153 184 OEGrapheme:: OESawArcFxn, 154 OEGrapheme:: OESurfaceArcStyle:: Eyelash, OEGrapheme:: OESimpsonArcFxn, 155 185 OEGrapheme:: OEStitchArcFxn, 157 OEGrapheme:: OESurfaceArcStyle:: Flower, OEGrapheme:: OESunArcFxn, 158 185 OEGrapheme:: OESurfaceArcFxnBase, 159 OEGrapheme:: OESurfaceArcStyle:: Necklace, OEGrapheme:: OEWreathArcFxn, 161 operator= 185 OEGrapheme::OESurfaceArcStyle::OliveBranch, OEGrapheme::OE2DActiveSiteDisplayOptions, 186 53 OEGrapheme:: OESurfaceArcStyle:: Pearls, OEGrapheme:: OE2DActiveSiteLegendDisplayOptions, 186 57 OEGrapheme:: OESurfaceArcStyle:: RaceTrack, OEGrapheme:: OE2DPropMap, 58 OEGrapheme:: OEAlignedDepictionFrom3DOptions, 186 OEGrapheme:: OESurfaceArcStyle:: RailroadTrack, 69 OEGrapheme:: OEColorForceFieldDisplay, 187 OEGrapheme:: OESurfaceArcStyle:: Saw, 187 97 OEGrapheme:: OESurfaceArcStyle:: Simpson, OEGrapheme:: OEColorForceFieldLegendDisplayOptio 187 99 OEGrapheme:: OESurfaceArcStyle:: Stitch, OEGrapheme:: OEColorGradientDisplayOptions, 188 84 OEGrapheme:: OESurfaceArcStyle:: Sun, 188 OEGrapheme:: OEColorGradientLabel, 96 OEGrapheme:: OESurfaceArcStyle:: Wreath, OEGrapheme:: OEColorOverlapDisplayOptions, 188 100 OEGrapheme:: OEWreathArcFxn, 160 OEGrapheme:: OEComplexSurfaceArcFxnBase, Constructors, 160 136 OEGrapheme:: OEDepictionFrom3DOptions, CreateCopy, 161 operator(), 161 102 OEGrapheme:: OEPeptideDisplayOptions,  $operator!=$ OEGrapheme:: OEPlotMarker, 110 106 OEGrapheme:: OEPlotMarker, 109 operator() OEGrapheme:: OEAlphaRainbowArcFxn, OEGrapheme:: OERamachandranPlot, 112 OEGrapheme:: OEShapeOverlapDisplay, 131 OEGrapheme:: OEBrickRoadArcFxn, 132 117 OEGrapheme:: OEShapeOverlapDisplayOptions, OEGrapheme:: OECastleArcFxn, 133

OEGrapheme:: OEColorForceFieldDisplay,

OEGrapheme:: OEColorGradientDisplayOptions,

OEGrapheme:: OEColorGradientDisplayOptions,

OEGrapheme:: OEColorGradientDisplayOptions,

OEGrapheme:: OEDepictionFrom3DOptions,

OEGrapheme:: OEShapeQueryDisplayOptions,

#### 119

```
OEGrapheme:: OEShapeQueryDisplay, 123
                                                  98
   OEGrapheme::OEShapeQueryDisplayOptionSetColorAtomStyle
       124OEGrapheme:: OEShapeQueryDisplayOptions,
   OEGrapheme:: OESurfaceArc, 128
                                                  126
                                          SetColorStopLabelFont
operator==
   OEGrapheme:: OEPlotMarker, 110
                                              OEGrapheme:: OEColorGradientDisplayOptions,
```

 $91$ 

92

92

 $Q<sub>3</sub>$ 

103

126

SetDepth

SetDepictOrientation

SetColorStopPrecision

SetColorStopVisibility

SetCoordsToInertialFrame

SetColorStopLabelFontScale

# R

```
Render
   OEGrapheme:: OE2DPropMap, 59
RenderGlyph
   OEGrapheme:: OEAtomGlyphBase, 71
   OEGrapheme:: OEAtomGlyphCircle, 72
   OEGrapheme:: OEBondGlyphArrow, 73
   OEGrapheme:: OEBondGlyphBase, 74
   OEGrapheme:: OEBondGlyphCircle, 76
   OEGrapheme:: OEBondGlyphCross, 77
   OEGrapheme:: OEBondGlyphCurvedArrow,
       79
   OEGrapheme:: OEBondGlyphScissors, 80
   OEGrapheme:: OEBondGlyphStitch, 82
   OEGrapheme:: OEBondGlyphZiqZaq, 83
```

# S

```
OEGrapheme:: OEComplexSurfaceArcFxnBase,
                                                  137
SetAminoAcidScale
   OEGrapheme:: OEPeptideDisplayOptions, SetDimensions
                                              OEGrapheme:: OE2DActiveSiteDisplayOptions,
       107
                                                  54
SetAtomDisplay
                                          SetEndAngle
   OEGrapheme:: OESurfaceArc, 129
                                              OEGrapheme:: OESurfaceArc, 129
SetBackgroundColor
   OEGrapheme::OE2DActiveSiteDisplayOptiSht5",
                                              OEGrapheme:: OE2DActiveSiteDisplayOptions,
       54
                                                 55
SetBqnAnqle
                                          SetInteractive
   OEGrapheme:: OESurfaceArc, 129
                                              OEGrapheme:: OEPeptideDisplayOptions,
SetBoxRange
                                                  108
   OEGrapheme:: OEColorGradientDisplayOptions,
                                          SetLabelStyle
       90
                                              OEGrapheme:: OEPeptideDisplayOptions,
SetBoxRangePen
                                                  108
   OEGrapheme:: OEColorGradientDisplayOptions,
                                          SetLegendFont
                                              OEGrapheme:: OE2DPropMap, 61
SetCenter
                                          SetLegendFontScale
   OEGrapheme:: OESurfaceArc, 129
                                              OEGrapheme:: OE2DPropMap, 61
SetClearBackground
   OEGrapheme::OEColorOverlapDisplayOptiShtsLegendLocation
                                              OEGrapheme:: OE2DPropMap, 62
       101
   OEGrapheme::OEShapeOverlapDisplayOptiSotSMarkedValuePen
                                              OEGrapheme:: OEColorGradientDisplayOptions,
       120
                                                 Q_{\Delta}OEGrapheme:: OEShapeQueryDisplayOptions,
                                           SetMarkedValuePrecision
       126
                                              OEGrapheme:: OEColorGradientDisplayOptions,
SetClearCoords
   OEGrapheme::OEAlignedDepictionFrom3DOptions, 94
                                           SetMarkedValues
       69
                                              OEGrapheme::OEColorGradientDisplayOptions,
SetColor
```

94 SetSurfaceArcFxn SetMaxBondRotations OEGrapheme:: OEShapeQueryDisplayOptions, OEGrapheme:: OEAlignedDepictionFrom3DOptions,126 SetSVGMagnifyResidueInHover 69 OEGrapheme:: OEDepictionFrom3DOptions, OEGrapheme:: OE2DActiveSiteDisplayOptions, 104 56 SetMaxValue SetWidth OEGrapheme:: OE2DPropMap, 63 OEGrapheme:: OE2DActiveSiteDisplayOptions, SetMinValue 56 OEGrapheme:: OE2DPropMap, 64 shapeoverlap2pdf.py SetName Example Code, 41 OEGrapheme:: OEColorForceFieldDisplay, 98 SetNegativeColor OEGrapheme:: OE2DPropMap, 65 SetOverlapColor OEGrapheme:: OEShapeOverlapDisplayOptions, 121 SetOverlapDisplayStyle OEGrapheme:: OEShapeOverlapDisplayOptions, 121 SetPositiveColor OEGrapheme:: OE2DPropMap, 65 SetQuerySurfaceArcFxn OEGrapheme:: OEColorOverlapDisplayOptions, 101 OEGrapheme:: OEShapeOverlapDisplayOptions, 121 SetRadius OEGrapheme:: OESurfaceArc, 129 SetRadiusRatio OEGrapheme:: OE2DPropMap, 66 SetRenderInteractiveLegend OEGrapheme:: OE2DActiveSiteDisplayOptions, 55 SetResidueSVGMarkupFunctor OEGrapheme:: OE2DActiveSiteDisplayOptions, 55 SetResolution OEGrapheme:: OE2DPropMap, 67 SetRotateTo2DReference OEGrapheme:: OEDepictionFrom3DOptions,  $104$ SetScale OEGrapheme:: OE2DActiveSiteDisplayOptions, 56 SetSuperAtomStyle OEGrapheme:: OE2DActiveSiteDisplayOptions, 56 SetSuppressHydrogens OEGrapheme:: OEAlignedDepictionFrom3DOptions, 70 OEGrapheme:: OEDepictionFrom3DOptions, 104