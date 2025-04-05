#!/usr/bin/env bash

set -e

echo -e "Running flake8..."
flake8 .

echo -e "\nRunning mypy..."
mypy .

echo -e "\nRunning pylint..."
pylint .

echo -e "\nRunning ruff..."
ruff check .

echo -e "\nAll linters completed!"
