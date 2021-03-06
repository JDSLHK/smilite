# Copyright 2014-2020 Sebastian Raschka
#
# Retrieves the SMILE string and simplified SMILE string for a given ZINC ID
# from a previously built smilite SQLite database
# or from the online ZINC database.
#
#
# Usage:
# [shell]>> python3 lookup_single_id.py ZINC_ID [sqlite_file]
#
# Example 1 (retrieve data from a smilite SQLite database):
# [shell]>> python3 lookup_single_id.py
#  ZINC01234567 \
#  ~/Desktop/smilite_db.sqlite
#
# Example 2 (retrieve data from the ZINC online database):
# [shell]>> python3 lookup_single_id.py ZINC01234567
#
#
#
# Output example:
# ZINC01234567
# C[C@H]1CCCC[NH+]1CC#CC(c2ccccc2)(c3ccccc3)O
# CC1CCCCN1CCCC(C2CCCCC2)(C3CCCCC3)O
#
#     Where
#     1st row: ZINC ID
#     2nd row: SMILE string
#     3rd row: simplified SMILE string
#

import smilite
import sys


def print_usage():
    print('\nUSAGE: python3 lookup_single_id.py ZINC_ID [sqlite_file]')
    print('\n\nEXAMPLE1 (retrieve data from a smilite SQLite database):\n'
          'python3 lookup_single_id.py ZINC01234567 '
          '~/Desktop/smilite_db.sqlite')
    print('\n\nEXAMPLE2 (retrieve data from the ZINC online database):\n'
          'python3 lookup_single_id.py ZINC01234567\n')


smile_str = ''
simple_smile_str = ''

try:
    zinc_id = sys.argv[1]

    if len(sys.argv) > 2:
        sqlite_file = sys.argv[2]
        lookup_result = smilite.lookup_id_sqlite(sqlite_file, zinc_id)
        try:
            smile_str, simple_smile_str = lookup_result[1], lookup_result[2]
        except IndexError:
            pass

    else:
        smile_str = smilite.get_zinc_smile(zinc_id)
        if smile_str:
            simple_smile_str = smilite.simplify_smile(smile_str)

    print('{}\n{}\n{}'.format(zinc_id, smile_str, simple_smile_str))

except IOError as err:
    print('\n\nERROR: {}'.format(err))
    print_usage()

except IndexError:
    print('\n\nERROR: Invalid command line arguments.')
    print_usage()
