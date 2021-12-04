#!/bin/sh

set +x

mkdir -p build
cd build

cmake                              \
    -DPython3_EXECUTABLE="$PYTHON" \
    -DCMAKE_INSTALL_PREFIX=$SP_DIR \
    -DCMAKE_BUILD_TYPE=Release     \
    -DBUILD_PYBIND=ON              \
    -DUSE_OPENLIBM=ON              \
    -DUSE_SINGLE_PRECISION=ON      \
    -DCERES_TINY_SOLVER=ON         \
    $SRC_DIR

make VERBOSE=1 -j${CPU_COUNT} pyoperon
make install
