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

    def add_branchs(self, beta: FormulaCollection) -> None:
        self.new_branch = BranchsTree(beta)

    def discard_closed_branch(self) -> None:
        self.new_branch.root.drop_all()
        self.new_branch = None

    def add_formulas_on_root(self, key_value_pair: tuple[str, bool]) -> None:
        self.root.add_formula(key_value_pair)
