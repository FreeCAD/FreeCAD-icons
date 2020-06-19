#!/bin/bash
# triplus 2020

# Check if themes directory was modified
if git diff --quiet HEAD -- Themes; then
  touch modified
fi

# Check if metadata directory was modified
if git diff --quiet HEAD -- Metadata; then
  touch modified
fi

# Stop if nothing was modified
if [ ! -f modified ]; then
  echo "No modifications detected."
  exit 0
fi

mkdir deploy

# Create theme packs
cd Themes
for f in *; do
  if [ -d ${f} ]; then
    cd $f
    # Deterministic compilation
    # Backwards compatibility (Qt 5.8 and earlier)
    /usr/bin/rcc --binary theme.qrc -o ../../deploy/$f.rcc --format-version 1
    cd ..
  fi
done
cd ..

# Update metadata
/usr/bin/python3 Travis/travis.py
cd Metadata
zip -rT ../deploy/metadata.zip .
cd ..

