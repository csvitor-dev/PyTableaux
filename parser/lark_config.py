from lark import Lark
from _types.tokens import TOKEN_AND, TOKEN_IMPL, TOKEN_NEG, TOKEN_OR

grammar = """
    start: expr

    ?expr: "("expr "{TOKEN_OR}" expr ")"  -> or_
          | "("expr "{TOKEN_AND}" expr ")"  -> and_
          | "("expr "{TOKEN_IMPL}" expr ")"  -> impl_
          | "{TOKEN_NEG}" expr  -> not_
          | VAR

    VAR: /[a-z]+[_0-9]*/

""".format(TOKEN_OR=TOKEN_OR, TOKEN_AND=TOKEN_AND, TOKEN_IMPL=TOKEN_IMPL, TOKEN_NEG=TOKEN_NEG)

parser = Lark(grammar, start='start')