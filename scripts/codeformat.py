#!/usr/bin/env python

import subprocess
import os
import sys
import pip
import shutil


def install_package(package_name):
    pip.main(['install', package_name])


def is_tool_installed(tool_name):
    """Check whether `tool_name` is on PATH and marked as executable."""
    return shutil.which(tool_name) is not None


if not is_tool_installed('yapf'):
    print('Error: yapf is not installed.', file=sys.stderr)
    print('Installing yapf...')
    install_package('yapf')

try:
    root_dir = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],
                                       universal_newlines=True).strip()
    print(f'Root directory: {root_dir}')
except subprocess.CalledProcessError:
    print(
        'Error: unable to determine the root directory. Are you inside a git repository?',
        file=sys.stderr)
    sys.exit(1)

style_file = os.path.join(root_dir, '.style.yapf')
target_dirs = ['all2proto', 'scripts', 'tests']  # Directories to format

for dir_name in target_dirs:
    for root, dirs, files in os.walk(os.path.join(root_dir, dir_name)):
        for file_name in files:
            if file_name.endswith('.py'):
                file_path = os.path.join(root, file_name)
                yapf_command = [
                    'yapf', '--style', style_file, '-vv', '--in-place',
                    file_path
                ]
                subprocess.run(yapf_command)

if __name__ == '__main__':
    pass
