# Import with sys.path.insert
import os
import sys
from contextlib import contextmanager


@contextmanager
def import_from(path):
    # A package importer that leaves no trace.
    # Say you want this function: package_path.xxx.yyy.zzz
    # with import_from(package_path):
    #     from xxx.yyy import zzz
    # zzz()
    try:
        abs_path = os.path.abspath(path)
        sys.path.insert(0, abs_path)
        yield
    finally:
        sys.path.pop(0)
