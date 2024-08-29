#!/usr/bin/env python3
''' this is a module '''


import re


def filter_datum(fields, redaction, message, separator):
    ''' function itself '''
    for j in fields:
        pat = r'{}=[^{}]+'.format(j, separator)
        r = f'{j}='+redaction
        message = re.sub(pat, r, message)
    return message
