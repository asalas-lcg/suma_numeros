#!/usr/bin/env python3
import argparse
import sys

parser = argparse.ArgumentParser(description="Generate k-mers from a DNA sequence")
parser.add_argument("--sequence", type=str, required=True)
parser.add_argument("--k", type=int, required=True)

args = parser.parse_args()
sequence = args.sequence.upper()
k = args.k

valid = {"A","T","G","C"}

if len(sequence) == 0:
    print("Error: sequence is empty")
    sys.exit(1)

for n in sequence:
    if n not in valid:
        print(f"Error: invalid character '{n}'")
        sys.exit(1)

if k <= 0:
    print("Error: k must be > 0")
    sys.exit(1)

if k > len(sequence):
    print("Error: k too large")
    sys.exit(1)

for i in range(len(sequence)-k+1):
    print(sequence[i:i+k])
