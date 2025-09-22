![](_page_0_Picture_0.jpeg)

# **OpenEye Toolkits Release Notes -Python**

Release 2024.2.0

**Cadence Design Systems, Inc.** 

**December 03, 2024** 

# **CONTENTS**

| 1 |                                                                                              | <b>Copyright and Trademarks</b>                                                                                                                                                                                                                    | 1                                                                    |
|---|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| 2 |                                                                                              | <b>Sample Code</b>                                                                                                                                                                                                                                 | 2                                                                    |
| 3 | <b>Citation</b><br>3.1<br>3.2<br>3.3                                                         | Orion ® Floes<br>Toolkits and Applications<br>OpenEye Web Services                                                                                                                                                                                 | 3<br>3<br>3<br>3                                                     |
| 4 | 4.1                                                                                          | <b>Technology Licensing</b><br><b>GCC</b>                                                                                                                                                                                                          | 4<br>4                                                               |
| 5 | 5.1<br>5.2                                                                                   | <b>OEToolkits 2024.2</b><br>Release Highlights 2024.2.0<br>General Notices                                                                                                                                                                         | 39<br>39<br>42                                                       |
| 6 | 6.1<br>6.2<br>6.3<br>6.4<br>6.5<br>6.6<br>6.7<br>6.8<br>6.9<br>6.10                          | <b>Detailed Release Notes 2024.2</b><br>Bioisostere TK 4.1.0<br>OEChem TK 4.1.1<br>OEPlatform TK 4.1.1<br>OEBio TK 4.1.1<br>OEDepict TK 2.5.5<br>OEDocking TK 4.3.2<br>Eon TK 3.1.0<br>FastROCS TK 2.2.7<br>Grapheme TK 1.5.2<br>GraphSim TK 2.6.1 | 43<br>43<br>43<br>44<br>44<br>45<br>45<br>46<br>46<br>47             |
|   | 6.11<br>6.12<br>6.13<br>6.14<br>6.15<br>6.16<br>6.17<br>6.18<br>6.19<br>6.20<br>6.21<br>6.22 | Lexichem TK 2.9.2<br>OEMedChem TK 1.2.3<br>MolProp TK 2.6.5<br>OEFF TK 2.8.0<br>Omega TK 6.0.0<br>Quacpac TK 2.2.5<br>Shape TK 3.7.0<br>SiteHopper TK 2.1.1<br>Spicoli TK 1.6.1<br>Spruce TK 1.6.1<br>Szmap TK 1.7.1<br>Szybki TK 2.8.0            | 47<br>47<br>47<br>48<br>48<br>49<br>49<br>49<br>49<br>49<br>50<br>50 |
|   | 6.23                                                                                         | Zap TK 2.5.0                                                                                                                                                                                                                                       | 50                                                                   |

| 7 |      | <b>Recent Release History</b>   | 51  |
|---|------|---------------------------------|-----|
|   | 7.1  | OEToolkits 2024.1               | 51  |
|   | 7.2  | OEToolkits 2023.2               | 55  |
|   | 7.3  | OEToolkits 2023.1               | 57  |
|   | 7.4  | Release Highlights 2022.2       | 58  |
| 8 |      | <b>Previous Release History</b> | 63  |
|   | 8.1  | Release Highlights 2022.1       | 63  |
|   | 8.2  | Release Highlights 2021.2       | 66  |
|   | 8.3  | Release Highlights 2021.1       | 69  |
|   | 8.4  | Release Highlights 2020.2       | 72  |
|   | 8.5  | Release Highlights 2020.1       | 76  |
|   | 8.6  | OEToolkits 2019.Oct             | 81  |
|   | 8.7  | OEToolkits 2019.Apr             | 83  |
|   | 8.8  | OEToolkits 2018.Oct             | 85  |
|   | 8.9  | OEToolkits 2018.Feb.            | 87  |
|   | 8.10 | OEToolkits 2017.Oct             | 89  |
|   | 8.11 | OEToolkits 2017.Jun             | 90  |
|   | 8.12 | OEToolkits 2017.Feb.            | 92  |
|   | 8.13 | OEToolkits 2016.Oct             | 95  |
|   | 8.14 | OEToolkits 2016.Jun             | 96  |
|   | 8.15 | OEToolkits 2016.Feb             | 99  |
|   | 8.16 | OEToolkits 2015.Oct             | 101 |
|   | 8.17 | OEToolkits 2015.Jun             | 104 |
|   | 8.18 | OEToolkits 2015.Feb             | 107 |
|   | 8.19 | OEToolkits 2014.Oct             |     |
|   | 8.20 | OEToolkits 2014.Jun             |     |
|   | 8.21 | OEToolkits 2014.Feb.            |     |
|   | 8.22 | OEToolkits 2013.Oct             |     |
|   | 8.23 | OEToolkits 2013.Jun             |     |
|   | 8.24 | OEToolkits 2013.Feb.            |     |
|   | 8.25 | OEToolkits 2012.Oct             |     |
|   | 8.26 | OEToolkits 2012.Jun             |     |
|   | 8.27 | OEToolkits 2012.Feb             |     |
|   | 8.28 | OEToolkits 2011.Oct             |     |
|   | 8.29 | OEToolkits 2011.1               |     |
|   | 8.30 | OEToolkits 1.7.4                |     |
|   | 8.31 | OEToolkits 1.7.2                |     |
|   | 8.32 | OEToolkits 1.7.1                |     |
|   | 8.33 | OEToolkits 1.7.0                |     |

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

#### **CHAPTER**

# **SAMPLE CODE**

For all of the code examples and samples within OpenEye documents, the following terms of use apply.

TERMS FOR USE OF SAMPLE CODE

The software below ("Sample Code") is provided to current licensees or subscribers of OpenEye products or SaaS offerings (each a "Customer"). Customer is hereby permitted to use, copy, and modify the Sample Code, subject to these terms. OpenEye claims no rights to Customer's modifications. Modification of Sample Code is at Customer's sole and exclusive risk. Sample Code may require Customer to have a then current license or subscription to the applicable OpenEye offering.

THE SAMPLE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED. OPENEYE DISCLAIMS ALL WARRANTIES, INCLUDING, BUT NOT LIMITED TO, WARRANTIES OF MER-CHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.

In no event shall OpenEye be liable for any damages or liability in connection with the Sample Code or its use.

#### **CHAPTER**

### **THREE**

# **CITATION**

## 3.1 Orion<sup>®</sup> Floes

To cite use of an Orion-based Floe package, please use the following:

```
OpenEye <package-name> <version-number>. OpenEye, Cadence Molecular Sciences, Santa
→Fe, NM. http://www.eyesopen.com.
```

### For example:

```
OpenEye Classic Floes 0.11.2. OpenEye, Cadence Molecular Sciences, Santa Fe, NM.
\rightarrowhttp://www.eyesopen.com.
```

The version number for a Floe package is displayed on the first page of the package's release notes. For example: https://docs.eyesopen.com/floe/modules/classic-floes/docs/source/releasenotes.html.

## **3.2 Toolkits and Applications**

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

## **3.3 OpenEye Web Services**

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

### For example:

MaaS 1.0. OpenEye, Cadence Molecular Sciences, Santa Fe, NM. http://www.eyesopen.com.

The MaaS version number appears on the web service's release notes.

#### **CHAPTER**

# **FOUR**

# **TECHNOLOGY LICENSING**

OpenEye products use the following technology under license.

Some of the open source technologies we use are licensed under the GNU Public License (GPL) version 2 or 3. In all instances, these technologies are communicated with using the "at arms length" principle, using pipes and command line arguments.

While the software is in some instances assembled into a container, that assembly does not invoke the GPL copyleft scope. For each Floe package where these are used, the environment log clearly details the installed programs and their version numbers. With the links below for each technology, the source for each of those programs is available.

| Name of Project               | Website                                                               | License |
|-------------------------------|-----------------------------------------------------------------------|---------|
| abseil-cpp                    | https://github.com/abseil/abseil-cpp                                  | https:/ |
| absl-py                       | https://github.com/abseil/abseil-py                                   | https:/ |
| aiohttp                       | https://docs.aiohttp.org/en/stable/                                   | https:/ |
| aiosignal                     | https://github.com/aio-libs/aiosignal                                 | https:/ |
| Amazon Linux 2                | https://aws.amazon.com/amazon-linux-2                                 | N/A     |
| AmberUtils                    | http://ambermd.org                                                    | N/A     |
| ambit                         | https://github.com/khimaros/ambit                                     | https:/ |
| amqp                          | https://github.com/celery/py-amqp                                     | https:/ |
| anaconda-anon-usage           | Orion Floes                                                           | https:/ |
| angular                       | https://github.com/angular/angular.js                                 | https:/ |
| angular-animate               | https://github.com/angular/angular.js                                 | https:/ |
| angular-cache                 | https://github.com/jmdobry/angular-cache                              | https:/ |
| angular-cookies               | https://github.com/angular/angular.js                                 | https:/ |
| angular-loggly-logger         | https://github.com/ajbrown/angular-loggly-logger                      | https:/ |
| angular-mocks                 | https://github.com/angular/angular.js                                 | https:/ |
| angular-resource              | https://github.com/angular/angular.js                                 | https:/ |
| angular-toggle-switch         | https://github.com/cgarvis/angular-toggle-switch                      | https:/ |
| angular-ui-grid               | https://github.com/angular-ui/ui-grid                                 | https:/ |
| angular-ui-router             | https://github.com/angular-ui/ui-router                               | https:/ |
| angular-ui-tree               | https://github.com/angular-ui-tree/angular-ui-tree                    | https:/ |
| angular-vs-repeat             | https://github.com/kamilkp/angular-vs-repeat                          | https:/ |
| aniso8601                     | https://bitbucket.org/nielsenb/aniso8601                              | https:/ |
| annotated-types               | https://github.com/annotated-types/annotated-types                    | https:/ |
| anyio                         | https://github.com/agronholm/anyio                                    | https:/ |
| appdirs                       | http://github.com/ActiveState/appdirs                                 | http:// |
| appengine                     | https://google.golang.org/appengine                                   | https:/ |
| arabic-reshaper               | https://github.com/mpcabd/python-arabic-reshaper/                     | https:/ |
| archspec                      | https://github.com/archspec/archspec/blob/master/README.md            | https:/ |
| Name of Project               | Website                                                               | License |
| argon2-cffi                   | https://github.com/hynek/argon2-cffi                                  |         |
| argon2-cffi-bindings          | https://github.com/hynek/argon2-cffi-bindings                         |         |
| arpack                        | https://www.caam.rice.edu/software/ARPACK/                            |         |
| ascii85                       | https://github.com/huandu/node-ascii85                                |         |
| ase                           | https://wiki.fysik.dtu.dk/ase/                                        |         |
| asgiref                       | https://github.com/django/asgiref/                                    |         |
| asn1crypto                    | https://github.com/wbond/asn1crypto                                   |         |
| assertions go-render          | https://github.com/smartystreets/assertions/internal/go-render/render |         |
| assertions oglmatchers        | https://github.com/smartystreets/assertions/internal/oglematchers     |         |
| assertions                    | https://github.com/smartystreets/assertions                           |         |
| asttokens                     | https://github.com/gristlabs/asttokens                                |         |
| astunparse                    | https://github.com/simonpercivall/astunparse                          |         |
| async-lru                     | https://github.com/aio-libs/async-lru                                 |         |
| async-timeout                 | https://github.com/aio-libs/async-timeout                             |         |
| atk-1.0                       | https://docs.gtk.org/atk/                                             |         |
| atomic                        | https://github.com/uber-go/atomic                                     |         |
| atomicwrites                  | https://github.com/untitaker/python-atomicwrites                      |         |
| attrs                         | https://www.attrs.org/                                                |         |
| aws-sdk-go                    | https://github.com/aws/aws-sdk-go                                     |         |
| Babel                         | https://github.com/python-babel/babel                                 |         |
| backcall                      | https://github.com/takluyver/backcall                                 |         |
| backports                     | https://github.com/brandon-rhodes/backports                           |         |
| backports.functools-lru-cache | https://github.com/jaraco/backports.functools_lru_cache               |         |
| base62                        | https://github.com/kare/base62                                        |         |
| beautifulsoup4                | https://www.crummy.com/software/BeautifulSoup/                        |         |
| billiard                      | https://github.com/celery/billiard                                    |         |
| biopython                     | https://biopython.org                                                 |         |
| biotite                       | https://github.com/biotite-dev/biotite/blob/master/README.rst         |         |
| bitset                        | https://github.com/willf/bitset                                       |         |
| blas                          | https://www.netlib.org/blas/                                          |         |
| bleach                        | https://github.com/mozilla/bleach                                     |         |
| blessings                     | https://github.com/erikrose/blessings                                 |         |
| blinker                       | https://pythonhosted.org/blinker/                                     |         |
| blosc                         | https://github.com/Blosc/python-blosc                                 |         |
| blosc2                        | https://github.com/Blosc/python-blosc2                                |         |
| boltons                       | https://github.com/mahmoud/boltons                                    |         |
| boost                         | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html |         |
| boost-cpp                     | https://www.boost.org/doc/libs/1_71_0/libs/python/doc/html/index.html |         |
| bootstrap-vue                 | https://github.com/bootstrap-vue/bootstrap-vue                        |         |
| boto3                         | https://github.com/boto/boto3                                         |         |
| botocore                      | https://github.com/boto/botocore                                      |         |
| Bottleneck                    | https://bottleneck.readthedocs.io/en/latest/index.html                |         |
| Brotli                        | https://github.com/google/brotli                                      |         |
| brotli-bin                    | https://github.com/google/brotli                                      |         |
| brotli-python                 | http://python-hyper.org/projects/brotlipy/en/latest/                  |         |
| brotlipy                      | https://github.com/python-hyper/brotlicffi                            |         |
| bson                          | http://github.com/py-bson/bson                                        |         |
| bytefmt                       | https://code.cloudfoundry.org/bytefmt                                 |         |
| bzip2                         | https://www.bzip.org                                                  |         |

