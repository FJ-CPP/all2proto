#!/usr/bin/env bash

# install yapf if not installed
if ! [ -x "$(command -v yapf)" ]; then
  echo 'Error: yapf is not installed.' >&2
  echo 'Installing yapf...'
  pip install yapf
fi

root_dir=$(git rev-parse --show-toplevel)
style_file="$root_dir/.style.yapf"
target_dirs="all2proto scripts tests"

for dir in $target_dirs; do
    find "$root_dir"/"$dir" -name "*.py" -exec yapf --style="$style_file" -vv --in-place '{}' \;
done
