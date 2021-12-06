# coding=utf-8
#
# msxdis - a MSX disassembler package
#
# Copyright (C) 2019 Ximenes R. Resende
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


msx1bios_calls = {
    
    '0x0000': dict(symbol='BEGIN',  comment='MSX System Init'),

    '0x01B6': dict(symbol='RDSLT',  comment=None),
    '0x01C6': dict(symbol='RDESLT', comment=None), 
    '0x01D1': dict(symbol='WRSLT',  comment=None),
    '0x01E1': dict(symbol='WRESLT',  comment=None),
    '0x01EC': dict(symbol='WRESED',  comment=None),
    '0x01FF': dict(symbol='CALBAS',  comment=None),
    '0x0205': dict(symbol='CALLF',  comment=None),
    '0x0217': dict(symbol='CALSLT',  comment=None),
    '0x022E': dict(symbol='CALESL',  comment=None),
    '0x022E': dict(symbol='CALESL',  comment=None),
    '0x025E': dict(symbol='ENASLT',  comment=None),
    '0x026B': dict(symbol='ENESLT',  comment=None),
    '0x027E': dict(symbol='SELPRM', comment=None), 
    '0x0288': dict(symbol='SLPRM1', comment=None), 
    '0x0299': dict(symbol='SLPRM2', comment=None), 
    '0x02A3': dict(symbol='SELEXP',  comment=None),
    '0x02BB': dict(symbol='SLEXP1',  comment=None),
    
    '0x02D7': dict(symbol='CHKRAM', comment=None),
    '0x02E7': dict(symbol='CKRM05', comment=None),
    '0x02FF': dict(symbol='CKRM10', comment=None),
    '0x0302': dict(symbol='CKRM15', comment=None),
    '0x0305': dict(symbol='CKRM20', comment=None),
    '0x0314': dict(symbol='CKRM25', comment=None),
    '0x0327': dict(symbol='CKRM30', comment=None),
    '0x0335': dict(symbol='CKRM35', comment=None),
    '0x0353': dict(symbol='CKRM50', comment=None),
    '0x0362': dict(symbol='CKRM55', comment=None),
    '0x0365': dict(symbol='CKRM60', comment=None),
    '0x0368': dict(symbol='CKRM65', comment=None),
    '0x0379': dict(symbol='CKRM70', comment=None),
    '0x038C': dict(symbol='CKRM75', comment=None),
    '0x0398': dict(symbol='CKRM80', comment=None),

    '0x049D': dict(symbol='INITIO', comment='Device initialization'),
    '0x0570': dict(symbol='ENASCR', comment='Enable screen display'),
    '0x0577': dict(symbol='DISSCR', comment='Disable screen display'),
    '0x057F': dict(symbol='ENASCR', comment='Write a byte to any VDP register'),
    '0x070F': dict(symbol='LDIRMV', comment='Move block of data from VRAM to memory'),
    '0x0744': dict(symbol='LDIRVM', comment='Move block of data from memory to VRAM'),
    '0x07CD': dict(symbol='WRTVRM', comment='Write VRAM address using [HL]'),
    '0x07D7': dict(symbol='RDVRM',  comment='Read VRAM address using [HL]'),
    '0x07DF': dict(symbol='SETWRT', comment='Set up VDP for write'),
    '0x07EC': dict(symbol='SETRD',  comment='Set up VDP for read'),
    '0x07F7': dict(symbol='CHGCLR', comment='Change fg, bg and border colors'),
    '0x0815': dict(symbol='FILVRM', comment='Fill VRAM with specified data'),
    '0x084F': dict(symbol='CHGMOD', comment='Change screen mode of VDP to [SCRMOD]'),
    '0x0C3C': dict(symbol='KEYINT', comment='Handlers for hardware interrupt'),
    '0x139D': dict(symbol='INIFNK', comment='Reset all function key\'s text'),
    
    
    # '0x0008': dict(symbol='_SYNCHR', comment=None),
    # '0x000C': dict(symbol='_RDSLT',  comment=None),
    # '0x0010': dict(symbol='_CHRGTR', comment=None),
    # '0x0014': dict(symbol='_WRSLT',  comment=None),
    # '0x0018': dict(symbol='_OUTDO',  comment=None),
    # '0x001C': dict(symbol='_CALSLT', comment=None),
    # '0x0020': dict(symbol='_DCOMPR', comment=None),
    # '0x0024': dict(symbol='_ENASLT', comment=None),
    # '0x0028': dict(symbol='_GETYPR', comment=None),
    # '0x0030': dict(symbol='_CALLF',  comment=None),
    # '0x0038': dict(symbol='_KEYINT', comment=None),
    # '0x003B': dict(symbol='_INITIO', comment=None),
    # '0x003E': dict(symbol='_INIFNK', comment='Inicializa strings das teclas de função'),
    # '0x0041': dict(symbol='_DISSCR', comment='Desativa tela'),
    # '0x0044': dict(symbol='_ENASCR', comment='Ativa tela'),
    # '0x0047': dict(symbol='_WRTVDP', comment='Escreve em registrador do VDP'),
    # '0x004A': dict(symbol='_RDVRM',  comment='Lê byte da VRAM'),
    # '0x004D': dict(symbol='_WRTVRM', comment='Escreve byte na VRAM'),
    # '0x0050': dict(symbol='_SETRD',  comment='Prepara VDP para leitura'),
    # '0x0053': dict(symbol='_SETWRT', comment='Prepara VDP para escrita'),
    # '0x0056': dict(symbol='_FILVRM', comment='Preenche bloco da VRAM'),
    # '0x0059': dict(symbol='_LDIRMV', comment='Copia bloco da VRAM para a RAM'),
    # '0x005C': dict(symbol='_LDIRVM', comment='Copia bloco da RAM para a VRAM'),
    # '0x005F': dict(symbol='_CHGMOD', comment='Altera modo do VDP'),
    # '0x0062': dict(symbol='_CHGCLR', comment='Altera cores do VDP'),
    # '0x0066': dict(symbol='_NMI',    comment='Manipulador da NMI'),
    # '0x0069': dict(symbol='_CLRSPR', comment='Limpa todos os sprites'),
    # '0x006C': dict(symbol='_INITXT', comment='Inicializa VDP em modo texto 40x24'),
    # '0x006F': dict(symbol='_INIT32', comment='Inicializa VDP em modo texto 32x24'),
    # '0x0072': dict(symbol='_INIGRP', comment='Inicializa VDP em modo gráfico 256x192'),
    # '0x0075': dict(symbol='_INIMLT', comment='Inicializa VDP em modo multicolorido 64x48'),
    # '0x0084': dict(symbol='_CALPAT', comment='Calcula endereço da imagem do sprite'),
    # '0x0087': dict(symbol='_CALATR', comment='Calcula endereço do atributo do sprite'),
    # '0x008A': dict(symbol='_GSPSIZ', comment='Obtém tamanho do sprite'),
    # '0x008D': dict(symbol='_GRPPRT', comment='Escreve caractere na tela gráfica'),
    # '0x0090': dict(symbol='_GICINI', comment='Inicializa PSG'),
    # '0x0093': dict(symbol='_WRTPSG', comment='Escreve em registrador do PSG'),
    # '0x0096': dict(symbol='_RDPSG',  comment='Lê registrador do PSG'),
    # '0x0099': dict(symbol='_STRTMS', comment='Desempilha fila musical'),
    # '0x009C': dict(symbol='_CHSNS',  comment='Verifica buffer do teclado'),
    # '0x009F': dict(symbol='_CHGET',  comment='Obtém caractere do buffer do teclado'),
    # '0x00A2': dict(symbol='_CHPUT',  comment='Escreve caractere na tela'),
    # '0x00A5': dict(symbol='_LPTOUT', comment='Imprime caractere na porta de impressora'),
    # '0x00A8': dict(symbol='_LPTSTT', comment='Teste de status da impressora'),
    # '0x00AE': dict(symbol='_PINLIN', comment='Lê uma linha do console'),
    # '0x00B1': dict(symbol='_INLIN',  comment='Lê uma linha do console'),
    # '0x00B4': dict(symbol='_QINLIN', comment='Lê uma linha do console'),
    # '0x00B7': dict(symbol='_BREAKX', comment='Verifica Ctrl+Stop'),
    # '0x00C0': dict(symbol='_BEEP',   comment='Emite beep'),
    # '0x00C3': dict(symbol='_CLS',    comment='Limpa tela'),
    # '0x00C6': dict(symbol='_POSIT',  comment='Posiciona cursor'),
    # '0x00CC': dict(symbol='_ERAFNK', comment='Apaga a linha das teclas de função'),
    # '0x00CF': dict(symbol='_DSPFNK', comment='Mostra a linha das teclas de função'),
    # '0x00D2': dict(symbol='_TOTEXT', comment='Retorna VDP ao modo texto'),
    # '0x00D5': dict(symbol='_GTSTCK', comment='Lê status do joystick'),
    # '0x00D8': dict(symbol='_GTTRIG', comment='Lê status do botão do joystick'),
    # '0x00DB': dict(symbol='_GTPAD',  comment='Lê status do tablet'),
    # '0x00DE': dict(symbol='_GTPDL',  comment='Lê status do paddle'),
    # '0x00E1': dict(symbol='_TAPION', comment='Aciona entrada de fita'),
    # '0x00E4': dict(symbol='_TAPIN',  comment='Lê entrada de fita'),
    # '0x00E7': dict(symbol='_TAPIOF', comment='Desliga entrada de fita'),
    # '0x00EA': dict(symbol='_TAPOON', comment='Aciona saída de fita'),
    # '0x00ED': dict(symbol='_TAPOUT', comment='Escreve na saída de fita'),
    # '0x00F0': dict(symbol='_TAPOOF', comment='Desliga saída de fita'),
    # '0x00F3': dict(symbol='_STMOTR', comment='Controla motor da unidade de fita'),
    # '0x00F6': dict(symbol='_LFTQ',   comment='Verifica espaço em fila musical'),
    # '0x00F9': dict(symbol='_PUTQ',   comment='Coloca byte em fila musical'),
    # '0x00FC': dict(symbol='_RIGHTC', comment='Move endereço de pixel à direita'),
    # '0x00FF': dict(symbol='_LEFTC',  comment='Move endereço de pixel à esquerda'),
    # '0x0102': dict(symbol='UPC',    comment='Move endereço de pixel acima'),
    # '0x0105': dict(symbol='TUPC',   comment='Testa e move endereço de pixel acima'),
    # '0x0108': dict(symbol='DOWNC',  comment='Move endereço de pixel abaixo'),
    # '0x010B': dict(symbol='TDOWNC', comment='Testa e Move endereço de pixel abaixo'),
    # '0x010E': dict(symbol='SCALXY', comment='"Clipa" coordenadas gráficas'),
    # '0x0111': dict(symbol='MAPXYC', comment='Converte coordenadas do modo gráfico'),
    # '0x0114': dict(symbol='FETCHC', comment='Obtém endereço físico do pixel atual'),
    # '0x0117': dict(symbol='STOREC', comment='Armazena endereço físico do pixel atual'),
    # '0x011A': dict(symbol='SETATR', comment='Muda cor de desenho'),
    # '0x011D': dict(symbol='READC',  comment='Lê atributo do pixel atual'),
    # '0x0120': dict(symbol='SETC',   comment='Muda atributo do pixel atual'),
    # '0x0123': dict(symbol='NSETCX', comment='Muda atributo de uma sequência de pixels'),
    # '0x0132': dict(symbol='CHGCAP', comment='Altera LED do CAPS LOCK'),
    # '0x0135': dict(symbol='CHGSND', comment='Altera o estado do click do teclado'),
    # '0x0138': dict(symbol='RSLREG', comment='Lê registrador do slot primário'),
    # '0x013B': dict(symbol='WSLREG', comment='Escreve registrador do slot primário'),
    # '0x013E': dict(symbol='RDVDP',  comment='Lê registrador de status do VDP'),
    # '0x0141': dict(symbol='SNSMAT', comment='Lê linha da matriz de teclado'),
    # '0x0156': dict(symbol='KILBUF', comment='Limpa buffer do teclado'),
    # '0x0159': dict(symbol='CALBAS', comment='Chama rotina BASIC a partir de qualquer slot'),

    '0x1398': dict(symbol='NMI',    comment='Handler of non-maskarable interrupt'),
    '0x06A8': dict(symbol='CLRSPR', comment='Init sprite data'),
    '0x050E': dict(symbol='INITXT', comment='Init VDP for 40 x 24 text mode (SCREEN 0)'),
    '0x0538': dict(symbol='INIT32', comment='Init VDP for 32 x 24 text mode (SCREEN 1)'),
    '0x05D2': dict(symbol='INIGRP', comment='Init VDP for high resolution mode (SCREEN 2)'),
    '0x061F': dict(symbol='INIMLT', comment='Init VDP for multi color mode (SCREEN 3)'),
    '0x0594': dict(symbol='SETTXT', comment='Set VDP display 40 x 24 text mode'),
    '0x05B4': dict(symbol='SETT32', comment='Set VDP display 32 x 24 text mode'),
    '0x0602': dict(symbol='SETGRO', comment='Set VDP display high resolution mode'),
    '0x0659': dict(symbol='SETMLT', comment='Set VDP display multi color mode'),
    '0x06E4': dict(symbol='CALPAT', comment='Get address of sprite pattern table'),
    '0x06F9': dict(symbol='CALATR', comment='Get address of sprite attribute table'),
    '0x0704': dict(symbol='GSPSIZ', comment='Return current sprite size'),
    '0x1510': dict(symbol='GRPPRT', comment='Print a char on the graphic screen'),
    
    '0x04BD': dict(symbol='GICINI', comment='Init PSG and static data for PLAY'),
    '0x1102': dict(symbol='WRTPSG', comment='Write data to PSG'),
    '0x110E': dict(symbol='RDPSG',  comment='Read data from PSG'),
    '0x11C4': dict(symbol='STRTMS', comment='Check and start bg task for PLAY'),

    '0x0D6A': dict(symbol='CHSNS',  comment='Check keyboard status'),
    '0x10CB': dict(symbol='CHGET',  comment='Return char typed, with wait'),
    '0x08BC': dict(symbol='CHPUT',  comment='Output character to console'),
    '0x085D': dict(symbol='LPTOUT', comment='Output character to printer, if possible'),
    '0x0884': dict(symbol='LPTSTT', comment='Check status of line printer'),
    '0x089D': dict(symbol='CNVCHR', comment='Check for graphic header byte and convert code'),
    '0x23BF': dict(symbol='PINLIN', comment='Read line from keyboard to buffer'),
    '0x23D5': dict(symbol='INLIN',  comment='Same as above, except in case of AUTFLG is set'),
    '0x23CC': dict(symbol='QINLIN', comment='Print a "?", then jump to INLIN'),
    '0x046F': dict(symbol='BREAKX', comment='[CTRL+STOP] pressed?'),
    '0x03FB': dict(symbol='ISCNTC', comment='[SHIFT+STOP] pressed?'),
    '0x10F9': dict(symbol='CKCNTC', comment='Same as ISCNTC, but used by BASIC'),
    '0x1113': dict(symbol='BEEP',   comment='Buzz'),
    '0x0848': dict(symbol='CLS',    comment='Clear screen'),
    '0x088E': dict(symbol='POSIT',  comment='Place cursor at column [H], row [L]'),
    '0x0B26': dict(symbol='FNKSB',  comment='Display function keys, if necessary'),
    '0x0B15': dict(symbol='ERAFNK', comment='Stop displaying the function keys'),
    '0x0B2B': dict(symbol='DSPFNK', comment='Enable funcion keys display'),
    '0x083B': dict(symbol='TOTEXT', comment='Force screen to text mode'),

    '0x11EE': dict(symbol='GTSTCK', comment=''),
    '0x1253': dict(symbol='GTTRIG', comment=''),
    '0x12AC': dict(symbol='GTPAD', comment=''),
    '0x1273': dict(symbol='GTPDL', comment=''),

    '0x1A63': dict(symbol='TAPION', comment=''),
    '0x1ABC': dict(symbol='TAPIN', comment=''),
    '0x19E9': dict(symbol='TAPIOF', comment=''),
    '0x19F1': dict(symbol='TAPOON', comment=''),
    '0x1A19': dict(symbol='TAPOUT', comment=''),
    '0x19DD': dict(symbol='TAPOFF', comment=''),
    '0x1384': dict(symbol='STMOTR', comment=''),
    '0x14EB': dict(symbol='LFTQ', comment=''),
    '0x1492': dict(symbol='PUTQ', comment=''),

    '0x146A': dict(symbol='DCOMPR', comment=None),
    '0x1B45': dict(symbol='OUTDO', comment='Output a char to the console or printer'),
    '0x1BBF': dict(symbol='CGTABL', comment='Address of character generator table to allow use of other character ROM'),
    '0x2683': dict(symbol='SYNCHR', comment=None),
    '0x2686': dict(symbol='CHRGTR', comment=None),
    '0x2689': dict(symbol='GETYPR', comment=None),
    }