| Name of Project               | Website                                                                             |                                                                    |
|-------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| c-ares                        | https://github.com/c-ares/c-ares                                                    |                                                                    |
| ca-certificates               | https://github.com/conda-forge/ca-certificates-feedstock                            |                                                                    |
| cached-property               | https://github.com/pydanny/cached-property                                          |                                                                    |
| cachetools                    | https://github.com/tkem/cachetools                                                  |                                                                    |
| cairo                         | https://pycairo.readthedocs.io/en/latest/                                           |                                                                    |
| canvas                        | https://github.com/Automattic/node-canvas                                           |                                                                    |
| cctbx                         | https://github.com/cctbx/cctbx_project                                              |                                                                    |
| celery                        | https://github.com/celery/celery                                                    |                                                                    |
| Cerberus                      | https://docs.python-cerberus.org/en/stable/                                         |                                                                    |
| certifi                       | https://certifi.readthedocs.io/en/latest/                                           |                                                                    |
| cffi                          | https://github.com/python-cffi/cffi                                                 |                                                                    |
| cftime                        | https://pypi.org/project/cftime/                                                    |                                                                    |
| chardet                       | https://github.com/chardet/chardet                                                  |                                                                    |
| charset-normalizer            | https://github.com/Ousret/charset_normalizer                                        |                                                                    |
| chunkreader                   | https://github.com/jackc/chunkreader/v2                                             |                                                                    |
| click                         | https://palletsprojects.com/p/click/                                                |                                                                    |
| click-completion              | https://github.com/click-contrib/click-completion                                   |                                                                    |
| click-didyoumean              | https://github.com/click-contrib/click-didyoumean                                   |                                                                    |
| click-plugins                 | https://github.com/click-contrib/click-plugins                                      |                                                                    |
| click-repl                    | https://github.com/untitaker/click-repl                                             |                                                                    |
| cloudpickle                   | https://github.com/cloudpipe/cloudpickle                                            |                                                                    |
| cmake                         | https://cmake.org/                                                                  |                                                                    |
| colorama                      | https://github.com/tartley/colorama                                                 |                                                                    |
| comm                          | https://github.com/ipython/comm                                                     |                                                                    |
| compose                       | https://github.com/docker/compose                                                   |                                                                    |
| conda-content-trust           | https://github.com/conda/conda-content-trust                                        |                                                                    |
| conda-libmamba-solver         | https://github.com/conda/conda-libmamba-solver                                      |                                                                    |
| conda-package-handling        | https://github.com/conda/conda-package-handling                                     |                                                                    |
| conda-package-streaming       | https://anaconda.org/conda-forge/conda-package-streaming                            |                                                                    |
| conda-token                   | https://anaconda.org/anaconda/conda-token                                           |                                                                    |
| confuse                       | https://github.com/beetbox/confuse                                                  |                                                                    |
| contourpy                     | https://github.com/contourpy/contourpy                                              |                                                                    |
| cpp-peglib                    | https://github.com/yhirose/cpp-peglib                                               |                                                                    |
| cryptography                  | https://github.com/pyca/cryptography                                                |                                                                    |
| cssselect2                    | https://github.com/Kozea/cssselect2                                                 |                                                                    |
| cudatoolkit                   | https://developer.nvidia.com/cuda-toolkit                                           |                                                                    |
| cupy-cuda113                  | https://cupy.dev/                                                                   |                                                                    |
| curl                          | https://curl.se                                                                     |                                                                    |
| cycler                        | https://github.com/matplotlib/cycler                                                |                                                                    |
| cyrus-sasl                    | https://github.com/cyrusimap/cyrus-sasl                                             |                                                                    |
| Cython                        | https://cython.org                                                                  |                                                                    |
| d3                            | https://github.com/mbostock/d3                                                      |                                                                    |
| dataclasses                   | https://github.com/ericvsmith/dataclasses                                           |                                                                    |
| ddsketch                      | https://github.com/datadog/sketches-py                                              |                                                                    |
| debugpy                       | https://aka.ms/debugpy                                                              |                                                                    |
| decimal                       | https://github.com/shopspring/decimal                                               |                                                                    |
| decorator                     | https://github.com/micheles/decorator                                               |                                                                    |
| deepdiff                      | https://github.com/seperman/deepdiff                                                |                                                                    |
| deeptime                      | https://github.com/deeptime-ml/deeptime                                             |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| defusedxml                    | https://github.com/tiran/defusedxml                                                 | https://                                                           |
| dill                          | https://github.com/uqfoundation/dill                                                | https://                                                           |
| distro                        | Orion Floes                                                                         | https://                                                           |
| Django                        | https://www.djangoproject.com/                                                      | https://                                                           |
| django-classy-tags            | https://github.com/django-cms/django-classy-tags                                    | https://                                                           |
| django-cors-headers           | https://github.com/adamchainz/django-cors-headers                                   | https://                                                           |
| django-csp                    | https://github.com/mozilla/django-csp                                               | https://                                                           |
| django-extensions             | https://github.com/django-extensions/django-extensions                              | https://                                                           |
| django-filter                 | https://github.com/carltongibson/django-filter/tree/master                          | https://                                                           |
| django-redis                  | https://github.com/jazzband/django-redis                                            | https://                                                           |
| django-taggit                 | https://github.com/jazzband/django-taggit                                           | https://                                                           |
| django-taggit-serializer      | https://github.com/glemmaPaul/django-taggit-serializer                              | https://                                                           |
| django-taggit-templatetags2   | https://github.com/fizista/django-taggit-templatetags2                              | https://                                                           |
| djangorestframework           | https://www.django-rest-framework.org/                                              | https://                                                           |
| dkh                           | https://psicode.org/psi4manual/master/dkh.html                                      | https://                                                           |
| dm-tree                       | https://github.com/deepmind/tree                                                    | https://                                                           |
| docker-py                     | https://github.com/docker/docker-py/                                                | https://                                                           |
| docopt                        | https://docopt.org                                                                  | https://                                                           |
| docutils                      | https://docutils.sourceforge.io                                                     | https://                                                           |
| drf-dynamic-fields            | https://github.com/dbrgn/drf-dynamic-fields                                         | https://                                                           |
| editdistance                  | https://github.com/roy-ht/editdistance                                              | https://                                                           |
| eigen                         | https://eigen.tuxfamily.org/index.php?title=Main_Page                               | https://                                                           |
| einops                        | https://github.com/arogozhnikov/einops                                              | https://                                                           |
| entrypoints                   | https://github.com/takluyver/entrypoints                                            | https://                                                           |
| errors                        | https://github.com/pkg/errors                                                       | https://                                                           |
| eslint-plugin                 | https://github.com/typescript-eslint/typescript-eslint                              | https://                                                           |
| et_xmlfile                    | https://foss.heptapod.net/openpyxl/et_xmlfile                                       | https://                                                           |
| exceptiongroup                | https://github.com/agronholm/exceptiongroup                                         | https://                                                           |
| executing                     | https://github.com/alexmojaki/executing                                             | https://                                                           |
| expat                         | https://libexpat.github.io                                                          | https://                                                           |
| fastjsonschema                | https://github.com/horejsek/python-fastjsonschema                                   | https://                                                           |
| fastrlock                     | https://github.com/scoder/fastrlock                                                 | https://                                                           |
| fftw                          | https://www.fftw.org                                                                | comm                                                               |
| filebuffer                    | https://github.com/mattetti/filebuffer                                              | https://                                                           |
| filelock                      | https://py-filelock.readthedocs.io/en/latest/index.html                             | https://                                                           |
| finufft                       | https://github.com/flatironinstitute/finufft                                        | https://                                                           |
| Flask                         | https://flask.palletsprojects.com/en/2.1.x/                                         | https://                                                           |
| flatbuffers                   | https://google.github.io/flatbuffers/                                               | https://                                                           |
| flit-core                     | https://github.com/pypa/flit                                                        | https://                                                           |
| FLTK                          | https://www.fltk.org/index.php                                                      | https://                                                           |
| fmt                           | https://fmt.dev/latest/index.html                                                   | https://                                                           |
| font-awesome                  | https://github.com/FortAwesome/Font-Awesome                                         | https://                                                           |
| font-ttf-dejavu-sans-mono     | https://dejavu-fonts.github.io                                                      | https://                                                           |
| font-ttf-inconsolata          | https://fonts.google.com/specimen/Inconsolata                                       | https://                                                           |
| font-ttf-source-code-pro      | https://fonts.google.com/specimen/Source+Code+Pro                                   | https://                                                           |
| font-ttf-ubuntu               | https://fonts.google.com/specimen/Ubuntu                                            | https://                                                           |
| fontconfig                    | https://www.freedesktop.org/wiki/Software/fontconfig/                               | https://                                                           |
| fonts-conda-ecosystem         | https://anaconda.org/conda-forge/fonts-conda-ecosystem/                             | https://                                                           |
| fonts-conda-forge             | https://anaconda.org/conda-forge/fonts-conda-forge/                                 | https://                                                           |
| Name of Project               | Website                                                                             |                                                                    |
| fonttools                     | https://github.com/fonttools/fonttools                                              |                                                                    |
| freetype                      | https://freetype.org                                                                |                                                                    |
| fribidi                       | https://github.com/fribidi/fribidi                                                  |                                                                    |
| frozendict                    | Orion Floes                                                                         |                                                                    |
| frozenlist                    | https://github.com/aio-libs/frozenlist                                              |                                                                    |
| fsmlite                       | https://github.com/tkem/fsmlite                                                     |                                                                    |
| fsspec                        | https://github.com/fsspec/filesystem_spec                                           |                                                                    |
| funcy                         | https://github.com/Suor/funcy                                                       |                                                                    |
| gast                          | https://github.com/serge-sans-paille/gast/                                          |                                                                    |
| gau2grid                      | https://github.com/dgasmith/gau2grid                                                |                                                                    |
| gax-go                        | https://github.com/googleapis/gax-go/v2                                             |                                                                    |
| gdk-pixbuf                    | https://gitlab.gnome.org/GNOME/gdk-pixbuf                                           |                                                                    |
| gemmi                         | https://gemmi.readthedocs.io/en/latest/                                             |                                                                    |
| genproto                      | https://google.golang.org/genproto/googleapis                                       |                                                                    |
| geometric                     | https://openbase.com/python/geometric                                               |                                                                    |
| giflib                        | https://giflib.sourceforge.net                                                      |                                                                    |
| glib                          | https://docs.gtk.org/glib/                                                          |                                                                    |
| GLM Library                   | https://github.com/g-truc/glm                                                       |                                                                    |
| gls                           | https://github.com/jtolds/gls                                                       |                                                                    |
| go-cleanhttp                  | https://github.com/hashicorp/go-cleanhttp                                           |                                                                    |
| go-connections                | https://github.com/docker/go-connections                                            |                                                                    |
| go-cpio                       | https://github.com/cavaliercoder/go-cpio                                            |                                                                    |
| go-getter                     | https://github.com/hashicorp/go-getter                                              |                                                                    |
| go-homedir                    | https://github.com/mitchellh/go-homedir                                             |                                                                    |
| go-ini                        | https://github.com/go-ini/ini                                                       |                                                                    |
| go-jmespath                   | https://github.com/jmespath/go-jmespath                                             |                                                                    |
| go-junit-report               | https://github.com/jstemmer/go-junit-report                                         |                                                                    |
| go-netrc                      | https://github.com/bgentry/go-netrc/netrc                                           |                                                                    |
| go-ole                        | https://github.com/go-ole/go-ole                                                    |                                                                    |
| go-pg                         | https://github.com/go-pg/pg                                                         |                                                                    |
| go-redis                      | https://github.com/go-redis/redis/v8                                                |                                                                    |
| go-rendezvous                 | https://github.com/dgryski/go-rendezvous                                            |                                                                    |
| go-safetemp                   | https://github.com/hashicorp/go-safetemp                                            |                                                                    |
| go-sysconf                    | https://github.com/tklauser/go-sysconf                                              |                                                                    |
| go-testing-interface          | https://github.com/mitchellh/go-testing-interface                                   |                                                                    |
| go-units                      | https://github.com/docker/go-units                                                  |                                                                    |
| go-version                    | https://github.com/hashicorp/go-version                                             |                                                                    |
| go-zglob                      | https://github.com/mattn/go-zglob                                                   |                                                                    |
| go.opencensus                 | https://go.opencensus.io                                                            |                                                                    |
| gobrake.v2                    | https://gopkg.in/airbrake/gobrake.v2                                                |                                                                    |
| goconvey                      | https://github.com/smartystreets/goconvey                                           |                                                                    |
| golden-layout                 | https://github.com/deepstreamIO/golden-layout                                       |                                                                    |
| google-auth                   | https://google-auth.readthedocs.io/en/master/                                       |                                                                    |
| google-auth-oauthlib          | https://github.com/googleapis/google-auth-library-python-oauthlib                   |                                                                    |
| google-cloud-go               | https://cloud.google.com/go                                                         |                                                                    |
| google-cloud-go/storage       | https://cloud.google.com/go/storage                                                 |                                                                    |
| google-pasta                  | https://github.com/google/pasta                                                     |                                                                    |
| google.golang.org/api         | https://google.golang.org/api                                                       |                                                                    |
| gopsutil                      | https://github.com/shirou/gopsutil                                                  |                                                                    |
| Name of Project               | Website                                                                             |                                                                    |
| gorilla websocket             | https://github.com/gorilla/websocket                                                |                                                                    |
| graphite2                     | https://github.com/silnrsi/graphite                                                 |                                                                    |
| graphviz                      | https://graphviz.org/                                                               |                                                                    |
| greenlet                      | https://greenlet.readthedocs.io/en/latest/                                          |                                                                    |
| groupcache                    | https://github.com/golang/groupcache                                                |                                                                    |
| grpc                          | https://google.golang.org/grpc                                                      |                                                                    |
| grpc-cpp                      | https://github.com/grpc/grpc                                                        |                                                                    |
| grpcio                        | https://github.com/grpc/grpc/blob/main/LICENSE                                      |                                                                    |
| gtk2                          | https://gitlab.gnome.org/GNOME/gtk                                                  |                                                                    |
| gts                           | https://sourceforge.net/projects/gts/                                               |                                                                    |
| h5py                          | https://www.h5py.org                                                                |                                                                    |
| harfbuzz                      | https://github.com/harfbuzz/harfbuzz                                                |                                                                    |
| hdbscan                       | https://hdbscan.readthedocs.io/en/latest/                                           |                                                                    |
| hdf4                          | https://www.hdfgroup.org/solutions/hdf4/                                            |                                                                    |
| hdf5                          | https://www.hdfgroup.org/solutions/hdf5/                                            |                                                                    |
| he                            | https://github.com/mathiasbynens/he                                                 |                                                                    |
| html-loader                   | https://github.com/webpack-contrib/html-loader                                      |                                                                    |
| html5lib                      | https://github.com/html5lib/html5lib-python                                         |                                                                    |
| htslib                        | https://www.htslib.org                                                              |                                                                    |
| humanize                      | https://github.com/jmoiron/humanize                                                 |                                                                    |
| icu                           | https://github.com/unicode-org/icu                                                  |                                                                    |
| idna                          | https://github.com/kjd/idna                                                         |                                                                    |
| imageio                       | https://github.com/imageio/imageio                                                  |                                                                    |
| imagesize                     | https://github.com/shibukawa/imagesize_py                                           |                                                                    |
| ImmuneBuilder                 | https://github.com/oxpig/ImmuneBuilder/tree/main                                    |                                                                    |
| importlib-metadata            | https://github.com/python/importlib_metadata                                        |                                                                    |
| importlib_resources           | https://github.com/python/importlib_resources                                       |                                                                    |
| InChI                         | https://iupac.org/who-we-are/divisions/division-details/inchi/                      |                                                                    |
| inflection                    | https://github.com/jinzhu/inflection                                                |                                                                    |
| ini.v1                        | https://gopkg.in/ini.v1                                                             |                                                                    |
| iniconfig                     | https://github.com/pytest-dev/iniconfig                                             |                                                                    |
| innersvg-polyfill             | https://github.com/dnozay/innersvg-polyfill                                         |                                                                    |
| intel-openmp                  | https://github.com/hermitcore/libomp_oss                                            |                                                                    |
| ipykernel                     | https://ipython.org                                                                 |                                                                    |
| ipython                       | https://ipython.org                                                                 |                                                                    |
| ipython-genutils              | http://ipython.org                                                                  |                                                                    |
| ipywidgets                    | http://jupyter.org                                                                  |                                                                    |
| isodate                       | https://github.com/gweis/isodate/                                                   |                                                                    |
| itsdangerous                  | https://palletsprojects.com/p/itsdangerous/                                         |                                                                    |
| jax                           | https://github.com/google/jax                                                       |                                                                    |
| jaxlib                        | https://github.com/google/jax                                                       |                                                                    |
| jedi                          | https://jedi.readthedocs.io/en/latest/                                              |                                                                    |
| Jinja2                        | https://palletsprojects.com/p/jinja/                                                |                                                                    |
| jmespath                      | https://github.com/jmespath/jmespath.py                                             |                                                                    |
| joblib                        | https://joblib.readthedocs.io/en/latest/                                            |                                                                    |
| jpeg                          | https://www.ijg.org                                                                 |                                                                    |
| json5                         | https://github.com/dpranke/pyjson5                                                  |                                                                    |
| jsonfield                     | https://github.com/dmkoch/django-jsonfield/                                         |                                                                    |
| jsonpatch                     | https://github.com/stefankoegl/python-json-patch                                    |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| jsonpickle                    | https://github.com/jsonpickle/jsonpickle                                            | https:                                                             |
| jsonpointer                   | https://github.com/stefankoegl/python-json-pointer                                  | https:                                                             |
| jsonschema                    | https://github.com/python-jsonschema/jsonschema                                     | https:                                                             |
| jsonschema-specifications     | https://github.com/python-jsonschema/jsonschema-specifications/blob/main/README.rst | https:                                                             |
| jstat                         | https://github.com/jstat/jstat                                                      | https:                                                             |
| jupyter-client                | https://jupyter.org                                                                 | https:                                                             |
| jupyter-core                  | https://jupyter.org                                                                 | https:                                                             |
| jupyter-events                | https://github.com/jupyter/jupyter_events                                           | https:                                                             |
| jupyter-lsp                   | https://github.com/jupyter-lsp/jupyterlab-lsp                                       | https:                                                             |
| jupyter-server                | http://jupyter.org                                                                  | https://github.com/jupyter-server/jupyter_server/blob/main/LICENSE |
| jupyterlab                    | https://github.com/jupyterlab/jupyterlab                                            | https:                                                             |
| jupyterlab-pygments           | http://jupyter.org                                                                  | https:                                                             |
| jupyterlab-widgets            | http://jupyter.org                                                                  | https:                                                             |
| jupyterlab_server             | https://github.com/jupyterlab/jupyterlab_server                                     | https:                                                             |
| jupyter_client                | http://jupyter.org                                                                  | https:                                                             |
| jupyter_core                  | http://jupyter.org                                                                  | https:                                                             |
| jupyter_server                | https://github.com/jupyter-server/jupyter_server                                    | https:                                                             |
| jupyter_server_terminals      | https://github.com/jupyter-server/jupyter_server_terminals                          | https:                                                             |
| kaleido                       | https://github.com/plotly/Kaleido                                                   | https:                                                             |
| keras                         | https://github.com/keras-team/keras                                                 | https:                                                             |
| Keras-Preprocessing           | https://github.com/keras-team/keras-preprocessing                                   | https:                                                             |
| keras-tuner                   | https://github.com/keras-team/keras-tuner                                           | https:                                                             |
| keyring                       | https://github.com/jaraco/keyring                                                   | https:                                                             |
| keyutils                      | https://github.com/sassoftware/python-keyutils                                      | https:                                                             |
| kiwisolver                    | https://kiwisolver.readthedocs.io/en/latest/                                        | https:                                                             |
| kombu                         | https://kombu.readthedocs.io                                                        | https:                                                             |
| krb5                          | https://web.mit.edu/kerberos/                                                       | https:                                                             |
| kt-legacy                     | https://github.com/haifeng-jin/kt-legacy                                            | https:                                                             |
| lazy_loader                   | https://github.com/scientific-python/lazy_loader                                    | https:                                                             |
| lcms2                         | https://www.littlecms.com                                                           | https:                                                             |
| lerc                          | https://github.com/Esri/lerc                                                        | https:                                                             |
| libarchive                    | http://www.libarchive.org                                                           | https:                                                             |
| libblas                       | https://www.netlib.org/blas/                                                        | https:                                                             |
| libbrotlicommon               | https://github.com/google/brotli                                                    | https:                                                             |
| libbrotlidec                  | https://github.com/google/brotli                                                    | https:                                                             |
| libbrotlienc                  | https://github.com/google/brotli                                                    | https:                                                             |
| libcblas                      | https://anaconda.org/conda-forge/libcblas                                           | N/A                                                                |
| libclang                      | <b>Orion Floes</b>                                                                  | https:                                                             |
| libcurl                       | https://curl.se/libcurl/                                                            | https:                                                             |
| libcxx                        | https://github.com/llvm-mirror/libcxx                                               | https:                                                             |
| libdb                         | https://www.oracle.com/technology/software/products/berkeley-db/index.html          | https:                                                             |
| libdeflate                    | https://github.com/ebiggers/libdeflate                                              | https:                                                             |
| libedit                       | https://thrysoee.dk/editline/                                                       | http://                                                            |
| libev                         | https://software.schmorp.de/pkg/libev.html                                          | https:                                                             |
| libffi                        | https://github.com/libffi/libffi                                                    | https:                                                             |
| libgcrypt                     | https://gnupg.org/software/index.html                                               | https:                                                             |
| libgd                         | https://libgd.github.io                                                             | https:                                                             |
| libglib                       | https://github.com/PolMine/libglib                                                  | https:                                                             |
| libiconv                      | https://www.gnu.org/software/libiconv/                                              | https:                                                             |
|                               |                                                                                     |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| libint                        | https://tinyurl.com/yvw97wbw                                                        | https://                                                           |
| liblapack                     | http://www.netlib.org/lapack/                                                       | https://                                                           |
| liblapacke                    | https://anaconda.org/conda-forge/liblapacke                                         | https://                                                           |
| libmamba                      | https://medium.com/@QuantStack/open-software-packaging-for-science-61cecee7fc23     | https://                                                           |
| libmambapy                    | https://www.anaconda.com/blog/a-faster-conda-for-a-growing-community                | https://                                                           |
| libnetcdf                     | https://www.unidata.ucar.edu/software/netcdf/                                       | https://                                                           |
| libnghttp2                    | https://github.com/nghttp2/nghttp2                                                  | https://                                                           |
| libopenblas                   | https://www.openblas.net/                                                           | https://                                                           |
| libpng                        | https://www.libpng.org/pub/png/libpng.html                                          | https://                                                           |
| libpq                         | https://www.postgresql.org/                                                         | https://                                                           |
| librsvg                       | https://gitlab.gnome.org/GNOME/librsvg                                              | https://                                                           |
| libsolv                       | https://github.com/openSUSE/libsolv                                                 | https://                                                           |
| libssh2                       | https://github.com/libssh2/libssh2                                                  | https://                                                           |
| libtiff                       | https://www.libtiff.org/                                                            | https://                                                           |
| libtrust                      | https://github.com/docker/libtrust                                                  | https://                                                           |
| libuuid                       | https://sourceforge.net/projects/libuuid/                                           | https://                                                           |
| libuv                         | https://github.com/libuv/libuv                                                      | https://                                                           |
| libwebp                       | https://chromium.googlesource.com/?format=HTML                                      | https://                                                           |
| libwebp-base                  | https://chromium.googlesource.com/?format=HTML                                      | https://                                                           |
| libxc                         | https://www.tddft.org/programs/libxc/                                               | https://                                                           |
| libxcb                        | https://xcb.freedesktop.org                                                         | https://                                                           |
| libxml2                       | https://git.gnome.org/browse/libxml2/                                               | https://                                                           |
| libxmlsec1                    | https://github.com/lsh123/xmlsec                                                    | https://                                                           |
| libxslt                       | https://gitlab.gnome.org/GNOME/libxslt/-/wikis/home                                 | https://                                                           |
| libzlib                       | https://zlib.net                                                                    | https://                                                           |
| lime                          | https://github.com/marcotcr/lime                                                    | https://                                                           |
| lit                           | http://llvm.org                                                                     | https://                                                           |
| llvm-openmp                   | https://github.com/llvm-mirror/openmp                                               | https://                                                           |
| llvmlite                      | http://llvmlite.readthedocs.io                                                      | https://                                                           |
| loader-utils                  | https://github.com/webpack/loader-utils                                             | https://                                                           |
| logomaker                     | https://logomaker.readthedocs.io/en/latest/                                         | https://                                                           |
| logrus                        | https://github.com/sirupsen/logrus                                                  |                                                                    |
| logrus-airbrake-hook.v2       | https://gopkg.in/gemnasium/logrus-airbrake-hook.v2                                  | https://                                                           |
| lxml                          | https://lxml.de                                                                     | https://                                                           |
| lz4-c                         | https://www.lz4.org/                                                                | https://                                                           |
| markdown                      | https://github.com/evilstreak/markdown-js                                           |                                                                    |
| markdown-it-py                | Orion Floes                                                                         | https://                                                           |
| MarkupSafe                    | https://palletsprojects.com/p/markupsafe/                                           | https://                                                           |
| matplotlib                    | https://matplotlib.org                                                              | https://                                                           |
| matplotlib-base               | https://matplotlib.org                                                              | https://                                                           |
| matplotlib-inline             | https://github.com/ipython/matplotlib-inline                                        | https://                                                           |
| mda-xdrlib                    | https://github.com/MDAnalysis/mda-xdrlib                                            | https://                                                           |
| mdtraj                        | https://www.mdtraj.org/                                                             | https://                                                           |
| mdurl                         | Orion Floes                                                                         | https://                                                           |
| menuinst                      | Orion Floes                                                                         | https://                                                           |
| mergo                         | https://github.com/imdario/mergo                                                    | https://                                                           |
| mistune                       | https://github.com/lepture/mistune                                                  | https://                                                           |
| mkl                           | https://github.com/rust-math/intel-mkl-src                                          | https://                                                           |
| mkl-fft                       | https://github.com/IntelPython/mkl_fft                                              | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
| mkl-random                    | https://github.com/IntelPython/mkl_random                                           | https:/                                                            |
| mkl-service                   | https://github.com/IntelPython/mkl-service                                          | https:/                                                            |
| ml-dtypes                     | Orion Floes                                                                         | https:/                                                            |
| molecupy                      | https://molecupy.readthedocs.io/en/latest/                                          | https:/                                                            |
| moment                        | https://github.com/moment/moment                                                    | https:/                                                            |
| moment-precise-range-plugin   | https://github.com/codebox/moment-precise-range                                     | https:/                                                            |
| more-itertools                | https://github.com/more-itertools/more-itertools                                    | https:/                                                            |
| mpiplus                       | https://github.com/choderalab/mpiplus                                               | https:/                                                            |
| mpmath                        | http://mpmath.org/                                                                  | https:/                                                            |
| mrcfile                       | https://github.com/ccpem/mrcfile                                                    | https:/                                                            |
| msgpack                       | https://msgpack.org/                                                                | https:/                                                            |
| multidict                     | https://github.com/aio-libs/multidict                                               | https:/                                                            |
| multierr                      | https://go.uber.org/multierr                                                        | https:/                                                            |
| multiprocess                  | https://github.com/uqfoundation/multiprocess                                        | https:/                                                            |
| munkres                       | https://software.clapper.org/munkres/                                               | https:/                                                            |
| myesui uuid                   | https://github.com/myesui/uuid                                                      | https:/                                                            |
| namex                         | Orion Floes                                                                         | https:/                                                            |
| nbclassic                     | http://jupyter.org                                                                  | https:/                                                            |
| nbclient                      | https://jupyter.org                                                                 | https:/                                                            |
| nbconvert                     | https://jupyter.org                                                                 | https:/                                                            |
| nbformat                      | http://jupyter.org                                                                  | https:/                                                            |
| ncurses                       | https://invisible-island.net/ncurses/                                               | https:/                                                            |
| nest-asyncio                  | https://github.com/erdewit/nest_asyncio                                             | https:/                                                            |
| netcdf-fortran                | https://www.unidata.ucar.edu/software/netcdf/                                       | https:/                                                            |
| netCDF4                       | http://github.com/Unidata/netcdf4-python                                            | https:/                                                            |
| nettle                        | https://git.lysator.liu.se/nettle/nettle                                            | https:/                                                            |
| networkx                      | https://networkx.org                                                                | https:/                                                            |
| nfpm                          | https://github.com/goreleaser/nfpm                                                  | https:/                                                            |
| ng-tags-input                 | https://github.com/mbenford/ngTagsInput                                             | https:/                                                            |
| ng-toast                      | https://github.com/tameraydin/ngToast                                               | https:/                                                            |
| ngdraggable                   | https://github.com/fatlinesofcode/ngDraggable                                       | https:/                                                            |
| ngVue                         | https://github.com/ngVue/ngVue                                                      | https:/                                                            |
| nlopt                         | https://nlopt.readthedocs.io/en/latest/NLopt_Python_Reference/                      | https:/                                                            |
| nodejs                        | https://nodejs.org/en/                                                              | https:/                                                            |
| nomkl                         | https://github.com/conda-forge/nomkl-feedstock                                      | https:/                                                            |
| notebook                      | http://jupyter.org                                                                  | https:/                                                            |
| notebook-shim                 | https://github.com/jupyter/notebook_shim                                            | https:/                                                            |
| notebook_shim                 | http://jupyter.org                                                                  | https:/                                                            |
| numba                         | https://numba.pydata.org                                                            | https:/                                                            |
| numcpus                       | https://github.com/tklauser/numcpus                                                 | https:/                                                            |
| numexpr                       | https://github.com/pydata/numexpr                                                   | https:/                                                            |
| numpy                         | https://numpy.org                                                                   | https:/                                                            |
| numpy-base                    | https://numpy.org                                                                   | https:/                                                            |
| numpydoc                      | https://numpydoc.readthedocs.io/en/latest/index.html                                |                                                                    |
| nvidia-cublas-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cublas-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-cupti-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-cupti-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-nvrtc-cu11        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| nvidia-cuda-nvrtc-cu12        | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-runtime-cu11      | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cuda-runtime-cu12      | https://developer.nvidia.com/cuda-zone                                              | https://                                                           |
| nvidia-cudnn-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cudnn-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cufft-cu11             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cufft-cu12             | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-curand-cu11            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-curand-cu12            | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusolver-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusolver-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusparse-cu11          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-cusparse-cu12          | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nccl-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nccl-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nvjitlink-cu12         | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nvtx-cu11              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| nvidia-nvtx-cu12              | https://developer.nvidia.com/cuda-zone                                              | https:/                                                            |
| $Oat++$                       | https://oatpp.io/                                                                   | https:/                                                            |
| oauthlib                      | https://github.com/oauthlib/oauthlib                                                | https:/                                                            |
| ocl-icd                       | https://github.com/OCL-dev/ocl-icd                                                  | https:/                                                            |
| ocl-icd-system                | https://github.com/conda-forge/ocl-icd-system-feedstock                             | https:/                                                            |
| olefile                       | https://www.decalage.info/python/olefileio                                          | https:/                                                            |
| OmegaFold                     | https://github.com/HeliXonProtein/OmegaFold/tree/main                               | https:/                                                            |
| omnicanvas                    | https://omnicanvas.readthedocs.io/en/latest/                                        | https:/                                                            |
| OpenFF                        | https://openforcefield.org/                                                         | https:/                                                            |
| openff-amber-ff-ports         | https://github.com/openforcefield/openff-amber-ff-ports                             | https:/                                                            |
| openff-forcefields            | https://openforcefield.org                                                          | https:/                                                            |
| openff-interchange            | https://github.com/openforcefield/openff-interchange                                | https:/                                                            |
| openff-models                 | https://github.com/openforcefield/openff-models                                     |                                                                    |
| openff-toolkit                | https://openforcefield.org                                                          | https:/                                                            |
| openff-toolkit-base           | https://openforcefield.org                                                          | https:/                                                            |
| openff-units                  | https://github.com/openforcefield/openff-units                                      |                                                                    |
| openff-utilities              | https://github.com/openforcefield/openff-utilities                                  | https:/                                                            |
| openjpeg                      | https://github.com/uclouvain/openjpeg                                               | https:/                                                            |
| openldap                      | https://www.openldap.org/software/repo.html                                         | https:/                                                            |
| OpenMM                        | https://openmm.org                                                                  | https:/                                                            |
| openmmtools                   | https://github.com/choderalab/openmmtools                                           | https:/                                                            |
| openmoltools                  | https://github.com/choderalab/openmoltools                                          | https:/                                                            |
| openpyxl                      | https://openpyxl.readthedocs.io/en/stable/                                          | https:/                                                            |
| openssl                       | https://www.openssl.org                                                             | https:/                                                            |
| opt-einsum                    | https://github.com/dgasmith/opt_einsum                                              | https:/                                                            |
| OptKing                       | https://github.com/psi-rking/optking                                                | https:/                                                            |
| oscrypto                      | https://github.com/wbond/oscrypto                                                   | https:/                                                            |
| overrides                     | https://github.com/mkorpela/overrides                                               | https:/                                                            |
| packaging                     | https://github.com/pypa/packaging                                                   | https:/                                                            |
| packmol                       | https://leandro.iqm.unicamp.br/m3g/packmol/home.shtml                               | https:/                                                            |
| pandas                        | https://pandas.pydata.org                                                           | https:/                                                            |
| pandocfilters                 | http://github.com/jgm/pandocfilters                                                 | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| panedr                        | https://github.com/MDAnalysis/panedr                                                | https:/                                                            |
| pango                         | https://pango.gnome.org                                                             | https:/                                                            |
| ParmEd                        | https://parmed.github.io/ParmEd/html/index.html                                     | https:/                                                            |
| parser                        | https://github.com/typescript-eslint/typescript-eslint                              | https:/                                                            |
| parso                         | https://parso.readthedocs.io/en/latest/                                             | https:/                                                            |
| pathos                        | https://github.com/uqfoundation/pathos                                              | https:/                                                            |
| patsy                         | https://patsy.readthedocs.io/en/latest/                                             | https:/                                                            |
| pbkdf2                        | https://golang.org/x/crypto/pbkdf2                                                  | https:/                                                            |
| pbr                           | https://docs.openstack.org/pbr/latest/                                              | https:/                                                            |
| pcmsolver                     | https://pcmsolver.readthedocs.io/en/stable/                                         | https:/                                                            |
| pcre                          | https://www.pcre.org                                                                | https:/                                                            |
| pcre2                         | https://www.pcre.org                                                                | https:/                                                            |
| pdb4amber                     | https://github.com/Amber-MD/pdb4amber                                               | https:/                                                            |
| pdbfixer                      | https://github.com/openmm/pdbfixer                                                  | https:/                                                            |
| pexpect                       | https://pexpect.readthedocs.io/                                                     | https:/                                                            |
| pgconn                        | https://github.com/jackc/pgconn                                                     | https:/                                                            |
| pgio                          | https://github.com/jackc/pgio                                                       | https:/                                                            |
| pgpassfile                    | https://github.com/jackc/pgpassfile                                                 | https:/                                                            |
| pgproto3                      | https://github.com/jackc/pgproto3/v2                                                | https:/                                                            |
| pgtype                        | https://github.com/jackc/pgtype                                                     | https:/                                                            |
| pgx                           | https://github.com/jackc/pgx/v4                                                     | https:/                                                            |
| phonopy                       | https://github.com/phonopy/phono3py                                                 | https:/                                                            |
| pickleshare                   | https://github.com/pickleshare/pickleshare                                          | https:/                                                            |
| Pillow                        | https://python-pillow.org                                                           | https:/                                                            |
| Pint                          | https://pint.readthedocs.io/en/stable/                                              | https:/                                                            |
| pip                           | https://pip.pypa.io/                                                                | https:/                                                            |
| pip-licenses                  | https://github.com/raimon49/pip-licenses                                            | https:/                                                            |
| pixman                        | https://pixman.org                                                                  | https:/                                                            |
| pkginfo                       | https://launchpad.net/pkginfo                                                       | https:/                                                            |
| platformdirs                  | https://github.com/platformdirs/platformdirs                                        | https:/                                                            |
| plotly                        | https://plotly.com/python/                                                          | https:/                                                            |
| plotly-orca                   | https://github.com/plotly/orca                                                      | https:/                                                            |
| plotly.js                     | https://github.com/plotly/plotly.js                                                 | https:/                                                            |
| pluggy                        | https://pluggy.readthedocs.io/en/stable/index.html                                  | https:/                                                            |
| pooch                         | https://github.com/fatiando/pooch                                                   | https:/                                                            |
| pox                           | https://github.com/uqfoundation/pox                                                 | https:/                                                            |
| ppft                          | https://github.com/uqfoundation/ppft                                                | https:/                                                            |
| pq                            | https://github.com/lib/pq                                                           | https:/                                                            |
| ProDy                         | http://www.csb.pitt.edu/ProDy                                                       | https:/                                                            |
| prometheus-client             | https://github.com/prometheus/client_python                                         | https:/                                                            |
| prompt-toolkit                | https://python-prompt-toolkit.readthedocs.io/en/stable/                             | https:/                                                            |
| protobuf                      | https://google.golang.org/protobuf                                                  | https:/                                                            |
| psi4                          | https://psicode.org                                                                 | https:/                                                            |
| psutil                        | https://psutil.readthedocs.io/en/latest/                                            | https:/                                                            |
| psycopg2                      | https://psycopg.org/                                                                | https:/                                                            |
| PTable                        | https://github.com/kxxoling/PTable                                                  | https:/                                                            |
| pthread-stubs                 | https://xcb.freedesktop.org                                                         | https:/                                                            |
| ptyprocess                    | https://ptyprocess.readthedocs.io/en/latest/                                        | https:/                                                            |
| pure-eval                     | http://github.com/alexmojaki/pure_eval                                              | http:/                                                             |
| Name of Project               | Website                                                                             | License                                                            |
| py                            | https://py.readthedocs.io/en/latest/                                                |                                                                    |
| py-cpuinfo                    | https://github.com/workhorsy/py-cpuinfo                                             |                                                                    |
| pyasn1                        | https://github.com/etingof/pyasn1                                                   |                                                                    |
| pyasn1-modules                | https://github.com/etingof/pyasn1-modules                                           |                                                                    |
| pybind11-abi                  | https://github.com/pybind/pybind11                                                  |                                                                    |
| pycairo                       | https://pycairo.readthedocs.io/en/latest/index.html                                 |                                                                    |
| pycosat                       | https://github.com/conda/pycosat                                                    |                                                                    |
| pycparser                     | https://github.com/eliben/pycparser                                                 |                                                                    |
| pydantic                      | https://pydantic-docs.helpmanual.io                                                 |                                                                    |
| pydantic-core                 | https://github.com/pydantic/pydantic-core                                           |                                                                    |
| pyedr                         | https://github.com/MDAnalysis/panedr                                                |                                                                    |
| pyEMMA                        | http://github.com/markovmodel/PyEMMA                                                |                                                                    |
| Pygments                      | https://pygments.org                                                                |                                                                    |
| pygraphviz                    | https://pygraphviz.github.io                                                        |                                                                    |
| pygtop                        | https://pygtop.readthedocs.io/en/latest/                                            |                                                                    |
| pyHanko                       | https://github.com/MatthiasValvekens/pyHanko                                        |                                                                    |
| pyhanko-certvalidator         | https://github.com/MatthiasValvekens/certvalidator                                  |                                                                    |
| PyJWT                         | https://github.com/jpadilla/pyjwt                                                   |                                                                    |
| pymbar                        | https://pymbar.org                                                                  |                                                                    |
| pyOpenSSL                     | https://pyopenssl.org/                                                              |                                                                    |
| pyparsing                     | https://pyparsing-docs.readthedocs.io/en/latest/                                    |                                                                    |
| PyPDF3                        | https://github.com/sfneal/PyPDF3                                                    |                                                                    |
| pyrsistent                    | http://github.com/tobgu/pyrsistent/                                                 |                                                                    |
| pysam                         | https://github.com/pysam-developers/pysam                                           |                                                                    |
| PySocks                       | https://github.com/Anorov/PySocks                                                   |                                                                    |
| pytables                      | https://www.pytables.org                                                            |                                                                    |
| python                        | https://www.python.org/                                                             |                                                                    |
| python-bidi                   | https://github.com/MeirKriheli/python-bidi                                          |                                                                    |
| python-constraint             | https://github.com/python-constraint/python-constraint                              |                                                                    |
| python-dateutil               | https://dateutil.readthedocs.io                                                     |                                                                    |
| python-json-logger            | http://github.com/madzak/python-json-logger                                         |                                                                    |
| python-ldap                   | https://www.python-ldap.org/                                                        |                                                                    |
| python3-saml                  | https://github.com/onelogin/python3-saml                                            |                                                                    |
| python_abi                    | https://github.com/conda-forge/python_abi-feedstock                                 |                                                                    |
| pytz                          | https://pythonhosted.org/pytz                                                       |                                                                    |
| pytz-deprecation-shim         | https://github.com/pganssle/pytz-deprecation-shim                                   |                                                                    |
| PyWavelets                    | https://github.com/PyWavelets/pywt                                                  |                                                                    |
| PyYAML                        | https://pyyaml.org/                                                                 |                                                                    |
| pyyml                         | No longer available                                                                 |                                                                    |
| pyzmq                         | https://pyzmq.readthedocs.io/en/latest/                                             |                                                                    |
| qcelemental                   | https://github.com/MolSSI/QCElemental                                               |                                                                    |
| qcengine                      | https://github.com/MolSSI/QCEngine                                                  |                                                                    |
| qrcode                        | https://github.com/lincolnloop/python-qrcode                                        |                                                                    |
| ramda                         | https://github.com/ramda/ramda                                                      |                                                                    |
| rapidjson                     | https://rapidjson.org/                                                              |                                                                    |
| rdkit                         | https://www.rdkit.org                                                               |                                                                    |
| re2                           | https://github.com/google/re2                                                       |                                                                    |
| readme-renderer               | https://github.com/pypa/readme_renderer                                             |                                                                    |
| redis-py                      | https://github.com/andymccurdy/redis-py                                             |                                                                    |
| Name of Project               | Website                                                                             | License                                                            |
| referencing                   | https://github.com/python-jsonschema/referencing                                    | https://                                                           |
| regex                         | https://github.com/mrabarnett/mrab-regex                                            | https://                                                           |
| reportlab                     | https://www.reportlab.com                                                           | https://                                                           |
| reproc                        | https://github.com/DaanDeMeyer/reproc                                               | https://                                                           |
| reproc-cpp                    | https://github.com/DaanDeMeyer/reproc                                               | https://                                                           |
| requests                      | https://requests.readthedocs.io                                                     | https://                                                           |
| requests-oauthlib             | https://github.com/requests/requests-oauthlib                                       | https://                                                           |
| requests-toolbelt             | https://toolbelt.readthedocs.org                                                    | https://                                                           |
| resumable                     | https://github.com/stevvooe/resumable                                               | https://                                                           |
| retrying                      | https://github.com/rholder/retrying                                                 | https://                                                           |
| rfc3339-validator             | https://github.com/naimetti/rfc3339-validator                                       | https://                                                           |
| rfc3986                       | https://rfc3986.readthedocs.io/en/latest/                                           | https://                                                           |
| rfc3986-validator             | https://github.com/naimetti/rfc3986-validator                                       | https://                                                           |
| rich                          | https://github.com/Textualize/rich                                                  | https://                                                           |
| rpds-py                       | https://github.com/crate-py/rpds                                                    | https://                                                           |
| rpmpack                       | https://github.com/google/rpmpack                                                   | https://                                                           |
| rsa                           | https://stuvel.eu/rsa                                                               | https://                                                           |
| ruamel-yaml                   | https://sourceforge.net/p/ruamel-yaml/code/ci/default/tree/                         | https://                                                           |
| ruamel.yaml.clib              | https://sourceforge.net/p/ruamel-yaml-clib/code/ci/default/tree/                    | https://                                                           |
| s3transfer                    | https://github.com/boto/s3transfer                                                  | https://                                                           |
| sasl                          | https://mellium.im/sasl                                                             | https://                                                           |
| scikit-gstat                  | https://mmaelicke.github.io/scikit-gstat/                                           | https://                                                           |
| scikit-image                  | https://scikit-image.org                                                            | https://                                                           |
| scikit-learn                  | https://scikit-learn.org/stable/                                                    | https://                                                           |
| scikit-learn-extra            | https://github.com/scikit-learn-contrib/scikit-learn-extra                          | https://                                                           |
| scipy                         | https://scipy.org                                                                   | https://                                                           |
| seaborn                       | https://seaborn.pydata.org                                                          | https://                                                           |
| seaborn-base                  | https://seaborn.pydata.org                                                          | https://                                                           |
| semver                        | https://github.com/Masterminds/semver/v3                                            | https://                                                           |
| Send2Trash                    | https://github.com/arsenetar/send2trash                                             | https://                                                           |
| setuptools                    | https://github.com/pypa/setuptools                                                  | https://                                                           |
| setuptools-scm                | https://github.com/pypa/setuptools_scm/                                             | https://                                                           |
| sh                            | https://github.com/amoffat/sh                                                       | https://                                                           |
| shellingham                   | https://github.com/sarugaku/shellingham                                             | https://                                                           |
| simint                        | https://www.bennyp.org/research/simint/                                             | https://                                                           |
| six                           | https://github.com/benjaminp/six                                                    | https://                                                           |
| smirnoff99frosst              | https://github.com/openforcefield/smirnoff99frosst                                  | https://                                                           |
| snappy                        | https://github.com/google/snappy                                                    | https://                                                           |
| sniffio                       | https://github.com/python-trio/sniffio                                              | https://                                                           |
| snowballstemmer               | https://github.com/snowballstem/snowball                                            | https://                                                           |
| soupsieve                     | https://github.com/facelessuser/soupsieve                                           | https://                                                           |
| spglib                        | https://github.com/spglib/spglib                                                    | https://                                                           |
| sphinx                        | https://github.com/sphinx-doc/sphinx                                                | https://                                                           |
| sphinxcontrib-applehelp       | https://github.com/sphinx-doc/sphinxcontrib-applehelp                               | https://                                                           |
| sphinxcontrib-devhelp         | https://github.com/sphinx-doc/sphinxcontrib-devhelp                                 | https://                                                           |
| sphinxcontrib-htmlhelp        | https://github.com/sphinx-doc/sphinxcontrib-htmlhelp                                | https://                                                           |
| sphinxcontrib-jsmath          | https://github.com/sphinx-doc/sphinxcontrib-jsmath                                  | https://                                                           |
| sphinxcontrib-qthelp          | https://github.com/sphinx-doc/sphinxcontrib-qthelp                                  | https://                                                           |
| sphinxcontrib-serializinghtml | https://github.com/sphinx-doc/sphinxcontrib-serializinghtml                         | https://                                                           |
| Name of Project               | Website                                                                             | License                                                            |
| SQLAlchemy                    | https://www.sqlalchemy.org                                                          | https:/                                                            |
| sqlite                        | https://sqlite.org/index.html                                                       | https:/                                                            |
| sqlparse                      | https://github.com/andialbrecht/sqlparse                                            | https:/                                                            |
| stack-data                    | http://github.com/alexmojaki/stack_data                                             | https:/                                                            |
| starfile                      | https://github.com/alisterburt/starfile                                             | https:/                                                            |
| statsmodels                   | https://github.com/statsmodels/statsmodels                                          | https:/                                                            |
| structlog                     | https://www.structlog.org/                                                          | https:/                                                            |
| svglib                        | https://github.com/deeplook/svglib                                                  | https:/                                                            |
| sympy                         | https://sympy.org                                                                   | https:/                                                            |
| tables                        | https://www.pytables.org/                                                           | https:/                                                            |
| tabulate                      | https://github.com/astanin/python-tabulate                                          | https:/                                                            |
| tbb                           | https://github.com/oneapi-src/oneTBB                                                | https:/                                                            |
| tenacity                      | https://github.com/jd/tenacity                                                      | https:/                                                            |
| tensorboard                   | https://github.com/tensorflow/tensorboard                                           | https:/                                                            |
| tensorboard-data-server       | https://github.com/tensorflow/tensorboard                                           | https:/                                                            |
| tensorboard-plugin-wit        | https://github.com/pair-code/what-if-tool                                           | https:/                                                            |
| tensorflow                    | https://github.com/tensorflow/tensorflow                                            | https:/                                                            |
| tensorflow-estimator          | https://github.com/tensorflow/estimator                                             | https:/                                                            |
| tensorflow-io-gcs-filesystem  | Orion Floes                                                                         | https:/                                                            |
| tensorflow-probability        | https://github.com/tensorflow/probability                                           | https:/                                                            |
| termcolor                     | https://github.com/hugovk/termcolor                                                 | https:/                                                            |
| terminado                     | https://github.com/jupyter/terminado                                                | https:/                                                            |
| testpath                      | https://github.com/jupyter/testpath                                                 | https:/                                                            |
| textangular                   | https://github.com/fraywing/textAngular                                             | https:/                                                            |
| tf_keras                      | Orion Floes                                                                         | https:/                                                            |
| threadpoolctl                 | https://github.com/joblib/threadpoolctl                                             | https:/                                                            |
| three                         | https://github.com/mrdoob/three.js                                                  | https:/                                                            |
| tifffile                      | https://github.com/cgohlke/tifffile/                                                | https:/                                                            |
| tinycss2                      | https://github.com/Kozea/tinycss2/                                                  | https:/                                                            |
| tinyxml2                      | https://github.com/leethomason/tinyxml2                                             | https:/                                                            |
| tk                            | https://www.tcl.tk/                                                                 | https:/                                                            |
| toml                          | https://github.com/toml-lang/toml                                                   | https:/                                                            |
| tomli                         | https://github.com/hukkin/tomli                                                     | https:/                                                            |
| toolz                         | https://github.com/pytoolz/toolz                                                    | https:/                                                            |
| torch                         | https://pytorch.org/                                                                | https:/                                                            |
| tornado                       | https://www.tornadoweb.org                                                          | https:/                                                            |
| tqdm                          | https://github.com/tqdm/tqdm                                                        | https:/                                                            |
| tracy                         | https://github.com/gear-genomics/tracy                                              | https:/                                                            |
| traitlets                     | https://github.com/ipython/traitlets                                                | https:/                                                            |
| triton                        | https://github.com/openai/triton/                                                   | https:/                                                            |
| truststore                    | Orion Floes                                                                         | https:/                                                            |
| ts-jest                       | https://github.com/kulshekhar/ts-jest                                               | https:/                                                            |
| ts-loader                     | https://github.com/TypeStrong/ts-loader                                             | https:/                                                            |
| twine                         | https://github.com/pypa/twine                                                       | https:/                                                            |
| twinj uuid                    | https://github.com/twinj/uuid                                                       | https:/                                                            |
| types                         | https://github.com/babel/babel                                                      | https:/                                                            |
| typescript                    | https://github.com/Microsoft/TypeScript                                             | https:/                                                            |
| typing_extensions             | https://github.com/python/typing                                                    | https:/                                                            |
| tzdata                        | https://github.com/python/tzdata                                                    | https:/                                                            |
| Name of Project               | Website                                                                             | License                                                            |
| tzlocal                       | https://github.com/regebro/tzlocal                                                  | https:/                                                            |
| umi-tools                     | https://github.com/CGATOxford/UMI-tools                                             | https:/                                                            |
| unicodedata2                  | https://github.com/fonttools/unicodedata2                                           | https:/                                                            |
| uritools                      | https://github.com/tkem/uritools/                                                   | https:/                                                            |
| urllib3                       | https://urllib3.readthedocs.io/                                                     | https:/                                                            |
| vine                          | https://github.com/celery/vine                                                      | https:/                                                            |
| vue                           | https://github.com/vuejs/vue                                                        | https:/                                                            |
| wcwidth                       | https://github.com/jquast/wcwidth                                                   | https:/                                                            |
| webencodings                  | https://github.com/gsnedders/python-webencodings                                    | https:/                                                            |
| websocket-client              | https://github.com/websocket-client/websocket-client.git                            | https:/                                                            |
| Werkzeug                      | https://palletsprojects.com/p/werkzeug/                                             | https:/                                                            |
| westpa                        | Orion Floes                                                                         | http://                                                            |
| wheel                         | https://github.com/pypa/wheel                                                       | https:/                                                            |
| widgetsnbextension            | https://github.com/jupyter-widgets/ipywidgets#readme                                | https:/                                                            |
| wrapt                         | https://github.com/GrahamDumpleton/wrapt                                            | https:/                                                            |
| wsutil                        | https://github.com/yhat/wsutil                                                      | https:/                                                            |
| x/lint                        | https://golang.org/x/lint                                                           | https:/                                                            |
| x/mod                         | https://golang.org/x/mod/semver                                                     | https:/                                                            |
| x/net                         | https://golang.org/x/net                                                            | https:/                                                            |
| x/oauth2                      | https://golang.org/x/oauth2                                                         | https:/                                                            |
| x/sys                         | https://golang.org/x/sys                                                            | https:/                                                            |
| x/text                        | https://golang.org/x/text                                                           | https:/                                                            |
| x/tools                       | https://golang.org/x/tools                                                          | https:/                                                            |
| x/xerrors                     | https://golang.org/x/xerrors                                                        | https:/                                                            |
| xhtml2pdf                     | http://github.com/xhtml2pdf/xhtml2pdf                                               | https:/                                                            |
| xlrd                          | https://github.com/python-excel/xlrd                                                | https:/                                                            |
| xmlsec                        | https://github.com/mehcode/python-xmlsec                                            | https:/                                                            |
| xmltodict                     | https://github.com/martinblech/xmltodict                                            | https:/                                                            |
| xorg-kbproto                  | https://gitlab.freedesktop.org/xorg/proto/kbproto                                   | https:/                                                            |
| xorg-libice                   | https://gitlab.freedesktop.org/xorg/lib/libice                                      | https:/                                                            |
| xorg-libsm                    | https://gitlab.freedesktop.org/xorg/lib/libsm                                       | https:/                                                            |
| xorg-libx11                   | https://gitlab.freedesktop.org/xorg/lib/libx11                                      | https:/                                                            |
| xorg-libxau                   | https://gitlab.freedesktop.org/xorg/lib/libxau                                      | https:/                                                            |
| xorg-libxdmcp                 | https://gitlab.freedesktop.org/xorg/lib/libxdmcp                                    | https:/                                                            |
| xorg-libxext                  | https://gitlab.freedesktop.org/xorg/lib/libxext                                     | https:/                                                            |
| xorg-libxrender               | https://gitlab.freedesktop.org/xorg/lib/libxrender                                  | https:/                                                            |
| xorg-libxt                    | https://gitlab.freedesktop.org/xorg/lib/libxt                                       | https:/                                                            |
| xorg-renderproto              | https://gitlab.freedesktop.org/xorg/proto/renderproto                               | https:/                                                            |
| xorg-xextproto                | https://gitlab.freedesktop.org/xorg/proto/xextproto                                 | https:/                                                            |
| xorg-xproto                   | https://gitlab.freedesktop.org/xorg/proto/xproto                                    | https:/                                                            |
| xxhash                        | https://github.com/cespare/xxhash/v2                                                | https:/                                                            |
| xz                            | https://github.com/ulikunitz/xz                                                     | https:/                                                            |
| yaml                          | https://pyyaml.org/                                                                 | https:/                                                            |
| yaml-cpp                      | https://github.com/jbeder/yaml-cpp                                                  |                                                                    |
| yaml.v2                       | https://gopkg.in/yaml.v2                                                            | https:/                                                            |
| yaml.v3                       | https://gopkg.in/yaml.v3                                                            | https:/                                                            |
| yarl                          | https://github.com/aio-libs/yarl/                                                   | https:/                                                            |
| yaspin                        | https://github.com/pavdmyt/yaspin                                                   | https:/                                                            |
| yfiles                        | https://www.yworks.com/products/yfiles                                              | comm                                                               |
| Name of Project               | Website                                                                             | License                                                            |
| yml                           | https://pypi.org/project/yml/                                                       | N/A                                                                |
| zap                           | https://go.uber.org/zap                                                             | https:/                                                            |
| zipp                          | https://github.com/jaraco/zipp                                                      | https:/                                                            |
| zlib                          | https://zlib.net/                                                                   | https:/                                                            |
| zstandard                     | https://github.com/indygreg/python-zstandard                                        | https:/                                                            |
| zstd                          | https://facebook.github.io/zstd/                                                    | https:/                                                            |
| _libgcc_mutex                 | https://github.com/conda-forge/_libgcc_mutex-feedstock                              | https:/                                                            |
| _openmp_mutex                 | https://github.com/conda-forge/_openmp_mutex-feedstock                              | https:/                                                            |

