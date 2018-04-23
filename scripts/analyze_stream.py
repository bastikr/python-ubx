#!/usr/bin/env python

import argparse
import sys
import os

from ubx.reader import UBXReader as Reader
from ubx.reader import UBXReaderException
import ubx


argparser = argparse.ArgumentParser(description="Analyze a UBX stream")
argparser.add_argument("input", help="file or socket")

args = argparser.parse_args()

if ":" in args.input:
    raise NotImplementedError()
else:
    if not os.path.exists(args.input):
        raise ValueError("Given argument is neither a path nor a socket.")
    f = open(args.input, "rb")
    read_raw = f.read


stats = ubx.Statistics()
def read(n):
    stats.add_bytesread_try(n)
    result = read_raw(n)
    stats.add_bytesread_success(len(result))
    sys.stdout.write("Bytes read: {}\r".format(stats.bytes_read_success))
    return result

reader = Reader(read)
parser = ubx.default_parser

def run():
    while True:
        try:
            rawmessage = reader.read_rawmessage()
        except ubx.ChecksumError as e:
            stats.add_error()
            continue
        except:
            break

        try:
            message = parser.parse(rawmessage)
        except KeyError:
            stats.add_unknownmessage(rawmessage)
            continue
        stats.add_knownmessage(message)

try:
    run()
except (ValueError, KeyboardInterrupt):
    pass

sys.stdout.write(" " * 50 + "\r")
print(stats)
