#!/usr/bin/python3
"""Program that counts status codes in a log and prints them periodicaly"""

import sys
import re

status_codes = {code: 0 for code in [200, 301, 400, 401, 403, 404, 405, 500]}
file_size = 0

pattern = re.compile(r'.+ - .* "GET /projects/260 HTTP/1.1" (\d+) (\d+)')


def parse_line(line):
    """
    parses log line and gets the code and size
    Args:
        line: the line to be parsed
    """
    m = pattern.match(line)
    if m:
        return (int(m.group(1)), int(m.group(2)))
    else:
        return (0, 0)


count = 0
while True:
    try:
        line = sys.stdin.readline()
        code, size = parse_line(line)
        status_codes[code] += 1
        file_size += size
        count += 1
        if count == 10:
            raise KeyboardInterrupt
    except KeyboardInterrupt:
        print('File size:', file_size)
        for code, occ in status_codes.items():
            if occ > 0:
                print(f'{code}: {occ}')
        count = 0
