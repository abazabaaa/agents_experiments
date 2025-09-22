![](_page_0_Picture_0.jpeg)

**FastROCS TK - Python** 

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1                                               | <b>Introduction</b>                                                                                      | 1 |
|-------------------------------------------------|----------------------------------------------------------------------------------------------------------|---|
| 2                                               | <b>FastROCS vs ROCS</b>                                                                                  | 1 |
| 3                                               | <b>Installation</b>                                                                                      | 1 |
|                                                 | <span style="padding-left:20px;">3.1 Prerequisites</span>                                                | 1 |
|                                                 | <span style="padding-left:40px;">3.1.1 GPU-Related Requirements</span>                                   | 1 |
|                                                 | <span style="padding-left:20px;">3.2 Hardware Performance Comparison</span>                              | 1 |
| 4                                               | <b>FastROCS Architecture</b>                                                                             | 1 |
|                                                 | <span style="padding-left:20px;">4.1 Memory Usage</span>                                                 | 1 |
|                                                 | <span style="padding-left:20px;">4.2 Multi-GPU Scaling</span>                                            | 1 |
|                                                 | <span style="padding-left:20px;">4.3 Multi-Node Scaling</span>                                           | 1 |
| 5                                               | <b>Examples</b>                                                                                          | 1 |
|                                                 | <span style="padding-left:20px;">5.1 FastROCS Example Suite</span>                                       | 1 |
|                                                 | <span style="padding-left:40px;">5.1.1 Simple Examples</span>                                            | 1 |
|                                                 | <span style="padding-left:40px;">5.1.2 Alternative Starts</span>                                         | 1 |
|                                                 | <span style="padding-left:40px;">5.1.3 Client-Server</span>                                              | 1 |
| 6                                               | <b>Tutorials</b>                                                                                         | 1 |
|                                                 | <span style="padding-left:20px;">6.1 Tutorial 0: Basic usage of FastROCS TK</span>                       | 1 |
|                                                 | <span style="padding-left:20px;">6.2 Tutorial 1: Alternative Starts</span>                               | 3 |
|                                                 | <span style="padding-left:40px;">6.2.1 Introduction</span>                                               | 3 |
|                                                 | <span style="padding-left:40px;">6.2.2 InertialAtHeavyAtoms</span>                                       | 3 |
|                                                 | <span style="padding-left:40px;">6.2.3 UserInertialStarts</span>                                         | 4 |
|                                                 | <span style="padding-left:40px;">6.2.4 Asls</span>                                                       | 4 |
|                                                 | <span style="padding-left:40px;">6.2.5 Retrieving Results</span>                                         | 4 |
|                                                 | <span style="padding-left:20px;">6.3 Tutorial 2: How to prepare a database for faster load speeds</span> | 4 |
| 7                                               | <b>API</b>                                                                                               | 5 |
|                                                 | <span style="padding-left:20px;">7.1 OEFastROCS Classes</span>                                           | 5 |
|                                                 | <span style="padding-left:40px;">7.1.1 OEDBTracer</span>                                                 | 5 |
|                                                 | <span style="padding-left:40px;">7.1.2 OEDBTracerBase</span>                                             | 5 |
|                                                 | <span style="padding-left:40px;">7.1.3 OEFastROCSHistogram</span>                                        | 5 |
|                                                 | <span style="padding-left:40px;">7.1.4 OEShapeDatabase</span>                                            | 5 |
|                                                 | <span style="padding-left:40px;">7.1.5 OEShapeDatabaseOptions</span>                                     | 6 |
|                                                 | <span style="padding-left:40px;">7.1.6 OEShapeDatabaseScore</span>                                       | 7 |
|                                                 | <span style="padding-left:20px;">7.2 OEFastROCS Constants</span>                                         | 8 |
|                                                 | <span style="padding-left:40px;">7.2.1 OEFastROCSOrientation</span>                                      | 8 |
|                                                 | <span style="padding-left:40px;">7.2.2 OEFastROCSReturnCode</span>                                       | 8 |
| 7.2.3 OEShapeDatabaseType                       | 8                                                                                                        |   |
| 7.2.4 OEShapeSimFuncType                        | 8                                                                                                        |   |
| 7.2.5 OEFastROCSMode                            | 9                                                                                                        |   |
| 7.3 OEFastROCS Functions                        | 9                                                                                                        |   |
| 7.3.1 OEFastROCSCacheStuff                      | 9                                                                                                        |   |
| 7.3.2 OEFastROCSGetArch                         | 9                                                                                                        |   |
| 7.3.3 OEFastROCSGetLicensee                     | 9                                                                                                        |   |
| 7.3.4 OEFastROCSGetNumDevices                   | 9                                                                                                        |   |
| 7.3.5 OEFastROCSGetPlatform                     | 9                                                                                                        |   |
| 7.3.6 OEFastROCSGetRelease                      | 9                                                                                                        |   |
| 7.3.7 OEFastROCSGetSite                         | 9                                                                                                        |   |
| 7.3.8 OEFastROCSGetVersion                      | 9                                                                                                        |   |
| 7.3.9 OEFastROCSGPUStatus                       | 9                                                                                                        |   |
| 7.3.10 OEFastROCSIsGPUReady                     | 9                                                                                                        |   |
| 7.3.11 OEFastROCSIsLicensed                     | 9                                                                                                        |   |
| 7.3.12 OEShapeDatabasePrep                      | 9                                                                                                        |   |
| 7.3.13 OEIsDatabasePrepared                     | 9                                                                                                        |   |
| 7.3.14 OEPrepareFastROCSMol                     | 9                                                                                                        |   |
| 7.3.15 OESetCoordsToInertialFrame               | 9                                                                                                        |   |
| 7.4 Using a Custom Color ForceField in FastROCS | 9                                                                                                        |   |
| 7.5 OEFastROCS ShapeDatabaseServer XMLRPC API   | 9                                                                                                        |   |
| 7.5.1 GetBestOverlays                           | 9                                                                                                        |   |
| 7.5.2 GetName                                   | 9                                                                                                        |   |
| 7.5.3 GetVersion                                | 9                                                                                                        |   |
| 7.5.4 IsLoaded                                  | 9                                                                                                        |   |
| 7.5.5 OEThrowSetLevel                           | 9                                                                                                        |   |
| 7.5.6 QueryHistogram                            | 9                                                                                                        |   |
| 7.5.7 QueryStatus                               | 9                                                                                                        |   |
| 7.5.8 QueryResults                              | 9                                                                                                        |   |
| 7.5.9 SetName                                   | 9                                                                                                        |   |
| 7.5.10 SubmitQuery                              | 9                                                                                                        |   |
| <b>8 Release History</b>                        | 10                                                                                                       |   |
| 8.1 FastROCS TK 2.2.7                           | 10                                                                                                       |   |
| 8.1.1 New features                              | 10                                                                                                       |   |
| 8.2 FastROCS TK 2.2.6                           | 10                                                                                                       |   |
| 8.3 FastROCS TK 2.2.5                           | 10                                                                                                       |   |
| 8.4 FastROCS TK 2.2.4                           | 10                                                                                                       |   |
| 8.5 FastROCS TK 2.2.3                           | 10                                                                                                       |   |
| 8.5.1 Major bug fixes                           | 10                                                                                                       |   |
| 8.6 FastROCS TK 2.2.2                           | 10                                                                                                       |   |
| 8.7 FastROCS TK 2.2.1                           | 10                                                                                                       |   |
| 8.8 FastROCS TK 2.2.0                           | 10                                                                                                       |   |
| 8.8.1 New features                              | 10                                                                                                       |   |
| 8.8.2 Minor bug fixes                           | 10                                                                                                       |   |
| 8.9 FastROCS TK 2.1.0                           | 10                                                                                                       |   |
| 8.9.1 New features                              | 10                                                                                                       |   |
| 8.9.2 Major bug fixes                           | 10                                                                                                       |   |
| 8.9.3 Minor bug fixes                           | 10                                                                                                       |   |
| 8.9.4 Python specific changes                   | 10                                                                                                       |   |
| 8.9.5 Java specific changes                     | 10                                                                                                       |   |
| 8.9.6 C++ specific changes                      | 10                                                                                                       |   |
| 8.9.7 Documentation changes                     | 10                                                                                                       |   |

| Section                                                                                     | Description             | Page |
|---------------------------------------------------------------------------------------------|-------------------------|------|
| 8.10.1                                                                                      | New features            | 104  |
| 8.10.2                                                                                      | Minor bug fixes         | 104  |
| 8.10.3                                                                                      | General notices         | 104  |
| 8.11                                                                                        | FastROCS TK 1.10.1      | 104  |
| 8.11.1                                                                                      | New features            | 104  |
| 8.11.2                                                                                      | Major bug fixes         | 104  |
| 8.11.3                                                                                      | Minor bug fixes         | 104  |
| 8.12                                                                                        | FastROCS TK 1.10.0      | 105  |
| 8.12.1                                                                                      | New features            | 105  |
| 8.12.2                                                                                      | Minor bug fixes         | 105  |
| 8.12.3                                                                                      | Python-specific changes | 105  |
| 8.12.4                                                                                      | Documentation changes   | 105  |
| 8.13                                                                                        | FastROCS TK 1.9.0       | 105  |
| 8.13.1                                                                                      | General notices         | 105  |
| 8.13.2                                                                                      | New features            | 105  |
| 8.13.3                                                                                      | Major bug fixes         | 105  |
| 8.13.4                                                                                      | Documentation changes   | 105  |
| 8.14                                                                                        | FastROCS TK 1.8.4       | 106  |
| 8.14.1                                                                                      | New features            | 106  |
| 8.14.2                                                                                      | Minor bug fixes         | 106  |
| 8.15                                                                                        | FastROCS TK 1.8.3       | 106  |
| 8.15.1                                                                                      | New features            | 106  |
| 8.15.2                                                                                      | Minor bug fixes         | 106  |
| 8.15.3                                                                                      | Python-specific changes | 106  |
| 8.15.4                                                                                      | Documentation changes   | 106  |
| 8.16                                                                                        | FastROCS TK 1.8.2       | 107  |
| 8.16.1                                                                                      | New features            | 107  |
| 8.16.2                                                                                      | Major bug fixes         | 107  |
| 8.16.3                                                                                      | Minor bug fixes         | 107  |
| 8.16.4                                                                                      | Documentation changes   | 107  |
| 8.17                                                                                        | FastROCS TK 1.8.1       | 110  |
| 8.17.1                                                                                      | New features            | 110  |
| 8.17.2                                                                                      | Major bug fixes         | 110  |
| 8.17.3                                                                                      | Minor bug fixes         | 110  |
| 8.18                                                                                        | FastROCS TK 1.8.0       | 111  |
| 8.18.1                                                                                      | New features            | 111  |
| 8.18.2                                                                                      | Minor bug fixes         | 111  |
| 8.18.3                                                                                      | Python-specific changes | 111  |
| 8.19                                                                                        | FastROCS TK 1.7.0       | 111  |
| 8.19.1                                                                                      | New features            | 112  |
| 8.19.2                                                                                      | Major bug fixes         | 112  |
| 8.19.3                                                                                      | Minor bug fixes         | 112  |
| 8.19.4                                                                                      | Python-specific changes | 113  |
| 8.19.5                                                                                      | Documentation changes   | 113  |
| 8.20                                                                                        | FastROCS TK 1.6.0       | 113  |
| 8.20.1                                                                                      | New features            | 113  |
| 8.20.2                                                                                      | Minor bug fixes         | 114  |
| 8.20.3                                                                                      | Python-specific changes | 114  |
| 8.20.4                                                                                      | Documentation changes   | 114  |
| 8.21                                                                                        | FastROCS TK 1.5.1       | 114  |
| 8.21.1                                                                                      | New features            | 114  |
| 8.21.2                                                                                      | Major bug fixes         | 114  |
| 8.21.3                                                                                      | Minor bug fixes         | 115  |
| 8.21.4                                                                                      | Documentation fixes     | 115  |
| Section                                                                                     | Page                    |      |
| 8.21.5  General notices                                                                     | 11                      |      |
| 8.22  FastROCS TK 1.5.0                                                                     | 11                      |      |
| 8.23  FastROCS TK 1.4.0                                                                     | 11                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 8.23.1  Features                    | 11                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 8.23.2  Bug Fixes                   | 11                      |      |
| 8.24  FastROCS TK 1.3.1                                                                     | 11                      |      |
| 8.25  FastROCS TK 1.3.0                                                                     | 11                      |      |
| 8.26  FastROCS TK 1.2.1                                                                     | 11                      |      |
| 8.27  FastROCS TK 1.1.1                                                                     | 11                      |      |
| 8.28  FastROCS TK 1.1.0                                                                     | 11                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 8.28.1  Major Bug Fixes             | 11                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 8.28.2  Minor Bug Fixes             | 11                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 8.28.3  Major Features              | 12                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 8.28.4  Minor Features              | 12                      |      |
| 8.29  FastROCS TK 1.0.1                                                                     | 12                      |      |
| 8.30  FastROCS TK 1.0.0                                                                     | 12                      |      |
| 8.31  FastROCS TK 0.4.0                                                                     | 12                      |      |
| 8.32  FastROCS TK 0.3.1                                                                     | 12                      |      |
| 8.33  FastROCS TK 0.3.0                                                                     | 12                      |      |
| 8.34  FastROCS TK 0.2.3                                                                     | 12                      |      |
| 8.35  FastROCS TK 0.2.2                                                                     | 12                      |      |
| 8.36  FastROCS TK 0.2.1                                                                     | 12                      |      |
| 8.37  FastROCS TK 0.2.0                                                                     | 12                      |      |
| 8.38  FastROCS TK 0.1.1                                                                     | 12                      |      |
| 8.39  FastROCS TK 0.1.0                                                                     | 12                      |      |
| 9  Copyright and Trademarks                                                                 | 12                      |      |
| 10  Sample Code                                                                             | 12                      |      |
| 11  Citation                                                                                | 12                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 11.1  Orion ® Floes                 | 12                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 11.2  Toolkits and Applications     | 12                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 11.3  OpenEye Web Services          | 13                      |      |
| 12  Technology Licensing                                                                    | 13                      |      |
| <span style="display:inline-block;width:1.5em;"></span> 12.1  GCC                           | 14                      |      |
| <span style="display:inline-block;width:3em;"></span> 12.1.1  GCC RUNTIME LIBRARY EXCEPTION | 14                      |      |
| <span style="display:inline-block;width:3em;"></span> 12.1.2  GNU GENERAL PUBLIC LICENSE    | 15                      |      |

### **Index**

Warning: FastROCS TK is available in Python, Java, and C++ on 64-bit Linux platforms only.

# **INTRODUCTION**

FastROCS TK is an extremely fast shape comparison application, based on the idea that molecules have similar shape if their volumes overlay well and any volume mismatch is a measure of dissimilarity. It uses a smooth Gaussian function to represent the molecular volume [Grant-1996], so it is possible to routinely minimize to the best global match. FastROCS will perform millions of these global shape matches every second. See the Molecular Shape section in the Shape TK theory documentation for a description of the shape and color theory used in FastROCS TK.

Now, in just seconds, FastROCS TK can perform a virtual screen over an entire multi-conformer representation of a corporate collection to find active compounds with similar shape to a lead compound (a task that could previously take up to a day [Rush-2005]). Recent work suggests that the underlying ligand-based shape similarity approach is competitive with, and often superior to, structure-based approaches in virtual screening [Hawkins-2007] [Venhorst-2008], both in terms of overall performance and consistency [Sheridan-2008]. Alignments to crystallographic conformations have also been useful in pose prediction in the absence of a protein structure [Sutherland-2007].

In addition to virtual screening and lead hopping, FastROCS TK can be used to perform NxN shape comparisons over an entire multiconformer database. A prototype of clustering with FastROCS TK can be found in the SphereExclusionClustering.py example program.

**TWO** 

# **FASTROCS VS ROCS**

OpenEye makes available two separate shape based virtual screening technologies:

**ROCS** Thousands of conformers per second

**FastROCS** Millions of conformers per second

The ROCS technology is also embodied in the Shape TK. The Shape TK is a very flexible toolkit for experimenting with molecular shape and different ways that it can be applied. FastROCS is also deployed as a toolkit, but with a very different goal in mind: raw performance. In order to achieve this raw performance GPU hardware is utilized. The use of GPUs required the complete rewrite of the ROCS algorithm to work well on GPUs. Furthermore, the opportunity was taken to completely rethink all trade-offs the algorithm makes in preference to speed. Therefore, it is expected that ROCS and FastROCS will output slightly different results.

In order for FastROCS to achieve a throughput of millions of conformers per second the entire informatics base of shape comparison had to be reimagined. FastROCS operates on millions of conformers in memory, in parallel, all at once. Whereas, the Shape TK will typically only operate on a single molecule at a time. Therefore, FastROCS is designed as a web service to serve shape queries from a database pre-loaded into memory: ShapeDatabaseServer.py example. The ShapeDatabaseServer.py is the best place for new users to start.

The ShapeDatabaseServer.py example is built around the most important API in FastROCS TK, the OEShape-Database. The OEShapeDatabase class is built to be a natural extension of the OEMolDatabase class in OEChem **TK**. The OEShapeDatabase object will manage the storage of conformers in memory and interacting with any GPU in the system. Theoretically, the user of OEShapeDatabase should not have to know that their calculation is being performed on a GPU.

Note: For batch processing operations where databases are brought into memory temporarily, the BestShapeOverlay.py is a better first script to read and alter.

**THREE** 

# **INSTALLATION**

1. Install the OpenEye Toolkits into a virtual environment:

```
$ mkvirtualenv fastrocs
(fastrocs) $ pip install --extra-index-url https://pypi.anaconda.org/OpenEye/
→simple OpenEye-toolkits
```

2. Once installed, follow the instructions in *Tutorial 0: Basic usage of FastROCS TK* to get you started.

## **3.1 Prerequisites**

### 3.1.1 GPU-Related Requirements

The following is required in order to use GPU-accelerated OpenEye toolkits and applications:

#### **Supported Platforms**

CUDA-enabled OpenEye software is only available on supported Linux platforms. For supported Linux platforms see above and/or the Platform Support Page

#### **Supported GPUs**

An NVIDIA Tesla, Quadro, or GeForce GPU with a **compute capability of 3.5** or higher is required on your system. For a comprehensive table of which GPUs fall into which compute capability category please refer to the CUDA wikipedia page.

#### **NVIDIA Drivers**

- Minimum NVIDIA Driver version: 450.x.
- CUDA is **not** required to be installed.

We recommend driver 450.80.02 and we strongly advise manually downloading and installing the appropriate NVidia driver for your system as opposed to using a package manager.

To install, root privilege is required. Follow these steps:

- 1. Download the driver to the machine you are installing it on.
- 2. chmod  $+x$  the driver package to make it executable.

3. Ensure you have disabled X-server by killing any running sessions. Reboot may be required if X-server is still running after this step.

Warning: Disabling X-server requires different processes to be killed depending on your Linux distribution. See Nvidia installation guide for more details.

Warning: The NVidia kernel module can often conflict with the open source Nouveau display drivers depending on your specific Linux distribution. The NVidia documentation is a much more complete and up-to-date source for information on how to work around this issue. See Disabling Nouveau on the NVIDIA website.

4. Install the driver by sudo ./NVIDIA-Linux-x86\_64-450.80.02.run and follow the step-by-step installation instructions.

For more details on driver installations see the CUDA Installation Guide

Note: The output of the nvidia-smi command is extremely useful when debugging GPU issues. Please include the output from  $n$ vidia-smi in any request to support@eyesopen.com.

### **Performance Tuning**

To get the most performance out of an NVIDIA Graphics card, use the persistence daemon to switch persistence mode on across all cards on the system (root privilege required):

sudo nvidia-persistenced --user foo

This will automatically enable persistence mode after reboot.

For full instructions on persistence daemon see the Persistence daemon section of the NVIDIA docs.

## 3.2 Hardware Performance Comparison

![](_page_14_Figure_2.jpeg)

The following graph shows the performance of FastROCS TK on some modern GPU models.

Note: Performance can vary with driver versions and other factors. The above graph is meant as a general guide of what performance customers can expect. It is highly recommended to go with a certified vendor like Exxact to ensure best performance.

# **FASTROCS ARCHITECTURE**

## 4.1 Memory Usage

A rule of thumb is 1 GB of main memory for every 4 million conformers. The primary variable FastROCS TK users need to think about is how many conformers per molecule is needed. The OMEGA default of 200 conformers per molecule is much higher than it needs to be due to OEDocking vs ROCS virtual screening performance. OEDocking needs a higher number of conformers than ROCS does. ROCS can perform quite well with 10-50 conformers per molecule. The number of conformers chosen has a direct linear relationship to **FastROCS** query performance and the amount of memory needed.

Note: The "rule of thumb" is based upon the number of heavy atoms being normally distributed around 25-30 heavy atoms. The number of heavy atoms also has a linear relationship to the memory consumption. So fragment databases will be significantly smaller, but large macro-cycle peptide databases will be significantly larger.

Note: The above "rule of thumb" assumes the default of four inertial starts and no alternative starting points. If you choose to use eight inertial starts, you should assume you'll need about 1.5 as much main memory, i.e. 1.5 GB for every 4 million conformers. If you choose to use alternative starts, you should multiply the amount of main memory by the number of alternative starts / 3.

Color scoring does significantly increase virtual screening performance. As much color information, centroids and self terms, is cached in memory as well. For doing pure  $OEShapeDatabaseType\ Shape$  analysis, color information can be elided allowing for a small percentage in memory size reduction, around 5-10%. For a more complete breakdown of memory usage, use the OEShapeDatabase. PrintMemoryUsage method to print statistics on memory usage.

Note: Color atom and self term calculation is a dominating factor in how fast FastROCS can load molecules from disk. Therefore, it is heavily recommended to pre-process OEB files with OEP repareFastROCSMo1.

It is important to note that FastROCS is most sensitive to host main memory, not GPU memory. On board GPU memory size does not heavily affect FastROCS performance, so buying the cheaper GPUs with less memory is just fine for FastROCS.

Note: This memory overhead will be improved over time. Significant advances were made in version 1.4.0, memory consumption per conformer was cut in half. Then cut in half again for the 1.7.0 release.

## **4.2 Multi-GPU Scaling**

**FastROCS** will automatically scale across as many GPUs as can be found on the current machine. It is not uncommon or overly expensive to get a machine with 4-8 GPUs in it. As with any parallel program, truly optimal linear scaling is difficult to achieve, but FastROCS gets fairly close as can be seen in the below graph.

![](_page_17_Figure_3.jpeg)

Fig. 1: This graph is a comparison of the various generations of Tesla compute cards produced by NVidia for high performance computing purposes.

Note: Static color calculations are still performed on the CPU. For best performance, a decent mid-range CPU with 2-cores per GPU is recommended.

The OEShapeDatabase class will by default automatically scale across all GPUs and CPUs in the system. In this way it can be a very large resource hog for CPU, GPU, and memory. There are some methods provided on the class to control resource utilization, but the current best control is through the CUDA VISIBLE DEVICES environment variable.

## **4.3 Multi-Node Scaling**

Scaling FastROCS across multiple nodes is possible with the included ShapeDatabaseProxy.py example.

# **FIVE**

# **EXAMPLES**

## 5.1 FastROCS Example Suite

FastROCS comes with a variety of scripts for configuring, reporting, and debugging. For more details of how to use these examples please see the Tutorials section.

### 5.1.1 Simple Examples

| Program                        | Description                                                          |
|--------------------------------|----------------------------------------------------------------------|
| bestshapeoverlay               | database searching with queries                                      |
| bestshapeoverlaymulticonfquery | database searching with every conformer of every query               |
| besttverskyshapeoverlay        | database searching with queries using Tversky similarity scoring     |
| coloroptimization              | optimize over color overlap in addition to shape overlap             |
| customcolorffprep              | cache custom color atoms onto molecules                              |
| implicitmillsdeannorings       | run fastrocs with the implicit mills dean cff sans rings             |
| rocsmode                       | turn on rocs mode                                                    |
| shapedatabasechunker           | split database into chunks                                           |
| shapedatabaseprep              | prepare OEB file for faster load performance                         |
| shapedistancematrix            | calculate distance between all molecules in database with themselves |
| shapeclustering                | cluster database into shape clusters                                 |

### 5.1.2 Alternative Starts

| Program                   | Description                                                                            |
|---------------------------|----------------------------------------------------------------------------------------|
| asisstarts                | database searching with queries using the as is starting orientation                   |
| inertialatheavyatomstarts | database searching with queries using the inertial at heavy atoms starting orientation |
| userinertialstarts        | database searching with queries using the user inertial starts orientation             |

### 5.1.3 Client-Server

| Program                      | Description                                                       |
|------------------------------|-------------------------------------------------------------------|
| shapedatabaseserver          | run the FastROCS server                                           |
| shapedatabaseclient          | send query to specified server                                    |
| shapedatabaseclienthistogram | send query to specified server and print histogram                |
| shapedatabaseisloaded        | returns whether the database has completed loading in server:port |
|                              |                                                                   |
| multiserverloadbalancing     | spread database across multiple servers                           |
| shapedatabaseproxy           | tie multiple servers to appear as a single server                 |
| shapedatabaseoethrowsetlevel | adjust the verbosity of server running on server:port             |

**SIX** 

# **TUTORIALS**

# 6.1 Tutorial 0: Basic usage of FastROCS TK

**FastROCS TK** is primarily designed to be used as a server/client interface. Example scripts are provided with FastROCS TK to help you get up and running. This tutorial demonstrates the use of the section\_example\_fastrocs\_shapedatabaseserver and section\_example\_fastrocs\_shapedatabaseclient. example scripts, which are provided below.

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
import os
import socket
try:
    from SocketServer import ThreadingMixIn
except ImportError:
    from socketserver import ThreadingMixIn
from threading import Thread
from threading import Lock
from threading import Condition
from threading import Event
from openeye import oechem
from openeye import oeshape
try:
```

```
from openeye import oefastrocs
except ImportError:
   oechem. OEThrow. Fatal ("This script is not available, "
                         "FastROCS is not supported on this platform.")
try:
    from xmlrpclib import Binary
    from SimpleXMLRPCServer import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
except ImportError: # python 3
   from xmlrpc.client import Binary
    from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
oepy = os.path.join(os.path.dirname(_file_), "..", "python")
sys.path.insert(0, os.path.realpath(oepy))
# very important that OEChem is in this mode since we are passing molecules between
\rightarrowthreads
oechem.OESetMemPoolMode(oechem.OEMemPoolMode_System)
class ReadWriteLock (object) :
    """ Basic locking primitive that allows multiple readers but only
   a single writer at a time. Useful for synchronizing database
   updates. Priority is given to pending writers. """
   def __init__(self):self.config = Condition()self. readers = 0self.writers = 0def AcquireReadLock(self):
        self.cond.acquire()
        try:
            while self.writers:
                self.cond.wait()
            self.readers += 1assert self.writers == 0finally:
           self.cond.notify_all()
            self.cond.release()
   def ReleaseReadLock(self):
        self.cond.acquire()
        assert self.readers > 0try:
            self.readers -1finally:
            self.cond.notify_all()
            self.cond.release()
    def AcquireWriteLock(self):
       self.cond.acquire()
        self.writers += 1while self.readers:
            self.config.wait()assert self.readers == 0
```

```
assert self.writers > 0def ReleaseWriteLock (self) :
        assert self.readers == 0assert self.writers > 0self.writers -= 1
        self.cond.notify_all()
        self.cond.release()
