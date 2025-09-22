![](_page_0_Picture_0.jpeg)

**Shape TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1 Theory                                               | 1 |
|--------------------------------------------------------|---|
| 1.1 Theory                                             | 1 |
| 1.1.1 Molecular Shape                                  | 1 |
| 1.1.2 Shape Characteristics and the Use of Gaussians   | 1 |
| 1.1.3 Shape from Hermite Representation                | 1 |
| 1.1.4 Color Features                                   | 1 |
| 1.1.5 Similarity Measures                              | 1 |
| 1.1.6 Implementation Details and Usage                 | 1 |
| 2 Examples                                             | 1 |
| 2.1 Calculating Overlap                                | 1 |
| 2.1.1 Simple Overlap                                   | 1 |
| 2.1.2 Adding overlap to molecules                      | 1 |
| 2.1.3 Color Overlap                                    | 1 |
| 2.1.4 Adding color score to molecules                  | 1 |
| 2.1.5 User Defined Color                               | 1 |
| 2.1.6 Shape and Color Overlap                          | 1 |
| 2.2 ROCS                                               | 2 |
| 2.2.1 Best Hit                                         | 2 |
| 2.2.2 Top Hits                                         | 2 |
| 2.2.3 Top Hits with Multiple Conformers                | 2 |
| 2.3 Overlay Optimization                               | 2 |
| 2.3.1 Best Optimization Result                         | 2 |
| 2.3.2 All Optimization Results                         | 2 |
| 2.3.3 Manipulating all results                         | 2 |
| 2.4 Working with Shape Query                           | 3 |
| 2.4.1 Creating a shape query                           | 3 |
| 2.4.2 Overlap with shape query                         | 3 |
| 2.4.3 Top hit against shape query                      | 3 |
| 2.5 Shape from Hermite expansion                       | 3 |
| 2.5.1 Hermite expansion                                | 3 |
| 2.5.2 Hermite Tanimoto comparison of shape             | 3 |
| 2.6 Flexible Overlay with Shape, Color, and Forcefield | 4 |
| 2.6.1 Flexible Overlay                                 | 4 |
| 2.6.2 Flexible Best Overlay                            | 4 |
| 2.7 Advanced Examples                                  | 4 |
| 2.7.1 Calculating NxN scores                           | 4 |
| 2.7.2 Calculating shape characteristics                | 4 |
| 2.7.3 Calculating excluded volume                      | 4 |

| $\mathbf{3}$ | <b>API</b> |        | 5                            |
|--------------|------------|--------|------------------------------|
|              | 3.1        |        | OEShape Classes<br>5         |
|              |            | 3.1.1  | OEAnalyticColorFunc<br>5     |
|              |            | 3.1.2  | OEAnalyticOptions<br>5       |
|              |            | 3.1.3  | OEAnalyticShapeFunc<br>5     |
|              |            | 3.1.4  | OEAsIsStarts<br>5            |
|              |            | 3.1.5  | OEAtomStarts<br>5            |
|              |            | 3.1.6  | OEBestOverlayResults<br>5    |
|              |            | 3.1.7  | OEBestOverlayScore<br>5      |
|              |            | 3.1.8  | OECartesianStarts<br>6       |
|              |            | 3.1.9  | OEColorFFParameter<br>6      |
|              |            | 3.1.10 | OEColorForceField<br>6       |
|              |            | 3.1.11 | OEColorFunc<br>6             |
|              |            | 3.1.12 | OEColorOptions<br>6          |
|              |            | 3.1.13 | OEColorTanimotoCutoff<br>6   |
|              |            | 3.1.14 | OEExactColorFunc<br>6        |
|              |            | 3.1.15 | OEExactShapeFunc<br>7        |
|              |            | 3.1.16 | OEFitColorTverskyCutoff<br>7 |
|              |            | 3.1.17 | OEFitTverskyComboCutoff<br>7 |
|              |            | 3.1.18 | OEFitTverskyCutoff<br>7      |
|              |            | 3.1.19 | OEFlexiOverlapFunc<br>7      |
|              |            | 3.1.20 | Overlap<br>7                 |
|              |            | 3.1.21 | SetupRef<br>7                |
|              |            | 3.1.22 | UpdateColorCoords<br>7       |
|              |            | 3.1.23 | OEFlexiOverlapOptions<br>7   |
|              |            | 3.1.24 | Validate<br>7                |
|              |            | 3.1.25 | GetShapeFuncType<br>7        |
|              |            | 3.1.26 | GetColorFuncType<br>7        |
|              |            | 3.1.27 | GetForceField<br>7           |
|              |            | 3.1.28 | GetHarmonic<br>7             |
|              |            | 3.1.29 | GetShapeOptions<br>7         |
|              |            | 3.1.30 | GetColorOptions<br>7         |
|              |            | 3.1.31 | GetOverlapFunc<br>7          |
|              |            | 3.1.32 | SetShapeFuncType<br>7        |
|              |            | 3.1.33 | SetColorFuncType<br>7        |
|              |            | 3.1.34 | SetForceField<br>7           |
|              |            | 3.1.35 | SetHarmonic<br>7             |
|              |            | 3.1.36 | SetShapeOptions<br>7         |
|              |            | 3.1.37 | SetColorOptions<br>7         |
|              |            | 3.1.38 | SetOverlapFunc<br>7          |
|              |            | 3.1.39 | OEFlexiOverlapResults<br>7   |
|              |            | 3.1.40 | OEFlexiOverlay<br>7          |
|              |            | 3.1.41 | SetupRef<br>7                |
|              |            | 3.1.42 | Overlay<br>7                 |
|              |            | 3.1.43 | SortedOverlay<br>7           |
|              |            | 3.1.44 | BestOverlay<br>7             |
|              |            | 3.1.45 | OEFlexiOverlayOptions<br>7   |
|              |            | 3.1.46 | GetMaxOptSteps<br>8          |
|              |            | 3.1.47 | GetRigidOverlay<br>8         |
|              |            | 3.1.48 | GetFlexiOverlapOptions<br>8  |
|              |            | 3.1.49 | GetRigidOverlayOptions<br>8  |
|              |            | 3.1.50 | SetMaxOptSteps<br>8          |
|              |            | 3.1.51 | SetRigidOverlay<br>8         |
|              |            | 3.1.52 | SetFlexiOverlapOptions<br>8  |

| Section | Title                    | Page |
|---------|--------------------------|------|
| 3.1.53  | SetRigidOverlayOptions   | 8    |
| 3.1.54  | OEGridColorFunc          | 8    |
| 3.1.55  | OEGridShapeFunc          | 8    |
| 3.1.56  | OEHermite                | 8    |
| 3.1.57  | CreateGrid               | 8    |
| 3.1.58  | GetCoefficients          | 8    |
| 3.1.59  | GetOptions               | 8    |
| 3.1.60  | GetSelfOverlap           | 8    |
| 3.1.61  | Setup                    | 8    |
| 3.1.62  | OEHermiteOptions         | 8    |
| 3.1.63  | OEHermiteShapeFunc       | 8    |
| 3.1.64  | OEHighestColorTanimoto   | 9    |
| 3.1.65  | OEHighestFitColorTversky | 9    |
| 3.1.66  | OEHighestFitTversky      | 9    |
| 3.1.67  | OEHighestFitTverskyCombo | 9    |
| 3.1.68  | OEHighestOverlap         | 9    |
| 3.1.69  | OEHighestRefColorTversky | 9    |
| 3.1.70  | OEHighestRefTversky      | 9    |
| 3.1.71  | OEHighestRefTverskyCombo | 9    |
| 3.1.72  | OEHighestScaledColor     | 9    |
| 3.1.73  | OEHighestTanimoto        | 9    |
| 3.1.74  | OEHighestTanimotoCombo   | 9    |
| 3.1.75  | OEHighestTverskyCombo    | 9    |
| 3.1.76  | OEInertialStarts         | 9    |
| 3.1.77  | OEIsColorAtomPred        | 9    |
| 3.1.78  | OEMultiRefOverlay        | 9    |
| 3.1.79  | OEOverlapCutoff          | 9    |
| 3.1.80  | OEOverlapFunc            | 10   |
| 3.1.81  | GetColorFunc             | 10   |
| 3.1.82  | GetShapeFunc             | 10   |
| 3.1.83  | OEOverlapFuncBase        | 10   |
| 3.1.84  | Overlap                  | 10   |
| 3.1.85  | SetupFlex                | 10   |
| 3.1.86  | SetupRef                 | 10   |
| 3.1.87  | OEOverlapPrep            | 10   |
| 3.1.88  | OEOverlapPrepOptions     | 10   |
| 3.1.89  | OEOverlapResults         | 10   |
| 3.1.90  | OEOverlay                | 11   |
| 3.1.91  | BestOverlay              | 11   |
| 3.1.92  | GetOverlayOptions        | 11   |
| 3.1.93  | Overlay                  | 11   |
| 3.1.94  | SetupRef                 | 11   |
| 3.1.95  | SortedOverlay            | 11   |
| 3.1.96  | OEOverlayOptions         | 11   |
| 3.1.97  | GetColorFuncType         | 11   |
| 3.1.98  | GetColorOptions          | 11   |
| 3.1.99  | GetMaxOptSteps           | 11   |
| 3.1.100 | GetOverlapFunc           | 11   |
| 3.1.101 | GetShapeFuncType         | 11   |
| 3.1.102 | GetShapeOptions          | 11   |
| 3.1.103 | GetStarts                | 11   |
| 3.1.104 | SetColorFuncType         | 11   |
| 3.1.105 | SetColorOptions          | 11   |
| 3.1.106 | SetMaxOptSteps           | 11   |

| Section / Entry                       | Page |
|---------------------------------------|------|
| 3.1.107 SetOverlapFunc                | 115  |
| 3.1.108 SetShapeFuncType              | 116  |
| 3.1.109 SetShapeOptions               | 116  |
| 3.1.110 SetStarts                     | 116  |
| 3.1.111 OEOverlayScoreCutoff          | 116  |
| 3.1.112 OEQuatStarts                  | 117  |
| 3.1.113 OERefColorTverskyCutoff       | 118  |
| 3.1.114 OERefTverskyComboCutoff       | 118  |
| 3.1.115 OERefTverskyCutoff            | 119  |
| 3.1.116 OERandomStarts                | 119  |
| 3.1.117 OEROCS                        | 121  |
| 3.1.118 OEROCSOptions                 | 122  |
| 3.1.119 OEROCSResult                  | 123  |
| 3.1.120 OEShapeFunc                   | 128  |
| 3.1.121 OEShapeGridOptions            | 130  |
| 3.1.122 OEShapeOptions                | 131  |
| 3.1.123 OEStarts                      | 133  |
| 3.1.124 OEShapeQuery                  | 134  |
| 3.1.125 OEShapeQueryBase              | 138  |
| 3.1.126 OESubrocsStarts               | 142  |
| 3.1.127 OETanimotoComboCutoff         | 143  |
| 3.1.128 OETanimotoCutoff              | 144  |
| 3.2 OEShape Constants                 | 144  |
| 3.2.1 OEColorFFType                   | 144  |
| 3.2.2 OEDerivativeType                | 145  |
| 3.2.3 OEExponentialType               | 145  |
| 3.2.4 OEMomentSymmetry                | 146  |
| 3.2.5 OEOverlapRadii                  | 146  |
| 3.2.6 OEScoreType                     | 147  |
| 3.2.7 OEShapeType                     | 147  |
| 3.2.8 OEColorType                     | 148  |
| 3.3 OEShape Functions                 | 148  |
| 3.3.1 OEAddColorAtom                  | 149  |
| 3.3.2 OEAddColorAtoms                 | 149  |
| 3.3.3 OEAddCoordsToColorAtom          | 149  |
| 3.3.4 OECalcShapeMultipoles           | 149  |
| 3.3.5 OECalcVolume                    | 149  |
| 3.3.6 OEClearCachedSelfColor          | 150  |
| 3.3.7 OEClearCachedSelfShape          | 150  |
| 3.3.8 OECompressColorAtoms            | 150  |
| 3.3.9 OECountColorAtoms               | 150  |
| 3.3.10 OEDeleteCompressedColorAtoms   | 150  |
| 3.3.11 OEGetCachedSelfColor           | 150  |
| 3.3.12 OEGetCachedSelfShape           | 150  |
| 3.3.13 OEGetCenterAndExtents          | 151  |
| 3.3.14 OEGetColorAtoms                | 151  |
| 3.3.15 OEGetColorParents              | 152  |
| 3.3.16 OEGetColorType                 | 152  |
| 3.3.17 OEGetMomentsOfInertiaTransform | 152  |
| 3.3.18 OEHasCachedSelfColor           | 152  |
| 3.3.19 OEHasCachedSelfShape           | 152  |
| 3.3.20 OEHasColorAtoms                | 153  |
| 3.3.21 OEHasCompressedColorAtoms      | 153  |
| 3.3.22 OEHasPerceivedColorAtoms       | 153  |

| Number   | Description                  | Page |
|----------|------------------------------|------|
| 3.3.23   | OEIsColorAtom                | 15   |
| 3.3.24   | OEIsFastROCSShapeQuery       | 15   |
| 3.3.25   | OEMol2Query                  | 15   |
| 3.3.26   | OEOrientByMomentsOfInertia   | 15   |
| 3.3.27   | OEReadShapeQuery             | 15   |
| 3.3.28   | OERemoveColorAtoms           | 15   |
| 3.3.29   | OEROCSOverlay                | 15   |
| 3.3.30   | OESelfColor                  | 15   |
| 3.3.31   | OESelfShape                  | 15   |
| 3.3.32   | OESetCachedSelfColor         | 15   |
| 3.3.33   | OESetCachedSelfShape         | 15   |
| 3.3.34   | OESetColorParents            | 15   |
| 3.3.35   | OESetColorType               | 15   |
| 3.3.36   | OESetCoordsFromColorParents  | 15   |
| 3.3.37   | OEShapeGetArch               | 15   |
| 3.3.38   | OEShapeGetLicensee           | 15   |
| 3.3.39   | OEShapeGetPlatform           | 15   |
| 3.3.40   | OEShapeGetRelease            | 15   |
| 3.3.41   | OEShapeGetSite               | 15   |
| 3.3.42   | OEShapeGetVersion            | 15   |
| 3.3.43   | OEShapeIsLicensed            | 15   |
| 3.3.44   | OESortOverlayScores          | 15   |
| 3.3.45   | OEUncompressColorAtoms       | 15   |
| 3.3.46   | OEWriteShapeQuery            | 15   |
| <b>4</b> | <b>Deprecated API</b>        | 15   |
| 4.1      | Deprecated OEShape Classes   | 15   |
| 4.1.1    | OEBestOverlay                | 15   |
| 4.1.2    | OEColorOverlap               | 16   |
| 4.1.3    | OEColorResults               | 16   |
| 4.1.4    | OEHighestComboScore          | 16   |
| 4.1.5    | OEOverlap                    | 16   |
| 4.1.6    | OEShapeQueryPublic           | 17   |
| 4.2      | Deprecated OEShape Constants | 17   |
| 4.2.1    | OEBOMinType                  | 17   |
| 4.2.2    | OEBOOrientation              | 17   |
| 4.2.3    | OEOverlapMethod              | 17   |
| 4.2.4    | OEOverlapRepresentation      | 17   |
| <b>5</b> | <b>Release History</b>       | 17   |
| 5.1      | Shape TK 3.7.0               | 17   |
| 5.1.1    | New features                 | 17   |
| 5.1.2    | Minor bug fixes              | 17   |
| 5.2      | Shape TK 3.6.2               | 17   |
| 5.2.1    | New features                 | 17   |
| 5.3      | Shape TK 3.6.1               | 17   |
| 5.3.1    | Major bug fixes              | 17   |
| 5.4      | Shape TK 3.6.0               | 17   |
| 5.4.1    | New features                 | 17   |
| 5.4.2    | Major bug fixes              | 17   |
| 5.4.3    | Minor bug fixes              | 17   |
| 5.5      | Shape TK 3.5.1               | 17   |
| 5.5.1    | New features                 | 17   |
| 5.5.2    | Major bug fixes              | 17   |

| 5.5.3 Minor bug fixes          | 176 |
|--------------------------------|-----|
| 5.5.4 Documentation changes    | 179 |
| 5.6 Shape TK 3.5.0             | 180 |
| 5.6.1 New features             | 180 |
| 5.6.2 Minor bug fixes          | 180 |
| 5.7 Shape TK 3.4.3             | 180 |
| 5.7.1 New features             | 180 |
| 5.7.2 Minor bug fixes          | 180 |
| 5.8 Shape TK 3.4.2             | 181 |
| 5.8.1 Major bug fixes          | 181 |
| 5.9 Shape TK 3.4.1             | 182 |
| 5.9.1 New features             | 182 |
| 5.9.2 Major bug fixes          | 182 |
| 5.9.3 Minor bug fixes          | 182 |
| 5.10 Shape TK 3.4.0            | 182 |
| 5.10.1 Minor bug fixes         | 182 |
| 5.11 Shape TK 2.0.4            | 182 |
| 5.11.1 New features            | 182 |
| 5.11.2 Minor bug fixes         | 182 |
| 5.12 Shape TK 2.0.3            | 182 |
| 5.12.1 New features            | 182 |
| 5.12.2 Minor bug fixes         | 182 |
| 5.12.3 Documentation changes   | 182 |
| 5.13 Shape TK 2.0.2            | 183 |
| 5.13.1 New features            | 183 |
| 5.13.2 Minor bug fixes         | 183 |
| 5.13.3 Java-specific changes   | 183 |
| 5.13.4 C#-specific changes     | 183 |
| 5.13.5 Documentation changes   | 183 |
| 5.14 Shape TK 2.0.1            | 184 |
| 5.14.1 New features            | 184 |
| 5.14.2 Minor bug fixes         | 184 |
| 5.14.3 Documentation changes   | 184 |
| 5.15 Shape TK 2.0.0            | 184 |
| 5.15.1 New features            | 184 |
| 5.15.2 Minor bug fixes         | 184 |
| 5.15.3 Documentation changes   | 184 |
| 5.16 Shape TK 1.11.0           | 186 |
| 5.16.1 New features            | 186 |
| 5.16.2 Documentation changes   | 187 |
| 5.17 Shape TK 1.10.4           | 187 |
| 5.18 Shape TK 1.10.3           | 187 |
| 5.18.1 Python-specific changes | 187 |
| 5.18.2 Java-specific changes   | 187 |
| 5.19 Shape TK 1.10.2           | 187 |
| 5.19.1 Major bug fixes         | 187 |
| 5.19.2 Minor bug fixes         | 187 |
| 5.20 Shape TK 1.10.1           | 188 |
| 5.20.1 New features            | 188 |
| 5.20.2 Documentation changes   | 188 |
| 5.21 Shape TK 1.10.0           | 188 |
| 5.21.1 Minor bug fixes         | 188 |
| 5.22 Shape TK 1.9.7            | 188 |
| 5.22.1 New features            | 188 |

| 5.22.2 | Major bug fixes       | 18 |
|--------|-----------------------|----|
| 5.22.3 | Minor bug fixes       | 18 |
| 5.22.4 | Documentation changes | 18 |
| 5.23   | Shape TK 1.9.6        | 18 |
| 5.23.1 | New features          | 18 |
| 5.23.2 | Major bug fixes       | 18 |
| 5.23.3 | Minor bug fixes       | 18 |
| 5.24   | Shape TK 1.9.5        | 18 |
| 5.24.1 | New features          | 18 |
| 5.24.2 | Major bug fixes       | 18 |
| 5.25   | Shape TK 1.9.4        | 18 |
| 5.25.1 | Major bug fixes       | 18 |
| 5.25.2 | Minor bug fixes       | 18 |
| 5.26   | Shape TK 1.9.3        | 19 |
| 5.27   | Shape TK 1.9.2        | 19 |
| 5.27.1 | Minor bug fixes       | 19 |
| 5.28   | Shape TK 1.9.1        | 19 |
| 5.28.1 | Bug fixes             | 19 |
| 5.29   | Shape TK 1.9.0        | 19 |
| 5.29.1 | New features          | 19 |
| 5.29.2 | Major bug fixes       | 19 |
| 5.29.3 | Minor bug fixes       | 19 |
| 5.30   | Shape TK 1.8.3        | 19 |
| 5.30.1 | New features          | 19 |
| 5.30.2 | Minor bug fixes       | 19 |
| 5.31   | Shape TK 1.8.2        | 19 |
| 5.32   | Shape TK 1.8.1        | 19 |
| 5.32.1 | Bug fixes             | 19 |
| 5.33   | Shape TK 1.8.0        | 19 |
| 5.33.1 | New features          | 19 |
| 5.33.2 | Bug fixes             | 19 |
| 5.34   | Shape TK 1.7.2        | 19 |
| 5.34.1 | New features          | 19 |
| 5.34.2 | Bug fixes             | 19 |
| 5.35   | Shape TK 1.7.1        | 19 |
| 5.35.1 | New features          | 19 |
| 5.35.2 | Bug fixes             | 19 |
| 5.36   | Shape TK 1.7.0        | 19 |
| 5.36.1 | New features          | 19 |
| 5.36.2 | Bug fixes             | 19 |
| 5.37   | Shape TK 1.6.2        | 19 |
| 5.37.1 | New features          | 19 |
| 5.37.2 | Bug fixes             | 19 |
| 5.38   | Shape TK 1.6.1        | 19 |
| 5.38.1 | New features          | 19 |
| 5.38.2 | Bug fixes             | 19 |
| 5.39   | Shape TK 1.6          | 19 |
| 5.39.1 | New features          | 19 |
| 5.39.2 | Bug fixes             | 19 |
| 5.40   | Shape TK 1.5          | 19 |
| 5.40.1 | New features          | 19 |

# Copyright and Trademarks

| 7     | Sample Code                   | 199 |
|-------|-------------------------------|-----|
| 8     | <b>Citation</b>               | 201 |
| 8.1   | Orion ® Floes                 | 201 |
| 8.2   | Toolkits and Applications     | 201 |
| 8.3   | OpenEye Web Services          | 203 |
| 9     | <b>Technology Licensing</b>   | 205 |
| 9.1   | GCC                           | 220 |
| 9.1.1 | GCC RUNTIME LIBRARY EXCEPTION | 220 |
| 9.1.2 | GNU GENERAL PUBLIC LICENSE    | 222 |
|       | <b>Index</b>                  | 235 |

### **CHAPTER**

# **ONE**

# **THEORY**

# 1.1 Theory

### **1.1.1 Molecular Shape**

What do we mean by shape? The word is often used without consideration of precise meaning but in this document we shall be very clear as to the definition of shape. Two entities will have the same shape if their volumes exactly correspond. The more the volumes differ, the more the shapes will differ. We will give a precise mathematical exposition below, but it is worth noting even at this most basic level shape is defined as a relative quantity, depending on references to other shapes. In this we differ from approaches that attempt to provide absolute, canonical, *shapes* by which to categorize molecules.

What do we mean by *volume*? A volume is any scalar field. This means a function that has a single number, or *scalar*, value at each point in space. The *special case* for the common understanding of volume is a specific scalar field that has a value of one inside an object and zero outside. The volume of a scalar field is:

$$
V(\text{volume}) = \int f(x, y, z) \, dx
$$

The volume function, f, is also referred to as the *characteristic* function. When the characteristic function corresponds to the common definition of a volume field this integral corresponds to what is commonly expected by volume. However, we are not restricted to such simple functions and can still calculate a V. In general the volume of a scalar field is a *contraction* of the information represented by that characteristic function. It is more precisely referred to as the zeroth-order contraction, or *moment*. We will discuss other moments and their uses later, but one immediate observation is that two objects can not have the same shape if their volumes are not the same. The converse is obviously not true. Rather, two objects can have the same volume and not have the same shape. Volume is typical, therefore, of most contractions of information.

We can now write down a precise definition of shape similarity. Consider the integral:

$$
S_1 = \int |f(x, y, z) - g(x, y, z)| dV
$$

where f and g are different characteristic functions. If this integral is zero then f and g are actually the same function and therefore correspond to the same shape. The larger the integral, the more different the shapes defined by f and g. It defines a metric quantity between the two fields  $f$  and  $g$ . The word *metric* is used loosely to mean *shape*, but here we mean the precise mathematical definition: *i.e.* a distance that is 1) always positive, 2) zero if and only if two entities are identical and 3) that obeys the triangle inequality. The triangle inequality states that if entity A is distance x from entity B and B is distance y from entity C then the distance between A and C is bounded by  $|x-y|$  and  $|x+y|$ . The type of comparison shown in  $S_1$  is referred to as an  $L_1$  metric. Another metric is the  $S_2$  metric:

$$
S_2 = \sqrt{\int [f(x, y, z) - g(x, y, z)]^2} dV
$$

Multiplying the terms in the integral out gives:

$$
S_2^2 = \int f(x, y, z)^2 dV + \int g(x, y, z)^2 dV - 2 \int f(x, y, z) g(x, y, z) dV
$$

This is the fundamental equation for shape comparison. We rewrite it as:

$$
S_{f,g} = I_f + I_g - 2O_{f,g}
$$

The I terms are the self-volume overlaps of each entity (for our purposes - molecule), while the  $O$  term is the overlap between the two functions. They constitute the three terms we need to compare the shapes of two fields. The I terms are independent of orientation but not O. Finding the orientation that maximizes O, and hence minimizes  $S_{f,s}$ , is equivalent to finding the best overlay between the two objects (a quantity that has its own, distinct metric properties). We also note here that the quantity referred to as a Tanimoto coefficient may be derived by recombining  $I$ 's and  $O$  so:

$$
Tanimoto_{f,g} = \frac{O_{f,g}}{I_f + I_g - O_{f,g}}
$$

Tanimoto coefficients will be familiar to those who use them for bitvector fingerprint comparison. An alternative measure is the Tversky coefficient, also mostly used for similarity between bitvector fingerprints. Similarly to the Tanimoto coefficient above, we can define a shape Tversky measure. The base equation for the Tversky coefficient is:

$$
Tversky_{f,g} = \frac{O_{f,g}}{\alpha I_f + \beta I_g}
$$

Normally,  $alpha + beta = 1$ , and for our current use,  $alpha$  is chosen to be 0.95. Since this introduces an asymmetry, the Tversky calculation depends on which molecule's self-overlap has the *alpha* pre-factor. ROCS calculates two Tversky values, one with the query molecule with *alpha* as the pre-factor and a second with the database molecule with *alpha* as the pre-factor. Also, note that since shape is a field property, instead of a simple scalar like a bitvector, shape Tversky can be larger than 1.0 since the overlap  $O_{f,g}$  can be larger than a molecule's self-overlap,  $I_f$ .

The OpenEye Shape Toolkit is a set of calculational objects designed to facilitate the calculation of these field-metric quantities. ROCS is an application built on top of the Shape toolkit.

### 1.1.2 Shape Characteristics and the Use of Gaussians

Molecules are traditionally viewed as a set of fused spheres, sometimes referred to as the CPK model. The common view of molecular volume is then of a characteristic function that is one  $(1)$  inside at least one sphere and zero  $(0)$ outside. How do we calculate the volume of such a seemingly simple function? The volume of a single sphere is  $(4pi)$  $r^2/3$  but the complication for two fused spheres is that we have to account for the shared volume and not count it twice. For more than two atoms, there are triple intersections that must be added back in if we have removed the three pairs of intersections. The general formula for N spheres that explicitly calculates the volume of every level of overlap and its correct contribution is:

$$
V = 1 - \int \prod_{i}^{N} (1 - f_i) dv
$$

This is easy to write, not so easy to solve because the analytic formulae for overlaps of increasing order are highly non-trivial (although they have been derived to arbitrary order). It is fair to say that this has hindered the development of shape comparison in many ways. Attempts to use analytic formulae led to very slow programs and approximate methods, for instance using grids of points that are turned in or *out* by each sphere, do not give smooth gradients required for minimization. Brian Masek (AstraZeneca) was the first to attempt to optimize overlaps of molecules using the analytic approach [Masek-1993]. His program would take several minutes per minimization. In addition it would often suffer from a common problem when using functions that vary sharply (such as solid spheres): it would often get stuck in local minima. Nevertheless, Brian did have encouraging success using this method to find similarities not obvious from chemical structure.

The conceptual breakthrough in shape comparison came in 1995 in a paper by Andrew Grant (AstraZeneca) and Barry Pickup (University of Sheffield) ([Grant-1995], [Grant-1996], [Grant-1997]). They showed that if one let go of the concept of the characteristic function being binary, and instead use a sum of continuous functions, *i.e.* a Gaussian, that the solid-sphere volume, could be recovered to high accuracy (typically  $\sim 0.1\%$ ). A sphere has one defining parameter, its radius, whereas a Gaussian has two defining parameters, its prefactor,  $p$ , and its width,  $w$ :

$$
pe^{-wx^2}
$$

Grant and Pickup found that by fixing  $p$  to 2.7 and setting  $w$  for each atom such that the volume integral for each atom agreed with its solid-sphere volume, they achieved remarkable precision. In addition, the overlap terms between any two atoms, and hence any higher-order overlaps, are all Gaussian functions themselves because of the Gaussian Contraction formula (shown here for one spatial variable):

$$
\int e^{a(x-x_i)^2} e^{b(x-x_i)^2} = \int e^{(a+b)(x-x_i)^2}
$$

i.e. two atomic-Gaussians overlap to produce another Gaussian. Likewise, a three atomic-Gaussian overlap is that of an overlap-Gaussian with an atomic-Gaussian, hence another Gaussian. The simplicity of these formulae and the formula for the volume of each individual Gaussian leads to very efficient algorithms for the calculation of the volume of a molecule so represented (the OpenEye method calculates several thousand volumes per second while calculating intersections up to sixth order).

In addition to simple calculation of molecular volume, which is the zeroth-order moment of the characteristic function, the ease of evaluation of intersections allows for accurate calculation of high-order moments: called the *steric* multipoles. For instance, if the product formulae for atomic and intersection Gaussians yields n Gaussians, the first order moments are:

$$
M_{1,x} = \sum_{i=1}^{n} \int xe^{a_i|(x-x_i)^2 + (y-y_i)^2 + (z-z_i)^2|}
$$
  
\n
$$
M_{1,y} = \sum_{i=1}^{n} \int ye^{a_i|(x-x_i)^2 + (y-y_i)^2 + (z-z_i)^2|}
$$
  
\n
$$
M_{1,z} = \sum_{i=1}^{n} \int ze^{a_i|(x-x_i)^2 + (y-y_i)^2 + (z-z_i)^2|}
$$

These integrals are easy to solve and their sum can be set to zero by an appropriate choice of origin: the center of *mass* for the sum of Gaussians. Second-order moments are found from integrals of the type:

$$
M_{2,PQ} = \sum_{i=1}^{n} \int PQ e^{a_i |(x-x_i)^2 + (y-y_i)^2 + (z-z_i)^2|}
$$

where P and Q are chosen from  $(x,y,z)$ , e.g.  $x^2$ , xy etc.

These moments can be thought of as a symmetric  $3*3$  matrix which we refer to as the *mass matrix*. Rotating or translating the molecule will change the moments and the transform that sets the first-order moments to zero and diagonalizes the mass-matrix puts the molecule into its *inertial frame*. By convention we assign the x-axis to the largest eigenvector of the mass matrix, y-axis to the median eigenvector, z-axis to the smallest. Note that this orientation is still not uniquely defined: 180 degree rotations around any axis also diagonalize the mass-matrix. The eight  $(2^3)$  possible transforms that can be generated by combinations of such rotations actually lead to four unique inertial orientations.

If a molecule is aligned to its inertial frame, all higher-order steric multipoles become invariant, ignoring certain signchanges from the four-fold degeneracy of the inertial frame. As such they, as well as the second-order moments, are shape *descriptors*. They are still contractions of the information contained in the characteristic field, *i.e.* two molecules can have the same steric moments and yet have different shapes. (Moments are *complete* in that if we calculate them to infinite order they do exactly define volume but this is seldom a practical approach!) Nevertheless, they do contain useful information and can be used as a rapid, approximate, filter for shape similarity.

The same advantages that allow for the calculation of molecular volume carry over to the calculation of molecular volume overlap. The overlap of volumes are Gaussian contractions, easily tabulated and efficiently retrieved. Andy rewrote Brian's program and obtained an order-of-magnitude improvement in performance as well as another remarkable observation: if the starting orientation of each molecule is that given from the inertial frame then very few "false" minima are produced. The smoothness of the Gaussian characteristic function is enough to overcome the problems with convergence in Brian's program. The four possible "inertial" starting points were enough to find the best, global, overlay between two molecules. This observation and the Gaussian approach are the basis of the OpenEye Shape Toolkit and ROCS program for rapid shape overlay.

But note, despite the algorithmic advantages, a correlation with common perception has been lost. Because the prefactor of each atomic Gaussian is not unity, the characteristic function does not correspond to the inside/outside description with which we are most comfortable. In the Gaussian model all points in space are to some degree inside and to some degree outside. That is, the Gaussian model typically shows about 0.1% error with respect to the solid sphere model due to the fact that is includes a portion of all points in space inside the volume.

### 1.1.3 Shape from Hermite Representation

So far, discussion has focused on a multi-center expansion of molecular shape based on a Gaussian representation of atoms. An interesting alternative is a single-center expansion of the shape into a complete set of functions. One possibility is to use a product of three Hermite functions, one per space dimension and expand the shape into the resulting complete set of functions. Expansion of an electron-density map into the three-dimensional basis of Hermite polynomials has been previously considered in Ref. [Derevyanko-2014].

Hermites are a class of functions known as "special" functions. They are special because linear combinations of these functions can reproduce any other reasonably behaved function. Just as the Discrete Fourier Transform shows that any periodic function can be represented by a sum of the trigonometric functions  $\{sin(n\varphi), cos(n\varphi)\}\$ , Hermite functions can be used to represent any localized, non-periodic function such as molecular shape. The "special" in special functions refers to the fact that each function in one of these classes is orthogonal to every other function. This means that the integral of the product of any two such functions is 1 if they are the same function, or zero if they are not. This makes much of the mathematics of finding the coefficients of the representational linear sum much simpler: a coefficient is then just the integral of the product of each particular special function with the function being represented.

There are many well-known special functions such as sine and cosine, Hermite polynomials, Legendre polynomials, and Laguerre polynomials. So why work with Hermite functions? The art of special functions is to choose one that fits the purpose. For instance, for a periodic function, sine and cosine make sense. Hermites make sense for shape because of their form. The **Hermite function** of order n (any non-negative integer) is defined as follows:

$$
\mathcal{H}_n(x) = H_n(x)e^{-x^2/2}
$$

The **Hermite polynomial** is defined as:

$$
H_n(x) = (-1)^n e^{x^2} \left(\frac{d}{dx}\right)^n e^{-x^2}.
$$

The first few Hermite polynomials are:

$$
H_0(x) = 1
$$
,  $H_1(x) = 2x$ ,  $H_2(x) = 4x^2 - 2$ ,  $H_3(x) = 8x^3 - 12x$ .

Hermite functions can be thought of as generalizations of Gaussian function to a complete set: this is why we like them as candidates for representing molecular shape! Since its formation, OpenEye has worked with molecular shape as a sum Gaussian ([Grant-1995], [Grant-1996], [Grant-1997]) and Hermites represent an extension of that work. The difference is that Hermites are all centered at the origin, while the "classical" OpenEye representation of molecular shape is to place a Gaussian at each non-hydrogen atom.

So, are there any advantages to using a single-centered Hermite representation rather than a multi-centered set of Gaussians? This is a similar question to the one we first posed at the beginning of OpenEye: Does representing shape by Gaussians give us any advantages over the canonical "sum of spheres" representation? We felt that it did. Shape became a smooth function that seemed more physical than sharp spherical functions, and they allowed a more efficient molecular overlay of shapes. We postulated that this might make a better dielectric function for Poisson-Boltzmann, which has been largely verified in ZAP TK ([Grant-2001]). The concept seemed very general, so we embedded it into an OpenEye toolkit, **Shape TK**, so that we and our customers could explore different uses. This led to applications in crystallography (AFITT), bioisostere replacement (BROOD), docking (FRED), pose prediction using ligand information (POSIT), and shape-based alignment (ROCS).

So what advantages might Hermites represent? For one, they are very compact (i.e., they have few coefficients). Second, the more coefficients we include (i.e., higher order functions), the more exact the match to a sum of atomcentered Gaussians; conversely, the fewer functions, the more "coarse" the representation becomes, while retaining the smooth properties we like about Gaussians in the first place. Third, the Fourier Transform of a Hermite function is the same function! If we imagine wanting to generate Fourier representations of shape, Hermites make it easy. Fourth, the overlap of two shapes represented by Hermite functions is just the sum of the product of the coefficients: it's that easy! It is not difficult to imagine ways in which we could apply Hermites to the same problems we currently tackle with atom-centered Gaussians.

The first application that has already intrigued us is the representation of protein shapes. Consider that an arbitrary molecular shape can be expanded into the following combination of Hermite functions:

$$
f(x, y, z) = \sum_{l,m,n}^{\infty} f_{lmn} \mathbf{H}_l(\lambda_x x) \mathbf{H}_m(\lambda_y y) \mathbf{H}_n(\lambda_z z).
$$

The (infinite) set of coefficients for  $f_{lmn}$  forms the Hermite representation. Due to reflection properties of Hermite polynomials, we can assume without loss of generality that the coefficients  $\lambda_x, \lambda_y, \lambda_z$  are all positive. In practice we take a finite sum in the above equation by truncating it with the following condition on l, m, n:

$$
l + m + n \le \text{NPolyMax},
$$

where NPolyMax is a resolution parameter, and can be varied from 0 (very inaccurate expansion) to infinity (exact Hermite expansion). The recommended value varies depending on the size of the molecule.

Below is an example of the Hermite representation of the protein DHFR.

![](_page_14_Figure_9.jpeg)

#### Fig. 1: Exact shape versus Hermite Representation

The left figure represents the VIDA view of the exact shape of the protein. The middle figure shows the Hermite representation with NPolyMax = 5. The right figure shows the Hermite representation with NPolyMax = 30. Remarkably, we can encode the main features of the protein shape using Hermite representation with only 56 floating point numbers (middle figure).

The advantages of representing proteins by Hermites include:

- smooth representations that capture any level of detail, from the atomistic (many coefficients, as in the picture on the right) to the very coarse (few coefficients, as in the middle picture),
- the ability to store these representations in a compact manner,
- the ability to transform these representations easily,
- very fast overlap calculations between proteins.

Of course, the mathematics of Hermites is more complex than that of a set of atom-centered Gaussians. We have to know how to make, rotate, translate, and scale such representations. Therefore, we are releasing this toolkit with no immediate application or goal - rather, in the spirit of OpenEye, to make potentially useful tools for our customers.

#### See also:

- OEHermite class
- OEHermiteOptions class
- OEHermiteShapeFunc class
- Shape from Hermite expansion examples

### **1.1.4 Color Features**

In addition to shape-alignments Shape TK, optionally, considers chemistry alignment, known as 'color'. Userspecified definitions of chemistry can be included in the superposition and similarity analysis process to facilitate the identification of those compounds that are similar both in shape and chemistry.

Color atoms are described as Gaussians and usually displayed as colored spheres in visualizations. The Gaussian for a color atom is relatively hard with a steep gradient. Figure: Hard vs. Soft Gaussians illustrates hard vs fuzzy Gaussians. Both Gaussians in the figure represent the same volume as the sphere. However, the hard Gaussian, with the steep gradient, reaches a probability of zero (0) within the radius of the sphere. The color features are either matched, if they fall within the sphere radius, or not matched. In the case of the fuzzy Gaussian there are areas outside the volume of the sphere (the area under the curve indicated by the two arrows) where the Gaussian probability is greater than zero. This would allow color features to match even when they align well outside the sphere representing the color atom. That situation would lead to less precise alignments and, for that reason, the 'hard' Gaussian is employed.

![](_page_15_Figure_14.jpeg)

#### Fig. 2: Hard vs. Soft Gaussians

A sphere described by two different Gaussian functions. The 'hard' Gaussian (dashed) is the one employed by Shape TK to approximate a color atom sphere.

Shape TK comes pre-loaded with two color force fields, Implicit Mills Dean (default) and Explicit Mills Dean. These are described in associated color force field files (\*.cff). The desired force field file can be supplied to the

 $OEColorForceField$ . Init method. Further information on editing color force field files is given in the below section Color File Format.

The color force field is used to measure chemical similarity between the query and the database molecule and to refine shape-based overlays. The color force field file describes:

- Color atom types
- The functional groups to which the color atoms should be applied. Shape TK uses only the heavy atoms of molecules; hydrogens are ignored.
- Whether the interaction between color atoms is attractive or repulsive. Interactions between color atoms of the same type are always attractive. The weight term describes the strength of the interaction relative to the shape gradients and the range term affects the range of the interaction.

The color features described in the Implicit and Explicit Mills Dean color force field files include:

**Donor** Functional groups that can act as H-bond donors e.g. acid-OH

Acceptor Functional groups that can act as H-bond acceptors e.g. carboxylate

**Anion** Functional groups with either localized or delocalized negative charge e.g. tetrazole

**Cation** Functional groups with either localized or delocalized positive charge e.g. guanidinium

Hydrophobe Terminal or non-terminal aromatic or aliphatic groups e.g. phenyl

Rings Rings of defined size e.g. 4-7 atoms

A custom force field file can include other features that you define e.g. positive, negative, carbonyl\_linker, metal\_binder. For each color atom type a set of SMARTS is used to define the specific functional groups to which the color atom will be applied. The Implicit and Explicit Mills Dean force fields differ in these functional group definitions. For example, the Explicit Mills Dean force field allows a primary amine to be an acceptor as well as a donor whereas it is a donor only in the Implicit Mills Dean force field.

The color force field can also be used for post-shape scoring either alone, e.g. ColorTanimoto and Color Tversky, or in combination with shape scores, e.g. TanimotoCombo and TverskyCombo.

#### **Color File Format**

As an alternative to the built-in force fields, the user can define a new color force field using the format described in this section. The following is a simplified example of a color force field specification.

```
DEFINE hetero [#7, #8, #15, #16]
DEFINE notNearHetero [ ! #1; ! $ ($hetero) ; ! $ ( \ * [ $hetero] ) ]
#\#TYPE donor
TYPE acceptor
TYPE rings
TYPE positive
TYPE negative
TYPE structural
##PATTERN donor [$hetero; H]
PATTERN acceptor [#8&4; (\xrightarrow{N}C[D1]), #7&40; [5([D4]); [6([D3]-\xleftarrow{r},1[Shetero])]PATTERN rings [R] \sim 1 \sim [R] \sim [R] \sim [R] 1PATTERN rings [R] \sim 1 \sim [R] \sim [R] \sim [R] \sim [R]1PATTERN rings [R] ~ 1 ~ [R] ~ [R] ~ [R] ~ [R] ~ [R] ~ [R] ~ [R]PATTERN rings [R] ~ 1 ~ [R] ~ [R] ~ [R] ~ [R] ~ [R] ~ [R] ~ [R]
```

```
PATTERN positive [+, \frac{\varsigma}{\varsigma}([N; ! \frac{\varsigma}{\varsigma}(\backslash *-\backslash *=0)])]PATTERN negative [-]
PATTERN negative [OD1+0]-[!#7D3]~[OD1+0]
PATTERN negative [OD1+0]-[!#7D4] (~[OD1+0])~[OD1+0]
PATTERN structural [$notNearHetero]
#INTERACTION donor donor attractive qaussian weight=1.0 radius=1.0
INTERACTION acceptor acceptor attractive qaussian weight=1.0 radius=1.0
INTERACTION rings rings attractive gaussian weight=1.0 radius=1.0
INTERACTION positive positive attractive gaussian weight=1.0 radius=1.0
INTERACTION negative negative attractive gaussian weight=1.0 radius=1.0
INTERACTION structural structural attractive gaussian weight=1.0 radius=1.0
```

There are four basic keywords in a cff file: DEFINE, TYPE, PATTERN, and INTERACTION. The TYPE field can be any user-defined term. TYPES can be any user-specified string such as "donor", "acceptor", "lipophilic anion" etc. The PATTERN keyword is used to associate SMARTS patterns with these types. There is no restriction on the number of patterns that can be associated with a user defined type. The position in Cartesian space of the PATTERN is taken as the average of the coordinates of the atoms that match the SMARTS pattern. If the desired location of the PATTERN is on a single atom of a larger SMARTS pattern recursive SMARTS (written as '[\$(SMARTS)]' can be used to this effect. Only the first atom in a recursive SMARTS pattern 'matches' the molecule, and the rest of the SMARTS pattern defines an environment. By writing a SMARTS pattern in recursive notation the location of the PATTERN will be taken as the atomic position of the first matching atom in the pattern. In order to simplify both reading and writing SMARTS, intermediate SMARTS can be associated with words using the DEFINE keyword. Once defined, these words can then be used as atom primitives in subsequent SMARTS patterns with the \$ prefix (see "DEFINE hetero" and "PATTERN donor" above).

Interactions between types are associated with the INTERACTION keyword. Two user-defined types must be listed, and whether their interaction is attractive or repulsive. The height and radius can be modified by keywords WEIGHT and RADIUS. At present, the only alternative to a Gaussian decay is invoked by the DISCRETE keyword. A discrete interaction contributes all of WEIGHT if the inter-type distance is less than RADIUS, or zero. Since it is not differentiable it makes no contribution to optimization (i.e. because the gradient of a DISCRETE function is 0 or infinite).

### **Built-in Color Force Fields**

Two color force fields, ImplicitMillsDean and ExplicitMillsDean, are built into the Shape toolkit. Both of these force fields define similar 6 TYPE color force-fields. The types are hydrogen-bond donors, hydrogen-bond acceptors, hydrophobes, anions, cations, and rings. The ImplicitMillsDean force field is recommended.

ImplicitMillsDean includes a simple pKa model that assumes pH=7. It defines cations, anions, donors and acceptors in such a way that they will be assigned the appropriate value independent of the protonation state in the reference or fit molecule. For example, if a molecule contains a carboxylate, ImplicitMillsDean will consider it an anionic center independent of whether it is protonated or deprotonated. This is convenient for searching databases which have not had careful curation of their protonation states. The ExplicitMillsDean file has a similar overall interaction model, however, it does not include a pKa model. It interprets the protonation and charge state of each molecule exactly. Thus, if a sulfate is protonated and neutral, it will not be considered an anion.

The hydrogen-bond models in both ImplicitMillsDean and ExplicitMillsDean are extensions of the original model presented by Mills and Dean [Mills-Dean-1996]. They both have donors and acceptors segregated into strong, moderate and weak categories.

# **1.1.5 Similarity Measures**

Measuring molecular similarity or dissimilarity has two basic components: the representation of molecular characteristics (such as shape and color) and the similarity coefficient that is used to quantify the degree of resemblance between two such representations. Different similarity coefficients quantify different types of structural resemblance.

The table below defines the basic terms that are used in shape based similarity calculations:

| Symbol         | Description                                      |
|----------------|--------------------------------------------------|
| $self_A$       | Self overlap or self color score for molecule A  |
| $self_B$       | Self overlap or self color score for molecule B  |
| $overlap_{AB}$ | Overlap or color score between molecules A and B |

#### Table 1: Basic components of similarity calculation

### **Tanimoto**

### Formula:

 $Tanimoto_{A,B} = \frac{overlapAB}{selfA + selfB - overlapAB}$ 

The Tanimoto similarity measure is symmetric, and always has a value between 0.0 and 1.0 for both shape and color.

### **Tversky**

### Formula:

 $Tversky_{A,B} = \frac{overlapAB}{\alpha \ast selfA + \beta \ast selfB}$ 

The Tversky similarity measure is asymmetric. Setting the parameters  $\alpha = \beta = 0.5$  makes it symmetric and somewhat identical to using the *Tanimoto* measure.

The factor  $\alpha$  weights the contribution of the first *reference* molecule. The larger  $\alpha$  becomes, the more weight is put on the self overlap of the reference molecule.

Like the Tanimoto similarity, the Tversky similarity always has a value between 0.0 and 1.0 for shape. However, that may not be always true for color. Depending on the number and types of color atoms between molecules A and B, it is possible to have  $|overlapAB| > |selfA|$ , and that along with certain value of  $\alpha$  can sometimes lead to  $Tversky_{A,B} > 1.0.$ 

**Note:** Default settings for RefTversky uses  $\alpha = 0.95$  and  $\beta = 0.05$ , and the default settings for FitTversky uses  $\alpha = 0.05$  and  $\beta = 0.95$ .

# 1.1.6 Implementation Details and Usage

### **Overlap Functions**

The overlap functions extend the molecule objective function (OEMolFunc1) interfaces, define in **OEFF TK**, with overlap interactions, through OEOverlapFuncBase. Similar to the force fields, a shape or a color is also defined as a collection of pairwise interactions. Implementation of overlaps as extension of the molecule objective functions allows for use of the standard optimizers (OEOptimizer1 and/or OEOptimizer2) for minimization of overlaps and corresponding quantities. Implementation of overlaps as extension of the molecule objective functions also allows for combining the overlap functions with other molecule objective functions, such as the force fields, for system optimization. An overlap function in **Shape TK** can consist of just shape or color, or a combination of both.

The overlap functions are the simplest objects in **Shape TK**, and can is used to calculate simple, static, overlap between two objects (molecules, grids or shape queries). Note that static means that the two input species (ref and fit) are not moved at all. These objects simply calculate the static overlap, gradients and other corresponding quantities, given the input positions.

### **Overlap Methods**

Three different algorithms are implemented to calculate the overlap and the corresponding gradients, between two gaussians, that provides a balance between accuracy and speed.

The *Exact* option considers all pairs of atoms in the system, and the Gaussian overlaps are calculated exactly.

The *Analytic* option provides multiple options to approximate the calculations. The first option corresponds to using a pre-calculated table for estimating the exponentials vs. doing exact calculation of the exponentials. The second option allows to use a proximity grid to only consider those atom pairs that are within a certain threshold distance (by default 3.0 Å). The average error introduced by either of these approximations is in the order of one part in a thousand. The speed gain from the proximity grid increases with size of the molecules, as well as with the number of overlap calculations performed. The later is related to the increased setup time for the proximity grid for the reference molecule. If both the tabulated exponentials and the proximity grid is turned off, the Analytic option simply folds back to the *Exact* option.

The final option, *Grid*, uses a grid representation of the volume of the target molecule. It requires significant set-up time relative to the cost of a single overlap calculation  $\sim 0.01$ s compared to  $\sim 0.0001$ s) but is significantly faster than other methods for the evaluation of each overlap once set. Grid suffers a few caveats and drawbacks. First is that, currently, for shape overlap calculation, all atoms are treated as if they have the same radius (that assigned to carbon). The second is that the approximation is slightly worse, typically a few parts in a thousand, at typical grid resolutions.

Both Analytic and Grid improve performance when the fit molecule is large (>20 atoms) because, if there are **n** atoms in the fit and  $\mathbf m$  in the reference, the work per atom in the fit is proportional to a constant not  $\mathbf n$ .

Besides the Gaussian based calculations, a fourth option, *Hermite* is available for shape overlap calculation, based on Hermite representation of shape as described above earlier.

### **Radii approximations**

Since we are considering molecular volume overlap as a measure of shape, the radii used for each atom is important. There are essentially two settings. A radii approximation of  $OEOverlapRadi$  All means each atom will be treated with the radius as passed in. Alternatively, one can treat all heavy atoms as similar and apply the OEOverlapRadii\_Carbon radius approximation. With this, all heavy atoms will be assigned the same radius, regardless of the value attached to each atom. As noted above, if the Grid method is used for overlap calculation, only the OEOverlapRadii\_Carbon radius approximation can be used.

### **Overlap Optimization and Overlay**

Two high level objects, OEROCS and OEOverlay are provided for optimizing a OEOverlapFuncBase, to maximize shape (and color) overlap between two objects and obtain the best overlay. Both the OEROCS and OEOverlay optimizes the overlap between the reference and fit object, but provides different level of usability.

### **Starting positions for optimization**

The starting points are important for any optimization. Various options to start an overlap optimization is provided through the OEStarts interface. The reference structure is always aligned by its principal moments of inertia, and the initial alignments of fit structure is determined by the specified options.

In the *Inertial* start, in general, the fit object is aligned in 4 positions with the primary and secondary moments of inertia in both directions. In order to deal with structures with symmetrical moments of inertia, additional starting points are generated. For a reference or fit where the 2 major moments of inertia are equal (to a user-defined percent, nominally 15%), 4 extra starting positions are generated. In the rare case of a molecule with all 3 moments of inertia essentially equal, 20 random starting translations and rotations are chosen as starting positions. For virtual screening uses, where the reference and fit molecule are similar in size, the inertial starts provide an excellent choice for starting positions that balances quality results with speed.

There are times when there is a large difference in size and a more elaborate search is needed. For these, there are a couple of built-in searches as well a user-defined search. To increase searching, instead of doing the inertial frame rotations with to 2 molecule centers-of-mass (COM) aligned, we can do a set of inertial rotations at many more locations.

The AtAtom starts will translate the COM of the fit molecule to the specified atom center (usually the heavy atoms) locations of the reference molecule. At each of these translations, it will perform the 4 basic inertial transforms. Note that this means that instead of  $4$  (or 8) starting positions, there will be  $4x$  number of reference molecule heavy atoms (or what other atom centers specified) starts, resulting in 20-30 more starting positions compared to the *Inertial* starts. Obviously this will slow the overall calculation so this is not recommended for high-volume virtual screening, but is very useful for low-volume fragment searching. A slightly less aggressive set of starting positions can be to use the color atom centers instead of the heavy atoms of the reference molecule. For an average reference molecule with  $\sim$ 10 color atoms, this will be faster than using all heavy atom positions, but not as elaborate of a search.

The Subrocs starts automatically performs AtAtom starts on each heavy atom of the larger molecule, regardless of which molecule is set as the reference.

With the Cartesian starts, the user can specify the points at which to translate the fit molecule before doing the 4 basic inertial transforms. This provides more flexibility in terms of how to starts to do for any optimization.

The Random starts, will generate N random starting positions where N is user-defined, as well as the maximum translation allowed between random starts. The fit molecule will be translated to these random starting positions, and the basic inertial transforms will be applied.

The AsIs starts gives the option to the user to start the optimization from a single, pre-aligned position.

And finally, the *Quat* starts takes the user specified quaternions as the transformations to be applied to the fit molecule before performing optimizations.

Thus, for any given optimization, there are multiple results returned, usually only one of which is useful.

### **Preparing Molecules**

Tools for preparing molecules are provided separately so users can prepare their molecules once and reuse those molecules for many calculations. However, the high level OEROCS object for overlay optimization also provides a convenient option to automatically prepare molecules, if desired.

There are essentially three components to preparing molecules.

The first is to choose either to have hydrogens explicitly or not, and add or remove the hydrogens in the molecules. Shape is a heavy atom property and most OpenEye uses (as well as the default option in OEOverlapPrep) is to ignore the hydrogens.

The second is to assign Bondi radii on the atoms, if desired. This is required if a radii approximation of OEOverlapRadii\_All is to be used for shape overlap calculations.

The third is to choose to have color atoms or not. Even if color is used for the calculations, it is possible to have user defined color atoms on the molecules and direct OEOverlapPrep to not make modifications to them (see OEOverlapPrep.SetAssignColor).

### **CHAPTER**

**TWO** 

# **EXAMPLES**

# **2.1 Calculating Overlap**

Overlap calculation is the simplest functionality offered through the **Shape TK**. These examples show how to calculate static overlap between two objects (molecules, grids or shape query). Note that static means that the two input species (ref and fit) are not moved at all. These examples simply calculate the overlap and/or other related quantities, given the input positions. Examples for performing calculations that actually optimize the alignment/overlap are considered in a separate section.

# 2.1.1 Simple Overlap

This example reads in a reference molecule and a few fit molecules and prints out the *Exact* overlap calculated.

### **Listing 1: Simple overlap using Exact Overlap**

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
from openeye import oeshape
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <reffile> <fitfile>" % argv[0])
```

```
reffs = occhem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])refmol = occhem. OEGraphMol()oechem.OEReadMolecule(reffs, refmol)
    # Prepare reference molecule for calculation
    # With default options this will remove any explicit hydrogens present
   prep = oeshape.OEOverlapPrep()
   prep.Prep(refmol)
    # Get appropriate function to calculate exact shape
    shapeFunc = oeshape.OEExactShapeFunc()shapeFunc.SetupRef(refmol)
    res = oeshape.OEOverlapResults()
    for fitmol in fitfs.GetOEGraphMols():
        prep.Prep(fitmol)
        shapeFunc.Overlap(fitmol, res)
        print ("title: ss exact tanimoto = s.2f" s(fitmol.GetTitle(),\ res.GetTanimoto());if _name_ = = "_main_".import sys
    sys.exit(main(sys.argv))
```

## 2.1.2 Adding overlap to molecules

This next example program uses the *Analytic* overlap method and also uses a little extra OEChem to attach the overlap scores to each molecule as SD data. This can be used to rescore a set of ROCS hits or to measure the overlap of ROCS alignments against an exclusion region in the binding site.

### **Listing 2: Rescoring pre-aligned structures**

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

```
(continued from previous page)
```

```
from openeye import oechem
from openeye import oeshape
def main(argv=[_name_]):
   if len(argv) != 4:
       oechem.OEThrow.Usage("%s <reffile> <rocs_hits_file> <output.sdf>" % argv[0])
   reffs = occhem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])outfs = oechem.oemolostream(argv[3])
   refmol = oechem. OEGraphMol()oechem.OEReadMolecule(reffs, refmol)
    # Get appropriate function to calculate analytic shape
    shapeFunc = oeshape.OEAnalyticShapeFunc()
    shapeFunc.SetupRef(refmol)
   res = oeshape.OEOverlapResults()
    for fitmol in fitfs. GetOEGraphMols():
        shapeFunc.Overlap(fitmol, res)
        oechem.OESetSDData(fitmol, "AnalyticTanimoto", "%.2f" % res.GetTanimoto())
        oechem.OEWriteMolecule(outfs, fitmol)
if name == " main ":
    import sys
    sys.exit(main(sys.argv))
```

# 2.1.3 Color Overlap

This example reads in a reference molecule and a few fit molecules and prints out the *Exact* color score calculated. By default all color calculations are performed using the ImplicitMillsDean force field.

### **Listing 3: Calculating color score**

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
```

```
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
from openeye import oechem
from openeye import oeshape
def main(argv=[_name_]):
   if len(argv) != 3:
        oechem.OEThrow.Usage("%s <reffile> <fitfile>" % argv[0])
   reffs = oechem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])refmol = oechem.OEGraphMol()
   oechem.OEReadMolecule(reffs, refmol)
    # Prepare reference molecule for calculation
    # With default options this will remove any explicit
    # hydrogens present, and add required color atoms
   prep = oeshape. 0E0verlapPrep()prep.Prep(refmol)
    # Get appropriate function to calculate exact color
   colorFunc = oeshape.OEExactColorFunc()colorFunc.SetupRef(refmol)
   res = oeshape.OEOverlapResults()
   fitmol = occhem.OEGraphMol()while oechem. OEReadMolecule (fitfs, fitmol) :
       prep.Prep(fitmol)
       colorFunc.Overlap(fitmol, res)
       print ("title: ss color score = s.2f" s(fitmol.GetTitle(), res.GetColorScore()))
if _name == " main ":
   import sys
    sys.exit(main(sys.argv))
```

# 2.1.4 Adding color score to molecules

This next example uses the ImplicitMillsDean force field and the *Analytic* color to rescore a set of ROCS hits and add the color scores to SD tags.

Listing 4: Using color to add scores to pre-aligned molecules.

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
from openeye import oeshape
def main(argv=[__name__]):
   if len(argv) != 4:
        oechem.OEThrow.Usage("%s <reffile> <rocs_hits_file> <output.sdf>" % argv[0])
   reffs = oechem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])outfs = occhem.oemolostream(argv[3])refmol = oechem.OEGraphMol()
   oechem.OEReadMolecule(reffs, refmol)
    # Prepare reference molecule for calculation
    # With default options this will add required color atoms
   prep = oeshape.OEOverlapPrep()
   prep.Prep(refmol)
    # Get appropriate function to calculate analytic color
   colorFunc = oeshape.OEAnalyticColorFunc()
   colorFunc.SetupRef(refmol)
   res = oeshape.OEOverlapResults()
    for fitmol in fitfs.GetOEGraphMols():
       prep.Prep(fitmol)
        colorFunc.Overlap(fitmol, res)
        oechem.OESetSDData(fitmol, "AnalyticColorTanimoto", "%.2f" % res.
\rightarrowGetColorTanimoto())
        oeshape.OERemoveColorAtoms(fitmol)
        oechem.OEWriteMolecule(outfs, fitmol)
        print ("Fit Title: %s Color Tanimoto: %.2f" %
              (fitmol.GetTitle(), res.GetColorTanimoto()))
```

```
if
   name = "main":
   import sys
   sys.exit(main(sys.argv))
```

# 2.1.5 User Defined Color

As a step toward writing a complete color force field, it is possible to combine built-in rules for color atom assignment with user defined interactions. A new OEColorForceField object can be created using one of the built-in types, then the interactions can be cleared using OEColorForceField. ClearInteractions and subsequent user interactions added with OEColorForceField, AddInteraction.

For example, to use the ImplicitMillsDean atom typing rules, but to only consider donor-donor and acceptor-acceptor interactions, one can use the following:

#### Listing 5: Using ImplicitMillsDean with user interactions.

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
from openeye import oeshape
def main(argv=[_name_]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <reffile> <overlayfile>" % argv[0])
   reffs = oechem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])refmol = occhem. OEGraphMol()oechem.OEReadMolecule(reffs, refmol)
    # Modify ImplicitMillsDean color force field by
    # adding user defined color interactions
    cff = oeshape. OEColorForceField()
    if not cff. Init (oeshape. OEColorFFType_ImplicitMillsDean) :
```

```
oechem. OEThrow. Error ("Unable to inititialize color forcefield")
    cff.ClearInteractions()
   donorType = cff.GetType("donor")
    accept{\gamma} = cff.GetType("acceptor")cff.AddInteraction(donorType, donorType, "gaussian", -1.0, 1.0)
    cff.AddInteraction(accepType, accepType, "gaussian", -1.0, 1.0)
    # Prepare reference molecule for calculation
    # With default options this will add required color atoms
    # Set the modified color force field for addignment
    prep = oeshape.OEOverlapPrep()
    if not prep. SetColorForceField(cff):
        oechem. OEThrow. Error ("Unable to set color forcefield")
   prep.Prep(refmol)
    # Get appropriate function to calculate exact color
    # Set appropriate options to use the user defined color
    options = oeshape.OEColorOptions()
    if not options. SetColorForceField(cff):
        oechem. OEThrow. Error ("Unable to set color forcefield")
    colorFunc = oeshape.OEExactColorFunc(options)
    colorFunc.SetupRef(refmol)
   res = oeshape.OEOverlapResults()
    for fitmol in fitfs. GetOEGraphMols():
        prep.Prep(fitmol)
        colorFunc.Overlap(fitmol, res)
        print ("Fit Title: %s Color Tanimoto: %.2f" %
              (fitmol.GetTitle(), res.GetColorTanimoto()))
   name = "main":
if,
    import sys
    sys.exit(main(sys.argv))
```

### 2.1.6 Shape and Color Overlap

This example reads in a reference molecule and a few fit molecules and prints out both the shape overlap and the color score calculated. By default the OEOverlapFunc uses the Grid shape and Exact color.

#### Listing 6: Calculating both shape and color overlap

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
from openeye import oechem
from openeye import oeshape
def main(argv=[_name_]):
   if len(argv) != 3:
       oechem.OEThrow.Usage("%s <reffile> <fitfile>" % argv[0])
   reffs = occhem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])refmol = occhem.OEGraphMol()oechem.OEReadMolecule(reffs, refmol)
    # Prepare reference molecule for calculation
    # With default options this will remove any explicit
    # hydrogens present and add color atoms
   prep = oeshape.OEOverlapPrep()
   prep.Prep(refmol)
    # Get appropriate function to calculate both shape and color
    # By default the OEOverlapFunc contains OEGridShapeFunc for shape
    # and OEExactColorFunc for color
    func = oeshape.OEOverlapFunc()
   func.SetupRef(refmol)
   res = oeshape.OEOverlapResults()
   for fitmol in fitfs. GetOEGraphMols():
       prep.Prep(fitmol)
       func.Overlap(fitmol, res)
       print ("title: ss tanimoto combo = s.2f shape tanimoto = s.2f color tanimoto
\leftrightarrow = 8.2f'' 8
              (fitmol.GetTitle(), res.GetTanimotoCombo(),
              res.GetTanimoto(), res.GetColorTanimoto()))
if __name__ == "_main_":
    import sys
   sys.exit(main(sys.argv))
```

# 2.2 ROCS

The high-level OEROCS provides the simplest way to maximize shape and/or color between two objects. OEROCS uses the same shape and color functions as used for static overlap calculation, but optimizes the overlap between the reference and the fit objects. By default both shape and color optimization is performed, with shape estimated with the *Grid* method and color estimated with the *Exact* method.

The fit object is not moved during the optimization. Part of the results returned from the calculation are the transform required to move the fit object into the final orientation. The results also contain a copy of the fit molecule conformer(s) in its final orientation.

A helper function OEROCSO verlay is created for the most simple usage of the functionality that performs optimizations between a set of conformers and returns the best hit.

## 2.2.1 Best Hit

This example reads in a reference molecule and a fit molecule, performs overlay optimization, finds the best hit conformer and prints it out in final orientation.

#### Listing 7: Finding best hit conformer pair

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
from openeye import oeshape
def main(argv=[_name_]):
    if len(argv) != 4:
        oechem. OEThrow. Usage ("%s <reffile> <fitfile> <outfile>" % argv[0])
    reffs = occhem.oemolistream(sys.argv[1])fits = occhem.oemolistream(sys.argv[2])outfs = oechem.oemolostream(sys.argv[3])
    refmol = occhem. OEMol()oechem.OEReadMolecule(reffs, refmol)
```

```
fitmol = occhem. OEMol()
    oechem.OEReadMolecule(fitfs, fitmol)
    res = oeshape.OEROCSResult()
    oeshape.OEROCSOverlay(res, refmol, fitmol)
    outmol = res.GetOverlayConf()
    oechem.OEWriteMolecule(outfs, outmol)
    print ("Tanimoto combo = \frac{2}{3}. 2f" \frac{1}{3} res. GetTanimotoCombo())
if name == " main ":
    import sys
    sys.exit(main(sys.argy))
```

## 2.2.2 Top Hits

This example reads in a reference molecule and a few fit molecules, performs overlay optimization, finds the few top hits, and prints them out in final orientation.

#### **Listing 8: Finding top ROCS hits**

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
from openeye import oeshape
def main(argv=[_name_]):
   if len(argv) != 5:
        oechem.OEThrow.Usage("%s <reffile> <fitfile> <outfile> <<hhits>" % argv[0])
   reffs = occhem.oemolistream(sys.argv[1])fits = occhem.oemolistream(sys.argv[2])outfs = occhem.oemolostream(sys.argv[3])
```

```
nhits = int(sys.argv[4])refmol = occhem. <math>OEMol()</math>oechem.OEReadMolecule(reffs, refmol)
    # Setup OEROCS with specified number of best hits
    options = oeshape.OEROCSOptions()
    options. SetNumBestHits (nhits)
    rocs = oeshape. OEROCS (options)
    rocs.SetDatabase(fitfs)
    for res in rocs. Overlay (refmol) :
        outmol = res.GetOverlayConf()
        oechem.OEWriteMolecule(outfs, outmol)
        print ("title: ss tanimoto combo = s.2f'' % (outmol. GetTitle(), res.
\rightarrowGetTanimotoCombo()))
if name == "_main_":
    import sys
    sys.exit(main(sys.argv))
```

### 2.2.3 Top Hits with Multiple Conformers

This example repeats the Top Hits example above but fixes the number of hits to 3 and asks for multiple best conformers for each hit reported.

#### Listing 9: Finding top ROCS hits with multiple conformers

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
from openeye import oeshape
def main(argv=[__name__]):
   if len(argv) != 5:
```

```
oechem.OEThrow.Usage("%s <reffile> <fitfile> <outfile> <confsperhit>" %.
\rightarrowargv[0])
    reffs = oechem.oemolistream(sys.argv[1])fits = occhem.oemolistream(sys.argv[2])outfs = oechem.oemolostream(sys.argv[3])
   nconfs = int(sys.argv[4])refmol = occhem. OEMol()
   oechem.OEReadMolecule(reffs, refmol)
    # Setup OEROCS to provide 3 best hits
    # with the specified number of conformers per hit
   options = oeshape.OEROCSOptions()
   options.SetNumBestHits(3)
   options. SetConfsPerHit (nconfs)
    rocs = oeshape.OEROCS(options)
    rocs.SetDatabase(fitfs)
    for res in rocs. Overlay (refmol) :
        outmol = res.GetOverlayConfs()
        oechem.OEWriteMolecule(outfs, outmol)
        print ("title: ss tanimoto combo = s.2f" s (outmol. GetTitle(), res.
\rightarrowGetTanimotoCombo()))
if name == " main ":
    import sys
    sys.exit(main(sys.argv))
```

# **2.3 Overlay Optimization**

The methods OEOverlay and OEMultiRefOverlay, compared to OEROCS, allow setting up a reference system and process overlay optimization of multiple fit molecules. Another difference is that both OEOverlay and OEMultiRefOverlay, in addition to providing the best overlay score, also give access to all the results obtained during an overlay optimization. Methods OEOverlay and OEMultiRefOverlay, which provide all results, should be used only when such a rigorous amount of resulting data is desired.

# 2.3.1 Best Optimization Result

This example reads in a reference molecule and a few fit molecules, performs overlay optimization, and returns only the best result per reference to fit molecule overlay optimization.

Listing 10: Getting the best scores from OEMultiRefOverlay.

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
def main(argv=[__name__]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <reffile> <fitfile>" % argv[0])
    reffs = oechem. oemolistream(argv[1])fits = occhem.oemolistream(argv[2])refmol = occhem. OEMol()oechem.OEReadMolecule(reffs, refmol)
    print ("Ref. Title:", refmol. GetTitle(), "Num Confs:", refmol. NumConfs())
    # Prepare reference molecule for calculation
    # With default options this will remove any explicit
    # hydrogens present and add color atoms
    prep = oeshape. 0E0verlapPrep()prep.Prep(refmol)
    overlay = oeshape. 0EMultiRefOverlay()overlay. SetupRef (refmol)
    for fitmol in fitfs. GetOEMols():
        prep.Prep(fitmol)
        score = oeshape.OEBestOverlayScore()
        overlay. BestOverlay (score, fitmol, oeshape. OEHighestTanimoto())
        print ("Fit Title: \frac{1}{6} - 4s FitConfIdx: \frac{1}{6} - 4d RefConfIdx: \frac{2}{6} - 4d tanimoto combo: \frac{2}{6}. 2f"
```

```
% (fitmol.GetTitle(), score.GetFitConfIdx(),
                score.GetRefConfIdx(), score.GetTanimotoCombo()))
if name == "_main_":
   sys.exit(main(sys.argv))
```

#### Listing 10b: Getting the best scores from OEMultiRefOverlay (multi-threaded version)

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
# This is a multi-threaded version of the example that reads in a
# reference molecule and a few fit molecules, performs overlay optimization,
# and shows the single best result.
# With the default options, OEOverlay optimizes both shape and color.
import sys
from openeye import oechem
from openeye import oeshape
from threading import Thread
class MultiCoreOverlay (Thread) :
   def _init_(self, refmol, ifs):
        Thread.__init__(self)
        self._prep = oeshape.OEOverlapPrep()
        self._prep.Prep(refmol)
        self._overlay = oeshape.OEMultiRefOverlay()
        self._overlay.SetupRef(refmol)
        self._ifs = ifsdef run (self) :
        for fitmol in self._ifs.GetOEMols():
            self._prep.Prep(fitmol)
            score = oeshape.OEBestOverlayScore()
            self._overlay.BestOverlay(score, fitmol, oeshape.OEHighestTanimoto())
            print ("Fit Title: \frac{2}{5} - 4s FitConfIdx: \frac{2}{5} - 4d RefConfIdx: \frac{2}{5} - 4d tanimoto combo:
\rightarrow \frac{6}{9}. 2f''% (fitmol.GetTitle(), score.GetFitConfIdx(),
```

```
score.GetRefConfIdx(), score.GetTanimotoCombo()))
def main(argv=[__name__]):
   if len(argv) != 3:
        oechem.OEThrow.Usage("%s <reffile> <fitfile>" % argv[0])
   reffs = oechem.oemolistream(argv[1])refmol = oechem. <math>OEMol()</math>oechem.OEReadMolecule(reffs, refmol)
   print ("Ref. Title:", refmol. GetTitle(), "Num Confs:", refmol. NumConfs())
   fits = occhem.oemolithread(sys.argv[2])thrds = []
    for i in range (oechem. OEGetNumProcessors()):
        thrd = MultiCoreOverlay(refmol, fitfs)
        thrd.start()
        thrds.append(thrd)
    for thrd in thrds:
        thrd.join()return 0
if name == " main ":
    sys.exit(main(sys.argy))
```

## **2.3.2 All Optimization Results**

This example repeats the above, but uses  $\sqrt{O(\text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot \text{Var} \cdot$ 

A single Overlay calculation will return N results, where N is the number of ref conformers times the number of fit conformers times the number of starting positions for each pair. So comparing 2 molecules with 10 conformers each could return 400 or more results.

There are two helper classes designed solely to contain these results and to make it easy to extract all or just the desired subset. OEBestOverlayResults holds the results of a single pair of conformers. It contains a set of OEBestOverlayScore objects, one for each starting position.

This example uses 2 iterators to show all the results.

#### Listing 11: Getting all the scores from OEMultiRefOverlay.

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
```

# exclusive risk. Sample Code may require Customer to have a then # current license or subscription to the applicable Cadence offering.

(continued from previous page)

```
# THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT
# NOT LIMITED TO, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
# PARTICULAR PURPOSE AND NONINFRINGEMENT. In no event shall Cadence be
# liable for any damages or liability in connection with the Sample Code
# or its use.
# This example reads in a reference molecule and a few fit
# molecules, performs overlay optimization, and uses 2 iterators to
# show all the results.
# With the default options, OEOverlay optimizes both shape and color.
from openeye import oechem
from openeye import oeshape
def main(argv=[_name_]):
    if len(argv) != 3:
        oechem.OEThrow.Usage("%s <reffile> <fitfile>" % argv[0])
    reffs = occhem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])refmol = occhem. OEMol()
   oechem.OEReadMolecule(reffs, refmol)
   print ("Ref. Title:", refmol. GetTitle(), "Num Confs:", refmol. NumConfs())
    # Prepare reference molecule for calculation
    # With default options this will remove any explicit
    # hydrogens present and add color atoms
    prep = oeshape. 0E0verlapPrep()prep.Prep(refmol)
   overlay = oeshape.OEMultiRefOverlay()
   overlay. SetupRef (refmol)
    for fitmol in fitfs. GetOEMols():
        print ("Fit Title:", fitmol. GetTitle(), "Num Confs:", fitmol. NumConfs())
        prep.Prep(fitmol)
        resCount = 0# double loop over results and scores to obtain all scores
        for res in overlay. Overlay (fitmol):
            for score in res. GetScores():
                print ("FitConfIdx: 8-4d RefConfIdx: 8-4d tanimoto combo: 8.2f''% (score.GetFitConfIdx(), score.GetRefConfIdx(), score.
\rightarrowGetTanimotoCombo()))
                resCount += 1print (resCount, "results returned")
if _name_ = = "_main_".
```

import sys sys.exit(main(sys.argv))

# 2.3.3 Manipulating all results

This example repeats the above to access all overlay results, and shows how to navigate through the results to extract a specific set. Here, the OESortOverlayScores function is used to turn the double iterator as shown in the example above into a single iterator of OEBestOverlayScore. Note that the third argument is a functor used to sort the list, such that in this next example, we get one OEBestOverlayScore for each pair of conformers, and they are returned in Tanimoto order.

OEOverlay or OEMultiRefOverlay does not actually move the fit molecule. Part of OEBestOverlayScore is the rotation matrix and translation matrix necessary to move the fit molecule into the final overlap position. (Note well: the rotation matrix is left-multiplied so can be regarded as left-handed.) This example also shows how to apply these transformations. The OpenEye standard is rotation then translation, but as a convenience, OEBestOverlayScore has OEBestOverlayScore. Transform method that will apply the transforms in the proper order.

This example keeps the user specified number of scores, aligns each fit conformer to the ref conformer it was overlaid on, and then write the pair to an output file. If SD or OEB is used as the output file type, then scores will also be stored in SD tags.

#### Listing 12: Writing few aligned structures from OEMultiRefOverlay.

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
# in tanimoto order, shows the user specified number of
# results, and saves the overlayed structures.
# With the default options, OEOverlay optimizes both shape and color.
from openeye import oechem
from openeye import oeshape
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
```

```
if len(argv) != 5:
        oechem. OEThrow. Usage("%s <reffile> <fitfile> <out.sdf> <keepsize>" % argv[0])
   reffs = occhem.oemolistream(argv[1])fits = occhem.oemolistream(argv[2])outfs = occhem.oemolostream(argv[3])keepsize = int(argv[4])
   refmol = occhem. OEMol()
   oechem.OEReadMolecule(reffs, refmol)
   print ("Ref. Title:", refmol. GetTitle(), "Num Confs:", refmol. NumConfs())
   # Prepare reference molecule for calculation
    # With default options this will remove any explicit
    # hydrogens present and add color atoms
   prep = oeshape.OEOverlapPrep()
   prep.Prep(refmol)
   overlay = oeshape.OEMultiRefOverlay()
   overlay. SetupRef (refmol)
   for fitmol in fitfs. GetOEMols():
       print ("Fit Title:", fitmol.GetTitle(), "Num Confs:", fitmol.NumConfs())
       prep.Prep(fitmol)
       resCount = 0# Sort all scores according to highest tanimoto
        scoreiter = oeshape.OEBestOverlayScoreIter()
        oeshape.OESortOverlayScores(scoreiter, overlay.Overlay(fitmol), oeshape.
\rightarrowOEHighestTanimoto())
        for score in scoreiter:
            outmol = oechem.OEGraphMol(fitmol.GetConf(oechem.OEHasConfIdx(score.
\rightarrowGetFitConfIdx())))
           score.Transform(outmol)
            oechem. OESetSDData (outmol, "RefConfIdx", "%-d" % score. GetRefConfIdx())
           oechem. OESetSDData (outmol, "tanimoto combo", "%-. 3f" % score.
\rightarrowGetTanimotoCombo())
            oeshape.OERemoveColorAtoms(refmol)
            oechem.OEWriteMolecule(outfs,
                                    refmol.GetConf(oechem.OEHasConfIdx(score.
\rightarrowGetRefConfIdx())))
            oeshape.OERemoveColorAtoms(outmol)
            oechem.OEWriteMolecule(outfs, outmol)
            resCount += 1# Break at the user specified size
            if resCount == keepsize:
                break
        print (resCount, "results returned")
```

```
if
   name
           == " main ":
   import sys
   sys.exit(main(sys.argv))
```

# 2.4 Working with Shape Query

This section of examples shows the use of a *OEShapeQuery*, and performs calculations where a shape query is used as the reference system instead of a molecule as the reference.

### 2.4.1 Creating a shape query

This examples shows how to create a simple shape query that combines a molecule with gaussians. In this example, the molecule is added in the query to define shape, and color is added separately in terms to gaussians. The created query is then saved in a file.

#### Listing 13: Creating a shape query.

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
from openeye import oechem, oeshape
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    opts = oechem.OESimpleAppOptions("CreateQuery", oechem.OEFileStringType_Mol3D, "sq
\leftrightarrow<sup>11</sup>)
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    ifs = oechem.oemolistream()
    if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    ofs = occhem.oeofstream()if not ofs.open(opts.GetOutFile()):
```

```
oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    cff = oeshape.OEColorForceField()
    cff.Init(oeshape.OEColorFFType_ImplicitMillsDean)
    mol = occhem. OEGraphMol()while oechem. OEReadMolecule(ifs, mol):
        query = oeshape. 0EShapeQueueif oeshape. OEMol2Query (query, mol, cff) :
            oeshape.OEWriteShapeQuery(ofs, query)
        else:oechem. OEThrow. Warning ("Failed to create query from: %s" % mol. GetTitle())
    return <sub>0</sub>if _name_ = = "_main_".import sys
    sys.exit(main(sys.argv))
```

# 2.4.2 Overlap with shape query

This example reads in a reference shape query and a few fit molecules and prints out both the shape overlap and the color score calculated. By default the OEOverlapFunc uses the Grid shape and Exact color.

#### Listing 14: Overlap with a shape query

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
from openeye import oeshape
def main(argv=[_name_]):
   if len(argv) != 3:
        oechem.OEThrow.Usage("%s <queryfile> <fitfile>" % argv[0])
```

```
if oechem. OEGetFileExtension(sys.argv[1]) != "sq":
        oechem. OEThrow. Fatal ("Requires a shape query . sq input file format")
    query = oeshape.OEShapeQueuecy()oeshape.OEReadShapeQuery(argv[1], query)
    # Get appropriate function to calculate both shape and color
    # By default the OEOverlapFunc contains OEGridShapeFunc for shape
    # and OEExactColorFunc for color
    func = oeshape.OEOverlapFunc()
    func.SetupRef(query)
   res = oeshape.OEOverlapResults()
   fits = occhem.oemolistream(argv[2])prep = oeshape.OEOverlapPrep()
    for fitmol in fitfs. GetOEGraphMols():
        prep.Prep(fitmol)
        func.Overlap(fitmol, res)
        print ("title: ss tanimoto combo = s.2f shape tanimoto = s.2f color tanimoto,
\leftarrow = \frac{9}{6}, 2f'' \frac{9}{6}(fitmol.GetTitle(), res.GetTanimotoCombo(),
               res.GetTanimoto(), res.GetColorTanimoto()))
if name == " main ":
    import sys
    sys.exit(main(sys.argy))
```

## 2.4.3 Top hit against shape query

This example reads in a reference query and a few fit molecules, performs overlay optimization, finds the few top hits, and prints them out in final orientation.

#### Listing 15: Finding top ROCS hits against a query

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

```
from openeye import oechem
from openeye import oeshape
def main(argv=[_name_]):
    if len(argv) != 5:
        oechem.OEThrow.Usage("%s <queryfile> <fitfile> <outfile> <hhits>" % argv[0])
   if oechem. OEGetFileExtension(sys.argv[1]) != "sq":
        oechem. OEThrow. Fatal ("Requires a shape query . sq input file format")
   fits = occhem.oemolistream(sys.argv[2])outfs = occhem.oemolostream(sys.arqv[3])nhits = int(sys.argv[4])query = oeshape. 0EShapeQueuery()oeshape.OEReadShapeQuery(sys.argv[1], query)
    # Setup OEROCS with specified number of best hits
   options = oeshape.OEROCSOptions()
   options. SetNumBestHits (nhits)
   rocs = oeshape.OEROCS(options)
   rocs.SetDatabase(fitfs)
    for res in rocs. Overlay (query) :
        outmol = res.GetOverlayConf()
        oechem.OEWriteMolecule(outfs, outmol)
        print ("title: ss tanimoto combo = s.2f" s (outmol. GetTitle (), res.
\rightarrowGetTanimotoCombo()))
if __name__ == "__main__\mathbf{m}_{\mathbf{r}}import sys
    sys.exit(main(sys.argv))
```

# 2.5 Shape from Hermite expansion

Using Hermite expansion we can obtain two functionalities: expand a molecule into Hermite representation and compare two molecules that are in the Hermite representation by computing their shape-Tanimoto coefficient. We illustrate both functionalities below with two examples.

## 2.5.1 Hermite expansion

In this example we input a molecule, set the level of Hermite expansion using NPolyMax variable, determine the optimal parameters for  $\lambda_x, \lambda_y, \lambda_z$ , and perform the computation of the Hermite expansion. At the end we output the resulting Hermite representation of the molecule as a grid, using CreateGrid method of the OEHermite class. The user can vary NPolyMax from low numbers, like 4 or 5, to higher numbers like 10–30 and observe convergence of the shape. Which value to use in practice depends on the size of the input molecule. Input molecule can be drug-like as well as a protein.

#### Listing 16: Expanding a molecular shape into Hermite polynomials

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
from openeye import oegrid
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface(InterfaceData, argv)
    NPolyMax = itf.GetInt("-NPolyMax")gridspacing = itf.GetFloat("-gridspacing")ifname = itf.GetString("-inputfile")
    ofname = \text{iff}. \text{GetString}("-outputgrid") \setminusifs = oechem.oemolistream()
    if (not ifs.open(ifname)):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % ifname)
    if (not ofname.endswith(".grd")):
        oechem. OEThrow. Fatal ("Output grid file extension hast to be '.grd' ")
    mol = occhem. OEMol()if (not oechem. OEReadMolecule(ifs, mol)):
        oechem. OEThrow. Fatal ("Unable to read molecule in %s" % ifname)
```

```
prep = oeshape. 0E0verlapPrep()prep.SetAssignColor(False)
   prep.Prep(mol)
   transfm = occhem.OETrans()oeshape.OEOrientByMomentsOfInertia(mol, transfm)
   hermiteoptions = oeshape.OEHermiteOptions()
   hermiteoptions. SetNPolyMax (NPolyMax)
   hermiteoptions.SetUseOptimalLambdas(True)
   hermite = oeshape.OEHermite(hermiteoptions)
    if (not hermite. Setup (mol)):
       oechem. OEThrow. Fatal ("Was not able to Setup the molecule for the OEHermite..
\leftarrowclass.")
   hopts = hermite.GetOptions()
   print ("Best lambdas found X = " + str(hopts.GetLambdaX()) + " Y = "+ str(hopts.GetLambdaY()) + " Z = " + str(hopts.GetLambdaZ()))print ("Hermite self-overlap=", hermite.GetSelfOverlap())
   basis_size = int ((NPolyMax+1) * (NPolyMax+2) * (NPolyMax+3) /6)
   coeffs = oechem. OEDoubleVector (basis_size)
   hermite.GetCoefficients(coeffs)
   NPolyMaxstring = str(NPolyMax)print ("Hermite coefficients f_{\text{m}}(1,m,n) in the following order l = 0..."
          + NPolyMaxstring + ", m = 0..." + NPolyMaxstring+"-1, n = " +.
\rightarrowNPolyMaxstring + "-1-m :")
    for x in coeffs:
        print (\text{str}(x) + " " ),
   grid = oegrid.OEScalarGrid()hermite. CreateGrid(grid, gridspacing, transfm)
   if (not oegrid.OEWriteGrid(ofname, grid)):
        oechem. OEThrow. Fatal ("Unable to write grid file")
    return 0
#######################################
InterfaceData = \cdots!BRIEF [-inputfile] <InputFileName> [-outputgrid] <OutputGridFileName> [-NPolyMax]
\leftrightarrow<NPolyMax> \
[-numgridpoints] <numgridpoints> [-gridspacing] <gridspacing>
!CATEGORY "input/output options :" 1
  !PARAMETER -inputfile 1
   !ALIAS -in
   !TYPE string
   !REQUIRED true
    !BRIEF Filename of the input molecule
    !KEYLESS 1
```

```
! END
  !PARAMETER -outputgrid 2
  !ALIAS -out
   !TYPE string
    !REQUIRED true
    !BRIEF Filename of the output Hermite grid (needs to have .grd file extension)
    !KEYLESS 2
  !END
! END
!CATEGORY "Hermite options :" 2
  !PARAMETER -NPolyMax 3
   !ALIAS -NP
   !TYPE int
   !REOUIRED false
    !DEFAULT 5
    !LEGAL_RANGE 0 30
    !BRIEF Resolution parameter of Hermite Prep
    !KEYLESS 3
  ! END
  !PARAMETER -gridspacing 4
   !ALIAS -qs
   !TYPE float
   !REOUIRED false
   !DEFAULT 1.0
    !LEGAL_RANGE 0.01 10.0
    !BRIEF Grid spacing of the output Hermite grid
    !KEYLESS 4
  !END
! END
\mathbf{r} \cdot \mathbf{r}#######################################
if name == " main ":
   sys.exit(main(sys.argy))
```

# 2.5.2 Hermite Tanimoto comparison of shape

In the second example below, we set up two molecules and compute the Tanimoto shape similarity coefficient, using Hermite expansion. The Hermite prep parameter NPolyMax\_MAX is used to vary the NPolyMax parameter and compute the shape-Tanimoto coefficient. First molecule in the reference input file is used versus all molecules in the fit input file. Results are attached as SD data to the moved fit molecule, as dictated by Hermite overlay, and sent to the output file. One can observe convergence of the Hermite Tanimoto coefficients as the level of expansion becomes more accurate.

Listing 17: Calculating shape Tanimoto using Hermite expansion

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
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData, argv)
    NPolyMax_MAX = itf.GetInt("-NPolyMax_MAX")
    ifrefname = itf.GetString("-inputreffile")
    iffitname = itf.GetString("-inputfitfile")
    ofname = itf.GetString("-outputfile")
    ifsref = occhem.oemolistream()if not ifsref.open(ifrefname):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % ifrefname)
    ifstit = occhem.oemolistream()if not ifsfit.open(iffitname):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % iffitname)
    refmol = occhem. OEMol()if not oechem. OEReadMolecule(ifsref, refmol):
        oechem. OEThrow. Fatal ("Unable to read molecule in %s" % ifrefname)
    prep = oeshape.OEOverlapPrep()
    prep.SetAssignColor(False)
    prep.Prep(refmol)
    reftransfm = occhem. OETrans()oeshape.OEOrientByMomentsOfInertia(refmol, reftransfm)
    hermiteoptionsref = oeshape.OEHermiteOptions()
    hermiteoptionsref.SetNPolyMax(NPolyMax_MAX)
    hermiteoptionsref.SetUseOptimalLambdas(True)
```

```
hermiteoptionsfit = oeshape.OEHermiteOptions()
   hermiteoptionsfit.SetNPolyMax(NPolyMax_MAX)
   hermiteoptionsfit.SetUseOptimalLambdas(True)
   hermitefunc = oeshape.OEHermiteShapeFunc(hermiteoptionsref, hermiteoptionsfit)
   options = oeshape.OEOverlayOptions()
   options. SetOverlapFunc (hermitefunc)
   overlay = oeshape.OEOverlay(options)
   overlay. SetupRef (refmol)
   ofs = occhem.oemolostream()if not ofs.open(ofname):
       oechem. OEThrow. Fatal ("Unable to open % for writing" % ofname)
   transfm = occhem. OETrans()fitmol = occhem. OEMol()
   while oechem. OEReadMolecule(ifsfit, fitmol):
        prep.Prep(fitmol)
        oeshape.OEOrientByMomentsOfInertia(fitmol, transfm)
        score = oeshape.OEBestOverlayScore()
        overlay. BestOverlay (score, fitmol)
        print ("Hermite Tanimoto = ", score. GetTanimoto())
       oechem. OESetSDData(fitmol, "HermiteTanimoto_"+str(NPolyMax_MAX), str(score.
\rightarrowGetTanimoto()))
       score.Transform(fitmol)
        # Transform from the inertial frame to the original reference mol frame
        reftransfm.Transform(fitmol)
        oeshape.OERemoveColorAtoms(fitmol)
        oechem.OEWriteMolecule(ofs, fitmol)
#######################################
InterfaceData = ''''!BRIEF [-inputreffile] <InputReferenceFileName> [-inputfitfile] <InputFitFileName> \
[-outputfile] <OutputFileName> [-NPolyMax_MAX] <NPolyMax_MAX>
!CATEGORY "input/output options :" 1
 !PARAMETER -inputreffile 1
   !ALIAS -inref
    !TYPE string
   !REQUIRED true
    !BRIEF Input file name with reference molecule (will only read the first,
\rightarrowmolecule).
   IKEYLESS 1
  LEND
 !PARAMETER -inputfitfile 2
   !ALIAS -infit
   !TYPE string
   !REQUIRED true
   !BRIEF Input file name with fit molecules
    !KEYLESS 2
  LEND
```

```
!PARAMETER -outputfile 3
    !ALIAS -out
    !TYPE string
    !REQUIRED true
    !BRIEF Output file name
    !KEYLESS 3
  !END
!END
!CATEGORY "Hermite options :" 2
  !PARAMETER -NPolyMax_MAX 4
   !ALIAS -NP MAX
   !TYPE int
   !REOUIRED false
    !DEFAULT 5
    !LEGAL_RANGE 0 30
    !BRIEF Maximum value of the parameter of the NPolyMax parameter of the Hermite
\leftrightarrowprep
    !KEYLESS 4
  !END
LEND
\mathbf{r} \rightarrow \mathbf{r}#######################################
if name == " main ":
    sys.exit(main(sys.argv))
```

# 2.6 Flexible Overlay with Shape, Color, and Forcefield

By incorporating Forcefield into the overlay optimization alongside Shape and Color, molecular flexibility can be introduced to the input fit molecule conformers. The flexible overlay optimization approach maintains rigidity in the reference molecule conformer while allowing for flexibility in the fit molecules. To illustrate the functionality of flexible overlay, we provide two examples. Note that, the default settings for the OEFlexiOverlay perform optimization on both Shape and Color overlap while also considering intra-molecular forcefield.

It is important to note that when running flexible overlay optimization of a molecule against itself, the user should not expect to obtain a tanimotocombo value of 2.0. This is because the fit molecules undergo flexible optimization, which includes intra-molecular force field, and thus may result in some deviation from 2.0.

# 2.6.1 Flexible Overlay

In this example, Flexible overlay optimization of the fit molecules is performed against a single reference molecule conformer. Results of flexible overlay of all of the fit molecule conformers are reported and saved.

#### Listing 18: Flexible overlay optimization

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
def main(argv=[__name__]):
   overlayOpts = oeshape.OEFlexiOverlayOptions()
    opts = oechem. OERefInputAppOptions (overlayOpts, "FlexiOverlay", oechem.
\rightarrowOEFileStringType_Mol3D,
                                       oechem.OEFileStringType_Mol3D, oechem.
→OEFileStringType_Mol3D, "-refmol")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    overlayOpts. UpdateValues (opts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
   rfs = oechem.oemolistream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
   ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    refmol = occhem. OEMol()
    oechem.OEReadMolecule(rfs, refmol)
    print ("Ref. Title:", refmol.GetTitle())
```

```
overlay = oeshape.OEFlexiOverlay(overlayOpts)
    overlay. SetupRef (refmol)
    for fitmol in ifs. GetOEMols () :
        results = overlay. Overlay (fitmol)
        for res, conf in zip(results, fitmol. GetConfs()):
            print ("Fit Title: 8-4s Tanimoto Combo: 8.2f Energy: 82f''% (fitmol.GetTitle(), res.GetTanimotoCombo(), res.
\rightarrowGetInternalEnergy()))
            oechem. OESetSDData (conf, "Tanimoto Combo", "%. 2f" % res.
\rightarrowGetTanimotoCombo())
            oechem. OESetSDData(conf, "Energy", "%. 2f" % res. GetInternalEnergy())
        oechem.OEWriteMolecule(ofs, fitmol)
if name == "_main_":
    sys.exit(main(sys.argv))
```

## 2.6.2 Flexible Best Overlay

In this example, Flexible overlay optimization of the fit molecules is performed against a single reference molecule conformer. The best overlaid conformers and the corresponding results are reported and saved.

#### **Listing 19: Flexible best overlay**

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
```

```
(continued from previous page)
```

```
from openeye import oechem
from openeye import oeshape
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    overlayOpts = oeshape.OEFlexiOverlayOptions()
    opts = oechem.OERefInputAppOptions(overlayOpts, "FlexiBestOverlay", oechem.
\rightarrowOEFileStringType_Mol3D,
                                          oechem.OEFileStringType_Mol3D, oechem.
\rightarrowOEFileStringType_Mol3D, "-refmol")
    if oechem. OEConfigureOpts(opts, argv, False) == oechem. OEOptsConfigureStatus_Help:
        return 0
    overlayOpts. UpdateValues (opts)
    if s = oechem. oemolistream()if not ifs.open(opts.GetInFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetInFile())
    rfs = oechem.oemolistream()if not rfs.open(opts.GetRefFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for reading" % opts. GetRefFile())
    ofs = occhem.oemolostream()if not ofs.open(opts.GetOutFile()):
        oechem. OEThrow. Fatal ("Unable to open %s for writing" % opts. GetOutFile())
    refmol = occhem. OEMol()
    oechem.OEReadMolecule(rfs, refmol)
    print ("Ref. Title:", refmol. GetTitle())
    overlay = oeshape.OEFlexiOverlay(overlayOpts)
    overlay. SetupRef (refmol)
    for fitmol in ifs. GetOEMols():
        results = oeshape.OEFlexiOverlapResults()
        if overlay. BestOverlay (results, fitmol):
             print ("Fit Title: 8-4s Tanimoto Combo: 8.2f Energy: 82f"
                   % (fitmol.GetTitle(), results.GetTanimotoCombo(), results.
\rightarrowGetInternalEnergy()))
            oechem. OESetSDData(fitmol, "Tanimoto Combo", "%. 2f" % results.
\rightarrowGetTanimotoCombo())
            oechem. OESetSDData(fitmol, "Energy", "%. 2f" % results. GetInternalEnergy())
            oechem.OEWriteMolecule(ofs, fitmol)
        else:
            print ("Failed Title: \frac{6}{6} - 4s" % (fitmol. GetTitle()))
if _name_ = "main":
    sys.exit(main(sys.argv))
```

# **2.7 Advanced Examples**

## 2.7.1 Calculating NxN scores

There are times when you want to have all the pairwise scores among a set of molecules. Maintaining this 2D matrix of scores is more complicated than the single set of scores from the *ref vs. set of fit molecules* examples shown above.

This example takes a set of molecules and performs all the pairwise shape optimizations with OEBestOverlay. It outputs a *spreadsheet* of the scores.

#### **Listing 20: Calculating NxN scores.**

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
from openeye import oeshape
def oneConf(conf, prep, filename, csvfile):
    csvfile.write("%s_%d" % (conf.GetTitle(), conf.GetIdx()))
   refmol = oechem.OEGraphMol(conf)
   options = oeshape.OEOverlayOptions()
   options.SetOverlapFunc(oeshape.OEGridShapeFunc())
   overlay = oeshape.OEOverlay(options)
   overlay. SetupRef (refmol)
   bfs = oechem.oemolistream(filename)
   fitmol = occhem. OEMol()
   while oechem. OEReadMolecule (bfs, fitmol) :
        prep.Prep(fitmol)
        scoreiter = oeshape.OEBestOverlayScoreIter()
        oeshape.OESortOverlayScores(scoreiter, overlay.Overlay(fitmol), oeshape.
\rightarrowOEHighestTanimoto(), 1, True)
        for score in scoreiter:
           csvfile.write(", %.2f" % score.GetTanimoto())csvfile.write("n")
```

```
def genHeader(filename, csvfile):
   csvfile.write("name")
   ifs = oechem.oemolistream(filename)
   mol = occhem. OEMol()while oechem. OEReadMolecule(ifs, mol):
        for conf in mol. GetConfs():
           csvfile.write(", %s_%d" % (conf.GetTitle(), conf.GetIdx()))
   csvfile.write("n")def main(argv=[_name_]):
   if len(argv) != 3:
       oechem.OEThrow.Usage("%s <infile> <csvfile>" % argv[0])
   csvfile = open(argv[2], "w")genHeader(sys.argv[1], csvfile)
   prep = oeshape. 0E0verlapPrep()prep. SetAssignColor (False)
   afs = occhem.oemolistream(argv[1])for molA in afs. GetOEMols():
       prep.Prep(molA)
       print (molA.GetTitle())
        for conf in molA. GetConfs():
            oneConf(conf, prep, sys.argv[1], csvfile)
if _name == " main":
    import sys
    sys.exit(main(sys.argv))
```

# 2.7.2 Calculating shape characteristics

While most functionality in the Shape Toolkit involves comparison of pairs of molecules, there are a few fundamental properties that can be calculated for a single molecule. All of these calculations are done using the same basic Gaussian description of a molecule as described above.

The simplest property to calculate is volume, using OECalcVolume.

In addition to simple volume calculations, the steric multipoles of a molecule can also be calculated. See section OECalcShapeMultipoles.

This next example demonstrates the calculation of volume and shape multipoles.

Listing 21: Calculating shape properties.

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
from openeye import oeshape
def main(argv=[_name_]):
   if len(argv) != 2:
        oechem.OEThrow.Usage("%s <infile>" % argv[0])
   ifs = oechem.oemolistream(argv[1])for mol in ifs. GetOEGraphMols():
        oechem.OEThrow.Info("
                                           Title: %s" % mol. GetTitle())
        oechem.OEThrow.Info("
                                         Volume: %8.2f" % oeshape.OECalcVolume(mol))
        oechem. OEThrow. Info("Volume: (without H): 88.2f\n" % oeshape. OECalcVolume(mol,
\rightarrow False))
        smult = oeshape.OECalcShapeMultipoles(mol)
        oechem. OEThrow. Info (" Steric multipoles:")
        oechem.OEThrow.Info("
                                       monopole: 8.2f'' % smult [0])
        oechem.OEThrow.Info(" quadrupoles: %8.2f %8.2f %8.2f"
                            % (smult[1], smult[2], smult[3]))
                                octopoles:")
        oechem.OEThrow.Info("
        oechem.OEThrow.Info("
                                             xxx: %8.2f                                    
                            % (smult[4], smult[5], smult[6]))
                                            xxy: %8.2f xxz: %8.2f yyx: %8.2f"
        oechem.OEThrow.Info("
                            % (smult[7], smult[8], smult[9]))
        oechem.OEThrow.Info("
                                            yyz: %8.2f zzx: %8.2f zzy: %8.2f"
                            % (smult[10], smult[11], smult[12]))oechem.OEThrow.Info("
                                            xyz: \; \$8.2f \, \text{m} \; \$ \; \text{smult}[13])if _name_ = = "_main_".import sys
    sys.exit(main(sys.argv))
```

### 2.7.3 Calculating excluded volume

This code demonstrates how to use the Shape toolkit to do an overlay to a crystallographic ligand, then calculate the overlap of the database molecule to the cognate protein. The output includes a new score Rescore which is the ShapeTanimotoCombo penalized by the fraction overlap.

A description of the command line interface can be obtained by executing the program with the -help argument.

prompt> python excludevolume.py --help

will generate the following output:

-q : Query file name

```
-e : Protein to use as exclusion volume
-d : Database file name
-o : Output file name
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
import os
import sys
from openeye import oechem
from openeye import oeshape
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    itf = oechem. OEInterface (InterfaceData, argy)
    # Set up best overlay to the query molecule
   qfs = oechem.oemolistream()if not qfs.open(itf.GetString("-q")):oechem. OEThrow. Fatal ("Unable to open %s" % itf. GetString ("-q"))
   qmol = occhem. OEMol()oechem.OEReadMolecule(qfs, qmol)
    # Set up overlap to protein exclusion volume
   efs = oechem.oemolistream()if not efs.open(itf.GetString("-e")):
        oechem. OEThrow. Fatal ("Unable to open %s" % itf. GetString ("-e"))
    emol = oechem. <math>OEMol()</math>
```

```
oechem.OEReadMolecule(efs, emol)
   evol = oeshape.OEExactShapeFunc()
   evol.SetupRef(emol)
    # open database and output streams
    if s = oechem.oemolistream()if not ifs.open(itf.GetString("-d")):
       oechem. OEThrow. Fatal ("Unable to open %s" % itf. GetString ("-d") )
   ofs = oechem.oemolostream()
   if not ofs.open(itf.GetString("-o")):
       oechem.OEThrow.Fatal("Unable to open %s" % itf.GetString("-o"))
   print ("Title
                                Combo Rescore")
   for mol in ifs. GetOEMols () :
        res = oeshape.OEROCSResult()
        oeshape.OEROCSOverlay(res, qmol, mol)
        outmol = res.GetOverlayConf()
        # calculate overlap with protein
        eres = oeshape.OEOverlapResults()
        evol.Overlap(outmol, eres)
       frac = eres.GetOverlap() / eres.GetFitSelfOverlap()
        rescore = res.GetTanimotoCombo() - frac# attach data to molecule and write it
        oechem. OESetSDData (outmol, "TanimotoCombo", "%-. 3f" % res. GetTanimotoCombo())
        oechem. OESetSDData (outmol, "Exclusion Volume", "%-. 3f" % eres. overlap)
        oechem. OESetSDData (outmol, "Fraction Overlap", "%-. 3f" % frac)
        oechem. OESetSDData (outmol, "Rescore", "%-. 3f" % rescore)
       oechem.OEWriteMolecule(ofs, outmol)
       print ("8-20s 8.3f 8.3f" 8(outmol.GetTitle(), res.GetTanimotoCombo(), rescore))
#######################################
InterfaceData = """!CATEGORY % (prog) s
 !BRIEF % (prog) s [-q] <query> [-e] <exclusion> [-d] <database> [-o] <output>
 !PARAMETER -q 1
   !TYPE string
   !REQUIRED true
    !BRIEF Query file name
   !KEYLESS 1
  ! END
 !PARAMETER -e 2
   !TYPE string
   !REQUIRED true
   !BRIEF Protein to use as exclusion volume
   !KEYLESS 2
 !END
  !PARAMETER -d 3
   !TYPE string
```

```
!REQUIRED true
   !BRIEF Database file name
   !KEYLESS 3
 ! END
 !PARAMETER -0 4
   !TYPE string
   !REQUIRED true
   !BRIEF Output file name
   !KEYLESS 4
 ! END
! END
""" % { "prog": os.path.basename (sys.argv[0]) }
#######################################
if __name__ == "__main__".sys.exit(main(sys.argv))
```

# **CHAPTER**

# **THREE**

**API** 

# **3.1 OEShape Classes**

# 3.1.1 OEAnalyticColorFunc

class OEAnalyticColorFunc : public OEShapeFunc

The OEAnalyticColorFunc class defines color overlap between a reference object and a fit molecule, using the Analytic method.

![](_page_60_Figure_7.jpeg)

### The following methods are publicly inherited from OEFunc0:

· operator()

- · GetFComponents
- · NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupFlex
- · SetupRef

The following methods are publicly inherited from OEColorFunc:

· GetColorOptions

#### The OEAnalyticColorFunc class defines the following public methods:

· GetAnalyticOptions

#### **Constructors**

```
OEAnalyticColorFunc()
OEAnalyticColorFunc(const OEColorOptions&)
OEAnalyticColorFunc(const OEAnalyticOptions&)
OEAnalyticColorFunc(const OEColorOptions&, const OEAnalyticOptions&)
OEAnalyticColorFunc(const OEAnalyticColorFunc&)
```

#### Default and copy constructors.

Constructs an *OEAnalyticColorFunc* instance using the specified set of parameters.

### operator=

OEAnalyticColorFunc & operator=(const OEAnalyticColorFunc &)

The assignment operator.

#### **GetAnalyticOptions**

const OEAnalyticOptions& GetAnalyticOptions() const

Returns a reference to the OEAnalyticOptions instance as currently set for this OEAnalyticColorFunc.

## 3.1.2 OEAnalyticOptions

class OEAnalyticOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for calculations with the Analytic method.

The OEAnalyticOptions class defines the following public methods:

- GetExpType
- · GetProxyGridCutoff
- · GetUseProxyGrid
- SetExpType
- SetProxyGridCutoff
- SetUseProxyGrid

### **Constructors**

```
OEAnalyticOptions()
OEAnalyticOptions (const OEAnalyticOptions&)
```

Default and copy constructors.

#### operator=

```
OEAnalyticOptions &operator=(const OEAnalyticOptions &)
```

### **GetExpType**

unsigned int GetExpType() const

Gets the current value of the exponential type used by the function.

### **GetProxyGridCutoff**

double GetProxyGridCutoff() const

Gets the proxy grid cutoff currently set.

#### **GetUseProxyGrid**

bool GetUseProxyGrid() const

Returns the state of the use proxy grid flag. If true, proxy grid would be used to decide if an atom pair should be included in calculations.

### **SetExpType**

bool SetExpType (const unsigned int)

Set the exponential type to be used for calculation. The default is  $OEExponentialType\_Standard$ . Alternatives are defined in the OEExponentialType namespace.

### **SetProxyGridCutoff**

bool SetProxyGridCutoff (const double)

Set the radius to use when using proxy grid is turned on. By default this is set to 3.0 Å.

#### **SetUseProxyGrid**

**bool** SetUseProxyGrid(const bool)

Sets the state of the use proxy grid flag. If true, proxy grid would be used to decide if an atom pair should be included in calculations.

### 3.1.3 OEAnalyticShapeFunc

class OEAnalyticShapeFunc : public OEShapeFunc

The OEAnalyticShapeFunc class defines shape overlap between a reference object and a fit molecule, using the Analytic method.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- $\bullet$  Setup

The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupFlex
- SetupRef

The following methods are publicly inherited from OEShapeFunc:

• GetShapeOptions

The OEAnalyticShapeFunc class defines the following public methods:

![](_page_64_Figure_1.jpeg)

· GetAnalyticOptions

### **Constructors**

```
OEAnalyticShapeFunc()
{\tt OEAnalyticShapeFunc}({\tt const\;\;OEShapeOptions\&})OEAnalyticShapeFunc(const OEAnalyticOptions&)
{\tt OEAnalyticShapeFunc} ({\tt const\ } {\tt OS} {\tt Map} {\tt OD} {\tt tions} \, \& \textit{\textbf{, const\ } OEAnalyticOptions} \, \& \textit{\textbf{)} }OEAnalyticShapeFunc(const OEAnalyticShapeFunc&)
```

### Default and copy constructors.

Constructs an OEAnalyticShapeFunc instance using the specified set of parameters.

### operator=

OEAnalyticShapeFunc & operator= (const OEAnalyticShapeFunc &)

The assignment operator.

### **GetAnalyticOptions**

const OEAnalyticOptions& GetAnalyticOptions() const

Returns a reference to the OEAnalyticOptions instance as currently set for this OEAnalyticShapeFunc.

# 3.1.4 OEAsIsStarts

class OEAsIsStarts : public OEStarts

The OEAsIsStarts represents the AsIs start for overlay optimization. The OEAsIsStarts takes the fit conformer as-is, without any rotation or translation.

The following methods are publicly inherited from OEStarts:

- CreateCopy
- · GetNumOfStarts
- · GetStarts
- $\bullet$  Setup
- SetupRef

### **Constructors**

```
OEAsIsStarts()
OEAsIsStarts (const OEAsIsStarts&)
```

Default and copy constructors.

#### operator=

OEAsIsStarts & operator=(const OEAsIsStarts &)

The assignment operator.

# 3.1.5 OEAtAtomStarts

class OEAtAtomStarts : public OEInertialStarts

The OEAtAtomStarts represents the AtAtom starts for overlay optimization. The OEAtAtomStarts translates the fit molecule to the specified atom center of the reference molecule, followed by the inertial rotations to generate starts.

The following methods are publicly inherited from OEStarts:

- CreateCopy
- · GetNumOfStarts
- · GetStarts
- · Setup

• SetupRef

The following methods are publicly inherited from OEInertialStarts:

- · GetSymmetryThreshold
- · SetSymmetryThreshold

### **Constructors**

```
OEAtAtomStarts()
OEAtAtomStarts(const OESystem::OEUnaryPredicate<OEChem::OEAtomBase>&)
OEAtAtomStarts (const OEAtAtomStarts&)
```

Default and copy constructors. Use the second constructor to specify the at center to be picked for AtAtom starts. By default the heavy atoms of reference molecule are picked.

#### operator=

OEAtAtomStarts & operator=(const OEAtAtomStarts &)

The assignment operator.

# 3.1.6 OEBestOverlayResults

class OEBestOverlayResults

#### **Constructors**

```
OEBestOverlayResults()
OEBestOverlayResults (const OEBestOverlayResults & rhs)
```

Default and copy constructors.

#### operator=

OEBestOverlayResults & operator=(const OEBestOverlayResults & rhs)

#### **AddScore**

**bool** AddScore (const OEBestOverlayScore &sc)

#### **Clear**

bool Clear()

#### **GetScores**

```
OESystem::OEIterBase<OEBestOverlayScore> *GetScores() const
OESystem:: OEIterBase<OEBestOverlayScore> *
  GetScores (const OESystem:: OEBinaryPredicate<OEBestOverlayScore,
            OEBestOverlayScore> &sorter, int nbest=1) const
```

# 3.1.7 OEBestOverlayScore

```
class OEBestOverlayScore : public OEOverlapResults
```

This class extends the OEOverlapResults to represent the results of a single overlay optimization between a reference and a fit object.

### The following methods are publicly inherited from OEOverlapResults:

- · GetColorScore
- · GetColorTanimoto
- · GetColorTversky
- · GetFitColorTversky
- · GetFitSelfColor
- GetFitSelfOverlap
- · GetFitTversky
- · GetFitTverskyCombo
- · GetOverlap
- · GetRefColorTversky
- · GetRefSelfColor
- GetRefSelfOverlap
- · GetRefTversky
- · GetRefTverskyCombo
- GetTanimoto
- · GetTanimotoCombo
- GetTversky

The OEBestOverlayScore class defines the following public methods:

- · GetFitConfIdx
- · GetRefConfIdx
- GetRotMatrix

- · GetTranslation
- Transform

#### **Constructors**

```
OEBestOverlayScore()
OEBestOverlayScore(const OEBestOverlayScore&)
```

Default and copy constructors.

#### operator=

OEBestOverlayScore & operator= (const OEBestOverlayScore&)

### **GetFitConfldx**

unsigned int GetFitConfIdx() const

Returns the conformer index of the fit conformer.

#### **GetRefConfldx**

unsigned int GetRefConfIdx() const

Returns the conformer index of the reference conformer.

### **GetRotMatrix**

void GetRotMatrix (float\*) const

Returns the rotation matrix to be applied on the fit conformer to obtain the optimized overlay. With OpenEye convention, rotation should be applied before the translation.

### **GetTranslation**

void GetTranslation (float\*) const

Returns the translation vector to be applied on the fit conformer to obtain the optimized overlay. With OpenEye convention, rotation should be applied before the translation.

### **Transform**

```
bool Transform (OEChem:: OEMolBase&) const
bool Transform (OEChem:: OEConfBase&) const
```

Transforms the molecule to optimized overlay position.

# 3.1.8 OECartesianStarts

```
class OECartesianStarts : public OEInertialStarts
```

The OECartesianStarts represents the user defined cartesian starts for overlay optimization. The OECartesianStarts translates the fit molecule to the specified starting points, followed by the inertial rotations to generate starts.

#### The following methods are publicly inherited from OEStarts:

- CreateCopy
- · GetNumOfStarts
- GetStarts
- · Setup
- SetupRef

#### The following methods are publicly inherited from OEInertialStarts:

- · GetSymmetryThreshold
- · SetSymmetryThreshold

The OECartesianStarts class defines the following public methods:

- · ClearStartPoints
- · GetNumStartPoints
- GetStartPoints
- SetStartPoints

#### **Constructors**

```
OECartesianStarts()
OECartesianStarts(const OECartesianStarts&)
```

Default and copy constructors.

operator=

```
OECartesianStarts &operator=(const OECartesianStarts &)
```

The assignment operator.

### **ClearStartPoints**

void ClearStartPoints()

Clears the currently specified cartesian start points.

### **GetNumStartPoints**

unsigned GetNumStartPoints()

Get the number of specified cartesian start points.

#### **GetStartPoints**

unsigned GetStartPoints (double \*Points)

Get the specified cartesian start points. Method expects an array of size 3\*NumPoints for the argument, where NumPoints can be obtained by calling GetNumStartPoints.

#### **SetStartPoints**

void SetStartPoints (const double \*Points, unsigned int NumPoints)

Sets the cartesian starting points. Method expects an array of size 3\*NumPoints for the first argument.

### 3.1.9 OEColorFFParameter

```
class OEColorFFParameter : public OESystem:: OEMultiParameter
→<OEShape::OEColorForceField>
```

The OEColorFFParameter represents parameter that has a value of type OEColorForceField.

#### Following methods are publicly inherited from OEParameter:

- · AddAlias and GetAliases
- · AddDetail and GetDetail
- · AddIllegalRange and GetIllegalRanges
- AddIllegalValue and GetIllegalValues
- · AddLegalRange and GetLegalRanges
- . AddStringDefault, GetStringDefault and GetStringDefaults

- · AddStringValue, GetStringValue and GetStringValues
- · ClearDefaults
- · ClearValues
- CreateCopy
- GetBrief and SetBrief
- · GetHasDefault
- · GetHasValue
- · GetIsList and SetIsList
- · GetKeyless and SetKeyless
- · GetName and SetName
- · GetOrderPriority and SetOrderPriority
- · GetVisibility and SetVisibility
- · IsLegalString
- · IsSet and IsSetToString

### Following methods are publicly inherited from OEMultiParameter:

- · AddLegalEntry
- · GetDefault and SetDefault
- · GetSetting
- · GetValue and SetValue

#### **Constructors**

```
OEColorFFParameter()
OEColorFFParameter (const std::string& name)
OEColorFP parameter (const OEColorFFParameter&)
```

#### Default and copy constructors.

Constructs an OEColorFFParameter instance using the specified set of parameters.

#### operator=

OEColorFFParameter & operator= (const OEColorFFParameter &)

The assignment operator.

# 3.1.10 OEColorForceField

```
class OEColorForceField
```

This class represents OEColorForceField.

### **Constructors**

```
OEColorForceField()
OEColorForceField(const OEColorForceField &rhs)
OEColorForceField(const OEColorForceFieldImpl *impl)
```

Default and copy constructors.

#### operator=

```
OEColorForceField &operator=(const OEColorForceField &rhs)
```

### **AddColorer**

```
bool AddColorer (unsigned int type, const char *smarts)
bool AddColorer (unsigned int type, const std::string &smarts)
```

### **AddInteraction**

```
bool AddInteraction (unsigned int type1, unsigned int type2,
                    const std::string &interaction_type, float weight,
                    float range)
```

### **AddType**

```
unsigned int AddType (const char *name)
unsigned int AddType (const std:: string & name)
```

**Clear** 

void Clear()

### **ClearInteractions**

void ClearInteractions()

### **GetTitle**

const char \*GetTitle() const

#### **GetType**

unsigned int GetType (std::string k) const

### **GetTypeName**

std::string GetTypeName(unsigned int type) const

#### **GetTypes**

OESystem:: OEIterBase<unsigned int>\* GetTypes(std:: string k) const

### Init

```
bool Init (unsigned int cffType)
bool Init (OEPlatform::oeistream &is, bool verbose=false)
bool Init (const std::string &filename, bool verbose=false)
```

### **Ready**

bool Ready () const

#### **SetTitle**

bool SetTitle(const char \*title)

**Write** 

**bool** Write (OEPlatform:: oeostream &os)

# 3.1.11 OEColorFunc

```
class OEColorFunc : public OEOverlapFuncBase
```

The OEColorFunc is an abstract base class. This class defines an interface for color overlap calculation between a reference object and a fit molecule. The OEColorFunc is a specialization of The OEOverlapFuncBase for color only overlap.

![](_page_74_Figure_6.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- · NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

### The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

#### The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupFlex
- SetupRef

#### The OEColorFunc class defines the following public methods:

· GetColorOptions

The following classes derive from this class:

- OEAnalyticColorFunc
- OEExactColorFunc
- OEGridColorFunc

#### **GetColorOptions**

const OEColorOptions& GetColorOptions() const

Returns a reference to the OEColorOptions instance as currently set for this OEColorFunc.

## 3.1.12 OEColorOptions

class OEColorOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for OEColorFunc calculations.

The OEColorOptions class defines the following public methods:

- GetColorForceField and SetColorForceField
- · GetMultiplier and SetMultiplier
- · GetScoreType and SetScoreType

### **Constructors**

```
OEColorOptions()
OEColorOptions (const OEColorOptions&)
```

Default and copy constructors.

#### operator=

OEColorOptions & operator=(const OEColorOptions &)

### **GetColorForceField**

const OEColorForceField\* GetColorForceField() const

See Set ColorForceField method.

#### **GetMultiplier**

double GetMultiplier () const

See SetMultiplier method.

### **GetScoreType**

unsigned int GetScoreType() const

See Set ScoreType method.

### **SetColorForceField**

```
bool SetColorForceField(unsigned int type)
bool SetColorForceField(OEPlatform::oeistream &is)
bool SetColorForceField(const std::string &filename)
bool SetColorForceField(const OEColorForceField &cff)
```

Sets the color force field to be used. By default the ImplicitMillsDean color force field is used.

#### **SetMultiplier**

bool SetMultiplier (const double)

Sets the multiplier to the color score. THe multiplier only effects the color score and has no effect on the color tanimoto. Default: 1.0

#### **SetScoreType**

bool SetScoreType (const unsigned)

Sets the score type to be reported by this function. Possible values are defined in the  $OEScoreType$  namespace. Default: OEScoreType\_Overlap

# 3.1.13 OEColorTanimotoCutoff

class OEColorTanimotoCutoff : public OEOverlayScoreCutoff

The OEColorTanimotoCutoff defines cutoff based on the color tanimoto.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator()
- CreateCopy

#### **Constructors**

OEColorTanimotoCutoff(const double)

Default and copy constructors. The argument expects the desired cutoff.

## 3.1.14 OEExactColorFunc

class OEExactColorFunc : public OEShapeFunc

The OEExactColorFunc class defines shape overlap between a reference object and a fit molecule, using the Exact method.

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- $\bullet$  NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupFlex
- SetupRef

The following methods are publicly inherited from OEColorFunc:

· GetColorOptions

![](_page_78_Figure_1.jpeg)

### **Constructors**

```
OEExactColorFunc()
OEExactColorFunc(const OEColorOptions&)
OEExactColorFunc(const OEExactColorFunc&)
```

#### Default and copy constructors.

Constructs an OEExactColorFunc instance using the specified set of parameters.

### operator=

OEExactColorFunc & operator=(const OEExactColorFunc &)

The assignment operator.

## 3.1.15 OEExactShapeFunc

class OEExactShapeFunc : public OEShapeFunc

The OEExactShapeFunc class defines shape overlap between a reference object and a fit molecule, using the Exact method.

![](_page_79_Figure_4.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

### The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupFlex
- SetupRef

#### The following methods are publicly inherited from OEShapeFunc:

· GetShapeOptions

#### **Constructors**

```
OEExactShapeFunc()
OEExactShapeFunc(const OEShapeOptions&)
OEExactShapeFunc(const OEExactShapeFunc&)
```

Default and copy constructors.

Constructs an OEExactShapeFunc instance using the specified set of parameters.

#### operator=

OEExactShapeFunc & operator=(const OEExactShapeFunc &)

The assignment operator.

### 3.1.16 OEFitColorTverskyCutoff

class OEFitColorTverskyCutoff : public OEOverlayScoreCutoff

The OEFitColorTverskyCutoff defines cutoff based on the fit molecule color tversky.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- $\bullet$  operator()
- CreateCopy

#### **Constructors**

OEFitColorTverskyCutoff(const double)

Default and copy constructors. The argument expects the desired cutoff.

### 3.1.17 OEFitTverskyComboCutoff

class OEFitTverskyComboCutoff : public OEOverlayScoreCutoff

The OEFitTverskyComboCutoff defines cutoff based on the fit molecule combined shape and color tversky.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

• operator()

• CreateCopy

#### **Constructors**

```
OEFitTverskyComboCutoff(const double)
```

Default and copy constructors. The argument expects the desired cutoff.

# 3.1.18 OEFitTverskyCutoff

class OEFitTverskyCutoff : public OEOverlayScoreCutoff

The OEFitTverskyCutoff defines cutoff based on the fit molecule shape tversky.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator ()
- CreateCopy

### **Constructors**

OEFitTverskyCutoff(const double)

Default and copy constructors. The argument expects the desired cutoff.

### 3.1.19 OEFlexiOverlapFunc

class OEFlexiOverlapFunc : public OEMolPotential:: OEMolFunc1

The OEFlexiOverlapFunc class defines an interface for static overlap calculation between a reference and a fit molecule. The OEFlexiOverlapFunc extends the OEMolFunc1 class to allow setting up a reference molecule and the underlying functions defining interactions based on shape and color overlaps along with intra-molecular force field of the fit molecule.

### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

### The following methods are publicly inherited from OEFunc1:

• operator()

### The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

The OEFlexiOverlapFunc class defines the following public methods:

- · Overlap
- · SetupRef
- · UpdateColorCoords

# 3.1.20 Overlap

```
bool Overlap (const double*, OEFlexiOverlapResults&)
bool Overlap (const OEChem:: OEMolBase, OEFlexiOverlapResults&)
```

These methods calculate the staitc overlap between the reference and the fit molecule using shape, color, and force field. The reference object must be set using the  $SetuppRef$  method. The first overload assumes that the fit molecule has been set using the Setup method and uses the specified coordinates for the fit molecule. The second overlap takes the specified fit molecule and its current coordinates.

## 3.1.21 SetupRef

```
bool SetupRef (const OEChem:: OEMolBase&)
bool SetupRef (const OEShape:: OEShapeQueryBase&)
```

This method defines the interface for setting up the reference system for the OEFlexiOverlapFunc instance with a molecule or a shape query.

### 3.1.22 UpdateColorCoords

```
bool UpdateColorCoords (const double* coords, std::vector<double>&...
→updatedCoord)
```

This method takes the coordinate of fit molecule and updates the coordinate of color atoms based on the modified coordinate of their parent atoms. The fit molecule must be set using the Setup method which assigns color atoms to the passed moleucle.

### 3.1.23 OEFlexiOverlapOptions

class OEFlexiOverlapOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for OEFlexiOverlapFunc.

The OEFlexiOverlapOptions class defines the following public methods:

- Validate
- GetShapeFuncType and SetShapeFuncType
- · GetColorFuncType and SetColorFuncType
- · GetForceField and SetForceField
- GetHarmonic and SetHarmonic
- · GetShapeOptions and SetShapeOptions

- · GetColorOptions and SetColorOptions
- GetOverlapFunc and SetOverlapFunc

#### **Constructor**

```
OEFlexiOverlapOptions();
OEFlexiOverlapOptions (const OEFlexiOverlapOptions&)
```

#### Default and copy constructors.

#### operator=

OEFlexiOverlapOptions & operator=(const OEFlexiOverlapOptions&)

### 3.1.24 Validate

bool Validate() const

Returns True if the provided options corresponding to OEFlexiOverlapOptions are valid.

# 3.1.25 GetShapeFuncType

```
unsigned GetShapeFuncType() const
```

Gets the current type of OEShapeFunc used for shape overlap calculations. See also Set ShapeFuncType method.

## 3.1.26 GetColorFuncType

unsigned GetColorFuncType() const

Gets the current type of OEColorFunc used for color overlap calculations. See also Set ColorFuncType method.

## 3.1.27 GetForceField

unsigned GetForceField() const

Gets the current type of ligand force field used. See also SetForceField method.

## 3.1.28 GetHarmonic

bool GetForceField() const

Returns True if the harmonic constraints are added to the force field for the flexible overlap optimizations.

# 3.1.29 GetShapeOptions

```
OEShapeOptions& GetShapeOptions()
const OEShapeOptions& GetShapeOptions() const
```

Returns a reference to the OEShapeOptions instance as currently set. These options are used in flexible overlap optimization of conformers. See also Set ShapeOptions method.

## 3.1.30 GetColorOptions

```
OEColorOptions& GetColorOptions()
const OEColorOptions& GetColorOptions() const
```

Returns a reference to the OEColorOptions instance as currently set. These options are used in flexible overlap optimization of conformers. See also SetColorOptions method.

# 3.1.31 GetOverlapFunc

const OEOverlapFuncBase& GetOverlapFunc() const

Returns a reference to the *OEOverlapFuncBase* instance as currently set. This defines the shape/color interactions to be optimized for overlay.

# 3.1.32 SetShapeFuncType

bool SetShapeFuncType (const unsigned)

Sets the type of *OEShape::OEShapeFunc* to be used for shape overlap calculations. The default is OEShapeType\_Grid. Alternatives are defined in the OEShapeType namespace.

# 3.1.33 SetColorFuncType

```
bool SetColorFuncType (const unsigned)
```

Sets the type of *OEShape::OEColorFunc* to be used for color overlap calculations. The default is OEColorType\_Exact. Alternatives are defined in the OEColorType namespace.

# 3.1.34 SetForceField

bool SetForceField (const unsigned)

Sets the type of ligand intra-molecular force field to be used for fixible optimizations. The default is OELigandFFType\_SAGE. Alternatives are defined in the OELigandFFType namespace.

## 3.1.35 SetHarmonic

void SetHarmonic (const bool)

This flag defines if the harmonic constraints should be added to the force field for the flexible overlap optimizations. Default False.

# 3.1.36 SetShapeOptions

void SetShapeOptions (const OEShapeOptions&)

Sets the options related to OEShapeFunc calculations used in flexible overlap optimization by passing in OEShapeOptions instance.

# 3.1.37 SetColorOptions

void SetColorOptions (const OEColorOptions&)

Sets the options related to OEColorFunc calculations used in flexible overlap optimization by passing in OEColorOptions instance.

## 3.1.38 SetOverlapFunc

void SetOverlapFunc (const OEOverlapFuncBase&)

Sets the overlap function by passing in an OEOverlapFuncBase instance. This defines the shape/color interactions to be optimized for overlay.

# 3.1.39 OEFlexiOverlapResults

class OEFlexiOverlapResults : public OEShape:: OEOverlapResults

This class extends the OEOverlapResults to represent the results of OEFlexiOverlapFunc calculation.

See also:

• OEOverlapResults class

The following methods are publicly inherited from OEOverlapResults:

- · GetColorScore
- · GetColorTanimoto

- · GetColorTversky
- · GetFitColorTversky
- GetFitSelfColor
- GetFitSelfOverlap
- · GetFitTversky
- · GetFitTverskyCombo
- GetOverlap
- GetRefColorTversky
- GetRefSelfColor
- GetRefSelfOverlap
- GetRefTversky
- · GetRefTverskyCombo
- · GetTanimoto
- · GetTanimotoCombo
- GetTversky

#### The OEFlexiOverlapResults class defines the following public method:

· GetInternalEnergy

### **Constructor**

```
OEFlexiOverlapResults();
OEFlexiOverlapResults (const OEFlexiOverlapResults&)
```

Default and copy constructors.

### operator=

OEFlexiOverlapResults & operator=(const OEFlexiOverlapResults&)

### **GetInternalEnergy**

double GetInternalEnergy() const

Returns the computed internal energy of the conformer.

## 3.1.40 OEFlexiOverlay

#### class OEFlexiOverlay

The OEFlexiOverlay class provides an interface for flexible overlay optimization between the reference molecule and a fit molecule conformers.

The OEFlexiOverlay class defines the following public methods:

- · SetupRef
- Overlay
- · SortedOverlay
- · BestOverlay

#### **Constructor**

```
OEFlexiOverlay();
OEFlexiOverlay (const OEFlexiOverlay&)
```

Default and copy constructors.

#### operator=

```
OEFlexiOverlay & operator=(const OEFlexiOverlay&)
```

# 3.1.41 SetupRef

```
bool SetupRef (const OEChem:: OEMolBase&) ;
bool SetupRef (const OEShape:: OEShapeQueryBase&)
```

This method defines the interface for setting up the reference system for the OEFlexiOverlay using a molecule or a shape query for flexible overlay optimization process.

# 3.1.42 Overlay

OESystem::OEIterBase<OEFlexiOverlapResults>\* Overlay(OEChem::OEMCMolBase&)

This method optimizes the shape and chemical similarity between the fit molecule conformers and a reference molecule, along with intra-molecular forcefield energies of the fit molecule. The reference molecule must be set using Set upRef method.

# 3.1.43 SortedOverlav

```
OESystem:: OEIterBase<OEFlexiOverlapResults>*
→SortedOverlay (OEChem:: OEMCMolBase&)
```

This method optimizes the shape and chemical similarity between the fit molecule conformers and a reference molecule, along with intra-molecular forcefield energies of the fit molecule. The reference molecule must be set using SetupRef method. This method returns an iterator over OEFlexiOverlapResults which are sorted based on the TanimotoCombo similarity of that conformer and the reference molecule.

# 3.1.44 BestOverlay

bool BestOverlay (OEFlexiOverlapResults&, OEChem:: OEMCMolBase&);

This method optimizes the shape and chemical similarity between the fit molecule conformers and a reference molecule, along with intra-molecular forcefield energies of the fit molecule. This method returns the best result only which is the conformer with the highest TanimotoCombo similarity to the reference molecule. The reference molecule must be set using SetupRef method.

# 3.1.45 OEFlexiOverlayOptions

class OEFlexiOverlayOptions : public OESystem: : OEOptions

This class provides an interface to setup options required to perform **flexible fitting** between the fit molecule conformers and a reference molecule using OEFlexiOverlay.

#### See also:

• OEFlexiOverlapOptions class

The OEFlexiOverlayOptions class defines the following public methods:

- · GetMaxOptSteps and SetMaxOptSteps
- · GetRigidOverlay and SetRigidOverlay
- GetFlexiOverlapOptions and SetFlexiOverlapOptions
- GetRigidOverlayOptions and SetRigidOverlayOptions

#### **Constructor**

```
OEFlexiOverlayOptions();
OEFlexiOverlayOptions (const OEFlexiOverlayOptions&)
```

Default and copy constructors.

#### operator=

OEFlexiOverlayOptions & operator=(const OEFlexiOverlayOptions&)

### 3.1.46 GetMaxOptSteps

unsigned GetMaxOptSteps() const

See SetMaxOptSteps method.

# 3.1.47 GetRigidOverlay

bool GetRigidOverlay () const

See SetRigidOverlay method.

## 3.1.48 GetFlexiOverlapOptions

```
OEFlexiOverlapOptions& GetFlexiOverlapOptions()
const OEFlexiOverlapOptions& GetFlexiOverlapOptions () const
```

Returns a reference to the OEFlexiOverlapOptions instance as currently set. These are options related to flexible overlap optimization using shape, color, and force field. See also SetFlexiOverlapOptions method.

## 3.1.49 GetRigidOverlayOptions

```
OEOverlayOptions& GetRigidOverlayOptions()
const OEOverlayOptions& GetRigidOverlayOptions () const
```

Returns a reference to the OEOverlayOptions instance as currently set. These are options related to rigid overlay optimization using shape and color. See also SetRigidOverlayOptions method.

## 3.1.50 SetMaxOptSteps

bool SetMaxOptSteps (const unsigned)

Sets the maximum number of optimization iteration steps in flexible overlay optimization. Default: 2000 steps.

## 3.1.51 SetRigidOverlav

bool SetRigidOverlay (const bool)

This control flag determines whether an initial rigid overlay optimization between the fit molecule conformers and the reference system should be performed prior to flexible optimization. Default: True.

# 3.1.52 SetFlexiOverlapOptions

void SetFlexiOverlapOptions (const OEFlexiOverlapOptions&)

Sets the options related to flexible overlap calculations by passing in OEFlexiOverlapOptions instance.

## 3.1.53 SetRigidOverlayOptions

**void** SetRigidOverlayOptions (const OEOverlayOptions&)

Sets the options related to overlay optimization using shape and color by passing in OEFlexiOverlapOptions instance.

## 3.1.54 OEGridColorFunc

class OEGridColorFunc : public OEShapeFunc

The OEGridColorFunc class defines color overlap between a reference object and a fit molecule, using the Grid method.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupFlex
- · SetupRef

The following methods are publicly inherited from OEColorFunc:

· GetColorOptions

The OEGridColorFunc class defines the following public methods:

![](_page_91_Figure_1.jpeg)

· GetGridOptions

### **Constructors**

```
OEGridColorFunc()
{\tt OEGridColorFunc}({\tt const}~{\tt OEColorOptions} \&)OEGridColorFunc(const OEShapeGridOptions&)
{\tt OEGridColorFunc}({\tt const\ } {\tt OECOlorOptions\&\ } ,\ {\tt const\ } {\tt OSShapeGridOptions\&\ }OEGridColorFunc(const OEGridColorFunc&)
```

### Default and copy constructors.

Constructs an OEGridColorFunc instance using the specified set of parameters.

### operator=

OEGridColorFunc & operator= (const OEGridColorFunc &)

The assignment operator.

### **GetGridOptions**

```
const OEShapeGridOptions& GetGridOptions() const
```

Returns a reference to the OEShapeGridOptions instance as currently set for this OEGridColorFunc.

# 3.1.55 OEGridShapeFunc

```
class OEGridShapeFunc : public OEShapeFunc
```

The OEGridShapeFunc class defines shape overlap between a reference object and a fit molecule, using the Grid method.

![](_page_92_Figure_7.jpeg)

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

### The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEMolFunc:

· GetInteractions

· Setup

#### The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- · SetupFlex
- SetupRef

#### The following methods are publicly inherited from OEShapeFunc:

• GetShapeOptions

The OEGridShapeFunc class defines the following public methods:

· GetGridOptions

### **Constructors**

```
OEGridShapeFunc()
OEGridShapeFunc (const OEShapeOptions )
OEGridShapeFunc(const OEShapeGridOptions&)
OEGridShapeFunc(const OEShapeOptions&, const OEShapeGridOptions&)
OEGridShapeFunc(const OEGridShapeFunc&)
```

Default and copy constructors.

Constructs an OEGridShapeFunc instance using the specified set of parameters.

#### operator=

OEGridShapeFunc & operator= (const OEGridShapeFunc &)

The assignment operator.

### **GetGridOptions**

const OEShapeGridOptions& GetGridOptions() const

Returns a reference to the OEShapeGridOptions instance as currently set for this OEGridShapeFunc.

### 3.1.56 OEHermite

```
class OESHAPE API OEHermite
```

This class performs Hermite expansion for a given molecule or a grid representation of a molecule and returns the coefficients of expansion and creates a grid representation of Hermite shape.

See also:

- Shape from Hermite Representation section
- OEHermiteOptions class
- OEHermiteShapeFunc class

• Shape from Hermite expansion examples

#### **Constructors**

```
OEHermite()
OEHermite (const OEHermite &)
OEHermite (const OEHermiteOptions & HermiteOptions)
```

This class has three constructors. First two are default and copy constructors. The third one is the constructor that takes an option class OEHermiteOptions.

#### operator=

OEHermite & operator= (const OEHermite &)

The assignment operator allows for equating two OEHermite classes which would copy the one on the right into the one on the left.

### 3.1.57 CreateGrid

```
void CreateGrid (OESystem:: OEScalarGrid&, const float)
void CreateGrid (OESystem::OEScalarGrid&, const float, const OEChem::OETrans)
```

This method creates a grid representation of the obtained Hermite expansion. Depending on the grid spacing parameter (scale) the number of grid points to cover the entire molecule will be calculated. If this number exceeds 300 points per space dimension, the user will be warned that instead the maximum allowed value of ngrid=300 will be used. The second overload uses the transform that is applied to transform the generated grid.

### 3.1.58 GetCoefficients

**bool** GetCoefficients(std::vector<**double**> &) const

Returns the values of Hermite expansion coefficients in the form of an STL vector. These are precisely the coefficients  $f_{lmn}$  introduced in *Shape from Hermite Representation* section above in the following order:  $l = 0 \dots$ NPolyMax,  $m = 0 \dots$ NPolyMax -  $l, n = 0 \dots$ NPolyMax -  $l - m$ . One can show that the total number of such possible sets of l, m, n equals to  $\frac{(NPolyMax+1)(NPolyMax+2)(NPolyMax+3)}{6}$ , which is precisely  $\epsilon$ the length of the returned STL vector.

### 3.1.59 GetOptions

const OEHermiteOptions &GetOptions() const

Returns the option class OEHermiteOptions that the OEHermite class is currently using.

### 3.1.60 GetSelfOverlap

double GetSelfOverlap() const

Returns the self-overlap of the molecule corresponding to Hermite expansion.

### 3.1.61 Setup

```
bool Setup (const OEShapeQuery & argQuery)
bool Setup (const OEChem:: OEMolBase &mol)
bool Setup (const OESystem:: OEScalarGrid &grid)
```

This overloaded method allows user to input into the OEHermite class a molecule as a shape query object, a molecule object, or via a grid representation. Method returns True if the setup was successful and False otherwise.

# 3.1.62 OEHermiteOptions

```
class OEHermiteOptions
```

This is an option class for the OEHermite class. It allows the user to input the level of Hermite expansion (NPolyMax), the parameters  $\lambda_x, \lambda_y, \lambda_z$  and whether or not the latter need to be optimized inside the *OEHermite* class.

#### See also:

- Shape from Hermite Representation section
- OEHermite class
- OEHermiteShapeFunc class
- Shape from Hermite expansion examples

### **Constructors**

```
OEHermiteOptions()
OEHermiteOptions (const OEHermiteOptions &)
```

This class has a default constructor and a copy constructor. The default constructor assumes the following parameters NPolyMax = 4,  $\lambda_{x,y,z} = 1.0$ , UseOptimalLambdas = True. The copy constructor as expected copies the option class into the new class.

#### operator=

OEHermiteOptions & operator= (const OEHermiteOptions &)

The assignment operator allows for copying an option class into another option class using the equal sign.

#### **GetLambdaX**

double GetLambdaX() const

Returns the value of  $\lambda_x$  parameter.

#### **GetLambdaY**

double GetLambdaY() const

Returns the value of  $\lambda_y$  parameter.

#### **GetLambdaZ**

double GetLambdaZ() const

Returns the value of  $\lambda_z$  parameter.

#### **GetNPolyMax**

unsigned int GetNPolyMax() const

Returns the value of NPolyMax parameter, which controls the level of Hermite expansion. In particular the lowest value 0 corresponds to a very inaccurate expansion, approximating the entire molecule by a single Gaussian, while the largest currently allowed value is equal to 30, which corresponds to a list of 5456 Hermite coefficients  $f_{l,m,n}$ . In the limit NPolyMax  $\rightarrow \infty$  we obtain exact equivalence of the Hermite expansion to the Gaussian representation of the molecule.

#### **GetUseOptimalLambdas**

**bool** GetUseOptimalLambdas() const

This method returns the value of the parameter UseOptimalLambdas. When this parameter is True, inside the  $Setup$ method, when it is passed a molecule an optimization of  $\lambda_{x,y,z}$  parameters will be performed via maximizing the self-overlap of the molecule at a given resolution of the Hermite expansion. Please note, that even in the case when UseOptimalLambdas is set to False, if the value of NPolyMax is high enough the Hermite expansion will converge to the Gaussian shape. However in practice at a given low resolution of Hermite expansion it is essential to use the optimal  $\lambda_{x,y,z}$  parameters for faster convergence.

Alternatively when UseOptimalLambdas is False, the current values of the  $\lambda_{x,y,z}$  parameters will be used inside the Set up method, without optimization.

### **SetLambdaX**

| <b>void</b> SetLambdaX( <b>double</b> ) |  |
|-----------------------------------------|--|
|-----------------------------------------|--|

Sets the value of  $\lambda_x$  parameter. Default value is 1.0.

#### **SetLambdaY**

void SetLambdaY (double)

Sets the value of  $\lambda_y$  parameter. Default value is 1.0.

### **SetLambdaZ**

void SetLambdaZ (double)

Sets the value of  $\lambda_z$  parameter. Default value is 1.0.

#### **SetNPolyMax**

void SetNPolyMax (unsigned int)

Sets the value of NPolyMax parameter. Default value is 4.

#### **SetUseOptimalLambdas**

void SetUseOptimalLambdas (bool)

Sets the value of UseOptimalLambdas parameter. Default value is True.

## 3.1.63 OEHermiteShapeFunc

class OESHAPE\_API OEHermiteShapeFunc : public OEShapeFunc

This class is derived from OEShapeFunc and is used to approximate Tanimoto shape-similarity coefficient based on Hermite representation of molecules.

See also:

- Shape from Hermite Representation section
- OEHermite class
- OEHermiteOptions class
- Shape from Hermite expansion examples

### The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents

![](_page_98_Figure_1.jpeg)

· NumVar

The following methods are publicly inherited from OEFunc1:

• operator()

The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupRef

The following methods are publicly inherited from OEShapeFunc:

· GetShapeOptions

The OEHermiteShapeFunc class defines the following public methods:

- GetFitHermiteOptions
- GetRefHermiteOptions

#### **Constructors**

```
OEHermiteShapeFunc(const OEHermiteShapeFunc &)
OEHermiteShapeFunc(const OEShapeOptions &argOptions=OEShapeOptions())
OEHermiteShapeFunc(const OEHermiteOptions & HermOptRef,
                   const OEHermiteOptions & HermOptFit)
OEHermiteShapeFunc(const OEShapeOptions &argOptions,
                   const OEHermiteOptions &HermOptRef,
                   const OEHermiteOptions & HermOptFit)
```

The four constructors are in the respective order: a standard copy constructor, a constructor that inputs a OEShapeOptions object, a constructor that inputs two OEHermiteOptions objects, one for reference and one for fit molecules, and finally a constructor that inputs OEShapeOptions object along with two OEHermiteOptions objects, one for reference and one for fit molecules.

#### operator=

OEHermiteShapeFunc & operator= (const OEHermiteShapeFunc &)

The assignment operator.

#### **GetFitHermiteOptions**

const OEHermiteOptions &GetFitHermiteOptions() const

This method returns OEHermiteOptions class currently being used for the fit molecule.

#### **GetRefHermiteOptions**

const OEHermiteOptions &GetRefHermiteOptions() const

This method returns OEHermiteOptions class currently being used for the reference molecule.

## 3.1.64 OEHighestColorTanimoto

```
struct OEHighestColorTanimoto : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→ OEBestOverlayScore>
```

This class represents OEHighestColorTanimoto, predicte to compare OEBestOverlayScore based on color tanimoto.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
  CreateCopy () const
```

## 3.1.65 OEHighestFitColorTversky

```
struct OEHighestFitColorTversky : public OESystem:: OEBinaryPredicate
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
```

This class represents OEHighestFitColorTversky, predicte to compare OEBestOverlayScore based on Fit molecule color Tversky.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
 CreateCopy () const
```

## 3.1.66 OEHighestFitTversky

```
struct OEHighestFitTversky : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→OEBestOverlayScore>
```

This class represents OEHighestFitTversky, predicte to compare OEBestOverlayScore based on Fit molecule shape Tversky.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

#### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore, OEBestOverlayScore, bool> *
 CreateCopy () const
```

# 3.1.67 OEHighestFitTverskyCombo

```
struct OEHighestFitTverskyCombo : public OESystem::OEBinaryPredicate
-<0EBestOverlayScore, OEBestOverlayScore>
```

This class represents OEHighestFitTverskyCombo, predicte to compare OEBestOverlayScore based on Fit molecule shape plus color Tversky.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
               const OEBestOverlayScore &s2) const
```

#### **CreateCopy**

```
OESystem:: OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
  CreateCopy() const
```

## 3.1.68 OEHighestOverlap

```
struct OEHighestOverlap : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→OEBestOverlayScore>
```

This class represents OEHighestOverlap, predicte to compare OEBestOverlayScore based on shape overlap.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
               const OEBestOverlayScore &s2) const
```

### **CreateCopy**

```
OESystem:: OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
 CreateCopy() const
```

## 3.1.69 OEHighestRefColorTversky

```
struct OEHighestRefColorTversky : public OESystem:: OEBinaryPredicate
→<OEBestOverlayScore, OEBestOverlayScore>
```

This class represents OEHighestRefColorTversky, predicte to compare OEBestOverlayScore based on reference molecule color Tversky.

operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

#### **CreateCopy**

```
OESystem:: OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
 CreateCopy() const
```

## 3.1.70 OEHighestRefTversky

```
struct OEHighestRefTversky : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→OEBestOverlayScore>
```

This class represents OEHighestRefTversky, predicte to compare OEBestOverlayScore based on reference molecule shape Tversky.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

#### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
  CreateCopy () const
```

## 3.1.71 OEHighestRefTverskyCombo

```
struct OEHighestRefTverskyCombo : public OESystem:: OEBinaryPredicate
→<OEBestOverlayScore, OEBestOverlayScore>
```

This class represents OEHighestRefTverskyCombo, predicte to compare OEBestOverlayScore based on reference molecule shape plus color Tversky.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
  CreateCopy () const
```

## 3.1.72 OEHighestScaledColor

struct OEHighestScaledColor : public OESystem:: OEBinaryPredicate<OEBestOverlayScore, →OEBestOverlayScore>

This class represents OEHighestScaledColor.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

#### **CreateCopy**

```
OESystem:: OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
 CreateCopy () const
```

### 3.1.73 OEHighestTanimoto

```
struct OEHighestTanimoto : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→OEBestOverlayScore>
```

This class represents OEHighestTanimoto, predicate to compare OEBestOverlayScore based on shape tanimoto.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
               const OEBestOverlayScore &s2) const
```

### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
 CreateCopy () const
```

# 3.1.74 OEHighestTanimotoCombo

```
struct OEHighestTanimotoCombo : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→ OEBestOverlayScore>
```

This class represents OEHighestTanimotoCombo, predicate to compare OEBestOverlayScore based on shape plus color tanimoto.

#### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

#### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
 CreateCopy() const
```

## 3.1.75 OEHighestTverskyCombo

```
class OEHighestTverskyCombo : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→OEBestOverlayScore>
```

This class represents OEHighestTverskyCombo, predicte to compare OEBestOverlayScore based on shape plus color Tversky.

#### **Constructors**

```
OEHighestTverskyCombo (const double)
```

Default constructor. The argument requires the desired alpha value for Tversky calculation.

### operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
  CreateCopy () const
```

# 3.1.76 OEInertialStarts

```
class OEInertialStarts : public OEStarts
```

The OEInertialStarts represents the inertial starts for overlay optimization.

![](_page_105_Figure_4.jpeg)

The following methods are publicly inherited from OEStarts:

- CreateCopy
- · GetNumOfStarts
- GetStarts
- $\bullet$  Setup
- $\bullet$  SetupRef

The OEInertialStarts class defines the following public methods:

- · GetSymmetryThreshold
- SetSymmetryThreshold

### The following classes derive from this class:

- OEAtAtomStarts
- OECartesianStarts
- OEQuatStarts
- OERandomStarts
- OESubrocsStarts

### **Constructors**

```
OEInertialStarts()
OEInertialStarts (const OEInertialStarts&)
```

Default and copy constructors.

#### operator=

OEInertialStarts & operator=(const OEInertialStarts &)

The assignment operator.

### GetSymmetryThreshold

double GetSymmetryThreshold() const

Returns the symmetry threshold value currently set.

#### **SetSymmetryThreshold**

void SetSymmetryThreshold (const double)

Sets the symmetry threshold value to be used to determine symmetry of objects. Default: 0.15.

## 3.1.77 OEIsColorAtomPred

class OEIsColorAtomPred : public OESystem::OEUnaryPredicate<OEChem::OEAtomBase>

This class represents OEIsColorAtomPred.

#### **Constructors**

OEIsColorAtomPred()

Default and copy constructors.

### operator()

bool operator () (const OEChem:: OEAtomBase & atom) const

### **CreateCopy**

OESystem::OEUnaryFunction<OEChem::OEAtomBase, bool> \*CreateCopy() const

# 3.1.78 OEMultiRefOverlay

class OEMultiRefOverlay

Note: With the default settings, the OEMultiRefOverlay optimizes both shape and color.

The OEMultiRefOverlay provides an extension to OEOverlay to enable setting up a multi-conformer molecule as the reference system for overlay optimization between a reference and a fit molecule conformers.

#### The OEMultiRefOverlay class defines the following public methods:

- · BestOverlay
- GetOverlayOptions
- Overlay
- · SetupRef

### **Constructors**

```
OEMultiRefOverlay()
OEMultiRefOverlay (const OEOverlayOptions&)
OEMultiRefOverlay (const OEMultiRefOverlay&)
```

Default and copy constructors.

#### operator=

```
OEMultiRefOverlay & operator=(const OEMultiRefOverlay &)
```

### **BestOverlay**

```
bool BestOverlay (OEBestOverlayScore& score, const OEChem:: OEMCMolBase& fitmol,
const OESystem::OEBinaryPredicate<OEBestOverlayScore, OEBestOverlayScore>& pred)
```

Method optimizes the overlay between the reference object and the fit molecule conformers, and returns the best result. The reference object must be set using the SetupRef method.

### **GetOverlayOptions**

const OEOverlayOptions& GetOverlayOptions() const

Returns a reference to the OEOverlayOptions instance as currently set. This defines options to calculate Overlay.

#### **Overlay**

```
OESystem::OEIterBase<OEBestOverlayResults> *Overlay(const
\rightarrow OEChem:: OEMCMolBase&)
```

Method optimizes the Overlay between the reference molecule and the fit molecule conformers. The reference molecule must be set using the SetupRef method.

### **SetupRef**

bool SetupRef (const OEChem:: OEMCMolBase&)

Method defines the interface for setting up the reference system for the OEMultiRefOverlay instance with a multiconformer molecule.

# 3.1.79 OEOverlapCutoff

class OEOverlapCutoff : public OEOverlayScoreCutoff

The OEOverlapCutoff defines cutoff based on the shape overlap.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator()
- CreateCopy

### **Constructors**

OEOverlapCutoff (const double)

Default and copy constructors. The argument expects the desired cutoff.

## 3.1.80 OEOverlapFunc

```
class OEOverlapFunc : public OEOverlapFuncBase
```

The OEOverlapFunc class defines an interface for combined shape and color overlap calculation between a reference object and a fit molecule. The OEOverlapFunc is a specialization of The OEOverlapFuncBase for combined shape and color overlap.

![](_page_109_Figure_4.jpeg)

#### The following methods are publicly inherited from OEFunc0:

- operator()
- · GetFComponents
- · NumVar

The following methods are publicly inherited from OEFunc1:

• operator ()

The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

### The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- SetupFlex
- SetupRef

The OEOverlapFunc class defines the following public methods:

- · GetColorFunc
- · GetShapeFunc

#### **Constructors**

```
OEOverlapFunc()
OEOverlapFunc (const OEShapeFunc&)
OEOverlapFunc (const OEColorFunc&)
OEOverlapFunc (const OEShapeFunc&, const OEColorFunc&)
OEOverlapFunc(const OEOverlapFunc&)
```

#### Default and copy constructors.

Constructs an OEOverlapFunc instance using the specified set of parameters.

#### operator=

OEOverlapFunc & operator= (const OEOverlapFunc &)

The assignment operator.

# 3.1.81 GetColorFunc

const OEColorFunc& GetColorFunc () const

Returns a reference to the OEColorFunc instance as currently set for this OEOverlapFunc.

### 3.1.82 GetShapeFunc

const OEShapeFunc& GetShapeFunc() const

Returns a reference to the OEShapeFunc instance as currently set for this OEOverlapFunc.

### 3.1.83 OEOverlapFuncBase

class OEOverlapFuncBase : public OEMolPotential:: OEMolFunc1

The OEOverlapFuncBase is an abstract base class. This class defines an interface for static overlap calculation between a reference object and a fit molecule. The OEOverlapFuncBase extends the OEMolFunc1 class to allow setting up a reference object (which could be a molecule, grid or a shape query) and the underlying functions defining interactions based on shape or color overlaps.

The following methods are publicly inherited from OEFunc0:

- operator ()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

![](_page_111_Figure_1.jpeg)

• operator()

### The following methods are publicly inherited from OEMolFunc:

- · GetInteractions
- · Setup

### The OEOverlapFuncBase class defines the following public methods:

- · Overlap
- SetupFlex
- SetupRef

### The following classes derive from this class:

- OEAnalyticColorFunc
- OEAnalyticShapeFunc
- $\bullet$  OEColorFunc
- OEExactColorFunc
- OEExactShapeFunc
- OEGridColorFunc
- OEGridShapeFunc
- $\bullet$  OEOverlapFunc
- OEShapeFunc

### 3.1.84 Overlap

```
bool Overlap (const double* argCoords, OEOverlapResults &)
bool Overlap (const OEChem:: OEMolBase & argFitMol, OEOverlapResults &)
```

These methods calculate the overlap between the reference object and the fit molecule. The reference object must be set using the  $SetupRef$  method. The first overload assumes that the fit molecule has been set using the Setup method and uses the specified coordinates for the fit molecule. The second overlap takes the specified fit molecule and its current coordinates.

### 3.1.85 SetupFlex

```
bool SetupFlex (const OEChem:: OEMolBase&)
```

This method is a substitute for the Set up method to setup the fit molecule. This method should be called instead of the Setup, when the fit molecule is expected to be flexible and that the shape of the molecule is expected to change.

# 3.1.86 SetupRef

```
bool SetupRef (const OEChem:: OEMolBase&)
bool SetupRef (const OESystem:: OEScalarGrid&)
bool SetupRef (const OEShapeQuery&)
```

These method defines the interface for setting up the reference system for the OEOverlapFuncBase derived instance with a molecule, grid or a shape query.

## 3.1.87 OEOverlapPrep

#### class OEOverlapPrep

This class provides facilities to prepare molecules for overlap calculations. Preparing a molecule for overlap calculation consists of any or all of the following: adding or removing explicit hydrogens; adding color atoms; and assigning Bondi radii to all the atoms. When color atoms are added to molecules for overlap calculations, it is often required to remove them before further modeling work involving those molecules. Color atoms from molecules can be removed using the OERemoveColorAtoms function.

#### The OEOverlapPrep class defines the following public methods:

- GetAssignBondiRadii
- GetAssignColor
- · GetColorForceField
- · GetUseHydrogens
- $•$  Prep
- · SetAssignBondiRadii
- SetAssignColor
- · SetColorForceField
- · SetUseHydrogens

### **Constructors**

```
OEOverlapPrep()
OEOverlapPrep (const OEOverlapPrepOptions&)
OEOverlapPrep (const OEOverlapPrep&)
```

Default and copy constructors.

#### operator=

```
OEOverlapPrep & operator=(const OEOverlapPrep &)
```

#### **GetAssignBondiRadii**

bool GetAssignBondiRadii() const

Returns the state of the assign Bondi radii flag. If true, Bondi radii would be assigned to all atoms during the  $Prep$ .

#### **GetAssignColor**

bool GetAssignColor() const

Returns the state of the assign color flag. If true, color atoms would be assigned during the  $Prep$ .

#### **GetColorForceField**

const OEColorForceField& GetColorForceField() const

Gets the instance of *OEColorForceField* currently associated with the *OEOverlapPrep*.

#### **GetUseHydrogens**

```
bool GetUseHydrogens () const
```

Returns the state of the use hydrogens flag. If true, explicit hydrogen atoms would be created during the  $Prep$ . If false, all hydrogen atoms would be removed.

#### **Prep**

```
bool Prep (OEChem:: OEMCMolBase&);
bool Prep (OEChem:: OEMolBase&);
```

Prepares the specified molecule for overlap calculation based on the current set of options set on  $Prep$ .

#### **SetAssignBondiRadii**

```
void SetAssignBondiRadii (const bool)
```

Sets the state of the assign Bondi radii flag. If true, Bondi radii would be assigned to all atoms during the  $Prep$ .

#### **SetAssignColor**

void SetAssignColor (const bool)

Sets the state of the assign color flag. If true, color atoms would be assigned during the Prep. Color atoms from molecules can be removed using the OERemoveColorAtoms function for further modeling work involving a molecule.

#### **SetColorForceField**

**bool** SetColorForceField(const OEColorForceField &cff)

Sets the color force field to be used. By default, the ImplicitMillsDean color force field is used.

### SetUseHydrogens

void SetUseHydrogens (const bool)

Sets the state of the use hydrogens flag. If true, explicit hydrogen atoms would be created during the  $Prep$ . If false, all hydrogen atoms would be removed.

### 3.1.88 OEOverlapPrepOptions

class OEOverlapPrepOptions : public OESystem: : OEOptions

This class provides an interface to set up options required for OEOverlapPrep. In addition to preparing options available in OEOverlapPrep, this option class provides two more additional options to control the Prep process regarding the removal of color atoms which are closer than a threshold distance.

The OEOverlapPrepOptions class defines the following public methods:

- · GetAssignBondiRadii and SetAssignBondiRadii
- · GetAssignColor and SetAssignColor
- · GetDuplicateDistance and SetDuplicateDistance
- · GetRemoveDuplicate and SetRemoveDuplicate
- · GetUseHydrogens and SetUseHydrogens
- · GetColorForceField and SetColorForceField

#### **Constructor**

```
OEOverlapPrepOptions();
OEOverlapPrepOptions (const OEOverlapPrepOptions&)
```

Default and copy constructors.

#### operator=

OEOverlapPrepOptions & operator=(const OEOverlapPrepOptions&)

#### **GetAssignBondiRadii**

unsigned GetAssignBondiRadii() const

Returns the state of the assign Bondi radii flag. If true, Bondi radii would be assigned to all atoms during the  $Prep$ .

#### **GetAssignColor**

unsigned GetAssignColor() const

Returns the state of the assign color flag. If true, color atoms would be assigned during the  $Prep$ .

#### **GetDuplicateDistance**

float GetDuplicateDistance() const

Returns the threshold distance for duplicate removal of color atoms.

#### **GetRemoveDuplicate**

bool GetRemoveDuplicate() const

Returns the state of the remove duplicate flag. If true, color atoms would be removed if their distance is less than the threshold distance for duplicate removal during the Prep.

#### **GetUseHydrogens**

```
bool GetUseHydrogens () const
```

Returns the state of the use hydrogens flag. If true, explicit hydrogen atoms would be created during the Prep. If false, all hydrogen atoms would be removed.

### **GetColorForceField**

const OEColorForceField& GetColorForceField() const

Gets the instance of OEColorForceField currently associated with the OEOverlapPrep.

#### **SetAssignBondiRadii**

void SetAssignBondiRadii (const bool)

Sets the state of the assign Bondi radii flag. If true, Bondi radii would be assigned to all atoms during the  $Prep$ . Default False.

#### **SetAssignColor**

void SetAssignColor (const bool)

Sets the state of the assign color flag. If true, color atoms would be assigned during the Prep. Color atoms from molecules can be removed using the OERemoveColorAtoms function for further modeling work involving a molecule. Default True.

### **SetDuplicateDistance**

void SetDuplicateDistance (const float)

Sets the threshold distance for duplicate removal of color atoms. The acceptable range is between  $0$  and  $1$ . Default  $0.001.$ 

#### **SetRemoveDuplicate**

void SetRemoveDuplicate (const bool)

Sets the state of the remove duplicate flag. Default False.

#### SetUseHydrogens

void SetUseHydrogens (const bool)

Sets the state of the use hydrogens flag. If true, explicit hydrogen atoms would be created during the  $Prep$ . If false, all hydrogen atoms would be removed. Default False.

### **SetColorForceField**

void SetColorForceField(const OEColorForceField&)

Sets the color force field to be used. By default, the *ImplicitMillsDean* color force field is used.

## 3.1.89 OEOverlapResults

#### struct OEOverlapResults

This class represents overlap calculation results between a reference and a fit object.

The OEOverlapResults class defines the following public methods:

- · GetColorScore
- · GetColorTanimoto
- · GetColorTversky
- · GetFitColorTversky
- · GetFitSelfColor
- · GetFitSelfOverlap
- · GetFitTversky
- · GetFitTverskyCombo
- GetOverlap
- GetRefColorTversky
- GetRefSelfColor
- GetRefSelfOverlap
- GetRefTversky
- · GetRefTverskyCombo
- GetTanimoto
- · GetTanimotoCombo
- GetTversky

#### **Constructors**

```
OEOverlapResults()
OEOverlapResults (const OEOverlapResults&)
```

Default and copy constructors.

#### operator=

OEOverlapResults & operator= (const OEOverlapResults &)

### **GetColorScore**

float GetColorScore() const

Returns the color score (overlap) between the reference and the fit.

### **GetColorTanimoto**

float GetColorTanimoto() const

Returns the color tanimoto.

#### **GetColorTversky**

float GetColorTversky (float alpha =  $0.95f$ , float beta =  $0.05f$ ) const

Returns the color tversky with the specified alpha and beta.

### **GetFitColorTversky**

float GetFitColorTversky() const

Returns the color tversky with beta =  $0.95$ .

### **GetFitSelfColor**

float GetFitSelfColor() const

Returns the self color score for the fit molecule.

#### **GetFitSelfOverlap**

float GetFitSelfOverlap() const

Returns the self shape overlap for the fit molecule.

### **GetFitTversky**

```
float GetFitTversky() const
```

Returns the shape tversky with beta  $= 0.95$ .

### **GetFitTverskyCombo**

float GetFitTverskyCombo() const

Returns the sum of shape tversky with beta =  $0.95$ , and the color tversky with beta =  $0.95$ .

#### **GetOverlap**

float GetOverlap () const

Returns the shape overlap between the reference and the fit.

### **GetRefColorTversky**

```
float GetRefColorTversky() const
```

```
Returns the color tversky with alpha = 0.95.
```

### **GetRefSelfColor**

```
float GetRefSelfColor() const
```

Returns the self color score for the reference object.

### **GetRefSelfOverlap**

float GetRefSelfOverlap() const

Returns the self shape overlap for the reference object.

### **GetRefTversky**

float GetRefTversky() const

Returns the shape tversky with  $alpha = 0.95$ .

### **GetRefTverskyCombo**

float GetRefTverskyCombo() const

Returns the sum of shape tversky with alpha = 0.95, and color tversky with alpha =  $0.95$ .

#### **GetTanimoto**

float GetTanimoto() const

Returns the shape tanimoto.

### **GetTanimotoCombo**

float GetTanimotoCombo() const

Returns the sum of shape tanimoto and color tanimoto.

#### **GetTversky**

float GetTversky (float alpha=0.95f, float beta=0.05f) const

Returns the shape tversky with the specified alpha and beta.

## 3.1.90 OEOverlay

class OEOverlay

Note: With the default settings, the OEOverlay optimizes both shape and color.

The OEOverlay defined an interface for overlap optimization between a reference object (a molecule, grid or a shape query) and a fit molecule conformers.

The OEOverlay class defines the following public methods:

- · BestOverlay
- · GetOverlayOptions
- Overlay
- SetupRef
- · SortedOverlay

### **Constructors**

```
OEOverlay()
OEOverlay (const OEOverlayOptions&)
OEOverlay (const OEOverlay&)
```

Default and copy constructors.

#### operator=

```
OEOverlay & operator= (const OEOverlay &)
```

# 3.1.91 BestOverlay

```
bool BestOverlay (OEBestOverlayScore& score, const OEChem:: OEMCMolBase&
\rightarrowfitmol,
const OESystem::OEBinaryPredicate<OEBestOverlayScore, OEBestOverlayScore>&
\rightarrowpred)
```

Method optimizes the overlay between the reference object and the fit molecule conformers, and returns the best result, sorted based on the binary predicate pred. The predicate has a default setting of OEHighestTanimotoCombo. The reference object must be set using the  $SetupRef$  method, prior to calling this method.

## 3.1.92 GetOverlayOptions

const OEOverlayOptions& GetOverlayOptions() const

Returns a reference to the OEOverlayOptions instance as currently set. This defines options to calculate overlay.

## 3.1.93 Overlay

```
OESystem::OEIterBase<OEBestOverlayResults> *Overlay(const
\rightarrow OEChem:: OEMCMolBase&)
```

Method optimizes the overlay between the reference object and the fit molecule conformers. The reference object must be set using the  $SetuppRef$  method, prior to calling this method.

See also:

- · BestOverlay
- · SortedOverlay

## 3.1.94 SetupRef

```
bool SetupRef (const OEChem:: OEMolBase&)
bool SetupRef (const OESystem:: OEScalarGrid&)
bool SetupRef (const OEShapeQuery&)
```

These method defines the interface for setting up the reference system for the *OEOverlay* instance with a molecule, grid or a shape query.

# 3.1.95 SortedOverlay

```
OESystem:: OEIterBase<OEBestOverlayScore>* SortedOverlay(
    const OEChem:: OEMCMolBase& fitmol, const unsigned maxHits,
    const OESystem:: OEBinaryPredicate<OEBestOverlayScore, OEBestOverlayScore>
→& pred)
```

Method optimizes the overlay between the reference object and the fit molecule conformers, and returns the desired number of top hits defined by maxHits, sorted based on the binary predicate pred. The predicate has a default setting of *OEHighestTanimotoCombo*. The reference object must be set using the Set upRef method, prior to calling this method.

This method is specifically preferred over the  $\sqrt{O(\pi L)}$  method when working with molecules containing a large number of conformers, as the burden to store all the results associated with all the conformers can stress the memory limits of a machine.

# 3.1.96 OEOverlayOptions

class OEOverlayOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for OEOverlay.

The OEOverlayOptions class defines the following public methods:

- GetColorFuncType and SetColorFuncType
- · GetColorOptions and SetColorOptions
- · GetMaxOptSteps and SetMaxOptSteps
- · GetOverlapFuncand SetOverlapFunc
- GetShapeFuncType and SetShapeFuncType
- GetShapeOptions and SetShapeOptions
- · GetStarts and SetStarts

### **Constructors**

```
OEOverlayOptions()
OEOverlayOptions (const OEOverlayOptions&)
```

Default and copy constructors.

#### operator=

OEOverlayOptions & operator= (const OEOverlayOptions &)

# 3.1.97 GetColorFuncType

unsigned GetColorFuncType() const

See SetColorFuncType method.

# 3.1.98 GetColorOptions

```
OEColorOptions& GetColorOptions()
const OEColorOptions& GetColorOptions() const
```

See SetColorOptions method.

# 3.1.99 GetMaxOptSteps

unsigned GetMaxOptSteps() const

See SetMaxOptSteps method.

# 3.1.100 GetOverlapFunc

const OEOverlapFuncBase& GetOverlapFunc() const

See SetOverlapFunc method.

# 3.1.101 GetShapeFuncType

unsigned GetShapeFuncType() const

See Set ShapeFuncType method.

# 3.1.102 GetShapeOptions

```
OEShapeOptions& GetShapeOptions()
const OEShapeOptions& GetShapeOptions() const
```

See SetShapeOptions method.

# 3.1.103 GetStarts

const OEStarts& GetStarts() const

See SetStarts method.

# 3.1.104 SetColorFuncType

bool SetColorFuncType (const unsigned)

Set the type of color func to be used for estimating color scores, as defined in the  $OEColorType$ namespace. Default: OEColorType\_Exact.

# 3.1.105 SetColorOptions

**bool** SetColorOptions (const OEColorOptions&)

Sets *options* related to color functions used.

# 3.1.106 SetMaxOptSteps

bool SetMaxOptSteps (const unsigned int)

Set the maximum number of optimization iteration steps. Default: 200

# 3.1.107 SetOverlapFunc

void SetOverlapFunc (const OEOverlapFuncBase&)

Set the overlap function by by passing in an OEOverlapFuncBase instance. This defines the shape/color interactions to be optimized for overlay.

## 3.1.108 SetShapeFuncType

bool SetShapeFuncType (const unsigned)

Set the type of shape func to be used for estimating shape overlap, as defined in the  $OEShapeType$ namespace. Default: OEShapeType\_Grid.

# 3.1.109 SetShapeOptions

```
bool SetShapeOptions (const OEShapeOptions&)
```

Sets *options* related to shape functions used.

# 3.1.110 SetStarts

void SetStarts (const OEStarts&)

Set the starts by by passing in an OEStarts instance. This defines the starts to be used for optimization.

# 3.1.111 OEOverlayScoreCutoff

class OEOverlayScoreCutoff : public OESystem::OEUnaryPredicate<OEBestOverlayScore>

The OEOverlayScoreCutoff is an abstract base class. This class defines an interface specifying cutoff criteria for finding OEROCS hits.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The OEOverlayScoreCutoff class defines the following public methods:

- operator()
- CreateCopy

#### operator()

bool operator () (const OEBestOverlayScore&) const

Method returns True if the specified score satisfies the cutoff criteria.

### **CreateCopy**

OESystem::OEUnaryFunction<OEBestOverlayScore, bool>\* CreateCopy() const

Returns a new copied instance of this unary function.

# 3.1.112 OEQuatStarts

class OEQuatStarts : public OEInertialStarts

The OEQuatStarts represents the user defined quaternion starts for overlay optimization. The OEQuatStarts takes the user defined quaternions as the starts, with reference to the inertial frame of the reference system.

The following methods are publicly inherited from OEStarts:

- CreateCopy
- · GetNumOfStarts
- · GetStarts
- · Setup
- SetupRef

The following methods are publicly inherited from OEInertialStarts:

- · GetSymmetryThreshold
- · SetSymmetryThreshold

The OEQuatStarts class defines the following public methods:

- ClearStarts
- · SetStarts

### **Constructors**

```
OEQuatStarts()
OEQuatStarts (const OEQuatStarts&)
```

Default and copy constructors.

#### operator=

```
OEQuatStarts & operator= (const OEQuatStarts &)
```

The assignment operator.

### **ClearStarts**

void ClearStarts()

Clears the currently specified starts.

### **SetStarts**

void SetStarts (const double \*Quats, unsigned int NumQuats)

Sets the starting quaternions. Method expects an array of size 7\*NumQuats for the first argument.

# 3.1.113 OERefColorTverskyCutoff

class OERefColorTverskyCutoff : public OEOverlayScoreCutoff

The OERefColorTverskyCutoff defines cutoff based on the reference system color tversky.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator ()
- CreateCopy

#### **Constructors**

OERefColorTverskyCutoff(const double)

Default and copy constructors. The argument expects the desired cutoff.

# 3.1.114 OERefTverskyComboCutoff

class OERefTverskyComboCutoff : public OEOverlayScoreCutoff

The OERefTverskyComboCutoff defines cutoff based on the reference system combined shape and color tversky.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator ()
- CreateCopy

### **Constructors**

OERefTverskyComboCutoff(const double)

Default and copy constructors. The argument expects the desired cutoff.

### 3.1.115 OERefTverskyCutoff

class OERefTverskyCutoff : public OEOverlayScoreCutoff

The OERefTverskyCutoff defines cutoff based on the reference system shape tversky.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator()
- CreateCopy

#### **Constructors**

OERefTverskyCutoff (const double)

Default and copy constructors. The argument expects the desired cutoff.

### 3.1.116 OERandomStarts

class OERandomStarts : public OEInertialStarts

The OERandomStarts represents the random starts for overlay optimization. The OERandomStarts translates the fit molecule to specified number of random starting points, followed by the inertial rotations to generate starts.

#### The following methods are publicly inherited from OEStarts:

- CreateCopy
- · GetNumOfStarts
- · GetStarts
- $Set up$
- SetupRef

The following methods are publicly inherited from OEInertialStarts:

- · GetSymmetryThreshold
- · SetSymmetryThreshold

#### The OERandomStarts class defines the following public methods:

- · GetMaxRandomTranslation
- · GetNumRandomStarts
- GetRandomSeed

- · SetMaxRandomTranslation
- · SetNumRandomStarts
- · SetRandomSeed

#### **Constructors**

```
OERandomStarts()
OERandomStarts (const OERandomStarts&)
```

Default and copy constructors.

#### operator=

OERandomStarts & operator=(const OERandomStarts &)

The assignment operator.

#### **GetMaxRandomTranslation**

double GetMaxRandomTranslation() const

Returns the maximum allowed translation value currently set.

#### **GetNumRandomStarts**

unsigned int GetNumRandomStarts() const

Returns the current value of the number of random starting points.

### **GetRandomSeed**

unsigned int GetRandomSeed() const

Returns the current value of the seed for random number generation.

#### **SetMaxRandomTranslation**

void SetMaxRandomTranslation (const double)

Sets the maximum allowed translation for generating the starting points. Default: 2.0.

### **SetNumRandomStarts**

unsigned int GetNumRandomStarts (const unsigned int num) const

Sets the number of random starting points to be generated. Default: 4.

### **SetRandomSeed**

unsigned int SetRandomSeed (const unsigned int seed) const

Sets the seed for random number generation. Default: 0.

# 3.1.117 OEROCS

class OEROCS

The OEROCS defines an interface for finding ROCS hits from a search database, by overlaying a reference object (a molecule, grid or a shape query).

#### The OEROCS class defines the following public methods:

- · AddMolecule
- · ClearMolecules
- · GetROCSOptions
- SetDatabase
- · Overlay

### **Constructors**

```
OEROCS()
OEROCS (const OEROCSOptions&)
OEROCS (const OEROCS&)
```

Default and copy constructors.

#### operator=

OEROCS & operator=(const OEROCS &)

### **AddMolecule**

unsigned int AddMolecule (const OEChem:: OEMCMolBase& argMol)

Adds a copy of the specified molecule to the search database. Returns the index of the molecule in the search database.

#### **ClearMolecules**

| <b>void</b> ClearMolecules() |  |  |  |  |
|------------------------------|--|--|--|--|
|------------------------------|--|--|--|--|

Remove all molecules and clear the search database.

#### **GetROCSOptions**

const OEROCSOptions& GetROCSOptions () const

Returns a reference to the OEROCSOptions instance as currently set. This defines options to perform OEROCS calculations.

### **SetDatabase**

```
bool SetDatabase (const OEChem:: OEMolDatabase&)
bool SetDatabase (OEChem:: oemolistream&)
```

Sets the search database with molecules from specified database or file stream. These methods cleans up any previous existing content of the search database.

### **Overlay**

```
OESystem:: OEIterBase<OEROCSResult>* Overlay(const OEChem:: OEMolBase&);
OESystem::OEIterBase<OEROCSResult>* Overlay(const OEChem::OEMCMolBase&);
{\tt OESystem::OEffectBase < OEROCSResult >\star\ Overlay\ (const\ OESystem::OEScalarGrid\&)\ }; }OESystem:: OEIterBase<OEROCSResult>* Overlay(const OEShapeQuery&);
```

Method optimizes the overlay between the reference object and the molecule conformers in the search database.

## 3.1.118 OEROCSOptions

class OEROCSOptions : public OESystem: : OEOptions

This class provides an interface to setup options required for OEROCS.

The OEROCSOptions class defines the following public methods:

- · AddCutoff
- · ClearCutoffs
- GetConfsPerHit
- GetMaxHits
- · GetNumBestHits
- GetOverlayOptions
- GetPerformPrep
- · GetRankPredicate
- · GetUseMaxHits
- · HasCutoff
- · MeetsCutoff
- SetConfsPerHit
- SetMaxHits
- SetNumBestHits
- SetOverlayOptions
- SetPerformPrep
- SetRankPredicate
- SetUseMaxHits

#### **Constructors**

```
OEROCSOptions()
OEROCSOptions (const OEROCSOptions&)
```

Default and copy constructors.

#### operator=

OEROCSOptions & operator= (const OEROCSOptions &)

### **AddCutoff**

void AddCutoff (const OESystem:: OEUnaryPredicate<OEBestOverlayScore>&)

Add a new cutoff criteria for scanning if a hit is acceptable. Multiple cutoff criteria can used for a single OEROCS calculation.

### **ClearCutoffs**

```
void ClearCutoffs()
```

Remove all currently defined cutoffs.

#### **GetConfsPerHit**

unsigned int GetConfsPerHit() const

Returns the current value for the desired number of conformers to be kept per hit in the OEROCSResult in a OEROCS calculation.

#### **GetMaxHits**

unsigned int GetMaxHits() const

Returns the current value of the maximum number of hits to be looked for in a OEROCS calculation, based on cutoffs.

#### **GetNumBestHits**

unsigned int GetNumBestHits() const

Returns the current value of the maximum number of best hit results to be returned from a OEROCS calculation.

### **GetOverlayOptions**

const OEOverlayOptions& GetOverlayOptions() const

Returns an instance of the OEOverlayOptions as currently set for overlay optimization. These options are used in overlay optimization of conformers.

### **GetPerformPrep**

bool GetPerformPrep() const

Returns the current state of the perform prep flag. This flag defines if the reference and fit molecules should be prepared (or used as is), before *OEROCS* calculations.

### **GetRankPredicate**

```
const OESystem::OEBinaryPredicate<OEBestOverlayScore, OEBestOverlayScore>&
→GetRankPredicate() const
```

Returns an instance of the binary predicate as currently set for ranking the obtained hits.

#### **GetUseMaxHits**

bool GetUseMaxHits() const

Returns the current state of the use max hits flag. This flag defines if a OEROCS calculation should be terminated when the defined maximum hits is reached.

### **HasCutoff**

bool HasCutoff () const

Returns True if any cutoffs are currently set, False otherwise.

### **MeetsCutoff**

bool MeetsCutoff (const OEBestOverlayScore&) const

Returns True if the specified score meets the cutoffs criterion currently set, False otherwise.

### **SetConfsPerHit**

bool SetConfsPerHit (const unsigned int)

Sets the value for the desired number of conformers to be kept per hit in the OEROCSResult in a OEROCS calculation. Default: 1.

### **SetMaxHits**

bool SetMaxHits (const unsigned int)

Sets the value of the maximum number of hits to be looked for in a OEROCS calculation, based on cutoffs. Default: 500.

#### **SetNumBestHits**

bool SetNumBestHits (const unsigned int)

Sets the value of the maximum number of best hit results to be returned from a OEROCS calculation. Default: 500.

#### **SetOverlayOptions**

**void** SetOverlayOptions (const OEOverlayOptions&)

Sets the OEOverlayOptions for overlay optimization. These options are used in overlay optimization of conformers.

#### **SetPerformPrep**

bool SetPerformPrep(const bool)

Sets the state of the perform prep flag. This flag defines if the reference and fit molecules should be prepared (or used as is), before OEROCS calculations. Default: True.

#### **SetRankPredicate**

```
void SetRankPredicate(const OESystem::OEBinaryPredicate<OEBestOverlayScore,
\rightarrowOEBestOverlayScore>&)
```

Sets the binary predicate to be used for ranking the obtained hits.

### **SetUseMaxHits**

bool SetUseMaxHits (const bool)

Sets the state of the use max hits flag. This flag defines if a OEROCS calculation should be terminated when the defined maximum hits is reached. Default: False.

# 3.1.119 OEROCSResult

class OEROCSResult : public OEOverlapResults

This class extends the OEBestOverlayScore to represent the results of a single OEROCS calculation.

The following methods are publicly inherited from OEOverlapResults:

- · GetColorScore
- · GetColorTanimoto
- · GetColorTversky
- · GetFitColorTversky
- · GetFitSelfColor
- GetFitSelfOverlap
- · GetFitTversky
- · GetFitTverskyCombo
- · GetOverlap
- · GetRefColorTversky
- GetRefSelfColor
- GetRefSelfOverlap
- GetRefTversky
- · GetRefTverskyCombo
- GetTanimoto
- · GetTanimotoCombo
- GetTversky

#### The following methods are publicly inherited from OEBestOverlayScore:

- · GetFitConfIdx
- · GetRefConfIdx
- GetRotMatrix
- GetTranslation
- Transform

### The OEROCSResult class defines the following public methods:

- · AddScore
- · GetOverlayConf
- · GetOverlayConfs

### **Constructors**

```
OEROCSResult()
OEROCSResult (const OEBestOverlayScore&, const OEChem::OEMCMolBase&);
OEROCSResult (const OEROCSResult&)
```

Default and copy constructors. The second constructor takes in an instance of a OEBestOverlayScore and the corresponding fit molecule.

#### operator=

```
OEROCSResult & operator= (const OEROCSResult &)
```

### **AddScore**

void AddScore (const OEBestOverlayScore&, const OEChem:: OEMCMolBase&)

Add a new conformer to the score. This method is useful for generating a multi-conformer OEROCSResult.

#### **GetOverlayConf**

const OEChem:: OEMolBase& GetOverlayConf() const

Returns the best hit conformer in the overlaid state.

### **GetOverlayConfs**

const OEChem:: OEMCMolBase& GetOverlayConfs() const

Returns the best hit conformers in the overlaid state, for a multi-conformer result.

### 3.1.120 OEShapeFunc

class OEShapeFunc : public OEOverlapFuncBase

The OEShapeFunc is an abstract base class. This class defines an interface for shape overlap calculation between a reference object and a fit molecule. The OEShapeFunc is a specialization of The OEOverlapFuncBase for shape only overlap.

The following methods are publicly inherited from OEFunc0:

- · operator()
- · GetFComponents
- NumVar

The following methods are publicly inherited from OEFunc1:

· operator()

The following methods are publicly inherited from OEMolFunc:

![](_page_138_Figure_1.jpeg)

- $\bullet$  GetInteractions
- · Setup

### The following methods are publicly inherited from OEOverlapFuncBase:

- · Overlap
- · SetupFlex
- SetupRef

### The OEShapeFunc class defines the following public methods:

• GetShapeOptions

### The following classes derive from this class:

- OEAnalyticShapeFunc
- OEExactShapeFunc
- OEGridShapeFunc

### **GetShapeOptions**

const OEShapeOptions& GetShapeOptions() const

Returns a reference to the OEShapeOptions instance as currently set for this OEShapeFunc.

# 3.1.121 OEShapeGridOptions

class OEShapeGridOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for calculations using the Grid method.

#### The OEShapeGridOptions class defines the following public methods:

- · GetDerivativeType
- · GetGridSpacing
- SetDerivativeType
- · SetGridSpacing

#### **Constructors**

```
OEShapeGridOptions()
OEShapeGridOptions (const OEShapeGridOptions&)
```

Default and copy constructors.

#### operator=

OEShapeGridOptions & operator=(const OEShapeGridOptions &)

#### **GetDerivativeType**

unsigned int GetDerivativeType() const

Gets the current value of the derivative type to be used on *Grid* method.

### **GetGridSpacing**

double GetGridSpacing() const

Gets the grid spacing to be used on Grid method.

#### **SetDerivativeType**

bool SetDerivativeType(const unsigned int)

Set the derivative type to be used  $\Omega$ Grid method. The default is OEDerivativeType\_NearestValue for shape overlap and OEDerivativeType\_Interpolated for color overlap. Alternatives are defined in the OEDerivativeType namespace.

#### **SetGridSpacing**

bool SetGridSpacing (const double)

Set the grid spacing to be used on *Grid* method. By default this is set to 0.25 Å.

### 3.1.122 OEShapeOptions

class OEShapeOptions : public OESystem:: OEOptions

This class provides an interface to setup options required for OEShapeFunc calculations.

The OEShapeOptions class defines the following public methods:

- · GetCarbonRadius
- · GetRadiiApproximation
- GetScoreType
- · SetCarbonRadius
- · SetRadiiApproximation
- SetScoreType

### **Constructors**

```
OEShapeOptions()
OEShapeOptions (const OEShapeOptions&)
```

Default and copy constructors.

#### operator=

OEShapeOptions & operator= (const OEShapeOptions &)

### **GetCarbonRadius**

double GetCarbonRadius() const

Gets the radius value for the carbon radius approximation, associated with OEOverlapRadii\_Carbon.

#### **GetRadiiApproximation**

unsigned int GetRadiiApproximation() const

Gets the current value of the radii approximation.

#### **GetScoreType**

unsigned int GetScoreType() const

Gets the current value of the score type of the function.

### **SetCarbonRadius**

**bool** SetCarbonRadius (double cradius)

Set the radius to use when using  $OEOverlapRadi\_Carbon$ . By default this is set to 1.7 Å.

### **SetRadiiApproximation**

**bool** SetRadiiApproximation (unsigned int type)

Set the radius approximation used to calculate overlap. The default is OEOverlapRadii\_Carbon. Alternatives are defined in the OEOverlapRadii namespace.

### **SetScoreType**

```
bool SetScoreType (unsigned int type)
```

Set the score type to be reported by this function. The default is  $OEScoreType\_Tanimoto$ . Alternatives are defined in the OEScoreType namespace.

# 3.1.123 OEStarts

```
class OEStarts
```

The OEStarts is an abstract base class. This class defines an interface for providing various kinds of Starts for overlay optimization calculations. Most methods in this interface are useful for advanced users that wants to create their own optimization workflow using these starts. For specifying starts for OEOverlay or OEROCS calculations, users merely needs to instantiate the appropriate OEStarts.

![](_page_142_Figure_7.jpeg)

### The OEStarts class defines the following public methods:

- CreateCopy
- GetNumOfStarts
- · GetStarts
- $\bullet$  Setup
- SetupRef

### The following classes derive from this class:

- OEAsIsStarts
- OEAtAtomStarts

- OECartesianStarts
- OEInertialStarts
- OEQuatStarts
- OERandomStarts
- OESubrocsStarts

#### **CreateCopy**

OEStarts\* CreateCopy() const

Returns a new instance of an *OEStarts* with the same parameters as the inherent starts.

#### **GetNumOfStarts**

unsigned int GetNumOfStarts() const

Returns the number of starts currently set. In most cases, the number of starts depends on the reference and the fit object to be used for optimization. Both  $Setupp \in and Setup$  should be called to setup the reference and fit information prior to accessing the number of starts for any specific optimization.

#### **GetStarts**

bool GetStarts (double\* argQuats) const

Returns the starting quaternions currently set. In most cases, the number of starts depends on the reference and the fit object to be used for optimization. Both  $Setupp \in and Setup$  should be called to setup the reference and fit information prior to accessing the number of starts for any specific optimization.

The array passed in for obtaining the starting quaternions must have a length of art least  $7*(\text{NumStarts})$ .

#### **Setup**

unsigned int Setup (const OEChem:: OEMolBase& argFitMol, OEChem:: OETrans& argTrans)

This method defines the interface for setting up the fit system for the OEStarts derived instance with a molecule. The second argument returns the transformation required to be applied on the fit molecule prior to starting any optimization. The return value of the method corresponds to the calculated symmetry type of the fit molecule. The reference system information must be set by calling  $SetuppRef$  prior to calling Setup.

**SetupRef** 

```
bool SetupRef (const unsigned int symmetry)
bool SetupRef (const OEChem:: OEMolBase& argRefMol, const unsigned int symmetry)
```

These methods define the interface for setting up the reference system for the OEStarts derived instance. The knowledge of the reference molecule is required for some variants of the OEStarts, whereas the others just require the symmetry information for the reference system. The corresponding symmetry values are defined in the OEMoment Symmetry namespace, and can be calculated using the OEOrientByMoment sOfInertia method.

## 3.1.124 OEShapeQuery

```
class OEShapeQuery : public OEShapeQueryBase
```

The OEShapeQuery class defines an interface for creating a shape query, useful for defining a reference system for shape/color overlap calculations.

The following methods are publicly inherited from OEBase:

- operator=
- $\bullet$  operator+=
- · AddBaseData
- · AddData
- CreateCopy
- · DeleteData
- · GetBoolData
- · GetData
- · GetDataIter
- · GetDataType
- · GetDoubleData
- · GetFloatData
- · GetIntData
- · GetStringData
- · HasData
- · IsDataType
- · SetBaseData
- · SetBoolData
- · SetData
- · SetDoubleData
- · SetFloatData
- · SetIntData
- · SetStringData

#### The following methods are publicly inherited from OEShapeQueryBase:

- · GetAtomStrength
- · GetColorForceField
- · GetColorGaussians
- · GetCompositeMolecule
- GetMolecule
- · GetShapeGaussians
- GetShapeGrid
- $\bullet$  GetTitle
- · HasColor
- · HasMolecule
- · HasShape
- · HasShapeGrid
- $\bullet$  IsEmpty
- $\bullet$  SetTitle

#### The OEShapeQuery class defines the following public methods:

- · AddColorGaussian
- · AddColorGaussians
- · AddShapeGaussian
- · Clear
- · ClearColorGaussians
- · ClearMolecule
- · ClearShapeGaussians
- · ClearShapeGrid
- · DeleteColorGaussian
- · DeleteShapeGaussian
- · SetAtomStrength
- SetMolecule
- SetShapeGrid

### **Constructors**

```
OEShapeQuery()
OEShapeQuery (const OEShapeQuery&)
```

Default and copy constructors.

#### operator=

OEShapeQuery & operator= (const OEShapeQuery &)

The assignment operator.

#### **AddColorGaussian**

void AddColorGaussian (const OESystem:: OEGaussianBase&)

Adds the specified color gaussian to the query.

### **AddColorGaussians**

```
unsigned AddColorGaussians (const OESystem:: OEScalarGrid& grid, const unsigned
\leftrightarrowcolorType)
unsigned AddColorGaussians (const OESystem:: OEScalarGrid& grid, const unsigned
→colorType, const double relGridContour)
```

Adds gaussians of the specified color type to the query, based on the input grid. Gaussians are placed to reproduce the shape of the input grid. The optional argument relGridContour refers to the grid values relative to the maximum, below which a gaussian should not be placed. A default of 0.25 is used for relation to the mone is not specified.

#### **AddShapeGaussian**

void AddShapeGaussian (const OESystem:: OEGaussianBase&)

Adds the specified shape gaussian to the query.

#### **Clear**

void Clear()

Removes all the current contents from the query.

### **ClearColorGaussians**

```
void ClearColorGaussians()
```

Removes all the color gaussians from the query.

### **ClearMolecule**

void ClearMolecule()

Removes the molecule from the query.

#### **ClearShapeGaussians**

void ClearShapeGaussians()

Removes all the shape gaussians from the query.

#### **ClearShapeGrid**

```
void ClearShapeGrid()
```

Removes the shape grid from the query.

### **DeleteColorGaussian**

bool DeleteColorGaussian (OESystem:: OEGaussianBase\*)

Removes the specified color gaussian from the query.

#### **DeleteShapeGaussian**

**bool** DeleteShapeGaussian (OESystem:: OEGaussianBase\*)

Removes the specified shape gaussian from the query.

### **SetAtomStrength**

bool SetAtomStrength (OEChem:: OEAtomBase& atom, const unsigned strength)

Sets the strength of the specified atom. A strength of larger than 1 means that the atom should be represented by multiple atoms at the same location. The atom must be a part of the molecule contained in the query, and may not be a color atom. Method returns False is the strength could not be set.

### **SetMolecule**

void SetMolecule ( const OEChem:: OEMolBase&)

Adds the specified molecule to the query.

#### **SetShapeGrid**

void SetShapeGrid(const OESystem:: OEScalarGrid&)

Adds the specified shape grid to the query.

### 3.1.125 OEShapeQueryBase

class OEShapeQueryBase : public OEBase

The OEShapeQueryBase is an abstract base class. This class defines an interface for creating a shape query, useful for defining a reference system for shape/color overlap calculations.

#### The following methods are publicly inherited from OEBase:

- · operator=
- operator+=
- · AddBaseData
- · AddData
- CreateCopy
- · DeleteData
- · GetBoolData
- $\bullet$  GetData
- · GetDataIter
- · GetDataType
- · GetDoubleData
- · GetFloatData
- · GetIntData
- · GetStringData
- · HasData
- · IsDataType
- · SetBaseData
- · SetBoolData
- · SetData
- · SetDoubleData
- · SetFloatData

- · SetIntData
- · SetStringData

### The OEShapeQueryBase class defines the following public methods:

- · GetAtomStrength
- · GetColorForceField
- · GetColorGaussians
- · GetCompositeMolecule
- GetMolecule
- · GetShapeGaussians
- GetShapeGrid
- $\bullet$  GetTitle
- · HasColor
- · HasMolecule
- · HasShape
- · HasShapeGrid
- $\bullet$  IsEmpty
- $\bullet$  SetTitle

#### The following classes derive from this class:

• OEShapeQuery

#### **GetAtomStrength**

unsigned GetAtomStrength (const OEChem:: OEAtomBase&) const

Returns the strength of the specified atom. The default strength of any atom that is part of the molecule within the query is 1.

### **GetColorForceField**

const OEColorForceField\* GetColorForceField() const

Returns a pointer to the color force field associated with this query.

### **GetColorGaussians**

OESystem::OEIterBase<const OESystem::OEGaussianBase>\* GetColorGaussians() const

Returns an iterator over the color gaussians currently contained in this query.

#### **GetCompositeMolecule**

bool GetCompositeMolecule (OEChem:: OEMolBase& mol) const

This method is useful in extracting the molecule contained in the query with atom strengths explicitly taken care of. Atoms with strength larger than 1 are explicitly represented by multiple atoms in the composite molecule.

#### **GetMolecule**

const OEChem:: OEMolBase& GetMolecule() const

Returns the molecule currently contained in this query. In contrast to the Get CompositeMolecule method, this method returns the molecule as is.

#### **GetShapeGaussians**

OESystem::OEIterBase<const OESystem::OEGaussianBase>\* GetShapeGaussians() const

Returns an iterator over the shape gaussians currently contained in this query.

#### **GetShapeGrid**

const OESystem:: OEScalarGrid& GetShapeGrid() const

Returns the shape grid currently contained in this query.

### **GetTitle**

const char \*GetTitle() const

Returns the title of the query.

#### **HasColor**

bool HasColor() const

Returns *True* if the query currently contains any color atoms or color gaussians.

### **HasMolecule**

bool HasMolecule() const

Returns True if the query currently contains any molecule.

#### **HasShape**

bool HasShape () const

Returns *True* if the query currently contains any molecule, shape grid, or shape gaussians.

#### **HasShapeGrid**

bool HasShapeGrid() const

Returns *True* if the query currently contains any shape grid.

#### **IsEmpty**

bool IsEmpty () const

Returns True if the query currently contains no shape or color.

### **SetTitle**

```
bool SetTitle (const char *)
bool SetTitle (const std:: string&)
```

Sets the title of the query.

### 3.1.126 OESubrocsStarts

class OESubrocsStarts : public OEInertialStarts

The OESubrocsStarts represents the Subrocs starts for overlay optimization.

The following methods are publicly inherited from OEStarts:

- CreateCopy
- $\bullet$  GetNumOfStarts
- · GetStarts
- · Setup
- SetupRef

The following methods are publicly inherited from OEInertialStarts:

- · GetSymmetryThreshold
- · SetSymmetryThreshold

### **Constructors**

```
OESubrocsStarts()
OESubrocsStarts (const OESubrocsStarts&)
```

Default and copy constructors.

#### operator=

OESubrocsStarts & operator=(const OESubrocsStarts &)

The assignment operator.

# 3.1.127 OETanimotoComboCutoff

class OETanimotoComboCutoff : public OEOverlayScoreCutoff

The OETanimotoComboCutoff defines cutoff based on the combined shape and color tanimoto.

The following methods are publicly inherited from OEUnaryPredicate:

```
• CreatePredicateCopy
```

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator()
- CreateCopy

### **Constructors**

OETanimotoComboCutoff (const double)

Default and copy constructors. The argument expects the desired cutoff.

# 3.1.128 OETanimotoCutoff

class OETanimotoCutoff : public OEOverlayScoreCutoff

The OETanimotoCutoff defines cutoff based on the shape tanimoto.

The following methods are publicly inherited from OEUnaryPredicate:

• CreatePredicateCopy

The following methods are publicly inherited from OEOverlayScoreCutoff:

- operator()
- CreateCopy

### **Constructors**

OETanimotoCutoff (const double)

Default and copy constructors. The argument expects the desired cutoff.

# **3.2 OEShape Constants**

# 3.2.1 OEColorFFType

This namespace contains constants defining color force fields.

### **Undefined**

### **OEDefault**

The default approximation is ImplicitMillsDean

#### **ImplicitMillsDean**

The ImplicitMillsDean color forcefield.

### **ExplicitMillsDean**

The ExplicitMillsDean color forcefield.

#### **ImplicitMillsDeanNoRings**

The ImplicitMillsDean color forcefield without rings.

### **ExplicitMillsDeanNoRings**

The ExplicitMillsDean color forcefield without rings.

### **Custom**

Custom color forcefield.

### **Max**

The largest numerical value that can be contained in this namespace. Useful for being able to iterate over all the constants in this namespace.

# 3.2.2 OEDerivativeType

This namespace controls how to extract derivatives from a shape grid, associated with the Grid based overlap calculation.

### Interpolated

Derivatives obtained from interpolation.

### **NearestValue**

Derivatives of the nearest grid point are picked.

# 3.2.3 OEExponentialType

This namespace controls how to obtain exponentials during calculation of Gaussian overlaps and their derivatives.

### **Standard**

Evaluate the exponentials with standard methods every time.

### **Tabulated**

Interpolate from tabulated values.

# 3.2.4 OEMomentSymmetry

This namespace defines constants corresponding to various possible Moments symmetry.

### **NoSymmetry**

No symmetry around any of the inertials axes

### **Oblate**

Oblate symmetry.

### **Prolate**

Prolate symmetry.

### **Spherical**

Spherical symmetry.

### **Unknown**

Unknown symmetry.

# 3.2.5 OEOverlapRadii

This namespace controls how radii of atoms should be handled by the **Shape TK** when doing calculations. The default value of using the carbon radii approximation, OEOverlapRadii\_Carbon, was found to have the best performance in virtual screening experiments.

### Carbon

Treat all atoms, as carbon, with the same radius.

### All

Use the radius of the atom as returned by OEAtomBase.GetRadius.

### **Default**

The default approximation is OEOverlapRadii\_Carbon, to treat all atoms as carbon.

### **Max**

The largest numerical value that can be contained in this namespace. Useful for being able to iterate over all the constants in this namespace.

# 3.2.6 OEScoreType

This namespace controls the type of score to be returned by the operator() methods of a OEOverlapFuncBase derived instance.

### Overlap

Calculate overlap

### **Tanimoto**

Calculate tanimoto

# 3.2.7 OEShapeType

This namespace contains constants that defines shape type appropriate for overlap calculations.

### Grid

**Exact** 

**Analytic** 

**Hermite** 

**None** 

## 3.2.8 OEColorType

This namespace contains constants that defines color type appropriate for overlap calculations.

Grid

**Exact** 

**Analytic** 

**None** 

# **3.3 OEShape Functions**

# 3.3.1 OEAddColorAtom

```
OEChem::OEAtomBase *OEAddColorAtom(OEChem::OEMolBase &mol, float *coords,
                                    unsigned type, const std:: string & typeName,
                                    const std::string &parentName=std::string())
OEChem::OEAtomBase *OEAddColorAtom(OEChem::OEMolBase &mol,
                                    const OEChem:: OEAtomBase ** parents,
                                    unsigned num, unsigned type,
                                    const std:: string & typeName)
OEChem:: OEAtomBase *OEAddColorAtom (OEChem:: OEMCMolBase & mol,
                                    const OEChem:: OEAtomBase ** parents,
                                    unsigned num, unsigned type,
                                    const std:: string & typeName)
```

These functions allow adding color atoms manually, as opposed to being assigned via SMARTS matches from a color force field. Note that the color atom will either be placed at the coordinates supplied in the first version, or at the center of mass of the *parents* atoms. num is the number of atoms in the parent array.

### 3.3.2 OEAddColorAtoms

```
unsigned int OEAddColorAtoms (OEChem:: OEMolBase &mol,
                              const OEColorForceField &cff,
                              bool setCachedSelfColor=false)
unsigned int OEAddColorAtoms (OEChem:: OEMCMolBase &mol,
                              const OEColorForceField &cff,
                              bool setCachedSelfColor=false)
```

Add color atoms to the passed in molecule. Note that this is not normally required as both OEColorOverlap and OEBestOverlay make internal copies of molecules and add color atoms automatically, but if you continually re-use the same molecule, this can be an optimization. Additionally, setting *setCachedSelfColor* to true will pre-calculate and cache the self color on the molecule. This cached value will then be used by OEColorOverlap and OEBestOverlay. The value can be accessed via OEGetCachedSelfColor.

# 3.3.3 OEAddCoordsToColorAtom

```
bool OEAddCoordsToColorAtom (OEChem:: OEMolBase &mol,
                             OEChem:: OEAtomBase *coloratom, float *coords)
```

Set the 3D coordinates of the given color atom.

# 3.3.4 OECalcShapeMultipoles

```
bool OECalcShapeMultipoles (const OEChem:: OEMolBase & mol, float *smult,
                            unsigned int type=OEOverlapRepresentation:: Atoms,
                            bool useHydrogens=false)
```

Calculate the shape (steric) multipoles.

# 3.3.5 OECalcVolume

float OECalcVolume (const OEChem:: OEMolBase &mol, bool useHydrogens=true)

Calculate the shape volume.

# 3.3.6 OEClearCachedSelfColor

```
void OEClearCachedSelfColor (OEChem:: OEMCMolBase &mol)
void OEClearCachedSelfColor (OEChem:: OEMolBase &mol)
```

Clear cached self color from molecule. See OESetCachedSelfColor for more info.

## 3.3.7 OEClearCachedSelfShape

```
void OEClearCachedSelfShape (OEChem:: OEMCMolBase &mol)
void OEClearCachedSelfShape (OEChem:: OEMolBase &mol)
```

Clear cached self shape from molecule. See OESetCachedSelfShape for more info.

# 3.3.8 OECompressColorAtoms

unsigned int OECompressColorAtoms (OEChem:: OEMolBase &mol)

Convert the color atoms on a molecule to an internal compressed form. Useful for saving space when storing precolored molecules. Use OEUncompressColorAtoms to restore the actual color atoms.

# 3.3.9 OECountColorAtoms

unsigned int OECountColorAtoms (const OEChem:: OEMolBase &mol)

Return the number of color atoms attached to a molecule.

# 3.3.10 OEDeleteCompressedColorAtoms

void OEDeleteCompressedColorAtoms (OEChem:: OEMolBase &mol)

Removes information created from the OECompressColorAtoms function.

# 3.3.11 OEGetCachedSelfColor

```
float OEGetCachedSelfColor (const OEChem:: OEConfBase &mol,
                            bool allcolor=false)
float OEGetCachedSelfColor (const OEChem:: OEMolBase &mol,
                            bool allcolor=false)
```

Return the value of cached self color on the molecule or conformer. This function doesn't work for OEM-CMolBase directly, so call it on each individual conformer. Returns 0.0 if there is no cached value. Use OEHasCachedSelfColor to determine if a real value is attached.

# 3.3.12 OEGetCachedSelfShape

```
float OEGetCachedSelfShape(const OEChem:: OEConfBase &conf,
                           unsigned int radiiApprox = OEOverlapRadii:: Carbon,
                           float cradius = 1.7f)
float OEGetCachedSelfShape (const OEChem:: OEMolBase &mol,
                           unsigned int radiiApprox = OEOverlapRadii: Carbon,
                           float cradius = 1.7f)
```

Return the value of cached self shape on the molecule or conformer. The value for radii approximation and cradius need to match those used to set this value initially. This function doesn't work for OEMCMolBase directly, so call it on each individual conformer. Returns 0.0 if there is no cached value. Use OEHasCachedSelfShape to determine if a real value is attached.

# 3.3.13 OEGetCenterAndExtents

```
void OEGetCenterAndExtents (const OEShapeQueryPublic &sq, float *ctr,
                                       float *ext)
```

Fills the first three values of ctr with the location of the center of sq and fills the first three values of ext with the extents.

# 3.3.14 OEGetColorAtoms

```
OESystem::OEIterBase<OEChem::OEAtomBase> *
  OEGetColorAtoms (OEChem:: OEMolBase &mol)
OESystem:: OEIterBase<const OEChem:: OEAtomBase> *
  OEGetColorAtoms (const OEChem:: OEMolBase & mol)
```

Return an iterator of all the color atoms attached to a molecule.

# 3.3.15 OEGetColorParents

```
OESystem:: OEIterBase<OEChem:: OEAtomBase> *
  OEGetColorParents (OEChem:: OEAtomBase *atom)
OESystem:: OEIterBase<const OEChem:: OEAtomBase> *
  OEGetColorParents (const OEChem:: OEAtomBase *atom)
```

Color atoms set via a SMARTS match store the matching atoms as *parents*. This method returns the parent atoms of a given color atom.

# 3.3.16 OEGetColorType

unsigned int OEGetColorType (const OEChem:: OEAtomBase \*coloratom)

Returns the type of a color atom as an unsigned int.

# 3.3.17 OEGetMomentsOfInertiaTransform

```
unsigned int OEGetMomentsOfInertiaTransform (OEChem:: OETrans& argTransform,
                                             const OEChem:: OEMolBase & argMol,
                                             const double argThreshold = 0.15;
unsigned int OEGetMomentsOfInertiaTransform(OEChem:: OETrans& argTransform,
                                             const OESystem:: OEScalarGrid & argGrid,
                                             const double argThreshold = 0.15;
unsigned int OEGetMomentsOfInertiaTransform(OEChem:: OETrans& argTransform,
                                             const OEShapeQuery& argQuery,
                                             const double argThreshold = 0.15);
```

Calculate the transform required to move the object (the specified molecule, grid or the shape query) to the center of its inertial frame. Method returns the moments symmetry of the object defined in the OEMoment Symmetry namespace. The required transform is returned in the first argument.

## 3.3.18 OEHasCachedSelfColor

```
bool OEHasCachedSelfColor (const OEChem:: OEMCMolBase &mol)
bool OEHasCachedSelfColor (const OEChem:: OEMolBase &mol)
```

Returns true if the molecule has cached self color.

# 3.3.19 OEHasCachedSelfShape

```
float OEHasCachedSelfShape (const OEChem:: OEConfBase &conf,
                           unsigned int radiiApprox = OEOverlapRadii:: Carbon,
                           float cradius = 1.7f)
float OEHasCachedSelfShape (const OEChem:: OEMolBase &mol,
                           unsigned int radiiApprox = OECDverlapRadii::Carbon,float cradius = 1.7f)
```

Returns true if the molecule has cached self shape. The value for radii approximation and cradius need to match those used to set this value initially.

# 3.3.20 OEHasColorAtoms

**bool** OEHasColorAtoms (const OEChem:: OEMolBase &mol)

Returns t rue if the molecule has any color atoms attached. Note, OEHasColorAtoms only checks for the existence of color atoms on the molecule, even if OEAddColorAtoms did not match any substructures to create color atoms. Use OEHasPerceivedColorAtoms if trying to determine whether OEAddColorAtoms still needs to be called on the molecule.

# 3.3.21 OEHasCompressedColorAtoms

**bool** OEHasCompressedColorAtoms (const OEChem:: OEMolBase &mol)

Returns true if the molecule contains compressed color atom information created from the OECompressColorAtoms function.

# 3.3.22 OEHasPerceivedColorAtoms

bool OEHasPerceivedColorAtoms (const OEChem:: OEMolBase &mol)

Returns true if OEAddColorAtoms has already been called on mol. Note, OEHasColorAtoms only checks for the existence of color atoms on the molecule, even if OEAddColorAtoms did not match any substructures to create color atoms

# 3.3.23 OEIsColorAtom

bool OEIsColorAtom (const OEChem:: OEAtomBase \*atom)

Returns true if the given atom is a color atom.

# 3.3.24 OEIsFastROCSShapeQuery

```
bool OEIsFastROCSShapeOuery(const OEShapeOueryPublic &query)
bool OEIsFastROCSShapeQuery (const OEShapeQuery & query)
```

Determines if a shape query object is compatible with the OEShapeQuery or a OEShapeQueryPublic overload of the OEShapeDatabase.GetScores and OEShapeDatabase.GetSortedScores in FastROCS TK.

# 3.3.25 OEMol2Query

```
bool OEMol2Query (OEShape:: OEShapeQuery &query, const OEChem:: OEMolBase& mol,
                 const OEShape:: OEColorForceField& cff)
```

Method creates a OEShapeQuery from the input OEMolBase. The specified OEColorForceField is used to generate the color atoms during the query generation process. Method returns True for successful query generation.

# 3.3.26 OEOrientByMomentsOfInertia

```
unsigned int OEOrientByMomentsOfInertia (OEChem:: OEMolBase & argMol,
                                         OEChem:: OETrans& argTransform,
                                         const double argThreshold = 0.15;
unsigned int OEOrientByMomentsOfInertia (OESystem:: OEScalarGrid &argGrid,
                                         OEChem:: OETrans& argTransform,
                                         const double argThreshold = 0.15;
unsigned int OEOrientByMomentsOfInertia (OEShapeQuery& argQuery,
                                         OEChem:: OETrans& argTransform,
                                         const double argThreshold = 0.15;
```

Calculate the transform required to move the object (the specified molecule, grid or the shape query) to the center of its inertial frame, and apply the transform to move the object to the inertial frame. Method returns the moments symmetry of the object defined in the  $OEMomentSymmetry$  namespace. The transform required to get the object back into the original frame is returned in the second argument of the method.

# 3.3.27 OEReadShapeQuery

```
bool OEReadShapeQuery (const char *filename, OEShapeQuery &query)
bool OEReadShapeQuery(const char *filename, OEShapeQueryPublic &query)
bool OEReadShapeQuery(OEPlatform::oeistream &ifs, OEShapeQuery &query)
bool OEReadShapeQuery(OEPlatform::oeistream &ifs, OEShapeQueryPublic &query)
```

The first two overloads reads from a file given in the first parameter into the shape query given in the second parameter. The later two overloads will read from the stream given in the first parameter into the shape query given in the second parameter.

## 3.3.28 OERemoveColorAtoms

void OERemoveColorAtoms (OEChem:: OEMolBase &mol)

Remove all color atoms from the molecule.

# 3.3.29 OEROCSOverlay

```
bool OEROCSOverlay (OEROCSResult& argResult,
        const OEChem:: OEMCMolBase& argQuery,
        const OEChem:: OEMCMolBase& argFitMol,
        const OEROCSOptions& argOptions = OEROCSOptions())
bool OEROCSOverlay (OEROCSResult& argResult,
        const OEChem:: OEMolBase& argOuery,
        const OEChem:: OEMCMolBase& argFitMol,
        const OEROCSOptions& argOptions = OEROCSOptions())
bool OEROCSOverlay (OEROCSResult& argResult,
        const OEChem:: OEMolBase& argQuery,
        const OEChem:: OEMolBase& argFitMol,
        const OEROCSOptions& argOptions = OEROCSOptions())
```

Calculate the overlay between the query and the fit molecule. Returns True if calculation completed successfully. The first argument returns the results of the single best hit.

**Note:** This function sets up the reference system in OEROCS every time it is called, even if it is called with the same reference object. This can have unexpected performance issues if the function is used in a loop.

# 3.3.30 OESelfColor

```
float OESelfColor (const OEChem:: OEMolBase &mol, const OEColorForceField &cff,
                  bool allcolor=false)
```

Calculate the self color score for the given molecule, using the passed in color force field.

# 3.3.31 OESelfShape

```
float OESelfShape (const OEChem:: OEMolBase &mol,
                  unsigned int radiiApprox = OEOverlapRadii::Carbon,
                  float cradius = 1.7f)
```

Return the self-volume term that can be used in molecular similarity measures. The volume is calculated as the first-order-gaussian overlap of all the atoms in the molecule to itself.

 $mol$ 

The molecule to calculate the self-volume for. This molecule is expected to have valid 3D coordinates.

radiiApprox

The approximation to use when calculating the volume. The constant should be pulled from the OEOverlapRadii namespace. The default is to approximate all atom types as carbon with the same radius. If OEOverlapRadii All is given, the radius of the atom as returned by OEAtomBase. GetRadius will be used.

cradius

The radius to use when the carbon radii approximation is being used. The default of 1.7 is based upon the original [Grant-1995] paper to reproduce hard sphere volumes.

#### See also:

Molecular Shape

# 3.3.32 OESetCachedSelfColor

```
bool OESetCachedSelfColor (OEChem:: OEMCMolBase &mol,
                           const OEColorForceField &cff)
bool OESetCachedSelfColor (OEChem:: OEMolBase &mol,
                           const OEColorForceField &cff)
```

Using the passed-in OEColorForceField, calculate and store the self color on each molecule. For the OEMCMolBase, each conformer gets its own stored value. To retrieve the value, use OEGetCachedSelfColor. OEColorOverlap and OEBestOverlay will use the cached value instead of re-calculating the self terms.

### 3.3.33 OESetCachedSelfShape

```
bool OESetCachedSelfShape(OEChem::OEMCMolBase &mcmol,
                          unsigned int radiiApprox = OEOverlapRadii::Carbon,
                          float cradius = 1.7f)
bool OESetCachedSelfShape(OEChem::OEMolBase &mol,
                          unsigned int radiiApprox = OEOverlapRadii:: Carbon,
                          float cradius = 1.7f)
```

Store the self shape term on the molecule. For the OEMCMolBase, each conformer stores its own value. To retrieve the value, use OEGetCachedSelfShape. OEOverlap and OEBestOverlay will use the cached value instead of re-calculating the self terms.

### 3.3.34 OESetColorParents

```
bool OESetColorParents (OEChem:: OEAtomBase *atom,
                        const OEChem:: OEAtomBase ** parents, unsigned num)
```

Set the parent atoms of a given color atom. Not normally used as parents are set for color atoms added via a SMARTS match in the color force field. But if you are manually creating color atoms, this is a way to set its parents.

## 3.3.35 OESetColorType

```
bool OESetColorType (OEChem:: OEAtomBase *coloratom, unsigned type,
                    const std:: string & typeName)
Set/changes the type of a given color atom.
```

# 3.3.36 OESetCoordsFromColorParents

```
bool OESetCoordsFromColorParents (OEChem:: OEMCMolBase &mol)
bool OESetCoordsFromColorParents (OEChem:: OEMolBase &mol)
```

Generates 3D coordinates for the given color atom based on the center of mass of that color atom's parents.

# 3.3.37 OEShapeGetArch

const char \*OEShapeGetArch()

Returns the architecture of the current version of the Shape toolkit. Examples include:

- $\cdot$  microsoft-win32-x86
- redhat-RHEL5-x86 64

### 3.3.38 OEShapeGetLicensee

**bool** OEShapeGetLicensee(std::string &licensee)

Returns the LICENSEE from the current valid Shape TK license.

# 3.3.39 OEShapeGetPlatform

const char \*OEShapeGetPlatform()

Returns the platform, including compiler version, of the current version of the Shape toolkit. Examples include:

- microsoft-win32-msvc9-MD-x86
- redhat-RHEL5-g++4.1-x86\_64

## 3.3.40 OEShapeGetRelease

const char \*OEShapeGetRelease()

Returns the version of this toolkit release. For example: 1.6.1.

# 3.3.41 OEShapeGetSite

**bool** OEShapeGetSite(std::string &site)

Returns the SITE from the current valid Shape TK license.

# 3.3.42 OEShapeGetVersion

unsigned int OEShapeGetVersion()

Returns the build date of the toolkit as an unsigned int. For example: 20090227.

# 3.3.43 OEShapelsLicensed

bool OEShapeIsLicensed(const char \*feature=0, unsigned int \*expdate=0)

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any Shape TK functionality.

The 'feature' argument can be used to check for a valid license to **Shape TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current **Shape TK** license.

See also:

· OEChemIsLicensed function

# 3.3.44 OESortOverlayScores

```
void OESortOverlayScores (OESystem:: OEIter<OEBestOverlayScore> &dst,
                         OESystem:: OEIter<OEBestOverlayResults> &scores,
                         const OESystem:: OEBinaryPredicate<OEBestOverlayScore,
                         OEBestOverlayScore> &sorter, int nbest=1,
                         bool conforder=false)
```

Sort the scores from multiple sets of OEBestOverlayResults into a single iterator of OEBestOverlayScore. The sorting function can be one of the pre-defined functors or a user-defined version.

The nbest default value of 1 implies that on the best overlay for each ref-fit conformer pair is returned. A value greater than one will mean multiple overlays for each ref-fit conformer pair will be kept.

Setting conforder to true forces the results to come out in conformer index order. If nbest is greater than 1 and conforder is **true**, then for each ref-fit conformer pair, the scores will be sorted by the sorting function, but each set of ref-fit results will come out together.

Several of the OEBestOverlay examples show variations of these values. Perhaps the easiest way to understand them is to modify one of the examples and observe the change in the number and order of the scores.

## 3.3.45 OEUncompressColorAtoms

unsigned OEUncompressColorAtoms (OEChem:: OEMolBase &mol)

Convert the internal compressed color atoms to actual color atoms. Has no effect unless the color atoms were previously compressed by OECompressColorAtoms

Note: This function was formerly named OEStringToColorAtoms.

# 3.3.46 OEWriteShapeQuery

```
bool OEWriteShapeQuery (const char *, const OEShapeQuery &query)
bool OEWriteShapeQuery(OEPlatform::oeostream &ofs, const OEShapeQueryBase &query)
```

Writes a query given in the second parameter. The first overload writes the query in the specified file and the second overload writes it to a oeostream. Method returns True if write is successful.

### **CHAPTER**

**FOUR** 

# **DEPRECATED API**

# **4.1 Deprecated OEShape Classes**

# 4.1.1 OEBestOverlay

#### class OEBestOverlay

Note: This deprecated class will not be developed further. It is being replaced by OEOverlay and OEROCS which provides more control and greater expandability.

This class is used to optimize the overlap between 2 molecules. Both molecules can contain one or more conformers. The reference molecule is held rigid and the fit molecule orientation is calculated to maximize overlap. Each conformer of the fit molecule is optimized against each conformer of the reference molecule, resulting in a large number of results that can be returned. The OEBestOverlayResults and OEBestOverlayScore classes are used to make handling this large amount of results easier

Additionally, the reference or fit shape can be a grid instead of a molecule.

Since an OEBestOverlay optimization can result in numerous final results, one for each starting position, the OEBestOverlayResults class is a container to hold all the results for a fit conformer against a reference conformer. This class is essentially a container for one or more OEBestOverlayScore instances. The actual number of scores depends on the OEBOOrientation used in the OEBestOverlay.

For OEBOOrientation Inertial, there will be 4, 8 or 20 scores per ref-fit conformer pair, depending on the symmetry of each conformer. For OEBOOrientation AsIs, there will be just 1 OEBestOverlayScore inside each OEBestOverlayResults instance. And for OEBOOrientation\_Random, then there will be 1 OEBestOverlayScore for each of the N random starts.

When dealing with the results from OEBestOverlay, the user can either use a double loop, *i.e.* loop over all the OEBestOverlayResults instances for each ref-fit conformer pair then loop over each OEBestOverlayScore inside each OEBestOverlayResults instance. In this case, the results also come out in conformer order.

```
for res in best. Overlay (fitmol) :
    for score in res. GetScores():
        # do something with score
```

Or, there is a free function OESortOverlayScores, that takes an iterator of OEBestOverlayResults and returns a single, sorted iterator of OEBestOverlayScores that can be used in a single loop.

```
scoreiter = OEBestOverlayScoreIter()
OESortOverlayScores(scoreiter, best.Overlay(fitmol), OEHighestTanimotoCombo())
```

```
for score in scoreiter:
     # do something with score
```

#### **Constructors**

```
OEBestOverlay ()
OEBestOverlay (const OEBestOverlay &)
OEBestOverlay (const OEChem:: OEMCMolBase & refmol)
OEBestOverlay (const OESystem::OEScalarGrid & refgrid, float interpolate=0.5f)
```

An empty OEBestOverlay class instance can be created, or a new instance can take the reference molecule or grid as an argument. Note that by default, grids that have a resolution larger that 0.5 Å will be interpolated to that resolution.

#### operator=

OEBestOverlay & operator= (const OEBestOverlay &)

The assignment operator.

### **ClearColorForceField**

void ClearColorForceField()

Clear out any color force field. No color scores will be calculated.

### **ClearUserStarts**

void ClearUserStarts()

Set the number of User Starts back to zero.

### **GetCarbonRadius**

float GetCarbonRadius() const

Return the current value for the carbon radius approximation.

### **GetInitialOrientation**

unsigned int GetInitialOrientation() const

Get the current value for initial orientation. Possible values are from the OEBOOrientation namespace.

### **GetMaxRandomTranslation**

float GetMaxRandomTranslation() const

Get the value in  $\AA$  of maximum random translation.

#### **GetMethod**

unsigned int GetMethod() const

Return the current value of overlap method.

#### **GetMinimizeType**

unsigned int GetMinimizeType() const

Get the current value for minimize type. Possible values are from the OEBOMinType namespace.

#### **GetNumRandomStarts**

unsigned int GetNumRandomStarts() const

Get the current number of random starts.

### **GetNumUserStarts**

unsigned int GetNumUserStarts() const

Get the number of user starts currently set. Note that these are not actually used unless OEBOOrientation\_UserInertialStarts is also set.

### **GetRadiiApproximation**

unsigned int GetRadiiApproximation() const

Return the current value of the radii approximation.

#### **GetRandomSeed**

unsigned int GetRandomSeed() const

Get the current value of the random seed.

### **GetRefGrid**

```
const OESystem:: OEScalarGrid *GetRefGrid() const
```

### **GetRefMol**

```
const OEChem:: OEMCMolBase *GetRefMol() const
```

#### **GetRefSelfColor**

```
float GetRefSelfColor()
```

Return the self color score of the reference molecule.

### **GetRefSymmetry**

unsigned int GetRefSymmetry (unsigned int confIdx) const

Return the current representation level.

### GetSymmetryThreshold

float GetSymmetryThreshold() const

#### **GetUseHydrogens**

bool GetUseHydrogens () const

Return the status of hydrogen use in OEBestOverlay.

### **GetUserStarts**

bool GetUserStarts (float \*xyz) const

Extract the coordinates of the user starts.  $xyz$  should be sized to 3  $*$  GetNumUserStarts().

#### **Overlay**

```
OESystem::OEIterBase<OEBestOverlayResults> *
  Overlay (const OEChem:: OEMCMolBase &fitmol)
```

Perform the calculation and return the an iterator of the results.

### **SetCarbonRadius**

void SetCarbonRadius (float cradius)

Set the radius to use when using  $OEOverlapRadi\_Carbon$ . By default this is set to 1.7 Å.

### **SetColorForceField**

```
bool SetColorForceField(unsigned int type)
bool SetColorForceField(OEPlatform::oeistream &is)
bool SetColorForceField(const std::string &filename)
bool SetColorForceField(const OEColorForceField &cff)
```

Set the color force field to be used. Once set, color scores will be calculated and included in the results. Color gradients will not be included in the optimization unless specifically set using SetColorOptimize(true).

### **SetColorOptimize**

void SetColorOptimize (bool state)

Add color gradients to shape gradients in the optimization. Has no effect unless a color force field is also set via OEBestOverlay. SetColorForceField.

#### **SetInitialOrientation**

void SetInitialOrientation (unsigned int orient)

Determines the initial orientation (starting position) for each optimization. The default is OEBOOrientation Inertial. Alternatives are defined in the OEBOOrientation namespace.

### **SetMaxRandomTranslation**

void SetMaxRandomTranslation (float trans)

If using random starts, this set the maximum distance (in  $\AA$ ) that the center of mass of the fit molecule will be moved away from the center calculated for inertial frame alignment.

#### **SetMethod**

void SetMethod (unsigned int method)

Set the method used to calculate overlap. The default for OEBestOverlay is OEOverlapMethod\_Grid. Alternatives are defined in the OEOverlapMethod namespace.

#### **SetMinimizeTvpe**

void SetMinimizeType (unsigned int type)

Set the score to use in the optimization. Options are in the OEBOMinType namespace.

#### **SetNumRandomStarts**

void SetNumRandomStarts (unsigned int n)

If SetInitialOrientation is set to OEBOOrientation\_Random, this method sets the number of random starting positions that will be used.

#### **SetRadiiApproximation**

void SetRadiiApproximation (unsigned int type)

Set the radius approximation used to calculate overlap. The default for OEBestOverlay is OEOverlapRadii\_Carbon. Alternatives are defined in the OEOverlapRadii namespace.

#### **SetRandomSeed**

void SetRandomSeed (unsigned int seed)

Set a random seed value to allow reproducible random searches.

#### **SetRefGrid**

bool SetRefGrid(const OESystem::OEScalarGrid & refgrid, float interpolate=0.5f)

Set a reference grid for the calculation. OEBestOverlay makes an internal copy. Pre-existing reference molecules or grids are replaced.

### **SetRefMol**

bool SetRefMol(const OEChem:: OEMCMolBase & refmol)

Set a reference molecule for the calculation. OEBestOverlay makes an internal copy. Pre-existing reference molecules or grids are replaced.

#### **SetSymmetryThreshold**

void SetSymmetryThreshold (float threshold)

#### **SetUseHydrogens**

void SetUseHydrogens (bool state)

Boolean to determine whether hydrogens are included in the shape calculation. By default this is false and hydrogens are ignored.

### **SetUserStarts**

void SetUserStarts (const float \*xyz, unsigned int nstarts)

Set a set of 3D coordinates for doing separate inertial starts.  $xyz$  should be 3<sup>\*</sup> nstarts. These are not used unless OEBOOrientation\_UserInertialStarts is also set.

### 4.1.2 OEColorOverlap

class OEColorOverlap

Note: This deprecated class will not be developed further. It is being replaced by derivatives of OEColorFunc which provides more control and greater expandability.

This class represents OEColorOverlap.

#### **Constructors**

```
OEColorOverlap()
OEColorOverlap (const OEColorOverlap & rhs)
```

Default and copy constructors.

### operator=

OEColorOverlap & operator=(const OEColorOverlap & rhs)

### **ColorScore**

```
bool ColorScore (OEColorResults & res)
bool ColorScore (const OEChem:: OEMolBase &fitmol, OEColorResults & res)
```

### **GetAllColor**

bool GetAllColor() const

#### **GetSelfColor**

float GetSelfColor() const

#### **SetAllColor**

void SetAllColor (bool state)

### **SetColorForceField**

```
bool SetColorForceField(unsigned int cffType)
bool SetColorForceField(OEPlatform::oeistream &is)
bool SetColorForceField(const std::string &filename)
bool SetColorForceField(const OEColorForceField &cff)
```

### **SetFitMol**

bool SetFitMol (const OEChem:: OEMolBase &fitmol)

### **SetRefMol**

bool SetRefMol(const OEChem:: OEMolBase & refmol)

# **4.1.3 OEColorResults**

struct OEColorResults

Note: This deprecated class will not be developed further. It is being replaced by OEOverlapResults which provides more control and greater expandability.

This class represents OEColorResults.

### **Constructors**

OEColorResults()

Default and copy constructors.

#### **GetFitTversky**

float GetFitTversky() const

#### **GetRefTversky**

float GetRefTversky () const

#### **GetTanimoto**

float GetTanimoto() const

#### **GetTversky**

float GetTversky (float alpha, float beta) const

### 4.1.4 OEHighestComboScore

```
struct OEHighestComboScore : public OESystem:: OEBinaryPredicate<OEBestOverlayScore,
→OEBestOverlayScore>
```

Note: This deprecated class will not be developed further, as it was developed based on a nonstandard score.

This class represents OEHighestComboScore, predicte to compare OEBestOverlayScore based on a combination of shape tanimoto and color score.

operator()

```
bool operator () (const OEBestOverlayScore &s1,
                const OEBestOverlayScore &s2) const
```

#### **CreateCopy**

```
OESystem::OEBinaryFunction<OEBestOverlayScore , OEBestOverlayScore , bool> *
 CreateCopy() const
```

## 4.1.5 OEOverlap

class OEOverlap

Note: This deprecated class will not be developed further. It is being replaced by derivatives of OEShapeFunc which provides more control and greater expandability.

OEOverlap calculates the static shape overlap between a reference molecule or grid and a fit molecule or grid. Note that this does not move the fit molecule(grid) nor does it optimize the overlap. It simply calculates the score for the provided orientation.

#### **Constructors**

```
OEOverlap()
OEOverlap (const OEOverlap & rhs)
OEOverlap (const OEChem:: OEMolBase & refmol)
OEOverlap (const OESystem:: OEScalarGrid & refmol)
```

Default and copy constructors.

#### operator=

OEOverlap &operator=(const OEOverlap &rhs)

Assignment operator. The contents of the passed OEOverlap reference are copied into the current OEOverlap instance.

### **GetCarbonRadius**

float GetCarbonRadius() const

Return the current value for the carbon radius approximation.

### **GetGridSpacing**

float GetGridSpacing() const

Return the current value for the grid spacing to use for the OEOVERLapMethod Grid method of calculating overlaps. Is not used by any other overlap method. Defaults to 0.25.

### **GetMethod**

unsigned int GetMethod() const

Return the current value of overlap method.

#### **GetRadiiApproximation**

unsigned int GetRadiiApproximation() const

Return the current value of the radii approximation.

#### **GetUseHydrogens**

bool GetUseHydrogens () const

Return the status of hydrogen use in OEOverlap.

#### Overlap

```
bool Overlap (OEOverlapResults & res, float *atomOverlaps=0)
bool Overlap (const OEChem:: OEMolBase &fitmol, OEOverlapResults & res,
             float *atomOverlaps=0)
```

Calculate the overlap of the passed in fit molecule or fit grid and place the results into the passed instance of OEOverlapResults.

#### **SetCarbonRadius**

bool SetCarbonRadius (float cradius)

Set the radius to use when using OEOverlapRadii\_Carbon. By default this is set to 1.7 Angstroms. See OEBestOverlay.GetCarbonRadius.

### **SetFitMol**

bool SetFitMol (const OEChem:: OEMolBase &fitmol)

Set molecule to be used as fit object.

#### **SetGridSpacing**

**bool** SetGridSpacing (float spacing)

Set the grid spacing to use for the OEOverlapMethod\_Grid method of calculating overlaps. Smaller values typically lead to more accurate results when considering large numbers of compounds, though not necessarily more accurate results in individual cases. This method will only accept values between 0.125 and 1.0 inclusive. The default is 0.25 angstroms for a balance of performance and reproducibility. Larger values may lead to better performance on some platforms.

#### **SetMethod**

bool SetMethod (unsigned int m)

Set the method used to calculate overlap. The default for OEOverlap is OEOverlapMethod\_Exact. Alternatives are defined in the OEOverlapMethod namespace.

#### **SetRadiiApproximation**

**bool** SetRadiiApproximation (unsigned int type)

Set the radius approximation used to calculate overlap. The default for OEOverlap is OEOverlapRadii\_Carbon. Alternatives are defined in the OEOverlapRadii namespace.

### **SetRefGrid**

bool SetRefGrid(const OESystem:: OEScalarGrid & refgrid)

Set a reference grid for the calculation. An internal copy is made. Any previous reference molecule or grid is cleared.

#### **SetRefMol**

bool SetRefMol(const OEChem:: OEMolBase & refmol)

Set a reference molecule for the calculation. An internal copy is made. Any previous reference molecule or grid is cleared.

### **SetUseHydrogens**

```
bool SetUseHydrogens (bool state)
```

Boolean to determine whether hydrogens are included in the shape calculation. By default this is false and hydrogens are ignored.

# 4.1.6 OEShapeQueryPublic

```
class OEShapeQueryPublic
```

This class represents OEShapeQueryPublic. This is an initial public implementation with limited functionality.

### **Constructors**

```
OEShapeQueryPublic()
OEShapeQueryPublic(const OEShapeQueryPublic &)
```

Default and copy constructors.

#### operator=

```
OEShapeQueryPublic & operator=(const OEShapeQueryPublic &)
```

Assignment operator.

#### operator bool

operator bool() const

Returns *true* if the instance is valid. Otherwise returns false.

### **GetColorForceField**

const OEColorForceField \*GetColorForceField() const

Returns a pointer to its OEColorForceField

### **GetTitle**

const char \*GetTitle() const

Returns the title.

# **4.2 Deprecated OEShape Constants**

# 4.2.1 OEBOMinType

Note: This is a deprecated namespace.

This namespace contains constants.

**Tanimoto** 

Overlap

**Autoscale** 

**Default** 

# **4.2.2 OEBOOrientation**

Note: This is a deprecated namespace.

This namespace contains constants.

**Inertial** 

**Asls** 

Random

**InertialAtHeavyAtoms** 

**InertialAtColorAtoms** 

**UserInertialStarts** 

**Subrocs** 

**Default** 

# 4.2.3 OEOverlapMethod

Note: This is a deprecated namespace.

This namespace contains constants.

Grid

**Analytic** 

**Analytic2** 

### **Exact**

### **Max**

# 4.2.4 OEOverlapRepresentation

Note: This is a deprecated namespace.

This namespace contains constants.

### **Atomic**

**Atoms** 

**Bonding** 

**Bonds** 

Full

**All** 

# Gaussian

**Default** 

**Max** 

### **CHAPTER**

# **FIVE**

# **RELEASE HISTORY**

# 5.1 Shape TK 3.7.0

### 5.1.1 New features

- A new method, *AddColorGaussians*, has been added that allows adding color Gaussians to the OEShapeQuery based on intensity of values on a grid.
- A new class, OEOverlapPrepOptions, has been added that allows modifying options that would be used during the Prep. Subsequently, a new constructor for OEOverlapPrep has been added that takes the OEOverlapPrepOptions as an argument.

# 5.1.2 Minor bug fixes

• Color force field names in OEColorFFParameter are now treated as case-insensitive.

# 5.2 Shape TK 3.6.2

## 5.2.1 New features

- The following preliminary API classes have been made permanent.
  - OEColorFFParameter
  - $-$  OEFlexiOverlapFunc
  - OEFlexiOverlapOptions
  - $-$  OEFlexiOverlapResults
  - OEFlexiOverlay
  - OEFlexiOverlayOptions
- New methods, SetAtomStrength and GetAtomStrength, have been added that allow multiplying the contribution of shape overlap for any atoms, without adding an additional atom or Gaussian.

# 5.3 Shape TK 3.6.1

# 5.3.1 Major bug fixes

• Memory consumption when initiating an OEColorForceField has been reduced by moving instantiation of internal OESubSearch-based *colorer* objects to a lazy instantiation mode.

# 5.4 Shape TK 3.6.0

# 5.4.1 New features

- OEFlexiOverlapFunc and OEFlexiOverlay have been updated to allow users to use a Shape Query as the reference system. This allows OEFlexiOverlapFunc SetupRef and OEFlexiOverlay SetupRef to accept a Shape Query.
- A new method, *SetupFlex*, has been added. This method can be used to set up overlap calculation functions when molecules are expected to be flexible and their self overlaps are not fixed to the initial value.
- A new method, *SortedOverlay*, has been added as an alternative to *Overlay*. This method provides a desired number of top hit results instead of all of the hits and is especially suitable when working with molecules with excessive numbers of conformers.
- Two additional control flags, GetRigidOverlay and SetRigidOverlay, have been added to the OEFlexiOverlay-Options class. These flags indicate if rigid overlay optimization between the fit molecule conformers and the reference system should be performed prior to the flexible optimization.

# 5.4.2 Major bug fixes

• An issue in *OEFlexiOverlay* that caused a TanimotoCombo value greater than 2.0 when a molecule was flexibly fitted against itself has been fixed.

# 5.4.3 Minor bug fixes

- The default value for the  $\text{color}$  function in OEFlexiOverlapOptions during OEFlexiOverlay has been changed from none to exact. This ensures that color overlaps are reported when flexible optimization is performed with default parameters.
- An issue has been fixed with OEFlexiOverlay that was causing shape Tanimoto to be occasionally reported as larger than 1.0 after a flexible optimization.
- The legal range of values for the color score multiplier has been added to the OEFlexiOverlapOptions and OEOverlayOptions option classes.
- OEColorFFParameter now allows users to select explicit mills deannorings properly as the color force field.
- The acceptable ranges for the number of optimization iteration steps have been defined for  $OEFlexiOverlayOp$ tions and OEOverlayOptions.
- Newer implementation of Hermite code had limits on lambda parameters of the expansion. In rare cases, these were affecting the lambda parameter search (Newton optimization stepping outside the limits). Removing the limits fixed the previous problems with finding lambda parameters.

# 5.5 Shape TK 3.5.1

# 5.5.1 New features

- The following new methods have been added to  $OEOverall$  *OEOverlayOptions* to improve flexibility in defining parameters:
  - $-$  SetShapeFuncType
  - $-$  GetShapeFuncType
  - SetColorFuncType
  - GetColorFuncType
  - SetShapeOptions
  - GetShapeOptions
  - SetColorOptions
  - GetColorOptions
- A new overload for the method *CreateGrid* has been added that takes a transform object as an additional argument that is applied after the grid is generated.

# 5.5.2 Major bug fixes

- Default forcefields in *OEFlexiOverlapOptions* now ignore electrostatic interactions, as electrostatics appear to have negligible effects on optimized overlaid structures. Ignoring the electrostatic interactions also improves efficiency of optimization for the corresponding OEFlexiOverlapFunc.
- The default for OEOverlapFunc in OEFlexiOverlayOptions now consists of Shape only and no Color. The default Shape score used is Overlap.

# 5.5.3 Minor bug fixes

- A mismatch between the Hermite grid and the input molecule has been fixed.
- The maximum value on the Hermite resolution parameter has been increased from 30 to 100.

# 5.5.4 Documentation changes

The following C++ and Python examples have been added to demonstrate how to use new preliminary APIs:

- Two new C++ and Python examples have been added to the Flexible Overlay with Shape, Color, and Forcefield section that show flexible overlay optimization of the fit molecules against a single reference molecule conformer.
- When using *BestOverlay*, only one conformer that has the highest Tanimoto-combo similarity to the reference molecule is returned.

# 5.6 Shape TK 3.5.0

# 5.6.1 New features

- The new preliminary API classes,
  - $-$  OEFlexiOverlapFunc
  - OEFlexiOverlapOptions
  - OEFlexiOverlapResults

have been added which provide an interface for overlap calculation between a reference molecule and a fit molecule using Shape and Color similarity along with intra-molecular force field of a fit molecule.

- The new preliminary API classes,
  - OEFlexiOverlay
  - OEFlexiOverlayOptions

have been added which provide an interface for flexible overlay optimization between a reference molecule and a fit molecule conformers using Shape and Color similarity along with intra-molecular force field of a fit molecule.

# 5.6.2 Minor bug fixes

• Swig wrapping issue for GetShapeGaussians and GetColorGaussians have been fixed.

# 5.7 Shape TK 3.4.3

Fall 2021

# 5.7.1 New features

- A new method, *OEMol2Query*, has been added that creates an *OEShapeQuery* from an input OEMolBase.
- A new preliminary API class, OEColorFFParameter, has been added as part of the extended set of OEParameter classes. The new parameter class works with predefined color force fields using an OEColorForceField object.

# 5.7.2 Minor bug fixes

• OESetColorParents now errors out properly if the color atom and the parent atoms specified do not have the same parent molecule.

# 5.8 Shape TK 3.4.2

July 2021

# 5.8.1 Major bug fixes

• A bug that caused some molecules to get a perfect Shape Tanimoto score of 1.0, even though their overlap was not optimal, has been fixed.

# 5.9 Shape TK 3.4.1

**Fall 2020** 

### 5.9.1 New features

• A new function, OEIsFastROCSShapeQuery, has been added that determines if an OEShapeQuery object is compatible with FastROCS TK.

# 5.9.2 Major bug fixes

- An issue that caused performance slowdown in  $OESelfShape$  has been fixed.
- An issue that caused OEGridColorFunc to give incorrect results when used with a custom color force field containing a range value other than 1.0 has been fixed.

# 5.9.3 Minor bug fixes

• The UserColor example has been updated to more robustly check return statuses. See Calculating Overlap.

# 5.10 Shape TK 3.4.0

As part of the integration of OEToolkits and OEApplications into a single release, the version number of Shape TK has been upgraded to 3.4.0 to make it consistent with that of the ROCS application.

# 5.10.1 Minor bug fixes

- The following methods now return bool instead of a void:
  - OEShapeOptions. SetCarbonRadius
  - OEShapeOptions. SetRadiiApproximation
  - OEShapeOptions. SetScoreType
  - OEColorOptions. SetMultiplier
  - OEColorOptions. SetScoreType
  - OEAnalyticOptions. SetExpType

- OEAnalyticOptions. SetProxyGridCutoff
- OEAnalyticOptions. SetUseProxyGrid
- OEShapeGridOptions. SetDerivativeType
- OEShapeGridOptions. SetGridSpacing
- OEOverlayOptions. SetMaxOptSteps
- OEROCSOptions. SetConfsPerHit
- OEROCSOptions. SetMaxHits
- OEROCSOptions. SetNumBestHits
- OEROCSOptions. SetPerformPrep
- OEROCSOptions. SetUseMaxHits
- The explicit Mills-Dean color force fields, *ExplicitMillsDean* and *ExplicitMillsDean*, now accurately treat a tertiary amine as a donor and not an acceptor.
- The OEColorForceField. AddColorer method now checks to ensure that the SMARTS patterns added as color do not have a mix of explicit and implicit hydrogen expressions.
- The OEOverlapPrep.Prep and OEAddColorAtoms methods now properly handle color atom assignments for molecules with explicit hydrogens and color SMARTS patterns containing hybridization.

# 5.11 Shape TK 2.0.4

## 5.11.1 New features

• Two new methods, SetMultiplier and GetMultiplier, have been added to the OEColorOptions class that enable use of a multiplier to the calculated color scores.

# 5.11.2 Minor bug fixes

- The Python example in the section, *Calculating NxN scores*, has been fixed.
- The multithread version of the Python example in *Best Optimization Result* has been fixed.

# 5.12 Shape TK 2.0.3

## 5.12.1 New features

• A new overload of  $OEWriteShapeQuery$  has been added that writes queries to an oeostream object.

# 5.12.2 Minor bug fixes

- OEAnalyticShapeFunc and OEGridShapeFunc now produce a value of 1.0 for self-shape Tanimoto.
- OEOverlay now properly handles empty query objects and queries consisting of only color atoms.
- *OEOverlay* now properly handles molecules without coordinates.
- The OEColorFunc assignment operator has been fixed.

# 5.12.3 Documentation changes

• Code examples in the *Examples* section have been revised.

# 5.13 Shape TK 2.0.2

# 5.13.1 New features

- Hermite classes OEHermiteOptions, OEHermite, and OEHermiteShapeFunc have graduated from preliminary API to stable API status for the 2018.Oct release.
- The OEHermiteShapeFunc class now derives from OEShapeFunc. As a result, Hermite overlay can be done more efficiently using the OEOverlay class.

# 5.13.2 Minor bug fixes

- The OEHermite. Setup method now takes an OEMolBase rather than a OEMCMolBase parameter.
- The OEShape:: OEColorFunc:: operator= method has been fixed.

# 5.13.3 Java-specific changes

• OEHermiteOptions, OEHermite, and OEHermiteShapeFunc are now available in Java.

# 5.13.4 C#-specific changes

• OEHermiteOptions, OEHermite, and OEHermiteShapeFunc are now available in C#.

# 5.13.5 Documentation changes

• Java and C# examples have been added to the *Shape from Hermite expansion* examples.

# 5.14 Shape TK 2.0.1

# 5.14.1 New features

- A new class, OEMultiRefOverlay, has been added to provide overlay optimization with a multi-conformer molecule as the reference.
- A new method,  $OEOverlay$ . Best Overlay, has been added to provide the single best OEBestOverlayScore as output from an overlay optimization calculation.
- . Two new methods, OEColorOptions. SetScoreType and OEColorOptions. GetScoreType, have been added to control color optimization options.
- A new class, OEHighestTverskyCombo, has been added to sort OEBestOverlayScore based on TverskyCombo.
- Instantiation of the old API classes *OEBestOverlay, OEOverlap*, and *OEColorOverlap* now produces a warning message stating that the class is deprecated.

# 5.14.2 Minor bug fixes

- An issue related to Shape TK requiring a case license has been fixed.
- An issue related to overlay optimization when an OEShapeQuery class with only Gaussians as the reference has been fixed.
- was initialized with • An unnecessary warning that occurred when an *OEColorForceField* OEColorFFType\_Custom has been removed.
- A SMARTS definition in ImplicitMillsDean that incorrectly defined an anion on the central carbon of a malate-like molecule with no hydrogen has been fixed.

# 5.14.3 Documentation changes

- The hermite-tanimoto example in both C++ and Python has been modified to move the fit molecule to the overlaid position.
- A Python example for performing best overlay calculations using multithreading has been added.

# 5.15 Shape TK 2.0.0

## 5.15.1 New features

- The Shape TK has been completely redesigned to make the library thread-safe, to make the library more flexible to use, and to allow the API to be easily extended with additional functionality.
- Three new classes, OEExactShapeFunc, OEGridShapeFunc, and OEAnalyticShapeFunc, have been added to provide static shape overlap calculation based on Exact, Grid, and Analytic methods.
- Three new classes, OEExactColorFunc, OEGridColorFunc, and OEAnalyticColorFunc, have been added to provide static color score calculation based on Exact, Grid, and Analytic methods.
- A new class, *OEShapeOptions*, has been added to define options related to all *OEShapeFunc* evaluations.
- A new class, *OEColorOptions*, has been added to define options related to all *OEColorFunc* evaluations.
- A new class, OEShapeGridOptions, has been added to define options related to grid-based method evaluations.

- A new class, *OEAnalyticOptions*, has been added to define options related to analytic method evaluations.
- A new class, *OEOverlapPrep*, has been added that can be used to prepare molecules for shape and/or color calculations.
- A new class, *OEOverlay*, has been added that can be used to overlay conformers of an OEMol on a reference system that can be a molecule, grid, or shape query.
- A new class, *OEOverlayOptions*, has been added that sets all options for overlay optimization using *OEOverlay*. *OEOverlayOptions* provides flexibility to optimize based on shape or color or both, to choose any method for shape or color calculation, and to optimize overlap or Tanimoto individually for shape and color.
- A new class, OEROCS, has been added that can be used to generate hits from a database on a reference system that can be a molecule, grid, or shape query. *OEROCS* provides top hits based on flexible scoring criterion.
- A new class, *OEROCSOptions*, has been added to define options for generating hits using *OEROCS*.
- A new class, *OEROCSResult*, has been added that extends the *OEBestOverlayScore* with overlaid conformer structures.
- Three overloads of a new function,  $OEROCSOVerlay$ , have been added to provide the best hit between a pair of molecules.
- New unary predicates have been added to terminate a hit search calculation using OEROCS:
  - OEColorTanimotoCutoff
  - OEFitColorTverskyCutoff
  - OEFitTverskyComboCutoff
  - OEFitTverskyCutoff
  - OEOverlapCutoff
  - OERefColorTverskyCutoff
  - OERefTverskyComboCutoff
  - OERefTverskyCutoff
- The OEShapeOueryPublic class has been replaced by OEShapeOuery and is complete with functionality to create and edit a shape query with combinations of molecules, grids, and Gaussians.
- With the introduction of the new API classes in **Shape TK**, several previously existing classes have been deprecated. The following table shows the deprecated classes and their replacements:

| Deprecated Class            | New Class                                                   |
|-----------------------------|-------------------------------------------------------------|
| OEShape::OEOverlap          | <i>OEExactShapeFunc OEGridShapeFunc OEAnalyticShapeFunc</i> |
| OEShape::OEColorOverlap     | <i>OEExactColorFunc OEGridColorFunc OEAnalyticColorFunc</i> |
| OEShape::OEBestOverlay      | <i>OEOverlay OEROCS</i>                                     |
| OEShape::OEColorResults     | <i>OEOverlapResults</i>                                     |
| OEShape::OEShapeQueryPublic | <i>OEShapeQuery</i>                                         |

- With the introduction of the new API, several obsolete functionalities have been removed. These functionalities were added in the early development days of **Shape TK** and are no longer deemed useful. Methods related to such functionality, contained within the deprecated classes, are now ignored. The list of methods that fall into this category, with their current behavior, is as follows:
  - OEShape:: OEOverlap:: Overlap (const OESystem:: OEScalarGrid&, OEOverlapResults&): The method does nothing and returns false.

- OEShape:: OEOverlap:: SetFitGrid(const OESystem:: OEScalarGrid&): The method does nothing and returns false.
- OEShape:: OEOverlap:: SetRepresentationLevel (unsigned int): The method does nothing and returns false. The default representation level is OEShape:: OEOverlapRepresentation:: Atomic.
- OEShape::OEColorOverlap::SetAllColor(bool): The method does nothing and returns false. The default AllColor state is true.
- OEShape::OEBestOverlay::SetAllColor(bool): The method does nothing and returns false. The default AllColor state is true.
- OEShape:: OEBestOverlay:: SetInertialAxialDivisions (unsigned int): The method does nothing and returns false.
- OEShape:: OEBestOverlay:: SetRepresentationLevel (unsigned int): The method does nothing and returns false. The default representation level is OEShape:: OEOverlapRepresentation:: Atomic.
- OEShape:: OEBestOverlay:: Overlay (const OESystem:: OEScalarGrid&): The method does nothing and returns an empty iterator.

### 5.15.2 Minor Bug Fixes

- The Hermite grid generated by OEHermite was previously offset from the original frame of the molecule being expanded. This has been corrected.
- Previously, using a molecule without 3D coordinates as a reference for an overlay had caused a crash. This has been fixed.

### 5.15.3 Documentation changes

• The ShapeTK examples have been rewritten to illustrate the use of the new API. The various best Overlay examples now have more descriptive names.

# 5.16 Shape TK 1.11.0

## 5.16.1 New features

- A new API has been added to perform Hermite expansion and store the approximate shape of drug-size molecules and proteins.
  - The class OEHermite and associated options class OEHermiteOptions allows the user to perform Hermite expansion of a molecule and output the results to a grid.
  - The class  $OEHermiteShapeFunc$  can be used to obtain a best shape overlap of two molecules by approximating each molecule with its Hermite representation.

# **5.16.2 Documentation changes**

- An overview of using Hermite expansion for molecular shape can be found here Shape from Hermite Representation.
- A new example section, *Shape from Hermite expansion*, has been added to illustrate the capabilities of the new API for Hermite expansion.

# 5.17 Shape TK 1.10.4

• Minor internal improvements have been made.

# 5.18 Shape TK 1.10.3

# 5.18.1 Python-specific changes

• The OESortOverlayScores function now accepts a custom scoring function derived from the OEBestOverlayScoreSorterPred Python class.

# 5.18.2 Java-specific changes

• The OESortOverlayScores function now accepts a custom scoring function derived from the OEBestOverlayScoreSorterPred Java class.

# 5.19 Shape TK 1.10.2

# 5.19.1 Major bug fixes

• OEShape::OEBestOverlay::SetAllColor(true) with custom color atoms will no longer result in Tanimoto values larger than 1.0 when custom color atoms are placed on the molecule. The bug was located in OESelfColor function when the allColor parameter was set to true and caused the function to arbitrarily remove the custom color atoms placed on the molecule and recalculate a new set of color atoms based on the color force field set. This meant OEBestOverlay was calculating the self term and the overlap terms with an entirely different set of color atoms. OESelfColor will now only incur a molecule copy and OEAddColorAtoms when OEHasColorAtoms is false.

# 5.19.2 Minor bug fixes

· OEBestOverlay. SetColorForceField will now throw a warning and return false if OEColorForce-Field is not valid, as determined by OECOLOTFOTCEField. Ready method.

# 5.20 Shape TK 1.10.1

### 5.20.1 New features

- OESelfShape is now nearly two times faster for the default case of the carbon radii approximation with the OEOverlapRadii Carbon constant.
- OEUncompressColorAtoms performance has been improved.

### 5.20.2 Documentation fixes

• A correction has been made to the Tversky equation in the Molecular Shape section.

# 5.21 Shape TK 1.10.0

### 5.21.1 Minor bug fixes

• A crash that occurred when attempting to use the Subrocs initial orientation method with an OEBestOverlay object to overlay molecules onto a reference grid has been fixed. A warning is now issued stating that Subrocs matching against grids is not implemented, and that inertial frame alignment will be used instead.

# 5.22 Shape TK 1.9.7

### 5.22.1 New features

- OEReadShapeQuery overload has been added to work on oeistream objects instead of a direct file name.
- OEOverlap. SetGridSpacing has been added to allow adjusting the grid spacing used by the OEOverlapMethod\_Grid shape overlap method. Lower values typically yield overlaps that agree more closely with the OEOverlapMethod\_Exact method, while higher values can sometimes be faster and will diverge more.

## 5.22.2 Major bug fixes

• OEBOOrientation\_Subrocs will sometimes crash when given a grid as the reference. Some of these crashes have been fixed, but others are more difficult to pin down and will persist till the next release.

## 5.22.3 Minor bug fixes

- OEShape:: OEBestOverlayScore:: GetTversky can now accept alpha and beta of 0.0 provided both parameters are not 0.0.
- OEHasCompressedColorAtoms return type has changed from unsigned int to bool as the return value was always Boolean.

# 5.22.4 Documentation changes

• OEHasCompressedColorAtoms and OEDeleteCompressedColorAtoms have been documented and are now fully supported.

# 5.23 Shape TK 1.9.6

## 5.23.1 New features

• A new OEHasPerceivedColorAtoms function has been added for determining whether OEAddColorAtoms has already been called on a molecule.

# 5.23.2 Major bug fixes

- OEBestOverlay will no longer cause undefined behavior and frequent crashes, particularly in Java, when more than one OEBestOverlay object is created and destroyed.
- Dummy atoms (atoms with an atomic number of 0) with non-zero radius will no longer cause shape Tanimoto values to exceed 1.0. These dummy atoms are now properly ignored for shape Tanimoto calculations.
- Undefined behavior can now be avoided when handling 32 different types of color atoms.
- Internal refactoring has been performed to improve stability.

# 5.23.3 Minor bug fixes

Examples of using exclusion volumes in a ROCS search were added for C++, Java, and C#.

# 5.24 Shape TK 1.9.5

## 5.24.1 New features

### 5.24.2 Major bug fixes

• OEBestOverlay constructor that takes a molecule will not terminate the process when given a molecule with only hydrogen atoms.

# 5.25 Shape TK 1.9.4

## 5.25.1 Major bug fixes

•  $OECalcVol$  ume will no longer allocate excessive amounts of memory and usually crash for molecules without coordinates.

## 5.25.2 Minor bug fixes

• Removed unbounded stack allocations.

# 5.26 Shape TK 1.9.3

• Minor internal improvements.

# 5.27 Shape TK 1.9.2

# 5.27.1 Minor bug fixes

- A bug has been fixed where OEBOO rientation Subrocs was not properly setting starting positions when the database molecule was larger than the query molecule.
- Fixed a rare invalid memory access from the OEOverlapMethod\_Analytic2 method.

# 5.28 Shape TK 1.9.1

# 5.28.1 Bug fixes

• OEUncompressColorAtoms no longer throws a warning when no color atoms are present.

# 5.29 Shape TK 1.9.0

# 5.29.1 New features

- · OEBOOrientation\_Subrocs has been added as a new starting position method. This method is very similar to OEBOOrientation\_InertialAtHeavyAtoms, except that it automatically uses the heavy atoms and center-of-mass of the larger molecule when determining starting positions.
- OEShapeQueryPublic has been added for reading shape queries. This is an initial public implementation with limited functionality.

# 5.29.2 Major bug fixes

## 5.29.3 Minor bug fixes

- OEBOOrientation\_Subrocs will now be used for highly symmetric molecules instead of random starts.
- OEBOOrientation\_Subrocs and OEBOOrientation\_InertialAtHeavyAtoms use the center-ofmass in addition to the heavy atoms when determining starting positions.

# 5.30 Shape TK 1.8.3

# 5.30.1 New features

• OEColorForceField. Get Types method added to return an iterator of the integer color forcefield types.

# 5.30.2 Minor bug fixes

- OEAddColorAtoms was setting an internal flag incorrectly such that OEHasColorAtoms would return true even if no color atoms were added. This has been fixed.
- OEAddColorAt om corrected to also set internal flags regarding presence of color atoms.
- OEBOOrientation\_InertialAtHeavyAtoms will now use the center-of-mass as a startpoint in addition to all heavy atoms. The constant is an option for OEBestOverlay. Set InitialOrientation.
- OEBOOrientation\_UserInertialStarts will now work with the reference being a grid.

# 5.31 Shape TK 1.8.2

• Internal build system improvements.

# 5.32 Shape TK 1.8.1

## 5.32.1 Bug fixes

- Fixing a crash in  $OECalcVol$  ume when dealing with Zinc and dummy atoms.
- $OECalcVol$  ume will now default to using appropriate Bondi VdW radii when no radii are set on the molecule. This effectively changes the value returned this function most molecules.

# 5.33 Shape TK 1.8.0

## 5.33.1 New features

- Added new functions that will cache the self shape score on a molecule. Analogous to the caching of self color, introduced in 1.7.2, this can speed up repeat shape calculations on the same molecule by not recalculating the self terms.
  - OESetCachedSelfShape
  - OEHasCachedSelfShape
  - OEGetCachedSelfShape
  - OEClearCachedSelfShape
- Updated the functions that cache self color to store work with multi-conformer molecules, storing a self color for each conformer.
- Added two new color force fields, ImplicitMillsDeanNoRings and ExplicitMillsDeanNoRings. These are identical to the existing similarly named force fields, but with no "rings" atom types or interactions.

- Added Has and Delete functions to the API for dealing with compressed color atoms.
- Several of the examples have been updated to count the output better and to use a better sort functor when color is included.
- Add new methods to OEBestOverlayScore to allow access to the transform.
  - OEBestOverlayScore.GetRotMatrix
  - OEBestOverlayScore. GetTranslation

### 5.33.2 Bug fixes

- Added OEGetColorAtoms and OEGetColorParents to Python, Java and C#.
- Fixed a bug where non-deterministic results could sometime occur when using OEBestOverlay and a highly symmetric molecule.
- Fixed calculation of multipoles. Previous versions used a non-irreducible representation of multipoles that is nonstandard. This method now calculates standard multipoles and allow better comparison between the values of two molecules.
- Fixed a missing type in ImplicitMillsDean to match an aldehyde acceptor with or without the explicit proton.
- Fixed a bug where OECalcVolume could crash using a molecule with deleted atoms.

# 5.34 Shape TK 1.7.2

### 5.34.1 New features

- OEAddColorAtoms now has an optional third argument to cause precalculation and caching of the self color. When re-using molecules in multiple comparisons (for example NxN studies), use OEAddColorAtoms once and then OEBestOverlay and OEColorOverlap will use the pre-stored color atoms and self color to speed up the calculations.
- Added a set of functions to manipulate cached self color.
  - OESetCachedSelfColor
  - OEHasCachedSelfColor
  - OEGetCachedSelfColor
  - OEClearCachedSelfColor
- The pair of functions (OEColorAtomsToString and OEStringToColorAtoms) added in v1.7.1 have been renamed to more appropriate names. The new functions are OECOmpressColorAtoms and OEUncompressColorAtoms.

# 5.34.2 Bug fixes

• Fixed a bug where dummy atoms could cause an erroneous result for OECalcVolume.

# 5.35 Shape TK 1.7.1

# 5.35.1 New features

- Added new types in OEBOOrientation. All of these are designed to provide a more deterministic search over the reference molecule for those case where the size of the fit molecule is much smaller than the reference, for example, when trying to match a fragment into part of a reference molecule.
  - OEBOOrientation\_InertialAtHeavyAtoms moves the center of mass of the fit molecule to each reference molecule heavy atom and performs 4 inertial starts at the position. This results in many more starting positions, but provides a more direct way to search over an entire reference molecule, without resorting to random starts.
  - OEBOOrientation\_InertialAtColorAtoms performs a similar search as above, but just moves to the location of each reference molecule color atom.
  - OEBOOrientation\_UserInertialStarts, used in conjunction with OEBestOverlay. Set UserStarts allows the user to pick specific points in space to perform the 4 inertial starts.
- Fixed a bug when calculating Tanimoto while using a grid as the reference object.
- Added more functions to manipulate the color atoms on a molecule. These include the ability to add color atoms one at a time (OEAddColorAtom) and the ability to get an iterator of color atoms from a molecule (OEGetColorAtoms).
- Added a of functions (OEShape:: OEColorAtomsToString and pair OEShape::OEStringToColorAtoms) that allow converting the color atoms of a molecule into a compressed string representation (that is attached to the molecule) and then to restore the actual color atoms from that string.

# 5.35.2 Bug fixes

- · Fixed a bug that could cause a crash when passing an empty molecule into OECalcVolume or OECalcShapeMultipoles.
- Fixed a bug that could cause a crash when passing large molecules to  $OECalcVolume$ .

# 5.36 Shape TK 1.7.0

## 5.36.1 New features

- Color Tanimoto is calculated just like Shape Tanimoto by using the self color scores of each molecule combined with the actual color score. The end result is to better match molecules of the same color, penalizing a molecule for having too much as well as too little color. Color Tversky scores can be calculated as well. We now calculate these extra color scores in *OEColorOverlap* and *OEBestOverlay*.
- OEColorResults now has Tanimoto, Tversky, RefTversky and FitTversky.
- OEBestOverlayScore now has ColorTanimoto, ColorTversky, RefColorTversky, FitColorTversky and adds three new combo scores based on these:

- TanimotoCombo the sum of Shape Tanimoto and Color Tanimoto
- RefTverskyCombo the sum of Ref Shape Tversky and Ref Color Tversky
- FitTverskyCombo the sum of Fit Shape Tversky and Fit Color Tversky
- OEOverlapResults now has Tversky, RefTversky and FitTversky.

### 5.36.2 Bug fixes

- Fixed an internal memory leak in OEColorOverlap/OEBestOverlap color objects.
- Fixed a bug where in some cases the user-supplied value for carbon radius in OEOverlap was ignored.

# 5.37 Shape TK 1.6.2

### 5.37.1 New features

• Added the ability to get the expiration date from OEShapeIsLicensed function.

### 5.37.2 Bug fixes

- Fixed a memory leak in the calculation of self color in OEColorFunc.
- Fixed a bug that prevented pre-colored molecules from being used in OEColorFunc.
- Replace old error messages that just went to stderr and routed all errors and warnings via OEThrow.

# 5.38 Shape TK 1.6.1

This is the first release as part of the consolidated toolkits release.

## 5.38.1 New features

• Added functions to retrieve the version and build date of the library.

## 5.38.2 Bug fixes

- Changed to a stable sort inside OESortOverlayScores to prevent crashes with a very large number of results.
- Fixes to OEOverlap that in some cases could result in slow behavior when internal grids were rebuilt instead of being cached.
- Fix a subtle bug that could result in erroneous behavior if reusing the same  $OEOverLap$  object while changing the fit object from a grid to a molecule or from a molecule to a grid.

# 5.39 Shape TK 1.6

# 5.39.1 New features

· Added new functions to calculate steric volume (OECalcVolume) and steric multipoles (OECalcShapeMultipoles).

# 5.39.2 Bug fixes

- Fixed a bug where OEAddColorAtoms would not correctly add color atoms to a molecule that had the IntType field on atoms filled from a previous calculation. IntType is scratch space on atoms, so OEAddColorAtoms now clears the IntType before adding color atoms to a molecule.
- Changed one of the cation definitions in ImplicitMillsDean force field from the too general ("n:1anaa1") to the more specific ("n:1cncc1").
- Fixed a bug that caused *OEBOOrientation\_AsIs* to not always start from the passed in positions.

# **5.40 Shape TK 1.5**

# 5.40.1 New features

• First release in C++, Java and Python.

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

# **CHAPTER**

# **SEVEN**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

### **CHAPTER**

# **EIGHT**

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

# **8.2 Toolkits and Applications**

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

# **NINE**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                                             | License             |
|-------------------------------|-------------------------------------------------------------------------------------|---------------------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                                | https://            |
| absl-py                       | https://github.com/abseil/abseil-py                                                 | https://            |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                                 | https://            |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                               | https://            |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                               | N/A                 |
| AmberUtils                    | http://ambermd.org                                                                  | N/A                 |
| ambit                         | https://github.com/khimaros/ambit                                                   | https://            |
| amqp                          | https://github.com/celery/py-amqp                                                   | https://            |
| anaconda-anon-usage           | <b>Orion Floes</b>                                                                  | https://            |
| angular                       | https://github.com/angular/angular.js                                               | https://            |
| angular-animate               | https://github.com/angular/angular.js                                               | https://            |
| angular-cache                 | https://github.com/jmdobry/angular-cache                                            | https://            |
| angular-cookies               | https://github.com/angular/angular.js                                               | https://            |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                                    | https://            |
| angular-mocks                 | https://github.com/angular/angular.js                                               | https://            |
| angular-resource              | https://github.com/angular/angular.js                                               | https://            |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                                    | https://            |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                               | https://            |
| angular-ui-router             | https://github.com/angular-ui/ui-router                                             | https://            |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                                  | https://            |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                                        | https://            |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                                            | https://            |
| annotated-types               | https://github.com/annotated-types/annotated-types                                  | https://            |
| anyio                         | https://github.com/agronholm/anyio                                                  | https://            |
| appdirs                       | http://github.com/ActiveState/appdirs                                               | http://             |
| appengine                     | https://google.golang.org/appengine                                                 | https://            |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                                   | https://            |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md                          | https://            |
| Name of Project               | Website                                                                             | License             |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                                | https://            |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                                       | https://            |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                                          | https://            |
| ascii85                       | https://github.com/huandu/node-ascii85                                              | https://            |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                                      | https://            |
| asgiref                       | https://github.com/django/asgiref/                                                  | https://            |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                                 | https://            |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render               | https://            |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers                   | https://            |
| assertions                    | https://github.com/smartystreets/assertions                                         | https://            |
| asttokens                     | https://github.com/gristlabs/asttokens                                              | https://            |
| astunparse                    | https://github.com/simonpercivall/astunparse                                        | https://            |
| async-lru                     | https://github.com/aio-libs/async-lru                                               | https://            |
| async-timeout                 | https://github.com/aio-libs/async-timeout                                           | https://            |
| atk-1.0                       | https://docs.gtk.org/atk/                                                           | https://            |
| atomic                        | https://github.com/uber-go/atomic                                                   | https://            |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                                    | https://            |
| attrs                         | https://www.attrs.org/                                                              | https://            |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                                   | https://            |
| Babel                         | https://github.com/python-babel/babel                                               | https://            |
| backcall                      | https://github.com/takluyver/backcall                                               | https://            |
| backports                     | https://github.com/brandon-rhodes/backports                                         | https://            |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache                             | https://            |
| base62                        | https://github.com/kare/base62                                                      | https://            |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                                      | https://            |
| billiard                      | https://github.com/celery/billiard                                                  | https://            |
| biopython                     | https://biopython.org                                                               | https://            |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https://            |
| bitset                        | https://github.com/willf/bitset                                                     | https://            |
| blas                          | https://www.netlib.org/blas/                                                        | https://            |
| bleach                        | https://github.com/mozilla/bleach                                                   | https://            |
| blessings                     | https://github.com/erikrose/blessings                                               | https://            |
| blinker                       | https://pythonhosted.org/blinker/                                                   | https://            |
| blosc                         | https://github.com/Blosc/python-blosc                                               | https://            |
| blosc2                        | https://github.com/Blosc/python-blosc2                                              | https://            |
| boltons                       | https://github.com/mahmoud/boltons                                                  | https://            |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://            |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://            |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                                      | https://            |
| boto3                         | https://github.com/boto/boto3                                                       | https://            |
| botocore                      | https://github.com/boto/botocore                                                    | https://            |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                              | https://            |
| Brotli                        | https://github.com/google/brotli                                                    | https://            |
| brotli-bin                    | https://github.com/google/brotli                                                    | https://            |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                                | https://            |
| brotlipy                      | https://github.com/python-hyper/brotlipy                                            | https://            |
| bson                          | http://github.com/py-bson/bson                                                      | https://            |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                               | https://            |
| bzip2                         | https://www.bzip.org                                                                | https://            |
| Name of Project               | Website                                                                             | License             |
| c-ares                        | https://github.com/c-ares/c-ares                                                    | https:/             |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/             |
| cached-property               | https://github.com/pydanny/cached-property                                          | https:/             |
| cachetools                    | https://github.com/tkem/cachetools/                                                 | https:/             |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           | https:/             |
| canvas                        | https://github.com/Automattic/node-canvas                                           | https:/             |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              | https:/             |
| celery                        | https://github.com/celery/celery                                                    | https:/             |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         | https:/             |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                           | https:/             |
| cffi                          | https://github.com/python-cffi/cffi                                                 | https:/             |
| cftime                        | https://pypi.org/project/cftime/                                                    | https:/             |
| chardet                       | https://github.com/chardet/chardet                                                  | https:/             |
| charset-normalizer            | https://github.com/ousret/charset_normalizer                                        | https:/             |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             | https:/             |
| click                         | https://palletsprojects.com/p/click/                                                | https:/             |
| click-completion              | https://github.com/click-contrib/click-completion                                   | https:/             |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   | https:/             |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      | https:/             |
| click-repl                    | https://github.com/untitaker/click-repl                                             | https:/             |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            | https:/             |
| cmake                         | https://cmake.org/                                                                  | https:/             |
| colorama                      | https://github.com/tartley/colorama                                                 | https:/             |
| comm                          | https://github.com/ipython/comm                                                     | https:/             |
| compose                       | https://github.com/docker/compose                                                   | https:/             |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        | https:/             |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      | https:/             |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     | https:/             |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/             |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           | https:/             |
| confuse                       | https://github.com/beetbox/confuse                                                  | https:/             |
| contourpy                     | https://github.com/contourpy/contourpy                                              | https:/             |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               | https:/             |
| cryptography                  | https://github.com/pyca/cryptography                                                | https:/             |
| cssselect2                    | https://github.com/Kozea/cssselect2/                                                | https:/             |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           | https:/             |
| cupy-cuda113                  | https://cupy.dev/                                                                   | https:/             |
| curl                          | https://curl.se                                                                     | https:/             |
| cycler                        | https://github.com/matplotlib/cycler                                                | https:/             |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             | https:/             |
| Cython                        | https://cython.org                                                                  | https:/             |
| d3                            | https://github.com/mbostock/d3                                                      | https:/             |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           | https:/             |
| ddsketch                      | http://github.com/datadog/sketches-py                                               | https:/             |
| debugpy                       | https://aka.ms/debugpy                                                              | https:/             |
| decimal                       | https://github.com/shopspring/decimal                                               | https:/             |
| decorator                     | https://github.com/micheles/decorator                                               | https:/             |
| deepdiff                      | https://github.com/seperman/deepdiff                                                | https:/             |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             | https:/             |
| Name of Project               | Website                                                                             | License             |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https:/             |
| dill                          | https://github.com/uqfoundation/dill                                                | https:/             |
| distro                        | Orion Floes                                                                         | https:/             |
| Django                        | https://www.djangoproject.com/                                                      | https:/             |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                    | https:/             |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                   | https:/             |
| django-csp                    | https://github.com/mozilla/django-csp                                               | https:/             |
| django-extensions             | https://github.com/django-extensions/django-extensions                              | https:/             |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                          | https:/             |
| django-redis                  | https://github.com/jazzband/django-redis                                            | https:/             |
| django-taggit                 | https://github.com/jazzband/django-taggit                                           | https:/             |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/             |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                              | https:/             |
| djangorestframework           | https://www.django-rest-framework.org/                                              | https:/             |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                      | https:/             |
| dm-tree                       | https://github.com/deepmind/tree                                                    | https:/             |
| docker-py                     | https://github.com/docker/docker-py/                                                | https:/             |
| docopt                        | https://docopt.org                                                                  | https:/             |
| docutils                      | https://docutils.sourceforge.io                                                     | https:/             |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/             |
| editdistance                  | https://github.com/roy-ht/editdistance                                              | https:/             |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/             |
| einops                        | https://github.com/arogozhnikov/einops                                              | https:/             |
| entrypoints                   | https://github.com/takluyver/entrypoints                                            | https:/             |
| errors                        | https://github.com/pkg/errors                                                       | https:/             |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                              | https:/             |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/             |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         | https:/             |
| executing                     | https://github.com/alexmojaki/executing                                             | https:/             |
| expat                         | https://libexpat.github.io                                                          | https:/             |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                   | https:/             |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 | https:/             |
| fftw                          | https://www.fftw.org                                                                | comm                |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              | https:/             |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/             |
| finufft                       | https://github.com/flatironinstitute/finufft                                        | https:/             |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/             |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               | https:/             |
| flit-core                     | https://github.com/pypa/flit                                                        | https:/             |
| FLTK                          | https://www.fltk.org/index.php                                                      | https:/             |
| fmt                           | https://fmt.dev/latest/index.html                                                   | https:/             |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         | https:/             |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      | https:/             |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       | https:/             |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/             |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            | https:/             |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/             |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/             |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/             |
|                               |                                                                                     | J.                  |
| Name of Project               | Website                                                                             | Licen               |
| fonttools                     | https://github.com/fonttools/fonttools                                              | https:/             |
| freetype                      | https://freetype.org                                                                | https:/             |
| fribidi                       | https://github.com/fribidi/fribidi                                                  | https:/             |
| frozendict                    | <b>Orion Floes</b>                                                                  | https:/             |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                              | https:/             |
| fsmlite                       | https://github.com/tkem/fsmlite                                                     | https:/             |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                           | https:/             |
| funcy                         | https://github.com/Suor/funcy                                                       | https:/             |
| gast                          | https://github.com/serge-sans-paille/gast/                                          | https:/             |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                | https:/             |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             | https:/             |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https:/             |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             | https:/             |
| genproto                      | https://google.golang.org/genproto/googleapis                                       | https:/             |
| geometric                     | https://openbase.com/python/geometric                                               | https:/             |
| giflib                        | https://giflib.sourceforge.net                                                      | https:/             |
| glib                          | https://docs.gtk.org/glib/                                                          | https:/             |
| <b>GLM</b> Library            | https://github.com/g-truc/glm                                                       | https:/             |
| gls                           | https://github.com/jtolds/gls                                                       | https:/             |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           | https:/             |
| go-connections                | https://github.com/docker/go-connections                                            | https:/             |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            | https:/             |
| go-getter                     | https://github.com/hashicorp/go-getter                                              | https:/             |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             | https:/             |
| go-ini                        | https://github.com/go-ini/ini                                                       | https:/             |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             | https:/             |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         | https:/             |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           | https:/             |
| go-ole                        | https://github.com/go-ole/go-ole                                                    | https:/             |
| go-pg                         | https://github.com/go-pg/pg                                                         | https:/             |
| go-redis                      | https://github.com/go-redis/redis/v8                                                | https:/             |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                            | https:/             |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                            | https:/             |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                              |                     |
|                               | https://github.com/mitchellh/go-testing-interface                                   | https:/             |
| go-testing-interface          | https://github.com/docker/go-units                                                  | https:/             |
| go-units<br>go-version        | https://github.com/hashicorp/go-version                                             | https:/             |
|                               | https://github.com/mattn/go-zglob                                                   | https:/             |
| go-zglob                      |                                                                                     | https:/             |
| go.opencensus                 | https://go.opencensus.io                                                            | https:/             |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                | https:/             |
| goconvey                      | https://github.com/smartystreets/goconvey                                           | https:/             |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                       | https:/             |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       | https:/             |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https:/             |
| google-cloud-go               | https://cloud.google.com/go                                                         | https:/             |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 | https:/             |
| google-pasta                  | https://github.com/google/pasta                                                     | https:/             |
| google.golang.org/api         | https://google.golang.org/api                                                       | https:/             |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  | https:/             |
| Name of Project               | Website                                                                             | J)<br>Licen         |
| gorilla websocket             | https://github.com/gorilla/websocket                                                | https:/             |
| graphite2                     | https://github.com/silnrsi/graphite                                                 | https:/             |
| graphviz                      | https://graphviz.org/                                                               | https:/             |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          | https:/             |
| groupcache                    | https://github.com/golang/groupcache                                                | https:/             |
| grpc                          | https://google.golang.org/grpc                                                      | https:/             |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        | https:/             |
| grpcio                        | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/             |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/             |
| gts                           | https://sourceforge.net/projects/gts/                                               | https:/             |
| h5py                          | https://www.h5py.org                                                                | https:/             |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                | https:/             |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           | https:/             |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/             |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/             |
| he                            | https://github.com/mathiasbynens/he                                                 | https:/             |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      | https:/             |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         | https:/             |
| htslib                        | https://www.htslib.org                                                              | https:/             |
| humanize                      | https://github.com/jmoiron/humanize                                                 | https:/             |
| icu                           | https://github.com/unicode-org/icu                                                  | https:/             |
| idna                          | https://github.com/kjd/idna                                                         | https:/             |
| imageio                       | https://github.com/imageio/imageio                                                  | https:/             |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           | https:/             |
| <b>ImmuneBuilder</b>          | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/             |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        | https:/             |
| importlib_resources           | https://github.com/python/importlib_resources                                       | https:/             |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/             |
| inflection                    | https://github.com/jinzhu/inflection                                                | https:/             |
| ini.v1                        | https://gopkg.in/ini.v1                                                             | https:/             |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             | https:/             |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         | https:/             |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            | https:/             |
| ipykernel                     | https://ipython.org                                                                 | https:/             |
| ipython                       | https://ipython.org                                                                 |                     |
| ipython-genutils              | http://ipython.org                                                                  | https:/<br>https:/  |
| ipywidgets                    | http://jupyter.org                                                                  | https:/             |
| isodate                       | https://github.com/gweis/isodate/                                                   |                     |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         | https:/<br>https:/  |
| jax                           | https://github.com/google/jax                                                       |                     |
| jaxlib                        | https://github.com/google/jax                                                       | https:/             |
|                               | https://jedi.readthedocs.io/en/latest/                                              | https:/             |
| jedi                          |                                                                                     | https:/             |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                | https:/             |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             | https:/             |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            | https:/             |
| jpeg                          | https://www.ijg.org                                                                 | https:/             |
| json5                         | https://github.com/dpranke/pyjson5                                                  | https:/             |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         | https:/             |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    | https:/             |
| Name of Project               | Website                                                                             | License             |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:/             |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https:/             |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https:/             |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:/             |
| jstat                         | https://github.com/jstat/jstat                                                      | https:/             |
| jupyter-client                | https://jupyter.org                                                                 | https:/             |
| jupyter-core                  | https://jupyter.org                                                                 | https:/             |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https:/             |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:/             |
| jupyter-server                | http://jupyter.org                                                                  | https:/             |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:/             |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:/             |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:/             |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:/             |
| jupyter_client                | http://jupyter.org                                                                  | https:/             |
| jupyter_core                  | http://jupyter.org                                                                  | https:/             |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https:/             |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:/             |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:/             |
| keras                         | https://github.com/keras-team/keras                                                 | https:/             |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:/             |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:/             |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:/             |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:/             |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:/             |
| kombu                         | https://kombu.readthedocs.io                                                        | https:/             |
| $\overline{\text{krb5}}$      | https://web.mit.edu/kerberos/                                                       | https:/             |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:/             |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:/             |
| lcms2                         | https://www.littlecms.com                                                           | https:/             |
| lerc                          | https://github.com/Esri/lerc                                                        | https:/             |
| libarchive                    | http://www.libarchive.org                                                           | https:/             |
| libblas                       | https://www.netlib.org/blas/                                                        | https:/             |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:/             |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:/             |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https:/             |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                 |
| libclang                      | <b>Orion Floes</b>                                                                  | https:/             |
| libcurl                       | https://curl.se/libcurl/                                                            | https:/             |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:/             |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:/             |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:/             |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://             |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:/             |
| libffi                        | https://github.com/libffi/libffi                                                    | https:/             |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:/             |
| libgd                         | https://libgd.github.io                                                             | https:/             |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:/             |
|                               |                                                                                     | J,                  |
| Name of Project               | Website                                                                             | Licen               |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https:/             |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https:/             |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https:/             |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https:/             |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https:/             |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/             |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https:/             |
| libopenblas                   | https://www.openblas.net/                                                           | https:/             |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https:/             |
| libpq                         | https://www.postgresql.org/                                                         | https:/             |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https:/             |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https:/             |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https:/             |
| libtiff                       | https://www.libtiff.org/                                                            | https:/             |
| libtrust                      | https://github.com/docker/libtrust                                                  | https:/             |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https:/             |
| libuv                         | https://github.com/libuv/libuv                                                      | https:/             |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https:/             |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https:/             |
| libxc                         | https://www.tddft.org/programs/libxc/                                               |                     |
| libxcb                        | https://xcb.freedesktop.org                                                         | https:/             |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https:/             |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https:/             |
|                               | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https:/             |
| libxslt                       |                                                                                     | https:/             |
| libzlib                       | https://zlib.net                                                                    | https:/             |
| lime                          | https://github.com/marcoter/lime                                                    | https:/             |
| $\overline{\text{lit}}$       | http://llvm.org                                                                     | https:/             |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https:/             |
| <b>Ilymlite</b>               | http://llvmlite.readthedocs.io                                                      | https:/             |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https:/             |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https:/             |
| logrus                        | https://github.com/sirupsen/logrus                                                  | https:/             |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/             |
| lxml                          | https://lxml.de                                                                     | https:/             |
| $1z4-c$                       | https://www.lz4.org/                                                                | https:/             |
| markdown                      | https://github.com/evilstreak/markdown-js                                           | https:/             |
| markdown-it-py                | <b>Orion Floes</b>                                                                  | https:/             |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https:/             |
| matplotlib                    | https://matplotlib.org                                                              | https:/             |
| matplotlib-base               | https://matplotlib.org                                                              | https:/             |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https:/             |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/             |
| mdtraj                        | https://www.mdtraj.org/                                                             | https:/             |
| mdurl                         | <b>Orion Floes</b>                                                                  | https:/             |
| menuinst                      | <b>Orion Floes</b>                                                                  | https:/             |
| mergo                         | https://github.com/imdario/mergo                                                    | https:/             |
| mistune                       | https://github.com/lepture/mistune                                                  | https:/             |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https:/             |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https:/             |
|                               |                                                                                     |                     |
| Name of Project               | Website                                                                             | License             |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https:/             |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https:/             |
| ml-dtypes                     | Orion Floes                                                                         | https:/             |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https:/             |
| moment                        | https://github.com/moment/moment                                                    | https:/             |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https:/             |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https:/             |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https:/             |
| mpmath                        | http://mpmath.org/                                                                  | https:/             |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https:/             |
| msgpack                       | https://msgpack.org/                                                                | https:/             |
| multidict                     | https://github.com/aio-libs/multidict                                               | https:/             |
| multierr                      | https://go.uber.org/multierr                                                        | https:/             |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https:/             |
| munkres                       | https://software.clapper.org/munkres/                                               | https:/             |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https:/             |
| namex                         | Orion Floes                                                                         | https:/             |
| nbclassic                     | http://jupyter.org                                                                  | https:/             |
| nbclient                      | https://jupyter.org                                                                 | https:/             |
| nbconvert                     | https://jupyter.org                                                                 | https:/             |
| nbformat                      | http://jupyter.org                                                                  | https:/             |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https:/             |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https:/             |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/             |
| netCDF4                       | https://github.com/Unidata/netcdf4-python                                           | https:/             |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https:/             |
| networkx                      | https://networkx.org                                                                | https:/             |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https:/             |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https:/             |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https:/             |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https:/             |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https:/             |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/             |
| nodejs                        | https://nodejs.org/en/                                                              | https:/             |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https:/             |
| notebook                      | http://jupyter.org                                                                  | https:/             |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https:/             |
| notebook_shim                 | http://jupyter.org                                                                  | https:/             |
| numba                         | https://numba.pydata.org                                                            | https:/             |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https:/             |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https:/             |
| numpy                         | https://numpy.org                                                                   | https:/             |
| numpy-base                    | https://numpy.org                                                                   | https:/             |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/             |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/             |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/             |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/             |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/             |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/             |
| Name of Project               | Website                                                                             | License             |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https://            |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https://            |
| Oat++                         | https://oatpp.io/                                                                   | https://            |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https://            |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https://            |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https://            |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https://            |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https://            |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https://            |
| OpenFF                        | https://openforcefield.org/                                                         | https://            |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https://            |
| openff-forcefields            | https://openforcefield.org                                                          | https://            |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https://            |
| openff-models                 | https://github.com/openforcefield/openff-models                                     | https://            |
| openff-toolkit                | https://openforcefield.org                                                          | https://            |
| openff-toolkit-base           | https://openforcefield.org                                                          | https://            |
| openff-units                  | https://github.com/openforcefield/openff-units                                      | https://            |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https://            |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https://            |
| openldap                      | https://www.openldap.org/software/repo.html                                         | https://            |
| OpenMM                        | https://openmm.org                                                                  | https://            |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https://            |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https://            |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https://            |
| openssl                       | https://www.openssl.org                                                             | https://            |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https://            |
| OptKing                       | https://github.com/psi-rking/optking                                                | https://            |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https://            |
| overrides                     | https://github.com/mkorpela/overrides                                               | https://            |
| packaging                     | https://github.com/pypa/packaging                                                   | https://            |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https://            |
| pandas                        | https://pandas.pydata.org                                                           | https://            |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https://            |
| Name of Project               | Website                                                                             | License             |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https:/             |
| pango                         | https://pango.gnome.org                                                             | https:/             |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https:/             |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https:/             |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https:/             |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https:/             |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https:/             |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https:/             |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https:/             |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/             |
| pcre                          | https://www.pcre.org                                                                | https:/             |
| pcre2                         | https://www.pcre.org                                                                | https:/             |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https:/             |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https:/             |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https:/             |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https:/             |
| pgio                          | https://github.com/jackc/pgio                                                       | https:/             |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https:/             |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https:/             |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https:/             |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https:/             |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https:/             |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https:/             |
| Pillow                        | https://python-pillow.org                                                           | https:/             |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https:/             |
| pip                           | https://pip.pypa.io/                                                                | https:/             |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https:/             |
| pixman                        | https://pixman.org                                                                  | https:/             |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https:/             |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https:/             |
| plotly                        | https://plotly.com/python/                                                          | https:/             |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https:/             |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https:/             |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/             |
| pooch                         | https://github.com/fatiando/pooch                                                   | https:/             |
| pox                           | https://github.com/uqfoundation/pox                                                 | https:/             |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https:/             |
| pq                            | https://github.com/lib/pq                                                           | https:/             |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https:/             |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https:/             |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/             |
| protobuf                      | https://google.golang.org/protobuf                                                  | https:/             |
| psi4                          | https://psicode.org                                                                 | https:/             |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https:/             |
| psycopg2                      | https://psycopg.org/                                                                | https:/             |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https:/             |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https:/             |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/             |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http://             |
| Name of Project               | Website                                                                             | License             |
| py                            | https://py.readthedocs.io/en/latest/                                                | https:/             |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             | https:/             |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   | https:/             |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           | https:/             |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  | https:/             |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/             |
| pycosat                       | https://github.com/conda/pycosat                                                    | https:/             |
| pycparser                     | https://github.com/eliben/pycparser                                                 | https:/             |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 | https:/             |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           | https:/             |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                | https:/             |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                | https:/             |
| Pygments                      | https://pygments.org                                                                | https:/             |
| pygraphviz                    | https://pygraphviz.github.io                                                        | https:/             |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            | https:/             |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        | https:/             |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  | https:/             |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   | https:/             |
| pymbar                        | https://pymbar.org                                                                  | https:/             |
| pyOpenSSL                     | https://pyopenssl.org/                                                              | https:/             |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/             |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    | https:/             |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 | https:/             |
| pysam                         | https://github.com/pysam-developers/pysam                                           | https:/             |
| PySocks                       | https://github.com/Anorov/PySocks                                                   | https:/             |
| pytables                      | https://www.pytables.org                                                            | https:/             |
| python                        | https://www.python.org/                                                             | https:/             |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          | https:/             |
| python-constraint             | https://github.com/python-constraint/python-constraint                              | https:/             |
| python-dateutil               | https://dateutil.readthedocs.io                                                     | https:/             |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         | https:/             |
| python-ldap                   | https://www.python-ldap.org/                                                        | https:/             |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            | https:/             |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 | https:/             |
| pytz                          | https://pythonhosted.org/pytz                                                       | https:/             |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/             |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  | https:/             |
| <b>PyYAML</b>                 | https://pyyaml.org/                                                                 | https:/             |
| pyyml                         | No longer available                                                                 | No longer available |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             | https:/             |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               | https:/             |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  | https:/             |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        | https:/             |
| ramda                         | https://github.com/ramda/ramda                                                      | https:/             |
| rapidjson                     | https://rapidjson.org/                                                              | https:/             |
| rdkit                         | https://www.rdkit.org                                                               | https:/             |
| re2                           | https://github.com/google/re2                                                       | https:/             |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             | https:/             |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             | https:/             |
| Name of Project               | Website                                                                             | License             |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https:/             |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https:/             |
| reportlab                     | https://www.reportlab.com                                                           | https:/             |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https:/             |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https:/             |
| requests                      | https://requests.readthedocs.io                                                     | https:/             |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https:/             |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https:/             |
| resumable                     | https://github.com/stevvooe/resumable                                               | https:/             |
| retrying                      | https://github.com/rholder/retrying                                                 | https:/             |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https:/             |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https:/             |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https:/             |
| rich                          | Orion Floes                                                                         | https:/             |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https:/             |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https:/             |
| rsa                           | https://stuvel.eu/rsa                                                               | https:/             |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/             |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/             |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https:/             |
| sasl                          | https://mellium.im/sasl                                                             | https:/             |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https:/             |
| scikit-image                  | https://scikit-image.org                                                            | https:/             |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https:/             |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/             |
| scipy                         | https://scipy.org                                                                   | https:/             |
| seaborn                       | https://seaborn.pydata.org                                                          | https:/             |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https:/             |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https:/             |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https:/             |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https:/             |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https:/             |
| sh                            | https://github.com/amoffat/sh                                                       | https:/             |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https:/             |
| simint                        | https://www.bennyp.org/research/simint/                                             | https:/             |
| six                           | https://github.com/benjaminp/six                                                    | https:/             |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https:/             |
| snappy                        | https://github.com/google/snappy                                                    | https:/             |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https:/             |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https:/             |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https:/             |
| spglib                        | Orion Floes                                                                         | https:/             |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https:/             |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/             |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/             |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/             |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/             |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/             |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/             |
| Name of Project               | Website                                                                             | License             |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          | https://            |
| sqlite                        | https://sqlite.org/index.html                                                       | https://            |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            | https://            |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             | https://            |
| starfile                      | https://github.com/alisterburt/starfile                                             | https://            |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          | https://            |
| structlog                     | https://www.structlog.org/                                                          | https://            |
| svglib                        | https://github.com/deeplook/svglib                                                  | https://            |
| sympy                         | https://sympy.org                                                                   | https://            |
| tables                        | https://www.pytables.org/                                                           | https://            |
| tabulate                      | https://github.com/astanin/python-tabulate                                          | https://            |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                | https://            |
| tenacity                      | https://github.com/jd/tenacity                                                      | https://            |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           | https://            |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           | https://            |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           | https://            |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            | https://            |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             | https://            |
| tensorflow-io-gcs-filesystem  | Orion Floes                                                                         | https://            |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           | https://            |
| termcolor                     | https://github.com/hugovk/termcolor                                                 | https://            |
| terminado                     | https://github.com/jupyter/terminado                                                | https://            |
| testpath                      | https://github.com/jupyter/testpath                                                 | https://            |
| textangular                   | https://github.com/fraywing/textAngular                                             | https://            |
| tf_keras                      |                                                                                     | https://            |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             | https://            |
| three                         | https://github.com/mrdoob/three.js                                                  | https://            |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                | https://            |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  | https://            |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             | https://            |
| tk                            | https://www.tcl.tk/                                                                 | https://            |
| toml                          | https://github.com/toml-lang/toml                                                   | https://            |
| tomli                         | https://github.com/hukkin/tomli                                                     | https://            |
| toolz                         | https://github.com/pytoolz/toolz                                                    | https://            |
| torch                         | https://pytorch.org/                                                                | https://            |
| tornado                       | https://www.tornadoweb.org                                                          | https://            |
| tqdm                          | https://github.com/tqdm/tqdm                                                        | https://            |
| tracy                         | https://github.com/gear-genomics/tracy                                              | https://            |
| traitlets                     | https://github.com/ipython/traitlets                                                | https://            |
| triton                        | https://github.com/openai/triton/                                                   | https://            |
| truststore                    | Orion Floes                                                                         | https://            |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               | https://            |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             | https://            |
| twine                         | https://github.com/pypa/twine                                                       | https://            |
| twinj uuid                    | https://github.com/twinj/uuid                                                       | https://            |
| types                         | https://github.com/babel/babel                                                      | https://            |
| typescript                    | https://github.com/Microsoft/TypeScript                                             | https://            |
| typing_extensions             | https://github.com/python/typing                                                    | https://            |
| tzdata                        | https://github.com/python/tzdata                                                    | https://            |
| Name of Project               | Website                                                                             | License             |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | https://            |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | https://            |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | https://            |
| uritools                      | https://github.com/tkem/uritools/                                                   | https://            |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | https://            |
| vine                          | https://github.com/celery/vine                                                      | https://            |
| vue                           | https://github.com/vuejs/vue                                                        | https://            |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | https://            |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | https://            |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | https://            |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | https://            |
| westpa                        | Orion Floes                                                                         | https://            |
| wheel                         | https://github.com/pypa/wheel                                                       | https://            |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | https://            |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | https://            |
| wsutil                        | https://github.com/yhat/wsutil                                                      | https://            |
| x/lint                        | https://golang.org/x/lint                                                           | https://            |
| x/mod                         | https://golang.org/x/mod/semver                                                     | https://            |
| x/net                         | https://golang.org/x/net                                                            | https://            |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | https://            |
| x/sys                         | https://golang.org/x/sys                                                            | https://            |
| x/text                        | https://golang.org/x/text                                                           | https://            |
| x/tools                       | https://golang.org/x/tools                                                          | https://            |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | https://            |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                               | https://            |
| xlrd                          | https://github.com/python-excel/xlrd                                                | https://            |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | https://            |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | https://            |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https://            |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https://            |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https://            |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https://            |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https://            |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https://            |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https://            |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https://            |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https://            |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https://            |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https://            |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https://            |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | https://            |
| xz                            | https://github.com/ulikunitz/xz                                                     | https://            |
| yaml                          | https://pyyaml.org/                                                                 | https://            |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  | https://            |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | https://            |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | https://            |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | https://            |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | https://            |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | Commercial          |
| Name of Project               | Website                                                                             | License             |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                 |
| zap                           | https://go.uber.org/zap                                                             | https://            |
| zipp                          | https://github.com/jaraco/zipp                                                      | https://            |
| zlib                          | https://zlib.net/                                                                   | https://            |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https://            |
| zstd                          | https://facebook.github.io/zstd/                                                    | https://            |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https://            |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https://            |

https://www.gnu.org/software/libiconv/

libiconv

https:/

# **9.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses **GNU** Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

# 9.1.1 GCC RUNTIME LIBRARY EXCEPTION

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

# 9.1.2 GNU GENERAL PUBLIC LICENSE

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

### See also:

• http://www.gnu.org/licenses/gpl.txt

# **INDEX**

# A

AddColorer OEShape:: OEColorForceField, 63 AddColorGaussian OEShape:: OEShapeQuery, 137 AddColorGaussians OEShape:: OEShapeOuery, 137 AddCutoff OEShape:: OEROCSOptions, 123 AddInteraction OEShape:: OEColorForceField, 63 AddMolecule OEShape:: OEROCS, 122 AddScore OEShape:: OEBestOverlayResults, 57 OEShape:: OEROCSResult, 128 AddShapeGaussian OEShape:: OEShapeQuery, 137 AddType OEShape:: OEColorForceField, 63

# B

```
besthit.py
   Example Code, 21
BestOverlay
   OEShape:: OEFlexiOverlay, 79
   OEShape:: OEMultiRefOverlay, 98
   OEShape:: OEOverlay, 112
```

# $\mathcal{C}$

```
Clear
   OEShape:: OEBestOverlayResults, 57
   OEShape:: OEColorForceField. 63
   OEShape:: OEShapeQuery, 137
ClearColorForceField
   OEShape:: OEBestOverlay, 160
ClearColorGaussians
   OEShape:: OEShapeQuery, 137
ClearCutoffs
   OEShape:: OEROCSOptions, 124
ClearInteractions
   OEShape:: OEColorForceField, 64
```

ClearMolecule OEShape:: OEShapeQuery, 138 ClearMolecules OEShape:: OEROCS, 122 ClearShapeGaussians OEShape:: OEShapeQuery, 138 ClearShapeGrid OEShape:: OEShapeQuery, 138 ClearStartPoints OEShape:: OECartesianStarts, 61 ClearStarts OEShape:: OEQuatStarts, 117 ClearUserStarts OEShape:: OEBestOverlay, 160 coloroverlap.py Example Code, 15 ColorScore OEShape:: OEColorOverlap, 166 colorscore.py Example Code, 16 Constructor OEShape:: OEFlexiOverlapOptions, 74 OEShape:: OEFlexiOverlapResults, 77 OEShape:: OEFlexiOverlay, 78 OEShape:: OEFlexiOverlayOptions, 79 OEShape:: OEOverlapPrepOptions, 105 Constructors OEShape:: OEAnalyticColorFunc, 52 OEShape:: OEAnalyticOptions, 53 OEShape:: OEAnalyticShapeFunc, 55 OEShape:: OEAsIsStarts, 56 OEShape:: OEAtAtomStarts, 57 OEShape:: OEBestOverlay, 160 OEShape:: OEBestOverlayResults, 57 OEShape:: OEBestOverlayScore, 59 OEShape:: OECartesianStarts, 60 OEShape:: OEColorFFParameter, 62 OEShape:: OEColorForceField, 63 OEShape:: OEColorOptions, 66 OEShape:: OEColorOverlap, 165 OEShape:: OEColorResults, 167 OEShape:: OEColorTanimotoCutoff, 68

```
OEShape:: OEExactColorFunc. 68
   OEShape:: OEExactShapeFunc, 71
   OEShape:: OEFitColorTverskyCutoff, 71
   OEShape:: OEFitTverskyComboCutoff, 72
   OEShape:: OEFitTverskyCutoff, 72
   OEShape:: OEGridColorFunc, 82
   OEShape:: OEGridShapeFunc, 84
   OEShape:: OEHermite, 85
   OEShape:: OEHermiteOptions, 86
   OEShape:: OEHermiteShapeFunc, 89
   OEShape:: OEHighestTverskyCombo, 95
   OEShape:: OEInertialStarts, 96
   OEShape:: OEIsColorAtomPred, 97
   OEShape:: OEMultiRefOverlay, 98
   OEShape:: OEOverlap, 168
   OEShape:: OEOverlapCutoff, 99
   OEShape:: OEOverlapFunc, 101
   OEShape:: OEOverlapPrep, 103
   OEShape:: OEOverlapResults, 108
   OEShape:: OEOverlay, 111
   OEShape:: OEOverlayOptions, 113
   OEShape:: OEQuatStarts, 117
   OEShape:: OERandomStarts, 120
   OEShape:: OERefColorTverskyCutoff,
       118
   OEShape:: OERefTverskyComboCutoff,
       118
   OEShape:: OERefTverskyCutoff, 119
   OEShape:: OEROCS, 121
   OEShape:: OEROCSOptions, 123
   OEShape:: OEROCSResult, 127
   OEShape:: OEShapeGridOptions, 130
   OEShape:: OEShapeOptions, 131
   OEShape:: OEShapeQuery, 136
   OEShape:: OEShapeOueryPublic.171
   OEShape:: OESubrocsStarts, 142
   OEShape:: OETanimotoComboCutoff, 143
   OEShape:: OETanimotoCutoff, 143
CreateCopy
   OEShape:: OEHighestColorTanimoto, 90
   OEShape:: OEHighestComboScore, 168
   OEShape:: OEHighestFitColorTversky,
       Q<sub>1</sub>OEShape:: OEHighestFitTversky, 91
   OEShape:: OEHighestFitTverskyCombo,
       92
   OEShape:: OEHighestOverlap, 92
   OEShape:: OEHighestRefColorTversky,
       Q<sub>3</sub>OEShape:: OEHighestRefTversky, 93
   OEShape:: OEHighestRefTverskyCombo,
       93
   OEShape:: OEHighestScaledColor, 94
   OEShape:: OEHighestTanimoto, 94
```

```
OEShape:: OEHighestTanimotoCombo, 95
   OEShape:: OEHighestTverskyCombo, 95
   OEShape:: OEIsColorAtomPred, 97
   OEShape:: OEOverlayScoreCutoff, 116
   OEShape:: OEStarts, 134
CreateGrid
   OEShape:: OEHermite, 85
createquery.py
   Example Code, 31
```

# D

```
DeleteColorGaussian
   OEShape:: OEShapeQuery, 138
DeleteShapeGaussian
   OEShape:: OEShapeQuery, 138
```

# E

```
Example Code
   besthit.py.21
   coloroverlap.py, 15
   colorscore.py, 16
   createquery.py, 31
   excludevolume.py, 47
   flexi_best_overlay.py, 42
   flexi_overlay.py, 40
   hermite-expansion.py, 35
   hermite-tanimoto.py, 37
   multicorebestoverlay.py, 26
   nxnshape.py, 44
   overlapcolor.py, 19
   overlapquery.py, 32
   overlayallres.py, 27
   overlaybestres.py, 24
   overlaystruct.py, 29
   rescore.py, 14
   shapeprops.py, 45
   simpleoverlap.py, 13
   tophits.py, 22
   tophitsconf.py, 23
   tophitsquery.py, 33
   usercolor.py, 18
excludevolume.py
   Example Code, 47
```

# F

flexi\_best\_overlay.py Example Code, 42 flexi\_overlay.py Example Code, 40

# G

GetAllColor OEShape:: OEColorOverlap, 166 GetAnalyticOptions

OEShape:: OEAnalyticColorFunc. 52 OEShape:: OEAnalyticShapeFunc, 55 GetAssignBondiRadii OEShape:: OEOverlapPrep, 104 OEShape:: OEOverlapPrepOptions, 106 GetAssignColor OEShape:: OEOverlapPrep, 104 OEShape:: OEOverlapPrepOptions, 106 GetAtomStrength OEShape:: OEShapeQueryBase, 140 GetCarbonRadius OEShape:: OEBestOverlay, 160 OEShape:: OEOverlap, 168 OEShape:: OEShapeOptions, 132 GetCoefficients OEShape:: OEHermite, 85 GetColorForceField OEShape:: OEColorOptions. 66 OEShape:: OEOverlapPrep, 104 OEShape:: OEOverlapPrepOptions, 106 OEShape:: OEShapeQueryBase, 140 OEShape:: OEShapeQueryPublic, 171 GetColorFunc OEShape:: OEOverlapFunc, 101 GetColorFuncType OEShape:: OEFlexiOverlapOptions, 74 OEShape:: OEOverlayOptions, 114 GetColorGaussians OEShape:: OEShapeQueryBase, 140 GetColorOptions OEShape:: OEColorFunc, 66 OEShape:: OEFlexiOverlapOptions, 75 OEShape:: OEOverlayOptions, 114 GetColorScore OEShape:: OEOverlapResults, 109 GetColorTanimoto OEShape:: OEOverlapResults, 109 GetColorTversky OEShape:: OEOverlapResults, 109 GetCompositeMolecule OEShape:: OEShapeQueryBase, 141 GetConfsPerHit OEShape:: OEROCSOptions, 124 GetDerivativeType OEShape:: OEShapeGridOptions, 131 GetDuplicateDistance OEShape:: OEOverlapPrepOptions, 106 GetExpType OEShape:: OEAnalyticOptions, 53 GetFitColorTversky OEShape:: OEOverlapResults, 109 GetFitConfIdx OEShape:: OEBestOverlayScore, 59 GetFitHermiteOptions

OEShape:: OEHermiteShapeFunc. 90 GetFitSelfColor OEShape:: OEOverlapResults, 109 GetFitSelfOverlap OEShape:: OEOverlapResults, 109 GetFitTversky OEShape:: OEColorResults, 167 OEShape:: OEOverlapResults, 109 GetFitTverskyCombo OEShape:: OEOverlapResults, 110 GetFlexiOverlapOptions OEShape:: OEFlexiOverlayOptions, 80 GetForceField OEShape:: OEFlexiOverlapOptions, 74 GetGridOptions OEShape:: OEGridColorFunc, 82 OEShape:: OEGridShapeFunc, 84 GetGridSpacing OEShape:: OEOverlap, 168 OEShape:: OEShapeGridOptions, 131 GetHarmonic OEShape:: OEFlexiOverlapOptions, 74 GetInitialOrientation OEShape:: OEBestOverlay, 160 GetInternalEnergy OEShape:: OEFlexiOverlapResults, 77 GetLambdaX OEShape:: OEHermiteOptions, 86 GetLambdaY OEShape:: OEHermiteOptions, 87 GetLambdaZ OEShape:: OEHermiteOptions, 87 GetMaxHits OEShape:: OEROCSOptions, 124 GetMaxOptSteps OEShape:: OEFlexiOverlayOptions, 80 OEShape:: OEOverlayOptions, 114 GetMaxRandomTranslation OEShape:: OEBestOverlay, 160 OEShape:: OERandomStarts, 120 GetMethod OEShape:: OEBestOverlay, 161 OEShape:: OEOverlap, 169 GetMinimizeType OEShape:: OEBestOverlay, 161 GetMolecule OEShape:: OEShapeQueryBase, 141 GetMultiplier OEShape:: OEColorOptions, 67 GetNPolyMax OEShape:: OEHermiteOptions, 87 GetNumBestHits OEShape:: OEROCSOptions, 124 GetNumOfStarts

OEShape:: OEStarts, 134 GetNumRandomStarts OEShape:: OEBestOverlay, 161 OEShape:: OERandomStarts, 120 GetNumStartPoints OEShape:: OECartesianStarts, 61 GetNumUserStarts OEShape:: OEBestOverlay, 161 GetOptions OEShape:: OEHermite, 85 GetOverlap OEShape:: OEOverlapResults, 110 GetOverlapFunc OEShape:: OEFlexiOverlapOptions, 75 OEShape:: OEOverlayOptions, 114 GetOverlayConf OEShape:: OEROCSResult, 128 GetOverlayConfs OEShape:: OEROCSResult, 128 GetOverlayOptions OEShape:: OEMultiRefOverlay, 98 OEShape:: OEOverlay, 112 OEShape:: OEROCSOptions, 124 GetPerformPrep OEShape:: OEROCSOptions, 124 GetProxyGridCutoff OEShape:: OEAnalyticOptions, 53 GetRadiiApproximation OEShape:: OEBestOverlay, 161 OEShape:: OEOverlap, 169 OEShape:: OEShapeOptions, 132 GetRandomSeed OEShape:: OEBestOverlay, 161 OEShape:: OERandomStarts, 120 GetRankPredicate OEShape:: OEROCSOptions, 125 GetRefColorTversky OEShape:: OEOverlapResults, 110 GetRefConfIdx OEShape:: OEBestOverlayScore, 59 GetRefGrid OEShape:: OEBestOverlay, 161 GetRefHermiteOptions OEShape:: OEHermiteShapeFunc, 90 GetRefMol OEShape:: OEBestOverlay, 162 GetRefSelfColor OEShape:: OEBestOverlay, 162 OEShape:: OEOverlapResults, 110 GetRefSelfOverlap OEShape:: OEOverlapResults, 110 GetRefSymmetry OEShape:: OEBestOverlay, 162 GetRefTversky

---

OEShape:: OEColorResults, 167 OEShape:: OEOverlapResults, 110 GetRefTverskyCombo OEShape:: OEOverlapResults, 110 GetRemoveDuplicate OEShape:: OEOverlapPrepOptions, 106 GetRigidOverlay OEShape:: OEFlexiOverlayOptions, 80 GetRigidOverlayOptions OEShape:: OEFlexiOverlayOptions, 80 GetROCSOptions OEShape:: OEROCS, 122 GetRotMatrix OEShape:: OEBestOverlayScore, 59 GetScores OEShape:: OEBestOverlayResults, 58 GetScoreType OEShape:: OEColorOptions. 67 OEShape:: OEShapeOptions, 132 GetSelfColor OEShape:: OEColorOverlap, 166 GetSelfOverlap OEShape:: OEHermite, 85 GetShapeFunc OEShape:: OEOverlapFunc, 101 GetShapeFuncType OEShape:: OEFlexiOverlapOptions, 74 OEShape:: OEOverlayOptions, 114 GetShapeGaussians OEShape:: OEShapeQueryBase, 141 GetShapeGrid OEShape:: OEShapeQueryBase, 141 GetShapeOptions OEShape:: OEFlexiOverlapOptions, 75 OEShape:: OEOverlayOptions, 114 OEShape:: OEShapeFunc, 129 GetStartPoints OEShape:: OECartesianStarts, 61 GetStarts OEShape:: OEOverlayOptions, 115 OEShape:: OEStarts, 134 GetSymmetryThreshold OEShape:: OEBestOverlay, 162 OEShape:: OEInertialStarts, 97 GetTanimoto OEShape:: OEColorResults, 167 OEShape:: OEOverlapResults, 111 GetTanimotoCombo OEShape:: OEOverlapResults, 111 GetTitle OEShape:: OEColorForceField, 64 OEShape:: OEShapeQueryBase, 141 OEShape:: OEShapeQueryPublic, 171 GetTranslation

OEShape:: OEBestOverlayScore, 59 GetTversky OEShape:: OEColorResults, 167 OEShape:: OEOverlapResults, 111 GetType OEShape:: OEColorForceField, 64 GetTypeName OEShape:: OEColorForceField, 64 GetTypes OEShape:: OEColorForceField, 64 GetUseHydrogens OEShape:: OEBestOverlay, 162 OEShape:: OEOverlap, 169 OEShape:: OEOverlapPrep, 104 OEShape:: OEOverlapPrepOptions, 106 GetUseMaxHits OEShape:: OEROCSOptions, 125 GetUseOptimalLambdas OEShape:: OEHermiteOptions, 87 GetUseProxyGrid OEShape:: OEAnalyticOptions, 53 GetUserStarts OEShape:: OEBestOverlay, 162

# H

HasColor OEShape:: OEShapeQueryBase, 141 HasCutoff OEShape:: OEROCSOptions, 125 HasMolecule OEShape:: OEShapeQueryBase, 141 HasShape OEShape:: OEShapeQueryBase, 142 HasShapeGrid OEShape:: OEShapeQueryBase, 142 hermite-expansion.py Example Code, 35 hermite-tanimoto.py Example Code, 37

# $\mathbf{I}$

Init OEShape:: OEColorForceField, 64 IsEmpty OEShape:: OEShapeQueryBase, 142

# M

MeetsCutoff OEShape:: OEROCSOptions, 125 multicorebestoverlay.py Example Code, 26

# N

nxnshape.py

Example Code, 44

# O

OEShape:: OEAddColorAtom, 148 OEShape:: OEAddColorAtoms, 149 OEShape:: OEAddCoordsToColorAtom, 149 OEShape:: OEAnalyticColorFunc, 51 Constructors, 52 GetAnalyticOptions, 52 operator=, 52 OEShape:: OEAnalyticOptions, 52 Constructors, 53 GetExpType, 53 GetProxyGridCutoff, 53 GetUseProxyGrid, 53 operator=, 53 SetExpType, 53 SetProxyGridCutoff, 54 SetUseProxyGrid, 54 OEShape:: OEAnalyticShapeFunc, 54 Constructors, 55 GetAnalyticOptions, 55 operator=, 55 OEShape:: OEAsIsStarts, 56 Constructors, 56 operator=, 56 OEShape:: OEAtAtomStarts, 56 Constructors. 57 operator=, 57 OEShape:: OEBestOverlay, 159 ClearColorForceField, 160 ClearUserStarts, 160 Constructors, 160 GetCarbonRadius. 160 GetInitialOrientation, 160 GetMaxRandomTranslation, 160 GetMethod, 161 GetMinimizeType, 161 GetNumRandomStarts, 161 GetNumUserStarts, 161 GetRadiiApproximation, 161 GetRandomSeed, 161 GetRefGrid, 161 GetRefMol, 162 GetRefSelfColor, 162 GetRefSymmetry, 162 GetSymmetryThreshold, 162 GetUseHydrogens, 162 GetUserStarts, 162 operator=,  $160$ Overlay, 162 SetCarbonRadius, 162 SetColorForceField, 163 SetColorOptimize, 163

```
SetInitialOrientation, 163
                                            OEShape:: OEColorFFParameter, 61
   SetMaxRandomTranslation. 163
                                                Constructors. 62
   SetMethod, 163
                                                operator=, 62
   SetMinimizeType, 163
                                            OEShape:: OEColorFFType, 144
   SetNumRandomStarts, 164
                                            OEShape:: OEColorFFType:: Custom, 144
   SetRadiiApproximation, 164
                                            OEShape:: OEColorFFType:: ExplicitMillsDean,
   SetRandomSeed. 164
                                                    144
   SetRefGrid. 164
                                            OEShape::OEColorFFType::ExplicitMillsDeanNoRings,
   SetRefMol. 164
                                                    144
   SetSymmetryThreshold, 164
                                            OEShape:: OEColorFFType:: ImplicitMillsDean,
   SetUseHydrogens, 165
                                                    144
                                            OEShape:: OEColorFFType:: ImplicitMillsDeanNoRings,
   SetUserStarts, 165
OEShape:: OEBestOverlayResults, 57
                                                    144
   AddScore, 57
                                            OEShape:: OEColorFFType:: Max, 145
   Clear. 57
                                            OEShape:: OEColorFFType:: OEDefault, 144
   Constructors, 57
                                            OEShape:: OEColorFFType:: Undefined, 144
   GetScores, 58
                                            OEShape:: OEColorForceField, 62
                                                AddColorer. 63
   operator=, 57
OEShape:: OEBestOverlayScore, 58
                                                AddInteraction, 63
   Constructors, 59
                                                AddType, 63
   GetFitConfIdx, 59
                                                Clear, 63
   GetRefConfIdx, 59
                                                ClearInteractions, 64
   GetRotMatrix, 59
                                                Constructors, 63
   GetTranslation. 59
                                                GetTitle. 64
   operator=, 59
                                                GetType, 64
   Transform, 59
                                                GetTypeName, 64
OEShape:: OEBOMinType, 172
                                                GetTypes, 64
OEShape:: OEBOMinType:: Autoscale, 172
                                                Init, 64
OEShape:: OEBOMinType:: Default, 172
                                                operator=, 63OEShape:: OEBOMinType:: Overlap, 172
                                                Ready, 64
OEShape:: OEBOMinType:: Tanimoto, 172
                                                SetTitle, 64
OEShape:: OEBOOrientation, 172
                                                Write, 64
OEShape:: OEBOOrientation:: AsIs, 172
                                            OEShape:: OEColorFunc, 65
OEShape:: OEBOOrientation:: Default, 173
                                                GetColorOptions, 66
OEShape:: OEBOOrientation:: Inertial, 172
                                            OEShape:: OEColorOptions, 66
OEShape:: OEBOOrientation:: InertialAtColorAt@mmnstructors.66
       173
                                                GetColorForceField, 66
OEShape:: OEBOOrientation:: InertialAtHeavyAt@retMultiplier, 67
       173
                                                GetScoreType, 67
OEShape:: OEBOOrientation:: Random, 172
                                                operator=, 66
                                                SetColorForceField, 67
OEShape:: OEBOOrientation:: Subrocs, 173
OEShape::OEBOOrientation::UserInertialStart SetMultiplier, 67
       173
                                                SetScoreType, 67
OEShape:: OECalcShapeMultipoles, 149
                                            OEShape:: OEColorOverlap, 165
OEShape:: OECalcVolume, 149
                                                ColorScore, 166
                                                Constructors, 165
OEShape:: OECartesianStarts, 60
   ClearStartPoints, 61
                                                GetAllColor, 166
   Constructors, 60
                                                GetSelfColor. 166
   GetNumStartPoints.61
                                                operator=, 165
   GetStartPoints, 61
                                                SetAllColor, 166
   operator=, 60
                                                SetColorForceField.166
   SetStartPoints, 61
                                                SetFitMol, 166
OEShape:: OEClearCachedSelfColor, 149
                                                SetRefMol, 166
OEShape:: OEClearCachedSelfShape, 149
                                            OEShape:: OEColorResults, 167
```

**Index** 

Constructors, 167 GetFitTversky, 167 GetRefTversky, 167 GetTanimoto, 167 GetTversky, 167 OEShape:: OEColorTanimotoCutoff, 67 Constructors. 68 OEShape:: OEColorType, 148 OEShape:: OEColorType:: Analytic, 148 OEShape:: OEColorType:: Exact, 148 OEShape:: OEColorType:: Grid, 148 OEShape:: OEColorType:: None, 148 OEShape:: OECompressColorAtoms, 150 OEShape:: OECountColorAtoms, 150 OEShape:: OEDeleteCompressedColorAtoms, 150 OEShape:: OEDerivativeType, 145 OEShape:: OEDerivativeType:: Interpolated, OEShape:: OEFlexiOverlayOptions, 79 145 OEShape:: OEDerivativeType:: NearestValue, 145 OEShape:: OEExactColorFunc, 68 Constructors, 68 operator=, 69 OEShape:: OEExactShapeFunc, 69 Constructors, 71 operator=, 71 OEShape:: OEExponentialType, 145 OEShape:: OEExponentialType:: Standard, 145 OEShape:: OEExponentialType:: Tabulated, 145 OEShape:: OEFitColorTverskyCutoff, 71 Constructors, 71 OEShape:: OEFitTverskyComboCutoff, 71 Constructors, 72 OEShape:: OEFitTverskyCutoff, 72 Constructors, 72 OEShape:: OEFlexiOverlapFunc, 72 Overlap, 73 SetupRef, 73 UpdateColorCoords, 73 OEShape:: OEFlexiOverlapOptions, 73 Constructor, 74 GetColorFuncType, 74 GetColorOptions, 75 GetForceField, 74 GetHarmonic, 74 GetOverlapFunc, 75 GetShapeFuncType, 74 GetShapeOptions, 75 operator=, 74 SetColorFuncType, 75 SetColorOptions, 76

SetForceField, 75 SetHarmonic.76 SetOverlapFunc, 76 SetShapeFuncType, 75 SetShapeOptions, 76 Validate, 74 OEShape:: OEFlexiOverlapResults, 76 Constructor, 77 GetInternalEnergy, 77 operator=, 77 OEShape:: OEFlexiOverlay, 77 BestOverlay, 79 Constructor, 78 operator=, 78 Overlay, 78 SetupRef, 78 SortedOverlay, 78 Constructor, 79 GetFlexiOverlapOptions, 80 GetMaxOptSteps, 80 GetRigidOverlay, 80 GetRigidOverlayOptions, 80 operator=, 79 SetFlexiOverlapOptions, 81 SetMaxOptSteps, 80 SetRigidOverlay, 80 SetRigidOverlayOptions, 81 OEShape:: OEGetCachedSelfColor, 150 OEShape:: OEGetCachedSelfShape, 150 OEShape:: OEGetCenterAndExtents, 150 OEShape:: OEGetColorAtoms, 151 OEShape:: OEGetColorParents, 151 OEShape:: OEGetColorType, 151 OEShape:: OEGetMomentsOfInertiaTransform, 151 OEShape:: OEGridColorFunc, 81 Constructors, 82 GetGridOptions, 82 operator=, 82 OEShape:: OEGridShapeFunc, 83 Constructors, 84 GetGridOptions, 84 operator=, 84 OEShape:: OEHasCachedSelfColor, 151 OEShape:: OEHasCachedSelfShape, 152 OEShape:: OEHasColorAtoms, 152 OEShape:: OEHasCompressedColorAtoms, 152 OEShape:: OEHasPerceivedColorAtoms, 152 OEShape:: OEHermite, 84 Constructors, 85 CreateGrid, 85 GetCoefficients, 85 GetOptions, 85

GetSelfOverlap. 85 operator=, 85 Setup, 86 OEShape:: OEHermiteOptions, 86 Constructors, 86 GetLambdaX, 86 GetLambdaY. 87 GetLambdaZ, 87 GetNPolyMax, 87 GetUseOptimalLambdas, 87 operator=, 86 SetLambdaX, 87 SetLambdaY, 88 SetLambdaZ, 88 SetNPolyMax, 88 SetUseOptimalLambdas, 88 OEShape:: OEHermiteShapeFunc, 88 Constructors, 89 GetFitHermiteOptions, 90 GetRefHermiteOptions, 90 operator=, 90 OEShape:: OEHighestColorTanimoto, 90 CreateCopy, 90 operator $(1, 90)$ OEShape:: OEHighestComboScore, 167 CreateCopy, 168 operator(), 167 OEShape:: OEHighestFitColorTversky, 91 CreateCopy, 91 operator $($ ), 91 OEShape:: OEHighestFitTversky, 91 CreateCopy, 91 operator(), 91 OEShape:: OEHighestFitTverskyCombo, 91 CreateCopy, 92 operator(), 92 OEShape:: OEHighestOverlap, 92 CreateCopy, 92 operator(), 92 OEShape:: OEHighestRefColorTversky, 92 CreateCopy, 93 operator(), 92 OEShape:: OEHighestRefTversky, 93 CreateCopy, 93 operator(), 93 OEShape:: OEHighestRefTverskyCombo, 93 CreateCopy, 93 operator $($ ), 93 OEShape:: OEHighestScaledColor, 94 CreateCopy, 94 operator(), 94 OEShape:: OEHighestTanimoto, 94 CreateCopy, 94 operator(), 94

OEShape:: OEHighestTanimotoCombo, 94 CreateCopy, 95 operator $($ ), 95 OEShape:: OEHighestTverskyCombo, 95 Constructors, 95 CreateCopy, 95 operator(), 95 OEShape:: OEInertialStarts, 95 Constructors, 96 GetSymmetryThreshold, 97 operator=, 97 SetSymmetryThreshold, 97 OEShape:: OEIsColorAtom, 152 OEShape:: OEIsColorAtomPred, 97 Constructors, 97 CreateCopy, 97 operator(), 97 OEShape:: OEIsFastROCSShapeOuery, 153 OEShape:: OEMol2Query, 153 OEShape:: OEMomentSymmetry, 145 OEShape:: OEMomentSymmetry:: NoSymmetry, 146 OEShape:: OEMomentSymmetry:: Oblate, 146 OEShape:: OEMomentSymmetry:: Prolate, 146 OEShape:: OEMomentSymmetry:: Spherical, 146 OEShape:: OEMomentSymmetry:: Unknown, 146 OEShape:: OEMultiRefOverlay, 98 BestOverlay, 98 Constructors, 98 GetOverlayOptions, 98 operator=, 98 Overlay, 99 SetupRef, 99 OEShape:: OEOrientByMomentsOfInertia, 153 OEShape:: OEOverlap, 168 Constructors, 168 GetCarbonRadius, 168 GetGridSpacing, 168 GetMethod, 169 GetRadiiApproximation, 169 GetUseHydrogens, 169 operator= $,168$ Overlap, 169 SetCarbonRadius, 169 SetFitMol, 169 SetGridSpacing, 170 SetMethod, 170 SetRadiiApproximation, 170 SetRefGrid, 170 SetRefMol, 170 SetUseHydrogens, 170 OEShape:: OEOverlapCutoff, 99 Constructors, 99

OEShape:: OEOverlapFunc. 99 Constructors, 101 GetColorFunc, 101 GetShapeFunc, 101 operator=, 101 OEShape:: OEOverlapFuncBase, 101 Overlap, 102 SetupFlex, 103 SetupRef, 103 OEShape:: OEOverlapMethod, 173 OEShape:: OEOverlapMethod:: Analytic, 173 OEShape:: OEOverlapMethod:: Analytic2, 173 OEShape:: OEOverlapMethod:: Exact, 173 OEShape:: OEOverlapMethod:: Grid, 173 OEShape:: OEOverlapMethod:: Max, 174 OEShape:: OEOverlapPrep, 103 Constructors, 103 GetAssignBondiRadii, 104 GetAssignColor, 104 GetColorForceField, 104 GetUseHydrogens, 104 operator=, 104 Prep, 104 SetAssignBondiRadii, 104 SetAssignColor, 105 SetColorForceField, 105 SetUseHydrogens, 105 OEShape:: OEOverlapPrepOptions, 105 Constructor, 105 GetAssignBondiRadii, 106 GetAssignColor, 106 GetColorForceField, 106 GetDuplicateDistance, 106 GetRemoveDuplicate, 106 GetUseHydrogens, 106 operator=, 106 SetAssignBondiRadii, 107 SetAssignColor, 107 SetColorForceField, 107 SetDuplicateDistance, 107 SetRemoveDuplicate, 107 SetUseHydrogens, 107 OEShape:: OEOverlapRadii, 146 OEShape:: OEOverlapRadii:: All, 146 OEShape:: OEOverlapRadii:: Carbon, 146 OEShape:: OEOverlapRadii:: Default, 147 OEShape:: OEOverlapRadii:: Max, 147 OEShape:: OEOverlapRepresentation, 174 OEShape:: OEOverlapRepresentation:: All, 174 OEShape:: OEOverlapRepresentation:: Atomic, 174 OEShape:: OEOverlapRepresentation:: Atoms, 174

OEShape:: OEOverlapRepresentation:: Bonding, 174 OEShape:: OEOverlapRepresentation:: Bonds, 174 OEShape:: OEOverlapRepresentation:: Default, 174 OEShape:: OEOverlapRepresentation:: Full, 174 OEShape:: OEOverlapRepresentation:: Gaussian, 174 OEShape:: OEOverlapRepresentation: : Max, 175 OEShape:: OEOverlapResults, 108 Constructors, 108 GetColorScore, 109 GetColorTanimoto, 109 GetColorTversky, 109 GetFitColorTversky, 109 GetFitSelfColor, 109 GetFitSelfOverlap, 109 GetFitTversky, 109 GetFitTverskyCombo, 110 GetOverlap, 110 GetRefColorTversky, 110 GetRefSelfColor, 110 GetRefSelfOverlap, 110 GetRefTversky, 110 GetRefTverskyCombo, 110 GetTanimoto, 111 GetTanimotoCombo, 111 GetTversky, 111 operator=, 108 OEShape:: OEOverlay, 111 BestOverlay, 112 Constructors, 111 GetOverlayOptions, 112 operator= $, 112$ Overlay, 112 SetupRef, 112 SortedOverlay, 113 OEShape:: OEOverlayOptions, 113 Constructors, 113 GetColorFuncType, 114 GetColorOptions, 114 GetMaxOptSteps, 114 GetOverlapFunc, 114 GetShapeFuncType, 114 GetShapeOptions, 114 GetStarts, 115 operator=, 114 SetColorFuncType, 115 SetColorOptions, 115 SetMaxOptSteps, 115 SetOverlapFunc, 115

SetShapeFuncType, 115 SetShapeOptions, 116 SetStarts, 116 OEShape:: OEOverlayScoreCutoff, 116 CreateCopy, 116 operator $($ ), 116 OEShape:: OEQuatStarts, 117 ClearStarts, 117 Constructors, 117 operator=, 117 SetStarts, 118 OEShape:: OERandomStarts, 119 Constructors, 120 GetMaxRandomTranslation, 120 GetNumRandomStarts, 120 GetRandomSeed, 120 operator=, 120 SetMaxRandomTranslation, 120 SetNumRandomStarts, 120 SetRandomSeed, 121 OEShape:: OEReadShapeQuery, 153 OEShape:: OERefColorTverskyCutoff, 118 Constructors, 118 OEShape:: OERefTverskyComboCutoff, 118 Constructors, 118 OEShape:: OERefTverskyCutoff, 119 Constructors, 119 OEShape:: OERemoveColorAtoms, 153 OEShape:: OEROCS, 121 AddMolecule, 122 ClearMolecules, 122 Constructors, 121 GetROCSOptions, 122 operator=, 121 Overlay, 122 SetDatabase, 122 OEShape:: OEROCSOptions, 122 AddCutoff, 123 ClearCutoffs, 124 Constructors, 123 GetConfsPerHit, 124 GetMaxHits, 124 GetNumBestHits, 124 GetOverlayOptions, 124 GetPerformPrep, 124 GetRankPredicate, 125 GetUseMaxHits, 125 HasCutoff, 125 MeetsCutoff, 125 operator=, 123 SetConfsPerHit, 125 SetMaxHits, 125 SetNumBestHits, 126 SetOverlayOptions, 126

SetPerformPrep, 126 SetRankPredicate, 126 SetUseMaxHits, 126 OEShape:: OEROCSOverlay, 154 OEShape:: OEROCSResult, 126 AddScore, 128 Constructors, 127 GetOverlayConf, 128 GetOverlayConfs, 128 operator=, 128 OEShape:: OEScoreType, 147 OEShape:: OEScoreType:: Overlap, 147 OEShape:: OEScoreType:: Tanimoto, 147 OEShape:: OESelfColor, 154 OEShape:: OESelfShape, 154 OEShape:: OESetCachedSelfColor, 155 OEShape:: OESetCachedSelfShape, 155 OEShape:: OESetColorParents, 155 OEShape:: OESetColorType, 155 OEShape:: OESetCoordsFromColorParents, 156 OEShape:: OEShapeFunc, 128 GetShapeOptions, 129 OEShape:: OEShapeGetArch, 156 OEShape:: OEShapeGetLicensee, 156 OEShape:: OEShapeGetPlatform, 156 OEShape:: OEShapeGetRelease, 156 OEShape:: OEShapeGetSite, 156 OEShape:: OEShapeGetVersion, 157 OEShape:: OEShapeGridOptions, 130 Constructors, 130 GetDerivativeType, 131 GetGridSpacing, 131 operator=, 130 SetDerivativeType, 131 SetGridSpacing, 131 OEShape:: OEShapeIsLicensed, 157 OEShape:: OEShapeOptions, 131 Constructors, 131 GetCarbonRadius, 132 GetRadiiApproximation, 132 GetScoreType, 132 operator=, 132 SetCarbonRadius, 132 SetRadiiApproximation, 132 SetScoreType, 132 OEShape:: OEShapeQuery, 135 AddColorGaussian, 137 AddColorGaussians, 137 AddShapeGaussian, 137 Clear, 137 ClearColorGaussians, 137 ClearMolecule, 138 ClearShapeGaussians, 138

ClearShapeGrid. 138 Constructors. 136 DeleteColorGaussian, 138 DeleteShapeGaussian, 138 operator=, 137 SetAtomStrength, 138 SetMolecule. 138 SetShapeGrid, 139 OEShape:: OEShapeQueryBase, 139 GetAtomStrength, 140 GetColorForceField, 140 GetColorGaussians, 140 GetCompositeMolecule, 141 GetMolecule, 141 GetShapeGaussians, 141 GetShapeGrid, 141 GetTitle, 141 HasColor, 141 HasMolecule, 141 HasShape, 142 HasShapeGrid, 142 IsEmpty, 142 SetTitle, 142 OEShape:: OEShapeQueryPublic, 171 Constructors, 171 GetColorForceField, 171 GetTitle, 171 operator bool, 171 operator=, 171 OEShape:: OEShapeType, 147 OEShape:: OEShapeType:: Analytic, 148 OEShape:: OEShapeType:: Exact, 147 OEShape:: OEShapeType:: Grid, 147 OEShape:: OEShapeType:: Hermite, 148 OEShape:: OEShapeType:: None, 148 OEShape:: OESortOverlayScores, 157 OEShape:: OEStarts, 133 CreateCopy, 134 GetNumOfStarts, 134 GetStarts, 134 Setup, 134 SetupRef, 134 OEShape:: OESubrocsStarts, 142 Constructors, 142 operator=, 143 OEShape:: OETanimotoComboCutoff, 143 Constructors, 143 OEShape:: OETanimotoCutoff, 143 Constructors, 143 OEShape:: OEUncompressColorAtoms, 157 OEShape:: OEWriteShapeQuery, 158 operator bool OEShape:: OEShapeQueryPublic, 171 operator()

OEShape:: OEHighestColorTanimoto, 90 OEShape:: OEHighestComboScore, 167 OEShape:: OEHighestFitColorTversky, 91 OEShape:: OEHighestFitTversky, 91 OEShape:: OEHighestFitTverskyCombo, 92 OEShape:: OEHighestOverlap, 92 OEShape:: OEHighestRefColorTversky, 92 OEShape:: OEHighestRefTversky, 93 OEShape:: OEHighestRefTverskyCombo, 93 OEShape:: OEHighestScaledColor, 94 OEShape:: OEHighestTanimoto, 94 OEShape:: OEHighestTanimotoCombo, 95 OEShape:: OEHighestTverskyCombo, 95 OEShape:: OEIsColorAtomPred. 97 OEShape:: OEOverlayScoreCutoff, 116 operator= OEShape:: OEAnalyticColorFunc, 52 OEShape:: OEAnalyticOptions, 53 OEShape:: OEAnalyticShapeFunc, 55 OEShape:: OEAsIsStarts, 56 OEShape:: OEAtAtomStarts, 57 OEShape:: OEBestOverlay, 160 OEShape:: OEBestOverlayResults, 57 OEShape:: OEBestOverlayScore, 59 OEShape:: OECartesianStarts, 60 OEShape:: OEColorFFParameter, 62 OEShape:: OEColorForceField, 63 OEShape:: OEColorOptions, 66 OEShape:: OEColorOverlap, 165 OEShape:: OEExactColorFunc, 69 OEShape:: OEExactShapeFunc, 71 OEShape:: OEFlexiOverlapOptions, 74 OEShape:: OEFlexiOverlapResults, 77 OEShape:: OEFlexiOverlay, 78 OEShape:: OEFlexiOverlayOptions, 79 OEShape:: OEGridColorFunc, 82 OEShape:: OEGridShapeFunc, 84 OEShape:: OEHermite, 85 OEShape:: OEHermiteOptions, 86 OEShape:: OEHermiteShapeFunc, 90 OEShape:: OEInertialStarts, 97 OEShape:: OEMultiRefOverlay, 98 OEShape:: OEOverlap, 168 OEShape:: OEOverlapFunc. 101 OEShape:: OEOverlapPrep, 104 OEShape:: OEOverlapPrepOptions, 106 OEShape:: OEOverlapResults, 108 OEShape:: OEOverlay, 112 OEShape:: OEOverlayOptions, 114 OEShape:: OEQuatStarts, 117

```
OEShape:: OERandomStarts, 120
   OEShape:: OEROCS, 121
   OEShape:: OEROCSOptions, 123
   OEShape:: OEROCSResult, 128
   OEShape:: OEShapeGridOptions, 130
   OEShape:: OEShapeOptions, 132
   OEShape:: OEShapeQuery, 137
   OEShape:: OEShapeQueryPublic, 171
   OEShape:: OESubrocsStarts, 143
Overlap
   OEShape:: OEFlexiOverlapFunc, 73
   OEShape:: OEOverlap, 169
   OEShape:: OEOverlapFuncBase, 102
overlapcolor.py
   Example Code, 19
overlapquery.py
   Example Code, 32
Overlay
   OEShape:: OEBestOverlay, 162
   OEShape:: OEFlexiOverlay, 78
   OEShape:: OEMultiRefOverlay, 99
   OEShape:: OEOverlay, 112
   OEShape:: OEROCS, 122
overlayallres.py
   Example Code, 27
overlaybestres.py
   Example Code, 24
overlaystruct.py
   Example Code, 29
```

# P

Prep OEShape:: OEOverlapPrep, 104

# R

Ready OEShape:: OEColorForceField, 64 rescore.py Example Code, 14

# S

SetAllColor OEShape:: OEColorOverlap, 166 SetAssignBondiRadii OEShape:: OEOverlapPrep, 104 OEShape:: OEOverlapPrepOptions, 107 SetAssignColor OEShape:: OEOverlapPrep, 105 OEShape:: OEOverlapPrepOptions, 107 SetAtomStrength OEShape:: OEShapeQuery, 138 SetCarbonRadius OEShape:: OEBestOverlay, 162 OEShape:: OEOverlap, 169

OEShape:: OEShapeOptions, 132 SetColorForceField OEShape:: OEBestOverlay, 163 OEShape:: OEColorOptions, 67 OEShape:: OEColorOverlap, 166 OEShape:: OEOverlapPrep, 105 OEShape:: OEOverlapPrepOptions, 107 SetColorFuncType OEShape:: OEFlexiOverlapOptions, 75 OEShape:: OEOverlayOptions, 115 SetColorOptimize OEShape:: OEBestOverlay, 163 SetColorOptions OEShape:: OEFlexiOverlapOptions, 76 OEShape:: OEOverlayOptions, 115 SetConfsPerHit OEShape:: OEROCSOptions, 125 SetDatabase OEShape:: OEROCS, 122 SetDerivativeType OEShape:: OEShapeGridOptions, 131 SetDuplicateDistance OEShape:: OEOverlapPrepOptions, 107 SetExpType OEShape:: OEAnalyticOptions, 53 SetFitMol OEShape:: OEColorOverlap, 166 OEShape:: OEOverlap, 169 SetFlexiOverlapOptions OEShape:: OEFlexiOverlayOptions, 81 SetForceField OEShape:: OEFlexiOverlapOptions, 75 SetGridSpacing OEShape:: OEOverlap, 170 OEShape:: OEShapeGridOptions, 131 SetHarmonic OEShape:: OEFlexiOverlapOptions, 76 SetInitialOrientation OEShape:: OEBestOverlay, 163 SetLambdaX OEShape:: OEHermiteOptions, 87 SetLambdaY OEShape:: OEHermiteOptions, 88 SetLambdaZ OEShape:: OEHermiteOptions, 88 SetMaxHits OEShape:: OEROCSOptions, 125 SetMaxOptSteps OEShape:: OEFlexiOverlayOptions, 80 OEShape:: OEOverlayOptions, 115 SetMaxRandomTranslation OEShape:: OEBestOverlay, 163 OEShape:: OERandomStarts, 120 SetMethod

OEShape:: OEBestOverlay, 163 OEShape:: OEOverlap, 170 SetMinimizeType OEShape:: OEBestOverlay, 163 SetMolecule OEShape:: OEShapeQuery, 138 SetMultiplier OEShape:: OEColorOptions, 67 SetNPolyMax OEShape:: OEHermiteOptions, 88 SetNumBestHits OEShape:: OEROCSOptions, 126 SetNumRandomStarts OEShape:: OEBestOverlay, 164 OEShape:: OERandomStarts, 120 SetOverlapFunc OEShape:: OEFlexiOverlapOptions, 76 OEShape:: OEOverlayOptions, 115 SetOverlayOptions OEShape:: OEROCSOptions, 126 SetPerformPrep OEShape:: OEROCSOptions, 126 SetProxyGridCutoff OEShape:: OEAnalyticOptions, 54 SetRadiiApproximation OEShape:: OEBestOverlay, 164 OEShape:: OEOverlap, 170 OEShape:: OEShapeOptions, 132 SetRandomSeed OEShape:: OEBestOverlay, 164 OEShape:: OERandomStarts, 121 SetRankPredicate OEShape:: OEROCSOptions, 126 SetRefGrid OEShape:: OEBestOverlay, 164 OEShape:: OEOverlap, 170 SetRefMol OEShape:: OEBestOverlay, 164 OEShape:: OEColorOverlap, 166 OEShape:: OEOverlap, 170 SetRemoveDuplicate OEShape:: OEOverlapPrepOptions, 107 SetRigidOverlay OEShape:: OEFlexiOverlayOptions, 80 SetRigidOverlayOptions OEShape:: OEFlexiOverlayOptions, 81 SetScoreType OEShape:: OEColorOptions, 67 OEShape:: OEShapeOptions, 132 SetShapeFuncType OEShape:: OEFlexiOverlapOptions, 75 OEShape:: OEOverlayOptions, 115 SetShapeGrid OEShape:: OEShapeQuery, 139

SetShapeOptions OEShape:: OEFlexiOverlapOptions, 76 OEShape:: OEOverlayOptions, 116 SetStartPoints OEShape:: OECartesianStarts, 61 SetStarts OEShape:: OEOverlayOptions, 116 OEShape:: OEQuatStarts, 118 SetSymmetryThreshold OEShape:: OEBestOverlay, 164 OEShape:: OEInertialStarts, 97 SetTitle OEShape:: OEColorForceField, 64 OEShape:: OEShapeQueryBase, 142 Setup OEShape:: OEHermite, 86 OEShape:: OEStarts, 134 SetupFlex OEShape:: OEOverlapFuncBase, 103 SetupRef OEShape:: OEFlexiOverlapFunc, 73 OEShape:: OEFlexiOverlay, 78 OEShape:: OEMultiRefOverlay, 99 OEShape:: OEOverlapFuncBase, 103 OEShape:: OEOverlay, 112 OEShape:: OEStarts, 134 SetUseHydrogens OEShape:: OEBestOverlay, 165 OEShape:: OEOverlap, 170 OEShape:: OEOverlapPrep, 105 OEShape:: OEOverlapPrepOptions, 107 SetUseMaxHits OEShape:: OEROCSOptions, 126 SetUseOptimalLambdas OEShape:: OEHermiteOptions, 88 SetUseProxyGrid OEShape:: OEAnalyticOptions, 54 SetUserStarts OEShape:: OEBestOverlay, 165 shapeprops.py Example Code, 45 simpleoverlap.py Example Code, 13 SortedOverlay OEShape:: OEFlexiOverlay, 78 OEShape:: OEOverlay, 113

# Τ

tophits.py Example Code, 22 tophitsconf.py Example Code, 23 tophitsquery.py Example Code, 33

Transform OEShape:: OEBestOverlayScore, 59

# $\bigcup$

UpdateColorCoords OEShape:: OEFlexiOverlapFunc, 73 usercolor.py Example Code, 18

# $\vee$

Validate OEShape:: OEFlexiOverlapOptions, 74

# W

Write OEShape:: OEColorForceField, 64