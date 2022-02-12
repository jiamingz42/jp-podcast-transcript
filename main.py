#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

def get_sentences(lines):
    for line in lines:
        idxs = [i for i, c in enumerate(line) if c in "。！"]
        for i, idx in enumerate(idxs):
            if i == 0:
                s = line[:idx+1]
            else:
                s = line[idxs[i-1]+1:idx+1]
            yield s.strip()


def main():
    assert len(sys.argv) == 2, "Should contains exactly one argv"

    with open(sys.argv[1], "r") as f:
        content = f.read()

    lines = [line for line in content.split("\n") if line.strip()]

    for i, s in enumerate(get_sentences(lines)):
        content = (
            f"{i}\n"
            "00:00:00,000 --> 0:00:00,000\n"
            f"{s}\n")
        print(content)

main()


