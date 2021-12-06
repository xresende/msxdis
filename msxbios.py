#!/usr/bin/python3

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


from msxdis import MSXDisassembler


def msxbios_begin(rom, beg, end):
    """."""
    rom.add_line_comment(addr=beg, comment=[
        'MSX BIOS',
        '========',
        '',
        '. Symbol table by MSX.BIOS by ASCII Corp., 1983 (v3.44)',
        '',
        '    file       : BIOHDR.MAC',
        '    use        : Restart calls and ROM entries table',
        '    written by : Jey Suzuki, Rick Yamashita',
        '                 ASCII Corporation, Japan',
        '',
        '    edit       : January, 1985',
        '    reason     : Zilog Z80 Mneumonic version and cleanup',
        '    edited by  : Steven M. Ting',
        '',
        '. Disassembled by Ximenes R. Resende (xresende@gmail.com)',
        '    file       : EXPERT10.ROM',
        '',
        ])
    rom.add_line_comment(0x0006, comment=[
        '** VDP Information **',
        'Any program that access the VDP hardware directly',
        'should read the I/O port address found here, to be certain',
        'the software is compatible with future versions of the VDP',
        ])

    rom.add_ins_comment(addr=0x0000, comment='Fail safe')
    rom.add_ins_comment(addr=0x0001, comment='Find all connected RAM')
    rom.add_ins_comment(addr=0x0006, comment='Port address for VDP data read')
    rom.add_ins_comment(addr=0x0007, comment='Port address for VDP data write')
    rom.add_dw(0x0004)
    rom.add_db([
        0x0006, 0x0007, 0x000B, 0x000F, 0x0013, 
        0x0017, 0x001B, 0x001F, 0x0023, 0x0027])    
    rom.add_db(0x002B, 0x002F)
    rom.add_db(0x0033, 0x0037)
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_ioinij(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'Following are used for I/O initializations',
        '',
        ])
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_vdprmc(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'The following entry points provide control of the ',
        'VDP\'s registers, screen mode settings, and memory block',
        'move between DRAM and VRAM.',
        ])
    rom.add_db(0x0065)
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_psgini(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'The following entry points are used for PSG initialization, ',
        'read and write PSG registers, and PLAY statement execution.',
        ])
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_inpprt(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'General INPUT and PRINT utilities.',
        '',
        ])
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_joystk(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'General INPUT and PRINT utilities.',
        '',
        ])
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_tapect(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'Following are used to access the cassette tape, ',
        'data read/write, and motor on/off',
        '',
        ])
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_basicq(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'BASIC queues',
        '',
        ])
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_basgrp(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'For BASIC interpreter\'s GENGRP and ADVGRP modules use',
        '',
        ])
    rom.add_ins_comment(addr=0x015C, comment='RESERVED FOR EXPANSION - start')
    rom.add_ins_comment(addr=0x01B5, comment='RESERVED FOR EXPANSION - end')
    rom.add_db(0x015C, 0x01B5)
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios_slotsm(rom, beg, end):

    rom.add_line_comment(addr=beg, comment=[
        '',
        'SLOTS',
        '',
        'Every cartridge located at 0000-3FFFH must contain codes in',
        'this module which are entered via following addresses.',
        '',
        '   0x000C RDSLT',
        '   0x0014 WRSLT',
        '   0x001C CALSLT',
        '   0x0024 ENASLT',
        '',
        '===== RDSLT =====',
        '',
        'Select the appropriate slot according to the value given',
        'through registers, and read the content of memory from the',
        'slot.',
        '',
        'Input parameters:',
        '',
        '  A - FxxxSSPP',
        '      |   ||||',
        '      |   ||++-- primary slot # (0-3)',
        '      |   ++---- secondary slot # (0-3)',
        '      +--------- 1 if secondary slot # specified',
        '',
        '  HL - address of target memory',
        '',
        'Returned value',
        '',
        '  A - content of memory',
        '',
        'Note: Interrupts are disabled automatically but never enabled',
        '      by this routine.',
        '',
        ])
    rom.disassemble(pc=beg, lastpc=end, nrbytes=None, print_addr=True)


def msxbios():
    """MSX BIOS Disassembler."""
    rom = MSXDisassembler()

    rom.load_system_rom('./EXPERT10.ROM')

    msxbios_begin(rom,  0x0000, 0x0037)
    msxbios_ioinij(rom, 0x0038, 0x003E)
    msxbios_vdprmc(rom, 0x0041, 0x008F)
    msxbios_psgini(rom, 0x0090, 0x009b)
    msxbios_inpprt(rom, 0x009C, 0x00D4)
    msxbios_joystk(rom, 0x00D5, 0x00E0)
    msxbios_tapect(rom, 0x00E1, 0x00F5)
    msxbios_basicq(rom, 0x00F6, 0x00FB)
    msxbios_basgrp(rom, 0x00FC, 0x01B5)
    msxbios_slotsm(rom, 0x01B6, 0x02D6)

    # --- BEGIN ---
    
    
    # rom.disassemble(pc=0x0000, lastpc=0x008D, nrbytes=None, print_addr=True)

    # rom.add_ins_comment(addr=0x01B6, comment='Calculate bit pattern and mask code')

    # rom.disassemble(pc='RDSLT', lastpc=0x01C5, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='RDESLT', lastpc=0x01CF, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='WRSLT', lastpc=0x01DE, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='WRESLT', lastpc=0x01E9, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='WRESED', lastpc=0x01FE, nrbytes=None, print_addr=True)
    
    # rom.disassemble(pc='CALBAS', lastpc=0x0203, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='CALLF', lastpc=0x025D, nrbytes=None, print_addr=True)

    # rom.disassemble(pc='ENASLT', lastpc=0x026A, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='ENESLT', lastpc=0x027C, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='SELPRM', lastpc=0x02A2, nrbytes=None, print_addr=True)
    # rom.disassemble(pc='SELEXP', lastpc=0x02D6, nrbytes=None, print_addr=True)

    # rom.add_skip('0x033B') # avoid replacing 0x0000 <-> _CHKRAM
    # rom.add_skip('0x039E') # avoid replacing 0x0000 <-> _CHKRAM
    # rom.disassemble(pc='CHKRAM', lastpc=0x03F8, nrbytes=None, print_addr=True)

    
if __name__ == "__main__":
    msxbios()


