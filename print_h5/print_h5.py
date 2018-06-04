#!/usr/bin/env python
"""Print the contents of an HDF5file"""

import numpy as np
# ddd
#np.warnings.filterwarnings("")
import h5py
import argparse


def print_node(node, indent: int =4) -> str:
    """

    Args:
        node: The node to print
        indent: How many spaces per indent level

    Returns:
        None

    Examples:
        >>> print_node("a/b/c", indent=4)
        "        c"
        >>> print_node("a")
        a
        >>> print_node("a/b", indent=3)
        b
    """

    *first, last = str(node).split("/")
    print(" " * indent * len(first) + last)

def print_h5(h5filename, indent = 4) -> object:
    """For a given HDF5file, print its contents"""
    with h5py.File(h5filename) as h5file:
        h5file.visit(lambda node: print_node(node, indent=indent))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("h5file", help="HDF5 file fto display")

    parser.add_argument("-i", "--indent", help="Indentation (default 4)",
                        type=int, default=4)
    args = parser.parse_args()
    print(args.h5file)

    #print_h5("/home/josan/Annecy2018/School2018/codingstyle/lofar-cal.h5")

if __name__ == "__main__":
    main()

