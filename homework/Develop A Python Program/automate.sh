#!/bin/bash
cat impl.py | grep "^\W\+[A-Z_]\+\|def \|class\|#" > spec_basis.txt

