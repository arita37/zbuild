

Building the wheel  or conda
```

Github action:
https://github.com/amzn/pecos/blob/mainline/.github/workflows/build_pypi.yml


## Wheel building
https://github.com/amzn/pecos/blob/mainline/.github/build_pypi_wheel.sh




#### Need conda for
  python 3.7  only


   First, in your user home directory, run the conda skeleton command:

   conda skeleton pypi libpecos

   



Install and develop locally
git clone https://github.com/amzn/pecos
cd pecos
python3 -m pip install --editable ./



#################################################################################################
numpy_requires = [
    'numpy<1.20.0; python_version<"3.7"', # setup_requires needs correct version for <3.7
    'numpy>=1.19.5; python_version>="3.7"'
]
setup_requires = numpy_requires + [
    'pytest-runner',
    'sphinx_rtd_theme'
]
install_requires = numpy_requires + [
    'scipy>=1.4.1',
    'scikit-learn>=0.24.1',
    'torch>=1.8.0',
    'sentencepiece>=0.1.86,!=0.1.92', # 0.1.92 results in error for transformers
    'transformers>=4.1.1; python_version<"3.9"',
    'transformers==4.4.2; python_version>="3.9"' # Python 3.9 only support transformer 4.4.2




######################################################################################
##### Test code
import numpy as np
X = np.random.random((10,5))
Y = np.random.random(5)



>>> from pecos.xmc.xlinear.model import XLinearModel
>>> from pecos.xmc import Indexer, LabelEmbeddingFactory

# Build hierarchical label tree and train a XR-Linear model
>>> label_feat = LabelEmbeddingFactory.create(Y, X)
>>> cluster_chain = Indexer.gen(label_feat)
>>> model = XLinearModel.train(X, Y, C=cluster_chain)
>>> model.save("./save-models")


```




### Install
```
wget   https://github.com/arita37/zbuild/suites/4530351276/artifacts/121312337    pecos.zi[p

unzip pecos.zip


conda install   /path/pecos-0.0.1-py37h2bc3f7f_0.tar.bz2
conda update -c conda-forge --all

pip install scikit-learn numpy



#### Need to install other requirements
while read req; do conda install --yes $req; done < build_pecos/reqs.txt
 
 
 
 In [6]: X = np.random.random((10,5))

In [7]: y= np.random.random((10,1))




Downloading and Extracting Packages
taskflow-3.2.0       | 105 KB    | ##################################################################################################### | 100%
zstd-1.5.0           | 490 KB    | ##################################################################################################### | 100%
fmt-8.0.1            | 170 KB    | ##################################################################################################### | 100%
lz4-c-1.9.3          | 179 KB    | ##################################################################################################### | 100%
pybind11-2.8.1       | 160 KB    | ##################################################################################################### | 100%
pybind11-global-2.8. | 193 KB    | ##################################################################################################### | 100%
cmake-3.21.3         | 15.2 MB   | ######



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
    pecos:           0.0.1-py37h42a920f_0        local      
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


#### Errors:
```



WARNING conda.core.prefix_data:_load_single_record(190): 
Ignoring malformed prefix record at: mconda/envs/py37/conda-meta/pecos-0-1.0.1-py37_0.json



python -c 'import numpy as np;from pecos.sklearn import SymbolicRegressor;'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/mconda/envs/py37/lib/python3.7/site-packages/pecos/__init__.py", line 4, in <module>
    from ._pecos import *
ImportError: libfmt.so.8: cannot open shared object file: No such file or directory




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
    https://github.com/arita37/zbuild/blob/zbuild_pecos/.github/workflows/build_pecos_py37.yml

    Cmake instructions:
    https://github.com/heal-research/pecos/blob/master/CMakeLists.txt


    There is a patch in conda build to activate AVX C++ Build.



### Docs

    https://pecosgp.readthedocs.io/en/latest/build.html#

    https://github.com/heal-research/pecos




