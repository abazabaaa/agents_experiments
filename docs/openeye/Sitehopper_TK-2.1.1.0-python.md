![](_page_0_Picture_0.jpeg)

# **Sitehopper TK - Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

## **CONTENTS**

| 1      | Introduction                      | 3                                   |    |
|--------|-----------------------------------|-------------------------------------|----|
| 2      | GPU-Related Requirements          | 5                                   |    |
| 2.1    | Supported Platforms               | 5                                   |    |
| 2.2    | Supported GPUs                    | 5                                   |    |
| 2.3    | NVIDIA Drivers                    | 5                                   |    |
| 2.4    | Performance Tuning                | 6                                   |    |
| 3      | Examples                          | 7                                   |    |
| 3.1    | SiteHopper Search                 | 7                                   |    |
| 3.1.1  | Search a SiteHopper Database      | 7                                   |    |
| 3.2    | SiteHopper Database               | 8                                   |    |
| 3.2.1  | Creating a new Database           | 8                                   |    |
| 3.2.2  | Query database info               | 9                                   |    |
| 3.2.3  | Get an OEDesignUnit from database | 10                                  |    |
| 4      | Preliminary OESiteHopper API      | 13                                  |    |
| 4.1    | OESiteHopper Classes              | 13                                  |    |
| 4.1.1  | OESiteHopperDatabase              | 13                                  |    |
| 4.1.2  | OESiteHopperDatabaseOptions       | 15                                  |    |
| 4.1.3  | OESiteHopperPatchOptions          | 16                                  |    |
| 4.1.4  | OESiteHopperResults               | 19                                  |    |
| 4.1.5  | OESiteHopperScore                 | 21                                  |    |
| 4.1.6  | OESiteHopperSearch                | 23                                  |    |
| 4.1.7  | OESiteHopperSearchBase            | 24                                  |    |
| 4.1.8  | OESiteHopperSearchOptions         | 24                                  |    |
| 4.2    | OESiteHopper Constants            | 27                                  |    |
| 4.2.1  | OESiteHopperDatabaseMode          | 27                                  |    |
| 4.3    | OESiteHopper Functions            | 28                                  |    |
| 4.3.1  | OEAddPatchSurface                 | 28                                  |    |
| 4.3.2  | OEGetPatchSurface                 | 28                                  |    |
| 4.3.3  | OEHasPatchSurface                 | 28                                  |    |
| 4.3.4  | OEMakePatchFromDesignUnit         | 28                                  |    |
| 4.3.5  | OESetPatchSurface                 | 29                                  |    |
| 4.3.6  | OESetProteinSDData                | 29                                  |    |
| 4.3.7  | OESiteHopperGetArch               | 29                                  |    |
| 4.3.8  | OESiteHopperGetLicensee           | 29                                  |    |
| 4.3.9  | OESiteHopperGetPlatform           | 29                                  |    |
| 4.3.10 | OESiteHopperGetRelease            | 30                                  |    |
| 4.3.11 | OESiteHopperGetSite               | 30                                  |    |
|        |                                   | 4.3.12 OESiteHopperGetVersion       | 30 |
|        |                                   | 4.3.13 OESiteHopperIsGPUReady       | 30 |
|        |                                   | 4.3.14 OESiteHopperIsLicensed       | 30 |
|        |                                   |                                     |    |
| 5      |                                   | <b>Release History</b>              | 31 |
|        | 5.1                               | SiteHopper TK 2.1.1                 | 31 |
|        |                                   | 5.1.1 Minor bug fixes               | 31 |
|        | 5.2                               | SiteHopper TK 2.1.0                 | 31 |
|        |                                   | 5.2.1 New features                  | 31 |
|        | 5.3                               | Sitehopper TK 2.0.4                 | 31 |
|        | 5.4                               | Sitehopper TK 2.0.3                 | 31 |
|        | 5.5                               | Sitehopper TK 2.0.2                 | 31 |
|        | 5.6                               | Sitehopper TK 2.0.1                 | 32 |
|        |                                   | 5.6.1 Python-specific changes       | 32 |
|        | 5.7                               | SiteHopper TK 2.0.0                 | 32 |
| 6      |                                   | <b>Copyright and Trademarks</b>     | 33 |
| 7      |                                   | <b>Sample Code</b>                  | 35 |
| 8      | <b>Citation</b>                   |                                     | 37 |
|        | 8.1                               | Orion ® Floes                       | 37 |
|        | 8.2                               | Toolkits and Applications           | 37 |
|        | 8.3                               | OpenEye Web Services                | 39 |
| 9      |                                   | <b>Technology Licensing</b>         | 41 |
|        | 9.1                               | <b>GCC</b>                          | 56 |
|        |                                   | 9.1.1 GCC RUNTIME LIBRARY EXCEPTION | 56 |
|        |                                   | 9.1.2 GNU GENERAL PUBLIC LICENSE    | 58 |

Attention: Sitehopper TK is currently only available in C++ and Python.

### **CHAPTER**

## **INTRODUCTION**

The SiteHopper TK uses technology from the OpenEye Shape TK to compare protein binding sites using Shape and Color similarity.

There are two main classes in the toolkit. OESiteHopperDatabase can be used to search and prepare a set of OEDesignUnit for search. For each OEDesignUnit, OESiteHopperDatabase creates a "patch" molecule generated by placing shape atoms on the molecular surface of the binding site and color atoms on protein atoms near the binding site.

Once the database is created, the OESiteHopperSearch class can take a query OEDesignUnit and return a set of similar OEDesignUnit objects, each transformed based on the optimized overlap and scored using a combination of the Shape and Color Tanimoto calculated via the Shape TK.

If running on a Linux machine with a supported Nvidia GPU, the Search can use the GPU to do a fast pre-screen to speed up the search. See the GPU Prerequisites section for more info on GPU requirements.

### **CHAPTER**

## **GPU-RELATED REQUIREMENTS**

The following is required in order to use GPU-accelerated OpenEye toolkits and applications:

## **2.1 Supported Platforms**

CUDA-enabled OpenEye software is only available on supported Linux platforms. For supported Linux platforms see above and/or the Platform Support Page

## **2.2 Supported GPUs**

An NVIDIA Tesla, Quadro, or GeForce GPU with a **compute capability of 3.5** or higher is required on your system. For a comprehensive table of which GPUs fall into which compute capability category please refer to the CUDA wikipedia page.

## **2.3 NVIDIA Drivers**

- Minimum NVIDIA Driver version: 450.x.
- CUDA is not required to be installed.

We recommend driver 450.80.02 and we strongly advise manually downloading and installing the appropriate NVidia driver for your system as opposed to using a package manager.

To install, root privilege is required. Follow these steps:

- 1. Download the driver to the machine you are installing it on.
- 2. chmod  $+x$  the driver package to make it executable.
- 3. Ensure you have disabled X-server by killing any running sessions. Reboot may be required if X-server is still running after this step.

Warning: Disabling X-server requires different processes to be killed depending on your Linux distribution. See Nvidia installation guide for more details.

Warning: The NVidia kernel module can often conflict with the open source Nouveau display drivers depending on your specific Linux distribution. The NVidia documentation is a much more complete and up-to-date source for information on how to work around this issue. See Disabling Nouveau on the NVIDIA website.

4. Install the driver by sudo ./NVIDIA-Linux-x86\_64-450.80.02.run and follow the step-by-step installation instructions.

For more details on driver installations see the CUDA Installation Guide

Note: The output of the nvidia-smi command is extremely useful when debugging GPU issues. Please include the output from  $n$ vidia-smi in any request to support@eyesopen.com.

## **2.4 Performance Tuning**

To get the most performance out of an NVIDIA Graphics card, use the persistence daemon to switch persistence mode on across all cards on the system (root privilege required):

sudo nvidia-persistenced --user foo

This will automatically enable persistence mode after reboot.

For full instructions on persistence daemon see the Persistence daemon section of the NVIDIA docs.

### **CHAPTER**

## **THREE**

## **EXAMPLES**

## **3.1 SiteHopper Search**

### 3.1.1 Search a SiteHopper Database

#### Listing 1: Simple example to search a SiteHopper database

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
from openeye import oesitehopper
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
def main (argv) :
   if len(argv) != 4:
        oechem.OEThrow.Usage("%s <shdb> <query du> <hits oedu>" % argv[0])
   shdb = oesitehopper.OESiteHopperDatabase()
   if not shdb. Open (argv[1], oesitehopper. OESiteHopperDatabaseMode_SEARCH) :
        oechem. OEThrow. Error (f"unable to open \{argv[1]\}.")
        return 1
