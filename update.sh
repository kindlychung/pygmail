#!/usr/bin/env bash

python3 setup.py bdist_wheel
python3 setup.py bdist_wheel upload
pip3 install $1 -U
