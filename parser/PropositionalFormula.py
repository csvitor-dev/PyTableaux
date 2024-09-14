
from parser.lark_config import parser
from parser.SubformulaExtractor import SubformulaExtractor

class PropositionalFormula:
    """ Classe `PropositionalFormula` tem o proposito de verificar se a fórmula é valida ou não, se a fórmula for valida ele retorna a fórmula e obtém o conectivo principal e suas subfórmulas.  """
    @staticmethod 
    def __get_parsed_formula(formula: str):
        try:
          parse_tree = parser.parse(formula)
        except:
          return
        return parse_tree
    
    @staticmethod
    def formula_is_valid(formula: str) -> bool:
       return PropositionalFormula.__get_parsed_formula(formula) != None

    @staticmethod
    def get_main_conective_and_immediate_subformulas(formula: str):
      parse_tree = PropositionalFormula.__get_parsed_formula(formula)
      if parse_tree is None:
        return None, None
      extractor = SubformulaExtractor()
      extractor.transform(parse_tree)
      return extractor.main_conective, extractor.immediate_subformulas