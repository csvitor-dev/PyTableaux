""" 

"""

import sys
from file_manipulation.FileManager import FileManager as FM

sys.path.append('..\\pyTableaux\\')

def main(args) -> None:
    print(args)
    """ build = FM()

    try:
        result = build.get_formulas_on_file()
    except FileNotFoundError as e:
        print(e.args[0])
        return
    print(result) """

if __name__ == "__main__":
    main(sys.args)
