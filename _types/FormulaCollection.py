class FormulaCollection:

    def __init__(self) -> None:
        self.__structure = dict()

    @property
    def formulas(self) -> dict[str: bool]:
        return self.__structure

    def get_formulas(self) -> list[tuple[str, bool]]:
        return list(self.__structure.items())
    
    def add_formula(self, key_value_pair: tuple[str, bool]) -> None:
        self.__structure[key_value_pair[0]] = key_value_pair[1]

    def drop_formula(self, key: str) -> bool:
        return self.__structure.pop(key)
    