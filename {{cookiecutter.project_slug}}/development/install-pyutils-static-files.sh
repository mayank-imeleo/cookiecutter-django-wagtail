#!/bin/bash

set -eu

SRC="venv/lib/python3.10/site-packages/pyutils/static"
DST=mooving_oms/static/pyutils

echo "Removing pyutils static files from $DST"
rm -rf "$DST"

echo "Copying pyutils static files from $SRC to $DST"

# copy only if destination directory exists
if [ -d "$DST" ]; then
  cp -rv "$SRC" "$DST"
fi
