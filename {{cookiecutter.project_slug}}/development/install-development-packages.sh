#!/bin/bash

set -eu

echo "Install development packages"

echo "Install pyutils in development mode"
pip install -r requirements/development.txt

./development/install-pyutils-static-files.sh