# **4.1 GCC**

On the Linux platform, The OpenEye toolkits are linked with the GCC libraries using an eligible compilation process under the terms of the GCC RUNTIME LIBRARY EXCEPTION (see below).

The OpenEye toolkits are NOT open source software and are NOT governed by GPL or other open source licenses. Your right to use the toolkits are governed by the OpenEye license which is binding to You.

For certain Linux distributions, GCC library components are included as object files. Your rights to use GCC library components (libstdc++, libgcc, and libgomp) included with these distributions are governed by the GPLv3 license as follows:

The components libstdc++, libgcc, and libgomp are part of GCC.

- GCC is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
- GCC is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with GCC (see below). If not, see Licenses GNU Project.

Per GPLv3, section 6d, the source for GCC is available for download from the following location: GNU. The GCC library components included here are from version gcc-4.9.3 and are built using the standard instructions at Installing GCC.

### **4.1.1 GCC RUNTIME LIBRARY EXCEPTION**

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

When you use GCC to compile a program, GCC may combine portions of certain GCC header  $\rightarrow$ files and runtime libraries with the compiled program. The purpose of this Exception is to allow compilation of non- $\rightarrow$ GPL (including proprietary) programs to use, in this way, the header files and runtime libraries covered by this Exception. 0. Definitions. A file is an "Independent Module" if it either requires the Runtime Library for. →execution after a Compilation Process, or makes use of an interface provided by the Runtime Library, but is not otherwise  $\rightarrow$ based on the Runtime Library. "GCC" means a version of the GNU Compiler Collection, with or without modifications,  $\rightarrow$  governed by version 3 (or a specified later version) of the GNU General Public License (GPL) with the option of using any  $\rightarrow$ subsequent versions published by the FSF. "GPL-compatible Software" is software whose conditions of propagation, modification.  $\rightarrow$  and use would permit combination with GCC in accord with the license of GCC. "Target Code" refers to output from any compiler for a real or virtual target →processor architecture, in executable form or suitable for input to an assembler, loader, linker and/or execution phase.  $\rightarrow$ Notwithstanding that, Target Code does not include data in any format that is used as a compiler intermediate. →representation, or used for producing a compiler intermediate representation. The "Compilation Process" transforms code entirely represented in non-intermediate  $\rightarrow$ languages designed for human-written code, and/or in Java Virtual Machine byte code, into Target Code. Thus, for example,..  $\rightarrow$ use of source code generators and preprocessors need not be considered part of the Compilation Process, since the →Compilation Process can be understood as starting with the output of the generators or preprocessors. A Compilation Process is "Eligible" if it is done using GCC, alone or with other GPL- $\rightarrow$  compatible software, or if it is done without using any work based on GCC. For example, using non-GPL-compatible →Software to optimize any GCC intermediate representations would not qualify as an Eligible Compilation Process. 1. Grant of Additional Permission. You have permission to propagate a work of Target Code formed by combining the  $\rightarrow$ Runtime Library with Independent Modules, even if such propagation would otherwise violate the terms of GPLv3, provided that all Target Code was generated by Eligible Compilation Processes. You may then convey such a combination under terms of  $\rightarrow$ your choice, consistent with the licensing of the Independent Modules. 2. No Weakening of GCC Copyleft.

```
The availability of this Exception does not imply any general presumption that third-
→party software is unaffected by
the copyleft requirements of the license of GCC.
```

#### See also:

• http://www.gnu.org/licenses/gcc-exception.html

### **4.1.2 GNU GENERAL PUBLIC LICENSE**

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

License will continue to apply to the part which is the covered work, but the special requirements of the GNU Affero General Public License, section 13, concerning interaction through a network will apply to the combination as such. 14. Revised Versions of this License. The Free Software Foundation may publish revised and/or new versions of the GNU General Public License from time to time. Such new versions will be similar in spirit to the present version, but may differ in detail to address new problems or concerns. Each version is given a distinguishing version number. If the Program specifies that a certain numbered version of the GNU General Public License "or any later version" applies to it, you have the option of following the terms and conditions either of that numbered version or of any later version published by the Free Software Foundation. If the Program does not specify a version number of the GNU General Public License, you may choose any version ever published by the Free Software Foundation. If the Program specifies that a proxy can decide which future versions of the GNU General Public License can be used, that proxy's public statement of acceptance of a version permanently authorizes you to choose that version for the Program. Later license versions may give you additional or different permissions. However, no additional obligations are imposed on any author or copyright holder as a result of your choosing to follow a later version. 15. Disclaimer of Warranty. THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW. EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS WITH YOU. SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY SERVICING, REPAIR OR CORRECTION. 16. Limitation of Liability. IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS), EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES.

17. Interpretation of Sections 15 and 16.

If the disclaimer of warranty and limitation of liability provided

above cannot be given local legal effect according to their terms, reviewing courts shall apply local law that most closely approximates an absolute waiver of all civil liability in connection with the Program, unless a warranty or assumption of liability accompanies a copy of the Program in return for a fee. END OF TERMS AND CONDITIONS

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

See also:

• http://www.gnu.org/licenses/gpl.txt

#### **CHAPTER**

# **OETOOLKITS 2024.2**

# 5.1 Release Highlights 2024.2.0

### 5.1.1 OMEGA: Thompson Sampling for Torsion Driving

A Bayesian approach to explore conformer space with torsion driving has been added as an alternative to the exhaustive searching of the space in **OMEGA**. This uses the framework of Thompson sampling to quickly direct the conformer search towards the low energy structures, reducing the time required to find the lowest energy conformer. As such, Thompson sampling is particularly suitable for generating small to moderately sized ensembles, such as used in the FastROCS or ROCS mode. Thompson sampling provides significant speedup for such ensemble generation, particularly for molecules with a large number of rotors.

Conformer ensembles for FastROCS usage are generated with OMEGA using both the standard exhaustive sampling and the newly implemented Thompson sampling, for ~5500 Iridium HT protein bound small molecule crystal structures. Performance between the two sampling methods is compared in terms of RMSD between the generated ensemble and the crystal pose, and in the time required to generate the ensembles. The results of the comparison, as shown in Figure 1 below, show that the accuracy of the generated ensembles, measured in RMSD, remains unaffected when using exhaustive versus Thompson sampling, whereas there is significant reduction in time usage to generate those ensembles when using Thompson sampling, especially as the size of the molecules grows.

![](_page_42_Figure_7.jpeg)

Fig. 1: Figure 1. Comparison of OMEGA performance between exhaustive and Thompson sampling.

Ligand-based virtual screening performance, using both the exhaustive and Thompson sampling generated ensembles, was also compared and displayed in Figure 2. The comparisons were performed using directory of useful decoys (DUD-Z) datasets containing 38 targets. The results ensure that there is no meaningful change in accuracy when using Thompson sampling for ensemble generation for usage in ligand-based virtual screening.

![](_page_43_Figure_1.jpeg)

Fig. 2: Figure 2. Comparison of performance of ligand-based virtual screening success rate with conformer ensembles generated using exhaustive versus Thompson sampling.

### 5.1.2 BROOD: Bioisosteric Fragment Replacement in Macrocyclic Peptides

A new pose generation algorithm has been introduced in Bioisostere TK, as well as in BROOD, based on flexible overlay of shape, color, and force fields, as used in pose generation with **ShapeFit**. The new algorithm generates high quality poses of molecules that are obtained from fragment replacement in Bioisostere TK and BROOD. The robust pose generation algorithm enables usage of **Bioisostere TK** and **BROOD** for molecules with complex geometry, including macrocyclic peptides. Figure 3 shows an example of a residue fragment replacement in a macrocyclic peptide.

### 5.1.3 Eon TK: New Toolkit for Overlay Optimization with Shape and Charge Density

The 2024.2 release introduces **Eon TK**, a new toolkit for molecular similarity based on shape and electrostatics. This provides toolkit-level access to the existing **EON** application functionality. Following **EON**, the new toolkit has both molecular charge density and electrostatic potential as options to use as descriptors of electrostatic properties. Figure 4 shows an example of **EON** overlay with charge density visualization.

**Eon TK** provides tools for molecular overlay optimization with shape and charge density, similarity estimation based on shape and charge density or electrostatic potential, and corresponding hit list building.

![](_page_44_Figure_1.jpeg)

Fig. 3: Figure 3. Bioisosteric replacement of a residue fragment in a macrocyclic peptide using BROOD.

![](_page_44_Figure_3.jpeg)

Fig. 4: Figure 4. EON shape charge density overlay between two molecules.

### **5.1.4 Supported Platforms**

| Package | Versions         | Linux              |                 | Windows              | macOS (x64 and arm64) |
|---------|------------------|--------------------|-----------------|----------------------|-----------------------|
| Python  | 3.9<br>-<br>3.12 | RHEL8/9,<br>ARM/24 | Ubuntu20/22/22- | Win10/11             | 12, 13, 14            |
| $C++$   |                  | RHEL8/9,<br>ARM/24 | Ubuntu20/22/22- | Win10/11<br>(VS2022) | 12, 13, 14            |
| Java    | 8, 11, 20        | RHEL8/9,<br>ARM/24 | Ubuntu20/22/22- | Win10/11             | 12, 13, 14            |
| C#      |                  |                    |                 | Win10/11<br>(VS2022) |                       |

