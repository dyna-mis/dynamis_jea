#!/bin/sh
rm -rf Debug/*
rm -rf Release/*
cd Debug
cmake -DBUILD_DEPS=ON -DCMAKE_BUILD_TYPE=Debug ../..
make -j8

cd ../Release
cmake -DBUILD_DEPS=ON -DCMAKE_BUILD_TYPE=Release ../..
make -j8
