

### Install
```
wget   https://github.com/arita37/zbuild/suites/4530351276/artifacts/121312337    operon.zi[p

unzip operon.zip


conda install --offline  /path/operon-0.0.1-py37h2bc3f7f_0.tar.bz2


#### Need to install other requirements
while read req; do conda install --yes $req; done < build_operon/reqs.txt
   


The following NEW packages will be INSTALLED:

    _libgcc_mutex:    0.1-conda_forge             conda-forge
    _openmp_mutex:    4.5-1_gnu                   conda-forge
    ca-certificates:  2021.10.8-ha878542_0        conda-forge
    fmt:              8.0.1-h4bd325d_0            conda-forge
    gflags:           2.2.2-he1b5a44_1004         conda-forge
    joblib:           1.1.0-pyhd8ed1ab_0          conda-forge
    ld_impl_linux-64: 2.36.1-hea4e1c9_2           conda-forge
    libblas:          3.9.0-12_linux64_openblas   conda-forge
    libcblas:         3.9.0-12_linux64_openblas   conda-forge
    libffi:           3.4.2-h7f98852_5            conda-forge
    libgcc-ng:        11.2.0-h1d223b6_11          conda-forge
    libgfortran-ng:   11.2.0-h69a702a_11          conda-forge
    libgfortran5:     11.2.0-h5c6108e_11          conda-forge
    libgomp:          11.2.0-h1d223b6_11          conda-forge
    liblapack:        3.9.0-12_linux64_openblas   conda-forge
    libnsl:           2.0.0-h7f98852_0            conda-forge
    libopenblas:      0.3.18-pthreads_h8fe5266_0  conda-forge
    libstdcxx-ng:     11.2.0-he4da1e4_11          conda-forge
    libzlib:          1.2.11-h36c2ea0_1013        conda-forge
    ncurses:          6.2-h58526e2_4              conda-forge
    numpy:            1.21.4-py37h31617e3_0       conda-forge
    openlibm:         0.7.0-h516909a_0            conda-forge
    openssl:          3.0.0-h7f98852_2            conda-forge
    operon:           0.0.1-py37h42a920f_0        local      
    pip:              21.3.1-pyhd8ed1ab_0         conda-forge
    python:           3.7.12-hf930737_100_cpython conda-forge
    python_abi:       3.7-2_cp37m                 conda-forge
    readline:         8.1-h46c0cb4_0              conda-forge
    scikit-learn:     1.0.1-py37hf9e9bfc_2        conda-forge
    scipy:            1.7.3-py37hf2a6cf1_0        conda-forge
    setuptools:       59.4.0-py37h89c1867_0       conda-forge
    sqlite:           3.37.0-h9cd32fc_0           conda-forge
    threadpoolctl:    3.0.0-pyh8a188c0_0          conda-forge
    tk:               8.6.11-h27826a3_1           conda-forge
    wheel:            0.37.0-pyhd8ed1ab_1         conda-forge
    xz:               5.2.5-h516909a_1            conda-forge
    zlib:             1.2.11-h36c2ea0_1013        conda-forge
    
    
```


### Requirements python
```
requirements:
  build:
    - {{ compiler('cxx') }}
    - python {{ python }}
    - make
    - cmake
    - fmt >=8.0.0
    - ceres-solver
    - doctest
    - taskflow
    - eigen
    - cxxopts
    - openlibm
    - pybind11
  host:
    - python {{ python }}
    - libstdcxx-ng
    - fmt >=8.0.0
    - doctest
    - taskflow
    - openlibm
    - gflags
  run:
    - python {{ python }}
    - openlibm
    - numpy
    - scikit-learn
```




### Conda install of reqs.txt
```

 iterating over the lines of the file

    while read req; do conda install --yes $req; done < reqs.txt


Edit: If you would like to install a package using pip if it is not available through conda, give this a go:

$ while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt



```



### Build Process:
    Github Actions
    https://github.com/arita37/zbuild/blob/zbuild_operon/.github/workflows/build_operon_py37.yml

    Cmake instructions:
    https://github.com/heal-research/operon/blob/master/CMakeLists.txt


### Docs

    https://operongp.readthedocs.io/en/latest/build.html#

    https://github.com/heal-research/operon