### 5.1.5 Related TK Versions

| Toolkit        | Version |
|----------------|---------|
| Bioisostere TK | 4.1.0   |
| OEChem TK      | 4.1.1   |
| OEDepict TK    | 2.5.5   |
| OEDocking TK   | 4.3.2   |
| FastROCS TK    | 2.2.7   |
| OEFF TK        | 2.8.0   |
| Grapheme TK    | 1.5.2   |
| Graphsim TK    | 2.6.1   |
| Lexichem TK    | 2.9.2   |
| OEMedChem TK   | 1.2.3   |
| MolProp TK     | 2.6.5   |
| Omega TK       | 6.0.0   |
| Quacpac TK     | 2.2.5   |
| Shape TK       | 3.7.0   |
| SiteHopper TK  | 2.1.1   |
| Spicoli TK     | 1.6.1   |
| Spruce TK      | 1.6.1   |
| Szmap TK       | 1.7.1   |
| Szybki TK      | 2.8.0   |
| Zap TK         | 2.5.0   |

# **5.2 General Notices**

- Support for Java 8 and 11 is now available on all platforms, including macOS arm64.
- Support for Ubuntu 24.04 has been added for C++, Python, and Java toolkits. Support for applications and VIDA will be added in the next release.
- Support for macOS 15 is not available in this release but will be added in the next release. This release will be the last to support macOS 12.
- Support for Python 3.13 is not available in this release but will be added in the next release.
- Support for Ubuntu 20.04 has been continued in this release, which will be the last to provide support for Ubuntu 20.04.

# **DETAILED RELEASE NOTES 2024.2**

# 6.1 Bioisostere TK 4.1.0

#### 6.1.1 New features

• A new algorithm, based on OEFlexiOverlay, has been adapted in Build for optimization of generated poses for molecules obtained from fragment replacement. The new algorithm is more robust for optimization of poses for all geometries, including cyclic peptides.

### 6.1.2 Major bug fixes

- Query building algorithms in OECreateBroodQuery have been improved for robustness. The improved API automatically includes any associated hydrogen atoms as part of the query fragment. Behavior has also been improved to provide better error behavior against invalid selections.
- The new methods SetSingleSourceMol and GetSingleSourceMol have been added to OEFragmentOptions to provide flexibility regarding source molecule storage during database building.

### 6.1.3 Minor bug fixes

• Some memory management issues have been fixed in Build and Generate.

# 6.2 OEChem TK 4.1.1

#### **6.2.1 New features**

- Support has been implemented for OEGroup information for OEMiniMol to support the return of enhanced stereogroup information from OEFastFPDatabase hits. Previously, enhanced stereogroup information on the indexed structures would be ignored during indexing and thus missed from returned hits.
- LINK records in the PDB metadata are now parsed to improve perception of covalently bound heterogens. The equivalent \_struct\_conn metadata is also parsed from mmCIF files. The distance between the listed atoms is confirmed before applying the bond.

### 6.2.2 Minor bug fixes

- If any parse error results from parsing a OEFOrmat\_CXSMILES appendix specifically, the full appendix plus the molecule title are now returned in the molecule title to allow user inspection and corrective action.
- OEFormat\_SDF data parsing has been modified to ensure that >-prefixed data is properly captured. Since SDF data field name lines are >-prefixed as well, the new behavior explicitly requires a blank line delimiter to be present between data entries, including null data items, per the SDF file format specification. This allows unambiguous identification of data field name header lines versus data entry lines.
- An issue has been fixed to avoid generating duplicate data tags from generic data that can result in invalid JSON output.
- Titles returned from OEMolDatabase. GetTitle when OEFormat CXSMILES files are indexed no longer contain the CXSMILES appendix unless there is a parse error with the appendix information itself.
- An error has been fixed that sometimes resulted in missing atom parity information in output SDF format files when a nondefault oemolistream. SetConfTest was provided.
- A line ending parse error has been fixed for OEFormat FASTA files affecting windows files.
- Propagation of perceived query aromaticity has been added for alternating single/double Kekulé forms so that alternate and equivalent s/d bond patterns are treated consistently.
- Null pointer protections have been added to some internal search matching code that could cause a crash.
- OEFileStringTypeFlavor\_Default has been augmented to exclude file types that are not suggested for use. Accordingly, a new constant, OEFileStringTypeFlavor\_Pretty, has been defined and is part of the new definition of OEFileStringTypeFlavor\_Default. Removing OEFileStringTypeFlavor\_Pretty from OEFileStringTypeFlavor\_Default would provide the file types that include everything.
- A new type, OEMMFFType\_CION, has been added to define a generic type for counterions.

# 6.3 OEPlatform TK 4.1.1

#### 6.3.1 New features

• The ZSTD library has been updated from version 1.5.2 to 1.5.6.

# 6.4 OEBio TK 4.1.1

#### 6.4.1 Major bug fixes

- In the Iridium categorization of a design unit, a properly perceived, covalently bound ligand no longer triggers an HT to MT category transition. The rule flags atoms that are within what is considered a covalent bond distance, where a bond is not properly perceived.
- An issue has been fixed so that ClearComponent can be used to clear user-defined components.

# 6.5 OEDepict TK 2.5.5

Minor internal improvements have been made.

# 6.6 OEDocking TK 4.3.2

#### 6.6.1 New features

- The method Optimize in OEPoseOptimizer now returns an unsigned code corresponding to any possible failure, instead of a bool. The method also takes additional arguments for protein and ligand masks in the OEDesignUnit.
- The following methods have been added to the OESinglePoseResult:
  - GetRelaxAttempted
  - GetRelaxStatus
  - GetRelaxStatusStr
- A new method, MethodChoice, has been added to OEPosit that provides information on the method that would be used for the pose prediction of a given ligand against a given receptor.
- The new methods GetTorLib and SetTorLib have been added to OEPositOptions to provide a choice for the torsion library that would be used for conformer generation during pose prediction.
- The following methods have been added to the OEShapeFitOptions:
  - GetMaxLocalStrain
  - SetMaxLocalStrain
  - $-$  GetTorLib
  - SetTorLib

#### 6.6.2 Major bug fixes

- The method Optimize in OEPoseOptimizer is now more robust in optimizing a docked pose. Accordingly, Docking with relaxation in OEPosit is also now more robust.
- The function OEHasClash now properly recognizes all clashes between a ligand and a protein that were previously mistaken because of some misidentification of covalent bonds.

### 6.6.3 Minor bug fixes

- Selection of the best receptor has been improved in OEPosit, ensuring that the correct receptor will always be picked in case of a self-docking.
- The internal algorithm has been optimized to improve time requirements for OEPosit when working with many receptors and a few ligands.

# 6.7 Eon TK 3.1.0

This is the first commercial release of Eon TK.

#### **6.7.1 New features**

The following classes are available as preliminary API with the first release of this toolkit.

- OEChargeFunc
- OEEonHit
- OEEonHitlistBuilder
- OEEonHitlistOptions
- OEEonOverlapFunc
- OEEonOverlapScore
- OEEonOverlay
- OEEonOverlayResults
- OEEonOverlayScore
- OEEonPBFunc
- OEEonPBOptions
- OEEonPBOverlay
- OEExactChargeFunc
- OEGridChargeFunc

The following functions are available as preliminary API with the first release of this toolkit.

- OEEtGetArch
- OEEtGetLicensee
- OEEtGetPlatform
- OEEtGetRelease
- OEEtGetSite
- OEEtGetVersion
- OEEtIsLicensed

# **6.8 FastROCS TK 2.2.7**

### **6.8.1 New features**

- New methods have been added to the OEShapeDatabaseOptions class that allow the shape and color scales to be modified.
  - SetShapeScoreScale
  - GetShapeScoreScale

- SetColorScoreScale
- GetColorScoreScale

# 6.9 Grapheme TK 1.5.2

### 6.9.1 New features

- An option has been added to the OEColorForceFieldDisplay to preserve input query color atoms instead of applying them from the defined color force field. There are two new methods and one new constructor, taking that argument along with the color force field.
  - SetPreserveQueryColors
  - GetPreserveQueryColors
  - Constructors

### 6.9.2 Minor bug fixes

• An issue has been fixed which incorrectly used the ligand density value for the active site density value when depicting the Iridium classification.

# 6.10 GraphSim TK 2.6.1

#### 6.10.1 Minor bug fixes

• The function OEGraphsimIsGPUReady has been safeguarded from a rare crash.

# **6.11 Lexichem TK 2.9.2**

Minor internal improvements have been made.

# 6.12 OEMedChem TK 1.2.3

Minor internal improvements have been made.

# 6.13 MolProp TK 2.6.5

Minor internal improvements have been made.

# 6.14 OEFF TK 2.8.0

### 6.14.1 New features

- The constant OESmirnoffType\_SAGE\_OPENFF now refers to the 2.2.1 version of the Sage OpenFF force field.
- Any SMIRNOFF set of parameters loaded using OESmirnoffParams, including the built-in OESageParams and OEParsleyParams, are now supplemented with van der Waals parameters for many metals and counterions, as used with the OpenMM package.
- The OEMMFF94sParams and OEMMFFParams are now supplemented with a generic set of van der Waals parameters for many metals and counterions to improve robustness.
- A new function, OEIsValidMMFFMolecule, has been added that can be used to check if OEMMFFParams are available for a molecule.

### 6.14.2 Minor Bug Fixes

• Loading a SMIRNOFF set of parameters using OESmirnoffParams no longer picks up the library charges.

# 6.15 Omega TK 6.0.0

#### 6.15.1 New features

- The following new methods have been added to OETorDriveOptions to enable use of Thompson sampling, instead of exhaustive sampling, of torsion angles during torsion driving. Use of Thompson sampling is especially useful, being significantly faster without losing quality, in generating smaller ensembles as obtained with the FastROCS or ROCS modes.
  - GetUseThompson
  - SetUseThompson
  - GetThompsonOptions
  - SetThompsonOptions
- A new class, OEThompsonOptions, has been added that enables controlling Thompson sampling during torsion driving.
- Generation of a single conformer with OEConformerBuilder has been modified to use Thompson sampling.

### 6.15.2 Minor bug fixes

- User-defined values passed through SetEnergyWindow, SetMaxConfs, and SetRMSThreshold are now properly accounted for, even when the corresponding defaults are range-based.
- . Molecule titles are retained when Build fails in OEOmega with fails to build structure from CT.
- A verbose log is provided for fragments that fail when Build fails in OEOmega with fails to build structure from CT.
- The OEOmegaIsGPUReady function has been safeguarded from a rare crash. The function has also been updated to check not only for device 0, but for devices from 0 to 100.

# **6.16 Quacpac TK 2.2.5**

### 6.16.1 Minor bug fixes

• Some issues with primary amines processing in OEMultistatepKaModel have been fixed.

# 6.17 Shape TK 3.7.0

### 6.17.1 New features

- A new method, AddColorGaussians, has been added that allows adding color Gaussians to the OEShapeQuery based on intensity of values on a grid.
- A new class, OEOverlapPrepOptions, has been added that allows modifying options that would be used during the Prep. Subsequently, a new constructor for OEOverlapPrep has been added that takes the OEOverlapPrepOptions as an argument.

### 6.17.2 Minor bug fixes

• Color force field names in OEColorFFParameter are now treated as case-insensitive.

# 6.18 SiteHopper TK 2.1.1

#### 6.18.1 Minor bug fixes

• The OESiteHopperIsGPUReady function has been safeguarded from a rare crash.

# 6.19 Spicoli TK 1.6.1

Minor internal improvements have been made.

# **6.20 Spruce TK 1.6.1**

#### 6.20.1 New features

- OEBuildSidechains now minimizes target side chains by default. Minimization can be controlled by setting minimizeSidechains and minimizeSidechainsShell options in the OESidechainBuilderOptions class.
- A feature has been added to support a next generation mmCIF feature, such that when an mmCIF file provides a connectivity record for the heterogens, **Spruce** will no longer look up the heterogen in the Chemical Component Dictionary but trust the input provided.
- A feature has been added that allows in-plane flipping of a single hydrogen on a double bonded nitrogen, when a clash is detected as part of hydrogen bond network optimization.

### 6.20.2 Major bug fixes

- An issue has been fixed related to using the OEHeterogenMetadata class, where the provided SMILES string was not respected for tautomer generation; when tautomers were not provided; and when the title (residue name) collided with existing residue names in the stored Chemical Component Dictionary.
- An issue has been fixed related to covalently bound ligands, where the pre-reaction input SMILES and related tautomers were not adjusted properly when accounting for the formed covalent bond.
- An issue has been fixed where the Spruce filter deleted single (disconnected) amino acid residues when they were marked HETATMs and were not real "floating" residues in part of the regular protein sequence.

### 6.20.3 Minor bug fixes

- OEMutateResidues, OEMutateResidue, and OEBuildSidechains now reduce failures arising from clashes by using shell minimization by default.
- An issue has been fixed that caused HEME-like molecules to be excluded from the stored chemical component database.

### **6.20.4 Documentation changes**

• Information has been added about setting and getting minimizeSidechains and minimizeSidechainsShell options in the OESidechainBuilderOptions class.

# 6.21 Szmap TK 1.7.1

Minor internal improvements have been made.

# 6.22 Szybki TK 2.8.0

#### 6.22.1 New features

• The constant SAGE\_OPENFF refers to the latest version of the Sage OpenFF force field.

# 6.23 Zap TK 2.5.0

Minor internal improvements have been made.

### **CHAPTER**

### **SEVEN**

### **RECENT RELEASE HISTORY**

# **7.1 OEToolkits 2024.1**

### 7.1.1 Release Highlights 2024.1.0

#### **EON: Overlay Optimization with Shape and Charge Density**

**EON**, the tool for molecular similarity based on shape and electrostatics, has been reimagined with the addition of charge density as a descriptor for electrostatic properties. By replacing electrostatic potential with molecular charge density as the primary descriptor of electrostatic properties, EON no longer requires the input molecules to be prealigned with the query molecule. Instead, EON now aligns the input molecules using shape- and electrostatics-based overlay optimization, where electrostatics are modeled via molecular charge density. EON still has the option to use electrostatic potential as a measure of similarity, if desired. Figure 1 shows an example of **EON** overlay with charge density visualization.

![](_page_54_Figure_7.jpeg)

Fig. 1: Figure 1. EON shape charge density overlay between two molecules.

Even with the addition of overlay optimization within the workflow, the new EON is now significantly faster compared to the previous version; and yet, as a tool for virtual screening with shape and charge similarity, the behavior of **EON** remains the same. When compared to ROCS, EON lags slightly when measured in terms of virtual screening success rates but excels in finding hits that are more chemically diverse.

Performance of the previous and current versions of EON, as compared to ROCS, are displayed in Figure 2. The comparisons were performed using multi-query directory of useful decoys (MDUD) datasets containing 38 targets. The current version of **EON** overlays and scores with shape and charge similarity. A command line flag -potential supports the rescoring of shape- and charge-aligned conformers with shape and electrostatic potential similarity. The current default version of **EON** is now almost as fast as **ROCS**, as can be seen in the right-hand plot below.

![](_page_55_Figure_1.jpeg)

Fig. 2: Figure 2. Comparison of performance of EON and ROCS for virtual screening success rate (left); for chemical diversity of actives found (middle); and for the speed of calculations (right). "Current" refers to the default version using shape and charge density for similarity, and "current (potential)" refers to **EON** using shape and electrostatics.

#### **FLYNN: Ligand fitting for Cryo-EM**

FLYNN, the tool for fitting small molecules to electron density, has been extended to support density maps generated through cryo-electron microscopy (cryo-EM).

**FLYNN** is a powerful tool for ligand fitting that uses adiabatic fitting to generate the best-fitting, lowest strain conformers consistent with experimental electron densities and structural models. This tool was one of the first to enable high-quality, physics-informed pockets and poses from X-ray crystallographic models. FLYNN has now been updated to enable researchers to access the same powerful insights from maps and models generated through cryo-electron microscopy (cryo-EM).

![](_page_55_Figure_6.jpeg)

Fig. 3: Figure 3. Ligand fitting with FLYNN to predict binding pockets and poses consistent with electron density from cryo-electron microscopy (cryo-EM).

#### **Hydrogen Placement Updates in SPRUCE**

In the 2024.1 release of **SPRUCE**, several improvements have been made to OEPlaceHydrogens to handle metal cation chelation effects on the nearby protonation states, specifically for ligands. The changes shown in Figure 5 below highlight new state and optimized geometries for sulfonamide, hydroxamate, phosphate, and borate groups. In addition, changes have been made around geometries for  $sp^3$  secondary amines. Lastly, improvements have been added in OE-ProtonateDesignUnit to allow for protonation state changes related to the detection of unfavorable acceptor-acceptor clashes, resulting in a more favorable hydrogen bond network.

### **1JD0- Sulfonamide Chelation**

![](_page_56_Figure_4.jpeg)

 $4IXU -$ **Chelation of Phosphates** 

# **1YQY-Hydroxamate Chelation**

![](_page_56_Figure_7.jpeg)

6SNN-**Acceptor-Acceptor Clashes** 

![](_page_56_Figure_9.jpeg)

![](_page_56_Figure_10.jpeg)

Fig. 4: Figure 4. Examples of improved chelator interactions and deprotonation rules for different moieties: hydroxamate, sulfonamide, and phosphates/borates. Also, on the bottom right, an example of improved interaction networks with acceptor-acceptor heuristic fixes.

#### **Bioisostere TK: New Toolkit for Bioisosteric Fragment Replacement**

The 2024.1 release introduces **Bioisostere TK**, a new toolkit for bioisosteric analog generation. It involves replacing a portion of a lead compound with fragments that have similar shape and electrostatics but with potentially novel connectivity and chemistry. This provides toolkit level access to the existing BROOD application functionality.

**Bioisostere TK** also brings several additional functionalities. At its core are tools for fragment-based modeling, such as fragment creation, fragment conformer generation, and fragment alignment and similarity in 3-dimensional space. Bioisostere TK brings OpenEye's shape-, color-, and electrostatics-based molecular similarity tools into fragmentbased similarity. It also exposes tools for the generation of 3D molecule conformers with fragment replacement.

An example of fragment alignment with **Bioisostere TK** based on shape and color is shown in Fopeigure 3. The attachment points in both the reference and fit fragments are marked in purple. The fragment overlay highlights how special attention is paid to the overlay of the attachment points.

![](_page_57_Figure_5.jpeg)

Fig. 5: Figure 5. Fragment overlay between a reference and a fit fragment.

#### **Supported Platforms**

| Package | Versions    | Linux                         | Windows           | macOS (x64 and arm64)                       |
|---------|-------------|-------------------------------|-------------------|---------------------------------------------|
| Python  | 3.9<br>3.12 | RHEL8/9, Ubuntu20/20-, ARM/22 | Win10/11          | 12, 13, 14                                  |
| C++     |             | RHEL8/9, Ubuntu20/20-, ARM/22 | Win10/11 (VS2022) | 12, 13, 14                                  |
| Java    | 8, 11, 20   | RHEL8/9, Ubuntu20/20-, ARM/22 | Win10/11          | 12, 13, 14 (only Java 20 support for arm64) |
| C#      |             |                               | Win10/11 (VS2022) |                                             |

#### **Related TK Versions**

| Toolkit        | Version |
|----------------|---------|
| Bioisostere TK | 4.0.0   |
| OEChem TK      | 4.1.0   |
| OEDepict TK    | 2.5.4   |
| OEDocking TK   | 4.3.1   |
| FastROCS TK    | 2.2.6   |
| OEFF TK        | 2.7.1   |
| Grapheme TK    | 1.5.1   |
| Graphsim TK    | 2.6.0   |
| Lexichem TK    | 2.9.1   |
| OEMedChem TK   | 1.2.2   |
| MolProp TK     | 2.6.4   |
| Omega TK       | 5.1.0   |
| Quacpac TK     | 2.2.4   |
| Shape TK       | 3.6.2   |
| SiteHopper TK  | 2.1.0   |
| Spicoli TK     | 1.6.0   |
| Spruce TK      | 1.6.0   |
| Szmap TK       | 1.7.0   |
| Szybki TK      | 2.7.1   |
| Zap TK         | 2.4.7   |

### **7.1.2 General Notices**

- Support for Java 20 is now available on all platforms.
- Support for macOS 14 has been added.
- Python 3.12 is now supported on all platforms.
- This release will be the last to support Ubuntu 20.04. Support for Ubuntu 24.04 will be added in the next release.

# **7.2 OEToolkits 2023.2**

#### 7.2.1 OEToolkits 2023.2.0

#### **Release Highlights**

- Sage force field (Sage 2.1.0), from the Open Force Field Consortium, is now available in **OMEGA** as a complement to MMFF94.
- The defaults for Sage force field from the Open Force Field Consortium have been updated to the latest 2.1.0 version, everywhere Sage is supported.
- The built-in fragment library in OMEGA has been updated; expanding on 80 K fragments in the previous library, the new fragment library contains approximately 540 K fragments.
- Stereo-enumeration options in Flipper have been improved to allow fine-grained control over enumerating different types of atom and bond stereocenters in an uncoupled manner.

- The torsion scanning algorithm in SZYBKI has been improved by adding the ability to optimize in internal coordinate space.
- Protein-ligand optimization with FF14SB-OpenFF in SZYBKI has been improved for performance and robustness.
- Support for PDBx/mmCIF in OEChem TK has been improved, following the format updates to PDB entries by wwPDB. The MMCIF reader now runs on Gemmi version 0.6.2.
- A preliminary API has been added to provide reaction automapping ability, based on the maximum common substructure, enhancing reaction support in OEChem TK.
- Python toolkit packaging has been improved to use pyproject.toml to declare metadata and dependencies.

#### **Supported Platforms**

| Package | Versions           | Linux                             | Windows              | macOS (x64 and arm64) |
|---------|--------------------|-----------------------------------|----------------------|-----------------------|
| Python  | 3.9, 3.10,<br>3.11 | RHEL8/9,<br>ARM/22<br>Ubuntu20/22 | Win10/11             | 12, 13                |
| C++     |                    | RHEL8/9,<br>ARM/22<br>Ubuntu20/22 | Win10/11<br>(VS2022) | 12, 13                |
| Java    | 8, 11              | RHEL8/9,<br>ARM/22<br>Ubuntu20/22 | Win10/11             | 12, 13                |
| C#      |                    |                                   | Win10/11<br>(VS2022) |                       |

#### **Related TK Versions**

| Toolkit       | Version |
|---------------|---------|
| OEChem TK     | 4.0.0   |
| OEDepict TK   | 2.5.3   |
| OEDocking TK  | 4.3.0   |
| FastROCS TK   | 2.2.5   |
| OEFF TK       | 2.7.0   |
| Grapheme TK   | 1.5.0   |
| Graphsim TK   | 2.5.7   |
| Lexichem TK   | 2.9.0   |
| OEMedChem TK  | 1.2.1   |
| MolProp TK    | 2.6.3   |
| Omega TK      | 5.0.0   |
| Quacpac TK    | 2.2.3   |
| Shape TK      | 3.6.1   |
| Sitehopper TK | 2.0.4   |
| Spicoli TK    | 1.5.7   |
| Spruce TK     | 1.5.3   |
| Szmap TK      | 1.6.7   |
| Szybki TK     | 2.7.0   |
| Zap TK        | 2.4.6   |

### **7.2.2 General Notices**

- Support for MacOS arm64 Java is now available.
- Python toolkits now use pyproject.toml to declare their metadata and dependencies, and no longer use the deprecated setup.py method.
- Python 3.11 is now fully supported on Windows.
- This is the last release to support MacOS 12. Support for MacOS 14 will be added in the next release.
- Python 3.12 will not be fully supported until the next release.
- This is the last release to support Python 3.9

# **7.3 OEToolkits 2023.1**

### 7.3.1 OEToolkits 2023.1.1

The OEToolkits 2023.1.1 is a bug-fix of the OEToolkits 2023.1.0 release.

- OEFF TK 2.5.2.1
- $\bullet$  Szybki TK 2.6.0.1

### 7.3.2 OEToolkits 2023.1.0

#### **Release Highlights**

#### **Supported Platforms**

| Package | Versions        | Linux              |                | Windows                   | macOS (x64 and arm64) |
|---------|-----------------|--------------------|----------------|---------------------------|-----------------------|
| Python  | 3.9, 3.10, 3.11 | RHEL8/9,<br>ARM/22 | Ubuntu20/20-22 | Win10/11 [no python 3.11] | 12, 13                |
| C++     |                 | RHEL8/9,<br>ARM/22 | Ubuntu20/20-22 | Win10/11 (VS2017/19/22)   | 12, 13                |
| Java    | 8, 11           | RHEL8/9,<br>ARM/22 | Ubuntu20/20-22 | Win10/11                  | 12, 13                |
| C#      |                 |                    |                | Win10/11 (VS2017/19/22)   |                       |

#### **Related TK Versions**

| Toolkit      | Version |
|--------------|---------|
| OEChem TK    | 3.4.0   |
| OEDepict TK  | 2.5.2   |
| OEDocking TK | 4.2.1   |
| FastROCS TK  | 2.2.4   |
| OEFF TK      | 2.5.2   |
| Grapheme TK  | 1.4.7   |
| Graphsim TK  | 2.5.6   |
| Lexichem TK  | 2.8.1   |
| OEMedChem TK | 1.2.0   |
| MolProp TK   | 2.6.2   |
| Omega TK     | 4.2.2   |
| Quacpac TK   | 2.2.2   |
| Shape TK     | 3.6.0   |
| Spicoli TK   | 1.5.6   |
| Spruce TK    | 1.5.2   |
| Szmap TK     | 1.6.6   |
| Szybki TK    | 2.6.0   |
| Zap TK       | 2.4.5   |

### **7.3.3 General Notices**

# 7.4 Release Highlights 2022.2

### 7.4.1 OEToolkits 2022.2.2

The OEToolkits 2022.2.2 is a bug-fix of the OEToolkits 2022.2.1 release.

• Release History

### 7.4.2 OEToolkits 2022.2.1

### 7.4.3 MCS based fix during OMEGA Conformer Generation

The ability to constrain a fragment of the molecules during conformer generation with torsion driving in OMEGA and the OMEGA toolkit has been extended to include fixing based on maximum common subgraph (MCS) match. In this mode of fixing, the MCS between the template fixmol and the generated molecule is determined, and subsequently that common subgraph portion of the generated molecule is fixed to the proved conformer of the fixmol.

