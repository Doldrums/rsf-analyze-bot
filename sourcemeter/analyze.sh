#!/usr/bin/env bash

git clone $@
projectName=$(basename "$@" .git) 
./AnalyzerPython -projectBaseDir:./$projectName -projectName:$projectName -resultsDir:./results -pythonVersion:3 -pythonBinary:python3 -currentDate:latest
mkdir /results/$projectName
cp ./results/$projectName/python/latest/*.csv /results/$projectName
