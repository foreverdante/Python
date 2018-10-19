#!/usr/bin/env python3

import csv
import os

class PdfConverter:
    def __init__(self, path=None, file=None):
        self.path = path # Set pathname
        self.file = file # Set filename

    def isPath(self):
        if self.path is not False:
            return True
        else:
            return False

    def isFile(self):
        if self.file is not False:
            return True
        else:
            return False

def readDocument(fname, pathname, user):
    fname = pathname + fname
    with open(fname, 'r') as file:
        reader = csv.reader(file)
        for row in enumerate(reader):
            if user is row[0]:
                print(row)


if __name__ == '__main__':
    info = {
        'path': '/home/<username>/$PATH_TO_DOCUMENT',
        'file': 'pdfconverter',
        'suffix': '.csv'
    }
    filename1 = os.path.join(info['file'] + info['suffix'])

user = input("Enter a username to search for: ")
readDocument(filename1, info['path'], user)
