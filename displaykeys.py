#!/usr/bin/env python

import struct
import sys

infile_path = "/dev/input/event" + (sys.argv[1] if len(sys.argv) > 1 else "0")

FORMAT = 'llHHI'

event_size = struct.calcsize(FORMAT)

in_file = open(infile_path, 'rb')

event = in_file.read(event_size)

while event:
    (tv_sec, tv_usec, keytype, code, value) = struct.unpack(FORMAT, event)
    if keytype !=0 or code != 0:
        print("Event type: {}, code: {}, value: {}, time: {}".format(keytype, code, value, tv_sec))
    else:
        print("=======================================================")
    event = in_file.read(event_size)

