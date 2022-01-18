# conda package for hnsw


## Purpose

This script will create a package for HNWW library
that can be installed by conda install.

https://github.com/arita37/cat_hnswlib/tree/master/python_bindings



## Build

please check here
https://github.com/arita37/zbuild/actions/workflows/build.yml

https://github.com/arita37/zbuild/tree/zbuild_hnsw/build_hnsw


```
git clone ...
cd /path/to/repo
conda build -c conda-forge recipe
```
You can also download the tar-ball as an artifact that is created by the github action.

## Install

```
conda install /path/to/-*.tar.bz2
conda update --all




    python-3.7.11              |       h12debd9_0        45.3 MB
    
    
    

```

## Compile problem
### gcc version
The latest version of gcc in version gcc 11.2.0 in conda,
as of December 26, 2021.

gcc 11.2.0 does not compile successfully as shown below.

```
:1: note: 'const char _ZTSZN5pecos13PostProcessorIfEC4ERKSt8functionIFfRKfEERKS2_IFfS4_S4_EEEd0_UlS4_E_ [78]' previously defined here
```

I checked and it seems to be gcc 11.2.0 that causes this problem.

| version | Compilation |
|---------|-------------|
| 9.4.0   | Success     |
| 10.3.0  | Success     |
| 11.2.0  | Failure     |

The package is compiled with 9.4.0, but there is no problem in using glibc since glibc is backward compatible.

### libpthread link problem
The build could not find the `pthread_nonshared.a` installed by conda.
I have not investigated why, but since it was a static library, I installed `glibc-devel` additionally.