class ShapeQueryThread (Thread) :
    """ A thread to run a query against a shape database """
    def _init_(self, shapedb, querymolstr, nhits, iformat, oformat, errorLevel,
\leftrightarrow*kwarqs):
        """ Create a new thread to perform a query. The query doesn't
        execute until start is called.
        shapedb - database to run the query against
        See MCMolShapeDatabase.GetBestOverlays for a description of
        the querymolstr and nhits arguments.
        n, n, nThread.__init__(self)
        self.shapeOnly = kwargs.pop('shapeOnly', False)
        self.tversky = kwargs.pop('tversky', False)
        self.altStarts = kwargs.pop('altStarts', False)
        self.randStarts = kwargs.pop('randStarts', False)
        self.shapedb = shapedb
        self.querymolstr = querymolstr
        self.iformat = iformatself.oformat = oformat
        self.scoretype = GetDatabaseType(self.shapeOnly)
        self.simFuncType = GetSimFuncType(self.tversky)
        numHistBins = 200if self.shapeOnly:
           numHistBins = 100self.tracer = oefastrocs.OEDBTracer(numHistBins)
        self.options = oefastrocs.OEShapeDatabaseOptions()
        self.options.SetTracer(self.tracer)
        self.options.SetLimit(nhits)
        self.options.SetScoreType(self.scoretype)
        self.options.SetSimFunc(self.simFuncType)
        if self.altStarts:
            self.options.SetInitialOrientation(GetStartType(self.altStarts))
            if self.randStarts:
                self.options.SetNumRandomStarts(self.randStarts)
        self. lock = Lock()self.errorLevel = errorLevel
    def run (self) :
        """ Perform the query """
```

```
(continued from previous page)
```

```
# make sure the error level is set for this operating system thread
        oechem.OEThrow.SetLevel(self.errorLevel)
        try:
            results = self.shapedb.GetBestOverlays(self.querymolstr,
                                                     self.options,
                                                     self.iformat,
                                                     self.oformat)
            # since we are writing to the thread's dictionary this could
            # race with the GetStatus method below
            self.lock.acquire()
            try:
                self.results = results
                if not results:
                    self.exception = RuntimeError("Query error, no results to return,
\leftrightarrow<sup>11</sup>
                                                     "check the server log for more
\leftrightarrowinformation")
            finally:
                self.lock.release()
        except Exception as e:
            self.lock.acquire()
            try:
                self. exception = efinally:
                self.lock.release()
   def GetStatus(self, blocking):
        """ Returns a tuple of (count, total). count is the number of
        conformers already searched. total is the total number of
        conformers that will be searched.
        If blocking is True this method will not return until the
        count has been changed (beware of deadlocks!). If blocking is
        False the function will return immediately.
        n \, n \, nself.lock.acquire()
        try:
            if hasattr (self, "exception"):
                raise self.exception
            return self.tracer.GetCounts(blocking), self.tracer.GetTotal()
        finally:
            self.lock.release()
    def GetHistogram (self) :
        """ Returns a list of integers representing the histogram of
        the molecule scores already scored.
        n \, n \, nself.lock.acquire()
        try:
            if hasattr (self, "exception"):
                raise self.exception
            hist = self.tracer.GetHistogram()
            scoretype = self.scoretype
```

```
finally:
            self.lock.release()
        frequencies = oechem. OEUIntVector()
        hist.GetHistogram(frequencies, scoretype)
        return list (frequencies)
    def GetResults (self) :
        """ Return an OEB string containing the overlaid
        confomers. This method should only be called after this thread
        has been joined. """
        if hasattr (self, "exception") :
            raise self.exception
        return self.results
class ShapeQueryThreadPool:
    H H HMaintains a pool of threads querying the same MCMolShapeDatabase.
    n \, n \, ndef __init__(self, dbase):
        """ Create a new thread pool to issues queries to dbase """
        self.shapedb = dbase
        self. queryidx = 0self.threads = \{\}self.lock = Lock()self.errorLevel = oechem.OEThrow.GetLevel()
    def SubmitQuery(self, querymolstr, nhits, iformat, oformat, kwargs):
        """ Returns an index that can be passed to the QueryStatus and
        QueryResults methods.
        See MCMolShapeDatabase.GetBestOverlays for a description of
        the querymolstr and nhits arguments.
        n, n, nself.lock.acquire()
        try:
            idx = self.queryidxself. queryidx += 1self.threads[idx] = ShapeQueryThread(self.shapedb,
                                                  querymolstr,
                                                  nhits,
                                                  iformat,
                                                  oformat,
                                                  self.errorLevel,
                                                  ***kwargs)
            self.threads[idx].start()
        finally:
            self.lock.release()
        return idx
    def QueryStatus(self, idx, blocking):
        """ Returns the status of the query indicated by idx. See
        ShapeQueryThread.GetStatus for the description of the blocking
```

```
argument. ""
        self.lock.acquire()
        try:
            thrd = self.threads[idx]finally:
            self.lock.release()
        return thrd. GetStatus (blocking)
    def QueryHistogram(self, idx):
        """ Returns the histogram of molecule scores already scored
        for the query indicated by idx. """
        self.lock.acquire()
        trv:
            thrd = self.threads[idx]
        finally:
            self.lock.release()
        return thrd. GetHistogram()
    def QueryResults(self, idx):
        """ Wait for the query associated with idx to complete and
        then return the results as an OEB string. """
        self.lock.acquire()
        try:
            thrd = self.threads [idx]del self.threads[idx]
        finally:
            self.lock.release()
        thrd.join()return thrd. GetResults ()
    def SetLevel(self, level):
        """ Set what level of information should be printed by the server. """
        self_errorLevel = levelreturn True
class DatabaseLoaderThread (Thread) :
    """ A thread to read a database into memory. Special note, OEChem
   must be placed in system allocation mode using
    oechem. OESetMemPoolMode (oechem. OEMemPoolMode_System). This is because the
    default OEChem memory caching scheme uses thread local storage,
    but since this thread is temporary only for reading in molecules
    that memory will be deallocated when this thread is terminated. """
    def _init_(self, shapedb, moldb, dbname, loadedEvent):
        n \, n \, nshapedb - the shapedb to add the molecules to
        moldb - the OEMolDatabase object to use
        dbname - the file name to open the OEMolDatabase on
        loadedEvent - event to set once loading is finished
        \pi \pi \piThread, init (self)
        self.shapedb = shapedbself.moldb = moldbself.dbname = dbname
```

```
(continued from previous page)
```

```
self.loadedEvent = loadedEvent
    def run (self) :
        """ Open the database file and load it into the OEShapeDatabase """
        timer = occhem.OEWallTimer()sys.stderr.write("Opening database file %s ...\n" % self.dbname)
        if not self.moldb.Open(self.dbname):
            oechem. OEThrow. Fatal ("Unable to open '%s'" % self.dbname)
        dots = occhem. OEThreadedDots (10000, 200, "conformers")if not self.shapedb.Open(self.moldb, dots):
            oechem. OEThrow. Fatal ("Unable to initialize OEShapeDatabase on '%s'" %
\rightarrowself.dbname)
        dots, Total()sys.stderr.write("%s seconds to load database\n" % timer.Elapsed())
        self.loadedEvent.set()
def SetupStream(strm, format):
    format = format.strip('.'')ftype = oechem. OEGetFileType(format)
   if ftype == oechem. OEFormat_UNDEFINED:
        raise ValueError ("Unsupported file format sent to server ' 8s'" % format)
    strm.SetFormat(ftype)
    strm.Setgz(oechem.OEIsGZip(format))
    return strm
OECOLOR_FORCEFIELDS = {
    "ImplicitMillsDean": oeshape.OEColorFFType_ImplicitMillsDean,
    "ImplicitMillsDeanNoRings": oeshape.OEColorFFType_ImplicitMillsDeanNoRings,
    "ExplicitMillsDean": oeshape.OEColorFFType_ExplicitMillsDean,
    "ExplicitMillsDeanNoRings": oeshape.OEColorFFType_ExplicitMillsDeanNoRings
    \mathcal{F}def GetDatabaseType(shapeOnly):
   if shapeOnly:
        return oefastrocs. OEShapeDatabaseType_Shape
    return oefastrocs. OEShapeDatabaseType Default
def GetSimFuncType(simFuncType):
    if simFuncType:
        return oefastrocs. OEShapeSimFuncType Tversky
    return oefastrocs. OEShapeSimFuncType_Tanimoto
def GetStartType(altStarts):
   if altStarts == 'random':
        return oefastrocs. OEFastROCSOrientation_Random
    if altStarts == 'inertialAtHeavyAtoms':
        return oefastrocs. OEFastROCSOrientation InertialAtHeavyAtoms
    if altStarts == 'inertialAtColorAtoms':
        return oefastrocs. OEFastROCSOrientation_InertialAtColorAtoms
    if altStarts == 'subrocs':
```

```
return oefastrocs. OEFastROCSOrientation_Subrocs
    return oefastrocs. OEFastROCSOrientation_Inertial
def GetAltStartsString(altStarts):
    if altStarts == oefastrocs.OEFastROCSOrientation_Random:
        return 'random'
    if altStarts == oefastrocs.OEFastROCSOrientation_InertialAtHeavyAtoms:
        return 'inertialAtHeavyAtoms'
   if altStarts == oefastrocs.OEFastROCSOrientation_InertialAtColorAtoms:
        return 'inertialAtColorAtoms'
    if altStarts == oefastrocs.OEFastROCSOrientation_Subrocs:
       return 'subrocs'
    return 'inertial'
def GetShapeDatabaseArgs(itf):
    shapeOnly = itf. GetBool("-shapeOnly")
    if shapeOnly and itf.GetParameter("-chemff").GetHasValue():
        oechem. OEThrow. Fatal ("Unable to specify -shapeOnly and -chemff at the same
\leftrightarrowtime!")
    chemff = \text{itf}.getString("-chemff")if not chemff.endswith(".cff"):
        return (GetDatabaseType(shapeOnly), OECOLOR_FORCEFIELDS[chemff])
    # given a .cff file, use that to construct a OEColorForceField
   assert not shapeOnly
   cff = oeshape.OEColorForceField()if not cff. Init (chemff) :
        oechem. OEThrow. Fatal ("Unable to read color force field from '%s'" % chemff)
    return (cff, )def ReadShapeQuery (querymolstr) :
   iss = oechem.oeisstream(querymolstr)
   query = oeshape.OEShapeQueryPublic()
    if not oeshape. OEReadShapeQuery(iss, query):
        raise ValueError ("Unable to read a shape query from the data string")
   return query
class MCMolShapeDatabase:
   """ Maintains a database of MCMols that can be queried by shape
    similarity.""
    def _init_(self, itf):
        """ Create a MCMolShapeDatabase from the parameters specified by the
\rightarrowOEInterface. """
        self.rwlock = ReadWriteLock()self.loadedEvent = Event()self.dbname = itf.GetString("-dbase")
        if oechem. OEIsGZip(self.dbname):
            oechem. OEThrow. Fatal ("%s is an unsupported database file format as it is,
                                                                            (continues on next page)
\rightarrowgzipped. "
```

```
"Preferred formats are .oeb, .sdf or .oez" % self.
\rightarrowdbname)
       self.moldb = oechem.OEMolDatabase()
       self.dbtype = GetDatabaseType(itf.GetBool("-shapeOnly"))
       self.shapedb = oefastrocs.OEShapeDatabase(*GetShapeDatabaseArqs(itf))
       # this thread is daemonic so a KeyboardInterupt
        # during the load will cancel the process
       self.loaderThread = DatabaseLoaderThread(self.shapedb,
                                                  self.moldb,
                                                  self.dbname,
                                                  self.loadedEvent)
       self.loaderThread.daemon = True
       self.loaderThread.start()
   def IsLoaded(self, blocking=False):
       """ Return whether the server has finished loading. """
       if blocking:
           self.loadedEvent.wait()
        # clean up the load waiter thread if it's still there
       if self.loadedEvent.is_set() and self.loaderThread is not None:
           self.rwlock.AcquireWriteLock()
           try: # typical double checked locking
                if self.loaderThread is not None:
                    self.loaderThread.join()
                    self.loaderThread = None
           finally:
               self.rwlock.ReleaseWriteLock()
       return self.loadedEvent.is_set()
   def GetBestOverlays (self, querymolstr, options, iformat, oformat):
        """ Return a string of the format specified by 'oformat'
       containing nhits overlaid confomers using querymolstr as the
       query interpretted as iformat.
       querymolstr - a string containing a molecule to use as the query
       options - an instance of OEShapeDatabaseOptions
       iformat - a string representing the file extension to parse the querymolstr.
\leftrightarrow as.
                  Note: old clients could be passing .sq files, so
                  iformat == '.oeb' will try to interpret the file as
                  a .sq file.
       oformat - file format to write the results as
        H, H, Htimer = occhem.OEWallTimer()
        # make sure to wait for the load to finish
       blocking = Trueloaded = self.Jsloaded(blocking)assert loaded
       if iformat.startswith(".sq"):
           query = ReadShapeQuery(querymolstr)
```

 $else:$ 

(continued from previous page)

```
# read in query
            qfs = oechem.oemolistream()qfs = SetupStream(qfs, iformat)
            if not qfs.openstring(querymolstr):
                raise ValueError ("Unable to open input molecule string")
            query = oechem. OEGraphMol()
            if not oechem. OEReadMolecule (qfs, query) :
                if iformat == ".oeb": # could be an old client trying to send a .sq.
\rightarrowfile.
                    query = ReadShapeQuery (querymolstr)
                else:
                    raise ValueError ("Unable to read a molecule from the string of.
\rightarrowformat '\frac{8}{5}s'"
                                       % iformat)
        ofs = occhem.oemolostream()ofs = SetupStream(ofs, oformat)
        if not ofs.openstring():
            raise ValueError("Unable to openstring for output")
        # do we only want shape based results?
        # this is a "Write" lock to be paranoid and not overload the GPU
        self.rwlock.AcquireWriteLock()
        try:
            # do search
            scores = self.shapedb.GetSortedScores(query, options)
            sys.stderr.write("%f seconds to do search\n" % timer.Elapsed())
        finally:
            self.rwlock.ReleaseWriteLock()
        timer. Start ()
        # write results
        for score in scores:
            mcmol = oechem. OEMol()
            if not self.moldb.GetMolecule(mcmol, score.GetMolIdx()):
                oechem. OEThrow. Warning ("Can't retrieve molecule %i from the
→OEMolDatabase, "
                                         "skipping..." % score. GetMolIdx())
                continue
            # remove hydrogens to make output smaller, this also
            # ensures OEPrepareFastROCSMol will have the same output
            oechem.OESuppressHydrogens(mcmol)
            mol = oechem. OEGraphMol(mcmol. GetConf(oechem. OEHasConfIdx(score.
\rightarrowGetConfIdx())))
            oechem.OECopySDData(mol, mcmol)
            if options. GetSimFunc() == oefastrocs. OEShapeSimFuncType_Tanimoto:
                oechem. OESetSDData (mol, "ShapeTanimoto", "%. 4f" % score.
\rightarrowGetShapeTanimoto())
                oechem. OESetSDData (mol, "ColorTanimoto", "%. 4f" % score.
\rightarrowGetColorTanimoto())
                oechem. OESetSDData(mol, "TanimotoCombo", "%. 4f" % score.
→GetTanimotoCombo())
```

```
(continued from previous page)
```

```
else:
                oechem. OESetSDData(mol, "ShapeTversky", "%. 4f" % score.
→GetShapeTversky())
                oechem. OESetSDData(mol, "ColorTversky", "%. 4f" % score.
\rightarrowGetColorTversky())
                oechem. OESetSDData (mol, "TverskyCombo", "%. 4f" % score.
\rightarrowGetTverskyCombo())
            if options. GetInitialOrientation () != oefastrocs. OEFastROCSOrientation_
\leftarrowTnertial·
                oechem. OEAddSDData (mol, "Opt. Starting Pos.",
                                    GetAltStartsString(options.
\rightarrowGetInitialOrientation()))
            score.Transform(mol)
            oechem.OEWriteMolecule(ofs, mol)
        output = ofs.GetString()
        sys.stderr.write("%f seconds to write hitlist\n" % timer.Elapsed())
        sys.stderr.flush()
        ofs.close()
        return output
    def GetName (self) :
        self.rwlock.AcquireReadLock()
        try:
            return self.dbname
        finally:
            self.rwlock.ReleaseReadLock()
    def SetName(self, name):
        self.rwlock.AcquireWriteLock()
        try:
            self.dbname = namefinally:
            self.rwlock.ReleaseWriteLock()
class ShapeQueryServer:
    """ This object's methods are exposed via XMLRPC. """
    def __init__(self, itf):
        """ Initialize the server to serve queries on the database
        named by dbname."""
        self.shapedb = MCMolShapeDatabase(itf)
        self.thdpool = ShapeQueryThreadPool(self.shapedb)
        self.itf = itf
    def IsLoaded(self, blocking=False):
        """ Return whether the server has finished loading. """
        return self.shapedb.IsLoaded(blocking)
    def GetBestOverlays(self, querymolstr, nhits, iformat=".oeb", oformat=".oeb"):
        """ A blocking call that only returns once the query is completed. """
        results = self.shapedb.GetBestOverlays(querymolstr.data, nhits, iformat,
\rightarrowoformat)
```

```
(continued from previous page)
```

```
return Binary (results)
    def SubmitQuery(self, querymolstr, nhits, iformat=".oeb", oformat=".oeb",
\rightarrowkwargs=None):
        """ Returns a index that can be used by QueryStatus and
        QueryResults. This method will return immediately."""
        if not kwargs:
            kwargs = \{\}if self.itf.GetBool("-shapeOnly"):
            kwargs['shapeOnly'] = True
        return self.thdpool.SubmitQuery(querymolstr.data, nhits, iformat, oformat,
\rightarrowkwarqs)
    def OueryStatus (self, queryidx, blocking=False):
        """ Return the status of the query specified by queryidx. See
        ShapeQueryThread.GetStatus for a description of the blocking
        argument and the return value."""
        return self.thdpool.QueryStatus(queryidx, blocking)
    def QueryHistogram(self, queryidx):
        """ Return the current histogram of scores specified by
        queryidx."""
        return self.thdpool.QueryHistogram(queryidx)
    def QueryResults(self, queryidx):
        """ Wait for the query associated with idx to complete and
        then return the results as an OEB string. """
        results = self.thdpool.QueryResults(queryidx)
        return Binary (results)
    def GetVersion (self) :
        """ Returns what version of FastROCS this server is. """
        return oefastrocs. OEFastROCSGetRelease()
   def OEThrowSetLevel(self, level):
        """ Set what level of information should be printed by the server. """
        return self.thdpool.SetLevel(level)
    def GetName (self) :
        """ The name of this database. By default this is the file name of the.
\rightarrowdatabase used. """
        return self.shapedb.GetName()
    def SetName(self, name):
        """ Set a custom database name for this server. """
        self.shapedb.SetName(name)
        return True
