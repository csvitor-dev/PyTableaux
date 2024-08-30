from _types.FormulaCollection import FormulaCollection

class BranchsTree:
    
    def __init__(self, first_branch: FormulaCollection) -> None:
        self.__root = first_branch
        self.__left_branch = None
        self.__right_branch = None
    
    def add_branchs(self, beta1: FormulaCollection, beta2: FormulaCollection) -> None:
        self.__left_branch = BranchsTree(beta1)
        self.__right_branch = BranchsTree(beta2)

    def discard_closed_branch(self, branch_position: str) -> None:
        match branch_position:
            case 'left':
                self.__left_branch = None
            case 'right':
                self.__right_branch = None
            case _:
                print('nothing happened')
