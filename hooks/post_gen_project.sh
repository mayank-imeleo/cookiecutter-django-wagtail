#!/bin/bash

set -eu

echo "executing post_gen_project.sh...."

# setup poetry
# ------------------------------------------------------------------------------
echo "Setting up Poetry...."

echo "Creating a virtual environment...."
poetry env use python3.10
echo "Creating a symlink for the virtual environment. venv -> .venv...."
ln -sf .venv venv

echo "Installing dependencies...."
source venv/bin/activate
poetry install


#echo "Activating the virtual environment...."
#source venv/bin/activate

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


# Django setup
## ------------------------------------------------------------------------------
#echo "creating django database {{cookiecutter.database_name}}...."
#django_create_db "{{cookiecutter.database_name}}"

echo "use source venv/bin/activate to activate the virtual environment...."

echo "executing post_gen_project.sh finished...."