The MCS based fixing during conformer generation can be turned on by setting OEConfFixOptions. SetFixMCS to true for use in the OMEGA toolkit. Additional API points have also been added to allow control during MCS search. A new flag -fixMCS is available in the OMEGA application to facilitate this.

![](_page_62_Picture_1.jpeg)

OMEGA generated conformers for two different molecules, with MCS based fix against a single bound ligand pose. Figure shows that with MCS based fix, two different fragments are fixed during conformer generation of the two different molecules.

### 7.4.4 New ShapeFit Algorithm for Pose Prediction

The algorithm for pose prediction with the OEPositMethod SHAPEFIT method has been modified. The new algorithm simultaneously optimizes the shape and chemical similarity between the fit molecule and bound ligand, and intra-molecular force-field energies of the fit molecule. The new simultaneous optimization algorithm replaces the previous adiabatic optimization algorithm and is more robust. The new algorithm also offers flexibility to use different forcefields and uses the OELigandFFType SAGE force field by default. Another advantage of the new algorithm is that it is capable of producing multiple distinct poses when desired. The new algorithm is automatically reflected in both the OEPosit toolkit and the POSIT application. ShapeFit is also now available in the OEDocking TK as an independent API OEShapeFit.

Cross-docking experiments based on the 22 diverse kinase types presented in [Tuccinardi-2010] shows that ShapeFit accuracy is unaffected between the previous and the new algorithm (when accuracy is measured as RMSD  $\leq$  =2.0). A balanced cross-docking set of 20,000 points, where points are equally distributed over the various similarity regions and kinase types, was used. However, we see clear indication that generating multiple poses helps increase the pose prediction accuracy. A separate self-docking study based on the highly trustworthy iridium dataset ([Warren-2012) with 280 ligand-protein structures shows that the new algorithm predicts poses that are closer to the x-ray crystallographic poses.

![](_page_63_Figure_1.jpeg)

Left: Comparison of ShapeFit accuracy in a cross-docking experiment between the existing and the new algorithm. The x-axis shows the tanimotocombo similarity between the ligand and the bound ligand present in protein complex. The Y-axis shows the fraction of accurately predicted poses based on being within 2 angstroms of the experimental pose. Right: Comparison of ShapeFit accuracy in a self-docking experiment, between the existing and the new algorithm. Axes show the RMSD of generated poses with respect to the experimental pose.

### 7.4.5 Protein-ligand Optimization with ff14SB forcefield and PB solvent model

Protein-ligand Optimization with ff14SB-OpenFF force field and Poisson-Boltzmann (PB) solvent model is now available both in SZYBKI and the SZYBKI toolkit.

In the SZYBKI TK, the functionality is available through the OEFixedProteinLigandOptimizer and the OEFlexProteinLigandOptimizer APIs, and can be enabled by setting OESolventModel PB as the value in OEProteinLigandOptOptions. SetSolventModel. In SZYBKI both the OptLigandInDU and OptimizeDU applications now accept pb as value for -solventModel.

Optimization of 244 highly trustworthy x-ray structures of protein-ligand complexes from the iridium dataset ([Warren-2012) with and without PB solvation and with ff14SB-Sage forcefield shows better accuracy for the optimized ligand poses when PB solvation is turned on. Accuracy is measured as the RMSD between the crystallographic ligand pose and the optimized pose. On an average PB solvation optimized structures have an RMSD of 0.31 angstroms, compared to a value of 0.55 angstroms when explicit solvation is not turned on. A paired T-test suggests that the average improvement of 0.24 angstroms is statistically significant with a p value of 0.00001. Turing on the solvation effects also removes any significant deviations (RMSD  $>$  2 angstroms) of pose, as was seen for a few cases when optimization was performed in vacuum.

### 7.4.6 New BROOD Fragment Databases

 $Tw$ **BROOD** brood-database-ChEMBL31 new fragment databases. and brood-database-ChEMBL31\_lite, built from the latest version of ChEMBL, have been generated and are made available. The brood-database-ChEMBL31 contains all possible fragments up to 3 attachment points, whereas the brood-database-ChEMBL31 lite is curated to prioritize fragments with medicinal relevance.

Limited validation, with 29 different queries across 14 molecules, shows that the number of hits of druglike molecules obtained from the new databases are within 1% of those generated from the existing database  $b$ rood-database-chembl-3.0.0, when a maximum of 1000 hits are requested. Comparison of belief score,

![](_page_64_Figure_1.jpeg)

Fig. 6: Comparison of RMSD for Flexible protein-ligand optimization of x-ray structures with and without PB solvation and with ff14SB-Sage forcefield.

a measure of potential activity of the generated hits, also shows that the hits generated from the new databases are at least as good as those generated from the existing database.

![](_page_64_Figure_4.jpeg)

Left: Comparison of the number of hits of druglike molecules using the brood-database-chembl- $3.0.0$ (ChEMBL20), brood-database-ChEMBL31 (ChEMBL31) and brood-database-ChEMBL31\_lite (ChEMBL31\_lite) fragment databases. Right: Comparison of the belief score distribution of all the hits generated using the ChEMBL20, ChEMBL31 and ChEMBL31 lite fragment databases.

#### **Supported Platforms**

| Package | Versions            | Linux                               | Windows                 | macOS  |
|---------|---------------------|-------------------------------------|-------------------------|--------|
| Python  | 3.7, 3.8, 3.9, 3.10 | RHEL7/8,<br>Ubuntu20/20-,<br>ARM/22 | Win10/11                | 11, 12 |
| C++     |                     | RHEL7/8,<br>Ubuntu20/20-,<br>ARM/22 | Win10/11 (VS2017/19/22) | 11, 12 |
| Java    | 1.8, 11             | RHEL7/8,<br>Ubuntu20/20-,<br>ARM/22 | Win10/11                | 11, 12 |
| C#      |                     |                                     | Win10/11 (VS2017/19/22) |        |

#### **Related TK Versions**

| Toolkit      | Version |
|--------------|---------|
| OEChem TK    | 3.3.1   |
| OEDepict TK  | 2.5.2   |
| OEDocking TK | 4.2.0   |
| FastROCS TK  | 2.2.3   |
| OEFF TK      | 2.5.1   |
| Grapheme TK  | 1.4.6   |
| Graphsim TK  | 2.5.5   |
| Lexichem TK  | 2.8.0   |
| OEMedChem TK | 1.1.7   |
| MolProp TK   | 2.6.1   |
| Omega TK     | 4.2.1   |
| Quacpac TK   | 2.2.1   |
| Shape TK     | 3.5.1   |
| Spicoli TK   | 1.5.5   |
| Spruce TK    | 1.5.1   |
| Szmap TK     | 1.6.5   |
| Szybki TK    | 2.5.1   |
| Zap TK       | 2.4.4   |

#### **General Notices**

- Support for macOS 12 has been added.
- This is the last release to support macOS 11. Support for macOS 13 will be added in the next release.
- Support for Ubuntu22 has been added. Support for Ubuntu18 has been dropped.
- This is the last release to support RHEL7. Support for RHEL9 will be added in the next release.
- This is the last release to support Visual Studio 2017 and Visual Studio 2019.

The detailed release notes consist of these highlights plus the individual release notes and the release history.

#### **CHAPTER**

# **PREVIOUS RELEASE HISTORY**

# 8.1 Release Highlights 2022.1

### 8.1.1 Enhanced Stereo Information Support

The 2022.1 release adds support for enhanced stereochemistry designations in molecules, defining relationships between stereocenters. Enhanced stereochemistry information on any molecule is honored by OEFlipper during stereo enumeration when asked to do so by setting appropriate options. Enhanced stereochemistry support has also been extended to both the OMEGA and the Flipper applications.

Support for CXSMILES as a valid molecular input format via OEFOrmat\_CXSMILES has been added. CXSMILES is specifically intended to support the import of Enamine download structure files containing enhanced stereochemistry designations. While many other features are possibly provided in the CXSMILES appendix information, only the enhanced stereochemistry group information is supported at this time. Please contact support@eyesopen.com with specific needs for additional CXSMILES features to allow prioritization in future releases.

**OMEGA** and **Flipper** applications can now accept molecule files in CXSMILES format.

![](_page_66_Figure_8.jpeg)

Fig. 1: Molecule with enhanced stereo designation. The molecule has 16 stereoisomers when stereocenters are treated independently and only 4 stereoisomers when the enhanced stereo is enabled.

### 8.1.2 Sheffield Solvation Model for Proteins

The simple two parameter Sheffield Solvation Model, as introduced by Grant et al. ([Grant-2007]) for calculating the electrostatic component of molecular solvation energy, is a semi-empirical model that performs well for small molecules and requires few computational resources. This model does not work well for macromolecules like proteins and complexes, where many of the atoms are hidden or only partially exposed to the solvent.

A modified three parameter Sheffield Solvation Model is parameterized and implemented in this release, where solvent exposure is treated by correcting the effective atomic radii with the introduction of a third additional parameter. The new model is available as part of the OESheffield API in the OEFF toolkit. The model is also available for use through the OEFixedProteinLigandOptimizer and the OEFlexProteinLigandOptimizer APIs in the **SZYBKI toolkit, and the OptLigandInDU and OptimizeDU applications in SZYBKI.** 

Electrostatic solvation energies for protein conformers are calculated using both the new Sheffield Solvation Model and the Poisson–Boltzmann (PB) model, and the difference in solvation energies between conformers of the same protein is compared between the two models. A set of 232 NMR proteins and peptide structures were used for this study that produced 41491 solvation energy differences between pairs of conformations. The results are compared in the image below.

![](_page_67_Figure_5.jpeg)

Fig. 2: Comparison between Sheffield and PB of differential electrostatic solvation energies between protein conformers.

### 8.1.3 Spruce Filter and Design Unit Validation

New functionality for preprocessing inputs and validation of the output Design Units has been added to Spruce TK in the form of two preliminary API classes OESpruceFilter and OEValidateDesignUnit. These classes are also used by the **SPRUCE** application to check and fix, if possible, inputs and to validate the resulting outputs.

OESpruceFilter performs a standardization and a filter check structures to use before prepping this structure in **SPRUCE**. It automatically checks and fixes invalid component names, invalid residue states, and invalid metal bonds. It also checks for invalid CRYST1 from the header file, low overlap between the electron density map and the structure, invalid sequence alignment, blank chain IDs, and invalid alternate locations. If the structure does not pass these tests, Spruce Filter will fail the structure.

The OEValidateDesignUnit function performs a check on the design units generated by **SPRUCE**. It will report if the provided DU contains partial side chains, missing loops, implicit hydrogens, incorrect partial charges, termini that are not capped properly, heavy atoms overlapping with each other, and broken chains.

### 8.1.4 Multistate Heuristic pKa Model

The multistate heuristic pKa model is an extension of the existing pKa model in **OpenEye** software. The existing model generates only one probable ionization state based on pKa estimated from about 80 rules. With the development of this multistate pKa model, we are enhancing the implementation with many more unique functional patterns in the form of pKa rules, identified from OpenEye's internal pKa database, allowing generation of all ionization states possible at physiological pH.

The model described herein uses SMARTS-based heuristics to assess the pKa of acidic or basic functional groups of molecules. For all atoms of a query molecule, pKa is assessed as it belongs to one of three classes: Acidic (pKa  $\lt$ 6.4), Basic (pKa > 8.4), and Neutral (6.4 < pKa < 8.4). According to the assessed pKa class for each atom, it is either ionized and/or un-ionized at pH 7.4. Any group with Acidic or Basic pKa range will result in one state, ionized or un-ionized and a group with Neutral pKa range will result in both states, ionized and un-ionized. Based on how many such functional groups there are in the molecule, and how many states are generated for them, multiple molecules can be generated for all possible combinations of all possible ionization states of acid/base groups.

The multistate heuristic pKa model is currently only available in **Quacpac TK** as preliminary API classes OEMultistatepKaModel and OEMultistatepKaModelOptions.

| Package | Versions            | Linux                            | Windows                 | macOS         |
|---------|---------------------|----------------------------------|-------------------------|---------------|
| Python  | 3.7, 3.8, 3.9, 3.10 | RHEL7/8, ARM<br>Ubuntu 18/20/20- | Win10/11                | 10.15, 11, 12 |
| C++     |                     | RHEL7/8, ARM<br>Ubuntu 18/20/20- | Win10/11 (VS2017/19/22) | 10.15, 11, 12 |
| Java    | 1.8, 11             | RHEL7/8, ARM<br>Ubuntu 18/20/20- | Win10/11                | 10.15, 11, 12 |
| C#      |                     |                                  | Win10/11 (VS2017/19/22) |               |

#### **Supported Platforms**

#### **Related TK Versions**

| Toolkit      | Version |
|--------------|---------|
| OEChem TK    | 3.3.0   |
| OEDepict TK  | 2.5.0   |
| OEDocking TK | 4.1.2   |
| FastROCS TK  | 2.2.2   |
| OEFF TK      | 2.5.0   |
| Grapheme TK  | 1.4.5   |
| Graphsim TK  | 2.5.4   |
| Lexichem TK  | 2.7.5   |
| OEMedChem TK | 1.1.6   |
| MolProp TK   | 2.6.0   |
| Omega TK     | 4.2.0   |
| Quacpac TK   | 2.2.0   |
| Shape TK     | 3.5.0   |
| Spicoli TK   | 1.5.4   |
| Spruce TK    | 1.5.0   |
| Szmap TK     | 1.6.4   |
| Szybki TK    | 2.5.0   |
| Zap TK       | 2.4.3   |

#### **General Notices**

- Support for macOS 12 has been added. macOS 10.14 is no longer supported.
- This is the last release to support macOS 10.15.
- A GCC 7.3 C++ toolkit package has been added for RHEL7.
- Support for Windows 11 has been added.
- Support for Visual Studio 2022 has been added.
- Support for Apple M1 architecture has been added for C++ and Python toolkits.
- Support for Linux ARM architectures has been added.
- This is the last release to support Ubuntu 18.04. Support for Ubuntu 22.04 will be added in the next release.

For detailed release notes, see Version 2022.1.0 Release Notes.

# 8.2 Release Highlights 2021.2

### 8.2.1 SiteHopper: New Toolkit for Protein Binding Site Comparison

The 2021.2 release introduces SiteHopper TK, a new toolkit for searching a database containing design units for proteins with similar binding sites to a query design unit. The new SiteHopper TK provides toolkit level access to the **SiteHopper** application functionality released in 2021.1.

Besides providing toolkit level access, the 2021.2 release also brings several other improvements to SiteHopper. Efficiency of database building in SiteHopper is enhanced with the use of a multi-threaded approach. Furthermore, search is now possible on the CPU, enabling cross platform support of the toolkit and application. On Linux machines with an NVIDIA graphics card, the GPU is used as a pre-screening method, speeding up the search dramatically. A feature to exclude results based on a similarity threshold has been added that allows for more diversity in the protein targets with similar binding sites. The database storage format has also been revised.

An example of a **SiteHopper** produced hit is shown in the figure below. 1UYG is a structure of human heat shock protein 90-alpha, bound to 8-(2,5-dimethoxy-benzyl)-2-fluoro-9H-purin-6-ylamine. 5IUN is a structure of the DesK-DesR complex, bound to AMP-PCP. The image on the left shows the overlay of 1UYG (green) and 5UIN (light yellow), zoomed out to show the major structural differences between the two proteins. The image on the right zooms in on the binding sites, with a surface showing the type of residues present in each binding site. Blue represents acidic, red represents basic, yellow represents polar, and white represents non polar. Despite a sequence similarity of only 46%, 1UYG and 5IUN may be targetable by similar ligands, as they have very similar steric and electrostatic properties in their binding sites.

![](_page_70_Picture_3.jpeg)

1UYG human hsp 90 (green) overlaid with 5UIN N-formyltransferase (yellow), full struture view (left), binding site view (right).

### 8.2.2 SZYBKI: OpenFF-Sage force field support

The latest force field, Sage, from the Open Force Field Initiative has been added to OEFF TK, Szybki TK, and **SZYBKI**. The major features of the **Sage** force field are outlined here.

New force field parameter classes OESageParams and OEFF14SBSageParams have been added to the toolkit to support the Sage parameters. Three new force field classes, OESage, OEFF14SBSage, and OEFF14SBSageComplex, have also been introduced. The Sage force field is now the default for free energy analysis of conformation ensembles with OEFreeFormConf, and the corresponding application **Freeform**. The protein-ligand forcefield, **FF14SBSage**, is now the default for protein-ligand optimization in OEFixedProteinLigandOptimizer and OEFlexProteinLigandOptimizer, OptimizeDU, and OptLigandInDU.

The Sage force field can be used in SZYBKI for ligand calculations, with the  $-ff$  sage\_openff2.0.0 command line option, and for calculations involving proteins using -ff ff14sb\_sage.

### 8.2.3 OEChem: MMCIF and CIF writers

Functionality to write Crystallographic Information Files (CIF and MMCIF) has been added to the OEChem TK in the 2021.2 release. Similar to writing other molecule file formats in OEChem TK, CIF and MMCIF files can be written using the high level OEWriteMolecule function. Low level functionality for advanced users is also provided through a new OEWriteCIFFile function.

If the molecule does not contain residue information, it is written as a small molecule CIF file if the data is available to do so (i.e. space group information). If residue information is available, the writer checks the number of residues and the molecule is either written as a chemical component dictionary entry (in the event there is a single residue) or as a macromolecular CIF file (MMCIF).

The small molecule CIF reader has also been improved for performance and robustness, and round-tripping these files has been tested and validated using the checkCIF facility from the International Union of Crystallography (IUCR). The MMCIF parser based on Gemmi has also been updated, and items parsed from PDB metadata have been expanded for proper processing of the biomolecules with Spruce.

#### **Supported Platforms**

| Package | Versions      | Linux                | Windows                | macOS            |
|---------|---------------|----------------------|------------------------|------------------|
| Python  | 3.7, 3.8, 3.9 | RHEL7/8, Ubuntu18/20 | Win10                  | 10.14, 10.15, 11 |
| C++     |               | RHEL7/8, Ubuntu18/20 | Win10 (VS2017, VS2019) | 10.14, 10.15, 11 |
| Java    | 1.8, 11       | RHEL7/8, Ubuntu18/20 | Win10                  | 10.14, 10.15, 11 |
| C#      |               |                      | Win10 (VS2017, VS2019) |                  |

#### **Related TK Versions**

| Toolkit             | Version |
|---------------------|---------|
| <b>OEChem TK</b>    | 3.2.0   |
| <b>OEDepict TK</b>  | 2.4.7   |
| <b>OEDocking TK</b> | 4.1.1   |
| <b>FastROCS TK</b>  | 2.2.1   |
| <b>OEFF TK</b>      | 2.4.0   |
| Grapheme TK         | 1.4.4   |
| Graphsim TK         | 2.5.3   |
| Lexichem TK         | 2.7.4   |
| <b>OEMedChem TK</b> | 1.1.5   |
| MolProp TK          | 2.5.7   |
| Omega TK            | 4.1.2   |
| Quacpac TK          | 2.1.3   |
| Shape TK            | 3.4.3   |
| Spicoli TK          | 1.5.3   |
| Spruce TK           | 1.4.0   |
| Szmap TK            | 1.6.3   |
| Szybki TK           | 2.4.0   |
| Zap TK              | 2.4.2   |

#### **General Notices**

- This is the last release to support macOS 10.14. Support for macOS 12 will be added in the next release.
- A gcc 7.3 C++ toolkit package has been added for RHEL7.
- Support for Windows 11 will be added in the next release.

# 8.3 Release Highlights 2021.1

### 8.3.1 OEDocking TK: Receptors in Design Unit

OEReceptor as an integral part of an OEDesignUnit, with properly prepped structures and contained in an OEDU file, is fully integrated in all workflows. Receptors in an OEDesignUnit can now be created using the Make Receptor GUI application, as well as the SPRUCE and ReceptorInDU command-line applications.

The Make Receptor GUI application has been extended to be a fully functional DesignUnit builder in addition to building receptors. A new DesignUnit can be created from a PDB/MMCIF file (with or without an associated MTZ file), or by combining molecules from various molecule files of any format. **SPRUCE** options are exposed through a graphical interface giving users control over the level of preparation the structure should go through. Existing receptors, both in OEDU or OEB format, can also be opened and edited as desired in Make Receptor.

OEMakeReceptor now automatically detects protein constraints. The detected protein constraints are kept disabled by default, and can be completely turned off if desired, functionality that was previously only available in the Make **Receptor** application. Both the detected constraints and any custom constraints can be enabled and edited via the OEMakeReceptor interface, or using commands from OEReceptorProteinConstraint and OEReceptorCustomConstraints classes in the toolkit.

Having the receptors as part of the OEDesignUnit with properly prepped structures makes it easier for the docked and posed structures to be used in further downstream modeling, which is especially necessary when working with protein force fields like FF14SB. The new receptors with properly prepped protein also enabled use of modern force fields like FF14SB and Parsley for structure optimization in flexible OEPosit.

### 8.3.2 OESiteHopper: Application Suite for Rapid Protein Binding Site Comparison

The 2021.1 release introduces SiteHopper, which can search a database containing hundreds of thousands of proteins in a few minutes for proteins with similar binding sites to a query protein. **SiteHopper** will output the most similar biomolecules, overlaid by binding site, for visualization and analysis. A visual representation of the binding site is also output. SiteHopper can also create databases for searching from a series of biomolecular structures in OEDU format.

**SiteHopper** finds proteins with similar binding sites which searching by sequence similarity would overlook. An example is shown in the figure below. 1UYG is a structure of human heat shock protein 90-alpha, bound to 8-(2,5dimethoxy-benzyl)-2-fluoro-9H-purin-6-ylamine. 5IUN is a structure of the DesK-DesR complex, bound to AMP-PCP.

The image on the left shows the overlay of 1UYG (green) and 5UIN (light yellow), zoomed out to show the major structural differences between the two proteins. The image on the right zooms in on the binding sites, with a surface showing the type of residues present in each binding site. Blue represents acidic, red represents basic, yellow represents polar, and white represents non polar. Despite a sequence similarity of only 46%, 1UYG and 5IUN may be targetable by similar ligands, as they have very similar steric and electrostatic properties in their binding sites.

![](_page_73_Figure_1.jpeg)

Fig. 3: OEDocking receptor for the 3TPP BACE1 Complexed with Inhibitor with target structure, bound ligand, and a protein constraint. Displayed in the Make Receptor viewer.

![](_page_73_Figure_3.jpeg)

1UYG human hsp 90 (green) overlaid with 5UIN N-formyltransferase (yellow), full struture view (left) and binding site view (right).

### 8.3.3 VIDA 5: Major Update and OEDesignUnit Support

VIDA has undergone major changes including:

- Upgrade to Python3.
- Upgrade to Qt5 with PySide2 providing for user-interface improvements.
- Updated to run on the same platforms as OpenEye Toolkits and Applications.

This allows us to release VIDA along side the toolkits and applications in our twice-yearly releases.

In addition, VIDA now has support for MMCIF files and improvements to I/O from other file format types. VIDA can also read prepared protein structures in OEDesignUnit format produced with SPRUCE and Make Receptor along with the receptor objects that are now stored on these design units.

![](_page_74_Figure_8.jpeg)

Fig. 4: VIDA DesignUnit Support with receptors showing the prepared beta-secretase structure 3TPP.

### **8.3.4 Supported Platforms**

| Package | Versions      | Linux                | Windows                | macOS            |
|---------|---------------|----------------------|------------------------|------------------|
| Python  | 3.7, 3.8, 3.9 | RHEL7/8, Ubuntu18/20 | Win10                  | 10.14, 10.15, 11 |
| C++     |               | RHEL7/8, Ubuntu18/20 | Win10 (VS2017, VS2019) | 10.14, 10.15, 11 |
| Java    | 1.8, 11       | RHEL7/8, Ubuntu18/20 | Win10                  | 10.14, 10.15, 11 |
| C#      |               |                      | Win10 (VS2017, VS2019) |                  |

### 8.3.5 Related TK Versions

| Toolkit      | Version |
|--------------|---------|
| OEChem TK    | 3.1.1   |
| OEDepict TK  | 2.4.6   |
| OEDocking TK | 4.1.0   |
| FastROCS TK  | 2.2.0   |
| OEFF TK      | 2.3.1   |
| Grapheme TK  | 1.4.3   |
| Graphsim TK  | 2.5.2   |
| Lexichem TK  | 2.7.3   |
| OEMedChem TK | 1.1.4   |
| MolProp TK   | 2.5.6   |
| Omega TK     | 4.1.0   |
| Quacpac TK   | 2.1.2   |
| Shape TK     | 3.4.2   |
| Spicoli TK   | 1.5.2   |
| Spruce TK    | 1.3.0   |
| Szmap TK     | 1.6.2   |
| Szybki TK    | 2.3.1   |
| Zap TK       | 2.4.1   |

### **8.3.6 General Notices**

- C++ CUDA-enabled toolkits and features are now supported on RHEL8 and Ubuntu20.
- Support for GCC 9.x has been added. Support for GCC 4.x and GCC 5.x has been dropped.
- Support for Python 3.6 has been dropped.
- Support for VS2015 has been dropped.
- Support for MacOS 11 has been added. Support for MacOS 10.13 has been dropped.
- OpenEye applications and toolkits have not been optimized for the M1 Mac but run under Rosetta 2.

# 8.4 Release Highlights 2020.2

#### 8.4.1 OEToolkits 2020.2.2

The OEToolkits 2020.2.2 is a bug-fix of the OEToolkits 2020.2 release. Click on the below links for more information about the bug fixes in this release:

- $\bullet$  OEChem TK 3.1.0.2
- OEDocking TK 4.0.0.2
- Quacpac TK  $2.1.1.2$

### 8.4.2 Omega TK: New fragment library

A new enhanced fragment library has been created for use in **Omega TK**. The new fragment library consists of more than 500,000 fragments that have been generated using the MMFF force field.

This new library is designed to reduce the run time of large-scale conformer generation, and therefore is not built in to **Omega TK** but is available as a separate download. To run **Omega TK** with the enhanced library, simply use the OEOmega method OEOmega.AddFragLib.

The fragments have been collated from commonly used electronic databases, such as Enamine Building Blocks. Consequently, dramatic runtime performance improvements can be seen for the Enamine Real dataset, among others, since less time is spent building fragments on the fly. Runtime performance improvements can be seen for all datasets; the Platinum and Enamine Real sets show particular improvement and run ~50% faster (benchmarks run on Ubuntu 16 with Intel(R) Xeon(R) Gold 6128 CPU 3.40GHz and NVIDIA Tesla V100 GPU).

![](_page_76_Figure_5.jpeg)

Fig. 5: GPU-OMEGA runtime performance using the built-in fragment library compared to the new enhanced fragment library. Benchmark datasets are a filtered set of 2359 molecules of the Platinum dataset and 10,000 randomly chosen molecules of the Enamine Real, Mcule and WuXi databases.

The enhanced fragment library generates the same high-quality conformers as the built-in library, as shown by the minimum RMSDs of the filtered Platinum dataset.

#### Datasets can be downloaded from:

- Mcule
- Enamine Real

![](_page_77_Figure_1.jpeg)

Fig. 6: Box plots showing minimum RMSDs of a filtered set of 2359 molecules of the Platinum dataset with the built-in fragment library and the new enhanced fragment library.

- Platinum Dataset
- $\bullet$  WuXi

We are eager to get your feedback on the new enhanced fragment library. Please share your experience with us at support@eyesopen.com.

### 8.4.3 OEDocking TK: Improved receptors

Receptors used in OEDocking TK classes, including FRED, HYBRID, and POSIT, have been improved to take advantage of properly prepared structures from SPRUCE. A new OEReceptor object has been introduced and is created and contained within an OEDesignUnit. Since an OEReceptor is now an integral part of an OEDesignUnit, it is saved into an OEDU file along with a design unit. There is no separate I/O for the receptors.

Having the receptors as part of the design unit with properly prepped structures makes it easier for the docked and posed structures to be used in further downstream modeling, which is especially necessary when working with protein force fields like FF14SB. The new receptors with properly prepped protein also enabled use of modern force fields like FF14SB and Parsley for structure optimization in flexible OEPosit.

![](_page_78_Figure_1.jpeg)

Fig. 7: OEDocking receptor, along with the target structure and the bound ligand, for the 2IKO Human Renin Complexed with Inhibitor.

# 8.4.4 Szybki TK: A new protein force field

The AMBER FF14SB protein force field has been implemented in OEFF TK. This new force field has also been made available in SZYBKI for optimizing both protein and protein-ligand complexes.

FF14SB is the most widely used protein force field for molecular dynamics or any other force field-based calculations. It is also used in Orion molecular dynamics package, and is the community gold standard for such calculations.

### **8.4.5 Supported Platforms**

| Package | Versions            | Linux                   | Windows                        | macOS                     |
|---------|---------------------|-------------------------|--------------------------------|---------------------------|
| Python  | 3.6,<br>3.7,<br>3.8 | RHEL7/8,<br>Ubuntu18/20 | Win10                          | 10.13,<br>10.14,<br>10.15 |
| C++     |                     | RHEL7/8,<br>Ubuntu18/20 | Win10 (VS2017, VS2019)         | 10.13,<br>10.14,<br>10.15 |
| Java    | 1.8, 11             | RHEL7/8,<br>Ubuntu18/20 | Win10                          | 10.13,<br>10.14,<br>10.15 |
| C#      |                     |                         | Win10 (VS2015, VS2017, VS2019) |                           |

### 8.4.6 Related TK Versions

| Toolkit      | Version |
|--------------|---------|
| OEChem TK    | 3.1.0   |
| OEDepict TK  | 2.4.5   |
| OEDocking TK | 4.0.0   |
| FastROCS TK  | 2.1.0   |
| OEFF TK      | 2.3.0   |
| Grapheme TK  | 1.4.2   |
| Graphsim TK  | 2.5.1   |
| Lexichem TK  | 2.7.2   |
| OEMedChem TK | 1.1.3   |
| MolProp TK   | 2.5.5   |
| Omega TK     | 4.1.0   |
| Quacpac TK   | 2.1.1   |
| Shape TK     | 3.4.1   |
| Spicoli TK   | 1.5.1   |
| Spruce TK    | 1.2.0   |
| Szmap TK     | 1.6.1   |
| Szybki TK    | 2.3.0   |
| Zap TK       | 2.4.0   |

### **8.4.7 General Notices**

- Support for Ubuntu20 has been added. Ubuntu16 is no longer supported.
- C++ CUDA-enabled toolkits and features are now supported on RHEL8 and Ubuntu18.
- This is the last release to support GCC 4.x and GCC 5.x. GCC 7.4 will be the minimum GCC supported in the next release.
- This is the last release to support Python 3.6.
- This is the last release to support VS2015.

# 8.5 Release Highlights 2020.1

### 8.5.1 OEToolkits 2020.1.1

The OEToolkits 2020.1.1 is a bug-fix of the OEToolkits 2020.1 release.

- OEChem TK 3.0.0.6
- $\bullet$  Omega TK 4.0.0.6

### 8.5.2 OEToolkits 2020.1

The OEToolkits 2020.1 is a bug-fix of the OEToolkits 2020.0 release.

- OEChem TK 3.0.0.5
- OEDocking TK 3.5.0.5

### 8.5.3 OEToolkits 2020.0

**OpenEye Toolkits** and Applications are now integrated into a single release cycle. This integration ensures that the tools delivered are more consistent across various product levels and, in keeping with OpenEye standards, are robust and efficient. In addition, the integration reduces release process management time, allows more time to deliver new features, and facilitates delivering bug-fix releases for critical issues when needed.

#### Omega TK: GPU-Omega - GPU-accelerated torsion driving

The 2020.0 release introduces GPU-Omega to the Omega TK. GPU-Omega provides accelerated torsion driving by utilizing a GPU (Graphics Processing Unit). GPU-Omega is integrated into the existing Omega TK; no additional user actions are required to make use of this new feature. GPU-Omega detects any supported Nvidia GPU on Linux platforms and accelerates torsion driving automatically unless explicitly suppressed through the option OETOrDriveOptions. SetUseGPU. GPU-Omega is available with all sampling modes except macrocycle, which does not use the torsion driving method for conformer generation. For more details on GPU-Omega, including prerequisites and additional requirements for use with dense mode, please see GPU-Omega.

GPU-Omega performs at the same high level of accuracy as Omega TK, as shown below using a filtered subset of the Platinum dataset [Friedrich-2017] [Hawkins-2020]:

GPU-Omega was benchmarked against the CPU on AWS to demonstrate the achievable performance on a P3 instance, which houses an Nvidia Tesla V100 GPU. GPU-Omega was benchmarked with all supported sampling modes (sparse, dense pose, rocs, and fastrocs) using a subset of ~6000 molecules from the GSK TCAMs dataset [Gamo-2010]. The most impressive speed-up is seen with the dense sampling mode, with a reduction in time from 120 hours to less than 4 hours with GPU-Omega.

#### **FastROCS TK: Color optimization on GPU**

Overlay optimization by color, in addition to shape, has been added to **FastROCS**. The color adds chemistry in the superposition and similarity analysis process, and thus facilitates identifying compounds that are similar both in shape and chemistry. FastROCS with color optimization was carried out on K80, M60, and V100 instances on AWS GPU instances and compared against those without color optimization:

Previous versions of FastROCS optimized over the shape score and followed that with a single point calculation for color. This can result in overlooking promising molecules. An example of the effect of optimizing over color and shape overlap rather than just shape overlap is shown below for XIAP BIR3 [Ndubaku-2009]:

On the far left is the XIAP BIR3 binding site with its crystallographic ligand in green. In the center is the crystallographic ligand, as well two copies of a known active ligand from the DUDE dataset [Mysinger-2012], with the best overlay from FastROCS without and with color optimization, respectively. Without color optimization, the ligand is not predicted to have high shape or chemical similarity. When color optimization is used, a high degree of chemical and volumetric overlap is predicted, as would be expected given that this compound is a known active. On the far right is the overlay in the binding site of XIAP BIR3, occupying a similar pose to the crystallographic ligand.

![](_page_81_Figure_1.jpeg)

Fig. 8: Comparison of the minimum RMSDs of CPU- and GPU-generated conformers against the experimental coordinates of a filtered subset of the Platinum dataset

#### **Spruce TK: Protein Loop Modeling**

The 2020.0 release adds protein loop modeling to **Spruce TK**. This feature is available with the lower level APIs OEBuildSingleLoop and OEBuildLoops. It is also incorporated as an option in the high level structure preparation API OEMakeDesignUnit.

The approach relies on a template database built from structures in the public RCSB Protein Data Bank. The database, which has been built for modeling loops that are 4-20 residues long by default, is available for download in a platformindependent format. An application in the **SPRUCE** bundle allows appending additional structures to the existing database. For example, proprietary in-house structures can be added, or the database can be completely rebuilt from scratch with different options.

This approach has been validated on a public dataset from Rossi et al. [Rossi-2007]. The results shown below were generated by building the excised loops back into the dataset, where the specific structures themselves were not part of the template database, and used the same success criterion as in the paper (<2.5A backbone RMSD). The results are generally good and the median RMSD is 0.6-0.7A (blue dots), irrespective of the length of the modeled loop. The unsuccessful cases (gray bar) have a large effect on the average RMSD (green dots), as loops are chosen that deviate significantly from the expected. Only in a single case of the  $\sim$ 200 loops modeled was a result not produced (red bar) that survived the search and filtering steps.

For the full list of new preliminary APIs, see Spruce TK 1.1.0 Release Notes.

![](_page_82_Figure_1.jpeg)

Fig. 9: Elapsed time comparison between Omega and GPU-Omega on an AWS P3 instance when sampling a subset of the GSK-TCAMS dataset with sparse, rocs, fastrocs, pose, and dense modes.

#### **OEChemTK: Data record preliminary API**

A preliminary API for OERecord and its associated classes has been added to OEChem TK. OERecord is a data container for storing and transmitting strongly typed data and its associated metadata. A pure Python implementation of **OERecord** has been in use by **ORION** and **Floe**; the new C++ implementation improves performance and memory management, and makes data records available to **OpenEye** toolkit code. The API is only available in C++ and Python at this time.

### **8.5.4 General Notices**

- Support for macOS Catalina 10.15 has been added. MacOS 10.12 is no longer supported.
- RHEL8 is supported across all toolkits except for the C++ CUDA-enabled toolkits and features. FastROCS TK, GPU-Omega TK, and GraphSim TK's CUDA fast fingerprints are not supported.
- C++ CUDA-enabled toolkits and features are not available on Ubuntu18. FastROCS TK, GPU-Omega TK, and GraphSim TK's CUDA fast fingerprints are not supported.
- C++ toolkits are now available for GCC 8.x.
- Support for Python 3.8 has been added for all supported platforms. Python 3.6 is no longer supported for Windows toolkits.
- Java toolkits are now available for macOS.
- Visual Studio 2019 toolkits are now available for C++ and C#.

![](_page_83_Figure_1.jpeg)

Fig. 10: Performance comparison for FastROCS with and without color optimization in the 2020.0 release, using OpenEye's standard benchmark dataset of 14M conformers on AWS.

![](_page_83_Figure_3.jpeg)

Fig. 11: Example of the improvement using color optimization in FastROCS

- This is the last release to support Ubuntu16.04. Support for Ubuntu20.04 will be added in the next release.
- Memory management in the Java toolkits no longer relies on the JVM to clean up objects. The new memory management significantly improves the Java toolkits performance, however requires users to manage memory. See Best Practices for Java for current best practices.

![](_page_84_Figure_1.jpeg)

Fig. 12: Performance assessment building loops ranging from 4-12 residues in length. Errors are when no loop was produced, failures when the backbone RMSD is larger than 2.5A from the original structure.

# 8.6 OEToolkits 2019.Oct

### 8.6.1 Spruce TK: A new toolkit for biomolecular structure preparation

The 2019.Oct release introduces Spruce TK. Spruce TK takes experimental biomolecular structure data in either PDB or mmCIF formats, and prepares the structures for use with downstream modeling applications, such as docking with FRED or HYBRID, pose prediction with POSIT, identifying favorable and unfavorable waters with SZMAP or free energy calculations using molecular dynamics simulations.

With Spruce TK, users can easily prepare proteins using either C++ or Python APIs (see OEMakeDesignUnits), where the output of the file is the recently developed OEDesignUnit class and is serialized to a new OEDU file format. The prepared system is componentized into molecular categories including *protein*, *ligand*, *nucleic*, *solvent*, and many other molecular types common to biomolecular experiments. By default, hydrogens are added to systems using a tautomer search for any ligand, cofactor, or other nonstandard residue molecules. In addition, the system is split into distinct biological units, and all final design unit structures are superposed into the common frame of reference of a parent structure. For more details, see Spruce theory.

Spruce TK has been tested across a broad range of industry-relevant targets. It has been used in virtual screening and molecular dynamics simulations in Orion, as well as to prepare structures for loading into the MacroMolecular Data Service (MMDS).

### 8.6.2 OEChem TK: Fast Substructure Search

Substructure search is a fundamental task in cheminformatics. OEChem TK now provides improved substructure search capability, allowing users to search tens of millions of molecules in seconds.

**OEChem TK** uses the screen-based approach to accelerate the search process. Screens are bit vectors encoding global and local features of molecules. They are prebuilt and can be used to rapidly eliminate structures that could not be matched to a query molecule. Only molecules that pass the screen are subjected to the computationally more expensive atom-by-atom matching for validation. OEChem TK provides three types of built-in screens based on the source of the query molecule: MDL, SMARTS, and Molecule. All screens are rigorously tested using diverse sets of queries and multiple molecule databases to ensure that they do not eliminate true positive matches.

The new multi-threaded substructure search can be performed in two modes: in-memory and molecule-database. The in-memory mode provides the fastest way to search a dataset, but it is memoryintensive as it holds both screens and molecules in memory. The molecule-database mode keeps only the screens in memory; only molecules with unmatching screens have to be loaded into the memory. This method can be slower but uses significantly less memory, allowing users to search larger datasets.

![](_page_85_Figure_5.jpeg)

See the Molecule searching chapter of **OEChem TK** for examples using the new OESubSearchDatabase class. For the full list of new preliminary APIs, see OEChem TK 2.3.0.

### 8.6.3 OEFF TK: SMIRNOFF

The 2019.Oct release incorporates the SMIRNOFF small molecule force field from the Open Force Field Initiative into OEFF TK. The force field can handle almost all pharmaceutically relevant chemical space.

The SMIRNOFF force field differs from traditional force fields principally in the data representation of the chemistry. It uses extended SMARTS strings for parameters instead of atom types, greatly reducing the number of interdependent parameters. It currently adopts the functional form of the AMBER force field, but the Open Force Field Initiative is actively examining improvements to this. OEFF TK intends to include the most up-to-date version of the force field in its own releases whenever possible.

### **8.6.4 General Notices**

- This is the last release to support macOS 10.12. Full support for macOS 10.15 will be added in the next release.
- This is the last release to support RHEL6. Full support for RHEL8 will be added in the next release.
- The 2019.Oct release skips Java support for macOS. For Java support on RHEL6, please contact support@eyesopen.com.
- A new search engine that provides better hits and shows results in a much cleaner format has been added to the documents.
- The 2019. Oct release now uses SWIG 3.0.12 for generating C#, Java, and Python wrappers. C# and Python use SWIG's built-in support for wrapping C++ std::vector and string types.

# 8.7 OEToolkits 2019.Apr

### 8.7.1 FastROCS TK: Color calculation on GPU

Changes to the **FastROCS** algorithm, including porting the static color calculation to GPU, have resulted in a more than 2x performance improvement of FastROCS on some GPU systems. Benchmarking was carried out on AWS GPU instances and compared to the 2018. Oct version of FastROCS TK:

![](_page_86_Figure_10.jpeg)

#### Fig. 13: Performance comparison between the 2018.Oct release and the 2019.Apr release using OpenEye's standard benchmark dataset of 14M conformers on AWS.

For some systems, the standard benchmark dataset of 14M conformers is not large enough to fully saturate the GPUs. To demonstrate the potential performance of larger databases, a 2 billion conformer subset of Enamine was searched on suitable AWS instances. FastROCS searched the 2 billion conformer database on an AWS P3 instance with 8x Nvidia Tesla V100 GPUs at a rate of over 44 million overlays per second:

![](_page_87_Figure_1.jpeg)

Fig. 14: Performance of a 2 billion conformer subset of Enamine on suitable AWS instances.

### 8.7.2 OEChem TK: OEZ compressed file format

A new compressed file format with the extension  $\phi$ ez has been added to **OEChem TK**. This format uses the Zstandard algorithm to efficiently compress individual multi-conformer molecules, making it well-suited to work with OEMolDatabase for fast read-only random access to molecules. See more details in the Compressed Input and Output section of the OEChem TK documentation.

### 8.7.3 OEGrapheme TK: Ramachandran plot

Following our tradition of providing easily comprehensible visualization of complex data, OEGrapheme TK can now depict Ramachandran plots ([Ramachandran-1963]). These plots provide an easy way to examine the distribution of backbone dihedral angles in a particular protein. For instance, structure quality can be assessed by identifying residues whose backbone  $\psi$  are outside energetically accessible regions. Grapheme TK uses the data and classifications available in OEBio TK, which were extracted from the open-source Computational Crystallography Toolbox [Grosse-Kunstleve-2002].

### **8.7.4 General Notices**

- OpenEye currently uses OpenJDK8 to build its Java packages. We are currently exploring support for OpenJDK 11.
- The 2019.Apr release skips Java support for macOS. For Java support on RHEL6, please contact support@eyesopen.com.
- This release adds support for macOS 10.14. OS X 10.11 is no longer supported.
- This release adds support for Ubuntu 18. Ubuntu 14 is no longer supported.
- Visual Studio 2017 support has been added for C++ and C#. This is the last release to support Visual Studio 2013, as well as 32-bit Windows for C++ and C#.
- Full support has been added for Python 3.7. Python 3.5 for Windows is no longer supported.

- The following prerequisites have been introduced so that **OpenEve** can implement algorithms in a more modern and efficient C++11 style:
  - GCC 4.8 is now the oldest targeted compiler for toolkits. RHEL6 with the default GCC 4.4 compiler is no longer supported.
  - $-$  The minimum recommended GNU binutils version is 2.26 for the C $++$  single-build Linux packages.
  - The minimum CMake version required to build the C++ examples is now  $3.1.3$  on all platforms.

# 8.8 OEToolkits 2018.Oct

### 8.8.1 Omega TK: Macrocycle

A new distance geometry-based, conformational space-sampling method has been added to **Omega TK** as a preliminary API. This approach opens up a new avenue for exploring conformer ensembles in **Omega TK**. Although the distance geometry-based sampling is slower than the traditional torsion driving-based approach, it works substantially better for ensemble generation of macrocyclic molecules. This sampling method can also be applied to linear and small ring-containing molecules.

![](_page_88_Figure_8.jpeg)

Fig. 15: Conformer ensemble subset for geldanamycin (PDB: 1YET) generated using the macrocycle method

### 8.8.2 FastROCS TK: C++ and Java Support

Previously, FastROCS TK was available only in Python. This release extends support to C++ and Java. All classes, functions, and constants are wrapped and available for use. Several example scripts now have C++ and Java versions to showcase FastROCS TK functionalities. Additionally, users running FastROCS TK on Tesla GPUs will see a 10-30% speed-up over the previous version, depending on the system.

### 8.8.3 Quacpac TK: Tautomers

This release adds several improvements to the tautomer functionality in Quacpac TK. Tautomer handling in molecular modeling and cheminformatics usually includes three important functions:

- Generating a canonical protomer representation for duplicate-free storage
- Generating a single tautomer suitable for visualization by chemists and modelers
- Generating an ensemble of aqueous-phase tautomers suitable for molecular modeling

![](_page_89_Figure_8.jpeg)

Fig. 16: Example of generating an ensemble of biologically relevant tautomers

This release provides new API to cover each of these use-cases. The algorithm has also been improved to handle memory usage when a large number of possible tautomeric forms are present.

### **8.8.4 General Notices**

- The release cycle of OpenEye Toolkits has been changed. See the Release Cycle section for more information.
- This is the last release to support GCC 4.4 on RHEL6. For future toolkit releases, GCC 4.8 will be the oldest targeted compiler.
- This is the last release to support OS X 10.11. Full support for macOS 10.14 will be added in the next release.
- This release adds support for Ubuntu 18 and will be the last release to support Ubuntu 14.
- This release adds support for Python 3.7 on macOS and Linux. On Windows, Python 3.7 will be supported in the next release that will also drop support for Python 3.5.
- FastROCS TK no longer supports Nvidia Tesla, GeForce, and Quadro cards with a compute capability of less than 3.0. This includes all GPUs with Fermi architecture (e.g., Tesla C2050 and GeForce GTX 430). Users running one of these older GPUs who cannot upgrade their hardware should not update to this version of **FastROCS TK.**
- Spruce TK now requires a specific license. For information on Spruce TK licensing, please visit https://www. eyesopen.com/contact.
- Improvements have been made to the Python 3 toolkits with regard to wrapping optimization. This results in Python 3 performance being comparable to Python 2.

# 8.9 OEToolkits 2018.Feb

### 8.9.1 GraphSim TK: GPU-Accelerated Fast Fingerprint Similarity Searches

GraphSim TK now supports CUDA for even faster fingerprint searching, allowing users to perform molecular similarity calculations up to 200x faster than the in-memory fast fingerprint mode (see the NxN similarity score calculations graph below).

CUDA mode involves preloading all fingerprints into GPU memory prior to performing similarity calculations. Searches are limited by GPU memory availability and will fall back to the memory-mapped CPU mode if the entire set of fingerprints cannot be preloaded into the GPU memory. Despite this limitation, this represents the fastest way to perform similarity searches.

The most effective way to use CUDA fingerprint searches is to perform multiple searches with a pre-loaded database on a dedicated GPU machine. If CUDA mode is selected but a GPU is not present on the system, the search will simply fall back to memory-mapped mode.

The new OEFastFPDatabase.GetHistogram method performs an NxN search of a database and returns a histogram of scores. This is valuable information for understanding the diversity of a database without consuming excess disk space. Using OEFastFPDatabase. GetHistogram in CUDA mode will afford 2.5 billion searches per second (benchmarked on an AWS P3 instance - NVIDIA Tesla V100) compared with 12.5 million searches per second when using memory-mapped mode on the CPU.

![](_page_90_Figure_7.jpeg)

See the GraphSim TK Examples chapter of the **OEGraphSim TK** documentation for more information and examples using the new OEFastFPDatabase class.

### 8.9.2 Grapheme TK: Unpaired Interaction Map

Grapheme TK now includes the ability to generate unpaired interaction maps (see the example below). An unpaired interaction map provides a complementary view to the more common active site interaction depiction. While the interaction map (on the right) depicts interactions between the ligand and protein, the unpaired map (on the left) illustrates interactions that could contribute to binding but are not formed in the complex. Together, these two maps of the protein-ligand binding site provide insights into protein-ligand interactions and communicate complex 3D structural results in a directly actionable way.

In the unpaired interaction map, different linker types are used to mark unpaired acceptor and donor hydrogen bond interactions (see the figure on the left). Note that since these interactions are unpaired, the direction of the linkers has no real spatial meaning. Ligand linkers are directed away from the ligand, while protein linkers are directed towards the ligand.

The geometric parameters used to perceive unpaired interactions are customizable to fit user needs.

![](_page_91_Figure_5.jpeg)

Table 1: Unpaired interaction map (left) and active site depiction (right) generated after hydrogen placement (PDB: 1BR6)

### 8.9.3 Conda Packages for Python

The 2018. Feb release is the first release to fully support Conda packages for Python toolkits on all supported platforms. The toolkits are available as a package named openeye-toolkits in the openeye Conda channel on the default conda . anaconda . org server. Versions are available for Python 3.5 and higher on Windows and Python 3.4 and higher on Linux and macOS. On Linux and macOS, users can install the toolkits into a Conda Python environment with conda install -c openeye openeye-toolkits. On Windows, Anaconda Navigator is a convenient way to manage Conda packages.

See Python Installation for more information.

### **8.9.4 General Notices**

- All OpenEye Toolkit Python code examples now follow the PEP8 standard.
- The 2018. Feb release fully supports macOS High Sierra 10.13.
- mac OS 10.10 is no longer supported.

# 8.10 OEToolkits 2017.Oct

### 8.10.1 Shape TK: Version 2.0.0

The 2017. Oct release introduces **Shape TK** version 2.0.0, which is completely redesigned with a new API that is more flexible and easily extended with new functionality. Shape TK version 2.0.0 is now thread-safe and is able to:

- calculate color using grid- or proxy grid-based analytic methods
- calculate shape overlap and color score between two fixed-in-space objects with a single calculation using the OEOverlapFunc class
- combine force fields from the OEFF TK with shape and/or color for overlay optimization
- obtain top hits from a database against a given query using the OEROCS class
- create a query combining any combination of a molecule, a grid, and multiple shape and/or color Gaussians using the OEShapeQuery class (see example below)

Preliminary testing of functionality from **Shape TK** version 2.0.0 indicates that overlay optimization is up to 10% faster than the 2017.Jun version.

![](_page_92_Figure_14.jpeg)

Table 2: Shape query with shape grid and color Gaussians

### 8.10.2 Omega TK: New Torsion Library

A new torsion library has been added to **Omega TK** based on a probabilistic analysis of torsion angles in the Cambridge Structural Database (CSD) by Guba et al. [Guba-2016] This torsion library, which contains more than 500 entries, complements the existing torsion library, which is based mainly on analysis of structures found in the Protein Data Bank (PDB). Replacement of the existing library with the new library has four important effects on OMEGA's performance:

- nearly complete elimination of torsion values not well represented in the CSD
- significantly improved run time
- substantial reduction in the size of the conformer ensemble
- small trade-off increase in the median RMSD for solid state structures (both from the PDB and the CSD)

### 8.10.3 OEDepict TK and Grapheme TK: Interactive SVG Images

The 2017. Oct release expands these toolkits' ability to assemble sets of graphical objects in SVG images.

Images can present great deal of information very quickly, but those that try to convey too much information at once can look convoluted. The solution lies in generating interactive images that on the surface are simple but that can reveal extra information on request. This release allows users to mouse over simple images to view additional embedded information.

In the example below, the sequence-level depiction of a peptide is easily comprehensible due to its simplicity (see image below). The more detailed atomic-level representation of the amino acid components of the peptide can be revealed on mouse-over without cluttering the simplified view.

For more information, see the Generating Interactive SVG Images chapter of the OEDepict TK documentation.

### 8.10.4 General Notices

- On macOS Python, single-build distributions are now installed by default when using the meta-installer via pip install openeye-toolkits.
- . The Python verification tests now use pytest rather than nosetest as the test discovery tool. pytest options can be passed to the openeye.examples.openeye\_tests module to control the tests and level of debugging information provided.
- This is the last release to support Java 1.6.
- This is the last release to support Python 2.7.

# 8.11 OEToolkits 2017.Jun

### 8.11.1 Shape TK: Hermite

The 2017. Jun release introduces the OEHermite class, which allows a molecule to be expanded into a Hermite representation. An initial suggested area of application is the representation of protein shape. The advantages of representing proteins by Hermites include:

- smooth representations that capture any level of detail, from the atomistic (many coefficients, see the picture on the right) to the very coarse (few coefficients, as in the middle picture),
- the ability to store these representations in a compact manner,

- the ability to transform these representations easily, and
- very fast overlap calculations between proteins.

Below are examples of low- and high-resolution Hermite representation images of dihydrofolate reductase (DHFR):

![](_page_94_Figure_4.jpeg)

Fig. 17: Exact shape versus Hermite Representation

**OpenEye** will explore the potential of Hermite representations; we invite users to do likewise with this exciting new addition to the OpenEye toolkits. See the Shape from Hermite Representation chapter of the Shape TK documentation for more information.

### 8.11.2 OEDepict TK and Grapheme TK: Interactive SVG images

Scalable Vector Graphics (SVG) image format is dominant in web applications due to its wide browser support and scalability. An SVG image contains a list of graphical objects that can be grouped, styled, and transformed together. This enables the generation of interactive images defined in the SVG XML elements or via scripting that accesses the SVG Document Object Model (DOM).

The new Preliminary API available in **OEDepict TK** provides low-level functionality that enables grouping of graphical elements in SVG images that can be manipulated externally by web developers. High-level API entrypoints are also available to generate self-contained SVG images that show or hide different elements of the image based on mouse events.

For more information see the Generating Interactive SVG Images chapter of the **OEDepict TK** documentation.

### 8.11.3 GraphSim TK: Fast Fingerprint Similarity Search

**OEGraphSim TK** now provides improved fingerprint search capability, allowing users to perform molecule similarity searches on large databases up to 10x faster than previous versions.

Fingerprint methods are used for the computation of similarity scores. When searching large virtual databases, performance can be problematic. To address this issue, OEGraphSim TK now uses popcount, a hardware instruction available on modern CPUs, to provide significant performance improvements for computing similarity.

The new fingerprint search can be performed in two modes: in-memory and memory-mapped. The in-memory mode involves preloading all fingerprints into memory and performing the search. While this represents the fastest way to perform similarity searches once the fingerprints are loaded, searches are limited by memory availability. The memory-mapped mode has no load time penalty or memory limitation but the search itself takes more time.

![](_page_95_Figure_1.jpeg)

See the GraphSim TK Examples chapter of the OEGraphSim TK documentation for more information and examples using the new OEFastFPDatabase class.

### 8.11.4 General Notices

- On Linux, Python single-build distributions are now installed by default when using the meta-installer via pip install openeye-toolkits. If a problem is encountered with the single-build packages, users can set the environment variable OE\_PIP\_ARCH=old before the pip install step.
- Python 3.6 is supported in the 2017. Jun release.
- This is the last release to support 32-bit Java.
- This is the last release to support Red Hat Enterprise Linux version 5. As of March 31, 2017, RHEL5 has reached end-of-production support.

Note: OpenEye continues to monitor and collect feedback from our customers on the need to support Python 2 wrappers. Our current plan is to phase out support for Python 2 on all platforms by the 2017. Oct release. As this is a substantial change for our customers, we are willing to help with migration. Please contact support@eyesopen.com for more details.

# 8.12 OEToolkits 2017.Feb

### 8.12.1 Alternative Starting Points for Shape Overlap Optimization in FastROCS TK

This release of FastROCS TK extends its capability to find the best possible shape match between two conformers by introducing the ability to use custom starting points for the shape search. For some systems, using these alternative starting points can lead to more accurate shape scoring as it enables broader sampling of the molecular volume overlap.

By default, the shape search in **FastROCS TK** starts from 4 poses of the database molecule aligned around the inertial axes. With the UserInertialStarts option, FastROCS TK translates the database molecule to user-defined starting coordinates. With the InertialAtHeavyAtoms option, the database molecule is translated to each heavy atom of the query molecule. In both cases, the shape overlap is optimized for 4 unique inertial poses at each location. The images below illustrate a shape search between caffeine query and a naphthalene derivative.

![](_page_96_Figure_2.jpeg)

Table 3: Caffeine query and naphthalene derivative

The default shape search results in a poor overlap between the two molecules (left). When the new InertialAtHeavyAtoms option is used, the resulting overlap is much more favorable (right).

![](_page_96_Figure_5.jpeg)

Table 4: Best overlap: default vs. ``InertialAtHeavyAtoms`` start-

In general, these options provide the ability to fine-tune FastROCS TK searching based on specific criteria.

### 8.12.2 Charging Engine

A new charging function, OEAssignCharges, has been added. This function introduces the concept of a charge engine, a flexible, open-ended options class that defines a charging method. Charge engines have been written for every currently supported charging method as well as the new method OEAM1BCCELF10Charges.

### 8.12.3 New Maximum Common Substructure (MCS) Similarity Capability

A new class, OEMCSFragDatabase, has been added that allows pairwise MCS similarity scores to be computed for a query molecule against a set of indexed target structures. The indexing algorithm uses a fragmentation approach to reduce the computational requirements of traditional NxN structure comparisons for MCS scoring. Tanimoto and Tversky similarity scoring functions are provided, as well as the ability to implement custom scoring functions.

### 8.12.4 Protein Preparation Update

In the 2016. Oct release, new functionality for hydrogen placement was added as part of a protein preparation workflow. This new functionality has been significantly improved.

A new scoring system, MMFF-NIE ("MMFF Neighbor Interaction Energies"), has been added to OEPlaceHydrogens that significantly improves optimization of hydrogen bonding networks and clash avoidance.

In addition, significant improvements have been made in the placement of hydrogens around metal complexes. In the following example, cysteine sulfurs are now properly perceived as deprotonated in the zinc finger domain of the nucleocapsid protein NCp8 (PDB: 2A51).

![](_page_97_Figure_9.jpeg)

Table 5: 2016. Oct vs 2017. Feb cysteines in zinc finger domain

### 8.12.5 General Notices

- For Python, the new environment variable  $OE$  PIP ARCH can be set to override the Python package download. OE\_ARCH now only applies to application installation. This should mitigate conflicts between Python and application package installation.
- On Linux, Python single-build distributions are now installed by default when using the meta-installer via pip install openeye-toolkits. If a problem is encountered with the single-build packages, users can set the environment variable OE PIP ARCH=old before the pip install step.
- The Java wrappers are now built using Java 1.8 in 1.6 compatibility mode. Users should see no impact.
- The 2017. Feb release fully supports macOS Sierra 10.12.

- Python 3.4 on Windows is no longer supported.
- Python 3.6 will be supported in the 2017. Jun release.

Note: The default Python version installed under Anaconda/Miniconda is Python 3.6. Until the 2017. Jun release is available, users should override the default Python version with conda create python= $3.5...$  during the conda environment creation step.

Note: OpenEye continues to monitor and collect feedback from our customers on the need to support Python 2 wrappers. Our current plan is to phase out support for Python 2 on Windows by the 2017. Oct release and phase out support on other platforms at a later date. As this is a substantial change for our customers, we are willing to help with migration. Please contact support@eyesopen.com for more details.

# 8.13 OEToolkits 2016.Oct

With this release, OpenEye continues to focus on protein handling and visualization. In addition, numerous improvements to the toolkits have been made.

### 8.13.1 Protein Preparation

A new function, OEP laceHydrogens, has been introduced to the OpenEye protein preparation workflow in OEBio TK. This function positions hydrogens in a molecule to build hydrogen bonding networks and avoid clashes. It can also flip functional groups that are sometimes modeled incorrectly, such as histidine, asparagine, and glutamine sidechains. Previously, **OpenEye** recommended that users run the open source application Reduce to perform these functions. OEPlaceHydrogens is easier to use and has broader applicability because it uses SMARTS patterns rather than relying on naming conventions.

This release represents an initial implementation of this functionality; it is under continuing development. A new example program, Preparing a Protein, demonstrates this functionality.

For more information, see the Protein Preparation section.

![](_page_98_Figure_11.jpeg)

#### Table 6: Example of a hydrogen bonding network in 1R1H along with the corresponding protein-ligand visualization

### 8.13.2 Protein-Ligand Interaction

This release of OEBio TK includes significant improvements to the perception of potential protein-ligand interactions, intramolecular interactions, and missing potential interactions.

A new type of interaction, Halogen Bonds, has been added to OEBio TK. It joins Hydrogen Bonds, Salt Bridges, Chelation, and Pi- and T-aromatic Stacking in the set of perceived interaction types. These interactions provide qualitative hints about biological interactions that may be important for binding, and can be helpful for visualizing interactions and clashes.

An interface for modifying the geometric definitions for each interaction has also been introduced. While the default bond geometries have been carefully constructed using literature data (see below), users can now customize interaction parameters to fit their needs.

- 1. Kumar, S. and Nussinov, R., Biophysical Journal, 83:1595-1612, 2002.
- 2. Cavallo, G., Metrangolo, P., Milani, R., Pilati, T., Priimagi, A., Resnati, G., Terraneo, G., Chem. Rev. 2478-2601, 2016.
- 3. Bissantz, C., Kuhn, B., Stahl, M., J. Med. Chem., 53:5061-5084, 2010.
- 4. Marcou, G., Rognan, D., J. Chem. Inf. Model., 47:195-207, 2007.

### 8.13.3 FastROCS TK CUDA Implementation

The internal GPU implementation of **FastROCS** has been ported from OpenCL to CUDA. Although this does not change the results returned by **FastROCS** and should not impact the deployment of **FastROCS TK** on customer machines, it does allow OpenEye to better support NVIDIA hardware and facilitates our ability to improve performance and add GPU functionality.

### 8.13.4 General Notices

- The 2016. Oct release adds support for Ubuntu16 for C++, Java, Python 2.7, and Python 3.x.
- The 2016.Oct release is the last release to support OSX 10.9. The 2017.Feb release will add full support for macOS Sierra 10.12.

Note: OpenEye continues to monitor and collect feedback from our customers on the need to support Python 2 wrappers. Our current plan is to phase out support for Python 2 on Windows by the 2017. Oct release and phase out support on other platforms at a later date. As this is a substantial change for our customers, we are willing to help with migration. Please contact support@eyesopen.com for more details.

# 8.14 OEToolkits 2016.Jun

### 8.14.1 Single Build Distributions

**OpenEye** is pleased to announce the release of a Linux distribution built for maximum compatibility across multiple Linux versions. This will simplify the deployment of toolkits and toolkit programs across heterogeneous Linux environments. A toolkit executable built using the single-build distribution will run unmodified on most modern Linux systems, eliminating the need to build executables for each Linux release or compiler version. Currently, this single-build release is available for C++ and Python in parallel with our normal version-specific releases. In the future, we plan to make this build strategy available for all **OpenEye**-supported platforms.

For more information, see the Single-Build Distributions (Linux) section for C++ and the Common Linux Single-Build Installation section for Python.

### 8.14.2 Protein-Ligand Visualization

Grapheme TK provides representation schemes that allow clear and coherent visualization of complex chemical information. Its most important function is to project the intricate interactions of a protein-ligand complex into a 2D diagram visualizing key interactions and properties that chemists can use to make fast and effective judgments.

The receptor-ligand visualization introduced in 2015. Feb has been extended to visualize two new interaction types: salt-bridges and stacking interactions (Pi and T). Accordingly, the color scheme used to depict these interactions has been revamped.

**Grapheme TK** has also introduced the capability to select and highlight various parts of the protein-ligand 2D depiction.

![](_page_100_Figure_6.jpeg)

Table 7: Examples of new protein-ligand visualization in Grapheme

Note: As per customers' request, the OEFragmentNetwork class and its related API have been renamed and deprecated. The words "fragment," "network," and "connection" appearing in the names of classes and functions designed to store receptor-ligand interactions has been found to be confusing. The primary class is now called OEInteraction-HintContainer. For more details, see the Deprecated OEFragmentNetwork and related API section. The new API retains all previous functionalities and adds the capability to handle the new interaction types.

### 8.14.3 Tversky Similarity Scoring in FastROCS TK

FastROCS TK has supported only Tanimoto (symmetric) similarity scoring since its inception. This release adds Tversky similarity scoring to FastROCS TK. Using Tversky instead of Tanimoto scoring can lead to a higher retrieval of actives in searches, as indicated by our large-scale comparison experiment using the DUDE database (see the chart below).

Other significant improvements in **FastROCS TK** include the reduced memory consumption of OEShapeDatabase to support color scoring and support for the new  $361. \star$  driver. This new driver has a noticeable performance improvement (approximately 10%), so upgrading is recommended.

![](_page_101_Figure_1.jpeg)

Table 8: Retrieval rates using Tanimoto and Tversky similarity measures

#### **8.14.4 General Notices**

- This 2016.Jun release supports Python 3.5 on Windows with Visual Studio 2015. Python 3.3 on Windows is no longer supported.
- This 2016.Jun release supports Visual Studio 2015 for C++ and C# toolkits. Visual Studio 2010 and Visual Studio 2012 are no longer supported.
- This 2016. Jun release is the last to support Ubuntu 12 for all toolkits. The 2016. Oct release will add Ubuntu 16 support.
- This 2016. Jun release is the last to support 32-bit RedHat 5 for all toolkits.
- This 2016.Jun release is the last to support Python 2.6 on RedHat 6.

Note: OpenEye is planning to phase out Python 2 support by the October, 2017 release. As this is a substantial change for us and our customers, we are willing to help with code migration, either with advice or hands-on work with your code-base. Please contact support@eyesopen.com for more details.

# 8.15 OEToolkits 2016.Feb

### 8.15.1 OpenEye Toolkit Security

OpenEye toolkits are increasingly being used in web services that require protection from malicious users. The most obvious attack vector against the **OpenEye** toolkits is file format parsing since scientific file formats are complex and often underdefined.

**OpenEye** has closed a significant number of vulnerabilities related to the parsing of supported file formats: molecules, grids, surfaces, receptors, etc. In addition, state-of-the-art testing and detection techniques are now continuously run on the OpenEye code base to ensure a high level of security going forward.

Security is a task requiring continuous vigilance and **OpenEve** will continue to make this effort a high priority.

### 8.15.2 FastROCS TK: Database Loading Performance Improvement

The utility of **FastROCS** has always been hampered by the amount of physical memory available in GPU machines. The computational chemistry community is continuously pushing the boundaries of FastROCS by searching larger and larger virtual libraries of compounds. In addition, **FastROCS** servers are becoming an increasingly important component of many infrastructures and must be able to be rapidly brought up and down on demand. Both these problems come down to the fact that loading a database into memory is often between 10 and 20 times slower than performing an actual FastROCS search on that database.

This problem has been addressed in this release by dramatically increasing the performance when loading a dataset into memory for eventual FastROCS processing. OEPrepareFastROCSMol generates additional information to be written to OEB that is used to rapidly read molecules into memory.

Using OEP repareFast ROCSMo1 on a molecule can result in load times that are nearly 10 times faster than previous uncached OEB file loads. Depending on the ratio of CPU and GPU compute power and conformers per molecule, this can mean that loading a dataset can now be just as fast as the **FastROCS** search itself.

![](_page_102_Figure_10.jpeg)

### 8.15.3 OEMedChem TK

OpenEye is pleased to announce the first official release of OEMedChem TK. This medicinal chemistry functionality was previously only available in beta form.

**OEMedChem TK** provides the ability to index a set of input structures and identify matched molecular pairs. Matched molecular pair analysis is becoming recognized as a powerful tool for the extraction of the effects of chemical changes on a property or properties of interest in large data sets.

![](_page_103_Figure_4.jpeg)

Table 9: Fragmentation and Indexing Approach to Matched Molecular Pair Analyses

Additional OEMedChem TK capabilities include fragmentation and perception, similarity measures, belief theory, and molecular complexity measures. For the full list of capabilities, see the OEMedChem functionalities section.

**Note:** If you would like to utilize the functionalities of **OEMedChem TK**, please visit https://www.eyesopen.com/ contact for a license.

### 8.15.4 General Notices

- This 2016. Feb release is the last to support Ubuntu 12 for all toolkits.
- OSX 10.8 is no longer supported, but support has been added for OSX 10.11.
- This 2016. Feb release is the last to support Visual Studio 2012 for C++ and C# toolkits and Visual Studio 2010 for Python 3.3 toolkit.
- This 2016. Feb release supports Python 3.5 for the following platforms: OSX 10.10, OSX 10.11, Ubuntu 12, Ubuntu 14, RedHat 6, and RedHat 7.
- The 2016. Jun release is expected to support Python 3.5 on Windows with Visual Studio 2015.
- The 2016. Jun release will add C++ support for Visual Studio 2015.

The Python 2 distributions of **OpenEye Python Toolkits** can now handle both ascii and unicode Python strings for all APIs that accept string arguments. For example, the OESmilesToMol function can now parse the following SMILES strings without throwing a 'TypeError' exception:

```
smiles_str = "[N+] (=0) ([O-]) ([O-]) nitrát"
smiles_unicode = u''[N+] (=0) ([0-]) ([0-]) nitrát"
```

Previously, the unicode strings would work in Python 3, but not in Python 2, making it difficult to write code that was compatible with both major versions of Python at the same time. This major change should make porting to Python 3 much easier for **OpenEye** toolkit users.

# 8.16 OEToolkits 2015.Oct

### 8.16.1 FastROCS TK

OpenEye is pleased to announce that FastROCS is joining the pantheon of OpenEye toolkits as FastROCS TK. Shape technology continues to be at the center of OpenEye's scientific mission, and the unprecedented performance gains of FastROCS TK continues to enable new science to be explored throughout the molecular modeling community.

Note: FastROCS TK is only available in Python on 64-bit Linux platforms.

![](_page_104_Figure_6.jpeg)

Warning: If your FastROCS license was created before May 19th, 2015, please visit https://www.eyesopen.com/ contact for a new license. FastROCS TK requires that the relevant "python" feature be turned on for access to **FastROCS TK.** 

### 8.16.2 OEChem: Molecule Reading Performance Improvement

In addition to extending the capability of **OpenEye's** toolkits, improving the performance of their existing functionalities is also important to us. We continually work to increase the performance of the molecule readers in OEChem TK to accommodate our field's ever-growing molecule databases. Significant effort has been made to accelerate reading molecules into OEMol. The graph below illustrates the overall results of the code optimizations performed since the previous release (2015.Jun).

![](_page_105_Figure_3.jpeg)

Table 11: Performance improvement in C++. See OEChem TK's detailed release notes for the other languages.

#### Note:

- OEB-OEMol OpenEye OEBinary file format stores molecules as OEMol (multi-conformer molecule representation)
- OEB-OEGraphMol OpenEye OEBinary file format stores molecules as OEGraphMol (single-conformer molecule representation)

### 8.16.3 OEBio: Fragment Network

The 2015. Feb release introduced the visualization of receptor-ligand interactions by Grapheme TK. The following  $2015$ .Jun release provided automatic identification of ligands by **OEBio TK**. This release extends these capabilities by providing read-only access to the fragment network data structure that can store interactions perceived by OEDocking TK. Several classes and predicates that provide convenient ways to examine various interactions types between a ligand and a protein have been also introduced.

![](_page_106_Figure_1.jpeg)

For more details about using these new APIs, see the example in the Perceive and Print Protein-Ligand Interactions section.

### 8.16.4 General Notices

• OpenEye Python Toolkits' installation command has been changed to:

```
$ pip install -i https://pypi.anaconda.org/OpenEye/simple OpenEye-toolkits
\ddots$ oecheminfo.py
Installed OEChem version: |oechemversion| platform: ubuntu-14.04-g++4.8-x64
\rightarrowbuilt: |builddate|
\cdots
```

- This is the last release to support FastROCS TK on Ubuntu 12.
- The 2016.Feb release will be the last release to support Ubuntu 12 for all toolkits.
- The 2015.Oct release is the last to support OSX 10.8.

# 8.17 OEToolkits 2015.Jun

### 8.17.1 PDB Splitting

**OEBio TK** includes a powerful new API for automatically classifying and separating the various components of a macromolecular complex by their functional roles. This new API makes it easy to excise a ligand or protein/cofactor complex automatically or identify binding-site residues. The process is also fully customizable to allow internal definitions of the ligand to augment the splitting algorithm. For more information, please see the Splitting Macromolecular Complexes documentation.

![](_page_107_Figure_4.jpeg)

Fig. 18: The above Sulfasalazine ligand was automatically identified in the glutathione S-transferase binding site by using the OESplitMolComplex function. The image was created by running the complex2img Grapheme TK example on the 13GS PDB entry. Previous versions required an external definition of the ligand; this new version bypasses that requirement for ease of use.

### 8.17.2 PAINS Filter

Pan Assay Interference Compounds (PAINS) filter was added to **OEMolProp TK** by adapting the supplementary material from the original [Baell-2010] paper. The PAINS filter can be used as a prefilter set for screening or, more interestingly, as a post-processing filter to identify possible protein-reactive or other assay-confounding functionalities within hits. Any hits so identified will require more care to determine if the measured activity is valid. The PAINS filters can give valuable insights into lead optimization priorities.

![](_page_108_Figure_1.jpeg)

### 8.17.3 Matched Molecular Pair Improvements

There is a wealth of information stored in a chemical series. Extracting this property change information from chemical analogs is at the heart of a matched molecular pair analysis. One challenge is capturing molecular differences corresponding to substitution of a hydrogen with a larger group in an unsupervised analysis approach. This new indexing capability generates significantly more matched molecular pairs during the analysis and yields additional information about substituent effects on molecular properties. More matched pairs means more information is being extracted from the chemical series.

This next beta release of OEMedChem TK improves the matched molecular pair analysis engine to robustly and efficiently support the identification of molecular pairs due to differences in hydrogen-atom substitutions:

![](_page_108_Figure_5.jpeg)

Additionally, indexing improvements also identify new linker insertions and modifications:

![](_page_108_Figure_7.jpeg)

#### 8.17.4 Custom Ring Template Dictionaries

Depiction of complex molecules in 2D is both a science and an art. For this reason, OEChem TK can now utilize custom ring template dictionaries specified by the user. This allows OpenEye Toolkits to adapt immediately to changing project demands. OpenEye will gladly continue to incorporate ring templates submitted to us, but this new feature will be more flexible. The Custom Ring Template Dictionary Guide explains the tools and process to start using custom internal dictionaries.

![](_page_109_Figure_3.jpeg)

#### 8.17.5 Anaconda Support

We want to work where you do. At **OpenEye**, we support all major platforms and Continuum's Anaconda is becoming a major platform for scientific Python. Anaconda is a Python distribution that installs commonly used scientific packages by default. OpenEye Python Toolkits have added binary support for Anaconda.

Note: Using the PIP installation mechanism described below greatly simplifies this compatibility; the user should not even notice that Anaconda Python requires a different binary.

#### 8.17.6 One-Command Python Installation

**OpenEye Python Toolkits** can now be installed with one command:

```
$ pip install -i https://pypi.binstar.org/OpenEye/simple OpenEye-toolkits
\mathbf{1}$ oecheminfo.py
Installed OEChem version: |oechemversion| platform: ubuntu-14.04-g++4.8-x64 built:
\rightarrow | builddate |
```

See the Quick Start guide to learn how to make this command even shorter:

pip install OpenEye-toolkits

The command above will automatically select the correct version and operating system in a way that is natural for any pure Python project.

- The Python toolkit package name has been changed from OpenEye to OpenEye-toolkits. This will change how the previous toolkit is uninstalled from a virtualenv.
- · examples, docexamples, and tests are now found under the openeye module in the OpenEye-toolkits package. This allows examples and integration testing to be performed easily after installing the OpenEye-toolkits package like a proper Python package. Run the following command to execute the integration tests:

(OpenEye) \$ python -m openeye.examples.openeye\_tests

In addition to OpenEye examples being placed in the Python bin or Scripts directory, examples can also be run through the Python interpreter's -m option:

(OpenEye)\$ python -m openeye.examples.oechem.oecheminfo

• py2exe should now work. OpenEye Python Toolkits will no longer use modules that are blacklisted by py2exe.

### 8.17.7 General Notices

- This is the last release to support Visual Studio 2010 for C++.
- This is the last release to support CMake 2.x in the C++ distributions; all future releases will use CMake 3.1+. The CMake files shipped with the C++ toolkits have been made compatible in both CMake 2.x and CMake 3.1+, but compatibility with CMake 2.x will not be tested after this release.

### 8.18 OEToolkits 2015.Feb

This release of the **OpenEve Toolkits** contains many new features and bug fixes. The most important are highlighted here.

#### 8.18.1 Protein-ligand Rendering

**Grapheme TK** now includes a powerful new API for the display of 3D information. The interactions between a protein and a ligand provide crucial information to the pursuit of new drugs. To facilitate the deciphering of these complex interactions, **OpenEye** is releasing the ability to render this 3D information in a 2D diagram. Currently, only OEDocking TK interactions can be rendered by Grapheme TK. However, this feature will be fully extensible through the OEBio TK. If you wish to display a particular type of interaction and would like to contribute to the development, please contact support@eyesopen.com.

![](_page_111_Figure_1.jpeg)

### **8.18.2 Documentation Refresh**

To improve usability and maintain a high level of quality, the OpenEye Toolkit documentation has been refreshed over the last year. In addition to a new logo and style, significant functionality has been added. All OpenEye Toolkits will now cross-reference, leading users to the correct toolkit while searching for functionality. In addition, searching the HTML documentation can now be performed with Google, offering significantly better search results than the previous HTML documentation. If you are an avid user of the PDF documentation, we strongly encourage you to take another look at the HTML documentation.

![](_page_111_Picture_4.jpeg)

### 8.18.3 Matched Pairs Transformations

This release continues the incorporation of community suggestions in the OEMedChem TK. In this release, the matched molecular pairs functionality has been augmented to include easy access to the transformations themselves in native form, allowing for retrieval and manipulation of transformations for many more matched pair use cases.

![](_page_112_Figure_3.jpeg)

### 8.18.4 Optimized Depiction Orientation

Molecular depictions are a common element in any chemistry environment. However, they can waste a lot of screen real estate, especially when displaying extended or oddly shaped molecules. To maximize screen space, the OEDepict **TK** now provides the ability to optimize for either horizontal or vertical rendering of the molecule coordinates. For example: to display molecules in a spreadsheet, horizontal depictions will conserve the most vertical whitespace; to display molecules in the sidebar of a webpage, vertical rendering will conserve the most horizontal whitespace.

![](_page_112_Figure_6.jpeg)

### 8.18.5 General Notices

- SuSe 11 is no longer supported.
- Visual Studio 2008 for C++ and C# toolkits is no longer supported.
- The 2015. Jun release will be the last to support Visual Studio 2010 for C++.
- OSX 10.10 Yosemite support has been added.
- Babel is a command line tool for molecular file format translation, incorporating a wide range of OEChem options. The application code is now open source and can be found here: https://github.com/oess/OEBabel
- OpenEve Python toolkits are now built with SWIG 3.0.2. Users who write and compile their own OpenEve C++ toolkit extensions will need to upgrade accordingly. An example of compiling a custom extension to the Python toolkits is given here: https://github.com/oess/oepython\_extension.

# 8.19 OEToolkits 2014.Oct

This release of the OpenEye toolkits contains many new features and bug fixes. The most important have been highlighted here, the full list can be accessed below.

### 8.19.1 Pictorial application for automatically writing OEDepict code

**OEDepict TK** is a powerful API for the "2D" depiction of small molecules. While such depictions are universal in chemistry there are many variants in drawing style, the majority of which are captured in OEDepict's extensive set of options. To aid navigation through the many options available we now provide a small application, Pictorial, written in Java, that will autogenerate code that can then be used in your own programming. The figure below is an illustration of the interface.

![](_page_114_Figure_1.jpeg)

### 8.19.2 Major improvements to Quacpac's protomer assignment algorithms

**Quacpac TK** is a set of tools for the assignment of charges, ionization states and proton positions. The latter has been significantly improved to produce more reasonable tautomeric forms, for instance by disfavoring exocyclic bonds adjacent to aromatic bonds (e.g. favoring aromatic forms). An example is depicted below.

![](_page_115_Figure_1.jpeg)

### 8.19.3 Major improvements to depiction of complex ring systems

**Depiction** of complex molecules in 2D is both a science and an art. Algorithms help with the majority of cases but sometimes they have to be supplemented with the 'art' of hand-drawn templates. In our continuing quest to provide the best 2D depiction of molecules, this release includes an additional 550 such templates to OEDepict and 2D coordinate generation in OEChem. Some examples are shown below.

![](_page_115_Figure_4.jpeg)

### 8.19.4 Multi-precision conformer handling

There are times where **precision** is important and times when, due to memory consumption, it gets in the way of computation. As such, this release of the toolkits includes two new levels of precision. In OEChem the basic molecular object OEMol can now store conformer coordinates as 16-bit 'half-floats', 64-bit double precision number or long doubles (typically 80 bits although storage requirements may vary). Half-floats have five bits reserved for the exponent, eleven for the fraction. Examples of where it might be useful include shape representation (robust to small coordinate changes) or compact storage. Extra-precision is useful when interfacing with quantum programs or for storage in rotor-offset form in OEB files.

Warning: C++ users may notice that OEChem::OEMCMolBaseT and OEChem::OEConfBaseT have been renamed to OEMCMolBase and OEConfBase respectively. This change was to enable the above feature and to ease the use of the documentation by Python, Java, and C# users who should see no effect from this change.

### 8.19.5 New force field in Szybki

Szybki TK encompasses our capabilities for molecular optimization. This version of the toolkit includes our latest advances in the calculation of intermolecular interactions, i.e. the combination of dispersion (attractive), Fermi overlap (repulsion) and Coulombic interactions (either). These are captured in the IEFF formulation, which represents the first two interaction terms in more detail than typical VdW forms. In addition, Coulombic interactions are calculated using atom-centered point multipoles, as output by quantum chemistry codes. OpenEye provides facilities to input these into OEB files for proteins and ligands, allowing a new level of sophistication in the evaluation of complex interactions. In addition, the Szybki toolkit also includes a new function call to allow for specifically constraining a single torsion and new methods to assign flexibility to residues during protein-ligand optimization.

### 8.19.6 Matched Pairs analysis beta API added to OEMedChem TK

This release includes an exciting beta of **OEMedChem** which includes containing facilities for "Matched Pair" analysis. The matched pair concept has resonated in the medicinal chemistry community because it provides a simple method of comparing two molecules, i.e. ascertaining whether they differ in chemically obvious ways, e.g. a swap of a fluorine for a chlorine or a benzamide for a benzamidine, and then using historical data on such transformations to make predictions on property differences. The functions within the OEMedChem toolkit in this release are capable of searching datasets for such pairings, allowing for such prior expectations to be tabulated. We stress this is a beta release feature and look forward to incorporating community suggestions and requests.

![](_page_116_Picture_5.jpeg)

### 8.19.7 Major bug fixes

Warning: It is strongly recommended for users of the 2014.Feb and 2014.Jun releases to upgrade to the 2014.Oct release because of the following major bug fixes for the SDF, MDL, and CDX file formats.

The addition of 2D coordinate generation for the SDF, MDL, and CDX file formats in the 2014. Feb release, **OEChem 2.0.0**, created the possibility of erroneously changing stereo chemistry in the following cases:

- 1. Bond stereo chemistry in macrocycles
- 2. Atom stereo from wedges or hashes between atoms with an angle less than 180 degrees

The 2D coordinate generation can not always generate coordinates that represent the required stereo chemistry. For these cases, OEChem will now leave the coordinates in the resulting file all zero. This will make file readers choose to honor the stereo marks instead of the 2D coordinates.

![](_page_117_Figure_1.jpeg)

### 8.19.8 General notices

- The following is no longer supported on RedHat Enterprise Linux 5:
  - $-$  Python 2.6
  - $-$  gcc 4.3
  - $-$  gcc 4.4
- Ubuntu 10.04 is no longer supported.
- This will be the last release to support SuSe 11.
- OSX 10.7 is no longer supported.
- This will be the last release to support Visual Studio 2008 for C++ and C# toolkits.

Several notable improvements have been made to the Python distributions:

• OpenEye Toolkit APIs will be more strict about coercing parameters into boolean arguments. When objects are passed as a parameter to a Python function call where a Boolean is expected, the language 'coerces' the parameter to "True". For instance, consider the following code:

```
mol = OEGraphMol()opts = OEPrepareDepictionOptions()
opts. SetSuppressHydrogens (False)
clearCords = TrueOEPrepareDepiction(mol, clearCoords, opts)
```

Here the result is a depiction that does not have hydrogens, even though we set the "SuppressHydrogens" flag to false. This happens because the last flag in the function call is an object, not the expected Boolean and so Python sets it to "True". This release has improvements in how this is handled and will throw an exception about the type mismatch.

- OpenEye Python toolkits are now built with SWIG 3.0.2. Users who write and compile their own extensions will need to upgrade accordingly.
- Incorrect OE\_ARCH environment variables will no longer cause importing the OpenEye libraries to fail. Instead, the malformed architectures in the list will be ignored and normal architecture lookup will continue.

# 8.20 OEToolkits 2014.Jun

This release of the OpenEye toolkits is focused on stability and new platform support. The last release, 2014.Feb, was a major feature release introducing numerous new features. This release focused on fixing many bugs and improving the overall stability of the OpenEye toolkits.

There is still a major new feature being added in this release:

• FreeForm API added to Szybki TK

Several notable **improvements** have been made to the **Python** distributions:

- Support for Python 3.3 officially added. Python 3.3+ has been thoroughly tested since the previous release. Python 3.4 also works and is binary compatible with Python 3.3, as such, OpenEye Python 3.x distributions will just be labeled "python3", except for Windows.
- All python examples should be compatible with both Python 2 and Python 3.
- An ImportError exception with a more straight forward error message will be printed if there is a mismatch between the Python interpreter version and what Python interpreter version the OpenEye Toolkits are built against.
- Fixed a bug in OpenEye's platform detection that would sometimes not recognize CentOS 6 as a RedHat 6 Linux distribution.

#### **General notices:**

- Windows XP is no longer a supported version of Microsoft Windows.
- Added support for Ubuntu 14.04, a long term support distribution that OpenEye will support for 4 years.
- This release will be the last release to support Ubuntu 10.04.
- Added support for RHEL 7. This is the next major release from RedHat that will be supported by OpenEye for at least 5 years. OpenEye will be very rapidly phasing out support for RHEL 5. RHEL 5 users should be planning their upgrade now.

To start the phase out, this will be the last release to support the following on RHEL 5:

- $-$  Python 2.6
- $-$  gcc 4.3
- $-$  gcc 4.4
- This release will be the last release to support OSX 10.7.
- The next release, 2014. Oct, will be the last release to support **Visual Studio 2008** for C++ and C# toolkits.
- Deprecated APIs will now throw a warning message once, and only once, for the lifetime of the process.
- Documentation examples for Java and Python distributions should now have documentation markup removed.

# 8.21 OEToolkits 2014.Feb

This release marks a major milestone for **OEChem**: 10 years as an OpenEye product! In recognition of that, we are releasing OEChem 2.0 to clean up some rough edges and bring in some important new features. We are committed to maintaining a stable OEChem API and thus the vast majority of programs written with previous versions of OEChem should continue to be supported in the **OEChem** 2.x series. The only "backwards breaking" functional change that everyone will see is something that we feel all users will appreciate:

#### Warning: '.smi' will now output molecules with stereochemistry.

A few of the new major features in **OEChem** are:

- OEGenerate2DCoordinates added for 2D coordinate generation and is automatically called when writing . sdf, . mdl, and . cdx files when the associated molecule had no coordinates.
- Support for . csv, comma-separated values, added as a supported molecule file format.
- Fast random access to all **OEChem** file formats through the new OEMolDatabase class.
- OEAddLicenseFromHttp added to Python, Java, and .NET toolkits to enable fetching license information from a server instead of the standard text file. This is not currently supported in C++.

This release also features the addition of **two new toolkits** to the distribution:

- Szmap TK this provides access to the core functionality used by the SZMAP application and enables the calculation of solvent energies and probabilities at arbitrary points in space. It also provides access to probe geometry for output and display.
- **OEMedChem TK** this is still in the experimental stages and is not yet officially supported; however, it provides many useful and interesting tools that we wanted to make available while we finalize the API and functionality set. As such, the existing API may (and most likely will) change in a future toolkit release.

An important fix to Python on Windows was added to this release:

• The OpenEye Python toolkits will no longer break interactive Python interpreters on Windows. Previously, importing the OpenEye Python toolkits would cause any subsequent commands typed into the interpreter to return a very confusing SyntaxError.

#### **General notices:**

- Added support for **OSX 10.9** Mavericks.
- The next toolkit release, 2014. Jun, will be the last release to support OSX 10.7.
- This release will be the last release to support OSX 10.6.
- The next toolkit release, 2014. Jun, will be the last release to support 64-bit Ubuntu 10.04.
- GCC 4.8.2 support added for RHEL6. GCC 4.8.1 had a bug that made it impossible to compile OpenEye header files. Please use 4.8.2+.
- Experimental support for Python 3.3 added.

### 8.22 OEToolkits 2013.Oct

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.9.3 **OEBrood TK 0.9.0 OEDepict TK** 2.2.1 **OEDocking TK** 1.2.1 Grapheme TK 1.1.0 **GraphSim TK** 2.0.6 **Grid TK** 1.4.4 Lexichem TK 2.3.0 MolProp TK 2.1.7 Omega TK 2.5.3 Quacpac TK 1.6.4 **Shape TK** 1.9.2 Spicoli TK 1.2.2 Szybki TK 1.7.5 Zap TK 2.1.6

Warning: The structure of the OpenEye Python Toolkit tarball is radically different for Linux and OSX. The OpenEye Python Toolkit tarball now conforms to Python standards for packaging. Please see the revised Python Quick Start manual for installation instructions.

- This is the last release to support Python 2.4 and 2.5. Please upgrade to 2.6 or 2.7.
- This is the last release to support Python 2.6 on Windows, 64-bit Windows Python 2.7 support is being added in this release.
- The Python toolkits will now work on OSX 10.8 when the Python interpreter was compiled with GCC instead of Clang.
- Performance improved by about 30% for the initial import of the Python toolkits on Linux and OSX. The python toolkits no longer rely on a shell script on these platforms to determine their architecture.
- The underlying version of SWIG has been upgraded to 2.0.10. This should only affect users who write custom extensions to the OpenEye Python toolkits in C++ and wrap them using SWIG. No other users should be affected by this change.
- No OpenEye toolkit will call OEErrorHandler. Fatal anymore. All instances have been replaced with OEErrorHandler. Error allowing end-users the ability to control whether programs should exit on error with OEErrorHandler. SetStrict. It is recommended to use OEThrow. SetStrict (false) inside long running services like web servers.

### 8.23 OEToolkits 2013.Jun

This is a new release of the OpenEye Toolkits with versions of the following libraries:

OEChem TK 1.9.2 **OEDepict TK** 2.2.0 **OEDocking TK** 1.2.0 Grapheme TK 1.0.6 GraphSim TK 2.0.5 **Grid TK** 1.4.3 Lexichem TK 2.2.3 MolProp TK 2.1.6 Omega TK 2.5.2 Quacpac TK 1.6.2 **Shape TK** 1.9.1 Spicoli TK 1.2.1 Szybki TK 1.7.4 Zap TK 2.1.6

- Most toolkit distributions do not ship with documentation anymore due to the sheer size of the documentation. Only the Python and C# Windows installers will continue to contain documentation. Documentation is still available as a separate download. Most users appear to rely on the OpenEye online documentation, that will continue to be maintained.
- The next release, 2013.Oct, will be the last release to support Python 2.4 and 2.5.
- A setup py has been included to allow developers to create pip compatible packages. See the Python Quick Start for more information.
- This release will be the last release to support SuSe 10.

### 8.24 OEToolkits 2013.Feb

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.9.1 **OEDepict TK 2.1.0 OEDocking TK** 1.1.4 Grapheme TK 1.0.5 GraphSim TK 2.0.4 **Grid TK** 1.4.2 Lexichem TK 2.2.2 MolProp TK 2.1.5 Omega TK 2.5.1

Quacpac TK 1.6.1 Shape TK 1.9.0 Spicoli TK 1.2.0 Szybki TK 1.7.3 Zap TK 2.1.5

- OSX 10.8 support added for C++, Python, and Java. Note, C++ and Python are built with the Clang 4 compiler.
- Visual Studio 2012 support added for C++ and C#.
- OSX 10.6 32-bit python is no longer supported.
- The next release, 2013. Jun, will be the last release to support SuSe 10.
- The documentation examples were accidentally left out of the last release on Windows. They can now be found in C: \Python27\OpenEye-2013. Feb. 1\docexamples.
- Importing the python toolkits when there are spaces in the directory structure should now work properly.
- Added the toolkit package version to the openeye module, e.g., openeye. version == "2013. Feb. x" for this release.

### 8.25 OEToolkits 2012.Oct

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.9.0 **OEDepict TK 2.0.4 OEDocking TK** 1.1.3 Grapheme TK 1.0.4 **GraphSim TK** 2.0.3 **Grid TK** 1.4.1 Lexichem TK 2.2.0 MolProp TK 2.1.4 Omega TK 2.5.0 Quacpac TK 1.6.0 Shape TK 1.8.3 Spicoli TK 1.1.3 Szybki TK 1.7.2 Zap TK 2.1.4

- Windows Python examples and documentation are installed into a subdirectory of  $C : \Python2* \setminus$  named after the version, e.g.,  $C:\Python27\OpenEye-2012.Oct.1$ . The installer will place links in the Windows start menu pointing to the new proper location.
- \*GetSite and \*GetLicensee free functions exposed by each toolkit now directly return a string to be more usable in all wrapped languages.

### 8.26 OEToolkits 2012.Jun

This is a new release of the OpenEye Toolkits with versions of the following libraries:

OEChem TK 1.8.0

**OEDepict TK 2.0.3** 

- **OEDocking TK** 1.1.2
- Grapheme TK 1.0.3
- GraphSim TK 2.0.2
- **Grid TK** 1.4.0
- Lexichem TK 2.1.2
- MolProp TK 2.1.3
- Omega TK 2.4.6

Quacpac TK 1.5.2

Shape TK 1.8.2

Spicoli TK 1.1.2

Szybki TK 1.7.1

Zap TK 2.1.3

- This release brings about the following changes in platform support:
  - Added support for 64-bit Ubuntu 12.04 LTS. A reminder that 32-bit will not be supported on future linux distributions.
  - Last release to support Visual Studio 2003. Please upgrade to Visual Studio 2008 or 2010.
  - Last release to support Python 2.5 on Windows. Please upgrade to Python 2.6 or 2.7.
  - Last release to support OSX 10.5. Please upgrade to OSX 10.6 or 10.7.

Warning: OEChem has undergone a major revision change from 1.7.7 to 1.8.0 to indicate that bugs were fixed in isomeric canonical smiles generation that could potentially change the smiles generated. A benchmark over 24.0 million unique compounds only yielded changes in 42 of the compound's isomeric canonical smiles. These 42 compounds fall into the following classes:

- broken porphyrins
- cross linked organometallics
- cross linked high molecular weight macrocycles
- trivalent and tetravalent oxygens
- polycyclic hydrazine dyes

See the OEChem release notes for a more specific description of these minor algorithmic changes.

# 8.27 OEToolkits 2012.Feb

This is a new release of the OpenEye Toolkits with versions of the following libraries:

OEChem TK 1.7.7 **OEDepict TK 2.0.2 OEDocking TK** 1.1.1 Grapheme TK 1.0.2 GraphSim TK 2.0.1 **Grid TK** 1.3.5 Lexichem TK 2.1.1 MolProp TK 2.1.2 Omega TK 2.4.5 Quacpac TK 1.5.0 **Shape TK** 1.8.1 Spicoli TK 1.1.1 Szybki TK 1.7.0 Zap TK 2.1.2

All the toolkits now use an extension of the MMFF94 force field for tricoordinate boron compounds. Please refer to the Omega TK and Szybki TK release notes for a more complete description of what types of boron are supported.

# 8.28 OEToolkits 2011.Oct

This is a new release of the OpenEye Toolkits with versions of the following libraries:

OEChem TK 1.7.6 **OEDepict TK 2.0.1 OEDocking TK** 1.1.0 Grapheme TK 1.0.1 **GraphSim TK 2.0.0 Grid TK** 1.3.5 Lexichem TK 2.1.0 MolProp TK 2.1.2 Omega TK 2.4.4 Quacpac TK 1.5.0 **Shape TK** 1.8.1 Spicoli TK 1.1.1 Szybki TK 1.6.0 **Zap TK** 2.1.2

This release is meant to be a minimal bug fix release to address a few key issues in the 2011.1 release.

- The 2011.1 release left internal debugging code turned on during all builds. The result was spurious application failures for corner case conditions. In general, the 2011.Oct version should run faster due to this being turned off.
- The package wide version number has been tweaked due to customer feedback to include an explicit month as the 2nd field to avoid confusion with the version number looking like a date. The version number will now be structured as the following:

[year].[month].[build]

year is the year the package was released

month is the month the package was released

**build** is an arbitrary number used for internally tracking the exact state of the package

# 8.29 OEToolkits 2011.1

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.7.5 **OEDepict TK 2.0.0 OEDocking TK** 1.1.0 Grapheme TK 1.0.0 GraphSim TK 2.0.0 **Grid TK 1.3.5** Lexichem TK  $2.1.0$ MolProp TK 2.1.2 Omega TK 2.4.4 Quacpac TK 1.5.0 Shape TK 1.8.1 Spicoli TK 1.1.1 Szybki TK 1.6.0 Zap TK 2.1.2

- C# support added across all the toolkits. See the C# Quick Start guide to get started using this new language binding.
- Renaming Ogham TK to OEDepict TK. OEDepict TK 2.0 is a major redesign of this core rendering library to enable new technology advances in 2D molecular communication.

Warning: The Ogham TK 1.x API is deprecated. The API is still available in OEDepict TK 2.0, but will be removed in a future release.

- Introducing a major new library, Grapheme TK, based upon OEDepict TK 2.0.
- Changing OEToolkits package version to no longer track the version of OEChem inside the package. The version number will now be structured as the following:

[year].[release].[build]

year is the year the package was released

release is a sequentially increasing number marking the release within the year

build is an arbitrary number used for internally tracking the exact state of the package

- Changed the default visibility of symbols in *OpenEye* libraries to be hidden. This can drastically lower the number of symbols exported from a given library improving compile times and shared library load time.
- When building with Microsoft Visual Studio, the OpenEye header files will enforce that you are building with the correct version of the compiler.
- The Python toolkits now allow for the OE\_ARCH environment variable to contain multiple colon separated options.

# 8.30 OEToolkits 1.7.4

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.7.4 GraphSim TK 1.0.0 **Grid TK** 1.3.4 Lexichem TK 2.0.2 MolProp TK 2.1.1 Ogham TK  $1.7.1$ Omega TK 2.4.1 Quacpac TK 1.4.1 Shape TK 1.8.0 Spicoli TK 1.1.0 Szybki TK 1.5.0 Zap TK 2.1.1 Docking TK 1.0.0

- This release of the OpenEye toolkit suite introduces a major new library, the :Docking TK:.
- The license error handling has been significantly improved to provide more descriptive error messages for why exactly a given license has failed. So instead of seeing "General failure to decrypt" as the license failure reason it will actually report "expired" or "version number" if that is the reason.
- The OE\*IsLicensed functions provided in each library will now report when the license expired if it is already expired instead of just erroring out.

Note: The above two changes do not affect licenses at all. Old and new licenses should continue to work exactly the same.

The following release notes are only for the python toolkit:

- OEBase. AddData, and thus any class that inherits from OEBase like molecules, now works properly on complex data types, such as molecules, grids, and surfaces. Before this release, OEBase.AddData was implemented in python for complex data types using OEBase. Set Data, so any previous data set was blown away. This release fixes OEBase. AddData for complex types to have proper AddData semantics.
- MiniMols and DBMols can now be attached as generic data.
- The Spicoli python module can now be queried for its license status without the need for a valid Spicoli license.
- The error message has been greatly improved when the OpenEye python libraries load to detect a mismatch between the platform being run on and what is actually installed. The intention is to make trouble shooting this common problem easier.
- Added the ability to run a 32-bit python with a 32-bit OpenEye python installation on a 64-bit machine. Some third party libraries have not been ported to 64-bit yet so this should ease the use of OpenEye libraries with these tools. Note, the python interpreter is directly queried for the machine architecture, not the operating system itself, i.e., the uname command.

Note: OSX 10.6 uses the VERSIONER\_PYTHON\_PREFER\_32\_BIT environment variable to specify what version of python to use, so the OpenEye libraries obey this environment variable as well.

• The OpenEye libraries used to insert integer keys into python's main dictionary. This caused problems with downstream tools like PyDoc that would expect keys to only be strings. This has been fixed so that those entry are now strings.

# 8.31 OEToolkits 1.7.2

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.7.2 GraphSim TK 1.0.0 **Grid TK** 1.3.3 Lexichem TK 2.0.0 MolProp TK 2.1.0 Ogham TK 1.7.1 **Omega TK**  $2.4.0$ Quacpac TK 1.4.1 Shape TK 1.7.2 Spicoli TK 1.1.0 Szybki TK 1.4.0 Zap TK  $2.1.1$ • There are two major additions to the OpenEye toolkit suite with this release:

#### **GraphSim TK**

A toolkit for doing 2D molecule similarity. The methods currently implemented are:

- Path based fingerprints
- MACCS key fingerprints

#### - LINGOS

#### **MolProp TK**

A toolkit derived from OpenEye's FILTER technology. This toolkit is useful for calculating an extensive list 2D molecular properties and building custom filters around these properties.

**Note:** The version number of *MolProp TK* will track with the FILTER application to indicate similarities.

- This release of OEChem introduces many bug fixes and new features provided they didn't break source-level compatibility with 1.7.0.
- This release completes the transition from the old LaTeX based documentation system to the new reStructured-Text based system. This includes better support for Python and Java in the manuals as separate manuals for every library.

The following release notes are only for the python toolkit:

- The OE\_ARCH environment variable has been introduced to force the python libraries to load shared libraries for a specific architecture. This can be useful for getting OpenEye libraries to work on non-officially-supported platforms.
- Quacpac: Added support for writing a custom OETautomerMolFunction or OETyperMolFunction in Python by deriving from the base class.

# 8.32 OEToolkits 1.7.1

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.7.1 **GraphSim TK** 1.0.0 **Grid TK** 1.3.3 Lexichem TK  $2.1.0$ **MolProp TK Ogham TK** Omega TK 1.4.0 Quacpac TK 1.4.1 Shape TK 1.4.0 Spicoli TK 1.1.0 Szybki TK Zap TK 2.1.1 • There are two major additions to the OpenEye toolkit suite with this release:

**GraphSim TK** 

A toolkit for doing 2D molecule similarity. The methods currently implemented are:

- Path based fingerprints
- MACCS key fingerprints

- LINGOS

#### **MolProp TK**

A toolkit derived from OpenEye's FILTER technology. This toolkit is useful for calculating an extensive list 2D molecular properties and building custom filters around these properties.

**Note:** The version number of *MolProp TK* will track with the FILTER application to indicate similarities.

- This release of OEChem introduces many bug fixes and new features provided they didn't break source-level compatibility with 1.7.0.
- This release completes the transition from the old LaTeX based documentation system to the new reStructured-Text based system. This includes better support for Python and Java in the manuals as separate manuals for every library.
- The OE\_ARCH environment variable has been introduced to force the python libraries to load shared libraries for a specific architecture. This can be useful for getting OpenEye libraries to work on non-officially-supported platforms.
- Quacpac: Added support for writing a custom OETautomerMolFunction or OETyperMolFunction in Python by deriving from the base class.

# 8.33 OEToolkits 1.7.0

This is a new release of the OpenEye Toolkits with versions of the following libraries:

**OEChem TK** 1.7.0 **Grid TK** 132 Lexichem TK  $1.9.0$ Ogham TK 1.7.0 **Omega TK** 2.3.3 Quacpac TK 1.4.0 Shape TK 1.7.1 Spicoli TK 1.0.2 Szybki TK 1.3.4

- **Zap TK** 2.1.1
- This release starts the transition from the old LaTeX based documentation system to the new reStructuredText based system.
- Starting with *OEChem* 1.7.0 the core OpenEye toolkits (OEPlatform, OESystem, OEChem, OEBio) are now considered "thread-safe". The Thread Safety section in the OEChem theory manual goes into more depth of what it means to be "thread-safe". Many minor changes were made to achieve this, only the major ones are listed in the release notes. No guarantee is made about any other library.

Note: The Python global interpreter lock is released around computationally expensive OEChem functions. Even so, the utility of threading in Python is still limited.

• Many example programs have been renamed and cleaned up to provide better support across all three languages.

• Documentation example code is given a descriptive name instead of an out of date chapter and section number.