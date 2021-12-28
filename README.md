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

--->


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ld_impl_linux-64-2.35.1    |       h7274673_9         586 KB
    libffi-3.3                 |       he6710b0_2          50 KB
    python-3.7.11              |       h12debd9_0        45.3 MB
    readline-8.1               |       h27cfd23_0         362 KB
    sqlite-3.36.0              |       hc218d9a_0         990 KB
    ------------------------------------------------------------
                                           Total:        47.3 MB

The following NEW packages will be INSTALLED:

  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.35.1-h7274673_9

The following packages will be REMOVED:

  libedit-3.1.20210910-h7f8727e_0

The following packages will be UPDATED:

  libffi                                3.2.1-hf484d3e_1007 --> 3.3-he6710b0_2
  python                                   3.7.4-h265db76_1 --> 3.7.11-h12debd9_0
  readline                                   7.0-h7b6447c_5 --> 8.1-h27cfd23_0
  sqlite                                  3.33.0-h62c20be_0 --> 3.36.0-hc218d9a_0


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
