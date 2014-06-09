#!/bin/bash

packdir=$(pwd)
packbase=$(basename "$packdir")
cd ..
sudo rsync -avu "$packdir" /usr/lib/python2.7/dist-packages/