```

```
du = occhem. OEDesignUnit()
    if not oechem. OEReadDesignUnit (argv[2], du) :
        oechem. OEThrow. Error (f"unable to read OEDesignUnit from {argv[2] }")
    ofs = occhem.oeofstream()if not ofs.open(argv[3]):
        oechem. OEThrow. Fatal (f"unable to open {argv[3]} for writing hits.")
   oesitehopper.OEAddPatchSurface(du, shdb.GetOptions().GetPatchOptions())
   oechem.OEWriteDesignUnit(ofs, du)
   search = oesitehopper.OESiteHopperSearch(shdb)
   tracer = oechem. OEConsoleProgressTracer()
   opts = oesitehopper.OESiteHopperSearchOptions()
    opts.SetNormalizeAndRescore(True)
    opts.SetMaxHits(25)
    score: oesitehopper.OESiteHopperScore
    for score in search. Search (du, opts, tracer):
        print (f'' (score.GetRank() }, {score.GetTitle() }, {score.GetPatchScore() : .2f}")
        hit_du = score.GetDesignUnit()
        oesitehopper.OESetProteinSDData(hit_du, score)
        oechem.OEWriteDesignUnit(ofs, hit_du)
if name == " main ":
   sys.exit(main(sys.argy))
```

## **3.2 SiteHopper Database**

### 3.2.1 Creating a new Database

Listing 2: Simple example to create new SiteHopper database

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
(continues on next page)
```

```
from openeye import oechem
from openeye import oesitehopper
def main (argv) :
   if len(argv) != 3:
        oechem.OEThrow.Usage("%s <shdb file> <du directory>" % argv[0])
    shdb = oesitehopper.OESiteHopperDatabase()
    if not shdb. Open (argv[1], oesitehopper. OESiteHopperDatabaseMode_CREATE) :
        oechem. OEThrow. Error (f"unable to open {argv[1] }.")
        return 1
   tracer = oechem. OEConsoleProgressTracer()
    shdb.AddDirectory(argv[2], 0, tracer)
if _name_ == " _main
                        \cdotssys.exit(main(sys.argv))
```

### 3.2.2 Query database info

Listing 3: Simple example to print info from a SiteHopper database

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
import sqlite3
import sys
from openeye import oesitehopper
def get_info(shdb_file):
   conn = sqlite3.connect(f"file:(shdb_file)?mode=ro", uri=True)
   cursor = conn.cursor()res = cursor.execute("SELECT title, lastModifiedDate, SiteHopperToolkitVersion from
  Tnfo: "
```

```
row = res.fetchone()print(f"Path: {os.path.abspath(shdb_file) }")
   print (f'' Title: \{row[0]\}")
   print (f" Modified: {row[1]}")
    print (f" SiteHopper TK version: {row[2]}")
   res = cursor.execute("SELECT * from Version;")row = res.fetchone()print(f'' version: \{row[0]}\})")res = cursor.execute("SELECT count (*) from patches;")row = res.fetchone()print (f" Num Patches: {row[0]}")
   res = cursor.execute("SELECT count (*) from designunit;")
   row = res.fetchone()print (f'' Num DUs: \{row[0]-1\}")
def main (args) :
    if len(args) != 2:
        print ("usage: shdb_info.py <shdbfile>")
        return <sub>0</sub>shdb = oesitehopper.OESiteHopperDatabase()
    if not os.path.exists(args[1]) or not shdb.Open(args[1], oesitehopper.
→OESiteHopperDatabaseMode READONLY):
        print (f"/args[1]) is not a valid SHDB file")
        return 1
    shdb.Close()
    get_info(args[1])
    return 0
if __name__ == "__main__\mathbf{m}_2sys.exit(main(sys.argv))
```

### 3.2.3 Get an OEDesignUnit from database

Listing 4: Simple example to extract one or more OEDesignUnits from a SiteHopper database.

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
import os
import sys
from openeye import oechem
from openeye import oesitehopper
def main (args) :
   itf = oechem. 0EInterface()oechem. OEConfigure (itf, interface)
   if oechem. OECheckHelp(itf, args):
        return 0
    if not oechem. OEParseCommandLine(itf, args):
        return 1
   dbname = itf. GetString("-shdb")outfile = Noneif itf.HasString("-out"):
        outfile = itf.GetString("-out")
    shdb = oesitehopper.OESiteHopperDatabase()
   if not os.path.isfile(dbname) or not shdb.Open(dbname, oesitehopper.
\rightarrowOESiteHopperDatabaseMode READONLY):
        print (f"unable to open {dbname} for reading")
        return 1
    if outfile and not oechem. OEIsWriteableDesignUnit (outfile) :
        print (f" {outfile} is not a valid OEDesignUnit filename")
        return 1
    if itf.HasUnsignedInt("-index") and itf.HasString("-title"):
        print ("can't use both -index and -title together")
        return 1
   du = occhem. OEDesignUnit()
    if itf.HasUnsignedInt("-index"):
        index = \text{itf.getUnsignedInt("-index")}if shdb.GetDesignUnit(du, index):
            if outfile and oechem. OEWriteDesignUnit (outfile, du) :
                print (f"Wrote DU {du.GetTitle() } to {outfile}")
                return 0
            else:
                print(f"ID: {index}, TITLE: {shdb.GetTitle(index)}")
        else:
            print ("unable to retrieve DU with IDX = \{index\}")
            return 1elif itf.HasString("-title"):
        title = itf.GetString("-title")
        indices = shdb.GetIDByTitle(title)
        if len(indices) == 0:
            print ("No DUs found with title matching '{title}'")
            return False
```

```
ofs = Noneif outfile:
            ofs = oechem.oeofstream(outfile)
        for index in indices:
            if ofs and shdb. GetDesignUnit (du, index):
                oechem.OEWriteDesignUnit(ofs, du)
                print (f"Wrote DU {du.GetTitle() } to {outfile}")
            else:
                print(f"ID: {index}, TITLE: {shdb.GetTitle(index)}")
    Also:print ("Please try -index or -title for DUs to extract")
interface = """"!BRIEF get_designunit.py [-index IDX | -title TITLE] <shdb> <oedu file>
!CATEGORY I/O
    !PARAMETER -shdb 1
        ! TYPE string
        !REQUIRED true
        !VISIBILITY simple
        !BRIEF Input OESiteHopperDatabase
    ! END
    !PARAMETER -out 2
        !TYPE string
        !REOUIRED false
        !VISIBILITY simple
        !BRIEF Output .oedu file. If empty, just print out titles of matched DUs
    !END
! END
!CATEGORY Choice 99
    !PARAMETER -index
        !TYPE unsigned
        !REQUIRED false
        !VISIBILITY simple
        !BRIEF Single index of OEDU to extract from database
    ! END
    !PARAMETER -title
        !TYPE string
        !REQUIRED false
        !VISIBILITY simple
        !BRIEF Title for substring match to extract from database
    ! END
!END
\mathbf{u} and \mathbf{u}if name == "_main ":
    sys.exit(main(sys.argv))
```

## PRELIMINARY OESITEHOPPER API

## **4.1 OESiteHopper Classes**

Attention: This API is currently available in C++ and Python.

### 4.1.1 OESiteHopperDatabase

class OESiteHopperDatabase : public OEShape:: OESiteHopperDatabaseBase

This class allows creation and searching of one or more OESiteHopper patches, built from OEDesignUnits. When adding data to the database, it can be opened in either Create or Append mode. For searching, open in Search (Read-Only) mode for thread safety and to prevent accidentally changing the data.

#### **Constructors**

```
OESiteHopperDatabase()
OESiteHopperDatabase(const OESiteHopperDatabase &)
```

Default constructors.

#### Open

```
bool Open (const std::string &dbfile, const unsigned int mode,
          const OESiteHopperDatabaseOptions &opts=OESiteHopperDatabaseOptions())
```

Open a file as an OESiteHopperDatabase.

To create a new database, use the mode OESiteHopperDatabaseMode\_CREATE. If the file already exists, it will be overwritten. The options used to create the database can be changed by passing an new version of OESiteHopper-DatabaseOptions.

To append to an existing database, use the mode OESiteHopperDatabaseMode\_APPEND. If the file does not yet exists, it will be created like the Create mode.

To read or search a file, open using the mode OESiteHopperDatabaseMode SEARCH. This opens the database in read-only mode and will not allow adding new entries.

Note: OESiteHopperDatabaseOptions are only used in CREATE mode. Otherwise, options already stored in the database will be used.

#### operator bool

operator bool () const

#### **Add**

```
unsigned int Add (const std:: string & filename)
unsigned int Add (const OEBio:: OEDesignUnit &du)
```

Add a single OEDesignUnit file or object to an open database. This method will fail if the database is not open or if not opened in Create or Append mode.

Returns the index of the newly added OEDesignUnit or UINT MAX on failure.

#### **AddDirectory**

```
bool AddDirectory (const std:: string &path, unsigned int ncpu=0,
                  OESystem:: OETracerBase &tracer=OESystem:: OENoTracer)
```

Add a directory of OEDesignUnit files to the database. This call will recurse the entire directory tree, looking for all available .oedu files.

By default, this call will use all available CPUs to process this set of OEDesignUnits. Setting ncpu can be used to reduce the number of CPUs used.

If you want to see a progress bar during the process, use an OEConsoleProgressTracer instead of the default OENo-Tracer.

#### **Close**

void Close()

Close the database connection. Any operations (except another call to  $Open$ ) after this will fail.

#### **GetDesignUnit**

bool GetDesignUnit (OEBio:: OEDesignUnit &du, unsigned int idx) const

Get a specific OEDesignUnit based on the database index.

#### **GetIDByTitle**

std::vector<unsigned int> GetIDByTitle(const std::string &title) const

Get a vector of indices based on a substring match of the passed in title to OEDesignUnit titles in the database.

#### **GetMaxMolldx**

unsigned int GetMaxMolIdx() const

Internal use: Get the maximum index in the database. Used by the GPU search.

#### **GetMolecule**

bool GetMolecule (OEChem:: OEMolBase &mol, unsigned int idx) const

Internal use: Get the patch molecule for the given index.

#### **GetOptions**

const OESiteHopperDatabaseOptions &GetOptions () const

Get the options used to create patches as they are added to the database.

#### GetSequenceInfo

```
bool GetSequenceInfo(std::vector<std::vector<std::string>> &seq,
                     unsigned int idx) const
```

Internal use: Get the sequence info for the given database index.

#### **GetTitle**

bool GetTitle(std::string &title, unsigned int idx) const

Get the OEDesignUnit title for the given index.

### 4.1.2 OESiteHopperDatabaseOptions

class OESiteHopperDatabaseOptions : public OESystem:: OEOptions

This class provides a way to set up how the SiteHopper database will be built.

#### **Constructors**

```
OESiteHopperDatabaseOptions()
OESiteHopperDatabaseOptions (const OESiteHopperDatabaseOptions &)
OESiteHopperDatabaseOptions (OESiteHopperDatabaseOptions & &) =default
```

Default and copy constructors.

#### **GetPatchOptions**

const OESiteHopperPatchOptions& GetPatchOptions() const

Returns a reference to the OESiteHopperPatchOptions instance as currently set. This defines options for building patches as they are added to the database.

#### **SetPatchOptions**

**void** SetPatchOptions (const OESiteHopperPatchOptions& opts)

Update the internal OESiteHopperPatchOptions.

#### operator=

```
OESiteHopperDatabaseOptions & operator= (const OESiteHopperDatabaseOptions &)
OESiteHopperDatabaseOptions & operator=(OESiteHopperDatabaseOptions & &)=default
```

#### **CreateCopy**

```
OESiteHopperDatabaseOptions *CreateCopy() const
```

### 4.1.3 OESiteHopperPatchOptions

class OESiteHopperPatchOptions : public OESystem:: OEOptions

Options that affect how SiteHopper Patches are contructed.

#### **Constructors**

```
OESiteHopperPatchOptions()
OESiteHopperPatchOptions (const OESiteHopperPatchOptions &)
OESiteHopperPatchOptions (OESiteHopperPatchOptions & &) = default
```

Default constructors.

#### operator=

```
OESiteHopperPatchOptions & operator= (const OESiteHopperPatchOptions &)
OESiteHopperPatchOptions & operator=(OESiteHopperPatchOptions & &)=default
```

#### **GetResidueCutoff**

float GetResidueCutoff() const

Get distance (in Angstroms) from any ligand atom to any protein residue to consider that residue part of the patch. [default: 7.0]

#### **GetSiteSize**

float GetSiteSize() const

Get distance from any site residue to edge of patch surface to be created. A larger distance means a larger patch will be created.

[ $default: 4.0$ ]

#### **GetSurfaceCutoff**

float GetSurfaceCutoff() const

Get maximum distance a color atom can be from the surface to be included in the patch.

[default:  $2.5$ ]

#### **GetScaleFactor**

unsigned int GetScaleFactor() const

Get factor by which number of surface points are reduced to create the patch surface.

[default: 4]

#### **GetUserStartsScaleFactor**

```
unsigned int GetUserStartsScaleFactor() const
```

Get factor by which the number of surface points are reduced to create user starts for the optimization.

[default: 14]

#### **SetResidueCutoff**

void SetResidueCutoff (float cutoff)

Set distance (in Angstroms) from any ligand atom to any protein residue to consider that residue part of the patch.

[default: 7.0]

#### **SetSiteSize**

void GetSiteSize (float size)

Set distance from any site residue to edge of patch surface to be created. A larger distance means a larger patch will be created.

[default:  $4.0$ ]

#### **SetSurfaceCutoff**

```
void SetSurfaceCutoff()
```

Set maximum distance a color atom can be from the surface to be included in the patch. A larger value means more color atoms from the protein will be included.

[ $default: 2.5$ ]

#### **SetScaleFactor**

void SetScaleFactor (unsigned int factor)

Set factor by which number of surface points are reduced to create the patch surface. A larger factor will result in fewer surface/shape point. Too few will result in a poor shape description of the patch.

[default: 4]

#### **SetUserStartsScaleFactor**

void SetUserStartsScaleFactor (unsigned int factor)

Set factor by which the number of surface points are reduced to create user starts for the optimization.

[default: 14]

#### **CreateCopy**

OESiteHopperPatchOptions \*CreateCopy() const

#### **GetColorForceField**

const OEShape:: OEColorForceField& GetColorForceField() const

Get a reference to the OEColorForceField used for patch creation and scoring.

### **4.1.4 OESiteHopperResults**

class OESiteHopperResults

This is a class used inside the SiteHopper search. User results user the OESiteHopperScore class.

The following classes derive from this class:

• OESiteHopperScore

#### **Constructors**

```
OESiteHopperResults()=default
OESiteHopperResults (OESiteHopperResults &&rhs) =default
OESiteHopperResults (const OESiteHopperResults & rhs) = default
```

Default constructors.

#### operator=

```
OESiteHopperResults & operator=(OESiteHopperResults & & rhs) = default
OESiteHopperResults & operator= (const OESiteHopperResults & rhs) = default
```

#### **GetColorScale**

float GetColorScale() const

Get scale factor applied to color Tanimoto to get PatchScore.

[default: 3.0]

#### **GetColorTanimoto**

float GetColorTanimoto() const

Get color Tanimoto from the patch overlay.

#### **GetPatchScore**

float GetPatchScore() const

Get PatchScore from overlay. This score is Shape Tanimoto + ScaleFactor \* Color Tanimoto.

#### GetRank

unsigned int GetRank() const

Get the rank in the hitlist.

#### **GetSequenceSimilarity**

float GetSequenceSimilarity() const

Get sequence similarity between referance patch protein and fit patch protein.

#### **GetShapeTanimoto**

float GetShapeTanimoto() const

Get Shape Tanimoto from overlay.

#### **SetColorScale**

void SetColorScale (float scale)

Set scale factor applied to color Tanimoto to get PatchScore.

[default: 3.0]

#### **SetColorTanimoto**

void SetColorTanimoto (float score)

#### **SetRank**

void SetRank (unsigned int rank)

#### **SetSequenceSimilarity**

```
void SetSequenceSimilarity (float similarity)
```

#### **SetShapeTanimoto**

void SetShapeTanimoto (float score)

### 4.1.5 OESiteHopperScore

class OESiteHopperScore : public OESiteHopperResults

This class is use to hold the score and results from a SiteHopper search.

The following methods are publicly inherited from OESiteHopperResults:

| operator=        | GetRank               | SetColorTanimoto      |
|------------------|-----------------------|-----------------------|
| GetColorScale    | GetSequenceSimilarity | SetRank               |
| GetColorTanimoto | GetShapeTanimoto      | SetSequenceSimilarity |
| GetPatchScore    | SetColorScale         | SetShapeTanimoto      |

#### **Constructors**

```
OESiteHopperScore()
OESiteHopperScore(OESiteHopperScore & &) =default
OESiteHopperScore(const OESiteHopperScore & rhs) =default
```

Default constructors.

#### operator=

```
OESiteHopperScore & operator= (OESiteHopperScore & & rhs) = default
OESiteHopperScore & operator=(const OESiteHopperScore & rhs) = default
```

#### **GetDesignUnit**

```
OEBio:: OEDesignUnit GetDesignUnit () const
```

Get output OEDesignUnit for this result. The transfrom from the overlay will already be applied.

#### **GetID**

unsigned int GetID() const

Get database index for this result.

#### **GetTitle**

std::string GetTitle() const

Get title from OEDesignUnit.

#### **GetTransform**

const OEChem:: OETrans & GetTransform() const

Get the transform from the overlay. This allows applying the same transform to other objects to move them into the output frame of reference.

Note: When asking for the OEDesignUnit from this class, DO NOT apply this transform as the OEDesignUnit will already be transformed.

#### **SetDesignUnit**

```
void SetDesignUnit (const OEBio:: OEDesignUnit &du)
```

Internal use: Set the OEDesignUnit.

#### **SetID**

void SetID (const unsigned int id)

Internal use: Set the database index.

**SetTitle** 

```
void SetTitle (const std:: string & title)
```

Internal use: Set the title.

#### **SetTransform**

**void** SetTransform(const OEChem:: OETrans & trans)

Internal use: Set the transform.

### 4.1.6 OESiteHopperSearch

class OESiteHopperSearch : public OESiteHopperSearchBase

Class to perform a search of an OESiteHopperDatabase.

The following methods are publicly inherited from OESiteHopperSearchBase:

operator bool operator= Search

#### **Constructors**

OESiteHopperSearch (OESiteHopperDatabase & shdb)

Construct a search object to perform searches of the passed in OESiteHopperDatabase.

#### operator bool

operator bool() const

Used to verify that the database is opened correctly and the object is ready for a search.

#### **Search**

```
OESystem::OEIterBase<OESiteHopper::OESiteHopperScore> *
  Search (const OEBio:: OEDesignUnit & query,
         const OESiteHopperSearchOptions &options=OESiteHopperSearchOptions(),
         OESystem:: OETracerBase &tracer=OESystem:: NullTracer)
```

Perform a search using a query OEDesignUnit.

If you want to see a progress bar during the process, use an OEConsoleProgressTracer instead of the default OENo-Tracer.

### 4.1.7 OESiteHopperSearchBase

#### class OESiteHopperSearchBase

Base class for OESiteHopperSearch.

The following classes derive from this class:

• OESiteHopperSearch

#### **Constructors**

OESiteHopperSearchBase()

Constructors that need documenting.

#### operator bool

```
\textbf{operator } \textbf{bool} \;(\text{)} \quad \textbf{const} \; = 0
```

#### **Search**

```
OESystem::OEIterBase<OESiteHopperScore> *Search(const OEBio::OEDesignUnit &query,
                                                    const OESiteHopperSearchOptions &
\rightarrowoptions=OESiteHopperSearchOptions(),
                                                    OESystem:: OETracerBase &
\rightarrowtracer=OESystem::NullTracer)=0
```

### 4.1.8 OESiteHopperSearchOptions

class OESiteHopperSearchOptions : public OESystem:: OEOptions

Options to control the process in OESiteHopperSearch.

#### **Constructors**

```
OESiteHopperSearchOptions()
OESiteHopperSearchOptions (OESiteHopperSearchOptions & &) =default
OESiteHopperSearchOptions (const OESiteHopperSearchOptions &)=default
```

Default constructors.

#### **GetMaxHits**

unsigned int GetMaxHits() const

Get maximum number of hits to return from the search. Very large hitlists can use a large amount of RAM. [default: 200]

#### **GetNCPU**

unsigned int GetNCPU() const

Get maximum number of CPUs to use for search. Zero (0) implies use all available.

[default: 0]

#### **GetNormalizeAndRescore**

bool GetNormalizeAndRescore() const

Flag to determine whether patches of hits will be normalized to the surface area of the query patch and then rescored for the final hitlist.

[default: false]

#### **GetScoreCutoff**

float GetScoreCutoff() const

Minimum PatchScore for a hit to be considered part of the hitlist.

[default: 0.0]

#### **GetSequenceCutoff**

float GetSequenceCutoff() const

Maximum protein sequence similarity for a hit to be considered part of the hitlist.

[default: 100.0]

#### **GetUseGPU**

bool GetUseGPU () const

Flag to determine whether to use a GPU for prescreen as part of the search. This reduced the search time significantly, but requires Linux and a compatible Nvidia GPU. See GPU Prerequisites

#### **SetMaxHits**

void SetMaxHits (unsigned int maxHits)

Set maximum number of hits to return from the search. Very large hitlists can use a large amount of RAM. [default: 200]

#### **SetNCPU**

void SetNCPU(unsigned int n)

Set maximum number of CPUs to use for search. Zero (0) implies use all available.

[default:  $0$ ]

#### **SetNormalizeAndRescore**

void SetNormalizeAndRescore (bool state)

Flag to determine whether patches of hit OEDesignUnits will be normalized to the surface area of the query patch and then rescored for the final hitlist.

[default: false]

#### **SetScoreCutoff**

void SetScoreCutoff (float cutoff)

Minimum PatchScore for a hit to be considered part of the hitlist.

[default:  $0.0$ ]

#### **SetSequenceCutoff**

void SetSequenceCutoff (float cutoff)

Maximum protein sequence similarity for a hit to be considered part of the hitlist.

[default: 100.0]

#### operator=

```
OESiteHopperSearchOptions & operator= (OESiteHopperSearchOptions & &) = default
OESiteHopperSearchOptions & operator=(const OESiteHopperSearchOptions &)=default
```

#### **CreateCopy**

```
OESiteHopperSearchOptions *CreateCopy() const
```

## **4.2 OESiteHopper Constants**

### 4.2.1 OESiteHopperDatabaseMode

Control the mode when opening an OESiteHopperDatabase.

#### **APPEND**

Opening in APPEND mode allows adding more OEDesignUnits to an existing database. OESiteHopperDatabaseOptions that are already stored in the database will be used to create new patches.

If the requested database file does not yet exist, this mode works like CREATE.

#### **CREATE**

Create a new OESiteHopperDatabase file. If the file already exists it will be overwritten.

#### **MAX**

The largest value in the namespace. Useful for verifying that a given mode is valid. This mode is not valid for opening an OESiteHopperDatabase.

#### **READONLY**

Open a OESiteHopperDatabase file in read-only mode. This is equivalent to SEARCH.

#### **SEARCH**

Open a OESiteHopperDatabase file for searching. This is equivalent to READONLY.

#### **UNDEFINED**

The lowest value in the namespace. Useful for verifying that a given mode is valid. This mode is not valid for opening an OESiteHopperDatabase.

## **4.3 OESiteHopper Functions**

### **4.3.1 OEAddPatchSurface**

```
bool OEAddPatchSurface(OEBio::OEDesignUnit &du,
                       const OESiteHopperPatchOptions opts=OESiteHopperPatchOptions())
```

Create the patch surface (as created inside  $A d d$ ) and attach it to the OEDesignUnit. This method is not needed for database creation or searching, but is useful for visualization.

### 4.3.2 OEGetPatchSurface

```
bool OEGetPatchSurface(OESpicoli::OESurface &,
                       const OEBio:: OEDesignUnit &du)
```

Get the patch surface (if attached) that is created by OEAddPatchSurface.

### 4.3.3 OEHasPatchSurface

**bool** OEHasPatchSurface (const OEBio:: OEDesignUnit &du)

Verify the OEDesignUnit has a patch surface attached.

### 4.3.4 OEMakePatchFromDesignUnit

```
bool OEMakePatchFromDesignUnit (OEChem:: OEMolBase &patch,
                                const OEBio:: OEDesignUnit &du,
                                const OESiteHopperPatchOptions &
→opts=OESiteHopperPatchOptions())
bool OEMakePatchFromDesignUnit (OEChem:: OEMolBase &patch,
                                OESpicoli:: OESurface &outSurface,
                                const OEBio:: OEDesignUnit &du,
                                const OESiteHopperPatchOptions &
→opts=OESiteHopperPatchOptions())
```

Create a new SiteHopper patch from the passed in OEDesignUnit. This is not normally used as this method is called inside database creation and at search time.

### 4.3.5 OESetPatchSurface

```
bool OESetPatchSurface(OEBio::OEDesignUnit &du,
                       const OESpicoli:: OESurface &surface)
```

Used by OEAddPatchSurface to attach the surface to the OEDesignUnit.

### 4.3.6 OESetProteinSDData

```
void OESetProteinSDData (OEBio:: OEDesignUnit &du,
                        const OESiteHopperScore &score)
```

Set various values from *score* as SD data on the protein inside the OEDesignUnit. Useful for showing these values in the spreadsheet in VIDA.

### 4.3.7 OESiteHopperGetArch

char \*OESiteHopperGetArch() const

Returns the architecture of the current version of the SiteHopper toolkit. Examples include:

- microsoft-win64-x64
- $\cdot$  linux-x64

### 4.3.8 OESiteHopperGetLicensee

```
std::string OESiteHopperGetLicensee()
bool OESiteHopperGetLicensee(std::string &licensee)
```

Returns the LICENSEE from the current valid SiteHopper TK license.

### 4.3.9 OESiteHopperGetPlatform

const char \*OESiteHopperGetPlatform()

Returns the platform, including compiler version, of the current version of the SiteHopper toolkit. Examples include:

- microsoft-win64-msvc17-x64
- $linux-g++7.x-x64$

### 4.3.10 OESiteHopperGetRelease

const char \*OESiteHopperGetRelease()

Returns the version of this toolkit release. For example: 1, 6, 1.

### 4.3.11 OESiteHopperGetSite

```
std::string OESiteHopperGetSite()
bool OESiteHopperGetSite(std::string &site)
```

Returns the SITE from the current valid SiteHopper TK license.

### 4.3.12 OESiteHopperGetVersion

unsigned int OESiteHopperGetVersion()

Returns the build date of the toolkit as an unsigned int. For example: 20210527.

### 4.3.13 OESiteHopperIsGPUReady

**bool** OESiteHopperIsGPUReady()

Returns true if Search can successfully use the GPU for prescreen search. Useful for checking whether the machine has an accelerator properly setup. It is guaranteed that if this function returns 'true' that all subsequent Search method can successfully execute queries. That means that this function will effectively initialize an underlying context that is re-used by OESiteHopperSearch objects, possibly grabbing an "exclusive process" lock: http://docs.nvidia. com/cuda/cuda-c-programming-guide/#compute-modes

### 4.3.14 OESiteHopperIsLicensed

```
bool OESiteHopperIsLicensed(const char *feature=0,
                            unsigned int *expdate=0)
```

Determines whether a valid license file is present. This function may be called without a legitimate run-time license to determine whether it is safe to call any **SiteHopper TK** functionality.

The 'feature' argument can be used to check for a valid license to SiteHopper TK along with the following features: 'python', 'java', or 'clr' (for CSharp).

The 'expdate' argument can be used to obtain the expiration date of the current **SiteHopper TK** license.

See also:

• OEChemIsLicensed function

### **CHAPTER**

## **FIVE**

## **RELEASE HISTORY**

## 5.1 SiteHopper TK 2.1.1

### 5.1.1 Minor bug fixes

• The OESiteHopperIsGPUReady function has been safeguarded from a rare crash.

## 5.2 SiteHopper TK 2.1.0

### 5.2.1 New features

• GPU-based SiteHopper is no longer used to prescreen but is enabled as a stand-alone search method.

## 5.3 Sitehopper TK 2.0.4

Minor internal improvements have been made.

## 5.4 Sitehopper TK 2.0.3

Minor internal improvements have been made.

## 5.5 Sitehopper TK 2.0.2

Minor internal improvements have been made.

## 5.6 Sitehopper TK 2.0.1

### 5.6.1 Python-specific changes

• An issue with OEGetPatchSurface wrapping to Python was fixed.

## 5.7 SiteHopper TK 2.0.0

### Fall 2021

This is the initial release of the SiteHopper TK.

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

## **SEVEN**

## **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

### **CHAPTER**

## **EIGHT**

## **CITATION**

## 8.1 Orion<sup>®</sup> Floes

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

## **8.3 OpenEye Web Services**

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

| Name of Project                  | Website                                                                             | License                                      |
|----------------------------------|-------------------------------------------------------------------------------------|----------------------------------------------|
| abseil-cpp                       | https://github.com/abseil/abseil-cpp                                                | https://                                     |
| absl-py                          | https://github.com/abseil/abseil-py                                                 | https://                                     |
| aiohttp                          | https://docs.aiohttp.org/en/stable/                                                 | https://                                     |
| aiosignal                        | https://github.com/aio-libs/aiosignal                                               | https://                                     |
| Amazon Linux 2                   | https://aws.amazon.com/amazon-linux-2                                               | N/A                                          |
| AmberUtils                       | http://ambermd.org                                                                  | N/A                                          |
| ambit                            | https://github.com/khimaros/ambit                                                   | https://                                     |
| amqp                             | https://github.com/celery/py-amqp                                                   | https://                                     |
| anaconda-anon-usage              | <b>Orion Floes</b>                                                                  | https://                                     |
| angular                          | https://github.com/angular/angular.js                                               | https://                                     |
| angular-animate                  | https://github.com/angular/angular.js                                               | https://                                     |
| angular-cache                    | https://github.com/jmdobry/angular-cache                                            | https://                                     |
| angular-cookies                  | https://github.com/angular/angular.js                                               | https://                                     |
| angular-loggly-logger            | https://github.com/ajbrown/angular-loggly-logger                                    | https://                                     |
| angular-mocks                    | https://github.com/angular/angular.js                                               | https://                                     |
| angular-resource                 | https://github.com/angular/angular.js                                               | https://                                     |
| angular-toggle-switch            | https://github.com/cgarvis/angular-toggle-switch                                    | https://                                     |
| angular-ui-grid                  | https://github.com/angular-ui/ui-grid                                               | https://                                     |
| angular-ui-router                | https://github.com/angular-ui/ui-router                                             | https://                                     |
| angular-ui-tree                  | https://github.com/angular-ui-tree/angular-ui-tree                                  | https://                                     |
| angular-vs-repeat                | https://github.com/kamilkp/angular-vs-repeat                                        | https://                                     |
| aniso8601                        | https://bitbucket.org/nielsenb/aniso8601                                            | https://                                     |
| annotated-types                  | https://github.com/annotated-types/annotated-types                                  | https://                                     |
| anyio                            | https://github.com/agronholm/anyio                                                  | https://                                     |
| appdirs                          | http://github.com/ActiveState/appdirs                                               | http://                                      |
| appengine                        | https://google.golang.org/appengine                                                 | https://                                     |
| arabic-reshaper                  | https://github.com/mpcabd/python-arabic-reshaper/                                   | https://                                     |
| archspec                         | https://github.com/archspec/archspec/blob/master/README.md                          | https://                                     |
| Name of Project                  | Website                                                                             | License                                      |
| argon2-cffi                      | https://github.com/hynek/argon2-cffi                                                | https:/                                      |
| argon2-cffi-bindings             | https://github.com/hynek/argon2-cffi-bindings                                       | https:/                                      |
| arpack                           | https://www.caam.rice.edu/software/ARPACK/                                          | https:/                                      |
| ascii85                          | https://github.com/huandu/node-ascii85                                              | https:/                                      |
| ase                              | https://wiki.fysik.dtu.dk/ase/                                                      | https:/                                      |
| asgiref                          | https://github.com/django/asgiref/                                                  | https:/                                      |
| asn1crypto                       | https://github.com/wbond/asn1crypto                                                 | https:/                                      |
| assertions go-render             | https://github.com/smartystreets/assertions/internal/go-render/render               | https:/                                      |
| assertions oglmatchers           | https://github.com/smartystreets/assertions/internal/oglematchers                   | https:/                                      |
| assertions                       | https://github.com/smartystreets/assertions                                         | https:/                                      |
| asttokens                        | https://github.com/gristlabs/asttokens                                              | https:/                                      |
| astunparse                       | https://github.com/simonpercivall/astunparse                                        | https:/                                      |
| async-lru                        | https://github.com/aio-libs/async-lru                                               | https:/                                      |
| async-timeout                    | https://github.com/aio-libs/async-timeout                                           | https:/                                      |
| atk-1.0                          | https://docs.gtk.org/atk/                                                           | https:/                                      |
| atomic                           | https://github.com/uber-go/atomic                                                   | https:/                                      |
| atomicwrites                     | https://github.com/untitaker/python-atomicwrites                                    | https:/                                      |
| attrs                            | https://www.attrs.org/                                                              | https:/                                      |
| aws-sdk-go                       | https://github.com/aws/aws-sdk-go                                                   | https:/                                      |
| Babel                            | https://github.com/python-babel/babel                                               | https:/                                      |
| backcall                         | https://github.com/takluyver/backcall                                               | https:/                                      |
| backports                        | https://github.com/brandon-rhodes/backports                                         | https:/                                      |
| backports.functools-lru-cache    | https://github.com/jaraco/backports.functools_lru_cache                             | https:/                                      |
| base62                           | https://github.com/kare/base62                                                      | https:/                                      |
| beautifulsoup4                   | https://www.crummy.com/software/BeautifulSoup/                                      | https:/                                      |
| billiard                         | https://github.com/celery/billiard                                                  | https:/                                      |
| biopython                        | https://biopython.org                                                               | https:/                                      |
| biotite                          | https://github.com/biotite-dev/biotite/blob/master/README.rst                       | https:/                                      |
| bitset                           | https://github.com/willf/bitset                                                     | https:/                                      |
| blas                             | https://www.netlib.org/blas/                                                        | https:/                                      |
| bleach                           | https://github.com/mozilla/bleach                                                   | https:/                                      |
| blessings                        | https://github.com/erikrose/blessings                                               | https:/                                      |
| blinker                          | https://pythonhosted.org/blinker/                                                   | https:/                                      |
| blosc                            | https://github.com/Blosc/python-blosc                                               | https:/                                      |
| blosc2                           | https://github.com/Blosc/python-blosc2                                              | https:/                                      |
| boltons                          | https://github.com/mahmoud/boltons                                                  | https:/                                      |
| boost                            | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                      |
| boost-cpp                        | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html               | https:/                                      |
| bootstrap-vue                    | https://github.com/bootstrap-vue/bootstrap-vue                                      | https:/                                      |
| boto3                            | https://github.com/boto/boto3                                                       | https:/                                      |
| botocore                         | https://github.com/boto/botocore                                                    | https:/                                      |
| Bottleneck                       | https://bottleneck.readthedocs.io/en/latest/index.html                              | https:/                                      |
| Brotli                           | https://github.com/google/brotli                                                    | https:/                                      |
| brotli-bin                       | https://github.com/google/brotli                                                    | https:/                                      |
| brotli-python                    | http://python-hyper.org/projects/brotlipy/en/latest/                                | https:/                                      |
| brotlipy                         | https://github.com/python-hyper/brotlicffi                                          | https:/                                      |
| bson                             | http://github.com/py-bson/bson                                                      | https:/                                      |
| bytefmt                          | https://code.cloudfoundry.org/bytefmt                                               | https:/                                      |
| bzip2                            | https://www.bzip.org                                                                | https:/                                      |
| Name of Project                  | Website                                                                             | License                                      |
| c-ares                           | https://github.com/c-ares/c-ares                                                    | https://spdx.org/licenses/MIT.html           |
| ca-certificates                  | https://github.com/conda-forge/ca-certificates-feedstock                            | https://spdx.org/licenses/MPL-2.0.html       |
| cached-property                  | https://github.com/pydanny/cached-property                                          | https://spdx.org/licenses/BSD-2-Clause.html  |
| cachetools                       | https://github.com/tkem/cachetools                                                  | https://spdx.org/licenses/Apache-2.0.html    |
| cairo                            | https://pycairo.readthedocs.io/en/latest/                                           | https://spdx.org/licenses/LGPL-2.1-only.html |
| canvas                           | https://github.com/Automattic/node-canvas                                           | https://spdx.org/licenses/MIT.html           |
| cctbx                            | https://github.com/cctbx/cctbx_project                                              | https://spdx.org/licenses/BSD-3-Clause.html  |
| celery                           | https://github.com/celery/celery                                                    | https://spdx.org/licenses/BSD-3-Clause.html  |
| Cerberus                         | https://docs.python-cerberus.org/en/stable/                                         | https://spdx.org/licenses/MIT.html           |
| certifi                          | https://certifi.readthedocs.io/en/latest/                                           | https://spdx.org/licenses/MPL-2.0.html       |
| cffi                             | https://github.com/python-cffi/cffi                                                 | https://spdx.org/licenses/MIT.html           |
| cftime                           | https://pypi.org/project/cftime/                                                    | https://spdx.org/licenses/LGPL-3.0-only.html |
| chardet                          | https://github.com/chardet/chardet                                                  | https://spdx.org/licenses/LGPL-2.1-only.html |
| charset-normalizer               | https://github.com/ousret/charset_normalizer                                        | https://spdx.org/licenses/MIT.html           |
| chunkreader                      | https://github.com/jackc/chunkreader/v2                                             | https://spdx.org/licenses/MIT.html           |
| click                            | https://palletsprojects.com/p/click/                                                | https://spdx.org/licenses/BSD-3-Clause.html  |
| click-completion                 | https://github.com/click-contrib/click-completion                                   | https://spdx.org/licenses/MIT.html           |
| click-didyoumean                 | https://github.com/click-contrib/click-didyoumean                                   | https://spdx.org/licenses/MIT.html           |
| click-plugins                    | https://github.com/click-contrib/click-plugins                                      | https://spdx.org/licenses/BSD-3-Clause.html  |
| click-repl                       | https://github.com/untitaker/click-repl                                             | https://spdx.org/licenses/MIT.html           |
| cloudpickle                      | https://github.com/cloudpipe/cloudpickle                                            | https://spdx.org/licenses/BSD-3-Clause.html  |
| cmake                            | https://cmake.org/                                                                  | https://spdx.org/licenses/BSD-3-Clause.html  |
| colorama                         | https://github.com/tartley/colorama                                                 | https://spdx.org/licenses/BSD-3-Clause.html  |
| comm                             | https://github.com/ipython/comm                                                     | https://spdx.org/licenses/BSD-3-Clause.html  |
| compose                          | https://github.com/docker/compose                                                   | https://spdx.org/licenses/Apache-2.0.html    |
| conda-content-trust              | https://github.com/conda/conda-content-trust                                        | https://spdx.org/licenses/BSD-3-Clause.html  |
| conda-libmamba-solver            | https://github.com/conda/conda-libmamba-solver                                      | https://spdx.org/licenses/BSD-3-Clause.html  |
| conda-package-handling           | https://github.com/conda/conda-package-handling                                     | https://spdx.org/licenses/BSD-3-Clause.html  |
| conda-package-streaming          | https://anaconda.org/conda-forge/conda-package-streaming                            | https://spdx.org/licenses/BSD-3-Clause.html  |
| conda-token                      | https://anaconda.org/anaconda/conda-token                                           | https://spdx.org/licenses/BSD-3-Clause.html  |
| confuse                          | https://github.com/beetbox/confuse                                                  | https://spdx.org/licenses/MIT.html           |
| contourpy                        | https://github.com/contourpy/contourpy                                              | https://spdx.org/licenses/BSD-3-Clause.html  |
| cpp-peglib                       | https://github.com/yhirose/cpp-peglib                                               | https://spdx.org/licenses/MIT.html           |
| cryptography                     | https://github.com/pyca/cryptography                                                | https://spdx.org/licenses/Apache-2.0.html    |
| cssselect2                       | https://github.com/Kozea/cssselect2                                                 | https://spdx.org/licenses/BSD-3-Clause.html  |
| cudatoolkit                      | https://developer.nvidia.com/cuda-toolkit                                           |                                              |
| cupy-cuda113                     | https://cupy.dev/                                                                   | https://spdx.org/licenses/MIT.html           |
| curl                             | https://curl.se                                                                     | https://spdx.org/licenses/curl.html          |
| cycler                           | https://github.com/matplotlib/cycler                                                | https://spdx.org/licenses/BSD-3-Clause.html  |
| cyrus-sasl                       | https://github.com/cyrusimap/cyrus-sasl                                             | https://spdx.org/licenses/BSD-3-Clause.html  |
| Cython                           | https://cython.org                                                                  | https://spdx.org/licenses/Apache-2.0.html    |
| d3                               | https://github.com/mbostock/d3                                                      | https://spdx.org/licenses/BSD-3-Clause.html  |
| dataclasses                      | https://github.com/ericvsmith/dataclasses                                           | https://spdx.org/licenses/Python-2.0.html    |
| ddsketch                         | http://github.com/datadog/sketches-py                                               | https://spdx.org/licenses/Apache-2.0.html    |
| debugpy                          | https://aka.ms/debugpy                                                              | https://spdx.org/licenses/MIT.html           |
| decimal                          | https://github.com/shopspring/decimal                                               | https://spdx.org/licenses/MIT.html           |
| decorator                        | https://github.com/micheles/decorator                                               | https://spdx.org/licenses/BSD-2-Clause.html  |
| deepdiff                         | https://github.com/seperman/deepdiff                                                | https://spdx.org/licenses/MIT.html           |
| deeptime                         | https://github.com/deeptime-ml/deeptime                                             | https://spdx.org/licenses/LGPL-3.0-only.html |
| Name of Project                  | Website                                                                             | License                                      |
| defusedxml                       | https://github.com/tiran/defusedxml                                                 | https:/                                      |
| dill                             | https://github.com/uqfoundation/dill                                                | https:/                                      |
| distro                           | Orion Floes                                                                         | https:/                                      |
| Django                           | https://www.djangoproject.com/                                                      | https:/                                      |
| django-classy-tags               | https://github.com/django-cms/django-classy-tags                                    | https:/                                      |
| django-cors-headers              | https://github.com/adamchainz/django-cors-headers                                   | https:/                                      |
| django-csp                       | https://github.com/mozilla/django-csp                                               | https:/                                      |
| django-extensions                | https://github.com/django-extensions/django-extensions                              | https:/                                      |
| django-filter                    | https://github.com/carltongibson/django-filter/tree/master                          | https:/                                      |
| django-redis                     | https://github.com/jazzband/django-redis                                            | https:/                                      |
| django-taggit                    | https://github.com/jazzband/django-taggit                                           | https:/                                      |
| django-taggit-serializer         | https://github.com/glemmaPaul/django-taggit-serializer                              | https:/                                      |
| django-taggit-templatetags2      | https://github.com/fizista/django-taggit-templatetags2                              | https:/                                      |
| djangorestframework              | https://www.django-rest-framework.org/                                              | https:/                                      |
| dkh                              | https://psicode.org/psi4manual/master/dkh.html                                      | https:/                                      |
| dm-tree                          | https://github.com/deepmind/tree                                                    | https:/                                      |
| docker-py                        | https://github.com/docker/docker-py/                                                | https:/                                      |
| docopt                           | https://docopt.org                                                                  | https:/                                      |
| docutils                         | https://docutils.sourceforge.io                                                     | https:/                                      |
| drf-dynamic-fields               | https://github.com/dbrgn/drf-dynamic-fields                                         | https:/                                      |
| editdistance                     | https://github.com/roy-ht/editdistance                                              | https:/                                      |
| eigen                            | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https:/                                      |
| einops                           | https://github.com/arogozhnikov/einops                                              |                                              |
| entrypoints                      | https://github.com/takluyver/entrypoints                                            | https:/                                      |
| errors                           | https://github.com/pkg/errors                                                       | https:/                                      |
| eslint-plugin                    | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                      |
| et_xmlfile                       | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https:/                                      |
| exceptiongroup                   | https://github.com/agronholm/exceptiongroup                                         | https:/                                      |
| executing                        | https://github.com/alexmojaki/executing                                             | https:/                                      |
| expat                            | https://libexpat.github.io                                                          | https:/                                      |
| fastjsonschema                   | https://github.com/horejsek/python-fastjsonschema                                   | https:/                                      |
| fastrlock                        | https://github.com/scoder/fastrlock                                                 | https:/                                      |
| fftw                             | https://www.fftw.org                                                                | comm                                         |
| filebuffer                       | https://github.com/mattetti/filebuffer                                              | https:/                                      |
| filelock                         | https://py-filelock.readthedocs.io/en/latest/index.html                             | https:/                                      |
| finufft                          | https://github.com/flatironinstitute/finufft                                        | https:/                                      |
| Flask                            | https://flask.palletsprojects.com/en/2.1.x/                                         | https:/                                      |
| flatbuffers                      | https://google.github.io/flatbuffers/                                               | https:/                                      |
| flit-core                        | https://github.com/pypa/flit                                                        | https:/                                      |
| FLTK                             | https://www.fltk.org/index.php                                                      | https:/                                      |
| fmt                              | https://fmt.dev/latest/index.html                                                   | https:/                                      |
| font-awesome                     | https://github.com/FortAwesome/Font-Awesome                                         | https:/                                      |
| font-ttf-dejavu-sans-mono        | https://dejavu-fonts.github.io                                                      | https:/                                      |
| font-ttf-inconsolata             | https://fonts.google.com/specimen/Inconsolata                                       | https:/                                      |
| font-ttf-source-code-pro         | https://fonts.google.com/specimen/Source+Code+Pro                                   | https:/                                      |
| font-ttf-ubuntu                  | https://fonts.google.com/specimen/Ubuntu                                            | https:/                                      |
| fontconfig                       | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https:/                                      |
| fonts-conda-ecosystem            | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https:/                                      |
| fonts-conda-forge                | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https:/                                      |
| Name of Project                  | Website                                                                             | License                                      |
| fonttools                        | https://github.com/fonttools/fonttools                                              | https://                                     |
| freetype                         | https://freetype.org                                                                | https://                                     |
| fribidi                          | https://github.com/fribidi/fribidi                                                  | https://                                     |
| frozendict                       | Orion Floes                                                                         | https://                                     |
| frozenlist                       | https://github.com/aio-libs/frozenlist                                              | https://                                     |
| fsmlite                          | https://github.com/tkem/fsmlite                                                     | https://                                     |
| fsspec                           | https://github.com/fsspec/filesystem_spec                                           | https://                                     |
| funcy                            | https://github.com/Suor/funcy                                                       | https://                                     |
| gast                             | https://github.com/serge-sans-paille/gast/                                          | https://                                     |
| gau2grid                         | https://github.com/dgasmith/gau2grid                                                | https://                                     |
| gax-go                           | https://github.com/googleapis/gax-go/v2                                             | https://                                     |
| gdk-pixbuf                       | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           | https://                                     |
| gemmi                            | https://gemmi.readthedocs.io/en/latest/                                             | https://                                     |
| genproto                         | https://google.golang.org/genproto/googleapis                                       | https://                                     |
| geometric                        | https://openbase.com/python/geometric                                               | https://                                     |
| giflib                           | https://giflib.sourceforge.net                                                      | https://                                     |
| glib                             | https://docs.gtk.org/glib/                                                          | https://                                     |
| GLM Library                      | https://github.com/g-truc/glm                                                       | https://                                     |
| gls                              | https://github.com/jtolds/gls                                                       | https://                                     |
| go-cleanhttp                     | https://github.com/hashicorp/go-cleanhttp                                           | https://                                     |
| go-connections                   | https://github.com/docker/go-connections                                            | https://                                     |
| go-cpio                          | https://github.com/cavaliercoder/go-cpio                                            | https://                                     |
| go-getter                        | https://github.com/hashicorp/go-getter                                              | https://                                     |
| go-homedir                       | https://github.com/mitchellh/go-homedir                                             | https://                                     |
| go-ini                           | https://github.com/go-ini/ini                                                       | https://                                     |
| go-jmespath                      | https://github.com/jmespath/go-jmespath                                             | https://                                     |
| go-junit-report                  | https://github.com/jstemmer/go-junit-report                                         | https://                                     |
| go-netrc                         | https://github.com/bgentry/go-netrc/netrc                                           | https://                                     |
| go-ole                           | https://github.com/go-ole/go-ole                                                    | https://                                     |
| go-pg                            | https://github.com/go-pg/pg                                                         | https://                                     |
| go-redis                         | https://github.com/go-redis/redis/v8                                                | https://                                     |
| go-rendezvous                    | https://github.com/dgryski/go-rendezvous                                            | https://                                     |
| go-safetemp                      | https://github.com/hashicorp/go-safetemp                                            | https://                                     |
| go-sysconf                       | https://github.com/tklauser/go-sysconf                                              | https://                                     |
| go-testing-interface             | https://github.com/mitchellh/go-testing-interface                                   | https://                                     |
| go-units                         | https://github.com/docker/go-units                                                  | https://                                     |
| go-version                       | https://github.com/hashicorp/go-version                                             | https://                                     |
| go-zglob                         | https://github.com/mattn/go-zglob                                                   | https://                                     |
| go.opencensus                    | https://go.opencensus.io                                                            | https://                                     |
| gobrake.v2                       | https://gopkg.in/airbrake/gobrake.v2                                                | https://                                     |
| goconvey                         | https://github.com/smartystreets/goconvey                                           | https://                                     |
| golden-layout                    | https://github.com/deepstreamIO/golden-layout                                       | https://                                     |
| google-auth                      | https://google-auth.readthedocs.io/en/master/                                       | https://                                     |
| google-auth-oauthlib             | https://github.com/googleapis/google-auth-library-python-oauthlib                   | https://                                     |
| google-cloud-go                  | https://cloud.google.com/go                                                         | https://                                     |
| google-cloud-go/storage          | https://cloud.google.com/go/storage                                                 | https://                                     |
| google-pasta                     | https://github.com/google/pasta                                                     | https://                                     |
| google.golang.org/api            | https://google.golang.org/api                                                       | https://                                     |
| gopsutil                         | https://github.com/shirou/gopsutil                                                  | https://                                     |
| Name of Project                  | Website                                                                             | License                                      |
| gorilla websocket                | https://github.com/gorilla/websocket                                                |                                              |
| graphite2                        | https://github.com/silnrsi/graphite                                                 |                                              |
| graphviz                         | https://graphviz.org/                                                               |                                              |
| greenlet                         | https://greenlet.readthedocs.io/en/latest/                                          |                                              |
| groupcache                       | https://github.com/golang/groupcache                                                |                                              |
| grpc                             | https://google.golang.org/grpc                                                      |                                              |
| grpc-cpp                         | https://github.com/grpc/grpc                                                        |                                              |
| grpcio                           | https://github.com/grpc/grpc.io/blob/main/LICENSE                                   |                                              |
| gtk2                             | https://gitlab.gnome.org/GNOME/gtk                                                  |                                              |
| gts                              | https://sourceforge.net/projects/gts/                                               |                                              |
| h5py                             | https://www.h5py.org                                                                |                                              |
| harfbuzz                         | https://github.com/harfbuzz/harfbuzz                                                |                                              |
| hdbscan                          | https://hdbscan.readthedocs.io/en/latest/                                           |                                              |
| hdf4                             | https://www.hdfgroup.org/solutions/hdf4/                                            |                                              |
| hdf5                             | https://www.hdfgroup.org/solutions/hdf5/                                            |                                              |
| he                               | https://github.com/mathiasbynens/he                                                 |                                              |
| html-loader                      | https://github.com/webpack-contrib/html-loader                                      |                                              |
| html5lib                         | https://github.com/html5lib/html5lib-python                                         |                                              |
| htslib                           | https://www.htslib.org                                                              |                                              |
| humanize                         | https://github.com/jmoiron/humanize                                                 |                                              |
| icu                              | https://github.com/unicode-org/icu                                                  |                                              |
| idna                             | https://github.com/kjd/idna                                                         |                                              |
| imageio                          | https://github.com/imageio/imageio                                                  |                                              |
| imagesize                        | https://github.com/shibukawa/imagesize_py                                           |                                              |
| ImmuneBuilder                    | https://github.com/oxpig/ImmuneBuilder/tree/main                                    |                                              |
| importlib-metadata               | https://github.com/python/importlib_metadata                                        |                                              |
| importlib_resources              | https://github.com/python/importlib_resources                                       |                                              |
| InChI                            | https://iupac.org/who-we-are/divisions/division-details/inchi/                      |                                              |
| inflection                       | https://github.com/jinzhu/inflection                                                |                                              |
| ini.v1                           | https://gopkg.in/ini.v1                                                             |                                              |
| iniconfig                        | https://github.com/pytest-dev/iniconfig                                             |                                              |
| innersvg-polyfill                | https://github.com/dnozay/innersvg-polyfill                                         |                                              |
| intel-openmp                     | https://github.com/hermitcore/libomp_oss                                            |                                              |
| ipykernel                        | https://ipython.org                                                                 |                                              |
| ipython                          | https://ipython.org                                                                 |                                              |
| ipython-genutils                 | http://ipython.org                                                                  |                                              |
| ipywidgets                       | http://jupyter.org                                                                  |                                              |
| isodate                          | https://github.com/gweis/isodate/                                                   |                                              |
| itsdangerous                     | https://palletsprojects.com/p/itsdangerous/                                         |                                              |
| jax                              | https://github.com/google/jax                                                       |                                              |
| jaxlib                           | https://github.com/google/jax                                                       |                                              |
| jedi                             | https://jedi.readthedocs.io/en/latest/                                              |                                              |
| Jinja2                           | https://palletsprojects.com/p/jinja/                                                |                                              |
| jmespath                         | https://github.com/jmespath/jmespath.py                                             |                                              |
| joblib                           | https://joblib.readthedocs.io/en/latest/                                            |                                              |
| jpeg                             | https://www.ijg.org                                                                 |                                              |
| json5                            | https://github.com/dpranke/pyjson5                                                  |                                              |
| jsonfield                        | https://github.com/dmkoch/django-jsonfield/                                         |                                              |
| jsonpatch                        | https://github.com/stefankoegl/python-json-patch                                    |                                              |
|                                  | Website                                                                             |                                              |
| Name of Project                  |                                                                                     | Licen                                        |
| jsonpickle                       | https://github.com/jsonpickle/jsonpickle                                            | https:                                       |
| jsonpointer                      | https://github.com/stefankoegl/python-json-pointer                                  | https:                                       |
| jsonschema                       | https://github.com/python-jsonschema/jsonschema                                     | https:                                       |
| jsonschema-specifications        | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:                                       |
| jstat                            | https://github.com/jstat/jstat                                                      | https:                                       |
| jupyter-client                   | https://jupyter.org                                                                 | https:                                       |
| jupyter-core                     | https://jupyter.org                                                                 | https:                                       |
| jupyter-events                   | https://github.com/jupyter/jupyter_events                                           | https:                                       |
| jupyter-lsp                      | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:                                       |
| jupyter-serverhttp://jupyter.org | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE                  |                                              |
| jupyterlab                       | https://github.com/jupyterlab/jupyterlab                                            | https:                                       |
| jupyterlab-pygments              | http://jupyter.org                                                                  | https:                                       |
| jupyterlab-widgets               | http://jupyter.org                                                                  | https:                                       |
| jupyterlab_server                | https://github.com/jupyterlab/jupyterlab_server                                     | https:                                       |
| jupyter_client                   | http://jupyter.org                                                                  | https:                                       |
| jupyter_core                     | http://jupyter.org                                                                  | https:                                       |
| jupyter_server                   | https://github.com/jupyter-server/jupyter_server                                    | https:                                       |
| jupyter_server_terminals         | https://github.com/jupyter-server/jupyter_server_terminals                          | https:                                       |
| kaleido                          | https://github.com/plotly/Kaleido                                                   | https:                                       |
| keras                            | https://github.com/keras-team/keras                                                 | https:                                       |
| Keras-Preprocessing              | https://github.com/keras-team/keras-preprocessing                                   | https:                                       |
| keras-tuner                      | https://github.com/keras-team/keras-tuner                                           | https:                                       |
| keyring                          | https://github.com/jaraco/keyring                                                   | https:/                                      |
| keyutils                         | https://github.com/sassoftware/python-keyutils                                      | https:                                       |
| kiwisolver                       | https://kiwisolver.readthedocs.io/en/latest/                                        | https:                                       |
| kombu                            | https://kombu.readthedocs.io                                                        | https:                                       |
| $\overline{\text{krb5}}$         | https://web.mit.edu/kerberos/                                                       | https:                                       |
| kt-legacy                        | https://github.com/haifeng-jin/kt-legacy                                            | https:                                       |
| lazy_loader                      | https://github.com/scientific-python/lazy_loader                                    | https:                                       |
| lcms2                            | https://www.littlecms.com                                                           | https:                                       |
| lerc                             | https://github.com/Esri/lerc                                                        | https:                                       |
| libarchive                       | http://www.libarchive.org                                                           | https:                                       |
| libblas                          | https://www.netlib.org/blas/                                                        | https:                                       |
| libbrotlicommon                  | https://github.com/google/brotli                                                    | https:                                       |
| libbrotlidec                     | https://github.com/google/brotli                                                    | https:                                       |
| libbrotlienc                     | https://github.com/google/brotli                                                    | https:                                       |
| libcblas                         | https://anaconda.org/conda-forge/libcblas                                           | N/A                                          |
| libclang                         | <b>Orion Floes</b>                                                                  | https:                                       |
| libcurl                          | https://curl.se/libcurl/                                                            | https:/                                      |
| libcxx                           | https://github.com/llvm-mirror/libcxx                                               | https:                                       |
| libdb                            | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:                                       |
| libdeflate                       | https://github.com/ebiggers/libdeflate                                              | https:                                       |
| libedit                          | https://thrysoee.dk/editline/                                                       | http://                                      |
| libev                            | https://software.schmorp.de/pkg/libev.html                                          | https:/                                      |
| libffi                           | https://github.com/libffi/libffi                                                    | https:                                       |
| libgcrypt                        | https://gnupg.org/software/index.html                                               | https:                                       |
| libgd                            | https://libgd.github.io                                                             | https:                                       |
| libglib                          | https://github.com/PolMine/libglib                                                  |                                              |
| libiconv                         | https://www.gnu.org/software/libiconv/                                              | https:<br>https:                             |
|                                  |                                                                                     |                                              |
|                                  |                                                                                     | J.                                           |
| Name of Project                  | Website                                                                             | Licen                                        |
| libint                           | https://tinyurl.com/yvw97wbw                                                        | https:/                                      |
| liblapack                        | http://www.netlib.org/lapack/                                                       | https:/                                      |
| liblapacke                       | https://anaconda.org/conda-forge/liblapacke                                         | https:/                                      |
| libmamba                         | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https:/                                      |
| libmambapy                       | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https:/                                      |
| libnetcdf                        | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                      |
| libnghttp2                       | https://github.com/nghttp2/nghttp2                                                  | https:/                                      |
| libopenblas                      | https://www.openblas.net/                                                           | https:/                                      |
| libpng                           | https://www.libpng.org/pub/png/libpng.html                                          | https:/                                      |
| libpq                            | https://www.postgresql.org/                                                         | https:/                                      |
| librsvg                          | https://gitlab.gnome.org/GNOME/librsvg                                              | https:/                                      |
| libsolv                          | https://github.com/openSUSE/libsolv                                                 | https:/                                      |
| libssh2                          | https://github.com/libssh2/libssh2                                                  | https:/                                      |
| libtiff                          | https://www.libtiff.org/                                                            | https:/                                      |
| libtrust                         | https://github.com/docker/libtrust                                                  | https:/                                      |
| libuuid                          | https://sourceforge.net/projects/libuuid/                                           | https:/                                      |
| libuv                            | https://github.com/libuv/libuv                                                      | https:/                                      |
| libwebp                          | https://chromium.googlesource.com/?format=HTML                                      | https:/                                      |
| libwebp-base                     | https://chromium.googlesource.com/?format=HTML                                      | https:/                                      |
| libxc                            | https://www.tddft.org/programs/libxc/                                               | https:/                                      |
| libxcb                           | https://xcb.freedesktop.org                                                         | https:/                                      |
| libxml2                          | https://git.gnome.org/browse/libxml2/                                               | https:/                                      |
| libxmlsec1                       | https://github.com/lsh123/xmlsec                                                    | https:/                                      |
| libxslt                          | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https:/                                      |
| libzlib                          | https://zlib.net                                                                    | https:/                                      |
| lime                             | https://github.com/marcoter/lime                                                    | https:/                                      |
| $\overline{\text{lit}}$          | http://llvm.org                                                                     | https:/                                      |
| llvm-openmp                      | https://github.com/llvm-mirror/openmp                                               | https:/                                      |
| <b>Ilvmlite</b>                  | http://llvmlite.readthedocs.io                                                      | https:/                                      |
| loader-utils                     | https://github.com/webpack/loader-utils                                             | https:/                                      |
| logomaker                        | https://logomaker.readthedocs.io/en/latest/                                         | https:/                                      |
| logrus                           | https://github.com/sirupsen/logrus                                                  | https:/                                      |
| logrus-airbrake-hook.v2          | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https:/                                      |
| 1xml                             | https://lxml.de                                                                     | https:/                                      |
| $1z4-c$                          | https://www.lz4.org/                                                                | https:/                                      |
| markdown                         | https://github.com/evilstreak/markdown-js                                           | https:/                                      |
| markdown-it-py                   | Orion Floes                                                                         | https:/                                      |
| MarkupSafe                       | https://palletsprojects.com/p/markupsafe/                                           | https:/                                      |
| matplotlib                       | https://matplotlib.org                                                              | https:/                                      |
| matplotlib-base                  | https://matplotlib.org                                                              | https:/                                      |
| matplotlib-inline                | https://github.com/ipython/matplotlib-inline                                        | https:/                                      |
| mda-xdrlib                       | https://github.com/MDAnalysis/mda-xdrlib                                            | https:/                                      |
| mdtraj                           | https://www.mdtraj.org/                                                             | https:/                                      |
| mdurl                            | <b>Orion Floes</b>                                                                  | https:/                                      |
| menuinst                         | <b>Orion Floes</b>                                                                  | https:/                                      |
| mergo                            | https://github.com/imdario/mergo                                                    | https:/                                      |
| mistune                          | https://github.com/lepture/mistune                                                  | https:/                                      |
| mkl                              | https://github.com/rust-math/intel-mkl-src                                          | https:/                                      |
| mkl-fft                          | https://github.com/IntelPython/mkl_fft                                              | https:/                                      |
|                                  |                                                                                     |                                              |
| Name of Project                  | Website                                                                             | License                                      |
| mkl-random                       | https://github.com/IntelPython/mkl_random                                           | https://                                     |
| mkl-service                      | https://github.com/IntelPython/mkl-service                                          | https://                                     |
| ml-dtypes                        | <b>Orion Floes</b>                                                                  | https://                                     |
| molecupy                         | https://molecupy.readthedocs.io/en/latest/                                          | https://                                     |
| moment                           | https://github.com/moment/moment                                                    | https://                                     |
| moment-precise-range-plugin      | https://github.com/codebox/moment-precise-range                                     | https://                                     |
| more-itertools                   | https://github.com/more-itertools/more-itertools                                    | https://                                     |
| mpiplus                          | https://github.com/choderalab/mpiplus                                               | https://                                     |
| mpmath                           | http://mpmath.org/                                                                  | https://                                     |
| mrcfile                          | https://github.com/ccpem/mrcfile                                                    | https://                                     |
| msgpack                          | https://msgpack.org/                                                                | https://                                     |
| multidict                        | https://github.com/aio-libs/multidict                                               | https://                                     |
| multierr                         | https://go.uber.org/multierr                                                        | https://                                     |
| multiprocess                     | https://github.com/uqfoundation/multiprocess                                        | https://                                     |
| munkres                          | https://software.clapper.org/munkres/                                               | https://                                     |
| myesui uuid                      | https://github.com/myesui/uuid                                                      | https://                                     |
| namex                            | <b>Orion Floes</b>                                                                  | https://                                     |
| nbclassic                        | http://jupyter.org                                                                  | https://                                     |
| nbclient                         | https://jupyter.org                                                                 | https://                                     |
| nbconvert                        | https://jupyter.org                                                                 | https://                                     |
| nbformat                         | http://jupyter.org                                                                  | https://                                     |
| ncurses                          | https://invisible-island.net/ncurses/                                               | https://                                     |
| nest-asyncio                     | https://github.com/erdewit/nest_asyncio                                             | https://                                     |
| netcdf-fortran                   | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                     |
| netCDF4                          | http://github.com/Unidata/netcdf4-python                                            | https://                                     |
| nettle                           | https://git.lysator.liu.se/nettle/nettle                                            | https://                                     |
| networkx                         | https://networkx.org                                                                | https://                                     |
| nfpm                             | https://github.com/goreleaser/nfpm                                                  | https://                                     |
| ng-tags-input                    | https://github.com/mbenford/ngTagsInput                                             | https://                                     |
| ng-toast                         | https://github.com/tameraydin/ngToast                                               | https://                                     |
| ngdraggable                      | https://github.com/fatlinesofcode/ngDraggable                                       | https://                                     |
| ngVue                            | https://github.com/ngVue/ngVue                                                      | https://                                     |
| nlopt                            | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https://                                     |
| nodejs                           | https://nodejs.org/en/                                                              | https://                                     |
| nomkl                            | https://github.com/conda-forge/nomkl-feedstock                                      | https://                                     |
| notebook                         | http://jupyter.org                                                                  | https://                                     |
| notebook-shim                    | https://github.com/jupyter/notebook_shim                                            | https://                                     |
| notebook_shim                    | http://jupyter.org                                                                  | https://                                     |
| numba                            | https://numba.pydata.org                                                            | https://                                     |
| numcpus                          | https://github.com/tklauser/numcpus                                                 | https://                                     |
| numexpr                          | https://github.com/pydata/numexpr                                                   | https://                                     |
| numpy                            | https://numpy.org                                                                   | https://                                     |
| numpy-base                       | https://numpy.org                                                                   | https://                                     |
| numpydoc                         | https://numpydoc.readthedocs.io/en/latest/index.html                                | https://                                     |
| nvidia-cublas-cu11               | https://developer.nvidia.com/cuda-zone                                              | https://                                     |
| nvidia-cublas-cu12               | https://developer.nvidia.com/cuda-zone                                              | https://                                     |
| nvidia-cuda-cupti-cu11           | https://developer.nvidia.com/cuda-zone                                              | https://                                     |
| nvidia-cuda-cupti-cu12           | https://developer.nvidia.com/cuda-zone                                              | https://                                     |
| nvidia-cuda-nvrtc-cu11           | https://developer.nvidia.com/cuda-zone                                              | https://                                     |
| Name of Project                  | Website                                                                             | License                                      |
| nvidia-cuda-nvrtc-cu12           | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cuda-runtime-cu11         | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cuda-runtime-cu12         | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cudnn-cu11                | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cudnn-cu12                | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cufft-cu11                | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cufft-cu12                | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-curand-cu11               | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-curand-cu12               | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cusolver-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cusolver-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cusparse-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-cusparse-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-nccl-cu11                 | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-nccl-cu12                 | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-nvjitlink-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-nvtx-cu11                 | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| nvidia-nvtx-cu12                 | https://developer.nvidia.com/cuda-zone                                              | https:/                                      |
| Oat++                            | https://oatpp.io/                                                                   | https:/                                      |
| oauthlib                         | https://github.com/oauthlib/oauthlib                                                | https:/                                      |
| ocl-icd                          | https://github.com/OCL-dev/ocl-icd                                                  | https:/                                      |
| ocl-icd-system                   | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/                                      |
| olefile                          | https://www.decalage.info/python/olefileio                                          | https:/                                      |
| OmegaFold                        | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/                                      |
| omnicanvas                       | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/                                      |
| OpenFF                           | https://openforcefield.org/                                                         | https:/                                      |
| openff-amber-ff-ports            | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/                                      |
| openff-forcefields               | https://openforcefield.org                                                          | https:/                                      |
| openff-interchange               | https://github.com/openforcefield/openff-interchange                                | https:/                                      |
| openff-models                    | https://github.com/openforcefield/openff-models                                     | https:/                                      |
| openff-toolkit                   | https://openforcefield.org                                                          | https:/                                      |
| openff-toolkit-base              | https://openforcefield.org                                                          | https:/                                      |
| openff-units                     | https://github.com/openforcefield/openff-units                                      | https:/                                      |
| openff-utilities                 | https://github.com/openforcefield/openff-utilities                                  | https:/                                      |
| openjpeg                         | https://github.com/uclouvain/openjpeg                                               | https:/                                      |
| openldap                         | https://www.openldap.org/software/repo.html                                         | https:/                                      |
| OpenMM                           | https://openmm.org                                                                  | https:/                                      |
| openmmtools                      | https://github.com/choderalab/openmmtools                                           | https:/                                      |
| openmoltools                     | https://github.com/choderalab/openmoltools                                          | https:/                                      |
| openpyxl                         | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                      |
| openssl                          | https://www.openssl.org                                                             | https:/                                      |
| opt-einsum                       | https://github.com/dgasmith/opt_einsum                                              | https:/                                      |
| OptKing                          | https://github.com/psi-rking/optking                                                | https:/                                      |
| oscrypto                         | https://github.com/wbond/oscrypto                                                   | https:/                                      |
| overrides                        | https://github.com/mkorpela/overrides                                               | https:/                                      |
| packaging                        | https://github.com/pypa/packaging                                                   | https:/                                      |
| packmol                          | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                      |
| pandas                           | https://pandas.pydata.org                                                           | https:/                                      |
| pandocfilters                    | http://github.com/jgm/pandocfilters                                                 | https:/                                      |
|                                  |                                                                                     |                                              |
| Name of Project                  | Website                                                                             | License                                      |
| panedr                           | https://github.com/MDAnalysis/panedr                                                | https:/                                      |
| pango                            | https://pango.gnome.org                                                             | https:/                                      |
| ParmEd                           | https://parmed.github.io/ParmEd/html/index.html                                     | https:/                                      |
| parser                           | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                      |
| parso                            | https://parso.readthedocs.io/en/latest/                                             | https:/                                      |
| pathos                           | https://github.com/uqfoundation/pathos                                              | https:/                                      |
| patsy                            | https://patsy.readthedocs.io/en/latest/                                             | https:/                                      |
| pbkdf2                           | https://golang.org/x/crypto/pbkdf2                                                  | https:/                                      |
| pbr                              | https://docs.openstack.org/pbr/latest/                                              | https:/                                      |
| pcmsolver                        | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/                                      |
| pcre                             | https://www.pcre.org                                                                | https:/                                      |
| pcre2                            | https://www.pcre.org                                                                | https:/                                      |
| pdb4amber                        | https://github.com/Amber-MD/pdb4amber                                               | https:/                                      |
| pdbfixer                         | https://github.com/openmm/pdbfixer                                                  | https:/                                      |
| pexpect                          | https://pexpect.readthedocs.io/                                                     | https:/                                      |
| pgconn                           | https://github.com/jackc/pgconn                                                     | https:/                                      |
| pgio                             | https://github.com/jackc/pgio                                                       | https:/                                      |
| pgpassfile                       | https://github.com/jackc/pgpassfile                                                 | https:/                                      |
| pgproto3                         | https://github.com/jackc/pgproto3/v2                                                | https:/                                      |
| pgtype                           | https://github.com/jackc/pgtype                                                     | https:/                                      |
| pgx                              | https://github.com/jackc/pgx/v4                                                     | https:/                                      |
| phonopy                          | https://github.com/phonopy/phono3py                                                 | https:/                                      |
| pickleshare                      | https://github.com/pickleshare/pickleshare                                          | https:/                                      |
| Pillow                           | https://python-pillow.org                                                           | https:/                                      |
| Pint                             | https://pint.readthedocs.io/en/stable/                                              | https:/                                      |
| pip                              | https://pip.pypa.io/                                                                | https:/                                      |
| pip-licenses                     | https://github.com/raimon49/pip-licenses                                            | https:/                                      |
| pixman                           | https://pixman.org                                                                  | https:/                                      |
| pkginfo                          | https://launchpad.net/pkginfo                                                       | https:/                                      |
| platformdirs                     | https://github.com/platformdirs/platformdirs                                        | https:/                                      |
| plotly                           | https://plotly.com/python/                                                          | https:/                                      |
| plotly-orca                      | https://github.com/plotly/orca                                                      | https:/                                      |
| plotly.js                        | https://github.com/plotly/plotly.js                                                 | https:/                                      |
| pluggy                           | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/                                      |
| pooch                            | https://github.com/fatiando/pooch                                                   | https:/                                      |
| pox                              | https://github.com/uqfoundation/pox                                                 | https:/                                      |
| ppft                             | https://github.com/uqfoundation/ppft                                                | https:/                                      |
| pq                               | https://github.com/lib/pq                                                           | https:/                                      |
| ProDy                            | http://www.csb.pitt.edu/ProDy                                                       | https:/                                      |
| prometheus-client                | https://github.com/prometheus/client_python                                         | https:/                                      |
| prompt-toolkit                   | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/                                      |
| protobuf                         | https://google.golang.org/protobuf                                                  | https:/                                      |
| psi4                             | https://psicode.org                                                                 | https:/                                      |
| psutil                           | https://psutil.readthedocs.io/en/latest/                                            | https:/                                      |
| psycopg2                         | https://psycopg.org/                                                                | https:/                                      |
| PTable                           | https://github.com/kxxoling/PTable                                                  | https:/                                      |
| pthread-stubs                    | https://xcb.freedesktop.org                                                         | https:/                                      |
| ptyprocess                       | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/                                      |
| pure-eval                        | https://github.com/alexmojaki/pure_eval                                             | http://                                      |
| Name of Project                  | Website                                                                             | License                                      |
| py                               | https://py.readthedocs.io/en/latest/                                                | https:/                                      |
| py-cpuinfo                       | https://github.com/workhorsy/py-cpuinfo                                             | https:/                                      |
| pyasn1                           | https://github.com/etingof/pyasn1                                                   | https:/                                      |
| pyasn1-modules                   | https://github.com/etingof/pyasn1-modules                                           | https:/                                      |
| pybind11-abi                     | https://github.com/pybind/pybind11                                                  | https:/                                      |
| pycairo                          | https://pycairo.readthedocs.io/en/latest/index.html                                 | https:/                                      |
| pycosat                          | https://github.com/conda/pycosat                                                    | https:/                                      |
| pycparser                        | https://github.com/eliben/pycparser                                                 | https:/                                      |
| pydantic                         | https://pydantic-docs.helpmanual.io                                                 | https:/                                      |
| pydantic-core                    | https://github.com/pydantic/pydantic-core                                           | https:/                                      |
| pyedr                            | https://github.com/MDAnalysis/panedr                                                | https:/                                      |
| pyEMMA                           | http://github.com/markovmodel/PyEMMA                                                | https:/                                      |
| Pygments                         | https://pygments.org                                                                | https:/                                      |
| pygraphviz                       | https://pygraphviz.github.io                                                        | https:/                                      |
| pygtop                           | https://pygtop.readthedocs.io/en/latest/                                            | https:/                                      |
| pyHanko                          | https://github.com/MatthiasValvekens/pyHanko                                        | https:/                                      |
| pyhanko-certvalidator            | https://github.com/MatthiasValvekens/certvalidator                                  | https:/                                      |
| PyJWT                            | https://github.com/jpadilla/pyjwt                                                   | https:/                                      |
| pymbar                           | https://pymbar.org                                                                  | https:/                                      |
| pyOpenSSL                        | https://pyopenssl.org/                                                              | https:/                                      |
| pyparsing                        | https://pyparsing-docs.readthedocs.io/en/latest/                                    | https:/                                      |
| PyPDF3                           | https://github.com/sfneal/PyPDF3                                                    | https:/                                      |
| pyrsistent                       | http://github.com/tobgu/pyrsistent/                                                 | https:/                                      |
| pysam                            | https://github.com/pysam-developers/pysam                                           | https:/                                      |
| PySocks                          | https://github.com/Anorov/PySocks                                                   | https:/                                      |
| pytables                         | https://www.pytables.org                                                            | https:/                                      |
| python                           | https://www.python.org/                                                             | https:/                                      |
| python-bidi                      | https://github.com/MeirKriheli/python-bidi                                          | https:/                                      |
| python-constraint                | https://github.com/python-constraint/python-constraint                              | https:/                                      |
| python-dateutil                  | https://dateutil.readthedocs.io                                                     | https:/                                      |
| python-json-logger               | http://github.com/madzak/python-json-logger                                         | https:/                                      |
| python-ldap                      | https://www.python-ldap.org/                                                        | https:/                                      |
| python3-saml                     | https://github.com/onelogin/python3-saml                                            | https:/                                      |
| python_abi                       | https://github.com/conda-forge/python_abi-feedstock                                 | https:/                                      |
| pytz                             | https://pythonhosted.org/pytz                                                       | https:/                                      |
| pytz-deprecation-shim            | https://github.com/pganssle/pytz-deprecation-shim                                   | https:/                                      |
| PyWavelets                       | https://github.com/PyWavelets/pywt                                                  | https:/                                      |
| <b>PyYAML</b>                    | https://pyyaml.org/                                                                 | https:/                                      |
| pyyml                            | No longer available                                                                 | No license found                             |
| pyzmq                            | https://pyzmq.readthedocs.io/en/latest/                                             | https:/                                      |
| qcelemental                      | https://github.com/MolSSI/QCElemental                                               | https:/                                      |
| qcengine                         | https://github.com/MolSSI/QCEngine                                                  | https:/                                      |
| qrcode                           | https://github.com/lincolnloop/python-qrcode                                        | https:/                                      |
| ramda                            | https://github.com/ramda/ramda                                                      | https:/                                      |
| rapidjson                        | https://rapidjson.org/                                                              | https:/                                      |
| rdkit                            | https://www.rdkit.org                                                               | https:/                                      |
| re2                              | https://github.com/google/re2                                                       | https:/                                      |
| readme-renderer                  | https://github.com/pypa/readme_renderer                                             | https:/                                      |
| redis-py                         | https://github.com/andymccurdy/redis-py                                             | https:/                                      |
| Name of Project                  | Website                                                                             | License                                      |
| referencing                      | https://github.com/python-jsonschema/referencing                                    | https:/                                      |
| regex                            | https://github.com/mrabarnett/mrab-regex                                            | https:/                                      |
| reportlab                        | https://www.reportlab.com                                                           | https:/                                      |
| reproc                           | https://github.com/DaanDeMeyer/reproc                                               | https:/                                      |
| reproc-cpp                       | https://github.com/DaanDeMeyer/reproc                                               | https:/                                      |
| requests                         | https://requests.readthedocs.io                                                     | https:/                                      |
| requests-oauthlib                | https://github.com/requests/requests-oauthlib                                       | https:/                                      |
| requests-toolbelt                | https://toolbelt.readthedocs.org                                                    | https:/                                      |
| resumable                        | https://github.com/stevvooe/resumable                                               | https:/                                      |
| retrying                         | https://github.com/rholder/retrying                                                 | https:/                                      |
| rfc3339-validator                | https://github.com/naimetti/rfc3339-validator                                       | https:/                                      |
| rfc3986                          | https://rfc3986.readthedocs.io/en/latest/                                           | https:/                                      |
| rfc3986-validator                | https://github.com/naimetti/rfc3986-validator                                       | https:/                                      |
| rich                             | Orion Floes                                                                         | https:/                                      |
| rpds-py                          | https://github.com/crate-py/rpds                                                    | https:/                                      |
| rpmpack                          | https://github.com/google/rpmpack                                                   | https:/                                      |
| rsa                              | https://stuvel.eu/rsa                                                               | https:/                                      |
| ruamel-yaml                      | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https:/                                      |
| ruamel.yaml.clib                 | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https:/                                      |
| s3transfer                       | https://github.com/boto/s3transfer                                                  | https:/                                      |
| sasl                             | https://mellium.im/sasl                                                             | https:/                                      |
| scikit-gstat                     | https://mmaelicke.github.io/scikit-gstat/                                           | https:/                                      |
| scikit-image                     | https://scikit-image.org                                                            | https:/                                      |
| scikit-learn                     | https://scikit-learn.org/stable/                                                    | https:/                                      |
| scikit-learn-extra               | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https:/                                      |
| scipy                            | https://scipy.org                                                                   | https:/                                      |
| seaborn                          | https://seaborn.pydata.org                                                          | https:/                                      |
| seaborn-base                     | https://seaborn.pydata.org                                                          | https:/                                      |
| semver                           | https://github.com/Masterminds/semver/v3                                            | https:/                                      |
| Send2Trash                       | https://github.com/arsenetar/send2trash                                             | https:/                                      |
| setuptools                       | https://github.com/pypa/setuptools                                                  | https:/                                      |
| setuptools-scm                   | https://github.com/pypa/setuptools_scm/                                             | https:/                                      |
| sh                               | https://github.com/amoffat/sh                                                       | https:/                                      |
| shellingham                      | https://github.com/sarugaku/shellingham                                             | https:/                                      |
| simint                           | https://www.bennyp.org/research/simint/                                             | https:/                                      |
| six                              | https://github.com/benjaminp/six                                                    | https:/                                      |
| smirnoff99frosst                 | https://github.com/openforcefield/smirnoff99frosst                                  | https:/                                      |
| snappy                           | https://github.com/google/snappy                                                    | https:/                                      |
| sniffio                          | https://github.com/python-trio/sniffio                                              | https:/                                      |
| snowballstemmer                  | https://github.com/snowballstem/snowball                                            | https:/                                      |
| soupsieve                        | https://github.com/facelessuser/soupsieve                                           | https:/                                      |
| spglib                           | Orion Floes                                                                         | https:/                                      |
| sphinx                           | https://github.com/sphinx-doc/sphinx                                                | https:/                                      |
| sphinxcontrib-applehelp          | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https:/                                      |
| sphinxcontrib-devhelp            | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https:/                                      |
| sphinxcontrib-htmlhelp           | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https:/                                      |
| sphinxcontrib-jsmath             | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https:/                                      |
| sphinxcontrib-qthelp             | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https:/                                      |
| sphinxcontrib-serializinghtml    | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https:/                                      |
| Name of Project                  | Website                                                                             | License                                      |
| SQLAlchemy                       | https://www.sqlalchemy.org                                                          | https:/                                      |
| sqlite                           | https://sqlite.org/index.html                                                       | https:/                                      |
| sqlparse                         | https://github.com/andialbrecht/sqlparse                                            | https:/                                      |
| stack-data                       | https://github.com/alexmojaki/stack_data                                            | https:/                                      |
| starfile                         | https://github.com/alisterburt/starfile                                             | https:/                                      |
| statsmodels                      | https://github.com/statsmodels/statsmodels                                          | https:/                                      |
| structlog                        | https://www.structlog.org/                                                          | https:/                                      |
| svglib                           | https://github.com/deeplook/svglib                                                  | https:/                                      |
| sympy                            | https://sympy.org                                                                   | https:/                                      |
| tables                           | https://www.pytables.org/                                                           | https:/                                      |
| tabulate                         | https://github.com/astanin/python-tabulate                                          | https:/                                      |
| tbb                              | https://github.com/oneapi-src/oneTBB                                                | https:/                                      |
| tenacity                         | https://github.com/jd/tenacity                                                      | https:/                                      |
| tensorboard                      | https://github.com/tensorflow/tensorboard                                           | https:/                                      |
| tensorboard-data-server          | https://github.com/tensorflow/tensorboard                                           | https:/                                      |
| tensorboard-plugin-wit           | https://github.com/pair-code/what-if-tool                                           | https:/                                      |
| tensorflow                       | https://github.com/tensorflow/tensorflow                                            | https:/                                      |
| tensorflow-estimator             | https://github.com/tensorflow/estimator                                             | https:/                                      |
| tensorflow-io-gcs-filesystem     | <b>Orion Floes</b>                                                                  | https:/                                      |
| tensorflow-probability           | https://github.com/tensorflow/probability                                           | https:/                                      |
| termcolor                        | https://github.com/hugovk/termcolor                                                 | https:/                                      |
| terminado                        | https://github.com/jupyter/terminado                                                | https:/                                      |
| testpath                         | https://github.com/jupyter/testpath                                                 | https:/                                      |
| textangular                      | https://github.com/fraywing/textAngular                                             | https:/                                      |
| tf_keras                         | <b>Orion Floes</b>                                                                  | https:/                                      |
| threadpoolctl                    | https://github.com/joblib/threadpoolctl                                             | https:/                                      |
| three                            | https://github.com/mrdoob/three.js                                                  | https:/                                      |
| tifffile                         | https://github.com/cgohlke/tifffile/                                                | https:/                                      |
| tinycss2                         | https://github.com/Kozea/tinycss2/                                                  | https:/                                      |
| tinyxml2                         | https://github.com/leethomason/tinyxml2                                             | https:/                                      |
| tk                               | https://www.tcl.tk/                                                                 | https:/                                      |
| toml                             | https://github.com/toml-lang/toml                                                   | https:/                                      |
| tomli                            | https://github.com/hukkin/tomli                                                     | https:/                                      |
| toolz                            | https://github.com/pytoolz/toolz                                                    | https:/                                      |
| torch                            | https://pytorch.org/                                                                | https:/                                      |
| tornado                          | https://www.tornadoweb.org                                                          | https:/                                      |
| tqdm                             | https://github.com/tqdm/tqdm                                                        | https:/                                      |
| tracy                            | https://github.com/gear-genomics/tracy                                              | https:/                                      |
| traitlets                        | https://github.com/ipython/traitlets                                                | https:/                                      |
| triton                           | https://github.com/openai/triton/                                                   | https:/                                      |
| truststore                       | <b>Orion Floes</b>                                                                  | https:/                                      |
| ts-jest                          | https://github.com/kulshekhar/ts-jest                                               | https:/                                      |
| ts-loader                        | https://github.com/TypeStrong/ts-loader                                             | https:/                                      |
| twine                            | https://github.com/pypa/twine                                                       | https:/                                      |
| twinj uuid                       | https://github.com/twinj/uuid                                                       | https:/                                      |
| types                            | https://github.com/babel/babel                                                      | https:/                                      |
| typescript                       | https://github.com/Microsoft/TypeScript                                             | https:/                                      |
| typing_extensions                | https://github.com/python/typing                                                    | https:/                                      |
| tzdata                           | https://github.com/python/tzdata                                                    | https:/                                      |
| Name of Project                  | Website                                                                             | License                                      |
| tzlocal                          | https://github.com/regebro/tzlocal                                                  | https://                                     |
| umi-tools                        | https://github.com/CGATOxford/UMI-tools                                             | https://                                     |
| unicodedata2                     | https://github.com/fonttools/unicodedata2                                           | https://                                     |
| uritools                         | https://github.com/tkem/uritools/                                                   | https://                                     |
| urllib3                          | https://urllib3.readthedocs.io/                                                     | https://                                     |
| vine                             | https://github.com/celery/vine                                                      | https://                                     |
| vue                              | https://github.com/vuejs/vue                                                        | https://                                     |
| wcwidth                          | https://github.com/jquast/wcwidth                                                   | https://                                     |
| webencodings                     | https://github.com/gsnedders/python-webencodings                                    | https://                                     |
| websocket-client                 | https://github.com/websocket-client/websocket-client.git                            | https://                                     |
| Werkzeug                         | https://palletsprojects.com/p/werkzeug/                                             | https://                                     |
| westpa                           | Orion Floes                                                                         | http://                                      |
| wheel                            | https://github.com/pypa/wheel                                                       | https://                                     |
| widgetsnbextension               | https://github.com/jupyter-widgets/ipywidgets#readme                                | https://                                     |
| wrapt                            | https://github.com/GrahamDumpleton/wrapt                                            | https://                                     |
| wsutil                           | https://github.com/yhat/wsutil                                                      | https://                                     |
| x/lint                           | https://golang.org/x/lint                                                           | https://                                     |
| x/mod                            | https://golang.org/x/mod/semver                                                     | https://                                     |
| x/net                            | https://golang.org/x/net                                                            | https://                                     |
| x/oauth2                         | https://golang.org/x/oauth2                                                         | https://                                     |
| x/sys                            | https://golang.org/x/sys                                                            | https://                                     |
| x/text                           | https://golang.org/x/text                                                           | https://                                     |
| x/tools                          | https://golang.org/x/tools                                                          | https://                                     |
| x/xerrors                        | https://golang.org/x/xerrors                                                        | https://                                     |
| xhtml2pdf                        | http://github.com/xhtml2pdf/xhtml2pdf                                               | https://                                     |
| xlrd                             | https://github.com/python-excel/xlrd                                                | https://                                     |
| xmlsec                           | https://github.com/mehcode/python-xmlsec                                            | https://                                     |
| xmltodict                        | https://github.com/martinblech/xmltodict                                            | https://                                     |
| xorg-kbproto                     | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https://                                     |
| xorg-libice                      | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https://                                     |
| xorg-libsm                       | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https://                                     |
| xorg-libx11                      | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https://                                     |
| xorg-libxau                      | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https://                                     |
| xorg-libxdmcp                    | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https://                                     |
| xorg-libxext                     | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https://                                     |
| xorg-libxrender                  | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https://                                     |
| xorg-libxt                       | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https://                                     |
| xorg-renderproto                 | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https://                                     |
| xorg-xextproto                   | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https://                                     |
| xorg-xproto                      | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https://                                     |
| xxhash                           | https://github.com/cespare/xxhash/v2                                                | https://                                     |
| xz                               | https://github.com/ulikunitz/xz                                                     | https://                                     |
| yaml                             | https://pyyaml.org/                                                                 | https://                                     |
| yaml-cpp                         | https://github.com/jbeder/yaml-cpp                                                  | https://                                     |
| yaml.v2                          | https://gopkg.in/yaml.v2                                                            | https://                                     |
| yaml.v3                          | https://gopkg.in/yaml.v3                                                            | https://                                     |
| yarl                             | https://github.com/aio-libs/yarl/                                                   | https://                                     |
| yaspin                           | https://github.com/pavdmyt/yaspin                                                   | https://                                     |
| yfiles                           | https://www.yworks.com/products/yfiles                                              | comm                                         |
| Name of Project                  | Website                                                                             | License                                      |
| yml                              | https://pypi.org/project/yml/                                                       | N/A                                          |
| zap                              | https://go.uber.org/zap                                                             | https:/                                      |
| zipp                             | https://github.com/jaraco/zipp                                                      | https:/                                      |
| zlib                             | https://zlib.net/                                                                   | https:/                                      |
| zstandard                        | https://github.com/indygreg/python-zstandard                                        | https:/                                      |
| zstd                             | https://facebook.github.io/zstd/                                                    | https:/                                      |
| _libgcc_mutex                    | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:/                                      |
| _openmp_mutex                    | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:/                                      |

T

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
\rightarrow section 7 of the GNU General Public License,
version 3 ("GPLv3"). It applies to a given file (the "Runtime Library") that bears a
\rightarrownotice placed by the copyright holder
of the file stating that the file is governed by GPLv3 along with this Exception.
```

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise →based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL-→ compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

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

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS How to Apply These Terms to Your New Programs If you develop a new program, and you want it to be of the greatest possible use to the public, the best way to achieve this is to make it free software which everyone can redistribute and change under these terms. To do so, attach the following notices to the program. It is safest to attach them to the start of each source file to most effectively state the exclusion of warranty; and each file should have at least the "copyright" line and a pointer to where the full notice is found. <one line to give the program's name and a brief idea of what it does.> Copyright (C) <year> <name of author> This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>. Also add information on how to contact you by electronic and paper mail. If the program does terminal interaction, make it output a short notice like this when it starts in an interactive mode: <program> Copyright (C) <year> <name of author> This program comes with ABSOLUTELY NO WARRANTY; for details type 'show w'. This is free software, and you are welcome to redistribute it under certain conditions; type 'show c' for details. The hypothetical commands 'show w' and 'show c' should show the appropriate parts of the General Public License. Of course, your program's commands might be different; for a GUI interface, you would use an "about box". You should also get your employer (if you work as a programmer) or school, if any, to sign a "copyright disclaimer" for the program, if necessary. For more information on this, and how to apply and follow the GNU GPL, see <http://www.gnu.org/licenses/>. The GNU General Public License does not permit incorporating your program into proprietary programs. If your program is a subroutine library, you may consider it more useful to permit linking proprietary applications with (continues on next page)

```
the library. If this is what you want to do, use the GNU Lesser General
Public License instead of this License. But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.
```

#### See also:

• http://www.gnu.org/licenses/gpl.txt

## **INDEX**

## $\mathsf{A}$

Add OESiteHopper:: OESiteHopperDatabase, 14 AddDirectory OESiteHopper:: OESiteHopperDatabase, 14

GetColorTanimoto  $\mathsf C$ OESiteHopper:: OESiteHopperResults, Close 19 OESiteHopper:: OESiteHopperDatabase, GetDesignUnit OESiteHopper:: OESiteHopperDatabase, 14 14 Constructors OESiteHopper:: OESiteHopperScore, 21 OESiteHopper:: OESiteHopperDatabase, GetID 13 OESiteHopper::OESiteHopperDatabaseOption@ESiteHopper::OESiteHopperScore, 22 GetIDByTitle 15 OESiteHopper::OESiteHopperPatchOptions, OESiteHopper::OESiteHopperDatabase, 16 14 OESiteHopper:: OESiteHopperResults, GetMaxHits OESiteHopper:: OESiteHopperSearchOptions, 19 OESiteHopper:: OESiteHopperScore, 21 24 GetMaxMolIdx OESiteHopper:: OESiteHopperSearch, 23 OESiteHopper:: OESiteHopperSearchBase, OESiteHopper:: OESiteHopperDatabase, 24 15 OESiteHopper:: OESiteHopperSearchOptidestMolecule 24 OESiteHopper:: OESiteHopperDatabase, 15 CreateCopy OESiteHopper:: OESiteHopperDatabaseOptGetNCPU OESiteHopper:: OESiteHopperSearchOptions, 16 OESiteHopper:: OESiteHopperPatchOptions, 25 GetNormalizeAndRescore 18 OESiteHopper::OESiteHopperSearchOptions, OESiteHopper::OESiteHopperSearchOptions, 25 27 GetOptions F OESiteHopper:: OESiteHopperDatabase, 15 Example Code GetPatchOptions sitehopper\_build\_example.py, 8 OESiteHopper:: OESiteHopperDatabaseOptions,

16

GetPatchScore

G

GetColorForceField

19

19

GetColorScale

OESiteHopper:: OESiteHopperPatchOptions,

OESiteHopper:: OESiteHopperResults,

sitehopper\_database\_info.py, 9 sitehopper\_get\_designunit.py, 10 sitehopper\_search\_example.py,7

OESiteHopper:: OESiteHopperResults,

| 20                                                         | AddDirectory, 14                                      |
|------------------------------------------------------------|-------------------------------------------------------|
| GetRank                                                    | Close, 14                                             |
| OESiteHopper::OESiteHopperResults,                         | Constructors, 13                                      |
| 20                                                         | GetDesignUnit, 14                                     |
| GetResidueCutoff                                           | GetIDByTitle, 14                                      |
| OESiteHopper::OESiteHopperPatchOptions,                    | GetMaxMolIdx, 15                                      |
| 17                                                         | GetMolecule, 15                                       |
| GetScaleFactor                                             | GetOptions, 15                                        |
| OESiteHopper::OESiteHopperPatchOptions, 17                 | GetSequenceInfo, 15<br>GetTitle, 15                   |
| GetScoreCutoff                                             | Open, 13                                              |
| OESiteHopper::OESiteHopperSearchOptions, operator bool, 14 |                                                       |
| 25<br>GetSequenceCutoff                                    | OESiteHopper::OESiteHopperDatabaseMode, 27            |
|                                                            | OESiteHopper::OESiteHopperDatabaseMode::APPEND, 27    |
|                                                            | OESiteHopper::OESiteHopperDatabaseMode::CREATE, 27    |
|                                                            | OESiteHopper::OESiteHopperDatabaseMode::MAX, 27       |
|                                                            | OESiteHopper::OESiteHopperDatabaseMode::READONLY, 27  |
|                                                            | OESiteHopper::OESiteHopperDatabaseMode::SEARCH, 27    |
|                                                            | OESiteHopper::OESiteHopperDatabaseMode::UNDEFINED, 27 |
| 27<br>GetSequenceInfo                                      | OESiteHopper::OESiteHopperDatabase, 15                |
| GetSequenceSimilarity                                      | OESiteHopper::OESiteHopperDatabaseOptions, 28         |
| OESiteHopper::OESiteHopperResults, 20                      | Constructors, 15                                      |
| GetShapeTanimoto                                           | CreateCopy, 16                                        |
| OESiteHopper::OESiteHopperResults, 20                      | GetPatchOptions, 16                                   |
| 20                                                         | operator=, 16                                         |
| GetSiteSize                                                | SetPatchOptions, 16                                   |
| OESiteHopper::OESiteHopperPatchOptions, 17                 | OESiteHopper::OESiteHopperGetArch, 29                 |
| GetSurfaceCutoff                                           | OESiteHopper::OESiteHopperGetLicensee, 29             |
| OESiteHopper::OESiteHopperPatchOptions, 17                 | OESiteHopper::OESiteHopperGetPlatform, 29             |
| 17                                                         | OESiteHopper::OESiteHopperGetRelease, 29              |
| GetTitle                                                   | OESiteHopper::OESiteHopperGetSite, 30                 |
| OESiteHopper::OESiteHopperDatabase, 15                     | OESiteHopper::OESiteHopperGetVersion, 30              |
| 15                                                         | OESiteHopper::OESiteHopperIsGPUReady, 30              |
| OESiteHopper::OESiteHopperScore, 22<br>GetTransform        | OESiteHopper::OESiteHopperIsLicensed, 30              |
| OESiteHopper::OESiteHopperScore, 22<br>GetUseGPU           | OESiteHopper::OESiteHopperPatchOptions, 16            |
| 25                                                         | Constructors, 16                                      |
| GetUserStartsScaleFactor                                   | CreateCopy, 18                                        |
| OESiteHopper::OESiteHopperPatchOptions, 17                 | GetColorForceField, 19                                |
| O                                                          | GetResidueCutoff, 17                                  |
| OESiteHopper::OEAddPatchSurface, 28                        | GetScaleFactor, 17                                    |
| OESiteHopper::OEGetPatchSurface, 28                        |                                                       |
| OESiteHopper::OEHasPatchSurface, 28                        |                                                       |
| OESiteHopper::OEMakePatchFromDesignUnit, 28                |                                                       |
| OESiteHopper::OESetPatchSurface, 28                        |                                                       |
| OESiteHopper::OESetProteinSDData, 29                       |                                                       |
| OESiteHopper::OESiteHopperDatabase, 13                     |                                                       |
| Add, 14                                                    |                                                       |

GetSiteSize, 17 GetSurfaceCutoff.17 GetUserStartsScaleFactor, 17 operator=, 16 SetResidueCutoff, 17 SetScaleFactor, 18 SetSiteSize.18 SetSurfaceCutoff, 18 SetUserStartsScaleFactor, 18 OESiteHopper:: OESiteHopperResults, 19 Constructors, 19 GetColorScale, 19 GetColorTanimoto, 19 GetPatchScore, 20 GetRank, 20 GetSequenceSimilarity, 20 GetShapeTanimoto, 20 operator=, 19 SetColorScale, 20 SetColorTanimoto, 20 SetRank, 20 SetSequenceSimilarity, 21 SetShapeTanimoto, 21 OESiteHopper:: OESiteHopperScore, 21 Constructors, 21 GetDesignUnit, 21 GetID, 22 GetTitle, 22 GetTransform, 22 operator=, 21 SetDesignUnit, 22 SetID. 22 SetTitle, 22 SetTransform, 23 OESiteHopper:: OESiteHopperSearch, 23 Constructors, 23 operator bool, 23 Search, 23 OESiteHopper:: OESiteHopperSearchBase,  $23$ Constructors, 24 operator bool, 24 Search, 24 OESiteHopper:: OESiteHopperSearchOptions, SetNCPU  $24$ Constructors, 24 CreateCopy, 27 GetMaxHits, 24 GetNCPU<sub>25</sub> GetNormalizeAndRescore, 25 GetScoreCutoff, 25 GetSequenceCutoff, 25 GetUseGPU, 25 operator=, 26

SetMaxHits, 25 SetNCPU. 26 SetNormalizeAndRescore, 26 SetScoreCutoff, 26 SetSequenceCutoff, 26 Open OESiteHopper:: OESiteHopperDatabase, 13 operator bool OESiteHopper:: OESiteHopperDatabase, 14 OESiteHopper:: OESiteHopperSearch, 23 OESiteHopper:: OESiteHopperSearchBase, 24 operator= OESiteHopper:: OESiteHopperDatabaseOptions, 16 OESiteHopper:: OESiteHopperPatchOptions, 16 OESiteHopper:: OESiteHopperResults,  $19$ OESiteHopper:: OESiteHopperScore, 21 OESiteHopper:: OESiteHopperSearchOptions, 26

## S

```
Search
   OESiteHopper:: OESiteHopperSearch, 23
   OESiteHopper:: OESiteHopperSearchBase,
       24
SetColorScale
   OESiteHopper:: OESiteHopperResults,
       20SetColorTanimoto
   OESiteHopper:: OESiteHopperResults,
       20SetDesignUnit
   OESiteHopper:: OESiteHopperScore, 22
SetID
   OESiteHopper:: OESiteHopperScore, 22
SetMaxHits
   OESiteHopper:: OESiteHopperSearchOptions,
       25
   OESiteHopper:: OESiteHopperSearchOptions,
       26
SetNormalizeAndRescore
   OESiteHopper:: OESiteHopperSearchOptions,
       26
SetPatchOptions
   OESiteHopper:: OESiteHopperDatabaseOptions,
       16
SetRank
```

```
OESiteHopper:: OESiteHopperResults,
       20SetResidueCutoff
   OESiteHopper:: OESiteHopperPatchOptions,
       17
SetScaleFactor
   OESiteHopper:: OESiteHopperPatchOptions,
       18
SetScoreCutoff
   OESiteHopper:: OESiteHopperSearchOptions,
       26
SetSequenceCutoff
   OESiteHopper:: OESiteHopperSearchOptions,
      26
SetSequenceSimilarity
   OESiteHopper:: OESiteHopperResults,
       21
SetShapeTanimoto
   OESiteHopper:: OESiteHopperResults,
       21
SetSiteSize
   OESiteHopper:: OESiteHopperPatchOptions,
      18
SetSurfaceCutoff
   OESiteHopper:: OESiteHopperPatchOptions,
       18
SetTitle
   OESiteHopper:: OESiteHopperScore, 22
SetTransform
   OESiteHopper:: OESiteHopperScore, 23
SetUserStartsScaleFactor
   OESiteHopper:: OESiteHopperPatchOptions,
       18
sitehopper_build_example.py
   Example Code, 8
sitehopper_database_info.py
   Example Code, 9
sitehopper_get_designunit.py
   Example Code, 10
sitehopper_search_example.py
   Example Code, 7
```