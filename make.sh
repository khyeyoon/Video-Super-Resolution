#!/usr/bin/env bash

# You may need to modify the following paths before compiling
CUDA_HOME=/usr/local/cuda-10.1 \
CUDNN_INCLUDE_DIR=/usr/include \
CUDNN_LIB_DIR=/usr/include/x86_64-linux-gnu/cudnn_v7.h \
python setup.py develop
