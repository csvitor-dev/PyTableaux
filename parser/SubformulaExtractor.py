from lark import Transformer
from utils.tokens import TOKEN_AND, TOKEN_IMPL, TOKEN_NEG, TOKEN_OR

class SubformulaExtractor(Transformer):
    """ A classe `SubFormulaExtractor`é usada para processar e transformar árvores sintáticas de fórmulas proposicionais, identificando os conectivos principais (como OR, AND, IMPL e NOT) e as subfórmulas imediatas. """
    def __init__(self):
        self.main_conective = None
        self.immediate_subformulas = None

    def or_(self, args):
        self.main_conective = TOKEN_OR
        self.immediate_subformulas = [args[0], args[1]]
        return f"({args[0]}{TOKEN_OR}{args[1]})"

    def and_(self, args):
        self.main_conective = TOKEN_AND
        self.immediate_subformulas = [args[0], args[1]]
        return f"({args[0]}{TOKEN_AND}{args[1]})"

    def impl_(self, args):
        self.main_conective = TOKEN_IMPL
        self.immediate_subformulas = [args[0], args[1]]
        return f"({args[0]}{TOKEN_IMPL}{args[1]})"

    def not_(self, args):
        self.main_conective = TOKEN_NEG
        self.immediate_subformulas = [args[0]]
        return f"{TOKEN_NEG}{args[0]}"

    def VAR(self, token):
        self.main_conective = "atom"
        self.immediate_subformulas = [token.value]
        return token.value

    def start(self, args):
        return args[0]