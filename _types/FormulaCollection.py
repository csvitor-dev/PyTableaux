class FormulaCollection:

    def __init__(self) -> None:
        self.__structure = {}
    
    @property
    def formulas(self) -> list[str]:
        return list(self.__structure.keys())
    
    @property
    def length(self) -> int:
        return len(self.__structure)

    def get_formulas(self) -> list[tuple[str, bool]]:
        return list(self.__structure.items())
    
    def add_formula(self, key_value_pair: tuple[str, bool]) -> None:
        self.__structure[key_value_pair[0]] = key_value_pair[1]

    def drop_formula(self, key: str) -> None:
        self.__structure.pop(key)
    
    def drop_all(self) -> None:
        self.__structure.clear()

    def contains(self, key: str) -> bool:
        return key in self.__structure.keys()