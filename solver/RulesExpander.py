from _types.tokens import TOKEN_AND, TOKEN_IMPL, TOKEN_NEG, TOKEN_OR

class RulesExpander:
    
    def __init__(self) -> None:
        self.__alphas = {TOKEN_AND: (True, True), TOKEN_OR: (False, False), TOKEN_IMPL: (True, False)}
        self.__betas = {TOKEN_AND: (False, False), TOKEN_OR: (True, True), TOKEN_IMPL: (False, True)}

    def expand(self, marking: bool, operator: str, subformulas: list[str]) -> tuple[list[tuple[str, bool]], str]:
        if operator == TOKEN_NEG:
            return self.__reversing_polarity(marking, subformulas[0])
        
        match operator:
            case "&":
                if marking:
                    return self.__alpha_rule(self.__alphas[TOKEN_AND], subformulas[0], subformulas[1])
                return self.__beta_rule(self.__betas[TOKEN_AND], subformulas[0], subformulas[1])
            case "|":
                if not marking:
                    return self.__alpha_rule(self.__alphas[TOKEN_OR], subformulas[0], subformulas[1])
                return self.__beta_rule(self.__betas[TOKEN_OR], subformulas[0], subformulas[1])
            case "->":
                if not marking:
                    return self.__alpha_rule(self.__alphas[TOKEN_IMPL], subformulas[0], subformulas[1])
                return self.__beta_rule(self.__betas[TOKEN_IMPL], subformulas[0], subformulas[1])

    def __reversing_polarity(self, marking: bool, alpha: str) -> tuple[list[tuple[str, bool]], str]:
        return [(alpha, not marking)], "alpha"

    def __alpha_rule(self, markings: tuple[bool], alpha1: str, alpha2: str) -> tuple[list[tuple[str, bool]], str]:
        return [(alpha1, markings[0]), (alpha2, markings[1])], "alpha"
    
    def __beta_rule(self, markings: tuple[bool], beta1: str, beta2: str) -> tuple[list[tuple[str, bool]], str]:
        return [(beta1, markings[0]), (beta2, markings[1])], "beta"