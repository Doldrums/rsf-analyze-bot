#!/usr/bin/env bash

git clone --depth 1 $@
projectName=$(basename "$@" .git) 
if [[ ! -e $projectName/__init__.py ]]; then
    touch $projectName/__init__.py
fi
./AnalyzerPython -projectBaseDir:./$projectName -projectName:$projectName -resultsDir:./results -pythonVersion:3 -pythonBinary:python3 -currentDate:latest
mkdir /results/$projectName
cp ./results/$projectName/python/latest/*.csv /results/$projectName
