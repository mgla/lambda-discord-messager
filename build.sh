#!/bin/sh
cd venv/lib/python3.8/site-packages && zip -r ../../../../package.zip .
cd -
zip -g package.zip lambda_function.py

