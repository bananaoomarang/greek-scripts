#!/bin/bash

INPUT_DIR=$1
OUTPUT_DIR=$2

rm -rf $OUTPUT_DIR
mkdir $OUTPUT_DIR

for f in $INPUT_DIR/*
do
    echo "Converting $f..."
    OUTPUT_PATH="$OUTPUT_DIR/$(basename $f)"
    ./bin/betacode.pl $f > $OUTPUT_PATH
done
