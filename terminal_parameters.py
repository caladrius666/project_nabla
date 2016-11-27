# coding: utf-8

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    'path',
    type=str,
)

parser.add_argument(
    '-sa',
    '--show_approx',
    action='store_true',
)

parser.add_argument(
    '-ax',
    '--axis',
    action='store_true',
)

parser.add_argument(
    '-hg',
    '--hide_grid',
    action='store_true',
)

parser.add_argument(
    '-sp',
    '--show_podgon',
    action='store_true',
)

args = parser.parse_args()
