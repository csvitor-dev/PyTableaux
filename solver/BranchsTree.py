from utils.Branch import Branch

class BranchsTree:
    
    def __init__(self, first_branch: Branch) -> None:
        self.root = first_branch
        self.right_branch: BranchsTree = None
        self.left_branch: BranchsTree = None
    
    @property
    def has_open_branch(self) -> bool:
        if self.right_branch != None:
            return self.right_branch.has_open_branch
        if self.left_branch != None:
            return self.left_branch.has_open_branch
        if self.root == None:
            return False
        return True

    def add_branch(self, beta: Branch, collection: Branch) -> None:
        hook = self.__search_branch(collection)

        if hook.right_branch == None:
            hook.right_branch = BranchsTree(beta)
        elif hook.left_branch == None:
            hook.left_branch = BranchsTree(beta)
        elif hook.right_branch.root != None:
            self.right_branch.add_branch(beta, hook.right_branch.root)
        elif hook.left_branch.root != None:
            self.left_branch.add_branch(beta, hook.left_branch.root)

    def discard_closed_branch(self, collection: Branch) -> None:
        hook = self.__search_branch(collection)
        hook.root.drop_all()
        hook.root = None

    def add_formulas_on_branch(self, key_value_pair: tuple[str, bool], collection: Branch) -> None:
        hook = self.__search_branch(collection)
        hook.root.add_formula(key_value_pair)

    def remove_formula_on_branch(self, formula: str) -> None:
        if formula in self.root.formulas:
            self.root.drop_formula(formula)
            return
        
        if self.right_branch != None:
            self.right_branch.remove_formula_on_branch(formula)   
        elif self.left_branch != None:
            self.left_branch.remove_formula_on_branch(formula)

    def find_open_branch(self) -> Branch:
        if self.right_branch != None:
            return self.right_branch.find_open_branch()
        if self.left_branch != None:
            return self.left_branch.find_open_branch()
        return self.root
    
    def __search_branch(self, collection: Branch):
        if self.root == None:
            return
        
        if self.root.marked_formulas == collection.marked_formulas:
            return self
        if self.right_branch.root != None:
            return self.right_branch.__search_branch(collection)
        if self.left_branch.root != None:
            return self.left_branch.__search_branch(collection)
