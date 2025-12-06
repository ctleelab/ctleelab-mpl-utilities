#!/usr/bin/env python3
#
# ctleelab-mpl-utilities: A collection of utilities for plotting with matplotlib
#
# Copyright 2025- ctleelab
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Please help us support development by citing the research
# papers on the package. Check out https://github.com/ctleelab/ctleelab-mpl-utilities/
# for more information.

import sys
import re

from pathlib import Path


def strip_comments(filename):
    """Load a file and strip comments (# style comments)."""
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        stripped_lines = []
        for line in lines:
            # Remove comments (everything after #)
            stripped_line = re.sub(r'#.*$', '', line).rstrip()
            # Keep the line if it's not empty after stripping
            if stripped_line:
                stripped_lines.append(stripped_line)

        return stripped_lines

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

if __name__ == "__main__":
    ref = Path("ctleelab_plothelper/base-ref.mplstyle")
    stripped_content = strip_comments(ref)

    stripped = Path("ctleelab_plothelper/base.mplstyle")
    # if stripped.exists():
    #     stripped.unlink()
    if stripped_content is not None:
        with open(stripped, 'w') as file:
            for line in stripped_content:
                file.write(line + '\n')
