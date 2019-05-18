#!/usr/bin/env python3

"""
VUnit run script
"""

import os
import pathlib
import vunit as vunit_pkg


REPO_DIR = pathlib.Path(os.getcwd())
SOURCES_DIR = REPO_DIR / 'sources'


def map_sources(vunit):
    print(SOURCES_DIR)
    libs = []
    for (root, dir, files) in os.walk(SOURCES_DIR):
        if any(fn.endswith('.vhd') for fn in files):
            lib = vunit.add_library("lib")
            for vhd_file in (fn for fn in files if fn.endswith('.vhd')):
                lib.add_source_file(file_name=pathlib.Path(root) / vhd_file)
            libs.append(lib)
    return vunit


def run_tests(vunit):
    """Start test run."""
    vunit.main()


def main():
    """Stand alone entry point."""
    vunit = vunit_pkg.VUnit.from_argv()
    vunit = map_sources(vunit)
    run_tests(vunit)


if __name__ == '__main__':
    main()
