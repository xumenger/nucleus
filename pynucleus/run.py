import pynucleus.librarys

from pynucleus.chars_in_file import chars_in_file
from pynucleus.env import Env
from pynucleus.eval_ import eval_list
from pynucleus.lexer import lex
from pynucleus.parser import parse


def run(filename, stdin, stdout, stderr):
    env = Env(stdin = stdin, stdout = stdout, stderr = stderr)
    pynucleus.librarys.import_(env)
    with open(filename, encoding = "ascii") as f:
        eval_list(parse(lex(chars_in_file(f))), env)
