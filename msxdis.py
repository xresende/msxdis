# coding=utf-8
#
# msxdis - a MSX disassembler package
#
# Copyright (C) 2019 Ximenes R. Resende (xresende@gmail.com)
#   https://github.com/xresende/msxdis
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from z80dis import disassemble as _disassemble
from msxbiossymbols import msx1bios_calls as _msx1bios_calls
from msxbiossymbols import msx1bios_sysvars as _msx1bios_sysvars


class MSXDisassembler:
    """."""

    _TABSIZE = 4
    _COMMENTPOS = 30

    BIOS_SYMBOLS = dict()
    BIOS_SYMBOLS.update(_msx1bios_calls)
    BIOS_SYMBOLS.update(_msx1bios_sysvars)

    def __init__(self, use_symbols=True):
        """."""
        self._memory = None
        self._org = 0
        self._pc = 0
        self._rom_id = ''
        self._rom_init = ''
        self._rom_statement = ''
        self._rom_device = ''
        self._line_comments = dict()
        self._ins_comments = dict()
        self._symbols = dict()
        self._db_string = dict()
        self._db_bytes = list()
        self._db = list()
        self._dw = list()
        self._skip = list()
        self._use_symbols = use_symbols
        if use_symbols:
            self._symbols.update(MSXDisassembler.BIOS_SYMBOLS)
    
    @property
    def org(self):
        """."""
        return self._org

    @property
    def pc(self):
        """."""
        return self._pc
    
    @property
    def symbols(self):
        """."""
        return self._symbols

    @pc.setter
    def pc(self, value):
        """."""
        self._pc = value

    def load_rom(self, fname):
        """."""
        data = []
        with open(fname, 'rb') as fp:
            byte = fp.read(1)
            while byte:
                data.append(byte)
                byte = fp.read(1)
        data = [ord(b) for b in data]
        if data[0] != 0x41 or data[1] != 0x42:
            raise TypeError
        pc = (data[3] << 8) + data[2]
        if pc < 0x4000:
            org = 0x0000
        elif pc < 0x8000:
            org = 0x4000
        elif pc < 0xc000:
            org = 0x8000
        else:
            raise ValueError
        self._memory = bytearray(data)
        self._org = org
        self._pc = pc
        self._rom_id = 'AB'
        self._rom_init = '0x{:04X}'.format(pc)
        self._rom_statement = '0x{:04X}'.format((data[5] << 8) + data[4])
        self._rom_device = '0x{:04X}'.format((data[7] << 8) + data[6])
        self._rom_text = '0x{:04X}'.format((data[9] << 8) + data[8])
        self._rom_reserved = \
            '0x{:02X}{:02X},0x{:02X}{:02X},0x{:02X}{:02X}'.format(
                data[0x0b], data[0x0a], 
                data[0x0f], data[0x0d],
                data[0x0f], data[0x0e])
        self.add_symbol(pc, 'INIT', 'ROM entrypoint')

    def load_system_rom(self, fname):
        """."""
        data = []
        with open(fname, 'rb') as fp:
            byte = fp.read(1)
            while byte:
                data.append(byte)
                byte = fp.read(1)
        data = [ord(b) for b in data]
        self._memory = bytearray(data)
        self._org = 0
        self._pc = 0
        # self.add_symbol(self._pc, 'INIT')

    @property
    def memsize(self):
        return len(self._memory)

    def add_symbol(self, addr, symbol, comment=None):
        """."""
        addr = MSXDisassembler._conv_pc2addr(addr)
        self._symbols[addr] = dict(symbol=symbol, comment=comment)

    def add_db_string(self, addr, size=None, terminator=None):
        """."""
        addr = MSXDisassembler._conv_pc2addr(addr)
        self._db_string[addr] = dict(size=size, terminator=terminator)

    def add_db_bytes(self, addr):
        """Add address from which db gathers bytes until a symbol address is found."""
        addr = MSXDisassembler._conv_pc2addr(addr)
        self._db_bytes.append(addr)

    def add_db(self, addr_beg, addr_end=None):
        if isinstance(addr_beg, (list, tuple)):
            for addr_ in addr_beg:
                addr = MSXDisassembler._conv_pc2addr(addr_)
                self._db.append(addr)
        elif isinstance(addr_beg, str):
            self._db.append(addr_beg)
        else:
            if addr_end is None:
                addr_end = addr_beg
            for addr_ in range(addr_beg, addr_end+1):
                addr = MSXDisassembler._conv_pc2addr(addr_)
                self._db.append(addr)

    def add_dw(self, addr):
        addr = MSXDisassembler._conv_pc2addr(addr)
        self._dw.append(addr)

    def add_ins_comment(self, addr, comment):
        addr = MSXDisassembler._conv_pc2addr(addr)
        self._ins_comments[addr] = comment

    def add_line_comment(self, addr, comment):
        addr = MSXDisassembler._conv_pc2addr(addr)
        self._line_comments[addr] = comment

    def add_skip(self, addr):
        addr = MSXDisassembler._conv_pc2addr(addr)
        self._skip.append(addr)

    def print_rom_header(self, print_addr=True):
        """."""
        text = list()
        text.append('; ROM SIZE      :' + str(len(self._memory)))
        text.append('; ROM ID        :' + self._rom_id)
        text.append('; ROM INIT      :' + self._rom_init)
        text.append('; ROM STATEMENT :' + self._rom_statement)
        text.append('; ROM DEVICE    :' + self._rom_device)
        text.append('; ROM TEXT      :' + self._rom_text)
        text.append('; ROM RESERVED  :' + self._rom_reserved)
        text.append('')
        prefix = '      ' if print_addr else ''
        ins = prefix + 'org ' + MSXDisassembler._conv_pc2addr(self.org)
        line = self._add_symbols_comments(ins, None, None, '', True)
        text.append(line)
        text.append('')
        text.append('; --- ROM Header bytes ---')
        text.append('')

        pc0 = self.pc
        self.pc = self.org

        ins = 'db "AB"'
        pc = self.pc if print_addr else None
        line = self._add_symbols_comments(ins, pc, None, '', True)
        text.append(line)
        self.pc += 2
        
        ins = 'dw INIT'
        pc = self.pc if print_addr else None
        line = self._add_symbols_comments(ins, pc, None, '', True)
        text.append(line)
        self.pc += 2

        ins = 'dw {}'.format(self._rom_statement)
        pc = self.pc if print_addr else None
        line = self._add_symbols_comments(ins, pc, None, '', True)
        text.append(line)
        self.pc += 2

        ins = 'dw {}'.format(self._rom_device)
        pc = self.pc if print_addr else None
        line = self._add_symbols_comments(ins, pc, None, '', True)
        text.append(line)
        self.pc += 2

        ins = 'dw {}'.format(self._rom_text)
        pc = self.pc if print_addr else None
        line = self._add_symbols_comments(ins, pc, None, '', True)
        text.append(line)
        self.pc += 2

        ins = 'dw {}'.format(self._rom_reserved)
        pc = self.pc if print_addr else None
        line = self._add_symbols_comments(ins, pc, None, '', True)
        text.append(line)
        self.pc += 6

        text.append('')
        self.pc = pc0

        return text

    def load_symbols(self, fname):
        self._use_symbols = True
        with open(fname, 'r') as fp:
            data = fp.readlines()
        symbols = dict()
        for line in data:
            line = line.strip()
            line = line.replace('\t','')
            token, comment = line.split(';')
            comment = comment.lstrip().rstrip()
            if not token:
                continue  # comment line
            symbol, address = token.split('equ')
            symbol = symbol.replace(':','').replace(' ', '').upper()
            address = address.replace(' ', '')
            symbols[address] = dict(symbol=symbol, comment=comment)
        self._symbols.update(symbols)

    def disassemble(self, pc=None, lastpc=None, nrbytes=None, print_addr=True):
        """."""
        text = list()
        
        if isinstance(pc, str):
            for addr, symbol in self._symbols.items():
                if symbol['symbol'] == pc:
                    pc = int(addr, base=16)

        if isinstance(lastpc, str):
            for addr, symbol in self._symbols.items():
                if symbol['symbol'] == lastpc:
                    lastpc = int(addr, base=16)

        if pc is not None:
            self.pc = pc

        if nrbytes is None:
            nrbytes = self.memsize

        pc0 = self.pc
        while self.pc < self.org + self.memsize and self.pc - pc0 < nrbytes:
            
            if lastpc is not None and self.pc > lastpc:
                break

            # get address string from PC
            addr0 = MSXDisassembler._conv_pc2addr(self.pc)

            lines = []

            # line comments
            if addr0 in self._line_comments:
                comments = self._line_comments[addr0]
                space = ' ' * (6 if print_addr else 0) \
                    + ' ' * MSXDisassembler._TABSIZE
                if isinstance(comments, str):
                    lines.append('')
                    line = space + '; ' + comments
                    lines.append(line)
                    lines.append('')
                else:
                    lines.append('')
                    for comment in comments:
                        line = space + '; ' + comment
                        lines.append(line)
                    lines.append('')

            # generate instruction line
            line = self._add_symbols_comments(addr0, None, addr0, ':', False)

            # label lines
            if line != addr0:
                lines.append('')
                lines.append(line)
                lines.append('')

            if addr0 in self._db_bytes:
                # db bytes
                txt = 'db '
                pc2 = self.pc
                while self.pc - pc0 < nrbytes and self.pc < self.org + len(self._memory):
                    addr2 = MSXDisassembler._conv_pc2addr(self.pc)
                    if addr2 in self._symbols:
                        break
                    txt += '{:02X}h,'.format(self._memory[self.pc - self.org])
                    self.pc += 1
                    if len(txt) >= 4*32:
                        pc = pc2 if print_addr else None
                        line = self._add_symbols_comments(txt, pc, addr0, '', True)
                        line = line.rstrip(',')
                        text.append(line)
                        txt = 'db '
                        pc2 = self.pc
                if len(txt) > 3:
                    pc = pc2 if print_addr else None
                    line = self._add_symbols_comments(txt, pc, addr0, '', True)
                    line = line.rstrip(',')
            elif addr0 in self._db:
                # db 
                mem, pc = self._memory, self.pc
                data = mem[pc]
                word = '{:02X}h'.format(data)
                ins = 'db   ' + word
                pc = self.pc if print_addr else None
                line = self._add_symbols_comments(ins, pc, word, '', True)
                self.pc += 1
            elif addr0 in self._dw:
                # dw 
                mem, pc = self._memory, self.pc
                data = mem[pc] + (mem[pc+1] << 8)
                word = '0x{:04X}'.format(data)
                ins = 'dw   ' + word
                pc = self.pc if print_addr else None
                line = self._add_symbols_comments(ins, pc, word, '', True)
                self.pc += 2
            elif addr0 in self._db_string:
                # db string
                pc = self.pc if print_addr else None
                db = self._db_string[addr0]
                if db['size']:
                    line = self._add_symbols_comments('db ', pc, '', '', True)
                    
                elif db['terminator'] is not None:
                    tbyte = db['terminator']
                    line = self._add_symbols_comments('db ', pc, '', '', True)
                    
                    stxt = '' 
                    while self.pc - pc0 < nrbytes and self.pc < self.org + len(self._memory) and self._memory[self.pc - self.org] != tbyte:
                        byte = self._memory[self.pc - self.org]
                        if 32 <= byte <= byte <= 126:
                            stxt += chr(byte)
                        else:
                            if stxt:
                                line += '"' + stxt + '",'
                                stxt = ''
                            line += '{:02X}h,'.format(byte)
                        self.pc += 1
                    if self.pc < len(self._memory):
                        line += '{:02X}h,'.format(tbyte)
                    self.pc += 1
                line = line.rstrip(',')
            else:
                # instruction lines
                pc = self.pc if print_addr else None
                try:
                    ins, steps, addr = _disassemble(
                        self._memory, self.pc - self.org, self.org)
                except UnboundLocalError:
                    print('pc:0x{:04X} org:0x{:04X}'.format(self.pc, self.org))
                line = self._add_symbols_comments(ins, pc, addr, '', True)
    
                # add label
                if addr and addr not in self._symbols:
                    self.add_symbol(addr=addr, symbol=addr)
                self.pc += steps

            if addr0 in self._ins_comments:
                # print(addr0, self._ins_comments)
                ins = line.split(';')[0]
                spcs = ' ' * (MSXDisassembler._COMMENTPOS - len(ins))
                line = ins + spcs + ' ; ' + self._ins_comments[addr0]

            text += lines
            text.append(line)

        # print lines
        for line in text:
            print(line)

        return text

    def _add_symbols_comments(self, ins, pc, addr, char, tab_flag):
        prefix = ''
        pc_ = MSXDisassembler._conv_pc2addr(pc)
        if pc is not None:
            prefix += pc_ 
        if tab_flag:
            prefix += ' '*MSXDisassembler._TABSIZE
        symbols = self._symbols
        comt = ''
        ins_sym = ins
        if self._use_symbols and symbols and addr in symbols:
            symbol = symbols[addr]
            if pc_ not in self._skip:
                ins_sym = ins_sym.replace(addr, symbol['symbol'] + char)
            spcs = ' ' * (MSXDisassembler._COMMENTPOS - len(ins_sym) - len(prefix))
            if symbol['comment'] is not None and pc_ not in self._skip:
                comt = spcs + ' ; ' + symbol['comment']
        line = prefix + ins_sym
        if True:
            line += comt
        return line

    @staticmethod
    def _conv_pc2addr(addr):
        if isinstance(addr, int):
            return '0x{:04X}'.format(addr)
        else:
            return addr

    @staticmethod
    def print_code(code):
        for line in code:
            print(line)

