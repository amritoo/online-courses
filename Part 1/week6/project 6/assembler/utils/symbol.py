# -*- coding: utf-8 -*-
"""
Mapping of (symbol, address) for Hack assembler
"""


class SymbolTable:
    def __init__(self):
        '''Creates a symbol table containing default symbols'''

        self.map = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'R0': 0,
            'R1': 1,
            'R2': 2,
            'R3': 3,
            'R4': 4,
            'R5': 5,
            'R6': 6,
            'R7': 7,
            'R8': 8,
            'R9': 9,
            'R10': 10,
            'R11': 11,
            'R12': 12,
            'R13': 13,
            'R14': 14,
            'R15': 15,
            'SCREEN': 16384,
            'KBD': 24576
        }
    # end def

    def add_entry(self, symbol, address):
        '''Adds the pair (symbol, address) to the table'''

        self.map[symbol] = address
    # end def

    def contains(self, symbol) -> bool:
        '''Returns True if the symbol table contains the given symbol,
            False otherwise'''

        if self.map.get(symbol) is None:
            return False
        else:
            return True
        # end if
    # end def

    def get_address(self, symbol) -> int:
        '''Returns the address associated with the symbol'''

        return self.map.get(symbol)
    # end def
# end class
