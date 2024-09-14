from utils.Branch import Branch

class BranchsTree:
    '''
    Classe para executar a busca por profundidade.
    :
    A classe faz buscas de possíveis ramos abertos, adição de ramos, assim como as fórmulas que geram esses 
    novos ramos e a remoções dessas fórmulas em casos de um ramo fechado.
    '''
    
    def __init__(self, first_branch: Branch) -> None:
        self.root = first_branch
        self.__expandable_branch = True
        self.right_branch: BranchsTree = None
        self.left_branch: BranchsTree = None
    
    @property
    def has_open_branch(self) -> bool:
        if self.right_branch is not None:
            if self.right_branch.has_open_branch:
                return True
            
        if self.left_branch is not None:
            if self.left_branch.has_open_branch:
                return True
        
        return self.root is not None and self.__expandable_branch

    def add_branch(self, beta: Branch, collection: Branch) -> None:
        hook = self.__search_branch(collection)
        hook.__expandable_branch = False

        if hook.right_branch is None:
            hook.right_branch = BranchsTree(beta)
        elif hook.left_branch is None:
            hook.left_branch = BranchsTree(beta)
        else:
            hook.right_branch.add_branch(beta, hook.right_branch.root)
            hook.left_branch.add_branch(beta, hook.left_branch.root)

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
        
        if self.right_branch is not None:
            self.right_branch.remove_formula_on_branch(formula)   
        
        if self.left_branch is not None:
            self.left_branch.remove_formula_on_branch(formula)

    def find_open_branch(self) -> Branch | None:
        if self.right_branch is not None:
            right_open_branch = self.right_branch.find_open_branch()
            if right_open_branch is not None:
                return right_open_branch
        
        if self.left_branch is not None:
            left_open_branch = self.left_branch.find_open_branch()
            if left_open_branch is not None:
                return left_open_branch
        
        if self.root is not None and self.__expandable_branch:
            return self.root
        return None
    
    def __search_branch(self, collection: Branch):
        if self.root is None:
            return
        
        if self.root.marked_formulas == collection.marked_formulas:
            return self
        
        if self.right_branch is not None:
            right_result = self.right_branch.__search_branch(collection)
            if right_result is not None:
                return right_result
        
        if self.left_branch is not None:
            left_result = self.left_branch.__search_branch(collection)
            if left_result is not None:
                return left_result
