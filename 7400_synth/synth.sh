#!/bin/sh
set -e # exit on error

# Run statistics/BOM
cd stat
make $1.stat
cat $1.stat

# Synthesize to Low-level verilog
cd ../sim
make $1.vcd

# Compile into KiCAD netlist
cd ../kicad
make $1.net
