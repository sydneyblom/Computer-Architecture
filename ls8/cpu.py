"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
         # Add list properties to the `CPU` class to hold 256 bytes of memory and 8
        # general-purpose registers.

        # > Hint: you can make a list of a certain number of zeros with this syntax:
        # >
        # > ```python
        # > x = [0] * 25  # x is a list of 25 zeroes
        # > ```

        # Also add properties for any internal registers you need, e.g. `PC`.

        # Later on, you might do further initialization here, e.g. setting the initial
        # value of the stack pointer.
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0

    def load(self):
        """Load a program into memory."""
        address = 0
        # For now, we've just hardcoded a program:
        program = [
            # From print8.ls8
            0b10000010, # LDI R0,8
            0b00000000,
            0b00001000,
            0b01000111, # PRN R0
            0b00000000,
            0b00000001, # HLT
        ]
        for instruction in program:
            self.ram[address] = instruction
            address += 1
    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        else:
            raise Exception("Unsupported ALU operation")
    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """
        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')
        for i in range(8):
            print(" %02X" % self.reg[i], end='')
        print()
    def run(self):
        """Run the CPU."""
        self.load()
        # Needs to read the memory address that's stored in register `PC`, and store
        # that result in `IR`, the _Instruction Register_.
        # `IR`, contains a copy of the currently executing instruction
        while True:
            IR = self.ram[self.pc]
            # LDI
            if IR == LDI:
                # Read the bytes at `PC+1` and `PC+2` from RAM into variables `operand_a` and `operand_b`
                operand_a = self.ram[self.pc + 1]
                operand_b = self.ram[self.pc + 2]
                # store the data
                self.reg[operand_a] = operand_b
                # increment the PC by 3 to skip the arguments
                self.pc += 3
            # PRN
            elif IR == PRN:
                data = self.ram[self.pc + 1]
                # print
                print(self.reg[data])
                # increment the PC by 2 to skip the argument
                self.pc += 2
            # HLT
            elif IR == HLT:
                sys.exit(0)
            # else, print did not understand
            else:
                print(f"I did not understand that command: {IR}")
                sys.exit(1)