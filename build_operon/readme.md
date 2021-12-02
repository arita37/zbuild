

### Install
```
wget   https://github.com/arita37/zbuild/suites/4530351276/artifacts/121312337    operon.zi[p

unzip operon.zip


conda install operon-0.0.1-py.tar.bz2


### Depndenencies
conda update -all

```


### Conda install of reqs.txt
```

I ended up just iterating over the lines of the file

    while read req; do conda install --yes $req; done < requirements.txt


Edit: If you would like to install a package using pip if it is not available through conda, give this a go:

$ while read requirement; do conda install --yes $requirement || pip install $requirement; done < requirements.txt

Edit: If you are using Windows (credit goes to @Clay):

$ FOR /F "delims=~" %f in (requirements.txt) DO conda install --yes "%f" || pip install "%f"

```



### Build Process:
    Github Actions
    https://github.com/arita37/zbuild/blob/zbuild_operon/.github/workflows/build_operon_py37.yml

    Cmake instructions:
    https://github.com/heal-research/operon/blob/master/CMakeLists.txt


### Docs

    https://operongp.readthedocs.io/en/latest/build.html#

    https://github.com/heal-research/operon



