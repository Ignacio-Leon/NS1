#!/usr/bin/env python3

import json
import random
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: rmap_select.py <routemap json file>")
        return 1

    with open(sys.argv[1]) as json_file:
        data = json.load(json_file)
        for elem in data["map"]:
            print(f"labels: {elem['labels']}")
            pf = random.choice(elem['networks'])
            print(f"prefix: {pf}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())