msx1bios_sysvars = {
    '0xF380': dict(symbol='RAMLOW',  comment=None),
    '0xF381': dict(symbol='RAMLOW+1',comment=None),
    '0xF385': dict(symbol='WRPRIM',  comment=None),
    '0xF38C': dict(symbol='CLPRIM',  comment=None),
    '0xF39A': dict(symbol='USRTAB0', comment='Endereço da função USR0'),
    '0xF39C': dict(symbol='USRTAB1', comment='Endereço da função USR1'),
    '0xF39E': dict(symbol='USRTAB2', comment='Endereço da função USR2'),
    '0xF3A0': dict(symbol='USRTAB3', comment='Endereço da função USR3'),
    '0xF3A2': dict(symbol='USRTAB4', comment='Endereço da função USR4'),
    '0xF3A4': dict(symbol='USRTAB5', comment='Endereço da função USR5'),
    '0xF3A6': dict(symbol='USRTAB6', comment='Endereço da função USR6'),
    '0xF3A8': dict(symbol='USRTAB7', comment='Endereço da função USR7'),
    '0xF3AA': dict(symbol='USRTAB8', comment='Endereço da função USR8'),
    '0xF3AC': dict(symbol='USRTAB9', comment='Endereço da função USR9'),
    '0xF3AE': dict(symbol='LINL40',  comment='Largura da screen 0 (comando WIDTH)'),
    '0xF3AF': dict(symbol='LINL32',  comment='Largura da screen 1 (comando WIDTH)'),
    '0xF3B0': dict(symbol='LINLEN',  comment='Largura do modo de texto atual'),
    '0xF3B1': dict(symbol='CRTCNT',  comment='Número de linhas nos modos texto'),
    '0xF3B3': dict(symbol='TXTNAM',  comment='Modo texto 40*24: Base da tabela de nomes'),
    '0xF3B5': dict(symbol='TXTCOL',  comment='Modo texto 40*24: Base da tabela de cores'),
    '0xF3B7': dict(symbol='TXTCGP',  comment='Modo texto 40*24: Base da tabela de caracteres'),
    '0xF3B9': dict(symbol='TXTATR',  comment='Modo texto 40*24: Base dos atributos de sprite'),
    '0xF3BB': dict(symbol='TXTPAT',  comment='Modo texto 40*24: Base das imagens de sprite'),
    '0xF3BD': dict(symbol='T32NAM',  comment='Modo texto 32*24: Base da tabela de nomes'),
    '0xF3BF': dict(symbol='T32COL',  comment='Modo texto 32*24: Base da tabela de cores'),
    '0xF3C1': dict(symbol='T32CGP',  comment='Modo texto 32*24: Base da tabela de caracteres'),
    '0xF3C3': dict(symbol='T32ATR',  comment='Modo texto 32*24: Base dos atributos de sprite'),
    '0xF3C5': dict(symbol='T32PAT',  comment='Modo texto 32*24: Base das imagens de sprite'),
    '0xF3C7': dict(symbol='GRPNAM',  comment='Modo gráfico 256*192: Base da tabela de nomes'),
    '0xF3C9': dict(symbol='GRPCOL',  comment='Modo gráfico 256*192: Base da tabela de cores'),
    '0xF3CB': dict(symbol='GRPCGP',  comment='Modo gráfico 256*192: Base da tabela de caracteres'),
    '0xF3CD': dict(symbol='GRPATR',  comment='Modo gráfico 256*192: Base dos atributos de sprite'),
    '0xF3CF': dict(symbol='GRPPAT',  comment='Modo gráfico 256*192: Base das imagens de sprite'),
    '0xF3D1': dict(symbol='MLTNAM',  comment='Modo gráfico 64*48: Base da tabela de nomes'),
    '0xF3D3': dict(symbol='MLTCOL',  comment='Modo gráfico 64*48: Base da tabela de cores'),
    '0xF3D5': dict(symbol='MLTCGP',  comment='Modo gráfico 64*48: Base da tabela de caracteres'),
    '0xF3D7': dict(symbol='MLTATR',  comment='Modo gráfico 64*48: Base dos atributos de sprite'),
    '0xF3D9': dict(symbol='MLTPAT',  comment='Modo gráfico 64*48: Base das imagens de sprite'),
    '0xF3DB': dict(symbol='CLIKSW',  comment='Click do teclado: 0=desligado, 1-255: ligado'),
    '0xF3DC': dict(symbol='CSRY',    comment='Coordenada Y do cursor em modo texto (1...CRTCNT)'),
    '0xF3DD': dict(symbol='CSRX',    comment='Coordenada X do cursor em modo texto (1...LINLEN)'),
    '0xF3DE': dict(symbol='CONSDFG', comment='Apresentação das teclas de função: 0=desligado'),
    '0xF3DF': dict(symbol='RG0SAV',  comment='Cópia dos registrador 0 do VDP (somente escrita)'),
    '0xF3E0': dict(symbol='RG1SAV',  comment='Cópia dos registrador 1 do VDP (somente escrita)'),
    '0xF3E1': dict(symbol='RG2SAV',  comment='Cópia dos registrador 2 do VDP (somente escrita)'),
    '0xF3E2': dict(symbol='RG3SAV',  comment='Cópia dos registrador 3 do VDP (somente escrita)'),
    '0xF3E3': dict(symbol='RG4SAV',  comment='Cópia dos registrador 4 do VDP (somente escrita)'),
    '0xF3E4': dict(symbol='RG5SAV',  comment='Cópia dos registrador 5 do VDP (somente escrita)'),
    '0xF3E5': dict(symbol='RG6SAV',  comment='Cópia dos registrador 6 do VDP (somente escrita)'),
    '0xF3E6': dict(symbol='RG7SAV',  comment='Cópia dos registrador 7 do VDP (somente escrita)'),
    '0xF3E7': dict(symbol='STATFL',  comment='Cópia do registrador de status do VDP'),
    '0xF3E8': dict(symbol='TRGFLG',  comment='Estado dos botões joysticks e da barra de espaço'),
    '0xF3E9': dict(symbol='FORCLR',  comment='Cor do primeiro plano'),
    '0xF3EA': dict(symbol='BAKCLR',  comment='Cor do segundo plano (fundo)'),
    '0xF3EB': dict(symbol='BDRCLR',  comment='Cor da borda'),
    '0xF3EC': dict(symbol='MAXUPD',  comment='(Código automodificável usado para traçar retas)'),
    '0xF3EF': dict(symbol='MINUPD',  comment='(Código automodificável usado para traçar retas)'),
    '0xF3F2': dict(symbol='ATRBYT',  comment='Cor da tinta gráfica em funções gráficas da BIOS'),
    '0xF3F3': dict(symbol='QUEUES',  comment='endereço do bloco de controle das filas musicais'),
    '0xF3F5': dict(symbol='FRCNEW',  comment='Indicador que distingue CLOAD (0) de CLOAD? (255)'),
    '0xF3F6': dict(symbol='SCNCNT',  comment='Contador controlar a freq das varreduras do teclado'),
    '0xF3F7': dict(symbol='REPCNT',  comment='Contador número de repetições de uma tecla'),
    '0xF3F8': dict(symbol='PUTPNT',  comment='Endereço de inserção em KEYBUF (buffer circular)'),
    '0xF3FA': dict(symbol='GETPNT',  comment='Endereço de remoção em KEYBUF (buffer circular)'),
    '0xF3FC': dict(symbol='CS1200',  comment='Parâmetros do cassete para 1200 baud'),
    '0xF401': dict(symbol='CS2400',  comment='Parâmetros do cassete para 2400 baud'),
    '0xF406': dict(symbol='CASLOW',  comment='Parâmetros do cassete atuais: ciclo LO'),
    '0xF408': dict(symbol='CASHIGH', comment='Parâmetros do cassete atuais: ciclo HI'),
    '0xF40A': dict(symbol='HEADER',  comment='Parâmetros do cassete atuais: ciclos no cabeçalho'),
    '0xF40B': dict(symbol='ASPCT1',  comment='Inverso da razão de aspecto do CIRCLE*256'),
    '0xF40D': dict(symbol='ASPCT2',  comment='Razão de aspecto do CIRCLE*256'),
    '0xF40F': dict(symbol='ENDPRG',  comment='Usado pelo interpretador BASIC para ON ERROR GOTO'),
    '0xF414': dict(symbol='ERRFLG',  comment='Armazena o código de erro do BASIC'),
    '0xF415': dict(symbol='LPTPOS',  comment='LPRINT, armazena posição da cabeça de impressão'),
    '0xF416': dict(symbol='PRTFLG',  comment='OUTDO saida para a tela(0) ou impressora (1)'),
    '0xF417': dict(symbol='NTMSXP',  comment='conversão OUTDO (0=sem conversão, 1-255=espaços)'),
    '0xF418': dict(symbol='RAWPRT',  comment='OUTDO: 0=prefixos gráficos,1=envia sem tratamento'),
    '0xF419': dict(symbol='VLZADR',  comment='Temporário usado pela função VAL do BASIC'),
    '0xF41B': dict(symbol='VLZDAT',  comment='Temporário usado pela função VAL do BASIC'),
    '0xF41E': dict(symbol='KBFMIN',  comment='Utilizado no tratamento de erros do BASIC'),
    '0xF41F': dict(symbol='KBUF',    comment='Utilizado no tratamento de erros do BASIC (318)'),
    '0xF55D': dict(symbol='BUFMIN',  comment='Utilizado na entrada de linhas BASIC'),
    '0xF55E': dict(symbol='BUF',     comment='Utilizado na entrada de linhas BASIC (259)'),
    '0xF661': dict(symbol='TTYPOS',  comment='Posição de tela atual, usada pelo PRINT'),
    '0xF662': dict(symbol='DIMFLG',  comment='Usado pelo interpretador BASIC na instrução DIM'),
    '0xF663': dict(symbol='VALTYP',  comment='Usado pelo interpretador BASIC'),
    '0xF664': dict(symbol='DORES',   comment='Usada pelo interpretador BASIC (linhas DATA)'),
    '0xF665': dict(symbol='DONUM',   comment='Usada pelo interpretador BASIC'),
    '0xF666': dict(symbol='CONTXT',  comment='Usada pelo interpretador BASIC'),
    '0xF668': dict(symbol='CONSAV',  comment='Usada pelo interpretador BASIC'),
    '0xF669': dict(symbol='CONTYP',  comment='Usada pelo interpretador BASIC'),
    '0xF66A': dict(symbol='CONLO',   comment='Usada pelo interpretador BASIC'),
    '0xF674': dict(symbol='STKTOP',  comment='Contém o endereço do topo da pilha'),
    '0xF676': dict(symbol='TXTTAB',  comment='Contém o endereço do texto de programa BASIC'),
    '0xF678': dict(symbol='TEMPPT',  comment='Aponta para a próxima entrada livre de TEMPST'),
    '0xF67A': dict(symbol='TEMPST',  comment='Buffer de descritores de string (BASIC)'),
    '0xF698': dict(symbol='DSCTMP',  comment='Buffer temporário para funções de string (BASIC)'),
    '0xF69B': dict(symbol='FRETOP',  comment='próxima posição livre no buffer a partit de MEMSIZ'),
    '0xF69D': dict(symbol='TEMP3',   comment='Variável temporária (interpretador BASIC)'),
    '0xF69F': dict(symbol='TEMP8',   comment='Variável temporária (interpretador BASIC)'),
    '0xF6A1': dict(symbol='ENDFOR',  comment='Usada pelo interpretador BASIC (loops FOR)'),
    '0xF6A3': dict(symbol='DATLIN',  comment='Linha do programa BASIC do item DATA atual'),
    '0xF6A5': dict(symbol='SUBFLG',  comment='Usada pelo interpretador BASIC'),
    '0xF6A6': dict(symbol='FLGINP',  comment='BASIC: distingue INPUT (0) de READ (1-255)'),
    '0xF6A7': dict(symbol='TEMP',    comment='Variável temporária (interpretador BASIC)'),
    '0xF6A9': dict(symbol='PTRFLG',  comment='Usada pelo interpretador BASIC'),
    '0xF6AA': dict(symbol='AUTFLG',  comment='Flag do modo AUTO do BASIC'),
    '0xF6AB': dict(symbol='AUTLIN',  comment='Número da linha AUTO atual (BASIC)'),
    '0xF6AD': dict(symbol='AUTINC',  comment='Incremento atual do AUTO (BASIC)'),
    '0xF6AF': dict(symbol='SAVTXT',  comment='Usado pelo manipulador de erro (BASIC)'),
    '0xF6B3': dict(symbol='ERRLIN',  comment='Número da linha que gerou o erro (BASIC)'),
    '0xF6B5': dict(symbol='DOT',     comment='Usada pelo interpretador BASIC'),
    '0xF6B7': dict(symbol='ERRTXT',  comment='Usada pelo interpretador BASIC (RESUME)'),
    '0xF6B9': dict(symbol='ONELIN',  comment='Usada pelo interpretador BASIC (ON ERROR GOTO)'),
    '0xF6BB': dict(symbol='ONEFLG',  comment='Usada pelo interpretador BASIC (ON ERROR GOTO)'),
    '0xF6BC': dict(symbol='TEMP2',   comment='Variável temporária (interpretador BASIC)'),
    '0xF6BE': dict(symbol='OLDLIN',  comment='Linha que terminou o programa BASIC, usada por CONT'),
    '0xF6C0': dict(symbol='OLDTXT',  comment='Aponta a instrução que terminou o programa'),
    '0xF6C2': dict(symbol='VARTAB',  comment='área de armazenamento de variáveis (BASIC)'),
    '0xF6C4': dict(symbol='ARYTAB',  comment='área de armazenamente de arrays (BASIC)'),
    '0xF6C6': dict(symbol='STREND',  comment='byte seguinte à área de ARYTAB (BASIC)'),
    '0xF6C8': dict(symbol='DATPTR',  comment='Aponta para item DATA atual (BASIC)'),
    '0xF6CA': dict(symbol='DEFTBL',  comment='Tp de variavel,por letra (BASIC),DEFINT,DEFSTR,...'),
    '0xF6E4': dict(symbol='PRMSTK',  comment='Usada pelo interpretador BASIC'),
    '0xF6E6': dict(symbol='PRMLEN',  comment='Usada pelo interpretador BASIC'),
    '0xF6E8': dict(symbol='PARM1',   comment='Usada pelo interpretador BASIC (buffer do FN)'),
    '0xF74C': dict(symbol='PRMPRV',  comment='Usada pelo interpretador BASIC (FN)'),
    '0xF74E': dict(symbol='PRMLN2',  comment='Usada pelo interpretador BASIC (FN)'),
    '0xF750': dict(symbol='PARM2',   comment='Usada pelo interpretador BASIC (buffer do FN)'),
    '0xF7B4': dict(symbol='PRMFLG',  comment='Usada pelo interpretador BASIC'),
    '0xF7B5': dict(symbol='ARYTA2',  comment='Usada pelo interpretador BASIC'),
    '0xF7B7': dict(symbol='NOFUNS',  comment='Usada pelo interpretador BASIC'),
    '0xF7B8': dict(symbol='TEMP9',   comment='Variável temporária (interpretador BASIC)'),
    '0xF7BA': dict(symbol='FUNACT',  comment='Usada pelo interpretador BASIC'),
    '0xF7BC': dict(symbol='SWPTMP',  comment='Usada pelo interpretador BASIC (SWAP)'),
    '0xF7C4': dict(symbol='TRCFLG',  comment='Ativado quando TRON está ligado (BASIC)'),
    '0xF7C5': dict(symbol='FBUFFR',  comment='Buffer de conversão numérica (BASIC)'),
    '0xF7F2': dict(symbol='DECTM2',  comment='Variável temporária (interpretador BASIC)'),
    '0xF7F4': dict(symbol='DECCNT',  comment='Variável temporária (interpretador BASIC)'),
    '0xF7F6': dict(symbol='DAC',     comment='Buffer de avaliação de expressão do BASIC'),
    '0xF7F8': dict(symbol='ARGUSR',  comment='?'),
    '0xF806': dict(symbol='HOLD8',   comment='Buffer temporário de multiplicação (BASIC)'),
    '0xF847': dict(symbol='ARG',     comment='Buffer de avaliação de expressão do BASIC'),
    '0xF857': dict(symbol='RNDX',    comment='Contém o último número aleatório (precisão dupla)'),
    '0xF85F': dict(symbol='MAXFIL',  comment='Número de buffers de E/S alocados (BASIC)'),
    '0xF860': dict(symbol='FILTAB',  comment='Aponta tabela de FCBs dos buffers de E/S (BASIC)'),
    '0xF862': dict(symbol='NULBUF',  comment='Aponta para o buffer de E/S'),
    '0xF864': dict(symbol='PTRFIL',  comment='Aponta para o FCB do buffer de E/S ativo'),
    '0xF866': dict(symbol='FILNAM',  comment='Buffer de nome de arquivo. (BASIC)'),
    '0xF871': dict(symbol='FILNM2',  comment='Buffer de nome de arquivo. (BASIC)'),
    '0xF87C': dict(symbol='NLONLY',  comment='Usada pelo interpretador BASIC'),
    '0xF87D': dict(symbol='SAVEND',  comment='Usada pelo interpretador BASIC'),
    '0xF87F': dict(symbol='FNKSTR',  comment='Buffer com strings das teclas de função'),
    '0xF91F': dict(symbol='CGPNT',   comment='Tabela de caract. em ROM (Slot ID 0,endereço 0x1BBF)'),
    '0xF922': dict(symbol='NAMBAS',  comment='Base da tabela de nomes no modo de video atual'),
    '0xF924': dict(symbol='CGPBAS',  comment='Base da tabela de caracteres no modo de video atual'),
    '0xF926': dict(symbol='PATBAS',  comment='Base da tabela de imagens de sprites no modo de video atual'),
    '0xF928': dict(symbol='ATRBAS',  comment='Base da tabela de atributos de sprites no modo de ví deo atual'),
    '0xF92A': dict(symbol='CLOC',    comment='Endereço do pixel atual (funções gráficas da BIOS)'),
    '0xF92C': dict(symbol='CMASK',   comment='Máscara do pixel atual'),
    '0xF92D': dict(symbol='MINDEL',  comment='Usado pela instrução LINE'),
    '0xF92F': dict(symbol='MAXDEL',  comment='Usado pela instrução LINE'),
    '0xF931': dict(symbol='ASPECT',  comment='Usado pela instrução CIRCLE'),
    '0xF933': dict(symbol='CENCNT',  comment='Usado pela instrução CIRCLE'),
    '0xF935': dict(symbol='CLINEF',  comment='Usado pela instrução CIRCLE'),
    '0xF936': dict(symbol='CNPNTS',  comment='Usado pela instrução CIRCLE'),
    '0xF938': dict(symbol='CPLOTF',  comment='Usado pela instrução CIRCLE'),
    '0xF939': dict(symbol='CPCNT',   comment='Usado pela instrução CIRCLE'),
    '0xF93B': dict(symbol='CPCNT8',  comment='Usado pela instrução CIRCLE'),
    '0xF93D': dict(symbol='CRCSUM',  comment='Usado pela instrução CIRCLE'),
    '0xF93F': dict(symbol='CSTCNT',  comment='Usado pela instrução CIRCLE'),
    '0xF941': dict(symbol='CSCLXY',  comment='Usado pela instrução CIRCLE'),
    '0xF942': dict(symbol='CSAVEA',  comment='Temporário usado por funções gráficas da BIOS'),
    '0xF944': dict(symbol='CSAVEM',  comment='Temporário usado por funções gráficas da BIOS'),
    '0xF945': dict(symbol='CXOFF',   comment='Usado pela instrução CIRCLE'),
    '0xF947': dict(symbol='CYOFF',   comment='Usado pela instrução CIRCLE'),
    '0xF949': dict(symbol='LOHMSK',  comment='Usado pela instrução PAINT'),
    '0xF94A': dict(symbol='LOHDIR',  comment='Usado pela instrução PAINT'),
    '0xF94B': dict(symbol='LOHADR',  comment='Usado pela instrução PAINT'),
    '0xF94D': dict(symbol='LOHCNT',  comment='Usado pela instrução PAINT'),
    '0xF94F': dict(symbol='SKPCNT',  comment='Usado pela instrução PAINT'),
    '0xF951': dict(symbol='MOVCNT',  comment='Usado pela instrução PAINT'),
    '0xF953': dict(symbol='PDIREC',  comment='Usado pela instrução PAINT'),
    '0xF954': dict(symbol='LEPROG',  comment='Usado pela instrução PAINT'),
    '0xF955': dict(symbol='RTPROG',  comment='Usado pela instrução PAINT'),
    '0xF958': dict(symbol='MCLFLG',  comment='Linguagem de macro atual, 0=DRAW, 1-255=PLAY'),
    '0xF959': dict(symbol='QUETAB',  comment='Blocos de controle das filas musicais'),
    '0xF971': dict(symbol='QUEBAK',  comment='Usado pelo manipulador de fila musical'),
    '0xF975': dict(symbol='VOICAQ',  comment='Buffer da fila musical A'),
    '0xF9F5': dict(symbol='VOICBQ',  comment='Buffer da fila musical B'),
    '0xFA75': dict(symbol='VOICCQ',  comment='Buffer da fila musical C'),
    '0xFAF5': dict(symbol='RS2IQ',   comment='Buffer da fila RS232'),
    '0xFB35': dict(symbol='PRSCNT',  comment='Usado pelo interpretador BASIC (PLAY)'),
    '0xFB36': dict(symbol='SAVSP',   comment='Usado pelo interpretador BASIC (PLAY)'),
    '0xFB38': dict(symbol='VOICEN',  comment='Voz atual do interpretador PLAY'),
    '0xFB39': dict(symbol='SAVVOL',  comment='Usado pelo interpretador BASIC (PLAY)'),
    '0xFB3B': dict(symbol='MCLLEN',  comment='Comprimento do operando de macro-linguagem analisado'),
    '0xFB3C': dict(symbol='MCLPTR',  comment='Aponta para caractere de macro-linguagem sendo analisado'),
    '0xFB3E': dict(symbol='QUEUEN',  comment='Fila atual do interpretador PLAY'),
    '0xFB3F': dict(symbol='MUSICF',  comment='Usado pelo interpretador BASIC (PLAY)'),
    '0xFB40': dict(symbol='PLACNT',  comment='Usado pelo interpretador BASIC (PLAY)'),
    '0xFB41': dict(symbol='VCBA',    comment='Buffer com parâmetros da voz A do PLAY'),
    '0xFB66': dict(symbol='VCBB',    comment='Buffer com parâmetros da voz B do PLAY'),
    '0xFB8B': dict(symbol='VCBC',    comment='Buffer com parâmetros da voz C do PLAY'),
    '0xFBB0': dict(symbol='ENSTOP',  comment='Se diferente de 0, faz warm boot quando CODE+GRAPH+CTRL+SHIFT forem pressionadas'),
    '0xFBB1': dict(symbol='BASROM',  comment='Ativa (0) ou desativa (1-255) manipulador de CTRL+STOP'),
    '0xFBB2': dict(symbol='LINTTB',  comment='Variável interna de funções da BIOS'),
    '0xFBCA': dict(symbol='FSTPOS',  comment='Usada internamente pelo editor de tela do BASIC'),
    '0xFBCC': dict(symbol='CURSAV',  comment='Armazena o caractere sob o cursor'),
    '0xFBCD': dict(symbol='FNKSWI',  comment='Usada pela rotina CHSNS para determinar se SHIFT está pressionado (0) ou não (1) para apresentar as strings das teclas de função'),
    '0xFBCE': dict(symbol='FNKFLG',  comment='Usada pelo BASIC. (indicadores de KEY(n) ON)'),
    '0xFBD8': dict(symbol='ONGSBF',  comment='Usado pelo interpretador BASIC'),
    '0xFBDA': dict(symbol='OLDKEY',  comment='Armazena o estado anterior da matriz de teclado'),
    '0xFBE5': dict(symbol='NEWKEY',  comment='Armazena o estado atual da matriz de teclado'),
    '0xFBF0': dict(symbol='KEYBUF',  comment='Buffer circular do teclado (caracteres decodificados)'),
    '0xFC18': dict(symbol='LINWRK',  comment='Buffer de linha de tela, usado pelo BIOS'),
    '0xFC40': dict(symbol='PATWRK',  comment='Buffer usado pelo BIOS'),
    '0xFC48': dict(symbol='BOTTOM',  comment='Armazena o início da RAM usada pelo interpretador BASIC'),
    '0xFC4C': dict(symbol='TRPTBL',  comment='Usado pelas instruções de interrupção (ON...) do BASIC'),
    '0xFC9A': dict(symbol='RTYCNT',  comment='Não-utilizada'),
    '0xFC9B': dict(symbol='INTFLG',  comment='Flag de detecção de CTRL-STOP (3) e STOP (4)'),
    '0xFC9C': dict(symbol='PADY',    comment='Última coordenada Y do tablet'),
    '0xFC9D': dict(symbol='PADX',    comment='Última coordenada X do tablet'),
    '0xFC9E': dict(symbol='JIFFY',   comment='Contador incrementado a cada interrupção do VDP'),
    '0xFCA0': dict(symbol='INTVAL',  comment='Duração do intervalo do ON INTERVAL (BASIC)'),
    '0xFCA2': dict(symbol='INTCNT',  comment='Contador do ON INTERVAL (BASIC)'),
    '0xFCA4': dict(symbol='LOWLIM',  comment='Duração mnima do bit de partida no cassete (TAPION)'),
    '0xFCA5': dict(symbol='WINWID',  comment='Duração de discriminação LO/HI (TAPION)'),
    '0xFCA6': dict(symbol='GRPHED',  comment='Variável auxiliar da rotina CNVCHR do BIOS'),
    '0xFCA7': dict(symbol='ESCCNT',  comment='Variável auxiliar da rotina CHPUT do BIOS'),
    '0xFCA8': dict(symbol='INSFLG',  comment='Indica modo de inserção do editor de tela'),
    '0xFCAA': dict(symbol='CSTYLE',  comment='Estilo do cursor, bloco (0) ou sublinhado (1-255)'),
    '0xFCAB': dict(symbol='CAPST',   comment='Status do CAPS LOCK (0=desligado, 1-255=ligado)'),
    '0xFCAC': dict(symbol='KANAST',  comment='Status do KANA LOCK (0=desligado, 1-255=ligado)'),
    '0xFCAD': dict(symbol='KANAMD',  comment='Modo kana (MSX japoneses)'),
    '0xFCAE': dict(symbol='FLBMEM',  comment='Usada pelo manipulador de erro de E/S'),
    '0xFCAF': dict(symbol='SCRMOD',  comment='Modo de tela (SCREEN) atual'),
    '0xFCB0': dict(symbol='OLDSCR',  comment='último modo de texto'),
    '0xFCB1': dict(symbol='CASPRV',  comment='Temporário de E/S do cassete'),
    '0xFCB2': dict(symbol='BDRATR',  comment='Usado pelas rotinas gráficas do BIOS'),
    '0xFCB3': dict(symbol='GXPOS',   comment='Temporário das rotinas gráficas do BIOS'),
    '0xFCB5': dict(symbol='GYPOS',   comment='Temporário das rotinas gráficas do BIOS'),
    '0xFCB7': dict(symbol='GRPACX',  comment='Temporário das rotinas gráficas do BIOS'),
    '0xFCB9': dict(symbol='GRPACY',  comment='Temporário das rotinas gráficas do BIOS'),
    '0xFCBB': dict(symbol='DRWFLG',  comment='Usado pelo manipulador do DRAW'),
    '0xFCBC': dict(symbol='DRWSCL',  comment='Usado pelo manipulador do DRAW'),
    '0xFCBD': dict(symbol='DRWANG',  comment='Usado pelo manipulador do DRAW'),
    '0xFCBE': dict(symbol='RUNBNF',  comment='Usado pelo manipulador do BLOAD'),
    '0xFCBF': dict(symbol='SAVENT',  comment='Usado pelo manipulador do BLOAD'),
    '0xFCC1': dict(symbol='EXPTBL',  comment='4 slots, (0x00=não expandido, 0x80=expandido)'),
    '0xFCC4': dict(symbol='EXPTBL+3',comment=None),
    '0xFCC5': dict(symbol='SLTTBL',  comment='Cópia dos registradores de slot primário'),
    '0xFCC7': dict(symbol='SLTTBL+2',comment=None),
    '0xFCC9': dict(symbol='SLTATR',  comment='Atributos de ROM,16 bytes por slot (4 por subslot)'),
    '0xFD09': dict(symbol='SLTWRK',  comment='bytes de trabalho para cada uma das 64 exten. ROM'),
    '0xFD89': dict(symbol='PROCNM',  comment='Buffer dispositivo/instrução analisado ROM de exten.'),
    '0xFD99': dict(symbol='DEVICE',  comment='passar número de dispositivo para ROM extensão.'),
    '0xFCA9': dict(symbol='CSRSW',   comment='Status do cursor (0=desligado, 1-255=ligado?)'),
    }
