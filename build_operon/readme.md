

### Install
```
wget   https://github.com/arita37/zbuild/suites/4530351276/artifacts/121312337    operon.zi[p

unzip operon.zip


conda install --offline  /path/operon-0.0.1-py37h2bc3f7f_0.tar.bz2




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



