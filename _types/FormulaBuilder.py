from parser.PropositionalFormula import PropositionalFormula as PF
from _types.FormulaCollection import FormulaCollection

class FormulaBuilder:

    @staticmethod
    def __validate_formulas(formulas: list[str]) -> ValueError | None:
        for sentence in formulas:    
            if not PF.formula_is_valid(sentence):
                raise ValueError({'error': f'has an invalid formula {sentence}'})

    @staticmethod
    def build_marked_formulas(amount: int, formulas: list[str]) -> FormulaCollection | None:
        try:
            FormulaBuilder.__validate_formulas(formulas)
        except ValueError as e:
            print(e.args[0])
            return

        marked_formulas = FormulaCollection()
        for i in range(amount - 1):
            marked_formulas.add_formula(formulas[i], True)
        marked_formulas.add_formula(formulas[amount - 1], False)
        return marked_formulas