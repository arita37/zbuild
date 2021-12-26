# conda package for amazon pecos

December 26, 2021

## Purpose

This script will create a package for Amazon PECOS library
that can be installed by conda install.

The target repository is as follow:
- https://github.com/amzn/pecos.git

Note that there is another pecos package in conda-forge.

## Build

```
git clone ...
cd /path/to/repo
conda build -c conda-forge recipe
```
You can also download the tar-ball as an artifact that is created by the github action.

## Install

```
conda install /path/to/amzn_pecos-*.tar.bz2
conda update --all
```

## Compile problem
### gcc version
The latest version of gcc in version gcc 11.2.0 in conda,
as of December 26, 2021.

gcc 11.2.0 does not compile successfully as shown below.

```
pecos/core/libpecos.cpp:466:1: error: redefinition of 'const char _ZTSZN5pecos13PostProcessorIfEC4ERKSt8functionIFfRKfEERKS2_IFfS4_S4_EEEd_UlS4_S4_E_ []'
  466 | }
      | ^
pecos/core/libpecos.cpp:466:1: note: 'const char _ZTSZN5pecos13PostProcessorIfEC4ERKSt8functionIFfRKfEERKS2_IFfS4_S4_EEEd_UlS4_S4_E_ [80]' previously defined here
pecos/core/libpecos.cpp:466:1: error: redefinition of 'const char _ZTSZN5pecos13PostProcessorIfEC4ERKSt8functionIFfRKfEERKS2_IFfS4_S4_EEEd0_UlS4_E_ []'
pecos/core/libpecos.cpp:466:1: note: 'const char _ZTSZN5pecos13PostProcessorIfEC4ERKSt8functionIFfRKfEERKS2_IFfS4_S4_EEEd0_UlS4_E_ [78]' previously defined here
```

I checked and it seems to be gcc 11.2.0 that causes this problem.

| version | Compilation |
|---------|-------------|
| 9.4.0   | Success     |
| 10.3.0  | Success     |
| 11.2.0  | Failure     |

The package is compiled with 9.4.0, but there is no problem in using glibc since glibc is backward compatible.

### libpthread link problem
The pecos build could not find the `pthread_nonshared.a` installed by conda.
I have not investigated why, but since it was a static library, I installed `glibc-devel` additionally.
