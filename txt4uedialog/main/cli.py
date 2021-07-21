"""
Tool for converting csv to json compatible with the dialog plugin
"""

import argparse
import os
import logging
import k3logging

import txt4uedialog
from txt4uedialog import __version__

__author__ = 'Joachim Kestner <kestner@lightword.de>'

logger = logging.getLogger(__name__)

def main():
    parser = argparse.ArgumentParser(description=__doc__+"\n\nAuthor: {}\nVersion: {}".format(__author__,__version__), formatter_class=argparse.RawDescriptionHelpFormatter)
    # parser.add_argument("-f", "--flag", action="store_true", help="Example argparse of a choice")
    # parser.add_argument("-c", "--choice", default="c1", choices=["c1", "c2", "c3", "c4"], help="Example of an argparse choice argument")
    parser.add_argument("-o", "--output", help="Output json file")
    parser.add_argument("input_csv_file", help="The input csv file")
    
    k3logging.set_parser_log_arguments(parser)
    
    args = parser.parse_args()
    
    k3logging.eval_parser_log_arguments(args)
    
    if args.output:
        outputfile = args.output
    else:
        base, ext = os.path.splitext(args.input_csv_file)
        outputfile = os.path.abspath(base+".json")
    
    txt4uedialog.convert_to_json(args.input_csv_file, outputfile)