# Restrict to a particular path.
class RequestHandler (SimpleXMLRPCRequestHandler) :
   rpc\_paths = ('/RPC2',')class AsyncXMLRPCServer (ThreadingMixIn, SimpleXMLRPCServer) :
   # if a shutdown request occurs through a signal force everything to terminate
                                                                            (continues on next page)
 \rightarrowimmediately
```

```
daemon_threads = True
    allow_reuse_address = True
InterfaceData = """\!BRIEF [-shapeOnly | -chemff <color forcefield>] [-hostname] [-dbase] database [[-
\rightarrowport] 8080]
!PARAMETER -dbase
  !TYPE string
  !REQUIRED true
  !BRIEF Input database to serve
 !KEYLESS 1
! END
!PARAMETER -port
  !TYPE int
  !REOUIRED false
  !BRIEF Port number to start the XML RPC server on
  IDEFAULT 8080
  !KEYLESS 2
!\,\mathsf{END}!PARAMETER -hostname
  !TYPE string
  IDFFAUI.T 0.0.0.0!BRIEF Name of the server to bind to
! END
!PARAMETER -shapeOnly
  !ALIAS -s
 !TYPE bool
 !DEFAULT false
 !BRIEF Run FastROCS server in shape only mode, clients can also control this
\leftrightarrowseparately
! END
!PARAMETER -chemff
  !TYPE string
  !LEGAL_VALUE ImplicitMillsDean
  !LEGAL_VALUE ImplicitMillsDeanNoRings
  !LEGAL_VALUE ExplicitMillsDean
  !LEGAL_VALUE ExplicitMillsDeanNoRings
  !LEGAL_VALUE *.cff
 !DEFAULT ImplicitMillsDean
  !BRIEF Chemical force field. Either a constant or a filename.
!END
\mathbf{u}u u
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if not oefastrocs. OEFastROCSIsGPUReady():
        oechem. OEThrow. Fatal ("No supported GPU available to run FastROCS TK!")
    itf = oechem. OEInterface (InterfaceData, argv)
    # default hostname to bind is 0.0.0.0, to allow connections with
    # any hostname
    hostname = itf.getString("-hostname")# default port number is 8080
```

```
(continued from previous page)
```

```
portnumber = itf.GetInt("-port")# create server
    server = AsyncXMLRPCServer ((hostname, portnumber),
                               requestHandler=RequestHandler,
                               logRequests=False)
    hostname, portnumber = server.socket.getsockname()
    if hostname == "0.0.0.0":
       hostname = socket.gethostname()
    sys.stderr.write("Listening for ShapeDatabaseClient.py requests on s: i \in \mathbb{N}n'n"
                     % (hostname, portnumber))
    sys.stderr.write("Example: ShapeDatabaseClient.py %s:%i query.sdf hit.sdf\n\n"
                     % (hostname, portnumber))
    # register the XMLRPC methods
    server.register_introspection_functions()
    server.register_instance(ShapeQueryServer(itf))
    try:
        # Run the server's main loop
        server.serve_forever()
    finally:
        server.server_close()
    return <sub>0</sub>if name = '_main ':
   sys.exit(main(sys.argv))
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
import argparse
try:
   from xmlrpclib import ServerProxy, Binary, Fault
except ImportError: # python 3
```

```
from xmlrpc.client import ServerProxy, Binary, Fault
def GetFormatExtension(fname):
   base, ext = os.path.splitext(fname.lower())if ext == ".gx":base, ext = os.path.splitext(base)ext += ".qz"
    return ext
def main(argv=[__name__]):
   parser = argparse.ArgumentParser()# positional arguments retaining backward compatibility
   parser.add_argument('server:port', help='Server name and port number of database_
\leftrightarrowto search '
                                              'i.e. localhost:8080.')
    parser.add_argument('query', help='File containing the query molecule to search '
                                        '(format not restricted to *.oeb).')
   parser.add_argument('results',
                         help='Output file to store results (format not restricted to,
\leftrightarrow \star.oeb).')
   parser.add_argument('nHits', nargs='?', type=int, default=100,
                         help='Number of hits to return (default=100).')
   parser.add_argument('--tversky', action='store_true', default=argparse.SUPPRESS,
                         help='Switch to Tversky similarity scoring (default=Tanimoto).
\leftarrow<sup>1</sup>)
    parser.add_argument('--shapeOnly', action='store_true', default=argparse.SUPPRESS,
                         help='Switch to shape-only scores (default=Combo).')
    parser.add_argument('--alternativeStarts', default=argparse.SUPPRESS, nargs=1,
\rightarrowdest='altStarts',
                         choices=('random', 'subrocs',
                                  'inertialAtHeavyAtoms', 'inertialAtColorAtoms'),
                         help='Optimize using alternative starts (default=inertial). '
                              'To perform N random starts do '
                              ""--alternativeStarts random N" (default N=10)')
    known, remaining = (\text{parse} \times \text{known} \text{ args}())dargs = vars(know)qfname = dargs.pop('query')
   numHits = dargs.pop('nHits')
    startType = dargs.get('altStarts', None)
    if startType:
        dargs['altStarts'] = str(startType[0])if len(remaining) == 1 and dargs['altStarts'] == 'random':
            try:
                numRands = int(remaining[0])dargs['randstarts'] = numRandsexcept ValueError:
                print ("Invalid argument given. See --help menu for argument list")
                sys.exit()
        if len(remaining) > 1:
```

```
print ("Too many arguments given. See --help menu for argument list")
            sys.exit()
   else:
       if remaining:
            print ("Too many arguments given. See --help menu for argument list")
            sys.exit()
   try:
       fh = open(qfname, 'rb')except IOError:
       sys.stderr.write("Unable to open '%s' for reading" % qfname)
       return 1
   iformat = GetFormatExtension(qframe)ofname = dargs.pop('results')
   oformat = GetFormatExtension(ofname)
   s = ServerProxy("http://" + dargs.pop('server:port'))data = Binary(fh.read())try:
       idx = s.SubmitQuery(data, numHits, iformat, oformat, dargs)
   except Fault as e:
       if "TypeError" in e.faultString:
            # we're trying to run against an older server, may be able
            # to still work if the formats ameniable.
            if ((iformat == ".oeb" or iformat == ".sq") and oformat == ".oeb"):
                idx = s.SubmitQuery(data, numHits)else:
                sys.stderr.write("%s is too new of a version to work with the server
\rightarrow \frac{6}{5}\n"
                                  % (argv[0], argv[1]))sys.stderr.write("Please upgrade your server to FastROCS version 1.4.0
\leftrightarrow<sup>11</sup>
                                  " or later to be able to use this client \n")
                sys.stderr.write("This client will work with this version of the
\rightarrowserver "
                                  "if the input file is either"
                                  "'.oeb' or '.sq' and the output file is '.oeb'\n")
                return 1
       else:
            sys.stderr.write(str(e))
           return 1
   first = Falsewhile True:
       blocking = Truetry:
            current, total = s. QueryStatus (idx, blocking)
       except Fault as e:
           print(str(e), file=sys.stderr)
            return 1
       if total == 0:
            continue
```

```
if first:
            print ("%s/%s" % ("current", "total"))
            first = Falseprint ("%i/%i" % (current, total))
        if total \leq current:
            break
    results = s. QueryResults (idx)
    # assuming the results come back as a string in the requested format
    with open (ofname, 'wb') as output:
        output.write(results.data)
    return 0
if name == '_main ':
    sys.exit(main(sys.argv))
```

After FastROCS TK has been installed follow these simple steps for the most basic usage of FastROCS TK:

1. Start the server on an OMEGA conformer database in your terminal in the virtual environment you used to install the OpenEye Toolkits:

(fastrocs) \$ ShapeDatabaseServer.py your\_database.oeb

2. Query the server from another terminal using the same virtual environment:

```
(fastrocs) $ ShapeDatabaseClient.py localhost:8080 your_query.sdf output_overlays.
\rightarrowsdf
```

Note: The server can be queried from the same terminal by putting the ShapeDatabaseServer process in the background by doing ctrl z && bg.

Warning: For best performance, do not use GNU Zipped (.gz) molecule databases with FastROCS. Uncompress the .oeb.qz to .oeb first.

For more advanced options see the  $-\text{help menu}$ :

```
(fastrocs) $ ShapeDatabaseClient.py --help
.. code-block:: bash
  usage: ShapeDatabaseClient.py [-h] [--tversky] [--shapeOnly]
                                  [--alternativeStarts {random, subrocs,
\rightarrowinertialAtHeavyAtoms, inertialAtColorAtoms}]
                                  server: port query results [nHits]
  positional arguments:
                            Server name and port number of database to search i.e.
    server:port
                           localhost:8080.
```

| query                                                                          | File containing the query molecule to search (format not restricted to *.oeb).                                                       |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| results                                                                        | Output file to store results (format not restricted to *.oeb).                                                                       |
| nHits                                                                          | Number of hits to return (default=100).                                                                                              |
| optional arguments:                                                            |                                                                                                                                      |
| -h, --help                                                                     | show this help message and exit                                                                                                      |
| --tversky                                                                      | Switch to Tversky similarity scoring (default=Tanimoto).                                                                             |
| --shapeOnly                                                                    | Switch to shape-only scores (default=Combo).                                                                                         |
| --alternativeStarts {random,subrocs,inertialAtHeavyAtoms,inertialAtColorAtoms} | Optimize using alternative starts (default=inertial).<br>To perform N random starts do "--alternativeStarts random N" (default N=10) |

# 6.2 Tutorial 1: Alternative Starts

## 6.2.1 Introduction

In this tutorial you will learn how to make use of the alternative starts functionality in **FastROCS TK**. This functionality was introduced in the OpenEye Toolkits v2017. Feb release of FastROCS TK 1.8.1.

Note: The data used in this tutorial is not provided.

Alternative starting points refer to the starting orientations of the query-conformer pair when optimizing their overlap in space. The default method is OEFastROCSOrientation. Inertial. In this method, the molecules are centered and set to an inertial frame of reference. The database molecule is then rotated about its inertial axes, creating up to a possible 8 starting points at which overlays are then optimized.

The default optimizes the first 4 inertial starts only. This can be changed via the OEShapeDatabaseOptions. Set NumInertialStarts method. The figure below shows the inertial starting points of caffeine.

![](_page_39_Picture_9.jpeg)

Fig. 1: Inertial Starting Points of Caffeine

For some molecular structures these inertial starting positions may not lead to adequate sampling of the molecular

volume overlap space, resulting in poor overlap/scores. Making use of alternative starts can solve this problem by creating additional starting positions at which to perform the inertial optimizations. One example of this is the alignment of 4TMN and 3TMN ligands of Thrombin [Grant-1996].

The figure below shows the 2D molecular structure of these ligands and their x-ray alignment. The x-ray alignment shows a good overlap between 3TMN and the side chain of 4TMN.

![](_page_40_Figure_3.jpeg)

Fig. 2: Alternative Starts Use Case 4TMN ligand, 3TMN ligand, and their x-ray alignment.

The figure below shows the resultant overlays in FastROCS TK when using default starting points compared to OEFastROCSOrientation. InertialAtHeavyAtoms starting points.

![](_page_40_Figure_6.jpeg)

#### Fig. 3: Overlap Comparison

Overlay generated from performing a default search (left) compared with "InertialAtHeavyAtoms" search (right).

The default search results in poor overlap between the two molecules (left). When the new OEFastROCSOrientation. InertialAtHeavyAtoms orientation option is used, the resultant overlap is much more favorable (right) and correlates well with the x-ray alignment from Alternative Starts Use Case.

There are 5 methods currently implemented in **FastROCS TK** that allow different starting orientations to be experimented with. They are:

- · OEFastROCSOrientation. Inertial
- · OEFastROCSOrientation. InertialAtHeavyAtoms
- · OEFastROCSOrientation. InertialAtColorAtoms

- · OEFastROCSOrientation. UserInertialStarts
- OEFastROCSOrientation.AsIs

A description of these can be found in the OEFastROCSOrientation section of the docs.

This tutorial will focus on 3 alternative starts methods:

- OEFastROCSOrientation. InertialAtHeavyAtoms
- · OEFastROCSOrientation. UserInertialStarts
- · OEFastROCSOrientation.AsIs

The methodology described can be adapted to the remaining starting point options that are not described in this tutorial. For example, the use case for OEFastROCSOrientation. InertialAtColorAtoms is almost identical to OEFastROCSOrientation. InertialAtHeavyAtoms except for the constant passed in to OEShapeDatabaseOptions. SetInitialOrientation and the use of OEShapeDatabaseOptions. GetNumColorAtomStarts instead of OEShapeDatabaseOptions. GetNumHeavyAtomStarts to retrieve the number of starts.

# 6.2.2 InertialAtHeavyAtoms

OEFastROCSOrientation. InertialAtHeavyAtoms translates the center of mass (COM) of each database molecule to each heavy atom of the query molecule and to the query molecule's COM. 4 inertial orientations are then optimized at each translation.

The figures below demonstrate the starting positions optimized for the first 2 heavy atoms in the query molecule:

![](_page_41_Picture_12.jpeg)

Fig. 4: Inertial starts optimized at heavy atom 1 (highlighted green)

![](_page_41_Figure_14.jpeg)

Fig. 5: Inertial starts optimized at heavy atom 2 (highlighted green)

Inertial starts continue to be optimized for the remaining atoms of the query molecule and it's COM.

Below is a link to a python script demonstrating the most basic usage of **FastROCS TK**. After explaining this simple script it will be modified to make use of the OEFastROCSOrientation. InertialAtHeavyAtoms function.

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
import os
from openeye import oechem
from openeye import oefastrocs
oepy = os.path.join(os.path.dirname(_file_), "..", "python")
sys.path.insert(0, os.path.realpath(oepy))
def main(argv=[_name_]):
    if len(argv) < 4:
        oechem. OEThrow. Usage ("%s <database> <query> <hits.oeb>" % argv[0])
        return 0
    # check system
    if not oefastrocs. OEFastROCSIsGPUReady():
        oechem.OEThrow.Info("No supported GPU available!")
        return 0
    # read in database
    dbname = argv[1]if oechem. OEIsGZip(dbname):
        oechem. OEThrow. Fatal ("%s is an unsupported database file format as it is.
\rightarrowgzipped.\n"
                             "Preferred formats are .oeb, .sdf or .oez", dbname)
   print ("Opening database file %s ..." % dbname)
   dbase = oefastrocs.OEShapeDatabase()
   moldb = oechem.OEMolDatabase()
   if not moldb. Open (dbname) :
        oechem. OEThrow. Fatal ("Unable to open '%s'" % dbname)
    dots = occhem.OETHreadedDots (10000, 200, "conformers")if not dbase. Open (moldb, dots) :
        oechem. OEThrow. Fatal ("Unable to initialize OEShapeDatabase on '%s'" % dbname)
    # customize search options
```

```
opts = oefastrocs.OEShapeDatabaseOptions()
    opts.SetLimit(5)
    qfname = argv[2]# read in query
    qfs = oechem.oemolistream()if not qfs.open(qfname):
        oechem. OEThrow. Fatal ("Unable to open '%s'" % qfname)
    query = oechem.OEGraphMol()
    if not oechem. OEReadMolecule (qfs, query) :
        oechem. OEThrow. Fatal ("Unable to read query from '%s'" % qfname)
   ofs = occhem.oemolostream()if not ofs.open(argv[3]):
        oechem. OEThrow. Fatal ("Unable to open '%s'" % argv[3])
    oechem.OEWriteMolecule(ofs, query)
    print ("Searching for %s" % qfname)
    for score in dbase. GetSortedScores (query, opts):
        print ("Score for mol %u(conf %u) %f shape %f color" % (
               score.GetMolIdx(), score.GetConfIdx(),
               score.GetShapeTanimoto(), score.GetColorTanimoto()))
        dbmol = occhem. OEMol()molidx = score.GetMolldx()if not moldb. GetMolecule (dbmol, molidx) :
            print ("Unable to retrieve molecule '%u' from the database" % molidx)
            continue
        mol = oechem. OEGraphMol(dbmol. GetConf(oechem. OEHasConfIdx(score.
\rightarrowGetConfIdx())))
        oechem. OESetSDData(mol, "ShapeTanimoto", "%. 4f" % score. GetShapeTanimoto())
        oechem. OESetSDData(mol, "ColorTanimoto", "%. 4f" % score. GetColorTanimoto())
        oechem. OESetSDData(mol, "TanimotoCombo", "%. 4f" % score. GetTanimotoCombo())
        score.Transform(mol)
        oechem.OEWriteMolecule(ofs, mol)
    print ("Wrote results to %s" % argv[3])
    return 0
if _name_ == '_main_':
    sys.exit(main(sys.argv))
```

The script creates an OEMolDatabase and an OEShapeDatabase object. The database file is first opened as an OEMol-Database object, which is used to load the molecules into OEShapeDatabase via OEShapeDatabase. Open. This is the simplest example of loading a database. The database is now ready for either combo or shape-only searches.

Note: To restrict searches to shape-only, create a shape-only database object:

 $shapeOnlyDB = oefastrocs.OEShapeDatabase(oefastrocs.OEShapeDatabaseType, Shape)$ 

While this reduces the memory footprint of the database as color data is no longer stored, the database cannot be searched for color scores.

In this example, an OEShapeDatabaseOptions object is also created and the number of results is limited to 5 via the OEShapeDatabaseOptions. SetLimit method.

Next, the query molecule is set up is using a molecule stream and the OEReadMolecule function. Queries are used to search the loaded database via the OEShapeDatabase. GetSortedScores method. The OEShape-DatabaseOptions class is passed to customize the search options. In this example, a subset of the eMolecules database was searched against a benzene query molecule. The top 5 scores are shown below.

```
Opening database file eMolecules.2015.1_100subset.oeb ...
Searching for benzene.oeb
Score for mol 65(conf 1) 0.530182 shape 0.237350 color
Score for mol 45(conf 1) 0.678128 shape 0.085376 color
Score for mol 49(conf 1) 0.596801 shape 0.153465 color
Score for mol 92(conf 0) 0.503204 shape 0.155330 color
Score for mol 33(conf 1) 0.442559 shape 0.175599 color
```

To make use of the OEFastROCSOrientation. InertialAtHeavyAtoms feature, modify the OEShape-DatabaseOptions object as follows:

```
opts = oefastrocs.OEShapeDatabaseOptions()
opts.SetLimit(5)
opts.SetInitialOrientation(oefastrocs.OEFastROCSOrientation_
→InertialAtHeavyAtoms)
```

An additional option, OEShapeDatabaseOptions. SetInitialOrientation, is also set to the desired method, OEFastROCSOrientation. InertialAtHeavyAtoms. The resultant scores reflect the change in starting points:

```
Opening database file eMolecules.2015.1_100subset.oeb ...
Searching for benzene.oeb
Score for mol 45(conf 1) 0.669345 shape 0.121420 color
Score for mol 65(conf 1) 0.530182 shape 0.237350 color
Score for mol 49(conf 1) 0.596801 shape 0.153465 color
Score for mol 92(conf 0) 0.503204 shape 0.155330 color
Score for mol 33(conf 1) 0.442559 shape 0.175599 color
```

The OEShapeDatabaseOptions. GetNumHeavyAtomStarts method can be used to find out how many heavy atom starts are being optimized. This method requires the query molecule in order to return the number of starts:

```
query = oechem.OEGraphMol()
oechem.OEReadMolecule(qfs, query)
if opts.GetInitialOrientation() == oefastrocs.OEFastROCSOrientation_
\rightarrow Inertial At Heavy Atoms:
    numStarts = opts.GetNumHeavyAtomStarts(query)
    oechem. OEThrow. Info ("This example will use \frac{2}{3}u starts" \frac{8}{3} numStarts)
```

When this code snippet is added to the Python script, the output should look like this:

```
This example will use 7 starts
Searching for benzene.oeb
```

Score for mol 45(conf 1) 0.669345 shape 0.121420 color

(continued from previous page)

```
Score for mol 65(conf 1) 0.530182 shape 0.237350 color
Score for mol 49(conf 1) 0.596801 shape 0.153465 color
Score for mol 92(conf 0) 0.503204 shape 0.155330 color
Score for mol 33(conf 1) 0.442559 shape 0.175599 color
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
from openeye import oefastrocs
oepy = os.path.join(os.path.dirname(_file_), "..", "python")
sys.path.insert(0, os.path.realpath(oepy))
def main(argv=[__name__]):
    if len(argv) < 4:
        oechem.OEThrow.Usage("%s <database.oeb> <queries> <hits.oeb>" % argv[0])
        return 0
    # check system
    if not oefastrocs. OEFastROCSIsGPUReady():
        oechem. OEThrow. Info ("No supported GPU available!")
        return 0
    # read in database
    dbname = \text{arg} \sqrt{1}if oechem. OEIsGZip (dbname):
        oechem. OEThrow. Fatal ("%s is an unsupported database file format as it is.
\rightarrowqzipped. \n"
                              "Preferred formats are .oeb, .sdf or .oez", dbname)
    print ("Opening database file %s ..." % dbname)
    dbase = ofastrocs. OEShapeDatabase()moldb = oechem.OEMolDatabase()
    if not moldb. Open (dbname) :
```

```
(continued from previous page)
```

```
oechem. OEThrow. Fatal ("Unable to open '%s'" % dbname)
   dots = occhem.OEFhreadedDots (10000, 200, "conformers")if not dbase. Open (moldb, dots) :
        oechem. OEThrow. Fatal ("Unable to initialize OEShapeDatabase on '%s'" % dbname)
    # customize search options
   opts = oefastrocs.OEShapeDatabaseOptions()
   opts.SetLimit(5)
   opts.SetInitialOrientation(oefastrocs.OEFastROCSOrientation_InertialAtHeavyAtoms)
   qfname = argv[2]# read in query
   qfs = oechem.oemolistream()if not qfs.open(qfname):
        oechem. OEThrow. Fatal ("Unable to open '%s'" % qfname)
   query = oechem. OEGraphMol()
   if not oechem. OEReadMolecule (qfs, query) :
        oechem. OEThrow. Fatal ("Unable to read query from '%s'" % qfname)
   # write out everthing to a similary named file
   ofs = oechem.oemolostream()
   if not ofs.open(argv[3]):
        oechem. OEThrow. Fatal ("Unable to open '%s'" % argv[3])
   oechem.OEWriteMolecule(ofs, query)
   if opts.GetInitialOrientation() == oefastrocs.OEFastROCSOrientation_
\rightarrow InertialAtHeavyAtoms:
        numStarts = opts.GetNumHeavyAtomStarts(query)
        print ("This example will use \frac{2}{3}u starts" % numStarts)
   opts.SetMaxOverlays(opts.GetNumInertialStarts() \star opts.
→GetNumHeavyAtomStarts(query))
   print ("Searching for %s" % qfname)
   for score in dbase. GetSortedScores (query, opts) :
        print ("Score for mol \frac{2}{3}u (conf \frac{2}{3}u) \frac{2}{3}f shape \frac{2}{3}f color" \frac{2}{3} (
               score.GetMolIdx(), score.GetConfIdx(),
               score.GetShapeTanimoto(), score.GetColorTanimoto()))
        dbmol = oechem. <math>OEMol()</math>molidx = score.GetMolldx()if not moldb. GetMolecule (dbmol, molidx) :
            print ("Unable to retrieve molecule '%u' from the database" % molidx)
            continue
        mol = oechem.OEGraphMol(dbmol.GetConf(oechem.OEHasConfIdx(score.
\rightarrowGetConfIdx())))
        oechem. OESetSDData (mol, "ShapeTanimoto", "%. 4f" % score. GetShapeTanimoto())
        oechem. OESetSDData(mol, "ColorTanimoto", "%. 4f" % score. GetColorTanimoto())
        oechem. OESetSDData (mol, "TanimotoCombo", "%. 4f" % score. GetTanimotoCombo ())
        score.Transform(mol)
        oechem.OEWriteMolecule(ofs, mol)
   print ("Wrote results to %s" % argv[3])
```

```
= ' \_ \text{main} ':
if
     _name_
    sys.exit(main(sys.argv))
```

## **6.2.3 UserInertialStarts**

return 0

OEFastROCSOrientation, UserInertialStarts allows custom coordinates to be used as starting positions for optimization. Using the 4TMN ligand from the Introduction as an example, optimization can be done at the atom highlighted in green below:

![](_page_47_Picture_5.jpeg)

#### Fig. 6: 4TMN Ligand with atom 34 highlighted green

Before running the program, the index of the desired atom needs to be identified. This can be accomplished by loading the molecule in VIDA and turning on atom indices. In this example, the atom's index is identified as idx 34. With this information, the x,y,z coordinates of atom idx 34 are pulled via the code snippet below. These coordinates are then used as user-defined starting coordinates:

```
startsCoords = oechem.OEFloatVector()
xyz = query {GetCoordinates() [34]}for x in xyz:
    startsCoords.append(x)
```

To use the OEFastROCSOrientation. UserInertialStarts method, set OEShapeDatabaseOptions. SetInitialOrientation and then input the starts vector using OEShapeDatabaseOptions. SetUserStarts:

```
opts.SetInitialOrientation(oefastrocs.OEFastROCSOrientation_UserInertialStarts)
opts. SetUserStarts(oechem. OEFloatVector(startsCoords), int(len(startsCoords)/3))
```

The first argument of OEShapeDatabaseOptions. SetUserStarts is the startsCoords vector created previously. This must be of the type OEF loat Vector. The second argument is the number of user-defined starting coordinates to optimize.

In this example, only 1 user-defined starting point has been set. There is no limit to the number of user-defined starts however, it should be noted that performance is inversely proportional to the number of starts being optimized.

To check that the starts have been set correctly, query OEShapeDatabaseOptions. GetInitialOrientation and OEShapeDatabaseOptions. GetNumUserStarts:

```
if opts. GetInitialOrientation () == oefastrocs. OEFastROCSOrientation
\rightarrowUserInertialStarts:
    numStarts = opts.GetNumUserStarts()
    oechem. OEThrow. Info ("This example will use %u starts" % numStarts)
```

The output from the modified Python script now looks like this:

```
Opening database file 3tmn_lig.sdf ...
This example will use 1 starts
Searching for 4tmn_lig.sdf
Score for mol 0(conf 0) 0.289689 shape 0.358462 color
Score for mol 0(conf 0) 0.320501 shape 0.098301 color
Score for mol 0(conf 0) 0.283724 shape 0.012400 color
Score for mol 0(conf 0) 0.145704 shape 0.023627 color
```

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
import os
import sys
from openeye import oechem
from openeye import oefastrocs
oepy = os.path.join(os.path.dirname(_file_), "..", "python")
sys.path.insert(0, os.path.realpath(oepy))
def main(argv=[_name_]):
    if len(argv) < 4:
        oechem. OEThrow. Usage ("% s < database> < queries> < hits. oeb>" % argv[0])
        return 0
```

```
# check system
   if not oefastrocs. OEFastROCSIsGPUReady () :
       oechem. OEThrow. Info ("No supported GPU available!")
       return 0
   # read in database
   dbname = \arg v[1]if oechem. OEIsGZip (dbname) :
       oechem. OEThrow. Fatal ("%s is an unsupported database file format as it is.
\rightarrowgzipped. \n"
                             "Preferred formats are .oeb, .sdf or .oez", dbname)
   print ("Opening database file %s ..." % dbname)
   dbase = ofastrocs. OEShapeDatabase()moldb = occhem.OEMolDatabase()if not moldb. Open (dbname) :
       oechem. OEThrow. Fatal ("Unable to open '%s'" % dbname)
   dots = occhem. 0ETH readed Dots (10000, 200, "conforms")if not dbase. Open (moldb, dots):
       oechem. OEThrow. Fatal ("Unable to initialize OEShapeDatabase on '%s'" % dbname)
   # customize search options
   opts = oefastrocs.OEShapeDatabaseOptions()
   opts.SetInitialOrientation(oefastrocs.OEFastROCSOrientation_UserInertialStarts)
   opts.SetLimit(5)
   qfname = argv[2]# read in query
   qfs = oechem.oemolistream()if not qfs.open(qfname):
       oechem. OEThrow. Fatal ("Unable to open '%s'" % qfname)
   query = occhem. OEGraphMol()if not oechem. OEReadMolecule (qfs, query) :
       oechem. OEThrow. Fatal ("Unable to read query from '%s'" % qfname)
   # write out everthing to a similary named file
   ofs = occhem.oemolostream()if not ofs.open(argV[3]):
       oechem. OEThrow. Fatal ("Unable to open '%s'" % argv[3])
   oechem.OEWriteMolecule(ofs, query)
   startsCoords = oechem.OEFloatVector()
   atomIdx = 1xyz = query. GetCoords () [atomIdx]
   for x in xyz:
       startsCoords.append(x)
   if not len(startsCoords) % 3 == 0:
       oechem. OEThrow. Fatal ("Something went wrong whilst reading in user-starts
\rightarrowcoordinates")
   opts.SetUserStarts(oechem.OEFloatVector(startsCoords), int(len(startsCoords)/3))
   opts.SetMaxOverlays(opts.GetNumInertialStarts() * opts.GetNumUserStarts())
```

```
if opts.GetInitialOrientation() == oefastrocs.OEFastROCSOrientation_
\rightarrowUserInertialStarts:
         numStarts = opts.GetNumUserStarts()
         print ("This example will use %u starts" % numStarts)
    print ("Searching for %s" % qfname)
    for score in dbase. GetSortedScores (query, opts) :
        print ("Score for mol %u(conf %u) %f shape %f color" % (
                score.GetMolIdx(), score.GetConfIdx(),
                score.GetShapeTanimoto(), score.GetColorTanimoto()))
         dbmol = occhem. OEMol()molidx = score.GetMolldx()if not moldb. GetMolecule (dbmol, molidx):
             print ("Unable to retrieve molecule '%u' from the database" % molidx)
             continue
        mol = oechem.OEGraphMol(dbmol.GetConf(oechem.OEHasConfIdx(score.
\rightarrowGetConfIdx())))
        oechem. OESetSDData(mol, "ShapeTanimoto", "%. 4f" % score. GetShapeTanimoto())<br>oechem. OESetSDData(mol, "ColorTanimoto", "%. 4f" % score. GetColorTanimoto())
         oechem. OESetSDData (mol, "TanimotoCombo", "%. 4f" % score. GetTanimotoCombo())
         score.Transform(mol)
         oechem.OEWriteMolecule(ofs, mol)
    print ("Wrote results to %s" % argv[3])
    return 0
if _name_ == '_main_':
    sys.exit(main(sys.argv))
```

### **6.2.4 Asls**

The final method to be discussed is  $OEFastROCSOrientation.AsIs$ . In this method, only one optimization is carried out at the query and the database molecule's original coordinates. No inertial starts are optimized.

When using this method, the database intended to be searched must be reloaded using  $OEShapeDatalog$ . Open. This ensures that the database molecules are not centered or set to an inertial frame of reference as is usually done. When reloading the database, the OEFastROCSOrientation. As Is constant must be passed to the Open routine:

```
oechem. OEThrow. Info ("Opening database file %s ..." % sys.argv[2])
dbase = oefastrocs. OEShapeDatabase()
moldb = oechem.OEMolDatabase()
moldb.Open(sys.argv[2])
dbase.Open(moldb, oefastrocs.OEFastROCSOrientation AsIs)
```

```
set the
              OEFastROCSOrientation.AsIs option
                                                   with OEShapeDatabaseOptions.
Next.
SetInitialOrientation:
```

opts. SetInitialOrientation (oefastrocs. OEFastROCSOrientation\_AsIs)

This will force the number of starts and the number of inertial starts to both equal 1. To check that the starts have

been set correctly, query OEShapeDatabaseOptions. GetNumStarts and OEShapeDatabaseOptions. GetNumInertialStarts:

```
if opts.GetInitialOrientation() == oefastrocs.OEFastROCSOrientation_AsIs:
    numStarts = opts.GetNumStarts()
    numInertialStarts = opts.GetNumInertialStarts()
    oechem. OEThrow. Info ("This example will use %u starts & %u inertial starts"
                        % (numStarts, numInertialStarts))
```

The output from the modified Python script now looks like this:

```
Opening database file 3tmn_lig.sdf ...
This example will use 1 starts & 1 inertial starts
Searching for 4tmn_lig.sdf
Score for mol 0(conf 0) 0.286799 shape 0.356514 color
```

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
import os
from openeye import oechem
from openeye import oefastrocs
oopy = os.path.join(os.path.dirname(file)), "..", "python")
sys.path.insert(0, os.path.realpath(oepy))
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) < 3:
        oechem.OEThrow.Usage("%s <database.oeb> <queries> <hits.oeb>" % argv[0])
        return 0
    # check system
    if not oefastrocs. OEFastROCSIsGPUReady():
        oechem. OEThrow. Info ("No supported GPU available!")
        return <sub>0</sub># read in database
```

```
dbname = \text{argv}[1]
```

if oechem. OEIsGZip (dbname) :

```
(continued from previous page)
```

```
oechem. OEThrow. Fatal ("%s is an unsupported database file format as it is,
\rightarrowgzipped.\n"
                              "Preferred formats are .oeb, .sdf or .oez", dbname)
   print ("Opening database file %s ..." % dbname)
   dbase = oefastrocs. OEShapeDatabase()
   moldb = oechem.OEMolDatabase()
   if not moldb. Open (dbname) :
       oechem. OEThrow. Fatal ("Unable to open '%s'" % dbname)
   dots = occhem.OEFhreadedDots(10000, 200, "conformers")if not dbase. Open (moldb, dots, oefastrocs. OEFastROCSOrientation_AsIs) :
       oechem. OEThrow. Fatal ("Unable to initialize OEShapeDatabase on '%s'" % dbname)
   # customize search options
   opts = oefastrocs.OEShapeDatabaseOptions()
   opts. SetInitialOrientation (oefastrocs. OEFastROCSOrientation_AsIs)
   opts.SetLimit(50)
   opts.SetMaxConfs(5)
   opts. SetMaxOverlays (opts. GetNumInertialStarts () * opts. GetNumStarts ())
   if opts.GetInitialOrientation() == oefastrocs.OEFastROCSOrientation_AsIs:
       numStarts = opts.GetNumStarts()
       numInertialStarts = opts.GetNumInertialStarts()
       oechem. OEThrow. Info ("This example will use \frac{2}{3}u starts & \frac{2}{3}u inertial starts"
                             % (numStarts, numInertialStarts))
   qfname = argv[2]# read in query
   qfs = oechem.oemolistream()if not qfs.open(qfname):
       oechem. OEThrow. Fatal ("Unable to open '%s'" % qfname)
   query = occhem. OEGraphMol()if not oechem. OEReadMolecule (qfs, query) :
       oechem. OEThrow. Fatal ("Unable to read query from '%s'" % qfname)
   # write out everthing to a similary named file
   ofs = occhem.oemolostream()if not ofs.open(argV[3]):
       oechem. OEThrow. Fatal ("Unable to open '%s'" % argv[3])
   oechem.OEWriteMolecule(ofs, query)
   print ("Searching for %s" % gfname)
   for score in dbase. GetSortedScores (query, opts):
       print ("Score for mol %u(conf %u) %f shape %f color" % (
               score.GetMolIdx(), score.GetConfIdx(),
              score.GetShapeTanimoto(), score.GetColorTanimoto()))
       dbmol = oechem. <math>OEMol()</math>molidx = score.GetMolldx()if not moldb. GetMolecule (dbmol, molidx) :
           print ("Unable to retrieve molecule '%u' from the database" % molidx)
           continue
       mol = oechem. OEGraphMol(dbmol. GetConf(oechem. OEHasConfIdx(score.
```

 $\rightarrow$ GetConfIdx())))

```
oechem. OESetSDData (mol, "ShapeTanimoto", "%. 4f" % score. GetShapeTanimoto())
        \verb|oechem.OESetSDData(mol,' "ColorTanimoto", "*, 4f" " score.GetColorTanimoto())|oechem. OESetSDData(mol, "TanimotoCombo", "%. 4f" % score. GetTanimotoCombo())
        score.Transform(mol)
        oechem.OEWriteMolecule(ofs, mol)
    print ("Wrote results to %s" % argv[3])
    return <sub>0</sub>if name == 'main:
    sys.exit(main(sys.argv))
```

### **6.2.5 Retrieving Results**

Finally, when using alternative starts, the way the results are handled should be taken into consideration. This will be unique to each specific problem. Here are some methods that may be useful:

opts.SetMaxOverlays(opts.GetNumInertialStarts() \* opts.GetNumUserStarts())

OEShapeDatabaseOptions. SetMaxOverlays allows the user to specify how many overlay results to return per conformer. In the above example, SetMaxOverlays has been set to return all possible overlays per conformer. This can be used along side the OEShapeDatabaseOptions. SetMaxConfs and/or OEShapeDatabaseOptions. SetLimit options:

```
opts.SetLimit(50)
opts.SetMaxConfs(5)
```

In this case, the results will be filtered twice. First, only the top 5 conformers for each molecule will be kept. For these 5 conformers all overlays will be kept. Finally, during sorting, only the top 50 scores of all overlays for the top 5 conformers per molecule will remain.

Warning: It is not recommended to return all overlay results for all conformers of large databases as this will leak memory rapidly.

**Note:** Please send any feedback about this tutorial to support@eyesopen.com using the tutorial title as the subject header.

# 6.3 Tutorial 2: How to prepare a database for faster load speeds

In this tutorial, you will learn how to pre-process a conformer database file for **FastROCS TK**, allowing for faster database load times with OEShapeDatabase. Open. Load times could be up to 10x faster. See the figure below for an eMolecules dataset of 14 million conformers.

To gain this extra loading performance, you need to use the following functions:

1. OEPreserveRotCompress - this function works on the input molecule stream to ensure that rotor-offset compression is preserved during the preparation process. Rotor offset compression is a way of storing con-

![](_page_54_Figure_1.jpeg)

Fig. 7: Pre-Processing Performance Impact

formers as a set of torsions instead of storing the coordinates for every single conformer of a molecule. This optimization reduces the memory footprint of a multi-conformer molecule.

- 2. OEPRECompress this function works on the output molecule stream object allowing the molecules to be stored in a 'pre-compressed' format:
  - Writes rotor-offset-compressed molecules in the perfect-rotor-encoding format
  - There is no need to Gzip which means faster OEMolDatabase. Open.
- 3. OEPrepareFastROCSMol this function works on each OEMol record of the input.oeb:
  - Sets the energy of each conformer to 0.0 to avoid writing it to OEB.
  - Suppresses hydrogens and reorders reference conformers for compression.
  - Pre-calculates color atoms.
  - Pre-calculates self-color and self-shape terms for all conformers.

The color terms cached by OEPrepareFastROCSMol are from the Note: OEColorFFType\_ImplicitMillsDean color force field. A different color force field can be given as the second argument to override ImplicitMillsDean.

In general, calling OEPrepareFastROCSMo1 and OEPRECompress will result in a smaller OEB file than the default OEB.GZ output from OMEGA.

Further reduction in file-size can be achieved by using an OEMCMolType HalfFloatCartesian molecule to store reference coordinates and torsions as 16-bit floating point.

Here is some example code showing how to pre-process a database with OEPrepareFastROCSMo1, save to a precompressed format, and reduce the file size by using half precision:

For added convenience, we have created a SimplePrepScript.py example script which can be modified to meet your exact needs:

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
import os
import sys
from openeye import oechem
from openeye import oefastrocs
oepy = os.path.join(os.path.dirname(_file_), "..", "python")
sys.path.insert(0, os.path.realpath(oepy))
def main(argv=[\underline{\hspace{1cm}}]name\underline{\hspace{1cm}}]):
    if len(argv) < 3:
        oechem. OEThrow. Usage ("%s input.oeb output_prepped_database.oeb" % argv[0])
        return <sub>0</sub># Input mol stream
   if s = oechem. oemolistream()ifs.open(argv[1])
    # PRE-Compress output mol stream
   ofs = occhem, oemolostream()oechem.OEPRECompress(ofs)
   ofs.open(argv[2])
    # Prepare mol & write to stream
    oechem.OEPreserveRotCompress(ifs)
```

```
for mol in ifs. GetOEMols():
        oefastrocs. OEPrepareFastROCSMol(mol)
        \verb|halfMol| = oechem. 0EMol(mol, oechem. 0EMCMolType_HalfFloatCartesian)|oechem.OEWriteMolecule(ofs, halfMol)
    ofs.close()
if __name__ == '__main__':sys.exit(main(sys.argv))
```

## **SEVEN**

**API** 

# **7.1 OEFastROCS Classes**

## 7.1.1 OEDBTracer

class OEDBTracer : public OEDBTracerBase

A thread-safe implementation of OEDBTracerBase meant for tracking the progress of a OEShapeDatabase query.

The following methods are publicly inherited from OEDBTracerBase:

| $ \Gamma$ $\Gamma$ $\Omega$<br>. . | Update |  |
|------------------------------------|--------|--|
|------------------------------------|--------|--|

### **Constructors**

OEDBTracer( $size_t$  numBins=0)

Construct a new thread-safe OEDBTracer object and initialize the internal synchronization primitives that are required.

The numBins argument specifies how many bins the internal OEFastROCSHistogram will have. The granularity of each bin is the determined by the range of the score divided by the number of bins. Note, OEShapeDatabaseType\_Shape and OEShapeDatabaseType\_Color have a range of 0.0-1.0, while OEShapeDatabaseType Combo has a range of 0.0-2.0.

### **GetCounts**

OEULongLong GetCounts (bool blocking=false)

Returns the current number of conformers already searched by a OEShapeDatabase. This is a thread-safe function for querying the current progress of the database search. OEShapeDatabase will update the progress of this tracer through the OEDBTracer. Update method from multiple threads. This function can be used by another thread to query that total progress.

The optional blocking parameter specifies whether the call should wait until there has been an update to the tracer before returning. This can be useful for making progress updates not spin too rapidly reporting the same number every time.

#### **GetHistogram**

OEFastROCSHistogram GetHistogram ()

Return a copy of the histogram currently accumulated in this database query as a OEFastROCSHistogram object. This histogram will be empty if numBins passed to the constructor is 0.

This is a thread-safe function for querying the current distribution of scores for the molecules already processed. The full histogram of the scores is not available until the value returned by  $OEDBTracer$ . Get Counts is equal to OEDBTracer.GetTotal.

### **GetNumBins**

size\_t GetNumBins() const

Return the number of bins to use for the score histogram during this particular query. Returning '0', the default, will indicate to OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores to skip histogram creation all together.

### **GetTotal**

OEULongLong GetTotal()

Return the total number of conformers to be processed.

**Warning:** It is possible for this function to return  $\theta$  for a short time after a call to  $OEShapeDatabase$ . GetScores or OEShapeDatabase. GetSortedScores. So a 0 return value should be taken with a grain of salt of that possible race-condition.

### **SetTotal**

void SetTotal (OEULongLong total)

Called by OEShapeDatabase. GetScores and OEShapeDatabase. GetSortedScores to set whatever the total number of conformers that will be processed.

#### **Update**

```
void Update (OEULongLong step=1,
            const OEFastROCSHistogram *hist=NULL)
```

Called by OEShapeDatabase. GetScores and OEShapeDatabase. GetSortedScores from multiple threads to communicate the current progress of the search.

## 7.1.2 OEDBTracerBase

class OEDBTracerBase

Abstract base class used by OEShapeDatabase to track the progress of an individual search against the database. Users should derive from this class and pass the derived class into OEShapeDatabaseOptions. Set Tracer for the options object later passed into OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores.

**Warning:** OEShapeDatabase.GetScores and OEShapeDatabase.GetSortedScores are multithreaded functions, so the Update method implemented by a derived class should be thread-safe.

The following classes derive from this class and should be used in preference of creating a custom tracer:

 $\bullet$  OEDBTracer

### **GetNumBins**

size t GetNumBins () const

Return the number of bins to use for the score histogram during this particular query. Returning '0', the default, will indicate to OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores to skip histogram creation all together.

### **SetTotal**

**void** SetTotal (OEULongLong total) =0

Called once by OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores in a single thread to indicate the total number of conformers that will be searched.

### **Update**

void Update (OEULongLong step=1, const OEFastROCSHistogram \*hist=NULL)=0

Called many times by OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores from many operating system threads so this function should be thread-safe. The OEShapeDatabase object will pass in a large step size to optimize the number of times this function is called, typically only hundreds of times will this method be called for a database containing millions of conformers. The step corresponds to the number of conformers already searched. Even so, this function should be implemented with very efficiently as it is called by the OEShapeDatabase search threads, so forward progress can not be made if this function is costly.

The optional hist argument is a OEFastROCSHistogram to accumulate into a master histogram for the entire query. Typically, OEShapeDatabase. GetScores and OEShapeDatabase. GetSortedScores will submit will call this method once for very large chunks of the database. This makes the synchronization point of calling this function very minimal to the overall runtime of the query. If a NULL pointer is passed, the default, no histogram accumulation will occur.

**Warning:** The implementer of a sub-class of *OEDBTracerBase* should guarantee the thread-safety of this method.

## 7.1.3 OEFastROCSHistogram

#### class OEFastROCSHistogram

This class is returned from OEDBTracer.GetHistogram during and after a query is sent to OEShapeDatabase.GetScores or OEShapeDatabase.GetSortedScores. It is used to contain a list of frequencies representing the distribution of scores. This same container is used to contain the frequencies of the following 3 score types:

- OEShapeDatabaseType\_Shape
- · OEShapeDatabaseType\_Color
- · OEShapeDatabaseType\_Combo

### **Constructors**

OEFastROCSHistogram (size\_t numBins=200)

Construct a new histogram with the specified number of "bins" in which to bin the score distribution. The same number of bins is applied to each score type.

OEFastROCSHistogram (const OEFastROCSHistogram & rhs)

Copy constructor for moving a OEFastROCSHistogram in memory.

### GetHistogram

```
void GetHistogram (std::vector<unsigned int> &frequencies,
                  unsigned int scoreType)
```

Initializes the frequencies vector to the required size to contain the number of bins for this histogram, then fills it with the number of molecules that falls within each bin for the scoreType specified. The scoreType should be one of the following:

- · OEShapeDatabaseType\_Shape
- · OEShapeDatabaseType\_Color
- · OEShapeDatabaseType\_Combo

#### **GetNumBins**

```
size_t GetNumBins() const
```

Returns the number of bins used for this histogram. The number of bins determines the granularity of the scores.

**Update** 

void Update (const OEFastROCSHistogram & rhs)

Sum the histogram rhs into this histogram. This histogram will then reflect the total of the two histograms. Used for aggregating histograms during the execution of OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores.

void Update (const OEShapeDatabaseScore &score)

Updates this histogram from an individual OEShapeDatabaseScore object usually representing one molecule during the execution of OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores.

## 7.1.4 OEShapeDatabase

```
class OEShapeDatabase
```

This is the primary class for performing **FastROCS TK** calculations. It is a very heavy-weight object:

- consuming many gigabytes of memory
- managing many host threads
- managing all GPU interaction

The goal is to allow abstracting away the complexities as much as possible to allow writing to a single API, allowing for the improvement of the underlying compute engine over time.

Ideally, this class is initialized once per dataset. There is a fair amount of pre-calculation done on each molecule and conformer while being loaded into memory. Some of this can be alleviated by pre-calculating and caching, but not all of it, as there is a balance between caching and recalculation that is always being tuned.

### **Constructors**

```
OEShapeDatabase (const OEShape:: OEColorForceField &cff)
OEShapeDatabase (unsigned int dbtype=OEShapeDatabaseType::Default,
                unsigned int cfftype=OEShape:: OEColorFFType:: OEDefault)
```

Create a new OEShapeDatabase for managing conformers and performing **FastROCS TK** calculations.

Whether the OEShapeDatabase can perform color calculations must be chosen at construction. If "shape only" is chosen by passing OEShapeDatabaseType\_Shape, then there can be significant memory and load-time performance improvements. Color atom assignment can be a significant cost during load and increase memory usage by roughly 2x.

A custom OEColorForceField can be passed to this constructor as well to allow color scoring to be completely customized. Note, in the case of a custom color force field, OEShapeDatabaseType\_Default is assumed. It is currently not possible to perform a "color only" scoring.

### **AddMol**

```
unsigned int AddMol (const OEChem:: OEMCMolBase &mol,
                    const unsigned orient = OEFastROCSOrientation:: Inertial))
```

Add a new collection of conformers to this database and return the index used to identify this molecule. This index will start at 0 and monotonically increase by 1 for every multi-conformer molecule added. OEShapeDatabaseScore.  $GetMOLIdx$  will return this index to be able to map **FastROCS** scores to molecules added through this mechanism.

If using alternative start method OEFastROCSOrientation AsIs, this constant needs to be passed as the final argument to the AddMol routine so the database can be loaded without pre-processing conformer coordinates. The final argument is ignored for all other use cases and does not need to be changed from the default argument as all molecules are identically pre-processed for all other starting points.

**Warning:** Databases must be re-added if using OEFastROCSOrientation\_AsIs

**Note:** Even though this method is not const, it has been made thread-safe so that it can be called from multiple threads. Furthermore, it has been optimized as much as possible to parallelize the pre-calculation this method performs. This makes it very efficient to use multiple threads to load a database file into memory.

### **GetColorForceFieldType**

unsigned int GetColorForceFieldType() const

Return a constant from the OECOLOTEFType namespace to indicate the color force field used to construct this database. Returns OEColorFFType Custom if a custom OEColorForceField object was passed to the constructor.

### **GetColorGridSpacing**

float GetColorGridSpacing() const

Return the grid spacing used to calculate color scores. This defaults to 0.5 for good performance. Lower values will yield answers that agree more closely with the Exact analytical calculation, at the expense of performance. Higher values can yield better performance. The default was chosen as a good balance of virtual screening statistical analysis (AUCs) versus raw throughput performance.

### **GetDatabaseType**

```
unsigned int GetDatabaseType() const
```

Returns a constant from the OEShapeDatabaseType namespace indicating what type of calculations this database can perform.

### **GetMaxNumDevices**

unsigned int GetMaxNumDevices () const

Returns the maximum number of GPU devices this database will use for calculations. The only way to restrict the GPUs seen by the database is to use the CUDA\_VISIBLE\_DEVICES environment variable before starting the process.

See also:

· OEShapeDatabase. SetNumDevices

#### **GetMaxOptIterations**

unsigned int GetMaxOptIterations() const

Return the number of optimizer iterations the **FastROCS** algorithm should use when optimizing the alignment of the database conformer and the query conformer. This currently defaults to 10 based upon analysis of producing good virtual screening statistics (AUCs) without excessive iterations that would cost performance.

#### **GetNumDevices**

unsigned int GetNumDevices () const

Returns the number of GPU devices this database will use for calculation. This will default to all the GPUs that are visible, i.e., the value returned from OEShapeDatabase. GetMaxNumDevices.

#### **GetNumOpenThreads**

unsigned int GetNumOpenThreads() const

Return how many CPU threads will be used to read a OEMolDatabase from disk into memory using the  $OEShapeDatabase$ . Open method. The default, a value of 0, is to use as many CPUs as can be found on the system with OEGetNumProcessors.

### **GetScores**

```
OESystem::OEIterBase<OEShapeDatabaseScore> *
  GetScores (const OEChem:: OEMolBase & query,
            const OEShapeDatabaseOptions &options=OEShapeDatabaseOptions()) const
OESystem:: OEIterBase<OEShapeDatabaseScore> *
  GetScores (const OEShape:: OEShapeQueryPublic & shapeQry,
            const OEShapeDatabaseOptions &options=OEShapeDatabaseOptions()) const
OESystem:: OEIterBase<OEShapeDatabaseScore> *
  GetScores (const OEShape:: OEShapeQuery & shapeQry,
            const OEShapeDatabaseOptions &options=OEShapeDatabaseOptions()) const
```

Return ALL scores of the query against the entire database subject to the options specified in the OEShape-DatabaseOptions passed to this method. This is useful for performing larger scale NxN clustering type of calculations where all pairs of scores need to be processed.

The query can be either a single conformer OEMolBase, a OEShapeQuery or a OEShapeQueryPublic object read from a . sq file. OEShapeQuery or OEShapeQueryPublic objects must contain a molecule. To determine if your OEShapeQuery object is FastROCS-friendly see OEIsFastROCSShapeQuery in the Shape TK.

**Warning:** The order of the OEShapeDatabaseScore returned by the iterator is non-deterministic and will certainly change for each execution due to the multi-threaded nature of this method. However, the values calculated in each OEShapeDatabaseScore will be the same. Therefore, users should rely on the return value of OEShapeDatabaseScore. GetMolIdx and OEShapeDatabaseScore. GetConfIdx to do further processing, not the location within the iterator.

### See also:

The OEShapeDatabaseOptions class is used to control many of the parameters to this method. For example, how many conformers per molecule to return.

### **GetShapeGridSpacing**

float GetShapeGridSpacing() const

Return the grid spacing used to calculate shape scores and drive the alignment. This defaults to  $0.5$  for good performance. Lower values will yield answers that agree more closely with the Exact analytical calculation, at the expense of performance. Higher values can yield better performance. The default was chosen as a good balance of virtual screening statistical analysis (AUCs) versus raw throughput performance.

### **GetSortedScores**

```
OESystem:: OEIterBase<OEShapeDatabaseScore> *
  GetSortedScores (const OEChem:: OEMolBase &query, unsigned int limit=0) const
OESystem:: OEIterBase<OEShapeDatabaseScore> *
  GetSortedScores (const OEChem:: OEMolBase & query,
                   const OEShapeDatabaseOptions &options) const
OESystem::OEIterBase<OEShapeDatabaseScore> *
  GetSortedScores(const OEShape:: OEShapeQueryPublic & shapeQry,
                   const OEShapeDatabaseOptions & options=OEShapeDatabaseOptions())
\rightarrowconst
OESystem:: OEIterBase<OEShapeDatabaseScore> *
  GetSortedScores (const OEShape:: OEShapeQuery & shapeQry,
                   const OEShapeDatabaseOptions &options=OEShapeDatabaseOptions())
\rightarrowconst
```

Return a hitlist of the query against the database based upon the scoring options of the database and the OEShape-DatabaseOptions passed to this method. The OEShapeDatabaseScore will be returned in descending order, i.e., the better 'hits' will come first in the iterator.

The query can be either a single conformer OEMolBase, a OEShapeQuery or a OEShapeQueryPublic object read from a . sq file. OEShapeQuery or OEShapeQueryPublic objects must contain a molecule. To determine if your OEShapeOuery object is **FastROCS**-friendly see OEIsFastROCSShapeOuery in the **Shape TK**.

Note: This method is typically used to select only a subset of the results based upon limit or OEShapeDatabaseOptions. SetLimit. It is optimized for rapidly constructing relatively small hitlists. If the entire set of scores for the database is desired, it can be faster to use the OEShapeDatabase. GetScores to avoid the sorting operation.

#### See also:

The OEShapeDatabaseOptions class is used to control many of the parameters to this method. For example, how

many conformers per molecule to return.

### **NumConfs**

unsigned int NumConfs() const

Return the number of conformers the database is currently managing. Useful for getting a ballpark idea of the underlying memory usage.

**Note:** This value has no relation to the indexes returned by OEShapeDatabase. AddMo1, except that this value will always be larger than the last index returned.

### Open

```
bool Open (const OEChem:: OEMolDatabase &moldb,
          const unsigned int orient=OEFastROCSOrientation::Default)
bool Open (const OEChem:: OEMolDatabase & moldb,
          OESystem:: OEThreadedDots &dots,
          const unsigned int orient=OEFastROCSOrientation::Default)
```

Initialize the database using a OEMolDatabase. This is the most efficient way to initialize a OEShapeDatabase as this method will launch an operating thread for each CPU core available and parallelize all the parsing and pre-calculation. The progress of the loading operation can be tracked through a thread-safe OEThreadedDots object.

If using alternative start method OEFastROCSOrientation AsIs, this constant needs to be passed as the final argument to the Open routine so the database can be loaded without adjusting conformer coordinates. The final argument can be left blank for all other use cases.

Warning: Databases must be re-opened if using OEFastROCSOrientation\_AsIs

This method will block and return true when the database has been successfully loaded into memory.

**Note:** The indices returned by OEShapeDatabaseScore. GetMolIdx are guaranteed to map directly into the OEMolDatabase index space. OEMolDatabase. GetMolecule can fail and return no molecule for good reason, i.e., an empty molecule from an SD file. Therefore, the index space used by OEShapeDatabase can have "holes" when initialized from a OEMolDatabase.

#### **PrintMemoryUsage**

```
void PrintMemoryUsage (OEPlatform:: oeostream &os) const;
void PrintMemoryUsage() const;
```

Print out memory usage statistics for this object. This will break down how much memory is being used to pre-cache various parts of the calculation. By default, the output will be written to OEPlatform over. The output stream can also be passed as an argument. The diagnostic output is meant for human consumption and may change format in future releases.

### **SetColorGridSpacing**

**bool** SetColorGridSpacing (float gridSpacing)

Set the grid spacing to use for static color scoring.

#### See also:

· OEShapeDatabase.GetColorGridSpacing

#### **SetMaxOptIterations**

void SetMaxOptIterations (unsigned int maxIter)

Set the number of optimizer iterations to use when optimizing the alignment by shape.

#### See also:

· OEShapeDatabase. GetMaxOptIterations

#### **SetNumDevices**

void SetNumDevices (unsigned int ndevices)

Set the number of GPU devices this calculation should use. This number should be between 1 and OEShapeDatabase. GetMaxNumDevices inclusively. This method is really only useful to efficiently collecting FastROCS scalability data across multiple GPUs. To restrict OEShapeDatabase to only run on a subset of GPUs on the machine, use the CUDA VISIBLE DEVICES environment variable instead before the process is launched.

#### **SetNumOpenThreads**

void SetNumOpenThreads (unsigned int numThrds)

Set how many CPU threads should be created to read a OEMolDatabase from disk into memory using the OEShapeDatabase. Open method. A value of 0 specifies that all CPUs in the system will be used. The value passed to this method should not exceed the value returned by OEGetNumProcessors.

#### **SetShapeGridSpacing**

**bool** SetShapeGridSpacing (float gridSpacing)

Set the grid spacing to use for shape scoring and alignment.

#### See also:

· OEShapeDatabase.GetShapeGridSpacing

## 7.1.5 OEShapeDatabaseOptions

#### class OEShapeDatabaseOptions

This class is used to control the behavior of OEShapeDatabase. GetScores and OEShapeDatabase. Get Sorted Scores. It allows setting options on a per-search basis.

**Note:** It is possible for the options selected in this class to not match the settings of the constructed OEShapeDatabase causing an error to be thrown.

### **Constructors**

```
OEShapeDatabaseOptions()
OEShapeDatabaseOptions (const OEShapeDatabaseOptions &)
```

Default constructor for creating a new instance with default options. The copy constructor will copy all the options into a new object.

#### operator=

OEShapeDatabaseOptions & operator=(const OEShapeDatabaseOptions &)

Assignment operator for making a copy of the options.

### **ClearCutoff**

void ClearCutoff()

Removes the cutoff from this set of options. The default is to have no cutoff value specified.

- · OEShapeDatabaseOptions.GetCutoff
- · OEShapeDatabaseOptions. HasCutoff
- · OEShapeDatabaseOptions. SetCutoff
- · OEShapeDatabaseOptions.GetCutoffLT
- · OEShapeDatabaseOptions. HasCutoffLT
- · OEShapeDatabaseOptions. SetCutoffLT

### **ClearTracer**

```
void ClearTracer()
```

Removes the progress bar tracer from this set of options.

Note: This does not release the memory of the OEDBTracerBase previously passed to OEShapeDatabaseOptions.SetTracer.

#### See also:

OEShapeDatabaseOptions.SetTracer

#### **ClearUserStarts**

void ClearUserStarts()

Removes any user inertial starts that have been previously set.

#### See also:

OEShapeDatabaseOptions.SetUserStarts OEShapeDatabaseOptions.GetNumStarts

OEShapeDatabaseOptions.GetUserStarts

### **GetColorForceFieldType**

unsigned int GetColorForceFieldType() const

#### **GetColorOptimization**

bool GetColorOptimization() const;

Returns true if color score is being optimized in addition to shape score.

#### See also:

· OEShapeDatabaseOptions. SetColorOptimization

#### **GetCutoff**

float GetCutoff() const

Returns the cutoff currently set in this set of options. The default is a cutoff of  $0.0$ , i.e., no cutoff, all scores will be returned. This is mutually exclusive to OEShapeDatabaseOptions. GetCutoffLT.

**Note:** This cutoff is applied to the final ranking score used. For a OEShapeDatabaseType\_Shape database, that means only the "shape" score. For the default database type, OEShapeDatabaseType\_Default, the cutoff is applied to the sum of the shape and color components (OEShapeDatabaseScore. GetTanimotoCombo).

- · OEShapeDatabaseOptions. HasCutoff
- · OEShapeDatabaseOptions. SetCutoff
- · OEShapeDatabaseOptions. ClearCutoff

### **GetCutoffGT**

float GetCutoffGT() const

This method is identical in functionality to OEShapeDatabaseOptions. GetCutoff and is mutually exclusive to OEShapeDatabaseOptions.GetCutoffLT.

#### See also:

· OEShapeDatabaseOptions.GetCutoff

#### **GetCutoffLT**

float GetCutoffLT() const

Returns the cutoff currently set in this set of options. The default is no cutoff, all scores will be returned. This method applies to a cutoff set using OEShapeDatabaseOptions. SetCutoffLT to retrieve results less than or equal to the cutoff value.

**Note:** This cutoff is applied to the final ranking score used. For a OEShapeDatabaseType Shape database, that means only the "shape" score. For the default database type, OEShapeDatabaseType\_Default, the cutoff is applied to the sum of the shape and color components (OEShapeDatabaseScore. GetTanimotoCombo).

#### See also:

- · OEShapeDatabaseOptions. HasCutoffLT
- · OEShapeDatabaseOptions. SetCutoffLT
- · OEShapeDatabaseOptions. ClearCutoff

#### **GetInitialOrientation**

unsigned int GetInitialOrientation() const

Returns the initial orientation to be used for the overlay optimization drawn from the OEFastROCSOrientation namespace. The default orientation is OEFastROCSOrientation\_Inertial

- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions. GetNumStarts.. oe:method:: GetInitialOrientation

### **GetFastROCSMode**

unsigned int GetFastROCSMode() const

Returns the calculation mode to be used for the overlay optimization drawn from the OEFastROCSMode namespace. The default mode is OEFastROCSMode\_FastROCS

#### See also:

· OEShapeDatabaseOptions. SetFastROCSMode

#### **GetLimit**

unsigned int GetLimit() const

Returns the number of individual molecule "hits" that will be returned from OEShapeDatabase. Get Sorted Scores, i.e., the number of individual OEShapeDatabaseScore objects that will be returned.

**Note:** This method has no effect on the OEShapeDatabase. GetScores method.

### **GetMaxConfs**

unsigned int GetMaxConfs() const

Returns the maximum number of conformers to return per molecule. By default this value is 1 indicating only the best conformer of a molecule that matched the query molecule will be returned as a single OEShapeDatabaseScore object. The conformer with the highest score will be indicated by the OEShapeDatabaseScore. GetConfIdx method.

#### **GetMaxOverlays**

unsigned int GetMaxOverlays () const

Returns the maximum number of starting points per conformer overlaid. By default this value is 1 indicating only the best of all optimizations performed will be returned.

### **GetMaxRandomTranslation**

float GetMaxRandomTranslation() const

Returns the maximum allowed translation when using random starting orientations. The default maximum is 2 angstroms.

- · OEShapeDatabaseOptions. SetMaxRandomTranslation
- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetNumRandomStarts

- OEShapeDatabaseOptions. GetNumRandomStarts
- · OEShapeDatabaseOptions. SetRandomSeed
- · OEShapeDatabaseOptions.GetRandomSeed
- · OEFastROCSOrientation

### **GetNumInertialStarts**

unsigned int GetNumInertialStarts() const

Returns the number of inertial starts used as starting points for the shape optimization. The default value is 4 starting points oriented along the principle moment of inertia.

### **GetNumStarts**

```
unsigned int GetNumStarts() const
unsigned int GetNumStarts (const OEChem:: OEMolBase &query) const
```

Returns the number of alternative starting points for shape optimizaset tion. When OEFastROCSOrientation\_InertialAtHeavyAtoms using  $\alpha$ OEFastROCSOrientation\_InertialAtColorAtoms the query molecule is required by the method. If alternative starts have not been set or OEFastROCSOrientation\_AsIs is set, these methods will return a value of 1.

### See also:

- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions. SetUserStarts
- · OEShapeDatabaseOptions. ClearUserStarts
- · OEFastROCSOrientation

### **GetNumColorAtomStarts**

unsigned int GetNumColorAtomStarts (const OEChem:: OEMolBase &query) const

Returns This the number of color atom starting points set for shape optimization. method requires OEShapeDatabaseOptions.SetInitialOrientation to be set to OEFastROCSOrientation\_InertialAtColorAtoms and the query molecule. If the query molecule does not have color atoms the search will throw a warning and default to OEFastROCSOrientation\_Inertial.

- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetNumStarts
- · OEFastROCSOrientation

#### **GetNumHeavvAtomStarts**

unsigned int GetNumHeavyAtomStarts (const OEChem:: OEMolBase &query) const

the number of heavy atom starting points set for shape This Returns optimization. method requires OEShapeDatabaseOptions.SetInitialOrientation  $f_{\Omega}$ be set  $f<sub>O</sub>$ OEFastROCSOrientation\_InertialAtHeavyAtoms and the query molecule.

#### See also:

- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetNumStarts
- · OEFastROCSOrientation

#### **GetNumRandomStarts**

unsigned int GetNumRandomStarts()

Returns the number of random starting orientations when using the OEFastROCSOrientation\_Random alternative start. The default value is 10.

#### See also:

- · OEShapeDatabaseOptions. SetNumRandomStarts
- · OEFastROCSOrientation
- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetMaxRandomTranslation
- · OEShapeDatabaseOptions.GetMaxRandomTranslation
- · OEShapeDatabaseOptions. SetRandomSeed
- · OEShapeDatabaseOptions.GetRandomSeed

### **GetNumUserStarts**

unsigned int GetNumUserStarts() const

Returns the number of user-defined starting points set for shape optimization. This method requires OEShapeDatabaseOptions.SetInitialOrientation to be  $f_{\Omega}$ set OEFastROCSOrientation UserInertialStarts and user-starts with to have been set OEShapeDatabaseOptions.SetUserStarts.

- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions. SetUserStarts
- · OEShapeDatabaseOptions. ClearUserStarts
- · OEShapeDatabaseOptions.GetNumStarts
- · OEFastROCSOrientation

### **GetRandomSeed**

unsigned int GetRandomSeed() const

Returns the random seed to be used with OEFastROCSOrientation Random. The default random seed is set based on the time.

### See also:

- · OEShapeDatabaseOptions. SetRandomSeed
- · OEFastROCSOrientation
- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetNumRandomStarts
- · OEShapeDatabaseOptions.GetNumRandomStarts
- · OEShapeDatabaseOptions. SetMaxRandomTranslation
- · OEShapeDatabaseOptions.GetMaxRandomTranslation

#### **GetScoreType**

unsigned int GetScoreType() const

Returns the score type drawn from the OEShapeDatabaseType namespace to be used for the search.

#### **GetSimFunc**

unsigned int GetSimFunc() const

Returns the type of similarity function to be used to score the search results. The constant type returned is either 'Tanimoto' or 'Tversky' which is drawn from the OEShapeSimFuncType namespace.

#### **GetTracer**

OEDBTracerBase \*GetTracer() const

Returns a pointer to the *OEDBTracerBase* to be used to track the progress of this search. Returns a NULL pointer to indicate that no tracer has been registered.

#### GetTverskyAlpha

float GetTverskyAlpha() const

Returns the alpha coefficient used in the Tversky similarity calculation. See OEShapeDatabaseOptions. Set TverskyCoeffs for details of how to set alpha. The default value is 0.95.

#### **GetTverskyBeta**

float GetTverskyBeta() const

Returns the beta coefficient used in the Tversky similarity calculation. See OEShapeDatabaseOptions. Set TverskyCoeffs for details of how to set beta. The default value is 0.05.

### **GetUserStarts**

bool GetUserStarts (vector<float> &startsCoords) const

Fills a float vector of size number of starts  $*$  3 with the starting coordinates previously set with OEShapeDatabaseOptions. SetUserStarts. To ensure vector of the correct size is passed in as an argument, the OEShapeDatabaseOptions. GetNumStarts method can be used to retrieve the number of starts set. If successful the return value will be true. The following code snippet shows example usage in python.

coords = oechem. OEFloatVector (opts. GetNumStarts ()  $\star$  3) opts.GetUserStarts(coords)

Warning: Code is not available. FastROCS TK is only supported in Python.

#### See also:

- · OEShapeDatabaseOptions. ClearUserStarts
- · OEShapeDatabaseOptions. SetUserStarts

#### **HasCutoff**

bool HasCutoff() const

Returns a boolean value indicating whether a cutoff value, at which all scores greater than or equal to the value will be saved and all scores less than the value will be discarded, has been previously registered with this set of options. By default this is false, no cutoff. If OEShapeDatabaseOptions. SetCutoff or OEShapeDatabaseOptions. SetCutoffGT has been called already, this will return true. OEShapeDatabaseOptions. ClearCutoff will set this back to false again. This method is mutually exclusive to OEShapeDatabaseOptions. HasCutoffLT

- · OEShapeDatabaseOptions. HasCutoffGT
- · OEShapeDatabaseOptions.GetCutoff
- · OEShapeDatabaseOptions. SetCutoff
- · OEShapeDatabaseOptions. ClearCutoff

### **HasCutoffGT**

bool HasCutoffGT() const

This method is identical in functionality to OEShapeDatabaseOptions. HasCutoff and is mutually exclusive to OEShapeDatabaseOptions. HasCutoffLT.

#### See also:

- · OEShapeDatabaseOptions. HasCutoff
- · OEShapeDatabaseOptions.GetCutoffGT
- · OEShapeDatabaseOptions.SetCutoffGT
- · OEShapeDatabaseOptions. ClearCutoff

### **HasCutoffLT**

bool HasCutoffLT() const

Returns a boolean value indicating whether a cutoff value, at which all scores less than or equal to the value will be saved and all scores greater than the value will be discarded, has been previously registered with this set of options. By default this is false, no cutoffLT. If OEShapeDatabaseOptions. SetCutoffLT has been called already, this will return true. OEShapeDatabaseOptions. ClearCutoff will set this back to false again. This method is mutually exclusive to OEShapeDatabaseOptions. HasCutoffGT

#### See also:

- · OEShapeDatabaseOptions.GetCutoffLT
- · OEShapeDatabaseOptions. SetCutoffLT
- · OEShapeDatabaseOptions. ClearCutoff

### **SetColorForceField**

bool SetColorForceField(const OEShape:: OEColorForceField & cff)

### **SetColorForceFieldType**

**bool** SetColorForceFieldType (unsigned int type)

#### **SetColorOptimization**

void SetColorOptimization (bool ColorOptimization);

Set to true to optimize over color score in addition to shape score. Default is false.

Note: optimizing over color will impact performance. A decrease in 5-20% can be expected.

• OEShapeDatabaseOptions. GetColorOptimization

#### **SetCutoff**

void SetCutoff (float cutoff)

Sets the cutoff to use when filtering the results of OEShapeDatabase. GetScores and OEShapeDatabase. GetSortedScores. Only OEShapeDatabaseScore objects greater than or equal to cutoff depending on the score type will be returned. This method is mutually exclusive to OEShapeDatabaseOptions. SetCutoffLT

**Note:** This cutoff is applied to the final ranking score used. For a OEShapeDatabaseType\_Shape database, that means only the "shape" score. For the default database type, OEShapeDatabaseType\_Default, the cutoff is applied to the sum of the shape and color components (OEShapeDatabaseScore. GetTanimotoCombo).

#### See also:

- · OEShapeDatabaseOptions.GetCutoff
- · OEShapeDatabaseOptions. HasCutoff
- · OEShapeDatabaseOptions. ClearCutoff

### **SetCutoffGT**

void SetCutoffGT (float cutoff)

This method is identical in functionality to OEShapeDatabaseOptions. SetCutoff and is mutually exclusive to OEShapeDatabaseOptions. SetCutoffLT.

#### See also:

· OEShapeDatabaseOptions. SetCutoff

#### **SetCutoffLT**

void SetCutoffLT (float cutoff)

Sets the cutoff to use when filtering the results of OEShapeDatabase. GetScores and OEShapeDatabase. GetSortedScores. Only OEShapeDatabaseScore objects less than or equal to cutoff depending on the score type will be returned.

This method is mutually exclusive to OEShapeDatabaseOptions. SetCutoff.

**Note:** This cutoff is applied to the final ranking score used. For a OEShapeDatabaseType\_Shape database, that means only the "shape" score. For the default database type, OEShapeDatabaseType\_Default, the cutoff is applied to the sum of the shape and color components (OEShapeDatabaseScore. GetTanimotoCombo).

- · OEShapeDatabaseOptions.GetCutoffLT
- · OEShapeDatabaseOptions. HasCutoffLT
- · OEShapeDatabaseOptions. ClearCutoff

### **SetFastROCSMode**

unsigned int SetFastROCSMode (unsigned int ) const

Sets the calculation mode to be used for the overlay optimization drawn from the OEFastROCSMode namespace. The default mode is OEFastROCSMode\_FastROCS

#### See also:

· OEShapeDatabaseOptions. SetFastROCSMode

#### **SetInitialOrientation**

bool SetInitialOrientation (unsigned int orient=OEFastROCSOrientation::Default)

Set the initial orientation to be used for optimization of the overlap. The options are drawn from the OEFastROCSOrientation and the default is OEFastROCSOrientation\_Inertial. If user-defined inertial starts are to be used then the starting coordinates must be set using the OEShapeDatabaseOptions. SetUserStarts method. Returns true if successful.

#### See also:

- · OEShapeDatabaseOptions. SetUserStarts
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEFastROCSOrientation

#### **SetNumRandomStarts**

bool SetNumRandomStarts (unsigned int numStarts)

Set the number of random starting orientations when using the OEFastROCSOrientation\_Random alternative start. The default value is 10.

Warning: Search speed and the amount of RAM required are proportional to the number of starting orientations therefore speed & memory degradation are to be expected if searching with a large number of random starting orientations.

- · OEShapeDatabaseOptions. GetNumRandomStarts
- · OEFastROCSOrientation
- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetMaxRandomTranslation
- · OEShapeDatabaseOptions.GetMaxRandomTranslation
- · OEShapeDatabaseOptions. SetRandomSeed
- · OEShapeDatabaseOptions.GetRandomSeed

### **SetLimit**

void SetLimit (unsigned int limit)

Set the number of individual OEShapeDatabaseScore objects that will be returned by OEShapeDatabase. GetSortedScores. This is a hard limit regardless of the multiplicative effect of also setting the OEShapeDatabaseOptions. SetMaxConfs and OEShapeDatabaseOptions. SetMaxOverlays methods to values greater than 1.

Note: This method has no effect on the OEShapeDatabase. GetScores method.

### **SetMaxConfs**

void SetMaxConfs (unsigned int maxConfs)

Set how many conformers per molecule should be returned in the results. The default value is 1, only the best conformer for each database molecule will be returned as an OEShapeDatabaseScore object. The conformer with the highest score will be indicated by the OEShapeDatabaseScore. GetConfIdx method.

Setting this value to 0 means all database conformers will be returned for every molecule in the database.

#### **SetMaxOverlays**

void SetMaxOverlays (unsigned int maxOverlaysToReturn)

Set how many starting points to return per conformer in the database. The default value is 1, only the best starting point for the conformer will be returned as an OEShapeDatabaseScore object.

Setting this value to 0 means all the starting points will be returned, i.e., there will be OEShapeDatabaseOptions.GetNumInertialStarts objects returned.

#### **SetMaxRandomTranslation**

**bool** SetMaxRandomTranslation (float trans)

Set the maximum allowed translation for each random orientation. The default is 2 angstroms. This method requires OEShapeDatabaseOptions. SetInitialOrientation to be set to OEFastROCSOrientation Random.

- · OEShapeDatabaseOptions.GetMaxRandomTranslation
- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetNumRandomStarts
- · OEShapeDatabaseOptions.GetNumRandomStarts
- · OEShapeDatabaseOptions. SetRandomSeed
- OEShapeDatabaseOptions. GetRandomSeed

· OEFastROCSOrientation

### **SetNumInertialStarts**

void SetNumInertialStarts (unsigned int numStarts)

Set how many starting points the shape optimization will use. Currently, only values between 1 and 8 inclusive can be set. The default value is 4, i.e., assume there is a dominant moment of inertia for both the query and database conformer. Setting this value higher can yield better global overlays. However, there is a direct linear relation between the performance of FastROCS TK and the number of starting points.

### **SetRandomSeed**

bool SetRandomSeed (unsigned int seed)

Sets the random seed to be used with OEFastROCSOrientation\_Random. Returns true if successfully set. The default random seed is set based on the time.

#### See also:

- · OEShapeDatabaseOptions.GetRandomSeed
- · OEFastROCSOrientation
- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetNumRandomStarts
- · OEShapeDatabaseOptions.GetNumRandomStarts
- · OEShapeDatabaseOptions. SetMaxRandomTranslation
- · OEShapeDatabaseOptions.GetMaxRandomTranslation

### **SetScoreType**

void SetScoreType (unsigned int type)

Sets which scores to perform during the search. The constant type should be drawn from the OEShapeDatabaseType namespace.

Note: The score type must be a proper subset of the score enabled during OEShapeDatabase construction. That means if the database was started in "shape only" mode, this value can not include OEShapeDatabaseType\_Color.

#### **SetSimFunc**

void SetSimFunc (unsigned int type)

Sets which type of similarity function to use to score search results. The constant type should be either "Tanimoto" or "Tversky" and should be drawn from the OEShapeSimFuncType.

#### **SetTracer**

**void** SetTracer (OEDBTracerBase & tracer)

Register a progress bar tracer with this set of options. The tracer will be updated with a count as chunks of the database are processed. It is very important that the implementation of OEDBTracerBase is thread-safe as it will be updated from multiple threads simultaneously. It is also expected that the consumer of the progress bar will be operating in a separate thread to avoid wasting search thread time on progress update overhead.

**Warning:** The user must take care to keep the tracer in scope during the full duration of the OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores call. The options object will not make a copy of the tracer at all, merely storing a pointer to the tracer. If the tracer is prematurely deleted, this will very likely result in a crash. Probably in a non-deterministic way due to the threading involved.

#### **SetTverskyCoeffs**

void SetTverskyCoeffs (float alpha, float beta)

Sets the alpha and beta coefficients to be used in the Tversky similarity calculation. See the Molecular Shape section in the **Shape TK** theory documentation for a description of how this is calculated. Default values for alpha and beta are 0.95 and 0.05, respectively. Any new values of alpha and beta can be chosen provided they add up to 1.00.

### **SetUserStarts**

bool SetUserStarts (vector<float> &startsCoords, unsigned int numStarts)

Sets the user-defined starting coordinates. The arguments are a vector of floats of length 3 \* the number of starting points (x, y and z coordinates for each start) - startsCoords and the number of starting coordinates in an unsigned int variable - numStarts.

Warning: Currently, error checking is not performed for user-defined starting coordinates that fall out of scope of the molecule's coordinate range therefore, bad starting coordinates will yield zero shape/color overlap. It is the responsibility of the user to ensure sensible starting coordinates.

The following code snippet shows how to use OEShapeDatabaseOptions. SetInitialOrientation and OEShapeDatabaseOptions. SetUserStarts in a python example.

opts = oefastrocs.OEShapeDatabaseOptions() opts.SetInitialOrientation(oefastrocs.OEFastROCSOrientation\_UserInertialStarts)

```
startsCoords = oechem.OEFloatVector()
startsCoords.append(float(1.45))
startsCoords.append(float(6.78))
startsCoords.append(float(-3.21))
```

opts. SetUserStarts (startsCoords, len (startsCoords) / 3)

#### See also:

- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetUserStarts
- · OEShapeDatabaseOptions.GetUserStarts

### **SetShapeScoreScale**

void SetShapeScoreScale(float scale)

Set a scale factor for the shape component, defaults to 1.0

### **SetColorScoreScale**

void SetColorScoreScale (float scale)

Set a scale factor for the color component, defaults to 1.0

#### **GetShapeScoreScale**

float GetShapeScoreScale(float scale)

Gets the scale factor for the shape component

### **GetColorScoreScale**

float SetColorScoreScale (float scale)

Gets the scale factor for the color component

## 7.1.6 OEShapeDatabaseScore

#### class OEShapeDatabaseScore

This object is used to represent the result of a **FastROCS TK** calculation returned by the OEShapeDatabase. GetSortedScores and OEShapeDatabase. GetScores methods.

It encapsulates the following information:

- Score information:
  - OEShapeDatabaseScore.GetColorTanimoto
  - OEShapeDatabaseScore.GetShapeTanimoto
  - OEShapeDatabaseScore.GetTanimotoCombo
  - OEShapeDatabaseScore.GetColorTversky
  - OEShapeDatabaseScore.GetShapeTversky
  - OEShapeDatabaseScore.GetTverskyCombo
  - OEShapeDatabaseScore.GetColorScore
  - OEShapeDatabaseScore.GetShapeScore
  - OEShapeDatabaseScore.GetScore
- Overlay recreation:
  - OEShapeDatabaseScore.GetQuat
  - OEShapeDatabaseScore.GetRotMatrix
  - OEShapeDatabaseScore.GetTranslation
  - OEShapeDatabaseScore. Transform
- Molecule retrieval: \* OEShapeDatabaseScore.GetMolIdx \* OEShapeDatabaseScore. GetConfIdx

**Warning:** The molecular transforms returned by OEShapeDatabaseScore.GetQuat, OEShapeDatabaseScore.GetRotMatrix, and OEShapeDatabaseScore.GetTranslation assume the conformer has already been aligned by OESetCoordsToInertialFrame.

While it was definitely in-elegant to require calling OESetCoordsToInertialFrame in order to reproduce overlays, this allows OEShapeDatabase to not store 28 bytes of memory per conformer, a significant space savings, especially when conformers are stored in rotor-compressed form.

Overlays are usually only required for a small number of conformations, so re-calculating this for only the "hits" is a small price to pay for potentially saving gigabytes of memory on an already memory constrained problem.

Users should prefer to use the OEShapeDatabaseScore. Transform directly to avoid having to deal with this subtlety, it will automatically do all the transformations necessary to generate overlays.

### **Constructors**

```
OEShapeDatabaseScore (size_t molIdx, unsigned int confIdx, float shapeTani,
                     float colorTani, const float *quat,
                     unsigned int csimFunc=OEShapeSimFuncType::Default,
                     unsigned int orient=OEFastROCSOrientation::Default)
OEShapeDatabaseScore (size_t molIdx, unsigned int confIdx, float shapeTani,
                     float colorTani, const double *quat,
                     unsigned int csimFunc=OEShapeSimFuncType::Default,
                     unsigned int orient=OEFastROCSOrientation::Default)
```

Constructs a new score object with the specified data. Typically only used by the internals of **FastROCS TK** in order to populate the hitlist.

**Warning:** The constructor has changed in order to support OEFastROCSOrientation AsIs. The constant OEFastROCSOrientation\_Default, drawn from the OEFastROCSOrientation namespace, has been added to the argument list. The default is OEFastROCSOrientation Inertial and the last argument should be left blank unless it is intended to use OEFastROCSOrientation\_AsIs starts on the database being loaded, in which case unsigned int orient=OEFastROCSOrientation:: AsIs should be passed to the constructor.

Warning: The constructor has changed in order to support Tversky scoring. The constant "OEShapeSimFunc-Type::Default", drawn from the OEShapeSimFuncType namespace, has been added to the argument list. The default is "Tanimoto". "Tversky" scoring is chosen by passing  $OEShapeSimFuncType_Tversky$  and setting OEShapeDatabaseOptions. SetSimFuncto "Tversky".

### **GetColorScore**

float GetColorScore() const

Returns the "color" component of the score used for ranking molecules by FastROCS TK. See the Molecular Shape section of the ShapeTK theory documentation for a description of the calculation. This function should be used in conjunction with OEShapeDatabaseOptions. GetSimFunc in order to determine which similarity function ("Tanimoto" or "Tversky") was used to calculate the scores. This function will return 0.0 if the search was requested to be "shape only", i.e., only OEShapeDatabaseType\_Shape was specified.

### **GetColorTanimoto**

float GetColorTanimoto() const

Returns the "color" component of the Tanimoto score used for ranking molecules by FastROCS TK. See the Color Features section in the **Shape TK** theory documentation for a description of what the "color" term is. This function will return 0.0 if the search was requested to be "shape only", i.e., only OEShapeDatabaseType\_Shape was specified.

**Note:** A color tanimoto of  $0.0$  is also possible if either the query or database molecule does not contain any color atoms. Even more surprising is that this value can sometimes exceed 1.0, which appears to violate the definition of "tanimoto". This is due to the first-order-gaussian approximation used, i.e, intersection volumes are not actually

subtracted out since they have little effect on virtual screening performance and would be significantly more costly to calculate. Typically, these cases are limited to complex cage systems like cubane that have many overlapping "ring" color atoms that heavily overlap. The use of the "ring" color term can be customized by using a custom color field specified through the OEShapeDatabase constructor.

#### **GetColorTversky**

float GetColorTversky () const

Returns the "color" component of the Tversky score used for ranking molecules by FastROCS TK. See the Color Features section in the **Shape TK** theory documentation for a description of what the "color" term is. This function will return 0.0 if the search was requested to be "shape only", i.e., only OEShapeDatabaseType\_Shape was specified. If "Tversky" scoring was not set using OEShapeDatabaseOptions. SetSimFunc prior to the search this function will return with an error.

### **GetConfldx**

unsigned int GetConfIdx() const

Returns the conformer's index of the matching conformer for this particular score. This index will match the index returned by the OEConfBase.GetIdx method. This allows retrieving the conformer from the OEMCMolBase. GetConf method using the OEHasConfIdx predicate like the following:

conf = mol.GetConf(OEHasIdx(score.GetConfIdx()))

#### **GetMolldx**

size\_t GetMolIdx() const

Returns the molecule index that returned this particular "score". This index maps to the indices used by OEMol-Database to retrieve molecules assuming the OEShapeDatabase was initialized with the OEShapeDatabase. Open method. This allows FastROCS TK to rely on disk-based storage through OEMolDatabase to retrieve overlays and provide connection tables, a significant memory space savings. However, this does come at the added latency and computational expense of the OEMolDatabase. GetMolecule method.

To allow for use cases other than virtual screening where only a small number of "hits" need to be sent on for further processing. This index may map to the index returned by the OEShapeDatabase. AddMo1 method. It is up to the user to decide how to store the OEMCMolBase for later access. Previously versions of FastROCS TK used OEMCMolType\_OEDBMCMol molecules for this purpose.

#### **GetQuat**

const float \*GetOuat () const

**Warning:** It will be easier to use the OEShapeDatabaseScore. Transform method than to use figure out how to use the data from this function.

Returns a pointer to a 7-element quaternion that can be used to overlay the database conformer represented by this score with the query conformation. This 7-element quaternion contains both the rotation and translational components: the first 4 elements being the quaternion rotation; the second 3 elements are the translational component.

**Warning:** Read FastROCS transforms warning above about performing overlays with these more advanced methods.

### **GetRotMatrix**

bool GetRotMatrix (float \*rmat) const

**Warning:** It will be easier to use the OEShapeDatabaseScore. Transform method than to use figure out how to use the data from this function.

Fills in the 9-element rotation matrix rmat with the rotation component needed to overlay the database conformer represented by this score with the query conformation. Returns false if the rotation matrix is ill-defined, i.e., the conversion from the underlying quaternion failed.

**Warning:** Read FastROCS transforms warning above about performing overlays with these more advanced methods.

#### **GetScore**

float GetScore() const

Returns the sum of the "shape" and "color" scores. This function should be used in conjunction with OEShapeDatabaseOptions. GetSimFunc in order to determine which similarity function ("Tanimoto" or "Tversky") was used to calculate the scores.

#### **GetShapeScore**

float GetShapeScore() const

Returns the "shape" component of the score used for ranking molecules by FastROCS TK. See the Molecular Shape section of the **Shape TK** theory documentation for a description of the calculation. This function should be used in conjunction with  $OEShapeDatabaseOptions. GetSimFunc$  in order to determine which similarity function ("Tanimoto" or "Tversky") was used to calculate the scores.

Currently, it is not possible to request a "color only" calculation from **FastROCS TK**. Therefore, this function should always be greater than  $0.0$ . A value of  $0.0$  would be a molecule with no volume, which is impossible.

#### **GetShapeTanimoto**

```
float GetShapeTanimoto() const
```

Returns the "shape" component of the tanimoto score used for ranking molecules by FastROCS TK. See the Molecular Shape section in the **Shape TK** theory documentation for a description of how this is calculated.

Currently, it is not possible to request a "color only" calculation from FastROCS TK. Therefore, this function should always be greater than  $0.0$ . A value of  $0.0$  would be a molecule with no volume, which is impossible.

Note: It is possible, though rare, to see values slightly greater than 1.0 in the 2nd decimal place. This is due to the approximation FastROCS TK uses for performance and can be disregarded, especially since they usually only occur whenever a molecule is matched against itself.

### **GetShapeTversky**

float GetShapeTversky() const

Returns the "shape" component of the tversky score used for ranking molecules by FastROCS TK. See the Molecular Shape section in the **Shape TK** theory documentation for a description of how this is calculated. If "Tversky" scoring was not set using OEShapeDatabaseOptions. SetSimFunc prior to the search this function will return with an error.

As with the "Tanimoto" scoring option, it is not currently possible to request a "color only" calculation from Fas**tROCS TK**. Therefore, this function should always be greater than  $0 \cdot 0$ . If this is not the case an error has occurred.

**Note:** It is possible, though rare, to see values slightly greater than 1.0 in the 2nd decimal place. This is due to the approximation FastROCS TK uses for performance and can be disregarded, especially since they usually only occur whenever a molecule is matched against itself.

### **GetSimFunc**

unsigned int GetSimFunc() const

Returns a constant from the OEShapeSimFuncType namespace indicating what type of similarity function, "Tanimoto" or "Tversky", is being used for scoring.

#### **GetTanimotoCombo**

float GetTanimotoCombo() const

Returns the sum of the "color" and "shape" tanimotos.

### **GetTranslation**

bool GetTranslation (float \*trans) const

**Warning:** It will be easier to use the OEShapeDatabaseScore. Transform method than to use figure out how to use the data from this function.

Fills in the 3-element vector trans with the translation component needed to overlay the database conformer represented by this score with the query conformation. Returns false if the translation is ill-defined, i.e., something went horribly wrong.

**Warning:** Read FastROCS transforms warning above about performing overlays with these more advanced methods.

### **ExtractTransform**

bool ExtractTransform(OETrans &transform, OEChem:: OEMolBase &mol) const

Fills in the OETrans object with the translation and rotation matrix necessary to transform mol onto the query. Note that OEShapeDatabaseScore. Transform is the preferred method for visualizing overlays. This method is available for the case in which you need to know exactly what transform was performed. For example, when you want to use the same transform on another molecule.

### **GetTverskyCombo**

float GetTverskyCombo() const

Returns the sum of the "color" and "shape" Tversky scores. If "Tversky" scoring was not set using OEShapeDatabaseOptions. SetSimFunc prior to the search this function will return with an error.

### **Transform**

bool Transform (OEChem:: OEMolBase &mol) const

Overlays the conformer represented by mol with the query conformation passed as the query to OEShapeDatabase. This overlay will be the orientation that was used to calculate the scores returned by the rest of this class.

#### See also:

This is the preferred method for generating overlays with FastROCS TK. There is a more complete description of the process and its subtleties above in the *FastROCS* transforms warning.

# **7.2 OEFastROCS Constants**

# 7.2.1 OEFastROCSOrientation

The FastROCS TK search algorithm performs an optimization to maximize the overlap between the query and the database molecule. This namespace defines a set of initial orientations for the optimization that are also referred to as alternative starts. The default orientation is OEFastROCSOrientation\_Inertial, which can also be accessed via OEFastROCSOrientation\_Default. As the optimization has a limited number of iterations, it may be beneficial to use alternative starting coordinates for some molecular systems. To set an alternative initial orientation use OEShapeDatabaseOptions. SetInitialOrientation.

At present there are 7 initial orientations available:

- · OEFastROCSOrientation Inertial
- · OEFastROCSOrientation UserInertialStarts
- · OEFastROCSOrientation InertialAtHeavyAtoms
- · OEFastROCSOrientation InertialAtColorAtoms
- · OEFastROCSOrientation AsIs
- · OEFastROCSOrientation Random
- · OEFastROCSOrientation Subrocs

#### See also:

- · OEShapeDatabaseOptions. SetInitialOrientation
- · OEShapeDatabaseOptions.GetInitialOrientation
- · OEShapeDatabaseOptions. SetUserStarts
- · OEShapeDatabaseOptions.GetUserStarts
- · OEShapeDatabaseOptions. GetNumStarts
- · OEShapeDatabaseOptions.GetNumUserStarts
- · OEShapeDatabaseOptions.GetNumHeavyAtomStarts
- · OEShapeDatabaseOptions.GetNumColorAtomStarts

### **Default**

The default orientation is OEFastROCSOrientation\_Inertial.

### **Inertial**

The query and the database molecule are aligned to the inertial frame and optimizations are performed for 4 inertial orientations of the database molecule, by rotating about its 2 major moments of inertia.

### **UserInertialStarts**

The database molecule is translated to each user-defined starting position and optimizations are performed for 4 inertial starts for each translation. See OEShapeDatabaseOptions. SetInitialOrientation and OEShapeDatabaseOptions. SetUserStarts for more details on setting the starting coordinates.

**Warning:** Currently, error checking is not performed for user-defined starting coordinates that fall out of scope of the molecule's coordinate range therefore, bad starting coordinates will yield zero shape/color overlap.

#### **InertialAtHeavyAtoms**

The database molecule is translated to each heavy atom of the query molecule and optimizations are performed for 4 inertial starts for each translation. See OEShapeDatabaseOptions. SetInitialOrientation and OEShapeDatabaseOptions.GetInitialOrientation

### **InertialAtColorAtoms**

The database molecule is translated to each color atom of the query molecule and optimizations are performed for 4 inertial starts for each translation. This method works for combo and shape-only searches. The only requirement is that the query molecule has color atoms. If the query molecule does not have color atoms the search will default to OEFastROCSOrientation\_Inertial. See OEShapeDatabaseOptions. SetInitialOrientation, OEShapeDatabaseOptions.GetInitialOrientation OEShapeDatabaseOptions. and GetNumColorAtomStarts.

### **Asls**

The query and database molecules are left ASIS. It is presumed that the conformers are already positioned in space (perhaps through docking) therefore they are not centered or set to the inertial frame of reference. This method carries out a single optimization at the query and database molecule's original coordinates. No inertial orientations are optimized.

**Warning:** In order to use this method on a database the entire database is required to be reloaded with the OEShapeDatabase. Open or OEShapeDatabase. AddMol routine using unsigned int orient=OEFastROCSOrientation: : AsIs as the last argument.

**Warning:** In order to use the OEShapeDatabaseScore. Constructors with this method it is required that the final argument to the constructor be unsigned int orient=OEFastROCSOrientation:: AsIs.

OEShapeDatabaseOptions. SetInitialOrientation, **See** OEShapeDatabaseOptions. GetInitialOrientation, OEShapeDatabase. Open and OEShapeDatabaseScore. Constructors.

### **Random**

N random starts are generated by randomly orientating the database molecule N times. This method includes the ability to set the maximum random translation via the OEShapeDatabaseOptions. SetMaxRandomTranslation, The number of random starts can be set using the option. The default maximum is 2 angstroms. OEShapeDatabaseOptions. SetNumRandomStarts option. The default number of random starts is 10. The random seed can be set using the OEShapeDatabaseOptions. SetRandomSeed. The default random seed is based on the time.

Warning: The random API point is only deterministic when using the same seed if only one thread is set to open the database using OEShapeDatabase. SetNumOpenThreads between calls to GetScores or GetScores is called on the same opened database object.

See OEShapeDatabaseOptions.SetInitialOrientation OEShapeDatabaseOptions. GetInitialOrientation OEShapeDatabaseOptions.SetMaxRandomTranslation OEShapeDatabaseOptions.GetMaxRandomTranslation OEShapeDatabaseOptions. SetNumRandomStarts OEShapeDatabaseOptions.GetNumRandomStarts OEShapeDatabaseOptions.SetRandomSeed OEShapeDatabaseOptions.GetRandomSeed

### **Subrocs**

Optimizations are carried for each inertial orientation at each heavy atom of the molecule with the most heavy atoms regardless of whether it is the query or the database molecule. This method is synonymous with OEFastROCSOrientation\_InertialAtHeavyAtoms.

See OEShapeDatabaseOptions.SetInitialOrientation OEShapeDatabaseOptions. GetInitialOrientation

See the Starting positions for optimization section in the Shape TK theory documentation for a description of alternative starts.

## 7.2.2 OEFastROCSReturnCode

This namespace contains constants returned by OEFastROCSGPUStatus to indicate the status of the GPU.

See also:

· OEFastROCSGPUStatus

### **Success**

The API call returned with no errors. The GPU is ready.

#### **InitializationError**

The CUDA driver and runtime could not be initialized.

### **InsufficientDriver**

The NVIDIA CUDA driver is older than the CUDA runtime library. This is not a supported configuration. Users should install an updated NVIDIA display driver to allow the application to run.

### **NoDevice**

No CUDA-capable devices were detected by the installed CUDA driver.

### **NoDeviceDetected**

No CUDA-capable devices were detected by the installed CUDA driver.

### **NotPermitted**

The attempted operation is not permitted.

#### **Unknown**

Unknown failure.

## 7.2.3 OEShapeDatabaseType

This namespace is used to control whether a OEShapeDatabase object should store the data necessary to calculate the following components of the output score: OEShapeDatabaseScore.GetShapeTanimoto and OEShapeDatabaseScore.GetColorTanimoto. Each component has an associated memory and calculation overhead that can be avoided is desired. For example, passing OEShapeDatabaseType\_Shape to the OEShape-Database constructor will cut memory consumption roughly in half and skip calculating static color scores.

#### See also:

· OEShapeDatabaseOptions. Constructors

• OEShapeDatabaseOptions. SetScoreType

### **Color**

Instructs OEShapeDatabase to cache the necessary color information so that a subsequent search with OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores will yield color scores. It is possible to pass this value into the OEShapeDatabase constructor and then turn it off for searches so the same database can be used for shape-only and shape+color searches. To turn off the color term for only a specific search, pass OEShapeDatabaseType\_Shape into the OEShapeDatabaseOptions. SetScoreType method, then pass that options object into either OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores.

#### Combo

The combination of OEShapeDatabaseType Shape and OEShapeDatabaseType Color as a convenience using the name most often used. This is a synonym of  $OEShapeDatabaseType\_Default$ .

#### **Default**

The default setting for OEShapeDatabase is to calculate both "Color" and "Shape" scores. The combination of both scores shows very good results for virtual screening performance.

#### **Shape**

Must be specified as part of the OEShapeDatabase constructor or as a term in the OEShapeDatabaseOptions class.

**Warning:** Color-only functionality is currently not supported.

#### **Sitehopper**

Must be specified as part of the *OEShapeDatabase* constructor to run a Sitehopper calculation.

**Warning:** Sitehopper functionality requires a Sitehopper license in addition to a FastROCS license.

# 7.2.4 OEShapeSimFuncType

This namespace is used to set which similarity function, 'Tanimoto' or 'Tversky', OEShapeDatabase objects use to score search results. The default option is OEShapeSimFuncType\_Tanimoto. Tversky scoring is set using the OEShapeDatabaseOptions. SetSimFunc member function of OEShapeDatabaseOptions.

**Note:** Tanimoto and Tversky scoring options are mutually exclusive therefore, whichever function was previously selected before performing a search will be the one used to calculate the subsequent score. If no function is set the default function is used.

### See also:

- · OEShapeDatabaseOptions.GetSimFunc
- · OEShapeDatabaseOptions. SetSimFunc

### **Default**

Set OEShapeDatabaseOptions to instruct OEShapeDatabaseScore to calculate scores for search results using the tanimoto similarity function. See  $OEShapeSimFuncType$  Tanimoto for more details on usage.

### **Tanimoto**

Set OEShapeDatabaseOptions to instruct OEShapeDatabaseScore to calculate scores for search results using the tanimoto similarity function. To retrieve the "shape" tanimoto score use either OEShapeDatabaseScore.GetShapeTanimoto <sub>or</sub> OEShapeDatabaseScore.GetShapeScore. To retrieve the "color" tanimoto score use either OEShapeDatabaseScore.GetColorTanimoto or OEShapeDatabaseScore.GetColorScore. To retrieve the combined "shape" and "color" tanimoto scores use either OEShapeDatabaseScore. GetTanimotoCombo or OEShapeDatabaseScore. GetScore.

### **Tversky**

Set OEShapeDatabaseOptions to instruct OEShapeDatabaseScore to calculate scores for search results using the tversky similarity function. To retrieve the "shape" tversky score use either OEShapeDatabaseScore. Get ShapeTversky or OEShapeDatabaseScore. Get ShapeScore. To retrieve the "color" tversky score use either OEShapeDatabaseScore.GetColorTversky or OEShapeDatabaseScore.GetColorScore. To retrieve the combined "shape" and "color" tversky scores use either OEShapeDatabaseScore. GetTverskyCombo or OEShapeDatabaseScore. GetScore.

**Warning:** If using the OEShapeDatabaseScore.GetColorScore, OEShapeDatabaseScore. GetShapeScore or OEShapeDatabaseScore. GetScore methods to retrieve scores it is advised that the  $OEShapeDatabaseOptions$ .  $GetSimFunc$  method is used to determine which similarity function the scores were calculated with.

Note: See OEShapeDatabaseType for details of how to set OEShapeDatabaseOptions to store only "shape" scores or both "shape" and "color" scores.

Warning: Color-only functionality is currently not supported.

See Molecular Shape section in the **Shape TK** theory documentation for a description of the Tanimoto and Tversky similarity functions.

## **7.2.5 OEFastROCSMode**

This namespace can be used to activate "ROCS" mode, which will result in scores that are more directly comparable to ROCS. The default option is OEFastROCSMode FastROCS. ROCS mode is set using the OEShapeDatabaseOptions. SetFastROCSMode member function of OEShapeDatabaseOptions.

### See also:

- · OEShapeDatabaseOptions.GetFastROCSMode
- · OEShapeDatabaseOptions. SetFastROCSMode

#### **Default**

The default calculation mode is OEFastROCSMode\_FastROCS

### **FastROCS**

Set OEShapeDatabaseOptions to instruct OEShapeDatabaseScore to calculate scores normally.

#### **ROCS**

Set OEShapeDatabaseOptions to instruct OEShapeDatabaseScore to calculate scores for search results more similar to ROCS.

Warning: setting OEFastROCSMode\_ROCS will impact performance. Between 5-20% performance decrease should be expected.

# **7.3 OEFastROCS Functions**

## 7.3.1 OEFastROCSCacheStuff

```
bool OEFastROCSCacheStuff (OEChem:: OEMCMolBase &mol,
                           const OEShape:: OEColorForceField &cff)
```

**Warning:** This function is deprecated and has been superseded by OEP repareFastROCSMol. Please use OEPrepareFastROCSMol to optimize for OEShapeDatabase. Open load time performance.

## 7.3.2 OEFastROCSGetArch

const char \*OEFastROCSGetArch()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify the hardware architecture. The format of these strings may change over time.

## 7.3.3 OEFastROCSGetLicensee

```
std::string OEFastROCSGetLicensee()
bool OEFastROCSGetLicensee (std::string &licensee)
```

Returns the licensee name from the license file.

## 7.3.4 OEFastROCSGetNumDevices

size t OEFastROCSGetNumDevices()

Returns the number of compatible GPUs available for execution in the system being queried. If no GPUs are visible the function will throw the following warning Unable to find a suitable device.

# 7.3.5 OEFastROCSGetPlatform

const char \*OEFastROCSGetPlatform()

Returns the internal build string used by OpenEye, Cadence Molecular Sciences to identify a platform. The format of these strings may change over time, and future distributions may contain different values even when using the same operating system, compiler and processor. For example, on a  $\times 86\_64$  Red Hat Enterprise Linux box this would return  $redhat-RHEL5-<sub>q</sub>++4.1-x64.$ 

## 7.3.6 OEFastROCSGetRelease

const char \*OEFastROCSGetRelease()

Returns the release name of the FastROCS library being used. This returns a value similar to 0.10.0 for production versions of the library, and 0.10.0 debug for the checking version of the library.

## 7.3.7 OEFastROCSGetSite

```
std::string OEFastROCSGetSite()
bool OEFastROCSGetSite(std::string &site)
```

Returns the physical site location of the licensee as registered in the license file.

## 7.3.8 OEFastROCSGetVersion

unsigned int OEFastROCSGetVersion()

Returns the version number of the library being used. This is an unsigned integer value indicating the date on which the library was built, for example  $20141001$ , for the 1st of October 2014. This value should be used when reporting problems, and unlike the release string, may be used in comparisons if needed.

## 7.3.9 OEFastROCSGPUStatus

unsigned OEFastROCSGPUStatus()

Queries the status of the GPU and returns an OEFastROCSReturnCode. Useful for checking whether the machine has an accelerator properly setup and ready to accept FastROCS queries. It is guaranteed that if this function returns OEFastROCSReturnCode\_Success that all subsequent OEShapeDatabase objects can successfully execute queries.

# 7.3.10 OEFastROCSIsGPUReady

bool OEFastROCSIsGPUReady()

Returns True if OEShapeDatabase can successfully execute queries. Useful for checking whether the machine has an accelerator properly setup and ready to accept FastROCS queries. It is guaranteed that if this function returns 'True' that all subsequent OEShapeDatabase object can successfully execute queries. That means that this function will effectively initialize an underlying context that is re-used by OEShapeDatabase objects, possibly grabbing an "exclusive process" lock: http://docs.nvidia.com/cuda/cuda-c-programming-guide/#compute-modes

## 7.3.11 OEFastROCSIsLicensed

```
bool OEFastROCSIsLicensed (const char *feature=0,
                           unsigned int *expdate=0)
```

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any **FastROCS TK** functionality.

The 'feature' argument can be used to check for a valid license to **FastROCS TK** along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current **FastROCS TK** license.

See also:

· OEChemIsLicensed function

## 7.3.12 OEShapeDatabasePrep

```
bool OEShapeDatabasePrep(string filein, string fileout,
                         unsigned int cfftype = OEShape:: OEColorFFType:: OEDefault) )
```

Prepares molecules stored in a OEFormat OEB file to improve the performance of loading the molecules into an OEShapeDatabase object. This is a multi-threaded implementation of the shapedatabaseprep example that takes the input OEB filename as the first argument and the output OEB filename as the second argument. An optional argument to specify the color force field type can be passed in. The default color force field is Implicit Mills Dean.

Using this function to prep a database will result in as much as 10-fold performance improvement of  $OEShapeDatabase$ . Open. OEShapeDatabasePrep does the following:

- Pre-compresses the output file with OEPRECompress, alleviating the need to Gzip the OEB and improving the performance of OEMolDatabase.Open.
- Sets the energy of each conformer to  $0.0$  to avoid writing it to  $OEB$ .
- Suppresses hydrogens and reorders reference conformers for compression.
- Pre-calculates color atoms.
- Pre-calculates self-color and self-shape terms for all conformers.

```
Note:
                                                                 self
                                                                                   for
                                                                                        the
            OEShapeDatabasePrep will cache
                                                color
                                                      atoms
                                                             and
                                                                      color terms
OEColorFFType ImplicitMillsDean color force field.
```

**Warning:** This function is non-deterministic so molecules will not appear in the same order as the input file.

Warning: This function should not be used to prepare a database intended to be used with a OEShapeDatabaseType\_Sitehopper database

## 7.3.13 OEIsDatabasePrepared

**bool** OEIsDatabasePrepared(OEChem::OEMolDatabase moldb)

bool OEIsDatabasePrepared(OEChem:: OEMolBase mol)

Returns True if the database (OEMolDatabase) or molecule (OEMolBase) input has already been prepared with the OEPrepareFastROCSMol function and False if preparation is still required.

It is recommended that all sizable databases that are intended to be re-used undergo preparation in order to benefit from significantly faster load times.

## 7.3.14 OEPrepareFastROCSMol

```
bool OEPrepareFastROCSMol(OEChem::OEMCMolBase &mol)
bool OEPrepareFastROCSMol(OEChem::OEMCMolBase &mol,
                          const OEShape:: OEColorForceField &cff)
```

Prepares the molecule mol to improve the performance of loading the molecule into memory as an OEShape-Database object from an OEFormat\_OEB file. The following steps are taken to improve the performance of OEShapeDatabase. Open by as much as 10-fold:

- Sets the energy of each conformer to 0.0 to avoid writing it to OEB.
- Suppresses hydrogens and reorders reference conformers for compression.
- Pre-calculates color atoms.
- Pre-calculates self-color and self-shape terms for all conformers.

It is recommended to call OEPRECompress on the oemolostream before writing out to OEB. This will store conformers in "PRE-compressed" form therefore alleviating the need to Gzip the OEB file and consequently improving the performance of OEMolDatabase. Open. In general, calling OEPrepareFastROCSMol and OEPRECompress will result in a smaller OEB file than the default OEB. GZ output from OMEGA.

Additionally, if OEB file size is of chief concern a further reduction in file size can be achieved by using an OEMCMolType HalfFloatCartesian molecule, which stores reference coordinates and torsions in half floating point precision (16-bit). The following code snippet demonstrates how to cast the resultant molecule from OEP repareFastROCSMol to use half precision:

```
OEPrepareFastROCSMol(mol);
OEMol halfMol(mol, OEMCMolType::HalfFloatCartesian);
OEWriteMolecule(ofs, halfMol);
```

```
OEPrepareFastROCSMol(mol)
halfMol = OEMol(mol, OEMCMolType_HalfFloatCartesian)
OEWriteMolecule(ofs, halfMol)
```

16-bit floating point will give a file size saving of approximately 12% with a tradeoff of about 7% more performance when loading the OEB from disk into memory.

Note: By default, OEPrepareFastROCSMol will cache color atoms and self color terms for the OEColorFFType ImplicitMillsDean color force field. The second overload that takes a OEColorForceField can be used to override this default.

## 7.3.15 OESetCoordsToInertialFrame

bool OESetCoordsToInertialFrame(OEChem::OEMolBase  $\&mod)$ 

Set the coordinates of mol to be aligned by its principle moments of inertia. The transformations returned by OEShapeDatabaseScore.GetQuat, OEShapeDatabaseScore.GetRotMatrix, and OEShapeDatabaseScore. GetTranslation assume the molecule has already been aligned by its principle moment of inertia. Users should prefer to use the OEShapeDatabaseScore. Transform directly to avoid having to deal with this subtlety.

See also:

OEShapeDatabaseScore

# 7.4 Using a Custom Color ForceField in FastROCS

Similar to the **Shape Toolkit**, a custom color forcefield can be used to compare color features beyond those captured with the default forcefield. To use a custom color forcefield, specify your forcefield during the initialization of your OEShapeDatabase OEShapeDatabase

Custom color forcefields in FastROCS are constructed the same way they are in the OEColorForceField class in the **OEShape TK** but are restricted to the following:

- 1. Interactions can only be between atoms of the same type
- 2. Interactions can only be favorable
- 3. Interactions can only be of type "gaussian"
- 4. user defined types are not permitted

in the following code example:

```
cff = oeshape.OEColorForceField()
cff. Init (oeshape. OEColorFFType_ImplicitMillsDeanNoRings)
cff.ClearInteractions()
cff.AddInteraction(
    cff.GetType("donor"), cff.GetType("donor"), "gaussian", -1.0, range
cff.AddInteraction(
    cff.GetType("acceptor"), cff.GetType("acceptor"), "gaussian", -1.0, range
\lambdadbase = oefastrocs. OEShapeDatabase (cff)
```

a color forcefield is created that will only count interactions between pairs of acceptors and pairs of donors. The -1.0 indicates a favorable interaction, with standard weighting. 2.0 is the range of the color interaction in space.

See also:

• OEColorForceField class in the OEShape TK

# 7.5 OEFastROCS ShapeDatabaseServer XMLRPC API

This chapter documents the XMLRPC API that is exposed by the ShapeDatabaseServer.py server since the 1.0 release of **FastROCS**. Since that release many users have created internal clients to the server that depend on that XMLRPC API, so OpenEye has strived to keep this API stable for pre-existing client code. This chapter should serve as a guide for anyone looking to create a new FastROCS server around the toolkit API.

Most users can just use the ShapeDatabaseClient. py script directly, without the need to worry about the details of the protocol between the client and server.

Note: The XMLRPC API will be replaced by a RESTful API in a future version of **FastROCS TK**.

## 7.5.1 GetBestOverlays

GetBestOverlays(querymolstr, nhits, iformat=".oeb", oformat=".oeb") -> Binary

Return the nhits results of the database search performed with the query querymolstr. The file format of the data in the XML RPC Binary querymolstr is specified by the iformat argument. Valid iformat arguments are any **OEChem** supported molecular file format that OEIs3DFormat will return True for. This is because FastROCS TK requires a 3D conformation to search against.

The returned XML RPC Binary will contain the best nhits of query against the database. The returned XML RPC Binary will contain the molecule sorted by the chosen scoring function for the database. nhits of 0 specifies that all database molecules should be returned in sorted order, not a very advisable operation as that could move many megabytes to gigabytes of data over the network.

The file format of the returned XML RPC Binary is specified by the oformat argument. This can be any OEChem supported file format that OEIsWriteable will return True for. However, scores are only stored as SD data, so only the following file formats will return score information:

- · OEFormat OEB
- · OEFormat SDF
- · OEFormat CSV

Furthermore, the molecules returned will be aligned to the query molecule in 3D. So only formats that can represent 3D information will actually contain the resulting alignment.

#### See also:

The File Formats section of the **OEChem** documentation for a list of valid file formats.

Note: iformat and oformat default to . oeb in order to be compatible with versions of FastROCS clients prior to 1.4.0.

Warning: This XML RPC request will block until the search has completed. Since searches can take many seconds to minutes, the underlying network connection for the XML RPC request may time out. This remote procedure call should only be used when the search is known to be short. Using the SubmitQuery remote procedure call to queue up the query is highly preferred for creating a better user experience.

## 7.5.2 GetName

GetName()  $->\,$ str

Return the name of the database being served from the server. By default, this is the filename the server was started with. However, this can be changed by the SetName remote procedure call.

## **7.5.3 GetVersion**

```
GetVersion() \rightarrow str
```

Return the version of **FastROCS TK** being run on the server.

## 7.5.4 IsLoaded

IsLoaded(blocking=False) -> bool

Returns True if the server has finished loading the database into memory and ready to accept queries. Returns False if the server is still initializing, causing any queries submitted to wait in a queue before they can be processed.

## 7.5.5 OEThrowSetLevel

OEThrowSetLevel(level)

Turns on debugging information for the server, or turning it back off again. The integer level should be drawn from the OEErrorLevel namespace. FastROCS TK uses OEThrow to handle all logging information. FastROCS TK will throw lots of performance debugging information to the OEErrorLevel Debug level that will not be seen by default. When contacting OpenEye support about FastROCS (support@eyesopen.com), including this information would be very beneficial to helping solve the problem.

## 7.5.6 QueryHistogram

QueryHistogram(queryidx) -> [int, ..., int]

Return the current distribution of scores for the search specified by the queryidx. The distribution is returned as a list of integers. The distribution of scores can be retrieved in 'real-time' during a search as well, though it is recommended to still use QueryStatus with the blocking parameter set to True to avoid spurious requests and load on the server.

The distribution is only guaranteed to be a complete distribution of all the scores once the query has fully completed executing. A query is fully complete when the integers returned by QueryStatus are equal and both non-zero.

## **7.5.7 QuervStatus**

 $\rightarrow$  (int, int) QueryStatus (queryidx, blocking=False)

Return the current progress of the search specified by the queryidx. The progress is returned as a pair of integers. The first integer in the pair is how many conformers have already been searched. The second integer in the pair is how many conformers there are total in the database to be searched. When the two integers are equal, the search has finished, and a call to  $QueryResults$  will return immediately with the resulting hits.

queryidx must be an integer that was previously returned by the  $SubmitQuery$  remote procedure call. This remote procedure call can be called any number of times with the same queryidx between the matching  $SubmitQuery$  remote procedure call and the finishing  $QueryResults$  remote procedure call.

The blocking parameter specifies whether this remote procedure call should return immediately. If blocking is False, the remote procedure call will return immediately with the current status. However, this returned value could be identical to a previous call and provide no new information to the end user. If blocking is True, this remote procedure call will not return until there is new information to return. This will result in less "busy waiting" network traffic constantly pinging the server for an update.

**Note:** It is possible for both values returned to be 0 even though the search is not complete. There is a very short period of time that the XML RPC service does not know the total number of conformers yet after the query has been submitted. Users can disregard this state and requery the server for a new status.

## **7.5.8 QueryResults**

QueryResults(queryidx) -> Binary

Return a XML RPC Binary of search results for the specified queryidx. The contents of the XML RPC Binary, including file format and size, are controlled by the corresponding call to  $SubmitQuery$ .

This remote procedure call will block if the search is not completed yet. Use the QueryStatus remote procedure call to determine if the results are ready to return.

Warning: This function can only be called once for a particular queryidx. Once a query's results are retrieved with this remote procedure call, all record of the search are removed from the server's memory. The reverse is true as well though, if this function is not called, the query's results will stay resident in memory until the server is restarted.

## 7.5.9 SetName

SetName (name)

Specify the name of the database this server is serving. Subsequent calls to the Get Name remote procedure call will return this name.

## 7.5.10 SubmitQuerv

```
SubmitQuery(querymolstr, nhits, iformat=".oeb", oformat=".oeb", shapeOnly=False) ->.
\rightarrowint
```

Submit a query 3D molecule to the server and begin processing immediately. If there is already a search in progress, the query will be submitted to a queue. An integer index is returned to allow tracking the progress of the search through the QueryStatus function, and then to retrieve the results through the QueryResults function. This function will return immediately, unlike the  $GetBestOverlays$  remote procedure call.

The shape Only argument specifies that color scoring should not be performed and taken into account when scoring and sorting molecules. This defaults to False to be compatible with versions of **FastROCS** prior to 1.5.0.

The file format of the query in the XML RPC Binary querymolstr is specified by the iformat argument. Valid iformat arguments are any OEChem supported molecular file format that OEIs3DFormat will return True for. This is because FastROCS TK requires a 3D conformation to search against. In addition to supporting 3D conformations from standard **OEChem** file formats, shape queries from  $\cdot$  sq files are also supported as queries. sq files are most easily constructed from within the vROCS GUI. They are usable from the **Shape TK** through the OEShapeQueryPublic APIs.

The nhits argument specifies how many hits should be returned by the corresponding  $QueryResults$  remote procedure call. These hits will be returned in the order of the best score first. A value of 0 given to nhits specifies that all database molecules should be returned, not a very advisable operation as that can potentially push many megabytes to gigabytes of data over the network.

The file format of the XML RPC Binary to return from  $QueryResults$  is specified by the oformat argument. This can be any OEChem supported file format that OEIsWriteable will return True for. However, scores are only stored as SD data, so only the following file formats will return score information:

- · OEFormat\_OEB
- · OEFormat\_SDF
- · OEFormat\_CSV

Furthermore, the molecules returned will be aligned to the query molecule in 3D. So only formats that can represent 3D information will actually contain the resulting alignment.

#### See also:

The File Formats section of the **OEChem** documentation for a list of valid file formats.

Note: iformat and oformat default to .oeb in order to be compatible with versions of FastROCS clients prior to 1.4.0.

# **EIGHT**

# **RELEASE HISTORY**

# 8.1 FastROCS TK 2.2.7

## 8.1.1 New features

- New methods have been added to the OEShapeDatabaseOptions class that allow the shape and color scales to be modified.
  - SetShapeScoreScale
  - GetShapeScoreScale
  - SetColorScoreScale
  - $-$  GetColorScoreScale

# **8.2 FastROCS TK 2.2.6**

Minor internal improvements have been made.

# **8.3 FastROCS TK 2.2.5**

Minor internal improvements have been made.

# **8.4 FastROCS TK 2.2.4**

Minor internal improvements have been made.

# **8.5 FastROCS TK 2.2.3**

## 8.5.1 Major bug fixes

• A memory leak which could cause a crash when calling OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores has bee fixed.

# **8.6 FastROCS TK 2.2.2**

• Minor internal improvements have been made.

# **8.7 FastROCS TK 2.2.1**

• Minor internal improvements have been made.

# **8.8 FastROCS TK 2.2.0**

July 2021

## 8.8.1 New features

• A new method, OEShapeDatabaseScore. ExtractTransform, that extracts an entire transform (not just the post inertial frame transformation) has been added.

## 8.8.2 Minor bug fixes

• An issue with custom weights in FastROCS *custom color* has been fixed.

# 8.9 FastROCS TK 2.1.0

**Fall 2020** 

## 8.9.1 New features

- FastROCS TK now requires a minimum NVIDIA Driver version of 450.x. See NVIDIA Drivers for more details.
- FastROCS TK now requires a minimum GPU compute capability of 3.5. See Supported GPUs for more details.
- OEShapeQuery objects now have limited support for use as queries with the OEShapeDatabase. GetScores and OEShapeDatabase. GetSortedScores database searching methods.
- Support has been dropped for database files that are gzipped (e.g.  $\circ$ eb. qz in the **FastROCS TK** examples). .oeb and .oez are still supported.

• A new database type,  $OEShapeDatabaseType$  Sitehopper, has been added that runs Sitehopper calculations using fastrocs. Note that a Sitehopper license is required to run a Sitehopper calculation. Please visit https://www.eyesopen.com/contact or your account manager for a license.

# 8.9.2 Major bug fixes

• Previously, GPU memory limits were being reached for routine searches when using OEFastROCSOrientation\_InertialAtHeavyAtoms with OEShapeDatabaseOptions. Set ColorOptimization set to true, causing the color calculation to default to the CPU. The improved alternative starts algorithm handles any number of starts without reaching GPU memory limits.

**Warning:** Performance will be affected by using large numbers  $(>10)$  of alternative starts.

• Previously, the section example fastrocs shapeclustering example suffered some performance degradation. This has now been fixed thanks to a performance bug fix in OESelfShape. The script should now perform at its normal speed,  $\sim 10x$  that of the previous release.

# 8.9.3 Minor bug fixes

• A warning is now thrown if users attempt to use a custom color forcefield that has either a non-Gaussian functional form or interactions between different color types.

## 8.9.4 Python specific changes

- · SimplePythonScript.py has been renamed SimpleFastROCSSearch.py in Tutorial 1: Inertial At Heavy Atoms Alternative Starts.
- OEPreserveRotCompress has been added to the molecule input stream in the SimplePrepScript.py script used in Tutorial 2: How to prepare a database for faster load speeds.

## 8.9.5 Java specific changes

- · SimpleJavaScript.java has been renamed SimpleFastROCSSearch.java in Tutorial 1: Inertial At Heavy Atoms Alternative Starts.
- . OEPreserveRotCompress has been added to the molecule input stream in the SimplePrepScript. java script used in Tutorial 2: How to prepare a database for faster load speeds.

# 8.9.6 C++ specific changes

- · simplecppscript.cpp has been renamed simplefastrocssearch.cpp in Tutorial 1: Inertial At Heavy Atoms Alternative Starts.
- OEPreserveRotCompress has been added to the molecule input stream in the simpleprepscript. cpp script used in Tutorial 2: How to prepare a database for faster load speeds.

### **8.9.7 Documentation changes**

• Tutorial 2: How to prepare a database for faster load speeds now has an additional step explaining OEPreserveRotCompress.

# 8.10 FastROCS TK 2.0.0

### 8.10.1 New features

- Two new options have been added to the OEShapeDatabase class:
  - OEShapeDatabaseOptions. SetColorOptimization is used for optimization over color overlap in addition to shape overlap during a FastROCS overlay calculation.
  - OEShapeDatabaseOptions. SetFastROCSMode is used to change several of the options in the OEShapeDatabase class to match what they would be in **ROCS** for a closer (though not identical) comparison to ROCS.

### 8.10.2 Minor bug fixes

• A warning regarding Tversky scores greater than 1.0 will now only be thrown if running with the Tversky scoring function.

### 8.10.3 General Notices

• The C++ FastROCS TK is not available on RHEL8 or Ubuntu18 in this release.

# 8.11 FastROCS TK 1.10.1

## 8.11.1 New features

• A new function, OEFastROCSGPUStatus, has been added that interrogates the status of the GPU and returns a code from the OEFastROCSReturnCode namespace. The return codes now allow for more specific error reporting of the GPU system.

## 8.11.2 Major bug fixes

- An issue that caused OEFastROCSOrientation\_Subrocs to fail to apply the correct number of starts to the color calculation has been fixed.
- OEShapeDatabase. SetColorGridSpacing had been broken after the previous major version change. This has been fixed.
- OEShapeDatabaseOptions. SetLimit now returns all N overlays of all conformers and orientations when used in conjunction with OEShapeDatabaseOptions. SetMaxOverlays set to 0 and OEShapeDatabaseOptions. SetMaxConfs set to 0.
- The default is now to run reference Tversky when running  $OEShapeSimFuncType_Tversky$ . For more details about Tversky similarity scoring, see the Molecular Shape section of the **Shape TK** theory documentation.

## 8.11.3 Minor bug fixes

- · OEShapeDatabaseOptions. SetNumInertialStarts is no longer order-dependent when using alternative starts.
- When running with Tversky similarity scoring, only a single warning about Tversky scores being greater than 1.0 will ever be thrown unless the debug error level is being used.

# 8.12 FastROCS TK 1.10.0

## 8.12.1 New features

• FastROCS TK has been optimized to yield a further ~2-3x in performance compared to the previous release. The performance improvement will vary from system to system. See more details in the OEToolkits 2019.Apr section.

## 8.12.2 Minor bug fixes

• GPUs in prohibited mode will now be honored when querying the number of available devices on the system. Previously, a fatal error occurred during the search.

## 8.12.3 Python-specific changes

• The example in the section\_example\_fastrocs\_shapedatabaseprep section now defaults to a maximum of 10 conformers per molecule and saves the coordinates in half-float precision. A flag is provided to switch to fullfloat precision coordinates.

## 8.12.4 Documentation changes

• A new GPU Prerequisites section has been added to the installation guide.

# 8.13 FastROCS TK 1.9.0

## 8.13.1 General notices

• FastROCS TK no longer supports Nvidia Tesla, GEForce, and Quadro cards with a compute capability of less than 3.0. This includes all GPUs with Fermi architecture (e.g., Tesla C2050 and GEForce GTX 430). If you are running one of these older GPUs and cannot upgrade your hardware, do not update to this version of FastROCS TK.

## 8.13.2 New features

• FastROCS TK is now supported for Java and C++. See the new documentation pages for Java and C++ for examples of toolkit usage and syntax.

**Note:** Java and C++ FastROCS TK API points are currently intended to be used only for toolkit functionality and not client-server functionality. The Python API should be used if client-server utilities are needed.

• A new  $OEShapeDatabasePrep$  function has been added to provide the same functionality as the shapedatabaseprep example, except as a multi-threaded function. This should improve performance when prepping databases on systems with multiple cores. This function is non-deterministic, so molecules will not appear in the same order as the input file.

## 8.13.3 Major bug fixes

- A memory leak that was only detectable when running large numbers of queries in succession against the same database without breaking context has been fixed.
- The OEShapeDatabase. AddMol method was previously missing the ability to load molecules for OEFastROCSOrientation\_AsIs alternative starting points. OEShapeDatabase.AddMol now takes the OEFastROCSOrientation constant as an additional argument. The default is OEFastROCSOrientation Inertial.

## 8.13.4 Documentation changes

- The examples section of the documentation has been reorganized by type: Simple Examples, Alternative Starts, and Client-Server. All are viewable from the FastROCS Example Suite, which includes brief descriptions as well as links to the specific example pages. The example pages now provide more in-depth descriptions of usage and download links to the example code.
- New examples have been added to the *Alternative Starts* section to demonstrate using **FastROCS TK** with alternative starts.
- Documentation for both the Java and C++ versions of **FastROCS TK** has been added.

# 8.14 FastROCS TK 1.8.4

## 8.14.1 New features

• A new Python example script, BestShapeOverlayMultiConfQuery.py, has been added to perform a query search for every conformer of the query molecule and save the sorted results sequentially in a single file for each query molecule.

## 8.14.2 Minor bug fixes

• A small modification has been made to ShapeDatabaseServer.py to reduce the number of server-related messages when running a query search via the client/proxy interface.

# 8.15 FastROCS TK 1.8.3

### 8.15.1 New features

- Alternative starting points in **FastROCS TK** have been extended to include two additional API points: OEFastROCSOrientation\_Random and OEFastROCSOrientation\_Subrocs.
  - OEFastROCSOrientation\_Random now randomly orients the database molecule N times. By default, N is set to 10 with a maximum allowed translation of 2 angstroms. Random alternative starts can be customized using the OEShapeDatabaseOptions. SetMaxRandomTranslation, OEShapeDatabaseOptions.SetNumRandomStarts, and OEShapeDatabaseOptions. Set RandomSeed methods. The default random seed is time-dependent.
  - OEFastROCSOrientation\_Subrocs now performs optimizations at every heavy atom of the molecule with the most heavy atoms, regardless of which molecule is the query and which is the database molecule. At each translation, 4 inertial poses are optimized, resulting in a total of [4 \* number of heavy atoms of the heaviest molecule] optimizations.

See OEFastROCSOrientation and OEShapeDatabaseOptions. SetInitialOrientation for more information.

- The following example scripts have been reworked to enable access to additional features of FastROCS TK:
  - ShapeDatabaseServer.py
  - ShapeDatabaseClient.py
  - ShapeDatabaseClientHistogram.py
  - ShapeDatabaseProxy.py

Tversky sampling, shape-only searches, and basic alternative starting points can be accessed via the client without having to rerun or modify the server/proxy scripts. Users can submit a query as usual from the client adding the relevant flags. The new flags are:

- --tversky
- --shapeOnly
- --alternativeStarts [inertialAtHeavyAtoms|inertialAtColorAtoms|subrocs|random  $\lceil N \rceil$

Warning: These scripts are not backwards compatible. The behavior of running server/proxy/client scripts with mismatched versions is undefined. In order to use the new client flags, ensure that the server and proxy scripts are also updated to this version.

• Warnings that are thrown for Tversky and Tanimoto scores greater than 1.0 have been simplified. Messages showing the actual Tversky/Tanimoto calculation are now Debug-level messages.

## 8.15.2 Minor bug fixes

- OEDBTracer. Get Total now correctly accumulates the total when using the same OEDBTracer object for multiple queries.
- OEShapeDatabaseOptions. SetLimit now correctly handles the scenario where the limit is greater than the maximum scores available. If the limit is greater than the possible number of scores able to be returned, a warning will be thrown and the limit will fall back to: number of conformers  $\star$ OEShapeDatabaseOptions.GetMaxOverlays.

## 8.15.3 Python-specific changes

• The example script karma, py in *FastROCS TK examples* has been renamed to the more descriptive SphereExclusionClustering.py.

## 8.15.4 Documentation changes

• A new tutorial, *Tutorial 2*, has been created for preparing a database to take advantage of faster OEShapeDatabase. Open times.

# 8.16 FastROCS TK 1.8.2

## 8.16.1 New features

- **TK** have been • Alternative starting points in FastROCS extended to now include OEFastROCSOrientation\_AsIs and OEFastROCSOrientation\_InertialAtColorAtoms.
  - OEFastROCSOrientation AsIs presumes that the query and the database molecules are already correctly aligned in space (perhaps through docking), so a single optimization per query-database molecule pair is carried out.
  - OEFastROCSOrientation\_InertialAtColorAtoms translates each database molecule to each color atom of the query molecule and optimizes for 4 inertial poses at each translation. This method can be used with both shape-only searches and combo searches. The only requirement is that the query molecule must have color atoms; otherwise, the search will throw a warning and default to inertial starts.

See OEFastROCSOrientation and OEShapeDatabaseOptions. SetInitialOrientation for more information.

- The following new getter methods have been added to OEShapeDatabaseOptions for retrieving the number of starts for the relevant method:
  - OEShapeDatabaseOptions.GetNumUserStarts
  - OEShapeDatabaseOptions.GetNumColorAtomStarts
  - OEShapeDatabaseOptions.GetNumHeavyAtomStarts
  - OEShapeDatabaseOptions.GetNumStarts

OEShapeDatabaseOptions. GetNumStarts has also been overloaded for each alternative start option.

• A new argument has been added to  $OEShapeDatabase$ . Open to ensure that conformers are correctly handled when using OEFastROCSOrientation AsIs.

When using the new OEFastROCSOrientation AsIs feature, the shape database must be opened with the additional argument set to OEFastROCSOrientation\_AsIs.

There is no need to alter existing scripts if the OEFastROCSOrientation\_AsIs alternative starts feature is not being used since the default argument results in the correct execution path for all other use cases.

See OEShapeDatabase. Open and OEFastROCSOrientation AsIs for more information.

• A new argument has been added to OEShapeDatabaseScore. Constructors to correctly transform conformers to their resultant position when using OEFastROCSOrientation AsIs.

Generally, the constructor is not used in most scripts as the OEShapeDatabaseScore object is constructed internally when calling OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores. Therefore, most users will not be affected by this change.

If the OEShapeDatabaseScore constructor is used and OEFastROCSOrientation\_AsIs is set, the constructor can be modified with the additional argument set to OEFastROCSOrientation\_AsIs.

The default value for the additional argument satisfies all other use cases, so no action is required.

See OEShapeDatabaseScore. Constructors for more information.

## 8.16.2 Major bug fixes

GPU memory limits were being reached for routine searches • Previously, when using OEFastROCSOrientation\_InertialAtHeavyAtoms, causing searches  $\overline{f}$ default  $\overline{f}$ OEFastROCSOrientation Inertial. The improved alternative starts algorithm handles any number of starts without reaching GPU memory limits.

Warning: Performance will be affected by using large numbers of alternative starts.

- . OEShapeDatabaseOptions. SetMaxOverlays now sets the number of overlay results to return per conformer. Previously, this was broken and was restricting the number of overlays to 1 per conformer regardless of its setting. OEShapeDatabaseOptions. SetMaxOverlays is now fixed and works correctly with OEShapeDatabaseOptions. SetMaxConfs, OEShapeDatabaseOptions. SetNumInertialStarts and alternative starts for both OEShapeDatabase.GetScores and OEShapeDatabase.GetSortedScores.
- Tversky calculations no longer overestimate the score of caged systems or conformer pairs where one conformer is much larger than the other.

## 8.16.3 Minor bug fixes

. A warning is now thrown if OEFastROCSOrientation\_UserInertialStarts is set with OEShapeDatabaseOptions.SetInitialOrientation and OEShapeDatabase.GetScores or if OEShapeDatabase.GetSortedScores is called before OEShapeDatabaseOptions. SetUserStarts.

## 8.16.4 Documentation changes

• A tutorials page has been created that walks through features of FastROCS TK and gives detailed examples. The first tutorial gives step-by-step instructions on how to use alternative starts.

If you have a specific feature that you would like in a tutorial, please contact support at support@eyesopen.com with the subject header FastROCS TK Tutorial Request.

# 8.17 FastROCS TK 1.8.1

### 8.17.1 New features

• This release extends the capabilities of FastROCS TK to allow for 2 types of alternative starting points: userdefined starts and starts at heavy atoms.

The FastROCS TK algorithm involves optimizing each overlaid query and database molecule by shape. Previously, the optimization had been performed for 4 orientations of each database molecule around its principle axes of inertia.

User-defined starts allow users to input starting coordinates directly. The database molecule is now translated to each starting position and the 4 inertial poses are optimized.

Starts at heavy atoms translate each database molecule to each heavy atom plus the center of mass of the query molecule. Again, the 4 inertial poses are optimized at each translation.

For more information. see OEShapeDatabaseOptions.SetInitialOrientation and OEFast ROCSOrient at ion.

- A new function, OEFastROCSGetNumDevices, has been added that returns the number of GPUs currently visible. Since no **FastROCS TK** objects are required, it can be used to probe a system prior to running any queries.
- A new function, OEIsDatabasePrepared, has been added to check whether a database file has already been run through OEP repareFastROCSMol. This is useful for ensuring that a database file has been prepared and also saves time by preventing it from being prepared twice. OpenEye recommends preparing all large databases in order to benefit from significantly faster OEShapeDatabase. Open times.
- The cutoffs in **FastROCS TK** now support the retrieval of all scores less than or equal to the desired cutoff. See OEShapeDatabaseOptions.SetCutoffLT.

## 8.17.2 Major bug fixes

• Customers using Tesla C2050 cards and GTX cards at compute capability 2.x may have experienced some issues with large databases of very small molecules since compute resources were being over-allocated in some scenarios. This issue has been resolved.

## 8.17.3 Minor bug fixes

- Warnings had previously been thrown for Tversky scores greater than 1.0 (shape/color). For performance reasons, components of the Tversky/Tanimoto scores can be calculated on either the GPU or CPU. This sometimes results in scores slightly greater than 1.0. Customers should be aware of this possibility when handling scores. A warning is now thrown if a score is greater than 1.2.
- When opening an OEShapeDatabase object, the presence of invalid molecules now results in a warning rather than error.
- karma, py can now handle databases with molecules that don't have titles. A unique title is given to each untitled molecule.

# 8.18 FastROCS TK 1.8.0

### 8.18.1 New features

- FastROCS TK has been switched from an OpenCL backend to a CUDA backend. This should have no impact on FastROCS usage but may reduce the complexity of the installation process. The installation of CUDA development tools is not required to use FastROCS TK.
- NVIDIA driver support has been added for driver versions  $367 \cdot \star$ . Support has been dropped for  $340 \cdot \star$ . A list of currently supported NVIDIA drivers for **FastROCS TK** can be found in the *Installation* section.

## 8.18.2 Minor bug fixes

- The method OEShapeDatabase. Open has been modified to give a warning rather than an error when a file contains some molecules with heavy atoms and some molecules without heavy atoms. This is to prevent an entire database upload from failing if only a handful of molecules are corrupt.
- ShapeSimilarityMatrix.py has been renamed ShapeDistanceMatrix.py and the resultant matrix has been fixed to accurately reflect distance on the diagonal (i.e., 0.0).

## 8.18.3 Python-specific changes

• The Python integration tests now check for the presence of a GPU and skip the **FastROCS** test if a GPU is not available. Previously, the integration tests would fail.

# 8.19 FastROCS TK 1.7.0

## 8.19.1 New features

- OEShapeDatabase now consumes approximately 50% less main memory. This improvement was gained by compressing color information in a more concise way. There should be negligible difference in color Tanimoto scores (only seen in the 4th decimal place).
- Tversky similarity scoring is now available in **FastROCS TK** in addition to the default Tanimoto scoring. The following APIs have been added to support this new scoring:
  - OEShapeDatabaseOptions. SetSimFunc and OEShapeDatabaseOptions. GetSimFunc methods have been added to set and retrieve the scoring type.

- OEShapeDatabaseOptions. SetTverskyCoeffs method has been included to allow custom tuning of the alpha and beta coefficients. OEShapeDatabaseOptions. GetTverskyAlpha and OEShapeDatabaseOptions. GetTverskyBeta methods have been added to retrieve the coefficients.
- OEShapeDatabaseScore.GetColorTversky, OEShapeDatabaseScore. GetShapeTversky, OEShapeDatabaseScore.GetTverskyCombo, OEShapeDatabaseScore.GetColorScore, OEShapeDatabaseScore.GetShapeScore, and OEShapeDatabaseScore. GetScore methods have been provided for retrieving Tversky scores.

For more details about Tversky similarity scoring, see the Molecular Shape section of the Shape TK theory documentation.

- OEFastROCSIsGPUReady function has been added to easily determine if the GPU is ready to accept Fas**tROCS TK** queries. It returns t rue if *OEShapeDatabase* can successfully execute queries on a supported accelerator device, and otherwise returns false. This function checks for the presence and status of GPU devices on the system, throwing an error message if the GPU is not ready for use. This function allows for any potential GPU issues to be caught prior to loading large databases.
- OEShapeDatabase. PrintMemoryUsage has been added to write out simple statistics about how much memory a particular OEShapeDatabase object is using and for what kinds of data.
- Driver support has been extended to include driver  $361 \cdot \star$ . A list of currently supported NVIDIA drivers for **FastROCS TK** can be found in the *Installation* section.

## 8.19.2 Major bug fixes

· OEShapeDatabase. GetScores and OEShapeDatabase. GetSortedScores will no longer add color atoms to queries passed as OEConfBase objects. Previously, the following code would yield nondeterministic color scores and bugs:

```
for conf in mol. GetConfs():
    for score in shapedb. GetScores (conf):
         \ddotsc
```

Users were previously instructed to make a temporary copy of the conformer into a new OEGraphMol before passing it to the methods that should have been logically const. This is no longer necessary.

- OEShapeDatabaseScore. Transform will now only change the coordinates of the molecule as the name implies. The method will transform hydrogens and color atoms in the molecule.
- ShapeDatabaseServer.py will now remove hydrogens from hit lists so that results from a cached OEB file (OEP repareFast ROCSMo1) are identical to when the server is started on a non-cached OEB file.

## 8.19.3 Minor bug fixes

• OEShapeDatabase. Open and OEShapeDatabase. GetScores methods now throw an error message if a molecule contains no heavy atoms.

## 8.19.4 Python-specific changes

• OEShapeDatabaseScore methods will no longer release the Python global interpreter lock.

# 8.19.5 Documentation changes

- ShapeDatabasePrep.py example now has an optional argument to trim to a desired lower number of conformers.
- BestShapeOverlay.py example will now output the proper filenames when a problem occurs while opening them.
- Bugs in ShapeDatabaseServer.py, ShapeDatabaseClient.py, and ShapeDatabaseHistogram.py that were exposed when tested using Python 3.5 have been fixed. Python 3.5 now has a more efficient caching system in which file objects are required to be explicitly closed to ensure data writes are flushed.

# 8.20 FastROCS TK 1.6.0

## 8.20.1 New features

• The performance of **FastROCS** when loading a database into memory has been significantly improved when the appropriate caching has been done to the input OEB file. OEP repareFastROCSMo1 function has been added to allow preparing a molecule to be written to OEB so that it can be read very quickly by OEShapeDatabase. Open. It is highly recommended to pre-process input OEB files with this function to achieve faster load times. This works especially well in combination with OEPRECompress, resulting in uncompressed OEB files that are comparable to their gzip-compressed counterparts, even with extra cached information inside them.

**Warning:**  $OEPrepareFastROCSMol$  strips out information that **OMEGA** generates (i.e., hydrogen coordinates and conformer energies). Care must be taken when using these OEB files for alternative use cases. Please refer to the OEPrepareFastROCSMol documentation for a full accounting of how the molecules are changed.

- . OEFastROCSCacheStuff was never officially supported and has been replaced by the OEPrepareFastROCSMol function. It now throws a deprecation warning and will be removed in a future release.
- FastROCS TK should be binary compatible with more NVidia driver versions as of this release. Previously, **FastROCS TK** could only target a single NVidia driver version. Now, several can be targeted in a single toolkit build. This version of **FastROCS TK** will work on the following NVidia driver versions: 340.x, 346.x, and 352.x. This should significantly reduce FastROCS TK installation headaches.
- OEShapeDatabase. SetNumOpenThreads method has been added to control how many CPU operatingsystem threads are created when calling OEShapeDatabase. Open on an OEMolDatabase object.
- All *OEShapeDatabase* instances now share the same GPU context. Previously, creating many *OEShape-*Database instances would result in many operating system threads created per instance. This would often hit resource limits around the number of threads allowed in a single process.

## 8.20.2 Minor bug fixes

• OEShapeDatabase. Open now returns false if no molecules are read from the OEMolDatabase object.

# 8.20.3 Python-specific changes

- All FastROCS TK Python examples now use /usr/bin/env python to determine the appropriate Python interpreter to use. Previously, some examples were erroneously hardcoded to use /usr/bin/python.
- karma. py shape clustering example had a minor bug that affected how invalid file names were handled. This has been fixed.

## 8.20.4 Documentation changes

• The FastROCS TK *Installation* section is now more general and defers to the NVidia website for installation instructions. A list of supported NVidia drivers for **FastROCS TK** can also be found in the *Installation* section.

# 8.21 FastROCS TK 1.5.1

## 8.21.1 New features

• OEFastROCSHistogram has been added to retrieve FastROCS TK's score distribution for the entire database, not just the hits, in real-time during a FastROCS TK query. The ShapeDatabaseServer.py example was extended with the OEFastROCS:: QueryHistogram function, as well as the ShapeDatabaseProxy.py. The ShapeDatabaseClientHistogram.py is an example of a client program to retrieve the histogram from the server in real time and print it to the terminal.

# 8.21.2 Major bug fixes

- ShapeDatabaseServer.py will now make sure to attach SD data from the parent OEMCMolBase to the output overlaid conformer.
- ShapeDatabaseOEThrowSetLevel.py will now work to effectively turn on additional performance debugging information. The additional operating system threads started by the OEShapeDatabase will now inherit the OEErrorLevel being used by the thread to execute the query through OEShapeDatabase. GetScores or OEShapeDatabase. GetSortedScores.
- FastROCS TK will now be compatible with NVidia compute architecture 2.0 cards. FastROCS TK beta in 2015. Jun. 5 only worked on compute capability 3.x cards. The 2015. Jun. 6 release was a bug fix release to fix this oversight. FastROCS TK in 2015. Oct should now work with any compute capability 2.0 card (the Fermi architecture) or greater.

## 8.21.3 Minor bug fixes

• ShapeDatabaseServer.py will now release its port number upon termination more quickly. Previously, the server would sometimes fail because when a new process was started the port number was already reserved by the previous process.

## 8.21.4 Documentation fixes

• The Installation section now recommends installing the NVidia driver with the --disable-nouveau flag to ensure that the open source nouveau display driver kernel module is turned off. The NVidia CUDA documentation is a much better source of this installation information: http://docs.nvidia.com/cuda/ cuda-getting-started-guide-for-linux/#runfile-nouveau

## 8.21.5 General notices

- This is the last release to support FastROCS TK on Ubuntu 12.
- Supported NVIDIA Driver: 352.\* (see Supported NVIDIA Drivers for alternative FastROCS TK releases).

# 8.22 FastROCS TK 1.5.0

- This is an initial public beta release of FastROCS TK as part of the larger OpenEye Toolkit suite. Initial support is being limited to 64-bit Linux Python platforms. Please bear with us as we work to bring **FastROCS** TK up to the same level of quality as you should expect from every OpenEye toolkit.
- The core suite of *FastROCS TK examples* have been tested and will work in this distribution. Note, the examples are present in the Windows and OSX distributions, but the following examples only work on 64-bit Linux Python platforms:
  - ShapeDatabaseServer.py
  - ShapeDatabaseChunker.py
  - BestShapeOverlay.py
  - karma.py

As FastROCS TK works towards official release, example programs will likely change names and be redesigned. We will keep compatibility with the following core examples many of the current **FastROCS** users depend on:

- ShapeDatabaseServer.py
- ShapeDatabaseClient.py
- ShapeDatabaseIsLoaded.py
- ShapeDatabaseProxy.py
- ShapeDatabaseServer.py will no longer hang indefinitely whenever the gzipped results are requested by the client.
- ShapeDatabaseServer.py now supports specifying a different color force field, including a custom color force through a .cff file.
- ShapeDatabaseServer.py now supports specifying the hostname to bind to.
- BestShapeOverlay.py optimized by using OEMolDatabase class.

- The name of **FastROCS TK** python module has changed from oeshapedatabase to oefastrocs. The example scripts have already been updated to account for the name change.
- OEShapeDatabase will be much more efficient when the database is in an empty state.
- OEShapeDatabase will now co-exist with other GPU processes, including other instances of OEShapeDatabase objects. Previously, OEShapeDatabase was very aggressive in the amount of GPU memory allocated, even when the data set sizes were very small. OEShapeDatabase will now be much more frugal with the amount of GPU memory it allocates making it possible to use many more OEShapeDatabase simultaneously, provided each dataset is small.
- · OEShapeDatabase. GetSortedScores and OEShapeDatabase. GetScores will now error more reliably. Previously, an error could occur, like an out-of-memory problem on a GPU, and a partial list of results would be returned. This made it very difficult to notice when something was wrong, requiring someone to notice the error messages in the server log. Now, no results at all will be returned if any problem with the search occurs.
- · OEShapeDatabase. GetSortedScores and OEShapeDatabase. GetScores APIs have changed from strings of shape queries to take actual OEShapeQueryPublic objects.
- OEShapeDatabase. AddMo1 will now throw an error immediately if there are no atoms or conformers in the molecule.

Note: Supported NVIDIA Driver: 346.\* (see Supported NVIDIA Drivers for alternative FastROCS TK releases).

# 8.23 FastROCS TK 1.4.0

- The structure of the FastROCS tar-ball has changed to mimic an openeye distribution tree usually seen on Linux. All programs can now be found in the openeye/bin directory.
- This version of FastROCS was built with the NVIDIA 310 driver included in this distribution. FastROCS should continue to work with the 295 driver as OpenCL and CUDA have not changed version between these driver versions. However, if problems are experienced during the upgrade, please try upgrading the NVIDIA driver to the 310 version.

## 8.23.1 Features

- FlaskROCS, an example web page service has been added. See openeye/FlaskROCS/README for more information.
- ShapeDatabaseClient (both Python and Java) no longer requires the OpenEye toolkits to run. This should make client applications a lot more portable and easier to write. Clients written against version 1.3.1 servers and prior versions will still continue to work. The following demonstrates client commands and that their behavior is unchanged when upgrading the server to version 1.4.0.

The 1.3.1 and prior clients: ./ShapeDatabaseClient.py 1\_3\_1\_server\_addr query.sdf results.oeb # still works /ShapeDatabaseClient.py 1 3 1 server addr query.oeb results.oeb # still works ./ShapeDatabaseClient.py 1\_3\_1\_server\_addr query.sdf results.sdf # would never work, results had to be an oeb file

./ShapeDatabaseClient.py 1\_4\_0\_server\_addr query.sdf results.oeb # still works ./ShapeDatabaseClient.py 1\_4\_0\_server\_addr query.oeb results.oeb # still works ./ShapeDatabaseClient.py 1\_4\_0\_server\_addr query.sdf results.sdf # would never work, results had to be an oeb file

The 1.4.0 client will only work with 1.3.1 servers when the input and output format is oeb. However, the results file no longer needs to be oeb when running the 1.4.0 client against a 1.4.0 server. The following demonstrates client commands and that their behavior unchanged when upgrading the server to version 1.4.0.

The 1.4.0 client: ./ShapeDatabaseClient.py 1 3 1 server addr query.sdf results.oeb # won't work, query is sdf file ./ShapeDatabaseClient.py 1\_3\_1\_server\_addr query.oeb results.oeb # still works ./ShapeDatabaseClient.py 1 3 1 server addr query sdf results sdf # would never work, results had to be an oeb file

./ShapeDatabaseClient.py 1\_4\_0\_server\_addr query.sdf results.oeb # still works ./ShapeDatabaseClient.py 1\_4\_0\_server\_addr query.oeb results.oeb # still works ./ShapeDatabaseClient.py 1\_4\_0\_server\_addr query.sdf results.sdf # works now! results can be any file format

Note: The servers (ShapeDatabaseServer.py and ShapeDatabaseProxy.py) still require an OEChem license. Though it is a long term to remove this deficiency in licensing.

still require OEChem: ShapeDatabaseIsLoaded.py The following client scripts Shape-DatabaseOEThrowSetLevel.py

This can be coded around upon customer request.

Note: the distribution no longer ships with the OpenEye Java jar files.

- ShapeDatabasePrep multi-threaded program added to replace the CacheStuff.py script to quickly and efficiently prepare OEB database files for faster load times into FastROCS. It is now highly recommended to run this program on your database to save on load time performance by the server.
- The memory footprint of the ShapeDatabaseServer.py has been reduced by about half by making use of new experimental OEChem technology, the OEMolDatabase. This effectively uses the database file itself to serve requests for molecule connection tables. This also improved database load time performance by 2x. Load time is now affected by disk bandwidth, so better load times can be achieved by investing in faster hard drive, e.g., solid state drives.

Note: it is now highly recommended to pass ShapeDatabaseServer.py an uncompressed on the instead of a .oeb.gz file.

- ShapeDatabaseAddMols.py has been removed from the distribution. ShapeDatabaseServer.py is now a "readonly" database after it finishes loading.
- ShapeDatabaseOEThrowSetLevel.py can now set the server into the "Error" level, that is, warnings are not even printed.
- The ShapeDatabaseServer's XML RPC SubmitQuery method now takes 2 additional optional arguments: iformat='.oeb' and iformat='.oeb'. The *iformat* arguments specifies what file format the query is being sent in at the first argument to SubmitQuery, querymolstr. The oformat argument specified what file format the results should be back in from the *QueryResults* method. The default is OEB since clients prior to this version always sent data in the OEB format.
- Added the NumConfs method to the OEShapeDatabase object.
- OEFastROCSGetRelease added to return the version number of the library.
- CustomColorFFPrep.py script added to demonstrate how to cache color atoms on molecules to force the server and client to use a custom color force field.
- Support has been added for custom OEColorForceFields to the OEShapeDatabase and OEShapeDatabaseOptions objects. The color force field given to the OEShapeDatabaseOptions must be a subset of the color force field used to construct the OEShapeDatabase.

## 8.23.2 Bug Fixes

- Fixed a license check issue that would call sys.exit when no OEChem license was present while importing the oeshapedatabase module.
- Fixed a crash that would be caused by using OESetMemPoolMode after loading the oeshapedatabase module.
- FastROCS results will now be returned in a deterministic order when the scores are identical. The order of hits with identical scores would sometimes appear in a different order upon subsequent runs due to results being sorted in parallel by the server. FastROCS will now break this tie by falling back to the order that the molecules are in the database.

# 8.24 FastROCS TK 1.3.1

- Adding support for RHEL6-x64 based upon customer request.
- Reducing the size of the FastROCS tar-ball by removing some of the toolkit bloat.

# 8.25 FastROCS TK 1.3.0

- Major performance improvement in how FastROCS scales to multiple GPUs. The NVidia 275, 285, 295 driver introduced a severe performance regression that hampered FastROCS ability to scale across multiple GPUs. The solution was to use a different strategy to transfer data between the host and the device as well as scaling back the number of host threads launching jobs on the GPUs to only 1 per GPU.
- Many additions to the python interface to allow tweaking how FastROCS is parallelized and memory is moved around in the system: SetNumDevices, SetHostToDeviceStrategy, SetDeviceToHostStrategy, Set-NumThreadsPerDevice. The defaults should be reasonable for everyone while using the 295 NVidia driver. They're left here to allow easy tweaking on future drivers, though they may be removed once a toolkit version is released, so don't rely on them.
- Fixed timer restart in OEShapeDatabaseOptions that would cause a reused OEShapeDatabaseOptions object to include time spent on previous searches.
- Only 4 decimal places are stored in the SD data fields for Shape Tanimoto, Color Tanimoto, and Tanimoto Combo.
- Made the NVidia driver install portion of the README easier to follow.
- Removed the restriction to use molecules with less than 3 heavy atoms.

# 8.26 FastROCS TK 1.2.1

- FastROCS is now built with the 2011. Oct toolkit release. This has some significant performance improvements on the server load time.
- FastROCS is now built against the latest two shipping NVidia drivers: OpenCL 1.1 CUDA 4.1 inside the 285 NVidia driver; and OpenCL 1.0 CUDA 4.0 inside the 275 NVidia driver. These drivers solve some search initialization costs that were seen in some setups.
- The Vida extension is being removed from the FastROCS distribution as a new version is being bundled directly into Vida.
- Significant updates to the README to remove a lot of cruft that had accumulated during development.

# 8.27 FastROCS TK 1.1.1

- Fixed bug with shape query support that would cause the server to crash when passing an empty shape query.
- Made the client/server interaction more robust in passing errors back from the server to the client.

# 8.28 FastROCS TK 1.1.0

## 8.28.1 Major Bug Fixes

- Fixed color bug that was calculating incorrect static color scores. Large errors were caused whenever the shape optimization produced large translations.
- Fixed bug that was causing certain database molecules (usually flat molecules) to be collapsed to a single point during the inertial alignment step of loading the database. This would sometimes manifest as tanimotos being outside the normal 0-1 range.

## 8.28.2 Minor Bug Fixes

- Fixed incorrect color Gaussian width used in the color score calculation.
- Handle zero division error in the color tanimoto calculation caused whenever a molecule has no color atoms. These tanimotos will now be 0.0.
- In the event an error occurs in the OpenCL driver and a command queue can not be opened to the GPU device only retry a finite amount of time. That is, don't loop infinitely in the event of a lower level error.
- Fixing order dependence problem caused whenever PYTHONPATH was explicitly set overriding the search path explicitly set inside ShapeDatabaseServer.py.
- Fixed bug in ShapeDatabaseServer.py caused by OEHeader objects in OEB files. This will be fixed in a more general sense by the next toolkit release.
- ShapeDatabaseServer.py will only allow one client query to process at a time to ensure that GPU resources are not exhausted. This restriction may be lifted in a future version, but for now this is the best way to keep the server robust in a multi-user environments.
- Cached color in OEB files use compressed color atoms in order to not corrupt the OEB rotor offset compression format. Also use the cached "AllColor" self term as it is closer to how the grid color overlap is calculated.

## 8.28.3 Major Features

- Added support for Shape Query (.sq) files generated from vROCS. These files can now be passed directly to ShapeDatabaseClient.(py/java).
- Significant performance improvement to post scoring with static color. Post scoring with static color is now essentially "free" as it occurs on the CPU after the shape optimization on the GPU. To achieve this at least 2 CPU cores per Fermi GPU is recommended.

## 8.28.4 Minor Features

- Significant performance improvement by caching the underlying GPU context more effectively. Some queries were seeing a 1-2 second overhead per GPU device because the GPU context could not be cached. Later versions of the driver seem to support this without crashing. If this version starts giving odd crashing behavior, try updating the NVidia driver first.
- ShapeDatabaseChunker.py is a little more robust in choosing output file names.
- Added ability to use 8 inertial starting points.
- Added the CacheStuff.py script to cache as much as possible to improve database load time. Shape-DatabaseChunker.py updated to cache color stuff as well.
- Totally revamped the output of Debug mode to allow for timing the more asynchronous nature of FastROCS now.

# 8.29 FastROCS TK 1.0.1

• First version of FastROCS that is designed to only work on a specific hardware and driver configuration. This release will only work on NVidia hardware with the CUDA 3.2 driver. FastROCS will work on any modern NVidia card that reports a compute capability of 1.0 or greater. Typically this is any NVidia card shipped after 2006. For a complete list of cards refer to Appendix A in the CUDA C Programming Guide.

Note: The more stringent requirement is on the driver version, CUDA 3.2. For this reason FastROCS will be shipping with the required associated NVidia Linux driver embedded in the tar-ball: devdriver\_3.2\_linux\_64\_260.19.26.run

This requirement is also embedded into the tar-ball name as "OpenCL-1.0-CUDA-3.2" in case we need to support multiple versions or rev'ing to OpenCL 1.1 breaks compatibility. If a driver upgrade needs to occur due to some bug in some other third party software, let OpenEye know and we will see how best we can accommodate you.

• Added ShapeSimilarityMatrix.py example to write out a similarity matrix of an input database into a csv file suitable for feeding to downstream tools like cluster analysis. Note, due to the current slow speed of clCreate-Context, the example is not crazy performant on small datasets, but on larger sets it is as the cost of clCreate-Context becomes amortized.

# 8.30 FastROCS TK 1.0.0

- ShapeDatabaseServer.py now has a "-shapeOnly" option to run in a mode where color is not calculated at all. By default this option is off indicated that the server will use color. ShapeDatabaseProxy.py has been updated accordingly to automatically recognize whether to use ComboTanimoto and ShapeTanimoto to resort the results by.
- Fixing BestShapeOverlay.py to work with color.
- karma.py has been updated to work with color.

# 8.31 FastROCS TK 0.4.0

- An experimental release that includes color support meant for scientific validation with the following implementation caveats:
  - Static color scores are calculated using the alignment generated by a shape driven optimization. Note, a color score is calculated for each of the 4 inertial starting points. Therefore, it is possible for a less favorable shape score to be picked due to a higher tanimoto combo. This is the only part color plays in the optimization.
- Color is calculated using the grid method in order to be fast enough to keep up with the GPU generated alignments.
- Color is calculated on the CPU so there is no increased bus overhead for color, but there is a significant increase in CPU usage. Calculating color on the CPU is a strategic move to see if we can get away with calculating color without any significant increase to the overall search time. This release gets part of the way towards that goal: a single core of a Xeon CPU E5520 at 2.27GHz is about 2 times slower at calculating static colors coming out of a single NVidia C2050. Future releases will spread this over multiple CPU cores to better even out the load.
  - The OEShapeScore object has been renamed to OEShapeDatabaseScore to disambiguate it. Renamed the method GetTanimoto to GetShapeTanimoto. Added GetColorTanimoto and GetTanimotoCombo.
  - Add the OEShapeDatabaseType constants namespace to indicate whether a database should store color information as well and whether a query should use color as well.
  - Added OEShapeDatabaseOptions::SetScoreType to be used with the OEShapeDatabaseType constants to indicate what type of search is being done.
  - Renamed OEShapeDatabase::SetGridSpacing to OEShapeDatabase::SetShapeGridSpacing. Added OE-ShapeDatabase::SetColorGridSpacing.
  - Load time has been significantly increased due to the calculation of color atoms during load time.

# 8.32 FastROCS TK 0.3.1

• The server would sometimes crash with a "clCreateContext" error. This is being thrown from the NVidia driver for some unknown reason. This release will continually try to create the worker thread despite all else. Note, if something is truly wrong, this could appear to hang queries as the server will keep retrying to create a context on the GPU, but at least the log will indicate an error code now that may tell us more about what is going on.

# 8.33 FastROCS TK 0.3.0

- Added ShapeDatabaseAddMols.py script to add molecules to a running ShapeDatabaseServer.
- Added ShapeDatabaseIsLoaded.py script to report whether the initial database load has completed.
- Added argument to ShapeDatabaseClient.py for the number of hits to return, defaults to 100.
- Redesigned how the BestShapeOverlay.py script runs to be more useful for doing evaluations.
- Restricting OEShapeDatabase to only run on one type of device and prefer to run on a GPU, and fall back to a CPU device only if there is no GPU present. Used to be that on OS X the search would run on the GPU and CPU simultaneously, however, the results of the overlay could differ depending on whether they were sent to the GPU or the CPU. Due to dynamic load balancing between the CPU and GPU this could change the rank of the results returned in an apparently non-deterministic manner. It is not pleasant for an end-user to run the same query multiple times and get different results so we restrict searches to either CPU or GPU, not both now.

Note, this only would occur on OS X. The NVidia implementation doesn't support a CPU device, so this never occurred there.

# 8.34 FastROCS TK 0.2.3

• OSX only release to fix obscure bug that occurred when using an NVidia GPU through Apple's OpenCL implementation.

# 8.35 FastROCS TK 0.2.2

- Fixed a major bug that would cause very high shape tanimotos to be calculated when cached color atoms were present in the input database.
- Added symlink from SLES to SLED to work around OEToolkit issue of not recognizing those as equivalent systems.
- Querying the database with an empty molecule will no longer crash.
- Added BenchmarkDatabaseTransfer.py benchmark to determine the maximum speed being achieved when transferring database chunks across the bus.

# 8.36 FastROCS TK 0.2.1

- Added support for SUSE 11.
- Added cuda.sh shell script that will create the appropriate nvidia device entries inside /dev/. It is a known issue on SLES11 the nvidia driver will create the /dev/ entries with the wrong permissions. Also, it is known issue that on RHEL5 LDAP users could not launch OpenCL based programs. Running this shell script as root (i.e. during boot) should fix these problems. We should push on NVidia to make this part of their driver installer.
- The PrintOpenCLDevices utility will now print "platform" information about the driver(s) found on the system. This is useful for displaying which version of CUDA is installed, instead of just what version of OpenCL is installed.
- Fixed problem where some systems without SWAP memory would crash with an out of memory error when the OEShapeDatabase object would try to reserve large swaths of memory. The virtual memory size of the process should now track more closely with the resident memory size.

# 8.37 FastROCS TK 0.2.0

- Added example of a XML RPC client written in Java. (See the javaclient directory.)
- Added example program for doing shape clustering. (See karma.py)
- Refactored benchmarking scripts into the benchmarks directory.
  - Added benchmarks for database size and random access patterns.
- Improved database load time of ShapeDatabaseServer.py by multithreading
  - It is now thread safe to use OEShapeDatabase::AddMol from multiple threads. Note, it is not thread safe to call Get(Sorted)Scores while calling AddMol. Let me know if this is desired.

# 8.38 FastROCS TK 0.1.1

• Adding the ShapeDatabaseOEThrowSetLevel.py script to adjust the verbosity level of the server without restarting it.

# 8.39 FastROCS TK 0.1.0

• First public release.

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

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

## **ELEVEN**

# **CITATION**

# 11.1 Orion ® Floes

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

# **11.2 Toolkits and Applications**

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

# 11.3 OpenEye Web Services

To cite use of the Macromolecular Data Service (MMDS) web service, please use the syntax:

Macromolecular Data Service <version-number>. OpenEye, Cadence Molecular Sciences, -Santa Fe, NM. http://www.eyesopen.com.

### For example:

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

# **TWELVE**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project                  | Website                                                                             | License            |
|----------------------------------|-------------------------------------------------------------------------------------|--------------------|
| abseil-cpp                       | https://github.com/abseil/abseil-cpp                                                | https:/            |
| absl-py                          | https://github.com/abseil/abseil-py                                                 | https:/            |
| aiohttp                          | https://docs.aiohttp.org/en/stable/                                                 | https:/            |
| aiosignal                        | https://github.com/aio-libs/aiosignal                                               | https:/            |
| Amazon Linux 2                   | https://aws.amazon.com/amazon-linux-2                                               | N/A                |
| AmberUtils                       | http://ambermd.org                                                                  | N/A                |
| ambit                            | https://github.com/khimaros/ambit                                                   | https:/            |
| amqp                             | https://github.com/celery/py-amqp                                                   | https:/            |
| anaconda-anon-usage              | Orion Floes                                                                         | https:/            |
| angular                          | https://github.com/angular/angular.js                                               | https:/            |
| angular-animate                  | https://github.com/angular/angular.js                                               | https:/            |
| angular-cache                    | https://github.com/jmdobry/angular-cache                                            | https:/            |
| angular-cookies                  | https://github.com/angular/angular.js                                               | https:/            |
| angular-loggly-logger            | https://github.com/ajbrown/angular-loggly-logger                                    | https:/            |
| angular-mocks                    | https://github.com/angular/angular.js                                               | https:/            |
| angular-resource                 | https://github.com/angular/angular.js                                               | https:/            |
| angular-toggle-switch            | https://github.com/cgarvis/angular-toggle-switch                                    | https:/            |
| angular-ui-grid                  | https://github.com/angular-ui/ui-grid                                               | https:/            |
| angular-ui-router                | https://github.com/angular-ui/ui-router                                             | https:/            |
| angular-ui-tree                  | https://github.com/angular-ui-tree/angular-ui-tree                                  | https:/            |
| angular-vs-repeat                | https://github.com/kamilkp/angular-vs-repeat                                        | https:/            |
| aniso8601                        | https://bitbucket.org/nielsenb/aniso8601                                            | https:/            |
| annotated-types                  | https://github.com/annotated-types/annotated-types                                  | https:/            |
| anyio                            | https://github.com/agronholm/anyio                                                  | https:/            |
| appdirs                          | http://github.com/ActiveState/appdirs                                               | http://            |
| appengine                        | https://google.golang.org/appengine                                                 | https:/            |
| arabic-reshaper                  | https://github.com/mpcabd/python-arabic-reshaper/                                   | https:/            |
| archspec                         | https://github.com/archspec/archspec/blob/master/README.md                          | https:/            |
| Name of Project                  | Website                                                                             | License            |
| argon2-cffi                      | https://github.com/hynek/argon2-cffi                                                | https://           |
| argon2-cffi-bindings             | https://github.com/hynek/argon2-cffi-bindings                                       | https://           |
| arpack                           | https://www.caam.rice.edu/software/ARPACK/                                          | https://           |
| ascii85                          | https://github.com/huandu/node-ascii85                                              | https://           |
| ase                              | https://wiki.fysik.dtu.dk/ase/                                                      | https://           |
| asgiref                          | https://github.com/django/asgiref/                                                  | https://           |
| asn1crypto                       | https://github.com/wbond/asn1crypto                                                 | https://           |
| assertions go-render             | https://github.com/smartystreets/assertions/internal/go-render/render               | https://           |
| assertions oglmatchers           | https://github.com/smartystreets/assertions/internal/oglematchers                   | https://           |
| assertions                       | https://github.com/smartystreets/assertions                                         | https://           |
| asttokens                        | https://github.com/gristlabs/asttokens                                              | https://           |
| astunparse                       | https://github.com/simonpercivall/astunparse                                        | https://           |
| async-lru                        | https://github.com/aio-libs/async-lru                                               | https://           |
| async-timeout                    | https://github.com/aio-libs/async-timeout                                           | https://           |
| atk-1.0                          | https://docs.gtk.org/atk/                                                           | https://           |
| atomic                           | https://github.com/uber-go/atomic                                                   | https://           |
| atomicwrites                     | https://github.com/untitaker/python-atomicwrites                                    | https://           |
| attrs                            | https://www.attrs.org/                                                              | https://           |
| aws-sdk-go                       | https://github.com/aws/aws-sdk-go                                                   | https://           |
| Babel                            | https://github.com/python-babel/babel                                               | https://           |
| backcall                         | https://github.com/takluyver/backcall                                               | https://           |
| backports                        | https://github.com/brandon-rhodes/backports                                         | https://           |
| backports.functools-lru-cache    | https://github.com/jaraco/backports.functools_lru_cache                             | https://           |
| base62                           | https://github.com/kare/base62                                                      | https://           |
| beautifulsoup4                   | https://www.crummy.com/software/BeautifulSoup/                                      | https://           |
| billiard                         | https://github.com/celery/billiard                                                  | https://           |
| biopython                        | https://biopython.org                                                               | https://           |
| biotite                          | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https://           |
| bitset                           | https://github.com/willf/bitset                                                     | https://           |
| blas                             | https://www.netlib.org/blas/                                                        | https://           |
| bleach                           | https://github.com/mozilla/bleach                                                   | https://           |
| blessings                        | https://github.com/erikrose/blessings                                               | https://           |
| blinker                          | https://pythonhosted.org/blinker/                                                   | https://           |
| blosc                            | https://github.com/Blosc/python-blosc                                               | https://           |
| blosc2                           | https://github.com/Blosc/python-blosc2                                              | https://           |
| boltons                          | https://github.com/mahmoud/boltons                                                  | https://           |
| boost                            | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://           |
| boost-cpp                        | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https://           |
| bootstrap-vue                    | https://github.com/bootstrap-vue/bootstrap-vue                                      | https://           |
| boto3                            | https://github.com/boto/boto3                                                       | https://           |
| botocore                         | https://github.com/boto/botocore                                                    | https://           |
| Bottleneck                       | https://bottleneck.readthedocs.io/en/latest/index.html                              | https://           |
| <b>Brotli</b>                    | https://github.com/google/brotli                                                    | https://           |
| brotli-bin                       | https://github.com/google/brotli                                                    | https://           |
| brotli-python                    | http://python-hyper.org/projects/brotlipy/en/latest/                                | https://           |
| brotlipy                         | https://github.com/python-hyper/brotlicffi                                          | https://           |
| bson                             | http://github.com/py-bson/bson                                                      | https://           |
| bytefmt                          | https://code.cloudfoundry.org/bytefmt                                               | https://           |
| bzip2                            | https://www.bzip.org                                                                | https://           |
|                                  |                                                                                     | J.                 |
| Name of Project                  | Website                                                                             | Licen              |
| c-ares                           | https://github.com/c-ares/c-ares                                                    | https:/            |
| ca-certificates                  | https://github.com/conda-forge/ca-certificates-feedstock                            | https:/            |
| cached-property                  | https://github.com/pydanny/cached-property                                          | https:/            |
| cachetools                       | https://github.com/tkem/cachetools/                                                 | https:/            |
| cairo                            | https://pycairo.readthedocs.io/en/latest/                                           | https:/            |
| canvas                           | https://github.com/Automattic/node-canvas                                           | https:/            |
| cctbx                            | https://github.com/cctbx/cctbx_project                                              | https:/            |
| celery                           | https://github.com/celery/celery                                                    | https:/            |
| Cerberus                         | https://docs.python-cerberus.org/en/stable/                                         | https:/            |
| certifi                          | https://certifiio.readthedocs.io/en/latest/                                         | https:/            |
| cffi                             | https://github.com/python-cffi                                                      | https:/            |
| cftime                           | https://pypi.org/project/cftime/                                                    | https:/            |
| chardet                          | https://github.com/chardet/chardet                                                  | https:/            |
| charset-normalizer               | https://github.com/ousret/charset_normalizer                                        | https:/            |
| chunkreader                      | https://github.com/jackc/chunkreader/v2                                             | https:/            |
| click                            | https://palletsprojects.com/p/click/                                                | https:/            |
| click-completion                 | https://github.com/click-contrib/click-completion                                   | https:/            |
| click-didyoumean                 | https://github.com/click-contrib/click-didyoumean                                   | https:/            |
| click-plugins                    | https://github.com/click-contrib/click-plugins                                      | https:/            |
| click-repl                       | https://github.com/untitaker/click-repl                                             | https:/            |
| cloudpickle                      | https://github.com/cloudpipe/cloudpickle                                            | https:/            |
| cmake                            | https://cmake.org/                                                                  | https:/            |
| colorama                         | https://github.com/tartley/colorama                                                 | https:/            |
| comm                             | https://github.com/ipython/comm                                                     | https:/            |
| compose                          | https://github.com/docker/compose                                                   | https:/            |
| conda-content-trust              | https://github.com/conda/conda-content-trust                                        | https:/            |
| conda-libmamba-solver            | https://github.com/conda/conda-libmamba-solver                                      | https:/            |
| conda-package-handling           | https://github.com/conda/conda-package-handling                                     | https:/            |
| conda-package-streaming          | https://anaconda.org/conda-forge/conda-package-streaming                            | https:/            |
| conda-token                      | https://anaconda.org/anaconda/conda-token                                           | https:/            |
| confuse                          | https://github.com/beetbox/confuse                                                  | https:/            |
| contourpy                        | https://github.com/contourpy/contourpy                                              | https:/            |
| cpp-peglib                       | https://github.com/yhirose/cpp-peglib                                               | https:/            |
| cryptography                     | https://github.com/pyca/cryptography                                                | https:/            |
| cssselect2                       | https://github.com/Kozea/cssselect2/                                                | https:/            |
| cudatoolkit                      | https://developer.nvidia.com/cuda-toolkit                                           | https:/            |
| $cupy-cuda113$                   | https://cupy.dev/                                                                   | https:/            |
| curl                             | https://curl.se                                                                     | https:/            |
| cycler                           | https://github.com/matplotlib/cycler                                                | https:/            |
| cyrus-sasl                       | https://github.com/cyrusimap/cyrus-sasl                                             | https:/            |
| Cython                           | https://cython.org                                                                  | https:/            |
| $\overline{d3}$                  | https://github.com/mbostock/d3                                                      | https:/            |
| dataclasses                      | https://github.com/ericvsmith/dataclasses                                           | https:/            |
| ddsketch                         | http://github.com/datadog/sketches-py                                               | https:/            |
| debugpy                          | https://aka.ms/debugpy                                                              | https:/            |
| decimal                          | https://github.com/shopspring/decimal                                               | https:/            |
| decorator                        | https://github.com/micheles/decorator                                               |                    |
| deepdiff                         | https://github.com/seperman/deepdiff                                                | https:/<br>https:/ |
| deeptime                         | https://github.com/deeptime-ml/deeptime                                             | https:/            |
|                                  |                                                                                     |                    |
| Name of Project                  | Website                                                                             | License            |
| defusedxml                       | https://github.com/tiran/defusedxml                                                 | https:/            |
| dill                             | https://github.com/uqfoundation/dill                                                | https:/            |
| distro                           | Orion Floes                                                                         | https:/            |
| Django                           | https://www.djangoproject.com/                                                      | https:/            |
| django-classy-tags               | https://github.com/django-cms/django-classy-tags                                    | https:/            |
| django-cors-headers              | https://github.com/adamchainz/django-cors-headers                                   | https:/            |
| django-csp                       | https://github.com/mozilla/django-csp                                               | https:/            |
| django-extensions                | https://github.com/django-extensions/django-extensions                              | https:/            |
| django-filter                    | https://github.com/carltongibson/django-filter/tree/master                          | https:/            |
| django-redis                     | https://github.com/jazzband/django-redis                                            | https:/            |
| django-taggit                    | https://github.com/jazzband/django-taggit                                           | https:/            |
| django-taggit-serializer         | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/            |
| django-taggit-templatetags2      | https://github.com/fizista/django-taggit-templatetags2                              | https:/            |
| djangorestframework              | https://www.django-rest-framework.org/                                              | https:/            |
| dkh                              | https://psicode.org/psi4manual/master/dkh.html                                      | https:/            |
| dm-tree                          | https://github.com/deepmind/tree                                                    | https:/            |
| docker-py                        | https://github.com/docker/docker-py/                                                | https:/            |
| docopt                           | https://docopt.org                                                                  | https:/            |
| docutils                         | https://docutils.sourceforge.io                                                     | https:/            |
| drf-dynamic-fields               | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/            |
| editdistance                     | https://github.com/roy-ht/editdistance                                              | https:/            |
| eigen                            | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/            |
| einops                           | https://github.com/arogozhnikov/einops                                              | https:/            |
| entrypoints                      | https://github.com/takluyver/entrypoints                                            | https:/            |
| errors                           | https://github.com/pkg/errors                                                       | https:/            |
| eslint-plugin                    | https://github.com/typescript-eslint/typescript-eslint                              | https:/            |
| et_xmlfile                       | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/            |
| exceptiongroup                   | https://github.com/agronholm/exceptiongroup                                         | https:/            |
| executing                        | https://github.com/alexmojaki/executing                                             | https:/            |
| expat                            | https://libexpat.github.io                                                          | https:/            |
| fastjsonschema                   | https://github.com/horejsek/python-fastjsonschema                                   | https:/            |
| fastrlock                        | https://github.com/scoder/fastrlock                                                 | https:/            |
| fftw                             | https://www.fftw.org                                                                | comm               |
| filebuffer                       | https://github.com/mattetti/filebuffer                                              | https:/            |
| filelock                         | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/            |
| finufft                          | https://github.com/flatironinstitute/finufft                                        | https:/            |
| Flask                            | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/            |
| flatbuffers                      | https://google.github.io/flatbuffers/                                               | https:/            |
| flit-core                        | https://github.com/pypa/flit                                                        | https:/            |
| FLTK                             | https://www.fltk.org/index.php                                                      | https:/            |
| fmt                              | https://fmt.dev/latest/index.html                                                   | https:/            |
| font-awesome                     | https://github.com/FortAwesome/Font-Awesome                                         | https:/            |
| font-ttf-dejavu-sans-mono        | https://dejavu-fonts.github.io                                                      | https:/            |
| font-ttf-inconsolata             | https://fonts.google.com/specimen/Inconsolata                                       | https:/            |
| font-ttf-source-code-pro         | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/            |
| font-ttf-ubuntu                  | https://fonts.google.com/specimen/Ubuntu                                            |                    |
| fontconfig                       | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/            |
| fonts-conda-ecosystem            | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/            |
| fonts-conda-forge                | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/            |
| Name of Project                  | Website                                                                             | License            |
| fonttools                        | https://github.com/fonttools/fonttools                                              | https://           |
| freetype                         | https://freetype.org                                                                | https://           |
| fribidi                          | https://github.com/fribidi/fribidi                                                  | https://           |
| frozendict                       | Orion Floes                                                                         | https://           |
| frozenlist                       | https://github.com/aio-libs/frozenlist                                              | https://           |
| fsmlite                          | https://github.com/tkem/fsmlite                                                     | https://           |
| fsspec                           | https://github.com/fsspec/filesystem_spec                                           | https://           |
| funcy                            | https://github.com/Suor/funcy                                                       | https://           |
| gast                             | https://github.com/serge-sans-paille/gast/                                          | https://           |
| gau2grid                         | https://github.com/dgasmith/gau2grid                                                | https://           |
| gax-go                           | https://github.com/googleapis/gax-go/v2                                             | https://           |
| gdk-pixbuf                       | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https://           |
| gemmi                            | https://gemmi.readthedocs.io/en/latest/                                             | https://           |
| genproto                         | https://google.golang.org/genproto/googleapis                                       | https://           |
| geometric                        | https://openbase.com/python/geometric                                               | https://           |
| giflib                           | https://giflib.sourceforge.net                                                      | https://           |
| glib                             | https://docs.gtk.org/glib/                                                          | https://           |
| GLM Library                      | https://github.com/g-truc/glm                                                       | https://           |
| gls                              | https://github.com/jtolds/gls                                                       | https://           |
| go-cleanhttp                     | https://github.com/hashicorp/go-cleanhttp                                           | https://           |
| go-connections                   | https://github.com/docker/go-connections                                            | https://           |
| go-cpio                          | https://github.com/cavaliercoder/go-cpio                                            | https://           |
| go-getter                        | https://github.com/hashicorp/go-getter                                              | https://           |
| go-homedir                       | https://github.com/mitchellh/go-homedir                                             | https://           |
| go-ini                           | https://github.com/go-ini/ini                                                       | https://           |
| go-jmespath                      | https://github.com/jmespath/go-jmespath                                             | https://           |
| go-junit-report                  | https://github.com/jstemmer/go-junit-report                                         | https://           |
| go-netrc                         | https://github.com/bgentry/go-netrc/netrc                                           | https://           |
| go-ole                           | https://github.com/go-ole/go-ole                                                    | https://           |
| go-pg                            | https://github.com/go-pg/pg                                                         | https://           |
| go-redis                         | https://github.com/go-redis/redis/v8                                                | https://           |
| go-rendezvous                    | https://github.com/dgryski/go-rendezvous                                            | https://           |
| go-safetemp                      | https://github.com/hashicorp/go-safetemp                                            | https://           |
| go-sysconf                       | https://github.com/tklauser/go-sysconf                                              | https://           |
| go-testing-interface             | https://github.com/mitchellh/go-testing-interface                                   | https://           |
| go-units                         | https://github.com/docker/go-units                                                  | https://           |
| go-version                       | https://github.com/hashicorp/go-version                                             | https://           |
| go-zglob                         | https://github.com/mattn/go-zglob                                                   | https://           |
| go.opencensus                    | https://go.opencensus.io                                                            | https://           |
| gobrake.v2                       | https://gopkg.in/airbrake/gobrake.v2                                                | https://           |
| goconvey                         | https://github.com/smartystreets/goconvey                                           | https://           |
| golden-layout                    | https://github.com/deepstreamIO/golden-layout                                       | https://           |
| google-auth                      | https://google-auth.readthedocs.io/en/master/                                       | https://           |
| google-auth-oauthlib             | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https://           |
| google-cloud-go                  | https://cloud.google.com/go                                                         | https://           |
| google-cloud-go/storage          | https://cloud.google.com/go/storage                                                 | https://           |
| google-pasta                     | https://github.com/google/pasta                                                     | https://           |
| google.golang.org/api            | https://google.golang.org/api                                                       | https://           |
| gopsutil                         | https://github.com/shirou/gopsutil                                                  | https://           |
| Name of Project                  | Website                                                                             | License            |
| gorilla websocket                | https://github.com/gorilla/websocket                                                | https:/            |
| graphite2                        | https://github.com/silnrsi/graphite                                                 | https:/            |
| graphviz                         | https://graphviz.org/                                                               | https:/            |
| greenlet                         | https://greenlet.readthedocs.io/en/latest/                                          | https:/            |
| groupcache                       | https://github.com/golang/groupcache                                                | https:/            |
| grpc                             | https://google.golang.org/grpc                                                      | https:/            |
| grpc-cpp                         | https://github.com/grpc/grpc                                                        | https:/            |
| grpcio                           | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   | https:/            |
| gtk2                             | https://gitlab.gnome.org/GNOME/gtk                                                  | https:/            |
| gts                              | https://sourceforge.net/projects/gts/                                               | https:/            |
| h5py                             | https://www.h5py.org                                                                | https:/            |
| harfbuzz                         | https://github.com/harfbuzz/harfbuzz                                                | https:/            |
| hdbscan                          | https://hdbscan.readthedocs.io/en/latest/                                           | https:/            |
| hdf4                             | https://www.hdfgroup.org/solutions/hdf4/                                            | https:/            |
| hdf5                             | https://www.hdfgroup.org/solutions/hdf5/                                            | https:/            |
| he                               | https://github.com/mathiasbynens/he                                                 | https:/            |
| html-loader                      | https://github.com/webpack-contrib/html-loader                                      | https:/            |
| html5lib                         | https://github.com/html5lib/html5lib-python                                         | https:/            |
| htslib                           | https://www.htslib.org                                                              | https:/            |
| humanize                         | https://github.com/jmoiron/humanize                                                 | https:/            |
| icu                              | https://github.com/unicode-org/icu                                                  | https:/            |
| idna                             | https://github.com/kjd/idna                                                         | https:/            |
| imageio                          | https://github.com/imageio/imageio                                                  | https:/            |
| imagesize                        | https://github.com/shibukawa/imagesize_py                                           | https:/            |
| ImmuneBuilder                    | https://github.com/oxpig/ImmuneBuilder/tree/main                                    | https:/            |
| importlib-metadata               | https://github.com/python/importlib_metadata                                        | https:/            |
| importlib_resources              | https://github.com/python/importlib_resources                                       | https:/            |
| InChI                            | https://iupac.org/who-we-are/divisions/division-details/inchi/                      | https:/            |
| inflection                       | https://github.com/jinzhu/inflection                                                | https:/            |
| ini.v1                           | https://gopkg.in/ini.v1                                                             | https:/            |
| iniconfig                        | https://github.com/pytest-dev/iniconfig                                             | https:/            |
| innersvg-polyfill                | https://github.com/dnozay/innersvg-polyfill                                         | https:/            |
| intel-openmp                     | https://github.com/hermitcore/libomp_oss                                            | https:/            |
| ipykernel                        | https://ipython.org                                                                 | https:/            |
| ipython                          | https://ipython.org                                                                 | https:/            |
| ipython-genutils                 | http://ipython.org                                                                  | https:/            |
| ipywidgets                       | http://jupyter.org                                                                  | https:/            |
| isodate                          | https://github.com/gweis/isodate/                                                   |                    |
| itsdangerous                     | https://palletsprojects.com/p/itsdangerous/                                         | https:/            |
| jax                              | https://github.com/google/jax                                                       | https:/            |
| jaxlib                           | https://github.com/google/jax                                                       | https:/            |
| jedi                             | https://jedi.readthedocs.io/en/latest/                                              | https:/            |
| Jinja2                           | https://palletsprojects.com/p/jinja/                                                | https:/            |
| jmespath                         | https://github.com/jmespath/jmespath.py                                             | https:/            |
| joblib                           | https://joblib.readthedocs.io/en/latest/                                            | https:/            |
| jpeg                             | https://www.ijg.org                                                                 | https:/            |
| json5                            | https://github.com/dpranke/pyjson5                                                  | https:/            |
| jsonfield                        | https://github.com/dmkoch/django-jsonfield/                                         | https:/            |
| jsonpatch                        | https://github.com/stefankoegl/python-json-patch                                    | https:/            |
|                                  |                                                                                     | Τ                  |
| Name of Project                  | Website                                                                             | Licen              |
| jsonpickle                       | https://github.com/jsonpickle/jsonpickle                                            | https:             |
| jsonpointer                      | https://github.com/stefankoegl/python-json-pointer                                  | https:             |
| jsonschema                       | https://github.com/python-jsonschema/jsonschema                                     | https:             |
| jsonschema-specifications        | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:             |
| jstat                            | https://github.com/jstat/jstat                                                      | https:             |
| jupyter-client                   | https://jupyter.org                                                                 | https:             |
| jupyter-core                     | https://jupyter.org                                                                 | https:             |
| jupyter-events                   | https://github.com/jupyter/jupyter_events                                           | https:             |
| jupyter-lsp                      | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:             |
| jupyter-serverhttp://jupyter.org | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE                  |                    |
| jupyterlab                       | https://github.com/jupyterlab/jupyterlab                                            | https:/            |
| jupyterlab-pygments              | http://jupyter.org                                                                  | https:             |
| jupyterlab-widgets               | http://jupyter.org                                                                  | https:/            |
| jupyterlab_server                | https://github.com/jupyterlab/jupyterlab_server                                     | https:             |
| jupyter_client                   | http://jupyter.org                                                                  | https:             |
| jupyter_core                     | http://jupyter.org                                                                  | https:             |
| jupyter_server                   | https://github.com/jupyter-server/jupyter_server                                    | https:             |
| jupyter_server_terminals         | https://github.com/jupyter-server/jupyter_server_terminals                          | https:             |
| kaleido                          | https://github.com/plotly/Kaleido                                                   | https:             |
| keras                            | https://github.com/keras-team/keras                                                 | https:             |
| Keras-Preprocessing              | https://github.com/keras-team/keras-preprocessing                                   | https:             |
| keras-tuner                      | https://github.com/keras-team/keras-tuner                                           | https:             |
| keyring                          | https://github.com/jaraco/keyring                                                   | https:             |
| keyutils                         | https://github.com/sassoftware/python-keyutils                                      | https:             |
| kiwisolver                       | https://kiwisolver.readthedocs.io/en/latest/                                        | https:             |
| kombu                            | https://kombu.readthedocs.io                                                        | https:/            |
| krb5                             | https://web.mit.edu/kerberos/                                                       | https:             |
| kt-legacy                        | https://github.com/haifeng-jin/kt-legacy                                            | https:/            |
| lazy_loader                      | https://github.com/scientific-python/lazy_loader                                    | https:/            |
| lcms2                            | https://www.littlecms.com                                                           | https:/            |
| lerc                             | https://github.com/Esri/lerc                                                        | https:             |
| libarchive                       | http://www.libarchive.org                                                           | https:             |
| libblas                          | https://www.netlib.org/blas/                                                        | https:             |
| libbrotlicommon                  | https://github.com/google/brotli                                                    | https:             |
| libbrotlidec                     | https://github.com/google/brotli                                                    | https:/            |
| libbrotlienc                     | https://github.com/google/brotli                                                    | https:/            |
| libcblas                         | https://anaconda.org/conda-forge/libcblas                                           | N/A                |
| libclang                         | <b>Orion Floes</b>                                                                  | https:             |
| libcurl                          | https://curl.se/libcurl/                                                            | https:             |
| libcxx                           | https://github.com/llvm-mirror/libcxx                                               | https:             |
| libdb                            | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:             |
| libdeflate                       | https://github.com/ebiggers/libdeflate                                              | https:             |
| libedit                          | https://thrysoee.dk/editline/                                                       | http://            |
| libev                            | https://software.schmorp.de/pkg/libev.html                                          | https:             |
| libffi                           | https://github.com/libffi/libffi                                                    | https:             |
| libgcrypt                        | https://gnupg.org/software/index.html                                               | https:             |
| libgd                            | https://libgd.github.io                                                             | https:             |
| libglib                          | https://github.com/PolMine/libglib                                                  | https:             |
| libiconv                         | https://www.gnu.org/software/libiconv/                                              | https:             |
|                                  |                                                                                     |                    |
|                                  |                                                                                     | -Li                |
| Name of Project                  | Website                                                                             | Licen              |
| libint                           | https://tinyurl.com/yvw97wbw                                                        | https:/            |
| liblapack                        | http://www.netlib.org/lapack/                                                       | https:/            |
| liblapacke                       | https://anaconda.org/conda-forge/liblapacke                                         | https:/            |
| libmamba                         | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https:/            |
| libmambapy                       | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https:/            |
| libnetcdf                        | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/            |
| libnghttp2                       | https://github.com/nghttp2/nghttp2                                                  | https:/            |
| libopenblas                      | https://www.openblas.net/                                                           | https:/            |
| libpng                           | https://www.libpng.org/pub/png/libpng.html                                          | https:/            |
| libpq                            | https://www.postgresql.org/                                                         | https:/            |
| librsvg                          | https://gitlab.gnome.org/GNOME/librsvg                                              | https:/            |
| libsolv                          | https://github.com/openSUSE/libsolv                                                 | https:/            |
| libssh2                          | https://github.com/libssh2/libssh2                                                  | https:/            |
| libtiff                          | https://www.libtiff.org/                                                            | https:/            |
| libtrust                         | https://github.com/docker/libtrust                                                  | https:/            |
| libuuid                          | https://sourceforge.net/projects/libuuid/                                           | https:/            |
| libuv                            | https://github.com/libuv/libuv                                                      | https:/            |
| libwebp                          | https://chromium.googlesource.com/?format=HTML                                      | https:/            |
| libwebp-base                     | https://chromium.googlesource.com/?format=HTML                                      |                    |
| libxc                            | https://www.tddft.org/programs/libxc/                                               | https:/            |
| libxcb                           |                                                                                     | https:/            |
|                                  | https://xcb.freedesktop.org                                                         | https:/            |
| libxml2                          | https://git.gnome.org/browse/libxml2/                                               | https:/            |
| libxmlsec1                       | https://github.com/lsh123/xmlsec                                                    | https:/            |
| libxslt                          | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https:/            |
| libzlib                          | https://zlib.net                                                                    | https:/            |
| lime                             | https://github.com/marcotcr/lime                                                    | https:/            |
| $\overline{\text{lit}}$          | http://llvm.org                                                                     | https:/            |
| llvm-openmp                      | https://github.com/llvm-mirror/openmp                                               | https:/            |
| <b>Ilymlite</b>                  | http://llvmlite.readthedocs.io                                                      | https:/            |
| loader-utils                     | https://github.com/webpack/loader-utils                                             | https:/            |
| logomaker                        | https://logomaker.readthedocs.io/en/latest/                                         | https:/            |
| logrus                           | https://github.com/sirupsen/logrus                                                  | https:/            |
| logrus-airbrake-hook.v2          | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/            |
| lxml                             | https://lxml.de                                                                     | https:/            |
| $1z4-c$                          | https://www.lz4.org/                                                                | https:/            |
| markdown                         | https://github.com/evilstreak/markdown-js                                           | https:/            |
| markdown-it-py                   | <b>Orion Floes</b>                                                                  | https:/            |
| MarkupSafe                       | https://palletsprojects.com/p/markupsafe/                                           | https:/            |
| matplotlib                       | https://matplotlib.org                                                              | https:/            |
| matplotlib-base                  | https://matplotlib.org                                                              | https:/            |
| matplotlib-inline                | https://github.com/ipython/matplotlib-inline                                        | https:/            |
| mda-xdrlib                       | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/            |
| mdtraj                           | https://www.mdtraj.org/                                                             | https:/            |
| mdurl                            | Orion Floes                                                                         | https:/            |
| menuinst                         | <b>Orion Floes</b>                                                                  | https:/            |
|                                  | https://github.com/imdario/mergo                                                    |                    |
| mergo                            |                                                                                     | https:/            |
| mistune                          | https://github.com/lepture/mistune                                                  | https:/            |
| mkl                              | https://github.com/rust-math/intel-mkl-src                                          | https:/            |
| mkl-fft                          | https://github.com/IntelPython/mkl_fft                                              | https:/            |
| Name of Project                  | Website                                                                             | License            |
| mkl-random                       | https://github.com/IntelPython/mkl_random                                           | https:/            |
| mkl-service                      | https://github.com/IntelPython/mkl-service                                          | https:/            |
| ml-dtypes                        | <b>Orion Floes</b>                                                                  | https:/            |
| molecupy                         | https://molecupy.readthedocs.io/en/latest/                                          | https:/            |
| moment                           | https://github.com/moment/moment                                                    | https:/            |
| moment-precise-range-plugin      | https://github.com/codebox/moment-precise-range                                     | https:/            |
| more-itertools                   | https://github.com/more-itertools/more-itertools                                    | https:/            |
| mpiplus                          | https://github.com/choderalab/mpiplus                                               | https:/            |
| mpmath                           | http://mpmath.org/                                                                  | https:/            |
| mrcfile                          | https://github.com/ccpem/mrcfile                                                    | https:/            |
| msgpack                          | https://msgpack.org/                                                                | https:/            |
| multidict                        | https://github.com/aio-libs/multidict                                               | https:/            |
| multierr                         | https://go.uber.org/multierr                                                        | https:/            |
| multiprocess                     | https://github.com/uqfoundation/multiprocess                                        | https:/            |
| munkres                          | https://software.clapper.org/munkres/                                               | https:/            |
| myesui uuid                      | https://github.com/myesui/uuid                                                      | https:/            |
| namex                            | <b>Orion Floes</b>                                                                  | https:/            |
| nbclassic                        | http://jupyter.org                                                                  | https:/            |
| nbclient                         | https://jupyter.org                                                                 | https:/            |
| nbconvert                        | https://jupyter.org                                                                 | https:/            |
| nbformat                         | http://jupyter.org                                                                  | https:/            |
| ncurses                          | https://invisible-island.net/ncurses/                                               | https:/            |
| nest-asyncio                     | https://github.com/erdewit/nest_asyncio                                             | https:/            |
| netcdf-fortran                   | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/            |
| netCDF4                          | http://github.com/Unidata/netcdf4-python                                            | https:/            |
| nettle                           | https://git.lysator.liu.se/nettle/nettle                                            | https:/            |
| networkx                         | https://networkx.org                                                                | https:/            |
| nfpm                             | https://github.com/goreleaser/nfpm                                                  | https:/            |
| ng-tags-input                    | https://github.com/mbenford/ngTagsInput                                             | https:/            |
| ng-toast                         | https://github.com/tameraydin/ngToast                                               | https:/            |
| ngdraggable                      | https://github.com/fatlinesofcode/ngDraggable                                       | https:/            |
| ngVue                            | https://github.com/ngVue/ngVue                                                      | https:/            |
| nlopt                            | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/            |
| nodejs                           | https://nodejs.org/en/                                                              | https:/            |
| nomkl                            | https://github.com/conda-forge/nomkl-feedstock                                      | https:/            |
| notebook                         | http://jupyter.org                                                                  | https:/            |
| notebook-shim                    | https://github.com/jupyter/notebook_shim                                            | https:/            |
| notebook_shim                    | http://jupyter.org                                                                  | https:/            |
| numba                            | https://numba.pydata.org                                                            | https:/            |
| numcpus                          | https://github.com/tklauser/numcpus                                                 | https:/            |
| numexpr                          | https://github.com/pydata/numexpr                                                   | https:/            |
| numpy                            | https://numpy.org                                                                   | https:/            |
| numpy-base                       | https://numpy.org                                                                   | https:/            |
| numpydoc                         | https://numpydoc.readthedocs.io/en/latest/index.html                                | https:/            |
| nvidia-cublas-cu11               | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cublas-cu12               | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-cupti-cu11           | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-cupti-cu12           | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| nvidia-cuda-nvrtc-cu11           | https://developer.nvidia.com/cuda-zone                                              | https:/            |
| Name of Project                  | Website                                                                             |                    |
| nvidia-cuda-nvrtc-cu12           | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cuda-runtime-cu11         | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cuda-runtime-cu12         | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cudnn-cu11                | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cudnn-cu12                | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cufft-cu11                | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cufft-cu12                | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-curand-cu11               | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-curand-cu12               | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusolver-cu11             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusolver-cu12             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusparse-cu11             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-cusparse-cu12             | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nccl-cu11                 | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nccl-cu12                 | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nvjitlink-cu12            | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nvtx-cu11                 | https://developer.nvidia.com/cuda-zone                                              |                    |
| nvidia-nvtx-cu12                 | https://developer.nvidia.com/cuda-zone                                              |                    |
| Oat++                            | https://oatpp.io/                                                                   |                    |
| oauthlib                         | https://github.com/oauthlib/oauthlib                                                |                    |
| ocl-icd                          | https://github.com/OCL-dev/ocl-icd                                                  |                    |
| ocl-icd-system                   | https://github.com/conda-forge/ocl-icd-system-feedstock                             |                    |
| olefile                          | https://www.decalage.info/python/olefileio                                          |                    |
| OmegaFold                        | https://github.com/HeliXonProtein/OmegaFold/tree/main                               |                    |
| omnicanvas                       | https://omnicanvas.readthedocs.io/en/latest/                                        |                    |
| OpenFF                           | https://openforcefield.org/                                                         |                    |
| openff-amber-ff-ports            | https://github.com/openforcefield/openff-amber-ff-ports                             |                    |
| openff-forcefields               | https://openforcefield.org                                                          |                    |
| openff-interchange               | https://github.com/openforcefield/openff-interchange                                |                    |
| openff-models                    | https://github.com/openforcefield/openff-models                                     |                    |
| openff-toolkit                   | https://openforcefield.org                                                          |                    |
| openff-toolkit-base              | https://openforcefield.org                                                          |                    |
| openff-units                     | https://github.com/openforcefield/openff-units                                      |                    |
| openff-utilities                 | https://github.com/openforcefield/openff-utilities                                  |                    |
| openjpeg                         | https://github.com/uclouvain/openjpeg                                               |                    |
| openldap                         | https://www.openldap.org/software/repo.html                                         |                    |
| OpenMM                           | https://openmm.org                                                                  |                    |
| openmmtools                      | https://github.com/choderalab/openmmtools                                           |                    |
| openmoltools                     | https://github.com/choderalab/openmoltools                                          |                    |
| openpyxl                         | https://openpyxl.readthedocs.io/en/stable/                                          |                    |
| openssl                          | https://www.openssl.org                                                             |                    |
| opt-einsum                       | https://github.com/dgasmith/opt_einsum                                              |                    |
| OptKing                          | https://github.com/psi-rking/optking                                                |                    |
| oscrypto                         | https://github.com/wbond/oscrypto                                                   |                    |
| overrides                        | https://github.com/mkorpela/overrides                                               |                    |
| packaging                        | https://github.com/pypa/packaging                                                   |                    |
| packmol                          | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               |                    |
| pandas                           | https://pandas.pydata.org                                                           |                    |
| pandocfilters                    | http://github.com/jgm/pandocfilters                                                 |                    |
|                                  |                                                                                     | Ъ                  |
| Name of Project                  | Website                                                                             | Licen              |
| panedr                           | https://github.com/MDAnalysis/panedr                                                | https:/            |
| pango                            | https://pango.gnome.org                                                             | https:/            |
| ParmEd                           | https://parmed.github.io/ParmEd/html/index.html                                     | https:/            |
| parser                           | https://github.com/typescript-eslint/typescript-eslint                              | https:/            |
| parso                            | https://parso.readthedocs.io/en/latest/                                             | https:/            |
| pathos                           | https://github.com/uqfoundation/pathos                                              | https:/            |
| patsy                            | https://patsy.readthedocs.io/en/latest/                                             | https:/            |
| pbkdf2                           | https://golang.org/x/crypto/pbkdf2                                                  | https:/            |
| pbr                              | https://docs.openstack.org/pbr/latest/                                              | https:/            |
| pcmsolver                        | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/            |
| pcre                             | https://www.pcre.org                                                                | https:/            |
| pcre2                            | https://www.pcre.org                                                                | https:/            |
| pdb4amber                        | https://github.com/Amber-MD/pdb4amber                                               | https:/            |
| pdbfixer                         | https://github.com/openmm/pdbfixer                                                  | https:/            |
| pexpect                          | https://pexpect.readthedocs.io/                                                     | https:/            |
| pgconn                           | https://github.com/jackc/pgconn                                                     | https:/            |
| pgio                             | https://github.com/jackc/pgio                                                       | https:/            |
| pgpassfile                       | https://github.com/jackc/pgpassfile                                                 | https:/            |
| pgproto3                         | https://github.com/jackc/pgproto3/v2                                                | https:/            |
| pgtype                           | https://github.com/jackc/pgtype                                                     | https:/            |
| pgx                              | https://github.com/jackc/pgx/v4                                                     | https:/            |
| phonopy                          | https://github.com/phonopy/phono3py                                                 | https:/            |
| pickleshare                      | https://github.com/pickleshare/pickleshare                                          | https:/            |
| Pillow                           | https://python-pillow.org                                                           | https:/            |
| Pint                             | https://pint.readthedocs.io/en/stable/                                              | https:/            |
| pip                              | https://pip.pypa.io/                                                                | https:/            |
| pip-licenses                     | https://github.com/raimon49/pip-licenses                                            | https:/            |
| pixman                           | https://pixman.org                                                                  | https:/            |
| pkginfo                          | https://launchpad.net/pkginfo                                                       | https:/            |
| platformdirs                     | https://github.com/platformdirs/platformdirs                                        | https:/            |
| plotly                           | https://plotly.com/python/                                                          | https:/            |
| plotly-orca                      | https://github.com/plotly/orca                                                      | https:/            |
| plotly.js                        | https://github.com/plotly/plotly.js                                                 | https:/            |
| pluggy                           | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/            |
| pooch                            | https://github.com/fatiando/pooch                                                   | https:/            |
| pox                              | https://github.com/uqfoundation/pox                                                 | https:/            |
| ppft                             | https://github.com/uqfoundation/ppft                                                | https:/            |
| pq                               | https://github.com/lib/pq                                                           | https:/            |
| ProDy                            | http://www.csb.pitt.edu/ProDy                                                       | https:/            |
| prometheus-client                | https://github.com/prometheus/client_python                                         | https:/            |
| prompt-toolkit                   | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/            |
| protobuf                         | https://google.golang.org/protobuf                                                  | https:/            |
| psi4                             | https://psicode.org                                                                 | https:/            |
| psutil                           | https://psutil.readthedocs.io/en/latest/                                            | https:/            |
| psycopg2                         | https://psycopg.org/                                                                | https:/            |
| PTable                           | https://github.com/kxxoling/PTable                                                  | https:/            |
| pthread-stubs                    | https://xcb.freedesktop.org                                                         | https:/            |
| ptyprocess                       | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/            |
| pure-eval                        | http://github.com/alexmojaki/pure_eval                                              | http://            |
|                                  |                                                                                     |                    |
|                                  |                                                                                     | J.                 |
| Name of Project                  | Website                                                                             | Licen              |
| py                               | https://py.readthedocs.io/en/latest/                                                | https:/            |
| py-cpuinfo                       | https://github.com/workhorsy/py-cpuinfo                                             | https:/            |
| pyasn1                           | https://github.com/etingof/pyasn1                                                   | https:/            |
| pyasn1-modules                   | https://github.com/etingof/pyasn1-modules                                           | https:/            |
| pybind11-abi                     | https://github.com/pybind/pybind11                                                  | https:/            |
| pycairo                          | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/            |
| pycosat                          | https://github.com/conda/pycosat                                                    | https:/            |
| pycparser                        | https://github.com/eliben/pycparser                                                 | https:/            |
| pydantic                         | https://pydantic-docs.helpmanual.io                                                 | https:/            |
| pydantic-core                    | https://github.com/pydantic/pydantic-core                                           | https:/            |
| pyedr                            | https://github.com/MDAnalysis/panedr                                                | https:/            |
| pyEMMA                           | http://github.com/markovmodel/PyEMMA                                                | https:/            |
| Pygments                         | https://pygments.org                                                                | https:/            |
| pygraphviz                       | https://pygraphviz.github.io                                                        | https:/            |
| pygtop                           | https://pygtop.readthedocs.io/en/latest/                                            | https:/            |
| pyHanko                          | https://github.com/MatthiasValvekens/pyHanko                                        | https:/            |
| pyhanko-certvalidator            | https://github.com/MatthiasValvekens/certvalidator                                  | https:/            |
| PyJWT                            | https://github.com/jpadilla/pyjwt                                                   | https:/            |
| pymbar                           | https://pymbar.org                                                                  | https:/            |
| pyOpenSSL                        | https://pyopenssl.org/                                                              | https:/            |
| pyparsing                        | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/            |
| PyPDF3                           | https://github.com/sfneal/PyPDF3                                                    | https:/            |
| pyrsistent                       | http://github.com/tobgu/pyrsistent/                                                 | https:/            |
| pysam                            | https://github.com/pysam-developers/pysam                                           | https:/            |
| PySocks                          | https://github.com/Anorov/PySocks                                                   | https:/            |
| pytables                         | https://www.pytables.org                                                            | https:/            |
| python                           | https://www.python.org/                                                             | https:/            |
| python-bidi                      | https://github.com/MeirKriheli/python-bidi                                          | https:/            |
| python-constraint                | https://github.com/python-constraint/python-constraint                              | https:/            |
| python-dateutil                  | https://dateutil.readthedocs.io                                                     | https:/            |
| python-json-logger               | http://github.com/madzak/python-json-logger                                         | https:/            |
| python-Idap                      | https://www.python-ldap.org/                                                        | https:/            |
| python3-saml                     | https://github.com/onelogin/python3-saml                                            | https:/            |
| python_abi                       | https://github.com/conda-forge/python_abi-feedstock                                 | https:/            |
| pytz                             | https://pythonhosted.org/pytz                                                       | https:/            |
| pytz-deprecation-shim            | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/            |
| PyWavelets                       | https://github.com/PyWavelets/pywt                                                  | https:/            |
| <b>PyYAML</b>                    | https://pyyaml.org/                                                                 | https:/            |
| pyyml                            | No longer available                                                                 | No lot             |
| pyzmq                            | https://pyzmq.readthedocs.io/en/latest/                                             | https:/            |
| qcelemental                      | https://github.com/MolSSI/QCElemental                                               | https:/            |
| qcengine                         | https://github.com/MolSSI/QCEngine                                                  | https:/            |
| qrcode                           | https://github.com/lincolnloop/python-qrcode                                        | https:/            |
| ramda                            | https://github.com/ramda/ramda                                                      | https:/            |
| rapidjson                        | https://rapidjson.org/                                                              | https:/            |
| rdkit                            | https://www.rdkit.org                                                               | https:/            |
| re2                              | https://github.com/google/re2                                                       | https:/            |
| readme-renderer                  | https://github.com/pypa/readme_renderer                                             | https:/            |
| redis-py                         | https://github.com/andymccurdy/redis-py                                             | https:/            |
|                                  |                                                                                     |                    |
| Name of Project                  | Website                                                                             | License            |
| referencing                      | https://github.com/python-jsonschema/referencing                                    | https:/            |
| regex                            | https://github.com/mrabarnett/mrab-regex                                            | https:/            |
| reportlab                        | https://www.reportlab.com                                                           | https:/            |
| reproc                           | https://github.com/DaanDeMeyer/reproc                                               | https:/            |
| reproc-cpp                       | https://github.com/DaanDeMeyer/reproc                                               | https:/            |
| requests                         | https://requests.readthedocs.io                                                     | https:/            |
| requests-oauthlib                | https://github.com/requests/requests-oauthlib                                       | https:/            |
| requests-toolbelt                | https://toolbelt.readthedocs.org                                                    | https:/            |
| resumable                        | https://github.com/stevvooe/resumable                                               | https:/            |
| retrying                         | https://github.com/rholder/retrying                                                 | https:/            |
| rfc3339-validator                | https://github.com/naimetti/rfc3339-validator                                       | https:/            |
| rfc3986                          | https://rfc3986.readthedocs.io/en/latest/                                           | https:/            |
| rfc3986-validator                | https://github.com/naimetti/rfc3986-validator                                       | https:/            |
| rich                             | https://github.com/Textualize/rich                                                  | Orion Floes        |
| rpds-py                          | https://github.com/crate-py/rpds                                                    | https:/            |
| rpmpack                          | https://github.com/google/rpmpack                                                   | https:/            |
| rsa                              | https://stuvel.eu/rsa                                                               | https:/            |
| ruamel-yaml                      | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/            |
| ruamel.yaml.clib                 | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/            |
| s3transfer                       | https://github.com/boto/s3transfer                                                  | https:/            |
| sasl                             | https://mellium.im/sasl                                                             | https:/            |
| scikit-gstat                     | https://mmaelicke.github.io/scikit-gstat/                                           | https:/            |
| scikit-image                     | https://scikit-image.org                                                            | https:/            |
| scikit-learn                     | https://scikit-learn.org/stable/                                                    | https:/            |
| scikit-learn-extra               | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/            |
| scipy                            | https://scipy.org                                                                   | https:/            |
| seaborn                          | https://seaborn.pydata.org                                                          | https:/            |
| seaborn-base                     | https://seaborn.pydata.org                                                          | https:/            |
| semver                           | https://github.com/Masterminds/semver/v3                                            | https:/            |
| Send2Trash                       | https://github.com/arsenetar/send2trash                                             | https:/            |
| setuptools                       | https://github.com/pypa/setuptools                                                  | https:/            |
| setuptools-scm                   | https://github.com/pypa/setuptools_scm/                                             | https:/            |
| sh                               | https://github.com/amoffat/sh                                                       | https:/            |
| shellingham                      | https://github.com/sarugaku/shellingham                                             | https:/            |
| simint                           | https://www.bennyp.org/research/simint/                                             | https:/            |
| six                              | https://github.com/benjaminp/six                                                    | https:/            |
| smirnoff99frosst                 | https://github.com/openforcefield/smirnoff99frosst                                  | https:/            |
| snappy                           | https://github.com/google/snappy                                                    | https:/            |
| sniffio                          | https://github.com/python-trio/sniffio                                              | https:/            |
| snowballstemmer                  | https://github.com/snowballstem/snowball                                            | https:/            |
| soupsieve                        | https://github.com/facelessuser/soupsieve                                           | https:/            |
| spglib                           | https://github.com/spglib/spglib                                                    | Orion Floes        |
| sphinx                           | https://github.com/sphinx-doc/sphinx                                                | https:/            |
| sphinxcontrib-applehelp          | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/            |
| sphinxcontrib-devhelp            | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/            |
| sphinxcontrib-htmlhelp           | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/            |
| sphinxcontrib-jsmath             | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/            |
| sphinxcontrib-qthelp             | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/            |
| sphinxcontrib-serializinghtml    | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/            |
|                                  |                                                                                     | T                  |
| Name of Project                  | Website                                                                             | Licen              |
| SQLAlchemy                       | https://www.sqlalchemy.org                                                          | https:/            |
| sqlite                           | https://sqlite.org/index.html                                                       | https:/            |
| sqlparse                         | https://github.com/andialbrecht/sqlparse                                            | https:/            |
| stack-data                       | http://github.com/alexmojaki/stack_data                                             | https:/            |
| starfile                         | https://github.com/alisterburt/starfile                                             | https:/            |
| statsmodels                      | https://github.com/statsmodels/statsmodels                                          | https:/            |
| structlog                        | https://www.structlog.org/                                                          | https:/            |
| svglib                           | https://github.com/deeplook/svglib                                                  | https:/            |
| sympy                            | https://sympy.org                                                                   | https:/            |
| tables                           | https://www.pytables.org/                                                           | https:/            |
| tabulate                         | https://github.com/astanin/python-tabulate                                          | https:/            |
| tbb                              | https://github.com/oneapi-src/oneTBB                                                | https:/            |
| tenacity                         | https://github.com/jd/tenacity                                                      | https:/            |
| tensorboard                      | https://github.com/tensorflow/tensorboard                                           | https:/            |
| tensorboard-data-server          | https://github.com/tensorflow/tensorboard                                           | https:/            |
| tensorboard-plugin-wit           | https://github.com/pair-code/what-if-tool                                           | https:/            |
| tensorflow                       | https://github.com/tensorflow/tensorflow                                            | https:/            |
| tensorflow-estimator             | https://github.com/tensorflow/estimator                                             | https:/            |
| tensorflow-io-gcs-filesystem     | <b>Orion Floes</b>                                                                  | https:/            |
| tensorflow-probability           | https://github.com/tensorflow/probability                                           | https:/            |
| termcolor                        | https://github.com/hugovk/termcolor                                                 | https:/            |
| terminado                        | https://github.com/jupyter/terminado                                                | https:/            |
| testpath                         | https://github.com/jupyter/testpath                                                 | https:/            |
| textangular                      | https://github.com/fraywing/textAngular                                             | https:/            |
| tf_keras                         | <b>Orion Floes</b>                                                                  | https:/            |
| threadpoolctl                    | https://github.com/joblib/threadpoolctl                                             | https:/            |
| three                            | https://github.com/mrdoob/three.js                                                  | https:/            |
| tifffile                         | https://github.com/cgohlke/tifffile/                                                | https:/            |
| tinycss2                         | https://github.com/Kozea/tinycss2/                                                  | https:/            |
| tinyxml2                         | https://github.com/leethomason/tinyxml2                                             | https:/            |
| tk                               | https://www.tcl.tk/                                                                 | https:/            |
| toml                             | https://github.com/toml-lang/toml                                                   | https:/            |
| tomli                            | https://github.com/hukkin/tomli                                                     | https:/            |
| toolz                            | https://github.com/pytoolz/toolz                                                    | https:/            |
| torch                            | https://pytorch.org/                                                                | https:/            |
| tornado                          | https://www.tornadoweb.org                                                          | https:/            |
| tqdm                             | https://github.com/tqdm/tqdm                                                        | https:/            |
|                                  | https://github.com/gear-genomics/tracy                                              | https:/            |
| tracy<br>traitlets               | https://github.com/ipython/traitlets                                                |                    |
|                                  | https://github.com/openai/triton/                                                   | https:/            |
| triton                           |                                                                                     | https:/            |
| truststore                       | <b>Orion Floes</b>                                                                  | https:/            |
| ts-jest                          | https://github.com/kulshekhar/ts-jest                                               | https:/            |
| ts-loader                        | https://github.com/TypeStrong/ts-loader                                             | https:/            |
| twine                            | https://github.com/pypa/twine                                                       | https:/            |
| twinj uuid                       | https://github.com/twinj/uuid                                                       | https:/            |
| types                            | https://github.com/babel/babel                                                      | https:/            |
| typescript                       | https://github.com/Microsoft/TypeScript                                             | https:/            |
| typing_extensions                | https://github.com/python/typing                                                    | https:/            |
| tzdata                           | https://github.com/python/tzdata                                                    | https:/            |
| Name of Project                  | Website                                                                             | License            |
| tzlocal                          | https://github.com/regebro/tzlocal                                                  |                    |
| umi-tools                        | https://github.com/CGATOxford/UMI-tools                                             |                    |
| unicodedata2                     | https://github.com/fonttools/unicodedata2                                           |                    |
| uritools                         | https://github.com/tkem/uritools/                                                   |                    |
| urllib3                          | https://urllib3.readthedocs.io/                                                     |                    |
| vine                             | https://github.com/celery/vine                                                      |                    |
| vue                              | https://github.com/vuejs/vue                                                        |                    |
| wcwidth                          | https://github.com/jquast/wcwidth                                                   |                    |
| webencodings                     | https://github.com/gsnedders/python-webencodings                                    |                    |
| websocket-client                 | https://github.com/websocket-client/websocket-client.git                            |                    |
| Werkzeug                         | https://palletsprojects.com/p/werkzeug/                                             |                    |
| westpa                           | Orion Floes                                                                         |                    |
| wheel                            | https://github.com/pypa/wheel                                                       |                    |
| widgetsnbextension               | https://github.com/jupyter-widgets/ipywidgets#readme                                |                    |
| wrapt                            | https://github.com/GrahamDumpleton/wrapt                                            |                    |
| wsutil                           | https://github.com/yhat/wsutil                                                      |                    |
| x/lint                           | https://golang.org/x/lint                                                           |                    |
| x/mod                            | https://golang.org/x/mod/semver                                                     |                    |
| x/net                            | https://golang.org/x/net                                                            |                    |
| x/oauth2                         | https://golang.org/x/oauth2                                                         |                    |
| x/sys                            | https://golang.org/x/sys                                                            |                    |
| x/text                           | https://golang.org/x/text                                                           |                    |
| x/tools                          | https://golang.org/x/tools                                                          |                    |
| x/xerrors                        | https://golang.org/x/xerrors                                                        |                    |
| xhtml2pdf                        | http://github.com/xhtml2pdf/xhtml2pdf                                               |                    |
| xlrd                             | https://github.com/python-excel/xlrd                                                |                    |
| xmlsec                           | https://github.com/mehcode/python-xmlsec                                            |                    |
| xmltodict                        | https://github.com/martinblech/xmltodict                                            |                    |
| xorg-kbproto                     | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   |                    |
| xorg-libice                      | https://gitlab.freedesktop.org/xorg/lib/libice                                      |                    |
| xorg-libsm                       | https://gitlab.freedesktop.org/xorg/lib/libsm                                       |                    |
| xorg-libx11                      | https://gitlab.freedesktop.org/xorg/lib/libx11                                      |                    |
| xorg-libxau                      | https://gitlab.freedesktop.org/xorg/lib/libxau                                      |                    |
| xorg-libxdmcp                    | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    |                    |
| xorg-libxext                     | https://gitlab.freedesktop.org/xorg/lib/libxext                                     |                    |
| xorg-libxrender                  | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  |                    |
| xorg-libxt                       | https://gitlab.freedesktop.org/xorg/lib/libxt                                       |                    |
| xorg-renderproto                 | https://gitlab.freedesktop.org/xorg/proto/renderproto                               |                    |
| xorg-xextproto                   | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 |                    |
| xorg-xproto                      | https://gitlab.freedesktop.org/xorg/proto/xproto                                    |                    |
| xxhash                           | https://github.com/cespare/xxhash/v2                                                |                    |
| xz                               | https://github.com/ulikunitz/xz                                                     |                    |
| yaml                             | https://pyyaml.org/                                                                 |                    |
| yaml-cpp                         | https://github.com/jbeder/yaml-cpp                                                  |                    |
| yaml.v2                          | https://gopkg.in/yaml.v2                                                            |                    |
| yaml.v3                          | https://gopkg.in/yaml.v3                                                            |                    |
| yarl                             | https://github.com/aio-libs/yarl/                                                   |                    |
| yaspin                           | https://github.com/pavdmyt/yaspin                                                   |                    |
| yfiles                           | https://www.yworks.com/products/yfiles                                              |                    |
| Name of Project                  | Website                                                                             | License            |
| yml                              | https://pypi.org/project/yml/                                                       | N/A                |
| zap                              | https://go.uber.org/zap                                                             | https:/            |
| zipp                             | https://github.com/jaraco/zipp                                                      | https:             |
| zlib                             | https://zlib.net/                                                                   | https:/            |
| zstandard                        | https://github.com/indygreg/python-zstandard                                        | https:/            |
| zstd                             | https://facebook.github.io/zstd/                                                    | https:             |
| _libgcc_mutex                    | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:/            |
| _openmp_mutex                    | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:/            |

# **12.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses GNU Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

# **12.1.1 GCC RUNTIME LIBRARY EXCEPTION**

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,..  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,.. →use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

## **12.1.2 GNU GENERAL PUBLIC LICENSE**

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

# $\mathsf{A}$

AddMol OEFastROCS:: OEShapeDatabase, 57 asisstartsexample.py Example Code, 46

# C

ClearCutoff OEFastROCS:: OEShapeDatabaseOptions, 63 ClearTracer OEFastROCS:: OEShapeDatabaseOptions, 63 ClearUserStarts OEFastROCS:: OEShapeDatabaseOptions,  $64$ Constructors OEFastROCS:: OEDBTracer, 53 OEFastROCS:: OEFastROCSHistogram, 56 OEFastROCS:: OEShapeDatabase, 57 OEFastROCS:: OEShapeDatabaseOptions, 63 OEFastROCS:: OEShapeDatabaseScore, 78

# E

Example Code asisstartsexample.py, 46 inertialatheavyatomstartsexample.py, 40 shapedatabaseclient.py, 30 shapedatabaseserver.py, 17 simplefastrocssearch.py, 36 simpleprepscript.py.50 userinertialstartsexample.py, 43 ExtractTransform OEFastROCS:: OEShapeDatabaseScore, 83

# G

GetColorForceFieldType OEFastROCS:: OEShapeDatabase, 58 OEFastROCS:: OEShapeDatabaseOptions, 64

GetColorGridSpacing OEFastROCS:: OEShapeDatabase, 58 GetColorOptimization OEFastROCS:: OEShapeDatabaseOptions, 64 GetColorScore OEFastROCS:: OEShapeDatabaseScore, 79 GetColorScoreScale OEFastROCS:: OEShapeDatabaseOptions, 77 GetColorTanimoto OEFastROCS:: OEShapeDatabaseScore, 79 GetColorTversky OEFastROCS:: OEShapeDatabaseScore, 80 GetConfIdx OEFastROCS:: OEShapeDatabaseScore, 80 GetCounts OEFastROCS:: OEDBTracer, 53 GetCutoff OEFastROCS:: OEShapeDatabaseOptions, 64 GetCutoffGT OEFastROCS:: OEShapeDatabaseOptions, 65 GetCutoffLT OEFastROCS:: OEShapeDatabaseOptions, 65 GetDatabaseType OEFastROCS:: OEShapeDatabase, 58 GetFastROCSMode OEFastROCS:: OEShapeDatabaseOptions, 65 GetHistogram OEFastROCS:: OEDBTracer, 53 OEFastROCS:: OEFastROCSHistogram, 56 GetInitialOrientation OEFastROCS:: OEShapeDatabaseOptions, 65 GetLimit OEFastROCS:: OEShapeDatabaseOptions, 66 GetMaxConfs

OEFastROCS:: OEShapeDatabaseOptions, 66 GetMaxNumDevices OEFastROCS:: OEShapeDatabase, 58 GetMaxOptIterations OEFastROCS:: OEShapeDatabase, 59 GetMaxOverlays OEFastROCS:: OEShapeDatabaseOptions, 66 GetMaxRandomTranslation OEFastROCS:: OEShapeDatabaseOptions, -66 GetMolIdx OEFastROCS:: OEShapeDatabaseScore, 80 GetNumBins OEFastROCS:: OEDBTracer, 54 OEFastROCS:: OEDBTracerBase, 55 OEFastROCS:: OEFastROCSHistogram, 56 GetNumColorAtomStarts OEFastROCS:: OEShapeDatabaseOptions, 67 GetNumDevices OEFastROCS:: OEShapeDatabase, 59 GetNumHeavyAtomStarts OEFastROCS:: OEShapeDatabaseOptions, 67 GetNumInertialStarts OEFastROCS:: OEShapeDatabaseOptions, 67 GetNumOpenThreads OEFastROCS:: OEShapeDatabase, 59 GetNumRandomStarts OEFastROCS:: OEShapeDatabaseOptions, 68 GetNumStarts OEFastROCS:: OEShapeDatabaseOptions, 67 GetNumUserStarts OEFastROCS:: OEShapeDatabaseOptions, 68 GetQuat OEFastROCS:: OEShapeDatabaseScore, 80 GetRandomSeed OEFastROCS:: OEShapeDatabaseOptions, 68 GetRotMatrix OEFastROCS:: OEShapeDatabaseScore, 81 GetScore OEFastROCS:: OEShapeDatabaseScore, 81 GetScores OEFastROCS:: OEShapeDatabase, 59 GetScoreType OEFastROCS:: OEShapeDatabaseOptions, 69

GetShapeGridSpacing OEFastROCS:: OEShapeDatabase, 60 GetShapeScore OEFastROCS:: OEShapeDatabaseScore, 81 GetShapeScoreScale OEFastROCS:: OEShapeDatabaseOptions, 77 GetShapeTanimoto OEFastROCS:: OEShapeDatabaseScore, 81 GetShapeTversky OEFastROCS:: OEShapeDatabaseScore, 82 GetSimFunc OEFastROCS:: OEShapeDatabaseOptions, 69 OEFastROCS:: OEShapeDatabaseScore, 82 GetSortedScores OEFastROCS:: OEShapeDatabase, 60 GetTanimotoCombo OEFastROCS:: OEShapeDatabaseScore, 82 GetTotal OEFastROCS:: OEDBTracer, 54 GetTracer OEFastROCS:: OEShapeDatabaseOptions, 69 GetTranslation OEFastROCS:: OEShapeDatabaseScore, 82 GetTverskyAlpha OEFastROCS:: OEShapeDatabaseOptions, 69 GetTverskyBeta OEFastROCS:: OEShapeDatabaseOptions, 69 GetTverskyCombo OEFastROCS:: OEShapeDatabaseScore, 83 GetUserStarts OEFastROCS:: OEShapeDatabaseOptions, 70

# H

```
HasCutoff
   OEFastROCS:: OEShapeDatabaseOptions,
       70
HasCutoffGT
   OEFastROCS:: OEShapeDatabaseOptions,
       70
HasCutoffLT
   OEFastROCS:: OEShapeDatabaseOptions,
       71
I
```

inertialatheavyatomstartsexample.py Example Code, 40

OEFastROCS:: OEFastROCSReturnCode, 86

85

87

OEFastROCS:: OEFastROCSOrientation:: UserInertialStal

OEFastROCS:: OEFastROCSReturnCode:: InitializationEr

# N

NumConfs OEFastROCS:: OEShapeDatabase, 61

# O

```
OEFastROCS:: OEFastROCSReturnCode:: InsufficientDrive
OEFastROCS:: OEDBTracer, 53
                                                   87
   Constructors, 53
                                            OEFastROCS:: OEFastROCSReturnCode:: NoDevice,
   GetCounts, 53
                                                   87
   GetHistogram, 53
                                            OEFastROCS:: OEFastROCSReturnCode:: NoDeviceDetected,
   GetNumBins, 54
                                                   87
   GetTotal, 54
                                            OEFastROCS:: OEFastROCSReturnCode:: NotPermitted,
   SetTotal, 54
                                                   87
   Update, 54
                                            OEFastROCS:: OEFastROCSReturnCode:: Success,
OEFastROCS:: OEDBTracerBase, 54
                                                   86
   GetNumBins.55
                                            OEFastROCS:: OEFastROCSReturnCode:: Unknown,
   SetTotal, 55
                                                   87
   Update, 55
                                            OEFastROCS:: OEIsDatabasePrepared. 93
OEFastROCS:: OEFastROCSCacheStuff, 91
                                            OEFastROCS:: OEPrepareFastROCSMol, 94
OEFastROCS:: OEFastROCSGetArch, 91
                                            OEFastROCS:: OESetCoordsToInertialFrame,
OEFastROCS:: OEFastROCSGetLicensee, 91
                                                   94
OEFastROCS:: OEFastROCSGetNumDevices, 91
                                            OEFastROCS:: OEShapeDatabase, 57
OEFastROCS:: OEFastROCSGetPlatform, 91
                                                AddMol, 57
OEFastROCS:: OEFastROCSGetRelease, 91
                                                Constructors. 57
OEFastROCS:: OEFastROCSGetSite, 92
                                                GetColorForceFieldType, 58
OEFastROCS:: OEFastROCSGetVersion, 92
                                                GetColorGridSpacing, 58
OEFastROCS:: OEFastROCSGPUStatus, 92
                                                GetDatabaseType, 58
OEFastROCS:: OEFastROCSHistogram, 55
                                                GetMaxNumDevices, 58
   Constructors, 56
                                                GetMaxOptIterations, 59
   GetHistogram, 56
                                                GetNumDevices, 59
   GetNumBins, 56
                                                GetNumOpenThreads, 59
   Update, 56
                                                GetScores, 59
OEFastROCS:: OEFastROCSIsGPUReady, 92
                                                GetShapeGridSpacing, 60
OEFastROCS:: OEFastROCSIsLicensed, 92
                                                GetSortedScores, 60
OEFastROCS:: OEFastROCSMode, 90
                                                NumConfs. 61
OEFastROCS:: OEFastROCSMode:: Default, 90
                                                Open, 61OEFastROCS:: OEFastROCSMode::FastROCS,
                                                PrintMemoryUsage, 61
       90
                                                SetColorGridSpacing, 61
OEFastROCS:: OEFastROCSMode:: ROCS, 90
                                                SetMaxOptIterations, 62
OEFastROCS:: OEFastROCSOrientation, 84
                                                SetNumDevices, 62
OEFastROCS:: OEFastROCSOrientation:: AsIs,
                                                SetNumOpenThreads, 62
       85
                                                SetShapeGridSpacing, 62
OEFastROCS:: OEFastROCSOrientation:: Defaul
                                            OEFastROCS::OEShapeDatabaseOptions, 62
       84
                                                ClearCutoff, 63
OEFastROCS:: OEFastROCSOrientation:: Inertial
                                                ClearTracer, 63
       84
ClearUserStarts, 64<br>OEFastROCS::OEFastROCSOrientation::InertialAtColorAtoms.
                                                Constructors, 63
       85
OEFastROCS::OEFastROCSOrientation::InertialAtHeavyAtoms.
                                                GetColorOptimization, 64
       85
                                                GetColorScoreScale, 77
OEFastROCS:: OEFastROCSOrientation:: Random,
                                                GetCutoff, 64
       86
                                                GetCutoffGT, 65
OEFastROCS:: OEFastROCSOrientation:: Subrocs,
                                                GetCutoffLT. 65
       86
                                                GetFastROCSMode, 65
```

GetInitialOrientation, 65 GetLimit. 66 GetMaxConfs, 66 GetMaxOverlays, 66 GetMaxRandomTranslation, 66 GetNumColorAtomStarts, 67 GetNumHeavyAtomStarts, 67 GetNumInertialStarts, 67 GetNumRandomStarts, 68 GetNumStarts, 67 GetNumUserStarts, 68 GetRandomSeed. 68 GetScoreType, 69 GetShapeScoreScale, 77 GetSimFunc. 69 GetTracer. 69 GetTverskyAlpha, 69 GetTverskyBeta, 69 GetUserStarts.70 HasCutoff, 70 HasCutoffGT, 70 HasCutoffLT, 71 operator=, 63 SetColorForceField, 71 SetColorForceFieldType, 71 SetColorOptimization, 71 SetColorScoreScale, 77 SetCutoff, 72 SetCutoffGT, 72 SetCutoffLT.72 SetFastROCSMode, 72 SetInitialOrientation, 73 SetLimit, 73 SetMaxConfs, 74 SetMaxOverlays, 74 SetMaxRandomTranslation, 74 SetNumInertialStarts, 75 SetNumRandomStarts, 73 SetRandomSeed, 75 SetScoreType, 75 SetShapeScoreScale, 77 SetSimFunc, 75 SetTracer, 76 SetTverskyCoeffs, 76 SetUserStarts, 76 OEFastROCS:: OEShapeDatabasePrep, 93 OEFastROCS:: OEShapeDatabaseScore, 77 Constructors, 78 ExtractTransform. 83 GetColorScore, 79 GetColorTanimoto, 79 GetColorTversky, 80 GetConfIdx, 80 GetMolIdx, 80

GetOuat, 80 GetRotMatrix, 81 GetScore, 81 GetShapeScore, 81 GetShapeTanimoto, 81 GetShapeTversky, 82 GetSimFunc. 82 GetTanimotoCombo, 82 GetTranslation. 82 GetTverskyCombo, 83 Transform, 83 OEFastROCS:: OEShapeDatabaseType, 87 OEFastROCS:: OEShapeDatabaseType:: Color, 88 OEFastROCS:: OEShapeDatabaseType:: Combo, 88 OEFastROCS:: OEShapeDatabaseType:: Default, 88 OEFastROCS:: OEShapeDatabaseType:: Shape, 88 OEFastROCS:: OEShapeDatabaseType:: Sitehopper, 88 OEFastROCS:: OEShapeSimFuncType, 88 OEFastROCS:: OEShapeSimFuncType:: Default, 89 OEFastROCS:: OEShapeSimFuncType:: Tanimoto, 89 OEFastROCS:: OEShapeSimFuncType::Tversky, 89 Open OEFastROCS:: OEShapeDatabase, 61 operator= OEFastROCS:: OEShapeDatabaseOptions, 63

# P

PrintMemoryUsage OEFastROCS:: OEShapeDatabase, 61

# S

SetColorForceField OEFastROCS:: OEShapeDatabaseOptions, 71 SetColorForceFieldType OEFastROCS:: OEShapeDatabaseOptions, 71 SetColorGridSpacing OEFastROCS:: OEShapeDatabase, 61 SetColorOptimization OEFastROCS:: OEShapeDatabaseOptions, 71 SetColorScoreScale OEFastROCS:: OEShapeDatabaseOptions, 77

SetCutoff OEFastROCS:: OEShapeDatabaseOptions,  $72$ SetCutoffGT OEFastROCS:: OEShapeDatabaseOptions, 72 SetCutoffLT OEFastROCS:: OEShapeDatabaseOptions, 72 SetFastROCSMode OEFastROCS:: OEShapeDatabaseOptions, 72 SetInitialOrientation OEFastROCS:: OEShapeDatabaseOptions,  $73$ SetLimit OEFastROCS:: OEShapeDatabaseOptions, 73 SetMaxConfs OEFastROCS:: OEShapeDatabaseOptions,  $74$ SetMaxOptIterations OEFastROCS:: OEShapeDatabase, 62 SetMaxOverlays OEFastROCS:: OEShapeDatabaseOptions,  $74$ SetMaxRandomTranslation OEFastROCS:: OEShapeDatabaseOptions, 74 SetNumDevices OEFastROCS:: OEShapeDatabase, 62 SetNumInertialStarts OEFastROCS:: OEShapeDatabaseOptions, 75 SetNumOpenThreads OEFastROCS:: OEShapeDatabase, 62 SetNumRandomStarts OEFastROCS:: OEShapeDatabaseOptions, 73 SetRandomSeed OEFastROCS:: OEShapeDatabaseOptions, 75 SetScoreType OEFastROCS:: OEShapeDatabaseOptions, 75 SetShapeGridSpacing OEFastROCS:: OEShapeDatabase, 62 SetShapeScoreScale OEFastROCS:: OEShapeDatabaseOptions, 77 SetSimFunc OEFastROCS:: OEShapeDatabaseOptions, 75 SetTotal

OEFastROCS:: OEDBTracer, 54 OEFastROCS:: OEDBTracerBase, 55 SetTracer OEFastROCS:: OEShapeDatabaseOptions, 76 SetTverskyCoeffs OEFastROCS:: OEShapeDatabaseOptions, 76 SetUserStarts OEFastROCS:: OEShapeDatabaseOptions, 76 shapedatabaseclient.py Example Code, 30 shapedatabaseserver.py Example Code, 17 ShapeDatabaseServer::GetBestOverlays, 96 ShapeDatabaseServer:: GetName, 96 ShapeDatabaseServer:: GetVersion, 97 ShapeDatabaseServer:: IsLoaded, 97 ShapeDatabaseServer:: OEThrowSetLevel, 97 ShapeDatabaseServer:: QueryHistogram, 97 ShapeDatabaseServer:: QueryResults, 98 ShapeDatabaseServer:: QueryStatus, 97 ShapeDatabaseServer::SetName, 98 ShapeDatabaseServer:: SubmitQuery, 98 simplefastrocssearch.py Example Code, 36 simpleprepscript.py Example Code, 50

# Т

Transform OEFastROCS:: OEShapeDatabaseScore, 83

# U

Update OEFastROCS:: OEDBTracer, 54 OEFastROCS:: OEDBTracerBase, 55 OEFastROCS:: OEFastROCSHistogram, 56 userinertialstartsexample.py Example Code, 43