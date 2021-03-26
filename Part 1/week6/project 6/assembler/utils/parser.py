# -*- coding: utf-8 -*-
"""
Instruction parser for Hack assembler
"""


class Parser:
    def __init__(self, input_file):
        '''Opens the input file/stream and gets ready to parse it'''

        self.input = open(input_file, 'r')
        self.current_index = 0
    # end def

    def has_more_commands(self) -> bool:
        '''Are there more commands in the input?'''

        self.next_line = self.input.readline()
        if self.next_line:
            return True
        else:
            return False
        # end if
    # end def

    def advance(self):
        '''Reads the next command from the input and makes it the current command. 
            Should be called only if hasMoreCommands() is true.
            Initially there is no current command'''

        # ignoring whitespace and comment
        command = self.next_line.split('/')[0].replace(' ', '')
        self.current_command = command
        return command
    # end def

    def command_type(self) -> str:
        '''Returns the type of the current command:
            1. A_COMMAND for @Xxx where Xxx is either a symbol or a decimal number
            2. C_COMMAND for dest=comp;jump
            3. L_COMMAND (actually, pseudocommand) for (Xxx) where Xxx is a symbol'''
        command = self.current_command
        if len(command) == 0:
            return 'NO_COMMAND'
        # end if
        if command[0] == '@':
            return 'A_COMMAND'
        elif command[0] == '(':
            return 'L_COMMAND'
        elif command[0] in 'ADMJ01-!':
            return 'C_COMMAND'
        else:
            return 'NO_COMMAND'
        # end if
    # end def

    def symbol(self) -> str:
        '''Returns the symbol or decimal Xxx of the current command @Xxx or (Xxx). 
            Should be called only when commandType() is A_COMMAND or L_COMMAND'''

        if self.current_command[0] == '(':
            command = self.current_command.split(')')[0]
            return command[1:].strip()
        else:
            return self.current_command[1:].strip()
        # end if
    # end def

    def dest(self) -> str:
        '''Returns the dest mnemonic in the current C-command (8 possibilities). 
            Should be called only when commandType() is C_COMMAND'''

        if '=' not in self.current_command:
            return None
        else:
            return self.current_command.split('=')[0].strip()
        # end if
    # end def

    def comp(self) -> str:
        '''Returns the comp mnemonic in the current C-command (28 possibilities). 
            Should be called only when commandType() is C_COMMAND'''

        command = self.current_command
        if '=' in command:
            command = command.split('=')[1]
        # end if
        if ';' in command:
            command = command.split(';')[0]
        # end if
        return command.strip()
    # end def

    def jump(self) -> str:
        '''Returns the jump mnemonic in the current C-command (8 possibilities). 
            Should be called only when commandType() is C_COMMAND'''

        if ';' not in self.current_command:
            return None
        else:
            return self.current_command.split(';')[1].strip()
        # end if
    # end def
# end class
