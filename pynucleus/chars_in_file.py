from pynucleus.assert_implements import assert_implements
from pynucleus.readable import Readable

def chars_in_file(f):
    assert_implements(f, Readable)
    ch = f.read(1)
    while ch != "":
        yield ch
        ch = f.read(1)
