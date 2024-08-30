from _types.tokens import TOKEN_AND, TOKEN_IMPL, TOKEN_NEG, TOKEN_OR

class RulesExpander:
    
    def __init__(self) -> None:
        self.__alphas = {TOKEN_AND: True, TOKEN_OR: False, TOKEN_IMPL: False}
        self.__betas = {TOKEN_AND: False, TOKEN_OR: True, TOKEN_IMPL: True}

    def expand(self, marking: bool, operator: str, subformulas: list[str]) -> list[tuple[str, bool]]:
        if operator == TOKEN_NEG:
            return self.__reversing_polarity(marking, subformulas[0])
        ...

    def __reversing_polarity(self, marking: bool, formula: str) -> list[tuple[str, bool]]:
        return [(formula, not marking)]

    def __alpha_rule(self):
        ...
    
    def __beta_rule(self):
        ...