#!/usr/bin/env bash

echo "remove logs"

echo "update code"

edho "generate and update supervisor"

echo "reset kafka"

echo "build aws container" 

echo "run test"
pytest -o faulthandler_timeout=120

echo "print version"
python <<< 'import volive; print(volive.__version__)'


