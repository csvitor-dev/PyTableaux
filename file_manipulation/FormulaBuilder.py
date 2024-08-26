class FormulaBuilder:
    @staticmethod
    def build_marked_formulas(amount: int, formulas: list[str]) -> dict[str: bool]:
        marked_formulas = dict()
        for i in range(amount - 1):
            marked_formulas[formulas[i]] = True
        marked_formulas[formulas[amount - 1]] = False
        return marked_formulas