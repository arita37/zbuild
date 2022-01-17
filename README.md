# conda package for hnsw


## Purpose

This script will create a package for ECOS library
that can be installed by conda install.





## Build

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


Working Env:  (tested with code execution)

name: t1
channels:
  - defaults
dependencies:
  - _libgcc_mutex=0.1=main
  - blas=1.0=mkl
  - bottleneck=1.3.2=py37heb32a55_1
  - ca-certificates=2021.10.26=h06a4308_2
  - certifi=2021.10.8=py37h06a4308_0
  - intel-openmp=2021.4.0=h06a4308_3561
  - ld_impl_linux-64=2.35.1=h7274673_9
  - libedit=3.1.20210910=h7f8727e_0
  - libffi=3.2.1=hf484d3e_1007
  - libgcc-ng=9.1.0=hdf63c60_0
  - libgfortran-ng=7.3.0=hdf63c60_0
  - libstdcxx-ng=9.1.0=hdf63c60_0
  - mkl=2021.4.0=h06a4308_640
  - mkl-service=2.4.0=py37h7f8727e_0
  - mkl_fft=1.3.1=py37hd3c417c_0
  - mkl_random=1.2.2=py37h51133e4_0
  - ncurses=6.3=h7f8727e_2
  - numexpr=2.7.3=py37h22e1b3c_1
  - numpy=1.21.2=py37h20f2e39_0
  - numpy-base=1.21.2=py37h79a1101_0
  - openssl=1.1.1l=h7f8727e_0
  - pandas=1.3.4=py37h8c16a72_0
  - python=3.7.4=h265db76_1
  - python-dateutil=2.8.2=pyhd3eb1b0_0
  - pytz=2021.3=pyhd3eb1b0_0
  - readline=7.0=h7b6447c_5
  - scipy=1.6.2=py37had2a1c9_1
  - setuptools=58.0.4=py37h06a4308_0
  - six=1.16.0=pyhd3eb1b0_0
  - sqlite=3.33.0=h62c20be_0
  - tk=8.6.11=h1ccaba5_0
  - wheel=0.37.0=pyhd3eb1b0_1
  - xz=5.2.5=h7b6447c_0
  - zlib=1.2.11=h7f8727e_4
  - pip:
    - joblib==1.1.0
    - libpecos==0.2.3
    - pip==19.2.3
    - scikit-learn==1.0.2
    - sklearn==0.0
    - threadpoolctl==3.0.0


--->

numpy scipy needed


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



   1630
   1631
-> 1632 clib = corelib(os.path.join(os.path.dirname(os.path.abspath(pecos.__file__)), "core"), "libpecos")

/opt/anaconda3/envs/test/lib/python3.7/site-packages/pecos/core/base.py in __init__(self, dirname, soname, forced_rebuild)
    505     def __init__(self, dirname, soname, forced_rebuild=False):
    506         self.clib_float32 = corelib.load_dynamic_library(
--> 507             dirname, soname + "_float32", forced_rebuild=forced_rebuild
    508         )
    509         self.link_xlinear_methods()

/opt/anaconda3/envs/test/lib/python3.7/site-packages/pecos/core/base.py in load_dynamic_library(dirname, soname, forced_rebuild)
    500                 _c_lib = CDLL(path_to_so)
    501             except BaseException:
--> 502                 raise Exception("{soname} library cannot be found and built.".format(soname=soname))
    503         return _c_lib
    504

Exception: libpecos_float32 library cannot be found and built.




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
