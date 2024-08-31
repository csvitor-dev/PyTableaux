from _types.FormulaCollection import FormulaCollection

class BranchsTree:
    
    def __init__(self, first_branch: FormulaCollection) -> None:
        self.__root = first_branch
        self.__new_branch = None
    
    @property
    def root(self) -> FormulaCollection:
        return self.__root

    def add_branchs(self, beta: FormulaCollection) -> None:
        self.__new_branch = BranchsTree(beta)

    def discard_closed_branch(self) -> None:
        self.__new_branch.__root.drop_all()
        self.__new_branch = None

    def add_formulas_on_root(self, key_value_pair: tuple[str, bool]) -> None:
        self.__root.add_formula(key_value_pair)
