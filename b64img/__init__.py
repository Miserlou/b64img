#! /usr/bin/env python

from __future__ import print_function

import base64
import argparse
import xerox

def convert_image(args):
    paths = args['query']
    copy = args['copy']
    encoded = ''

    for path in paths:
        with open(path,'rb') as img:
            encoded = encoded + 'data:image/png;base64,' + base64.b64encode(img.read())
            encoded = encoded + "\n"

    if copy:
        xerox.copy(encoded)

    print(encoded)

def get_parser():
    parser = argparse.ArgumentParser(description='Command line b64 image converter.')
    parser.add_argument('query', metavar='QUERY', type=str, nargs='*',
            help='The path of the image to encode.')
    parser.add_argument('-c','--copy', help='copy result to the clipboard.', default=False, dest='copy', action='store_true')
    return parser

def command_line_runner():
    parser = get_parser()
    args = vars(parser.parse_args())
    if not args['query']:
        parser.print_help()
        return
    if args['query']:
        convert_image(args)
    
if __name__ == '__main__':
    command_line_runner()
