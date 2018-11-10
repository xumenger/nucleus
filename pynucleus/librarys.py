from pynucleus.lexer import lex
from pynucleus.parser import parse
from pynucleus.eval_ import eval_list

import pynucleus.library.native.char_at
import pynucleus.library.native.concat
import pynucleus.library.native.equals
import pynucleus.library.native.if_
import pynucleus.library.native.len_
import pynucleus.library.native.print_
import pynucleus.library.native.set_

import pynucleus.library.nucleus.not_
import pynucleus.library.nucleus.chars_in
import pynucleus.library.nucleus.pairs
import pynucleus.library.nucleus.lists


def import_(env):
    env.set("char_at", ("native", pynucleus.library.native.char_at.char_at))
    env.set("concat",  ("native", pynucleus.library.native.concat.concat))
    env.set("equals",  ("native", pynucleus.library.native.equals.equals))
    env.set("if",      ("native", pynucleus.library.native.if_.if_))
    env.set("len",     ("native", pynucleus.library.native.len_.len_))
    env.set("print",   ("native", pynucleus.library.native.print_.print_))
    env.set("set",     ("native", pynucleus.library.native.set_.set_))
    env.set("None",    ("none",))

    eval_list(parse(lex(as_text(env))), env)


def as_text(env):
    str = pynucleus.library.nucleus.not_.not_
    str += pynucleus.library.nucleus.chars_in.chars_in
    str += pynucleus.library.nucleus.pairs.pairs
    str += pynucleus.library.nucleus.lists.lists

    return str

