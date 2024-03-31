#!/bin/bash

set -eu

# setup poetry
# ------------------------------------------------------------------------------
echo "Setting up Poetry...."
poetry env use python3.10
poetry shell
poetry install


# setup Node
# ------------------------------------------------------------------------------
echo "Setting up Node...."

# remove node_modules
rm -rf node_modules

# install tailwindcss
npm install tailwindcss

# install stylelint
npm install stylelint stylelint-config-standard

# install prettier
npm install prettier

# install yuglify
npm install yuglify
