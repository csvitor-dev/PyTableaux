class FormulaCollection:

    def __init__(self, key_value_pair: tuple[str: bool] = None) -> None:
        self.__structure = self.init(key_value_pair)
    
    def init(self, key_value_pair: tuple[str: bool] | None) -> dict:
        if key_value_pair:
            return {key_value_pair[0]: key_value_pair[1]}
        return {}

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

    def value(self, key: str) -> bool:
        return self.__structure[key]

    def contains(self, key: str) -> bool:
        return key in self.__structure.keys()