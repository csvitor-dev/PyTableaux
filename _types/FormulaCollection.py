class FormulaCollection:

    def __init__(self) -> None:
        self.__structure = dict()
    
    def add_formula(self, key: str, value: bool) -> None:
        self.__structure[key] = value

    def get_formulas(self):
        return self.__structure.keys()
    