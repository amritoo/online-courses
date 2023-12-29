# -*- coding: utf-8 -*-
"""
Assembler for Hack assembly language.
"""
from utils.parser import Parser
from utils.symbol import SymbolTable
from utils.code import Code


def main():
    '''Main code'''

    # getting code file path and initializing objects
    input_file = input('Path to code file: ')
    parser = Parser(input_file)
    symbol_table = SymbolTable()
    code = Code()
    instructions = []
    remaining = []

    # converting C instructions
    while parser.has_more_commands():
        parser.advance()
        type = parser.command_type()

        if type == 'A_COMMAND':
            v = parser.symbol()
            try:
                v = int(v)
            except:
                pass
            # end try

            # print(v, isinstance(v, int))
            if isinstance(v, int):
                inst = '0' + code.binary(v)
                instructions.append(inst)
            elif symbol_table.contains(v) or isinstance(v, int):
                inst = '0' + code.binary(symbol_table.get_address(v))
                instructions.append(inst)
            else:
                instructions.append(v)
                # adding current index to remaining
                remaining.append(len(instructions) - 1)
            # end if
        elif type == 'C_COMMAND':
            c = code.comp(parser.comp())
            d = code.dest(parser.dest())
            j = code.jump(parser.jump())
            # print(c, d, j)
            inst = '111' + c + d + j
            instructions.append(inst)
        elif type == 'L_COMMAND':
            symbol_table.add_entry(parser.symbol(), len(instructions))
        # end if
    # end while

    # Converting A instruction
    last_var = 16
    for index in remaining:
        v = instructions[index]
        if not symbol_table.contains(v):
            symbol_table.add_entry(v, last_var)
            last_var += 1
        # end if
        inst = '0' + code.binary(symbol_table.get_address(v))
        instructions[index] = inst
    # end for

    # write to output file
    output_file = input_file.replace('.asm', '.hack')
    print('output file path:', output_file)
    with open(output_file, 'w') as file:
        for inst in instructions:
            file.write(inst + '\n')
        # end for
        file.close()
    # end with
# end def


main()
