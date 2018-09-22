#!/usr/bin/env python3
import argparse
from clmstutorial.parsing import init_parser, parse_sent

if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('grammar', help='Path to the grammar file')

    args = p.parse_args()

    parser = init_parser(args.grammar)
    parses = parse_sent(parser, 'Hello, world!')
    next(parses).pretty_print()