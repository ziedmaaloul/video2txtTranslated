#!/bin/sh
inputFile=${1}
targetlang=${2}
outfile=${3}

python /input/bash.py --inputfilepath ${inputFile} --output_language ${targetlang} --outputfolder ${outfile}
