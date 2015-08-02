#!/usr/bin/env python
from __future__ import print_function

import argparse
import os
from subprocess import check_output
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('ARGS', nargs='*')
    args = parser.parse_args()

    if args.ARGS:
        output = check_output('eval $({}) > /dev/null; printenv'
                              .format(' '.join(args.ARGS)),
                              shell=True)
        new_env = parse_printenv(output)
    else:
        new_env = parse_printenv(sys.stdin)

    diff = dict_diff(os.environ, new_env)
    print(fishify(diff))


def parse_printenv(output):
    if isinstance(output, bytes):
        lines = (l for l in output.splitlines())
    elif hasattr(output, 'read'):
        lines = output

    env = {}
    for line in lines:
        var, val = line.split('=', 1)
        env[var] = val.strip()
    return env


def dict_diff(this, that):
    diff = set(that.keys()) - set(this.keys())
    return {key: that[key] for key in diff}


def fishify(env):
    return '; and '.join('set -x {} {}'.format(k, v) for k, v in env.iteritems())


def escape(string):
    return string.replace(' ', '\ ')


if __name__ == '__main__':
    main()
