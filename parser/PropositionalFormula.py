from parser.lark_config import parser
from parser.SubformulaExtractor import SubformulaExtractor

class PropositionalFormula:
    @staticmethod
    def _get_parsed_formula(formula):
        try:
          parse_tree = parser.parse(formula)
        except:
          return
        return parse_tree

    @staticmethod
    def get_main_conective_and_immediate_subformulas(formula):
      parse_tree = PropositionalFormula._get_parsed_formula(formula)
      if parse_tree is None:
        return None, None
      extractor = SubformulaExtractor()
      extractor.transform(parse_tree)
      return extractor.main_conective, extractor.immediate_subformulas