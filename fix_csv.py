"""
***Write a program fix_csv.py that turns a pipe-delimited file into a CSV file
***Allow the input delimiter and quote character to be optionally specified.
***Automatically detect the delimiter if an in-delimiter value isn't supplied (don't assume it's pipe and quote, figure it out).
"""
from argparse import ArgumentParser
import csv
import sys



parser = ArgumentParser()
parser.add_argument("-i",help="choose delimiter for input file",action="store",dest="input_delimiter",type=str) #default="|"
parser.add_argument("-q",help="quote character for input file",action="store",dest="quote_char",type=str) #default='"'
results = parser.parse_args()

old_filename = sys.argv[1]
new_filename = sys.argv[2]



with open(old_filename, newline='') as old_file:
    arguments = {}
    if results.input_delimiter:
        arguments['delimiter'] = results.input_delimiter
    if results.quote_char:
        arguments['quotechar'] = results.quote_char
    if not results.input_delimiter and not results.quote_char:
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0)
    reader = csv.reader(old_file, **arguments)
    with open(new_filename, 'w', newline='') as new_file:
        writer = csv.writer(new_file,delimiter=',')
        writer.writerows(reader)


