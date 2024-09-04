from _types.FormulaCollection import FormulaCollection

class BranchsTree:
    
    def __init__(self, first_branch: FormulaCollection) -> None:
        self.root = first_branch
        self.new_branch = None
    
    @property
    def has_open_branch(self) -> bool:
        if self.root == None:
            return False
        if self.new_branch != None:
            return self.new_branch.has_open_branch
        return True

    def add_branch(self, beta: FormulaCollection, collection: FormulaCollection) -> None:
        hook = self.__search_branch(collection)
        hook.new_branch = BranchsTree(beta)

    def discard_closed_branch(self, collection: FormulaCollection) -> None:
        hook = self.__search_branch(collection)
        hook.root.drop_all()
        hook.root = None

    def add_formulas_on_branch(self, key_value_pair: tuple[str, bool], collection: FormulaCollection) -> None:
        hook = self.__search_branch(collection)
        hook.root.add_formula(key_value_pair)

    def remove_formula_on_branch(self, formula: str) -> None:
        if formula in self.root.formulas:
            self.root.drop_formula(formula)
            return
        if self.new_branch != None:
            self.new_branch.remove_formula_on_branch(formula)   

    def find_open_branch(self) -> FormulaCollection:
        if self.new_branch == None:
            return self.root
        return self.new_branch.find_open_branch()
    
    def __search_branch(self, collection: FormulaCollection):
        if self.root.formulas == collection.formulas:
            return self
        if self.new_branch != None:
            return self.new_branch.__search_branch(collection)
